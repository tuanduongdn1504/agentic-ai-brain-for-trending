# (C) README + multi-language cluster summary — graphify

> **Sources:** README.md (en) + README.ja-JP.md + README.ko-KR.md + README.zh-CN.md (all from v4 branch)
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

4 language versions of README document the same positioning. Cluster view extracts: (a) positioning, (b) features, (c) benchmarks, (d) Karpathy inspiration, (e) commands, (f) install surface, (g) CJK-trio localization pattern.

## 2. Core positioning (verbatim)

### English (primary)

> "A Claude Code skill. Type `/graphify` in Claude Code — it reads your files, builds a knowledge graph, and gives you back structure you didn't know was there."

> "AI coding assistant skill. Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph."

### Karpathy inspiration (verbatim)

> "Andrej Karpathy keeps a `/raw` folder where he drops papers, tweets, screenshots, and notes. graphify is the answer to that problem."

**Meta-significance:** 2nd Karpathy reference in corpus after autoresearch v10 (Karpathy's own). graphify is **Karpathy-inspired but not Karpathy-authored** — novel connection type.

## 3. Features (from README structured list)

### Extraction capabilities

- **Code:** 25 programming languages via tree-sitter AST parsing (deterministic — no LLM needed)
- **Docs:** PDF, markdown, plain text via Claude subagent extraction
- **Images:** Screenshots, diagrams, whiteboard photos, multilingual text via Claude vision
- **Audio/Video:** Local transcription via faster-whisper
- **URLs:** Direct fetch for arxiv papers, Twitter threads, video transcripts (`graphify add <url>`)

### Knowledge graph features

- **Persistent graph** — query weeks later without re-reading source files
- **Confidence-tagged edges** — `EXTRACTED` / `INFERRED` / `AMBIGUOUS`
- **Honest attribution** — separates "what was found" from "what was guessed"
- **Community detection** — Leiden algorithm (via graspologic) over edge topology
- **God nodes identification** — critical components surfaced automatically
- **No embeddings required** — graph-topology clustering instead of vector similarity

### Output formats

- **Interactive HTML** (`graph.html`) — vis.js rendered
- **Obsidian vault** (`--obsidian`) — markdown with wikilinks
- **Wiki generation** (`--wiki`) — Wikipedia-style articles per community
- **SVG** (`--svg`) — static export
- **GraphML** (`--graphml`) — Gephi/yEd compatible
- **Neo4j** (`--neo4j`, `--neo4j-push bolt://host:port`)
- **JSON** (`graph.json`) — canonical format
- **Markdown report** (`GRAPH_REPORT.md`) — summary

### Workflow features

- **Git hooks** — `graphify hook install` (post-commit + post-checkout auto-rebuild)
- **Watch mode** — `--watch` auto-sync on file changes
- **Incremental update** — `--update` merges into existing graph, re-extracts only changed files
- **MCP server** — `python -m graphify.serve` exposes structured API

## 4. Performance benchmarks

### Token reduction claims (verbatim)

| Corpus | Files | Reduction |
|--------|-------|-----------|
| Karpathy repos + 5 papers + 4 images | 52 | **71.5x** |
| graphify source + Transformer paper | 4 | 5.4x |
| httpx synthetic library | 6 | ~1x |

**Interpretation from README:** *"6 files fits in a context window anyway, so graph value there is structural clarity, not compression."*

**Compound savings:** *"The first run extracts and builds the graph (this costs tokens). Every subsequent query reads the compact graph instead of raw files — that's where the savings compound."*

### Corpus context

Graphify is **3rd research-style benchmark in corpus**:
- codymaster SkillsBench +18.6pp (agent skill benchmark)
- autoresearch val_bpb metric (training loss)
- **graphify 71.5x** (token compression)

**Pattern #8 (Empirical Research Emergence) reinforced** — quantitative benchmarks increasingly published by frameworks.

## 5. 15-platform install surface (corpus-broadest)

### Direct skill installation

1. **Claude Code** (primary)
2. **Codex** (OpenAI)
3. **OpenCode** (open-source)
4. **Cursor**
5. **GitHub Copilot CLI**
6. **VS Code Copilot Chat**
7. **Gemini CLI** (Google)
8. **Aider**
9. **OpenClaw** ← cross-wiki runtime standard (4th wiki mentioning)
10. **Factory Droid**
11. **Trae** (standard + CN variant)
12. **Hermes** ← cross-wiki runtime standard (3rd wiki mentioning)
13. **Kiro IDE/CLI**
14. **Google Antigravity**

**Total: 15 platform targets** — broadest agent integration in corpus.

### Significance

- **Agent-runtime standards validated via install** — OpenClaw + Hermes both get dedicated install paths, confirming they're real runtimes (not just mentioned)
- **Pattern #18 (Agent Runtime Standardization) reinforced** — 4 wikis now mention OpenClaw; 3 mention Hermes; graphify adds execution-level evidence
- **BYO-skill-for-BYO-agent** — graphify positions as universal skill layer across BYO-agent ecosystem

### Install command pattern

```bash
pip install graphifyy
graphify [platform] install
```

Per-platform install writes skill to platform-specific location (e.g., `~/.claude/skills/graphify/` for Claude Code).

## 6. Commands reference (verbatim from README)

### Core invocation

```bash
/graphify                          # Current directory
/graphify ./path                   # Specific folder
/graphify ./path --mode deep       # Aggressive inference extraction
/graphify ./path --update          # Merge into existing graph
/graphify ./path --directed        # Preserve edge direction
/graphify ./path --cluster-only    # Recalculate communities only
/graphify ./path --no-viz          # Skip HTML output
/graphify ./path --obsidian        # Generate Obsidian vault
/graphify ./path --watch           # Auto-sync on file changes
/graphify ./path --wiki            # Build agent-crawlable wiki
/graphify ./path --svg             # Export SVG
/graphify ./path --graphml         # Export GraphML
/graphify ./path --neo4j           # Generate Cypher
/graphify ./path --neo4j-push bolt://host:port  # Push to Neo4j
```

### URL fetching

```bash
/graphify add <url>                # Fetch paper/tweet/video
/graphify add <url> --author "Name" --contributor "Name"
```

### Query operations

```bash
/graphify query "question"         # Terminal graph query
/graphify query "question" --dfs   # Trace specific paths
/graphify query "question" --budget 1500
/graphify path "Node1" "Node2"    # Shortest path between nodes
/graphify explain "NodeName"       # Plain-language node explanation
```

### Git integration

```bash
graphify hook install              # Post-commit + post-checkout
graphify hook uninstall
graphify hook status
```

### Platform install

```bash
graphify [platform] install        # Platform-specific always-on rules
```

## 7. Output directory structure

```
graphify-out/
├── graph.html          (interactive vis.js visualization)
├── graph.json          (canonical JSON export)
├── GRAPH_REPORT.md     (markdown summary)
├── obsidian/           (if --obsidian)
├── wiki/               (if --wiki)
│   └── index.md
├── cache/              (extraction cache for --update)
└── ...
```

**Meta-observation:** `wiki/index.md` structure = **parallel to Storm Bear vault's `(C) index.md` pattern**. Graphify produces LLM-Wiki-style output automatically.

## 8. CJK-trio localization (corpus-first)

### Translation coverage

| Language | File | Status |
|----------|------|--------|
| English | README.md | Primary |
| Japanese | README.ja-JP.md | Full translation |
| Korean | README.ko-KR.md | Full translation |
| Chinese Simplified | README.zh-CN.md | Full translation |
| Vietnamese | — | Not present |

### Corpus context

- **CJK-trio first in corpus** — only project with ja + ko + zh-CN together
- Prior CJK: deer-flow v9 (zh-CN), multica v15 (zh-CN)
- Prior VN: goclaw v4 (vi-VN), BMAD v11 (vi-VN), codymaster v12 (vi-VN author-native)
- **graphify has NO VN** — unusual given corpus trend; signals Japanese/Korean developer market as primary non-EN target

### Localization quality

Phase 2 cannot verify ja/ko translation quality natively. Assumption: at par with README main. If machine-translated, honest correction needed at Phase 2 re-read (parallel to BMAD v11 VN downgrade).

## 9. Tech stack (from README)

- **NetworkX** — Python graph library (standard)
- **Leiden algorithm** via **graspologic** — community detection
- **tree-sitter** — AST parsing for 25 languages
- **Claude** — subagent extraction + vision
- **vis.js** — interactive HTML visualization
- **faster-whisper** — local audio/video transcription
- **No Neo4j required** — optional export only
- **No server** — runs locally
- **No vector DB** — graph-topology replaces embeddings

### Python 100% — pyproject.toml driven

- Package name on PyPI: **`graphifyy`** (double-y; unique)
- Python 3.10+ required
- CLI entry point: `graphify`

## 10. Target audience (from README tone)

1. **Developers on large codebases** — navigation + architectural understanding
2. **Researchers with mixed media** — papers + tweets + screenshots + notes (Karpathy's /raw use case)
3. **Teams sharing architectural knowledge** — persistent graph vs ad-hoc explanations

**Not targeted:**
- Non-coding users (product-oriented)
- Pure data analysts (not SQL-style)
- Enterprise with strict data-residency (unclear how vision calls handle sensitive data)

## 11. Corpus-first observations

- **Broadest platform install surface** (15 targets)
- **CJK-trio README** (first in corpus — ja + ko + zh)
- **MCP server built-in first-class** (first explicit MCP output in corpus)
- **Graph-topology clustering without embeddings** (novel architecture)
- **2nd Karpathy-linked wiki** (after autoresearch v10)
- **Wiki generation built into tool** (self-referential — graphify makes LLM-Wiki-style output)
- **Obsidian vault export** (direct Storm Bear applicability)

## 12. Cross-references

- [[(C) ARCHITECTURE + AGENTS + SECURITY cluster summary]] — technical substrate
- [[(C) Integration + Packaging + 15 Platforms cluster summary]] — distribution detail
- [[(C) Knowledge Graph for AI Coding Assistants]] (entity)
- [[(C) Karpathy-Inspired Raw-Folder Problem + Meta-Cycle Extension]] (entity)

## 13. Open questions raised

- Q21: Is penpax.ai commercial? (unclear from README)
- Q22: Multi-vision-model support beyond Claude? (README implies Claude-primary)
- Q27: Benchmark methodology published? (71.5x claim needs reproducibility)
- Q29: Has Karpathy engaged? (unknown)
