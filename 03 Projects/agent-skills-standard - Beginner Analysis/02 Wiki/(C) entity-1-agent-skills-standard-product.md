# (C) Entity 1 — agent-skills-standard (T1 Standards-Layer)

## Identity

- **Name:** agent-skills-standard
- **Tagline:** "The portable SDLC standards layer for AI coding agents. Sync once, then work in your own runtime."
- **Repo:** https://github.com/HoangNguyen0403/agent-skills-standard
- **NPM:** https://www.npmjs.com/package/agent-skills-standard
- **License:** Apache 2.0 (README mistakenly declares "MIT License" — Pattern #83 sub-mechanism 83f N=2)
- **Latest release:** android v1.4.2 (2026-05-18) — per-component versioning across categories
- **Tier:** T1 Assistant Skill / Standards-Layer
- **Primary lang:** TypeScript 94.4% + JavaScript 3.2% + Python 2.2%
- **Scale:** 496 stars / 147 forks / 9 watchers / 0 open issues / 144 commits / created 2026-01-15

## Velocity-screen

| Metric | Value | Signal |
|--------|-------|--------|
| Repo age | 124 days (created 2026-01-15) | sustained-developing |
| Stars/day | **4.0** | BELOW Pattern #52 sub-class thresholds (non-viral); standards-layer typical |
| Fork ratio | **0.296** | **CORPUS-RECORD-HIGH active-deployment intent** (1.66× v65 17.8% prior record) |
| Watcher/star | 0.018 | low engagement-per-star |
| Issue/star | **0** | **CORPUS-RECORD-LOW engagement-deficit-extreme** (0 open issues despite 147 forks) |

## What it is

A **TypeScript npm monorepo** that distributes 259 framework-specific coding standards across 10+ AI coding agents via a CLI sync mechanism + optional MCP runtime enforcement server. Single canonical source generates native formats for each harness.

The corpus-defining novelty: traditional approaches stuff all rules into every prompt (3,600+ tokens). agent-skills-standard achieves the same outcome with **~25 lines scanned per edit** via a 3-tier hierarchical lookup (claimed "85% fewer tokens").

## What it does (3-layer interaction model)

1. **CLI** (`npx agent-skills-standard@latest init` + `sync`) — detects project tech stack + distributes skills to detected AI agent folders in native formats
2. **MCP server** (optional) — runtime "Transparent Interception" intercepts agent file reads + auto-injects relevant skill rules + audit logs
3. **Canonical `skills/` source** — 259 SKILL.md files organized by category, edited once, distributed everywhere

## Multi-harness compatibility (10+ AI agents)

Native formats generated per harness:

| Harness | Native format | Output location |
|---------|---------------|-----------------|
| Claude Code | Command Markdown | `.claude/` |
| Roo | Command Markdown | (Roo-specific) |
| OpenCode | Command Markdown | `.opencode/` |
| Cursor | Skill folder with SKILL.md | `.cursor/rules/` |
| Trae | Skill folder with SKILL.md | `.trae/skills/` |
| Codex | Skill folder with SKILL.md | `.codex/skills/<workflow>/SKILL.md` |
| Gemini | TOML command files | (Gemini-specific) |
| GitHub Copilot | Prompt instruction files | `.github/instructions/*.instructions.md` |
| Windsurf | MCP + Rule Persistence | `.codeium/windsurf/mcp_config.json` |
| Kiro | Native Markdown workflows | (Kiro-specific) |
| Antigravity | Native Markdown workflows | `.antigravity/` |
| MCP | Tool definitions (JSON) | MCP-compatible runtimes |

**Distribution mechanism:** v76 agent-skills-standard uses **CLI-generates-native-formats-from-canonical-source** — distinct from v75 impeccable's **repo-stored-N-harness-replicas**. Both achieve multi-target portability but via different layers.

## Skill library (259 skills × 20+ frameworks)

**Frameworks covered:**

| Domain | Frameworks |
|--------|-----------|
| Mobile | Flutter, Dart, iOS, Swift, Android, Kotlin |
| Web Frontend | React, Next.js, Angular, TypeScript |
| Backend | NestJS, Go, Spring Boot, Java, PHP, Laravel |
| Database | (multiple) |
| Specialist | QA workflows, architect roles, others |

**Per-skill discipline:**
- Max 100 lines per `SKILL.md`
- ~500 tokens average
- Heavy reference content → `references/` subfolder (lazy-loaded)
- `evals.json` validation data for CI gates

## 3-tier hierarchical lookup (the architecture innovation)

| Tier | File | Purpose | Approx. lines |
|------|------|---------|---------------|
| 1 | `AGENTS.md` | Router (file-extension → category) | ~20 |
| 2 | Category `_INDEX.md` | File Match / Keyword Match triggers | ~10-15 |
| 3 | `SKILL.md` | Skill content (loaded on-demand) | ~100 max |

**O(n) → O(1) scan cost** vs flat-list designs that grew unwieldy at 238+ entries.

## MCP server "Transparent Interception"

Inspired by "Rust Token Killer" principles per ARCHITECTURE.md.

- **Lazy Loading** — skills unloaded until triggered
- **Interception Model** — MCP intercepts file read requests; injects relevant skill rules; eliminates manual rule-fetching
- **Token Filtering** — ~90% reduction in initial scouting tokens
- **Audit Logs** — show which skills informed each AI decision (CORPUS-FIRST audit-trail layer)

## CLI service architecture (4 services)

| Service | Responsibility |
|---------|----------------|
| SkillSyncService | Fetches SKILL.md + references; writes to agent dirs; prunes orphans |
| WorkflowSyncService | Distributes workflows in native format per agent |
| IndexGeneratorService | Produces router (AGENTS.md) + category (_INDEX.md) indices |
| AgentBridgeService | Generates agent-specific rule files pointing to AGENTS.md |

**Design principles:**
- **Safe Overwrite** — `custom_overrides` in `.skillsrc` preserved across syncs
- **Local-First Indexing** — local custom skills integrated into generated indices

## `.skillsrc` user config

Controls per-project:
- Which agents receive synced skills
- Framework/skill exclusions (e.g., excluding GetX if unused)
- Custom skill paths for project-specific rules
- MCP scope (`project` / `user` / `snippets-only` / `disabled`)

## Security model (zero-trust)

- **Text-only artifacts** — Markdown/JSON; no executable code; no filesystem access; no network requests
- **CLI downloads text only**
- **Zero telemetry** — no usage data collected
- **Local-first** — project data stays on local disk
- **Prompt injection scanning** — skills scanned at sync time
- **ConfigService validates schemas via Zod**
- **evals.json per skill** — automated AI adherence validation

## "85% fewer tokens" benchmark

Per README:
- Traditional prompts: 3,600+ tokens per chat
- Skills Standard: ~500 tokens per skill, loaded selectively
- ~25 lines scanned per edit (router + index) vs all rules

`benchmark-report.md` documents the methodology.

## License declaration mismatch

| Surface | Declaration |
|---------|-------------|
| LICENSE file | Apache-2.0 |
| GitHub API license field | Apache-2.0 |
| README "License & Attribution" section | **"MIT License"** |

**Structural reality:** Apache 2.0. README is OUT-OF-SYNC.

Pattern #83 sub-mechanism 83f sister-evidence — **N=2 PROMOTION-ELIGIBLE** post-v74 LLMs-from-scratch (which had CITATION.cff "Apache-2.0" vs LICENSE.txt modified Apache).

## Trade-offs

- **Strength**: opinionated 3-tier architecture solves real token-cost problem; multi-harness portability eliminates lock-in; MCP audit-log enforcement provides accountability; 259 skills + 20+ frameworks is broad coverage; benchmark-driven design
- **Weakness**: 0 open issues despite 147 forks signals unusual community-engagement pattern (issues bypassed?); README license declaration mismatch needs fixing; android v1.4.2 (and other per-category versions) implies category-specific releases that could create version-sprawl
- **Cost**: 7+ governance files (README/AGENTS/AGENTS_LEARNING/ARCHITECTURE/CONTRIBUTING/LICENSE/CHANGELOG/benchmark-report) is heavyweight onboarding; learning the 3-tier lookup model requires effort upfront

## Pattern Library implications (see entity 3)

- Pattern #84 84c N=5 NEW sub-mechanism "CLI-generates-native-formats-from-canonical-source"
- Pattern #78 N=4 CORPUS-RECORD codification density (259 skills × 20+ frameworks)
- Pattern #19 NEW sub-mechanism 19g "Vietnamese-Solo-Standards-Codifier"
- Pattern #83 sub-mechanism 83f N=2 PROMOTION-ELIGIBLE
- Pattern #82 N+1 quantitative-marketing ("85% fewer tokens" + 540 tokens/skill + benchmark-report.md)
- Pattern #18 B1 MCP variant N=3 strengthening (Transparent Interception + audit logs)
- 3 NEW observational candidates (OC-X / OC-Y / OC-Z)
