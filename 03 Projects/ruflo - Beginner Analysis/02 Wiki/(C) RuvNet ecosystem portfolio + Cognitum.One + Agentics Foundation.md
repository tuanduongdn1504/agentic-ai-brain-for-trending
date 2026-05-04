# (C) Entity 2 — RuvNet ecosystem portfolio + Cognitum.One + Agentics Foundation

## 1 | RuvNet (Reuven Cohen) — author profile

| Signal | Value |
|--------|-------|
| **Full name** | Reuven Cohen |
| **GitHub** | `ruvnet` |
| **Email** | `ruv@ruv.io` |
| **Twitter/X** | `@ruv` |
| **LinkedIn** | `reuvencohen` |
| **YouTube** | `@ReuvenCohen` |
| **Personal AI platform** | `ruv.io` |
| **Commercial parent (inferred)** | `Cognitum.One` (security@cognitum.one primary) |
| **Community** | Agentics Foundation (founder) Discord + foundation reference |
| **Industry background** | Senior tech operator (ex-Enomaly founder, early cloud-computing pioneer, past Cloud Foundry CTO) |

## 2 | Product portfolio (Pattern #17 variant 1 — strongest evidence to date)

**Ruflo core family (3-tier package naming):**
- `claude-flow` — primary npm package (preserved through rebrand)
- `ruflo` — new brand name package (parallel distribution since v3.1.0-alpha.43)
- `@claude-flow/cli` — scoped package

**Internal v3 monorepo sub-packages (6):**
- `@claude-flow/cli` (26 commands)
- `@claude-flow/codex` (Dual-mode Claude + Codex collaboration) — **separately published npm**
- `@claude-flow/guidance` (Governance control plane)
- `@claude-flow/hooks` (17 hooks + 12 workers)
- `@claude-flow/memory` (AgentDB + HNSW)
- `@claude-flow/security` (Input validation + CVE remediation)

