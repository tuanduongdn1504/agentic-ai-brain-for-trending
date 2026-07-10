# (C) career-ops — Verdict (LLM Wiki v200)

**Subject:** `santifer/career-ops` @ `e9bacc48` · **Ship:** v200 (the 200th LLM-Wiki) · **Date:** 2026-07-09 · **Routine:** v2.6.

## Headline

**GOAL-ALIGNED INCLUDE 3/4** — `[(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG]`.
**Pattern outcome: 1 NEW §C standalone at N=1 — "Agent-First End-to-End Candidate-Side Job-Search / Career-Operations Pipeline" — CORPUS-FIRST for the surface, NOT world-first. NO-MINT alternative recorded.**
**Counts UNCHANGED 46/11.** §C live standalones **39 → 40**; tracked PROVISIONAL surface ≈46 → **≈47**. **Streak GA:60 → GA:61** (47 consecutive goal-aligned ships v153→v200). **§35 CLEAR** (window {v198 GA, v199 GA, **v200 GA**} = 0 OG).

---

## The four criteria

### (a) Anthropic-authored? — **FAIL (clean)**
Santiago Fernández de Valderrama (`@santifer`) is a **disclosed individual** — Head of Applied AI at **Zinkee** (a Spanish SaaS company), ex-founder of a Spanish phone-repair business (Santifer iRepair, 2009–2025, exited), based in Seville. **NOT Anthropic** — verified independently by hand (my own WebSearch + `CITATION.cff` + `LICENSE` + `package.json`, which all name "Santiago Fernández de Valderrama"; the first WebFetch's "Santiago Ferreira" was a small-model confabulation, corrected). First `santifer` author → **#19 19a** institutional/portfolio data-point. He is another **disclosed indie builder** (the Waishnav v171 / Neo Reid v174 / Jack Le v181 / Evan Bacon v183 / Addy Osmani v184 / calesthio v188 / Cobus Greyling v189 / Dmitriy Kovalenko v194 lineage) → **reinforces, does not reopen**, the disclosed-indie-builder (a)-axis held operator-reviewable at N=3+ per the v182 audit; NOT registered. *(A workflow agent's "Anthropic AI Fluency educator credential" + exact GitHub-API dates are sourced to the mocked GitHub API (§37.4) → unverified, not relied upon; an education credential ≠ employment ≠ (a)-7 regardless. (a) FAILS cleanly either way.)*

