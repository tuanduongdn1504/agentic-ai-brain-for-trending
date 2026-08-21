# How the watermark works

> **Sources:** Squintist `[01:49]`–`[05:12]` (the clearest account in the bundle) · Code Bear `[whole]` · BetterWay `[00:59]`–`[02:21]` · Kyle Balmer `[07:03]`–`[08:25]`
> **Graded against:** [SynthID-Text, *Nature* 634:818 (Oct 2024)](https://www.nature.com/articles/s41586-024-08025-4) — figures quoted from the [open-access PMC mirror](https://pmc.ncbi.nlm.nih.gov/articles/PMC11499265/) · [arXiv:2603.03410](https://arxiv.org/abs/2603.03410) · [arXiv:2402.19361](https://arxiv.org/abs/2402.19361)

**The bundle is substantially accurate on the mechanism.** This is the rare case where four YouTube explainers
describe a published algorithm correctly. The verification lens's verdict: *"No claims are technically impossible
or confuse watermarking with statistical AI detection."*

## The one fact everything rests on

A language model does not pick the obvious next word. At each step it computes a distribution over plausible
next tokens and **samples** from it. Squintist `[02:18]`: *"Why roll the dice at all? … Because a model that always
takes the favorite writes like a broken record."* The sampling temperature is the dial.

**A watermark is a rigged dice roll.** Nothing is added to the text. The mark *is* which word came out.

## Tournament sampling

Anthropic's scheme is based on Google DeepMind's **SynthID-Text**. Squintist's account `[03:15]`, which matches the
paper:

1. At a step where several near-synonyms are plausible — *big, large, huge, vast* — the sampler runs a **knockout
   tournament** among candidates instead of a plain draw.
2. Each match is decided by a **hidden score** derived from a **secret key mixed with the last few tokens written**.
3. So at this step the key might favour *big* and *vast*; the winner is emitted.
4. **The key reshuffles every step**, because the context it is mixed with just changed. Next step, *large* and
   *huge* may be the favoured pair.

Squintist `[03:45]`, on why this is not detectable by inspection: *"No word is permanently favored. Run it for a
million steps, and big wins exactly as often as it would have with no tournament at all."* Word frequencies do not
budge. There is no stylistic tell.

Kyle Balmer `[07:30]` gives the simpler Kirchenbauer-style intuition his cited expert uses — hash the previous token,
split the vocabulary into a **green set and a red set**, boost the green set, then count green words at detection
time. Same family, cruder instrument.

## Detection is the same trick in reverse

Squintist `[04:13]`: the checker holds the key, slides along the text, and at each position recomputes what the
hidden score *would have been*, then asks whether the word actually sitting there scored high.

- In human prose, roughly **half** the words score high — coin flips.
- In keyed output, the rate runs **noticeably above half**.
- The signal exists only **in aggregate across hundreds of words**, never in any single word.
- **No database and no model are needed** — only the words plus the key. This is why Anthropic can promise detection
  from pasted text alone.

BetterWay `[02:21]` draws the right conclusion: *"Nothing is actually added to the text… That's why Anthropic can
say it costs nothing."*

## What the production numbers actually are

All three figures below are quoted from the open-access paper, not from the bundle. **Squintist reported all three
approximately correctly**; a verification lens marked them UNVERIFIED after hitting the paywall and not trying the
mirror.

| Measure | Paper's words | Squintist's version |
|---|---|---|
| Scale of the live Gemini experiment | *"We analysed approximately 20 million watermarked and unwatermarked responses"* | "about 20 million responses" ✅ |
| User satisfaction | *"the thumbs-up rate for the two models differed by 0.01% (with the watermarked model being higher); and the thumbs-down rate differed by 0.02%"* | "differed by 1/100 of a percent, which is statistically nothing" ✅ |
| Latency | *"15.527 ms per token; this increases to 15.615 ms per token with 30-layer Tournament sampling, a latency increase of only 0.57%"* | "about half a percent" ✅ |

Note the direction on satisfaction: the **watermarked** model scored *higher*. Within noise, but it is not a
quality penalty in the aggregate.

## Where the watermark cannot go: entropy

This is the most useful practical fact in the topic, and Squintist states it best `[05:40]`:
*"The tournament needs contestants."*

- Ask for the capital of France and only *Paris* is acceptable. A tournament with one contestant carries no signal.
- **Code has the same property.** Syntactically constrained positions have one right token; the wrong synonym breaks
  the build.
- **Short passages** never accumulate enough positions.

Squintist's summary `[06:07]`: *"The watermark lives in linguistic freedom… You can hide a pattern in brushstrokes.
You can't hide one in a barcode."* Confirmed against the literature.

**Corollary that matters to anyone using Claude Code:** the more constrained the output, the weaker the mark. The
inverse is Kyle Balmer's warning `[08:25]` — his cited expert says rigging the sampler *does* cost quality, tolerable
in an email and *"a massive problem"* in code. That is a genuine tension the bundle does not resolve, and
**Anthropic's flat claim that marking "doesn't change the meaning, quality, or readability"** is where it bites.
See [[caveats-and-corrections]].

## The consequence nobody in the bundle drew

If the mark needs entropy, then **the strength of the mark on a given output is a function of how much freedom the
model had** — which means a proofread of a human's text can be *more* strongly marked than a factual answer, because
rephrasing is high-entropy work. Squintist gets closest `[07:32]`: *"The more the model rephrases, the stronger the
mark can be, and a real copy edit involves a lot of rephrasing."* The person who wrote every word themselves and
asked only for a polish is, mechanically, a **worse** off case than someone who asked a factual question.

## Key Takeaways

- **The mark is the word choice. Nothing is inserted**, so there is nothing to find and delete — and it survives
  copy-paste for the same reason.
- **A secret key mixed with recent context re-randomizes every step**, which is why frequencies look normal and no
  reader can tell.
- **Detection needs the key and hundreds of words**, never a single word, and needs no model at inference time.
- **Verified production cost is real but tiny**: +0.57% latency, satisfaction difference 0.01% in the watermarked
  model's favour, across ~20M responses.
- **Entropy is the binding constraint.** Code, one-answer facts, and short text are structurally hard to mark — and
  the same knob means high-rephrasing tasks like copy-editing are marked *most* strongly.
- The quality claim is contested: Anthropic says no impact; a cited practitioner says a measurable impact that
  matters specifically in code. Unresolved — see [[caveats-and-corrections]].
