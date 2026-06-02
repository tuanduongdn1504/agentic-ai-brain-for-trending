# Odysseus — Project Context

**Subject:** [`pewdiepie-archdaemon/odysseus`](https://github.com/pewdiepie-archdaemon/odysseus) — "Self-hosted AI workspace."
**Wiki version:** **v136** (Routine **v2.6** — CURRENT; §37 fact-provenance applied).
**Status:** SHIPPED 2026-06-02. **GOAL-ALIGNED INCLUDE** (v2.6 §31/§33) — (b) **STRONG** + (c)(d) STRONG + (a) FAIL. A clean goal-aligned ship; the §35 off-goal ceiling was cleared back at v131/v132, and the rolling-3-ship window at v136 = {v134 GA · v135 GA · v136 GA} = 0 OG (healthy). Tier-1 pilotable.

> **Numbering history:** researched/built as a **v131→v132** candidate during a concurrent-ship window (this session), then shipped as **v136** after main independently advanced to v135 (v132 supermemory / v133 GordenPPTSkill / v134 obsidian-second-brain / v135 open-slide). Two concurrent-ship renumbers, no content impact. Per the 2026-06-02 convention, shipped on branch `wiki/v136-odysseus` off current main — operator merges.

## One-line

PewDiePie's open-sourced **"ChatOS" → Odysseus**: a self-hosted AI workspace — "the self-hosted version of the UI experience you get from ChatGPT and Claude." Multi-model chat (vLLM/llama.cpp/Ollama/OpenRouter/OpenAI) + autonomous **agents over MCP** (web/files/shell/skills/memory) + **Cookbook** (← llmfit; VRAM-aware, 270+ models) + **Deep Research** (← Alibaba Tongyi) + blind **Compare** + **self-evolving Skills** + ChromaDB memory + email/calendar/notes. FastAPI + vanilla-JS PWA (:7000). MIT. By **Felix "PewDiePie" Kjellberg** (Swedish creator). **~11,771★ in ~1 day** (as of 2026-06-01 — stated, NOT API-verified §37.4) = EXTREME-VIRAL but **audience-driven, not organic dev signal**.

## Pattern Library impact

**PRIMARY: NEW Library-vocab "Agent-Authored Self-Extracting Skill Library" PROVISIONAL N=1 (CORPUS-FIRST)** — skills auto-distilled from agent runs (≥2 rounds / ≥2 tool calls → conservative LLM extraction, `MIN_CONFIDENCE=0.6`), persisted as **Hermes-lineage `SKILL.md`** with `source: learned|taught|imported` + `teacher_model` provenance + confidence-gated eviction. Distinct from human-authored skill collections AND from the corpus's memory engines (v66 agentmemory / v118 OpenHuman / v132 supermemory). *Filed to `_patterns/06` as the 10th standalone.* **SECONDARY (strengthening, no mint):** parallel-skill-standard **N=2** (v121 Codex-native + v136 Hermes-lineage); Pattern #18 Multi-Source LLM Aggregator N+1; Pattern #84 cross-vendor; Pattern #57 honest corpus-composition (opencode + llmfit + Tongyi); Pattern #83 Honest-Deficiency (ROADMAP); Pattern #52 EXTREME-VIRAL audience-driven caveat; corpus-memory cluster (v66/v118/v132/v134); **v118 OpenHuman sibling**.

**§28 filing — DONE not claimed:** 1 new PROVISIONAL standalone (≤2 cap) + the parallel-standard strengthening written into the registry this session. **NO new top-level Pattern; NO promotions; NO confirmed-count change** (46 confirmed / 8 Library-vocab CONFIRMED unchanged). **Honest non-claims:** (a) FAILS (Swedish celebrity, not (a)-7); **composition** of OSS not novel primitives; SKILL.md is **Hermes-lineage NOT agentskills.io** (NOT a 57k implementer); ★-velocity audience-driven + NOT API-verified; renumbered v131→v132→v136.

## Streak (v2.6 §32 forward)

GA:5·OG:4 [1 ov] (post-v135) → **`GA:6 · OG:4 [1 ov]`** (v136 Odysseus = 6th goal-aligned PASS).

## Files

- `02 Wiki/index.md` — wiki page.
- `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` — GOAL-ALIGNED INCLUDE gate (v2.6 tier-tag + §37 provenance).
- `01 Analysis/(C) Pattern-Library-Phase-4b-self-evolving-skill-library-N1.md` — the PRIMARY + secondaries.
- Research basis: `00 Notes/(C) Odysseus (PewDiePie) - autopilot research.md` (3-iteration `/loop` autopilot).

## Pilot note

**Tier-1 pilotable — heavy but reversible.** `install-snapshot` first (Docker + ~12 GB pip per HN, NOT API-verified). `docker compose up -d --build` → **:7000**; `AUTH_ENABLED=true`. GPU optional — Ollama/llama.cpp (Apple Silicon Metal) or an API. Highest-value study target = the **self-evolving Skills system** (`services/memory/skill_*.py`): prior art for automating the Pattern-Library "don't repeat the same mistake twice" loop, and a sibling to the §37 fact-provenance discipline the vault adopted at v134.
