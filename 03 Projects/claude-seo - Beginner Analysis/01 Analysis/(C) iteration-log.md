# Iteration log — v64 claude-seo wiki build

> **Routine:** llm-wiki-routine-v2.1 direct-write mode
> **Build date:** 2026-05-13
> **Sessions:** continuation of v62/v63/v63-EARLY-mini-audit/pilot-v3.2 arc
> **Subject:** `AgriciDaniel/claude-seo` v1.9.9

## Phase-by-phase log

| Phase | Status | Duration (est) | Notes |
|---|---|---|---|
| Phase 0 — Probe + classify | ✅ COMPLETE | ~15 min | GitHub API + curl downloads (README 398 / CLAUDE 210 / AGENTS 126 / CHANGELOG 607 / plugin.json / marketplace.json); 12-axis classification; Phase 0.9 STRICT 1-of-4 evaluation (SKIP) |
| Phase 1 — Scaffold + project CLAUDE.md | ✅ COMPLETE | ~15 min | Project folder + CLAUDE.md with classification + Phase 0.9 SKIP + Pattern Library preview |
| Phase 2 — Cluster summaries | ✅ COMPLETE | ~20 min | index.md + 3 cluster files (Cluster 1 README + Cluster 2 architecture + Cluster 3 ecosystem/CHANGELOG) |
| Phase 3 — 4 entity pages | ✅ COMPLETE | ~30 min | Entity 1 core / Entity 2 ecosystem-portfolio N=3 PRIMARY / Entity 3 NEW T1 sub-archetype + Living-Domain-Standards / Entity 4 multi-platform + Pattern Library implications package |
| Phase 4a — Bilingual VN+EN beginner guide | ✅ COMPLETE | ~15 min | 9-section bilingual walkthrough (what / who / install / try 5min / strengths / caveats / when-to-use / vault implications / further reading) |
| Phase 4b — Pattern #19 N=3 promotion proposal | ✅ COMPLETE | ~12 min | Formal proposal document for v66 audit deliberation; 5-criteria evidence package; 3-axis sub-taxonomy v69-deferred recommendation |
| Phase 5 — Iteration log + Pattern Library update | 🔄 in progress | ~10 min so far | This document + 03-active-candidates.md (#77 + #78 NEW) + 05-recent-additions.md (v64 strengthening notes block appended) |
| Phase 6 — Vault sync | pending | est ~5-10 min | root CLAUDE.md state-block update + 03a-projects entry append + GOALS version log |

**Total estimated wiki-build time at Phase 5 in-progress:** ~117 min (sub-2h direct-write velocity; on-track with v60-v63 velocity range)

## Key decisions made

### 1. Phase 0.9 SKIP (Storm Bear meta-entity)

**Decision:** SKIP. 0/4 strong PASS + 2/4 WEAK.

**Evidence:** SEO domain not directly vault-relevant per Goal #2 (vault is LLM Wiki knowledge base, NOT marketing site; not deployable for software-development tooling). No in-corpus references. Solo-individual not archetype-peer per Phase 0.9 STRICT discipline.

**Streak effect:** Storm Bear meta-entity 4-consecutive post-v60-RESTART **RESETS to 0** at v64. 9-instance post-amendment window: 77.8% INCLUDE rate (7 PASS / 2 SKIP) — STRICT calibration confirmed healthy (rejects when truly non-operational; not over-strict).

### 2. Entity slot reallocation post-SKIP

**Decision:** Reallocate 4th entity slot to "multi-platform + Pattern Library implications package" rather than leaving entity count at 3.

**Rationale:** Phase 0.9 SKIP cleanly removes Storm Bear meta-entity slot but the v64 wiki has substantial Pattern Library implications (6 strengthenings + 2 NEW candidates + 4 observational candidates). Consolidating these into Entity 4 keeps them discoverable rather than scattering across cluster pages.

**Routine v2.2 candidate captured:** "Phase 0.9 SKIP entity slot reallocation discipline" — when STRICT yields SKIP, formally reallocate to Pattern Library implications.

### 3. Phase 4b PRIMARY routing

**Decision:** Phase 4b PRIMARY = Pattern #19 ecosystem-portfolio-builder N=3 promotion proposal.

**Rationale:** N=3 cross-archetype with 3 distinct portfolio shapes is the strongest single Pattern Library implication of v64 ship. PROMOTION-ELIGIBLE under criterion #2 (structural-unambiguity-at-N=2 already exceeded with margin) + criterion #3 (3 distinct archetypes) + criterion #4 (mechanism specifiable). Sub-taxonomy 19a/19b/19c deferred to v69 (need N=4+ before splitting).

**Routine v2.2 candidate captured:** "Phase 4b PRIMARY routing discipline" — when wiki ship has clear PRIMARY Pattern Library implication, structure Phase 3 entity pages around it as PRIMARY deliverable. Pre-register at Phase 0 classification.

### 4. NEW candidate proposal-document discipline

**Decision:** When Phase 4b generates NEW top-level candidate(s), draft formal proposal-document at `01 Analysis/` for v66 audit deliberation (not just append to `05-recent-additions.md`).

**Implementation:** v64 demonstrates with Pattern #19 N=3 promotion proposal. Length ~3KB; structured per audit criteria; includes recommended verdict + checklist + cross-references.

**Routine v2.2 candidate captured:** "NEW Pattern candidate proposal-document discipline."

## Surprises + corrections

### Surprise 1: claude-seo's external-standards tracking is corpus-strongest

**Observation:** 8 deprecation events tracked with specific dates is the strongest external-authority tracking observed in 63 prior wikis. This motivated registration of NEW Pattern #78 Living-Domain-Standards Tracking.

**Why surprising:** Most T1 plugins describe capabilities; claude-seo describes capabilities + tracks how external standards (Google / Schema.org / Anthropic spec / ISO codes) evolve over time with dated absorption. Different mechanism from prior corpus patterns.

### Surprise 2: 5-version-source atomic-bump CI discipline (13 assertions)

**Observation:** claude-seo's v1.9.7 → v1.9.9 thread documents a 2-month case study in manifest-drift-as-learning. v1.7.x initial drift → v1.9.7 5-source contradiction → v1.9.8 first test suite → v1.9.9 13 assertions across 4 new manifest-consistency tests.

**Captured as:** Observational candidate "Manifest-Drift-As-First-Class-CI-Concern" for v66 deliberation.

### Surprise 3: codex-seo sister-port = NEW Pattern #18 Layer 2 sub-archetype

**Observation:** Solo author (Agrici Daniel) maintains PARALLEL repos for distinct vendor primitives — no translation layer; codex-seo is structurally a sibling repo, not a derived port.

**Why this matters:** Distinct from runtime translation (v60 free-claude-code) / install-time translation (v61 cc-sdd) / cross-vendor bridge-as-plugin (v62 codex-plugin-cc). N=1 stale-flagged at v64; un-stale criterion = 2nd subject with solo-author cross-vendor parallel-port arrangement.

### Correction: NEW candidate numbering tentative

**Issue:** Entity 3 page used speculative numbering #80 + #81 for the 2 NEW top-level candidates.

**Correction:** Formal numbering in `_patterns/03-active-candidates.md` is **#77 (T1 domain-vertical-skill-collection) + #78 (Living-Domain-Standards Tracking)** — directly following v63 mini-audit's #74 + #75 + #76 registrations. Entity 3 numbering left as "tentative" per the entity page's own disclaimer ("Numbering tentative pending v66 actual audit").

## Pattern Library implications snapshot (post-v64 ship)

| Category | Item count | Net change |
|---|---|---|
| Confirmed patterns | 42 | unchanged |
| Active candidates | **21** | +2 (v64 NEW: #77 + #78) |
| Stale candidates | 1 | unchanged |
| Retired | 9 | unchanged |
| Observation-tracks | 6 | unchanged |
| **Total full / active** | **77 / 63** | +2 active |
| **Ratio** | **0.500:1** | +0.048 from 0.452:1 |
| Buffer to 0.95:1 mini-trigger | 0.450 | -0.048 (still healthy in sub-0.55 zone since v60) |
| Routine v2.2 codification candidates | **29** | +4 from v64 |
| 9-instance Phase 0.9 INCLUDE rate | **77.8%** (7 PASS / 2 SKIP) | -9.7% from 87.5% (v64 = 2nd SKIP) |
| Storm Bear meta-streak | **0** | RESET from 4 |
| ZERO-NEW-ACTIVE-CANDIDATES streak | BROKEN | +2 candidates at v64; streak un-counted |

## v66 audit agenda accumulated (post-v64)

**Combined items from v63 EARLY-AUDIT + v63 wiki-ship + v64 wiki-ship:** ~**24+ items**

PRIMARY deliberations:
1. **Pattern #19 ecosystem-portfolio-builder N=3 PROMOTION** (v64 PRIMARY) — proposal doc ready
2. **Pattern #21 SDD methodology emergence un-stale** (carry from v63 EARLY mini-audit — RESOLVED at v63 promotion)
3. **Pattern #52 N=3 cross-archetype sub-archetype 3-axis deliberation** (v63 wiki-ship carry-forward)
4. **Pattern #18 Layer 1 sub-archetype consolidation** (v64 — shared-skill-content-with-per-platform-dispatch-file at 5-platform scale)
5. **Pattern #18 Layer 2 NEW sub-archetype** (v64 — solo-author-cross-vendor-parallel-port stale-check)

Stale-checks:
6. NEW Pattern #77 T1 domain-vertical-skill-collection (v67 stale-check window — early check)
7. NEW Pattern #78 Living-Domain-Standards Tracking (v67 stale-check window — early check)
8. Pattern #74 EARS-format / #75 External-IDE-methodology-lineage / #76 Adversarial-review (v63 registrations; v66 = stale-check window)
9. Pattern #52 sustained-velocity test (v69 audit window — Pattern #52 N=3 subjects mattpocock + codex-plugin-cc + karpathy-skills)
10. Pattern #28 credential-tier-progressive-disclosure sub-variant consideration

Observational candidates → top-level deliberation:
11. Manifest-Drift-As-First-Class-CI-Concern (claude-seo v64 strongest evidence)
12. Self-Marketing Release Pipeline Meta-Command (claude-seo `/release-blog`)
13. Gamified-Curated Community Contribution (Pro Hub Challenge v1.9.0)
14. Honest-Deficiency-Disclosure Discipline (claude-seo Limitations + v2 deferrals)

Routine v2.2 codifications (URGENT at v65 window):
15. **29 candidates accumulated** v60+v61+v62+v63+v64 — codify at v65 minimum (was v65-v70 range)

## Cross-wiki sibling decisions

| Sibling | Wiki | Why cross-referenced |
|---|---|---|
| cc-sdd v61 | gotalab N=1 baseline for Pattern #19 ecosystem-portfolio-builder | Direct cross-archetype peer for promotion proposal |
| karpathy-skills v63 | forrestchang N=2 for Pattern #19 | Direct cross-archetype peer |
| mattpocock-skills v57 | T1 general-purpose sub-archetype | Distinguishing peer for NEW Pattern #77 T1 domain-vertical sub-archetype |
| awesome-claude-skills v50 | T1 curated-meta sub-archetype | Distinguishing peer for NEW Pattern #77 |
| agent-skills-of-vercel v51 | T1 corporate-curated sub-archetype | Distinguishing peer for NEW Pattern #77 |
| codex-plugin-cc v62 | Pattern #18 Layer 2 cross-vendor-bridge | Distinguishing peer for v64 NEW Pattern #18 Layer 2 sub-archetype (solo-author parallel-port) |
| oh-my-claudecode v27 + claude-hud v35 | Pattern #59 Claude Code Plugin Marketplace solo-individual | Sub-variant comparison (claude-seo medium-high engagement vs prior smaller-scale) |
| free-claude-code v60 | Pattern #18 Layer 2 api-protocol-translation-proxy | Distinguishing peer for v64 sister-port |
| shannon v45 + aidevops v47 | MCP extension peers | claude-seo extensions architecture (DataForSEO/Firecrawl/Banana MCP) |
| AutoGPT v59 | Pattern #45 Dual-Licensing precedent | claude-seo dual-license MIT + CC BY 4.0 at single-author scale (smaller-scale precedent) |

## Files written at v64

```
/Users/Cvtot/KJ OS Template/03 Projects/claude-seo - Beginner Analysis/
├── CLAUDE.md                                                              (project, Phase 0+1)
├── 01 Analysis/
│   ├── (C) iteration-log.md                                                (this file, Phase 5)
│   └── (C) Pattern-19 ecosystem-portfolio-builder N=3 promotion proposal.md  (Phase 4b)
├── 02 Wiki/
│   ├── index.md                                                            (Phase 2)
│   ├── cluster-1-readme-and-commands.md                                    (Phase 2)
│   ├── cluster-2-architecture-and-skill-system.md                          (Phase 2)
│   ├── cluster-3-ecosystem-and-changelog.md                                (Phase 2)
│   ├── entity-1-claude-seo-core.md                                         (Phase 3)
│   ├── entity-2-ecosystem-portfolio-n3.md                                  (Phase 3 PRIMARY)
│   ├── entity-3-domain-vertical-and-living-standards.md                    (Phase 3)
│   └── entity-4-multi-platform-and-patterns.md                             (Phase 3)
├── 03 Published/
│   └── (C) claude-seo - Huong dan cho nguoi moi.md                         (Phase 4a bilingual)
└── 04 Reviews/                                                              (empty; for future review docs)

Vault state appends (Phase 5):
- /Users/Cvtot/KJ OS Template/_patterns/03-active-candidates.md             (+#77 + #78 NEW candidates)
- /Users/Cvtot/KJ OS Template/_patterns/05-recent-additions.md              (+Post-v64 strengthening notes block)

Vault state pending (Phase 6):
- /Users/Cvtot/KJ OS Template/CLAUDE.md                                     (root state-block update)
- /Users/Cvtot/KJ OS Template/_state/03a-projects-v48-v61.md                (v64 project entry append)
- /Users/Cvtot/KJ OS Template/GOALS.md or _goals/                           (version log if applicable)
```

## Velocity comment

~117 min total wiki-build (Phase 0 → Phase 5 in-progress) = direct-write velocity on-track with v60-v63 range. Direct-write mode preserved; no clusters/entities required re-reading sources during writing. Phase 4b promotion proposal added ~12 min — small overhead for substantial v66 audit prep value.

Subject density was HIGH (claude-seo CHANGELOG 607 lines with multiple version-drift incidents + 43 primitives + 5-product portfolio + 5-platform reach + 8 deprecation events). Higher-than-average source-extraction-to-synthesis transformation — Cluster 3 has unusual amount of CHANGELOG narrative; Entity 4 packages 8 Pattern Library items including 2 NEW + 4 observational.

Next routine v2.1 wiki-build subject benefits from earlier Pattern #19 N=3 promotion-eligible verification (cleaner Phase 0 classification + cleaner Phase 4b routing decision).
