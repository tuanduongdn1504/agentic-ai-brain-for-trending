# Source provenance

> How this topic's six sources were selected, fetched and verified — and the two mechanical findings that came out of doing it.

## Selection

| Step | Detail |
|---|---|
| Trigger | Operator submitted `https://www.youtube.com/watch?v=5R9Nw8eKDCA`, asking whether anything in the queue blocked shipping it |
| Queue state | `bin/autopilot-drain.py --list-only` → **`Pending topics: 0`**. No cron, no scheduled tasks, no running drain. launchd `com.cvtot.autopilot-research` loaded, fires 23:35 daily; the 2026-08-20 run had exited `Nothing to drain` |
| Query probe | Three candidate queries probed by importing `yt_search()` / `select_videos()` directly (no queue writes, no log spam) |
| Query chosen | `Anthropic Claude watermark AI generated text` — best balance of mechanism, critique and consequence coverage |
| Selection run | `bin/autopilot-drain.py --dry-run`, 1 declared anchor + 5 yt-search slots |
| Anchor validation | **PASS 1/1, overlap 100%** |
| Corpus position | topic **#79** (78 → 79) |

## The bundle

| # | ID | Title | Channel | Date | Len | Views | Track |
|---|---|---|---|---|---|---|---|
| 1 | **[ANCHOR]** `5R9Nw8eKDCA` | Tin AI Cực Hot: Gemini Flash 3.7 Ra Mắt, NotebookLM Nâng Cấp, Grok Bot & AI Watermark! | BizMate AI Official | 2026-08-19 | 14:47 | 1,683 | **`vi-orig`** |
| 2 | `3FhxdhVMJoU` | Claude Now Watermarks Its Text. How Do You Even Do That? | Squintist | 2026-08-13 | 15:00 | 176,578 | `en-orig` |
| 3 | `KUeW3zzF49A` | Claude's Watermarks Just Broke SEO | Caleb Ulku | 2026-08-14 | 10:37 | 133,195 | `en-orig` |
| 4 | `FnAqruxx-QE` | Claude Text Watermark - The Science behind it! | Code Bear | 2026-08-15 | 12:15 | 132,023 | `en-orig` |
| 5 | `vcBevA3skXU` | The Problem With Claude's Watermark | BetterWay | 2026-08-17 | 8:11 | 7,689 | `en-orig` |
| 6 | `rR2QW5WQ3aE` | Claude Is Hiding Watermarks in Your AI Text (What It Actually…) | Kyle Balmer / AI with Kyle | 2026-08-12 | 19:57 | 52,073 | `en-orig` |

**88,712 bytes / 2,193 cue lines across 6 tracks, all read in full in the main loop. No NotebookLM** — a claims
scorecard cannot grade a paraphrase (precedent: [[../engineer-of-the-future/_index]], [[../deepseek-harness/_index]]).

**Repeat channel to this corpus:** Code Bear also appears in `deepseek-harness` as "Code Bug VN". **New to the corpus:**
Squintist, Caleb Ulku, BetterWay, Kyle Balmer, BizMate AI Official.

**Bundle-shape note.** Five of six were published 2026-08-12 → 2026-08-17, all reacting to one announcement. That is
tight temporal clustering: **agreement between them is weak evidence.** The independent grounding in this topic comes
from primary documents, not from source convergence.

**Reach is inverted against depth.** The bundle's best security content — spoofing, watermark-stealing, radioactivity —
is in the **smallest** channel (BetterWay, 7,689 views). The rubric ranks engagement; it has no notion of depth.
Recorded, not fixed.

## Fetch — and the guard that was asked for

The [[../homebrew-macos-package-manager/_index]] ship closed with a ⭐⭐ deepen candidate: *"assert one transcript file
per selected video before compiling (silent-fetch-failure guard)."* **It was implemented for this ingest.**

```
=== GUARD: one non-empty transcript per selected video ===
PASS — 6/6 videos have a transcript >=2KB
```

