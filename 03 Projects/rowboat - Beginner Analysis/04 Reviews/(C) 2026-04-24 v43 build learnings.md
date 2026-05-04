# (C) 2026-04-24 v43 build learnings — rowboat

**Wiki #:** 43 (Storm Bear corpus)
**Routine:** v2.1 (7th v2.1-era execution; 6th + consecutive at YELLOW primitive-count discipline)
**Source:** https://github.com/rowboatlabs/rowboat
**Velocity:** ~2h 30min YELLOW (preserves plateau)

---

## 1. Milestones hit (corpus-level + framework-specific)

**Corpus-level:**

- ✅ **T5 extends to N=8** with 100% archetype-diversity preserved (8 distinct organizational archetypes + 8 distinct product-domain sub-archetypes)
- ✅ **NEW T5 sub-archetype: personal-productivity-application** (distinct from research/ML/orchestration/browser/SWE/education domains)
- ✅ **7-streak zero-registration preserved** (v37-v43 = 7 consecutive wikis with 0 new active pattern candidates) — longest in corpus history
- ✅ **Ratio 0.54:1 UNPRECEDENTED preserved** from post-v42-deferred mini-audit baseline (0.41 buffer below 0.95:1 trigger)
- ✅ **32 consecutive wikis at ~2h velocity plateau** (v6-v43); 2nd YELLOW primitive-count wiki after pi-mono v36 without velocity degradation
- ✅ **32nd consecutive Storm Bear meta-entity** (v10-v43)
- ✅ **7th v2.1-era routine execution** — all 5 discipline mechanisms exercised cleanly (overlap pre-check, un-stale, counter-evidence, consolidation-forward, N=1 stale-risk)

**Framework-specific:**

- ✅ **YC S24 batch explicit project-level README badge** — corpus-first in 43 wikis
- ✅ **Knowledge-graph-as-Markdown explicitly Obsidian-compatible at T5** — most-direct Storm Bear peer-category match in 43 wikis
- ✅ **Implicit Karpathy structural parallel at T5** — 7th+ Pattern #19 archetype 1 touchpoint; corpus-first implicit-not-explicit
- ✅ **Track Blocks corpus-first architecture** — YAML-fenced + HTML-comment-region + 4 trigger types + 2-pass LLM classifier + single-writer invariant
- ✅ **4-OSS-surface distribution at T5** (desktop binary + Docker + npm + PyPI, all Apache-2.0) — corpus-first
- ✅ **Apache-2.0 at T5** — first in 8 T5 entrants (prior 7 used MIT or AGPL variants)
- ✅ **Product-pivot-in-monorepo** observed (legacy SaaS `apps/rowboat` + new Electron flagship `apps/x` coexist)
- ✅ **7-surface commercial-funnel** ties ruflo v42 for corpus-most-elaborate

## 2. Phase breakdown (duration per phase)

| Phase | Duration | Notes |
|---|---|---|
| 0 Pre-flight | ~20 min | 12-axis classification + pattern pre-check + primitive-count YELLOW probe |
| 1 Scaffold | ~10 min | 8 subfolders + CLAUDE.md + COMMANDS.md + index/log/open-questions |
| 2 Sources | ~35 min | 3 cluster summaries (User-facing / Architecture / Commercial-ecosystem) |
| 3 Entities | ~45 min | 4 entity pages (Core / Architecture / T5-sub-archetype + Storm Bear peer / 32nd meta) |
| 4a Beginner guide | ~15 min | Bilingual VN+EN ~480 lines, 12 parts, HIGH Storm Bear pilot framing |
| 4b Phase deliverable | ~25 min | T5 8-way + personal-productivity-application + Storm Bear direct-peer-category ~700 lines |
| 5 Iteration log | ~10 min | This document |
| 6 Vault sync | ~15 min | Root CLAUDE.md + PATTERN_LIBRARY.md state block |

**Total:** ~2h 30min (YELLOW). Preserves plateau.

## 3. What worked

