# (C) AGENTS + CONTRIBUTING + SECURITY + SUPPORT + DEVELOPMENT + COC cluster summary — spec-kit

> **Sources:** AGENTS.md + CONTRIBUTING.md + SECURITY.md + SUPPORT.md + DEVELOPMENT.md + CODE_OF_CONDUCT.md (main branch)
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

6 governance documents at repo root = **most comprehensive corporate open-source governance set in corpus**. Together they define how GitHub (organization) formalizes spec-kit contribution + extension + security workflows.

### Corpus context

| Framework | Governance files |
|-----------|------------------|
| ECC v1 | minimal |
| Superpowers v2 | README only |
| BMAD v11 | CONTRIBUTING + limited |
| codymaster v12 | README + limited |
| multica v15 | CLAUDE + AGENTS + CONTRIBUTING (3-file) |
| graphify v16 | AGENTS + SECURITY (2-file) |
| gws v13 | CLAUDE + AGENTS + CONTEXT (tri-file) |
| **spec-kit v17** | **AGENTS + CONTRIBUTING + SECURITY + SUPPORT + DEVELOPMENT + COC (6-file)** |

**Pattern #12 (Corporate formalizes agent docs) confirmed at T1 corporate level.** v13 observation (gws) now joined by v17 (spec-kit) — both corporate-official.

## 2. AGENTS.md — integration contributor guide

### Purpose

**Contributor guide for adding new AI agent integrations to Specify CLI framework.**

Not an agent-usage guide (contrast with graphify v16 AGENTS.md which instructs agents how to use the tool).

### Architecture — modular integration system

Each agent integration is a **self-contained subpackage** under:

```
src/specify_cli/integrations/<agent-key>/
```

Extends a base class and registers itself in global `INTEGRATION_REGISTRY`.

### 4 base class options

Contributors pick based on agent's config format:

| Base class | Format |
|------------|--------|
| `MarkdownIntegration` | Markdown-based (most CLI agents) |
| `TomlIntegration` | TOML config (some agents) |
| `YamlIntegration` | YAML config (some agents) |
| `SkillsIntegration` | Skill-based (Claude Code-style) |
| `IntegrationBase` | Fully custom |

### Required metadata per integration

- `key` — matches CLI executable name
- `config` — agent metadata
- `registrar_config` — command output format
- `context_file` — path to agent instructions (e.g., `AGENTS.md`, `CLAUDE.md`)

### Argument placeholder convention

Format-specific:
- `$ARGUMENTS` — Markdown agents
- `{{args}}` — TOML/YAML agents
- `{SCRIPT}` — script paths

### AGENTS.md format convention note

**spec-kit references `AGENTS.md` as a convention** for agent context files (used by Codex, Goose, Forge, others). Does NOT define the AGENTS.md format formally — treats it as **de facto industry convention**.

**Corpus insight:** AGENTS.md appears to be emerging as **cross-framework industry convention** (not single-project invention). Pattern #22 candidate?

## 3. CONTRIBUTING.md — corporate open-source governance

### Workflow overview

1. Fork repository
2. `uv sync --extra test` — install dev dependencies
3. Create focused branch
4. Add tests
5. Validate locally
6. Submit PR

### Conversation-first requirement (verbatim)

> "Pull requests with large changes that did not have a prior conversation and agreement will be closed."

**Corporate-style policy:** prevents drive-by PRs. Forces issue-first discussion.

### Testing requirements

- Automated: `pytest` for agent configuration consistency
- Manual: test affected slash commands through agent interface
- Reporting template: pass/fail status required
- Prerequisite ordering: `/speckit.specify` before `/speckit.plan`, etc.

### AI disclosure policy (corpus-first)

**Verbatim:**
> "If you are using any kind of AI assistance...this must be disclosed in the pull request or issue"

**Enforcement:**
> "Maintainers reserve authority to close untested or low-effort AI-generated submissions"

**Corpus significance:**
- **First framework with formal AI-disclosure policy** in corpus
- GitHub organization's stance on AI-assisted contributions
- Sets corporate precedent for other projects

**Pattern candidate #23** — AI-Disclosure Policy Emergence. As frameworks themselves are AI-assisted products, meta-policy on AI-assisted contributions may become standard.

## 4. SECURITY.md — vulnerability disclosure

### Standard GitHub pattern

- Private vulnerability reporting via GitHub Security Advisories
- Response SLA expectations
- Coordinated disclosure policy

### Corpus context

- graphify v16: first SECURITY.md standalone
- **spec-kit v17: second; standard GitHub corporate pattern**

SECURITY.md adoption rate in corpus: 2/17 wikis → ~12% adoption. Rising trend.

## 5. CODE_OF_CONDUCT.md — community conduct standard

### Likely Contributor Covenant

