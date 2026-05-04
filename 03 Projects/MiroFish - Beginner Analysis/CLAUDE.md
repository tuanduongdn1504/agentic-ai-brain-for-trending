# MiroFish — Beginner Analysis (Project CLAUDE.md)

**Wiki version:** v49 (49th LLM wiki in Storm Bear corpus)
**Routine:** `05 Skills/llm-wiki-routine-v2.1.md`
**Source:** `00 Source/MiroFish/` (clone of `666ghj/MiroFish` main branch, snapshot 2026-04-02)
**Date shipped:** 2026-04-25

---

## Phase 0 — Source probe (12-axis classification)

| Axis | Value |
|------|-------|
| **Repo** | `666ghj/MiroFish` |
| **Description** | "Simple and Universal Swarm Intelligence Engine, Predicting Anything" / 简洁通用的群体智能引擎，预测万物 |
| **Stars** | 57,307 (~#7 in corpus, between OpenHands v30 71.7K and TrendRadar v19 52.1K) |
| **Forks** | 8,835 (15.4% — high-fork-ratio observation; corpus baseline ~10%) |
| **Watchers** | 57,307 (auto-equal-stars; not meaningful) |
| **Open issues** | 250 |
| **License** | **AGPL-3.0** (4th project-scope AGPL data point in corpus: Skyvern v24 + shannon v45 + + Unsloth Studio v23 component-scope + MiroFish v49) |
| **Primary lang** | Python (backend Flask) + JavaScript (frontend Vue) |
| **Default branch** | main |
| **Created** | 2025-11-26 |
| **Pushed** | 2026-04-02 (source snapshot date) |
| **Latest release** | v0.1.2 (2026-03-07) — early-stage despite 57K stars |
| **Repo size** | 16.2 MB |
| **Topics** | agent-memory, financial-forecasting, future-prediction, knowledge-graph, llms, multi-agent-simulation, public-opinion-analysis, python3, social-prediction, swarm-intelligence |
| **Homepage** | https://mirofish.ai (commercial domain) |

### Authorship + organization

- **Author**: BaiFu (`666ghj`) — Shanghai, China; bio "Do what you love, and love what you do." 3,838 followers, 7 public repos.
- **Affiliation (per GitHub profile)**: BUPT (Beijing University of Posts and Telecommunications) + Shanda Group (盛大).
- **Commercial backing**: README explicit: *"MiroFish has received strategic support and incubation from Shanda Group!"* Recruiting at `mirofish@shanda.com` for full-time/internship.
- **Methodology lineage** (corpus-first CAMEL-AI citation): README explicit: *"MiroFish's simulation engine is powered by **OASIS (Open Agent Social Interaction Simulations)**, We sincerely thank the CAMEL-AI team for their open-source contributions!"* Backend depends on `camel-oasis==0.2.5` + `camel-ai==0.2.78` (pinned versions).

### Tech stack (verified from source)

**Backend** (`backend/`):
- Python ≥3.11, ≤3.12; `uv` package manager; `hatchling` build backend
- Flask 3.0+ + flask-cors 6.0+
- LLM: `openai>=1.0.0` (OpenAI SDK format; vendor-agnostic via env config — `LLM_BASE_URL` + `LLM_API_KEY` + `LLM_MODEL_NAME`)
- Memory: `zep-cloud==3.13.0` (Zep memory graph as managed dependency)
- Multi-agent: `camel-oasis==0.2.5` + `camel-ai==0.2.78` (OASIS social simulation + CAMEL-AI base framework)
- File parsing: `PyMuPDF>=1.24.0` + `charset-normalizer>=3.0.0` + `chardet>=5.0.0`
- Validation: `pydantic>=2.0.0`
- Dev: pytest + pytest-asyncio + pipreqs

**Frontend** (`frontend/`):
- Vue 3.5.24 + Vite 7.2.4 + vue-i18n 11.3.0 + vue-router 4.6.3
- D3 7.9 (visualization)
- axios 1.14 (HTTP)
- @vitejs/plugin-vue 6.0.1 (build)

**Top-level**:
- `package.json` orchestrates with `concurrently` for `npm run dev` (parallel backend + frontend)
- `Dockerfile` (723 B) — multi-stage with Python 3.11 + Node + uv
- `docker-compose.yml` (371 B) — single service `mirofish` from GHCR `ghcr.io/666ghj/mirofish:latest` + Nanjing University mirror cited as comment for CN faster pull
- `.github/workflows/docker-image.yml` — single workflow: builds + pushes Docker image to GHCR on tag push or manual dispatch

### Backend app structure (`backend/app/`)

```
app/
├── __init__.py        # Flask factory, blueprint registration, CORS
├── config.py          # Env config (LLM + Zep + OASIS + Report Agent) + Twitter/Reddit action lists
├── api/               # 3 blueprints: graph (20 KB), simulation (94 KB!), report (30 KB)
├── models/            # project + task data models (Python objects, not ORM)
├── services/          # 13 services: graph_builder + ontology_generator + oasis_profile_generator + simulation_runner (69 KB!) + simulation_manager + simulation_config_generator + simulation_ipc + report_agent (99 KB!) + zep_entity_reader + zep_graph_memory_updater + zep_tools (66 KB) + text_processor
└── utils/             # file_parser + llm_client + locale + logger + retry + zep_paging
```

**Three "heavy" service files** (>50 KB each):
- `services/report_agent.py` — 99 KB — ReportAgent (post-simulation deep-interaction + report generation, with rich toolset)
- `services/simulation_runner.py` — 69 KB — actual OASIS simulation execution
- `services/zep_tools.py` — 66 KB — Zep memory-graph tools wrapper

**Three "heavy" API blueprints**:
- `api/simulation.py` — 94 KB — simulation lifecycle endpoints
- `api/report.py` — 30 KB — report generation + chat
- `api/graph.py` — 20 KB — graph build + entity extraction

**Hard-coded action lists** (from `config.py`):
- Twitter: `CREATE_POST` / `LIKE_POST` / `REPOST` / `FOLLOW` / `DO_NOTHING` / `QUOTE_POST` (6 actions)
- Reddit: `LIKE_POST` / `DISLIKE_POST` / `CREATE_POST` / `CREATE_COMMENT` / `LIKE_COMMENT` / `DISLIKE_COMMENT` / `SEARCH_POSTS` / `SEARCH_USER` / `TREND` / `REFRESH` / `DO_NOTHING` / `FOLLOW` / `MUTE` (13 actions)

**Default OASIS rounds**: 10 (env-tunable via `OASIS_DEFAULT_MAX_ROUNDS`); README warns "high consumption — try simulations with fewer than 40 rounds first".

### Frontend app structure (`frontend/src/`)

```
src/
├── App.vue
├── main.js
├── api/         # axios endpoints
├── assets/
├── components/
├── i18n/        # vue-i18n integration
├── router/      # vue-router
├── store/       # state management (Pinia or Vuex)
└── views/       # page-level components
```

### i18n surface (`locales/`)

- `languages.json` — 7 languages registered: **zh / en / es / fr / pt / ru / de** (each with localized label + LLM-instruction string for response language steering)
- `en.json` — 38 KB
- `zh.json` — 36.8 KB
- **README**: bilingual EN + ZH only (`README.md` + `README-ZH.md`)
- **No VN translation** at any layer (README, locales, runtime)

### Governance surface (top-level)

- `README.md` (9.1 KB) + `README-ZH.md` (8.2 KB)
- `LICENSE` (AGPL-3.0, 34.5 KB full text)
- `Dockerfile` + `docker-compose.yml` + `.dockerignore` + `.gitignore` + `.env.example`
- `package.json` + `package-lock.json` (root + frontend separate)

**ABSENT** at top-level:
- AGENTS.md, CLAUDE.md, AGENT.md
- CONTRIBUTING.md
- SECURITY.md
- SUPPORT.md
- CODE_OF_CONDUCT.md
- CHANGELOG.md
- CODEOWNERS
- ADRs / architecture docs
- Test directory at root (only `backend/scripts/test_profile_format.py` exists)

This is **light-minimal-governance at 57K-star scale** — counter-evidence to Pattern #12 simple formulation; fits Pattern #12 v42 refined 3-factor formulation (maintainer-philosophy: solo + maturity-ambition: cold-start-product + scale-tier: medium-large viral). Operator BaiFu hasn't pivoted to community-governance mode yet despite 57K stars in 5 months — suggests intentional product-velocity prioritization OR pre-monetization positioning.

### 12-axis classification (Phase 0)

| Axis | Value |
|------|-------|
| **Tier** | **T5 Agent-as-application** (10th T5 entrant). Multi-agent prediction-simulation app primary. **Could be argued T2 Agent-as-service** (Flask backend serves frontend; modular API), but the autonomous multi-agent simulation engine + ReportAgent + interactive sandbox + 5-stage workflow + standalone-deployment archetype = T5 application. Frontend is dedicated UI for one specific application (prediction-via-simulation) not a general agent-platform — disqualifies T2. |
| **Archetype** | **Solo-author + commercial-incubation + academic-affiliation hybrid (BUPT-Shanda)** — corpus-first solo + commercial-incubation (Shanda Group strategic backing) + university affiliation (BUPT). Distinct from prior T5: research-corporate (deer-flow ByteDance) / solo-known-individual (autoresearch Karpathy) / community-platform (paperclip) / commercial-startup (Skyvern + browser-use + DeepTutor + shannon Keygraph) / academic-commercial-fusion (OpenHands UIUC+CMU+All-Hands-AI) / personal-productivity-startup (rowboat YC-S24). MiroFish = solo + commercial-incubation-by-conglomerate + university-tied. |
| **Scale tier** | Medium-large (57K / ~5 months ≈ 11.5K/month sustained-community-viral; high velocity but not extreme-burst at 1K+/day awesome-design-md tier) |
| **Primary lang** | Python (backend Flask) + JavaScript (frontend Vue 3) — first **Vue 3 at T5** in corpus (prior T5 frontends: deer-flow Next.js, OpenHands React, browser-use no-frontend, Skyvern React, DeepTutor Next.js, rowboat React+Electron, shannon CLI-only). |
| **Packaging** | Source clone + Docker single-service (`docker-compose up -d` from GHCR) + uv (Python deps) + npm (Node deps); no PyPI package, no npm package — clone-only distribution at 57K. |
| **Origin story** | Solo-academic-author with conglomerate-strategic-backing (Shanda Group incubation; recruiting through Shanda email). Created 2025-11-26 (5 months old at v49). Early-stage product (v0.1.2). |
| **Methodology** | Multi-agent prediction-simulation via 5-stage workflow (Graph Building → Environment Setup → Simulation → Report Generation → Deep Interaction). Built on OASIS / CAMEL-AI methodology lineage. |
| **Governance** | **Light-minimal** (only LICENSE + 2 READMEs + Docker + .env.example + package.json — 7 governance primitives). NO AGENTS/CLAUDE/CONTRIBUTING/SECURITY/CHANGELOG/CODE_OF_CONDUCT/SUPPORT. **Counter-evidence to Pattern #12 simple formulation; consistent with v42 refined 3-factor formulation** (solo + cold-start + commercial-product-velocity). |
| **Agent/skill count** | ~30-50 primitives (5 workflow stages × multi-agent roles; 2 simulation platforms Twitter+Reddit; 19 OASIS hard-coded actions; 13 backend services; 3 API blueprints; 7-language i18n; ReportAgent toolset; Zep memory graph). **Estimated GREEN tier** (standard 4-entity format viable; no aggressive compression needed). |
| **i18n** | **7-language runtime UI** (zh / en / es / fr / pt / ru / de via vue-i18n) but **bilingual README only** (EN + ZH). No VN. **Mismatch worth noting**: runtime localization is broader than documentation localization — pattern observation. |
| **Intellectual influence** | **CAMEL-AI / OASIS lineage CORPUS-FIRST citation**. README + dependency. Pattern #19 archetype 2 methodology-lineage NEW research-org-cluster node candidate (CAMEL-AI is Tsinghua-affiliated open-source AI research collective; first such citation in corpus). Apply consolidation-forward — DO NOT register as 5th individual node; CAMEL-AI is research-org distinct from individual-author lineage. |
| **Agent platforms** | Standalone web app (browser frontend at `localhost:3000` + Flask API at `localhost:5001`); no Claude Code / Codex / Gemini / Cursor integration; no MCP server; no plugin marketplace. |

---

## Phase 0.5 — Pattern Library overlap pre-check (CONSOLIDATION-FORWARD)

**Pre-check protocol (v2.1)**: For every new candidate observation, check whether it overlaps existing patterns ≥70%. If yes, route as strengthening / sub-variant / observational; do NOT register standalone. Only register if clearly structurally distinct.

### 14 candidate observations evaluated

| # | Observation | Existing pattern check | Decision |
|---|-------------|------------------------|----------|
| 1 | T5 multi-agent prediction-simulation sub-archetype | T5 archetype taxonomy (CLAUDE.md state block, not Pattern Library) | Document as taxonomy extension; not Pattern Library candidate |
| 2 | AGPL-3.0 4th project-scope data point | Pattern #29 License-Category Diversity (CONFIRMED) | **Strengthen #29** — 4th project-scope AGPL (Skyvern v24 + shannon v45 + Unsloth Studio v23 component-scope + MiroFish v49 = N=4 across 3 sub-contexts). Sub-variant formalization candidate at next mini-audit. |
| 3 | CAMEL-AI / OASIS methodology lineage | Pattern #19 archetype 2 methodology-lineage (CONFIRMED, 4-node graph: Karpathy + Lam + Anthropic-team-cluster + Lance Martin) | **Document within #19** as research-org-cluster node candidate; **not registered standalone**. Need N=2 corpus citation of CAMEL-AI for formal node addition. Stale-risk-flagged at observation. |
| 4 | BUPT + Shanda Group academic-commercial hybrid affiliation | Pattern #44 Academic-Lab Affiliation (CONFIRMED, 4 sub-variants 44a-d) | **Strengthen #44** observationally — possible 5th sub-variant 44e academic-individual-with-commercial-incubation (BaiFu individual + BUPT loose-affiliation + Shanda corporate-incubation; distinct from 44a single-institution N=1 / 44b multi-institutional-academic-only / 44c multi-institutional-with-industry-partner DeepTutor / 44d corporate-research-lab Google Research magika). Document; not register standalone (N=1 stale-risk). |
| 5 | Shanda Group strategic incubation | Pattern #31 Open-Core Commercial Entity (CONFIRMED N=9) | **Strengthen #31** — 10th data point with corporate-conglomerate-incubation sub-variant observation (vs prior: VC-funded / academic-commercial / commercial-startup-from-day-1 / etc.). Mirofish.ai homepage + recruiting via mirofish@shanda.com = commercial-funnel observable. Pro-tier docs: NOT YET (early-stage) — observable as missing. |
| 6 | Multi-channel community + 2 CN-native channels (Bilibili + QQ Group) + Discord/X/Instagram | Pattern #50 Commercial-Funnel Companion Platform (CONFIRMED N=8) | **Strengthen #50** — 9th data point with multi-region-channel-mix sub-variant (Western: Discord + X + Instagram + GHCR; CN: Bilibili + QQ Group + ghcr.nju.edu.cn mirror). |
| 7 | 57K stars in ~5 months sustained ~11.5K/month | Pattern #27 Community-Viral Scale Path (CONFIRMED) | **Strengthen #27** — 21st+ observation with sustained-community-viral CN-author-amplified sub-path. NOT extreme-burst (so #52 stays stale). Negative un-stale on #52. |
| 8 | LLM provider abstraction via env (LLM_BASE_URL + LLM_API_KEY + LLM_MODEL_NAME) | Pattern #28 Multi-Provider AI Support (CONFIRMED, internal-env-switch sub-variant per v40) | **Strengthen #28** — N=12+ data point with internal-env-switch sub-variant. README explicit Qwen-via-Bailian default; OpenAI-SDK-format-compatible-any-LLM positioning. Plus optional `LLM_BOOST_*` accelerator-mode (separate "fast model" config in .env.example) — sub-observation. |
| 9 | Vue 3 + D3 visualization at T5 (corpus-first Vue at T5) | Pattern #2 Distribution Evolution (CONFIRMED) | **Strengthen #2** observationally — Vue 3 first at T5 (prior T5: React/Next.js dominant). |
| 10 | 7-language runtime i18n (zh/en/es/fr/pt/ru/de) but bilingual README only | (No specific pattern; corpus i18n observations) | Document as observation in entity pages; not Pattern Library candidate. |
| 11 | Memory-as-managed-cloud-dependency (Zep Cloud paid SaaS) at T5 | (No specific pattern; corpus dependency observations) | Document as observation; not Pattern Library candidate. |
| 12 | NO MCP integration + NO Claude Code integration at T5 + 57K-star | Pattern #18 MCP exclusion (refined v36 + v46 multi-layer + v47 sub-axis) | **Strengthen #18 MCP-exclusion observation** — 4th T5-scope MCP-exclusion data point (after pi-mono v36 T1 + DeepTutor v38 T5 + ollama v46 outside-scope). MiroFish at 57K T5 = standalone-application-domain-focused MCP-rejection sub-variant. |
| 13 | NO AGENTS.md / NO CLAUDE.md at T5 commercial-product | Pattern #22 AGENTS.md (CONFIRMED with sub-variants) | **Strengthen #22 absence-observation** — T5 solo + commercial-product abstention; consistent with rowboat v43 + shannon v45 prior T5-no-AGENTS observations. Reinforces T5-application abstention sub-pattern. |
| 14 | High fork-to-star ratio (15.4% — above corpus baseline ~10%) | (No specific pattern) | Document observationally; possible derivative-velocity signal but N=1; do not register. |

### Phase 0.5 outcome

- **0 NEW ACTIVE CANDIDATES** registered
- **0 NEW OBSERVATION-TRACKs** registered (CAMEL-AI lineage and BUPT-Shanda hybrid documented as within-pattern strengthening observations rather than OT to extend zero-streak; both stale-risk-flagged should they re-appear)
- **9 patterns strengthened**: #29 / #19 / #44 / #31 / #50 / #27 / #28 / #18 / #22
- **1 pattern observation strengthening**: #2 (Vue 3 at T5)
- **Negative un-stale check**: #52 Extreme-Viral-Velocity (sustained ≠ burst); other stale candidates negative
- **13-CONSECUTIVE-WIKI ZERO-NEW-ACTIVE-CANDIDATES STREAK** (v37-v49) extending the corpus record
- **Pattern Library ratio target**: preserve 19:37 = 0.513:1 unchanged 13th consecutive cycle

---

## Phase 0.9 — Primitive-count flagging (v2.1 informal discipline)

**Primitive surface estimation**:
- 5 workflow stages × ~3-5 sub-steps each = ~15-25 stage-primitives
- 13 backend services + 3 API blueprints + 6 utils = 22 backend modules
- 19 OASIS hard-coded actions (Twitter 6 + Reddit 13)
- 7 i18n languages
- ~10-15 frontend Vue components/views (estimate without enumerating)
- Zep tools + ReportAgent toolset (~10-20 tools — large file 99 KB)

**Total primitive estimate**: ~75-100 surface primitives across 4-entity allocation. **Outcome: GREEN** (within 4-entity standard format; no aggressive compression needed; below YELLOW threshold ~120-180 / RED ~250-400 / EXTREME ~500+).

**Velocity expectation**: ~2h GREEN baseline within tolerance.

**Compression decisions**:
- Zep tools (66 KB single file) cited not enumerated tool-by-tool
- ReportAgent (99 KB single file) summarized with tool-category list, not exhaustive
- 64-table-equivalent OASIS internals cited via `camel-oasis==0.2.5` upstream reference, not extracted
- Frontend components grouped by view-category, not file-by-file

---

## Storm Bear meta-entity per-wiki applicability

MiroFish = financial / political / public-opinion / novel-ending **prediction tool** — domain-distant from Storm Bear vault (Markdown knowledge base + Scrum coach role).

**Direct utility**: ZERO — Storm Bear doesn't predict financial/political outcomes; vault doesn't run multi-agent simulations.

**Observational value (LOW-MEDIUM)**:
- AGPL-3.0 license-choice reference (4th project-scope data point in corpus)
- CAMEL-AI / OASIS methodology lineage as alternative to Karpathy / John Lam / Anthropic-team / Lance Martin influence nodes
- Multi-language runtime i18n (7 languages) vs documentation i18n (2 languages) mismatch as architectural choice
- Solo + commercial-incubation hybrid governance model (BaiFu + Shanda) as commercial-positioning reference
- Light-minimal governance at 57K-star scale = 6th counter-evidence wiki to Pattern #12 simple formulation (further validates v42 refined 3-factor formulation)

**Decision: INCLUDE 38th consecutive Storm Bear meta-entity** — but framed as "domain-distant peer + GREEN-primitive-count-discipline observation + Pattern #12 baseline-fits-correlation reinforcement"; NOT structural template. Streak preservation v10-v49 acknowledged but per-wiki applicability per v29 reform applied: meta-entity is light-touch documentation of indirect lessons, not artificial-streak inflation.

---

## Deliverables checklist (13 files)

- [x] Project CLAUDE.md (this file)
- [ ] 3 cluster summaries (`01 Cluster Summaries/`)
- [ ] 4 entity pages (`02 Entity Pages/`) — incl. 38th Storm Bear meta
- [ ] 1 bilingual VN+EN beginner guide (`03 Beginner Guide/`)
- [ ] 1 Phase 4b primary deliverable (`04 Phase 4b Deliverable/`)
- [ ] 1 iteration log v49 (`05 Iteration Log/`)
- [ ] 1 INDEX.md
- [ ] 1 LOG.md
- [ ] 1 OPEN-QUESTIONS.md
- [ ] PATTERN_LIBRARY.md updates (Phase 5)
- [ ] Vault CLAUDE.md state block + project entry (Phase 6)
- [ ] GOALS.md session entry (Phase 6)

---

## Phase 4b primary focus (preview)

**T5 10-way extension + multi-agent prediction-simulation T5 sub-archetype + Pattern #29 AGPL-3.0 4th project-scope data point + Pattern #19 archetype 2 CAMEL-AI lineage corpus-first observation + Pattern #44 academic-individual-with-commercial-incubation observation + Vue-3-at-T5 corpus-first.**

100% T5 archetype-diversity-per-wiki preserved at N=10 if MiroFish prediction-simulation sub-archetype confirmed distinct.
