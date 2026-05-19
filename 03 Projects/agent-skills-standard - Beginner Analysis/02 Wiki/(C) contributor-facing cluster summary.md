# (C) Cluster: Contributor-facing — architecture + multi-harness distribution mechanism + governance

## In one sentence

agent-skills-standard is a **TypeScript monorepo** with a 3-tier hierarchical-lookup architecture, an "Transparent Interception" MCP server inspired by "Rust Token Killer" principles, a multi-service CLI orchestration (`SkillSyncService` + `WorkflowSyncService` + `IndexGeneratorService` + `AgentBridgeService`), and a multi-agent compatibility matrix that generates native formats for 10+ AI harnesses from a single canonical source.

## Repository topology

```
HoangNguyen0403/agent-skills-standard/
├── README.md, CHANGELOG.md, LICENSE, CONTRIBUTING.md
├── AGENTS.md            (compact router ~20 lines, file-extension → category index)
├── AGENTS_LEARNING.md   (learning resources for agent behavior)
├── ARCHITECTURE.md      (3-tier lookup + MCP design + multi-harness matrix)
├── benchmark-report.md  (token efficiency metrics)
├── .skillsrc            (user config: agents, exclusions, MCP scope, custom paths)
├── metadata.json        (registry: file routing, broad globs, categories, version)
├── package.json, pnpm-workspace.yaml, tsconfig.json
│
├── skills/              ← canonical skill source (259 SKILL.md files, organized by category)
│   └── <category>/
│       └── <framework>/
│           ├── SKILL.md      (100-line max, ~500 tokens avg)
│           ├── references/   (lazy-loaded reference content)
│           ├── evals.json    (validation data for AI adherence)
│           └── _INDEX.md     (category index, ~10-15 lines)
│
├── cli/                 (init + sync + MCP management commands)
├── mcp/                 (MCP server: Transparent Interception + audit logs)
├── server/              (backend service layer)
├── scripts/             (orchestration scripts)
│
├── .agents/             (primary agent configuration location)
├── .codex/              (Codex-specific harness files)
├── .antigravity/        (Google Antigravity workflow integration ← CORPUS-FIRST mention in v60+ window)
├── .github/             (CI workflows + issues + community)
├── .vscode/, .husky/    (dev tooling)
```

## 3-tier hierarchical lookup (the architecture innovation)

This is the architecture-defining design choice. Traditional prompt-engineering approaches load ALL rules every time, which scales as O(n) with the rule count. agent-skills-standard's approach is O(1):

```
File edit / agent task triggers
         ↓
[Tier 1] AGENTS.md ROUTER
  ~20 lines / file-extension → category index
  Example: *.ts → typescript/_INDEX.md
         ↓
[Tier 2] CATEGORY _INDEX.md
  ~10-15 lines / "File Match" vs "Keyword Match" triggers
  File Match: glob patterns auto-trigger (e.g., **/*.test.ts)
  Keyword Match: token-based triggers (e.g., "react", "useState")
         ↓
[Tier 3] SKILL.md FILE
  ~500 tokens avg / 100-line max
  Loaded ONLY when conditions match
  Heavy reference content in references/ subfolder (lazy-loaded)
```

**Skill file structure constraints:**
- Max 100 lines per `SKILL.md`
- ~500 tokens avg per skill (corpus-record-low density per artifact)
- Heavy reference content **segregated** to `references/` for lazy loading
- Broad globs (like `**/*.ts`) **demoted** from File Match to Keyword Match unless designated `base_language_skills`

## metadata.json registry settings

Registry-level config governing index generation:

| Field | Purpose |
|-------|---------|
| `file_routing` | Maps extensions to skill categories |
| `broad_globs` | Patterns considered too expansive for auto-triggering |
| `base_language_skills` | Single skill per category retaining broad-glob File Match status |
| `foundational_composite_rules` | Auto-injected composite triggers based on skill naming |
| `categories` | Version, tag prefix, token metrics per category |

## MCP server "Transparent Interception"

Inspired by "Rust Token Killer" principles per ARCHITECTURE.md. Two key behaviors:

- **Lazy Loading** — skills unloaded until triggered by tool calls or router matches
- **Interception Model** — MCP server intercepts file read requests; injects relevant skill rules into outputs; eliminates manual rule-fetching by agents
- **Token Filtering** — high-density info prioritization reduces initial scouting tokens by ~90% (claimed in ARCHITECTURE.md)

