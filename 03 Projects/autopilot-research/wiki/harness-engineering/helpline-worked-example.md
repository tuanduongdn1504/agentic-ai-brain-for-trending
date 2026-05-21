# helpline — worked-example codebase for the Anthropic 7-component harness

> **Source repo:** [coleam00/helpline](https://github.com/coleam00/helpline) — Cole Medin (coleam00), Python, created 2026-05-19, last pushed 2026-05-20, no license declared, 2 stars at fetch (2026-05-21)
> **Companion to:** [[anthropic-large-codebases-anchor]] (Anthropic blog 2026-05-14 + Cole Medin video 2026-05-21)
> **Raw:** `raw/2026-05-19-coleam00-helpline-readme.md`
> **Compiled:** 2026-05-21

This article is the worked-example reference companion to the [[anthropic-large-codebases-anchor|Anthropic large-codebases anchor]]. Where the anchor article explains the 7-component framework conceptually, this article documents the **concrete implementation** in `coleam00/helpline` — a deliberately mid-sized realistic codebase (5 services + 2 shared packages monorepo) where every component is built and validated.

The repo is corpus-first as **the most complete worked example of the Anthropic harness in autopilot's coverage**. Per Cole Medin in the [companion video at `[01:07]`](https://www.youtube.com/watch?v=efRIrLXoOVA): *"I took all of their strategies and I built them into a demo codebase for this video. So not only are we covering the article, but we're also going to see concrete examples of all the strategies in action."*

---

## Repo positioning

### Helpline as a domain

Helpline is a **B2B helpdesk and customer-support platform** — a deliberately realistic mid-sized monorepo. The README's framing:

> *"It's the kind of mid-sized, multi-service codebase where an AI coding agent either pays for itself or quietly makes a mess: shared packages that everything imports, money rules that must never silently regress, a request gateway with its own conventions, and tests scattered across services."*

The repo is **not** a toy:
- 5 services (`api`, `auth`, `billing`, `notifications`, `search`) communicating over HTTP
- 2 shared packages (`packages/core` for domain models + error types; `packages/db` for connection + repositories)
- Cross-service integration tests in `tests/`
- Local-dev orchestration via `infra/docker-compose`
- Python toolchain: `uv` for dependency management, `pyright` for type-checking

This sizing is **load-bearing**: at this scale, the failure modes that the Anthropic blog warns about (CLAUDE.md bloat, wrong subdirectory scoping, lint timeouts on full-suite runs, unscoped skill activation, grep ambiguity, exploration-burns-context, etc.) all become measurable.

### Helpline as a teaching artifact

The repo has a **deliberate before/after structure in git history**:
- **Commit 1:** Helpline with NO AI Layer (pure application code + tests)
- **Commit 2:** Helpline with THE ENTIRE AI Layer added

This makes the repo readable as both:
- A "what does an AI Layer look like" reference
- A "what does adding an AI Layer to my existing codebase look like" tutorial

Cole's preferred way to operationalize this (`[25:33]–[26:07]`): clone helpline, point Claude Code at it, ask: *"Read AI-LAYER.md and the .claude/ folder in the Helpline repo. It is a worked example of the AI Layer from Anthropic's large-codebases article. Build a comparable AI Layer for THIS codebase — adapted to our structure and conventions."*

The `AI-LAYER.md` file in the repo (not fetched here but referenced) is **explicitly written for agent consumption** — an agent-readable map from each Anthropic article concept to the artifact that implements it, plus a 13/13 validator that proves every piece works end to end.

---

## The 7-component implementation map

| # | Component | Helpline file/dir | Notes on implementation |
|---|---|---|---|
| 1 | CLAUDE.md hierarchy | `CLAUDE.md` (root) + `*/CLAUDE.md` per service | Lean root + one per service/package, loaded additively per Anthropic Pattern 1. Root holds big-picture overview + general conventions + commands to run; subdirectory CLAUDE.md holds service-specific rules. |
| 2 | Hooks | `.claude/hooks/` | Two hooks: `SessionStart` orientation hook (loads git context — unstaged changes, recent commits) + self-improving `Stop` hook (runs separate Claude in headless mode at end of session, reviews session diff, proposes concrete CLAUDE.md edits as markdown). |
| 3 | Skills | `.claude/skills/` | Three skills: `billing-money-rules` (financial-correctness guardrails — scoped to `billing/` paths via `paths:` glob), `api-add-route` (workflow for adding new API endpoints — scoped to `services/api/`), `scoped-tests` (generic test-running scoped via paths). All use progressive disclosure into `references/`. |
| 4 | Plugins | `tooling/helpline-ai-layer/` | The portable AI Layer pieces bundled as a one-command-install Claude Code plugin. See [§ Plugin distribution](#plugin-distribution-the-portable-ai-layer) below. |
| 5 | LSP | `docs/lsp-setup.md` (configuration) | pyright + `pyright-langserver` for symbol-level Python navigation. Implemented as a setup doc rather than a runtime artifact — operators configure their IDE / Claude environment to consume the LSP. |
| 6 | MCP server | `tooling/mcp/` | Custom `codebase-search` MCP exposing AST-based `where_is` / `find_references` / `outline` tools. AST-aware (not just text-grep) — returns symbol-level results. Designed for layout-agnostic discovery (walks the repo to find source, doesn't hard-code paths). |
| 7 | Subagent | `.claude/agents/explorer.md` | Read-only `explorer` subagent — has NO write tools. Job: map a subsystem and report back. Implements the Anthropic Pattern 1 sub-rule "split exploration from editing" — main agent gets the summary, never burns its context on the exploration phase. |

---

## Component deep-dives

### 1. CLAUDE.md hierarchy

The implementation pattern (confirmed by Cole's walkthrough at `[05:33]–[07:53]`):

- **Root `CLAUDE.md`** — kept lean. Contains: codebase purpose (one paragraph), tech stack/architecture (a few bullets), general conventions and gotchas, commands for testing and dev-server.
- **Subdirectory `CLAUDE.md`** — per-service rules. Activated additively when Claude operates in or imports from that service. Examples: `services/api/CLAUDE.md` for API gateway conventions, `services/billing/CLAUDE.md` for money-handling conventions.

Cole's emphasized anti-pattern at `[05:08]–[05:24]`: **thousand-line CLAUDE.md files hurt performance.** The lean+layered structure mitigates by:
1. Root file stays under ~50 lines
2. Subdirectory files only loaded when relevant
3. Per-service conventions don't pollute root context

**Initialization pattern** (Cole at `[07:14]–`): when working on a specific service, `cd services/api && claude` initializes Claude Code with the API service as working directory. Claude automatically walks up the directory tree, loading both `services/api/CLAUDE.md` AND root `CLAUDE.md`. No context lost from root, but working scope bounded.

### 2. Hooks — the self-improving Stop hook

The most architecturally distinctive helpline component. Implementation flow (Cole walkthrough `[11:30]–[15:22]`):

1. **Stop hook fires** at end of every Claude Code turn
2. Hook spawns **separate Claude Code session in headless mode**
3. Headless session:
   - Reads the diff (changes made during the just-completed session)
   - Reads current root `CLAUDE.md`
   - Reads relevant subdirectory `CLAUDE.md` files (where the diff touched)
   - Decides: do conventions need updating to match the new behavior?
4. Hook outputs **markdown review document** (e.g., `claude-md-review.md`) with:
   - Reflection summary
   - Areas touched
   - Specific edit proposals (or "no changes needed" if conventions still hold)
5. **Operator reviews + actions on the proposals** (manual step — not auto-applied)

The pattern this implements: **continuous CLAUDE.md maintenance against drift**. As code evolves, conventions evolve; if CLAUDE.md goes stale, future sessions get wrong-shaped guidance. The Stop hook makes the drift detectable without operator vigilance.

Cole's demo at `[13:46]–[15:01]`:
- Demo 1: Small code change → Stop hook fires → review markdown says "no changes needed — adding a trial enum value follows the existing model-only convention" (correct conservatism)
- Demo 2: Bigger billing service change → Stop hook fires → review markdown recommends updating bullet 2 in `services/billing/CLAUDE.md` (correct detection)

The headless-Claude-reviewing-Claude pattern is **a recursive harness construct** — the harness extends itself with a meta-agent that maintains the harness. Compare with [[external|agent-development-lifecycle/langchain-interrupt-26-anchor|LangSmith Engine]] which does the same at framework level (proactive meta-agent on traces); helpline does it at file level (proactive meta-agent on diffs + CLAUDE.md).

### 3. Skills — glob-scoped via `paths:`

Each skill in helpline has a `paths:` field in its frontmatter that **restricts activation to specific code paths**. This is the load-bearing detail Cole emphasizes at `[16:42]–[17:11]`:

> *"This is what Anthropic talks about right here, we can make it so that skills can be scoped to specific paths. So they only activate in relevant parts of the codebase. Like we know that this process for adding API routes that we want to be very repeatable. It only applies when we're going to be reading and editing files in the API services directory."*

The three helpline skills:
- `billing-money-rules` — scoped to `services/billing/**`; activates only when billing files are in context
- `api-add-route` — scoped to `services/api/**`; activates only when adding routes to the API gateway
- `scoped-tests` — generic; demonstrates the path-scoping pattern

**Skills vs CLAUDE.md disambiguation** (Cole `[17:32]–[17:56]`):
- CLAUDE.md = **rules / conventions** (what must / must not be done)
- Skills = **workflows** (how to do a specific recurring task)

Both can be path-scoped; the distinguishing feature is whether the content is declarative (CLAUDE.md) or procedural (skills). Cole notes there's overlap and ultimately the **more important thing is scoping context to where it matters**.

### 4. Plugin distribution — the portable AI Layer

The helpline plugin is corpus-first as **a complete-AI-Layer-in-a-box distribution pattern**. Install:

```bash
/plugin marketplace add /path/to/helpline/tooling
/plugin install helpline-ai-layer@helpline-tooling
```

What the plugin ships (the **layout-agnostic** pieces of the AI Layer — i.e., the parts that work in ANY repo):

| Plugin piece | Why it travels |
|---|---|
| **Self-improving Stop hook** | Uses operator's CLAUDE.md hierarchy structure — doesn't care about content |
| **`explorer` read-only subagent** | Generic subsystem-mapper — works on any directory layout |
| **`codebase-search` MCP** | AST-based discovery walks the repo automatically — discovers source, doesn't hard-code paths |
| **Generic `scoped-tests` skill** | Pattern template; demonstrates `paths:` scoping |

What the plugin **doesn't** ship (the **repo-specific** pieces operators rebuild):

- The CLAUDE.md files themselves (your conventions)
- Domain-specific skills (`billing-money-rules`, `api-add-route`, etc. are templates to imitate, not copy)
- The LSP config (configure for your language toolchain)

This split — **portable mechanism vs reproducible pattern** — is exactly the architecturally-clean answer to "how do I distribute an AI Layer?" Mechanisms travel; conventions are local.

Compare with [[external|claudekit/_index|ClaudeKit]] (vividkit.dev) which distributes a similar plugin-based AI Layer at framework scale. Both are valid; ClaudeKit is more opinionated (50+ commands, multi-provider routing); helpline plugin is more minimal (4 portable pieces, sticks tightly to Anthropic 7-component baseline).

### 5. LSP — pyright integration

Helpline configures `pyright-langserver` as the LSP provider for symbol-level navigation. The setup lives in `docs/lsp-setup.md` (not the runtime — the runtime is the operator's IDE config).

Anthropic's argument for LSP (blog text): *"Grep returns thousands of matches; LSP returns only relevant symbols, filtering before Claude reads anything."* Cole reinforces at `[20:55]–[21:13]`:

> *"For massive codebases once you get like into the six digits for lines of code you need something like this because Grep by itself is going to be slow and really token inefficient as you're trying to navigate through a codebase."*

The LSP-via-MCP integration is technically distinct from raw LSP support. Cole's pattern: build a custom MCP server (`codebase-search`) that **wraps the LSP** and exposes its capabilities as Claude-callable tools. This makes LSP queryable from Claude Code's standard tool-call mechanism without requiring Claude itself to speak LSP.

### 6. MCP — codebase-search

Three tools the helpline `codebase-search` MCP exposes:

- `where_is <symbol>` — find the definition of a symbol
- `find_references <symbol>` — find all places a symbol is referenced
- `outline <file>` — get an AST-based outline of a file's symbols

Cole's demo at `[19:42]–[20:55]`: prompt "find every place that monthly total cents is referenced in this repo" + explicit "do not use grep, use symbol-level approach" → MCP returns 1 definition + 2 references using `where_is` + `find_references`.

The MCP is **layout-agnostic** — discovers source by walking the repo, doesn't hard-code service paths. Same plugin works in any repo regardless of directory layout.

### 7. Subagent — `explorer` (read-only)

Cole's framing of subagent value `[22:38]–[23:15]`:

> *"The advice Anthropic has here is simple, but still really powerful. We want to use subagents to split exploration from editing. The idea with a sub agent is that we send in a task ... and it runs with its own context window. It does all the analysis it needs to and then it returns a summary back to our primary cloud code session to reason about and action on."*

`explorer` has explicitly **no write tools**. Job: map subsystems, report back. Why this matters:
- Exploration tasks can burn 100K+ tokens reading files
- If main session does the exploration, by the time editing starts, context is bloated
- Read-only subagent isolates the exploration cost in its own context window
- Main session receives the summary (~1-5K tokens), preserves its budget for editing

The read-only constraint is **architecturally critical**: if the subagent had write tools, it would be tempted to start editing during exploration, defeating the split. Cole's helpline implementation hard-removes write tools at the subagent definition level.

Compare with [[personal-repo-router-multimodel|howznguyen's parallel-research-then-implement pattern]]: same architectural move (read-only sub-agents for research) but achieved via runtime cross-vendor routing instead of subagent-definition tool-restriction. Two valid paths to the same architecture.

---

## What helpline is NOT

Surgical honesty per Storm Bear convention: the repo at fetch time has notable limitations.

| Limitation | Implication |
|---|---|
| **No declared license** (as of 2026-05-21 fetch) | Operators cannot legally know terms of reuse. Cole's "take this to your codebase" instruction assumes implicit permission; legally ambiguous. Recommend operator pilot adoption only after license declared. |
| **2 stars / 0 forks** at fetch | Very new (created 2026-05-19); insufficient social validation. Code quality not yet community-vetted. |
| **No declared topics or wiki on GitHub** | Discoverability low; relies on Cole's YouTube channel for traffic. |
| **Python-specific** | LSP and MCP code-search are pyright-bound. Operators in non-Python stacks must port the LSP/MCP pieces. Pattern transfers; implementation doesn't. |
| **Mid-sized, not large** | Helpline is ~10K LOC equivalent; Anthropic blog targets multi-million-LOC monorepos. Pattern is valid at multi-million scale per Anthropic claims, but helpline doesn't prove it. |

---

## Pilot-readiness assessment

This repo is **Tier-A operationally pilotable** for individual / small-team adopters with these caveats:

- Setup time: ~1-2 hours (clone, run validator, inspect `.claude/` structure, then either (a) install plugin in own repo or (b) point Claude Code at helpline and have it bootstrap your codebase)
- Reversibility: full (delete `.claude/` from your repo + uninstall plugin)
- Pre-requisites: Claude Code installed; Python `uv` for running helpline's own tests + validator
- License gate: **decide whether to wait for license declaration before adoption**

Recommended pilot protocol:
1. Clone helpline; read README + AI-LAYER.md
2. Run validator (`uv run --extra dev python tooling/validate/validate_all.py`) — expect 13/13 pass
3. Install plugin in a sandbox project (NOT production codebase first)
4. Operate Claude Code in sandbox with plugin for 1 week
5. Measure: did Stop hook propose accurate CLAUDE.md updates? did explorer subagent reduce context burn?
6. Write up findings in `04 Reviews/(C) YYYY-MM-DD-helpline-plugin-pilot.md`

---

## Open questions

1. **What does the `AI-LAYER.md` file actually contain?** README references it as the "agent-readable map" but we haven't fetched it directly. Follow-up fetch warranted to validate the agent-bootstrapping flow Cole describes.
2. **How does the validator (`validate_all.py`) actually validate "every piece works end to end"?** README claims 13/13 — what are the 13 checks? Operational insight for building similar validators.
3. **Is the Stop hook's headless-Claude-review cost-justifiable at high session volume?** Each Stop fires a full Claude session; at 20 sessions/day per dev × 100 devs, that's 2000 review-sessions/day. Quantified cost-benefit study would settle.
4. **Does the `explorer` subagent's read-only constraint create blind spots?** If exploration discovers code that should be edited but the subagent has no write tools, the main agent gets the summary but must re-read context to edit — partial loss of token savings.
5. **Will the plugin work in Claude Code clones / forks** (e.g., [[external|claude-code-clones/_index|OpenClaw / Hermes]])? Plugin format may be Claude-Code-specific.

---

## Cross-links

- [[anthropic-large-codebases-anchor]] — primary anchor article this is companion to
- [[_index|harness-engineering index]]
- [[personal-repo-overview]] — individual-scale baseline this implementation maps to
- [[personal-repo-router-multimodel]] — howznguyen's parallel-research pattern; both repos demonstrate the read-only subagent architectural move
- [[external|claudekit/_index]] — ClaudeKit framework as plugin-based AI Layer alternative at framework scale
- [[external|claude-code-hooks/_index]] — Anthropic Hooks component prior coverage
- [[external|claude-md-12-rules/_index]] — Mnilax 12-rule template operates within helpline's CLAUDE.md hierarchy pattern
- [[research-roadmap]] — `AI-LAYER.md` content + validator details are candidates for follow-up ingest
