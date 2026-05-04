# (C) Cluster — AGENTS.md + 19 agents + child-agent protocol + tools

> **Type:** Source cluster summary
> **Sources:** AGENTS.md (21 KB, 407 lines) + CLAUDE.md (6.6 KB)
> **Coverage:** Agent catalog, child-agent protocol, delegation rules, model routing, verification protocols, commit protocol
> **Parent:** [[(C) index]]

---

## 1. Summary

OMC's AGENTS.md + CLAUDE.md define a **governance contract for intelligent multi-agent orchestration** — 19 specialized agents, child-agent spawning protocol (up to 6 concurrent), model routing (haiku/sonnet/opus), delegation rules, verification protocols, and commit trailers. Among the **largest AGENTS.md files in Storm Bear corpus at 21 KB** (Pattern #22 strengthening).

## 2. 19 specialized agents (canonical catalog)

From CLAUDE.md `<agent_catalog>` (all invoked with `oh-my-claudecode:` prefix):

| Agent | Model | Role |
|-------|-------|------|
| `explore` | haiku | Fast codebase search, file/symbol mapping |
| `analyst` | opus | Requirements clarity, acceptance criteria, hidden constraints |
| `planner` | opus | Task decomposition and execution planning |
| `architect` | opus | System architecture, deep analysis |
| `debugger` | sonnet | Root-cause diagnosis |
| `executor` | sonnet | Default for substantive code changes |
| `verifier` | sonnet | Evidence-driven completion verification |
| `tracer` | sonnet | Evidence-driven tracing lane |
| `security-reviewer` | sonnet | Security-focused review |
| `code-reviewer` | opus | Approval pass (never self-approve same context) |
| `test-engineer` | sonnet | Test strategy + implementation |
| `designer` | sonnet | UI/UX design |
| `writer` | haiku | Content authoring |
| `qa-tester` | sonnet | Quality assurance |
| `scientist` | sonnet | Experimental / ML workflows |
| `document-specialist` | sonnet | SDK/API docs consultation (uses Context Hub / `chub` when available) |
| `git-master` | sonnet | Git operations |
| `code-simplifier` | opus | Deletion-first refactoring |
| `critic` | opus | Independent critique |

## 3. Child-agent protocol (up to 6 concurrent)

**Claude Code spawns child agents via `spawn_agent` tool** (requires `multi_agent = true`). Parent MUST read role prompt and pass it in spawn message.

**Delegation steps:**
1. Decide role (`architect`, `executor`, `debugger`, etc.)
2. Read prompt from `~/.codex/prompts/{role}.md`
3. Call `spawn_agent(message=<prompt content> + <task>)`
4. Child executes independently

**Parallel delegation example:**
```
spawn_agent(message: "<architect prompt>\n\nTask: Review auth module")
spawn_agent(message: "<executor prompt>\n\nTask: Add input validation")
spawn_agent(message: "<test-engineer prompt>\n\nTask: Write auth tests")
```

**Constraints:**
- Max 6 concurrent child agents
- Each child has isolated context window
- Parent must read prompt file BEFORE spawn_agent
- Children access skills via `$name` but focus on assigned role

## 4. Invocation conventions

Three custom-command prefixes:

- `/prompts:name` — invoke custom prompt (e.g., `/prompts:architect "review auth"`)
- `$name` — invoke skill (e.g., `$ralph "fix all tests"`, `$autopilot "build REST API"`)
- `/skills` — browse available skills interactively

**Agent prompts location:** `~/.codex/prompts/` (architect, executor, planner, etc.)
**Workflow skills location:** `~/.agents/skills/` (ralph, autopilot, plan, ralplan, team, etc.)

## 5. Delegation rules

**Delegate when** work benefits from:
- Multi-file implementations, refactors, debugging, reviews, planning, research, verification
- Specialist prompts (security, API compatibility, test strategy, product framing)
- Independent tasks in parallel (up to 6 concurrent children)

**Work directly only for:**
- Small clarifications, quick status checks, single-command sequential operations
- Trivial ops where delegation adds disproportionate overhead

**Default routing:** Substantive code changes → `executor` (both standard + complex). Non-trivial SDK/API/framework usage → `dependency-expert` (checks official docs first).

## 6. Model routing

Match role to complexity:
- **Low** (quick lookups, narrow checks): `explore`, `style-reviewer`, `writer` → haiku
- **Standard** (implementation, debugging, reviews): `executor`, `debugger`, `test-engineer` → sonnet
- **High** (architecture, deep analysis, complex refactors): `architect`, `executor` (opus mode), `critic` → opus

**Cost optimization claim from README:** "Smart model routing saves 30-50% on tokens."

## 7. Tools surface

From CLAUDE.md `<tools>`:

**External AI:**
- `/team N:executor "task"` (native teams)
- `omc team N:codex|gemini "..."` (tmux CLI workers)
- `omc ask <claude|codex|gemini>` (advisor)
- `/ccg` (tri-model synthesis)

