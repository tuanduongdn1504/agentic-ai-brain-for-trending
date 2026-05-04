# (C) Entity — GitNexus Core

> **Category:** Core product
> **Tier:** T4 Agent-as-bridge (7th entrant)
> **Wiki:** v33
> **Date:** 2026-04-23

---

## 1. One-line summary

GitNexus is a TypeScript-based codebase indexing tool that produces a queryable knowledge graph of every dependency, call chain, cluster, and execution flow, then exposes this graph to AI coding agents (Claude Code, Cursor, Codex, Windsurf, OpenCode) via 16 MCP tools, enabling architectural awareness that grep/search cannot provide.

## 2. Identifiers

- **Repo:** github.com/abhigyanpatwari/GitNexus
- **npm:** `gitnexus` (global CLI)
- **Homepage:** gitnexus.vercel.app (browser-native)
- **Commercial:** akonlabs.com (Enterprise SaaS + Self-hosted)
- **Discord (community):** discord.gg/MgJrmsqr62
- **Discord (commercial):** discord.gg/AAsRVT6fGb
- **License:** PolyForm Noncommercial 1.0.0
- **Created:** 2025-08-02
- **Stars:** 28,467 (as of 2026-04-23)
- **Forks:** 3,273 (11.5%)
- **Author:** Abhigyan Patwari (Guwahati, Assam, India)

## 3. Core value proposition

**Problem:** AI coding agents receive raw code snippets but lack architectural awareness. When an agent modifies a function, it doesn't know the 47 other functions depending on that function's return type. Breaking changes ship silently.

**Solution:** Precomputed knowledge graph of the codebase. Every dependency, import, call chain, cluster, and execution flow stored in LadybugDB (graph+vector). Agents query this graph via MCP tools before making changes, receiving architectural context.

**Metaphor:** *"Building nervous system for agent context."* Agents previously had raw text-level perception; GitNexus adds structural-level perception.

## 4. How it works (5-step flow)

1. **Install** — `npm install -g gitnexus` OR visit gitnexus.vercel.app OR `docker compose up -d`
2. **Index** — `gitnexus analyze <path>` parses codebase via tree-sitter, builds LadybugDB graph
3. **Configure** — `gitnexus setup` auto-configures MCP for 5 AI editors (Claude Code / Cursor / Codex / Windsurf / OpenCode)
4. **Query** — AI agent calls `query`, `context`, `impact`, `detect_changes`, `rename`, or `cypher` MCP tool with natural language or structured query
5. **Consume** — Agent receives process-grouped, RRF-ranked results with confidence scoring; makes informed decisions about edits / refactors / impacts

## 5. Technical architecture

### Parsing
- Tree-sitter (native CLI + WASM browser)
- 14 languages: TypeScript, JavaScript, Python, Java, Kotlin, C#, Go, Rust, PHP, Ruby, Swift, C, C++, Dart
- Extracts: functions, classes, methods, interfaces, imports, exports, inheritance, constructor-inferred types, named bindings (re-exports, aliases)

### Storage
- **LadybugDB** — embedded graph+vector database (native + WASM variants)
- **Graphology** — Leiden community-detection for clustering

### ML
- **transformers.js** (HuggingFace) for embeddings
- WebGPU in browser; GPU/CPU in CLI

### Search
- BM25 (keyword) + semantic (embeddings) + Reciprocal Rank Fusion (RRF)
- **Process-grouped output** (results organized by execution-flow)

### Frontend
- React 18 + TypeScript + Vite + Tailwind CSS v4
- Sigma.js (WebGL graph rendering)

### Agent layer
- MCP (stdio transport)
- LangChain ReAct (browser web-agent)
- Claude Code PreToolUse + PostToolUse hooks (EXCLUSIVE to Claude Code)

## 6. Novel primitives (corpus-first observations)

1. **Nervous-system philosophy framing** — agents have spatial-perception gap; knowledge graph fills it
2. **LadybugDB** — embedded graph+vector DB (corpus-first)
3. **BM25 + semantic + RRF hybrid search** — corpus-first
4. **Process-grouped search UX** — results grouped by execution-flow, not flat file list
5. **Multi-repo group operations** — 5 group MCP tools for cross-repo graph queries
6. **Sigstore + K8s policy-controller** — supply-chain-signed deployment (corpus-first)
7. **Wiki auto-generation from graph** — browser-native display (distinct from graphify v16 Obsidian export)
8. **16 MCP tools** — most per-project in corpus
9. **Claude Code bidirectional hooks** — PreToolUse + PostToolUse (corpus-first bidirectional)
10. **Per-language capability matrix** — 14 languages with type-annotation / constructor-inference disclosure (most detailed in corpus)
11. **Anti-crypto disclaimer at top** — corpus-first project leading with scam-denial
12. **Browser-native knowledge-graph runtime** — WASM tree-sitter + WASM LadybugDB + transformers.js + WebGPU

## 7. Scale + adoption signals

