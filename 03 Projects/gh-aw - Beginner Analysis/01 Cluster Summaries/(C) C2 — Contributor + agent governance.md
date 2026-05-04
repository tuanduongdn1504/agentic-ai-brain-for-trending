# (C) Cluster 2 — Contributor + agent governance

> **Wiki #48 · gh-aw** | **2026-04-25** | Sources: AGENTS.md (49.8 KB) / CONTRIBUTING.md (27.8 KB) / DEVGUIDE.md (38 KB) / DEADCODE.md (218 lines) / CODEOWNERS / CODE_OF_CONDUCT / 24 skill subdirs / scratchpad/ (63 engineering notes) / .github/ workflows + agents config

## Governance file inventory (CORPUS-RECORD-TIER 12+ files)

| File | Size | Purpose |
|------|------|---------|
| **AGENTS.md** | **49.8 KB / 1,240 lines** | **CORPUS-LARGEST AGENTS.md** — primary agent doc; build commands + testing patterns + GitHub MCP usage + console formatting + debug logging + CLI command patterns + validation complexity guidelines |
| README.md | 21 KB / 988 lines | User-facing (988 lines, 86% community attribution) |
| CONTRIBUTING.md | 27.8 KB / 621 lines | Contribution model: "Traditional Pull Requests Are Not Enabled for non-Core team members" |
| DEVGUIDE.md | 38 KB / 1,193 lines | Developer guide companion to AGENTS.md |
| DEADCODE.md | 218 lines | Dead-code policy + how to mark + when to remove |
| SECURITY.md | 65 lines | Security reporting (opensource-security@github.com) + SBOM (SPDX + CycloneDX) generation |
| SUPPORT.md | 11 lines | Support routing |
| SKILL.md | 39 lines | Mini-skill self-description for external coding agents |
| CHANGELOG.md | (long) | Release notes; documents `githubnext/gh-aw` → `github/gh-aw` migration at v0.40.1 |
| CODEOWNERS | 6 lines | 4 maintainers: `@dsyme @eaftan @pelikhan @krzysztof-cieslak` |
| CODE_OF_CONDUCT.md | (standard) | GitHub standard CoC |
| LICENSE | (MIT) | MIT |
| **`.architecture.yml`** | **10 lines** | **CORPUS-FIRST: explicit architectural-threshold manifest** — file-line BLOCKER (2000) + WARNING (1000) + function-line WARNING (200) + max-exports INFO (10) |

**Pattern #12 Governance-Depth refined v42 3-factor model verdict:** github-corporate-official + heavy-governance — **5th counter-evidence to original "solo→light" prediction** (joining claude-hud + pi-mono + ruflo + aidevops). v42 refined formulation (maturity-ambition + maintainer-philosophy + scale-tier) HOLDS strongly.

## CODEOWNERS = research-cluster lineage signal

```text
- @dsyme @eaftan @pelikhan @krzysztof-cieslak
```

