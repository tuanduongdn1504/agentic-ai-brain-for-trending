# RAG — Retrieval-Augmented Generation (Ch. 6, part 1)

## Source

Video sections "Why Context Matters" → "Improving RAG Quality" + Huyen *AI Engineering* Ch.6 (RAG and Agents). See [[overview]], [[agents-and-memory]], [[source-provenance]].

## Why context matters

- **Many AI failures happen because the model doesn't have the right information.** Without context, answers are generic, hallucination-prone, weakly personalized, and miss current/domain facts.
- With good context: more relevant, better factual grounding, stronger domain performance, adapted to your tone/style/output. **Context can come from** retrieved documents, user data, tools, structured systems, state, and the prompt.
- RAG's purpose (Huyen, Ch.6): it "addresses context-window limitations and improves response quality while reducing costs." It "helps when the model needs facts it did not memorize or that change over time" — e.g. **your private business data a foundation model could never know.**

## Basic RAG architecture (the 2-step loop)

`User query` → **Retriever** (pull relevant chunks from a vector store / document corpus) → find similarity between query and chunks → pick the relevant chunks → **prompt the model with the retrieved context** → grounded answer.

> Two-step: **retrieve relevant info, then generate** using it. Both RAG and agents are **"prompt-based"** — they influence output through inputs *without modifying model weights* (contrast with [[finetuning-dataset-inference]]).

## The RAG data pipeline — offline vs online

**Offline indexing** (build the knowledge base ahead of time):
`Document sources (PDFs, DBs)` → **clean & parse** (drop boilerplate; keep abstract/sections/text) → **chunk** (by section / characters / pages — *no single method works for all data*) → **embedding model** turns each chunk into a vector → store in a **vector store / index**.

**Online query time** (when the user asks):
`User query` → embed into the **same vector space** → retrieve relevant chunks → **re-ranker / filter** picks the best ones → **inject into the prompt** as context → model generates.

> "A good RAG starts with clean documents, strong chunks, and reliable indexing." Expect to **experiment** — there's no single best chunking method, embedding model, or vector store.

## Retrieval methods (Ch.6 "Retrieval Algorithms")

| Method | What it does | Best for |
|---|---|---|
| **BM25 / keyword (term-based)** | matches exact words | rare terms, IDs, exact titles, simple/cheap baselines (Elasticsearch-class) |
| **Embedding / semantic** | understands meaning, not just words | paraphrases, where wording differs from the query |
| **Hybrid** | combines keyword + semantic, scores + merges | **usually strongest in practice** — best recall *and* precision |

> Huyen: term-based retrievers (BM25, Elasticsearch) are a **lighter baseline**; embedding-based retrievers have **higher potential performance**. The video's advice: *start simple, then test BM25, semantic, and hybrid on your own data.*

## Improving RAG quality (Ch.6 "Retrieval Optimization")

Most RAG gains come from **improving retrieval and context quality** (garbage context → garbage output). Levers:

- **Better chunking** — split into useful units; depends entirely on data type (paper vs book vs spreadsheet).
- **Query rewriting** — turn vague/misspelled questions into stronger searches.
- **Metadata** — filter by author/country/date/etc. to narrow fast (e.g. "last 20 American authors" → filter by country, don't scan everything).
- **Re-ranking** — reorder retrieved results by relevance; surface the best chunks.
- **Evaluation loops** — measure what actually helps. *Eval is always part of a RAG system* (see [[evaluation]]).

> *Treat RAG as a system to optimize, not just a vector-search add-on.* Ch.6 also notes **RAG beyond text** (retrieving over images, tables, multimodal data).

## RAG failure modes (the video's checklist)

1. **Missing documents** — the source isn't in the corpus (can't answer what you don't have).
2. **Bad chunks** — too large/small or poorly split → meaning lost.
3. **Weak retrieval** — the right content isn't returned.
4. **Poor ranking** — relevant content buried below weaker results.
5. **Stale knowledge** — documents outdated.
6. **Unsupported answer** — the model claims more than the context supports.

> **RAG reduces hallucination — but only when retrieval and grounding are strong.** Weak retrieval just hallucinates with extra steps.

## Key Takeaways

- **Context is the difference between generic and grounded.** RAG injects facts the model never memorized or that change over time — including your private data.
- The pipeline is **offline (clean → chunk → embed → index)** + **online (embed query → retrieve → re-rank → prompt)**.
- **Retrieval = BM25 (exact) vs embeddings (meaning) vs hybrid (usually best).** Test all three on *your* data.
- Most quality gains are in **retrieval**: chunking, query-rewriting, metadata filters, re-ranking, eval loops.
- **RAG only reduces hallucination when retrieval is good** — most RAG failures are retrieval failures.

## Cross-links

- [[agents-and-memory]] — agents extend RAG with planning + tools + memory
- [[foundation-models]] (embeddings) · [[evaluation]] (evaluate the retriever) · [[prompt-engineering-and-guardrails]] (retrieved content is untrusted)
- [[../claude-code-memory-systems/_index]] — RAG as a memory layer (L3 semantic / L5 knowledge-base); **this vault is itself a hand-curated RAG**
- [[../graphify-codebase-graph/_index]] — graph-based retrieval as an alternative to vector RAG · [[../claude-api-cost-optimization/_index]] (RAG reduces cost vs stuffing context)
