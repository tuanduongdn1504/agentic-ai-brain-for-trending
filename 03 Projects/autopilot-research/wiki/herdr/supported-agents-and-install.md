# Supported agents & install

## Source
- [herdr.dev/docs/agents](https://herdr.dev/docs/agents/) + README install section (verified 2026-07-18).

## The 21 detected agents (zero-config)

Herdr detects **21 coding agents out of the box**, no configuration:

Pi · OMP · GitHub Copilot CLI · Devin CLI · Kimi Code CLI · Hermes Agent · Qoder CLI · Droid · OpenCode · Kilo Code CLI · MastraCode · **Claude Code** · **Codex** · Cursor Agent CLI · Amp · **Grok CLI** · Antigravity CLI · Kiro CLI · Maki · Gemini CLI · Cline

- **Gemini CLI** and **Cline** are noted as *"less thoroughly tested."*
- ⚠️ Videos that say "15+ agents" are **true but undercount** — the real number is **21** as of v0.7.4. [context for C09]
- The list spans essentially every major coding harness (Anthropic Claude Code, OpenAI Codex, xAI Grok, Cognition Devin, GitHub Copilot, plus OpenCode/Cursor/Amp/Kilo/etc.) — this cross-harness reach is the whole point (Claude Code's own `agent view` only covers Claude Code). See [[competitive-landscape]].

## Install

| Platform | Command |
|---|---|
| **macOS** | `brew install herdr` · or `curl -fsSL https://herdr.dev/install.sh \| sh` · or `mise use -g herdr` |
| **Linux** | `curl -fsSL https://herdr.dev/install.sh \| sh` · or `mise use -g herdr` |
| **Windows** | **BETA** — `powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 \| iex"` |

- A **Homebrew formula** exists (`formulae.brew.sh/formula/herdr`). Prebuilt binaries per release (linux-aarch64/x86_64, macos-aarch64) are on the [releases page](https://github.com/ogulcancelik/herdr/releases).
- Start with `herdr`; detach with `ctrl+b q`; reattach with `herdr`.
- ⚠️ **Windows is beta** — the anchor's "works on Windows and Mac" is true but omits the beta qualifier; there's an open Windows-specific detection bug (#1514). [CORRECT-BUT-INCOMPLETE — C13; see [[license-and-adoption-caveats]]]

## Agent skill & plugins

- **Agent skill** — a one-line install adds a skill that teaches your agents how to drive Herdr (spawn panes, create/organize sessions) via the socket API. [[architecture-and-detection]]
- **Plugin marketplace** — real (herdr.dev/plugins). Independently-confirmed community plugins: **herdr-file-viewer** (`smarzban`, 156★ — git-aware read-only file viewer TUI) and **herdr-mirror** (`nikok6`, 35★ — mirror remote Herdr servers into your local sidebar over SSH). Ecosystem is young and community-maintained. (A "reviewer" plugin referenced in one video could not be located — do not rely on it.) [MISLEADING re: specific plugin — C22]

## Related
- [[architecture-and-detection]] · [[competitive-landscape]] · [[license-and-adoption-caveats]]
