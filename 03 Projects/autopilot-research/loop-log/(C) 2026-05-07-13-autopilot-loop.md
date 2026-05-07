# (C) Autopilot Loop — 2026-05-07-13

> **Status:** Complete ✅
> **Trigger:** Auto-mode triggered by user after `notebooklm auth check` passed
> **Topic:** Claude Code hooks (calibration target per plan)
> **Started:** 2026-05-07 ~13:30
> **Ended:** 2026-05-07 ~14:00
> **Duration:** ~30 min wall-clock (mostly NotebookLM Q&A latency)
> **Worktree:** `/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research`
> **NotebookLM notebook:** `c8db4d82-8e33-4bab-ad6e-f6491bd2c3c0`

---

## Phase 0 — Pre-flight ✅

| Check | Result |
|---|---|
| yt-dlp on PATH | ✅ `/usr/local/bin/yt-dlp` v2026.03.17 |
| notebooklm in venv | ✅ v0.3.4 at `.venv/bin/notebooklm` |
| AUTOPILOT_ROOT | ✅ resolves to worktree root |
| Scope clamp | ✅ verified |
| Auth | ✅ `notebooklm auth check` passed (17 cookies, SID present) |

---

## Phase 1 — Wiki state

- Articles: 1 (only `_master-index.md`)
- Topics: 0
- **`gaps_at_start = 1`** (empty wiki = 1 gap to fill)

---

## Phase 2 — Source ingestion (yt-pipeline)

### Step 1: yt-search
20 results via `yt-dlp ytsearch20:"Claude Code hooks"`.

### Step 2: Auto-selection (5 picked from 20)
After 6-month recency filter (dropped 9 older videos), applied scoring rubric (relevance + engagement + recency + diversity):

| # | Channel | Title | Date | Duration | Eng. ratio | URL |
|---|---|---|---|---|---|---|
| 1 | AI Terminal | Hooks Deep Dive: All 9 Events | 2026-04-07 | 2:21 | 0.80× | https://www.youtube.com/watch?v=ENNZEqvodgY |
| 2 | Code Playbook | Course 11 - Hooks | 2026-02-06 | 13:07 | 0.31× | https://www.youtube.com/watch?v=bOewYZvpiNo |
| 3 | Joe Rhew | Get Notified When Tasks Finish | 2026-03-05 | 14:42 | 8.40× | https://www.youtube.com/watch?v=G9OBGn0h6LE |
| 4 | Matt Pocock | Force Claude to use right CLI | 2026-02-25 | 6:51 | 0.18× | https://www.youtube.com/watch?v=3CSi8QAoN-s |
| 5 | Simon Scrapes | Master 80% of Claude Code | 2026-04-28 | 18:23 | 0.37× | https://www.youtube.com/watch?v=0qqV4yv-Hss |

### Step 3: NotebookLM bundle
- Notebook: `c8db4d82-8e33-4bab-ad6e-f6491bd2c3c0` (`autopilot-claude-code-hooks-2026-05-07`)
- 5 sources added sequentially → all `ready` within seconds (faster than projected 5-10 min)

### Steps 4-5: Analysis + write to raw
- 1× `notebooklm summary` → output came in **Vietnamese** (account locale `.google.com.vn`)
- 4× `notebooklm ask` (Trends / Outliers / Gaps / Key Takeaways) → output in English
- Total NotebookLM API calls: **6** (within `budget_calls=10`)
- Output file: `raw/2026-05-07-claude-code-hooks.md` (255 lines, ~10 KB)

---

## Phase 3 — Compile

Topic folder created: `wiki/claude-code-hooks/`

**5 articles + 1 index:**

| File | Source section | Lines |
|---|---|---|
| `_index.md` | (synthesised) — topic index + source citations | ~50 |
| `overview.md` | NotebookLM summary + lifecycle events list | ~70 |
| `core-patterns.md` | Trends — deterministic automation, instruction budget, common use cases, filtering pattern | ~95 |
| `expert-disagreements.md` | Outliers — productivity-vs-latency, minimalist-vs-essential, AI-vs-no-AI conflicts | ~80 |
| `practical-takeaways.md` | Key Takeaways — 7 actionable rules + my synthesised adoption order | ~85 |
| `gaps-and-followups.md` | Gaps — what's NOT covered + 5 follow-up topics for next loop | ~95 |

