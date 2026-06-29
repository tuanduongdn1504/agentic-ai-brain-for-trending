# Graphify — CLI, Install & Commands

> **Source:** [[graphify-codebase-graph/_index]]. Commands verified against the repo README + the video walkthrough. ⚠️ **Package name = `graphifyy` (double-y); CLI = `graphify` (single-y).** This mismatch is a real typosquat risk — see [[graphify-codebase-graph/security-and-install-safety]].

## Install (the video's exact ritual)

1. **Check Python** — needs **3.10+** (older versions fail or hit weird errors).
2. **Install the package** (note the **double-y**):
   ```bash
   pip install graphifyy            # or, safer:
   uv tool install graphifyy        # recommended — exact-name, isolated
   pipx install graphifyy
   ```
   On WSL/Linux use a venv (newer Python blocks global pip installs).
3. **Register the skill** for your platform:
   ```bash
   graphify install                       # default: Claude Code
   graphify install --platform opencode   # for OpenCode (see opencode-integration)
   graphify install --platform codex|cursor|gemini|...
   ```
4. **(OpenCode only) make it always-on:** `graphify opencode install` — writes an `AGENTS.md` section + installs the `tool.execute.before` plugin + registers it in `opencode.json`. See [[graphify-codebase-graph/opencode-integration]].

## Build the graph

```bash
graphify .                 # graph the current directory ( "." = current dir )
graphify ./src             # graph just a subfolder
/graphify .                # the slash-command form, from inside the agent
```
- For a medium project (a few hundred files), expect **~5-10 min**; it shows progress.
- Drop a **`.graphifyignore`** at the root (gitignore syntax) to skip `node_modules/`, `vendor/`, `dist/`, etc.
- Output lands in **`graphify-out/`** (`graph.html`, `GRAPH_REPORT.md`, `graph.json`, `cache/`). See [[graphify-codebase-graph/three-pass-architecture]].

## Build-time flags

| Flag | Effect |
|---|---|
| `--update` | Re-extract **only changed files** and merge (cheap; code changes = AST-only, no LLM) |
| `--mode deep` | Aggressive inferred-edge extraction (more `INFERRED` edges) |
| `--watch` | Auto-sync the graph as files change |
| `--wiki` | Also build an agent-crawlable **markdown wiki** from the graph |
| `--obsidian --obsidian-dir <path>` | Emit an **Obsidian vault** of the graph |
| `--svg` / `--graphml` / `--neo4j` | Export `graph.svg` / `graph.graphml` (Gephi/yEd) / `cypher.txt` (Neo4j/FalkorDB) |
| `--mcp` | Start an MCP stdio server over the graph |

> ⚠️ **Headless vs skill quirk** (from the lucasrosati setup): in **headless CLI** you must use explicit subcommands (`graphify extract . --out ...`, `graphify update`, `graphify watch`) — passing a bare `.` can throw "unknown command". The bare `graphify .` / `/graphify .` form is the **skill** invocation. Confirm the exact form for your install.

## Keep it in sync

- **Manual:** `graphify --update` whenever you feel like it (only touches changed files).
- **Automatic (recommended):**
  ```bash
  graphify hook install     # installs a post-commit / post-checkout git hook
  ```
  → the graph rebuilds on **every commit and branch switch**. The video recommends this — "you'll forget otherwise." (Code-only rebuilds are free; doc changes re-incur Pass-3 cost.)

## Query the graph (no agent session needed)

These run straight from the terminal and answer **with source-file references**:

| Command | What it does |
|---|---|
| `graphify query "how does auth work?"` | Traverse the graph and answer the question |
| `graphify path "Login" "Database"` | Find the shortest connection between two concepts |
| `graphify explain "PaymentService"` | Plain-language summary of a single node |
| `graphify add <url>` | Fetch + add an arXiv paper or a tweet into the graph |

> Every `graphify query` call logs to `~/.cache/graphify-queries.log` (JSONL). Disable with `GRAPHIFY_QUERY_LOG_DISABLE=1`.

## Key Takeaways

- **Install = `pip install graphifyy` (double-y) → `graphify install [--platform X]` → `graphify .`** Mind the package-name typo trap.
- `--update` and `graphify hook install` keep the graph fresh cheaply; the git-hook route is the "set and forget."
- `query` / `path` / `explain` give you graph answers **without spinning up a full agent session** — useful for quick architecture questions.
- Many export formats (`--obsidian`, `--wiki`, `--graphml`, `--neo4j`, `--mcp`) make the graph portable into other tools, including your Obsidian vault.
