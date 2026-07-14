# Caveats and corrections — Rule 12 ledger

## Source

- Verification pass 2026-07-14 ([[source-provenance]]). Nothing here changes the talk's core content; these are the precision notes required before quoting it.

## Caption garbles (auto-subs)

- **"Clojure Code for Real Engineers" / "Clojure Code" → "Claude Code"** — both the course name and the tool name are garbled throughout the transcript. Course verified at [aihero.dev](https://www.aihero.dev/cohorts/claude-code-for-real-engineers-2026-04).
- **"macpocockskills" → `mattpocock/skills`** — repo verified directly via `gh api`.
- **"John Osterhout" → John Ousterhout** — same garble the corpus logged on the podcast transcript.

## Description-vs-talk gaps (the channel's copy, not Matt)

- **"vertical slices"** promised, never covered (zero transcript mentions). If Matt has vertical-slices material it is elsewhere (possibly the excluded ~96-min workshop's tracer-bullets content — unconfirmed).
- **"AI agent swarms"** — the talk's model is one AFK agent under a human strategist; no swarms, no orchestration.
- **"18 months of teaching"** — public cohort record supports ~9 months at upload; 18 months requires counting pre-launch content development (~Oct 2024).

## Precision notes on stage quotes

- **Kent Beck** (Incremental Design, *XP Explained* 2nd ed.): original = "We invest in the design every day, **but we have the additional constraint that we need to keep our APIs stable**." Stage version drops the constraint — ironically the half that matches Matt's own interface-first thesis.
- **Brooks design tree**: real Brooks content (Ch. 2), but it is the **"Rational Model" Brooks critiques as an unrealistic account of design practice**. Using it as a deliberate *interview procedure* (grill-me) is a legitimate repurposing; presenting it as Brooks' recommendation would over-read. Note the production skill now says "**decision** tree" and no longer names Brooks.
- **Talk numbering is loose**: verbal delivery jumps to "failure mode number six" and "tip number five" without six/five enumerated items — the slide deck likely had more modes than the talk delivered. Don't cite "the six failure modes"; the talk verbally covers ~4 modes and ~5 tips.

## Skill-lifecycle drift (talk vs repo, 2026-07-14)

- **grill-me** is now a stub → `/grilling` carries the interview text, near-verbatim to the slide with "this plan"→"this", "design tree"→"decision tree", plus matured mechanics (one question at a time; facts-from-environment vs decisions-from-human; act-only-after-confirmation).
- **ubiquitous-language** deprecated → `skills/engineering/domain-modeling/` (glossary + lazy ADRs).
- Repo grew 37 → **39 skills** between 2026-07-03 and 2026-07-14; star count 154.5K → **169,558** same window.

## Verifier-misfire log (pipeline hygiene)

- **Event-attribution misfire, caught by design:** the video-context dive fetched the real World's Fair page (June 29–July 2, 2026, San Francisco) and wrongly attributed THIS talk to it. Its refute-first verifier corrected: the talk is from **AI Engineer Europe 2026 (London, QEII Centre, April 8–10)** — confirmed by upload-date logic + [tldrecap.tech recap](https://tldrecap.tech/posts/2026/aie-europe/software-fundamentals-ai/) + a main-loop WebFetch of that recap. The description's World's-Fair promo ("next week… use YOUTUBEPROMO") is *advertising the June event*, not naming the talk's venue — the bait that misled the dive. Recap gives the on-site title as possibly "**It Ain't Broke: Why Software Fundamentals Matter More Than Ever**."
- **Critic-flagged transparency wobble:** the view-count comparison cited real yt-dlp numbers but initially reported "sources: none given" — numbers were independently re-fetched and held (9.6K/3.8K/3.3K/15.8K/55.2K/35.1K/41.1K/63.5K vs 967.8K).
- **InfoQ 405:** one Brooks verifier went UNREACHABLE (InfoQ blocks fetches); the design-tree claim was confirmed via O'Reilly instead. Correct UNREACHABLE≠REFUTED behavior — the discipline holding.
- **Star-timeline interim points** (9K on Mar 23; 21.9K Apr 26; 48.5K late Apr) are verifier-reported from secondary sources and NOT independently confirmed in the main loop — treat as approximate curve shape; the endpoints (repo creation, 150.8K/154.5K/169.6K) are ground-checked.

## Key Takeaways

- Nothing load-bearing was overturned: the talk survives verification intact; all corrections are garbles, packaging, or precision trims.
- The refute-first verifier layer caught a genuine dive confabulation (wrong conference) — the architecture justified itself this run.
- Reusable lesson: **a promo line in a description is not provenance** — event attribution needs an independent source.
- Cross-links: [[claims-scorecard]] · [[source-provenance]] · [[the-originals]].
