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

Invoke `(C) notebooklm.md` Operation 2 (`bundle_to_markdown`). Concretely:

```bash
NB_ID=$(notebooklm create "autopilot-<topic-slug>-<YYYY-MM-DD>" --json | jq -r .id)
notebooklm use "$NB_ID"
for url in "${urls[@]}"; do
  notebooklm source add "$url"
done
notebooklm source wait --timeout 600   # block up to 10 min until all processed
```

**Failure handling:**
- Source processing timeout → keep notebook intact, abort with "manual inspection required: notebook ID $NB_ID"
- One source fails (age-restricted, removed) → `source list --json` shows status; continue; report skip count
- Notebook creation fails → abort, surface error

---

## Step 4: Generate analysis

v0.3.4 has no single "report generation" command. Compose summary + targeted Q&A:

```bash
{
  echo "# ${topic} — autopilot bundle"
  echo ""
  echo "## Summary (NotebookLM auto)"
  notebooklm summary
  echo ""
  echo "## Trends"
  notebooklm ask "What patterns appear across multiple sources? What approach/framework/concept is most-mentioned? Cite sources inline."
  echo ""
  echo "## Outliers"
  notebooklm ask "Which source disagrees with the others? Where do experts conflict? What's the contrarian take?"
  echo ""
  echo "## Gaps"
  notebooklm ask "What did the sources NOT cover? What questions remain unanswered? What deserves a follow-up search?"
  echo ""
  echo "## Key Takeaways"
  notebooklm ask "Give 5-7 bullets distilling the most actionable insights from this research set. Each bullet must cite the source by title."
} > "$raw_path"
```

If `--deliverable podcast` was passed, also:
```bash
notebooklm generate audio -n "$NB_ID"
notebooklm generate audio wait -n "$NB_ID"
notebooklm download audio -n "$NB_ID" -o "output/${topic-slug}-podcast.mp3"
```

For `--deliverable slides`: NotebookLM v0.3.4 has no slide generator. Use mind-map as alternative or fall back to report-only.

---

## Step 5: Write metadata header

The script in step 4 already wrote markdown to `raw/<YYYY-MM-DD>-<topic-slug>.md`. Now prepend a YAML metadata header:

```bash
raw_path="raw/<YYYY-MM-DD>-<topic-slug>.md"
{
  echo "---"
  echo "source: yt-pipeline"
  echo "topic: <topic>"
  echo "generated: $(date -Iseconds)"
  echo "videos_count: $N"
  echo "notebook_id: $NB_ID"
  echo "deliverable: ${deliverable:-report}"
  echo "---"
  echo ""
  cat "$raw_path"
} > "$raw_path.tmp" && mv "$raw_path.tmp" "$raw_path"
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
