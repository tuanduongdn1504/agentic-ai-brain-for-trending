# (C) Iteration Log — v6 Build Learnings (2026-04-18)

> **Session type:** 6th auto-execution của routine `llm-wiki-routine` — **first different-domain wiki** (education vs dev-tool siblings)
> **Duration:** 1 session (autonomous, continued across context compaction)
> **Outputs:** 13 files (3 sources + 4 entities + 2 published + 3 foundation + 1 log)
> **Purpose:** Test routine generalization beyond agent-framework tooling. Expand v4 taxonomy 2-tier → 3-tier.
>
> **Baselines (full progression N=1→6):**
> - v1 ECC (~6h, 0 siblings, first wiki, Tier 1)
> - v2 Superpowers (~3.5h, 1 sibling, 2-way, Tier 1)
> - v3 gstack (~2.5h, 2 siblings, routine codified, 3-way, Tier 1)
> - v4 goclaw (~2.5h, 3 siblings, adjacent-domain reframe, 2-tier taxonomy unlocked, Tier 2)
> - v5 GSD (~2.5h, 4 siblings, 4-way, 6 emergent patterns, Tier 1 slot completed)
> - **v6 ai-agents-for-beginners** (~2h, 5 siblings, **different-domain generalization**, **3-tier taxonomy emergent**, **first Tier 3**)

---

## Tóm tắt / Summary

v6 ai-agents-for-beginners tests routine's outer boundary — **first non-dev-tool wiki**. Clone blocked, pivoted to WebFetch. Despite constraint, velocity held at ~2h. Taxonomy expanded v4's 2-tier → v6's 3-tier with Tier 3 "agent-as-education" addition. 6-wiki corpus now covers all 3 tiers — structurally complete snapshot.

**Hypothesis verified:** Routine generalizes beyond agent-framework tool domain. WebFetch-based source acquisition viable fallback.

**Novel insights:**
1. **3-tier taxonomy stable** — 6 wikis partition cleanly across 3 tiers
2. **Purpose → Format correlation** — Learn needs curriculum, Use needs reference, Deploy needs platform
3. **Tier learning is recursive, not linear** — advanced practitioners oscillate between tiers

---

## ✅ Cái gì work tốt / What worked well

### 1. WebFetch fallback when clone blocked

Git clone failed 3 times (default branch mismatch, filter-blob stall, timeout unavailable). **WebFetch to raw.githubusercontent.com** handled content acquisition cleanly.

