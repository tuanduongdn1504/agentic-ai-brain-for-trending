# (C) Cluster 2 — Architecture + 8-package monorepo + Pi-SDK vendoring

## Source files

| Source | Use |
|---|---|
| Root `package.json` | Workspaces declaration + bin + scripts |
| 8 `packages/*/package.json` | Per-package manifest evidence |
| README "Architecture" section (lines 757-790) | Author-stated architecture |
| `src/cli.ts` (referenced) | Entry-point routing |
| `src/loader.ts` (referenced) | Two-file loader pattern |

## Workspace structure

```
gsd-2/
├── packages/                       (8 npm workspaces)
│   ├── daemon/                     @gsd-build/daemon — background process for project monitoring + Discord
│   ├── mcp-server/                 @gsd-build/mcp-server — MCP server exposing GSD orchestration tools
│   ├── native/                     @gsd/native — Native Rust bindings via N-API
│   ├── pi-agent-core/              @gsd/pi-agent-core — vendored from pi-mono ⭐
│   ├── pi-ai/                      @gsd/pi-ai — vendored from pi-mono ⭐
│   ├── pi-coding-agent/            @gsd/pi-coding-agent — vendored from pi-mono ⭐
│   ├── pi-tui/                     @gsd/pi-tui — vendored from pi-mono ⭐
│   └── rpc-client/                 @gsd-build/rpc-client — RPC client
├── studio/                         @gsd/studio — Electron + React 19 + Zustand desktop app (private; v0.0.0)
├── extensions/                     1 extracted workspace
│   └── google-search/              @gsd-extensions/google-search — first reference extension carved out of core (v2.78)
├── src/                            CLI core (~30 .ts files at root)
│   ├── cli.ts                      Wires SDK managers + extensions + InteractiveMode
│   ├── loader.ts                   Sets PI_PACKAGE_DIR + GSD env vars + dynamic-imports cli.ts
│   ├── headless.ts                 Headless orchestrator
│   ├── onboarding.ts               First-run setup wizard
│   └── resources/
│       ├── extensions/             21 in-source bundled extensions (gsd core + 20 supporting)
│       ├── agents/                 13 specialist subagent .md files
│       ├── skills/                 35 skill packages
│       └── GSD-WORKFLOW.md         Manual bootstrap protocol
├── native/                         Cargo.toml + Rust crates for performance modules
├── docs/                           1.7 MB documentation
│   ├── user-docs/                  16+ user-facing guides
│   ├── dev/                        ADRs (ADR-001/003/etc.) + architecture + PRDs
│   ├── extension-sdk/              Extension authoring guide
│   └── zh-CN/                      Chinese localization (scope unknown)
├── gsd-orchestrator/               SKILL.md + workflows + templates + references
├── mintlify-docs/                  152 KB Mintlify documentation site
├── pkg/                            Shim directory — PI_PACKAGE_DIR points here
├── scripts/                        Build + tooling scripts
├── tests/                          44 KB test files
├── docker/                         Docker sandbox configuration
├── vscode-extension/               VS Code chat participant + sidebar dashboard
├── web/                            Web UI workspace (browser-based project management)
├── README.md / VISION.md / CONTRIBUTING.md / CHANGELOG.md / LICENSE
├── package.json                    Root workspace declaration
├── tsconfig.json / tsconfig.{extensions,resources,test}.json
└── Dockerfile
```

## Pi SDK vendoring — corpus-first explicit evidence

**4 of 8 packages** are vendored from Mario Zechner's pi-mono v36 wiki subject. Each `package.json` description verbatim:

| Package | Description (verbatim) |
|---|---|
| `@gsd/pi-coding-agent` | `"Coding agent CLI (vendored from pi-mono)"` |
| `@gsd/pi-ai` | `"Unified LLM API (vendored from pi-mono)"` |
| `@gsd/pi-agent-core` | `"General-purpose agent core (vendored from pi-mono)"` |
| `@gsd/pi-tui` | `"Terminal User Interface library (vendored from pi-mono)"` |

**Pattern #57 implications**: This is the **strongest possible Pattern #57 evidence** in 54 corpus wikis. Prior data points were narrative citations or aggregator listings. gsd-2 puts the vendoring acknowledgment in **machine-readable package.json metadata** — searchable, deterministic, unambiguous.

**Versioning lockstep**: All 4 vendored pi-* packages versioned `2.78.1` (lockstep with gsd-2 root). pi-mono v36 was at v0.69.0 at probe; gsd-2 at 2.78.1 has diverged significantly via in-tree maintenance.

**Vendoring vs dependency**: gsd-2 does NOT install `@mariozechner/pi-coding-agent` from npm; it ships its own copy under `@gsd/*` scope. Trade-off: faster iteration + isolation from upstream breaking changes / cost: divergence from upstream + maintenance burden + supply-chain question (which version of pi-mono was forked + when?).

