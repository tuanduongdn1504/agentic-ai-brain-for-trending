# (C) Cluster — Core protocols + TutorBot + CLI + 27 providers + Docker

> **Sources:** `deeptutor/core/` protocol files + `deeptutor_cli/` + `Dockerfile` + `docker-compose.yml` + `docker-compose.ghcr.yml` + `docker-compose.dev.yml` + `scripts/start_tour.py` (31.6K) + `scripts/start_web.py` (4.9K) + `.env.example` + `.env.example_CN`.
> **Cluster theme:** Runtime protocol + CLI command surface + multi-provider ecosystem + deployment surfaces.

---

## 1. Core protocol layer — `deeptutor/core/`

**Files + sizes:**

| File | Size | Purpose |
|------|------|---------|
| `__init__.py` | 834B | Package export |
| `capability_protocol.py` | 1.9K | `BaseCapability` + `CapabilityManifest` |
| `context.py` | 1.9K | `UnifiedContext` + `Attachment` |
| `errors.py` | 1.3K | Error hierarchy |
| `stream.py` | 1.9K | `StreamEvent` + `StreamEventType` enum |
| `stream_bus.py` | 6.9K | Event fan-out bus + producer helpers |
| `tool_protocol.py` | 4.0K | `BaseTool` abstract |
| `trace.py` | 2.3K | Trace metadata helpers |

**Design properties:**

- **Abstract protocol separation** — core/ has ONLY protocol + minimal dataclass files; no business logic. Capabilities + Tools + UI all depend on core/ but core/ depends on nothing.
- **Async-first** — all `run()` methods are `async def`; streaming via `async for` subscription.
- **Dataclass manifests** — capabilities declare themselves via `CapabilityManifest(name, description, stages, tools_used, cli_aliases, request_schema, config_defaults)`.
- **Trace metadata helper** (`trace.py`) — `merge_trace_metadata(data, metadata)` — standardizes metadata merging for events.

## 2. Runtime layer — `deeptutor/runtime/`

**Files (from AGENTS.md + directory probe):**

- `orchestrator.py` — **ChatOrchestrator** (unified entry; routes to ChatCapability default or selected deep Capability)
- `registry/tool_registry.py` — **ToolRegistry** (discovery + registration of BaseTool subclasses)
- `registry/capability_registry.py` — **CapabilityRegistry** (discovery + registration of BaseCapability subclasses)
- `mode.py` — **RunMode** enum (`CLI` vs `SERVER`) — distinguishes terminal-interactive vs API-server behavior

**Flow:**
```
Entry (CLI / WS / SDK)
  → ChatOrchestrator
  → routes via active_capability field in UnifiedContext:
    - None → ChatCapability (default; tool-augmented chat)
    - "deep_solve" / "deep_question" / "deep_research" / ... → deep Capability
  → Capability.run(context, stream)
  → Capability invokes Tools from enabled_tools (if set)
  → StreamBus fans events to consumers (CLI renderer / WS pusher / JSON writer)
```

**RunMode distinction (corpus-novel):**

- `CLI` mode: rich terminal rendering (via Rich library)
- `SERVER` mode: WebSocket event emission + REST JSON responses

## 3. CLI entry — `deeptutor_cli/` (Typer-based)

**Entry:** `deeptutor_cli/main.py` (5K) — Typer app with 12 subcommand groups registered.

**File inventory:**

| File | Size | Purpose |
|------|------|---------|
| `main.py` | 5.0K | Typer root app + command-group registration |
| `common.py` | 7.4K | Shared CLI utilities (output formatting / config loading) |
| `chat.py` | 8.7K | `deeptutor chat` REPL + `deeptutor run <capability>` |
| `kb.py` | 10.2K | `deeptutor kb` subcommands (list / info / create / add / search / set-default / delete) |
| `bot.py` | 3.3K | `deeptutor bot` subcommands (list / create / start / stop) |
| `book.py` | 1.9K | `deeptutor book` subcommands (list / health / refresh-fingerprints) |
| `memory.py` | 2.4K | `deeptutor memory` subcommands (show / clear) |
| `session_cmd.py` | 3.3K | `deeptutor session` subcommands (list / show / open / rename / delete) |
| `notebook.py` | 2.4K | `deeptutor notebook` subcommands (list / create / show / add-md / replace-md / remove-record) |
| `config_cmd.py` | 3.1K | `deeptutor config` subcommands (show / ...) |
| `plugin.py` | 2.3K | `deeptutor plugin` subcommands (list / info) |
| `provider_cmd.py` | 2.5K | `deeptutor provider` subcommands (login — OAuth for openai-codex / github-copilot) |

