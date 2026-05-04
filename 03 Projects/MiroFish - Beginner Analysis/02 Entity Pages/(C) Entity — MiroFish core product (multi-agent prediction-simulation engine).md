# (C) Entity — MiroFish core product (multi-agent prediction-simulation engine)

**Tier**: T5 Agent-as-application — 10th T5 entrant + multi-agent prediction-simulation sub-archetype CORPUS-FIRST
**License**: AGPL-3.0
**Stars**: 57,307 (~5 months old; sustained ~11.5K/month community-viral)
**Repo**: `666ghj/MiroFish`
**Homepage**: https://mirofish.ai
**Live demo**: https://666ghj.github.io/mirofish-demo/

---

## What it is

MiroFish is a **multi-agent prediction engine** that turns a small "seed" of real-world information (news, policy draft, financial signal, novel chapters) into a high-fidelity **digital sandbox** populated by autonomous agents with personalities, memory, and behavior, then runs **social simulations** on **simulated Twitter + Reddit platforms** to deduce future trajectories. After simulation, a **ReportAgent** synthesizes findings + lets the user **chat with any agent** in the simulated world.

**Verbatim positioning from README**:
> *"rehearse the future in a digital sandbox, and win decisions after countless simulations"*
> *"Predict anything"*

**Verified architecture** (from source code, not just README):
- **Backend**: Flask 3.0 + Python 3.11-3.12, deps include `camel-oasis==0.2.5` + `camel-ai==0.2.78` (multi-agent simulation libraries) + `zep-cloud==3.13.0` (memory graph SaaS) + `openai>=1.0.0` (vendor-agnostic LLM)
- **Frontend**: Vue 3.5 + Vite 7 + D3 7.9 + vue-i18n 11 + vue-router 4
- **Multi-process**: Flask main process + simulation subprocesses spawned via IPC (`services/simulation_ipc.py`); cleanup-on-shutdown registered in `app/__init__.py`

---

## 5-stage workflow ↔ source code mapping

| Stage | What it does | Source files |
|-------|-------------|--------------|
| **1. Graph Building** | Extract seed info → build knowledge graph; inject individual + collective memory | `services/graph_builder.py` (18 KB) + `services/ontology_generator.py` (19 KB) + `services/zep_graph_memory_updater.py` (22 KB) + `services/text_processor.py` |
| **2. Environment Setup** | Extract entity relationships → generate personas → inject agent configs into OASIS | `services/oasis_profile_generator.py` (50 KB) + `services/simulation_config_generator.py` (40 KB) |
| **3. Simulation** | Run dual-platform parallel sim (Twitter + Reddit); auto-parse prediction requirements; dynamic temporal memory updates | `services/simulation_runner.py` (69 KB) + `services/simulation_manager.py` (20 KB) + `services/simulation_ipc.py` (12 KB) + `backend/scripts/run_twitter_simulation.py` + `run_reddit_simulation.py` + `run_parallel_simulation.py` |
| **4. Report Generation** | ReportAgent uses rich toolset to interact with post-simulation environment + generate report | `services/report_agent.py` (**99 KB** — largest file in repo) + `services/zep_tools.py` (66 KB) |
| **5. Deep Interaction** | Chat with any agent in simulated world + interact with ReportAgent | `api/report.py` (30 KB) + `api/simulation.py` (94 KB) |

The 5-stage workflow is **mirrored verbatim in the file structure** — useful pedagogy for learners reading source.

---

## OASIS simulation config (verified from `app/config.py`)

**Hard-coded simulation platforms**: Twitter + Reddit only. Adding a new platform requires code changes (not config). Trade-off: simplicity over flexibility.

**Twitter actions** (6):
`CREATE_POST` / `LIKE_POST` / `REPOST` / `FOLLOW` / `DO_NOTHING` / `QUOTE_POST`

**Reddit actions** (13):
`LIKE_POST` / `DISLIKE_POST` / `CREATE_POST` / `CREATE_COMMENT` / `LIKE_COMMENT` / `DISLIKE_COMMENT` / `SEARCH_POSTS` / `SEARCH_USER` / `TREND` / `REFRESH` / `DO_NOTHING` / `FOLLOW` / `MUTE`

Reddit has **2.2× more action types** than Twitter (13 vs 6) — reflects platform behavioral diversity (commenting, voting, search, mute).

**Default rounds**: 10 (env-tunable via `OASIS_DEFAULT_MAX_ROUNDS`). README explicitly warns: *"High consumption — try simulations with fewer than 40 rounds first."* — economic reality (LLM API cost) baked into product positioning.

**ReportAgent params**:
- `REPORT_AGENT_MAX_TOOL_CALLS = 5`
- `REPORT_AGENT_MAX_REFLECTION_ROUNDS = 2` (reflection-loop bounded)
- `REPORT_AGENT_TEMPERATURE = 0.5`

Finite-budget safety baked into config defaults.

---

## Use cases (per README)

- **Public Opinion Simulation** — live demo: Wuhan University event (CN-native context)
- **Novel Ending Simulation** — Bilibili demo: Dream of the Red Chamber lost-ending prediction (hundreds of thousands of words from first 80 chapters as seed)
- **Financial Prediction** — listed as "coming soon" in README
- **Political News Prediction** — listed as "coming soon" in README

