# LOOP.md — Storm Bear vault

How this vault is operated as loops (loop-engineering v189 convention; adapted from the reference repo's root `LOOP.md` @ `f18df04`). **Every loop below is operator-fired or operator-gated — there is deliberately NO always-on/scheduled layer** (0 scheduled tasks, 0 crons as of 2026-07-02). Adding any schedule requires `loop-budget.md` caps + the kill switch first (operator fence, 2026-07-02).

## Active Loops

### Wiki-ship routine (LLM Wiki Routine v2.6) — operator-fired, L2-equivalent with human gates
- Trigger: operator request ("build LLM wiki from <repo>…"). NOT scheduled.
- Triage: Phase 0.9 gate (GOAL-ALIGNED / OFF-GOAL / SKIP; §35 off-goal ceiling).
- State: CLAUDE.md shim head + `_state/03c` (authoritative entries) + `_patterns/06` (registry) + this STATE.md.
- Isolation: every ship on a `wiki/vNNN-<slug>` branch; **never auto-merged** — operator reviews + merges (human gate).
- Maker/checker: read-only research workflows may gather source/upstream facts; **ALL corpus/collision/identity claims verified by hand** (`feedback_wiki_verify_independently_check_collisions`); verifier artifact: `.claude/agents/loop-verifier.md`.
- Budget + run-log: per `loop-budget.md`; append one JSON line per ship to `loop-run-log.md`.

### Pilot loops (the v189 ladder) — operator-fired, L1 first
- Current: D16 hireui PR-Babysitter (L1 report-only, week one) — lives in the hireui repo on branch `agent-loop-pr-babysitter` with its own LOOP.md/budget/state; runs hireui-rooted per its CONSTITUTION (I-2 / I-8 / GitNexus-first).
- Rule: **no loop starts above L1**; L1→L2 only per the graduation bar (2 weeks L1 · <20% noise · verifier proven on a manual case · denylist documented · loop-audit ≥58).

### Autopilot-research — operator-fired, L1 report+draft (lives in a separate repo)
- The drain pipeline (`bin/autopilot-drain.py` + evals + output docs) is NOT in this vault; its state surfaces here via memory pilot-thread files + `03 Projects/` docs. Audit it in its own repo.

### Memory consolidation — manual, L1
- `/consolidate-memory` on request; write-gate = operator rules in `loop-constraints.md`.

### Ad-hoc `/loop` / ScheduleWakeup — session-scoped only
- Dies with the session; no persistent state. If one is ever made persistent (scheduled task / cron), it MUST first get a row in `loop-budget.md` + honor `loop-pause-all`.

## Worktrees & branches
- Ships: `wiki/vNNN-<slug>` · pilots: `pilot/*` · hireui agent work: `agent-*` (its I-2). `.claude/worktrees/` used for parallel session isolation. One unit of work per branch; operator merges.

## Connectors (MCP)
- In use, session-scoped: scheduled-tasks · telegram · ccd_session · Claude_Preview / Claude-in-Chrome · visualize. Scope: no connector writes to external surfaces without an explicit operator ask (telegram replies only on operator-initiated threads).

## Budget & Observability
- Caps + kill switch: `loop-budget.md` (**≥80% of a cap → report-only mode; ≥100% or `loop-pause-all` in STATE.md → exit immediately**).
- Run history: `loop-run-log.md` — JSON, one line per run: `{run_id, pattern, duration_s, items_found, actions_taken, escalations, tokens_estimate, outcome}`.

## Safety & Gates (this vault)
- Never merge to `main` (operator merges everything). No auto-merge policy exists at all — by design.
- Path denylist + write rules: `loop-constraints.md` (binding; read it before acting).
- Corpus discipline: §37 fact-provenance tags · §28 ≤2 new standalones/wiki · verify-independently for all corpus claims.

---
*This file is documentation AND the seed for any future scheduled loop. Operating phase today: L1/L2 with human gates everywhere; the Loop-Ready score measures scaffolding, not judgment.*
