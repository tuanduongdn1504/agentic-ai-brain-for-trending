# Caveats & Corrections — Every Video Claim Graded

## Source

Workflow `wf_7208577a-1cc` (13 deep-divers + 24 refute-first verifiers + completeness critic) + main-loop gap-closes. Full verdict trail in [[source-provenance]].

## Scorecard (16 pre-registered claims)

| # | Claim (video) | Verdict | Note |
|---|---|---|---|
| C1 | 58.5% US / 59.7% EU zero-click (Fishkin) | ✅ CONFIRMED ×2 | Exact match to SparkToro 2024-07-02 |
| C2 | 360/1,000 clicks reach open web; ~30% of clicks to Google properties | ✅ (precision: 28.5%) | "Close to 30%" is SparkToro's own gloss; share of *clicks*, not searches |
| C3 | Nilay Patel coined "Google Zero" | ✅ (format nuance) | Verge/Decoder 2024-05-30; definition accurate |
| C4 | "Experts predict search volume falls 25%" | ✅ attribution / ⚠️ framing | It's ONE source (Gartner, Feb 2024, by-2026 prediction), not expert consensus; outcome unmeasured |
| C5 | HouseFresh: British, tested purifiers, ranked top, −91% after "the update" | ✅ w/ 2 nuances | Ranked **#2** not #1; damage cumulative over **two** updates (Sept 2023 HCU + Mar 2024 core) |
| C6 | NYT "code red"; engineers reassigned; founders recalled | ✅ CONFIRMED | Via 5 independent secondaries citing NYT (primary paywalled) |
| C7 | SGE 2023 → AIO May 2024; glue/rocks; official response; AI Mode | ✅ CONFIRMED | All four sub-parts verified incl. The Onion + "fucksmith" provenance |
| C8 | All ten Pew numbers | ✅ CONFIRMED | Every number exact vs pewresearch.org; two paraphrase footnotes ([[pew-ai-overviews-study]]) |
| C9 | March 2024 update pushed experts down, forums up | ⚠️ PARTIAL | **Correction: the boost began fall 2023** (Hidden Gems + HCU); March 2024 intensified it |
| C10 | $60M Reddit deal; +1,300% visibility; 22M→41M pages; **"#2 most-visited from Google search after Wikipedia"** | ⚠️ last part ❌ | Deal/1,328%/pages ✅; the #2 line **conflates three different rankings** — Reddit = #2 US site overall & #2 AIO-cited domain; #3-4 in search visibility |
| C11 | Reddit blocked all other search engines; OpenAI deal "reported $70M" | ⚠️ PARTIAL | Lockdown ✅ (2024-07-01, Google-only); **"$70M" was never reported — it is derived arithmetic** from Reddit revenue disclosures; terms undisclosed |
| C12 | Raptive $2B; 20-60% traffic loss; McCollum "low end" revision | ✅ CONFIRMED ×2 | Name is Marc **McCollum**, Chief Innovation Officer (VN dub garbles to "McCallum"); $2B is a *model* |
| C13 | Germany: hundreds of millions of clicks lost monthly | ✅ CONFIRMED ×2 | SISTRIX Feb 2026: **265M/month** — the video's vaguest-sounding claim had the hardest data |
| C14 | Monopoly ruling; soft remedies; appeal | ✅ CONFIRMED | Omits the DOJ *cross*-appeal (post-dates script sources) |
| C15 | Model collapse ("copies of copies") + AI-slop flood | ⚠️ PARTIAL | Lab-real (Nature 2024); **production-unproven**; Schaeffer 2025 says avoidable; slop numbers need detector-error bars ([[model-collapse-and-ai-slop]]) |
| C16 | "Really simple licensing" — music-industry playbook | ✅ CONFIRMED | RSL is real, ASCAP/BMI-modeled, 1,500+ publishers; **VN dub loses the proper noun** |

## The corrections to never re-propagate

1. **"Reddit became the second-most-visited site from Google search"** → conflation; say: #2 US website overall (2025) and #2 most-cited domain in AI Overviews; #3-4 in Google-search visibility indexes.
2. **"OpenAI paid a reported $70M"** → never reported; derived estimate ($130M AI-licensing revenue − $60M Google); terms undisclosed.
3. **"The March 2024 update did it"** → fall 2023 (Hidden Gems + Sept HCU) started the forum boost and small-site purge; March 2024 completed it.
4. **"Google is worth about $2 trillion"** → stale 2024-era figure; Alphabet was ~**$4.3T** at video air date (June 2026, stockanalysis.com/companiesmarketcap.com) — the script's number is half reality, which *understates* the video's own thesis about Google's scale.

## Reported-only / unverified flags

- "Washington Post cut one-third of staff" (Q1-2026 layoff roll-up) — single aggregator source (MediaCopilot); treat as reported-only
- HouseFresh's exact 2026 recovery state — conflicting accounts (visibility recovered vs traffic partial); unresolved ([[housefresh-case-study]])
- Gartner 25%-by-2026 outcome — no reforecast/scorecard found; adjacent Chartbeat data measures *referrals*, not query volume
- Datos panel scale ("tens of millions of users") — vendor-stated, not independently audited
- Schaeffer et al. 2025 — position paper/preprint; venue acceptance unconfirmed
- The glue-pizza Reddit comment's exact age — sources vary ("11-year-old"/"13-year-old"); "a decade-old joke comment by user 'fucksmith'" is the safe form

## VN-dub-specific losses (for anyone quoting the VN version)

- "Really Simple Licensing" → generic "cơ chế cấp phép cực kỳ đơn giản" (proper noun lost — the most actionable artifact in the video becomes unfindable)
- "Marc McCollum" → "Mark McCallum"; "Perplexity" → "Perplex City"; "Quora" → "Quar"; "Raptive" → "Raptive/Ractive" varies
- Pew paraphrase drifts toward "news sites barely present" (EN original's "news sites barely move" is the accurate form)

## Key Takeaways

- Verdict distribution: ~9 CONFIRMED, 6 PARTIAL (nuance/timeline), 1 sub-claim REFUTED — by far the most accurate mass-market explainer the corpus has verified.
- All four hard corrections are *secondhand-compression* errors (conflated rankings, derived numbers reported as reports, timeline compression, stale valuations) — exactly the error class the verify-before-cite rule targets.
- The video's rhetorical frame ("deliberate murder of the web") exceeds its evidence; the verified frame is "deliberate self-preservation whose collateral damage is the open web, undisputed by the measurements."
