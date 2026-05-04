# shannon - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`KeygraphHQ/shannon`](https://github.com/KeygraphHQ/shannon) — **"Shannon — autonomous, white-box AI pentester for web applications and APIs."**

**40.1K stars, 4.4K forks (11.0%), 195 watchers, 17 open issues, AGPL-3.0 (Shannon Lite; Shannon Pro commercial), TypeScript (pnpm-workspaces monorepo: `apps/cli` + `apps/worker`), main branch, v1.1.0 (2026-04-21 latest release), Trendshift badge repository 15604, Topics: security-audit / penetration-testing / pentesting / security-automation / security-tools**. Organization: **Keygraph** (commercial startup; homepage keygraph.io; SOC 2 Type I certified). Product line: **Shannon Lite (AGPL-3.0 OSS, this repo) + Shannon Pro (commercial all-in-one AppSec platform with SAST/SCA/secrets/business-logic/pentesting correlation + Tower managed service)**. Customers cited: Optexity, Scowtt Inc., Mesmer.

**Scope status: T5 Agent-as-application — 9TH T5 ENTRANT with NEW AI-pentester sub-archetype.** 100% T5 archetype-diversity preserved at N=9 (prior 8 sub-archetypes: research-deer-flow v9 / ML-autoresearch v10 / orchestration-paperclip v14 / browser-automation-Skyvern v24 / SWE-OpenHands v30 / education-DeepTutor v38 / browser-viral-browser-use v41 / personal-productivity-rowboat v43).

**Positioning (verbatim):**
- *"Shannon is an autonomous, white-box AI pentester for web applications and APIs. It analyzes your source code, identifies attack vectors, and executes real exploits to prove vulnerabilities before they reach production."*
- *"Thanks to tools like Claude Code and Cursor, your team ships code non-stop. But your penetration test? That happens once a year. This creates a massive security gap."*
- **Core principle:** *"POC or it didn't happen"* / *"No Exploit, No Report"* policy

## Core product — 10+ corpus-firsts

**Shannon Lite (this repo — AGPL-3.0):**
- **Autonomous AI pentester T5 sub-archetype** — corpus-first (prior T5 = research/ML/orchestration/browser/SWE/education/personal-productivity)
- **White-box + source-code-aware dynamic testing** — corpus-first (prior browser-agent T5 Skyvern/browser-use = black-box)
- **5 attack domains × 2 phases = 10 specialized agents** — Injection + XSS + SSRF + Auth + Authz × Vulnerability-analysis + Exploitation + shared (pre-recon-code / recon / report-executive) = 13 prompt files total
- **4 security-tool integrations** — Nmap + Subfinder + WhatWeb + Schemathesis (corpus-first integrated security-tooling suite)
- **Autonomous 2FA/TOTP/SSO login handling** — corpus-first in T5 (generate-totp CLI; TOTP via dedicated MCP server in Pro)
- **96.15% on hint-free XBOW security benchmark** — corpus-first XBOW benchmark usage (first pentesting-domain peer-reviewed-equivalent eval; prior benchmarks WebBench Skyvern / SWE-Bench OpenHands / ML-research-paper chains)
- **Pipelined parallel processing** — 5 vuln + 5 exploit agents run concurrently; per-domain early-start when vuln agent completes
- **Temporal-backed workflow durability** — corpus-first Temporal.io orchestration at T5 scope
- **Per-invocation ephemeral Docker container + per-scan task queue** — corpus-first deterministic isolation architecture
- **Workspaces + git-checkpoint-resume** — each agent checkpointed via git commit; resumable from any failure point
- **Sample-reports directory with OWASP Juice Shop + c{api}tal + crAPI real pentest reports** — corpus-first proof-of-capability demonstration artifact in repo
- **Claude Agent SDK as reasoning core** — `@anthropic-ai/claude-agent-sdk` v0.2.38 with `maxTurns: 10_000` + `bypassPermissions`

