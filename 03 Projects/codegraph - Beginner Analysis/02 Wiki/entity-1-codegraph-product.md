# Entity 1 — codegraph as pre-indexed code knowledge graph (T2 Service)

> Tier: T2 Service · Archetype: solo-individual-multi-product-portfolio · Velocity: SUSTAINED-MODERATE-HIGH 42 stars/day / 121 days

## What codegraph IS

codegraph is a **TypeScript-built local-first code intelligence MCP server** that pre-indexes a codebase using tree-sitter parsers + SQLite (FTS5) and serves the pre-indexed knowledge graph to AI coding agents (Claude Code / Cursor / Codex CLI / OpenCode) via Model Context Protocol.

The product axis is **pre-indexed-context-layer** as alternative to runtime grep/find/Read exploration by agents — saving 94% of tool calls + 77% of exploration time on average across a 6-codebase benchmark suite.

## Corpus position (T2 Service)

| Axis | codegraph (v70) | Sibling: agentmemory (v66) | Sibling: crawl4ai (v29) |
|------|-----------------|---------------------------|-------------------------|
| Tier | T2 Service | T2 Service | T2 Service |
| Primary lang | TypeScript 95.4% | TypeScript 82.4% | Python |
| MCP server | Yes (8 tools) | Yes (51 tools) | No (custom protocol) |
| Multi-platform | **4 agent platforms** | 15+ agent platforms | Standalone |
| Local-only | **100% local** | 100% local | 100% local |
| License | MIT | Apache-2.0 | Apache-2.0 |
| Author | colbymchenry (solo) | rohitg00 (solo) | unclecode (solo) |
| Age at observation | 121 days | ~35 days | ~18 months |
| Stars | 5,062 (42/day) | 7,900 (~226/day) | ~58,000 |
| Anti-detection / privacy | "No data leaves your machine. No API keys. No external services. SQLite database only." | Local memory | Local scraping |

**codegraph's distinguishing axis:** It is the **corpus-first code-knowledge-graph-as-T2-Service** subject — addresses the same agent-augmentation problem-space as agentmemory (different layer: code-structure vs memory) with the same MCP-server-for-multi-platform-agents architectural shape.

## Product architecture (5-layer pipeline)

```
┌─────────────────────────────────────────────────────────────┐
│ LAYER 1: Agent clients (4 platforms)                         │
│ - Claude Code (configures via ~/.claude.json)                │
│ - Cursor (configures via .cursor/rules/codegraph.mdc)        │
│ - Codex CLI (configures via ~/.codex/AGENTS.md)              │
│ - OpenCode (configures via opencode.jsonc)                   │
└─────────────────────────────────────────────────────────────┘
                              ↓ MCP
┌─────────────────────────────────────────────────────────────┐
│ LAYER 2: MCP Server + CLI (Node.js + commander)              │
│ - 8 MCP tools: search / context / callers / callees /        │
│   impact / node / files / status                             │
│ - 12 CLI subcommands: install / init / index / sync /        │
│   status / query / files / context / affected / serve --mcp  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 3: ContextBuilder + GraphQueryManager                   │
│ - BFS/DFS traversal + impact radius analysis                  │
│ - Context assembly for AI consumption                         │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 4: ReferenceResolver + DatabaseConnection               │
│ - Framework-aware pattern matching (13 frameworks)            │
│ - Import/name matching                                        │
│ - SQLite FTS5 (better-sqlite3 native + wasm fallback)         │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 5: ExtractionOrchestrator (tree-sitter)                 │
│ - Per-language extractors (19 languages)                      │
│ - Specialized handlers (Svelte / Vue / Liquid / Delphi)       │
│ - "Extraction is deterministic — derived from AST, not        │
│   LLM-summarized" (CLAUDE.md verbatim)                        │
└─────────────────────────────────────────────────────────────┘
```

The 5-layer architecture cleanly separates extraction from query from agent-interface. Layer 5's AST-deterministic-not-LLM-summarized positioning is the **anti-LLM-summarization product-axis** distinguishing codegraph from LLM-based semantic-search competitors.

## Benchmark positioning (6-codebase comparison)

The README leads with a benchmark table covering 6 real-world codebases at varied scales + languages:

| Codebase | Language | With CodeGraph | Without | Improvement |
|----------|----------|---|---|---|
| VS Code | TypeScript | 3 calls / 17s | 52 calls / 1m 37s | 94% fewer / 82% faster |
| Excalidraw | TypeScript | 3 calls / 29s | 47 calls / 1m 45s | 94% fewer / 72% faster |
| Claude Code | Python + Rust | 3 calls / 39s | 40 calls / 1m 8s | 93% fewer / 43% faster |
| Claude Code | Java | 1 call / 19s | 26 calls / 1m 22s | 96% fewer / 77% faster |
| Alamofire | Swift | 3 calls / 22s | 32 calls / 1m 39s | 91% fewer / 78% faster |
| Swift Compiler | Swift/C++ | 6 calls / 35s | 37 calls / 2m 8s | 84% fewer / 73% faster |

