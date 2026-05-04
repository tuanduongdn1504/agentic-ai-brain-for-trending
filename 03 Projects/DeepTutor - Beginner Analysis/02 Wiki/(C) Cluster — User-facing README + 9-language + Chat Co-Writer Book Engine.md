# (C) Cluster — User-facing README + 9-language + Chat / Co-Writer / Book Engine

> **Source:** `README.md` (759 lines) + 9 localized READMEs under `assets/README/` + homepage badges + release-notes + News section + Feature catalog.
> **Cluster size:** ~760 lines primary + 9 translations (exact line counts not probed; translations referenced not replicated).
> **Positioning verbatim:** *"DeepTutor: Agent-Native Personalized Tutoring"*.

---

## 1. Positioning + tagline verbatim

**Tagline:** `DeepTutor: Agent-Native Personalized Tutoring`

**Elevator pitch (synthesized from Key Features + Get Started intro):**

> Agent-native intelligent learning companion. Six-mode unified chat workspace. AI Co-Writer for multi-document writing with AI as first-class collaborator. Book Engine multi-agent pipeline turns materials into structured, interactive "living books" with 14 block types. Knowledge Hub (RAG-ready KBs + notebooks + question bank + user-authored skills). Persistent memory (Summary + Profile). Personal TutorBots (autonomous, not chatbot; each bot = own workspace + memory + personality + skillset; powered by HKUDS/nanobot). Agent-Native CLI exposes every capability for humans (rich terminal) and AI agents (structured JSON) — hand any agent the `SKILL.md` and it can drive DeepTutor autonomously.

**Audience:** Learners (primary) + AI agents-driving-DeepTutor (secondary) + developers extending via plugins (tertiary).

**Philosophy (inferred from architecture):**
- Agent-native (not agent-augmented) — architecture ground-up-rewrite April 2026 ~200k-line v1.0.0 release.
- Tools decoupled from workflows — in every mode, user decides which tools to enable, how many, or none.
- Knowledge actively participates — not passive storage; every KB entry feeds conversations.
- Dual-audience CLI — humans get rich terminal; agents get structured JSON event stream.

## 2. Scale signals (verbatim from GitHub)

| Metric | Value |
|--------|-------|
| Stars | **21,230** |
| Forks | 2,900 (13.7% fork-to-star ratio) |
| Watchers | 125 |
| Open issues | 20 |
| Total commits | 598 |
| Contributors | 48 |
| Size | Repo is ~medium-large (multi-surface monorepo) |
| Velocity | **20,000 stars in 111 days = ~190 stars/day sustained-viral** (News section explicit) |
| Created | Effective start ~December 2025 (v0.2.0 on 2026-01-02 + "2025.12.29 DeepTutor officially released!" News entry) |
| Pushed | 2026-04-22 (today-adjacent; v1.2.2 release) |
| Latest release | **v1.2.2 (2026-04-22)** |
| License | Apache-2.0 |
| Primary lang | Python 74.7% + TypeScript 24.2% + JavaScript 0.4% |

**Scale context:** 21.2K places DeepTutor in **large-tier (20-60K)** between Skyvern v24 (21.3K) and claude-howto v32 (28.2K). Within T5 tier, DeepTutor is **4th largest** (autoresearch 74K > paperclip 55.9K > OpenHands 71.7K > deer-flow 62K > **DeepTutor 21.2K** > Skyvern 21.3K; tied approximately with Skyvern).

## 3. 9-language i18n (corpus-first T5 9-language)

| Language | File path | Flag |
|----------|-----------|------|
| English | `README.md` (primary) | 🇺🇸 (implicit) |
| Chinese (Simplified) | `assets/README/README_CN.md` | 🇨🇳 |
| Japanese | `assets/README/README_JA.md` | 🇯🇵 |
| Spanish | `assets/README/README_ES.md` | 🇪🇸 |
| French | `assets/README/README_FR.md` | 🇫🇷 |
| Arabic | `assets/README/README_AR.md` | 🇸🇦 |
| Russian | `assets/README/README_RU.md` | 🇷🇺 |
| Hindi | `assets/README/README_HI.md` | 🇮🇳 |
| Portuguese | `assets/README/README_PT.md` | 🇵🇹 |
| Thai | `assets/README/README_TH.md` | 🇹🇭 |

