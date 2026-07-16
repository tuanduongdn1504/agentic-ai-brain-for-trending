# (C) OmniRoute — Deep Dive

> LLM-wiki **v208** · built 2026-07-16 · subject `diegosouzapw/OmniRoute`
> Produced **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions` — **no workflow relied on** (the ~205K CLAUDE.md shim overflows every subagent's context > 200K → the read-only deep-dive workflow fails prompt-too-long; the v200/v202/v204/v205/v206/v207 self-throttle precedent). Source hand-fetched (repo page + raw README + ecosyste.ms + landscape); identity + lineage + landscape by WebSearch; **collision + the v207/v144 corpus-recursive links by hand-grep of `_state/` + `_patterns/`**.

---

## One line

**OmniRoute is a free, self-hosted, MIT TypeScript "AI gateway" — a single `/v1` endpoint that fans a coding agent (Claude Code / Codex / Cursor / Cline / Copilot / Antigravity) out across ~250 LLM providers (90+ with free tiers) with stacked token-compression, a 4-tier auto-fallback (Subscription → API → Cheap → Free), 18 routing strategies, an MCP server + A2A protocol, and multi-platform delivery (web / Electron desktop / Android-Termux / PWA). It openly states it "started as a fork of [9router] and a TypeScript port of the Go project [CLIProxyAPI]" — i.e. it is a TypeScript re-implementation of the corpus's own v207 subject, built into a much larger platform.**

The "double deep dive" — the two facts that matter most for this vault:
1. **OmniRoute is a TypeScript port of CLIProxyAPI (corpus v207)** + a fork of 9router (non-corpus). This is verified from OmniRoute's own README acknowledgements, not just search summaries. → It is the cleanest possible **N=2** of the §C standalone this vault minted one ship ago, and a **genuine Pattern #57 corpus-recursion** (a corpus subject that openly credits — and re-implements — another corpus subject).
2. **OmniRoute integrates the corpus's headroom v144** — its `headroom` compression engine + `ccr` retrieve-marker are openly credited to `headroomlabs-ai/headroom` (which redirects to `chopratejas/headroom` = the corpus's v144 SmartCrusher/CCR project; author now disclosed as **Tejas Chopra, Netflix**). → A **second genuine #57** in one ship.

So OmniRoute is a **doubly corpus-recursive** subject: it openly cites and builds on **two** prior corpus subjects (v207 as its port-parent, v144 as a compression-engine inspiration).

---

## What it is (from source)

**Tagline (repo/GitHub description, verbatim):** *"Never stop coding. Free AI gateway: one endpoint, 231+ providers (50+ free), connect Claude Code, Codex, Cursor, Cline & Copilot to FREE Claude/GPT/Gemini. RTK+Caveman stacked compression saves 15-95% tokens, smart auto-fallback, MCP/A2A, multimodal APIs, Desktop/PWA."*

**README headline (verbatim):** *"Never stop coding. Connect every AI tool to 250 providers — 90+ free — through one endpoint."*

**Core promise (verbatim):** *"Plug Claude Code, Codex, Cursor, Cline, Copilot & Antigravity into FREE Claude / GPT / Gemini. Auto-fallback."* The 4-tier fallback: **"Subscription → API → Cheap → Free, in milliseconds."**

It is a **self-hosted gateway** you run locally (`npm install -g omniroute` → `omniroute`; dashboard `http://localhost:20128`, API `http://localhost:20128/v1`; also Docker `diegosouzapw/omniroute`, pnpm, Arch AUR, Nix, Podman; Node ≥22 <23 or ≥24 <27). You point your coding agents at OmniRoute's `/v1`; it routes each request to the best provider under your policy.

---

## The lineage (verified from OmniRoute's own README)

OmniRoute's acknowledgements section, verbatim:

> *"OmniRoute stands on the shoulders of giants. It started as a fork of [9router](https://github.com/decolua/9router) and a TypeScript port of the Go project [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) — and from there, every subsystem below was inspired by an open-source project that got there first."*

