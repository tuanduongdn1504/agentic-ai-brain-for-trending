# (C) 12 Divisions + 144 Agents Taxonomy cluster summary — agency-agents

> **Sources:** README division list + directory structure + inferred agent examples
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

agency-agents' core value = **144 specialized agents organized into 12 divisions**. This is the largest + most-organized agent taxonomy in Storm Bear corpus. Understanding the division structure reveals the project's product philosophy.

## 2. Full division taxonomy (verbatim from README)

### 12 divisions, 144+ agents total

| # | Division | Agents | % of total |
|---|----------|--------|------------|
| 1 | Engineering | 27 | 19% |
| 2 | Design | 8 | 6% |
| 3 | Paid Media | 7 | 5% |
| 4 | Sales | 9 | 6% |
| 5 | Marketing | 26 | 18% |
| 6 | Product | 5 | 3% |
| 7 | Project Management | 6 | 4% |
| 8 | Testing | 8 | 6% |
| 9 | Support | 6 | 4% |
| 10 | Spatial Computing | 6 | 4% |
| 11 | Specialized | 41 | 28% |
| 12 | Finance | 5 | 3% |
| (13) | Game Development | 20+ | 14% |
| (14) | Academic | 5 | 3% |

**Notes:**
- **14 total divisions visible** (12 named in summary + Game Development + Academic as additional in directory)
- **"Specialized" largest at 41** (catch-all)
- **Engineering + Marketing dominate** at 53 agents (37% combined)
- **Traditional software team coverage** + novel divisions (Game Dev, Spatial, Paid Media)

## 3. Division breakdown analysis

### Software-traditional divisions (8)

These parallel traditional software-company structure:
- Engineering (27)
- Design (8)
- Product (5)
- Project Management (6)
- Testing (8)
- Support (6)
- Sales (9)
- Finance (5)

**Total: 74 agents (51%) covering software-company baseline**

### Marketing-focused divisions (3)

- Marketing (26)
- Paid Media (7)
- (Reddit Community Builder in Marketing)

**Total: 33 agents (23%) covering marketing/growth**

### Novel divisions (3)

- **Game Development** (20+) — unique to agency-agents
- **Spatial Computing** (6) — AR/VR
- **Academic** (5) — research/writing

**Total: ~31 agents (22%)**

### Catch-all

- **Specialized** (41) — edge cases, domain-specific agents not fitting above

**Total: 41 agents (28%)** — largest single division

### Distribution insight

Agency-agents deliberately covers **beyond software** — game dev, marketing, spatial computing, academia. Suggests positioning as "complete agency for any knowledge work" not just software.

## 4. Novel agent types (detailed)

### Whimsy Injector (Design)

**Purpose:** Inject playful/delightful elements into products.

**Governance:** "Every playful element must serve a functional or emotional purpose"

**Corpus significance:** First agent focused on playfulness.

### Reality Checker (Testing)

**Purpose:** Find problems others miss.

**Behavior:** "Defaults to finding 3–5 issues and requires visual proof for everything"

**Corpus significance:** Explicit quality-governance mechanism at agent level.

### Reddit Community Builder (Marketing)

**Purpose:** Authentic community engagement.

**Philosophy:** "You're becoming a valued community member who happens to represent a brand"

**Corpus significance:** Anti-inauthentic-marketing stance encoded in agent.

### Brand Guardian (Design)

**Purpose:** Protect brand consistency.

**Corpus significance:** Cross-agent consistency enforcement.

### Discovery Coach (Sales)

**Purpose:** Help in early customer discovery conversations.

**Corpus significance:** Acknowledges sales is not just closing but discovery.

### Deal Strategist (Sales)

**Purpose:** Close complex deals.

**Corpus significance:** Deal-closing expertise as specialized agent.

## 5. Agent library size comparison

### Corpus agent counts

| Framework | Agent/skill count | Agent definition |
|-----------|-------------------|------------------|
| ECC v1 | ~12 subagents | Specialists |
| Superpowers v2 | 7-stage | Workflow stages |
| gstack v3 | 1 virtual team | Team metaphor |
| GSD v5 | Harness-agnostic | No fixed count |
| BMAD v11 | 12+ agents | Named roles |
| codymaster v12 | 79 skills | Skill library |
| spec-kit v17 | Constitution-driven | Governance not agents |
| **agency-agents v18** | **144+ agents** | **Largest library** |

