# pi-coding-agent — Flagship terminal coding harness

**Entity type:** Core product (primary user surface)
**npm:** `@mariozechner/pi-coding-agent`
**Location:** `packages/coding-agent/` in `badlogic/pi-mono` monorepo
**Wiki version:** v1 (2026-04-23 — pi-mono wiki v1, 36th LLM Wiki)

---

## What it is

pi-coding-agent is the **flagship product** of pi-mono — an interactive terminal coding-agent CLI that competes directly with Claude Code, Cursor CLI, Codex CLI, and other standalone terminal coding harnesses. Installation is a single command:

```bash
npm install -g @mariozechner/pi-coding-agent
```

Then either `export ANTHROPIC_API_KEY=...` for API-key mode or run `pi` and use `/login` for OAuth subscription-mode against Anthropic/OpenAI/GitHub Copilot/Google/etc.

The root pi-mono README directs new users to this package first: *"Looking for the pi coding agent? See packages/coding-agent for installation and usage."* All other packages exist as foundation layers (pi-ai, pi-agent-core, pi-tui) or spin-off products (pi-mom, pi-pods, pi-web-ui).

**Tagline / positioning:** *"Adapt pi to your workflows, not the way around."* Minimal defaults + deep extensibility.

---

## Feature surface (~110 user-facing primitives)

### CLI (~25 flags)

Modes: `-p` print / `--mode json` / `--mode rpc` / `--export <in> [out]`
Model: `--provider`, `--model`, `--api-key`, `--thinking <level>`, `--models`, `--list-models`
Session: `-c` continue / `-r` resume / `--session` / `--fork` / `--no-session` / `--session-dir`
Tools: `--tools <list>` / `--no-tools`
Resources: `-e` extension / `--skill` / `--prompt-template` / `--theme` + `--no-*` variants
Context: `-nc` / `--no-context-files`
System prompt: `--system-prompt` / `--append-system-prompt`
Other: `--verbose`, `-h`, `-v`, `@file` inclusion prefix

### Slash commands (~20 built-in + dynamic)

Auth: `/login` `/logout`
Model: `/model` `/scoped-models`
Settings: `/settings`
Sessions: `/resume` `/new` `/name` `/session` `/tree` `/fork` `/clone` `/compact`
IO: `/copy` `/export` `/share` (GitHub gist)
Admin: `/reload` `/hotkeys` `/changelog` `/quit`
Dynamic: `/skill:<name>` `/<templatename>`

### Keybindings (~15, all configurable)

`Ctrl+C` clear (twice = quit) / `Escape` cancel (twice = `/tree`) / `Ctrl+L` model / `Ctrl+P` cycle / `Shift+Tab` thinking / `Ctrl+O` tool output / `Ctrl+T` thinking block / `Shift+Enter` multi-line / `Tab` path / `Ctrl+V` images / `@` file ref / `!cmd` bash+send / `!!cmd` bash-only / message queue: `Enter` steering / `Alt+Enter` follow-up / `Alt+Up` retrieve

### Built-in tools (7)

- Default 4: `read` / `write` / `edit` / `bash`
- Extended 3: `grep` / `find` / `ls`

Type-safe via TypeBox (from pi-ai tool-definition system).

### 4 resource types (hot-reloadable via `/reload`)

1. **Extensions** — TypeScript modules with full ExtensionAPI (events, tools, commands, UI, state) — **no sandboxing**
2. **Skills** — Agent Skills standard (Claude Code + Codex CLI compatible via companion pi-skills repo)
3. **Prompt templates** — markdown with variable expansion
4. **Themes** — visual customization

### ~38 configuration settings

Global `~/.pi/agent/settings.json` + project `.pi/settings.json` (merged). Notable: thinking level, theme, `steeringMode`/`followUpMode`, transport (sse/websocket/auto), context-file discovery, telemetry, auto-compaction, packages (npm:/git:/https: extension sources), extensions/skills/promptTemplates/themes paths, `npmCommand` (for nvm/n).

---

## Distribution: Pi Packages (corpus-first at T1)

Extensions distribute as npm or git packages via pi's own package manager:

```bash
pi install <source> [-l]   # npm:/git:/https:
pi remove <source>
pi update [source]
pi list
pi config
```

Sources in `settings.json`:
```json
"packages": [
  "npm:@foo/bar@1.0.0",
  "git:github.com/user/repo@v1"
]
```

