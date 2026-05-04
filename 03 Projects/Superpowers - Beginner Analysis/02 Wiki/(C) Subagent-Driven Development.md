# (C) Subagent-Driven Development (SDD) — Entity Page

> **Type:** Building block #3 (Stage 4 execution mechanism) — **THE distinctive execution pattern** của Superpowers
> **Status:** Third entity page
> **Sources:** 5 — README, RELEASE-NOTES.md (v5.0.0 + v5.0.6), subagent-driven-development/SKILL.md (head + structure), 3 prompt files
> **Last updated:** 2026-04-18

---

## Một câu / One-liner

**VI:** SDD là **execution pattern Stage 4** của 7-stage workflow — dispatch **fresh subagent per task** với isolated context + **two-stage review per task** (spec compliance → code quality). Loại context pollution, autonomous "vài giờ liền không deviate," structured status protocol (DONE/DONE_WITH_CONCERNS/BLOCKED/NEEDS_CONTEXT). Khác ECC's "Iterative Retrieval" pattern — **đây là per-task delegation pattern** focused execution.

**EN:** SDD is Superpowers' Stage 4 execution mechanism — dispatches a fresh subagent per task with isolated context + two-stage review per task. Eliminates context pollution, autonomous for hours, structured status protocol.

---

## Khi nào dùng / Khi nào KHÔNG dùng

### ✅ Dùng SDD khi:
- Có **implementation plan** từ Stage 3 writing-plans
- Tasks **mostly independent** (decomposed in plan)
- Want **stay in current session** (no context switch)
- Harness có **subagent capability** (Claude Code, Codex)
- Want **fast iteration** (no human-in-loop between tasks)

### ❌ KHÔNG dùng SDD khi:
- Tasks **tightly coupled** — sequential dependencies, breaks SDD parallelism
- Cần **parallel session** (use `executing-plans` instead)
- Harness **không support subagent** (Gemini CLI fallback to executing-plans)
- Cần **human checkpoint** giữa tasks (use executing-plans batch mode)
- No plan yet (back to Stage 3 writing-plans)

> **Per skill decision diagram:**
> ```
> Have plan? → Tasks independent? → Stay in session? → SDD
>                                  → No → executing-plans (parallel session)
>                  → No → Manual or brainstorm first
> ```

---

## SDD vs sibling concepts (chọn cái nào?)

| Tiêu chí | SDD (Superpowers) | executing-plans (Superpowers fallback) | Iterative Retrieval (ECC) | Sequential Phases (ECC) |
|----------|-------------------|----------------------------------------|---------------------------|-------------------------|
| **Mechanism** | Per-task subagent + 2-stage review | Batch + checkpoints | Per-query subagent + follow-up loop | Per-phase subagent + file handoff |
| **Granularity** | Per task (2-5 min each) | Batch (3 tasks then stop) | Per query | Per phase (5 phases) |
| **Review** | 2 stages per task (spec then quality) | At checkpoints | Within retrieval loop | At phase boundary |
| **Status protocol** | Structured (DONE/BLOCKED/etc.) | Free-form | Free-form | Free-form |
| **Parallel?** | Sequential default; can use dispatching-parallel-agents | Sequential | Single subagent | Sequential |
| **Context isolation** | ✅ Fresh per task | Same session | ✅ Per query | ✅ Per phase |
| **Best for** | Production tasks decomposed in plan | Parallel session work | Exploration/research | Multi-phase deep work |
| **Token cost** | Higher (per task overhead) | Medium | Medium | Higher (multi-phase) |

> **Quy tắc quyết định:**
> - Plan có independent tasks + want autonomy → SDD
> - Need human-in-loop giữa tasks → executing-plans
> - Exploration, không có plan → ECC's Iterative Retrieval
> - Multi-phase deep work → ECC's Sequential Phases

---

## Sub-types: 3 sub-prompts trong SDD

SDD skill folder có **4 files** — SKILL.md + 3 supporting prompts:

