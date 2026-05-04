# (C) C1 — README EN+ZH + positioning + 5-stage workflow

**Cluster source**: `00 Source/MiroFish/README.md` (9.1 KB) + `README-ZH.md` (8.2 KB) + LICENSE header + Trendshift badge metadata

---

## What MiroFish positions itself as (verbatim from README)

> *"a next-generation AI prediction engine powered by multi-agent technology. By extracting seed information from the real world (such as breaking news, policy drafts, or financial signals), it automatically constructs a high-fidelity parallel digital world. Within this space, thousands of intelligent agents with independent personalities, long-term memory, and behavioral logic freely interact and undergo social evolution. You can inject variables dynamically from a 'God's-eye view' to precisely deduce future trajectories — **rehearse the future in a digital sandbox, and win decisions after countless simulations**."*

**Tagline (CN)**: *简洁通用的群体智能引擎，预测万物* (literally: "Simple and Universal Swarm Intelligence Engine, Predicting Anything")

**Tagline (EN)**: *"A Simple and Universal Swarm Intelligence Engine, Predicting Anything"*

**Vision (verbatim)**:
- Macro: *"a rehearsal laboratory for decision-makers, allowing policies and public relations to be tested at zero risk"*
- Micro: *"a creative sandbox for individual users — whether deducing novel endings or exploring imaginative scenarios, everything can be fun, playful, and accessible"*

**Operator promise** (verbatim):
> *"You only need to: Upload seed materials (data analysis reports or interesting novel stories) and describe your prediction requirements in natural language"*
> *"MiroFish will return: A detailed prediction report and a deeply interactive high-fidelity digital world"*

⚠️ **Caveat per Storm Bear vault rules** (NEVER fabricate; flag README claims): the phrase *"thousands of intelligent agents"* and *"high-fidelity parallel digital world"* are README marketing claims. Verified via `pyproject.toml`: backend depends on `camel-oasis==0.2.5` + `camel-ai==0.2.78`, which are real OASIS / CAMEL-AI multi-agent simulation libraries. Whether actual deployments instantiate "thousands" of agents at simulation runtime depends on `OASIS_DEFAULT_MAX_ROUNDS` config (default 10) and per-stage agent counts (not exhaustively probed in this v49 wiki — flagged as observable claim, not falsified).

---

## 5-stage workflow (verbatim from README §🔄 Workflow)

1. **Graph Building**: Seed extraction & Individual/collective memory injection & GraphRAG construction
2. **Environment Setup**: Entity relationship extraction & Persona generation & Agent configuration injection
3. **Simulation**: Dual-platform parallel simulation & Auto-parse prediction requirements & Dynamic temporal memory updates
4. **Report Generation**: ReportAgent with rich toolset for deep interaction with post-simulation environment
5. **Deep Interaction**: Chat with any agent in the simulated world & Interact with ReportAgent

**Cross-references to backend services**:
- Stage 1 → `services/graph_builder.py` (18 KB) + `services/ontology_generator.py` (19 KB) + `services/zep_graph_memory_updater.py` (22 KB)
- Stage 2 → `services/oasis_profile_generator.py` (50 KB) + `services/simulation_config_generator.py` (40 KB)
- Stage 3 → `services/simulation_runner.py` (69 KB) + `services/simulation_manager.py` (20 KB) + `services/simulation_ipc.py` (12 KB) + `backend/scripts/run_twitter_simulation.py` + `run_reddit_simulation.py` + `run_parallel_simulation.py`
- Stage 4 → `services/report_agent.py` (99 KB!) — largest single file in repo
- Stage 5 → `api/report.py` (30 KB) + `api/simulation.py` (94 KB)

The 5-stage workflow is reflected verbatim in the source-code organization. Heavyweight stages (3 + 4) have correspondingly heavyweight modules.

---

## Use cases stated in README