| Maintainer | Identity | GitHub Next role | Prior corpus presence |
|------------|----------|------------------|----------------------|
| **@dsyme** | **Don Syme** | F# language creator; GitHub Next researcher | **CORPUS-FIRST** |
| **@eaftan** | Eric Aftandilian | Engineering lead | CORPUS-FIRST |
| **@pelikhan** | **Peli de Halleux** | "Peli's Agent Factory" namesake; researcher | **CORPUS-FIRST** |
| **@krzysztof-cieslak** | **Krzysztof Cieślak** | Ionide (F# IDE for VS Code) creator; researcher | **CORPUS-FIRST** |

= **CORPUS-FIRST GitHub Next 4-researcher cluster lineage** at github-corporate-official tier. Pattern #19 archetype 2 methodology-lineage strengthening: research-org-cluster as observable lineage type (analogous to Anthropic-team-cluster precedent at v34/v47, but for github-mainline-graduated research project).

**Don Syme is structurally significant** — F# language creator (originally at Microsoft Research, joined GitHub Next). His presence at gh-aw CODEOWNERS signals serious-language-design DNA in agentic-workflow-compiler architecture.

## CONTRIBUTING.md inverse-PR governance (corpus-first)

Verbatim opening warning:
> *"⚠️ IMPORTANT: This project uses agentic development by a core team (inner-circle) primarily using Copilot coding agent or local coding agents."*
>
> *"🚫 Traditional Pull Requests Are Not Enabled for non-Core team members: If you are not part of the core team, please do not create pull requests directly. Instead, you create detailed agentic plans in issues, discuss with the team, and a core team member will create and implement the PR for you using agents."*

**Contribution model:**
1. Non-core: Open issue with **detailed agentic plan** (analysis + implementation plan + step-by-step instructions for the agent to follow)
2. Core team member adopts plan + executes via Copilot coding agent or local agent
3. Plan-author credited in README community-contributions section (this is why README has 86% attribution)

**Why this approach** (verbatim):
- *"Consistency: All changes go through the same automated quality gates"*
- *"Dogfooding: We use our own tools to build our tools"*
- *"Best practices: Agents follow established patterns and guidelines automatically"*
- *"Quality plans: Encourages contributors to think through the full implementation before work begins"*

= **CORPUS-FIRST inverse-PR governance** = corporate-official agentic-development model where humans craft plans + agents execute. Within Pattern #69 Agent-PR Fast-Track Governance Protocol scope as **inverse observation**: where #69 documented contributor-fast-track (`🤖🤖🤖`) + maintainer-approval (`lgtm`/`lgtmi`), gh-aw observes maintainer-only-PR + contributor-plan-only with attribution-as-credit.

**CORPUS-FIRST Codespace/Dev-Container-only contributor environment**:
> *"⚠️ Generic dev environments (e.g. manually installed Node.js, Go, or other tools) are not supported. This project is designed to be developed inside a Dev Container or GitHub Codespace."*

= corporate-binding-of-contributor-environment to GitHub's own Codespaces product (dogfooding extension).

## AGENTS.md highlights (selected from 1,240 lines)

### MANDATORY agent instructions

```markdown
🚨 IF YOU ARE THE GITHUB COPILOT CODING AGENT AND YOU HAVE FILE CHANGES,
   YOU MUST ALWAYS CREATE A PULL REQUEST - NO EXCEPTIONS.

🚨 BEFORE EVERY COMMIT - NO EXCEPTIONS:
   make agent-finish  # Runs build, test, recompile, fmt, lint
```

### gh-aw vs GitHub Copilot CLI clarity

> *"`gh-aw` is a GitHub CLI extension (`gh aw`) that compiles markdown workflows into GitHub Actions. It is **not** the GitHub Copilot CLI (`copilot` command). While workflows can use the Copilot CLI as an AI engine, gh-aw itself is a separate tool for workflow management and compilation."*

= **CORPUS-FIRST product-disambiguation-from-sibling-product** at corporate-official tier. Reflects portfolio-internal-naming-collision risk.

### Skills usage discipline ("BE LAZY")

> *"Skills in `skills/` provide detailed, specialized knowledge about specific topics. Only reference skills when you actually need their specialized knowledge. Do not load or reference skills preemptively."*

= **CORPUS-FIRST progressive-skill-loading discipline** (BE LAZY) at corporate-official tier. Distinct from claude-howto v32 lookup-on-demand and codymaster v12 79-skill library — gh-aw explicit non-preemptive principle.

### Skill optimizer daily workflow

> *"The daily skill-optimizer workflow uses the committed config at `.skill-optimizer/skill-optimizer.json`. When tuning optimizer behavior (models, maxTasks, maxIterations, pass-rate target), update this file directly in a PR so changes are reviewable."*

= **CORPUS-FIRST self-improving-skill-system at corporate-official tier**: gh-aw uses agentic workflows to optimize its own skills daily. Dogfooding meta-layer.

### Cross-cutting Go discipline

- File-line target 100-200 / hard 300 (validators)
- Function-line WARNING 200 / file BLOCKER 2000 (`.architecture.yml`)
- Console-formatting required (custom `pkg/console` package)
- Debug logging via custom `pkg/logger` (DEBUG=* env-var pattern)
- Build tags MANDATORY on test files (`//go:build !integration` / `//go:build integration`)
- 6-test-domain organization (unit / integration / security / etc.)

## skills/ directory (24 specialized skill subdirs)

Each skill follows Anthropic-skill format: `skills/<name>/SKILL.md` with YAML frontmatter (`name:` + `description:`).

| Skill | Domain |
|-------|--------|
| custom-agents | Custom agent creation patterns |
| error-messages | Error message conventions |
| reporting | Report generation patterns |
| developer | Developer workflow guidance |
| documentation | Doc-writing standards |
| error-pattern-safety | Defensive error handling |
| messages | Message formatting |
| github-script | github-script Action usage |
| error-recovery-patterns | Recovery patterns |
| gh-agent-session | Agent session management |
| temporary-id-safe-output | Safe-output ID conventions |
| **github-mcp-server** | **GitHub MCP server documentation** (auto-generated by daily workflow) |
| http-mcp-headers | HTTP MCP header patterns |
| skillz-integration | Integration with skillz tooling |
| console-rendering | Console rendering library |
| dictation | Dictation (voice?) |
| github-copilot-agent-tips-and-tricks | Copilot-agent-specific patterns |
| gh-agent-task | Agent-task patterns |
| github-pr-query | PR querying patterns |
| github-issue-query | Issue querying patterns |
| javascript-refactoring | JS refactoring guidance |
| github-discussion-query | Discussion querying patterns |
| (24 total) | |

= **CORPUS-FIRST skills-as-architectural-component at corporate-official tier**. Distinct from codymaster v12 79-skill library (T1 assistant; broader-scope) and claude-howto v32 50+-template library (T1 tutorial; broader-scope). gh-aw skills are **engineering-domain-focused** (each skill = one engineering surface).

## scratchpad/ directory (63 engineering notes)

Sample notes (illustrating engineering depth):
- `architecture.md` / `engine-architecture-review.md` / `engine-review-summary.md` — engine architecture documentation
- `actions.md` — Actions integration
- `adding-new-engines.md` — engine extensibility guide
- `agent-container-testing.md` — container testing patterns
- `agent-sessions.md` — session management
- `breaking-cli-rules.md` — when to break CLI conventions
- `capitalization.md` — capitalization conventions
- `cli-command-patterns.md` — CLI command design
- `code-organization.md` — code organization guidance
- `debugging-action-pinning.md` — debugging action SHA pinning
- `end-to-end-feature-testing.md` — E2E testing
- `errors.md` / `error-recovery-patterns.md` — error handling
- `firewall-log-parsing.md` — AWF log parsing
- `functional-patterns.md` — functional programming patterns (notable: Don Syme F# influence visible)
- `github-actions-security-best-practices.md` — security best practices
- `github-mcp-access-control-specification.md` — MCP access control spec
- `github-rate-limit-observability.md` — rate-limit observability
- `go-type-patterns.md` — Go type patterns
- `gosec.md` — gosec linter usage
- `guard-policies-specification.md` — guard policy spec
- (43 more)

= **CORPUS-FIRST 63-engineering-note scratchpad/ directory at corporate-official tier**. Distinct from typical `docs/architecture/` patterns — these are working-engineering-documents not finalized docs. Represents living engineering-decision-record at extreme breadth.

## .github/ subdirectory (corporate-official tier configuration)

```
.github/
├── actionlint.yaml         # actionlint configuration
├── agents/                 # Agentic-workflows agents (gh aw init creates this)
├── aw/                     # AW workflow specs (catalog of named workflows)
├── copilot/                # Copilot configuration
├── dependabot.yml          # Dependabot configuration
├── mcp.json                # MCP server configuration (gh aw init creates this)
├── shared/                 # Shared workflow components
├── skills/                 # Skills configuration
├── smoke-tests/            # Smoke tests
├── workflows/              # 201 paired *.md + *.lock.yml workflows
├── vet/                    # Vet configuration
├── zizmor.yml              # zizmor (GitHub Actions linter) configuration
```

`.github/aw/` contains 24 named workflow specs:
- `agentic-chat.md` / `campaign.md` / `charts.md`
- `create-agentic-workflow.md` / `update-agentic-workflow.md` / `debug-agentic-workflow.md` / `upgrade-agentic-workflows.md`
- `dependabot.md` / `deployment-status.md`
- `github-agentic-workflows.md` / `github-mcp-server.md`
- `memory.md` / `messages.md` / `network.md`
- `releases.json` / `releases.schema.json`
- `report.md` / `runbooks/`
- `serena-tool.md` (= integration with `oraios/serena` per `.serena/` config in repo root)
- `test-coverage.md` / `test-expression.md` / `visual-regression.md`
- `actions-lock.json` (compiled action SHA pins)

= 24 named workflow primitives forming the **gh-aw self-development workflow catalog** (gh-aw uses these workflows to develop gh-aw itself = dogfooding meta-layer).

## .skill-optimizer/ self-improvement subsystem

`.skill-optimizer/skill-optimizer.json` configures daily skill-optimization workflow that:
- Runs daily as scheduled GitHub Actions workflow
- Uses agentic workflow to evaluate and refine skills/* content
- Tunable via `models` / `maxTasks` / `maxIterations` / pass-rate target

= **CORPUS-FIRST autonomous-self-improvement subsystem at corporate-official tier**. Adjacent to aidevops v47 Pulse Supervisor (LLM-as-cron) but distinct in purpose — gh-aw skill-optimizer focuses narrowly on skill quality maintenance.

## 8 corpus-first observations from Cluster 2

1. **CORPUS-LARGEST AGENTS.md** — 49.8 KB at github-corporate-official tier (beats prior largest in corpus; aidevops v47 had ~21KB at root + 18KB nested)
2. **CORPUS-FIRST `.architecture.yml` architectural-threshold manifest** at root (file-line BLOCKER + WARNING + function-line + export-count)
3. **CORPUS-FIRST inverse-PR governance** — non-core PR rejection by default + agentic-plan-in-issue convention at corporate-official tier (Pattern #69 inverse observation)
4. **CORPUS-FIRST GitHub Next 4-researcher cluster lineage** — Don Syme + Eric Aftandilian + Peli de Halleux + Krzysztof Cieślak as CODEOWNERS
5. **CORPUS-FIRST Don Syme citation** — F# language creator at github-mainline tier (Pattern #19 archetype-2 strengthening with serious-language-design researcher)
6. **CORPUS-FIRST Krzysztof Cieślak citation** — Ionide (F#) creator at github-mainline tier
7. **CORPUS-FIRST product-disambiguation-from-sibling at corporate-official tier** — explicit "gh-aw is NOT GitHub Copilot CLI" framing in AGENTS.md
8. **CORPUS-FIRST autonomous self-improving skill optimizer** — daily workflow tunes skill quality at corporate-official tier (.skill-optimizer/ subsystem)
9. **CORPUS-FIRST 24-skill engineering-domain-focused library** at corporate-official tier (each skill = one engineering surface, Anthropic-skill format)
10. **CORPUS-FIRST 63-engineering-note working-scratchpad** at corporate-official tier (living engineering-decision-records)
11. **CORPUS-FIRST Codespace/Dev-Container-only contributor binding** — generic dev envs explicitly unsupported

## Pattern Library implications from Cluster 2

- **Pattern #12 Governance-Depth refined v42 3-factor model**: 5th counter-evidence to "solo→light" — corporate-official + heavy-governance (12+ files) confirms refined formulation HOLDS strongly. Most-decorated governance in corpus at corporate-official tier.
- **Pattern #19 archetype 2 methodology-lineage**: GitHub Next 4-researcher cluster as research-org-cluster lineage type (parallel to Anthropic-team-cluster). NOT 4 new individual nodes — single cluster node. Strengthening, not registration.
- **Pattern #22 AGENTS.md sub-variant analysis**:
  - 22c authoritative-with-shim aidevops v47 = AGENTS.md primary + CLAUDE.md/AGENT.md redirect-shims
  - **gh-aw v48 = AGENTS.md-only (NO CLAUDE.md, NO AGENT.md)** — cleanest AGENTS.md-only at corporate-official tier
  - Counter-evidence narrowing 22c: at github-corporate-official tier, AGENTS.md-only is the convention (spec-kit v17 + gh-aw v48); 22c authoritative-with-shim is solo-multi-runtime-platform pattern (aidevops v47)
- **Pattern #69 Agent-PR Fast-Track Governance**: gh-aw inverse-observation = non-core PR rejection + agentic-plan-in-issue. Within-#69 observational; sub-variant tracking opportunity at next mini-audit.
- **Pattern #66 OT Supply-Chain**: defense-in-depth visibility deepens — full architectural framing in C3.

## Counter-evidence + absences

- **No CLAUDE.md at root** — pure AGENTS.md-only at github-corporate-official tier (counter-evidence to aidevops v47 22c sub-variant; aligned with spec-kit v17 corporate-official precedent).
- **No CITATION.cff** — despite research-lineage. Notable absence (magika v44 had CITATION.cff at Google-Research-OSS tier; gh-aw doesn't).
- **No paper / arXiv** — despite GitHub Next research origins. Pattern #42 Academic-Published does NOT apply.
- **No Discord-specific community** — uses GitHub Next umbrella Discord.
- **EN-only** — no i18n at github-corporate-official tier.
