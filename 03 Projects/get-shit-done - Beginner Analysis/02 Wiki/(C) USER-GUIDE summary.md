# (C) USER-GUIDE Summary

> **Source:** `00 Sources/get-shit-done/docs/USER-GUIDE.md` (1184 lines, ~50KB) — **skim-first** (section headers + 2-3 key sections full)
> **Ingested:** 2026-04-18
> **Routine context:** Source #2 of 3 (Phase 2)

---

## TL;DR

**VI:** USER-GUIDE cover: (1) **Full lifecycle workflow diagram** từ `/gsd-new-project` đến `/gsd-complete-milestone`; (2) **UI Design Contract** (6-pillar visual system); (3) **Spiking & Sketching** (throwaway experiments trước planning); (4) **Backlog & Threads** (persistent cross-session context); (5) **Workstreams** (parallel milestone work); (6) **Security** (threat-model-anchored enforcement); (7) **Edit Safety Rule** + **Git Commit Rules for Agents** (discipline). Structure matches README nhưng deeper detail.

**EN:** USER-GUIDE covers full lifecycle workflow, UI Design Contract, spiking+sketching, backlog+threads, workstreams, security, and agent discipline rules.

---

## 17 major sections

Per TOC:
1. **Workflow Diagrams** (line 23)
2. **UI Design Contract** (line 183)
3. **Spiking & Sketching** (line 263)
4. **Backlog & Threads** (line 316)
5. **Workstreams** (line 361)
6. **Security** (line 384)
7. **Code Review Workflow** (line 444)
8. **Exploration & Discovery** (line 481)
9. **Command Reference** (line 525)
10. **Configuration Reference** (line 612)
11. **Usage Examples** (line 744)
12. **Troubleshooting** (line 853)
13. **Edit Safety Rule** (line 878)
14. **Git Commit Rules for Agents** (line 1112)
15. **Recovery Quick Reference** (line 1124)
16. **Project File Structure** (line 1145)

→ **Most comprehensive USER-GUIDE của 5 projects.** 1184 lines vs Superpowers ~500, gstack similar.

---

## Full project lifecycle (ASCII diagram)

```
NEW PROJECT
/gsd-new-project (Questions → Research → Requirements → Roadmap)
  ↓
FOR EACH PHASE:
  /gsd-discuss-phase  (Lock preferences)
  /gsd-ui-phase       (Design contract, frontend only)
  /gsd-plan-phase     (Research + Plan + Verify)
  /gsd-execute-phase  (Parallel execution)
  /gsd-verify-work    (Manual UAT)
  /gsd-ship           (PR, optional)
  ↓
  Next Phase? Yes → loop | No ↓
  ↓
/gsd-audit-milestone
/gsd-complete-milestone
  ↓
Another milestone? Yes → /gsd-new-milestone | No → Done!
```

→ **Match Superpowers's 7-stage workflow + gstack's Sprint Pipeline.** Convergent "dev workflow" pattern across Tier 1.

---

## Planning Agent Coordination (diagram)

```
/gsd-plan-phase N
  │
  ├── Phase Researcher (x4 parallel)
  │     ├── Stack researcher
  │     ├── Features researcher
  │     ├── Architecture researcher
  │     └── Pitfalls researcher
  │           ↓
  │      RESEARCH.md
  │           ↓
  │      Planner  ← reads PROJECT.md, REQUIREMENTS.md, CONTEXT.md, RESEARCH.md
  │           ↓
  │      Plan Checker → PASS? (loop if fail)
```

**4 parallel researchers** = distinctive. Each specialized (stack/features/arch/pitfalls).

→ **Research depth > 3 siblings.** ECC/Superpowers/gstack don't explicitly parallel-research.

---

## UI Design Contract (`/gsd-ui-phase`)

**6-pillar visual audit system** (per `/gsd-ui-review`):
- (Inferred — full details in section line 183-262, not deep-read this session)

