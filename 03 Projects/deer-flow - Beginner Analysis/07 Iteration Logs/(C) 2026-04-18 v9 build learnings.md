# (C) Iteration Log — v9 Build Learnings (2026-04-18)

> **Session type:** 9th auto-execution của routine — **third different-domain wiki + Tier 5 proposal**
> **Duration:** 1 session (autonomous)
> **Outputs:** 13 files (3 sources + 4 entities + 2 published + 3 foundation + 1 log)
> **Purpose:** Test routine handles standalone autonomous agent app category (distinct from Claude Code plug-in T1, platform T2, bridge T4). Propose Tier 5 extension.
>
> **Baselines (full progression N=1→9):**
> - v1 ECC (~6h, 0 siblings, T1 first wiki)
> - v2 SP (~3.5h, 1 sibling, 2-way, T1)
> - v3 gstack (~2.5h, routine codified, 3-way, T1)
> - v4 goclaw (~2.5h, adjacent-domain, 2-tier, T2)
> - v5 GSD (~2.5h, 4-way, T1 complete, 6 emergent patterns)
> - v6 course (~2h, different-domain #1, 3-tier, T3)
> - v7 notebooklm-py (~2h, different-domain #2, 4-tier + orthogonality, T4)
> - v8 build-your-own-x (~2h, outside-scope meta-reference, 7 Phase 4b modes)
> - **v9 deer-flow (~2h, different-domain #3, 5-tier + T5 application)**

---

## Tóm tắt / Summary

v9 deer-flow introduces **Tier 5 "Agent-as-application"** — standalone autonomous agent harness (Devin/AutoGPT/OpenHands class). Distinct from T1 (Claude Code plug-in), T2 (multi-tenant service), T4 (library bridge). ByteDance-backed, 62K stars (2nd largest in corpus), MIT license, pushed today.

**Hypothesis verified:** Routine handles 3rd different-domain type (standalone autonomous app after education + bridge). Velocity stable at ~2h (4th consecutive wiki at plateau).

**Novel insights:**
1. **Tier 5 "Agent-as-application"** — new tier with deer-flow as first entrant
2. **Task-duration → form-factor pattern** (5th emergent pattern) — longer tasks = more infrastructure
3. **T5 vs T2 distinction** — single-tenant autonomous vs multi-tenant service
4. **Complementary relationship explicit** — deer-flow README says integrates with Claude Code via OAuth
5. **Most complex deployment** in corpus — 4 services + Nginx + Docker
6. **Corporate backing parallel** — T3 Microsoft + T5 ByteDance (standalone apps need infrastructure investment)

---

## ✅ Cái gì work tốt / What worked well

### 1. API-probe-first standard practice (4 consecutive wikis)

v6, v7, v8, v9 all used API probe before clone. Routine v2 should formalize as Phase 0 default.

### 2. Tier 5 proposal emerged cleanly

Like v7's T4 proposal, v9's T5 didn't force-fit. deer-flow genuinely doesn't match T1-T4. T5 = natural extension.

Unlike v8 which declared outside-scope (no tier fit), v9 fits new tier cleanly.

### 3. Taxonomy health improving

| Version | Tiers | Multi-entrant validated |
|---------|-------|-------------------------|
| v4 | 2 | 0 (too new) |
| v6 | 3 | T1 (4 entrants) |
| v7 | 4 | T1 (4 entrants) |
| **v9** | **5** | **T1 (4 entrants)** |

**3 tiers (T2, T3, T4, T5) still single-entrant.** N=10+ needed for multi-entrant validation.

### 4. Complementary positioning highlighted

deer-flow README explicit: can invoke Claude Code via OAuth; Claude Code can invoke deer-flow via `claude-to-deerflow` skill.

**New pattern observation:** Tier interoperability — T5 and T1 talk. Future: T2 embedding T4 bridges (proposed v7).

### 5. Corporate-backing pattern visible

| Tier | Corporate backing? |
|------|---------------------|
| T3 | Yes (Microsoft) |
| T1 | Mixed |
| T4 | Rare (solo usually) |
| **T5** | **Yes (ByteDance)** |
| T2 | Mixed |

**Pattern refined:** Tiers requiring significant infrastructure (T3 curriculum, T5 app) correlate với corporate backing. Solo maintainers rarely afford.

### 6. Cross-project links continue growing

~120+ links across 9 wikis now. Compound growth sustained (+15-20 per wiki).

### 7. Meta-relevance chain extended to 7 consecutive wikis (v3-v9)

deer-flow's Skill system (progressive loading) ≈ potential routine v2 enhancement (lazy-load skill definitions).

**Pattern reinforced:** Every wiki reveals vault adjacent learning.

### 8. Velocity plateau confirmed 4 consecutive

v6 + v7 + v8 + v9 all ~2h. Routine at steady-state. No further gains without architectural changes (routine v2).

---

## 🟡 Cái gì cần cải thiện / What needs improvement

### 1. T5 multi-entrant validation pending

Only deer-flow in T5. Need 2nd (candidates: OpenHands, AutoGPT, CrewAI, Agent Zero, Devin-OSS-alt) to validate.

**Action:** 10th wiki should target 2nd T5.

### 2. ByteDance strategic context thin

deer-flow = ByteDance OSS. What's ByteDance strategic intent? Related to Doubao (their LLM)? Thin analysis.

**Action:** Flag in open questions; research future.

### 3. LangGraph dependency analysis light

deer-flow deep-uses LangGraph. What are LangGraph's own governance signals? Another wiki candidate.

### 4. Cost analysis superficial

deer-flow sub-agents = cost multiplier. No empirical data in my wiki. Users will hit bill-shock without warning.

**Action:** Could add "Cost calculator" entity page if Storm Bear actually pilots.

### 5. Hands-on testing absent

I wrote wiki without actually running deer-flow. Classic routine limitation — documentation-level only.

**Action:** Phase 7 hypothetical — routine v2 could optionally include smoke test (install + hello-world).

### 6. T5 vs T2 line fuzzy in edge cases

deer-flow = single-tenant today. But could be deployed multi-user. At what point does T5 become T2?

**Action:** Crystallize rule at 2nd T5 wiki (may need T5a/T5b subcategories).

### 7. Action items continue accumulating

v8 had 26+. v9 adds ~6-8 new items. **~32+ total action items** across v3-v9.

**Recommendation:** Routine v2 = urgent NOW.

---

## 📊 Velocity comparison vs v1-v8

| Metric | v1-v5 | v6 | v7 | v8 | **v9** | Delta v8→v9 |
|--------|-------|----|----|-----|--------|-------------|
| **Session time** | 6h→2.5h | ~2h | ~2h | ~2h | **~2h** | stable |
| **Format iter** | 3→0 | 0 | 0 | 0 | **0** | — |
| **Repo size** | 67KB→13MB | ? | 26MB | 1.2MB | **32MB** | larger |
| **Stars** | 1K→5K | 56K | 11K | 491K | **62K** | 2nd largest |
| **Siblings at time** | 0-4 | 5 | 6 | 7 | **8** | +1 |
| **Phase 4b type** | N-way + Tier 2/3/4 | 3-tier | 4-tier | Outside-scope | **5-tier (T5 extension)** | 8th mode |
| **Entity pages** | 4-7 | 4 | 4 | 4 | **4** | stable |
| **Published guides** | 1-2 | 2 | 2 | 2 | **2** | stable |
| **Cross-project links** | 0-55 | 70 | 90 | 105 | **120** | +15 |
| **Domain** | T1 + T2 | T3 | T4 | outside | **T5** | new tier |
| **Source acquisition** | Clone | WebFetch | API+WebFetch | API+WebFetch | **API+WebFetch** | standard |
| **Complexity of subject** | Medium | Medium | Medium | Low | **High** | app = highest |

**Key observations:**
- **Velocity plateau 4 consecutive wikis** (~2h each)
- **8th distinct Phase 4b routing mode** (5-tier extension via T5)
- **Highest-complexity subject so far** (full-stack app với 4 services vs skill/plugin/bridge)
- **Corporate-backed repos accelerating** — T3 Microsoft, T5 ByteDance

---

## 🎯 Insights cho vault-level

### Insight 1: Routine handles 8 distinct Phase 4b routing modes

- Same-domain N-way (v2, v3, v5): 3 modes by N
- Adjacent-domain taxonomy creation (v4)
- Same-tier 4-way (v5)
- Different-domain tier extension (v6): T3 added
- Different-domain tier extension (v7): T4 added + orthogonality
- Outside-scope meta-reference (v8)
- **Different-domain tier extension (v9): T5 added**

**8 modes proven.** Routine v2 can codify all as explicit routing logic.

### Insight 2: 5-tier taxonomy covers spectrum adequately

9 corpus items clean partition across 5 tiers + 1 outside-scope. **Comprehensive for AI agent ecosystem current state.**

**Remaining gaps for future wikis:**
- 2nd entrants each tier (validate)
- Potential Tier 6 (protocol/infrastructure/spec)
- Subcategories within tiers (T1 subtypes? T5a vs T5b?)

### Insight 3: Corporate backing pattern refined

Tiers needing significant infrastructure (curriculum production T3 / app deployment T5) → corporate backing.
Tiers that can be solo-built (skill libraries T1, library bridges T4) → mixed.
Platforms T2 → mixed.

**For Storm Bear:** Solo vault operator OK for T1/T4 effort; T3/T5 scale requires resources.

### Insight 4: Deployment complexity correlates với ambition

| Ambition level | Tier | Deployment |
|----------------|------|------------|
| Learn | T3 | Static docs |
| Use daily | T1 | Plugin install |
| Integrate service | T4 | Library install |
| **Run autonomous** | **T5** | **Full-stack deploy** |
| Multi-tenant service | T2 | Platform operations |

**Pattern:** T5 = sweet spot of "ambitious autonomous + manageable complexity" (single-tenant).

### Insight 5: deer-flow's Skill system ≈ Storm Bear's `llm-wiki-routine.md`

Both Markdown-based. Both orchestrate multi-step workflows. **Pattern convergence** continues.

Interoperability potential: Storm Bear routine portable to deer-flow Skill format? If yes, routine runnable in deer-flow autonomous mode (task-submit routine, walk away, results later).

### Insight 6: Task-duration → form-factor is robust pattern

Validated across tiers:
- Seconds: T1 interactive
- Call-based: T4 libraries
- Minutes-hours: **T5 apps**
- Continuous: T2 platforms

**Implication:** Picking tier = picking duration profile. Storm Bear decision framework simplifies.

### Insight 7: Claude Code complementary positioning is rare

Most Tier siblings position AS Claude Code alternative. deer-flow explicitly complementary (OAuth both ways).

**Pattern:** Maturity signal. Established T5 can afford complementary positioning; nascent alternatives fight Claude Code for attention.

---

## ✏️ Action items cho vault

### Update skill `llm-wiki-routine` (carryover + new từ v9)

Existing từ v3-v8 (26+ items):
- Phase 0.5 sibling classification
- Phase 2.5 vault-relevance check
- Phase 3.5 entity deduplication pass
- Phase 4b output-type logic encoded
- License tracking in Phase 0
- Velocity diversification trigger
- Document routing logic
- Framing specificity analysis
- Version tier normalization
- Skim-first threshold
- WebFetch-first for doc-heavy
- Cluster summary strategy
- Different-domain = tier extension
- 3-tier taxonomy reference
- API-probe-first as Phase 0.5
- Size-based clone decision
- 4-tier taxonomy reference
- Bridge detection heuristic
- Orthogonality vs tier model
- Outside-scope classification criteria
- Meta-reference routing mode
- Single-file vs multi-file architecture
- Star-count threshold
- Vault-level meta-lesson entity page
- Flat INDEX.md aggregator
- 26+ items → v2 triggering threshold

**New từ v9 (6 items):**
- [ ] **5-tier taxonomy reference** — codify T1-T5 classifications
- [ ] **T5 "Agent-as-application" detection heuristic** — signals: standalone app + autonomous + minutes-hours tasks + frontend+backend
- [ ] **Corporate vs solo backing tracking** — Phase 0 should capture vendor type
- [ ] **Task-duration categorization** — map repos to duration profile (interactive/call/minutes-hours/continuous)
- [ ] **Complementary positioning detection** — signal of maturity (vs competitive framing)
- [ ] **Deployment complexity score** — 1-5 scale based on services + infra (useful for persona matching)

**Total: ~32+ action items.** Routine v2 upgrade **CRITICAL** now.

### Update root CLAUDE.md

- [ ] Add deer-flow project entry với Tier 5 framing
- [ ] Note 9-wiki corpus milestone
- [ ] Update routine evidence (8x → 9x proven)
- [ ] Note 5-tier taxonomy established

### Update GOALS.md

- [ ] Mark 9th LLM Wiki shipped
- [ ] Note T5 Agent-as-application tier established
- [ ] Update version log với v9 entry
- [ ] Strengthen routine v2 urgency (32+ action items)

### Vault TODOs

- [ ] Consider: install deer-flow, pilot Scrum retro synthesis custom skill
- [ ] Flag: 2nd T5 entrant validation needed (OpenHands/AutoGPT/CrewAI/Agent Zero)
- [ ] Monitor: LangGraph health (deer-flow deep-uses it)
- [ ] Consider: VN translation `README_vi.md` PR to deer-flow
- [ ] Consider: Zalo bot integration PR to deer-flow message gateway

---

## 🚀 Next session recommendation

### Option A: Storm Bear pilot với deer-flow (new recommendation)

Install deer-flow + deploy Scrum retro synthesis custom skill + pilot on 1 real team retro.

**Why:** 
- Dual-win: Storm Bear pilot (5th consecutive rec) + T5 validation
- deer-flow fits Scrum coaching use case (long autonomous tasks)
- Real-use data would inform Storm Bear vault strategy

### Option B (STRENGTHENED): Routine v2 upgrade

32+ action items now. 1-session codification sprint.

**Scope expanded:**
- All prior Phase 0.5 classification
- Phase 4b 8 routing modes explicit
- 5-tier taxonomy encoded
- T5 detection heuristic
- Complementary positioning detection
- Deployment complexity scoring

### Option C: 2nd T5 wiki (validate multi-entrant)

Candidates:
- OpenHands (OSS alternative to Devin)
- AutoGPT (classic, still maintained)
- CrewAI (multi-agent framework)
- Agent Zero (newer entrant)

**Why:** Validates T5 tier multi-entrant. Tests if deer-flow/autoGPT/OpenHands really same tier or need subcategories.

### Option D: Storm Bear architectural overhaul

Apply v8's 7 vault action items:
1. Codify 13-section format
2. Standardize published guide template
3. Flat INDEX.md aggregator
4-7 conditional on publishing decision

### Option E: Contribution sprint

- VN translation deer-flow (`README_vi.md`)
- Zalo integration PR (deer-flow gateway)
- Build Scrum coaching skill library for deer-flow

### Storm Bear opinion

**Option A + Option B combined = best path:**
- Week 1: Install deer-flow, test Scrum skill (Option A pilot)
- Week 2-3: Routine v2 upgrade (Option B)
- Week 4: Evaluate Option C (2nd T5 wiki) based on pilot learnings

**Option D = ongoing low-risk vault improvements alongside.**

---

## 🎉 Milestones achieved this session

- ✅ **9th LLM Wiki shipped** — deer-flow (Tier 5 establishment)
- ✅ **Tier 5 "Agent-as-application" added** — 5-tier taxonomy v4
- ✅ **3rd different-domain wiki** — routine handles standalone autonomous app category
- ✅ **8 distinct Phase 4b routing modes** — comprehensive coverage
- ✅ **5 emergent patterns observed** (task-duration → form-factor new)
- ✅ **Velocity plateau 4 consecutive** — ~2h stable
- ✅ **32+ action items** — routine v2 upgrade CRITICAL urgency
- ✅ **~120+ cross-project links** — knowledge graph dense
- ✅ **Meta-relevance 7 consecutive wikis** — progressive skill loading ≈ routine v2 enhancement
- ✅ **Pattern proven 9x** — feature/methodology/role/platform/context-rot/education/bridge/meta-reference + **standalone autonomous app**
- ✅ **ByteDance corporate-backed addition** — T5 parallels T3 Microsoft pattern
- ✅ **Complementary Claude Code positioning** — mature tier signal

> **Conclusion:** 9-wiki corpus = substantial AI agent ecosystem coverage (5 tiers). Routine production-stable across 8 Phase 4b routing modes. Storm Bear vault = comprehensive decision framework. **Routine v2 upgrade CRITICAL** (32+ action items). 🪐

---

## Cross-references

- Sibling iteration logs v1-v8 in siblings
- Published guides this wiki:
  - [[../03 Published/(C) deer-flow - Huong dan cho nguoi moi]]
  - [[../03 Published/(C) Agent framework taxonomy v4 - 5 tier with application]]
- Taxonomy evolution:
  - v4 (2-tier): goclaw wiki
  - v6 (3-tier): course wiki
  - v7 (4-tier + orthogonality): notebooklm-py wiki
  - v9 (5-tier + application): THIS wiki
- Routine: `../../../05 Skills/llm-wiki-routine.md`
- Root vault: `../../../CLAUDE.md`
- Goals: `../../../GOALS.md`
