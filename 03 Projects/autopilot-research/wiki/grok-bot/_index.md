# grok-bot

> **Topic index.** Six sources on **Grok Bot** — SpaceXAI's persistent-agent platform — compiled from an operator anchor submitted **the day it was published**, with 0 views.
> **Compiled:** 2026-09-11 · path 1 anchored bundle (operator anchor + yt-search ×5). All transcripts read in full; **no NotebookLM**.
> **Anchor:** [`CqhE6qPoEAs`](https://www.youtube.com/watch?v=CqhE6qPoEAs) — Quân IT, *"Grokbot | Elon knows how to build product"* (VN, 57:04, **237 views**, 2026-09-11). Anchor validation **PASS 1/1, overlap 100%**. Fetch guard **PASS 6/6**.
> **Raw:** [`raw/2026-09-11-grok-bot-xai-persistent-agents/`](../../raw/2026-09-11-grok-bot-xai-persistent-agents/_sources.md) — 24,506 words / 6 transcripts
> **Scorecard:** **160 claims — 0 FABRICATED.** Anchor: 7 CONFIRMED · 8 CBI · 3 CORRECTED · 1 MISLEADING · 16 UNVERIFIED · 1 UNFALSIFIABLE. See [[claims-scorecard]].
> **Verified by** workflow `wf_c3cb4b9e-bbe` — 14 Opus agents, **0 errors / 0 empty / 14 of 14**, 1.35M tokens.

## Why this topic exists

The operator submitted one Vietnamese video and asked whether anything in the queue blocked building knowledge from it. Nothing did — **the queue was empty**, and checking that turned up [a silent-skip bug in the drain's queue parser](../../bin/autopilot-drain.py) which was fixed in the same session.

The anchor had **0 views** when submitted and 237 by drain time, against `MIN_VIEWS = 1000` — so the rubric **structurally cannot select it**. It enters only as an anchor. That is the third time this wall has been hit, and the clearest: **a 0-view video is not a low-quality video, it is a new one.**

## The four findings

> **1. 🔴 One computer per USER, not per bot — and the bundle got it backwards 4-to-2.** The launch page says *"Bots have their own computer."* The FAQ says *"Every Bot on your account uses one persistent cloud computer… assigned per user, not per Bot. **Do not use separate Bots as a security boundary.**"* The four wrong sources are not four errors — they all recite the same headline. **One vendor simplification, propagated four times**, which is why a 4-to-2 majority loses to verbatim first-party text. The two that got it right: a $200-skeptic and a crypto-promo channel. The two that got it wrong include the paid sponsored walkthrough and the 312K-view flagship. **Neither reach, sponsorship nor independence predicted accuracy on the one fact where being wrong is expensive.** → [[one-computer-per-user-not-per-bot]]

> **2. The vendor renamed itself and all six sources missed it.** SpaceX acquired xAI **2026-02-02**; the entity is **SpaceXAI LLC** — x.ai's own copyright line says so — rebranded July 2026, two months *before* Grok Bot shipped. All six sources say "xAI." So did this ingest's first three messages, and so did a pre-flight lens scoped specifically to first-party surfaces: it fetched the right page and read past the copyright notice, because it was checking *whether* the product was official, not *who owns it.* **Garble is noisy and self-corrects across sources; a stale-but-live brand name fails all six together.** → [[the-vendor-renamed-itself]]

> **3. The pricing "contradiction" was a timeline.** The pre-flight critic recommended **do-not-ship** over *"three unresolved, conflicting price points."* There is **no Grok Bot price at all** — no SKU. The entry floor fell **$200 → $60 → $20** between Aug 11 and Aug 26 by *expanding eligibility*, not discounting. Nate B Jones's *"Is It Worth $200?"* was correct when asked and expired twelve days later. Averaging $200 and $20 gives $110, true on no day. Underneath: unpublished weekly quota, uncapped token overage in arrears — **the headline is a floor, not a cost.** → [[pricing-is-a-timeline-not-a-number]]

> **4. The anchor's "blockchain product" error has a documented internal origin, stated on camera.** He tried to build a **DePIN-style idle-compute marketplace** himself — *"a distributed system so AI agents could access idle VMs"* — a category that genuinely is blockchain-settled (Akash, io.net, Render) and whose own 2026 marketing pitch is verbatim *"always-on AI agents."* So a product whose headline primitive is "every bot has its own cloud computer" landed on his prior. **Not a scam-token confusion — a category label inherited from his own abandoned project, and he explains the difference himself.** → [[the-blockchain-misframing]]

## ⭐⭐⭐ The methodological finding

**This corpus's own scorecard rewards reciting and punishes doing.** The best mechanical score (5.9% error, 64.7% CONFIRMED) belongs to a **paid sponsored** walkthrough that records **zero security reservations in 3,148 words**. The worst CONFIRMED share (19.4%) and highest UNVERIFIED share (44.4%) belong to the **only source that installed the product from zero** — because first-run observation inside a private account is unauditable **by construction**. A source with no evidence of installing it at all posts the second-highest CONFIRMED rate *and* the highest hard-error rate.

**Verifiability tracks proximity to fetchable text and is nearly orthogonal to how much a source actually learned.** Report the **error signature**, not the rate. → [[the-anchor-audit]]

Related: the prior ship's *"operator's anchor was the most accurate source"* **does not replicate** — the anchor hit ~11% hard error **again** (11% then, 11.1% now), but ranks 3rd of 6, because **rank is a property of the companion set.** And *"reach ≠ reliability"* **inverts** here at the extremes.

## Articles

| Article | What it covers |
|---|---|
| [[what-grok-bot-is]] | Architecture, access, marketplace, privacy posture, and what is claimed but unconfirmable |
| [[one-computer-per-user-not-per-bot]] | 🔴 The load-bearing security fact and the 4-to-2 split |
| [[pricing-is-a-timeline-not-a-number]] | No SKU; the eligibility timeline; why four figures aren't a conflict |
| [[the-vendor-renamed-itself]] | SpaceXAI; correlated upstream error that source diversity cannot fix |
| [[the-blockchain-misframing]] | The anchor's opening error and its documented origin |
| [[the-anchor-audit]] | Anchor vs 5 companions; why the scorecard metric misreads hands-on sources |
| [[claims-scorecard]] | 160 claims, both decided contradictions, 3 logged main-loop overrides |
| [[caveats-and-corrections]] | ⚠️ This ingest's 8 own errors, tooling defects, open questions, deepen candidates |

## 🔴 For `hireui`

**Do not pilot this against candidate data.** Shared browser sessions + shared filesystem + agent autonomy + *"training opt-out follows your Cursor settings"* is the wrong combination for candidate PII. The exposure class is the same **BOLA**-shaped risk [[../api-security-7-techniques/_index]] names as this operator's **#1 unmitigated risk**, and the same shape as the real-world incident in [[../ai-text-watermarking/_index]]. If it is ever piloted, **one Cursor user per trust domain** is the only boundary the vendor will stand behind — it says so in writing.

**Cross-links:** [[../hermes-agent/_index]] (vendor-seeded false claims; *fidelity is not accuracy*) · [[../homebrew-macos-package-manager/_index]] (docs outperformed every video; the Rosetta finding that explains this project's python shim) · [[../local-llm-coding-hardware-ladder/_index]] + [[../quanit-becoming-ai-engineer-2026/_index]] (**same creator** — this is the 3rd Quân IT topic) · [[../api-security-7-techniques/_index]] · [[../ai-text-watermarking/_index]]
