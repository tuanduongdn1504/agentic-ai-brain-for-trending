# (C) code-review-graph — Deep Dive

**Wiki v226 · shipped 2026-07-25 · GOAL-ALIGNED INCLUDE 3/4 · NO MINT (CONFIRMED Library-vocab #23 instance-strengthening, N=4 → N=5)**

> Repo: `tirth8205/code-review-graph` · Author: **Tirth Kanani** (London) · MIT · Python 3.10+ · **v2.3.7** · pip: `code-review-graph`
> ⚠️ **NOT source-cloned** — this wiki is built from the rendered GitHub repo page + the raw `README.md` + the raw `pyproject.toml` + the author's GitHub profile + landscape WebSearch. Graph-algorithm + MCP-tool internals are page/README/dependency-stated, not code-verified (the v200→v225 self-throttle: the ~205K CLAUDE.md shim overflows every subagent > 200K → deep-dive workflows fail prompt-too-long; source hand-fetched, verified by hand).

---

## 1. What it is, in one sentence

A **self-hosted, local, pip-installable code-intelligence engine** that parses your whole codebase into a **structural graph** (Tree-sitter → functions/classes/imports as nodes; calls/inheritance/tests as edges), keeps it fresh with **incremental sub-2s updates**, and serves an AI coding agent **precise, minimal context via MCP** so the agent reads *only what matters for a code review* instead of the whole corpus. Tagline: **"Stop burning tokens. Start reviewing smarter."**

It is, structurally, **the same species the vault already tracks as CONFIRMED Library-vocab #23** — "Pre-Indexed Read-Only Code Knowledge-Graph Queried by Coding Agents via MCP" (graphify v16 / GitNexus v33 / codegraph v70 / codebase-memory-mcp v172). code-review-graph is the **5th** instance and the closest living twin of **codebase-memory-mcp v172**, differing mainly in its store (in-memory **networkx** rather than SQLite) and in a richer analysis + delivery surface.

---

## 2. The problem it solves

An AI code reviewer that reads files one-by-one burns enormous token budgets and still misses cross-file impact. The bet here: pre-compute the code's structure ONCE into a graph, then answer an agent's review questions ("what breaks if I change this function?", "who calls this?", "which tests cover this?") by **traversing the graph and returning only the relevant slice** — not by re-reading files. That is the exact "token-reduction, 100% local, read-only graph via MCP" shape of Library-vocab #23.

**Headline benchmark (README, primary source):** **~82× median per-question token reduction (range 38×–528×) across 6 real repositories.**

> ⚠️ **Metric discrepancy, resolved:** the author's GitHub *profile* summary states **"6.8× average context compression across 23 languages"** — a *different* metric (an aggregate/whole-context compression framing, and a conservative "23-language" count) from the README's **per-question** ~82× reduction. They measure different things; the README's per-question figure is the operative agent-workflow metric and is treated as authoritative here. The README itself lists **40+** Tree-sitter grammars (see §5), well beyond the profile's "23." Both figures are **page-stated (§37.4)** and neither grounds a Pattern #52 (viral-velocity) claim.

---

## 3. Architecture (source-verified from `pyproject.toml` + README)

**Core pipeline:**
1. **Parse** — Tree-sitter (`tree-sitter` + `tree-sitter-language-pack`) turns source into an AST → nodes (functions, classes, imports) + edges (calls, inheritance, test-coverage links).
2. **Graph** — an **in-memory `networkx` graph** holds the structural model. *(Note: NOT SQLite-persisted — a genuine variant vs codebase-memory-mcp v172's SQLite store and codegraph v70. It can EXPORT to Neo4j Cypher / GraphML but its live store is networkx-in-memory.)*
3. **Watch + incrementally update** — `watchdog` re-parses only changed files → **under 2 seconds** for subsequent changes (build performance README-stated: flow detection ~95–128 ms; search latency 0.4–1.5 ms).
4. **Serve to agents via MCP** — a **`fastmcp`-based MCP server** (`mcp>=1.0` + `fastmcp>=3.2`) exposes **30 MCP tools** so the agent queries the graph instead of reading files.

**Blast-radius / impact analysis (the distinctive feature).** When files change, it traces callers, dependents, and affected tests — the "blast radius" of a change — so a reviewer sees *what a change actually touches*. This is benchmarked (repo page):

| Metric | Value |
|---|---|
| Average **F1** across 6 repos | **0.714** |
| Average Precision | 0.578 |
| Recall | 1.0 *(explicitly noted as a graph-derived upper bound, "circular by construction")* |
| F1 range | 0.609 (gin) → 0.864 (httpx) |

> The "recall = 1.0, circular by construction" self-disclosure is an **unusually honest benchmark caveat** — the tool doesn't overclaim; it states that recall is graph-bounded and reports the more meaningful precision/F1.

**Analysis layers (optional extras, source-verified):**
- **Community detection** via `igraph` (the `communities` extra) — igraph ships Leiden + betweenness-centrality, so it can partition the codebase into modules / find central hub nodes.
- **Semantic search** via `sentence-transformers` + `numpy` (the `embeddings` extra) or Google embeddings (`google-generativeai`) — an **optional** vector layer *on top of* the graph. ⚠️ This makes it a **graph-PRIMARY tool with a bolt-on vector option**, NOT a vector-first tool — so it remains a Library-vocab #23 *graph* instance (the vector-based sibling **claude-context v40** is the DISTINCT retrieval architecture #23 explicitly does NOT count; here embeddings are an add-on facet, not the store).
- **Enrichment** via `jedi` (the `enrichment` extra) — Python type-inference to sharpen the graph.
- **Wiki generation** via `ollama` (the `wiki` extra) — generates a prose/Obsidian wiki of the codebase from the graph using a **local** Ollama model. *(A direct cross-ref to THIS vault's own LLM-Wiki pattern + openwiki v195: the agent-readable-docs-from-a-code-graph idea.)*

**Delivery surfaces (multi-surface):**
- **pip CLI** — `pip install code-review-graph` → `code-review-graph install` → `code-review-graph build`; entry points `code-review-graph` (`cli:main`) + **`crg-daemon`** (`daemon_cli:main`, a **multi-repo daemon**).
- **VS Code extension** — `code-review-graph-vscode` folder in the repo.
- **GitHub Action** — a composite Action for CI review.
- **Multi-format export** — GraphML, Neo4j Cypher, Obsidian vaults, SVG.
- **Website + community** — code-review-graph.com; Discord.

**Harness support (repo page — the breadth is notable):** "Works with Codex, Claude Code, CodeBuddy Code, Cursor, Windsurf, Zed, Continue, OpenCode, Antigravity, Gemini CLI, Qwen, Qoder, Kiro, GitHub Copilot, and GitHub Copilot CLI." Claude Code is a **first-class** named install target (topics include `claude`, `claude-code`, `mcp`).

**The 30 MCP tools (README categories):** query, traversal, semantic search, impact radius, review context, community detection, flow analysis, refactoring, wiki generation, architecture overview, change detection, and multi-repo utilities.

**Full dependency surface (verified, `pyproject.toml` v2.3.7):**
- Runtime: `mcp>=1.0,<2`, `fastmcp>=3.2.4,<4`, `tree-sitter>=0.23,<1`, `tree-sitter-language-pack>=0.3,<1`, `pyyaml`, `networkx>=3.2,<4`, `watchdog>=4,<7`, `tomli` (Py<3.11).
- Extras: `embeddings` (sentence-transformers + numpy) · `google-embeddings` (google-generativeai) · `communities` (igraph) · `enrichment` (jedi) · `eval` (matplotlib + pyyaml) · `wiki` (ollama) · `all` · `dev` (pytest/pytest-asyncio/pytest-cov/ruff).
- **Not present:** sqlite/sqlite3, neo4j (as a store), chromadb, faiss, leidenalg (Leiden comes via igraph), langchain, openai.

---

## 4. Author (criterion (a) evidence)

**Tirth Kanani** (`tirth8205`; display "Tirth Kanani") — an **AI/ML engineer and technical founder based in London**. GitHub profile: "building production-grade tools and products that developers actually use"; affiliated with the **University of Birmingham HCI and AI Lab**; won first place at the **Epiminds Multi-Agent Hackathon 2025**. Other work: founder of **CrumbleUX** (a real-time VLM product for design critique); open-sourced **MERIT** and **Jailbreak-Eval** frameworks; pinned repos GraphMinds / code-review-graph / claude-games. Links: tirthkanani.com, X `@tirth_8205`, LinkedIn in/tirthkanani, Medium `@tirthkanani18`. 577 followers page-stated.

**A disclosed, credentialed individual builder — NOT Anthropic, and no registered (a)-7 vendor-direct source.** Per §41, no notability / credential / hackathon-win / other-project inference rescues an (a) FAIL. First `tirth8205` / Tirth-Kanani author in the corpus → **#19 19a** data-point.

---

## 5. Language coverage (README-listed, 40+ Tree-sitter grammars)

Python · JavaScript / TypeScript / TSX · Go · Rust · Java · C / C++ · C# · VB.NET · Ruby · Kotlin · Swift · PHP · Scala · Solidity · Dart · R · Perl (+ Perl XS) · Lua / Luau · Objective-C · shell scripts · Elixir · Zig · PowerShell · Julia · ReScript · GDScript · Nix · Verilog / SystemVerilog · SQL · Terraform / OpenTofu · Ansible · Vue / Svelte · Astro · Jupyter / Databricks notebooks. The breadth comes from `tree-sitter-language-pack`; the author's profile summarizes it as "23 languages" (conservative / stale — see §2).

---

## 6. Where it sits in the corpus — CONFIRMED Library-vocab #23 (the code-knowledge-graph-via-MCP family)

CONFIRMED Library-vocab **#23** = "Pre-Indexed Read-Only Code Knowledge-Graph Queried by Coding Agents via MCP (symbols/edges/call-chains; SQLite/Cypher/LSP/tree-sitter variants) instead of reading files one-by-one — token-reduction, 100% local." Promoted at the v182 audit at **N=4**:

| N | Wiki | Instance | Store / variant |
|---|---|---|---|
| 1 | graphify **v16** | "code → knowledge graph → Claude Code," ships an MCP server | graph |
| 2 | GitNexus **v33** (`abhigyanpatwari`) | "indexes any codebase into a knowledge graph … 16 MCP tools" | graph |
| 3 | codegraph **v70** | code knowledge-graph via MCP | graph |
| 4 | codebase-memory-mcp **v172** (`DeusData`) | SQLite graph + Cypher + LSP + tree-sitter; ~99.2% token reduction; 100% local; 11-client auto-config | **SQLite** graph |
| **5** | **code-review-graph v226** (Tirth Kanani) | Tree-sitter → **networkx in-memory** graph; blast-radius (0.714 F1); ~82× per-question token reduction; 30 MCP tools; 15+ harnesses | **networkx** graph |

**code-review-graph is a textbook 5th instance:** pre-built read-only code graph, queried by coding agents via a `fastmcp` MCP server, explicitly for token-reduction, 100% local, tree-sitter variant. It is the **closest twin of codebase-memory-mcp v172** (MCP-native, tree-sitter, token-reduction, blast-radius ≈ v172's Cypher impact-traversal) differing in store (networkx-in-memory vs SQLite) and in analysis/delivery breadth.

**Distinguishing facets (recorded, NOT separately minted — anti-"draw-the-circle," the camofox v179 / CLIProxyAPI v207 / geti v213 discipline):**
- `igraph` community detection (Leiden / betweenness-centrality) as a first-class analysis layer.
- **Benchmarked blast-radius impact analysis (0.714 avg F1, honestly caveated).**
- An **optional** sentence-transformers semantic layer (a hybrid graph+vector, but graph-primary → still a #23 graph instance, not the claude-context v40 vector class).
- 40+-language Tree-sitter breadth.
- Multi-format export (GraphML / Neo4j Cypher / **Obsidian vaults** / SVG) + an ollama-powered **wiki-generation** tool (the LLM-Wiki-pattern-for-code cross-ref to this vault + openwiki v195).
- Multi-surface delivery: pip CLI + VS Code extension + GitHub Action + a `crg-daemon` multi-repo daemon.

**Adjacent, NOT this family:**
- **claude-context v40** — vector/embedding-based semantic code search, NOT a graph → the DISTINCT retrieval architecture #23 excludes. (code-review-graph's *optional* embeddings extra is a bolt-on, not the store — so it stays a #23 graph instance.)
- **fff v194** — resident in-process *lexical* fuzzy file+content search via MCP; a different retrieval mechanism (lexical, not graph) with the same token-reduction goal.
- **agentmemory v66 / supermemory v132** — conversational/agent memory, not a *code* graph.
- **devspace v171** — manufactures a coding agent (opposite vector).

---

## 7. Secondary observations (recorded, NOT minted)

- **#18 sub-archetype B / B1-MCP** — one `fastmcp` MCP server consumed by 15+ named clients = instance-strengthening (the *distribution structure*; #23 is the *capability* — recorded, **no double-count**, the v140/v172 precedent).
- **#84 84c cross-harness** — a 15+-harness install matrix; **NO N-bump** (one server many hosts consume; NOT the ponytail v168 native-rule-file *generator*).
- **Library-vocab #20 Token-Economy-Quantification** — QUALIFIED-ADJACENT (an explicit per-question ~82× benchmark); **N stays 4** (the v168/v172/v179 anti-inflation precedent — token-impact quantified, but recorded not incremented).
- **#66 supply-chain** — install BENIGN: `pip install code-review-graph` + a local `build` (NO `curl|bash`, NO compiled-binary download unlike codebase-memory-mcp v172); MIT; the optional wiki-gen uses a **local** Ollama model (no cloud egress); the optional embeddings extra can use Google embeddings (a cloud egress if enabled). ⚠️ NOT source-cloned → install-snapshot + pip-security-check + inspect the 30 MCP tools before wiring into an agent.
- **#19 19a** — first Tirth-Kanani / `tirth8205` author + first University-of-Birmingham-HCI/AI-Lab-affiliated indie builder.
- **Author-portfolio note** — CrumbleUX (VLM design-critique) / MERIT / Jailbreak-Eval / GraphMinds (a distinctive graph-engineering + AI-eval portfolio; none are corpus subjects → NOT #57).
- **Vault cross-ref** — the Obsidian-vault export + ollama-powered wiki-generation = the LLM-Wiki-pattern applied to code (openwiki v195 sibling; a fun mirror of this very vault).

**NON-claims:** NOT #52 (~26.2k★/2.5k forks page-stated §37.4 → velocity unestablishable) · NOT corpus-first (the #23 family predates it 4× back to graphify v16) · NOT a new §C standalone · NOT a new top-level pattern (max #85) · NOT #57 (deps tree-sitter/networkx/igraph/sentence-transformers/mcp — none corpus subjects; harness names = install targets, not influence-citations) · NOT world-first (Sourcegraph / GitHub code-graph / Glean / the whole code-intelligence space precede) · NOT SQLite-based (networkx-in-memory variant) · NOT source-cloned (flagged).

---

## 8. Verdict pointer

See **`(C) code-review-graph — Verdict.md`** for the 4-criteria call and the NO-MINT reasoning, and **`(C) code-review-graph — Pilot Methods Menu.md`** for the on-goal pilot ladder (it is a genuinely LOW-risk, on-goal, directly-pilotable subject — the fff v194 / codebase-memory-mcp v172 class, and hireui is already "GitNexus-first," a #23-family tool → a natural bake-off).
