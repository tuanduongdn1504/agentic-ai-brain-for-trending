# (C) TimesFM — Pilot Methods Menu (v193)

**24 ways to apply TimesFM to your working flow, honestly weighted.** Grouped A→F by effort/risk/goal-fit. All code uses the **source-verified 2.5 API** (not third-party approximations).

> **The honest weighting up front:**
> - **TimesFM's domain is off your Goal #1** (Claude + agents for software). So the highest-value applications are **Goal #2 (hireui)** — recruitment forecasting — and **borrowing the model's *engineering patterns*** into your agent work.
> - **Only ONE recruitment metric is a genuinely HIGH fit: application/candidate volume** (regular cadence, long history). Most others (time-to-fill, offer-accept, no-show) are **too sparse/irregular/process-sensitive** — don't force them onto a 200M foundation model; use Prophet/statsforecast/regression instead. Being blunt: forcing TimesFM onto sparse hiring events is a rabbit hole.
> - **The Goal-#1 bridge is real but indirect:** the value is *Claude Code orchestrating a forecasting pipeline* (a genuine agent-for-software task) and the model's *first-party Agent Skill* as a design exemplar — not the forecasting itself.

**⭐ One-thing path:** **D13** (forecast hireui application volume via BigQuery ML `AI.FORECAST` — zero training, ~1–2h if data's in BQ) **+ D16** (backtest gate: require MASE < 1.0 before trusting) **+ B7** (steal the preflight-checker + backtest-gate patterns into your own agent skills regardless). That's a real, small, first Goal-#2 data feature that requires no model hosting.

---

## A. Read + learn (zero risk, zero install)

**A1 — Read the paper as the "LLM patterns → new modality" case study.** arXiv 2310.10688. The transferable insight: *decoder-only pretraining + patching + zero-shot transfer* is a general recipe, not a text-only one. Sharpens your intuition for how Claude-style pretraining generalizes. ~1h.

**A2 — Read `SKILL.md` (511 lines) as an exemplar of a *well-built* Agent Skill.** This is the on-goal gold: a mandatory **preflight system-checker** (blocks if RAM/disk/GPU insufficient *before* loading a model that could crash the machine), dataset-fit memory estimation, an explicit "when to use / do NOT use" table, a quality checklist, and a "common mistakes" section. This is a template for how *your* `05 Skills/` skills should be defensive. ~30min.

**A3 — Map the honest fit-matrix to hireui's metrics** (from the Deep Dive §7 / research): application volume = **HIGH**; source volume = **MED-HIGH**; pipeline velocity / headcount = **MEDIUM**; offer-accept / no-show / time-to-fill = **LOW** (too sparse/noisy/process-sensitive). Decide the 1–2 metrics worth forecasting *before* touching code. 30min.

**A4 — Read the competitive landscape** (Chronos-2 / Moirai-2.0 / IBM TTM / Toto / TimeGPT). If you ever ship forecasting, know that **Chronos-2 currently leads GIFT-Eval** and **Moirai-2.0 is natively multivariate** — TimesFM's edges are long context (16k) + Google Cloud integration. 30min.

---

## B. Borrow the *patterns* into your own work (high ROI, zero/low install)

These are the real Goal-#1-adjacent wins: TimesFM's engineering ideas ported into your vault/hireui/agent tooling.

**B5 — The mandatory-preflight-gate pattern.** `SKILL.md` runs `check_system.py` *before* loading the model and **blocks** on insufficient resources. Port this into your own agent skills/tools: a preflight that refuses to run rather than crashing/OOMing. Composes with your `install-snapshot` discipline. Zero install.

**B6 — Quantile-as-anomaly-detector.** No separate anomaly model needed: forecast, then flag actuals outside `[q10, q90]`. A cheap, general monitoring primitive you can apply to *any* metric you already track (CI durations, token spend, API latency, hiring funnel). Steal the recipe, use whatever forecaster.

**B7 — The backtest-gate discipline as a "verify before ship" pattern.** The skill's recipe: split off the last H points, forecast, compute **MASE/MAPE + PI coverage**, and only trust the forecast if `MASE < 1.0` (beats the naive baseline). This is the *numeric quality gate* pattern — directly analogous to your **loop-engineering v189** L1→L2 graduation bar and loop-verifier. Generalize: no forecast/model output ships without a held-out numeric gate.

**B8 — The "agent orchestrates a pipeline with a numeric gate" pattern into your loop work.** The realistic TimesFM use = Claude Code doing query→forecast→backtest→**gate**→PR. That shape (agent runs a pipeline, a *number* decides go/no-go, human approves) is a reusable loop-engineering pattern independent of forecasting. Add it to your loop patterns menu.

**B9 — Cost-governance cross-ref.** If you ever route forecasting through Vertex/BigQuery, the estimate→run→reconcile mindset from your `claude-api-cost-optimization` spec applies. Note it; don't build yet (hireui has no LLM spend yet).

---

## C. Low-risk hands-on trial (scratch, ~1–3h)

**C10 — `pip install timesfm[torch]` in a scratch venv (Linux/Colab, NOT Mac torch).** Run the verified minimal example on synthetic data:
```python
import torch, numpy as np, timesfm
torch.set_float32_matmul_precision("high")
m = timesfm.TimesFM_2p5_200M_torch.from_pretrained("google/timesfm-2.5-200m-pytorch")
m.compile(timesfm.ForecastConfig(max_context=512, max_horizon=64, normalize_inputs=True,
          use_continuous_quantile_head=True, fix_quantile_crossing=True))
point, q = m.forecast(horizon=24, inputs=[np.sin(np.linspace(0,20,300))])
print(point.shape, q.shape)   # (1,24) (1,24,10)
```
Fence: scratch venv + `install-snapshot` first + **on Mac use `[flax]` not `[torch]`** (lingvo/ARM issue) + expect ~800 MB weight download.

**C11 — Free BigQuery ML `AI.FORECAST` on a public dataset.** No training, no `CREATE MODEL` — it's a **built-in** model. Forecast a column of a public time-series table to feel the SQL surface (confirm exact arg names against the [live doc](https://cloud.google.com/bigquery/docs/timesfm-model) — the shape is `SELECT * FROM AI.FORECAST(TABLE …, data_col => …, timestamp_col => …, horizon => …, …)`). Lowest-effort surface of all.

**C12 — Install the Agent Skill into a scratch `~/.claude/skills/` and let Claude Code drive a forecast.** `cp -r timesfm-forecasting/ ~/.claude/skills/` (from a pinned clone), then ask Claude Code to forecast a CSV. This is the on-goal loop: *a coding agent using a domain skill*. ⚠️ Expect the `anomaly-detection` + `covariates` demos to fail against the current package (they use the stale 1.x API — see Deep Dive §9); `global-temperature` works. Uninstall via `install-snapshot`'s checklist.

**C13 — Backtest on a public dataset** (electricity/traffic/retail): use the B7 recipe, compute MASE/MAPE + 80% PI coverage. Builds the "is this forecast trustworthy?" muscle before pointing it at real data.

---

## D. hireui-specific — the real Goal-#2 payoff (on an `agent-*` branch)

> Fence for all of D: application/candidate-**volume** only (the HIGH-fit metric); **backtest MASE < 1.0** before trusting any forecast; hireui per its CONSTITUTION (**I-2** `agent-*` branch, **I-8** operator-installs, **GitNexus-first**); prefer **BigQuery ML** (no infra) or a **batched Cloud Run cron** (never a live per-request model load — cold load is slow). hireui has **no LLM spend yet**, so this is a build-it-right data feature, not a retrofit.

**D13 — ⭐ Forecast hireui application volume via BigQuery ML `AI.FORECAST`** (if the data is in BigQuery). Zero training, ~1–2h. Query daily application counts (last 12+ months) → `AI.FORECAST` for the next 4/13 weeks with a confidence level → store the point + PI. The single lowest-effort, highest-fit hireui application. *(Confirm the exact `AI.FORECAST` argument names against the live BigQuery doc.)*

**D14 — Python microservice forecast endpoint** (if you want to own the model + quantiles). A Cloud Run batch/cron job using the verified 2.5 API:
```python
m = timesfm.TimesFM_2p5_200M_torch.from_pretrained("google/timesfm-2.5-200m-pytorch")
m.compile(timesfm.ForecastConfig(max_context=512, max_horizon=91, normalize_inputs=True,
          use_continuous_quantile_head=True, infer_is_positive=True, fix_quantile_crossing=True))
point, q = m.forecast(horizon=91, inputs=[daily_application_counts])   # 13-week forecast
# write point + q[:, :, 1] (q10) + q[:, :, 9] (q90) to BigQuery/Postgres
```
Run it weekly (cron), not per-request. ~4–8h.

**D15 — Candidate source-volume forecasting (MED-HIGH fit).** Forecast per-source volume (job board / referrals / recruiter sourcing) as a batch of series (`inputs=[src_a, src_b, …]` → one `.forecast` call). Feeds source-mix capacity planning + detects when a source is underperforming its forecast.

**D16 — ⭐ The backtest gate (composes with D13/D14).** Before any hireui forecast is shown to a user, hold out the last 13 weeks, forecast, require **MASE < 1.0** (beats naive) + **PI coverage ≥ 75%**. If it fails for a given series (too sparse/noisy), the feature **falls back to a naive/Prophet baseline or hides the forecast** — don't ship a bad number. This is the difference between a real feature and a demo.

**D17 — Quantile-based hiring-funnel anomaly monitor.** Apply B6 to hireui: each week, forecast expected volume, flag weeks where actual falls outside the 80% PI as "unusual" (a recruiter-facing alert). The SKILL.md's anomaly recipe, applied to recruitment. Read-only, low-risk.

**D18 — ⭐ Have Claude Code ORCHESTRATE the whole build (the Goal-#1 bridge).** This is the genuine autonomous-agent-for-software artifact: give Claude Code a spec ("forecast application volume, 4 weeks, backtest MASE<1, else escalate"), let it read the schema (GitNexus-first) → write the query → run the forecast → compute the gate → open a PR with the numbers + a chart. TimesFM is one component; the *agent running the pipeline with a numeric gate + human approval* is the on-goal part. Composes with your multi-agent-orchestration + loop-engineering v189 threads. **A completed D13+D16+D18 on an `agent-*` branch = the first real Goal-#2 pilot artifact of this thread.**

**D19 — Capacity-planning view.** A 13-week application forecast with PI bands feeding a "how many recruiters/interview slots will we need?" panel. The business-facing payoff once D13/D16 prove out.

---

## E. Off-goal personal use (be honest — this is not the software goal)

**E20 — Forecast personal metrics** (finances, project velocity, health/fitness series). Fastest way to *feel* zero-shot forecasting; not goal-relevant.

**E21 — Learn the FM-forecasting landscape as a durable skill.** Knowing TimesFM vs Chronos-2 vs Moirai-2.0 vs Prophet is a genuinely useful data-science skill for a Scrum coach advising teams — but it's a side quest relative to the Claude/agents goal.

---

## F. Vault-meta follow-ups

**F22 — Record the "model/product retrofitted to be agent-native" watch axis.** v192 palmier-pro bolted an **MCP server** onto a video editor; v193 TimesFM bolts an **Agent Skill + Vertex agentic endpoint** onto a forecasting model. Two instances of the same meta-move. Flag to the ~v192-due audit: is this a forming pattern, or two unlike shapes? (Record, don't mint at N=2.)

**F23 — Queue Chronos-2 (Amazon) as a potential future subject.** It currently leads GIFT-Eval and is natively multivariate — the natural "landscape revisit" if forecasting ever becomes load-bearing for hireui. Same off-goal caveat applies.

**F24 — Feed the "agent orchestrates a numeric pipeline with a go/no-go gate" pattern into loop-engineering v189.** The D18 shape (agent runs pipeline → number decides → human approves) is a reusable loop pattern worth codifying alongside the v189 patterns, independent of forecasting.

---

## The blunt summary

- **Do:** B5/B6/B7 (steal the preflight + anomaly + backtest-gate patterns — pure win, zero install) → C11/C12 (feel the BigQuery + Agent-Skill surfaces) → **D13 + D16 + D18** (forecast hireui application volume, gated, agent-orchestrated, on an `agent-*` branch).
- **Don't:** force TimesFM onto time-to-fill / offer-accept / no-show (too sparse — use Prophet/regression); run it as a live per-request model in hireui (batch/cron only); install `[torch]` on Mac (use `[flax]`); trust any forecast that fails the MASE<1 gate.
- **Remember:** this is off your Goal #1. The value is (a) a real Goal-#2 data feature and (b) the *engineering patterns* + the *agent-orchestration* shape — not the forecasting per se.

*Fence (all pilots): pin commit `4a6c5cd` · `install-snapshot` before `pip install` · scratch venv/project first · Linux/Colab or Flax-on-Mac · hireui per its CONSTITUTION (I-2/I-8/GitNexus-first) · backtest gate before trusting any number.*
