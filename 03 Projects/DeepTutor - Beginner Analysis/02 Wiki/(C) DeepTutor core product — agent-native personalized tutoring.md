# (C) DeepTutor core product — agent-native personalized tutoring

> **Entity:** DeepTutor product surface (4 entry points + 7 tools + 4 capabilities + 6 chat modes + Book Engine + Co-Writer + Knowledge Hub + Memory)
> **Tier:** T5 Agent-as-application — 6th T5 entrant + NEW education-application sub-archetype
> **Cluster sources:** All 3 cluster summaries; primarily User-facing README + AGENTS+Architecture.

---

## 1. What it is

**Verbatim positioning:** `DeepTutor: Agent-Native Personalized Tutoring`.

An agent-native intelligent learning companion built ground-up (v1.0.0 = ~200K-line rewrite April 4, 2026) around a **2-layer plugin model** (Tools Level 1 + Capabilities Level 2) with **4 entry surfaces** (Web UI / CLI / WebSocket API / Python SDK). Users upload documents to Knowledge Bases, chat across 6 modes in one thread, compile interactive multi-agent "living books", write with AI as first-class collaborator, and run persistent autonomous TutorBots each with own memory + personality + skills.

**Not a chatbot.** TutorBots initiate (proactive heartbeat). Book Engine compiles. Co-Writer collaborates. Memory evolves. Agents drive DeepTutor via SKILL.md. This is a full **agent-native education platform**.

## 2. Why it exists

- **Build-your-own-personalized-tutor** at consumer-hardware cost (Ollama + DeepSeek + Gemini free-tier viable paths)
- **Learn-from-your-own-materials** — KB-first; upload PDFs / MD / text → living book / quiz / Socratic dialogue
- **Agent-era education UX** — traditional courseware is static + linear; DeepTutor is dynamic + multi-modal + agent-driven
- **Research platform** — arXiv-pending paper implies academic publication target; HKUDS Data Intelligence Lab @ HKU credibility signal

## 3. Who uses it

**Primary audience (from README Key Features):**
- Students + self-directed learners
- Researchers processing papers (arXiv paper_search + TeX chunker tools)
- Subject educators building custom tutors

**Secondary audience (from SKILL.md + dual-output CLI):**
- AI agents operating DeepTutor autonomously (nanobot / any tool-using LLM)
- Developers building Skills (user-authored, v1.2.2) + Plugins (manifest.yaml + capability.py)

**Tertiary audience:**
- Enterprise educational deployments (roadmap: auth + multi-user)

## 4. Core product mechanisms

### 4.1 Unified Chat Workspace — 6 modes, 1 thread

Single workspace; 6 modes share context:

| Mode | Purpose |
|------|---------|
| **Chat** | Fluid tool-augmented conversation (RAG / web / code / reason / brainstorm / paper) |
| **Deep Solve** | Multi-agent: plan → investigate → solve → verify + source citations |
| **Quiz Generation** | KB-grounded assessments + built-in validation |
| **Deep Research** | Decompose topic → parallel subtopic agents (RAG + web + papers) → cited report |
| **Math Animator** | Manim-powered math animations + storyboards |
| **Visualize** | NL → SVG / Chart.js / Mermaid / self-contained HTML |

**Tool decoupling:** in every mode, user chooses which tools to enable (or none). Workflow orchestrates reasoning; tools composed.

### 4.2 AI Co-Writer — multi-document AI-collaborative writing

- Multi-document Markdown workspace (each doc persisted; not scratchpad)
- Select-text → Rewrite / Expand / Shorten
- Optional KB + web context
- Non-destructive + full undo/redo
- Save-to-notebook integration

### 4.3 Book Engine — "living books" multi-agent compiler (CORPUS-FIRST)

**Multi-agent pipeline:**
1. Propose outline
2. Retrieve relevant KB sources
3. Synthesize chapter tree
4. Plan each page
5. Compile every block (14 types)

