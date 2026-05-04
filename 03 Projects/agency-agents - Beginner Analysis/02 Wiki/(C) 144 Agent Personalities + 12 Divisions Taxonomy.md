# (C) 144 Agent Personalities + 12 Divisions Taxonomy

> **Type:** Entity — core product
> **Parent:** [[(C) index]]
> **Sources:** [[(C) README + CONTRIBUTING + zh-CN cluster summary]] §4, [[(C) 12 Divisions + 144 Agents Taxonomy cluster summary]] §2-§6
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

agency-agents' core product is **144+ specialized AI agent personalities** organized across **12-14 divisions**. This is the **largest agent library in Storm Bear corpus** (1.8× codymaster v12's 79 skills). Each agent combines personality traits + domain-specific workflows + code examples + success metrics — a **personality-driven design** that distinguishes from codymaster's functional skills or BMAD's methodology-driven roles. Novel division structure includes **Game Development (20+)**, **Spatial Computing (6)**, and **Paid Media (7)** — corpus-firsts — alongside traditional software-team divisions (Engineering 27, Design 8, Product 5, etc.).

## 2. Key claims

1. **144+ agents** — largest agent library in corpus
2. **12-14 divisions** — most-organized taxonomy
3. **Personality-driven design** — novel T1 architectural choice
4. **Engineering + Marketing dominate** — 27 + 26 = 53 agents (37%)
5. **Specialized catch-all** — 41 agents (28%, largest division)
6. **Game Development + Spatial Computing + Paid Media** — 3 corpus-first divisions
7. **Reality Checker + Whimsy Injector** — signature novel agents

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 144+ agents | README verbatim | High |
| 12 divisions | README division table | High |
| Division counts | README | High |
| Personality-driven | README §Each agent includes | High |
| Novel divisions | README + corpus comparison | High |

## 4. Full division taxonomy

### Software-traditional divisions (74 agents, 51%)

| Division | Agents | Notable |
|----------|--------|---------|
| Engineering | 27 | Frontend, Backend, Mobile, DevOps, Security, Architecture |
| Design | 8 | UI/UX + **Whimsy Injector** + **Brand Guardian** |
| Product | 5 | PM, PO, product strategy |
| Project Management | 6 | Scrum coach, project ops |
| Testing | 8 | QA + **Reality Checker** |
| Support | 6 | Customer support, community |
| Sales | 9 | **Discovery Coach** + **Deal Strategist** |
| Finance | 5 | Revenue, accounting |

### Marketing-focused divisions (33 agents, 23%)

| Division | Agents | Notable |
|----------|--------|---------|
| Marketing | 26 | Content Creator + **Reddit Community Builder** |
| Paid Media | 7 | Ad strategy, performance marketing (**corpus first**) |

### Novel divisions (~31 agents, 22%)

| Division | Agents | Notable |
|----------|--------|---------|
| Game Development | 20+ | Game design, level design, narrative (**corpus first**) |
| Spatial Computing | 6 | AR/VR agents (**corpus first**) |
| Academic | 5 | Research, writing, citation |

### Catch-all

| Division | Agents |
|----------|--------|
| Specialized | 41 (28% — largest, corpus edge cases) |

## 5. Agent-level design principles

### Each agent includes (verbatim from README)

1. **Personality traits** — distinct character
2. **Domain-specific workflows** — how agent approaches task
3. **Code examples** — concrete implementation
4. **Success metrics** — measurable outcomes

### Invocation patterns

**Claude Code:**
```
"Use the Frontend Developer agent to review this component."
```

**Antigravity (Gemini):**
```
@agency-frontend-developer review this React component
```

**OpenCode:**
```
@backend-architect design this API.
```

**Cursor:**
```
Use the @security-engineer rules to review this code.
```

**Aider/Windsurf:**
```
Use the [Agent Name] agent to [specific task].
```

## 6. Signature novel agents

### Whimsy Injector (Design)

**Purpose:** Inject playful/delightful elements into products.

**Discipline (verbatim):**
> "Every playful element must serve a functional or emotional purpose."

**Use cases:**
- Loading state animations with personality
- Error messages that are helpful + charming
- Easter eggs that reinforce brand
- Onboarding moments with warmth

**Why novel:** First corpus agent explicitly designed for playfulness-with-purpose. Prior T1 frameworks treat whimsy as out-of-scope.

### Reality Checker (Testing)

**Purpose:** Find problems others miss.

**Behavior (verbatim):**
> "Defaults to finding 3–5 issues and requires visual proof for everything."

**Governance implication:**
- **Agent-level quality gate** — agent mandate generates minimum issues
- **Evidence requirement** — visual proof enforces rigor
- **3-5 issues default** — prevents cursory review

**Corpus significance:** First agent with explicit quantitative quality governance. Parallels paperclip v14's invariant-architecture but at agent behavior level.

### Reddit Community Builder (Marketing)

**Purpose:** Authentic community engagement.

**Philosophy (verbatim):**
> "You're becoming a valued community member who happens to represent a brand."

**Anti-patterns avoided:**
- Astroturfing
- Hard-selling
- Drive-by promotion

