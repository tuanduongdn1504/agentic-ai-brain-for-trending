# (C) Iteration Log — v7 Build Learnings (2026-04-18)

> **Session type:** 7th auto-execution của routine `llm-wiki-routine` — **second different-domain wiki** (first after v6 course)
> **Duration:** 1 session (autonomous)
> **Outputs:** 13 files (3 sources + 4 entities + 2 published + 3 foundation + 1 log)
> **Purpose:** Test routine handles bridge/connector library (different-domain #2). Propose Tier 4 taxonomy extension.
>
> **Baselines (full progression N=1→7):**
> - v1 ECC (~6h, 0 siblings, first wiki, T1)
> - v2 Superpowers (~3.5h, 1 sibling, 2-way, T1)
> - v3 gstack (~2.5h, 2 siblings, routine codified, 3-way, T1)
> - v4 goclaw (~2.5h, 3 siblings, adjacent-domain, 2-tier taxonomy, T2)
> - v5 GSD (~2.5h, 4 siblings, 4-way, 6 emergent patterns, T1 slot complete)
> - v6 course (~2h, 5 siblings, different-domain #1, 3-tier taxonomy, T3)
> - **v7 notebooklm-py** (~2h, 6 siblings, **different-domain #2**, **4-tier taxonomy with bridge**, T4)

---

## Tóm tắt / Summary

v7 notebooklm-py tests routine's outer boundary again — **second different-domain wiki** after v6. First bridge/connector library in corpus. Velocity stable at ~2h. Taxonomy expanded v6 3-tier → v7 4-tier with Tier 4 "Agent-as-bridge" addition. Orthogonality observation: T4 plugs INTO T1/T2, may be more accurately described as cross-cutting axis than strict tier.

**Hypothesis verified:** Routine generalizes to 2nd different-domain type cleanly. API-probe-first rule (from v6 retry lesson) applied successfully — clone skipped entirely, WebFetch for 5 docs succeeded.

**Novel insights:**
1. **4-tier taxonomy** with T4 Bridge (agent-as-connector)
2. **Orthogonality** — T4 is cross-cutting axis, not strict tier
3. **Bridge maintainer bus factor = systematically 1** — T4 risk pattern
4. **Triple-surface design (Library + CLI + Skill)** emerging pattern for T4 bridges
5. **API-probe-first** saved 30+ min (no clone retries)

---

## ✅ Cái gì work tốt / What worked well

### 1. API-probe-first applied successfully (v6 retry lesson)

v6 spent ~30 min troubleshooting clone (3 failures). v7 went straight to API probe + WebFetch, **zero clone attempts**.

**Time saved:** ~30 min. 
**Decision criteria:** If repo has extensive docs + size decision possible via API → skip clone.

→ **Routine v2 action item converted to practice.**

### 2. Triple-surface routing — first time encountering Library + CLI + Skill pattern

notebooklm-py = 3 consumer surfaces (Python API / CLI / agent Skill). Generated 4 entity pages matching:
- CLI Surface (building block)
- Python API Architecture (architecture)
- Skill Integration (integration concept)
- Web-UI-Exclusive Capabilities (value prop)

**Pattern:** 4 entities fit naturally when library has multiple surfaces. Not forced to split or merge.

### 3. Tier 4 proposal emerges cleanly

Unlike v4 taxonomy (forced 4-way → reframed as 2-tier) or v6 taxonomy (3-tier addition natural), **v7 Tier 4 = unforced fit**.

notebooklm-py doesn't fit T1/T2/T3. New tier emerges immediately during Phase 0 classification.

**Confidence:** High. Alternative cross-cutting axis model also valid but doesn't conflict.

### 4. Cross-project links continue compounding

~90+ links across 7 wikis (est.). Each new wiki adds ~15-20 links. Compounding non-linear.

### 5. Meta-relevance chain continues (5 wikis in a row)

| Wiki | Meta-relevance finding |
|------|------------------------|
| v3 gstack | Specialist roles ≈ vault proto-MAS |
| v4 goclaw | Knowledge Vault = Karpathy pattern infrastructure |
| v5 GSD | `/gsd-ingest-docs` ≈ vault's `llm-wiki-ingest` |
| v6 course | L12 Context Engineering = GSD's context rot concept |
| **v7 notebooklm-py** | **Storm Bear routine could add Phase 4c podcast generation; SKILL.md mega-skill pattern ≈ llm-wiki-ingest pattern** |

**Pattern:** Every wiki reveals vault adjacent learning. Pattern reinforced.

### 6. 11K-star repo = significant corpus addition

notebooklm-py = 11,043 stars, highest among corpus (except Microsoft fork which = 56K upstream). Adds credibility to corpus.

**Signal:** T4 bridges can be mainstream — not niche. Solo maintainer ≠ low adoption.

### 7. Velocity held at ~2h

Same as v6. No regression despite:
- 4-tier taxonomy more complex than 3-tier
- First T4 entrant requires new entity types (Skill Integration entity is new)
- Cross-reference load grew (6 siblings to reference)

**Lesson:** Routine has reached steady-state velocity. Further reductions require architectural changes.

---

## 🟡 Cái gì cần cải thiện / What needs improvement

### 1. Tier 4 single-entrant = tentative

4-tier taxonomy proposed với only 1 T4 entrant. Multi-entrant validation pending.

**Action:** Flag in taxonomy doc. Resolve at 2nd T4 (e.g., Linear/Slack bridge next wiki).

### 2. Orthogonality model vs 4-tier — both valid

Taxonomy v7 covers both framings but doesn't pick winner:
- Strict 4-tier: T4 = tier
- Cross-cutting axis: T4 = plugin axis

**Action:** Resolve at 2nd T4 entrant. If 2nd T4 also plugs into T1/T2 → orthogonality wins. If 2nd T4 standalone → tier wins.

### 3. OpenClaw mention unresolved

notebooklm-py README names "OpenClaw" as compat agent. Unknown what OpenClaw is.

**Hypotheses:**
- OSS Claude Code alternative
- New Anthropic product
- Vaporware / aspirational mention

**Action:** Web search / check context at next session. May be candidate for next wiki.

### 4. Python 3.14 forward-compat claim unusual

Library claims support 3.10-3.14. Python 3.14 not released yet (2026-04-18). Either typo (meant 3.13) or aspirational.

**Impact:** Negligible on wiki quality. Note in open questions.

### 5. OpenClaw dilution of "Claude Code, Codex, OpenClaw" claim

If OpenClaw vaporware or unknown, claim of "compatible with Claude Code, Codex, OpenClaw" weakens.

**Action:** Verify OpenClaw existence before relying on cross-agent compat claim.

### 6. Skill Integration entity page overlaps with SKILL summary source

Entity #3 (Skill Integration) and Source #2 (SKILL summary) cover similar ground. Acceptable redundancy but could be tighter.

**Action:** Routine v2 — deduplicate Phase 2 vs Phase 3 content (already in action items from v3+).

### 7. VN translation gap repeated

Similar to gstack/GSD (no VN) and unlike course (has VN):
- notebooklm-py: en-only
- Storm Bear wiki adds VN layer = unique value

**Status:** Consistent pattern. Contribution opportunity flagged.

---

## 📊 Velocity comparison vs v1-v6

| Metric | v1 ECC | v2 SP | v3 gstack | v4 goclaw | v5 GSD | v6 course | **v7 nlmpy** | Delta v6→v7 |
|--------|--------|-------|-----------|-----------|--------|-----------|-------------|-------------|
| **Session time** | ~6h | ~3.5h | ~2.5h | ~2.5h | ~2.5h | ~2h | **~2h** | stable |
| **Format iter** | 3 | 0 | 0 | 0 | 0 | 0 | **0** | — |
| **Repo .md via API probe** | No | No | No | No | No | No | **Yes** | Methodology win |
| **Source strategy** | Individual | Individual | Individual+skim | Individual+skim | Aggressive skim | Cluster | **Individual (1 big SKILL + smaller cluster)** | Hybrid |
| **Siblings at time** | 0 | 1 | 2 | 3 | 4 | 5 | **6** | +1 |
| **Phase 4b type** | N/A | 2-way | 3-way | Taxonomy v4 2-tier | 4-way | Taxonomy v6 3-tier | **Taxonomy v7 4-tier + orthogonality** | Extension |
| **Entity pages** | 7 | 4 | 4 | 4 | 4 | 4 | **4** | stable |
| **Published guides** | 1 | 2 | 2 | 2 | 2 | 2 | **2** | stable |
| **Beginner guide lines** | ~500 | ~447 | ~594 | ~620 | ~620 | ~550 | **~620** | +70 |
| **Taxonomy guide lines** | 0 | ~445 | ~616 | ~500 | ~700 | ~750 | **~720** | -30 |
| **Cross-project links** | 0 | ~15 | ~25 | ~40 | ~55 | ~70 | **~90** | +20 |
| **Domain** | T1 | T1 | T1 | T2 | T1 | T3 | **T4 (NEW)** | New tier |
| **Source acquisition** | Clone | Clone | Clone | Clone | Clone | WebFetch | **API + WebFetch** | Methodology mature |

**Key observations:**
- **Velocity plateau confirmed at ~2h** (v6 + v7 identical)
- **API-probe-first** = standard practice now
- **Each "different-domain" wiki** extends taxonomy (v4: 2-tier, v6: 3-tier, v7: 4-tier)
- **Cross-project links compound** — still growing +15-20 per wiki
- **Format iterations 0** for 6 consecutive runs → routine stable

---

## 🎯 Insights cho vault-level

### Insight 1: Routine handles 4 distinct domain routing types

- Same-domain (v2, v3, v5): N-way comparison
- Adjacent-domain (v4): taxonomy creation (2-tier)
- Same-tier 4-way (v5): emergent pattern extraction
- Different-domain type A (v6): taxonomy extension (Tier 3 education)
- Different-domain type B (v7): taxonomy extension (Tier 4 bridge)

**6 distinct routing outcomes.** Routine v1 production-stable across all.

### Insight 2: 4-tier taxonomy with orthogonality

v6 established 3-tier. v7 added T4 with nuance: T4 is orthogonal plug-in axis. **Dual framing** in taxonomy v3 doc.

Future: v8 may formalize axis system OR add Tier 5 infrastructure.

### Insight 3: API-probe-first is production practice

v6 retry lesson → v7 SOP. Saved ~30 min. Pattern:
1. Curl API for metadata
2. Check size threshold (>1 GB = skip clone)
3. WebFetch key docs
4. Skip clone unless code execution needed

**Routine v2 should codify this as Phase 0.5.**

### Insight 4: Bridge maintainer systematic risk

T4 notebooklm-py = solo maintainer. Future T4 entrants likely same pattern (unofficial API reverse engineering = individual effort).

**Pattern:** T4 = highest bus factor risk in taxonomy.

**Vault implication:** Don't pin critical Storm Bear workflows on T4 bridges without fallback.

### Insight 5: Triple-surface design emerging

notebooklm-py = Library + CLI + Skill. Future T4 bridges likely same.

**Prediction:** Linear bridge, Slack bridge, GitHub enhanced bridge all follow triple-surface.

**Why:** Each surface serves different consumer:
- Library = Python devs
- CLI = shell scripters / agents
- Skill = agent users

### Insight 6: 7 wikis = significant corpus milestone

7 wikis × avg 13 files each = ~91 files.
7 × 4 tiers identified.
Cross-project links ~90+.

**Storm Bear vault = substantial knowledge asset now.** Not theoretical.

### Insight 7: Meta-relevance chain reaches 5 consecutive wikis

v3 → v7 all revealed vault adjacent learning. **Pattern robust.**

Future wikis: check meta-relevance by Phase 0.5 vault-relevance audit (action item from v3+).

---

## ✏️ Action items cho vault

### Update skill `llm-wiki-routine` (carryover + new từ v7)

Existing từ v3/v4/v5/v6:
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
- [ ] WebFetch-first for doc-heavy repos
- [ ] Cluster summary strategy for education domain
- [ ] Different-domain Phase 4b = taxonomy extension
- [ ] 3-tier taxonomy reference in Phase 0

**New từ v7:**
- [ ] **API-probe-first as Phase 0.5** — curl GitHub API before clone decision
- [ ] **Size-based clone decision** — skip clone if size >1 GB OR docs-only build
- [ ] **4-tier taxonomy reference** — encode T1/T2/T3/T4 classification
- [ ] **Bridge detection heuristic** — library + CLI + Skill triple = T4 signal
- [ ] **Orthogonality vs tier model** — pick at 2nd T4 entrant
- [ ] **OpenClaw disambiguation** — track 3rd-party agent compat claims

Total action items now **19+** across v3-v7. Routine v2 upgrade = high-value investment.

### Update root CLAUDE.md

- [ ] Add notebooklm-py project entry in "Current Projects"
- [ ] Note: **4-tier taxonomy** established at N=7 corpus
- [ ] Note: First Tier 4 entrant (bridge/connector)
- [ ] Update "Evidence" in LLM Wiki Routine pattern (5x → 7x)

### Update GOALS.md

- [ ] Mark 7th LLM Wiki shipped
- [ ] Note: routine v1 stable 7 runs (6 routing modes, 4 tiers)
- [ ] **Recommend: Routine v2 upgrade** (19+ action items) if Storm Bear pilot still blocked
- [ ] Update version log với v7 entry

### Vault TODOs

- [ ] Consider: Install notebooklm-py skill trong Claude Code, test retro podcast workflow
- [ ] Consider: VN translation PR for notebooklm-py README + SKILL
- [ ] Flag: OpenClaw disambiguation (candidate for 8th wiki?)
- [ ] Monitor: 2nd T4 entrant for multi-entrant validation

---

## 🚀 Next session recommendation

### Option A (HIGHEST PRIORITY, UNCHANGED): Storm Bear pilot

5th consecutive recommendation. 7 wikis = more than enough decision input. **Real use data > more wiki analysis.**

Recommended: Pick **gstack** (methodology matches Scrum coaching) OR **notebooklm-py** (immediate retro podcast value for team).

### Option B: Routine v2 upgrade

**Newly strong.** 19+ action items accumulated. Routine v2 = meaningful velocity + quality improvement.

Priorities for v2:
1. API-probe-first Phase 0.5
2. Size-based clone skip
3. Taxonomy-aware Phase 4b routing
4. Cluster summary heuristic
5. Bridge detection heuristic

### Option C: 2nd T4 wiki (validate multi-entrant)

Candidates:
- `linear-py` or similar Linear bridge
- Slack agent skill (MCP Slack server? Direct Slack bridge?)
- GitHub enhanced skill (beyond official MCP)
- Figma skill

**Why:** Validates T4 tier + orthogonality vs tier model resolution.

### Option D: Storm Bear + notebooklm-py integration pilot

Small pilot: install skill, test retro podcast workflow on real team retro transcript. Generates real-use data AND validates T4 bridge value proposition.

**Why:** Dual-win — Storm Bear pilot + T4 validation.

### Option E: Resolve OpenClaw (dirsambiguation wiki)

Mini-wiki (1-3 files) to disambiguate OpenClaw mention. Cheap to execute.

**Why:** Unblocks notebooklm-py claim about cross-agent compat. Low priority.

### Storm Bear opinion

**Option D = new best recommendation.** Replaces Option A solo pilot with **Option A + T4 validation combined**:
1. Install notebooklm-py skill cho Claude Code
2. Use it on real Storm Bear Scrum project
3. Generate retro podcast (real-use data)
4. Report back: T4 bridge value + Storm Bear workflow gaps

**Option B** second priority if Option D blocked (no real project ready).

---

## 🎉 Milestones achieved this session

- ✅ **7th LLM Wiki shipped** — notebooklm-py (Tier 4 establishment)
- ✅ **First Tier 4 entrant** — agent-as-bridge category established
- ✅ **4-tier taxonomy + orthogonality model** — v7 extends v6 3-tier
- ✅ **Routine 7x consistent** — handles 6 routing modes, 4 tiers
- ✅ **API-probe-first mainstreamed** — saved ~30 min vs v6 retries
- ✅ **Bridge bus factor pattern observed** — T4 = solo-maintained risk
- ✅ **Triple-surface design pattern** — Library + CLI + Skill (likely T4 standard)
- ✅ **Cross-project knowledge graph** — ~90+ links across 7 wikis
- ✅ **Meta-relevance continues** — 5 consecutive wikis reveal vault adjacent learning
- ✅ **Pattern proven 7x** — feature framework + methodology + role-based + platform + context-rot + education + **bridge/connector**
- ✅ **Velocity plateau confirmed** — ~2h steady-state across v6-v7

> **Conclusion:** 7 wikis × 4 tiers = substantial knowledge asset. Routine production-stable. 19+ action items carryover = clear v2 upgrade path. Storm Bear decision framework now covers Learn / Use / Integrate / Deploy full spectrum. 🪐

---

## Cross-references

- Sibling iteration logs:
  - v1 ECC, v2 Superpowers, v3 gstack, v4 goclaw, v5 GSD, v6 course (all in siblings' `07 Iteration Logs/`)
- Published guides this wiki:
  - [[../03 Published/(C) notebooklm-py - Huong dan cho nguoi moi]]
  - [[../03 Published/(C) Agent framework taxonomy v3 - 4 tier with bridge]]
- Taxonomy evolution:
  - v4 (2-tier): `../../goclaw - Beginner Analysis/03 Published/(C) Agent framework taxonomy.md`
  - v6 (3-tier): `../../ai-agents-for-beginners - Beginner Analysis/03 Published/(C) Agent framework taxonomy v2 - 3 tier.md`
  - v7 (4-tier): [[../03 Published/(C) Agent framework taxonomy v3 - 4 tier with bridge]]
- Routine: `../../../05 Skills/llm-wiki-routine.md`
- Skill: `../../../05 Skills/llm-wiki-ingest.md`
- Root vault: `../../../CLAUDE.md`
- Goals: `../../../GOALS.md`
