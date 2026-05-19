# cc-switch — Hướng dẫn cho người mới (VN/EN)

> *Cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Gemini CLI & Hermes Agent.*
>
> *Ứng dụng desktop quản lý đa runtime: Claude Code, Codex, OpenCode, OpenClaw, Gemini CLI & Hermes Agent.*

**Wiki version:** v73 (built 2026-05-19)
**Repository:** https://github.com/farion1231/cc-switch
**Homepage:** https://ccswitch.io
**Author:** farion1231 (solo developer, Chinese-speaking)
**License:** MIT
**Stars / forks:** 75,033 / 4,866

---

## Phần 1: cc-switch là gì?

**Tóm tắt (VN):** cc-switch là ứng dụng desktop cross-platform (Windows + macOS + Linux) quản lý 6 AI coding agent runtimes (Claude Code + Codex + Gemini CLI + OpenCode + OpenClaw + Hermes Agent) qua giao diện thống nhất. Thay vì sửa file JSON/TOML/`.env` thủ công khi switch provider API, bạn dùng UI để: import provider qua 50+ preset có sẵn, switch instant qua system tray, sync MCP/Skills/Prompts qua các runtime, backup config tự động.

**Summary (EN):** cc-switch is a cross-platform desktop app (Windows + macOS + Linux) managing 6 AI coding agent runtimes through unified UI. Instead of manually editing JSON/TOML/`.env` config files when switching API providers, you get: 50+ provider presets for one-click import, system-tray instant switching, unified MCP/Skills/Prompts sync across runtimes, auto-backup config protection.

**Điểm nổi bật chính:**
- **6 runtimes managed:** Claude Code + Codex + Gemini CLI + OpenCode + OpenClaw + Hermes Agent
- **50+ provider presets:** AWS Bedrock + NVIDIA NIM + 20+ Chinese API relay services (PackyCode + AIGoCode + Shengsuanyun + etc.)
- **Unified MCP & Skills management** — one panel manages MCP servers + Skills + Prompts across 4 of 6 runtimes
- **System Tray Quick Switch** — switch provider instantly without opening main UI
- **Cloud Sync** — sync configs across devices via Dropbox / OneDrive / iCloud / WebDAV
- **Tauri 2 binary** — Rust + TypeScript; small binary (~10-15 MB)
- **macOS code-signed + notarized** — direct install without "unidentified developer" warning
- **Atomic-write config protection** — temp file + rename prevents corruption
- **SQLite SSOT** — single source of truth at `~/.cc-switch/cc-switch.db`
- **Minimal-intrusion design** — uninstall leaves CLI tools functional
- **Deep Link (`ccswitch://`)** — URL-based provider/MCP/prompt/skill import
- **CJK trio i18n** — EN + Simplified Chinese + Japanese
- **Tray + auto-update + dark/light theme**

---

## Phần 2: Tín hiệu corpus-first (v73 wiki context)

**Trong corpus 73-wiki của Storm Bear, cc-switch đặt ra rất nhiều kỷ lục:**

1. **75,033 stars** — first 60-100K stars tier subject in v60+ window
2. **9 packaging channels** — corpus-record T1 subject (vượt v72 DeepSeek-TUI 5 methods)
3. **6 agent runtimes managed** — corpus-first multi-runtime aggregator
4. **50+ provider presets** — corpus-record multi-provider library (vượt v72 9-provider matrix)
5. **12-layer Living-Domain-Standards integration** — corpus-record (vượt v71 78a 5-layer + v72 6-layer)
6. **Atomic-writes-as-architectural-primitive** — corpus-first explicit formalization
7. **SSOT (Single Source of Truth) explicit formalization** — corpus-first
8. **"Minimal intrusion design principle"** — corpus-first formal discipline
9. **20+ sponsor density** — OC-Q "Sponsor-Density-As-Corpus-Signal" candidate
10. **3+ corpus subjects explicitly cited** — Pattern #57 STRONGEST corpus-recursive (vượt v65 record at 1 subject)
11. **Tauri 2 corpus subject first**
12. **Deep-Link URL protocol (`ccswitch://`) first**
13. **Dual-way sync (write live + backfill) discipline first**
14. **SQLite-as-config-source discipline first**
15. **CHANGELOG at 133KB density corpus-record for v60+ window**
16. **4-cloud-sync destinations corpus-first** (Dropbox + OneDrive + iCloud + WebDAV)
17. **Pattern #18 sub-archetype #8 candidate "multi-runtime-aggregator-desktop-app"**

