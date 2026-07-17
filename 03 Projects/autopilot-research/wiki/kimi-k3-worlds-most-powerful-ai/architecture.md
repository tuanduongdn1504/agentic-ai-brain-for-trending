# Architecture — KDA, Attention Residuals, and the MoE

The video's architecture segment (~[16:39]–[17:33]) is the part it gets **most right**. Everything below is CONFIRMED (ArXiv 2510.26692 "Kimi Linear", ArXiv 2603.15031 "Attention Residuals", Moonshot blog, MarkTechPost) — with the trade-offs the video glossed over.

## Mixture-of-Experts ("Stable LatentMoE")

- **896 routed experts; 16 active per token** → ~1.79% sparsity. 2.8T total params, **~50B active** per forward pass.
- Supporting machinery: **Quantile Balancing** (routes on router-score quantiles, no hand-tuned heuristics), **Per-Head Muon** optimizer, **Sigmoid-Tanh Unit (SiTU)** activation.
- The video's "896 experts, activates 16" is **exactly correct**.

## Kimi Delta Attention (KDA)

- KDA is a **hybrid linear-attention** mechanism that refines **Gated DeltaNet** with **channel-wise gating** (independent forgetting rate per feature dimension, vs coarse head-wise gates).
- Uses a specialized **Diagonal-Plus-Low-Rank (DPLR)** transition matrix (binds the low-rank vectors to the key `k_t`), giving ~2× the speed of standard DPLR kernels up to 64k tokens.
- Claimed benefit: **~6.3× faster decoding** (Time-Per-Output-Token) at 1M context vs standard MLA, with **~75% smaller KV cache**. (Some sources say "6×" — throughput vs TPOT measure; the video quotes a single number without the qualifier.)

## The trade-off the video skipped

- KDA is **interleaved 3:1 with full attention (MLA)** — three lightweight KDA layers, then one full-attention layer. **This ratio is necessary, not incidental:** pure linear attention loses **2–5% on retrieval tasks** vs full softmax. The video presents KDA as a free "faster decoding" win; it's a **speed-vs-retrieval trade managed by the hybrid**.

## Attention Residuals (AttnRes)

- Lets a layer selectively retrieve representations from **earlier depths** instead of accumulating every prior state uniformly — improving how information flows through depth.
- Claim: **~25% higher training efficiency (1.25× compute-equivalent) at ~4% training overhead / ~2% inference latency**.
- ⚠️ **CORRECT-BUT-INCOMPLETE:** this is a **vendor claim**, and the original validation was on the **48B Kimi Linear** model — scaling to the full 2.8T K3 has **not** been independently reproduced. (Elon Musk's "impressive" praise, per the video, was actually for *this* March-2026 AttnRes paper, not the K3 launch — see [[reception-and-skeptics]].)

## 2.5× scaling efficiency vs K2

- CONFIRMED as **Moonshot's own reported figure** (combined effect of KDA + AttnRes + Stable LatentMoE + training changes). No third-party reproduction or reproducible methodology has been published. Treat as a credible vendor claim, not an independently established fact.

## Multimodal / vision

- Native multimodal (text + high-res image + video in one model). Reported vision benchmarks: **MMMU-Pro 81.6, CharXiv-RQ 91.3, MathVision 97.8, OmniDocBench 91.1**. Head-to-head vs Fable 5 / GPT-5.6 on vision is **not** available in public reports, so "best multimodal" is unverifiable.

## Key Takeaways

- The architecture claims are **real and well-sourced** — this is the trustworthy half of the video.
- Two honesty gaps: KDA's speed comes with a **retrieval trade-off** (hence the 3:1 hybrid), and the AttnRes / 2.5× numbers are **vendor-reported at 48B scale**, not independently reproduced at 2.8T.
- A full **technical report** is due with the July 27 weights — that's when these claims become checkable ([[open-weights-reality]]).
