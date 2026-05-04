# (C) 5-Step Workflow

> **Source:** README.md lines 264-470, USER-GUIDE.md lifecycle diagram
> **Ingested:** 2026-04-18
> **Type:** Entity page (workflow concept) — building block #2 cho GSD

---

## One-liner

**VI:** 5-Step Workflow là **sprint backbone của GSD** — mỗi phase đi qua `discuss → plan → execute → verify → ship`, với wave-based parallel execution trong step 3 (execute). Distinctive feature: **`/gsd-next` auto-detects state và runs next step** — zero state-tracking burden on user. Convergent với Superpowers 7-stage và gstack Sprint Pipeline, nhưng narrower (5 vs 7) và more auto-routed.

**EN:** 5-Step Workflow is GSD's sprint backbone — discuss → plan → execute → verify → ship, với wave-based parallel execution. Distinctive: `/gsd-next` auto-detects next step. Convergent với Superpowers 7-stage + gstack Sprint Pipeline.

---

## Khi nào dùng concept này

**Hữu ích khi:**
- Hiểu phase-level workflow của GSD
- So sánh với Superpowers 7-stage + gstack Sprint Pipeline
- Chọn workflow framework cho new project
- Debug "where am I in the workflow" via `/gsd-progress`

**Không cần memorize** — `/gsd-next` handles transition cho bạn.

---

## Comparison sibling across Tier 1

| Axis | Superpowers 7-stage | gstack Sprint Pipeline | **GSD 5-Step** |
|------|---------------------|------------------------|----------------|
| Stages | 7 explicit | 7 conceptual (Think/Plan/Build/Review/Test/Ship/Reflect) | **5 (discuss/plan/execute/verify/ship)** |
| Enforcement | HARD-GATE XML | Smart routing via proactive suggestion | **`/gsd-next` auto-detect** |
| Skip granularity | Can't skip stages 1/5 | Smart-skip based on work type | **Skip any individual step** (per `--quick` mode) |
| Reflection phase | Manual iteration log | `/retro` built-in | **`/gsd-audit-milestone` + `/gsd-session-report`** |
| Parallelism | SDD subagents | Conductor external | **Wave execution built-in** |
| Auto-routing | Skill description matching | Stage-aware suggestions | **`/gsd-next` explicit command** |

→ **GSD most auto-routed.** User just says "next" → system knows.

---

## Sub-types: 5 steps detail

### Step 1: `/gsd-discuss-phase <N>`

**Purpose:** Capture implementation preferences BEFORE planning.

**What it does:**
- Analyzes phase, identifies gray areas:
  - Visual features → Layout, density, interactions, empty states
  - APIs/CLIs → Response format, flags, error handling, verbosity
  - Content systems → Structure, tone, depth, flow
  - Organization tasks → Grouping, naming, duplicates, exceptions
- Asks until satisfied per gray area
- Output: `{phase_num}-CONTEXT.md`

**Why first:** Roadmap has "sentence or two per phase." Not enough to build what *you* imagine. Discuss locks preferences.

**Mode options:**
- `questions` (default) — asks one-by-one
- `assumptions` — reads codebase, surfaces what it would do, asks corrections
- `--batch` — answer small grouped set at once
- `--chain` — auto-chains into plan+execute

**Creates:** `{phase_num}-CONTEXT.md` (feeds downstream steps)

### Step 2: `/gsd-plan-phase <N>`

**Purpose:** Research + atomic XML plans + verification.

**Inner flow (4 parallel researchers + planner + checker):**
```
/gsd-plan-phase N
  ↓
Phase Researcher (x4 parallel)
  ├── Stack researcher
  ├── Features researcher
  ├── Architecture researcher
  └── Pitfalls researcher
  ↓ (merged by research-synthesizer)
RESEARCH.md
  ↓
Planner ← reads PROJECT.md, REQUIREMENTS.md, CONTEXT.md, RESEARCH.md
  ↓
Creates 2-3 atomic task plans (XML structure)
  ↓
Plan Checker → PASS? (loop if fail)
  ↓
{phase_num}-{N}-PLAN.md
```

**Why 4 parallel researchers:** cover investigation axes without sequential blocking.

**`--reviews` flag:** loads codebase review findings từ `/gsd-review`.

