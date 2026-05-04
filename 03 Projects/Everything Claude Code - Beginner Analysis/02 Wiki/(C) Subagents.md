# (C) Subagents — Entity Page

> **Type:** Building block #4 (foundation)
> **Status:** Second entity page (re-test format)
> **Sources:** 5 — README, shortform, longform, `agents/planner.md`, `agents/code-reviewer.md`, `agents/harness-optimizer.md`
> **Last updated:** 2026-04-17

---

## Một câu / One-liner

**VI:** Subagents là **process Claude con với scope và tool permissions giới hạn**, được orchestrator (Claude chính) delegate task để thực thi 1 việc cụ thể — return summary thay vì dump toàn bộ exploration → giúp main agent giữ context window khoẻ.

**EN:** Subagents are **scoped child Claude processes with limited tool permissions** that the orchestrator (main Claude) delegates tasks to — they return summaries instead of dumping exploration → keep main agent's context window healthy.

---

## Khi nào dùng / Khi nào KHÔNG dùng

### ✅ Dùng subagent khi:
- Task **tốn nhiều exploration** (đọc 10+ files để trả lời 1 câu hỏi) → return summary
- Task **lặp lại** với scope rõ (code review, build error fix, doc update)
- Cần **model khác** (vd Opus cho planning, Haiku cho exploration)
- Cần **tool scope hẹp** vì lý do safety (vd reviewer không cần Edit/Write)
- Cần chạy **song song** nhiều task không overlap

### ❌ KHÔNG dùng subagent khi:
- Task ngắn, 1-2 step → main agent làm thẳng
- Cần **interactive iteration** với user → subagent chạy 1 lần rồi return, không hội thoại
- Cần Claude "nhớ" full context → subagent không thấy main conversation
- Logic chỉ là format/automate → dùng **hook** thay vì subagent

---

## Subagent vs Hook vs Skill (chọn cái nào?)

| Tiêu chí | Hook | Skill | Subagent |
|----------|------|-------|----------|
| **Trigger** | Event tự động (PreTool, PostTool, Stop…) | User invoke (/skill-name) hoặc auto via description | Orchestrator delegate |
| **Reasoning** | ❌ Không | ✅ Có (workflow) | ✅ Có (full Claude inference) |
| **Latency** | Phải nhanh (< 200ms cho blocking) | Trung bình | Chậm nhất (spawn + inference) |
| **Cost** | ~0 token | Token của main session | Token RIÊNG cho subagent (cộng thêm) |
| **Output** | Stderr warning / block | Trả về cùng conversation | Summary trả về cho orchestrator |
| **Khi dùng** | Enforce rule, format, audit | Reusable workflow + structure | Delegate exploration / phân biệt model |

---

## ECC ship 48 agents — phân loại / 48 agents categorized

> Số liệu verified bằng `ls agents/ | wc -l` (2026-04-17). README Quick Start ghi 48 — chính xác. Changelog v1.10.0 ghi 38 — outdated.

### Theo vai trò / By role

| Loại | Ví dụ |
|------|-------|
| **Reviewer** (code review per language) | `code-reviewer`, `python-reviewer`, `typescript-reviewer`, `go-reviewer`, `java-reviewer`, `rust-reviewer`, `kotlin-reviewer`, `cpp-reviewer`, `csharp-reviewer`, `flutter-reviewer`, `dart-reviewer`, `database-reviewer`, `healthcare-reviewer`, `security-reviewer`, `a11y-architect` |
| **Build resolver** (fix build errors per stack) | `build-error-resolver`, `cpp-build-resolver`, `go-build-resolver`, `java-build-resolver`, `kotlin-build-resolver`, `rust-build-resolver`, `dart-build-resolver`, `pytorch-build-resolver` |
| **Planner / Architect** | `planner`, `architect`, `code-architect`, `gan-planner` |
| **Specialist / Helper** | `tdd-guide`, `e2e-runner`, `refactor-cleaner`, `doc-updater`, `docs-lookup`, `code-explorer`, `code-simplifier`, `comment-analyzer`, `conversation-analyzer`, `silent-failure-hunter`, `type-design-analyzer`, `pr-test-analyzer`, `seo-specialist`, `performance-optimizer` |
| **Operator / Meta** | `chief-of-staff`, `loop-operator`, `harness-optimizer`, `gan-evaluator`, `gan-generator`, `opensource-forker`, `opensource-packager`, `opensource-sanitizer` |

### Theo model assignment

- **Opus** — planner, security-reviewer, complex architecture decisions
- **Sonnet** — most reviewers, harness-optimizer, default coding tasks
- **Haiku** — exploration agents (code-explorer)

