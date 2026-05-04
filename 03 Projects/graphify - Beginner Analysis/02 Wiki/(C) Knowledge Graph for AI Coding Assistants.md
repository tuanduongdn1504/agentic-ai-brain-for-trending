# (C) Knowledge Graph for AI Coding Assistants

> **Type:** Entity — core product
> **Parent:** [[(C) index]]
> **Sources:** [[(C) README + multi-language cluster summary]] §2-§4, [[(C) ARCHITECTURE + AGENTS + SECURITY cluster summary]] §2-§6
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

Graphify turns **any folder of code, docs, papers, images, or videos** into a **queryable knowledge graph** — extracted via tree-sitter AST (25 languages, deterministic, no LLM) + Claude subagent/vision (docs + images + multimedia) + local transcription (audio/video). The output is a **persistent NetworkX graph** with Leiden-detected communities, confidence-tagged edges (`EXTRACTED`/`INFERRED`/`AMBIGUOUS`), and multiple exports (HTML/Obsidian/Wiki/Neo4j). **71.5x token reduction on 52-file mixed corpus** is graphify's headline research-style benchmark. Unique architectural choice: **graph-topology clustering WITHOUT embeddings** — no vector DB required.

## 2. Key claims

1. **Multimodal input** — code + PDF + images + video + audio + URLs
2. **Deterministic code extraction** — tree-sitter AST, no LLM cost on code
3. **71.5x token reduction** on mixed 52-file corpus (research-style benchmark)
4. **Graph-topology clustering** — Leiden algorithm, no embeddings needed
5. **Confidence taxonomy** — 3-level edge labels (EXTRACTED/INFERRED/AMBIGUOUS) = epistemic honesty
6. **Persistent graph** — query weeks later without re-reading source
7. **Local-first** — no server, no vector DB, runs entirely locally
8. **Compound savings** — first run costs tokens; subsequent queries near-free

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 25 language support | README feature list | High |
| 71.5x token reduction | README benchmark table | High (claim) / Medium (methodology not fully published) |
| No embeddings | README + ARCHITECTURE.md (cluster.py uses Leiden) | High |
| Confidence taxonomy | ARCHITECTURE.md §Confidence Taxonomy verbatim | High |
| Persistent graph | README "persistent graph" | High |
| MCP server | ARCHITECTURE.md serve.py | High |
| 52-file benchmark | README benchmark section | High (stated) |

## 4. How it works — pipeline

### 7-stage pipeline

```
detect() → extract() → build_graph() → cluster() → analyze() → report() → export()
```

**Discipline:** "no shared state between stages" (ARCHITECTURE.md verbatim).

### Stage detail

| Stage | Module | What happens |
|-------|--------|--------------|
| 1. detect | detect.py | Filter files by registered extensions (25 langs + doc types + media) |
| 2. extract | extract.py | Per-file → node/edge dicts (tree-sitter for code; Claude subagent for docs; Claude vision for images; faster-whisper for audio/video) |
| 3. build_graph | build.py | Assemble extraction outputs into NetworkX graph |
| 4. cluster | cluster.py | Leiden algorithm (graspologic) → communities |
| 5. analyze | analyze.py | Identify god nodes + anomalies |
| 6. report | report.py | Markdown summary (GRAPH_REPORT.md) |
| 7. export | export.py | Obsidian / JSON / HTML / SVG / Wiki / Neo4j outputs |

### Deterministic vs probabilistic

- **Deterministic (no LLM):** Code extraction via tree-sitter AST; graph construction; Leiden clustering
- **Probabilistic (LLM-needed):** PDF subagent; image vision; audio transcription (model-based but local)
- **Caching:** extraction cached by file hash → subsequent runs only re-process changed files

### Cost profile

| Operation | LLM cost | Local cost |
|-----------|----------|------------|
| Code extraction (first run) | ~0 (tree-sitter deterministic) | CPU |
| PDF subagent extraction | Claude API calls | — |
| Image vision extraction | Claude vision API | — |
| Audio/video transcription | 0 (local faster-whisper) | GPU/CPU |
| `--update` (subsequent) | ~0 for unchanged files | cache lookups |
| Query (`graphify query`) | 1 call per question | graph traversal |

