# (C) Index — graphify Wiki

## 🎯 Project status (2026-04-19)

- ✅ Phase 0: Pre-flight
- ✅ Phase 1: Setup
- ✅ Phase 2: Source ingestion (3 cluster summaries)
- ✅ Phase 3: Entity pages (4)
- ✅ Phase 4a: Beginner published guide
- ✅ Phase 4b: T4 3-way comparison (extended T4 to N=3, refined Pattern #9 to multi-axial)
- ✅ Phase 5: Iteration log v16
- ✅ Phase 6: Vault file updates

**Repo:** safishamsi/graphify
- **Description:** "AI coding assistant skill. Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph"
- **Core tagline:** "A Claude Code skill. Type `/graphify` in Claude Code — it reads your files, builds a knowledge graph, and gives you back structure you didn't know was there"
- **Stats:** 30,000 stars, 3,300 forks, 169 commits (v4 branch), v0.4.23 (April 18, 2026), 124 watchers, 44 open issues, 7 contributors
- **Languages:** Python 100%
- **License:** MIT
- **Author:** safishamsi (solo)
- **Homepage:** https://safishamsi.github.io/penpax.ai
- **PyPI:** graphifyy (double-y)
- **Routine:** `05 Skills/llm-wiki-routine.md` v1 — 16th auto-execution, T4 N=3
- **Domain:** **Tier 4 "Agent-as-bridge" entrant #3** (bridges local filesystem to agents as knowledge graph)
- **Unique:** Karpathy-cited + 15-platform install + graph-topology-no-embeddings + 71.5x token reduction + MCP-server-built-in + CJK-trio README

## Sources (planned)

| Page | Summary | Status |
|------|---------|--------|
| [[(C) README + multi-language cluster summary]] | Positioning + features + commands + benchmarks + Karpathy inspiration + CJK translations | ✅ |
| [[(C) ARCHITECTURE + AGENTS + SECURITY cluster summary]] | Pipeline stages + confidence taxonomy + security layer + agent-docs convention | ✅ |
| [[(C) Integration + Packaging + 15 Platforms cluster summary]] | 15 install targets + pyproject.toml + versioning + release cadence | ✅ |

## Concepts (planned)

- **Agent skill** — installable capability package (skill-as-distribution-unit)
- **Knowledge graph** — nodes (files, concepts) + edges (EXTRACTED/INFERRED/AMBIGUOUS)
- **Graph-topology clustering** — Leiden algorithm; no embeddings; no vector DB
- **Multimodal extraction** — code (tree-sitter 25 langs) + PDFs + images + video + audio (faster-whisper)
- **Confidence taxonomy** — EXTRACTED (deterministic) / INFERRED (LLM deduction) / AMBIGUOUS (flagged)
- **71.5x token reduction** — compression ratio on 52-file mixed corpus
- **MCP server built-in** — query_graph / get_node / get_neighbors / shortest_path
- **Git hooks auto-rebuild** — post-commit automation
- **Multi-platform install** — 15 targets (Claude Code, Codex, Cursor, Gemini CLI, OpenClaw, Hermes, etc.)
- **Wiki generation** — `--wiki` produces Wikipedia-style articles per community
- **Karpathy /raw folder problem** — explicit inspiration citation
- **Local-first** — no server, no vector DB, runs locally

## Entities (planned)

| Page | Type | Sources | Status |
|------|------|---------|--------|
| [[(C) Knowledge Graph for AI Coding Assistants]] | Core product | README + ARCHITECTURE | ✅ |
| [[(C) 15-Platform Install + Agent-Runtime Standards Confirmed]] | Integration + ecosystem | README platform list + cross-wiki | ✅ |
| [[(C) Karpathy-Inspired Raw-Folder Problem + Meta-Cycle Extension]] | Meta-entity | README Karpathy quote + autoresearch v10 | ✅ |
| [[(C) T4 3-way Extension + Pattern 9 Test + Storm Bear]] | **Tier meta + Storm Bear** | T4 comparison + Pattern #9 history | ✅ |

## Roadmaps / Published

- ⏸ [[../03 Published/(C) graphify - Huong dan cho nguoi moi]] — beginner bilingual guide
- ⏸ [[../03 Published/(C) Tier 4 3-way comparison]] — extends T4 to N=3; tests Pattern #9; parallels T5 3-way v14

## Cross-project siblings (15 total)

- **T4 peers (2) — 3-way comparison targets:**
  - `../../googleworkspace-cli - Beginner Analysis/02 Wiki/(C) index.md` (v13 — official-corporate-broad)
  - `../../notebooklm-py - Beginner Analysis/02 Wiki/(C) index.md` (v7 — unofficial-solo-narrow)
- **Karpathy meta-cycle peer:**
  - `../../autoresearch - Beginner Analysis/02 Wiki/(C) index.md` (v10 — Karpathy's own)
- **Agent-runtime standards (OpenClaw + Hermes):**
  - codymaster v12 (OpenClaw only)
  - paperclip v14 (OpenClaw + Hermes)
  - multica v15 (OpenClaw + Hermes)
- T1: ECC, Superpowers, gstack, GSD, BMAD, codymaster (6)
- T2: goclaw, multica (2)
- T3: course (1)
- T5: deer-flow, autoresearch, paperclip (3)
- Outside: build-your-own-x (1)

## Logs

- [[(C) log]]
