# Graphify × OpenCode — the "always-on" plugin mechanism

> **Source:** [[graphify-codebase-graph/_index]]. OpenCode = SST's open-source agent CLI ([opencode.ai](https://opencode.ai), [github.com/sst/opencode](https://github.com/sst/opencode)). Cross-ref [[claude-code-clones/_index]] (OpenCode is one of the named Claude Code clones).

## What OpenCode is

- **The open-source AI coding agent** by SST — terminal-first, project-rooted, slash-command-driven (the Claude Code UX), built in **TypeScript**, distributed via npm/Homebrew/Scoop.
- **Model-agnostic:** 75+ providers (Claude, GPT, Gemini, **Ollama / local models**) — vs Claude Code being Anthropic-locked. Free to self-host.
- Has switchable agents (Build = full access, Plan = read-only, General subagent) toggled with Tab.

## The two config conventions Graphify uses

- **`AGENTS.md`** — OpenCode's project-instruction file (the `CLAUDE.md` analog), in the repo root (global variant at `~/.config/opencode/AGENTS.md`). Sections like Tech Stack / Code Style / Architecture / Testing / Gotchas / Commands. *(Compatible with Claude Code + Cursor.)*
- **`opencode.json`** — config for models, tools, and **plugins** (project `./opencode.json` or global). Plugins are registered under a `plugin` field as npm packages or local paths.

## The plugin + hook system

- Plugins are **JS/TS modules** that export hook functions, loaded from `.opencode/plugins/` (project) or `~/.config/opencode/plugins/` (global), or as npm packages.
- They receive a context object (project, directory, worktree, client, Bun shell API) and return a hooks object.
- **Available hooks:** `tool.execute.before`, `tool.execute.after`, `file.edited`, `message.updated`, `session.created`, `shell.env`, `tui.prompt.append`.
- **`tool.execute.before`** fires *before* a tool runs — used for validation, cost control, blocking dangerous commands, and **context injection**. This is the one Graphify hooks.

## How Graphify wires in (`graphify opencode install`)

Running the install does three things under the hood, so you never have to remind the agent the graph exists:

1. **Writes a section into `AGENTS.md`** in the project root → tells the assistant to *check the knowledge graph before doing anything else.*
2. **Installs a plugin at `.opencode/plugins/graphify.js`** → it hooks `tool.execute.before` and **fires right before any bash tool call**, injecting a reminder into the output: *"the knowledge graph exists — read the graph report first before grepping around."*
3. **Registers itself in `opencode.json`** → no manual wiring.

> **Why the plugin matters:** without it, you'd have to *remember* to tell OpenCode about the graph every session. With it, **every new conversation has the graph context available without you typing anything** — that's what makes the token savings actually happen day-to-day, not just in theory.

## ⚠️ Caveats found in verification

- OpenCode's `raw` README 404'd during research; details came from `opencode.ai/docs` — low-level edge cases may differ.
- Community issues report **`tool.execute.before` not firing in some edge cases** (rtk-ai #1706) and **Graphify plugins not always appearing** in `~/.config/opencode/plugins` despite docs (Graphify #356, #755). **Verify the plugin actually fired** (look for the injected reminder) before trusting it's on.
- The same "always-on" pattern works for Claude Code via `CLAUDE.md` + a PreToolUse hook — OpenCode is just the video's chosen surface. See [[claude-code-hooks/_index]] for the Claude-Code primitive.

## Key Takeaways

- OpenCode mirrors Claude Code (`AGENTS.md` ≈ `CLAUDE.md`, `opencode.json` ≈ settings, plugins ≈ hooks) but is open-source + model-agnostic.
- Graphify's "always-on" trick = an **`AGENTS.md` instruction + a `tool.execute.before` plugin** that injects "read the graph first" before bash calls.
- The plugin is the load-bearing piece — it turns a static graph into a habit the agent can't skip.
- **Verify the hook fired** — there are open issues about it silently not installing/firing.
