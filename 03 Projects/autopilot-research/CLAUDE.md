# autopilot-research — Knowledge Base + Autopilot

> **Project type:** Karpathy-style "Obsidian RAG" + autopilot research loop
> **Created:** 2026-04-29
> **Parent vault:** Storm Bear (`/Users/Cvtot/KJ OS Template`)
> **Sources:** YouTube (yt-pipeline) + Web Clipper + arbitrary URLs (notebooklm-py)
> **Trigger surface:** `/loop autopilot research <topic>` (manual) or `/schedule autopilot nightly` (cron)

---

## Purpose

This is the **fast-cadence experimental knowledge layer** of the Storm Bear vault. The Storm Bear root vault is curated and slow (~2h per wiki, 46 wikis to date). This project is the opposite: dump raw material in, compile autonomously, query without ceremony, and surface promising threads for slow-track ingestion later.

Inspired by:
- Andrej Karpathy's [LLM Wiki / Obsidian RAG pattern](https://www.youtube.com/watch?v=kU3qYQ7ACMA) — folders + markdown + `CLAUDE.md` librarian rules; no vector DB
- Andrej Karpathy's [autoresearch](https://github.com/karpathy/autoresearch) — autonomous overnight loop with bounded experiments, quantitative metric, git checkpoints

---

## Vault Structure

```
03 Projects/autopilot-research/
├── CLAUDE.md          ← You are here. Librarian rules + skills registry.
├── .gitignore         ← Excludes .venv/, .cache/, .config/ from git.
├── bin/
│   └── autopilot-env.sh  ← Sourceable: activates .venv + Playwright override.
├── raw/               ← INBOX. Web Clipper / NotebookLM exports / yt-pipeline outputs.
├── wiki/              ← LLM-MAINTAINED knowledge base.
│   └── _master-index.md  ← Entry point. Topic listing + 1-line descriptions.
├── output/            ← Query results, audit reports, generated deliverables.
├── loop-log/          ← Autopilot iteration logs (one per /loop or /schedule run).
├── skills/            ← Project-local skills (4 files).
│   ├── (C) yt-search.md                    — search YouTube via yt-dlp
│   ├── (C) notebooklm.md                   — ingest URL/PDF → markdown
│   ├── (C) yt-pipeline.md                  — topic → 5-8 videos → NotebookLM → raw/
│   └── (C) autopilot-research-routine.md   — meta-orchestrator (8 phases)
└── .venv/             ← (Created by setup) Python venv + Playwright browsers (~350 MB).
                          Excluded from git. `rm -rf .venv` cleans everything project-local.
```

---

## Setup (Option A — project venv install, worktree-aware)

All Python deps land inside `.venv/` for clean cleanup. Only `yt-dlp` is system-wide (~10 MB via brew, justified for its size).

**Worktree note:** this branch may be checked out in multiple git worktrees. The env shim (`bin/autopilot-env.sh`) self-locates via `${BASH_SOURCE[0]}`, so the SAME script works in every worktree without modification. Each worktree gets its own independent `.venv/` and `.cache/` — no cross-contamination.

**Per-worktree setup (run once per worktree):**

```bash
# 1. yt-dlp (system-wide, small) — done ONCE across all worktrees
brew install yt-dlp

# 2. cd to the autopilot-research project root in YOUR worktree
cd "<your-worktree>/03 Projects/autopilot-research"
# Examples:
#   cd "/Users/Cvtot/KJ OS Template/03 Projects/autopilot-research"   # main vault
#   cd "/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research"  # autopilot worktree

# 3. Create project Python venv with explicit Python 3.12 (PER WORKTREE)
#    NOTE: this user's `python3` shim was broken — use the absolute path to brew Python 3.12
/usr/local/opt/python@3.12/bin/python3.12 -m venv .venv

# 4. Source env shim — self-locates AUTOPILOT_ROOT, activates venv
source bin/autopilot-env.sh

# 5. Install notebooklm-py (~170 MB Python deps in .venv/)
pip install notebooklm-py

# 6. Install Playwright + Chromium for the browser-based login flow.
#    Playwright is NOT a transitive dep of notebooklm-py 0.3.4 — must install separately.
#    PLAYWRIGHT_BROWSERS_PATH was set in step 4, so chromium lands inside .venv/.
pip install playwright
playwright install chromium    # ~530 MB → .venv/playwright-browsers/

# 7. Authenticate to Google NotebookLM (interactive — opens browser)
notebooklm login          # opens browser, log in to Google, press ENTER in terminal
notebooklm auth check     # verify SID cookies present
```

