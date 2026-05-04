# (C) Entity 1 — Ruflo core product

> **EXTREME-compressed entity.** Due to ~500+ primitive count, this entity uses aggressive citation-not-replication. Full enumerations referenced upstream (README sections, `npx claude-flow mcp list`, ADR catalog, plugin marketplace).

## 1 | One-liner

Ruflo is a **self-learning AI agent orchestration platform** that transforms Claude Code (or OpenAI Codex CLI) into a multi-agent development environment with swarm coordination, vector memory, 313 MCP tools, and enterprise-grade governance. It does NOT execute code itself — it is a **coordination ledger** that orchestrates agents (Claude/Codex/others) doing the actual work.

## 2 | Surface area (EXTREME primitive count ~500+)

| Primitive family | Count | Examples | Where enumerated |
|------------------|-------|----------|------------------|
| **MCP tools** | **313** | `swarm_init`, `agent_spawn`, `memory_search`, `hooks_route`, `neural_train`, `hive-mind_init`, `agentdb_*`, `flow-nexus_*`, ... | `npx claude-flow mcp list` |
| **Specialized agents** | **100+** (README) / 60+ (v3.0.0-alpha.1) / 16 headline-roles + custom | coder, tester, reviewer, architect, researcher, security-architect, memory-specialist, performance-engineer, + custom | `npx claude-flow agent list` |
| **Skills (Codex path)** | 137+ | `$swarm-orchestration`, `$sparc-methodology`, `$hive-mind-advanced`, `$agentdb-vector-search`, `$flow-nexus-neural`, ... | `.agents/skills/` |
| **Skills (Claude path)** | 42+ | `/swarm-orchestration`, `/sparc-methodology`, ... | `.claude/skills/` |
| **CLI commands + subcommands** | 26 + 140+ | `swarm init`, `agent spawn`, `memory store`, `hooks pre-task`, `daemon start`, `doctor`, `init --wizard`, ... | `npx claude-flow --help` |
| **Hooks** | 17 | `pre-task`, `post-task`, `session-start`, `session-end`, `route`, `progress`, ... | `v3/@claude-flow/hooks/` |
| **Background workers** | 12 | ultralearn, audit, optimize, ... (context-triggered, auto-dispatch) | README Intelligence & Memory section |
| **RL algorithms** | 9 | Q-Learning, SARSA, A2C, PPO, DQN, Decision Transformer, Policy Gradient, Actor-Critic, REINFORCE | @ruvector/sona + neural/ |
| **Consensus protocols** | 5 | Byzantine (f<n/3), Raft, Gossip, CRDT, Quorum | swarm/consensus/ |
| **Topologies** | 6 | hierarchical, mesh, ring, star, hierarchical-mesh, adaptive | `--topology` flag |
| **AgentDB controllers** | 19 (8 activated v3.1.0-alpha.55) | HierarchicalMemory, MemoryConsolidation, SemanticRouter, GNNService, RVFOptimizer, MutationGuard, AttestationLog, GuardedVectorBackend, + 11 | ADR-053/055 |
| **Providers** | 6 | Anthropic, OpenAI, Google (Gemini), Cohere, Ollama, + cost-based failover | `v3/providers/` |
| **ADRs** | 70+ | ADR-001 (agentic-flow foundation), ADR-006 (unified memory), ADR-008 (Vitest), ADR-009 (hybrid memory), ADR-026 (3-tier routing), ADR-048 (auto-memory-bridge), ADR-049 (self-learning memory), ADR-056 (agentic-flow v3 integration) | `docs/adr/` |
| **DDD bounded contexts** | 5 | Core / Memory / Security / Integration / Coordination | CLAUDE.md + ADR system |
| **Plugin marketplace** | 8 official + 10 RuVector WASM | Gas Town Bridge, @claude-flow/teammate-plugin, RuVector plugins (50 MCP tools) | IPFS/Pinata registry CID in discovery.ts |
| **Pre-built collaboration templates** | 4 | feature, security, refactor, bugfix | `@claude-flow/codex dual templates` |

**Total: ~500+ distinct user-facing primitives.** This exceeds browser-use v41 RED (~200) by 2.5×; establishes **EXTREME tier** precedent.

## 3 | Architecture (RuVector intelligence stack)

