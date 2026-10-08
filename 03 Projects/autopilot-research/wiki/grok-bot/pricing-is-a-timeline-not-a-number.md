# Pricing is a timeline, not a number

> **There is no first-party dollar price for Grok Bot. There cannot be — it has no SKU.** Every figure in this bundle is the price of a *host subscription* that bundles a Grok Bot allowance. The pre-flight critic blocked the ship over *"three unresolved, conflicting price points."* They were never in conflict: **most are four different dates, and the rest are category errors.**

## The eligibility timeline

Grok Bot's entry price fell 10× in fifteen days — **not because anything got cheaper, but because progressively lower tiers gained access.** This is a rollout, not a discount.

| Date | Newly eligible tiers | Individual floor |
|---|---|---|
| **2026-08-11** launch | Cursor **Ultra $200**/mo · SuperGrok **Heavy ~$300**/mo · Cursor Teams **Premium $120**/seat | **$200** |
| **2026-08-21** | Cursor **Pro+ $60** · SuperGrok **Plus $100** · Cursor Teams **Standard $40**/seat · **+ free trial** *("a free trial with limited usage for all other users")* | **$60** |
| **2026-08-26/27** | Cursor **Pro $20** · SuperGrok **$30** | **$20** |

That reaches the **eight tiers** the current `x.ai` page lists. Cursor Teams Premium seats: **$120/mo**, **$96** annual, 5× usage at 3× Standard, renewals from 2026-07-01.

## What first-party actually says about money

`x.ai/news/introducing-grok-bot` **names no figure at all** — independently fetched and confirmed by two separate graders. `docs.x.ai/grok-bot/faq` says only:

> *"Subscriptions include weekly usage with optional on-demand billing."*

and

> *"Eligible accounts can add on-demand usage billed from model and token cost."*

Cursor's side is the only place a dollar amount is first-party: `cursor.com/pricing` shows Individual at **"$20 / mo."** with tiers Pro / Pro+ / Ultra and a literal **"✓ Grok Bot access"** row, plus *"On-demand usage allows you to continue using models after your included amount is consumed, billed in arrears."*

**The structural facts, which survive any future price change:**

1. **You cannot buy Grok Bot.** No standalone SKU. *"What does Grok Bot cost"* has no answer — only *"what is the cheapest plan that includes it."*
2. **The included allowance is a weekly quota whose size is not published.** Launch-week reports describe it exhausted in **one or two days** of heavy use.
3. **Overage bills at model and token cost, in arrears.** The headline price is a **floor, not a cost.**

## Claim-by-claim

| Source | Date | Figure | Grade |
|---|---|---|---|
| **t5 Nate B Jones** | 08-14 | **$200**; *"no $20-25 category"* | **TIME-BOUND** — both correct on his date, 3 days post-launch. His hedged *"$300 for SuperGrok Heavy"* and *"ultra or super heavy"* eligibility were **accurate at publication**; the apparent clash with today's eight-tier page is an artifact of reading that page now. Only publication-time omission: Teams Premium. **He wins the launch-date question and cannot be cited for current pricing.** |
| **t6 Alex Carter** | 08-23 | three-tier eligibility | **STALE BY THREE TIERS** — published two days *after* the 08-21 expansion, so the correct list that day was six. His *"not for someone with a $20 subscription"* was literally true when said and false three days later. |
| **t1 Quân IT** (anchor) | 09-11 | upgrade screen shows **"20"**, tiers **"Pro" / "Pro Plus"** | **UNVERIFIED as a Grok Bot price.** *"Pro"/"Pro+" are **Cursor** tier names* — Grok-side tiers are SuperGrok / Plus / Heavy; there is no Grok "Pro". The 20 is almost certainly **Cursor Pro $20/mo**. The source does not disambiguate and this wiki will not resolve it for him. |
| **t1 Quân IT** (anchor) | 09-11 | **"$50"** | **NOT A PRICE.** This is his own **user-set on-demand spend cap**, entered on a screen also showing *"reset in N days"* and *"open dashboard"* — not a tier, not a vendor figure. Do not file it alongside $20/$200. ⚠️ *An earlier draft of this article mis-filed it as an unverified tier price.* |
| pre-flight agents | 09-11 | *"$20 / $50 / $200-300"* | **CONFLATION** — mixed the launch floor, the Heavy tier, and a user's spend cap into a false contradiction, then recommended blocking the ship over it. |

## The grader's own trap

The compile's per-source verifier marked Alex Carter **stale by five tiers**, measuring him against the **current** eight-tier page — which postdates his video by three days. The cross-source reconcile pass caught it and corrected to three.

**A dated claim measured against a live page produces a false error.** That is a defect in the *checking* method, not the source, and it is the mirror image of the vendor-headline problem: there, everyone read the same page and was wrong together; here, the checker read the *right* page at the *wrong time*. **Both failures come from treating a web page as timeless.** Any grader touching a fast-moving product needs the claim's publication date pinned to it, or it will manufacture errors.

## Key Takeaways

- **No SKU, no price.** Grok Bot is bundled into eight host tiers with a separate, unpublished weekly quota and uncapped token overage in arrears.
- **Four "conflicting" figures, zero conflicts** — three dates and one category error. `TIME-BOUND` is the right grade for nearly all of it.
- **Never average prices across dates.** Averaging $200 and $20 gives $110, true on no day. Cleanest instance yet of "surface conflicts, don't average them."
- **The entry price fell by expanding eligibility, not by discounting.** Nothing got cheaper; more tiers got included.
- **A date is the cheapest defence a claim can carry** — and the cheapest way for a *checker* to be wrong is to omit it.
- **The anchor's "$50" is a spend cap he chose**, and its "20" is a Cursor tier. Neither is a Grok Bot price.

## Sources

- `x.ai/news/introducing-grok-bot` (names no figure) · `docs.x.ai/grok-bot/faq` · `cursor.com/pricing` · `cursor.com/blog/teams-pricing-june-2026` — first-party
- Secondary pricing aggregators corroborate the timeline's **shape**; no individual figure below tier level is first-party confirmed
- `raw/2026-09-11-grok-bot-xai-persistent-agents/` — all six transcripts

**Related:** [[_index]] · [[what-grok-bot-is]] · [[one-computer-per-user-not-per-bot]] · [[the-vendor-renamed-itself]] · [[claims-scorecard]] · [[caveats-and-corrections]]
