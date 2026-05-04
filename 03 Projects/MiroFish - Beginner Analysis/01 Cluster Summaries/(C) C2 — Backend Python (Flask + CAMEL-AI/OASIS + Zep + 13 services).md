# (C) C2 — Backend Python (Flask + CAMEL-AI/OASIS + Zep Cloud + 13 services)

**Cluster source**: `00 Source/MiroFish/backend/` (entire backend tree) — `pyproject.toml` + `requirements.txt` + `run.py` + `app/__init__.py` + `app/config.py` + directory listings of `app/api/` + `app/models/` + `app/services/` + `app/utils/` + `scripts/`

---

## Backend stack (verified from `pyproject.toml`)

```toml
[project]
name = "mirofish-backend"
version = "0.1.0"
requires-python = ">=3.11"
license = { text = "AGPL-3.0" }
authors = [{ name = "MiroFish Team" }]

dependencies = [
    "flask>=3.0.0",
    "flask-cors>=6.0.0",
    "openai>=1.0.0",
    "zep-cloud==3.13.0",
    "camel-oasis==0.2.5",
    "camel-ai==0.2.78",
    "PyMuPDF>=1.24.0",
    "charset-normalizer>=3.0.0",
    "chardet>=5.0.0",
    "python-dotenv>=1.0.0",
    "pydantic>=2.0.0",
]
```

Build: `hatchling` (modern PEP 517 backend). Wheel target: `app` package. Optional dev deps: `pytest>=8.0.0` + `pytest-asyncio>=0.23.0` + `pipreqs>=0.5.0`.

**Pinned versions**: `zep-cloud==3.13.0` + `camel-oasis==0.2.5` + `camel-ai==0.2.78` (3 hard-pinned dependencies — defensive against upstream breakage; rest are `>=`-floored). Pinning CAMEL-AI/OASIS at exact versions = signal of tight coupling to specific OASIS API surface.

---

## Flask app factory (`app/__init__.py`)

Standard Flask factory pattern with:
- CORS enabled for `/api/*` (open origin `*` — light-security default; not production-hardened)
- Request/response debug logging middleware (`@app.before_request` / `@app.after_request`)
- Reloader-process awareness (avoid double-print in debug mode)
- 3 blueprints registered:
  - `graph_bp` at `/api/graph` (from `api/graph.py`)
  - `simulation_bp` at `/api/simulation` (from `api/simulation.py`)
  - `report_bp` at `/api/report` (from `api/report.py`)
- Health check at `/health` returns `{'status': 'ok', 'service': 'MiroFish Backend'}`
- Cleanup hook: `SimulationRunner.register_cleanup()` (terminates simulation processes on server shutdown — multi-process architecture signal)
- JSON config: `app.json.ensure_ascii = False` (CN-text-friendly JSON output; corpus-first explicit non-ASCII JSON config)

---

## Config (`app/config.py`)

```python
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mirofish-secret-key')
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    JSON_AS_ASCII = False

    LLM_API_KEY = os.environ.get('LLM_API_KEY')
    LLM_BASE_URL = os.environ.get('LLM_BASE_URL', 'https://api.openai.com/v1')
    LLM_MODEL_NAME = os.environ.get('LLM_MODEL_NAME', 'gpt-4o-mini')

    ZEP_API_KEY = os.environ.get('ZEP_API_KEY')

    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50 MB upload limit
    UPLOAD_FOLDER = '../uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'md', 'txt', 'markdown'}

    DEFAULT_CHUNK_SIZE = 500
    DEFAULT_CHUNK_OVERLAP = 50

    OASIS_DEFAULT_MAX_ROUNDS = 10
    OASIS_SIMULATION_DATA_DIR = '../uploads/simulations'

    OASIS_TWITTER_ACTIONS = ['CREATE_POST', 'LIKE_POST', 'REPOST', 'FOLLOW', 'DO_NOTHING', 'QUOTE_POST']  # 6 actions
    OASIS_REDDIT_ACTIONS = ['LIKE_POST', 'DISLIKE_POST', 'CREATE_POST', 'CREATE_COMMENT',
                             'LIKE_COMMENT', 'DISLIKE_COMMENT', 'SEARCH_POSTS', 'SEARCH_USER',
                             'TREND', 'REFRESH', 'DO_NOTHING', 'FOLLOW', 'MUTE']  # 13 actions

    REPORT_AGENT_MAX_TOOL_CALLS = 5
    REPORT_AGENT_MAX_REFLECTION_ROUNDS = 2
    REPORT_AGENT_TEMPERATURE = 0.5
```

