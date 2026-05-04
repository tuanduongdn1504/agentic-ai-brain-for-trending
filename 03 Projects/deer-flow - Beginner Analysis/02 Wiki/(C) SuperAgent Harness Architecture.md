# (C) SuperAgent Harness Architecture

> Entity page — Architecture concept
> Sources: README architecture section + CONTRIBUTING layered diagram
> Format: 13-section canonical

## 1. What is it / Nó là gì

**SuperAgent Harness Architecture** = layered full-stack system supporting long-horizon autonomous agent execution. Unlike T1 Claude Code plugins (run inside Claude Code process), deer-flow is **standalone app** với own UI + orchestrator. 5 core components (Sandbox/Memory/Skills/Sub-agents/Gateway) + 4-port layered deployment (Nginx/Frontend/Gateway/LangGraph).

## 2. Why it matters / Sao quan trọng

### Long-horizon tasks need infrastructure

Interactive Claude Code sessions = seconds-to-minutes, conversation-paced, user-guided.
deer-flow autonomous tasks = minutes-to-hours, workflow-paced, goal-guided.

**Long tasks require:**
- **Persistent state** (session can span days)
- **Resumability** (recover from crashes)
- **Isolation** (agents shouldn't crash each other)
- **Observability** (user checks progress)
- **Cost control** (parallel sub-agents multiply LLM spend)

→ **Architecture supports these.** Not optional for autonomous long-horizon.

## 3. 5 Core Architectural Components

### Component 1: Sandbox Environment
- **What:** Isolated execution contexts
- **How:** Docker containers OR local filesystem
- **Why:** Agents run arbitrary code; containment prevents system damage
- **Security boundary:** Read/write confined to workspace

### Component 2: Memory System
- **What:** Persistent long-term memory
- **Tracks:** user preferences, profiles, workflows
- **Scope:** Cross-session (survives restarts)
- **Implementation:** Not detailed publicly (likely vector DB or structured store)

### Component 3: Skills Framework
- **What:** Modular Markdown-based capability definitions
- **Examples:** research, report generation, slide creation, web operations
- **Progressive loading:** skills load when context needs them
- **Why progressive:** conserves context window (100k+ token models still have limits)

### Component 4: Sub-Agent System
- **What:** Lead agents spawn parallel sub-agents
- **Pattern:** Fan-out (decompose task) → parallel execute (isolated contexts) → synthesize (merge results)
- **Benefit:** throughput + specialization

### Component 5: Message Gateway
- **What:** Multi-channel integration
- **Supports:** Telegram, Slack, Feishu, WeChat, WeCom
- **Why:** users submit tasks from IM apps instead of needing web UI open

## 4. Layered deployment architecture

```
┌──────────────────────────────┐
│ Browser / IM App             │
└──────┬───────────────────────┘
       │ HTTP/WS
┌──────▼───────────────────────┐
│ Nginx (port 2026)            │ ← Unified entry, routing
└─┬─────────┬──────────┬───────┘
  │ /       │ /api/*   │ /api/langgraph/*
  ▼         ▼          ▼
┌────────┐ ┌──────────┐ ┌─────────────┐
│Frontend│ │Gateway API│ │LangGraph    │
│Next.js │ │Python    │ │Server       │
│:3000   │ │:8001     │ │:2024        │
└────────┘ └──────────┘ └──────┬──────┘
                               │
                               ▼
                     ┌─────────────────┐
                     │ Sandbox         │
                     │ (Docker/FS)     │
                     └─────────────────┘
                     ┌─────────────────┐
                     │ Memory Store    │
                     └─────────────────┘
                     ┌─────────────────┐
                     │ LLM Providers   │
                     │ (GPT/Gemini/etc)│
                     └─────────────────┘
```

## 5. Port + service responsibilities

| Port | Service | Language | Purpose |
|------|---------|----------|---------|
| 2026 | Nginx | - | Reverse proxy, single entry |
| 3000 | Frontend | TypeScript | Web UI (Next.js) |
| 8001 | Gateway API | Python | Domain REST API |
| 2024 | LangGraph Server | Python | Agent orchestration engine |

### Why 4 services không 1?

- **Dev velocity:** frontend team iterates without backend redeploy
- **Tech fit:** TS ecosystem for UI, Python for agents (LangGraph native)
- **Scale differently:** frontend static, backend compute-intensive
- **Language boundary clarity:** Python can't easily do Next.js SSR

## 6. Nginx as single entry

### Routing rules

- `/api/langgraph/*` → LangGraph Server :2024 (agent tasks)
- Other `/api/*` → Gateway API :8001 (domain logic)
- Everything else → Frontend :3000 (UI assets)

### Why unified entry
- Single URL user bookmarks (`http://localhost:2026`)
- SSL termination at 1 point (production)
- Rate limiting at 1 point
- Auth future-proofed at 1 point

## 7. Example request flow

User submits task "Research quantum computing, write report":

1. **Browser** POSTs to `http://localhost:2026/api/langgraph/run`
2. **Nginx** routes to LangGraph Server :2024
3. **LangGraph** identifies research + report tasks, spawns 2 sub-agents
4. **Sub-agent A** (research): loads research skill from `skills/public/research.md`
5. **Sub-agent A** calls LLM API với research tools (web search), writes notes to sandbox
6. **Sub-agent A** marks complete, returns research notes
7. **Sub-agent B** (report): loads report gen skill, reads research notes from sandbox
8. **Sub-agent B** calls LLM to write report, writes final output to sandbox
9. **Lead agent** synthesizes, returns artifact to Gateway API
10. **Gateway API** persists in memory + returns to Frontend
11. **Frontend** displays artifact to user, downloads available

Total time: 15-60 minutes depending on research depth.

## 8. Trade-offs / Limitations

### Strengths
- **Long-horizon capable** — architecture designed for hours-long tasks
- **Isolated sub-agents** — one agent crash ≠ all crash
- **Multi-channel accessible** — IM + web UI
- **Model-agnostic** — any OpenAI-compatible API
- **Open-source MIT** — self-hostable

### Weaknesses
- **Ops complexity** — 4 services + Nginx + Docker = significant deploy overhead
- **Single-tenant bias** — not designed as multi-tenant SaaS (goclaw T2 fills that)
- **Cost unpredictable** — parallel sub-agents × long tasks = expensive
- **Self-hosting burden** — monitoring, scaling, upgrades = user's job
- **LangGraph dependency** — framework shifts impact architecture

## 9. Comparison to sibling architectures

| Sibling | Architecture |
|---------|--------------|
| **ECC (T1)** | Plugin in Claude Code process (lightweight) |
| **Superpowers (T1)** | Skills library in Claude Code |
| **gstack (T1)** | Specialist roles + sprint pipeline in Claude Code |
| **GSD (T1)** | Commands + agents via harness |
| **goclaw (T2)** | Multi-tenant Go platform |
| **course (T3)** | Static curriculum |
| **notebooklm-py (T4)** | 4-layer Python library |
| **build-your-own-x (outside)** | Single README aggregator |
| **deer-flow (T5)** | **Layered full-stack app (4 services)** |

### Complexity ranking (deployment complexity)
1. build-your-own-x = lowest (just a README)
2. course = low (git clone + Jupyter)
3. ECC/Superpowers/gstack/GSD = low-medium (skill install)
4. notebooklm-py = medium (pip install + login)
5. goclaw = high (Go binary + multi-tenant config)
6. **deer-flow = highest** (frontend + backend + orchestrator + proxy)

→ **deer-flow = most complex architecture.** Justified by ambition (long-horizon autonomous) but raises deployment bar.

## 10. Common pitfalls

1. **Running without Docker** — local setup requires node + pnpm + uv + nginx; easy to miss dep
2. **Port conflicts** — 2026/3000/8001/2024 need to be free
3. **Nginx misconfigured** — routes break silently; user sees frontend but API fails
4. **Memory persistence loss** — if volume not mounted in Docker, memory wipes on restart
5. **Sandbox escape attempts** — autonomous code execution + weak sandbox = security risk
6. **Cost explosion** — parallel sub-agents + long task + expensive model = surprise bill
7. **Skill loading bugs** — if skill load fails, sub-agent silently underperforms

## 11. When NOT to adopt deer-flow architecture

- **Short interactive tasks** — Claude Code (T1) better for minutes not hours
- **Simple automation** — cron + script simpler than SuperAgent
- **Multi-tenant SaaS needs** — goclaw (T2) designed for that
- **Learning AI agents** — course (T3) better for concepts
- **Specific service integration** — T4 bridges more efficient for single service

## 12. Storm Bear vault relevance

### Could deer-flow run Storm Bear routine?

**Conceptually yes:**
- Routine = autonomous long task (1-2 hours per wiki)
- Routine researches + synthesizes + writes
- deer-flow handles exactly this class

**Implementation considerations:**
- Port `05 Skills/llm-wiki-routine.md` → deer-flow Skill (Markdown)
- deer-flow's research skill ≈ vault's Phase 2 source ingestion
- deer-flow's report gen ≈ vault's Phase 4a published guide
- Sub-agent parallelization could speed routine (parallel source fetch)

### Could Storm Bear adopt deer-flow's architecture concepts?

- **Progressive skill loading** — lesson: don't front-load all of vault into Claude context
- **Sub-agent pattern** — potential routine enhancement (parallel entity pages)
- **Memory persistence** — vault already has this implicitly (Obsidian filesystem)
- **Multi-channel gateway** — vault currently Obsidian-only; could add Telegram/Zalo bridge

### Comparison: Storm Bear routine vs deer-flow workflow

| Aspect | Storm Bear routine | deer-flow |
|--------|-------------------|-----------|
| Duration | ~2h | Minutes to hours |
| Autonomy | Claude Code session | Fully autonomous |
| User interaction | Continuous (Claude visible) | Submit task, wait |
| Output | Wiki files in Obsidian | Artifacts in sandbox |
| Infrastructure | None (Claude Code) | Nginx + Frontend + Gateway + LangGraph |

**Storm Bear routine = T1 + LLM Wiki pattern specialization.**
**deer-flow = T5 generic autonomous harness.**

Both valid. Different paradigms.

## 13. References / Nguồn

- Source: [[(C) README summary]] (5 components) + [[(C) Architecture + Contributing cluster summary]] (layered diagram)
- Related entities:
  - [[(C) Skill System (Progressive Loading)]]
  - [[(C) Sub-Agent System (Parallel Fan-out)]]
  - [[(C) Message Gateway (Multi-Channel)]]
- Sibling architectures:
  - `../../goclaw - Beginner Analysis/02 Wiki/(C) Multi-Tenant Architecture.md` (T2)
  - `../../notebooklm-py - Beginner Analysis/02 Wiki/(C) Python API Architecture.md` (T4)
