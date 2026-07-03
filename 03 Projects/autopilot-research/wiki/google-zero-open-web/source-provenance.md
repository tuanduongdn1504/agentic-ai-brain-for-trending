# Source Provenance — google-zero-open-web

## Pipeline

1. **Operator-submitted** VN video AUAte1VmtK4 (2026-07-04 session). Path 5 yt-dlp: metadata + VN auto-subs (463 deduped lines, read in full). EN subs for the VN video 429'd (rate limit) — not needed once the original was found.
2. **Original located**: VN channel description credits @theinfographicsshow → channel listing grep → **GPynHL1VNiA "Google Just Killed Websites. It's Not Good."** (2026-06-18). EN auto-subs pulled on retry with `--sleep-requests 2` (406 deduped lines, read in full). Both transcripts archived in `raw/2026-07-04-google-zero-open-web.md`.
3. **Double deep-dive** (per the operator's standing ask): the videos are third-party synthesis, so the deep-dive targeted the **13 primary-source clusters** behind the script, via Workflow **`wf_7208577a-1cc`** — **38 agents** (13 deep-divers → 24 refute-first verifiers on 16 pre-registered claims → 1 completeness critic), ~**1.87M tokens**, **817 tool calls**, ~8.2 min wall-clock.
4. **Main-loop gap-closes** (from the critic's list): Alphabet mid-2026 market cap (~$4.3T — WebSearch, stockanalysis.com + companiesmarketcap.com); "AI slop" sibling-video existence (4WyduoGpIPo, confirmed in channel listing at step 2); AIO-prevalence estimate conflict resolved as methodology difference (panel vs keyword-telemetry — documented in [[ai-overviews-timeline]]); HouseFresh recovery conflict surfaced-not-averaged (documented in [[housefresh-case-study]]).

## Verdict summary (16 claims, 24 refuter verdicts + 13 dive verdicts)

- **CONFIRMED**: C1 (×3 incl. dive), C3*, C4*, C5*, C6*, C7, C8 (dive: all 10 sub-numbers), C12 (×3), C13 (×3), C14 (×2), C16 (×2) — *dive CONFIRMED with refuter PARTIAL on paraphrase-level nuance
- **PARTIAL with corrections**: C2 (28.5% precision), C9 (timeline compression — the load-bearing correction), C10 (one sub-claim conflation), C11 ("$70M" derived-not-reported), C15 (lab-vs-production)
- **REFUTED**: C10d sub-claim ("#2 most-visited from Google search after Wikipedia") — conflation of three rankings
- Full grading table: [[caveats-and-corrections]]

## Verifier-behavior notes (for the cross-topic misfire ledger)

- **No verifier misfires this run** — first topic in recent memory with zero overridden verdicts (contrast: agent-memory-architecture ×2 critic misfires, jsm-practical-vibe-coding ×4, mosh ×5). Probable cause: all sources are mainstream web documents well inside every agent's reach — no gh-api/niche-repo blind spots, no post-cutoff products to trip the "declare-it-fictional" reflex.
- Systematic refuter caution observed: several refuters graded PARTIAL where the dive said CONFIRMED, citing paraphrase-level imprecision (e.g., C3's article-vs-podcast title format; C8's "who/what/why" gloss). These were adopted as footnotes, not corrections.
- One dive-internal contradiction caught by the critic (HouseFresh recovery vs no-recovery across two clusters) — resolved as visibility-vs-traffic metric difference, flagged unresolved on the absolute number.
- Two suspicious-number flags investigated and cleared: SparkToro's 58.5/59.7 "suspiciously round 1% gap" — both confirmed as exact primary-source figures; "48% (Mar 2026) vs 60.32% (Nov 2025)" prevalence inversion — different tools/universes, not a typo in the corpus.

## Corpus notes

- **First media/platform-economics topic** in the wiki (41 prior topics are tools/methodologies/courses/architectures). No topic-name collision: grep of `wiki/` shows only `google-antigravity-skills` sharing the "google" prefix (unrelated product).
- Cleanest source-accuracy profile the pipeline has processed for a mass-market explainer (cf. multi-agent-orchestration's invented certification, ai-web-design's reversed benchmark claims).
- The Infographics Show = 15.5M-sub production channel; VN adaptation = licensed 2-day-lag localization — first observed instance of a *licensed dub* as the operator-submitted surface (provenance chain: VN dub → EN script → ~13 primary clusters).

## Raw artifacts

- `raw/2026-07-04-google-zero-open-web.md` — provenance table + chapter map + both transcripts
- Workflow journal: run `wf_7208577a-1cc` (script preserved at the session workflows dir); full structured output parsed into the digest that grounded these articles
- Inventory row: `raw/_inventory.md` 2026-07-04 entry
