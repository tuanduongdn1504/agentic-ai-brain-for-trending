# (C) SKILL summary — notebooklm-py

> Nguồn: `SKILL.md` (26 KB, fetched via raw.githubusercontent.com 2026-04-18)
> Purpose: Complete invocation reference cho AI agents using notebooklm-py skill

## TL;DR

SKILL.md = **26 KB operations reference** agents load when user intent matches NotebookLM tasks. Covers: invocation triggers, auth flow, CRUD operations per domain (notebook/source/chat/artifact/language/profile), content generation options (audio/video/quiz/flashcard/slide-deck/mind-map/infographic/data-table/report), download formats, autonomy rules (what runs without confirmation vs needs approval), workflow patterns, Claude Code integration code samples, output JSON schemas, error handling with exit codes. **Most comprehensive skill file trong Storm Bear corpus** (v1's ECC individual skills typically <5 KB; SKILL.md = 5x larger because consolidates all domains into 1 file).

## Invocation Patterns

### Explicit triggers
- `/notebooklm` slash command
- Direct tool name reference

### Intent detection (automatic activation)
- "Create a podcast about [topic]"
- "Summarize these URLs"
- "Generate a quiz from my research"
- "Turn this into an audio overview"
- "Make flashcards for studying"

→ **Skill auto-activates on NL intent.** Agents don't need user to invoke by name.

## Authentication Flow

```bash
notebooklm login          # OAuth browser flow
notebooklm auth check     # Validates credentials
notebooklm auth check --test  # Full diagnostic with network test
```

### CI/CD alternatives
- `NOTEBOOKLM_AUTH_JSON` — env var với `storage_state.json` contents
- `NOTEBOOKLM_PROFILE=profile_name` — profile-based
- `NOTEBOOKLM_HOME=/path/to/config` — custom config dir

## Core Operations (5 domains × CRUD)

### Notebook Management
| Op | Command |
|----|---------|
| List | `notebooklm list [--json]` |
| Create | `notebooklm create "Title"` |
| Set context | `notebooklm use <id>` |
| Delete | `notebooklm delete <id>` |
| Status | `notebooklm status` |

### Source Management
| Op | Command |
|----|---------|
| Add URL/PDF/YouTube | `notebooklm source add "url\|path"` |
| List | `notebooklm source list [--json]` |
| Get fulltext | `notebooklm source fulltext <id>` |
| Get guide | `notebooklm source guide <id>` |
| Delete by ID | `notebooklm source delete <id>` |
| Delete by title | `notebooklm source delete-by-title "Title"` |
| Wait for processing | `notebooklm source wait <id> [--timeout 600]` |
| Web research (fast) | `notebooklm source add-research "query"` |
| Web research (deep) | `notebooklm source add-research "query" --mode deep` |

### Chat/Query Operations
| Op | Command |
|----|---------|
| Ask | `notebooklm ask "question"` |
| With specific sources | `notebooklm ask "q" -s src_id1 -s src_id2` |
| JSON output with refs | `notebooklm ask "q" --json` |
| Save as note | `notebooklm ask "q" --save-as-note --note-title "Title"` |
| View history | `notebooklm history` |
| Save history | `notebooklm history --save` |
| Continue conversation | `notebooklm ask "q" -c <conversation_id>` |

### Artifact & Research Status
| Op | Command |
|----|---------|
| List artifacts | `notebooklm artifact list [--json]` |
| Wait artifact | `notebooklm artifact wait <id> [-n notebook_id] [--timeout 1200]` |
| Research status | `notebooklm research status [--json]` |
| Research wait | `notebooklm research wait [-n notebook_id] --import-all [--timeout 1800]` |

### Profile Management (multi-account)
| Op | Command |
|----|---------|
| List | `notebooklm profile list` |
| Create | `notebooklm profile create work` |
| Switch | `notebooklm profile switch work` |
| One-off | `notebooklm -p work <command>` |

## Content Generation Options Matrix

### Podcast/Audio
```bash
notebooklm generate audio "instructions"
  --format [deep-dive|brief|critique|debate]
  --length [short|default|long]
  --source src_id [--source src_id2]
  --language ja --json --wait
```

### Video
```bash
notebooklm generate video "instructions"
  --format [explainer|brief]
  --style [auto|classic|whiteboard|kawaii|anime|watercolor|retro-print]
```

### Slide Deck
```bash
notebooklm generate slide-deck
  --format [detailed|presenter]
  --length [default|short]
  --append "custom instructions"
```

### Slide Revision (individual)
```bash
notebooklm generate revise-slide "prompt"
  --artifact <id> --slide N --wait
```

### Reports / Study Guides
```bash
notebooklm generate report
  --format [briefing-doc|study-guide|blog-post|custom]
  --append "extra instructions"
```

### Quiz & Flashcards
```bash
notebooklm generate quiz
  --difficulty [easy|medium|hard]
  --quantity [fewer|standard|more]

notebooklm generate flashcards
  --difficulty [easy|medium|hard]
  --quantity [fewer|standard|more]
```

### Other Artifacts
- `generate mind-map` — instant, synchronous
- `generate infographic --orientation [landscape|portrait|square]`
- `generate data-table "description"`

→ **9 artifact types × format options matrix.** Most generation flexibility of any library wrapping NotebookLM.

## Download Formats Matrix

| Artifact | CLI | Formats |
|----------|-----|---------|
| Audio | `download audio ./out.mp3` | MP3 |
| Video | `download video ./out.mp4` | MP4 |
| Slide deck | `download slide-deck ./out.pdf [--format pptx]` | PDF, **PPTX** (beyond web UI) |
| Quiz | `download quiz ./q.json [--format markdown]` | JSON, Markdown, HTML |
| Flashcards | `download flashcards ./f.json [--format html]` | JSON, Markdown, HTML |
| Report | `download report ./r.md` | Markdown |
| Mind-map | `download mind-map ./m.json` | JSON |
| Data table | `download data-table ./d.csv` | CSV |
| Batch all | `download <type> --all` | Multi-file |

## Autonomy Rules

### Run without confirmation (automatic)
- Status checks, diagnostics, listings
- Authentication operations
- Context setting (`use`, `profile switch`)
- Chat queries (without `--save-as-note`)
- Source/artifact waits in subagent context

### Require confirmation
- **Destructive ops** (`delete`)
- **Long-running generation** (`generate *`)
- **Filesystem writes** (`download`)
- **Saving to notebook** (`ask --save-as-note`, `history --save`)

→ **Explicit trust boundary.** Agents safely run read-only ops; confirm before mutation/cost/FS writes.

## Key Workflow Patterns

### Pattern 1: Interactive Research to Podcast
1. `notebooklm create "Research: topic"`
2. `notebooklm source add "url"` × N
3. `notebooklm source list --json` (verify status=ready)
4. `notebooklm generate audio "Focus on X"`
5. `notebooklm download audio ./podcast.mp3`

### Pattern 2: Automated Background Agent
1. Create + add sources
2. Generate with `--json` → capture `artifact_id`
3. Spawn subagent task:
   ```bash
   notebooklm artifact wait {artifact_id} -n {notebook_id} --timeout 600
   notebooklm download audio ./podcast.mp3 -a {artifact_id}
   ```
4. Main conversation continues

### Pattern 3: Document Analysis
1. Create notebook
2. `notebooklm source add ./doc.pdf`
3. Multi-turn chat (follow-up questions)

### Pattern 4: Deep Web Research (Background)
1. Create notebook
2. `notebooklm source add-research "topic" --mode deep --no-wait`
3. Spawn subagent: `notebooklm research wait --import-all --timeout 300`

### Pattern 5: Parallel Workflow Safety
- Always use `-n <id>` / `--notebook <id>` explicitly (avoid context file in parallel agents)
- Per-agent isolation: `NOTEBOOKLM_PROFILE=agent-$ID` or unique `NOTEBOOKLM_HOME`

## Output Formats (JSON)

Structured JSON output via `--json` flag. Sample responses:

```json
// notebooks list
{"notebooks": [{"id": "abc123de-...", "title": "Research", "created_at": "..."}]}

// source add
{"source_id": "def456...", "title": "Example", "status": "processing"}

// generate *
{"task_id": "xyz789...", "status": "pending"}

// ask --json
{
  "answer": "X is... [1] [2]",
  "conversation_id": "...",
  "references": [
    {"source_id": "abc123...", "citation_number": 1, "cited_text": "Passage snippet"}
  ]
}
```

## Error Handling

| Scenario | Cause | Resolution |
|----------|-------|-----------|
| Auth/cookie error | Session expired | `notebooklm login` → retry |
| "No notebook context" | Context not set | Use `-n <id>` |
| Rate limit | Google throttled | Wait 5-10 min, retry |
| Timeout (code 2) | Generation exceeded | Extend `--timeout` |
| "Not found" (code 1) | Invalid ID | Verify với `list` |

**Exit codes:** `0` = success, `1` = error, `2` = timeout.

## Processing Times (from SKILL.md)

| Task | Time | Recommended timeout |
|------|------|-------------------|
| Source processing | 30s–10 min | 600s |
| Research (fast) | 30s–2 min | 180s |
| Research (deep) | 15–30+ min | 1800s |
| Quiz/flashcards | 5–15 min | 900s |
| Reports | 5–15 min | 900s |
| Audio generation | 10–20 min | 1200s |
| Video generation | 15–45 min | 2700s |

→ **Explicit SLA documentation.** Agents can plan timeouts accurately.

## Reliability Tiers

**Reliable (always work):**
- Notebook ops, source management, chat, mind-maps, reports, study guides

**Rate-limited (may fail):**
- Audio, video, quiz, flashcard, infographic, slide deck generation

→ **Self-aware about fragility.** Agents can fallback on rate-limit failures.

## Claude Code Integration Scenarios (4 in SKILL.md)

1. **Generate Podcast and Wait** — subprocess + polling loop + download
2. **Batch Research with Source Waiting** — multi-source add + parallel wait + chat
3. **Deep Web Search with Subagent** — non-blocking research + subagent wait
4. **Citation Lookup** — fulltext retrieval + context extraction around citation

Each = working Python code sample. **~50-80 lines each.** Drop-in usable.

## Source Limits & Plan Details

| Plan | Sources/notebook |
|------|------------------|
| Standard | 50 |
| Plus | 100 |
| Pro | 300 |
| Ultra | 600 |

CLI doesn't enforce (applied by Google account plan).

**Supported source types:** PDFs, YouTube URLs, web URLs, Google Docs, text files, Markdown, Word docs, audio, video, images.

## Installation Verification Commands

```bash
pip install notebooklm-py
notebooklm status              # show auth user
notebooklm list --json         # valid JSON check
notebooklm doctor              # health check
notebooklm doctor --fix        # auto-fix
```

## Key Capabilities Beyond Web UI (from SKILL.md)

- Batch downloads (`download <type> --all`)
- Quiz/flashcard JSON/Markdown/HTML export
- Mind-map JSON extraction
- Data table CSV export
- Slide deck editable PPTX
- Individual slide revision (`revise-slide`)
- Custom report instructions (format + append)
- Source fulltext retrieval
- Save chat/history as notebook notes
- Programmatic sharing management

## Insights vs sibling skill files

| Sibling | Skill file size | Approach |
|---------|-----------------|----------|
| ECC | ~1-5 KB per skill | Many small skills |
| Superpowers | ~2-10 KB per skill | Pattern-based skills |
| gstack | ~3-8 KB per specialist | Role-based skills |
| GSD | ~2-5 KB per command | Command-based |
| goclaw | Platform-level | Not per-skill |
| course | N/A (teaches concepts) | — |
| **notebooklm-py** | **26 KB single SKILL.md** | **Service-integration mega-skill** |

→ **notebooklm-py skill = different pattern.** One big reference doc instead of many small files. **Trade-off:** complete but overwhelming on first read. Agents load once, consult often.

## Cross-references

- Main summary: [[(C) README summary]]
- Related entities:
  - [[(C) CLI Surface]] (draws from SKILL operations matrix)
  - [[(C) Skill Integration (Claude Code + Codex + OpenClaw)]] (draws from SKILL invocation + integration scenarios)
- Sibling skill patterns:
  - ECC: many small skills (`05 Skills/*.md` in root vault)
  - gstack: role-based specialist skills
- Vault's own skill examples:
  - `../../../05 Skills/llm-wiki-ingest.md`
  - `../../../05 Skills/llm-wiki-routine.md`
