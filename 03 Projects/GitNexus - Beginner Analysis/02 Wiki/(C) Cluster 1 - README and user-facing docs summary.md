# (C) Cluster 1 — README + User-facing docs summary

> **Source:** GitNexus README.md (33,747 bytes, ~720 lines) + homepage gitnexus.vercel.app + npm package `gitnexus` + Discord server `MgJrmsqr62`
> **Fetched:** 2026-04-23 via WebFetch
> **Role in wiki:** User-facing positioning + feature inventory + deployment mode catalog + editor support matrix

---

## 1. Project identity (verbatim)

- **Name:** GitNexus
- **Tagline:** *"Building nervous system for agent context."*
- **One-line description (GitHub):** *"GitNexus: The Zero-Server Code Intelligence Engine - GitNexus is a client-side knowledge graph creator that runs entirely in your browser."*
- **Owner handle:** abhigyanpatwari
- **Owner real name:** Abhigyan Patwari
- **Owner location:** Guwahati, Assam, India
- **Owner affiliation:** CS student & AI engineer (self-described); commercial entity akonlabs.com
- **Trendshift badge:** repository ID 19809 (trending indicator)
- **Homepage:** https://gitnexus.vercel.app
- **npm package:** `gitnexus` (global install)
- **License:** PolyForm Noncommercial 1.0.0
- **Primary language:** TypeScript (React frontend + Node.js CLI + WASM compilations)

## 2. Corpus-first observations (12)

1. **"Nervous system for agent context" philosophy framing** — distinct from graphify v16 ("/raw folder answer"), markitdown v28 ("Built by AutoGen Team"), crawl4ai v29 ("LLM Friendly Web Crawler"). Anthropomorphized metaphor — agents have PERCEPTION gap that a nervous system can fill.
2. **Anti-crypto disclaimer at top of README** — *"⚠️ Important Notice: GitNexus has NO official cryptocurrency, token, or coin. Any token/coin using the GitNexus name on Pump.fun or any other platform is not affiliated with, endorsed by, or created by this project or its maintainers. Do not purchase any cryptocurrency claiming association with GitNexus."* — first corpus project leading with anti-impersonation warning. Suggests Pump.fun scam targeted the project name, indicating meaningful reach.
3. **PolyForm Noncommercial 1.0.0 license** — corpus-first. Standard license family (polyformproject.org) distinct from custom-research licenses (fish-speech v20 Fish Audio Research License custom-written). PolyForm explicitly restricts all commercial use; commercial license obtained separately via akonlabs.com.
4. **5 deployment surfaces:** npm global CLI + npx ephemeral + browser (gitnexus.vercel.app) + Docker Compose + Kubernetes (Sigstore-signed). **1st Sigstore-signed Docker + K8s policy-controller** in corpus. Supply-chain posture = production-grade.
5. **16 MCP tools** — most MCP tools exposed per project in corpus. Per-repo: list_repos / query / context / impact / detect_changes / rename / cypher. Group: group_list / group_sync / group_contracts / group_query / group_status.
6. **5 AI editor integrations with explicit tier matrix** — Claude Code (full: MCP + Skills + Hooks PreToolUse+PostToolUse) / Cursor (MCP + Skills) / Codex (MCP + Skills) / Windsurf (MCP only) / OpenCode (MCP + Skills). Claude Code deepest integration.
7. **4 built-in agent skills:** Exploring / Debugging / Impact Analysis / Refactoring. Plus `--skills` flag for auto-generated repo-specific skills.
8. **LadybugDB embedded graph+vector database** — corpus-first. Native (CLI) + WASM (web) variants. Not attributed in README to author; appears in Acknowledgments.
9. **BM25 + semantic + Reciprocal Rank Fusion (RRF)** hybrid search — corpus-first. graphify v16 used graph-topology clustering without embeddings; GitNexus layers embeddings + classical search + re-ranking.
10. **Process-grouped search** — results grouped by execution-flow rather than flat file list. Novel UX primitive.
11. **Wiki auto-generation from knowledge graph** — LLM-powered extraction of documentation from graph structure. Distinct from graphify v16 Obsidian export (markdown files); GitNexus creates wiki pages inside browser UI.
12. **Browser ~5K file limit** — WebGPU + transformers.js + WASM LadybugDB runtime; beyond 5K files, use bridge mode (local server) or CLI.

## 3. Key features catalog

### Indexing + knowledge graph
- Tree-sitter AST parsing (native + WASM)
- Function / class / method / interface / import / export extraction
- Import + function-call resolution
- Inheritance/heritage tracking
- Constructor inference for `self`/`this` receiver types
- Named binding tracking (re-exports, aliases)
- Folder + file structure mapping
- Clustering via Leiden community detection (Graphology)
- Process tracing (entry points → call chains)
- Confidence scoring on relationships (3-level: EXTRACTED / INFERRED / AMBIGUOUS — inherited pattern from graphify v16)
- Embeddings for semantic search (transformers.js HuggingFace)