**Creates:** `{phase_num}-RESEARCH.md`, `{phase_num}-{N}-PLAN.md`

### Step 3: `/gsd-execute-phase <N>`

**Purpose:** Wave-based parallel execution.

**Wave mechanism:**
```
┌─────────────────────────────────────────────────────┐
│  PHASE EXECUTION                                    │
│                                                     │
│  WAVE 1 (parallel)   →   WAVE 2 (parallel)   →  W3  │
│  Plan 01 | Plan 02       Plan 03 | Plan 04      P05 │
│                                                     │
│  Dependencies: Plan 03 needs Plan 01                │
│                Plan 04 needs Plan 02                │
│                Plan 05 needs Plans 03 + 04          │
└─────────────────────────────────────────────────────┘
```

**Rules:**
- Independent plans → same wave → parallel goroutines
- Dependent plans → later wave → wait
- File conflicts → sequential or same plan

**Key insight:** "Vertical slices" (Plan 01: User feature end-to-end) parallelize better than "horizontal layers" (Plan 01: All models).

**Per-plan context:**
- Fresh 200k tokens
- Isolated execution
- Zero accumulated garbage
- Atomic commit per task

**Creates:** `{phase_num}-{N}-SUMMARY.md`, `{phase_num}-VERIFICATION.md`

### Step 4: `/gsd-verify-work <N>`

**Purpose:** Manual UAT (User Acceptance Testing).

