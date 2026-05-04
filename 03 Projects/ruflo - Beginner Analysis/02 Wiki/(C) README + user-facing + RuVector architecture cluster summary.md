# (C) Cluster 1 — README + user-facing + RuVector intelligence architecture

> Source: `README.md` (280.6 KB, 7,541 lines — **largest README in Storm Bear corpus**). Ruflo v3.5 (brand) / claude-flow v3.5.80 (primary npm package).

## 1 | Positioning (verbatim)

- **Top headline:** "🌊 RuFlo v3.5: Enterprise AI Orchestration Platform"
- **Sub-headline:** "Multi-agent AI orchestration for Claude Code. Deploy 16 specialized agent roles + custom types in coordinated swarms with self-learning capabilities, fault-tolerant consensus, and enterprise-grade security."
- **Origin-of-name statement:** "Claude Flow is now Ruflo — named by Ruv, who loves Rust, flow states, and building things that feel inevitable. The 'Ru' is the Ruv. The 'flo' is the flow. Underneath, WASM kernels written in Rust power the policy engine, embeddings, and proof system. 6,000+ commits later, this is v3.5."
- **Onboarding claim:** "You don't need to learn 310+ MCP tools or 26 CLI commands. After running init, just use Claude Code normally — the hooks system automatically routes tasks to the right agents, learns from successful patterns, and coordinates multi-agent work in the background."
- **Core value prop:** "Extend your Claude Code subscription by 250%" via intelligent 3-tier routing (WASM / Haiku / Sonnet-Opus)

## 2 | Key capabilities (README verbatim summary)

| # | Capability | Verbatim claim |
|---|-----------|---------------|
| 1 | **100+ Specialized Agents** | "Ready-to-use AI agents for coding, code review, testing, security audits, documentation, and DevOps" |
| 2 | **Coordinated Agent Teams** | "Run unlimited agents simultaneously in organized swarms" (hierarchical queen/workers OR mesh peer-to-peer) |
| 3 | **Learns From Your Workflow** | "Successful patterns are stored and reused, routing similar tasks to the best-performing agents. Gets smarter over time" |
| 4 | **Works With Any LLM** | "Switch between Claude, GPT, Gemini, Cohere, or local models like Llama. Automatic failover" |
| 5 | **Plugs Into Claude Code** | "Native integration via MCP (Model Context Protocol)" |
| 6 | **Production-Ready Security** | "Prompt injection protection, input validation, path traversal prevention, command injection blocking" |
| 7 | **Extensible Plugin System** | "Share plugins via the decentralized IPFS marketplace" |

## 3 | RuVector intelligence stack (corpus-first 9-component ML architecture)

| Component | Purpose | Verbatim performance claim |
|-----------|---------|---------------------------|
| **SONA** | Self-Optimizing Pattern Learning | "<0.05ms" / "Fast adaptation" |
| **EWC++** | Elastic Weight Consolidation — prevents catastrophic forgetting | "Preserves learned patterns" |
| **Flash Attention** | Optimized attention computation | "2.49-7.47× speedup (benchmarked)" |
| **HNSW** | Hierarchical Navigable Small World vector search | "Sub-millisecond retrieval" |
| **ReasoningBank** | Pattern storage with trajectory learning | "RETRIEVE → JUDGE → DISTILL" |
| **Hyperbolic** | Poincaré ball embeddings for hierarchical data | "Better code relationships" |
| **LoRA / MicroLoRA** | Low-Rank Adaptation for efficient fine-tuning | "Lightweight adaptation" |
| **Int8 Quantization** | Memory-efficient weight storage | "~4× memory reduction" |
| **SemanticRouter** | Semantic task routing with cosine similarity | "Fast intent routing" |
| **9 RL Algorithms** | Q-Learning, SARSA, A2C, PPO, DQN, Decision Transformer, etc. | "Task-specific learning" |

## 4 | Learning loop (ADR-049 — RETRIEVE → JUDGE → DISTILL → CONSOLIDATE → ROUTE)

```
1. LEARN: memory_search(query="task keywords", namespace="patterns")
   → If score > 0.7, USE that pattern
2. COORDINATE: swarm_init(topology="hierarchical")
   → agent_spawn(type="coder", name="worker-1")
3. EXECUTE: [user/Codex] writes code, runs commands
4. REMEMBER: memory_store(key, value, namespace="patterns")
```

## 5 | Swarm architecture (hive-mind)

