# agent-bom — Beginner Analysis (project CLAUDE.md)

**Subject:** `msaad00/agent-bom` ("Agent BOM") (v157 wiki ship, 2026-06-05).
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) MODERATE (firm, flagged for audit) · (c) STRONG · (d) STRONG.
**Routine:** v2.6 (§31/§35/§37).
**Requested:** "build LLM wiki for https://github.com/msaad00/agent-bom with related topic macOS app to manage AI Bill of Materials" (same ask as v156).

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis verdict + §35 + §37 + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY: the v156 AI-BOM-generator standalone → N=2 (a strengthening, NOT a mint); registry 06 §C edited.
- `02 Wiki/index.md` — the knowledge page.
- `02 Wiki/(C) related-topic-macOS-app-to-manage-AI-BOM.md` — the operator-requested related topic (still **no native macOS app**; references the v156 landscape + adds agent-bom specifics).

## One-paragraph summary
**"Open security scanner and self-hosted control plane for AI/MCP infrastructure."** An open-source (Apache-2.0; Python 87.2% + TS) **AI supply-chain security scanner + control plane** that "builds an AI BOM across agents, MCP servers, tools, packages, credential env-names, cloud, runtime, and skills" → findings + compliance evidence + a **blast-radius** exposure graph (package → MCP-server → tools → creds → agents). 6 surfaces: CLI/CI (GitHub Action) · REST API · **MCP server (63 tools + 6 resources + 6 prompts, `agent-bom mcp server`; Glama-listed; OpenClaw skill)** · dashboard · runtime proxy/gateway (live MCP-traffic policy enforcement) · Python/TS clients. Output JSON/SARIF/CycloneDX/SPDX/Markdown/HTML/compliance-bundles. `pip install agent-bom` + Docker/Helm/EKS/Postgres/self-hosted `serve`. **Independent — NOT a fork of Trusera/ai-bom** (no mention; original work). Goal-aligned as the governance/supply-chain-inventory layer of the operate-your-agent-stack family. Owner `msaad00` (handle only). **2,351 commits / 111 releases / v0.88.5 — but only 21★ / 0 watchers** (engagement-deficit-extreme).