**Audit logs:** when MCP scope is enabled, audit log shows which skills informed each AI decision. Corpus-first audit-log enforcement layer (distinct from prior corpus subjects' enforcement mechanisms).

## CLI orchestration (4-service architecture)

`SyncService` orchestrates 4 dependent services:

| Service | Responsibility |
|---------|----------------|
| **SkillSyncService** | Fetches SKILL.md + references from registry; writes to agent directories; prunes orphaned files |
| **WorkflowSyncService** | Distributes canonical workflows from `.agents/workflows/*.md` into each agent's native format |
| **IndexGeneratorService** | Produces router indices (AGENTS.md) + category indices (_INDEX.md) |
| **AgentBridgeService** | Generates agent-specific rule files pointing to AGENTS.md |

**Design principles:**
- **Safe Overwrite** — respects `custom_overrides` in `.skillsrc` (user customizations preserved across syncs)
- **Local-First Indexing** — scans local disk post-sync; user-created custom skills integrate into generated indices

## Multi-harness native format generation matrix

Workflows export across distinct agent formats:

| Format | Used By |
|--------|---------|
| Native Markdown workflows | Antigravity, Kiro |
| Command Markdown | Claude, Roo, OpenCode |
| TOML command files | Gemini |
| Prompt instruction files | Copilot |
| Skill folders with SKILL.md | Cursor, Trae, Codex |
| MCP tools (JSON definitions) | Any MCP-compatible runtime |

**Codex special case:** receives transformed workflow skills under `.codex/skills/<workflow>/SKILL.md` rather than consuming `.agents/workflows` directly.

## Multi-Agent Compatibility Matrix (from ARCHITECTURE.md)

| Agent | Strategy | Primary Hook | Scope |
|-------|----------|--------------|-------|
| VS Code Copilot | Prompt Instructions | `.github/instructions/*.instructions.md` | Session |
| Cursor | MCP + Rules | `hooks.json` / `.cursor/rules/` | Project |
| Windsurf | MCP + Rule Persistence | `.codeium/windsurf/mcp_config.json` | Project |
| Claude Code | Bash Interception | `.mcp.json` / `~/.claude/` | User/Project |

## Security model (zero-trust architecture)

- **Files remain on local disk** — registry acts as standards SOURCE, not runtime
- **MCP enforces rule application through intercepted calls** (not RPC-exposed actions)
- **ConfigService validates schemas via Zod** — runtime input validation
- **User configuration (`.skillsrc`) controls dependency exclusions + skill subsets**
- **User-Extensibility by default** — manual edits + local custom skills integrate into generated indices

## License inconsistency

| Surface | Declaration |
|---------|-------------|
| LICENSE file | Apache-2.0 |
| GitHub API license field | Apache-2.0 |
| README "License & Attribution" | **"MIT License"** ← out-of-sync |

This is **Pattern #83 sub-mechanism 83f "license-declaration-vs-actual-mismatch" N=2 evidence** (promotes from N=1 v74 LLMs-from-scratch which had CITATION.cff "Apache-2.0" vs LICENSE.txt modified Apache).

## Build + release discipline

- **Per-component versioning:** android v1.4.2 (2026-05-18) suggests skill-categories version independently (analogous to v75 impeccable's Skill 3.1.1 + CLI + extension + plugin separately versioned)
- **TypeScript 94.4% + Python 2.2%** — multi-language monorepo with TS primary + Python utilities
- **pnpm-workspace.yaml** — monorepo with workspace boundaries
- **Husky pre-commit hooks** — Git hook discipline
- **GitHub Actions** in `.github/workflows/`
- **`evals.json` per skill** — automated AI adherence validation as CI gate

## What's missing / what to watch

- README declares MIT but LICENSE is Apache-2.0 — needs fixing or formal Pattern #83 sub-mechanism 83f registration
- 0 open issues despite 147 forks — issue triage process unclear or community managed via different channel (Discord? PRs only?)
- benchmark-report.md content not yet probed — verify "85% fewer tokens" claim methodology
- VMO Holding company context — sponsorship? working-time vs personal-time? Hoang's role positioning unclear
