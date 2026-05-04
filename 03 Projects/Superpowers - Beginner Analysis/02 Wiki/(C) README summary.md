# (C) README Summary — Superpowers

> **Source:** `00 Sources/superpowers/README.md` (7.4KB, 199 lines)
> **Author:** Jesse Vincent (`obra`) at Prime Radiant
> **Ingested:** 2026-04-18
> **Coverage:** Full file 1 pass

---

## TL;DR

**VI:** Superpowers là **complete software development methodology** cho coding agents — đóng gói thành plugin với composable skills + initial instructions để agent tự dùng. Khác ECC (configuration pack), Superpowers là **methodology trước, skills sau**: agent KHÔNG nhảy vào code mà step back, brainstorm spec, plan implementation, rồi mới TDD execute. Có thể chạy autonomous "vài giờ liền không deviate." Available trên 7 harnesses (Claude Code official + community + Codex CLI/App + Cursor + OpenCode + Copilot CLI + Gemini).

**EN:** Superpowers is a complete software development methodology for coding agents, packaged as a plugin with composable skills + initial instructions ensuring the agent uses them. Unlike ECC (configuration pack), Superpowers is **methodology-first, skills-second**: the agent doesn't jump into coding — it steps back, brainstorms spec, plans implementation, then TDD-executes. Can run autonomous "for hours without deviating." Available on 7 harnesses.

---

## Core philosophy

**4 principles (giống ECC nhưng wording khác):**

1. **Test-Driven Development** — Write tests first, always. **No exceptions** without your human partner's permission.
2. **Systematic over ad-hoc** — Process over guessing
3. **Complexity reduction** — Simplicity as primary goal
4. **Evidence over claims** — Verify before declaring success

**Distinctive language:**
- *"Your human partner"* — không "the user" (deliberate, được flag trong CLAUDE.md là không thay đổi được)
- *"Mandatory workflows, not suggestions"* — stricter enforcement than ECC
- *"94% PR rejection rate"* — quality bar publicly stated trong CLAUDE.md

---

## How it works (bestselling point của README)

> Excerpt nguyên văn:
> *"As soon as it sees that you're building something, it doesn't just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do."*

**Flow tự động (qua skills auto-trigger):**
1. Agent detect "building something" → activate `brainstorming` skill
2. Tease spec qua dialogue → present trong chunks ngắn
3. After sign-off → `writing-plans` tạo implementation plan "đủ rõ cho enthusiastic junior engineer"
4. User say "go" → `subagent-driven-development` launches, agents work through tasks
5. **Có thể autonomous vài giờ** không deviate

**Vai trò user:** approve spec → approve plan → say "go" → review final.

**Vai trò agent:** brainstorm → plan → execute → verify → review.

---

## The 7-Stage Basic Workflow (xem entity page)

Workflow names + skills tương ứng:

| # | Stage | Skill |
|---|-------|-------|
| 1 | brainstorming | `brainstorming` — Socratic refinement, save design doc |
| 2 | git worktrees | `using-git-worktrees` — isolated workspace, clean test baseline |
| 3 | writing plans | `writing-plans` — bite-sized tasks (2-5 phút each) với exact paths + complete code |
| 4 | subagent execution | `subagent-driven-development` hoặc `executing-plans` |
| 5 | TDD | `test-driven-development` — RED-GREEN-REFACTOR enforcement |
| 6 | code review | `requesting-code-review` |
| 7 | branch finishing | `finishing-a-development-branch` — merge/PR/keep/discard, cleanup |

> **The agent checks for relevant skills before any task.** Mandatory workflows, not suggestions.

→ Detail trong [[(C) The 7-Stage Workflow]] entity page.

---

## Skills library (14 skills tổng cộng)

**Categorized:**

### Testing (1 skill)
- `test-driven-development` — RED-GREEN-REFACTOR cycle (includes testing anti-patterns reference)

### Debugging (2 skills)
- `systematic-debugging` — 4-phase root cause process (gồm root-cause-tracing, defense-in-depth, condition-based-waiting)
- `verification-before-completion` — Ensure it's actually fixed

### Collaboration (8 skills)
- `brainstorming` — Socratic design refinement
- `writing-plans` — Detailed implementation plans
- `executing-plans` — Batch execution với checkpoints
- `dispatching-parallel-agents` — Concurrent subagent workflows
- `requesting-code-review` — Pre-review checklist
- `receiving-code-review` — Responding to feedback
- `using-git-worktrees` — Parallel development branches
- `finishing-a-development-branch` — Merge/PR decision workflow
- `subagent-driven-development` — Fast iteration với two-stage review (spec compliance, then code quality)

### Meta (2 skills)
- `writing-skills` — Create new skills theo best practices
- `using-superpowers` — Introduction to skills system

→ Detail trong [[(C) Skills Library]] entity page.

---

## Cross-harness installation (7 harnesses!)

> Đây là **distinctive feature** — nhiều harness hơn ECC:

| Harness | Install method |
|---------|----------------|
| **Claude Code (official)** | `/plugin install superpowers@claude-plugins-official` |
| **Claude Code (Superpowers Marketplace)** | `/plugin marketplace add obra/superpowers-marketplace` → install |
| **OpenAI Codex CLI** | `/plugins` → search "superpowers" → install |
| **OpenAI Codex App** | UI: Plugins sidebar → Coding section → `+` next to Superpowers |
| **Cursor** | `/add-plugin superpowers` trong Cursor Agent chat |
| **OpenCode** | Tell OpenCode to fetch `.opencode/INSTALL.md` |
| **GitHub Copilot CLI** | `copilot plugin marketplace add obra/superpowers-marketplace` → install |
| **Gemini CLI** | `gemini extensions install https://github.com/obra/superpowers` |

