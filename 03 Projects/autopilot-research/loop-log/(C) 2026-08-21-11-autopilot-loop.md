# (C) Autopilot Loop — 2026-08-21-11

> **Trigger:** `/loop` (manual, operator-initiated)
> **Topic:** Homebrew — the macOS package-manager layer (VN anchor + 6.0 release)
> **Started:** 2026-08-21 ~11:16 ICT
> **Ended:** 2026-08-21 ~11:5x ICT
> **Mode:** Path A selection (`bin/autopilot-drain.py --dry-run`) + main-loop direct-write compile

## Trigger context

Operator submitted `https://www.youtube.com/watch?v=A_nvIGTNfuw` and asked whether anything in the queue blocked
shipping it — the same question that opened `deepseek-harness` two days earlier.

Pre-flight answer: **nothing blocked it.**

| Check | Result |
|---|---|
| `raw/topics-queue.md` pending topics | **0** |
| Running drain / yt-dlp / brew processes | none |
| `crontab -l` | no crontab |
| launchd `com.cvtot.autopilot-research` | loaded, fires **23:35** daily |
| Last overnight run (2026-08-20 23:35) | `pending topics: 0` → `Nothing to drain. Exiting.` |
| Corpus size | **77 topics** |

Dependency gate (routine Phase 0.3): `yt-dlp 2026.06.09` ✅ · venv Python `3.12.13` ✅ · `notebooklm-py 0.3.4` ✅
(present but deliberately unused).

## Operator decisions

Two questions were put before any work started, because they materially changed the deliverable:

1. **Scope** → *anchored 6-video bundle* (over single-source capture / a vault-hygiene framing / skip-as-off-goal).
2. **Timing** → *now, via `/loop`* (over queueing for the 23:35 launchd drain).

Both concerns raised before asking were stated plainly: the topic is **off-goal** on its face (general macOS
dev-tooling, not agents), and **one 14-minute video is a thin bundle** — the corpus's only recent single-source
topic, `local-ai-coding-agents`, is precisely the one whose central claim was refuted by topic #77.

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 6 | 1 (topic absent) | 0 | **1.0** |

**Stop reason:** `gaps_closed_ratio` (1.0) ≥ target 0.5 after one cycle. Single cycle, no loop-back.

**Honest accounting of the metric:** the formula scores the topic-level gap, which one cycle closes by construction.
It does **not** capture that the cycle also *opened* **6 explicitly named unresolved items**
(`caveats-and-corrections.md` §9) and **7 deepen candidates**. The ratio is 1.0 and simultaneously
understates the remaining work. Recorded rather than smoothed.

## Sources ingested

`bin/autopilot-drain.py --dry-run`, query `Homebrew macOS package manager terminal setup`, 1 declared anchor.
**Anchor validation PASS 1/1, overlap 100%.**

1. **[ANCHOR]** `A_nvIGTNfuw` — Kunkka, VN, 14:05, 2026-08-10, 15,621 views
2. `1uvr9-zUB3w` — Hands-On Apple / **Leo Laporte, TWiT**, 2020-05-08, 78,800
3. `d4bTkiftBOk` — Warp, 2023-07-07, 452,340
4. `OPGxO1fdrT8` — Dev Neil A, 2025-12-06, 4,382
5. `ODVaw70G0ko` — Easy Tech Steps, 2026-03-26, 6,681
6. `IwzVzvDw68w` — **Better Stack**, 2026-07-29, 52,132

63,531 bytes of transcript, all read in full. **No NotebookLM.**

## Wiki articles created

- `raw/2026-08-21-homebrew-macos-package-manager-layer.md` (NEW)
- `wiki/homebrew-macos-package-manager/` — **11 files, NEW**: `_index` · `this-machine-audit` ·
  `homebrew-6-security-release` · `why-macos-has-no-package-manager` · `why-homebrew-won` · `the-three-weaknesses` ·
  `terminology-and-commands` · `the-howell-interview-story` · `claims-scorecard` · `caveats-and-corrections` ·
  `source-provenance`
