# DeepSeek-TUI Technical / Distribution Cluster Summary

**Scope:** Architecture, packaging, multi-provider matrix, OS sandbox, MCP/LSP integration, RLM internals
**Audience:** Technical evaluator + integrator + deployment engineer
**Source files analyzed:** docs/ARCHITECTURE.md (305 lines), docs/INSTALL.md (excerpt), docs/MCP.md (226 lines), docs/SUBAGENTS.md (178 lines), docs/MODES.md (93 lines), README.md install section

---

## 1. Distribution architecture — 5 packaging methods (corpus-record)

| Method | Command | Notes |
|--------|---------|-------|
| **npm** | `npm install -g deepseek-tui` | Downloads matching prebuilt Rust binaries from GitHub Releases; npm package is installer-wrapper not agent runtime |
| **Cargo** | `cargo install deepseek-tui-cli --locked && cargo install deepseek-tui --locked` | No Node needed; requires Rust 1.88+ (2024 edition; `let_chains` stable) |
| **Homebrew** | `brew tap Hmbown/deepseek-tui && brew install deepseek-tui` | macOS package manager |
| **Docker** | `ghcr.io/hmbown/deepseek-tui:latest` | Prebuilt release image |
| **Direct download** | GitHub Releases | Prebuilt for Linux x64/ARM64, macOS x64/ARM64, Windows x64; verify SHA-256 manifest |

**Prior corpus-record:** 3-4 packaging methods (e.g., v66 agentmemory npm+pip+docker, v70 codegraph npm+docker). **DeepSeek-TUI = 5-packaging-method corpus-first.**

**Update commands per install path:**

```bash
deepseek update                              # release-binary updater (canonical)
npm install -g deepseek-tui@latest           # npm wrapper
brew update && brew upgrade deepseek-tui     # Homebrew
cargo install deepseek-tui-cli --locked --force
cargo install deepseek-tui     --locked --force
```

## 2. Two-binary architecture (corpus-first Pattern #18 sub-mechanism candidate)

`deepseek` (CLI dispatcher) + `deepseek-tui` (companion ratatui binary) ship as **SEPARATE executables**.

```
deepseek (dispatcher CLI)
   └─→ resolves and spawns deepseek-tui as sibling on PATH for interactive use
deepseek-tui (TUI runtime)
   └─→ ratatui interface ↔ async engine ↔ OpenAI-compatible streaming client
```

**Why split:** Update-path isolation + hot-reload of TUI without dispatcher restart + cross-compilation strategy isolation + headless `deepseek serve` path separate from interactive TUI.

**Distinct from v70 codegraph's Pattern #18 sub-mechanism B (one-binary-many-CLIENTS via MCP/CDP):** DeepSeek-TUI is one-dispatcher-spawns-companion-binary architecture. Candidate for **NEW Pattern #18 sub-mechanism C "dispatcher-companion-binary-split"**.

## 3. Internal architecture (docs/ARCHITECTURE.md synthesis)

```
deepseek-tui (ratatui interface)
   ↕
async engine
   ├── session state + turn tracking
   ├── durable task queue (survives restarts)
   ├── LSP subsystem (rust-analyzer / pyright / typescript-language-server / gopls / clangd)
   ├── typed tool registry (shell / file ops / git / web / sub-agents / MCP / RLM)
   └── OpenAI-compatible streaming client
       ↕
   API provider (DeepSeek / NVIDIA / OpenRouter / etc.)
```

**Post-edit LSP diagnostics** are fed into model context BEFORE next reasoning step — corpus-first explicit LSP-in-the-loop discipline.

## 4. 9-Provider Matrix (Pattern #84 84c FIRST POST-PROMOTION STRENGTHENING)

