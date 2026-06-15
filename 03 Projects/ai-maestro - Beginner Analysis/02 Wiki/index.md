# (C) AI Maestro (v163 wiki)

> **Status: GOAL-ALIGNED INCLUDE 3/4** ((a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG). A **multi-vendor orchestration platform for AI coding agents** — manage Claude Code / Codex / Aider / Cursor (or any terminal agent) from one dashboard, give them **persistent memory + code-graph queries + agent-to-agent messaging**, and move agents across machines. It is the corpus's genuine **2nd "Multi-Vendor Coding-Agent Orchestration Platform"** (after v150 Paseo), completing the *platform* bucket of the v162 orchestration-theme decomposition. See `01 Analysis/`.

**Repo:** https://github.com/23blocks-OS/ai-maestro · **Owner:** `23blocks-OS` org · **Author:** Juan Pelaez (`@jkpelaez` / `jpelaez-23blocks`), CTO & Founder of 3Metas + 23blocks (Boulder USA / Roma Italy) · **License:** MIT
**Tagline:** *"The OS for AI-first organizations — orchestrate any AI agent with persistent memory, agent-to-agent messaging, and multi-machine support."*
**README origin:** *"I was running 35 AI agents across multiple terminals and became the human mailman between them. So I built AI Maestro."*
**Site:** https://ai-maestro.23blocks.com/ · **Ecosystem:** `23blocks-OS/ai-maestro-plugins` (Plugin Builder) · `23blocks-OS/lolabot` (Chief-of-Staff agent template)

## What it is
A **self-hosted control plane** for running many AI coding agents at once. You point it at any terminal-based agent — **Claude Code, Codex, Aider, Cursor, OpenClaw, Hermes, Droid, or a custom script** ("we don't lock you in") — and AI Maestro gives you a **unified dashboard** (Next.js + xterm.js), **persistent memory + a code graph** so agents stop having amnesia, **agent-to-agent messaging** so they stop needing you as the relay, and a **multi-machine peer mesh** so agents on different computers/locations all appear in one place. It is **not a SaaS** — you deploy it yourself (laptop / team server / your cloud); your infrastructure, agents, and data are yours.

This is the **platform** layer, not a session multiplexer: where v99 cmux / v162 AoE *host* human-driven sessions, AI Maestro adds **agents that message each other** (AMP), **shared memory**, and a **machine mesh** on top.

## The three open protocols (the architectural core)
- **AMP — Agent Messaging Protocol.** Email-like, **agent-to-agent** communication with cryptographic signatures and push notifications **across machines**. (This is the product's reason to exist — it replaces the human "mailman.")
- **AID — Agent Identity.** A portable **cryptographic identity** for each agent across platforms.
- **AAP — Agent Actions Protocol.** Standardizes how agents execute tools, call APIs, and trigger workflows.

## How it integrates (the instructive parts)
- **Claude Code plugin** — installs a plugin with **5 skills + 32 CLI scripts** (the Claude integration is *product*, not internal dev-exhaust; Medium: "My AI Agents have their own inbox … A Claude Code Skill Story"). A **Plugin Builder** (`ai-maestro-plugins`) extends skills + canvas artifacts.
- **Three-layer persistent intelligence** — agent conversations/decisions + auto-generated documentation (**CozoDB** semantic memory) + an interactive **code graph** (**ts-morph** + **delta indexing**). Cures "agent amnesia."
- **Multi-machine peer mesh** — "every machine is equal," machines auto-discover and join, **no central server**; all agents visible from one dashboard regardless of location.
- **Four deployment modes** — local **tmux** sessions · **Docker** (resource-limited containers) · **AWS EC2** (dedicated ARM64 + Nginx + SSL) · **AWS ECS Fargate** (serverless), provisioned via **Terraform** (HCL).
- **Work coordination + gateways** — Kanban boards, team meetings, task tracking; connectivity gateways for **Slack / Discord / Email / WhatsApp**.
- **Agent identity UX** — custom avatars + personality profiles; smart auto-coloring 3-level naming tree.
- **Security-forward** — cryptographic signatures on agent messages + a content-security gateway that screens **34 prompt-injection patterns** before agents process input.
- **LolaBot** — an open-source "batteries-included Chief of Staff" agent template (email triage, semantic memory, task management, content security).

## Where it sits in the corpus
- **The genuine 2nd "Multi-Vendor Coding-Agent Orchestration Platform"** → that standalone (minted at v150 Paseo) reaches **N=2** (v150 + v163), **PROMOTION-ELIGIBLE at N=3.** This **completes the 2nd bucket** of the v162 orchestration-theme decomposition: a session-multiplexer species (cmux + AoE, N=2) **and** an orchestration-platform class (Paseo + ai-maestro, N=2) — both N=2, both DEFERRED to the overdue audit. **0 new standalones.**
- **vs v150 Paseo (same class, different sub-flavor):** Paseo orchestrates via an **agent-of-agents `/paseo-*` skill suite**, cross-DEVICE (phone/desktop/web/CLI). ai-maestro orchestrates via **AMP agent-to-agent messaging + a peer mesh**, multi-MACHINE, with memory + code-graph baked in. Same class; the **confirm-or-keep-two-sub-flavors + rename DEFERRED to the audit** (the v162 / v158 "don't generalize-to-fit" discipline).
- **vs the cmux / AoE session-multiplexer species:** those *host* human-driven sessions; ai-maestro adds autonomous **agent-to-agent messaging**, shared **memory**, and a **machine mesh** — a platform, not a multiplexer.
- **Corpus-recursive capability absorption (observation):** its CozoDB **persistent memory** echoes **v66 agentmemory** (Pattern #85) + v132 supermemory; its ts-morph **code graph** echoes **v70 codegraph** — the platform *absorbs* what the corpus catalogued separately. **NOT minted, NOT double-counted** (components, not the product).
- **AMP / AID / AAP** — home-grown protocols made architecturally first-class. Like v162's ACP: a **Pattern #18 sub-mechanism-B protocol-variant candidate** if a 2nd subject adopts them; **NOT a §C standalone** here. Observation.
- **Pattern #84 cross-tool** (7+ agents, agent-agnostic); **OpenClaw / Hermes corpus-recursive**; **T4c** notification-bridge N+1 (Slack/Discord/Email/WhatsApp); **Pattern #66 supply-chain** (curl|bash + crypto-identity + injection-screening); **Pattern #57 agentskills.io-adjacent** (the 5-skill Claude Code plugin, modest, not a 57k implementer).
- **NOT** Pattern #18 #8 (orchestrates **agents**, not LLM **providers**). **NOT** the v158 observability sub-archetype (orchestrates/messages/runs; status is a sub-feature). **NOT** LV-C7 #22 (Next.js web platform, not a Tauri management-GUI).

## Provenance (§37)
≈**713★** / 94 forks / 13 watchers / **12 open issues** / **995 commits** / latest **v0.35.54** (Jun 5 2026) / MIT ("free for any purpose, including commercial") / **TypeScript 87.8%** (+ Shell 6.6% / JS 4.4% / HCL 0.5% / CSS / Dockerfile / Smarty).
*Page-stated as of 2026-06 via WebFetch (repo + raw README) + WebSearch corroboration (GitHub profile, two Juan Pelaez Medium posts, docs QUICKSTART, ai-maestro.23blocks.com) — **NOT independently API-verified (§37.4)**; env mocks the GitHub API.* **No reliable creation date surfaced → NOT a Pattern #52 / velocity claim.** Author **Juan Pelaez** (`@jkpelaez`/`jpelaez-23blocks`), CTO & Founder 3Metas + 23blocks (Boulder/Roma) → **(a) FAIL, no axis minted** (US/Italy founder, not a cultural-peer, not (a)-7; notable-founder ≠ (a) PASS, the v139 discipline).

## Why it's goal-aligned (and a genuine — but fenced — pilot)
- **On goal #1, and close to THIS vault's workflow:** the origin story ("running 35 agents, became the human mailman") *is* Storm Bear's pain — running many parallel Claude Code agents to build these wikis. The agent-to-agent messaging + shared memory directly target the relay/amnesia tax.
- **Pilot candidate, but heavier-fenced than AoE:** MIT + self-hosted + reversible. ⚠️ **Pilot fence:** `curl -fsSL … | sh` install + a **multi-machine peer mesh** + **gateway integrations** (Slack/WhatsApp) + cryptographic identity = a *bigger surface* than v162 AoE. `install-snapshot` first; trial single-machine (tmux/Docker mode) before any mesh/cloud/gateway wiring.
- ⚠️ **11th consecutive "tool for operating AI coding agents" subject (v153→v163), ZERO piloted** — and now the corpus has **two N=2 orchestration buckets** sitting un-confirmed. The lever is unchanged and louder: **run the overdue audit** (it now owes two N=2 promote/rename calls) **or pilot one** (AoE is the lightest; ai-maestro is the most ambitious). A v164 in this space is the lowest-value next move.

## §35 note
A goal-aligned v163 keeps the ceiling clear: window {v161 GA, v162 GA, v163 GA} = 0 OG (**11 consecutive goal-aligned ships v153→v163**). Streak GA:25·OG:11 → **GA:26·OG:11 [7 ov]** (26th goal-aligned PASS; not an override).
