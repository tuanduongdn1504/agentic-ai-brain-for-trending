# Detectors are not watermarks

> **Sources:** Squintist `[08:56]`–`[12:39]` — the only source in the bundle that covers this at all, and the reason it is the strongest source
> **Graded against:** [The Markup on the Stanford/TOEFL study](https://themarkup.org/machine-learning/2023/08/14/ai-detection-tools-falsely-accuse-international-students-of-cheating) · [NeurIPS 2026 blog](https://blog.neurips.cc/2026/06/02/ai-generated-papers-in-the-neurips-2026-position-paper-track/) · [AI Weekly on the NeurIPS rejections](https://aiweekly.co/alerts/neurips-rejects-184-of-position-papers-via-pangram-ai-tool) · [AI Weekly on ICML](https://aiweekly.co/alerts/icml-desk-rejects-497-papers-over-llm-review-violations) · Gizmodo on OpenAI's classifier

**This is the most important distinction in the topic and five of six sources skip it.** The tool that will actually
be pointed at a person is almost never a watermark detector. It is a **style detector** — and style detectors have a
documented record of being wrong about specific, identifiable people.

## Two different instruments

| | Watermark detector | Style detector (GPTZero, Pangram, Turnitin) |
|---|---|---|
| Needs | the provider's **secret key** | nothing |
| Reads | whether word choices match a keyed pattern | whether the prose *looks* machine-made |
| Answers | "did this come through **this** model" | "does this resemble AI writing in general" |
| Error mode | false negative (mark washed off) | **false positive on unusual human writing** |
| Available today | no — Anthropic's is unreleased | yes, sold commercially, in use now |

Squintist's image `[09:24]`: *"If a watermark is a serial number stamped at the factory, these are handwriting
experts."*

## The record of the handwriting experts

**OpenAI's own classifier (2023).** Caught roughly a quarter of AI text, **falsely flagged ~9% of human writing**,
shut down within months. The vendor best placed to build one gave up.

**Stanford, 2023 — the finding that should govern policy.** 91 TOEFL essays by non-native English speakers, run
through seven leading detectors: **61% were flagged as AI-generated** despite being entirely human-written, and
roughly **19.8% were flagged unanimously by all seven.** Squintist `[09:52]` names the mechanism: *"Careful, formal
second language English is exactly what these systems are worst at judging."*

**This vault's anchor is a Vietnamese channel.** The population these tools fail hardest on is the population the
operator's own source belongs to. Pangram now reports zero flags on that specific dataset — improvement on a
benchmark, not a fix for the failure mode.

**The individual cases.** A writing professor of 25 years spent six months polishing a comedy short story; Pangram
returned **100% AI**, and he said he was thinking of giving up. Squintist `[10:19]` finds the reason and it is the
best line in the bundle: *comedy runs on the rule of three, a classical human rhetorical device* — and the rule of
three is now read as a machine tell. **Human craft mistaken for a machine.**

## Then it reached academia

### NeurIPS 2026 position-paper track — detection as the gate

Squintist `[10:49]` reports 969 submissions scanned with Pangram and **178 rejected before peer review, 18% of the
track, no appeal.** Verified, and the primary record is worse than his summary:

- ~**969–971** submissions, all scanned with **Pangram v3.3.2**
- **178 desk-rejected outright (18.4%)** — no appeal
- a further **123 (12.7%)** required to show evidence of substantial human engagement or face rejection
- **273 (28.2%)** initially scored at **100% AI probability**; the final count settled at 178 after narrower windows
  and internal review
- **outcomes were highly sensitive to the detection-window choice, which authors could not see**

And the calibration check that indicts the instrument: applied to papers **already accepted at ICLR 2026**, the same
tool flagged **1%** — against **28%** at NeurIPS.

Squintist `[11:16]` adds the detail that lands hardest: a rejected author ran the **track chairs' own published
papers** through the same detector and got **24% to 69%** (individually 69, 45, 36, 24). Below their thresholds — but
not zero.

### ICML July 2026 — the same year, the opposite result

BetterWay `[06:34]`: ICML inserted **watermarked** prompts into submission PDFs, so a reviewer feeding a paper to an
LLM would produce a telltale signal. **506 unique reviewers** who had declared no-LLM use were caught, **795 reviews**
flagged, **497 papers** desk-rejected.

**Put the two side by side and the lesson is not "detection works" or "detection fails".**

- ICML used a **watermark** — a keyed signal it planted itself, testing a specific behaviour it had defined. It caught
  real violations.
- NeurIPS used a **style detector** — a commercial classifier with unpublished calibration — as an unappealable gate,
  and flagged its own chairs' work at up to 69%.

**Plant your own signal and you can prove something. Buy a classifier and point it at people and you cannot.**

## Why style detection is a dissolving premise

Squintist `[12:11]`: the detector vendors retrain against the "humanizer" tools (undetectable.ai, QuillBot,
StealthGPT), the humanizers retool against the detectors, *"and both markets grow on each other."*

But the deeper problem is the premise `[12:39]`: a style detector only works while AI writing looks different from
human writing, **and that gap is closing from both ends.** Models are trained to sound human — that is the training
objective. And humans are absorbing model style: after ChatGPT, researchers found its favourite words — *delve,
meticulous, realm* — appearing **up to 50% more often in human talks**, with speakers unaware it was happening.

*"A style detector is a snapshot of a difference, and the difference is dissolving."*

## The disclosure that makes the source credible

Squintist `[13:36]` ends by turning the instrument on himself: *"Almost every word in this script came from one AI
model or another. The voice, yes, this voice was generated, too."* He predicts his own transcript would come back
mostly AI, and says it *"wouldn't exactly be wrong."*

**A source that discloses its own construction and predicts its own detection result is a more reliable narrator than
one that does not** — which is worth noting given the operator's anchor is also a synthetic-voice channel that
discloses it (*"tôi là Avatar kỹ thuật số của Victor"*) and the bundle's other four do not raise the question.

## Key Takeaways

- **A watermark detector and a style detector answer different questions.** Only the first needs a key; only the second
  exists today; only the second will be pointed at people this year.
- **Style detectors have a documented false-positive problem concentrated on non-native English writers** — 61% of
  human TOEFL essays flagged across seven tools, ~19.8% unanimously.
- **NeurIPS 2026 desk-rejected 178 of ~969 position papers (18.4%) with no appeal** on a commercial detector that
  flagged the track chairs' own papers at 24–69% and accepted ICLR papers at 1% versus 28%.
- **ICML's planted watermark caught 506 reviewers.** Same year, opposite outcome — because a signal you plant yourself
  is evidence and a bought classifier is not.
- **The premise is dissolving**: models are trained toward human style and humans are absorbing model style
  (*delve*, *meticulous*, *realm* up ~50% in human speech).
- **Never adopt a vendor watermark detector as a general AI test.** It answers "was this Claude" and returns *no* for
  every other model — see [[what-it-does-not-prove]].
