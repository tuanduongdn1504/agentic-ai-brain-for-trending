# (C) Cluster: User-facing — what agent-skills-standard does + how to use it

## In one sentence

agent-skills-standard is an Apache-2.0 npm package that gives AI coding agents (Claude Code, Cursor, GitHub Copilot, Gemini, Windsurf, Trae, Kiro, Roo, Codex, MCP) **a shared SDLC standards library** — 259 framework-specific coding standards loaded on-demand via 3-tier hierarchical lookup, claiming **85% fewer tokens** than putting all rules in every prompt.

## Who it's for

The target user is the **team-lead or senior engineer who already has coding standards** but is frustrated that AI agents don't follow them. The README states the problem directly: "Every team has coding standards. But AI agents don't know them." Users arrive having tried prompt engineering and finding it expensive and unmaintainable.

Not the target: someone seeking to learn coding standards from scratch — the skills assume you've already decided what your team's standards are.

## What you get

**One npm package** (`agent-skills-standard`) with:
- **259 ready-to-use coding standards** across 20+ frameworks (Flutter / React / Next.js / Angular / NestJS / TypeScript / Go / Spring Boot / Android / iOS / Swift / Kotlin / Java / PHP / Laravel / Dart / databases / specialist roles)
- **CLI** with two main commands (`init` + `sync`)
- **MCP server** for runtime enforcement + audit logs
- **`.skillsrc`** project config file controlling which skills sync to which agents
- **`metadata.json`** registry-level settings for routing + composite rules

## How invocation works

```bash
# 1. Initialize: detect project tech stack
npx agent-skills-standard@latest init

# 2. Sync: distribute skills to your AI agent folders
npx agent-skills-standard@latest sync
```

The `sync` command:
- Reads canonical `skills/` source files
- Generates **native formats** for each AI agent your project uses:
  - Claude / Roo / OpenCode → command Markdown files
  - Cursor / Trae / Codex → skill folders with SKILL.md
  - Gemini → TOML command files
  - Copilot → prompt instruction files
  - MCP → tool definitions for runtime enforcement
- Distributes outputs into agent-specific directories (`.claude/`, `.cursor/`, etc.)

You only edit one canonical source; the CLI handles each agent's native format.

## How the 3-tier hierarchical lookup works (the "85% fewer tokens" claim)

Traditional approach: every prompt loads ALL rules. With 200+ standards, this is expensive.

agent-skills-standard's approach:

```
File edit / agent task
         ↓
[1] AGENTS.md router (~20 lines) — maps file extension → category index
         ↓
[2] Category _INDEX.md (~10-15 lines) — "File Match" or "Keyword Match" triggers
         ↓
[3] SKILL.md file (~500 tokens avg) — loaded ONLY when conditions match
```

Only ~25 lines scanned per edit instead of 3,600+ tokens. The cost drops from O(n) to O(1).

## The `.skillsrc` config

You configure which skills sync to which agents, plus framework exclusions and MCP scope:

```yaml
agents:
  - claude
  - cursor
  - copilot

exclusions:
  - flutter/getx     # we don't use GetX

custom_skill_paths:
  - ./team-rules/    # project-specific rules

mcp:
  scope: project     # project | user | snippets-only | disabled
```

## MCP runtime enforcement (optional)

If MCP scope is enabled, agent-skills-standard runs a **transparent interception** MCP server:
- Intercepts file read requests from your AI agent
- Auto-injects relevant skill rules into the output
- **No manual rule-fetching by the agent required** — rules apply automatically based on file context
- Provides **audit logs** showing which skills informed each AI decision

This is **lazy loading** — skills remain unloaded until triggered.

## Comparison table (from README)

| Aspect | Traditional Prompts | Skills Standard |
|--------|--------------------|------------------|
| Token overhead | 3,600+ per chat | ~500 per skill, loaded selectively |
| Maintenance | Rules drift across team | Single source of truth, version-controlled |
| Multi-tool portability | Copy-paste required | Native format generated per tool |
| Rule application | All rules scanned every time | ~25 lines scanned per edit via hierarchy |

## Security model

- **Text-only artifacts** — skills are Markdown/JSON; no executable code, no filesystem access, no network requests
- **CLI downloads text only** — no scripts, no binaries
- **Zero telemetry** — no usage data collected
- **Local-first** — project data stays on your machine
- **Prompt injection scanning** — skills automatically scanned for injection patterns
- **Automated evals** — `evals.json` validation tests AI adherence to each skill

## When NOT to use agent-skills-standard

- Your team has no existing standards (this is a distribution layer, not a standards generator)
- Your project uses only one AI agent and you're fine with prompt injection
- You need binary/executable skills (this is text-only by design)

## Fast facts

- 🌟 **496 stars** at 124 days = **4.0 stars/day** (sustained-low velocity)
- 🍴 **147 forks** = **fork ratio 0.296 CORPUS-RECORD-HIGH** (1.66× v65 17.8% prior record)
- ⚠️ **0 open issues** = corpus-record-low engagement-deficit (despite 147 forks)
- 📦 **10+ AI agents** supported via CLI-generated native formats
- 📚 **259 skills × 20+ frameworks** = corpus-record codification density
- 🏗️ Author **Nguyen Huy Hoang** — Senior Software Engineer at VMO Holding, **Hanoi, Vietnam**
- 📜 **Apache 2.0** (README mistakenly declares "MIT License")
