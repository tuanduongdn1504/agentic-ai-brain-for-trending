# Odysseus — Wiki (v132)

> `pewdiepie-archdaemon/odysseus` · **"Self-hosted AI workspace."** · *"Your own AI workspace, running on your hardware — local-first, privacy-first, and no telemetry. Just you and your models."* · PewDiePie's open-sourced **"ChatOS"**: a self-hostable ChatGPT/Claude-style workspace with autonomous MCP agents, a hardware-aware model Cookbook, Deep Research, and a **self-evolving skills** system.

**(C) Claude-generated wiki page.** Fetched 2026-06-01 (GitHub API + recursive tree + key source files + landing page + HN + press). Routine **v2.6, wiki #132** (renumbered from v131 — a concurrent **v131 `harness`** ship took v131 on a parallel branch); carries the §33 tier-tag. Phase 0.9: **GOAL-ALIGNED INCLUDE** — (a) FAIL (Swedish creator), (b) **STRONG**, (c)(d) STRONG. The breached §35 off-goal-rate ceiling (v127/v128/v129 all off-goal) was remedied by the concurrent v131 harness ship; **Odysseus-v132 is the 2nd consecutive goal-aligned ship → it CLEARS the §35 rolling-3 window** (v129 OG · v131 GA · v132 GA = 1 OG ≤ ceiling), cleanly, no override. Tier-1 pilotable.

---

## Identity

