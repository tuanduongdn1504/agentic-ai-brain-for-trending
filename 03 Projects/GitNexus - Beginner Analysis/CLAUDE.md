# GitNexus - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`abhigyanpatwari/GitNexus`](https://github.com/abhigyanpatwari/GitNexus) — **"Building nervous system for agent context. Indexes any codebase into a knowledge graph — every dependency, call chain, cluster, and execution flow — then exposes it through smart tools so AI agents never miss code."**

**28,467 stars (#11 in corpus — between HF agents-course 27,995 v26 and claude-howto 28,186 v32), 3,273 forks (11.5%), 97 subscribers, 305 open issues, PolyForm Noncommercial 1.0.0 (CORPUS-FIRST PolyForm license family), TypeScript (primary), main-branch, created 2025-08-02 (~8.5 months), pushed 2026-04-22 (active).** Homepage: **gitnexus.vercel.app**. npm: `gitnexus`. Commercial entity: **akonlabs.com** (SaaS & Self-hosted Enterprise).

Owner: **Abhigyan Patwari (abhigyanpatwari)** — based in **Guwahati, Assam, India**. Bio: *"CS student & AI engineer who likes to dig into the guts of systems. If it's interesting, I'll probably try to build something with it."* 444 followers, 20 public repos, GitHub account since 2023-02-25. **1st Indian-authored framework in Storm Bear corpus** — adds to regional archetype observations (Korean #55 N=1 + VN #70 CONFIRMED N=2 + now Indian at T4 N=1).

**Scope status: T4 Agent-as-bridge — 7TH T4 ENTRANT (2nd-largest tier) + FIRST PolyForm Noncommercial license + FIRST Indian-authored framework in corpus + solo-student-author with commercial-company companion (akonlabs.com Enterprise tier).**

**Positioning:** *"Building nervous system for agent context."* Anti-thesis: codebase knowledge should be a PRECOMPUTED knowledge graph, not real-time grep/search. Metaphor: AI agents have no spatial awareness of code → GitNexus = nervous system providing architectural perception.

**Core product:**
- **Codebase → knowledge graph** via Tree-sitter (native CLI) + WASM (browser). 14 languages: TypeScript, JavaScript, Python, Java, Kotlin, C#, Go, Rust, PHP, Ruby, Swift, C, C++, Dart.
- **LadybugDB embedded graph database** with vector index support (native + WASM variants) — **corpus-first LadybugDB usage**
- **16 MCP tools** exposed: per-repo (list_repos / query / context / impact / detect_changes / rename / cypher) + group operations (group_list / group_sync / group_contracts / group_query / group_status)
- **5 deployment modes:** npm global CLI + npx ephemeral + browser (gitnexus.vercel.app) + Docker Compose + Kubernetes (Sigstore-signed images with policy-controller)
- **5 AI editor integrations:** Claude Code (full — MCP + Skills + Hooks PreToolUse+PostToolUse) / Cursor (MCP + Skills) / Codex (MCP + Skills) / Windsurf (MCP only) / OpenCode (MCP + Skills)
- **Agent skills in `.claude/skills/`:** Exploring / Debugging / Impact Analysis / Refactoring + auto-generated repo-specific skills via `--skills` flag
- **Process-grouped hybrid search:** BM25 + semantic + Reciprocal Rank Fusion (RRF) — novel search primitive for corpus
- **Wiki auto-generation** from knowledge graph (LLM-powered documentation extraction) — distinct from graphify v16 Obsidian export
- **Blast radius analysis + git-diff impact detection + multi-file coordinated rename** — governance-primitive set
- **Sigstore (Cosign keyless) Docker signing + Kubernetes policy-controller enforcement** — **corpus-first supply-chain-signed-image deployment protocol**
- **Browser-only mode** supports ~5k files via WebGPU + transformers.js; unlimited via bridge mode with local server

**Companion / commercial ecosystem (open-core structure):**
- **OSS:** `abhigyanpatwari/GitNexus` (PolyForm Noncommercial 1.0.0, this wiki)
- **Enterprise (closed):** akonlabs.com — PR Review + auto-updating code wiki + auto-reindexing + multi-repo + OCaml support + priority features
- **Commercial Discord:** discord.gg/AAsRVT6fGb (inquiries); public Discord: discord.gg/MgJrmsqr62 (community)
- **Commercial contact:** founders@akonlabs.com

**Community integrations (third-party):**
- `pi-gitnexus` by @tintinweb — pi.dev plugin
- `gitnexus-stable-ops` by @ShunsukeHayashi — Miyabi ecosystem deployments

**Intellectual influence cited (Acknowledgments):** Tree-sitter (AST parsing) + LadybugDB (embedded graph+vector DB) + Sigma.js (WebGL rendering) + transformers.js (browser ML) + Graphology (clustering) + Anthropic MCP protocol. No individual lineage cited (distinct from Karpathy / John Lam / Boris Cherny archetypes). **Tool-lineage archetype** — lineage through dependencies not individuals.

**Origin story (inferred):** Created 2025-08-02, ~8.5 months ago. Author Abhigyan = CS student + AI engineer in Guwahati, India. Growth 28K stars in 8.5 months = ~3,352 stars/month sustained-community-viral. Commercial entity akonlabs.com indicates open-core monetization from early-stage.

**v2.1 Routine 12-axis classification:**

| Axis | Value |
|------|-------|
| **Tier** | **T4 Agent-as-bridge (7th T4 entrant — 2nd-largest tier extends further)** |
| **Archetype** | **Solo-Indian-author-student with commercial-entity companion (open-core structure)** — hybrid of Pattern #17 individual-led-dev variant + Pattern #31 open-core commercial-entity (confirmed v24, N≥3 now) + NEW Indian-at-T4 regional observation (not yet pattern; single data point) |
| **Scale tier** | **Large (20-60K)** — 28.5K stars in 8.5 months (~3.3K/mo sustained) |
| **Primary lang** | TypeScript (React + Node.js + WASM compilations of tree-sitter + LadybugDB + transformers.js) |
| **Packaging** | npm (`gitnexus` global CLI) + npx + web (browser-only) + Docker Compose + Kubernetes (Sigstore-signed) |
| **Origin story** | Individual-pedagogical/engineering + open-core commercial (akonlabs.com) |
| **Methodology** | Knowledge-graph-for-agent-context (bridge methodology; domain-specific) |
| **Governance file count** | **3-4 (medium)** — README + CONTRIBUTING + LICENSE (PolyForm) + possibly SECURITY (to verify) |
| **Agent/skill count** | 16 MCP tools + 4 built-in skills + auto-generated repo-specific skills (unbounded) |
| **i18n** | **EN-only** (no translations; notable absence at 28K-scale T4) |
| **Intellectual influence** | Tool-lineage archetype — Tree-sitter + LadybugDB + Sigma.js + transformers.js + Graphology + Anthropic MCP. No individual-author lineage cited. |
| **Agent platforms** | **5** (Claude Code full + Cursor + Codex + Windsurf + OpenCode) — narrower than graphify v16's 15 platforms |

**Tier placement rationale:** T4 Agent-as-bridge — GitNexus is a BRIDGE between codebase (source) and AI agent (consumer). Does not autonomously execute tasks (not T5); does not teach (not T3); does not provide assistant-level feature-framework (not T1); does not host service (not T2). Bridges code → knowledge graph → MCP → agent consumption. **Direct peer with graphify v16** (code+docs → knowledge graph → Claude Code skill). Differs from graphify: browser-native runtime, embedded graph DB, narrower platform integration, MCP-first surface, PolyForm license, commercial-entity companion, CS-student author vs small-brand ecosystem-layer.

**Cross-wiki siblings (MANDATORY cross-references):**

Primary:
- **graphify v16** (safishamsi/penpax.ai) — **#1 sibling** — direct semantic peer (code → knowledge graph → agent skill); both enable "AI agents understand codebase structure"; compare Python/local vs TypeScript/browser runtime + license approach + commercial model
- **crawl4ai v29** (unclecode solo-enterprise T4) — **#2 sibling** — Pattern #20 solo-scale dictionary row peer (3rd solo-enterprise-scale T4 candidate); similar solo-author-with-commercial-platform structure; crawl4ai web-content / GitNexus code
- **markitdown v28** (Microsoft AutoGen T4 utility) — **#3 sibling** — T4 5-way peer; corporate-narrow-utility vs solo-broad-knowledge-graph
- **fish-speech v20** (39 AI, INC. open-core) — Pattern #31 Open-Core analog (PolyForm ≈ custom-research-license as commercial-gating mechanism; distinct from AGPL/MIT)

Secondary:
- **gws v13** (official Google Workspace T4) — T4 5-way ancestor
- **notebooklm-py v7** (teng-lin solo T4) — T4 5-way ancestor
- **TrendRadar v19** (sansan0 solo-CN T4) — T4 5-way ancestor; regional-archetype absence comparison (CN vs Indian)

Pattern-relevant:
- **Skyvern v24** (Skyvern-AI T5 open-core AGPL) — Pattern #31 Open-Core peer + proprietary anti-bot moat comparison
- **awesome-mcp-servers v31** (Fiegel+Glama) — Pattern #18 MCP-runtime-standard consumer (GitNexus exposes 16 MCP tools; GitNexus listed-or-listable in awesome-mcp-servers directory)
- **OpenHands v30** (All Hands AI academic-commercial T5) — Pattern #42/#44 academic-adjacent observation (Abhigyan = CS student, not yet academic-lab publication; observation not pattern)
- **claude-howto v32** (luongnv89 VN-diaspora T1) — Pattern #70 VN-Regional-Archetype T1 analog; GitNexus introduces Indian-at-T4 observation (cross-tier; not yet regional-archetype pattern)

**v2.1 Phase 0.5 expanded pattern pre-check:**

1. **Overlap pre-check** — proposed new candidates evaluated:
   - **"PolyForm Noncommercial License as Commercial-Gate"** — distinct from #29 License-Category Diversity (CONFIRMED v21; categorical diversity observation) and #33 Non-OSI Custom License (candidate registered v20 for fish-speech custom). PolyForm is STANDARDIZED non-OSI license family (not custom-written) specifically DESIGNED for commercial-gating via non-commercial restriction. Structurally distinct: fish-speech = custom-written research-only; PolyForm = standard license family with commercial-gate clause. **Register as #72 stale-risk-flagged at N=1.**
   - **"Browser-native knowledge-graph runtime"** — WASM tree-sitter + WASM LadybugDB + WASM transformers.js + WebGPU. Structurally distinct from graphify v16 (Python-local). Could be new candidate BUT observation is highly niche (no second corpus entrant yet). **Defer** — strengthen Pattern #20 dictionary row instead.
   - **"Indian-Regional-Archetype T4"** — cross-tier regional observation. Pattern #55 Korean at T1 + Pattern #70 VN at T1 are T1-specific regional archetypes. T4 Indian would be 1st non-T1 regional archetype observation. **Too premature for pattern** — noted as wiki observation, not registered as candidate (consolidation-forward discipline preserved; defer until 2nd cross-tier regional observation).

2. **Un-stale check:**
   - #45 Dual-Licensing (STALE v29) — single PolyForm Noncommercial (not dual), though commercial option exists via contact. No un-stale.
   - #46 Duo-Founder (STALE v29) — solo Abhigyan. No un-stale.
   - #52 Extreme-Viral-Velocity (STALE v31) — 28K/8.5mo = 3,352/mo ≈ 112/day = NOT extreme-viral (v25 awesome-design-md was ~3,000/day). No un-stale.
   - #55 Korean Regional Archetype T1 (STALE v32) — Indian ≠ Korean; T4 ≠ T1. No un-stale.

3. **Counter-evidence check:**
   - Pattern #17 Ecosystem-Layer 5-variant (CONFIRMED v15) — Abhigyan's 20 public repos is MUCH SMALLER ecosystem than Karpathy / Luong (claude-howto v32) / safishamsi (graphify v16). Abhigyan is primarily SINGLE-PROJECT + commercial-company (akonlabs). **Counter-evidence OR new variant:** individual-single-project-with-commercial-entity archetype; distinct from ecosystem-portfolio variant 1. Narrow-scope refinement candidate at next audit — NOT new registration.
   - Pattern #22 AGENTS.md — README doesn't mention AGENTS.md; needs cluster 2 verification. Continued potential T4 absence observation.
   - Pattern #9 Multi-Axial Tier Bifurcation Resolution D — T4 N=7 extends. Indian solo + commercial-company = a NEW archetype variant in T4 quadrant (joins gws corporate-broad, notebooklm-py solo-narrow, graphify solo-broad-local, TrendRadar solo-CN-external, markitdown corporate-narrow-utility, crawl4ai solo-broad-sustained). **T4 now has 7 archetype variants at N=7.**

4. **Consolidation-forward discipline:**
   - Indian regional observation NOT registered (defer for multi-region cross-tier registry)
   - PolyForm observation IS registered (structurally distinct license category, stale-risk-flagged N=1)
   - Commercial-entity-companion observation STRENGTHENS Pattern #31 (open-core); akonlabs.com = 4th corpus data point (after fish-speech/39 AI INC + Skyvern-AI + OpenHands/All Hands AI). Pattern #31 already CONFIRMED at N=3 post-v30; GitNexus extends N=4.

**v2.1 Phase 0.6 candidate overlap pre-check:** See above. Proposed new candidates:

- **#72 PolyForm Noncommercial Commercial-Gate License** (N=1 stale-risk-flagged at registration; distinct from #29 category-diversity and #33 custom-license — PolyForm is standard license family structurally designed for commercial-gating)

Deferring (strengthening existing instead):
- Abhigyan's single-project-with-company portfolio → potential variant of #17 (next-audit refinement)
- Browser-native knowledge-graph runtime → Pattern #20 dictionary row extension
- Indian regional observation → wiki note, not candidate
- Tool-lineage-archetype (no individual lineage cited) → Pattern #19 continuation (3-archetype model holds; tool-lineage = no-lineage sub-variant already observed in agency-agents v18)

**Phase 0.9 Storm Bear meta-entity applicability:** **YES** — GitNexus is a knowledge-graph tool with direct vault applicability: (1) Storm Bear vault could be indexed by GitNexus to extract cross-references / entity-structure / cluster semantics; (2) 21+ wiki corpus is de facto "codebase" that could benefit from knowledge-graph intelligence; (3) MCP integration means Claude Code could query vault structure via GitNexus; (4) PolyForm Noncommercial license has operator implications (permissive for personal use; commercial Scrum-coaching use requires akonlabs.com discussion). **22nd consecutive Storm Bear meta-entity.**

**Phase 4b routing decision:** Primary mode = **T4 N-way extension (N=6 → N=7)** with 1 new archetype variant (solo-Indian-student-with-commercial-company) + 1 new license observation (PolyForm Noncommercial). Secondary mode = **graphify v16 direct peer comparison** (knowledge-graph semantic peer; Python-local vs TypeScript-browser axis). Tertiary mode = **commercial-entity open-core deep-dive** (Pattern #31 4th data point — 4 distinct open-core license approaches observed now: PolyForm / custom-research / AGPL / MIT-with-enterprise-directory). Deliverable: ~600-700 lines T4 7-way comparison.

**Novel elements at v33 (corpus-firsts):**
1. **1st Indian-authored framework in corpus** (Abhigyan Patwari, Guwahati, Assam)
2. **1st PolyForm Noncommercial license** in corpus (4th non-permissive license distinct from GPL/AGPL/custom-research)
3. **1st CS-student author archetype** (distinct from academic-lab affiliation Pattern #44)
4. **1st LadybugDB usage** in corpus (embedded graph+vector DB)
5. **1st browser-native knowledge-graph runtime** (WASM tree-sitter + WASM graph DB + WASM embeddings + WebGPU)
6. **1st Sigstore-signed Docker deployment** in corpus (Kubernetes policy-controller supply-chain enforcement)
7. **1st "nervous system for agent context" philosophy framing** (distinct from graphify's "/raw folder answer" framing)
8. **1st BM25+semantic+RRF hybrid search** in corpus (graphify v16 uses graph-topology clustering WITHOUT embeddings; GitNexus uses embeddings + classical search fusion)
9. **1st explicit crypto-disclaimer-at-top** — corpus-first project leading with anti-crypto warning (response to Pump.fun token impersonation)
10. **1st Git-diff-impact-as-primary-feature** — `detect_changes` MCP tool maps changed lines to affected processes (graphify v16 doesn't do this)
11. **14 languages with per-language capability matrix** (type-annotation / constructor-inference partial) — most-detailed multi-language capability disclosure in corpus
12. **16 MCP tools at T4** — most MCP tools exposed per project in corpus (markitdown v28 had ~3, graphify v16 has MCP-server output)
13. **T4 7th entrant → 7 distinct archetype variants** (completes T4 diversity beyond T1's 10 archetype variants)
14. **Indian-at-T4 cross-tier regional observation** (wiki-noted, pattern-deferred) — adds to Korean-T1 + VN-T1 regional observations

**Risk/ethical framing considerations:**
- **PolyForm Noncommercial license restricts commercial use** without separate akonlabs.com agreement — ⚠️ "Read this first" section warranted in beginner guide (Scrum coaching is commercial; operator must evaluate)
- **Supply-chain awareness:** Sigstore signing + Kubernetes policy-controller = PRODUCTION-GRADE supply-chain posture (positive signal)
- **Student-author bus-factor:** solo-student with commercial-company = medium bus-factor risk (company offers continuity buffer)
- **No perverse incentive detected** — commercial Enterprise = standard open-core path; no ZeroLeaks-style incentive misalignment
- **Crypto disclaimer at top** — author explicitly distances from Pump.fun token impersonation (responsible governance signal)

**Phase 4b routing = T4 7-way extension + PolyForm license observation + Pattern #31 4th data point deliverable.**

## Claude's Role

Claude là wiki maintainer, chạy bằng routine `llm-wiki-routine-v2.1.md` (**33rd auto-execution, 14th v2-era execution, 2ND v2.1-era execution**):

- **Ingest sources via WebFetch + curl** — README + GitHub API + author profile + akonlabs.com (to verify)
- **Cross-reference với 32 sibling wikis** — primarily graphify v16 (direct semantic peer) + crawl4ai v29 (T4 solo-enterprise peer) + markitdown v28 (T4 utility peer) + fish-speech v20 (open-core commercial-entity peer) + Pattern #17/#20/#31 ecosystem
- **Phase 4b = T4 7-way extension + PolyForm Noncommercial license observation + Pattern #31 4th data point deliverable**
- **Beginner angle** — VN operator + developer + Scrum coach evaluating codebase-knowledge-graph tool; PolyForm commercial-gate warrants ethical framing

**Prime directive:** Outcome = wiki + PolyForm candidate #72 + Pattern #17/#20/#31 strengthening + Indian regional observation (noted, not registered) + fact-verification clean.

## Process — routine `llm-wiki-routine-v2.1.md`

7 phases. 2ND v2.1-era execution. Phase 4b = T4 7-way extension + PolyForm observation + Pattern #31 N=4 deliverable.

## Key People / Organization

- **Abhigyan Patwari (abhigyanpatwari)** — Guwahati, Assam, India; CS student & AI engineer; 20 public repos; 444 followers
- **akonlabs.com** — commercial entity (SaaS + Self-hosted Enterprise); founders@akonlabs.com; separate Discord
- **Community integrations:** @tintinweb (pi-gitnexus) + @ShunsukeHayashi (gitnexus-stable-ops Miyabi ecosystem)
- **Cross-project:** 32 sibling wikis. This is 33rd.

## Folder Structure

```
GitNexus - Beginner Analysis/
├── CLAUDE.md
├── 00 Sources/     01 Analysis/
├── 02 Wiki/        03 Published/
├── 04 Reviews/
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ VN + 13-section format
- **Cross-reference 32 siblings MANDATORY** — especially graphify v16 (direct peer) + crawl4ai v29 (T4 solo-enterprise) + markitdown v28 (T4 utility) + fish-speech v20 (open-core)
- **Pattern Library direct update** — register PolyForm #72 (N=1 stale-flagged) + strengthen Pattern #17/#20/#31 + Indian regional observation noted (deferred)

## Current Status

> **Last updated:** 2026-04-23
> **Status:** ✅ **COMPLETE** — 33rd LLM Wiki, 2ND v2.1-era execution, T4 7-way extension, PolyForm candidate #72 registered, Pattern #31 N=4 structural validation

### Expected milestones

- [x] Phase 0 Pre-flight (completed — 12-axis classified, overlap pre-checked, un-stale checked, counter-evidence flagged)
- [x] Phase 1 Scaffold
- [x] Phase 2 Source ingestion (3 clusters)
- [x] Phase 3 Entity pages (4)
- [x] Phase 4a Beginner published guide (~520 lines VN+EN bilingual; PolyForm ethical framing)
- [x] Phase 4b **T4 7-way extension + PolyForm observation + Pattern #31 N=4 deliverable** (~700 lines)
- [x] Phase 5 Iteration log v33 + PATTERN_LIBRARY.md direct update + fact-verification clean
- [x] Phase 6 Vault file updates (CLAUDE + GOALS + PATTERN_LIBRARY — counts consistent across all)
