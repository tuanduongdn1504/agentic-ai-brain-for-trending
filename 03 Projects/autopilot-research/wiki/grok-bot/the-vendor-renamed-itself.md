# The vendor renamed itself, and all six sources missed it

> **Grok Bot is not an xAI product. It is a SpaceXAI product.** SpaceX acquired xAI on **2026-02-02**; the combined entity was rebranded **SpaceXAI** in July 2026. Grok Bot launched **2026-08-11** — after both. **All six sources in this bundle call the vendor "xAI."** So did this ingest's own pre-flight, its four identity lenses, and the main loop's first three messages to the operator.

## The evidence

**First-party, fetched and read by the main loop:**

- [x.ai/news/xai-joins-spacex](https://x.ai/news/xai-joins-spacex) — *"SpaceX announced today that it has acquired xAI."* Dated **February 2, 2026**.
- The same page's copyright notice reads **"© 2026 SpaceXAI LLC"** — the legal entity, stated on xAI's own domain.
- The site's own title renders as **SpaceXAI**.

**Corroborating (secondary):** an all-stock merger valuing the combined entity at **$1.25 trillion** ($1T SpaceX + $250B xAI), per [CNN](https://www.cnn.com/2026/02/02/tech/spacex-acquires-xai-elon-musk) and [Yahoo Finance](https://finance.yahoo.com/news/know-spacex-xai-merger-2026-102500167.html); rebrand to SpaceXAI in **July 2026** per [Wikipedia](https://en.wikipedia.org/wiki/SpaceXAI).

Note that [InfoQ's own headline](https://www.infoq.com/news/2026/08/grok-bot-agent/) is *"**SpaceXAI** Launches Grok Bot"* — the trade press got this right while every video in the bundle did not.

## Who said what

| Source | Names the vendor | Grade |
|---|---|---|
| t1 Quân IT (anchor) | *"team XAI"*, *"từ một cái Elon M"* | **CBI** — the team is right, the corporate name is one rebrand behind |
| t2 HistoryAI | xAI | **CBI** |
| t3 How I AI | xAI | **CBI** |
| t4 Eric Nowoslawski | xAI | **CBI** |
| t5 Nate B Jones | xAI | **CBI** |
| t6 Alex Carter | *"produced by xAI and Elon Musk"* | **CBI** |
| **this ingest's pre-flight** | xAI (4 identity lenses, 3 refuters, 1 critic) | **CBI — and it ran a lens dedicated to first-party surfaces** |

**Correct-but-incomplete, not false.** "xAI" names a real organisation that really did build Grok; it is the brand the product still ships under (`x.ai`, `grok.com`). Nobody in this bundle is lying or confused about who made it. They are all carrying a name that stopped being the company's name two months before the product shipped.

## Why this is the interesting failure, not a pedantic one

**This is the corpus's cleanest example yet of a claim class that no amount of source diversity can fix.** Six independent sources, four different countries of origin, 55,000 combined words, spanning 2026-08-14 to 2026-09-11 — and the error rate on this claim is **6 of 6**.

Contrast the caption-garble class, which source diversity fixes trivially: the anchor renders the product name as *"Crockbot"*, *"Rockbot"*, *"crossbot"* and *"clockbot"*, and any one companion corrects it instantly. **Garble is noisy and self-correcting across sources. A stale-but-current brand name is silent and correlated across all of them**, because everyone reads it off the same still-live website.

This is the same structure as the vendor-seeded false claim documented in [[../hermes-agent/the-vendor-seeded-false-claim]] — *origin predicts recurrence* — with one instructive difference. There, the vendor published something false and careful creators reproduced it faithfully. Here, the vendor published something true, **stopped being that thing, and left the true-at-the-time name in place**. Same mechanism, opposite cause: **what everyone reads from one upstream surface fails together, whether the upstream is wrong or merely out of date.**

**And the pre-flight demonstrates it against its own design.** One of the four identity lenses was scoped *"FIRST-PARTY ONLY — check x.ai and its docs/blog/news."* It fetched x.ai, confirmed Grok Bot was official, and reported the vendor as "xAI (by xAI)" — reading the rebranded site without noticing the rebrand. An instrument pointed directly at the evidence returned the wrong name, because it was checking *whether the product was official*, not *who owns it now*. **A lens finds what it is looking for.**

## ⚠️ Self-correction

The main loop told the operator *"Grok Bot is a genuine **xAI** product"* three times before checking. It reached the right verdict on authenticity by reading the first-party page — and misnamed the vendor **from that same page**, because the copyright line was not what it was reading for. The correction came only when two independent sources used the unfamiliar string "SpaceXAI" and that disagreement was chased rather than normalised.

**The transferable rule: when a source uses an unexpected name for a known entity, that is a lead, not a typo.** Two sources here said "SpaceXAI" and the cheap read was garble — the corpus's own [[../homebrew-macos-package-manager/_index]] ship found *4 of 5* corrected grades were mangled proper nouns, which primes exactly the wrong instinct. The [discard-as-garble guard](../../CLAUDE.md) already says to run one search before discarding date-sensitive news. **A corporate rebrand is date-sensitive news.** The guard covered this case; it just had not been applied to an entity *name* before.

## Key Takeaways

- **Grok Bot's vendor is SpaceXAI LLC** (formerly xAI; acquired by SpaceX 2026-02-02, rebranded July 2026). Use "SpaceXAI" for the company and "xAI" only for the pre-acquisition organisation or the surviving `x.ai` brand.
- **6 of 6 sources got it wrong, and so did a lens built to check first-party surfaces.** Source diversity does not defend against a correlated upstream error.
- **Garble is self-correcting across sources; a stale brand name is not.** One is noise, the other is everyone reading the same page.
- **An unexpected name for a known entity is a lead, not a typo** — extend the discard-as-garble guard from news claims to entity names.
- **A lens finds what it is scoped to find.** The first-party lens fetched the right page and answered the question it was asked, which was not this one.

## Sources

- [x.ai/news/xai-joins-spacex](https://x.ai/news/xai-joins-spacex) — first-party, main-loop read
- [x.ai/news/introducing-grok-bot](https://x.ai/news/introducing-grok-bot) — first-party, main-loop read
- [InfoQ](https://www.infoq.com/news/2026/08/grok-bot-agent/), [CNN](https://www.cnn.com/2026/02/02/tech/spacex-acquires-xai-elon-musk) — secondary corroboration
- All six bundle transcripts in `raw/2026-09-11-grok-bot-xai-persistent-agents/`

**Related:** [[_index]] · [[what-grok-bot-is]] · [[pricing-is-a-timeline-not-a-number]] · [[claims-scorecard]] · [[caveats-and-corrections]] · [[external|hermes-agent: the vendor-seeded false claim]]
