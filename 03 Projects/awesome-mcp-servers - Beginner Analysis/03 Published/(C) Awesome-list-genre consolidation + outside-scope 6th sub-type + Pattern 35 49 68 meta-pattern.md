# (C) Awesome-list-genre consolidation + outside-scope 6th sub-type + Pattern 35/49/68 meta-pattern

> **Storm Bear LLM Wiki v31 Phase 4b deliverable.**
> **Subject:** 3-way comparison across corpus awesome-list-genre wikis (build-your-own-x v8 + awesome-design-md v25 + awesome-mcp-servers v31) + audience sub-type classification + Pattern #68 meta-pattern consolidation proposal + Pattern #18 Agent Runtime Standardization strengthening.
> **Date:** 2026-04-22. **Author:** Claude (C). **Bilingual VN/EN** (primary VN; EN summary per section).

---

## 1. Mục đích / Purpose

**VN:** Tại v31, Storm Bear corpus có 3 wiki cùng genre (awesome-list-style aggregator directory), mỗi wiki phục vụ một audience khác nhau:

1. **build-your-own-x v8** — tutorials cho người học (human-directed learning input)
2. **awesome-design-md v25** — DESIGN.md templates cho AI agents (AI-agent-directed content input)
3. **awesome-mcp-servers v31** — MCP server directory (AI-runtime infrastructure directory)