| File | Size | Purpose |
|------|------|---------|
| `SKILL.md` | 11.9KB | Main SDD workflow, decision diagrams, status protocol |
| `implementer-prompt.md` | 4.2KB | Prompt cho implementer subagent (per task) |
| `spec-reviewer-prompt.md` | 2.0KB | Prompt cho Stage 1 review subagent (spec compliance) |
| `code-quality-reviewer-prompt.md` | 1.1KB | Prompt cho Stage 2 review subagent (code quality) |

**Per-task pipeline:**
1. **Implementer** subagent (uses `implementer-prompt.md`) — does the work
2. **Spec reviewer** subagent (uses `spec-reviewer-prompt.md`) — checks spec compliance
3. **Code quality reviewer** subagent (uses `code-quality-reviewer-prompt.md`) — checks code quality

→ **3 subagents per task.** High overhead but high confidence.

---

## Anatomy: Implementer prompt structure (concrete)

Implementer prompt đóng vai trò "frame" cho subagent's whole behavior:

**Likely sections (per common pattern + 4.2KB size):**
- Identity ("You are an implementer...")
- Task description (passed in)
- Plan reference (passed in)
- Quality requirements
- TDD enforcement reminder (Iron Law)
- Status protocol explanation:
  - `DONE` — task complete, all tests pass
  - `DONE_WITH_CONCERNS` — done but flagged issues
  - `BLOCKED` — can't proceed, need help
  - `NEEDS_CONTEXT` — missing info to complete
- Code organization reminder (file structure follow)
- Escalation guidance: "When You're in Over Your Head"

**v5.0.0 added (per RELEASE-NOTES):**
> "Implementer status protocol — Subagents now report DONE, DONE_WITH_CONCERNS, BLOCKED, or NEEDS_CONTEXT. Controller handles each status appropriately: re-dispatching with more context, upgrading model capability, breaking tasks apart, or escalating to human"

---

## Cơ chế / How It Works

### Full per-task cycle

```
Task N (from plan)
    ↓
Controller (main agent) constructs context for implementer:
  - Task description (exact text từ plan)
  - File paths (from plan)
  - Spec doc reference (from Stage 1)
  - Plan doc reference (from Stage 3)
  - NO main session history (isolation)
    ↓
Dispatch implementer subagent (uses implementer-prompt.md)
    ↓
Implementer asks clarifying questions? (per skill diagram)
  Yes → Controller answers, provides context
  No → proceed
    ↓
Implementer follows TDD (Stage 5) — RED-GREEN-REFACTOR
    ↓
Implementer reports status:
  - DONE → proceed to review
  - DONE_WITH_CONCERNS → proceed but flag
  - BLOCKED → controller decides: re-dispatch / upgrade model / break task / escalate
  - NEEDS_CONTEXT → controller provides more context, retry
    ↓
Stage 1 Review: Dispatch spec-reviewer subagent
  - Question: Does code match plan?
  - Pass → proceed
  - Fail → re-dispatch implementer with feedback
    ↓
Stage 2 Review: Dispatch code-quality-reviewer subagent
  - Question: Is code well-organized? Architecture sound? Files growing?
  - Pass → mark task complete, move to Task N+1
  - Fail → re-dispatch implementer with feedback
    ↓
Loop until plan complete OR human escalation
```

### Why "Two-stage review" (not single)

**Lesson từ v5.0.0 + practical reasoning:**
- **Stage 1 (spec compliance):** Did you do what the plan said? — **Cheap to check**, fast feedback
- **Stage 2 (code quality):** Is what you did good? — **More expensive**, only invest if Stage 1 passes

→ Sequential filtering. Fail fast on spec compliance.

### Context isolation enforcement

**Per v5.0.2 cross-skill principle (RELEASE-NOTES):**
> "All delegation skills... now include context isolation principle. Subagents receive only the context they need, preventing context window pollution."

**SDD specific:**
> "You delegate tasks to specialized agents with **isolated context**. By precisely crafting their instructions and context, you ensure they stay focused and succeed at their task. They should never inherit your session's context or history — you construct exactly what they need. This also preserves your own context for coordination work."

→ **Controller's context preserved** for coordination. Subagents work blind to main conversation.

### Model selection per task type (v5.0.0)

> "Model selection — Guidance for choosing model capability by task type: cheap models for mechanical implementation, standard for integration, capable for architecture and review"