**Corpus-first observations:**
- **First Arabic + Russian + Hindi + Portuguese README** among T5 entrants
- **Ties 9-language top-tier** shared by oh-my-claudecode v27 (7-language), pi-mono v36 (EN-only), fish-speech v20 (7-language), awesome-mcp-servers v31 (7-language); **DeepTutor 9-language exceeds all prior corpus** except matches tie at 9-language with awesome-mcp-servers if counting all (Thai added at v1.1.2 release = 2026-04-18)
- **Thai README added at v1.1.2** (2026-04-18, explicit release note) — demonstrates i18n is deliberate roadmap item, not historical accident

## 4. Key Features (6 features, verbatim structure)

### 4.1 Unified Chat Workspace — 6 modes, 1 thread

| Mode | Description (verbatim condensed) |
|------|-----------------------------------|
| **Chat** | Fluid, tool-augmented conversation. Choose RAG retrieval / web search / code execution / deep reasoning / brainstorming / paper search — mix and match. |
| **Deep Solve** | Multi-agent problem solving: plan, investigate, solve, verify — with precise source citations at every step. |
| **Quiz Generation** | Generate assessments grounded in your knowledge base, with built-in validation. |
| **Deep Research** | Decompose a topic into subtopics, dispatch parallel research agents across RAG + web + academic papers, produce a fully cited report. |
| **Math Animator** | Turn mathematical concepts into visual animations and storyboards powered by Manim. |
| **Visualize** | Generate interactive SVG diagrams / Chart.js charts / Mermaid graphs / self-contained HTML pages from natural language. |

**Novel UX claim:** *"Tools are decoupled from workflows — in every mode, you decide which tools to enable, how many to use, or whether to use any at all. The workflow orchestrates the reasoning; the tools are yours to compose."*

**Continuity claim:** *"Start with a quick chat question, escalate to Deep Solve when it gets hard, visualize a concept, generate quiz questions to test yourself, then launch a Deep Research to go deeper — all in one continuous thread."*

### 4.2 AI Co-Writer — multi-document Markdown + AI as first-class collaborator

- Multi-document workspace (not single scratchpad)
- Select text → Rewrite / Expand / Shorten
- Optionally draw context from KB or web
- Non-destructive editing with full undo/redo
- Save any piece straight to notebooks

### 4.3 Book Engine — interactive "living books"

- Input: topic + KB
- Multi-agent pipeline: propose outline → retrieve sources → synthesize chapter tree → plan each page → compile blocks
- Output: structured interactive book (not static export)
- **14 block types:** text / callout / quiz / flash cards / code / figure / deep dive / animation / interactive demo / timeline / concept graph / section / user note / placeholder
- Real-time progress timeline during compilation
- User control: review proposal, reorder chapters, chat alongside any page
- **Corpus-first multi-agent-living-book-compiler architecture**

### 4.4 Knowledge Hub

- **Knowledge Bases**: Upload PDF/TXT/Markdown → RAG-ready searchable collections; incremental add
- **Notebooks**: Cross-session organized learning records; save from Chat/Co-Writer/Book/Deep Research into color-coded notebooks
- **Question Bank**: All generated quiz questions; bookmark + @-mention in chat
- **Skills** (user-authored, NEW v1.2.2): `SKILL.md` files = custom teaching personas; name + description + optional triggers + Markdown body injected into chat system prompt when active; Socratic tutor / peer study partner / research assistant / any role

### 4.5 Persistent Memory

- **Summary**: running digest (what studied / topics explored / understanding progression)
- **Profile**: learner identity (preferences / knowledge level / goals / communication style)
- **Shared across all features + all TutorBots**
- Automatically refines with every interaction

### 4.6 Personal TutorBots — persistent autonomous agents

