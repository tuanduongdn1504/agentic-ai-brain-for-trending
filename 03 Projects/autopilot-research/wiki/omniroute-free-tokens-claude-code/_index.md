# omniroute-free-tokens-claude-code

> **Topic index.** Maintained per `../../CLAUDE.md` librarian rules.
> **Compiled:** 2026-07-20 (Path 1 `/loop`; 7-video bundle + refute-first Workflow `wf_e3d4a558-e70`, 23 agents + main-loop Opus re-verification).
> **Corpus position:** NEW topic #70 (independently collision-checked; no prior OmniRoute/CLIProxy topic here).

## What this is

**OmniRoute** ([github.com/diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute), ★~20.3K, MIT, TypeScript, Brazilian author Diego Souza) is a free, self-hosted **AI gateway**: one OpenAI-compatible endpoint on your machine, behind it **~268 providers / 500+ models** (90+ with free tiers), with quota-aware auto-fallback, RTK+Caveman prompt compression, combos, MCP, and a dashboard. It is a **TypeScript port of the Go project CLIProxyAPI** + a fork of 9router. This topic catalogs a 7-video bundle (operator-submitted anchor `x2BmXTur4oo` DEVKIT AI, Vietnamese) that markets it as *"get 1.6 billion free tokens for Claude Code."*

**Verdict: real, useful tool — systematically misleading framing.** The "~1.6B free tokens" is honest and comes **100% from non-Claude free tiers** (the anchor's own demo served DeepSeek V4, not Claude). "Free tokens **for Claude Code**" blurs into "free **Claude**," and every route to actual free Claude is either **expired** (Google AntiGravity removed Claude ~May 2026), **ToS-violating** (AWS Kiro prohibits third-party proxies), or **banned** (Anthropic blocked subscription-OAuth reuse in Jan/Feb 2026, cutting off OpenClaw/OpenCode/Roo/Goose — the exact CLIProxyAPI pattern OmniRoute inherits).

**Scorecard (12 clusters): 0 CONFIRMED · 9 CORRECT-BUT-INCOMPLETE · 2 MISLEADING · 1 FALSE · 0 FABRICATED** — a hype-bundle profile (trustworthy numbers, omitted risk context). **hireui: AVOID any candidate-facing / Path-B / Path-C use; STUDY the paid, hardened, ToS-clean version of a multi-provider cost-routing seam.**

## The three-path frame (read this first)
- **Path A** ✅ — route the client to **free non-Claude** models (DeepSeek/Gemini/Mistral/Kimi). This is the real "1.6B tokens"; legal, useful for routine work.
- **Path B** ⚠️ — real Claude via proxying **AntiGravity/Kiro** free tiers. Expired / violates Google-AWS ToS.
- **Path C** 🚫 — reuse a Claude **subscription OAuth token** (CLIProxyAPI pattern). Banned by Anthropic; account-ban risk.

## Articles

- [[overview]] — one-page verdict + the three-path frame.
- [[what-omniroute-is]] — the tool: architecture, features, lineage, ground-truth identity.
- [[the-1.6-billion-free-tokens-claim]] — the headline number: real, honest, and 100% non-Claude.
- [[free-tokens-vs-free-claude-three-paths]] — **load-bearing**: Path A / B / C disentangled, with the one-glance table.
- [[anthropic-oauth-ban-and-tos-risk]] — Anthropic's Jan/Feb 2026 OAuth ban; allowed vs banned; where OmniRoute sits.
- [[antigravity-kiro-and-the-free-claude-window]] — why t6's "free Claude" is expired/prohibited (and why a live demo can still appear to work).
- [[cliproxyapi-lineage-and-the-gateway-ecosystem]] — CLIProxyAPI/9router lineage; Bifrost/LiteLLM/OpenRouter/OpenCode; the shared "swap the engine, keep the cockpit" mechanism.
- [[how-it-works-setup-and-clients]] — install, VPS/systemd, provider/combo config, Claude Desktop third-party-inference, per-request flow.
- [[compression-rtk-caveman]] — the 15–95%/89% compression claim (self-reported; code/JSON preserved).
- [[security-and-privacy]] — unhardened VPS defaults + "local-first ≠ private" (upstream free tiers log/train).
- [[claims-scorecard]] — the full 12-cluster table.
- [[caveats-and-corrections]] — method limits, the 2 empty verifiers, 3 main-loop re-verifications, ASR normalization.
- [[hireui-relevance]] — AVOID Path B/C + candidate data; borrow the disciplined paid-seam pattern.
- [[source-provenance]] — the 7 videos, dropped candidates, ground-truth sources, workflow stats.

## Cross-links
[[harness-engineering/personal-repo-router-multimodel]] (operator's own multi-model router pilot — the disciplined analog) · [[hermes-agent/_index]] (prior "personal-agent" hype-verification, t69) · [[local-ai-coding-agents/_index]] (local/private alternative to upstream routing) · [[claude-api-cost-optimization/_index]] · [[cowork-third-party-inference/_index]] · [[external|Storm Bear: hireui candidate-LLM legibility ADR]]
