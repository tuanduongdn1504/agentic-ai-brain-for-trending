# (C) msaad00/agent-bom — Phase 0 + Phase 0.9 STRICT verdict (v157)

**Subject:** `msaad00/agent-bom` — https://github.com/msaad00/agent-bom
**Date:** 2026-06-05 · **Routine:** v2.6 (§31 + §35 + §37)
**Requested:** "build LLM wiki for msaad00/agent-bom with related topic: macOS app to manage AI Bill of Materials" (same ask as v156).
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) MODERATE (firm, flagged for audit) · (c) STRONG · (d) STRONG.

---

## Phase 0 — scope gate
**On-goal (adjacent-but-real; firmer than v156).** agent-bom = an **AI supply-chain security scanner + self-hosted control plane** that "builds an AI BOM across agents, MCP servers, tools, packages, credential env-names, cloud, runtime, and skills" → findings + compliance evidence + blast-radius exposure graph. Its named core is an **AI-BOM generator** = the genuine **2nd independent instance** of the standalone minted at v156 (Trusera/ai-bom). **Independent, NOT a fork** (no Trusera/ai-bom mention; original work). It is **also** an MCP server (63 tools) + a runtime MCP gateway — so it both *audits* and *serves/governs* the agent stack. Related topic (macOS-app-to-manage-AIBOM) → still **no native app exists**; see the related-topic page (references the v156 landscape).

## Phase 0.9 STRICT — four axes

### (a) Cultural-peer / geographic — **FAIL**
`msaad00` — GitHub handle only; **no real name, location, company, or cultural/geographic signal**; not a Foundational-Vendor-Direct-Source ((a)-7). **(a) FAIL.** No (a)-rescue attempted — (b) carries the goal-aligned include (the v150/v156 shape). No axis minted from a bare handle (v139/v150/v152/v156 discipline).

### (b) Goal-relevance — **MODERATE (firm, flagged for audit challenge)** — load-bearing
**Same domain as v156, same MODERATE call, a touch firmer — and called on merits (§35 already clear → no inflate-incentive).**
- **Clears FAIL → MODERATE:** its entire subject IS the agentic ecosystem (inventories agents/MCP/tools/skills; blast-radius graph linking packages→servers→tools→creds→agents) and supply-chain/governance visibility is a real dimension of *operating* agentic software (the v156 reasoning). NOT off-goal like Expensify/OpenCut/FreeDomain (their subject is unrelated to agents).
- **Firmer than v156 (but still MODERATE, not STRONG):** unlike v156 (which only *detects* MCP servers — passive audit), agent-bom **(i)** exposes **63 MCP tools** so an agent can drive the scanner (the v149-Scrapling capability-FOR-agents direction) and **(ii)** runs a **runtime MCP gateway** that enforces policy on live agent traffic (operating-and-governing the stack, not just auditing). That pushes it closer to the STRONG line.
- **Held MODERATE, not STRONG:** center of gravity is **security / supply-chain / compliance / governance** (tagline leads with "security scanner"); the 63 MCP tools are **read-mostly** (it exposes its *audit* data to agents, not a build capability — 3 write "Shield" actions only); the runtime gateway is **optional/secondary** ("scoped to where enforcement is worth the operational cost"). For THIS vault's Claude-Code-mastery goal it's adjacent-domain → architecture-study/awareness, not a daily build tool. The v147/v156 borderline-MODERATE shape; flagged for the next audit to overturn to WEAK/off-goal.

### (c) Instructive engineering — **STRONG**
6 surfaces (CLI/CI + REST API + 63-tool MCP server + dashboard + runtime proxy/gateway + Python/TS clients); blast-radius dependency-graph model; **CycloneDX/SPDX/SARIF/JSON/HTML/Markdown/compliance-bundle** output; Helm/EKS/Docker/Postgres/tenant-scope/audit-logs; OpenSSF Scorecard + threat-model + pentest-readiness docs. **2,351 commits / 111 releases / v0.88.5** = more heavily built than v156 ai-bom (279 commits). Apache-2.0. **STRONG** (clearly). ⚠️ Engagement-deficit-extreme (21★ / 0 watchers despite all that) — an honest provenance flag, not a quality knock.