- **YELLOW primitive-count discipline validated 2nd time** — pi-mono v36 introduced YELLOW; rowboat v43 confirms ~30-50 primitives fits 4-entity format with strategic compression. Velocity preserved at ~2h 30min.
- **Consolidation-forward discipline 7th consecutive successful application** — all candidate observations routed to within-pattern strengthening or OBSERVATION-TRACK avoidance. 0 new active candidates.
- **Implicit-Karpathy-touchpoint observation surfaced cleanly** — recognized as within-Pattern-#19 strengthening rather than new pattern registration. Disciplined.
- **Storm Bear direct-peer-category framing** — rowboat is the corpus mirror; framing reveals empirical-test thesis for LLM Wiki pattern viability.
- **WebFetch-first probe** retrieved stars/forks/age cleanly. GitHub API via WebFetch worked for metadata.
- **Dual-product observation** — recognized `apps/rowboat` legacy + `apps/x` new flagship coexistence as product-pivot-in-monorepo (corpus-first). Routed to within-Pattern-#58 observational watch (not standalone registration).
- **Track Blocks deep-dive** — TRACKS.md 26KB single-feature doc yielded 10+ corpus-first architectural observations cleanly.

## 4. What didn't work / friction

- **Rowboatlabs.com + /downloads** WebFetch returned minimal content — landing page is minimal HTML, no paid-tier info, no team info. Had to infer commercial model from code (`billing/` subsystem + Auth0 legacy).
- **GitHub API topic fields** required 2 separate WebFetch calls (repo page first, then api.github.com direct) to get exact numeric stars/forks. Minor inefficiency.
- **No single file to confirm team composition** — Ramnique Singh surfaced via PyPI pyproject.toml metadata (not README or docs/team.md). Standard for YC-stage startups but friction for corpus researcher.
- **Triple-package divergence** ambiguity — `@rowboatlabs/rowboatx` npm v0.16.0 vs `apps/rowboat/` legacy vs `apps/x/` Electron flagship. Unclear which is "current product" without reading multiple sources. Disambiguation required ~20 min of source-probing.
- **Primitive-count probe YELLOW discipline** — still informal (not codified in routine v2.1). Relied on heuristic judgment. Routine v2.2 candidate for formalization (defer to ~v45-v50 natural cadence).

## 5. Routine v2.1 action items (for v2.2 consideration)

