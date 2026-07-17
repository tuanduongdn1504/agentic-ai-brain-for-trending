# Graph & Traversal — BFS and DFS

**Source:** [video](https://www.youtube.com/watch?v=uHpzKcm8qh0) ~24:00 · `raw/2026-07-17-data-structures-16-in-32-min.md`

## Graph (đồ thị)

- **Definition:** just **vertices** + **edges** between them. No limit on how many vertices one vertex connects to.
- **Tree is a special case:** the [[balanced-trees|trees]] earlier are simply graphs with **no cycles** — an explicit unification the video makes.
- **Storage:** most commonly an **adjacency list** — record, per vertex, which vertices it connects to.

## The two traversals (this is where stack + queue pay off)

The video's example: 7 vertices A–G with some edges. The **only difference** between the two traversals is the tool driving them — and that single swap changes the entire shape of the walk.

### BFS — breadth-first (duyệt theo tầng) — uses a QUEUE

- Start at A, enqueue A. Dequeue A (visit), enqueue its neighbors B, C. Dequeue B (visit), enqueue D, E. Dequeue C, enqueue F. …
- **Result:** visits **layer by layer** — everything near A first, farther nodes later.
- **Origin:** attributed to **Konrad Zuse, 1945** (in a PhD thesis that was rejected and only published 1972); **reinvented by Edward F. Moore, 1959** to find the shortest path through a maze.

### DFS — depth-first (duyệt theo chiều sâu) — uses a STACK

- Start at A, push A. Pop A (visit), push B, C. Pop B, push D, E. Pop D — dead end. Pop E, push G. Pop G — dead end. Back to C … — plunges down one path to the end, then backtracks (the stack's LIFO rule made visible).
- **Result:** one deep thread, then retreat.
- **Origin:** from **Trémaux's** maze-solving method (~1880s), **recorded by Édouard Lucas in 1883**; a similar method observed by **Gaston Tarry, 1895** (the video garbles this name as "Cherry" — see [[caveats-and-corrections]]).

> **The lesson:** same graph, same edges — **swap the queue for a stack** and the traversal order flips from "spread in rings" to "dive and backtrack." The [[linear-structures|stack and queue]] weren't idle foundations; they *are* the control logic of graph search.

## Complexity

- Traversal visits every vertex + every edge → **O(V + E)**.

## Key Takeaways

- **Graph** = vertices + edges, unbounded connectivity; **a tree is a graph with no cycles.**
- Stored as an **adjacency list**; traversal is **O(V + E)**.
- **BFS = queue → layer-by-layer** (Zuse 1945 / Moore 1959, maze shortest path).
- **DFS = stack → dive-and-backtrack** (Trémaux 1880s / Lucas 1883 / Tarry 1895).
- The **only change** between BFS and DFS is queue-vs-stack — the clearest payoff of the [[linear-structures]] section.
