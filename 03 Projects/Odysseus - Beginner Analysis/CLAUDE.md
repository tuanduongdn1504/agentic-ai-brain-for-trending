# Odysseus — Project Context

**Subject:** [`pewdiepie-archdaemon/odysseus`](https://github.com/pewdiepie-archdaemon/odysseus) — "Self-hosted AI workspace."
**Wiki version:** **v132** (Routine **v2.6** — CURRENT). *Renumbered from v131 — a concurrent **v131 `harness`** ship took v131 on a parallel branch (commit `8aa25e8`).*
**Status:** SHIPPED 2026-06-01. **GOAL-ALIGNED INCLUDE** (v2.6 §31/§33 tier) — (b) **STRONG** + (c)(d) STRONG + (a) FAIL. The breached v2.6 §35 off-goal-rate ceiling (v127/v128/v129 all off-goal) was remedied by the concurrent v131 harness ship; **Odysseus-v132 is the 2nd consecutive GOAL-ALIGNED ship → it CLEARS the §35 rolling-3 window** (v129 OG · v131 GA · v132 GA = 1 OG ≤ ceiling). Not an override, not an (a)-rescue. Tier-1 pilotable.

## One-line

PewDiePie's open-sourced **"ChatOS" → Odysseus**: a self-hosted AI workspace — "the self-hosted version of the UI experience you get from ChatGPT and Claude." Multi-model chat (vLLM/llama.cpp/Ollama/OpenRouter/OpenAI) + autonomous **agents over MCP** (web/files/shell/skills/memory) + **Cookbook** (VRAM-aware recommend/serve, 270+ models) + **Deep Research** (← Alibaba Tongyi DeepResearch) + blind **Compare** + **self-evolving Skills** + ChromaDB memory + email/calendar/notes. FastAPI + vanilla-JS PWA (:7000), local data. MIT. By **Felix "PewDiePie" Kjellberg** (Swedish creator). **~11,771★ / ~1,538 forks in ~1 day** = EXTREME-VIRAL but **audience-driven, not organic dev signal** (caveat). Launch video: *"MY trillion $Dollar Project is finally OUT!"*

## Pattern Library impact

**PRIMARY: NEW Library-vocab "Agent-Authored Self-Extracting Skill Library" PROVISIONAL N=1 (CORPUS-FIRST)** — skills auto-distilled from agent runs (≥2 rounds / ≥2 tool calls → conservative LLM extraction, `MIN_CONFIDENCE=0.6`), persisted as **Hermes-lineage `SKILL.md`** with `source: learned|taught|imported` + `teacher_model` provenance + confidence-gated eviction. Distinct from human-authored skill collections (agentskills.io chain) and from v118 OpenHuman's memory-tree. *Filed to `_patterns/06-library-vocab-registry.md`.* **SECONDARY (strengthening, no mint):** parallel-skill-standard observation **N=2** (v121 Codex-native + v132 Hermes-lineage — the skill ecosystem is bifurcating beyond agentskills.io); Pattern #18 Multi-Source LLM Aggregator N+1 (multi-provider + multi-runtime); Pattern #84 cross-vendor; Pattern #57 corpus-composition (opencode v67/v99 + Hermes v78/v82/v112 + Tongyi); Pattern #83 Honest-Deficiency-Disclosure (ROADMAP "I dont know what I'm doing hlep"); Pattern #52 EXTREME-VIRAL pulse w/ audience-driven caveat; agentmemory v66 / ChromaDB; **v118 OpenHuman sibling** (productized Karpathy-LLM-wiki genus); **v131 harness** concurrent sibling.

**§28 filing — DONE not claimed:** 1 new PROVISIONAL standalone (within the ≤2 cap) + the v121 strengthening written into the registry this session. **NO new top-level Pattern; NO promotions at ship; NO confirmed-count change** (46 confirmed / 8 Library-vocab CONFIRMED unchanged; PROVISIONAL +1). **Honest non-claims:** (a) FAILS (PewDiePie = Swedish celebrity, not a cultural-peer, not (a)-7); it's a **composition** of OSS (opencode + llmfit + Tongyi + ChromaDB + SearXNG + MCP), not novel primitives; ★-velocity is audience-driven; SKILL.md is **Hermes-lineage, NOT agentskills.io** (so NOT a 57k-chain implementer); **renumbered v131 → v132** (concurrent v131 harness was the first v2.6 ship).

## Streak (v2.6 §32 forward)

Historical **"49+3\*" frozen @v125**. Forward (post-v131 harness GA): GA:2·OG:3 [1 ov] → **`GA:3 · OG:3 [1 ov]`** (v132 Odysseus = 3rd goal-aligned PASS in the v2.5/v2.6 forward window).

## ✅ §35 ceiling

Breach (v127/v128/v129 all off-goal) **remedied by the concurrent v131 harness** (GOAL-ALIGNED, the §35-mandated goal-aligned next ship). **v132 Odysseus = 2nd consecutive GOAL-ALIGNED ship → CLEARS the rolling-3-ship window** (v129 OG · v131 GA · v132 GA = 1 OG ≤ the ceiling). NOT an override; NO frequency-trigger trip.

## ⚠️ Concurrent-ship / merge note

This branch (`claude/affectionate-lalande-c6d83f`) does **not** contain the v131 harness ship (it's on a parallel branch). State files here are named forward-correctly for **v132**, but a **merge with the harness branch** is needed to fold in the v131 entry + reconcile the shared chapter (`_state/03c-projects-v61-v132.md`) and root shim. v131's tier (GOAL-ALIGNED) is taken from its commit message `8aa25e8`.

## Files

- `02 Wiki/index.md` — wiki page.
- `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` — GOAL-ALIGNED INCLUDE gate (v2.6 tier-tag; §35 window-clearing).
- `01 Analysis/(C) Pattern-Library-Phase-4b-self-evolving-skill-library-N1.md` — the PRIMARY + secondaries.
- Research basis: `00 Notes/(C) Odysseus (PewDiePie) - autopilot research.md` (the `/loop` autopilot research note, 3 iterations).

## Pilot note

**Tier-1 pilotable — heavy but reversible.** `install-snapshot` first (Docker + large pip surface; HN noted ~12 GB). `docker compose up -d --build`, serves on **:7000**; keep `AUTH_ENABLED=true`. GPU optional — local serving via Ollama/llama.cpp (Apple Silicon Metal) or point at an API. The genuinely vault-relevant study target = the **self-evolving Skills system** (`services/memory/skill_*.py`): prior art for automating the Pattern-Library "don't repeat the same mistake twice" loop.
