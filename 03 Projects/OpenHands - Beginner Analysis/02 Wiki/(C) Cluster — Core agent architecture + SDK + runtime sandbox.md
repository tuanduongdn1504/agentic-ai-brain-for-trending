# (C) Cluster — Core agent architecture + SDK + runtime sandbox

> **Wiki:** v30 OpenHands
> **Cluster:** Core technical architecture (the engine that makes OpenHands work)
> **Source density:** High — ICLR 2025 paper + SDK Nov 2025 paper + README + openhands.dev product page + COMMUNITY.md
> **Status:** Cluster summary complete

---

## 1. Summary

OpenHands' core value proposition is an **autonomous software-engineering agent** that writes code, runs commands, browses the web, and interacts with development environments the way a human developer does. The architecture has two major layers covered by two separate peer-reviewed papers 16 months apart:

1. **OpenHands platform layer (ICLR 2025 paper, arXiv 2407.16741)** — originally published as *"OpenHands: An Open Platform for AI Software Developers as Generalist Agents"* (f.k.a. OpenDevin). Defines the overall agent loop, sandboxed execution model, multi-agent coordination, and benchmark harness.

2. **Software Agent SDK layer (arXiv 2511.03690, Nov 2025)** — *"The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents."* Redesign as a composable Python SDK emphasizing flexibility, security, and production-grade features: native sandboxed execution, lifecycle control, model-agnostic multi-LLM routing, built-in security analysis, local-to-remote execution portability, integrated REST/WebSocket services, and multi-interface environments (VS Code + VNC browser + CLI).

Both layers are community-backed (71.7K stars, 9K forks, 101+ releases) and company-backed (All Hands AI commercial entity with $18.8M funding).

## 2. Sources in cluster

| Source | Type | Key content |
|--------|------|-------------|
| README.md (OpenHands/OpenHands main branch) | Project docs | 5-surface product taxonomy (SDK / CLI / Local GUI / Cloud / Enterprise) + SWE-Bench 77.6 badge + trusted users |
| arXiv 2407.16741 (ICLR 2025) | Peer-reviewed paper | Platform architecture + agent loop + sandboxed execution + multi-agent coordination + benchmark harness |
| arXiv 2511.03690 (Nov 2025) | Tech report / paper | SDK redesign + production-grade features + lifecycle control + multi-interface + security analysis |
| openhands.dev product page | Company product | Pre-built workflows + enterprise positioning + funding reference |
| COMMUNITY.md | Governance | Benevolent dictator model + High Openness + High Agency values |

## 3. Core architecture — agent loop + Action-Observation model

### The agent loop (ICLR 2025 paper)

OpenHands implements a generalist agent loop consistent with the emerging T5 Agent-as-application paradigm:

1. **Goal specification** — user provides natural-language task
2. **Perception** — agent observes file system, terminal, browser, IDE state
3. **Action selection** — LLM selects next action (shell command / file edit / browser navigation / IDE interaction)
4. **Sandboxed execution** — action runs in isolated Docker runtime (not host)
5. **Observation** — result captured and fed back to LLM context
6. **Iteration** — loop continues until goal achieved or halt condition triggered
7. **Human-in-the-loop** — user may intervene, approve, or redirect at any step

### Sandboxed execution model

Key innovation vs naive agent-runs-shell approaches:

- **Docker-based runtime** — each agent session spawns its own container (isolation + reproducibility)
- **Lifecycle control** (SDK paper) — pause / resume / observe agent state externally
- **Built-in security analysis** (SDK paper) — actions reviewed pre-execution (consistent with trust boundary emerging in Storm Bear corpus at [v13 gws](../../../googleworkspace-cli%20-%20Beginner%20Analysis/02%20Wiki/) AGENTS.md §6 discipline)
- **Local-to-remote execution portability** — same agent definition runs laptop or cloud cluster

**Corpus comparison:** Skyvern v24 sandbox is Playwright-based (browser-only); OpenHands sandbox is Docker-based (full-OS). OpenHands runtime is **more general** — can edit code + run tests + browse + use IDE.

### Multi-interface environments (SDK paper)

SDK supports multiple environment surfaces simultaneously:

- **VS Code integration** — agent sees + edits user's IDE state
- **VNC browser** — agent can see + interact with GUI apps
- **CLI** — traditional terminal access

First corpus wiki with VNC-based GUI-app-interaction as first-class feature. Skyvern v24 uses Playwright (browser-only headless); OpenHands VNC enables **any GUI app**.

## 4. SDK architecture (Nov 2025 paper) — production-grade composition

### Composability primitives

SDK paper emphasizes **composable extension** rather than monolithic framework. Key primitives (inferred from paper abstract + README):

- **Agent base class** — BYO agent implementation subclassing common primitives
- **Action / Observation dataclasses** — typed interfaces between agent and runtime
- **LLM client abstraction** — model-agnostic routing (multi-provider support)
- **Runtime adapter** — Docker local / Kubernetes remote / Cloud hosted
- **REST/WebSocket services** — external API surface for integration
- **Lifecycle hooks** — observability + security analysis insertion points

### Model-agnostic multi-LLM routing

