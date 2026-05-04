# (C) Cluster — AGENTS.md + SKILL.md + CONTRIBUTING.md + 2-layer plugin architecture

> **Sources:** `AGENTS.md` (149 lines) + `SKILL.md` (148 lines) + `CONTRIBUTING.md` (220 lines) + `pyproject.toml` (275 lines) + `.pre-commit-config.yaml` + `deeptutor/README.md` (5.6K; package-level architecture) + `deeptutor/core/` protocol files.
> **Cluster theme:** Architecture + contributor surface + governance discipline.

---

## 1. AGENTS.md — architecture documentation (not just rules file)

**Size:** 149 lines — **rich architecture doc**, not minimum-viable pointer (contrast v37 bizos 327B minimum or corporate standards). Medium-weight AGENTS.md for Storm Bear corpus observations.

**Structure:**
1. Overview (agent-native + 2-layer plugin model + 3 entry points)
2. Architecture diagram (ASCII: Entry → ChatOrchestrator → {ToolRegistry Level 1, CapabilityRegistry Level 2})
3. Level 1 Tools table (7 tools enumerated)
4. Level 2 Capabilities table (3 capabilities enumerated — chat / deep_solve / deep_question)
5. Playground Plugins (deep_research)
6. CLI Usage (pip install + run commands + REPL + kb + plugins + memory + serve)
7. Key Files (13 paths enumerated)
8. Plugin Development (directory structure + manifest.yaml + capability.py minimal example)
9. Dependency Layers (4 layers: cli / server / math-animator / dev)

**Novel for corpus:**
- **2-layer plugin model** (Tools L1 = single-function LLM-invoked; Capabilities L2 = multi-step agent pipelines taking over conversation) — **corpus-first explicit 2-layer declaration**
- Plugin Development section gives complete minimal plugin source (manifest.yaml + capability.py 5-line `run()` method) — contributor-friendly; lower barrier to entry than most T5 entrants
- `RunMode (CLI vs SERVER)` runtime mode abstraction — novel for corpus

## 2. SKILL.md — bilateral agent-skill convention (CORPUS-FIRST)

**Size:** 148 lines.

**Name/positioning verbatim:** `# DeepTutor CLI Skill` + `> Teach your AI agent to configure, manage, and use DeepTutor — an intelligent learning platform — entirely through the command line.`

**CORPUS-FIRST BILATERAL PATTERN:**

DeepTutor simultaneously:
1. **Runs agents internally** (TutorBots + Capabilities = 2-layer agent pipelines powered by HKUDS/nanobot)
2. **Exposes SKILL.md for external agents** — any tool-using LLM (nanobot / Claude / ChatGPT-with-tools / Codex) can read SKILL.md and autonomously operate DeepTutor via CLI

This bilateral dual-role (runtime-for-own-agents + skill-for-external-agents) is **corpus-first** — no prior Storm Bear wiki documented a framework that is both agent-host AND agent-driven-tool.

**Contrast with prior SKILL/AGENTS.md conventions:**
- v16 graphify `SKILL.md` exposes graphify to Claude Code/Cursor/etc. — but graphify itself is NOT an agent runtime (consumed-only)
- v30 OpenHands is agent runtime — but no external-facing SKILL.md convention observed
- v36 pi-mono is agent runtime (pi-coding-agent CLI) — no external SKILL.md
- DeepTutor uniquely: agent-runtime (TutorBot nanobot-powered) **+** external-facing SKILL.md → 2-way

**SKILL.md structure (12 sections):**
1. When to Use (7 use cases)
2. Prerequisites (Python 3.11+ + pip install + start_tour.py)
3. Chat & Capabilities (deeptutor chat + run commands + 8 CLI flags)
4. Knowledge Bases (7 `deeptutor kb` commands)
5. TutorBot (4 `deeptutor bot` commands)
6. Memory (2 `deeptutor memory` commands)
7. Sessions (5 `deeptutor session` commands)
8. Notebooks (6 `deeptutor notebook` commands)
9. System (6 commands: config / plugin / provider / serve)
10. REPL Slash Commands (12 `/` commands: `/quit` `/session` `/new` `/tool` `/cap` `/kb` `/history` `/notebook` `/refs` `/config` `/regenerate` `/retry`)
11. Typical Workflows (4 example workflows)
12. Build-a-KB-from-documents + Quiz-generation example

