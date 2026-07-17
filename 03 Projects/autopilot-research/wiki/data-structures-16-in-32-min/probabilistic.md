# Probabilistic — skip list & bloom filter

**Source:** [video](https://www.youtube.com/watch?v=uHpzKcm8qh0) ~29:00 · `raw/2026-07-17-data-structures-16-in-32-min.md`

These two break the pattern of the earlier structures: they **accept a little randomness / a small chance of error** in exchange for a big win in speed or memory. "No absolute certainty, but much faster."

## Skip list (danh sách liên kết có tầng)

- **Mechanism:** on top of an ordinary **sorted [[linear-structures|linked list]]**, build a few **express lanes** that skip elements. The higher the lane, the sparser it is, the farther each hop jumps.
- **Promotion is random:** whether an element rises to a higher lane is decided by a **coin flip on insert** — no complex rebalancing math like the [[balanced-trees|AVL/red-black trees]].
- **Worked example (find 25 in 3, 6, 9, 12, 17, 21, 25):** start on the top lane → only stop is 17 (< 25, hop there) → drop to the middle lane → next is 25 (found, but confirm) → drop to the base lane from 17 → 21 → 25, match. **Touches only 3 numbers (17, 21, 25),** skipping the first four.
- **Origin:** **William Pugh, 1990** (CACM, "Skip lists: a probabilistic alternative to balanced trees").
- **Search:** ~**O(log n)** expected, with far simpler code than a balanced tree.

## Bloom filter (bộ lọc Bloom)

- **Mechanism:** a **bit array** (all 0s initially) + several **hash functions**. To add a key, run it through the hash functions and set those bits to 1. To test membership, hash the key and check those bits.
- **One-sided error — the key property:** if **any** of the bits is 0, the key is **definitely not** in the set. If all are 1, the key is **"possibly present"** — it might be a **false positive** (bits set by other keys). **Never a false negative** — "it can over-report, never under-report."
- **Worked example (video):** a 12-bit array, 3 hash functions per key; adding keys sets bits; a query whose 3 bits include a 0 → certainly absent; a query whose 3 bits are all already set → "possibly present" even if never inserted (the false positive).
- **Origin:** **Burton H. Bloom, 1970.**
- **Payoff:** a tiny amount of accepted risk buys **huge memory + time savings** versus storing the full set.

> Nuance the video doesn't raise: a third probabilistic structure family, **count-min sketch** (approximate frequency counting), rounds out this category — noted in [[beyond-the-video]].

## Key Takeaways

- **Skip list** (Pugh 1990): express lanes over a sorted linked list, **random coin-flip promotion**, **O(log n)** expected — a simpler alternative to balanced trees.
- **Bloom filter** (Bloom 1970): bit array + hash functions for set-membership; **false positives possible, false negatives impossible** ("can over-report, never under-report").
- Shared theme: **trade a little certainty/randomness for large speed or memory gains.**
- Use skip list for **ordered data with simple code**; bloom filter for **cheap "probably in the set?" checks** (e.g. dedup) — see [[selection-framework]].
