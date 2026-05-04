# (C) Cluster 3 — v3 monorepo architecture + RuvNet ecosystem portfolio + commercial positioning

> Sources: `package.json` (3.5 KB), `CHANGELOG.md` (9.0 KB, 235 lines), `v3/` folder structure, npm registry data (via WebFetch), README monorepo + ecosystem references.

## 1 | Package.json verbatim (main branch v3.5.80)

```json
{
  "name": "claude-flow",
  "version": "3.5.80",
  "description": "Ruflo - Enterprise AI agent orchestration for Claude Code. Deploy 60+ specialized agents in coordinated swarms with self-learning, fault-tolerant consensus, vector memory, and MCP integration",
  "bin": {
    "claude-flow": "./bin/cli.js"
  },
  "main": "dist/index.js",
  "author": "RuvNet (ruv@ruv.io, https://ruv.io)",
  "license": "MIT",
  "engines": { "node": ">=20.0.0" }
}
```

**Key observation:** Primary npm package name remains `claude-flow` despite brand rebrand to Ruflo. `ruflo` package exists separately at v3.5.65 (per CLAUDE.md). `@claude-flow/cli` also at v3.5.65. **Triple-package parallel distribution**.

## 2 | Production dependencies (post-v3.5 minimalism)

- `semver ^7.6.0`
- `zod ^3.22.4`

**Only 2 required production dependencies.** Everything else is optional.

## 3 | Optional dependencies (9 packages)

- `@claude-flow/codex ^3.0.0-alpha.8` — Dual-mode Claude + Codex collaboration (sibling internal monorepo)
- `@claude-flow/plugin-gastown-bridge ^0.1.3` — Plugin bridge (sibling internal)
- `@ruvector/attention ^0.1.3` — Flash Attention optimization kernels
- `@ruvector/core ^0.1.30` — RuVector core runtime
- `@ruvector/router ^0.1.30` — SemanticRouter
- `@ruvector/router-linux-x64-gnu ^0.1.30` — Platform-specific router
- `@ruvector/sona ^0.1.5` — SONA self-optimizing pattern learning
- `agentdb ^3.0.0-alpha.9` — Embedded graph + vector DB (parallel to GitNexus LadybugDB)
- `agentic-flow ^2.0.7` — Coordination engine foundation (ADR-001)

