# ai-maestro — Beginner Analysis (project CLAUDE.md)

**Subject:** `23blocks-OS/ai-maestro` — "AI Maestro" (**v163** wiki ship, 2026-06-15).
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.
**Routine:** v2.6 (§31/§35/§37). **Ships into the v158-audit-CONFIRMED Pattern Library.**

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis verdict + §35 + §37 + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY (Paseo orchestration-PLATFORM standalone → N=2; completes the 2nd bucket of the v162 decomposition; defer confirm/rename to audit) + observations.
- `02 Wiki/index.md` — the knowledge page.

## One-paragraph summary
**"The OS for AI-first organizations — orchestrate any AI agent with persistent memory, agent-to-agent messaging, and multi-machine support."** A self-hosted **multi-vendor orchestration platform** by **Juan Pelaez** (CTO & Founder, 3Metas + 23blocks) that manages **Claude Code / Codex / Aider / Cursor / OpenClaw / Hermes / Droid** (or any terminal agent) from one **Next.js + xterm.js dashboard**; gives agents **persistent memory** (CozoDB) + a **code graph** (ts-morph + delta indexing) + **agent-to-agent messaging** (the AMP protocol — its reason to exist: "I became the human mailman between them"); runs them across a **multi-machine peer mesh** (no central server) in **four deploy modes** (tmux / Docker / EC2 / Fargate, Terraform-provisioned); ships a **Claude Code plugin (5 skills + 32 CLI scripts)**, three open protocols (**AMP** messaging / **AID** identity / **AAP** actions), gateway integrations (Slack/Discord/Email/WhatsApp), and the LolaBot Chief-of-Staff agent template. TypeScript 87.8%; MIT; ≈713★ / 995 commits / v0.35.54.

## Verdict rationale
- **(b) STRONG** = orchestrates multiple coding agents = dead-center goal #1, and close to this vault's own workflow; **STRONG-not-STRONGEST** = a third-party control-plane *around* the agents (the Paseo/cmux/AoE/ai-switcher calibration; STRONGEST reserved for the substrate / a methodology).
- **(a) FAIL** = Juan Pelaez (US/Italy founder); not a cultural-peer, not (a)-7 (23blocks is not a vault-substrate dependency); notable-founder ≠ PASS (v139); no axis minted.
- (c) STRONG (mature TS+infra: 995c/v0.35.54; CozoDB + ts-morph + 4 deploy modes + Terraform + Vitest; AMP/AID/AAP protocols; multi-machine mesh; crypto-signatures + 34-injection-pattern gateway). (d) STRONG (orchestration-platform standalone N=2 with Paseo; completes the v162 decomposition's 2nd bucket; #84 7-agent cross-tool; OpenClaw/Hermes corpus-recursive; memory↔v66/v132 + code-graph↔v70 absorption observations; T4c gateways; #66 supply-chain; #57 5-skill Claude Code plugin).

## §35 / streak
**§35 STAYS CLEAR** — window {v161 GA, v162 GA, v163 GA} = 0 OG (**11 consecutive goal-aligned ships v153→v163**). NOT an override → override-frequency UNCHANGED (lifetime 10). Streak GA:25·OG:11 [7 ov] → **GA:26·OG:11 [7 ov]** (26th GOAL-ALIGNED PASS).

## Pattern Library
**PRIMARY (tier layer, 02b / registry 06 §F): the v150 Paseo "Multi-Vendor Coding-Agent Orchestration Platform" §C standalone → N=2** (v150 Paseo agent-of-agents-skill-suite + v163 ai-maestro agent-to-agent-messaging-mesh). **Completes the 2nd bucket** of the v162 orchestration-theme decomposition (session-multiplexer species cmux+AoE N=2 / orchestration-platform Paseo+ai-maestro N=2 / harness team-generator N=1 adjacent). **PROMOTION-ELIGIBLE at N=3; confirm-or-keep-two-sub-flavors + rename DEFERRED to the overdue audit** (the v162/v158 "don't generalize-to-fit" discipline). **0 new §C standalones.** Two sub-flavors recorded: (a) agent-of-agents-via-skill-suite (Paseo, cross-device) / (b) agent-to-agent-messaging-mesh (ai-maestro, multi-machine). **NO confirmed-count change: 46 patterns / 10 Library-vocab CONFIRMED.** Observations (NOT minted): AMP agent-to-agent peer messaging = candidate sub-flavor + possible future standalone (DEFER; v162-ACP discipline) · AMP/AID/AAP home-grown protocol suite = Pattern #18 sub-mechanism-B protocol-variant candidate if a 2nd subject adopts · memory(CozoDB)↔v66 agentmemory/#85/v132 + code-graph(ts-morph)↔v70 codegraph = corpus-recursive capability-absorption, NOT double-counted · T4c gateways N+1 (Slack/Discord/Email/WhatsApp) · #84 7-agent cross-tool · #57 5-skill Claude Code plugin (PRODUCT, modest, NOT a 57k implementer) · #66 supply-chain (curl|bash + crypto-identity + 34-injection-screen) · multi-machine peer mesh · LolaBot framework (cited-to-subject-elevation watch) · NOT #18 #8 / NOT observability sub-archetype / NOT LV-C7 #22 / NOT the cmux/AoE session-multiplexer species.

## Provenance (§37)
≈**713★** / 94 forks / 13 watchers / **12 open issues** / **995 commits** / **v0.35.54** (Jun 5 2026) / MIT / TypeScript 87.8% (+ Shell/JS/HCL/CSS/Dockerfile) — page-stated via WebFetch (repo + raw README) + WebSearch corroboration, **NOT API-verified §37.4** (env mocks the GitHub API). No reliable creation date → **NOT a #52 claim.** Author Juan Pelaez (`@jkpelaez`/`jpelaez-23blocks`), CTO & Founder 3Metas + 23blocks (Boulder/Roma).

## Pilot
**Genuine but heavier-fenced pilot than AoE.** On-goal and close to the vault workflow (the "human mailman" origin = running many parallel Claude Code agents). MIT + self-hosted + reversible. ⚠️ **Pilot fence:** `curl|bash` install + multi-machine peer mesh + gateway integrations (Slack/WhatsApp) + crypto identity = a bigger surface than AoE → `install-snapshot` first; trial single-machine (tmux/Docker) before any mesh/cloud/gateway wiring. ⚠️ **11th consecutive "tool for operating AI coding agents" subject (v153→v163), ZERO piloted** — and the corpus now has TWO N=2 orchestration buckets un-confirmed. The lever: **run the overdue audit** (it owes two N=2 promote/rename calls) **or pilot one** (AoE lightest, ai-maestro most ambitious) — not a v164 in this space.

Shipped on branch `wiki/v163-ai-maestro` off main (at `1b8be88`, post-v162). Not auto-merged — operator reviews + merges.