---

## Anatomy: Một subagent file trông như thế nào / What an agent file looks like

```markdown
---
name: planner
description: Expert planning specialist for complex features and refactoring.
             Use PROACTIVELY when users request feature implementation,
             architectural changes, or complex refactoring.
             Automatically activated for planning tasks.
tools: ["Read", "Grep", "Glob"]
model: opus
color: teal              # optional, hiển thị trong UI
---

You are an expert planning specialist focused on creating comprehensive,
actionable implementation plans.

## Your Role
- Analyze requirements...
- Break down complex features...

## Workflow
### 1. Requirements Analysis
- Understand the feature request completely
...

## Plan Format
[markdown template orchestrator có thể parse]

## Best Practices
1. Be Specific: Use exact file paths, function names...
...

## Worked Example
[concrete example showing expected detail level]
```

### Frontmatter fields

| Field | Bắt buộc | Ý nghĩa |
|-------|----------|---------|
| `name` | ✅ | Định danh, lowercase + hyphen (`code-reviewer`) |
| `description` | ✅ | **Quyết định khi nào Claude tự delegate.** Dùng "PROACTIVELY", "MUST BE USED", "Automatically activated" để trigger mạnh. |
| `tools` | ✅ | List tools subagent được phép dùng. Càng hẹp càng safe. |
| `model` | ✅ | `opus` / `sonnet` / `haiku` |
| `color` | ❌ | UI accent color |

### Tool scope examples (real)

| Agent | Tools | Tại sao |
|-------|-------|---------|
| `planner` | `Read, Grep, Glob` | Chỉ phân tích, không sửa code |
| `code-reviewer` | `Read, Grep, Glob, Bash` | Cần `git diff`, `git log` qua Bash |
| `harness-optimizer` | `Read, Grep, Glob, Bash, Edit` | Cần Edit để apply config changes |
| `tdd-guide` | (hẹp) | Không cần Bash vì không chạy code, chỉ guide |

> **Pattern:** **Pure analyzer** = Read/Grep/Glob. **Reviewer with git** = thêm Bash. **Implementer** = thêm Edit/Write.

---

## Cơ chế / How It Works

```
User request
    ↓
Main Claude (orchestrator) đánh giá
    ↓
Match description của subagent?
    ↓
Spawn subagent process (separate context)
    ↓
Subagent có:
  - Frontmatter + body làm system prompt
  - Tool permissions giới hạn (theo `tools`)
  - Model riêng (theo `model`)
  - Task description từ orchestrator
    ↓
Subagent runs (có thể nhiều turn)
    ↓
Subagent return SUMMARY (không return raw exploration)
    ↓
Orchestrator nhận summary, tiếp tục với main user
```

### Auto vs explicit invocation

| Cách | Trigger | Ví dụ |
|------|---------|-------|
| **Auto** | Description có "PROACTIVELY", "MUST BE USED" + Claude detect match | Sau Edit/Write code → code-reviewer auto fire |
| **Explicit** | User gọi tên / orchestrator gọi tên | "Use the planner agent to design X" |

---

## Sub-agent Context Problem (longform pattern)

> **Vấn đề cốt lõi:** Subagent existed để save context (return summary), nhưng orchestrator có **semantic context mà subagent không có**. Subagent chỉ biết literal query, không biết PURPOSE.

### Ví dụ / Example

| Cách gọi | Kết quả |
|----------|---------|
| ❌ "Search for `authentication`" | Subagent return list 50 file match từ "authentication" — không biết relevant cái nào |
| ✅ "Search for `authentication` — context: tao đang refactor middleware, cần tất cả entry point gọi auth check để không miss case nào" | Subagent return curated list 8 entry point thật sự cần xem |

### Iterative Retrieval Pattern (giải pháp)

```
1. Orchestrator gọi subagent với query + context
2. Subagent return summary
3. Orchestrator EVALUATE — đủ chưa?
4. Nếu thiếu → orchestrator hỏi follow-up (vd "what about middleware in api/v2?")
5. Subagent về source, lấy thêm, return lại
6. Loop max 3 cycles
```

> **Key:** Pass **objective context**, không chỉ raw query.

---

## Sequential Phases Orchestration (longform pattern)

> Orchestrator tự chạy 5 agent tuần tự, mỗi phase có 1 input/output rõ.

```
Phase 1: RESEARCH    → Explore agent       → research-summary.md
Phase 2: PLAN        → planner agent       → plan.md
Phase 3: IMPLEMENT   → tdd-guide agent     → code changes
Phase 4: REVIEW      → code-reviewer agent → review-comments.md
Phase 5: VERIFY      → build-error-resolver → done OR loop back
```

