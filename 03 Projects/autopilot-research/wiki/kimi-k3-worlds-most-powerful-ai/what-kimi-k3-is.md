# What Kimi K3 actually is

The verified spec sheet — everything below is CONFIRMED against primary/multiple sources (Moonshot's `kimi.com/blog/kimi-k3`, Artificial Analysis, ArXiv, MarkTechPost) unless flagged.

## Identity

- **Model:** Kimi K3 — flagship of Moonshot AI (Chinese lab; the "Kimi" line, successor to Kimi K2 / K2.6).
- **Released:** **2026-07-16** (the video is 2026-07-17, one day later).
- **Access at launch:** hosted only — Kimi app, Playground, Kimi API (`platform.kimi.ai`), Kimi Code, Kimi Work. **Not downloadable** (see [[open-weights-reality]]).

## Spec

| Property | Value | Status |
|---|---|---|
| Total parameters | **2.8 trillion** (Moonshot rounds to "3T-class"; the video's "3T" is that rounding) | CONFIRMED |
| Active parameters | **~50B** per token ("2.8T-A50B") | CONFIRMED |
| Architecture | Sparse **Mixture-of-Experts** ("Stable LatentMoE"), **16 of 896** experts active (~1.79% sparsity) | CONFIRMED |
| Attention | **Kimi Delta Attention (KDA)** + **Attention Residuals (AttnRes)**, hybrid **3:1 KDA-to-full-attention** | CONFIRMED |
| Context window | **1,000,000 tokens** | CONFIRMED |
| Modality | **Native multimodal** — text, high-res image, video end-to-end | CONFIRMED |
| Efficiency claim | **2.5× scaling efficiency vs Kimi K2** | CONFIRMED as *vendor-reported* (no third-party reproduction) |
| Pricing | **$3 / M input** (cache-miss), **$0.30 / M** cache-hit, **$15 / M output** | CONFIRMED |
| License (weights) | "Modified MIT," promised **2026-07-27** | CONFIRMED (date + license per multiple sources; full terms not yet published) |

## Where it actually ranks (headline)

- **#1** — arena.ai **Frontend Code Arena** (1,679 Elo; 76% pairwise win rate). Domain-narrow.
- **#3–4** — Artificial Analysis **Intelligence Index** (57.1), behind **Fable 5 (59.9)** and **GPT-5.6 Sol (58.9)**, ~tied with **Opus 4.8 (~56)**.
- **#9** — general **text** arena (~1,486 Elo). Mid-pack.

Full leaderboard breakdown in [[benchmarks-fact-vs-hype]].

## The one-line honest summary

> A genuine 3T-class open-weight-*announced* model that is **best-in-class at frontend/visual coding, near-frontier overall, mid-pack at general text, more hallucination-prone than its predecessor, hosted-only at launch, and frontier-priced** — not "the world's most powerful AI."

## Key Takeaways

- Believe the **spec** — all of it checks out.
- Discount the **superlatives** — "world's most powerful / beats Fable 5" is true only on one narrow board.
- The two facts the video buries: **weights weren't available** ([[open-weights-reality]]) and **hallucination went up** ([[benchmarks-fact-vs-hype]]).
