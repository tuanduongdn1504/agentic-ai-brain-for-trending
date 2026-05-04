# (C) claude-context — Hướng dẫn cho người mới / Beginner Guide (VN+EN Bilingual)

> **Target:** `zilliztech/claude-context` — MCP plugin thêm semantic code search vào Claude Code và các AI coding agent khác
> **Audience:** Storm Bear operator + VN developer community làm AI-assisted development
> **Wiki reference:** v40 in Storm Bear corpus (40-wiki milestone; 8TH T4 entrant; 3rd code-indexing T4)

---

## Phần 1 / Part 1 — What is claude-context?

**VN:** claude-context là một **MCP plugin** (Model Context Protocol) giúp Claude Code và các AI coding agent khác (Cursor / Codex / Cline / Windsurf / Gemini / 12+ tools) thực hiện **semantic code search** trên toàn bộ codebase của bạn — thay vì phải load nguyên thư mục source code vào context mỗi lần, claude-context index codebase thành vector database và chỉ pull các đoạn code liên quan.

**EN:** claude-context is an MCP plugin that adds **semantic code search** to Claude Code and other AI coding agents (12+ clients). Instead of loading entire directories into Claude context on every request (very expensive), it indexes your codebase into a vector database and retrieves only semantically-relevant snippets.

**Tại sao quan trọng / Why it matters:**
- **Cost reduction:** -39.4% token usage (measured via SWE-bench Verified subset)
- **Tool call reduction:** -36.3% tool calls
- **F1 preserved:** 0.40 (same retrieval quality as grep baseline)

