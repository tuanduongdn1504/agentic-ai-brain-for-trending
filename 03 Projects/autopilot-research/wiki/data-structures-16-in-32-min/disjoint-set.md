# Disjoint-Set — union-find

**Source:** [video](https://www.youtube.com/watch?v=uHpzKcm8qh0) ~28:00 · `raw/2026-07-17-data-structures-16-in-32-min.md`

## The question it answers

**"Are these two elements in the same group?"** — answered near-instantly, plus the ability to **merge** two groups.

## Mechanism

Two operations only:
1. Every group has a single **representative**.
2. Two elements are in the same group **iff they share a representative**. Merging two groups = merging their representatives into one.

Speed comes from two tricks the video names:
- **Union by rank** — attach the smaller tree under the larger.
- **Path compression** — on each query, flatten the path toward the representative.

## Worked example (Kruskal's MST)

The video demonstrates union-find **inside Kruskal's algorithm** for a minimum spanning tree: process edges in increasing weight order, union the endpoints if they're in different groups, and **skip an edge if both endpoints already share a representative** (it would create a redundant cycle). Because the same-group question is answered in near-constant time, **Kruskal's algorithm runs on millions of edges without slowing down.**

- **Kruskal's algorithm:** published by **Joseph Kruskal, 1956.**

## Origin & complexity milestones

- **Galler & Fischer, 1964** — published this way of managing disjoint groups.
- **Hopcroft & Ullman, 1973** — proved a first complexity bound.
- **Robert Tarjan, 1975** — proved a much tighter, **near-constant** bound (inverse-Ackermann) using union-by-rank + path compression.

## Key Takeaways

- **Union-find** answers **"same group?"** in near-constant time and **merges** groups cheaply.
- Speed from **union-by-rank + path compression**.
- Canonical use: **Kruskal's MST** (Kruskal 1956) — skip edges whose endpoints already share a representative.
- Milestones: **Galler & Fischer 1964** → Hopcroft & Ullman 1973 (first bound) → **Tarjan 1975** (near-constant, inverse-Ackermann).
- Reach for it whenever you repeatedly ask **connectivity / grouping** questions — see [[selection-framework]].