`raw/2026-05-07-claude-code-hooks.md` marked as compiled (`<!-- compiled: 2026-05-07 ... -->` header).

`wiki/_master-index.md` updated — added `claude-code-hooks` topic entry.

---

## Phase 4 — Cross-link

Cross-links added during writing (not as a separate post-pass). 18 total `[[wiki links]]` across 6 files in the topic. No other topics in wiki yet → no inter-topic linking. First cycle pattern.

---

## Phase 5 — Audit

| Metric | Before | After | Δ |
|---|---|---|---|
| Articles | 1 | 7 | +6 |
| Topics | 0 | 1 | +1 |
| Gap markers (`(gap|TODO|missing|stub)`) | 0 | 0 | 0 |
| Wiki disk size | <1 KB | 48 KB | +48 KB |
| **`gaps`** | **1** (empty wiki) | **0** | **−1** |

**`gaps_closed_ratio = (1 − 0) / 1 = 1.0`**

(For the gap accounting: an empty wiki = 1 gap; once a topic exists with all 5 articles populated and no `(gap)` / `(TODO)` markers, count drops to 0.)

---

## Phase 6 — Decide

Stop conditions evaluated:

| Condition | Threshold | Actual | Triggered? |
|---|---|---|---|
| `gaps_closed_ratio` | ≥ 0.5 | 1.0 | ✅ STOP |
| `cycles_completed` | ≥ 5 | 1 | — |
| `wall_clock` | ≥ 60 min | ~30 min | — |
| `notebooklm_calls` | ≥ 10 | 6 | — |
| Sources processed + `_master-index` stable | both true | only first half | partial |

**Stop reason:** `gaps_closed_ratio = 1.0 >= 0.5` (target). Hand control back to user. No `ScheduleWakeup` (constitutional invariant #6 — never recurse).

---

## Phase 7 — Log + git checkpoint

This file written. Git commit follows.

---

## Surprises / lessons for v2 of the routine

1. **NotebookLM source processing was instant** — sources were `ready` within 1 list-poll. The `--timeout 600` budget was vast overkill. Reduce default to ~60s for v2.
2. **Summary came back in Vietnamese** — locale-driven (account on `.google.com.vn`). For English-only research, may need to set output language explicitly via `notebooklm language` group. Worth investigating for v2.
3. **`notebooklm source wait` doesn't accept "all" — requires individual source ID.** Patched yt-pipeline to use `source list --json` polling instead. Still needs a true "wait for all" helper in v2.
4. **The "report generation" step in v1 of yt-pipeline was wrong** — there's no `generate report --prompt` command in v0.3.4. Composing from `summary` + 4× `ask` works well, output quality is excellent.
5. **Token cost was low** — only 6 NotebookLM API calls for a 5-source 5-article output. Budget of 10/cycle has plenty of headroom.
6. **Output quality is high.** NotebookLM's source citations [Source N] are solid; the 4-section split (Trends / Outliers / Gaps / Key Takeaways) produced cleanly separable wiki articles.

---

## Suggested next actions (per Storm Bear prime directive)

1. **Verify the wiki articles read correctly** — open `wiki/claude-code-hooks/_index.md` in Obsidian (or any markdown viewer). Confirm `[[wiki links]]` resolve as expected.
2. **Decide on language** — if the Vietnamese summary is a problem, look at `notebooklm language list` / `notebooklm language set en` (need to check exact command).
3. **Run a second loop on a different topic** — e.g. `agent frameworks 2026` or `Claude Code plugins`. Confirms the routine is repeatable. The 5 follow-up topics in `gaps-and-followups.md` are good candidates.
4. **Calibrate v2 budget defaults** — based on this run: lower `source-wait-timeout` to 60s, keep `budget_calls=10`, drop `wall_clock_budget` to 30 min for `/loop` mode (was 60).