| Provider | Type | Auth | Models |
|----------|------|------|--------|
| **DeepSeek** | Hosted (default) | API key → `~/.deepseek/config.toml` | `deepseek-v4-pro` / `deepseek-v4-flash` |
| **NVIDIA NIM** | Hosted | API key | Provider-specific catalog |
| **AtlasCloud** | Hosted | API key | Provider-specific catalog |
| **OpenRouter** | Hosted aggregator | API key | `deepseek/deepseek-v4-pro` + 200+ models |
| **Novita** | Hosted | API key | `deepseek/deepseek-v4-pro` |
| **Fireworks** | Hosted | API key | `deepseek-v4-pro` |
| **Generic OpenAI-compatible** | Hosted/Self-hosted | API key + `OPENAI_BASE_URL` | Any (e.g., glm-5) |
| **SGLang** | Self-hosted | `SGLANG_BASE_URL` | `deepseek-v4-flash` |
| **vLLM** | Self-hosted | `VLLM_BASE_URL` | `deepseek-v4-flash` |
| **Ollama** | Self-hosted | (default localhost) | `deepseek-coder:1.3b` + any Ollama model |

**Provider switching:**
```bash
deepseek auth set --provider <name> --api-key "$KEY"
deepseek --provider <name>
```

Inside TUI: `/provider <name>` switches directly; `/model <id>` uses provider's live catalog (provider-aware defaults as fallback).

**Significance:** DeepSeek-TUI provides 9-provider matrix beyond v71 agents-best-practices' dual-vendor synthesis (Anthropic + OpenAI). **FIRST POST-v72-AUDIT 84c sub-mechanism strengthening — N=2 within sub-mechanism reached at v72 wiki itself (0-wiki gap from v72 audit registration).**

## 5. OS-Level Sandbox (corpus-first 3-platform integration)

| Platform | Sandbox technology | Scope |
|----------|---------------------|-------|
| **macOS** | Seatbelt | Workspace-scoped filesystem access |
| **Linux** | Landlock | Workspace-scoped filesystem access |
| **Windows** | Job Objects | Workspace-scoped filesystem access |

Shell commands run with workspace-scoped FS access only. Trust mode (`/trust`) opens access outside workspace. YOLO mode auto-enables trust mode.

**Pattern #66 Supply-Chain Isolation evidence:** OS-native sandboxing primitives + workspace-boundary as default + explicit opt-in for cross-workspace access.

## 6. MCP integration (Pattern #78 + Pattern #18 evidence)

DeepSeek-TUI is **MCP CLIENT** — connects to Model Context Protocol servers for extended tooling. Distinct from v66 agentmemory + v70 codegraph which are MCP SERVERS.

**MCP tool surface (docs/MCP.md):**
- MCP tools exposed as `mcp_<server>_<tool>` namespace
- Same approval flow as built-in tools (per-mode rules)
- Read-only MCP helpers may auto-run in `suggest` approval mode
- MCP tools with side effects require approval

`deepseek mcp ...` for MCP server management commands.

## 7. LSP integration (corpus-first 5-language-server integration)

Inline error/warning surfacing after EVERY edit via 5 language servers:

| Language | LSP server |
|----------|-----------|
| Rust | rust-analyzer |
| Python | pyright |
| TypeScript/JavaScript | typescript-language-server |
| Go | gopls |
| C/C++ | clangd |

Post-edit diagnostics fed into model context BEFORE next reasoning step. Corpus-first explicit LSP-in-the-loop discipline.

## 8. Native RLM (REPL Language Mode) — corpus-first batch-analysis primitive

**Purpose:** persistent REPL sessions for batched analysis over large files / papers / logs / structured payloads.

**Tool surface:**
- `rlm_open` — open persistent REPL session
- `rlm_eval` — run focused Python; loaded source is `_context` with `content` convenience alias
- `rlm_configure` — set `sub_query_timeout_secs` for child calls
- `rlm_close` — close session
- Helpers inside REPL: `peek` / `search` / `chunk` / `sub_query_batch` (fans out 1-16 cheap parallel child calls pinned to `deepseek-v4-flash`)
- `finalize(...)` + `handle_read` for bounded retrieval

**Use cases:** Categorize 15 files / inspect a paper / mine a long log / batch classification without dumping repeated reads into parent transcript.

## 9. Sub-agents — concurrent task queue

**Tool surface (docs/SUBAGENTS.md):**
- `agent_open` — non-blocking launch; child gets fresh context + tool registry
- `agent_eval` — assign additional work to child OR retrieve detail beyond summary
- `agent_close` — close completed session

**Pool capacity:** default 10 concurrent sub-agents; configurable to 20 via `--max-subagents`.

