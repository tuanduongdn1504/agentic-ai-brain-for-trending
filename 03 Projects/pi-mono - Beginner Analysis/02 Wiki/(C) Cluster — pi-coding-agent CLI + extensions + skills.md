# Cluster — pi-coding-agent CLI + extensions + skills

**Source:** `packages/coding-agent/README.md` + `packages/coding-agent/docs/` (extensions + settings docs)
**Fetch date:** 2026-04-23
**Cluster role:** Deep dive into the flagship package — primary user surface for pi

---

## Summary

`pi-coding-agent` (npm `@mariozechner/pi-coding-agent`) is pi's flagship — an interactive terminal coding-agent CLI positioned as *"minimal terminal coding harness"* with the mantra **"Adapt pi to your workflows, not the way around."** Installation is a single command: `npm install -g @mariozechner/pi-coding-agent`, followed by either `export ANTHROPIC_API_KEY=...` or `pi` + `/login` for OAuth subscription mode.

Feature surface is dense: **~25 CLI flags**, **~20 built-in slash commands** + dynamic `/skill:*` and `/template*`, **~15 keybindings** (customizable via `~/.pi/agent/keybindings.json`), **7 built-in tools** (default: read/write/edit/bash; extended: grep/find/ls), **4 resource types** (extensions, skills, prompt-templates, themes) with global + project-local discovery, **~38 configuration settings**, and **4 output modes** (interactive / print `-p` / JSON `--mode json` / RPC `--mode rpc`). Session data is JSONL-based under `~/.pi/agent/sessions/` with support for forking, cloning, branching, compaction, and HTML export + GitHub-gist sharing.

**Notable architectural deviation from corpus:** pi does NOT support MCP (Model Context Protocol) natively. Explicitly: *"Build CLI tools with READMEs (see Skills), or build an extension that adds MCP support."* This is **counter-evidence at T1 scale** for Pattern #18 Agent Runtime Standardization.

---

## Installation & auth

Three auth paths:

1. **API key** — `export ANTHROPIC_API_KEY=sk-ant-...` + run `pi` (works with any of 20+ providers)
2. **OAuth subscription** — `pi` → `/login` (supports Anthropic Claude Pro/Max, OpenAI ChatGPT Plus/Pro, GitHub Copilot, Google Gemini CLI, Google Antigravity)
3. **Custom** — via `~/.pi/agent/models.json` for OpenAI/Anthropic/Google-compatible endpoints (Ollama, vLLM, LM Studio, custom inference servers)

---

## CLI flag surface (~25)

**Modes:**
- `-p, --print` — non-interactive: print response and exit
- `--mode json` — newline-delimited JSON output for scripting
- `--mode rpc` — process-integration RPC mode
- `--export <in> [out]` — convert session JSONL to HTML

**Model:**
- `--provider <name>` / `--model <pattern>` / `--api-key <key>`
- `--thinking <level>` — off/minimal/low/medium/high/xhigh
- `--models <patterns>` — comma-separated for Ctrl+P cycling
- `--list-models [search]`

**Session:**
- `-c, --continue` / `-r, --resume` / `--session <path|id>` / `--fork <path|id>` / `--no-session` / `--session-dir <dir>`

**Tools:**
- `--tools <list>` / `--no-tools`

**Resources:**
- `-e, --extension <source>` / `--no-extensions`
- `--skill <path>` / `--no-skills`
- `--prompt-template <path>` / `--no-prompt-templates`
- `--theme <path>` / `--no-themes`
- `-nc, --no-context-files` — disable AGENTS.md / CLAUDE.md loading

**System prompt:**
- `--system-prompt <text>` — replace
- `--append-system-prompt <text>` — append

**Other:** `--verbose` / `-h` / `-v` / `@file.md` prefix for file inclusion

---

## Slash commands (~20 built-in + dynamic)

**Auth:** `/login` / `/logout`
**Model:** `/model` / `/scoped-models`
**Settings:** `/settings` (thinking level, theme, message delivery)
**Session navigation:**
- `/resume` — browse past sessions
- `/new` — start fresh
- `/name <name>` — set display name
- `/session` — info
- `/tree` — navigate session tree in-place
- `/fork` — create session from previous message
- `/clone` — duplicate current branch
- `/compact [prompt]` — manually compact context

