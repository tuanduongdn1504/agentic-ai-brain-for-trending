# Source manifest — hermes-agent RUBRIC-REJECT AUDIT (2026-09-12)

> **This is neither a new topic nor an ordinary revisit. It is an audit OF THE SELECTION RUBRIC.**
> `wiki/hermes-agent/` already exists (built 2026-07-18, revisited 2026-09-03, 14 files, 100 graded claims).
> Corpus topic count stays at **80**.
>
> **Trigger:** operator asked *"Can I start build knowledge from this video with loop or anything in queue now?"* — the
> **fifth** time that exact question has opened a ship (`deepseek-harness` 2026-08-18, `homebrew` 2026-08-21,
> `hermes-agent` revisit 2026-09-03, `grok-bot` 2026-09-11). The queue was empty (0 pending, confirmed two ways),
> nothing was running, launchd `com.cvtot.autopilot-research` armed for 23:35.
>
> **What made this different:** the video the operator brought — `DYdvJCxWd6M` — was **already in this corpus, by name,
> in the 2026-09-03 manifest's "High-reach candidates the rubric dropped" list.** It had been surfaced by the search,
> scored, and rejected. In the nine days since, it **more than doubled** (140,334 → 294,324 views, +109.7%) while its
> two sibling videos on the same channel stayed flat (+1.5%, +2.3%) — so this is video-specific velocity, not channel growth.
>
> **Operator election:** *"Audit the rubric's rejects"* — ingest the 5 rejected sources and compare their error
> signature against the 6 the rubric selected, rather than doing a third ordinary pass on a saturated topic.
> Chosen over anchor-only, over a full re-drain, and over skipping.

## The bundle — 5 sources, all of them previously REJECTED

| # | Slug | Video ID | Channel | Views @2026-09-03 | Views @2026-09-12 | Δ | Len | Uploaded | Why it was rejected |
|---|------|----------|---------|---:|---:|---:|---|---|---|
| 1 ⚓ | `r1-metics-fulltutorial` | [DYdvJCxWd6M](https://www.youtube.com/watch?v=DYdvJCxWd6M) | **Metics Media** | 140,334 | **294,324** | **+109.7%** | 34:23 | 2026-08-31 | **Ranked out by 0.31 points** (score 7.74 vs CodeHead-t6's 8.05, a video with <half its reach) |
| 2 | `r2-codehead-5min` | [9GpWELm3_XI](https://www.youtube.com/watch?v=9GpWELm3_XI) | CodeHead | 224,435 | 253,592 | +13.0% | **4:53** | 2026-05-23 | **Structurally excluded: 293s against a 300s `MIN_DURATION_SEC` floor — by 7 seconds.** Scored #3 of 11 |
| 3 | `r3-tinahuang-hermesos` | [1CLc-VeEivk](https://www.youtube.com/watch?v=1CLc-VeEivk) | Tina Huang | 141,888 | 166,146 | +17.1% | 16:24 | 2026-08-25 | Ranked out (7.43). **The only source in the pool naming "HermesOS"** |
| 4 | `r4-metics-stepbystep` | [LvWobwr0Neg](https://www.youtube.com/watch?v=LvWobwr0Neg) | Metics Media | 129,686 | 132,606 | +2.3% | 33:48 | 2026-05-28 | Ranked out (7.13) |
| 5 | `r5-metics-ultimate` | [CwPUOVUdApE](https://www.youtube.com/watch?v=CwPUOVUdApE) | Metics Media | 117,001 | 118,772 | +1.5% | 37:08 | 2026-04-24 | Ranked out (6.85). Oldest — much of the product did not yet exist |

**Total runtime:** 2h 6m 36s. **Word counts:** r1 6,893 · r2 915 · r3 3,785 · r4 6,312 · r5 7,130 = **25,035**.

**The rejected bundle out-reached the bundle that was selected.** At selection time the 5 rejects totalled **753,344**
views against the 6 selected sources' **664,343**. The rubric discarded more reach than it kept.

## Three sources, one channel — a natural experiment

r1, r4 and r5 are all **Metics Media**, spanning 2026-04-24 → 2026-05-28 → 2026-08-31. That is the same creator
covering the same product three times across four months of heavy release churn (v0.13-era → v0.21.0). It permits a
question no previous bundle in this corpus could ask: **does one creator's accuracy drift as the product moves under
them?** The channel-diversity cap (2 per channel) would have admitted at most two of the three anyway.

## Fetch method

`yt-dlp --cookies-from-browser chrome --skip-download --write-subs --write-auto-subs --sub-langs "en-orig,en,en-US"
--sub-format vtt` → `bin/vtt-to-md.py`. All five are natively English (`en-orig` and `en` byte-identical).
**Per-slug fetch guard: PASS 5/5, zero recoveries** — the guard added after the Homebrew ship's silent `--sub-langs`
failure, which caught a real failure on the 2026-09-03 run.

**NotebookLM: none.** 25,035 words is direct-read range, and a claims scorecard cannot grade a paraphrase.

## Grounding — pre-fetched local snapshot, not live lookups

Every verifier graded against **one identical local snapshot**, fetched once at 2026-09-12 16:20:

- `README.md` (17,688 bytes, HTTP 200)
- `apps/desktop/README.md` (10,404 bytes, HTTP 200)
- `repo.json` + `releases.json` (30 most recent releases) → condensed to `PRIMARY-FACTS.md`

This design decision closes **two** failure classes recorded on the previous two ships at once:
1. The GitHub API's unauthenticated **60/hour limit, which fails silently into UNVERIFIED** and was exhausted mid-run
   across 248 agents on 2026-09-03.
2. **Grounder fabrication** — a 2026-09-03 grounder invented a 20-platform enumeration that reached the wiki. Verifiers
   here were given the documents and forbidden from fetching anything else, so a fabrication is checkable against a
   file that still exists.

Verifiers were additionally forbidden from reading this project's own wiki (a 2026-09-03 critic "confirmed" figures by
reading our own wiki — circular), and each source's **upload date was pinned into every grader prompt** (the grok-bot
ship graded a dated claim against a live page and manufactured a false error).

## Verification

Workflow `wf_660869eb-780`: 5 gatherers (no claim cap) → **3 perspective-diverse lenses per source**
(primary-source / framing / time-bound) → **majority verdict with severity tiebreak, adjudicated in code**, no-consensus
panels resolved to the primary-source lens (the only document-grounded one) → 2 cross-source agents (contradictions;
bundle-vs-bundle comparison) → 2 critics, one of them tasked with **refuting this audit's own headline finding**.

Adjudication is deterministic code, not a model call — per CLAUDE.md Rule 5, *if code can answer, code answers*.

## Known limitation, stated up front

Channel subscriber counts used to reproduce the rubric scores are **today's**, not 2026-09-03's. YouTube does not expose
historical subscriber counts. The reproduction nonetheless returns **exactly the six sources that were actually
selected**, which is strong evidence the model is faithful; but the precise score values carry this caveat.
