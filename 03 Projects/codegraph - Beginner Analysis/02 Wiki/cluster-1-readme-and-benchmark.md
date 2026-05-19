# Cluster 1 — README + value-claim + benchmark positioning

> Source: `README.md` · v0.7.9 era · fetched 2026-05-19

## Subject self-positioning (verbatim)

**Tagline:** *"Pre-indexed code knowledge graph for Claude Code, Codex, Cursor, and OpenCode — fewer tokens, fewer tool calls, 100% local"*

**Triple value-claim (verbatim from README):**
*"94% fewer tool calls · 77% faster exploration · 100% local"*

**Positioning rationale (verbatim):**
> "When Claude Code explores a codebase, it spawns Explore agents that scan files with grep, glob, and Read — consuming tokens on every tool call." Pre-indexing provides: "symbol relationships, call graphs, and code structure. Agents query the graph instantly instead of scanning files."

This positioning frames codegraph as **alternative to runtime grep/find exploration** by AI coding agents. The product axis is **pre-indexed-context-layer** vs **runtime-exploration** — a corpus-novel positioning. → **OC-K Pre-Indexed-Context-Layer observational candidate.**

## Benchmark positioning (corpus-rare in primary README)

The README includes a **6-codebase benchmark table** with quantitative tool-call + time comparisons:

| Codebase | Language | With CodeGraph | Without CodeGraph | Improvement |
|----------|----------|---|---|---|
| VS Code | TypeScript | 3 calls, 17s | 52 calls, 1m 37s | **94% fewer · 82% faster** |
| Excalidraw | TypeScript | 3 calls, 29s | 47 calls, 1m 45s | **94% fewer · 72% faster** |
| Claude Code | Python + Rust | 3 calls, 39s | 40 calls, 1m 8s | **93% fewer · 43% faster** |
| Claude Code | Java | 1 call, 19s | 26 calls, 1m 22s | **96% fewer · 77% faster** |
| Alamofire | Swift | 3 calls, 22s | 32 calls, 1m 39s | **91% fewer · 78% faster** |
| Swift Compiler | Swift/C++ | 6 calls, 35s | 37 calls, 2m 8s | **84% fewer · 73% faster** |

**Average:** 92% fewer tool calls / 71% faster.

**Corpus context:** v69 CloakBrowser also led with quantitative benchmark table (14-axis comparison vs stock Playwright + 5-tool comparison matrix). codegraph v70 leads with same marketing-positioning strategy. **N=2 evidence for OC-M Quantitative-Benchmark-Marketing observational candidate.**

**Pattern Library implication for Pattern #57 strengthening:** the benchmark uses **Claude Code (vault substrate; foundation product)** as one of the tested codebases — corpus-rare instance of *testing-the-corpus-substrate-from-within-corpus-subject*. Pattern #57 sub-mechanism candidate: subject-tests-against-substrate.

## Installation (multi-agent installer pattern)

```bash
# Interactive installer
npx @colbymchenry/codegraph

# Project init
cd your-project
codegraph init -i

# Global install
npm install -g @colbymchenry/codegraph

# Non-interactive scripting
codegraph install --yes
codegraph install --target=cursor,claude --yes
codegraph install --target=auto --location=local
```

The `--target=cursor,claude --yes` syntax is **corpus-novel multi-agent installer pattern** — single command installs/configures for multiple agent platforms in one operation. v0.7.7 CHANGELOG describes this as: *"Multi-agent installer with interactive selection for Claude Code, Cursor, Codex CLI, and OpenCode."*

→ **OC-L Multi-Agent-Installer-Pattern observational candidate** (single tool, multiple agent targets in one installer flow).

## 19+ supported languages (corpus-broadest tree-sitter coverage)

| Language | Extension(s) |
|----------|-------------|
| TypeScript | `.ts`, `.tsx` |
| JavaScript | `.js`, `.jsx`, `.mjs` |
| Python | `.py` |
| Go | `.go` |
| Rust | `.rs` |
| Java | `.java` |
| C# | `.cs` |
| PHP | `.php` |
| Ruby | `.rb` |
| C | `.c`, `.h` |
| C++ | `.cpp`, `.hpp`, `.cc` |
| Swift | `.swift` |
| Kotlin | `.kt`, `.kts` |
| Scala | `.scala`, `.sc` |
| Dart | `.dart` |
| Svelte | `.svelte` |
| Vue | `.vue` |
| Liquid | `.liquid` |
| Pascal/Delphi | `.pas`, `.dpr`, `.dpk`, `.lpr` |

**19 languages** is the **corpus-broadest single-subject language-coverage** observed (prior corpus subjects single-or-narrow). Pascal/Delphi inclusion is corpus-novel-at-multilanguage-tool — most code-intel tools skip Delphi entirely.

## 13 framework-aware route detection

| Framework | Detection mechanism |
|-----------|---------------------|
| Django | `path()`, `re_path()`, `url()`, `include()` in `urls.py` |
| Flask | `@app.route()` decorators, blueprint routes |
| FastAPI | `@app.get()`, `@router.post()` + standard methods |
| Express | `app.get()`, `router.post()` with middleware chains |
| Laravel | `Route::get()`, `Route::resource()`, controller syntax |
| Rails | `get '/x', to: 'users#index'` hash-rocket syntax |
| Spring | `@GetMapping`, `@PostMapping`, `@RequestMapping` |
| Gin/chi/gorilla/mux | `r.GET()`, `router.HandleFunc()` |
| Axum/actix/Rocket | `.route("/x", get(handler))` |
| ASP.NET | `[HttpGet("/x")]` attributes |
| Vapor | `app.get("x", use: handler)` |
| React Router | Route component nodes |
| SvelteKit | Route component nodes |