**IO:**
- `/copy` — copy last assistant message to clipboard
- `/export [file]` — HTML export
- `/share` — upload as private GitHub gist

**Admin:**
- `/reload` — reload keybindings/extensions/skills/prompts/context
- `/hotkeys` — show all shortcuts
- `/changelog` — version history
- `/quit`

**Dynamic:**
- `/skill:<name>` — invoke skill
- `/<templatename>` — expand prompt template

---

## Keybindings (~15)

**Common:**
- `Ctrl+C` — clear editor (twice = quit)
- `Escape` — cancel/abort (twice = open `/tree`)
- `Ctrl+L` — model selector
- `Ctrl+P / Shift+Ctrl+P` — cycle scoped models
- `Shift+Tab` — cycle thinking level
- `Ctrl+O` — collapse/expand tool output
- `Ctrl+T` — collapse/expand thinking blocks
- `Shift+Enter` — multi-line
- `Tab` — path completion
- `Ctrl+V` — paste images
- `@` — fuzzy file reference
- `!command` — run bash + send output
- `!!command` — run bash WITHOUT sending output

**Message queue:**
- `Enter` — queue steering (delivered after current turn)
- `Alt+Enter` — queue follow-up (delivered after all work)
- `Escape` — abort + restore queued
- `Alt+Up` — retrieve queued

**Customization:** `~/.pi/agent/keybindings.json` — all bindings configurable; defaults in `DEFAULT_EDITOR_KEYBINDINGS` / `DEFAULT_APP_KEYBINDINGS`

---

## Built-in tools (7)

**Default four:** `read`, `write`, `edit`, `bash`
**Extended three:** `grep`, `find`, `ls`

