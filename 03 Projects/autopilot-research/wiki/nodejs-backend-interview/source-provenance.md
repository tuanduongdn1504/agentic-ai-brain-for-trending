# Source & Provenance

## The source

- **Video:** "BE Interview Nguyễn Chánh Đạt" — [youtube.com/watch?v=6OYzD13GtKs](https://www.youtube.com/watch?v=6OYzD13GtKs)
- **Channel:** Tuấn Dương (2 subscribers, 3 views at ingest — a tiny personal/training channel; almost certainly an internal interview recording, not a content channel)
- **Uploaded:** 2026-06-17
- **Duration:** 3792s (~63 min)
- **Language:** Vietnamese (`vi`) — **auto-captions only**, no human subtitles
- **Category:** People & Blogs

## What it is

A real **Node.js / backend internship screening interview**. A senior engineer ("anh Hoàng Phạm") technically screens **Nguyễn Chánh Đạt**, a 4th-year Software Engineering student at a Polytechnic university (Đại học Bách Khoa), for a **Node.js intern** role. A second person (channel owner "anh Tuấn" / Tuấn Dương) observes and handles the HR close. The interview is delivered Socratically and escalates from JavaScript fundamentals to Node internals, API design, and a ~20-minute dependency-injection deep dive.

## Why it was ingested

Operator goal: **prepare knowledge for interviews.** This is a dense, escalating **backend/Node.js question bank** with the interviewer's corrections attached — ideal raw material for a study guide and for a portable interview-coach agent.

## Ingestion trail

- **Path 5 (yt-dlp only)** — no NotebookLM, no yt-search (single operator-specified video).
- Transcript: `yt-dlp --skip-download --write-auto-subs --sub-langs vi --sub-format vtt` → `cap.vi.vtt` (465 KB) → `grep/sed/awk` de-duplication of rolling captions → `transcript_clean.txt` (1224 lines / 52 KB) → **read in full in the main loop**.
- Faithful structured extraction written to `raw/2026-07-31-nodejs-backend-interview.md` (the ground-truth Q&A the wiki is compiled from). Because the auto-captions are heavily garbled (see [[caveats-and-corrections]]), the extraction is the librarian's best faithful reading of intent, with every technical term reconstructed.

## Verification

- **Workflow `wf_a6a465f8-155`** — 6 topic drafters → 6 refute-first technical verifiers (live WebSearch/WebFetch against MDN, nodejs.org, v8.dev, GraphQL history) → 1 completeness critic. Maker/checker split: drafters extract + write canonical answers; verifiers try to disprove every load-bearing technical claim.
- The verification target here is **technical correctness of the canonical study answers** (not marketing-hype refutation, as with most corpus topics) — plus catching where the **interviewer himself** stated a questionable claim (notably GraphQL's origin). See [[claims-scorecard]] and [[caveats-and-corrections]].

## Corpus placement

- The corpus' **first interview / interview-prep topic** (grep-verified against 72 prior topics — no collision).
- Sibling backend/CS-fundamentals topics: [[api-types/_index]], [[data-structures-16-in-32-min/_index]], [[hoidanit-fullstack-vibe-coding/_index]], [[aws-email-at-scale-sqs-lambda-ses/_index]], [[fullstack-docker-cicd/_index]], [[pocock-software-fundamentals/_index]].

## A note on the individual

The candidate is a named real person in a publicly-posted video. This wiki extracts the **technical Q&A and learning value** for interview preparation. It notes where the candidate's answers were incomplete or inverted **only as study signal** (those are the hard questions worth drilling) — it is not a performance dossier on the person.