**Integration partners explicit:** nanobot (primary) + "any LLM with tool access" (general).

## 3. CONTRIBUTING.md — governance + discipline

**Size:** 220 lines.

**Key structural facts:**
- **Sole named maintainer**: `@pancacake` ("Currently just me!") — solo-maintainer signal despite HKUDS lab + 48 GitHub contributors. Relevant for Pattern #12 Governance-Depth archetype classification.
- **Branching model** (not main-push):
  - `dev` — general development (target for PRs)
  - `multi-user` — multi-user / multi-tenant feature branch (experimental)
  - `main` — production (no direct PRs)
- Quick Start: Fork → Clone → Sync → Feature branch → Develop → pre-commit → PR to `dev`/`multi-user`

**Pre-commit + CI stack (7 tools — extensive for academic-lab):**

| Tool | Purpose |
|------|---------|
| **Ruff** | Python linting + formatting |
| **Prettier** | Frontend + config file formatting |
| **detect-secrets** | Hardcoded secret scanning |
| **pip-audit** | Dependency vulnerability scanning |
| **Bandit** | Security issue analysis |
| **MyPy** | Static type checking |
| **Interrogate** | Docstring coverage reporting |

*"Local pre-commit hooks may only show warnings, but CI will perform strict checks and automatically reject PRs that fail."*

**Coding standards:**
- Python type hints required for all function signatures
- f-strings preferred
- PEP 8 (enforced by Ruff)
- Small + focused functions (max-complexity 10 via ruff.mccabe)
- Google Python Style docstrings required for new modules/classes/public functions

**Commit Message Format (Conventional Commits):**
`feat` / `fix` / `docs` / `style` / `refactor` / `test` / `chore`

**Security Best Practices:**
- File Upload: 100 MB general / 50 MB PDF / multi-layer validation (extension + MIME + content-sanitization) / path-traversal sanitization
- Development: `shell=False` subprocess / `pathlib.Path` / LF line endings via `.gitattributes`

## 4. pyproject.toml — packaging + dependency strategy

### 4.1 Base dependencies (required)
```
python-dotenv, PyYAML, jinja2, openai (>=1.30), tiktoken, aiohttp, httpx, requests, ddgs,
nest_asyncio, tenacity, pydantic, pydantic-settings, aiosqlite, typer[all], rich, prompt_toolkit
```

**Note: `openai>=1.30.0` is base dependency** (native OpenAI SDK; litellm was dropped v1.0.0-beta.3 on 2026-04-08).

### 4.2 Optional-dependencies (4 extras groups)

| Group | Packages |
|-------|----------|
| **anthropic** | `anthropic>=0.30.0` |
| **dashscope** | `dashscope>=1.14.0` |
| **search** | `perplexityai>=0.1.0` |
| **oauth** | `oauth-cli-kit>=0.1.1` (Python 3.11+) |
| **server** | `fastapi>=0.100.0`, `uvicorn[standard]>=0.24.0`, `websockets>=12.0`, `python-multipart>=0.0.6` |
| **math-animator** | `manim>=0.19.0` |
| **all** | anthropic + dashscope + perplexityai + oauth-cli-kit + server + math-animator |

### 4.3 Entry point
```
deeptutor = "deeptutor_cli.main:main"
```
(Typer-based; see SKILL.md for command reference.)

### 4.4 Tool configurations (Black + Ruff + pytest + MyPy + Bandit)
- Black: line-length 100; target py311/py312
- Ruff: line-length 100; target py311; relaxed rule set (E/F/I core + B006; many ignores documented)
- Ruff isort: first-party `deeptutor`/`deeptutor_cli`/`scripts`
- pytest: `testpaths = ["tests"]` + strict-markers + asyncio fixture loop = function
- MyPy: 3.11; relaxed (`warn_return_any = false` + `disallow_untyped_defs = false`); tests/tools modules error-ignore (dynamic imports)
- Bandit: skips B101/B311/B403/B404/B110/B104/B112/B105/B301/B501/B603/B202 with explicit justifications

