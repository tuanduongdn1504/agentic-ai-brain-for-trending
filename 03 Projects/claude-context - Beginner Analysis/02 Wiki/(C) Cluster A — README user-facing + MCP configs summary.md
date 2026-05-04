# (C) Cluster A — README user-facing + MCP configs summary

> **Source files in cluster:** `README.md` (755 lines) + `docs/README.md` + 12+ MCP client config subsections embedded in README + documentation site navigation
> **Scope:** User-facing positioning + quick-start + MCP client integrations + usage patterns + architecture overview + evaluation summary + roadmap

---

## 1. Identity & tagline

**Repo description (verbatim):** *"Code search MCP for Claude Code. Make entire codebase the context for any coding agent."*

**README hero (verbatim):** *"Your entire codebase as Claude's context"*

**Positioning sentence (verbatim):** *"Claude Context is an MCP plugin that adds semantic code search to Claude Code and other AI coding agents, giving them deep context from your entire codebase."*

**Value-proposition (verbatim):** *"Instead of loading entire directories into Claude for every request, which can be very expensive, Claude Context efficiently stores your codebase in a vector database and only uses related code in context to keep your costs manageable."*

**Philosophy distilled:** Cost-effective semantic retrieval substitute for naive directory-loading. Pricing-conscious positioning is unusual in agent-space (most frameworks frame around capability); Zilliz explicitly foregrounds cost.

**Brand variations observed:**
- Top-level repo: `claude-context`
- npm scopes: `@zilliz/claude-context-core` + `@zilliz/claude-context-mcp`
- VS Code Marketplace: `semanticcodesearch` (slug)
- Void config sometimes uses `code-context` (README inconsistency noted — minor)

**Corpus-first observation:** **Cost-first framing at T4 bridge-tier.** Prior T4 entrants (gws / notebooklm-py / graphify / TrendRadar / markitdown / crawl4ai / GitNexus) foregrounded capability or discovery. claude-context explicitly leads with cost-reduction narrative — commercially pragmatic framing.

---

## 2. Demo + integration flow

**MCP demo flow (verbatim paraphrase):**
1. Get free Zilliz Cloud account → API key
2. Get OpenAI API key for embedding
3. Run `claude mcp add claude-context -e OPENAI_API_KEY=... -e MILVUS_ADDRESS=... -e MILVUS_TOKEN=... -- npx @zilliz/claude-context-mcp@latest`
4. Open Claude Code in project directory → "Index this codebase" → wait → "Find functions that handle user authentication"

**4 MCP tools exposed** (from `### Available Tools` section):
1. `index_codebase` — hybrid BM25 + dense vector index build
2. `search_code` — natural-language queries → semantic results
3. `clear_index` — clear index for a codebase
4. `get_indexing_status` — progress % / completion status

**Novel architectural primitive (corpus-first):** **Indexing lifecycle is exposed as explicit MCP tool surface** — not hidden behind auto-indexing. Agent decides when to index, searches across states. Distinct from graphify v16 (implicit `/graphify` skill invocation) and GitNexus v33 (multi-tool MCP but no explicit lifecycle exposure).

---

## 3. 12+ MCP client configurations (corpus-broadest documented MCP-client support)

Configurations explicitly documented in `README.md`:

| # | Client | Config format | Notable detail |
|---|--------|---------------|----------------|
| 1 | **Claude Code** (primary) | `claude mcp add` CLI | Product-name-referring; positioned as default audience |
| 2 | **OpenAI Codex CLI** | `~/.codex/config.toml` (TOML) | `mcp_servers.claude-context` table syntax + `startup_timeout_ms` (custom timeout override) |
| 3 | **Gemini CLI** | `~/.gemini/settings.json` | Standard JSON `mcpServers.claude-context` |
| 4 | **Qwen Code** | `~/.qwen/settings.json` | Standard JSON; CN AI coding agent |
| 5 | **Cursor** | `~/.cursor/mcp.json` or `.cursor/mcp.json` | Global vs project-scoped |
| 6 | **Void** | UI-driven via Settings → MCP | Config typo: `code-context` vs `claude-context` (minor inconsistency in README) |
| 7 | **Claude Desktop** | standard `mcpServers` JSON | Anthropic desktop client |
| 8 | **Windsurf** | standard JSON MCP settings | |
| 9 | **VS Code** (generic) | MCP-compatible extensions JSON | Uses `-y` npx flag |
| 10 | **Cherry Studio** | GUI-driven configuration | Visual MCP server setup; first corpus documentation of Cherry Studio at T4 |
| 11 | **Cline** | `cline_mcp_settings.json` | Cline UI navigation documented (MCP Servers icon → Installed → Advanced MCP Settings) |
| 12 | **Augment Code** | UI or `augment.advanced.mcpServers` array | Two config paths documented |
| 13 | **Roo Code** | `mcp_settings.json` | Settings → MCP Servers → Edit Global Config |
| 14 | **Zencoder** | JetBrains + VS Code plugins | UI-driven Add Custom MCP |
| 15 | **LangChain/LangGraph** | SDK pattern reference (commit-pinned URL) | Custom Python bridge example `evaluation/retrieval/custom.py#L88` |
| 16 | **Other MCP Clients** (catch-all) | stdio transport | Standard MCP protocol |

**Corpus-first at T4 code-indexing sub-taxonomy:** **12+ documented MCP-client integrations.** Contrast:
- graphify v16: 15 platforms but most are generic
- GitNexus v33: 5 AI editor integrations (Claude Code + Cursor + Codex + Windsurf + OpenCode)
- claude-context v40: 12+ explicit with distinct config formats (TOML + JSON + UI) documented

**Pattern #18 Layer 1 MCP-protocol-universal strengthening** — claude-context's MCP-primary distribution + 12-client documentation = strongest MCP-layer-native T4 evidence in corpus.

---

## 4. Environment variable configuration

Referenced: `docs/getting-started/environment-variables.md` (detailed guide; Phase 2 probe confirmed existence via docs TOC).

Observed env vars:
- `OPENAI_API_KEY` — embedding auth
- `MILVUS_ADDRESS` — vector DB endpoint (self-hosted or Zilliz Cloud)
- `MILVUS_TOKEN` — Zilliz Cloud auth (omit for local Milvus)
- `EMBEDDING_PROVIDER` — switch among OpenAI / VoyageAI / Gemini / Ollama
- `EMBEDDING_MODEL` — per-provider model override
- `OPENAI_BASE_URL` — Azure OpenAI / compatible override
- `VOYAGEAI_API_KEY` — VoyageAI override
- `GEMINI_API_KEY` + `GEMINI_BASE_URL`
- `OLLAMA_HOST` — localhost:11434 default

**Provider abstraction evidence** — 4 embedding providers with per-provider env overrides = Pattern #28 Multi-Provider AI Support 8th data point.

---

## 5. Usage in Claude Code (3-step flow)

Documented flow:
1. `cd your-project-directory && claude`
2. Prompt: *"Index this codebase"*
3. Prompt: *"Check the indexing status"* → *"Find functions that handle user authentication"*

**Natural-language-prompt-driven indexing** — user interacts via prompts, agent invokes MCP tools. No CLI flags, no setup UI (beyond env vars). Aligns with MCP philosophy: agent as orchestrator.

---

## 6. Architecture (verbatim from `🏗️ Architecture`)

**Implementation details (verbatim bullets):**
- **Hybrid Code Search** (BM25 + dense vector)
- **Context-Aware** — relates across millions of lines of code
- **Incremental Indexing** — *"Efficiently re-index only changed files using Merkle trees"*
- **Intelligent Code Chunking** — AST-based
- **Scalable** — Zilliz Cloud integration
- **Customizable** — file extensions, ignore patterns, embedding models

**Merkle-tree incremental indexing = CORPUS-FIRST architectural observation.** No prior wiki uses Merkle trees for codebase re-indexing. graphify v16 uses NetworkX graph rebuild; GitNexus v33 uses LadybugDB graph; markitdown v28 is stateless conversion. Novel mechanism at T4 code-indexing: content-addressable hash-tree allows incremental re-index bounded by actual file changes.