**Top-level commands (3):**

| Command | Description |
|---------|-------------|
| `deeptutor run <capability> <message>` | One-shot capability (chat / deep_solve / deep_question / deep_research / math_animator / visualize) |
| `deeptutor chat` | Interactive REPL |
| `deeptutor serve` | Start API server (FastAPI + uvicorn + WebSocket) |

**12 REPL slash commands** (inside `deeptutor chat`):

| Command | Effect |
|---------|--------|
| `/quit` | Exit |
| `/session` | Show current session id |
| `/new` | Start new session |
| `/tool on\|off <name>` | Toggle tool |
| `/cap <name>` | Switch capability |
| `/kb <name>\|none` | Set or clear KB |
| `/history add <id>` / `/history clear` | Manage history references |
| `/notebook add <ref>` / `/notebook clear` | Manage notebook references |
| `/refs` | Show active references |
| `/config show\|set\|clear` | Manage capability config |
| `/regenerate` / `/retry` | Re-run last user message (v1.2.1 release) |

**`deeptutor run` flags:**
- `--session <id>` — resume existing
- `--tool/-t <name>` — enable tool (repeatable)
- `--kb <name>` — KB (repeatable)
- `--notebook-ref <ref>` — notebook ref (repeatable)
- `--history-ref <id>` — session id (repeatable)
- `--language/-l <code>` — response language (default en)
- `--config <key=value>` — capability config (repeatable)
- `--config-json <json>` — JSON config
- `--format/-f rich|json` — output format (**corpus-first dual-output rich-vs-json CLI at T5**)

## 4. Multi-provider ecosystem — 27 LLM + 7 embedding + 7 search = 41 integrations

### 4.1 LLM providers (27; from README provider table)

| Provider | Binding | Default Base URL |
|----------|---------|------------------|
| AiHubMix | `aihubmix` | `https://aihubmix.com/v1` |
| Anthropic | `anthropic` | `https://api.anthropic.com/v1` |
| Azure OpenAI | `azure_openai` | (deployment-specific) |
| BytePlus | `byteplus` | `ap-southeast.bytepluses.com/api/v3` |
| BytePlus Coding Plan | `byteplus_coding_plan` | `.../api/coding/v3` |
| Custom (OpenAI-compat) | `custom` | (user-defined) |
| DashScope (Qwen) | `dashscope` | `dashscope.aliyuncs.com` |
| DeepSeek | `deepseek` | `api.deepseek.com` |
| Gemini | `gemini` | `generativelanguage.googleapis.com/v1beta/openai/` |
| GitHub Copilot | `github_copilot` | `api.githubcopilot.com` |
| Groq | `groq` | `api.groq.com/openai/v1` |
| llama.cpp | `llama_cpp` | `localhost:8080/v1` |
| LM Studio | `lm_studio` | `localhost:1234/v1` |
| MiniMax | `minimax` | `api.minimax.io/v1` |
| Mistral | `mistral` | `api.mistral.ai/v1` |
| Moonshot (Kimi) | `moonshot` | `api.moonshot.ai/v1` |
| Ollama | `ollama` | `localhost:11434/v1` |
| OpenAI | `openai` | `api.openai.com/v1` |
| **OpenAI Codex** | `openai_codex` | `chatgpt.com/backend-api` |
| OpenRouter | `openrouter` | `openrouter.ai/api/v1` |
| **OpenVINO Model Server** | `ovms` | `localhost:8000/v3` |
| **Qianfan (Ernie Baidu)** | `qianfan` | `qianfan.baidubce.com/v2` |
| SiliconFlow | `siliconflow` | `api.siliconflow.cn/v1` |
| **Step Fun** | `stepfun` | `api.stepfun.com/v1` |
| vLLM | `vllm` | `localhost:8000/v1` |
| VolcEngine | `volcengine` | `ark.cn-beijing.volces.com/api/v3` |
| VolcEngine Coding Plan | `volcengine_coding_plan` | `.../api/coding/v3` |
| **Xiaomi MIMO** | `xiaomi_mimo` | `api.xiaomimimo.com/v1` |
| Zhipu AI (GLM) | `zhipu` | `open.bigmodel.cn/api/paas/v4` |

