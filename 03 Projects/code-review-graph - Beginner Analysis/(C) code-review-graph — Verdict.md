# (C) code-review-graph — Verdict

**Wiki v226 · 2026-07-25 · `tirth8205/code-review-graph` (Tirth Kanani, London) · MIT · v2.3.7**

## Headline

**GOAL-ALIGNED INCLUDE 3/4 [(a) FAIL · (b) STRONG keys the tier · (c) STRONG · (d) STRONG] — cleanly GOAL-ALIGNED via §31 (no §40 backstop needed).**

**Pattern outcome: NO MINT — N=4 → N=5 instance-strengthening of CONFIRMED Library-vocab #23** ("Pre-Indexed Read-Only Code Knowledge-Graph Queried by Coding Agents via MCP"). The cleanest, strongest instance-strengthening of that family in the recent run — a near-carbon-copy of the **codebase-memory-mcp v172** species (MCP-native, Tree-sitter, token-reduction, 100% local), in a networkx-in-memory variant with a richer analysis + delivery surface.

**Counts UNCHANGED: 46 top-level patterns / 11 CONFIRMED Library-vocab.** §C live standalones **47 UNCHANGED** (strengthening a CONFIRMED item adds no §C row). §C surface **≈54 UNCHANGED.**

**Streak: v225 GA:83 → `GA:84 · OG:13 [7 ov]`** (cleanly GA on (b) STRONG; **7 consecutive GA post the v219 OG break**). **§35 CLEAR** (window {v224 GA, v225 GA, **v226 GA**} = 0 OG).

**Tier T2 Service** (self-hosted local code-intelligence MCP server / developer tool — the codegraph v70 / codebase-memory-mcp v172 / agentmemory v66 / fff v194 family).

---

## The 4 criteria

### (a) FAIL — Tirth Kanani, disclosed individual, not Anthropic
London-based AI/ML engineer + technical founder; University of Birmingham HCI/AI Lab; Epiminds Multi-Agent Hackathon 2025 winner; founder of CrumbleUX; author of MERIT / Jailbreak-Eval / GraphMinds. **Not Anthropic; no registered (a)-7 vendor-direct source.** Per §41, no notability / credential / hackathon-win / heritage / locale inference rescues an (a) FAIL, and the disclosed-individual (a)-axis answers NO. First `tirth8205` / Tirth-Kanani author → **#19 19a**.

### (b) STRONG — keys the tier
An **MCP code-intelligence server for coding agents** (Claude Code first-class among 15+ harnesses) whose **entire raison d'être is token reduction for AI code review** ("Stop burning tokens"):
- **Dead-center on the Goal-#1 agent substrate** — a read-only code knowledge graph queried by coding agents via MCP is the exact capability the vault has tracked four times (graphify v16 / GitNexus v33 / codegraph v70 / codebase-memory-mcp v172).
- **Dead-center on the operator's live `claude-api-cost-optimization` pilot thread** — this IS the flagship tool-class of that thread (cut the tokens an agent spends reading code). ~82× median per-question token reduction (README, page-stated).
- **On the `CC-memory-systems` thread** — a code knowledge graph is an L-level code-memory system, the code analogue of this very vault.
- **Directly, safely, on-goal pilotable** into the vault's own Claude Code AND into **hireui** — which is **already "GitNexus-first"** (GitNexus v33 = a member of this same #23 family) → code-review-graph is a direct **alternative / complement** to hireui's existing code-intel choice (a genuine bake-off, not a stretch).

**STRONG-not-STRONGEST:** third-party + read-only capability-augmentation + Claude one of 15+ harnesses + an **established-pattern instance**, not a novel primitive. Calibrates exactly to codebase-memory-mcp v172 / codegraph v70 / fff v194 (all (b) STRONG). No §40 needed — on-goal by (b) alone.

### (c) STRONG — with honest caveats
Real, pip-installable Python package **v2.3.7**, source-verified from `pyproject.toml`: a `mcp`+`fastmcp` MCP server, `tree-sitter`+`tree-sitter-language-pack` (40+ languages), a `networkx` in-memory graph, `watchdog` incremental updates (<2s), optional `igraph` community detection + `sentence-transformers` semantic layer + `jedi` enrichment + `ollama` wiki-generation; **30 MCP tools**; **blast-radius impact analysis** with an honestly-caveated **0.714 avg F1** benchmark (precision 0.578, recall 1.0-by-construction, 0.609–0.864 across 6 repos); **~82× median per-question token reduction** (range 38×–528×); multi-format export (GraphML / Neo4j Cypher / Obsidian / SVG); VS Code extension + GitHub Action + `crg-daemon` multi-repo; code-review-graph.com + Discord; MIT.

