# (C) CLIProxyAPI — Deep Dive

> **Wiki v207** · built 2026-07-16 · subject `router-for-me/CLIProxyAPI` · operator-requested ("Build LLM wiki for `github.com/router-for-me/CLIProxyAPI`").
> **Provenance discipline:** produced **INLINE + hand-verified** per `feedback_wiki_verify_independently_check_collisions`. **NOT source-cloned** — the ~205K shim overflows subagent context (prompt-too-long on all agents at v200/v202/v204/v205/v206 → the self-throttle precedent), so no read-only workflow was run. Facts below are **repo-page / README / official-docs (help.router-for.me) / landscape-search / ToS-research verified**; the internal Go architecture is documented-not-inspected (flagged inline).

---

## 1. One-sentence thesis

CLIProxyAPI is a **self-hosted Go proxy server that reverse-engineers the OAuth login flows of interactive AI *CLI* tools** — Claude Code, ChatGPT Codex, Gemini CLI / Antigravity, Grok Build, Kimi — **and re-exposes those subscription accounts as standard, multi-protocol API endpoints** (OpenAI Chat Completions / OpenAI Responses / Gemini / Claude Messages / Codex / Grok), with multi-account load-balancing, so any client or SDK can call the models you already pay a *subscription* for as if they were a plain *API*.

The repo tagline (verbatim, GitHub description):

> *"Wrap Antigravity, ChatGPT Codex, Claude Code, Grok Build as an OpenAI/Gemini/Claude/Codex compatible API service, allowing you to enjoy the free Gemini 3.1 Pro, GPT 5.5, Grok 4.3, Claude model through API."*

The README one-liner (verbatim):

> *"A proxy server that provides OpenAI/Gemini/Claude/Codex/Grok compatible API interfaces for CLI."*

The word doing the heavy lifting is **"free"** — the value proposition is: *use the models bundled in your $20–$200/mo CLI subscription through a generic API, instead of paying metered API rates.* That is also exactly what makes it a **terms-of-service gray zone** (see §7).

---

## 2. What it actually is (facts)