**RuvNet ecosystem structure inferred:**
- **ruflo (flagship):** `claude-flow` + `ruflo` + `@claude-flow/*` packages
- **@ruvector/* sibling family:** attention + core + router + sona
- **agentdb + agentic-flow:** other RuvNet-maintained OSS libs (implied from deep integration)

## 4 | Dev dependencies signal

- `@openai/codex ^0.98.0` — official OpenAI Codex SDK (dual-mode first-class partner)
- `vitest ^1.0.0` — ADR-008 Vitest chosen over Jest

## 5 | Scripts surface

12 npm scripts: `dev / build / build:ts / test / test:ui / test:security / lint / security:audit / security:fix / security:test / v3:domains / v3:swarm / v3:security`

**Security-first discipline:** 4 of 12 scripts are security-oriented (`security:audit/fix/test` + `test:security`).

## 6 | v3/ monorepo internal structure

Top-level v3 dirs:
- `v3/@claude-flow/cli/` — CLI entry point (26 commands)
- `v3/@claude-flow/codex/` — Dual-mode collab
- `v3/@claude-flow/guidance/` — Governance control plane
- `v3/@claude-flow/hooks/` — 17 hooks + 12 workers
- `v3/@claude-flow/memory/` — AgentDB + HNSW
- `v3/@claude-flow/security/` — Input validation + CVE remediation
- `v3/agents/` — 100+ agent templates
- `v3/aidefence/` — Threat detection module
- `v3/browser/` — Browser integration
- `v3/claims/` — Claims system (work ownership)
- `v3/deployment/` — Deployment automation
- `v3/embeddings/` — Embedding resolution (ReasoningBank WASM → @claude-flow/embeddings → mock)
- `v3/integration/` — Tokenization optimizer + agentic-flow bridge
- `v3/mcp/` — MCP server implementation
- `v3/neural/` — Neural training + learning
- `v3/performance/` — Benchmarks
- `v3/plugins/` — Plugin marketplace + IPFS registry
- `v3/providers/` — 6-provider adapters
- `v3/security/` — Security hardening
- `v3/shared/` — Shared utilities
- `v3/swarm/` — Swarm coordination
- `v3/testing/` — Test infrastructure

**21 top-level v3 dirs** — architectural breadth signal.

## 7 | ruflo/ brand directory structure

```
ruflo/
├── assets/           # ruflo-small.jpeg banner + branding assets
├── bin/              # Binary entry points
├── docs/             # Documentation
├── src/              # Source code
├── docker-compose.yml # Docker orchestration
├── package.json      # Separate package manifest
├── rvf.manifest.json # "RVF" (RuVector format?) manifest
└── README.md         # Ruflo-branded README
```

**Separate `rvf.manifest.json`** — novel file format, corpus-first. Likely RuVector format manifest for plugin/intelligence resource declaration.

## 8 | CHANGELOG milestone timeline (235 lines)

| Milestone | Version | Date | Key Feature |
|-----------|---------|------|-------------|
| Initial Release | v1.0.1 | 2025-01 | AI agent orchestration system |
| SPARC Integration | v1.0.50 | 2025-03 | Swarm + SPARC methodology |
| Alpha Foundation | v2.0.0-alpha.33 | 2025-05 | V2 alpha with hook safety |
| agentic-flow | v2.7.0 | 2025-08 | Coordination engine integration |
| V3 Foundation | v3.0.0-alpha.1 | 2025-10 | V3 monorepo, 215 MCP tools |
| Plugin Marketplace | v3.0.0-alpha.170 | 2025-12 | 8 plugins + IPFS registry |
| Guidance Control Plane | v3.0.0-alpha.100 | 2026-01 | WASM policy kernel, ContinueGate |
| AgentDB v3 | v3.1.0-alpha.55 | 2026-02 | 8 controllers, MutationGuard |
| **Ruflo v3.5** | **v3.5.0** | **2026-02-27** | **First stable release, rebranding** |

**Development timeline:** 16 months from initial release (2025-01-01) to current v3.5.80 (2026-04-11). **55 alpha iterations** before stable.

## 9 | MCP tool growth trajectory

- v3.0.0-alpha.1 (2025-10): **215 MCP tools**
- v3.5 (2026-02-27): **215 MCP tools** (unchanged at stable release headline)
- README current (v3.5.80): **"313 tools"** / CLAUDE.md: **"314 tools"**
- **Growth: +~100 MCP tools in 2 months of post-stable development**

## 10 | Rebrand protocol (CHANGELOG-documented)

- v3.1.0-alpha.43 (2026-02-15): "Ruflo Branding Fix: show 'ruflo' instead of 'claude-flow' when run via `npx ruflo`"
- v3.5.0 (2026-02-27): "Rebranding: Claude Flow → Ruflo across all packages"
- **Triple-package preserved** rather than replaced — maintains backward compatibility

## 11 | Commercial positioning (Cognitum.One + ruv.io + Agentics Foundation + Flow Nexus)

**Layered commercial structure inferred:**

| Layer | Entity | Purpose | Evidence |
|-------|--------|---------|----------|
| Parent commercial entity | **Cognitum.One** | Commercial operator | `security@cognitum.one` SECURITY.md primary contact + README homepage badge |
| AI Platform brand | **ruv.io** | RuvNet personal brand + AI platform | `ruv@ruv.io` author email + `security@ruv.io` secondary + `https://ruv.io` homepage in package.json |
| Community | **Agentics Foundation** | OSS community + Discord | `https://discord.com/invite/dfxmpwkG2D` badge + Agentics Foundation referenced in README + AGENTS.md ("Agentic AI Foundation standard") |
| Cloud tier | **Flow Nexus** | Commercial SaaS platform | Referenced throughout README + skills (`$flow-nexus-neural`, `$flow-nexus-swarm`, `$flow-nexus:workflow`) |

**Open-core verification:**
- OSS core: MIT license, full ruflo v3.5 feature set including swarm, RuVector, AgentDB
- Commercial tier: Flow Nexus referenced but NOT self-describable from OSS README alone
- Pattern #31 Open-Core **N=6 strengthening confirmed** (Cognitum.One as commercial entity + Flow Nexus as cloud tier funnel)

## 12 | RuvNet author profile (Reuven Cohen)

- **Email:** ruv@ruv.io
- **Twitter/X:** @ruv (https://x.com/ruv)
- **LinkedIn:** reuvencohen (https://www.linkedin.com/in/reuvencohen/)
- **YouTube:** @ReuvenCohen (https://www.youtube.com/@ReuvenCohen)
- **GitHub:** ruvnet
- **AI platform:** https://ruv.io
- **Commercial entity:** Cognitum.One (inferred)
- **Community:** Agentics Foundation (founder/active)

**Reuven Cohen** has public AI industry presence (LinkedIn Chief Technology Officer of Cloud Foundry / ex-Enomaly founder, cloud-computing pioneer). This is a **senior industry operator** doing solo-flagship with corporate-grade governance — analogous to but distinct from **solo-enterprise-scale** Pattern #20 cluster (graphify safishamsi / agency-agents msitarzewski / crawl4ai unclecode).

## 13 | Intellectual lineage observations

**Claimed influences (from README + CHANGELOG):**
- **SPARC methodology** — RuvNet claims origination ("SPARC Integration" at v1.0.50, March 2025). Not cited to external source.
- **Agentics Foundation** — framework standard ("Agentic AI Foundation standard" in AGENTS.md). RuvNet is founder.
- **agentic-flow** — coordination engine (ADR-001, ADR-056); own/related RuvNet project.

**Not cited:**
- ❌ Karpathy LLM wiki / /raw pattern
- ❌ John Lam / SDD lineage (contrast spec-kit v17)
- ❌ BMAD methodology (contrast BMAD v11)
- ❌ Any research paper
- ❌ Any peer-reviewed framework

**Pattern #19 archetype 4 (no-lineage) at T2** — T2 extends from N=0 (goclaw had no lineage either; multica implicit community-platform).

## 14 | Agentic-flow foundation (ADR-001)

- Cited as "foundation that eliminates 10,000+ duplicate lines"
- External dependency: `agentic-flow ^2.0.7` (sibling RuvNet project)
- ADR-056: "agentic-flow v3 Integration Architecture"
- **Potential observation:** agentic-flow may be RuvNet's attempt at generalizing multi-runtime orchestration beyond Claude Code

## 15 | Corpus-first observations (Cluster 3)

1. **Triple-package parallel distribution** (`claude-flow` + `ruflo` + `@claude-flow/cli`) all at same v3.5.65/80 version — first corpus pattern
2. **55 alpha iterations before stable** — corpus-most alpha-count (v3.0.0-alpha.1 → v3.0.0-alpha.184 → v3.1.0-alpha.x → v3.5.0 stable)
3. **Only 2 required production dependencies** (`semver` + `zod`) with 9 optional — unusual minimalism at enterprise-scale T2
4. **8+ package RuvNet ecosystem** (flagship + sibling ecosystem) — strongest Pattern #17 variant 1 evidence to date
5. **rvf.manifest.json** novel file format — corpus-first agent-framework-manifest format
6. **3-tier commercial structure** (Cognitum.One / ruv.io / Agentics Foundation) — corpus-most-elaborate commercial positioning
7. **16-month rapid-evolution timeline** v1 → v3.5 with 4 major product phases (SPARC → Hive-Mind → RuVector → Rebrand) — corpus-fastest major-version progression
8. **MCP tool count tracked manually** (315 vs 314 vs 313 discrepancies across CLAUDE.md + README + CHANGELOG) — manual-maintenance signal
9. **Senior-industry-operator solo-flagship** (Reuven Cohen ex-Enomaly + Cloud Foundry) — corpus-first solo-at-T2 with established-industry-founder background
10. **Agentic-flow as foundation dependency** — ADR-001 + separate RuvNet project; suggests 2-tier internal architecture (ruflo is ruflo-specific layer on top of agentic-flow general-purpose)

## 16 | Absences (Cluster 3)

- **No ISSUES_TEMPLATE.md or dedicated CONTRIBUTING.md** — governance heavy in CLAUDE.md + AGENTS.md but missing GitHub issue-template surface
- **No formal community contribution graph** (410+ open issues suggest heavy-maintenance-burden signal)
- **No stated maintainer policy** — bus factor appears 1 (RuvNet solo)
- **No CODE_OF_CONDUCT.md** (contrast Microsoft claude-howto v32 + Anthropic claude-hud v35)
- **No disclosed funding** (no VC, angel, grant, or crowdfunding references) — contrast OpenHands v30 All Hands AI $18.8M disclosed
- **No formal multi-institutional partnership** (contrast LlamaFactory v22 Lab4AI or OpenHands v30 UIUC+CMU)
