# (C) The 7-Stage Workflow — Entity Page

> **Type:** Building block #1 (core methodology) — **THE distinctive feature** của Superpowers
> **Status:** First entity page (Superpowers project)
> **Sources:** 4 — README, CLAUDE.md, brainstorming/SKILL.md, RELEASE-NOTES.md
> **Last updated:** 2026-04-18

---

## Một câu / One-liner

**VI:** 7-Stage Workflow là **methodology core** của Superpowers — sequence 7 stages bắt buộc từ idea → shipped code, mỗi stage có skill tương ứng auto-trigger. Khác ECC (per-task skills), Superpowers enforce **fixed sequential pipeline**: brainstorm → worktree → plan → execute → TDD → review → finish. *"Mandatory workflows, not suggestions."*

**EN:** The 7-Stage Workflow is **Superpowers' methodology core** — a mandatory sequence of 7 stages from idea → shipped code, each stage has an auto-triggering skill. Unlike ECC (per-task skills), Superpowers enforces a **fixed sequential pipeline**: brainstorm → worktree → plan → execute → TDD → review → finish.

---

## Khi nào dùng / Khi nào KHÔNG dùng

### ✅ Dùng workflow khi:
- Build new feature từ scratch (full pipeline)
- Significant refactoring (full pipeline)
- Bug fix với scope > 1 file (skip stage 1, start at stage 3 writing-plans)
- Cần ensure consistency cross-team (workflow standardize behavior)

### ❌ KHÔNG dùng workflow khi:
- Trivial change 1-line typo (overhead không justify)
- Throwaway prototype/spike (waiver per CLAUDE.md)
- Configuration-only change (ask human partner)
- Task explicitly waived bởi human partner

> **Iron Law variant:** *"Every project goes through this process. A todo list, a single-function utility, a config change — all of them. 'Simple' projects are where unexamined assumptions cause the most wasted work."* (từ brainstorming skill)

---

## 7-Stage Workflow vs sibling concepts

