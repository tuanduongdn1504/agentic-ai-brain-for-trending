# Claims scorecard

Every checkable claim the video makes, ruled against primary/multiple sources. Verified by main-loop WebSearch/WebFetch (Opus) + refute-first workflow verifiers — **all 7 flagged corrections came back UPHELD at high confidence.**

## Scorecard (17 claims)

| # | Video claim | Verdict | Correction |
|---|---|---|---|
| 1 | Kimi K3 is open-source; download the weights now, do whatever | **FALSE** | Hosted-API-only at video time; weights promised **July 27** (Modified MIT). [[open-weights-reality]] |
| 2 | $3/$15 pricing is cost-effective / won't break the bank | **MISLEADING** | A **~3.2–3.8× increase** over K2.6 ($0.95/$4 → 3.16× in / 3.75× out); frontier-tier (= Sonnet 5). "End of cheap Chinese AI." *(corrected 2026-07-17 from "~5–6×")* [[pricing-and-the-end-of-cheap-chinese-ai]] |
| 3 | Beats the frontier; Fable 5 win-rate 58%, GPT-5.6 50% | **FALSE** | Actual arena.ai: Fable 5 **63%**, GPT-5.6 Sol **58%**, K3 76%. On AA Index K3 is **#3–4** behind both. [[benchmarks-fact-vs-hype]] |
| 4 | Accuracy improved (no downside mentioned) | **MISLEADING** | Hallucination rate **rose 39%→51%** — fabricates more. Omitted. [[benchmarks-fact-vs-hype]] |
| 5 | The US restricted K3 for hacking US systems; Americans-only | **FALSE** | Controls were on Anthropic's **Fable 5/Mythos 5**, not K3; imposed Jun 12, lifted ~Jul 1. [[cyber-and-export-control]] |
| 6 | 2.8T params / ~50B active / 6.3× decode via KDA | **CONFIRMED** | Correct. Video omits the 3:1 KDA-to-MLA hybrid exists because linear attention loses 2–5% on retrieval. [[architecture]] |
| 7 | Attention Residuals: 25% training efficiency at <2% cost | **CORRECT-BUT-INCOMPLETE** | Vendor-claimed; validated at 48B (Kimi Linear), not independently at 2.8T. [[architecture]] |
| 8 | 1M-token context window | **CONFIRMED** | Correct. |
| 9 | 2.5× scaling efficiency vs Kimi K2 | **CORRECT-BUT-INCOMPLETE** | Moonshot's own figure; no third-party reproduction. |
| 10 | Ranks ~#3, just under GPT-5.6, on the AA Index | **CONFIRMED** | Fable 5 (59.9) > GPT-5.6 Sol (58.9) > K3 (57.1) ≈ Opus 4.8 (~56). (The video's *"beats Opus 4.8"* elsewhere is the cherry-pick.) |
| 11 | #1 / top-tier across the arenas | **MISLEADING** | #1 on **frontend** only; **#9** on general text (~1,486 Elo). Domain-narrow. |
| 12 | Weights under "Modified MIT" on July 27 | **CONFIRMED** | Correct — but a future promise, not launch reality. |
| 13 | Self-host it once weights drop | **FALSE** | 650GB–1.7TB memory; ~8–16 H100 (~$150–300K); ecosystem lag. Infeasible for normal teams for months. |
| 14 | The demos show what it can do | **CORRECT-BUT-INCOMPLETE** | Real, but **first-party Moonshot marketing** — favorable-condition showcases, not independent. [[demos-and-kimi-work]] |
| 15 | 16 of 896 experts active (MoE) | **CONFIRMED** | Exactly correct. |
| 16 | Native multimodal | **CONFIRMED** | Correct (MMMU-Pro 81.6, MathVision 97.8, etc.). |
| 17 | Cost/task ≈ $0.94 vs Opus ~$1.80 | **CONFIRMED** | Correct — but K3 is ~2× as verbose (130M vs 63M median output tokens), inflating real cost. |

## Side-claims ruled separately

- **"#1 writing at 2,840 Elo" (Louis / editorial-voice benchmark):** **UNVERIFIABLE** — no public record; implausible on any standard Elo scale (~2× frontier). Do not quote. [[benchmarks-fact-vs-hype]]
- **GDPval "near human baseline, beats Opus 4.8 & GPT-5.6":** **PARTIALLY TRUE** — K3 (~1,687) is *above* the 1,000 human baseline (not "near"), beats Opus 4.8, but is **below** GPT-5.6 Sol Max (1,748).
- **Elon Musk "impressive" (re K3 launch):** **CORRECT-BUT-INCOMPLETE** — his praise was for the March-2026 AttnRes paper. [[reception-and-skeptics]]

## Tally

**8 CONFIRMED · 3 CORRECT-BUT-INCOMPLETE · 3 MISLEADING · 3 FALSE · 0 FABRICATED-by-the-corpus** (+ side-claims: 1 UNVERIFIABLE, 1 PARTIAL, 1 CBI).

**Integrity read:** unlike the corpus' high-integrity explainers (e.g. [[../data-structures-16-in-32-min/_index]] at 22/24 clean), this is a **hype-video profile**: the *technical spec* is trustworthy, but the *availability, competitive-ranking, pricing-context, and geopolitics* framing carries **3 outright-false claims**. The model is real; the story around it is inflated.
