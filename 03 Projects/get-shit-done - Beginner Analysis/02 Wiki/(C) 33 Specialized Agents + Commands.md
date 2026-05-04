# (C) 33 Specialized Agents + 83 Commands

> **Source:** `agents/` folder listing (33 files), `commands/gsd/` folder (83 files), docs/AGENTS.md (21 categorized)
> **Ingested:** 2026-04-18
> **Type:** Entity page (building block) — entity #3 cho GSD

---

## One-liner

**VI:** GSD có **largest agent + command library của 4 Tier 1 frameworks** — 33 agents (agents/gsd-*.md) + 83 slash commands (commands/gsd/*.md) + 11 hooks. Structured theo **thin orchestrator pattern**: workflow commands spawn specialized agents, agents produce artifacts, orchestrator integrates. 33 folder agents vs 21 categorized in docs = **docs lag behind code** (discrepancy worth noting).

**EN:** GSD has largest library of Tier 1 frameworks: 33 agents + 83 commands + 11 hooks. Thin orchestrator pattern. Docs list 21 agents; folder has 33 (lag).

---

## Khi nào dùng concept này

**Hữu ích khi:**
- Navigate GSD's 83 commands (overwhelming at first)
- Understand agent specialization logic (why 33?)
- Compare scope với sibling frameworks (ECC 185+48, Superpowers 14+1, gstack 23+8+1)
- Debug "which agent runs when"

**Không cần memorize all 83 commands** — `/gsd-next` auto-routes + `/gsd-help` lists.

---

## Comparison sibling

| Axis | ECC | Superpowers | gstack | **GSD** |
|------|-----|-------------|--------|---------|
| Skills/Commands | 185 skills + 79 commands (legacy) | 14 skills | 23 specialists + 8 power tools | **83 slash commands** |
| Agents | 48 specialized | 1 (code-reviewer) + dynamic spawn | 23 role-based (same as commands) | **33 specialized** |
| Hooks | 8 standard | 1 SessionStart | None public | **11 custom (.js/.sh)** |
| Naming prefix | N/A | N/A | `/` (or `/gstack-`) | **`/gsd-`** (always) |
| Agent categorization | Domain (security, DB, frontend) | Function (implementer/reviewer) | Role (CEO, QA, CSO) | **Function (researcher/planner/executor/checker)** |
| Discrepancy | N/A | N/A | N/A | **docs 21 / folder 33 (12+ lag)** |

→ **GSD most explicit about agent specialization.** 33 functions = 33 agents.

---

## Sub-types: 33 agents by category (from folder)

### Researchers (5, docs says 3)

| Agent | Purpose |
|-------|---------|
| `gsd-project-researcher` | Investigates project domain |
| `gsd-phase-researcher` | Investigates phase-specific patterns |
| `gsd-ui-researcher` | UI/frontend investigation |
| `gsd-domain-researcher` | **[in folder, not in docs]** Generic domain research |
| `gsd-ai-researcher` | **[in folder, not in docs]** AI/ML research |

### Analyzers (3, docs says 2)

| Agent | Purpose |
|-------|---------|
| `gsd-assumptions-analyzer` | Surfaces assumptions for validation |
| `gsd-advisor-researcher` | Advisor/consultant patterns |
| `gsd-pattern-mapper` | **[extra]** Pattern recognition across codebase |

### Synthesizers (2, docs says 1)

| Agent | Purpose |
|-------|---------|
| `gsd-research-synthesizer` | Merges 4-parallel-researcher output |
| `gsd-doc-synthesizer` | **[extra]** Synthesize docs for `/gsd-ingest-docs` |

### Planners + Roadmappers (2)

| Agent | Purpose |
|-------|---------|
| `gsd-planner` | Atomic XML plan generation |
| `gsd-roadmapper` | Phase → roadmap mapping |

### Executors (2, docs says 1)

| Agent | Purpose |
|-------|---------|
| `gsd-executor` | Wave-based plan execution |
| `gsd-code-fixer` | **[extra]** Targeted code fixes |

### Checkers + Verifiers + Auditors (8, docs says 7)

| Agent | Purpose |
|-------|---------|
| `gsd-plan-checker` | Validates plans against requirements |
| `gsd-integration-checker` | Checks integration correctness |
| `gsd-ui-checker` | UI checks |
| `gsd-verifier` | End-to-end verification |
| `gsd-nyquist-auditor` | **[named after Nyquist — likely quality sampling]** |
| `gsd-ui-auditor` | UI audits |
| `gsd-security-auditor` | Security audit |
| `gsd-eval-auditor` | **[extra]** Eval quality audit |
| `gsd-eval-planner` | **[extra]** Plan evals |
| `gsd-code-reviewer` | **[extra]** Code review |

### Mappers + Debuggers (3, docs says 2)

| Agent | Purpose |
|-------|---------|
| `gsd-codebase-mapper` | Analyze existing codebase structure |
| `gsd-debugger` | Systematic debugging |
| `gsd-debug-session-manager` | **[extra]** Long-running debug sessions |

### Doc Writers (3, docs says 2)

| Agent | Purpose |
|-------|---------|
| `gsd-doc-writer` | Generate docs |
| `gsd-doc-verifier` | Verify docs match code |
| `gsd-doc-classifier` | **[extra]** Classify docs for ingest |

### Profilers + Utilities (3, docs says 1)

| Agent | Purpose |
|-------|---------|
| `gsd-user-profiler` | Behavioral profile of developer |
| `gsd-framework-selector` | **[extra]** Choose framework for context |
| `gsd-intel-updater` | **[extra]** Update intel/knowledge |

**Total folder: 33.** **Total docs: 21.** **Extras: 12+.**

→ **Docs lag behind development.** Folder = source of truth.

---

## Sub-types: 83 commands by category

From README's Commands section (full list):

### Core Workflow (13)
`/gsd-new-project`, `/gsd-discuss-phase`, `/gsd-plan-phase`, `/gsd-execute-phase`, `/gsd-verify-work`, `/gsd-ship`, `/gsd-next`, `/gsd-fast`, `/gsd-audit-milestone`, `/gsd-complete-milestone`, `/gsd-new-milestone`, `/gsd-forensics`, `/gsd-milestone-summary`

### Workstreams (5)
`/gsd-workstreams` + subcommands

### Multi-Project Workspaces (3)
`/gsd-new-workspace`, `/gsd-list-workspaces`, `/gsd-remove-workspace`

### Spiking & Sketching (4)
`/gsd-spike`, `/gsd-sketch`, `/gsd-spike-wrap-up`, `/gsd-sketch-wrap-up`

### UI Design (2)
`/gsd-ui-phase`, `/gsd-ui-review`

### Navigation (6)
`/gsd-progress`, `/gsd-next`, `/gsd-help`, `/gsd-update`, `/gsd-join-discord`, `/gsd-manager`

### Brownfield (1)
`/gsd-map-codebase`

### Phase Management (5)
`/gsd-add-phase`, `/gsd-insert-phase`, `/gsd-remove-phase`, `/gsd-list-phase-assumptions`, `/gsd-plan-milestone-gaps`

### Session (3)
`/gsd-pause-work`, `/gsd-resume-work`, `/gsd-session-report`

### Code Quality (5)
`/gsd-review`, `/gsd-secure-phase`, `/gsd-pr-branch`, `/gsd-audit-uat`, `/gsd-docs-update`

### Backlog & Threads (4)
`/gsd-plant-seed`, `/gsd-add-backlog`, `/gsd-review-backlog`, `/gsd-thread`

### Utilities (10+)
`/gsd-settings`, `/gsd-set-profile`, `/gsd-add-todo`, `/gsd-check-todos`, `/gsd-debug`, `/gsd-do`, `/gsd-note`, `/gsd-quick`, `/gsd-health`, `/gsd-stats`, `/gsd-profile-user`

### Plus in folder (not in README — extras trong commands/gsd/)
- `/gsd-add-backlog.md`, `/gsd-add-phase.md`, `/gsd-add-tests.md`, `/gsd-add-todo.md`
- `/gsd-ai-integration-phase.md`, `/gsd-analyze-dependencies.md`, `/gsd-audit-fix.md`
- `/gsd-autonomous.md`, `/gsd-cleanup.md`, `/gsd-code-review-fix.md`, `/gsd-code-review.md`
- `/gsd-debug.md`, `/gsd-discuss-phase.md`, `/gsd-do.md`
- `/gsd-eval-review.md`, `/gsd-execute-phase.md`, `/gsd-explore.md`
- `/gsd-extract_learnings.md`, `/gsd-forensics.md`, `/gsd-from-gsd2.md` [migration command]
- `/gsd-graphify.md` [visualization?], `/gsd-help.md`, `/gsd-import.md` [import skills?]
- (full list = 83 .md files)

**Total commands:** ~83 based on folder count.

---

## Anatomy: Thin orchestrator pattern

```
User: /gsd-plan-phase 1
  ↓
commands/gsd/plan-phase.md (thin orchestrator)
  ↓ spawns
  ├── agents/gsd-project-researcher (parallel)
  ├── agents/gsd-phase-researcher (parallel)
  ├── agents/gsd-ui-researcher (parallel)
  └── agents/gsd-domain-researcher (parallel)
  ↓ wait
  RESEARCH.md
  ↓
  agents/gsd-research-synthesizer
  ↓
  RESEARCH.md synthesized
  ↓
  agents/gsd-planner (reads PROJECT.md, REQUIREMENTS.md, CONTEXT.md, RESEARCH.md)
  ↓
  agents/gsd-plan-checker
  ↓ (loop until PASS)
  {phase_num}-{N}-PLAN.md
  ↓
  commands/gsd/plan-phase.md returns control to user
```

**Orchestrator responsibilities:**
- Spawn agents
- Wait for completion
- Integrate results (route to next agent)
- Never do heavy lifting itself

**Agent responsibilities:**
- Focused role
- Limited tool access
- Fresh context window (200k)
- Produce specific artifact

→ **Decoupled architecture.** Orchestrator changes don't break agents và vice versa.

---

## Cơ chế

### Mechanism 1: SKILL.md format per agent/command

Each file = Markdown với:
- YAML frontmatter (name, description, tool restrictions)
- Prose prompt (role, instructions)
- Examples (if applicable)

Match Anthropic skill format + siblings' conventions.

### Mechanism 2: Tool access restriction

Per docs/AGENTS.md: "Each agent has... limited tool access."

Examples (inferred):
- `gsd-planner` — Read + Write (no Bash/Exec)
- `gsd-executor` — all tools
- `gsd-verifier` — Read + Bash (run tests)
- `gsd-doc-writer` — Read + Write

→ **Principle of least privilege.** Security + safety.

### Mechanism 3: Fresh context per agent invocation

Orchestrator spawns each agent with fresh 200k tokens. Agents don't accumulate context between calls.

### Mechanism 4: Artifact hand-off

Agent N reads previous agents' artifacts from `.planning/`. Writes own artifact. Next agent reads.

No shared in-memory state. **Everything via files.**

### Mechanism 5: Agent size-budget (v1.37.0)

XL: 1600 lines, Large: 1000, Default: 500. Enforced in CI.

→ **Prompt-bloat prevention** at code-review stage.

### Mechanism 6: Shared boilerplate via references/

v1.37.0: "Mandatory-initial-read and project-skills-discovery logic extracted to reference files, reducing duplication across a dozen agents."

```
references/
├── mandatory-initial-read.md
├── project-skills-discovery.md
└── doc-conflict-engine.md (used by /gsd-ingest-docs + /gsd-import)
```

→ **DRY for agent prompts.** Match gstack's preamble-resolver + ETHOS injection.

### Mechanism 7: Orchestrator naming convention

Workflow commands in `commands/gsd/{action}.md` (kebab-case). Agents in `agents/gsd-{function}.md`. **Consistent naming** aids discovery.

---

## Out-of-box behavior

**Default install:**
- All 33 agents installed
- All 83 commands installed
- `/gsd-help` lists available
- `/gsd-next` auto-detects state
- Hooks active

**User doesn't pick agents.** Orchestrators choose per phase.

**Config via `/gsd-settings`:**
- Model profile (quality/balanced/budget/inherit) per agent
- Mode (yolo/interactive)
- Workflow toggles

---

## Configuration knobs

| Knob | Default | Effect |
|------|---------|--------|
| Model profile per agent | `balanced` | Override via `/gsd-set-profile` |
| Mode | `interactive` | `yolo` auto-approve everything |
| `workflow.discuss_mode` | `questions` | `assumptions` alternative |
| Size budgets | XL/Large/Default | Config override (inferred) |
| Hook activation | all 11 enabled | Disable via hooks config |

---

## Recipes

### Recipe 1: Debug which agent runs for command

```bash
/gsd-plan-phase 1 --verbose   # (inferred flag)
```

Or read `commands/gsd/plan-phase.md` directly — orchestrator lists spawned agents.

### Recipe 2: Override model per agent

```bash
/gsd-settings
# Select model per agent (quality profile for planner, balanced for researcher, budget for doc-writer)
```

### Recipe 3: Spawn agent directly (inferred)

```bash
# Not sure if user-facing — likely internal
Task tool → spawn gsd-debugger
```

→ Agents designed for orchestrator spawn, not direct user invocation. Debug via `/gsd-debug`.

### Recipe 4: Audit agent quality

```bash
/gsd-eval-review  # Runs gsd-eval-auditor on agent outputs
```

→ **Eval-driven improvement** built-in.

### Recipe 5: See all commands

```bash
/gsd-help   # Lists all 83
```

Or `ls commands/gsd/` in installed location.

### Recipe 6: Manage multiple phases concurrently

```bash
/gsd-manager   # Interactive command center for managing multiple phases
```

→ **Dashboard for long-running projects.**

---

## Advanced patterns

### Pattern 1: Function-named agents (not domain)

Agents named after function (researcher/planner/executor/verifier) vs ECC's domain (security/DB/frontend) vs gstack's role (CEO/QA/CSO).

→ **Generic functions** = work across domains. Trade-off: less domain-specific wisdom.

### Pattern 2: Explicit verifier/checker pairs

Plan phase has planner + plan-checker. Execute phase has executor + verifier. **Every producer has paired validator.**

→ **Convergent với Superpowers's 2-stage review pattern** (spec-reviewer + code-quality-reviewer).

### Pattern 3: 4-researcher parallelism

Fixed 4 researchers (stack/features/arch/pitfalls) per plan phase. **Opinionated decomposition.**

→ Prevents "researcher forgot to check pitfalls."

### Pattern 4: Agent proliferation via category extension

Core categories (researcher/analyzer/synthesizer/planner/checker/auditor/etc.) fixed. New agents = new instance of existing category.

Examples:
- `gsd-ai-researcher` = researcher category
- `gsd-eval-auditor` = auditor category

→ **Consistent organizational principle.** Easy to onboard new agents.

### Pattern 5: Nyquist audit (naming curiosity)

`gsd-nyquist-auditor` — named after Nyquist (signal processing)?

Possible meaning: audit quality at sampling rate sufficient to capture full signal.

→ **Technical naming.** Not obvious without context.

### Pattern 6: Shared conflict engine (v1.37.0 unreleased)

`references/doc-conflict-engine.md` used by both `/gsd-ingest-docs` và `/gsd-import`.

→ **DRY for logic**, not just prompts.

### Pattern 7: Hook layer separate từ agents

Hooks = runtime guards (.js/.sh). Agents = Claude-invoked. **Different execution contexts.**

Hooks:
- `gsd-check-update-worker.js`
- `gsd-context-monitor.js` ← context rot detection
- `gsd-phase-boundary.sh` ← lifecycle events
- `gsd-prompt-guard.js` ← prompt injection prevention
- `gsd-read-guard.js` ← read access control
- `gsd-read-injection-scanner.js` ← injection scanning
- `gsd-session-state.sh` ← session tracking
- `gsd-statusline.js` ← status display
- `gsd-validate-commit.sh` ← commit validation
- `gsd-workflow-guard.js` ← workflow integrity

→ **Most hooks của 4 Tier 1 frameworks.** Defensive by design.

---

## Combination với building blocks khác

### + 5-Step Workflow
Workflow commands spawn agents per step. Agent proliferation = workflow richness.

### + Context Rot Solution
Each agent fresh 200k context. Workflow orchestrator stays light.

### + 14 Harnesses
All 33 agents + 83 commands install to all 14 harnesses. Command/agent files same format.

### + Hooks
Hooks run at lifecycle boundaries (pre-tool-use, session-start, etc.). Defensive layer.

### Cross-project: + ECC 48 specialized agents
**Different taxonomy:**
- ECC: domain (security, DB, frontend) — where the work is
- GSD: function (researcher, planner, executor) — what the work is

Both valid. Different decompositions.

### Cross-project: + Superpowers SDD
Superpowers has 1 pre-built agent + dynamic spawn. GSD has 33 pre-built + dynamic via orchestrator.

→ Trade-off: GSD upfront investment (more agents) vs Superpowers runtime flexibility.

### Cross-project: + gstack 23 specialists
Similar role-based taxonomy. gstack's "specialists" = GSD's "agents." Different count (23 vs 33), different naming (role vs function).

---

## Anti-patterns

❌ **Invoke agent directly** — orchestrator spawn, not user call. Use `/gsd-debug` for debugging, không spawn `gsd-debugger` directly.

❌ **Edit installed agent files** — will be overwritten on `/gsd-update`. Fork repo if customization needed.

❌ **Confuse agents với commands** — agents = subagents spawned; commands = orchestrators.

❌ **Exceed agent size budget** — CI rejects. Extract shared refs first.

❌ **Skip specialized agent cho generic** — using `gsd-executor` cho debug task vs `gsd-debugger` = suboptimal.

❌ **Ignore 12+ folder extras** — docs lag, but agents are real + callable. Source = folder.

❌ **Disable hooks** — especially `gsd-context-monitor.js` + `gsd-workflow-guard.js`. Core defensive layers.

---

## Cross-references

- [[(C) Context Rot Solution]]
- [[(C) 5-Step Workflow]]
- [[(C) 14-Harness npm Distribution]]
- [[(C) README summary]]
- [[(C) USER-GUIDE summary]]
- [[(C) ARCHITECTURE + CHANGELOG summary]]
- Cross-project: `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) Subagents.md`
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) Skills Library.md`
- Cross-project: `../../gstack - Beginner Analysis/02 Wiki/(C) Specialist Roles.md`

## Citations

- `agents/` folder listing (33 files, `gsd-*.md`)
- `commands/gsd/` folder (83 files, various)
- `hooks/` folder (11 files, .js + .sh)
- `docs/AGENTS.md` (21 categorized agents — subset)
- README.md lines 558-686 (Commands reference — partial list)
- CHANGELOG v1.37.0 (size budgets + shared boilerplate)

## TODO

- ⏸ Read each agent's SKILL.md YAML frontmatter — tool access lists
- ⏸ Verify all 83 command files match README table
- ⏸ Understand `gsd-nyquist-auditor` naming (Nyquist sampling theorem application?)
- ⏸ Compare GSD's function-taxonomy vs ECC's domain vs gstack's role — which more effective?
- ⏸ Map ECC's 48 agents against GSD's 33 — overlap %
