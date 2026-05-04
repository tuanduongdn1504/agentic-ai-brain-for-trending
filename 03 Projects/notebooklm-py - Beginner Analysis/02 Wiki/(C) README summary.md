# (C) README summary — notebooklm-py

> Nguồn: `README.md` (11 KB, fetched via raw.githubusercontent.com 2026-04-18)
> Repo: `teng-lin/notebooklm-py`

## TL;DR

**notebooklm-py** là **unofficial Python library + CLI + agentic skill** cung cấp programmatic access cho Google NotebookLM, including features mà web UI không expose. Positioning: "automate research workflows, generate content, integrate NotebookLM into broader applications." **Three-surface design** (Python API + CLI + Skill), 11K stars, MIT, active development (v0.3.4, pushed 1 day ago). **Not a Tier 1 agent framework — it's a bridge library** that agents adopt.

## Positioning / framing

- **Tagline:** "A Comprehensive NotebookLM Skill & Unofficial Python API. Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents"
- **Audience:** Developers + researchers + AI agent operators who use NotebookLM
- **Value prop:** Programmatic + CLI + agent access + features beyond web UI
- **Relationship to Google NotebookLM:** Extends, not replaces. Mirrors all official functionality + adds export/automation/agent capabilities.
- **Stability warning:** Unofficial, undocumented Google APIs, subject to breaking changes

## Installation

```bash
pip install notebooklm-py                          # basic
pip install "notebooklm-py[browser]"               # with browser auth
playwright install chromium                        # required for browser flow
pip install git+https://github.com/teng-lin/notebooklm-py@main   # latest unreleased
```

## Three Integration Approaches

1. **Python API** — async programmatic access for custom workflows
2. **CLI** — `notebooklm <command>` for shell scripts/automation
3. **Agent Skill** — bundled SKILL.md for Claude Code, Codex, OpenClaw

→ **Unique architecture choice.** Most siblings offer 1-2 surfaces; notebooklm-py covers 3.

## CLI Command Groups

### Core Operations
- `notebooklm login` — auth (browser-based, supports Chrome + Edge for SSO)
- `notebooklm create "title"` — create notebook
- `notebooklm use <id>` — set context
- `notebooklm list` — list notebooks
- `notebooklm source add "url|path"` — add URL/PDF/YouTube/Drive/text
- `notebooklm ask "question"` — chat query

### Content Generation
- `notebooklm generate audio` — 4 formats × multi-language
- `notebooklm generate video` / `cinematic-video` — preset variations
- `notebooklm generate quiz` / `flashcards` — educational content
- `notebooklm generate slide-deck` / `infographic` / `mind-map` / `data-table` / `report`

### Downloads
- `notebooklm download <type> [path]` — supports MP3/MP4/PDF/PPTX/JSON/CSV/PNG/Markdown/HTML
- `--all` flag for batch downloads

### Utilities
- `auth check --test` — diagnostic validation
- `language list` — 80+ languages
- `metadata --json` — structured notebook export
- `source add-research` — web research with auto-import

## Python API Surface

```python
async with await NotebookLMClient.from_storage() as client:
    nb = await client.notebooks.create("name")
    await client.sources.add_url(nb.id, url, wait=True)
    fulltext = await client.sources.get_fulltext(nb.id, source_id)
    result = await client.chat.ask(nb.id, "question")
    status = await client.artifacts.generate_audio(nb.id, instructions)
    await client.artifacts.wait_for_completion(nb.id, status.task_id)
    await client.artifacts.download_audio(nb.id, filepath)
    await client.sharing.set_sharing_state(nb.id, public=True)
```

**Namespaces:** `notebooks`, `sources`, `artifacts`, `chat`, `sharing` (plus more in SKILL.md)
**Style:** `async with` context manager + `from_storage()` constructor + namespaced methods

## Web UI-Exclusive Features (API/CLI Only)

These = **core differentiation** from just using NotebookLM web:

- **Batch downloads** — multiple artifacts at once
- **Quiz/Flashcard structured export** — JSON, Markdown, HTML (web UI = interactive only)
- **Mind map JSON extraction** — for third-party visualization
- **Slide deck PPTX export** — editable PowerPoint (web UI = PDF only)
- **Individual slide revision** — via natural-language prompt
- **Report template customization** — append custom instructions
- **Chat history persistence** — save Q&A as notebook notes
- **Source content access** — retrieve indexed text programmatically
- **Programmatic permission management** — sharing without UI

→ **Value prop defensible.** If you need any of these, library is the only option.

## Agent Integration

### SKILL.md bundled
Library ships SKILL.md — reusable skill template for agents.

### Installation methods
```bash
notebooklm skill install              # local CLI (populates ~/.claude/skills/notebooklm)
npx skills add teng-lin/notebooklm-py  # npx ecosystem
# OR manual: copy SKILL.md into agent skill directory
```

### Compatible agents named
- **Claude Code** (Anthropic) — primary target
- **Codex** (OpenAI) — compatible
- **OpenClaw** — compatible (unclear what this is; possibly open-source Claude Code alternative?)

→ **Only sibling to explicitly name multiple agent targets.** Most Tier 1 siblings = Claude Code exclusive.

## Authentication & Configuration