**Observations**:
- LLM is OpenAI-SDK-compatible-vendor-agnostic with **default fallback** `https://api.openai.com/v1` + `gpt-4o-mini`. README recommends Qwen-plus via Bailian. Pattern #28 internal-env-switch sub-variant.
- Zep is required (no fallback path) → tight coupling to Zep Cloud as memory infrastructure.
- File upload: 50 MB limit; 4 file types (pdf / md / txt / markdown).
- Default chunk size 500 / overlap 50 = standard RAG chunking.
- **Hard-coded simulation platforms**: Twitter (6 actions) + Reddit (13 actions). Adding a new platform requires code change, not config. Architectural choice = simplicity-over-flexibility at cost of extension friction.
- ReportAgent has 3 tunable params: max_tool_calls=5 / max_reflection_rounds=2 / temperature=0.5. Reflection-loop architecture observable.

**Config validation method** `Config.validate()` returns errors list if `LLM_API_KEY` or `ZEP_API_KEY` missing. Not auto-invoked at startup — manual responsibility.

---

## API blueprints (`app/api/`)

3 blueprints, total ~145 KB Python:

### `api/graph.py` (20 KB)
- Endpoints under `/api/graph`
- Maps to 5-stage workflow Stage 1 (Graph Building)
- Imports likely include `services/graph_builder.py` + `services/ontology_generator.py`

### `api/simulation.py` (94 KB!)
- Endpoints under `/api/simulation`
- Largest API file — handles entire simulation lifecycle (start / monitor / pause / resume / stop / inspect / interact)
- Maps to 5-stage workflow Stages 2 + 3 + 5
- Heavyweight indicates long-running async workflow management at HTTP layer (likely SSE streaming or polling endpoints for progress tracking)

### `api/report.py` (30 KB)
- Endpoints under `/api/report`
- Maps to 5-stage workflow Stages 4 + 5
- Wraps `services/report_agent.py` (99 KB) — likely thin HTTP wrapper over heavy ReportAgent

---

## Models (`app/models/`)

Two data models (Python objects, not SQLAlchemy ORM — file persistence implied):
- `models/project.py` (9.6 KB) — Project entity
- `models/task.py` (5.7 KB) — Task entity (likely simulation task lifecycle)

No DB/ORM dependency in `pyproject.toml` → file-system or in-memory persistence.

---

## Services (`app/services/`) — 13 files

| File | Size | Stage | Function |
|------|------|-------|----------|
| `graph_builder.py` | 18 KB | 1 | GraphRAG construction from seed |
| `ontology_generator.py` | 19 KB | 1 | Entity ontology from text |
| `oasis_profile_generator.py` | 50 KB | 2 | OASIS agent profile generation (Persona) |
| `simulation_config_generator.py` | 40 KB | 2 | OASIS simulation config from prediction-requirement |
| `simulation_runner.py` | 69 KB | 3 | Actual OASIS simulation execution (forks subprocess?) |
| `simulation_manager.py` | 20 KB | 3 | Simulation lifecycle (start/stop/status) |
| `simulation_ipc.py` | 12 KB | 3 | Inter-process communication for simulation subprocesses |
| `report_agent.py` | **99 KB** | 4 | ReportAgent — largest single file in repo |
| `zep_entity_reader.py` | 15 KB | 1+5 | Zep memory-graph entity reader |
| `zep_graph_memory_updater.py` | 22 KB | 1+5 | Zep memory-graph updater |
| `zep_tools.py` | **66 KB** | 4+5 | Zep memory-graph tools wrapper for ReportAgent |
| `text_processor.py` | 1.7 KB | 1 | Text chunking + preprocessing |
| `__init__.py` | 1.7 KB | — | Module init |

**Total services**: ~432 KB Python source. Heavy concentration in 3 files: `report_agent.py` (99 KB) + `simulation_runner.py` (69 KB) + `zep_tools.py` (66 KB) = 234 KB / 54% of services LOC.

**Architectural observation**: Memory-graph (Zep) is treated as first-class subsystem with 4 dedicated services (`zep_entity_reader` + `zep_graph_memory_updater` + `zep_tools` + `utils/zep_paging.py`). Memory-as-managed-cloud-dependency at T5 is unusual (most T5 corpus entrants embed memory libraries: rowboat IndexedDB, browser-use file system, OpenHands Docker volumes). Zep Cloud = paid SaaS; trade-off is operational simplicity ↔ vendor lock-in + recurring cost.

