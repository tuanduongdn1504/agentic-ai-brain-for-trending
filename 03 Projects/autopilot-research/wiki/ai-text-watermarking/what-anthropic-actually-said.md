# What Anthropic actually said

> **Source:** primary — [`support.claude.com` "How Claude marks AI-generated content"](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content), fetched 2026-08-21. Corroborated by [`anthropic.com/news/claude-text-watermark`](https://www.anthropic.com/news/claude-text-watermark) (fetched by two verification agents) and [TechCrunch 2026-08-15](https://techcrunch.com/2026/08/15/anthropic-shares-more-details-about-how-claudes-new-watermarks-will-work/).
> **Bundle source:** all six videos in [[source-provenance]]; the closest reading is Kyle Balmer's *"let's go straight to the horse's mouth."*

**Read this article before any other in this topic.** Five of the six sources in the bundle get something wrong
about scope, dates or what a mark proves, and every one of those errors is settled by one page.

## The six sentences that matter

Quoted from Anthropic's support page:

1. **Scope and date** — *"Claude models launched on or after August 2, 2026 will support machine-readable marking at launch."*
2. **Older models** — *"The law includes a transition period for Anthropic models launched before August 2, 2026, and we're working to add marking support for those models as well."*
3. **Coverage of text** — *"Embedded watermarks will apply to all generated text."*
4. **Files** — *"When Claude generates a supported file type, such as a .svg, .png, or .jpg, it will attach signed provenance metadata."*
5. **What a hit means** — *"Detecting a Claude mark tells you that the content may have been processed by Claude."* And: *"It does not, on its own, confirm the full provenance of the content… Claude may not be the original author. People often use Claude to proofread, translate, summarize, or convert files."*
6. **Geography** — *"Marking will apply to output from supported models wherever Claude is offered, worldwide."*

Two more, on what defeats it: detection may fail where *"the text has been heavily edited, paraphrased, translated,
or mixed into other writing"*, or where *"the passage is very short, leaving too little text for a reliable signal."*

On the detector: *"We'll share details on detection mechanisms in forthcoming technical documentation."*

## The distinction the whole topic turns on

**"All generated text" is true. "All models" is not.** Sentence 3 and sentence 1 are doing different jobs:
*within a supported model*, every piece of generated text is marked; but *which models* are supported is bounded by
a launch date. The anchor in this bundle collapses the two and says **all their models**. See
[[the-anchor-audit]] and [[claims-scorecard]].

The EU's own timetable is the other half: models already on the market before 2026-08-02 have until
**2026-12-02** to comply. BetterWay is the only source in the bundle that mentions the December date, and it is
right. See [[the-eu-ai-act-chain]].

## The two mechanisms, which are not the same thing

| | Embedded text watermark | Signed provenance metadata |
|---|---|---|
| Lives in | the word choices themselves | the file container |
| Applies to | all generated text | `.svg`, `.png`, `.jpg` and other supported types |
| Standard | Anthropic's own, based on SynthID-Text | **C2PA** |
| Survives copy-paste? | yes — the words *are* the mark | no — copying content out drops the metadata |
| Stripped by | heavy edit, paraphrase, translation, mixing | any metadata strip; trivial |

Kyle Balmer chose to cover only the text watermark, on the explicit and correct ground that *"metadata can be
stripped easily."* That is the right editorial call and the reason this topic is about text.

## What Anthropic did **not** say

Recorded as gaps, not as denials — the page is silent, which is different from the anchor's claim that opt-out is
impossible:

- **No opt-out statement either way.** Nothing about disabling marking, and nothing about differences between the
  consumer app, the API, Claude Code, Cowork or enterprise agreements. The anchor's *"users cannot opt out"* is
  **UNVERIFIED**, not confirmed.
- **No false-positive or false-negative rate.** None. For anyone who has to make a decision about a person on the
  strength of a detection, this is the missing number. See [[what-it-does-not-prove]].
- **No detector release date, and no access tier.** Anthropic has said a detection API is coming. As of the last
  source in this bundle (2026-08-17) it did not exist.
- **No mechanism specification.** Anthropic points at SynthID-Text and Scott Aaronson's 2022 proposal rather than
  publishing its own construction. Whether Anthropic's scheme is SynthID-Text unmodified is **unresolved** —
  Code Bear's video assumes it is; Anthropic's wording is "based on".
- **Nothing about non-English text.** Marking is worldwide; there is no statement that detection performs equally
  in Vietnamese, or in any language other than English. For a vault whose anchor is Vietnamese, that is a live gap.

## Key Takeaways

- **The primary source is one page long and settles most of the bundle's disputes.** Reading it cost one fetch and
  overturned four verification-agent verdicts — see [[caveats-and-corrections]].
- **"Processed by Claude", not "written by Claude".** This is Anthropic's own framing, in its own words, and it is
  the single most-misreported fact in the coverage.
- **New models from 2026-08-02; older models by 2026-12-02.** Not "all models, now".
- **Text watermark and C2PA file metadata are separate mechanisms with opposite failure modes.** The one that
  survives copying is the one you cannot remove by accident.
- **Absence of a published false-positive rate is the operative problem**, not the watermark itself. Every
  downstream harm in [[what-it-does-not-prove]] flows from acting on a detection whose error rate nobody has stated.
