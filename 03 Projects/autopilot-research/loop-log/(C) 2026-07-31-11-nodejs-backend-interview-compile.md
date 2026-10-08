# (C) Compile Log — nodejs-backend-interview — 2026-07-31

> **Trigger:** interactive request ("build wiki knowledge from this video + make a handoff resource for another agent")
> **Topic:** nodejs-backend-interview (NEW — corpus-first interview topic; #73)
> **Source:** single YouTube video `6OYzD13GtKs` ("BE Interview Nguyễn Chánh Đạt", Tuấn Dương, 2026-06-17, ~63 min, VN)
> **Ended:** 2026-07-31T11:22+07:00
> **Path:** 5 (yt-dlp only — NO NotebookLM, NO yt-search)

## What was done

1. **Ingest:** `yt-dlp --write-auto-subs --sub-langs vi` → 465KB VTT → grep/sed/awk rolling-caption dedup → 1224-line clean transcript → **read in full in main loop** → faithful structured extraction (16 Q&A) to `raw/2026-07-31-nodejs-backend-interview.md`. (Python execution was SIGKILLed in this environment; used unix-tool pipeline for VTT cleaning.)
2. **Verify + draft:** Workflow `wf_a6a465f8-155` — 13 agents (6 topic drafters → 6 refute-first technical verifiers over MDN/nodejs.org/v8.dev/libuv/GraphQL-history → 1 completeness critic). 0 errors / 0 empty / 0 skipped; ~811K tokens; 110 tool calls; ~5.5 min.
3. **Main-loop QA (maker/checker):** applied 2 required edits + 2 precision fixes; **rejected** 1 verifier edit that would have broken faithfulness (overwriting the "what the interviewer said" record with the correction) — kept the faithful record + inline flag instead.
4. **Compiled 13 wiki files** with full cross-linking (0 broken links, filesystem-validated).
5. **Deliverable:** portable interview-coach handoff → `output/(C) 2026-07-31-nodejs-interview-coach-handoff.md` (self-contained; another agent can run a mock interview from it).

## Metric

- `gaps_at_start` = 1 (cold-start: the topic itself)
- `gaps_at_end` = 0 (index + all articles + scorecard + provenance present; 0 broken links; 0 stub/TODO markers)
- **`gaps_closed_ratio` = 1.0**
- **Scorecard:** 86 technical claims → 82 CONFIRMED / 3 CORRECT-BUT-INCOMPLETE / 1 MISLEADING / 0 FALSE / 0 FABRICATED. Faithfulness: 0 fabricated interview content across all 6 articles.

## Wiki files created (13)

- `wiki/nodejs-backend-interview/_index.md` (NEW)
- `.../overview.md`, `.../source-provenance.md`
- `.../01-javascript-core.md` … `.../06-testing-git-docker.md` (6 topic articles)
- `.../study-guide-and-gaps.md`, `.../claims-scorecard.md`, `.../caveats-and-corrections.md`, `.../hireui-relevance.md`

## Index updates

- `wiki/_master-index.md` — prepended `## nodejs-backend-interview` topic section
- `raw/_inventory.md` — added row (Status: compiled)
- `raw/2026-07-31-nodejs-backend-interview.md` — marked `<!-- compiled -->`

## Key finding

The single MISLEADING verdict is the **interviewer's own** claim that GraphQL "wasn't built for the frontend" — historically inverted (Facebook 2012, for mobile clients). Preserved as a faithful record, flagged, corrected in [[04-rest-graphql-api-design]] + carried into the handoff so a downstream agent doesn't re-teach it. This is the [[discard-as-garble guard]] working in the other direction: verifying an *authority's* claim, not a caption garble.

## Top unclosed gaps / follow-ups

1. **Not committed** — files are staged on branch `autopilot-research`, unstaged. User merges per convention.
2. **N=1 source** — a single interview; a future DEEPEN could add 2-3 more backend-interview videos to broaden the question bank and cross-validate the interviewer's framings.
3. **Promotion candidate?** — 13 files, but N=1 and interview-genre; hold for a 2nd interview source before considering Storm Bear promotion.

## Suggested next action

Review the topic (start at [[nodejs-backend-interview/_index]] → [[study-guide-and-gaps]]) and the handoff at `output/(C) 2026-07-31-nodejs-interview-coach-handoff.md`; then commit on the `autopilot-research` branch if satisfied. Optionally run a mock interview by pasting the handoff into a fresh agent.