### 5 rules

1. Mỗi agent: **ONE clear input → ONE clear output**
2. Output của phase N = input của phase N+1
3. **Không skip phase**
4. **`/clear` giữa các agent** (xoá conversation, không xoá file)
5. Lưu intermediate output ra **FILE** (không giữ trong conversation)

> ⚠️ Vì `/clear` xoá conversation, agent N+1 phải đọc file output của agent N. Convention naming/path là TODO chưa rõ — đọc agent files cụ thể để xem.

---

## Anti-patterns / Sai lầm hay gặp

1. **Tạo subagent cho task ngắn** — overhead spawn + inference > tiết kiệm context. Dùng main agent.
2. **Description quá generic** — "helps with code" → Claude không biết khi nào fire. Cụ thể: "Use PROACTIVELY after writing or modifying TypeScript code."
3. **Mở quá nhiều tools** — vi phạm principle of least privilege. Reviewer không nên có Write/Edit.
4. **Không pass objective context** — subagent gặp sub-agent context problem, return junk.
5. **Skip phase trong sequential orchestration** — agent N+1 thiếu input, hallucinate.
6. **Không `/clear` giữa các phase** — context của phase trước pollute phase sau, defeats mục đích delegate.
7. **Kỳ vọng subagent "nhớ" main conversation** — subagent chỉ thấy task description, không thấy chat history.
8. **Spawn arbitrary terminal counts** (5 local + 5 upstream) — Boris suggest, tác giả ECC advise against. Minimum viable parallelization.

---

## Patterns kết hợp / Combination patterns

### Subagent + Skill

Subagent có thể gọi skill. Vd `tdd-guide` agent dùng skill `tdd-workflow` để execute. → Tái dùng workflow knowledge giữa main agent và sub.

### Subagent + Hook

Hook có thể trigger sự delegation. Vd `Stop` hook detect modified `.ts` file → main agent tự delegate cho `typescript-reviewer`.

### Subagent + Plan Mode

Plan mode (Shift+Tab) có thể spawn `planner` agent để tạo plan, sau đó `/clear` rồi vào execution. Tận dụng "context cleared after plan" của plan mode.

---

## Two-Instance Kickoff (longform pattern, áp dụng cho project mới)

| Instance | Vai trò | Output |
|----------|---------|--------|
| **1: Scaffolding Agent** | Tạo project structure, configs (CLAUDE.md, rules, agents) | Skeleton repo |
| **2: Deep Research Agent** | Connect services + web search, viết PRD, mermaid architecture, compile docs | PRD + architecture docs |

> Chạy 2 instance song song, mỗi instance focus 1 mảng, không overlap.

---

## Cross-references

- [[(C) Hooks]] — alternative khi không cần reasoning, chỉ cần enforce
- [[(C) Shortform Guide summary]] — subagent overview + setup mẫu (9 agents tác giả dùng)
- [[(C) Longform Guide summary]] — sub-agent context problem, iterative retrieval, sequential phases
- [[(C) README summary]] — list 28+ agents kèm vai trò
- [[(C) index]] — main catalog
- _Sẽ link tới_ [[(C) Skills]] khi entity page Skills tạo (subagent thường dùng skill)

## Citations

- `agents/planner.md` (full file, 6.9KB) — concrete agent example với worked example chi tiết
- `agents/code-reviewer.md` (lines 1–80) — confidence-based filtering pattern, security checklist
- `agents/harness-optimizer.md` (full file, 928B) — minimal agent contrast
- `the-shortform-guide.md`, lines 76–95 — subagent overview, scoping principle
- `the-longform-guide.md`, lines 256–286 — context problem, iterative retrieval, sequential phases
- `README.md`, lines 346–373 — list 28+ specific agents kèm vai trò
- Agent count verified: `ls agents/ | wc -l` = 48 (giải Q2 từ open questions)

---

## TODO cho lần ingest tiếp

- [ ] Đọc 2-3 agent files khác (`tdd-guide.md`, `architect.md`, `e2e-runner.md`) verify pattern frontmatter có consistent không
- [ ] Tìm convention naming/path cho file giữa sequential phases (vd `research-summary.md` ở đâu?)
- [ ] Verify với Anthropic docs: `tools` field có exhaustive list nào không? Có tool nào subagent KHÔNG được phép dùng không?
- [ ] Check xem Anthropic docs có khái niệm "subagent" chính thức không, hay đây là ECC convention
