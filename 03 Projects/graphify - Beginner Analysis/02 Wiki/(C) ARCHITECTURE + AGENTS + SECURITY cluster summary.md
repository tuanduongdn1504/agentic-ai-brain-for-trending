# (C) ARCHITECTURE + AGENTS + SECURITY cluster summary — graphify

> **Sources:** ARCHITECTURE.md + AGENTS.md + SECURITY.md (v4 branch)
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

3 technical/governance docs at repo root: ARCHITECTURE.md explains pipeline; AGENTS.md gives agent usage guidance; SECURITY.md covers input validation. Together they reveal graphify's engineering discipline and trust model.

## 2. ARCHITECTURE.md — pipeline and components

### Linear pipeline (verbatim)

> `detect() → extract() → build_graph() → cluster() → analyze() → report() → export()`

**Discipline:** "no shared state between stages."

**Parallel to other corpus pipelines:**
- gws v13: Dynamic Discovery → runtime CLI tree
- paperclip v14: Company → Org Chart → Employee
- **graphify:** File → Extract → Graph → Cluster → Export

### Component map

| Component | File | Responsibility |
|-----------|------|----------------|
| Input detection | `detect.py` | Filter files by registered extensions |
| Extraction | `extract.py` | Parse files into node/edge dicts |
| Cache | `cache.py` | Split work into cached vs uncached |
| Build | `build.py` | Assemble extractions into NetworkX graph |
| Cluster | `cluster.py` | Leiden community detection |
| Analyze | `analyze.py` | Identify god nodes + anomalies |
| Report | `report.py` | Generate markdown summary |
| Export | `export.py` | Obsidian / JSON / HTML / SVG outputs |
| Serve | `serve.py` | **MCP stdio server** |
| Watch | `watch.py` | Directory change monitoring |
| Security | `security.py` | Input validation |

### Extraction format (standardized JSON)

```json
{
  "nodes": [
    {"id": "...", "label": "...", "source_location": "..."}
  ],
  "edges": [
    {"source": "...", "target": "...", "relation": "...", "confidence": "EXTRACTED|INFERRED|AMBIGUOUS"}
  ]
}
```

Every extractor (tree-sitter code, PDF subagent, vision image) emits this schema. Unified format = unified graph.

### Confidence taxonomy (3 levels)

| Level | Meaning | Example |
|-------|---------|---------|
| `EXTRACTED` | Explicit statement found in source | "function foo() calls bar()" |
| `INFERRED` | LLM deduction from context | "this class implements auth pattern" |
| `AMBIGUOUS` | Uncertain — flagged for review | Vision detects partial text |

**Significance:** First corpus framework with explicit epistemic-confidence taxonomy on edges. Parallels paperclip v14's 5 control-plane invariants (both are governance-via-architecture patterns).

## 3. AGENTS.md — agent usage guidance

### Purpose

Single-file convention: agents working in the repo consult `graphify-out/GRAPH_REPORT.md` and `graphify-out/wiki/index.md` **before** reading individual source files.

### Key rules (verbatim-paraphrase)

1. **Architecture queries:** Consult `graphify-out/GRAPH_REPORT.md` first → understand god nodes + community organization
2. **Navigation:** Use `graphify-out/wiki/index.md` as primary entry point (not individual files)
3. **After code changes:** Run `graphify update .` to refresh knowledge graph (AST-only, no API cost)

### Governance model

**Lightweight** — single file, simple rules. Contrast with:
- paperclip v14 (5 invariants + 4 primitives = heavy)
- multica v15 (21KB CLAUDE.md + cross-platform rules = medium)
- gws v13 (tri-file CLAUDE + AGENTS + CONTEXT = medium)
- **graphify (single AGENTS.md = lightest)**

### Corpus placement for AGENTS.md pattern

AGENTS.md first emerged around paperclip v14 / gws v13 as convention. Graphify adopts lightly.

## 4. SECURITY.md — input validation layer

### Scope

- **URL validation** — for `graphify add <url>` commands
- **Fetched content size/timeout** — prevents DoS via large downloads
- **Graph file paths** — prevents path traversal on load/export
- **Node label sanitization** — control chars stripping + 256-char cap + HTML escape

### Validation details (verbatim)

> "control chars stripping, 256-char cap, HTML-escaping"

Applied in `security.py`, consumed by extraction + export layers.

### Corpus context

First corpus framework with dedicated SECURITY.md at root:
- gws v13 has AGENTS.md §6 "adversarial-input-first validation policy" (inline)
- paperclip v14 has governance primitives (architectural)
- **graphify first with SECURITY.md as standalone file**