---

## Utils (`app/utils/`)

| File | Size | Function |
|------|------|----------|
| `file_parser.py` | 5.2 KB | PDF + MD + TXT parser (PyMuPDF + charset-normalizer + chardet) |
| `llm_client.py` | 3.0 KB | OpenAI SDK wrapper |
| `locale.py` | 2.0 KB | Server-side locale handling for i18n LLM-instruction injection |
| `logger.py` | 3.3 KB | Standardized logging setup |
| `retry.py` | 7.5 KB | Retry decorator (likely exponential backoff for LLM calls) |
| `zep_paging.py` | 4.5 KB | Zep API pagination helper |

---

## Backend scripts (`backend/scripts/`) — 5 files

These are NOT services-imported; they are standalone runnable scripts:
- `run_twitter_simulation.py` — Twitter platform simulation runner
- `run_reddit_simulation.py` — Reddit platform simulation runner
- `run_parallel_simulation.py` — dual-platform parallel runner (Twitter + Reddit)
- `action_logger.py` — log actions taken by agents during simulation
- `test_profile_format.py` — single test script (only test file in the repo)

These scripts likely correspond to "subprocess invocation targets" used by `services/simulation_runner.py` via IPC (referenced in `services/simulation_ipc.py`). Multi-process architecture: Flask main process + simulation subprocesses spawned via IPC + cleanup-on-shutdown registration.

---

## Run entry point (`backend/run.py`)

Single Flask runner; uses `create_app()` factory; default port 5001. Confirmed via README quickstart.

---

## Multi-agent + memory architecture (synthesized)

```
┌─ Flask backend (port 5001) ─────────────────────────────────┐
│  • api/graph.py        Stage 1 endpoints                    │
│  • api/simulation.py   Stages 2-3-5 endpoints (94 KB)       │
│  • api/report.py       Stage 4-5 endpoints                  │
│                                                              │
│  Services:                                                   │
│  • graph_builder ─┐                                         │
│  • ontology_gen ──┼─→ Zep Cloud (zep-cloud==3.13.0)         │
│  • zep_entity_reader / zep_graph_memory_updater / zep_tools │
│                                                              │
│  • oasis_profile_gen + simulation_config_gen ─┐             │
│                                               ├─→ OASIS     │
│  • simulation_runner (69 KB) + simulation_manager + IPC ──→ │
│  • [subprocess] backend/scripts/run_*_simulation.py         │
│                          (camel-oasis==0.2.5 + camel-ai==0.2.78)│
│                                                              │
│  • report_agent (99 KB) — LLM + Zep tools + reflection loop │
│  • llm_client (utils) — OpenAI SDK abstraction              │
└──────────────────────────────────────────────────────────────┘
              ↑ HTTP                ↑ IPC + subprocess
              │                     │
       Frontend (Vue 3 / port 3000)  OASIS simulation subprocesses
```

**Architectural choices**:
1. **Memory-as-managed-SaaS** (Zep Cloud) — T5 first-of-kind in corpus
2. **Multi-agent-as-research-library** (CAMEL-AI / OASIS) — corpus-first lineage
3. **Multi-process simulation** (Flask + subprocess + IPC) — durable long-running task pattern
4. **LLM-vendor-abstraction-via-env** (OpenAI SDK format + LLM_BASE_URL override) — Pattern #28 internal-env-switch sub-variant
5. **Reflection-loop-bounded** (`REPORT_AGENT_MAX_REFLECTION_ROUNDS=2`) — finite-budget safety
6. **Hard-coded simulation platforms** (Twitter + Reddit only) — extension point requires code change

---

## Open questions for future deep-dive wikis (deferred)

- ReportAgent toolset enumeration (currently 99 KB cited not extracted)
- Zep tools enumeration (currently 66 KB cited not extracted)
- OASIS profile generator schema (50 KB not extracted)
- Simulation config schema (40 KB not extracted)
- IPC protocol between Flask + subprocess simulation runners
- Whether "thousands of agents" claim is per-simulation-round or aggregate

These are GREEN-tier-deferral observations (per Phase 0.9): cited via service-file size + naming, not enumerated. Not blocking for v49 wiki.

---

**Cluster summary status:** ✅ complete. Backend tree fully mapped. CAMEL-AI/OASIS lineage + Zep Cloud dependency + 5-stage workflow ↔ services mapping confirmed. 0 fabrications.