**14 block types:**
text / callout / quiz / flash cards / code / figure / deep dive / animation / interactive demo / timeline / concept graph / section / user note / placeholder

**User control:** review proposal / reorder chapters / chat alongside any page.

**Real-time progress timeline** streams as compilation runs.

**KB fingerprint + drift detection** (`kb_health.py`) — detects stale Book pages when KB docs change.

### 4.4 Knowledge Hub

**4 knowledge objects:**

| Object | Purpose |
|--------|---------|
| **Knowledge Base** | RAG-ready PDF/TXT/MD collection; incremental add |
| **Notebook** | Cross-session organized learning records (color-coded) |
| **Question Bank** | All generated quiz questions; bookmark + @-mention |
| **Skill** | User-authored `SKILL.md` teaching personas (v1.2.2) |

### 4.5 Persistent Memory — Summary + Profile

- **Summary** — running digest (what studied / topics / progression)
- **Profile** — learner identity (preferences / level / goals / communication style)
- Shared across all features + all TutorBots
- Auto-refined every interaction
- CLI: `deeptutor memory show [summary|profile|all]`

### 4.6 Personal TutorBots — persistent autonomous agents (see sibling entity)

See `(C) TutorBot + CLI + bilateral SKILL-md nanobot ecosystem.md` for full deep-dive.

**Highlights:**
- NOT a chatbot — persistent multi-instance autonomous agents
- Per-bot workspace + memory + personality (Soul Template) + skills
- Powered by HKUDS/nanobot (40.7K-star sibling)
- Heartbeat proactive initiation
- 8+ multi-channel connectors (Telegram / Discord / Slack / Feishu / WeChat Work / DingTalk / Email / more)

## 5. Architecture (2-layer plugin model)

### Level 1 — Tools (single-function)

| Tool | Description |
|------|-------------|
| `rag` | KB retrieval |
| `web_search` | Web search with citations (Brave / Tavily / Serper / Jina / SearXNG / DuckDuckGo / Perplexity) |
| `code_execution` | Sandboxed Python |
| `reason` | Dedicated deep-reasoning LLM call |
| `brainstorm` | Breadth-first idea exploration + rationale |
| `paper_search` | arXiv search + TeX chunker + downloader |
| `geogebra_analysis` | Image → GeoGebra commands (4-stage vision pipeline) |

### Level 2 — Capabilities (multi-step)

| Capability | Stages |
|------------|--------|
| `chat` | responding (default tool-augmented) |
| `deep_solve` | planning → reasoning → writing |
| `deep_question` | ideation → evaluation → generation → validation |
| `deep_research` | decompose → parallel-research → synthesize-cited-report |
| `math_animator` | design storyboard → render Manim |
| `visualize` | NL → SVG/Chart.js/Mermaid/HTML |

### Plugin directory convention

```
deeptutor/plugins/<name>/
  manifest.yaml   # name, version, type, description, stages
  capability.py   # class extending BaseCapability
```

**Minimum plugin:** 5-line `async def run(self, context, stream)` method. Lower barrier-to-entry than most T5 entrants.

### Entry surfaces (4)

| Entry | Surface |
|-------|---------|
| **Web UI** | Next.js 16 + React 19 frontend @ `localhost:3782`; Setup Tour interactive onboarding |
| **CLI** | Typer-based; `deeptutor <command>` (15 command families + 12 REPL slash commands) |
| **WebSocket API** | `/api/v1/ws` unified endpoint; heartbeat + auto-reconnect |
| **Python SDK** | Direct import of `deeptutor.core` + `deeptutor.capabilities` |

## 6. Installation (4 options)

| Option | When |
|--------|------|
| A: Setup Tour (`python scripts/start_tour.py`) | First-time user |
| B: Manual local (pip `.[server]` + npm) | Dev control |
| C: Docker (GHCR pre-built multi-arch) | Production / fastest |
| D: CLI-only (pip `.[cli]`) | No web UI / headless agents |

