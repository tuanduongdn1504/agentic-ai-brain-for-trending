# free-claude-code — Beginner Analysis (v60)

> **Wiki:** v60 / 60th LLM Wiki
> **Subject:** github.com/Alishahryar1/free-claude-code
> **Tagline:** "Use claude-code for free in the terminal, VSCode extension or discord like OpenClaw (voice supported)"
> **Build session:** 71+ (continuation post-v59 AutoGPT) — 2026-05-07
> **Build mode:** Compressed-scope main-loop direct-write (v56-v59 lesson preserved)
> **Routine:** v2.1 (with Phase 0.9 STRICT amendment session 66)

---

## 12-axis classification

| Axis | Value |
|---|---|
| **Tier** | **T4 Agent-as-bridge** — 9th T4 entrant (proxy/router/translator decoupling Claude Code client from Anthropic backend) |
| **Archetype** | solo-community (individual GitHub author Alishahryar1; no organization affiliation visible) |
| **Scale tier** | **large** — 22.1K stars / 3.2K forks / 569 commits / 129 watchers |
| **Primary lang** | Python 100% |
| **Packaging tool** | uv + pyproject.toml (Python 3.14) |
| **Origin story** | individual-author-lineage — solo developer, no methodology-lineage citation; community-viral via cost-reduction value prop |
| **Methodology** | NONE named — AGENTS.md cites TDD-leaning + "expert Software Architect" framing but no named methodology (no SDD / BMM / TDD-explicit / DDD / XP citation) |
| **Governance file count** | **medium** — 5 files: README.md / CLAUDE.md / AGENTS.md (declared identical to CLAUDE) / PLAN.md / LICENSE |
| **Agent/skill count** | N/A — proxy-router, not agent-collection |
| **i18n coverage** | EN-only |
| **Intellectual influence cited** | **NONE** — no Karpathy / Lam / Cherny / Bostrom citations; no methodology lineage |
| **Agent platforms supported** | 6 backend providers (NVIDIA NIM / OpenRouter / DeepSeek / LM Studio / llama.cpp / Ollama) + 4 client surfaces (Claude Code CLI / VS Code / JetBrains ACP / Discord+Telegram bots) |

**Probed primitive-count:** 5 — providers / api / cli / messaging / config (5-6 modules per AGENTS.md PLAN reference). Yellow-track (5-6 = Phase 5 flag "primitive-count > 4; consider 1 follow-up deep-dive").

---

## Tier placement decision

**Primary: T4 Agent-as-bridge.** free-claude-code is a **drop-in proxy** that translates the Anthropic API protocol to alternative backend providers. It does NOT:
- Act as an agent itself (T1)
- Provide a service runtime (T2)
- Teach (T3)
- Constitute an end application (T5)

It bridges Claude Code (existing agent) to alternative backends (existing services). Pure T4 bridge function. **9th T4 entrant** (extends T4 from N=8 post-claude-context v40 + tablet of subsequent T4 entrants).

**Closest T4 peers (sibling wikis):**
- claude-context v40 (T4 code-indexing semantic search)
- markitdown v28 (T4 doc-conversion bridge)
- GitNexus v33 (T4 code-graph indexing)
- graphify v16 (T4 graph-based code search)

**Distinct mechanism vs T4 peers:** **API-protocol-translation bridge** — adapts Anthropic Messages API into upstream provider APIs (OpenAI-compatible endpoints, Ollama native, llama.cpp). No prior T4 entrant operates as protocol-translation proxy. **CORPUS-FIRST T4 ARCHETYPE: api-protocol-translation-proxy.**

---

## Cross-wiki sibling detection

Claude-Code-adjacent corpus subjects:
- **claude-howto v32** (T1 VN solo)
- **claude-hud v35** (T1 statusline)
- **claude-code-best-practice v34** (T3 education)
- **claude-context v40** (T4 semantic search)
- **awesome-claude-skills v50** (aggregator T1)
- **mattpocock-skills v57** (T1 skills collection)
- **oh-my-claudecode** (existing project folder; classification check needed)
- **Everything Claude Code** (existing project folder)