All tools are **type-safe via TypeBox** (via `pi-ai`'s tool-definition system). Can be enabled/disabled via `--tools <list>` or `--no-tools`.

**Read-only mode example** (useful for code review without write access):
```bash
pi --tools read,grep,find,ls -p "Review the code"
```

---

## 4 resource types + discovery

Pi's extensibility is spread across 4 declarative primitives with **hot-reload** support (`/reload`):

### Extensions (TypeScript modules)

**What:** Custom tools, commands, event handlers, UI components, hooks, state persistence.

**Discovery paths:**
- `~/.pi/agent/extensions/*.ts` (global)
- `.pi/extensions/*.ts` (project-local)
- Subdirectories with `index.ts`
- Explicit paths in `settings.json` under `extensions` or `packages`

**API surface (ExtensionAPI):**
- `pi.on(event, handler)` — subscribe to 20+ lifecycle events
- `pi.registerTool()` / `pi.setActiveTools()`
- `pi.registerCommand()` / `pi.registerShortcut()`
- `pi.sendMessage()` / `pi.sendUserMessage()`
- `ctx.ui` UI primitives (select / confirm / input / editor / notify)
- `ctx.sessionManager` (read-only in handlers)
- `ctx.newSession()` / `ctx.fork()` / `ctx.switchSession()` (command-only to prevent deadlocks)

**Security warning (verbatim):**
> Extensions run with your full system permissions and can execute arbitrary code. Only install from sources you trust.

No sandboxing.

### Skills (Agent Skills standard)

**What:** Compliant with broader Agent Skills standard (compatible with Claude Code + Codex CLI per companion `pi-skills` repo).

**Invocation:** `/skill:<name>`

**Source:** pi-skills sibling repo (1.3K stars; Claude Code + Codex CLI interop).

### Prompt templates

**What:** Reusable markdown prompts with variable expansion.

**Invocation:** `/<templatename>`

### Themes

**What:** Visual customization; hot-reloadable.

**Flag:** `--theme <path>`

---

## ~38 configuration settings

**Locations:**
- `~/.pi/agent/settings.json` — global
- `.pi/settings.json` — project overrides (merged)

**Notable settings (per AGENTS.md + README):**
- Thinking level (default, per-session override)
- Theme selection
- `steeringMode` / `followUpMode` — message-delivery modes
- Transport preference (`sse` / `websocket` / `auto`)
- Context file discovery enable/disable
- Telemetry (`enableInstallTelemetry`)
- Auto-compaction behavior
- `packages` — list of npm:/git:/https: extension sources
- `extensions` / `skills` / `promptTemplates` / `themes` — path lists
- `npmCommand` — for nvm/n-based node-version-manager envs

Full reference: `docs/settings.md`.

**Environment variables:**
- `PI_CODING_AGENT_DIR` (default `~/.pi/agent`)
- `PI_PACKAGE_DIR`
- `PI_SKIP_VERSION_CHECK`
- `PI_TELEMETRY`
- `PI_CACHE_RETENTION=long` (extended prompt cache)
- `VISUAL` / `EDITOR` — external editor for Ctrl+G

---

## Pi Packages — bundled extension distribution

Unique to pi (corpus-first at T1): **extensions can be distributed as npm or git packages** and installed via pi's own package manager:

```bash
pi install <source> [-l]      # npm, git, or https
pi remove <source> [-l]
pi update [source]
pi list
pi config                     # enable/disable resources
```

Source syntax:
```json
"packages": [
  "npm:@foo/bar@1.0.0",
  "git:github.com/user/repo@v1"
]
```

**Production install:** `npm install --omit=dev` — runtime deps must be in `dependencies`, not `devDependencies`.

**Project-local vs global:** `-l` flag installs to `.pi/` for team sharing vs `~/.pi/agent/` for personal use.

---

## Context files (AGENTS.md + CLAUDE.md loading)

Pi automatically loads `AGENTS.md` and `CLAUDE.md` from project hierarchy (disabled via `-nc` / `--no-context-files`). System prompt can be:
- Replaced via `--system-prompt <text>` or `SYSTEM.md` file
- Appended via `--append-system-prompt <text>` or `APPEND_SYSTEM.md`

**Corpus-relevance:** pi-coding-agent natively consumes the same `AGENTS.md` industry convention tracked in Pattern #22 (AGENTS.md T1 absence — CANDIDATE v17). pi-mono itself has a 182-line AGENTS.md. **5th+ T1 data point** for AGENTS.md adoption.

---

## MCP explicit exclusion

From coding-agent docs (per probe):

> Build CLI tools with READMEs (see Skills), or build an extension that adds MCP support.

**Design philosophy:** pi deliberately excludes MCP in favor of:
- CLI tools with READMEs (let the model call commands directly)
- Agent Skills standard (declarative, hot-reloadable)
- Extensions (TypeScript modules, full system access)

This is **counter-evidence at T1 scale for Pattern #18 Agent Runtime Standardization** (CONFIRMED v15 primarily via MCP-consumer observations). 38.9K-star T1 coding agent deliberately rejecting MCP-as-primary is a stronger signal than claude-hud v35's narrow-plugin extension-point positioning.

---

## Platform support

Documented: Windows (Terminal setup considerations; Alt+Enter fullscreen remap needed), Termux (Android), tmux, standard Linux/macOS.

Node.js required (npm install global).

---

## Sample invocations (from README)

```bash
# Interactive with prompt
pi "List all .ts files in src/"

# Non-interactive
pi -p "Summarize this codebase"

# Piped stdin
cat README.md | pi -p "Summarize this text"

# Different model
pi --provider openai --model gpt-4o "Help me refactor"

# Model with thinking
pi --model sonnet:high "Solve this complex problem"

# Model cycling
pi --models "claude-*,gpt-4o"

# Read-only mode
pi --tools read,grep,find,ls -p "Review the code"

# Continue/browse/fork
pi -c
pi -r
pi --fork <path|id>
pi --no-session

# Extension
pi -e ./my-ext.ts

# File inclusion
pi @prompt.md "Answer this"
pi @code.ts @test.ts "Review these files"
```

---

## Cross-reference signals

- **Most similar corpus entry:** oh-my-claudecode v27 (solo ecosystem multi-runtime orchestration). But OMC wraps Claude Code + 3 other runtimes; pi **replaces** Claude Code.
- **Functional peer:** Claude Code itself (not yet a corpus wiki). pi is the OSS alternative.
- **Feature-superset over claude-hud:** pi-coding-agent is a full coding agent; claude-hud is a narrow display plugin for Claude Code. Different tiers of scope at same T1 archetype.
- **pi-skills sibling (1.3K stars):** Agent Skills interop layer — Claude Code + Codex CLI compatible.

---

*(C) Claude-generated 2026-04-23 per routine v2.1.*
