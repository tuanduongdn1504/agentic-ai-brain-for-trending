# What Grok Bot is

> **A persistent-agent platform from SpaceXAI, launched 2026-08-11.** You name a bot, give it instructions in conversation, and it works on a cloud computer that keeps running when your laptop is closed. The distinguishing primitive is not the model — it is the **always-on machine with a browser, a filesystem and a terminal**, and a **human take-over handoff** when the bot hits a wall it should not climb.

**Vendor naming:** the company is **SpaceXAI LLC** (SpaceX acquired xAI 2026-02-02; rebranded July 2026). Products still ship under the `x.ai` / Grok brand. See [[the-vendor-renamed-itself]].

## The architecture

**One persistent cloud computer per USER** — a dedicated **Firecracker microVM** — shared by every bot on the account, which share its files, browser sessions and logins so they can hand work off. Each bot gets its own **screen**; screens are *"work surfaces, not separate security boundaries."*

🔴 **This is the one fact four of six sources get wrong**, because the launch page's headline says *"Bots have their own computer."* The docs say *"Do not use separate Bots as a security boundary."* Read [[one-computer-per-user-not-per-bot]] before piloting anything — it is the load-bearing security fact of the whole topic.

**What a bot can reach:** a real browser, a filesystem, a terminal, and sign-ins to the SaaS tools you already use. Connectors appear as **Plugins** in Settings and are **account-wide** (the docs do not enumerate them). Because the bot drives an actual browser, **a missing connector is not a blocker** — it navigates the site like a person, and when it hits a login wall or a consent screen it **stops and hands off to you**. That handoff is why the product needs no code and no API keys, and it is the mechanism the anchor demonstrates most clearly: *"Action needed nè. Đó mình sẽ take over nè."*

**Persistence and memory:** bots hold conversation context, remember preferences and workflows, and can be **taught a process by watching you do it once**, after which the workflow is saved and re-runnable. Multiple bots can be assigned to one workflow and coordinate.

## Access and distribution

- **Desktop app** — macOS, Windows, Linux; **companion app** — iOS, Android. (The anchor installs the macOS build from a `.dmg`.)
- **Two identity families**, which are the only documented access routes: **Grok-side** (SuperGrok / Plus / Heavy) and **Cursor-side** (Pro / Pro+ / Ultra / Teams Standard & Premium).
- **Cursor is a co-vendor, not a detail.** `cursor.com/pricing` carries a literal *"✓ Grok Bot access"* row, and `docs.x.ai/grok-bot/faq` routes enterprise access to *"your Cursor account team."* A pure "xAI/Elon built this" frame — the anchor's frame — **misses the company that actually gates access and billing.**
- **Marketplace** at `x.ai/bot/marketplace` — externally verified at **71 public bots, 43 creators, 9 categories** (Engineering, Sales, Marketing, Design, Personal, Recruiting & People, Operations, Product…). Bots are **published and "Added" — not bought.** No price or purchase surface exists anywhere on it.
- **Documentation** — a dedicated tree at `docs.x.ai/grok-bot/`: `overview`, `faq`, `computer-and-apps`, `approvals-security-and-privacy`, `security-faq`, plus guides at `x.ai/bot/guides`. ⚠️ The anchor reports *"there is no Grok Bot–specific documentation"* and infers from its thinness that no programming knowledge is needed. **The doc tree exists** — he likely landed on the API docs root. The conclusion is right, the reason is wrong: no code is needed because of the browser-plus-take-over design, not because the docs are short.

## Pricing, in one line

**There is no Grok Bot price** — no SKU. It is bundled into eight host tiers with a separate, **unpublished** weekly quota and **uncapped** token overage billed in arrears. The entry floor fell $200 → $60 → $20 between 2026-08-11 and 2026-08-26 by *expanding eligibility*, not by discounting. Full timeline in [[pricing-is-a-timeline-not-a-number]].

## Privacy posture

`docs.x.ai/grok-bot/approvals-security-and-privacy` says only: *"Training opt-out follows the applicable Cursor account and privacy settings."* **The no-training state is conditional on Cursor configuration** — it is never asserted flatly for Grok Bot. The anchor reports a first-run screen stating data is not used for training with an optional opt-in to store conversations, and declines it; that is consistent with the stack but **drops the qualifier that makes the sentence true or false.**

## ⚠️ What is claimed but not confirmable

A large share of this topic rests on **one person's screen**. These are single-source with nothing independent behind them:

- The sign-in screen offering **exactly two** providers.
- A **free tier** in the plan chooser, and a trial meter at **35%** after two bots and one job — **no allowance size is published anywhere, so the percentage has no denominator**, and secondary coverage contradicts itself (7-day card-required trial vs *"no separate Grok Bot free tier"*). Refused rather than averaged. *The 2026-08-21 expansion did introduce "a free trial with limited usage for all other users," which supports the observation without confirming the screen.*
- The **connector picker** enumerating LinkedIn, Google Workspace, Monday, Box, Calendly, Salesforce, Databricks and **no YouTube** — docs never enumerate plugins, so not one entry is checkable, **including the YouTube absence his whole workflow turns on.** This is exactly the invented-enumeration shape this project has a logged history of; it is recorded as his observation, not as fact.
- Onboarding **department templates** (Engineering, Design, Marketing, Customer Support, Product) — four map to real marketplace categories; **"Customer Support" does not exist** (nearest: Operations).

**A provenance warning that changes the count:** two sources *look* corroborated and are not. How I AI's figures are matched by her own companion page on `chatprd.ai` — **same author**, so that establishes transcription fidelity, not accuracy. HistoryAI's bot roster is likewise self-reported. **Author-to-own-writeup agreement is one source, not two** — the v283 finding, recurring.

## Key Takeaways

- **The primitive is the always-on machine, not the model.** Browser + filesystem + terminal, running when you are not.
- **One microVM per user, shared by all your bots.** Per-bot screens are not boundaries. Separate trust domains need separate Cursor users.
- **The browser-plus-take-over handoff is why it needs no code** — and it is why a missing connector does not block a workflow.
- **Cursor co-gates the product.** Access, billing and enterprise routing all run through it; treating this as a pure SpaceXAI product misreads the distribution.
- **The marketplace publishes, it does not sell** — 71 bots, 43 creators, 9 categories, "Add" buttons, no prices.
- **A lot of this topic is one person's screen.** Where that is so, it is labelled, not laundered.

## Sources

- `x.ai/news/introducing-grok-bot` · `docs.x.ai/grok-bot/{overview,faq,computer-and-apps,approvals-security-and-privacy,security-faq}` · `x.ai/bot/marketplace` · `cursor.com/pricing` — first-party
- All six transcripts in `raw/2026-09-11-grok-bot-xai-persistent-agents/`

**Related:** [[_index]] · [[one-computer-per-user-not-per-bot]] · [[pricing-is-a-timeline-not-a-number]] · [[the-vendor-renamed-itself]] · [[the-blockchain-misframing]] · [[claims-scorecard]] · [[caveats-and-corrections]]
