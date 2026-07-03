# (C) TimesFM — Deep Dive (v193 wiki)

> **Subject:** `google-research/timesfm` — **TimesFM (Time Series Foundation Model)**, Google Research.
> **What it is:** a *pretrained decoder-only transformer foundation model for time-series **forecasting*** — feed it (almost) any univariate series, get a zero-shot forecast + calibrated prediction intervals, no training.
> **License:** Apache-2.0 (code + checkpoints). README caveat: *"This open version is not an officially supported Google product."*
> **Source-verified** at commit `4a6c5cd` (default branch `master`, 2026-07-02). Repo **~26.5k★ / 2.6k forks, Python 70.8%** (page-stated §37.4 — GitHub API is mocked in this env; treat stars/forks as page-stated, NOT a viral-velocity claim).
> **Paper:** *"A decoder-only foundation model for time-series forecasting"*, arXiv **2310.10688**, ICML 2024. Authors: **Abhimanyu Das, Weihao Kong, Rajat Sen, Yichen Zhou** (+ Petros Mol, Michael Chertushkin in `pyproject`) — Google Research.
>
> ⚠️ **Honest framing up front:** TimesFM's *domain* — time-series forecasting — is **off your Goal #1** ("master Claude + autonomous agents for software development"). It is not Claude, not an agent, not agent infrastructure, not a coding tool. It's the **GLM-5 v176 / DeepSpec v186 situation**: a Google model that is *goal-adjacent*, built at operator request. BUT there are **two real on-goal bridges** (below) and a **sharp Goal-#2 (hireui) payoff** — recruitment forecasting — which is where the pilot value actually is. See the Verdict + Pilot docs.

---

## 1. The one-paragraph mental model

Large-language-model pretraining, transplanted to numbers-over-time. Instead of pretraining a decoder-only transformer on internet text and getting zero-shot text generation, TimesFM pretrains one on ~100 billion time-points (Wikipedia pageviews, Google Trends, synthetic series) and gets **zero-shot forecasting**: it will forecast a series it has never seen, competitively with models *trained specifically on that series*. The trick that makes it work on numbers is **patching** — a window of the series is chopped into fixed-size chunks ("patches") that play the role of tokens, and the model predicts the next chunk. That's it. Everything else (quantiles, covariates, long context) is engineering on top.

---

## 2. The two on-goal bridges (why this isn't purely off-goal)

