# (C) Trusera/ai-bom — Phase 0 + Phase 0.9 STRICT verdict (v156)

**Subject:** `Trusera/ai-bom` — https://github.com/Trusera/ai-bom
**Date:** 2026-06-05 · **Routine:** v2.6 (§31 + §35 + §37)
**Requested:** "build LLM wiki for Trusera/ai-bom with related topic: macOS app to manage AI Bill of Materials."
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) MODERATE (borderline, flagged for audit) · (c) STRONG · (d) STRONG.

---

## Phase 0 — scope gate
**On-goal (adjacent-but-real).** ai-bom is an **AI Bill of Materials** generator: scan a codebase/container/cloud → inventory + risk-score every AI component (agent frameworks, MCP servers, LLM providers incl. Anthropic, model refs, API keys, cloud AI) → emit SBOM-standard output (CycloneDX 1.6 / SPDX 3.0 / SARIF 2.1.0). Its entire subject matter is the AI/agent ecosystem. It is the **governance/supply-chain-inventory layer** of the "operate-your-agent-stack" tool family the corpus has been building since v149. NOT a finance/video/DNS off-goal product (its subject IS agents); NOT a skill collection / not an agent / not an MCP server it exposes. **Related topic** (macOS-app-to-manage-AIBOM) handled in `02 Wiki/(C) related-topic-macOS-app-to-manage-AI-BOM.md` — finding: no such native app exists; landscape + gap analysis.

## Phase 0.9 STRICT — four axes

### (a) Cultural-peer / geographic — **FAIL**
Owner `Trusera` = a security vendor/startup org ("Securing the Agentic Service Mesh"; trusera.dev), no individual identity / no location / no VN/Asian/declared cultural-peer signal, and **not** a Foundational-Vendor-Direct-Source ((a)-7 = Anthropic-tier substrate vendor the vault depends on; Trusera is a third-party security startup). **(a) FAIL.** No (a)-rescue attempted — (b) carries the goal-aligned include (the v150 Paseo shape: org-owner, (a) FAIL + (b) carries it). **No axis minted from a bare org name** (the v139/v142/v145/v150/v152 discipline).

### (b) Goal-relevance — **MODERATE (low/borderline, flagged for audit challenge)** — load-bearing
**The crux of this ship, and called on merits (no §35 pressure — see §35 below).**

- **Why it clears FAIL (→ MODERATE, GOAL-ALIGNED):** ai-bom's *entire subject matter* is the agentic ecosystem — it detects/inventories agent frameworks (LangChain/CrewAI/AutoGen/LlamaIndex/LangGraph), **MCP servers**, LLM providers (incl. Anthropic), and model references. "Know what AI/agents are actually in your stack" (EU AI Act Art. 53, OWASP, supply-chain risk) is a legitimate professional dimension of *operating* autonomous-agent software at scale. It is a coherent same-family member alongside the corpus's already-GOAL-ALIGNED agent-observability (v89/v109/v154) and account-management (v153) tools — the **governance/supply-chain-inventory layer** of "operate-your-agent-stack." This is NOT Expensify (a finance product with incidental Claude), OpenCut (a video editor), or FreeDomain (a DNS service) — those are off-goal because their *subject* is unrelated to agents; ai-bom's subject IS the agent stack.
- **Why it's MODERATE, not STRONG:** the center of gravity is **security/compliance/governance**, not building-or-operating coding agents; it's an **audit/scanner** you don't *build with*; it does NOT expose a capability to agents (the v149 Scrapling STRONG basis) and is NOT a skill-authoring exemplar (the v98/v124 MODERATE basis). For THIS vault's specific Claude-Code-mastery goal it's **adjacent-domain → architecture-study / awareness value, not a daily operational tool.**
- **Flagged for audit:** this is a **borderline MODERATE**, the v147 system-design-academy shape. Recorded so the next audit can overturn it to WEAK/off-goal if it disagrees. The line held: it's a *real, consistent same-family member* of the operate-your-agent-stack tools, but at the governance/awareness altitude.

### (c) Instructive engineering — **STRONG**
13 auto-registered scanners → Pydantic models (`AIComponent`/`ScanResult`) → stateless 0–100 risk scorer → compliance modules (EU AI Act/OWASP/licenses) → **9 output formats** incl. CycloneDX 1.6 / SPDX 3.0 / SARIF 2.1.0. **651+ tests / 80%+ coverage.** **7-surface distribution** (CLI/pipx · Docker · Python library · GitHub Action · n8n community node · VS Code extension · Python/TS/Go SDKs). Apache-2.0; v3.1.0; 279 commits; Python 65.9%+TS 28.3%+Go 5.3%. A mature, well-tested, standards-conformant multi-surface OSS tool. **STRONG.**

