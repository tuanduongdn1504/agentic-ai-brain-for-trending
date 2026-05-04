# (C) Distribution Model

> **Source:** `00 Sources/superpowers/.claude-plugin/`, `.codex/`, `.cursor-plugin/`, `.opencode/`, `.gemini/`, `gemini-extension.json`, `package.json`, `docs/README.codex.md`, `docs/README.opencode.md`
> **Ingested:** 2026-04-18
> **Type:** Entity page (concept) — building block #4

---

## One-liner

**VI:** Distribution Model của Superpowers là **single repo, multi-harness shipping pattern** — 1 codebase root duy nhất phục vụ 7 harness khác nhau (Claude Code, Codex CLI, Codex App, Cursor, OpenCode, Copilot CLI, Gemini CLI) thông qua **per-harness manifest folders** (`.claude-plugin/`, `.codex/`, `.cursor-plugin/`, `.opencode/`, `.gemini/`) và **2 distribution channels** (Claude marketplace + git URL).

**EN:** The Distribution Model is a **single-repo, multi-harness shipping pattern** — one codebase root serves 7 different harnesses through per-harness manifest folders, plus 2 distribution channels (Claude marketplace + git URL).

---

## Khi nào dùng concept này

**Hữu ích khi:**
- Hiểu vì sao Superpowers cài đặt khác nhau giữa Claude Code (`/plugin marketplace add`) vs Codex (clone + symlink) vs OpenCode (plugin array trong JSON)
- Designing tool của riêng bạn muốn ship multi-harness — xem Superpowers làm template
- So sánh distribution với ECC (manual install + plugin) để hiểu trade-off
- Muốn upgrade từ harness này sang harness khác mà không mất skills

**Không cần để dùng cơ bản** — chỉ cần follow `INSTALL.md` của harness mình đang dùng.

---

## Comparison sibling: Distribution Model vs Plugin Manifest

| Khía cạnh | Distribution Model (concept) | Plugin Manifest (file) |
|-----------|------------------------------|------------------------|
| Phạm vi | Toàn bộ chiến lược ship code | 1 file JSON khai báo metadata |
| Số lượng | 1 model duy nhất | 5 manifests (1 cho mỗi harness) |
| Câu hỏi trả lời | "Làm sao 1 repo serve 7 harness?" | "Harness X cần biết gì về plugin?" |
| Tương tự ECC | Distribution = manual install + chia branch | Manifest = `plugin.json` từng harness |

→ Distribution Model là chiến lược; Plugin Manifest là implementation.

---

## Sub-types của distribution channels

**Channel 1: Claude Code Marketplace** (primary)
```
/plugin marketplace add obra/superpowers
/plugin install superpowers@superpowers-dev
```
- Native UX của Claude Code
- Auto-update qua marketplace refresh
- Đọc từ `.claude-plugin/marketplace.json`

**Channel 2: Git URL** (cross-harness)
```bash
# OpenCode
"plugin": ["superpowers@git+https://github.com/obra/superpowers.git"]

# Codex / Cursor / Copilot CLI / Gemini CLI
git clone https://github.com/obra/superpowers.git ~/.<harness>/superpowers
```
- Direct git clone, không qua marketplace
- Pin version qua git tag (`#v5.0.3`)
- Mỗi harness có installation method riêng

---

## Anatomy: 1 repo phục vụ 7 harness

### Folder cấu trúc

