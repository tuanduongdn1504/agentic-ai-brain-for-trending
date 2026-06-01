# (C) Phase 0 + Phase 0.9 INCLUDE verdict — Odysseus (v132)

**Routine:** v2.6 (CURRENT). **Fetched:** 2026-06-01 (GitHub API + recursive tree + key source files + landing page + HN + press). **Verdict:** **GOAL-ALIGNED INCLUDE** — (a) FAIL + (b) **STRONG** + (c) STRONG + (d) STRONG. **STRONG INCLUDE 3/4.**

> ⚠️ **§35 ceiling context (renumbered v131 → v132):** the off-goal-rate ceiling was **BREACHED** (v127/v128/v129 all OFF-GOAL CAPTURE). A **concurrent v131 `harness` ship** (GOAL-ALIGNED INCLUDE 3/4; the first ship under v2.6; on a parallel branch — commit `8aa25e8`) **already remedied** the breach (it was the goal-aligned "next ship" §35 required). **Odysseus is therefore v132** — a **2nd consecutive GOAL-ALIGNED ship** that **CLEARS the §35 rolling-3-ship window** (v129 OG · v131 GA · v132 GA = 1 OG ≤ the ceiling). Clean GOAL-ALIGNED INCLUDE; **no override, no (a)-rescue.**

---

## Phase 0 — scope gate

| Gate | Result |
|---|---|
| Repo reachable + readable | ✅ `pewdiepie-archdaemon/odysseus` |
| License | ✅ **MIT** |
| Active | ✅ created **2026-05-31**; pushed 2026-06-01 (today); ~1 day old; extremely active |
| Scale | ✅ **11,771★ / 1,538 forks / 117 watchers / 161 open issues** |
| Tier | **T2 Service / Self-Hosted AI-Agent Workspace** (run-it-yourself app) + autonomous-agent harness + MCP host + agent-memory/skills system |

**Phase 0 = PASS.** Squarely in-scope: a self-hosted **autonomous-agent AI workspace** — multi-model chat, MCP agents with shell/file/web tools, self-evolving skills, persistent memory, deep research.

---

## Phase 0.9 — STRICT 4-criterion filter + v2.6 §31 tier routing

### (a) Author cultural-peer to Storm Bear — **FAIL**

Owner `pewdiepie-archdaemon` = **Felix Kjellberg ("PewDiePie")**, a Swedish YouTuber/creator (~110M+ subscribers) on a 2025 self-hosting-AI arc (10-GPU home rig; the "ChatOS"/"Council"/"Swarm" experiments). Not a VN/Asian cultural-peer; not a foundational vault-substrate vendor ((a)-7). None of the 7 (a) sub-axes PASS. **(a) FAIL** — clean, no (a)-rescue (mirrors v97/v98/v112/v113/v114/v118/v126).

### (b) Goal-relevance / vault-utility — **STRONG**

Goal #1 = "master Claude and autonomous agents **for software development**." Odysseus is a runnable, studyable **autonomous-agent workspace**: a multi-round tool-using agent loop (adapted from **opencode**), an MCP host + 4 built-in MCP servers, shell/file/web tools, **self-evolving SKILL.md skills**, ChromaDB memory, deep research. It is both a *pilot* (self-hostable) and a *reference architecture* (its agent loop + skills system are directly instructive for the vault's own skill/wiki methodology).

Per §10 (cost × relevance): cost **MODERATE** (Docker + large pip surface; GPU optional via Ollama/API — reversible), relevance **DIRECT**, applicability **HIGH** but as a *workspace to run/study*, not a vault-routine tool. MODERATE-cost × DIRECT = **STRONG** (not STRONGEST — a heavy install and a study/run subject more than a daily vault utility). **(b) STRONG.**

### (c) Instructive / exemplary — **STRONG**

A complete, honestly-attributed reference for a local agent workspace: a streaming multi-round agent loop with prompt-injection defense + per-owner tool gating; a **Hermes-lineage self-extracting skills system** (auto-distill reusable skills from runs, with learned/taught/imported provenance + confidence-gated eviction); a documented security model; a disarmingly honest ROADMAP. Genuine teaching material — especially the skills system as prior art for automating "don't repeat the same mistake twice." **(c) STRONG.**

