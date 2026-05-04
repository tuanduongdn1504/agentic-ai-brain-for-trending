# (C) Rules and Memory — Entity Page

> **Type:** Building block #5 (foundation) — "always-follow guidelines + persistent context"
> **Status:** Fourth entity page (format đã ổn)
> **Sources:** 6 — README, shortform, longform, `rules/README.md`, `rules/common/security.md`, `rules/common/testing.md`, `rules/typescript/coding-style.md`
> **Last updated:** 2026-04-17

---

## Một câu / One-liner

**VI:** Rules là **best practices Claude PHẢI luôn follow** (security checks, coding style, testing requirement…), viết bằng markdown trong `rules/` folder hoặc CLAUDE.md. Memory là tầng **persistent context** (CLAUDE.md, session files, dynamic system prompt) Claude load mỗi session để "nhớ" project/user. Hai khái niệm này thường đi cùng — Rules là layer **static** (luôn áp dụng), Memory là layer **dynamic** (load có chọn lọc).

**EN:** Rules are **always-follow best practices** (security checks, coding style, testing requirements) written in markdown in `rules/` or CLAUDE.md. Memory is the **persistent context layer** (CLAUDE.md, session files, dynamic system prompt) Claude loads per session to "remember" project/user. The two go together — Rules is the **static** layer (always applied), Memory is the **dynamic** layer (selectively loaded).

---

## Khi nào dùng / Khi nào KHÔNG dùng

### ✅ Dùng Rules khi:
- Có convention **cả team phải theo** (vd "no console.log in production", "80% test coverage")
- Có security check **bắt buộc** trước commit (vd "validate inputs", "parameterized queries")
- Codebase có **idiom riêng** ngôn ngữ (vd "use Zod for validation in TypeScript")
- Cần Claude **luôn check** điều gì đó, không chỉ khi user ask

### ✅ Dùng Memory (CLAUDE.md / session files) khi:
- Có **persistent context** Claude cần biết mỗi session (project overview, key people, current goals)
- Cần **bridge giữa các session** (continuing complex work hôm sau)
- Có **mode-specific context** (dev mode khác review mode khác research mode)

### ❌ KHÔNG dùng Rules khi:
- Workflow có nhiều bước cần guide → dùng **skill** (rules nói "what", skill nói "how")
- Logic enforce mechanical → dùng **hook** (rule chỉ là markdown, hook execute thật)
- Convention chỉ áp dụng 1 file đơn lẻ → ghi comment trong file luôn

### ❌ KHÔNG dùng CLAUDE.md khi:
- Context cực lớn (10K+ tokens) → split thành rules folder + skills, không nhồi vào CLAUDE.md
- Context chỉ relevant 1 mode → dùng **dynamic system prompt** (`--system-prompt`)

---

## Rules vs Skills vs Hook vs CLAUDE.md (chọn cái nào?)

| Tiêu chí | Rules | Skills | Hook | CLAUDE.md |
|----------|-------|--------|------|-----------|
| **Content** | What (standards/checklists) | How (workflows/structure) | Trigger logic + side effect | Persistent context |
| **Loading** | Auto mỗi session | On invoke / auto via description | On event | Auto mỗi session |
| **Reasoning** | ❌ Claude tự áp dụng | ✅ Workflow | ❌ Mechanical | ❌ Just context |
| **Modular?** | ✅ Per-language folder | ✅ Per skill folder | ✅ Per hook entry | ❌ 1 file |
| **Override** | Language > common | N/A | Profile / env var | Project > user |
| **Use case** | "Validate inputs", "no `any`" | `/tdd`, `/code-review` | Format on save | "I'm Storm Bear, my goal is X" |

> **Quy tắc quyết định:**
> - Cần **ràng buộc behavior** mọi session → **Rule**
> - Cần **workflow tái dùng** → **Skill**
> - Cần **enforce mechanical** → **Hook**
> - Cần **context "ai/ở đâu/làm gì"** → **CLAUDE.md** hoặc dynamic system prompt

---

## ECC ship: 15 rule directories — phân loại / 15 rule directories categorized

> Số liệu: `ls -d rules/*/` = **14 directories** + `common/` = **15 total**.

### Common (universal, 10 files)

| File | Nội dung |
|------|----------|
| `coding-style.md` | Immutability, file organization |
| `git-workflow.md` | Commit format, PR process |
| `testing.md` | TDD mandatory, 80% coverage min |
| `performance.md` | Model selection, context management |
| `patterns.md` | Design patterns, skeleton projects |
| `hooks.md` | Hook architecture |
| `agents.md` | When to delegate to subagents |
| `security.md` | 8 mandatory pre-commit checks |
| `code-review.md` | Review checklist |
| `development-workflow.md` | End-to-end dev process |

