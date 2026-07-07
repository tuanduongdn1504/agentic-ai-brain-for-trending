# (C) mlsysbook — Verdict (v197, routine v2.6)

**Subject:** `harvard-edge/cs249r_book` — "Machine Learning Systems" (MLSysBook.ai), Vijay Janapa Reddi / Harvard. Two-volume open textbook + integrated curriculum; MIT Press hardcopy 2026.
**Date:** 2026-07-07. **Verdict produced INLINE + hand-verified** per `feedback_wiki_verify_independently_check_collisions`.

---

## Decision: GOAL-ALIGNED INCLUDE 3/4 — T3 Education — **NO MINT** — counts **46/11 UNCHANGED**

| Axis | Call | Reason |
|---|---|---|
| **(a) Anthropic-authored / cultural-peer** | **FAIL** | Harvard University / Prof. Vijay Janapa Reddi — a major academic institution, **not Anthropic** ((a)-7 is Anthropic-only). **First `harvard-edge` org subject** → a **#19 19a** institutional-portfolio data-point, NOT a new (a) axis. No heritage/name rescue (v159→v196 discipline). |
| **(b) Goal-relevance** | **MODERATE (keys the tier)** | An **ML-systems-engineering curriculum** — the discipline *underneath* the tools, teaching what a production AI system is, how to serve/evaluate/deploy/govern one, and (uniquely) **responsible-AI-for-hiring** (the Amazon-recruiting-bias / proxy-variable content is literally hireui's domain). On-goal-adjacent via: the "what Claude/an LLM feature is made of at the systems level" spine, the hireui-LLM-feature relevance, SocratiQ's genuine multi-agent content, StaffML's interview-design method, and design-grammar mirroring the vault's own method. **Held below STRONG:** it's a textbook/curriculum, not installable tooling on the Claude/agent substrate. ⚠️ **STRONG is a defensible operator-reviewable reading** (arguably the strongest-MODERATE education subject the corpus has had); **OFF-GOAL is also defensible** (an ML-systems curriculum, not the Claude substrate — the AI-For-Beginners v191 / TimesFM v193 situation). GOAL-ALIGNED per §31 (keys on (b) MODERATE+) + operator direction ("build LLM wiki + double deep dive + pilot to apply into my working flow"). |
| **(c) Craft / substance** | **STRONG** | An enormous, mature, genuinely-engineered artifact: two-volume physics-first textbook (Hennessy-&-Patterson model) + 20-module TinyTorch + a systems simulator embedded in the chapters + 9,000-question AGPL interview vault + Marimo labs + hardware kits + an instructor blueprint + a multi-agent AI tutor + a formal design-grammar; MIT Press hardcopy; **agent-maintained via a bespoke `binder` validation CLI** + pre-commit + Vale + pytest. Multi-license discipline (5 distinct licenses, per-component). |
| **(d) Cross-references** | **STRONG** | Dense education cluster (**ai-agents-for-beginners v6, dive-into-llms v39, LLMs-from-scratch v74, easy-vibe v77, AI-For-Beginners v191, DeepTutor v38, HF agents-course, system-design-academy, ai-engineering-from-scratch, build-your-own-x**) + ML-training-substrate (LlamaFactory v22, fish-speech v20, DeepSpec v186) + SocratiQ→multi-agent-orchestration + StaffML→hireui-recruitment + design-grammar→the vault's own Pattern Library + the meetily-v196 "vendor seam" echo (SocratiQ's provider-fallback). |

---

## Pattern outcome: **NO MINT** (T3 Education instance-strengthening)

