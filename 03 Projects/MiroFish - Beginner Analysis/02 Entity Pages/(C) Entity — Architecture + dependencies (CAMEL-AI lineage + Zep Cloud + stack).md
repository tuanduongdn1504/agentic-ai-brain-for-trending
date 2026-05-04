# (C) Entity — Architecture + dependencies (CAMEL-AI / OASIS lineage + Zep Cloud + stack)

**Linked entities**: Core product / BaiFu+Shanda / Storm Bear meta

---

## High-level architecture

```
                        ┌──────────────────────────────────┐
                        │         User Browser             │
                        │   (localhost:3000 — Vue 3 SPA)   │
                        └───────────────┬──────────────────┘
                                        │ HTTP / axios
                                        ▼
        ┌───────────────────────────────────────────────────────────┐
        │  Flask backend (port 5001) — `npm run dev` orchestrated   │
        │                                                            │
        │  3 blueprints under /api/{graph,simulation,report}        │
        │  • api/graph.py        20 KB  → Stage 1                   │
        │  • api/simulation.py   94 KB  → Stages 2-3-5              │
        │  • api/report.py       30 KB  → Stages 4-5                │
        │                                                            │
        │  13 services in app/services/                              │
        │  • graph_builder + ontology_generator                     │
        │  • oasis_profile_generator + simulation_config_generator  │
        │  • simulation_runner + simulation_manager + simulation_ipc│
        │  • report_agent (99 KB)                                   │
        │  • zep_entity_reader + zep_graph_memory_updater           │
        │  • zep_tools (66 KB)                                      │
        │  • text_processor                                          │
        │                                                            │
        │  Utils: file_parser + llm_client + locale + logger +      │
        │         retry + zep_paging                                 │
        └────┬────────────────────────────┬─────────────────┬───────┘
             │ HTTPS                      │ HTTPS           │ IPC
             ▼                            ▼                 ▼
     ┌──────────────────┐   ┌──────────────────────┐  ┌────────────────────────┐
     │   Zep Cloud      │   │  LLM API             │  │ OASIS sim subprocess   │
     │   (paid SaaS)    │   │  (Qwen / OpenAI /    │  │ run_twitter_sim.py     │
     │   memory graph   │   │   any OpenAI-SDK)    │  │ run_reddit_sim.py      │
     │                  │   │                      │  │ run_parallel_sim.py    │
     │   3.13.0 pinned  │   │  default Qwen-plus   │  │                        │
     │                  │   │  via Bailian         │  │ camel-oasis 0.2.5      │
     │                  │   │                      │  │ camel-ai 0.2.78        │
     └──────────────────┘   └──────────────────────┘  └────────────────────────┘
```

---

## Dependency lineage analysis

### CAMEL-AI / OASIS — methodology + library lineage (CORPUS-FIRST)

**README acknowledgment**:
> *"MiroFish's simulation engine is powered by **OASIS (Open Agent Social Interaction Simulations)**, We sincerely thank the CAMEL-AI team for their open-source contributions!"*

**Backend `pyproject.toml`** confirms:
```toml
"camel-oasis==0.2.5",   # OASIS multi-agent social simulation library
"camel-ai==0.2.78",     # CAMEL-AI base multi-agent framework
```

**About CAMEL-AI** (verified from public sources, not fabricated):
- Open-source AI research collective focused on multi-agent communication and society simulation
- Founded around 2023; affiliated with academic AI research circles in CN
- Releases include CAMEL framework + OASIS (Open Agent Social Interaction Simulations) + AGI research
- GitHub: `camel-ai/camel` + `camel-ai/oasis`

**Significance for Storm Bear corpus**:
- This is the **first explicit CAMEL-AI / OASIS lineage citation** in 49 wikis
- Pattern #19 archetype 2 methodology-lineage currently has 4 nodes: Karpathy (individual) + John Lam (individual) + Anthropic-team-cluster + Lance Martin (individual)
- CAMEL-AI is a **research-organization-cluster** node candidate — distinct from individual nodes
- **Decision per consolidation-forward discipline**: do NOT register as 5th node at N=1; document as observational sub-node within Pattern #19 archetype 2; promote at N=2 if a 2nd corpus wiki cites CAMEL-AI explicitly

### Zep Cloud — managed memory infrastructure (T5 corpus-first)

**Pinned**: `zep-cloud==3.13.0` (one of 3 hard-pinned deps)