⚠️ **Caveats:**
- **NOT source-cloned** (README + repo page + author profile + `pyproject.toml` + landscape only — the v200→v225 self-throttle). Graph-algorithm + MCP-tool internals are page/README/dependency-stated.
- **Page-stated ~26.2k★ / 2.5k forks (§37.4)** → **NOT a Pattern #52** (viral-velocity) claim.
- **Metric framing** — the README's per-question **~82×** vs the author-profile's aggregate **"6.8×"** measure different things; README primary; both page-stated (see Deep Dive §2).
- **The hard parts are library-backed** — Tree-sitter parsing, networkx/igraph graph algorithms, sentence-transformers embeddings. code-review-graph is the **graph-model + blast-radius + MCP-surface orchestration layer** (a substantive but not from-scratch contribution — the honest reading).

### (d) STRONG — connectivity
Direct **N=4 → N=5 instance of CONFIRMED Library-vocab #23** (graphify v16 / GitNexus v33 / codegraph v70 / codebase-memory-mcp v172 → + code-review-graph); closest twin **codebase-memory-mcp v172** (networkx-in-memory variant vs its SQLite). Plus: the **claude-context v40** vector-based CONTRAST (excluded from #23; code-review-graph's optional embeddings extra is a graph-primary bolt-on, not the store); **fff v194** lexical-search sibling (different mechanism, same token-reduction goal); the **claude-api-cost-optimization** + **CC-memory-systems** pilot threads; **#18 B1-MCP** (one fastmcp server, 15+ clients); **Library-vocab #20** Token-Economy-Quantification QUALIFIED-ADJACENT; the **Obsidian-export + ollama-wiki-generation** cross-ref to this vault's own LLM-Wiki pattern + **openwiki v195**.

---

## Why NO MINT (and why that's the disciplined call)

code-review-graph does the **exact defining thing** of CONFIRMED Library-vocab #23: a coding agent queries a pre-built read-only graph of the codebase via MCP (symbols/edges/call-chains; tree-sitter variant) instead of reading files, for token-reduction, 100% local. That is not a new capability class — it is the 5th cross-author instance of a family the corpus promoted to CONFIRMED at the v182 audit.

**The distinguishing facets do NOT warrant a separate §C mint** (the anti-"draw-the-circle" discipline — camofox v179 / CLIProxyAPI v207 / OmniRoute v208 / geti v213): igraph community-detection, the benchmarked-blast-radius F1, the optional hybrid vector layer, 40+-language breadth, multi-format export, and the multi-surface delivery (CLI + VS Code + GitHub Action + daemon) are **within-species variation + a richer profile**, not a new primitive. Drawing a circle tight enough to make code-review-graph "corpus-first" (e.g. "benchmarked-blast-radius code graph") would be the phantom-count inflation §28 fights.

**Bookkeeping:** #23 goes **N=4 → N=5** (a genuine cross-author 5th instance strengthens the CONFIRMED item; recorded, exact tally reconciled at the next audit per the CONFIRMED-item convention). CONFIRMED-count (11) and top-level-pattern-count (46) UNCHANGED; §C live standalones (47) UNCHANGED.

**No reviewable §C-mint alternative is even close here** — unlike v224/v225 (which recorded §C-mint alternatives), code-review-graph is a clean, unambiguous instance-strengthening of an already-CONFIRMED item. There is nothing to over-mint.

---

## Blunt bottom line

**code-review-graph is a genuinely good, on-goal, directly-pilotable code-intelligence MCP server — and it is the corpus's 5th instance of a pattern you already confirmed, so the corpus value is the clean N=4→N=5 strengthening + a real pilot, not a new mint.** It's a near-twin of codebase-memory-mcp v172 (networkx-in-memory instead of SQLite) with a richer blast-radius benchmark + community-detection + broad-language + multi-surface profile. It is **arguably a stronger *pilot* than v172** for you specifically: pure-`pip install` (no `curl|bash` binary), MIT, its whole value prop maps onto your live cost-optimization thread, and hireui is already GitNexus-first (a #23-family tool) so there's a natural head-to-head. Borrow it as a tool, measure the token delta, don't over-mint it.
