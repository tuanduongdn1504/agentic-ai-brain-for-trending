# Symphony architecture — triangulated across 6 sources

> **Why this article exists:** Lopopolo's Symphony is described in the talk + podcast (Apr 2026) but absent from the Feb blog (see [[blog-talk-evolution#3]]). OpenAI published an "open-source Symphony spec" blog post on Apr 27, 2026 — but that page's backend gates fail Tier 1 + Tier 2 bypass (see `output/bypass-attempts.md`). This article triangulates Symphony's architecture from 3 community implementations (Elixir, Go, Rust) plus Lopopolo's spoken descriptions. **Three independent reproductions = stronger evidence than the single missing spec.**
>
> **Sources triangulated** (NotebookLM `d772d58b-...`):
> - **OpenAI primary** (Sources 1-3): YouTube talk · Latent Space podcast · OpenAI blog (Feb 2026, no Symphony mention)
> - **Community implementations** (Sources 4-6):
>   - [ACNoonan/symphony-restate](https://github.com/ACNoonan/symphony-restate) — Elixir + Restate + Linear (closest to OpenAI's stated stack)
>   - [ryanjdillon/symphony](https://github.com/ryanjdillon/symphony) — Go, multi-agent (Codex + Claude Code), explicit "harness-engineering" topic tag
>   - [howardpen9/symphony-rs](https://github.com/howardpen9/symphony-rs) — Rust rewrite, CLI focus
> - **Synthesis raw:** `raw/2026-05-09-symphony-community-synthesis.md`

## What Symphony does (consensus across all sources)

A **long-running, agent-agnostic orchestration service** that:
1. Polls **Linear** (issue tracker) for issues in `Todo` / `In Progress` states
2. **Claims** issues to prevent duplicate dispatch
3. Loads a `WORKFLOW.md` template (prompt + YAML frontmatter, rendered via Liquid or similar)
4. Spawns agents in **isolated git worktrees** via lifecycle hooks
5. Provides **Skills** (repo-embedded scripts) for environment-specific actions (launch app, query DB, drive browser)
6. Runs a **Ralph Loop** — agents iterate self-correcting until spec satisfied
7. Uses **GitHub CLI (`gh`)** to open PRs, respond to feedback, merge on green CI

## Core components

| Component | Role | OpenAI? | ACNoonan (Elixir/Restate) | Ryanjdillon (Go) | Howardpen9 (Rust) |
|---|---|---|---|---|---|
| Orchestrator/scheduler | Polling, claim management, state reconciliation | ✓ | ✓ (Restate-backed) | ✓ (Go service) | ✓ (Rust CLI service) |
| Agent-agnostic runner | Pluggable model interface (Codex, Claude Code, GPT-5.x) | ✓ | ✓ | ✓ (multi-agent explicit) | ✓ (Codex-first) |
| Workspace manager | Isolated git worktrees, lifecycle hooks | ✓ | ✓ | ✓ (SSH remote workers — distributed) | ✓ |
| Codex App-Server client | stdio protocol for orchestrator↔agent | ✓ | ✓ | ✓ | ✓ |
| Real-time dashboard | UI for sessions, token usage, retries | ? (not detailed) | Phoenix LiveView | React (embedded in binary) | not yet |

## Stack choices — convergence + divergence

**Convergence (all 4 implementations):**
- Linear (issue tracker) via GraphQL API
- GitHub CLI for PR ops
- Some form of OpenTelemetry / observability
- Skills as repo-embedded scripts
- Ralph Loop self-correcting iteration pattern

**Divergence — durable execution:**
- **OpenAI's Symphony:** in-memory state, no recovery on node death (Lopopolo: "exact in-memory scheduler state is not restored upon restart")
- **ACNoonan's Restate version:** explicitly addresses this with Restate's durable execution → if a node dies mid-flow, every issue resumes on a different node without losing the conversation journal or creating "double-dispatches". **This is a community improvement over the OpenAI original.**

**Divergence — distribution model:**
- **OpenAI's Symphony:** local worktrees on developer box (single-node oriented)
- **Ryanjdillon's Go version:** SSH remote workers with least-loaded host selection + health tracking — distributed across a fleet

**Divergence — language:**
- OpenAI: Elixir/BEAM (process supervision + GenServers as load-bearing primitives per Lopopolo)
- Community: ports show concepts are NOT Elixir-specific — Rust (typed safety + CLI perf) and Go (operational simplicity) reproduce the same architecture
- This **weakens** Lopopolo's claim that Elixir/Beam is uniquely suited (see [[core-claims#5]] tension; see [[open-questions#6]] language-specific agent legibility)

## Lopopolo features MISSING from community implementations

These are emphasized in Sources 1-3 but absent from Sources 4-6:

1. **Visual perception via CDP** — Lopopolo: agents "see" the UI through Chrome DevTools Protocol + rasterization. Community: text-only integrations (Linear API, filesystem). Possible reasons: harder to implement; lower ROI for community use cases.
2. **"Editor ban" enforcement** — Lopopolo's culture forbids human direct edits. Community tools are "for humans to manage work" — they assist, don't enforce.
3. **Post-merge-only human review** — Lopopolo: humans don't review pre-merge. Community: still operate within standard PR workflows where humans gate merges.

These gaps reveal the OpenAI internal stack is **organizationally + culturally distinct** from the architectural reproduction. Architecture is portable; the org culture isn't.

## Community-added capabilities NOT in Lopopolo's descriptions

1. **Cold-path conversation seeding** (ACNoonan) — fresh agent session on a new node rehydrates entire thread context from durable state
2. **Multi-workflow hot-reload** (ryanjdillon) — watches a directory to dynamically add/remove `WORKFLOW.md` files without restarting service
3. **Kubernetes / FluxCD / Traefik manifests** — explicit cloud-native deployment patterns; community treats Symphony as a "single-replica Deployment"
4. **Mutation guards + tool validation** (ryanjdillon) — explicit `ToolHandler` interface with single-operation validation for `linear_graphql` to prevent unauthorized destructive actions

These are **operational hardening** the community needed to run Symphony as production infrastructure — beyond what OpenAI's research-experiment write-ups document.

## Falsifier check — claim #4 (Symphony throughput)

[[core-claims#4|Claim #4]]: "Symphony orchestration increases output from 3.5 PRs/day baseline to **5-10 PRs/day per engineer**."

**Status after community ingest:** ❌ **NOT INDEPENDENTLY CORROBORATED** as of 2026-05-09.

None of the 3 community implementations document throughput benchmarks comparable to Lopopolo's claim:
- ACNoonan/symphony-restate: explicitly **"pre-alpha"** status (May 2026) — too early to measure throughput
- howardpen9/symphony-rs: status documented as `cargo test` + `cargo run -- validate` smoke checks; no longitudinal data
- ryanjdillon/symphony: 117 tests covering workspace sanitization + orchestrator scheduling; OpenTelemetry metrics infrastructure exists but no sample throughput data published

Community focus is on **architectural invariants** (state survival under node death, idempotent claim handling, durable execution) NOT on **operational velocity claims**. Lopopolo's 5-10 PRs/day remains an **internal-OpenAI-only number**.

**What this means for the research thread:**
- Claim #4 should be marked `unverified externally` until community implementations reach production maturity OR a third party publishes comparable benchmarks
- The architectural pattern is reproducible; the throughput is not yet
- This is exactly the falsification-check this article was structured to enable (see [[research-roadmap]] criterion A)

## What we still don't know about Symphony

- **OpenAI's actual Symphony spec content** — `openai.com/index/open-source-codex-orchestration-symphony/` requires bypass beyond Tier 2; deferred. Community implementations reference a `SPEC.md` they followed but don't reproduce it verbatim.
- **Throughput at production scale** — see falsifier check above
- **GPT-5.2 vs Claude Code performance under Symphony** — community impl supports both; no comparative data
- **Migration path from non-Symphony to Symphony** — community repos all start fresh; no incremental-adoption playbook

These belong in [[open-questions]] — adding when this article gets cross-linked back.

## How to extend

When future ingests touch Symphony architecture:
1. Add `### Update YYYY-MM-DD` block under the relevant Convergence/Divergence/Missing/Added section
2. If a 4th community implementation surfaces, add row to the Core Components table
3. If throughput data emerges (community OR third-party benchmark), update Falsifier check section — change status from `NOT INDEPENDENTLY CORROBORATED` to `partial` or `confirmed`
4. If OpenAI's spec page becomes accessible (cache change, Wayback snapshot, mirror), append spec-vs-community-divergence section
