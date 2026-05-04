# (C) Shortform Guide Summary — Everything Claude Code

> **Source:** `00 Sources/everything-claude-code/the-shortform-guide.md` (15.9 KB, 432 lines)
> **Author:** Affaan Mustafa, Anthropic Hackathon Winner (built `zenith.chat`)
> **Ingested:** 2026-04-17
> **Coverage:** Full file đọc 1 pass.
> **Status:** README chỉ định "Read this first" → đây là document nền tảng cho beginner.

---

## TL;DR

**VI:** Shortform guide trình bày setup Claude Code sau 10 tháng dùng hằng ngày của tác giả. Cốt lõi gồm **7 building blocks**: Skills, Commands, Hooks, Subagents, Rules/Memory, MCPs, Plugins — mỗi block giải quyết một loại vấn đề riêng. Bài học lớn nhất: **context window là tài nguyên quý** — phải disable MCPs/plugins không dùng, vì 200K context có thể bị "ăn" còn 70K nếu bật quá nhiều tools.

**EN:** Shortform guide presents the author's Claude Code setup after 10 months of daily use. Core: **7 building blocks** — Skills, Commands, Hooks, Subagents, Rules/Memory, MCPs, Plugins — each solves a distinct problem. The biggest lesson: **context window is precious** — disable unused MCPs/plugins, because 200K context can shrink to 70K with too many tools enabled.

---

## 7 Building Blocks (Bộ 7 khối nền tảng)

> Bảng tóm tắt — mỗi block sẽ có entity page riêng trong các lần ingest sau.

| # | Block | Vai trò (VN) | Role (EN) | Where it lives |
|---|-------|--------------|-----------|----------------|
| 1 | **Skills** | Workflow bundles có thể tái dùng — "đơn vị bền vững nhất" của Claude Code | Reusable workflow bundles — the "durable unit" | `~/.claude/skills/` |
| 2 | **Commands** | Slash-entry shims (legacy), đang được migrate sang skills | Legacy slash-command shims, being migrated to skills | `~/.claude/commands/` |
| 3 | **Hooks** | Automation kích hoạt theo event (PreToolUse, PostToolUse, Stop, …) | Event-triggered automations | `~/.claude/settings.json` (hooks block) |
| 4 | **Subagents** | Process con với scope hẹp, để delegate task — tiết kiệm context cho main agent | Scoped child processes for delegation — frees main agent context | `~/.claude/agents/` |
| 5 | **Rules/Memory** | Best practices Claude PHẢI luôn theo (security, style, testing…) | Always-follow best practices | `~/.claude/rules/` hoặc CLAUDE.md |
| 6 | **MCPs** | Cầu nối từ Claude tới external services (DB, GitHub, Vercel, browser…) | Bridge from Claude to external services | `~/.claude/settings.json` (mcpServers) |
| 7 | **Plugins** | Đóng gói các block trên thành 1 unit dễ install | Bundle of the above into easily-installable units | `/plugin marketplace add ...` |

---

## Nguyên tắc cốt lõi / Core principles

### 1. Skills > Commands

> "Slash entries are convenient, but the real durable unit is the underlying skill."

Commands chỉ là shim để gõ `/tdd` cho nhanh. Logic thực phải nằm ở skill — vì skill có structure, supporting files, codemaps, và tái dùng được trong subagents. Khi học, hiểu skills trước.

### 2. Context window là tài nguyên quý

> "200k context window before compacting might only be 70k with too many tools enabled."

**Quy tắc ngón tay cái / Rule of thumb:**
- Có 20–30 MCPs trong config, NHƯNG chỉ bật <10 MCP per session
- Tổng số tool active < 80
- Tác giả cá nhân: **14 MCPs configured, ~5–6 enabled per project**, **4–5 plugins enabled** (trong số 14 đã install)

### 3. Scope subagent thật chặt

Subagent có quyền tools/MCPs riêng → cấu hình hẹp → focused execution. Subagent + skill là combo: subagent gọi skill để làm 1 việc cụ thể, không cần đọc lại context của main agent.

### 4. Automate cái lặp lại

Hooks dùng cho: format on save (prettier sau Edit), tmux reminder trước long-running command, block ghi `.md` ngoài README/CLAUDE, check `console.log` sau mỗi Stop.

### 5. Đừng over-architect

> "Don't overcomplicate — treat configuration like fine-tuning, not architecture."

Bắt đầu nhỏ. Thêm khi cần.

---

## 6 hook types (chi tiết / detailed)

| Type | Trigger | Use case ví dụ |
|------|---------|----------------|
| `PreToolUse` | Trước khi tool chạy | Validation, reminder (tmux khi sắp chạy `npm install`) |
| `PostToolUse` | Sau khi tool chạy xong | Format file (prettier sau Edit), typecheck (tsc --noEmit), feedback loop |
| `UserPromptSubmit` | Khi user gửi message | Inject context, log query |
| `Stop` | Claude trả lời xong | Check modified files, reminder cleanup |
| `PreCompact` | Trước khi compact context | Save state để khôi phục |
| `Notification` | Khi cần permission | Custom permission flow |

> **Pro tip:** dùng plugin `hookify` (`/hookify`) để tạo hook qua hội thoại — không cần viết JSON tay.

---

## Parallel workflows / Workflow song song

