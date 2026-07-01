# (C) DeepSpec / DSpark — Deep Dive + Verdict (v186)

> **Wiki ship v186** · built 2026-07-01 · subject `deepseek-ai/DeepSpec` (MIT, cloned + source-verified at commit `afdfa7c`, last commit 2026-06-30 by `Hannibal046`).
> **Prefix `(C)` = Claude-generated.** Verdict produced **inline + hand-verified** per `feedback_wiki_verify_independently_check_collisions`.
> **One-line honest read:** DeepSpec is *not* a spec-driven-development tool — the name misleads. It is **DeepSeek's speculative-*decoding* training framework**: it trains and evaluates small **draft models** that make a big LLM generate tokens faster, losslessly. It's inference-acceleration ML research, not Claude/agent tooling — the **GLM-5 v176 situation**, arguably more so.

---

## 0. TL;DR

- **What it is:** A full-stack Python codebase (torch/transformers/triton, MIT) for **training + evaluating draft models for speculative decoding**. Ships three drafter algorithms — **DSpark** (DeepSeek's own, with a paper), **DFlash** (from z-lab), **Eagle3** (baseline, adapted from SGLang's SpecForge) — targeting **Qwen3-{4B,8B,14B}** and **Gemma-4-12B**, with released HuggingFace checkpoints.
- **The novel method (DSpark):** *"Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation"* (paper by Peking University + DeepSeek-AI, incl. founder **Liang Wenfeng**). Two ideas: **(1)** a *semi-autoregressive* drafter = heavy **parallel backbone** (DFlash) + a **lightweight sequential head** (Markov / RNN) that injects intra-block token dependency to kill "suffix decay"; **(2)** **confidence-scheduled verification** = a confidence head predicts per-token prefix-survival probability, and a hardware-aware scheduler spends the target model's verification budget only on tokens likely to be accepted.
- **Where it runs in production:** Deployed in **DeepSeek-V4** (Flash + Pro previews). Vs the prior **MTP-1** production baseline, DSpark accelerates per-user generation **60–85%** (V4-Flash) / **57–78%** (V4-Pro) at matched throughput *(DeepSeek's own page/paper-stated benchmarks — unreplicated)*.
- **Verdict:** **GOAL-ALIGNED INCLUDE 3/4 per operator direction** [(a) FAIL · **(b) MODERATE** · (c) STRONG · (d) STRONG]. The stricter **(b) FAIL → OFF-GOAL CAPTURE** reading is *equally / more* defensible — recorded as the operator-reviewable alternative (the GLM-5 v176 template).
- **Pattern outcome: NO MINT.** No new top-level pattern (max #85), no new §C standalone, **counts UNCHANGED 46/11**, §C surface unchanged. Corpus-FIRST for the *speculative-decoding / inference-acceleration domain* within the vault — but a **DEFERRED watch axis**, not a mint (anti-inflation). It is the **2nd "model/inference-substrate" data-point** after GLM-5 v176 → strengthens that deferred-tier question.
- **Pilot honesty:** DeepSpec's checkpoints only accelerate **open-weight** models (Qwen3/Gemma4). **They cannot be applied to Claude** (closed weights — you can't swap a draft model in). The real "apply" is **conceptual** (understand the inference cost/latency levers) + a **conditional self-host path**. See the separate **Pilot Methods Menu**.

---

## 1. What DeepSpec actually is (source-verified)

Repo tree (67 `.py` files, ~11.7K lines, 1 PDF):

```
DeepSpec/
├── DSpark_paper.pdf          ← DeepSeek's DSpark paper (24 pp)
├── LICENSE (MIT) / NOTICE    ← attributions: SpecForge (Apache-2.0), DFlash (MIT)
├── requirements.txt          ← torch 2.9.1, transformers 5.10.2, triton 3.5.1, ...
├── train.py / eval.py
├── config/{dspark,dflash,eagle3}/*_qwen3_{4,8,14}b.py + *_gemma4_12b.py
├── deepspec/
│   ├── modeling/{dspark,eagle3}/{qwen3,gemma4}/  ← the drafter architectures
│   │   └── dspark/{common,markov_head,loss}.py   ← the DSpark novelty
│   ├── eval/{dspark,eagle3}/ + base_evaluator.py ← accepted-length (τ) measurement
│   ├── trainer/{base,dspark,eagle3}_trainer.py   ← FSDP training loop
│   ├── data/{jsonl_dataset,target_cache_dataset}.py
│   └── utils/{sampling,optim,distributed,hfai_suspend}.py
├── eval_datasets/            ← gsm8k, math500, aime25, humaneval, mbpp,
│                                livecodebench, mt-bench, alpaca, arena-hard-v2
└── scripts/{data,train,eval}/
```

**Repo facts (page-stated — §37.4 GitHub API is mocked in this env, so NOT verified velocity → NOT a Pattern #52 claim):** 5.4k★ / 428 forks / 25 watchers · Python 97.9% + Shell 2.1% · MIT · **no releases** · 14 commits. Author = **DeepSeek-AI** (org `deepseek-ai`; 94.7k followers; sibling repos DeepSeek-OCR 23.5k★, FlashMLA 12.7k★, 3FS 10k★, DeepEP 9.8k★, DeepGEMM 7.5k★).

### The name trap (documented so nobody re-makes it)
"DeepSpec" reads like a **spec-driven-development** tool (cf. corpus subjects spec-kit v17 / cc-sdd v61 / OpenSpec). **It is not.** The `Spec` = **Speculative decoding**. This was caught at first inspection from the tree (`DSpark_paper.pdf`, `config/eagle3`, `confidence_head.py`, `markov_head.py`, draft models for Qwen3/Gemma4, LLM benchmark eval sets) and confirmed by the README line 3: *"DeepSpec is a full-stack codebase for training and evaluating draft models for speculative decoding."*

---

## 2. Background — speculative decoding in 90 seconds

Autoregressive LLMs generate **one token per forward pass**, so latency ∝ output length and GPUs sit underused. **Speculative decoding** (Leviathan et al. 2023, [arXiv 2211.17192](https://arxiv.org/abs/2211.17192); Chen et al. 2023, [arXiv 2302.01318](https://arxiv.org/abs/2302.01318)) fixes this:

1. A cheap **draft model** proposes a block of γ candidate tokens.
2. The full **target model** verifies the whole block **in one forward pass**, accepting the longest prefix consistent with its own distribution (via **rejection sampling**) plus one bonus token.
3. Because verification is parallel and the acceptance rule preserves the target distribution **exactly**, it is **lossless** — the output is identical to normal sampling, just faster.

Per-token latency: **L = (T_draft + T_verify) / τ**, where τ = average accepted tokens per cycle. Three levers to go faster: **draft cheaper** (↓T_draft), **draft better** (↑τ), **verify smarter** (↓effective T_verify). DSpark attacks the last two.

**Landscape (2026):** speculative decoding is now table-stakes in production serving — built into vLLM, SGLang, TensorRT-LLM, llama.cpp. Methods: EAGLE/EAGLE-3, Medusa, n-gram lookup, **MTP** (DeepSeek/Google). DeepSeek's V3 shipped **MTP** as its spec-decoding module; DSpark is the V4-generation successor. *(Sources: [premai spec-decoding 2026](https://blog.premai.io/speculative-decoding-2-3x-faster-llm-inference-2026/), [vLLM spec-decode](https://blog.vllm.ai/2024/10/17/spec-decode.html).)*
**Claude:** there is **no publicly disclosed statement** about whether Claude's inference stack uses speculative decoding — do not assume it does or doesn't. (Confirmed via the `claude-api` reference: spec-decoding is not a user-facing Claude API lever.)

---

## 3. DSpark — the novel method (the "double deep dive")

Paper: **"DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation"** — Xin Cheng, Xingkai Yu, Chenze Shao, Jiashi Li, Yunfan Xiong (equal contrib) + DeepSeek-AI team incl. Damai Dai, **Wenfeng Liang**. Affiliations: ¹Peking University ²DeepSeek-AI.

**The problem DSpark names:** *parallel* drafters (like DFlash) produce a whole block in one pass, so drafting latency is ~independent of block size — but each position predicts *independently*, so they can't model within-block token dependencies. Result: "multi-modal collision" (e.g. proposing "of problem" / "no course" instead of "of course" / "no problem") and **rapid acceptance decay** deeper in the block. Separately, blindly verifying long blocks **wastes target-model batch capacity** under high concurrency. DSpark = two complementary fixes.

### 3.1 Semi-autoregressive generation (fix draft quality)
- **Parallel stage:** a heavy **parallel backbone** (DFlash — a shallow transformer stack that takes an anchor token + γ mask tokens and, via **KV-injection** of the target model's hidden states from a set of target layers, produces γ base logits in one pass). *Verified in code:* `Qwen3DSparkAttention` concatenates `[target_hidden_states ‖ draft_hidden]` for K/V so draft queries attend to real target context; `self.fc` projects the concatenated target-layer states.
- **Sequential stage:** a **lightweight serial head** adds a *prefix-dependent transition bias* `B_k(x_0, x_<k, x_k)` on top of the base logits, so each draft position conditions on the tokens actually sampled before it — injecting local dependency at minimal latency.
  - **Markov head (default):** first-order bias `B(x_{k-1}) = W1[x_{k-1}]·W2`, a **low-rank factorization** (rank `r=256`). *Verified:* `markov_head.py` → `VanillaMarkov` is exactly `nn.Embedding(vocab, r)` (=W1) then `nn.Linear(r, vocab)` (=W2). Also present: `GatedMarkovHead` (sigmoid gate) and `RNNHead` (GRU-like recurrent state carrying the full within-block prefix).
- **Why it works (paper Fig. 2):** the parallel backbone gives a big accuracy edge at **position 1** (deep network, and position 1 has the most leverage — a rejection there kills the whole block); the sequential head stops the tail decay parallel drafters suffer. Net: DSpark keeps parallel drafting speed *and* autoregressive-like coherence.

### 3.2 Confidence-scheduled verification (fix system efficiency)
- **Confidence head:** a tiny sigmoid predictor `c_k = σ(wᵀ[h_k ; W1[x_{k-1}]])` estimates the *conditional* per-position acceptance probability, supervised on the analytical target `c*_k = 1 − ½‖p^d_k − p^t_k‖₁` (1 − ½·total-variation between draft and target). *Verified:* `AcceptRatePredictor` = `nn.Linear(input_dim, 1)`; the prefix-survival estimate is `cumprod` of the per-step sigmoids.
- **Sequential Temperature Scaling (STS):** post-hoc left-to-right calibration (grid-search a temperature per position to minimize Expected Calibration Error) so the *absolute* survival magnitudes are trustworthy — needed because the scheduler uses them to compute expected accepted length, not just to rank tokens.
- **Hardware-Aware Prefix Scheduler (Algorithm 1):** across a batch of R live requests, greedily admit draft tokens by descending survival probability to maximize system throughput **Θ = τ · SPS(B)** (SPS = a pre-profiled engine step-rate curve). A **non-anticipating** early-stop keeps it lossless. Under high load it shrinks per-request verification length; under light load it extends it.

### 3.3 Training (3-loss, frozen target)
The target model is **frozen**; the draft **shares (copies, then freezes) the target's embedding + LM head** and trains only the backbone + sequential head + confidence head. Three position-weighted losses (`w_k = exp(−(k−1)/γ)`, emphasizing earlier positions):
- **L_ce** — cross-entropy vs ground-truth token.
- **L_tv** — total-variation distribution-matching (‖p^d − p^t‖₁); a direct proxy for acceptance rate.
- **L_conf** — BCE training the confidence head to predict `c*_k`.
- Default weights **α_ce=0.1, α_tv=0.9, α_conf=1.0** *(verified: these live in the config files, e.g. `config/dspark/dspark_qwen3_4b.py` — not hard-coded in `loss.py`)*.

### 3.4 Offline results (paper Table 1, accepted length τ ↑ = better)
DSpark beats both baselines across Qwen3-4B/8B/14B + Gemma4-12B on math / code / chat. Macro-average accepted-length improvement: **+30.9% / +26.7% / +30.0% over Eagle3** and **+16.3% / +18.4% / +18.3% over DFlash** (Qwen3 4B/8B/14B). Structured tasks (math ~5.57, code ~5.12 for Qwen3-4B) accept far more than open chat (~3.49) — which is *why* confidence-scheduled verification pays off (don't waste compute verifying doomed chat suffixes).

### 3.5 Online results (paper §5, DeepSeek-V4 live traffic)
DSpark-5 (γ=5) vs the **MTP-1** production baseline inside DeepSeek-V4-Flash/Pro (preview): **+60–85%** per-user gen speed (V4-Flash) and **+57–78%** (V4-Pro) at matched throughput; it also holds throughput under strict interactivity SLAs where MTP-1 collapses, shifting the serving Pareto frontier. The production backbone = 3 MoE layers + mHC + sliding-window-128; trained on the internal **HAI-LLM** framework (paper footnote → high-flyer.cn — HAI-LLM confirmed). *All these figures are DeepSeek's own, unreplicated.*

---

## 4. Code-vs-paper faithfulness (source-verified)

A 14-agent read-only workflow read every code slice; I hand-read the paper (24 pp) + `markov_head.py` + `confidence_head.py` + `draft_ops.py`. Findings:

- ✅ **Code matches the paper** on the drafter architecture, KV-injection, Markov/RNN heads, the 3 losses + position weights, the confidence head, and lossless rejection-sampling with cumulative-prefix acceptance.
- ⚠️ **Honest scope gap (documented faithfully):** the **production Hardware-Aware Prefix Scheduler (Algorithm 1)** is **NOT** in the open-source repo. The eval code implements only a **static confidence threshold** (`_confident_prefix_length` in `draft_ops.py` truncates the block at the first position whose sigmoid confidence < threshold; default 0.0 = disabled) + **offline calibration diagnostics** (ECE/AUROC/Brier + reliability diagrams in `confidence_head.py`). The dynamic, load-aware, throughput-maximizing scheduler that delivers the online §5 gains lives in DeepSeek's internal serving stack. → **The open repo is the training + offline-eval framework; the production scheduler is not shippable from it.** This bounds what "reproduce DSpark" means in a pilot.
- **Attribution is clean (NOTICE + in-file headers, hand-read):** Eagle3 modeling/loss/optim/eval adapted from **SpecForge** (sgl-project, Apache-2.0), whose fused log-softmax kernel itself credits **Unsloth** + **Liger-Kernel**; DSpark/DFlash configs build on **DFlash** (z-lab, MIT). Upstream, non-corpus dependencies — properly credited.
- **Cost of use (real numbers):** 8-GPU node default (FSDP), 10 epochs; target-cache of per-token hidden states ≈ **38 TB** for Qwen3-4B (README storage warning). Data pipeline = download `mlabonne/open-perfectblend` → regenerate answers via **SGLang** servers → precompute the target cache.

---

## 5. Verdict (INLINE + hand-verified)

**GOAL-ALIGNED INCLUDE 3/4 per operator direction** — [(a) FAIL · **(b) MODERATE** · (c) STRONG · (d) STRONG]. This mirrors the **GLM-5 v176** decision exactly: a goal-*adjacent* model/inference-substrate subject the operator elected to build.

### (a) FAIL — cleanly
DeepSeek-AI is a major **Chinese frontier-model corporate lab**, not Anthropic ((a)-7 is Anthropic-only), and not the individual cultural-peer axis. Declared-non-Anthropic-institution — the ByteDance v143 / NVIDIA v169 / OpenBMB v175 / **Zhipu (GLM-5) v176** / Microsoft (SkillOpt) v178 situation. No heritage rescue (v159→v185 discipline). **⚠️ Notable but corrected:** this is plausibly the corpus's **first *first-party* `deepseek-ai` org subject** — **DeepSeek-TUI v72** was a *third-party* TUI (`Hmbown`) *for* DeepSeek models, and **GLM-5 v176** is Zhipu, not DeepSeek. → a **#19 19a** institutional-portfolio data-point, not a new (a) axis.

### (b) MODERATE — tier-keying, operator-directed *(⚠️ (b) FAIL → OFF-GOAL CAPTURE is equally/more defensible)*
**For MODERATE:** speculative decoding is *the* core technique behind LLM inference latency + cost — the **engine layer** beneath "autonomous agents for software development." The released checkpoints are drop-in accelerators for **open-weight agent backends** (Qwen3/Gemma4 via SGLang/vLLM), and the concept lands directly on the operator's live **`claude-api-cost-optimization`** thread (understand *why* latency/throughput behave as they do).
**Flagged stretches (why OFF-GOAL is defensible — and arguably stronger than GLM-5's):**
1. It is a **training framework for draft models** (8 GPUs + 38 TB), not applicable tooling/methodology — nothing to "install and use" in the operator's flow.
2. It targets **open models, not Claude** — Claude is closed-weight, so you **cannot** apply these checkpoints to it. GLM-5 was at least a *routable Claude-Code backend* (via cc-switch v73); **DeepSpec is not even that.**
3. The corpus substrate is *tools-around-Claude*, not inference-acceleration ML research — this sits at the far edge of scope.
→ Per §31 the tier keys on **(b) MODERATE+ → GOAL-ALIGNED**, per operator direction. The `(b) FAIL → OFF-GOAL CAPTURE` reading is recorded as the operator-reviewable alternative.

### (c) STRONG
Real, publishable engineering: a **novel method** (DSpark) with a paper, **deployed in DeepSeek-V4 production**, plus a complete training+eval framework (FSDP, 3-loss objective, target-cache pipeline, 9-benchmark eval, 3 drafter algorithms, HAI-LLM preemption handling). **Caveats:** the hard novelty is the *method/paper*; the *repo* forks SpecForge (framework + Eagle3) and builds on DFlash; and the **production scheduler is not in the open repo** (§4).

### (d) STRONG
Dense adjacency: the model/inference-substrate cluster (**GLM-5 v176** / **DeepSeek-TUI v72** / **cc-switch v73** / **LLMs-from-scratch v74** / **fish-speech v20**) + the `claude-api-cost-optimization` pilot thread + the DeepSeek org portfolio + the optimizer-research neighborhood (see NON-#43 note below).

---

## 6. Pattern outcome — **NO MINT** (the GLM-5 v176 template)

**No new top-level pattern (max stays #85), no new §C standalone, counts UNCHANGED 46 confirmed / 11 CONFIRMED Library-vocab, §C surface unchanged.**

It **is** corpus-FIRST for the *speculative-decoding / inference-acceleration domain* **within the vault** (hand-grep of `_state/` + `_patterns/` returned no prior spec-decoding / draft-model / EAGLE / DFlash / MTP *subject*). A mint *would* therefore be corpus-first as a class. **DECLINED — recorded as a DEFERRED watch axis**, for the GLM-5 reasons:
1. **Goal-adjacent/off-goal single subject** — the exact reason GLM-5 v176 was NO MINT. §28 phantom-count inflation guard: minting a CORPUS-FIRST §C standalone ("Speculative-Decoding / Draft-Model Training Framework") on one goal-adjacent inference-infra subject is inflation.
2. **2nd data-point in the DEFERRED "model / inference-substrate" tier** — GLM-5 v176 flagged that tier and it was **DEFERRED at N=1**. DeepSpec makes it **N=2 in the broad area** (GLM-5 = a *frontier model*; DeepSpec = an *inference-acceleration framework/technique* — a different sub-class). This **strengthens** the eventual-tier case; it does not itself cross the mint bar.
3. **Kilo-Code-v177 "mint the exemplar" precedent doesn't fit** — that applies to a recurring *agent-capability* class within scope; this class (inference acceleration) is out of the agent-capability substrate the §C vocab is shaped for.
4. Mint on a cleaner in-scope exemplar later; DeepSpec becomes a credited prior data-point (§28 + §35) — the v179 camofox / v180 ai-telegram / v181 cortex-hub DEFERRED-watch template.

### SECONDARY observations (NOT minted)
- **#19 19a** — first *first-party* `deepseek-ai` org subject (institutional data-point; DeepSeek-TUI v72 = third-party, GLM-5 = Zhipu).
- **NOT Pattern #43 (Optimizer-Research Integration Velocity)** — LlamaFactory v22 / Unsloth are **weight-space *training* optimizers**; DeepSpec is **inference-time acceleration** via a trained auxiliary draft model (opposite optimization target). This is the exact SkillOpt v178 "NOT #43" reasoning (text-space ≠ weight-space; here: inference-time ≠ training-time). Cross-ref only.
- **Pattern #32 (Research-Paper-Chain Lineage) candidate cross-ref** — DeepSpec packages a published-paper lineage (its own DSpark paper + builds on EAGLE3 / DFlash / Leviathan 2023). A candidate #32 instance-strengthening data-point; **exact N deferred to audit, NOT self-incremented** (current #32 N not verified this session — fish-speech v20 / LlamaFactory-era set).
- **#66 supply-chain** — MIT, **no postinstall**, pure Python research code (torch/transformers/triton/CUDA). Benign; the "risk" is **compute + storage cost** (8 GPUs + 38 TB), not security. `pip install -r requirements.txt` pins exact versions.
- **NOT #57** — cites SpecForge/sgl-project, DFlash/z-lab, Qwen3, Gemma, Leviathan, DeepSeek-V3/V4 — **none are corpus subjects**; mentions ≠ recursion. (Thematic-only corpus adjacency: DeepSeek-TUI v72 was a TUI *for* DeepSeek-V4 models, and DSpark is *deployed in* DeepSeek-V4 — a link, not a citation.)
- **NOT #52** — 5.4k★/428 forks/**no releases** page-stated; §37.4 GitHub API mocked → velocity unestablishable.
- **#84 84c (minor)** — supports multiple target-model families (Qwen3 + Gemma4) × 3 algorithms; **NOT** the ponytail v168 "14-platform native-rule-file distribution" mechanism; **NO N-bump**.
- **Library-vocab #20 (Token-Economy-Quantification) QUALIFIED-ADJACENT** — DSpark's speed/accepted-length figures (60–85% faster gen; +30.9% τ) are DeepSeek's own page/paper-stated, unreplicated benchmarks → **N stays 4** (the v168/v172/v175 precedent).
- **NOT #18 B1-MCP** — a training framework, not an MCP server.

### NON-claims (guardrails)
NOT corpus-first spec-decoding **globally** (the external field is mature: EAGLE/Medusa/MTP/DFlash/SpecForge) — corpus-first is scoped to *the vault's own subject set*. NOT a frontier model (that's GLM-5 v176). NOT the first model-subject (fish-speech v20 TTS preceded; GLM-5 = first *frontier-LLM*). NOT #43. NOT a new top-level pattern.

### Tier
Like GLM-5 → no clean fit. Proposed **"Model / inference substrate" tier (audit-reviewable)**, now **N=2** (GLM-5 v176 frontier-model + DeepSpec inference-acceleration-framework). Artifact-type = an **ML research / training framework** — the LlamaFactory v22 / Unsloth / LLMs-from-scratch v74 / fish-speech v20 family. Provisionally a goal-aligned INCLUDE reference, **not T1**.

### State deltas
Counts UNCHANGED **46 / 11**; §C live standalones **31** (unchanged); tracked PROVISIONAL surface **≈38** (unchanged); streak **GA:46 → GA:47** *per operator direction* (⚠️ OFF-GOAL reading → GA:46 · OG:12); **§35 CLEAR** (rolling-3 window {v184 GA, v185 GA, **v186 GA**} = 0 OG; under OFF-GOAL reading = 1 OG ≤ 1 → still clear); **32 consecutive goal-aligned ships v153→v186** (GA reading).

---

## 7. inflation_check (§28)

Discipline **HELD**: **0 mints** (NO MINT — the GLM-5 template), max #85, counts **46/11 unchanged**, §C surface unchanged, no improper N-bumps (#20 stays 4; #43 not incremented — not an instance; #32 deferred to audit), no double-count, and the corpus-first-spec-decoding facet **recorded as a DEFERRED watch axis, not minted**. The "model/inference-substrate" tier stays **audit-deferred at N=2**.

---

## 8. Verification log (`feedback_wiki_verify_independently_check_collisions`)

- **Source-read + upstream research delegated** to a 14-agent **read-only** workflow (`wf_f69580d3-d6e`, ~1.02M subagent-tokens, 126s) — safe/factual only. **All corpus-fact / collision / identity / lineage claims verified BY HAND.**
- Hand-read: the **DSpark paper** (24 pp, myself), + `markov_head.py` / `confidence_head.py` / `draft_ops.py` (myself) → confirmed code matches paper + the Algorithm-1-not-in-repo scope gap.
- Hand-grep over `_state/*.md` + `_patterns/*.md` + `03 Projects/`: **CONFIRMED** (a) no prior speculative-decoding / draft-model / EAGLE / DFlash / MTP *subject* → corpus-first for the domain; (b) no "DeepSpec" collision; (c) **DeepSeek-TUI v72 is third-party** (`Hmbown`), **GLM-5 v176 is Zhipu** → DeepSpec = first first-party deepseek-ai subject; (d) **fish-speech v20** = first model-subject (TTS), **GLM-5 v176** = first frontier-LLM + the "model/inference-substrate" DEFERRED tier @N=1.
- **DeepSeek-V4 (arXiv 2606.19348) + HAI-LLM** cross-checked against the **paper's own references + footnote** (not just the web agent, which flagged HAI-LLM "unverified") → both confirmed from the primary source.
- **Dropped unverified sub-claims** from the web agents: SpecForge "Domino / D-PACE / SpecBundle" internals (kept only the NOTICE-verified "SpecForge = the training framework + Eagle3 impl DeepSpec forks"); DeepSeek-V4 param counts (1.6T/284B) framed as **page-stated** only.

---

## 9. Sources
- Repo: `github.com/deepseek-ai/DeepSpec` (commit `afdfa7c`) · DSpark paper `DSpark_paper.pdf` (in-repo).
- Speculative decoding: Leviathan 2023 [arXiv 2211.17192](https://arxiv.org/abs/2211.17192) · Chen 2023 [arXiv 2302.01318](https://arxiv.org/abs/2302.01318).
- EAGLE [arXiv 2401.15077](https://arxiv.org/abs/2401.15077) · EAGLE-3 [arXiv 2503.01840](https://arxiv.org/abs/2503.01840) · DFlash [arXiv 2602.06036](https://arxiv.org/abs/2602.06036) · SpecForge `github.com/sgl-project/SpecForge`.
- DeepSeek-V3 [arXiv 2412.19437](https://arxiv.org/abs/2412.19437) · DeepSeek-V4 [arXiv 2606.19348](https://arxiv.org/abs/2606.19348) · HAI-LLM `high-flyer.cn/en/blog/hai-llm/`.
- Corpus: GLM-5 v176 / DeepSeek-TUI v72 / cc-switch v73 / LLMs-from-scratch v74 / fish-speech v20 (`_state/03c` + `_state/05`).
- HTML artifact: https://claude.ai/code/artifact/a3ea641d-bfd1-4532-bd42-e08a24acd37e

---

**Next:** see `(C) DeepSpec — Pilot Methods Menu.md` for the "how do I actually apply this" ladder (spoiler: it's a *knowledge* subject — the honest top-3 is conceptual, not a deploy).
