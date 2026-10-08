# Claims scorecard — 160 claims across 6 sources

> **160 graded claims.** Every claim was extracted by a per-source Opus digest reading its transcript in full, then graded **refute-first** against first-party and independent evidence by a second Opus pass, then reconciled across sources by a third. **14 agents, 0 errors, 0 empty returns, 1.35M tokens** (workflow `wf_c3cb4b9e-bbe`).

## By source

| Source | Claims | Hard error | CONFIRMED | UNVERIFIED | FALSE | CONTRADICTED |
|---|---|---|---|---|---|---|
| HistoryAI (⚠️ paid) | 17 | **5.9%** (1) | **64.7%** | low | 0 | 0 |
| How I AI | 40 | 10.0% (4) | 32.5% | — | — | — |
| **Quân IT** (anchor) | **36** | **11.1%** (4) | 19.4% | **44.4%** | **0** | **0** |
| Nate B Jones | 22 | 13.6% (3) | 31.8% | — | 1 | 1 |
| Eric Nowoslawski | 27 | 14.8% (4) | 22.2% | — | — | — |
| Alex Carter (crypto) | 18 | **16.7%** (3) | 38.9% | low | 1 | — |

*Hard error = CORRECTED + FALSE + MISLEADING + CONTRADICTED-IN-BUNDLE. Anchor detail: 7 CONFIRMED / 8 CBI / 3 CORRECTED / 1 MISLEADING / 16 UNVERIFIED / 1 UNFALSIFIABLE.*

⚠️ **Do not quote this as a ranking.** It reverses under two defensible attribution calls — see [[the-anchor-audit]]. The **error signature** (fabrication vs dropped qualifier) is the robust reading; the rate is not.

## The two decided contradictions

**1. One computer per bot, or per account? — 4 vs 2, and the minority wins.**
Quân IT, HistoryAI, How I AI and Eric all assert per-bot isolation. Nate and Alex Carter assert one per account. **Nate + Alex Carter win decisively on verbatim first-party text** (`docs.x.ai/grok-bot/faq`: *"Every Bot on your account uses one persistent cloud computer… assigned per user, not per Bot. Do not use separate Bots as a security boundary"*). The majority is wrong because all four reproduce the launch-page headline — **one vendor simplification propagated four times**, which is why majority count is worthless here. Full analysis: [[one-computer-per-user-not-per-bot]].

**2. Is the security perimeter a feature or a blast radius?**
Nate: *"adding more agents doesn't add to that security perimeter"* and *"a much more secure version of OpenClaw."* Alex Carter: a login or file on that machine is available to every bot the user runs. **Alex Carter wins** on the docs' own operational rule. Nate states the numerator and omits the exposure: more bots do not add perimeters, they add **reach inside the one perimeter**, so a single prompt-injected bot inherits **every credential on the machine.** His *"much more secure"* is unfalsifiable and contestable on his own premise.

## Grade classes used

`CONFIRMED` · `CBI` (correct-but-incomplete — a dropped load-bearing qualifier; **the dominant real defect in this bundle**) · `CORRECTED` · `MISLEADING` · `FALSE` · `UNVERIFIED` · `TIME-BOUND` · `CONTRADICTED-IN-BUNDLE` · `UNFALSIFIABLE` · `FABRICATED` (**0 instances**).

## Where the dominant defect sits

**Caption garble mangles proper nouns; it does not corrupt reasoning.** The anchor's product name is destroyed throughout — *Crockbot / Rockbot / crossbot / clockbot* → **Grok Bot**; *Rock AI* → **Grok**; *con boss* → **bots**; *Cyberc ở Austin Texas* → **Cybercab**; *DNG* → **DMG**; *Elon M* → **Elon Musk**. Every one is graded on substance, per project rule. One remains unresolved: *"slash"* is either **Slack** or **slash-commands** and the context does not settle it — left open rather than guessed.

**The substantive defect is different and more interesting: the dropped qualifier.** Per-bot vs per-account computer. *Publish* vs *buy* in the marketplace. General xAI docs vs the Grok Bot doc tree. "xAI" vs SpaceXAI. "Not used for training" vs "follows your Cursor settings." In each case the source says something true-shaped about something real and omits the clause that decides it.

## ⚠️ Overrides logged by the main loop

Agent grades were **not** accepted as final. Three overrides, each with the evidence that forced it:

1. **Vendor name.** No agent flagged it; all six sources and all pre-flight agents said "xAI." Overridden to **SpaceXAI LLC** on first-party evidence (`x.ai/news/xai-joins-spacex`, *"© 2026 SpaceXAI LLC"*). → [[the-vendor-renamed-itself]]
2. **Pricing.** The per-source verifier graded Alex Carter *"stale by five tiers"* by measuring a 2026-08-23 claim against **today's** eight-tier page. Corrected to **three** by the reconcile pass. A dated claim measured against a live page manufactures a false error. → [[pricing-is-a-timeline-not-a-number]]
3. **The ingest's own ground truth.** The main loop passed the launch-page sentence *"Bots have their own computer"* into the workflow **as verified fact**. It is the marketing simplification the FAQ contradicts. Two graders caught it by going past the announcement — the process worked *against* its own brief. → [[one-computer-per-user-not-per-bot]]

## ⚠️ Provenance: two apparent corroborations that are not

**How I AI's** figures are matched by her own companion page on `chatprd.ai` — **same author**. **HistoryAI's** bot roster is self-reported. **Author-to-own-writeup agreement establishes transcription fidelity, not accuracy**, and counts as one source. This is the v283 *"fidelity is not accuracy"* finding recurring in a new form.

## Key Takeaways

- **160 claims, 0 FABRICATED.** The bundle's problem is not invention, it is omission.
- **CBI is the dominant grade class.** Sources drop the qualifier that decides the sentence.
- **The minority won both decided contradictions**, both times on verbatim first-party text, both times against four sources reciting the same headline.
- **Three main-loop overrides were needed**, one of them against this ingest's own ground truth.
- **Same-author corroboration is not corroboration.**

**Related:** [[_index]] · [[the-anchor-audit]] · [[one-computer-per-user-not-per-bot]] · [[pricing-is-a-timeline-not-a-number]] · [[the-vendor-renamed-itself]] · [[caveats-and-corrections]]
