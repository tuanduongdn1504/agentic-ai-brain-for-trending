# Skill: yt-pipeline

> **Type:** Composite skill (project-local to autopilot-research)
> **Created:** 2026-04-29
> **Depends on:** `(C) yt-search.md`, `(C) notebooklm.md`
> **Reused by:** `(C) autopilot-research-routine.md` (Phase 2)

---

## Purpose

End-to-end YouTube research pipeline. Given a topic, autonomously: search → select 5-8 best videos → bundle into NotebookLM → generate analysis (trends/outliers/gaps) → drop markdown into `raw/`. No pauses, no check-ins.

---

## Contract

| Aspect | Value |
|--------|-------|
| **Input** | research topic string + optional `--deliverable <type>` (one of: `report` (default), `podcast`, `slides`) + optional `--video-count <N>` (default 6, min 5, max 8) |
| **Output** | path to markdown file in `raw/` + key takeaways printed inline |
| **Side effects** | creates one NotebookLM notebook + writes one markdown file to `raw/` + updates `raw/.notebook-ids.json` |

---

## Setup gate

yt-pipeline inherits dep checks from `(C) yt-search.md` and `(C) notebooklm.md` — both auto-source the env shim. Pipeline itself adds one pre-flight step:

```bash
# Worktree-agnostic source: cd to the autopilot-research project root in your worktree first.
[ -z "${AUTOPILOT_ROOT:-}" ] && source ./bin/autopilot-env.sh
```

If either dep is missing, the failure surfaces from the called skill — yt-pipeline does NOT install anything.

---

## Pipeline (5 steps, fully autonomous)

```
[1] yt-search    →  20 candidate videos with metadata
       ↓
[2] auto-select  →  5-8 best per scoring rubric
       ↓
[3] notebooklm bundle  →  notebook ID + processing wait
       ↓
[4] generate analysis  →  trends/outliers/gaps report
       ↓
[5] download markdown  →  raw/<YYYY-MM-DD>-<topic-slug>.md
```

---

## Step 1: Search

Invoke `(C) yt-search.md --json` with the topic. Default filter: last 6 months.

Failure modes:
- Less than 8 videos returned → still proceed if ≥5; otherwise abort with "insufficient sources for topic <topic>"
- yt-dlp not installed → abort with setup instructions (delegated from yt-search)

---

## Step 2: Auto-selection rubric

Score each candidate video on 4 axes (each 0-1):

1. **Relevance** — keyword match between topic and title + channel description (cosine-style overlap; simple stop-word filter)
2. **Engagement** — `views / subscribers` ratio, normalized to 0-1 across the candidate set (top result = 1.0)
3. **Recency** — newer is better; linear decay from 1.0 (today) to 0.0 (6 months ago)
4. **Source diversity** — bonus if from a new channel not yet selected; penalty if same channel already picked twice

**Total score** = `0.35*relevance + 0.30*engagement + 0.20*recency + 0.15*diversity`

Pick top `<video-count>` (default 6). Always at least 5; never more than 8.

**Tiebreakers** (in order): higher relevance > newer upload > shorter duration (favors focused content over rambling).

**Edge case — all top candidates from same channel:** force include at least 2 different channels (drops the lowest-scored same-channel pick to free a slot).

---

## Step 3: Bundle into NotebookLM

Invoke `(C) notebooklm.md` with `bundle_to_markdown` operation:

```
notebooklm bundle --topic "<topic>" --urls "url1,url2,...,urlN"
```

This:
- Creates one notebook `autopilot-<topic-slug>-<YYYY-MM-DD>`
- Adds all N videos as sources (sequential)
- Waits up to 10 min for all sources to process
- Returns notebook ID

**Failure handling:**
- Source processing timeout → keep notebook intact, abort with "manual inspection required: <notebook URL>"
- One source fails (e.g., age-restricted, removed) → continue with remaining; report skip count
- Notebook creation fails → abort, surface error

---

## Step 4: Generate analysis

