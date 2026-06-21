# (C) PRIMARY — v175 PilotDeck — New §C Standalone (CORPUS-FIRST, N=1)

**Standalone (filed to Library-vocab registry §C):**

> **"Open-Source Self-Contained Agent OS Organized Around Per-Project WorkSpace Isolation (isolated filesystem + memory store + skill set per project) with White-Box Editable/Rollback Memory"** — N=1, anchor **v175 PilotDeck (`OpenBMB`)**.

**Status:** CORPUS-FIRST. PROMOTION-ELIGIBLE at N=2. Time-aware stale-watch (≥15 wikis AND ≥30 days, §39).

---

## The defining axis (the CONJUNCTION that is corpus-first)

A **self-contained agent runtime/OS** (not a wrapper, not an orchestrator, not a plug-in) whose **primary organizing primitive is the per-project WorkSpace** — each project gets its *own isolated filesystem + memory store + skill set* ("WorkSpace-Level Isolation & Accretion … avoiding global context pollution") — **combined with white-box memory** whose generation/extraction/storage/retrieval is *visible end-to-end and editable*, supporting *pinpoint-and-fix of a wrong entry* and *one-click rollback* (Dream Mode consolidates in idle windows).

Two of these axes are *each* corpus-first, and their conjunction is the mint:
1. **Per-project WorkSpace isolation as the central primitive** — no prior corpus subject organizes an agent around *isolated-per-project* filesystem+memory+skills.
2. **White-box editable/rollback memory** — no prior corpus memory subject makes the memory lifecycle *visible, editable, and rollback-able* as its headline (the others are auto-consolidating black boxes).

The supporting pillars (task-difficulty **smart routing**, **always-on background execution**) each have corpus precedent *as features of other subjects*, so they are **not** part of the novel-conjunction claim — they are recorded as adjacencies (below). The mint centers on **WorkSpace-isolation + white-box memory**.

---

## Distinction from every near-neighbor (the anti-"generalize-to-fit" pass)

| Neighbor | What it is | Why PilotDeck is DISTINCT |
|---|---|---|
| **OpenHuman v118** (closest cousin) | Self-contained agentic *desktop assistant*; ingests personal/work life (118 services) into a *unified persistent memory tree* (Karpathy-LLM-wiki) | Same *family* (self-contained agentic platform + own memory + routing + background). **Different organizing primitive:** OpenHuman = ONE unified personal memory tree across all of life; PilotDeck = MANY isolated per-project WorkSpaces. OpenHuman ingests *services*; PilotDeck isolates *projects*. **OpenHuman anchors NO §C standalone** (it minted zero) → minting PilotDeck's WorkSpace-isolation axis erases no prior priority. |
| **agentmemory v66 / supermemory v132 / codebase-memory-mcp v172** | Dedicated memory engines / MCP servers that **plug into existing agents** | PilotDeck is a *full platform*, not a pluggable backend. Its memory is **white-box (visible/editable/rollback)** vs agentmemory's 4-tier *auto*-consolidation (black-box), supermemory's benchmark, codebase-memory-mcp's read-only code graph. |
| **Paseo v150 / ai-maestro v163** (§C #23 — Multi-Vendor Orchestration Platform) | Orchestrate *multiple heterogeneous third-party agents* (Claude Code/Codex/Aider…) as the orchestration UNITS | PilotDeck is its **own single agent runtime** — it does not run other agents as units; it *uses* model *providers* underneath. Orchestrator vs runtime. |
| **cmux v99 / AoE v162** (session-multiplexer species) | HOST human-driven sessions of *other* coding-agent CLIs (tmux/worktrees) | PilotDeck is the agent itself, not a multiplexer of other agents' sessions. |
| **CodePilot v161** (§C #27 — Desktop GUI Client for a CLI agent) | A GUI that **wraps a CLI coding agent** (Claude Code) so you operate it visually | PilotDeck is its **own runtime**, not a front-end over another agent's CLI. |
| **Pattern #18 #8 Multi-Source LLM Aggregator** | Routes/aggregates LLM *providers/sources* | PilotDeck's ClawXRouter routes by **task difficulty for cost** *inside* the platform — adjacent (a feature), not the mint. |

**No existing "agent OS" / "WorkSpace-isolation" / "white-box-memory" standalone exists in §C** (verified by grep). Corpus-first stands.

---

## Secondary observations — filed at their own layers, NOT minted

- **Pattern #57 corpus-recursive cross-reference (genuine):** README thanks *"Agent OS pioneers such as OpenClaw, Claude Code, Codex, Cursor, and Hermes for their explorations."* This is an explicit *influence-acknowledgment* of corpus subjects — stronger than the recent "mentions ≠ recursion" cases (v172/v173/v174, where subjects were named only as *clients/targets*). A real #57 data-point; **NOT a promotion** (a generic acknowledgment, not deep methodology-recursion like OpenHuman's Karpathy citation).
- **Library-vocab #20 Token-Economy-Quantification — QUALIFIED-ADJACENT, N stays 4.** The ~70% / 1/6-cost claims quantify token/cost impact, but are **page-stated, single-scenario, unreplicated** → the v168 ponytail / v172 codebase-memory-mcp precedent (bump DEFERRED, recorded as a qualified instance).
- **MCP host / consumer-side cross-reference** (#18 / #22 consumer flavor): consumes MCP servers + ClawHub skills + lifecycle hooks. **NOT** the #18 B1-MCP one-server-many-clients distribution shape.
- **Pattern #19 19a institutional-org portfolio data-point:** first OpenBMB / THUNLP / Tsinghua-lineage subject; OpenBMB = 79 repos (ChatDev, MiniCPM, VoxCPM, UltraRAG, AgentVerse, XAgent). Richer/heavier than the recent bare-handle authors — an *institutional* data-point.
- **Pattern #66 supply-chain / privacy cross-reference:** one-line `curl -fsSL …/install.sh | bash` (auto-installs Node 22) = supply-chain attack-surface note + the pilot fence; offset by local-first WorkSpace memory (privacy-positive) + Docker-compose option.
- **Dream-Mode ↔ memory-consolidation echo:** idle-window memory consolidation echoes the leaked Claude `tengu_onyx_plover` "Dream-Task background memory consolidation" (corpus, `_state/03a`) + agentmemory's Ebbinghaus-decay consolidation. A connectivity note.

---

## Non-claims (anti-inflation guardrails)

- **NOT a new top-level pattern** (max stays #85; same anti-inflation that rejected #86/#88 at v168/v169).
- **NOT Pattern #52** — 3.6k★ / 364 forks / v0.1.0 / 1 release / open-sourced 2026-05-28, **all page-stated, NOT API-verified (§37.4)** → velocity unestablishable. ~156★/day page-implied is *suggestive only*, not a claim.
- **NOT #18 B1-MCP** (MCP host/consumer, not a server distributed to many clients).
- **NOT §C #23** (orchestration platform — it does not orchestrate third-party agents as units).
- **NOT** the session-multiplexer species (cmux/AoE), the GUI-client standalone (CodePilot §C #27), or a pluggable memory engine (agentmemory/supermemory/codebase-memory-mcp §C #32).
- **NOT N=2 of OpenHuman v118** — OpenHuman is a *family cousin* with a different organizing primitive and anchors no standalone; PilotDeck's WorkSpace-isolation axis is genuinely first.
- **Counts UNCHANGED: 46 / 10.** §C surface ≈32 → ≈33 (+1 N=1).
