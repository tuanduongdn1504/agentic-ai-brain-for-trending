# ai-bom — Beginner Analysis (project CLAUDE.md)

**Subject:** `Trusera/ai-bom` ("AI Bill of Materials") (v156 wiki ship, 2026-06-05).
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) MODERATE (borderline, flagged for audit) · (c) STRONG · (d) STRONG.
**Routine:** v2.6 (§31/§35/§37).
**Requested:** "build LLM wiki for https://github.com/Trusera/ai-bom with related topic macOS app to manage AI Bill of Materials."

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis verdict + §35 + §37 + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY: 1 NEW Library-vocab standalone (CORPUS-FIRST AI-BOM generator); registry 06 §C edited.
- `02 Wiki/index.md` — the knowledge page.
- `02 Wiki/(C) related-topic-macOS-app-to-manage-AI-BOM.md` — the operator-requested related topic (landscape + gap: **no native macOS app exists**).

## One-paragraph summary
**"Discover every AI agent, model, and API in your infrastructure."** An open-source **AI Bill of Materials** scanner (Apache-2.0; Python 65.9% + TS + Go): point it at a codebase / container / cloud account / n8n workflow / Jupyter notebook / GitHub Actions, and its **13 auto-registered scanners** inventory the AI components (LLM providers incl. **Anthropic**, agent frameworks LangChain/CrewAI/AutoGen/LangGraph, **MCP servers**, model refs, API keys, cloud AI, containers), **risk-score** them (0–100), check EU AI Act / OWASP / license compliance, and emit **CycloneDX 1.6 / SPDX 3.0 / SARIF 2.1.0** (+ HTML/MD/CSV/JUnit/JSON). 7 distribution surfaces (CLI/pipx · Docker · Python lib · GitHub Action · n8n node · VS Code ext · 3 SDKs); 651+ tests / 80%+ coverage; v3.1.0. It is **the open-source foundation of the commercial Trusera platform** ("Securing the Agentic Service Mesh"). Goal-aligned as the **governance/supply-chain-inventory layer** of the operate-your-agent-stack tool family.