```
superpowers/
├── .claude-plugin/              ← Claude Code (Channel 1)
│   ├── plugin.json              ← {"name", "version", "author"}
│   └── marketplace.json         ← {"name": "superpowers-dev", "plugins": [...]}
├── .codex/                      ← Codex CLI
│   ├── INSTALL.md               ← Clone + symlink instructions
│   └── plugins/                 ← Codex-specific plugin scripts
├── .cursor-plugin/              ← Cursor
│   └── plugin.json              ← Trỏ skills/agents/commands/hooks vào root
├── .opencode/                   ← OpenCode
│   ├── INSTALL.md
│   └── plugins/superpowers.js   ← Entry point (per package.json "main")
├── .gemini/                     ← Gemini CLI
│   └── (gemini-specific config)
├── gemini-extension.json        ← {"contextFileName": "GEMINI.md"}
├── skills/                      ← Shared by ALL harnesses (14 skills)
├── agents/                      ← Shared (1 agent: code-reviewer)
├── commands/                    ← Deprecated stubs
├── hooks/
│   ├── hooks.json               ← Default (Claude Code)
│   ├── hooks-cursor.json        ← Cursor variant
│   ├── session-start            ← Cross-platform script
│   └── run-hook.cmd             ← Windows wrapper
├── docs/
│   ├── README.codex.md          ← Codex-specific docs
│   ├── README.opencode.md       ← OpenCode-specific docs
│   └── windows/                 ← Windows compatibility notes
├── CLAUDE.md ← shared context file
├── AGENTS.md → CLAUDE.md (symlink) ← Codex/OpenCode pickup
├── GEMINI.md ← Gemini pickup
├── package.json                 ← {"main": ".opencode/plugins/superpowers.js"}
└── README.md
```

### Nguyên tắc Anatomy

1. **Skills/agents/commands SHARED** — 1 source of truth ở root (`skills/`, `agents/`, `commands/`), mỗi harness manifest chỉ point vào.
2. **Manifests PER-HARNESS** — mỗi harness có folder riêng (`.{harness}/` hoặc dot file) để khỏi conflict format.
3. **Hooks DUPLICATE khi cần** — `hooks.json` (Claude) vs `hooks-cursor.json` (Cursor) vì 2 harness expect schema khác.
4. **Context files via SYMLINK** — `AGENTS.md → CLAUDE.md` để Codex/OpenCode đọc cùng nội dung mà không duplicate.
5. **Entry point tuỳ harness** — `package.json "main"` trỏ vào OpenCode plugin script (chỉ OpenCode cần JS entry).

---

## Cơ chế: Per-harness installation flow

### Claude Code (preferred)

```bash
/plugin marketplace add obra/superpowers
/plugin install superpowers@superpowers-dev
```

**What happens:**
1. Claude Code đọc `.claude-plugin/marketplace.json`
2. Tìm plugin `superpowers` trong array `plugins`
3. Auto-load `skills/`, `agents/`, `commands/`, `hooks/hooks.json`
4. Skills auto-trigger qua description matching (xem [[(C) Skills Library]])

**Update:** `/plugin marketplace refresh` → re-pull repo.

### Codex CLI

```bash
git clone https://github.com/obra/superpowers.git ~/.codex/superpowers
mkdir -p ~/.agents/skills
ln -s ~/.codex/superpowers/skills ~/.agents/skills/superpowers
# Restart Codex
```

**Mechanism:** Codex auto-discovers skills trong `~/.agents/skills/`. Symlink khiến Codex thấy Superpowers như native skill collection.

**Update:** `cd ~/.codex/superpowers && git pull` — symlink instant.

### Cursor

Cursor đọc `.cursor-plugin/plugin.json`:

```json
{
  "skills": "./skills/",
  "agents": "./agents/",
  "commands": "./commands/",
  "hooks": "./hooks/hooks-cursor.json"
}
```

→ Cursor mount tất cả paths vào agent context.

### OpenCode

```json
// opencode.json
{
  "plugin": ["superpowers@git+https://github.com/obra/superpowers.git"]
}
```

**Mechanism:**
1. OpenCode pull git repo vào local cache
2. Đọc `package.json "main"` → load `.opencode/plugins/superpowers.js`
3. JS plugin register skills qua OpenCode native `skill` tool

**Pin version:**
```json
"plugin": ["superpowers@git+https://github.com/obra/superpowers.git#v5.0.3"]
```

### Gemini CLI

`gemini-extension.json` declares:
```json
{
  "name": "superpowers",
  "contextFileName": "GEMINI.md"
}
```

→ Gemini CLI extension reads `GEMINI.md` (root) which points to skills.

### Copilot CLI (v5.0.7 newest)

Cài đặt tương tự Codex pattern (clone + symlink). Detail trong RELEASE-NOTES.md v5.0.7.

---