> ⚠️ **Discrepancy:** `rules/README.md` chỉ liệt kê 8 common files (thiếu `code-review.md` và `development-workflow.md`). README outdated — actual có 10. *(Verified 2026-04-17)*

### Per-language (14 directories, mỗi language ~5 files)

| Language | Files típical |
|----------|---------------|
| `typescript/` | coding-style, hooks, patterns, security, testing |
| `python/` | coding-style, hooks, patterns, security, testing |
| `golang/` | coding-style, hooks, patterns, security, testing |
| `java/`, `kotlin/`, `swift/`, `cpp/`, `csharp/`, `dart/`, `perl/`, `php/`, `rust/` | tương tự, mỗi language ~5 files |
| `web/` | Frontend/web specific (cross-language) |
| `zh/` | Chinese localization |

**Tổng số file rules ECC ship:** ~80 (10 common + 14 language * ~5).

---

## Anatomy: Một rule file trông như thế nào / What a rule file looks like

### Common rule (no frontmatter)

```markdown
# Security Guidelines

## Mandatory Security Checks

Before ANY commit:
- [ ] No hardcoded secrets (API keys, passwords, tokens)
- [ ] All user inputs validated
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (sanitized HTML)
- [ ] CSRF protection enabled
- [ ] Authentication/authorization verified
- [ ] Rate limiting on all endpoints
- [ ] Error messages don't leak sensitive data

## Secret Management
- NEVER hardcode secrets in source code
- ALWAYS use environment variables...

## Security Response Protocol
If security issue found:
1. STOP immediately
2. Use **security-reviewer** agent
3. Fix CRITICAL issues before continuing
...
```

### Language-specific rule (CÓ frontmatter `paths`)

```markdown
---
paths:
  - "**/*.ts"
  - "**/*.tsx"
  - "**/*.js"
  - "**/*.jsx"
---
# TypeScript/JavaScript Coding Style

> This file extends [common/coding-style.md](../common/coding-style.md) with TypeScript/JavaScript specific content.

## Types and Interfaces
[code examples + rules]

## Avoid `any`
- Use `unknown` for external input...

## React Props
- Define component props with named interface...
```

### Frontmatter fields

| Field | Bắt buộc cho lang? | Ý nghĩa |
|-------|--------------------|---------|
| `paths` | ✅ | Glob patterns — Claude apply rule khi edit file match pattern |

> **Convention:** language file luôn bắt đầu với reference đến common file: `> This file extends [common/xxx.md](../common/xxx.md) with <Language> specific content.`

### CLAUDE.md anatomy (Memory layer)

```markdown
# [Vault/Project] — Claude Context File

[1 sentence: what this is]

## Who I Am & My Purpose
[2-3 paragraphs in first person]

## Claude's Purpose in This Level
[Bulleted list of responsibilities + prime directive]

## Claude's Rules & Boundaries
[Bulleted concrete rules]

## Folder Structure
[ASCII tree]

## My Strengths & Weaknesses
[Bulleted, honest]

## My Goals & Current Progress
[Real numbers + plan]

## Weekly Update
[Template, fill weekly]
```

> Ví dụ chuẩn: `examples/CLAUDE.md`, `examples/user-CLAUDE.md`, `examples/saas-nextjs-CLAUDE.md` trong repo ECC.

---

## Cơ chế / How It Works

### Rules loading

```
Session starts
    ↓
Claude Code load:
  - ~/.claude/CLAUDE.md           (user-level memory)
  - ~/.claude/rules/common/*.md   (universal rules)
  - ~/.claude/rules/<lang>/*.md   (language rules, theo project)
  - <project>/CLAUDE.md           (project-level memory, override user-level)
  - <project>/.claude/rules/*.md  (project-specific rules, override defaults)
    ↓
Combined into system prompt context
    ↓
Claude follow rules trong mọi response
```

### Rule precedence (override hierarchy)

```
project rules        ← highest priority (most specific)
   ↓ (overrides)
language rules
   ↓ (overrides)
common rules         ← lowest priority (universal default)
```

> **Pattern giống CSS specificity hoặc `.gitignore`** — specific overrides general. Common rules có thể đánh dấu "may be overridden" cho rules ngôn ngữ idiom riêng (vd Go uses pointer receivers — override "immutability" của common).

### Memory loading levels

