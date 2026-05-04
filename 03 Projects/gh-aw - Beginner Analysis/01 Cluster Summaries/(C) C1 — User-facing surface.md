# (C) Cluster 1 — User-facing surface

> **Wiki #48 · gh-aw** | **2026-04-25** | Sources: README.md / SKILL.md / install.md / create.md / debug.md / Companion projects refs / Peli's Agent Factory blog reference

## Verbatim positioning

- Hero tagline (README + repo description): **"Write agentic workflows in natural language markdown, and run them in GitHub Actions."**
- Equation framing (README HTML comment for agent reference): **"GitHub Agentic Workflows = Actions + Agent + Safety."**
- Guardrails framing (verbatim): *"Workflows run with read-only permissions by default, with write operations only allowed through sanitized `safe-outputs`."*
- Risk disclosure (verbatim): *"Using agentic workflows in your repository requires careful attention to security considerations and careful human supervision, and even then things can still go wrong. Use it with caution, and at your own risk."*

## What gh-aw does

| Capability | Description |
|------------|-------------|
| Compile markdown → CI | Converts `.md` agentic-workflow specs into compiled `.lock.yml` GitHub Actions workflow files |
| 5-engine support | `copilot` / `claude` / `codex` / `custom` engines selectable per-workflow via frontmatter |
| MCP integration | First-class MCP server configuration including GitHub MCP server (default toolsets: repos / issues / pull_requests / etc.) |
| Safe outputs | Sanitized output paths (`safe-outputs`) for write operations |
| CLI commands | `gh aw compile` / `gh aw run` / `gh aw mcp list` / `gh aw mcp inspect` / `gh aw logs` / `gh aw audit <run>` |
| GitHub Copilot Chat integration | `/agent` invokes unified `agentic-workflows` custom agent (specify intent: create/debug/update/upgrade) |

## Install surface (3 channels)

```bash
# Channel 1: GitHub CLI extension (canonical)
gh extension install github/gh-aw

# Channel 2: curl bash installer
curl -sL https://raw.githubusercontent.com/github/gh-aw/main/install-gh-aw.sh | bash

# Channel 3: Homebrew (per CHANGELOG)
brew install gh-aw   # availability per release notes
```

After install: `gh aw init` configures `.gitattributes` (`.lock.yml` as generated) + `.github/agents/agentic-workflows.agent.md` dispatcher + `.vscode/settings.json` + `.github/mcp.json` + `.github/workflows/copilot-setup-steps.yml`.

## 4 onboarding markdown files at repo root (corpus-first pattern)

| File | Lines | Purpose |
|------|-------|---------|
| `install.md` | 109 | Repository setup walkthrough for coding agents (install + init + commit) |
| `create.md` | 200 | Decision tree for create / update / debug / upgrade actions; routes to detailed prompt files |
| `debug.md` | 141 | Debug agentic workflow walkthrough |
| `SKILL.md` | 39 | Mini-skill self-description for external coding agents to consume |

**Observation:** README HTML comment to agents reads:
> *"Hello fellow agent! Welcome to GitHub Agentic Workflows = Actions + Agent + Safety. Here are some pointers to get you started in using this tool. - Create: raw.githubusercontent.com/github/gh-aw/main/create.md - Install: ../install.md - Reference: ../.github/aw/github-agentic-workflows.md"*

= **CORPUS-FIRST**: explicit agent-targeted README comment routing to coding-agent-consumable markdown specs at `raw.githubusercontent.com/github/gh-aw/main/<file>.md`. Bridge philosophy is built into onboarding pathway: humans read README, agents fetch raw markdown specs.

## Documentation site

- **Hosted:** https://github.github.com/gh-aw/ (GitHub Pages site, generated from `docs/` via Astro framework per `docs/astro.config.mjs`)
- **For agents:** https://github.github.com/gh-aw/llms.txt (LLM-consumable summary of all documentation)
- **Quick Start path:** https://github.github.com/gh-aw/setup/quick-start/
- **How It Works:** https://github.github.com/gh-aw/introduction/how-they-work/
- **Security Architecture:** https://github.github.com/gh-aw/introduction/architecture/

`docs/` repo subdirectory contains: `adr/` (Architecture Decision Records) + `enterprise-configuration.md` + `interactive-run-mode.md` + `functional-patterns.md` + `security-findings-2026-01-19.md` + Astro-built site infrastructure.

## Community contributions section (986 README lines, ~120 actual content + ~860 attribution)

README's `## 🌍 Community Contributions` collapsible block (auto-generated; updated programmatically) lists:
- ~150+ named contributors with linked issue numbers
- Format: `### @<username>` headings + bulleted issue references (`#NNNNN _(direct issue)_`)
- Trailing "Attribution Candidates Need Review" subsection lists 15 closed-but-unlinkable issues with NOT_PLANNED / DUPLICATE labels and ~6-week lookback window

**Observation:** README is **86% community attribution** by line count (≈860 of 988 lines). Distinct from corpus precedents:
- spec-kit v17 README: ~12 KB technical content
- aidevops v47 README: ~142 KB heavy
- gh-aw README: ~21 KB but most is auto-attribution

