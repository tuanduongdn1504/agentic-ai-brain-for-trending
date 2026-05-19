# cc-switch Technical / Distribution Cluster Summary

**Scope:** Architecture, packaging, multi-runtime aggregation, distribution channels, sync mechanisms
**Audience:** Technical evaluator + deployment engineer + integrator

---

## 1. Distribution architecture — 9 packaging channels (corpus-record)

| Channel | Format | Install command |
|---------|--------|-----------------|
| **Homebrew (macOS)** | Cask | `brew install --cask cc-switch` |
| **Arch Linux** | AUR | `paru -S cc-switch-bin` |
| **Windows MSI** | Installer | Download from Releases |
| **Windows Portable** | ZIP | Download from Releases |
| **macOS DMG** | Disk image (code-signed + notarized) | Download from Releases |
| **macOS ZIP** | Archive | Download from Releases |
| **Linux deb** | Debian package | Download from Releases (Debian/Ubuntu) |
| **Linux rpm** | RPM package | Download from Releases (Fedora/RHEL/openSUSE) |
| **Linux AppImage** | Universal | Download from Releases |
| **Flatpak** | User-build only | See `flatpak/README.md` for build instructions |

**Prior corpus-record:** v72 DeepSeek-TUI 5 packaging methods. **cc-switch v73 = 9 packaging methods = NEW corpus-record T1 subject.**

## 2. Internal architecture (Tauri 2 cross-platform desktop)

```
deepskinned architecture:

Frontend (React + TS + Vite)
   ├── Components (UI)
   ├── Hooks (Business Logic)
   └── TanStack Query (Cache/Sync)
   ↕ Tauri IPC
Backend (Tauri + Rust)
   ├── Commands (API Layer)
   ├── Services (Business Layer)
   │   ├── ProviderService
   │   ├── McpService
   │   ├── ProxyService
   │   ├── SessionManager
   │   ├── ConfigService
   │   └── SpeedtestService
   └── Models/Config (Data Layer)
       ├── SQLite (cc-switch.db) — SSOT
       └── JSON (settings.json) — device-level settings
```

**Build toolchain:**
- Frontend: `pnpm` + Vite + Vitest
- Backend: Cargo + Tauri CLI 2.8+
- Production: `pnpm tauri build` → platform-specific installer

## 3. 6 agent runtime targets (Pattern #84 84c third-strengthening + Pattern #18 sub-archetype #8 candidate)

| Runtime | Vendor | Hot-switch | cc-switch role |
|---------|--------|------------|-----------------|
| **Claude Code** | Anthropic | ✅ Yes | Hot-switches provider data without terminal restart |
| **Codex** | OpenAI | ❌ No | Requires terminal restart |
| **Gemini CLI** | Google | ❌ No | Requires terminal restart |
| **OpenCode** | Community | ❌ No | Requires terminal restart |
| **OpenClaw** | Community fork | ❌ No | Workspace editor for AGENTS.md / SOUL.md |
| **Hermes Agent** | Community | ❌ No | Provider-management only |

**Each runtime has distinct config format:**
- Claude Code: `~/.claude/` directory with multiple files (Markdown CLAUDE.md + JSON settings)
- Codex: TOML config
- Gemini CLI: `~/.gemini/` directory
- OpenCode: TOML/JSON variant
- OpenClaw: Forked from OpenCode with AGENTS.md/SOUL.md additions
- Hermes Agent: Project-specific format

**cc-switch handles all 6 formats** via per-runtime adapter logic.

## 4. 50+ provider preset library (Pattern #28 corpus-record)

**Provider categories:**

| Category | Providers (selected) |
|----------|----------------------|
| Anthropic official | Direct + AWS Bedrock + OAuth flow |
| OpenAI / Codex | Official + relay services |
| Google / Gemini | Official + relay |
| NVIDIA | NIM |
| Chinese API relay (20+) | PackyCode + AIGoCode + Shengsuanyun + AICodeMirror + PatewayAI + BytePlus + SiliconFlow + Cubence + DMXAPI + Compshare + AICoding + Crazyrouter + RightCode + SSSAiCode + Micu + LemonData + CTok + ClaudeAPI + ClaudeCN + RunAPI + Pateway + others |
| Custom / OpenAI-compatible | User-supplied endpoint |
| OpenCode / OpenClaw | Universal config sync |

**Per-preset config includes:**
- API endpoint URL
- Auth scheme (API key / OAuth / Bearer)
- Default model
- Format conversion rules (if needed)
- Health-check endpoint

## 5. Provider switching mechanism

**Switch flow:**
1. User selects provider in UI OR clicks tray menu
2. cc-switch writes live config files for selected runtime (atomic write: temp + rename)
3. Database updated with new active provider
4. Backfill registered: any subsequent edits to live config trigger DB update
5. For Claude Code: hot-switch — no terminal restart needed
6. For other runtimes: user notified to restart terminal/CLI tool

## 6. Local proxy + failover (corpus-rare advanced feature)

**Local proxy with hot-switching:**
- Translates between provider API formats (e.g., Anthropic → OpenAI-compatible mid-request)
- Provides single endpoint that routes to multiple providers
- Hot-switch active provider without changing client-side config

**Auto-failover:**
- When primary provider fails (rate-limit, error, timeout), automatically switch to backup
- Circuit breaker pattern — backoff on repeated failures
- Provider health monitoring dashboard

