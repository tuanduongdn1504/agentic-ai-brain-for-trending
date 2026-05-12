# v63 andrej-karpathy-skills build — iteration log

**Subject:** [`forrestchang/andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills)
**Build date:** 2026-05-09
**Routine:** llm-wiki-routine-v2.1
**Status:** DONE (Pattern #52 N=2 cleanly identified + N=3 retroactive correction caught + substitution question answered cleanly)

---

## 1. Milestones hit

### Corpus-level milestones

- **63rd wiki shipped** (v1 ECC 2026-04-17 → v63 andrej-karpathy-skills 2026-05-09; 23 days corpus age)
- **CORPUS-RECORD stars/day velocity** at observation: ~1,186 stars/day (3.2× mattpocock baseline)
- **CORPUS-FIRST source-celebrity-derivative-distillation observation** — solo-engineer distills public-figure observations into installable skill artifact with explicit attribution
- **Pattern #52 N=1 → N=3 cross-archetype strengthening** (mattpocock author-celebrity v57 + codex-plugin-cc corporate-celebrity v62 RETROACTIVE + andrej-karpathy-skills source-celebrity-derivative v63)
- **v62 audit gap caught** — codex-plugin-cc velocity (~847 stars/day) qualified for Pattern #52 strengthening but v62 wiki did not register; retroactive correction at v63 = sister to v61 catch of OpenSpec v58 missing from Pattern #21 evidence list
- **Storm Bear meta-entity 4-consecutive post-v60-RESTART** (v60 PASS + v61 PASS + v62 PASS + v63 PASS)
- **8-instance Phase 0.9 post-amendment window** v56-v63 = 7 PASS / 1 SKIP = **87.5% INCLUDE rate**
- **Karpathy = corpus-foundation-individual returns** — 1st explicit Karpathy citation in v8 autoresearch; v63 is direct derivative of corpus-foundation
- **Pattern #19 ecosystem-portfolio-builder N=2 sub-type strengthening** (gotalab v61 + forrestchang v63)

### Framework-specific milestones

- 121,227 stars / 12,246 forks / 639 watchers / 28 commits (created 2026-01-27; ~102 days at v63 ship)
- 4 principles in 1 CLAUDE.md (~65 lines source)
- 522-line EXAMPLES.md = corpus-rare pedagogical density
- 3-platform delivery (Claude Code plugin / per-project / Cursor) at single-skill scale
- Bilingual EN+ZH

---

## 2. Phase breakdown

| Phase | Duration (est) | Status |
|---|---|---|
| 0 Probe + classification | ~10 min | ✅ |
| 1 Scaffold | ~5 min | ✅ |
| 2 Sources (3 cluster summaries) | ~12 min | ✅ |
| 3 Entities (4 entity pages) | ~25 min | ✅ |
| 4a Beginner guide bilingual | ~10 min | ✅ |
| 4b Pattern #52 N=2-N=3 deliverable | ~12 min | ✅ |
| 5 Iteration log + Pattern Library update | ~10 min | ⏳ in progress |
| 6 Vault sync | ~6 min | pending |

**Total est:** ~85-90 min main-loop direct-write — within sub-2h plateau; appropriate for Pattern-Library-strengthening-heavy wiki.

---

## 3. What worked

- **Phase 0 fast probe** caught EXTREME-VIRAL velocity immediately on `gh api repos/...` call returning 121K stars; pre-empted Pattern #52 routing decision
- **Re-examination of codex-plugin-cc v62 stars/day at entity-3 phase** caught v62 audit gap (~847 stars/day qualifies for Pattern #52); retroactive N=3 correction kept Pattern Library accurate
- **Substitution question handling** — user's prior question about mattpocock + karpathy combo replacing cc-sdd answered cleanly via category distinction (behavioral-overlay vs methodology-harness); preview in entity 1 + full answer in entity 4
- **Cross-platform single-skill manual-sync sub-axis** registered as NEW within Pattern #18 Layer 2 (vs cc-sdd v61 framework-scale install-time-translator); clean distinction
- **Karpathy corpus-foundation-individual lineage observation** — Pattern #57 57c-positive-corpus-citation strongest instance in corpus

---

## 4. What didn't work / friction

- **Initial WebFetch returned high-level summary rather than full README** — switched to direct `curl` of raw.githubusercontent.com files for verbatim content; faster after switch
- **`gh` CLI not installed** on user's system; fell back to `curl https://api.github.com/...` with Python JSON parsing — slower but works
- **Pattern #52 stale-flag decision required restraint** — strong N=3 evidence at v63 ship tempting to promote, but sustained-velocity criterion is the actual test; deferred to v69 audit per v60 Item 12 pre-registration discipline
- **EXAMPLES.md is large (522 lines)** — only read first 220 lines for cluster-3 analysis; rest assumed structurally similar (8 examples, 2-per-principle) — minor coverage gap

---

## 5. Routine v2.2 action items (NEW from v63)

1. **Phase 0 velocity-screen automation** — auto-compute stars/day-vs-90d-threshold for ALL incoming wiki subjects (not only viral-routing subjects). Would have caught codex-plugin-cc v62 Pattern #52 qualification at v62 ship rather than retroactively at v63.
2. **Source-celebrity-derivative-distillation as Pattern #19 a4 sub-type** — codify recognition criteria for v63-style distillation: (1) author ≠ source individual, (2) explicit source attribution with URL, (3) public observations as raw material, (4) installable artifact packaging.
3. **EXTREME-VIRAL sub-archetype 3-axis (52a/52b/52c)** — codify in v66 audit; deliberate consolidation vs split at v69.
4. **Watchers/stars + forks/stars ratio sub-investigation discipline** — when EXTREME-VIRAL subjects appear, capture engagement metrics not just stars; helps distinguish drive-by-stars-dominant from active-deployment.
5. **Pre-Phase-6 retroactive-correction-check** — when v63-style correction is caught, formal mechanism to retroactively update prior wiki's Pattern Library register (vs only forward-only updates).

---

## 6. Total action items accumulating

Routine v2.2 candidates post-v63: **25 items accumulated** (5 new at v63 + 20 prior from v60+v61+v62+v63 audit). **Codification natural cadence URGENT — codify at v65 window** (was approaching at v65 already; v63 brings count to 25 = above 20-threshold).

---

## 7. Meta-observations

- **Pattern #52 N=3 in 13 wikis (v50→v63)** = relatively fast accumulation for OBSERVATIONAL FLAG; cross-archetype velocity-source diversity (author / corporate / source-celebrity-derivative) supports structural-N pattern emergence
- **Pattern #19 corporate-archetype N=3 cross-org** post-v62 NOW joined by **derivative-distillation a4 NEW sub-type** post-v63; Pattern #19 sub-archetype lattice growing rapidly (v61 ecosystem-portfolio-builder + v62 corporate-strategic + v63 derivative-distillation)
- **forrestchang ecosystem-portfolio-builder N=2** (sister to gotalab v61) suggests Pattern #19 ecosystem-portfolio-builder is repeatable mechanism, not gotalab-specific
- **v62 audit gap correction at v63** = 2nd consecutive audit-gap-caught-at-next-wiki cycle (v61 caught v58→v60 gap; v63 catches v62 gap); may signal need for routine v2.2 pre-Phase-6 fact-verification expansion
- **Karpathy's authority transfers** — derivative-distillation outperforms author-original on velocity (1186 vs 370 stars/day); when source celebrity > author celebrity, distillation can amplify reach

---

## 8. Unique findings (corpus-firsts at v63)

8 corpus-firsts:

1. Largest stars/day velocity in corpus history (~1,186/day at observation)
2. Pattern #52 N=2 strengthening ending 13-wiki OBSERVATIONAL-FLAG-stale-since-v50
3. Pattern #52 N=3 retroactive correction (v62 audit gap caught)
4. Source-celebrity-derivative-distillation = Pattern #19 a4 NEW sub-type
5. Multi-platform single-skill manual sync = Pattern #18 Layer 2 NEW sub-axis
6. Bilingual EN+ZH at single-skill (vs prior EN-only single-skill artifacts)
7. Karpathy explicit X-tweet citation in skill artifact = Pattern #57 57c-strongest instance
8. forrestchang ecosystem-portfolio-builder N=2 sub-type confirms gotalab v61 mechanism repeatable

---

## 9. Storm Bear vault impact

**Pilot ranking update:**
- andrej-karpathy-skills inserts at **#3.5 NEW Tier-2** (after free-claude-code v60 #2 / before n8n v56 Tier-2)
- Recommended deployment timing: Week 3+ stack-layer test AFTER Tier-1 pilots
- Setup cost very low (~2 min plugin install)
- Operational utility MEDIUM (behavioral overlay; not workflow-primitive contribution)

**Vault state changes (v63 wiki-ship):**
- Confirmed patterns: 42 → 42 (Pattern #52 promotion deferred to v69)
- Active candidates: 19 → 19 (only within-pattern strengthenings; no NEW top-level candidates)
- Stale candidates: 1 → 1 (Pattern #52 preserved with stronger evidence; Pattern #52 itself wasn't in stale-candidates list — it's an OBSERVATIONAL FLAG distinct category)
- Ratio: 0.452:1 (UNCHANGED at v63 ship; LARGEST sub-0.475 zone PRESERVED)

**Pilot deployment urgency UNCHANGED:** 8 ranked pilots / 0 deployed at v62 ship → 9 ranked / 0 deployed at v63 ship. Goal #2 ("build software with these tools") only resolved via actual pilot deployment.

---

## 10. Next wiki candidates (strategic selection)

### High-priority (would directly satisfy v66/v69 audit criteria)

1. **2nd source-celebrity-derivative-distillation** (e.g., a future "andrew-ng-skills" or "fast.ai-skills") — would un-stale-flag Pattern #19 a4 sub-type
2. **2nd multi-platform single-skill manual-sync** — would un-stale-flag Pattern #18 Layer 2 NEW sub-axis
3. **Subject hitting >300 stars/day with NEW velocity-source archetype** — would test Pattern #52 sub-archetype taxonomy completeness

### Medium-priority

4. **3rd corporate-org observation in T1-T3** — would advance Pattern #19 corporate-archetype N=3+ cross-org
5. **T2-T5 SDD framework** — would satisfy Pattern #21 cross-tier criterion (still all T1)

---

## 11. Strategic decision point

### Consolidation recommendation

**No consolidation block at v63 ship.** Ratio 0.452:1 well below 0.95:1 trigger. Action backlog ~25 (above 20 routine-v2.2-cadence threshold; below 100 hard-block).

### Routine v2.2 codification urgency

**Codification URGENT at v65 window.** 25 candidates accumulated:
- 5 new at v63 (velocity-screen automation / derivative-distillation criteria / sub-archetype 3-axis / engagement-signal discipline / pre-Phase-6 retroactive-correction-check)
- 7 from v62 (fast-counter-evidence detection / implementation-stratum taxonomy / Phase 0.9 (a)-FAIL-handling / NEW-pattern-candidate-mechanism / background-task-lifecycle-set / etc.)
- 7 from v61 (Phase 0.9 STRICT-triad / EXTENDED MINI-AUDIT classification / pre-step audit protocol / etc.)
- 6 from v60 (lineage-test/independence-test ordering / cross-archetype N-counting / pre-Phase-6 fact-verification expansion / Phase 0.4 docs-tree-listing / etc.)

### Backlog escalation

**Pilot deferral imbalance ESCALATES at v63** — 9 ranked pilots / 0 deployed. Goal #2 progress further stalled. v62 STRONG RECOMMENDATION (pause wiki builds at v63/v64 + pilot cc-sdd + codex-plugin-cc comparison-bundle) HAS NOT BEEN EXECUTED — wiki-build at v63 was elected over pilot-execution per user explicit request.

**RE-AFFIRMED RECOMMENDATION:** Pause wiki builds at v64 window; execute Tier-1 pilot bundle (cc-sdd + codex-plugin-cc + free-claude-code) Week 1-2; resume wiki builds with pilot evidence informing v66/v69 audit decisions.

---

## 12. Scorecard

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Novelty | **5** | Largest stars/day velocity in corpus; source-celebrity-derivative-distillation NEW mechanism |
| Pilot-relevance (Storm Bear) | **3** | Tier-2; orthogonal layer; VERY low setup cost; complement-not-substitute to Tier-1 pilots |
| Pattern-contribution | **5** | Pattern #52 N=1 → N=3 cross-archetype + Pattern #19 a4 NEW sub-type + Pattern #18 NEW sub-axis + Pattern #57 57c-strongest + v62 audit gap caught |
| Velocity | **5** | ~85-90 min (sub-2h plateau preserved; appropriate for Pattern-Library-heavy wiki) |
| Quality | **5** | DONE clean; substitution question answered cleanly; retroactive correction caught; sustained-velocity discipline preserved |

**Overall: 23/25** — Slightly below v62's 24/25 (v62 had 10 corpus-firsts vs v63's 8); but v63 made stronger Pattern Library contribution (N=3 retroactive correction is meaningful for corpus health-loop).

---

## 13. Primitive-count check (v2.1 informal discipline)

- **Probed primitive-count:** 4 behavioral principles + 1 skill artifact + 3 platform paths + 522-line examples corpus + 4 governance files
- **Fits 4-entity format cleanly?** YES — Entity 1 (core artifact) + Entity 2 (derivative-distillation mechanism) + Entity 3 (Pattern #52 N=2-N=3) + Entity 4 (multi-platform + Storm Bear meta + substitution question)
- **Compression strategy:** counter-evidence focus folded into Phase 4b deliverable; substitution question answered in entity 4 + bilingual guide
- **Operator decision:** ACCEPT compression. 4-entity format absorbed Pattern #52 strengthening + Pattern #19 a4 + Pattern #18 sub-axis + Pattern #57 strengthening + substitution analysis cleanly.
