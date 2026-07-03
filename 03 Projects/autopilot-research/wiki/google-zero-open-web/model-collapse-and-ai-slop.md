# Model Collapse & AI Slop — The Lab vs the Hype

## Source

- Primary: [Shumailov et al., "AI models collapse when trained on recursively generated data", Nature 631:755–759](https://www.nature.com/articles/s41586-024-07566-y) (2024-07; preprint ["The Curse of Recursion"](https://arxiv.org/abs/2305.17493) May 2023; minor notation correction March 2025, findings unchanged)
- Counterweight: [Schaeffer et al., "Position: Model Collapse Does Not Mean What You Think"](https://arxiv.org/abs/2503.03150) (March 2025, position paper — ⚠️ preprint/position, publication venue unconfirmed)
- Prevalence measurements: [Originality.ai ongoing Google-results study](https://originality.ai/ai-content-in-google-search-results) · [Ahrefs 900K-new-pages study](https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/) (Apr 2025)
- Video chapter 8 · verified by workflow `wf_7208577a-1cc` (C15 PARTIAL — the qualification below)

## What the science actually shows

- **Shumailov (Nature 2024) is real and solid**: models trained recursively on predominantly synthetic data degrade irreversibly — distribution tails vanish first, diversity collapses, outputs drift from truth. Demonstrated across VAEs, GMMs, LLMs. The video's "copies of copies… each new version drifts further from the truth" is a faithful gloss *of the lab result*.
- **Schaeffer (2025) is the missing counterweight**: the literature holds ~8 conflicting definitions of "collapse"; many collapse scenarios assume data-replacement regimes that don't match practice (real pipelines *accumulate* data and curate); under realistic mixing, collapse is "readily avoidable."
- **No production model collapse has ever been demonstrated.** 2025's observed model regressions (GPT-4 code-quality drift, Gemini 2.5 complaints, Claude code incidents) were attributed by vendors to routing/versioning — none acknowledged (or were shown to have) training-data collapse. Vendors don't disclose synthetic-data shares, so the question is open, not settled.

## What the slop measurements show

- Originality.ai (500 keywords, bimonthly): AI-generated content in Google top-20 results ≈ **10.2%** (Mar 2024) → **~17–19.6%** (2025 peak) — real growth, not majority
- Ahrefs (Apr 2025, 900K newly indexed pages): **74.2%** contain *some* AI content — but only **2.5% pure AI**; 71.7% mixed human+AI
- Detector caveat (both studies): AI-detection accuracy ≈96%, false positives ~1.5-2%+, worse on non-native English — treat all prevalence numbers as ±several points
- LinkedIn: 50%+ of long posts likely AI-assisted (Originality.ai); Reddit posts ~15%

## Where the video overreaches (the one chapter that runs ahead of evidence)

1. **Causal chain unproven**: "Google's AI must train on AI output → rot → answer engine decays" is speculation. Google's answer-engine pivot is a product/UX strategy; no evidence ties it to training-data degradation.
2. **"Dead internet spiral" as inevitability**: Schaeffer et al. argue collapse is avoidable with curation; fresh human data keeps arriving (though its *economics* are what the rest of the video correctly shows eroding — that's the real spiral risk: incentive collapse, not gradient collapse).
3. AI-slop prevalence is real but "the web fills with AI pages" needs the numbers above attached: some-AI-involvement is becoming the norm; pure-AI spam remains a small slice of new pages *indexed*.

## The defensible synthesis

The strong version of the video's point isn't the ML mechanism — it's the **economics**: if original human research stops being funded (the [[publisher-economics]] story), the training and grounding corpus quality degrades *regardless* of whether formal model collapse occurs. Incentive rot precedes and outpaces gradient rot.

## Key Takeaways

- Cite Shumailov for "collapse is real in the lab"; cite Schaeffer alongside it for "and avoidable in practice with curation" — never one without the other (Rule 7: surface the conflict).
- No production LLM has demonstrated model collapse as of mid-2026; vendor training mixes are undisclosed — the honest verdict is "open question," not "happening now."
- Slop numbers worth keeping: ~17-19% of Google top-20 results AI-generated (2025); 74% of new pages have *some* AI involvement but only 2.5% pure-AI; all ± detector error.
- The vault's own countermeasure is this pipeline: primary-source pinning + adversarial verification = a curated non-slop corpus ([[../claude-code-memory-systems/_index|memory systems thread]]).

Related: [[ai-overviews-timeline]] (provenance failures as the near-term quality problem), [[publisher-economics]] (the incentive-collapse version), [[state-of-play-2026]].
