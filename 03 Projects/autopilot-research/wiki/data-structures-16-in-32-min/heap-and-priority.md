# Heap & Priority — always know the top

**Source:** [video](https://www.youtube.com/watch?v=uHpzKcm8qh0) ~22:00 · `raw/2026-07-17-data-structures-16-in-32-min.md`

## The question it answers

You want a structure that **always knows, instantly, which element is largest (or smallest)** — regardless of insertion order.

## Mechanism

- A **heap** is a **near-complete tree** — every level is filled before the next begins.
- **Max-heap rule:** every parent ≥ both children ⇒ the maximum is always at the **root**.
- **Array-backed callback:** because the tree is always complete, it packs perfectly into an **[[linear-structures|array]]** — node *i* has children at **2i+1** and **2i+2**. (An explicit "reuses the array section" moment in the video.)
- **Insert (`shift up`):** append to the end of the array, then swap upward while the parent is smaller, stopping when the parent is larger.
- **Extract-max (`shift down`):** the root leaves; the last element moves to the root, then swaps down with the larger child until it's ≥ both children.

## Payoff

No matter how scrambled the insertion order, the heap answers **"what's the highest-priority element?"** immediately — it's sitting at the root. This is the structure behind **priority queues**.

## Origin

- **J.W.J. Williams, 1964**, introduced the heap as the structure behind **Heapsort** (ACM **Algorithm 232**). **Floyd** improved heap construction the same year.

## Key Takeaways

- **Heap** = near-complete tree, **parent ≥ children** (max-heap) ⇒ max always at the root.
- Stored in an **array** (children at 2i+1, 2i+2) — a direct callback to the [[linear-structures|array]] section.
- `shift up` on insert, `shift down` on extract — both O(log n); peek-max is O(1).
- Use it when you **continuously need the highest-priority element** irrespective of insert order (priority queue).
- Origin: **Williams 1964** (Heapsort, ACM Algorithm 232); Floyd improved heapify same year.