### (b) Goal-relevance? — **STRONG (keys the tier)**
career-ops is Claude-Code-first (`cd career-ops && claude`; "Built with Claude Code" badge) and a **mature, agent-native operational system** = dead-center on the Goal-#1 agent substrate: agent-first (the coding agent IS the runtime), the open agent-skill standard, multi-CLI via one symlinked SKILL.md, deterministic-Node-offload, a strict system/user data contract, a self-updater, zero-token cost design, and a genuine subagent cost guardrail + anti-fabrication provenance rules — one of the richest agent-engineering exemplars in the corpus. **AND** it has the sharpest Goal-#2 (hireui) angle of the recent run: it is the **domain-exact inverse** of hireui (candidate-side scoring/tailoring vs employer-side screening) — directly informative for red-teaming hireui's screening, mirroring career-ops's scoring/legitimacy/comp rubric into hireui, and modelling the EU-AI-Act/GDPR/human-in-the-loop ethics hireui must build.
**STRONG-not-STRONGEST** because: third-party + candidate-side (not the operator's employer-side product) + the domain is job-search/career-ops (not software-dev agent infra) + Claude is one of 8+ harnesses. GOAL-ALIGNED without question (§31 keys the tier on (b) STRONG). *(Operator-reviewable: arguably STRONGEST for Goal #2 given the domain-exact inverse relationship — recorded, not asserted.)*

### (c) Engineering substance? — **STRONG**
Genuinely substantial and mature: ~50 single-job Node scripts + ~53 zero-token provider modules + a Go Bubble Tea TUI + an alpha Next.js web UI; a 1–5 evaluation rubric with 6 archetypes + Block-G scam detection + a 10-type comp-reliability taxonomy; two ATS-safe PDF pipelines (defensive not injective) + a two-tier Voice-DNA anti-slop guardrail; a strict data contract + a self-updater with import-closure resolution + atomic report-number reservation; **66 test files / 513+ assertions**; 11 CI workflows incl. CodeQL + a hard-blocking user-data guard; 4 model-agnostic evaluator backends; v1.18.0 / multiple releases per week; 15 README translations; full governance docs.
**Honest caveats (foregrounded):** the *hard AI* is the underlying CLI/model (career-ops orchestrates prompts + deterministic scripts, doesn't build a model); the case-study metrics (740+/100+/landed-a-role) are self-stated marketing; stars/velocity are page/web-stated only (no #52); ~3 months old, launch-viral, one active maintainer (SPOF); the `dependency-review` CI is currently non-blocking (issue #343).

### (d) Cross-references? — **STRONG**
- **hireui (Goal #2)** — the domain-exact inverse; the `miai-cv-matching` memory thread (a CV↔job matching agent) is the domain-adjacent sibling.
- **The mint boundary:** OpenMontage v188 §C (the "agent-first end-to-end operational pipeline, coding-agent-as-runtime, deliverable = artifacts" shape — career-ops is analogous) vs ai-berkshire v187 (the Domain-Vertical-Skill-Collection *reasoning* shape — the NO-MINT foil).
- **Skill-collection / agent-first-system genre:** agent-skills v184, CodexKit v121, karpathy v63, ai-berkshire v187.
- **Open agent-skill standard (agentskills.io):** agent-skills-standard v76, serve-sim v183, ponytail v168, SkillOpt v178.
- **Provider-agnostic #84 84c** (one SKILL.md → 8+ CLIs via symlink + 4 standalone evaluators).
- **files-are-canonical-databases-derived** — the vault's own LLM-Wiki files-as-brain philosophy + loop-engineering v189 STATE.md conventions + OpenMontage v188 JSON-state.
- **deterministic-tool-offload** — the ai-berkshire v187 `financial_rigor.py` / OpenMontage v188 deterministic-tool substrate pattern, at ~50-script scale.
- **claude-api-cost-optimization thread** — zero-token scan + cheap/local evaluators + budget doc + the subagent cost guardrail.
- **multi-agent-orchestration thread** — batch parallel sub-agent workers + the anti-swarm "single-pass workers, never nest, never call recursive research" rule.
- **Playwright browser-automation** — browser-use v41, Skyvern v24, crawl4ai v29, serve-sim v183, camofox v179, page-agent v199 (career-ops *uses* Playwright; a substrate consumer, not a #57 citation).
- **Voice-DNA anti-slop** — ponytail v168, taste-skill v81/v85, the voice-calibration §C standalone (v108/v138).

---

## Pattern outcome — the mint

**1 NEW §C standalone at N=1 — "Agent-First End-to-End Candidate-Side Job-Search / Career-Operations Pipeline (a self-contained, local-first, AI-coding-CLI-native system where the coding agent IS the runtime: zero-token discovery/scan → 1–5 CV-vs-JD scoring + archetype + posting-legitimacy → ATS-safe CV/cover-letter generation → tracked application pipeline with a strict system/user data contract + self-updater; filter-not-spray, human-in-the-loop, never-auto-submit)."**

**Corpus-first — collision-clean (hand-verified).** A grep of `_state/` + `_patterns/` + `03 Projects/` for career-ops / job-search / career / résumé / ATS / CV-matching / greenhouse / ashby / jobscan / cover-letter returns **no prior corpus subject** in this space. The only faint hits are individual *listed skills* inside the awesome-claude-skills v50 catalog (`tailored-resume-generator`, `composio-skills/ashby-automation`, `lever-automation`) — catalog entries, not subjects. The full §C live-standalone registry (rows through v199) confirms **no job-search / career / résumé / ATS standalone exists**.

**Why MINT (analogous to OpenMontage v188, not ai-berkshire v187):** the Domain-Vertical-Skill-Collection instances (SEO v64 / academic v90 / cybersecurity v98 / finance v187) are **knowledge-work reasoning collections** (the agent reasons → outputs text; tools are calculators). career-ops is structurally **more** — a full **operational pipeline** (a discovery/scanner layer + a scoring engine + an artifact-generation layer + a tracking DB with a data contract + a self-updater + a Go TUI + eval harnesses) whose deliverable is a **tracked pipeline + generated artifacts**, with the **coding agent as the runtime**. That is the exact boundary OpenMontage v188 minted on ("agent as production director conducting a manufacturing pipeline, deliverable is a file, not analysis text") — applied to a **new capability domain** (candidate-side career operations) that is also the domain-exact inverse of the operator's Goal-#2 product.

**Scope honestly bounded: CORPUS-FIRST for the surface, NOT world-first.** The AI-job-search space is densely populated commercially (Jobscan / Teal / Careerflow — quality/tailoring SaaS; LazyApply / ApplyPilot / LinkedIn_AIHawk / LoopCV — quantity auto-apply bots) and résumé keyword-optimization + ATS scanners + auto-apply all pre-exist. The landscape research found **no direct peer for the specific conjunction** career-ops occupies (candidate-side + local-first OSS + runs *inside* your AI coding CLI as an agent-skill system + filter-not-spray + human-in-the-loop-never-submit + scoring+tailoring+scanning+tracking+self-updater); the closest OSS peer (ApplyPilot, Feb 2026, AGPL-3.0) is a standalone Python auto-apply bot, NOT CLI-native. Mint at N=1 per the serve-sim v183 / fff v194 / openwiki v195 / video-use v198 / page-agent v199 precedent (strong real anchor: mature production system, no direct peer on the surface). **§28 ≤2-new-standalones cap honored (1 mint).**

⚠️ **NO-MINT alternative recorded (operator/audit-reviewable)** — the ai-berkshire v187 / camofox v179 discipline: *"career-ops is simply the job-search vertical of the Domain-Vertical-Skill-Collection tier sub-archetype (SEO/academic/cybersecurity/finance → job-search) → instance-strengthening (the sub-archetype → N=5), no fresh standalone."* **Leaned MINT** because career-ops is an end-to-end *operational* pipeline (not a reasoning-skill collection), corpus-first-for-surface with no direct OSS peer, in a genuinely new domain. **Either reading counts UNCHANGED 46/11.**

**Tier: T1 Skill/Methodology Collection (Candidate-Side Job-Search / Career-Operations Pipeline flavor)** — the OpenMontage v188 / agent-skills v184 / ai-berkshire v187 family. ⚠️ Audit-reviewable: career-ops has more T5-ish application breadth (Go TUI + web UI + self-updater + plugin registry) than a typical T1; filed T1 with the note, consistent with OpenMontage v188's T1 filing.

### Secondary observations (NOT minted)
- **#19 19a** first `santifer` / Fernández de Valderrama author (disclosed indie builder; reinforces-not-reopens the (a)-axis).
- **#84 84c** provider-agnostic (one canonical SKILL.md symlinked to 8+ CLIs + 4 standalone evaluators; **NO N-bump** per v86 — multi-harness ≠ the ponytail v168 14-platform generator; career-ops distributes ONE skill that many CLIs consume via symlink).
- **#12** LLM-routing artifacts (AGENTS.md/CLAUDE.md/CODEX.md/OPENCODE.md/GEMINI.md/KIMI.md + per-CLI skill dirs; high-density but incidental; **NO N-bump**).
- **files-are-canonical-databases-derived (RFC #918)** + system/user data contract — a strong **vault-meta** cross-ref (the vault's own files-as-brain philosophy); design-philosophy cross-ref, NOT a mint.
- **deterministic-tool-offload** (~50 zero-LLM single-job scripts) — the ai-berkshire v187 / OpenMontage v188 pattern; cross-ref, NOT a mint.
- **claude-api-cost-optimization** + **multi-agent-orchestration** threads (zero-token scan, 4 cheap/local evaluators, the anti-swarm cost guardrail, batch sub-agents).
- **Voice-DNA anti-slop** cross-ref (ponytail v168 / taste-skill / voice-calibration §C) — a *feature* of generation, not a standalone.
- **#66 supply-chain:** install BENIGN (postinstall Chromium transparent; 4 minimal deps; zero telemetry; no-user-data hard-blocking CI), data-privacy BENIGN (PII local-only), dual-use MODERATE-conservatively-handled (public-ATS scraping only + ToS/anti-spam disclaimer + reject-ToS-violating-contributions; defensive-not-injective ATS; never-auto-submit in code). Open: dependency-review non-blocking (#343); node:sqlite needs Node ≥22.5.

### Non-claims
NOT a new top-level pattern (max #85) · NOT corpus-first AI-job-search globally (dense landscape) · NOT world-first · NOT #52 (59.2k★/11.6k forks/21 releases/v1.18.0 + Trendshift + "46k stars in first month" all page/web-stated, GitHub API mocked §37.4 → velocity unestablishable; a clearly viral launch, recorded qualitatively) · NOT #57 (runs inside Claude Code/Codex/Gemini as harnesses + uses Playwright/Greenhouse/Ashby as deps + the agentskills.io standard + the cv-santiago sibling repo; none are corpus subjects cited as influences; mentions/deps/harness-targets ≠ recursion) · NOT #18 B1-MCP (an agent-skill + Node-script + Go-TUI system, not an MCP server) · NOT the Domain-Vertical-Skill-Collection tier instance (that's the recorded NO-MINT alternative).

---

## Confabulation log (verification transparency — per `feedback_wiki_verify_independently_check_collisions`)

The verdict + every corpus/collision/identity/mint claim + all load-bearing quantitative facts were produced **INLINE + hand-verified**. A read-only 13-agent workflow (`wf_045c237d-fb8`, ~2.45M subagent tokens, 226 tool uses, all agents on **Haiku** → elevated confabulation risk) did source-reading + web research ONLY; **11/13 succeeded, 2 failed ("Prompt is too long": `src:scanner` + `src:domain-engines`) + 1 dud (`web:health-community` returned a "I don't know the project name" non-answer, toolCalls=0) — all three hand-covered.** Confabulations caught + corrected:

1. First WebFetch: **"Santiago Ferreira"** → CORRECTED to **Fernández de Valderrama** (CITATION/LICENSE/package.json + WebSearch).
2. Scoring-brain (Haiku): **"25/20/15/15/15/10% weights + a 6th 'intuition' dimension"** → CONFABULATED; `oferta.md:404` = *"average of block scores (default), user-overridable"*, `_shared.md` = 5 dimensions, no fixed percentages. **Not cited as fact.**
3. Scoring-brain (Haiku): **"Block G caps the score at 3.5 (hard veto)"** → CONTRADICTED by `_shared.md:65` (*"Block G … does NOT affect the 1-5 global score — a separate qualitative assessment"*). **Corrected.**
4. Scoring-brain (Haiku): threshold muddle "<4.0" AND "<3.5" → `_shared.md` authoritative = **<3.5 recommend-against** (README markets <4.0). **Documented as doc-vs-code.**
5. Identity (Haiku): **mocked-GitHub-API dates** (profile 2026-01-23, repo 2026-04-04, "59,210 exact") + **"Anthropic AI Fluency educator credential"** → provenance is the mocked API (§37.4) → **NOT relied upon**; the core (a)-FAIL fact confirmed by my own WebSearch + repo files.
6. Doc-vs-code caught by hand: README **"21 provider modules"** → actual **~53** provider files; README **"A-F scoring / 10 weighted dimensions"** → code **A–G blocks / 1–5 avg-of-blocks / 5 dimensions**; ARCHITECTURE.md "500+ checks" ≈ **513+ assertions** (source-discoverable, not a marketing headline).
7. `web:health-community` dud discarded; project-health assembled by hand from the other agents (Trendshift #25195, Product Hunt, Discord, 15 translations, BI/WIRED, plugins-registry) — qualitative, no #52.

**inflation_check = discipline HELD** (1 mint ≤2 cap; N=1 corpus-first-for-surface, NOT world-first; NO-MINT alternative recorded; counts 46/11 unchanged; max #85; no double-count [#84 84c NO N-bump]; no N-bumps).

**Loop-budget note:** the workflow spent ~2.45M subagent tokens; with main-loop reads the ship crossed the 80% line of the 3M soft cap during doc-writing → **self-throttled per the binding rule + the v191 precedent: no further fan-outs; the optional loop-verifier agent SKIPPED** (inline hand-verification stands — 7 confabulations caught by hand); ship completed as the operator-requested deliverable under the 3M soft cap.
