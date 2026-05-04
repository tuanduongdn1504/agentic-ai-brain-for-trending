# (C) Cluster 2 — CLAUDE.md + AGENTS.md + governance + behavioral rules

> Sources: `CLAUDE.md` (38.9 KB, 1,094 lines — corpus-large at T2), `AGENTS.md` (20.7 KB, 634 lines — substantial), `CLAUDE.local.md` (1.8 KB), `SECURITY.md` (1.9 KB, 53 lines).

## 1 | CLAUDE.md positioning header (verbatim)

```
# Claude Code Configuration - Ruflo v3.5

> Ruflo v3.5 (2026-04-07) — Stable release with verified capabilities.
> 6,000+ commits, 314 MCP tools, 16 agent roles + custom types, 19 AgentDB controllers.
> Packages: @claude-flow/cli@3.5.65, claude-flow@3.5.65, ruflo@3.5.65
```

**Note:** README top-line says "313 MCP tools" (at "Claude Code can use all 313 ruflo MCP tools"), CLAUDE.md says "314". Minor discrepancy suggests hand-maintained count drift.

## 2 | Behavioral Rules (always enforced)

Verbatim enumeration:
1. Do what has been asked; nothing more, nothing less
2. NEVER create files unless absolutely necessary for achieving your goal
3. ALWAYS prefer editing an existing file to creating a new one
4. NEVER proactively create documentation files (*.md) or README files unless explicitly requested
5. NEVER save working files, text/mds, or tests to the root folder
6. Never continuously check status after spawning a swarm — wait for results
7. ALWAYS read a file before editing it
8. NEVER commit secrets, credentials, or .env files

## 3 | File Organization (verbatim)

- NEVER save to root folder — use the directories below
- `/src` — source code files
- `/tests` — test files
- `/docs` — documentation and markdown files
- `/config` — configuration files
- `/scripts` — utility scripts
- `/examples` — example code

## 4 | Project Architecture rules (verbatim)

- Follow Domain-Driven Design with bounded contexts
- Keep files under 500 lines
- Use typed interfaces for all public APIs
- Prefer TDD London School (mock-first) for new code
- Use event sourcing for state changes
- Ensure input validation at system boundaries

## 5 | Key v3 monorepo packages (from CLAUDE.md)

| Package | Path | Purpose |
|---------|------|---------|
| `@claude-flow/cli` | `v3/@claude-flow/cli/` | CLI entry point (26 commands) |
| `@claude-flow/codex` | `v3/@claude-flow/codex/` | Dual-mode Claude + Codex collaboration |
| `@claude-flow/guidance` | `v3/@claude-flow/guidance/` | Governance control plane |
| `@claude-flow/hooks` | `v3/@claude-flow/hooks/` | 17 hooks + 12 workers |
| `@claude-flow/memory` | `v3/@claude-flow/memory/` | AgentDB + HNSW search |
| `@claude-flow/security` | `v3/@claude-flow/security/` | Input validation, CVE remediation |

## 6 | Concurrency rules — "1 MESSAGE = ALL RELATED OPERATIONS" (verbatim)

- All operations MUST be concurrent/parallel in a single message
- Use Claude Code's Task tool for spawning agents, not just MCP

**Mandatory batching patterns:**
- ALWAYS batch ALL todos in ONE TodoWrite call (5-10+ minimum)
- ALWAYS spawn ALL agents in ONE message with full instructions via Task tool
- ALWAYS batch ALL file reads/writes/edits in ONE message
- ALWAYS batch ALL terminal operations in ONE Bash message
- ALWAYS batch ALL memory store/retrieve operations in ONE message

## 7 | Dual-Mode Collaboration (Claude Code + Codex) — corpus-first explicit dual-runtime governance

**Key premise:** "Ruflo runs Claude Code (🔵) and OpenAI Codex (🟢) workers in parallel with shared memory coordination."

**Platform strengths (verbatim):**

