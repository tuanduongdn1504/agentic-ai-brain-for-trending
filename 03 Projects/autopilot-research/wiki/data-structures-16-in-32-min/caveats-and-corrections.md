# Caveats & Corrections

Two kinds of note here: (A) **caption/ASR garbles** in the Vietnamese auto-transcript (transcription artifacts, not video errors), and (B) **substantive nuances** where the video's telling differs from the scholarly record. All verified via Workflow `wf_83c9b13a-5b9` + nuance-hunter.

## A. Caption / ASR garbles (transcription only — the video itself is fine)

The `vi-orig` auto-captions mangled several proper names. Corrected spellings used throughout this wiki:

| Caption | Correct | Who |
|---|---|---|
| "Paul Bman" | **Paul Bachmann** | Big-O |
| "Edmund Landow" | **Edmund Landau** | Big-O |
| "Donal Knut" | **Donald Knuth** | Big-O → CS |
| "V Newman" | **von Neumann** | array/EDVAC |
| "Hans Peter Lun / Loon" | **Hans Peter Luhn** | hash table |
| "Bower / Bauer … Samelson … Mich / Minion" | **Bauer & Samelson, TU Munich** | stack |
| "Newwell, Shaw, Simon … Range/Rand" | **Newell, Shaw & Simon, RAND** | linked list |
| "Ederson Velski / Adamson Velski … Landis" | **Adelson-Velsky & Landis** | AVL |
| "Galler … Fisher" | **Galler & Fischer** | union-find |
| "Hopcroft … Woman" | **Hopcroft & Ullman** | union-find bound |
| "Robert Chargen" | **Robert Tarjan** | union-find near-constant bound |
| "BNG Bloom / Blu future" | **Burton Bloom / bloom filter** | bloom filter |
| "Rudolph Bayer … Edward McCracht … Boeing" | **Rudolf Bayer & Edward McCreight, Boeing** | B-tree |
| "Gibass … Swig / Squck … Serox SPK" | **Guibas & Sedgewick, Xerox PARC** | red-black |
| "William Pew" | **William Pugh** | skip list |
| "Conradus" | **Konrad Zuse** | BFS |
| "Tro … Eduar Lucas … Cherry" | **Trémaux … Édouard Lucas … Gaston Tarry** | DFS lineage |
| "Joseph Crossco / thuật toán Crossc" | **Joseph Kruskal / Kruskal's algorithm** | MST |
| "Rene de La Briandez" | **René de la Briandais** | trie |
| "cây LSM / LSM3 / lock structured merch" | **LSM-tree (Log-Structured Merge-tree)** | disk-scale |

## B. Substantive nuances

### B1 — Red-black "laser printer" story is ANECDOTAL (competing account)
The video states red was chosen because the lab's laser printer rendered red best. **Sedgewick has indeed said this in interviews** — but co-inventor **Leonidas Guibas has given a different account: the colors were simply the red and black pens they had for drawing trees.** Both stories come from the authors. Treat "because of the laser printer" as *a* story, not *the* settled reason.

### B2 — DFS lineage: Lucas date is ~1 year off; "Tarry" not "Cherry"
Trémaux (~1880s) → Lucas → Tarry (1895) is correct. Precisely: Lucas *reported* Trémaux's method ~**1881** and *posed* the maze problem **1883** (*Récréations Mathématiques* vol. 1 is dated **1882**). The video's "Lucas 1883" is within a year. **Tarry 1895 is exactly right** — the captions' "Cherry" is garble.

### B3 — Big-O: Landau *refined*, didn't *invent*
Bachmann (1894) invented the O notation; **Landau (1909) adopted and extended it** (added little-o), which is why both are "Landau symbols." Intro sources sometimes over-credit Landau. Neither popularized it in CS — **Knuth did, in the 1970s.** The video's ordering (Bachmann → Landau → Knuth) is correct.

### B4 — Linked-list date: 1955–56, not "1959"
The video's timeline montage flashes "linked list born 1959," but its own detailed section (correctly) ties it to the Logic Theorist ~1955–56. Verified: **developed 1955–56** at RAND (IPL / "NSS memory"), **published 1956–59**. Use 1955–56 for invention.

### B5 — Kellerprinzip = "cellar principle" (and why)
Literally "cellar principle" (Keller = cellar). Bauer explained the metaphor in a 1980 ACM interview: in a **Bavarian beer cellar the last barrel rolled in is the first tapped** — a vivid LIFO image. Standard, well-attributed.

## C. Format-level caveats (the video's teaching limits — not errors)

These aren't corrections; they're honest limits of a 32-min/16-structure survey. Fully treated in [[beyond-the-video]] and [[critical-appraisal]]:
- Teaches **knowledge, not implementation** — you can't code any of these from the video alone.
- Omits **amortized vs. worst-case**, **cache locality / constant factors**, and **space complexity**.
- The **"pick one structure"** framing understates that real systems **compose** many.

## Key Takeaways

- **~20 proper-name garbles are ASR artifacts**, not video errors — corrected table above.
- Only **one contested claim** (red-black laser printer) and **one minor date wobble** (Lucas) survive as substantive caveats.
- The video's **factual accuracy is excellent**; its limits are **format** (survey depth), not correctness — see [[beyond-the-video]].