| Field | Value (page/README/docs-stated §37.4) |
|---|---|
| Repo | `router-for-me/CLIProxyAPI` |
| Tagline | "…OpenAI/Gemini/Claude/Codex compatible API service…through API" |
| Language | **Go 100%** |
| License | **MIT** |
| Stars | **~42.4k** (a 2nd search returned ~42.2k — page-stated, sources vary → **NOT a Pattern #52 claim**) |
| Forks | ~6.8k |
| Releases | **761** (extraordinary release velocity) |
| Latest release | **v7.2.80** (2026-07-15) |
| Docker image | **`eceasy/cli-proxy-api`** ← *the load-bearing corpus link, §5* |
| Docs | help.router-for.me (also a Mintlify mirror) |
| Author | **router-for-me / "Router-For.ME"** — a **bare GitHub org**, footer "Copyright © 2025-present Router-For.ME", no disclosed individual/company |
| Go SDK | `github.com/router-for-me/CLIProxyAPI/v6/sdk/cliproxy` (published on pkg.go.dev) |

**Sibling repos under the same org (an ecosystem, not a single repo):**
- **`router-for-me/EasyCLI`** — a **Tauri v2 desktop GUI** to manage/operate CLIProxyAPI in local or remote mode.
- **`router-for-me/Cli-Proxy-API-Management-Center`** — a **WebUI** that talks to the proxy's Management API (`/v0/management`) to read/update config, upload credentials, view logs.
- 20+ community projects listed in the README build on it (desktop apps, VS Code extensions, dashboards, and at least one downstream **MCP server** — "Grok Search MCP" — that wraps CLIProxyAPI; CLIProxyAPI itself ships **no** MCP server).

---

## 3. Supported providers & models (README-stated, 2026-07)

| Vendor | Models exposed | Access path |
|---|---|---|
| **Anthropic Claude** | Fable, Opus, Sonnet | **OAuth login (Claude Code)** — ⚠️ ToS-blocked, §7 |
| **OpenAI** | GPT-5.6, GPT-5.5 | OAuth login (Codex) |
| **Google Gemini** | 3.5 Flash, 3.1 Pro | OAuth (Gemini CLI / Antigravity) |
| **xAI Grok** | 4.5, Composer 2.5 Fast | OAuth login (Grok Build) |
| **Moonshot Kimi** | K2.7 Code, K2.6 | OAuth or compatible API |
| **Any OpenAI-compatible upstream** | e.g. OpenRouter | config (API key) |

Front-side (the endpoints *clients* call) exposes: **OpenAI Chat Completions** (`/v1/chat/completions`), **OpenAI Responses**, **Gemini** (`/v1beta/models/...`), **Claude Messages** (`/v1/messages`), **Codex** endpoints, plus **path-based provider routing** (`/api/provider/{provider}/v1/messages`) so you can pin a request to a specific backend.

---

## 4. Architecture & mechanism (docs-stated — NOT source-cloned)

The "double deep dive" mechanism, assembled from the official docs + third-party setup guides (flagged as documented-not-inspected):

1. **Credential capture via OAuth.** For each supported CLI tool you run an OAuth login *through* CLIProxyAPI; it captures + stores the OAuth session/refresh credentials that the official CLI tool would normally hold. (The docs describe these as "OAuth login sessions" / "OAuth-related credentials" that "require security boundaries" but give **no** specifics on storage format or encryption — a gap.)
2. **Protocol translation front-end.** Incoming requests in *any* supported protocol (OpenAI/Gemini/Claude/Codex/Grok) are normalized, routed to the right backend, and the backend's streaming response is translated back into the client's requested protocol. *"Use a single protocol to access all models."*
3. **Multi-account load-balancing.** Multiple accounts per provider are rotated round-robin ("multi-account rotation and load balancing for Gemini, OpenAI, and Claude"). Implementation details (rotation algorithm, health-checking) are **not** documented.
4. **Config + Management API.** A YAML config (`config.example.yaml`) + a Management API (`/v0/management`, documented in `MANAGEMENT_API.md`) that the WebUI and EasyCLI GUI drive to update config, upload credentials, and read logs at runtime.
5. **Reusable Go SDK.** The core is embeddable as a Go library (`sdk/cliproxy`) — so other Go programs can host the proxy in-process.

**Documented architectural caveat (verbatim from a setup guide):** *"a model name does not uniquely identify a backend. If multiple backends expose the same client-visible model name, the path alone may not lock the request to the backend that actually performs inference"* — i.e. alias management is on you, and a mislabelled backend can silently serve a request.

**Feature list (README):** OpenAI/Gemini/Claude/Grok-compatible endpoints · Codex/Claude-Code/Grok-Build support via OAuth login · streaming + non-streaming · function-calling/tools · multimodal (text + images) · multi-account round-robin · OpenAI-compatible upstream providers via config · reusable Go SDK.

---

## 5. ⚠️ The load-bearing corpus link — this is `eceasy/cli-proxy-api` (hand-verified)

**cortex-hub v181** (`lktiep/cortex-hub`, wiki'd 2026-06-22) bundled its LLM gateway as the third-party Docker image **`eceasy/cli-proxy-api:latest` on `:8317`** (recorded verbatim in `_state/03c`). Independent WebSearch confirms **CLIProxyAPI publishes exactly that Docker image** (`eceasy/cli-proxy-api`), and the sibling `Cli-Proxy-API-Management-Center` README describes itself as "based on CLI-Proxy-API."

**Therefore: `router-for-me/CLIProxyAPI` IS the "CLIProxy" that cortex-hub v181 silently bundled.**

This means **cortex-hub v181 bundled TWO now-corpus subjects**:
- **GitNexus v33** (`abhigyanpatwari/GitNexus`) as its code-intelligence engine, and
- **CLIProxyAPI v207** (`eceasy/cli-proxy-api`) as its LLM gateway.

This is a **corpus-recursive DEPENDENCY** data-point (an earlier corpus ship used this later ship as a load-bearing runtime dependency), of the same shape as the GitNexus-v33-inside-cortex-hub finding. It is **NOT Pattern #57** (v181 did not *cite* CLIProxyAPI as an intellectual influence — it silently incorporated it as a black-box dependency; and #57 is normally *subject cites an earlier subject*, whereas here an earlier ship bundled this later ship). Recorded as a cross-reference data-point, not a #57 promotion.

---

## 6. Landscape — corpus-first-for-surface, NOT world-first

CLIProxyAPI is the **world-canonical flagship** of a real, populated class of "turn a CLI subscription into a unified API" tools:

- **`aryan877/claude-proxy`** — a peer ("Run Claude Code on GPT-5.6 Codex, Gemini 3, GLM-5.2, Claude…, a local Anthropic-compatible proxy with in-session /model switching and OAuth login").
- **`kittors/CliRelay`** — a near-identical-description fork/mirror.
- **`kur4ge/CLIProxyAPI`** — a fork.
- **`ben-vargas/ai-cli-proxy-api`** — an explicit **downstream enhancement** ("Enhancement of CLIProxyAPI to support Factory and Amp CLI…").

So the "subscription→unified-API proxy" surface is populated, and several projects **fork CLIProxyAPI directly** — it is the biggest, most-forked, most-canonical instance, but **not the world-first** of the idea. This is the **Kilo-Code v177 / awesome-llm-apps v201 "world-canonical NOT world-first"** situation.

(Adjacent-but-inverse class, for context: `musistudio/claude-code-router` and CLIProxyAPI's own multi-model support route Claude Code *out* to other models; the *core* CLIProxyAPI move is the reverse — expose Claude/Codex/Gemini/Grok subscriptions *as* APIs.)

---

## 7. ⚠️ The terms-of-service gray zone (fence-defining)

CLIProxyAPI's flagship value ("enjoy the free … Claude model through API") is, for **Claude specifically**, ToS-violating and now largely defeated:

- **Jan 2026** — Anthropic **enforced its ToS against tools that intercept the Claude Code OAuth flow, extract the access token, and make API calls impersonating Claude Code**. Tools in this class (OpenClaw, OpenCode, others) had their consumer OAuth tokens **blocked** and **accounts suspended** (web-reported).
- **April 4 2026** — Anthropic **blocked third-party harnesses from using Claude Max subscription limits.** Using CLIProxyAPI's subscription-OAuth path for Claude is reported to **no longer be viable** without paying Anthropic's separate "extra usage" pay-as-you-go.
- **What remains allowed:** the official `claude` CLI binary (Anthropic's own product) on any machine.

CLIProxyAPI's *mechanism* (reverse-engineer a CLI-tool OAuth session → use it as an API) is precisely the class Anthropic acted against. Other providers (Gemini, Codex, Grok, Kimi) may still function, but each carries the same subscription-vs-API ToS exposure + account-ban risk. **No prominent legal/ToS disclaimer surfaced on the docs homepage or README** (contrast the corpus's opencode-antigravity-auth v67, which foregrounded a CAUTION block + a legal footer — noted, not asserted-absent since the repo was not cloned).

**Security surface:** it captures + persists OAuth session/refresh credentials for your subscription accounts (credential-sensitive), and is typically deployed via Docker (`curl`/compose). Treat the stored tokens as high-value secrets; a leaked config = someone else billing/impersonating your accounts.

---

## 8. Corpus neighborhood (the (d) map)

CLIProxyAPI sits dead-center in a neighborhood the vault has repeatedly studied:

| Corpus subject | What it does | vs CLIProxyAPI |
|---|---|---|
| **cc-switch v73** (LV#22 8a) | Tauri GUI that rewrites Claude Code's provider **config** to point elsewhere | Points a client *at* an endpoint; CLIProxyAPI *is* the endpoint (a gateway) |
| **freellmapi v112** (LV-C2) | Free-tier **stacking** as capacity aggregation | No subscription-OAuth; different source |
| **CodexPlusPlus v117** (LV-C2 + LV#22 8b) | Points a coding agent at **reseller relay** endpoints + session mgmt | Reseller relays sell API access; CLIProxyAPI uses *your own* subscriptions, self-hosted |
| **ai-switcher v153** (§C + LV#22 8c) | Multi-**account** rotation on quota exhaustion | No unified-API front; different capability |
| **opencode-antigravity-auth v67** (Pattern #83 83c, T4 Bridge) | **Single-provider OAuth-credential BRIDGE** — lets `opencode` use Antigravity creds | ⭐ **closest cousin** — same core "reverse-engineer a CLI-tool OAuth" idea, but a single-provider *bridge plugin*, not a multi-provider *API gateway service* |
| **Pattern #18 #8** | Multi-Source LLM **Aggregator** (routes providers) | CLIProxyAPI *is* an instance — but the subscription-OAuth *source* + unified multi-protocol *front* is the distinctive |
| **cortex-hub v181** | Bundled `eceasy/cli-proxy-api` as its LLM gateway | ⭐ **corpus-recursive dependency** (§5) |
| **EasyCLI** (same org) | Tauri desktop GUI *for the proxy* | LV#22 adjacency (manages a proxy, not "another coding agent" directly) |

Also on the operator's live **claude-api-cost-optimization** pilot thread (the mosh-ai A2 vendor-seam) — CLIProxyAPI is a *reference architecture* for a multi-protocol provider-routing layer, though hireui must use **official API keys**, never subscription-OAuth reverse-engineering.

---

## 9. Honest maturity read

**Strong:** Go 100%, MIT, ~42.4k★, **761 releases** (relentless cadence), v7.2.80, a full ecosystem (GUI + WebUI + SDK + 20+ community projects), adopted as another OSS project's gateway (cortex-hub v181). This is not a toy — it is a widely-used, actively-maintained piece of the "grey-market LLM access" infrastructure.

**Weak / caveats:** (1) internal architecture **documented-not-inspected** (no source clone this session); (2) star count page-stated §37.4 (→ not #52); (3) the **ToS gray zone + account-ban risk** — its headline Claude use is blocked since April 2026; (4) the "model name ≠ backend" alias footgun the docs themselves flag; (5) OAuth-credential storage format/encryption undocumented; (6) no prominent ToS disclaimer surfaced. A high-velocity project in an adversarial cat-and-mouse with the vendors whose auth it wraps — expect the Claude path in particular to keep breaking.
