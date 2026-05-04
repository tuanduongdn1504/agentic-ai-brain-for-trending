# (C) Iteration Log — v5 Build Learnings (2026-04-18)

> **Session type:** 5th auto-execution của routine `llm-wiki-routine` — **Tier 1 slot completion** (4 frameworks analyzed)
> **Duration:** 1 session (autonomous)
> **Outputs:** 13 files (3 sources + 4 entities + 2 published + 3 foundation + 1 log)
> **Purpose:** Verify routine handles **same-domain 4-way comparison** (after v4 adjacent-domain handling). Complete Tier 1 analysis for stable "spectrum" insight.
>
> **Baselines (full progression):**
> - v1 ECC (~6h, 0 siblings, first wiki)
> - v2 Superpowers (~3.5h, 1 sibling, 2-way comparison)
> - v3 gstack (~2.5h, 2 siblings, **routine codified**, 3-way comparison)
> - v4 goclaw (~2.5h, 3 siblings, **adjacent-domain reframe**, taxonomy unlock)
> - **v5 GSD** (~2.5h, 4 siblings, **Tier 1 spectrum complete**, 4-way comparison)

---

## Tóm tắt / Summary

v5 GSD completes Tier 1 slot với 4 frameworks. Routine handled **same-domain 4-way comparison** cleanly (vs v4's adjacent-domain reframe). Velocity plateau continues (~2.5h). **6 emergent 4-way patterns** unlocked that 3-way/taxonomy couldn't show.

**Hypothesis verified:** Routine stable cho both same-domain (4-way) và adjacent-domain (taxonomy) routing. Spectrum insight emerges at N=4 trong same tier.

**Novel insight:** Framing specificity correlates với scope (pattern #1). Context rot framing (GSD) + 33 agents = specificity enables ambition. Strategic finding.

---

## ✅ Cái gì work tốt / What worked well

### 1. Routine auto-routed to 4-way comparison

v4 adjusted Phase 4b to taxonomy (adjacent domain). v5 Phase 4b = 4-way comparison (same domain). **Routine handled both** without manual spec.

Logic inferred: if sibling in same tier/domain → 1:1 comparison. Else → taxonomy/context.

→ **Self-regulating.** Routine v1 generalized better than expected.

### 2. 4-way unlocks 6 emergent patterns

Only visible với 4 data points trong same tier:

1. **Framing specificity correlates với scope** — broad framing = broad scope; specific framing = medium-large scope
2. **Distribution mechanism evolution** — Plugin → Marketplace → Setup script → **npm** (getting friction-lower)
3. **Subagent taxonomy divergence** — Domain (ECC) vs Function (Superpowers + GSD) vs Role (gstack) — 3 mental models
4. **Workflow stage count convergence** — 5-7 stages consistently
5. **Voice protection maturity** — increases over framework maturity
6. **Commercial model diversification** — 4 different paths (paid products / pure OSS / recruiting funnel / crypto token)

→ 3-way showed "spectrum" (v3). 4-way shows "patterns" (v5). **Non-linear value compounds.**

### 3. Largest repo handled via aggressive skim

GSD = 396 .md files (highest of 5). CHANGELOG 2222 lines. USER-GUIDE 1184 lines. README 927 lines.

Skim strategy:
- README full (500 lines foundational)
- USER-GUIDE TOC + 2 sections
- CHANGELOG grep + head
- AGENTS.md quick scan

Time saved: ~3 hours. Coverage adequate.

### 4. Novel features captured (Spike/Sketch/Seeds/Threads)

GSD has 4 primitives absent from siblings:
- Spike/Sketch (pre-planning experiments → skill packaging)
- Seeds (time-aware forward capture với triggers)
- Threads (persistent cross-session context)
- Workstreams + Workspaces (parallelism on 2 axes)

→ **Best "unique primitives per framework" of 5 projects.** Enriches Tier 1 mental model.

### 5. Cross-project meta-relevance: `/gsd-ingest-docs`

v5 discovered GSD's unreleased `/gsd-ingest-docs` command:

> "Scan a repo containing mixed ADRs, PRDs, SPECs, and DOCs and bootstrap or merge the full `.planning/` setup from them"

**Convergent với Storm Bear vault's `llm-wiki-ingest` skill!** Same concept (scattered docs → structured knowledge), different implementation.

→ Meta-relevance pattern repeats (v4 discovered goclaw as potential vault backend; v5 discovered GSD command mirroring vault skill). **Cross-project learning compounds.**

### 6. Docs lag caught early

33 agents trong folder vs 21 in docs — discrepancy flagged in Phase 0 survey + carried through entity page. **Source = folder, docs lag.**

→ **Filesystem verification discipline** pays off. Would've missed trust-docs-only.

### 7. Vietnamese market gap identified

GSD = 4 langs (en/pt-BR/zh-CN/ja-JP/ko-KR), no VN. Unlike goclaw's Zalo + `README.vi.md`.

Captured as contribution opportunity. Storm Bear's wiki = first VN reference.

---

## 🟡 Cái gì cần cải thiện / What needs improvement

### 1. Version tier tracking absent

Framework versions:
- ECC: unknown recency
- Superpowers: v5.0.7
- gstack: v0.18.3.0
- goclaw: v3.x
- GSD: v1.37.1

→ 4 different versioning schemes. **Not normalized in comparison tables.** Future comparison could track "relative maturity" explicitly.

### 2. $GSD token tokenomics not investigated

Flagged but not resolved. Commercial implications unclear. If token value ties to framework usage, future pricing changes possible.

**Action:** Separate investigation session OR flag as permanent open question.

### 3. Agent count discrepancy persists

33 folder / 21 docs discrepancy mentioned but not resolved (which is "canonical"). Without GSD contributor input, can't verify.

**Possibility:** docs/AGENTS.md maintained manually, folder expanded. Either acceptable, just note.

### 4. Skills format compatibility untested

Multiple frameworks claim Anthropic skill format compatibility. Can GSD's skills import into gstack? Into Claude Code with Superpowers? **Not verified this session.**

**Action:** Future cross-framework integration test pilot.

### 5. 83 commands = learning cliff concern

v5 beginner guide introduced 83 commands but acknowledged overwhelm. Recommended "start with 7 core" heuristic.

**Trade-off:** breadth vs learnability. Flag as GSD weakness in Tier 1 decision tree.

### 6. Emergent pattern #1 (framing → scope) correlation not causal

Observed: specific framing + medium-large scope (GSD) vs broad framing + broad scope (ECC). **Correlation observed with N=4.** Causation?

Speculation: specific problem framing forces specific scope (can't have "context rot solution" with just 14 skills). But:
- gstack: medium framing + medium scope
- Superpowers: medium framing + narrow scope
- Correlation not monotonic

**Action:** Don't over-claim causation. Observe with N=5+ if pattern holds.

---

## 📊 Velocity comparison vs v1-v4

| Metric | v1 ECC | v2 SP | v3 gstack | v4 goclaw | **v5 GSD** | Delta v4→v5 |
|--------|--------|-------|-----------|-----------|-----------|-------------|
| **Session time** | ~6h | ~3.5h | ~2.5h | ~2.5h | **~2.5h** | stable |
| **Format iter** | 3 | 0 | 0 | 0 | **0** | — |
| **Repo .md count** | ~20 | 73 | 92 | 117 | **396** | +279 (3.4x) |
| **Repo size** | ~67KB | 140KB | 12MB | 42MB | **13MB** | -29MB |
| **Skim-first applied** | No | Partial | Yes (CHANGELOG) | Yes (several) | **Yes (most aggressive yet)** | Intense skim |
| **Siblings at time** | 0 | 1 | 2 | 3 | **4** | +1 |
| **Phase 4b type** | N/A | 2-way | 3-way | Taxonomy (reframed) | **4-way (same-tier)** | Different routing |
| **Entity pages** | 7 | 4 | 4 | 4 | **4** | — |
| **Published guides** | 1 | 2 | 2 | 2 | **2** | — |
| **Beginner guide lines** | ~500 | ~447 | ~594 | ~620 | **~620** | stable |
| **Comparison/taxonomy lines** | 0 | ~445 | ~616 | ~500 | **~700** | +200 (more data) |
| **Cross-project links** | 0 | ~15 | ~25 | ~40 | **~55+** | +15 |
| **Emergent patterns unlocked** | 0 | 0 | Spectrum (3) | Taxonomy (2-tier) | **4-way (6 patterns)** | Richest yet |

**Key observations:**
- **Velocity plateaued** at ~2.5h across v3/v4/v5 despite increasing complexity
- **Skim-first scaling** — 396 .md files handled in same time budget as 92
- **Cross-project links compound non-linearly** — each new wiki adds 15+ links (1.5x compounding)
- **Comparison doc size grows với N** — 4-way > taxonomy > 3-way > 2-way

---

## 🎯 Insights cho vault-level

### Insight 1: Tier 1 slot complete (4 frameworks)

All 4 Tier 1 frameworks analyzed. No more add-ons needed trong Tier 1 unless:
- New major Tier 1 entrant launches
- Community-requested specific analysis

→ **Storm Bear vault's Tier 1 coverage = definitive cho current state.**

### Insight 2: Routine handles domain routing automatically

Without explicit Phase 0.5 classification code, routine:
- v2-v3: same-domain → N-way comparison
- v4: adjacent-domain → taxonomy
- v5: same-tier → 4-way comparison

**Self-regulated based on analysis pattern.** Routine v2 upgrade can formalize (action items carryover).

### Insight 3: 4-way unlocks emergent-pattern extraction

3-way = spectrum. Taxonomy (2-tier model) = hierarchy. **4-way within same tier = patterns.**

Projection:
- 5-way same-tier: pattern refinement
- 6-way: diminishing returns unless new category emerges
- **Cross-tier (Tier 1 × Tier 2 integration patterns): new value**

### Insight 4: Framework cadence spectrum visible

| Framework | Cadence | Pattern |
|-----------|---------|---------|
| ECC | Monthly | Steady |
| Superpowers | 5/month | Aggressive |
| gstack | 5+/week | Extreme |
| goclaw | Active | Unknown |
| GSD | Active | Unknown |

**Pattern:** no framework plateaus. All actively developed. User picks based on culture + scope, not "mature vs new."

### Insight 5: Meta-relevance chain strengthens

v4: goclaw = Karpathy LLM Wiki pattern as infrastructure (potential vault backend)
v5: GSD's `/gsd-ingest-docs` = convergent với Storm Bear's `llm-wiki-ingest` skill

**Pattern:** Every wiki reveals something Storm Bear could learn/adopt/integrate. **Wiki building = self-education loop.**

### Insight 6: Voice protection as Tier 1 maturity signal

- ECC (oldest): none explicit
- Superpowers: explicit (Iron Law + "your human partner")
- gstack: 3 hard-gates (ETHOS + promotional + tone)
- GSD: implied (TÂCHES voice)

→ **Voice protection correlates with framework maturity.** AI agent slop concern is real.

### Insight 7: 5 is enough for Tier 1 analysis

Diminishing returns clear. 6th Tier 1 wiki:
- Same patterns confirmed
- New emergent? Unlikely unless new category
- Maintenance burden +20% per wiki

**Recommendation:** Shift from "more Tier 1 wikis" to either:
- Storm Bear pilot (real use data)
- Different domain wiki (non-agent-framework)
- Routine v2 upgrade
- Contribution back to frameworks

---

## ✏️ Action items cho vault

### Update skill `llm-wiki-routine` (carryover + new)

Existing từ v3/v4:
- [ ] Phase 0.5 sibling classification
- [ ] Phase 2.5 vault-relevance check
- [ ] Phase 3.5 entity deduplication pass
- [ ] Phase 4b output-type logic encoded
- [ ] License tracking in Phase 0
- [ ] Velocity diversification trigger after plateau

New từ v5:
- [ ] **Document 4-way routing logic** — what triggers 4-way vs taxonomy vs N-way?
- [ ] **Add "framing specificity vs scope" analysis** to comparison template
- [ ] **Track version tier normalization** — cache framework versioning conventions
- [ ] **Skim-first threshold adjustment** — aggressive skim scales to 400+ files fine

### Update root CLAUDE.md

- [ ] Add GSD project entry in "Current Projects"
- [ ] Note: Tier 1 slot complete (4 frameworks analyzed)
- [ ] Note: 6 emergent 4-way patterns in Tier 1

### Update GOALS.md

- [ ] Mark 5th LLM Wiki shipped
- [ ] Note: routine v1 stable 5 runs (all phases × all domain types)
- [ ] Recommend: shift from pattern expansion to real-use pilot OR different domain
- [ ] Update version log

### Vault TODOs

- [ ] Consider: VN translation PR for GSD (contribution opportunity)
- [ ] Consider: test if GSD's `/gsd-ingest-docs` can ingest Storm Bear's `00 Sources/` → compare output với manual wiki build
- [ ] Flag: $GSD Solana token implications (separate investigation)
- [ ] Decide: 6th wiki topic OR pivot to Storm Bear pilot

---

## 🚀 Next session recommendation

### Option A (HIGHEST PRIORITY): Storm Bear pilot

Unchanged từ v3+v4+v5 consecutive recommendation. **Real use data > wiki analysis.**

### Option B: 6th LLM Wiki different domain

Verify routine beyond agent frameworks:
- Anthropic MCP spec
- LangChain / LangGraph
- OpenAI Agents SDK
- n8n / Make.com workflow platforms

**Why:** Test routine's outer generalization.

### Option C: Routine v2 upgrade

Encode 8+ action items across v3+v4+v5 iteration logs. Formalize domain classification + 4-way logic + velocity triggers.

**Why:** Routine maintenance = scale enabler. Code skill before pattern expansion.

### Option D: Cross-framework integration test

Install multiple Tier 1 frameworks trên same Claude Code. Test collision patterns. Validate 4-way comparison claims.

**Why:** Empirical validation của wiki-level claims.

### Option E: Contribute back

- VN translation PR to GSD (or gstack)
- Storm Bear vault as reference blog post
- Taxonomy framework contribution to community

**Why:** Compound vault reputation + validate externally.

### Storm Bear opinion

**Option A still strongest.** 5 wikis = plenty for decisions. Real use fills only gap.

**Option C second** if Option A blocked by external factor.

**Option D third** if want empirical backing before committing.

---

## 🎉 Milestones achieved this session

- ✅ **5th LLM Wiki shipped** — GSD (Tier 1 completion)
- ✅ **Routine 5x consistent** — stable across all analyzed domain types
- ✅ **Tier 1 slot complete** — 4 frameworks analyzed cleanly
- ✅ **4-way comparison built** — 700+ lines với 15-axis analysis
- ✅ **6 emergent 4-way patterns** — unlock not visible với 3-way or taxonomy
- ✅ **Cross-project knowledge graph** — ~55+ links across 5 wikis
- ✅ **Meta-relevance chain continues** — GSD's `/gsd-ingest-docs` ≈ Storm Bear's `llm-wiki-ingest`
- ✅ **Pattern proven 5x** — feature framework (ECC) + methodology (Superpowers) + role-based (gstack) + platform (goclaw Tier 2) + **context-rot spec (GSD)**

> **Conclusion:** Routine + skill library production-stable. 5 wikis form **decision framework** cho AI agent tooling selection. Storm Bear vault value shifts from "build more" to "use + share." Compounding knowledge architecture 🪐

---

## Cross-references

- Sibling iteration logs:
  - v1 ECC, v2 Superpowers, v3 gstack, v4 goclaw (all in siblings)
- Published guides:
  - [[../03 Published/(C) GSD - Huong dan cho nguoi moi]]
  - [[../03 Published/(C) Tier 1 4-way comparison]]
- Routine: `05 Skills/llm-wiki-routine.md`
- Skill: `05 Skills/llm-wiki-ingest.md`
- Taxonomy guide from v4: `../../goclaw - Beginner Analysis/03 Published/(C) Agent framework taxonomy.md`