| Level | Path | Khi load |
|-------|------|----------|
| **User-level** | `~/.claude/CLAUDE.md` | Mọi session, mọi project |
| **Project-level** | `<project>/CLAUDE.md` | Khi cd vào project đó |
| **Project rules** | `<project>/.claude/rules/*.md` | Khi cd vào project đó |
| **Dynamic** | `claude --system-prompt "$(cat mode.md)"` | Theo CLI flag, mỗi mode khác nhau |

---

## Configuration: Cách install rules

### Cách 1: Install script (khuyến nghị)

```bash
# Install common + 1 language
./install.sh typescript

# Install nhiều language cùng lúc
./install.sh typescript python golang
```

### Cách 2: Manual

```bash
# Common (bắt buộc cho mọi project)
cp -r rules/common ~/.claude/rules/common

# Language theo stack
cp -r rules/typescript ~/.claude/rules/typescript
cp -r rules/python ~/.claude/rules/python
```

> ⚠️ **Quan trọng:** Copy ENTIRE directory, đừng flatten với `/*`. Common và language directory có file cùng tên (`hooks.md`, `testing.md`…) — flatten sẽ overwrite hoặc break relative `../common/` references.

### Cách 3: Disable hoặc override

- **Disable rule:** xoá file khỏi `~/.claude/rules/<lang>/`
- **Override common với language idiom:** edit language rule, thêm note "overrides common's X principle"
- **Per-project override:** tạo `<project>/.claude/rules/<lang>/<file>.md` — sẽ thắng global rule

---

## Memory persistence patterns (longform)

### Pattern 1: Session `.tmp` files

```
.claude/
└── session-2026-04-17.md   ← tóm tắt cuối session, append đến cuối
```

**Rules cho session file:**
- ✅ Approaches đã work + evidence
- ❌ Approaches đã thử không work
- ⏸ Approaches chưa thử + việc còn lại

### Pattern 2: Dynamic system prompt injection

```bash
alias claude-dev='claude --system-prompt "$(cat ~/.claude/contexts/dev.md)"'
alias claude-review='claude --system-prompt "$(cat ~/.claude/contexts/review.md)"'
alias claude-research='claude --system-prompt "$(cat ~/.claude/contexts/research.md)"'
```

> **Authority hierarchy:** system prompt > user message > tool result. System prompt = highest authority.
> *(Tác giả ECC tuyên bố như fact; cần verify với Anthropic docs — ghi vào TODO.)*

### Pattern 3: Memory persistence hooks

| Hook | Khi fire | Việc làm |
|------|----------|----------|
| `PreCompact` | Trước context compact | Save state ra `.claude/.tmp/<session>.md` |
| `Stop` | Session response xong | Append learnings ra session file |
| `SessionStart` | Session mới mở | Auto-load previous session file vào context |

> Implementation có sẵn ở `hooks/memory-persistence/` trong repo ECC.

---

## Patterns kết hợp / Combination patterns

### Rules + Skills

Rules định "what" (vd "tests must use AAA pattern"), skills định "how" (`tdd-workflow` skill execute pattern). Language rule file thường reference skill: vd `rules/python/testing.md` link tới `skills/python-testing/`.

### Rules + Hooks

Rule nói "no console.log in production"; hook `Stop` audit modified files cho `console.log`. → Rule là policy, hook là enforcement.

### Rules + Subagents

Rule nói "use security-reviewer agent for any auth code"; rule `agents.md` define **when to delegate**. Subagent thực thi rule.

### CLAUDE.md + Skills

CLAUDE.md inject context "Tao là dev TypeScript làm SaaS" → Claude tự pick relevant skill (`typescript-reviewer`, `nextjs-turbopack`) khi gặp `.tsx` file.

### Static rules + Dynamic system prompt

Static rules cho universal stuff (security, coding style); dynamic system prompt cho mode-specific (dev/review/research). Combined coverage.

---

## Real-world examples từ ECC

ECC ship **5+ example CLAUDE.md** trong `examples/`:

| File | Stack |
|------|-------|
| `CLAUDE.md` | Generic project example |
| `user-CLAUDE.md` | User-level config example |
| `saas-nextjs-CLAUDE.md` | SaaS Next.js + Supabase + Stripe |
| `go-microservice-CLAUDE.md` | Go microservice + gRPC + PostgreSQL |
| `django-api-CLAUDE.md` | Django REST API + DRF + Celery |
| `laravel-api-CLAUDE.md` | Laravel API + PostgreSQL + Redis |
| `rust-api-CLAUDE.md` | Rust API + Axum + SQLx + PostgreSQL |

> Đáng đọc trước khi tự viết CLAUDE.md — copy structure rồi customize.

---

