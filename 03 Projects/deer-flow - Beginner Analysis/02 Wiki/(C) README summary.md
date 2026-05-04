# (C) README summary — deer-flow

> Nguồn: `README.md` (38 KB, fetched via raw.githubusercontent.com 2026-04-18)
> Repo: `bytedance/deer-flow`

## TL;DR

**deer-flow (v2.0)** = **open-source SuperAgent harness** cho long-horizon autonomous tasks. ByteDance-backed. 62K stars (2nd largest in corpus). Architecture: Sandbox + Memory + Skills + Sub-agents + Message Gateway. Python backend + Next.js frontend. Self-hosted. **Runs tasks minutes to hours**, not interactive seconds. **Complementary với Claude Code** (OAuth invocation both ways). **First Tier 5 "Agent-as-application" entrant in Storm Bear corpus.** Category peer: Devin (closed), AutoGPT (older), OpenHands (parallel OSS).

## Positioning / framing

- **Tagline:** "A super agent harness that orchestrates sub-agents, memory, and sandboxes through extensible skills. Do almost anything powered by a comprehensive toolkit."
- **Problem statement:** Agents need more than conversation — need execution, memory, multi-step coordination for real workflows (data pipelines, presentations, research).
- **Audience:** Researchers, developers automating content/data, teams building agent apps, organizations needing local + auditable AI execution.
- **Deployment model:** Self-hosted (local trusted-network recommended; production needs auth gateways + IP allowlists).
- **License:** MIT.

## Architecture Overview

### 5 Core Components

1. **Sandbox Environment** — Isolated execution (Docker containers or local filesystem). Agents read/write files within boundaries without system-wide access.
2. **Memory System** — Persistent long-term memory. Tracks user preferences, profiles, workflows across sessions.
3. **Skills Framework** — Markdown-based modular capabilities (research, report gen, slide creation, web ops). **Progressive loading** to conserve context.
4. **Sub-Agent System** — Lead agents spawn parallel sub-agents. Each sub-agent = isolated context tackling decomposed task segment.
5. **Message Gateway** — Multi-channel integration: Telegram, Slack, Feishu, WeChat, WeCom.

### Layered architecture (from CONTRIBUTING)

```
Browser → Nginx (port 2026) → Frontend (3000) / Gateway API (8001) / LangGraph Server (2024)
```

- **Frontend:** TypeScript/Next.js
- **Gateway API:** Python backend (domain logic)
- **LangGraph Server:** Agent orchestration engine
- **Nginx:** Reverse proxy routing `/api/langgraph/*` to agents, other `/api/*` to Gateway

## Capabilities

- **Deep research** with multi-angle exploration
- **Report + presentation generation** với visuals
- **Web content creation + modification**
- **Code execution + generation**
- **File operations + workspace management**
- **Image/video generation + analysis**

## Installation

```bash
# Interactive wizard
make setup    # guides LLM provider + search + sandbox config

# Docker (recommended)
make docker-init
make docker-start

# Local dev
make check    # detects missing deps: node, pnpm, uv, nginx
make install
make dev
```

Access: `http://localhost:2026` (Nginx unified entry).

## UI / Frontend

Web interface provides:
- Task submission
- Model selection
- Thread management
- Memory review
- Skill configuration
- Artifact viewing

→ **Full web app, not CLI tool.** Distinct from T1 siblings (all CLI + skill-based).

## Comparisons (from README)

### vs Devin/AutoGPT/CrewAI
deer-flow emphasizes:
- Orchestrated sub-agent parallelization
- Persistent memory integration
- Multi-channel deployment
- (vs focused coding assistance or workflow templates)

### vs Claude Code
**Complementary relationship:**
- DeerFlow can invoke Claude Code via OAuth
- Claude Code can invoke DeerFlow through `claude-to-deerflow` skill
- → Interoperability designed-in, not adversarial

**Implication for Storm Bear:** Can use BOTH. Claude Code for interactive dev (T1), deer-flow for long-horizon autonomous tasks (T5).

## Model Provider Support

Agnostic — any OpenAI-compatible API.

**Recommended capability profile:**
- 100k+ token context windows
- Reasoning capabilities
- Strong tool-use

