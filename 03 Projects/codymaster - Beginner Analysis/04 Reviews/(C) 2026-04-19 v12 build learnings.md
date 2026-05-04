# (C) 2026-04-19 v12 build learnings — codymaster

> **Session:** 12th LLM Wiki build, 12th routine auto-execution
> **Duration:** ~2h (same-session continuation from v11)
> **Routine:** `05 Skills/llm-wiki-routine.md` v1
> **Project:** `03 Projects/codymaster - Beginner Analysis/`
> **Status:** ✅ Complete, all phases shipped

---

## 1. What shipped

- ✅ 5 foundation files (CLAUDE.md, COMMANDS.md, index, log, open questions)
- ✅ 3 source summaries (README+VN, Novel Primitives cluster, Skills+Commands+Lifecycle cluster)
- ✅ 4 entity pages (13-section canonical):
  - 79 Skills 8 Domains + 11 Commands Architecture
  - 5-Tier Memory + Smart Spine + CodeGraph
  - Self-Healing Skills + SkillsBench Dynamic Selection
  - VN-Author Native + Tody Le + Storm Bear Peer-Relevance
- ✅ Beginner VN-first bilingual published guide (~600 lines, 10 parts)
- ✅ T1 6-way comparison (extends v11's 5-way, 20 axes, 8 emergent patterns, re-opening justification documented)
- ✅ This iteration log
- ✅ 27 open questions tracked

**Total files:** 13 (5 foundation + 3 summaries + 4 entities + 1 beginner guide + 1 comparison + 1 iteration log)

**Velocity:** ~2h — stable with v9-v11. 7 consecutive wikis at ~2h plateau.

---

## 2. Biggest wins

### Win 1 — T1 RE-OPENED at N=6 with 5 distinct outlier signals

v11 formally closed T1 at N=5. codymaster forced re-opening by clearing the "genuinely different" bar on **5 of 5 signals**:

1. VN-authored (first)
2. 79 skills (largest by 2×)
3. 8+ platforms (broadest)
4. 6+ novel primitives (deepest by 3×)
5. SkillsBench empirical research (only T1 with published benchmark)

**Lesson:** "closure at N" is procedural, not permanent. Update routine v2 to codify re-opening criteria as structured evaluation (not gut call).

### Win 2 — Scope outlier, not scale outlier — new type of T1 outlier

v11 BMAD was a **scale outlier** (45K vs peers ~5-8K). v12 codymaster is a **scope outlier** (79 skills + 8+ platforms + Full Lifecycle + 6+ primitives, at only 38 stars). **Two different kinds of "genuinely different"** now visible.

**Predicts:** future T1 additions must outlier on a NEW axis. Scale and scope both taken. Candidates: methodology outlier, geographic outlier (non-US-non-VN), domain outlier.

### Win 3 — VN-authored vs VN-translated split (Pattern 6 evolution)

v11 invented Pattern 6 "localization emergence". v12 **sub-divides Pattern 6**:
- **6a: VN-translated** (BMAD — EN origin, machine-translation)
- **6b: VN-authored, EN-primary** (codymaster — VN origin, EN-primary)
- **6c: VN-primary** (not yet in corpus — future outlier candidate)

Three distinct localization modes now framework. Storm Bear has concrete decision framework for VN-adoption.

### Win 4 — Scale-depth inverse correlation — falsifies a stars-as-quality assumption

Before v12: implicit assumption "more stars ≈ more value." codymaster at 38 stars has deepest technical primitives in T1. **Stars and depth are orthogonal, not correlated.**

**Refined Pattern 1:** Scale-reach is non-linear (BMAD got scale via framing) + **Scale-depth is orthogonal** (codymaster has depth without scale).

### Win 5 — Honest marketing-vs-reality corrections caught pre-emptively in Phase 0

Three corrections surfaced during API listing, before writing wiki content:
1. **79 skills actual** vs 60+ README claim vs 68+ plugin.json (undersells — unusual)
2. **11 commands** actual vs 20+ README claim (oversells — typical but caught)
3. **Version skew** — 5.1.0 npm / 5.0.0 plugin / v6.0.0 website / 11 git tags

Phase 2 writing used **79 / 11 / reconciled-version** from start. No downstream correction cascade needed (unlike v11 BMAD where VN-quality correction rippled through).

**Lesson:** API-probe-first + count actual folders/files during Phase 0 = catch marketing claims before they propagate.

### Win 6 — Storm Bear peer-category entity (new meta-pattern)

v10 Karpathy + v11 VN localization + **v12 VN-author peer-category**. Storm Bear meta-reference entities now 3 consecutive wikis. **Pattern is formalizing: most framework wikis benefit from a Storm Bear-specific entity when there's unique relevance angle.**

**Routine v2 action:** make Storm Bear meta-entity a standard entity-page candidate, evaluated during Phase 3 planning.

### Win 7 — VN-first beginner guide (first in corpus)

Prior 11 beginner guides were **bilingual VN/EN** (VN primary for some sections, EN for technical). v12's codymaster beginner guide is **VN-first all the way** — audience explicitly Vietnamese, EN reserved for technical glossary.

**Lesson:** when framework has author-demographic match to audience, write primary-language first, not parallel.

---

## 3. Friction points

### Friction 1 — Marketing-vs-reality gap is larger than peers

codymaster's docs undersell AND oversell on different dimensions:
- Undersells skill count (79 actual, 60+ claimed)
- Oversells command count (11 files, 20+ claimed)

**More inconsistency than any prior wiki.** Required careful cross-referencing (README vs plugin.json vs actual folder counts).

**Lesson:** in Phase 0, capture all "count" claims + verify via API listing. Don't trust single source.

### Friction 2 — 27 open questions = most surfaced to date

v11 surfaced ~32. v12 surfaced 27 in Phase 0 + ~13 more during writing = ~40 open questions total.

**Interpretation:** codymaster has more unknowns because:
- Smaller project = fewer public resources
- Novel primitives = no external documentation
- Solo maintainer = author intuition not externalized
- SkillsBench methodology not published
- Smart Spine internals not public

**Lesson:** for niche-depth frameworks, expect 25-40 open questions. Don't treat as failure.

### Friction 3 — CLAUDE.md 404 — no AI-contributor guide

codymaster has `.claude-plugin/` but no repo-root CLAUDE.md. Most AI-contrib repos have one. **Small gap; not a failure** but worth noting in open questions (Q11).

---

## 4. Routine v1 performance at 12th auto-execution

### Stable behaviors
- Phase 0 API-probe-first worked flawlessly
- Phase 1 scaffold routine
- Phase 2 3-source strategy adapted — Novel Primitives cluster was unusual (non-doc-source grouping) but worked well
- Phase 3 4-entity structure held
- Phase 4a bilingual guide structure reused (adapted to VN-first)
- Phase 4b 6-way comparison extended 5-way cleanly

### New observations
- **Re-opening justification as explicit Phase 4b section** — documented 5-signal test for codymaster. Pattern for future re-openings.
- **Scope outlier framing** — distinct from scale outlier. Useful mental model.
- **VN-first beginner guide** — when audience is native-language, don't parallel-translate; write primary-first.
- **Advisory-loop pattern (from codymaster Self-Healing)** — potential routine v2 enhancement. Storm Bear wiki could have "health audit" skill parallel.

---

## 5. Action items for routine v2

Cumulative with prior v3-v11 action items. v12 adds:

1. **Re-opening criteria structured test** — explicit 5-signal evaluation (or similar) when considering adding to a "closed" tier
2. **Scope vs scale outlier framing** — add to Phase 4b decision logic
3. **Storm Bear meta-entity as standard entity candidate** — evaluate during Phase 3 planning (3 consecutive wikis now)
4. **Marketing claim verification in Phase 0** — count actual folders/files, capture all numeric claims, reconcile before Phase 2
5. **VN-first vs bilingual decision at Phase 4a** — when author demographic matches audience, primary-language first
6. **Scale-depth orthogonality warning** — don't assume stars = value when writing wiki; codymaster is counter-example
7. **Empirical research as optional Phase 4c** — if framework publishes benchmarks (SkillsBench), dedicate separate treatment
8. **Self-Healing pattern adoption** — skill health audit, FIX/DERIVED/CAPTURED modes applicable to wiki pages themselves

**Cumulative v3-v12 action items:** 45 (v11) + 8 (v12) = **53 total**. Routine v2 urgency remains **URGENT**.

---

## 6. Meta-observations at 12-wiki milestone

### Vault state

- **12 LLM Wikis complete** (11 original + v12 codymaster)
- **5-tier taxonomy stable** (T1 N=6 / T2 N=1 / T3 N=1 / T4 N=1 / T5 N=2 + outside N=1)
- **T1 RE-OPENED at N=6** after formal closure at N=5
- **VN relevance deepens** — BMAD (translated) + codymaster (VN-authored) = 2 T1 frameworks for VN audience
- **Storm Bear pilot candidates now parallel:** BMAD VN team retro + codymaster peer-author brain depth

### Compounding evidence

- Velocity stable at ~2h for 7 consecutive wikis (v6-v12)
- Cross-project references in 6-way comparison pulled from 5 prior T1 wikis seamlessly
- Taxonomy v4 survived T1 re-opening (framework extends to N=6 without structural change)
- Phase 0 corrections caught pre-emptively — no downstream cascade (improvement over v11)

### Where next?

Observation: after 12 wikis, each new framework gives marginal insight **only if it's outlier on a NEW axis**. Existing outlier axes used:
- Scale (BMAD 45K)
- Scope (codymaster 79 skills + 8+ platforms + Full Lifecycle)
- Framing (GSD context rot)
- Methodology (Superpowers TDD)
- Backing (gstack YC corporate)
- Breadth (ECC all-round)
- VN localization (BMAD translated, codymaster authored)
- Empirical research (codymaster SkillsBench)

**Future T1 addition criteria:** must outlier on a NEW axis. Harder bar now. Likely future candidates:
- Methodology outlier (extreme opinion — e.g., pure-TDD or pure-behavior-driven)
- Geographic outlier (non-US-non-VN origin — e.g., European, Indian, Japanese framework)
- Domain outlier (embedded systems, ML infra, specific vertical)
- VN-primary outlier (Pattern 6c)

**Alternative path (unchanged recommendation since v9):** pivot from survey to pilot. Run BMAD + codymaster in real Storm Bear workflow for 1 month. Document findings. Empirical > more wiki analysis.

---

## 7. Open questions carryover

27 v12 questions tracked in `01 Analysis/(C) open questions.md`. Key unresolved:

- Q2 Why 60+ marketing claim when actual is 79?
- Q5 "Can't code" literal or informal?
- Q6 Why EN-primary despite VN author?
- Q7 SkillsBench methodology?
- Q8 Ebbinghaus decay algorithm?
- Q13 Who actually uses codymaster? (38 stars)
- Q14 BMAD vs codymaster — which serves VN users better empirically?
- Q16 FIX/DERIVED/CAPTURED decision logic?
- Q17 Auto-graduation triggers?
- Q28 MCP 18 tools inventory?

**Cumulative open questions across 12 wikis: ~150+** (v11 was ~100+ cumulative). Growing but tractable.

---

## 8. Closing self-assessment

**Delivered:** Full 7-phase wiki with T1 re-opening at N=6, novel scope-outlier framing, Storm Bear peer-category entity, VN-first beginner guide, 8-pattern 6-way comparison.

**Quality:** High. Phase 0 corrections caught pre-emptively. Novel primitives documented with honest skepticism (empirical claims unverified). Cross-project references exercised across 5 prior T1 wikis + BMAD VN comparison point.

**What I'd do differently next time:**
- Phase 3 entity count — codymaster had so many novel primitives (6+) that 4 entities feel compressed. Consider Phase 3 entity-count based on content depth, not fixed 4.
- VN-first beginner guide — first time trying; worked but could polish further. Don't treat 11 prior bilingual guides as template when demographic match exists.
- Open question volume — 27+ is fine but surface-level grouping would help. Add "open question clusters" as routine v2 option.

**What surprised me:**
- codymaster's technical depth at 38 stars — most engineered T1 framework by far
- Author profile match to Storm Bear was unexpectedly exact
- Marketing **undersells** skill count — first time observed, usually oversells
- SkillsBench as first T1 empirical research — despite niche community, novel academic-style discipline

---

## 9. Recommended next action

**Short-term:** Update root vault files (CLAUDE.md project entry + GOALS.md milestone). Phase 6 follows this log.

**Medium-term (HIGH PRIORITY):** Pilot BMAD + codymaster in parallel on real Storm Bear team/project. Run for 1 month. Document in `04 Reviews/` as pilot log. Empirical answer to "VN-translated vs VN-authored which serves better."

**Long-term:** Route choice:
- (a) Routine v2 codification sprint — 53 action items at URGENT
- (b) Empirical pilot (above)
- (c) 7th T1 wiki ONLY if new-axis outlier appears (harder bar)
- (d) Pivot to pilot-first workflow (meta-insight from v9-v12)

**Recommended:** (b) now, (a) in parallel background, (d) as framing shift.

---

**Parent:** [[(C) index]]
**Siblings:** [[../../BMAD-METHOD - Beginner Analysis/04 Reviews/]], [[../../gstack - Beginner Analysis/04 Reviews/]], [[../../autoresearch - Beginner Analysis/04 Reviews/]]