Pass a structured prompt to NotebookLM's report generator:

```
notebooklm generate report --notebook <id> --prompt "
Analyze these <N> videos as a coherent research set on topic '<topic>'.

Produce four sections:

## Trends
What patterns appear across multiple videos? What approach/framework/concept is most-mentioned?

## Outliers
Which video disagrees with the others? Where do experts conflict? What's the contrarian take?

## Gaps
What did the videos NOT cover? What questions remain unanswered? What deserves a follow-up search?

## Key Takeaways
5-7 bullet points distilling the most actionable insights, each citing the source video by title.

Cite all sources inline using [Source 1], [Source 2], etc.
"
```

If `--deliverable podcast` or `--deliverable slides` was passed, also generate that artifact:
```
notebooklm generate <audio|slides> --notebook <id>
```

---

## Step 5: Download + write to raw/

```
notebooklm download artifact --notebook <id> --format md \
  --output "/Users/Cvtot/KJ OS Template/03 Projects/autopilot-research/raw/<YYYY-MM-DD>-<topic-slug>.md"
```

Append metadata header to the file:

```md
---
source: yt-pipeline
topic: <topic>
generated: <ISO timestamp>
videos_count: <N>
notebook_id: <id>
deliverable: <type>
---
```

Update `raw/.notebook-ids.json` with the new entry (per `notebooklm.md` constitutional rule #4).

---

## Output (inline, before returning)

Print to stdout:

```
✅ yt-pipeline complete

Topic:       <topic>
Videos:      <N> ingested (<skipped> skipped if any)
Notebook:    <id>
Markdown:    raw/<YYYY-MM-DD>-<topic-slug>.md

═══ Key Takeaways ═══

• <takeaway 1>
• <takeaway 2>
...

═══ Next action ═══

Compile this raw file into wiki/ via the autopilot routine, OR open the markdown
to review before compiling.
```

---

## Constitutional rules

1. **NEVER skip selection** — pipeline ALWAYS runs the auto-selection rubric. No "just take the top 5 by view count"
2. **NEVER pause for confirmation** — fully autonomous. If a step fails, abort or skip per the failure handling above
3. **NEVER fabricate analysis** — if NotebookLM report generation fails, abort. Do NOT write a hand-rolled summary
4. **ALWAYS write markdown to `raw/`** — even on partial failure (e.g., 4 of 6 videos processed), produce a markdown file with what succeeded; mark the gaps explicitly
5. **ALWAYS print the inline output above** — even on partial success
6. **NEVER call yt-pipeline recursively** — outputs go to `raw/`; the autopilot routine compiles them. yt-pipeline does NOT compile

---

## Edge cases

- **Topic too narrow (yt-search returns <5 results):** abort with "narrow your topic OR increase --months window"
- **All candidates filtered by recency:** suggest `--months 12` and abort
- **Topic has language barrier (e.g., Vietnamese topic, English-only NotebookLM analysis):** still works; NotebookLM handles multilingual sources, but inline takeaways may be English-translated. Note this in the markdown header
- **NotebookLM API rate-limited mid-pipeline:** abort, leave notebook intact, surface retry-after info from the error

---

## Examples

### Example 1: default report

```
yt-pipeline "Claude Code hooks"
```
Result: `raw/2026-04-29-claude-code-hooks.md` (6 videos, report deliverable)

### Example 2: podcast deliverable

```
yt-pipeline "agent frameworks 2026" --deliverable podcast
```
Result: markdown + audio artifact (audio downloaded separately to `output/`)

### Example 3: maximum video count

```
yt-pipeline "Andrej Karpathy ML" --video-count 8
```
Result: 8-video bundle, broader coverage but more NotebookLM processing time

---

## Next action (per Storm Bear convention)

After yt-pipeline drops a markdown file in `raw/`, the autopilot-research-routine's Phase 3 (compile) processes it into wiki articles with `[[wiki links]]`. yt-pipeline's job ends at the file landing in `raw/`.