**What it does:**
1. Extracts testable deliverables (what you should be able to do now)
2. Walks you through one at a time ("Can you log in với email?" Yes/no, or describe what's wrong)
3. Diagnoses failures automatically (spawns debug agents → root cause)
4. Creates verified fix plans (ready for re-execution)

**If all pass:** move on.
**If failures:** run `/gsd-execute-phase` again with fix plans.

**Why manual step:** Automated tests check code exists + tests pass. User verifies **does feature work như expected.**

**Creates:** `{phase_num}-UAT.md`, fix plans if issues

### Step 5: `/gsd-ship <N>` (optional)

**Purpose:** Create PR from verified work.

**`--draft` flag:** creates draft PR.

**Generates:**
- Auto-filtered branch (excludes `.planning/` commits)
- PR body from phase summaries
- Task-level commit traceability

→ **Clean PR = task commits + feature commits, no .planning/ noise.**

**Alternative:** `/gsd-pr-branch` — just create clean branch, PR manually later.

---

## Auto-routing: `/gsd-next`

**Distinctive feature.** Instead of memorizing step sequence:

```bash
/gsd-next
```

**Auto-detects:**
- Are we mid-phase? → suggests next step in phase
- Phase done? → suggests new phase
- Milestone done? → suggests audit-milestone
- All done? → suggests new-milestone

→ **Zero workflow memorization.** User just says "next."

**Contrast với:**
- Superpowers: user explicitly invokes stage skill
- gstack: proactive skill suggestions + user invokes
- **GSD: explicit `/gsd-next` command = cleaner mental model**

---

## Anatomy: Full milestone loop

```
/gsd-new-project (or /gsd-new-milestone)
  ↓
FOR EACH PHASE:
  /gsd-discuss-phase N  →  CONTEXT.md
  /gsd-ui-phase N       →  UI-SPEC.md (frontend only)
  /gsd-plan-phase N     →  RESEARCH.md + PLAN.md files
  /gsd-execute-phase N  →  SUMMARY.md files
  /gsd-verify-work N    →  UAT.md
  /gsd-ship N           →  PR (optional)
  ↓
  Next phase? → loop
  ↓
/gsd-audit-milestone    → verify milestone DoD
/gsd-complete-milestone → archive + tag
  ↓
Another milestone? /gsd-new-milestone
```

→ **Match Superpowers 7-stage pattern + gstack Think/Plan/Build/Review/Test/Ship/Reflect.** Convergent.

---

## Quick Mode (bypass full flow)

```bash
/gsd-quick
> What do you want to do? "Add dark mode toggle to settings"
```

**Skip:**
- No research
- No plan checker
- No verifier (default)

**Flags (composable):**
- `--discuss` — lightweight gray-area surfacing
- `--research` — focused researcher
- `--validate` — plan-checking + post-exec verification
- `--full` — all phases (full GSD pipeline in quick-task form)

**Creates:** `.planning/quick/001-add-dark-mode-toggle/PLAN.md`, `SUMMARY.md`

→ **Match Superpowers's simple task path + gstack's `/fast`.** 5-step for serious work, quick for ad-hoc.

---

## Cơ chế

### Mechanism 1: Artifact hand-off

Each step produces artifacts consumed by next:
```
discuss → CONTEXT.md → plan reads CONTEXT.md
plan → PLAN.md → execute reads PLAN.md
execute → SUMMARY.md → verify reads SUMMARY.md
verify → UAT.md → ship reads UAT.md (if issues, execute reads fix plans)
```

→ **Match gstack's artifact-driven skill composition.** Same philosophy.

### Mechanism 2: `.planning/` namespace

All artifacts trong single folder → clean project root + easy gitignore + clear audit.

### Mechanism 3: Auto-detection via file system state

`/gsd-next` reads `.planning/STATE.md` + checks which artifacts exist → infers next step.

→ **File system as state machine.** Simpler than explicit state tracking.

### Mechanism 4: 4 parallel researchers

Plan phase spawns 4 researchers parallel (stack/features/arch/pitfalls). Research synthesizer merges. **Faster than sequential.**

### Mechanism 5: Wave grouping by dependency

Planner categorizes plans into dependency-ordered waves. Wave N+1 waits for Wave N. **Max parallelism within wave.**

### Mechanism 6: Fresh-context-per-executor

Each plan executor spawns fresh 200k context. Main session stays light.

### Mechanism 7: Per-task atomic commit

Every completed task = own git commit immediately. **Git bisect-friendly.**

---

## Out-of-box behavior

**Default:**
- Interactive mode (`mode: "interactive"` in config)
- Questions-based discuss (not assumptions)
- 4 parallel researchers per plan phase
- Wave execution with max parallelism
- Atomic commits per task
- Fresh context per executor

**First-run:**
```bash
npx get-shit-done-cc@latest
# pick runtime (claude/opencode/etc.)
# pick location (global/local)
# → installs `.planning/` or global skills dir
# → verify với /gsd-help
```

Then: `/gsd-new-project` to start first milestone.

---

## Configuration knobs

| Knob | Default | Effect |
|------|---------|--------|
| `mode` | `interactive` | vs `yolo` auto-approve |
| `workflow.discuss_mode` | `questions` | vs `assumptions` |
| Model profile | `balanced` | quality/balanced/budget/inherit |
| Wave parallelism | max | Limit if resource-bound |
| `--chain` flag | off | auto-chain discuss → plan → execute |
| `--batch` flag | off | group discussion questions |

---

## Recipes

### Recipe 1: First project end-to-end

```bash
/gsd-new-project   # Questions + research + requirements + roadmap
# Approve roadmap
/gsd-next          # Auto-routes to /gsd-discuss-phase 1
# Answer questions
/gsd-next          # Auto-routes to /gsd-plan-phase 1
# Approve plan
/gsd-next          # Auto-routes to /gsd-execute-phase 1
# Walk away, come back later
/gsd-next          # Auto-routes to /gsd-verify-work 1
# UAT
/gsd-next          # Auto-routes to /gsd-ship 1 or next phase
```

### Recipe 2: Chained execution (skip between prompts)

```bash
/gsd-discuss-phase 1 --chain
# → auto-chains to plan + execute without stopping
```

Good cho trusted phases where user approves up-front.

### Recipe 3: Brownfield (existing codebase)

```bash
/gsd-map-codebase   # Analyze existing stack + conventions
/gsd-new-project    # Questions focused on what's being added
# Planner now knows your patterns
```

→ Avoids "AI ignoring your conventions."

### Recipe 4: Quick ad-hoc task

```bash
/gsd-quick --discuss --research
> "Add a dark mode toggle to settings"
```

5-step pipeline compressed to ~2-step for small tasks.

### Recipe 5: Milestone recovery

```bash
/gsd-forensics     # Diagnose stuck workflow
/gsd-health --repair  # Auto-repair .planning/ integrity
/gsd-resume-work   # If session paused
```

### Recipe 6: Pause + resume across machines

```bash
# Laptop
/gsd-pause-work    # Creates HANDOFF.json
git commit + push

# Desktop (after pull)
/gsd-resume-work   # Restores state
```

---

## Advanced patterns

### Pattern 1: Auto-detection via file system state

`/gsd-next` reads `.planning/` to infer state. No explicit state machine. **Simpler maintenance.**

### Pattern 2: Artifact-driven stage composition

Each step produces known output → next step input. **Loose coupling.**

→ Reusable cho Storm Bear vault routine (already partially applied: source summaries → entity pages → published).

### Pattern 3: Wave-based dependency resolution

DAG scheduler groups independent nodes into parallel waves. **Better than "process queue sequentially" or "pure parallel without order."**

### Pattern 4: 4 research axes fixed (not configurable)

Stack + Features + Architecture + Pitfalls. **Opinionated.**

→ Ensures balanced research. User can't skip "pitfalls" to save time → rot prevention.

### Pattern 5: Modular phase management

- Add phase to current milestone
- Insert urgent work between phases
- Adjust plans without rebuilding

→ **Adapts to reality.** Plans can change without starting over.

### Pattern 6: Quick mode = 5-step compressed

Same agents, skip optional steps. **Not separate code path.** Reduces maintenance.

---

## Combination với building blocks khác

### + Context Rot Solution
5-step workflow = operationalizes context rot prevention. Each step fresh subagent + artifact hand-off.

### + 33 Specialized Agents
Workflow orchestrators spawn specialized agents per step. Planner, executor, verifier are agents.

### + 14 Harnesses
Workflow portable cross-harness. Commands map to each harness's invocation syntax.

### + Hooks
- `gsd-phase-boundary.sh` — boundary events
- `gsd-workflow-guard.js` — prevents invalid transitions
- `gsd-session-state.sh` — tracks session state

### Cross-project: + Superpowers 7-stage
Same concept, different granularity:
- Superpowers: 7 stages với HARD-GATE XML (brainstorming → finishing-a-development-branch)
- GSD: 5 steps với `/gsd-next` auto-routing

Both enforce sequence. GSD friendlier UX.

### Cross-project: + gstack Sprint Pipeline
Same 5-7 concept, different implementation:
- gstack: proactive skill suggestions + smart routing
- GSD: explicit `/gsd-next` command

Both hide complexity. Different affordances.

### Cross-project: + goclaw 8-stage agent loop
**Different abstraction layer.** goclaw's = internal agent execution (Context/Think/Tool/Observe per LLM call). GSD = developer workflow (phase-level). Orthogonal.

---

## Anti-patterns

❌ **Skip `/gsd-discuss-phase`** — "Just plan" = generic defaults. Your vision not captured.

❌ **Use `/gsd-quick` for real work** — quick mode skips verifier. Production = `/gsd-quick --full` or full flow.

❌ **Force `--chain` on unfamiliar phases** — auto-chain works for well-understood work. New domain = pause between steps.

❌ **Bypass wave execution** — running plans sequentially wastes parallelism. Trust waves.

❌ **Skip atomic commits** — `--no-commit` flag exists (inferred) but violates git bisect-ability.

❌ **Ignore `/gsd-next` → manual commands** — auto-detect is feature. Manual = error-prone.

❌ **Run multiple phases parallel** — workstreams for that. Don't run 2 phases in 1 milestone concurrently without workstream namespace.

---

## Cross-references

- [[(C) Context Rot Solution]] — why workflow exists
- [[(C) 33 Specialized Agents + Commands]] — workflow agents
- [[(C) 14-Harness npm Distribution]]
- [[(C) README summary]]
- [[(C) USER-GUIDE summary]] — lifecycle diagrams
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) The 7-Stage Workflow.md`
- Cross-project: `../../gstack - Beginner Analysis/02 Wiki/(C) Sprint Pipeline.md`

## Citations

- README.md lines 264-470 (full workflow description + wave diagram)
- README.md lines 440-470 (`/gsd-quick` mode)
- USER-GUIDE.md lines 23-180 (workflow diagrams)

## TODO

- ⏸ Deep-read USER-GUIDE sections 183-612 (UI Design Contract, Spiking, Security, Command Reference detail)
- ⏸ Verify `/gsd-next` auto-detection logic (what files does it read?)
- ⏸ Document failure paths: what if `/gsd-plan-phase` plan-checker loops infinitely?
- ⏸ Compare `.planning/STATE.md` với Superpowers's iteration log + gstack's `/learn`