- **NOT chatbot** (explicit positioning)
- Each TutorBot = own workspace + memory + personality + skillset
- Powered by HKUDS/nanobot (40.7K-star sibling)
- Simultaneously run multiple (Socratic math tutor + patient writing coach + rigorous research advisor)
- See SKILL+CLI cluster for TutorBot mechanics deep-dive

### 4.7 Agent-Native CLI (7th feature item — see SKILL cluster for deep-dive)

- Every capability + KB + session + memory + TutorBot = 1 command away
- Dual output: rich terminal (humans) + structured JSON (agents/pipelines)
- Hand `SKILL.md` to any tool-using agent → autonomous operation

## 5. Release cadence (observed from README Releases section)

**Major milestones:**
- **2025.12.29** DeepTutor officially released (v0.1.x)
- **2026.1.5** v0.3.0 Unified PromptManager + GHCR Docker images
- **2026.1.9** v0.4.0 Multi-provider LLM + embedding support
- **2026.1.15** v0.5.0 Unified service config + RAG-per-KB pipeline
- **2026.1.23** v0.6.0 Session persistence + Chinese localization
- **2026.4.4** **v1.0.0-beta.1** — **AGENT-NATIVE ARCHITECTURE REWRITE ~200K LINES** (Tools + Capabilities plugin model, CLI & SDK, TutorBot, Co-Writer, Guided Learning, persistent memory)
- **2026.4.8** v1.0.0-beta.3 — Native OpenAI/Anthropic SDK (dropped litellm; drops Pattern #28 abstraction-library and moves to native-routing — noteworthy design decision)
- **2026.4.10** v1.0.1 Visualize capability
- **2026.4.13** v1.0.3 Question Notebook + Mermaid Visualize
- **2026.4.15** v1.1.0 LaTeX block math + LLM diagnostic probe
- **2026.4.18** v1.1.2 Schema-driven Channels + Thai README
- **2026.4.20** **v1.2.0** — **Book Engine multi-agent "living book" compiler with 14 block types** + **multi-document Co-Writer workspace** + interactive HTML visualizations
- **2026.4.21** v1.2.1 Per-stage chat token limits + regenerate last response
- **2026.4.22** **v1.2.2 (latest)** — **user-authored Skills system (CRUD + chat integration)** + response_format auto-fallback + TutorBot WebSocket auto-start + Book Library UI

**Cadence:** ~35+ releases in ~4 months (~9 releases/month); extremely active post-v1.0 agent-native rewrite.

## 6. Get Started (4 installation options)

### Option A — Setup Tour (recommended)

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor
conda create -n deeptutor python=3.11 && conda activate deeptutor
python scripts/start_tour.py
```

Interactive guided tour (Web or CLI mode) — dependency install + `.env` configuration + live connection testing + auto-launch. Runs on `http://localhost:3782`.

### Option B — Manual local install

```bash
pip install -e ".[server]"
cd web && npm install && cd ..
cp .env.example .env
# Edit .env: LLM_BINDING, LLM_MODEL, LLM_API_KEY, LLM_HOST, EMBEDDING_BINDING, EMBEDDING_MODEL, EMBEDDING_API_KEY, EMBEDDING_HOST, EMBEDDING_DIMENSION
python scripts/start_web.py
```

### Option C — Docker

- **Official GHCR image:** `ghcr.io/hkuds/deeptutor:latest` (amd64 + arm64)
- `docker compose -f docker-compose.ghcr.yml up -d`
- Or build from source: `docker compose up -d`
- Dev mode with hot-reload: `docker compose -f docker-compose.yml -f docker-compose.dev.yml up`

### Option D — CLI-only

```bash
pip install -e ".[cli]"
cp .env.example .env
deeptutor chat  # or: deeptutor run <capability> "<message>"
```

**Default ports:** Backend 8001 / Frontend 3782 (atypical ports; avoid clash with standard 8000/3000 dev servers).

**Remote deployment:** `NEXT_PUBLIC_API_BASE_EXTERNAL=https://server.com:8001` for browser→backend public URL.

**Data volumes:** `./data/user` (settings/memory/workspace/sessions/logs) + `./data/knowledge_bases` (docs + vector indices); survive `docker compose down`.

## 7. Provider ecosystem (27 LLM + 7 embedding + 7 search = **corpus-most-extensive at 41 integrations**)

### LLM (27)
AiHubMix / Anthropic / Azure OpenAI / BytePlus + Coding Plan / Custom (OpenAI-compat) / DashScope (Qwen) / DeepSeek / Gemini / GitHub Copilot / Groq / llama.cpp / LM Studio / MiniMax / Mistral / Moonshot (Kimi) / Ollama / OpenAI / OpenAI Codex / OpenRouter / OpenVINO Model Server / Qianfan (Ernie) / SiliconFlow / Step Fun / vLLM / VolcEngine + Coding Plan / Xiaomi MIMO / Zhipu AI (GLM)

**Notable corpus-firsts among providers:**
- **OpenAI Codex** (GitHub Copilot-adjacent), **OpenVINO Model Server**, **Qianfan (Ernie Baidu)**, **Step Fun**, **Xiaomi MIMO**, **VolcEngine Coding Plan** — first in Storm Bear corpus

### Embedding (7)
OpenAI / Azure OpenAI / Cohere / Jina / Ollama / vLLM-LM-Studio / custom. `.env.example_CN` covers Chinese embedding providers.

### Web Search (7)
Brave / Tavily / Serper / Jina / SearXNG / DuckDuckGo / Perplexity. Brave recommended (free tier).

**CN-ecosystem-aware:** `.env.example_CN` separate from `.env.example` indicates deliberate China-ecosystem support (DashScope + DeepSeek + Moonshot + Qianfan + SiliconFlow + Step Fun + VolcEngine + Xiaomi MIMO + Zhipu = **9 CN-ecosystem LLM bindings** alone).

## 8. Roadmap (6 items)

| Status | Milestone |
|--------|-----------|
| 🎯 | Authentication & Login (optional login for public deployments + multi-user) |
| 🎯 | Themes & Appearance (diverse themes + customizable UI) |
| 🎯 | Interaction Improvement (optimize icons + interaction details) |
| 🔜 | Better Memories (integrate better memory management) |
| 🔜 | **LightRAG Integration** (integrate HKUDS/LightRAG as advanced KB engine) |
| 🔜 | Documentation Site (docs page + API reference + tutorials) |

**Observation:** LightRAG integration 🔜 demonstrates **HKUDS ecosystem-portfolio coordinated roadmap** — DeepTutor (21.2K education-agent) will integrate LightRAG (34.2K RAG backbone). Cross-project HKUDS synergy.

## 9. Community + ecosystem (7 HKUDS repos)

**DeepTutor community:**
- Discord (badge visible; `discord.gg/eRsjPgMU4t`)
- Feishu (CN-ecosystem group; `Communication.md` reference)
- WeChat (issue #78 registration; CN-ecosystem group)
- GitHub Discussions

**DeepTutor stands on:**
- **nanobot** (HKUDS, 40.7K stars) — "Ultra-lightweight agent engine powering TutorBot"
- **LlamaIndex** (non-HKUDS, `run-llama/llama_index`) — "RAG pipeline and document indexing backbone"
- **ManimCat** (`Wing900/ManimCat`, non-HKUDS) — "AI-driven math animation generation for Math Animator"

**HKUDS ecosystem references at bottom of README:**
- ⚡ **LightRAG** (34.2K) — Simple & Fast RAG
- 🤖 **AutoAgent** (mentioned in README; not in top-7 HKUDS visible list, check org page) — Zero-Code Agent Framework
- 🔬 **AI-Researcher** (mentioned; not in top-7 HKUDS visible list) — Automated Research
- 🧬 **nanobot** (40.7K) — Ultra-Lightweight AI Agent

**Full HKUDS top-7 repos (from HKUDS org page probe):**
1. **nanobot** 40,692 stars (MIT) — Ultra-Lightweight Personal AI Agent
2. **LightRAG** 34,162 stars (MIT; EMNLP 2025 paper) — Simple and Fast RAG
3. **CLI-Anything** 32,394 stars (Apache-2.0) — Making ALL Software Agent-Native
4. **DeepTutor** 21,230 stars (Apache-2.0) — Agent-Native Personalized Learning Assistant
5. **RAG-Anything** 18,272 stars (MIT) — All-in-One RAG Framework
6. **DeepCode** 15,264 stars (MIT) — Open Agentic Coding (Paper2Code + Text2Web + Text2Backend)
7. **OpenHarness** 11,068 stars (MIT) — Open Agent Harness with Built-in Personal Agent Ohmo

**Combined ~173K stars across 7 agent-focused repos** — **first academic-lab ecosystem-portfolio in Storm Bear corpus** exceeding corporate Microsoft (v6+v28 spanning T3+T4) in agent-focused-repo-count-per-org.

## 10. Star History (News section)

- **2026.2.6** 10K stars in 39 days (~256 stars/day early-viral)
- **2026.4.19** 20K stars in 111 days (~190 stars/day sustained-viral)
- Deceleration moderate (256 → 190 stars/day over 72 days); sustained-viral not extreme-viral (#52 threshold 1K/day).

## 11. Attribution + author signature

**Footer verbatim:** `**Data Intelligence Lab @ HKU**`

**Licensed:** Apache License 2.0

**Visit counter badge:** Active (`visitor-badge.laobi.icu`); **first T5 corpus entrant with visit counter** (novelty marker consistent with CN-ecosystem README convention).

## 12. Supply-chain + safety framing (none explicit)

- No dedicated SECURITY.md
- No Code of Conduct file (corpus-notable absence for 21K-star academic project; Microsoft markitdown v28 had CoC)
- CONTRIBUTING.md §7 Security Best Practices covers:
  - File upload size limits (100 MB general / 50 MB PDF) + multi-layer validation (extension + MIME + content sanitization) + path-traversal filename sanitization
  - `shell=False` subprocess enforcement
  - `pathlib.Path` + LF line endings via `.gitattributes`
- No supply-chain incident disclosure (unlike crawl4ai v29 `unclecode-litellm` Pattern #66)
- detect-secrets pre-commit + `.secrets.baseline` present — supply-chain-aware but preventive, not reactive

## 13. 13-section summary pattern-library signals

| Signal | Pattern | Direction |
|--------|---------|-----------|
| 9-language README | #27 Community-Viral Scale Path | Strengthens (Asia-academic-amplified sub-path) |
| 27 LLM providers | #28 Multi-Provider AI Support | **Corpus-most extensive** — strengthens |
| Academic lab + arXiv-pending | #42 Academic-Published Framework | Observational-in-waiting |
| Academic lab affiliation | #44 Academic-Lab Affiliation Archetype | **N=3 strengthening** (was N=2; now 3rd data point) |
| 7-repo HKUDS portfolio | #17 Ecosystem-Layer Organizations | Observational variant 5a academic-lab |
| No MCP integration | #18 Agent Runtime Standardization | Counter-evidence T5-academic-research scope |
| Medium governance | #12 Governance Depth Correlates with Org | Consistent with academic-lab archetype |
| AGENTS.md 149 lines | #22 AGENTS.md Industry Standard | T5 adoption data point |
| Bilateral runtime-and-skill | N/A | Corpus-first observation; no pattern registration |
| Multi-agent-living-book compiler | N/A | Corpus-first architecture; no pattern registration |
| Education-application T5 sub-archetype | N/A | Structural tier observation; no pattern |

**Cluster summary complete.** Cross-reference: see `(C) Cluster — AGENTS SKILL CONTRIBUTING + 2-layer plugin architecture.md` for Level 1 Tools / Level 2 Capabilities / plugin discovery details, and `(C) Cluster — Core protocols + TutorBot + CLI + 27 providers + Docker.md` for runtime architecture and deployment surfaces.