**Corpus-first providers** (bold in table above): OpenAI Codex + OpenVINO + Qianfan + Step Fun + Xiaomi MIMO — not observed in any prior Storm Bear wiki.

**CN-ecosystem subset (9 providers):** BytePlus / BytePlus Coding / DashScope / DeepSeek / Moonshot / Qianfan / SiliconFlow / Step Fun / VolcEngine / VolcEngine Coding / Xiaomi MIMO / Zhipu = **11 CN bindings** (one of the broadest CN-provider-coverage in corpus; awesome-mcp-servers v31 covered directory-scale). `.env.example_CN` exists as CN-default configuration file.

**Local-model subset (5):** llama.cpp / LM Studio / Ollama / vLLM / OpenVINO — full local-inference stack without cloud dependency (pair with Ollama embedding).

### 4.2 Embedding providers (7)

| Provider | Binding | Default dim |
|----------|---------|-------------|
| OpenAI | `openai` | 3072 (text-embedding-3-large) |
| Azure OpenAI | `azure_openai` | (deployment-specific) |
| Cohere | `cohere` | 1024 (embed-v4.0) |
| Jina | `jina` | 1024 (jina-embeddings-v3) |
| Ollama | `ollama` | 768 (nomic-embed-text) |
| vLLM / LM Studio | `vllm` | variable |
| Custom | `custom` | user-defined |

OpenAI-compatible providers (DashScope / SiliconFlow) accessible via `custom` or `openai` binding.

### 4.3 Web Search providers (7)

| Provider | Env Key | Notes |
|----------|---------|-------|
| Brave | `BRAVE_API_KEY` | **Recommended** — free tier |
| Tavily | `TAVILY_API_KEY` | — |
| Serper | `SERPER_API_KEY` | Google Search via Serper (v1.1.0 release integration) |
| Jina | `JINA_API_KEY` | — |
| SearXNG | — | Self-hosted |
| DuckDuckGo | — | No API key |
| Perplexity | `PERPLEXITY_API_KEY` | Requires API |

**7-provider search stack** = corpus-most diverse search provider coverage at T5; ties with pi-mono v36 + crawl4ai v29 at ~5-7 search providers observed.

## 5. `.env.example` structure

**Required fields (9):**
- `LLM_BINDING` / `LLM_MODEL` / `LLM_API_KEY` / `LLM_HOST`
- `EMBEDDING_BINDING` / `EMBEDDING_MODEL` / `EMBEDDING_API_KEY` / `EMBEDDING_HOST` / `EMBEDDING_DIMENSION`

**Optional fields:**
- `SEARCH_PROVIDER` + `SEARCH_API_KEY`
- `BACKEND_PORT` (default 8001) / `FRONTEND_PORT` (default 3782)
- `NEXT_PUBLIC_API_BASE_EXTERNAL` (public backend URL for cloud deployment)
- `DISABLE_SSL_VERIFY` (default false)

**`.env.example_CN`:** parallel file pre-configured with CN providers as defaults (DeepSeek LLM + DashScope/Zhipu embedding + Jina/Brave search); observed corpus-first **region-specific .env example** (beyond locale-file convention).

## 6. Docker + GHCR multi-arch deployment

**3 compose files:**

### 6.1 `docker-compose.yml` (4.1K) — build-from-source
- Single container (backend + frontend bundled)
- Dockerfile 12.8K (multi-stage build)
- Default ports 8001/3782
- Volume mounts: `/app/data/user` + `/app/data/knowledge_bases`
- `.env` loaded

