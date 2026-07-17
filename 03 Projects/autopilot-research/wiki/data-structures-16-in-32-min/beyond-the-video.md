# Beyond the Video — what a learner still needs

**Not from the video.** This article captures the gaps a completeness pass flagged (Workflow `wf_83c9b13a-5b9`, completeness critic) — concepts the 32-minute survey *raises implicitly but never teaches*. Kept separate so nothing here is mistaken for the source's content. It exists so a reader querying this wiki for "which structure for X?" isn't silently misled by a landscape survey.

## 1. The video teaches KNOWLEDGE, not IMPLEMENTATION

At ~2 minutes per structure, this is a **landscape survey** — it tells you *what exists* and *its Big-O*, not *how to build it*. Anyone who tries to implement a hash table (collision resolution), an AVL tree (LL/RR/LR/RL rotations), or a red-black tree from this video alone will fail. **Best audience: an experienced developer refreshing vocabulary**, not a beginner learning from scratch. (See [[critical-appraisal]].)

## 2. Amortized vs. worst-case vs. average — the missing distinction

The video says "O(1)" flatly. Reality:
- **Dynamic array append** = O(1) *amortized*, but O(n) on the resize.
- **Hash table** = O(1) *average*, but O(n) worst-case under collisions / adversarial keys.
- **Balanced trees** = O(log n) *worst-case guaranteed* — that's their whole point.

Choosing between a hash table and a B-tree often comes down to "average-case fast" vs. "guaranteed bound," which the flat Big-O hides.

## 3. Cache locality & constant factors beat Big-O in practice

Arrays and linked lists both iterate in O(n), yet an array is often **10–100× faster** because contiguous memory is cache- and prefetch-friendly. B-trees are shaped to match **disk block / page size**. Big-O ignores all of this; on modern CPUs/SSDs, memory layout frequently matters more than asymptotic class.

## 4. Implementation variants inside each family

- **Hash table:** chaining vs. open addressing vs. cuckoo vs. hopscotch (10× perf swings by workload).
- **Trees:** AVL (rigid balance → faster reads) vs. red-black (looser → faster writes).
- **Graph:** adjacency list vs. adjacency matrix (sparse vs. dense).
- **Union-find:** **union-by-rank + path-compression are load-bearing, not optional** — without them it's ~O(n) per op; with them, near-O(1).

## 5. Structures the video omits within its own categories

- **Strings:** suffix tree / suffix array (substring search), radix / compressed trie (space).
- **Probabilistic:** count-min sketch (approximate frequency), HyperLogLog (cardinality).
- **Disk-scale:** **B+-tree** (values in leaves → efficient range scans; what most RDBMSs actually use) vs. plain B-tree.

## 6. Composition, not selection

The [[selection-framework]] says "pick one." Real systems **stack many**: e.g. **Redis** = hash tables (main store) + skip list (ordered sets) + bloom filter (RedisBloom) + queues (pub/sub). The "16 answers to one question" framing is a strong *mental model*, a weak *design methodology*.

## 7. Concurrency & thread-safety — entirely absent

Nothing on lock-free hash tables, concurrent skip lists, or immutable/persistent (copy-on-write) structures. Relevant the moment data crosses thread or agent boundaries (directly applicable to multi-agent systems — see [[corpus-and-hireui-relevance]]).

## 8. Structural relationships as reasoning tools

The video drops three composition insights in passing; they're worth holding as *reasoning patterns*, not trivia:
- **A heap is an array** (contiguous → cache-friendly, index math for parent/child).
- **A tree is a graph with no cycles** (so tree algorithms are graph algorithms with a constraint).
- **A skip list is a randomized balanced tree** (randomization replaces rebalancing — and enables lock-free variants).

## Key Takeaways

- This video is a **map, not a manual** — pair it with implementation practice (LeetCode/HackerRank, reading real source like Java's `HashMap`).
- The four biggest silent gaps: **amortized-vs-worst-case, cache/constant-factors, implementation variants, and composition.**
- **Union-find's optimizations are mandatory, not optional.**
- For a real feature you **compose** 4–6 structures — see the hireui walk-through in [[corpus-and-hireui-relevance]].
