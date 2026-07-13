# Caveats and corrections

## The confabulation the critic caught (Rule 12 — fail loud)

The verification workflow's own **completeness critic** (agent 17 of 17) flagged a direct contradiction between two of its own agents:

- The **dive** agent researching the coding-agent feature reported: *"I could not verify a specific 'Coding Agent' feature announced on July 11, 2026... there is no documented GA announcement, specific UI affordance like 'Assign to Copilot,' or detailed sandbox/MCP configuration in accessible pages."*
- The **verify** agent for the same claim reported CONFIRMED, citing a specific press-release URL (`github.com/newsroom/press-releases/coding-agent-for-github-copilot`) and a verbatim quote, plus a "July 2026, Enterprise tier" GA date.

Both agents had the same search scope; one finding a press release the other couldn't is a strong confabulation signal. **The critic flagged this explicitly and recommended requesting the source before trusting it.**

**Main-loop resolution:** an independent WebSearch + WebFetch pass (outside the workflow, done directly in this session) found the real GitHub Changelog entry: *"Copilot coding agent is now generally available"* dated **2025-09-25** — a real GA date, but a different one than the verifier claimed, and via a real changelog post, not the press-release URL the verifier cited. The feature is genuinely real and GA; the specific press-release quote and "July 2026" date are **not used anywhere in this wiki** and should be treated as fabricated by that one Haiku verifier. See [[coding-agent-issue-to-pr]] for the corrected article.

## Softened / quarantined specifics (not asserted as fact)

Per this project's standing discipline (unverified specifics get quarantined, not deleted or asserted):

- **GitHub issue #6235's exact reaction/comment counts.** The verification workflow's Claude-parity dive cited "3,000+ upvotes, 224 comments." An independent main-loop search found a different figure ("5,200+ reactions" as of a different date, from a third-party gist, referring to a *cluster* of duplicate issues, not #6235 alone). Both could be technically consistent with different measurement dates or scopes — but rather than pick one, this wiki states only "thousands, across a cluster of duplicate issues, still growing" (see [[agents-md-guardrail]]).
- **The `argument-hint` frontmatter field's exact regression citation** (a specific GitHub issue number and January 2026 date) is reported by the verification workflow but not independently re-confirmed by the main loop. Held as *plausible-but-unverified* in [[custom-agents-vs-subagents]] rather than stated as settled fact.
- **The coding agent's exact sandbox network/secrets constraints** were not pinned to a specific, quotable doc passage — [[coding-agent-issue-to-pr]] states the sandbox is real and isolated without over-specifying its limits.
- **A "YouTube oEmbed API" citation** in the provenance dive was flagged by the critic as possibly an imprecise tool-name (undocumented in the dive's own methodology). This is a non-issue for this wiki specifically: the video's title, channel, upload date, and view count were independently confirmed via this project's own `yt-dlp --print` metadata pull at ingest time (see [[source-provenance]]), so the provenance facts stated here don't depend on that agent's specific claim.

## Load-bearing claims the critic flagged as uncovered

Four rhetorical/framing elements from the talk were correctly identified by the critic as not fact-checkable and therefore not part of the scorecard — they are speaker framing, not GitHub product claims:

- "10x/20x/100x developer" — Chris's own aspirational framing, not a cited GitHub benchmark.
- "Human in the loop" as an approval-gate philosophy — mechanically supported by the real draft-PR-requires-review design (see [[coding-agent-issue-to-pr]]), but the "we chose this deliberately for safety" framing is the speaker's own narrative, not a documented GitHub design-rationale quote.
- The axe-vs-chainsaw metaphor — pure rhetorical color.
- "Half the room uses Claude vs. Copilot" — an audience-composition anecdote, plausible but inherently unverifiable after the fact.

## One clean caption-garble fix

The auto-generated English captions render the community term **"AI slop"** as **"AI slope"** throughout (e.g. "many of you have heard the term AI slope... I see nods here"). This is a standard ASR mishearing of a word ending in a soft consonant, not a real alternate term — confirmed directly from the raw transcript, no external check needed. "AI slop" itself (low-quality, fragmented AI-generated output) is well-established (Merriam-Webster flagged it among notable 2025 vocabulary).

## See also
[[_index]] · [[source-provenance]] · [[claims-scorecard]] · [[coding-agent-issue-to-pr]] · [[agents-md-guardrail]] · [[custom-agents-vs-subagents]]
