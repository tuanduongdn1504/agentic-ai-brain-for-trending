# What a detected mark does not prove

> **Sources:** Kyle Balmer `[10:17]`–`[13:32]` (the most careful treatment) · Squintist `[00:29]`, `[07:32]` · Caleb Ulku `[01:52]` · BetterWay `[00:31]` · anchor `[10:41]`
> **Primary:** [`support.claude.com`](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) — *"Detecting a Claude mark tells you that the content may have been processed by Claude."*

**All six sources in the bundle agree on this, and the coverage outside the bundle mostly does not.** It is the one
point on which the operator's anchor, the 176K-view explainer and the 7.7K-view critique are unanimous — and the point
the viral framing destroys.

## Processed, not authored

Anthropic's wording is *"may have been **processed** by Claude"*, and the page names the cases explicitly:
*"People often use Claude to proofread, translate, summarize, or convert files."*

Squintist `[00:29]` states the consequence plainly: *"You write a thousand-word report, every word of it yourself, and
ask Claude to copy-edit it… What comes back can now carry a machine-readable mark saying an AI made this."*

Kyle Balmer `[12:37]` supplies the right mental model: **treat it as a fingerprint showing contact with the tool
rather than an authorship certificate.**

He also quotes the objection that drove the backlash, from Peter Harrell `[11:12]`: if you upload your own writing and
ask for a copy-edit, *"Claude will now watermark my human-written AI copy-edited text as AI, which seems ridiculous."*

## The two errors, and they are symmetrical

### False positive: a mark is not a cheating verdict

A mark is present in all of these cases, and a naive reader cannot distinguish them:

- Claude wrote it from scratch
- Claude summarized a human's document
- Claude translated a human's document
- Claude fixed a human's grammar
- Claude converted a file format

Kyle Balmer `[12:09]`: using the mark *"as an automatic cheating verdict… is overstepping what Anthropic are
claiming."* He names the exposed parties: **employers, schools and clients.** The anchor `[11:41]` reaches the same
worry from the other direction — a student hit with a *"báo động giả"* (false alarm), a firm losing a contract because
a client thinks they were deceived.

**And there is no published false-positive rate.** Not from Anthropic, not anywhere. See
[[what-anthropic-actually-said]]. Every institution that will act on this number is going to act without it.

### False negative: no mark is not proof of a human

Kyle Balmer `[12:37]` — *"The opposite mistake is just as bad"* — and this list is his, confirmed against the primary
page:

- The text came from a Claude model released **before 2026-08-02** (marking not yet supported)
- The passage is **too short** to carry a reliable signal
- It was **heavily rewritten, paraphrased, translated, or mixed** with other writing
- File metadata was stripped somewhere in an ordinary workflow, or the export path never supported it
- **It came from a different vendor entirely.** Balmer `[13:32]`: run ChatGPT output through Anthropic's detector and
  *"it's going to flag up as no, this was not written by artificial intelligence."*

That last one is the trap for any institution that adopts one vendor's detector as a general-purpose AI test.

## What the mark genuinely answers

Squintist `[13:06]` draws the boundary precisely: **"Did these words come through this model?"** That is the whole
question a watermark answers. Not who had the idea, not how much a human contributed, not whether the claims are
true.

BetterWay `[06:34]` supplies the honest counterweight, and it is the strongest argument *for* the mechanism in the
bundle: at ICML in July 2026, watermarked papers sent for peer review caught **506 reviewers** violating a no-AI
policy. Its reading: *"some people will evade detection carefully, while many others will just copy and paste. A weak
signal still catches the second group, but the second group is a lot larger."*

**A weak, easily-defeated mark can still be useful against casual violation and useless as evidence against a
motivated one.** Both halves are true at once, and this is the topic's central tension.

## Key Takeaways

- **"Processed by", not "written by".** Anthropic's own words. A mark means Claude touched the text and nothing more.
- **A polish of your own writing is marked identically to text Claude wrote from nothing.** The law exempts that case;
  Anthropic marks it anyway.
- **No false-positive rate has been published by anyone**, which makes any adverse decision based on a detection
  unauditable today.
- **Absence of a mark proves nothing** — wrong-vintage model, too short, rewritten, metadata stripped, or a different
  vendor.
- **A vendor detector is not an AI detector.** Anthropic's tool answers "was this Claude", and returns *no* for
  ChatGPT output.
- **The honest case for it**: it catches the careless majority — 506 ICML reviewers — while a determined evader walks.
  Design for that, not for proof.
