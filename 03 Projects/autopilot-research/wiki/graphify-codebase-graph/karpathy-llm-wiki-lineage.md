# Graphify & Karpathy's LLM Wiki — the lineage (deep-dive into the original idea)

> **Source:** [[graphify-codebase-graph/_index]]. This is the **"double deep-dive into the original resource"** for this topic — and it matters more to *you* than to most viewers, because **Karpathy's LLM Wiki pattern is the foundation your entire vault is built on** (see the project `CLAUDE.md`).

## The attribution truth (verified, skeptical)

The video says Graphify *"came out of Andrej Karpathy mentioned publicly."* That's **overstated**. Three distinct facts get conflated — here they are, separated:

1. **Karpathy published the LLM Wiki pattern** (X / Twitter, early April 2026). His intellectual contribution: a **three-layer architecture** — `raw/` (immutable sources) → `wiki/` (LLM-generated pages) → `CLAUDE.md` (operational schema/librarian rules). ✅ Confirmed (in the [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f); your vault cites it directly).
2. **Safi Shamsi built Graphify ~48 hours later** as an *independent implementation inspired by* that idea. ✅ Confirmed (repo created 2026-04-03; "the tool Karpathy said someone should build" went viral via a 12K-like tweet).
3. **Karpathy did NOT create, build, or formally endorse Graphify.** ✅ Confirmed. Community enthusiasm ≠ Karpathy's voice.

> ⚠️ Two specific corrections: the phrase *"a pile of mixed content you can never fully reconstruct"* is **Graphify's marketing copy, NOT a Karpathy quote.** And "came out of Karpathy" should read **"inspired by Karpathy's published pattern."** If anyone says Graphify is "Karpathy's project," that's false.

## Karpathy's LLM Wiki, in his own framing

- **Problem:** *"the LLM is rediscovering knowledge from scratch on every question. There's no accumulation."*
- **Solution:** *"the LLM incrementally builds and maintains a persistent wiki."*
- **Human/AI split:** humans do *"sourcing, exploration, and asking the right questions"*; the LLM does *"summarizing, cross-referencing, filing, and bookkeeping."*
- **Why it stays maintained:** *"LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero."*
- **No vector DB** until scale forces it; `index.md` is the retrieval entry-point, `log.md` is append-only.

## Graphify ≈ the LLM Wiki, **automated** (and narrowed)

| Dimension | Karpathy LLM Wiki (your vault) | Graphify |
|---|---|---|
| **Build** | Hand-curated by an LLM *librarian*, one source at a time | **Automated** 3-pass extraction (tree-sitter + Whisper + LLM) |
| **Artifact** | Markdown `wiki/` pages + `_index.md` (prose synthesis) | `graph.json` (NetworkX) + `GRAPH_REPORT.md` (structural map) |
| **Relationships** | Hand-written `[[wiki links]]` | **Auto-extracted edges** (confidence-tagged) + Leiden communities |
| **Retrieval** | Agent reads `_index.md` → drills into articles | Agent reads `GRAPH_REPORT.md` → queries `graph.json` |
| **Strength** | **Curated synthesis, judgment, narrative** | **Speed, completeness, structural coverage** |
| **Weakness** | Slow; manual upkeep | **Structure ≠ understanding** — a graph maps *what connects*, not *why it matters* |

> **The key insight for you:** these are **complementary, not competing.** Graphify gives you, in minutes, the *structural skeleton* (god nodes, communities, surprising cross-links) that your librarian would otherwise discover slowly by hand. Your librarian then does what Graphify can't: **curate, synthesize, decide what matters, write the prose.** Graphify is a **scout**, not a replacement for the cartographer.

## Where this lands on your memory map

- On the 6-level taxonomy ([[claude-code-memory-systems/_index]]), Graphify is an **automated L3/L5 hybrid**: a knowledge graph (richer than L1/L2 markdown, not a vector DB like L3's MemSearch, not a hand-built wiki like L5). It's hook-injected at session start (the L2-L4 mechanism).
- Your vault is **L5 (LLM Wiki)** — *built by hand*. Graphify would be the **machine that pre-drafts the graph layer** for that wiki.

## The honest tension (worth keeping in view)

The sister memory video (Simon Scrapes) argues an LLM Wiki is **"a knowledge base, not operational memory"** — a real challenge to the vault thesis. Graphify sits in between: it's an *operational structural map* of a codebase, generated fast, but it is **not curated synthesis**. So:
- Don't expect Graphify's `GRAPH_REPORT.md` to replace your curated wiki articles — it's a map, not an essay.
- Do consider it as a **feeder**: auto-graph → your librarian reviews → promotes the genuinely-insightful connections into curated articles.

## Key Takeaways

- Graphify is **inspired by** Karpathy's LLM Wiki — *not* built or endorsed by him. The "pile of mixed content" line is Graphify's marketing, not a Karpathy quote.
- Karpathy's pattern = **humans ask, LLM maintains; raw/ → wiki/ → CLAUDE.md; no vector DB.** It's literally your vault's foundation.
- Graphify **automates a narrow slice** of that (structural extraction) but **can't do curation/synthesis** — it's a scout, not a cartographer.
- The productive frame: **auto-graph as a feeder into your hand-curated wiki**, not a replacement for it.
