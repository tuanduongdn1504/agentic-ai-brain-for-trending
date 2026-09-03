# (C) Autopilot Loop — 2026-09-03-13 — hermes-agent REVISIT

> **Trigger:** `/loop` (manual, operator-submitted URL)
> **Mode:** Path 1 — `/loop` yt-dlp-only + main-loop direct-write. **NotebookLM: none.**
> **Topic:** **REVISIT** of existing `wiki/hermes-agent/` — *not* a new topic. Corpus topic count unchanged at **79**.
> **Started:** 2026-09-03 ~13:40 · **Ended:** ~2026-09-03 late afternoon · **Duration:** ~3h wall-clock (two verification workflows ~36 min of it)
> **Companion:** the drain's own dry-run log is `(C) 2026-09-03-13-autopilot-overnight.md` (mechanical selection only).

## Trigger and operator elections

The operator asked: *"Can I start build knowledge from this video https://www.youtube.com/watch?v=k8lz9P3MrlM with loop or anything in queue now?"* — **the third time that exact question has opened a ship** (`deepseek-harness` 2026-08-18, `homebrew-macos-package-manager` 2026-08-21).

**Queue state at ask:** empty. 0 pending topics; the 2026-09-02 23:41 overnight drain had exited `Nothing to drain` rc=0; no processes running; launchd `com.cvtot.autopilot-research` armed for 23:35. **Answer: yes, lane clear.**

**Collision found before starting:** `wiki/hermes-agent/` already existed (2026-07-18, 10 articles, 22 graded claims), and the submitted anchor was the *same language, genre and framing* as that build's own anchor. Surfaced to the operator with the recommendation to run it as a revisit framed as a **replication test**, not a fresh ingest.

**Operator elected:** (1) run **now** via `/loop` rather than queue for 23:35; (2) **FULL 6-source re-drain** — the widest of three offered scopes, over the recommended anchor-only revisit, with the overlap risk stated and accepted.

**The overlap risk did not materialise.** I predicted the rubric would re-pick NetworkChuck and Tech With Tim. **0 of 6 videos overlap the prior bundle**; 1 creator overlap (Tonbi ep.1 here vs ep.3 previously — complementary). **The operator's wider scope was the better call, and my caveat was wrong on the specifics.** The wide scope is what made the replication test possible at N=6 instead of N=1.

## Per-phase record

| Phase | Result |
|---|---|
| 0 pre-flight | PASS — `AUTOPILOT_ROOT` resolved to the `KJ-OS-autopilot` worktree; venv Python 3.12.13; yt-dlp `/usr/local/bin`; notebooklm-py 0.3.4 |
| 0 inventory | Row appended to `raw/_inventory.md` (Status `raw`), updated to `compiled` at Phase 7 — constitutional rule #8 |
| 1 wiki state | 79 topics; `hermes-agent` 10 files, 22 claims, last verified 2026-07-18 |
| 2 selection | `--dry-run`: 15 candidates → 6 picked (1 anchor + 5 yt-search). **Anchor validation PASS 1/1, overlap 100%** |
| 2 fetch | **Fetch guard PASS 6/6 after 1 recovery.** 18 VTT tracks → 6 EN markdown + 1 VN original. 27,703 words EN (+12,536 VN) |
| 3 compile | 3 NEW articles + 6 existing files corrected in place |
| 4 cross-link | **137 wikilinks across 14 files, 0 broken** (validated programmatically) |
| 5 audit | 78 claims graded; 10 verification-process failures recorded |
| 6 decide | STOP — scope satisfied, both workflows returned, budget breached |
| 7 log + checkpoint | this file + inventory + queue → Completed + git commit |

## Verification

Two refute-first workflows, **248 agents / 16.42M subagent tokens / 2,872 tool calls / 1 agent error**:

- **`wf_519820ad-57c`** (115 agents, 7.52M tokens, 16.7 min): 6 transcript gatherers + 5 primary-source grounders run concurrently → merge/dedupe in code (78 unique claims from 79 extracted; **only 1 claim asserted by more than one source**) → 34 claims × 3 perspective-diverse lenses → 2 critics.
- **`wf_9ecdce57-2bc`** (133 agents, 8.90M tokens, 19.5 min): the **44 claims the first run's cap excluded**, same 3 lenses, + 1 coverage critic. **This run exists because the first run's coverage was skewed — see failure #1.**

Lenses: **primary-source** / **framing** / **time-bound**. Grounders instructed to use `curl` via Bash rather than a summarizing fetch layer (per the `ai-text-watermarking` ⭐⭐ finding).

## Final scorecard — 78 claims

**34 CONFIRMED · 15 MISLEADING · 14 UNVERIFIED · 9 FALSE · 6 CORRECTED · 0 FABRICATED**

