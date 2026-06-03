# (C) D4Vinci/Scrapling — Phase 0 + Phase 0.9 STRICT verdict (v149)

**Subject:** `D4Vinci/Scrapling` — https://github.com/D4Vinci/Scrapling
**Date:** 2026-06-03 · **Routine:** v2.6 (§31 + §35 + §37)
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG

---

## Phase 0 — scope gate
**Borderline-in, resolved IN.** Scrapling's *core* is a web-scraping library (a domain that, on its own, is off goal #1). But the CURRENT release (v0.4.x) ships two **shipped, first-class agent surfaces**: a **built-in MCP server** ("to be used with AI (Claude/Cursor/etc)", `pip install "scrapling[ai]"`) and an **official agent-skill** (`/agent-skill` dir + `clawhub.ai/D4Vinci/scrapling-official`). The relationship to agents is "a capability exposed **TO** agents" (the v140 google_workspace_mcp / v143 larksuite-cli shape) — **not** "an app that internally calls an LLM" (the v123 MoneyPrinterTurbo off-goal shape). That direction is what puts it in scope and makes (b) load-bearing-positive.

**Distinctions held honestly:**
- **NOT roadmap-only** (the v146 OpenCut SKIP basis): the MCP is installable *now* via `scrapling[ai]`, v0.4.8, with a demo — a shipped product feature.
- **NOT internal dev-exhaust** (the v122 dograh / v142 OrcaSlicer basis): this isn't a `.claude/` the team uses internally; it's a product capability aimed *at* external agents.

## Phase 0.9 STRICT — four axes

### (a) Cultural-peer / geographic — **FAIL**
- Owner `D4Vinci` = **Karim Shoair** (CS degree, 10+ yrs; author of several OSS projects). Inferred **MENA / Arabic-speaking** (the repo ships a `docs/README_AR.md` Arabic README; commonly associated with Egypt) — **but undeclared on the repo page** (confidence: inference).
- MENA / North-African is **not a registered cultural-peer (a) axis** and is **not (a)-7**. Per the v139 image-extender precedent ("North-African/ME inferred-only, no (a)-rescue, no axis minted") and the v97→v115 (a)-8 retirement lesson, **(a) FAILs and NO new axis is minted** for a single subject. No rescue.
- (a) FAIL is immaterial to the verdict — like v140 (a FAIL US individual), v143 (a FAIL corporate org), v144 (a FAIL undisclosed individual), this is a GOAL-ALIGNED-on-(b) INCLUDE.

### (b) Goal-relevance — **STRONG** (load-bearing)
- **Shipped MCP server for AI agents** (`scrapling[ai]`): "extract targeted content before passing it to the AI (Claude/Cursor/etc)." Gives a coding agent a real new capability — robust, stealth-capable web-data extraction — directly on goal #1 (infrastructure for autonomous coding agents). Structurally the v140 google_workspace_mcp relationship (MCP server exposing a capability to agents → GOAL-ALIGNED, (b) STRONG).
- **Official agent-skill** for the vendor's own product (`/agent-skill` + clawhub/OpenClaw "scrapling-official") — the v114 gsap / v126 Every vendor-DevRel-via-agent-tooling shape.
- Also **directly vault-applicable**: a Scrapling MCP would harden the vault's own research/ingestion step (the `WebFetch`/`WebSearch` used to build this wiki is a thin version of it).
- **STRONG not STRONGEST:** the core product is a general-purpose scraping library, and the agent surface (MCP + skill) is one delivery mode among several (most users use the Python library directly). So it's a capability-provider/connector, not the agent-building substrate/methodology itself (the v126/v131 STRONGEST bar). **⚠️ Flagged for the next audit to challenge** the dual nature (scraping library vs agent tooling) — held at STRONG on a principled basis, not to clear §35 (a clean §35 clearance only needs goal-aligned, which STRONG already is).