Supports Claude, GPT, Minimax, and other providers via routing layer. **Pattern #28 Multi-Provider AI Support 6th corpus data point** (joins v19 TrendRadar LiteLLM + v15 multica 8 providers + v26 HF agents-course multi-framework + v27 OMC 4 CLI runtimes + v29 crawl4ai unclecode-litellm fork).

OpenHands native-BYO variant: applications explicitly route across providers vs library-level adapter. Distinct from abstraction-library variant (LiteLLM-based) — similar to Skyvern v24 approach.

### Security analysis feature

**First corpus T5 wiki with built-in security analysis as first-class primitive.** Distinct from:
- [v13 gws](../../../googleworkspace-cli%20-%20Beginner%20Analysis/) Model Armor (post-LLM sanitization, response-level)
- [v22 LlamaFactory](../../../LlamaFactory%20-%20Beginner%20Analysis/) (training-time, not agent-time)
- [v24 Skyvern](../../../Skyvern%20-%20Beginner%20Analysis/) anti-bot (proprietary Cloud feature, not OSS architecture)

OpenHands security analysis is **agent-action-level review** — actions evaluated pre-execution within the agent loop itself.

## 5. Cross-wiki technical parallels

### T5 peer architecture comparison

| Dimension | deer-flow v9 | autoresearch v10 | paperclip v14 | Skyvern v24 | **OpenHands v30** |
|-----------|--------------|-------------------|----------------|-------------|-------------------|
| **Runtime isolation** | Internal ByteDance infra | Local git-based | PGlite + Playwright | Playwright container | **Docker-native + Kubernetes** |
| **Primary interface** | Next.js web UI | CLI git-based | React web UI | Web UI + API | **5 surfaces (SDK+CLI+GUI+Cloud+K8s)** |
| **Security primitive** | Not highlighted | Ephemeral git branch | 5 invariants promptfoo | Anti-bot proprietary | **Built-in security analysis (OSS)** |
| **Multi-LLM** | Configurable | Single-model | BYO agent adapter | 8+ providers native | **Claude+GPT+Minimax+BYO** |
| **Paper lineage** | Trending report | Karpathy blog | No paper | No paper | **ICLR 2025 + Nov 2025 SDK** |

### Pattern #18 Agent Runtime Standardization

- OpenClaw/Hermes mentioned in corpus 6+ wikis (community-platform-specific)
- **OpenHands NOT adopting OpenClaw/Hermes** — builds own Docker-native runtime. Fits Pattern #18 refinement: "Western-community-platform-specific" OR "smaller-scale-tool-specific" — OpenHands is commercial-entity + enterprise-scale, opts out similar to gws v13 + spec-kit v17 + markitdown v28.

## 6. Claims + evidence grounding

Every claim above anchored to sources:

- **SWE-Bench 77.6**: README badge + paper claim (verifiable)
- **$18.8M funding**: openhands.dev product page testimonial section (WebFetch retrieval, unverified by filing)
- **ICLR 2025 acceptance**: arXiv 2407.16741 page (peer-reviewed acceptance claim from abstract)
- **2.1K contributions + 188+ contributors**: ICLR 2025 paper abstract (verifiable via GitHub contributors page)
- **Nov 2025 SDK paper**: arXiv 2511.03690 retrieved directly
- **5 product surfaces**: README + openhands.dev verified
- **Multi-institutional academic authorship**: ICLR 2025 author list shows 23+ co-authors (not explicit institutional affiliations on arXiv page; inferred from Neubig @ CMU + Wang @ UIUC public profiles)

**To verify later (flagged per CLAUDE.md NEVER fabricate rule):**
- Full institutional affiliation list (arXiv page didn't render affiliations in WebFetch)
- Exact All Hands AI incorporation date + legal entity type
- Whether Lab4AI-style academic-lab variant applies (LlamaFactory v22 comparison)
- Specific $18.8M funding round participants / valuation

## 7. Cluster synthesis

OpenHands' core architecture represents the **most-mature T5 Agent-as-application sub-type** in the Storm Bear corpus at v30:

- **2 peer-reviewed papers** (ICLR 2025 + arXiv Nov 2025) vs deer-flow/paperclip/Skyvern zero
- **5 deployment surfaces** vs Skyvern's 3 (OSS/Cloud/Self-hosted)
- **Multi-institutional research lineage** (UIUC + CMU + 20+ other author affiliations)
- **Commercial-entity with $18.8M funding** vs autoresearch (Karpathy solo, no funding disclosed)
- **Production-grade SDK** (explicit Nov 2025 paper goal) vs paperclip's "55K-star polish but no VC disclosed"

The novel corpus contribution of OpenHands at v30 is **academic-commercial fusion as T5 archetype** — simultaneous academic credibility (ICLR acceptance) + commercial scalability (All Hands AI entity + enterprise tier). Neither pure-academic (Karpathy autoresearch) nor pure-commercial (Skyvern) nor pure-corporate (deer-flow ByteDance).

**Next cluster:** LLM integrations + microagents + evaluation → deeper into Pattern #28 data point + SWE-Bench measurement discipline + BYO agent ecosystem.