**@ruvector/* sibling family (publicly-distributed):**
- `@ruvector/attention ^0.1.3` — Flash Attention kernels
- `@ruvector/core ^0.1.30` — RuVector runtime
- `@ruvector/router ^0.1.30` — SemanticRouter
- `@ruvector/router-linux-x64-gnu ^0.1.30` — Platform-specific binary
- `@ruvector/sona ^0.1.5` — SONA pattern learning

**RuvNet-related foundation packages (integration points):**
- `agentdb ^3.0.0-alpha.9` — Embedded graph + vector DB
- `agentic-flow ^2.0.7` — Coordination engine foundation (ADR-001, ADR-056)

**Plugin marketplace (IPFS/Pinata):**
- 8 official plugins
- 10 RuVector WASM plugins (50 MCP tools)
- `@claude-flow/teammate-plugin` (Agent Teams coordination)
- `@claude-flow/plugin-gastown-bridge ^0.1.3` — Gas Town Bridge WASM-accelerated orchestrator

**Platforms / services:**
- **Flow Nexus** — cloud tier SaaS (commercial), referenced via `$flow-nexus-*` skills
- **ruv.io AI Platform** — RuvNet's flagship landing / platform
- **Cognitum.One** — commercial parent (inferred from security contact)
- **Agentics Foundation** — community / standard-setter (Discord + README badge)

**Total ecosystem count: 15+ distinct packages/platforms** under a single solo-flagship author. **Strongest Pattern #17 variant 1 evidence in corpus** (prior strongest: Luong claude-howto v32 15+ companion repos; Fiegel awesome-mcp-servers v31 with 7 repos + Glama commercial).

## 3 | Cognitum.One — commercial parent entity

**Evidence:**
- `security@cognitum.one` — primary vulnerability reporting email (SECURITY.md)
- WebFetch `https://cognitum.one` returned 403 (gated or access-restricted), BUT domain exists and is separately resolvable from `ruv.io`
- Listed as homepage in GitHub repo metadata

**Inferred role:** Commercial parent entity for Ruflo OSS + Flow Nexus SaaS. May also hold trademark for "Ruflo" brand.

**Not yet verified:** legal structure (LLC / Inc), funding status (bootstrap / VC / angel), team size (solo Reuven Cohen / incorporated team), customer base (pre-launch / paying customers).

## 4 | Flow Nexus — cloud tier (open-core commercial layer)

**Evidence:**
- README Competitor Comparison: "✅ Flow Nexus" as "Cloud Platform" (contrast CrewAI/LangGraph/AutoGen/Manus "⛔")
- Skills catalog: `$flow-nexus-neural`, `$flow-nexus-swarm`, `$flow-nexus:workflow`
- CHANGELOG references Flow Nexus indirectly via alpha-phase feature integration

**Commercial boundary hypothesis:** OSS Ruflo provides swarm + RuVector + AgentDB + MCP tools + 100+ agents + plugins. Flow Nexus adds managed cloud hosting + enterprise features (team collaboration, SLA, compliance, SSO, audit log, managed scale) — but README does NOT provide pricing or feature-matrix for Flow Nexus. **Pre-launch or reference-only status possible.**

**Pattern #31 Open-Core N=6 strengthening evidence:** (fish-speech + Skyvern + OpenHands + crawl4ai + browser-use + ruflo = 6 distinct commercial-tier-on-OSS instances).

## 5 | Agentics Foundation — community/standard

**Evidence:**
- README badge: `Agentics Foundation` linking to `https://discord.com/invite/dfxmpwkG2D`
- AGENTS.md header: "For OpenAI Codex CLI - **Agentic AI Foundation standard**"
- Reuven Cohen's public association with the foundation (X/Twitter timeline + Agentics.org reference)
- `agentics.org` referenced as foundation web

**Role:** Appears to be a standard-setting community/foundation with RuvNet as founder. Publishes "Agentic AI Foundation standard" (e.g., AGENTS.md convention for Codex CLI). Discord-first community hub.

**Not yet verified:** legal structure (501(c), unincorporated community, trademark-only), governance model (benevolent dictatorship / elected board / open membership), membership tiers (free Discord / paid membership).

**Pattern #50 Commercial-Funnel Companion observation:** Agentics Foundation acts as community-funnel (free Discord → awareness → ruflo OSS adoption → Flow Nexus commercial). 3-tier commercial structure is corpus-unique.

## 6 | ruv.io AI Platform — personal brand / AI platform

**Evidence:**
- `ruv@ruv.io` author email
- `security@ruv.io` policy questions
- `https://ruv.io` homepage referenced in package.json
- README badge: "ruv.io — AI Platform"

**Inferred role:** Reuven Cohen's personal AI platform / portfolio brand, likely consolidating his multiple AI-industry projects under single identity. Distinct from Cognitum.One (commercial entity) but overlapping/related.

**Corpus observation:** First corpus author with **3-layer identity stack** (personal brand `ruv.io` + commercial `Cognitum.One` + community `Agentics Foundation`). Compare:
- Luong claude-howto v32: `luongnv.com` personal + Medium + GitHub (2-layer)
- Fiegel awesome-mcp-servers v31: personal + Glama commercial (2-layer)
- **RuvNet: 3-layer with explicit separation of roles**

## 7 | Intellectual lineage (Pattern #19 archetype 4 — no-lineage)

**What's NOT cited:**
- Karpathy /raw folder or LLM wiki pattern
- John Lam SDD lineage
- BMAD methodology
- Any academic research paper
- Any peer-reviewed framework
- Any individual-author inspiration (contrast spec-kit v17 John Lam, awesome-design-md v25 Google Stitch, graphify v16 Karpathy)

**What IS claimed:**
- **SPARC methodology** — originated by RuvNet at v1.0.50 (March 2025); not cited to external source
- **Agentics Foundation standard** — RuvNet is founder
- **Agentic-flow** — RuvNet-maintained foundation package

**Pattern #19 archetype 4 at T2 (first):** Ruflo joins archetype-4 no-explicit-lineage family (Pakistani Shayan claude-code-best-practice v34, Jarrod Watts claude-hud v35, Mario Zechner pi-mono v36 — all T1 archetype-4). **First archetype-4 at T2**.

**Self-originated methodology positioning:** RuvNet claims SPARC origination rather than citing upstream. Parallel to BMAD v11 (Brian commercial-entity original methodology) but distinct — SPARC predates rebrand-to-Ruflo by ~2 years and is carried as methodology-brand through v3.5.

## 8 | Publishing cadence (16-month velocity)

| Milestone | Version | Date | Commits | Gap |
|-----------|---------|------|---------|-----|
| Initial release | v1.0.1 | 2025-01-01 | 0 | 0 |
| SPARC integration | v1.0.50 | 2025-03 | ~100 | 3 months |
| v1 stable (71 patches) | v1.0.71 | 2025-04 | ~300 | 1 month |
| v2 alpha foundation | v2.0.0-alpha.33 | 2025-05 | ~500 | 1 month |
| agentic-flow integration | v2.7.0 | 2025-08 | ~2000 | 3 months |
| v3 alpha foundation | v3.0.0-alpha.1 | 2025-10 | ~3000 | 2 months |
| v3.0 plugins + IPFS | v3.0.0-alpha.170 | 2025-12 | ~4000 | 2 months |
| v3.0 guidance + WASM | v3.0.0-alpha.100 | 2026-01 | ~4500 | 1 month |
| v3.1 AgentDB v3 | v3.1.0-alpha.55 | 2026-02 | ~5500 | 1 month |
| **v3.5 stable rebrand** | **v3.5.0** | **2026-02-27** | **~5800** | 1 month |
| v3.5 patches to current | v3.5.80 | 2026-04-11 | 6,067 | 1.5 months |

**Average: ~380 commits/month (sustained 16 months).** 55 alpha iterations before v3.5 stable. Corpus-first **rapid 16-month v1→v3.5 major-version progression**.

## 9 | Cross-wiki ecosystem-layer comparison

| Solo ecosystem-layer individual | Ecosystem size | Primary product | Sibling products | Commercial |
|--------------------------------|----------------|-----------------|------------------|------------|
| **RuvNet v42** | **15+** | **ruflo (flagship)** | **@claude-flow/* (6) + @ruvector/* (4) + agentdb + agentic-flow + plugins** | **Cognitum.One + Flow Nexus** |
| Luong v32 | 15+ | claude-howto | asm + skills + asm-registry + context-stats + ccl + sleek-ui + unsloth-mlx + vibe-coding + ~100 | Not explicit |
| Fiegel v31 | 7 | awesome-mcp-servers | awesome-mcp-clients + awesome-mcp-devtools + fastmcp + mcp-proxy + mcp-ping + pipenet | Glama (glama.ai/mcp/servers) |
| Yeachan v27 | 2 | oh-my-claudecode | oh-my-codex | Not explicit |
| Mario v36 | 7 | pi-mono | pi-ai + pi-agent-core + pi-tui + pi-web-ui + pi-mom + pi-pods | Not explicit (libGDX legacy) |

**RuvNet stands out on:**
- **Most explicit 3-layer commercial structure** (Cognitum.One + Flow Nexus + Agentics Foundation)
- **Deepest ecosystem-foundation split** (agentic-flow as foundation + AgentDB as DB + ruflo as flagship)
- **Most alpha iterations** (55 pre-stable)
- **Fastest major-version cadence** (v1 → v3.5 in 16 months)

## 10 | Cross-references

- Entity 1: `(C) Ruflo core product — CLI + MCP + swarm + memory (EXTREME-compressed).md`
- Entity 3: `(C) T1 vs T2 tier decision + Pattern 18 MCP-scale outlier + EXTREME primitive-count precedent.md`
- Entity 4: `(C) Storm Bear meta — 31st consecutive + EXTREME-tier compression lesson.md`
- Sibling wiki: Luong v32 claude-howto / Fiegel v31 awesome-mcp-servers / Yeachan v27 oh-my-claudecode / Mario v36 pi-mono / Shayan v34 claude-code-best-practice / Jarrod v35 claude-hud

## 11 | Observations summary

- **Pattern #17 variant 1 strongest evidence to date** (15+ ecosystem packages under single solo flagship)
- **Pattern #31 Open-Core N=6 strengthening** (Cognitum.One + Flow Nexus)
- **Pattern #50 Commercial-Funnel 5th data point** (3-layer Cognitum.One + Flow Nexus + Agentics Foundation)
- **Pattern #19 archetype 4 no-lineage at T2 first** (senior-industry-operator with self-originated SPARC methodology)
- **Pattern #20 Solo-Scale Ceiling dictionary new row** (T2 solo-flagship + commercial + foundation at 33K/16mo)
- **Corpus-first 3-layer identity stack** (personal brand + commercial entity + community foundation)
- **Corpus-first explicit "methodology origination + rebrand" trajectory** (SPARC stays branded through Claude Flow → Ruflo)
