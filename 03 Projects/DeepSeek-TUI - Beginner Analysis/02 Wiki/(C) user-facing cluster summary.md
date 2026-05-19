# DeepSeek-TUI User-Facing Cluster Summary

**Scope:** README + Quickstart + Modes + key user-facing CLI commands
**Audience:** End-user / developer trying DeepSeek-TUI for first time
**Source files analyzed:** README.md (588 lines), docs/MODES.md (93 lines), README.zh-CN.md (excerpt), README.ja-JP.md (excerpt)

---

## 1. What it is

**Verbatim positioning (README line 3):** *"Terminal coding agent for DeepSeek V4. It runs from the `deepseek` command, streams reasoning blocks, edits local workspaces with approval gates, and includes an auto mode that chooses both model and thinking level per turn."*

**Synthesis:** Keyboard-driven coding agent in your terminal. Reads/edits files, runs shell, manages git, browses web, coordinates sub-agents. Built around DeepSeek V4 (1M token context, streaming reasoning) but supports 9+ providers.

## 2. First 90 seconds (Quickstart)

```bash
npm install -g deepseek-tui     # easiest — npm wrapper downloads Rust binaries
deepseek --version              # verify install
deepseek --model auto           # start TUI; auto-routes between v4-flash/v4-pro
```

First launch prompts for DeepSeek API key — saved to `~/.deepseek/config.toml`.

## 3. Three modes (Plan / Agent / YOLO)

| Mode | What it does | When to use |
|------|--------------|-------------|
| **Plan** | Read-only investigation; shell/patch disabled | Think-out-loud; produce plan for human review |
| **Agent** | Multi-step tool use; shell + paid tools need approval; file writes auto-allowed | Standard workflow |
| **YOLO** | Auto-approves all tools; enables trust mode | Trusted repos only |

Switch via `Tab` (cycle) / `/mode` (picker) / `/mode agent`, etc.

## 4. Reasoning-effort tiers

`Shift+Tab` cycles `off → high → max`. Auto mode chooses per-turn.

## 5. Auto mode (`--model auto`)

Before each turn, a small `deepseek-v4-flash` routing call selects the concrete model + thinking level. Short turns stay on Flash/off; complex work moves up to Pro + higher thinking. Sub-agents inherit auto mode unless overridden.

## 6. Key slash commands

- `/mode` — open mode picker
- `/model` — open model picker (uses provider's live catalog)
- `/provider` — switch API provider
- `/skills` — manage installable skill packs
- `/compact` — manage context (suggested at 60% per AGENTS.md)
- `/statusline` — toggle statusline; shows prefix-cache stability chip
- `/theme` — Catppuccin / Tokyo Night / Dracula / Gruvbox / light/dark
- `/trust` — enable trust mode (file access outside `--workspace`)
- `/config` — edit approval_mode (suggest/auto/never)

## 7. Sessions

```bash
deepseek -c                      # continue most recent session for workspace
deepseek -r <ID|PREFIX|latest>   # resume specific session
deepseek exec --resume <ID|PREFIX> <PROMPT>  # non-interactive resume
deepseek exec --continue <PROMPT>            # non-interactive continue
```

Sessions checkpoint automatically; can resume long-running work across restarts.

## 8. Workspace rollback

Side-git pre/post-turn snapshots (DOES NOT touch your repo's `.git`). Tools:
- `/restore` — restore from snapshot
- `revert_turn` — undo a turn's filesystem changes

## 9. Provider switching

```bash
# Switch to NVIDIA NIM
deepseek auth set --provider nvidia-nim --api-key "$NVIDIA_KEY"
deepseek --provider nvidia-nim
```

Supported providers (Pattern #84 84c evidence — 9-provider matrix):
- **Hosted:** DeepSeek (default) / NVIDIA NIM / AtlasCloud / OpenRouter / Novita / Fireworks
- **Generic:** OpenAI-compatible endpoint (`OPENAI_BASE_URL=...`)
- **Self-hosted:** SGLang / vLLM / Ollama

## 10. Cost tracking

- Per-turn + session-level token usage + cost estimates
- Cache hit/miss breakdown (DeepSeek prefix-cache)
- CNY display when session locale is `zh-Hans`
- **Honest deficiency disclosure (Pattern #83):** AGENTS.md notes "Token counting and cost estimation may be inflated due to thinking token accounting bugs. Use `/compact` to manage context, and treat cost estimates as approximate."

## 11. Skills system

11 bundled starter skills ship with first launch (`/skills`):
- `skill-creator` / `mcp-builder` / `plugin-creator` / `v4-best-practices` / `documents` / `presentations` / `spreadsheets` / `pdf` / `feishu` / `skill-installer` / `delegate`

Composable, installable skill packs from GitHub (Pattern #84 84c sub-mechanism evidence — skills are themselves provider-agnostic).

## 12. Localization

Localized UI: `en` / `ja` / `zh-Hans` / `pt-BR` (auto-detection). Corpus-record 4-locale T1 subject (previous corpus-record was CJK trio).

## 13. China-friendly install path

Mainland China users get explicit support:
- npm registry mirror: `--registry=https://registry.npmmirror.com`
- Cargo registry mirror (Tsinghua TUNA): config snippet provided
- `DEEPSEEK_TUI_RELEASE_BASE_URL` for mirrored release assets
- Tencent Cloud / CNB mirror / Lighthouse HK / Feishu integrations

## 14. Notifications (corpus-first 3-protocol)

Terminal-native notifications via OSC escape sequences:
- **OSC 9** — iTerm2 / WezTerm / Ghostty
- **OSC 99** — Kitty
- **OSC 777** — Ghostty
- Desktop notification fallback (when terminal doesn't support OSC)

## 15. Honest deficiency disclosures (Pattern #83 evidence — multi-surface)

User-facing surfaces with explicit deficiency disclosure:
- **Install README:** "Download safety: official release binaries... For manual downloads, verify the SHA-256 manifest and avoid look-alike repositories or search-result mirrors."
- **Scoop note:** "Scoop's manifest updates independently and can lag the GitHub/npm/Cargo release. Run `scoop update` first."
- **Cargo note:** "Requires Rust 1.88+ (the crates use the 2024 edition; older toolchains fail with 'feature `edition2024` is required'). Run `rustup update` first."
- **Linux ARM64 caveat:** "`npm i -g deepseek-tui` works on glibc-based ARM64 Linux from v0.8.8 onward."
- **Auto-mode router caveat:** "If the router call fails or returns an invalid answer, the app falls back to a local heuristic."

These disclosures pattern as **Pattern #83 83b methodology-disclosure** + **83d experimental-status-disclosure** within-pattern strengthening evidence.

---

**Cross-reference:** Pattern Library Implications → `entity-3-pattern-library.md`. Distribution + Multi-Provider details → `entity-2-distribution-multi-provider.md`. Coding-agent internals → `entity-1-coding-agent.md`.
