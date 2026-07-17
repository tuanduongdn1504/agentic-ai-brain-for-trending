# Data Structures — 16 in 32 Minutes

**A Vietnamese explainer walking through 16 classic data structures — each with its Big-O, its historical origin (inventor + year), and a closing "task → structure" selection framework — verified claim-by-claim against primary CS-history sources.**

- **Source:** [Tất Tần Tật Về Cấu Trúc Dữ Liệu Trong 32 Phút](https://www.youtube.com/watch?v=uHpzKcm8qh0) · Học Giải Thuật Cùng HPN · 2026-07-12 · 32:22 · VN
- **Ingested:** 2026-07-17 (path 5 yt-dlp; full transcript read in main loop) · raw: `raw/2026-07-17-data-structures-16-in-32-min.md`
- **Verification:** Workflow `wf_83c9b13a-5b9` (10 agents, 0 errors) → **22 CONFIRMED / 1 ANECDOTAL / 1 CORRECT-BUT-INCOMPLETE / 0 FALSE / 0 FABRICATED** — one of the highest-integrity sources in the corpus.
- **Corpus first:** the wiki's **first pure CS-fundamentals topic** (2nd non-Claude/non-agent topic).

## The one framing

**16 answers to a single question — "how should this data be arranged so the task gets easier?"** No structure wins absolutely; you choose by workload. And the structures **compose** (a heap is an array; a tree is a graph without cycles; hash collisions resolve into a linked list).

## Articles

### Concepts
- [[overview]] — the one framing, the grouping, the recurring "no structure wins" thesis.
- [[big-o-primer]] — the measuring stick (O(1)/O(log n)/O(n)/O(n²)); Bachmann→Landau→Knuth; what Big-O hides.

### The 16 structures (grouped)
- [[linear-structures]] — array, linked list, stack (LIFO), queue (FIFO).
- [[hashing]] — hash table: O(1) lookup by arbitrary key; collisions.
- [[balanced-trees]] — BST → its degeneration → AVL & red-black fixes.
- [[heap-and-priority]] — heap: always know the top; array-backed.
- [[graph-and-traversal]] — graph + BFS (queue) vs DFS (stack).
- [[string-trie]] — trie: prefix / autocomplete, O(string length).
- [[disjoint-set]] — union-find: "same group?" near-instant; Kruskal's MST.
- [[probabilistic]] — skip list & bloom filter: trade certainty for speed/space.
- [[disk-scale]] — B-tree (read-optimized) & LSM-tree (write-optimized).

### Synthesis
- [[historical-timeline]] — the full ~1894→1996 chronology, verified.
- [[selection-framework]] — the task→structure decision table + complexity cheat-sheet.
- [[beyond-the-video]] — honest gaps: amortized-vs-worst-case, cache effects, implementation variants, composition, concurrency.

### Verification & relevance
- [[claims-scorecard]] — the 24-claim CS-history/Big-O verification.
- [[caveats-and-corrections]] — ASR garbles + the contested red-black anecdote + minor date nuances.
- [[critical-appraisal]] — is this a good way to learn? (survey vs. implementation; who it's for).
- [[corpus-and-hireui-relevance]] — cross-links graded (thematic vs. content); the 4–6 structures hireui's matching feature actually uses.
- [[source-provenance]] — ingestion + verification method.

## Cross-links

- **Content:** [[graphify-codebase-graph/_index]] (graphs + Leiden algorithm).
- **Thematic (fundamentals thread):** [[pocock-software-fundamentals/_index]], [[quanit-becoming-ai-engineer-2026/_index]], [[system-thinking-ai-coding/_index]].
- **Structural sibling:** [[self-hosted-devops-oss/_index]] (other non-agent topic).
