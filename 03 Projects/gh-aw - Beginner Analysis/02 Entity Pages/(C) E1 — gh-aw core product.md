# (C) Entity 1 — gh-aw core product

> **Wiki #48** | **2026-04-25** | github/gh-aw — GitHub CLI extension that compiles natural-language markdown agentic-workflow specs into executable GitHub Actions YAML.

## 1. What it is

**gh-aw** = a GitHub CLI extension (`gh aw` subcommand family) that compiles markdown agentic-workflow specs into compiled GitHub Actions YAML lock files (`.lock.yml`). It enables writing AI-agent-driven CI/CD workflows in natural-language markdown rather than handcrafted YAML.

Tagline: *"Write agentic workflows in natural language markdown, and run them in GitHub Actions."*

Equation framing: **GitHub Agentic Workflows = Actions + Agent + Safety.**

## 2. Headline metrics

- **Stars:** 4,367 (medium scale; ~514 stars/month sustained-organic since 2025-08-12)
- **Forks:** 366 (8.4% — mature consumption-low ratio)
- **Open issues:** 124 (active triage)
- **License:** MIT
- **Primary lang:** Go (1,789 .go files; 96%+ Go)
- **Latest release:** v0.68.3 (2026-04-14)
- **Docs:** https://github.github.com/gh-aw/ (Astro-built site)
- **LLM-consumable summary:** https://github.github.com/gh-aw/llms.txt

## 3. Tier placement (Pattern Library)

**T4 Agent-as-bridge primary** — 8th T4 entrant + NEW T4i sub-archetype: **agentic-workflow-compiler-for-CICD-bridge** (compiles markdown → executable Actions YAML).

Distinct from prior T4 sub-archetypes:
- T4a corporate-broad gws v13 (Google Workspace bridge to AI-agent harnesses)
- T4b solo-narrow notebooklm-py v7 (Python bridge to NotebookLM)
- T4c solo-broad-local graphify v16 (code → knowledge graph)
- T4d solo-broad-external TrendRadar v19 (CN news → AI-agent + push channels)
- T4e corporate-narrow-utility markitdown v28 (file → markdown for LLM)
- T4f solo-enterprise-scale crawl4ai v29 (web → LLM-friendly markdown)
- T4g solo-student-with-commercial GitNexus v33 (code → graph + commercial tier)
- T4h commercial-ecosystem-startup claude-context v40 (vector code-indexing + Zilliz)
- **T4i NEW github-corporate-official-workflow-compiler gh-aw v48** (markdown → CI YAML)

T4 is now corpus's 2nd-largest tier (after T1 N=14) at N=8.

## 4. Core architecture (4 layers)

### Layer 1: User-facing markdown specs

User authors `.md` files (e.g., `weekly-digest.md`) with YAML frontmatter:
```yaml
---
on:
  schedule:
    - cron: '0 9 * * 1'
permissions:
  contents: read
  issues: write
engine: copilot
tools:
  github:
    toolsets: [default]
---

# Weekly Digest Workflow

Summarize PRs and issues from the last week into a Markdown report
and post it as an issue comment.
```

### Layer 2: Compile-time validation + transformation

`gh aw compile` validates markdown spec (schema + permissions + expressions + actions) and emits compiled `.lock.yml` GitHub Actions workflow. Lock files are **tracked in git** (NEVER .gitignored).

### Layer 3: Runtime execution on GitHub Actions

GitHub Actions runners execute `.lock.yml` workflow:
1. **Activation job** — handle event trigger
2. **Agentic job** — sandboxed LLM execution via selected engine (copilot/claude/codex/custom)
3. **Safe-output job** — sanitize agent outputs before write operations

### Layer 4: Companion infrastructure (3 repos)

- **`github/gh-aw-firewall`** (AWF) — Network egress control for AI agents (domain allowlists + activity logging)
- **`github/gh-aw-mcpg`** (MCP Gateway) — Routes MCP server calls through unified HTTP gateway
- **`github/gh-aw-actions`** — Shared GitHub Actions library used by compiled workflows

## 5. CLI command surface