**Observation on governance maturity:** 7-tool pre-commit stack + documented Bandit skip-with-rationale + per-module MyPy overrides = **academic-lab with commercial-quality discipline** — heavier than typical solo/community academic project; lighter than Microsoft corporate standard (no CLA).

## 5. deeptutor/ package architecture (from deeptutor/README.md 5.6K)

**Package structure:**
```
deeptutor/
  agents/        # ChatAgent + Deep* agents (multi-step orchestration)
  api/           # FastAPI WebSocket + REST endpoints
  app/           # App lifecycle + bootstrap
  book/          # Book Engine (14 block types; compiler.py 12.3K + engine.py 43.1K)
  capabilities/  # 4 built-in capabilities (chat + deep_solve + deep_question + deep_research) + 3 playground (math_animator, visualize, _answer_now)
  co_writer/     # Multi-document AI-collaborative writing (edit_agent.py 11.1K + storage.py 8K)
  config/        # Config management
  core/          # Protocol layer: BaseTool, BaseCapability, UnifiedContext, StreamBus, StreamEvent, trace, errors
  events/        # Event types + stream protocol
  knowledge/     # KB manager (40.4K) + add_documents + initializer + progress_tracker
  logging/       # Log config
  runtime/       # ChatOrchestrator + ToolRegistry + CapabilityRegistry + RunMode (CLI vs SERVER)
  services/      # Shared services
  tools/         # Level-1 tools (builtin/)
  tutorbot/      # Persistent autonomous tutors (agent + bus + channels + config + cron + heartbeat + providers + session + skills + templates + utils)
  utils/         # Shared utilities
deeptutor_cli/   # Typer CLI entry (main.py 5K + 11 subcommand files: chat / kb / bot / book / config_cmd / memory / notebook / plugin / provider_cmd / session_cmd + common.py shared + __main__.py)
```

## 6. TutorBot subsystem (corpus-novel)

**Directory:** `deeptutor/tutorbot/` — 11 subdirectories:

| Subdir | Purpose |
|--------|---------|
| `agent/` | nanobot-powered agent loop |
| `bus/` | Event bus |
| `channels/` | **Multi-channel connectors** (Telegram / Discord / Slack / Feishu / WeChat Work / DingTalk / Email / more) |
| `config/` | Per-bot config |
| `cron/` | Scheduled task execution |
| `heartbeat/` | **Proactive initiation system** (recurring study check-ins / review reminders / scheduled tasks) |
| `providers/` | LLM provider adapters |
| `session/` | Per-bot session isolation |
| `skills/` | Per-bot skill library (teach new abilities by adding skill files) |
| `templates/` | **Soul Templates** (personality + tone + teaching philosophy editable files; built-in archetypes Socratic / encouraging / rigorous + custom) |
| `utils/` | Shared utils |

**Novel concepts:**
- **Soul Template** — editable personality + teaching philosophy (not prompt template; declared as file archetype)
- **Heartbeat** — proactive initiation; *"Bots don't just respond — they initiate. Your tutor shows up even when you don't."*
- **Multi-Channel Presence** — 7+ connectors (corpus-first T5 multi-channel-bot delivery)
- **Skill Learning** — per-bot skill library; add skill files → bot gains abilities (mirrors Claude Code skill convention at bot-instance scope)
- **Team & Sub-Agents** — *"Spawn background sub-agents or orchestrate multi-agent teams within a single bot for complex, long-running tasks."*

## 7. Book Engine subsystem (corpus-novel)

**Directory:** `deeptutor/book/` — files:
- `compiler.py` (12.3K) — block compilation pipeline
- `engine.py` (43.1K) — multi-agent orchestrator
- `inputs.py` (13K) — KB reference inputs
- `kb_health.py` (11K) — KB drift + fingerprint tracking
- `models.py` (17.9K) — block type data models
- `storage.py` (10.6K) — persistence
- `streaming.py` (3.8K) — progress streaming
- `agents/`, `blocks/`, `prompts/` subdirs

**Pipeline (from README):**
1. Propose outline (multi-agent)
2. Retrieve relevant sources from KB
3. Synthesize chapter tree
4. Plan each page
5. Compile every block (1 of 14 types)
6. Real-time progress timeline streams to UI

