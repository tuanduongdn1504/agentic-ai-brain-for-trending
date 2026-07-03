# AI Overviews Timeline — SGE → AI Overviews → AI Mode Default

## Source

- Primary: [Liz Reid, "AI Overviews: About last week"](https://blog.google/products/search/ai-overviews-update-may-2024/) (2024-05-30) + [Google I/O 2026 Search announcements](https://blog.google/products-and-platforms/products/search/search-io-2026/) (2026-05-19) + [Liz Reid, "AI in Search is driving more queries and higher quality clicks"](https://blog.google/products-and-platforms/products/search/ai-search-driving-more-queries-higher-quality-clicks/) (2025-08-06)
- Incident documentation: [The Onion original "Geologists Recommend Eating At Least One Small Rock Per Day"](https://theonion.com/geologists-recommend-eating-at-least-one-small-rock-per-1846655112/) (2021); Peter Yang's glue-pizza screenshot thread (X, 2024-05-24)
- Video chapters 3 & 7 · verified by workflow `wf_7208577a-1cc` (C7: dive CONFIRMED ×4 sub-claims; refuter PARTIAL on framing nuance only)

## Timeline (all dates verified)

| Date | Event |
|---|---|
| 2023-05-10 | **SGE** (Search Generative Experience) announced at Google I/O; opt-in via Search Labs, US English |
| 2024-05-14 | **AI Overviews** launch at I/O (Liz Reid, VP Head of Search); target 1B+ users by end of 2024 |
| 2024-05-19–24 | **Error week**: "put glue on pizza" (traced to a years-old joke comment by Reddit user "fucksmith") and "eat one small rock a day" (traced to The Onion 2021, republished on a geology-industry site) go viral |
| 2024-05-30 | Liz Reid response blog "About last week": content-policy violations "less than one in every 7 million unique queries"; safeguards — less user-generated/satirical content, restrictions on health queries |
| 2025-03-05 | **AI Mode** (fully conversational search) launches in Search Labs |
| 2025-05 | AI Overviews reach 200+ countries / 40+ languages; AI Mode announced broadly at I/O 2025 |
| 2025-08-06 | Google's counter-narrative blog: "total organic click volume … relatively stable year-over-year", "average click quality has increased" — **no supporting data published** (see [[state-of-play-2026]]) |
| 2026-05-19 | **AI Mode becomes the DEFAULT Google Search experience globally** (I/O 2026); 1B+ monthly AI Mode users; default model Gemini 3.5 Flash |

## The error incidents — what they actually showed

- Both viral failures were **provenance failures, not reasoning failures**: the system faithfully summarized garbage sources (a joke comment; satire laundered through a legitimate-looking industrial site).
- Google's fix was **source-class filtering** (down-rank UGC/satire for factual queries), not model change — evidence that answer-engine quality is a curation problem. This maps 1:1 onto the vault's own discipline: verify the source class before trusting the claim ([[../claude-md-12-rules/_index|Rule: never fabricate / verify]]).
- The video's framing "the AI takes the traffic whether it's right or wrong" is the durable point: correctness and click-capture are independent axes.

## Prevalence estimates disagree (conflict surfaced, Rule 7)

- Pew (panel, March 2025): **18%** of searches showed a summary
- Ahrefs (keyword telemetry, Nov 2025): AI Overviews on **60.32%** of tracked *keywords*
- SE Ranking (keyword telemetry, March 2026): **48%** of tracked queries
- These measure different universes (real user searches vs tracked keyword sets) with different keyword mixes; do not average them. Panel data (Pew) is the best estimate for "what users saw"; SEO-tool data is best for "what keyword categories are covered."

## Key Takeaways

- The product arc is one-directional: experiment (2023) → default summary layer (2024) → conversational default (May 2026). Each step reduces outbound clicks further (AI Mode: **93% zero-click**, Semrush 69M-session study).
- The May 2024 error week did not slow the rollout — it refined source filtering. The market lesson: quality incidents are absorbable; the strategic pivot was never at risk.
- Google's only public defense of publisher impact (Aug 2025 "quality clicks") shipped without data and was contradicted by Pew, Chartbeat, DCN, SISTRIX, and Similarweb-based measurements — a case study in vendor-claim vs measurement.
- The video (June 2026) narrates the 2024 story; the 2026 story (AI Mode default) is bigger and appears only in [[state-of-play-2026]].

Related: [[pew-ai-overviews-study]] (behavioral impact), [[model-collapse-and-ai-slop]] (source-quality spiral), [[caveats-and-corrections]] (claim grades).