**Core flow:** User → Ruflo (CLI/MCP) → Router → Swarm → Agents → Memory → LLM Providers → (Learning Loop back to Router).

**RuVector 9-component intelligence layer** (included with ruflo via @ruvector/* optional deps):

- **SONA** (<0.05ms): Self-Optimizing Pattern Learning — learns optimal routing
- **EWC++**: Elastic Weight Consolidation — prevents catastrophic forgetting
- **Flash Attention** (2.49-7.47× benchmarked): Optimized attention
- **HNSW**: Sub-millisecond vector search
- **ReasoningBank**: Pattern storage with RETRIEVE → JUDGE → DISTILL trajectory learning
- **Hyperbolic (Poincaré ball)**: Hierarchical code-relationship embeddings
- **LoRA / MicroLoRA**: Low-Rank Adaptation, lightweight
- **Int8 Quantization** (~4× memory): Weight compression
- **SemanticRouter**: Cosine-similarity intent routing
- **9 RL Algorithms**: task-specific learning

**Learning loop (ADR-049):** RETRIEVE (HNSW) → JUDGE (verdicts) → DISTILL (LoRA) → CONSOLIDATE (EWC++) → ROUTE (Q-learning).

## 4 | Swarm coordination (hive-mind)

- **3 Queen types:** Strategic (planning) / Tactical (execution) / Adaptive (optimization)
- **8 Worker types:** Researcher / Coder / Analyst / Tester / Architect / Reviewer / Optimizer / Documenter
- **Anti-Drift default:** `hierarchical` topology + maxAgents 6-8 + specialized strategy + raft consensus
- **Task → Agent routing:** Bug Fix (4 agents) / Feature (5 agents) / Refactor (4 agents) / Performance (3 agents) / Security (3 agents) / Memory (3 agents)

## 5 | 3-Tier Model Routing (ADR-026)

| Tier | Handler | Latency | Cost | Use Cases |
|------|---------|---------|------|-----------|
| 1 | Agent Booster (WASM) | <1ms | $0 | `var→const`, `add-types`, `remove-console`, `async-await`, `add-error-handling`, `add-logging` |
| 2 | Haiku / Sonnet | 500ms-2s | $0.0002-$0.003 | Bugs, refactoring, features |
| 3 | Opus | 2-5s | $0.015 | Architecture, security, distributed systems |

Routing mechanism: Q-learning with epsilon-greedy exploration, sub-ms decision latency.

**Token optimizer savings:** ReasoningBank -32% / Agent Booster -15% / Cache -10% / Optimal batch -20% / **Combined 30-50% reduction**.

## 6 | Memory architecture (ADR-006 / 009 / 048 / 049)

- **Vector memory:** HNSW sub-ms retrieval
- **Knowledge graph:** PageRank + community detection identifies influential insights
- **3-scope agent memory:** project / local / user (cross-agent transfer)
- **Embeddings:** ONNX Runtime + MiniLM (local, no API) / Tier-1 ReasoningBank WASM fallback
- **Persistence:** SQLite + AgentDB + PostgreSQL (RuVector, optional, 77+ SQL functions)
- **Auto Memory Bridge (ADR-048):** Claude Code ↔ AgentDB bidirectional sync
- **Hyperbolic embeddings:** Poincaré ball for hierarchical data

## 7 | Security surface

- **AIDefence:** Threat detection <10ms
- **Input validation:** Zod schemas for all public API inputs
- **SQL injection prevention:** parameterized queries
- **Path traversal prevention:** `PathValidator` module
- **Command injection protection:** `SafeExecutor` module
- **CVE hardening:** bcrypt, timing attack fixes, eliminated hardcoded HMAC keys (v3.5 release-note)
- **TOCTOU race fix:** Promise-based singleton caching
- **Vulnerability reporting:** security@cognitum.one / security@ruv.io

**0 Production Vulnerabilities** claimed across all packages (v3.5 release note via `npm audit`).

## 8 | Distribution

- npm `ruflo@latest` + `claude-flow@3.5.80` + `@claude-flow/cli@3.5.65` (triple-package)
- curl install: `curl -fsSL https://cdn.jsdelivr.net/gh/ruvnet/ruflo@main/scripts/install.sh | bash`
- npx: `npx ruflo@latest init --wizard`
- Global: `npm install -g ruflo@latest`
- Bun: `bunx ruflo@latest init`
- Claude Code MCP registration: `claude mcp add ruflo -- npx -y ruflo@latest mcp start`
- Codex CLI: `codex mcp add ruflo -- npx ruflo mcp start` (auto-registered via `init --codex`)
- Dual-mode: `npx ruflo@latest init --dual`

**Install profiles:**
- `--omit=optional` ~45 MB core CLI only
- Default ~340 MB full install (includes ML/embeddings)

## 9 | Dual-mode Claude+Codex (ADR `@claude-flow/codex`)

**Division of labor:**
- claude-flow = LEDGER (tracks state, coordinates, stores memory)
- Claude / Codex = EXECUTORS (write code, run commands, implement)

**Platform strengths (README verbatim):**
- 🔵 Claude: Architecture / Security review / Testing strategy
- 🟢 Codex: Implementation / Performance optimization / Refactoring

**Pre-built templates:** feature / security / refactor / bugfix (4 pipelines).

## 10 | Cross-wiki comparison (tier positioning)

| Wiki | Tier | Archetype | Scale | MCP tools | Agents | Pattern Library touchpoints |
|------|------|-----------|-------|-----------|--------|------------------------------|
| **ruflo v42** | **T2 + T1 secondary** | **Solo-flagship-multi-sibling-ecosystem + commercial** | **33K / 16mo** | **313** | **100+** | **#17 variant 1 (13th+) + #18 (strongest MCP evidence) + #20 (4th solo-enterprise) + #31 (6th) + #50 (5th) + #58 un-stale + #12 counter-evidence + #22 + #28 + #27** |
| OMC v27 | T1 | Korean solo-multi-runtime | 30K / 3.5mo | (MCP via runtimes) | 19 specialized | #17 variant 5 / #18 / #27 / #56 / #57 / #58 founding / #59 |
| agency-agents v18 | T1 | US solo-at-enterprise | 82.9K / 12mo | 0 explicit | 144 persona | #17 v1 / #20 solo-at-enterprise founding / #24 / #25 retired / #26 / #27 |
| multica v15 | T2 | CN community-platform | 16.2K | explicit vectors | 8 agents (teammate concept) | #16 / #17 / #18 / #9 Resolution D T2 |
| goclaw v4 | T2 | Multi-tenant corporate-ish | medium | explicit | corporate-ish | #9 Resolution D T2 foundational |

## 11 | Unique architectural signature

Ruflo is distinct from ALL prior corpus entrants in:
1. **Coordination-ledger positioning** (not executor) — first corpus framework explicitly non-executing
2. **9-component neural/ML intelligence stack** — first corpus T2 with full SONA/EWC++/HNSW/Hyperbolic/LoRA/MoE/Flash Attention suite
3. **313 MCP tools** — 20× prior corpus max
4. **Dual-runtime first-class** (Claude + Codex with dedicated `@claude-flow/codex` sibling package)
5. **IPFS/Pinata plugin registry** — decentralized plugin distribution
6. **Rust WASM kernels for policy engine + embeddings + proof system** — corpus-first
7. **70+ ADRs with `hooks progress` validation gates** — largest-documented ADR enforcement surface
8. **Triple-package parallel distribution** (claude-flow + ruflo + @claude-flow/cli)

## 12 | Sources

- `README.md` (7,541 lines / 280 KB)
- `CLAUDE.md` (1,094 lines / 38.9 KB)
- `AGENTS.md` (634 lines / 20.7 KB)
- `CLAUDE.local.md` (1.8 KB)
- `SECURITY.md` (53 lines)
- `CHANGELOG.md` (235 lines)
- `package.json` (main v3.5.80 via WebFetch)

## 13 | Cross-references

- Entity 2: `(C) RuvNet ecosystem portfolio + Cognitum.One + Agentics Foundation.md`
- Entity 3: `(C) T1 vs T2 tier decision + Pattern 18 MCP-scale outlier + EXTREME primitive-count precedent.md`
- Entity 4: `(C) Storm Bear meta — 31st consecutive + EXTREME-tier compression lesson.md`
- Sibling wikis: OMC v27 / agency-agents v18 / multica v15 / goclaw v4 / GitNexus v33 (MCP precedent) / OpenHands v30 (ADR-driven)
