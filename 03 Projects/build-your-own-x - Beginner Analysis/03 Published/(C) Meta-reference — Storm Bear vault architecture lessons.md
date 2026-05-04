# (C) Meta-reference — Storm Bear vault architecture lessons

> **Outside Storm Bear 4-tier agent taxonomy.** Published as meta-reference — lessons Storm Bear vault can apply to its own architecture, extracted from build-your-own-x (491K-star aggregator).
> Corresponds to Phase 4b role: **meta-reference positioning** (new routing mode, different from v6 tier extension + v7 tier + orthogonality extension).
> For prior taxonomy (v7 4-tier): `../../notebooklm-py - Beginner Analysis/03 Published/(C) Agent framework taxonomy v3 - 4 tier with bridge.md`

---

## Tóm tắt / TL;DR

build-your-own-x is **not another agent wiki peer.** It belongs to different ecosystem (general programming education). Storm Bear's v7 4-tier agent taxonomy doesn't extend to accommodate it — **explicit out-of-scope classification** is cleaner.

**But** build-your-own-x offers **substantial architecture lessons** for Storm Bear vault itself. This doc codifies those lessons + proposes concrete vault improvements.

---

## Part 1 — Why "outside taxonomy" is the right framing

### Options considered for classification

1. **Extend taxonomy to Tier 5 "Catalog / Aggregator"** — BUT this conflates "any aggregator" với the 4-tier agent ecosystem axis. Would dilute taxonomy.

2. **Fit into Tier 3 "Education" as adjacent** — BUT Tier 3 = authored curriculum (like MS course). build-your-own-x = aggregated links, not authored. Different paradigm.

3. **Explicit outside scope** — Chosen approach. Acknowledges this is **different axis entirely** (general programming vs AI agent ecosystem).

### Decision: Outside scope + Meta-reference

**Benefits:**
- Preserves 4-tier taxonomy integrity
- Allows unique Phase 4b value (vault architecture lessons)
- Signals to future wikis: not every wiki fits agent taxonomy
- Maintains conceptual clarity

**Drawback:**
- Doesn't fit nice-uniform classification. Some wikis will always be "special cases."

### When to reclassify?

If 2nd non-agent aggregator wiki ships (e.g., "awesome-AI-agents", "LLM-frameworks list", etc.), reconsider Tier 5 formalization. For now, N=1 = ad-hoc.

---

## Part 2 — Lessons summary (from entity page detail)

See [[../02 Wiki/(C) Storm Bear Vault — Knowledge Architecture Lessons]] for deep dive. Executive summary:

### Lesson 1: Single-file architecture works at scale (sometimes)
build-your-own-x = 1 README for 491K users. Flat simple wins at certain scales.

### Lesson 2: Format standardization = value
Consistent `[**Language**: _Title_](URL)` = instant scannability.

### Lesson 3: Curator voice = defining asset
Daniel Stefanovic's taste set the tone. CodeCrafters preserves.

### Lesson 4: Community contribution scales with curation
491K stars from thousands of PRs. Curator essential.

### Lesson 5: Staging area for uncategorized content
Uncategorized section = intake. Graduates to own category when clusters form.

### Lesson 6: Sustainable funding source matters
CodeCrafters business model funds maintenance over 10 years.

### Lesson 7: License choice matters early
CC0 for content aggregators. MIT for code libraries.

---

## Part 3 — Actionable Storm Bear vault improvements

### Near-term (this month — immediate value)

#### Action 1: Codify 13-section entity page format explicitly

**Problem:** Format is emergent (from v1 ECC iteration log); new wikis may drift.

**Solution:** Add formal spec to `05 Skills/llm-wiki-routine.md` Phase 3 rules.

**Implementation:** 1-page spec listing 13 sections + example + common pitfalls.

#### Action 2: Standardize published guide template

**Problem:** Published guides vary in structure (6-11 parts, different headings).

**Solution:** Define canonical 9-part structure (intro, concepts, examples, comparison, roadmap, risks, next steps, contribution, summary).

**Implementation:** Template file in `04 System/` folder, referenced by routine.

#### Action 3: Create flat aggregator INDEX.md

