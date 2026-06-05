# (C) msaad00/agent-bom — "Agent BOM" (v157 wiki)

> **Status: GOAL-ALIGNED INCLUDE 3/4** ((a) FAIL · (b) MODERATE [firm, flagged for audit] · (c) STRONG · (d) STRONG). An open-source AI-supply-chain security scanner **+ self-hosted control plane** that builds an AI-BOM across agents/MCP/tools/packages/cloud, links findings to "blast-radius" exposure paths, and can run as an MCP server + runtime gateway. The **independent 2nd instance** of the AI-BOM-generator standalone minted at v156 (Trusera/ai-bom) → **N=2, promotion-eligible**. See `01 Analysis/`. Related-topic (macOS-app-to-manage-AI-BOM) → `02 Wiki/(C) related-topic-macOS-app-to-manage-AI-BOM.md`.

**Repo:** https://github.com/msaad00/agent-bom · **Owner:** `msaad00` (no name/location/identity disclosed) · **License:** Apache-2.0
**Tagline:** *"Open security scanner and self-hosted control plane for AI/MCP infrastructure."*

## What it is
An **AI supply-chain security scanner** that *"builds an AI BOM across agents, MCP servers, tools, packages, credential environment names, cloud, runtime, and skills,"* then turns that inventory into **findings, compliance evidence, and graph-backed exposure paths.** Its organizing idea is **"blast radius"**: a vulnerable package isn't just a CVE row — it's linked to the MCP server that loads it, the tools that server exposes, the credential env-names in reach, and the agents that can call it. So it's the same AI-BOM core as v156 ai-bom, **plus an active control plane** (REST API + MCP tools + dashboard + optional runtime proxy/gateway with policy enforcement).

## What it inventories
Agents · **MCP servers** · tools · packages (dependency trees + attack paths) · credential **environment-names** (values redacted) · cloud resources · runtime · **skills**. Output: **JSON / SARIF / CycloneDX / SPDX / Markdown / HTML / compliance-evidence bundles.**

## Surfaces (6) — the instructive part
- **CLI / CI** — `pip install agent-bom` → `agent-bom agents -p . -f html -o report.html`; deterministic exit codes; GitHub Action.
- **REST API** — scans, findings, graph evidence, audit, runtime summaries.
- **MCP server** — **63 MCP tools + 6 resources + 6 workflow prompts** (read-mostly + 3 "Shield" write actions); run via `agent-bom mcp server`. *(Listed on the Glama MCP registry + an OpenClaw `agent-bom` skill.)*
- **Dashboard** — inventory, findings, graph cockpit, compliance evidence.
- **Runtime proxy / gateway** — live MCP traffic inspection, policy decisions, audit (optional, "scoped to where enforcement is worth the operational cost").
- **Python & TypeScript clients** — typed REST helpers.
- Deploy: Docker · Helm · EKS · Postgres · self-hosted `agent-bom serve` ("no managed cloud offering in this repository today").

## The direction (vs v156 ai-bom) — both ways
v156 ai-bom only **detects** MCP servers (inventory; the "inverse" direction). agent-bom does **both**:
- it **detects/inventories** agents + MCP servers (the AI-BOM), **and**
- it **exposes itself as an MCP server** (63 tools, so an agent can drive the scanner — the v149-Scrapling capability-FOR-agents direction) **and actively governs live MCP traffic** via the runtime gateway (policy enforcement, not just audit).

That makes agent-bom a *firmer* goal-aligned subject than v156 (it serves agents + operates on live agent traffic), though its center of gravity is still **security / supply-chain / compliance / governance** — hence (b) MODERATE, not STRONG.

## Where it sits in the corpus
- **Independent 2nd instance** of the v156-minted **"AI Supply-Chain Inventory / AI-BOM Generator"** standalone (Trusera/ai-bom + msaad00/agent-bom; no fork relationship) → **N=2, PROMOTION-ELIGIBLE at N=3.** Two sub-flavors recorded: **pure scanner/inventory** (v156, passive) vs **scanner + runtime control-plane / enforcement gateway** (v157, active). See `01 Analysis/(C) Pattern-Library-Phase-4b.md`.
- It is the **governance/supply-chain-inventory layer** of the operate-your-agent-stack family (provider-aggregation #18 #8 / capability v149 / orchestration v150 / account-mgmt v153 / observability v89+v109+v154 / ambient-status v154+v155 / **governance v156+v157**).

## Provenance (§37)
≈**21★** / 8 forks / **0 watchers** / 14 open issues / **2,351 commits** / **111 releases** (latest **v0.88.5**, Jun 1 2026) / Apache-2.0 / Python 87.2% (+ TypeScript 11.3%).
*Page-stated as of 2026-06 via WebFetch — **NOT independently API-verified (§37.4)**; this env mocks the GitHub API.* Creation date not stated → age/velocity unestablished → **NOT a Pattern #52 claim.** ⚠️ **Engagement-deficit-extreme**: a heavily-built solo project (2,351 commits / 111 releases / v0.88.x / Helm+EKS+Postgres + OpenSSF Scorecard) with **near-zero traction (21★ / 0 watchers)** — the build-effort-vs-attention mismatch is the most notable provenance signal (cf. the high-commits-low-stars shape of v151/v152).

## Why it's goal-aligned (MODERATE, firm — and where the line is)
- **On goal #1 (firmer than v156):** it inventories the agent/MCP stack, **serves 63 MCP tools to agents**, and **enforces policy on live MCP traffic** — operating-and-governing the agent stack, not just auditing it.
- **Held MODERATE, not STRONG:** its center of gravity is **security / supply-chain / compliance**; the MCP tools are read-mostly (it exposes its *audit* data to agents, not a build capability), and the runtime gateway is an optional secondary feature. For THIS vault's Claude-Code-mastery goal it's adjacent-domain → architecture-study/awareness. Flagged for the next audit to challenge (could go WEAK/off-goal).
- **No §35 incentive to inflate:** the ceiling was already clear (4 consecutive goal-aligned ships before this), so the verdict is on merits — same MODERATE-borderline line as v156, a touch firmer.

## §35 / streak
**§35 STAYS CLEAR** — window {v155 GA, v156 GA, v157 GA} = 0 OG (5 consecutive goal-aligned ships). NOT an override → override-frequency UNCHANGED (7-in-20 trailing; lifetime 10). Streak GA:19·OG:11 → **GA:20·OG:11 [7 ov]** (20th goal-aligned PASS). ⚠️ **2nd consecutive AI-BOM ship** (v156 + v157) — the corpus is now thickening the AI-BOM niche, still with ZERO piloted.

## Pilot
**READ-leaning pilot candidate** (like v156, slightly higher-friction). `pip install agent-bom && agent-bom agents -p . -f html -o report.html` on a repo is reversible and shows the blast-radius inventory of your own AI stack; the MCP-server mode (`agent-bom mcp server`) is the genuinely interesting bit — it plugs into Claude Code so an agent can query your AI-BOM. `install-snapshot` first. ⚠️ Two AI-BOM scanners now catalogued (v156 + v157), zero piloted — pick **one** and run a scan rather than catalogue a third.