**Cross-corpus pi-mono v36 comparison** (per Storm Bear v36 wiki):

| pi-mono v36 (7 packages) | gsd-2 v54 (4 vendored) | Status |
|---|---|---|
| pi-coding-agent | @gsd/pi-coding-agent | ✅ vendored |
| pi-ai | @gsd/pi-ai | ✅ vendored |
| pi-agent-core | @gsd/pi-agent-core | ✅ vendored |
| pi-tui | @gsd/pi-tui | ✅ vendored |
| pi-web-ui | — | ❌ not vendored (gsd-2 has separate `web/` workspace) |
| pi-mom | — | ❌ not vendored (Slack bot — not gsd-2 concern) |
| pi-pods | — | ❌ not vendored (GPU pod CLI — not gsd-2 concern) |

Plus gsd-2 adds **NEW capabilities** beyond pi-mono:
- `@gsd/native` Rust N-API bindings
- `@gsd-build/daemon` background process + Discord
- `@gsd-build/mcp-server` MCP server exposing GSD orchestration tools (NOT pi-mono's bidirectional MCP — different role)
- `@gsd-build/rpc-client` RPC for VS Code extension
- `@gsd/studio` Electron desktop app (private workspace)

## Two-file loader pattern (corpus-first explicit at T1)

Per README architecture section verbatim:

> **`pkg/` shim directory** — `PI_PACKAGE_DIR` points here (not project root) to avoid Pi's theme resolution collision with our `src/` directory. Contains only `piConfig` and theme assets.
>
> **Two-file loader pattern** — `loader.ts` sets all env vars with zero SDK imports, then dynamic-imports `cli.ts` which does static SDK imports. This ensures `PI_PACKAGE_DIR` is set before any SDK code evaluates.
>
> **Always-overwrite sync** — `npm update -g` takes effect immediately. Bundled extensions and agents are synced to `~/.gsd/agent/` on every launch, not just first run.
>
> **State lives on disk** — `.gsd/` is the source of truth. Auto mode reads it, writes it, and advances based on what it finds. No in-memory state survives across sessions.

This is **architectural pattern reference** for Storm Bear vault routine v2.2 evolution (see `(C) Entity 4` for Storm Bear meta).

## State-on-disk architecture (`.gsd/` directory contract)

**Auto mode** is a state machine driven by files. Per README:

| Artifact | Purpose |
|---|---|
| `.gsd/STATE.md` | Quick-glance dashboard (regenerable) |
| `.gsd/PROJECT.md` | Living doc — what the project is right now |
| `.gsd/DECISIONS.md` | Append-only register of architectural decisions |
| `.gsd/KNOWLEDGE.md` | Cross-session rules, patterns, lessons learned |
| `.gsd/RUNTIME.md` | Runtime context — API endpoints, env vars, services (v2.39+) |
| `.gsd/M001-ROADMAP.md` | Milestone plan with slice checkboxes |
| `.gsd/M001-CONTEXT.md` | User decisions from discuss phase |
| `.gsd/M001-RESEARCH.md` | Codebase + ecosystem research |
| `.gsd/S01-PLAN.md` | Slice task decomposition |
| `.gsd/T01-PLAN.md` | Individual task plan |
| `.gsd/T01-SUMMARY.md` | What happened (YAML frontmatter + narrative) |
| `.gsd/S01-UAT.md` | Human test script |
| `.gsd/auto.lock` | Crash-detection PID lock (per session) |
| `.gsd/gsd.db` + WAL | SQLite checkpoint state + forensics |
| `.gsd/journal/` | Daily-rotated structured event journal |
| `.gsd/event-log.jsonl` | Workflow event stream |
| `.gsd/worktrees/` | Git worktree working copies |
| `.gsd/parallel/` | Multi-worker IPC + status |
| `.gsd/reports/` | Auto-generated HTML reports |

**Pattern observation**: gsd-2's `.gsd/` directory contract is **strongest at-T1 example of state-on-disk discipline** in corpus. Prior precedents: vault `02 Wiki/` (Markdown-as-source-truth) but no formal state.md / no event log / no SQLite checkpoint.

## 24 bundled extensions (loaded automatically)

| # | Extension | Purpose |
|---|---|---|
| 1 | **GSD** | Core workflow engine, auto mode, commands, dashboard |
| 2 | **Browser Tools** | Playwright-based browser with form intelligence + intent-ranked element finding + semantic actions + PDF export + session state persistence + network mocking + device emulation + structured extraction + visual diffing + region zoom + test code generation + prompt injection detection |
| 3 | **Search the Web** | Brave Search, Tavily, or Jina page extraction |
| 4 | **Google Search** | Gemini-powered web search (extracted to `@gsd-extensions/google-search` v2.78) |
| 5 | **Context7** | Up-to-date library/framework documentation |
| 6 | **Background Shell** | Long-running process management with readiness detection |
| 7 | **Async Jobs** | Background bash with job tracking + cancellation |
| 8 | **Subagent** | Delegated tasks with isolated context windows |
| 9 | **GitHub** | Full-suite GitHub issues + PR management via `/gh` |
| 10 | **Mac Tools** | macOS native app automation via Accessibility APIs |
| 11 | **MCP Client** | Native MCP server integration via `@modelcontextprotocol/sdk` |
| 12 | **Voice** | Real-time speech-to-text (macOS, Linux Ubuntu 22.04+) |
| 13 | **Slash Commands** | Custom command creation |
| 14 | **Ask User Questions** | Structured user input with single/multi-select |
| 15 | **Secure Env Collect** | Masked secret collection without manual .env editing |
| 16 | **Remote Questions** | Route decisions to Slack/Discord in headless/CI mode |
| 17 | **Universal Config** | Discover + import MCP servers + rules from other AI coding tools |
| 18 | **AWS Auth** | Automatic Bedrock credential refresh |
| 19 | **Ollama** | First-class local LLM support |
| 20 | **Claude Code CLI** | External provider extension for Claude Code CLI |
| 21 | **cmux** | Claude multiplexer integration — desktop notifications + sidebar metadata + visual subagent splits |
| 22 | **GitHub Sync** | Auto-sync milestones to GitHub Issues + PRs + Milestones |
| 23 | **LSP** | Language Server Protocol — diagnostics + definitions + references + hover + rename |
| 24 | **TTSR** | Tool-triggered system rules — conditional context injection based on tool usage |

## 13 bundled agents (specialist subagents in `src/resources/agents/`)

`debugger / doc-writer / git-ops / javascript-pro / planner / refactorer / researcher / reviewer / scout / security / tester / typescript-pro / worker` (verified via `ls`).

README cites only 5: Scout / Researcher / Worker / JavaScript Pro / TypeScript Pro. **Documentation drift**: 13 agent .md files exist on disk; README under-counts at 5. Likely 8 specialist subagents added during component-system migration (v2.72 mentioned "8 specialist subagents") and not yet re-documented.

## 35 skills (`src/resources/skills/`)

Skill catalog: `accessibility / agent-browser / api-design / best-practices / btw / code-optimizer / core-web-vitals / create-gsd-extension / create-mcp-server / create-skill / create-workflow / debug-like-expert / decompose-into-slices / dependency-upgrade / design-an-interface / forensics / frontend-design / github-workflows / grill-me / handoff / lint / make-interfaces-feel-better / observability / react-best-practices / review / security-review / spike-wrap-up / tdd / test / userinterface-wiki / verify-before-complete / web-design-guidelines / web-quality-audit / write-docs / write-milestone-brief`

**Skill mix**: methodology (TDD / decompose-into-slices / write-milestone-brief / verify-before-complete) + tooling (lint / test / forensics / observability) + frontend (frontend-design / react-best-practices / web-design-guidelines / core-web-vitals / accessibility) + meta (create-skill / create-gsd-extension / create-mcp-server / create-workflow). Mid-scope (35) — between OMC v27 (15+) and codymaster v12 (79).

## Build pipeline orchestration (root package.json scripts)

```
build:pi-tui      → npm run build -w @gsd/pi-tui
build:pi-ai       → npm run build -w @gsd/pi-ai
build:pi-agent-core → npm run build -w @gsd/pi-agent-core
build:pi-coding-agent → npm run build -w @gsd/pi-coding-agent
build:native-pkg  → npm run build -w @gsd/native
build:rpc-client  → npm run build -w @gsd-build/rpc-client
build:pi          → native-pkg + pi-tui + pi-ai + pi-agent-core + pi-coding-agent (lockstep)
build:mcp-server  → npm run build -w @gsd-build/mcp-server
build:core        → build:pi + build:rpc-client + build:mcp-server + tsc + copy-resources + copy-themes + copy-export-html
build             → build:core + build-web-if-stale.cjs
stage:web-host    → stage-web-standalone.cjs
build:web-host    → web build + stage:web-host
```

## Engines + Node version

`"engines": { "node": ">=22.0.0" }` + README guides **Node 24 LTS** specifically (with `docs/user-docs/node-lts-macos.md` for Homebrew users). **Aggressive Node version requirement** vs corpus baseline (typical T1 = Node 18+).

## Cross-references

- See `(C) Cluster 1` for README headline positioning + GSD-1 relationship
- See `(C) Cluster 3` for governance + commercial-funnel
- See `(C) Entity 3` for Pi SDK cross-corpus connection deep-dive
