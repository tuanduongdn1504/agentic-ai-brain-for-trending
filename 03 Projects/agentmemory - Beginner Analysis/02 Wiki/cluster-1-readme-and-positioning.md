# Cluster 1 — README + product positioning

> **Sources:** README.md (primary), package.json (version/license/deps)

## What agentmemory is

A **persistent memory engine for AI coding agents**. The README's framing of the problem:

> *"agentmemory is a persistent memory engine built on the iii engine that captures what AI coding agents do and makes that knowledge searchable and retrievable across sessions. It solves the problem that every coding agent forgets everything when a session ends, forcing developers to re-explain their architecture, preferences, and bugs repeatedly."*

The tagline distills it: **"Your coding agent remembers everything. No more re-explaining."**

The closing philosophy statement:

> *"Developers shouldn't re-explain their codebase to every new session. agentmemory captures context silently through hooks, compresses observations into a searchable knowledge base, and injects only the most relevant memories into each new session. One server, memories shared across all agents, zero manual effort."*

**Corpus placement:** This is the **first dedicated agent-memory-system** in the 65-wiki corpus. Prior corpus subjects touched memory tangentially — `graphify` (vault project) builds knowledge graphs; `claude-code-system-prompts` v65 documented Claude Code's *own* memory-instruction fragments — but agentmemory is the first subject whose **entire reason for existing is cross-session memory**. The named competitors (mem0 53K⭐, Letta/MemGPT 22K⭐) are not yet in the corpus.

## The headline claims (README "Key Statistics")

| Claim | Value | Source cited |
|---|---|---|
| Retrieval accuracy | **95.2% R@5** | LongMemEval-S, ICLR 2025 |
| Token efficiency | **92% fewer tokens** than pasting full context | ~170K tokens/year vs. 650K+ with LLM summarization |
| MCP tool count | **51 MCP tools** (extended mode) | — |
| Auto-capture | **12 hooks** | SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, PreCompact, SubagentStart/Stop, Stop, SessionEnd |
| External databases | **0** | SQLite + iii-engine only |
| Tests | **827 passing** | — |

These claims are the spine of the README's positioning. The **95.2% R@5** number is load-bearing — it anchors the competitive-comparison table (below) and the whole "this actually works" pitch.

## The 4-tier memory architecture

The README's central architectural idea — **memory consolidation modelled on human sleep**:

| Tier | Purpose | Human-memory analogy |
|---|---|---|
| **Working** | Raw observations from tool use | Short-term memory |
| **Episodic** | Compressed session summaries | "What happened" |
| **Semantic** | Extracted facts and patterns | "What I know" |
| **Procedural** | Workflows and decision patterns | "How to do it" |

> *"Memories decay over time (Ebbinghaus curve), strengthen with access, and auto-evict when stale."*

This is the project's most distinctive design stance: memory is not a flat store, it is a **tiered consolidation pipeline** where raw observations are progressively distilled into reusable knowledge, and unused memories *decay and evict themselves*. The Ebbinghaus forgetting curve is named explicitly — a **research-paper-chain intellectual lineage** (Axis 11 of the Phase 0 classification).

## Triple-stream search (RRF-fused)

Retrieval combines three independent signals:

1. **BM25** — *"Stemmed keyword matching with synonym expansion"*
2. **Vector** — *"Cosine similarity over dense embeddings"* (local `all-MiniLM-L6-v2` or API providers)
3. **Graph** — *"Knowledge graph traversal via entity matching"*

> *"Results fused with Reciprocal Rank Fusion (k=60) and session-diversified to max 3 per session."*

The fusion weights are tunable (`BM25_WEIGHT=0.4`, `VECTOR_WEIGHT=0.6`). The **graph stream is the structural link to vault project `graphify`** — both treat a knowledge graph as a first-class retrieval primitive. The "session-diversified to max 3 per session" detail is a notable anti-clumping discipline: retrieval won't return ten memories all from one past session.

## The competitive-comparison table

The README ships an explicit competitor table — corpus-rare directness:

| Feature | agentmemory | mem0 (53K⭐) | Letta/MemGPT (22K⭐) | Built-in (CLAUDE.md) |
|---|---|---|---|---|
| Retrieval R@5 | **95.2%** | 68.5% | 83.2% | N/A (grep) |
| Auto-capture | 12 hooks (zero effort) | Manual calls | Agent self-edit | Manual edit |
| Search strategy | BM25 + Vector + Graph (RRF) | Vector + Graph | Vector only | Loads all context |
| Multi-agent support | MCP + REST + leases + signals | API (uncoordinated) | Letta-only | Per-agent files |
| External dependencies | None (SQLite + iii-engine) | Qdrant/pgvector | Postgres + vector DB | None |
| Token efficiency | ~1,900/session ($10/yr) | Varies | Core memory in context | 22K+ at 240 obs |