## Anti-patterns / Sai lầm hay gặp

1. **Nhồi mọi thứ vào CLAUDE.md** → context window ăn token, slow mọi session. Move standards sang `rules/`, dynamic stuff sang `--system-prompt` flags.
2. **Flatten rules với `cp rules/common/* rules/typescript/* ~/.claude/rules/`** → file cùng tên overwrite nhau, break `../common/` references. Phải copy nguyên directory.
3. **Rule contradiction giữa common và language** → Claude bối rối. Solution: dùng "Language note" marker trong common, hoặc explicit override note trong language file.
4. **Rule quá chung chung** → "write good code" → vô nghĩa. Cụ thể: "no `any` in TypeScript application code, use `unknown` for untrusted input."
5. **CLAUDE.md không update** → stale "Weekly Update" 6 tháng trước, "current goal" outdated → Claude follow plan cũ. Nguyên tắc: update Weekly Update mỗi tuần, GOALS.md mỗi quarter.
6. **Project-level CLAUDE.md duplicate user-level** → wasted context. Project CLAUDE.md chỉ nên có **delta** (cái khác user-level), không repeat.
7. **Rule nói "use Zod" mà không có example code** → Claude không biết format. Mọi rule technical phải có code snippet.
8. **Quên `>` quote prefix khi trích common** trong language rule → markdown render xấu, traceability mất.
9. **Hardcode path tuyệt đối trong rules** → portability mất khi share team. Dùng `~/.claude/...` hoặc `${CLAUDE_PROJECT_DIR}/...`.
10. **Skip "extends common" reference trong language file** → rule lonely, không leverage được common. Convention bắt buộc.

---

## Tools liên quan / Related Tools

| Tool | Vai trò |
|------|---------|
| **`./install.sh <lang>`** | Install common + language rules vào `~/.claude/rules/` |
| **`/init`** command | Initialize CLAUDE.md cho project mới (theo Claude Code official) |
| **`brain-setup` skill** (Storm Bear vault) | Generate CLAUDE.md qua interview 5 rounds |
| **`anthropic-skills:consolidate-memory`** | Reflective pass over memory files — merge duplicates, fix stale facts |
| **`code-reviewer` agent** | Tự động check rules khi review code |
| **`security-reviewer` agent** | Tự động check security rules |

---

## Cross-references

- [[(C) Skills]] — alternative khi cần "how" (rules là "what")
- [[(C) Hooks]] — enforcement layer cho rule mechanical
- [[(C) Subagents]] — agents đọc rules + auto-apply trong review
- [[(C) Shortform Guide summary]] — Rules and Memory section + setup mẫu
- [[(C) Longform Guide summary]] — memory persistence patterns chi tiết
- [[(C) README summary]] — rules folder structure + install commands
- [[(C) index]] — main catalog
- _Sẽ link tới_ [[(C) MCPs]] khi tạo (MCP config cũng load qua memory)

## Citations

- `rules/README.md` (full file, 4.5KB) — structure, install, precedence, naming convention
- `rules/common/security.md` (full file, 862B) — example common rule
- `rules/common/testing.md` (full file, 1.4KB) — example common rule
- `rules/typescript/coding-style.md` (full file, 4.2KB) — example language-specific rule với frontmatter
- `the-shortform-guide.md`, lines 99–124 — Rules and Memory overview
- `the-longform-guide.md`, lines 38–86 — context management, dynamic system prompt, memory hooks
- `README.md`, lines 477–492 — rules tree structure trong "What's Inside"
- Counts verified: `ls -d rules/*/ | wc -l` = 14 + common = 15 total; `ls rules/common/*.md | wc -l` = 10 (README ghi 8 — outdated)

---

## TODO cho lần ingest tiếp

- [ ] Đọc `rules/common/agents.md` + `rules/common/hooks.md` để có rule-level view của 2 building blocks đó
- [ ] Đọc 1 example CLAUDE.md (vd `examples/saas-nextjs-CLAUDE.md`) để lấy concrete pattern
- [ ] Cập nhật `rules/README.md` discrepancy (8 vs 10) thành PR cho ECC repo (contribution opportunity!)
- [ ] Verify Anthropic docs xem "authority hierarchy" (system > user > tool result) là official spec hay convention
- [ ] Đếm exact rule file count: `find rules -name "*.md" | wc -l`
- [ ] Đọc `contexts/dev.md` + `contexts/review.md` + `contexts/research.md` để có concrete dynamic system prompt examples
- [ ] Compare với `anthropic-skills:consolidate-memory` skill — có cùng triết lý "review and prune memory" không?
