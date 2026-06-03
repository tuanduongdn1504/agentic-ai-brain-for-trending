# (C) anthropics/financial-services ("Claude for Financial Services") — Phase 0 + Phase 0.9 STRICT verdict (v141)

**Subject:** `anthropics/financial-services` — https://github.com/anthropics/financial-services
**Date:** 2026-06-03 · **Routine:** v2.6 (§31 2-tier INCLUDE + §35 ceiling + §37 fact-provenance)
**Verdict:** **GOAL-ALIGNED INCLUDE 4/4** — (a) PASS [(a)-7] · (b) STRONG · (c) STRONG · (d) STRONG

---

## Phase 0 — scope gate
In scope, and squarely so. The subject is **Anthropic's own production reference implementation of Claude *agents*** — Managed Agents API deployment, the Agent SDK orchestration loop, agent-definition (`agent.yaml`) + skills + MCP connectors, packaged as Cowork/Claude-Code plugins. That is the dead-center of goal #1 ("master Claude and autonomous agents for software development"). The financial-services *domain* is the worked example; the transferable content is agent architecture + deployment, by the foundational vendor.

## Phase 0.9 STRICT — four axes

### (a) Cultural-peer / geographic — **PASS via (a)-7 Foundational-Vendor-Direct-Source**
- Owner = **`anthropics`, the official Anthropic organization** (confidence: stated). Anthropic is the vault's substrate vendor (Claude / Claude Code).
- **(a)-7 Foundational-Vendor-Direct-Source** is a CONFIRMED Phase-0.9 (a) sub-axis (formal admission via N=3 promotion v92+v93+v95). This is the ~5th Anthropic-direct-org subject in the v60+ window (claude-for-legal + anthropics/skills v93 + claude-plugins-official v95 + claude-cookbooks + financial-services) → (a)-7 N+1 administrative strengthening. PASS (not a cultural-peer geographic PASS — the vendor-direct axis).

### (b) Goal-relevance — **STRONG** (load-bearing)
- A reference implementation that exercises **the full Anthropic agent stack**: Claude API + **Managed Agents API** (`/v1/agents`, headless deployment) + **Agent SDK** (multi-agent orchestration) + **Claude Skills** + **MCP** (11 data connectors) + Cowork + Claude Code plugin marketplace + a documented multi-agent **orchestrate.py** event loop with **leaf-worker subagents** + **steering events / `handoff_request` routing**.
- **STRONG, not STRONGEST:** the *domain* is financial services (investment banking / equity research / PE / wealth mgmt / fund admin) — off Storm Bear's software-dev/Scrum vertical, and you cannot operationally run the agents without paid financial-data MCP connectors + finance data. So its value to *this* vault is as a **READ/architecture-study reference** (very high) rather than an operational install (low) — the v113 calibration (STRONG, READ-pilot). The agent-architecture is what carries (b); the finance domain tempers it from STRONGEST.

### (c) Instructive engineering — **STRONG**
An exemplary, production-grade reference:
- **Dual deployment from one source** — same system prompt + skills install as a Cowork plugin OR deploy through the Managed Agents API ("you choose where it runs").
- **Single-source skill → propagate-to-bundled-agents + drift CI** — `sync-agent-skills.py` propagates a vertical's skill edits into the bundled agents; `validate.py` does **bundled-skill drift detection**; `check.py` does manifest linting + cross-file reference resolution. (Pattern #81 manifest-drift-as-CI-concern, the *good* pole.)
- 10 named agents, 7 vertical plugins + 2 **partner-built** plugins (LSEG, S&P Global), 11 MCP connectors, MS-365 add-in provisioning, `orchestrate.py` multi-agent reference loop, `deploy-managed-agent.sh`. Apache-2.0; Python 79.7% (+ Shell/JS/PowerShell); markdown/YAML skill+agent definitions, no build step. CLAUDE.md + `.claude-plugin/` present.

### (d) Corpus connectivity — **STRONG**
- **Pattern #84 84c.1 Marketplace-Plugin-Install (CONFIRMED N=6)** — Cowork plugin marketplace + `claude plugin marketplace add` / `claude plugin install`. N+1 (sibling to v95 claude-plugins-official, v126 compound-engineering).
- **Pattern #18 sub-mechanism B1 "MCP"** — **11 data-connector MCP integrations** (Daloopa/Morningstar/S&P/FactSet/Moody's/MT Newswires/Aiera/LSEG/PitchBook/Chronograph/Egnyte/Box) = one of the densest MCP-connector instances in the corpus. Strong instance (MCP cluster v66/v70/v119/v132/v134/v140).
- **(a)-7 cluster** (v92/v93/v95) + **methodology-influence-tier** Anthropic-direct lineage.
- **Pattern #81 manifest-drift-as-CI** good pole (v64 anchor) + **Pattern #57** plugin-marketplace/skills chain (Claude Skills, .md — not the agentskills.io SKILL.md spec, so NOT a 57k `npx skills add` implementer).

---

## §35 — Soft Off-Goal-Rate Ceiling
**STAYS CLEAR.** Rolling-3-ship window after v141 = **{v139 OG, v140 GA, v141 GA} = 1 OG ≤ 1 → CLEAR.** (The two `aBaiAutoplus` declines were NOT ships — refused on safety+off-goal grounds — and do not count toward the window.) v141 is GOAL-ALIGNED; NOT a ceiling-override. Override-frequency triggers UNCHANGED (lifetime 5; v141 not an override).

## §37 — Fact-provenance (volatile metrics)
≈**29.5k★** / 4.1k forks / 231 watchers / Apache-2.0 / Python 79.7% (as of 2026-06, repo page — **stated, NOT API-verified §37.4**; env mocks the GitHub API). High-star (typical of an Anthropic-official repo) but velocity/age not established → **NOT a Pattern #52 claim**. Owner = anthropics official org (**stated**).

## Streak (v2.6 §32)
GA:9 · OG:5 [2 ov] → **GA:10 · OG:5 [2 ov]** (v141 = 10th goal-aligned PASS; "49+3\*" frozen @v125).

## Honest non-claims
- (a) PASSes on the **vendor-direct (a)-7 axis**, NOT a geographic cultural-peer — recorded as such.
- (b) is STRONG-not-STRONGEST (finance domain → READ/architecture-study value for this vault, not an operational install; the v113 calibration).
- NOT a #52 promotion (29.5k★ unverified, no velocity window).
- NOT an agentskills.io 57k `npx skills add` implementer (Claude Skills as `.md`, no SKILL.md spec / vercel-labs CLI).
- Phase 4b mints **1** Library-vocab standalone (§28 1 ≤ 2); NO new top-level Pattern, NO new tier sub-archetype, NO Pattern-Library confirmed-count change (the (a)-7 + #84-84c.1 + #18-B1 + #81 moves are administrative N+1 strengthenings of CONFIRMED items).
