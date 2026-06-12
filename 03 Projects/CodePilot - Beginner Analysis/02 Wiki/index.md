# CodePilot (op7418 / 歸藏 Guizang) — Wiki

> **"A multi-model AI agent desktop client — connect any AI provider, extend with MCP & skills, control from your phone."**
> *(Guizang's own framing: "高颜值 Claude Code 桌面端产品" / 可视化编程助手 — a good-looking native desktop GUI for Claude Code.)*

**Repo:** [op7418/CodePilot](https://github.com/op7418/CodePilot) · **Docs:** [codepilot.sh](https://codepilot.sh) · **Owner:** op7418 = 歸藏 / Guizang ([guizang.ai](https://guizang.ai), [@op7418](https://x.com/op7418))
**Wiki version:** v161 (2026-06-05) · **Verdict:** GOAL-ALIGNED INCLUDE 4/4 · **Tier:** T2 Service (desktop GUI client) + bundled aggregator/bridge

---

## What it is

CodePilot is a **cross-platform Electron + Next.js desktop GUI for Claude Code** — instead of driving Claude Code from the terminal, you chat, code, browse files, run git, and manage agent sessions in a graphical app. It doubles as a **17+-provider aggregator** (switch model/provider mid-conversation) and ships a **remote bridge** so you can drive it from your phone via common messaging apps. Guizang famously built it in ~a day, AI-assisted (Opus 4.6 + Agent Teams + Claude Code).

It is the **operating surface** for Claude Code — distinct from the v153–v160 niche of menu-bar/notch tools that *watch or switch* your agents from the outside.

## Core capabilities

| Area | What it does |
|---|---|
| **Multi-provider** | 17+ providers — Anthropic, OpenRouter, Bedrock, Vertex/Gemini, Zhipu GLM, Kimi/Moonshot, MiniMax, Volcengine Ark (Doubao), Xiaomi MiMo, Aliyun Bailian (Qwen), Ollama, LiteLLM, custom Anthropic/OpenAI-compatible. Switch model mid-conversation. |
| **Claude Code integration** | Drives the Claude Code CLI for file editing, terminal commands, git — visually. Built on the Claude Agent SDK. |
| **Sessions** | Pause, resume, **rewind to checkpoints**; **split-screen dual concurrent sessions**. |
| **Assistant workspace** | Persona/memory files (`soul.md`, `user.md`, `claude.md`, `memory.md`), onboarding flows, daily check-ins, persistent preferences. |
| **MCP** | stdio / sse / http servers with runtime monitoring. |
| **Skills** | Custom / project / global skills + the **skills.sh** marketplace. |
| **Remote bridge** | Telegram, Feishu, Discord, QQ, WeChat — control sessions from your phone. |
| **Extras** | Generative-UI dashboards, media studio (image gen + batch + gallery), cron task scheduler, token/cost analytics, file browser + git panel + syntax highlighting. |
| **Storage** | Local SQLite (WAL mode); data stays on-machine. |

## Stack

Next.js 16 · Electron 40 · Radix UI + shadcn/ui · Tailwind CSS 4 · Motion (Framer Motion) · Claude Agent SDK · Vercel AI SDK · TypeScript 97.5% · cross-platform (macOS / Windows / Linux).

## Provenance (§37 — page-stated, NOT API-verified)

≈**5.9k★** · 641 forks · 369 open issues · 74 PRs · **1,160 commits** · latest **v0.55.1** (Jun 4 2026) · created ~Feb 11 2026 · **BSL-1.1** (free for personal/academic/non-profit; commercial use needs a separate license; auto-converts to **Apache 2.0 on 2029-03-16**).

> ⚠️ This environment **mocks the GitHub API** (§37.4) — all metadata above is page-stated via WebFetch + WebSearch, not independently API-verified. ~115 days × ~51★/day ≈ SUSTAINED-MODERATE-HIGH *if accurate*, but velocity is unverified → **NOT a Pattern #52 claim.**

## Where it sits in the corpus

- **Owner is a recurring cultural-peer:** op7418 = 歸藏/Guizang — also v105 (guizang-social-card-skill) and bundled in v83 (open-design's `skills/guizang-ppt/`). 3rd corpus appearance; China-Mainland cluster.
- **Pattern #18 #8 Multi-Source LLM Aggregator** (CONFIRMED N=3): N+1 instance (17 providers in a GUI client).
- **T4c Operator-Notification/Control-Bridge via Messaging Platform** (v88 teleport): N+1 — here it's *remote control*, a step beyond notification.
- **agentskills.io / skills.sh**: 57k-chain-adjacent (skills + marketplace).
- **Agent-memory adjacency** (v66 agentmemory / v132 supermemory): persona files — but declined as a Karpathy-LLM-wiki corpus-recursive instance (per-assistant memory, not a self-maintaining knowledge wiki).
- **Nearest neighbors:** v150 Paseo (orchestration platform), v118 OpenHuman (agentic desktop assistant), v99 cmux (terminal multiplexer) — CodePilot is distinct: a **GUI client / visual front-end** for Claude Code.

## Pattern Library outcome (Phase 4b)

- **PRIMARY:** 1 NEW §C standalone — **"Desktop GUI Client / Visual Front-End for a CLI Coding Agent"** (PROVISIONAL N=1, CORPUS-FIRST). Distinct from cmux (terminal multiplexer), LV-C7 #22 (config-switcher management-GUIs), Paseo (orchestration platform), OpenHuman (general assistant).
- **SECONDARY (not minted):** #18 #8 aggregator N+1 · T4c bridge N+1 · skills.sh/57k-adjacent · agent-memory adjacency · LV-C3 self-referential-build (SOFT) · Pattern #45 BSL-1.1-with-change-date sub-variant · op7418/Guizang corpus-recursive · Pattern #19 Chinese-AI-KOL + WeChat-funnel · Electron (vs Swift-native cluster).
- **Counts:** 46 patterns / 10 Library-vocab CONFIRMED (both UNCHANGED) / +1 §C standalone. **§35 CLEAR** (9 consecutive goal-aligned, v153→v161). Streak **GA:24·OG:11 [7 ov]**.

## Pilot note

Strong pilot candidate, and a genuine **domain-shift** from the monitor niche — it's the surface you'd actually operate Claude Code in. BSL-1.1 free for personal use; cross-platform; reversible. ⚠️ Broad surface (sessions + 5-platform bridge + scheduler + 17 providers) → `install-snapshot` first; review the bridge config before linking any messaging account. ⚠️ It's the **9th consecutive "manage/monitor AI coding tools" subject with zero piloted** — varying the archetype is good, but *piloting one* (CodePilot is a fine candidate) remains the unaddressed move.

---

*Sources:* [op7418/CodePilot](https://github.com/op7418/CodePilot) · [Releases](https://github.com/op7418/CodePilot/releases) · [Guizang's X launch thread](https://x.com/op7418/status/2020023161702805576) · [bonza.cn writeup — "Claude Code 的原生桌面 GUI"](https://blog.bonza.cn/2026/02/11/codepilot-claude-desktop-gui/) · [codepilot.sh](https://codepilot.sh)
*Provenance NOT API-verified (§37.4 — env mocks the GitHub API). Authored by Claude (C).*