Hai candidates (#35 + #49) đã được register sau v8 + v25. Tại v31, thay vì register candidate #68 làm MCP-server-aggregator-standalone (3rd aggregator candidate), deliverable này **đề xuất consolidation-forward meta-pattern** — Pattern #68 wraps 3 sub-types thành một meta-pattern duy nhất, đề xuất retire #35 + #49 tại audit.

**EN:** With 3 aggregator-genre wikis now in corpus, this deliverable proposes consolidation-forward registration: Pattern #68 as meta-pattern wrapping #35 + #49 + MCP-server-aggregator with 3 audience sub-type classifications. Ratio-discipline-positive approach.

---

## 2. 3-way comparison table (~18 axes)

| Axis | build-your-own-x v8 | awesome-design-md v25 | awesome-mcp-servers v31 |
|------|---------------------|----------------------|-------------------------|
| **Owner** | CodeCrafters Inc. (originally Daniel Stefanović) | VoltAgent (commercial-startup) | Frank Fiegel (solo, Glama founder) |
| **Org archetype** | Individual-to-company transition | Commercial-startup ecosystem | Solo-ecosystem-layer-with-commercial-platform |
| **Launch date** | ~2016 (tutorial curation) | 2026-03-31 | 2024-11-30 |
| **Age (at 2026-04-22)** | ~10 years | 3 weeks | 17 months |
| **Stars** | 491,000 | 60,585 | 85,323 |
| **Scale velocity** | Ultra-long-burn (~4K/month, 10 yrs) | Extreme-viral (~9K/day, 20 days) | Sustained-community-viral (~5K/month, 17 mo) |
| **License** | CC0 | MIT | MIT |
| **Content language** | Markdown (links to external tutorials) | Markdown (DESIGN.md templates stored in-repo) | Markdown (links to external MCP server repos) |
| **Category count** | 29 | 10 | 50+ |
| **Entry count** | ~200 tutorials | 69 design systems | ~1,200 MCP servers |
| **Legend/taxonomy** | None | None | **4-axis 15-badge** |
| **i18n language count** | 1 | 1 | **7** |
| **Commercial companion** | None explicit | getdesign.md | glama.ai/mcp/servers + Glama Chat |
| **Sibling framework published** | No | Yes (voltagent parent framework) | Yes (fastmcp by Fiegel) |
| **Paired companion directory** | No | No | Yes (awesome-mcp-clients 6.4K stars) |
| **Industry-state report** | No | No | Yes (State-of-MCP-2025) |
| **Agent-PR protocol** | No explicit | No explicit | Yes (`🤖🤖🤖` fast-track) |
| **Audience sub-type** | Human-directed learning | AI-agent content input | AI-runtime infrastructure |
| **Scope vs corpus** | Outside-scope sub-type 1 | Outside-scope sub-type 5 | Outside-scope sub-type 6 |
| **Supply-chain surface** | Low (tutorial links) | Low (template content) | **High (runtime plugins installable, 1,200 trust boundaries)** |

### Key observations from 3-way

**1. Scale velocity pattern diverges widely.** v8 / v25 / v31 represent 3 distinct Pattern #27 sub-paths: ultra-long-burn / extreme-viral / sustained-community-viral. Aggregator genre does NOT predict velocity.

**2. Legend complexity correlates with functional role.** v31 has 4-axis 15-badge vocabulary; v8 + v25 have none. MCP = runtime infrastructure where language / OS / scope matters for filtering; tutorials + templates don't require multi-axis classification.

**3. i18n investment correlates with ecosystem-layer ambition.** v31 has 7-language README; v8 + v25 have 1 each. Fiegel invested i18n as ecosystem-reach signal; v8 + v25 did not.

**4. Commercial companion pattern emerging.** v25 + v31 both have commercial companion platforms (getdesign.md / glama.ai). v8 does not (CodeCrafters is separate product, not companion to the aggregator). Pattern #50 reaches N=2 structurally-unambiguous.

**5. Supply-chain surface differs meaningfully.** v8 tutorials = low risk (read-only knowledge). v25 DESIGN.md templates = medium risk (agents consume as context). v31 MCP servers = high risk (installable runtime plugins). **Audience sub-type predicts risk surface.**

---

## 3. Audience sub-type classification (3 audiences)

### Sub-type A: Human-directed learning input

**Exemplar:** build-your-own-x v8
**Content:** Tutorials / educational links
**Consumption:** Humans read-and-implement
**Risk surface:** Low (read-only knowledge)
**Curation bar:** High-quality educational value
**Longevity expectation:** 5+ years (educational content ages slowly)
**License pattern:** CC0 / permissive
**Governance complexity:** Low (issue-based quality filter)

### Sub-type B: AI-agent-directed content input

**Exemplar:** awesome-design-md v25
**Content:** Templates / prompts / structured context
**Consumption:** LLMs + agents consume as prompt / context
**Risk surface:** Medium (content shapes agent behavior)
**Curation bar:** Fits agent interpretation + is safe as context
**Longevity expectation:** 1-3 years (agent norms evolve)
**License pattern:** MIT / permissive
**Governance complexity:** Medium (template quality signal)

### Sub-type C: AI-runtime infrastructure directory

**Exemplar:** awesome-mcp-servers v31
**Content:** Runtime plugins / servers / executables
**Consumption:** Agents invoke at runtime via protocol
**Risk surface:** **High (installable runtime with potential system access)**
**Curation bar:** Technical compatibility + security + spec-compliance
**Longevity expectation:** Ecosystem-speed (protocol evolves)
**License pattern:** MIT / permissive
**Governance complexity:** High (multi-axis classification required)

**Observation:** as audience moves from human → agent-content → agent-runtime, risk surface increases, curation complexity increases, governance requirements increase. Meta-pattern formulation should capture this progression.

---

## 4. Pattern #68 meta-pattern formulation

### Unified statement

> **Awesome-list-genre aggregators** emerge as community-curated directories with **3 distinguishable audience sub-types**: (a) **human-directed learning input**, (b) **AI-agent-directed content input**, (c) **AI-runtime infrastructure directory**. All share: light governance / MIT or CC0 license / alphabetical organization / community PR intake / concurrent-with-ecosystem-emergence timing. Sub-type classification predicts risk surface (low→medium→high) and governance complexity (low→medium→high).

### Consolidation plan at promotion

- **Retire Pattern #35 Education-Aggregator** as standalone; convert to sub-type A of meta-pattern
- **Retire Pattern #49 Design-Template-Aggregator-for-AI-Agents** as standalone; convert to sub-type B of meta-pattern
- **Pattern #68 registered at v31 as meta-pattern candidate** — evaluate promotion at next audit
- Future aggregator wikis register data points against meta-pattern (with sub-type tag), not new standalone patterns

### Benefits

1. **Ratio discipline:** 3 candidates → 1 meta-pattern (net -2 active candidates at promotion)
2. **Structural clarity:** audience sub-type captures meaningful variation
3. **Audit efficiency:** 1 audit action (promote meta-pattern) vs 3 separate decisions
4. **Future-ready:** 4th, 5th aggregator wikis fit sub-type taxonomy without pattern-library bloat

### Risks

- **Loss of granularity:** sub-type nuance may compress if too aggressive
- **Premature generalization:** 3 data points is minimum for meta-abstraction; audit may judge too early
- **Audit friction:** retire-at-promotion is multi-step operator decision; simpler to keep separate

### Alternative: keep 3 standalone

If operator audit prefers granular tracking:
- Keep #35 standalone (education-aggregator)
- Keep #49 standalone (design-template-aggregator)
- Promote #68 as 3rd standalone (MCP-server-aggregator)
- **Net result:** 3 active candidates remain, ratio does not improve

### Recommendation

**Consolidation-forward.** Register Pattern #68 as meta-pattern with explicit retire-at-promotion of #35 + #49. Audit decides at next trigger. Default if ratio discipline prioritized.

---

## 5. Pattern #18 Agent Runtime Standardization — strengthening

### Pre-v31 state

Pattern #18 registered candidate v15 (multica + graphify). Strengthened v17 → community-platform-specific. v19 CN-community split refinement. N=2 Western-community + 1 CN-community.

### v31 evidence (major strengthening)

**v31 is the directory of the MCP runtime standard at corpus scale.**

- 85,323 stars (corpus-top-5 scale)
- ~1,200 curated MCP servers × 50+ categories
- Concurrent launch with Anthropic MCP spec (2024-11-30)
- ≥6 corpus wikis consume MCP (goclaw v4 / multica v15 / graphify v16 / spec-kit v17 / TrendRadar v19 / OpenHands v30)
- Commercial platform companion (Glama Chat) integrates MCP
- Industry-state report (State-of-MCP-2025) formalizes ecosystem narrative

### Triple-layer runtime view post-v31

| Layer | Standard | Scale signal | Adoption |
|-------|----------|--------------|----------|
| **Transport/resource protocol** | **MCP** (Anthropic) | 85K directory + 1,200 servers | ≥6 corpus wikis consume |
| **Agent-runtime (community)** | OpenClaw | 5 corpus wikis integrate | Western-community-specific |
| **Agent-framing/protocol sibling** | Hermes | 3 corpus wikis integrate | Western-community-specific |

MCP + OpenClaw + Hermes are complementary layers, not competing. MCP = resource access protocol; OpenClaw + Hermes = agent-execution conventions.

### Audit recommendation

**Pattern #18 PROMOTE to CONFIRMED at next audit.**

- MCP corpus-pervasive (6+ wikis consume + 1 meta-reference directory at 85K scale)
- Structurally-unambiguous at multi-wiki evidence across 2+ tiers
- Meta-reference (v31) validates ecosystem consolidation claim

Formulation post-promotion should distinguish 3 layers with MCP as dominant transport standard.

---

## 6. Pattern #50 Commercial-Funnel Companion Platform — N=2

### Pre-v31 state

Registered candidate v25 (VoltAgent + getdesign.md). N=1.

### v31 evidence

**Fiegel + Glama stack.** Matches all structural features:
- Free OSS aggregator (awesome-mcp-servers) as top-of-funnel
- Branded commercial web platform (glama.ai/mcp/servers + Glama Chat)
- MIT permissive licensing on OSS side
- Commercial platform downstream of directory traffic
- No proprietary-tier-on-OSS-core (distinguishes from Pattern #31 open-core)

### Structural comparison

| Feature | VoltAgent + getdesign.md v25 | Fiegel + Glama v31 |
|---------|------------------------------|----------------------|
| OSS aggregator name | awesome-design-md | awesome-mcp-servers |
| Commercial platform name | getdesign.md | glama.ai (Chat + MCP directory + Blog) |
| OSS license | MIT | MIT |
| Owner | Commercial-startup org | Solo + commercial company |
| Industry-state publication | No | Yes (State-of-MCP-2025) |
| Sibling framework OSS | Yes (voltagent) | Yes (fastmcp) |
| Paired directory OSS | No | Yes (awesome-mcp-clients) |

Both meet Pattern #50 criteria at structurally-unambiguous N=2.

### Audit recommendation

**Pattern #50 PROMOTE to CONFIRMED at next audit.** Structurally-unambiguous N=2 criterion met. Distinguish from Pattern #31 open-core (separate-commercial-platform vs proprietary-tier-on-OSS-core).

---

## 7. New candidates at v31 (conservative)

### #68 Awesome-list-genre meta-pattern (consolidation-forward)

As §4 above. N=3 data points (v8 + v25 + v31). Consolidation-forward registration proposes retire #35 + #49 at promotion.

### #69 Agent-PR Fast-Track Governance Protocol

**Description:** Explicit workflow-level routing for automated-agent-authored PRs (e.g., `🤖🤖🤖` title suffix opt-in in awesome-mcp-servers CONTRIBUTING.md). Corpus-first explicit workflow-primitive.

**Distinct from:** retired Pattern #23 AI-Disclosure Policy (passive declaration). #69 is active workflow-routing primitive.

**N:** 1 at v31
**Tier:** outside-scope only
**Stale-risk:** flagged at registration (per v30 iteration log discipline). Check at v36, retire at v41 if no 2nd data point.

### No other new candidates

Per discipline, avoid new registrations for:
- Fiegel ecosystem-individual variant 6 → document as Pattern #17 strengthening (9th data point)
- Glama commercial platform → document as Pattern #50 N=2 promotion-candidate
- MCP as runtime standard → document as Pattern #18 major strengthening
- Sustained-community-viral sub-path → document as Pattern #27 9th data point
- Thai README first-in-corpus → observational, not pattern
- `fastmcp` as TypeScript framework published by directory maintainer → observational (conflict-of-interest tension worth noting but not pattern-track)

---

## 8. Outside-scope sub-type register at v31

| # | Sub-type | Wiki(s) | Audience | Pattern ref |
|---|----------|---------|----------|-------------|
| 1 | Education-aggregator | build-your-own-x v8 | Human learners | #35 → sub-type A of #68 |
| 2 | Foundation-model-as-product | fish-speech v20 | ML developers | (standalone) |
| 3 | Prompt-leak-archive | system-prompts-leaks v21 | AI-ops | (standalone) |
| 4 | Training-infrastructure | LlamaFactory v22 + Unsloth v23 | ML engineers | Pattern #41 (confirmed v23) |
| 5 | Design-template-aggregator-for-AI-agents | awesome-design-md v25 | Coding-agent users | #49 → sub-type B of #68 |
| **6** | **MCP-server-aggregator** | **awesome-mcp-servers v31** | **Agent infrastructure builders** | **sub-type C of #68** |

6 sub-types post-v31. Three (1 / 5 / 6) unify via Pattern #68 meta-pattern. Three (2 / 3 / 4) remain distinct outside-scope categories.

---

## 9. Ratio projection analysis

### Literal count post-v31

- Confirmed: 28
- Active candidates: 30 (28 pre + 2 new #68 + #69)
- Stale: 3
- Retired: 5
- Observation-track: 2
- **Ratio: 28:30 = 1.00:1 at trigger threshold**

### Post-#68-promotion (future audit scenario)

If #68 promotes to confirmed + retires #35 + #49:
- Confirmed: 29 (28 + #68)
- Active candidates: 30 − 2 retirements − 1 promotion = 27
- **Ratio: 29:27 = 0.93:1 (improvement)**

If additionally Pattern #18 + #42 + #44 + #50 all promote (4 additional promotions):
- Confirmed: 33
- Active candidates: 27 − 4 = 23
- **Ratio: 33:23 = 0.70:1 (significantly healthier)**

### Implication

v31 literal state 1.00:1 is at trigger but next audit has clear path to 0.70:1 via simultaneous consolidation + promotions. Ratio discipline very healthy when planned holistically.

---

## 10. Corpus lifecycle observation

Per v26 HF agents-course tier-closure inflection:
- **v1-v25:** corpus-BUILDING (tier gaps, pattern accumulation)
- **v26+:** corpus-APPLICATION (apply accumulated patterns)

**v30 + v31 demonstrate corpus-application mode:**
- v30: un-staling mechanism first-use; ratio 1.00→0.93 via existing candidate validation
- v31: consolidation-forward meta-pattern first-use; ratio 0.93→1.00 but with structural path to 0.70 via audit

**Both wikis strengthen existing patterns more than register new.** Pattern #18 (v31) + #50 (v31) + #31/#32/#42/#44 (v30) all become promotion-candidates at next audit.

---

## 11. Storm Bear implications

### Direct-infrastructure relevance (HIGH)

awesome-mcp-servers v31 is **infrastructure-usable-today** for Storm Bear:
- MCP server discovery for Scrum-coach workflow (Product Management / Version Control / Communication / Workplace & Productivity / Knowledge & Memory)
- graphify v16 MCP server = vault-query pathway
- Potential VN README translation contribution

### Methodological parallel — ecosystem-historian artifact

Fiegel produces State-of-MCP-2025 from 1,200-server curation. Storm Bear produces Pattern Library from 31-wiki corpus. Same methodology class.

**Strategic recommendation:** consider State-of-Agent-Frameworks-2026 report as high-ROI application of accumulated corpus. Would aggregate:
- 31 wiki summaries → industry analysis
- Pattern Library → formal claim catalog
- Tier distribution / scale distribution / license diversity / organizational archetypes
- Publishable artifact establishing Storm Bear as ecosystem-historian

### Ecosystem-layer playbook reference

Fiegel's stack (directory → framework → commercial companion → industry report) is applicable model if Storm Bear ever publishes public-facing assets:
- Directory-first positioning
- Concurrent-with-ecosystem timing
- Multi-language i18n investment
- Agent-PR fast-track governance
- Commercial companion downstream

---

## 12. Cross-references

### Pattern Library peers

- [[PATTERN_LIBRARY]] — v31 direct updates section
- [[03 Projects/build-your-own-x - Beginner Analysis/|build-your-own-x v8]] — sub-type A exemplar
- [[03 Projects/awesome-design-md - Beginner Analysis/|awesome-design-md v25]] — sub-type B exemplar
- Pattern #17 Ecosystem-Layer Orgs peers: safishamsi v16 / VoltAgent v25 / Yeachan v27
- Pattern #18 peers: multica v15 / graphify v16 / TrendRadar v19 / OpenHands v30 / goclaw v4 / spec-kit v17
- Pattern #50 peer: VoltAgent + getdesign.md v25

### MCP consumer peers (v31 = meta-reference for these)

- [[03 Projects/goclaw - Beginner Analysis/|goclaw v4]]
- [[03 Projects/multica - Beginner Analysis/|multica v15]]
- [[03 Projects/graphify - Beginner Analysis/|graphify v16]]
- [[03 Projects/spec-kit - Beginner Analysis/|spec-kit v17]]
- [[03 Projects/TrendRadar - Beginner Analysis/|TrendRadar v19]]
- [[03 Projects/OpenHands - Beginner Analysis/|OpenHands v30]]

### Sibling wiki files

- [[02 Wiki/(C) Cluster — README structure + categorization taxonomy]]
- [[02 Wiki/(C) Cluster — Aggregator governance + contribution + community]]
- [[02 Wiki/(C) Cluster — punkpeye ecosystem + companion projects]]
- [[02 Wiki/(C) punkpeye — Author ecosystem + MCP advocate archetype]]
- [[02 Wiki/(C) MCP Server Directory Structure + Categorization + Scale]]
- [[02 Wiki/(C) Pattern Implications — Awesome-List-Genre consolidation + MCP runtime standardization]]
- [[02 Wiki/(C) Outside-Scope 6th Sub-Type + Storm Bear Meta]]

### Beginner guide

- [[(C) awesome-mcp-servers - Huong dan cho nguoi moi]]

---

## 13. One-page summary

**VN:** v31 awesome-mcp-servers là 3rd awesome-list-genre wiki trong corpus (sau v8 + v25). Phase 4b deliverable này đề xuất consolidation-forward meta-pattern Pattern #68 wrapping cả 3 sub-types (human-directed learning + AI-agent content + AI-runtime infrastructure). Pattern #18 Agent Runtime Standardization strengthens majorly qua v31 là meta-directory của MCP — **promotion candidate ở next audit**. Pattern #50 Commercial-Funnel Companion Platform reaches N=2 structurally-unambiguous (Fiegel + Glama joins VoltAgent + getdesign.md) — **promotion candidate ở next audit**. Ratio post-v31 at 1.00:1 threshold; audit path to 0.70:1 clear via 5 simultaneous promotions. Storm Bear operator relevance HIGH — MCP infrastructure directly usable today.

**EN:** v31 is 3rd awesome-list-genre wiki; proposes meta-pattern consolidation wrapping #35 + #49 + MCP-server-aggregator via 3 audience sub-types. Pattern #18 (MCP runtime standardization) + Pattern #50 (commercial-funnel companion) both become promotion candidates. Ratio 1.00:1 at threshold; audit path to 0.70 clear. Storm Bear infrastructure-usable-today.

---

_Phase 4b deliverable. Storm Bear LLM Wiki v31. Written by Claude (C). 2026-04-22. ~620 lines. 13 sections. Bilingual VN/EN. Cross-refs 6 prior wikis + 2 aggregator peers + 6 MCP-consumer peers + 7 sibling wiki files._