This is **corpus-broadest framework-aware code-intel coverage** in a single tool. Distinct from per-framework tooling (e.g., django-extensions, flask-shell) — single tool covers 13 frameworks orthogonally.

## 8 MCP tools (the API surface)

| Tool | Purpose |
|------|---------|
| `codegraph_search` | Find symbols by name across the codebase |
| `codegraph_context` | Build relevant code context for a task |
| `codegraph_callers` | Find what calls a function |
| `codegraph_callees` | Find what a function calls |
| `codegraph_impact` | Analyze code affected by changing a symbol |
| `codegraph_node` | Get details about a specific symbol with source |
| `codegraph_files` | Get indexed file structure |
| `codegraph_status` | Check index health and statistics |

8 tools is moderate-granular vs v66 agentmemory's 51 tools. Different design philosophy: codegraph optimizes for **lightweight tools** ("Main session may use lightweight tools (`search`, `callers`, `impact`, `node`) for targeted lookups").

## 12 CLI commands

```
codegraph                              # Interactive installer
codegraph install                      # Explicit installer
codegraph init [path]                  # Initialize project
codegraph uninit [path]                # Remove CodeGraph
codegraph index [path]                 # Full index
codegraph sync [path]                  # Incremental update
codegraph status [path]                # Show statistics
codegraph query <search>               # Search symbols
codegraph files [path]                 # Show file structure
codegraph context <task>               # Build context for AI
codegraph affected [files...]          # Find affected test files
codegraph serve --mcp                  # Start MCP server
```

12 commands cover full lifecycle (install/init/index/sync/uninit) + query interface (query/context/files/affected) + service mode (serve --mcp).

## Architecture diagram (from README)

```
Claude Code / Cursor / Codex CLI / opencode
            ↓
    CodeGraph MCP Server
    ├── Search tool
    ├── Callers/Callees
    └── Context builder
            ↓
    SQLite Graph Database
    ├── Symbol nodes
    ├── Reference edges
    └── Full-text search (FTS5)
```

**4-layer pipeline:** Agent clients → MCP server → SQLite graph database → tree-sitter extraction (pre-indexed).

**Pattern #18 sub-mechanism B evidence:** This diagram explicitly visualizes "one-binary-many-CLIENTS via MCP" — 4 agent platforms above the MCP server. Strong visual confirmation of sub-mechanism B "one-binary-many-CLIENTS" structural shape that v69 audit registered.

## Agent integration table

| Agent | Config Location |
|-------|---|
| Claude Code | `~/.claude.json` |
| Cursor | `.cursor/rules/codegraph.mdc` |
| Codex CLI | `~/.codex/AGENTS.md` |
| OpenCode | `opencode.jsonc` (v0.7.8 fixed from `opencode.json`) |

**Observation:** OpenCode and Codex CLI use AGENTS.md / opencode.jsonc style configs (per-platform CLAUDE.md analogs). Claude Code uses `.claude.json`. Cursor uses `.cursor/rules/codegraph.mdc` — Cursor-specific path. This is **per-platform config-target write** — installer auto-handles 4 distinct config paths.

→ **OC-N Auto-generated AGENTS.md from tool installer** observational candidate (codegraph installer GENERATES AGENTS.md in user's project per v0.7.8 CHANGELOG).

## Pre-indexing rationale (verbatim from README)

> "When Claude Code explores a codebase, it spawns Explore agents that scan files with grep, glob, and Read — consuming tokens on every tool call."

> Pre-indexing provides: "symbol relationships, call graphs, and code structure. Agents query the graph instantly instead of scanning files."

**Key product positioning:** *"Agents achieve 94% fewer tool calls on average, 77% faster exploration, with zero file reads from the indexed database."*

The "zero file reads" claim is **maximally-different positioning** from default Claude Code Read+Grep behavior. → OC-K Pre-Indexed-Context-Layer.

## Agent instruction guidance (verbatim from README)

**Key instruction for Explore agents:** *"Use `codegraph_explore` as the primary tool; avoid re-reading files that the tool already returned source code for."*

**Main session guidance:** *"Main session may use lightweight tools (`search`, `callers`, `impact`, `node`) for targeted lookups."*

This is **product-defined agent-usage discipline** — codegraph instructs how Claude Code (and other agents) should USE codegraph. Corpus-rare framing (most tools don't dictate user behavior so specifically). → Pattern #18 sub-mechanism candidate: **tool-defined-agent-usage-discipline** (related to but distinct from agentmemory's per-tool instructions).

## What's NOT in the README

- No commercial product page / SaaS tier
- No sponsorship link (no Patreon / GitHub Sponsors / ko-fi)
- No telemetry/analytics opt-in toggle (consistent with "100% local")
- No security disclosure policy explicit in README
- No support / contact email
- No code-of-conduct in README (may exist separately)

The README is **purely technical/product positioning** — no funding, no support tier, no commercial path. Matches **solo-individual passion-project profile** of colbymchenry.