**Typical project (52 files mixed):** first run = moderate LLM cost; queries thereafter = 1 call per query, 71.5× less context.

## 5. Worked example — Karpathy /raw folder

### Scenario (from README)

Karpathy drops into `/raw/`:
- 5 research papers (PDFs)
- 4 whiteboard photos (images)
- nanoGPT repo (Python code, ~200 files)
- llm.c repo (C code, ~50 files)
- Various tweets (added via URLs)

### Graphify execution

```bash
pip install graphifyy
graphify claude install
cd /raw
/graphify .                    # First run — builds graph
/graphify query "How does attention work?"   # Traverse graph instead of re-reading papers
```

### Output

```
graphify-out/
├── graph.html                 (interactive)
├── graph.json                 (canonical)
├── GRAPH_REPORT.md           (markdown summary)
├── wiki/                     (if --wiki)
│   └── index.md              (Wikipedia-style entry points)
└── cache/                    (for --update)
```

### Benefit

- **First run:** ~$5-20 in Claude API (depending on LLM usage for PDFs/images)
- **Query:** 1 call × compact graph context (71.5× fewer tokens than raw corpus)
- **Weeks later:** same graph — no re-reading source files

## 6. Edges + failure modes

### Extraction edges

- **Tree-sitter parse error** — malformed code → file skipped, logged. No crash.
- **Claude vision rate limits** — many images → may throttle; manual retry needed
- **Faster-whisper CPU-only default** — long videos may be slow
- **Non-English text in images** — graphify claims multilingual support; quality varies by language

### Graph edges

- **Leiden stability** — community assignments may shift on minor updates; downstream wiki references may break
- **God node misidentification** — test coverage may label test files as "god nodes" incorrectly
- **Cache invalidation** — hash-based; doesn't auto-reextract dependents on utility changes

### Query edges

- **Graph-traversal vs LLM-reasoning** — graphify uses LLM on compact graph; still LLM-limited
- **DFS path budgets** — `--budget 1500` = token cap; may truncate long paths
- **Confidence levels in output** — user must interpret EXTRACTED vs INFERRED

### Export edges

- **Obsidian format** — wikilinks format may not match all Obsidian versions
- **Neo4j push** — requires running Neo4j; `--neo4j-push bolt://...` failures = unclear recovery
- **Large graphs** — HTML visualization may lag beyond 10K nodes

## 7. Why no embeddings

### Design rationale (from README)

Graphify's position:
> "Clustering is graph-topology-based — no embeddings."

**Arguments for this approach:**
1. **Semantic similarity already in graph** — if two nodes co-occur in extractions, the edge captures it
2. **Interpretability** — graph structure explainable; vector embeddings opaque
3. **No infra dependency** — no pgvector, no Pinecone, no Weaviate
4. **Deterministic communities** — Leiden converges reproducibly
5. **Scale invariance** — graph algorithms scale predictably vs embeddings

### Contrast with multica v15 (pgvector)

- multica: PostgreSQL 17 + pgvector — RAG-style retrieval
- **graphify: NetworkX + Leiden — structural retrieval**
- Philosophically opposite

### Tradeoffs

| Aspect | Embeddings (multica) | Graph-topology (graphify) |
|--------|---------------------|--------------------------|
| Cold-start quality | Good if model good | Depends on extraction quality |
| Infra | Vector DB required | None |
| Update cost | Re-embed changed files | Re-extract + re-cluster |
| Interpretability | Low (opaque) | High (edges visible) |
| Unstructured data | Excellent | Good if extracted correctly |
| Structural queries | Hard | Native |

**Graphify bets on structural queries + interpretability.**

## 8. Confidence taxonomy deep-dive

### 3 levels

```
EXTRACTED   — explicit in source ("function foo() calls bar()")
INFERRED    — LLM deduced from context ("this class implements auth pattern")
AMBIGUOUS   — uncertain; flagged for review (partial vision extraction, etc.)
```

### Corpus significance

**First framework with explicit edge-level epistemic confidence.** Parallels:
- paperclip v14: governance invariants (trust boundaries at architecture level)
- gws v13: trusted/untrusted input zones
- **graphify:** trust at edge level (every relationship labeled)

