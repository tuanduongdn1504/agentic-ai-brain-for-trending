# (C) Entity 3 — T1 vs T2 tier decision + Pattern #18 MCP-scale outlier + EXTREME primitive-count precedent

## 1 | Tier decision — T2 primary + T1 secondary (dual classification)

**Primary classification: T2 Agent-as-service.**

Rationale:
- **Daemon + MCP server architecture:** Ruflo runs as stateful daemon (`npx claude-flow daemon start/stop/status`) with MCP server on port 3000 (stdio transport)
- **Enterprise governance surface:** 70+ ADRs + 5 DDD bounded contexts + SECURITY.md + `hooks progress` validation gates
- **Cloud tier commercial layer:** Flow Nexus (referenced throughout README + skills) — open-core commercial model
- **Commercial parent entity:** Cognitum.One (security@cognitum.one domain)
- **Multi-tenant architecture signals:** 3-scope agent memory (project / local / user) + cross-agent transfer + IPFS/Pinata plugin registry (decentralized distribution) + background workers (12)
- **PostgreSQL RuVector:** Enterprise-grade vector DB with 77+ SQL functions (T2 infrastructure signal)
- **6 provider adapters with cost-based routing + failover:** Multi-LLM service layer

**Secondary classification: T1 Agent-as-assistant.**

Rationale:
- **MCP integration INTO Claude Code:** "Plugs Into Claude Code" headline
- **Uses Claude Code's Task tool + TodoWrite:** architected around Claude Code workflow
- **Dual-mode Claude+Codex:** both T1 runtimes as peers
- **`init` workflow:** creates CLAUDE.md + `.claude/` dir in user project (T1 assistant-configuration pattern)
- **Claude Code IS required prerequisite:** "IMPORTANT: Claude Code must be installed first"

**Reconciliation:** Ruflo is **both**. It's a T2 service that EXTENDS T1 assistants. This is the **Pattern #9 Resolution D multi-axial bifurcation** at its clearest: ruflo occupies simultaneously the T2 service-platform quadrant AND the T1 assistant-extension quadrant.

**Tier count impact:**
- **T2 extends N=2 → N=3** (goclaw v4 + multica v15 + ruflo v42)
- T1 gets 14th entrant (secondary)
- **Corpus tier distribution post-v42:** T1 N=13 + T2 N=3 + T3 N=2 + T4 N=7 + T5 N=7 + outside-scope N=7

**Structural observation:** T2 still smallest multi-entrant tier. Each T2 has distinct archetype:
- **goclaw v4** — Multi-tenant Go-backend platform with Karpathy Knowledge Vault
- **multica v15** — Community-platform Linear-analog TypeScript+Go
- **ruflo v42** — Solo-flagship-multi-sibling-ecosystem with RuVector intelligence + commercial layer

## 2 | Pattern #18 MCP Agent Runtime Standardization — scale outlier analysis

**Ruflo: 313 MCP tools.** This is the largest per-project MCP tool count in Storm Bear corpus by ~20×.

**Corpus MCP-tool-count distribution (post-v42):**

| Tier | Wiki | MCP tool count | Purpose |
|------|------|----------------|---------|
| **Basic consumer (1-5 tools)** | Most wikis | 1-5 | MCP used for specific integration (e.g., playwright + context7 + deepwiki in claude-code-best-practice v34) |
| **MCP-heavy (6-15 tools)** | GitNexus v33 | 16 | Code-indexing per-repo + cross-repo-group primitives |
| **MCP-heavy** | browser-use v41 | ~10+ | browser automation + session management |
| **MCP-heavy** | OMC v27 | (via runtimes) | 4-runtime orchestration |
| **MCP-PLATFORM-SCALE (100+ tools) — NEW TIER** | **ruflo v42** | **313** | **Entire agent-orchestration-platform exposed as MCP surface** |

**Proposed Pattern #18 formal-statement-update at next mini-audit:**

Current Pattern #18 statement (paraphrased): "Agent frameworks at T1/T2/T5 community-platform archetype adopt MCP as de facto runtime standard for Claude Code interop; 70-75% adoption baseline with deliberate-rejection minority."

**Proposed v42-post refinement:**
> "MCP adoption exhibits **3-tier count distribution** within adopting frameworks:
> - **Tier 1 (basic consumer):** 1-5 tools for specific integrations
> - **Tier 2 (MCP-heavy):** 6-99 tools for domain-specific exposure
> - **Tier 3 (MCP-platform-scale):** 100+ tools where entire agent-platform IS the MCP surface (ruflo v42 313 = corpus-first; established 100+ threshold)"

**This formal-statement-update is strengthening-not-new-candidate** — fits within existing Pattern #18 formulation.