### Core components (verbatim monorepo structure)

- **`@zilliz/claude-context-core`** — *"Core indexing engine with embedding and vector database integration"*
- **VSCode Extension** — *"Semantic Code Search extension for Visual Studio Code"*
- **`@zilliz/claude-context-mcp`** — *"Model Context Protocol server for AI agent integration"*

**Unstated in top README but present in source tree:**
- **Chrome Extension** (packages/chrome-extension) — GitHub code search browser extension (Coming Soon on Chrome Web Store)
- **Python bridge** (python/) — TypeScript↔Python integration path
- **Evaluation** (evaluation/) — reproducible benchmark framework

### Supported technologies

- **Embedding providers:** OpenAI / VoyageAI / Ollama / Gemini
- **Vector databases:** Milvus / Zilliz Cloud (managed SaaS)
- **Code splitters:** AST-based (Tree-sitter; automatic fallback) / LangChain character-based
- **Languages:** TypeScript, JavaScript, Python, Java, C++, C#, Go, Rust, PHP, Ruby, Swift, Kotlin, Scala, Markdown (14 total)
- **Tools:** VSCode + MCP

---

## 7. Alternative use paths (non-MCP)

**Core package Library API** (corpus-first explicit 3-deployment-mode documentation):

```typescript
import { Context, MilvusVectorDatabase, OpenAIEmbedding } from '@zilliz/claude-context-core';
const context = new Context({ embedding, vectorDatabase });
await context.indexCodebase('./your-project', (progress) => { ... });
const results = await context.semanticSearch('./your-project', 'vector database operations', 5);
```

**VSCode Extension** via Marketplace `zilliz.semanticcodesearch` — IDE-integrated semantic search UI.

**3 deployment surfaces explicitly documented:** MCP (recommended for AI agents) / Core library (custom apps) / VS Code extension (IDE use).

---

## 8. Evaluation (empirical corpus-first at T4 code-indexing)

**From evaluation summary:**
> *"Our controlled evaluation demonstrates that Claude Context MCP achieves ~40% token reduction under the condition of equivalent retrieval quality."*

**Quoted metrics:**
- Token usage: 73,373 (baseline) → 44,449 (+MCP) = **-39.4%**
- Tool calls: 8.3 → 5.3 = **-36.3%**
- F1-score: 0.40 (both) — equivalent retrieval quality preserved
- Dataset: 30 SWE-bench Verified instances (15-60 min difficulty, 2 file modifications)
- Framework: LangGraph MCP + ReAct via GPT-4o-mini
- Replicates: 3 runs × 2 methods = 6 total runs

**Pattern #8 Research-Benchmark Integration 9th data point** — SWE-bench Verified subset methodology joins OpenHands v30 as 2nd SWE-bench corpus usage. **First T4 empirical evaluation with SWE-bench substrate.**

**Corpus-first methodological observation:** Reproducible comparative methodology with structured baseline (grep-only) vs treatment (grep + MCP) and explicit dataset-generation script (`generate_subset_json.py`). Publishable-grade rigor at T4-tier OSS.

---

## 9. FAQ + troubleshooting references

From `docs/troubleshooting/faq.md` (Q&A headers observed):
1. What files does Claude Context decide to embed?
2. Can I use a fully local deployment setup? (Ollama + local Milvus)
3. Does it support multiple projects/codebases?
4. How does Claude Context compare to other coding tools like Serena, Context7, or DeepWiki?

**Comparative positioning** — README explicitly calls out Serena + Context7 + DeepWiki as peers. Corpus-first T4 code-indexing with **explicit competitor-naming in FAQ**. Prior T4 wikis did not self-position against named competitors.

---

## 10. Roadmap (verbatim bullet status)

- [x] AST-based code analysis for improved understanding
- [x] Support for additional embedding providers
- [ ] Agent-based interactive search mode
- [x] Enhanced code chunking strategies
- [ ] Search result ranking optimization
- [ ] Robust Chrome Extension

**3 shipped + 3 pending.** Chrome Extension is flagged "Coming Soon" in packages/chrome-extension/README.md; roadmap confirms not yet production-ready.