Scoring: **majority verdict with severity tiebreak**; the 14 no-consensus panels hand-adjudicated to the primary-source lens (the only document-grounded one). **13 adjudication overrides applied**, 12 by that rule and **1 manual on corpus-convention grounds** — the anchor's *"launched this year, in 2026"* → CONFIRMED, because the 2026-07-18 build established *launch := first public release* (2026-03-12) when it graded "launched Feb 2026" FALSE; the dissenting lens used repo creation (2025-07-22), a fact the prior wiki already separates.

## Findings shipped

1. ⭐⭐⭐ **The replication test returned a third answer the design did not anticipate: vendor-seeded.** The one prior-FALSE claim that replicated is the one **Nous Research still publishes in its own README** (*"It's the only agent with a built-in learning loop"*, first paragraph, live 2026-09-03). The anchor reads it off the GitHub page and **attributes it correctly** — VN [00:55] *"ở đây họ mô tả"* = "here **they** describe". The three claims the vendor does not own drew **0 repeats and 5 contradictions** across six independent sources. **Origin predicts recurrence**; fidelity is not accuracy. → `wiki/hermes-agent/the-vendor-seeded-false-claim.md`
2. ⭐⭐ **The operator's anchor was the most accurate source in the bundle** — 11% error rate (7/9 CONFIRMED, 0 MISLEADING) vs 50% for the 398,873-view source. "Reach ≠ reliability" holds **at the extremes only**; there is no monotone trend at N=6.
3. ⭐⭐ **Hermes Desktop closes a real gap** — first-party, in-tree at `apps/desktop/` (HTTP 200 verified), MIT, macOS/Windows/Linux, and absent from the prior 10-article build. **A true no-code install exists** (prebuilt installer bundling Python/Git/ripgrep) but it is the *un*-recommended path — the vendor recommends `hermes desktop`, which starts in a terminal, and the "no coding needed" anchor demonstrates a VPS terminal session. **HermesOS does not exist** (0 org results) — a creator coinage. → `wiki/hermes-agent/hermes-desktop.md`
4. 🔴 **The Ollama Cloud trap** (most operator-relevant). Two sources present Ollama as the route to local, private inference. The documented integration is **"Ollama Cloud" — a cloud service on an API key**, default endpoint `https://ollama.com/v1`; a local override is undocumented. **The bundle's most-recommended "private" path ships data to a third party by default**, compounding the standing data-residency blocker for anything near candidate PII.
5. **The star count is the most-misreported fact about this project** — ~7,000 (05-04) → 140,000 (05-14) → 200,000+ (08-26) vs 240,313 verified. No two sources agree, and 7K→140K in 10 days is not plausible.
6. **47 days of drift:** 216,731→240,313★ · 40,656→49,189 forks · 23,647→**38,680** open issues (+63.6%, far outpacing star growth) · v0.18.2→**v0.21.0** · 27→37 tags · 6→**7** backends (+Vercel Sandbox). **10 releases in 54 days**; contributors 450+→650+ in two weeks.

## Verification-process failures (10) — Rule 12

**Six of the ten are agents asserting untruths. One reached the wiki before I caught it.**

1. **My claim cap was skewed, not random.** `CAP=34` sorted on a boolean, so ties fell to gatherer completion order: **100% of t5-tina-huang (largest reach) and 100% of t3-tonbi excluded, and 8 of the operator's 9 anchor claims excluded.** Caught by self-audit before shipping; fixed with the 133-agent second run. **The excluded sources proved to be among the least accurate** — the skew was hiding the worst material.
2. **Worst-verdict-wins scoring inflated MISLEADING by ~46%** — 19/34 reported vs 13 by majority; **9 of the 19 rested on a single lens.** The framing lens's *modal* verdict is MISLEADING (18/34 alone), so most-severe-wins promoted one instrument's bias to the verdict. Only **11 of 34** first-run panels were unanimous. Fixed by re-scoring and re-calibrating that lens for run 2.
3. 🔴 **The docs grounder fabricated a 20-platform enumeration** (Matrix, Mattermost, DingTalk, Feishu, WeCom, Weixin, QQ Bot, Yuanbao, BlueBubbles, Teams, Google Chat) attributed to the README. **The README contains none of them and no "N platforms" string at all.** It also attributed "60+ built-in tools" to a docs page it *simultaneously listed under its own failures as unreadable*. **I propagated it into `channels-providers-deployment.md`, then caught it on a manual re-read of the README and reverted.** The standing rule — verify counts yourself — was violated, then enforced.
4. **Completeness critic confabulated a 4-source pattern** ("four sources agree on February 2026"). `grep -in "februar"` across all six transcripts: **exactly one hit**. It conflated "launched in 2026" with "launched in February 2026".
5. **Same critic confabulated a 3-source pattern** on "71 skills". `grep`: **exactly one** — t4, reading a Desktop UI panel on camera.
6. **Drift-audit critic performed circular verification** — "confirmed" Desktop's macOS 12+/Windows 10-11 floors by reading **the prior wiki**. Not a primary source; `apps/desktop/README.md` names no floors. **A wiki cannot be evidence for itself.**
7. **The desktop grounder asserted a code path that 404s** (`apps/desktop/src/plugins/hermes-bots/`) — it was quoting an archived repo's claim about where its code was going.
8. **A gatherer mis-cited a timestamp** — F4 at VN [01:23]; actual [00:55] in both tracks. The headline finding rests on that quote, so it was re-verified by hand in both languages.
9. ⚠️ **GitHub API rate limit exhausted mid-run.** Unauthenticated cap is **60 req/hour**; it hit **0 remaining** while 248 agents had been told to `curl api.github.com`. Late verdicts may rest on the supplied digest rather than a fresh check, and **a rate-limit UNVERIFIED is indistinguishable from a genuine one.** `raw.githubusercontent.com` has separate, far higher limits (and is what finally settled `apps/desktop/`).
10. **One agent hard-failed** (`StructuredOutput` retry cap, 5 attempts) — that claim was adjudicated on 2 lenses instead of 3.