**14 block types:**
text / callout / quiz / flash cards / code / figure / deep dive / animation / interactive demo / timeline / concept graph / section / user note / placeholder

**CLI sub-surface:**
- `deeptutor book list`
- `deeptutor book health <book_id>`
- `deeptutor book refresh-fingerprints <book_id>`

**KB fingerprint + drift detection** (`kb_health.py`): novel for corpus — detects when underlying KB docs change and stale Book pages need rebuild.

## 8. Co-Writer subsystem (corpus-novel)

**Directory:** `deeptutor/co_writer/` — files:
- `edit_agent.py` (11.1K) — AI edit agent (Rewrite / Expand / Shorten ops)
- `storage.py` (8K) — multi-document persistence

**Features:**
- Multi-document Markdown workspace (not single scratchpad)
- Select-text → Rewrite / Expand / Shorten with KB or web context
- Full undo/redo non-destructive
- Save-to-notebook integration

## 9. 2-Layer plugin model (core architecture signature)

### Level 1 — Tools (BaseTool abstract, `deeptutor/core/tool_protocol.py`)

**7 tools (from AGENTS.md):**

| Tool | Description |
|------|-------------|
| `rag` | Knowledge base retrieval (RAG) |
| `web_search` | Web search with citations |
| `code_execution` | Sandboxed Python execution |
| `reason` | Dedicated deep-reasoning LLM call |
| `brainstorm` | Breadth-first idea exploration with rationale |
| `paper_search` | arXiv academic paper search |
| `geogebra_analysis` | Image → GeoGebra commands (4-stage vision pipeline) |

**Character:** single-function; LLM invokes on demand; no multi-step workflow.

### Level 2 — Capabilities (BaseCapability abstract, `deeptutor/core/capability_protocol.py`)

**Manifest dataclass:**
```python
@dataclass
class CapabilityManifest:
    name: str
    description: str
    stages: list[str]
    tools_used: list[str]
    cli_aliases: list[str]
    request_schema: dict
    config_defaults: dict
```

**4 built-in capabilities (README/AGENTS):**

| Capability | Stages (verbatim from AGENTS.md) |
|------------|-----------------------------------|
| `chat` | responding (default; tool-augmented) |
| `deep_solve` | planning → reasoning → writing |
| `deep_question` | ideation → evaluation → generation → validation |

**Additional capabilities inferred from `deeptutor/capabilities/` directory:**
- `deep_research.py` (20.8K) — decompose + parallel subtopic research + cited report
- `math_animator.py` (19.1K) — Manim-based math animation
- `visualize.py` (14.9K) — SVG/Chart.js/Mermaid/HTML generation
- `_answer_now.py` (9.2K) — universal "Answer now" interrupt (v1.1.1 release)

**Character:** multi-step agent pipelines; take over the conversation; stream events; emit `stage_start`/`stage_end` boundaries.

### Plugin Discovery (`deeptutor/plugins/loader.py`)

**Directory convention** (AGENTS.md §8):
```
deeptutor/plugins/<name>/
  manifest.yaml   # name, version, type, description, stages
  capability.py   # class extending BaseCapability
```

**Minimum plugin:**
```yaml
name: my_plugin
version: 0.1.0
type: playground
description: "My custom plugin"
stages: [step1, step2]
```
+ capability.py with `async def run(self, context, stream) -> None:` implementation.

## 10. UnifiedContext + StreamBus event protocol

### UnifiedContext (`deeptutor/core/context.py`)

**Single data object flows through orchestrator → tool/capability/plugin:**

```python
@dataclass
class UnifiedContext:
    session_id: str
    user_message: str
    conversation_history: list[dict]  # OpenAI format
    enabled_tools: list[str] | None   # None=not-specified; []=explicitly-disable-all
    active_capability: str | None
    knowledge_bases: list[str]
    attachments: list[Attachment]     # type in {image, file, pdf}
    config_overrides: dict
    language: str = "en"              # "en" | "zh" (UI + response)
    notebook_context: str
    history_context: str
    memory_context: str
    skills_context: str
    metadata: dict
```

**i18n observation:** `language` field only supports `"en" | "zh"` at context-level. UI-level i18n is EN+zh via explicit type hint — documented VN operator impact: VN would require new `"vi"` binding (minor PR).

