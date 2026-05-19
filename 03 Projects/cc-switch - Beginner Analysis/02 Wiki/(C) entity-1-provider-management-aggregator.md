# Entity 1 — cc-switch Provider-Management Aggregator

## 1. One-liner (VI/EN)

**EN:** Cross-platform desktop application managing 6 AI coding agent runtimes (Claude Code + Codex + Gemini CLI + OpenCode + OpenClaw + Hermes Agent) through unified UI with 50+ provider presets, MCP/Skills/Prompts unified management, atomic-write config protection, SSOT SQLite database, and Tauri 2 cross-platform binary distribution.

**VI:** Ứng dụng desktop cross-platform quản lý 6 AI agent runtimes (Claude Code + Codex + Gemini CLI + OpenCode + OpenClaw + Hermes Agent) qua giao diện thống nhất với 50+ provider preset, quản lý MCP/Skills/Prompts hợp nhất, bảo vệ config ghi atomic, SSOT SQLite, và phân phối binary cross-platform qua Tauri 2.

## 2. When to use / NOT to use

**Use when:**
- You use 2+ AI coding agent runtimes (Claude Code + Codex, etc.)
- You switch between provider API endpoints (Anthropic direct ↔ AWS Bedrock ↔ relay services)
- You need provider failover / circuit-breaker discipline
- You want unified MCP/Skills/Prompts across multiple runtimes
- You need cloud-sync of provider configs across devices
- You're in mainland China and use API relay services

**NOT use when:**
- You only use one AI coding agent runtime (overkill)
- You don't switch providers (cc-switch's value is switching)
- You need IDE integration (cc-switch is desktop app, not IDE plugin)
- You require headless/server deployment (cc-switch is GUI desktop app)

## 3. Entity vs sibling concepts

| Subject | Tier | Scope | Architecture |
|---------|------|-------|--------------|
| **cc-switch (v73)** | T1 multi-runtime aggregator | 6 runtimes + 50+ providers | Tauri 2 (Rust + TS) desktop |
| Claude Code (substrate) | T1 | 1 vendor (Anthropic) | npm CLI |
| DeepSeek-TUI (v72) | T1 | 1 primary + 8 alternatives | Rust TUI |
| agents-best-practices (v71) | T1 | Declarative skill | Markdown-only |
| codegraph (v70) | T2 | Code indexer (single-purpose) | TS MCP server |
| agentmemory (v66) | T2 | Memory service (single-purpose) | TS service |

**cc-switch's distinct positioning:** First corpus subject to manage MULTIPLE distinct agent runtimes through unified UI. Pattern #18 sub-archetype #8 candidate "multi-runtime-aggregator-desktop-app".

## 4. Sub-types

**By runtime managed:**
- Claude Code (hot-switch supported)
- Codex
- Gemini CLI
- OpenCode
- OpenClaw (workspace editor + provider-management)
- Hermes Agent

**By provider preset category:**
- Vendor-official (Anthropic / OpenAI / Google)
- Infrastructure (AWS Bedrock / NVIDIA NIM)
- Chinese relay (20+)
- Custom (user-supplied OpenAI-compatible endpoint)

**By management surface:**
- Providers (50+ presets)
- MCP servers
- Prompts (CLAUDE.md / AGENTS.md / GEMINI.md)
- Skills
- Sessions (conversation history)
- Proxy + failover

## 5. Anatomy

```
~/.cc-switch/
├── cc-switch.db                # SQLite SSOT
├── settings.json               # Device-level UI prefs
├── backups/                    # Auto-rotated (10 most recent)
├── skills/                     # Centralized skills repo
│   └── (symlinked to apps' skill dirs)
└── skill-backups/              # Pre-uninstall (20 most recent)
```

**Binary distribution:**
- `cc-switch` (Tauri desktop app) — single binary per platform
- macOS: code-signed + notarized
- Windows: MSI signed (likely)

## 6. Mechanism / How it works

**Provider switch flow:**

