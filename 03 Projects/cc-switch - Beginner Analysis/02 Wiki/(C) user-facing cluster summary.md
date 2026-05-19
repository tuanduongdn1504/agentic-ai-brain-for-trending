# cc-switch User-Facing Cluster Summary

**Scope:** README + Quickstart + FAQ + user-manual + 6-runtime feature surface
**Audience:** End-user / developer trying cc-switch for first time

---

## 1. What it is

**Verbatim (README line 5):** *"The All-in-One Manager for Claude Code, Codex, Gemini CLI, OpenCode, OpenClaw & Hermes Agent"*

**Synthesis:** Cross-platform desktop application (Windows/macOS/Linux) that manages 6 AI coding agent runtimes through unified UI. Eliminates manual JSON/TOML/`.env` editing for provider configuration; provides one-click provider switching with system-tray quick-access.

## 2. First 90 seconds (Quickstart)

```bash
# macOS (recommended)
brew install --cask cc-switch

# Arch Linux
paru -S cc-switch-bin

# Windows / Linux — download from https://github.com/farion1231/cc-switch/releases
```

Launch:
1. App opens to main UI
2. First-launch dialog: option to import existing CLI tool configs as default providers
3. Click "Add Provider" → choose preset (50+ available) → paste API key → done
4. Switch via system tray menu (instant) OR main UI (restart CLI tool except Claude Code which hot-switches)

## 3. Six runtimes managed

| Runtime | Hot-switch | Notes |
|---------|------------|-------|
| **Claude Code** | ✅ Yes | Anthropic official agent; cc-switch hot-switches without terminal restart |
| **Codex** | ❌ No | OpenAI official agent; requires terminal restart after switch |
| **Gemini CLI** | ❌ No | Google official agent |
| **OpenCode** | ❌ No | Community runtime |
| **OpenClaw** | ❌ No | Community fork/variant |
| **Hermes Agent** | ❌ No | Community runtime |

## 4. Provider management (50+ presets, Pattern #28 corpus-record)

**Built-in preset categories:**
- Anthropic official + AWS Bedrock + AWS Bedrock-via-relay
- Codex official + Codex relay services
- Gemini official + Gemini relay services
- NVIDIA NIM
- 20+ Chinese API relay services (PackyCode + AIGoCode + Shengsuanyun + AICodeMirror + PatewayAI + BytePlus + SiliconFlow + Cubence + DMXAPI + Compshare + AICoding + Crazyrouter + RightCode + SSSAiCode + Micu + LemonData + CTok + ClaudeAPI + ClaudeCN + RunAPI + Pateway + others)
- Custom provider for any OpenAI-compatible endpoint

**Operations:**
- One-click switching
- Drag-and-drop sorting
- Import/export
- System tray quick switch (instant — no app open needed)
- Provider health monitoring (via Proxy & Failover service)

## 5. MCP unified management

**Single panel manages MCP servers across 4 of 6 apps:**
- Add via template OR custom config
- Bidirectional sync (write to all 4 apps; backfill from changes detected in any one)
- Deep-link import: `ccswitch://mcp/...` URLs
- Toggle per-app sync (enable/disable per runtime)

## 6. Skills system

**Unified Skills management across 4 apps:**
- One-click install from GitHub repos OR ZIP files
- Custom repository management
- Symlink-based install (default) OR file-copy install (per-user)
- Auto-backup before uninstall (20 most recent)
- Skills stored centrally at `~/.cc-switch/skills/` with symlinks to each app's expected location

## 7. Prompts system

**Cross-app prompt sync (CLAUDE.md / AGENTS.md / GEMINI.md unified editor):**
- Markdown editor with preview
- Activate to sync to live files in each app
- Backfill protection (detects external edits, prompts to reconcile)

## 8. Session Manager

- Browse, search, restore conversation history across all 6 apps
- Workspace editor (OpenClaw) for AGENTS.md / SOUL.md etc.

## 9. Proxy & Failover

- Local proxy with hot-switching
- Format conversion (translate between provider APIs)
- Auto-failover (when primary provider fails, switch to backup)
- Circuit breaker (rate-limit-aware backoff)
- Provider health monitoring (dashboard)
- Request rectifier (fix common request-format errors)
- App-level takeover (independently proxy specific apps)

## 10. Usage & Cost dashboard

- Track spending / requests / tokens
- Trend charts
- Detailed request logs
- Custom per-model pricing (configurable)

## 11. Cloud sync

Sync provider data across devices via:
- Dropbox
- OneDrive
- iCloud (macOS)
- WebDAV server (custom)

## 12. System tray (instant switching)

Click provider name in tray menu → switches active provider for selected runtime without opening main UI.

## 13. Atomic-writes config-protection (Pattern #66 sub-mechanism candidate)

**Architectural primitive (verbatim from README):** *"Atomic Writes: Temp file + rename pattern prevents config corruption"*

Plus:
- SQLite SSOT (Single Source of Truth) at `~/.cc-switch/cc-switch.db`
- Auto-backup rotation (10 most recent)
- Minimal-intrusion design: uninstall leaves CLI tools functional

## 14. Localization

CJK trio: EN + zh-Hans + ja with full README + UI translation. CHANGELOG also localized.

## 15. Installation methods (Pattern packaging corpus-record)

| Method | Channel |
|--------|---------|
| Homebrew | `brew install --cask cc-switch` |
| Arch Linux | `paru -S cc-switch-bin` |
| Windows MSI | GitHub Releases |
| Windows Portable | GitHub Releases ZIP |
| macOS DMG | GitHub Releases (code-signed + notarized) |
| macOS ZIP | GitHub Releases |
| Linux deb | GitHub Releases (Debian/Ubuntu) |
| Linux rpm | GitHub Releases (Fedora/RHEL/openSUSE) |
| Linux AppImage | GitHub Releases (universal) |
| Flatpak (user-build) | `flatpak/README.md` (community-built) |

**9 packaging channels — corpus-record T1 subject.**

---

**Cross-reference:** Pattern Library implications → `entity-3-pattern-library.md`. Architecture details → `entity-2-distribution-multi-runtime.md`. Storm Bear vault relevance → `entity-4-storm-bear.md`.
