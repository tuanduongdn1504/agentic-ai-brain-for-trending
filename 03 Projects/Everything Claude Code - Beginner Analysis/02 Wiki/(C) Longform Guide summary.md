# (C) Longform Guide Summary — Everything Claude Code

> **Source:** `00 Sources/everything-claude-code/the-longform-guide.md` (14.8 KB, 354 lines)
> **Author:** Affaan Mustafa
> **Ingested:** 2026-04-17
> **Coverage:** Full file đọc 1 pass.
> **Prerequisite:** Đã đọc [[(C) Shortform Guide summary]]

---

## TL;DR

**VI:** Longform là tầng "advanced" sau khi đã setup xong foundation (skills/hooks/subagents/MCPs/plugins). Trọng tâm: **token economics, memory persistence, verification patterns, parallelization, compound effects**. Đây là những kỹ thuật phân biệt session productive với session lãng phí — dựa trên 10+ tháng kinh nghiệm hằng ngày của tác giả.

**EN:** The longform layer comes after foundational setup. Focus: **token economics, memory persistence, verification patterns, parallelization, compound effects**. These are the techniques separating productive from wasteful sessions, refined over 10+ months of daily use.

---

## Mục lục / Outline

1. **Token optimization** — model selection, MCP-to-skill conversion, mgrep
2. **Memory & context management** — session files, dynamic system prompt, memory hooks
3. **Continuous learning** — Stop-hook pattern để Claude tự học từ session
4. **Verification & evals** — pass@k vs pass^k, checkpoint vs continuous evals
5. **Parallelization** — git worktrees, cascade method, two-instance kickoff
6. **Sub-agent best practices** — iterative retrieval, sequential phases
7. **Groundwork philosophy** — đầu tư vào reusable patterns

---

## 1. Token Optimization

### Strategy 1: Subagent architecture chọn model rẻ nhất đủ dùng

> Default Sonnet cho 90% coding tasks. Upgrade Opus chỉ khi: lần đầu thất bại / span 5+ files / architectural decisions / security-critical.

| Task | Model | Lý do |
|------|-------|-------|
| Exploration / search | **Haiku** | Nhanh, rẻ, đủ tốt để tìm file |
| Simple edits (1 file) | **Haiku** | Single-file, instructions rõ |
| Multi-file implementation | **Sonnet** | Balance tốt nhất cho coding |
| Complex architecture | **Opus** | Cần deep reasoning |
| PR reviews | **Sonnet** | Hiểu context, bắt nuance |
| Security analysis | **Opus** | Không được miss vulnerability |
| Writing docs | **Haiku** | Structure đơn giản |
| Debugging complex bugs | **Opus** | Cần giữ cả system trong đầu |

### Strategy 2: Convert MCP → CLI + Skill

> Nhiều MCP (GitHub, Supabase, Vercel, Railway) chỉ là wrapper quanh CLI có sẵn. CLI + custom skill = **giảm context cost** mà vẫn có ergonomics.

**Ví dụ:** thay vì load GitHub MCP cả session, tạo command `/gh-pr` wrap `gh pr create` với options ưa thích. Skill được lazy-load khi cần.

> ⚠️ Lưu ý: lazy loading giải quyết **context window**, KHÔNG giải quyết **token usage / cost**. CLI + skill vẫn là token optimization, không chỉ là context optimization.

### Strategy 3: Replace `grep` với `mgrep`

- **~50% token reduction** so với grep/ripgrep (theo benchmark 50-task của tác giả)
- Cùng (hoặc tốt hơn) judged quality
- Đây là **quantitative number** đáng nhớ

### Strategy 4: Modular codebase

File chính nên 100s lines (không 1000s). Lợi ích kép: token-efficient + Claude làm đúng từ lần đầu cao hơn.

---

## 2. Memory & Context Management

### Session files (giữa các session)

**Pattern:** skill/command tóm tắt session, lưu vào `.tmp` file trong `.claude/`, append đến cuối session. Hôm sau load file đó để pick up.

**Mỗi session một file riêng** — không pollute context cũ vào work mới.

**Session file phải chứa:**
- ✅ Approaches nào đã work (kèm evidence)
- ❌ Approaches nào đã thử nhưng không work
- ⏸ Approaches chưa thử + việc còn lại

### Strategic clearing

- Disable **auto compact**
- Manually compact tại logical interval (sau exploration phase, trước implementation phase)
- Hoặc tạo skill compact hộ
- Plan mode mặc định đã clear context sau khi plan xong → tận dụng

### Dynamic system prompt injection

Thay vì nhồi mọi thứ vào CLAUDE.md (load mỗi session), dùng CLI flag để inject context theo mode:

