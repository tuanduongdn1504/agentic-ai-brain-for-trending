# (C) Cluster 1 — README + VISION + positioning

## Source files

| File | Size | Purpose |
|------|------|---------|
| README.md | 873 lines (~37 KB) | User-facing overview + commands + architecture summary + bundled extensions/agents |
| VISION.md | 37 lines (~2.5 KB) | 5 principles + "what we won't accept" + GSD-1 relationship |

## Headline positioning

**Tagline (banner)**: *"The evolution of [Get Shit Done](https://github.com/gsd-build/get-shit-done) — now a real coding agent."*

**Anti-positioning vs GSD-1** (verbatim, README line 14-16):

> The original GSD went viral as a prompt framework for Claude Code. It worked, but it was fighting the tool — injecting prompts through slash commands, hoping the LLM would follow instructions, with no actual control over context windows, sessions, or execution.
>
> This version is different. GSD is now a standalone CLI built on the [Pi SDK](https://github.com/badlogic/pi-mono), which gives it direct TypeScript access to the agent harness itself. That means GSD can actually _do_ what v1 could only _ask_ the LLM to do: clear context between tasks, inject exactly the right files at dispatch time, manage git branches, track cost and tokens, detect stuck loops, recover from crashes, and auto-advance through an entire milestone without human intervention.

**One-liner**: "One command. Walk away. Come back to a built project with clean git history."

## Hierarchical work model (corpus-first explicit at T1)

```
Milestone  →  a shippable version (4-10 slices)
  Slice    →  one demoable vertical capability (1-7 tasks)
    Task   →  one context-window-sized unit of work
```

**Iron rule**: *"a task must fit in one context window. If it can't, it's two tasks."*

**Loop**: `Plan (with integrated research) → Execute (per task) → Complete → Reassess Roadmap → Next Slice → ... → Validate Milestone → Complete Milestone`

## Two execution modes

| Mode | Command | Behavior |
|------|---------|----------|
| **Auto** | `/gsd auto` | State machine reads `.gsd/STATE.md`, dispatches next unit, fresh agent session per task, advances autonomously through entire milestone |
| **Step** | `/gsd` or `/gsd next` | Same state machine but pauses between units with wizard showing what completed and what's next |

## What changed from v1 (verbatim README table)

|                      | v1 (Prompt Framework)        | v2 (Agent Application)                                  |
| -------------------- | ---------------------------- | ------------------------------------------------------- |
| Runtime              | Claude Code slash commands   | Standalone CLI via Pi SDK                               |
| Context management   | Hope the LLM doesn't fill up | Fresh session per task, programmatic                    |
| Auto mode            | LLM self-loop                | State machine reading `.gsd/` files                     |
| Crash recovery       | None                         | Lock files + session forensics                          |
| Git strategy         | LLM writes git commands      | Worktree isolation, sequential commits, squash merge    |
| Cost tracking        | None                         | Per-unit token/cost ledger with dashboard               |
| Stuck detection      | None                         | Retry once, then stop with diagnostics                  |
| Timeout supervision  | None                         | Soft/idle/hard timeouts with recovery steering          |
| Context injection    | "Read this file"             | Pre-inlined into dispatch prompt                        |
| Roadmap reassessment | Manual                       | Automatic after each slice completes                    |
| Skill discovery      | None                         | Auto-detect and install relevant skills during research |
| Verification         | Manual                       | Automated verification commands with auto-fix retries   |
| Reporting            | None                         | Self-contained HTML reports with metrics and dep graphs |
| Parallel execution   | None                         | Multi-worker parallel milestone orchestration           |

## VISION.md 5 principles (verbatim)

1. **Extension-first** — *"If it can be an extension, it should be. Core stays lean. New capabilities belong in extensions, skills, and plugins unless they fundamentally require core integration."*
2. **Simplicity over abstraction** — *"The codebase was aggressively cleaned up. Every line earns its place. Don't add helpers, utilities, or abstractions unless they eliminate real duplication or solve a real problem. Three similar lines of code is better than a premature abstraction."*
3. **Tests are the contract** — *"If you change behavior, the tests tell you what you broke. Write tests for new behavior. Trust the test suite."*
4. **Ship fast, fix fast** — *"Get it out, iterate quickly, don't let perfect be the enemy of good. Every release should work, but we'd rather ship and patch than delay and accumulate."*
5. **Provider-agnostic** — *"GSD works with any LLM provider. No architectural decisions should privilege one provider over another."*

**5 PR rejection categories**: enterprise patterns / framework swaps / cosmetic refactors / complexity-without-user-value / heavy-orchestration-layers.

## GSD-1 → GSD-2 relationship (VISION.md verbatim)

> GSD-2 is the future. GSD-1 continues to serve its community but GSD-2 is where active development, new features, and architectural investment happen. The goal is to eventually migrate GSD-1 users to GSD-2.

**Migration tooling** (README): `/gsd migrate` parses `.planning` directories from GSD-1, maps phases→slices/plans→tasks/milestones→milestones, preserves completion state, consolidates research files, supports format variations (milestone-sectioned roadmaps with `<details>` blocks, bold phase entries, decimal phase numbering, duplicate phase numbers).

## Cross-corpus references in README

| Reference | Type | Implication |
|---|---|---|
| **[Pi SDK](https://github.com/badlogic/pi-mono)** | Direct dependency citation | Pattern #57 5th/6th data point — Mario Zechner's pi-mono v36 wiki subject explicitly cited as foundation |
| **[Get Shit Done](https://github.com/gsd-build/get-shit-done)** | Predecessor/lineage | Pattern #58 sub-variant 58e successor-repo-not-rename observation |
| **[RTK](https://github.com/rtk-ai/rtk)** | Managed third-party binary | Corpus-first managed-third-party-binary-with-telemetry-discipline observation (Pattern #2 + #66 sub-observations) |
| **GSD2 Config Utility** (jeremymcs/gsd2-config) | Ecosystem add-on | Pattern #17 variant 1 strengthening |
| **Star History** (star-history.com) | Vanity link | Standard |
| **Discord** (discord.com/invite/nKXTsAcmbT) | Community | Pattern #18 Western-community-platform |
| **$GSD Token Dexscreener** | Crypto monetization | Pattern #37 Crypto-Donation-Funded 2nd data point |

## What's New in v2.78 (5 categories, verbatim from README)

| Category | Key items |
|---|---|
| **Worktree Lifecycle & Forensics** | Slice-cadence worktree collapse / Worktree telemetry events / `/gsd forensics` worktree section / Worktree-aware canonical milestone root / Bootstrap orphan audit |
| **Auto Pipeline & Component System** | Unified component system (skills/agents/pipelines/marketplace) / UnitContextManifest v2 typed contract / Composer migration phase 3 / Milestone scope classifier + pipeline variants / Per-unit-type skill manifest resolver / **Single-writer-v3 control plane** / Opt-in `reassess-roadmap` |
| **Extensions Framework** | Extension lifecycle commands (install/update/uninstall/list/info/validate) / Topological extension load order (Kahn's algorithm) / cmux ↔ gsd decoupling / **Extracted `@gsd-extensions/google-search` workspace** (first reference extension carved out) |
| **Models, Agent, and UX** | GPT-5.5 Codex support (incl. `xhigh` thinking) / Auth mode in `/model` / Permission granularity picker / Headless auto default → `bypassPermissions` / `skillFilter` for system prompts / Visual postinstall / PR-risk verification |
| **Reliability & Safety** | Major git-safety pass (TOCTOU ancestry guard / atomic sync-lock / `.git/index.lock` 5-min age guard / env stripping / rebase abort) / Atomic `.gsd/` state writes / Compaction correctness / Write-gate / Auto state machine / Slice + crash recovery / Empty-turn recovery |

## Build commands ecosystem hint

Root `package.json` `scripts` section reveals build dependency chain:
```
build:pi → builds pi-tui + pi-ai + pi-agent-core + pi-coding-agent + native
build:rpc-client → @gsd-build/rpc-client
build:mcp-server → @gsd-build/mcp-server
build:core → orchestrates all above + tsc + copy-resources + copy-themes + copy-export-html
build → build:core + build-web-if-stale (web/ workspace)
```

This confirms gsd-2's architecture: **Pi SDK foundation (vendored) + native Rust + RPC client + MCP server + core CLI + web UI**.

## Dual-naming bin convention

Root `package.json` `bin` field:
```json
{
  "gsd": "dist/loader.js",
  "gsd-cli": "dist/loader.js",
  "gsd-pi": "scripts/install.js"
}
```

3 bin aliases: `gsd` (primary) + `gsd-cli` (alias) + `gsd-pi` (installer-named-after-npm-package). **Not Pattern #58 sub-variant 58c** (omo's repo→npm name mismatch); rather a 3-alias-from-single-codebase convention.

## Cross-references

- See `(C) Cluster 2` for architecture deep-dive on the 8-package monorepo + Pi SDK vendoring evidence
- See `(C) Cluster 3` for governance + extensions + commercial-funnel analysis
- See `(C) Entity 1` for core product synthesis