1. User clicks provider in main UI OR tray menu
2. cc-switch reads target runtime's config requirements (file paths, format)
3. **Atomic write:** Generates new config in temp file → renames over live file (corruption-resistant)
4. Updates SQLite SSOT with new active provider
5. Registers backfill watcher: any subsequent external edit to live file triggers DB update
6. For Claude Code: triggers hot-reload signal (no terminal restart)
7. For other runtimes: notifies user to restart terminal

**MCP server add flow:**

1. User adds MCP server via template OR custom config
2. cc-switch writes MCP server config to live MCP files for each of 4 apps
3. Bidirectional sync registered: external MCP edits in any app trigger backfill
4. Per-app toggle: disable in specific runtime if needed

**Skill install flow:**

1. User selects GitHub repo OR ZIP file
2. cc-switch downloads skill into `~/.cc-switch/skills/`
3. Creates symlinks (default) OR file copies to each app's skill directory
4. Backup snapshot taken before any uninstall

## 7. Out-of-box list

**11 bundled features (corpus-record):**

| Feature | Description |
|---------|-------------|
| 50+ provider presets | One-click import |
| 6 agent runtime targets | Claude Code / Codex / Gemini CLI / OpenCode / OpenClaw / Hermes Agent |
| MCP unified panel | Manage MCP servers across 4 apps |
| Prompts editor | CLAUDE.md / AGENTS.md / GEMINI.md unified |
| Skills system | GitHub repo OR ZIP install; symlink + file-copy modes |
| Session Manager | Cross-app conversation history |
| Workspace Editor | OpenClaw AGENTS.md / SOUL.md editing |
| Local Proxy | Format conversion + failover + circuit breaker |
| Usage Dashboard | Spending / tokens / requests tracking |
| Cloud Sync | Dropbox / OneDrive / iCloud / WebDAV |
| Deep-Link | `ccswitch://` URL protocol |

## 8. Configuration

**Primary config:** `~/.cc-switch/cc-switch.db` (SQLite)

**Device-level:** `~/.cc-switch/settings.json` (UI preferences, theme, auto-launch, etc.)

**Cloud sync:** Configure custom config directory pointed at Dropbox/OneDrive/iCloud/WebDAV folder.

**Themes:** Dark / Light / System

**Auto-launch:** Configurable in settings

