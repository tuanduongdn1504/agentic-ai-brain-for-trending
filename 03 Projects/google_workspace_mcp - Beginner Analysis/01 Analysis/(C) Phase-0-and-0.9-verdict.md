# (C) google_workspace_mcp — Phase 0 + Phase 0.9 STRICT verdict (v140)

**Subject:** `taylorwilsdon/google_workspace_mcp` — https://github.com/taylorwilsdon/google_workspace_mcp
**Date:** 2026-06-03 · **Routine:** v2.6 (§31 2-tier INCLUDE + §35 ceiling + §37 fact-provenance)
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG

---

## Phase 0 — scope gate

In scope. The subject is an **MCP (Model Context Protocol) server** — the connectivity layer between Claude / autonomous agents and external tools — which is squarely inside corpus goal #1 ("master Claude and autonomous agents for software development"). MCP is the corpus's core agent-tooling axis (Pattern #18 sub-mechanism B1; prior MCP subjects: v66 agentmemory, v70 codegraph, v119 nature-skills' bundled MCP, v132 supermemory, v134 obsidian-second-brain). No safety concern: it is a read/write integration server for the user's *own* Google Workspace via OAuth — not abuse tooling.

## Phase 0.9 STRICT — the four axes

### (a) Cultural-peer / geographic — **FAIL**
- Owner `taylorwilsdon` — name reads as **Taylor Wilsdon, Western/English-speaking, US-presumed** (confidence: speculation/medium — username is stated; no bio/location disclosed in-repo; `workspacemcp.com` project site lists no author identity).
- Not a registered cultural-peer (not Asian-cluster, not South-American (a)-8, not VN/China-Mainland).
- **Not (a)-7 Foundational-Vendor-Direct-Source** — taylorwilsdon is an *individual third party*; the repo integrates Google Workspace and builds on jlowin's FastMCP, but the author is neither Google nor Anthropic nor a vault-substrate vendor. NO new (a) sub-axis minted (a single US-individual subject does not warrant one — the v97→v115 (a)-8-retirement anti-pattern).

### (b) Goal-relevance — **STRONG** (load-bearing; this is what makes it GOAL-ALIGNED)
- An MCP server exposing **12 Google Workspace services** (Gmail · Drive · Calendar · Docs · Sheets · Slides · Forms · Chat · Apps Script · Tasks · Contacts · Custom Search) as **50+ tools** to **any MCP client** (Claude Desktop, Claude Code, VS Code MCP, LM Studio). This is exactly the tool-connectivity an autonomous agent needs to do real software/knowledge work, and it ships a **bundled Claude skill** (`skills/managing-google-workspace/`) to improve the agent's tool-routing.
- **STRONG, not STRONGEST:** it is a *vendor-integration connector* for one SaaS suite, not a core agent-orchestration framework or methodology (the STRONGEST bar — cf. v126 compound-engineering's SWE-process loop, v131 harness's team-factory). It's first-class infrastructure for agents, not the agent-building substrate itself. Cost-of-trial is LOW–MINIMUM (`uvx workspace-mcp`, reversible) × DIRECT goal-relevance → STRONG per §10.

### (c) Instructive engineering — **STRONG**
A production-grade reference implementation of a large-surface MCP server:
- **3-tier tool exposure** (`--tool-tier core|extended|complete`) — graduated, least-privilege tool registration (see Phase 4b).
- **OAuth 2.0 / 2.1** — confidential + public PKCE clients, **multi-user bearer tokens** (`MCP_ENABLE_OAUTH21`), service-account domain-wide delegation, and a **stateless container mode** (`WORKSPACE_MCP_STATELESS_MODE` — no on-disk credential writes; tokens in-memory only).
- **3 transports** — stdio (legacy local) / streamable-HTTP (recommended, multi-user) / reverse-proxy behind nginx/Cloudflare.
- Read-only mode with scope filtering; per-service granular permissions; Fernet credential encryption; optional GCS/Valkey-Redis backends. Built on **jlowin/FastMCP 2.13.0+** (NOT an Anthropic product — the popular OSS MCP framework, `gofastmcp.com`), using FastMCP's native `GoogleProvider` for DCR + CORS.

### (d) Corpus connectivity — **STRONG**
- **Pattern #18 sub-mechanism B1 "MCP / one-binary-many-CLIENTS"** — a clean, strong instance (one server, 4+ MCP clients). N+1 strengthening of the B1 line (v70 codegraph B1 anchor + v66/v119/v132/v134 MCP threads).
- **Pattern #84 multi-harness / cross-client tolerance** — Claude Desktop + Claude Code + VS Code + LM Studio + any MCP-1.0 client. N+1 (modest — MCP-client-side, via one protocol, not N native formats).
- **Bundled Claude skill** (`skills/managing-google-workspace/` → `~/.claude/skills/`) — an agentskills.io-*adjacent* artifact (a Claude Skills directory, not a formal SKILL.md-spec / `npx skills add` 57k implementer). Connects to the skill-routing cluster (the skill exists to help the agent *use* the MCP server better — a skill-augments-server pairing).
- **FastMCP** ties to the broader MCP-framework ecosystem; **Pattern #66** supply-chain surface (OAuth, Fernet, credential backends) — thin/clean.

---

## §35 — Soft Off-Goal-Rate Ceiling
**STAYS CLEAR.** Rolling-3-ship window after v140 = **{v138 GA, v139 OG, v140 GA} = 1 OG ≤ 1 → CLEAR.** v140 is a GOAL-ALIGNED INCLUDE, so the §35 risk flagged at v139 ("a 2nd consecutive off-goal at v140 RE-BREACHES") is **avoided**, not overridden. NOT a ceiling-override. Override-frequency triggers UNCHANGED (v140 is not an operator override; lifetime overrides remain 5 = v84+v116+v122+v127+v139).

## §37 — Fact-provenance (volatile metrics)
≈**2.6k★** / 784 forks / 16 watchers / 52 open issues / 49 open PRs / MIT / Python 3.10+ / FastMCP 2.13.0+ / website workspacemcp.com (as of 2026-06, repo page — **stated, NOT API-verified §37.4**; this environment mocks the GitHub API). Velocity/age not established → **NOT a Pattern #52 claim**. Author location US-presumed (**speculation/medium** — name-only, undeclared).

## Streak (v2.6 §32)
GA:8 · OG:5 [2 ov] → **GA:9 · OG:5 [2 ov]** (v140 = 9th goal-aligned PASS; the v139-broken consecutive-GA run restarts at 1; "49+3\*" frozen @v125).

## Honest non-claims
- (a) genuinely FAILS (US-individual, not a cultural-peer, not (a)-7) — not laundered.
- (b) is STRONG-not-STRONGEST (vendor-integration connector, not agent-building substrate).
- NOT a #52 promotion (metrics unverified, no velocity window).
- NOT an agentskills.io 57k `npx skills add` implementer (bundled Claude skill = a directory artifact, not the vercel-labs CLI standard).
- FastMCP is jlowin/OSS, **not** an Anthropic product (corrects a common misread).
- Phase 4b mints **1** Library-vocab standalone (§28 1 ≤ 2); NO new top-level Pattern, NO new tier sub-archetype, NO Pattern-Library confirmed-count change.