| Task Type | Preferred Platform | Reason |
|-----------|-------------------|--------|
| Architecture & Design | 🔵 Claude | Strong reasoning, system thinking |
| Implementation | 🟢 Codex | Fast code generation |
| Security Review | 🔵 Claude | Careful analysis, threat modeling |
| Performance Optimization | 🟢 Codex | Code-level optimizations |
| Testing Strategy | 🔵 Claude | Coverage analysis, edge cases |
| Refactoring | 🟢 Codex | Bulk code transformations |

**Pre-built collaboration templates:**

| Template | Workers | Pipeline |
|----------|---------|----------|
| `feature` | 🔵 Architect → 🟢 Coder → 🔵 Tester → 🟢 Reviewer | Full feature development |
| `security` | 🔵 Analyst → 🟢 Scanner → 🔵 Reporter | Security audit workflow |
| `refactor` | 🔵 Architect → 🟢 Refactorer → 🔵 Tester | Code modernization |
| `bugfix` | 🔵 Researcher → 🟢 Coder → 🔵 Tester | Bug investigation & fix |

## 8 | AGENTS.md positioning (Codex-first)

- Header: "Claude Flow V3 - Agent Guide. For OpenAI Codex CLI — Agentic AI Foundation standard"
- Skills syntax: `$skill-name` (Codex) vs `/skill-name` (Claude)
- Config: `.agents/config.toml`
- TL;DR (verbatim):
  1. claude-flow = LEDGER (tracks state, stores memory, coordinates)
  2. Codex = EXECUTOR (writes code, runs commands, creates files)
  3. NEVER stop after calling claude-flow — IMMEDIATELY continue working
  4. If you need something BUILT/EXECUTED, YOU do it, not claude-flow
  5. ALWAYS search memory BEFORE starting
  6. ALWAYS store patterns AFTER success

## 9 | Division of Labor (CRITICAL framing — verbatim)

```
┌─────────────────────────────────────────────────────────────┐
│  CLAUDE-FLOW = ORCHESTRATOR (tracks state, coordinates)     │
│  CODEX = WORKER (writes code, runs commands, implements)    │
└─────────────────────────────────────────────────────────────┘
```

**Significant corpus observation:** Ruflo explicitly positions itself NOT as an executor but as a **state-tracking ledger + coordination layer**. Agents (Claude or Codex) do the actual work. This is architecturally distinct from agency-agents v18 (executing persona library), multica v15 (managed-agents-platform), OMC v27 (orchestration of runtimes that themselves coordinate).

## 10 | Skills system (Codex path)

Verbatim skill catalog (categories):

| Category | Examples |
|----------|----------|
| V3 Core | `$v3-security-overhaul`, `$v3-memory-unification`, `$v3-performance-optimization` |
| AgentDB | `$agentdb-vector-search`, `$agentdb-optimization`, `$agentdb-learning` |
| Swarm | `$swarm-orchestration`, `$swarm-advanced`, `$hive-mind-advanced` |
| GitHub | `$github-code-review`, `$github-workflow-automation`, `$github-multi-repo` |
| SPARC | `$sparc-methodology`, `$sparc:architect`, `$sparc:coder`, `$sparc:tester` |
| Flow Nexus | `$flow-nexus-neural`, `$flow-nexus-swarm`, `$flow-nexus:workflow` |
| Dual-Mode | `$dual-spawn`, `$dual-coordinate`, `$dual-collect` |

**137+ skills total** (Codex path); 42+ skills (Claude path; listed separately in `.claude/skills/`).

**"Flow Nexus" naming** = cloud-tier commercial product referenced (e.g., `$flow-nexus-neural` skills); suggests open-core commercial boundary.

## 11 | SECURITY.md (verbatim 53 lines — mid-sized)

- Supported versions: 3.5.x only. 3.0-3.4 NO. 2.x NO.
- Report vulnerabilities: `security@cognitum.one` — **corpus-first Cognitum.One email domain** explicitly identifies commercial parent entity
- Response timeline: 48h ack / 7d preliminary / 30d fix target
- Safe harbor: good-faith research authorized
- Security practices:
  - Input validation using Zod schemas
  - Parameterized SQL queries
  - Path traversal prevention via `PathValidator` module
  - Command injection protection via `SafeExecutor` module
- Contact secondary: `security@ruv.io` ("For questions about this policy")

