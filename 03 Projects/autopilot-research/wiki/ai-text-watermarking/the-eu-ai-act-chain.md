# The EU AI Act chain

> **Sources:** Kyle Balmer `[02:23]`–`[04:43]`, `[09:20]`–`[10:17]` (the only source in the bundle that reads Article 50 on screen and names the provider/deployer split) · Squintist `[07:32]`–`[08:56]` · BetterWay `[02:21]`–`[02:49]`
> **Graded against:** [artificialintelligenceact.eu Article 50](https://artificialintelligenceact.eu/article/50/) · [EC digital-strategy: transparency guidelines](https://digital-strategy.ec.europa.eu/en/policies/guidelines-transparency-ai-generated-content) · [EC: how to sign the Code of Practice](https://digital-strategy.ec.europa.eu/en/library/how-sign-code-practice-transparency-ai-generated-content) · [Tech Policy Press explainer](https://www.techpolicy.press/the-eus-ai-transparency-code-of-practice-explained/)

**The anchor never mentions any of this.** It presents the watermark as *"giám sát ngầm"* — covert surveillance. The
verified chain is a published law with a named article, a signed voluntary code, a signatory list, two hard dates and
a penalty ceiling. That is the largest single gap between the anchor and reality; see [[the-anchor-audit]].

## The chain, verified end to end

**Article 50(2) → Code of Practice (2026) → ~190 signatories (July 2026) → obligations bite 2026-08-02 → Anthropic ships the mark.**

Article 50(2), quoted verbatim:

> *"Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated."*

Signing the Code gives a **presumption of compliance** with Article 50. It is voluntary; the law behind it is not.
Squintist `[08:29]` puts it best: *"The code is voluntary, but the law behind it isn't."*

## Provider vs deployer — the distinction that decides who owes what

Kyle Balmer `[02:23]` calls this *"the root cause of most of the misunderstanding that I have seen"*, and he is right.
He is also the **only** source in the six that names it.

| | Who | Obligation |
|---|---|---|
| **Article 50(2)** | **Providers** — Anthropic, OpenAI, Google | Mark synthetic output in a machine-readable, detectable format |
| **Article 50(4)** | **Deployers** — anyone building on those models | Disclose AI-generated text published to inform the public on matters of public interest; disclose deepfakes |

**This is the load-bearing fact for anyone shipping a product on Claude.** The marking duty is Anthropic's. The
*disclosure* duty is the builder's, and it is a separate obligation with a separate trigger. See
[[consequences-for-this-vault]].

## The dates

| Date | What happens | In the bundle? |
|---|---|---|
| **2026-08-02** | Article 50 transparency obligations take effect. Claude models launched on/after this date mark at launch | all six sources ✅ |
| **2026-12-02** | Generative systems **already on the market** before 2026-08-02 must meet the machine-readable marking requirement (AI Omnibus provisional agreement, May 2026) | **BetterWay only** — *"models already released have until December"* ✅ |
| **2027-02-02** | Code of Practice **interoperability** deadline — detection tooling must be publicly accessible and interoperable | **no source** ⚠️ |

The February 2027 date is absent from the entire bundle and is the one a builder would actually plan against.

## What the Code of Practice adds beyond the law

Performance requirements, not prescribed technology — the Code names **effectiveness, reliability, robustness and
interoperability**, and leaves the construction open. Two provisions the bundle almost entirely misses:

- **At least two independent layers of machine-readable marking.** This explains Anthropic's architecture: the text
  watermark *and* C2PA file metadata are not belt-and-braces marketing, they are the two layers.
- **Free access to a checker** — but Squintist `[08:29]` reports a carve-out that matters enormously: *"for plain
  text, the code lets labs restrict that checker to verified experts at first, because text marks are the least
  reliable kind."* The regulator's own instrument concedes that **text marking is the weakest modality.**

Squintist also catches the sharpest irony in the topic `[08:00]`: the law **exempts standard editing** — *"Spelling,
grammar, and translation need no mark"* — and **Anthropic watermarks it anyway.** The complaint that dominates the
backlash is about behaviour the regulation did not require. Confirmed: the Article 50 guidelines exempt *"assistive
editing functions"* and systems *"not substantially altering input data or semantics"*.

## Penalty and reach

- **Up to €15,000,000 or 3% of global annual turnover.** Stated by BetterWay `[02:21]`, confirmed.
- **The Act reaches outside the EU when output is used inside it.** Kyle Balmer `[09:48]`: Anthropic can *"stop
  providing their models to the EU and lose quite a lot of money… or play by the rules."*
- **Worldwide application is Anthropic's own choice, not a legal requirement.** BetterWay `[02:21]`: Anthropic
  applies it globally because it *"doesn't yet have a durable way to limit it to one region."* Anyone outside the EU
  is being marked by an operational decision, not by Brussels.

## Who signed — and who did not

Confirmed by the European Commission's own signatory material: **Aleph Alpha, Anthropic, Black Forest Labs, Cohere,
Google, Meta, Microsoft, Mistral, OpenAI, Synthesia**, among ~190 organizations.

**xAI refused.** Kyle Balmer `[18:33]` calls it *"the big holdout… I don't think is getting enough credit for this"*
and declines to editorialize further. Note the anchor's own inconsistency: it worries that marking *"could push users
to other models not subject to this rule"* `[11:35]` — while spending four minutes earlier in the same video
promoting Grok, the product of the one lab that refused to sign. It never connects the two.

Coverage differs by vendor: Anthropic ships a documented text watermark plus C2PA for files. OpenAI documents C2PA
and SynthID on images and audio and has committed to extending provenance to text — Kyle Balmer `[03:46]` quotes its
support page. **Google has marked text with SynthID since 2024** and has open-sourced SynthID-Text.

## Key Takeaways

- **The regulatory chain is real, verifiable and named.** Article 50(2), a signed Code of Practice, ~190 signatories,
  and two hard dates. The anchor's surveillance framing is editorial, not factual.
- **Article 50(2) binds providers; Article 50(4) binds deployers.** Different duties, different triggers. If you ship
  on Claude, the marking is not your obligation but the **disclosure may be**.
- **2026-12-02** for pre-existing models; **2027-02-02** for interoperable public detection tooling — the second is
  missing from every source in the bundle.
- **The Code requires at least two marking layers**, which is why Claude does text watermarking *and* C2PA.
- **The law exempts spelling, grammar and translation. Anthropic marks them anyway** — the single most-resented
  behaviour was not compelled.
- **The regulator itself treats text marks as the least reliable modality**, to the point of allowing the free public
  checker to be restricted to verified experts at first.
- **xAI is the sole major holdout**, which is the unexamined tension in a roundup that promotes Grok and frets about
  users fleeing to unmarked models.