The guard asserts, per selected video, that at least one `.vtt` exists and exceeds 2 KB — closing the exact hole from
topic #78, where `--sub-langs "en.*,vi.*"` matched nothing, returned **rc=0 and no file**, and would have produced a
wiki claiming six sources built from five. `validate_anchors()` cannot catch this: it validates **selection**, not
**retrieval**.

**The anchor again required `vi-orig` explicitly.** It has no manual subtitles; only auto-captions, listed as
`vi-orig` (Vietnamese, Original) plus ~190 machine translations. The lesson from #78 held on its first re-test.

Videos 2–6 each returned **two identical-size files** (`en-orig` and `en`); the `-orig` copy was used and the
duplicate ignored.

## ⚠️ Finding: the source bundle is not reproducible

The selection was run **three times** on the same query with the same rubric, minutes apart:

| Run | Time | Slot 4/5 outcome |
|---|---|---|
| Probe | ~13:1x | Squintist · Ulku · Code Bear · **BetterWay** · Balmer |
| `--dry-run` (the logged bundle) | 13:25 | Squintist · Ulku · Code Bear · **BetterWay** · Balmer |
| Fetch-time re-selection | ~13:3x | first 3 identical, then **"Everything AI writes is now traceable (SSALAT L7FLA)"** replaced a slot |
| Fetch-time re-selection (2nd) | ~13:4x | back to the dry-run bundle exactly |

**One of three runs produced a different bundle.** YouTube search results are not stable minute-to-minute, so
`--dry-run` does **not** lock a bundle — it records one. This was caught only because the fetch script asserted the
resolved titles against the titles the dry-run had logged; without that assertion the wiki would have cited a bundle
it did not read.

**How it was handled:** the **dry-run's logged bundle is the audit record**, so the locked titles were resolved to
URLs explicitly and those exact six videos were fetched. The drift is recorded rather than smoothed.

**Filed, not fixed** (Rule 3 — changing selection mid-ingest invalidates the bundle it produced): `--dry-run` should
emit video **IDs**, and a real drain should accept an ID list, so a selection can be replayed rather than
re-rolled.

Also still open from #78 and **deliberately unfixed here**: the recency filter is structurally unsatisfiable on mature
topics, and `eng_ratio * 3` is unbounded — visible again in this run, where one query's top pick scored **313.39**
against 49.58 for a video with 3.5× the views.

## Verification

**Workflow `wf_89d8a73f-4de`** — 11 agents, 3 phases, **749,523 tokens, 218 tool calls, 0 errors / 0 empty / 0 skipped**,
~11 minutes:

- **Read (6):** one digest agent per transcript → 148 deduped claims, 90 load-bearing
- **Ground (4):** Anthropic primary docs · EU AI Act Article 50 · watermarking literature · adversarial refuter
- **Critic (1):** completeness

**Plus 7 main-loop primary fetches**, which overturned four lens verdicts and produced the topic's scope correction:
`support.claude.com` (the settling document) · the *Nature* paper metadata · its **open-access PMC mirror** (three
figures a lens had abandoned at the paywall) · NeurIPS/Pangram · the Melbourne gym incident · Gemini 3.7 Flash ·
Manus/Meta.

**Six verification-process failures were found and are recorded in [[caveats-and-corrections]] §2.** "0 agent errors"
means nothing crashed; it does not mean the verdicts were right.

## Key Takeaways

- **Anchor validation PASS 1/1; the fetch guard PASS 6/6.** Both mechanisms did their job on first re-test.
- **`--dry-run` records a bundle, it does not lock one.** One selection in three drifted. Assert resolved titles
  against the logged bundle, and make the tool emit IDs.
- **`vi-orig` explicitly, every time**, for any Vietnamese source. A glob that matches nothing looks exactly like
  success.
- **Depth and reach were inversely correlated in this bundle** — the engagement-ranked rubric put the best security
  analysis in last place.
- **Five of six sources published within five days of one event**: their agreement is not independent corroboration.
- **The main loop must fetch the subject's own primary source.** Delegating it produced four wrong verdicts.