```bash
alias claude-dev='claude --system-prompt "$(cat ~/.claude/contexts/dev.md)"'
alias claude-review='claude --system-prompt "$(cat ~/.claude/contexts/review.md)"'
alias claude-research='claude --system-prompt "$(cat ~/.claude/contexts/research.md)"'
```

> **Authority hierarchy:** system prompt > user message > tool result. System prompt = highest authority.

### Memory persistence hooks (ít người biết)

| Hook | Khi nào fire | Use case |
|------|--------------|----------|
| `PreCompact` | Trước context compaction | Save important state ra file |
| `Stop` (Session End) | Khi session kết thúc | Persist learnings ra file |
| `SessionStart` | Session mới bắt đầu | Auto-load previous context |

**Repo path:** `hooks/memory-persistence/` — có sẵn implementation.

---

## 3. Continuous Learning (giải Q7 từ ingest README)

> **Pattern cốt lõi:** Khi Claude phát hiện thứ gì non-trivial (debug technique, workaround, project-specific pattern), nó **lưu thành skill mới**. Lần sau gặp problem tương tự, skill auto-load.

**Vấn đề muốn giải:**
- Wasted tokens khi phải lặp lại prompt
- Wasted context khi Claude gặp cùng issue
- Wasted time

**Design quan trọng — Stop hook, KHÔNG dùng UserPromptSubmit:**

| Hook | Tần suất chạy | Trade-off |
|------|---------------|-----------|
| `UserPromptSubmit` | Mỗi message | Latency mỗi prompt → ❌ |
| `Stop` (session end) | 1 lần / session | Lightweight → ✅ |

**Repo:** `skills/continuous-learning/` (v1) — Stop-hook based pattern extraction.

**v2 ("instinct-based với confidence scoring") — Vẫn chưa rõ chi tiết kỹ thuật.** Longform guide không đi sâu v2; chỉ README mention nó. **Cần đọc trực tiếp `skills/continuous-learning-v2/` để hiểu.**

> External reference: `rlancemartin.github.io/2025/12/01/claude_diary/` — "Session reflection pattern"

---

## 4. Verification Loops & Evals

### Eval pattern types

| Type | Khi chạy | Use case |
|------|----------|----------|
| **Checkpoint-based** | Tại checkpoint định nghĩa trước | Verify against criteria, fix trước khi proceed |
| **Continuous** | Mỗi N phút hoặc sau major change | Full test suite + lint |

### Key metrics: pass@k vs pass^k

**Cực kỳ quan trọng — mọi người mới phải hiểu:**

```
pass@k: ÍT NHẤT 1 trong k attempts thành công
        k=1: 70%   k=3: 91%   k=5: 97%

pass^k: TẤT CẢ k attempts đều phải thành công
        k=1: 70%   k=3: 34%   k=5: 17%
```

**Cách dùng:**
- **`pass@k`** — khi chỉ cần "nó work" (vd prototype, exploration). Nhiều attempt = xác suất 1 cái work tăng nhanh.
- **`pass^k`** — khi cần consistency (vd production CI, autonomous loop). Nhiều attempt = xác suất MỌI cái work giảm nhanh.

> **Insight:** Cùng base rate 70%, nhưng k=5 attempts cho thấy: pass@k = 97% (tốt) vs pass^k = 17% (tệ). **Đây là lý do reliability ≠ capability.**

### Benchmarking workflow để verify giá trị skill

Fork conversation: 1 fork dùng skill, 1 fork không dùng. Diff output. Xem skill có thực sự cải thiện không.

---

## 5. Parallelization

### Nguyên tắc / Principle

> "How much can you get done with the **minimum viable amount** of parallelization."

Không set arbitrary terminal counts (Boris ở Anthropic gợi ý 5+5; tác giả advise against). Mỗi terminal mới phải có lý do thực sự cần.

### Tác giả's preferred pattern

- **Main chat** — code changes
- **Forks** — câu hỏi về codebase, research external services

### Git worktrees cho overlapping work

```bash
git worktree add ../project-feature-a feature-a
git worktree add ../project-feature-b feature-b
git worktree add ../project-refactor refactor-branch
cd ../project-feature-a && claude
```

**Khi nào MUST dùng worktree:** scale instances + work overlap về code. Cộng `/rename <name>` để chat dễ phân biệt.

### Cascade Method

- Tab mới mở về phía phải
- Sweep left → right (oldest → newest)
- Tối đa 3–4 task active cùng lúc

---

## 6. Sub-agent Best Practices

### Sub-agent context problem (giải Q8 từ ingest README)

> **Vấn đề:** Sub-agent tồn tại để save context (return summary, không dump everything). Nhưng **orchestrator có semantic context mà sub-agent không có**. Sub-agent chỉ biết literal query, không biết PURPOSE đằng sau.

### Iterative Retrieval Pattern (giải Q8)

