# Zero-Click Data — SparkToro 2024/2026, "Google Zero", Gartner

## Source

- Primary: [SparkToro 2024 Zero-Click Search Study](https://sparktoro.com/blog/2024-zero-click-search-study-for-every-1000-us-google-searches-only-374-clicks-go-to-the-open-web-in-the-eu-its-360/) (Rand Fishkin, 2024-07-02; Datos/Semrush clickstream panel, Sept 2022–May 2024)
- Primary: [SparkToro 2026 follow-up — "In 2026, Less than One Third of Google Searches Still Send a Click"](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/) (Jan–Apr 2026, Similarweb panel)
- Primary: [Gartner press release 2024-02-19](https://www.gartner.com/en/newsroom/press-releases/2024-02-19-gartner-predicts-search-engine-volume-will-drop-25-percent-by-2026-due-to-ai-chatbots-and-other-virtual-agents) (Alan Antin, VP Analyst)
- Nilay Patel "Google Zero": [The Verge article + Decoder episode, 2024-05-30](https://www.theverge.com/2024/5/30/24168047/google-zero-is-here-now-what) (episode interviews Sundar Pichai); explainer: [Digiday "WTF is Google Zero"](https://digiday.com/marketing/wtf-is-google-zero/)
- Video chapters 1–2 · verified by workflow `wf_7208577a-1cc` (C1 CONFIRMED ×2, C2 PARTIAL ×2, C3 PARTIAL, C4 PARTIAL — details in [[source-provenance]])

## The 2024 numbers (what the video cites — all exact)

- **58.5%** of US Google searches ended in zero clicks; **59.7%** in the EU ✅ exact match to primary
- Per 1,000 US searches: **360 clicks** reach a non-Google-owned, non-Google-ad property (EU: 374) ✅ exact
- **~28.5% of clicks** (SparkToro's own gloss: "almost 30%") go to Google-owned properties — YouTube, Maps, Images, Flights… The video's "close to 30% go to Google's own sites" is faithful to SparkToro's phrasing; the precise figure is 28.5%, *and it is a share of clicks, not of searches*
- Methodology: Datos (a Semrush company) clickstream panel, "tens of millions" of devices; weighted ~63% mobile; known limitation: thin iOS coverage
- Lineage: Fishkin first quantified zero-click in 2019 (~49%, Jumpshot data); 2021 (Datos) ~64.8%. Numbers across years use different panels — **not a clean time series** (the 2024 "58.5%" is not comparable 1:1 with the 2021 "64.8%")

## The 2026 follow-up (post-video-source; the video does not have this)

- **68.01%** of US Google searches ended without a click (Jan–Apr 2026) — up from ~60.45% in 2024 by the 2026 study's own recomputation
- **276 clicks per 1,000 searches** reach the open web — down from 360 in 2024 (−26% in two years)
- Panel switched to Similarweb — again, cross-study comparisons are directional, not exact

## "Google Zero" (Nilay Patel)

- Coined by Nilay Patel (Editor-in-Chief, The Verge) in 2024: the point where Google referral traffic to a site falls to (almost) zero — Google stops being a gateway and becomes an answer engine
- Canonical artifacts: The Verge piece + Decoder episode "Google Zero is here. Now what?" (both 2024-05-30; the Decoder episode is an interview with Sundar Pichai)
- By 2026 the term is industry-standard — e.g., Digital Content Next's ["Publisher's Playbook for the Google Zero Era"](https://digitalcontentnext.org/blog/2026/04/09/the-publishers-playbook-for-the-google-zero-era/) (2026-04-09)

## The "search volume will fall 25%" prediction

- Source: **Gartner, 2024-02-19** (Alan Antin): "search engine volume will drop 25% by 2026, due to AI chatbots and other virtual agents"
- The video says "experts predict" — it is a single-firm prediction, not a consensus (critic flag)
- Scorecard as of mid-2026: no Gartner reforecast found; adjacent real-world data — Chartbeat (via Reuters Institute): Google referral traffic to 2,500+ publisher sites **−33% globally / −38% US** Nov 2024→Nov 2025. Note that is *referral traffic*, not *search volume* — the two are different quantities; search volume itself may be stable-or-up while clicks-out collapse (Google's own framing in [[state-of-play-2026]])

## Key Takeaways

- The video's zero-click numbers are exactly right and exactly sourced; what it couldn't include is that the 2026 refresh is materially worse (68%, 276/1,000).
- "Zero-click" ≠ "user got nothing" — it includes answered-on-page (AI Overview, knowledge panel, featured snippet) *and* abandonment/refinement; it also ≠ "Google captured the click" (the 28.5% Google-property share is a separate slice).
- Panel-based clickstream studies are directionally strong, precision-weak: three different panels (Jumpshot → Datos → Similarweb) across 2019-2026. Quote single-study numbers with their year and panel.
- "Google Zero" is the vocabulary word this whole topic hangs on: use it for the platform-dependency conversation in [[../google-zero-open-web/caveats-and-corrections|any team retro]] — "what's our Google Zero?"
- Gartner's 25% was a prediction about *query volume*; the measured catastrophe is in *outbound clicks*. Don't conflate them when citing.

Related: [[pew-ai-overviews-study]] (the per-search behavioral mechanism), [[state-of-play-2026]] (2026 refresh), [[publisher-economics]] (what the lost clicks cost).
