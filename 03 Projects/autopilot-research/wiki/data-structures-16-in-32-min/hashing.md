# Hashing — the hash table

**Source:** [video](https://www.youtube.com/watch?v=uHpzKcm8qh0) ~14:00 · `raw/2026-07-17-data-structures-16-in-32-min.md`

## The question it answers

Arrays give O(1) lookup **by sequential index**. But what if you want O(1) lookup **by an arbitrary key** (a name, a user ID) — not by position? That's the hash table.

## Mechanism

- Run the key through a **hash function** → it produces a number → that number **is** the slot to go to.
- No sequential scan: one computation tells you the slot. This is another flavor of **O(1)**, but keyed by anything, not by contiguous index.
- Example from the video: key `user_2.1024` → hash → a slot index → the value lights up in that slot, done.

## Collisions (va chạm)

Two different keys can hash to the **same** slot. Two resolutions the video names:
1. **Chaining** — link the colliding keys together with a **linked list** at that slot (reuses the [[linear-structures|linked list]] just taught).
2. **Open addressing** — if the slot is taken, probe to the next free slot and place it there.

A **good hash function** makes collisions rare, so lookups stay near O(1).

## The catch

- The hash table **keeps no ordering** of the data. If you need data to stay sorted / queryable by range, you must move to a **[[balanced-trees|balanced tree]]** instead.

## Origin

- A **January 1953 IBM internal memo by Hans Peter Luhn** proposed placing data into bins computed from the key. The hash table is born there.

## Key Takeaways

- Hash table = **O(1) lookup by arbitrary key** (average case), via a hash function that computes the slot.
- **Collisions** are resolved by **chaining (linked list)** or **open addressing (probe next slot)**.
- **Trade-off:** you give up ordering; need order/range → use a [[balanced-trees|balanced tree]].
- Nuance the video skips: O(1) is *average*; a bad hash or adversarial keys degrade to O(n) — see [[caveats-and-corrections]].
- Origin: **Hans Peter Luhn, IBM, Jan 1953**.