**Pattern:**
- Mechanical implementation (CRUD, simple parsing) → cheap model (Haiku)
- Integration tasks (connecting modules) → standard (Sonnet)
- Architecture decisions, complex review → capable (Opus)

→ Match ECC's model selection table from longform.

---

## Configuration

### Mandatory vs optional (v5.0.0)

**v5.0.0 breaking change:**
> "Subagent-driven development mandatory on capable harnesses. Writing-plans no longer offers a choice between subagent-driven and executing-plans."

**Capable harnesses** (SDD mandatory):
- Claude Code
- Codex (App + CLI)

**Non-capable harnesses** (executing-plans fallback):
- Gemini CLI (no subagent support)
- Limited harnesses

### v5.0.5 partial restoration

> "Execution handoff — restore user choice between subagent-driven and inline execution after plan writing. Subagent-driven is recommended but no longer mandatory."

→ Partial walkback. User can choose, but SDD recommended.

### Customize prompts

Prompts in `subagent-driven-development/` folder. Editing them changes subagent behavior. **Per CLAUDE.md, modifications need eval evidence** — these are carefully-tuned.

---

## Recipes

### Recipe 1: Standard SDD execution

```
[Stage 3 writing-plans complete, plan saved to docs/superpowers/plans/...]

User: "go"

Controller: SDD activates
  Task 1 → dispatch implementer → review spec → review quality → mark done
  Task 2 → ... (autonomous)
  Task 3 → ... (autonomous)
  ...
  Task N → all done

Controller: "All tasks complete, [test results]. Proceed to Stage 7 finishing?"
```

**Time:** Hours (per README claim "couple hours autonomous").

### Recipe 2: SDD with BLOCKED status

```
Implementer: BLOCKED — "Schema doesn't match what plan describes"

Controller decides:
  Option A: Re-dispatch with more context (likely fix)
  Option B: Upgrade model (Sonnet → Opus)
  Option C: Break task apart
  Option D: Escalate to human partner

Controller picks based on context, retries.
```

### Recipe 3: SDD with parallel agents (advanced)

For independent tasks, combine SDD với `dispatching-parallel-agents` skill:

```
Plan has Task 4 + Task 5 + Task 6 — all independent
Use dispatching-parallel-agents to run 3 implementers concurrently
Each follows SDD per-task pipeline
Results merged when all DONE
```

**Caveat:** Truly independent tasks only. Race conditions on shared files.

### Recipe 4: Override SDD cho specific task

```
User: "For Task 3, do it inline yourself — don't dispatch. I want to watch."

Controller: respects user instruction (priority hierarchy v5.0.0).
Inline execution Task 3, then resume SDD for Task 4+.
```

---

## Patterns kết hợp / Combination patterns

### SDD + TDD (mandatory pairing trong Stage 4)

Every implementer subagent follows TDD Iron Law. SDD provides task structure; TDD provides per-task discipline.

### SDD + dispatching-parallel-agents

Per pattern above — for independent tasks, parallelize SDD instances.

### SDD + code-reviewer agent

Stage 2 quality review CAN invoke `code-reviewer` agent for specialized review beyond skill defaults.

### SDD + status protocol → escalation

DONE_WITH_CONCERNS / BLOCKED → controller has structured handling. Combined với human partner contact when escalation needed.

### SDD + writing-plans

SDD requires plan từ Stage 3. Plan structure MUST follow writing-plans format (bite-sized 2-5 min tasks, exact paths, complete code) for SDD to work.

→ **Tight coupling Stage 3 ↔ Stage 4.** Bad plan = bad SDD execution.

---

## Anti-patterns / Sai lầm hay gặp

1. **Run SDD without plan** — no task structure, subagents flail. Always Stage 3 first.
2. **SDD on tightly coupled tasks** — sequential dependencies break parallelism. Use executing-plans batch instead.
3. **Skip Stage 2 quality review** — "spec passed = good enough." Wrong. Code quality issues compound.
4. **Modify implementer-prompt.md without eval** — carefully tuned for behavior. Need evidence per CLAUDE.md.
5. **Inherit main session context to subagent** — defeats isolation purpose. Construct minimal context only.
6. **Ignore BLOCKED status** — controller MUST handle. "Try again" without changing context = same block.
7. **Use SDD on Gemini CLI** — no subagent support. Falls back to executing-plans automatically; if forced, fails.
8. **Run parallel SDD on shared files** — race conditions. Verify true independence first.
9. **Skip DONE_WITH_CONCERNS** — concerns are signals, not noise. Address before next task.
10. **Try to monitor subagent's "thinking"** — defeats isolation. Trust output, not process.