- **Financial Prediction** ("coming soon")
- **Political News Prediction** ("coming soon")
- **Public Opinion Simulation** (live demo: Wuhan University public opinion event, hosted at https://666ghj.github.io/mirofish-demo/)
- **Novel Ending Simulation** (Bilibili demo: Dream of the Red Chamber lost ending, hundreds of thousands of words from first 80 chapters)

The corpus-first **novel-ending simulation** use case is structurally distinct from prior corpus T5 use cases (research / ML training / SWE / pentesting / education / personal-productivity / browser-automation). MiroFish positions across **decision-rehearsal-tool** (serious enterprise use) AND **creative-sandbox-tool** (individual playful use) — bimodal positioning observable in vision statement.

---

## Quick Start (verbatim from README)

### Prerequisites table

| Tool | Version | Description | Check |
|------|---------|-------------|-------|
| Node.js | 18+ | Frontend runtime, includes npm | `node -v` |
| Python | ≥3.11, ≤3.12 | Backend runtime | `python --version` |
| uv | Latest | Python package manager | `uv --version` |

### Required env

```env
LLM_API_KEY=your_api_key
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus

ZEP_API_KEY=your_zep_api_key
```

**README explicit recommendation**: Alibaba Bailian (百炼) cloud platform with **Qwen-plus** model. Vendor-agnostic via OpenAI SDK format compatibility.

**Cost warning (verbatim)**: *"High consumption, try simulations with fewer than 40 rounds first"* — README places this warning inline with API key config.

**Optional accelerator config** (from `.env.example`, NOT in README quickstart): `LLM_BOOST_API_KEY` + `LLM_BOOST_BASE_URL` + `LLM_BOOST_MODEL_NAME` — separate "fast model" for non-critical paths. Sub-observation: 2-tier LLM routing (primary + accelerator) at architectural level.

### Install

```bash
npm run setup:all   # one-click: root + frontend + backend
```

Or individually:
```bash
npm run setup       # root + frontend (Node)
npm run setup:backend  # backend (uv sync)
```

### Run

```bash
npm run dev   # concurrently starts backend (5001) + frontend (3000)
```

Or separately: `npm run backend` / `npm run frontend`.

### Docker

```bash
cp .env.example .env
docker compose up -d
```

Pulls `ghcr.io/666ghj/mirofish:latest`. Mirror `ghcr.nju.edu.cn/666ghj/mirofish:latest` (Nanjing University CN-mirror) cited as comment for faster CN pull.

---

## Acknowledgments (verbatim from README — source of corpus-first observations)

> *"**MiroFish has received strategic support and incubation from Shanda Group!**"*

> *"MiroFish's simulation engine is powered by **[OASIS (Open Agent Social Interaction Simulations)](https://github.com/camel-ai/oasis)**, We sincerely thank the CAMEL-AI team for their open-source contributions!"*

These two acknowledgments ground:
- **Pattern #31 strengthening** (Shanda Group commercial-conglomerate incubation = 10th data point)
- **Pattern #19 archetype 2 CAMEL-AI corpus-first methodology-lineage citation**

---

## Recruitment statement (verbatim — also unique signal in corpus)

> *"The MiroFish team is recruiting full-time/internship positions. If you're interested in multi-agent simulation and LLM applications, feel free to send your resume to: **mirofish@shanda.com**"*

The `@shanda.com` email domain (rather than e.g. `@mirofish.ai`) suggests Shanda is the legal-employer entity for MiroFish team hires. **Commercial-funnel companion observation** (Pattern #50 strengthening): mirofish.ai homepage + recruiting through corporate parent + GHCR Docker distribution = 3-channel commercial funnel. NOT a Pro-tier-paywall structure (no $/mo tier observable in README); pre-monetization positioning.

---

## CN README (`README-ZH.md`) — observations

The CN README mirrors EN README structure with these CN-specific additions/differences:
- Identical 5-stage workflow + use cases
- CN-localized API platform recommendations
- QQ Group join image at the bottom (CN community channel; not in EN README)
- Same Shanda + CAMEL-AI acknowledgment

The bilingual EN+ZH README (no other languages) is consistent with author's CN-origin + commercial-incubation by CN conglomerate. **Notable absence**: despite 7-language runtime i18n (zh / en / es / fr / pt / ru / de), README is only in 2 languages. **Mismatch observation**: runtime localization broader than documentation localization — N=1 corpus observation.

---

## Cluster takeaways for downstream entity pages

1. **Core product** entity page should ground the 5-stage workflow with backend service file pointers
2. **BaiFu + Shanda + BUPT** entity page should treat README acknowledgments as primary source, plus GitHub profile data
3. **Architecture + dependencies** entity page should ground CAMEL-AI / OASIS / Zep lineage with `pyproject.toml` exact versions
4. **Storm Bear meta** should reference Pattern #12 (light-minimal governance at 57K), Pattern #19 (CAMEL-AI lineage observation), Pattern #29 (AGPL N=4) — domain-distant peer framing

---

**Cluster summary status:** ✅ complete. 3 of 3 source documents read, 0 fabrications, 1 explicit caveat on README "thousands of agents" claim.