## Out-of-box behavior

**Khi cài thành công 1 harness, ngay lập tức có:**
- 14 skills auto-discoverable qua description matching
- 1 agent (`code-reviewer`) callable qua review skill
- Cross-harness shared `CLAUDE.md` (rules + philosophy)
- Hooks gắn vào session lifecycle (Claude Code/Cursor only)
- Brainstorm WebSocket server (Claude Code/Codex only — local-only port)

**KHÔNG có:**
- API key hoặc telemetry
- External dependencies (zero-dependency design — xem [[(C) Release Notes overview]] Theme 3)
- Project-specific configuration

---

## Configuration knobs

| Knob | Type | Default | Khi cần đổi |
|------|------|---------|-------------|
| `plugin install <name>@<marketplace>` | Claude Code command | n/a | Cài/uninstall |
| `git tag pin` | OpenCode plugin URL | latest | Reproducibility/rollback |
| `~/.agents/skills/<name>` symlink | Codex/Copilot CLI | n/a | Multi-skill-collection setup |
| `hooks-cursor.json` vs `hooks.json` | File switch | auto | Custom hook variants |
| `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` | Context files | shared via symlink | Per-harness override (rare) |

→ **Minimal knobs by design.** Superpowers ship opinionated config; user customization qua own plugin overlays.

---

## Recipes (use cases)

### Recipe 1: Beginner trên Claude Code (recommended path)

```
/plugin marketplace add obra/superpowers
/plugin install superpowers@superpowers-dev
# Restart Claude Code
# Try: "brainstorm a feature for X"
```

Skill `brainstorming` auto-triggers — verify install thành công.

### Recipe 2: Test trên 2 harness song song

Clone 1 lần, mount vào nhiều harness:
```bash
git clone https://github.com/obra/superpowers.git ~/superpowers-shared

# Codex
ln -s ~/superpowers-shared/skills ~/.agents/skills/superpowers

# OpenCode (pull lại từ git URL — không thể share local clone)
# OpenCode pulls into its own cache
```

→ Lesson: Codex/Copilot CLI = filesystem-level (sharable); OpenCode = git URL (separate cache).

### Recipe 3: Pin version cho team (reproducibility)

```json
// opencode.json
{
  "plugin": ["superpowers@git+https://github.com/obra/superpowers.git#v5.0.3"]
}
```

Team commit `opencode.json` → mọi member dùng cùng version. Tránh "works on my machine" do Superpowers update breaking changes (xem v5.0.0 breaking).

### Recipe 4: Migrate từ install cũ

V5.x có new installation mechanism. Per-harness `INSTALL.md` đều có **"Migrating from old"** section:
- Codex: remove old `~/.codex/AGENTS.md` bootstrap block
- OpenCode: remove old symlinks `~/.config/opencode/plugins/superpowers.js`

→ **Discipline:** maintainer document migration explicitly mỗi khi installation mechanism đổi. ECC không có pattern này (lighter governance).

---

## Advanced patterns

### Pattern: Manifest-driven harness portability

Thay vì rewrite skills cho từng harness, Superpowers **giữ skills format universal** (Markdown với YAML frontmatter), chỉ wrap qua manifest:

```
skills/brainstorming/SKILL.md   ← 100% universal Markdown
.claude-plugin/plugin.json       ← "skills auto-discovered"
.cursor-plugin/plugin.json       ← "skills": "./skills/"
.opencode/plugins/superpowers.js ← register via OpenCode API
```

→ Add 1 harness mới = thêm 1 manifest + INSTALL.md, **KHÔNG đụng skills**. Xem v5.0.7 (Copilot CLI added).

### Pattern: Tool name mapping ở runtime

Per `docs/README.opencode.md`:
```
Claude Code tool → OpenCode equivalent
TodoWrite       → todowrite
Task subagent   → @mention syntax
Skill tool      → native `skill` tool
```

→ Skills viết theo Claude Code conventions. OpenCode plugin script translate runtime. Allows skills tổng quát mà không cần if/else per harness.

### Pattern: Context file convention chain

