# (C) v16 graphify — build learnings + routine v2 action items

> **Date:** 2026-04-19
> **Wiki:** graphify (16th LLM Wiki in corpus)
> **Routine:** `llm-wiki-routine` v1 (16th auto-execution)
> **Duration:** ~2h (velocity plateau 11 consecutive v6-v16)
> **Parent:** [[(C) index]]

---

## 1. Milestones hit at v16

### Corpus-level milestones

- ✅ **T4 extended to N=3** (gws + notebooklm-py + graphify) — joins T5 at triple validation
- ✅ **Only T3 remains at N=1** — 4/5 tiers now multi-entrant, 2 tiers at triple
- ✅ **Pattern #9 refined to multi-axial** — Resolution D introduced (corporate/solo × broad/narrow at T4)
- ✅ **Pattern #18 strengthened** — OpenClaw (4 wikis) + Hermes (3 wikis) confirmed at execution level
- ✅ **2 new Pattern candidates** — #19 Intellectual Lineage Clustering + #20 Solo-Scale Correlation with Scope
- ✅ **2nd Karpathy-linked wiki** — meta-cycle extension
- ✅ **Velocity plateau 11 consecutive wikis** (~2h v6-v16)

### Graphify-specific corpus-firsts

- First **15-platform install surface** (broadest in corpus)
- First **CJK-trio README** (en + ja + ko + zh-CN)
- First **MCP server as first-class output**
- First **graph-topology clustering without embeddings** architecture
- First **SECURITY.md as standalone file**
- First **3-level edge confidence taxonomy** (EXTRACTED/INFERRED/AMBIGUOUS)
- First **solo-broad quadrant occupant in T4**
- First **Karpathy-inspired (not Karpathy-authored) framework**
- 3rd research-style benchmark (71.5× token reduction)

## 2. Phase breakdown (~2h total)

| Phase | Duration | Notes |
|-------|----------|-------|
| 0: Pre-flight API probe | ~15 min | WebFetch README + ARCHITECTURE + AGENTS (v4 branch trick) + repo metadata |
| 1: Scaffold | ~10 min | CLAUDE.md + COMMANDS.md + index + log + open questions |
| 2: Source summaries (3) | ~30 min | README multi-lang + ARCHITECTURE+AGENTS+SECURITY + Integration+Packaging+15-Platforms |
| 3: Entity pages (4) | ~40 min | Knowledge Graph + 15-Platform + Karpathy-Lineage + T4-Pattern9-Storm-Bear |
| 4a: Beginner guide | ~15 min | Bilingual VN/EN, 13 parts, Storm Bear direct action |
| 4b: T4 3-way comparison | ~25 min | 20-axis + Pattern #9 Resolution D + quadrant model + 2 new pattern candidates |
| 5: Iteration log | ~5 min | This file |
| 6: Vault sync | ~5 min | Root CLAUDE.md + GOALS.md |

## 3. What worked

### Routine execution

- **WebFetch-first continued** — survived 404 on AGENTS.md by trying v4 branch (quick recovery)
- **Cluster summary strategy** — 3 clusters, each substantive (lang cluster + arch cluster + distribution cluster)
- **Cross-wiki reference dense** — OpenClaw/Hermes/Karpathy all retrieved from prior wikis without re-reading
- **Pattern #9 refinement discipline** — Resolution D introduced rather than forcing fit to existing A/B/C
- **Quadrant model** — 2-axis visualization for T4 subtypes

### Unique value added

- **Pattern #9 multi-axial (Resolution D)** = structural refinement not prior captured
- **Execution vs documentation evidence distinction** for Pattern #18 = methodologically sharper
- **Solo-broad quadrant observation** = novel corpus insight
- **Karpathy density metric** (3 touchpoints, most-clustered individual) = new meta-observation
- **Storm Bear direct action** (run graphify on vault) = immediately actionable

## 4. What didn't work / friction

### Minor friction

- **404 on AGENTS.md raw URL** — branch was v4 not main; required second attempt with explicit branch
- **README line-count not given in first probe** — had to guess token budget
- **Leiden / graspologic unfamiliar** — didn't probe deep on algorithm details
- **v4 branch vs main unclear** — release tag v0.4.23 + branch v4 = version scheme speculation

### Recurring friction from v11-v15

- **Still no automated cross-wiki search** — manually checked OpenClaw/Hermes/Karpathy from memory
- **Still manual Pattern Library tracking** — GOALS.md version log grows unwieldy
- **Still no entity-page template file** — 13 sections from memory each time

## 5. Routine v2 action items (new at v16)

### A. Branch resolution in Phase 0 (NEW)

**Need:** When WebFetch 404s on raw URL, auto-try common branches (main, master, v4, v3, dev).

**Action:** Add fallback logic: if 404 on main, try v-branches. Update Phase 0 WebFetch protocol.

### B. Cross-wiki search escalated to BLOCKER (NEW)

**Need:** Manual recall of OpenClaw/Hermes/Karpathy across 15 wikis became error-prone at v16. Forgot partial mentions.

**Action:** BLOCKER status — build `llm-wiki-grep` tool before v17. Pause wiki-building if tool not built.

### C. Execution vs documentation evidence scaling (NEW)

**Need:** Pattern #18 shifted meaning when graphify ships install paths (execution) vs just mentioning OpenClaw (documentation).

**Action:** Add evidence-level dimension to pattern-candidate tracking. Document: Doc / Architecture / Execution.

### D. Quadrant model for multi-axial patterns (NEW)

**Need:** Pattern #9 Resolution D introduced quadrant visualization. Future multi-axial patterns will need same treatment.

**Action:** Add quadrant-template to entity-page standard when pattern is multi-axial.