---

## Comparison với ECC's "Iterative Retrieval" pattern

> Both patterns address sub-agent context problem. Different solutions.

| Aspect | SDD (Superpowers) | Iterative Retrieval (ECC) |
|--------|-------------------|---------------------------|
| **Use case** | Implementation per plan task | Information retrieval per query |
| **Subagent role** | Implementer (writes code) | Researcher (answers question) |
| **Context delivery** | Constructed minimal context | Query + objective context (purpose) |
| **Loop mechanism** | Status protocol (DONE/BLOCKED/etc.) | Follow-up questions (max 3 cycles) |
| **Review** | Two-stage (spec + quality) | None — orchestrator validates |
| **Output** | Code + status report | Summary |
| **Failure mode** | BLOCKED → controller decides | Insufficient → ask follow-up |
| **Best for** | Production code execution | Research, exploration |

> **Both are convergent solutions to "subagent has no context" problem. SDD = code execution focus; Iterative Retrieval = research focus.**

---

## Tools liên quan / Related Tools

| Tool | Purpose |
|------|---------|
| `implementer-prompt.md` | Subagent identity + task framing |
| `spec-reviewer-prompt.md` | Stage 1 review: spec compliance |
| `code-quality-reviewer-prompt.md` | Stage 2 review: code quality |
| `writing-plans` skill | Provides plan input |
| `test-driven-development` skill | Per-task discipline |
| `dispatching-parallel-agents` skill | For parallel SDD instances |
| `code-reviewer` agent | Available for Stage 2 escalation |
| Status protocol (DONE/etc.) | Communication contract |

---

## Cross-references

- [[(C) The 7-Stage Workflow]] — SDD is Stage 4 mechanism
- [[(C) Skills Library]] — SDD is one of 14 skills
- [[(C) Distribution Model]] — capable harness requirement
- [[(C) Philosophy and Contribution Culture summary]] — eval discipline cho prompt tuning
- [[(C) Release Notes overview]] — v5.0.0 mandatory + v5.0.5 partial restore + v5.0.6 review optimization
- ECC sister: `03 Projects/Everything Claude Code - Beginner Analysis/02 Wiki/(C) Subagents.md` — Iterative Retrieval pattern
- ECC sister: `03 Projects/Everything Claude Code - Beginner Analysis/02 Wiki/(C) Longform Guide summary.md` — Sequential Phases pattern
- [[(C) index]]

## Citations

- `00 Sources/superpowers/skills/subagent-driven-development/SKILL.md` (head + folder structure, 11.9KB total)
- `00 Sources/superpowers/skills/subagent-driven-development/implementer-prompt.md` (4.2KB, structure inferred)
- `00 Sources/superpowers/skills/subagent-driven-development/spec-reviewer-prompt.md` (2.0KB)
- `00 Sources/superpowers/skills/subagent-driven-development/code-quality-reviewer-prompt.md` (1.1KB)
- `00 Sources/superpowers/RELEASE-NOTES.md`, v5.0.0 (status protocol + model selection), v5.0.2 (context isolation), v5.0.5 (mandatory walkback), v5.0.6 (review optimization)
- `00 Sources/superpowers/README.md`, lines 13–15 ("autonomous couple hours" claim)

---

## TODO cho lần ingest tiếp

- [ ] Read full SDD/SKILL.md (11.9KB) for complete decision logic
- [ ] Read 3 prompt files in detail to verify status protocol implementation
- [ ] Find concrete example of SDD execution in docs/ folder
- [ ] Compare SDD per-task overhead numbers vs executing-plans batch (if benchmark exists)
- [ ] Verify Codex App SDD compatibility (v5.0.6 added design spec mention)