### Method bugs found in project tooling (2 — both silent-failure class)

- 🔴 **Silent topic-skip in the queue parser.** A topic written exactly as `raw/topics-queue.md`'s own format doc describes parses as `skip (no Query in block)` and the drain reports `Pending topics: 0` — **indistinguishable from an empty queue**. `parse_queue()` (`bin/autopilot-drain.py` ~line 102) requires the query in **backticks**, and the block regex (~line 97) requires a **blank line after the `## ` heading**; the doc mentions neither. Cost one round trip. **Background task filed.**
- 🔴 **2nd occurrence of the silent `--sub-langs` failure class** (1st: 2026-08-21 Homebrew ship). t6 `8GjyOQy19so` wrote **0 caption files at rc=0** because `en-orig` was unavailable and its absence **aborted the entire caption write** — `en` and `vi` existed and were still lost, behind nothing but a `WARNING`. Recovered with `--sub-langs "en,en-US,vi"`. **The ⭐⭐ per-video fetch guard the Homebrew ship recommended was implemented here and caught it on first use.**
- ⚠️ **`--dry-run` still does not emit video IDs** (⭐⭐ candidate open since the watermarking ship). The operator-requested overlap audit required re-running the search by hand to resolve them. **Until this lands, no bundle in this corpus is replayable.** **Background task filed.**

⚠️ **Token budget breached, loudly (Rule 6).** Nominal 4,000/task and 30,000/session. Actual **16.42M subagent tokens / 248 agents**. These caps have been obsolete for this project since at least the v0.18 build (1.83M / 44 agents); recorded as breached rather than silently ignored.

## Metric

`gaps_closed_ratio` = **(10 − 7) / 10 = 0.30** — below the 0.5 `/loop` target.

⚠️ **The metric is a poor fit for a revisit and is reported rather than gamed.** A revisit *discovers* gaps as fast as it closes them: **8 items were corrected in place** (stars/forks/issues, release, tags, backends, Windows-native, platform floor, HermesOS, Desktop coverage) while **7 were newly established as unverifiable or contested** (Portal tiers, "20+ platforms", "60+ tools", memory filenames, Desktop session continuity, Bot Mode default-on, built-in skill count). Converting an unknown-unknown into a documented unverifiable is the drain doing its job, and it *lowers* this ratio. **Recommend the routine treat revisits separately** — v2.2 codification candidate.

## Files

**NEW (3 wiki + 1 raw manifest + 7 transcripts):**
- `wiki/hermes-agent/revisit-2026-09-03.md` · `the-vendor-seeded-false-claim.md` · `hermes-desktop.md`
- `raw/2026-09-03-hermes-agent-revisit/_sources.md` + 6 EN transcripts + 1 VN original + `subs/` (18 VTT)

**CORRECTED in place (6):** `_index.md` · `overview.md` · `channels-providers-deployment.md` · `pricing-license-and-skill-hub.md` · `caveats-and-corrections.md` (+10 corrections, #7–16) · `source-provenance.md`; plus `wiki/_master-index.md`, `raw/_inventory.md`, `raw/topics-queue.md`.

## Suggested next action

**Clone the repo.** ⭐⭐⭐ Six of this drain's UNVERIFIED verdicts are document-shaped and collapse the moment someone runs `git clone` — memory filenames, real built-in skill/tool counts, whether `apps/desktop` bundles Bot Mode, and whether the Ollama endpoint can point at localhost. Every remaining ambiguity in this topic is a clone away, and no further video will settle any of them.

Then, in order: ⭐⭐⭐ **switch fan-out verification to `raw.githubusercontent.com` and/or an authenticated token** — the 60/hour unauthenticated ceiling is a structural cap on any workflow above ~20 agents and it fails *silently* into UNVERIFIED; ⭐⭐ **adopt majority-with-severity-tiebreak as the corpus default panel rule**; ⭐⭐ **never sort-then-cap on a boolean** — stratify by source so no source can reach zero coverage; ⭐ chase the pool's only **critical-comparison** source (Tonbi's *"Better than OpenClaw? Testing Hermes Agent w/ Qwen 3"*, 18,072 views) — **this bundle has zero critical sources**, which is its clearest stance gap.