| Tiêu chí | 7-Stage Workflow (Superpowers) | Sequential Phases (ECC longform) | Free-form (default Claude) |
|----------|--------------------------------|----------------------------------|---------------------------|
| **Sequence** | Fixed 7 stages, mandatory order | 5 phases recommended | None — ad-hoc |
| **Trigger mechanism** | Skills auto-trigger via description | User invokes per phase | User direct request |
| **Enforcement** | Hard gates trong skills (can't skip) | Best practice, can skip | None |
| **Subagent involvement** | Stage 4 mandatory subagent (capable harness) | Phase per agent (planner/tdd-guide/code-reviewer) | Optional |
| **Output artifacts** | Spec doc + plan doc + commits | Files per phase (research-summary.md, plan.md, etc.) | None |
| **Time overhead** | High (full process even cho small task) | Medium | Zero |
| **Result quality** | Most consistent | High but variable | Lowest |
| **Best for** | Production code, team workflows | Single-dev high-stakes work | Quick experiments |

> **Quy tắc quyết định:** Need consistency + production quality → Superpowers 7-stage. Need flexibility + single-dev → ECC sequential. Need speed > quality → free-form.

---

## The 7 Stages (chi tiết)

### Stage 1: brainstorming

**Skill:** `brainstorming`

**Activates:** Before any code (description match: creating features, building components, adding functionality, modifying behavior)

**Output:** Design document at `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`

**Process (9 steps theo skill checklist):**
1. Explore project context (files, docs, recent commits)
2. Offer Visual Companion (nếu visual-heavy topic)
3. Ask clarifying questions — **one at a time**
4. Propose 2-3 approaches with trade-offs + recommendation
5. Present design in **sections scaled to complexity**
6. Write design doc + commit
7. Spec self-review (placeholders, contradictions, ambiguity, scope)
8. User reviews written spec
9. Transition to writing-plans

**Hard Gate:**
> ```
> <HARD-GATE>
> Do NOT invoke any implementation skill, write any code, scaffold any project,
> or take any implementation action until you have presented a design and the
> user has approved it.
> </HARD-GATE>
> ```

**Đặc điểm:** Socratic dialogue, 1 question per message, presents recommendation lead.

---

### Stage 2: using-git-worktrees

**Skill:** `using-git-worktrees`

**Activates:** After design approval

**Process:**
- Create isolated workspace on new branch
- Run project setup (deps, env)
- Verify clean test baseline (all tests pass)

**Why:** Isolate work-in-progress from main, parallel work safety, prevent accidental main commits.

**Connection to ECC:** Same git worktree pattern from longform guide ("Git worktrees for parallel instances"). **Convergent.**

---

### Stage 3: writing-plans

**Skill:** `writing-plans`

**Activates:** With approved design

**Output:** Implementation plan at `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`

**Plan format requirements:**
- **Bite-sized tasks** (2-5 phút each)
- Every task has:
  - Exact file paths
  - Complete code (not pseudo-code)
  - Verification steps
- Plan written cho audience: "enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing"

**Why this audience framing:** Forces explicit-everything. Plan robust to subagent execution without context.

**v5.0.4 update:** Single whole-plan review (not chunk-by-chunk), reduced max iterations 5→3.

**v5.0.6 update:** Replaced subagent review loop với inline self-review checklist (placeholder scan, internal consistency, scope check, ambiguity check). Saves ~25 phút overhead.

---

### Stage 4: subagent-driven-development OR executing-plans

**Skill:** `subagent-driven-development` (preferred) hoặc `executing-plans` (fallback)

**Activates:** After plan approved + user says "go"

**subagent-driven-development:**
- Dispatches **fresh subagent per task**
- **Two-stage review** per task:
  1. Spec compliance (does it match plan?)
  2. Code quality (clean, idiomatic, maintainable?)
- Continues until plan complete
- Implementer status protocol: DONE / DONE_WITH_CONCERNS / BLOCKED / NEEDS_CONTEXT

**executing-plans:**
- Batch execution với human checkpoints
- Used khi harness không có subagent capability (Gemini CLI fallback)

**v5.0.0 breaking change:** Subagent-driven mandatory trên capable harnesses. Removed user choice.

**Distinctive:** *"Claude can work autonomously for a couple hours at a time without deviating from the plan."*

→ Detail trong [[(C) Subagent-Driven Development]] entity page.

---

### Stage 5: test-driven-development

**Skill:** `test-driven-development`

**Activates:** During implementation (within Stage 4)

**Iron Law:**
```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

**RED-GREEN-REFACTOR cycle:**
1. **RED:** Write failing test (one minimal test, real code)
2. **Verify RED:** Watch it fail (mandatory — never skip)
3. **GREEN:** Write minimal code to pass
4. **Verify GREEN:** Watch it pass + other tests still pass
5. **REFACTOR:** Clean up, keep green

**Includes:**
- Testing anti-patterns reference (`@testing-anti-patterns.md`)
- Common Rationalizations table (11 excuses + counter-arguments)
- Red Flags table (13 patterns to STOP at)

**Embedded in Stage 4:** Each subagent task follows TDD.

---

### Stage 6: requesting-code-review

**Skill:** `requesting-code-review`

**Activates:** Between tasks

**Process:**
- Reviews against plan
- Reports issues by severity
- **Critical issues block progress**

**Single agent involved:** `code-reviewer` (only agent in `agents/`).

**Output:** Issue list categorized (critical/high/medium/low).

---

### Stage 7: finishing-a-development-branch

**Skill:** `finishing-a-development-branch`

**Activates:** When tasks complete

**Process:**
- Verifies all tests pass
- Presents options to human partner:
  - Merge to main
  - Open PR
  - Keep branch
  - Discard
- Cleans up worktree (Stage 2 reverse)

**Output:** Decision + cleanup. Branch lifecycle complete.

---

## Cơ chế / How It Works

```
User: "I need to add user authentication"
    ↓
Skills auto-detect "building something" via description matching
    ↓
HARD GATE engages: brainstorming skill fires
    ↓
Stage 1: brainstorming
  - Socratic questions
  - 2-3 approaches proposed
  - Design sections presented
  - User approves each section
  - Spec doc written + committed
  - Self-review
  - User reviews spec
    ↓
Stage 2: using-git-worktrees
  - Create branch + worktree
  - Project setup
  - Clean test baseline verified
    ↓
Stage 3: writing-plans
  - Bite-sized tasks (2-5 min each)
  - Exact paths + complete code
  - Plan doc written + committed
  - Inline self-review (~30s, catches 3-5 bugs)
    ↓
User: "go"
    ↓
Stage 4: subagent-driven-development
  - Dispatch fresh subagent per task
  - Stage 5 TDD enforced inside each task
  - Stage 6 code review per task (two-stage)
  - Status protocol: DONE/DONE_WITH_CONCERNS/BLOCKED/NEEDS_CONTEXT
  - Loop until plan complete
    ↓
Stage 7: finishing-a-development-branch
  - All tests pass verification
  - Present options (merge/PR/keep/discard)
  - Cleanup worktree
    ↓
Done — production code shipped
```

**Time:** Hours autonomous. README claims *"a couple hours at a time without deviating."*

---

## Skills auto-trigger mechanism

Mỗi skill có frontmatter `description` matched vào agent context:

```yaml
---
name: brainstorming
description: "You MUST use this before any creative work - creating features,
              building components, adding functionality, or modifying behavior.
              Explores user intent, requirements and design before implementation."
---
```

**Trigger keywords:**
- "MUST use" / "Must" — hard activation language
- "before any X" — pre-condition matching
- Action verbs (creating, building, adding, modifying) — intent matching

→ Agent reads description, auto-detects context, invokes skill. **Mandatory** because hard gates inside skill body block alternative paths.

---

## Configuration

### Override workflow (rare cases)

**Per CLAUDE.md instruction priority hierarchy (v5.0.0):**

1. **User's explicit instructions** (CLAUDE.md, AGENTS.md, direct requests) — highest
2. Superpowers skills — override default
3. Default system prompt — lowest

**Example override:**
> CLAUDE.md: "For this prototype, skip TDD and brainstorming. We're exploring."
> Result: Workflow respects user instruction, skips stages.

### Skip individual stages

- **Skip Stage 1 brainstorming:** human partner explicit waiver ("we already designed this")
- **Skip Stage 2 worktrees:** if work happens directly on existing branch
- **Skip Stage 4 subagent:** falls back to executing-plans nếu harness không support subagent (vd Gemini CLI)
- **Skip Stage 5 TDD:** human partner waiver cho throwaway prototype/generated code/config

### Disable workflow entirely

Uninstall Superpowers plugin. Skills không activate, agent reverts to default.

---

## Recipes

### Recipe 1: Standard new feature flow

```
User: "I want to add OAuth login"
→ Stage 1: brainstorming (Socratic, 5-15 min)
→ User approves design
→ Stage 2: git worktree (1 min)
→ Stage 3: writing-plans (5-10 min, bite-sized tasks)
→ User: "go"
→ Stage 4-6: SDD execution (autonomous, hours)
→ Stage 7: finishing (1-5 min, merge decision)
```

### Recipe 2: Bug fix flow (skip Stage 1)

```
User: "Bug: empty email accepted in form"
→ Stage 3: writing-plans (focused: 1 test + 1 fix)
→ User: "go"
→ Stage 5 TDD: write failing test reproducing bug
→ Apply fix until green
→ Stage 6: code review
→ Stage 7: finishing (often direct merge)
```

### Recipe 3: Refactor flow (full pipeline, no new feature)

```
User: "Refactor authentication module — too coupled"
→ Stage 1: brainstorming (architecture options)
→ Stage 2: worktree (isolated)
→ Stage 3: writing-plans (each refactor step bite-sized)
→ Stage 4 SDD with TDD enforced
→ Stage 6: thorough review (refactors high-risk for regressions)
→ Stage 7: finishing
```

### Recipe 4: Multi-subsystem project (decompose first)

Per brainstorming skill:
> "If the project is too large for a single spec, help the user decompose into sub-projects: what are the independent pieces, how do they relate, what order should they be built? Then brainstorm the first sub-project through the normal design flow."

```
User: "Build full SaaS platform with chat, billing, analytics"
→ Stage 1 (decompose): identify 3 sub-projects, dependency order
→ Each sub-project gets full Stage 1 → Stage 7 cycle
```

---

## Patterns kết hợp / Combination patterns

### Workflow + git worktree (parallel projects)

Multiple worktrees → multiple workflow instances in parallel. Each worktree = own branch + own workflow state. Per ECC pattern (longform), prevents conflicts.

### Workflow + dispatching-parallel-agents

Stage 4 SDD typically sequential (per task). Skill `dispatching-parallel-agents` enables concurrent subagents on **independent** tasks. Use khi tasks không có dependencies.

### Workflow + visual-companion (brainstorming)

Stage 1 có optional **Visual Companion** — browser-based companion server. Useful for:
- UI design questions
- Architecture diagrams
- Comparison tables
- Mockups review

**v5.0.2:** Zero-dependency Node.js server (custom WebSocket implementation).

---

## Anti-patterns / Sai lầm hay gặp

1. **Skip Stage 1 vì "task simple"** — per skill: "Simple projects are where unexamined assumptions cause the most wasted work."
2. **Skip Stage 5 TDD "just this once"** — Iron Law violation. Delete code, start over.
3. **Stage 3 plan có placeholders ("TBD", "similar to Task N")** — v5.0.6 added explicit "No Placeholders" section. Plans với placeholders fail review.
4. **Stage 4 dispatch subagents song song khi tasks dependent** — race conditions. Use `dispatching-parallel-agents` only when verified independent.
5. **Modify carefully-tuned skill content** (Red Flags tables, "your human partner" language) — per CLAUDE.md, requires extensive eval evidence. Not casual edit.
6. **Treat workflow as suggestions** — README explicit "Mandatory workflows, not suggestions." Hard gates enforce.
7. **Bypass HARD-GATE blocks** — XML tags trong skill body, designed non-bypassable. If you find a way to bypass, that's a skill bug.
8. **Stage 6 review without code reviewer agent** — agent có chuyên môn cho code review. Skipping = self-review only = blind spots.
9. **Stage 7 cleanup skipped** — leaves dangling worktrees, eats disk. `git worktree list` should be clean after Stage 7.
10. **Run workflow in shared env (not worktree)** — Stage 2 exists để isolate. Skipping = main branch pollution risk.

---

## Tools liên quan / Related Tools

| Tool | Purpose |
|------|---------|
| **Visual Companion server** | Browser-based UI cho Stage 1 brainstorming (optional) |
| `git worktree` | Stage 2 mechanism |
| Spec doc template | Stage 1 output structure |
| Plan doc template | Stage 3 output structure |
| `code-reviewer` agent | Stage 6 specialist (only agent in repo) |
| Skill auto-trigger via description | Workflow activation mechanism |
| Implementer status protocol (DONE/BLOCKED/etc.) | Stage 4 communication |

---

## Cross-references

- [[(C) Skills Library]] — 14 skills detail (workflow uses 7-9 of them)
- [[(C) Subagent-Driven Development]] — Stage 4 deep dive
- [[(C) Distribution Model]] — how workflow ships across 7 harnesses
- [[(C) README summary]] — workflow overview
- [[(C) Philosophy and Contribution Culture summary]] — Iron Law context
- [[(C) Release Notes overview]] — v5.0.0 breaking changes (subagent mandatory, batching removed)
- ECC sister: `03 Projects/Everything Claude Code - Beginner Analysis/02 Wiki/(C) Longform Guide summary.md` — Sequential Phases pattern
- [[(C) index]]

## Citations

- `00 Sources/superpowers/README.md`, lines 119–135 (workflow stages list)
- `00 Sources/superpowers/skills/brainstorming/SKILL.md`, lines 1–100 (Stage 1 detail)
- `00 Sources/superpowers/skills/test-driven-development/SKILL.md` (Stage 5 detail)
- `00 Sources/superpowers/RELEASE-NOTES.md`, v5.0.0 section (lines 203–294, breaking changes)
- `00 Sources/superpowers/RELEASE-NOTES.md`, v5.0.6 section (lines 16–40, review loop replacement)

---

## TODO cho lần ingest tiếp

- [ ] Đọc full skills cho Stage 2 (using-git-worktrees), Stage 3 (writing-plans), Stage 4 (subagent-driven-development), Stage 6 (requesting-code-review), Stage 7 (finishing-a-development-branch)
- [ ] Check `docs/superpowers/specs/` và `docs/superpowers/plans/` folders cho example designs/plans
- [ ] Verify Visual Companion server actual UX với screenshot
- [ ] Eval evidence (5 versions × 5 trials methodology) — find documented test setup
