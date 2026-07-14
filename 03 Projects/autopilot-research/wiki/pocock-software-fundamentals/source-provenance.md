# Source provenance — how this topic was built and verified

## Ingestion

- **Video:** [v4F1gFy-hqg](https://www.youtube.com/watch?v=v4F1gFy-hqg) — "Software Fundamentals Matter More Than Ever" — Matt Pocock, **AI Engineer channel**, uploaded 2026-04-23, 18:26. Metadata snapshot 2026-07-14: 967,140 views / 33,112 likes.
- **Event (verified, not from the description):** AI Engineer **Europe** 2026, London, Queen Elizabeth II Centre, April 8–10 — recap: [tldrecap.tech](https://tldrecap.tech/posts/2026/aie-europe/software-fundamentals-ai/) (published 2026-04-23, same day as upload).
- **Path 5 yt-dlp:** EN auto-subs (VTT) → rolling-caption dedupe → **3,340-word clean transcript, read in full in the main loop** → `raw/2026-07-14-pocock-software-fundamentals.md` with **12 pre-registered verify flags** written BEFORE any verification ran.
- **Session-limit interruption:** ingest checkpointed + committed (`d5cd60e`) 2026-07-14 ~15:25 ICT; ship resumed same day after reset. Loop log: `loop-log/(C) 2026-07-14-15-pocock-fundamentals-autopilot-loop.md`.

## Verification

- **Workflow `wf_75a9c75d-7e4`** — 32 agents: **6 cluster dives** (skills-repo / star-timeline / aihero-course / books-Ousterhout-Beck / books-PragProg-Brooks / video-context) → **25 refute-first verifiers** (one per load-bearing finding, instructed UNREACHABLE≠REFUTED + the discard-as-garble guard verbatim) → **1 completeness critic**. ~1.56M subagent tokens, 412 tool calls, 0 errors, 0 empty results. All agents Haiku 4.5.
- **Main-loop ground-checks (operator side):** `gh api repos/mattpocock/skills` (stars 169,558; created 2026-02-03; MIT; full 39-path SKILL.md tree); direct fetches of `grill-me/SKILL.md`, `grilling/SKILL.md`, `improve-codebase-architecture/SKILL.md`; grill-me file history (`commits?path=`); WebFetch of the tldrecap recap closing the critic's URGENT event-attribution check.
- **Critic's five next-checks: all closed** — (1) event attribution re-confirmed by main-loop WebFetch; (2) "macpocockskills" garble noted in [[caveats-and-corrections]]; (3) anti-specs-to-code cross-corpus consistency confirmed against [[../pocock-real-feature-build/_index]]'s documented anti-spec stance (read this session); (4) Kent Beck constraint caveat written; (5) raw-file event correction appended.

## Verdict flow (what the layers each caught)

| Layer | Caught |
|---|---|
| Pre-registration (main loop, before verify) | "Clojure Code" garble hypothesis · 13K-vs-150K star tension · vertical-slices gap · loose numbering |
| Dives | Course name + cohort dates · book topic/tip numbers · skill paths + texts · star-growth math · view-count comparison set |
| Refute-first verifiers | **The World's-Fair event confabulation (REFUTED, corrected to AIE Europe)** · Kent Beck omitted-constraint incompleteness · view-count "sources: none given" transparency wobble |
| Completeness critic | Flags 2+10 still open (closed in main loop) · InfoQ-405 degraded Brooks wording check · star-timeline interim points unsourced |
| Main loop | Independent tldrecap fetch · gh api ground truths · corpus cross-reads |

## Fidelity notes

- Quotes from the talk are from **auto-captions** — good quality but garble-prone (see the garble list in [[caveats-and-corrections]]). Book quotes were verified against the books' published text, not the captions.
- Star-timeline interim points are approximate (secondary sources); endpoints are API ground truth.
- The Brooks "shared invisible entity" wording is via InfoQ's book coverage; InfoQ blocked one verifier (405), so the design-concept *wording* rests on the dive's fetch + secondary confirmations, while the design-tree claim was independently confirmed via O'Reilly.

## Key Takeaways

- Full pattern held: pre-register flags → dive → refute-first verify → critic → main-loop closes the remainder — and the refute-first layer caught a real confabulation this run.
- 18-claim scorecard: **13 CONFIRMED / 2 CORRECT-BUT-INCOMPLETE (speaker) · 1 CORRECT-BUT-INCOMPLETE / 2 MISLEADING (description) · 0 FALSE · 0 FABRICATED** ([[claims-scorecard]]).
- Cross-links: [[claims-scorecard]] · [[caveats-and-corrections]] · [[overview]].