**Note the "Built-in (CLAUDE.md)" column.** agentmemory positions itself *explicitly against the hand-maintained CLAUDE.md + grep approach* — which is exactly the approach the **Storm Bear vault currently uses** (CLAUDE.md working memory + a `memory/` directory maintained by hand). The README's claim — *"22K+ tokens at 240 observations"* for the manual approach — is the pitch directly relevant to Entity 4.

## The 51 MCP tools

**10 core tools (always available):**
`memory_recall` / `memory_smart_search` / `memory_save` / `memory_patterns` / `memory_file_history` / `memory_sessions` / `memory_timeline` / `memory_profile` / `memory_export` / `memory_relations`

**Extended tools (set `AGENTMEMORY_TOOLS=all`):** consolidation, graph queries, knowledge extraction, team sharing + audit trails, snapshots/actions/leases/signals, routines/sentinels/sketches/facet-tagging, governance/verification/health-diagnostics.

**Plus 6 Resources / 3 Prompts / 4 Skills.** The 4 skills are slash-command-style: `/recall`, `/remember`, `/session-history`, `/forget`.

The **core/extended split** is a deliberate context-economy choice — exposing only 10 tools by default keeps the agent's tool-list lean, with the full 51 opt-in.

## What gets automatically captured (the 12 hooks)

The README's pitch is **"zero manual effort"** — every hook fires automatically:

| Hook | Captures |
|---|---|
| SessionStart | Project path, session ID |
| UserPromptSubmit | User prompts (privacy-filtered) |
| PreToolUse | File access patterns + enriched context |
| PostToolUse | Tool name, input, output |
| PostToolUseFailure | Error context |
| PreCompact | **Re-injects memory before compaction** |
| SubagentStart/Stop | Sub-agent lifecycle |
| Stop | End-of-session summary |
| SessionEnd | Session complete marker |

The `PreCompact` hook is the cleverest: it re-injects relevant memory *into the context window right before Claude Code compacts it* — fighting context loss at exactly the moment it happens.

> **Privacy by design:** *"API keys, secrets, and `<private>` tags are stripped before storage."*

## Real-time tooling

- **Viewer (port 3113):** live observation stream, session explorer, memory browser, knowledge-graph visualization, health dashboard
- **iii Console:** OpenTelemetry traces on every memory operation, editable KV state, function invocation, live stream monitoring

The viewer being a **separate port** (3113 vs the 3111 API) and the iii Console giving OTEL traces "on every memory operation" both flow from the iii-engine foundation (Cluster 3).

## Configuration surface

**LLM providers** (auto-detected, *no default* — a deliberate choice after the v0.9.2 breaking change, see Cluster 2): Anthropic (`ANTHROPIC_API_KEY`), Gemini, OpenRouter, MiniMax (Anthropic-compatible).

**Embedding providers** (defaults to free local `all-MiniLM-L6-v2`): local (recommended, free, offline), OpenAI `text-embedding-3-small`, Voyage AI, Cohere, Gemini.

**Key environment variables:** `AGENTMEMORY_SECRET` (bearer token) / `AGENTMEMORY_AUTO_COMPRESS=false` (LLM-backed compression, off by default) / `AGENTMEMORY_SLOTS=false` (editable pinned memory slots) / `AGENTMEMORY_REFLECT=false` (auto-slot reflection) / `TOKEN_BUDGET=2000` (context injection limit) / `BM25_WEIGHT=0.4`, `VECTOR_WEIGHT=0.6`.

**Multi-provider on two independent axes** (LLM + embeddings), both vendor-diverse, both with safe free defaults — a **STRONG Pattern #28 Multi-Provider AI Support instance** (most corpus subjects are multi-provider on the LLM axis only).

## Pattern Library signals from Cluster 1

- **Pattern #8 Research-Benchmark Integration** — LongMemEval-S (ICLR 2025), 95.2% R@5; **first memory-retrieval-domain benchmark in corpus** (prior: ML-classification magika v44, pentesting shannon v45, agent-task Skyvern/OpenHands).
- **Pattern #28 Multi-Provider AI Support** — STRONG dual-axis instance (LLM + embeddings independently multi-provider, both with free defaults).
- **Pattern #19 Intellectual Lineage** — research-paper-chain archetype (Ebbinghaus forgetting curve + human sleep consolidation as named design influences).
- **Pattern #57 Recursive Corpus Reference** — explicit competitive-comparison vs the "Built-in CLAUDE.md" approach = the vault's own current method; structural sibling to `graphify` via the knowledge-graph search stream.
- **README over-claim flag (Finding #2)** — *"One server, memories shared across all agents"* in the philosophy statement is contradicted by the ROADMAP (Cluster 2), which lists cross-agent sharing as a Q3 2026 *candidate*. Cluster 1's marketing surface is ahead of the implementation surface.