- **No new top-level pattern** (max stays **#85**). **No new §C standalone.** **Counts UNCHANGED 46/11.** §C surface unchanged.
- **T3 Education instance-strengthening** — the AI-For-Beginners v191 / DeepSpec v186 / TimesFM v193 handling. MLSysBook is **corpus-first for a DOMAIN** (ML-systems-engineering education — collision grep clean, no prior Harvard/Reddi/MLSysBook/cs249r/TinyTorch/StaffML/SocratiQ subject) — but **corpus-first-for-a-domain ≠ a mintable capability class** (the TimesFM v193 / meetily v196 discipline). A tempting *"corpus-first ML-systems education subject"* §C mint is **DECLINED per §28** (a single-domain educational curriculum is not a recurring, tool/capability-shaped class; §C vocab is capability-shaped).

### Candidate mints considered and DECLINED
1. **"Corpus-first ML-systems-engineering education subject"** — domain-first, not a capability class. **DECLINE** (TimesFM v193 / meetily v196 discipline).
2. **SocratiQ = "embedded AI Socratic tutor in a static learning site."** A candidate corpus-first facet — but **DeepTutor v38** (`HKUDS/DeepTutor`, "Agent-Native Personalized Tutoring", **T5**) is the prior AI-tutor precedent, and SocratiQ is an experimental *sub-component* of this subject, not the primary subject. Minting on an experimental sub-feature = §28 inflation. **DECLINE**, record as a watch/cross-ref.
3. **"The repository IS the curriculum" — one integrated repo unifying textbook + framework + simulator + kits + labs + interview vault + tutor + design-grammar.** A distinctive *scale/integration* facet — but integration-not-capability (the cortex-hub v181 discipline: minting on packaging = "draw-the-circle"). **DECLINE**, record as the distinguishing T3-Education facet (the "learning ecosystem" scale — the largest in the corpus).
4. **TinyTorch = build-your-own-framework.** **LLMs-from-scratch v74** (build-your-own-LLM) + **build-your-own-x** are the precedents. Not corpus-first. **DECLINE**, cross-ref.
5. **design-grammar = "formal grammar of ML-systems design (primitives + rewrite rules)."** Genuinely novel + vault-relevant, but an *experimental sub-component*, N=1, packaging-not-capability. **DECLINE**, record as a DEFERRED watch axis + the sharpest vault cross-ref.

### SECONDARY (NOT minted)
- **#19 19a** — first `harvard-edge` org author; Reddi is a returning cultural-landscape figure via TinyML/MLPerf (no prior corpus subject).
- **#12 LLM-routing-artifacts / agent-maintenance data-point** — the book is Claude+Codex agent-maintained via `.claude` rules + a bespoke `binder` CI; the interview corpus is Gemini-generated + AI-math-verified with a `human_reviewed` provenance trail. (The AI-For-Beginners v191 "agent-maintained education repo" data-point, one notch richer.) NO N-bump.
- **AI-generated-corpus provenance** — StaffML questions carry `validation_model`/`math_model`/`human_reviewed:not-reviewed` fields = a corpus-quality audit-trail data-point (cross-ref the vault's own inflation-check discipline).
- **#84 84c adjacency** — SocratiQ's 8-provider fallback chain + the "build fallback for prod, buy for dev" serving pattern = provider-agnostic *by design*; the meetily v196 vendor-seam echo. NO N-bump (it's a sub-component's config, not the primary subject's distribution mechanism).
- **T3 sub-typology question** (open since v115, re-raised at v191): whether the T3 Education tier needs formal sub-archetypes (structured-curriculum v6/v191 vs. build-from-scratch v74 vs. reference-index vs. integrated-ecosystem-v197). **Recorded, DEFERRED to the badly-overdue ~v192 audit** — NOT self-incremented.

### NON-claims (explicit)
- **NOT #52** (stars/adoption page-stated only, §37.4 — the repo mocks the GitHub API → velocity unestablishable; MIT Press deal + "100k learners" goal are page/press-stated).
- **NOT #57** (cites Hennessy&Patterson, Barroso, Sculley, Chinchilla, Chip Huyen, Goodfellow, d2l.ai, fast.ai as landscape/upstream — none are corpus subjects; mentions/comparison ≠ influence-citation).
- **NOT #18 B1-MCP** (a textbook + curriculum; SocratiQ is a Shadow-DOM widget + Cloudflare proxy, not an MCP server).
- **NOT a new top-level pattern** (max #85).
- **NOT corpus-first education** (ai-agents-for-beginners v6 precedes by ~191 wikis; the T3 cluster is dense).
- **NOT the first model-subject / not a model at all** (it's a textbook *about* building ML systems; fish-speech v20 was the first model-subject).

---

## Tier: **T3 Education** (the ai-agents-for-beginners v6 / LLMs-from-scratch v74 / AI-For-Beginners v191 family; the corpus's largest integrated learning *ecosystem*).

## Counts / streak / §35
- Counts **UNCHANGED: 46 confirmed top-level patterns / 11 CONFIRMED Library-vocab.** §C live standalones **37** (unchanged). Tracked PROVISIONAL surface **≈44** (unchanged).
- **Streak: GA:57 → GA:58** *per operator direction* (44 consecutive goal-aligned ships v153→v197). ⚠️ Under the defensible OFF-GOAL reading (joining v176/v186/v191/v193/v196), the alt tally is `GA:52 · OG:17`.
- **§35 CLEAR** — rolling-3-ship window {v195 GA, v196 GA(⚠️OG-defensible), **v197 GA**} = 0–1 OG ≤ 1.

---

## Verification (hand-done)
- **Collision grep clean:** subject-specific grep (`mlsysbook|cs249r|tinytorch|staffml|socratiq|harvard-edge`) over `_state/` + `_patterns/` returned **zero files** → corpus-first as a subject. ("vijay/reddi" hits are all "Reddit" from Agent-Reach v174 etc.)
- **DeepTutor v38** confirmed as the prior AI-tutor precedent (`HKUDS/DeepTutor`, T5) — anchors no §C standalone → SocratiQ mint temptation defeated.
- **Education cluster confirmed** present (v6/v38/v39/v74/v77/v191 + HF agents-course + system-design-academy + build-your-own-x).
- **Knowledge extraction faithful:** the 8 chapter-reader agents all had `toolCalls > 0` (8/11/…), and their extractions match my own hand-read of `ml_systems.qmd` exactly (constraints-drive-architecture / D·A·M / 4 paradigms) — no confabulation (the v191 per-agent-toolCalls lesson applied). I also hand-read `README.md`, `LICENSE.md`, `CITATION.cff`, `vol1/index.qmd`, `ml_systems.qmd`, `socratiq/README.md`, `interviews/README.md` + a real question YAML (`cloud-0231.yaml`), `design-grammar/README.md` + `grammar.yml`, `CLAUDE_RESUME_FULL_AUDIT.md`, `tinytorch/README.md`.
- **inflation_check = HELD:** 0 mints; the corpus-first-ML-systems-domain + SocratiQ + design-grammar + integrated-ecosystem facets each DECLINED per §28/§C-is-capability-shaped; max #85; counts 46/11 unchanged; no N-bumps; no double-count.

⚠️ **Ultracode note:** a read-only research workflow was used for the source-reading double-dive (per the standing directive); the **verdict + every corpus/collision/identity claim were done BY HAND.** The workflow hit a subagent weekly-limit at 8/13 agents; the 5 uncompleted (components + upstream identity/landscape/security) were fully covered by my own hand-reads — no verdict gap.
