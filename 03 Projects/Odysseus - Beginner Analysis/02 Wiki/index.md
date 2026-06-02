# Odysseus — Wiki (v136)

> `pewdiepie-archdaemon/odysseus` · **"Self-hosted AI workspace."** · *"Your own AI workspace, running on your hardware — local-first, privacy-first, and no telemetry."* · PewDiePie's open-sourced **"ChatOS"**: a self-hostable ChatGPT/Claude-style workspace with autonomous MCP agents, a hardware-aware model Cookbook, Deep Research, and a **self-evolving skills** system.

**(C) Claude-generated wiki page.** Researched 2026-06-01 (3-iteration `/loop` autopilot: GitHub API + recursive tree + key source files + landing page + HN + press). **Shipped v136, 2026-06-02** (§37 fact-provenance applied). Phase 0.9: **GOAL-ALIGNED INCLUDE** — (a) FAIL (Swedish creator), (b) **STRONG**, (c)(d) STRONG. A clean goal-aligned ship in a healthy streak (the §35 off-goal ceiling was cleared back at v131/v132). Tier-1 pilotable.

> **Numbering:** researched as a v131→v132 candidate; shipped as **v136** after main advanced to v135 (two concurrent-ship renumbers; no content impact).

---

## Identity (volatile facts carry §37 provenance)

