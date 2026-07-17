# Balanced Trees — BST, AVL, red-black

**Source:** [video](https://www.youtube.com/watch?v=uHpzKcm8qh0) ~16:00–22:00 · `raw/2026-07-17-data-structures-16-in-32-min.md`

The arc here is a **problem → fix** story: the BST is fast when balanced but degenerates; AVL and red-black are two different repairs.

## Binary Search Tree (cây tìm kiếm nhị phân)

- **Rule:** each node has ≤ 2 children. **Left subtree < node < right subtree**, recursively, everywhere.
- **Search:** start at the root; smaller → go left, larger → go right. Each step **discards half** the remaining nodes.
- **Balanced ⇒ O(log n).** Example: find 40 in a tree rooted at 50 → left to 30 → right to 40 → done in 3 comparisons.
- **The failure mode:** insert already-sorted data (10, 20, 30, 40, 50) and the tree never branches — it becomes a one-sided "tail" indistinguishable from a linked list, and search collapses to **O(n)**.

## AVL tree (cây AVL) — the first self-balancing tree

- **Fix:** after each insert, the tree checks whether one side is more than one level taller; if so it **rotates** to rebalance.
- Example: inserting 10, 20, 30 would form a tail → AVL detects the imbalance, rotates once (20 becomes root, 10 and 30 split to the sides) → balanced again.
- **Origin:** **Adelson-Velsky & Landis, 1962** — the first self-balancing BST in history; the name = their initials.

## Red-black tree (cây đỏ đen) — a different balance discipline

- **Lineage:** grew from **Bayer's 1972 "symmetric binary B-tree"**, then reworked and **renamed "red-black" by Guibas & Sedgewick at Xerox PARC in 1978**. (The color "red" was reportedly chosen because the lab's laser printer rendered red best against black — see [[caveats-and-corrections]] for the contested anecdote.)
- **Rule:** each node is red or black, under 3 invariants — **root is black; a red node can't have a red child; every root→leaf path passes the same number of black nodes.** Keeping these prevents degeneration into a tail.
- **vs AVL:** both prevent the degenerate case; AVL balances by comparing subtree *heights*, red-black balances by *color* invariants. (Practical note the video omits: AVL is more rigidly balanced → faster lookups; red-black rebalances more cheaply → faster inserts. Both O(log n).)

## When to use these

- You need data **always ordered**, want **range queries**, and require a **guaranteed** no-degeneration bound → AVL or red-black. (Contrast the [[hashing|hash table]], which is faster for point lookups but keeps no order.)

## Key Takeaways

- **BST:** left < node < right; O(log n) balanced, but **O(n) if inserted in sorted order** (degenerates to a tail).
- **AVL (1962, Adelson-Velsky & Landis):** first self-balancing tree; rotates on height imbalance.
- **Red-black (Guibas & Sedgewick 1978, from Bayer 1972):** balances via color invariants; cheaper inserts than AVL.
- Choose a balanced tree when you need **ordering + range queries + a guaranteed bound**; choose a [[hashing|hash table]] for pure point lookups.
