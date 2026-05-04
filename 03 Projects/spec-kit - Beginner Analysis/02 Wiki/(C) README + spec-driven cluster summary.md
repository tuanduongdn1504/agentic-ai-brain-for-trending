# (C) README + spec-driven cluster summary — spec-kit

> **Sources:** README.md + spec-driven.md (both from main branch)
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

README = marketing + user-facing positioning. spec-driven.md = methodology manifesto + formal SDD philosophy. Together they define what spec-kit is and why it exists.

## 2. Core positioning (verbatim)

### README tagline

> "💫 Toolkit to help you get started with Spec-Driven Development"

### README anti-thesis

> "An open source toolkit that allows you to focus on product scenarios and predictable outcomes instead of **vibe coding** every piece from scratch."

**Corpus-first:** formal opposition to "vibe coding" — prior corpus frameworks may imply this but spec-kit explicit.

### spec-driven.md philosophical inversion (verbatim)

> "For decades, code has been king — specifications were just scaffolding we built and discarded once the 'real work' of coding began."

> "Spec-Driven Development (SDD) inverts this power structure. Specifications don't serve code—code serves specifications."

> "SDD eliminates the gap by making specifications and their concrete implementation plans born from the specification executable."

### spec-driven.md premise

> "AI capabilities have reached a threshold where natural language specifications can reliably generate working code."

## 3. 7-step workflow (5 core + 2 optional)

### Core slash commands (from README)

| # | Command | Purpose |
|---|---------|---------|
| 1 | `/speckit.constitution` | Establish project principles (governance) |
| 2 | `/speckit.specify` | Create functional specifications |
| 3 | `/speckit.plan` | Generate technical implementation plan |
| 4 | `/speckit.tasks` | Break plan into actionable tasks |
| 5 | `/speckit.implement` | Execute tasks (AI agent does work) |

### Optional commands

| # | Command | Purpose |
|---|---------|---------|
| 6 | `/speckit.clarify` | Resolve underspecified areas |
| 7 | `/speckit.analyze` | Cross-artifact consistency analysis |

### Pattern: slash-namespace convention

`speckit.*` prefix prevents collision with other agent skills. Parallels how graphify v16 uses `/graphify` (single namespace).

## 4. Constitution concept — governance architecture

### Structure (from spec-driven.md)

- **File location:** `memory/constitution.md`
- **9 articles** shape every aspect of development process
- **Function:** "architectural DNA governing specification generation"

### Named articles

| Article | Principle |
|---------|-----------|
| I | Library-first (every feature begins as standalone library) |
| III | Test-first imperative (no implementation before tests) |
| VII | Simplicity |
| VIII | Anti-abstraction |
| II, IV, V, VI, IX | (not specified in README/spec-driven.md excerpts available) |

### Enforcement mechanism (verbatim)

> "These gates act as compile-time checks for architectural principles. The LLM cannot proceed without either passing the gates or documenting justified exceptions."

**Implication:** Constitution = **executable governance**. LLM agent respects articles architecturally, not just advisorially.

### Amendment process

> "Constitutional principles remain immutable while their application evolves through an amendment process requiring explicit documentation and approval."

### Corpus parallel

**paperclip v14** had 5 control-plane invariants (architectural governance).
**spec-kit v17** has 9 articles (architectural governance).

**Pattern #15 (Governance-Depth Correlation)** reinforced at v17:
- v14: autonomy-maximum + heavy governance (paperclip)
- v17: SDD methodology + heavy governance (spec-kit)
- Governance depth correlates with claim-ambition (autonomy OR methodology replacement)

## 5. Executable specifications mechanism

### Productivity claim (verbatim from spec-driven.md)

> "Traditional approach requires ~12 hours of documentation; SDD with commands accomplishes equivalent work in 15 minutes through template-driven generation."

**Ratio:** 48× speedup claimed.

### Corpus context

spec-kit's 48× productivity = 4th research-style benchmark:
- codymaster v12: SkillsBench +18.6pp
- autoresearch v10: val_bpb training metric
- graphify v16: 71.5× token reduction
- **spec-kit v17: 48× documentation-to-implementation speedup**

**Pattern #8 (Empirical Research Emergence) reinforced** — quantitative benchmarks now in 4 framework wikis.

## 6. Intellectual lineage — John Lam

### Acknowledgement (verbatim from README)

> "This project is heavily influenced by and based on the work and research of [John Lam](https://github.com/jflam)."

### Who is John Lam?

- GitHub handle: `jflam`
- Historically: Microsoft principal engineer, IronRuby/IronPython work
- Context: not detailed in spec-kit docs; external research required

### Corpus intellectual-lineage tracking (v17 update)

Pattern #19 candidate (from v16): intellectual-lineage clustering.

**v16 data:**
- Karpathy: 3 touchpoints (vault + autoresearch + graphify)

**v17 addition:**
- John Lam: 1 touchpoint (spec-kit)
- **Diversifies** Pattern #19 — Karpathy not the only influencer

**Pattern #19 refinement:** Intellectual-lineage clustering is REAL, but no single individual dominates. Multiple influence nodes.

### spec-driven.md notably silent on John Lam

Only README acknowledges him. spec-driven.md makes no lineage mention. **Methodology document ahistorical** — presents SDD as newly-enabled by AI, no TDD/BDD/ATDD acknowledgement.

