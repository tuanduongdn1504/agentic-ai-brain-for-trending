# graphify - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`safishamsi/graphify`](https://github.com/safishamsi/graphify) — **"AI coding assistant skill. Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph."** **30K stars, 3.3K forks, MIT, v0.4.23 (April 18, 2026), 169 commits (v4 branch), 124 watchers, 44 open issues**. Python 100%. Author: **safishamsi** (solo maintainer). Homepage: penpax.ai (related product brand).

**Positioning:** *"A Claude Code skill. Type `/graphify` in Claude Code — it reads your files, builds a knowledge graph, and gives you back structure you didn't know was there."*

**Karpathy explicit inspiration:** *"Andrej Karpathy keeps a `/raw` folder where he drops papers, tweets, screenshots, and notes. graphify is the answer to that problem."* → **2nd Karpathy-connected wiki in corpus** (after autoresearch v10, Karpathy's own).

**Tech stack — novel:** NetworkX + Leiden (graspologic) + tree-sitter (25 languages) + Claude vision + vis.js + faster-whisper + **MCP server built-in**. **Graph-topology clustering WITHOUT embeddings** — no vector DB needed.

**Tier placement:** **T4 "Agent-as-bridge" extended at N=3** — graphify bridges local filesystem content to agents (parallel to gws + notebooklm-py bridging external services). 

**Critical milestone:** **T4 multi-entrant EXTENDED to N=3** (gws + notebooklm-py + graphify). **All 5 tiers validated** pending (T3 still at N=1 only).

**Pattern #9 T4 test at N=3:**
- T4a official-corporate-broad: gws (Google, 11+ services)
- T4b unofficial-solo-narrow: notebooklm-py (teng-lin, single service)
- T4c **solo-open-general-purpose: graphify (safishamsi, filesystem not specific service)** — new subcategory candidate
- Or: graphify extends T4b (solo-broad vs solo-narrow differentiation)
- **First T4 3-way test of Pattern #9**

**Cross-wiki agent-runtime signals REINFORCED:**
- OpenClaw now in **4 wikis** (codymaster v12 + paperclip v14 + multica v15 + graphify v16) — **Pattern #18 strengthened**
- Hermes now in **3 wikis** (paperclip v14 + multica v15 + graphify v16) — **Pattern #18 strengthened**
- Graphify ships install-paths for OpenClaw + Hermes → validates them as real runtimes (not just mentioned)

**Meta-cycle extension:** Karpathy explicit inspiration = **2nd Karpathy-connected wiki**. autoresearch v10 was his own; graphify cites him. Corpus touches Karpathy intellectual lineage twice.

**Phase 4b routing = T4 3-way comparison** (gws + notebooklm-py + graphify). Parallel to T5 3-way v14 paperclip. Tests Pattern #9 at T4 with 3 data points.

## Claude's Role

Claude là wiki maintainer, chạy bằng routine `llm-wiki-routine` v1 (**16th auto-execution — T4 N=3 extension + 2nd Karpathy connection + agent-runtime-standards validated by install surface**):

- **Ingest sources via WebFetch** — README (+ ja-JP + ko-KR + zh-CN) + ARCHITECTURE.md + AGENTS.md + SECURITY.md + pyproject.toml
- **Cross-reference với 15 sibling wikis** — gws v13 (T4 N=1 direct 3-way peer) + notebooklm-py v7 (T4 N=2 direct 3-way peer) + autoresearch v10 (Karpathy meta-cycle peer) + multica v15 + paperclip v14 (agent-runtime standards)
- **Phase 4b = T4 3-way comparison** — validates T4 triple; tests Pattern #9 refinement at T4 third-entrant
- **Beginner roadmap** — angle: graphify as SKILL installable to 15 platforms; low barrier + high structural value; Storm Bear vault direct applicability (graphify Storm Bear vault itself to generate knowledge graph of wiki ↔ entity ↔ cross-references)

**Prime directive:** Outcome = wiki + T4 3-way comparison + document Pattern #9 T4 3-way test + document agent-runtime-standards install-surface confirmation + Karpathy meta-cycle second touchpoint.

## Process — routine `llm-wiki-routine` v1

7 phases. Continuous execution. Phase 4b = **T4 3-way comparison** (structurally parallel T5 3-way v14).

## Key People / Organization

- **safishamsi** — solo creator/maintainer (named in README + inferred from repo ownership)
- **Andrej Karpathy** — cited inspiration (raw-folder problem)
- **7 total contributors** listed on GitHub
- **Homepage:** penpax.ai (safishamsi's product brand; possibly commercial overlay)
- **No VC/corp disclosed**
- **Cross-project:** 15 sibling wikis. This is 16th = T4 N=3 + 2nd Karpathy connection.

## Folder Structure

```
graphify - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md
├── 00-07 folders
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ + 13-section format
- **Cross-reference 15 siblings MANDATORY** — especially gws v13 + notebooklm-py v7 (T4 peers) + autoresearch v10 (Karpathy peer)
- **Document agent-runtime-standards install confirmation** — graphify ships install paths for OpenClaw + Hermes = real targets
- **Pattern #9 T4 3-way test** — third T4 entrant tests whether corporate/solo bifurcation holds OR refines to solo-narrow/solo-broad subsplit
- **Storm Bear direct applicability** — graphify on Storm Bear vault itself = immediate action item

## Positioning note

**graphify trong taxonomy v4 (v16 update):**

| Tier | Frameworks (n=16 now) | v16 change |
|------|----------------------|------------|
| T1: Agent-as-assistant | ECC, Superpowers, gstack, GSD, BMAD, codymaster (6) | — |
| T2: Agent-as-service | goclaw, multica (2) | — |
| T3: Agent-as-education | course (1) | **Still only single-entrant tier** |
| **T4: Agent-as-bridge** | **notebooklm-py, gws, graphify (3 ← N=3 EXTENSION)** | **✅ Third entrant; extends to N=3** |
| T5: Agent-as-application | deer-flow, autoresearch, paperclip (3) | — |
| Outside scope | build-your-own-x (1) | — |

→ **T4 joins T5 at N=3**, matching tiers. **Only T3 pending**.

### T4 3-way preview

| Axis | gws (v13) | notebooklm-py (v7) | graphify (v16) |
|------|-----------|--------------------|----------------| 
| **Stars** | 25K | ~300 | **30K** |
| **License** | Apache-2.0 | MIT | **MIT** |
| **Primary lang** | Rust 98.8% | Python | **Python 100%** |
| **Author org** | Google (official) | teng-lin (solo) | **safishamsi (solo)** |
| **Bridge target** | Google Workspace (11+ services) | NotebookLM (1 service) | **Local filesystem (any content)** |
| **Scope** | Broad corporate | Narrow solo | **Broad solo** |
| **Agent integration** | CLI + skills | Library + CLI + Skill | **Skill installable to 15 platforms** |
| **MCP server** | — | — | **Built-in** |
| **Community size at solo** | N/A | ~300 stars | **30K stars (scale outlier for solo)** |

## Unique positioning claims của graphify (từ Phase 0)

- **30K stars, solo maintainer** = scale outlier for solo archetype (compare notebooklm-py ~300)
- **Karpathy explicit inspiration** — /raw folder problem cited verbatim
- **71.5x token reduction** on 52-file mixed corpus = research-style benchmark
- **15 agent-platform install targets** — broadest agent-integration surface in corpus
- **Graph-topology clustering without embeddings** — novel architecture; no vector DB
- **25 programming languages** via tree-sitter AST parsing
- **Multimodal** — code + docs + papers + images + videos (whiteboard photos, screenshots, arxiv links, twitter URLs)
- **Multi-language README** — en + ja-JP + ko-KR + zh-CN (**CJK-trio first in corpus**)
- **MCP server built-in** — `python -m graphify.serve` exposes query_graph/get_node/get_neighbors/shortest_path
- **Wiki generation** — `--wiki` flag produces Wikipedia-style articles (meta: graphify generates LLM Wikis!)
- **Obsidian vault export** — `--obsidian` (meta: Storm Bear uses Obsidian)
- **Neo4j export** — optional (`--neo4j`, `--neo4j-push bolt://...`)
- **Git hooks** — auto-rebuild on commit
- **Confidence taxonomy** — EXTRACTED / INFERRED / AMBIGUOUS edge labels
- **Local-first** — runs entirely locally; no server; no vector DB
- **MIT + open source** — permissive
- **PyPI package: `graphifyy`** (double-y, typo-resistant naming?)
- **169 commits / v4 branch** — suggests major-version branching
- **Homepage: penpax.ai** — author's product brand

## Current Status

> **Last updated:** 2026-04-19
> **Status:** 🟡 Routine auto-execute IN PROGRESS — 16th LLM Wiki, T4 N=3 extension

### Expected milestones

- [x] Phase 0 Pre-flight (API probe, 30K stars, T4 N=3 extension, Karpathy 2nd-connection)
- [ ] Phase 1 Setup
- [ ] Phase 2 Source ingestion (3 — README multi-lang / ARCHITECTURE+AGENTS+SECURITY / Integration+packaging+releases)
- [ ] Phase 3 Entity pages (4 — Knowledge Graph core product / 15-Platform Install + Agent-Runtime Standards / Karpathy-Inspired Raw-Folder Problem / T4 3-way + Pattern #9 test + Storm Bear meta)
- [ ] Phase 4a Beginner published guide bilingual
- [ ] Phase 4b **T4 3-way comparison** (gws + notebooklm-py + graphify; tests Pattern #9)
- [ ] Phase 5 Iteration log v16
- [ ] Phase 6 Vault file updates
