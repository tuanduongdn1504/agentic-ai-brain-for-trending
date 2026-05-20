# (C) NEW T5 sub-archetype "Hybrid-RPA-with-LLM-augmented-decision-making" — N=1 registration proposal

**Proposal-document discipline** (per routine v2.2 §"NEW Pattern candidate proposal-document"):

- **Status**: PROVISIONAL REGISTRATION at v80 ship (2026-05-20)
- **Confidence**: HIGH for registration; LOW for any promotion discussion at v85+ until N=2 evidence
- **Evidence depth**: N=1 (this proposal documents v80 thu-vu92→TroniePh/SmartMacroAI as the single subject)
- **Sub-archetype taxonomy**: 80a — NEW sub-archetype within already-existing T5 Application tier
- **Top-level T5 status**: UNCHANGED
- **First-cycle stale-check**: v85 (5-wiki rule)
- **Retire-check**: v90 (10-wiki rule)

## 1. Current status of T5 Application tier (pre-v80)

**T5 Application tier** = "Agent-as-application" — corpus subjects where the framework IS the end-user application, distinct from:
- T1 (assistant skills consumed by harness)
- T2 (services for agents)
- T3 (educational artifacts)
- T4 (bridges / connectors)

**Existing T5 entrants** (per corpus history):
- v9 autoresearch (Karpathy) — agentic-research-framework with LLM-as-orchestration-brain
- v79 autoresearch_folktales (Thu Vu) — Apple Silicon MPS port of v9; inherits LLM-as-orchestration-brain
- (Various earlier T5 entrants per `_state/03b` + `_state/04` + `_state/05`)

**Pre-v80 observation**: T5 entrants in v60+ window all use LLM at the orchestration layer (LLM drives the framework loop).

## 2. NEW sub-archetype 80a — definition

**80a "Hybrid-RPA-with-LLM-augmented-decision-making"** PROVISIONAL N=1 registration.

### Definition

A T5 Application where rule-based RPA / automation logic forms the framework spine, and LLM API calls are integrated as **ONE OF MULTIPLE tool-mode options** at the decision-making layer — NOT as orchestration brain.

### Required criteria for 80a classification

1. **Tier T5** (end-user application)
2. **Multiple input/automation modes available** — LLM is one of N tool modes
3. **LLM API integration is OPTIONAL** — framework runs without LLM
4. **LLM is called at decision-layer** (interpretation / classification / reasoning), NOT orchestration-layer
5. **LLM is REMOTE service** (OpenAI / Anthropic / Gemini / etc.); not local-LLM
6. **The fundamental architecture is rule-based**, not LLM-driven

### Architectural inversion

| Typical T5 (LLM-as-orchestration-brain) | NEW 80a (LLM-as-tool-mode-option) |
|------------------------------------------|------------------------------------|
| LLM → tools → results → LLM (loop) | Rules → (tool A OR LLM OR tool B OR …) → result |
| LLM drives the framework | LLM is consumed by rule-based framework |
| Tools serve the LLM | Tools (including LLM) serve rule-based engine |
| Application's intelligence = LLM's reasoning | Application's intelligence = rule-based logic + optional LLM augmentation |

## 3. N=1 evidence: v80 SmartMacroAI

### Subject

**`TroniePh/SmartMacroAI`** (product) + **`TroniePh/SmartMacroAI-Website`** (marketing site).

### Architecture spine (NON-LLM rule-based)

- **4 input modes**: Stealth PostMessage + Raw Input SendInput + Hardware mouse_event + Driver Level Kernel — all rule-based Win32 calls
- **Image recognition** with confidence thresholds — rule-based OpenCV via Emgu.CV
- **Pixel color detection** — rule-based color queries
- **OCR Text Detection** — rule-based Tesseract 5.2
- **If/Else branching** — rule-based conditional logic
- **Loop control** — rule-based iteration
- **CSV auto-fill** — rule-based data feeding
- **Multi-dashboard / scheduling / recording / undo-redo** — rule-based productivity features

### LLM integration (optional decision-layer tool)

**Verbatim from README**: *"AI Integration — OpenAI & Gemini for smart decision-making"*