**Corpus significance:** First agent with anti-inauthentic-marketing ethic. Notable given agency-agents' own Reddit-viral origin.

### Brand Guardian (Design)

**Purpose:** Protect brand consistency across touchpoints.

**Cross-agent role:** Reviews outputs from other agents (Content Creator, UI Designer) for brand alignment.

## 7. Personality-driven design — Pattern candidate #25

### Formal statement

> "**Pattern #25 — Personality-Driven Agent Design:** T1 frameworks differentiate via agent personality (distinct character + voice + quirks) beyond role/responsibility definition. Personality serves as product differentiation and user engagement."

### Evidence

- **agency-agents v18:** personality first-class; 144 distinct personalities
- **BMAD v11:** agents have names (Amelia, Barry, Quinn, Bob) — some personality hints
- **Other T1:** functional focus (codymaster skills, GSD harness-agnostic, spec-kit methodology)

### Prediction

T1 competition will accelerate personality emphasis. Future T1 frameworks may:
- Hire writers for agent voice
- Develop personality frameworks (Myers-Briggs-style)
- Measure user-agent affinity metrics

### Storm Bear action

Personality-driven agents in Scrum context:
- **Risk:** corporate teams may resist non-professional tone
- **Opportunity:** engagement + memorability boost
- **Guideline:** match agent personality to team culture (casual startup vs corporate enterprise)

## 8. Comparison with corpus agent libraries

### Scale + structure

| Framework | Count | Structure | Personality |
|-----------|-------|-----------|-------------|
| ECC v1 | ~12 | Subagents | Low |
| Superpowers v2 | — | 7-stage workflow | — |
| BMAD v11 | 12+ | Roles/modules | Medium (named) |
| codymaster v12 | 79 | Multi-axis skills | Low (functional) |
| spec-kit v17 | — | Constitution-driven | — |
| **agency-agents v18** | **144** | **12 divisions** | **High (distinct)** |

### Definition style contrast

**codymaster skill** (functional):
```
Skill: frontend-testing
Purpose: Write unit tests for React components
Inputs: Component file
Outputs: Test file
```

**agency-agents agent** (personality):
```
Agent: Whimsy Injector
Personality: Playful, purposeful, detail-obsessed
Workflow: Analyze UX moments → identify opportunity → inject whimsy that serves function
Example: Loading skeleton with gentle animation
Success metric: User engagement +X%
```

**Different product philosophies** — functional vs character-driven.

## 9. Division novelty — 3 corpus-firsts

### Game Development (20+)

**Coverage (inferred):**
- Game designer
- Level designer
- Narrative designer
- Character designer
- Combat systems designer
- Monetization designer
- Playtesting coordinator
- (etc.)

**Significance:** First corpus framework with substantial game-dev focus. Expands T1 beyond software/tech.

### Spatial Computing (6)

**Coverage (inferred):**
- AR designer
- VR developer
- Spatial UX
- 3D modeling
- (etc.)

**Significance:** First corpus AR/VR focus. Future-ready.

### Paid Media (7)

**Coverage (inferred):**
- Paid search strategist
- Paid social expert
- Ad copy
- Creative performance
- Attribution analyst
- (etc.)

**Significance:** First corpus paid-media specialization. Marketing agents previously generic.

## 10. Related concepts

- [[(C) 11-Platform Install + OpenClaw 5th Wiki Validation]] — distribution
- [[(C) Solo-at-Enterprise-Scale + Reddit Community Origin + Pattern 20 Revision]] — organizational
- [[(C) T1 8-way + Agent Persona Library + Pattern 19 No-Lineage + Storm Bear]] — tier meta

## 11. Edges + failure modes

### Library scale edges

- **144 agents quality variance** — some thin, some deep
- **Specialized division (41 agents) overlap** — boundary with other divisions unclear
- **Maintenance burden** — solo maintainer updates 144 agents over time
- **Agent discoverability** — no search system; browse-only

### Personality edges

- **Tone mismatch** — corporate clients resist Whimsy Injector
- **Inconsistent personality** across 144 (quality drift)
- **Cultural bias** — Reddit Community Builder assumes Western/English communities

### Division edges

- **Boundaries unclear** — Content Creator in Marketing or Design?
- **Division inflation** — Specialized at 41 = catch-all leaks
- **Cross-division collaboration** undocumented

## 12. Decision log

- **Initial:** Reddit thread origin → seed agents
- **Iteration:** months of community feedback
- **Current:** 144 agents across 12-14 divisions
- **Future:** may add orchestration layer (multi-agent coordination); LLC formalization; commercial offering

## 13. References

- README division table
- Novel agent examples (Whimsy Injector, Reality Checker, Reddit Community Builder)
- Parent: [[(C) index]]
- Cross-wiki: `../../codymaster - Beginner Analysis/02 Wiki/(C) 79 Skills Library.md` (prior largest library)
- Cross-wiki: `../../BMAD-METHOD - Beginner Analysis/02 Wiki/(C) 12 Agents Architecture.md` (role-based precedent)