**agency-agents = 1.8× codymaster v12** (prior largest). 12× BMAD v11.

### Agent definition variance

- BMAD: agents have detailed methodology (BMM modules)
- codymaster: skills have multi-axis classification
- **agency-agents: personality + workflow + examples + metrics** — emphasis on personality

## 6. Personality-driven design (novel T1 choice)

### Philosophy (verbatim)

> "Every agent includes personality traits, domain-specific workflows, code examples, and success metrics."

### What "personality" means

Not just role + responsibilities — distinct character:
- **Whimsy Injector** — playful, creative
- **Reality Checker** — skeptical, rigorous (3-5 issues default)
- **Reddit Community Builder** — authentic, community-focused

### Contrast with other T1

- **BMAD v11:** roles (Amelia, Barry, Quinn, Bob) — names but less personality emphasis
- **codymaster v12:** skills are functional (no personality)
- **spec-kit v17:** no personas, methodology-first
- **agency-agents v18:** personalities are FIRST-class design element

**Corpus first:** personality-driven agent design.

### Pattern candidate #25 — Personality-Driven Agent Design

> "As T1 frameworks compete on differentiation, personality-driven agent design (distinct character + voice) emerges as differentiator beyond role/responsibility definition."

Predict future T1 frameworks will emphasize personality.

## 7. Division organization principles (inferred)

### Organizational pattern

```
Division
  ├── Agent A (specialty 1)
  │   ├── Personality
  │   ├── Workflows
  │   ├── Code examples
  │   └── Success metrics
  ├── Agent B (specialty 2)
  └── ...
```

### Cross-division patterns

- **Engineering + Testing** = software quality pair
- **Design + Marketing** = brand consistency pair
- **Sales + Product** = go-to-market pair
- **Project Management + Support** = operations pair

### Missing integrations (not documented)

- **Cross-agent collaboration patterns** — how do agents coordinate on complex tasks?
- **Hierarchical agent chains** — does Senior agent delegate to Junior?
- **Parallel agent orchestration** — multiple agents for same task?

Pattern candidate: future agency-agents versions may add **orchestration layer** (meta-agent coordinator).

## 8. Examples folder

### Inferred purpose

```
examples/
├── e-commerce/
│   └── ... (using multiple agents for full project)
├── saas-landing/
└── ...
```

**Likely content:** concrete scenarios showing multiple agents coordinating.

### Corpus first

First corpus framework with dedicated examples directory for multi-agent scenarios.

## 9. Integration folder

### Inferred structure

```
integrations/
├── claude-code/
├── cursor/
├── copilot/
└── ... (11+ platform adapters)
```

**Corresponds to 11-platform support** — each platform gets dedicated integration logic + conversion templates.

## 10. Edges + failure modes

### Agent library edges

- **144 agents quality variance** — some deeply specified, some thin
- **Division overlap** — "Specialized" catch-all may duplicate other divisions
- **Maintenance cost** — 144 agents × ongoing updates = significant work
- **Agent discoverability** — no search system; users must browse

### Personality-driven edges

- **Personality overshadowing function** — playful language may hide substance
- **Personality mismatch** — corporate users may resist Whimsy Injector tone
- **Inconsistent tone** across 144 agents (solo maintainer or community contribution)

### Division edges

- **Boundary cases** — is "Content Creator" Marketing or Design?
- **Cross-division coordination** undocumented
- **Division inflation** — Specialized at 41 suggests boundaries unclear

## 11. Corpus-first observations

- **Largest agent library** (144)
- **Most-organized taxonomy** (12-14 divisions)
- **First personality-driven design** at T1
- **First game-development division**
- **First spatial-computing division**
- **First paid-media division**
- **Reality Checker 3-5 issues default** = novel agent-level governance
- **Whimsy Injector purposeful-playfulness** = novel design principle

## 12. Cross-references

- [[(C) README + CONTRIBUTING + zh-CN cluster summary]] — positioning
- [[(C) SECURITY + Governance + Installation Scripts cluster summary]] — distribution
- [[(C) 144 Agent Personalities + 12 Divisions Taxonomy]] (entity)

## 13. Open questions

- Q7: Full 144 agent names?
- Q9: Whimsy Injector actual behavior?
- Q11: Comparison with codymaster 79 skills at agent level?
- Q13: Cross-agent collaboration patterns?
- Q14: Quality control with 144 agents?
- Q20: Agent discovery system?
