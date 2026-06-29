# Level 4 — Verbatim recall: MemPalace

> **Source:** [[claude-code-memory-systems/_index]] · video [23:45–28:46] + deep-dive of [MemPalace](https://github.com/MemPalace/mempalace) (mempalaceofficial.com). **Local-first, free, the highest-fidelity recall in the taxonomy.**

**When you need L4:** when you catch yourself thinking *"I know we discussed this a few weeks ago, but I can't remember exactly what was decided."* Where L3 finds your **notes + a summary**, L4 finds **the exact words used** when a decision was made.

## What makes it different

- A **proper RAG system**, **stored entirely locally**, **free**.
- **Verbatim — nothing is summarized.** *"The content stays verbatim always."* So (in theory) nothing can be lost to summarization.
- **Vendor benchmark claims** (repo): raw semantic search **96.6% R@5** on LongMemEval (500 Qs); hybrid v4 pipeline **98.4% R@5**; with LLM rerank **≥99%**. The video's *"highest benchmark score of any memory system ever published, apparently"* is a **marketing claim — flagged** in [[claude-code-memory-systems/source-provenance]] ("apparently" is the author's own hedge).

## Architecture: two databases + a symbolic index

- **Two stores:**
  - a **SQLite** database — a *temporal entity-relationship graph* with validity windows (add / query / invalidate / timeline) tracking entities + their relationships;
  - a **ChromaDB** vector store (default; pluggable: `sqlite_exact`, `qdrant`, `pgvector`) — every conversation stored as searchable **verbatim chunks**.
- **The "AAAK" symbolic index** — a *"dense symbolic dialect an LLM can scan at a glance."* The index is written in this compact language so the model can **scan thousands of "drawers" in a single pass**; it's a set of pointers to where the real verbatim data lives. (Full AAAK syntax is **not documented** in public docs — flagged.)

## The memory-palace metaphor (the file structure)

Borrowing the ancient method of loci — content is filed hierarchically instead of in a flat corpus, so **searches can be scoped**:

| Palace level | Maps to |
|---|---|
| **Wings** | people / projects / topics |
| **Rooms** | day sessions / threads |
| **Closets / Drawers** | topics / threads / **the verbatim text itself** |

*Example from the docs:* "My son's name is Noah, he turns 6 on Sept 12, he loves dinosaurs" → indexed as a pointer (`Noah, son, age 6, DOB…`) → filed in e.g. *drawer 007, wing 42, room 11*. Two weeks later a query retrieves the exact drawer in **~42 ms** and returns the verbatim text.

## Hooks + install + retro-mining

- **Background hooks** silently store + index — filing happens on **`SessionEnd`** and **`PreCompact`** (fires right before compaction). Auto-save hooks support **Claude Code, Codex CLI, and Cursor**. (Exact hook identifiers aren't enumerated in docs — flagged.)
- **Install + init:**
  ```bash
  uv tool install mempalace        # or pipx / pip install mempalace
  mempalace init ~/projects/myapp  # creates .mempalace/ + registers hooks in settings.json
  ```
- **Retro-mine existing history** — index conversations you had *before* installing:
  ```bash
  mempalace mine ~/projects/myapp
  mempalace mine ~/.claude/projects/ --mode convos
  mempalace sweep <transcript-dir>
  ```
  Mining is **idempotent + resume-safe**. (33 MCP tools are referenced in the docs.)

## The cost of fidelity

- **Not plain markdown.** The verbatim text is locked in ChromaDB + the AAAK index — you **can't just open and read it** like L1/L2/L3/L5. You retrieve fast, but you lose human-readability/portability.
- Still **100% local** — like L1–L3, nothing leaves your machine (that's what L5/L6 change).

## Key Takeaways

- L4 = **local, free, verbatim** conversation recall — exact words, not summaries — for *"what exactly did we decide weeks ago?"*
- **Two stores:** SQLite entity-graph (with validity windows) + ChromaDB verbatim chunks, indexed by the compact **AAAK** symbolic language for fast single-pass scans.
- **Memory-palace metaphor**: wings (people/projects) → rooms (sessions) → drawers (verbatim text); scoped, not flat. ~42 ms retrieval demoed.
- **Background hooks** (SessionEnd / PreCompact) file silently; **`mine`** retro-indexes prior sessions, idempotently.
- **Trade-off:** highest recall fidelity, but **opaque** (not readable markdown). Benchmark "best ever" + AAAK details are **vendor-claimed / under-documented** — flagged.