**Dual commercial email addresses:** `security@cognitum.one` (primary vulnerability reports) + `security@ruv.io` (policy questions) — 2-domain commercial structure.

## 12 | Topologies (verbatim AGENTS.md CLI reference)

| Topology | Use Case | Flag |
|----------|----------|------|
| `hierarchical` | Coordinated teams, anti-drift | `--topology hierarchical` |
| `mesh` | Peer-to-peer, equal agents | `--topology mesh` |
| `hierarchical-mesh` | Hybrid (recommended for V3) | `--topology hierarchical-mesh` |
| `ring` | Sequential processing | `--topology ring` |
| `star` | Central coordinator | `--topology star` |
| `adaptive` | Dynamic switching | `--topology adaptive` |

## 13 | Agent types (verbatim AGENTS.md)

**Core:** coordinator / coder / tester / reviewer / architect / researcher
**Specialized:** security-architect / security-auditor / memory-specialist / performance-engineer
**Swarm Coordination:** hierarchical-coordinator / mesh-coordinator / adaptive-coordinator
**Consensus:** byzantine-coordinator / raft-manager / gossip-coordinator

**README-claimed 16 roles** but listed above = 16 total matches the "16 specialized agent roles" headline. Additional "custom types" referenced but not enumerated.

## 14 | CLAUDE.local.md (development configuration — 1.8 KB)

- **Environment variables:** `CLAUDE_FLOW_CONFIG`, `CLAUDE_FLOW_LOG_LEVEL`, `CLAUDE_FLOW_MEMORY_BACKEND=hybrid`, `CLAUDE_FLOW_MEMORY_PATH=./data/memory`, `CLAUDE_FLOW_MCP_PORT=3000`, `CLAUDE_FLOW_MCP_TRANSPORT=stdio`
- **Plugin Registry Maintenance (IPFS/Pinata):** registry CID in `v3/@claude-flow/cli/src/plugins/store/discovery.ts`; gateway `https://gateway.pinata.cloud/ipfs/{CID}`; 4-step add-plugin protocol documented
- **Doctor Health Checks:** `npx claude-flow@v3alpha doctor` checks Node 20+, npm 9+, git, config, daemon, memory DB, API keys, MCP servers, disk space, TypeScript
- **Intelligence System (RuVector):** 4-step pipeline RETRIEVE (HNSW) → JUDGE (verdicts) → DISTILL (LoRA) → CONSOLIDATE (EWC++); components SONA (<0.05ms), MoE (8 experts), HNSW (150×-12,500×), Flash Attention (2.49×-7.47×)

## 15 | Key corpus-first observations (Cluster 2)

1. **Dual-runtime explicit governance** — CLAUDE.md + AGENTS.md both substantial (38.9 + 20.7 KB); BOTH describe the same system from different runtime vantage points. Pattern #22 AGENTS.md at T2 is corpus-first.
2. **"1 message = ALL operations" batching mandate** — mandatory batching patterns documented explicitly at T2; stronger than v41 browser-use or v36 pi-mono
3. **Division-of-labor framing** (claude-flow = ledger / Codex = executor) — first corpus T2 positioning as explicitly coordination-only (not execution)
4. **`$skill-name` Codex + `/skill-name` Claude dual naming convention** — first corpus divergent-syntax-per-runtime for skills
5. **Pre-built collaboration templates** (feature / security / refactor / bugfix) — first corpus explicit template catalog for multi-runtime pipelines
6. **security@cognitum.one + security@ruv.io 2-domain** — first corpus 2-domain commercial security contact structure
7. **IPFS/Pinata plugin registry protocol in CLAUDE.local.md** — 4-step add-plugin documented; first corpus decentralized-plugin-registry governance
8. **ADR-driven governance with `hooks progress` validation gate** — mid-scale corpus ADR practice (smaller than OpenHands' but broader)
9. **DDD 5-bounded-context enforcement** (Core / Memory / Security / Integration / Coordination) — first corpus explicit DDD-at-T2-enterprise
10. **SPARC methodology branding** (methodology lineage originator RuvNet claims v1.0.50 introduction March 2025) — distinct from Kent Beck TDD / Jesse Vincent test-discipline / Luong Shayan-style content-frameworks