### 6.2 `docker-compose.ghcr.yml` (3.6K) — pre-built official image
- Pulls `ghcr.io/hkuds/deeptutor:latest` (or `:1.0.0`)
- Built for `linux/amd64` + `linux/arm64` (corpus-first T5 multi-arch GHCR)
- Published on every release (via GitHub Actions)
- Same volumes + ports

### 6.3 `docker-compose.dev.yml` (1.6K) — dev override
- Layers on top of main: `docker compose -f docker-compose.yml -f docker-compose.dev.yml up`
- Mounts source code for hot-reload
- Changes to `deeptutor/`, `deeptutor_cli/`, `scripts/`, `web/` reflect immediately

**Deployment options summary:**

| Option | Surface | Velocity |
|--------|---------|----------|
| A: Setup Tour (`python scripts/start_tour.py`) | Interactive web OR CLI guided | Recommended |
| B: Manual local | pip + npm + .env | Full control |
| C1: Docker GHCR | 1 command pull+run | Fastest for production |
| C2: Docker build-source | 1 command build+run | For customization |
| D: CLI-only | pip `.[cli]` + .env | Minimal install |

## 7. WebSocket API — `deeptutor/api/routers/unified_ws.py`

**Endpoint:** `/api/v1/ws`
- Bidirectional
- Client sends: chat requests + tool toggles + capability switches
- Server streams: `StreamEvent`s via NDJSON frames
- WebSocket heartbeat + auto-reconnect (v1.1.0-beta; corpus-first explicit WS heartbeat at T5)
- LAN remote access fix (v1.2.2 release)

## 8. TutorBot deep-dive — `deeptutor/tutorbot/`

### 8.1 Agent (`agent/`)
- Built on HKUDS/nanobot (40.7K-star sibling)
- Independent agent loop per bot
- Can reach DeepTutor's full toolkit (RAG / code exec / web search / paper search / reason / brainstorm)

### 8.2 Channels (`channels/`) — 8+ integration
- **Telegram**
- **Discord**
- **Slack**
- **Feishu** (Lark-CN)
- **WeChat Work** (企业微信)
- **DingTalk** (钉钉)
- **Email**
- Plus additional per README "and more"

### 8.3 Heartbeat (`heartbeat/`)
- **Proactive initiation system** — *"Bots don't just respond — they initiate."*
- Recurring study check-ins
- Review reminders
- Scheduled tasks
- Implementation: likely cron-based (see `cron/` subdir)

### 8.4 Skills (`skills/`)
- Per-bot skill library
- Add skill files → bot gains abilities
- Scoped to bot instance (not global)

### 8.5 Soul Templates (`templates/`)
- Editable personality + tone + teaching philosophy files
- Built-in archetypes: Socratic / encouraging / rigorous
- User-craftable custom souls
- Injected into chat system prompt when bot active

### 8.6 Session (`session/`)
- Per-bot session isolation
- Independent from main DeepTutor session
- Shared knowledge access via DeepTutor's shared knowledge layer

### 8.7 Providers (`providers/`)
- Per-bot LLM provider choice
- Override main DeepTutor provider
- Bot can use different model from user session (e.g., Socratic bot uses Claude; research bot uses OpenAI)

### 8.8 Config (`config/`)
- Per-bot atomic config writes (v1.1.1 release robustness fix)
- Live-reload friendly

## 9. Knowledge subsystem — `deeptutor/knowledge/`

**Files:**
- `manager.py` (40.4K) — KB CRUD + document indexing (largest single file in package; reflects KB-centric architecture)
- `add_documents.py` (11.7K) — incremental add
- `initializer.py` (11.9K) — KB initialization + schema
- `progress_tracker.py` (7.1K) — upload/index progress (v1.0.0-beta.4 rate-limit retry)

**Document support:**
- PDF / TXT / Markdown
- Incremental add (not re-build from scratch)
- RAG pipeline per KB (v0.5.0 release; flexible pipeline selection per KB)
- MinerU nested output support (v1.0.0-beta.2)
- Docling support for RAG-Anything (v0.5.2 release)
- RAG integration with HKUDS/LightRAG roadmap 🔜