**Cross-wiki evidence:**
- T1: MCP-basic consumers (most T1 wikis)
- T4: GitNexus v33 = 16 tools (MCP-heavy at T4 bridge)
- T2: ruflo v42 = 313 tools (MCP-platform-scale at T2)
- T5: browser-use v41 = MCP-heavy at T5 application

**Pattern #18 projection:** As agent-orchestration matures, Tier 3 MCP-platform-scale may become common for T2 platforms. Watch for N=2 Tier 3 in future wikis.

## 3 | EXTREME primitive-count precedent — corpus methodology contribution

**Prior corpus primitive-count tiers (per Phase 0.9 informal discipline established at v35):**

| Tier | Prior data point | Primitive count | Velocity |
|------|------------------|-----------------|----------|
| **GREEN** | claude-hud v35 | ~70 | ~2h (baseline) |
| **YELLOW** | pi-mono v36 | ~150-200 | ~2h 40min |
| **RED** | browser-use v41 | ~200+ | ~3h 15min |
| **EXTREME (NEW v42)** | **ruflo v42** | **~500+** | **~3h 45min+ expected** |

**Precedent established:** EXTREME tier (>300 primitives) requires:
1. **Aggressive citation-not-replication** — 313 MCP tools NOT enumerated; reference `npx claude-flow mcp list`
2. **Primitive family grouping** in entity 1 (MCP / agents / skills / commands / hooks / workers / RL algos / consensus / topologies / controllers / providers / ADRs / contexts / plugins / templates = 15 families, one-sentence each)
3. **Follow-up deep-dive flags** (5 recommended for ruflo: MCP catalog / RuVector stack / swarm + consensus / ADR catalog / agentic-flow + AgentDB architecture)
4. **Velocity overhead +50-100%** vs GREEN baseline (GREEN ~2h, EXTREME ~3h 45min = 2× overhead acceptable for once-per-many-wikis EXTREME)

**Methodology reform input for routine v2.2:**
- Formalize 4-tier primitive-count taxonomy (GREEN / YELLOW / RED / EXTREME)
- EXTREME tier should trigger primitive-family-grouping + follow-up-deep-dive-flag + velocity-tolerance protocols explicitly
- 4-entity format remains valid at EXTREME (vs variable-entity-count proposal) — confirmed by ruflo execution

## 4 | Cross-tier archetype positioning

**T2 archetype N=3 post-v42:**

| T2 entrant | Archetype | Scale | Commercial | Novel primitive |
|------------|-----------|-------|-----------|------------------|
| goclaw v4 | Multi-tenant corporate-ish | Medium | Implicit | Karpathy Knowledge Vault as infrastructure |
| multica v15 | Community-platform Linear-analog | 16.2K | Not explicit | Skills-lock.json + Anthropic skills registry import |
| **ruflo v42** | **Solo-flagship-multi-sibling-ecosystem + commercial-layer** | **33K** | **Cognitum.One + Flow Nexus (explicit)** | **RuVector 9-component intelligence + 313 MCP tools + IPFS plugin registry** |

**Archetype diversity at T2 N=3:** 100% unique (3 archetypes, 3 entrants). Parallel to T4 at N=3 (v16 graphify) and T5 at N=3 (v14 paperclip). **T2 validates via archetype-diversity hypothesis**.

**Pattern #9 Resolution D at T2 validates:** All 3 T2 entrants occupy distinct quadrants on corporate-vs-solo × broad-vs-narrow axes:
- goclaw: corporate-ish × broad-platform
- multica: community × broad-platform
- ruflo: solo × broad-platform-with-commercial-layer

## 5 | T1 + T2 crossover implications

Ruflo is the **corpus-first T1/T2 dual-classification framework**. Prior corpus examples of tier-adjacency without crossover:
- **Graphify v16 T4** stays T4 (bridge) despite 15-platform install surface
- **Multica v15 T2** stays T2 (service) despite Claude Code integration
- **OMC v27 T1** stays T1 despite orchestrating 4 runtimes

**Why ruflo is genuinely dual:**
- Runs as daemon/service (T2 signal) AND extends Claude Code specifically (T1 signal)
- Primary installation creates daemon + extends Claude Code CLAUDE.md + registers MCP server
- Both patterns are FIRST-CLASS (not "also supports") in README + CLAUDE.md

**Framework suggestion (not a pattern):** Future similar "agent-orchestration platforms that extend specific T1 assistants" may warrant dual-classification. Watch for N=2 at future wikis.

## 6 | Cross-references

- Entity 1: `(C) Ruflo core product — CLI + MCP + swarm + memory (EXTREME-compressed).md`
- Entity 2: `(C) RuvNet ecosystem portfolio + Cognitum.One + Agentics Foundation.md`
- Entity 4: `(C) Storm Bear meta — 31st consecutive + EXTREME-tier compression lesson.md`
- Siblings: goclaw v4 / multica v15 (T2 peers) / GitNexus v33 (MCP precedent) / browser-use v41 (RED primitive precedent)
