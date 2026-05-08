# Telegram Remote-Control Stack — topic index

> Unified synthesis of 4 autopilot drains (2026-05-07) covering the 4-layer stack to **control Claude Code/Desktop from a phone via Telegram**: interface (Telegram/Discord/Native Remote Control) → engine (headless Claude Code SDK + Ralph loop) → integration (MCP servers / Channels) → network (tunneling: tailscale, Cloudflare Tunnel, Twingate, VPS).
>
> Compiled from 23 distinct YouTube creator bundles + Claude Code's creator interview. Heavy bias toward **operationally-deployable solo/team setups**; production-scale gaps called out separately in [[gaps-production]].
>
> **🔧 Pilot-verified 2026-05-08:** Recipe A end-to-end deployment caught 5 deviations from the bundle's published commands. The corrected ritual is in [[setup-recipe-a]] — read this BEFORE following any of the layer-1 setup blocks. Older tutorial commands fail silently on current Claude Code 2.1.x + plugin v0.0.6.

## Articles

| File | What it covers |
|---|---|
| [[overview]] | Operator goal, 4-layer stack diagram, decision matrix (pick-your-own-path by team size / privacy / availability) |
| **[[setup-recipe-a]]** ⭐ | **Verified pilot ritual (2026-05-08)** — the 7-step recipe that actually works, with the 5 deviations from internet tutorials called out explicitly. Read this before anything else if you want to deploy today. |
| [[layer-1-interface-telegram]] | Telegram BotFather + Claude Code Channels + Discord alternative + native Remote Control + access policy. Setup commands updated to match pilot. |
| [[layer-2-engine-headless-claude-code]] | Claude Code SDK headless mode + Ralph loop with Stop Hooks + warm vs cold sessions + agents.md persistent memory |
| [[layer-3-mcp-integration]] | MCP "USB-C for AI" architecture + official plugins vs custom Python `fastmcp` + token-cost warning + when to convert MCP → Skill |
| [[layer-4-network-tunneling]] | Tailscale + Cloudflare Tunnel + Twingate (Zero Trust) + tmux + VPS hardening (Fail2Ban / UFW / SSH keys) + Wolfgang's local-first contrarian view |
| [[operator-recipes]] | 4 concrete end-to-end recipes: solo+local, solo+VPS, team+private-cloud, observation-only. Recipe A patched with pilot-verified commands. |
| [[gaps-production]] | What's NOT covered: secrets vaults, IAM/RBAC, observability/audit logs, FinOps token caps, HA/failover, IaC reproducibility |

## Sources (23 unique videos across 4 drains)

### Drain 1 — Telegram bot remote control (6 videos)
- Kumo Explains — How to Connect Claude Code to Telegram (Claude Code Channels) — https://www.youtube.com/watch?v=DUztF4mVt8o
- Chris Verzwyvelt — Claude Channels: Full Setup Guide (AI Agents via Telegram) — https://www.youtube.com/watch?v=2z1Y7Wd0n0g
- Kris Torrington — Connect Claude Code to Discord in 5 Minutes — https://www.youtube.com/watch?v=lDlSGmCXht4
- Developers Digest — Claude Code Channels in 8 Minutes — https://www.youtube.com/watch?v=QZXaAc80OL0
- NetworkChuck — Claude Code on your Phone is OFFICIAL — https://www.youtube.com/watch?v=ocQ7ZKhHU5Q
- NetworkChuck — Claude Code on your phone in 10 minutes — https://www.youtube.com/watch?v=FEDiAHzS0zw

### Drain 2 — Claude Code SDK headless / programmatic (5 videos)
- Simon Scrapes — How to Use Claude Code Skills Like the 1% — https://www.youtube.com/watch?v=BZh4qHmdyx8
- Developers Digest — How to Run Claude Code For Hours Autonomously — https://www.youtube.com/watch?v=ZDkkS4U6X5Y
- IBM Technology — MCP vs API: Simplifying AI Agent Integration — https://www.youtube.com/watch?v=xIK7dGrYV6E
- NetworkChuck — Claude Code on your Phone is OFFICIAL — (cross-referenced)
- Greg Isenberg — Cursor AI Agents Work Like 10 Developers — https://www.youtube.com/watch?v=...

### Drain 3 — MCP messaging integration (6 videos)
- Kumo Explains — How to Connect Claude Code to Telegram — (cross-referenced)
- Samir Kharel — Connect an MCP server to CLAUDE DESKTOP in 7 Minutes — https://www.youtube.com/watch?v=...
- Lewis Jackson — How To Connect Claude to Trading View — https://www.youtube.com/watch?v=...
- Chris Verzwyvelt — (cross-referenced)
- Michele Torti — Master Claude Code MCP in 13 minutes — https://www.youtube.com/watch?v=...
- Mervin Praison — Claude Code on Telegram: The Game Changer — https://www.youtube.com/watch?v=GjDRlqmfoT8

### Drain 4 — Network tunneling / remote agent control (6 videos)
- logicBase Labs — Cloudflare Tunnel: Make Localhost Public — https://www.youtube.com/watch?v=...
- Wolfgang's Channel — Quick and Easy Local SSL Certificates for Your Homelab — https://www.youtube.com/watch?v=...
- Craylor — 5 Things to Know BEFORE Using Cloudflare — https://www.youtube.com/watch?v=...
- Thomas Wilde — Access your TrueNAS apps SECURELY from ANYWHERE — https://www.youtube.com/watch?v=...
- Techno Tim — Self-Hosting Security Guide for your HomeLab — https://www.youtube.com/watch?v=...
- NetworkChuck — Your Remote Desktop SUCKS! Try this instead — https://www.youtube.com/watch?v=EXL8mMUXs88

### Cross-bundle reference (creator interview)
- Boris Cherny @ Y Combinator — Inside Claude Code (already cited in [[../10x-claude-code/_index|10x-claude-code]])

**NotebookLM bundles:**
- `5f514e9c-d8e4-42be-af1e-c456dfa1e4c7` — Telegram bot
- `dafc8c4f-840b-41a1-b125-bfe973c919f0` — Claude Code SDK
- `183e3635-ea8c-4c52-9c16-11aa32e19c78` — MCP messaging
- `46ee01f8-81e3-47d6-b617-4c322359b6b9` — Network tunneling

**Compiled:** 2026-05-08

## Related topics in this wiki

- [[../workflow-ai-coding/_index|Workflow for AI Coding]] — strategic frame (harness engineering, autonomous loops). The Ralph loop pattern from [[layer-2-engine-headless-claude-code]] is the same pattern formalized in workflow-ai-coding.
- [[../10x-claude-code/_index|10x Claude Code]] — tactical configurations. Plan Mode, Git worktrees, custom skills all relevant when running headless.
- [[../claude-code-hooks/_index|Claude Code hooks]] — Stop Hooks (used by Ralph loop) + Exit Code 2 path protection are deep-dived here.
