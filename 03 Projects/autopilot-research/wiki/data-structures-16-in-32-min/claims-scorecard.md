# Claims Scorecard — CS-history & Big-O verification

**Method:** every checkable date / inventor / complexity claim in the video was ground-truthed by a refute-first Workflow (`wf_83c9b13a-5b9`, 10 agents / ~378K tokens / 0 errors / 0 empty; all Haiku 4.5), each running WebSearch against Wikipedia, ACM/CACM, primary papers, and university CS-history pages, plus a dedicated nuance-hunter. Source: [video](https://www.youtube.com/watch?v=uHpzKcm8qh0).

## Tally (24 checkable claims)

**22 CONFIRMED · 1 ANECDOTAL · 1 CORRECT-BUT-INCOMPLETE · 0 MISLEADING · 0 FALSE · 0 FABRICATED**

→ **One of the highest-integrity sources in the corpus.** A well-researched CS-history explainer: essentially every inventor + year checks out against primary sources. The only two non-CONFIRMEDs are (a) a widely-repeated anecdote that has a competing account from the co-inventor, and (b) a one-year imprecision in a 19th-century citation. Neither is an error of substance.

## CONFIRMED (22)

| Claim | Verified against |
|---|---|
| Big-O introduced by **Paul Bachmann, 1894** (*Analytische Zahlentheorie*; "O" = *Ordnung*) | Wikipedia, MAA "Math Origins", MacTutor |
| **Landau, 1909** adopts/refines it (adds little-o; "Landau symbols") | Wikipedia, MAA |
| **Knuth** brings Big-O into CS, ~1970s (adds Ω, Θ) | Wikipedia, Pomona CS history |
| O(1)/O(log n)/O(n)/O(n²) growth characterizations correct (n² quadruples on doubling) | freeCodeCamp, GeeksforGeeks |
| **Array** ← **von Neumann 1945**, EDVAC draft (sequential indexed memory) | Wikipedia, Computer History Museum |
| **Hash table** ← **Hans Peter Luhn, IBM, Jan 1953** (buckets + chaining) | IEEE Spectrum, Wikipedia |
| **Stack "Kellerprinzip"** ← Bauer & Samelson, TU Munich ~1955, patent 1957; **Turing anticipated (ACE, 1946, BURY/UNBURY)** | Google Patents DE1094019B, Wikipedia, Springer |
| Array random access O(1); middle insert O(n) | Wikipedia, dev.to |
| **Linked list** ← **Newell, Shaw & Simon @ RAND, 1955–56**, IPL for the Logic Theorist | IRE Trans. 1956, Wikipedia |
| **Trie** ← de la Briandais 1959 (WJCC); **Fredkin 1960** coins "trie" (CACM "Trie Memory") | ACM, Wikipedia |
| **AVL** ← Adelson-Velsky & Landis **1962** (first self-balancing BST; initials) | academic sources |
| Balanced BST O(log n); sorted-insert degenerates to O(n) tail | standard CS |
| **Heap** ← **Williams 1964** (Heapsort, CACM Algorithm 232); Floyd improves heapify | NIST DADS, Wikipedia |
| **Union-find** ← Galler & Fischer 1964; Hopcroft-Ullman bound 1973; **Tarjan 1975** inverse-Ackermann | CACM 1964, SIAM 1973, JACM 1975 |
| **Bloom filter** ← **Burton Bloom 1970**; false positives yes, false negatives never | Wikipedia |
| Max-heap parent≥children, array-backed, children at 2i+1/2i+2, max at root | Wikipedia, Baeldung |
| **B-tree** ← **Bayer & McCreight @ Boeing**, circulated 1970, published **1972** | Wikipedia, Acta Informatica |
| **Skip list** ← **William Pugh 1990** (CACM); random coin-flip promotion | ACM DL |
| **LSM-tree** ← **O'Neil, Cheng, Gawlick, O'Neil 1996** (Acta Informatica; C0/C1) | Springer |
| **BFS** ← Zuse 1945 (rejected thesis, pub. 1972); **Moore 1959** reinvents (maze shortest path) | Wikipedia, Moore 1959 |
| **Kruskal's MST** ← Joseph Kruskal 1956 (Bell Labs); union-find skips cycle edges | Wikipedia, CMU |
| B-/B+-trees in **Btrfs, XFS, ext4 (HTree)** | HTree Wikipedia, filesystem comparisons |

## ANECDOTAL (1)

- **Red-black "red because of the laser printer."** Guibas & Sedgewick (Xerox PARC, 1978, from Bayer's 1972 symmetric binary B-tree) are correctly credited. But the color story has **two accounts from the authors themselves**: Sedgewick has said the Xerox color laser printer rendered red best; **Guibas has said it was simply the red and black pens they had to draw with.** The video presents the laser-printer version as fact — it's a real-but-contested anecdote, not settled history. → [[caveats-and-corrections]].

## CORRECT-BUT-INCOMPLETE (1)

- **DFS 19th-century lineage.** Trémaux (~1880s) → **Lucas** → **Tarry 1895** is correct. Minor imprecision: Lucas's *Récréations Mathématiques* vol. 1 is dated **1882** and he *reported* Trémaux's method ~**1881**, *posed* the problem **1883** — so the video's flat "Lucas 1883" is within a year, not wrong in spirit. Tarry 1895 is exactly right (the captions' "Cherry" is an ASR garble of **Tarry**, not a video error). → [[caveats-and-corrections]].

## Key Takeaways

- **24 claims: 22 CONFIRMED / 1 ANECDOTAL / 1 CORRECT-BUT-INCOMPLETE / 0 FALSE / 0 FABRICATED.**
- The video is **exceptionally accurate** for a fast-format explainer — a rare corpus case where the fact-check finds essentially nothing to correct in substance.
- Only soft spots: the **red-black laser-printer anecdote** (competing author account) and a **one-year date wobble** on Lucas.
- All enriching detail (Turing 1946 BURY/UNBURY, Bavarian beer-cellar LIFO metaphor, "NSS memory", Tarjan's inverse-Ackermann) is in [[historical-timeline]] and [[caveats-and-corrections]].
