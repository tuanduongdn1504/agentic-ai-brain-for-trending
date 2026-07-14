# The "teach" Skill is (near-certainly) Matt Pocock's, unattributed

## The claim (as presented in the video)

The presenter says: "cái bộ skill mà hôm trước mình có chia sẻ lên group" ("the skill pack I shared to the group the other day") — framing it as something they made/curated and are now distributing to their own private Facebook community ("Tự Học Cùng AI"). No GitHub link, no external attribution, and no vendor name is mentioned anywhere in the video or its description.

## What a direct fetch shows

A main-loop `WebFetch` of [`github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md`](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md) — Matt Pocock's own public, MIT-style Agent Skills repository — returns, verbatim:

- All **six identically-named concepts**: "Mission... A document capturing the *reason* the user is interested in the topic"; "Lesson... a single, self-contained... output that teaches one tightly-scoped thing"; "Reference... Compressed learnings from the lessons — cheat sheets, reference algorithms, syntax"; "Learning Record... Capture what the user has learned"; "Resource... A list of resources which can be explored to ground your teaching"; "Note... A scratchpad for you to jot down user preferences, or working notes."
- The **exact same three-layer model**, matching language: *"To learn at a deep level, the user needs three things: **Knowledge**, captured from high-quality, high-trust resources; **Skills**, acquired through highly-relevant interactive lessons devised by you, based on the knowledge; **Wisdom**, which comes from interacting with other learners and practitioners."*

This is not a loose thematic overlap — it is the same concept names, in the same order, with closely matching descriptive language, appearing in a Vietnamese-language video with zero mention of the English-language source repository.

## What remains genuinely unverifiable

- **We cannot see inside the private Facebook group's actual distributed ZIP file** — the video only shows the presenter's own folder-browser, not the file contents in a way that lets us diff against Pocock's `SKILL.md` line-by-line.
- It's possible (though less likely given the near-verbatim conceptual match) that the group repackaged/translated/modified Pocock's skill significantly, or built an independent skill using his public write-up as a *reference* rather than his file *as-is*.
- We cannot confirm whether the Facebook group's internal materials credit Matt Pocock somewhere the video doesn't show (e.g., in a README inside the zip). The video itself, however, gives the audience no way to know this is derived from public work.

## Why this is the headline finding, not a minor footnote

Per this vault's own governing discipline (never fabricate, never make silent assumptions, surface conflicts) — the responsible framing is: **this is very likely Matt Pocock's public work, redistributed through a closed community channel without visible attribution in the video** — not proven beyond all doubt (since the private-group contents are opaque to us), but strong enough that presenting the Skill as the channel's own original creation, without checking, would be misleading to a wiki reader.

## Corpus recurrence

This is the **third time Matt Pocock's work has surfaced in this corpus**:
1. [[../claude-skills/_index|claude-skills]] — Ben AI's "Process Interviewer" meta-skill traces to Pocock's "grill me" methodology.
2. The vault's own Pattern Library tracks `mattpocock/skills` directly (an Observational Flag on the repo's viral-velocity pattern, and a cross-port of his `/grill-with-docs` into this vault's own brain-setup routine).
3. **Here** — his public `teach` skill, appearing via a VN community redistribution with no visible credit.

Three independent appearances across three different source videos is a reasonable signal that Matt Pocock's `mattpocock/skills` repository is a genuinely load-bearing, widely-circulating artifact in the Claude/Codex Skills ecosystem — worth treating as a recurring first-party-adjacent anchor when future videos reference generically-named "skills" without a clear source.

## Verdict

**FALSE** on the "genuinely original to this VN creator, no public precedent" framing — the pedagogical structure is a known, public, pre-existing design (predates the video: Pocock's skill was live on GitHub well before the 2026-06-28 upload). **UNVERIFIABLE** on whether the actual distributed file is a byte-for-byte copy, a light localization, or an independent-but-derivative rebuild. See [[claims-scorecard]].

## See also

[[_index]] · [[overview]] · [[../claude-skills/_index]] · [[claims-scorecard]] · [[source-provenance]]