**Auto-updater:** Built-in (uses Tauri's updater)

## 9. Recipes

### Minimal — install + first provider

```bash
brew install --cask cc-switch
open -a "CC Switch"
# Add Provider → choose Anthropic preset → paste API key → done
```

### Common — switch between Claude Code providers

```text
1. Open cc-switch
2. Click Anthropic Direct preset → Enable
3. Open terminal, run claude code
4. (Or use tray menu for instant switch — no app open needed)
```

### Common — multi-runtime sync via MCP

```text
1. Click MCP button → Add Server → choose template (e.g., filesystem MCP)
2. Toggle sync for: Claude Code + Codex + OpenCode + Gemini CLI
3. Apply
4. MCP server now appears in all 4 apps with bidirectional sync
```

### Common — Skills unified install

```text
1. Click Skills → Browse repos
2. Add GitHub repo URL (e.g., https://github.com/.../my-skill)
3. Click Install → cc-switch downloads + symlinks to all apps
4. Skill now available in Claude Code / Codex / OpenCode / Gemini CLI
```

### Advanced — local proxy with failover

```text
1. Open Proxy Settings
2. Add primary provider (Anthropic Direct)
3. Add backup provider (AWS Bedrock)
4. Enable circuit breaker
5. Set health-check interval (e.g., 30s)
6. cc-switch routes through proxy; auto-fails to backup on primary error
```

### Advanced — cloud sync across 3 devices

```text
1. On device 1: Settings → Cloud Sync → choose Dropbox
2. cc-switch syncs ~/.cc-switch/cc-switch.db to Dropbox folder
3. On devices 2+3: install cc-switch → Settings → Cloud Sync → point at same Dropbox folder
4. Provider configs now synced across all 3 devices
```

### Advanced — Deep-Link sharing

```text
Share provider config via URL:
ccswitch://provider/<base64-encoded-config>

Recipient clicks URL → cc-switch opens → import dialog → confirm
```

## 10. Advanced patterns

- **Failover chain:** Primary → backup → tertiary with auto-failover
- **App-level takeover:** Independently proxy specific apps (Claude through proxy, Codex direct)
- **Sponsor preset integration:** Sponsor-recommended providers pre-configured
- **Backup-restore workflow:** Auto-rotated backups every config change; restore individual snapshots
- **WSL support:** Windows Subsystem for Linux integration (per repo topics)
- **Workspace editor:** Edit AGENTS.md / SOUL.md with preview (OpenClaw workflow)
- **CHANGELOG-as-documentation:** 133KB CHANGELOG is itself reference documentation for feature evolution

## 11. Combination patterns

| Combination | Use case |
|-------------|----------|
| **Multi-runtime + Cloud sync** | Use Claude Code at home (Anthropic Direct) + Codex at office (corporate Bedrock) — provider state synced via iCloud |
| **MCP + Skills + Prompts** | Unified workflow setup across 4 apps — one config-edit propagates everywhere |
| **Proxy + Failover** | Production-grade reliability for API-dependent workflows |
| **Tray quick-switch + Per-app toggle** | Switch primary provider per-task without opening main UI |
| **Deep-Link + Sponsor presets** | One-click sponsor-partner provider setup via URL |

## 12. Anti-patterns / common mistakes

- **Editing config files externally while cc-switch is running** — Backfill protection handles this but may surface conflicts; prefer in-app editing
- **Deleting all providers** — cc-switch refuses to delete the active provider to prevent CLI tool breakage (minimum-1-config guarantee)
- **Skipping `brew upgrade` on macOS** — Homebrew cask may lag GitHub releases
- **Storing API keys in 20+ providers without rotation discipline** — Recommend periodic key rotation; use Custom Config Panel "Shared Config Snippet" for plugin config preservation
- **Trusting sponsor recommendations uncritically** — 20+ sponsors are commercial relationships; verify pricing/quality independently
- **Assuming OpenAI-compatible endpoint quirks** — Each preset may have slight differences (model name conventions, base URL format, auth scheme)

## 13. Related tools + cross-references + citations

### Vault cross-references

- **v72 DeepSeek-TUI** — Pattern #52 HIGH-NOT-EXTREME sister + Pattern #84 84c sister
- **v71 agents-best-practices** — Pattern #84 84c sister (declarative skill vs aggregator desktop)
- **v70 codegraph** — Pattern #18 sub-mechanism B sister (MCP server vs MCP client manager)
- **v69 CloakBrowser** — Pattern #66 signature-verification sister (artifact-layer vs config-layer)
- **v67 opencode-antigravity-auth** — OpenCode runtime managed by cc-switch (corpus subject reference)
- **v65 claude-code-system-prompts** — Claude Code runtime managed by cc-switch (corpus subject reference)
- **v62 codex-plugin-cc** — Codex runtime managed by cc-switch (corpus subject reference)
- **v66 agentmemory** — Pattern #18 sub-mechanism B B1 MCP integration sister
- **v61 cc-sdd** — "cc"-naming convention sister observation

### External references

- Homepage: https://ccswitch.io
- Trendshift listing: https://trendshift.io/repositories/15372
- Releases: https://github.com/farion1231/cc-switch/releases
- Documentation: docs/user-manual/en/README.md
- Changelog: CHANGELOG.md (133 KB)

### Pattern Library tags

- Pattern #18 sub-archetype #8 candidate (multi-runtime-aggregator-desktop-app)
- Pattern #21 SDD methodology layered-architecture sub-variant
- Pattern #28 50+ provider preset corpus-record
- Pattern #52 HIGH-NOT-EXTREME N=3 corpus-record sustenance
- Pattern #57 corpus-recursive STRONGEST (3+ subjects)
- Pattern #66 atomic-writes + SSOT + minimal-intrusion sub-mechanism candidate
- Pattern #78 12-layer LDS corpus-record
- Pattern #84 84c third-strengthening
- OC-Q "Sponsor-Density-As-Corpus-Signal" candidate
