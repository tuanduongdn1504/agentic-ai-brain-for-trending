# Big-O Primer — the video's measuring stick

**Source:** [video](https://www.youtube.com/watch?v=uHpzKcm8qh0) 01:09 "Big O Notation" · `raw/2026-07-17-data-structures-16-in-32-min.md`

## Why not measure in seconds

The video makes the point crisply: **you don't measure speed in seconds** because a fast machine and a slow machine give different numbers — comparing wall-clock across machines is meaningless. Instead you measure **how much the processing time balloons as the data grows** (doubles, 10×). That growth rate is written with the letter **O**.

- **O(n)** — data doubles ⇒ time doubles (grows in lockstep).
- **O(log n)** — data doubles ⇒ time nudges up only a little.

## The four curves the video draws

| Notation | Shape | Behavior as data doubles |
|---|---|---|
| **O(1)** | flat line | time unchanged — data size is irrelevant |
| **O(log n)** | rises very slowly | time barely nudges |
| **O(n)** | straight diagonal | time doubles |
| **O(n²)** | steep curve | time **quadruples** |

The video's advice: **memorize the symbols, not the math behind them.** Every structure will be tagged with one of these.

## Provenance of the notation

- The **O** symbol was introduced by German mathematician **Paul Bachmann** (video leaves the year blank; the notation appears in his 1894 *Analytische Zahlentheorie*).
- **Edmund Landau** extended/popularized it (video says "1909").
- **Donald Knuth** brought it into computer science to measure algorithm speed (~1970s).

> Exact dates/attribution are ground-truthed in [[claims-scorecard]]; the video's own gap (blank Bachmann year) is noted in [[caveats-and-corrections]].

## What Big-O quietly leaves out (video does NOT cover)

Worth flagging for any learner — the video's Big-O treatment is intentionally minimal:
- **Worst-case vs amortized vs average** — e.g. hash-table O(1) is *average*; a bad hash degrades to O(n). Dynamic-array append is *amortized* O(1). The video says "O(1)" without this nuance.
- **Constant factors & cache locality** — arrays beat linked lists in practice even at equal Big-O because contiguous memory is cache-friendly; Big-O hides this.
- **Space complexity** — the video is almost entirely about *time*.

See [[caveats-and-corrections]] for the full "what a 32-min format omits" list.

## Key Takeaways

- Big-O measures **growth rate**, not seconds — that's what makes it machine-independent.
- Four curves to know: **O(1) < O(log n) < O(n) < O(n²)**.
- Lineage: **Bachmann → Landau → Knuth (into CS)**.
- The video omits **amortized/worst-case distinctions, constant factors, cache effects, and space** — real gaps for a learner ([[caveats-and-corrections]]).
