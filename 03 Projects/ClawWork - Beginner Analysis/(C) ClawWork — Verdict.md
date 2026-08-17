# (C) ClawWork — Verdict (wiki v233)

**Subject:** `HKUDS/ClawWork` — a live **economic-survival benchmark** in which LLM agents start with $10, are assigned real professional tasks from OpenAI's **GDPval** gold subset, **pay for their own tokens**, are graded by an LLM judge against occupation-specific rubrics, get paid `quality × hours × BLS wage`, and go **bankrupt at $0**; plus **ClawMode**, a wrapper applying the same accounting to a live nanobot chat gateway across 9 channels.
**Built:** 2026-08-17 · operator-requested (link arrived via Facebook; `fbclid` stripped).
**Verification:** produced **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions` — **no workflow, no subagent** (the ~972 KB shim overflows every subagent >200K → prompt-too-long; the standing v200→v232 self-throttle).

---

## Phase 0.9 — STRICT criteria: **GOAL-ALIGNED INCLUDE 3/4**

| # | Criterion | Call |
|---|---|---|
| (a) | Anthropic affiliation / registered (a)-7 source | **FAIL** |
| (b) | Goal relevance | **MODERATE** — *keys the tier* ⚠️ STRONG reviewable |
| (c) | Substance | **STRONG** ⚠️ MODERATE reviewable |
| (d) | Cross-references | **STRONG** |

### (a) FAIL
**HKUDS = Data Intelligence Lab @ The University of Hong Kong** (PI **Chao Huang**) — an academic lab, **not Anthropic** (§41: (a) passes only on a declared Anthropic affiliation or a registered (a)-7 vendor-direct source; no name/heritage/locale/notability inference). ⚠️ **A summariser claim that nanobot is "Anthropic's agent framework" was caught and discarded** — nanobot is `HKUDS/nanobot`, the same lab's own OpenClaw-inspired engine. Had that stood it would have wrongly flipped (a).
**#19 19a — returning institution, NOT a first-author claim:** `HKUDS/DeepTutor` is corpus subject **v38**; `HKUDS/OpenSpace` was credited by **cortex-hub v181**. ClawWork is the **2nd HKUDS *subject***.

### (b) MODERATE — keys the tier (cleanly GOAL-ALIGNED via §31; no §40 rescue needed)
**For:** agent **evaluation/benchmark infrastructure** is on-domain Goal-#1 substrate, and this lands on four live vault threads at once — the **prompt-eval** pilot thread (the corpus's only other eval-shaped subject is llm-space v221), **claude-api-cost-optimization** (this is the sharpest instantiation of that thread the corpus has: *token cost is the score*), **multi-agent-orchestration** (LangGraph), and the **agent-skills** substrate (it ships a real `SKILL.md`). It also uses **MCP** as its internal tool bus, and its rubric-plus-threshold evaluator is directly transferable to the vault's RATIFIED candidate-LLM legibility ADR.
**Held below STRONG by:** **Claude is absent from the leaderboard and from the README entirely** (though Sonnet 4.6 run configs ship); the judge and the required key are **OpenAI**; the domain — economic benchmarking of professional labour — sits one step off *autonomous agents for software development*; **nothing here is a tool you install into a daily Claude workflow** (it is a read-and-borrow artifact); and the repo has been **quiet ~5.5 months**.
⚠️ **STRONG is defensible** on the "evaluation infrastructure is core substrate" reading — recorded as the operator/audit-reviewable alternative. Calibrates level with **v232 gemini-web2api** (MODERATE, Claude-absent), above **v180**, below **llm-space v221** / **PixelRAG v211** (both STRONG).

### (c) STRONG ⚠️ MODERATE-reviewable
**For:** an **876-line `EconomicTracker`** with per-channel cost ledgers and three JSONL stores; a **237→829-line evaluator chain** with per-occupation rubrics, a hard 0.6 payment gate, 2MB artifact caps, and an explicit refusal to fall back to heuristics; an MCP tool server; a React dashboard + FastAPI/WebSocket backend; 18 per-model run configs; a genuine second product surface (ClawMode over 9 channels); and it consumes a **real published dataset** (OpenAI GDPval gold subset).
**Against:** ~**37–40 commits in a two-week burst (Feb 16 – Mar 3 2026), silent since**; the **leaderboard is self-run by the authoring lab**; 🔴 **the cost axis is compromised** — pricing is hardcoded universal (`2.5`/`10.0` per 1M) with **no model-specific table**, so "Cost" largely measures token volume; **doc-vs-code drift** (README says judge = GPT-5.2, code default = `"gpt-4o"`; README says "44 sectors", GDPval is 44 *occupations* across 9 sectors); `trading/` is an empty stub; **NOT source-cloned**.

### (d) STRONG
llm-space v221 (agent-dev workbench w/ eval — closest corpus neighbour) · **DeepTutor v38** (same lab; its *vertical-stack hypothesis* is confirmed here) · cortex-hub v181 (cited HKUDS/OpenSpace) · **CodexBar v159** (Peter Steinberger = OpenClaw's creator) · **GLM-5 v176** (already cites Vending Bench 2) · **OfficeCLI v206** (GDPval deliverables *are* Office documents) · agent-skills substrate · #18 MCP · #84 84c provider-agnostic · the cost + prompt-eval + orchestration threads · hireui's candidate-LLM legibility ADR.

---

## Pattern outcome: **1 NEW §C standalone at N=1**

> **"Economic-Survival Agent Benchmark — agents are assigned real professional work, must pay for their own inference out of a starting balance, are paid by rubric-graded output quality against real wage data, and fail terminally by going bankrupt."**

**Corpus-first for the surface** — hand-grep confirms the corpus has **no benchmark/eval-harness subject at all** (`livebench` 0 · `gdpval` 0 · `self-funding` 0 · `earn money` 0; "benchmark" appears 52× only as a *property* of other subjects). The nearest neighbour, **llm-space v221**, is a *private development workbench* for evaluating **your own** agent — a different object from a **competitive public benchmark with a leaderboard and an economic failure state**.

⚠️ **Explicitly NOT world-first, and the prior art is central:** **Vending-Bench / Vending-Bench 2** (Andon Labs) is the canonical instance and is **already cited inside this corpus** (GLM-5 v176); **Anthropic's Project Vend** ("Claudius") is the real-world version; **GDPval** is OpenAI's; **CoffeeBench**, **Agent Bazaar**, **EvoAgentBench** and the **Artificial Analysis GDPval-AA** leaderboard populate the space. The mint is scoped to the *conjunction* — GDPval professional deliverables × **endogenous token cost** × work-vs-learn investment × bankruptcy × a live-gateway product wrapper.

**Precedent for minting at N=1 on a corpus-first-not-world-first surface:** serve-sim v183 · fff v194 · OfficeCLI v206 · CLIProxyAPI v207 · grok-build v215 · llm-space v221 · openinterpreter v223 · open-lovable v224 — and, decisively, the **v232 finding that "not world-first" has never independently blocked a §C row here** (Firecrawl v214 was minted while being *neither* corpus- nor world-first).

⚠️ **NO-MINT alternative recorded, operator/audit-reviewable, NOT self-executed:** *"a research benchmark artifact, not a mintable agent-capability class — the PixelRAG v211 'research-system-not-tool' + corpus-first-for-a-technique discipline, compounded by a weak anchor (two-week burst, stale ~5.5 months, self-run leaderboard, broken cost axis) per the v231 ground-2 reasoning."* This is a genuine judgment call and the audit should re-open it. **Leaned MINT** because an evaluation harness is a *capability class* the corpus wholly lacks (unlike a domain or a technique), because it sits on a live pilot thread, and because it gives the overdue audit an explicit row to adjudicate rather than a buried observation.

**Either way, counts are UNCHANGED: 46 confirmed patterns / 11 CONFIRMED Library-vocab.** §C live standalones **48 → 49**; tracked PROVISIONAL surface **≈55 → ≈56**. §28 ≤2-mints cap honoured (1 of ≤2).

---

## Secondary observations (recorded, **NOT** minted)

- **#19 19a** — HKUDS returning institution; a textbook **ecosystem-portfolio-builder** (LightRAG · MiniRAG · VideoRAG · AutoAgent · DeepTutor · OpenSpace · **nanobot** · ClawWork). Another **Pattern #44** academic-lab data point.
- **⭐ Corpus-recursive prediction-confirmation (a genuine one):** the **DeepTutor v38** wiki posited an HKUDS *vertical-stack hypothesis* — *engine (nanobot) → infra (LightRAG) → **apps***. ClawWork is a same-lab **app/benchmark built on that same engine**, confirming the v38 analysis from a later, independent ship. **NOT #57** (ClawWork cites no corpus subject; this is the vault's own prior inference being validated).
- **Author cross-ref, NOT #57:** ClawMode targets **nanobot**, which is openly *inspired by* **OpenClaw**, created by **Peter Steinberger** — author of corpus subject **CodexBar v159**. An authorship adjacency two hops out, not an influence-citation.
- **#18 MCP cross-ref, NO B1-MCP N-bump:** ships an MCP server (`start_live_services.py`) but as an **internal tool bus for its own benchmark agents**, not a one-server-many-external-clients distribution. Anti-inflation: recorded, not counted.
- **Agent-skills cross-ref, NO N-bump:** `clawmode_integration/skill/SKILL.md` — an "Economic Survival Protocol" with a four-state financial policy and a 15-iteration budget.
- **#84 84c, NO N-bump:** provider-agnostic by config (Claude / Gemini / GLM / Qwen / Kimi / DeepSeek via LangChain·LiteLLM·OpenRouter).
- **LV #20 Token-Economy-Quantification — QUALIFIED-ADJACENT, N stays 4.** Conceptually the strongest possible instance (cost *is* the score) but the figures are self-run and the universal-price flaw undercuts them (the v179/v211/v226 handling).
- **#83 honest-disclosure — MIXED, leaning negative:** ships a real disclaimer (*"educational, research, and technical exchange purposes only"*) ✓, but pairs it with a **`💰 $15K earned in 11 Hours` headline** over a self-run leaderboard whose cost column is methodologically broken.
- **#66 supply-chain / runtime — BENIGN install, MODERATE runtime:** plain `pip install -r requirements.txt`, **no `curl|bash`**, no postinstall evidenced; but it **executes agent-generated code** (boxlite/E2B sandboxes), writes agent-created files, needs an OpenAI key (+ optional Tavily/E2B), and **ClawMode extracts API keys out of `~/.nanobot/config.json` into environment variables**. NOT source-cloned → treat as untrusted-until-inspected.
- **OfficeCLI v206 cross-ref:** the docx/pptx/xlsx/reportlab dependency stack exists because GDPval deliverables are Office documents — v206 is the corpus's agent-first answer to exactly that need.
- **Naming note:** the internal package `livebench` collides by name with the unrelated external **LiveBench** benchmark.

**NON-claims:** NOT **#52** (metrics page-stated §37.4; a two-week burst then 5.5 months silent → velocity unestablishable) · NOT **#57** · NOT **world-first** · NOT **Anthropic-affiliated** (nanobot confabulation corrected) · NOT **#18 B1-MCP** · NOT a new top-level pattern (max **#85**) · NOT the corpus's first HKUDS author (DeepTutor v38) · NOT source-cloned.

**Tier: T2 Service** — self-hosted developer/evaluation tool, **benchmark-harness flavour** (the llm-space v221 / codebase-memory-mcp v172 / fff v194 family).

---

## Streak & ceilings

- **Streak: v232 GA:90 → `GA:91 · OG:13 [7 ov]`** — **14 consecutive GOAL-ALIGNED ships** post the v219 OG break.
- **§35 CLEAR** — rolling-3 window {v231 GA, v232 GA, **v233 GA**} = 0 OG. (Under the reviewable OFF-GOAL reading the window would still be ≤1 OG → clear either way.)

---

## Verification log

✅ **Collision — CLEAN, sanity-anchored hand-grep.** `clawwork`, `claw work`, `chao huang`, `lightrag`, `minirag`, `autoagent`, `videorag`, `gdpval`, `livebench`, `self-funding`, `earn money` = **0 hits** across `_state/03c` + `_patterns/06`, while anchors `openclaw` (35/11), `cortex-hub` (36/20), `palmier-pro` (26/15), `CoreOfPotato`, `gemini-web2api` all hit richly → **the grep works, so the empty results are trustworthy.**
✅ **Identity + landscape** by independent WebSearch/WebFetch (HKU Data Intelligence Lab; GDPval arXiv 2510.04374; Vending-Bench/Project Vend; nanobot ≠ Anthropic; OpenClaw = Steinberger).
✅ **Source** hand-fetched: repo page, raw README, tree, `requirements.txt`, `configs/` listing, `clawmode_integration/README.md`, `skill/SKILL.md`, `economic_tracker.py`, `evaluator.py`, `llm_evaluator.py`, commit history.
✅ **Prior-art tie verified inside the corpus:** Vending Bench 2 already cited in the GLM-5 v176 entry; nanobot already documented in the DeepTutor v38 entry.

**Errors caught by hand (4):**
1. **"nanobot is Anthropic's agent framework"** — summariser confabulation, **discarded**; it is `HKUDS/nanobot` (would have flipped criterion (a)).
2. **"first HKUDS author"** — my own initial over-claim, **corrected**: DeepTutor **v38** precedes.
3. **"zero Claude support"** — README-scoped, **corrected**: two `test_claude_sonnet_4_6_*.json` configs ship; Claude is absent from the *leaderboard*, not from the repo.
4. **Cost-axis credibility** — the README's cost-efficiency framing **corrected against source**: hardcoded universal token pricing, no per-model table.

**inflation_check — HELD:** 1 mint ≤ 2 cap · N=1 honestly scoped (corpus-first for the surface, **not** world-first, with all prior art credited) · the NO-MINT alternative recorded and **not** self-executed · counts 46/11 unchanged · max pattern stays **#85** · no N-bumps taken on #18 B1-MCP, #84, #20, or the agent-skills substrate · no double-count.

---

## Bottom line

**ClawWork is a genuinely clever framing wrapped around a two-week research burst.** The idea that an agent should pay for its own thinking — that cost belongs *inside* the objective, not outside it — is the sharpest thing the corpus has seen on the cost thread, and its evaluator (per-occupation rubrics, a hard payment threshold, no heuristic fallback) is a shape you can lift directly into an LLM feature gate. But the leaderboard it is famous for is **self-run, judged by the authors' own rubrics, and priced with a single hardcoded rate for every model** — so the `$15K in 11 hours` headline is a simulation artifact, not evidence. Read it, steal the two ideas, and do not cite its numbers.
