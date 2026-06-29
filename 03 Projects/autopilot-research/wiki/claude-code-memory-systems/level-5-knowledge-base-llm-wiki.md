# Level 5 — Self-organizing knowledge base: Karpathy's LLM Wiki

> **Source:** [[claude-code-memory-systems/_index]] · video [28:46–35:13] + **deep-dive of the original**: [Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) + the hosted [Recall](https://www.recall.it/) + enterprise [LightRAG]. **This is the pattern this entire vault runs on** — so this article also records the video's *critique* of it, which directly challenges the vault thesis.

**A different job.** Levels 1–4 + 6 are **operational memory** — remembering *your work*. Level 5 is about building a **researched, interconnected knowledge base** on topics you care about (articles, videos, podcasts, client notes) — a "second brain," not a work-log. Add it *only* if you regularly consume information you want to keep + connect.

## The original (Karpathy) — deep-dive

The pattern replaces traditional RAG with an **LLM-maintained persistent wiki**: a structured markdown layer between raw sources and you. Instead of re-deriving knowledge per query, the LLM **incrementally builds + maintains a wiki** — summaries, entity pages, cross-references, evolving synthesis.

**Three-layer architecture:**
1. **Raw sources** (immutable) — articles, papers, transcripts, PDFs, data. The LLM **reads but never writes** here.
2. **The wiki** — LLM-generated markdown: summaries, entity/concept pages, an overview, synthesis. The LLM **owns it completely** — *no human writes the wiki.*
3. **The schema** (e.g. `CLAUDE.md`) — defines structure, conventions, workflows; **evolves over time** with use.

**Operations (the verbs):**
- **Ingest** — add a source; LLM reads it, discusses takeaways, writes summary pages, updates the index, revises entity/concept pages, appends a log entry. *One source can touch 10–15 pages.*
- **Query** — ask a question; LLM reads the index, drills into relevant pages, synthesizes **with citations**. *Good answers become new wiki pages* — knowledge compounds.
- **Lint** — periodic health check: contradictions, stale claims, orphan pages, missing cross-refs, data gaps.

**Indexing + logging + retrieval:**
- **`index.md`** — a content catalog: every page + a one-line summary, by category. Updated on every ingest. **This is the retrieval mechanism** — at ~100 sources / hundreds of pages the LLM reads the index first, then drills in. **No vector DB required.** (At larger scale, add a hybrid search tool like `qmd` (BM25+vector+LLM rerank) via CLI/MCP.)
- **`log.md`** — append-only chronological record of ingests/queries/lints, consistently prefixed (`## [2026-04-02] ingest | Title`) for parseable history.

**Why it works (the load-bearing insight):**
> *"The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping."*

LLMs don't forget cross-references; they maintain consistency across dozens of pages in one pass. **Contradictions are flagged, not auto-resolved** — the human reviews genuine conflicts. (Karpathy frames it as finally solving the maintenance problem Vannevar Bush's 1945 *Memex* couldn't: *"The part he couldn't solve was who does the maintenance. The LLM handles that."*)

> **This is your vault.** raw/ + wiki/ + `_master-index.md` + per-topic `_index.md` + `[[wiki links]]` + the librarian rules + the compile/query/audit verbs + the loop-log = a faithful, *industrialized* implementation of this gist. See [[claude-code-memory-systems/your-current-setup-mapping]].

## The hosted alternative: Recall

**Recall** = "Karpathy's wiki done for you." Browser extension → save articles/podcasts/PDFs → it summarizes, tags, and **auto-builds the knowledge graph**; gives you an AI chat over your saved content; works on phone; has **MCP access** to connect Claude Code. Zero setup, no Obsidian.

**Why the video still prefers the DIY LLM Wiki for most people:**
1. **Ownership** — your data lives on Recall's servers (exportable to markdown, but you're *renting*).
2. **Built for content consumption, not operational memory** — great for *"I watched 40 videos on Claude Code; which one covered memory?"*; **not** for *"what did we decide about client X's landing page in March?"*
3. **Pricing** — it's paid SaaS.

Verdict: **non-technical + organizing articles/videos/podcasts → Recall.** Want maximum control + own your Wikipedia → **DIY LLM Wiki.**

## The heavyweight alternative: LightRAG

An **enterprise-grade knowledge graph** — heavier entity extraction, dual-level retrieval, research-grade. **"Overkill for 99% of business owners."** Skip unless you genuinely need that; otherwise go back to L4 or use the LLM Wiki / Recall.

## ⚠️ The video's critique of Level 5 — a real challenge to the vault thesis

The author is **openly skeptical that Level 5 belongs in an *operational* system**, and says so repeatedly:

- *"I can't see the directly applicable use cases for retrieving this information... inside a system like the Business OS or the Agent OS."*
- Best use case (quoting Connolly): a **"save for later"** pile — bookmarked threads, videos, notes you never revisit, where you want to *see the interlinking relationships*. I.e. **deep research on interconnected topics**, **not** running projects.
- Both LLM Wiki **and** Recall are *"for building knowledge bases, not for operational memory."*
- His personal stack: **up to Level 3 only.** L5 isn't in it.

**Why this matters to you (Rule 7 — surface, don't average):** your vault *is* L5, and you use it for exactly the job the video doubts. But note the **distinction is real, not a refutation**: this vault is explicitly the **research / knowledge layer**, and your *operational* memory is the separate `~/.claude/.../memory/` system (L1/L2). The video's critique actually **validates keeping them separate** — don't try to make the LLM Wiki do operational recall (that's what L2/L3 are for), and don't bloat your operational memory with research synthesis (that's what L5 is for). The honest counter to the author: L5 earns its keep precisely *because* you've matched it to research, and **layered L1/L2 underneath for operations** — the two-system split he'd actually endorse. (Corroborating signal: LangChain is **productizing** the LLM Wiki as "Context Hub" for exactly the research/agent-context job — [[agent-development-lifecycle/_index]].)

## Key Takeaways

- L5 = an **LLM-maintained markdown wiki** (raw/ read-only + wiki/ LLM-owned + an index), built for **researched knowledge bases**, *not* operational work-memory.
- The original's core claim: the bottleneck isn't reading/thinking, it's **bookkeeping** — and LLMs eliminate it (consistent cross-refs, flagged contradictions, compounding query→page).
- **Retrieval is the `index.md`** read first, then drill-in — **no vector DB** until scale demands one (`qmd`).
- **Recall** = hosted LLM Wiki (zero setup, MCP, but rented data + consumption-oriented); **LightRAG** = enterprise KG (overkill for most).
- **The video doubts L5 for operational systems** and personally stops at L3 — a genuine challenge to using a wiki as your work-memory. The resolution: **separate the research wiki (L5) from operational memory (L1/L2/L3)** — which is exactly the split this vault already runs.
