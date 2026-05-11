# ClaudeKit architecture — 4 pillars + 4 layers

## What ClaudeKit IS

A **framework integrated into Claude Code's `.claude/` directory** (or `~/.claude/` global). NOT a standalone IDE. NOT an AI model provider. NOT a replacement for Claude Code. It's a **professional automation system** that sits on top of native Claude Code, adding structured commands + agents + hooks.

Philosophy per the docs: equip Claude with a "super-powered toolbox" and coordinate a "team of specialists" for complex tasks. Move user from manual "chatting" to structured "commands".

## The 4 pillars

| Pillar | Role | Concrete artifact |
|---|---|---|
| **Agents** (Specialists) | Single-domain AI agents — Planner, Tester, Reviewer, Architect, Builder, Inspector, Debugger | Configured prompts + internal tools per role |
| **Skills** (Knowledge) | Specialized knowledge packages — primary execution units triggered by slash commands | `SKILL.md` files with deep prompts, references, scripts |
| **Workflows** (Process) | Combinations of Hooks + Skills + Agents that run sequentially for end-to-end task cycles | `/ck:cook` = research → plan → implement → test → review pipeline |
| **Hooks** (Automation) | Background scripts reacting to lifecycle events (session start, tool call, completion) | `session-init.cjs`, `session-state.cjs`, `privacy-block.cjs`, `git-manager` |

## Pillar interaction (lifecycle)

1. **Initialization** — Hooks fire on session start: detect project type, load rules, restore previous session
2. **Triggering** — user invokes Workflow via slash command (e.g., `/ck:cook "add login button"`)
3. **Execution** — system identifies required Agents and runs them sequentially
4. **Completion** — Hooks handle state-saving, commit, doc updates

Full lifecycle detail: [[request-lifecycle]].

## The 4 architectural layers

### 1. Integration layer

Lives in `.claude/` (project-local) or `~/.claude/` (global). Enhances rather than replaces existing Claude Code setup. Selective merging preserves user's existing `settings.json` entries.

### 2. Orchestration layer

Manages "agentic" behavior — specialized agents in structured pipelines. Example: `/ck:fix` 6-phase pipeline (Scout → Diagnosis → Routing → Fix → Verification → Prevention). Prevents infinite loops by halting after 3 failed attempts ("wicked problem" detection).

### 3. Runtime layer — CCS (Claude Code Switch)

Multi-provider abstraction. ClaudeKit commands can route through different providers based on cost, reasoning depth, rate limits:
- Claude Pro / Team / Enterprise (Anthropic native)
- GPT (via OpenAI)
- GLM (Chinese alternative)
- Kimi (Moonshot)
- Codex (via `ck migrate` + Codex CLI)

**Important caveat:** CCS does NOT generate more quota. Multiple accounts sharing a common upstream pool will still hit limits.

### 4. Compatibility layer — `ck migrate`

Ports ClaudeKit's "intelligence layer" (agents, skills, rules) to other AI coding tools:
- **Cursor** — converts rules into `.cursorrules`
- **Windsurf**
- **Codex** (OpenAI's CLI)
- **Droid**
- Several others

Migration modes:
- `--install` — manual selection
- `--reconcile` — automatic sync via checksums
- `--dry-run` — preview changes before writing

## Why this matters for personal harness

The 4-pillar / 4-layer separation is itself an architectural idea worth borrowing regardless of whether you adopt ClaudeKit:
- **Agents = specialization** (don't run one prompt for everything)
- **Skills = knowledge packaging** (`SKILL.md` files as composable, reusable units)
- **Workflows = sequencing** (explicit phase structure for multi-step tasks)
- **Hooks = automation** (deterministic background work, NOT model-decided)

This separation echoes Lopopolo's harness engineering ([[external|harness-engineering/blog-talk-evolution#high-leverage-missing-from-talk-content|Layers, Skills, Doc-Gardening]]) and operationalizes several of Mnilax's 12 rules ([[external|claude-md-12-rules/the-12-rules]]).

See [[vs-harness-engineering-and-12-rules]] for the comparison matrix and adoption recommendations.

## Key Takeaways

- ClaudeKit ≠ Claude Code replacement; it's a configuration framework layered on top
- 4 pillars (agents / skills / workflows / hooks) + 4 architectural layers (integration / orchestration / runtime / compatibility)
- CCS multi-provider routing is a unique-to-ClaudeKit capability not in raw Claude Code or harness-engineering's Symphony
- Portability via `ck migrate` reduces vendor lock-in — distinct from harness-engineering's OpenAI-only stack
- The separation of concerns (pillars + layers) is borrowable architectural idea even without adopting the product