This signals **community-issue-as-primary-contribution-pathway** (consistent with CONTRIBUTING.md's "Traditional Pull Requests Are Not Enabled for non-Core team members" rule documented in C2).

## Peli's Agent Factory (intellectual lineage signal)

README links: https://github.github.com/gh-aw/blog/2026-01-12-welcome-to-pelis-agent-factory/

**"Peli"** = Peli de Halleux (@pelikhan), GitHub Next researcher, named in CODEOWNERS. The blog post is described as: *"a guided tour through many uses of agentic workflows."*

**Observation:** This is an unusually-personal product-positioning element at github-corporate-official tier. Where spec-kit v17 had attribution to John Lam's research lineage, gh-aw has Peli as named research-lineage exemplar plus GitHub Next as institutional context. Will explore in Cluster 3 entity page.

## Companion projects (Related Projects section)

3 companion repos in github/* org (Pattern #17 variant 2a sub-ecosystem observation):

| Repo | Description | Function |
|------|-------------|----------|
| **github/gh-aw-firewall** (AWF) | Agent Workflow Firewall | Network egress control for AI agents; domain-based access controls + activity logging |
| **github/gh-aw-mcpg** | MCP Gateway | Routes MCP server calls through unified HTTP gateway for centralized access management |
| **github/gh-aw-actions** | Shared GitHub Actions library | Custom Actions used by compiled workflows (e.g., MCP server file management) |

= **CORPUS-FIRST**: 4-repo coordinated agentic-CICD-platform under single corporate parent. Distinct from prior corpus ecosystem variants (RuvNet 15-package solo / HKUDS 7-repo academic / Zilliz 8-product commercial-startup).

## Sharing + community

- **Community Feedback Discussions:** https://github.com/orgs/community/discussions/186451 (uses GitHub-org-discussion forum pattern)
- **Discord:** GitHub Next Discord at https://gh.io/next-discord (= GitHub Next research org Discord, not a gh-aw-specific Discord)

**Observation:** No dedicated Discord for gh-aw — uses GitHub Next umbrella + GitHub community forum. This is consistent with research-incubation-graduated-to-mainline hypothesis: gh-aw inherits GitHub Next community infrastructure rather than building its own.

## 8 corpus-first observations from Cluster 1

1. **CORPUS-FIRST agent-targeted README HTML comment** routing agents to raw-markdown specs at `raw.githubusercontent.com/github/gh-aw/main/<file>.md`
2. **CORPUS-FIRST agentic-workflow-compiler-for-CICD-bridge T4i sub-archetype** (markdown → Actions YAML compilation pipeline; distinct from 7 prior T4 sub-archetypes including code-bridge graphify v16 / GitNexus v33 / claude-context v40)
3. **CORPUS-FIRST 4-onboarding-markdown-files at repo root** (install.md / create.md / debug.md / SKILL.md as first-class onboarding artifacts vs nested in docs/)
4. **CORPUS-FIRST 5-engine first-class support** (copilot/claude/codex/custom + extensible) at github-corporate-official tier; engine-selection via frontmatter
5. **CORPUS-FIRST `.lock.yml` compiled-from-markdown convention** ("never add lock files to .gitignore" enforcement)
6. **README 86% community-attribution by line count** = corpus extreme on attribution-density (consistent with non-core-PR-rejection contribution model)
7. **GitHub Pages docs site with explicit `llms.txt`** for LLM consumption = first explicit corpus llms.txt observation
8. **3-companion github-org sub-ecosystem under single corporate parent** (AWF + MCP Gateway + Actions library) = corpus-first non-commercial corporate-platform-companion pattern

## Pattern Library implications from Cluster 1

- **Pattern #2 Distribution Evolution** strengthening: 3 install surfaces (gh extension + curl + brew) — medium for corpus
- **Pattern #17 variant 2a corporate-official strengthening**: github-org 4-repo sub-ecosystem (gh-aw + gh-aw-firewall + gh-aw-mcpg + gh-aw-actions); same parent, multi-product portfolio
- **Pattern #22 AGENTS.md-only sub-variant**: github-corporate-official preserves AGENTS.md-only convention (NO CLAUDE.md alias at repo root); counter-evidence to aidevops v47 22c authoritative-with-shim sub-variant — the github-corporate-official tier convention is AGENTS.md-only
- **Pattern #28 Multi-Provider strengthening**: 5 named engines via frontmatter (copilot/claude/codex/custom + extensibility); engine-selection-as-frontmatter-axis sub-observation (within-pattern, not new candidate)
- **Pattern #66 OT supply-chain strengthening signal**: SHA-pinned dependencies + sandboxed execution + network isolation explicitly named in user-facing docs (full architectural framing in C3)

## Counter-evidence + absences

- **Pattern #19 archetype 1 individual-author-lineage ABSENT** — gh-aw has named research lineage but it's a 4-researcher cluster (GitHub Next), not single individual node like Karpathy / Lam / Cherny. Counter-evidence framing: "research-org-cluster ≠ individual-author-node" — strengthen archetype 2 lineage-cluster sub-observation.
- **AGENTS.md without CLAUDE.md** — counter-evidence to aidevops v47 22c authoritative-with-shim sub-variant.
- **No i18n** — EN-only at github-corporate-official tier (consistent with spec-kit v17). Notable absence at 4K+-star scale.
- **No Discord/community-platform-specific community** — uses GitHub Next umbrella + community forum (consistent with research-graduated-to-mainline organizational pattern).
