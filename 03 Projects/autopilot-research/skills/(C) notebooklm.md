# Skill: notebooklm

> **Type:** Worker skill (project-local to autopilot-research)
> **Created:** 2026-04-29
> **Backend:** [`teng-lin/notebooklm-py`](https://github.com/teng-lin/notebooklm-py) (external Python CLI)
> **Reused by:** `(C) yt-pipeline.md`, `(C) autopilot-research-routine.md`
> **Storm Bear ref:** v7 wiki at `../../notebooklm-py - Beginner Analysis/`

---

## Purpose

Bridge from any URL / PDF / YouTube video / Drive file → markdown summary in `raw/`. Wraps `notebooklm-py` CLI to expose 3 high-level operations: ingest single URL, bundle multiple URLs into one notebook, and query existing notebooks via chat.

**Why notebooklm-py over direct LLM ingestion:** NotebookLM has best-in-class long-document understanding, supports YouTube transcripts natively, and produces structured artifacts (reports, mind maps, podcasts) that aren't available from raw LLM API access. notebooklm-py exposes these via 50+ Click CLI commands.

---

## Caveats (per Storm Bear v7 wiki)

⚠️ **Read these before invoking:**

1. **Paid plan required** — NotebookLM has a free tier but the artifacts (mind maps, audio overviews, reports) require a paid Google plan
2. **Undocumented APIs** — notebooklm-py wraps internal Google endpoints; subject to breaking changes when Google updates the web UI. Storm Bear v7 wiki documents stability practices but breakage risk is real
3. **Bus factor = 1** — solo maintainer (`teng-lin`); a stalled PR or stale Google API can block usage
4. **Rate limits propagate** — no built-in retry; if Google rate-limits, this skill surfaces the error
5. **OAuth via Playwright** — first-time auth opens a browser window; CI/CD requires `NOTEBOOKLM_AUTH_JSON` env var

---

## Setup gate

Before invoking, source the project env (activates venv + Playwright override) and verify dependency + auth:

```bash
# Worktree-agnostic source: cd to the autopilot-research project root in your worktree first.
[ -z "${AUTOPILOT_ROOT:-}" ] && source ./bin/autopilot-env.sh

# Verify notebooklm installed inside the venv
pip show notebooklm-py 2>/dev/null && notebooklm auth status 2>/dev/null
```

If either fails, abort with this message:

> **notebooklm-py setup required (Option A — project venv).** From your worktree's project folder:
> ```bash
> cd "<your-worktree>/03 Projects/autopilot-research"   # any worktree path works
> python3 -m venv .venv                                 # if .venv missing
> source bin/autopilot-env.sh                           # activate + override Playwright path
> pip install notebooklm-py                             # ~50 MB Python deps
> python -m playwright install chromium                 # ~280 MB → .venv/playwright-browsers/
> notebooklm auth login                                 # interactive Google OAuth
> notebooklm auth status                                # verify "logged in"
> ```
>
> All deps land inside `.venv/` → `rm -rf .venv` to nuke 350 MB cleanly.
>
> NotebookLM **paid plan** is required for artifact generation (reports, mind maps, audio).

---

## Operation 1: `ingest_to_markdown(url)`

**Single URL → markdown file in `raw/`.**

Invocation:
```
notebooklm ingest "<url>" [--topic-slug <slug>]
```

Procedure:
1. Verify URL reachable (`curl -sI` or follow redirects)
2. Create a NotebookLM notebook named `autopilot-<topic-slug>-<YYYY-MM-DD>` (or auto-generated if no slug)
   ```bash
   notebooklm notebook create --name "autopilot-<slug>-<date>"
   ```
3. Capture the returned notebook ID
4. Add the URL as a source:
   ```bash
   notebooklm source add "<url>" --notebook <id>
   ```
5. Wait for source processing (poll status; max 5 min)
6. Generate the report artifact:
   ```bash
   notebooklm generate report --notebook <id>
   ```
7. Download as markdown:
   ```bash
   notebooklm download artifact --notebook <id> --format md --output "<vault>/03 Projects/autopilot-research/raw/<YYYY-MM-DD>-<slug>.md"
   ```
8. Return the markdown file path
9. (Optional) Persist notebook ID in `raw/.notebook-ids.json` for later querying

---

## Operation 2: `bundle_to_markdown(urls[], topic)`

**Multiple URLs → single notebook → consolidated markdown.** Used by `yt-pipeline` to bundle 5-8 videos.

Invocation:
```
notebooklm bundle --topic "<topic>" --urls "url1,url2,url3,..."
```

Procedure:
1. Create one notebook named `autopilot-<topic-slug>-<date>`
2. For each URL: `notebooklm source add "<url>" --notebook <id>` (sequential; parallel may rate-limit)
3. Wait for all sources to finish processing (poll until all show `ready` status, max 10 min total)
4. Generate report:
   ```bash
   notebooklm generate report --notebook <id> --prompt "Summarize trends, outliers, and gaps across all sources. Cite each source by title."
   ```
5. Download markdown report → `raw/<YYYY-MM-DD>-<topic-slug>.md`
6. Return the markdown path + the notebook ID (so downstream tools can query the bundle later)

---

## Operation 3: `query(notebook_id, question)`

**Chat against an existing notebook.** Used for follow-up questions without re-ingesting sources.

Invocation:
```
notebooklm query --notebook <id> --question "<question>"
```

Procedure:
1. Verify notebook ID exists: `notebooklm notebook list | grep <id>`
2. Send chat message:
   ```bash
   notebooklm chat send "<question>" --notebook <id>
   ```
3. Capture response, return as text (no file write — caller decides where it goes)

---

## Constitutional rules

1. **NEVER fabricate summaries** — if `notebooklm generate report` fails, abort with the error. Do not synthesize a fake summary from the URL alone
2. **NEVER write outside `raw/`** — markdown exports only land in `03 Projects/autopilot-research/raw/`
3. **NEVER auto-share notebooks** — `notebooklm sharing add` is forbidden in autopilot mode (would expand audience)
4. **ALWAYS persist notebook IDs** — successful ingests append to `raw/.notebook-ids.json`. Format:
   ```json
   {
     "<topic-slug>": {
       "notebook_id": "...",
       "created": "YYYY-MM-DD",
       "sources": ["url1", "url2"],
       "markdown_path": "raw/<YYYY-MM-DD>-<slug>.md"
     }
   }
   ```
5. **ALWAYS surface rate-limit errors verbatim** — don't silently retry; let the caller decide

---

## Edge cases

- **YouTube auto-transcript missing:** notebooklm-py will fail; surface the error
- **PDF too large (>NotebookLM limit, ~500 pages):** split or skip; report the limit
- **Source processing stuck >5 min:** abort with timeout, leave notebook intact for manual inspection
- **Auth expired mid-run:** detect via 401, abort with re-auth instructions
- **Free-tier user attempts artifact gen:** detect via permission error, surface "paid plan required" message

---

## Markdown export format

The `--format md` artifact from NotebookLM contains:
- `# <Notebook title>`
- `## Sources` (list with titles + URLs)
- `## Summary` (auto-generated)
- `## Key Themes`
- `## Quotes` (highlighted excerpts with timestamps if YouTube)
- `## References` (numbered citations back to sources)

The librarian (autopilot routine Phase 3) is responsible for further structuring this into wiki articles. notebooklm.md just delivers the raw export.

---

## Examples

### Example 1: ingest a single blog post

```
notebooklm ingest "https://simonwillison.net/2026/Apr/28/some-post/" --topic-slug llm-agents
```
Result: `raw/2026-04-29-llm-agents.md`

### Example 2: bundle YouTube videos for a topic

```
notebooklm bundle --topic "Claude Code hooks" --urls "url1,url2,url3,url4,url5"
```
Result: `raw/2026-04-29-claude-code-hooks.md` + entry in `.notebook-ids.json`

### Example 3: follow-up query against existing bundle

```
notebooklm query --notebook abc123 --question "What hooks does Karpathy specifically recommend?"
```
Result: text answer printed to stdout

---

## Next action (per Storm Bear convention)

After ingest, the autopilot routine's compile phase processes the markdown in `raw/` into structured wiki articles with `[[wiki links]]`. This skill's job ends at the file landing in `raw/`.