GitHub's default for open-source projects. Defines:
- Acceptable behavior
- Unacceptable behavior
- Enforcement mechanism
- Reporting contacts

### Corpus context

First COC at repo root in corpus? Prior wikis didn't foreground COC. spec-kit's corporate formality includes COC prominently.

## 6. SUPPORT.md — user support pathways

### Likely content

- Where to ask questions (GitHub Issues / Discussions)
- Response expectations
- Community vs official support boundary

### Corpus first

**First SUPPORT.md in corpus.** Corporate formality — defines user-expectation management.

## 7. DEVELOPMENT.md — internal development workflow

### Likely content

- Local development setup
- Testing approach
- Release process
- Internal conventions

### Corpus first at T1

First T1 wiki with DEVELOPMENT.md. Common in enterprise open-source but new in Storm Bear corpus.

## 8. Governance architecture comparison

### vs paperclip v14 (T5 constitutional governance)

| Aspect | paperclip v14 | spec-kit v17 |
|--------|---------------|--------------|
| Governance depth | 5 invariants + 4 primitives | 9 constitutional articles |
| Governance model | Architectural invariants | Constitutional + amendment process |
| Documentation | SAFETY.md absent | COC + SUPPORT + SECURITY + DEVELOPMENT |
| Autonomy framing | Zero-human companies | Disciplined AI collaboration |
| Corporate | Unknown (community-platform hypothesis) | Official GitHub |

**Pattern #15 (Governance-Depth Correlation) refined:** governance depth correlates with ambitious methodology claims (autonomy OR SDD), not autonomy alone.

### vs multica v15 (T2 cross-platform rules)

| Aspect | multica v15 | spec-kit v17 |
|--------|-------------|--------------|
| Rules-as-documentation | 5 cross-platform + 5 desktop-specific | 9 constitutional articles |
| Enforcement | Developer discipline | LLM architectural gates |
| Scope | Single-project codebase rules | Any-project governance |

## 9. Corporate signals from cluster

### Signal list

1. **6-file governance set** — most comprehensive in corpus
2. **AI disclosure policy** — corpus-first formal
3. **"Prior conversation" requirement** — gate on PRs
4. **AGENTS.md as modular architecture** — 4 base classes + registry
5. **uv sync dev dependencies** — modern Python stack
6. **Python-specific AGENTS.md** (contributor not user) — mature project organization

### Governance-depth claim

**spec-kit has heaviest open-source governance architecture** in corpus:
- Constitutional principles (9 articles) — methodology
- Contribution policy (conversation-first, AI-disclosure) — operations
- Security policy (vulnerability handling) — security
- Conduct code (community norms) — culture
- Development guide (internal workflow) — engineering
- Support pathways (user expectations) — community

**Implication:** GitHub treats spec-kit as **serious enterprise open-source** project. Not a side experiment.

## 10. Extension governance disclaimer

### README verbatim

> "Community extensions are independently created and maintained by their respective authors. GitHub and the Spec Kit maintainers may review pull requests that add entries to the community catalog for formatting, catalog structure, or policy compliance, but they do **not review, audit, endorse, or support the extension code itself**."

### Corporate-hands-off pattern

- GitHub catalogs but doesn't vet
- Parallel to npm / pypi / cargo marketplaces
- Liability boundary

**Corpus novelty:** first explicit corporate extension-governance disclaimer. BMAD v6.3 emerging marketplace didn't have this formality.

## 11. Edges + failure modes

### Governance edges

- **9 articles may conflict** — library-first (I) vs simplicity (VII) tension
- **Amendment process unclear** — who approves? (single maintainer? committee?)
- **AI disclosure enforcement** — self-report → unverifiable

### Contribution edges

- **"Prior conversation" gate** — may slow community contribution
- **Low-effort closure** — discretionary; could be applied inconsistently
- **AI-disclosure loophole** — hybrid AI+human work may underreport

### Integration edges

- **30+ integrations maintenance burden** — each platform evolves
- **Base-class choice mistakes** — picking wrong base = rewrite later
- **Registry conflicts** — two agents with same `key` = collision

## 12. Cross-references

- [[(C) README + spec-driven cluster summary]] — methodology
- [[(C) Integration + Extensions + Packaging cluster summary]] — distribution
- [[(C) GitHub-Official Corporate Backing + T1 Corporate-vs-Community Bifurcation]] (entity)

## 13. Corpus-first observations

- **Most comprehensive corporate open-source governance** (6-file set)
- **First formal AI-disclosure policy**
- **First modular integration architecture** (4-base-class + registry)
- **First extension-governance disclaimer** at scale (80+ extensions + corporate hands-off)
- **Pattern #12 (Corporate formalizes agent docs) at T1** — v13 (T4 gws) now joined by v17 (T1 spec-kit)