| Pattern | Khi nào dùng | Cách dùng |
|---------|--------------|-----------|
| **`/fork`** | Nhiều task KHÔNG overlap (không sửa cùng file) | Fork conversation, mỗi fork làm 1 task |
| **Git worktrees** | Nhiều task OVERLAP (sửa cùng codebase) | `git worktree add ../branch-x branch-x`, chạy Claude riêng trong mỗi worktree |
| **tmux** | Long-running commands (build, test, dev server) | `tmux new -s dev`; detach/reattach để watch logs |

---

## Keyboard shortcuts đáng nhớ / Worth-remembering shortcuts

| Phím | Chức năng |
|------|-----------|
| `Ctrl+U` | Xoá cả dòng (nhanh hơn backspace) |
| `!` | Prefix cho bash command nhanh |
| `@` | Search file |
| `/` | Slash command |
| `Shift+Enter` | Multi-line input |
| `Tab` | Toggle thinking display |
| `Esc Esc` | Interrupt Claude / restore code |

## Useful commands

- `/rewind` — quay lại state trước đó
- `/statusline` — customize status bar (branch, context %, todos)
- `/checkpoints` — file-level undo points
- `/compact` — manual context compaction
- `/mcp` — list enabled MCPs
- `/plugins` — manage plugins

---

## Editor recommendation

Tác giả dùng **Zed** (Rust-based, nhanh, ít RAM, không tranh resource với Claude khi chạy Opus). VSCode/Cursor cũng work. Bí kíp editor-agnostic:
1. Split screen (terminal + editor)
2. Auto-save bật để Claude đọc file luôn current
3. Git integration để review change của Claude trước khi commit

---

## Setup mẫu của tác giả / Author's exact setup

### Plugins (14 installed, 4–5 enabled cùng lúc)

`ralph-wiggum`, `frontend-design`, `commit-commands`, `security-guidance`, `pr-review-toolkit`, `typescript-lsp`, `hookify`, `code-simplifier`, `feature-dev`, `explanatory-output-style`, `code-review`, `context7`, `pyright-lsp`, `mgrep`

### MCPs (14 configured)

GitHub, Firecrawl, Supabase, Memory, Sequential-Thinking, Vercel, Railway, Cloudflare-Docs, Cloudflare-Workers-Bindings, ClickHouse, AbletonMCP, Magic. **Chỉ ~5–6 enabled per project.**

### Hooks chính

```
PreToolUse:
  - npm|pnpm|yarn|cargo|pytest → tmux reminder
  - Write && .md file → block trừ README/CLAUDE
  - git push → mở editor để review

PostToolUse:
  - Edit && .ts/.tsx/.js/.jsx → prettier --write
  - Edit && .ts/.tsx → tsc --noEmit
  - Edit → grep console.log warning

Stop:
  - * → check modified files for console.log
```

### Subagents

`planner`, `architect`, `tdd-guide`, `code-reviewer`, `security-reviewer`, `build-error-resolver`, `e2e-runner`, `refactor-cleaner`, `doc-updater`

### Rules folder

`security.md`, `coding-style.md`, `testing.md`, `git-workflow.md`, `agents.md`, `patterns.md`, `performance.md`, `hooks.md`

---

## 5 Key Takeaways (gốc từ tác giả)

1. **Don't overcomplicate** — treat configuration like fine-tuning, not architecture
2. **Context window is precious** — disable unused MCPs and plugins
3. **Parallel execution** — fork conversations, use git worktrees
4. **Automate the repetitive** — hooks for formatting, linting, reminders
5. **Scope your subagents** — limited tools = focused execution

---

## Beginner action plan (đề xuất từ guide này / proposed from this guide)

> Lộ trình này là gợi ý của Storm Bear wiki — không phải tác giả. Sẽ refine sau khi đọc longform guide.

**Tuần 1 — Foundation:**
1. Cài Claude Code, mở terminal + editor split screen
2. Tạo file `~/.claude/CLAUDE.md` với 5–7 rule cá nhân (style, security, testing)
3. Học 5 keyboard shortcut: `Ctrl+U`, `!`, `@`, `/`, `Esc Esc`
4. Học 3 command: `/compact`, `/rewind`, `/statusline`

**Tuần 2 — Skills & Subagents:**
5. Cài ECC plugin (full profile)
6. Dùng thử 3 skills: `/tdd`, `/refactor-clean`, `/code-review`
7. Đọc 1 subagent file (vd `code-reviewer.md`) để hiểu format
8. Thử delegate 1 task cho subagent

**Tuần 3 — Hooks & MCPs:**
9. Cài plugin `hookify`, tạo 1 hook đầu tiên (vd `prettier` sau Edit)
10. Bật 1 MCP (vd GitHub), thử dùng trong 1 task
11. Audit MCPs/plugins enabled — disable cái không dùng

**Tuần 4 — Parallel & Advanced:**
12. Thử `/fork` cho 2 task không overlap
13. Tạo 1 git worktree, chạy 2 Claude song song
14. Sang Longform Guide cho token optimization & memory persistence

---

## Cross-references

- [[(C) index]] — main catalog
- [[(C) log]] — activity log
- [[(C) README summary]] — repo overview
- [[../01 Analysis/(C) README - open questions]] — questions từ README, có cập nhật câu trả lời từ guide này

## Citations

- `the-shortform-guide.md`, lines 1–432 (full file)
- Cross-link: `the-longform-guide.md` (chưa ingest) cho advanced patterns
- External: [Plugins Reference](https://code.claude.com/docs/en/plugins-reference), [Hooks Docs](https://code.claude.com/docs/en/hooks), [Subagents](https://code.claude.com/docs/en/sub-agents), [MCP Overview](https://code.claude.com/docs/en/mcp-overview)