**Velocity sustained:** 259.6 stars/day × 289 days = **HIGH-NOT-EXTREME sub-class N=3 + CORPUS-RECORD 289-day sustenance** (Phase 4b PRIMARY).

---

## Phần 3: Định vị tier (Pattern Library)

**Tier T1** — Multi-Runtime Aggregator (Pattern #18 sub-archetype #8 candidate).

**Khác với:**
- T1 single-runtime client (v72 DeepSeek-TUI): manage 1 primary vendor + alternatives
- T1 declarative skill (v71 agents-best-practices): markdown-only skill definition
- T2 single-purpose service (v66 agentmemory, v70 codegraph): one function
- T4 single-vendor bridge (v62 codex-plugin-cc, v67 opencode-antigravity-auth): one cross-vendor pair

**cc-switch's distinct positioning:** First multi-runtime AI agent aggregator desktop application in 73-wiki corpus.

---

## Phần 4: Cài đặt

**Cách dễ nhất (macOS):**

```bash
brew install --cask cc-switch
open -a "CC Switch"
```

**Windows:**

```text
1. Download CC-Switch-v{version}-Windows.msi từ Releases
2. Double-click cài
3. Launch từ Start menu
```

**Arch Linux:**

```bash
paru -S cc-switch-bin
cc-switch
```

**Linux Ubuntu/Debian:**

```bash
wget https://github.com/farion1231/cc-switch/releases/latest/download/CC-Switch-Linux.deb
sudo dpkg -i CC-Switch-Linux.deb
cc-switch
```

**Universal Linux (AppImage):**

```bash
wget https://github.com/farion1231/cc-switch/releases/latest/download/CC-Switch-Linux.AppImage
chmod +x CC-Switch-Linux.AppImage
./CC-Switch-Linux.AppImage
```

**Sau khi cài:**
- Lần đầu chạy: option để import config CLI tool đã có (Claude Code / Codex / etc.) làm default providers
- Add Provider qua 50+ preset có sẵn → paste API key → done

---

## Phần 5: Quy trình sử dụng cốt lõi

### Switch provider cho Claude Code

```text
1. Open cc-switch
2. Sidebar chọn Claude Code
3. Chọn provider preset (Anthropic Direct / AWS Bedrock / etc.)
4. Click "Enable"
5. Claude Code HOT-SWITCH ngay (không cần restart terminal)
```

### Quick switch qua System Tray

```text
1. Click cc-switch tray icon
2. Hover Claude Code (hoặc runtime khác)
3. Click provider name → instant switch
4. (Không cần mở main UI)
```

### Add MCP server đến tất cả 4 apps

```text
1. Open cc-switch
2. MCP button → Add Server
3. Choose template (filesystem MCP, github MCP, etc.) OR custom config
4. Toggle sync cho: Claude Code + Codex + OpenCode + Gemini CLI
5. Apply
6. MCP server xuất hiện ở all 4 apps; sync bidirectional
```

### Install skill từ GitHub đến tất cả apps

```text
1. Skills button → Browse repos
2. Add GitHub repo URL
3. Click Install
4. cc-switch download skill, symlink đến all apps
5. Skill có sẵn ở Claude Code / Codex / OpenCode / Gemini CLI ngay
```

### Cross-app prompt sync

```text
1. Prompts button → Create preset
2. Edit Markdown content
3. Click Activate
4. Prompt sync đến CLAUDE.md / AGENTS.md / GEMINI.md cho từng runtime
```

### Cloud sync giữa nhiều thiết bị

```text
1. Settings → Cloud Sync → choose Dropbox (hoặc OneDrive / iCloud / WebDAV)
2. cc-switch sync ~/.cc-switch/cc-switch.db lên cloud
3. Install cc-switch trên device 2+3 → point at same cloud folder
4. Configs sync across all devices
```

### Local proxy + failover (advanced)

```text
1. Open Proxy Settings
2. Add primary provider (Anthropic Direct)
3. Add backup provider (AWS Bedrock)
4. Enable circuit breaker
5. cc-switch route qua proxy; auto-fail to backup khi primary error
```

---

## Phần 6: Khái niệm mới / Kiến trúc quan trọng

### SSOT (Single Source of Truth) — SQLite database

cc-switch lưu tất cả config tại `~/.cc-switch/cc-switch.db`:
- Providers
- MCP servers
- Prompts
- Skills (registry; actual files in `~/.cc-switch/skills/`)

Device-level UI settings tại `~/.cc-switch/settings.json` (không sync).

### Atomic writes — corruption-resistant

```
Write flow:
1. Write content to temp file (.tmp)
2. Rename .tmp over live file (atomic operation)
3. If process crashes, .tmp still on disk, live file unchanged
```

Sister to v69 CloakBrowser 3-tier signature verification (artifact-layer); cc-switch is config-state-layer integrity.

### Dual-way sync

- **Write to live files on switch:** cc-switch writes Claude Code config when you switch
- **Backfill from live on edit:** If you edit `~/.claude/CLAUDE.md` directly while cc-switch is running, cc-switch detects + updates DB

Resolves "config drift" problem common in multi-runtime setups.

### Minimal-intrusion design principle

- cc-switch NEVER deletes your existing config
- Always keeps one active configuration (cannot delete the active provider — minimum-1-config guarantee)
- Cleanup on uninstall is opt-in
- CLI tools' configs persist independently

**Test:** Uninstall cc-switch. Run `claude code`. It works. Your Claude Code config wasn't touched.

### Layered architecture (Pattern #21 SDD evidence)

```
Frontend (React + TS)
   ├── Components (UI)
   ├── Hooks (Business Logic)
   └── TanStack Query (Cache/Sync)
   ↕ Tauri IPC
Backend (Tauri + Rust)
   ├── Commands (API Layer)
   ├── Services (Business Layer) — ProviderService / McpService / ProxyService / SessionManager / ConfigService / SpeedtestService
   └── Models/Config (Data Layer) — SQLite + JSON
```

Clear separation Commands → Services → DAO → Database. Each service single-responsibility.

### Deep-Link URL protocol (`ccswitch://`)

```
ccswitch://provider/<base64-encoded-config>
ccswitch://mcp/<url>
ccswitch://prompt/<id>
ccswitch://skill/<github-url>
```

Click URL → cc-switch opens → import dialog → confirm.

Use cases: sponsor sites pre-configure provider; community config sharing via URL; documentation deep links.

---

## Phần 7: So sánh với corpus subjects khác

| Đặc điểm | cc-switch (v73) | DeepSeek-TUI (v72) | agents-best-practices (v71) | Claude Code (substrate) |
|----------|------------------|--------------------|-----------------------------|--------------------------|
| Tier | T1 multi-runtime aggregator | T1 single-runtime client | T1 declarative skill | T1 (substrate) |
| Runtimes managed | **6 (corpus-record)** | 1 primary (DeepSeek) | Declarative | 1 |
| Provider matrix | **50+ presets** | 9 providers | Declarative | 1 |
| Packaging methods | **9 (corpus-record)** | 5 | 2 (npm + git) | 1 (npm) |
| OS support | Win + macOS + Linux + WSL | Linux + macOS + Win | All (Markdown) | All |
| Locales | EN + zh-Hans + ja (CJK trio) | EN + zh-Hans + ja + pt-BR | EN | EN |
| Binary format | Tauri 2 (Rust + TS) | Rust binary (TUI) | Markdown-only | Node.js wrapper |
| Code-signing | macOS notarized | Not documented | N/A | Signed |
| Cloud sync | **Dropbox + OneDrive + iCloud + WebDAV (4 destinations)** | None | N/A | None |
| Cost | $0 (MIT binary) | $0 (MIT) | $0 (MIT) | Per Anthropic |
| Velocity sustained | 259/d × 289d (CORPUS-RECORD sub-class sustenance) | 267/d × 120d | n/a (4d age) | n/a |

---

## Phần 8: Ethical framing — Honest disclosures (Pattern #83)

**README emphasizes:**
- *"Only official website: ccswitch.io"* — explicit warning về look-alike/fork-confusion
- *"minimal intrusion design principle — even if you uninstall the app, your CLI tools will continue to work normally"* — honest về tool's own footprint
- Sponsor recommendations — 20+ commercial relationships disclosed openly
- Code-signing + notarization on macOS — explicit trust-layer
- *"Atomic Writes: Temp file + rename pattern prevents config corruption"* — explicit failure-mode awareness

**Cảnh báo dùng cẩn thận:**
- 20+ sponsor presets are commercial relationships — verify pricing/quality độc lập
- Provider switching has session-state implications for some runtimes (Codex requires terminal restart)
- Cloud sync exposes config (including possibly API keys) — verify cloud destination security
- macOS code-signing trust extends to all functionality — vetted by Apple notarization but not by independent auditor

---

## Phần 9: Storm Bear relevance — HIGHEST-RELEVANCE vault pilot candidate

**Verdict: STRONGEST INCLUDE (3-4/4 STRICT PASS Storm Bear meta-entity criteria) — first STRONGEST since v65 claude-code-system-prompts.**

| Criterion | Status |
|-----------|--------|
| (a) Author archetype peer | PROBABLE PASS (Chinese-speaking solo dev; structural peer to Storm Bear VN-aligned) |
| (b) Operational tool for vault | **STRONGEST PASS** — manages Claude Code (Storm Bear's primary substrate) + 5 alternatives + 50+ providers; addresses documented "Tool lock-in moderate — heavy investment in Claude Code + Anthropic stack" risk |
| (c) Methodology influence | PASS — multi-runtime provider-management + SSOT-with-atomic-writes + dual-way sync + minimal-intrusion inform routine v2.3 design |
| (d) In-corpus reference | **STRONGEST PASS** — explicitly names 3 corpus subjects (Claude Code v65 + Codex v62 + OpenCode v67); CORPUS-RECORD corpus-recursive citation depth |

**Pilot ranking UPDATED:** cc-switch becomes **vault pilot #1** (replaces codegraph as previous #1). Recommended pilot sequence:

1. **cc-switch (FIRST — highest relevance + lowest infrastructure overhead + immediate vendor-diversification awareness)**
2. codegraph (SECOND — read-only indexing)
3. agents-best-practices skill (THIRD — zero infrastructure)
4. agentmemory (FOURTH — service deployment)
5. DeepSeek-TUI (FIFTH — full alternative coding agent)

---

## Phần 10: 4-week learning roadmap

**Week 1 — Cài đặt + first session:**
- Cài qua Homebrew (macOS) hoặc MSI (Windows) hoặc paru/deb/rpm (Linux)
- Add Anthropic Direct provider preset (current Claude Code config)
- Test hot-switch giữa providers
- Setup system tray quick-switch
- Try 3 chế độ approval (suggest/auto/never)

**Week 2 — Multi-runtime exploration:**
- Add Codex preset, test provider management
- Add Gemini CLI preset (cần Google API key)
- Try Universal Provider feature cho OpenCode + OpenClaw
- Test format conversion qua local proxy
- Bookmark sponsor preset comparison (giá cả + chất lượng)

**Week 3 — Advanced features:**
- MCP server unified management (add 2-3 common MCP servers)
- Skills system (install 1-2 skills từ GitHub)
- Prompts cross-app sync (CLAUDE.md ↔ AGENTS.md ↔ GEMINI.md)
- Session Manager (browse history across apps)
- Workspace editor cho OpenClaw

**Week 4 — Production discipline:**
- Cloud sync setup (Dropbox or iCloud)
- Local proxy + failover configuration
- Usage Dashboard + cost tracking
- Provider health monitoring
- Backup-restore workflow validation
- Decision: integrate as production tool / pilot end

---

## Phần 11: Tradeoffs + limitations

**Lợi thế:**
- Manage 6 runtimes through unified UI (corpus-first capability)
- 50+ provider presets — easiest provider switching trong corpus
- Atomic-writes + SSOT — corruption-resistant config layer
- Minimal-intrusion — safely reversible
- macOS code-signed + notarized — Apple-trust layer
- Cloud sync across 4 destinations
- Tauri 2 binary size advantage over Electron
- Active development (133KB CHANGELOG)
- 20+ sponsor presets cho cost-saving options
- CJK trio i18n

**Hạn chế:**
- Desktop GUI only (no headless / server mode)
- Hot-switch only for Claude Code (other 5 runtimes require terminal restart)
- 20+ sponsor presets create "marketing surface" trong README (sponsor section dominates first 140 lines)
- Single-maintainer trust boundary (farion1231) — bus-factor concern at 75K-star scale
- Cloud sync exposes config including possibly API keys — security verification needed
- Codex + Gemini CLI authentication flow may differ from documented preset (verify per-vendor)
- Provider preset quality varies (Chinese relay services may have geographic restrictions)

**Khi nên dùng:**
- Bạn dùng 2+ AI coding agent runtimes
- Bạn switch providers thường xuyên (vendor-diversification workflow)
- Bạn cần MCP/Skills/Prompts unified management
- Bạn ở mainland China (20+ Chinese API relay presets)
- Bạn cần cost-optimization qua provider preset comparison

**Khi không nên dùng:**
- Bạn chỉ dùng 1 AI agent runtime (overkill)
- Bạn không switch providers (cc-switch value is switching)
- Bạn cần IDE plugin (cc-switch là desktop app)
- Bạn cần headless deployment (cc-switch là GUI)

---

## Phần 12: Caveats + safety notes

**Supply-chain awareness (Pattern #66):**
- Verify download source: chỉ ccswitch.io hoặc github.com/farion1231/cc-switch official
- macOS DMG: code-signed + notarized by Apple — direct install safe
- Windows MSI: signed (verify in installer properties)
- Linux deb/rpm: no native signing; verify GitHub Releases checksum if available
- AppImage: no signing; download from official GitHub Releases only
- Arch AUR: `cc-switch-bin` is maintained by community — verify maintainer before install

**Sponsor recommendations awareness:**
- 20+ sponsors are commercial API relay services with affiliate codes
- Pricing claims (e.g., "Claude Code at 38% of original price") may vary
- Each sponsor has separate ToS + security model — review independently
- "Verify line by line" sponsor billing claims pre-commit
- Sponsor relationships do NOT imply farion1231 endorses these companies for production use

**API key security:**
- API keys saved to `~/.cc-switch/cc-switch.db` (SQLite)
- Cloud sync exposes DB to chosen destination — encrypt cloud folder if security-sensitive
- Use Custom Config Panel "Shared Config Snippet" feature carefully (may contain secrets across providers)
- Rotate API keys periodically

**Multi-runtime config integrity:**
- cc-switch atomic-writes prevent corruption — BUT external editors can still corrupt
- Backfill detects external edits but may surface conflicts
- Auto-backup (10 most recent) recovers from accidents

---

## Phần 13: References + Next Action

### Tài liệu chính

- **Repository:** https://github.com/farion1231/cc-switch
- **Homepage:** https://ccswitch.io
- **Releases:** https://github.com/farion1231/cc-switch/releases
- **User Manual:** docs/user-manual/en/README.md
- **CHANGELOG:** CHANGELOG.md (133 KB)
- **Trendshift listing:** https://trendshift.io/repositories/15372
- **README (zh):** README_ZH.md
- **README (ja):** README_JA.md

### Storm Bear vault cross-references

- **CLAUDE.md** (vault root) — Storm Bear meta-entity + Pattern Library state
- **v72 audit document:** `04 Reviews/(C) 2026-05-19 ... PROMOTION-DRIVEN + 5TH-CONSECUTIVE-TRIGGER ...md`
- **v73 wiki entities:**
  - `02 Wiki/(C) entity-1-provider-management-aggregator.md` (modes/tools)
  - `02 Wiki/(C) entity-3-pattern-library.md` (Pattern Library impacts)
  - `02 Wiki/(C) entity-4-storm-bear.md` (vault pilot ranking)
- **Phase 4b PRIMARY:** `01 Analysis/(C) Pattern-52-HIGH-NOT-EXTREME-sub-class-N3-corpus-record-sustenance-evaluation.md`
- **Sister wikis:** v72 DeepSeek-TUI + v71 agents-best-practices + v70 codegraph + v69 CloakBrowser + v67 opencode + v66 agentmemory + v65 claude-code-system-prompts + v62 codex-plugin-cc + v61 cc-sdd

### Sibling tools trong vault corpus (managed by cc-switch)

- **Claude Code (v65 corpus reference)** — primary substrate Storm Bear uses
- **Codex (v62 corpus reference)** — secondary alternative
- **OpenCode (v67 corpus reference)** — community alternative
- **DeepSeek-TUI (v72)** — distinct tool; vendor-diversification alternative

### Next action

**For Storm Bear (vault operator):**

1. **HIGHEST PRIORITY: Pilot cc-switch as vault pilot #1** — replaces codegraph as pilot #1
2. Install on macOS: `brew install --cask cc-switch`
3. Add 3-5 provider presets (Anthropic + AWS Bedrock + 2-3 Chinese relays for cost-comparison)
4. Use 1-2 weeks; document findings in `_state/pilot-ranking-2026-05-07.md` update
5. **Verify Pattern Library v73 contributions at next vault sync:**
   - Pattern #52 HIGH-NOT-EXTREME sub-class N=3 + CORPUS-RECORD sustenance ✓
   - Pattern #84 84c THIRD strengthening ✓
   - Pattern #57 STRONGEST corpus-recursive citation ✓
   - Pattern #28 CORPUS-RECORD 50+ presets ✓
   - Pattern #66 66f atomic-writes + SSOT + minimal-intrusion candidate ✓
   - Pattern #78 12-layer LDS CORPUS-RECORD ✓
   - Pattern #18 sub-archetype #8 candidate ✓
   - OC-Q "Sponsor-Density-As-Corpus-Signal" candidate ✓

6. **v75 audit prep:** Pattern #52 PROMOTION LOCKED-IN — schedule at v75 audit; OC-P + OC-Q + 18#8 + 66f + 21-sub-variant first-cycle stale-checks; 84c sub-typology split decision.

**For end-user (not Storm Bear):**

1. Install cc-switch via package manager appropriate for your OS
2. Add Anthropic Direct preset (or your current provider)
3. Add 1-2 alternative providers for cost-experimentation
4. Try MCP unified management
5. Read CHANGELOG for feature evolution
6. Verify sponsor recommendations independently before commercial commitment

---

**Wiki end. Built by Storm Bear vault v73 LLM Wiki Routine v2.2 — 2026-05-19.**

**Independent value-add of this guide:** Vault-pilot ranking update (cc-switch becomes #1) + Pattern Library context (Pattern #52 v75 promotion locked-in) + corpus comparison vs DeepSeek-TUI + agents-best-practices.