## 10. Capabilities deep-dive — `deeptutor/capabilities/`

**Files + sizes:**

| File | Size | Role |
|------|------|------|
| `__init__.py` | 257B | Exports |
| `_answer_now.py` | 9.2K | Universal "Answer now" interrupt (v1.1.1) |
| `chat.py` | 1000B | ChatCapability (default; minimal) |
| `deep_question.py` | 25.1K | 4-stage quiz generation pipeline |
| `deep_research.py` | 20.8K | Parallel subtopic research + report |
| `deep_solve.py` | 14.4K | 3-stage solver (plan → reason → write) |
| `math_animator.py` | 19.1K | Manim-based animation |
| `request_contracts.py` | 5.1K | Request validation schemas |
| `visualize.py` | 14.9K | SVG/Chart.js/Mermaid/HTML |

**Notable:** `deep_question.py` largest (25.1K) + `deep_research.py` (20.8K) + `math_animator.py` (19.1K) — educational-domain depth reflects T5 education-application archetype.

## 11. Tools deep-dive — `deeptutor/tools/builtin/`

**Files + sizes:**

| File | Size | Role |
|------|------|------|
| `__init__.py` | 1.6K | Registry |
| `brainstorm.py` | 3.0K | Breadth-first idea exploration |
| `code_executor.py` | 16.2K | Sandboxed Python exec |
| `paper_search_tool.py` | 5.9K | arXiv search |
| `rag_tool.py` | 4.3K | RAG retrieval |
| `reason.py` | 4.0K | Deep-reasoning LLM call |
| `tex_chunker.py` | 11.2K | TeX document chunking |
| `tex_downloader.py` | 7.7K | arXiv TeX download |
| `web_search.py` | 1.6K | Web search abstraction |

**Notable:** `code_executor.py` largest (16.2K) — sandboxing + security logic + result handling dominates tool-layer code. `tex_chunker` + `tex_downloader` = academic-paper-processing infrastructure (T5 academic-research tier signal).

**`geogebra_analysis` tool** (4-stage vision pipeline from AGENTS.md) — not in `tools/builtin/`; likely in `deeptutor/tools/` subdirs (`prompting/` `question/` `vision/`). Image → GeoGebra command conversion for math tutoring.

## 12. API layer — `deeptutor/api/`

**Structure:**
- FastAPI app + routers
- WebSocket router (`unified_ws.py`)
- REST endpoints for session / KB / memory CRUD
- `deeptutor.api.run_server` entry module (per README Option B manual install)

**Schema-driven Channels tab (v1.1.2 release):** bot configuration via schema (secret masking + UI form generation).

## 13. Pattern Library signals from this cluster

| Signal | Pattern | Direction |
|--------|---------|-----------|
| 27 LLM providers | #28 Multi-Provider AI Support | **Corpus-most** — strengthens (abstraction-library v0.4.0 → native-SDK-routing v1.0.0-beta.3 architectural shift documented) |
| Native OpenAI/Anthropic SDK (no litellm) | #28 sub-variant | Counter-evidence to #28 "LiteLLM-abstraction sub-variant" — DeepTutor chose native routing at provider count 27 |
| GHCR multi-arch amd64+arm64 | #2 Distribution Evolution | Strengthens T5 (corpus-first explicit amd64+arm64 T5) |
| RAG pipeline per-KB selectability | N/A | Novel; not pattern-eligible |
| TutorBot 8+ channel connectors | N/A | Novel multi-channel delivery; not pattern-eligible |
| Local-model stack (llama.cpp + LM Studio + Ollama + vLLM + OpenVINO) | #28 + local-inference sub-variant | Observational |
| MinerU + Docling PDF-processing integration | N/A | Domain-specific; not pattern-eligible |
| arXiv TeX-downloader + chunker | #42 / academic-lab-signal | Academic-lab archetype signal; not pattern |
| NDJSON dual-output (rich for humans + JSON for agents) | N/A | Corpus-first T5 dual-CLI-output |

**Cluster summary complete.** All 3 clusters now document the 12-axis classification. Next: 4 entity pages.