Creates `UI-SPEC.md` for frontend phases. Retroactive audit via `/gsd-ui-review`.

→ **Match gstack's `/plan-design-review` + `/design-review`.** Same concept, different namings.

---

## Spiking & Sketching (v1.37.0 highlight)

**`/gsd-spike [idea] [--quick]`** — throwaway experiments before planning
- Runs 2-5 focused experiments with Given/When/Then verdicts
- Stores in `.planning/spike-*/`

**`/gsd-sketch [idea] [--quick]`** — throwaway HTML mockups
- Generates 2-3 interactive HTML variants per design question
- Stores in `.planning/sketch-*/`

**Wrap-up commands package findings into project-local skills:**
- `/gsd-spike-wrap-up` → skill file for future build conversations
- `/gsd-sketch-wrap-up` → skill file for future builds

→ **Distinctive:** experiments BEFORE planning, packaged into skills AFTER. Match gstack's `/design-shotgun` concept, different mechanism.

---

## Backlog & Threads

**`/gsd-plant-seed <idea>`** — forward-looking ideas với **trigger conditions** — surface at right milestone

**`/gsd-add-backlog <desc>`** — parking lot with **999.x numbering** (outside active sequence)

**`/gsd-thread [name]`** — **persistent context threads** — lightweight cross-session knowledge

→ **"Planting seeds" metaphor distinctive.** Forward-looking capture với delayed activation.

---

## Workstreams (parallel milestone work)

**`/gsd-workstreams`** — manage parallel work:
- `list`, `create <name>`, `switch <name>`, `status`, `progress`, `complete <name>`

Use case: 2 teammates on different workstreams in same milestone.

→ **Team-coordinate primitive.** Not in siblings explicitly (Superpowers single-user, gstack solo focused).

---

## Multi-Project Workspaces

**`/gsd-new-workspace`** — isolated workspace với repo copies (**worktrees or clones**)

Use case: 1 developer, multiple concurrent projects, no interference.

→ **Match gstack's Conductor parallel sprints.** Different mechanism (worktrees vs separate Claude Code sessions).

---

## Security section (line 384)

Mentions:
- Threat-model-anchored verification (`/gsd-secure-phase`)
- Edit safety rule
- Commit rules for agents
- Recovery quick reference

**Full details in section line 384-443 + 878+** (not deep-read this session).

→ **Security taken seriously.** Match ECC's AgentShield scope, different mechanism.

---

## Configuration Reference (line 612)

**`.planning/config.json`** stores project settings.

Core settings (từ README):
| Setting | Default | Effect |
|---------|---------|--------|
| `mode` | `interactive` | `yolo` or `interactive` auto-approve |
| `workflow.discuss_mode` | `questions` | `questions` or `assumptions` |
| Model profiles | `balanced` | quality/balanced/budget/inherit |

**`/gsd-settings`** command — interactive config editor.
**`/gsd-set-profile <profile>`** — quick switch.

---

## Usage Examples (line 744)

(Not deep-read — contains concrete multi-step scenarios per README workflow.)

---

## Edit Safety Rule (line 878)

**Major section (234 lines covering lines 878-1112).** Discipline around file edits:
- Likely: no edits outside `.planning/` without explicit approval
- Safety guards around destructive operations
- Match gstack's `/freeze` + Superpowers's HARD-GATE philosophy

(Not deep-read — infer from section length + pattern.)

---

## Git Commit Rules for Agents (line 1112)

**Short but critical section (12 lines).**

Inferred rules (match README + other Tier 1 patterns):
- Atomic commits per task
- No bulk commits (`git add .`)
- Commit message convention (prefix with task ID)

→ **Discipline convergence** với gstack's "Always bisect commits" + Superpowers's git-worktree skill.

---

## Recovery Quick Reference (line 1124)

`/gsd-pause-work` + `/gsd-resume-work` + `/gsd-session-report` mentioned trong README commands.