**Gap:** For an official GitHub document, absence of TDD/BDD/ATDD references is notable. Classic software-engineering literature absent.

## 7. 30+ AI agent integrations

### Named in README (14 of 30+)

Claude Code, Gemini CLI, Cursor CLI, Qwen CLI, opencode, Codex CLI, Qoder CLI, Tabnine CLI, Kiro CLI, Pi, Forge, Goose, Mistral Vibe, GitHub Copilot.

### Full list reference

> "Spec Kit works with 30+ AI coding agents" — full list at https://github.github.io/spec-kit/reference/integrations.html

### Corpus comparison — agent ecosystem breadth

| Framework | Integration count | Notes |
|-----------|-------------------|-------|
| ECC v1 | 1 (Claude Code) | Single-platform |
| gstack v3 | 1 (Claude Code) | Single-platform |
| multica v15 | 8 named models | BYO-agent |
| graphify v16 | 15 skill-install paths | Broadest previously |
| **spec-kit v17** | **30+** | **New broadest in corpus** |

**spec-kit doubles graphify** in integration breadth. Corporate GitHub resources enable scale.

### Notable absences (comparison with multica/paperclip/graphify)

| Integration | multica | paperclip | graphify | spec-kit |
|-------------|---------|-----------|----------|----------|
| Claude Code | ✅ | ✅ | ✅ | ✅ |
| OpenClaw | ✅ | ✅ | ✅ | **❌** |
| Hermes | ✅ | ✅ | ✅ | **❌** |

**Pattern #18 test result at v17:** spec-kit does NOT adopt OpenClaw/Hermes despite broadest integration list.

**Interpretation:** OpenClaw + Hermes are **community-platform phenomena**. Corporate-official T1 uses different ecosystem subset. Pattern #18 tier-dependent / archetype-dependent.

## 8. Target audience

### From README

- Greenfield (0-to-1) projects
- Brownfield (legacy modernization)
- Teams seeking "structured AI-assisted development"

### Target contrast (not vs)

- NOT for "vibe coding" workflows
- NOT for ad-hoc prompt-based generation

**Implication:** spec-kit targets **disciplined teams** vs quick experimenters. Enterprise-friendly.

## 9. Installation (verbatim from README)

### Persistent install

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
specify version
```

### One-time usage

```bash
uvx --from git+https://github.com/github/spec-kit.git@vX.Y.Z specify init <PROJECT_NAME>
```

### Upgrade

```bash
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

### Corpus novelty — uv tool install

**First corpus framework using `uv tool install`** (Astral's uv, modern Python packaging).

**Contrast with prior Python-based frameworks:**
- graphify v16: `pip install graphifyy`
- notebooklm-py v7: `pip install notebooklm-py`
- deer-flow v9: standard Python
- **spec-kit v17: `uv tool install`** — modern ecosystem adoption

**Implication:** GitHub officially endorses uv. Potentially drives Python ecosystem shift.

## 10. SDD methodology convergence with GSD v5

### GSD v5 positioning (from earlier wiki)

> "meta-prompting, context engineering, spec-driven development"

### spec-kit v17 positioning

> "Spec-Driven Development" (whole methodology)

### Pattern candidate #21 — SDD Methodology Emergence

Two independent frameworks in corpus treat SDD as core:
- **GSD v5** (2025 — community framework, spec-driven as feature)
- **spec-kit v17** (2026 — GitHub official, spec-driven as whole)

**Hypothesis:** SDD may become **dominant methodology** in T1 Agent-as-assistant tier. Other frameworks (BMAD BMM, Superpowers TDD, GSD spec-driven) already partially aligned.

**Prediction:** Future T1 frameworks likely adopt SDD language. Testable in v18+.

## 11. Spec-driven.md key concepts (additional)

### Intent-driven development

> "The intent of the development team is expressed in natural language ('intent-driven development'), design assets, core principles and other guidelines. The lingua franca of development moves to a higher level, and code is the last-mile approach."

**Reframe:** programming language is no longer primary communication medium. Natural language + specs are.

### Test-first imperative (Article III enforcement)

> "Tests MUST use realistic environments: Prefer real databases over mocks, Use actual service instances over stubs, Contract tests mandatory before implementation."

**Parallel:** Superpowers v2 TDD discipline. spec-kit formalizes at article level.

### Feature branching per spec

`/speckit.specify` creates git branch automatically + assigns feature number. **Workflow-integrated with git**.

## 12. Cross-references

- [[(C) AGENTS + CONTRIBUTING + SECURITY + SUPPORT + DEVELOPMENT + COC cluster summary]] — governance
- [[(C) Integration + Extensions + Packaging cluster summary]] — distribution
- [[(C) Spec-Driven Development methodology + Constitution + 7-step Workflow]] (entity)

## 13. Corpus-first observations

- **First formal anti-vibe-coding stance**
- **First 9-article constitutional governance at T1**
- **First uv tool install usage**
- **First 30+ integration breadth**
- **First official GitHub-organizational T1 framework**
- **First John Lam intellectual-lineage citation**
- **48× productivity claim** (4th research-style benchmark)
- **SDD methodology convergence with GSD v5** (Pattern #21 candidate)