| Command | Purpose |
|---------|---------|
| `gh aw init` | Configure repo for agentic workflows (`.gitattributes`, agent dispatcher, mcp.json, copilot-setup-steps.yml) |
| `gh aw compile` | Compile all `.md` workflow specs to `.lock.yml` |
| `gh aw run <workflow>` | Manually trigger a workflow |
| `gh aw mcp list` | List MCP server configurations |
| `gh aw mcp inspect <workflow>` | Inspect MCP server usage in a workflow |
| `gh aw logs` | Download and analyze workflow logs |
| `gh aw audit <run-id>` | Audit a specific workflow run |
| `gh aw add <repo>` | Add workflows from another repo (e.g., `gh aw add githubnext/agentics`) |
| `gh aw new <name>` | Create new workflow (or use `/agent` in Copilot Chat) |
| `gh aw version` | Display version info |
| `gh aw upgrade aw` | Upgrade extension |

## 6. 5-engine support (frontmatter selectable)

| Engine | Description | Constraints |
|--------|-------------|-------------|
| `copilot` | GitHub Copilot Coding Agent | Cannot directly access api.github.com — MUST use GitHub MCP server (`tools: github: { toolsets: [default] }`) |
| `claude` | Claude (Anthropic API or Claude Code OAuth) | Standard Claude integration |
| `codex` | OpenAI Codex | Standard Codex integration |
| `custom` | Extensible engine plugin | User-defined engine adapter |
| (extensibility) | per `scratchpad/adding-new-engines.md` | Plugin architecture documented |

= **CORPUS-FIRST 5-engine first-class support at corporate-official tier**. Engine-selection-as-frontmatter-axis is structurally distinct from native multi-provider routing (multica v15 / TrendRadar v19) and verification-not-routing (aidevops v47).

## 7. Safety architecture (Pattern #66 OT strongest data point)

**Reference:** `specs/security-architecture-spec.md` (W3C-style v1.0.0 Candidate Recommendation, 2026-01-29)

**7-layer defense-in-depth:**
0. Compilation-Time Validation (schema + expressions + permissions)
1. Input Sanitization (@mentions / bot triggers / XML/HTML / URIs)
2. Output Isolation (separate read/write; safe-outputs)
3. Network Isolation (domain allowlisting via AWF)
4. Permission Management (least-privilege; role-based access)
5. Sandbox Isolation (AWF/SRT containers + MCP isolation)
6. Threat Detection (prompt injection / secret leaks / malicious patches)

**7 Security Guarantees (SG-01 through SG-07):**
- SG-01 Input sanitization
- SG-02 No direct AI write access
- SG-03 Network restricted to allowlists
- SG-04 Least-privilege defaults
- SG-05 Sandboxed agent processes
- SG-06 Auditable artifacts
- SG-07 Fail-secure on security failures

**130+ formal requirements (RFC 2119) + 70+ compliance tests + 3 conformance classes** (Basic / Standard / Complete).

## 8. Install + initialization

```bash
# Install (3 channels)
gh extension install github/gh-aw                # canonical
curl -sL .../install-gh-aw.sh | bash             # script
brew install gh-aw                                # Homebrew (per CHANGELOG)

# Initialize repo
gh aw init   # creates .gitattributes / .github/agents/agentic-workflows.agent.md
             # / .vscode/settings.json / .github/mcp.json / .github/workflows/copilot-setup-steps.yml

# Compile + run
gh aw compile
gh aw run my-workflow.md
```

## 9. Key innovations (corpus-first)

