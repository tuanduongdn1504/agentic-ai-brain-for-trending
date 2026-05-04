# (C) Plugins — Entity Page

> **Type:** Building block #7 (foundation) — bundling mechanism
> **Status:** Sixth entity page (foundation 6/7 complete)
> **Sources:** 5 — README, shortform, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.claude-plugin/PLUGIN_SCHEMA_NOTES.md`
> **Last updated:** 2026-04-17

---

## Một câu / One-liner

**VI:** Plugins là **mechanism đóng gói agents + skills + commands + hooks** thành 1 unit install-able qua marketplace, thay vì setup thủ công từng component. Là "bridge concept" — không phải building block độc lập, mà là **cách distribute các building block khác**.

**EN:** Plugins are the **bundling mechanism** that packages agents + skills + commands + hooks into a single install-able unit via marketplace, instead of manual component setup. It's a "bridge concept" — not a standalone building block, but **the way other building blocks get distributed**.

---

## Khi nào dùng / Khi nào KHÔNG dùng

### ✅ Dùng plugin khi:
- **Share** workflows cho team/community qua 1 install step
- **Distribute** custom setup (agents + skills + hooks cùng lúc)
- **Version control** configs của team qua semver
- Cần **auto-update** khi author release version mới
- Cài **3rd-party tooling** (mgrep, hookify, LSP plugins)

### ❌ KHÔNG dùng plugin khi:
- Setup chỉ mình bạn dùng → config `~/.claude/` directly
- One-off experiment → inline settings
- **Plugin install KHÔNG auto-install rules** (per README) → phải install rules manual
- Cần **hot-swap** components giữa session → plugin cần re-install

---

## Plugin vs các concepts khác (chọn cái nào?)

| Tiêu chí | Plugin | Rules folder | `~/.claude/<component>` | Marketplace |
|----------|--------|--------------|-------------------------|-------------|
| **Purpose** | Bundle components | Standards/checklists | Individual component | Catalog of plugins |
| **Unit of distribution** | agents + skills + commands + hooks | Markdown files | Single file | Multiple plugins |
| **Install** | `/plugin install X@Y` | Manual copy hoặc `install.sh` | Manual file creation | `/plugin marketplace add <url>` |
| **Update** | Auto via marketplace | Manual re-copy | Manual edit | Pulls plugin updates |
| **Includes rules?** | ❌ NO (rules install separately) | N/A (IS the rules) | N/A | ❌ NO |
| **Share team** | ✅ Via marketplace URL | ✅ Via `install.sh` | ❌ Hard | ✅ Team marketplace |
| **Security risk** | **HIGH** (supply chain — code execution) | LOW (markdown only) | LOW-MED | HIGH (untrusted sources) |

> **Quy tắc quyết định:**
> - Cần **share cross-team** + components nhiều → **plugin**
> - Cần **standards/policies** only → **rules folder**
> - Cần **1 skill/agent đơn lẻ** → **`~/.claude/<component>/*.md`**
> - Plugins phụ thuộc nhau → **marketplace** (multi-plugin catalog)

---

## ECC ship: Plugin structure của chính nó

ECC **là** 1 plugin self-host marketplace. Cấu trúc:

```
everything-claude-code/
├── .claude-plugin/
│   ├── plugin.json              ← Plugin metadata + component manifest
│   ├── marketplace.json         ← Self-hosted marketplace catalog
│   ├── README.md                ← Gotchas guide
│   └── PLUGIN_SCHEMA_NOTES.md   ← Critical validator quirks (MUST READ)
├── agents/          ← 48 files (chỉ 38 được list trong plugin.json v1.10.0)
├── skills/          ← ~185 directories
├── commands/        ← ~79 files
├── hooks/           ← Auto-loaded, KHÔNG declare trong plugin.json
└── rules/           ← NOT installed via plugin (manual install required)
```

> ⚠️ **Discrepancy quan trọng:** `plugin.json` liệt kê **38 agents explicit**; filesystem có **48 agents** (verified từ ingest (C) Subagents). → **10 agent mới chưa được thêm vào manifest**. Nếu user install qua plugin (không manual clone), 10 agent này KHÔNG được load. **Contribution opportunity #4** (bên cạnh 3 opportunity đã track).

---

## Anatomy: `plugin.json` và `marketplace.json`

### `plugin.json` (individual plugin definition)

```json
{
  "name": "everything-claude-code",
  "version": "1.10.0",                    ← MANDATORY (validator bắt buộc)
  "description": "Battle-tested Claude Code plugin...",
  "author": {
    "name": "Affaan Mustafa",
    "url": "https://x.com/affaanmustafa"
  },
  "homepage": "https://ecc.tools",
  "repository": "https://github.com/affaan-m/everything-claude-code",
  "license": "MIT",
  "keywords": ["claude-code", "agents", "skills", "hooks", "tdd"],

  "agents": [                             ← MUST be array, MUST be file paths
    "./agents/planner.md",
    "./agents/code-reviewer.md",
    "...38 agents total explicit..."
  ],
  "skills": ["./skills/"],                ← Directory path OK (wrapped array)
  "commands": ["./commands/"]             ← Directory path OK (wrapped array)

  // ⚠️ NO "hooks" field! Auto-loaded by Claude Code v2.1+ convention.
}
```

### `marketplace.json` (catalog of plugins)

```json
{
  "name": "everything-claude-code",
  "owner": { "name": "Affaan Mustafa", "email": "me@affaanmustafa.com" },
  "metadata": {
    "description": "Battle-tested Claude Code configurations..."
  },
  "plugins": [                            ← Array of plugin entries
    {
      "name": "everything-claude-code",
      "source": "./",                     ← Path relative to marketplace root
      "version": "1.10.0",
      "category": "workflow",
      "tags": ["agents", "skills", "hooks", "tdd"],
      "strict": false                     ← Plugin strict mode
      // + metadata duplicated from plugin.json
    }
  ]
}
```

### Field reference (plugin.json)

| Field | Bắt buộc | Type | Ghi chú |
|-------|----------|------|---------|
| `name` | ✅ | string | Plugin identifier |
| `version` | ✅ | string | **MANDATORY** — validator fail nếu thiếu |
| `description` | ✅ | string | Marketplace display |
| `agents` | ❌ | **array of file paths** | ⚠️ Directory paths REJECTED |
| `skills` | ❌ | array (directories OK) | Có thể `["./skills/"]` |
| `commands` | ❌ | array (directories OK) | Có thể `["./commands/"]` |
| `hooks` | ❌ | **ĐỪNG ADD** | Auto-loaded v2.1+, add sẽ duplicate error |
| `author` | ❌ | object | `name`, `email`, `url` |
| `homepage`, `repository`, `license` | ❌ | string | Metadata |
| `keywords` | ❌ | array | Searchable tags |

---

## Cơ chế / How It Works

### Install flow

```
User: /plugin marketplace add https://github.com/affaan-m/everything-claude-code
    ↓
Claude Code fetch marketplace.json
    ↓
Parse plugin list, display trong /plugin UI
    ↓
User: /plugin install everything-claude-code@everything-claude-code
    ↓
Clone repo (hoặc fetch artifact) theo source URL
    ↓
Parse plugin.json:
  - Validate schema (strict!)
  - Copy agents → ~/.claude/plugins/<plugin>/agents/
  - Copy skills dir → ~/.claude/plugins/<plugin>/skills/
  - Copy commands dir → ~/.claude/plugins/<plugin>/commands/
  - Auto-detect hooks/hooks.json (v2.1+ convention)
    ↓
Claude Code load plugin components next session
    ↓
User: /plugin list → verify installed
```

### Component path resolution

| Component | Plugin path | Installed path |
|-----------|-------------|----------------|
| Agents | `./agents/planner.md` | `~/.claude/plugins/<plugin>/agents/planner.md` |
| Skills | `./skills/` | `~/.claude/plugins/<plugin>/skills/` |
| Commands | `./commands/` | `~/.claude/plugins/<plugin>/commands/` |
| Hooks | `./hooks/hooks.json` (auto) | Loaded via convention |
| Rules | ❌ NOT copied | Must install separately via `./install.sh` |

> **⚠️ Rules KHÔNG install qua plugin** — per README, "Claude Code plugins cannot distribute rules automatically."

---

## Configuration: 4 slash commands

| Command | Purpose |
|---------|---------|
| `/plugin marketplace add <url>` | Thêm marketplace từ GitHub repo URL |
| `/plugin install <plugin>@<marketplace>` | Install plugin từ marketplace |
| `/plugin list` | List plugins installed |
| `/plugin` (no args) | UI để toggle enable/disable, scroll to MCP section |

### Plugin identifier convention

Full form: `<plugin-name>@<marketplace-name>`

Ví dụ:
- `everything-claude-code@everything-claude-code` — ECC tự host marketplace
- `typescript-lsp@claude-plugins-official` — plugin từ official marketplace
- `mgrep@Mixedbread-Grep` — mgrep từ marketplace Mixedbread-Grep

> **Note:** ECC có **3 public identifier khác nhau** (đã note trong [[(C) README summary]]):
> - GitHub: `affaan-m/everything-claude-code`
> - Plugin: `everything-claude-code@everything-claude-code`
> - npm: `ecc-universal`

---

## Popular plugins ecosystem / Hệ sinh thái plugin

### Setup tác giả ECC (14 plugins installed, 4–5 enabled cùng lúc)

| Plugin | Marketplace | Purpose |
|--------|-------------|---------|
| `ralph-wiggum` | `claude-code-plugins` | Loop automation |
| `frontend-design` | `claude-code-plugins` | UI/UX patterns |
| `commit-commands` | `claude-code-plugins` | Git workflow |
| `security-guidance` | `claude-code-plugins` | Security checks |
| `pr-review-toolkit` | `claude-code-plugins` | PR automation |
| `typescript-lsp` | `claude-plugins-official` | TS intelligence (LSP) |
| `hookify` | `claude-plugins-official` | Create hooks qua conversation |
| `code-simplifier` | `claude-plugins-official` | Refactor |
| `feature-dev` | `claude-code-plugins` | Feature development workflow |
| `explanatory-output-style` | `claude-code-plugins` | Output style |
| `code-review` | `claude-code-plugins` | Review workflow |
| `context7` | `claude-plugins-official` | Live documentation lookup |
| `pyright-lsp` | `claude-plugins-official` | Python type checking |
| `mgrep` | `Mixedbread-Grep` | Better search (BM25/vector) |

### 3 categories đáng biết

1. **LSP Plugins** — Language Server Protocol tích hợp: `typescript-lsp`, `pyright-lsp`. Đặc biệt hữu ích nếu chạy Claude Code **ngoài editor** (real-time type checking, go-to-def, completions).
2. **Meta Plugins** — `hookify` (tạo hooks qua conversation), `skill-creator` (sinh skills).
3. **Tool replacement** — `mgrep` (~50% token reduction so với grep/ripgrep per longform).

---

## Recipe cho người mới / Beginner recipes

### Recipe 1: Minimal 3 plugins (safe start)

```bash
# 1. Add ECC marketplace
/plugin marketplace add https://github.com/affaan-m/everything-claude-code

# 2. Install ECC core
/plugin install everything-claude-code@everything-claude-code

# 3. Install rules manually (plugin không include rules)
cd /path/to/everything-claude-code
./install.sh typescript   # hoặc ngôn ngữ của bạn
```

### Recipe 2: Add LSP support

```bash
# Thêm official Claude plugins marketplace
/plugin marketplace add https://github.com/claude-plugins-official

# Install LSP cho language stack
/plugin install typescript-lsp@claude-plugins-official
/plugin install pyright-lsp@claude-plugins-official
```

### Recipe 3: Add mgrep để giảm token cost

```bash
/plugin marketplace add https://github.com/mixedbread-ai/mgrep
/plugin install mgrep@Mixedbread-Grep
```

### Recipe 4: Tạo plugin của riêng bạn

Cấu trúc minimal:

```
my-plugin/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── agents/
│   └── my-agent.md
└── skills/
    └── my-skill/
        └── SKILL.md
```

Publish lên GitHub, share URL.

---

## Validator quirks (MUST READ trước khi publish plugin)

> **Nguồn:** `PLUGIN_SCHEMA_NOTES.md` — "validator hostile và literal, assume worst."

### 5 rule bắt buộc

1. **`version` MANDATORY** — thiếu là fail
2. **Component fields MUST be arrays** — string rejected (`"./agents"` ❌, `["./agents/..."]` ✅)
3. **Agents MUST use file paths** — directory rejected (`["./agents/"]` ❌, liệt kê từng file ✅)
4. **Commands + skills** — directory OK nếu wrap array (`["./skills/"]` ✅)
5. **KHÔNG ADD `hooks` field** — v2.1+ auto-load, add manual → duplicate error

### Minimal known-good example

```json
{
  "version": "1.1.0",
  "agents": [
    "./agents/planner.md",
    "./agents/code-reviewer.md"
  ],
  "commands": ["./commands/"],
  "skills": ["./skills/"]
}
```

### Validate trước khi publish

```bash
claude plugin validate .claude-plugin/plugin.json
```

### Flip-flop history warning

`hooks` field đã bị **add/remove 4 lần** trong ECC history (commits `22ad036` → `a7bc5f2` → `779085e` → `e3a1306`) vì Claude Code CLI thay đổi behavior giữa pre-v2.1 và v2.1+. **Lesson:** convention changes break manifests; pin Claude Code version khi possible.

---

## Patterns kết hợp / Combination patterns

### Plugin + Marketplace (self-hosted)

Team host marketplace riêng: `marketplace.json` trong team repo, liệt kê internal plugins. `/plugin marketplace add <team-repo>` → share team-wide.

### Plugin + `.mcp.json` (project scope)

Plugin install global; nhưng project-specific MCPs vẫn dùng `.mcp.json`. **2 layer distribution:** plugin cho workflow components, `.mcp.json` cho environment-specific MCPs.

### Plugin + Rules (hybrid install)

Plugin install agents/skills/commands/hooks; sau đó `./install.sh <lang>` install rules. Hybrid vì plugin không support rules.

### Plugin + Version pinning

Nếu repo `.mcp.json` pin version MCP (`@2025.4.8`), plugin.json cũng nên pin Claude Code compatibility version. Supply chain protection.

### Plugin + LSP

Stack plugin: ECC core (workflow) + LSP plugins (type intelligence) + `mgrep` (search) + `hookify` (hook creator). 4 plugin compose thành "full dev setup."

---

## Real-world examples

| Marketplace | Source | Plugins đáng biết |
|-------------|--------|-------------------|
| `everything-claude-code` | github.com/affaan-m/everything-claude-code | ECC core |
| `claude-plugins-official` | Anthropic-maintained | LSP, hookify, context7, pyright |
| `claude-code-plugins` | Community | `ralph-wiggum`, `commit-commands`, `code-review`, `security-guidance` |
| `Mixedbread-Grep` | Mixedbread AI | `mgrep` |

---

## Security considerations (integrated với Security Guide)

> Plugin install = executing code from external source. **Supply chain attack vector thứ 2** sau MCP.

### Threats

1. **Malicious plugin marketplace** — URL lookalike (`github.com/affaan-m-official/...`)
2. **Plugin with malicious hooks** — auto-load `hooks/hooks.json` convention có nghĩa hook run without review nếu user không check
3. **Plugin with poisoned agents/skills** — 36% Snyk ToxicSkills stat (từ (C) Security Guide summary)
4. **Plugin dependency hijack** — plugin dùng npm package đã được compromise
5. **Version drift** — `@latest` → new malicious version pushed

### Mitigations

1. **Verify plugin source** — check GitHub repo, commit history, author
2. **Scan plugin với AgentShield** — `npx ecc-agentshield scan` covers hook injection + secret exposure
3. **Review `hooks/hooks.json`** của plugin trước khi accept install (đặc biệt custom hooks)
4. **Pin plugin version** — không `@latest`
5. **Use `/plugin list`** để audit đã install gì
6. **Test plugin trong devcontainer** trước khi add vào production setup

---

## Anti-patterns / Sai lầm hay gặp

1. **Add `"hooks"` field vào plugin.json** → duplicate error v2.1+. Auto-loaded by convention.
2. **Use directory path cho agents** → validator reject. Phải explicit files.
3. **Skip `version` field** → install fail với "Invalid input" generic error.
4. **Component field là string** → reject. Luôn phải wrap array (kể cả 1 entry).
5. **Tưởng plugin install include rules** → rules không copy, phải `./install.sh` manual.
6. **Install plugin từ URL lạ mà không verify** → supply chain attack. Check repo + author.
7. **Enable mọi plugin installed** → context window degrade. Disable unused per session (tác giả: 14 installed, 4–5 enabled).
8. **Dùng `@latest` trong marketplace URL** → auto-update có thể break.
9. **Quên add agent mới vào plugin.json** khi filesystem có (như ECC: 48 filesystem vs 38 manifest). → Plugin install miss components.
10. **Hardcode path tuyệt đối trong plugin config** → break khi install cross-platform (Windows vs Unix).

---

## Tools liên quan / Related Tools

| Tool | Vai trò |
|------|---------|
| `/plugin marketplace add <url>` | Add marketplace |
| `/plugin install <plugin>@<marketplace>` | Install plugin |
| `/plugin list [plugin@marketplace]` | List installed, có thể filter |
| `/plugin` (UI) | Toggle enable/disable components |
| `claude plugin validate` | Validate plugin.json schema trước publish |
| `npx ecc-agentshield scan` | Scan plugin hooks/secrets/risks |
| `/hookify` (plugin) | Tạo hooks qua conversation |
| `/skill-create` | Sinh skills từ git history |

---

## Cross-references

- [[(C) Hooks]] — plugin auto-load `hooks/hooks.json` v2.1+
- [[(C) Subagents]] — plugin bundle agents qua explicit file list (KHÔNG directory)
- [[(C) Skills]] — plugin bundle skills qua directory path OK
- [[(C) MCPs]] — plugin thường include MCP config (hybrid với project `.mcp.json`)
- [[(C) Rules and Memory]] — rules NOT installed via plugin, phải manual
- [[(C) Shortform Guide summary]] — 14 plugins tác giả dùng, LSP recommendation
- [[(C) Security Guide summary]] — supply chain risks, AgentShield mitigation
- [[(C) README summary]] — 3 identifier của ECC (GitHub/plugin/npm)
- [[(C) index]] — main catalog
- _Sẽ link tới_ [[(C) Commands]] khi tạo (legacy commands bundled trong plugin)

## Citations

- `.claude-plugin/plugin.json` (full file, 2.1KB) — ECC plugin manifest
- `.claude-plugin/marketplace.json` (full file, 1.2KB) — self-hosted marketplace catalog
- `.claude-plugin/PLUGIN_SCHEMA_NOTES.md` (full file, 5.2KB) — **critical** validator quirks, flip-flop history
- `.claude-plugin/README.md` (full file, 1.2KB) — gotchas, custom endpoints/gateways
- `README.md`, lines 170–185, 254 — install commands, identifier convention
- `the-shortform-guide.md`, lines 156–185, 287–309 — 14 plugin setup mẫu, LSP category
- Cross-verified: `plugin.json agents array length` = 38; `ls agents/*.md | wc -l` = 48 → **10-agent discrepancy**

---

## TODO cho lần ingest tiếp

- [ ] Flag agent manifest discrepancy (38 vs 48) — contribution opportunity #4 (bên cạnh README rules count 8 vs 10, VI translation, mgrep benchmark verify)
- [ ] Verify Claude Code v2.1+ hook auto-load behavior với Anthropic official docs
- [ ] Đếm commands trong plugin.json vs filesystem — có cùng discrepancy?
- [ ] Đọc 1 plugin khác (vd `hookify` plugin) để xem structure plugin bên ngoài ECC
- [ ] Tìm hiểu `strict: false` field trong marketplace.json — nghĩa là gì?
- [ ] Check xem LSP plugins anatomy khác plugins thường không (LSP có expose custom tools?)
- [ ] Verify "Claude Code plugins cannot distribute rules automatically" claim — why? Có workaround không?
