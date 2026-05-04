# (C) Spec-Driven Development methodology + Constitution + 7-step Workflow

> **Type:** Entity — core methodology
> **Parent:** [[(C) index]]
> **Sources:** README.md §What is Spec-Driven Development + spec-driven.md §Philosophy + Workflow
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

Spec-kit's core product is **Spec-Driven Development (SDD)** — a methodology that **inverts the traditional code/spec relationship**: specifications become executable primary artifacts, code becomes generated secondary output. Operationalized through a **7-step slash-command workflow** (`/speckit.constitution → specify → plan → clarify → tasks → analyze → implement`) enforced by a **9-article constitution** that acts as "compile-time checks" — the LLM cannot proceed without passing gates or documenting justified exceptions. SDD targets disciplined teams opposing "vibe coding" and claims **48× productivity speedup** (~12 hours → 15 minutes) on equivalent documentation-to-implementation work.

## 2. Key claims

1. **SDD inverts power structure** — "code serves specifications" (not reverse)
2. **Specifications are executable** — generate working systems directly
3. **9-article constitution** governs entire process (architectural DNA)
4. **Template checkpoints act as gates** — LLM cannot bypass without documented exceptions
5. **7-step workflow** — constitution → specify → plan → clarify → tasks → analyze → implement
6. **48× productivity claim** — 12h → 15min for documentation-to-implementation
7. **Anti-vibe-coding explicit** — formal methodology opposition
8. **Git-integrated** — each spec gets a branch via `/speckit.specify`

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| SDD inverts code-vs-spec | spec-driven.md §Philosophy verbatim | High |
| 9 constitution articles | spec-driven.md §Constitution verbatim | High |
| Article enforcement via gates | spec-driven.md §Enforcement verbatim | High |
| 48× speedup | spec-driven.md productivity claim | High (claim) / Medium (methodology not published) |
| 7-step workflow | README commands table | High |
| Git branching per spec | README workflow description | High |

## 4. Philosophy — verbatim from spec-driven.md

### The inversion

> "For decades, code has been king — specifications were just scaffolding we built and discarded once the 'real work' of coding began. Spec-Driven Development (SDD) inverts this power structure. Specifications don't serve code—code serves specifications."

### The mechanism

> "SDD eliminates the gap by making specifications and their concrete implementation plans born from the specification executable."

### The premise

> "AI capabilities have reached a threshold where natural language specifications can reliably generate working code."

### Intent-driven development

> "The intent of the development team is expressed in natural language ('intent-driven development'), design assets, core principles and other guidelines. The lingua franca of development moves to a higher level, and code is the last-mile approach."

### Productivity claim

> "Traditional approach requires ~12 hours of documentation; SDD with commands accomplishes equivalent work in 15 minutes through template-driven generation."

## 5. Constitution architecture (9 articles)

### File location

`memory/constitution.md` — inside project.

### Function

> "Architectural DNA governing specification generation"

### Named articles

| Article | Principle | Implication |
|---------|-----------|-------------|
| **I** | **Library-first** — every feature begins as standalone library | Forces modular design; no monolithic feature code |
| **III** | **Test-first imperative** — no implementation before tests | TDD discipline encoded at constitutional level |
| **VII** | **Simplicity** | Anti-complexity constraint |
| **VIII** | **Anti-abstraction** | Pragmatic over "enterprise" patterns |
| II, IV, V, VI, IX | (not detailed in available excerpts) | Likely: modularity, documentation, versioning, integration, etc. |

### Enforcement — gates

> "These gates act as compile-time checks for architectural principles. The LLM cannot proceed without either passing the gates or documenting justified exceptions."

### Amendment process

> "Constitutional principles remain immutable while their application evolves through an amendment process requiring explicit documentation and approval."

**Parallel to paperclip v14 invariants:** both use **constitutional architecture** — invariants at governance level, LLM/runtime respects them structurally.

## 6. 7-step workflow

