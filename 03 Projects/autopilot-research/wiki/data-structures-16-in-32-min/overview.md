# Overview — 16 Data Structures in 32 Minutes

**Source:** [Tất Tần Tật Về Cấu Trúc Dữ Liệu Trong 32 Phút](https://www.youtube.com/watch?v=uHpzKcm8qh0) · Học Giải Thuật Cùng HPN · 2026-07-12 · `raw/2026-07-17-data-structures-16-in-32-min.md`

## The one framing

The video's spine is a single question: **"how should this data be arranged so the task at hand gets easier?"** The 16 structures are **16 answers to that one question** — not a list to memorize. Choosing the right arrangement makes a hard problem "naturally lighter."

A data structure is a **mould** (khuôn) the data is poured into from the start — a row (array), a chain (linked list), a branching tree, or a mesh (graph). The whole video is a tour of those moulds from the most basic to the ones "you only hit after years of writing code."

## How each structure is presented

Every structure gets the same three-part treatment:
1. **Mechanism** — how it physically arranges data + its core operations.
2. **Big-O** — how fast those operations are as data grows (see [[big-o-primer]]).
3. **Origin** — the inventor + year (see [[historical-timeline]]).

Then a closing **[[selection-framework]]** collapses all 16 into a fast "task → structure" lookup.

## The 16, grouped (as this wiki organizes them)

| Group | Structures | Article |
|---|---|---|
| Linear / sequential | array, linked list, stack, queue | [[linear-structures]] |
| Key → slot | hash table | [[hashing]] |
| Ordered + self-balancing | BST, AVL, red-black | [[balanced-trees]] |
| Always-know-the-top | heap | [[heap-and-priority]] |
| Many-to-many relations | graph + BFS/DFS traversal | [[graph-and-traversal]] |
| Prefix / string | trie | [[string-trie]] |
| Same-group-or-not | union-find | [[disjoint-set]] |
| Accept a little risk for speed | skip list, bloom filter | [[probabilistic]] |
| Data bigger than RAM | B-tree, LSM-tree | [[disk-scale]] |

## The recurring meta-lesson

The video repeats one theme at almost every transition: **no structure wins absolutely.** Each is a trade-off — the array's O(1) random access costs O(n) middle-inserts; the linked list flips that; the hash table drops ordering to gain O(1) lookup; the balanced tree pays rotation cost to keep order; B-tree favors reads, LSM favors writes. Picking well = matching the trade-off to your workload.

The closer also nests structures inside each other: **a tree is just a graph with no cycles; a heap is stored inside an array; hash-table collisions are resolved with a linked list.** The moulds compose.

## Key Takeaways

- 16 data structures, each = one answer to *"how do I arrange this data to make my task easier?"*
- Uniform treatment: **mechanism → Big-O → historical origin**, then a task→structure selection framework.
- Central thesis: **no structure is universally best — choose by workload.**
- Structures **compose** (tree ⊂ graph; heap ⊂ array; hash-collision → linked list).
- This is the corpus' **first pure CS-fundamentals topic** and slots under the "software fundamentals matter more in the AI era" thread — see [[corpus-and-hireui-relevance]], [[pocock-software-fundamentals/_index]], [[quanit-becoming-ai-engineer-2026/_index]].
