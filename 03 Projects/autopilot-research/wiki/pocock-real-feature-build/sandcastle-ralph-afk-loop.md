# Sandcastle / Ralph AFK loop — the harness at birth vs today

## Source

- Transcript `raw/2026-07-03-pocock-real-feature-build.md` · current source verified via `gh api` on [mattpocock/course-video-manager](https://github.com/mattpocock/course-video-manager) (`.sandcastle/`) + [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) + npm `@ai-hero/sandcastle`.

## Terminology (pin this)

- **Ralph** = the *technique* (run an agent in a loop against a queue; lineage: Geoffrey Huntley — see [[../pocock-agentic-workflow/the-originals]]).
- **Sandcastle** = Matt's *implementation/package* (`@ai-hero/sandcastle`). The video is its public origin: "the provisional name for this is Sandcastle… I've been cooking my setup over the last 24 hours."

## Verified timeline — this video is Sandcastle's birth certificate

| Date | Event |
|---|---|
| 2026-03-17 ~14:49 UTC | `mattpocock/sandcastle` GitHub repo created (~16.5h before the video published) |
| 2026-03-18 | Video published; in-video harness = Dockerfile + prompt inside course-video-manager, run via `pnpm ralph` |
| 2026-03-26 | npm `@ai-hero/sandcastle` v0.0.1 published (9 days later) |
| 2026-06-18 | Ondrej podcast discusses the mature package (5 sandbox × 6 agent providers) — see [[../pocock-agentic-workflow/sandcastle-deep-dive]] |

## The harness as shown in the video (March 2026)

- **Docker container** built from a repo Dockerfile; **mounts the working directory**; Claude Code runs inside.
- **Commits made inside the container are pulled out as patches** and applied to the local repo — isolation without giving the agent your host.
- `pnpm ralph` starts the loop (video says "max iterations of 100" — see correction below). The agent: pulls GitHub issues → picks one → implements → **runs tests and typecheck on every commit** → closes the issue → repeats; the loop naturally exhausts when the queue is empty ("it will run out of GitHub issues").
- Prompt contains a human-in-the-loop guard: "if there's a human-in-the-loop label on it or it looks like it's for humans, don't work on it" (video claim; current source uses different mechanics — below).
- Run 1: **5 iterations, 6 commits, ~90 minutes AFK** ("went for a walk, had a cup of tea with my parents"). Feature build total: ~14 commits, ~8 iterations.

## The harness as it exists now (verified in `.sandcastle/`, 2026-07)

- Orchestration lives in **`.sandcastle/main.ts`**, invoked via `pnpm sandcastle`; uses the published `@ai-hero/sandcastle` package. **`MAX_ITERATIONS = 10`** (line-verified) — not 100.
- **4-phase loop: Plan → Implement → Review → Merge**, with separate prompt files per phase — the review phase is a distinct agent pass, not an afterthought.
- **Up to 4 issues processed in parallel** per cycle (MAX_PARALLEL=4 semaphore).
- **Issue selection is dependency-based** — picks issues with zero open blockers. (The video's label-based human-skip was not found in current source; label filtering appears superseded by dependency selection + explicit labels like the implement label being *required* to enqueue.)
- Container: Node 22 + GitHub CLI + Claude Code CLI; the container **persists and is reused** (`sleep infinity`), not rebuilt per issue.
- **Two-phase issue closure:** implementation does NOT close issues; closure happens at the merge phase — discipline separating "code written" from "change accepted."
- Commit trail shows co-author signatures (Claude Opus 4.6 / Sonnet 4.6 / claude-code[bot]) from 2026-03-31 onward; the ghost-work Sandcastle-labeled issue trail (#743–#748) closed 2026-03-31 → 04-02.

## Why this design (Matt's articulation)

- "For folks who say this approach seems really slow: it's slow because you're trying to extract ideas out of your human brain. And while this is happening, you've got AFK agents implementing your previous grilling sessions." — the **day shift / night shift** framing (attributed to "my friend Jaman on Twitter"; attribution unverified).
- On parallelism: he'd like "a team of agents", but "it's quite nice having these gaps… I get to do deep focus, then come back and do a big QA session." (The current 4-parallel harness partially delivers the team.)
- Crucial success factor, verbatim: **"making sure it runs tests and types on every single commit."**

## Key Takeaways

- The full mechanism is liftable: **queue = GitHub issues · sandbox = Docker + patch-extraction · loop = bounded iterations · gate = tests+typecheck per commit · exit = empty queue**.
- The evolution from video (1 issue at a time, monolithic prompt) to now (4-phase, 4-parallel, dependency-selected, two-phase closure) is itself instructive: **review became a phase, closure became a gate, labels became a dependency graph**.
- Bound your loops (10, not ∞) and let the queue, not the loop counter, define done.
- Cross-links: [[prd-and-issues-pipeline]] (what feeds the queue) · [[qa-plan-and-feedback-loop]] (what refills it) · [[../pocock-agentic-workflow/sandcastle-deep-dive]] (the package, mature form) · [[../multi-agent-orchestration/_index]] (orchestrator-worker patterns) · [[../harness-engineering/_index]].