| Field | Value |
|---|---|
| Repo | [`pewdiepie-archdaemon/odysseus`](https://github.com/pewdiepie-archdaemon/odysseus) |
| What | **Self-hosted AI workspace** — multi-model chat + autonomous MCP agents + Cookbook + Deep Research + self-evolving Skills + memory + email/calendar/notes |
| Tier / archetype | **T2 Service / Self-Hosted AI-Agent Workspace** (run-it-yourself app) + autonomous-agent harness + MCP host + agent-memory/skills system |
| Stars / forks | **11,771★ / 1,538 forks** (fork_ratio ~0.13) |
| Subscribers / open issues | 117 / 161 |
| Created / pushed | **2026-05-31** / 2026-06-01 (**~1 day old**, pushed today) |
| Velocity | **~11,771★/day → EXTREME-VIRAL** — ⚠️ **audience-driven** (PewDiePie's ~110M audience), NOT organic dev signal; a Pattern #52/#82 caveat specimen, **NOT** a velocity promotion |
| License | **MIT** |
| Language | **JavaScript ~49% / Python ~37%** (FastAPI backend + vanilla-JS PWA frontend) |
| Serves on | **:7000** (mobile-responsive PWA); deploy via Docker Compose or bare-metal Python 3.11+ |
| Default branch / homepage | `main` / [pewdiepie-archdaemon.github.io/odysseus](https://pewdiepie-archdaemon.github.io/odysseus/) |
| Author | **`pewdiepie-archdaemon` = Felix Kjellberg ("PewDiePie")** — Swedish creator (~110M+ subs); 2025 self-hosting-AI arc (10-GPU rig, "ChatOS"/"Swarm") |
| Launch video | *"MY trillion $Dollar Project is finally OUT!"* — https://www.youtube.com/watch?v=rAzT5lcezPs |
| Wiki # | **v132** (renumbered from v131; concurrent v131 = `harness`, parallel branch) |

## What it is

The open-sourced, productized form of PewDiePie's home-built **"ChatOS"** — *"the self-hosted version of the UI experience you get from ChatGPT and Claude."* The arc behind it (documented by Tom's Hardware, TechReport, BigGo, wccftech): a ~10-GPU home rig (8× modded RTX 4090 48 GB ≈ 256 GB VRAM) running Qwen-235B / Llama-70B / GPT-OSS-120B via **vLLM**; a multi-model **"Council"** that votes on responses (and famously showed *emergent "collusion"*); then **"The Swarm"** (~64 small 2B models). Odysseus is the cleaned-up product.

**Modules:**
- **Chat** — local (vLLM · llama.cpp · Ollama) + remote (OpenRouter · OpenAI) multi-model.
- **Agent** — *"hand it tools and let it run the whole task."* Built on **opencode**; over **MCP** + web + files + shell + skills + memory. Streaming multi-round loop (`src/agent_loop.py`): the LLM calls tools by writing fenced code blocks (+ function-call fallback), capped at `MAX_AGENT_ROUNDS`, with **prompt-injection defense** + **per-owner tool gating** (`tool_security.py`).
- **Cookbook** — built on **llmfit**: scans hardware → computes VRAM fit → recommends/serves from **270+ models** (GGUF / FP8 / AWQ).
- **Deep Research** — adapted from **Alibaba Tongyi DeepResearch** (Apache-2.0): multi-step gather→read→synthesize into cited reports.
- **Memory / Skills** — ChromaDB + fastembed (ONNX) vector+keyword memory; **self-evolving Skills** (see below).
- **Compare** (blind side-by-side), **Email** (IMAP/SMTP + AI triage), **Calendar** (CalDAV), Notes/Tasks/Reminders, Document editor, Image gallery.

**⭐ Self-evolving Skills** (`services/memory/skill_*.py`) — the standout: skills are **Hermes-lineage `SKILL.md`** files (frontmatter `name/description/version/category/tags/status/confidence/source[learned|taught|imported]/teacher_model`; body *When to Use / Procedure / Pitfalls / Verification*). After any run with **≥2 rounds or ≥2 tool calls**, an LLM *conservatively* auto-distills a reusable skill (`MIN_CONFIDENCE=0.6`); usage counters + confidence-gated eviction. **The agent writes, refines, and evicts its own skills.**

**Built on (honest `ACKNOWLEDGMENTS.md`):** opencode (MIT, agent loop) · llmfit (MIT, Cookbook) · Tongyi DeepResearch (Apache-2.0, Deep Research) · Docker-composed unmodified: SearXNG (AGPL-3.0) + ChromaDB (Apache-2.0) + ntfy · MCP SDK (MIT). **Security** (`SECURITY.md`): documented + responsible — *"do not run it as a public, unauthenticated service"*; `AUTH_ENABLED=true`; high-risk tools (shell/Python/file/email/MCP/serving) admin-gated; 2FA; a fork-publishing secret-scan checklist.

## Why it's in the corpus

**GOAL-ALIGNED INCLUDE** (v2.6 §31 tier — (b) PASSes, so this is the corpus's core, not an off-goal capture):
- **(a) FAIL** — PewDiePie = Swedish creator, not a cultural-peer, not (a)-7. Honest fail, no (a)-rescue.
- **(b) STRONG** — directly goal-#1: a runnable + studyable autonomous-agent workspace (opencode-adapted agent loop, MCP, self-evolving skills, memory). MODERATE-cost reversible × DIRECT = STRONG (not STRONGEST — a heavy self-hosted workspace to run/study, not a drop-in vault tool).
- **(c) STRONG** — instructive reference architecture; the self-extracting skills system + honest attribution + documented security are real teaching material.
- **(d) STRONG** — opencode (v67/v99), Hermes skill-format (v78/v82/v112), agentmemory v66 / ChromaDB, MCP cluster (v66/v70/v76), Pattern #18/#84 multi-provider, DeepSeek/Qwen (v72), Tongyi deep-research (v9/v79), **v118 OpenHuman sibling**, **v131 harness** concurrent sibling.

**§35 ceiling:** breached (v127/v128/v129 all off-goal); the concurrent **v131 harness** ship (GOAL-ALIGNED) was the goal-aligned "next ship" that remedied it. **v132 Odysseus is the 2nd consecutive goal-aligned ship → it CLEARS the rolling-3 window** (v129 OG · v131 GA · v132 GA = 1 OG ≤ ceiling). No override, no (a)-rescue.

## Pattern Library contribution (summary)

- **PRIMARY: NEW Library-vocab "Agent-Authored Self-Extracting Skill Library" PROVISIONAL N=1 (CORPUS-FIRST)** — the agent auto-authors its own `SKILL.md` library from its runs, with learned/taught/imported provenance + confidence-gated eviction. Distinct from human-authored skill collections (57k chain) and from v118's memory tree. *Filed to registry.* Promotion-eligible at N=2.
- **SECONDARY (strengthening / administrative, no further mint — §28):** parallel-skill-standard **N=2** (v121 Codex-native + v132 Hermes-lineage — skill ecosystem bifurcating beyond agentskills.io; *deliberately NOT a 57k implementer*); Pattern #18 Multi-Source LLM Aggregator N+1; Pattern #84 cross-vendor + MCP host; Pattern #57 honest corpus-composition (opencode + llmfit + Tongyi); Pattern #83 Honest-Deficiency (ROADMAP); Pattern #45 multi-license; Pattern #52 EXTREME-VIRAL **audience-driven caveat**; agentmemory v66 / #85; v118 OpenHuman sibling; Pattern #82 quantitative-marketing.
- **Honest non-claims:** (a) FAILS; it's a **composition** of OSS not novel primitives; SKILL.md is **Hermes-lineage NOT agentskills.io** (not a 57k implementer); ★-velocity is audience-driven; **1 new standalone (≤ §28 cap) + 1 strengthening, both filed**; NO new top-level Pattern; NO confirmed-count change; NO promotions; **renumbered v131 → v132** (concurrent v131 harness was first under v2.6).

## Pilot

**Tier-1 — pilotable but heavy, fully reversible.** `install-snapshot` first (Docker + large pip surface — HN: ~12 GB). `docker compose up -d --build` → **:7000**; keep `AUTH_ENABLED=true`. GPU optional (Ollama/llama.cpp on Apple Silicon Metal, or point at an API). Highest-value study target = the **self-evolving Skills system** (`services/memory/skill_*.py`) — prior art for automating the vault's "don't repeat the same mistake twice" loop.

---

*Backstory + reception + sources: `00 Notes/(C) Odysseus (PewDiePie) - autopilot research.md`. Gate + Pattern-Library detail: `01 Analysis/`. ⚠️ Concurrent v131 harness ship is on a parallel branch — a merge is needed to fold the v131 entry into the shared chapter/shim.*
