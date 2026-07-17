# Linear Structures — array, linked list, stack, queue

**Source:** [video](https://www.youtube.com/watch?v=uHpzKcm8qh0) ~04:00–14:00 · `raw/2026-07-17-data-structures-16-in-32-min.md`

The four sequential moulds, in the order the video builds them — each one invented to fix the previous one's weakness.

## 1. Array (mảng)

- **Mechanism:** a run of memory cells packed side by side, each with its own address. Indexing **starts at 0** (position 4 = the 5th cell).
- **Random access is O(1):** the address is computed directly — `base + index × cell_size` — no scanning.
- **Middle insert is O(n):** every following cell must shift over to make room.
- **Origin:** rooted in **von Neumann's 1945** report describing memory numbered sequentially cell by cell.
- **Trade-off:** blazing fast to read by position; slow when you constantly insert/remove in the middle.

## 2. Linked list (danh sách liên kết)

- **Mechanism:** each element is a **node** = data + a **pointer** to the next node. Nodes need not be adjacent in memory.
- **Head insert is O(1):** just repoint one pointer.
- **Index access is O(n):** no address arithmetic — you must walk node-by-node from the head.
- **Variants:** singly linked (knows next only) vs doubly linked (knows next + previous, traverse both ways).
- **Origin:** **Newell, Shaw & Simon at RAND, ~1955–56**, built to run the **Logic Theory Machine** (first program to prove math theorems).
- **Trade-off:** the exact inverse of the array — loses instant addressing, gains near-free insert/delete at the head.

> The linked list reappears as the collision-resolution mechanism inside the [[hashing|hash table]] — the moulds compose.

## 3. Stack (ngăn xếp) — LIFO

- **Rule:** **last in, first out.** Like a stack of plates: you add and remove only from the top.
- **Operations:** `push` (place on top) and `pop` (take from top) — both **O(1)**, regardless of height.
- **Where it shows up:** the **call stack** (each function call stacks a new frame; the last-called returns first) and **undo** in editors (most recent state pops first).
- **Origin:** the "Kellerprinzip" (cellar principle) by **Bauer & Samelson at TU Munich, ~1955**, patented **1957**; Alan Turing anticipated the idea earlier.

## 4. Queue (hàng đợi) — FIFO

- **Rule:** **first in, first out** — the opposite of a stack. Like a line: whoever arrives first is served first.
- **Ends:** new elements enter at the **rear**; served elements leave at the **front**. Both **O(1)**.
- **Where it shows up:** print queues, OS task scheduling — arrive-first, served-first, no jumping the line.
- **Deque (hàng đợi hai đầu):** a variant allowing insert/remove at **both** ends.
- **Payoff later:** stack + queue are the engines behind the two [[graph-and-traversal|graph traversals]] (DFS uses a stack, BFS uses a queue).

## Key Takeaways

- **Array**: O(1) index, O(n) middle-insert — great for random access, bad for churn.
- **Linked list**: O(1) head-insert, O(n) index — the array's mirror-image trade-off.
- **Stack (LIFO)**: push/pop O(1) — call stack + undo.
- **Queue (FIFO)**: enqueue/dequeue O(1) — schedulers + print spools; deque = both ends.
- These four **compose into later structures** (linked list → hash collisions; stack/queue → graph traversal).
- See [[selection-framework]] for the task→structure mapping and [[historical-timeline]] for dates.
