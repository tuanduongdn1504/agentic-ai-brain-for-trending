# (C) TutorBot + CLI + bilateral SKILL.md + nanobot ecosystem

> **Entity:** DeepTutor agent-runtime (TutorBot + Capabilities) + CLI + SKILL.md bilateral dual-role + nanobot lineage
> **Corpus-first observation:** DeepTutor is simultaneously an agent-HOST (runs TutorBots + Capabilities) AND an agent-TOOL (exposes SKILL.md + structured NDJSON events for external agents) — dual-role.
> **Cluster sources:** All 3 cluster summaries; primarily AGENTS+Architecture + Core-protocols+TutorBot+CLI clusters.

---

## 1. The bilateral observation (corpus-first)

**Claim:** DeepTutor is the first Storm Bear corpus entrant to simultaneously:

1. **Run agents internally** — TutorBots (persistent multi-instance autonomous agents; nanobot-powered) + Capabilities (multi-step pipelines)
2. **Expose own surface as agent-skill externally** — SKILL.md (148 lines) teaches any tool-using agent (nanobot / Claude Code / Codex / any LLM-with-tool-access) to configure + operate DeepTutor autonomously

**Why novel:**
- v16 graphify: exposes SKILL.md for external consumption but NOT an agent runtime itself (single-direction: consumed-only)
- v30 OpenHands: agent runtime but NO documented external-facing SKILL.md convention
- v36 pi-mono: agent runtime (pi-coding-agent CLI) + pi-skills for Claude Code consumption — approximates bilateral BUT pi-skills is separate repo, not same-repo bilateral
- **DeepTutor:** same repo + same installation + agent-runtime AND agent-skill

