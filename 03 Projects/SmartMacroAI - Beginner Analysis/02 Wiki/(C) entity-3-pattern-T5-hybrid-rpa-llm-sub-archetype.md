# (C) Entity 3 — Phase 4b PRIMARY: NEW T5 sub-archetype "Hybrid-RPA-with-LLM-augmented-decision-making"

**Phase 4b PRIMARY entity** (pre-registered Phase 0; structures around Pattern Library PRIMARY deliverable).

**Pre-registration**: `v80 SmartMacroAI: Phase 0 pre-registered NEW T5 sub-archetype candidate "Hybrid-RPA-with-LLM-augmented-decision-making" PROVISIONAL N=1 as Phase 4b PRIMARY`.

## 13-section canonical format

### 1. Background: T5 Application tier state (pre-v80)

**T5 Application tier** ("Agent-as-application") — corpus subjects where the framework IS the application end-users interact with directly, vs T1 (assistant skills consumed by harness) / T2 (services for agents) / T3 (educational artifacts) / T4 (bridges).

**Current T5 entrants (per CLAUDE.md state)**:
- v9 autoresearch (Karpathy original) — LLM-as-orchestration-brain
- v79 autoresearch_folktales (Thu Vu, Apple Silicon MPS port) — LLM-as-orchestration-brain (inherits)
- (Various T5 entrants from older v-range)

**Pattern**: pre-v80 T5 entrants all use LLM at orchestration layer.

### 2. NEW sub-archetype 80a — definition

**80a "Hybrid-RPA-with-LLM-augmented-decision-making"** PROVISIONAL N=1 registration.

**Definition**: A T5 Application where rule-based RPA / automation logic forms the framework spine, and LLM API calls are integrated as ONE OF MULTIPLE tool-mode options at the decision-making layer — NOT as orchestration brain.

**Required criteria for 80a classification**:
1. Tier T5 (end-user application)
2. Multiple input/automation modes available (LLM is one of N)
3. LLM API integration is OPTIONAL (framework runs without LLM)
4. LLM is called at decision-layer (interpretation / classification / reasoning), NOT orchestration-layer
5. LLM is REMOTE service (OpenAI / Anthropic / Gemini / etc.); not local-LLM
6. The fundamental architecture is rule-based, not LLM-driven

**v80 evidence (single subject)**:
- 4 input modes (Stealth + Raw Input + Hardware + Driver Level Kernel) — all non-LLM
- "AI Integration — OpenAI & Gemini for smart decision-making" — LLM as one of many tools
- Macros can run entirely without LLM (rule-based mode)
- LLM is at decision-layer (image-condition fallback / OCR-result interpretation)
- OpenAI + Gemini = remote APIs (user provides keys)
- Framework spine: WPF UI + Win32 API + 4-input-mode + computer vision + OCR — fundamentally rule-based

→ All 6 sub-archetype criteria PASS at N=1.

### 3. Distinction from existing T5 sub-classes

| Sub-class | LLM role | Examples | Architecture |
|-----------|---------|----------|--------------|
| LLM-as-orchestration-brain | LLM drives loop | v9 + v79 | LLM → tools → results → LLM |
| LLM-as-harness-consumer | LLM uses skills/tools | ECC v1+v78 + v66 + v68 | Harness → LLM → tools |
| LLM-as-application-itself | LLM IS the UI | (chat-like applications) | User ↔ LLM |
| **80a LLM-as-tool-mode-option (NEW v80)** | **LLM is one of multiple tools** | **v80 SmartMacroAI** | **Rules → (tool A or LLM or tool B or...) → result** |

**Architectural inversion**: typical T5 entrants put LLM at the TOP of the call hierarchy (orchestration); v80 puts LLM at the BOTTOM (as a callable tool). This is corpus-first.

### 4. Promotion criteria evaluation (5 + 1 dimension routine v2.2)

| # | Criterion | Status at N=1 |
|---|-----------|---------------|
| 1 | Default: ≥3 observations across 2+ tiers | FAIL at N=1; need N≥3 |
| 2 | Structural-unambiguity-at-N=2 | FAIL at N=1; need N=2 |
| 3 | Spectrum-pattern-at-N=2 | N/A — sub-archetype not spectrum |
| 4 | Variant-within-pattern-at-N=2 | APPLICABLE (80a is sub-archetype within T5); PROMOTION-ELIGIBLE at N=2 |
| 5 | Meta-pattern-at-N=3-consolidation | N/A |
| NEW v2.2 | Cross-archetype N-counting | N/A at N=1 |

**Recommended verdict**: REGISTER as PROVISIONAL N=1 sub-archetype within T5. Re-evaluate at N=2.

**Stale-check at v85 + retire-check at v90.**

### 5. Distinguishing from outside-scope classification

**Could be classified as outside-scope** if:
- LLM integration were superficial (e.g., README mentions "AI" but no actual API integration)
- Framework were 100% rule-based with no LLM consumption
- Domain were unrelated to corpus (e.g., gardening app, retail POS)

**v80 is NOT outside-scope** because:
- LLM integration is real (OpenAI + Gemini APIs called at decision-layer)
- Framework provides genuine architectural-novelty (LLM-inversion)
- Domain is automation-relevant to corpus (RPA + browser-automation + computer-vision)

