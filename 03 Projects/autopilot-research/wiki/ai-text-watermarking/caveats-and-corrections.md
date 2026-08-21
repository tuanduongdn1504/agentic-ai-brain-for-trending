# Caveats and corrections

> Everything this topic could not settle, plus everything the **verification process itself** got wrong. Recorded loudly, per `CLAUDE.md` Rule 12 (fail loud) and the vault prime directive — don't repeat the same mistake twice, **in either direction**.

## 1. Unresolved — do not cite these as settled

1. **Is Anthropic's scheme SynthID-Text, or a variant?** Anthropic says "based on". Code Bear's video assumes
   identity. **Every attack number in [[attacks-and-robustness]] is measured on SynthID-Text or the general family,
   never on Anthropic's shipped scheme.** Treat them as the right order of magnitude, not as Claude's.
2. **Does the mark degrade output quality?** A09 vs C16 is a direct contradiction. Anthropic says no impact; the
   practitioner Kyle Balmer cites says yes, imperceptible in prose and *"a massive problem"* in code. The *Nature*
   satisfaction data (0.01% thumbs-up difference, in the watermarked model's favour) supports Anthropic **for
   Gemini prose**, and says nothing about code. **Unresolved, and the most consequential open question for anyone
   using Claude Code.**
3. **Is there any opt-out, in any tier?** Anthropic's page is silent — consumer, API, Code, Cowork, enterprise. The
   anchor asserts there is none. **Silence is not confirmation.** Marked UNVERIFIED.
4. **False-positive and false-negative rates for Claude's detector.** Do not exist publicly. The detector does not
   exist publicly. This blocks the ADR's eval-gating clause — see [[consequences-for-this-vault]].
5. **Non-English performance.** Marking is worldwide. Nothing states that detection performs equally in Vietnamese,
   Chinese, Japanese or Arabic. Every robustness number in this topic is English. **Given the anchor is Vietnamese
   and [[detectors-are-not-watermarks]] shows detectors fail hardest on non-native English, this is the largest
   substantive gap in the topic.**
6. **Does marking cover Claude Tag, and per-skill invocations?** Marking applies "wherever Claude is offered", but
   nothing addresses whether every skill invocation or every turn of a multi-turn Claude Code session is marked
   independently.
7. **Whether the Melbourne gym victim was notified, compensated, or had the booking restored.** Not reported by any
   outlet. The agent said it could not undo it.
8. **The 50%-word-drift figure (E10).** The direction is well documented; the specific number is not traced to a
   primary study.
9. **Twelve of the anchor's fourteen news items** are UNVERIFIED — deliberately. They are outside this topic's scope
   and are listed in [[the-anchor-audit]] so a later ingest can pick them up rather than re-derive them.

## 2. ⚠️ Verification-process failures in this very ingest

The workflow ran 11 agents, 0 errors, 749,523 tokens. **"0 errors" means no agent crashed. It does not mean the
verdicts were right.** Six failures, all caught by main-loop primary fetches:

1. **Two lenses confirmed a false claim.** `A01` — the anchor's "all their models" — was returned **CONFIRMED** by the
   EU-AI-Act lens and by the adversarial lens, and CONFIRMED-BUT-INCOMPLETE by the Anthropic-primary lens. All three
   are wrong. **One fetch of `support.claude.com` settled it.** The adversarial lens, whose entire brief was to refute,
   confirmed the single most important error in the bundle.
2. **The completeness critic asserted there were no disagreements.** Verbatim: *"No head-on verdict disagreements
   detected where Lens A marks CONFIRMED and Lens B marks FALSE/CONTRADICTED on identical claim ID."* There were three
   (A01, A14, and the four empirical claims in #4 below). **A critic that reports the absence of a thing it did not
   look for is worse than no critic**, because the report reads as a clean bill.
3. **Anachronistic grading.** `A14` — Squintist saying Anthropic had not published the mechanism — was graded
   CONTRADICTED-IN-BUNDLE by one lens and MISLEADING by another, both using information published **the day after**
   his video. **A dated source must be graded against what was knowable on its date.** Correct verdict: TIME-BOUND.
4. **Single-repository search reported as absence of evidence.** The mechanism lens searched only `arxiv.org` and
   returned **UNVERIFIED** for four facts that are not on arXiv: OpenAI's 2023 detector, the Stanford/TOEFL study,
   ICML 2026, and the *Nature* deployment figures. The adversarial lens confirmed all four from Gizmodo, The Markup,
   AI Weekly and Nature. **"I searched one place and found nothing" is not a finding.**
5. **A fetch failure generalized into a property of the world.** The Anthropic-primary lens reported a *"MAJOR
   ACCESSIBILITY LIMITATION: anthropic.com uses React-rendered dynamic content"* and fell back to TechCrunch — while
   **two sibling agents in the same run fetched `anthropic.com/news/claude-text-watermark` successfully.** It then
   graded Anthropic's own policy from secondary coverage.
6. **A paywall treated as the end of the road.** The same lens marked the *Nature* figures UNVERIFIED after
   `nature.com` gated it. The paper has an **open-access PMC mirror** (`PMC11499265`) that yields all three numbers
   verbatim. Per the project's own block-handling discipline: **a block means change technique, not give up** —
   and here the technique was one search away.

**The pattern across all six: the agents were reliable at reading the transcripts and unreliable at deciding when
they had finished verifying.** The digests (phase 1) produced accurate, well-quoted claim sets. The failures are all
in phase 2, and all are failures of *sufficiency judgement*, not of comprehension.

**Rule for the next ingest:** when a claim is about the subject's own published policy, **the main loop fetches the
primary source itself** and does not delegate it. It cost one call here and overturned four verdicts.

## 3. Corrections to figures as stated in the bundle

| Source claim | Correct | Where |
|---|---|---|
| "all their models" (anchor) | models launched **on or after 2026-08-02**; earlier ones by 2026-12-02 | A01 |
| "whether Claude is the author" (anchor) | *"may have been **processed** by Claude"* | B01 |
| Manus backup "before the end of this month" (anchor) | **07:59 SGT, 2026-08-23** | G11 |
| watermark scrubbing "above 90%" (BetterWay) | *"over 80%"* per arXiv:2402.19361 | D09 |
| "the mark survives editing" (Ulku, `[00:28]`) | heavy rewriting kills it — contradicted by the same video at `[01:52]` | G07 |
| Gemini 3.7 Flash "a slight improvement" (anchor) | FrontierCode 43.6% vs 34.4%; intro price half of 3.6 | G09 |

## 4. Reading caveats about this topic's own construction

- **Anthropic's support-page quotes reached this wiki through `WebFetch`**, which converts a page and summarizes with
  a small model. The quotes are consistent with independent reporting and with two agents' own fetches of
  `anthropic.com/news/claude-text-watermark`, but they are **one layer removed from reading the HTML directly.**
  A future pass should re-read the page verbatim.
- **The bundle is 6 videos, 5 of them published within 5 days of each other**, all reacting to the same announcement.
  Convergence between them is weak evidence — they may share sources. The independent grounding is the primary
  documents, not the agreement.
- **The source bundle is not reproducible.** See [[source-provenance]].
- **This file is itself Claude output, written after 2026-08-02.** By the mechanism in [[how-the-watermark-works]] it
  is watermarked. So is every other file in this topic.

## Key Takeaways

- **Zero fabricated claims, but six verification-process failures** — and the failures were in the *verifier*, not the
  sources.
- **"0 agent errors" is not "0 wrong verdicts."** An adversarial lens confirmed the bundle's biggest error.
- **Grade a dated source against its own date.**
- **A single-repository search that finds nothing is not evidence of absence**; a paywall is not a dead end; a fetch
  failure is not a property of the internet.
- **Fetch the subject's own primary source in the main loop.** One call overturned four verdicts here.
- **The largest real gap is non-English performance**, on a topic reached through a Vietnamese source, in a corpus
  whose operator screens non-native-English candidates.