### Core commands (5)

```
1. /speckit.constitution      — Establish project principles
2. /speckit.specify          — Create functional specifications
3. /speckit.plan             — Generate technical implementation plan
4. /speckit.tasks            — Break into actionable tasks
5. /speckit.implement        — Execute (AI agent does the work)
```

### Optional commands (2)

```
6. /speckit.clarify          — Resolve underspecified areas
7. /speckit.analyze          — Cross-artifact consistency analysis
```

### Workflow diagram

```
┌───────────────────────────┐
│  /speckit.constitution    │  ← Project principles (9 articles)
└────────────┬──────────────┘
             ↓
┌───────────────────────────┐
│  /speckit.specify         │  ← Functional spec + auto-git-branch
└────────────┬──────────────┘
             ↓  (optional)
┌───────────────────────────┐
│  /speckit.clarify         │  ← Resolve ambiguities
└────────────┬──────────────┘
             ↓
┌───────────────────────────┐
│  /speckit.plan            │  ← Technical implementation plan
└────────────┬──────────────┘
             ↓
┌───────────────────────────┐
│  /speckit.tasks           │  ← Actionable task list with parallelization markers
└────────────┬──────────────┘
             ↓  (optional)
┌───────────────────────────┐
│  /speckit.analyze         │  ← Cross-artifact consistency check
└────────────┬──────────────┘
             ↓
┌───────────────────────────┐
│  /speckit.implement       │  ← AI agent executes tasks
└───────────────────────────┘
```

### Namespace

`speckit.*` prefix prevents slash-command collision with other agent skills. Parallels graphify `/graphify`, BMAD `/bmad-*`, etc.

## 7. Worked example — adding auth feature

### Context

New greenfield project. Team wants to add JWT authentication.

### Step-by-step

```bash
# 1. Establish principles
/speckit.constitution
# → AI asks about code quality, testing, UX standards
# → memory/constitution.md created with 9 articles tailored to project

# 2. Specify the feature
/speckit.specify "Add JWT authentication with refresh tokens"
# → Git branch `001-jwt-auth` created
# → spec.md generated with functional requirements

# 3. Clarify (optional)
/speckit.clarify
# → AI asks: "Should refresh tokens be single-use or reusable?"
# → User answers; spec.md updated

# 4. Plan
/speckit.plan
# → plan.md generated: architecture, dependencies, sequence diagram

# 5. Tasks
/speckit.tasks
# → tasks.md generated with parallelization markers:
#    [P1] Install JWT libraries
#    [P1] Create User model
#    [P2] Implement /login endpoint
#    [P2] Implement /refresh endpoint
#    [P3] Add auth middleware
#    [P3] Write contract tests

# 6. Analyze (optional)
/speckit.analyze
# → Cross-checks: spec vs plan vs tasks consistency
# → Flags: "tasks.md mentions middleware not in plan.md"
# → User revises

# 7. Implement
/speckit.implement
# → AI executes tasks sequentially
# → Generates code, writes tests first (Article III)
# → Commits per task
```

### Expected outcome

JWT auth implemented in ~15 minutes (vs ~12 hours traditional) — per spec-kit's productivity claim.

## 8. Edges + failure modes

### Philosophical edges

- **Specification completeness gap** — SDD assumes natural-language specs are complete. Incomplete specs → wrong code.
- **Specification precision gap** — English ambiguity persists; `/speckit.clarify` partial mitigation
- **AI capability assumption** — "AI reliably generates from natural language" is hypothesis, not proven at all scales
- **48× productivity claim** — no methodology published; numbers self-reported

### Constitutional edges

- **Article conflicts** — library-first (I) vs simplicity (VII) may tension
- **Amendment process undefined** — who approves? committee? BDFL?
- **Article IX unknown** — partial article list available
- **Gate bypass with "documented exception"** — can be abused

### Workflow edges

