# course-video-manager as artifact — the repo behind the demo

## Source

- [github.com/mattpocock/course-video-manager](https://github.com/mattpocock/course-video-manager) — fetched via `gh api` 2026-07-03 (metadata, package.json, `CONTEXT.md`, `.claude/skills/`, `.sandcastle/`, `settings.local.json`, commit/issue history).

## Why it matters

- It's a **rare public specimen of a real, daily-driven, single-operator + AI-agents production repo** — not a demo repo built for the video. Created 2025-07-24, actively pushed through 2026-07-02; 506★ / 114 forks / 33 open issues; **1,109+ closed issues** (the video's "637" was point-in-time March).
- It's Matt's actual work tool (course authoring: sections/lessons/videos backed by git, published as immutable snapshots) — the dogfooding surface for every skill and harness he ships.

## Stack (verified in package.json)

- **React Router** app · **TypeScript** · Node · **Drizzle ORM** (+ `db:push` script) · **Postgres** (with **PGLite** in-memory for tests) · **Vitest** · **Effect** for backend service composition — all six video claims confirmed.
- Run-locally-not-deployed workflow (build + start scripts) — an internal tool, so "I don't really care what my API looks like from the outside."

## The harness surface inside the repo

- **`.sandcastle/`** — the AFK loop orchestration (see [[sandcastle-ralph-afk-loop]]): `main.ts` (MAX_ITERATIONS=10, 4-parallel), per-phase prompts (plan/implement/review/merge), Dockerfile (Node 22 + gh CLI + Claude Code CLI).
- **`CONTEXT.md`** — the ubiquitous-language glossary (see [[ubiquitous-language-for-llms]]): ghost lesson/section/course, materialize, materialization cascade, aliases-to-avoid, authoring-status vs fsStatus invariant.
- **`.claude/skills/`** — in-repo project skills, notably:
  - **`do-work/DB-TDD.md`** — interface-based DB testing via PGLite; explicitly rejects query-structure assertions in favor of behavior-through-interface tests (tests-verify-intent, cf. [[../claude-md-12-rules/_index]] Rule 9).
  - **`to-prd-project/SKILL.md`** — project-tuned PRD skill; PRD-as-parent-issue; "do NOT apply the implement label" guard so the loop never picks up the parent.
- **`settings.local.json`** — **89-entry fine-grained permissions ALLOW-list** (git, testing, GitHub issue ops, WebFetch domains, read paths…) — curated allow-list rather than blanket permissions; operator-level permission discipline.
- **`api.feedback.ts`** — the feedback button backend; **Haiku**-generated issue titles (see [[qa-plan-and-feedback-loop]]).
- **`CLAUDE.md`** — repo knowledge vault following the Karpathy LLM-Wiki pattern (per deep-dive read).

## The agent trail

- Ralph/Sandcastle commits carry **dual co-author signatures** (human + Claude Opus 4.6 / Sonnet 4.6 / claude-code[bot]) from 2026-03-31 onward — auditable AI authorship, not laundered commits.
- The ghost-work Sandcastle-labeled issues **#743–#748** closed 2026-03-31 → 04-02 — the publicly visible trail of the feature family demoed in the video (post-upload iteration; the video's own issue batch isn't separately identifiable).

## What this repo models for anyone building a personal harness

1. Glossary (`CONTEXT.md`) + knowledge vault (`CLAUDE.md`) = the agent's *context layer*.
2. Project skills (`.claude/skills/`) = the *procedure layer*, tuned per-repo on top of the global skills repo.
3. `.sandcastle/` = the *execution layer* with bounded loops and per-commit gates.
4. `settings.local.json` allow-list = the *permission layer*.
5. GitHub issues = the *queue layer* connecting human planning/QA to agent execution.

## Key Takeaways

- The repo demonstrates that the whole stack — context, procedures, execution, permissions, queue — fits inside **one repo with zero external infrastructure** beyond Docker + GitHub.
- **In-repo project skills beat global skills for repo-specific discipline** (DB-TDD encodes *this* repo's testing philosophy; to-prd-project encodes *this* repo's labels).
- An 89-entry allow-list is what "actively curated permissions" actually looks like in practice.
- Cross-links: [[overview]] · [[the-originals]] · [[../harness-engineering/_index]] (this is individual-scale harness engineering, fully materialized).
