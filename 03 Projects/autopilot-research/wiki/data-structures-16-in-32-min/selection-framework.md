# Selection Framework — task → structure

**Source:** [video](https://www.youtube.com/watch?v=uHpzKcm8qh0) closing segment ~30:40 · `raw/2026-07-17-data-structures-16-in-32-min.md`

The video's payoff: collapse all 16 into a fast **"what am I trying to do?" → structure** lookup. The framing that ties it together — *"16 answers to one question: how should this data be arranged to make the task easier?"*

## The decision table (as the video states it)

| If you need… | Choose | Why | Article |
|---|---|---|---|
| Exact element by index, instantly; don't care about middle insert/delete | **Array** | O(1) addressed access | [[linear-structures]] |
| Constant add/remove at the **ends**, no random access | **Linked list** | O(1) head insert | [[linear-structures]] |
| **Last-in-first-out** discipline | **Stack** | push/pop O(1) | [[linear-structures]] |
| **First-in-first-out** discipline | **Queue** | enqueue/dequeue O(1) | [[linear-structures]] |
| Lookup by **arbitrary key**, order irrelevant | **Hash table** | O(1) avg by hash | [[hashing]] |
| Data **always ordered** + range queries + guaranteed no-degeneration | **AVL / red-black tree** | O(log n) guaranteed | [[balanced-trees]] |
| Ordered data but want **simpler code**, accept randomness | **Skip list** | O(log n) expected, no rebalancing | [[probabilistic]] |
| Continuously pull the **highest-priority** element | **Heap** | peek-max O(1) | [[heap-and-priority]] |
| **Many-to-many relationships**, no single root | **Graph** | vertices + edges | [[graph-and-traversal]] |
| Fast **"same group?"** / connectivity | **Union-find** | near-constant | [[disjoint-set]] |
| **Prefix** lookup / type-ahead autocomplete | **Trie** | O(string length) | [[string-trie]] |
| Cheap **"probably in the set?"** with tiny memory, tolerate over-reporting | **Bloom filter** | one-sided error | [[probabilistic]] |
| Data **exceeds RAM**, on disk, **read-heavy** | **B-tree** | few disk seeks | [[disk-scale]] |
| Data on disk, **write-heavy** at scale | **LSM-tree** | append-optimized | [[disk-scale]] |

## The complexity cheat-sheet (video's closing summary)

- **Instant / near-instant** for their intended job: array, hash table, stack, queue, heap.
- **Around O(log n):** balanced trees, B-tree, skip list.
- **Graph traversal:** O(vertices + edges).
- **Trie:** O(string length) — independent of dictionary size.

## The one rule

> **"No structure wins absolutely on all fronts. Choosing right is simply choosing the one that matches the task you actually have."**

Then the deeper point: **data structures are the foundation; algorithms (sorting, searching, dynamic programming) are the story that runs on top of them** — "they all stand on the shoulders of the names in this video."

## Important caveat (NOT in the video)

Real systems rarely pick **one** structure — they **compose** several (e.g. a database = B+-tree index + hash index + bloom filter + write buffer). The "pick one" framing is a learning device, not a design methodology. See [[beyond-the-video]] and [[corpus-and-hireui-relevance]] for how a real feature stacks 4–6 of these together.

## Key Takeaways

- Map **task → structure**, not structure → memorization; the 16 are answers to one question.
- Rough tiers: **O(1)** (array/hash/stack/queue/heap) · **O(log n)** (balanced trees/B-tree/skip list) · **O(V+E)** (graph) · **O(len)** (trie).
- **Core rule:** no structure is universally best — match the workload.
- **Real caveat:** production systems **compose** structures; "pick one" is pedagogy, not architecture ([[beyond-the-video]]).
