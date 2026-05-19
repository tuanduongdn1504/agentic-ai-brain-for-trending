# Entity 2 — Distribution + Multi-Runtime Ecosystem

## 1. One-liner (VI/EN)

**EN:** cc-switch's distribution + multi-runtime architecture — 9 packaging methods (corpus-record), 6 agent runtime targets, 50+ provider preset library, CJK trio i18n, code-signed + notarized macOS, atomic-write config-protection at runtime layer.

**VI:** Kiến trúc phân phối + đa runtime của cc-switch — 9 phương thức đóng gói (kỷ lục corpus), 6 agent runtime targets, thư viện 50+ provider preset, i18n CJK trio, macOS code-signed + notarized, bảo vệ config atomic-write.

## 2. When to use this entity

Use this reference when:
- Choosing install method for cc-switch (npm vs Homebrew vs cargo vs Docker vs direct)
- Comparing cc-switch distribution architecture to other corpus subjects
- Evaluating cc-switch's 6-runtime + 50+ provider matrix scope
- Designing cross-platform installer strategy for own desktop app
- Assessing macOS code-signing + notarization for solo-developer projects

## 3. Distribution dimension vs sibling subjects

| Dimension | cc-switch (v73) | v72 DeepSeek-TUI | v71 agents-best-practices | Claude Code (substrate) |
|-----------|------------------|--------------------|----------------------------|--------------------------|
| Packaging methods | **9** | 5 | 2 (npm + git) | 1 (npm) |
| Agent runtimes managed | **6** | 1 (DeepSeek primary) | Declarative skill | 1 |
| Provider matrix | **50+ presets** | 9 providers | Declarative | 1 |
| OS targets | Win + macOS + Linux + WSL | Linux + macOS + Win | All (Markdown) | All |
| Locales | EN + zh-Hans + ja (CJK trio) | EN + zh-Hans + ja + pt-BR | EN | EN |
| Binary format | Tauri 2 (Rust + TS) | Rust binary (TUI) | Markdown-only | Node.js wrapper |
| Code-signing | macOS notarized | Not documented | N/A | Signed |
| Cloud-sync | Dropbox + OneDrive + iCloud + WebDAV | None | N/A | None |

**cc-switch's distinct positioning:** Highest distribution breadth in v60+ corpus window — 9 packaging methods + 5 OS-specific installer formats + 4 cloud-sync destinations.

## 4. Sub-types

**By packaging method:**

- **Wrapper:** Homebrew cask (downloads release binary) / Arch paru (downloads from AUR)
- **Native installer:** Windows MSI / macOS DMG (notarized) / Linux deb / Linux rpm
- **Portable:** Windows Portable ZIP / macOS ZIP
- **Universal:** Linux AppImage
- **User-build:** Flatpak (instructions in `flatpak/README.md`)

**By installation route:**

- **macOS:** `brew install --cask cc-switch` (recommended) OR DMG download
- **Arch Linux:** `paru -S cc-switch-bin` (recommended) OR direct download
- **Windows:** MSI installer (recommended) OR portable ZIP
- **Debian/Ubuntu:** `.deb` package
- **Fedora/RHEL/openSUSE:** `.rpm` package
- **Universal Linux:** AppImage

**By update mechanism:**

- Homebrew: `brew upgrade --cask cc-switch`
- AUR: `paru -Syu`
- In-app auto-updater (built-in via Tauri)
- Manual download from Releases

## 5. Anatomy

**Binary layout:**

```
cc-switch (single binary, ~10-15 MB)
├── Tauri runtime (system WebView + Rust runtime)
├── React + TS frontend (bundled JS/CSS)
└── Tauri Commands (Rust backend)
```

**Per-platform installer:**

| OS | Format | Size estimate | Signed |
|----|--------|---------------|--------|
| Windows | MSI | ~15 MB | Yes (likely) |
| Windows | Portable ZIP | ~12 MB | Yes |
| macOS | DMG (Universal) | ~25 MB (x86 + ARM) | Yes (notarized) |
| macOS | ZIP | ~25 MB | Yes |
| Linux | deb | ~12 MB | N/A |
| Linux | rpm | ~12 MB | N/A |
| Linux | AppImage | ~30 MB (bundled) | N/A |

## 6. Mechanism / How distribution works

**Homebrew install flow:**

```
brew install --cask cc-switch
   ↓
1. Homebrew downloads cask manifest
2. Verifies SHA-256 against manifest
3. Downloads CC-Switch-{version}-macOS.dmg
4. Mounts DMG, copies .app to /Applications/
5. Removes quarantine flag (Apple notarization recognized)
```

**Tauri auto-update flow:**

```
1. App startup → checks Tauri updater
2. If new version available → notifies user
3. User accepts → downloads + applies update
4. App restarts with new version
```

**Cross-platform build (developer):**

```
pnpm tauri build
   ↓
Generates per-platform installer:
  ├── target/release/bundle/msi/    (Windows)
  ├── target/release/bundle/dmg/    (macOS)
  ├── target/release/bundle/deb/    (Linux Debian)
  ├── target/release/bundle/rpm/    (Linux Fedora)
  └── target/release/bundle/appimage/  (Linux universal)
```

## 7. Out-of-box list

**Distribution channels (10 total):**

| Channel | Type | Install |
|---------|------|---------|
| Homebrew Cask | Package manager | `brew install --cask cc-switch` |
| Arch AUR | Package manager | `paru -S cc-switch-bin` |
| Windows MSI | Native installer | Download from Releases |
| Windows Portable | ZIP archive | Download from Releases |
| macOS DMG | Disk image (notarized) | Download from Releases |
| macOS ZIP | Archive | Download from Releases |
| Linux deb | Debian package | Download from Releases |
| Linux rpm | RPM package | Download from Releases |
| Linux AppImage | Universal | Download from Releases |
| Flatpak (user) | Build instructions | `flatpak/README.md` |

