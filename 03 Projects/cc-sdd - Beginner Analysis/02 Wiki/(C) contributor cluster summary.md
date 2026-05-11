# Cluster 2 — Contributor / agent-facing docs

> **Sources:** CLAUDE.md (project root) + AGENTS.md + skill-reference.md + workflow heuristics for agent operators.
> **Wiki:** cc-sdd v61.

---

## 1. Verbatim positioning / philosophy

From CLAUDE.md (project root):
> *"steering files provide 'project-wide rules and context,' while specs formalize 'development process for individual features.'"*

> *"Follow the user's instructions precisely, and within that scope act autonomously: gather necessary context and complete requested work end-to-end in this run."*

From AGENTS.md:
> *"If there is even a 1% chance a skill applies to the current task, invoke it."*

## 2. Steering vs Specs (organizational division)

| Directory | Purpose | Lifetime | Audience |
|---|---|---|---|
| `.kiro/steering/` | Project-wide rules + context | Long-lived | All agents, every task |
| `.kiro/specs/<feature>/` | Per-feature development process | Feature-scoped | Subagents working on that feature |

Default steering files:
- `product.md` — business context
- `tech.md` — technology decisions / architecture
- `structure.md` — directory + file responsibility map

Custom steering files (created via `/kiro:steering-custom`): API standards, testing practices, security patterns, etc.

**Observation:** 3-file default steering set is leaner than spec-kit v17 (9-article constitution) and BMAD v11 (multi-file BMM persona library). Closer to oh-my-claudecode (OMC) v27's lightweight memory-tier approach.

## 3. Skill reference (6 primary skills)

### Workflow skills (3)

#### `/kiro-discovery`
- **Purpose:** routes new work into 5 outcomes (extend existing spec / direct implementation / single spec / multi-spec decomposition / no-spec-needed)
- **Inputs:** New work request (often unclear scope)
- **Outputs:** Routing decision + scope refinement + `brief.md` + (if multi-feature) `roadmap.md`
- **Typical next:** One of `/kiro-spec-init` / `/kiro-spec-batch` / direct implementation

#### `/kiro-spec-batch`
- **Purpose:** creates multiple specs in parallel with cross-spec consistency + roadmap-shaped backlog
- **Inputs:** Roadmap or discovery-output indicating multi-spec work
- **Outputs:** Multiple specs with maintained dependency-aware coherence

#### `/kiro-impl`
- **Purpose:** Execute implementation from approved task definitions
- **Modes:**
  - **Autonomous** (no task args): fresh-roles per iteration, dispatches subagents independently
  - **Manual** (task args): TDD in main context, targeting specified tasks
- **Outputs:** Implemented features with reviewer approval + completion verification
- **Dependencies:** Approved `tasks.md`; integrates `kiro-review`, `kiro-debug`, `kiro-verify-completion`

### Supporting skills (3)

#### `kiro-review`
- **Purpose:** Task-local adversarial review protocol
- **Checks:** spec compliance / boundary fit / mechanical verification (tests + lint + types) / RED-phase evidence
- **Used by:** Reviewer subagents in autonomous mode + manual review gates

#### `kiro-debug`
- **Purpose:** Root-cause-first investigation protocol
- **Returns:** `ROOT_CAUSE` / `CATEGORY` / `FIX_PLAN` / `NEXT_ACTION`
- **Triggered by:** Implementer blockage OR reviewer rejection loops

#### `kiro-verify-completion`
- **Purpose:** Fresh-evidence gate before success claims
- **Returns:** `VERIFIED` / `NOT_VERIFIED` / `MANUAL_VERIFY_REQUIRED`
- **Used before:** Marking tasks complete + confirming fixes + reporting success

## 4. Workflow phase boundaries

Three explicit phases with **human-approval gates between**:
1. **Requirements** (human approval)
2. **Design** (human approval)
3. **Tasks** (human approval)
4. **Implementation** (autonomous within task scope)

> *"3-phase approval workflow: Requirements → Design → Tasks → Implementation"* (CLAUDE.md project root)

**Observation:** Strict phase-boundary discipline; CLAUDE.md states approval is required between phases. Distinct from BMAD v11's persona-flow (no fixed approval gates) and from spec-kit v17's concurrent-section design (less rigid boundaries).

## 5. Operational principles (verbatim)

From CLAUDE.md:
- *"All project documentation must be written in the language configured in spec.json"* — i18n at the spec-config level, not global default
- *"Skills are modular tools located in `.claude/skills/kiro-*/` directories"* — Skills mode primitive
- *"Default steering files include product.md, tech.md, and structure.md in `.kiro/steering/`"* — explicit defaults

From AGENTS.md:
- *"emphasizes human review at phase boundaries while enabling agent autonomy within defined scopes"* — autonomy-bounded-by-contract design philosophy

## 6. Quality gates (validation skills)

CLAUDE.md describes 3 validation checkpoints:
- `/kiro-validate-gap` — analyzes existing codebase against requirements (brownfield)
- `/kiro-validate-design` — technical design review with GO/NO-GO assessment
- `/kiro-validate-impl` — validates implementation against requirements + design + test coverage

