# Skill: Autopilot Research Routine

> **Type:** Orchestration meta-skill (project-local to autopilot-research)
> **Version:** v1 — initial codification
> **Created:** 2026-04-29
> **Inspired by:** Karpathy autoresearch (`03 Projects/autoresearch - Beginner Analysis/`) + paperclip constitutional governance (`05 Skills/(C) project-code-analysis-harness.md`) + LLM Wiki routine (`05 Skills/llm-wiki-routine-v2.1.md`)
> **Depends on:** `(C) yt-pipeline.md`, `(C) notebooklm.md`
> **Triggered by:** `/loop autopilot research <topic>` OR `/schedule autopilot nightly`

---

## Purpose

Autonomous research loop that ingests sources, compiles them into a Karpathy-style wiki, audits for gaps, decides whether to continue, and logs every iteration. Bounded by quantitative metric (`gaps_closed_ratio`) + budget (wall-clock + cost). Self-stops; never recurses.

This is the **Karpathy autoresearch analog for knowledge work**:
- Their `val_bpb` → our `gaps_closed_ratio`
- Their 5-min experiment budget → our per-cycle wall-clock + cost budgets
- Their git-checkpointed iteration → our `loop-log/` + optional `git commit`
- Their `program.md` agent skill → this file

---

## Invocation

The user types one of:
- `/loop autopilot research <topic>` — manual session-bound burst
- `/schedule autopilot nightly` — cloud cron, processes `raw/topics-queue.md`

Both routes invoke this skill. The vault root CLAUDE.md `## Project-local skills registry` section makes the skill discoverable from any session.

---

## Constitutional invariants (autoresearch + paperclip)

These bind every autopilot run. Violation = run is invalid; abort, log, return control.

1. **READ-ONLY outside scope** — NEVER write outside `03 Projects/autopilot-research/`. Storm Bear's `00 Notes/`, `01 Journals/`, `02 Chess Moves/`, other `03 Projects/` entries, `04 Reviews/`, `05 Skills/`, root `CLAUDE.md`/`GOALS.md`/`PATTERN_LIBRARY.md` are off-limits for writes.
2. **ALWAYS write a dated loop log** to `loop-log/(C) YYYY-MM-DD-HH-autopilot-loop.md` per run, even on partial failure
3. **ALWAYS report metric Δ** at the end of every cycle (`gaps_closed_ratio` before vs after)
4. **NEVER fabricate sources or content** — if NotebookLM/yt-pipeline fail, the loop log says so; do not synthesize
5. **NEVER skip librarian discipline** — every raw file → wiki article must update `_master-index.md` + topic `_index.md` + `[[wiki links]]`
6. **NEVER recurse** — the autopilot does NOT call itself, does NOT call `/loop` from within, does NOT schedule wake-ups
7. **BUDGET ENFORCED** — wall-clock + cost are hard caps. Exceeded → graceful stop + log

---

## Configuration

Default budget settings (can be overridden via flags):

| Setting | Default (`/loop`) | Default (cron) | Override flag |
|---------|-------------------|----------------|---------------|
| Max cycles per run | 5 | 20 | `--max-cycles <N>` |
| Wall-clock budget | 60 min | 360 min (6h) | `--budget-minutes <N>` |
| NotebookLM calls per cycle | 10 | 10 | `--budget-calls <N>` |
| Sources per cycle | 5 | 5 | `--sources-per-cycle <N>` |
| Stop when `gaps_closed_ratio` ≥ | 0.5 | 0.3 | `--target-ratio <F>` |

---

## Phase structure (8 phases)

### Phase 0 — Pre-flight + config check (<2 min)

1. Verify scope: target = `/Users/Cvtot/KJ OS Template/03 Projects/autopilot-research/`. If any other path is requested, abort.
2. Verify dependencies:
   - `which yt-dlp` (required by yt-pipeline)
   - `pip show notebooklm-py` + `notebooklm auth status` (required by notebooklm)
   - If missing → write loop log noting the gate failure, abort.
