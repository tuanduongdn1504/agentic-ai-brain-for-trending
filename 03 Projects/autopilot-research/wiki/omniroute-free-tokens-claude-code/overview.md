# OmniRoute — Overview

## Source
7-video bundle in [`raw/2026-07-20-omniroute-free-tokens-claude-code/`](../../raw/2026-07-20-omniroute-free-tokens-claude-code/_sources.md) (operator-submitted anchor `x2BmXTur4oo` DEVKIT AI + yt-search bundle) + independent ground-truth (GitHub API, WebSearch) + refute-first verification Workflow `wf_e3d4a558-e70` (23 agents).

## One-line verdict
**OmniRoute is a real, genuinely useful open-source AI gateway that aggregates ~1.6B free tokens/month across ~250 provider free tiers — but every video in the bundle blurs "free tokens for Claude Code" into "free Claude," and the "free Claude" path is either expired, ToS-violating, or an account-ban risk. The mechanism is trustworthy; the framing is systematically misleading.**

## What it is (30 seconds)
- [github.com/diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) — a **free, MIT-licensed, self-hosted "AI gateway"**: one OpenAI-compatible endpoint on your machine, behind it **~250–268 providers (90+ with a free tier, ~50 truly free)** and 500+ models.
- A **TypeScript port of the Go project [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI)** + a fork of `9router`. ~20.3K stars, Brazilian author Diego Souza, created 2026-02-13, pushed daily.
- You point Claude Code / OpenCode / Cursor / Cline / Copilot / **Claude Desktop** at OmniRoute, and it routes each request to whichever provider you configure — with quota-aware auto-fallback, prompt-compression, combos, and a dashboard.

## The core finding — "free tokens for Claude Code" is three different things
The videos collapse three very different mechanisms into one "free forever" pitch. See [[free-tokens-vs-free-claude-three-paths]]:

- **Path A — legit & useful:** route the Claude Code *client* to **free NON-Claude models** (DeepSeek, Gemini, Mistral, Kimi, Nvidia Nemotron free tiers). The anchor's own demo served **DeepSeek V4, not Claude**. This is where the "~1.6B free tokens" actually come from — 100% non-Claude. Fair use of published free tiers (subject to each provider's anti-abuse rules).
- **Path B — ToS-gray / expired:** get *real* Claude free by proxying **other vendors' free tiers** that once bundled Claude (Google **Antigravity**, AWS **Kiro**). Antigravity's free Claude was **removed ~May 2026**; Kiro's ToS **prohibits third-party proxy/harness use**. So this path is largely closed and violates those vendors' terms. (video t6)
- **Path C — banned:** reuse a **Claude subscription's OAuth token** in a third-party client (the CLIProxyAPI/OpenClaw pattern). Anthropic **explicitly banned this Jan/Feb 2026** and blocked OpenClaw, OpenCode, Roo Code, and Goose. OmniRoute inherits this capability via its CLIProxyAPI account import. See [[anthropic-oauth-ban-and-tos-risk]].

## Scorecard shape
12 verified claim clusters: **0 CONFIRMED · 9 CORRECT-BUT-INCOMPLETE · 2 MISLEADING · 1 FALSE · 0 FABRICATED**. The near-total "correct-but-incomplete" profile is the signature of a hype bundle: the *numbers* survive scrutiny, but every video omits the ToS/security/provider-caveat context that changes the decision. Full table: [[claims-scorecard]].

## Should the operator care?
- **As a tool:** Path A is a legitimate cost-reduction pattern for **non-critical, model-agnostic** work — this is the same idea as the corpus's own [[harness-engineering/personal-repo-router-multimodel]] pilot. Worth understanding.
- **For hireui / any real Claude account:** **catalog defensively, do NOT pilot Path B/C.** Routing a Claude subscription through OmniRoute to get "free Claude" risks an Anthropic ban and violates ToS. See [[hireui-relevance]].

## Key Takeaways
- OmniRoute is real and useful **as a free-non-Claude-model router** (Path A); the "~1.6B free tokens" number is honest and comes entirely from non-Claude free tiers.
- "**Free Claude**" is the misleading part: the Antigravity route is expired (removed ~May 2026), the Kiro route violates Kiro's ToS, and the OAuth-reuse route is **banned by Anthropic** (Jan/Feb 2026 enforcement).
- The mechanism is trustworthy; the marketing conflates a legal pattern with two risky/dead ones. **Do not run the "free Claude" path against a real Anthropic account.**
- Related: [[what-omniroute-is]] · [[the-1.6-billion-free-tokens-claim]] · [[anthropic-oauth-ban-and-tos-risk]] · [[security-and-privacy]]