**Shannon Pro (commercial, SHANNON-PRO.md 26KB documented — observational only, not in Lite):**
- **Code Property Graph (CPG)** — AST + CFG + PDG unified structure; corpus-first at T5
- **Static-dynamic correlation pipeline** — static-analysis findings fed into dynamic exploitation queue; corpus-first architectural pattern
- **Business-logic invariant discovery + fuzzer generation + exploit synthesis** — 4-phase pipeline (invariant / fuzzer / violation / PoC); corpus-first at T5
- **SCA with reachability analysis via CPG** — distinguishes reachable CVEs from unreachable
- **Secrets detection with liveness validation** — regex + LLM + active API auth check (read-only)
- **Self-hosted runner model** — GitHub-Actions-style split: customer data plane + Keygraph control plane; corpus-first at T5
- **Boundary analysis for monorepo scoping** — corpus-first
- **13 specialized agents in 5 phases** — Pro expands on Lite with static-analysis agents

**Commercial structure (2-tier open-core):**
- Shannon Lite: AGPL-3.0 OSS (local testing; sharing requirements apply if offered as SaaS)
- Shannon Pro: Commercial licensed; enterprise SAST+SCA+secrets+business-logic+pentest
- **Contributing policy:** *"At this time, we're not accepting external code contributions (PRs)."* — issues-only governance (corpus-first at T5 scale)
- **SOC 2 Type I certified** (Keygraph)