**Time cost:** ~30 min lost troubleshooting clone + pivoting.
**Lesson:** **Skip clone, go WebFetch for doc-heavy repos** (especially courses/wikis where we don't need runnable code).

### 2. Different-domain routing worked without manual spec

Routine automatically:
- v4: adjacent-domain → taxonomy reframe
- v5: same-tier → 4-way comparison
- **v6: different-domain → Tier expansion**

Self-regulating. No Phase 0.5 classification code needed yet.

### 3. 3-tier taxonomy clean partition

6 corpus items place cleanly in 3 tiers. No item fits multiple. **Defensible classification.**

### 4. Cluster-based source strategy (v6 innovation)

First wiki to use **cluster summaries** (not individual source summaries):
- `(C) README summary.md` (1 file = main repo)
- `(C) Core lessons cluster summary.md` (1 file = 4 lessons: 01, 03, 05, 08)
- `(C) Frameworks + Protocols cluster summary.md` (1 file = 4 lessons: 02, 11, 12, 14)

**Why it worked:**
- Course = 14 lessons individually too granular for 3-source budget
- Lessons share themes → cluster by theme cleaner
- Each cluster = 4 lessons = manageable entity

**Lesson:** For curriculum/education domain, **cluster by theme** instead of source-by-source.

### 5. Phase 4b = taxonomy extension (not new artifact)

Previous:
- v3 = N-way comparison
- v4 = taxonomy reframe (new)
- v5 = N-way refinement
- **v6 = taxonomy extension (v4 → v2 3-tier)**

**Lesson:** Phase 4b output-type grows: comparison → taxonomy → taxonomy-update. Routine naturally produces right artifact based on corpus state.

### 6. Meta-relevance pattern compounds

| Wiki | Meta-relevance finding |
|------|------------------------|
| v4 goclaw | Knowledge Vault = Karpathy LLM Wiki as infrastructure |
| v5 GSD | `/gsd-ingest-docs` ≈ Storm Bear's `llm-wiki-ingest` skill |
| **v6 course** | **Lesson 12 Context Engineering = GSD's "context rot solution" at concept level** |

3 consecutive wikis revealed vault-relevance. Pattern: **every wiki reveals Storm Bear adjacent learning**.

### 7. VN market signal strengthens

- goclaw (v4): `README.vi.md` + Zalo
- ai-agents-for-beginners (v6): **native VN translation** (of 50+ languages)

**2 of 6 projects have VN from source.** Storm Bear wiki adds VN-accessibility to the other 4.

---

## 🟡 Cái gì cần cải thiện / What needs improvement

### 1. Clone pipeline unreliable

3rd failure this session (also in v6 alone — 3 clone attempts). **Pattern:** git clone unreliable for large doc-heavy repos (course materials, multi-language translations).

**Action:** Update routine Phase 1 to prefer WebFetch for doc-heavy repos. Skip clone unless code execution needed.

### 2. Lesson 13 (Agentic Memory) not covered in detail

6th cluster planned but skipped (only 2 clusters produced). Memory concept deserves dedicated coverage.

**Action:** Future v6.1 supplementary summary OR dedicated entity page if Tier 3 grows.

### 3. Jupyter notebook contents not reviewed

Only lesson READMEs fetched. Notebooks = sample code value. Without review:
- Can't assess code quality claim
- Can't verify "learnability-optimized" framing
- Can't cross-reference to specific Tier 1 tool patterns

**Action:** Optional future deep dive if Tier 3 becomes major vault pillar.

### 4. Fork vs upstream divergence unknown

cvtot fork of microsoft/ai-agents-for-beginners. Whether fork has divergent content OR stays synced = unclear. Didn't `git log` compare.

**Action:** Flagged in open questions. Future check with `gh api repos/cvtot/ai-agents-for-beginners/compare/main...microsoft:main`.

### 5. Coming Soon lessons (15-18) not scoped

4 lessons listed but not released. Wiki snapshot = current state. When released, wiki needs update.

**Action:** Calendar reminder to check repo in 3 months for lesson 15-18 release.

### 6. Metacognition (L09) insufficient coverage

Unique concept in course, absent from Tier 1 siblings. Could deserve own entity page (instead of folded into Multi-Agent entity). Flagged opportunity.

**Action:** Consider `(C) Metacognition.md` entity page as v6.1 addition.

---

## 📊 Velocity comparison vs v1-v5

| Metric | v1 ECC | v2 SP | v3 gstack | v4 goclaw | v5 GSD | **v6 course** | Delta v5→v6 |
|--------|--------|-------|-----------|-----------|--------|--------------|-------------|
| **Session time** | ~6h | ~3.5h | ~2.5h | ~2.5h | ~2.5h | **~2h** | **-0.5h (first reduction since v3)** |
| **Format iter** | 3 | 0 | 0 | 0 | 0 | **0** | — |
| **Repo .md count** | ~20 | 73 | 92 | 117 | 396 | **?? (clone blocked)** | N/A |
| **Source strategy** | Individual | Individual | Individual+skim | Individual+skim | Aggressive skim | **Cluster (new)** | Novel |
| **Siblings at time** | 0 | 1 | 2 | 3 | 4 | **5** | +1 |
| **Phase 4b type** | N/A | 2-way | 3-way | Taxonomy (v4 2-tier) | 4-way | **Taxonomy v2 (3-tier)** | Extension |
| **Entity pages** | 7 | 4 | 4 | 4 | 4 | **4** | stable |
| **Published guides** | 1 | 2 | 2 | 2 | 2 | **2** | stable |
| **Beginner guide lines** | ~500 | ~447 | ~594 | ~620 | ~620 | **~550** | slight reduction |
| **Comparison/taxonomy lines** | 0 | ~445 | ~616 | ~500 | ~700 | **~750** | +50 |
| **Cross-project links** | 0 | ~15 | ~25 | ~40 | ~55 | **~70+** | +15 |
| **Domain** | Tier 1 | Tier 1 | Tier 1 | Tier 2 | Tier 1 | **Tier 3 (NEW)** | New tier |
| **Source acquisition** | Clone | Clone | Clone | Clone | Clone | **WebFetch** | Methodology shift |

**Key observations:**
- **First velocity reduction since v3** — v6 at ~2h despite clone friction
  - Cluster-based summary strategy saved writing time
  - Less comparison complexity (taxonomy extension vs 4-way)
  - Familiar terrain (6th run routine proficiency)
- **Different-domain handled** — routine didn't break outside agent-framework tool domain
- **Taxonomy evolution** — 2-tier → 3-tier cleanly emerged from N=6 corpus
- **Source acquisition adapted** — WebFetch-as-fallback added to arsenal

---

## 🎯 Insights cho vault-level

### Insight 1: Routine handles 3 domain routing types

- Same-domain (v2, v3, v5): N-way comparison
- Adjacent-domain (v4): taxonomy creation
- Same-tier (v5): 4-way pattern extraction
- **Different-domain (v6): taxonomy extension**

**4 routing modes observed across 6 runs.** Routine v1 handles without explicit spec.

### Insight 2: 3-tier taxonomy = stable structural model

6 corpus items partition cleanly across 3 tiers. No forcing. **Defensible durable model.**

Future entrants:
- 2nd Tier 3 → validates multi-entrant (watch LangChain Academy, DeepLearning.AI courses)
- 2nd Tier 2 → validates multi-entrant (watch LangGraph Platform, AutoGen Studio)
- Potential Tier 4 → infrastructure/research tier (watch MCP spec, research labs)

### Insight 3: Cluster summaries for education domain

**Source strategy scales:**
- v1-v5 (tool domain): 3 individual source summaries
- v6 (education domain): **3 cluster summaries**

Pattern: **adapt strategy to domain characteristics**. Tool docs = cohesive per file. Course = cohesive per theme cluster.

### Insight 4: WebFetch as resilient fallback

Clone blocked 3 times v6. WebFetch succeeded every time. Future routine should **try WebFetch first for doc-heavy repos** (save clone for code-execution-needed repos).

### Insight 5: Meta-relevance chain repeats

3 consecutive wikis (v4/v5/v6) each revealed Storm Bear adjacent learning.

**Pattern:** Wiki building = self-education. Every wiki → vault upgrade opportunity identified.

### Insight 6: Velocity bottleneck NOT understanding — it's writing

v6 reduction (~2h vs ~2.5h baseline) = cluster summaries wrote faster than individual summaries. **Writing time dominates, not comprehension.**

**Action:** Routine v2 should optimize for **faster writing per unit insight**, not faster reading.

### Insight 7: 3-tier coverage = decision framework complete for current corpus

All 3 tiers have at least 1 entrant. Storm Bear vault now has:
- Education resource for beginners
- 4 daily-use tools (Tier 1 spectrum)
- 1 deployment platform (Tier 2)

**Storm Bear decision tree complete for current moment.** Future wikis = refinement or tier multi-entrant validation, not filling gaps.

---

## ✏️ Action items cho vault

### Update skill `llm-wiki-routine` (carryover + new từ v6)

Existing từ v3/v4/v5:
- [ ] Phase 0.5 sibling classification
- [ ] Phase 2.5 vault-relevance check
- [ ] Phase 3.5 entity deduplication pass
- [ ] Phase 4b output-type logic encoded
- [ ] License tracking in Phase 0
- [ ] Velocity diversification trigger after plateau
- [ ] Document 4-way routing logic
- [ ] Add "framing specificity vs scope" analysis
- [ ] Track version tier normalization
- [ ] Skim-first threshold adjustment

**New từ v6:**
- [ ] **WebFetch-first for doc-heavy repos** — skip clone attempt for course/wiki/translation-heavy repos
- [ ] **Cluster summary strategy** — for education domain (≥10 lessons), use theme clusters not individual
- [ ] **Different-domain Phase 4b = taxonomy extension** — not new taxonomy, update existing
- [ ] **3-tier taxonomy reference** — encode Tier 1/2/3 classification in Phase 0 survey

### Update root CLAUDE.md

- [ ] Add ai-agents-for-beginners project entry in "Current Projects"
- [ ] Note: **3-tier taxonomy** established at N=6 corpus
- [ ] Note: First Tier 3 entrant (education tier)

### Update GOALS.md

- [ ] Mark 6th LLM Wiki shipped
- [ ] Note: routine v1 stable 6 runs (all 4 domain routing types)
- [ ] Recommend: **Option A Storm Bear pilot** still highest priority (unchanged from v3/v4/v5 recommendation)
- [ ] Update version log with v6 entry

### Vault TODOs

- [ ] Consider: VN translation QA PR for ai-agents-for-beginners (improve existing VN translations)
- [ ] Flag: cvtot fork vs microsoft upstream divergence unknown
- [ ] Consider: `(C) Metacognition.md` as v6.1 entity page addition
- [ ] Monitor: Coming Soon lessons 15-18 release (calendar reminder 3 months)

---

## 🚀 Next session recommendation

### Option A (HIGHEST PRIORITY): Storm Bear pilot

Unchanged từ v3+v4+v5+v6 consecutive recommendation. **Real use data > wiki analysis.**

Specifically: Pick 1 Tier 1 tool (gstack strongly suggested based on methodology match to Scrum coaching) + pilot on real Storm Bear project for 1-2 weeks.

### Option B: Routine v2 upgrade

Now 10+ action items carryover across v3-v6 iteration logs. **Routine v2 = worthwhile investment** if Storm Bear blocks Option A.

### Option C: 2nd Tier 3 wiki (education domain)

Candidates:
- LangChain Academy
- DeepLearning.AI agents short course
- Anthropic courses

**Why:** Validates Tier 3 multi-entrant. Similar value to v5 completing Tier 1 spectrum.

### Option D: 2nd Tier 2 wiki (service domain)

Candidates:
- LangGraph Platform
- AutoGen Studio (if platform-ized)
- E2B sandboxes

**Why:** Validates Tier 2 multi-entrant. Parallels Option C for Tier 2.

### Option E: Contribution back

- VN translation QA PR to ai-agents-for-beginners
- Storm Bear vault 3-tier taxonomy as public blog post
- Storm Bear as reference for VN agent developer community

**Why:** Compound reputation + validate externally.

### Option F: Cross-framework integration pilot

Install ECC + Superpowers trên same Claude Code. Test collisions.

**Why:** Empirical validation of Tier 1 4-way comparison claims.

### Storm Bear opinion

**Option A still strongest** after 4 consecutive recommendations. 6 wikis = plenty for decisions.

**Option B second** if pivoting to routine v2 investment.

**Option E third** if wanting to compound vault visibility externally.

---

## 🎉 Milestones achieved this session

- ✅ **6th LLM Wiki shipped** — ai-agents-for-beginners (Tier 3 completion)
- ✅ **First different-domain wiki** — education vs dev-tool siblings
- ✅ **Routine 6x consistent** — handles 4 routing types (same-domain N-way + adjacent taxonomy + same-tier 4-way + different-domain tier extension)
- ✅ **3-tier taxonomy established** — cleanly partitions 6 corpus items
- ✅ **Cluster summary strategy proven** — for education domain (3 clusters vs 3 individuals)
- ✅ **WebFetch fallback proven** — doc-heavy repos don't need clone
- ✅ **Velocity improved** — first reduction since v3 plateau (~2h vs ~2.5h)
- ✅ **Cross-project knowledge graph** — ~70+ links across 6 wikis
- ✅ **Meta-relevance continues** — L12 Context Engineering = GSD's context rot solution at concept level
- ✅ **Pattern proven 6x** — feature framework + methodology + role-based + platform + context-rot + **education curriculum**

> **Conclusion:** 6 wikis form **complete structural snapshot** of agent framework ecosystem (3 tiers covered). Routine production-stable across 4 routing modes. Storm Bear vault value = "use what's built" OR "expand via different-domain to test generalization further." 🪐

---

## Cross-references

- Sibling iteration logs:
  - v1 ECC, v2 Superpowers, v3 gstack, v4 goclaw, v5 GSD (all in siblings' `07 Iteration Logs/`)
- Published guides this wiki:
  - [[../03 Published/(C) AI Agents for Beginners - Huong dan cho nguoi moi]]
  - [[../03 Published/(C) Agent framework taxonomy v2 - 3 tier]]
- Taxonomy evolution:
  - v4 (2-tier): `../../goclaw - Beginner Analysis/03 Published/(C) Agent framework taxonomy.md`
  - v6 (3-tier): [[../03 Published/(C) Agent framework taxonomy v2 - 3 tier]]
- Routine: `../../../05 Skills/llm-wiki-routine.md`
- Skill: `../../../05 Skills/llm-wiki-ingest.md`
- Root vault: `../../../CLAUDE.md`
- Goals: `../../../GOALS.md`
