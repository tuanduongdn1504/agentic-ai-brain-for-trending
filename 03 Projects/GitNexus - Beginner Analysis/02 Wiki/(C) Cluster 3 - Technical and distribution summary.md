# (C) Cluster 3 — Technical + Distribution summary

> **Sources:** Tech stack sections of README + package metadata + Docker/K8s/MCP integration docs + editor support matrix
> **Fetched:** 2026-04-23 via WebFetch
> **Role in wiki:** Technical architecture + MCP tool catalog + deployment details + language support depth + supply-chain architecture

---

## 1. Technical architecture

### Parsing layer
- **Tree-sitter** — AST parser
  - Native binding for CLI (faster)
  - WASM compilation for browser
- Extracts: functions, classes, methods, interfaces, imports, exports
- Resolves: import chains, function calls, inheritance/heritage, constructor inference for `self`/`this`, named bindings (re-exports, aliases)

### Knowledge-graph layer
- **LadybugDB** — embedded graph+vector database
  - Native variant for CLI
  - WASM variant for browser
  - **Corpus-first LadybugDB usage** (not in Acknowledgments attribution; appears to be the author's own project or lesser-known OSS)
- **Graphology** — JS graph library for clustering/community-detection
  - Leiden algorithm for cluster identification
  - Structure mapping (folder/file relationships → graph nodes/edges)
- **Process tracing** — execution-flow graphs from entry-points through call chains
- **Confidence scoring** — relationship confidence levels (level-count not disclosed; contrast graphify v16 explicit 3-level EXTRACTED/INFERRED/AMBIGUOUS)

### Machine-learning layer
- **transformers.js (HuggingFace)** — in-browser embeddings
  - WebGPU acceleration in browser
  - CPU/GPU in Node.js CLI
- Embedding model: not disclosed in README (likely default transformers.js small-model)
- Embeddings power semantic search (hybrid with BM25)

### Search layer
- **BM25** — classical information-retrieval algorithm (keyword-based)
- **Semantic** — embedding-based cosine similarity (via transformers.js vectors in LadybugDB)
- **Reciprocal Rank Fusion (RRF)** — re-ranking fusion of BM25 + semantic results
- **Process-grouped output** — results grouped by execution-flow rather than flat file list
- **Corpus-first hybrid search** (graphify v16 used pure graph-topology clustering without embeddings)

### Frontend layer
- **React 18** — UI framework
- **TypeScript** — primary language
- **Vite** — build tool
- **Tailwind CSS v4** — styling
- **Sigma.js** — WebGL graph rendering (node/edge visualization)

### Agent integration layer
- **MCP (Model Context Protocol)** — stdio transport for MCP servers
- **LangChain ReAct** — web-agent architecture for browser-resident AI interaction

## 2. 16 MCP tools (complete catalog)

### Per-repo tools (7)
| Tool | Purpose |
|------|---------|
| `list_repos` | Enumerate indexed repositories in global registry |
| `query` | Execute query against knowledge graph (natural language or structured) |
| `context` | Fetch agent context for a file/function/class |
| `impact` | Analyze blast radius of proposed change |
| `detect_changes` | Git-diff → affected processes mapping |
| `rename` | Multi-file coordinated rename across call chains |
| `cypher` | Raw Cypher query against graph DB (power-user) |

### Group tools (5 — multi-repo operations)
| Tool | Purpose |
|------|---------|
| `group_list` | List repository groups (collections of indexed repos) |
| `group_sync` | Sync all repos in group with latest git state |
| `group_contracts` | Identify contract-boundaries between repos in group (API surfaces) |
| `group_query` | Cross-repo query spanning group |
| `group_status` | Group-level health/indexing state |

**4 additional tools** — context/resources/prompts/skills (README details less specific; 16 total confirmed)

**Significance:** 16 MCP tools = **most tools exposed per project in corpus**. Validates Pattern #18 MCP-runtime-standard consumer at T4 bridge role.

## 3. Installation matrix

| Method | Command | Platform | Prerequisites |
|--------|---------|----------|---------------|
| Global CLI | `npm install -g gitnexus` | macOS / Linux / Windows (Node.js 20+) | Node.js |
| Ephemeral | `npx gitnexus analyze` | Same | Node.js |
| Browser | Visit gitnexus.vercel.app | Any modern browser w/ WebGPU | WebGPU-capable browser |
| Docker Compose | `docker compose up -d` | Docker engine | Docker + Docker Compose |
| Kubernetes | `kubectl apply -f ...` | K8s cluster | K8s 1.24+ + Sigstore policy-controller (optional but recommended) |
| Local dev | `git clone` + `npm install` | Dev machine | Full Node toolchain |

**Setup command:** `gitnexus setup` auto-configures MCP for supported editors (Claude Code / Cursor / Codex / Windsurf / OpenCode). Writes `.claude/settings.json` + `.cursor/mcp.json` + equivalents.

## 4. 14-language support detail

### All 14 languages support
- Imports
- Exports
- Hierarchy (inheritance / composition)

### Type-annotation support
- **Full:** TypeScript, Python, Java, Kotlin, C#, Go, Rust, Swift, C, C++, Dart (11)
- **Partial:** PHP (3)
- **Absent:** JavaScript, Ruby (2)

### Constructor-inference support
- **Full:** TypeScript, Python, Java, C#, Rust, Swift, Dart (7)
- **Partial:** JavaScript, Kotlin, PHP, C++ (4)
- **Absent:** Go, Ruby, C (3)

**Observation:** Go + C lack constructor inference (language design: no classical constructors — Go has `NewX` factory; C has initializers). Ruby lacks type-annotation support (dynamic typing + duck-typing idioms).

**OCaml** — NOT in OSS 14 languages; IS in akonlabs.com Enterprise tier. Language-gate is commercial differentiator.

## 5. Deployment deep-dive

### CLI + MCP (recommended by README)
- **Privacy:** Everything local; no network calls except optional LLM for wiki generation
- **Performance:** Native tree-sitter bindings + native LadybugDB = fastest
- **Limits:** None explicitly documented (file count unbounded)
- **Use case:** primary developer workflow

### Web UI (browser)
- **Privacy:** In-browser, no server; user drags ZIP or connects GitHub
- **Performance:** WASM + WebGPU — slower than native but respectable
- **Limits:** ~5,000 files (browser memory); larger → bridge mode or CLI
- **Use case:** quick exploration; demo; non-developer audiences

### Bridge mode (`gitnexus serve`)
- **Privacy:** Local HTTP server (127.0.0.1) + browser UI
- **Performance:** Native backend + WASM frontend = fast + visual
- **Limits:** None (backend is CLI)
- **Use case:** developer wants visual UI without browser's memory limits

### Docker Compose
- **Privacy:** Container isolation
- **Includes:** server + UI bundled
- **Use case:** team deployment; CI/CD integration

### Kubernetes with Sigstore
- **Security:** Docker images signed with Cosign keyless; K8s policy-controller enforces signature verification
- **Supply-chain:** corpus-first explicit K8s policy-controller deployment
- **Use case:** production multi-tenant deployment; regulated environment

## 6. Editor support detail

### Claude Code (Full integration)
- **MCP:** 16 tools auto-configured via `gitnexus setup`
- **Skills:** 4 built-in (Exploring / Debugging / Impact Analysis / Refactoring) + `--skills` flag for auto-generated repo-specific skills
- **Hooks:** PreToolUse (before Claude Code executes a tool, fetch GitNexus context) + PostToolUse (after execution, update graph if changed)
- **Integration depth:** HIGHEST in corpus T4 category — deeper than graphify v16 Claude Code skill

### Cursor
- **MCP:** Yes (`.cursor/mcp.json` auto-configured)
- **Skills:** Yes (Cursor has skill system)
- **Hooks:** No (Cursor doesn't support pre/post hooks like Claude Code)

### Codex (OpenAI)
- **MCP:** Yes
- **Skills:** Yes
- **Hooks:** No

### Windsurf
- **MCP:** Yes (only)
- **Skills:** No
- **Hooks:** No

### OpenCode
- **MCP:** Yes
- **Skills:** Yes
- **Hooks:** No

**Total editors supported: 5** (Claude Code + Cursor + Codex + Windsurf + OpenCode) — narrower than graphify v16 (15) but DEEPER in Claude Code-specific integration (hooks exclusive to Claude Code).

## 7. Wiki generation capability

- **Mechanism:** LLM-powered documentation extraction from knowledge graph
- **Output:** Browser-displayed wiki (not markdown files — in contrast to graphify v16 Obsidian export)
- **Use case:** understand unfamiliar codebase via auto-generated wiki
- **LLM:** not specified; likely configurable (claude / gpt / local)
- **First corpus "wiki-from-graph" generator with browser-native display**

## 8. Supply-chain architecture (detailed)

### Sigstore integration
- **Docker images signed with Cosign keyless** (no static signing keys to manage)
- **Verified via Sigstore public transparency log** (Rekor)
- **Documented in README** as standard deployment path
- **Corpus-first Sigstore mention at T4**

### Kubernetes policy-controller
- **Cosign policy controller** (sigstore.dev/policy-controller) — K8s admission controller
- **Only signed images admitted** to cluster
- **Regulated deployment ready** (finance / healthcare / government use cases)
- **Corpus-first K8s policy-controller enforcement documented**

### Threat model implications
- **Image-tampering defense:** attacker cannot substitute malicious image for signed release
- **Transitive-trust:** dependencies (Tree-sitter + LadybugDB + Graphology + transformers.js + Sigma.js) still rely on npm/pip ecosystem trust (no explicit lockfile signing)

### Contrast with corpus supply-chain observations
- **crawl4ai v29** — `unclecode-litellm` fork (Pattern #66 OBSERVATION-TRACK): reactive incident response
- **GitNexus v33** — proactive infrastructure-level signing: Sigstore + K8s enforcement
- **Observation:** corpus now has 2 distinct supply-chain postures documented

## 9. Multi-repo architecture (group operations)

- **Global MCP registry** enables one MCP server to serve multiple indexed codebases
- **Groups** = collections of related repos (e.g., micro-services in an org)
- **`group_contracts`** tool — identifies API-surface boundaries between repos (contract testing)
- **`group_query`** — spans cross-repo queries (e.g., "which repo owns user authentication?")
- **`group_sync`** — batch-sync all repos in group with git HEAD

**Novel primitive** — corpus-first cross-repo-graph-operation primitive (graphify v16 is single-repo; crawl4ai v29 is web-content; markitdown v28 is single-doc).

## 10. LadybugDB significance

- **Embedded graph+vector DB** — graph structure + vector similarity in single DB
- **Native + WASM runtime variants** — runs in browser or Node.js
- **In Acknowledgments** without origin attribution in README; likely lesser-known OSS or author-adjacent project
- **Corpus-first usage:**
  - graphify v16 used NetworkX (Python graph lib) — no embeddings, graph-topology clustering
  - awesome-mcp-servers v31 — no graph DB (directory only)
  - pgvector (PostgreSQL extension) in multica v15 — relational+vector, not graph+vector
- **Technical distinction:** graph queries + vector similarity in single embedded DB = simpler stack than typical "Neo4j + pinecone" or "NetworkX + separate vector DB"

## 11. Process-grouped search primitive

- **Traditional search:** flat list of file matches
- **GitNexus search:** results grouped by execution-flow (process)
- **Example:** search "authentication" returns grouped by which call chain (signup flow / login flow / OAuth flow)
- **Novel UX primitive** — corpus-first
- **Agent value:** AI agents receive structurally-organized results rather than flat list

## 12. Roadmap + active development

**Actively building (per README):**
- **LLM cluster enrichment** — automated semantic naming of discovered clusters (currently unnamed clusters; LLM will label them)
- **AST decorator detection** — recognize framework decorators (@Controller, @Get, etc.) as semantic markers
- **Incremental indexing** — changed-files-only re-index (vs. current full re-index)

**Recently completed (per README):**
- Constructor-inferred type resolution
- Wiki generation
- Multi-file rename
- Git-diff impact analysis
- Process-grouped search
- Claude Code hooks
- 14-language support
- Confidence scoring

## 13. Cross-wiki technical observations

**Pattern #18 Agent Runtime Standardization (CONFIRMED v15, MCP-layer extended v31)** — GitNexus exposes 16 MCP tools = most MCP tools per project in corpus. Strong data point for MCP-as-runtime-standard Layer 1.

**Pattern #8 Research-Benchmark Emergence** — ABSENT at v33; "reliable, token-efficient" claim without quantitative benchmark. Narrow-scope refinement: T4 tools underspecify quantitative claims.

**Pattern #20 Solo-Scale Ceiling Dictionary** — NEW ROW: "Solo-student + commercial-company at T4 = 28.5K/8.5mo". Fits dictionary.

**Pattern #27 Community-Viral Scale Path** — 10th data point. Sustained-community-viral ~3.3K/mo sub-path continues.

**Pattern #19 Intellectual Lineage** — tool-lineage continuation (no individual-author citation). Archetype 4 (no-lineage at agency-agents v18) strengthens.

## 14. Novel corpus-first observations tally (v33)

1. PolyForm Noncommercial 1.0.0 — 1st standardized non-OSI commercial-gate license
2. LadybugDB — 1st embedded graph+vector DB in corpus
3. BM25 + semantic + RRF hybrid search — 1st in corpus
4. Sigstore-signed Docker — 1st supply-chain-signed deployment
5. K8s policy-controller enforcement — 1st K8s admission-control documented
6. 16 MCP tools — most per project
7. Process-grouped search UX primitive — 1st
8. Multi-repo group operations — 1st cross-repo graph operations
9. Anti-crypto disclaimer at top — 1st corpus project leading with scam-denial
10. Indian-authored framework — 1st corpus (Guwahati, Assam)
11. CS-student archetype — 1st (distinct from Pattern #44 academic-lab faculty)
12. Tool-lineage archetype continuation — no individual-author citation; depends on Tree-sitter + LadybugDB + Graphology + transformers.js + Sigma.js + MCP
13. Claude Code Hooks PreToolUse + PostToolUse — 1st explicit bidirectional-hook integration in corpus
14. Wiki-from-graph browser-native display — distinct from graphify v16 Obsidian export

## 15. Cross-wiki siblings (reference)

**Primary:** graphify v16 (direct semantic peer); crawl4ai v29 (T4 solo-enterprise peer); markitdown v28 (T4 utility peer); fish-speech v20 (open-core peer)

**Technical-architecture peers:**
- **graphify v16:** knowledge-graph-for-Claude-Code-skill; Python-local; NetworkX
- **crawl4ai v29:** web-content-for-AI; Python CLI+browser; Playwright+Chromium
- **markitdown v28:** file→markdown-for-LLM; Python+CLI+Docker; Microsoft corporate
- **GitNexus v33:** codebase→graph-for-agent; TypeScript+browser+K8s; LadybugDB+MCP-16-tools

## 16. Source consulted

- `https://raw.githubusercontent.com/abhigyanpatwari/GitNexus/main/README.md` (technical sections)
- `https://raw.githubusercontent.com/abhigyanpatwari/GitNexus/main/CONTRIBUTING.md`
- `https://raw.githubusercontent.com/abhigyanpatwari/GitNexus/main/SECURITY.md` (404 — absent)
- `https://polyformproject.org/licenses/noncommercial/1.0.0/` (license text)
- `https://api.github.com/repos/abhigyanpatwari/GitNexus` (metadata)

## 17. Phase 3 — Entity page selection

Based on 3 clusters, selected 4 entities for Phase 3:

1. **(C) GitNexus Core** — codebase→knowledge-graph product; 13-section format
2. **(C) MCP Integration Layer (16 tools + 5 editors)** — agent integration architecture
3. **(C) Open-Core Structure with PolyForm Noncommercial** — commercial-gate + akonlabs.com (Pattern #31 N=4 data point, Pattern #72 new candidate anchor)
4. **(C) Storm Bear Meta — GitNexus for vault knowledge-graph** — 22nd consecutive meta-entity; vault-indexing applicability