| Field | Value |
|---|---|
| Repo | [`pewdiepie-archdaemon/odysseus`](https://github.com/pewdiepie-archdaemon/odysseus) |
| What | **Self-hosted AI workspace** — multi-model chat + autonomous MCP agents + Cookbook + Deep Research + self-evolving Skills + memory + email/calendar/notes |
| Tier / archetype | **T2 Service / Self-Hosted AI-Agent Workspace** + autonomous-agent harness + MCP host + agent-memory/skills system |
| Stars / forks | **~11,771★ / ~1,538 forks** (as of 2026-06-01, repo page + `gh api` — stated, **NOT API-verified** §37.4) |
| Subscribers / open issues | 117 / 161 (as of 2026-06-01 — stated, NOT API-verified) |
| Created / pushed | **2026-05-31** / 2026-06-01 (~1 day old) (stated, NOT API-verified) |
| Velocity | **~11,771★/day → EXTREME-VIRAL** (NOT API-verified) — ⚠️ **audience-driven** (PewDiePie ~110M subs), NOT organic dev signal; a Pattern #52/#82 caveat, NOT a promotion |
| License | **MIT** (repo + ACKNOWLEDGMENTS.md — stated; structural) |
| Language | **JS ~49% / Python ~37%** (FastAPI backend + vanilla-JS PWA frontend) |
| Serves on | **:7000** (mobile PWA); Docker Compose or bare-metal Python 3.11+ |
| Default branch / homepage | `main` / [pewdiepie-archdaemon.github.io/odysseus](https://pewdiepie-archdaemon.github.io/odysseus/) |
| Author | **`pewdiepie-archdaemon` = Felix "PewDiePie" Kjellberg** — Swedish creator (~110M subs) (declared via launch video + press — confidence high) |
| Launch video | *"MY trillion $Dollar Project is finally OUT!"* — https://www.youtube.com/watch?v=rAzT5lcezPs |

## What it is

The open-sourced, productized form of PewDiePie's home-built **"ChatOS"** — *"the self-hosted version of the UI experience you get from ChatGPT and Claude."* Backstory (Tom's Hardware / TechReport / BigGo / wccftech, confidence high): a ~10-GPU home rig (8× modded RTX 4090 ≈ 256 GB VRAM) running Qwen-235B / Llama-70B / GPT-OSS-120B via **vLLM**; a multi-model **"Council"** that votes on responses (showed emergent "collusion"); then **"The Swarm"** (~64 small 2B models). Odysseus is the cleaned-up product.

**Modules:**
- **Chat** — local (vLLM · llama.cpp · Ollama) + remote (OpenRouter · OpenAI).
- **Agent** — built on **opencode**; over **MCP** + web + files + shell + skills + memory. `src/agent_loop.py`: streaming multi-round loop, fenced-code-block tool calls + function-call fallback, `MAX_AGENT_ROUNDS`, **prompt-injection defense** + **per-owner tool gating**.
- **Cookbook** — built on **llmfit**: scans hardware → VRAM fit → recommends/serves 270+ models (GGUF/FP8/AWQ).
- **Deep Research** — adapted from **Alibaba Tongyi DeepResearch** (Apache-2.0): gather→read→synthesize cited reports.
- **Memory / Skills** — ChromaDB + fastembed (ONNX); **self-evolving Skills** (below).
- **Compare** (blind side-by-side), **Email** (IMAP/SMTP + AI triage), **Calendar** (CalDAV), Notes/Tasks, Document editor, Image gallery.

**⭐ Self-evolving Skills** (`services/memory/skill_*.py`) — the standout: **Hermes-lineage `SKILL.md`** files (frontmatter `name/version/category/tags/status/confidence/source[learned|taught|imported]/teacher_model`; body *When to Use / Procedure / Pitfalls / Verification*). After any run with **≥2 rounds or ≥2 tool calls**, an LLM *conservatively* auto-distills a reusable skill (`MIN_CONFIDENCE=0.6`); usage counters + confidence-gated eviction. **The agent writes, refines, and evicts its own skills.**

**Built on (honest `ACKNOWLEDGMENTS.md`):** opencode (MIT) · llmfit (MIT) · Tongyi DeepResearch (Apache-2.0) · Docker-composed: SearXNG (AGPL-3.0) + ChromaDB (Apache-2.0) + ntfy · MCP SDK (MIT). **Security** (`SECURITY.md`): "do not run it as a public, unauthenticated service"; `AUTH_ENABLED=true`; high-risk tools admin-gated; 2FA; a fork-publishing secret-scan checklist.

## Why it's in the corpus

**GOAL-ALIGNED INCLUDE** (v2.6 §31 — (b) PASSes, so corpus core):
- **(a) FAIL** — PewDiePie = Swedish creator, not a cultural-peer, not (a)-7. No (a)-rescue.
- **(b) STRONG** — runnable + studyable autonomous-agent workspace (opencode-adapted loop, MCP, self-evolving skills, memory). MODERATE-cost reversible × DIRECT = STRONG (not STRONGEST — heavy self-host, study/run not a drop-in vault tool).
- **(c) STRONG** — instructive reference architecture; self-extracting skills + honest attribution + documented security.
- **(d) STRONG** — opencode (v67/v99), Hermes skill-format (v78/v82/v112), agentmemory v66 / ChromaDB, **v132 supermemory (agent-memory engine) + v134 obsidian-second-brain (agent-maintained vault)**, MCP cluster (v66/v70/v76), Pattern #18/#84, DeepSeek/Qwen v72, Tongyi (v9/v79), **v118 OpenHuman** sibling.

## Pattern Library contribution (summary)

- **PRIMARY: NEW Library-vocab "Agent-Authored Self-Extracting Skill Library" PROVISIONAL N=1 (CORPUS-FIRST)** — the agent auto-authors its own `SKILL.md` library from its runs, with learned/taught/imported provenance + confidence-gated eviction. Distinct from human-authored skill collections (57k chain) and from the memory engines v66/v118/v132. *Filed to registry (10th standalone).* Promotion-eligible at N=2.
- **SECONDARY (strengthening / administrative, §28):** parallel-skill-standard **N=2** (v121 Codex-native + v136 Hermes-lineage; NOT a 57k implementer); Pattern #18 N+1; Pattern #84 cross-vendor + MCP host; Pattern #57 honest corpus-composition (opencode + llmfit + Tongyi; NOT the relabeled corpus-recursive thread); Pattern #83 Honest-Deficiency (ROADMAP); Pattern #45 multi-license; Pattern #52 EXTREME-VIRAL **audience-driven caveat** (NOT API-verified); corpus-memory cluster connectivity (v66/v118/v132/v134).
- **Honest non-claims:** (a) FAILS; **composition** of OSS not novel primitives; SKILL.md is **Hermes-lineage NOT agentskills.io**; ★-velocity audience-driven + NOT API-verified; **1 new standalone + 1 strengthening, both filed**; NO new top-level Pattern; NO confirmed-count change (46/8); renumbered v131→v132→v136.

## Pilot

**Tier-1 — pilotable but heavy, fully reversible.** `install-snapshot` first (Docker + large pip surface — HN: ~12 GB, NOT API-verified). `docker compose up -d --build` → **:7000**; `AUTH_ENABLED=true`. GPU optional (Ollama/llama.cpp on Apple Silicon Metal, or an API). Highest-value study target = the **self-evolving Skills system** (`services/memory/skill_*.py`) — prior art for automating the vault's "don't repeat the same mistake twice" loop.

---

*Backstory + reception + sources: `00 Notes/(C) Odysseus (PewDiePie) - autopilot research.md`. Gate + Pattern-Library detail: `01 Analysis/`.*