- **Git branch explosion** — 100 specs = 100 branches; cleanup discipline needed
- **Tasks parallelization markers** — quality depends on LLM reasoning
- **Consistency analysis (optional)** — if skipped, downstream artifacts drift
- **Implement step trusts prior artifacts** — errors compound downstream

### Team-adoption edges

- **Learning curve** — 7 commands + constitution = non-trivial onboarding
- **Skeptics** — "vibe coding" practitioners may reject methodology
- **Documentation overhead** — SDD is heavy up-front even if total time less

## 9. Related concepts

- [[(C) 30+ Platform Integration + 80+ Community Extensions Marketplace]] — distribution
- [[(C) GitHub-Official Corporate Backing + T1 Corporate-vs-Community Bifurcation]] — organizational
- [[(C) T1 7-way + SDD Convergence + Intellectual Lineage Diversification + Storm Bear]] — tier meta

## 10. Cross-project comparison

### SDD across corpus

| Framework | SDD positioning | Depth |
|-----------|-----------------|-------|
| **GSD v5** | "meta-prompting, context engineering, **spec-driven development**" | Feature-level |
| **spec-kit v17** | "Toolkit for **Spec-Driven Development**" | Whole methodology |
| BMAD v11 | BMM (BMAD Method) | Separate methodology |
| Superpowers v2 | TDD 7-stage | Adjacent (test-driven) |
| codymaster v12 | "vibe coding framework" | **Opposite direction** — embraces vibe coding |

**Pattern candidate #21 — SDD Methodology Emergence:** 2 independent frameworks (GSD v5 + spec-kit v17) in corpus center SDD. **If GSD v5 predates spec-kit, influence direction unclear.** Worth investigating.

### vs BMAD v11 methodology

| Aspect | BMAD BMM | spec-kit SDD |
|--------|----------|--------------|
| Scope | Multiple modules (BMM/BMB/TEA/BMGD/CIS) | Single SDD-centered |
| Governance | Implicit (methodology as guidance) | Explicit (9 constitutional articles) |
| Autonomy | Human Amplification, Not Replacement | Disciplined AI collaboration |
| Scale | 45K stars | 89.2K stars (2×) |
| Corporate backing | LLC | Official GitHub |

### vs paperclip v14 constitutional governance

| Aspect | paperclip v14 | spec-kit v17 |
|--------|---------------|--------------|
| Governance | 5 invariants + 4 primitives | 9 articles + amendment |
| Tier | T5 (app) | T1 (assistant) |
| Target | "Zero-human companies" | "Disciplined AI collaboration" |
| Governance depth | Very heavy | Very heavy |

**Pattern #15 (Governance-Depth Correlation) reinforced** — both are ambitious-claim frameworks with constitutional governance.

## 11. Open questions

- Q3: Constitution enforcement in practice — how rigorously does LLM respect articles?
- Q4: Single file or multiple files for constitution?
- Q5: John Lam's specific SDD contribution?
- Q11: spec-driven.md as formal spec vs methodology essay?
- Q21: Influence direction between GSD v5 SDD and spec-kit v17 SDD?
- Q22: John Lam's published SDD writings?

## 12. Decision log

- **Pre-v0.1:** John Lam's research influenced
- **v0.1-0.5:** Initial SDD methodology + basic commands
- **v0.6:** Constitution architecture + 9 articles
- **v0.7.x current:** Full 7-step workflow + 30+ agent integrations
- **Future:** likely Copilot deep integration + enterprise features

## 13. References

- README.md §What is Spec-Driven Development + §Commands
- spec-driven.md §Philosophy + §Constitution + §Workflow
- Parent: [[(C) index]]
- Cross-wiki: `../../get-shit-done - Beginner Analysis/02 Wiki/(C) index.md` (SDD convergence)
- Cross-wiki: `../../paperclip - Beginner Analysis/02 Wiki/(C) Zero-Human Companies Orchestration + Governance Layer.md` (constitutional governance parallel)