**Implication:** establishes a corpus observation class for "agent-dual-role-frameworks." Not registered as pattern (N=1 + conceptually spans existing Pattern #2 Distribution Evolution + Pattern #18 Agent Runtime Standardization territories); if N=2 emerges (another clean bilateral), could justify Pattern #76 candidate registration in future audit.

## 2. TutorBot — persistent autonomous tutors

### 2.1 What it is

Verbatim README: *"TutorBot is not a chatbot — it is a **persistent, multi-instance agent** built on [nanobot](https://github.com/HKUDS/nanobot). Each TutorBot runs its own agent loop with independent workspace, memory, and personality. Create a Socratic math tutor, a patient writing coach, and a rigorous research advisor — all running simultaneously, each evolving with you."*

### 2.2 Architecture (`deeptutor/tutorbot/` — 11 subdirectories)

| Subdir | Purpose |
|--------|---------|
| `agent/` | nanobot-powered agent loop |
| `bus/` | Event bus (per-bot) |
| `channels/` | 8+ connectors (Telegram / Discord / Slack / Feishu / WeChat Work / DingTalk / Email / more) |
| `config/` | Per-bot config (atomic writes v1.1.1) |
| `cron/` | Scheduled tasks |
| `heartbeat/` | Proactive initiation (recurring check-ins / reminders / scheduled tasks) |
| `providers/` | Per-bot LLM provider (can differ from user session) |
| `session/` | Per-bot session isolation |
| `skills/` | Per-bot skill library (add files → new abilities) |
| `templates/` | **Soul Templates** (personality / tone / teaching philosophy; built-in Socratic / encouraging / rigorous + custom) |
| `utils/` | Shared utils |

### 2.3 Novel concepts

| Concept | Novelty |
|---------|---------|
| **Soul Template** | Editable personality file type (distinct from prompt template); corpus-first explicit personality-as-file archetype |
| **Heartbeat proactive initiation** | Bot initiates, not just responds; *"Your tutor shows up even when you don't."* |
| **Multi-Channel Presence** | 8+ chat platforms (Telegram + Discord + Slack + Feishu + WeChat Work + DingTalk + Email + more); corpus-first T5 multi-channel-bot-delivery |
| **Skill Learning** | Per-bot skill library file-based; mirrors Claude Code skill convention at per-bot scope (novel scoping) |
| **Team & Sub-Agents** | *"Spawn background sub-agents or orchestrate multi-agent teams within a single bot for complex, long-running tasks."* |
| **Per-bot provider override** | Each bot can use different LLM (Socratic=Claude / research=OpenAI); cross-provider fleet economics |
| **Shared knowledge access** | Each bot isolated session BUT accesses shared DeepTutor knowledge layer — isolated identity + shared knowledge architecture |

### 2.4 CLI

```bash
deeptutor bot create math-tutor --persona "Socratic math teacher who uses probing questions"
deeptutor bot create writing-coach --persona "Patient, detail-oriented writing mentor"
deeptutor bot list
deeptutor bot start <id>
deeptutor bot stop <id>
```

**Flags:** `--name "My Tutor"` / `--persona "..."` / `--model <provider>`.

## 3. CLI entry — Typer-based, 15 command families, 12 REPL slash commands

### 3.1 Top-level

| Command | Purpose |
|---------|---------|
| `deeptutor run <capability> <message>` | One-shot (chat / deep_solve / deep_question / deep_research / math_animator / visualize) |
| `deeptutor chat` | REPL |
| `deeptutor serve` | FastAPI + WebSocket API server |

### 3.2 Command families (subcommand groups)

| Family | Subcommands |
|--------|-------------|
| **`bot`** | list / create / start / stop |
| **`kb`** | list / info / create / add / search / set-default / delete |
| **`book`** | list / health / refresh-fingerprints |
| **`memory`** | show / clear (args: summary \| profile \| all) |
| **`session`** | list / show / open / rename / delete |
| **`notebook`** | list / create / show / add-md / replace-md / remove-record |
| **`config`** | show |
| **`plugin`** | list / info |
| **`provider`** | login (openai-codex OAuth / github-copilot validate) |

**Total:** ~40+ distinct subcommands (across 12 families + 3 top-level).

### 3.3 REPL slash commands (12)

| Command | Effect |
|---------|--------|
| `/quit` | Exit REPL |
| `/session` | Show session id |
| `/new` | New session |
| `/tool on\|off <name>` | Toggle tool (7 available) |
| `/cap <name>` | Switch capability (4+ built-in + plugins) |
| `/kb <name>\|none` | Set/clear KB |
| `/history add <id>` / `/history clear` | History refs |
| `/notebook add <ref>` / `/notebook clear` | Notebook refs |
| `/refs` | Show active refs |
| `/config show\|set\|clear` | Capability config |
| `/regenerate` / `/retry` | Re-run last user message (v1.2.1) |

### 3.4 Dual-output format (corpus-first T5)

```bash
deeptutor run chat "Summarize chapter 3" -f rich   # Colored formatted (humans)
deeptutor run chat "Summarize chapter 3" -f json   # NDJSON events (agents/pipelines)
```

**NDJSON consumer:** external agents read line-delimited StreamEvent JSON (type + source + stage + content + metadata) → structured parsing without terminal-ANSI stripping.

### 3.5 Session continuity

```bash
deeptutor session list        # All sessions
deeptutor session open <id>   # Resume REPL
```

URL-based bookmarkable sessions (v1.1.0-beta release) enable browser-shareable session links.

## 4. SKILL.md — the external-facing contract (148 lines)

### 4.1 Positioning verbatim

`> Teach your AI agent to configure, manage, and use DeepTutor — an intelligent learning platform — entirely through the command line.`

### 4.2 Structure (12 sections)

1. **When to Use** (7 use cases: setup / chat / run capability / manage KB / manage TutorBot / view memory / start API server)
2. **Prerequisites** (Python 3.11+ + pip + `start_tour.py` first-time setup)
3. **Chat & Capabilities** — REPL + one-shot + 8 CLI flags
4. **Knowledge Bases** — 7 commands
5. **TutorBot** — 4 commands
6. **Memory** — 2 commands
7. **Sessions** — 5 commands
8. **Notebooks** — 6 commands
9. **System** — 6 commands (config / plugin / provider / serve)
10. **REPL Slash Commands** — 12 `/` commands
11. **Typical Workflows** — 4 example workflows
12. **Build-a-KB-from-documents + Quiz-generation example**

### 4.3 Integration partners (explicit)

- **Primary:** HKUDS/nanobot (40.7K-star sibling ultra-lightweight agent engine) — DeepTutor CLI is skill-consumable by nanobot
- **General:** *"any LLM with tool access"* — Claude-with-tool-use / ChatGPT-with-tools / Codex / Gemini with function-calling

### 4.4 What this enables

- **Autonomous agent operation** — external agent reads SKILL.md → learns DeepTutor CLI grammar → autonomously sets up LLM + embedding + search providers via `deeptutor config` / `deeptutor provider login` → creates KB via `deeptutor kb create` → runs capabilities via `deeptutor run` → reads NDJSON events via `-f json`
- **Scriptable + composable** — DeepTutor slots into larger agent workflow (another agent drives DeepTutor as a sub-capability)
- **Education-workflow automation** — agent-level automation of "upload my PDFs → generate quiz + Book + research" pipelines

## 5. nanobot — the powering sibling (HKUDS 40.7K stars)

### 5.1 Relationship

From README.md footer: *"[nanobot](https://github.com/HKUDS/nanobot) — Ultra-lightweight agent engine powering TutorBot"*.

**Questions (see Open Questions file):**
- Did nanobot predate DeepTutor? Or was nanobot extracted from DeepTutor's agent subsystem into standalone?
- Both MIT vs Apache-2.0 (nanobot MIT; DeepTutor Apache-2.0) — why different licenses from same lab?

### 5.2 Implication for ecosystem

- HKUDS publishes BOTH the foundation agent engine (nanobot) AND the consumer application (DeepTutor) — **vertical integration within academic-lab ecosystem-portfolio**
- nanobot at 40.7K > DeepTutor at 21.2K — **powering primitive has greater community pull than application** (interesting inversion; typically application > primitive)
- Combined with LightRAG (34.2K RAG backbone; integration roadmap 🔜), HKUDS controls agent engine + RAG + education application = tightly-coupled stack

### 5.3 Other HKUDS dependencies

| Dependency | Source | Role |
|-----------|--------|------|
| **nanobot** | HKUDS (MIT, 40.7K) | TutorBot agent engine |
| **LightRAG** | HKUDS (MIT, 34.2K; EMNLP 2025 paper) | Roadmap integration 🔜 |
| **LlamaIndex** | run-llama (Apache-2.0) | RAG pipeline + document indexing |
| **ManimCat** | Wing900 (not HKUDS) | AI-driven math animation for Math Animator |

**HKUDS self-dependency fraction:** 2 of 4 major dependencies are HKUDS (50%) = **notable vertical integration**.

## 6. The Capabilities layer — 4 built-in + 3 extended + plugins

### 6.1 Built-in Capabilities (from AGENTS.md + capabilities/)

| Capability | Size | Stages |
|-----------|------|--------|
| `chat` | 1K | responding (default) |
| `deep_solve` | 14.4K | planning → reasoning → writing |
| `deep_question` | 25.1K | ideation → evaluation → generation → validation (largest) |
| `deep_research` | 20.8K | decompose → parallel-research → cited-report |

### 6.2 Extended Capabilities

| Capability | Size | Role |
|-----------|------|------|
| `math_animator` | 19.1K | Manim storyboard + render |
| `visualize` | 14.9K | SVG / Chart.js / Mermaid / HTML |
| `_answer_now` | 9.2K | Universal "Answer now" interrupt (v1.1.1) |

### 6.3 Plugin development

```
deeptutor/plugins/<name>/
  manifest.yaml   # name, version, type, description, stages, tools_used, cli_aliases
  capability.py   # class extending BaseCapability with async def run()
```

**5-line minimum `run()` method** — low barrier-to-entry. External contributors can add Capability without modifying core.

## 7. Tools layer — 7 built-in + extensible

| Tool | Size | Role |
|------|------|------|
| `rag_tool` | 4.3K | KB retrieval |
| `web_search` | 1.6K | Web with 7 providers (Brave / Tavily / Serper / Jina / SearXNG / DuckDuckGo / Perplexity) |
| `code_executor` | 16.2K | Sandboxed Python (largest; sandboxing + security logic) |
| `reason` | 4.0K | Dedicated deep-reasoning LLM call |
| `brainstorm` | 3.0K | Breadth-first exploration |
| `paper_search_tool` | 5.9K | arXiv search |
| `geogebra_analysis` | n/a | 4-stage vision → GeoGebra commands (math-tutoring specialist) |

**Plus academic infrastructure:** `tex_chunker.py` (11.2K) + `tex_downloader.py` (7.7K) — arXiv TeX processing (T5 academic-research signal).

## 8. UnifiedContext + StreamBus — the runtime substrate

### 8.1 UnifiedContext

Single data object flowing through all entry surfaces:
- session_id
- user_message
- conversation_history (OpenAI format)
- enabled_tools (None=default / []=disable-all)
- active_capability (None=ChatCapability default)
- knowledge_bases
- attachments (image / file / pdf)
- config_overrides
- language ("en" | "zh")
- notebook_context / history_context / memory_context / skills_context
- metadata (catch-all)

### 8.2 StreamBus — async fan-out event bus

- Producer: tools + capabilities emit StreamEvent
- Consumer: CLI renderer / WebSocket pusher / JSON writer (multiple subscribers)
- Event types: STAGE_START / STAGE_END / CONTENT / THINKING / OBSERVATION / TOOL_CALL / TOOL_RESULT / PROGRESS / SOURCES / RESULT / ERROR
- Async context manager: `async with bus.stage("planning"): ...`
- NDJSON serialization for agent consumption

## 9. Book Engine + Co-Writer integration (see core entity for full detail)

Both leverage:
- Capability layer (deep agent pipelines per block / per edit op)
- Tool layer (RAG + web + code execution + brainstorm for content generation)
- StreamBus progress streaming (real-time compilation timeline / editing progress)
- Memory + KB integration

## 10. Unique scale observation — primitive breadth vs depth

**Breadth:** 4 entry surfaces × 7 tools × 4+ capabilities × 14 Book blocks × 8+ bot channels × 12 REPL slashes × 27 LLM providers = **multiplicatively huge user-facing surface area**.

**Depth:** Largest single file is `book/engine.py` (43.1K) — multi-agent Book compilation orchestration is the architectural centerpiece. `knowledge/manager.py` (40.4K) — KB is the data-gravity center. `deep_question.py` (25.1K) — quiz generation pipeline.

**Implication for Primitive-count:** DeepTutor's ~120-150 primitives surface = **3rd YELLOW** in corpus (after v36 pi-mono + v37 bizos). Scope-compression applied per Phase 0.9: 4-entity allocation + citation-not-replication for provider-enumeration + lossy-compression of per-block / per-channel details.

## 11. Corpus-first observations (TutorBot + CLI + SKILL)

| # | First |
|---|-------|
| 1 | Bilateral runtime-and-skill (agent-HOST and agent-TOOL in same repo) |
| 2 | Persistent-autonomous-tutor-bot architecture (proactive Heartbeat at T5) |
| 3 | Soul Template personality-as-file archetype |
| 4 | 8+ multi-channel bot delivery at T5 |
| 5 | Per-bot LLM provider override (cross-provider fleet economics within single deployment) |
| 6 | `deeptutor run` dual `-f rich\|json` output at T5 |
| 7 | URL-based bookmarkable sessions (v1.1.0-beta) at T5 |
| 8 | Per-bot skill library file-based (mirrors Claude Code at instance scope) |
| 9 | HKUDS vertical integration (nanobot + LightRAG + DeepTutor self-dependency 50%) |
| 10 | 4-stage vision pipeline for `geogebra_analysis` (math-tutoring specialist tool) |

## 12. Cross-wiki siblings

- **v16 graphify** — SKILL.md-consumed-only; DeepTutor is SKILL.md-exposed-WHILE-being-agent-runtime (bilateral extension)
- **v36 pi-mono** — pi-skills companion repo for Claude Code consumption; DeepTutor bilateral is within single repo (tighter coupling)
- **v24 Skyvern** — T5 commercial browser-agent with LLM provider abstraction (8+ providers); DeepTutor extends to 27 providers with NATIVE SDK (native after v1.0.0-beta.3 vs Skyvern's abstraction)
- **v14 paperclip** — T5 community-platform multi-agent orchestrator; paperclip has 4 skills vs DeepTutor's user-authored Skills + 19-agent taxonomy-style TutorBot personas (different scale approach)
- **v27 oh-my-claudecode** — 4-runtime orchestration (Claude+Codex+Gemini+Cursor); DeepTutor has 27-provider internal routing (higher provider count, single runtime)

## 13. Open questions (see full file)

- How does nanobot relate to DeepTutor historically (predecessor / extraction / parallel)?
- Are HKUDS repos coordinated in release cadence or independent-parallel?
- VN UI i18n PR: which files need VN translation? How accepting is `@pancacake` of non-EN-non-zh i18n PRs?

---

*This entity deep-dives agent-runtime + CLI + bilateral-skill architecture. See `(C) DeepTutor core product — agent-native personalized tutoring.md` for product-level overview, `(C) HKUDS ecosystem-portfolio + academic-lab Pattern 44 N=3.md` for organizational archetype, and `(C) Storm Bear Vault — DeepTutor as education-application T5 peer.md` for operator relevance.*