**Problem:** Storm Bear vault has 8 projects; each has deep wiki. No flat browsable index.

**Solution:** Create `03 Projects/INDEX.md` in build-your-own-x style:

```markdown
# Storm Bear — Project Aggregator

## Tier 1: Agent-as-assistant
* [**TS**: _Everything Claude Code_](./Everything Claude Code - Beginner Analysis/)
* [**Methodology**: _Superpowers_](./Superpowers - Beginner Analysis/)
* [**Role-based**: _gstack_](./gstack - Beginner Analysis/)
* [**Context-rot**: _GSD_](./get-shit-done - Beginner Analysis/)

## Tier 2: Agent-as-service
* [**Go**: _goclaw_](./goclaw - Beginner Analysis/)

## Tier 3: Agent-as-education
* [**Curriculum**: _ai-agents-for-beginners_](./ai-agents-for-beginners - Beginner Analysis/)

## Tier 4: Agent-as-bridge
* [**Python**: _notebooklm-py_](./notebooklm-py - Beginner Analysis/)

## Meta-references
* [**Aggregator**: _build-your-own-x_](./build-your-own-x - Beginner Analysis/)
```

**Implementation:** 1 file, auto-maintainable via routine Phase 6.

### Mid-term (this quarter)

#### Action 4: License decision

**Current:** Unspecified (implied private).

**Proposal:**
- `02 Wiki/*` và `03 Published/*` = CC0 (if publishing publicly)
- `05 Skills/*` = MIT (if publishing publicly)
- Mark license in each folder's README

**Action needed only if publishing.** Private-only vault doesn't need license.

#### Action 5: CONTRIBUTING.md for team/community

**When needed:** If Storm Bear team or community contributes.

**Contents:**
- 13-section format specification
- Published guide template
- PR flow
- Review criteria
- Curator reservation (Cvtot preserves voice)

### Long-term (this year)

#### Action 6: Sustainable maintenance plan

**Current:** Cvtot + Claude solo. Sustainable while Cvtot employed.

**Risks:** If Cvtot life changes (new job, illness, etc.), vault stalls.

**Mitigation:** 
- Document routine fully (routine v2 spec)
- Multiple people trained to operate routine
- Periodic vault freshness audit

#### Action 7: Public release evaluation

**Options:**
- **Private forever** — solo curation, maximum voice control
- **Team-shared** — small team (3-5) with shared criteria
- **Public aggregator** — follow build-your-own-x model, high visibility

**Decision framework:**
- If Storm Bear becomes marketing asset for Cvtot's consulting → public
- If Storm Bear stays personal thinking tool → private
- If Storm Bear becomes team training → team-shared

---

## Part 4 — What build-your-own-x CAN'T teach Storm Bear

### 1. AI agent specifics
build-your-own-x predates AI agent era. Its lessons apply to **knowledge organization**, not agent framework selection.

### 2. Vietnamese context
build-your-own-x is English-only. Storm Bear's bilingual approach = beyond build-your-own-x's scope.

### 3. LLM-era learning
build-your-own-x assumes traditional "type code yourself" learning. LLM-era (Claude Code assisted learning) = new territory. Storm Bear pioneers this.

### 4. Routine automation
build-your-own-x = community-maintained over 10 years (slow). Storm Bear routine = 8 wikis in 1 month (fast). Different execution paradigm.

### 5. Small-scale curator
build-your-own-x has CodeCrafters team. Storm Bear = solo. Lessons from 491K-star don't fully transfer to 1-user.

---

## Part 5 — Novel Phase 4b routing mode: "Meta-reference"

### v2-v7 Phase 4b routing modes

| Wiki | Phase 4b output | Routing mode |
|------|-----------------|--------------|
| v2 Superpowers | 2-way comparison | Same-domain N-way |
| v3 gstack | 3-way comparison | Same-domain N-way |
| v4 goclaw | Taxonomy 2-tier | Adjacent-domain |
| v5 GSD | 4-way comparison | Same-tier N-way |
| v6 course | Taxonomy 3-tier | Different-domain type A |
| v7 notebooklm-py | Taxonomy 4-tier + orthogonality | Different-domain type B |
| **v8 build-your-own-x** | **Meta-reference + vault lessons** | **Outside scope (new)** |