3. Determine trigger:
   - Manual `/loop`: use the topic from invocation args
   - Cron `/schedule`: read `raw/topics-queue.md` line-by-line; pick the next unprocessed topic; mark it `IN-PROGRESS` (in-place edit OK because it's inside scope)
4. Scaffold loop log: `loop-log/(C) YYYY-MM-DD-HH-autopilot-loop.md` with metadata stub.
5. Record `start_time` + initial budget state.

**Abort conditions:** scope violation, dep missing, no topic available.

---

### Phase 1 — Wiki state read (<1 min)

1. Read `wiki/_master-index.md`. Count topics + articles.
2. Read each topic's `_index.md`. Count articles per topic.
3. Compute `gaps_at_start` = number of `(gap)`, `(missing)`, `(TODO)`, or `(stub)` markers across all `_index.md` + `_master-index.md`. (See Audit phase for definition.)
4. Record baseline in loop log.

If this is a cold-start (empty wiki), `gaps_at_start = 1` (the topic itself is a gap).

---

### Phase 2 — Source ingestion (budget = N sources/cycle)

Per cycle, pick a source-ingestion strategy:

**Strategy A — yt-pipeline (default for new topics):**
```
yt-pipeline "<topic>" --video-count 6
```
Drops one consolidated markdown file in `raw/`.

**Strategy B — single URL ingest (when topic-queue specifies a URL):**
```
notebooklm ingest "<url>" --topic-slug <topic-slug>
```

**Strategy C — process backlog (when `raw/` already has unprocessed files):**
Skip new ingestion this cycle; go straight to Phase 3.

Track `sources_added_this_cycle` + `notebooklm_calls_used`. If `notebooklm_calls_used >= budget_calls`, stop ingestion and proceed to compile.

---

### Phase 3 — Compile (per-source, <5 min each)

For each NEW file in `raw/` that hasn't been compiled yet:

1. Read the file
2. Decide topic — match against existing topics in `wiki/_master-index.md`. Create new topic folder if no match.
3. Write a wiki article:
   - File name: lowercase with hyphens (e.g., `claude-code-hooks-overview.md`)
   - `# <Title>` heading
   - `## Source` (cite raw/ path + original URL)
   - Bullet-point summary of key points (no paragraphs)
   - `## Key Takeaways` section (5-7 bullets)
   - `[[wiki links]]` to related concepts (run a quick grep across other topics' articles)
4. Update topic's `_index.md` (add a 1-line description + link)
5. Update `wiki/_master-index.md` (add topic if new; otherwise touch the description)
6. Mark the raw file as compiled — append a comment to its first line: `<!-- compiled: YYYY-MM-DD -->`. (Edit OK — file is inside scope.)

**Constitutional rule #5 enforcement:** if any of steps 4-5 fail, abort the cycle; do NOT leave wiki/ in an inconsistent state.

---

### Phase 4 — Cross-link & dedupe (<5 min)

1. For each newly-created article: scan all OTHER articles' titles + headings for keyword overlap. Add `[[wiki links]]` to top-3 most-related articles.
2. For potential duplicates (>70% title similarity): merge via consolidation note at the bottom of the older article: `> See also [[<new article>]] (<date>)`. Don't auto-merge content; just cross-reference.
3. If a wiki article references an external Storm Bear curated wiki, use the policy from `../CLAUDE.md`: `[[external|Storm Bear: <topic>]]`.

---

### Phase 5 — Audit (<2 min)

1. Re-read `wiki/_master-index.md` + every topic `_index.md`.
2. Recount gaps:
   - Stub articles (file exists, <5 lines): count as 0.5 gap
   - Topics with `(gap)` / `(TODO)` markers in `_index.md`: count as 1 gap
   - Articles citing a source that wasn't compiled: count as 1 gap
3. Compute `gaps_at_end`.
4. Compute the metric:
   ```
   gaps_closed_ratio = (gaps_at_start - gaps_at_end) / max(gaps_at_start, 1)
   ```
   Range: `[-∞, 1.0]`. Negative = cycle introduced more gaps than it closed (rare but possible).
5. Identify top-3 unclosed gaps for the loop log.

---

### Phase 6 — Decide: continue or stop (instant)

Stop conditions (whichever first):

1. `gaps_closed_ratio >= target_ratio` (default 0.5 for `/loop`, 0.3 for cron) — meaningful progress, hand control back
2. `cycles_completed >= max_cycles` (default 5 / 20)
3. `wall_clock_used >= budget_minutes` (default 60 / 360)
4. `notebooklm_calls_total >= budget_calls * cycles_completed` — cost cap
5. `_master-index.md` unchanged for 2 consecutive cycles AND raw/ has no unprocessed files

If none → loop back to Phase 2.
If any → proceed to Phase 7.

---

### Phase 7 — Log + git checkpoint (<1 min)

1. Finalize the loop log file `loop-log/(C) YYYY-MM-DD-HH-autopilot-loop.md`. Required sections:
   - **Trigger** (manual /loop OR cron /schedule)
   - **Topic** + start time + end time + duration
   - **Per-cycle metric snapshots** (table: cycle | sources added | gaps before | gaps after | ratio)
   - **Sources ingested** (paths in `raw/`)
   - **Wiki articles** created/updated (paths in `wiki/`)
   - **Final `gaps_closed_ratio`**
   - **Stop reason** (which condition fired)
   - **Suggested next action** (per Storm Bear prime directive)
2. Optional git checkpoint: if `git -C <vault> rev-parse --git-dir` succeeds (vault is git-tracked), run:
   ```bash
   git add "03 Projects/autopilot-research/"
   git commit -m "autopilot: <topic> cycle <N> (gaps: <before>→<after>)"
   ```
   Skip on vaults that aren't git repos. Constitutional rule #1 (READ-ONLY outside scope) still applies — git operates on vault root but only commits paths within scope.
3. If cron mode: update `raw/topics-queue.md` — change `IN-PROGRESS` to `DONE` for this topic.
4. Print the suggested next action to stdout for the user.

**End of routine.** No `ScheduleWakeup` call (constitutional rule #6: NEVER recurse).

---

## Loop log template

```md
# (C) Autopilot Loop — <YYYY-MM-DD-HH>

> **Trigger:** /loop OR cron
> **Topic:** <topic>
> **Started:** <ISO timestamp>
> **Ended:** <ISO timestamp>
> **Duration:** <minutes>m

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 6 | 1 | 7 | -6.0 |
| 2 | 0 | 7 | 4 | 0.43 |
| 3 | 2 | 4 | 2 | 0.5 |

## Sources ingested

- raw/2026-04-29-claude-code-hooks.md (yt-pipeline, 6 videos)
- raw/2026-04-29-anthropic-blog-hooks.md (notebooklm-py, 1 URL)

## Wiki articles created/updated

- wiki/claude-code-hooks/_index.md (NEW)
- wiki/claude-code-hooks/overview.md (NEW)
- wiki/claude-code-hooks/hooks-types.md (NEW)
- wiki/_master-index.md (UPDATED — added "claude-code-hooks" topic)

## Final metric

- `gaps_closed_ratio` = 0.71
- Stop reason: target_ratio (0.5) reached

## Top-3 unclosed gaps

1. wiki/claude-code-hooks/_index.md mentions "PreToolUse hook examples" but no article
2. wiki/claude-code-hooks/overview.md cites a 4th source not yet compiled
3. No cross-link to existing Storm Bear curated wikis (e.g., agent frameworks)

## Suggested next action

Run `/loop autopilot research Claude Code hooks` again next week to capture new sources, OR manually compile the 4th cited source listed above.
```

---

## Topic queue file format (`raw/topics-queue.md`)

For cron mode. Format: one topic per line, prefixed with status marker.

```md
# Topic Queue

- TODO: Claude Code hooks
- TODO: agent framework comparison 2026
- IN-PROGRESS: LLM evaluation methodologies   ← currently being processed
- DONE: Karpathy LLM Wiki overview            ← already compiled
- DONE: NotebookLM API best practices
- TODO: prompt caching strategies
```

The routine reads this file in Phase 0 and updates status atomically. User may add new TODO lines anytime.

---

## Edge cases

- **Cold start (empty wiki):** Phase 1 reports `gaps_at_start = 1`. Phase 5 will likely show `gaps_closed_ratio` close to 1.0 since first cycle creates everything. This is normal.
- **Topic already exists:** Phase 3 adds new articles to existing topic folder; updates `_index.md`. No duplicate topic creation.
- **All sources fail to process:** Phase 3 produces 0 articles; Phase 5 metric is 0 or negative; Phase 6 stops on `cycles_completed`. Loop log records the failures.
- **Budget exhausted mid-cycle:** finish current cycle's compile (don't leave partial wiki state), then stop.
- **Vault not git-tracked:** Phase 7 skips git commit silently; loop log still produced.

---

## Examples

### Example 1: manual loop with a topic

```
/loop autopilot research Claude Code hooks
```

Expected: 1-3 cycles, 5-12 articles in `wiki/claude-code-hooks/`, loop log in `loop-log/`.

### Example 2: cron nightly with topic queue

User has `raw/topics-queue.md` with 3 TODO topics. Sets up:

```
/schedule autopilot nightly at 2am
```

At 2am the cloud agent fires this routine. It processes the next TODO topic (or 2-3 topics if budget allows), updates the queue, writes a loop log, exits.

### Example 3: focused single-URL ingest

User wants to ingest one specific blog post and have the routine compile it without doing yt-pipeline:

```
/loop autopilot research https://example.com/blog/post-title
```

Phase 0 detects the input is a URL (not a topic phrase), routes to Strategy B in Phase 2. Single notebooklm.md ingest, then compile.

---

## How this mirrors the inspirations

| Inspiration | This routine |
|---|---|
| Karpathy autoresearch — `val_bpb` metric | `gaps_closed_ratio` |
| Karpathy autoresearch — 5-min experiment budget | wall-clock + NotebookLM call budgets |
| Karpathy autoresearch — git checkpoint per experiment | optional `git commit` in Phase 7 |
| Karpathy autoresearch — `program.md` agent skill | this file |
| Karpathy autoresearch — autonomous overnight loop | cron `/schedule` mode |
| Karpathy autoresearch — bounded autonomy (can't touch eval code) | constitutional rule #1 (scope clamp) |
| Paperclip — constitutional governance | 7 invariants above |
| Paperclip — always-produces-artifact | rule #2 (dated loop log) |
| Paperclip — read-only target | rule #1 |
| Karpathy LLM Wiki — librarian compiles raw → wiki | Phase 3 |
| Karpathy LLM Wiki — `_master-index.md` first | Phase 1 |
| Karpathy LLM Wiki — audit / lint verb | Phase 5 |

---

## Future v2 candidates (out of scope for v1)

- Adaptive budget allocation (more cycles for under-explored topics)
- Cross-topic synthesis articles auto-generated from `_master-index.md`
- Auto-promotion path: when a topic matures, file a Storm Bear v2.1 wiki request
- GitHub-issue-style "research questions" stored in `output/questions.md` and auto-triaged
- Multi-source diversity quotas (e.g., "every topic must have ≥1 academic source + ≥1 industry source")

---

## Next action (per Storm Bear prime directive)

After this skill is in place: run the smoke test, then `/loop autopilot research Claude Code hooks` (or any first real topic). The first run calibrates the v2 budget defaults.
