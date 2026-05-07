# Skill: notebooklm

> **Type:** Worker skill (project-local to autopilot-research)
> **Created:** 2026-04-29
> **Updated:** 2026-05-07 — calibrated to notebooklm-py v0.3.4 actual CLI
> **Backend:** [`teng-lin/notebooklm-py`](https://github.com/teng-lin/notebooklm-py) v0.3.4 (external Python CLI)
> **Reused by:** `(C) yt-pipeline.md`, `(C) autopilot-research-routine.md`
> **Storm Bear ref:** v7 wiki at `../../notebooklm-py - Beginner Analysis/`

---

## Purpose

Bridge from any URL / PDF / YouTube video / Drive file → markdown summary in `raw/`. Wraps `notebooklm-py` CLI to expose 3 high-level operations: ingest single URL, bundle multiple URLs into one notebook, and query existing notebooks via chat.

**Why notebooklm-py over direct LLM ingestion:** NotebookLM has best-in-class long-document understanding, supports YouTube transcripts natively, and produces structured artifacts (reports, mind maps, podcasts) that aren't available from raw LLM API access. notebooklm-py exposes these via 50+ Click CLI commands.

---

## Caveats (per Storm Bear v7 wiki + v0.3.4 CLI verification)

⚠️ **Read these before invoking:**

1. **Paid plan required** — NotebookLM has a free tier but artifacts (mind maps, audio overviews) may require a paid Google plan
2. **Undocumented APIs** — notebooklm-py wraps internal Google endpoints; subject to breaking changes when Google updates the web UI. Storm Bear v7 wiki documents stability practices but breakage risk is real
3. **Bus factor = 1** — solo maintainer (`teng-lin`); a stalled PR or stale Google API can block usage
4. **Rate limits propagate** — no built-in retry; if Google rate-limits, this skill surfaces the error
5. **Browser-based login REQUIRES Playwright** — `notebooklm login` uses Playwright + Chromium to drive the Google login flow. Playwright is NOT a transitive dep of notebooklm-py 0.3.4 (despite the v7 wiki summary suggesting otherwise) — must `pip install playwright && playwright install chromium` separately. Installs land in `.venv/playwright-browsers/` because the env shim sets `PLAYWRIGHT_BROWSERS_PATH`. CI/CD alternative via `NOTEBOOKLM_AUTH_JSON` env var
6. **Auth storage** — by default saved to `~/.notebooklm/storage_state.json`. Override with `--storage <path>` to keep project-local

---

## Setup gate

Before invoking, source the project env (activates venv + Playwright override) and verify dependency + auth:

```bash
# Worktree-agnostic source: cd to the autopilot-research project root in your worktree first.
[ -z "${AUTOPILOT_ROOT:-}" ] && source ./bin/autopilot-env.sh

# Verify notebooklm installed inside the venv + auth state valid
pip show notebooklm-py 2>/dev/null && notebooklm auth check 2>/dev/null
```

If either fails, abort with this message:

> **notebooklm-py setup required (Option A — project venv).** From your worktree's project folder:
> ```bash
> cd "<your-worktree>/03 Projects/autopilot-research"
> /usr/local/opt/python@3.12/bin/python3.12 -m venv .venv   # use Python 3.12 explicitly
> source bin/autopilot-env.sh                                # activate venv + set PLAYWRIGHT_BROWSERS_PATH
> pip install notebooklm-py                                  # ~170 MB Python deps
> pip install playwright                                     # additional ~50 MB
> playwright install chromium                                # ~530 MB → .venv/playwright-browsers/
> notebooklm login                                           # opens browser for Google login
> notebooklm auth check                                      # verify SID cookies present
> ```
>
> Playwright is required by `notebooklm login` but NOT installed automatically by `pip install notebooklm-py`. Install it explicitly in step 4.
>
> All deps land inside `.venv/` → `rm -rf .venv` to nuke 350 MB cleanly.
>
> NotebookLM **paid plan** is required for artifact generation (reports, mind maps, audio).

---

## Operation 1: `ingest_to_markdown(url)`

**Single URL → markdown file in `raw/`.** v0.3.4 doesn't have a one-shot "report to markdown" — we compose 3 commands.

Procedure:
1. Verify URL reachable (`curl -sI` or follow redirects)
2. Create notebook (returns ID):
   ```bash
   NB_ID=$(notebooklm create "autopilot-<slug>-<date>" --json | jq -r .id)
   ```
3. Add the URL as a source (auto-detects URL/YouTube/text):
   ```bash
   notebooklm source add "<url>" -n "$NB_ID"
   notebooklm source wait -n "$NB_ID" --timeout 300   # block until processed
   ```
4. Get AI summary (markdown by default):
   ```bash
   notebooklm summary -n "$NB_ID" > "raw/<YYYY-MM-DD>-<slug>.md"
   ```
5. (Optional) Add structured Q&A for analysis sections:
   ```bash
   notebooklm use "$NB_ID"
   notebooklm ask "What are the key takeaways?" >> "raw/<YYYY-MM-DD>-<slug>.md"
   ```
6. Append metadata header to the file (notebook_id, source URL, timestamp)
7. Persist notebook ID in `raw/.notebook-ids.json` for later querying

---

## Operation 2: `bundle_to_markdown(urls[], topic)`

**Multiple URLs → single notebook → consolidated markdown.** Used by `yt-pipeline` to bundle 5-8 videos.

Procedure:
1. Create one notebook:
   ```bash
   NB_ID=$(notebooklm create "autopilot-<topic-slug>-<date>" --json | jq -r .id)
   notebooklm use "$NB_ID"
   ```
2. For each URL (sequential — parallel may rate-limit):
   ```bash
   notebooklm source add "<url>"
   ```
3. Wait for all sources to finish:
   ```bash
   notebooklm source wait --timeout 600
   ```
4. Get summary + targeted analysis via `ask`:
   ```bash
   {
     echo "# <topic> — autopilot bundle"
     echo ""
     notebooklm summary
     echo ""
     echo "## Trends"
     notebooklm ask "What patterns appear across multiple sources?"
     echo "## Outliers"
     notebooklm ask "Which source disagrees? What's the contrarian take?"
     echo "## Gaps"
     notebooklm ask "What did the sources NOT cover? What deserves follow-up?"
   } > "raw/<YYYY-MM-DD>-<topic-slug>.md"
   ```
5. Append metadata header (topic, notebook_id, sources count, timestamp)
6. Return the markdown path + the notebook ID

---

## Operation 3: `query(notebook_id, question)`

**Chat against an existing notebook.** Used for follow-up questions without re-ingesting sources.

Procedure:
1. Verify notebook ID exists:
   ```bash
   notebooklm list --json | jq -r '.[].id' | grep -q "<notebook_id>"
   ```
2. Set context + ask:
   ```bash
   notebooklm use "<notebook_id>"
   notebooklm ask "<question>"        # plain text
   notebooklm ask "<question>" --json # structured w/ source IDs
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