**Completion notification:** structured `<deepseek:subagent.done>` event with summary + evidence list + execution metrics. Parent reads `summary` field; calls `agent_eval` ONLY if summary insufficient.

**Bounded result retrieval:** Large transcripts parked behind `var_handle` references. Model calls `handle_read` for slices / ranges / JSONPath projections — keeping parent context lean.

**Pattern #21 sub-variant candidate** — "concurrent-sub-agent-pool-with-completion-events" architecture. Distinct from v71 agents-best-practices' 7-invariant single-loop architecture (DeepSeek-TUI runs N children concurrently; v71's 7-invariant runs one loop sequentially).

## 10. Durable task queue

Background tasks can survive restarts. Task queue persisted to disk; resumes on next launch.

Combined with session save/resume (`deepseek -c` / `deepseek -r <ID>`), enables multi-day workflows.

## 11. HTTP/SSE runtime API (corpus-first headless agent workflow path)

```bash
deepseek serve --http   # starts HTTP/SSE runtime
```

For headless agent workflows + backend wrappers + harness integration. Runtime stays bound to localhost (Tencent Cloud / CNB deployment notes: EdgeOne is NOT used to expose `/v1/*`).

`deepseek exec --output-format stream-json <PROMPT>` for stream-JSON output one object per line (harness-friendly).

## 12. Session save/resume

Checkpoint long-running sessions to disk. Resume via:

```bash
deepseek -c                                  # continue most recent session for workspace
deepseek -r <ID|PREFIX|latest>               # resume specific session
deepseek exec --resume <ID|PREFIX> <PROMPT>  # non-interactive resume
deepseek exec --continue <PROMPT>            # non-interactive continue
```

## 13. Workspace rollback (corpus-rare side-git discipline)

Pre/post-turn snapshots via side-git that does NOT touch your repo's `.git`. Operations:
- `/restore` — restore from snapshot
- `revert_turn` — undo turn's filesystem changes

Side-git lives outside the active `.git/` to avoid contaminating the user's repository state with agent-internal snapshots. Corpus-first explicit "agent state separate from user repo state" discipline.

## 14. Notifications — 3 OSC protocols (corpus-first terminal-emulator protocol awareness)

Terminal-native notifications via OSC escape sequences (selected by terminal emulator):
- **OSC 9** — iTerm2 / WezTerm / Ghostty
- **OSC 99** — Kitty
- **OSC 777** — Ghostty (alternative)
- Desktop notification fallback (when terminal doesn't support OSC notifications)

## 15. Localization architecture (corpus-record 4-locale T1)

| Locale | Coverage |
|--------|----------|
| `en` | Default |
| `ja` | Japanese (full README + UI) |
| `zh-Hans` | Simplified Chinese (full README + UI + CNY currency display) |
| `pt-BR` | Brazilian Portuguese (UI) |

Auto-detection from system locale; manual override available.

**Significance:** Prior corpus-record was CJK trio (3-locale at v54 fish-speech). DeepSeek-TUI = **4-locale T1 subject corpus-first** (CJK trio + Latin/Romance language coverage extends beyond Asian-script-only corpus norm).

---

## Technical Cross-References

- **Pattern Library implications** → `entity-3-pattern-library.md`
- **End-user experience** → `user-facing cluster summary.md` + `entity-1-coding-agent.md`
- **Contributor governance** → `contributor-facing cluster summary.md` + AGENTS.md
- **Storm Bear vault-deployment** → `entity-4-storm-bear.md` (vendor-diversification pilot recommendation)

## Corpus-Distinguishing Properties

| Property | DeepSeek-TUI value | Prior corpus value |
|----------|---------------------|--------------------|
| Packaging methods | **5** | 3-4 (corpus-record at v66/v70) |
| Provider matrix | **9** | 2 (v71 dual-vendor) |
| OS sandbox platforms | **3** | 0-1 (most corpus subjects) |
| LSP language servers | **5** | 0-1 |
| Locales | **4** | 3 (CJK trio) |
| Velocity sustained | **267/d × 120d** | 172/d × 86d (v69 HIGH-NOT-EXTREME N=1) |
| Stars at age | **32K at 120d** | 5K at 121d (v70 codegraph) / 14.8K at 86d (v69 CloakBrowser) |