**Agent-based interactive search mode** — hypothesis: next-generation MCP tool that iterates ranked results with agent feedback; not yet shipped.

---

## 11. Links & external references

- GitHub: https://github.com/zilliztech/claude-context
- VSCode Marketplace: `zilliz.semanticcodesearch`
- npm core: `@zilliz/claude-context-core`
- npm mcp: `@zilliz/claude-context-mcp`
- Zilliz Cloud: https://zilliz.com/cloud
- Milvus docs: https://milvus.io/docs
- Discord: discord.gg/mKc3R95yE5
- Twitter: @zilliz_universe
- DeepWiki: deepwiki.com/zilliztech/claude-context (2nd corpus use after claude-code-best-practice v34)

---

## 12. Pattern Library observations

| Pattern | Status | Observation |
|---------|--------|-------------|
| #2 Distribution Evolution | Strengthening | 3 surfaces (Core API + VS Code + MCP) + npm + Chrome-coming = multi-surface mature distribution |
| #8 Research-Benchmark | 9th data point | SWE-bench Verified subset with reproducible methodology |
| #17 Ecosystem-Layer variant 3 | Strengthening | Zilliz commercial-startup ecosystem (Milvus + claude-context + memsearch + Zilliz Cloud + 4 others) |
| #18 MCP Layer 1 | 15th+ strengthening | MCP-PRIMARY distribution + 12-client doc breadth |
| #22 AGENTS.md | T4-abstention observation | No AGENTS.md at root; continuing T4-abstention majority |
| #27 Community-Viral | 16th observation | 8.6K corporate-amplified + Trendshift + DeepWiki integration; corporate-amplified sub-path |
| #28 Multi-Provider AI Support | 8th data point | 4 embedding providers + 2 vector DBs |
| #50 Commercial-Funnel Companion | **N=3 STRENGTHENING** | Zilliz Cloud free Serverless with UTM-tracked sign-up — first T4 data point for #50 |

---

## 13. Novel observations / corpus-firsts

1. **Cost-first README framing at T4** — explicit commercial pragmatism unusual for code-indexing bridge
2. **Merkle-tree incremental indexing** — novel architecture for codebase re-index (no prior corpus use)
3. **12+ explicit MCP-client integration docs** — broadest at T4-bridge tier
4. **Indexing lifecycle exposed as 4 separate MCP tools** — explicit agent-invokable lifecycle
5. **SWE-bench Verified at T4 code-indexing** — reproducible empirical methodology 2nd corpus use (OpenHands v30 1st)
6. **DeepWiki AI-docs integration** — 2nd corpus (after claude-code-best-practice v34)
7. **Explicit competitor-naming in FAQ** — Serena + Context7 + DeepWiki comparison
8. **Zilliz Cloud UTM-tracked commercial funnel** — observable commercial-conversion-funnel instrumentation

---

## 14. Cross-wiki bridges (mandatory)

- **graphify v16** (T4c graph-based code indexing) — vector vs graph code-indexing sub-taxonomy axis
- **GitNexus v33** (T4g graph + commercial code indexing) — 2nd graph-based + commercial predecessor
- **awesome-mcp-servers v31** — directory where claude-context would likely list itself
- **markitdown v28** (T4e corporate-narrow-utility) — sibling Microsoft vs Zilliz corporate narrow-utility comparison
- **OpenHands v30** (T5) — SWE-bench Verified methodology shared substrate

---

## 15. Summary

Cluster A establishes claude-context as **T4 Agent-as-bridge, commercial-ecosystem-startup variant, MCP-primary-native, vector-search-based code indexing**. Key positioning: cost-reduction via substitute-for-naive-directory-loading. 4-surface distribution (core + mcp + vscode + chrome-coming). 12+ MCP clients documented. Novel Merkle-tree incremental indexing + SWE-bench empirical validation. Commercial companion Zilliz Cloud with observable UTM-funnel instrumentation. Light governance + MIT license + Zilliz corporate backing.

Architecture decision-points documented in Cluster B; ecosystem context + commercial funnel in Cluster C.
