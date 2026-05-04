# (C) v20 fish-speech — build learnings + 2nd v2 routine evaluation

> **Date:** 2026-04-19
> **Wiki:** fish-speech (20th LLM Wiki in corpus; **2nd outside-scope** after build-your-own-x v8)
> **Routine:** `llm-wiki-routine-v2.md` (2nd v2 execution)
> **Duration:** ~2h (velocity plateau 15 consecutive v6-v20)
> **Parent:** [[(C) index]]

---

## 1. Milestones hit at v20

### Corpus-level milestones

- ✅ **2nd outside-scope wiki** (after build-your-own-x v8, 12 wikis ago)
- ✅ **2nd v2 routine execution** — validates v2 generalizes beyond v19 T4 extension mode
- ✅ **Pattern #19 4TH ARCHETYPE formalized** (research-paper-chain)
- ✅ **Pattern #29 refined** to license-category-diversity
- ✅ **Pattern #18 strengthened** — CN-ecosystem N=2 (fish-speech + TrendRadar)
- ✅ **Pattern #8 5th data point** — most rigorous (arXiv + WER + win-rate)
- ✅ **5 new pattern candidates** (#31-35)
- ✅ **Velocity plateau 15 consecutive wikis** (~2h v6-v20)
- ✅ **Storm Bear meta-entity pattern** — 11th consecutive wiki

### fish-speech-specific corpus-firsts (15 total)

- First **non-OSI license** in corpus (Fish Audio Research License)
- First **anti-distillation clause** (prohibit training foundation models from outputs)
- First **attribution-display clause** ("Built with Fish Audio" required)
- First **litigation-termination clause** (anti-patent-troll)
- First **research-paper-chain lineage** (7 prior research citations)
- First **7-language README** (largest i18n in corpus)
- First **foundation-model-as-product** in corpus
- First **open-core commercial entity** (39 AI, INC. revealed)
- First **SGLang production inference** explicit
- First **TTS benchmark family** (Seed-TTS Eval + EmergentTTS-Eval)
- First **10M-hours training corpus** explicit
- First **natural-language emotion tags** (15,000+ inline)
- First **GRPO RL alignment for generation**
- First **80+ language support** (single framework)
- First **2-arXiv-publication pattern** (2024 + 2026 tech reports)

## 2. Phase breakdown (~2h total)

| Phase | Duration | Notes |
|-------|----------|-------|
| 0: Pre-flight API probe + **v2 12-axis classification** | ~15 min | Used v2 enhanced probe; detected outside-scope + custom-license + research-chain immediately |
| 1: Scaffold | ~8 min | CLAUDE.md populated with outside-scope framing + Pattern #19 4th archetype table |
| 2: Source summaries (3) | ~30 min | README/i18n + Architecture/research-lineage + LICENSE/39AI/SGLang |
| 3: Entity pages (4) | ~40 min | Standard 4 entities including Storm Bear outside-scope meta-entity |
| 4a: Beginner guide | ~15 min | Bilingual VN/EN, 13 parts, license commercial-warning prominent |
| 4b: Outside-scope meta-reference | ~30 min | Pattern #19 4th archetype formalization + 5 new candidates + Pattern #18/#29 refinements |
| 5: Iteration log + PATTERN_LIBRARY update | ~10 min | This file + direct library update (v2 protocol) |
| 6: Vault sync | ~5 min | Project files + root CLAUDE.md + GOALS.md + PATTERN_LIBRARY.md |

**Total: ~2h** — velocity plateau preserved for 2nd v2 execution.

## 3. What worked — v2 routine 2nd evaluation

### v2 features that proved useful (2nd execution)

- ✅ **12-axis Phase 0 classification** — caught outside-scope + license + research-chain at probe; saved time downstream
- ✅ **Consolidation guard** — smoothly passed (0.5:1 ratio post-v19); didn't block
- ✅ **Cross-wiki absence detection** — flagged NO OpenClaw/Hermes (consistent with TrendRadar CN-pattern), NO AGENTS.md, NO Karpathy lineage as systematic signals
- ✅ **Outside-scope Phase 4b routing** — 16-mode framework made "outside-scope meta-reference" (2nd use after v8) obvious choice
- ✅ **Pattern Library integration Phase 5** — direct update with 5 new candidates + 1 refinement
- ✅ **Storm Bear meta-entity** — 11th consecutive wiki, executed without special instruction
- ✅ **Branch fallback** — main worked, no fallback needed (consistent with v19)

### Generalization validation

v19 proved v2 on T4 extension mode. v20 proved v2 on outside-scope mode (2nd type of routing). **Two different Phase 4b modes executed successfully** = v2 routine generalizes.

### v2 vs prior state comparison

| Aspect | v1 (v1-v18) | v2 (v19-v20) | Delta |
|--------|-------------|--------------|-------|
| Phase 0 depth | 5-axis probe | 12-axis classification | **Better** — catches more |
| Outside-scope handling | Ad-hoc (v8) | Formalized routing mode | **Better** — systematic |
| Pattern Library updates | Batch at iteration log | Direct Phase 5 update | **Better** — no drift |
| Velocity | ~2h | ~2h | Same (confirmed 2nd execution) |
| Decisions captured | Ad-hoc | 16-mode Phase 4b routing | **Better** |
| 2 v2 executions | — | T4-extension + outside-scope | **Generalized** |

**v2 routine generalization validated at 2nd execution.** Velocity preserved, quality improved, pattern discovery continues.

## 4. What didn't work / friction

### Minor friction

- **License interpretation time** — Fish Audio Research License required careful reading to extract 7 distinct clauses (standard-OSI licenses are more familiar)
- **VN language quality unknown** — fish-speech claims 80+ but VN-specific quality not published; beginner guide had to note "testing required"
- **arXiv papers not deeply fetched** — 2 arXiv preprint abstracts would have enriched architecture entity; routine didn't auto-fetch
- **Origin of 39 AI, INC. opaque** — founding date, funding, headcount, geography not public; inference-only

### No recurring friction from v19

**v2 routine eliminated previous friction (consistent with v19):**
- Cross-wiki search no longer manual (absence detection automated)
- Pattern Library updates no longer deferred (direct Phase 5)
- Storm Bear meta-entity now standard
- Branch resolution didn't need fallback

## 5. Routine v2 refinement suggestions (minor, for v2.1)

### A. Research-lineage probe enhancement

**Need:** fish-speech Pattern #19 4th archetype detection required manual inference. v2 probe should auto-detect research citation patterns.

**Proposed refinement:** Phase 0 add "citation count" field → numeric value + source projects. Would help auto-classify Pattern #19 archetype.

### B. License-category classification

**Need:** fish-speech custom license required manual classification. v2 should auto-category license.

**Proposed refinement:** Phase 0 add "license category" → enum: permissive / copyleft / non-OSI-custom / public-domain / proprietary. Pattern #29 automation.

### C. Commercial-entity detection

**Need:** 39 AI, INC. revealed via LICENSE attribution, easily missed. v2 should probe for commercial-entity attribution in LICENSE/README.

**Proposed refinement:** Phase 0 check LICENSE for "Copyright © [entity]" pattern → flag as commercial-entity signal.

### D. arXiv paper auto-fetch

**Need:** fish-speech has 2 arXiv papers; v2 noted but didn't fetch. Would enrich architecture understanding.

**Proposed refinement:** Phase 2 mandate: if README cites arXiv IDs, WebFetch abstracts as Phase 2 sub-summaries.

### Backlog

4 minor v2.1 refinements proposed from v20. Not blocking — v2 works well at 2nd execution.

## 6. Pattern library updates at v20

### Direct updates to PATTERN_LIBRARY.md (v2 Phase 5 protocol)

**New candidates registered (5):**
- #31 Open-Core Commercial Entity — N=1
- #32 Research-Paper-Chain Lineage — N=1 (formalizes Pattern #19 4th archetype separately)
- #33 Non-OSI Custom License — N=1
- #34 Anti-Distillation License Clause — N=1
- #35 Foundation-Model-as-Product Scope Category — N=1

**Pattern refinements applied:**
- #18 Runtime Standards — 2nd CN-ecosystem data point confirms regional+archetypal layering
- #19 Intellectual Lineage — 4TH archetype formalized (research-paper-chain)
- #29 GPL-3.0 — refined to License-Category-Diversity (copyleft + non-OSI-custom paths)

**Pattern #8 5th data point** (not a refinement, just evidence accumulation).

### Library state post-v20

- Pre-v20: 20 confirmed + 10 candidates = 30 total
- **Post-v20: 20 confirmed + 15 candidates = 35 total**
- Candidate:confirmed = 0.75:1 (still healthy, well under 2:1)

### Next audit trigger reassessment

Pre-v20: trigger at candidate count > 10 (was hit at v19, deferred).
Post-v20: candidate count = 15. **Audit candidate strongly recommended before v21-v22.**

## 7. Meta-observations at 20-wiki milestone

### Corpus maturity

- 20 wikis across 5 tiers + outside-scope
- **Outside-scope doubled at v20** (build-your-own-x + fish-speech)
- Only T3 remains at N=1
- Pattern Library: 35 total (20 confirmed + 15 candidates)
- Routine v2 production-validated on 2 execution modes

### Pattern #19 4-archetype completion

Storm Bear corpus now documents 4 distinct intellectual-lineage archetypes. This is **structurally complete** (individual / methodology / community-viral / research-chain cover major lineage types). Future wikis likely refine or add sub-variants within these 4.

### Research-first vs product-first organizational culture

fish-speech is **first research-first framework** in corpus (others are product-first):
- 2 arXiv preprints
- Standard-eval benchmarks (Seed-TTS, EmergentTTS-Eval)
- Research lineage explicit
- Academic documentation depth

Suggests new corpus axis: research-first vs product-first orientation.

### License landscape mapping

Post-v20 corpus licenses:
- Permissive (MIT/Apache/ISC) — default agent-framework norm
- Copyleft (GPL-3.0) — community-preservation (TrendRadar)
- Public Domain (CC0) — aggregator content (build-your-own-x)
- **Custom non-OSI** — commercial-funnel (fish-speech)

4 categories = mature license landscape visible at 20 wikis.

### Pattern discovery dynamics

| Phase | Rate |
|-------|------|
| v1-v10 | 1 pattern / 2-3 wikis |
| v11-v15 | 2 patterns / wiki |
| v16-v18 | 3-4 candidates / wiki |
| v19 | 3 new candidates |
| **v20** | **5 new candidates** (highest per-wiki rate) |

**v20 highest pattern-discovery rate.** Outside-scope wikis with novel structural elements yield more patterns than incremental agent-framework wikis.

## 8. v20-specific unique findings

1. **Custom non-OSI license** at 29.8K scale — Fish Audio Research License
2. **Anti-distillation clause** — first in corpus, likely will become common
3. **Research-paper-chain lineage** — 7 citations, Pattern #19 4th archetype
4. **39 AI, INC.** — first explicit OSS-commercial-entity separation
5. **7-language README** — 75% increase over prior i18n high-water-mark
6. **10M hours training** — foundation-model-scale corpus
7. **Dual-AR architecture** — novel two-model cascade
8. **RVQ 10-codebook codec at 21 Hz** — lowest framerate TTS codec
9. **GRPO RL alignment for TTS** — LLM technique cross-modal transfer
10. **15,000+ emotion tags** — natural-language inline control
11. **SGLang production** — LMSYS inference runtime first in corpus
12. **2 arXiv publications** — most rigorous research evidence

## 9. Storm Bear vault impact

### Immediate

- Root `CLAUDE.md` updated with v20 project entry
- Root `GOALS.md` v20 session milestone appended
- **`PATTERN_LIBRARY.md` directly updated** (v2 Phase 5 protocol) — 5 new candidates + 1 refinement + Pattern #18 CN-evidence

### Medium-term

- Pattern Library audit candidate (15 candidates at threshold)
- Foundation-model scope category formalization (v2.1 candidate)
- License-category classification (v2.1 candidate)

### Long-term

- **graphify-on-vault STILL pending (now 4+ sessions overdue since v16)**
- T3 second entrant STILL pending
- Pattern #19 4th archetype validation at 2nd foundation-model wiki

## 10. Next wiki candidates

Criteria:
- **T3 second entrant** — ONLY remaining N=1 tier, would close 5/5 corpus validation
- **2nd foundation-model wiki** — validate Pattern #19 4th archetype + Pattern #28-35 candidates
- **2nd CN-ecosystem framework** — validate Pattern #18 regional strengthening
- **Research-lab commercial-entity 2nd** — validate Pattern #31

**Top priority per consolidation:** Pattern Library audit, THEN v21.

## 11. Strategic recommendation at v20

**State:**
- Library: 20 confirmed + 15 candidates (ratio 0.75:1, approaching audit)
- Routine v2 generalized (2 execution modes proven)
- Velocity preserved at ~2h
- graphify-on-vault **4+ sessions overdue**
- T3 second entrant still pending

**Recommendation sequence:**
1. **Run graphify on vault** (still highest-leverage single action — 30-60 min + $5-20 API)
2. **Pattern Library audit** (candidate count at 15, approaching v19 audit trigger)
3. **T3 second entrant** (closes 5/5 corpus validation)
4. Continue pattern observation on new wikis

**No consolidation BLOCKER currently.** v2 routine manages accumulation.

**⚠️ Explicit overdue note:** graphify-on-vault has been recommended every v16/v17/v18/v19/v20 iteration log. 4 sessions of ignored recommendation = user has de facto deprioritized it. Either:
- (a) Execute graphify-on-vault now and stop adding wikis
- (b) Explicitly deprioritize in GOALS.md and remove from future recommendations
- (c) Continue ignoring (current pattern) — accumulates technical debt in vault

## 12. References

- Parent: [[(C) index]]
- Prior iteration log: `../../TrendRadar - Beginner Analysis/04 Reviews/(C) 2026-04-19 v19 build learnings.md`
- Published: `../03 Published/(C) fish-speech - Huong dan cho nguoi moi.md` + `(C) Outside-scope meta-reference + Pattern 19 4th archetype.md`
- Pattern Library: `../../../PATTERN_LIBRARY.md` (vault root)
- Routine v2: `../../../05 Skills/llm-wiki-routine-v2.md`

---

**v20 complete. 2nd v2 routine execution (outside-scope mode). Pattern #19 4TH archetype (research-paper-chain) formalized. Pattern #29 refined. Pattern #18 CN N=2. 5 new candidates (#31-35). Pattern Library at 35 total. Velocity preserved at ~2h. v2 routine generalized across T4-extension + outside-scope modes. graphify-on-vault 4+ sessions overdue — strategic decision required.**