**Pattern hypothesis:** As agent-skills handle untrusted external content (URLs, images, transcripts), explicit SECURITY.md emerges. Prediction: future agent-skill frameworks will adopt SECURITY.md convention.

## 5. MCP server architecture

### Exposed operations (from serve.py)

- `query_graph` — free-form question → graph traversal
- `get_node` — fetch node details by ID
- `get_neighbors` — fetch N-hop neighbors
- `shortest_path` — path between two nodes

### Invocation

```bash
python -m graphify.serve graphify-out/graph.json
```

### Corpus significance

**First corpus wiki where MCP is explicit first-class output.** Prior frameworks mention MCP (GSD v5, gws v13) but graphify ships production MCP server.

**Pattern candidate:** As MCP ecosystem matures, agent-skills may default to MCP server as primary query interface. Prediction testable across future wikis.

## 6. Graph structure

### Node types (inferred from README + ARCHITECTURE)

- **File nodes** — per-file in the corpus
- **Concept nodes** — extracted concepts (classes, functions, ideas from docs)
- **Entity nodes** — named entities from vision/PDF extraction
- **Community nodes** — Leiden-detected clusters (virtual)

### Edge relations (inferred)

- Structural (code): `calls`, `imports`, `inherits`, `uses`
- Semantic (docs/images): `discusses`, `references`, `illustrates`
- Cross-modal: code ↔ docs mapping

### Leiden community detection

- Implemented via **graspologic** library (Microsoft Research)
- Optimizes modularity — dense-edge subgraphs as communities
- Resolution parameter controlled by `--mode` flag (implied)

## 7. Cache architecture

From `cache.py` splitting work into cached vs uncached:

- **File-level caching** — hash-based (likely content hash)
- **Extraction caching** — avoid re-calling Claude for unchanged files
- **Update pathway:** `--update` uses cache to re-extract only changed files

**Cost implication:** First run pays LLM extraction cost; subsequent updates near-free.

**Compared to multica v15 hybrid architecture:** graphify is even more aggressive on local execution — no cloud orchestration at all.

## 8. Watch mode architecture

`watch.py` monitors directory:
- File change events trigger incremental `--update`
- Background process manages debouncing
- Commits to graph.json atomically

## 9. Edges + failure modes

### Pipeline edges

- **Extraction failure** — tree-sitter parse error on malformed code → file skipped, logged
- **Vision limit** — Claude vision has image size caps → large whiteboard photos may fail
- **Audio transcription** — faster-whisper CPU-only by default → slow on long videos

### Security edges

- **URL fetching** — SECURITY.md covers size/timeout; not clear on content-type validation
- **Path traversal** — graph file paths validated; unclear if source-file paths validated for extraction
- **Code injection via node labels** — HTML-escape prevents HTML injection; unclear on shell injection for Obsidian/markdown export

### Architectural edges

- **No shared state between stages** — discipline maintained; but makes debugging harder
- **Cache invalidation** — hash-based; dependency-graph invalidation not clear (e.g., if utility.py changes, callers might need re-extraction)
- **Leiden stability** — community assignments may shift on minor updates → breaks persistent references

## 10. Tech ecosystem maturity signals

### Libraries used

- **NetworkX** — 20+ year Python standard
- **graspologic** — Microsoft Research-backed
- **tree-sitter** — GitHub-backed, 25+ languages
- **Claude API** — Anthropic
- **faster-whisper** — active open-source
- **vis.js** — mature visualization
- **Python 3.10+** — modern baseline

**Mature stack, no bleeding-edge dependencies** — contrast with multica v15 (Node 22 + Go 1.26 bleeding edge).

### Deployment model

- **pip install** — Python-standard
- **No server** — local-only
- **No vector DB** — graph-topology replaces
- **Optional Neo4j** — export, not dependency

**Lowest-friction deployment in corpus** — `pip install graphifyy && graphify install`.

## 11. Cross-references

- [[(C) README + multi-language cluster summary]] — positioning
- [[(C) Integration + Packaging + 15 Platforms cluster summary]] — distribution
- [[(C) Knowledge Graph for AI Coding Assistants]] (entity)

## 12. Open questions

- Q4: Leiden resolution parameter controllable? (partially — via --mode)
- Q12: INFERRED edge confidence scoring algorithm?
- Q13: Vision rate limits?
- Q15: Rename detection in --watch?

## 13. Corpus-first observations

- **First SECURITY.md at repo root** (graphify)
- **First first-class MCP server output** (graphify)
- **First explicit 3-level confidence taxonomy on edges** (graphify)
- **First graph-topology-no-embeddings** (graphify — architectural novelty)
- **Lightest agent-docs governance** (single AGENTS.md file)
