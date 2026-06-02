# (C) Phase 0 + Phase 0.9 INCLUDE verdict — Odysseus (v136)

**Routine:** v2.6 (CURRENT; §37 fact-provenance applied). **Researched:** 2026-06-01 (3-iteration `/loop` autopilot). **Shipped:** v136, 2026-06-02. **Verdict:** **GOAL-ALIGNED INCLUDE** — (a) FAIL + (b) **STRONG** + (c) STRONG + (d) STRONG. **STRONG INCLUDE 3/4.**

> **Numbering:** researched/built as a v131→v132 candidate during a concurrent-ship window, then **shipped as v136** after main independently advanced to v135 (v132 supermemory / v133 GordenPPTSkill / v134 obsidian-second-brain / v135 open-slide). v136 = next free number; two concurrent-ship renumbers (v131→v132→v136), no content impact.
> **§35 ceiling:** healthy. The v127–v129 breach was remedied at v131 harness + cleared at v132 supermemory; the rolling-3-ship window at v136 = {v134 GA · v135 GA · v136 GA} = **0 OG**. v136 is a clean goal-aligned ship, **NOT** a ceiling event.

---

## §37 — fact-provenance (volatile facts)

- **11,771★ / 1,538 forks / 117 watchers / 161 open issues** (as of 2026-06-01, github.com/pewdiepie-archdaemon/odysseus repo page + `gh api` — confidence: **stated, NOT API-verified** per §37.4; the env mocks the GitHub API).
- **Created 2026-05-31, pushed 2026-06-01** (~1 day old) (as of 2026-06-01, repo metadata — stated, NOT API-verified).
- **~11,771★ "in ~1 day"** velocity (as of 2026-06-01, derived — stated, NOT API-verified) → **audience-driven** (PewDiePie ~110M subs), NOT organic dev signal.
- **Author = Felix "PewDiePie" Kjellberg**, Swedish creator (as of 2026-06, launch video `rAzT5lcezPs` + press [Tom's Hardware / TechReport / wccftech] — confidence: high).
- **MIT · JS ~49% / Python ~37%** (repo page + ACKNOWLEDGMENTS.md — stated; structural/stable, low-volatility).

---

## Phase 0 — scope gate

| Gate | Result |
|---|---|
| Repo reachable + readable | ✅ `pewdiepie-archdaemon/odysseus` |
| License | ✅ **MIT** (stated) |
| Active | ✅ ~1 day old, pushed daily (stated, NOT API-verified) |
| Scale | ✅ ~11,771★ (stated, NOT API-verified) |
| Tier | **T2 Service / Self-Hosted AI-Agent Workspace** + autonomous-agent harness + MCP host + agent-memory/skills system |

**Phase 0 = PASS** — a self-hosted autonomous-agent AI workspace (multi-model chat, MCP agents w/ shell/file/web, self-evolving skills, persistent memory, deep research).

---

## Phase 0.9 — STRICT 4-criterion filter + v2.6 §31 tier routing

- **(a) FAIL** — PewDiePie = Swedish mega-creator (declared via video+press, confidence high), not a VN/Asian cultural-peer, not (a)-7. None of the 7 (a) sub-axes PASS. No (a)-rescue. Clean fail (mirrors v97/v98/v112/v113/v114/v118/v126/v131).
- **(b) STRONG** — directly goal-#1: a runnable + studyable autonomous-agent workspace (opencode-adapted multi-round tool loop, MCP host + 4 built-in MCP servers, shell/file/web tools, self-evolving SKILL.md skills, ChromaDB memory, deep research). Per §10: cost MODERATE (Docker + large pip surface; GPU optional via Ollama/API — reversible) × DIRECT relevance = **STRONG** (not STRONGEST — heavy self-host, a study/run subject, not a drop-in vault tool).
- **(c) STRONG** — instructive reference architecture: streaming agent loop w/ prompt-injection defense + per-owner tool gating; the **Hermes-lineage self-extracting skills system** (auto-distill skills from runs, learned/taught/imported provenance + confidence-gated eviction); documented security model; disarmingly honest ROADMAP.
- **(d) STRONG** — opencode (v67/v99); **Hermes** skill-format lineage (v78/v82/v112); ChromaDB persistent memory ↔ **agentmemory v66**; **NEW corpus neighbors on current main: v132 supermemory** (AI agent-memory engine — direct sibling to Odysseus's memory module) **+ v134 obsidian-second-brain** (agent-maintained knowledge vault); MCP cluster (v66/v70/v76); Pattern #18 Multi-Source LLM Aggregator + #84 cross-vendor; DeepSeek/Qwen v72; Tongyi deep-research (v9/v79); **v118 OpenHuman** sibling.

---

## Verdict + v2.6 tier tag

| Criterion | Result |
|---|---|
| (a) cultural-peer | **FAIL** (PewDiePie, Swedish; not (a)-7) |
| (b) goal-relevance / vault-utility | **STRONG** (runnable + studyable autonomous-agent workspace; MODERATE-cost reversible × DIRECT; Tier-1 pilotable) |
| (c) instructive | **STRONG** (opencode-adapted loop + self-evolving skills + honest attribution/security) |
| (d) corpus connectivity | **STRONG** (opencode + Hermes + agentmemory v66 + supermemory v132 + obsidian v134 + MCP cluster + #18/#84 + OpenHuman v118) |

**→ v2.6 §33 TIER TAG: `GOAL-ALIGNED INCLUDE`** — (b) PASSes (STRONG); corpus core (autonomous agents for software dev), not an off-goal capture. 3/4 with (a) the only fail.

**Streak (v2.6 §32 forward):** GA:5·OG:4 [1 ov] (post-v135) → **`GA:6 · OG:4 [1 ov]`** (v136 Odysseus = 6th goal-aligned PASS).

**Pilot:** Tier-1 — pilotable but heavy. `install-snapshot` first (Docker + ~12 GB pip per HN, NOT API-verified). `docker compose up -d --build` → :7000; `AUTH_ENABLED=true`. GPU optional. Highest-value study target = the self-evolving Skills system (`services/memory/skill_*.py`).

**Finding-2 calibration:** (a) genuinely FAILS (Swedish celebrity, not laundered); (b) honestly **STRONG, not STRONGEST** (heavy self-host, not a drop-in vault tool). Clean GOAL-ALIGNED 3/4 resting on (b)(c)(d).