**Runtimes managed (6):**

| # | Runtime | Vendor | cc-switch role |
|---|---------|--------|-----------------|
| 1 | Claude Code | Anthropic | Hot-switching + MCP/Skills/Prompts sync |
| 2 | Codex | OpenAI | Provider management |
| 3 | Gemini CLI | Google | Provider management |
| 4 | OpenCode | Community | Provider management |
| 5 | OpenClaw | Community | Provider management + Workspace editor |
| 6 | Hermes Agent | Community | Provider management |

**Cloud sync destinations (4):** Dropbox + OneDrive + iCloud + WebDAV.

## 8. Configuration (distribution-level)

**Code-signing (macOS):**
- Apple Developer ID required (cc-switch has it)
- Notarization process (`xcrun notarytool`)
- Result: macOS Gatekeeper allows direct launch (no "unidentified developer" warning)

**Auto-updater:**
- Tauri 2 built-in updater
- Checks update endpoint on app startup
- Atomic update with rollback support (Tauri convention)

**Cloud sync configuration:**
- Settings → Cloud Sync → choose destination
- cc-switch maintains custom config directory at chosen path
- All syncable data (SQLite + JSON) synced as opaque blobs

## 9. Recipes

### Minimal — macOS install

```bash
brew install --cask cc-switch
open -a "CC Switch"
```

### Common — Windows install via MSI

```text
1. Download CC-Switch-v{version}-Windows.msi from Releases
2. Double-click to launch installer
3. Follow prompts (admin elevation required)
4. Launch from Start menu
```

### Common — Arch Linux

```bash
paru -S cc-switch-bin
cc-switch  # launches GUI
```

### Common — Linux Ubuntu/Debian

```bash
wget https://github.com/farion1231/cc-switch/releases/latest/download/CC-Switch-Linux.deb
sudo dpkg -i CC-Switch-Linux.deb
cc-switch
```

### Advanced — Universal Linux via AppImage

```bash
wget https://github.com/farion1231/cc-switch/releases/latest/download/CC-Switch-Linux.AppImage
chmod +x CC-Switch-Linux.AppImage
./CC-Switch-Linux.AppImage
```

### Advanced — Flatpak (user-build)

```text
See flatpak/README.md for build instructions.
Build from .deb package using flatpak-builder.
Not included in official releases (community-build only).
```

### Advanced — Cloud sync across 3 devices

```text
1. Install cc-switch on device 1 (macOS)
2. Settings → Cloud Sync → iCloud Drive
3. cc-switch saves config to iCloud
4. Install cc-switch on device 2 (Windows) + device 3 (Linux)
5. Settings → Cloud Sync → point at same iCloud path (via 3rd-party iCloud sync on Windows/Linux)
6. Configs sync across all 3 devices
```

## 10. Advanced patterns

- **WSL support** (per repo topics): cc-switch on Windows manages Claude Code installed in WSL
- **Universal Provider** feature: one config syncs to multiple apps (OpenCode + OpenClaw share format)
- **Per-app sponsor preset**: Sponsor-recommended providers pre-configured for specific runtimes
- **Tauri 2 system tray integration**: Native tray menu on Windows + macOS + Linux
- **Format conversion at proxy layer**: Translate between provider APIs without changing client config
- **Single-binary distribution + per-platform installer**: Tauri 2 enables this combo (small binary + native UX)

## 11. Combination patterns

| Combination | Use case |
|-------------|----------|
| Homebrew + iCloud Sync | macOS power-user with multi-device workflow |
| Arch paru + WebDAV | Self-hosted Linux user with NAS-based config sync |
| Windows MSI + WSL Claude Code | Windows dev managing WSL-installed Claude Code |
| AppImage + portable workflow | Linux user without root privileges |
| DMG + Tauri auto-updater | macOS user wanting in-app update flow |

## 12. Anti-patterns / common mistakes

- **Installing both Homebrew cask AND direct DMG download** — Conflict; choose one path
- **Skipping macOS notarization check** — cc-switch IS notarized; direct DMG download is safe (no "unidentified developer" override needed)
- **Manual binary download without SHA-256 verification** — README warning about look-alike repositories (only official site is ccswitch.io)
- **Using Scoop on Windows** — Not officially supported (use MSI or portable ZIP); Scoop manifest is community-maintained, may lag
- **Trusting unofficial websites** — README emphatic: *"Only official website: ccswitch.io"*

## 13. Related tools + cross-references + citations

### Vault cross-references

- **v72 DeepSeek-TUI** — 5 packaging methods sister (cc-switch v73 = 9 methods = corpus-record exceeds)
- **v66 agentmemory** — 3 packaging methods sister
- **v70 codegraph** — npm + docker only
- **v71 agents-best-practices** — npm + git only

### Pattern Library tags

- Pattern #28 50+ provider preset corpus-record
- Pattern #66 macOS code-signing + notarization + atomic-writes
- Pattern #78 12-layer LDS (DeepSeek + Anthropic + OpenAI + Google + community runtimes + Tauri + Rust + SQLite + WebDAV + cloud-sync APIs)
- Pattern #84 84c third-strengthening (6-runtime multi-vendor matrix)
- 9-packaging-method corpus-record
- 4-cloud-sync-destination corpus-first

### External references

- Releases: https://github.com/farion1231/cc-switch/releases
- Tauri 2 docs: https://v2.tauri.app/
- Homebrew cask: `homebrew/cask` includes `cc-switch`
- AUR: `cc-switch-bin`
- Trendshift: https://trendshift.io/repositories/15372