**Ai làm / Author:** Cheney Zhang ([Zilliz](https://zilliz.com) engineer) + Zilliz team (commercial-startup; parent của Milvus vector DB)

**License:** MIT — tự do dùng commercial + modify + distribute

---

## Phần 2 / Part 2 — Corpus-first signals (v40 milestone)

Theo phân tích Storm Bear corpus, claude-context v40 có **10+ corpus-first signals**:

1. **Cost-first README positioning** tại T4 (commercial-pragmatic framing)
2. **Merkle-tree incremental indexing** (corpus-first incremental-indexing architecture)
3. **12+ MCP client configs documented** (broadest MCP-client documentation tại T4)
4. **4 MCP tools exposed** cho toàn bộ indexing lifecycle (index / search / clear / status)
5. **SWE-bench Verified subset methodology tại T4** (2nd corpus SWE-bench use sau OpenHands v30)
6. **Commercial-startup ecosystem variant 3 strengthening** (8+ Zilliz products)
7. **First T4 data point cho Pattern #50 Commercial-Funnel** (N=3 default-criterion)
8. **UTM-tracked commercial funnel instrumentation** (`2507-codecontext-readme` campaign)
9. **Tree-sitter AST chunking cross-wiki convergence** (3 code-indexing T4 use Tree-sitter)
10. **DeepWiki AI-docs integration** (2nd corpus use sau claude-code-best-practice v34)

---

## Phần 3 / Part 3 — Vị trí trong taxonomy

**Tier:** T4 Agent-as-bridge (Bridge tier — kết nối external resource sang AI agent)

**Archetype:** **NEW T4h Commercial-Ecosystem-Startup with Vector-Search Code-Indexing** — 8th T4 archetype observed

### So sánh với T4 peers

| Archetype | Wiki | Stars | Approach |
|-----------|------|-------|----------|
| T4a Corporate-broad-official | gws v13 | 25K | Google Workspace API |
| T4b Solo-narrow | notebooklm-py v7 | ~300 | NotebookLM wrapper |
| T4c Solo-broad-local | graphify v16 | 30K | **Graph-based** code indexing |
| T4d Solo-broad-external-regional | TrendRadar v19 | 52K | CN news aggregator |
| T4e Corporate-narrow-utility | markitdown v28 | 114K | Microsoft file conversion |
| T4f Solo-enterprise-scale | crawl4ai v29 | 64K | Web crawler |
| T4g Solo-student-with-commercial | GitNexus v33 | 28.5K | **Graph-based + commercial** |
| **T4h Commercial-ecosystem-startup 🆕** | **claude-context v40** | **8.6K** | **Vector-based + Zilliz commercial** |

### Code-indexing sub-taxonomy (3 T4 wikis)

| Axis | graphify v16 | GitNexus v33 | claude-context v40 |
|------|--------------|--------------|---------------------|
| **Retrieval** | Graph topology + Leiden clustering | Graph + LadybugDB + RRF | **BM25 + dense vector hybrid** |
| **Incremental** | Full rebuild | LadybugDB diff | **Merkle tree (novel)** |
| **Commercial** | None | akonlabs.com | **Zilliz Cloud funnel** |

---

## Phần 4 / Part 4 — Installation (5-10 phút)

### Prerequisites

**VN:** Bạn cần 3 thứ trước khi cài:

**EN:** You need 3 prerequisites:

1. **Node.js 20+** (nhưng < 24 — 24.0 chưa compatible). Check version: `node --version`
2. **Claude Code** (hoặc compatible MCP client: Cursor / Codex / Windsurf / Cline / Gemini / etc.)
3. **2 API keys:**
   - **OpenAI API key** ([platform.openai.com/api-keys](https://platform.openai.com/api-keys)) — cho embedding (mặc định; VoyageAI / Gemini / Ollama cũng work)
   - **Zilliz Cloud API key + endpoint** ([cloud.zilliz.com](https://cloud.zilliz.com)) — free Serverless tier enough cho vault cỡ 24K lines

### Quick install (Claude Code)

```bash
claude mcp add claude-context \
  -e OPENAI_API_KEY=sk-your-openai-key \
  -e MILVUS_ADDRESS=your-zilliz-cloud-endpoint \
  -e MILVUS_TOKEN=your-zilliz-cloud-api-key \
  -- npx @zilliz/claude-context-mcp@latest
```

**Restart Claude Code** để MCP server load.

### Alternative: Local Milvus (no Zilliz Cloud signup)

```bash
# Run Milvus locally via Docker
docker run -d --name milvus -p 19530:19530 milvusdb/milvus:latest

# Then configure MCP without MILVUS_TOKEN
claude mcp add claude-context \
  -e OPENAI_API_KEY=sk-... \
  -e MILVUS_ADDRESS=localhost:19530 \
  -- npx @zilliz/claude-context-mcp@latest
```

### Alternative: Fully local (Ollama + local Milvus)

```bash
# Install Ollama and pull embedding model
ollama pull nomic-embed-text

# Configure MCP
claude mcp add claude-context \
  -e EMBEDDING_PROVIDER=Ollama \
  -e EMBEDDING_MODEL=nomic-embed-text \
  -e MILVUS_ADDRESS=localhost:19530 \
  -- npx @zilliz/claude-context-mcp@latest
```

**Privacy-focused:** Không gửi code lên external API. Suitable cho client proprietary codebases.

### Other MCP clients (Cursor, Codex, Cline, Windsurf, etc.)

Config paths khác nhau per client — xem README upstream cho exact format:
- Cursor: `~/.cursor/mcp.json` hoặc `.cursor/mcp.json`
- Codex CLI: `~/.codex/config.toml` (TOML không phải JSON)
- Gemini CLI: `~/.gemini/settings.json`
- Cline: `cline_mcp_settings.json` (via Cline UI → Advanced MCP Settings)

Config schema tương tự: `command: npx`, `args: [@zilliz/claude-context-mcp@latest]`, `env: {OPENAI_API_KEY, MILVUS_ADDRESS, MILVUS_TOKEN}`.

---

## Phần 5 / Part 5 — Core usage pattern

### 3-step workflow

```bash
# 1. Navigate to project
cd your-project-directory
claude  # start Claude Code

# 2. Index codebase (first time only)
> Index this codebase

# 3. Search semantically
> Find functions that handle user authentication
> Where does payment webhook processing happen?
> Show me the email validation logic
```

**VN:** Claude sẽ tự động gọi 4 MCP tools (`index_codebase`, `search_code`, `clear_index`, `get_indexing_status`) khi bạn hỏi natural-language queries.

**EN:** Claude automatically invokes 4 MCP tools based on natural-language prompts.

### Check indexing status

```
> Check the indexing status
```

Response sẽ show progress % hoặc completion.

### Re-index sau khi code thay đổi

**VN:** claude-context dùng **Merkle tree** nên chỉ re-index files thực sự đã thay đổi — fast.

**EN:** Merkle-tree-based incremental indexing skips unchanged files — fast re-indexing.

### Clear index

```
> Clear the search index
```

---

## Phần 6 / Part 6 — Novel concepts + architecture

### Hybrid retrieval (BM25 + dense vector)

**VN:**
- **BM25** — keyword matching truyền thống (tốt cho exact function/variable names)
- **Dense vector** — semantic similarity (tốt cho intent queries như "auth logic")
- **Fusion** — kết hợp 2 scores để có best of both worlds

**EN:**
- BM25 = classical keyword retrieval (exact names)
- Dense vector = embedding-based semantic retrieval (intent queries)
- Results fused for hybrid ranking

### AST-based chunking

**VN:** Dùng **Tree-sitter** để parse code thành abstract syntax tree, sau đó chunk theo boundaries có ý nghĩa (function / class / module) thay vì cắt bừa theo số ký tự. Kết quả: chunks giữ được context structure.

**EN:** Tree-sitter AST parsing chunks code at semantic boundaries (function / class / module), preserving context.

**14 ngôn ngữ supported / 14 languages:**
TypeScript, JavaScript, Python, Java, C++, C#, Go, Rust, PHP, Ruby, Swift, Kotlin, Scala, Markdown

**Fallback:** LangChain character-based splitter nếu ngôn ngữ không support AST.

### Merkle-tree incremental indexing (corpus-first novel architecture)

**VN:**
1. Build content-addressable hash tree trên codebase
2. Mỗi subtree có hash riêng
3. Khi re-index, walk tree; nếu subtree hash không đổi → skip
4. Chỉ files hash-changed mới được re-embed

**EN:** Content-addressable Merkle tree enables efficient re-indexing — only files whose hash changed get re-embedded.

**Advantage:** Re-indexing 100K-line codebase mà chỉ thay đổi 50 lines = near-instant (chỉ re-embed subtree containing 50 lines).

### 4 embedding providers

| Provider | Best for | Local/Remote |
|----------|----------|--------------|
| OpenAI `text-embedding-3-small` (default) | General-purpose | Remote |
| VoyageAI `voyage-code-3` | **Specialized for code** | Remote |
| Gemini `gemini-embedding-001` | Multilingual | Remote |
| Ollama `nomic-embed-text` | **Privacy-first (local)** | Local |

### 2 vector DB backends

- **Milvus** — self-hosted (Docker); full control
- **Zilliz Cloud** — managed SaaS; free Serverless tier cho development/small-scale

---

## Phần 7 / Part 7 — So sánh với other corpus T4 code-indexing

### graphify v16 (Graph-based solo)

**Khi nên dùng graphify:**
- Cần **structural navigation** (ai call function này / blast radius của refactor)
- Want Obsidian export
- Knowledge-graph-first mental model

### GitNexus v33 (Graph-based + commercial entity)

**Khi nên dùng GitNexus:**
- Cần graph structure + cross-repo analysis
- OK với PolyForm Noncommercial license (non-commercial use)
- Want browser-native WASM runtime

### claude-context v40 (Vector-based + commercial-startup)

**Khi nên dùng claude-context:**
- Cần **natural-language semantic search** queries
- Want MCP-native Claude Code integration
- OK với Zilliz Cloud free tier OR self-host Milvus
- Want cost-measured token reduction

**VN mnemonic:**
- **Structural questions** (cấu trúc) → **graphify** hoặc **GitNexus**
- **Semantic questions** (ý nghĩa) → **claude-context**

### 3-plugin Claude Code augmentation stack

| Plugin | Role | License | Stars |
|--------|------|---------|-------|
| **claude-hud v35** | Context-window statusline visibility | MIT | 20K |
| **claude-context v40** | Semantic code search | MIT | 8.6K |
| **memsearch** (Zilliz sibling) | Persistent session memory | MIT | 1.4K |

Cả 3 MIT-licensed + MCP-compatible → có thể compose together thành Claude Code enhancement suite.

---

## Phần 8 / Part 8 — Ethical framing

**VN:** claude-context là MIT-licensed tool của Zilliz — commercial-startup với funnel rõ ràng sang Zilliz Cloud paid tier.

**Observable commercial funnel:**
- Free Zilliz Cloud Serverless tier → upgrade sang paid cho production scale
- UTM tracking (`utm_campaign=2507-codecontext-readme`) observable → Zilliz measures conversion từ OSS users

**EN:** claude-context is MIT OSS from Zilliz (commercial-startup) with transparent commercial funnel to Zilliz Cloud managed SaaS. Free Serverless tier available; production scale requires paid upgrade.

**Không có red-flag gì / No red flags:**
- MIT license = commercial use allowed
- Code transparent trên GitHub
- Alternative self-host path available (local Milvus)
- No anti-distillation or research-only restriction

**Mild considerations:**
- Zilliz is CN-origin company (US-registered) — nếu bạn có enterprise data sovereignty concerns, dùng self-hosted Milvus thay vì Zilliz Cloud
- OpenAI embedding API sends code chunks to OpenAI — nếu proprietary code concerns, dùng Ollama local embedding (fully-offline path)

---

## Phần 9 / Part 9 — Storm Bear / VN operator use cases

### Use case 1: Index Storm Bear vault cho semantic wiki-navigation

**VN:** Vault có ~40 wikis + nhiều cluster summaries + entity pages. Queries useful:

**EN:** Vault has ~40 wikis + cluster summaries + entity pages. Useful queries:

```
> Find wikis discussing Pattern #18 MCP Layer 1
> Which wikis use Tree-sitter for AST chunking?
> Show me commercial-funnel observations across all wikis
> Find wikis with Merkle-tree or incremental indexing
```

**Cost estimate:** ~$0.005 full index (OpenAI embedding) + free Zilliz Cloud Serverless tier.

### Use case 2: Scrum coaching codebase research

**VN:** Khi coaching team về technical debt, claude-context giúp:
- *"Find all places we handle rate limiting"*
- *"Where is authentication logic concentrated?"*
- *"Show me cache-invalidation patterns"*

Useful cho explaining architectural patterns tới team members who don't know codebase well yet.

### Use case 3: VN client codebase onboarding

**VN:** Khi onboard VN team/client, index codebase trước, sau đó pair-program với Claude Code. Search queries VN-friendly:
- *"Tìm function xử lý authentication"* (may work — embedding is multilingual; empirical test needed for VN quality)
- Or revert to EN queries for reliability

**Caveat:** VN-language embedding quality may be Tier-2 (behind EN). Test empirically on your data.

### Use case 4: Evaluate vs graphify (parallel pilot)

Run **both** claude-context + graphify on Storm Bear vault. Compare:
- graphify: structural navigation + Obsidian graph view
- claude-context: semantic search via natural-language queries

After 1-week pilot, decide which matches mental model better.

---

## Phần 10 / Part 10 — 4-week evaluation roadmap

### Week 1 — Install + index (2-3h)

- [ ] Sign up Zilliz Cloud free Serverless tier
- [ ] Get OpenAI API key (if not already)
- [ ] Install MCP server via `claude mcp add`
- [ ] Index Storm Bear vault (1 command trong Claude Code)
- [ ] Run 5-10 natural-language queries; evaluate quality

### Week 2 — Production project pilot (3-5h)

- [ ] Index 1 real project (Scrum client codebase hoặc personal project)
- [ ] Daily-usage: 3-5 queries/day cho 3-5 days
- [ ] Track: query latency, result relevance, cost (OpenAI bill + Zilliz Cloud usage)

### Week 3 — Compare with graphify (3-5h)

- [ ] Install graphify v16 on same vault/project
- [ ] Same queries both tools; compare results
- [ ] Decide: claude-context primary / graphify primary / both-parallel

### Week 4 — Decision + integration (2h)

- [ ] If keep claude-context: commit to `.mcp.json` trong project OR user-level
- [ ] If drop: document reason; un-install
- [ ] Update Storm Bear vault CLAUDE.md với pilot-result notes
- [ ] Schedule mini-audit for Pattern Library at next natural cadence

**Total time budget:** ~10-15h over 4 weeks (assumes parallel graphify evaluation).

---

## Phần 11 / Part 11 — Tradeoffs + limitations

### Strengths

- ✅ MIT license + OSS
- ✅ MCP-native — works với 12+ AI coding agents
- ✅ Cost reduction empirically measured (SWE-bench)
- ✅ 4 embedding providers + 2 vector DBs (flexibility)
- ✅ Merkle-tree incremental re-index (fast)
- ✅ Local Milvus + Ollama = fully offline option
- ✅ VS Code extension available
- ✅ Active development (168 commits, recent activity)

### Limitations

- ⚠️ **Node.js 20-22** strict — Node 24 not yet compatible
- ⚠️ **OpenAI embedding** sends code chunks to OpenAI (unless switch to Ollama)
- ⚠️ **Zilliz Cloud commercial funnel** — free tier enough for small/medium; production needs paid upgrade
- ⚠️ **Early version** (v0.1.7) — API may evolve
- ⚠️ **8.6K stars moderate** — smaller community than graphify v16 (30K) / GitNexus v33 (28.5K) at code-indexing T4
- ⚠️ **Markdown primary for code** — vault semantic search works but not primary use case
- ⚠️ **VN language** embedding quality needs empirical test
- ⚠️ **AGENTS.md absent** — no contributor-facing agent usage doc (common at T4)

### Supply-chain considerations

- npm package `@zilliz/claude-context-mcp` depends on:
  - `@modelcontextprotocol/sdk` (Anthropic-maintained MCP SDK)
  - `@zilliz/milvus2-sdk-node` (Milvus SDK)
  - Tree-sitter + multiple grammar packages
  - Various provider SDKs (OpenAI, Voyage, Gemini)
- Commercial vendor risk: Zilliz is ~$100M-funded commercial-startup; OSS version stable even if Zilliz Cloud business changes

---

## Phần 12 / Part 12 — Caveats + safety notes

### Before indexing production codebase

- ⚠️ **Embedding provider data handling** — OpenAI + VoyageAI + Gemini all process your code chunks; check each provider's data policy for your use case
- ⚠️ **Use Ollama cho fully-local** nếu indexing proprietary/sensitive codebase
- ⚠️ **Zilliz Cloud data residency** — check region when signing up cho data sovereignty
- ⚠️ **Chunk size 1000 / overlap 200** default — may need tuning cho large-function languages (Java) or narrow-scope languages

### Operational cost monitoring

- **OpenAI embedding cost:** ~$0.02/1M tokens for `text-embedding-3-small`
  - 100K-line codebase ≈ 2M tokens ≈ **$0.04 one-time full index**
  - Incremental re-indexes: only changed portions (much cheaper)
- **Zilliz Cloud free Serverless tier:** sufficient for small codebases; paid upgrade ~$19/month starting (check current pricing)
- **Query cost:** embedding cost per query + Zilliz Cloud query (free tier usually sufficient)

### Monitoring data sovereignty

- Nếu enterprise client requires data-residency compliance, dùng:
  - Ollama local embedding (no external API)
  - Milvus self-hosted (no external DB)
  - Fully-offline setup = 100% control

---

## Phần 13 / Part 13 — References + next action

### Official resources

- **GitHub:** https://github.com/zilliztech/claude-context
- **npm core:** https://www.npmjs.com/package/@zilliz/claude-context-core
- **npm mcp:** https://www.npmjs.com/package/@zilliz/claude-context-mcp
- **VS Code Marketplace:** `zilliz.semanticcodesearch`
- **Zilliz Cloud:** https://zilliz.com/cloud
- **Milvus docs:** https://milvus.io/docs
- **Discord:** https://discord.gg/mKc3R95yE5
- **Twitter:** [@zilliz_universe](https://twitter.com/zilliz_universe)
- **DeepWiki (AI docs):** https://deepwiki.com/zilliztech/claude-context

### Storm Bear wiki references

- Full entity analysis: `02 Wiki/(C) Entity 1 — Core Product (claude-context MCP).md`
- Ecosystem analysis: `02 Wiki/(C) Entity 2 — Zilliz ecosystem + commercial funnel.md`
- Sub-taxonomy analysis: `02 Wiki/(C) Entity 3 — Code-Indexing T4 Sub-Taxonomy (3 data points, 2 axes).md`
- Phase 4b T4 8-way: `03 Published/(C) T4 8-way extension + Code-Indexing Sub-Taxonomy + Pattern 50 N=3.md`

### Peer wikis (code-indexing T4)

- `03 Projects/graphify - Beginner Analysis/` — graph-based peer
- `03 Projects/GitNexus - Beginner Analysis/` — graph+commercial peer

### Immediate next action (operator decision)

**VN recommendation:** Với v27 diagnostic HIGH bundle đã deferred 17 sessions, Storm Bear operator decision-point:
1. **Execute v27 HIGH bundle** trước (items 1 + 2 + 5; 6-8h total; unblocks vault state)
2. **Run claude-context + graphify parallel vault pilot** next (3-5h empirical validation)
3. **Resume v41 wiki-building** sau

**EN recommendation:** With v27 diagnostic HIGH bundle deferred 17 sessions, suggested execution order: (1) v27 HIGH bundle → (2) claude-context + graphify vault pilot → (3) v41 wiki.

---

**Wiki version:** v40 / 40-wiki corpus milestone
**Routine:** llm-wiki-routine-v2.1 (5th v2.1-era execution)
**Date:** 2026-04-24
**Primitive-count outcome:** GREEN (standard 4-entity format fits cleanly)