### 14 languages supported
TypeScript, JavaScript, Python, Java, Kotlin, C#, Go, Rust, PHP, Ruby, Swift, C, C++, Dart. Per-language capability matrix disclosed: all support imports/exports/hierarchy; some lack type annotations or constructor inference.

### Deployment modes (5)
| Mode | Scope | Privacy | Setup |
|------|-------|---------|-------|
| CLI + MCP (recommended) | Local machine | Everything local, no network | `npm install -g gitnexus` |
| npx ephemeral | Single command | Local | `npx gitnexus analyze` |
| Web UI (browser) | Browser session | In-browser, no server | gitnexus.vercel.app |
| Bridge mode | Local server + web UI | Local HTTP auto-detect | `gitnexus serve` |
| Docker Compose | Containers | Isolated | `docker compose up -d` |
| Kubernetes | Multi-pod cluster | Sigstore signed images + policy-controller | policy.yaml |

### 16 MCP tools
- **Per-repo:** list_repos / query / context / impact / detect_changes / rename / cypher
- **Groups:** group_list / group_sync / group_contracts / group_query / group_status
- Setup: `gitnexus setup` auto-configures MCP for supported editors

### Editor support (5)
| Editor | MCP | Skills | Hooks | Tier |
|--------|-----|--------|-------|------|
| Claude Code | ✓ | ✓ | ✓ (PreToolUse + PostToolUse) | Full |
| Cursor | ✓ | ✓ | — | MCP + Skills |
| Codex | ✓ | ✓ | — | MCP + Skills |
| Windsurf | ✓ | — | — | MCP only |
| OpenCode | ✓ | ✓ | — | MCP + Skills |

### Community integrations (third-party)
- `pi-gitnexus` by @tintinweb — pi.dev plugin
- `gitnexus-stable-ops` by @ShunsukeHayashi — Miyabi ecosystem deployments

## 4. Verbatim key claims

- *"Codebase indexing into knowledge graphs"* — primary function
- *"Every dependency, call chain, cluster, and execution flow"* — extraction scope
- *"Then exposes it through smart tools so AI agents never miss code"* — delivery mechanism
- *"When an editor makes changes, it doesn't know 47 functions depend on its return type — breaking changes ship"* — problem statement (paraphrased from README)
- *"Reliable, token-efficient"* — performance claim (quantitative token-efficiency benchmark NOT provided)

## 5. Supported languages capability matrix (from README table)

| Language | Imports | Exports | Hierarchy | Type Annotations | Constructor Inference |
|----------|---------|---------|-----------|------------------|----------------------|
| TypeScript | ✓ | ✓ | ✓ | ✓ | ✓ |
| JavaScript | ✓ | ✓ | ✓ | — | partial |
| Python | ✓ | ✓ | ✓ | ✓ | ✓ |
| Java | ✓ | ✓ | ✓ | ✓ | ✓ |
| Kotlin | ✓ | ✓ | ✓ | ✓ | partial |
| C# | ✓ | ✓ | ✓ | ✓ | ✓ |
| Go | ✓ | ✓ | ✓ | ✓ | — |
| Rust | ✓ | ✓ | ✓ | ✓ | ✓ |
| PHP | ✓ | ✓ | ✓ | partial | partial |
| Ruby | ✓ | ✓ | ✓ | — | — |
| Swift | ✓ | ✓ | ✓ | ✓ | ✓ |
| C | ✓ | ✓ | ✓ | ✓ | — |
| C++ | ✓ | ✓ | ✓ | ✓ | partial |
| Dart | ✓ | ✓ | ✓ | ✓ | ✓ |

**Most-detailed multi-language capability disclosure in corpus.**

## 6. Roadmap

**Actively Building:**
- LLM cluster enrichment (semantic naming of clusters)
- AST decorator detection (@Controller, @Get, etc.)
- Incremental indexing (changed files only)

**Recently Completed:**
- Constructor-inferred type resolution
- Wiki generation
- Multi-file rename
- Git-diff impact analysis
- Process-grouped search
- Claude Code hooks
- 14-language support
- Confidence scoring

## 7. Star history

Trendshift repository ID 19809; README links to star-history.com chart. Growth trajectory: 28K stars in 8.5 months = ~3,352 stars/month sustained-community-viral.

## 8. Cross-wiki observations

**Strongest peer:** [[graphify - Beginner Analysis]] v16 — both convert codebase/content into queryable knowledge graph. Differences:

