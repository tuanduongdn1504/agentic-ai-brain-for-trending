# Source Provenance & Verification Ledger — ai-engineering

> Constitutional rule #4 (never fabricate) honored. Every load-bearing fact below was independently verified; corrections are logged in the open. The video's *conceptual* content is faithful to the book and low-risk; the verification effort focused on **book metadata, the author, the companion repo, and the video creator's identity** (the confabulation-prone facts).

## What was ingested

- **Video (entry point):** Anas Riad, "AI Engineering in 41 Minutes: From Demo to Production" — [geQqpO_AFMo](https://www.youtube.com/watch?v=geQqpO_AFMo), 2026-06-17, 41:54, 17,381 views. **Path 5 (yt-dlp)** — full English auto-subs pulled, deduped to a ~7,400-word transcript, **read in full**. Raw: `raw/2026-06-29-ai-engineering-chip-huyen.md`.
- **Original resource (deep-dived):** Chip Huyen, *AI Engineering: Building Applications with Foundation Models* (O'Reilly). Primary sources fetched directly: the companion repo's [chapter-summaries.md](https://github.com/chiphuyen/aie-book/blob/main/chapter-summaries.md) and [ToC.md](https://github.com/chiphuyen/aie-book/blob/main/ToC.md), the [O'Reilly product page](https://www.oreilly.com/library/view/ai-engineering/9781098166298/), and [huyenchip.com/books/](https://huyenchip.com/books/).

## How it was verified

- **Workflow `wf_508f1c32-b7b`** — 15 agents: 5 deep-dive finders (book TOC/metadata · author identity · GitHub repo · related-video + creator · skipped-chapter theses) + **9 independent skeptics** (each re-verifying one load-bearing claim from scratch) + 1 completeness critic. 520K subagent tokens, 174 tool calls, ~5 min.
- **Plus a direct primary-source fetch** of Huyen's own chapter summaries + ToC (to ground the skipped chapters in *her* words, not third-party blogs).
- One skeptic (the Claypot/NVIDIA bio claim) failed to emit structured output; that fact was independently CONFIRMED by the author-identity finder with full sourcing, so there is no gap.

## CONFIRMED (verified true)

| Claim | Verdict | Source |
|---|---|---|
| Title *AI Engineering: Building Applications with Foundation Models*, Chip Huyen, O'Reilly | ✅ CONFIRMED | oreilly.com, goodreads, amazon |
| Released Kindle **2024-12-04** / paperback **2025-01-07**; 534 pages; ISBN 9781098166298 / 9781098166304 | ✅ CONFIRMED | oreilly.com, openlibrary, amazon |
| **Exactly 10 chapters** (titles as listed in [[book-author-and-video]]) | ✅ CONFIRMED | aie-book/ToC.md, oreilly.com, deepwiki |
| Prior book *Designing Machine Learning Systems* (O'Reilly, **May 2022**, 386pp) + taught **Stanford CS329S** (from Jan 2021) | ✅ CONFIRMED | oreilly.com, stanford-cs329s.github.io, huyenchip.com |
| Official companion repo **github.com/chiphuyen/aie-book** (16.3K★, [WIP]) | ✅ CONFIRMED | github.com (README, ToC, chapter-summaries, resources) |
| Chip Huyen: NVIDIA / Snorkel / Netflix + co-founded **Claypot AI → acquired by Voltron Data (2024)**; blog huyenchip.com | ✅ CONFIRMED | huyenchip.com, LinkedIn, O'Reilly author page |
| Related video `18sMYvzqhTU` = "ML Engineering in 45 minutes (Designing ML systems)" by Anas Riad (his summary of her *first* book) | ✅ CONFIRMED | youtube/yt-dlp |
| Book has dedicated chapters on finetuning (7), dataset engineering (8), inference optimization (9) — video skips them | ✅ CONFIRMED (PARTIAL on "video skips") | aie-book/ToC.md + transcript |

## CORRECTED / FLAGGED (the confabulation guards that mattered)

1. **❌ REFUTED — the book's companion is NOT `huyenchip.com/ai-engineering`.** That URL **404s**. The companion is the **GitHub repo `chiphuyen/aie-book`**, with the books hub at `huyenchip.com/books/`. (`huyenchip.com/llama-police` exists but is an unrelated open-source-LLM directory, now GoodAIList.com — not a book companion.) *Do not cite a huyenchip.com/ai-engineering page; it does not exist.*

2. **⚠️ Anas Riad is a third-party summarizer, not official.** Verified as a **Data Scientist / ML Engineer (Cardiff) + ex-Upwork freelancer**, ~7.5K-subscriber channel, who sells a freelancing course. He is **not Chip Huyen** and the video is **not official O'Reilly/Anthropic content.** The wiki treats the **book as authority** and his "own take" as commentary. (Verdict PARTIAL: he presents specifically as Data-Scientist/ML-Engineer, not a generic "AI thought leader.")

3. **⚠️ "Most-read book on O'Reilly's platform since release" is author-reported** (huyenchip.com), not independently confirmed by O'Reilly rankings. Stated as a claim, not a fact.

4. **⚠️ Skipped-chapter theses were initially sourced from third-party summaries** (the deep-dive finder flagged it couldn't fetch the book text). **Closed** by fetching Huyen's *own* `chapter-summaries.md` — every Ch.7–10 quote in [[finetuning-dataset-inference]] and [[production-architecture-and-feedback]] now traces to her primary text.

5. **⚠️ The 5-layer production architecture** (context → guardrails → router/gateway → caches → agent patterns) is confirmed as the **Ch.10 verbatim step structure** (from ToC.md) — *not* merely her older blog post. Resolved in favor of the primary source.

6. **⚠️ Audiobook date** ("July 2025") flagged as possibly stale relative to today (2026-06-29); stated approximately ("mid-2025").

7. **No Wikipedia article** exists for Chip Huyen (only a Wikidata entry); her bio rests on primary sources (huyenchip.com, LinkedIn, O'Reilly, Stanford) — which are authoritative for this purpose.

## Confidence summary

- **Book facts, chapter structure, author, repo:** HIGH (multiple independent primary sources).
- **Video coverage claims:** HIGH — the operator read the **full transcript** (the workflow's critic worked without it and over-cautioned; the transcript resolves it).
- **Skipped-chapter detail (Ch.7–10):** HIGH — grounded in Huyen's own chapter summaries.
- **Reception / audiobook-date / "official-ness":** flagged as author-reported / approximate / explicitly-third-party.

## Cross-links

- [[book-author-and-video]] · [[overview]] · [[_index]]