**About Zep Cloud**: managed memory-graph SaaS for LLM applications. Provides entity extraction, knowledge graph storage, fact retrieval, temporal knowledge tracking. Free tier sufficient for "simple usage" per README; paid tiers for production.

**4 dedicated services** treat Zep as first-class:
- `services/zep_entity_reader.py` (15 KB) — read entities from Zep graph
- `services/zep_graph_memory_updater.py` (22 KB) — write / update entities in Zep graph
- `services/zep_tools.py` (66 KB) — toolset wrapper around Zep API for ReportAgent (LLM tool-call interface)
- `utils/zep_paging.py` (4.5 KB) — pagination helper for Zep API

**Architectural trade-off**:
- ✅ Pro: no DB to host, no embedding pipeline, fast time-to-MVP, scales horizontally on Zep's side
- ❌ Con: vendor lock-in, recurring cost, network round-trip latency, data residency questions for sensitive use cases (financial / political prediction)

**Comparison to corpus T5 alternatives**:
- rowboat v43 — local IndexedDB (browser-side; no cloud)
- browser-use v41 — local file system
- OpenHands v30 — Docker volumes
- DeepTutor v38 — own multi-tier memory (Summary + Profile + cross-channel local)
- shannon v45 — Workspaces + git checkpoints
- Skyvern v24 — own session storage

MiroFish is **first T5 in corpus to use managed-cloud-memory-as-dependency**. Architectural choice = simplicity-over-control.

### LLM provider abstraction (Pattern #28 internal-env-switch sub-variant)

**Primary LLM** (3 env vars):
```env
LLM_API_KEY=...
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus
```

**Accelerator LLM** (3 optional env vars from `.env.example`):
```env
LLM_BOOST_API_KEY=...
LLM_BOOST_BASE_URL=...
LLM_BOOST_MODEL_NAME=...
```

**README explicit**: *"supports any LLM API with OpenAI SDK format. Recommended: Alibaba Qwen-plus model via Bailian Platform."*

**OpenAI SDK format compatibility** = de-facto industry-standard interface. MiroFish doesn't implement provider-specific routing logic; it relies on OpenAI SDK's `base_url` parameter to point at any compatible endpoint (Qwen via Bailian, Claude via proxy, OpenAI direct, Anthropic via proxy, OpenRouter, local Ollama, etc.).

**N-th data point for Pattern #28**: 12+ corpus data points; this is internal-env-switch sub-variant (per v40 formalization). Not native-multi-provider-routing; not abstraction-library (no LiteLLM); not native-SDK-routing.

---

## Frontend stack

| Component | Version | Role |
|-----------|---------|------|
| Vue | 3.5.24 | SPA framework (Composition API era) |
| Vite | 7.2.4 | Build tool + dev server |
| @vitejs/plugin-vue | 6.0.1 | Vite ↔ Vue adapter |
| vue-i18n | 11.3.0 | Runtime localization |
| vue-router | 4.6.3 | SPA routing |
| axios | 1.14 | HTTP client |
| **D3 7.9** | — | Visualization (knowledge graph + simulation results) |

**ESM-only** (`"type": "module"` in `package.json`).

**Corpus-first**: Vue 3 at T5. Prior T5 frontends were React/Next.js dominant. CN-author + CN-corporate-incubation context aligns with Vue dominance in CN ecosystem (Alibaba, Tencent, ByteDance heavy Vue users).

**D3 first-class** observation: D3 is the de-facto knowledge-graph + custom-visualization library. Required for rendering simulation outputs (entity graphs, agent interaction networks, temporal trajectories). Indicates frontend invests in **rich visualization** rather than pre-built charting (Chart.js / Recharts).

---

## Multi-process architecture

Flask main process spawns simulation subprocesses via IPC:
- `services/simulation_ipc.py` (12 KB) — IPC protocol implementation
- `services/simulation_runner.py` (69 KB) — orchestrates subprocess lifecycle
- `services/simulation_manager.py` (20 KB) — high-level simulation lifecycle (start/stop/status)
- `backend/scripts/run_twitter_simulation.py` + `run_reddit_simulation.py` + `run_parallel_simulation.py` — actual subprocess entry points

Cleanup hook at app startup:
```python
# app/__init__.py
from .services.simulation_runner import SimulationRunner
SimulationRunner.register_cleanup()
```

→ Flask shutdown terminates all live simulation subprocesses (avoids orphaned processes).