Also verbatim:
- *"one-click account import from CLIProxyAPI (`~/.cli-proxy-api/`)"* — OmniRoute even reads v207's on-disk credential store.
- *"Special thanks to CLIProxyAPI by router-for-me — the original Go implementation that inspired this JavaScript port."*
- *"Special thanks to 9router by decolua — the original project that inspired this fork. OmniRoute builds upon that incredible foundation with additional features, multi-modal APIs, and a full TypeScript rewrite."*
- **headroom credit (verbatim):** *"[headroom](https://github.com/headroomlabs-ai/headroom) · headroomlabs-ai | 54.5k | Reversible context-compression (SmartCrusher) — inspired our `headroom` engine and the `ccr` retrieve-marker pattern."*

**Corpus-recursion map (hand-verified):**
| Upstream OmniRoute credits | Corpus? | Link |
|---|---|---|
| **CLIProxyAPI** (`router-for-me`) | **YES — corpus v207** | OmniRoute *is a TypeScript port of it* → genuine **#57** |
| **headroom** (`headroomlabs-ai/headroom` → redirects to `chopratejas/headroom`) | **YES — corpus v144** | `headroom` engine + `ccr` marker *inspired by it* → genuine **#57** |
| 9router (`decolua`) | no | non-corpus fork-parent |
| RTK (`rtk-ai/rtk`) | no | compression inspiration |
| Caveman (`JuliusBrussee/caveman`, ⭐ ~78k) | no | compression inspiration (the corpus's "caveman" hits are the ponytail v168 benchmark control-arm, a different thing) |
| LLMLingua-2 (`microsoft/LLMLingua`) | no | one bundled compression engine |
| Troglodita (`leninejunior`, PT-BR) | no | compression inspiration |

---

## Architecture (page/README-stated — NOT source-cloned; see caveats)

**Providers & economics.** ~250 providers (README badge); "231+" / "177" in other snapshots (README churn); 90+ with free tiers; **11 "free forever"** (Kiro, Qoder, Pollinations, LongCat, Cloudflare AI, NVIDIA NIM, Cerebras, AgentRouter, SiliconFlow, Z.AI GLM-Flash, OpenCode Zen). Badge claims **"~1.6B free tokens/month"** across aggregated free tiers. Major labs wrapped: OpenAI, Anthropic (Claude), Google (Gemini), xAI (Grok), DeepSeek, Mistral, Qwen, Meta, Groq, NVIDIA, MiniMax, Cohere, Perplexity, HF, Together, Fireworks, Cloudflare, Baidu.

**Routing — 18 strategies:** priority, fill-first, weighted, round-robin, p2c (power-of-two-choices), least-used, random, strict-random, cost-optimized, headroom, reset-window, reset-aware, context-relay, context-optimized, lkgp (last-known-good-path), auto (12-factor scoring), fusion (panel + judge), pipeline (chained execution). (Some snapshots say 17 — README churn.)

**4-tier auto-fallback:** *"Subscription → API → Cheap → Free, in milliseconds."*

**Token compression — a 10-engine composable stack:** Session-Dedup, CCR, RTK, **Headroom**, Relevance, **Caveman**, LLMLingua-2, Lite, Aggressive, Ultra. Engines run in sequence (default combo "RTK → Caveman"); claimed **15–95% token savings**. This is the densest token-compression instance in the corpus and lands directly on the `claude-api-cost-optimization` thread.

**MCP server:** stdio + HTTP + SSE transports; **94 tools**; 30 scopes; full audit trail. OmniRoute is thus an MCP *server* (exposes its gateway to agents), not just an MCP client.

**A2A (Agent-to-Agent) protocol:** JSON-RPC 2.0 + SSE, 6 skills, exposed at `/.well-known/agent.json`. (Corpus-first observation — see Verdict; not minted.)

**Resilience & load-balancing:** circuit breakers (provider-level) + connection cooldown (account-level) + model lockout (model-level); work-conserving quota-sharing across accounts; per-(key, model) caps; session stickiness for prompt-cache hits; deficit-round-robin.

**Other subsystems (page-stated):** OAuth auto-refresh (8 providers, PKCE); memory (SQLite FTS5 + opt-in int8 vector store); guardrails (PII / injection / vision checks); cost analytics (USD spend, per-key quotas); output-style steering; **TLS-fingerprint stealth via `wreq-js`** (anti-detection, dual-use); 3-level proxy (global / per-provider / per-connection); 42 locales; **21,000+ test cases** (claimed).

**OpenAI-compatible surface (`/v1`):** `/v1/models`, `/v1/chat/completions`, `/v1/completions`, `/v1/embeddings`, `/v1/images/generations`, `/v1/audio/transcriptions`, `/v1/audio/translations`, `/v1/ocr` (Mistral); plus `/api/mcp/stream`, `/api/mcp/sse`, and tokenized paths (`/vscode/YOUR_KEY/...`) for clients that can't send headers.

**Delivery surfaces:** web dashboard, Electron desktop, Android (Termux), PWA.

**Config:** `.env` (port/data-dir/proxy/compression); JSON/YAML (combos, routing profiles, plugins, skills manifests); Markdown drop-in skills (`skills/*/SKILL.md`); `CLAUDE.md` present in the repo (routing-artifact, incidental).

---

## Author / identity

**Diego Rodrigues de Sa e Souza** (`diegosouzapw`), São Paulo, Brazil; affiliated with **CDWA Solutions**. A **disclosed individual**, **not Anthropic**. Also authored **OmniGlyph** (a "context-as-image compression proxy" that renders bulky context as PNG pages) and an OpenCode provider-helper for OmniRoute. Prolific in the LLM-gateway / token-economy space.

---

## Metrics & provenance (§37.4)

⚠️ **This environment mocks the GitHub API (§37.4)** — all counts are page-stated, not API-verified. And OmniRoute's snapshots **conflict** across sources (fast-moving repo + heavy README churn):

| Source | Stars | Forks | Providers | Strategies | Version |
|---|---|---|---|---|---|
| GitHub repo page (rendered) | ~18k | ~2.7k | 250 | 18 | v3.8.49 |
| ecosyste.ms | 5,174 | 884 | 177 | — | — |
| GitHub description | — | — | 231+ | — | — |
| landscape/compare pages | — | — | 231+ | 17 | — |

→ **~5.2k–18k★ page-stated (conflicting) → NOT a Pattern #52 claim** (velocity unestablishable in this env even though Trendshift tracks it as repo #23589 and the growth is clearly fast). License **MIT**; TypeScript ~100% (Next.js 16 + React 19 + Node); ~5,032 commits page-stated; the "250 providers / 18 strategies / 10 engines / 94 MCP tools / 21,000+ tests / 1.6B free tokens / 15–95% savings" figures are all **page/README-stated and marketing-flavored — not independently verified** (no source clone; see the self-throttle note at the top).

---

## The ToS gray-zone (the load-bearing pilot caveat)

OmniRoute's flagship value-prop — *"connect Claude Code … to **FREE Claude** … Subscription → API → Cheap → Free … OAuth auto-refresh (8 providers, PKCE)"* — is the **same subscription-OAuth reverse-engineering** that got its parent **CLIProxyAPI v207** flagged **pilot-AVOID-for-Claude**: using a Claude subscription's OAuth login as a generic API violates Anthropic's ToS, was **blocked by Anthropic on April 4 2026** (Claude Max subscription-limit enforcement + Jan-2026 OAuth-token blocks + account suspensions), and carries **account-ban risk**. OmniRoute even reads v207's `~/.cli-proxy-api/` credential store. **No prominent ToS disclaimer was surfaced in the README.** The same fence as v207 therefore applies — see the Verdict + the Pilot Methods Menu.

Gray-zone ≠ off-goal: dual-use tooling is still GOAL-ALIGNED per routine §31 (the opencode-antigravity-auth v67 / CloakBrowser v69 / camofox v179 / Strix v190 / CLIProxyAPI v207 precedent). It just means **don't run the Claude path against your own account.**