### StreamBus (`deeptutor/core/stream_bus.py` 6.9K)

**Event-driven fan-out architecture:**

```python
class StreamBus:
    # Producer: bus.emit(StreamEvent)
    # Consumer: async for event in bus.subscribe()
    # Async context manager: async with bus.stage("planning") as s: ...
```

**Event types (via StreamEventType):**
- `STAGE_START` / `STAGE_END` — capability stage boundaries
- `CONTENT` — streaming response text
- `THINKING` — chain-of-thought visibility
- `OBSERVATION` — agent observations (tool results processed by agent)
- `TOOL_CALL` / `TOOL_RESULT` — tool invocations
- `PROGRESS` — numerical progress (current/total)
- `SOURCES` — citation sources (RAG + paper + web)
- `RESULT` — final result payload
- `ERROR` — error events

**NDJSON serialization:** `StreamBus.event_to_json(event)` → single-line JSON. **Dual-consumer (CLI renderer + WebSocket pusher + JSON writer) from single producer.**

**Corpus observation:** event-driven async fan-out is conventional; novelty is **NDJSON agent-consumable output mode** enabling SKILL.md-bilateral pattern (external agent reads structured events).

## 11. Cross-cluster integration table

| Feature | Primary cluster | Secondary references |
|---------|-----------------|----------------------|
| 2-layer plugin model | This (AGENTS+Architecture) | Technical cluster (protocol files) |
| TutorBot | This (AGENTS architecture) + Technical | — |
| Book Engine 14 blocks | User-facing cluster | This (directory layout) |
| Co-Writer | User-facing cluster | This (directory layout) |
| SKILL.md bilateral | This (SKILL.md) | Technical cluster (CLI + Typer) |
| 27 LLM providers | User-facing cluster | Technical cluster (`.env.example` + providers/) |
| Multi-channel bot | User-facing cluster | This (tutorbot/channels/) + Technical |
| Persistent memory (Summary + Profile) | User-facing cluster | — |
| Pre-commit 7-tool stack | This (CONTRIBUTING.md) | — |

## 12. Governance depth quantification (Pattern #12 data)

| Metric | Value | Archetype fit |
|--------|-------|---------------|
| Total governance files | 5 (README + AGENTS + SKILL + CONTRIBUTING + LICENSE) | Medium |
| CoC file | **Absent** | Lighter than Microsoft corporate |
| SECURITY.md dedicated | **Absent** (Security best practices inline in CONTRIBUTING §7) | Lighter than Microsoft |
| Branching model | `main`/`dev`/`multi-user` 3-branch | Medium-heavy |
| Pre-commit tool count | 7 | Heavy (commercial-quality) |
| Type checking | Relaxed MyPy | Medium |
| CLA required | **No** | Lighter than Microsoft |
| Named maintainer | `@pancacake` solo in CONTRIBUTING.md despite 48 GH contributors | Solo-signal |
| Communication channels | Discord + Feishu + WeChat + GitHub Discussions | Heavy (CN+EN dual) |

**Classification:** **Medium governance at academic-lab archetype** — heavier than solo community (codymaster v12) but lighter than corporate Microsoft (markitdown v28). Consistent with Pattern #12 "governance-depth correlates with organization archetype."

## 13. Pattern Library signals from this cluster

| Signal | Pattern | Direction |
|--------|---------|-----------|
| 2-layer plugin model (Tools L1 + Capabilities L2) | N/A | Corpus-first architecture; no registration |
| SKILL.md bilateral (agent-host + external-skill) | N/A | Corpus-first observation; no registration |
| 7-tool pre-commit at academic lab | #12 Governance-Depth | Strengthens (academic-lab archetype classification) |
| 149-line AGENTS.md | #22 AGENTS.md Industry Standard | Medium adoption data point (between v36 182-line max and v37 327B min) |
| Typer-based CLI | N/A | Python-ecosystem-standard; not pattern-eligible |
| NDJSON event stream | N/A | Corpus-first dual-consumer; not pattern-eligible |

**Cluster summary complete.** Next cluster: `(C) Cluster — Core protocols + TutorBot + CLI + 27 providers + Docker.md` covers runtime + deployment detail.