| Axis | graphify v16 | GitNexus v33 |
|------|--------------|--------------|
| Runtime | Python-local (pip) | TypeScript-browser + CLI (npm) |
| Graph DB | NetworkX + graph-topology clustering | LadybugDB + embeddings |
| Search | Graph-topology (no embeddings) | BM25 + semantic + RRF hybrid |
| Agent platforms | 15+ (broadest) | 5 (narrower; Claude Code deepest) |
| Output | Obsidian markdown + MCP | Browser wiki + MCP + 16 tools |
| License | MIT | PolyForm Noncommercial 1.0.0 |
| Commercial | penpax.ai brand | akonlabs.com Enterprise |
| Inspiration | Karpathy /raw folder | "nervous system" metaphor |
| Author | safishamsi (solo-brand) | Abhigyan (CS student + akonlabs entity) |
| Scale | 30K (6 months) | 28.5K (8.5 months) |
| Confidence taxonomy | 3-level EXTRACTED/INFERRED/AMBIGUOUS | Confidence scoring (level-count not disclosed) |
| Languages | Tree-sitter 25 | Tree-sitter 14 (narrower, deeper capability matrix) |

**Pattern #18 Agent Runtime Standardization** (CONFIRMED v15; MCP layer added v31 mini-audit) — GitNexus is a MCP-runtime-standard consumer at 16-tool scale (most MCP tools exposed per corpus project). Validates Pattern #18 MCP universal-layer at T4 bridge role.

**Pattern #20 Solo-Scale Ceiling Dictionary** — NEW ROW: "Solo-student-at-T4 with commercial-company" = 28.5K/8.5mo. Previous T4 solo-scale data points: graphify 30K, crawl4ai 64K, TrendRadar 52K. GitNexus fits the T4 solo-scale range.

**Pattern #27 Community-Viral Scale Path** — 10th data point (post-v32 9 data points). GitNexus "sustained-community-viral 3.3K/mo" sub-path. Distinct from Reddit-single-viral (agency-agents) / Korean-community (OMC) / corporate-amplified (markitdown).

**Pattern #31 Open-Core Commercial Entity** (CONFIRMED v24, N=3 at v30) — **4th data point**: GitNexus OSS (PolyForm Noncommercial) + akonlabs.com Enterprise. Joins fish-speech (custom research license) + Skyvern (AGPL-3.0) + OpenHands (MIT with in-repo enterprise directory). **4 structurally-distinct open-core license approaches now observed** in corpus.

**Pattern #17 Ecosystem-Layer Organizations** — 10th data point (post-v32 9). Abhigyan is **NOT ecosystem-portfolio variant** (only 20 repos, most unrelated); he's **single-project-with-commercial-company variant**. Candidate new variant or narrow-scope refinement at next audit.

## 9. Absences detected (informative)

- **No i18n** — EN-only README. At 28.5K scale, absence of translation notable (contrast claude-howto v32 EN+VN+CN+UK at similar 28K scale; fish-speech v20 7-language at 29.8K; TrendRadar v19 bilingual CN+EN at 52K).
- **No Karpathy/John Lam/Boris Cherny lineage citation** — tool-lineage archetype (Tree-sitter + LadybugDB + Graphology + transformers.js + Sigma.js + MCP). Pattern #19 continuation.
- **No benchmark numbers** — claim "reliable, token-efficient" without quantitative benchmark (Pattern #8 absence at T4; contrast crawl4ai v29 OSS anti-bot quant, markitdown v28 processing metrics).
- **Narrow platform support (5)** — fewer than graphify v16 (15), spec-kit v17 (30+), agency-agents v18 (11). Claude Code primary focus.
- **No AGENTS.md mentioned** — CONTRIBUTING.md exists; AGENTS.md absence at T4 continues Pattern #22 narrow-scope refinement candidate (from v32 claude-howto counter-evidence observation).

## 10. Storm Bear applicability notes

- **Direct utility:** GitNexus browser mode can index Storm Bear vault (~32 wiki × ~10 files = ~320 files, well below 5K limit)
- **MCP integration:** Claude Code could query Storm Bear vault structure via GitNexus MCP server (novel — no prior wiki tool does this)
- **⚠️ PolyForm Noncommercial commercial-gate:** personal use for Scrum-coaching evaluation = clearly permitted; paid Scrum consulting practice = commercial use requiring akonlabs.com discussion
- **Operator decision point:** GitNexus alternative to graphify v16 pending on browser-vs-local preference + license-compatibility (graphify MIT unrestricted; GitNexus PolyForm commercial-gated)

## 11. Sources consulted (this cluster)

- `https://raw.githubusercontent.com/abhigyanpatwari/GitNexus/main/README.md` (primary)
- `https://api.github.com/repos/abhigyanpatwari/GitNexus` (metadata)
- `https://api.github.com/users/abhigyanpatwari` (author metadata)
- `https://gitnexus.vercel.app` (homepage — referenced, not deep-fetched)
- `https://www.npmjs.com/package/gitnexus` (referenced, not deep-fetched)

## 12. Next cluster — Contributor-governance

Verify CONTRIBUTING.md content (found — has AI-assisted-contributions section), SECURITY.md (not found; 404), LICENSE text, akonlabs.com commercial-tier feature description, Discord community signals.