### (d) Corpus connectivity — **STRONG**
- **PRIMARY: CORPUS-FIRST AI-BOM / AI-supply-chain-inventory generator** — a NEW governance/inventory layer in the operate-your-agent-stack family (see `(C) Pattern-Library-Phase-4b.md`; filed to registry 06 §C).
- **Pattern #66 supply-chain-security** — the *purest* supply-chain subject in the corpus (it literally generates SBOMs). Observation.
- **Pattern #78 Living-Domain-Standards-Tracking** — CycloneDX 1.6 / SPDX 3.0 / SARIF 2.1.0 / EU AI Act Art. 53 versioned-standards conformance. Observation.
- **Pattern #18 B1 MCP — INVERSE** (detects MCP servers as inventory; does NOT expose/serve one — the v154 "observes vs controls" + v149 "tool-FOR-agents-vs-detects" direction). NOT counted as a B1 MCP-server instance.
- **Pattern #84 multi-distribution** (7 surfaces) + **Pattern #82 quantitative-marketing** ("60%+ undocumented," "50,000+ scanned," 13 scanners, 25+ SDKs, 651 tests). Observations.
- **LV-C1 #21 adjacency** — ai-bom is "the open-source foundation of the Trusera platform" = open-core/funnel for a commercial security platform; an *adjacent flavor* (open-core foundation) of CONFIRMED #21 (official-agent-tooling-for-own-product), NOT a clean instance → observation for the audit, NOT counted.

---

## §35 — Soft Off-Goal-Rate Ceiling — **STAYS CLEAR**
- Rolling-3-ship window after v156 = **{v154 GA, v155 GA, v156 GA} = 0 OG → CLEAR** (4 consecutive goal-aligned ships; the v151/v152 breach was resolved at v154 and stays resolved).
- **Crucially: the ceiling was ALREADY clear before this ship**, so there is **zero §35 incentive to inflate (b)** to MODERATE — the verdict is on merits (the v152 anti-launder discipline, applied with the pressure absent).
- **NOT an override** → override-frequency triggers UNCHANGED (7-in-20 trailing from v152; lifetime overrides 10 UNCHANGED). The next audit's mandated override review stands; v156 adds nothing to it.

## §37 — Fact-provenance
≈**246★** / 68 forks / 5 watchers / 7 open issues / 8 open PRs / **279 commits** / latest release **v3.1.0 (Feb 12, 2026)** / Apache-2.0 / Python 65.9% (+ TypeScript 28.3% + Go 5.3% + Shell/Makefile/HCL) (page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified §37.4**; this env mocks the GitHub API). Creation date not stated → age/velocity unestablished → **NOT a Pattern #52 claim** (246★ is modest regardless). Owner `Trusera` (security vendor; ai-bom = the OSS foundation of the commercial Trusera platform).

## Streak (v2.6 §32)
GA:18 · OG:11 [7 ov] → **GA:19 · OG:11 [7 ov]** (19th GOAL-ALIGNED PASS; NOT an override; "49+3\*" frozen @v125). Four consecutive goal-aligned ships (v153 + v154 + v155 + v156).

## Pattern Library — see `(C) Pattern-Library-Phase-4b.md`
**PRIMARY** = 1 NEW Library-vocab standalone "AI Supply-Chain Inventory / AI-BOM Generator (governance/compliance layer for the agentic stack)" N=1 CORPUS-FIRST. **§28: 1 new standalone (≤2 cap); registry 06 §C ACTUALLY edited (rule-5).** NO new top-level Pattern; NO confirmed-count change (46 patterns / 9 Library-vocab CONFIRMED).

## Pilot
**READ-leaning pilot candidate** — `pipx install ai-bom && ai-bom scan .` (or `docker run … scan /scan`) is reversible and shows what a scanner finds in your own code; the CycloneDX/SPDX/SARIF output design is worth reading. Daily value to a Scrum-coach-mastering-Claude is awareness/architecture-study, not continuous operation. `install-snapshot` first if you `pipx install`. ⚠️ Standing note: 4 goal-aligned ships running, ~zero piloted — one `ai-bom scan` would be a cheap way to break that.

## Honest non-claims
- (b) is **MODERATE, borderline — flagged for audit**, NOT inflated to STRONG; and called with §35 already clear (no incentive to launder).
- (a) FAILS (org owner, undisclosed) — not laundered, no axis minted.
- PRIMARY is **1 genuine new standalone** (the AI-BOM generator), NOT a new top-level Pattern; §28 cap used at 1 of ≤2.
- **Pattern #18 B1 MCP is INVERSE here** (detects, doesn't serve) → explicitly NOT counted as an MCP-server instance.
- **LV-C1 #21** is an *adjacent* flavor (open-core foundation) → observation, NOT counted as a clean instance.
- NOT a #52 claim (creation date unstated; metrics NOT API-verified §37.4).
- The related-topic macOS app **does not exist** — landscape/gap analysis, flagged as such.
- NO confirmed-count change (46 patterns / 9 Library-vocab CONFIRMED).
