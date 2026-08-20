# Corpus correction — what this topic changes in `local-ai-coding-agents`

> This topic exists to test a standing claim. Here is the precise diff. **No files in `local-ai-coding-agents/` have been edited** — per librarian discipline, corrections are cross-linked, not silently overwritten.

## What was claimed, and on what evidence

[[../local-ai-coding-agents/_index|local-ai-coding-agents]] (2026-07-11) was compiled from **a single source** — Code with Beto, *"Local AI Coding Agents Are Finally Good Enough"* — plus first-party dives into the tools it named. Its hardware article, [[../local-ai-coding-agents/hardware-economics-and-tco|hardware-economics-and-tco]], concluded:

> **"≥24 GB is a *practical minimum*, not a ceiling"** — with a quant→machine table keyed on model weights, and two data points: an 18 GB MacBook that failed and a 96 GB M3 Ultra that worked.

## What changes

| Claim in `local-ai-coding-agents` | Status after this topic | Basis |
|---|---|---|
| "≥24 GB is a practical minimum" | **REFUTED for agentic coding** | A 24 GB M4 Pro failed a *small static site* with a **4 B 4-bit** model — stalled 20 min, died. WEBdoze: *"not powerful enough even to run a four bits and four billion parameter model."* |
| Quant→machine table keyed on **weights** | **INCOMPLETE** | Measured: a 36 GB model consumed **~80 GB RAM** once context loaded. The table omits the KV-cache term it names in prose. |
| "KV cache is the hidden cost… tens of GB" | **UPHELD and strengthened** | Now first-party: Apple states agentic sessions are *"hundreds of thousands of tokens, and most of those are not generated."* |
| Memory capacity as the organising axis | **SUPERSEDED** | Bandwidth (prefill) and workload size are the binding constraints. See [[the-hardware-ladder]], [[why-agentic-differs-from-chat]]. |
| "Local inference = strongest privacy posture" ([[../local-ai-coding-agents/privacy-data-residency|privacy-data-residency]]) | **UPHELD but incomplete** | True for weights and prompts. The anchor's agent requested **iCloud Drive and Music** access — filesystem scope is a separate axis. **Local ≠ contained.** |
| Beto's "good enough" verdict | **SCOPE-NARROWED, not refuted** | It was measured on a small feature. Both sources here that ran **real production repos** returned negative verdicts. |
| `qwen3.6-27b` article's subject | **CONFIRMED to still exist** | A verification agent claimed Qwen3.6 doesn't exist; that was wrong. Released 2026-04-22, Apache-2.0. See [[caveats-and-corrections]]. |

## The one-sentence diff

> The old topic asked **"how much memory do you need?"** and answered with a number. The right question is **"how much memory, for what size repository, at what bandwidth?"** — and at every rung anyone actually measured against a real codebase, the answer was **not enough**.

## Why the original wasn't wrong to publish

It was compiled from one source and said so. It correctly identified KV cache as the hidden cost — it simply didn't have the data points to see that the cost dominates. **This is the corpus health loop working**: a single-source claim, published with its provenance visible, tested by a later bundle, corrected with evidence rather than opinion.

The failure to avoid in future is the one this pair demonstrates: **naming a mechanism in prose and then publishing a table that ignores it.** The prose said "KV cache is the hidden cost"; the table was keyed on weights alone. Readers use the table.

## Recommended edits to `local-ai-coding-agents` (not applied — operator's call)

Per the vault rule *"ask before editing existing notes"*:

1. Add a banner to `hardware-economics-and-tco.md` pointing at [[the-hardware-ladder]] and marking the "≥24 GB minimum" line as superseded for agentic workloads.
2. Add a **workload column** to its quant table, or relabel it *"minimum to load for chat"*.
3. Add a filesystem-scope caveat to `privacy-data-residency.md` linking [[anchor-quanit-64gb]].
4. Add a `See also` from its `_index.md` to this topic.

## Key Takeaways

- **The "≥24 GB practical minimum" is refuted for agentic coding** by direct measurement one rung below and one rung above.
- **The KV-cache mechanism the old topic named is now first-party-confirmed by Apple** — and it dominates rather than merely adds.
- **Beto's verdict is narrowed, not overturned**: true for small features, unsupported for real repositories.
- **Local privacy claims need a filesystem-scope caveat.**
- **The structural lesson: don't publish a table that contradicts your own prose.**

## See also
[[the-hardware-ladder]] · [[why-agentic-differs-from-chat]] · [[anchor-quanit-64gb]] · [[caveats-and-corrections]] · [[../local-ai-coding-agents/_index|local-ai-coding-agents]]
