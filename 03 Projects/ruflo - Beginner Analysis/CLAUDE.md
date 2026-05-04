# Ruflo - Beginner Analysis

> **Project type:** LLM Wiki (v2.1 routine, 42nd wiki in Storm Bear corpus)
> **Source:** `ruvnet/ruflo` (https://github.com/ruvnet/ruflo) — branch `main`, v3.5.80 (2026-04-11)
> **Scope:** 42nd wiki, 6th v2.1-era execution, T2-leaning-T1 tier decision, EXTREME primitive-count precedent (corpus-first)
> **Status:** v1 in progress (2026-04-24)

---

## Source signature (Phase 0 probe)

| Axis | Value |
|------|-------|
| Name | Ruflo (formerly Claude Flow) |
| Tagline (verbatim) | "The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems." |
| Sub-tagline | "Multi-agent AI orchestration for Claude Code. Deploy 16 specialized agent roles + custom types in coordinated swarms with self-learning capabilities, fault-tolerant consensus, and enterprise-grade security." |
| Stars / Forks / Watchers | 33,000 / 3,700 / 291 |
| Open Issues | 411 |
| Commits | 6,067 |
| Latest release | v3.5.80 (2026-04-11) |
| License | MIT |
| Primary language | TypeScript (64.8%) |
| Default branch | main |
| Homepage | Cognitum.One |
| Author / Org | RuvNet (Reuven Cohen) — solo-flagship, Toronto-area |
| Created | 2025-01-01 (v1.0.1) |
| Topics | Multi-agent systems / swarm intelligence / autonomous agents / Claude API integration / MCP / agentic AI frameworks / RAG systems |
| Dependencies ecosystem | `@claude-flow/codex` / `@claude-flow/plugin-gastown-bridge` / `@ruvector/*` (attention/core/router/sona) / `agentdb` / `agentic-flow` — RuvNet multi-product ecosystem |
| Governance files | 6 (README 280KB / CLAUDE.md 38.9KB / CLAUDE.local.md / AGENTS.md 20.7KB / SECURITY.md / CHANGELOG.md) |
| MCP tools | **313** (corpus-most by >19× — prior max GitNexus v33 = 16) |
| Agents | **100+ claimed** (60+ in v3.0.0-alpha.1 release notes; 16 roles + custom types in v3.5 README headline) |
| Skills | 137+ (Codex path) / 42+ (Claude path) |
| CLI commands | 26 + 140+ subcommands |
| Hooks | 17 |
| Workers | 12 |
| RL algorithms | 9 (Q-Learning, SARSA, A2C, PPO, DQN, Decision Transformer, etc.) |
| Consensus protocols | 5 (Byzantine, Raft, Gossip, CRDT, Quorum) |
| AgentDB controllers | 19 (8 activated v3.1.0-alpha.55) |
| ADRs | 70+ |
| Topologies | 6 (hierarchical, mesh, ring, star, hierarchical-mesh, adaptive) |
| Providers | 6 (Anthropic, OpenAI, Google, Cohere, Ollama, + failover) |
| Plugin marketplace | IPFS/Pinata + 8 official plugins + 10 RuVector WASM plugins (50 MCP tools) |
| DDD bounded contexts | 5 (Core / Memory / Security / Integration / Coordination) |
| i18n | EN-only |

## 12-axis v2.1 classification

| Axis | Value |
|------|-------|
| **Tier** | **T2 Agent-as-service primary + T1 Agent-as-assistant secondary** — dual classification. Runs as MCP server/daemon (T2 enterprise orchestration platform with Cloud tier "Flow Nexus") but INTEGRATES WITH Claude Code as assistant-extension (T1 pattern). **Primary classification = T2** (enterprise service: daemon + Cloud platform + PostgreSQL + RuVector SaaS + security@cognitum.one commercial entity + 70+ ADRs enterprise governance surface). **Secondary = T1 via MCP integration**. T2 goes from N=2 → N=3 (multica v15 + goclaw v4 + ruflo v42). |
| **Archetype** | **NEW solo-flagship-with-multi-sibling-ecosystem-portfolio + commercial-entity (Cognitum.One) + academic-adjacent foundation (Agentics Foundation)** — distinct from prior T2 archetypes (multica community-platform + goclaw multi-tenant-platform). Pattern #17 variant 1 13th+ data point (strongest evidence to date: ruflo main + @claude-flow/codex + @claude-flow/plugin-gastown-bridge + @ruvector/attention/core/router/sona + agentdb + agentic-flow = 8+ package ecosystem). |
| **Scale tier** | Medium-large (33K in 16 months ≈ 2,060 stars/month sustained-community-viral) |
| **Primary lang** | TypeScript (64.8%) + Rust WASM kernels (policy engine / embeddings / proof system) + Python bindings possible |
| **Packaging** | npm `claude-flow@3.5.80` + npm `ruflo@latest` + npm `@claude-flow/cli@3.5.65` (triple-package parallel distribution) + curl install script (cdn.jsdelivr.net) + Claude Code MCP registration |
| **Origin story** | Individual-author-multi-phase (RuvNet SPARC methodology → v1 SPARC orchestrator → v2 hive-mind → v3 RuVector intelligence + WASM + open-core) |
| **Methodology** | SPARC + Anti-Drift swarm + Spec-Driven (70+ ADRs) + DDD (5 bounded contexts) + Self-learning loop (RETRIEVE → JUDGE → DISTILL → CONSOLIDATE → ROUTE) |
| **Governance** | Heavy (6 files including 38.9KB CLAUDE.md + 20.7KB AGENTS.md + 280KB README + 70+ ADRs + SECURITY.md + CHANGELOG.md + Behavioral Rules + File Organization + Anti-Drift + Dual-Mode protocols) |
| **Agent/skill count** | **EXTREME tier: ~500+ primitives** (313 MCP tools + 100+ agents + 137+ skills + 26 commands + 17 hooks + 12 workers + 9 RL algos + 5 consensus + 8+19 AgentDB controllers + 6 topologies + 6 providers + 70+ ADRs + 8 plugin marketplace + 10 RuVector WASM plugins/50 MCP tools) |
| **i18n** | EN-only (notable absence at T2 enterprise scale; contrast OMC v27 7-lang + claude-howto v32 4-lang) |
| **Intellectual influence** | No explicit AI-space individual-author lineage cited; implicit: SPARC methodology origin (v1.0.50 March 2025) + Agentics Foundation community lineage (Reuven Cohen founder) |
| **Agent platforms** | Claude Code (primary, native MCP) + OpenAI Codex CLI (dual-mode first-class via `@claude-flow/codex`) + potentially others via MCP |

## Phase 0.9 Primitive-count probe — **EXTREME (CORPUS-FIRST NEW TIER)**

**Probed primitive-count:** ~500+

**Signal breakdown:**
1. **README TOC top-level sections:** ~50 collapsed-details sections (system architecture / agents / swarm / memory / RuVector / security / deployment / etc.)
2. **Repo folder structure top-level:** 14 dirs (.agents, .claude, .claude-plugin, .github, .githooks, agents, bin, plugin, ruflo, scripts, tests, v2, v3, package monorepo)
3. **CLAUDE.md + AGENTS.md components:** 6 packages (@claude-flow/cli + codex + guidance + hooks + memory + security) + 313 MCP tools + 100+ agents + 17 hooks + 12 workers
4. **Documentation surface:** 70+ ADRs + docs/ subfolder (per ruflo/docs/ + v3/docs/ + main docs/)

**Fits 4-entity format cleanly?** **NO — EXTREME (worse than RED)**

Prior corpus baselines:
- **GREEN:** claude-hud v35 ~70 primitives
- **YELLOW:** pi-mono v36 ~150-200 primitives (3-4× GREEN)
- **RED:** browser-use v41 ~200+ primitives (4-5× GREEN)
- **EXTREME (NEW v42):** ruflo ~500+ primitives (7-10× GREEN, 2.5-5× RED)

**Scope-compression decisions applied (aggressive + EXTREME-tier):**

- **4-entity allocation forced lossy compression:**
  - Entity 1: **Core product = CLI/MCP + swarm + agents + memory** (unified; citation-not-replication for 313 MCP tools, 100+ agents, 17 hooks, 12 workers, 26 commands; reference upstream docs for full enumerations)
  - Entity 2: **RuvNet ecosystem portfolio + Cognitum.One commercial + Agentics Foundation** (Pattern #17 variant 1 strongest evidence + commercial positioning + founding lineage)
  - Entity 3: **Tier decision T1 vs T2 + EXTREME primitive-count precedent + Pattern #18 MCP-scale outlier analysis** (pattern-relevant entity, corpus-methodology focused)
  - Entity 4: **31st consecutive Storm Bear meta-entity** (v10-v42 streak preservation + Scrum-coach pilot strategy + vault-architectural implications)

- **Lossy compression accepted (explicit list):**
  - RuVector intelligence stack (SONA / EWC++ / Flash Attention / HNSW / ReasoningBank / Hyperbolic / LoRA / Int8 Quant / SemanticRouter / 9 RL) — summarized in Entity 1 sidebar, NOT enumerated
  - 70+ ADRs — reference-only (7 key ADRs named: 001, 006, 008, 009, 026, 048, 049, 056)
  - 5 consensus protocols — listed by name only, no per-protocol explanation
  - 19 AgentDB controllers — summary sentence; not enumerated
  - 6 topologies — table with 1-line each
  - 8 plugin marketplace + 10 RuVector WASM plugins — reference-only
  - v3 monorepo 6 sub-packages — listed with 1-line purpose each
  - Agentic-flow v3 + AgentDB v3 deep architecture details — sidebar only
  - v1/v2/v3 historical timeline — CHANGELOG citation only (not replicated)

- **Citation-not-replication (reference upstream):**
  - Full 313 MCP tool enumeration → cite `npx claude-flow mcp list` + README section
  - Full 100+ agent list → cite `npx claude-flow agent list` + agents/ folder
  - Full 70+ ADR list → cite docs/adr/ or ruflo/docs/
  - Full RuVector component details → cite @ruvector/core package docs

- **Follow-up deep-dive flags (recommended for future wikis if operator interested):**
  1. `ruflo - MCP tools catalog deep-dive` (313 tools + 6 category split)
  2. `ruflo - RuVector intelligence stack deep-dive` (SONA + EWC++ + HNSW + 9 RL)
  3. `ruflo - Swarm + hive-mind + consensus deep-dive` (6 topologies + 5 consensus + Queen types)
  4. `ruflo - ADR catalog deep-dive` (70+ ADRs governance surface)
  5. `ruflo - Agentic-flow + AgentDB architecture deep-dive` (sibling ecosystem packages)

**Velocity tolerance:** ~3h 45min+ expected (vs v41 RED ~3h 15min, vs baseline ~2h). EXTREME-tier precedent established for future ~500+ primitive wikis.

**Operator decision:** accept compression + proceed with 4-entity format. EXTREME-tier is INFORMAL PRECEDENT only; routine v2.2 (future) may formalize variable-entity-count handling. Document compression decisions in iteration log.

## v2.1 Phase 0.5 Pattern pre-check

### Expected outcome: 0 new active candidates (streak-continuation target = 6 consecutive)

**1. Pattern #58 Branding vs Package-Name Divergence (N=1 stale-risk from v27 oh-my-claudecode):**
- **v27 OMC:** repo `oh-my-claudecode` + npm `oh-my-claude-sisyphus@latest` (branding != package)
- **v42 ruflo:** repo `ruvnet/ruflo` + packages `claude-flow@3.5.80` + `ruflo@3.5.80` + `@claude-flow/cli@3.5.65` (brand = Ruflo; primary npm = `claude-flow`; rebrand preserves original package names as transitional)
- **Structural parallel:** both are brand-name-in-README differs from primary-npm-package-name
- **BUT:** v42 is genuinely more complex — it's TRIPLE-PACKAGE parallel distribution (`claude-flow` + `ruflo` + `@claude-flow/cli`) with explicit rename documented in CHANGELOG.md + `CHANGELOG.md` "v3.1.0-alpha.43 — Ruflo Branding Fix: show 'ruflo' instead of 'claude-flow' when run via `npx ruflo`"
- **Decision:** **UN-STALE + N=2 promotion-candidate** at next mini-audit under Criterion 2 structural-unambiguity
- Sub-variants: 58a rename-without-npm-rename (v27 OMC) + 58b partial-rename-with-transitional-original (v42 ruflo triple-package)

**2. Pattern #17 Ecosystem-Layer variant 1 solo-individual-ecosystem-portfolio:**
- RuvNet portfolio: ruflo main + @claude-flow/codex + @claude-flow/plugin-gastown-bridge + @claude-flow/cli + @ruvector/attention + @ruvector/core + @ruvector/router + @ruvector/sona + agentdb + agentic-flow + Cognitum.One commercial + Agentics Foundation community + ruv.io AI platform
- **8+ package ecosystem** = STRONGEST variant 1 evidence to date (prior strongest: Luong claude-howto v32 15+ companion repos)
- **Strengthening** — 13th data point; NOT registration

**3. Pattern #18 MCP Agent Runtime Standardization:**
- Ruflo has **313 MCP tools** — CORPUS-MOST BY ~20× (prior max GitNexus v33 at 16 MCP tools)
- **Major strengthening data point** — propose formal-statement-update documenting MCP-tool-count distribution tiers at next mini-audit:
  - Tier 1 (basic MCP consumer): 1-5 tools (most wikis)
  - Tier 2 (MCP-heavy): 6-15 tools (GitNexus v33 + browser-use v41)
  - Tier 3 (MCP-platform-scale): 100+ tools (ruflo v42 313 — corpus-first)

**4. Pattern #20 Solo-Scale Ceiling dictionary:**
- RuvNet solo-individual-multi-sibling-ecosystem-portfolio-with-commercial-entity 33K/16mo
- Add new row to dictionary; ceiling analysis: solo with commercial-ecosystem + self-branded commercial entity (Cognitum.One) can sustain enterprise-scale. 3rd+ solo-enterprise-scale data point (graphify v16 30K + agency-agents v18 82.9K + crawl4ai v29 64K + **ruflo v42 33K**).

**5. Pattern #31 Open-Core Commercial Entity:**
- Cognitum.One commercial entity (security@cognitum.one is the official security contact per SECURITY.md)
- Ruflo OSS MIT + Flow Nexus cloud platform (commercial tier referenced in README "☁️ **Cloud Platform** Flow Nexus")
- **Verification:** Flow Nexus = commercial cloud tier for ruflo OSS → YES open-core
- **N=6 strengthening** (currently confirmed N=5: fish-speech + Skyvern + OpenHands + crawl4ai + browser-use + ruflo = 6)
- License variety: ruflo = MIT at T2 scale (joins browser-use MIT at T5 89.9K)

**6. Pattern #50 Commercial-Funnel Companion Platform:**
- Cognitum.One (homepage) + Flow Nexus (cloud tier referenced) + Agentics Foundation Discord
- **N=5 strengthening** (currently confirmed N=4 post-v41: VoltAgent + Glama + ... + Browser-Use Cloud)
- Novel observation: 3-layer commercial structure (Cognitum.One parent / Flow Nexus SaaS / Agentics Foundation community-feed)

**7. Pattern #22 AGENTS.md:**
- AGENTS.md = 20.7KB (substantial; T2 scale)
- Compare: browser-use v41 = 37.4KB (corpus-largest T5), pi-mono v36 = 182 lines T1
- Ruflo AGENTS.md is Codex-focused (distinct sub-use: AGENTS.md as OpenAI-Codex-primary config)
- **Strengthening data point** — T2 observation with Codex-specific archetype

**8. Pattern #28 Multi-Provider AI Support:**
- 6 providers with failover (Anthropic, OpenAI, Google, Cohere, Ollama, + cost-based routing)
- **10th data point** (currently N=9 post-v41) — strengthening

**9. Pattern #27 Community-Viral Scale Path:**
- 33K/16mo ≈ 2,060 stars/month sustained-community-viral
- **18th observation** — T2 scale + solo + ecosystem-portfolio combination

**10. Pattern #12 Governance-Depth counter-evidence (solo + heavy governance):**
- pi-mono v36 (T1 solo + 182-line AGENTS.md)
- claude-hud v35 (T1 solo + 7 governance files)
- **ruflo v42 (T2 solo + 6 files including 280KB README + 38.9KB CLAUDE.md + 20.7KB AGENTS.md + 70+ ADRs)**
- **N=3 refinement trigger** — Pattern #12 original formulation "governance-depth correlates with ORGANIZATION (corporate vs solo)" should be REFINED to "governance-depth correlates with MATURITY-ambition + maintainer-philosophy, NOT solo-vs-corporate alone"
- **Propose formal refinement at next mini-audit**

**11. Pattern #8 Research-Benchmark Integration:**
- No explicit third-party benchmark (no arXiv paper, no SWE-Bench, no peer-review)
- README claims performance metrics ("89% accuracy" task routing / "Fast adaptation" / "Sub-millisecond retrieval") but no external validation
- **Not a Pattern #8 data point** — internal-benchmark-only; flag as absence-signal

**12. Pattern #9 Multi-axial tier bifurcation (Resolution D):**
- Ruflo is BOTH T2 (service/platform) AND T1 (Claude Code extension) = strong cross-tier archetype
- Strengthens Resolution D at T2 level

**13. EXTREME primitive-count observation:**
- 500+ primitives ~2.5× browser-use v41 RED (~200 primitives)
- **Potential OBSERVATION-TRACK:** "Primitive-count distribution in T2 vs T1 vs T5 agent-platforms" (within-Phase-0.9 methodology, NOT new pattern)
- **Decision:** do NOT register as pattern; document as v2.2 routine-reform input (tier naming: GREEN/YELLOW/RED/**EXTREME**)

**14. v3 monorepo as T2 architectural signal:**
- 6-package monorepo (@claude-flow/cli + codex + guidance + hooks + memory + security)
- Parallel to pi-mono v36 7-package monorepo (T1 scale)
- Observation: multi-package-internal-monorepo-with-external-sibling-packages architecture pattern emerging
- **Decision:** within-Pattern-#17 variant 1 observation; no new registration

**15. Dual-mode Claude+Codex first-class integration:**
- Ruflo treats OpenAI Codex CLI as first-class peer via `@claude-flow/codex` dedicated package
- README "Dual-Mode Integration" section + CLAUDE.md "Dual-Mode Collaboration" section
- Parallel to OMC v27 4-runtime orchestration (Claude + Codex + Gemini + Cursor)
- **Pattern #56 Multi-Runtime Orchestration** — candidate N=1 OMC → N=2 ruflo (Claude+Codex)
- **Decision:** strengthening-not-promotion (different scale: OMC is 4-runtime, ruflo is 2-runtime + deeper-Codex-integration). Keep #56 as candidate; note N=1.5 structural variant.

**16. Un-stale check:**
- #45 Dual-Licensing: Ruflo = MIT single-license → negative
- #52 Extreme-Viral-Velocity: 33K/16mo = 2K/month (moderate, not extreme viral) → negative
- #46 Duo-Founder: Ruflo is solo → negative (but #46 just un-staled v41)
- #67 Academic-Commercial Fusion: Ruflo has Agentics Foundation (community, not academic) → negative
- #66 Supply-Chain Incident: No documented incident → negative

**17. Consolidation-forward discipline:**
- **Target: 0 new active candidates** (6 consecutive streak)
- All 16 pattern-relevant observations routed to strengthening existing patterns
- No borderline new-candidate OR OBSERVATION-TRACK registrations
- **Prefer**: Pattern #12 refinement proposal + Pattern #58 un-stale + Pattern #18 formal-statement-update proposal at next mini-audit

**18. N=1 stale-risk-flagging:** N/A (no new registrations)

## Phase 4b routing mode decision

**Primary mode:** Tier-within-variant-extension + Counter-evidence-refinement + Un-stale-mechanism (compound)
- T2 extends N=2 → N=3 (goclaw + multica + ruflo)
- Pattern #58 un-stale from N=1 → N=2 promotion-candidate
- Pattern #12 counter-evidence refinement (solo-heavy-governance N=3)
- Pattern #18 formal-statement-update (MCP-tool-count distribution tiers)

**Secondary modes:**
- Pattern-strengthening (6+ patterns advanced without registration)
- EXTREME primitive-count precedent (corpus-methodology contribution)
- Consolidation-forward discipline (6 consecutive zero-registration streak)

## Phase 6 Storm Bear meta-entity applicability: YES

Ruflo meets Storm Bear meta-entity criteria:
- **Pilot candidate?** MEDIUM — ruflo's `/plugin marketplace` + 313 MCP tools + swarm orchestration have direct Scrum-coaching applicability BUT EXTREME primitive-count makes it a heavy-onboarding investment (likely 2-4 weeks). Ranked #4 if feasible.
- **Observational value?** HIGH — Pattern #58 un-stale, Pattern #12 refinement, Pattern #18 formal-statement-update, Pattern #17 variant 1 strongest evidence, solo-at-T2-enterprise-scale archetype, EXTREME-tier methodology precedent.
- **Meta-entity warranted?** YES — 31st consecutive + vault-architectural lesson (aggressive compression for EXTREME primitive-counts + structural-promotion-via-un-stale precedent).

## Cross-wiki siblings

- **v27 oh-my-claudecode** (T1 multi-runtime orchestration; Pattern #58 founding data point) — primary structural parallel
- **v18 agency-agents** (T1 solo-at-enterprise-scale precedent)
- **v15 multica** (T2 managed-agents-platform; closest T2 archetype peer)
- **v4 goclaw** (T2 multi-tenant platform; T2 N=2 precedent)
- **v14 paperclip** (T5 orchestration-for-zero-human-companies; autonomy-framing neighbor)
- **v31 awesome-mcp-servers** (MCP-ecosystem-directory; Pattern #18 meta-reference)
- **v33 GitNexus** (prior MCP-tool-count max 16; Pattern #18 upper-bound precedent)
- **v30 OpenHands** (similar ADR-driven + enterprise-ambition + academic-commercial-fusion-adjacent via Agentics Foundation)

---

## Deliverables checklist

- [x] Phase 0: 12-axis classification + Pattern pre-check + EXTREME primitive-count probe
- [ ] Phase 1: Scaffold complete (this file + foundational wiki files)
- [ ] Phase 2: 3 cluster summaries
- [ ] Phase 3: 4 entity pages (with 31st Storm Bear meta-entity)
- [ ] Phase 4a: Bilingual VN+EN beginner guide
- [ ] Phase 4b: Primary deliverable (T2 extension + Pattern #58 un-stale + Pattern #12 refinement + Pattern #18 formal-statement-update + EXTREME-tier methodology)
- [ ] Phase 5: Iteration log v42 + PATTERN_LIBRARY.md direct update
- [ ] Phase 6: Vault sync (index / log / root CLAUDE / PATTERN_LIBRARY / GOALS)