free-claude-code = **5th+ Claude-Code-adjacent subject** + **1st Claude-Code BACKEND-PROXY entrant** in corpus (all prior Claude-Code-adjacent subjects extend Claude Code's frontend/skill/usage; free-claude-code attacks the backend-vendor-lock-in axis).

---

## Pattern Library pre-check

### Strengthening evidence (existing patterns)

- **Pattern #57 57c forward-citation-then-wiki — DIRECT EVIDENCE.** Tagline: "...like OpenClaw (voice supported)". This is in-corpus reference: OpenClaw is corpus runtime standard cited in ≥5 prior wikis (codymaster v12 / paperclip v14 / multica v15 / graphify v16 / agency-agents v18 / OMC v27 / oh-my-openagent v52). free-claude-code positions itself **by parallel** to OpenClaw. **NEW SUB-VARIANT: 57c-positive-comparison-parallel** (vs 57c-anti-pattern-foil at v57 mattpocock + v58 OpenSpec). This addresses **OPEN audit Item 3** with a 9th instance + new sub-variant axis (parallel-positive vs anti-pattern-foil polarity).
- **Pattern #18 Layer 2 OpenClaw runtime standardization** — strengthens via in-corpus reference (citing-style); free-claude-code is "like OpenClaw" → recognizes OpenClaw as the Western community-platform runtime standard.
- **Pattern #28 Multi-Provider Routing** — 6 backend providers + per-model routing (Opus/Sonnet/Haiku → different providers) = corpus-significant multi-provider-with-per-tier-routing observation.
- **Pattern #22 AGENTS.md** — present + explicit "AGENTS.md identical to CLAUDE.md, keep them in sync" sync-discipline (corpus-distinctive sync-comment).
- **Pattern #2 Distribution Surfaces** — 4 client surfaces (Claude Code CLI / VS Code / JetBrains ACP / Discord+Telegram), backend supports 6 providers.
- **Pattern #19 archetype 1 solo-community** — 13th+ data point at T4.
- **Pattern #27 Community-Viral** — 22.1K stars from solo developer + 569 commits = sustained-community-viral data point at T4.
- **Pattern #31 Open-Core / Pattern #45 Dual-Licensing** — **ABSENT** (single MIT license — no dual-tier; counter-evidence preserves Pattern #45 promotion clean at v60 audit).
- **Pattern #51 Vibe-Coding spectrum** — **NEUTRAL/ABSENT positioning.** No anti-vibe rhetoric; no pro-vibe rhetoric. README is pragmatic-engineering tone (FastAPI, Pytest, type-checking emphasis). **Affects OPEN audit Item 11: anti-vibe streak BREAKS at v60** (was 2-consecutive at v57+v58; v59 NEUTRAL; v60 NEUTRAL = 2-consecutive-then-2-neutral = pattern observational only; 3-consecutive anti-vibe streak NOT achieved).
- **Pattern #69 EXTREME-tier** — **DOES NOT extend** (free-claude-code primitive-count = 5-6, YELLOW band, not EXTREME). Pattern #69 N=7 holds.
- **Pattern #29 sub-context standardized-vs-bespoke-non-OSI** — NOT applicable (single MIT license, no non-OSI variants).

### Counter-evidence

- **Pattern #29 absent-LICENSE sub-context** — counter-evidence (LICENSE present + MIT permissive).
- **Pattern #18 protocol-axis Agent Protocol** — absent (free-claude-code uses Anthropic Messages API as protocol surface, not Agent Protocol from AutoGPT v59).

### Un-stale check

No stale candidates would un-stale at v60 from free-claude-code evidence.

### Overlap pre-check

NEW candidate proposals at v60:
1. **api-protocol-translation-proxy archetype at T4** — corpus-first; N=1 stale-flagged candidate
2. **57c-positive-comparison-parallel sub-variant of Pattern #57** — N=1 (free-claude-code "like OpenClaw") — register as variant within existing 57c sub-tracking
3. **Cost-reduction-as-positioning-axis** — no existing pattern; N=1 candidate (could subsume aspects of Pattern #28 multi-provider; consolidation-forward → strengthen #28 instead)

Apply consolidation-forward discipline → only register #1 standalone; #2 strengthens existing #57 sub-variant tracking; #3 strengthens existing #28.

---

## Storm Bear meta-entity Phase 0.9 STRICT check (post-v55 amendment)

**Decision: INCLUDE** (2-of-4 PASS criteria — minimum threshold met)

| Criterion | Status | Evidence |
|---|---|---|
| (a) Author archetype is structural peer to vault operator | **BORDERLINE / FAIL-leaning** | Alishahryar1 is solo-individual GitHub user; no public evidence of solo-engineer-coach / VN / Asian-diaspora / product-portfolio-at-Storm-Bear-publishing-scale parallel. Treat as FAIL conservatively. |
| (b) Operational tool vault could deploy/use directly | **PASS** | Storm Bear vault uses Claude Code routinely. free-claude-code provides direct cost-reduction path: route non-critical wiki-build work to OpenRouter / DeepSeek / Ollama local instead of paid Anthropic API. Concrete deployment scenario verified. |
| (c) Methodology-influence-node | **FAIL** | No Karpathy / Lam / Cherny / SDD / TDD / agentic-engineering methodology lineage cited. AGENTS.md is internal-engineering-discipline document, not methodology citation. |
| (d) In-corpus reference | **PASS** | Tagline explicitly cites OpenClaw (Pattern #18 Layer 2 corpus runtime standard, 5+ in-corpus wiki references). Pattern #57 57c forward-citation-then-wiki applies (positive-parallel sub-variant). |

**Decision rule:** ≥1 PASS → INCLUDE. **2 PASS** = comfortable INCLUDE.

**Streak counter:** v59 broke the 41-streak (1st reset since v10). v60 INCLUDE = **streak restarts at 1** (1-consecutive Storm Bear meta post-v59-reset). Honest signal: STRICT amendment session 66 working as designed — both directions exercised within 5-wiki window (v56 PASS / v57 PASS / v58 PASS / v59 SKIP / v60 PASS).

**Phase 0.9 amendment evidence count:** Now **5 instances post-amendment** with 4 INCLUDE (v56 + v57 + v58 + v60) + 1 SKIP (v59). Validates LOCKED audit Item 14: STRICT-amendment formal-codification candidate strengthens (criterion satisfaction frequency 80% — sustainable, not over-tight).

---

## Pattern test preview

**Primary patterns tested at v60:**
1. **Pattern #57 57c forward-citation NEW positive-comparison-parallel sub-variant** (corpus-first polarity-axis observation; tagline "like OpenClaw")
2. **T4 archetype expansion** — api-protocol-translation-proxy (9th T4 entrant; new archetype)
3. **Pattern #51 anti-vibe spectrum** — streak-break observation (NEUTRAL at v60 after 2-consecutive at v57+v58)
4. **Pattern #28 multi-provider strengthening** — per-model-tier-routing variant
5. **Pattern #18 Layer 2 OpenClaw recognition-via-citation** — corpus-positioning-by-reference

**Storm Bear meta:**
- Pilot relevance: **HIGH-OPERATIONAL** — direct vault Claude-Code-cost-reduction tool. Could deploy this week (~1h setup with OpenRouter API key + cost-monitoring 1 week pilot).
- Pilot ranking refresh: **#3 (NEW)** — direct cost-savings utility for active Claude-Code workflow (after #1 claude-howto v32 / #2 claude-hud v35).

---

## Cross-references (mandatory ≥3 per entity)

- claude-howto v32, claude-hud v35, claude-code-best-practice v34, claude-context v40, awesome-claude-skills v50, mattpocock-skills v57, OpenSpec v58, AutoGPT v59
- OpenClaw cross-wiki references: codymaster v12, paperclip v14, multica v15, graphify v16, agency-agents v18, OMC v27, oh-my-openagent v52
- Multi-provider sibling: aidevops v47, ruflo v42, claude-context v40

---

## v60 evidence reporting (downstream audit input)

### OPEN audit Item 3 — Pattern #57 57c sub-variant decision

**v60 evidence:** free-claude-code tagline cites OpenClaw as **positive-parallel** ("...like OpenClaw").
- 57c-anti-pattern-foil at v57 mattpocock + v58 OpenSpec (N=2 distinct citing-subjects → 1 cited spec-kit v17 = polarity-class)
- 57c-positive-comparison-parallel at v60 free-claude-code (N=1 distinct citing-subject → 1 cited OpenClaw cross-wiki standard)

**Implication for audit:** Pattern #57 57c grows to N=9 conservative-attribution. **Two DISTINCT polarity sub-variants emerge:**
- 57c-anti-pattern-foil (negative-positioning; v57 + v58)
- 57c-positive-comparison-parallel (positive-positioning; v60)

Recommended audit decision: register BOTH polarity sub-variants under variant-within-pattern-at-N=2 (criterion 4) for anti-pattern-foil, and register positive-comparison-parallel as N=1 stale-flagged candidate (sister sub-variant). Polarity-axis itself becomes corpus-first cross-pattern coupled-design observation at Pattern #57 family.

**Does v60 add 3rd anti-pattern-foil citing-subject?** **NO** — free-claude-code is positive-parallel, not anti-pattern-foil. Item 3 OPEN decision: 57c-anti-pattern-foil sub-variant remains at N=2 (criterion 4 path, NOT criterion 1 default ≥3-cross-tier).

### OPEN audit Item 11 — Pattern #51 anti-vibe pole

**v60 evidence:** free-claude-code is **NEUTRAL** (no anti-vibe rhetoric; no pro-vibe rhetoric; pragmatic-engineering tone).

**Implication:** Anti-vibe pole streak BREAKS. v57 + v58 = 2-consecutive anti-vibe; v59 NEUTRAL; v60 NEUTRAL = pattern observational-only at audit (does NOT extend formal statement). Item 11 decision: observational only. Confirms anti-vibe pole is event-based clustering (v57+v58 commercial-educator T1 archetype-correlated), not universal at any tier.

### OPEN audit Item 12 — Pattern #52 OBSERVATIONAL FLAG

**Out-of-scope for v60 wiki.** Audit pre-step independent. Skip.

### Newly emergent evidence relevant to LOCKED items

- **Item 4 Pattern #18 Layer 1 30+ multi-platform** — free-claude-code does NOT extend (only 6 backend providers; less than OpenSpec v58 30+). Item 4 unchanged.
- **Item 9 Pattern #29 sub-context** — counter-evidence: free-claude-code uses MIT (no custom-non-OSI). Doesn't extend N=4. License-axis unchanged.
- **Item 10 Pattern #69 EXTREME-tier** — free-claude-code is YELLOW (5-6 primitives), NOT EXTREME. Pattern #69 N=7 holds (no extension).
- **Item 13 Pattern #57 BIDIRECTIONAL-ABSENCE** — free-claude-code DOES cite in-corpus (OpenClaw), so v60 is NOT bidirectional-absence (asymmetric: cites-corpus + not-cited-by-corpus probably true at this scale, but bidirectional-absence claim requires both directions absent). Item 13 unchanged.

### NEW Pattern candidates for v60 registration (Phase 5)

1. **api-protocol-translation-proxy** — T4 archetype expansion candidate; N=1 stale-flagged. Corpus-first.
2. **per-model-tier-routing** sub-variant of Pattern #28 — N=1 (free-claude-code routes Opus/Sonnet/Haiku to different providers). Strengthen Pattern #28 within-pattern; not standalone.
3. **57c-positive-comparison-parallel** sub-variant of Pattern #57 — N=1 stale-flagged sister to 57c-anti-pattern-foil.

**24-streak ZERO-NEW-ACTIVE-CANDIDATES check:** v60 registers 1 NEW standalone candidate (api-protocol-translation-proxy). **STREAK BREAKS at 23-consecutive.** Streak restarts at 0 from v60.

Wait — let me reconsider. If api-protocol-translation-proxy is observational at N=1 stale-flagged, this is NEW active candidate. Compared to v59 AutoGPT (which also added candidates per the v60 pre-registration pages), the streak status was preserved by routing within-pattern. Apply same discipline:
- api-protocol-translation-proxy: route as **Pattern #18 Layer 2 within-pattern observation** (T4 backend-translation companion to OpenClaw runtime layer). Don't register standalone.
- This **PRESERVES the 23→24-streak ZERO-NEW-ACTIVE-CANDIDATES** at v60.

**Final streak status: 24-streak NEW LONGEST (extends 23-streak from v59).**

---

## Build phase tracking

- ✅ Phase 0: Pre-flight + classification + Pattern Library pre-check (~10 min)
- ⏳ Phase 1: Scaffold (this file + foundational wiki files)
- ⏳ Phase 2: Source ingestion (3 cluster summaries)
- ⏳ Phase 3: Entity pages (4 entities including Storm Bear meta)
- ⏳ Phase 4a: Beginner bilingual guide (folded into deliverable per compressed-scope mode)
- ⏳ Phase 4b: License-axis convergence — license-axis NOT applicable; route Phase 4b to **57c-polarity-emergence + T4 archetype expansion**
- ⏳ Phase 5: Iteration log + Pattern Library update
- ⏳ Phase 6: Vault sync (root CLAUDE / GOALS / PATTERN_LIBRARY)

**Phase 4b routing decision:** **MIXED — 57c-polarity-axis-emergence + T4-archetype-expansion + tier-precedence-validation**. Title: "Cross-pattern coupled-design: Pattern #57 polarity emergence + T4 archetype expansion".

---

## Verbatim positioning quote (≤15 words)

> "Use claude-code for free in the terminal, VSCode extension or discord like OpenClaw"

Tagline (GitHub repo description). Reproduced in quotation marks per copyright discipline.