### Implications for agent use

Agents querying graphify can:
- Weight EXTRACTED > INFERRED in reasoning
- Flag AMBIGUOUS for human review
- Provide honest "I found X but inferred Y" responses

This is **honest epistemics encoded in data structure** — rare in corpus.

## 9. Related concepts

- [[(C) 15-Platform Install + Agent-Runtime Standards Confirmed]] — distribution
- [[(C) Karpathy-Inspired Raw-Folder Problem + Meta-Cycle Extension]] — design lineage
- [[(C) T4 3-way Extension + Pattern 9 Test + Storm Bear]] — tier context

## 10. Cross-project comparison

### vs multica v15 pgvector

| Aspect | multica pgvector | graphify graph-topology |
|--------|------------------|------------------------|
| Retrieval approach | Vector similarity | Graph traversal + clustering |
| Infra | Postgres 17 + pgvector | Just Python + NetworkX |
| Best for | Unstructured semantic search | Code/doc structural queries |
| Embedding cost | Per-file on update | 0 (topology-based) |

### vs notebooklm-py v7 (T4 peer)

| Aspect | notebooklm-py | graphify |
|--------|---------------|----------|
| Bridge target | NotebookLM web API | Local filesystem |
| Output | Programmatic access to NotebookLM | Standalone knowledge graph |
| Multimodal | Relies on NotebookLM | Local extraction |
| Persistence | In NotebookLM | In graphify-out/ |

### vs gws v13 (T4 peer)

| Aspect | gws | graphify |
|--------|-----|----------|
| Bridge target | Google Workspace (11+ services) | Local filesystem (any content type) |
| Official? | ✅ Google | ❌ Solo safishamsi |
| Scope | Specific services | General-purpose extraction |
| Stars | 25K | 30K |

### vs autoresearch v10 (Karpathy peer)

| Aspect | autoresearch | graphify |
|--------|--------------|----------|
| Karpathy relation | His own project | Cites /raw folder |
| Purpose | ML experimentation | Knowledge extraction |
| Usage | Agent-run overnight | User-invoked on demand |

## 11. Open questions

- Q4: Leiden resolution parameter? (partially exposed via --mode)
- Q10: Portable graphs across machines? (graph.json likely is, obsidian absolute-path risk)
- Q12: INFERRED edge confidence score algorithm?
- Q27: Benchmark methodology reproducibility?

## 12. Decision log

- **v0.1:** initial deterministic code extraction
- **v0.2:** multimodal (docs + images)
- **v0.3:** audio/video + MCP server
- **v0.4 current:** 15-platform install + wiki generation
- **Future (inferred):** multi-repo graphs + team sharing + commercial via penpax.ai

## 13. Storm Bear relevance

### Direct applicability to Storm Bear vault

**Immediate action item:** Run graphify on Storm Bear vault itself.

```bash
pip install graphifyy
graphify claude install
cd "/Users/Cvtot/KJ OS Template"
/graphify . --obsidian --wiki
```

Expected output:
- Graph of 16 wiki projects + cross-references
- Communities = tier clusters (T1/T2/T3/T4/T5)
- God nodes = most-referenced entities (Karpathy, OpenClaw, Hermes, Pattern #9)
- Wiki generation = Wikipedia-style navigation over existing Storm Bear content

**This is a real experiment Storm Bear should run.**

### Use cases for Storm Bear

1. **Vault meta-analysis** — graph of wikis reveals structure Storm Bear may not see
2. **Pattern discovery automation** — god-node detection may surface patterns (Pattern #19+ candidates)
3. **Cross-wiki links surfaced** — graphify infers relationships Storm Bear may have missed
4. **Maintenance alerts** — `--watch` detects stale claims when source wikis update
5. **Published output** — `--wiki` generates public-facing Storm Bear knowledge base

### 14. References

- README.md (en) — primary source
- README.ja-JP.md + README.ko-KR.md + README.zh-CN.md — CJK translations
- ARCHITECTURE.md — pipeline details
- AGENTS.md — agent usage guidance
- Homepage: https://safishamsi.github.io/penpax.ai
- PyPI: https://pypi.org/project/graphifyy/
- Parent: [[(C) index]]
