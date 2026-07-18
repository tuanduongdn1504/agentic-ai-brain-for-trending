# Theo's benchmark read + the hallucination reconciliation (N=3)

> Theo's independent leaderboard read **corroborates** the corpus's "#3–4 specialist, not #1 overall" verdict — and his honesty claim, reconciled against primary sources, produced **the single most important nuance in this whole topic**.

## What Theo actually reported (only his stated figures)

Discipline note: the verification workflow's Haiku agents enriched these with precise sub-scores (e.g. "Frontier SWE 86.6/81.2/71.3", "Briefcase 1547") that **Theo never states on-camera**. Below is only what Theo actually said, with timestamps; qualitative where he was qualitative.

| Benchmark | What Theo said | vs corpus |
|---|---|---|
| **AA Intelligence Index** | K3 = **57**, "third smartest ever," comparable to Opus 4.8 & GPT-5.5, behind Fable 5 & GPT-5.6 Sol [21:11–22:05] | **CORROBORATES** scorecard #10/#3 (57.1, #3–4) — *independently verified this pass*: 57.11, #3 distinct / #4 all entries, behind Fable 5 (59.86) & GPT-5.6 Sol max (58.89) |
| **Deep SWE** | Soul **73** > Fable **70** > K3 **67.5**; K3 ahead of GPT-5.5 / Opus-4.8 / GLM-5.2 [06:00] | NEW granular detail; consistent with "#3, behind the two leaders" |
| **Frontier SWE** | K3 slides **between Fable and Soul**, ~10-pt lead on Soul; "more tasteful / mergeable code" [06:29] | NEW; K3's relative *strength* is code that "looks and feels better" |
| **Terminal / Program bench** | Beats Opus & Fable 5, just behind Soul (terminal); "world-class," just beats Soul (program) [06:58] | NEW; near-top, not top |
| **SWE-marathon** | K3 **leads** (ahead of Opus-4.8, Soul, Fable) [07:26] | NEW; one bench K3 tops outright |
| **GDPval** | K3 ≈ **1,668** (up from open-weight-frontier 1,514), ahead of Opus 4.8 [22:33] | CORROBORATES the corpus side-claim (~1,687, above the 1,000 human baseline, below GPT-5.6 Sol Max) |
| **Frontend (Arena/LMArena)** | "industry-leading… really, really good at front end" [13:54] | **CORROBORATES** scorecard #11 — #1 frontend *specialist* |
| **Grok 4.5** | self-corrected: Grok 4.5 is "**behind Tera, Opus, and 5.5** — not at frontier level," but K3 is [21:39] | EXTENDS #3 ranking; Grok sits *below* K3 |

**Net:** a skeptic who "hasn't been hyped about open weights" independently lands exactly where the corpus did — **K3 is a strong #3, a genuine specialist (frontend/visual, some coding benches), not "the world's most powerful AI."** The one bench he says K3 tops outright is SWE-marathon; everywhere near the top it's *behind* GPT-5.6 Sol and/or Fable 5.

## The hallucination reconciliation (the centerpiece)

This is where Theo appears to **contradict** the corpus — and resolving it is the whole payoff of an N=3 skeptical source.

- **Theo's claim [23:56–24:23]:** via Artificial Analysis's **Omniscience** bench, K3 is *"one of the best open-weight models at not hallucinating… the best by quite a bit."* He explains the metric: you score **positive** by saying "I don't know," **negative** by lying — and notes GPT-5.6 Sol/Luna score low for being "too quick to lie."
- **The corpus's claim (scorecard #4):** K3's hallucination rate **rose 39% → 51%** — it *fabricates more*.

**Both are true. They measure different things** (verified against the primary AA sources this pass — [Artificial Analysis](https://artificialanalysis.ai/articles/kimi-k3-achieves-3-in-the-artificial-analysis-intelligence-index-comparable-to-opus-4-8-and-gpt-5-5), [the-decoder](https://the-decoder.com/kimis-open-model-k3-nears-gpt-5-6-sol-and-fable-5-while-signaling-the-end-of-super-cheap-chinese-ai/), [winbuzzer](https://winbuzzer.com/2026/07/17/moonshot-ai-unveils-28t-parameter-kimi-k3-ai-model-xcxwbn/)):

| Metric | Direction | What it measures |
|---|---|---|
| **AA-Omniscience *Index*** | **+6 → +18** (better) | A **composite calibration** score. Rewards correct answers, penalizes confident wrong answers, **no penalty for refusing**. K3's rose because **accuracy improved (33% → 46%)** *and* it refuses more. This is what **Theo** cites. |
| **Raw hallucination *rate*** | **39% → 51%** (worse) | Of the answers K3 **does attempt**, the share that are fabricated. This is what the **corpus** cites. |

**The resolution:** K3 got **better at *refusing*** (so the composite index went up and it looks "honest"), but **worse at *truthfulness when it does answer*** (so the raw fabrication rate went up). Theo's statement is therefore **CORRECT-BUT-INCOMPLETE** — the index is genuinely the best among open-weight models, but he omits that the underlying fabrication rate regressed. The independent completeness critic ruled the reconciliation **holds**, and flagged the missing 51% caveat as a **mandatory** correction to Theo's framing.

### Why this matters more than it looks

- It's a **general lesson in reading model benchmarks:** a favorable *composite/calibration* score can rise while the *raw error rate* underneath it gets worse. "Best at not hallucinating" (index) ≠ "least likely to fabricate when it answers" (rate).
- It **sharpens the hireui verdict, not softens it.** For a candidate-facing Match-Explain, the metric that matters is the **raw fabrication rate (51%)** — a model that "honestly refuses" is useless for the task, and when it *does* answer it's now *more* likely to invent a qualification or requirement. See [[hireui-translation]].
- All three sources now agree on the *shape*: N=1 said "accuracy improved, no downside" (MISLEADING), the corpus corrected it to "51% — fabricates more," and N=3's skeptic — while impressed — **unwittingly demonstrates the trap** by quoting the flattering index without the rate.

## Key Takeaways

- **Independent corroboration of the core correction:** Theo's own leaderboard read puts K3 at **#3, a specialist**, matching the corpus — stronger evidence than the hype video making the claim.
- **The hallucination "conflict" is an index-vs-rate distinction, not a contradiction:** Omniscience **Index +6→+18** (better calibration via refusing) sits on top of a **raw hallucination rate 39%→51%** (worse truthfulness when answering). Both verified against primary AA sources.
- **Theo's "best at not hallucinating" is correct-but-incomplete** — mandatory caveat: it describes the calibration index, not the fabrication rate.
- Only assert what Theo *stated* (73/70/67.5, AA 57, GDPval 1668, Grok-below-K3); the finer sub-scores are secondary-source enrichment, not on-camera claims. See [[theo-claims-scorecard-and-caveats]].