**App-level takeover:**
- Independently proxy Claude / Codex / Gemini
- Per-runtime + per-provider granularity

**Pattern Library implication:** Proxy + failover at desktop app layer = corpus-first multi-runtime proxy aggregation. Sister to v67 opencode-antigravity-auth (T4 Bridge OAuth proxy) but at multi-runtime layer rather than single-vendor-bridge layer.

## 7. Cloud sync (4 destinations)

- **Dropbox** — sync via Dropbox API
- **OneDrive** — sync via OneDrive API
- **iCloud** — macOS-native iCloud Drive
- **WebDAV** — custom WebDAV server (self-hosted)

**Implementation:**
- Custom config directory pointed at cloud-sync folder
- SQLite + JSON files synced as opaque blobs
- Conflict resolution via timestamp + version

## 8. MCP integration (Pattern #78 LDS evidence)

**MCP servers managed across 4 of 6 apps:**
- Unified add/edit UI
- Bidirectional sync (write to all 4 apps' MCP config; backfill from any external change)
- Deep-link import (`ccswitch://mcp/...`)
- Template + custom config support
- Per-app toggle (enable/disable MCP server in specific runtime)

## 9. Skills system (corpus-rare unified skills management)

**Centralized storage at `~/.cc-switch/skills/`:**
- Symlinked to each app's expected skills directory (default)
- File-copy mode (per-user opt-in for non-symlink-supported scenarios)
- One-click install from GitHub repos OR ZIP files
- Custom skill repository management (point at own GitHub fork)
- Auto-backup before uninstall (`~/.cc-switch/skill-backups/` keeps 20 most recent)

**Pattern Library implication:** Multi-runtime skill sync = first corpus subject to formalize cross-runtime skill portability at desktop-management layer.

## 10. Prompts system (cross-app prompt sync)

- Markdown editor with preview
- Activate prompt → sync to live files (CLAUDE.md / AGENTS.md / GEMINI.md per runtime)
- Backfill protection (detect external edits to prompt files; prompt user to reconcile)

## 11. Session Manager (cross-app history)

- Browse / search / restore conversation history
- Works across all 6 supported apps
- Persisted to SQLite for fast search

## 12. Deep-Link URL protocol (`ccswitch://`)

**Import via URL:**
- `ccswitch://provider/...` — add provider preset
- `ccswitch://mcp/...` — add MCP server
- `ccswitch://prompt/...` — add prompt template
- `ccswitch://skill/...` — install skill

**Use case:** Sponsor partner sites OR community config sharing OR documentation links.

**Pattern Library implication:** First corpus subject with explicit deep-link URL protocol for config import. Could be Pattern Library candidate at v76+ if v76+ subject adopts similar pattern.

## 13. Data storage layout

| Path | Contents | Type |
|------|----------|------|
| `~/.cc-switch/cc-switch.db` | SQLite — providers, MCP, prompts, skills | SSOT |
| `~/.cc-switch/settings.json` | Device-level UI preferences | Local-only |
| `~/.cc-switch/backups/` | Auto-rotated backups (10 most recent) | Recovery |
| `~/.cc-switch/skills/` | Centralized skill storage (symlinks to apps) | Skill repo |
| `~/.cc-switch/skill-backups/` | Pre-uninstall skill backups (20 most recent) | Recovery |

**SSOT discipline:** All syncable data in SQLite; device-specific UI settings in JSON.

## 14. CHANGELOG release cadence (Pattern #83 evidence pending verification)

CHANGELOG.md at 133KB. Sustained-release-narrative density exceeds corpus norm.

**v60+ corpus comparison:**
- v66 agentmemory: CHANGELOG ~36KB
- v67 opencode-antigravity-auth: 91 releases
- v69 CloakBrowser: 28+ releases in 86 days
- v70 codegraph: 28+ releases in 121 days
- v72 DeepSeek-TUI: significant CHANGELOG (size not measured)
- **v73 cc-switch: 133KB CHANGELOG corpus-record for v60+ window**

## 15. Cross-platform binary size

Tauri 2 advantage over Electron — much smaller binary (Tauri uses system WebView; Electron bundles Chromium).

**Estimated sizes:**
- Windows MSI: ~10-15 MB
- macOS DMG: ~10-15 MB
- Linux deb: ~10-15 MB
- AppImage: ~10-15 MB
- Compared to Electron equivalents: ~100-150 MB

---

**Cross-references:**
- Pattern Library implications → `entity-3-pattern-library.md`
- User-facing details → `user-facing cluster summary.md`
- Contributor governance → `contributor-facing cluster summary.md`
- Storm Bear vendor-diversification → `entity-4-storm-bear.md`

## Corpus-distinguishing properties (v73)

| Property | cc-switch | Prior corpus-record |
|----------|-----------|---------------------|
| Packaging methods | **9** | 5 (v72 DeepSeek-TUI) |
| Provider matrix | **50+ presets** | 9 (v72 DeepSeek-TUI) |
| Agent runtimes managed | **6** | 1 primary (v72 DeepSeek-TUI for DeepSeek) |
| LDS layer count | **12+** | 6 (v72) / 5 (v71 78a) |
| Stars at age | **75K @ 289d** | 32K @ 120d (v72) |
| Velocity sustained | **259/d × 289d** | 267/d × 120d (v72) |
| CHANGELOG density | **133KB** | ~36KB (v66) |
| Sponsor density | **20+** | 0 typical |