> **Note:** Available trên Anthropic's **official** Claude plugin marketplace — không phải self-hosted only như ECC initial. Anthropic đã endorse.

→ Detail trong [[(C) Distribution Model]] entity page.

---

## Distinctive features khác ECC

### 1. "Your human partner" terminology
Throughout skills, agent gọi user là "your human partner" — không "the user", không "you". Per CLAUDE.md là **deliberate, không interchangeable**.

### 2. Hard gates trong skills
Skill `brainstorming` có `<HARD-GATE>` block: "Do NOT invoke any implementation skill, write any code, scaffold any project, or take any implementation action until you have presented a design and the user has approved it."

→ Stricter enforcement than ECC's "best practice" tone.

### 3. Anti-pattern recognition tables
Skills có sections **"Common Rationalizations"** + **"Red Flags - STOP and Start Over"** liệt kê 11+ excuses + 13+ red flag patterns. Agent học recognize own rationalization.

### 4. "Iron Law" framing
TDD skill: *"NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"* — Iron Law. *"Write code before the test? Delete it. Start over."*

→ ECC: best-practice rules. Superpowers: iron laws.

### 5. Single agent (code-reviewer)
Chỉ 1 agent file (`agents/code-reviewer.md`). Mọi specialized work qua **skills auto-trigger** — không cần per-language reviewer agents như ECC (typescript-reviewer, go-reviewer, etc.).

→ Different design philosophy: methodology > tool count.

### 6. "94% PR rejection rate" public stance
CLAUDE.md mở đầu warning AI agents về reject rate. **Sets the bar for contribution quality** explicitly.

### 7. Zero-dependency by design
"Superpowers is a zero-dependency plugin by design." Bất kỳ change nào require external tool/service → reject.

→ ECC: tích hợp ECC Tools (separate paid product), AgentShield, etc.

---

## Sự kiện cộng đồng / Community

- **Discord:** [discord.gg/35wsABTejz](https://discord.gg/35wsABTejz)
- **Issues:** github.com/obra/superpowers/issues
- **Release announcements:** primeradiant.com/superpowers/
- **Origin blog:** blog.fsck.com/2025/10/09/superpowers/ (Oct 2025 launch)

---

## Câu hỏi đã giải / Resolved

- ✅ Q3 7-stage workflow exact stages (đầy đủ tên + skill tương ứng)
- ✅ Q4 Skills count (14 verified, vs ECC 185 — quality-over-quantity)
- ✅ Q5 TDD enforcement (Iron Law framing với "delete code, start over")
- ✅ Q6 Subagent count (1 agent only, methodology-driven)
- ✅ Q7 Claude marketplace (official, claude.com/plugins/superpowers)
- ✅ Q8 Author Jesse Vincent at Prime Radiant, blog.fsck.com

---

## Câu hỏi mới từ ingest này

1. ⏸ **GitHub stars count** — README không show badges như ECC. Cần check repo page.
2. ⏸ **Eval evidence** — CLAUDE.md mention "extensive eval" cho skills. Format/methodology cụ thể như thế nào? **→ skill `writing-skills` có cover.**
3. ⏸ **`docs/superpowers/` folder** — README mention save design doc trong `docs/superpowers/specs/` nhưng folder chỉ có 3 subfolders (plans/, superpowers/, windows/). Convention vs example folder?
4. ⏸ **`subagent-driven-development` two-stage review chi tiết** — README mention nhưng chưa explain stages. **→ đọc skill file.**
5. ⏸ **`primeradiant.com`** — startup của Jesse Vincent, có related products commercial không? Independence vs commercial backing?
6. ⏸ **Why 1 agent only?** — design decision quan trọng. Agent vs skill philosophy của Superpowers.
7. ⏸ **`session-start` hook** — load gì vào context? **→ đọc hook script.**

---

## Connection to Storm Bear vault

**Pattern matches LLM Wiki principle:**

- Methodology-driven approach (Superpowers' bias) ↔ LLM Wiki maintainer pattern (Karpathy)
- "Step back before action" ↔ Plan Mode trong Claude Code
- "Mandatory workflows, not suggestions" ↔ vault rule "always end with suggested next action"
- Quality > quantity ↔ vault rule "NEVER fabricate, ASK if unclear"

**Áp dụng cho Storm Bear team:**
- Adopt "your human partner" terminology trong vault skills?
- Apply "Iron Law" framing cho mandatory rules?
- Eval skills trước khi modify (skill `writing-skills` pattern)?

---

## Cross-references

- [[(C) index]] — main catalog
- [[(C) log]] — activity log
- [[../01 Analysis/(C) open questions]] — open questions tracking
- _Sẽ link tới_ [[(C) The 7-Stage Workflow]] khi entity page tạo
- _Sẽ link tới_ [[(C) Skills Library]] khi entity page tạo
- _Sẽ link tới_ [[(C) Distribution Model]] khi entity page tạo

## Citations

- `README.md`, lines 1–199 (full file)
- Cross-loaded: repo's CLAUDE.md (auto-loaded khi đọc) — contributor guidelines, 94% PR rejection context
