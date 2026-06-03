# (C) larksuite/cli — Phase 0 + Phase 0.9 STRICT verdict (v143)

**Subject:** `larksuite/cli` — https://github.com/larksuite/cli
**Date:** 2026-06-03 · **Routine:** v2.6 (§31 + §35 + §37)
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG

---

## Phase 0 — scope gate
In scope. The official Lark/Feishu CLI, **"built for humans and AI Agents"** — a tool explicitly co-designed for AI-agent consumption (200+ commands + 26 AI Agent Skills + identity-switching + agent-auth flow). Goal #1 ("master Claude and autonomous agents for software development") — this is agent-tooling: how an autonomous agent drives a real productivity platform. Sibling shape to v140 google_workspace_mcp (same goal — give an agent control of a vendor suite — different delivery: agent-native CLI vs MCP server).

## Phase 0.9 STRICT — four axes

### (a) Cultural-peer / geographic — **FAIL**
- Owner = **`larksuite`, official ByteDance org** (Lark/Feishu). Not a cultural-peer (corporate official org, like the v124 K-Dense / v140 taylorwilsdon FAILs), and **not (a)-7** (Lark is not a vault-substrate vendor the way Anthropic is). ByteDance/China-origin is corporate, not an individual cultural-peer → no (a)-rescue, no axis minted.

### (b) Goal-relevance — **STRONG** (load-bearing)
- A CLI **architected for AI agents**: 26 bundled **AI Agent Skills** (`/skills`), an agent-friendly **shortcut tier** (`+` prefix, smart defaults, table output, **dry-run previews**), **identity-switching** (`--as user|bot`), a **non-blocking device-code auth handoff** for headless agents (`--no-wait` → returns the auth URL for the agent to hand to its user; resume via `--device-code`), and a `lark-skill-maker` for authoring more skills. "Every command is tested with real Agents."
- **STRONG, not STRONGEST:** it's a *vendor-integration connector* for one suite (Lark/Feishu), not a general agent-building substrate/methodology (the STRONGEST bar — v126/v131). Same calibration as v140 google_workspace_mcp. Highly goal-relevant as agent infrastructure; not the agent-orchestration core itself.

### (c) Instructive engineering — **STRONG**
A production official CLI with a clean **three-layer command architecture**: **shortcuts** (`+`, human+AI-friendly, dry-run) / **curated API** (100+, auto-generated from Lark OAPI metadata, evaluation + quality gates, 1:1) / **raw API** (`api`, 2,500+ endpoints). Plus the agent-auth affordances above. Go 97.3%, MIT, official org. Install via `npx @larksuite/cli@latest install` (npm) or Go 1.23+/Python3 from source; skills via `npx skills add larksuite/cli`.

### (d) Corpus connectivity — **STRONG**
- **Productivity-suite agent-connectivity cluster with v140 google_workspace_mcp** — two delivery patterns for the same goal (MCP server vs agent-native CLI+skills). Fresh, useful comparison.
- **Pattern #57 / agentskills.io chain — implementer-CANDIDATE (honest, not confirmed):** the skills are **Lark-native** in content but **distributed via `npx skills add larksuite/cli`** — the vercel-labs skills CLI that anchors the 57k chain. So it rides the 57k *distribution* mechanism even though the skill content is vendor-specific. Flagged as a candidate, not asserted as a confirmed 57k implementer.
- **Pattern #84** agent-tooling / multi-consumer (CLI for humans + agents). Agent-auth primitives (identity-switching, device-code handoff) connect to the credential/auth threads (v67 OAuth-bridge lineage, loosely).

---

## §35 — Soft Off-Goal-Rate Ceiling
**STAYS CLEAR.** Rolling-3-ship window after v143 = **{v141 GA, v142 OG, v143 GA} = 1 OG ≤ 1 → CLEAR.** v143 is GOAL-ALIGNED — this is exactly the goal-aligned ship §35 required after the v142 off-goal override, **avoiding the re-breach** the v142 entry flagged. NOT a ceiling-override. Override-frequency triggers UNCHANGED (v143 is not an override; lifetime 6).

## §37 — Fact-provenance
≈**13.3k★** / 909 forks / MIT / Go 97.3% (as of 2026-06, repo page — **stated, NOT API-verified §37.4**; env mocks the GitHub API). Owner = `larksuite` official ByteDance org (**stated**). Velocity/age not established → **NOT a Pattern #52 claim**.

## Streak (v2.6 §32)
GA:10 · OG:6 [3 ov] → **GA:11 · OG:6 [3 ov]** (v143 = 11th goal-aligned PASS; "49+3\*" frozen @v125).

## Honest non-claims
- (a) genuinely FAILS (corporate official org, not a cultural-peer, not (a)-7).
- (b) STRONG-not-STRONGEST (vendor-integration connector, not the agent substrate — v140 calibration).
- Pattern #57 is an implementer-**candidate** only (Lark-native skills riding the `npx skills add` distribution; NOT asserted as a confirmed 57k SKILL.md-spec implementer).
- NOT a #52 promotion (13.3k★ unverified, no velocity window).
- Phase 4b mints **1** Library-vocab standalone (§28 1 ≤ 2); NO new top-level Pattern, NO new tier sub-archetype, NO Pattern-Library confirmed-count change.
