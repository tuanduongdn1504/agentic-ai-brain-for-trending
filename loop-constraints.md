# loop-constraints.md — Storm Bear vault

Binding rules for any loop/agent acting in this vault (loop-engineering v189 convention, adapted from `templates/loop-constraints.md` @ `f18df04`). **The agent MUST read this file at the start of a run and apply every rule to every action.** If `loop-pause-all` is present in STATE.md → exit immediately.

## Push & Merge
- Never merge to `main`. Never push to `main`. All merges are operator actions.
- Ships go on `wiki/vNNN-<slug>` branches; pilots on `pilot/*`; hireui agent work on `agent-*` (its CONSTITUTION I-2).
- Never publish/send to external surfaces (posts, PRs to third-party repos, telegram to new chats) without an explicit operator ask.

## Paths
- Never edit operator-authored notes without asking — `00 Notes/`, `01 Journals/`, `02 Chess Moves*/`, and any file NOT prefixed `(C)` outside the maintained state set. ("Ask before editing existing notes" is the root rule.)
- Claude-maintained state set (edit as part of routine work): CLAUDE.md shim · `_state/*` · `_patterns/*` · `_goals/*` · `(C) *` files · **the five loop convention files (STATE.md / LOOP.md / loop-budget.md / loop-run-log.md / loop-constraints.md — operator (C)-prefix waiver, 2026-07-02)**.
- Never touch `.env*`, credentials, or secrets anywhere; in hireui also honor its CONSTITUTION (I-8 operator-only skill registry).

## Content & Verification (corpus discipline)
- All corpus/collision/identity claims verified BY HAND (`feedback_wiki_verify_independently_check_collisions`); research workflows are read-only fact-gatherers.
- §37 provenance tags on volatile facts; GitHub API is mocked here → stars/forks are page-stated, never #52 claims.
- §28: ≤2 new §C standalones per wiki; clustering-first; record NO-MINT alternatives.
- Never fabricate; flag contradictions for the operator, don't auto-resolve (§38).

## Loops
- **No loop starts above L1 (report-only).** L1→L2 only per the graduation bar: 2 weeks L1 · <20% noise · verifier proven on a manual case first · denylist documented · loop-audit ≥58.
- Budget check (per `loop-budget.md`) at start AND end of every run; append a `loop-run-log.md` entry at end.
- Max 3 attempts on any fix, then escalate. One problem per invocation. Never mark your own work done — the verifier (`.claude/agents/loop-verifier.md`) or the operator decides.
- Never `--dangerously-skip-permissions`. Pin third-party tool versions/commits (loop-engineering = `f18df04`).

## Communication
- Every session response ends with a suggested next action. Report failures plainly, with numbers.