### (d) Corpus connectivity — **STRONG**
- **PRIMARY: strengthens the v156 "AI Supply-Chain Inventory / AI-BOM Generator" standalone → N=2** (PROMOTION-ELIGIBLE at N=3); two sub-flavors (pure-scanner v156 vs scanner+runtime-control-plane v157). See `(C) Pattern-Library-Phase-4b.md`.
- **Pattern #18 B1 MCP — genuine instance (NOT inverse, unlike v156):** agent-bom IS an MCP server (63 tools, `agent-bom mcp server`; Glama-listed). N+1 to the dense B1 line. (It *also* detects MCP servers — both directions.)
- **Pattern #66 supply-chain** (purest-instance, again; the blast-radius graph is a sophisticated supply-chain model) + **Pattern #78 standards** (CycloneDX/SPDX/SARIF) + **Pattern #84 multi-surface** (6) + **OpenClaw/clawhub agent-skill** (the v149/v121 parallel-registry thread; NOT a 57k agentskills.io implementer) + **Library-vocab #16 Engagement-Deficit-Extreme** (21★/0-watchers vs 2,351 commits).
- **LV-C1 #21 — weak/adjacent, NOT counted** (msaad00 is an individual + "no managed cloud offering in this repository today" → open-source-first, not a clear commercial-platform funnel; weaker than v156's Trusera).

---

## §35 — Soft Off-Goal-Rate Ceiling — **STAYS CLEAR**
- Rolling-3-ship window after v157 = **{v155 GA, v156 GA, v157 GA} = 0 OG → CLEAR** (5 consecutive goal-aligned ships).
- Ceiling was ALREADY clear before this ship → **zero §35 incentive to inflate (b)** → verdict on merits (the v152 anti-launder discipline, pressure absent).
- **NOT an override** → override-frequency UNCHANGED (7-in-20 trailing; lifetime 10). The next audit's mandated override review stands; v157 adds nothing.

## §37 — Fact-provenance
≈**21★** / 8 forks / 0 watchers / 14 open issues / **2,351 commits** / **111 releases** (latest **v0.88.5**, Jun 1 2026) / Apache-2.0 / Python 87.2% (+ TypeScript 11.3%) (page-stated as of 2026-06 via WebFetch — **NOT independently API-verified §37.4**; env mocks the GitHub API). Creation date not stated → age/velocity unestablished → **NOT a #52 claim** (21★ is tiny). ⚠️ Build-vs-traction mismatch (2,351 commits / 111 releases vs 21★ / 0 watchers) = engagement-deficit-extreme. Owner `msaad00` (handle only).

## Streak (v2.6 §32)
GA:19 · OG:11 [7 ov] → **GA:20 · OG:11 [7 ov]** (20th GOAL-ALIGNED PASS; NOT an override; "49+3\*" frozen @v125). Five consecutive goal-aligned ships (v153–v157).

## Pattern Library — see `(C) Pattern-Library-Phase-4b.md`
**PRIMARY** = the v156 AI-BOM-generator standalone **N=1 → N=2** (a strengthening, NOT a mint). **§28: 0 new standalones; registry 06 §C row ACTUALLY edited (rule-5) + §F log.** NO new top-level Pattern; NO confirmed-count change (46 patterns / 9 Library-vocab CONFIRMED).

## Pilot
**READ-leaning pilot candidate** (slightly higher-friction than v156). `pip install agent-bom && agent-bom agents -p . -f html` is reversible and shows your own AI stack's blast-radius inventory; the MCP-server mode (`agent-bom mcp server`) plugs into Claude Code so an agent can query the AI-BOM (the genuinely interesting bit). `install-snapshot` first. ⚠️ Two AI-BOM scanners now catalogued (v156 + v157), ZERO piloted — pick one and run a scan, don't catalogue a third.

## Honest non-claims
- (b) MODERATE (firm), flagged for audit — NOT inflated to STRONG (and §35 already clear → no incentive).
- (a) FAILS (handle only) — no axis minted.
- PRIMARY is a **strengthening** of the v156 standalone (N=2), **NOT** a new mint — §28 cap used at 0; independent 2nd instance (different author + scanner-vs-control-plane sub-flavor), not a fork, not manufactured.
- The runtime-MCP-gateway / blast-radius-graph is recorded as the v157 **sub-flavor** + an OBSERVATION (candidate future standalone at N=2), **NOT** minted now (anti-inflation; v124/v155 strengthen-over-discover discipline).
- Pattern #18 B1 MCP is a **genuine** server instance here (contrast v156's inverse/detect-only).
- LV-C1 #21 weak/adjacent, NOT counted; OpenClaw skill NOT a 57k claim; NOT a #52 claim.
- The related-topic macOS app **does not exist** — landscape/gap analysis, flagged.
- NO confirmed-count change (46 patterns / 9 Library-vocab CONFIRMED).