### (d) Corpus connectivity — **STRONG**

opencode (v67 opencode-antigravity-auth, v99 cmux) — agent loop; **Hermes** skill-format lineage (v78 ECC, v82 huashu-design, v112 freellmapi); ChromaDB persistent memory ↔ **agentmemory v66** (Pattern #85 Platform-Primitive); **MCP** host + built-in servers ↔ v66/v70/v76 MCP cluster; multi-provider + multi-runtime ↔ **Pattern #18 Multi-Source LLM Aggregator** (CONFIRMED N=3) + **Pattern #84 cross-vendor**; local models Qwen/DeepSeek ↔ v72 DeepSeek-TUI; Deep Research ← Tongyi ↔ autoresearch v9/v79; **closest sibling v118 OpenHuman** (productized Karpathy-LLM-wiki); the concurrent **v131 harness** (sibling agent-harness subject); Pattern #83 (honest ROADMAP), Pattern #45 (multi-license composition), Pattern #52 (audience-driven velocity caveat). **(d) STRONG.**

---

## Verdict + v2.6 tier tag

| Criterion | Result |
|---|---|
| (a) cultural-peer | **FAIL** (PewDiePie = Swedish creator; not (a)-7) |
| (b) goal-relevance / vault-utility | **STRONG** (runnable + studyable autonomous-agent workspace; MODERATE-cost reversible × DIRECT; Tier-1 pilotable) |
| (c) instructive | **STRONG** (opencode-adapted agent loop + self-evolving skills + honest attribution/security) |
| (d) corpus connectivity | **STRONG** (opencode v67/v99 + Hermes v78/v82/v112 + agentmemory v66 + MCP cluster + Pattern #18/#84 + DeepSeek v72 + OpenHuman v118 + v131 harness sibling) |

**→ v2.6 §33 TIER TAG: `GOAL-ALIGNED INCLUDE`** — (b) PASSes (STRONG); this is the corpus's core (autonomous agents for software dev), not an off-goal capture. 3/4 with (a) the only fail.

**§35 ceiling note:** the ceiling was BREACHED (v127/v128/v129 all OFF-GOAL). The **concurrent v131 `harness` ship** (GOAL-ALIGNED, parallel branch) was the goal-aligned "next ship" that **remedied** it; **v132 Odysseus is the 2nd consecutive GOAL-ALIGNED ship and CLEARS the rolling-3-ship window** (v129 OG · v131 GA · v132 GA = 1 OG ≤ ceiling). NOT an override; NO (a)-rescue; NO 2-in-20/3-in-30 frequency-trigger trip.

**Streak (v2.6 §32 forward):** historical **"49+3\*" frozen @v125**. Forward (post-v131 harness GA): GA:2·OG:3 [1 ov] → **`GA:3 · OG:3 [1 ov]`** (v132 Odysseus = 3rd goal-aligned PASS in the v2.5/v2.6 forward window).

**Pilot:** **Tier-1 — pilotable but heavy.** `install-snapshot` first (Docker + ~12 GB deps per HN). `docker compose up -d --build` → :7000; keep `AUTH_ENABLED=true`. GPU optional. Highest-value study target = the self-evolving Skills system (`services/memory/skill_*.py`).

**Finding-2 calibration note:** (a) genuinely FAILS (Swedish celebrity, not laundered to a soft pass); (b) is honestly **STRONG, not STRONGEST** — a heavy self-hosted workspace to run/study, not a drop-in vault tool, so it is not inflated to v126's STRONGEST. A clean GOAL-ALIGNED 3/4 resting on (b)(c)(d).

> ⚠️ **Concurrent-ship / merge note:** this branch (`claude/affectionate-lalande-c6d83f`) does **not** contain the v131 harness ship (shipped on a parallel branch). State files here are named forward-correctly for **v132**, but a merge with the harness branch is needed to fold in the v131 entry + reconcile the shared chapter/shim. v131 harness's tier (GOAL-ALIGNED) is taken from its commit message `8aa25e8`.
