# (C) Entity 1 — Core Product (claude-context MCP)

> **Entity type:** Product / core subject of v40 wiki
> **Scope:** `zilliztech/claude-context` top-level product architecture — hybrid BM25+dense-vector semantic code search via MCP protocol for AI coding agents
> **Pattern relevance:** Pattern #18 Layer 1 MCP-native / Pattern #28 Multi-Provider AI Support 8th data point / Pattern #8 Research-Benchmark 9th data point / Pattern #2 Distribution Evolution

---

## 1. Identity (verbatim)

- **Name:** Claude Context
- **Repo description (GitHub):** *"Code search MCP for Claude Code. Make entire codebase the context for any coding agent."*
- **README hero:** *"Your entire codebase as Claude's context"*
- **Author:** Cheney Zhang (`277584121@qq.com`) — Zilliz engineer, CN-origin (QQ email)
- **Org:** Zilliz (commercial-startup; parent of Milvus vector DB)
- **License:** MIT (permissive)
- **Version:** 0.1.7 (early; 168 commits; active)
- **Stars / Forks:** 8.6K / 670 (7.8% fork ratio — moderate)

---

## 2. Core value proposition

### Cost-reduction positioning (verbatim)

> *"Instead of loading entire directories into Claude for every request, which can be very expensive, Claude Context efficiently stores your codebase in a vector database and only uses related code in context to keep your costs manageable."*

**Corpus-first at T4:** Commercial-pragmatic positioning leads with COST not capability. Prior T4 entrants (graphify v16 *"knowledge graph"* / GitNexus v33 *"nervous system"* / markitdown v28 *"file conversion"* / crawl4ai v29 *"LLM-friendly crawler"*) positioned around capability or metaphor. claude-context positions around **dollar-denominated operational cost reduction**.

### Measurable gain (from evaluation)

- **-39.4% token usage** (73,373 → 44,449 on SWE-bench Verified subset)
- **-36.3% tool calls** (8.3 → 5.3)
- **F1 preserved at 0.40** (retrieval quality unchanged)

---

## 3. Architecture (4-layer stack)

### Layer 1 — Protocol: MCP (Model Context Protocol)

**Primary distribution:** MCP server `@zilliz/claude-context-mcp` on npm. Agent invokes MCP tools; framework doesn't need direct API.

**4 MCP tools exposed:**

| # | Tool | Signature (natural-language) | Lifecycle phase |
|---|------|-------------------------------|-----------------|
| 1 | `index_codebase` | Build hybrid BM25 + dense vector index | Write |
| 2 | `search_code` | Natural-language query → ranked results | Read |
| 3 | `clear_index` | Clear index for a codebase | Delete |
| 4 | `get_indexing_status` | Progress % / completion status | Observe |

**Novel corpus observation:** **Indexing lifecycle exposed as explicit MCP tool surface.** Competitors typically bundle indexing behind auto-invoke; claude-context exposes index/search/clear/status as first-class agent-invokable tools. Gives agent explicit control over indexing state.

### Layer 2 — Retrieval: Hybrid search

- **BM25** — classical keyword TF-IDF retrieval
- **Dense vector** — embedding-based semantic retrieval
- **Fusion** — results combined from both retrievers