**Explicitly supported:**
- GPT-4 (OpenAI)
- Gemini (Google)
- Qwen (Alibaba)
- Doubao (ByteDance's own)
- DeepSeek
- Kimi (Moonshot)

→ **Chinese LLM support strong** (Qwen, Doubao, DeepSeek, Kimi) — unlike ECC/Superpowers siblings Claude-focused.

## Headline Features (5)

1. **Parallel Sub-Agents** — fan out → synthesize
2. **Isolated Execution** — filesystem + optional containerized bash with security boundaries
3. **Progressive Skill Loading** — context-aware loading keeps windows lean
4. **Persistent Memory** — cross-session learning + preference retention
5. **Multi-Channel Integration** — native IM support (Slack, Telegram, WeChat, etc.)

## Performance Claims

- Reached **#1 GitHub Trending** following v2.0 launch (February 2026)
- Designed để handle tasks **spanning minutes to hours** through distributed sub-agent execution
- **Batteries-included** extensibility without framework boilerplate

## Version / Stability

- **v2.0** (current) — rebuilt from scratch, no shared code với v1
- Active development (pushed today 2026-04-18)
- MIT license — permissive
- ByteDance maintained — sustainability stronger than solo maintainers

## Unique positioning vs 8 siblings

| Axis | deer-flow | T1 Claude Code tools | T2 goclaw | T3 course | T4 notebooklm-py | Outside build-your-own-x |
|------|-----------|----------------------|-----------|-----------|------------------|--------------------------|
| **Form factor** | Standalone app | Skill/plugin | Platform | Curriculum | Library | Aggregator |
| **Consumer verb** | Run | Use | Deploy | Learn | Integrate | Study |
| **Task duration** | Minutes-hours | Interactive | Platform ops | Curriculum-paced | Per-integration | Open-ended |
| **Autonomy level** | High (autonomous) | Low (user-directed) | Platform manages | N/A | Per-call | N/A |
| **UI** | Web interface | CLI | Web + API | Static docs | CLI + lib | Single README |
| **Interaction model** | Submit task, wait | Conversation | API calls | Read+code | Invocation | Read |

→ **deer-flow occupies new category** = Standalone autonomous agent app. Not comparable to siblings on same axis. **Tier 5 "Agent-as-application" proposed.**

## Meta-relevance to Storm Bear vault

### Direct uses
1. **Storm Bear research automation** — deer-flow's deep-research + report gen could replace manual routine wiki research phase
2. **Scrum retro synthesis** — deer-flow analyzes multiple retros, generates team-health report
3. **Coaching pipeline** — Scrum coach queries → deer-flow runs multi-hour research → Storm Bear receives structured output

### Complementary với Claude Code
- Morning: Claude Code (interactive dev) — ECC, Superpowers, gstack, GSD workflow
- Afternoon: deer-flow (long tasks) — async research, report generation
- Evening: Claude Code (review deer-flow outputs)

### Meta-pattern cho vault
- **Skills framework ≈ Storm Bear's `05 Skills/`** — both Markdown-based skill abstractions
- **Progressive loading** = lesson Storm Bear could apply (load routine docs lazy)
- **Sub-agent parallelization** ≈ potential Storm Bear routine enhancement (parallel source fetch)

## Risks / watchouts

- **LangGraph lock-in** — deer-flow deep uses LangGraph; framework shifts = impact
- **Multi-channel attack surface** — 5 IM platforms = security exposure if misconfigured
- **Cost multiplier** — parallel sub-agents = N× LLM calls per task (deer-flow doesn't manage cost internally)
- **Self-hosting ops burden** — Nginx + backend + frontend + sandbox = complex deploy (not serverless)
- **Autonomous risk** — long-horizon agents can go off-rails; need monitoring
- **Memory leakage** — persistent memory = privacy concern if multi-user misconfigured

## Open questions (→ `01 Analysis/(C) open questions.md`)

1. ByteDance strategic intent
2. v1 → v2 migration
3. LangGraph lock-in
4. Devin feature parity
5. Cost control
6. Skill marketplace future

## Sources list (for Phase 2 ingestion)

- README.md (this summary) — 38 KB
- Install.md — setup flows
- CONTRIBUTING.md + config.example.yaml — architecture + dev workflow

## Cross-references

- Sibling summaries:
  - 4 T1 agent-assistant (ECC, Superpowers, gstack, GSD)
  - 1 T2 service (goclaw)
  - 1 T3 education (course)
  - 1 T4 bridge (notebooklm-py)
  - 1 outside-scope (build-your-own-x)
- Proposed same-tier candidates (future):
  - OpenHands, AutoGPT, CrewAI, Agent Zero, Cognition Devin OSS-alt