Production install: `npm install --omit=dev`. Runtime deps MUST be in `dependencies` (not `devDependencies`).

Project-local (`-l` flag) vs global install paths.

---

## Session architecture

- **Format:** JSONL (one message per line)
- **Location:** `~/.pi/agent/sessions/` organized by working directory
- **Operations:** fork (branch from any previous message), clone (duplicate current branch), tree (navigate branches in-place), compact (manual or auto context summarization)
- **Export:** HTML (`/export` or `--export`); GitHub-gist share (`/share`)
- **Ephemeral mode:** `--no-session` — zero persistence

---

## Output modes (4)

1. **Interactive (default)** — full TUI with pi-tui differential rendering
2. **`-p` print** — non-interactive; prints response + exits
3. **`--mode json`** — newline-delimited JSON events for scripting
4. **`--mode rpc`** — process-integration RPC mode

Multi-mode + stdin piping + `@file` inclusion combine for powerful scripting:

```bash
cat README.md | pi -p "Summarize this"
pi --mode json @code.ts "Review" | jq '.messages[0].content'
```

---

## Platform support

Documented: Windows (Terminal setup), Termux (Android), tmux, standard Linux/macOS.

Node.js required (npm install global).

---

## MCP: explicitly excluded

From coding-agent docs:

> Build CLI tools with READMEs (see Skills), or build an extension that adds MCP support.

**Design philosophy:** pi deliberately excludes MCP. Alternatives provided:
- CLI tools with READMEs (model calls commands directly via bash tool)
- Agent Skills standard (declarative, hot-reloadable)
- Extensions (TypeScript, full system access)

This is **first T1-scale counter-evidence for Pattern #18 Agent Runtime Standardization at v36**. 38.9K-star T1 coding agent deliberately rejecting MCP-as-primary.

---

## Context file convention (AGENTS.md + CLAUDE.md)

pi natively loads both `AGENTS.md` and `CLAUDE.md` from project hierarchy. Disabled via `-nc`. System prompt can be:
- Replaced via `--system-prompt` or `SYSTEM.md`
- Appended via `--append-system-prompt` or `APPEND_SYSTEM.md`

**Cross-corpus note:** Reinforces Pattern #22 AGENTS.md-as-industry-standard. pi-mono's own 182-line AGENTS.md is parsed by pi-coding-agent itself (meta-usable: pi uses its own context-file convention to drive pi-development sessions).

---

## Storm Bear pilot notes

pi-coding-agent is a **plausible direct alternative to Claude Code** for Storm Bear operator workflows. Key pilot observations:

**Advantages over Claude Code:**
1. Multi-provider built-in (not Anthropic-subscription-locked; pi-ai 20+ providers including local vLLM/Ollama/LM Studio)
2. Export + share via GitHub gist + HF session publication = public workflow artifacts for Scrum-coach content marketing
3. Session forking + branching = experimental workflow exploration without losing history
4. Extension API = deeper customization than Claude Code plugins allow

**Disadvantages / friction:**
1. No MCP = existing MCP server investments incompatible without writing extensions
2. EN-only docs (no VN for VN-client context)
3. Heavier learning curve (110+ primitives)
4. Solo bus factor (Mario single-point)
5. 8.5-month-old project = less production-track-record than Claude Code

**Recommended pilot:** ~2 hours. Install `npm install -g @mariozechner/pi-coding-agent`. Run one Scrum-doc-session with full HTML export. Compare output quality with Claude Code baseline. Test pi-skills interop with existing Claude Code skills.

---

## Cross-references

- Cluster summaries: `(C) Cluster — pi-coding-agent CLI + extensions + skills.md` (parent source cluster); `(C) Cluster — Root README + 7-package monorepo + contribution gate.md` (monorepo context)
- Related entities: `(C) pi-ai + pi-agent-core — Foundation libraries.md`; `(C) Mario Zechner — Austrian solo-flagship + ecosystem portfolio.md`
- Cross-wiki peers: oh-my-claudecode v27 (architectural cousin — multi-runtime orchestration vs multi-package monorepo); claude-hud v35 (narrow T1 plugin vs broad T1 runtime); Everything Claude Code v1 / Superpowers v2 / spec-kit v17 (US-T1-corporate peers)
- Pattern observations: #18 MCP-exclusion counter-evidence / #22 AGENTS.md solo adoption refinement / #19 archetype 4 no-lineage 13th T1

---

*(C) Claude-generated 2026-04-23 per routine v2.1.*