**Why hybrid?** BM25 alone misses semantic connections (e.g., "auth handler" won't match `validateUser()` variable name). Dense vector alone loses exact-name-match precision. Hybrid captures both signal types.

**Peer comparison:**
- graphify v16: graph-topology + semantic similarity (no BM25)
- GitNexus v33: BM25 + semantic + RRF (Reciprocal Rank Fusion) — same hybrid genre
- claude-context v40: BM25 + dense vector (RRF not confirmed but likely similar)

### Layer 3 — Chunking: AST-based (Tree-sitter) with character-based fallback

**Primary:** **AST-based (syntax-aware)** — parses code through Tree-sitter grammars to chunk at semantic boundaries (function / class / module). Preserves code structure integrity in chunks.

**Fallback:** **LangChain character-based** — fixed-size chunks (1000 chars default) with 200-char overlap. Used for: (a) languages without Tree-sitter grammar, (b) files exceeding AST parser capability, (c) non-code content (markdown).

**Defaults:**
- Chunk size: 1000 characters
- Chunk overlap: 200 characters
- Splitter preference: AST (recommended)

**14 languages with AST-based support:**
TypeScript, JavaScript, Python, Java, C++, C#, Go, Rust, PHP, Ruby, Swift, Kotlin, Scala, Markdown

**Pattern #28 Multi-Provider AI Support 8th data point:** language-grammar-provider diversity (14 Tree-sitter grammars) = provider abstraction at parser-layer.

### Layer 4 — Storage: Vector database

**2 backends supported:**
- **Milvus** (self-hosted) — open-source vector DB, full control
- **Zilliz Cloud** (managed SaaS) — Zilliz commercial tier with free Serverless start

**Why 2-tier?**
- OSS developers can use Milvus self-hosted (no commercial lock-in)
- Production users get managed Zilliz Cloud scale + SLA (commercial funnel)

**Pattern #50 Commercial-Funnel Companion Platform N=3 default-criterion:** Zilliz Cloud IS the commercial funnel for claude-context OSS. First T4 data point for #50.

### Novel architectural primitive: Merkle-tree incremental indexing

**From README (verbatim):** *"Efficiently re-index only changed files using Merkle trees."*

**Mechanism (inferred from `packages/core/src/snapshot.ts` size = 24.2K):**
1. Build content-addressable hash tree over codebase
2. Compute tree hash per subtree (file / directory / root)
3. On re-index, walk tree; if subtree hash unchanged, skip re-embedding
4. Propagate changes bottom-up; only hash-changed subtrees trigger re-embed

**CORPUS-FIRST:** No prior wiki uses Merkle-tree for incremental indexing. graphify v16 uses full rebuild. GitNexus v33 uses LadybugDB diff detection. markitdown v28 is stateless. claude-context v40's Merkle-tree = novel incremental-indexing primitive.

---

## 4. 4 embedding providers (Pattern #28 data point)

| # | Provider | Default model | Specialization | Local/Remote |
|---|----------|---------------|----------------|--------------|
| 1 | **OpenAI** (default) | `text-embedding-3-small` | General-purpose | Remote API |
| 2 | **VoyageAI** | `voyage-code-3` | **Specialized for code** | Remote API |
| 3 | **Gemini** | `gemini-embedding-001` | Multilingual | Remote API |
| 4 | **Ollama** | `nomic-embed-text` | Local/self-hosted | **Local** |

**Provider-quality tradeoff:**
- OpenAI: commercial accessibility, baseline quality
- VoyageAI `voyage-code-3`: purpose-built for code, higher quality for code-retrieval tasks
- Gemini: multilingual support signal (but README says "good multilingual support" — implies natural language, not code multilingualism)
- Ollama: privacy (local embedding; nothing sent to external providers)

**Provider-abstraction style:** claude-context uses **switch-by-env-var** (`EMBEDDING_PROVIDER=OpenAI|VoyageAI|Gemini|Ollama`) + per-provider env overrides. Distinct from LiteLLM-style (crawl4ai v29) provider-abstraction-library. claude-context's abstraction is internal implementation, not library-consumer-oriented.

---

## 5. 3 distribution surfaces (Pattern #2 Distribution Evolution strengthening)

### Surface 1: MCP server (`@zilliz/claude-context-mcp`)

**Primary distribution. Recommended for AI coding agents.**

```bash
claude mcp add claude-context \
  -e OPENAI_API_KEY=sk-... \
  -e MILVUS_ADDRESS=... \
  -e MILVUS_TOKEN=... \
  -- npx @zilliz/claude-context-mcp@latest
```

**12+ documented MCP clients** (broadest T4 MCP-client support):
- Claude Code / OpenAI Codex / Gemini / Qwen / Cursor / Void / Claude Desktop / Windsurf / VS Code (generic) / Cherry Studio / Cline / Augment / Roo Code / Zencoder / LangChain-LangGraph

### Surface 2: Core library (`@zilliz/claude-context-core`)

**For custom integrations.**

```typescript
import { Context, MilvusVectorDatabase, OpenAIEmbedding } from '@zilliz/claude-context-core';
const context = new Context({ embedding, vectorDatabase });
await context.indexCodebase('./your-project', (progress) => { ... });
const results = await context.semanticSearch('./your-project', 'vector database operations', 5);
```

### Surface 3: VS Code extension (`zilliz.semanticcodesearch`)

IDE-integrated semantic search UI. Configure via VS Code Settings. Useful for developers who don't use AI coding agents but want semantic search.

### Surface 4: Chrome Extension (Coming Soon)

Browser extension for GitHub code search. "Coming Soon" on Chrome Web Store; active development per `packages/chrome-extension/CONTRIBUTING.md` 7.1K size (largest per-package CONTRIBUTING).

**Surface-audience mapping:**
- MCP → AI coding agent audience (primary)
- Core library → custom SDK consumer (secondary)
- VS Code → IDE-native developer audience (secondary)
- Chrome Extension → GitHub browser code-search audience (emerging)

---

## 6. Configuration surface

**Environment variables (key-value):**
- `OPENAI_API_KEY` / `VOYAGEAI_API_KEY` / `GEMINI_API_KEY` + `OLLAMA_HOST`
- `MILVUS_ADDRESS` + `MILVUS_TOKEN`
- `EMBEDDING_PROVIDER` + `EMBEDDING_MODEL`
- Base URL overrides (`OPENAI_BASE_URL` / `GEMINI_BASE_URL`)

**Per-client MCP config:** each of 12+ clients has config-path differences documented (CLI / TOML / JSON / UI).

**VS Code extension Settings UI:** embedding provider + model + API key + splitter type + chunk size/overlap + Milvus connection

**Chunk configuration:**
- `Splitter Type`: AST (recommended) OR LangChain
- `Chunk Size`: 1000 chars (default)
- `Chunk Overlap`: 200 chars (default)

**File inclusion/exclusion:** documented in `docs/dive-deep/file-inclusion-rules.md` (not probed in detail; standard glob patterns + ignore-file support expected).

---

## 7. Empirical evaluation (Pattern #8 9th data point)

### Dataset

**30 instances** from **Princeton NLP SWE-bench Verified** (filtered for 15-60 min difficulty + 2 file modifications). Generation script `generate_subset_json.py` reproducible.

### Experimental design

- **Framework:** LangGraph MCP + ReAct
- **Model:** GPT-4o-mini (cost-fixed variable)
- **Replicates:** 3 per method × 2 methods = 6 runs
- **Baseline:** grep + read + edit
- **Treatment:** grep + read + edit + claude-context MCP

### Results (verbatim table)

| Metric | Baseline | + claude-context | Improvement |
|--------|----------|------------------|-------------|
| F1-Score | 0.40 | 0.40 | Comparable |
| Token Usage | 73,373 | 44,449 | **-39.4%** |
| Tool Calls | 8.3 | 5.3 | **-36.3%** |

### Positioning in Pattern #8 rigor hierarchy

1. **Marketing-claim tier:** graphify v16 (71.5× token reduction), spec-kit v17 (48× productivity)
2. **Intermediate empirical tier:** **claude-context v40** — structured experiment + replicates + published methodology, not peer-reviewed
3. **Peer-reviewed tier:** LlamaFactory v22 (ACL 2024), OpenHands v30 (NeurIPS/ICLR)

---

## 8. Tech stack summary

| Layer | Technology | Role |
|-------|-----------|------|
| **Protocol** | MCP (Model Context Protocol) | Agent integration |
| **Retrieval** | BM25 + dense vector hybrid | Semantic code search |
| **Chunking** | Tree-sitter AST + LangChain char fallback | Code-aware splitting |
| **Embedding** | OpenAI / VoyageAI / Gemini / Ollama | Vector generation |
| **Storage** | Milvus / Zilliz Cloud | Vector DB |
| **Incremental** | Merkle trees | Efficient re-indexing |
| **Language** | TypeScript 69.5% + Python 15.2% | Implementation |
| **Package manager** | pnpm workspaces (monorepo) | Build + release |
| **Distribution** | npm + VS Code Marketplace + Chrome Ext (coming) | User surfaces |

---

## 9. Storm Bear applicability (direct pilot candidate)

**Pilot relevance: HIGH-MEDIUM (#4-5 ranking candidate)**

### Direct use case: Index Storm Bear vault

Storm Bear vault contains 40 wikis × ~600 lines average ≈ 24K lines of markdown + CLAUDE.md + GOALS.md + PATTERN_LIBRARY.md.

**claude-context handles markdown** (14th supported language). Semantic search across 40 wikis for queries like:
- *"Find wikis discussing Pattern #18 MCP Layer 1 triple-layer formulation"*
- *"Which T4 wikis mention Merkle-tree or graph-based incremental indexing?"*
- *"Show me all corpus-firsts across wikis"*

### Friction points

1. **Zilliz Cloud free tier limits** — need to check if sufficient for 24K lines (likely yes)
2. **Embedding cost** — OpenAI `text-embedding-3-small` ~$0.02/1M tokens; 24K lines × ~10 tokens/line avg ≈ 240K tokens ≈ $0.005 full index
3. **VN language** — embedding may be Tier-2 quality for VN vs EN; needs empirical test
4. **Merkle-tree incremental** — after first index, re-runs only hash-changed files (fast)

### Alternative: graphify v16 (graph-based)

Graphify would surface **entity relationships** (wikis citing wikis, patterns strengthening patterns). claude-context would surface **semantic similarity** (which wikis talk about same concept).

**Both have value; different retrieval modalities.** Storm Bear could run both for vault as pilot — graph for structural navigation, vector for semantic-query-by-natural-language.

**Pilot recommendation:** 30-minute trial — install claude-context MCP + index vault + ask 5 natural-language queries. Compare quality to current Grep-based search.

---

## 10. Cross-references

- **graphify v16** — T4c graph-based code indexing; **primary sibling** for code-indexing sub-taxonomy
- **GitNexus v33** — T4g graph-based code indexing + commercial; **secondary sibling**
- **awesome-mcp-servers v31** — MCP directory; claude-context candidate for listing
- **markitdown v28** — T4e corporate-narrow-utility; sibling Microsoft vs Zilliz corporate narrow-utility comparison
- **OpenHands v30** — T5 Agent-as-application; shared SWE-bench Verified substrate
- **multica v15** + **graphify v16** + **spec-kit v17** — prior MCP-consuming wikis; claude-context extends MCP consumer base
- **Pattern #18 triple-layer** — Layer 1 MCP-native 15th+ strengthening
- **Pattern #28 Multi-Provider AI Support** — 8th data point
- **Pattern #50 Commercial-Funnel** — N=3 default-criterion first T4
- **Pattern #8 Research-Benchmark** — 9th data point

---

## 11. Open questions

Parked to `01 Analysis/(C) open questions.md`:
- Merkle-tree incremental indexing — prior art?
- Chunk size 1000/overlap 200 — empirical tuning source?
- OpenAI default vs VoyageAI-code-3 — accessibility-over-quality tradeoff rationale?
- Chrome Extension timeline?

---

## 12. Confidence + versioning

**Version at wiki build:** 0.1.7 (early; rapid iteration expected)

**Evidence confidence:** High — all claims sourced from README + per-package READMEs + evaluation/README.md + source-tree inspection. No fabrications. Cheney Zhang's QQ email is CN-origin signal but nationality not directly stated.

**Forward stability:** Medium — at v0.1.7, API + tool surface may evolve. Merkle-tree implementation may refine. Chrome Extension shipping will add surface.

---

## 13. Summary

claude-context = **MCP-primary semantic code search for AI coding agents**, with **hybrid BM25+dense-vector retrieval**, **Tree-sitter AST chunking + LangChain fallback**, **4 embedding providers (OpenAI+VoyageAI+Gemini+Ollama)**, **2 vector DBs (Milvus+Zilliz Cloud)**, and **novel Merkle-tree incremental indexing** (corpus-first). **4-surface distribution** (MCP + Core library + VS Code + Chrome Ext coming). **12+ MCP clients** documented (broadest T4). **Empirical evaluation with SWE-bench Verified subset** (Pattern #8 9th data point) demonstrates -39.4% tokens at equivalent F1. **Commercial funnel via Zilliz Cloud** (Pattern #50 N=3 first T4). **Cost-reduction-first positioning** (corpus-first T4 framing). **Author:** Cheney Zhang, Zilliz engineer. **License:** MIT.