## Verdict rationale
- **(b) MODERATE (firm, flagged for audit)** = same domain + reasoning as v156, a touch firmer: agent-bom's subject IS the agent ecosystem AND it **serves 63 MCP tools to agents** (capability-FOR-agents, the v149 direction) + **enforces policy on live MCP traffic** (operating/governing the stack, not just auditing). **MODERATE-not-STRONG** = center of gravity is security/supply-chain/compliance; the MCP tools are read-mostly (exposes *audit* data, not a build capability); the runtime gateway is optional/secondary. Adjacent-domain → architecture-study/awareness for THIS vault. Called on merits (§35 already clear → no inflate-incentive). v147/v156 borderline-MODERATE shape; flagged for audit.
- **(a) FAIL** = `msaad00` handle only; no name/location/cultural-peer signal; not (a)-7. No rescue, no axis minted (b carries the include).
- (c) STRONG (6 surfaces + blast-radius graph + CycloneDX/SPDX/SARIF + Helm/EKS/Postgres + OpenSSF Scorecard + threat-model/pentest docs; 2,351 commits / 111 releases = more heavily built than v156). (d) STRONG (strengthens v156 AI-BOM standalone → N=2 + Pattern #18 B1 MCP GENUINE-server (contrast v156 inverse) + #66 purest supply-chain + #78 standards + #84 multi-surface + OpenClaw skill + #16 engagement-deficit).

## §35 / streak
**§35 STAYS CLEAR** — window {v155 GA, v156 GA, v157 GA} = 0 OG (5 consecutive goal-aligned ships). NOT an override → override-frequency UNCHANGED (7-in-20 trailing; lifetime 10). Streak GA:19·OG:11 [7 ov] → **GA:20·OG:11 [7 ov]** (20th GOAL-ALIGNED PASS). ⚠️ 2nd consecutive AI-BOM ship (v156+v157); the corpus is thickening the AI-BOM niche, ZERO piloted.

## Pattern Library
**PRIMARY: the v156-minted standalone "AI Supply-Chain Inventory / AI-BOM Generator (governance/compliance layer for the agentic stack)" → N=2** (v156 Trusera/ai-bom pure-scanner + v157 msaad00/agent-bom scanner+control-plane; independent, NOT a fork) → **PROMOTION-ELIGIBLE at N=3.** Two sub-flavors recorded: passive pure-scanner/inventory (v156) vs active scanner + runtime control-plane/enforcement-gateway (v157); one-class-or-two is an N=3-audit question. **§28: 0 new standalones** (a strengthening, NOT a mint); registry 06 §C row updated N=1→N=2 (rule-5). NO confirmed-count change (46 patterns / 9 Library-vocab CONFIRMED). Observations (NOT minted): **Pattern #18 B1 MCP GENUINE server instance** (63 tools — contrast v156's inverse/detect-only; the B1 line densifies, MCP-server tier-sub-archetype review even more OVERDUE); runtime-MCP-enforcement-gateway + blast-radius-graph = the v157 sub-flavor + candidate-future-standalone (NOT minted; anti-inflation); Pattern #66 purest-supply-chain (again) + N+1; Pattern #78 standards (CycloneDX/SPDX/SARIF); Pattern #84 multi-surface (6); OpenClaw skill + Glama MCP listing (v149/v121 parallel-registry thread, NOT a 57k claim); Library-vocab #16 Engagement-Deficit-Extreme N+1 (21★/0-watchers vs 2,351 commits — the v151/v152 high-commits-low-stars shape); LV-C1 #21 weak/adjacent (individual owner, no clear commercial funnel — NOT counted); 2nd-consecutive-AI-BOM niche note.

## Provenance (§37)
≈**21★** / 8 forks / 0 watchers / 14 open issues / **2,351 commits** / **111 releases** (latest **v0.88.5**, Jun 1 2026) / Apache-2.0 / Python 87.2% (+ TypeScript 11.3%) — page-stated as of 2026-06 via WebFetch, **NOT independently API-verified §37.4** (env mocks the GitHub API). Creation date unstated → velocity/age unestablished → **NOT a #52 claim** (21★ tiny). ⚠️ Engagement-deficit-extreme (heavy build, near-zero traction). Owner `msaad00` (handle only).

## Related topic (operator ask)
**"macOS app to manage AI Bill of Materials"** — finding UNCHANGED from v156: **no dedicated native macOS app exists** (as of 2026-06). agent-bom widens the *non-native* management surface (web dashboard via `agent-bom serve` + REST + 63-tool MCP server + runtime gateway) but ships no `.app`/menu-bar/tray. agent-bom's MCP server *sharpens* the gap-fill idea: a native Mac menu-bar manager could call its 63 MCP tools (rather than shelling a CLI) = the governance-layer analog of v153 Tauri / v154 Swift / v155 Electron. Landscape+gap analysis (no product exists), flagged. Full landscape in the v156 related-topic page (referenced).

## Pilot
**READ-leaning pilot candidate** (slightly higher-friction than v156). `pip install agent-bom && agent-bom agents -p . -f html -o report.html` is reversible and shows your own AI stack's blast-radius inventory; the MCP-server mode (`agent-bom mcp server`) plugs into Claude Code so an agent can query the AI-BOM (the genuinely interesting bit). `install-snapshot` first. ⚠️ Two AI-BOM scanners now catalogued (v156 ai-bom + v157 agent-bom), ZERO piloted — pick one and run a scan, don't catalogue a third.

Shipped on branch `wiki/v157-agent-bom` (stacked on the unmerged v156 branch). Not auto-merged — operator merges (stack order v156 → v157).
