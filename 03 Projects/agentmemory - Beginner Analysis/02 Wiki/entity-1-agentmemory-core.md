# Entity 1 — agentmemory core artifact

> **Type:** Foundation entity (what agentmemory IS / what it DOES)
> **Cross-references:** [Cluster 1 README](./cluster-1-readme-and-positioning.md) / [Cluster 2 governance](./cluster-2-contributor-docs-and-governance.md) / [Cluster 3 iii-foundation](./cluster-3-iii-foundation-and-distribution.md)

## Identity

| Field | Value |
|---|---|
| **Full name** | agentmemory — persistent memory engine for AI coding agents |
| **Author** | **Rohit Ghumare** (`ghumare64@gmail.com`) — solo individual engineer |
| **Repo** | [`github.com/rohitg00/agentmemory`](https://github.com/rohitg00/agentmemory) |
| **Package** | `@agentmemory/agentmemory` v0.9.12 (npm) |
| **License** | Apache-2.0 |
| **Stack** | TypeScript 82.4% (+ HTML 8.7% / JS 6.7% / CSS 1.5% / Python 0.7%) |
| **First release** | `[0.8.0]` — 2026-04-09 (CHANGELOG); latest v0.9.12 — 2026-05-13 |
| **Repo age at v66 ship** | ~35 days (first-release proxy; exact creation date not retrievable) |
| **Stars / forks / subscribers** | **7,900 / 675 / 23** |
| **Stars-per-day** | ~226 (HIGH velocity; just below Pattern #52 EXTREME-VIRAL 300/day flag) |
| **Issues / PRs / commits / releases** | 28 / 51 / 301 / 34 |
| **Scale / units** | 118 source files · ~21,800 LOC · 827 tests · 123 functions · **34 KV scopes** |

## Function

A **persistent memory engine** that captures what AI coding agents do, compresses it into a tiered, searchable knowledge base, and injects only the most relevant memories back into each new session — *"zero manual effort,"* via lifecycle hooks.

**The problem it targets** (README): *"every coding agent forgets everything when a session ends, forcing developers to re-explain their architecture, preferences, and bugs repeatedly."*

**What it IS:**
- A long-lived **server process** — REST API on port 3111, real-time viewer on port 3113
- A **51-tool MCP server** + **107-endpoint REST API** + a **12-hook auto-capture plugin**
- A **4-tier memory consolidation pipeline** with decay/strengthen/evict dynamics
- A **triple-stream (BM25 + Vector + Graph) RRF-fused** retrieval engine

**What it IS NOT:**
- Not an agent or assistant itself (it has no autonomy; it serves memory to agents)
- Not a methodology or framework-with-opinions (no SDD-style workflow)
- Not a hosted SaaS — the ROADMAP *"deliberately excludes"* a cloud offering
- Not (yet) fully cross-agent — see Entity 3 / Cluster 2 Finding #2: shared *backend*, but cross-agent *sharing* of that backend is partly still on the ROADMAP

## The 4-tier memory consolidation pipeline

The single most distinctive design idea — memory modelled on **human sleep consolidation**:

```
   tool use
      │
      ▼
┌─────────────┐   compress    ┌─────────────┐   extract    ┌─────────────┐   distill   ┌──────────────┐
│   WORKING   │ ────────────▶ │  EPISODIC   │ ───────────▶ │  SEMANTIC   │ ──────────▶ │  PROCEDURAL  │
│ raw observ. │               │ session     │              │ facts +     │             │ workflows +  │
│ "short-term"│               │ summaries   │              │ patterns    │             │ decisions    │
│             │               │"what happened"             │"what I know"│             │"how to do it"│
└─────────────┘               └─────────────┘              └─────────────┘             └──────────────┘
```

Across all tiers: memories **decay over time (Ebbinghaus forgetting curve)**, **strengthen with access**, and **auto-evict when stale**. This is not a flat key-value store with a TTL — it is a *consolidation pipeline* where raw observations are progressively refined into reusable knowledge, and the system actively forgets what it doesn't use.

The naming of the Ebbinghaus curve + sleep consolidation is a **research-paper-chain intellectual lineage** (Pattern #19) — agentmemory borrows its core metaphor from cognitive science, not from software architecture.

## Triple-stream RRF search

Retrieval runs three independent signals in parallel and fuses them:

| Stream | Signal | Implementation |
|---|---|---|
| **BM25** | keyword | stemmed matching + synonym expansion |
| **Vector** | semantic | cosine similarity over dense embeddings (`all-MiniLM-L6-v2` local, or API) |
| **Graph** | relational | knowledge-graph traversal via entity matching |

Fusion: **Reciprocal Rank Fusion, k=60**, then **session-diversified to max 3 results per session** (an anti-clumping discipline so retrieval doesn't return ten memories from one past session). Weights are tunable: `BM25_WEIGHT=0.4`, `VECTOR_WEIGHT=0.6`.

The **Graph stream** is the structural bridge to vault project [`graphify`](../../graphify%20-%20Beginner%20Analysis/02%20Wiki/) — both treat a knowledge graph as a first-class retrieval primitive rather than a visualization afterthought.

## The 12 auto-capture hooks

The "zero manual effort" promise rests on lifecycle hooks that fire automatically:

`SessionStart` · `UserPromptSubmit` (privacy-filtered) · `PreToolUse` · `PostToolUse` · `PostToolUseFailure` · **`PreCompact`** · `SubagentStart` · `SubagentStop` · `Stop` · `SessionEnd`

The cleverest is **`PreCompact`** — it *re-injects relevant memory into the context window right before Claude Code compacts it*, fighting context loss at the exact moment it occurs. Codex CLI gets a 6-hook subset.

**Privacy by design:** API keys, secrets, and `<private>`-tagged content are stripped before storage.

## The 51 MCP tools (10 core + extended)

**10 core (always exposed):** `memory_recall` / `memory_smart_search` / `memory_save` / `memory_patterns` / `memory_file_history` / `memory_sessions` / `memory_timeline` / `memory_profile` / `memory_export` / `memory_relations`.

**Extended (opt-in via `AGENTMEMORY_TOOLS=all`):** consolidation, graph queries, knowledge extraction, team sharing + audit trails, snapshots/actions/leases/signals, routines/sentinels/sketches/facet-tagging, governance/verification/health.

Plus **6 Resources / 3 Prompts / 4 Skills** (`/recall`, `/remember`, `/session-history`, `/forget`). The **core/extended split is a deliberate context-economy choice** — 10 tools by default keeps the agent's tool-list lean; the full 51 are there when needed.

## Benchmark posture

| Metric | agentmemory | mem0 | Letta/MemGPT | Built-in CLAUDE.md |
|---|---|---|---|---|
| **Retrieval R@5** | **95.2%** | 68.5% | 83.2% | N/A (grep) |
| Token efficiency | ~1,900/session (~$10/yr) | varies | core memory in-context | 22K+ at 240 obs |

Benchmark: **LongMemEval-S, ICLR 2025.** This is the **first memory-retrieval-domain benchmark in the 65-wiki corpus** (Pattern #8). The competitive-comparison table is corpus-rare in its directness — most subjects don't name competitors with star counts.

## Verification status of the claims

Per Storm Bear's "NEVER fabricate" rule, the claims in this entity are **as-stated by the project, not independently verified by this wiki**:
- The 95.2% R@5 number is the *project's* benchmark result; the `benchmark/` directory holds the harness but this wiki did not re-run it.
- The "827 tests passing" is the CHANGELOG's claim as of v0.9.2.
- Cluster 2 Finding #4 (6 CRITICAL/HIGH vulns at v0.8.2) is a documented reason for *measured* skepticism about the v0.8.x claims specifically — the v0.9.x design is the credible one.

## Pattern Library implications snapshot

- **Pattern #8 Research-Benchmark Integration** — first memory-retrieval-domain benchmark in corpus (LongMemEval-S, ICLR 2025)
- **Pattern #28 Multi-Provider AI Support** — STRONG dual-axis instance (LLM + embeddings independently multi-provider, both free-defaulted)
- **Pattern #19 Intellectual Lineage** — research-paper-chain archetype (Ebbinghaus + sleep consolidation as named design influences)
- **Pattern #57 Recursive Corpus Reference** — explicit comparison vs the "Built-in CLAUDE.md" approach (= the vault's own current method); graph-stream sibling to graphify
- See **Entity 2** for the PRIMARY deliverable (Platform-Primitive Foundation), **Entity 3** for distribution + the quality-maturity tension, **Entity 4** for the Storm Bear pilot framing

## Why this entity matters

This is the **foundation reference** for what agentmemory IS as an artifact — the 4-tier pipeline, triple-stream search, hooks, and tool surface. The other three entity pages build on it:
- **Entity 2** isolates the corpus-first structural observation (built entirely on iii-engine's primitives)
- **Entity 3** covers how it's distributed + integrated, and the viral-velocity-vs-quality tension
- **Entity 4** asks the question this entity sets up: *should the Storm Bear vault actually deploy this?*