1. **Markdown-as-source-truth-compiled-to-YAML** at corporate-official tier
2. **5-engine first-class support** with engine-selection via frontmatter
3. **`.lock.yml` track-the-compiled-output convention** (never .gitignored)
4. **W3C-style formal security architecture spec** (130+ MUST/SHOULD; 70+ tests; 3 conformance classes)
5. **MCP Gateway** companion repo (Pattern #18 Layer 0 observation)
6. **AWF (Agent Workflow Firewall)** companion repo for network egress control
7. **24-skill engineering-domain-focused skill library** (each skill = engineering surface)
8. **Daily skill-optimizer self-improvement workflow**
9. **`.architecture.yml` architectural-threshold manifest** at root
10. **Agent-targeted README HTML comment** routing agents to raw-md specs

## 10. vs sibling corpus frameworks

| Dimension | gh-aw v48 | spec-kit v17 | aidevops v47 | graphify v16 (T4) | markitdown v28 (T4) |
|-----------|-----------|--------------|--------------|-------------------|---------------------|
| **Tier** | T4 (CICD bridge) | T1 (methodology) | T1 (assistant) | T4 (knowledge-graph bridge) | T4 (file utility) |
| **Parent** | github org | github org | solo Marcus Quinn | solo safishamsi | Microsoft / AutoGen |
| **License** | MIT | MIT | MIT | PolyForm Noncommercial | MIT |
| **Primary lang** | Go | Python | Bash + TS | Python | Python |
| **AGENTS.md** | 49.8 KB (corpus-largest) | medium | 18 KB nested | absent | absent |
| **Skills system** | 24 engineering-domain | 80+ skills | 873 .sh / 1,792 .md | absent | absent |
| **Engines** | 5 (copilot/claude/codex/custom + ext) | spec-driven; engine-agnostic | OpenCode-primary + 4-OAuth | Claude Code primary | LLM-client DI |
| **Security spec** | W3C-style 130+ requirements | 9-article constitution | SHA-pinned + AGENTS.md | minimal | minimal |
| **Companion repos** | 3 (AWF + MCP Gateway + Actions) | 0 | 0 | 0 | 0 |
| **Distribution** | gh ext + curl + brew | uv tool + curl | npm + Bun + brew + curl + manual | npm | pip + Docker |

**gh-aw distinguishing features:**
- Compiles human-readable markdown → executable CI YAML (bridge function)
- Most-formalized security spec at corporate-official tier in corpus
- Most-coordinated 4-repo sub-ecosystem (gh-aw + AWF + MCP Gateway + Actions)
- Self-improving skill optimizer subsystem

## 11. Cross-references

- **spec-kit v17** — sibling github/* corpus entry (T1 methodology). Same parent org, distinct product archetypes; gh-aw is T4 bridge while spec-kit is T1 methodology.
- **aidevops v47** — recent EXTREME-tier comparison; 22c authoritative-with-shim sub-variant (gh-aw counter-evidence: AGENTS.md-only at corporate-official, no shims).
- **awesome-mcp-servers v31** — Pattern #18 ancestor; gh-aw consumes MCP servers via gateway companion repo.
- **graphify v16** — T4 bridge sibling (code → knowledge graph; gh-aw = markdown → CI workflow); both are bridge-tier compilation pipelines.
- **markitdown v28** — Microsoft T4 utility precedent; gh-aw = github-corporate-broad-bridge (different scope but corporate-official tier kinship).
- **claude-context v40** — Zilliz T4 commercial-ecosystem-startup precedent; gh-aw = corporate-official non-commercial sibling.
- **OMC v27** — Pattern #18 Western-community OpenClaw precedent (gh-aw is corporate-official, distinct positioning).
- **claude-howto v32** — Boris Cherny / Anthropic-team-cluster precedent for cluster-as-lineage-node (gh-aw uses GitHub Next 4-researcher cluster).
- **rowboat v43** — Pattern #57 Recursive Corpus Reference precedent (implicit Karpathy); gh-aw has explicit GitHub Next lineage.

## 12. Pattern Library cross-tags

- Pattern #2 Distribution Evolution — strengthening (3-surface install)
- Pattern #12 Governance-Depth refined v42 3-factor — 5th counter-evidence (corporate + heavy)
- Pattern #17 variant 2a corporate-official — strengthening (4-repo sub-ecosystem under same parent)
- Pattern #18 MCP Layer 0 — N=1 observation (MCP Gateway as unified routing infrastructure)
- Pattern #19 archetype 2 methodology-lineage — strengthening (research-org-cluster as lineage type; GitHub Next 4-researcher CODEOWNERS)
- Pattern #22 AGENTS.md sub-variant — counter-evidence narrowing 22c (AGENTS.md-only at corporate-official tier vs 22c shim-pattern at solo-multi-runtime)
- Pattern #28 Multi-Provider — strengthening (engine-selection-as-frontmatter-axis sub-observation)
- Pattern #66 OT Supply-Chain — MAJOR STRENGTHENING (W3C-style spec + 7-layer + SG-01-07 + 130+ requirements + 70+ tests + SBOM + AWF + MCP Gateway + compile-time validation)
- Pattern #69 Agent-PR Fast-Track — inverse-observation (non-core PR rejection + agentic-plan-in-issue convention)

## 13. Status + recommendation

**Production-stable** at v0.68.3 (2026-04-14, ~8.5 months mature). Active development by 4-maintainer GitHub Next research-graduated team.

**Storm Bear pilot recommendation: NOT in top-11.** Domain mismatch (CICD-workflow vs Markdown-knowledge-vault) + security-binding deployment friction (requires GitHub Actions, write permissions, LLM API key, repo-write trust). **Observational value HIGH** for AGENTS.md template + skills/ pattern + W3C-style spec discipline reference.