1. **It ships a first-party Claude Code Agent Skill.** The repo contains `AGENTS.md` (an "Agent Entry Point") + `timesfm-forecasting/SKILL.md` — a genuine, well-built **Agent Skill** installable via `cp -r timesfm-forecasting/ ~/.claude/skills/`, auto-discovered by any agent supporting the open **agentskills.io** standard (Claude Code / Cursor / OpenCode / Codex). Authored by community contributor **Clayton Young (@borealBytes)**. This lands squarely on the agent-skills substrate the vault already studies (agent-skills-standard v76, SkillOpt v178, agent-skills v184, ponytail v168). *(Sharp cross-ref: this is the same meta-move as v192 palmier-pro — a product/model retrofitted to be **agent-native** via a first-party agent interface. palmier-pro bolted on an MCP server; TimesFM bolts on an Agent Skill + a Vertex "dockerized endpoint for agentic calling.")*
2. **The realistic way to USE it is agent-orchestrated.** TimesFM is *not* a tool an agent "calls" like a calculator. The realistic pattern is: **Claude Code orchestrates the forecasting pipeline** — read the data schema → write the query → run the forecast → backtest (MASE/MAPE) → gate on accuracy → open a PR. That IS an autonomous-agent-for-software task (Goal #1), with TimesFM as one component.

Neither bridge makes the *model* on-goal; they make it **goal-adjacent and genuinely pilotable**. Verdict keys the tier at **(b) MODERATE**, GOAL-ALIGNED per operator direction, OFF-GOAL-CAPTURE equally defensible (see Verdict).

---

## 3. Architecture (TimesFM 2.5, source-verified from `src/timesfm/`)

**Type:** decoder-only transformer, **200M parameters** (2.5; down from 2.0's 500M). Two backends: **PyTorch** (`TimesFM_2p5_200M_torch`) and **JAX/Flax** (`TimesFM_2p5_200M_flax`), plus a HuggingFace `-transformers` checkpoint.

**Config (verified in `timesfm_2p5/timesfm_2p5_base.py` + `configs.py`):**

| Dimension | Value |
|---|---|
| Transformer layers | **20** |
| Model dims | **1280** |
| Attention heads | **16** (head dim 80) |
| Feedforward hidden | 1280, **SiLU/swish** activation |
| Positional encoding | **Rotary (RoPE)** |
| Normalization | **RMSNorm**, pre-LN, with QK-norm; **fused QKV** projection + per-dim scale |
| **Input patch length** | **32** time-points (= one "token") |
| **Output patch length** | **128** (larger than input → fewer autoregressive steps, less error accumulation) |
| Output quantile length | 1024 |
| **Context limit** | **16,384** time-points (2.5; was 2,048 in 2.0, 512 in 1.0) |
| Quantiles | `[0.1 … 0.9]` deciles **+ mean** = **10 output slices** |

**How a forecast flows (from `timesfm_2p5_torch.py`):**
1. The history is chopped into 32-point patches; each patch is concatenated with a mask and passed through a **ResidualBlock tokenizer** → embeddings.
2. Embeddings flow through **20 transformer layers** with a **KV-cache** (`DecodeCache`).
3. Two heads: a **point head** and a **quantile head** → point forecast + 9 quantiles.
4. Long horizons are produced by **autoregressive decode in 128-point output patches** (feed the last output back as input).
5. **Reversible instance normalization (ReVIN)** + **Welford online running-stats** normalize each series by its own mean/std (numerical stability across scales), then de-normalize the output.

**Notable property (documented in code):** `TimesFM(aX + b) = a·TimesFM(X) + b` for `a ≥ 0` (scale/shift equivariance); `force_flip_invariance=True` extends it to `a < 0`.

**Covariates (XReg, `utils/xreg_lib.py`):** `forecast_with_covariates()` supports dynamic/static × numerical/categorical exogenous variables via **in-context linear regression** (`BatchedInContextXRegLinear`, an sklearn `LinearRegression` + one-hot). Two modes: `"xreg + timesfm"` (fit linear model first, TimesFM forecasts residuals) or `"timesfm + xreg"`. Requires `pip install timesfm[xreg]`.

---

## 4. The public API (source-verified — use THIS, not third-party approximations)

```python
import torch, numpy as np, timesfm
torch.set_float32_matmul_precision("high")

# 1. Load a pretrained checkpoint from HuggingFace (~800 MB, cached in ~/.cache/huggingface)
model = timesfm.TimesFM_2p5_200M_torch.from_pretrained("google/timesfm-2.5-200m-pytorch")

# 2. Compile with a ForecastConfig (controls all behavior)
model.compile(timesfm.ForecastConfig(
    max_context=1024,                  # longest history you'll feed
    max_horizon=256,                   # longest forecast
    normalize_inputs=True,             # ALWAYS set True
    use_continuous_quantile_head=True, # calibrated PIs for long horizons
    force_flip_invariance=True,
    infer_is_positive=True,            # clamp ≥0 for non-negative series (counts!); set False for temp/returns
    fix_quantile_crossing=True,        # ensure q10 ≤ q20 ≤ … ≤ q90
))

# 3. Forecast a batch of series
point, quantiles = model.forecast(
    horizon=24,
    inputs=[series_a, series_b],       # list of 1-D numpy arrays, any length
)
# point.shape     == (2, 24)      — the median / point forecast
# quantiles.shape == (2, 24, 10)  — index 0 = mean, 1 = q10, … 9 = q90
```

**Quantile index map (a documented footgun):** `quantiles[..., 0]` is the **mean**, NOT q0. `q10 = index 1`, `q50/median = index 5`, `q90 = index 9`.

**Anomaly detection is free** (no separate model): forecast, then flag actuals outside `[q10, q90]` (outside 80% PI) as anomalies — the bundled example detrends + z-scores the context and uses quantile PIs on the forecast.

**Backtesting recipe (from the SKILL.md):**
```python
H = 24; train, actual = values[:-H], values[-H:]
point, q = model.forecast(horizon=H, inputs=[train])
mae, rmse = np.mean(np.abs(actual-point[0])), np.sqrt(np.mean((actual-point[0])**2))
mape = np.mean(np.abs((actual-point[0])/actual))*100
coverage = np.mean((actual>=q[0,:,1]) & (actual<=q[0,:,9]))*100   # % inside 80% PI
```

---

## 5. Version history (README update-log is authoritative — secondary-source dates conflict)

| Version | Params | Context | Quantiles | Covariates | Launched |
|---|---|---|---|---|---|
| **1.0** | 200M | 512 | experimental/uncalibrated | freq indicator only | paper Oct 2023 / ICML 2024 |
| **2.0** | 500M | 2,048 | experimental/uncalibrated | freq indicator only | + LOTSA data, median-head default |
| **2.5** (latest) | **200M** | **16,384** | **calibrated deciles + mean** | **XReg** (restored) | **Sept 15, 2025** (README) |

- **Sept 15 2025:** TimesFM 2.5 — smaller (200M), 8× longer context (16k), continuous quantile head (up to 1k horizon), **`frequency` indicator removed**, QKV fused for speed.
- **Oct 29 2025:** XReg covariate support restored for 2.5.
- **Mar 19 2026:** `AGENTS.md` + `SKILL.md` added (@borealBytes).
- **Apr 9 2026:** LoRA fine-tuning example + unit tests added.
- **Jul 2 2026:** PyPI `timesfm 2.0.2` (loads the 2.5 model).

⚠️ Two research agents produced **conflicting/garbled release dates** (one said 2023-2024, another 2024-2025 for the same tags). I discarded both and used the repo's own dated update-log (read first-hand). The paper (1.0) is 2023/ICML-2024; the 2.5 model launched Sept 2025.

**HuggingFace monthly downloads (page-stated only, §37.4 — NOT a velocity claim):** `timesfm-1.0-200m-pytorch` ~19.8k/mo, `timesfm-2.0-500m-pytorch` ~28k/mo, `timesfm-2.5-200m-transformers` ~202.7k/mo.

---

## 6. How it was trained (paper-stated)

- **Corpus:** ~**100 billion time-points**, predominantly **Wikipedia pageviews + Google Trends**, plus **synthetic** series (ARMA processes, seasonal sine/cosine mixtures, trends, step functions). Roughly **80% real / 20% synthetic** (paper-stated; exact sub-volumes vary across the paper's tables — treat the ~100B order + the 80/20 split as the reliable figures).
- **Objective:** MSE on predicted patches; **random patch masking** during training exposes the model to every context length 1→max so it handles variable histories at inference.
- **Hardware:** 16 TPUv5e cores, ~2 days, ~1.5M iterations (for the 200M model).
- **Design rationale:** input patch 32 balances speed vs accuracy (p=32 ≈ 2× faster than p=16 at similar quality); output patch 128 > input patch to cut autoregressive steps on long horizons.

---

## 7. Benchmarks + competitive landscape (the honest read)

**Paper zero-shot results (paper-stated):**
- Monash (18 datasets), geometric-mean scaled MAE: TimesFM **0.6846** vs supervised N-BEATS 0.7005.
- ETT (electricity transformer temp), avg MAE: TimesFM **~0.36** ≈ supervised **PatchTST 0.37** — i.e. *zero-shot matches a model trained on the target*, at 200M params vs 175B for GPT-3.5-based approaches.

**Where it sits in 2026 (leaderboard-stated, churns fast):** TimesFM 2.5 led GIFT-Eval zero-shot on release (Sept 2025), but is now a strong **#2**, not the leader:

| Model | Org | Note |
|---|---|---|
| **Chronos-2** | Amazon | **Current GIFT-Eval leader** (~79.8% win-rate vs TimesFM ~70.0%, per the Chronos-2 paper's late-2025 snapshot); natively multivariate/covariate |
| **TimesFM 2.5** | Google | Strong #2; **longest context (16k)**, most param-efficient top-tier (200M), Google Cloud integration |
| **Moirai-2.0** | Salesforce | #3; **native any-variate multivariate** |
| **IBM TTM / Granite** | IBM | 1M-scale, **CPU/edge**-friendly |
| **Toto** | Datadog | **observability-metrics** specialist (2T-point corpus) |
| **TimeGPT** | Nixtla | the only **closed / API-only** top-tier model |
| **Moment** | CMU (MIT license) | multi-task (forecast/classify/anomaly/impute) |

**TimesFM wins:** long univariate context (16k), parameter efficiency, Google Cloud distribution (BigQuery/Vertex/Sheets), calibrated quantiles (2.5).
**TimesFM loses:** multivariate/covariate-heavy workloads (→ Moirai-2.0), raw GIFT-Eval accuracy (→ Chronos-2), edge/CPU (→ IBM TTM), observability (→ Toto).
*(Numbers here are from a competitor's paper + a public leaderboard, page/leaderboard-stated and time-sensitive — treat as "competitive #2, leader churns," not gospel.)*

---

## 8. Deployment surfaces (how you'd actually run it)

| Surface | Status | How | Notes |
|---|---|---|---|
| **PyPI** | ✅ verified | `pip install timesfm[torch\|flax\|xreg]` (Python ≥3.10) | Load `from_pretrained`, `.compile`, `.forecast` |
| **HuggingFace** | ✅ verified | checkpoints `google/timesfm-2.5-200m-{pytorch,flax,transformers}` | Custom loader (not plain `AutoModel`), though a `-transformers` checkpoint exists |
| **BigQuery ML** | ✅ verified (key fact) | **`AI.FORECAST` — built-in, NO `CREATE MODEL`, no training**, all regions | Lowest-effort if your data is in BigQuery. *(Exact arg names weren't fetchable from the SPA docs — confirm `data_col`/`timestamp_col`/`horizon`/`id_cols`/`confidence_level` against the live [BigQuery TimesFM doc](https://cloud.google.com/bigquery/docs/timesfm-model) before relying on a specific signature.)* |
| **Google Sheets** | README-advertised | Connected Sheets forecasting (BigQuery ML + TimesFM) | Not independently verified here |
| **Vertex Model Garden** | README-advertised | "Dockerized endpoint for **agentic calling**" | Managed REST endpoint; steps/pricing not verified here |
| **Fine-tuning** | ✅ present in repo | HF Transformers + PEFT **LoRA**, `timesfm-forecasting/examples/finetuning/` | ⚠️ horizon < 128 may conflict with the 128 output-patch (issue #460) |

---

## 9. Honest caveats (all source- or issue-verified)

- **Univariate at heart.** Multivariate is a workaround (per-series models, or XReg covariates); Moirai-2.0 handles arbitrary variables natively, TimesFM doesn't.
- **Needs contiguous, regularly-sampled history, no gaps/NaNs** — interpolate/forward-fill first. And it needs enough of it (~hundreds of points for a good forecast; short/sparse series are a poor fit).
- **`jax[cuda]` is hardcoded** in the `flax` and `xreg` extras (`pyproject.toml`) → **CPU-only installs of those extras break** (issue #443). Use `[torch]`, or install a CPU JAX manually.
- **Apple Silicon torch issues** (lingvo lineage) — use the **Flax** backend on Mac, or Linux for torch inference.
- **CI is build-only.** `main.yml` builds the package on push/PR but **runs no test step** — the 6 `tests/` files (configs, model-loading, torch layers, running-stats, NaN-strip) exist but aren't gated in CI.
- **2 of the 3 bundled skill examples are stale.** `anomaly-detection/detect_anomalies.py` and `covariates-forecasting/demo_covariates.py` import `timesfm.TimesFmHparams` / `timesfm.TimesFmCheckpoint` — the **legacy 1.x API the current 2.5-only package no longer exports** (verified: current `src/timesfm/__init__.py` exports only `ForecastConfig` + `TimesFM_2p5_200M_{torch,flax}`). They target `timesfm==1.3.0`. Only `global-temperature/run_forecast.py` uses the current 2.5 API. If you install the skill, expect the anomaly/covariates demos to need the archived package or a rewrite.
- **Quantiles were uncalibrated until 2.5** (1.0/2.0 quantile heads are experimental).
- **No in-repo training code** — you get pretrained weights + inference + a LoRA fine-tune example, not the pretraining pipeline.
- **Not an officially supported Google product** (repo's own words).
- **Supply-chain: BENIGN** (Apache-2.0, no `postinstall`/`curl|bash`/telemetry; ~800 MB weight download from HuggingFace on first use). The real "risks" are install-fragility (jax[cuda], Apple Silicon), not security.

---

## 10. Anti-confabulation log (what I nearly got wrong, and killed)

Per the vault's `feedback_wiki_verify_independently_check_collisions` rule, verification was **hand-done**; the read-only workflow did source+upstream research ONLY. Caught + discarded:
- **Two false "doc-drift" findings** — I twice suspected `AGENTS.md`/`SKILL.md` referenced files/dirs (`v1/`, `v1/tests/`, `scripts/`, `references/`, `examples/global-temperature/`) that were "absent." They are **all present at HEAD** (`git ls-tree` confirmed 102 tracked files); my local working tree was left **partial by a missing `git-lfs` binary**. Completed the checkout (LFS-bypass) and confirmed AGENTS.md is accurate. Neither false caveat entered the wiki.
- **Two research agents' release dates** were garbled/conflicting → discarded; used the README's own dated update-log.
- **The recruiting agent's code snippets** (`TimesFM.from_pretrained(historical_data=…)`, a `vertexai … TimeSeriesForecastingModel` class, a `CREATE MODEL … model_type='TIME_SERIES'` BigQuery snippet, "BigQuery isn't really TimesFM") are **approximations/partly fabricated** → replaced with the **source-verified 2.5 API** and the **verified** BigQuery fact (built-in `AI.FORECAST`, no training). Its *fit-matrix reasoning* is excellent and kept.
- **Collision grep** across `_state/` + `_patterns/` + `03 Projects/` → **no prior time-series / forecasting-model / TimesFM / Chronos / Moirai subject** anywhere (the "forecast"/"moment" hits are the vault's own bookkeeping). TimesFM is **corpus-first for the forecasting domain** (but see Verdict — that does **not** earn a mint).

---

*Files: `(C) TimesFM — Deep Dive.md` (this) · `(C) TimesFM — Verdict.md` · `(C) TimesFM — Pilot Methods Menu.md`. Wiki v193, shipped on branch `wiki/v193-timesfm`.*