**Verify install (1 command, run from the project root in your worktree):**

```bash
source bin/autopilot-env.sh && which yt-dlp && pip show notebooklm-py | head -2 && notebooklm auth check
```

Expected: 3 OK lines.

**Disk footprint after setup (v0.3.4 measured):**
- `.venv/` Python deps ≈ 170 MB (notebooklm-py + httpx + Playwright + click + rich + pyee + greenlet)
- `.venv/playwright-browsers/` ≈ 528 MB (Chromium + headless-shell + ffmpeg)
- yt-dlp via brew ≈ 10 MB (system-wide, only non-project location)
- `~/.notebooklm/storage_state.json` ≈ <1 KB (Google auth cookies; redirectable via `--storage`)
- **Total: ~700 MB project-local + ~10 MB system** (Playwright IS required by `notebooklm login`)

**Cleanup options:**

```bash
# Free Playwright + Python deps (~350 MB), keep wiki + auth state
rm -rf .venv

# Free everything project-installed including auth
rm -rf .venv .cache .config

# Nuke project entirely (also removes your knowledge base!)
cd .. && rm -rf autopilot-research
```

**Re-install after cleanup:** repeat steps 2-5 above.

---

## Knowledge Base Rules (Karpathy "Obsidian RAG")

You are the **librarian** of the `wiki/` folder. The user rarely edits wiki files directly.

### Folder responsibilities

- `raw/` — the inbox. When the user dumps files here (or yt-pipeline does), you process them into the wiki during a "compile" step.
- `wiki/` — your domain. You write and maintain everything in it.
- `wiki/_master-index.md` — the entry point. Lists every topic folder with a one-line description. Always keep this up to date.
- Each topic gets its own subfolder in `wiki/` (e.g., `wiki/claude-code-hooks/`) with its own `_index.md` that lists all articles in that topic with brief descriptions.
- `output/` — for query results and generated reports. `promotion-candidates.md` lives here.
- `loop-log/` — autopilot iteration logs. Append-only.

### Always use `[[wiki links]]` to connect related concepts across topics.

### Compiling (when raw/ has new material)

1. Read the raw file
2. Decide which topic it belongs to (or create a new one)
3. Write a wiki article with key takeaways and relevant `[[wiki links]]`
4. Update that topic's `_index.md`
5. Update `wiki/_master-index.md`
6. If a raw file spans multiple topics, create articles in both and cross-link

### Article conventions

- File names: lowercase with hyphens (e.g., `claude-code-hooks-overview.md`)
- Keep articles concise — bullet points over paragraphs
- Always include a `## Key Takeaways` section
- Always cite the source (path in `raw/` or external URL)

### Querying

When answering questions against the knowledge base:
1. Read `wiki/_master-index.md` first to navigate
2. Drill into the relevant topic's `_index.md`
3. Read 1-3 specific articles
4. Synthesize the answer

If the answer is valuable, file it back into the wiki as a new article and link to the sources you referenced. Every question makes the system smarter.

### Auditing

When the user says "audit" or "lint":
- Review every topic for inconsistent / contradictory information across articles
- Check missing cross-links between related concepts
- Identify gaps in coverage — topics that are mentioned but don't have articles yet
- Suggest 3-5 new articles that would strengthen the knowledge base
- Don't make changes yet — just give the report (write to `output/(C) YYYY-MM-DD-audit.md`)

---

## Storm Bear–specific additions

### 1. Scope clamp (CRITICAL)

