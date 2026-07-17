# Historical Timeline — 70 years of data structures

**Source:** [video](https://www.youtube.com/watch?v=uHpzKcm8qh0) 02:47 "Lịch sử 70 năm" + per-structure sections · `raw/2026-07-17-data-structures-16-in-32-min.md`
**Verification:** every date/name below is ground-truthed in [[claims-scorecard]] (Workflow `wf_83c9b13a-5b9`, WebSearch against Wikipedia / ACM / primary papers).

The video's spine is that these inventions are **decades apart** yet now "stand together in one video." Chronological, verified:

## Pre-computing (maze theory → DFS)

- **~1880s** — **Charles Pierre Trémaux** devises a maze-solving method (the seed of depth-first search).
- **1881 / 1883** — **Édouard Lucas** reports Trémaux's method (*Récréations Mathématiques*, vol. 1 dated **1882**) and poses the maze problem (**1883**).
- **1895** — **Gaston Tarry** formalizes a systematic maze procedure — the third link in the DFS chain. *(The video's captions garble "Tarry" as "Cherry" — see [[caveats-and-corrections]].)*

## The notation

- **1894** — **Paul Bachmann** introduces **Big-O** (*Analytische Zahlentheorie*, vol. 2); "O" = *Ordnung* (order).
- **1909** — **Edmund Landau** adopts + refines it (adds little-o); hence "Landau symbols."
- **~1970s** — **Donald Knuth** brings Big-O into computer science for algorithm analysis.

## The structures (1945 → 1996)

| Year | Structure | People / place |
|---|---|---|
| **1945** | **Array** lineage | von Neumann, *First Draft of a Report on the EDVAC* (sequentially-numbered memory) |
| **1945** | **BFS** | Konrad Zuse, in a rejected PhD thesis (published only **1972**) |
| **1946** | **Stack** anticipated | Turing's ACE report — `BURY`/`UNBURY` for subroutine calls |
| **1953 (Jan)** | **Hash table** | Hans Peter Luhn, IBM internal memo (buckets + chaining) |
| **1955–56** | **Linked list** | Newell, Shaw & Simon @ RAND — IPL / "NSS memory" for the Logic Theorist |
| **1955** | **Stack** ("Kellerprinzip") | Bauer & Samelson @ TU Munich (patent filed **1957**, granted 1971) |
| **1956** | **Kruskal's MST algorithm** | Joseph Kruskal @ Bell Labs (drives [[disjoint-set|union-find]]) |
| **1959** | **BFS** reinvented | Edward F. Moore — shortest path through a maze |
| **1959** | **Trie** first described | René de la Briandais (Western Joint Computer Conference) |
| **1960** | **Trie** named | Edward Fredkin, "Trie Memory" (CACM) — from re**trie**val |
| **1962** | **AVL tree** (first self-balancing BST) | Adelson-Velsky & Landis |
| **1964** | **Heap** | J.W.J. Williams (Heapsort, ACM Algorithm 232); Floyd improves heapify |
| **1964** | **Union-find** | Galler & Fischer (CACM, "An Improved Equivalence Algorithm") |
| **1970** | **Bloom filter** | Burton H. Bloom |
| **1970→1972** | **B-tree** | Bayer & McCreight @ Boeing (circulated 1970, published 1972) |
| **1972** | **Symmetric binary B-tree** (→ red-black) | Rudolf Bayer |
| **1973** | Union-find first bound | Hopcroft & Ullman |
| **1975** | Union-find near-constant bound (inverse-Ackermann) | Robert Tarjan (Turing Award laureate) |
| **1978** | **Red-black tree** | Guibas & Sedgewick @ Xerox PARC (rename of Bayer's structure) |
| **1990** | **Skip list** | William Pugh (CACM) |
| **1996** | **LSM-tree** | O'Neil, Cheng, Gawlick & O'Neil (Acta Informatica) |

## Notable threads

- **IBM + Bell Labs + RAND + Xerox PARC + Boeing + academia** — no single institution owns the canon.
- **Publication lag is a recurring theme:** Zuse's BFS (1945) waited 27 years to publish; Moore (1959) got the practical credit. Bauer & Samelson's stack patent (filed 1957) granted only in 1971.
- **Names encode people:** AVL = Adelson-**V**elsky + **L**andis; the linked list was once "**NSS** memory" (Newell-Shaw-Simon).

## Key Takeaways

- The 16 structures span **~1894 (Big-O) → 1996 (LSM)**, roughly the "70 years" the video claims (structures proper: 1945→1996).
- **DFS predates computing** (Trémaux/Lucas/Tarry maze theory, 1880s–1895).
- Two structures had major **publication lags** (BFS/Zuse; stack patent) — invention ≠ credit.
- All dates verified against primary/scholarly sources — [[claims-scorecard]].