→ **Decision: in-scope as NEW T5 sub-archetype, not outside-scope**.

### 6. Sub-archetype-vs-NEW-tier consideration

Alternative classification considered: register as NEW T6 tier "Application-with-AI-augmented-decision-making".

REJECTED because:
- v80 fits cleanly under existing T5 (Application) tier
- LLM-inversion-architecture is the sub-archetype dimension, not new tier
- Tier-Taxonomy Review T6 already pending v80 audit per CLAUDE.md state — adding a new T6 candidate would conflict with that scheduled review

→ **Cleaner: register as T5 sub-archetype 80a, not NEW T6 tier**.

### 7. 2-wiki sustained "narrow-distribution" Library-vocabulary candidate strengthening

**v79 autoresearch_folktales contributed** Library-vocabulary candidate "Deliberately-Narrow Distribution Profile in v60+ window" at PROVISIONAL N=1.

**v80 SmartMacroAI strengthens** at N=2:
- v79: uv-exclusive + Apple-Silicon-only + 2-explicit-agent-platforms narrow
- v80: GitHub-Releases-only + Windows-only + dual-repo separation narrow

Both narrow on DIFFERENT axes (substrate / packaging / harness count) but share the meta-pattern of NARROWNESS as deliberate design choice.

→ 2-wiki sustained at PROVISIONAL N=2 — Library-vocabulary item filing decision at v85 audit.

### 8. 2-wiki sustained "Localization-Depth-vs-Locale-Breadth" candidate strengthening

**v77 easy-vibe** contributed locale BREADTH (13 locales).

**v80 SmartMacroAI** contributes locale DEPTH (2 locales × 830+ keys = 1,660+ translations).

→ N=2 sustained at sub-distinction level — Library-vocabulary item filing decision at v85 audit.

### 9. Audit checklist for v85+ audit

- [ ] Verify 80a N=1 evidence package is complete (this entity + Cluster 2 §6 + Cluster 3 §6)
- [ ] Stale-check schedule at v85 (5-wiki rule)
- [ ] Retire-check schedule at v90 (10-wiki rule)
- [ ] N+1 acceleration scan v81-v84 for similar LLM-as-tool-mode-option architectures
- [ ] T5 sub-archetype taxonomy update — 4-sub-class taxonomy: orchestration-brain / harness-consumer / application-itself / **tool-mode-option (NEW)**
- [ ] Library-vocabulary candidates filing decisions (Narrow-Distribution-Profile + Localization-Depth-vs-Locale-Breadth at N=2)
- [ ] Pattern #29 absent-LICENSE NEW sub-mechanism "404-confirmed-absent-LICENSE" first-cycle stale-check
- [ ] Pattern #19 NEW sub-mechanism 19k first-cycle stale-check

### 10. Pre-Phase-6 fact-verification

**Cross-checked against existing Pattern Library state**:
- T5 Application tier exists in PATTERN_LIBRARY.md / `_patterns/` chapter files
- Existing T5 entrants: v9 autoresearch + various older entries
- No prior T5 sub-archetype taxonomy formalization observed (would-be 4-sub-class taxonomy is new at v80)
- Tier-Taxonomy Review T6 already scheduled v80 audit per CLAUDE.md state (separate item; T6 is potential NEW TIER 6 question, not T5 sub-archetype question)

**No retroactive corrections triggered**.

### 11. Cross-references to evidence documents

- **Cluster 1** § 5 "AI/ML/LLM mentions" (downplayed on website)
- **Cluster 2** § 5 "Core capabilities" (verbatim "AI Integration — OpenAI & Gemini for smart decision-making")
- **Cluster 2** § 6 "AI integration analysis" (full architectural distinction)
- **Cluster 3** § 6 "Tech stack supply chain analysis" (hybrid local + remote)
- **Entity 1** § 4 "AI integration architecture" (LLM-inversion-architecture)
- **Entity 2** § 6 "Tech stack supply chain"

### 12. Recommended verdict

**REGISTER 80a sub-archetype as PROVISIONAL N=1 candidate within T5 Application tier.**

**Confidence**: HIGH for the registration itself (clean evidence chain; all 6 sub-archetype criteria PASS; structural distinctness from existing T5 sub-classes confirmed).

**Confidence**: LOW for any promotion-related discussion at v85+ until N=2 evidence emerges.

**Top-level T5 tier status**: UNCHANGED.

**Sub-archetype taxonomy expansion**: 3-sub-class → 4-sub-class (orchestration-brain / harness-consumer / application-itself / **tool-mode-option**).

### 13. Filing instructions for Phase 6 vault sync

**Where this proposal lives**: `01 Analysis/(C) T5-NEW-sub-archetype-Hybrid-RPA-with-LLM-augmented-decision-making-N1-registration.md`

**Where to register at Pattern Library**:
- Add 80a entry to `_patterns/03-active-candidates.md` (Active Candidates section)
- Update `_patterns/05-recent-additions.md` § "v80 strengthening block" with PRIMARY narrative
- Update PATTERN_LIBRARY.md root shim if T5 sub-archetype taxonomy is referenced
- Update stale-tracking table with v85 stale-check + v90 retire-check entries

**No top-level state transitions to apply** — Pattern Library counts unchanged (45 confirmed / 29 active / 0.644 ratio); T5 tier already exists.
