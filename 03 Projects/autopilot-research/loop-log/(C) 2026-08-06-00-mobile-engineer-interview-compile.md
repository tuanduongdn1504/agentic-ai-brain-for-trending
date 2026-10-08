# Loop log — 2026-08-06 00:46 — mobile-engineer-interview compile

**Trigger:** interactive (operator-submitted 5 video URLs). Path 5 (yt-dlp only). NOT an autopilot/cron run.
**Verbs:** research (given URLs) → compile → deliverable (cheatsheet handoff).

## Metric

- **Topics compiled:** +1 (`mobile-engineer-interview`) → corpus now includes 2 interview topics.
- **Q&A items extracted / verified:** 170 / ~166 faithful (~97%).
- **gaps_closed_ratio:** 1.0 — all 5 requested videos ingested + compiled; the 2 that failed first-pass extraction were recovered (no silent drop).
- **Deliverable:** 1 portable cheatsheet handoff (the explicit request).

## What happened

1. **Access:** all 5 videos were **Private**; anonymous yt-dlp failed. Recovered via `--cookies-from-browser chrome` (operator's logged-in session; Safari/Brave/FF/Edge had no usable store). Confirmed each video's real stack from content before committing the plan.
2. **Captions:** pulled BOTH `vi-orig` + `en` per video (EN mangles tech terms, VI preserves English words). awk cleaner → ~68K words total.
3. **Extract+verify (maker/checker):** Workflow `wf_89de7c46-db7` — 5 per-video extractors (garble-key + domain reconstruction) → 5 refute-first verifiers re-reading both transcripts. **3/5 succeeded; videos 2 (aKMV 64-min) + 3 (0n8o) hit the StructuredOutput retry cap** (strict schema + long output → truncated JSON).
4. **Recovery:** Workflow `wf_2408264b-657` — looser schema (no `additionalProperties:false`, minimal `required`) + ~30-item cap + compact-output (≤55-word answers). Both recovered. 13 agents total.
5. **Authorship:** Opus main-loop wrote the 15-file wiki + raw extraction + cheatsheet, folding in the 4 verifier technical corrections (const/final, Flutter lifecycle→State class, stack-vs-heap, `-b`/`-B`) and preserving 4 candidate misconceptions as cautionary examples.
6. **Librarian discipline:** `wiki/_master-index.md` prepended (dense entry) · `raw/_inventory.md` row added · topic `_index.md` + `[[wiki links]]` + `raw` `<!-- compiled -->` marker set.

## Artifacts

- `raw/2026-08-06-mobile-engineer-interview.md` (faithful record, compiled marker)
- `wiki/mobile-engineer-interview/` — 15 files
- `output/(C) 2026-08-06-mobile-engineer-cheatsheet-handoff.md` — portable cheatsheet
- Workflows: `wf_89de7c46-db7`, `wf_2408264b-657`

## Learnings (don't repeat the mistake)

- **Long-interview extraction needs the looser schema + item cap FROM THE START** — a strict schema + unbounded output truncates JSON on 60-min transcripts. Bake the ~30-item cap + ≤55-word answers into the extractor prompt for any interview ≥45 min.
- **Private operator videos** are reachable via `--cookies-from-browser chrome` (only Chrome had a usable cookie store on this Mac).
- **Doubly-garbled captions** (VN ASR + MT) need BOTH tracks + a verified garble key; EN alone destroys every technical term.

## Corpus-collision check

Grep-verified: no prior mobile/front-end **interview** topic. `nodejs-backend-interview` is the only other interview topic (same interviewer Tuấn Dương) — cross-linked, not colliding. Mobile-build topics (`codesistency-mobile-app-course`, `jasonlee-claude-mobile-app`) are course/build topics, distinct.

## Housekeeping flag (pre-existing, not this task's)

Two stray files sit at `wiki/` root — `04-rest-graphql-api-design.md` and `06-testing-git-docker.md` — apparently misplaced during the 2026-07-31 nodejs build (duplicates of files already inside `wiki/nodejs-backend-interview/`). Left untouched (out of scope); flagged for the operator to confirm deletion.

## Next action

Operator to review + merge the branch (branch-ship convention). Optional: run a mock interview from the cheatsheet to sanity-check it, or clean the 2 stray wiki-root files.