```
1. Orchestrator evaluate mỗi return của sub-agent
2. Hỏi follow-up questions TRƯỚC KHI accept
3. Sub-agent về source, lấy thêm answer, return lại
4. Loop đến khi đủ (max 3 cycles)
```

**Key:** Pass **objective context**, không chỉ query.

> **Ví dụ cụ thể:**
> - ❌ "Search for `authentication`"
> - ✅ "Search for `authentication` — context: tao đang refactor middleware, cần biết tất cả entry point gọi auth check để không miss case nào"

### Orchestrator with sequential phases

```
Phase 1: RESEARCH (Explore agent) → research-summary.md
Phase 2: PLAN (planner agent) → plan.md
Phase 3: IMPLEMENT (tdd-guide agent) → code changes
Phase 4: REVIEW (code-reviewer agent) → review-comments.md
Phase 5: VERIFY (build-error-resolver if needed) → done or loop back
```

**5 rules:**
1. Mỗi agent: ONE clear input → ONE clear output
2. Output của phase N = input của phase N+1
3. Không skip phase
4. `/clear` giữa các agent
5. Lưu intermediate output ra **file** (không giữ trong conversation)

---

## 7. Groundwork: Two-Instance Kickoff

Pattern bắt đầu repo mới với **2 Claude instances song song**:

| Instance | Vai trò | Output |
|----------|---------|--------|
| **1: Scaffolding Agent** | Lays scaffold, project structure, configs (CLAUDE.md, rules, agents) | Skeleton repo |
| **2: Deep Research Agent** | Connect services + web search, tạo PRD, mermaid architecture, compile docs | PRD + architecture docs |

### `llms.txt` pattern

Nhiều docs site có `/llms.txt` — phiên bản LLM-optimized (clean, structured). Thêm `/llms.txt` vào URL khi reach docs page để check.

### Compound effects philosophy (từ @omarsar0)

> "Early on, I spent time building reusable workflows/patterns. Tedious to build, but this had a wild compounding effect as models and agent harnesses improved."

**Đầu tư vào:**
- Subagents
- Skills
- Commands
- Planning patterns
- MCP tools
- Context engineering patterns

> **Đây là cùng triết lý với LLM Wiki pattern của Karpathy** — đầu tư vào artifact persistent, hoa lợi compound theo thời gian. Storm Bear vault và ECC chia sẻ cùng worldview.

---

## "Fun stuff" (không critical)

- **`/statusline`** — custom status bar
- **Voice transcription** — superwhisper / MacWhisper trên Mac (tác giả dùng); transcription mistakes OK vì Claude hiểu intent
- **Terminal aliases** — `alias c='claude'` v.v.

---

## Resources cuối guide

- **`claude-flow`** — community enterprise orchestration với 54+ specialized agents
- **`skills/continuous-learning/`** trong repo — implementation v1
- **`system-prompts-and-models-of-ai-tools`** (110k+ stars) — community collection AI system prompts
- **Anthropic Academy** — `anthropic.skilljar.com`

---

## Câu hỏi từ ingest này / New open questions

1. **`mgrep` 50-task benchmark** — ở đâu? Tự reproduce được không? **→ verify trước khi viết vào beginner guide.**
2. **`continuous-learning` v1 vs v2 architecture** — longform mention v1 (Stop-hook), không đi sâu v2. **→ phải đọc skills/continuous-learning-v2/.**
3. **Authority hierarchy: system > user > tool result** — tác giả tuyên bố như fact. Cần verify với Anthropic docs chính thức. *(Khả năng cao đúng — Anthropic system prompt thường có cao authority hơn — nhưng "tool result" có thực sự là tier 3 chính thức không?)*
4. **`/clear` giữa các agent trong sequential phases** — `/clear` xoá toàn bộ context. Vậy làm sao agent N+1 biết output của agent N? **→ Phải qua FILE (rule #5). OK, đã hiểu.** *(Tự giải.)*
5. **Plan mode "default option clears context"** — feature này đã có sẵn trong Claude Code chưa? Phiên bản nào? **→ check Claude Code release notes.**
6. **`llms.txt` chuẩn hoá ở đâu?** — proposal của Anthropic, Mintlify, hay community? **→ google "llms.txt spec".**

---

## Cross-references

- [[(C) index]] — main catalog
- [[(C) log]] — activity log
- [[(C) README summary]] — repo overview
- [[(C) Shortform Guide summary]] — foundation prerequisite
- [[../01 Analysis/(C) README - open questions]] — open questions từ README, có cập nhật câu trả lời từ guide này

## Citations

- `the-longform-guide.md`, lines 1–354 (full file)
- Cross-link: `the-shortform-guide.md` (đã ingest)
- External: [Anthropic — Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), [RLanceMartin — Claude Diary](https://rlancemartin.github.io/2025/12/01/claude_diary/)
