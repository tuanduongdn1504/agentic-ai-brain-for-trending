# Caveats and corrections

> Everything this ingest got wrong, in the order it got it wrong, plus what remains open. Recorded as loudly as the findings — prime directive: don't repeat the same mistake twice, in either direction.

## 🔴 Read-before-acting caveats

**1. One microVM per user, shared by every bot.** Files, browser sessions and logins are shared. The docs say *"Do not use separate Bots as a security boundary."* A prompt-injected bot inherits **every credential on the machine**. Two of the bundle's own demos put a plaintext-credential `.env` and a card-on-file DoorDash session inside that blast radius on camera, without noticing. → [[one-computer-per-user-not-per-bot]]

**2. There is no Grok Bot price.** No SKU; bundled into eight host tiers with an **unpublished** weekly quota and **uncapped** token overage billed in arrears. Any single-source cost figure is wrong by up to 10×. → [[pricing-is-a-timeline-not-a-number]]

**3. Training opt-out is conditional.** *"Training opt-out follows the applicable Cursor account and privacy settings"* — never asserted flatly for Grok Bot. For this operator, that plus shared browser sessions is disqualifying for candidate PII until independently tested.

**4. The vendor is SpaceXAI LLC, not xAI.** All six sources are a rebrand behind. → [[the-vendor-renamed-itself]]

## ⚠️ This ingest's own errors

**A. Quoted marketing as mechanism — and passed it to 14 agents as ground truth.** The main loop fetched the launch page, quoted *"Bots have their own computer"* to the operator as verified first-party fact, and injected that sentence into the compile workflow with instructions to treat it as given. It is the simplification the FAQ contradicts. **Two graders overturned it by reading past the announcement.** The rule: *a launch announcement is marketing, not documentation* — the mechanism lives in the FAQ, security docs and changelog.

**B. Misnamed the vendor three times.** Told the operator *"Grok Bot is a genuine **xAI** product"* in three consecutive messages — having read the page whose own copyright line says **SpaceXAI LLC**. Reached the right authenticity verdict from that page and the wrong vendor name from it, because the copyright line was not what was being read for. The correction came only when two sources used the unfamiliar string "SpaceXAI" and that disagreement was chased instead of normalised. **An unexpected name for a known entity is a lead, not a typo.**

**C. Wrote a guessed explanation into two committed files.** The queue entry and `raw/.../_sources.md` both state that the crypto-trading companion is *"the best available evidence for why the operator's anchor reached for the word blockchain."* **That was a guess and it is wrong** — the real explanation is endogenous and sits twenty seconds into the anchor's own transcript, in lines the main loop had already read and printed before launching a single agent. → [[the-blockchain-misframing]]

**D. Ran a 15-agent scam investigation against the wrong hypothesis.** "Blockchain product from Elon's team" pattern-matched to impersonation-token risk, and that story was interesting enough to crowd out the cheaper check: *read the next paragraph.* The pre-flight's `amplificationRisk: high` and `do-not-ship` rested partly on it.

**E. Mis-filed the anchor's "$50" as a tier price** in the first draft of the pricing article. It is his own **user-set on-demand spend cap**. Corrected in place, noted there.

**F. Suspected a true claim was confabulated.** Flagged the agents' "bundled into **Cursor** tiers" detail as likely hallucination. It is in SpaceXAI's own announcement. Cursor is a genuine co-vendor.

**G. Built a schema that killed 3 of 4 pre-flight lenses.** `officialName` was marked required; two agents omitted it and one emitted unparseable JSON, each burning the 5-retry cap. The surviving lens's verdict was then reported as a tally (`official-xai 1/1`) and fed to three refuters as though it were consensus — so `0/3 refuted` was refuting an n=1 claim. **The crypto lens's leaked partial output disagreed** (`third-party-using-grok-name`, *"Two distinct produ…"*). Lesson: keep schemas minimal, and never present a survivor count as agreement.

**H. Ran the pre-flight fleet on Haiku.** No model was specified, so all agents inherited Haiku — the failure mode already logged in this corpus. The compile was explicitly pinned to Opus and returned **0 errors / 0 empty / 14 of 14**.

## ⚠️ Tooling defects found

**`bin/vtt-to-md.py` is killed (exit 137) on a ~1-hour auto-caption VTT.** The 240 KB anchor track could not be converted; a shell fallback (`sed` tag-strip → `grep -v` cue-drop → `awk '!seen[$0]++'`) produced all six transcripts. The converter does not scale — **deepen candidate.**

**`--dry-run` still does not emit video IDs**, so a selection cannot be replayed — the IDs for this bundle had to be re-derived by title search. This was already a logged deepen candidate from the `ai-text-watermarking` ship; it bit again here.

**Inline `python3 -c` and `python3 <script>` are killed (137) or permission-denied in this environment**; the project venv's `python` after `source bin/autopilot-env.sh` works. Consistent with the Rosetta/x86_64 prefix finding in [[../homebrew-macos-package-manager/_index]].

**An `en` caption fetch for the anchor returned HTTP 429.** Not retried, per block-handling discipline; `vi-orig` is the preferred source anyway.

## Open questions

- **The anchor's "20" on the upgrade screen** — Cursor Pro $20/mo is the near-certain reading, but the source does not disambiguate. Left **UNVERIFIED**.
- **The weekly allowance size.** The number that decides real cost, and the one SpaceXAI withholds. Launch-week reports: exhausted in one or two days of heavy use.
- **Is there a Grok Bot free tier?** The 2026-08-21 expansion introduced *"a free trial with limited usage for all other users"*; secondary coverage then contradicts itself (7-day card-required trial vs no separate free tier). **Refused rather than averaged.**
- **The connector list.** Docs never enumerate plugins, so the anchor's picker inventory — including the **YouTube absence his whole workflow turns on** — is neither confirmable nor refutable.
- **"slash"** — Slack, or slash-commands? Context does not settle it. Left open.
- **"Customer Support"** as an onboarding template — not a marketplace category (nearest: Operations). Either onboarding differs from the marketplace taxonomy, or it is a mis-read.

## Deepen candidates

- ⭐⭐⭐ **Install it and test the shared-machine boundary directly.** Every unresolved security question (credential reach across bots, what a prompt-injected bot can actually touch, whether take-over gates every login) collapses on one hands-on hour. No further video will settle any of them.
- ⭐⭐⭐ **Read `docs.x.ai/grok-bot/*` as a docs-first ingest.** The docs outperformed all six videos on every contested fact — the same result the Homebrew ship got. *On any topic with a first-party owner, read the owner's docs before compiling the commentary.*
- ⭐⭐ **Pin publication dates into the grader prompt.** A dated claim measured against a live page manufactures false errors; that happened here and was caught only by a later pass.
- ⭐⭐ **Fix `vtt-to-md.py`** for hour-long tracks, and **make `--dry-run` emit video IDs** so a bundle is replayable.
- ⭐⭐ **Report error signature, not error rate.** The scorecard structurally penalises hands-on sources and rewards doc-reciters. → [[the-anchor-audit]]
- ⭐ **Third anchor-audit datapoint.** The operator's anchors have now scored ~11% hard error twice; a third bundle makes it a trend.
- ⭐ **The Cursor relationship** — a co-vendor gating access and billing for a SpaceXAI product is odd and unexplained by any source here.

**Related:** [[_index]] · [[claims-scorecard]] · [[the-anchor-audit]] · [[one-computer-per-user-not-per-bot]] · [[pricing-is-a-timeline-not-a-number]] · [[the-vendor-renamed-itself]] · [[the-blockchain-misframing]]