**Average:** 92% fewer tool calls / 71% faster.

**Pattern #57 sub-mechanism candidate:** "Testing-against-substrate-from-within-corpus-subject" — codegraph tests against Claude Code's own codebase (in Python+Rust + Java). This is **corpus-recursive testing** — codegraph (built FOR Claude Code) tests itself against Claude Code's source.

## Cross-corpus integration depth (Pattern #57 STRONG strengthening)

| Layer | Evidence |
|-------|----------|
| Cite | README + CLAUDE.md name Claude Code / Cursor / Codex / OpenCode |
| Integrate | MCP server provides tools to Claude Code (Codex CLI v62 corpus) + OpenCode (v67 corpus) + Cursor + Claude Code |
| Test | Benchmark suite includes Claude Code's own codebase (Python+Rust + Java sub-projects) |

**3-layer cross-corpus integration** matches v69 CloakBrowser depth. The third layer (testing-against-substrate) is corpus-novel for codegraph — most corpus subjects don't test against the substrate they augment.

## Why this matters at the corpus level

**Pattern #18 sub-archetype shared-backend-service sub-mechanism B "one-binary-many-CLIENTS" N=3 strengthening.** The sub-archetype was registered at v69 audit with sub-mechanism A (one-backend-many-IDENTITIES; v67) + B (one-binary-many-CLIENTS via CDP; v69 CloakBrowser CDP). codegraph adds N=3 evidence:

| Subject | Sub-mechanism B variant | Protocol | Clients |
|---------|------------------------|----------|---------|
| v66 agentmemory | one-binary-many-CLIENTS via MCP | **MCP** | 15+ agent platforms |
| v69 CloakBrowser | one-binary-many-CLIENTS via CDP | **CDP** | Multiple framework clients |
| **v70 codegraph** | **one-binary-many-CLIENTS via MCP** | **MCP** | **4 agent platforms** |

Sub-mechanism B is now N=3 across 2 protocol-variants (MCP × 2 + CDP × 1). → Phase 4b PRIMARY proposes formalizing protocol-variants within sub-mechanism B.

## Comparison with default Claude Code exploration

The README explicitly frames the comparison:

> *"When Claude Code explores a codebase, it spawns Explore agents that scan files with grep, glob, and Read — consuming tokens on every tool call."*

codegraph replaces grep + glob + Read with:
- `codegraph_search` (pre-indexed symbol search)
- `codegraph_context` (pre-built context-bundles)
- `codegraph_callers/callees` (call-graph queries; instant vs running ast-grep)
- `codegraph_impact` (impact analysis; not available natively)
- `codegraph_node` (symbol-with-source)
- `codegraph_files` (indexed file structure)

The **call-graph + impact analysis** capabilities are corpus-novel — neither Claude Code's native tools nor most alternatives (grep / ast-grep / sourcegraph / GitHub code search) provide native call-graph queries with impact radius.

→ **OC-K Pre-Indexed-Context-Layer as agent augmentation strategy** observational candidate.

## Storm Bear lessons from Entity 1

For the vault operator:

- **Single-axis differentiation that's deeply technical creates moat.** codegraph's "pre-indexed-context-layer" + "AST-deterministic-not-LLM-summarized" positioning is one specific architectural choice with significant downstream benefits (94% fewer tool calls). Similar to v69 CloakBrowser's "C++ source-level patches" decision.

- **Multi-platform via MCP is replicating across corpus subjects.** agentmemory (15+ platforms) + codegraph (4 platforms) both follow Pattern #18 sub-mechanism B "one-binary-many-CLIENTS via MCP." MCP is becoming the de facto multi-platform protocol for agent augmentation services. Worth tracking for vault tooling design.

- **Solo-individual passion-project profile.** codegraph is colbymchenry's 5K-star solo project with 20-repo portfolio. Similar to other corpus subjects (agentmemory rohitg00 / claude-seo AgriciDaniel / Unsloth solo). The solo-individual-multi-product-portfolio archetype is corpus-N=4 within Pattern #19 19a — strengthening.

- **Pilot candidacy:** codegraph IS a vault-deployable pilot candidate for Storm Bear (would augment Claude Code on the vault's own codebase, especially the TypeScript-heavy hireui-harness sibling project). Direct value-add for vault-maintenance work.
