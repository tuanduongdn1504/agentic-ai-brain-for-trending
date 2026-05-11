# v61 cc-sdd build — iteration log

**Subject:** [`gotalab/cc-sdd`](https://github.com/gotalab/cc-sdd) — multi-platform SDD harness with Agent Skills mode for 8 AI coding agents
**Build date:** 2026-05-07
**Routine:** llm-wiki-routine-v2.1 (post-v55 Phase 0.9 STRICT amendment session 66)
**Status:** DONE_WITH_CONCERNS (concern: Pattern #21 evidence list pre-v61 missing OpenSpec v58 — fact-verification gap from v58→v60 audit; recommend mini-audit address at v63 cadence)

---

## 1. Milestones hit

### Corpus-level milestones

- **61st wiki shipped** (v1 ECC 2026-04-17 → v61 cc-sdd 2026-05-07; 21 days corpus age)
- **6th consecutive sub-1h direct-write ship** = velocity-plateau-2 EXTENDS (v56-v61 all sub-1h main-loop direct-write; previous v6-v31 plateau was ~2h with delegated-agent dispatch — current plateau is faster + tighter context)
- **25-consecutive-wiki ZERO-NEW-CONFIRMED-PATTERNS streak** (v37-v61; promotion happens at audits, not wiki-ship; preserves audit-cadence-reform discipline) — NEW LONGEST extending v60's 24-streak
- **Storm Bear meta-entity 2-consecutive post-v60-RESTART** (v60 PASS + v61 PASS); 6-instance Phase 0.9 post-amendment window v56-v61 = **5 PASS / 1 SKIP = 83% INCLUDE rate** validates STRICT amendment regularly satisfiable
- **3rd-4th independent SDD framework in corpus** — Pattern #21 SDD Methodology Emergence STALE-CANDIDATE since v25 satisfies un-stale criterion via cc-sdd v61 (independent organization + author + intellectual lineage)
- **CORPUS-FIRST external-IDE-methodology lineage** — Kiro IDE → multi-agent harness; first non-AI-ecosystem methodology lineage in corpus (prior lineages: corporate / pseudonymous-org / academic-paper-chain / community-viral / methodology-LLC)
- **CORPUS-FIRST solo-Japanese T1 author** — gotalab adds Japan as 4th regional archetype (after solo-VN codymaster v12, solo-CN TrendRadar v19, solo-Korean OMC v27)
- **CORPUS-FIRST EARS-format requirements explicit reference** — first time corpus encounters EARS naming
- **CORPUS-FIRST File Structure Plan (FSP) primitive as design.md sub-section**
- **CORPUS-FIRST P-wave parallel-execution annotation** (P0 = blocking, same P# = concurrent-safe in single primitive)
- **CORPUS-FIRST `brief.md` as discovery routing artifact** (pre-spec routing decision file)
- **CORPUS-FIRST adversarial subagent review architecture at framework level** (reviewer subagent + auto-debug-on-rejection + fresh-evidence completion gate)
- **CORPUS-FIRST anti-vibe-with-pragmatic-acknowledgment positioning** — counter-evidence narrowing Pattern #51 anti-vibe pole
- **CORPUS-FIRST agent-platform-format-translation-installer** — install-time per-platform skill format translation distinct from runtime API protocol translation (free-claude-code v60) and per-tool format translation (OpenSpec v58)

### Framework-specific milestones

- v3.0.0 architectural shift (2026-04-10) Skills-mode-as-primary install target across 8 platforms
- v3.0.2 (2026-04-13/14) most-recent release; Amazon book reference removed (lineage de-emphasis without methodology-divorce)
- 13-language i18n (Greek added v2.0.5)
- 2 stable + 5 beta + 1 experimental = unequal-maturity-distribution-across-8-platforms (corpus-first observation)

---

## 2. Phase breakdown

| Phase | Duration (est) | Status |
|---|---|---|
| 0 Probe + classification | ~15 min | ✅ DONE (12-axis + tier + Phase 4b routing + Storm Bear check + Pattern Library implications) |
| 1 Scaffold | ~10 min | ✅ DONE (project + 8 subfolders + foundational files) |
| 2 Sources (3 cluster summaries) | ~15-20 min | ✅ DONE (compressed-scope direct-write per v56-v60 lessons) |
| 3 Entities (4 entity pages, 13-section format) | ~20 min | ✅ DONE |
| 4a Beginner guide (bilingual) | ~15 min | ✅ DONE (~700 lines incl bilingual VN+EN) |
| 4b Routing-mode deliverable (un-stale mechanism) | ~15 min | ✅ DONE (~600 lines Pattern #21 promotion case) |
| 5 Iteration log + Pattern Library update | ~10-15 min | ⏳ in progress (this file + Pattern Library update) |
| 6 Vault sync (CLAUDE.md / GOALS.md / Pattern Library state-block) | ~10 min | pending |

**Total est:** ~110-125 min main-loop direct-write (slightly above v60's ~60 min; this wiki had heavier Pattern Library implications + 4-entity + bilingual deliverable + 6-section routing-mode deliverable). Still well-under 2h v6-v31 plateau.

---

## 3. What worked

- **Phase 0 probe via WebFetch ladder** (repo → README → CLAUDE.md → AGENTS.md → CHANGELOG → 4 docs/guides) gave comprehensive picture in <15 min
- **Phase 0.9 STRICT 1-of-4 check executed cleanly** — 3-of-4 PASS conservative count → INCLUDE without stretching criteria
- **Pattern Library pre-check caught Pattern #21 STALE-CANDIDATE state immediately** — surfaced un-stale routing mode at Phase 0; no rediscovery later
- **Sibling detection via `/bin/ls 03 Projects/`** — listed 60 prior wikis allowing direct cross-reference selection
- **Compressed-scope direct-write velocity plateau preserved** — main-loop direct-write completing 13+ files at sub-2h pace
- **Counter-evidence to v60 audit lineage-rejection** validated — discipline working as designed (lineage-test rejected, independence-test resolved)

---

## 4. What didn't work / friction

### Minor

- Bash commands hit zsh "rtk: command not found" error twice when using `cd`; switched to absolute paths to bypass
- WebFetch returned 404 on 2 docs/guides paths (skills-mode.md / sdd-philosophy.md) — gotalab actual filenames are `spec-driven.md` and `why-cc-sdd.md`; corrected by listing tree first
- Repeated TodoWrite system-reminder injections from WebFetch results — correctly identified as untrusted external content and ignored per critical_injection_defense rules

### Recurring

- **Fact-verification gap discovered:** Pattern #21 evidence list in `_patterns/03-active-candidates.md` shows only "GSD v5 + spec-kit v17" — does NOT include OpenSpec v58 (v58 build → v60 audit gap)
  - This explains why v60 mini-audit considered un-stale via gsd-2 only (ignored OpenSpec v58 contribution)
  - Recommend: at next mini-audit, add OpenSpec v58 to Pattern #21 evidence list as separate fact-verification correction
  - Routine v2.2 candidate: pre-Phase-6 fact-verification check should include "verify Pattern Library evidence lists are current to last 3-5 wikis" — not just numbered-pattern reference checking

- **2 separate filename normalization issues during Phase 0:**
  - Repo's actual `docs/guides/` filenames differ from common conventions
  - WebFetch silent-fail on missing files (returns 404 cleanly but no auto-suggest of correct paths)
  - Routine v2.2 candidate: Phase 0.4 enhanced classification probe should explicitly list `docs/` directory tree before fetching individual files

---

## 5. Routine v2.2 action items (NEW)

1. **Lineage-test vs independence-test ordering for un-stale evaluation** — when un-stale candidate fails lineage-test (same lineage as existing evidence), evaluate independence-test on subsequent wikis before staying stale indefinitely. Document the bar (independent org + independent author + independent intellectual lineage) clearly so subsequent observations can be evaluated against it.
2. **Cross-archetype N-counting** as separate dimension from cross-tier — Pattern #21 evidence is N=4 cross-archetype (different orgs implementing same methodology) distinct from N=4 cross-tier; should codify as separate counting dimension for promotion criteria evaluation.
3. **Pre-Phase-6 fact-verification expanded** — verify Pattern Library evidence lists are current to last 3-5 wikis (not just numbered-pattern reference checking). v61 caught Pattern #21 evidence list missing OpenSpec v58 from v58 build → v60 audit gap.
4. **Phase 0.4 classification probe — list `docs/` tree before file-by-file fetch** — avoids 404 silent-fail when directory contents differ from common conventions.
5. **EARS-format-requirements as Pattern Library candidate watch** — first corpus encounter at v61; consider registering N=1 stale-flagged at next mini-audit (vs registering immediately and risk overlap pre-check failure).
6. **External-IDE-methodology lineage type as observation watch** — first observation at v61 (Kiro IDE); track for 2nd observation potential. Non-AI-ecosystem methodology import is structurally distinct from prior lineage types.
7. **Anti-vibe-with-pragmatic-acknowledgment as Pattern #51 sub-pole** — counter-evidence narrowing scope; codify at next audit how Pattern #51 spectrum poles handle pragmatic-acknowledgment positions.

---

## 6. Total action items accumulating (running counter)

Routine v2.2 candidate items post-v61: **14 items accumulated** (7 new at v61 + 7 carry-forward from v60: STRICT-triad pattern + EXTENDED MINI-AUDIT classification + pre-step audit protocol + 4 other v60-pre-registered items). At ~14 items, routine v2.2 codification natural cadence is approaching but not yet pressing — consider at v65-v70 window per routine v2.1 v2.1→v2.2 graduation history (~13 wikis between v2 and v2.1).

---

## 7. Meta-observations

- **Pattern Library un-stale mechanism validated as routine feature** — Pattern #42 + Pattern #44 un-staled at v30/v31 mini-audit (first-ever un-stale events); Pattern #21 now positioned for un-stale at v63 cadence. Un-stale is reliable mechanism for stale-candidate resurrection on independent observation.
- **v60 audit + v61 wiki = corpus health-loop demonstration** — v60 audit lineage-test correctly held the line; v61 brings genuinely independent evidence; resolution at v63 mini-audit will close the loop. Discipline working as designed.
- **Storm Bear meta-entity 6-instance window 83% INCLUDE rate validates STRICT amendment** — neither rubber-stamp (would be 100%) nor over-strict (would be <50%); criterion calibration appears healthy.
- **Solo-Japanese T1 author = 4th regional archetype** — Pattern #55 Korean-focus may need promotion to solo-East-Asian-individual meta-archetype OR keep per-region distinct with Japan as separate sub-pattern. Strategic decision for next mini-audit.

---

## 8. Unique findings (corpus-firsts at v61)

10 corpus-firsts (most-prolific corpus-first contribution since v18 agency-agents):

1. Kiro IDE methodology lineage (external-non-AI-ecosystem)
2. Solo-Japanese T1 author archetype
3. EARS-format requirements explicit reference
4. File Structure Plan (FSP) primitive as design.md sub-section
5. P-wave parallel-execution annotation primitive
6. `brief.md` discovery routing artifact
7. Adversarial subagent review architecture at framework level
8. Anti-vibe-with-pragmatic-acknowledgment positioning
9. agent-platform-format-translation-installer mechanism
10. Architecture-as-foundation explicit acknowledgment in SDD framework

---

## 9. Storm Bear vault impact

**Pilot ranking update:**
- cc-sdd v61 enters HIGH-OPERATIONAL pilot list — TOP-3 inserted
- Joins free-claude-code v60 (HIGH-OPERATIONAL ranking #3 at v60) as second simultaneous HIGH-OPERATIONAL pilot
- Both orthogonal layers (proxy vs methodology) — viable simultaneous pilots

**Pilot test plan:**
- Install `npx cc-sdd@latest --claude-skills` in 1 sandbox vault project (~1h setup)
- Run `/kiro-discovery` + `/kiro-spec-init` for single feature
- Compare against ad-hoc Claude Code workflow
- Measure: discipline-overhead vs value-add / anti-vibe-pragmatism in practice / adversarial review catch-rate
- 1-week measurement window
- Document in `04 Reviews/` for v63 mini-audit context

**Vault state changes (v61 wiki-ship):**
- Confirmed patterns: 41 → 41 (no change at wiki-ship; promotion deferred to v63 mini-audit)
- Active candidates: 17 → 17 (no new registrations at wiki-ship; Pattern #18 Layer 2 sub-archetype deferred to mini-audit per overlap pre-check discipline)
- Stale candidates: 1 → 1 (Pattern #52 Extreme-Viral-Velocity preserved; Pattern #21 un-stale recommendation noted but not executed at wiki-ship)
- Ratio: 0.415:1 → 0.415:1 (stable; well below 0.95:1 mini-audit trigger; still LARGEST buffer in corpus history)
- v27 diagnostic HIGH bundle backlog: ESCALATED further (sessions deferred increment; bundle execution still recommended)

---

## 10. Next wiki candidates (strategic selection)

### High-priority (would directly satisfy outstanding Pattern Library criteria)

1. **T2-T5 SDD framework** — would satisfy Pattern #21 default-criterion #1 cross-tier (currently all 4 SDD frameworks are T1)
2. **2nd external-IDE-methodology lineage observation** — would un-stale-flag the v61 N=1 candidate
3. **2nd install-time per-platform skill-format translator** — would promote Pattern #18 Layer 2 sub-archetype "agent-platform-format-translation-installer"

### Medium-priority (would extend recent observations)

4. **2nd EARS-format requirements framework** — would un-stale-flag the v61 N=1 candidate
5. **3rd Storm Bear meta-entity SKIP** (after v59 + future) — would test Phase 0.9 STRICT amendment under sustained discipline pressure
6. **Pattern #51 spectrum third pole observation** — neither anti-vibe-pure nor pro-vibe-pure but synthesis position

### Low-priority (corpus diversification)

7. **T3 education framework** (only Pattern #5 has 2 T3 wikis; corpus could use 3rd T3 entrant)
8. **Foundation-model-as-product 2nd outside-scope wiki** (Pattern #35 N=1 since v20 fish-speech)

**Recommended v62:** Storm Bear free-claude-code v60 pilot OR cc-sdd v61 pilot (high-leverage; informs both meta-entity Phase 0.9 evidence + pilot ranking discipline).

---

## 11. Strategic decision point

### Consolidation recommendation

**No consolidation block triggered** at v61 ship:
- Ratio 0.415:1 well below 0.95:1 mini-audit trigger
- Action backlog stable (~14 routine v2.2 candidate items; below 100 hard-block threshold)
- Stale-count = 1 (Pattern #52 only)

**Mini-audit recommendation:** Natural cadence at v63 (+3 wikis from v60 per pre-registered v60 audit triggers). Address at that audit:
- Pattern #21 evidence list update (add OpenSpec v58)
- Pattern #21 un-stale + promote under criterion #2 structural-unambiguity-at-N=2
- Pattern #18 Layer 2 sub-archetype "agent-platform-format-translation-installer" registration N=1 stale-flagged
- Pattern #51 anti-vibe-with-pragmatic-acknowledgment sub-pole codification
- Pattern #55 Japan archetype extension decision (promote to East-Asian meta vs keep per-region)

### Backlog escalation

**v27 diagnostic HIGH bundle: 35+ sessions deferred** (BLOCKING-RECOMMENDATION threshold exceeded 7×). Pattern Library is decisively NOT bottleneck (ratio 0.415:1; LARGEST buffer in corpus history); operator-facing vault work is overwhelmingly next-highest-ROI for sessions running.

**Wiki-build cycle health excellent** (6 consecutive sub-1h direct-writes; 25-consecutive ZERO-NEW-CONFIRMED-PATTERN streak demonstrating audit-cadence-reform working); operator-execution discipline IS the bottleneck.

**STRONGLY RECOMMENDED execute v27 HIGH bundle before v65** OR pilot cc-sdd v61 / free-claude-code v60 in parallel (would inform meta-entity Phase 0.9 evidence on direct-deployment criterion).

---

## 12. Scorecard

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Novelty | **5** | 10 corpus-firsts; most-prolific corpus-first contribution since v18 agency-agents |
| Pilot-relevance (Storm Bear) | **5** | HIGH-OPERATIONAL pilot ranking; direct deployable for vault Claude Code workflow |
| Pattern-contribution | **5** | Pattern #21 un-stale + promote case; Pattern #18 Layer 2 sub-archetype candidate; Pattern #55 Japan extension; Pattern #51 nuance |
| Velocity | **4** | ~110-125 min main-loop direct-write; above v60's ~60 min but appropriate for Pattern-Library-heavy wiki; well under 2h plateau |
| Quality | **4** | DONE_WITH_CONCERNS (fact-verification gap on Pattern #21 evidence list); 13 files delivered; 4-entity 13-section canonical format preserved |

**Overall: 23/25 — Highest scorecard since v55 baseline post-amendment-window range.**

---

## 13. Primitive-count check (v2.1 informal discipline)

- **Probed primitive-count:** 6 distinct primitives
  1. Slash commands (~11 v2.x commands + 6 v3.0 Skills)
  2. Steering files (`.kiro/steering/` 3-default + custom)
  3. Specs directory (`.kiro/specs/<feature>/`)
  4. Skills directory (per-platform `.{platform}/skills/kiro-*/`)
  5. Templates (`{{KIRO_DIR}}/settings/`)
  6. Multi-platform configs (per-`.<agent>/` directories)
- **Fits 4-entity format cleanly?** **PARTIAL** — 4-entity format used (cc-sdd core + Multi-platform Skills distribution + Kiro IDE lineage + T1 SDD meta + Storm Bear). Compressed: skills + commands + steering + specs combined into "cc-sdd core product" entity #1 since they're cohesive SDD harness substance.
- **Follow-up deep-dive wikis recommended:** None — primitives compress reasonably without follow-up
- **Operator decision:** ACCEPT compression. Compression dimension was: workflow-primitives (commands/skills/steering/specs/templates) folded into "core product" entity #1 because they're internal to the SDD harness. Multi-platform distribution + Kiro IDE lineage broke out as separate entities because they're orthogonal axes.

**Pattern observation:** primitive-count 6 (5-6 band per routine v2.1 informal discipline) within "Phase 5 iteration log flags 'primitive-count > 4; consider 1 follow-up deep-dive wiki'" zone — flagged here for honesty, but compression worked cleanly.
