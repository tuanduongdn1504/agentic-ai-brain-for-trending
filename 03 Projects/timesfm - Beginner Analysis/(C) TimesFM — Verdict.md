# (C) TimesFM — Verdict (v193 · LLM Wiki Routine v2.6)

**Subject:** `google-research/timesfm` — TimesFM, a pretrained decoder-only foundation model for time-series forecasting (Google Research). Apache-2.0. Latest **2.5** (200M / 16k context / calibrated deciles / XReg). Paper arXiv 2310.10688 (ICML 2024). Source-verified at commit `4a6c5cd` (2026-07-02). Repo ~26.5k★/2.6k forks (page-stated §37.4).

**Operator-requested** ("build LLM wiki from this + double deep dive into the original resource for knowledge + pilot to apply into my working flow, show me many methods").

---

## The four criteria

### (a) Anthropic / cultural-peer axis — **FAIL** (clean)
Google Research = a major corporate/institutional AI lab, **not Anthropic** ((a)-7 is Anthropic-only) and not the individual cultural-peer axis. This is the declared-non-Anthropic-institution situation (matches magika v44 / google_workspace_mcp v140 = prior Google subjects; ByteDance v143 / NVIDIA v169 / Zhipu-GLM-5 v176 / Microsoft-SkillOpt v178 / DeepSeek-v186). **First `google-research/` ORG subject**, but **Google is a returning author** → a **#19 19a** data-point, NOT corpus-first-Google. No heritage rescue (v159→v192 discipline).

### (b) Goal-relevance — **MODERATE (keys the tier; operator-directed)** ⚠️ OFF-GOAL CAPTURE equally defensible
Goal #1 = *"master Claude + autonomous agents for software development."* TimesFM's **domain (time-series forecasting) is off Goal #1** — it is not Claude, not an agent, not agent infra, not a coding tool. Held at MODERATE (not FAIL, not STRONG) because of two genuine on-goal bridges:
1. **It ships a first-party Claude Code Agent Skill** (`timesfm-forecasting/SKILL.md` + `AGENTS.md`, agentskills.io standard) — dead on the agent-skills substrate the vault studies (agent-skills-standard v76 / SkillOpt v178 / agent-skills v184).
2. **The realistic use is agent-orchestrated** — Claude Code orchestrating a forecast pipeline (query → forecast → backtest → gate → PR) is a real autonomous-agent-for-software task, on the `multi-agent-orchestration` pilot thread.

Plus a **sharp Goal-#2 (hireui) payoff**: recruitment-metric forecasting (application volume, source volume).

**Calibration:** a notch **above** GLM-5 v176's MODERATE (GLM-5 was a raw competitor LLM — "nothing to pilot but swap the backend"; TimesFM ships an installable Claude Code skill + a genuine agent-orchestration pilot) but **held below STRONG** because the model itself is an off-domain forecasting model, not the Claude/agent substrate. Per routine v2.5 §31, (b) MODERATE+ → **GOAL-ALIGNED INCLUDE per operator direction**; the **OFF-GOAL CAPTURE reading** (the model's domain is off Goal #1) is **equally/more defensible** and recorded operator-reviewable — the **GLM-5 v176 / DeepSpec v186 / AI-For-Beginners v191 template**.

### (c) Substance — **STRONG** (with honest caveats)
A real, significant, source-verified foundation model: 200M decoder-only transformer (20 layers / 1280 dims / 16 heads / RoPE / RMSNorm / fused QKV / input-patch-32 / output-patch-128 / calibrated deciles / ReVIN), torch + flax backends, HF checkpoints, XReg covariates, ICML 2024 paper, ~100B-token pretraining, competitive **#2 on GIFT-Eval**, deployed in **BigQuery ML / Sheets / Vertex**, ~26.5k★. **Caveats (verified):** CI is build-only (tests exist, not gated); univariate at heart (multivariate = workaround); quantiles uncalibrated until 2.5; `jax[cuda]` hardcoded → CPU-only extras break (#443); Apple-Silicon torch issues; 2 of 3 bundled skill examples use the stale 1.x API; no in-repo training code; leaderboard slipped behind Chronos-2; "not an officially supported Google product."