- OpenAI API calls (remote)
- Gemini API calls (remote)
- User provides own API keys
- Called at decision-layer (e.g., "is this screen showing X?" when rule-based image-conditions can't determine)
- Optional — most macros run entirely without LLM

### Per-criterion evaluation (sub-archetype 80a criteria)

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Tier T5 | ✅ PASS | End-user Windows desktop application |
| 2 | Multiple input/automation modes | ✅ PASS | 4 input modes (Stealth + Raw + Hardware + Driver Level) + image-rec + OCR + pixel + LLM = 7+ tool-modes |
| 3 | LLM integration OPTIONAL | ✅ PASS | Framework runs without LLM (rule-based by default) |
| 4 | LLM at decision-layer not orchestration | ✅ PASS | LLM called for interpretation/classification, not framework loop control |
| 5 | LLM is REMOTE service | ✅ PASS | OpenAI + Gemini = remote APIs (user provides keys) |
| 6 | Fundamental architecture rule-based | ✅ PASS | WPF UI + Win32 API + .NET 8 form the spine |

→ All 6 sub-archetype criteria PASS at N=1.

## 4. Structural diversity table

| Dimension | v9 autoresearch | v79 autoresearch_folktales | **v80 SmartMacroAI (PROPOSED 80a)** |
|-----------|-----------------|----------------------------|-------------------------------------|
| Tier | T5 | T5 | T5 |
| LLM role | Orchestration brain | Orchestration brain (inherits) | **Tool-mode option** |
| Domain | LLM research | LLM research | Windows RPA |
| OS target | Linux+GPU | Apple Silicon MPS | Windows x64 |
| End-user audience | ML researchers | LLM experimenters | RPA practitioners / gamers / power-users |
| Sub-archetype proposed | (existing) | (inherits v9) | **NEW 80a** |

## 5. Promotion criteria evaluation (5 + 1 dimension routine v2.2)

| # | Criterion | Status at N=1 |
|---|-----------|---------------|
| 1 | Default: ≥3 observations across 2+ tiers | FAIL at N=1; need N≥3 |
| 2 | Structural-unambiguity-at-N=2 | FAIL at N=1; need N=2 |
| 3 | Spectrum-pattern-at-N=2 | N/A — sub-archetype not spectrum |
| 4 | Variant-within-pattern-at-N=2 | APPLICABLE (80a is sub-archetype within T5); PROMOTION-ELIGIBLE at N=2 |
| 5 | Meta-pattern-at-N=3-consolidation | N/A |
| NEW v2.2 | Cross-archetype N-counting | N/A at N=1 |

**Recommended verdict**: REGISTER as PROVISIONAL N=1 sub-archetype within T5. Re-evaluate at N=2.

**Expected promotion trigger**: when another corpus subject emerges with similar:
- T5 tier
- Multiple non-LLM tool modes
- Optional remote-LLM-API integration at decision-layer
- Fundamentally rule-based architecture

**Potential N=2 future subjects**:
- AI-augmented n8n / Make.com / Zapier-style workflow tools
- Vision-language-model integrated RPA at non-LLM-orchestration scale
- Robot Framework / Selenium IDE / TestComplete with LLM-fallback for flaky tests

## 6. Distinguishing from outside-scope classification

**Could be outside-scope** if:
- LLM integration is superficial (marketing-only without actual API calls)
- Framework is 100% rule-based with no LLM consumption
- Domain unrelated to corpus (gardening / retail POS / etc.)

**v80 is NOT outside-scope** because:
- LLM integration is real and verifiable (README explicit; OpenAI + Gemini named)
- Architecture provides novel insight (LLM-inversion)
- Domain is automation-relevant (RPA + Playwright + browser automation)

→ **Decision: in-scope as NEW T5 sub-archetype 80a, not outside-scope**.

## 7. Sub-archetype-vs-NEW-tier consideration

Alternative considered: register as NEW T6 tier "Application-with-AI-augmented-decision-making".

**REJECTED** because:
- v80 fits cleanly under existing T5 (Application) tier
- LLM-inversion-architecture is sub-archetype dimension, not tier dimension
- Tier-Taxonomy Review T6 already pending v80 audit per CLAUDE.md state — adding new T6 candidate would conflict

→ **Cleaner: register as T5 sub-archetype 80a**.

## 8. T5 sub-archetype taxonomy expansion proposal

**Pre-v80 (implicit)**:
- T5.a Orchestration-brain (v9, v79)
- T5.b Harness-consumer (corpus convention; ECC v1+v78, v66, v68)
- T5.c Application-itself (chat UIs)

**Post-v80 (proposed registration)**:
- T5.a Orchestration-brain
- T5.b Harness-consumer
- T5.c Application-itself
- **T5.80a Tool-mode-option (NEW)** ← v80 SmartMacroAI

→ 3-sub-class → 4-sub-class T5 taxonomy.

## 9. Cross-references to evidence documents

- **Cluster 1** § 5 "AI/ML/LLM mentions on website" (downplayed)
- **Cluster 2** § 5 "Core capabilities" (verbatim "AI Integration — OpenAI & Gemini for smart decision-making")
- **Cluster 2** § 6 "AI integration analysis" (architectural distinction)
- **Cluster 3** § 6 "Tech stack supply chain analysis"
- **Entity 1** § 4 "AI integration architecture" (LLM-inversion)
- **Entity 3** § 2 "NEW sub-archetype 80a definition" (most-detailed)
- **Entity 4** § 9 "Library-vocabulary candidates" (LLM-Inversion-Architecture)

## 10. Audit checklist for v85+ audit

- [ ] Verify 80a N=1 evidence package is complete (this proposal + Entity 3 + Cluster 2 § 5-6 + Cluster 3 § 6)
- [ ] Stale-check schedule at v85 (5-wiki rule)
- [ ] Retire-check schedule at v90 (10-wiki rule)
- [ ] N+1 acceleration scan v81-v84 for similar Hybrid-RPA-with-LLM-as-tool-mode subjects
- [ ] T5 sub-archetype taxonomy update at v85 audit — 3-sub-class → 4-sub-class formalization (if 80a sustains)
- [ ] Library-vocabulary candidate "LLM-Inversion-Architecture" first-cycle stale-check
- [ ] Pattern #19 NEW sub-mechanism 19k first-cycle stale-check
- [ ] Pattern #29 NEW sub-mechanism "404-confirmed-absent-LICENSE" first-cycle stale-check
- [ ] Library-vocabulary candidate "Deliberately-Narrow Distribution Profile" N=2 filing decision (v79 + v80)
- [ ] Library-vocabulary candidate "Localization-Depth-vs-Locale-Breadth Distinction" N=2 filing decision (v77 + v80)

## 11. Pre-Phase-6 fact-verification

**Cross-checked against existing Pattern Library state**:
- T5 Application tier: exists in PATTERN_LIBRARY.md / `_patterns/` chapter files
- Existing T5 entrants: v9 autoresearch + various older entries
- No prior T5 sub-archetype taxonomy formalization observed (4-sub-class taxonomy would be new at v85)
- Tier-Taxonomy Review T6 already scheduled v80 audit per CLAUDE.md state (separate item; T6 is potential NEW TIER 6 question, not T5 sub-archetype question)

**No retroactive corrections triggered**.

## 12. Recommended verdict

**REGISTER 80a sub-archetype as PROVISIONAL N=1 candidate within T5 Application tier.**

- Confidence in registration: **HIGH**
- Confidence in promotion discussion at v85+: **LOW** until N=2 evidence
- Top-level T5 status: UNCHANGED
- Sub-archetype taxonomy expansion: 3-sub-class → 4-sub-class (proposed; pending v85 formalization)

**Pattern Library counts unchanged at v80**: 45 confirmed / 29 active / 0.644 ratio (T5 sub-archetype registration is administrative within already-CONFIRMED T5 tier).

## 13. Filing instructions for Phase 6 vault sync

**Where this proposal lives**: `01 Analysis/(C) T5-NEW-sub-archetype-Hybrid-RPA-with-LLM-augmented-decision-making-N1-registration.md`

**Where to register at Pattern Library**:
- Add 80a entry to `_patterns/03-active-candidates.md` (Active Candidates section)
- Update `_patterns/05-recent-additions.md` § "v80 strengthening block" with PRIMARY narrative
- Update PATTERN_LIBRARY.md root shim if T5 sub-archetype taxonomy is referenced
- Update stale-tracking table with v85 stale-check + v90 retire-check entries

**No top-level state transitions to apply** — Pattern Library counts unchanged.