**Architectural significance**: long-running simulations (10-40+ rounds × N agents × M actions × LLM API calls) are CPU/network heavy and would block Flask's request-handler. Subprocess isolation = standard production pattern for batch ML/LLM workloads. **GREEN-tier deferral**: exact IPC protocol + parallel-run vs sequential-run decisions not extracted in v49; flagged for future deep-dive wiki if pattern observation calls for it.

---

## Build + distribution

### Build
- **Backend**: `hatchling` build backend, wheel target `app` package, version 0.1.0
- **Frontend**: Vite build via `npm run build`
- **Root orchestration**: `concurrently` (only root devDep) for parallel backend + frontend dev servers

### Distribution
- **Source clone** (primary): `git clone github.com/666ghj/MiroFish` + `npm run setup:all`
- **Docker** (secondary): `docker compose up -d` pulls `ghcr.io/666ghj/mirofish:latest`
- **CN mirror**: `ghcr.nju.edu.cn/666ghj/mirofish:latest` (Nanjing University CDN-mirror) cited as comment for faster CN pull
- **No PyPI / no npm publish** — clone-only at 57K stars (T5 norm; matches deer-flow / Skyvern / OpenHands / DeepTutor T5 distribution patterns)

### Single CI workflow
`.github/workflows/docker-image.yml`:
- Triggers: tag push (`tags: ["*"]`) + manual dispatch (`workflow_dispatch`)
- Builds + pushes Docker image to GHCR
- Multi-arch capable (QEMU + Buildx setup) but no platforms specified → defaults to host arch
- **No test workflow, no lint workflow, no security scan workflow** — light-minimal CI consistent with light-minimal-governance

---

## Architectural choices summary

| Choice | Trade-off |
|--------|-----------|
| Flask + Python (not FastAPI / Django / Node backend) | Familiar / fast iteration ↔ no async-first by default; multi-process for concurrency |
| Vue 3 + Vite (not React / Next.js) | CN-ecosystem default; modern Composition API ↔ smaller English-speaking community than React |
| D3 (not Chart.js / Recharts / vis.js) | Custom visualization power ↔ steeper learning curve |
| CAMEL-AI / OASIS (not LangChain agents / AutoGen / custom) | Research-grade multi-agent simulation ↔ research velocity; pinned versions = upstream stability concern |
| Zep Cloud managed memory (not self-hosted vector DB) | Operational simplicity ↔ vendor lock-in + cost |
| OpenAI SDK format vendor-agnostic (not LiteLLM / direct multi-provider) | Standard industry interface ↔ no native fallback / cost-routing logic |
| Hard-coded Twitter + Reddit sim platforms | Simplicity ↔ extension friction |
| Subprocess IPC for simulation (not async tasks / Celery / RQ) | Process isolation ↔ IPC complexity |
| GHCR Docker distribution (not Docker Hub) | Owned by GitHub-Microsoft; CN mirror handles geographic friction |
| Light-minimal governance (no AGENTS.md / CONTRIBUTING / SECURITY) | Solo-velocity ↔ contributor onboarding friction |

---

## Observable risks (unhardened areas)

1. **CORS open to `*`** in `app/__init__.py` — fine for dev, security risk in production
2. **Default `SECRET_KEY = 'mirofish-secret-key'`** — development-grade; production deployment must override via env
3. **`FLASK_DEBUG=True` default** — same; production must override
4. **Dockerfile runs `npm run dev`** in container — dev-mode-as-deployment; not production-hardened
5. **No test suite** beyond `backend/scripts/test_profile_format.py` (single file)
6. **No CI security scanning** — Dependabot / CodeQL / Bandit absent
7. **No SECURITY.md** — vulnerability disclosure path unclear
8. **3 hard-pinned deps** (`zep-cloud` / `camel-oasis` / `camel-ai`) — security-update friction; intentional pinning suggests upstream-API-stability concerns

These risks are **observable, not necessarily blocking**, depending on deployment context. Pre-monetization product velocity often defers production hardening; v0.1.2 + 5-month age + 57K stars = product-traction validation phase, hardening expected later.

---

## Cross-references

- **Core product entity**: 5-stage workflow + use cases + corpus-first observations
- **BaiFu + Shanda + BUPT entity**: human + organizational context
- **Storm Bear meta (38th)**: indirect lessons for vault
- **Phase 4b deliverable**: T5 10-way comparison + Pattern #29 / #19 / #44 / #31 / #50 / #28 / #18 / #22 strengthening
