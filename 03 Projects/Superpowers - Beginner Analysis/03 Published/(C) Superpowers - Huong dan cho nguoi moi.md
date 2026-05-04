# Superpowers — Hướng dẫn cho người mới

> **For team / Cho team:** Đây là hướng dẫn tổng hợp để bắt đầu với **Superpowers** — methodology + skills library cho AI coding agents do Jesse Vincent (`obra`) build. Đọc 1 lần ~30 phút, đủ để cài đặt và chạy 1 task end-to-end.
>
> **Tác giả wiki:** Storm Bear, dựa trên `obra/superpowers` (v5.0.7, Mar 2026).
> **Ngày:** 2026-04-18 | **Phiên bản:** v1
> **Song ngữ:** Tiếng Việt (chính) + English (technical terms)

---

## 📋 Mục lục

1. [Tại sao đọc cái này](#tại-sao-đọc-cái-này)
2. [Part 1: Superpowers là gì](#part-1-superpowers-là-gì)
3. [Part 2: 7-Stage Workflow](#part-2-7-stage-workflow---trái-tim-của-superpowers)
4. [Part 3: 14 Skills + 1 Agent](#part-3-14-skills--1-agent)
5. [Part 4: Setup roadmap 2 tuần](#part-4-setup-roadmap-2-tuần)
6. [Part 5: Subagent-driven & TDD discipline](#part-5-subagent-driven--tdd-discipline)
7. [Part 6: FAQ thường gặp](#part-6-faq-thường-gặp)
8. [Part 7: Resources & References](#part-7-resources--references)

---

## Tại sao đọc cái này

### Ai nên đọc / Who should read

- **Dev team** muốn chuẩn hoá workflow AI coding (TDD + code review + planning)
- **Tech lead / Scrum Coach** đang tìm methodology kỷ luật cho team
- **Anyone** đang dùng Claude Code (hoặc Codex/Cursor/OpenCode/Copilot CLI) và muốn áp pattern proven
- **Người đã đọc ECC guide** muốn so sánh 2 frameworks để chọn

### Bạn sẽ có gì sau khi đọc / What you'll get

- Hiểu **7-stage workflow** (brainstorm → branch hoàn tất) và khi nào skip stage nào
- Biết **14 skills** trong library, mỗi skill làm gì + khi nào auto-trigger
- **Setup roadmap 2 tuần** từ zero → chạy 1 PR end-to-end với SDD + TDD
- Hiểu **subagent-driven development (SDD)** — pattern Superpowers ép dùng trên capable harnesses
- Hiểu **Iron Law TDD** + tại sao Superpowers strict hơn ECC

### Không phải là gì / What this is NOT

- ❌ Không phải tutorial cài Claude Code từ đầu (xem [docs.claude.com/claude-code](https://docs.claude.com/en/docs/claude-code))
- ❌ Không cover full skill anatomy chi tiết — xem `02 Wiki/` để đọc sâu
- ❌ Không cover Brainstorm visual server (advanced, optional)

---

## Part 1: Superpowers là gì

### TL;DR

**Superpowers** là **plugin/skills library** cho Claude Code (và 6 harnesses khác), do Jesse Vincent — người đứng sau nhiều OG dev tool — build và maintain qua hơn 6 tháng (Oct 2025 → nay). Không phải feature framework như ECC. Đây là **methodology framework**: dạy agent cách làm việc đúng (TDD-first, plan trước khi code, review-driven, subagent isolation) hơn là cung cấp 200+ skills generic.

**Khác với ECC ở 4 điểm cốt lõi:**
1. **Phạm vi nhỏ hơn nhiều** — 14 skills + 1 agent (vs ECC 185 skills + 48 agents)
2. **Methodology-first** — quy trình > tools
3. **Iron Law discipline** — bắt agent recognize own rationalizations và STOP (vs ECC "best practices" tone)
4. **Public maintained** — Jesse Vincent active commits, public 94% PR rejection rate (eval-driven)

**Con số:**
- 14 skills (Testing 1, Debugging 2, Collaboration 8, Meta 2, Foundation 1)
- 1 agent (`code-reviewer`)
- 7 harnesses supported (Claude Code, Codex CLI/App, Cursor, OpenCode, Copilot CLI, Gemini CLI)
- Plugin version v5.0.7 (Mar 2026)
- Repo size: 140KB, 73 .md files (rất gọn)
- Zero external dependencies (philosophy)

### Lịch sử ngắn

- **Oct 2025:** v3.0 launch public (blog post fsck.com)
- **Dec 2025–Jan 2026:** v4.x — multi-harness foundation
- **Mar 2026:** v5.0.0 breaking — SDD bắt buộc, slash commands deprecated
- **Mar 2026 (v5.0.6):** Insight quan trọng — **inline self-review thay subagent review loop**, tiết kiệm ~25 phút/run mà không giảm chất lượng (regression test 5 versions × 5 trials)
- **Mar 2026 (v5.0.7):** Copilot CLI support added (harness #7)

### Triết lý cốt lõi

Đọc CLAUDE.md trong repo, 4 nguyên tắc:

1. **"Skills are not prose — they are code that shapes agent behavior"** → modify skill cần eval evidence
2. **Zero-dependency by design** → reject mọi PR thêm dep
3. **"Your human partner"** terminology, không phải "the user" → frame collaboration
4. **94% PR rejection rate** → công khai để cảnh báo AI agents khỏi spray-and-pray

→ **Superpowers ship opinionated framework.** Bạn dùng theo cách Jesse design hoặc fork riêng.

---

## Part 2: 7-Stage Workflow — trái tim của Superpowers

Đây là **single concept quan trọng nhất** để hiểu Superpowers. Mọi feature/bugfix đi qua 7 stage tuần tự:

```
1. Brainstorming        → spec design, user approve trước khi code
2. Using Git Worktrees   → isolate work, không pollute main branch
3. Writing Plans         → break spec thành tasks, file structure cụ thể
4. Subagent-Driven Dev   → executor + spec-reviewer + code-quality-reviewer (3 sub-prompts)
5. Test-Driven Dev       → Iron Law: NO PRODUCTION CODE WITHOUT FAILING TEST FIRST
6. Requesting Code Review → code-reviewer agent đánh giá trước khi merge
7. Finishing Branch      → cleanup, merge, archive
```

**Mỗi stage có 1 skill chính** (auto-trigger qua description matching) và **hard gates** giữa stages — không skip được.

### Stage 1: Brainstorming

Skill: `brainstorming`

```
<HARD-GATE>
Do NOT invoke any implementation skill, write any code, scaffold any project,
or take any implementation action until you have presented a design and the
user has approved it.
</HARD-GATE>
```

→ Bắt buộc design + user approve trước khi code. **Áp dụng MỌI project, không cần biết simple hay complex.**

### Stage 2: Git Worktrees

Skill: `using-git-worktrees`

Mỗi feature = 1 worktree riêng. Không làm trên main. Lý do: dễ rollback, parallel multiple agents, không pollute trunk.

### Stage 3: Writing Plans

Skill: `writing-plans`

Spec từ stage 1 → break thành tasks cụ thể. File structure section + Scope Check backstop (catch scope creep). Lưu vào `docs/superpowers/plans/YYYY-MM-DD-<topic>.md`.

### Stage 4: Subagent-Driven Development (SDD)

Skill: `subagent-driven-development`

**Quan trọng nhất.** Stage 4 chia thành 3 sub-prompts:
- **Implementer prompt** → spawn subagent execute từng task
- **Spec-reviewer prompt** → subagent so sánh code với spec
- **Code-quality-reviewer prompt** → agent `code-reviewer` đánh giá quality

Subagent return 1 trong 4 status:
- `DONE` — xong, no concerns
- `DONE_WITH_CONCERNS` — xong nhưng flag issue
- `BLOCKED` — không tự giải quyết được, cần human input
- `NEEDS_CONTEXT` — cần thêm info để tiếp tục

→ Controller agent xử lý từng status khác nhau (re-dispatch with more context, upgrade model, escalate human).

**Trên Claude Code và Codex, SDD là MANDATORY** từ v5.0.0. Removed user choice.

### Stage 5: TDD — Iron Law

Skill: `test-driven-development`

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Wording deliberate (ALL CAPS, "Iron Law"). Vi phạm? Reaction:

> "Write code before the test? **Delete it. Start over.** No exceptions: don't keep it as 'reference'. Don't 'adapt' it while writing tests. Don't look at it. **Delete means delete.**"

**11+ Common Rationalizations table** (anti-pattern detection):
| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30s. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Already manually tested" | Ad-hoc ≠ systematic. |
| "Sunk cost — too much effort to delete" | Sunk cost fallacy. |
| ... (xem [[../02 Wiki/(C) Philosophy and Contribution Culture summary]]) | |

→ Agent học recognize own rationalization → STOP → restart đúng cách.

### Stage 6: Requesting Code Review

Skill: `requesting-code-review` + agent `code-reviewer`

Sau khi code xong + tests pass, dispatch agent `code-reviewer` review. Agent return findings → fix → re-review hoặc merge.

### Stage 7: Finishing Branch

Skill: `finishing-a-development-branch`

Merge vào main, archive worktree, cleanup. Stage này short nhưng critical — không skip để tránh stale branches.

---

## Part 3: 14 Skills + 1 Agent

Đầy đủ list, theo category. Mỗi skill auto-trigger qua **description matching** (Claude đọc YAML frontmatter `description` để quyết định khi nào dùng).

### Foundation (1 skill)

| Skill | Purpose |
|-------|---------|
| `superpowers` | Meta-skill chính — entry point + index |

### Testing (1 skill)

| Skill | Purpose |
|-------|---------|
| `test-driven-development` | Iron Law TDD enforcement, 11 rationalizations table, Red Flags STOP table |

### Debugging (2 skills)

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Step-by-step debug, không guess |
| `root-cause-analysis` | 5 Whys-style depth |

### Collaboration (8 skills)

| Skill | Purpose |
|-------|---------|
| `brainstorming` | Stage 1 — design before code, hard gate |
| `using-git-worktrees` | Stage 2 — isolate work |
| `writing-plans` | Stage 3 — spec → tasks |
| `subagent-driven-development` | Stage 4 — 3 sub-prompts pattern |
| `requesting-code-review` | Stage 6 — dispatch reviewer agent |
| `finishing-a-development-branch` | Stage 7 — merge/cleanup |
| `dispatching-parallel-agents` | Multiple subagents parallel |
| `executing-plans` | Continuous execution (no batching since v5.0.0) |

### Meta (2 skills)

| Skill | Purpose |
|-------|---------|
| `writing-skills` | Meta-skill — how to author/test skills (eval-driven) |
| (1 more — TBD verify in folder listing) | |

### Agent (1)

| Agent | Purpose |
|-------|---------|
| `code-reviewer` | Stage 6 reviewer — assess production-readiness |

→ **Toàn bộ 14 skills + 1 agent < ECC's 185 skills + 48 agents.** Khác philosophy: Superpowers narrow & deep, ECC broad & shallow.

**Đọc sâu:** [[../02 Wiki/(C) Skills Library]]

---

## Part 4: Setup roadmap 2 tuần

(ECC roadmap là 4 tuần vì 185 skills + 7 building blocks. Superpowers gọn hơn → 2 tuần đủ.)

### Tuần 1: Install + chạy 1 task end-to-end

**Day 1: Install Superpowers (Claude Code path — recommended)**

```
/plugin marketplace add obra/superpowers
/plugin install superpowers@superpowers-dev
# Restart Claude Code
```

Verify: chạy `"brainstorm a feature for hello world CLI"` → skill `brainstorming` phải auto-trigger với hard gate.

**Day 2: Đọc CLAUDE.md trong repo**

Open `~/.claude/plugins/superpowers/CLAUDE.md`. Đọc toàn bộ 6.5KB. Hiểu:
- Iron Law framing
- "Your human partner" terminology
- 94% PR rejection rate warning
- 8 categories of rejected changes

**Day 3-4: Chạy 1 brainstorm + writing-plans cho task nhỏ**

Pick task thật trong project (vd: "add JSON export cho data model X"). Đi qua:
1. `brainstorming` → spec design → user approve
2. `using-git-worktrees` → isolate
3. `writing-plans` → tasks cụ thể trong `docs/superpowers/plans/`

**KHÔNG** code ở tuần 1. Mục tiêu: làm quen hard gates.

**Day 5-7: Chạy stage 4 (SDD) lần đầu**

Skill `subagent-driven-development` auto-trigger sau writing-plans. Quan sát:
- Implementer subagent return status nào? (DONE/CONCERNS/BLOCKED/NEEDS_CONTEXT)
- Spec-reviewer có catch divergence không?
- Code-quality-reviewer có flag bug nào?

→ Đọc `agents/code-reviewer.md` để hiểu reviewer rubric.

### Tuần 2: TDD discipline + production PR

**Day 8-10: Chạy TDD strict mode**

Pick 1 bug. Bắt đầu **test trước** — verify test FAIL → write code → test PASS → refactor.

**Stress test:** thử "ăn gian" — write code trước. Quan sát skill `test-driven-development` có catch + force restart không. Nếu agent rationalize ("just this once"), test xem agent có recognize anti-pattern + STOP không.

**Day 11-12: Stage 6 code review**

Skill `requesting-code-review` dispatch agent `code-reviewer`. Đọc kỹ findings — không auto-accept, học rubric.

**Day 13-14: Ship 1 PR end-to-end**

Pick 1 feature thật. Đi qua **toàn bộ 7 stages**. Document mỗi stage tốn bao lâu. Compare với cách làm trước đây.

→ Sau tuần 2, bạn có 1 PR shipped + 1 baseline về Superpowers velocity.

---

## Part 5: Subagent-driven & TDD discipline

### Subagent-driven là gì

Thay vì 1 agent monolithic làm tất cả, Superpowers dispatch **subagent isolated** cho từng task. Subagent có:
- Limited context (chỉ những gì task cần) — **context isolation principle**
- 1 task duy nhất
- Structured status return

**Lợi ích:**
- Main agent context không bị pollute
- Parallel multiple subagents (skill `dispatching-parallel-agents`)
- Failure 1 subagent không lây sang chỗ khác

**Trade-off:**
- Overhead spawn/teardown subagent (~1-3s mỗi lần)
- Phức tạp hơn debug khi subagent fail

### Tại sao Superpowers chọn SDD mandatory

Per Jesse Vincent (RELEASE-NOTES v5.0.0): **eval evidence** cho thấy SDD outperform monolithic agent trên multi-step tasks. Strict default > user choice (xem v5.0.0 breaking change).

**Lưu ý quan trọng:** Trên harness không có Task tool (Gemini CLI), SDD graceful degrade — fallback monolithic. Không crash.

### TDD Iron Law — tại sao strict

Per `test-driven-development/SKILL.md`:

> "Tests-after = 'what does this code do?' Tests-first = 'what should this code do?'"

Iron Law không phải dogma — là **shaping agent behavior**. Empirical: agent ít làm sai khi forced TDD.

**13 Red Flags** agent should detect + STOP:
- "Code before test"
- "Test passes immediately" (test đúng phải FAIL trước)
- "I'll test after"
- "It's about spirit not ritual"
- "TDD is dogmatic, I'm being pragmatic"
- ... (full list trong [[../02 Wiki/(C) Philosophy and Contribution Culture summary]])

→ Agent monitor own internal monologue. Self-policing.

### So sánh ECC

ECC dùng skill `tdd-workflow` (1 trong 185 skills). Style "best practice" — guidance, không strict gate. Agent có thể skip TDD nếu user nói "skip tests".

Superpowers: **không có way để skip TDD trên capable harness**. Iron Law.

→ Trade-off: Superpowers stricter = more friction nhưng less drift. ECC flexible = less friction nhưng dễ accumulate technical debt nếu agent rationalize.

---

## Part 6: FAQ thường gặp

### Q1: Superpowers có thay thế Claude Code không?

Không. Superpowers là **plugin overlay** lên Claude Code (hoặc 6 harnesses khác). Claude Code vẫn là CLI gốc; Superpowers thêm skills + methodology.

### Q2: Cài Superpowers có conflict ECC không?

Có khả năng overlap (cả 2 đều có TDD skill). Khi cả 2 cùng cài, skill nào có description match closer sẽ trigger. **Khuyến nghị:** chọn 1 framework chính, không mix.

### Q3: Tôi đang dùng Cursor/OpenCode, Superpowers có chạy không?

Có. Cài qua per-harness install (xem [[../02 Wiki/(C) Distribution Model]]). Lưu ý: SDD chỉ work trên harness có Task tool (Claude Code, Codex, Cursor, OpenCode). Gemini CLI không có → SDD graceful degrade.

### Q4: 7 stages có phải bắt buộc đi đủ không?

Stage 1 (brainstorming) và Stage 5 (TDD) là **hard gates** trên capable harness. Không skip. Stage 2 (worktrees) và Stage 7 (finishing) skippable nếu hot fix nhỏ. Stage 4 (SDD) auto-applied khi task ≥3 sub-tasks.

### Q5: TDD Iron Law có quá strict không?

Empirically: ít drift hơn vs ECC. Frustrating tuần đầu, payoff tuần 2-3. Nếu team kháng cự, **không nên dùng Superpowers** — culture mismatch.

### Q6: 94% PR rejection rate có thật không?

Có, public stat trong CLAUDE.md repo. Lý do: Jesse Vincent reject mọi PR thiếu eval evidence, thiếu cụ thể problem statement, hoặc spray-and-pray. **Không submit PR cho Superpowers nếu không đọc kỹ CLAUDE.md.**

### Q7: Subagent dùng nhiều có tốn token không?

Có, ~30-50% extra tokens vs monolithic. Nhưng v5.0.6 milestone tiết kiệm bằng cách thay subagent review loop bằng inline self-review (~25 phút/run saved). Net: token cost ~+30%, time saved meaningful.

### Q8: Có training/cert chính thức không?

Không. Đọc CLAUDE.md + thử qua 7 stages 2 tuần là path khuyến nghị từ Jesse.

### Q9: Tôi nên dùng Superpowers hay ECC?

→ Đọc [[(C) ECC vs Superpowers comparison]] — comparison guide chi tiết.

**TL;DR:**
- **Superpowers** nếu team value methodology, willing accept Iron Law TDD, ship deliberate PRs
- **ECC** nếu team cần broad skill library (185 skills), cross-domain coverage, less strict tone

---

## Part 7: Resources & References

### Repo + docs

- **Repo:** https://github.com/obra/superpowers
- **README:** https://github.com/obra/superpowers/blob/main/README.md
- **CLAUDE.md (philosophy):** `00 Sources/superpowers/CLAUDE.md`
- **RELEASE-NOTES:** https://github.com/obra/superpowers/blob/main/RELEASE-NOTES.md
- **Per-harness install docs:** `.codex/INSTALL.md`, `.opencode/INSTALL.md`, `docs/README.codex.md`, `docs/README.opencode.md`

### Wiki Storm Bear (đọc sâu)

- [[../02 Wiki/(C) README summary]] — overview ngắn
- [[../02 Wiki/(C) Philosophy and Contribution Culture summary]] — Iron Law + anti-pattern tables
- [[../02 Wiki/(C) Release Notes overview]] — v3 → v5.0.7 timeline + 5 themes
- [[../02 Wiki/(C) The 7-Stage Workflow]] — entity page chi tiết
- [[../02 Wiki/(C) Skills Library]] — 14 skills anatomy
- [[../02 Wiki/(C) Subagent-Driven Development]] — Stage 4 deep dive
- [[../02 Wiki/(C) Distribution Model]] — 7 harness install methods
- [[(C) ECC vs Superpowers comparison]] — comparison guide

### Author + community

- **Jesse Vincent (obra):** https://blog.fsck.com — launch blog post Oct 2025
- **Issue tracker:** https://github.com/obra/superpowers/issues
- **PR template (read trước khi submit):** `.github/PULL_REQUEST_TEMPLATE.md`

### Khi gặp issue

- **Skill không trigger:** check description matching, restart harness
- **SDD fail trên Gemini CLI:** expected — no Task tool, fallback monolithic
- **Hard gate annoying:** không bypass — design intent
- **Test framework not detected:** Superpowers expect standard test framework (pytest, vitest, jest...). Custom runner cần adapt skill `test-driven-development`

---

## Closing thoughts

Superpowers là **opinionated framework**. Nếu philosophy match (TDD-first, plan-driven, eval-evidence > opinion), bạn có 1 production-ready system trong 2 tuần. Nếu không match (team thích flexibility, ad-hoc workflow), framework sẽ feel restrictive — đừng dùng.

**Compare với ECC:** ECC là toolbox; Superpowers là discipline. Khác nhau bản chất, không phải competitor.

→ **Next action:** Đọc [[(C) ECC vs Superpowers comparison]] để quyết định framework cho team.

---

> **Wiki maintained by Storm Bear.** Tất cả insight verified từ source. Nếu thấy fact sai hoặc outdated (Superpowers update nhanh — 5 versions/tháng), ping để fix.