```
CLAUDE.md ← canonical
AGENTS.md → CLAUDE.md (symlink) ← Codex/OpenCode pickup
GEMINI.md ← separate (Gemini doesn't follow AGENTS convention)
```

→ Tận dụng convention `AGENTS.md` đang trở thành de-facto standard cho non-Claude harnesses.

### Pattern: Brainstorm server bundled, optional

Brainstorm visual companion là zero-dependency Node.js server (v5.0.2 milestone). Bundled trong repo, nhưng chỉ chạy nếu user invoke `brainstorming` skill. **Không** start automatic.

---

## Combination với building blocks khác

### + Skills Library
Distribution Model là **delivery vehicle** cho [[(C) Skills Library]]. 14 skills ship qua đây.

### + 7-Stage Workflow
[[(C) The 7-Stage Workflow]] là content; Distribution Model là **packaging** để workflow available trong mọi harness.

### + Subagent-Driven Development
[[(C) Subagent-Driven Development]] yêu cầu harness có Task tool capability. Distribution Model **không cài SDD trên Gemini CLI** (no Task tool) — graceful degradation.

### + Hooks (cross-project: ECC)
Hooks file trong Superpowers minimal (1 SessionStart hook). ECC's [[../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) Hooks]] có 8 hook events. **Divergent design philosophy:** Superpowers favors skill-driven (declarative); ECC favors hook-driven (imperative).

---

## Anti-patterns

❌ **"Cài qua npm install"** — Superpowers KHÔNG publish lên npm. `package.json` chỉ tồn tại để OpenCode đọc `"main"` field. Đừng `npm i superpowers`.

❌ **Edit skills trong installed location** — sẽ bị overwrite khi update. Custom skills → own plugin overlay.

❌ **Mix multiple Superpowers versions across harness** — Codex pinned v5.0.3 + Claude Code latest = inconsistent behavior. Pin tất cả về same version.

❌ **Symlink approach trên Windows mà không dùng junction** — Per Codex INSTALL.md, Windows cần `mklink /J` (junction), không phải symlink thường.

❌ **Trust marketplace alone cho production team** — `superpowers-dev` marketplace không có version locking ở marketplace level. Pin qua git tag thay vì.

❌ **"Plugin sẽ install dependencies"** — zero-dependency by design. Nếu install asks dependencies → nghi ngờ supply chain.

---

## Cross-references

- [[(C) README summary]] — installation overview cho 7 harnesses
- [[(C) Release Notes overview]] — Theme 1 (multi-harness expansion timeline) + Theme 3 (zero-dependency)
- [[(C) Skills Library]] — content được distribute
- [[(C) The 7-Stage Workflow]] — workflow shipped via this model
- [[(C) Subagent-Driven Development]] — harness capability dependency
- [[(C) Philosophy and Contribution Culture summary]] — "zero-dependency by design" mandate
- [[(C) index]]
- [[(C) log]]

**Cross-project:**
- `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) Plugins.md` — ECC plugin model (manual install + plugin)
- `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) Hooks.md` — ECC's hook-driven approach (contrast)

## Citations

- `00 Sources/superpowers/.claude-plugin/plugin.json` (full file)
- `00 Sources/superpowers/.claude-plugin/marketplace.json` (full file)
- `00 Sources/superpowers/.codex/INSTALL.md` (full, lines 1–60)
- `00 Sources/superpowers/.cursor-plugin/plugin.json` (full)
- `00 Sources/superpowers/.opencode/INSTALL.md` (full, lines 1–80)
- `00 Sources/superpowers/gemini-extension.json` (full)
- `00 Sources/superpowers/package.json` (full)
- `00 Sources/superpowers/hooks/` (folder listing — 4 files)
- `00 Sources/superpowers/docs/` (folder listing — codex, opencode, windows variants)

## TODO

- ⏸ Verify Copilot CLI install mechanism (v5.0.7) — chưa đọc full release notes, infer Codex pattern
- ⏸ Test thực tế install trên 2 harness để verify symlink behavior trên macOS
- ⏸ Document brainstorm server port + how to disable (advanced config)
- ⏸ Map deprecated commands (`/brainstorm`) migration cho user cũ