- **Queen types (3):** Strategic (planning) / Tactical (execution) / Adaptive (optimization)
- **Worker types (8):** Researcher / Coder / Analyst / Tester / Architect / Reviewer / Optimizer / Documenter
- **Consensus algorithms (3 primary):** Majority / Weighted (Queen 3×) / Byzantine (f < n/3)
- **Extended consensus (5 total):** + Raft / Gossip / CRDT / Quorum
- **Topologies (6):** hierarchical / mesh / ring / star / hierarchical-mesh / adaptive

**Anti-Drift default configuration:**
```javascript
swarm_init({
  topology: "hierarchical",
  maxAgents: 8,
  strategy: "specialized"
})
```

Rationale: hierarchical = coordinator validates outputs / maxAgents 6-8 = less drift surface / specialized = clear role boundaries / raft consensus = leader maintains authoritative state.

## 6 | 3-Tier Model Routing (ADR-026) — "Extend Claude Code subscription by 250%"

| Tier | Handler | Latency | Cost | Use Cases |
|------|---------|---------|------|-----------|
| **1** | Agent Booster (WASM) | <1ms | $0 | Simple transforms: `var→const`, `add-types`, `remove-console`, `async-await`, `add-error-handling`, `add-logging` |
| **2** | Haiku / Sonnet | 500ms-2s | $0.0002-$0.003 | Bug fixes, refactoring, feature implementation |
| **3** | Opus | 2-5s | $0.015 | Architecture, security design, distributed systems |

Routing: Q-learning with epsilon-greedy exploration, sub-ms decision latency.

## 7 | Token Optimizer savings (stacked multiplicatively)

| Optimization | Savings |
|-------------|---------|
| ReasoningBank retrieval | -32% |
| Agent Booster edits | -15% |
| Cache (95% hit rate) | -10% |
| Optimal batch size | -20% |
| **Combined** | **30-50%** |

## 8 | Memory architecture (ADR-006 / ADR-009 / ADR-048 / ADR-049)

| Layer | Components | What It Does |
|-------|-----------|--------------|
| Memory | HNSW, AgentDB, Cache | Stores + retrieves patterns with fast HNSW search |
| Knowledge Graph | MemoryGraph, PageRank, Communities | Identifies influential insights (ADR-049) |
| Self-Learning | LearningBridge, SONA, ReasoningBank | Triggers learning from insights, confidence lifecycle |
| Agent Scopes | AgentMemoryScope, 3-scope dirs | Per-agent isolation + cross-agent transfer (project/local/user) |
| Embeddings | ONNX Runtime, MiniLM | Local vectors without API calls |
| Learning | SONA, MoE, ReasoningBank | Self-improves from results |
| Fine-tuning | MicroLoRA, EWC++ | Lightweight adaptation without full retraining |

## 9 | Plugin marketplace (IPFS/Pinata — corpus-first decentralized agent-plugin distribution)

- **IPFS registry CID** stored in `v3/@claude-flow/cli/src/plugins/store/discovery.ts`
- **Gateway:** `https://gateway.pinata.cloud/ipfs/{CID}`
- **Official plugins:** 8
- **RuVector WASM plugins:** 10 (50 MCP tools)
- **@claude-flow/teammate-plugin:** Agent Teams coordination MCP tools
- **Gas Town Bridge plugin:** WASM-accelerated orchestrator integration

## 10 | Installation surface

```bash
# One-line curl (recommended)
curl -fsSL https://cdn.jsdelivr.net/gh/ruvnet/ruflo@main/scripts/install.sh | bash

# npx
npx ruflo@latest init --wizard

# Global
npm install -g ruflo@latest

# Bun
bunx ruflo@latest init

# Codex CLI init
npx ruflo@latest init --codex

# Dual-mode (Claude + Codex)
npx ruflo@latest init --dual
```

**Install profiles:**
- `--omit=optional` ~45 MB core CLI only
- Default ~340 MB full install with ML/embeddings

**Speed:** npx cached ~3s / npx fresh ~20s / global ~35s / `--minimal` ~15s

## 11 | Claude Code vs Claude Code + Ruflo (comparison table verbatim)

| Capability | Claude Code Alone | Claude Code + Ruflo |
|------------|-------------------|---------------------|
| Agent Collaboration | Agents work in isolation | Swarms with shared memory + consensus |
| Coordination | Manual orchestration | Queen-led hierarchy, 3 consensus algorithms |
| Hive Mind | ⛔ Not available | 🐝 Queen-led, 3 queen types, 8 worker types |
| Consensus | ⛔ No multi-agent decisions | Byzantine (f < n/3), weighted, majority |
| Memory | Session-only | HNSW vector memory + knowledge graph |
| Vector Database | ⛔ | 🐘 RuVector PostgreSQL 77+ SQL functions, ~61µs search, 16,400 QPS |
| Knowledge Graph | ⛔ | PageRank + community detection (ADR-049) |
| Collective Memory | ⛔ | 8 memory types, LRU cache, SQLite |
| Learning | Static behavior | SONA self-learning sub-ms pattern matching |
| Agent Scoping | Single project | 3-scope (project/local/user) cross-agent transfer |
| Task Routing | You decide | Learned patterns (89% accuracy claim) |
| Complex Tasks | Manual breakdown | Auto-decomposition across 5 domains |
| Background Workers | ⛔ | 12 context-triggered auto-dispatch |
| LLM Provider | Anthropic only | 5 providers + failover + cost-based routing |
| Security | Standard | CVE-hardened + bcrypt + input validation + path traversal prevention |