1. **YELLOW primitive-count discipline formalization** — 2nd successful application (v36 + v43). Consider codifying trigger (~5-6 primitives = YELLOW threshold) for v2.2.
2. **Implicit-vs-explicit citation sub-classification** — Pattern #19 archetype 1 could gain sub-a (explicit-citation) + sub-b (implicit-structural-parallel) sub-classifications. Wait for N=2 on implicit-parallel before formalizing.
3. **Dual-product-in-monorepo observation** — Pattern #58 3rd data point watch. When 3rd structurally-distinct observation (product-pivot-variant, vs 58a rename-variant + 58b transitional-preserve-variant), consider refinement.
4. **Open-core sub-classification 31c undeclared-monetization** — v43 adds 2nd data point (after ruflo v42). If 3rd data point emerges, consider formal sub-classification within Pattern #31.
5. **YC-batch explicit project-level acknowledgment** — v43 first observation. Stale-flag tracking after v48 if no 2nd YC-batch project observation.
6. **4-OSS-surface distribution at T5** — corpus-first observation. Watch for 2nd T5 with 4+ OSS-only surfaces; could refine Pattern #2 Distribution Evolution.
7. **Karpathy lineage cluster N=7+ touchpoints** — suggests Pattern #19 archetype 1 may warrant sub-cluster-specific formal-statement formalization (vs broader archetype 1 = "individual-author-lineage" current). Consider for v2.2 if Karpathy-specific touchpoints continue accruing.
8. **Standardized config-format discipline** (rowboat's `{ "apiKey": "<key>" }`) — observational pattern in rowboat; watch for 2nd data point across integrations.

**Total cumulative action items v3-v43:** ~250+ (previously ~245 post-v42 mini-audit consolidation cycles; +8 at v43 v2.2 candidates).

## 6. Meta-observations

- **7-streak zero-registration** is unprecedented. Discipline mechanism (consolidation-forward + overlap pre-check + N=1 stale-risk flagging) demonstrates sustainability. Corpus discovery phase appears to be converging on strengthening-over-discovering mode at v43.
- **Corpus mirror milestone:** Rowboat v43 is structurally what Storm Bear vault is. No prior wiki had this direct parallel. Suggests corpus at v43 is mature enough to recognize peer-category products as structural equivalents.
- **Karpathy lineage cluster at 7+ touchpoints** makes Karpathy the most-clustered individual influence node in corpus. If pattern continues (Storm Bear bet on LLM Wiki works → more Karpathy-influenced products emerge → more wikis cite/parallel Karpathy), archetype 1 may warrant Karpathy-specific-sub-formalization.
- **Ratio 0.54:1 UNPRECEDENTED preserved** — 7-streak discipline + 2 mini-audits since v36 (v36 mini-audit + v42 mini-audit + v42-deferred mini-audit all within 72h window) produce unmatched library health.
- **YELLOW primitive-count** is sustainable mode — 2 consecutive YELLOW wikis (pi-mono v36 + rowboat v43) + velocity preserved suggests ~30-200 primitives = routine-manageable via strategic compression.

## 7. Unique findings (corpus-firsts)

15 corpus-firsts documented:

| # | Corpus-first |
|---|---|
| 1 | YC S24 batch project-level README badge (first in 43 wikis) |
| 2 | `claude-cowork` repo topic identity signal |
| 3 | Triple-package commercial product distribution (3 different registries) |
| 4 | 4-surface OSS-only commercial T5 distribution |
| 5 | Product-pivot-in-progress observable in single monorepo |
| 6 | 7-surface commercial-funnel (ties ruflo v42) |
| 7 | Apache-2.0 at T5 (first in 8 T5 entrants) |
| 8 | Track Blocks: YAML-fenced live-updating notes with 4 trigger types + 2-pass classifier |
| 9 | Single-writer invariant explicit discipline |
| 10 | Hybrid mtime+hash change detection documented technique |
| 11 | Auto-generated Copilot skill schema from Zod source-of-truth |
| 12 | esbuild-bundle-for-Electron-Forge-symlink-workaround documented technique |
| 13 | 22-subsystem core-package architectural decomposition at T5 |
| 14 | Implicit-not-explicit Karpathy structural parallel (within-Pattern-#19) |
| 15 | Personal-productivity-application T5 sub-archetype (NEW definition at v43) |

## 8. Storm Bear vault impact

**Pilot ranking update: rowboat v43 = NEW #1** (displaces claude-hud v35).

**Rationale:**
- Most-direct peer-category match in 43 wikis (knowledge-graph-as-Markdown)
- Empirical test of LLM Wiki pattern viability thesis
- Zero-commitment evaluation (Apache-2.0, 5-min install, uninstallable)
- Non-disruptive testing (fresh test vault, not Storm Bear primary)
- 4-week structured pilot protocol documented

**Actions spawned:**

1. **HIGH:** 1-4 week rowboat pilot with 4-week protocol (documented in beginner guide + Phase 4b deliverable)
2. **MEDIUM:** Adapt Track Blocks YAML-fenced-region convention manually in Storm Bear vault (usable without adopting rowboat)
3. **LOW:** Consider standardized config format `{ "apiKey": "<key>" }` for Storm Bear skills
4. **LOW:** Document single-writer invariant for PATTERN_LIBRARY.md operations

**⚠️ v27 diagnostic HIGH bundle status:** **21 sessions deferred** (v28 + v29 + v30 + v31 + v31-mini + v32 + v32-mini + v33 + v34 + v34-action + v35 + v36 + v36-mini + v37 + v38 + v39 + v40 + v41 + v42 + v42-mini + v42-deferred + v43). BLOCKING-RECOMMENDATION critical threshold exceeded 4× per v2.1 operator-facing backlog discipline.

**Rowboat pilot could integrate with diagnostic-HIGH item #1 vault CLAUDE.md refactor** if pilot outcome favorable (AI-maintainer augmentation integrated into vault workflow). If pilot unfavorable: diagnostic-HIGH proceeds with human-maintainer discipline unchanged.

## 9. Next wiki candidates (strategic selection for pattern-strengthening)

**Strengthening-priority-ordered:**

1. **Mem0 / Letta / Khoj / Reor** (personal-productivity-application sub-archetype N=2 → potential promotion under Criterion 2 structural-N=2)
2. **Another YC-batch project** (YC-S24-batch sub-observation N=2 → potential Pattern #17 variant-within-pattern refinement)
3. **Another implicit-Karpathy-structural-parallel** (Pattern #19 archetype 1 sub-b sub-classification promotion candidate)
4. **Another T5 with 4+ OSS-only surfaces** (Pattern #2 Distribution Evolution T5-refinement candidate)
5. **Another dual-product-in-monorepo** (Pattern #58 3rd data point watch)

**Storm Bear-internal-priority (vs external wiki):**
- **Rowboat pilot** (4-week protocol) before v44 — highest-leverage single Storm Bear action at v43
- v27 diagnostic HIGH bundle execution (21 sessions deferred) — BLOCKING-RECOMMENDATION

## 10. Strategic decision point

**Corpus at v43 in strong state:**
- 7-streak zero-registration (unprecedented)
- Ratio 0.54:1 UNPRECEDENTED
- 32 consecutive velocity-plateau wikis
- 5/5 tier validation preserved since v26
- Pattern Library health excellent

**However, v27 diagnostic HIGH bundle 21-sessions-deferred is concerning.** Per v2.1 operator-facing backlog discipline, escalated to BLOCKING-RECOMMENDATION.

**Recommendation for operator decision before v44:**

**Option A:** Execute rowboat pilot Week 1 (2-4h) — HIGH-leverage single action; reveals whether AI-maintainer augments Storm Bear vault workflow
**Option B:** Execute v27 diagnostic HIGH bundle item #1 (vault CLAUDE.md refactor) — LONG-overdue operator-facing action
**Option C:** Execute Options A + B hybrid — rowboat pilot + vault refactor integrated if pilot favorable
**Option D:** Continue wiki production (v44+) with current discipline — pattern-strengthening mode sustainable but operator-action-backlog continues accumulating

**Strongly recommend Option A or C.** Option A alone produces empirical data that informs Option B timing (whether to integrate AI-maintainer layer in vault refactor).

## 11. Scorecard

| Dimension | Score | Note |
|---|---|---|
| Novelty | 9/10 | 15 corpus-firsts + new T5 sub-archetype + corpus mirror milestone |
| Pilot-relevance | 10/10 | HIGH #1 pilot ranking; direct peer-category; empirical test pathway |
| Pattern-contribution | 8/10 | 10+ strengthening + 1 observational refinement (Pattern #19 implicit); 0 new candidates (7-streak) |
| Velocity | 9/10 | ~2h 30min YELLOW preserves plateau (2nd YELLOW validation) |
| Quality | 9/10 | 13 deliverables + cross-references consistent + fact-verification clean |

**Overall: 9.0/10** — HIGH-quality wiki with HIGH-strategic-value pilot outcome.

## 12. Primitive-count check (v2.1 informal discipline)

- **Probed primitive-count:** ~30-50 across monorepo (7 apps + 22 core subsystems + 35 knowledge modules + 4 Track trigger types + 6+ integrations + 5 specialized agents)
- **Fits 4-entity format cleanly?** Partial (YELLOW; strategic compression applied)
- **Strategic compression decisions:**
  - Entity 1: Core product (rowboat knowledge-graph + Track Blocks + voice + integrations combined)
  - Entity 2: Architecture + Distribution (dual-product-monorepo + 4-surface combined)
  - Entity 3: T5 8-way + Storm Bear peer (combined — 3 routing modes into 1 entity)
  - Entity 4: 32nd Storm Bear meta-entity (Karpathy implicit-touchpoint)
- **Lossy compression accepted:**
  - apps/rowboat legacy SaaS covered briefly in Entity 2 (not separate entity)
  - apps/cli + apps/docs + apps/experimental cited not enumerated
  - apps/rowboatx CLI specifics cited not deeply explored
  - Chrome extension + Granola integration subdirs mentioned not probed
  - knowledge/ subsystem 35-module list enumerated but most modules not deeply read
- **Follow-up deep-dive wikis candidates:**
  - `Rowboat - Track Blocks architecture deep-dive` (26KB TRACKS.md worthy of dedicated wiki if strategic-value emerges)
  - `Rowboat - Dual-product-in-monorepo case study` (product-pivot observation)
- **Operator decision:** Ship with compression; defer follow-up wikis unless rowboat pilot outcome motivates deeper analysis
- **Velocity overhead measured:** ~2h 30min (vs ~2h GREEN baseline) = 25% overhead within YELLOW expectation

## 13. Summary for root CLAUDE.md update

**v43 ships:**
- T5 extends to N=8 with personal-productivity-application sub-archetype (NEW)
- 0 new active candidates (7-streak unprecedented preserved)
- 10+ pattern strengthening data points including implicit-Karpathy-touchpoint observation
- Ratio 0.54:1 UNPRECEDENTED preserved
- 32 consecutive velocity-plateau wikis
- 32nd consecutive Storm Bear meta-entity
- Rowboat = NEW #1 Storm Bear pilot (direct peer-category)
- 15 corpus-firsts documented
- YELLOW primitive-count 2nd successful application

**Strategic ask:** Operator decision before v44 on Option A (rowboat pilot) / Option B (v27 diagnostic) / Option C (hybrid).