**You may ONLY write inside `03 Projects/autopilot-research/`.** Never modify Storm Bear's `00 Notes/`, `01 Journals/`, `02 Chess Moves/`, other entries in `03 Projects/`, `04 Reviews/`, `05 Skills/`, or root files (`CLAUDE.md`, `GOALS.md`, `PATTERN_LIBRARY.md`).

Reading from those locations is fine. Writing is not.

### 2. Cross-vault link policy

Wiki articles MAY reference Storm Bear's curated wikis via relative path (e.g., `../notebooklm-py - Beginner Analysis/wiki/...`) BUT must mark the link clearly:

- ✅ `[[external|Storm Bear: notebooklm-py overview]]`
- ❌ `[[notebooklm-py overview]]` (looks like a local wiki link, but isn't)

This makes cross-references explicit and prevents confusion when the autopilot wiki and Storm Bear's curated wiki overlap on a topic.

### 3. Promotion path

When a topic in autopilot wiki matures (≥5 articles, stable across 2+ audit cycles), append a one-liner to `output/promotion-candidates.md`:

```md
- 2026-MM-DD: claude-code-hooks (8 articles, stable since YYYY-MM-DD) — propose Storm Bear v47 wiki via llm-wiki-routine-v2.1
```

The user reviews `promotion-candidates.md` periodically and decides whether to run the slow-track full LLM Wiki ingest.

### 4. Local skills registry

The 4 skills in `skills/` and their dependency arrows:

```
autopilot-research-routine ──┬── yt-pipeline ──┬── yt-search   (yt-dlp)
                             │                 └── notebooklm  (notebooklm-py CLI)
                             └── notebooklm    (also called directly for non-YouTube URLs)
```

| Skill | Reads | Writes |
|---|---|---|
| `(C) yt-search.md` | network (yt-dlp) | stdout (structured list) |
| `(C) notebooklm.md` | network (notebooklm-py) | `raw/` (markdown exports) |
| `(C) yt-pipeline.md` | network | `raw/` (markdown summaries) |
| `(C) autopilot-research-routine.md` | `raw/`, `wiki/`, `wiki/_master-index.md` | `wiki/`, `wiki/_master-index.md`, `output/`, `loop-log/` |

---

## How to invoke

### Manual session-bound burst

```
/loop autopilot research <topic>
```

The vault root CLAUDE.md has a `## Project-local skills registry` section pointing to `skills/`. The autopilot-research-routine takes over and runs 8 phases bounded by metric + budget.

### Cron / cloud schedule

```
/schedule run autopilot research routine every night at 2am, processing topics from raw/topics-queue.md
```

A topics-queue file (you create it, format: 1 topic per line) drives nightly runs. The routine reads it, picks the next topic, runs the pipeline, logs to `loop-log/`, exits.

### Without trigger plumbing (just local prompts in this folder)

When working inside this folder in a Claude Code session, four verbs work directly:

- **`compile`** — process everything in `raw/` that hasn't been compiled yet
- **`query: <question>`** — answer using the wiki, save valuable answers as new articles
- **`audit`** — health check + suggested improvements (see Auditing section above)
- **`research <topic>`** — invoke `(C) yt-pipeline.md` then compile the result

---

## Constitutional invariants (per autopilot-research-routine)

These bind autopilot runs (not interactive sessions). Full list in `skills/(C) autopilot-research-routine.md`.

1. **READ-ONLY outside scope** — see Scope clamp above
2. **ALWAYS write a dated loop log** to `loop-log/`
3. **ALWAYS report metric Δ** at end of every cycle
4. **NEVER fabricate sources or content**
5. **NEVER skip librarian discipline** — every raw file → wiki article must update `_master-index.md` + topic `_index.md` + `[[wiki links]]`
6. **NEVER recurse** — autopilot does NOT re-trigger itself
7. **BUDGET ENFORCED** — wall-clock + cost are hard caps

---

## Next action (per Storm Bear prime directive)

After the smoke test passes (verify `yt-dlp` + `notebooklm-py` installed + authenticated): run the first end-to-end loop with a small topic (e.g. `Claude Code hooks` or any topic the user is currently exploring). The first run will calibrate budget defaults for v2 of the routine.