## 12 | Spec-Driven Development (ADR system)

- **70+ ADRs** defining system behavior, integration patterns, security requirements
- **5 DDD bounded contexts:** Core / Memory / Security / Integration / Coordination
- **Drift detection:** statusline shows ADR compliance %
- **Validation gates:** `hooks progress` blocks merges that violate specifications
- **Key ADRs cited in README:**
  - ADR-001: agentic-flow@alpha as foundation
  - ADR-006: Unified Memory Service with AgentDB
  - ADR-008: Vitest testing framework (10× faster than Jest)
  - ADR-009: Hybrid Memory Backend (SQLite + HNSW)
  - ADR-026: Intelligent 3-tier model routing
  - ADR-048: Auto Memory Bridge (Claude Code ↔ AgentDB bidirectional sync)
  - ADR-049: Self-Learning Memory with GNN (LearningBridge, MemoryGraph, AgentMemoryScope)
  - ADR-056: agentic-flow v3 Integration Architecture

## 13 | Competitor comparison framing (corpus-first explicit 5-way table)

Ruflo v3 vs CrewAI / LangGraph / AutoGen / Manus across 4 axes:
- **Neural & Learning:** Ruflo uniquely claims SONA + EWC++ + pattern-learning + MoE + Flash Attention + LoRA (all "✅" vs all competitors "⛔")
- **Memory & Embeddings:** Ruflo uniquely claims Vector memory + knowledge graph + self-learning memory + 3-scope agent-memory + PostgreSQL RuVector + hyperbolic + Int8 quant + GNN/attention in SQL
- **Swarm & Coordination:** Ruflo 4 topologies vs 1 each / 5 consensus vs 0 / 12 background workers vs 0 / 6 multi-provider vs 1-3
- **Developer Experience:** MCP 313 tools vs 0 / skills 42+ vs 0 / stream pipelines / pair programming / auto-updates

**Self-positioning:** "self-learning neural capabilities that no other agent orchestration framework offers"

## 14 | Corpus-first observations (user-facing surface)

1. **Largest README in Storm Bear corpus** — 280.6 KB / 7,541 lines (prior: browser-use v41 ~60 KB; markitdown v28 ~30 KB)
2. **313 MCP tools** — corpus-most by ~20× (prior: GitNexus v33 = 16 tools)
3. **100+ agents** — largest single-project agent library in corpus (prior: agency-agents v18 = 144, but those are persona templates; ruflo's are fully wired)
4. **9 RL algorithms named** — first explicit RL-algorithm-enumeration at T2 scale
5. **WASM kernels in Rust for policy engine** — first explicit Rust-WASM agent-runtime kernel in corpus
6. **IPFS/Pinata decentralized plugin registry** — first corpus agent plugin distribution via IPFS (vs npm-only or marketplace-only)
7. **Triple-package parallel distribution** (claude-flow / ruflo / @claude-flow/cli) — first corpus triple-package-same-codebase pattern
8. **70+ ADR surface** — largest ADR catalog in corpus (prior: OpenHands v30 had ADRs but ~20-30)
9. **5-way competitor comparison in README** — corpus-first explicit Manus/CrewAI/LangGraph/AutoGen framing
10. **"250% extend Claude Code" + token optimizer 30-50%** — first explicit dollar-value ROI claim in corpus

## 15 | Absences (counter-evidence signals)

- **No Karpathy lineage** cited (Pattern #19 archetype 4 no-lineage at T2)
- **No research-paper citations** (Pattern #8 absent — claims "benchmarked" but no external validation)
- **No academic-lab affiliation** (Pattern #44 absent)
- **No i18n** (EN-only at T2 enterprise scale — absence signal vs OMC v27 7-lang at T1)
- **No dual-licensing** (MIT single)
- **No explicit SWE-Bench / WebBench / benchmark leaderboard** (contrast OpenHands v30 + browser-use v41)
- **No peer-reviewed publication** (contrast LlamaFactory v22 ACL 2024)