The **novel-ending simulation use case is corpus-first** at T5 — distinct from prior corpus T5 use cases (research / ML / SWE / pentesting / education / personal-productivity / browser-automation).

**Bimodal positioning**:
- Macro / serious: *"rehearsal laboratory for decision-makers, allowing policies and PR to be tested at zero risk"*
- Micro / playful: *"creative sandbox for individual users — deducing novel endings or exploring imaginative scenarios"*

This bimodal framing is unusual in corpus — most T5 entrants pick one tier (serious enterprise OR playful experiment) but not both.

---

## Memory architecture

**Zep Cloud as managed-SaaS memory infrastructure** (`zep-cloud==3.13.0` pinned). 4 dedicated services + 1 utility:
- `services/zep_entity_reader.py` (15 KB)
- `services/zep_graph_memory_updater.py` (22 KB)
- `services/zep_tools.py` (**66 KB** — second-largest file in repo)
- `utils/zep_paging.py` (4.5 KB)

**Memory-as-managed-cloud-dependency** is corpus-first at T5. Prior T5:
- rowboat v43 — IndexedDB local
- browser-use v41 — file-system local
- OpenHands v30 — Docker volumes local
- Skyvern v24 — own session storage
- DeepTutor v38 — own multi-tier memory (Summary + Profile + cross-channel)
- shannon v45 — Workspaces + git checkpoints

MiroFish trades **operational simplicity** (no DB to host, no embedding pipeline to manage) for **vendor lock-in + recurring cost** (Zep Cloud is paid SaaS; free tier per README "sufficient for simple usage").

---

## LLM integration

**OpenAI-SDK-format vendor-agnostic** via 3 env variables:
```env
LLM_API_KEY=...
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1   # README default: Alibaba Bailian (Qwen-plus)
LLM_MODEL_NAME=qwen-plus
```

Pattern #28 internal-env-switch sub-variant (per v40 claude-context formalization).

**Optional accelerator** (from `.env.example`, NOT in README quickstart):
```env
LLM_BOOST_API_KEY=...
LLM_BOOST_BASE_URL=...
LLM_BOOST_MODEL_NAME=...
```

→ **2-tier LLM routing** observable: primary model (heavyweight, e.g. Qwen-plus) for critical paths + accelerator model (lightweight, e.g. Qwen-turbo or local Ollama) for non-critical paths. Architectural pattern not extensively documented; inferred from env naming convention.

---

## What MiroFish is NOT

- ❌ Not a Claude Code plugin (no `.claude/` config)
- ❌ Not an MCP server or MCP client (no MCP integration)
- ❌ Not a Cursor / Codex / OpenClaw / Hermes / Gemini CLI / OpenCode integration
- ❌ Not a published Python package (`mirofish-backend==0.1.0` is local; not on PyPI)
- ❌ Not a published npm package
- ❌ Not a CLI tool (web app only; no `mirofish` command)
- ❌ Not a research benchmark publisher (no SkillsBench / SWE-bench / WebVoyager / arXiv paper observable)
- ❌ Not (yet) a paid SaaS (no Pro tier observable in README; pre-monetization positioning)

This is a **standalone web application** delivered as source-clone + Docker. It does NOT plug into any existing agent runtime.

---

## Corpus-first observations

1. **Multi-agent prediction-simulation T5 sub-archetype** (10th T5 entrant; 100% T5 archetype-diversity-per-wiki preserved)
2. **CAMEL-AI / OASIS methodology lineage** explicit citation (Pattern #19 archetype 2 1st research-org-cluster observation in corpus)
3. **Vue 3 + D3 at T5** (first Vue at T5; prior T5 frontends dominated by React/Next.js)
4. **Zep Cloud as managed-SaaS memory at T5** (first managed-cloud-memory dependency at T5)
5. **Dual-platform-only hard-coded sim** (Twitter + Reddit; not extensible via config)
6. **Bimodal serious-AND-playful positioning** (decision-rehearsal AND creative-sandbox)
7. **Novel-ending simulation use case** (Dream of Red Chamber) — first literary-prediction use case at T5
8. **2-tier LLM routing via `LLM_BOOST_*` env** (primary + accelerator) — corpus-first explicit env-based 2-tier
9. **Reflection-loop bounded by config** (`REPORT_AGENT_MAX_REFLECTION_ROUNDS=2`) — finite-budget safety
10. **High fork-to-star ratio 15.4%** (corpus baseline ~10%; observable but not formalized as pattern)

---

## Cross-references

- **Architecture + dependencies entity**: deep dive into Flask + Vue + CAMEL-AI / OASIS + Zep stack
- **BaiFu + Shanda + BUPT entity**: ecosystem + commercial structure + author profile
- **Storm Bear meta entity (38th)**: domain-distant peer + Pattern #12 baseline-fits-correlation reinforcement
- **Phase 4b deliverable**: T5 10-way comparison + Pattern strengthening summary

---

## Open questions deferred to future deep-dive

- ReportAgent toolset enumeration (99 KB file not extracted in v49)
- Zep tools exhaustive list (66 KB file not extracted)
- OASIS profile generator schema (50 KB)
- Simulation config schema (40 KB)
- Whether "thousands of agents" claim is per-round or aggregate (README marketing vs runtime reality)
- IPC protocol between Flask main + simulation subprocess

These are GREEN-tier-deferral observations; non-blocking for v49.