### Characteristics of outside-scope routing

- Acknowledges wiki doesn't fit primary taxonomy
- Extracts meta-value (lessons about vault itself)
- Keeps taxonomy clean (no forced extension)
- Useful when N=1 doesn't justify new tier

### When to use this routing again

Future wikis potentially also outside scope:
- Personal productivity tools (not agent-specific)
- General programming resources
- Scrum/Agile meta-books
- Biography / essay collections

For these: meta-reference framing likely better than tier inflation.

---

## Part 6 — Taxonomy corpus after v8

### Final state (N=8)

| Tier | Entrants | Count |
|------|----------|-------|
| T1: Agent-as-assistant | ECC, Superpowers, gstack, GSD | 4 |
| T2: Agent-as-service | goclaw | 1 |
| T3: Agent-as-education | ai-agents-for-beginners | 1 |
| T4: Agent-as-bridge | notebooklm-py | 1 |
| Outside scope | build-your-own-x | 1 |
| **TOTAL** | | **8** |

### Tier multi-entrant validation status

| Tier | Multi-entrant validated? |
|------|--------------------------|
| T1 | ✅ Yes (4 entrants, Tier 1 completion in v5) |
| T2 | ❌ No (1 entrant — goclaw) |
| T3 | ❌ No (1 entrant — course) |
| T4 | ❌ No (1 entrant — notebooklm-py) |

**3 tiers unvalidated.** Future wikis should target 2nd T2/T3/T4 entrants to validate multi-entrant hypothesis.

---

## Part 7 — 7 concrete vault actions (summary)

| # | Action | Priority | When |
|---|--------|----------|------|
| 1 | Codify 13-section entity format explicitly | High | This week |
| 2 | Standardize published guide template | High | This week |
| 3 | Create flat aggregator `03 Projects/INDEX.md` | Medium | This month |
| 4 | License decision (CC0 for content, MIT for skills) | Medium | Before publishing |
| 5 | CONTRIBUTING.md | Low | Before opening team |
| 6 | Sustainable maintenance plan | Low | This quarter |
| 7 | Public release evaluation | Low | This year |

**Actions 1-3 = best immediate ROI.** Actions 4-7 = conditional on future decisions.

---

## Part 8 — Cross-vault synthesis

### All 8 Storm Bear wikis now share knowledge graph

~100+ cross-references est. across 8 wikis now. Largest vault knowledge graph yet.

### Meta-pattern: 8 wikis taught vault about itself

Each wiki revealed vault lessons:
- v1 ECC → 13-section format emerged
- v2 Superpowers → generalization pattern
- v3 gstack → routine codified
- v4 goclaw → taxonomy 2-tier unlocked
- v5 GSD → 4-way patterns
- v6 course → cluster strategy + WebFetch
- v7 notebooklm-py → API-probe-first + orthogonality
- **v8 build-your-own-x → knowledge architecture lessons**

**Every wiki = self-education opportunity.** Storm Bear compounds meta-knowledge.

---

## References

- Taxonomy v7 (4-tier, outside-scope alternative framework): `../../notebooklm-py - Beginner Analysis/03 Published/(C) Agent framework taxonomy v3 - 4 tier with bridge.md`
- Beginner guide: [[(C) build-your-own-x - Huong dan cho nguoi moi]]
- Entity pages this wiki:
  - [[../02 Wiki/(C) 29 Categories Taxonomy]]
  - [[../02 Wiki/(C) Feynman Philosophy Applied to Learning]]
  - [[../02 Wiki/(C) Curation Model]]
  - [[../02 Wiki/(C) Storm Bear Vault — Knowledge Architecture Lessons]] (primary synthesis)
- Sibling wikis (all agent-related):
  - 7 wikis in `03 Projects/` — all Tier 1/2/3/4 of agent taxonomy
- Routine: `../../../05 Skills/llm-wiki-routine.md`
- Root vault: `../../../CLAUDE.md`
- Goals: `../../../GOALS.md`