Recovery từ:
- Session interruption (laptop sleep, crash)
- Failed workflow run (`/gsd-forensics`)
- Stuck phase (`/gsd-health --repair`)

→ **Resilience-first design.**

---

## Project File Structure (line 1145, last section)

Expected structure after `/gsd-new-project`:
```
.planning/
├── PROJECT.md         # Vision
├── REQUIREMENTS.md    # Scoped v1/v2
├── ROADMAP.md         # Phases
├── STATE.md           # Cross-session memory
├── research/          # Ecosystem knowledge
├── phases/
│   ├── 01/
│   │   ├── CONTEXT.md
│   │   ├── RESEARCH.md
│   │   ├── 01-PLAN.md
│   │   ├── 01-SUMMARY.md
│   │   └── VERIFICATION.md
│   └── ...
├── todos/
├── threads/
├── seeds/
├── spike-{N}/
├── sketch-{N}/
└── quick/
```

→ **Comprehensive file structure.** Everything namespaced trong `.planning/`.

---

## Distinctive patterns (từ USER-GUIDE skim)

### Pattern 1: `.planning/` namespace

All GSD artifacts trong single folder. Easy .gitignore, easy audit, clean project root.

→ **Clean namespace.** gstack has `~/.gstack/` + project-local `.gstack/`. GSD keeps project-local only via `.planning/`.

### Pattern 2: 4 parallel researchers

Stack/Features/Architecture/Pitfalls. Each fresh context. Synthesized by Research Synthesizer agent.

→ **Research depth = core differentiator** vs siblings.

### Pattern 3: "Seeds" forward-looking capture

Ideas với trigger conditions surface at right milestone. Prevents "add to backlog and forget."

→ **Time-aware backlog management.** Novel vs siblings.

### Pattern 4: Spike + Sketch → skill packaging

Experiments → project-local skill files. Reusable for future build conversations.

→ **Learning loop built-in.** Match gstack's `/learn` concept, different artifact (skill file vs JSON state).

### Pattern 5: Workstreams + Workspaces for parallelism

Workstreams = logical parallel within 1 project.
Workspaces = physical parallel (worktrees/clones).

→ **2 parallelism axes.** gstack = workspaces via Conductor. GSD = both built-in.

---

## Commands summary (from USER-GUIDE section 525)

Commands categorized trong USER-GUIDE match README list. See `(C) README summary.md` for full 83-command list.

---

## Open questions resolved

- ✅ Q12: Spec-driven focus — `/gsd-new-project` → REQUIREMENTS.md + ROADMAP.md is spec-driven flow
- ✅ Q3: 83 commands are categorized (14 groups). Not all equally important — core workflow ~6 commands

## Open questions raised

- ⏸ Edit Safety Rule exact implementation — section 878-1112 not deep-read
- ⏸ Security section details (line 384-443) — threat models?
- ⏸ 4 parallel researchers coordination — how does synthesizer merge?
- ⏸ "Plant Seed" trigger conditions — concrete example?
- ⏸ Workstreams branching model — git-level?

---

## Cross-references

- [[(C) README summary]]
- [[(C) ARCHITECTURE + CHANGELOG summary]]
- [[(C) index]]
- [[(C) log]]
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) The 7-Stage Workflow.md` — workflow comparison
- Cross-project: `../../gstack - Beginner Analysis/02 Wiki/(C) Sprint Pipeline.md`

## Citations

- `docs/USER-GUIDE.md` TOC (lines 7-22)
- Full Project Lifecycle diagram (lines 23-80)
- Planning Agent Coordination diagram (lines 80-180)
- Section headers throughout (grep scan)

## TODO

- ⏸ Deep-read Edit Safety Rule (234 lines) for dev guidance
- ⏸ Deep-read Security section (60 lines)
- ⏸ Compare `.planning/` structure vs gstack's `~/.gstack/` vs ECC's plugin artifacts