## Verdict rationale
- **(b) MODERATE (borderline, flagged for audit)** = its *entire subject matter* is the agentic ecosystem (it inventories agents/MCP/LLM-providers) and supply-chain/governance visibility ("know what AI is in your stack" — EU AI Act, OWASP) is a real dimension of *operating* agents at scale → a coherent same-family member alongside agent-observability (v154) and account-mgmt (v153). **MODERATE-not-STRONG** = center of gravity is security/compliance/governance, it's an audit/scanner you don't *build with*, NOT a capability-for-agents (v149 STRONG basis) and NOT a skill-authoring exemplar (v98/v124 MODERATE basis) → adjacent-domain, architecture-study/awareness value for THIS vault. Called on merits (§35 already clear → zero inflate-incentive). The v147 borderline-MODERATE shape; flagged for audit to overturn to WEAK/off-goal if it disagrees.
- **(a) FAIL** = `Trusera` security-vendor org, no individual/location/cultural-peer signal, not (a)-7 (third-party startup, not a substrate vendor). No (a)-rescue (b carries the include); no axis minted from a bare org name.
- (c) STRONG (13 scanners + Pydantic + risk-scorer + compliance modules + 9 output formats + 651 tests/80% + 7-surface distribution; Apache-2.0; v3.1.0). (d) STRONG (CORPUS-FIRST AI-BOM generator + Pattern #66 purest supply-chain instance + #78 standards + #18 B1 MCP INVERSE + #84 multi-surface + #82 + LV-C1 #21 open-core adjacency).

## §35 / streak
**§35 STAYS CLEAR** — window {v154 GA, v155 GA, v156 GA} = 0 OG (4 consecutive goal-aligned ships). NOT an override → override-frequency UNCHANGED (7-in-20 trailing; lifetime 10). Streak GA:18·OG:11 [7 ov] → **GA:19·OG:11 [7 ov]** (19th GOAL-ALIGNED PASS). Breaks the 3-in-a-row desktop-app-to-manage-AI-coding-tools niche run (v153/v154/v155) — different shape (CLI/library governance scanner).

## Pattern Library
**PRIMARY: 1 NEW Library-vocab standalone — "AI Supply-Chain Inventory / AI Bill-of-Materials Generator (governance/compliance layer for the agentic stack)" N=1 CORPUS-FIRST** (FILED to registry 06 §C). The corpus had every other operate-your-agent-stack layer (provider-aggregation / capability / orchestration / account-mgmt / observability / ambient-status) but NO governance/supply-chain-inventory layer; ai-bom adds it. Distinct from Pattern #66 supply-chain-*awareness* (a within-subject discipline — this is a dedicated AI-BOM *generator*), v140 tool-tiers, the agentskills.io chain, #20 Token-Economy. PROMOTION-ELIGIBLE at N=2 (a 2nd AI-BOM generator). **§28: 1 of ≤2 new standalones; registry 06 ACTUALLY edited (rule-5).** NO confirmed-count change (46 patterns / 9 Library-vocab CONFIRMED). Observations (NOT minted): Pattern #66 purest-supply-chain instance + N+1; Pattern #18 B1 MCP **INVERSE** (detects MCP servers, does NOT serve one — the v154 observes-vs-controls / v149 detects-vs-serves direction; NOT counted as a B1 server instance); Pattern #78 Living-Domain-Standards (CycloneDX 1.6/SPDX 3.0/SARIF 2.1.0/EU-AI-Act-Art-53); Pattern #84 multi-surface (7 surfaces); Pattern #82 quantitative-marketing; **LV-C1 #21 ADJACENT** (open-core foundation of a commercial platform — an adjacent flavor of official-tooling-for-own-product, NOT counted); operate-your-agent-stack meta-map now large enough to formalize at audit (flagged, NOT minted); niche-run BROKEN (different shape from v153/v154/v155).

## Provenance (§37)
≈**246★** / 68 forks / 5 watchers / 7 open issues / 8 open PRs / **279 commits** / latest release **v3.1.0 (Feb 12, 2026)** / Apache-2.0 / Python 65.9% (+ TS 28.3% + Go 5.3%) — page-stated as of 2026-06 via WebFetch, **NOT independently API-verified §37.4** (env mocks the GitHub API). Creation date unstated → velocity/age unestablished → **NOT a #52 claim** (246★ modest regardless). Owner `Trusera` (security vendor; ai-bom = OSS foundation of the commercial Trusera platform).

## Related topic (operator ask)
**"macOS app to manage AI Bill of Materials"** — finding: **no dedicated native macOS app exists** (as of 2026-06). The space is CLI tools (ai-bom, Cisco AI Defense OSS) + commercial web platforms (Mend/Snyk/JFrog/Wiz/Cycode/Sysdig/Palo Alto), all runnable on macOS but none native. On a Mac you manage AI-BOM via the `ai-bom` CLI (pipx) + its Flask web dashboard + Docker + the VS Code extension. The gap = a native menu-bar/tray manager (scheduled re-scan + risk badge + diff-over-time + CycloneDX export) wrapping the `ai-bom` CLI — the **governance-layer analog** of the corpus's v153 Tauri / v154 Swift / v155 Electron native-desktop management surfaces for AI coding tools. Landscape + gap analysis (no product exists), flagged as such. Full page: `02 Wiki/(C) related-topic-macOS-app-to-manage-AI-BOM.md`.

## Pilot
**READ-leaning pilot candidate** — `pipx install ai-bom && ai-bom scan .` (or `docker run … scan /scan`) is reversible and shows what a scanner finds in your own code; the CycloneDX/SPDX/SARIF output design is worth reading. Daily value to a Scrum-coach-mastering-Claude = awareness/architecture-study, not continuous operation. `install-snapshot` first if you `pipx install`. ⚠️ Standing note: 4 goal-aligned ships running, ~zero piloted — one `ai-bom scan` would be a cheap way to break that.

Shipped on branch `wiki/v156-ai-bom` off main (at v155 `5f84673`). Not auto-merged — operator merges.
