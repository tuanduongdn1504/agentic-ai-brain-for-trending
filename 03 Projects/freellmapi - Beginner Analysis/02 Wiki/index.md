# freellmapi — Wiki (v112)

> `tashfeenahmed/freellmapi` · **One OpenAI-compatible endpoint. Twelve free LLM providers. ~1B+ tokens/month.** · An OpenAI-compatible **proxy/gateway** that stacks the free tiers of 12 providers behind a single `/v1/chat/completions`, with a priority router, automatic fallover, per-key rate-tracking, and an encrypted key store.

**(C) Claude-generated wiki page.** Fetched 2026-05-29 (GitHub API + README). Routine v2.3.1, wiki #112.

---

## Identity

| Field | Value |
|---|---|
| Repo | [`tashfeenahmed/freellmapi`](https://github.com/tashfeenahmed/freellmapi) |
| What | OpenAI-compatible **multi-provider aggregation proxy** (free-tier LLM gateway) |
| Tier / archetype | **T2 Service** / Multi-Provider LLM API Aggregation Proxy |
| Stars / forks | **6,171★ / 938 forks** (fork_ratio **0.152** — strong active-deployment) |
| Subscribers / open issues | 28 / 34 |
| Created / pushed | 2026-04-21 / 2026-05-26 (**~38 days** old at fetch) |
| Velocity | **~162 stars/day → Pattern #52 HIGH-NOT-EXTREME** (150–300/d), short 38-day window |
| License | **MIT** (LICENSE file + GitHub API agree — clean) |
| Language | **TypeScript ~98%** (+ CSS / JS / HTML) |
| Packaging | self-hosted **Node 20+** server (git clone + `npm`) + React/Vite dashboard; **no npm package, 0 tags, 0 releases** |
| Default branch / homepage | `main` / `tashfeenahmed.github.io/freellmapi` |
| Author | **Tashfeen Ahmed** (@tashfeenahmed) — Microsoft, Dublin; 12-yr GH account; tashfeen.me; @tashfene |
| Contributors | ~12 community contributors (incl. @VinhPhamAI) |

## What it is

Every major AI lab now ships a free tier (a few M tokens/month, a few K requests/day). On its own each is a toy; **stacked, they add up to ~1.3 billion tokens/month** across dozens of models. The pain is that stacking by hand means *N* SDKs, *N* rate limits, *N* failure points. FreeLLMAPI collapses that into **one OpenAI-compatible endpoint** — point any OpenAI client's `base_url` at your local server and it routes transparently across whichever providers you've added keys for.

**The 12 providers:** Google (Gemini 2.5 Flash / 3.x) · Groq (Llama 3.3/4, GPT-OSS, Qwen3) · Cerebras (Qwen3 235B) · SambaNova (DeepSeek V3.x, Llama 4, Gemma 3) · Mistral (Large 3, Medium 3.5, Codestral, Devstral) · OpenRouter (21 free models) · GitHub Models (GPT-4.1, GPT-4o) · Cloudflare (Kimi K2, GLM-4.7, GPT-OSS, Granite 4) · Cohere (Command R+, Command-A) · Z.ai/Zhipu (GLM-4.5, GLM-4.7 Flash) · NVIDIA (NIM, *disabled by default*) · HuggingFace (router → DeepSeek V4, Kimi K2.6, Qwen3).

## Architecture

```
OpenAI SDK / curl / any OpenAI client
   │  Bearer freellmapi-…
   ▼
Express proxy (:3001)  /v1/chat/completions  /v1/models
   ▼
Router  ── 1. pick highest-priority model with a healthy key under all rate caps
        ── 2. AES-256-GCM-decrypt key, call provider SDK
        ── 3. on 429/5xx/timeout → cooldown + retry next model (up to 20 attempts)
   ▼
Google · Groq · Cerebras · OpenRouter · HuggingFace · …(12 total)
```

- **Adapter-per-provider** (`server/src/providers/*.ts`) — one file per provider implementing a `Provider` base class: `chatCompletion()` + `streamChatCompletion()`. Adding a provider = copy the `openai-compat.ts` template, wire it in, seed its models, add a test.
- **Priority router** (`server/src/services/router.ts`) — picks a model per request.
- **Rate-limit ledger** (`server/src/services/ratelimit.ts`) — in-memory RPM/RPD/TPM/TPD counters per `(platform, model, key)`, backed by SQLite, with cooldowns on 429s.
- **Health service** (`server/src/services/health.ts`) — periodic probes mark keys `healthy` / `rate_limited` / `invalid` / `error`.
- **Storage** — SQLite (`better-sqlite3`) with **AES-256-GCM envelope encryption** for keys at rest; decryption happens in-memory just before a request.
- **Dashboard** (`client/`) — React + Vite + shadcn/ui admin surface: Keys, Fallback Chain reorder, Analytics, Playground.

**Notable features:** streaming (SSE) + non-streaming · OpenAI-style **tool-calling** that round-trips across providers (Gemini requests translated to `functionDeclarations`/`functionResponse` and back) · **sticky sessions** (a multi-turn conversation keeps talking to the same model for 30 min to avoid the mid-conversation hallucination spike from model-switching) · **unified API key** (`freellmapi-…` bearer; apps never see upstream provider keys) · `X-Routed-Via: <platform>/<model>` + `X-Fallback-Attempts: N` response headers · ~40 MB RSS at idle behind PM2/systemd.

## Corpus position

**PRIMARY — Pattern #18 sub-archetype #8 "Multi-Provider/Runtime LLM Aggregator" N=2 STRENGTHENING.** Anchor = **[[v73 cc-switch]]** (registered PROVISIONAL N=1). Both aggregate **~12 LLM providers** into one surface — but cc-switch is a desktop **config-switcher** (switch one provider active by rewriting runtime config; one active at a time) while freellmapi is a server-side **live-routing proxy** (all providers live, per-request routing + fallover). Same archetype, distinct mechanism, ~9× scale gap, different author = genuine cross-instance spread. This **directly relieves the v2.4-deferred item** "Multi-runtime-aggregator-as-distinct-sub-archetype (v73 N=1 only)." Honest open question for the audit: v73 was "multi-**runtime**-aggregator", freellmapi is "multi-**provider**-aggregator" → generalize the label to "Multi-Source LLM Aggregator" with 2 sub-variants (8a config-switcher / 8b live-routing-proxy), or treat freellmapi as a sibling sub-archetype. Full proposal: `01 Analysis/(C) Pattern-18-Multi-Provider-Aggregator-sub-archetype-N2-strengthening.md`.

**Secondary (OC layer):**
- **Pattern #84 Cross-Vendor Ecosystem-Tolerance** — the **strongest cross-vendor subject in the corpus** (12 vendor APIs behind one adapter layer); provider-side aggregation = the inverse of 84c's consumer-side provider-agnostic-distribution.
- **Pattern #18 sub-mechanism B → protocol-variant B3 "OpenAI-compatible-API"** — one-service-many-CLIENTS (OpenAI SDK / LangChain / LlamaIndex / Continue / **Hermes** all point at it); joins B1 MCP (v70) + B2 CDP.
- **Pattern #57 57c framework/provider-citation density** — Hermes (**[[v78 ECC]]** corpus-recursive) · DeepSeek V4 (**[[v72 DeepSeek-TUI]]**) · Mistral · Z.ai/GLM · Qwen · Kimi · LangChain/LlamaIndex/Continue.
- **Pattern #66 supply-chain/security** — AES-256-GCM key-encryption + unified-key abstraction + `ENCRYPTION_KEY`-required startup + explicit dev-key-fallback warning.
- **Pattern #83 honest-deficiency-disclosure (STRONG)** — full Limitations / Not-yet-supported / Disclaimer / ToS-review sections (below).
- **Pattern #82 quantitative-marketing** ("~1.3B tokens/month", "up to 20 attempts", "~40 MB RSS"); **Pattern #52 HIGH-NOT-EXTREME N+1**; **Library-vocab #19 Deliberately-Narrow Distribution N+1** ("the scope is deliberately narrow").
- **Library-vocab candidates** — "Free-Tier-Stacking-as-Capacity-Aggregation" (economic framing) + "Sticky-Session Model-Affinity (anti-hallucination-on-switch)" (N=1 each).

## Functional fit (Storm Bear)

**Verdict: STRONG INCLUDE 3/4** — (a) **FAIL** / (b) STRONG / (c) STRONG / (d) STRONG. NOT STRONGEST (no STRONGEST criterion). Full reasoning: `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md`.

- **(a) FAIL** — Tashfeen Ahmed is a **Microsoft, Dublin** engineer (Pakistani-heritage); none of the 7 (a) sub-axes PASS. Not a VN/Asian-cluster cultural-peer; English-only (no locale-inclusion); and although he works *at* Microsoft, this is a **personal** repo, not `microsoft/*`, so it is **not** (a)-7 Foundational-Vendor-Direct-Source either. Per §25 + the v98 precedent, no new (a) sub-axis is coined for a single South-Asian-Dublin instance. Mirrors v97 / v98 / v108.
- **(b) STRONG** — **LOW cost to try** (clone + `npm install` + one instant-free key like Groq + `npm run dev`; reversible via folder-delete; the vault already runs Node). A one-endpoint multi-provider gateway is a real **software-dev utility** for experimentation / side-projects / bulk-cheap tasks — squarely in Storm Bear's "I build software" + "master autonomous agents" wheelhouse. **Honest caveat:** it offers **no frontier models** → it is **NOT a Claude replacement** and does **not** serve the core Claude-based wiki routine.
- **(c) STRONG** — an instructive **reference architecture** for multi-provider agent infrastructure (adapter pattern · priority router · rate ledger · health · fallover · sticky sessions · key-encryption · cross-provider tool-call translation).
- **(d) STRONG** — high corpus connectivity: sibling to v73 cc-switch, routes v72's DeepSeek V4, cites v78's Hermes; Patterns #84/#18/#57/#66.

**Pilot:** MEDIUM-RELEVANCE side-utility (not Tier-1). It routes *away* from Claude, so it complements — but does not join — the Claude-Code-adjacent pilot stack (claude-mem memory / harness process / humanizer de-slop / cclog-cli observability). A genuine ~15-min trial path exists (clone + 1 free key + Playground), reversible; worth it only if/when Storm Bear wants free multi-provider inference for a *side* project, not for the vault's wiki work.

## Honest limitations (from the README — Pattern #83 disclosure)

- **No frontier models.** Tops out around Llama 3.3 70B / GLM-4.5 / Qwen3 Coder / Gemini 2.5 Pro. *"For hard problems, pay for a real API."*
- **Intelligence degrades as the day progresses** — top models have the lowest daily caps; the router falls to weaker models late in the day, resets at UTC midnight.
- **Variable latency** (Cerebras/Groq fast; others not); **free tiers change without notice**; **no SLA, by definition**; **local-first** (no multi-tenant auth — *"don't expose it to the internet"*).
- **Not yet supported:** embeddings, image gen, audio, vision/multimodal, legacy completions, moderation, `n>1`, multi-tenant billing.

## Honest non-claims

- **Not a Pattern #52 promotion** (HIGH-NOT-EXTREME CONFIRMED at v73; this is short-window N+1).
- **Not a Claude Code skill / not in the agentskills.io (57k) chain** — it is a proxy that OpenAI-clients consume; no SKILL.md/AGENTS.md/plugin.
- **No new top-level Pattern** — PRIMARY is sub-archetype N=2 STRENGTHENING, not a CONFIRMED promotion.
- **Not (a)-7** — personal repo, not at `microsoft/*`.
- CORPUS-FIRST claims are modest + pressure-test-ready: first OpenAI-compatible live-routing aggregation *proxy* (vs v73's config-*switcher*) + corpus-novel free-tier-stacking economic framing — held as cautious notes, not headline firsts.

## Sources

- Repo + GitHub API metadata + README (fetched 2026-05-29).
- Corpus cross-refs: [[v73 cc-switch]] (PRIMARY anchor) · [[v72 DeepSeek-TUI]] · [[v78 ECC]] · Pattern #18 / #84 / #57 / #66 / #82 / #83 / #52 (`PATTERN_LIBRARY.md` + `_patterns/`).
- Routine: `05 Skills/llm-wiki-routine-v2.3.md` (v2.3.1).