- `wiki/_master-index.md` (UPDATED — topic #78 prepended)
- `raw/_inventory.md` (UPDATED — table row + coverage bullet)
- `raw/topics-queue.md` (UPDATED — moved to Completed)

**109 wikilinks filesystem-validated, 0 broken.**

## Findings

**1. The headline finding came from measuring, not reading.** No source discusses it. Because the topic was justified
on the grounds that `brew` is this project's only system-wide dependency, the ingest audited the actual host:
an **Apple M4 Pro** runs its primary Homebrew as **x86_64 under Rosetta 2** at `/usr/local` (6.0.3, 105 formulae,
first on `PATH`) while a **native arm64** install sits unused at `/opt/homebrew` (5.1.9, 27 formulae).
`python@3.12` and the whole project `.venv` are `Mach-O x86_64`. **This diagnoses the previously-unexplained
`CLAUDE.md` note that the `python3` shim was "broken"**, and it collides with Homebrew 6.0.0's
**Intel `x86_64` → Tier 3 in September 2026**. Remediation is listed and **NOT applied**.

**2. Silent-failure bug in the fetch method.** `yt-dlp --sub-langs "en.*,vi.*"` produced **no file and rc=0** for the
VN anchor; explicit `vi-orig` worked instantly. A glob matching nothing is indistinguishable from success, and
`validate_anchors()` would not have caught it — it validates *selection*, not *retrieval*. Near-miss: a wiki claiming
six sources built from five.

**3. Two rubric defects, recorded and deliberately unfixed** (Rule 3 — a rubric change mid-ingest invalidates the
bundle it produced). The recency filter is **structurally unsatisfiable on mature topics**: all three probed queries
returned only 1–2 of 15 results inside the 6-month window, so it relaxes every time and a stale-mixed bundle logs
identically to a fresh one. And `eng_ratio * 3` is **unbounded** against terms capping near 6 and 2, so the score
ranks channel smallness above reach, authority and recency combined — measured **334.29** for a 15,099-view video
against **52.84** for a 1,091,944-view one. Background task filed, including a request to report which past picks
would have changed.

**4. A hand-tally of the scorecard was wrong** (38 vs the true 46) and was caught by counting the table
mechanically, per the `deepseek-harness` rule *"tally the table, don't hand-count it."*

## Rule compliance

- **Rule 6 (token budget) — BREACHED, surfaced not hidden.** A six-source wiki ship structurally exceeds the
  4,000/task and 30,000/session budgets by more than an order of magnitude, as every prior ship in this corpus has.
  The operator explicitly elected the full bundle after the thin-bundle concern was stated. Flagging rather than
  silently overrunning.
- **Rule 3 (surgical changes)** — two known defects in `bin/autopilot-drain.py` left unfixed; filed instead.
- **Rule 7 (surface conflicts)** — the App-Store-framing contradiction between the anchor and Easy Tech Steps is
  stated and resolved in favour of the ledger framing, with reasons, not averaged.
- **Rule 12 (fail loud)** — the silent caption fetch, the wrong hand-tally, the 6 unverified claims and the
  `leetcode.com` 403 are all recorded in the wiki rather than papered over.
- **Constitutional #1 (scope)** — all writes inside `03 Projects/autopilot-research/`. `brew doctor` was **not** run
  to completion and no `brew` state was modified; the audit was read-only.
- **Constitutional #6 (no recursion)** — no `ScheduleWakeup`, no self-trigger.

## Note on a mislabeled sibling log

Running `bin/autopilot-drain.py --dry-run` by hand also emitted
`loop-log/(C) 2026-08-21-11-autopilot-overnight.md`, whose header reads *"Trigger: unattended (launchd UserAgent)"*.
That is cosmetically wrong — this was an operator-initiated `/loop`. `flush_loop_log()` hardcodes the unattended
header regardless of invocation path. Not worth a code change on its own; worth knowing when reading logs.

## Suggested next action

**Decide the prefix question.** The wiki's top recommendation is a bounded piece of real work with an external
deadline: migrate this machine's Homebrew from the Rosetta-translated `/usr/local` prefix to the native
`/opt/homebrew`, rebuild the project `.venv` from a native Python, and write up the before/after. Start with the two
read-only commands in `this-machine-audit.md` (`brew bundle dump` on both prefixes, then `brew doctor`) — they cost
nothing and size the job. **September 2026 is when Intel `x86_64` goes Tier 3 and bottles stop being published.**
