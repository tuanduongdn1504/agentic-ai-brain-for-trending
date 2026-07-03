# The Pew Study — AI Summaries vs Clicks (July 2025)

## Source

- Primary: [Pew Research Center short read, 2025-07-22 — "Google users are less likely to click on links when an AI summary appears in the results"](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) (Athena Chapekis et al.)
- Primary: [Methodology document](https://www.pewresearch.org/2025/05/23/methodology-metered-data-ai/) — KnowledgePanel Digital, RealityMeter app
- Video chapter 3 · verified by workflow `wf_7208577a-1cc` (C8: dive CONFIRMED on all 10 sub-numbers; 2 refuters PARTIAL only on paraphrase nuances — see below)

## Design

- **900 US adults**, consented device metering (RealityMeter), tracked **March 1–31, 2025**
- **68,879 unique Google searches**; **12,593 (18%)** produced an AI summary (AI Overview)
- Panel: Ipsos KnowledgePanel Digital — probability-based, US-only, English-skewed (generalization limit flagged by the completeness critic)

## The numbers (all exact matches to the video)

| Measure | With AI summary | Without |
|---|---|---|
| Clicked a traditional result during the visit | **8%** | **15%** |
| Clicked a link *inside* the AI summary | **1%** | — |
| Ended the browsing session right after the page | **26%** | **16%** |

- ~1 in 5 searches (18%) showed an AI summary at the time (March 2025; prevalence has grown sharply since — see [[state-of-play-2026]])
- Trigger patterns: **60%** of question-format searches (who/what/when/why) produced a summary; **53%** of 10+-word searches
- Sources cited inside AI summaries: **Wikipedia + YouTube + Reddit = 15%** of all cited links (17% of standard-result links); **.gov sites 6%** in summaries vs 2% in standard results (over-represented); **news sites 5% in both**

## Two precision notes (refuter findings)

1. The video's "for who/what/why questions, the box shows up most of the time" is a fair gloss of "60% of question-format searches" — but Pew did not rank which specific question words trigger most; it reported the aggregate for question-format queries.
2. The EN video's line "news sites barely move" is *accurate* (5% with, 5% without — unchanged). Beware the tempting misreading "news sites are barely present" — Pew's finding is *no differential*, not absence. (The VN dub's rendering drifts toward the misreading.)

## Why this study is the load-bearing one

- It is the only major *behavioral panel* measurement (real users, real devices) — everything else in this topic is either clickstream inference (SparkToro), SEO-tool telemetry (Sistrix/Semrush/Ahrefs), or publisher self-report (DCN).
- Google's rebuttals ("clicks are stable," Aug 2025 — see [[state-of-play-2026]]) have offered **no data** against it.
- It was cited in the Penske Media v. Google antitrust complaint ([[licensing-resistance]]) — the study is now litigation-grade evidence.

## Key Takeaways

- An AI summary roughly **halves** the chance a search sends anyone anywhere (15%→8%), and the citations inside it are clicked **1%** of the time — attribution exists, traffic does not.
- Summaries also **end curiosity**: 26% of sessions stop right after a summary vs 16% without — the "window shopper" chapter's strongest evidentiary base.
- The winners inside summaries are the already-huge (Wikipedia/YouTube/Reddit) and .gov; the independent expert site is structurally invisible.
- **Design lesson for any citation-bearing LLM feature (hireui's included): a source list rendered as footnotes yields ~1% engagement.** If you want sources consulted, make them the interaction (deep-links as the primary action, previews inline) — the anti-pattern is now quantified.
- Cite this study with its scope attached: US-only, March 2025, 900 adults, 68,879 searches — panel studies are strong on behavior, weak on global generalization.

Related: [[zero-click-data]] (macro numbers), [[ai-overviews-timeline]] (the product being measured), [[publisher-economics]] (revenue consequence), [[licensing-resistance]] (legal use of this study).