**Observation:** Validation skills are OPTIONAL quality gates. Distinct from spec-kit v17's compile-time-gates (mandatory). cc-sdd offers gates but doesn't enforce them.

## 7. Cross-agent compatibility note

AGENTS.md emphasizes:
- Skills are compartmentalized in **agent-specific directories** (e.g., `.claude/skills/`, `.codex/skills/`, `.cursor/skills/`)
- May spawn parallel research subagents (autonomy heuristic)
- Per-agent skill format translation handled at `npx cc-sdd@latest --<platform>-skills` install time

**Observation:** **CORPUS-FIRST agent-platform-format-translation-installer pattern** — single npm CLI installer translates SDD skill definitions into per-platform skill formats at install time. Distinct from:
- OpenSpec v58 30+ tools per-tool format translation (broader breadth, similar mechanism)
- free-claude-code v60 6-provider API protocol translation (runtime, not install-time)
- mattpocock-skills v57 (Claude Code-only, no multi-platform translation)

## 8. AGENTS.md ↔ CLAUDE.md duplication pattern (Pattern #22 reference)

Both `AGENTS.md` and `CLAUDE.md` (project root) cover same content with high-overlap (per Pattern #22c v60 sub-variant). cc-sdd does NOT include the AGENTS.md ↔ CLAUDE.md explicit-sync-comment-header observed in v60 (corpus-first there). cc-sdd is post-amendment-window observation 22c-natural — files are duplicated but no explicit sync-comment.

## 9. Subagent dispatch pattern

`/kiro-impl` autonomous mode:
- Fresh-roles per iteration (each subagent starts clean per task)
- Independent review cycle (reviewer subagent separate from implementer subagent)
- Auto-debug-on-failure (kiro-debug invoked when implementer blocks or reviewer rejects)
- Long-running task execution (continues across multiple subagent rounds)

**Observation:** Strong adversarial-review architecture with separate roles. Compare to:
- BMAD v11 persona-system (cooperative roles)
- spec-kit v17 concurrent-section design (no explicit reviewer subagent)
- OpenHands v30 4-layer agent architecture (more layers, less spec-driven)

cc-sdd's role separation is **adversarial-by-design** at the subagent level — closer to LLM-as-judge research patterns than to cooperative agent orchestration.

## 10. Implementation discipline

From CHANGELOG / command-reference:
- TDD mandatory: RED (failing test) → GREEN (minimal code) → REFACTOR
- Task sizing: subtasks 1-3 hours each; major tasks span multiple subtasks
- Parallel safety: P0 = blocking work, same P# = concurrent-safe
- Checkbox format: exact `- [ ]` / `- [x]` (machine-parseable)
- Auto-approval caution: `-y` flag skips human review (use only for trusted workflows)

## 11. Corpus-first observations

- **Adversarial subagent review architecture** — separate reviewer subagent + auto-debug-on-rejection (corpus-first explicit adversarial review at the framework level)
- **kiro-verify-completion fresh-evidence gate** — explicit primitive for "did this actually work" before reporting success (corpus-first as separate skill)
- **3-phase approval-gate architecture** with discrete documented gates (corpus-first explicit gate-discipline at this granularity; spec-kit v17 has gates but less structured)
- **P-wave parallel-execution annotation** — task priority + concurrency in same primitive (corpus-first)
- **`brief.md` discovery artifact** — pre-spec routing decision (corpus-first as discovery output)

## 12. Absences (vs prior corpus subjects)

- ❌ NO persona-library (vs BMAD v11)
- ❌ NO 9-article constitution (vs spec-kit v17)
- ❌ NO MCP-server primitive in cc-sdd (sibling skillport adds this)
- ❌ NO marketplace (vs spec-kit v17 80+ marketplace)
- ❌ NO Karpathy citation
- ❌ NO research-paper-chain
- ❌ NO ML-training infrastructure (vs LlamaFactory v22 / Unsloth v23)

## 13. Cross-wiki corpus-context

- Strong sibling: spec-kit v17 (3-phase workflow vs spec-kit specify/plan/tasks; both T1 SDD)
- Strong sibling: OpenSpec v58 (per-tool skill format translation; cc-sdd at 8 vs OpenSpec at 30+)
- Adjacent: BMAD v11 (methodology-shaped peer; BMM not SDD; persona-library vs steering-files)
- Adjacent: gh-aw v48 (workflow-shaped peer)

## 14. Pattern advancement check

- **Pattern #21 SDD Methodology Emergence un-stale** — confirmed via independent SDD-centered framework
- **Pattern #18 sub-archetype: agent-platform-format-translation-installer** — N=1 candidate registration
- **Pattern #57 57c family** — cc-sdd does not directly cite spec-kit/OpenSpec/GSD; conservative-attribution does NOT apply here
- **Pattern #51 Vibe-Coding nuance** (counter-evidence) — anti-vibe-with-pragmatic-acknowledgment sub-pole

## 15. Length / granularity note

CLAUDE.md (project root) + AGENTS.md are short (~30-50 lines each estimated) — gotalab uses these as agent-instruction headers, not exhaustive documentation. Detailed skill behaviors live in `docs/guides/skill-reference.md` (covered here under §3) and command behaviors in `docs/guides/command-reference.md` (covered Cluster 3).