### (d) Corpus connections — **STRONG**
- **Model / inference-substrate tier** (the recurring "off-domain-but-goal-adjacent model" cluster): GLM-5 v176 (frontier LLM) · DeepSpec v186 (spec-decoding framework) · fish-speech v20 (TTS) · LLMs-from-scratch v74 · LlamaFactory v22.
- **Agent-skills substrate** (via its first-party SKILL.md): agent-skills-standard v76 · SkillOpt v178 · agent-skills v184 · ponytail v168.
- **Agent-orchestration** pilot thread (the realistic use pattern) · **claude-api-cost-optimization** thread (BigQuery/Vertex cost) · **Google-author cluster** (magika v44 / google_workspace_mcp v140).
- **Sharp cross-ref to v192 palmier-pro:** the *"product/model retrofitted to be agent-native via a first-party agent interface"* meta-move — palmier-pro bolted on an **MCP server**, TimesFM bolts on an **Agent Skill + Vertex agentic-calling endpoint**. Two instances now; recorded as a DEFERRED watch axis (below).

---

## Pattern outcome — **NO MINT**

- **No new top-level pattern** (max stays **#85**).
- **No new §C standalone.** A mint *could* be argued as **"corpus-first time-series-forecasting foundation model"** (hand-grep confirmed the corpus has **zero** prior forecasting-model / TimesFM / Chronos / Moirai subject — a genuinely new domain). **Mint DECLINED** per §28 (phantom-count-inflation guard): a single off-domain / goal-adjacent model is **not a recurring capability class** the corpus tracks; §C vocab is tool/capability-shaped; off-domain models have only ever entered as **goal-adjacent knowledge data-points** (GLM-5 v176, DeepSpec v186, fish-speech v20). Minting corpus-first at N=1 on an off-domain single model = exactly the inflation the routine fights. **Recorded as a corpus-knowledge data-point in a new domain (time-series forecasting FMs) + a DEFERRED watch axis** (the GLM-5 / DeepSpec / cortex-hub "recorded-not-minted, deferred to audit" template).
- **Counts UNCHANGED: 46 confirmed top-level patterns / 11 CONFIRMED Library-vocab.** §C live-standalone surface UNCHANGED (35).

**SECONDARY (NOT minted):**
- **#19 19a** — first `google-research/` org subject; Google a returning author.
- **First-party Agent-Skill packaging** cross-ref (agent-skills-standard v76 / agentskills.io) — a data-point, NOT a mint (TimesFM is a *model that ships one skill*, not a skill collection).
- **"Model/product retrofitted to be agent-native"** watch axis — v192 palmier-pro (MCP-on-a-video-editor) + v193 TimesFM (Agent-Skill + Vertex-agentic-endpoint-on-a-forecasting-model). **2 instances → DEFERRED to the ~v192-due audit** (is this a forming axis? record, don't mint at N=2 across such different shapes).
- **"Model / inference-substrate" tier** — now GLM-5 (frontier LLM) / DeepSpec (spec-decoding) / TimesFM (forecasting FM) / fish-speech (TTS): the tier keeps filling; flag to audit.
- **#66** supply-chain: **BENIGN** (Apache-2.0, no postinstall/curl-bash/telemetry; the real risks are install-fragility, not security).

**NON-claims:** NOT a new top-level pattern (max #85) · NOT corpus-first-*as-a-mint* (corpus-first for the forecasting domain is TRUE but earns no §C entry — see above) · NOT **#52** (stars/HF-downloads page-stated §37.4 → velocity unestablishable) · NOT **#57** (cites no corpus subjects; competitors Chronos/Moirai/TimeGPT are not corpus subjects) · NOT **#18 B1-MCP** (ships an **Agent Skill**, not an MCP server; the Vertex "agentic-calling" endpoint is a managed REST service, not an MCP server) · NOT the first model-subject (fish-speech v20 TTS preceded; GLM-5 v176 = first frontier-LLM; TimesFM = first **forecasting** FM).

---

## Tier

**"Model / inference substrate" (audit-reviewable)** — the GLM-5 v176 / DeepSpec v186 provisional-tier precedent. Artifact-type = ML foundation model + installable inference package + first-party agent skill (the fish-speech v20 / LlamaFactory v22 / DeepSpec v186 family). Provisional label: **"Domain foundation model (time-series forecasting) shipped as an installable inference package + Claude Code agent skill."** NOT T1 (it ships a skill but isn't a skill collection); NOT cleanly T2 (it's a model, though its package + BigQuery/Vertex surfaces are service-like). Counts UNCHANGED 46/11.

---

## Streak & ceiling

- **Streak: `GA:54` per operator direction** (39 consecutive goal-aligned ships v153→v193).
- ⚠️ **Under the OFF-GOAL reading** (TimesFM joining v176/v186/v191 as OFF-GOAL-defensible off-domain models): **GA:50 · OG:15**.
- **§35 soft off-goal ceiling:** under the **GA reading**, window {v191 GA, v192 GA, **v193 GA**} = 0 OG → **CLEAR**. ⚠️ Under the **strict reading**, {v191 OG, v192 GA, **v193 OG**} = **2 OG in the rolling-3 window → BREACH** → the next ship should be goal-aligned or carry a logged `[ceiling-override]`. **Recorded operator-reviewable** (matches how the shim treats GLM-5 v176 / DeepSpec v186 / AI-For-Beginners v191).
- Lifetime operator overrides = 10 (3 logged `[ceiling-override]`); v153→v193 = **zero** overrides. Off-goal-intake via operator *direction* (not the override door), consistent with the GLM-5/DeepSpec/AI-4B precedent.

---

## Verification log (per `feedback_wiki_verify_independently_check_collisions`)

- **Verdict produced INLINE + hand-verified.** A read-only 8-agent workflow (`wf_a9c67046-b37`, ~1.22M subagent-tokens, 159 tool calls, 0 errors/empty) did **source-reading + upstream research ONLY**. **All corpus/collision/identity claims verified BY HAND.**
- **Collision grep** (`_state/` + `_patterns/` + `03 Projects/`): clean — no prior time-series / forecasting-model / TimesFM / Chronos / Moirai subject; "forecast"/"moment" hits are the vault's own bookkeeping + an old HR-SaaS "forecast" screen. `google-research/` org: first (Google returning via magika v44 / google_workspace_mcp v140).
- **Source hand-read** by me: README (full), LICENSE, pyproject, requirements, `AGENTS.md`, `SKILL.md` (511 lines), `configs.py`, `src/timesfm/__init__.py`, the anomaly example, + `git ls-tree` (102 tracked files). The src-architecture agent's output cross-matched my hand-reads exactly (correct line numbers → real tool calls, not confabulated).
- **Confabulations caught + discarded:** two false "doc-drift" findings (partial LFS-blocked checkout — `v1/`, `v1/tests/`, `scripts/`, `references/`, `examples/` all verified present at HEAD); two agents' garbled release dates (used README's own log); the recruiting agent's approximated/fabricated code + "BigQuery isn't really TimesFM" claim (replaced with source-verified API + the verified BigQuery built-in-`AI.FORECAST` fact).
- **inflation_check = discipline HELD:** 0 mints (the tempting "corpus-first forecasting FM" mint DECLINED as §28 inflation), max #85, counts 46/11 unchanged, §C surface unchanged, no N-bumps, corpus-first-domain fact recorded-not-minted, NO-MINT is the whole outcome.
- ⚠️ **Ultracode note:** a workflow was used for read-only research (per the standing ultracode directive), but per the vault's verify rule the **verdict + every corpus claim were done by hand** — the workflow's role was bounded to source/upstream fact-gathering.

---

**Bottom line:** A high-quality, source-verified Google foundation model whose *domain* is off your Goal #1 but which is **goal-adjacent + genuinely pilotable** (first-party Claude Code skill + agent-orchestration pattern) and has a **real Goal-#2 hireui payoff** (recruitment forecasting). Built at operator request; NO MINT; counts 46/11 unchanged; GOAL-ALIGNED per operator direction (OFF-GOAL defensible, §35 flag recorded). See the Pilot Methods Menu.