**Defaults:** backend 8001 / frontend 3782. Volumes at `./data/user` + `./data/knowledge_bases`.

## 7. Configuration — 27 LLM + 7 embedding + 7 search providers

**Required `.env` fields (9):** LLM_BINDING / MODEL / API_KEY / HOST + EMBEDDING_BINDING / MODEL / API_KEY / HOST / DIMENSION.

**LLM providers (27):** AiHubMix / Anthropic / Azure OpenAI / BytePlus(+coding) / Custom / DashScope / DeepSeek / Gemini / GitHub Copilot / Groq / llama.cpp / LM Studio / MiniMax / Mistral / Moonshot / Ollama / OpenAI / OpenAI Codex / OpenRouter / OpenVINO / Qianfan / SiliconFlow / Step Fun / vLLM / VolcEngine(+coding) / Xiaomi MIMO / Zhipu.

**Corpus-most-extensive** at 41 integrations (LLM + embedding + search). CN-ecosystem: 11 LLM bindings + `.env.example_CN` pre-configured.

**Local-model stack (5):** llama.cpp / LM Studio / Ollama / vLLM / OpenVINO — full consumer-hardware path.

## 8. Scale + momentum

- **21,230 stars** / 2,900 forks (13.7%) / 48 contributors / 125 watchers / 20 open issues
- **20K in 111 days = ~190 stars/day sustained-viral** (Pattern #27 14th data point; Asia-academic-amplified sub-path)
- **35+ releases in ~4 months** post-v1.0 (~9 releases/month)
- **9-language README** (EN + zh-CN + JA + ES + FR + AR + RU + HI + PT + TH); corpus-first Arabic + Russian + Hindi + Portuguese + Thai in T5

## 9. License + governance

- **Apache-2.0** (Pattern #29 3rd strengthening; no commercial gate)
- **Maintainer:** `@pancacake` (sole named)
- **Governance files:** README + AGENTS + SKILL + CONTRIBUTING + LICENSE (5 files; no CoC / no dedicated SECURITY.md; Security practices inline CONTRIBUTING §7)
- **Pre-commit stack (7 tools):** Ruff + Prettier + detect-secrets + pip-audit + Bandit + MyPy + Interrogate
- **Branching:** `main` / `dev` / `multi-user` (no direct main PRs)

## 10. Corpus-first observations

| # | First |
|---|-------|
| 1 | Asia-academic-lab T5 (HKU-authored; joins US-academic UIUC+CMU v30 + CN-academic Lab4AI v22) |
| 2 | Education-application T5 sub-archetype (teaches humans via agents; distinct from T3 which teaches humans how to build agents) |
| 3 | 9-language README at T5 (Arabic + Russian + Hindi + Portuguese + Thai first in T5) |
| 4 | Multi-agent "living book" compiler (14 block types) |
| 5 | Persistent-autonomous-tutor-bot architecture (not chatbot; not reactive assistant; proactive Heartbeat) |
| 6 | Bilateral runtime-and-skill (SKILL.md exposes DeepTutor to external agents WHILE internally running TutorBot + Capabilities — dual-role) |
| 7 | 7-repo academic ecosystem-portfolio (HKUDS ~173K combined; rivals corporate ecosystem count) |
| 8 | arXiv-pending observation-in-waiting (Pattern #42 data point track pending publication) |
| 9 | 27 LLM providers (corpus-most; 11 CN-ecosystem bindings; `.env.example_CN` region-specific defaults) |
| 10 | ManimCat integration (first Manim-based math-animation specialist in corpus) |
| 11 | Unified Chat Workspace 6-mode single-thread UX (Chat + Deep Solve + Quiz + Deep Research + Math Animator + Visualize share context) |
| 12 | User-authored Skills (`SKILL.md` teaching personas injected into system prompt; v1.2.2) |

## 11. Cross-wiki siblings

- **v30 OpenHands** — closest peer (T5 academic-commercial SWE-agent; UIUC+CMU + ICLR 2025; Pattern #44 N=2)
- **v22 LlamaFactory** — outside-scope training-infra academic-lab (Lab4AI + ACL 2024); Pattern #44 N=1 → now extended to N=3 via DeepTutor
- **v9 deer-flow** — T5 corporate research agent (ByteDance); earliest T5
- **v10 autoresearch** — T5 solo-known ML research agent (Karpathy)
- **v14 paperclip** — T5 community-platform orchestration agent (zero-human companies)
- **v24 Skyvern** — T5 commercial browser-agent (AGPL-3.0 + Cloud)

**Pattern #27 Community-Viral Scale Path** — 14th data point at ~190 stars/day sustained Asia-academic-amplified sub-path.

**Pattern #17 Ecosystem-Layer Organizations** — observational within-pattern variant 5a (academic-lab-ecosystem-portfolio; HKUDS 7 repos = 6th-archetype-variant candidate distinct from variant 5 commercial HuggingFace + Microsoft). N=1; requires another academic-lab ecosystem-portfolio to justify within-pattern variant-at-N=2 promotion.

**Pattern #44 Academic-Lab Affiliation Archetype** — **strengthens to N=3** (default ≥3-observations criterion now satisfied; was structurally-unambiguous-N=2 at v31 mini-audit promotion). Lab4AI + UIUC+CMU + HKU across 3 institutions on 3 continents.

## 12. Storm Bear pilot ranking impact

**NEW candidate #N** for Storm Bear operator self-directed learning pilot (pilot ranking table updated at v38):

- **Pilot rank HIGH-MEDIUM** (new rank ~#3-4 pending other-pilot reassessment):
  - **Apache-2.0** + no commercial gate = zero legal friction for Scrum coach client-facing learning aid
  - **27 LLM providers** including DeepSeek + Qwen (DashScope) = cost-effective for VN budget
  - **Local models supported** (Ollama + llama.cpp + LM Studio + vLLM) = no cloud dependency option
  - **Book Engine** can compile Scrum body-of-knowledge (Scrum Guide + Agile Estimating and Planning + Succeeding with Agile) → interactive VN-localized "Scrum living book"
  - **TutorBot** can be VN Socratic Scrum Master via custom Soul Template (~2-4 weekends operator time)
  - **Deep Research** enables VN Scrum research across arXiv + web
  - **Docker GHCR multi-arch** = simple VN deployment

- **Caveats:**
  - UI i18n currently `"en" | "zh"` — VN UI would require PR (not prohibitive but needs work)
  - No Vietnamese README yet (gap vs claude-howto v32's 73-line VN port)
  - `@pancacake` sole maintainer = bus factor 1 at HKUDS-lab-level (not individual-level; lab absorbs if maintainer leaves)
  - arXiv paper "Coming Soon" — not yet citable in client pitches
  - Python 3.11+ required; Manim math-animator dependency heavy (optional `.[math-animator]`)
  - No MCP integration = doesn't plug into Claude Code workflow; standalone only

## 13. Open questions

- See `01 Analysis/(C) open questions.md`
- Key: Which arXiv venue / year for DeepTutor paper? How does DeepTutor relate to HKUDS LightRAG EMNLP 2025 shared techniques? Bus-factor at HKUDS-lab-level (48 GH contributors but 1 named maintainer)?

---

*This entity is the primary product descriptor. See `(C) TutorBot + CLI + bilateral SKILL-md nanobot ecosystem.md` for agent-runtime + CLI deep-dive, `(C) HKUDS ecosystem-portfolio + academic-lab Pattern 44 N=3.md` for org archetype, and `(C) Storm Bear Vault — DeepTutor as education-application T5 peer.md` for operator relevance.*