- **28,467 stars** (#11 in corpus; between HF agents-course 27,995 v26 and claude-howto 28,186 v32)
- **3,273 forks** (11.5% fork ratio — higher than median, indicates adoption)
- **305 open issues** (active)
- **97 subscribers** (lower than stars suggest — typical for quick-star projects)
- **~8.5 months old** (young)
- **~3,352 stars/month sustained-community-viral growth** (Pattern #27 9th data point extension — sustained-community-viral sub-path at ~3K/mo)
- **Community integrations:** `pi-gitnexus` (tintinweb) + `gitnexus-stable-ops` (ShunsukeHayashi Miyabi ecosystem)
- **Trendshift repository #19809** (trending signal)
- **Anti-impersonation evidence:** Pump.fun token impersonation — indicates meaningful reach (scammers target projects with audience)

## 8. Comparison with closest peer: graphify v16

| Axis | graphify v16 | GitNexus v33 |
|------|--------------|--------------|
| Core function | Code+docs+media → knowledge graph | Code → knowledge graph |
| Runtime | Python-local (pip) | TypeScript browser + CLI (npm) |
| Graph DB | NetworkX (no vector) | LadybugDB (graph+vector) |
| Search | Graph-topology clustering | BM25 + semantic + RRF hybrid |
| Agent platforms | 15+ (broadest) | 5 (narrower) |
| Hook integration | Claude Code skill only | Claude Code PreTool+PostTool bidirectional |
| License | MIT | PolyForm Noncommercial 1.0.0 |
| Commercial | penpax.ai (solo brand) | akonlabs.com (commercial entity) |
| Output | Obsidian markdown files | Browser wiki + MCP responses |
| Scale | 30K (6 mo) | 28.5K (8.5 mo) |
| Languages | Tree-sitter 25 (broad, shallow) | Tree-sitter 14 (narrower, deeper matrix) |
| Deployment | pip | npm + web + Docker + K8s Sigstore |
| Philosophy | "Karpathy /raw folder answer" | "Nervous system for agent context" |
| Author | safishamsi (solo-brand) | Abhigyan (CS student + akonlabs) |

**Complementary, not directly competitive:** graphify broader file types (papers, images, videos); GitNexus deeper code + browser-native + K8s-grade deployment.

## 9. Roadmap (active work)

- LLM cluster enrichment (semantic naming of clusters)
- AST decorator detection (@Controller, @Get, etc.)
- Incremental indexing (changed files only)

## 10. Limitations

- **Browser mode:** ~5,000 files (memory); larger → bridge or CLI
- **PolyForm Noncommercial license:** commercial use requires akonlabs.com agreement
- **Claim without benchmark:** "reliable, token-efficient" asserted without quantitative measurement (Pattern #8 absence at T4)
- **14 languages only** (OCaml is Enterprise-gated)
- **No SECURITY.md** — vulnerability-disclosure channel undocumented (inconsistent with Sigstore deployment sophistication)
- **Solo-student-author bus factor** — mitigated partially by commercial akonlabs entity

## 11. Cross-wiki references

- **Direct semantic peer:** [[graphify - Beginner Analysis]] v16 — Code → knowledge graph (Python-local)
- **T4 solo-enterprise peer:** [[crawl4ai - Beginner Analysis]] v29 — Web content crawler for LLM (64K stars at T4)
- **T4 utility peer:** [[markitdown - Beginner Analysis]] v28 — File → Markdown for LLM (Microsoft corporate at T4)
- **Open-core peer:** [[fish-speech - Beginner Analysis]] v20 — TTS foundation model (custom non-OSI research license)
- **MCP-consumer context:** [[awesome-mcp-servers - Beginner Analysis]] v31 — MCP directory at 85K
- **Pattern #70 VN analog:** [[claude-howto - Beginner Analysis]] v32 — VN-diaspora T1 (Pattern #70 VN-Regional-Archetype)

## 12. Pattern Library observations

- **Pattern #18 Agent Runtime Standardization (CONFIRMED v15, MCP-extended v31)** — 16 MCP tools = largest per-project adoption observed
- **Pattern #20 Solo-Scale Ceiling Dictionary (CONFIRMED v21)** — NEW ROW: Solo-student-at-T4-with-commercial-company 28.5K/8.5mo
- **Pattern #27 Community-Viral Scale Path (CONFIRMED v21)** — 10th data point; sustained-community-viral ~3.3K/mo
- **Pattern #19 Intellectual Lineage** — tool-lineage archetype (no individual-author citation)
- **Pattern #31 Open-Core Commercial Entity (CONFIRMED v24, N=3 at v30)** — **4TH DATA POINT** (PolyForm Noncommercial + akonlabs.com)
- **Pattern #17 Ecosystem-Layer Organizations (CONFIRMED v15, 5-variant table)** — Abhigyan single-flagship-project-with-commercial-entity variant (distinct from ecosystem-portfolio variant 1); potential new variant or narrow-scope refinement at next audit
- **Pattern #22 AGENTS.md (CONFIRMED v17)** — T4 absence (3rd at T4: GitNexus + claude-howto v32 + agency-agents v18 at T1)
- **Pattern #8 Research-Benchmark** — ABSENT at v33; no quantitative benchmark claim

## 13. Storm Bear operator relevance

**Direct utility (MEDIUM-HIGH):**
- Index Storm Bear vault (~320 files, well under 5K browser limit) — visualize cross-references
- MCP-enabled — Claude Code could query vault structure via GitNexus MCP server (novel workflow)
- Browser-native — no install friction if evaluating fit

**Commercial constraint (⚠️):**
- PolyForm Noncommercial 1.0.0 — commercial Scrum-coaching practice = commercial use
- Personal vault exploration = clearly permitted; paid client consulting = requires akonlabs.com agreement
- Operator decision: free personal use OR evaluate commercial licensing IF production adopting

**Recommendation (preliminary; full verdict in beginner guide Phase 4a):**
- **If operator wants vault knowledge-graph tool WITH commercial use compatibility:** graphify v16 (MIT, Python) — no license gate
- **If operator wants browser-native + MCP + personal exploration:** GitNexus — more sophisticated tech
- **If operator wants BOTH:** run graphify for production vault tooling; run GitNexus for personal exploration + commercial-compatibility evaluation