- **Browser-based OAuth** via Playwright (Chrome + Microsoft Edge for SSO)
- **Persistent storage** — credentials saved locally; `NotebookLMClient.from_storage()` retrieves
- **Diagnostic tool** — `notebooklm auth check --test`
- **CI/CD alternatives:**
  - `NOTEBOOKLM_AUTH_JSON` env var with `storage_state.json`
  - `NOTEBOOKLM_PROFILE=profile_name`
  - `NOTEBOOKLM_HOME=/path/to/config`

## Version & Stability

- **Python:** 3.10, 3.11, 3.12, 3.13, 3.14 (forward-compat to 3.14, unusual)
- **License:** MIT
- **Current:** v0.3.4 (Mar 12, 2026)
- **Status:** Production-grade maturity (transitioned from v0.1.x beta)
- **Fragility warning:** "Unofficial; undocumented Google APIs subject to breaking changes"
- **Stability policy:** `docs/stability.md`
- **Release checklist:** `docs/releasing.md`

## Comparison to Official NotebookLM

| Axis | Web UI | notebooklm-py |
|------|--------|---------------|
| Core features (create, source, chat, generate) | ✅ | ✅ (mirrors) |
| PPTX export | ❌ (PDF only) | ✅ |
| JSON/CSV artifact export | ❌ | ✅ |
| Batch downloads | ❌ | ✅ |
| Individual slide revision | ❌ | ✅ |
| Mind map JSON extraction | ❌ | ✅ |
| Programmatic sharing | ❌ | ✅ |
| Custom report templates | ❌ | ✅ (via `--append`) |
| Agent integration | ❌ | ✅ |

## Unique positioning vs 6 siblings

| Axis | notebooklm-py | Tier 1 siblings | Tier 2 goclaw | Tier 3 course |
|------|---------------|-----------------|---------------|---------------|
| **Purpose** | Bridge to external service | Dev tool | Platform | Learn concepts |
| **Provides** | Skill library + API + CLI | Agent framework | Multi-tenant platform | Curriculum |
| **Consumer verb** | Integrate | Use | Deploy | Learn |
| **Code relationship to agents** | Library IMPORTED by agent | Agent framework IS | Hosts agents | Teaches about |
| **External dependency** | Google NotebookLM (hard) | None | None | None |

→ **Not comparable on same axis as 6 siblings.** Distinct category = proposed Tier 4.

## Meta-relevance to Storm Bear vault

### Direct
1. **Scrum coaching use case** — transcript of retro → podcast summary → team listens on commute. Library automates.
2. **Source aggregation** — multi-coach knowledge base → consolidated research notebook → team guide
3. **Research → published guide pipeline** — vault's `03 Published/` guides could be generated from NotebookLM sources

### Cross-sibling
1. **Tier 1 ECC/Superpowers/gstack/GSD users** — can all adopt notebooklm-py skill. Library is tier-agnostic consumer library.
2. **Tier 2 goclaw** — multi-tenant deployment could embed notebooklm-py as bundled skill per tenant
3. **Tier 3 course** — Lesson 04 (Tool Use) + Lesson 11 (Agentic Protocols MCP) both conceptually apply to notebooklm-py as a tool/skill agents invoke

### Meta-concept
notebooklm-py demonstrates **"skill as published library"** pattern:
- Skill consumable via CLI install (`notebooklm skill install`)
- Skill consumable via npx (`npx skills add teng-lin/notebooklm-py`)
- **Storm Bear's `05 Skills/llm-wiki-ingest.md`** could be packaged similarly — distribute pattern to wider community

## Signals of quality / trust

- **11,043 stars** — significant validation
- **1-2 week release cadence** — healthy maintenance
- **Semantic versioning** — disciplined
- **Breaking changes documented** — deprecation warnings before removal
- **4-layer architecture** — clean separation (CLAUDE.md confirms)
- **Test strategy** — unit + integration + E2E (AGENTS.md)
- **Pre-commit hooks** — ruff + mypy + pytest
- **Stability policy documented** — sets expectations correctly
- **MIT license** — permissive

## Risks / watchouts

- **Undocumented Google APIs** — can break any day without notice
- **Solo maintainer** — bus factor = 1 (teng-lin handles all RPC reverse engineering)
- **Requires paid NotebookLM plan** — Google's pricing applies (library doesn't provide NotebookLM)
- **Browser auth via Playwright** — adds install footprint (chromium)
- **Rate limiting** — must respect Google's limits; library doesn't protect you
- **OpenClaw unknown** — mentioned but unexplained; suggest due diligence before assuming

## Open questions (→ `01 Analysis/(C) open questions.md`)

1. RPC stability window (historic breakage frequency)
2. OpenClaw relationship clarification
3. Agent isolation enforcement strength
4. Vietnamese content quality via NotebookLM
5. Cross-agent profile collision

## Sources list (for Phase 2 ingestion)

- README.md (this summary) — 11 KB
- SKILL.md — 26 KB (invocation reference)
- CLAUDE.md + CHANGELOG.md + AGENTS.md — cluster summary (architecture + release + agent guidance)

## Cross-references

- Sibling summaries:
  - `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) README summary.md`
  - `../../Superpowers - Beginner Analysis/02 Wiki/(C) README summary.md`
  - `../../gstack - Beginner Analysis/02 Wiki/(C) README summary.md`
  - `../../goclaw - Beginner Analysis/02 Wiki/(C) README summary.md`
  - `../../get-shit-done - Beginner Analysis/02 Wiki/(C) README summary.md`
  - `../../ai-agents-for-beginners - Beginner Analysis/02 Wiki/(C) README summary.md`