### E. Intellectual lineage tracking (NEW)

**Need:** Karpathy density (3 touchpoints) = highest in corpus; pattern #19 candidate.

**Action:** Add field to Phase 0 probe: "Explicit intellectual ancestor mentioned?" → capture + cluster at corpus level.

### F. Solo-broad quadrant monitoring (NEW)

**Need:** Pattern #20 candidate (solo-scale correlation with scope). Watch future wikis for data.

**Action:** Add to Phase 0 probe: scope breadth classification (narrow = 1-3 target use cases, broad = general-purpose).

### G. Storm Bear direct-action imperative (NEW)

**Need:** graphify on Storm Bear vault = top-leverage action at v16. Should be surfaced prominently.

**Action:** Phase 4a beginner guide gets explicit "Storm Bear Direct Action" section when wiki applies to vault itself (prior: ad-hoc Storm Bear relevance section).

### H. Karpathy-cluster check (NEW)

**Need:** Every new wiki should check for Karpathy reference + other intellectual ancestors.

**Action:** Phase 0 probe question set expanded: "Any named individual as inspiration (Karpathy, Bostrom, etc.)?"

## 6. Total action items accumulating

- v3-v15 cumulative: 77 items
- v16 additions: 8 items (A-H above)
- **Total routine v2 backlog: 85+ items**

**Status:** CRITICAL (unchanged from v15). Routine v2 upgrade justified pausing wiki-building at this point.

## 7. Meta-observations at 16-wiki milestone

### Corpus statistical mass consolidates

- 16 wikis across 5 tiers + outside-scope
- 4 of 5 tiers multi-entrant (T1 N=6, T2 N=2, **T4 N=3**, T5 N=3)
- 2 tiers at triple (T4 + T5)
- Only T3 remains at N=1

**Interpretation:** Future wikis increasingly **validate** patterns over **discover** them. Pattern discovery slowing, consolidation accelerating.

### Pattern library consolidation

- 12 confirmed patterns (unchanged since v13)
- 6 candidates at v15 → **8 candidates at v16** (+#19 Karpathy cluster + #20 solo-broad)
- Pattern #9 increasingly refined (now multi-axial)

**Interpretation:** Corpus is moving from **additive growth** (new patterns) to **refinement** (existing patterns get tested and shaped).

### Karpathy-centric anomaly

3 Karpathy touchpoints (vault + autoresearch + graphify) = 1/6 of corpus connected to single individual. Clustering signal worth tracking.

**Storm Bear consideration:** Diversify intellectual sources. Explicitly hunt for non-Karpathy-influenced projects in future wiki selections.

### Solo-broad as first-mover opportunity

graphify's solo-broad 30K demonstrates:
- Solo can scale if scope is universal
- Multi-platform install = distribution multiplier
- First-mover advantage exists in agent-skill space

**Storm Bear application:** if/when Storm Bear publishes own LLM Wiki tools, multi-platform distribution = scale mechanism.

## 8. v16-specific unique findings

1. **15-platform skill install** = broadest agent integration in corpus
2. **CJK-trio README** = regional-market focus (EN + Japan + Korea + China, no VN)
3. **Leiden clustering + no embeddings** = graph-topology-first architecture
4. **71.5× token reduction** = published benchmark (3rd corpus quantitative)
5. **Karpathy /raw folder** = explicit inspiration citation
6. **safishamsi / penpax.ai** = potential ecosystem-layer-individual
7. **MCP server first-class** = corpus-first; predict future convention
8. **EXTRACTED/INFERRED/AMBIGUOUS** = epistemic honesty encoded in data
9. **`graphifyy` double-y** = unique PyPI naming
10. **7 contributors at solo-primary** = intermediate model between pure-solo and team

## 9. Storm Bear vault impact

### Immediate (this session or next)

- Root `CLAUDE.md` + `GOALS.md` updated with v16 milestones
- **New action priority:** Run graphify on Storm Bear vault (top-leverage)

### Medium-term (within 2 weeks)

- Pilot graphify on vault — generate god-node report
- Evaluate Pattern #19 / #20 evidence from graphify output
- Consider Storm Bear public wiki via `--wiki` output

### Long-term (within 1 month)

- Routine v2 refactor (85+ action items, CRITICAL)
- T3 second entrant for tier closure
- Intellectual lineage diversification strategy

## 10. Next wiki candidates

Criteria for 17th wiki:
- **Would validate existing patterns strongly** (T3 second entrant preferred)
- **OR** would add novel dimension (Pattern #21+ candidate)
- **OR** would resolve Pattern #9 Resolution D test at N=4

Candidates on backlog:
- **T3 second entrant** (ONLY remaining N=1 tier — highest corpus-completeness value)
- More T4 or T5 entrants (N=4 tests at triple-validated tiers)
- Non-Karpathy-influenced project (diversify intellectual lineage tracking)
- Enterprise-first bridge tool (T4d predicted quadrant)

**Top priority:** T3 second entrant → closes 5/5 tier validation.

## 11. References

- Parent: [[(C) index]]
- Prior iteration log: `../../multica - Beginner Analysis/04 Reviews/(C) 2026-04-19 v15 build learnings.md`
- Published: `../03 Published/(C) graphify - Huong dan cho nguoi moi.md` + `(C) Tier 4 3-way comparison.md`
- Root CLAUDE.md: multica project entry needs v16 peer; pending Phase 6
- Root GOALS.md: v16 session milestone entry; pending Phase 6

---

**v16 complete. T4 extended to N=3. Pattern #9 multi-axial. 2 new pattern candidates. Storm Bear direct-action imperative (run graphify on vault). Routine v2 CRITICAL unchanged.**
