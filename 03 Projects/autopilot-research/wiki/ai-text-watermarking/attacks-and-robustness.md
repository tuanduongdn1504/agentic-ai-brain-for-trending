# Attacks and robustness

> **Sources:** BetterWay `[02:49]`–`[07:55]` — **7,689 views, the smallest channel in the bundle and by far the deepest security content** · Squintist `[06:07]`–`[06:35]`, `[11:16]` · Caleb Ulku `[07:33]`–`[09:56]`
> **Graded against:** [arXiv:2607.16010](https://arxiv.org/html/2607.16010v1) · [arXiv:2402.19361 / watermark-stealing.org (ETH Zurich)](https://arxiv.org/abs/2402.19361) · [arXiv:2402.14904 "Watermarking Makes Language Models Radioactive"](https://arxiv.org/abs/2402.14904) · [arXiv:2604.11546](https://arxiv.org/abs/2604.11546) · [arXiv:2502.18608](https://arxiv.org/abs/2502.18608)

**Every vulnerability claim in this bundle checks out against published research.** The verification lens confirmed
all of them. The uncomfortable summary: **the mark is easy to remove, possible to forge, and it leaks.**

## 1. Removal — the mark washes off

Because the mark *is* the word choices, changing the words destroys it.

| Attack | Cost | Result | Source |
|---|---|---|---|
| Meaning-preserving paraphrase with off-the-shelf tools | free | **58 of 59** detected texts lost the mark — **98.3%** | arXiv:2607.16010 |
| Round-trip translation | free | mark gone; same mechanism | Squintist `[06:07]` |
| Hand the text to a second, unmarked model and say "rewrite this" | a **9B open model on a home machine** | no provider in the loop | Squintist `[11:16]` |
| Earlier schemes (KGW, Unigram) under the same attack | free | **100%** removal | arXiv:2607.16010 |

Squintist `[06:35]` on why the number is knowable at all: **Google open-sourced SynthID-Text**, so anyone can build a
copy and attack it. He is appropriately careful — *"Their copy is a home version, not the system Google runs inside
Gemini. So, treat that number as a first result, but the attack itself clearly works."*

Squintist `[11:43]` also names the structural point that no regulation touches: *"an open model can't be forced to
mark anything because the person running it controls the dice."*

**⚠️ Cross-link with a standing vault pin.** `arXiv:2607.16010` is the **same paper** already pinned in this
operator's notes from the `watermarks-remover` pilot thread, where it supplied the finding that **detectors miss
70–83% of unattacked AI text**. The same paper now supplies the 98.3% paraphrase-removal figure. Two independent
research paths in this vault landed on one document — treat it as the anchor citation for this whole area.

## 2. Stealing the key — the sub-$50 attack

BetterWay `[03:16]`, attributed to **ETH Zurich**, confirmed against `watermark-stealing.org`:

- An attacker with **only public API access** can approximate the secret scheme's rules by querying it with a limited
  prompt set.
- Cost: **under $50.**
- The paper's abstract: *"for under $50 an attacker can both spoof and scrub state-of-the-art schemes"*, with an
  *"average success rate of over 80%"*.
- The same group finds **SynthID-Text easier to strip than several competing designs.**

**⚠️ Number correction.** BetterWay says *"scrubbing success rates above 90%"*. The cited paper says **over 80%**.
One verification lens flagged the 10-point gap; another reported "80–91%" without resolving it. Use **over 80%** and
treat >90% as unsupported. See [[caveats-and-corrections]].

## 3. Spoofing — forging Claude's signature onto text Claude never wrote

This is the consequence with the worst tail risk, and only BetterWay covers it.

**The piggyback attack** `[04:14]`, requiring almost no skill: take genuine watermarked Claude output, change a few
words to invert the argument or insert something hateful. The meaning is now different; **the mark is still there and
still reads as Claude.** The output is harmful text that any detector confirms came from Claude.

More capable versions forge from scratch: arXiv:2604.11546 demonstrates **62%** spoof success with minimal
supervision; arXiv:2502.18608 demonstrates key recovery enabling spoofing. BetterWay cites a group forging *"a
prominent scheme well enough to produce quality text falsely attributed to the model provider more than 80% of the
time."*

**The trade-off is fundamental, not an implementation defect** `[05:08]`: a mark that resists removal *clings harder
to altered text* — which is exactly what a piggyback attack needs. Strengthen robustness and you strengthen
forgeability. There is no setting that fixes both.

This inverts the usual reading of the topic. The risk is not only *"I will be falsely accused of using AI"* — it is
**"text I never wrote can be provably attributed to my Claude account's model."**

## 4. Radioactivity — the mark leaks into other companies' models

BetterWay `[05:35]`, confirmed against arXiv:2402.14904 *"Watermarking Makes Language Models Radioactive"*:

- Watermarked text is published to the open web, scraped, and used as training data.
- A model trained on it **inherits the word-choice bias** — a model that was never watermarked now carries the signal.
- Detection of this contamination is reliable at **p < 10⁻⁵** at 5% contamination; the effect still holds when only
  **6.5%** of the training set is watermarked.
- It works **even when the contaminated model is closed and the investigator has no training-data access.**

The consequence BetterWay draws is the sharpest observation in the bundle `[06:05]`: a transparency measure becomes a
**distillation detector**. *"A watermark meant for detecting machine-generated text ends up exposing whose outputs
somebody else's model was trained on."* And it notes the obvious corporate incentive — for Anthropic, which has
accused Chinese models of distilling Claude, *"this may actually be a good thing."*

Kyle Balmer `[15:19]` reaches the same place from the training-data side: labs need clean, non-synthetic data;
industry-wide marking lets them **exclude or deprioritize AI text in future training runs**, and *"they get to point
at the EU and say, they made us do it."* His read: the labs benefit and pay none of the blame.

## 5. Character-level attacks — and why they are the worst option

Caleb Ulku `[08:59]` on homoglyph swapping (replacing Latin `a` with a visually identical Cyrillic character):

- **Google resolves entities, not pixels.** Text is tokenized before anything reads it.
- A swapped character *"doesn't resolve to anything at all"* — it is not a misspelling recoverable from context. Do it
  to a business name, a service, or a city and the page stops making the connection it exists to make.
- **Mixed-script text is trivially detectable and Google has run it as a spam signal for years.**

His conclusion: *"You'd be degrading real pages to hide from a consequence that doesn't exist."* See [[the-seo-panic]].

## What is *not* known

- **No published attack results against Anthropic's actual deployed scheme.** Everything above is SynthID-Text or the
  general family. Anthropic says "based on" SynthID, not "is".
- **No false-positive or false-negative rate for Claude's detector**, which does not exist publicly yet.
- **Nothing on non-English robustness.** Every attack number above is English.

## Key Takeaways

- **Paraphrase removes the mark in 98.3% of cases** (58/59). Round-trip translation and a local 9B rewrite do the same
  for free. Removal is not the hard part.
- **Under $50 of API queries approximates the secret rules**, enabling both scrubbing and spoofing at **over 80%**
  success — not the >90% the bundle claims.
- **Spoofing is the underrated risk**: a piggyback edit inverts your meaning and keeps the mark, so harmful text can
  be provably attributed to Claude.
- **Robustness and forgeability trade off against each other by construction.** No parameter fixes both.
- **The mark is radioactive** — it survives into models trained on marked text (p < 10⁻⁵ at 5% contamination, still
  detectable at 6.5%), turning transparency into a distillation detector.
- **Do not strip watermarks with homoglyphs.** You break entity resolution and trip a long-standing spam signal to
  avoid a penalty that has never been shown to exist.
- **All of it is measured on SynthID-Text, not on Anthropic's shipped scheme.** Treat the numbers as the right order
  of magnitude, not as Claude's.
