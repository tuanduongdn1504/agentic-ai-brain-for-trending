# One computer per user, not per bot

> 🔴 **The load-bearing security fact, and the bundle got it backwards 4-to-2.** SpaceXAI's launch headline says *"Bots have their own computer."* Its own FAQ says the opposite: **one persistent cloud computer per USER**, shared by every bot on the account — sharing files, browser sessions and logins — and *"Do not use separate Bots as a security boundary."*

## The first-party text

From `docs.x.ai/grok-bot/faq`, under the question *"Do my Bots share one computer?"*:

> *"**Yes.** Every Bot on your account uses one persistent cloud computer. They share its files, browser sessions, and logins so they can hand work off. The computer is assigned **per user, not per Bot**. **Do not use separate Bots as a security boundary.**"*

From `docs.x.ai/grok-bot/security-faq`:

> *"Each user gets a dedicated **Firecracker microVM**"* — but *"Within one user, **every Bot shares that computer**."*

Each bot gets its own **screen**, and screens are *"work surfaces, not separate security boundaries."* The operational rule the docs give: **a workload that needs its own credential set needs its own Cursor user**, not its own bot.

Independently corroborated by TechTimes on day two (2026-08-12): all bots share one cloud computer and every login.

## Who said what

| Source | Claim | Verdict |
|---|---|---|
| t5 Nate B Jones | one computer per **account**, shared | ✅ **CORRECT** |
| t6 Alex Carter | isolation is per user, not per bot; a login or file is available to every bot | ✅ **CORRECT** |
| t1 Quân IT (anchor) | *"each Grok Bot gets its own always-on virtual computer"* | ❌ wrong |
| t2 HistoryAI | *"every Grok Bot has a virtual machine"* | ❌ wrong |
| t3 How I AI | per-bot isolation | ❌ wrong |
| t4 Eric Nowoslawski | per-bot isolation | ❌ wrong |

**Majority count is worthless here.** The four wrong sources are not four independent errors — they are all faithfully reproducing the launch page's headline. **One vendor simplification, propagated four times.** A 4-to-2 majority against the vendor's own FAQ is what correlated upstream error looks like from inside a bundle.

**Status did not predict accuracy.** The two sources that got it right are a **$200-skeptic** and a **crypto-promo channel**. The two that got it wrong include the **paid sponsored walkthrough** and the **312,210-view flagship**. On the single most safety-relevant fact in the topic, reach, sponsorship and independence all failed as proxies.

### The anchor's near-miss is the sharpest moment in the bundle

Quân IT **captured the correct FAQ text on camera** — and then talked himself out of it. Judging that his auto-captions had dropped a negation, he proposed a "correction" that **inverts the truth**. He aimed his skepticism at the caption layer instead of at the vendor headline. He had the right answer on screen and reasoned his way off it, because the marketing claim was the more plausible prior.

## Why this matters operationally

Nate states the numerator and omits the exposure. *"Adding more agents doesn't add to that security perimeter"* is true — and the consequence is that **adding bots adds reach *inside* the one perimeter.** A single prompt-injected bot inherits **every credential on the machine.** His *"much more secure version of OpenClaw"* is unfalsifiable and contestable on his own premise.

The bundle's own demos show the blast radius, without noticing it:

- **Eric Nowoslawski** writes a `.env` containing a **plaintext username and password** — onto a filesystem *"visible to every Bot."*
- **HistoryAI** authenticates a **DoorDash session with a card on file** in the shared browser — reachable by **all 13** of his bots, not just the one he built for it.
- **HistoryAI records zero security reservations** across 3,148 words.

🔴 **For this operator specifically:** this is the same shape as the BOLA finding in [[../ai-text-watermarking/_index]] and the class [[../api-security-7-techniques/_index]] names as the **#1 unmitigated risk** for `hireui`. Shared browser sessions plus agent autonomy plus candidate PII is precisely the combination to keep away from a production hiring pipeline. If Grok Bot is ever piloted here, **one Cursor user per trust domain** is not a nicety — it is the only boundary the vendor will stand behind. And note the privacy stack: `docs.x.ai/grok-bot/approvals-security-and-privacy` says only *"Training opt-out follows the applicable Cursor account and privacy settings"* — the no-training state is **conditional on Cursor configuration**, never asserted flatly for Grok Bot.

## ⚠️ This ingest made the same mistake

The main loop fetched the launch page, quoted *"Bots have their own computer"* to the operator as verified first-party fact, and then **passed that sentence into the compile workflow as `GROUND_TRUTH` with instructions to treat it as given.** The error was upstream of every agent that inherited it.

Two graders caught it anyway, by going past the announcement to the FAQ. **That is the process working, but it worked against the ingest's own ground truth, not with it** — and it only worked because the agents were told to verify refute-first against first-party material rather than trust the brief.

**The transferable rule: a launch announcement is marketing, not documentation.** Quote it for intent and positioning; never let it stand as the mechanism. The mechanism lives in the FAQ, the security docs and the changelog — the pages written for people who have already bought.

## Key Takeaways

- **One Firecracker microVM per user; every bot on the account shares it** — files, browser sessions, logins. Per-bot screens are work surfaces, not boundaries.
- **The vendor says in writing: do not use separate bots as a security boundary.** Use separate Cursor users.
- **4 of 6 sources are wrong because they all quote the same headline.** Majority voting cannot detect a correlated upstream error — this is the third instance of that mechanism in the corpus, after [[the-vendor-renamed-itself]] and [[../hermes-agent/the-vendor-seeded-false-claim]].
- **A prompt-injected bot inherits every credential on the shared machine.** Two of the bundle's own demos put plaintext credentials and a card-on-file session inside that blast radius on camera.
- **Neither reach, sponsorship, nor independence predicted accuracy** on the one fact where being wrong is expensive.
- **A launch page is not documentation.** This ingest quoted one as ground truth and was corrected by its own verifiers.

## Sources

- `docs.x.ai/grok-bot/faq` and `docs.x.ai/grok-bot/security-faq` — first-party, the deciding evidence
- `docs.x.ai/grok-bot/approvals-security-and-privacy` — the conditional training opt-out
- TechTimes, 2026-08-12 — independent day-two corroboration
- All six transcripts in `raw/2026-09-11-grok-bot-xai-persistent-agents/`

**Related:** [[_index]] · [[what-grok-bot-is]] · [[the-vendor-renamed-itself]] · [[claims-scorecard]] · [[caveats-and-corrections]] · [[external|api-security-7-techniques]] · [[external|ai-text-watermarking]]
