# (C) PilotDeck — LLM Wiki

> **Subject:** `OpenBMB/PilotDeck` · **Wiki ship:** v175 · **Date:** 2026-06-20
> **Verdict:** GOAL-ALIGNED INCLUDE 3/4 — `(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG`
> **One-line:** An open-source, self-contained **"agent operating system"** organized around **per-project WorkSpace isolation** (each project gets its own filesystem + memory store + skill set), with **white-box editable/rollback memory**, **task-difficulty smart routing**, and **always-on background execution**.

---

## 1. What it is (for a beginner)

PilotDeck calls itself a *"Task-oriented AI Agent productivity platform — redefining operational boundaries and memory evolution, one WorkSpace at a time."* (tagline, verbatim from the README).

Strip the marketing and here is the concrete idea. Most AI coding/agent tools today are **one big shared chat** — every project, every task, every memory lives in the same context, and they pollute each other. PilotDeck instead gives you an **agent runtime** where the unit of work is a **WorkSpace**: open a new project, and the agent gets a *fresh, isolated* filesystem, memory store, and skill set for it. Work in WorkSpace A never bleeds into WorkSpace B. The README heading for this is **"WorkSpace-Level Isolation & Accretion"** and the explicit goal is *avoiding "global context pollution."*

It is **not** a wrapper around another agent (it is its own agent runtime), **not** an orchestrator that drives a fleet of other agents, and **not** a pluggable memory add-on for an existing CLI. It is a complete platform you run, that *uses* model providers (OpenAI, **Anthropic**, DeepSeek, Qwen, Kimi, MiniMax, or any OpenAI-compatible endpoint) underneath.

It is open source under **AGPL-3.0**, **jointly developed by Tsinghua University [THUNLP] + ModelBest + OpenBMB + AI9Stars** — i.e. a serious Chinese academic-industrial AI lab, not a weekend project. Open-sourced **2026-05-28**; first desktop build **PilotDeck Desktop v0.1.0 (June 10, 2026)**.

---

## 2. The three pillars (verbatim headings + what they mean)

### Pillar 1 — **Traceable White-box Memory**
> *"Memory generation, extraction, storage and retrieval are visible end-to-end. When AI mis-remembers, you can pinpoint and fix the offending entry."*

This is the most distinctive idea. Where the corpus's other memory engines (agentmemory v66's 4-tier auto-consolidation; supermemory v132; OpenHuman v118's memory tree) are largely **black-box** — the system decides what to remember and how — PilotDeck makes the whole memory lifecycle **visible and editable**. You can see what was remembered, find a wrong entry, and **edit or roll it back**. Paired with **Dream Mode** (below), this is "memory you can debug."

### Pillar 2 — **Smart Routing & Cost Optimization**
> *"Task difficulty is auto-detected; complex calls go to flagship models … simple ones drop to lighter models."*

