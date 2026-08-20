# The star numbers, and grading "fastest growing repo EVER"

> The anchor video's title is a superlative. This page grades it. Short answer: **the numbers are accurate, the trajectory is real, and the superlative is press-repeated but not primary-sourced.**

## The trajectory is internally coherent

Six independent readings across four days, plus the vault's own source-level snapshot:

| Date | Source | Stars | Forks |
|---|---|---|---|
| 2026-08-17 | The Cef Experience | 135,000 | — |
| 2026-08-17 | Turing Post TV | 147,000 | 15,000 |
| 2026-08-17 | external reporting (official counter) | 141,532 | 14,350 |
| 2026-08-18 | Firecrawl | "over 150,000" | — |
| 2026-08-18 | VN (Code Bug) | 158,000 | — |
| 2026-08-18 | **vault v242 source-level read** | **159.0k** | — |
| 2026-08-19 | Better Stack | 150,000 | — |
| **2026-08-20** | **this ship, fetched directly** | **169.1k** | **18.1k** |

**Every reading is within a day's drift of its neighbours, and the vault's own independent snapshot (159.0k on 8/18) sits exactly between the videos on either side.** The growth curve — roughly 5–10k stars/day at this stage — is consistent across sources with no coordination.

Two mild outliers, both same-day and both explicable by time-of-day: Cef's 135,000 runs low against the 141,532 official figure for 2026-08-17, and Turing Post's 147,000 runs high. Better Stack's 150,000 on 8/19 is stale-low, likely recorded before publication.

**Chase AI's anchor claim — "167,000 stars" on 2026-08-20 — is accurate to within ~1% of the 169.1k this ship measured the same day.** Graded CONFIRMED.

## The superlative: what holds and what doesn't

Chase AI: *"it has become the fastest growing repo ever."* Firecrawl's title: *"This Free Harness Just Broke GitHub."* The VN source makes the narrower, checkable version: *"cái tốc độ tăng trưởng này nó còn nhanh hơn cả thằng OpenClaw đợt trước"* (this growth rate is even faster than OpenClaw).

**What external verification supports:**
- ~20,000 stars in about **one hour**; ~100k in **under 48 hours**.
- The prior pure-speed reference point was xAI's Grok-1 at about **1.2 days** to the same mark.
- DeepSeek's own R1 model repo took **5.7 days** to reach 20,000.
- Multiple independent reports name **OpenClaw** as the previous holder — which is precisely the comparison the VN source made independently, without citing anyone.

**What breaks the superlative:**

> **GitHub publishes no official star-velocity record, and no primary source — not DeepSeek, not GitHub — has made the "fastest in history" claim.**

So "fastest growing GitHub repo ever" is a **press-consensus inference from page-stated star counts**, not a verified record against a maintained leaderboard. It is very likely directionally true. It is not a fact the vault can cite.

**Verdict: PLAUSIBLE — NOT PRIMARY-VERIFIED.** The vault may state "reportedly the fastest star-growth on record, though no official leaderboard exists"; it may not state "the fastest growing repo ever."

## Standing vault rule, refined

The v242 PIN says: **do not cite any star figure** — 159.0k was page-stated, and DSH's own web-UI tooling mocks the GitHub API.

**This ship refines rather than overturns that rule, and the distinction is worth keeping straight:**

- The **mocked-API** caveat is about figures *rendered by DSH's own surfaces* (v239's finding). A star count shown inside DSH Market or the dsh-web-ui is not evidence of anything.
- The **page-stated** caveat is about figures read off github.com — including this ship's 169.1k. Still page-stated, still not API-verified.

**But six independent page-stated readings plus the vault's own, all mutually consistent across four days, is meaningfully stronger evidence than one.** The refined rule: *cite star figures only with a date stamp and the words "page-stated"; never cite a figure sourced from DSH's own UI; never cite a velocity record.*

The VN source models the right instinct here without being told — see his star-provenance doubt in [[deepseek-harness/ecosystem-and-the-catalogue-gap]].

## What the velocity actually signals

Turing Post is the only source that reads the number as evidence about something other than quality:

> *"The GitHub explosion is the visible story. Underneath it, DeepSeek released the assistant while its architecture was open enough for everyone to inspect, modify, and copy."*

And she notes the revealing asymmetry: the harness is at ~147k while **the paper's repo sits at ~2.4k**. *"The crowd has clearly chosen the object with the buttons, but the paper may be the even more important release."*

**That ratio — roughly 70:1 — is the most informative number in this whole page.** It says the star count is measuring attention to an installable artifact, not assent to an architectural argument. Anyone citing 169k as evidence that the industry has adopted spatiotemporal composability is misreading it by a factor of seventy.

## Cross-links

[[deepseek-harness/_index]] · [[deepseek-harness/hype-vs-source-scorecard]] · [[deepseek-harness/claims-scorecard]] · [[deepseek-harness/cordis-and-the-paper]] · [[deepseek-harness/ecosystem-and-the-catalogue-gap]] · [[deepseek-harness/caveats-and-corrections]]