**OMC State:**
- `state_read`, `state_write`, `state_clear`, `state_list_active`, `state_get_status`

**Teams:**
- `TeamCreate`, `TeamDelete`, `SendMessage`, `TaskCreate`, `TaskList`, `TaskGet`, `TaskUpdate`

**Notepad:**
- `notepad_read`, `notepad_write_priority`, `notepad_write_working`, `notepad_write_manual`

**Project Memory:**
- `project_memory_read`, `project_memory_write`, `project_memory_add_note`, `project_memory_add_directive`

**Code Intel:**
- LSP: `lsp_hover`, `lsp_goto_definition`, `lsp_find_references`, `lsp_diagnostics`, etc.
- AST: `ast_grep_search`, `ast_grep_replace`
- `python_repl`

## 8. Verification protocol

*"Verify before claiming completion. Size appropriately: small→haiku, standard→sonnet, large/security→opus. If verification fails, keep iterating."*

**Execution protocols:**
- Broad requests → explore first, then plan
- 2+ independent tasks in parallel
- `run_in_background` for builds/tests
- **Authoring and review as separate passes** — writer pass creates/revises, reviewer/verifier pass evaluates later in separate lane
- **Never self-approve in same active context** — use `code-reviewer` or `verifier` for approval pass
- Before concluding: zero pending tasks, tests passing, verifier evidence collected

## 9. Commit protocol (git trailers)

OMC prescribes structured git trailers for every non-trivial commit:

**Format:** conventional commit subject + optional body + structured trailers

**Trailer types:**
- `Constraint:` active constraint shaping this decision
- `Rejected:` alternative considered | reason for rejection
- `Directive:` warning/instruction for future modifiers
- `Confidence:` high | medium | low
- `Scope-risk:` narrow | moderate | broad
- `Not-tested:` edge case not covered

**Corpus first — structured git trailer protocol at T1.** Distinct from BMAD v11 methodology-only commits or spec-kit v17 constitution gates.

## 10. Working agreements (canonical)

From AGENTS.md `<working_agreements>`:

- Write cleanup plan before modifying code
- Prefer deletion over addition
- Reuse existing utilities and patterns first
- No new dependencies without explicit request
- Keep diffs small and reversible
- Run lint, typecheck, tests, static analysis after changes
- Final reports include: changed files, simplifications made, remaining risks

## 11. Guidance schema contract

AGENTS.md defines **canonical guidance schema** in `docs/guidance-schema.md`. Required sections:
- **Role & Intent** → title + opening paragraphs
- **Operating Principles** → `<operating_principles>`
- **Execution Protocol** → delegation/model routing/agent catalog/skills/team pipeline sections
- **Constraints & Safety** → keyword detection, cancellation, state-management rules
- **Verification & Completion** → `<verification>` + continuation checks
- **Recovery & Lifecycle Overlays** → runtime/team overlays appended by marker-bounded hooks

**Runtime marker contracts (stable + non-destructive):**
- `<!-- OMX:RUNTIME:START --> ... <!-- OMX:RUNTIME:END -->`
- `<!-- OMX:TEAM:WORKER:START --> ... <!-- OMX:TEAM:WORKER:END -->`

## 12. Per-role team routing

Configurable in `.claude/omc.jsonc` under `team.roleRouting`:
- Codex → critic
- Gemini → reviewer
- Aliases normalized at runtime (`reviewer` etc.)

See `skills/team/SKILL.md#per-role-provider--model-routing`.

## 13. Cross-wiki signals

- **Pattern #22 AGENTS.md industry standard** — OMC 21 KB AGENTS.md is **among largest in corpus** (cf. gws v13 209-line corporate tri-file, spec-kit v17 6-file corporate governance)
- **Pattern #18 Agent Runtime Standardization** — OpenClaw integration + Codex + Gemini + Cursor = multi-runtime first-class
- **Pattern #12 Governance Depth vs Organization** — solo-author (Yeachan) but **corporate-depth governance** (21 KB AGENTS.md + child-agent protocol + commit trailers + verification protocol) — **challenges Pattern #12 formulation** (corporate ≠ depth; solo can match corporate depth)
- **Pattern #28 Multi-Provider AI Support** — 3 canonical CLI providers (Claude + Codex + Gemini) + Cursor-agent
- **Commit trailer novelty** — Constraint/Rejected/Directive/Confidence/Scope-risk/Not-tested = corpus first at T1

---

**Cluster signal:** OMC governance is **corporate-grade despite solo authorship** — 19-agent catalog with explicit model routing + child-agent spawning protocol + structured commit trailers + guidance schema contract challenges Pattern #12 correlation between org type and governance depth. Solo-at-enterprise-scale (agency-agents v18 pattern) now extends to solo-at-enterprise-governance-depth.