**Intellectual lineage:** Tool-lineage archetype (Pattern #19 archetype 4 no-lineage). Implicit Anthropic SDK integration (Claude Agent SDK); Playwright browser automation; Temporal workflow; Nmap/Subfinder/WhatWeb/Schemathesis. No explicit individual-author lineage cited. Consistent with v33 GitNexus + prior tool-lineage T5 entries.

## v2.1 Routine 12-axis classification

| Axis | Value |
|------|-------|
| **Tier** | **T5 Agent-as-application — 9th T5 entrant + NEW AI-pentester sub-archetype (distinct from 8 prior sub-archetypes)** |
| **Archetype** | Commercial-startup-AGPL-open-core-with-dedicated-Pro-tier-documentation (Keygraph) |
| **Scale tier** | Medium-large (40.1K / ~16 months ≈ 2.5K/month organic — fast but not extreme-viral) |
| **Primary lang** | TypeScript monorepo (pnpm-workspaces + Turborepo + Biome + tsdown) |
| **Packaging** | npm `@keygraph/shannon` (via npx) + Docker Hub `keygraph/shannon` + Clone+Build (pnpm) — 3 surfaces |
| **Origin story** | Commercial-founded (Keygraph) + OSS Lite as lead-gen + proprietary Pro as revenue |
| **Methodology** | White-box AI-pentesting + static-dynamic correlation (Pro) + "POC or it didn't happen" principle + OWASP WSTG/Top-10 alignment |
| **Governance** | Medium-heavy (README 39KB + CLAUDE.md 15KB + SHANNON-PRO.md 26KB + COVERAGE.md + LICENSE AGPL 33KB + .env.example + `.github/workflows/release.yml`) |
| **Agent/skill count** | **13 specialized agents** (5 vuln × Injection/XSS/SSRF/Auth/Authz + 5 exploit same domains + pre-recon + recon + reporting) + 13 prompt files |
| **i18n** | EN-only (notable absence at 40K scale; contrast fish-speech 7-language / OMC 7-language) |
| **Intellectual influence** | No explicit individual lineage (tool-lineage: Anthropic SDK + Temporal + Playwright + Nmap/Subfinder/WhatWeb/Schemathesis) |
| **Agent platforms** | Self-hosted Docker primary + managed-cloud-via-Pro — bounded (Claude Agent SDK only officially) |

## v2.1 Phase 0.5 pattern pre-check results

### Patterns strengthening (no status change) — SIGNIFICANT activity

- **Pattern #31 Open-Core Commercial Entity** (CONFIRMED v24) — **data-point strengthening.** Shannon Lite AGPL + Shannon Pro commercial = 2-tier with **dedicated SHANNON-PRO.md 26KB documentation file** (corpus-first most-detailed Pro-tier docs). Strengthens mature-open-core sub-observation.
- **Pattern #50 Commercial-Funnel Companion Platform** (CONFIRMED v36 mini-audit) — **data-point strengthening.** Keygraph + Tower managed service + Shannon Pro = full companion-platform stack.
- **Pattern #29 License-Category Diversity / AGPL-3.0** (CONFIRMED v21) — **3rd project-scope AGPL** (Skyvern v24 + browser-use NOT AGPL / Unsloth Studio v23 component-scope / TrendRadar v19 GPL / **shannon v45 AGPL project-scope**). AGPL sub-category strengthens.
- **Pattern #17 Ecosystem-Layer variant 3 commercial-startup** — **data-point strengthening.** Keygraph ecosystem = Shannon Lite OSS + Shannon Pro commercial + Tower managed + SOC 2 + case studies.
- **Pattern #18 Agent Runtime Standardization** (CONFIRMED v15, MCP-extended) — **MCP sub-observation** via Pro's *"TOTP is handled via a dedicated MCP server tool"* — Shannon Pro uses MCP for internal tool exposure (Tier 1 MCP consumer).
- **Pattern #28 Multi-Provider AI Support** (CONFIRMED v25) — **5-provider** (Anthropic direct + Claude Code OAuth + AWS Bedrock + Google Vertex + Custom-Base-URL-via-LiteLLM). Documents *"Only Claude models officially supported"* narrowing.
- **Pattern #58 Branding Divergence** (PROMOTED v42 mini-audit) — **4th observation data point.** `claude-code-router` router-mode sunset (feature-deprecation-with-public-discussion-notice at Discussion #301) = feature-lifecycle within repo. 4th observation after OMC v27 branding / ruflo v42 package-vs-display / rowboat v43 website/website-ng / magika v44 website-transition.
- **Pattern #12 Governance-Depth (REFINED v42 3-factor model)** — strong governance at medium-large commercial-startup scope (README 39KB + CLAUDE.md 15KB + SHANNON-PRO.md 26KB + LICENSE + COVERAGE + sample-reports + CONTRIBUTING via README + .github/workflows). Confirms maturity-ambition + maintainer-philosophy + scale-tier 3-factor refinement.
- **Pattern #27 Community-Viral Scale Path** (CONFIRMED v21) — **observational data point.** 40.1K / 16 months ≈ 2.5K stars/month organic-commercial sub-path (NOT extreme-viral; steady-commercial-growth).
- **Pattern #22 AGENTS.md** (CONFIRMED v17) — **T5 absence observation** (shannon has CLAUDE.md 15KB but NO AGENTS.md; T5 absence-continuation pattern).
- **Pattern #20 Solo-Scale Ceiling dictionary** (CONFIRMED v21 reformulated) — NEW ROW observation: commercial-startup + open-core + AGPL + dedicated-Pro-docs + 40K-in-16-months.

### Domain-scope observations (neither strengthening nor invalidating)

- **Pattern #47 Vision-Based Browser Automation** (REFINED v29 3-point spectrum) — **Shannon uses browser automation but NOT vision-primary** (Shannon is DOM-based + CLI-based pentesting, like crawl4ai DOM-only variant). Does NOT satisfy un-stale trigger for #47 (still conditional retirement at v46 if no 2nd vision-primary).
- **Pattern #48 Proprietary Anti-Bot Commercial Moat** (PROMOTED v42-deferred mini-audit) — **Shannon is security-testing domain NOT browser-anti-bot.** Scope-distinct: pattern scope locked to browser-agent commercial anti-bot gating. Shannon's AGPL + Pro-tier gating is different domain. **Does NOT strengthen #48** — scope-respect.

### Un-stale check (5 stale candidates)

- **#14 Alignment-Theory Visibility** — negative (shannon has no alignment-theory framing)
- **#16 Skill Dependency Locking** — negative (no lockfile beyond pnpm-lock; not skill-focused)
- **#21 SDD Methodology Emergence** — negative (shannon is not SDD)
- **#23 AI-Disclosure Policy** — negative (no explicit AI-disclosure policy found)
- **#25 Personality-Driven Agent Design** — negative (agents are domain-specialized not personality-driven)

All 5 stale stay stale. Disciplined negative results.

### Counter-evidence observations

- **Pattern #31** — Shannon demonstrates mature-open-core with dedicated Pro-tier documentation file (SHANNON-PRO.md 26KB) = most-detailed Pro-tier docs in corpus. Observational data point for potential sub-variant-formalization at future audit if N=2 of mature-open-core-with-dedicated-docs emerges.
- **Pattern #18 MCP adoption** — Shannon Pro uses MCP selectively (TOTP-only at start, not broad MCP adoption). Confirms pi-mono v36's ~70-75% MCP adoption observation.

### Consolidation-forward discipline

**Target: 0 new active candidates (9th consecutive wiki — extends corpus-longest streak v37-v44 to v37-v45).**

Rejected candidate attempts (all routed to within-existing-pattern strengthening):
1. **AI-pentester T5 sub-archetype** — T5 sub-archetype = taxonomic observation within tier, NOT pattern registration (consistent with prior 8 T5 sub-archetypes)
2. **Autonomous 2FA/TOTP/SSO agent handling** — observational within #18 MCP layer (TOTP via dedicated MCP server)
3. **Static-dynamic correlation pipeline (Pro)** — observational within Pattern #2 Distribution Evolution or T5 methodology documentation; commercial-only (not in Lite)
4. **Security-tool integration suite (Nmap + Subfinder + WhatWeb + Schemathesis)** — observational within #18 external-tool layer
5. **CPG (Code Property Graph)** (Pro) — commercial-only observational reference; not testable from Lite
6. **Business-logic invariant-fuzzer-generation** (Pro) — commercial-only observational
7. **"POC or it didn't happen" / "No Exploit, No Report"** principle — methodology philosophy, not architectural pattern
8. **sample-reports/ directory** — proof-of-capability artifact observational (not pattern)
9. **Issues-only-no-PRs governance** — governance-convention observational within Pattern #12 refined
10. **Self-hosted runner model (Pro)** — commercial-only observational within Pattern #31 deployment sub-observation

## Phase 0.9 Primitive-count probe (v2.1 informal discipline)

Estimated primitives:
- 13 specialized agents (10 vuln+exploit × 5 domains + pre-recon + recon + report)
- 13 prompt files (matching agent count)
- 5 attack domains (Injection / XSS / SSRF / Auth / Authz)
- 5 pipeline phases (pre-recon / recon / vuln / exploit / reporting)
- 3 deployment surfaces (npx / Clone+Build / self-hosted Pro runner)
- 5 AI provider options (Anthropic direct / Claude Code OAuth / AWS Bedrock / Google Vertex / Custom Base URL)
- 3 model tiers (small/medium/large via ANTHROPIC_*_MODEL env vars)
- 3 CLI commands main (setup / start / stop) + 5 subcommands (logs / status / workspaces / build / uninstall)
- 4 security-tool integrations (Nmap / Subfinder / WhatWeb / Schemathesis)
- 7 Pro analysis capabilities (data-flow SAST / point-issue / business-logic / SCA reachability / secrets / boundary / false-positive-tagging)
- 3 sample reports (Juice Shop / c{api}tal / crAPI)
- Workspaces + resume + git-checkpoint system
- Dual CLI mode (npx / local) + TOML config + YAML authentication config

**Count estimate:** ~120-150 primitives = **YELLOW** (DeepTutor v38 range; not ruflo EXTREME or browser-use RED).

**Scope-compression decisions:**
- **4-entity format preserved** (standard; not variable)
- **Focus on Shannon Lite (this repo)** — Pro covered observationally via SHANNON-PRO.md references, NOT replicated primitive-by-primitive
- **Citation-not-replication** for: full WSTG coverage table (reference COVERAGE.md), full AWS Bedrock / Vertex / Custom-Base-URL setup wizard details (reference README)
- **Lossy compression accepted:** Pro's 13-agent 5-phase static-analysis pipeline mentioned as observational reference, NOT exhaustively documented as primary entity (commercial tier = secondary focus)
- **Velocity target:** ~2h 30min (YELLOW tolerance band)

## Phase 4b routing

**Primary mode:** T5 N-way extension (9-way) + AI-pentester sub-archetype formalization + Pattern #31 N=8 strengthening + Pattern #50 N=7 strengthening.

**Single Phase 4b deliverable** covers all four concerns (similar to v28 / v30 / v42 multi-concern deliverables).

## Storm Bear meta-entity applicability (Phase 0.9)

**Decision:** INCLUDE — but with LOW direct-pilot score, MEDIUM-HIGH observational value.

**Storm Bear Direct pilot relevance:** **LOW** — Storm Bear vault is a markdown knowledge base, NOT a web application. Shannon requires source code + running web app to test. Potential future use IF Storm Bear develops web-app product (e.g., Scrum coaching SaaS). **Pilot ranking: #12 (LOWEST; lower than GitNexus v33 prior lowest)** due to markdown-vault fundamental mismatch.

**Observational value HIGH:**
1. T5 AI-pentester 9th sub-archetype reference
2. Static-dynamic correlation pipeline architectural pattern
3. Keygraph commercial-startup playbook (OSS lead-gen + Pro tier + managed Tower service + SOC 2)
4. 13-agent pipelined-parallel orchestration reference
5. Temporal + Docker ephemeral container durability pattern
6. Most-detailed Pro-tier documentation file (SHANNON-PRO.md 26KB) = strategic-marketing reference
7. Ethical framing — authorization-required + AGPL-derivative-disclosure + responsible-disclosure as template for Storm Bear ethical-product-positioning (if commercial product emerges)

**34th consecutive Storm Bear meta-entity (v10-v45) will be included.**

## Expected deliverables at v45

- 1 project CLAUDE.md (this file)
- 3 cluster summaries (README+positioning / Architecture+monorepo+Temporal / Keygraph commercial+Pro tier + sample reports)
- 4 entity pages (Shannon Lite core / Keygraph ecosystem+Pro tier / T5 meta 9-way + AI-pentester sub-archetype / 34th Storm Bear meta)
- 1 bilingual VN+EN beginner guide (~430 lines, ⚠️ authorization-required + AGPL-derivative-disclosure + responsible-disclosure framing PROMINENT)
- 1 Phase 4b primary deliverable: T5 9-way + AI-pentester sub-archetype formalization + Pattern #31 N=8 strengthening + Pattern #50 N=7 strengthening (~650 lines)
- 1 iteration log v45 with 13 sections
- 1 index + 1 log + 1 open-questions

## Current Status

> **Last updated:** 2026-04-24
> **Status:** ✅ Routine v2.1 auto-execute COMPLETE — 45th LLM Wiki shipped, 5th+ v2.1-era execution, T5 9th entrant, 9-streak zero-registration extended (v37-v45 NEW LONGEST)

### Milestones

- [x] Phase 0 Pre-flight with 12-axis + pattern pre-check + primitive-count YELLOW + consolidation guard (0.54:1 green)
- [x] Phase 1 Scaffold
- [x] Phase 2 Source ingestion (3 clusters)
- [x] Phase 3 Entity pages (4)
- [x] Phase 4a Beginner bilingual guide with ethical framing
- [x] Phase 4b T5 9-way + Pattern #31 N=8 + Pattern #50 N=7 + AI-pentester sub-archetype
- [x] Phase 5 Iteration log v45 + PATTERN_LIBRARY.md update
- [x] Phase 6 Vault file updates (CLAUDE.md post-v45 state block + project entry + GOALS.md session 53 entry + Last-updated)

## Claude's Role

Claude runs the `llm-wiki-routine-v2.1` skill (45th auto-execution; 5th+ v2.1-era execution). Ingest via WebFetch + local clone reads. Cross-reference with 44 sibling wikis. Direct Pattern Library updates.