A built-in router (OpenBMB's own **ClawXRouter**) classifies each call's difficulty and sends hard work to a flagship model and easy work to a cheap one. Project-stated benchmark claims:
- **~70% cost savings on social-media workloads** ($2.83 vs $12.58; 1.1× vs 5.0×).
- **1/6 the cost while *beating* frontier models on hard tasks** — a *Sonnet 4.6 + MiniMax-M2.7* routed mix scored **70.6 at $3.15** vs *Sonnet 4.6 solo* **69.1 at $18.36**.

> ⚠️ These are the project's **own, single-scenario, unreplicated** benchmarks (page-stated). Treat as a design claim, not a verified result.

### Pillar 3 — **Always-on Background Execution**
> *"After you sign off, the agent keeps discovering candidate tasks, running long-horizon monitors, and finally lands deliverables as local files."*

The agent doesn't stop when you close the window. It keeps working — discovering follow-up tasks, monitoring long-running things, and writing finished work to your local files. This is the "operating system" framing: agents are long-lived processes, not one-shot chats.

---

## 3. How it's built

- **Stack:** TypeScript **70.8%** / JavaScript **22.1%** / Python **3.8%** / Shell / HTML / CSS / Dockerfile. UI: Vite + React + Tailwind + shadcn/ui.
- **OpenBMB's own components it's built on:** **ClawXRouter** (the smart-routing layer), **ClawXMemory** (the agent-memory system), **UltraRAG** (OpenBMB's RAG framework, a separate 5.6k★ repo). Skills/tools can be pulled from **ClawHub**.
- **MCP Native** — natively supports the Model Context Protocol; it is an MCP *host/client* that consumes MCP servers and tools.
- **Extension surface:** MCP servers, custom Tools & Skills (via ClawHub), **Lifecycle Hooks** (`PreToolUse`, `UserPromptSubmit`), and **pluggable memory-store providers**.
- **Multi-frontend consistency:** Web / CLI / IM (instant-messaging) front-ends over the same backend.
- **Install paths:** (A) one-line `curl -fsSL …/install.sh | bash` (auto-installs Node.js 22, clones, builds); (B) source build (Git LFS + Node, config via `~/.pilotdeck/pilotdeck.yaml`); (C) `docker compose up -d`.
- **Links:** site `pilotdeck.openbmb.cn`; community on Discord / Feishu / WeChat.

---

## 4. Who is behind it — OpenBMB

**OpenBMB = "Open Lab for Big Model Base"** — *"aims to build foundation models and systems towards AGI."* It is the open-source umbrella over **Tsinghua University's THUNLP lab + ModelBest (面壁智能)**, with **AI9Stars** named as a co-developer here. 79 repos, including some of the most-starred Chinese OSS AI projects: **ChatDev** (33.5k★, LLM multi-agent software-dev), **MiniCPM** / **MiniCPM-V** (on-device LLM / multimodal), **VoxCPM** (TTS), **UltraRAG** (5.6k★, the RAG framework PilotDeck builds on), and historically **AgentVerse** / **XAgent** / **ToolBench**.

This is the **first OpenBMB / THUNLP-lineage subject in the 175-wiki corpus** (previously OpenBMB appeared only as the source of "MiniCPM," a model name in LlamaFactory's supported-models list). It is a *declared, well-known institutional* author — which matters for the identity criterion below.

---

## 5. Storm Bear evaluation (Phase 0.9)

**GOAL-ALIGNED INCLUDE 3/4** — `(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG`. (§31 of routine v2.6 keys the tier on **(b)**, not (a) — so an (a) FAIL with (b) STRONG ships GOAL-ALIGNED, the v168/v171/v174 shape.)

- **(a) FAIL — clean.** OpenBMB is a **major institutional AI lab** (Tsinghua THUNLP / ModelBest / AI9Stars), **not Anthropic** ((a)-7 is Anthropic-only), and a large org is not the individual *cultural-peer* axis. This is the **ByteDance v143 / NVIDIA v169 / Google v140** situation — a declared, non-Anthropic institution → FAIL, no axis. A "Chinese-origin / academic-lab" inference is **not** an (a)-rescue (the v159→v174 discipline, standing rec (ii)). The China-Mainland *academic-lab* origin (vs the prior commercial-vendor FAILs) is a **(d)/identity data-point**, not an (a) axis.
- **(b) STRONG** — this is **dead-center Goal #1** ("Master Claude and autonomous agents for software development"). It is a full **autonomous-agent OS** that natively supports Claude/Anthropic; its **white-box editable/rollback memory** lands directly on the operator's **CC-memory-systems** pilot thread (and on the vault's own 584 KB-CLAUDE.md *context-pollution* problem — exactly what WorkSpace isolation is designed to prevent); its **smart routing** lands on the **claude-api-cost-optimization** thread; it is **MCP native**. **STRONG-not-STRONGEST** because it is a *third-party* agent runtime that *uses* Claude as one of several providers — it is an alternative/complementary platform, not the Anthropic substrate itself.
- **(c) STRONG** — substantial engineered platform (TS-heavy: WorkSpace-isolation engine, white-box memory store with rollback, Dream Mode consolidation, ClawXRouter routing, ClawXMemory, MCP host, multi-frontend Web/CLI/IM, lifecycle hooks, pluggable memory providers, three install paths), built on OpenBMB's own component stack and with institutional engineering weight. Caveat: **young** — v0.1.0, 1 release, ~3 weeks open-source.
- **(d) STRONG** — exceptional connectivity: sibling to **OpenHuman v118** (self-contained agentic platform family); contrasts the memory engines **agentmemory v66 / supermemory v132 / codebase-memory-mcp v172**; distinct from the orchestration platforms **Paseo v150 / ai-maestro v163**, the multiplexers **cmux v99 / AoE v162**, and the GUI client **CodePilot v161**; a genuine **Pattern #57** corpus-recursive cross-reference (the README explicitly thanks *"Agent OS pioneers such as OpenClaw, Claude Code, Codex, Cursor, and Hermes"*); MCP / Dream-Mode-consolidation / cost-routing threads.

### Pattern outcome
**1 NEW Library-vocab §C standalone (CORPUS-FIRST, N=1):** *"Open-Source Self-Contained Agent OS Organized Around Per-Project WorkSpace Isolation (isolated filesystem + memory store + skill set per project) with White-Box Editable/Rollback Memory."* See the PRIMARY doc in `01 Analysis/` for the full distinction-from-neighbors argument.

**Secondary observations (NOT minted):** Pattern #57 corpus-recursive cross-reference (pioneer-acknowledgment of Claude Code / Codex / Cursor / OpenClaw / Hermes); smart-routing = cost-optimization + Library-vocab #20 Token-Economy-Quantification QUALIFIED-ADJACENT (page-stated single-scenario, N stays 4 — the v168/v172 precedent); MCP-host consumer-side cross-ref; #19 19a institutional-org portfolio data-point (first OpenBMB subject); #66 supply-chain/privacy cross-ref (`curl|bash` install + local-first memory); Dream-Mode ↔ memory-consolidation echo (cf. the leaked `tengu_onyx_plover` Dream-Task).

**Non-claims:** NOT a new top-level pattern (max #85); NOT #52 (3.6k★/364 forks/v0.1.0/1 release page-stated, **NOT API-verified** §37.4 → velocity unestablishable); NOT #18 B1-MCP (it's an MCP *host*, not a one-server-many-clients distribution); NOT an orchestration platform (#23 — it's its own single runtime, not an orchestrator of third-party agents); NOT a multiplexer / GUI client / pluggable memory engine. **Counts UNCHANGED 46/10.**

---

## 6. Pilot note — study the design first

PilotDeck is **strongly on-goal** for the operator's two live threads:
- **CC-memory-systems** — its white-box, *editable, rollback-able* memory + per-WorkSpace isolation is a **reference design** for the exact problem this vault hit (the 584 KB CLAUDE.md context-pollution refactor). The biggest value is *studying the architecture*, not necessarily adopting the runtime.
- **claude-api-cost-optimization** — its task-difficulty smart routing is a concrete instance of the cost-routing idea.

**But the footprint is heavy** (it's a whole agent OS, not a small tool), it is **young** (v0.1.0, ~3 weeks old, 1 release), the install is **`curl|bash`**, and the license is **AGPL-3.0** (copyleft — relevant if ever integrated into hireui). 

**Fence:** `install-snapshot` first → inspect `install.sh` → run via **Docker-compose-isolated** or on a scratch machine, **not** the vault host → study the **WorkSpace-isolation + white-box-memory design** as a memory-architecture reference → pin the commit (v0.1.0). It sits *outside* the existing 5-rung pilot ladder (SkillSpector → claude-tap → Agent-Reach → codebase-memory-mcp → devspace): those are tools you bolt onto Claude Code; PilotDeck is an *alternative runtime* — so treat it as a **"study the design" pilot**, not an "adopt it" pilot.

---

## 7. Sources & provenance (§37)

- Tagline, three pillars, WorkSpace isolation, Dream Mode, MCP, providers, cost claims, AGPL, joint-development — **stated**, `github.com/OpenBMB/PilotDeck` README + `raw.githubusercontent.com/.../README.md` (WebFetch, 2026-06-20).
- 3.6k★ / 364 forks / v0.1.0 (Jun 10 2026) / 1 release / TS 70.8% — **stated, NOT API-verified** (§37.4: this environment mocks the GitHub API). ~3.6k★ in ~23 days ≈ ~156★/day is **page-implied only → NOT a Pattern #52 claim.**
- OpenBMB identity (THUNLP / ModelBest / AGI mission / 79 repos / ChatDev / MiniCPM / UltraRAG) — **high** (org page WebFetch + README + well-known).
- Cost/benchmark figures (~70%, 1/6) — **stated** (project's own unreplicated single-scenario benchmark; explicitly *not* independently verified).
- Corpus collision/identity claims (first OpenBMB subject; OpenHuman v118 anchors no standalone; no existing agent-OS standalone) — **independently verified** by grep over `_state/` + `_patterns/` and 2× WebFetch (per the `feedback_wiki_verify_independently_check_collisions` discipline).

---

*Built inline with independent collision/identity verification (the v171 inline precedent + the wiki-verify memory). Full criterion reasoning in `01 Analysis/(C) Phase-0.9 verdict — GOAL-ALIGNED INCLUDE 3of4.md`; the corpus-first standalone argument in `01 Analysis/(C) PRIMARY — agent-OS-workspace-isolation standalone N1.md`.*
