# Overview — the whole session in one screen

## Source

- `raw/2026-07-03-pocock-real-feature-build.md` (full transcript) · [hX7yG1KVYhI](https://www.youtube.com/watch?v=hX7yG1KVYhI) — Matt Pocock, 2026-03-18, 44:16, first-party.
- Repo: [mattpocock/course-video-manager](https://github.com/mattpocock/course-video-manager) — see [[course-video-manager-as-artifact]].

## The setup

- The repo is Matt's **real daily work tool** — a course video manager ("my one-stop shop": records videos, organizes courses, edits thumbnails, writes). Video claims ~1,200 commits / ~637 closed issues (point-in-time; 1,109+ closed by 2026-07).
- The domain already has **ghost lessons** (DB row, nothing on disk) vs **real lessons** (on-disk repo directory); the feature request is: (1) create a real lesson directly (skip the ghost step), (2) delete a real lesson directly, (3) **ghost courses** — plan a whole course without committing to a file path.
- Entry state is deliberately mundane: "you have some small tweaks based on some vague ideas… the first thing you need to do is road-test and harden those ideas."

## The 8 phases he walks through

1. **Grill me** — dictates the rough idea (Wispr-Flow-style dictation); the skill explores the codebase first, then asks one smart question at a time. See [[grill-me-in-practice]].
2. **Ubiquitous language update** — after the grilling converges, the LLM updates the repo glossary (`CONTEXT.md`) with new terms (ghost course, materialization cascade). He commits that himself. See [[ubiquitous-language-for-llms]].
3. **Write a PRD** — synthesizes the Q&A transcript into a PRD, sketching **modules** first; asks which modules need tests; files it as a GitHub issue. Matt does NOT review the PRD text. See [[prd-and-issues-pipeline]].
4. **PRD → issues** — slices the PRD into GitHub issues with blocking relationships; Matt merges two too-small slices (6 → 4 + a later count nuance) — his only edit.
5. **AFK loop** — `pnpm ralph` spins the Docker harness (provisional name **Sandcastle**); it pulls issues, implements, runs tests+types per commit, closes issues; Matt goes for a walk (~90 min). See [[sandcastle-ralph-afk-loop]].
6. **QA plan** — new session, freehand prompt: "take the last five commits and create a QA plan… save it in a GitHub issue" ("I haven't come up with a skill for this yet"). Labels it human-only so Ralph skips it.
7. **QA + feedback button** — walks the QA plan in the running app; every observation goes through the **in-app feedback button** → GitHub issue (AI-generated title + route + dictated detail) → Ralph fixes in the background *while he keeps QAing*. Six issues in 8 minutes. See [[qa-plan-and-feedback-loop]].
8. **Iterate to done** — rebuild, re-QA, more feedback; "at some point I would call this done." Total: 14 commits across the feature, ~8 Ralph iterations visible.

## What the human actually did

- **Decided scope** (ghost courses + direct create/delete belong in ONE PRD — "I'm making that decision kind of arbitrarily").
- **Answered why-questions and made trade-off calls** (option A vs B for lesson-creation flows — modeled with the LLM, not in his head).
- **Corrected one wrong claim** ("no test harness for course write service" → "look harder" → found).
- **Right-sized the issue slices.**
- **QA'd by hand** and dictated feedback.
- **Did NOT:** review the PRD, review the issues in detail, read most of the code. "What I'm doing is reviewing inputs and outputs… every so often I'll poke around the code just to make sure it's on the right track."

## Design-thinking notes embedded in the demo

- **Interfaces over implementations:** when the PRD proposed a new `materializeCourseAndLesson` method he weighed the *API shape* ("could it just be a parameter on materializeGhost? …that would be dodgy API-wise"), not the code.
- **Module-level review:** "I don't need to look inside these modules. I just want to know how they're changing."
- **Prototype-vs-ship judgment:** UI ambiguity (buttons vs modal vs checkbox) — he consciously skips a prototyping phase, ships one way, and lets QA feedback correct it (which it does: the checkbox modal wins).
- **The anti-spec stance:** the not-a-git-repo edge case surfaced only in QA → "specs-to-code is just never going to work… in the QA loop you find weird edge cases that are really hard to plan for." (His position — see [[caveats-and-corrections]] for the counter-view held elsewhere in this vault.)

## Key Takeaways

- The pipeline is **grill → glossary → PRD → issues → AFK → QA → feedback-issues → AFK again**; the human owns ideas, trade-offs, slicing, and QA — everything else is delegated.
- Front-load human effort: half the session is requirement-hardening, because "the more we do here, the less we need to do when we guide the LLM."
- Context stayed lean: ~40K tokens after 20+ minutes of grilling, thanks to Explore subagents and no-tool Q&A.
- The feature shipped through **GitHub issues as the queue** — the same queues-not-loops architecture in [[../pocock-agentic-workflow/afk-queues-not-loops]], now shown end-to-end.