### (c) Instructive engineering — **STRONG**
A genuinely well-built library: three fetcher tiers (HTTP **Fetcher** / **DynamicFetcher** browser / **StealthyFetcher** anti-bot + Cloudflare-solving + impersonation), a Scrapy-like **Spider framework** (concurrent crawl, multi-session, pause/resume, streaming), **adaptive/self-healing parsing** (relocates elements after markup changes), multi-modal selection (CSS/XPath/filter/text-regex), claimed perf wins over BeautifulSoup/Selenium, full type coverage (PyRight/MyPy). Python 99.9%; BSD-3-Clause; an interactive `scrapling shell` REPL + an `extract` CLI; Docker image. STRONG.

### (d) Corpus connectivity — **STRONG**
- **LV-C1 Vendor-Official Agent-Tooling for Own Product → N=3** (v114 gsap + v126 Every + v149 Scrapling); library-vendor sub-type now N=2 (v114+v149). PRIMARY — see Phase 4b.
- **Pattern #18 B1 MCP** — N+1 (ships an MCP server). The B1 line is now dense (v66/v70/v119/v132/v134/v140/v141/v144/v149) → MCP-server tier-sub-archetype review overdue (audit).
- **Pattern #84 multi-harness / agent-tooling** — N+1 (MCP + agent-skill, Claude/Cursor/OpenClaw).
- **OpenClaw/clawhub parallel agent-skill registry** — sibling-standard to agentskills.io (the v121 CodexKit "parallel standard" thread); observation, NOT a 57k implementer claim.
- Capability-provider-for-agents neighbors: v140 google_workspace_mcp, v144 headroom, v143 larksuite-cli.

---

## §35 — Soft Off-Goal-Rate Ceiling — **CLEARS THE BREACH**
- Before v149: rolling-3-ship window {v146 OG, v147 GA, v148 OG} = **2 OG → BREACHED** (v146 = 1st `[ceiling-override]`, v148 = 2nd consecutive; v148 deepened it). §35.2 mandate carried from v148: **v149 MUST be GOAL-ALIGNED.**
- After a GOAL-ALIGNED v149: window {v147 GA, v148 OG, v149 GA} = **1 OG ≤ 1 → CLEAR.** v149 scrolls v146 out.
- v149 is a clean goal-aligned ship — **NOT a ceiling-override.** Override-frequency triggers UNCHANGED (lifetime overrides still 9; v149 adds none).

## §37 — Fact-provenance
≈**59.4k★** / 5.7k forks / 226 watchers / 10 open issues / v0.4.8 (May 11 2026) / 1,447 commits / BSD-3-Clause / Python 99.9% (page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified §37.4**; this env mocks the GitHub API). Created ~late-2024 (project public history; **not verified here**) → velocity/age unestablished → **NOT a Pattern #52 claim** (even though 59.4k★ is large; no verified velocity). Author identity Karim Shoair (D4Vinci); MENA/Arabic-speaking **inferred** (README_AR), location undeclared → (a) FAIL, no axis minted.

## Streak (v2.6 §32)
GA:13 · OG:9 [6 ov] → **GA:14 · OG:9 [6 ov]** (v149 = 14th goal-aligned PASS; §35 CLEARED; "49+3\*" frozen @v125; lifetime overrides 9 UNCHANGED — v149 is not an override).

## PILOT — Tier-1, genuinely
A real pilot for THIS vault (joins v144 headroom as a directly-vault-applicable goal-aligned ship). The Scrapling MCP hardens the vault's own web research/ingestion. Path: `pip install "scrapling[ai]"` → `scrapling install` (browser binaries) → register the MCP with Claude → trial `stealthy-fetch`/extract on a real page; reversible. **`install-snapshot` recommended** (pip + a browser-download postinstall step). Even reading the adaptive-selector + stealth-fetch-tier design is worth borrowing.

## Honest non-claims
- (a) genuinely FAILS (MENA/Arabic-speaking inferred-only, undeclared, not a registered axis, not (a)-7; no mint).
- (b) STRONG-not-STRONGEST (general-purpose scraping library core; agent surface is one delivery mode) — flagged for audit challenge.
- Metrics page-stated, NOT API-verified; NOT a #52 claim.
- Phase 4b: **0** new standalones + **1** cluster strengthening (LV-C1 → N=3, promotion-eligible — audit's call); NO new top-level Pattern, NO tier sub-archetype, NO confirmed-count change.
