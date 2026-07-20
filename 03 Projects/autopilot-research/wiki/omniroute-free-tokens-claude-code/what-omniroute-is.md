# What OmniRoute Is — the tool

## Source
GitHub ground-truth ([api.github.com/repos/diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute), README + docs) + bundle transcripts (t1, t2, t3, t5) + Workflow `wf_e3d4a558-e70` verdicts.

## Identity (verified 2026-07-20)
- **Repo:** [github.com/diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) · **License:** MIT · **Language:** TypeScript
- **Stars:** ~20,300 (20,322 and climbing) · **Forks:** ~2,800 · created **2026-02-13**, pushed daily
- **Author:** Diego Souza (Diego Rodrigues de Sá e Souza), São Paulo, Brazil
- **Site:** omniroute.online · **Install:** `npm install -g omniroute` (needs **Node 22+**) · **Dashboard:** `localhost:20128`
- ⚠️ Repo description claims "**Built by 500+ contributors**" — GitHub's contributor API enumerates **257 named** (289 incl. anonymous). The "500+" is marketing inflation. See [[caveats-and-corrections]].

## What it does
OmniRoute is a **self-hosted AI gateway / router**: a single OpenAI-compatible endpoint on your own machine (or VPS) that sits *in front of* many upstream LLM providers. Your coding client only ever talks to `localhost:20128`; OmniRoute decides which upstream actually answers.

- **~250–268 providers, 500+ models** behind one endpoint (the count is version-dependent and grows fast; videos show 236 / 256 / 344, current docs say 268+ / 500+).
- **90+ providers with a free tier**, ~50 "free"; a handful advertised "free forever, no card" (Kiro, Qoder, Pollinations, LongCat…) — but see the caveats in [[the-1.6-billion-free-tokens-claim]] and [[antigravity-kiro-and-the-free-claude-window]].
- **API translator:** converts between OpenAI / Claude / Gemini API formats, so any client that accepts a custom OpenAI-compatible base URL works (Claude Code, Codex CLI, Gemini CLI, Cursor, Cline, Kilocode, OpenCode, and Claude Desktop via its "third-party inference" feature).

## Feature surface (as advertised)
- **Quota-aware auto-fallback** across a 4-tier chain (subscription → API key → cheap → free): if a provider is down/rate-limited/slow, it re-routes mid-request. ⚠️ Quota-awareness had a documented bug (GitHub issue #7387, filed/closed 2026-07-16→17) where combo routing still picked exhausted-quota accounts. See [[caveats-and-corrections]].
- **18 routing strategies** (priority, round-robin, cheapest-first, fastest-first, weighted splits, hard cost caps…). One transcript said "17" — docs say 18.
- **RTK + Caveman prompt compression** — self-reported 15–95% token savings (~89% on tool-heavy sessions). Code/URLs/JSON preserved byte-for-byte. Not independently validated. See [[compression-rtk-caveman]].
- **Combos** — named model bundles (e.g. "route this combo across these providers round-robin") the client selects by name.
- **Built-in MCP server (~94–95 tools)**, agent-to-agent (A2A) protocol, semantic cache, analytics dashboard, Desktop/PWA UI, multimodal APIs.
- **Local-first:** keys + usage + history in encrypted local SQLite; "no telemetry, no account required." (True for OmniRoute itself — but your prompts still go *upstream* to the free providers; see [[security-and-privacy]].)

## Lineage (this matters)
OmniRoute is **not** "inspired by OpenRouter" (the anchor's repeated claim is an ASR/attribution slip — "OpenRouter" is garbled as "Nouter/Narrator/NRT"). Its README Acknowledgments credit:
- a fork of **9router** (~22.7K★, "the original project this fork is built on"), and
- a **TypeScript port of [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI)** (Go, ~43.6K★, "the Go implementation that inspired this port").

CLIProxyAPI's whole purpose is wrapping CLI subscription OAuth (Claude Code, Codex, Gemini, Grok) as an API — the **exact pattern Anthropic banned**. OmniRoute inherits it (one-click import from `~/.cli-proxy-api/`). This is why the tool's capabilities are legitimate *and* it technically enables the banned path. See [[cliproxyapi-lineage-and-the-gateway-ecosystem]] and [[anthropic-oauth-ban-and-tos-risk]].

## Key Takeaways
- OmniRoute = a self-hosted, MIT, TypeScript **AI gateway**: one local endpoint → ~250+ providers → any OpenAI-compatible client.
- Genuinely feature-rich: auto-fallback, 18 routing strategies, compression, combos, MCP, local-encrypted storage.
- Its lineage is **CLIProxyAPI + 9router**, not OpenRouter — and that lineage carries the OAuth-reuse capability Anthropic banned.
- Ground-truth corrections vs the videos: "500+ contributors" → 257; "17 strategies" → 18; provider counts are version-drift, not errors.
- Related: [[overview]] · [[how-it-works-setup-and-clients]] · [[claims-scorecard]]
