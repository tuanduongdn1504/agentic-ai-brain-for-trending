# (C) OmniRoute — Pilot Methods Menu (24 methods)

> LLM-wiki **v208** · `diegosouzapw/OmniRoute` · 2026-07-16
> **Blunt framing:** OmniRoute is on-goal *as a knowledge/landscape subject* and directly relevant to the `claude-api-cost-optimization` thread (compression + cost-routing). But its flagship "free Claude via subscription-OAuth" path is **ToS-violating + Anthropic-blocked (April 4 2026) + account-ban-risk** — same as its parent **CLIProxyAPI v207**, of which it is literally a TypeScript port. → **pilot-AVOID-for-Claude.** The genuinely-usable borrows are *architectural* (compression + provider-routing), used with **official, paid API keys**.
>
> ⭐ **One-thing path: A1 → A3 → B7.**

**FENCE (mandatory).** DO NOT run OmniRoute's Claude path against your Claude/Anthropic account (ToS + ban-risk). If you evaluate the *non-Claude* mechanics at all: a scratch/disposable account only + `install-snapshot` first + `npm-security-check` the `omniroute` package + inspect the Docker image + treat any stored provider OAuth tokens as high-value secrets + pin the version + note the `wreq-js` TLS-fingerprint stealth is anti-detection (dual-use). hireui uses **official API keys** per its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first); no LLM spend yet → build-it-right.

---

## A — Read & learn (zero install, zero risk)

- **A1 ⭐** Read the compression-stack + routing-strategy design (10 engines; 18 strategies; the "auto" 12-factor scorer; fusion panel+judge; pipeline chaining) as a *landscape reference* for how a mature gateway thinks about token cost and provider selection.
- **A2** Read OmniRoute *as the TypeScript sibling of v207 CLIProxyAPI* — a same-surface, different-language, much-broader re-implementation. Note what a "port" adds (compression, MCP server, A2A, multimodal, desktop/PWA) vs the Go original.
- **A3 ⭐** Read the **ToS boundary**: OmniRoute's Subscription→API→Cheap→Free + OAuth-refresh path is the subscription-OAuth reverse-engineering Anthropic blocked (April 4 2026). Internalize *why* this is off-limits for Claude — it's the exact anti-pattern hireui must never adopt.
- **A4** Read the LLM-gateway landscape it sits in (LiteLLM / OpenRouter / Portkey / one-api / new-api / kRouter / 9router) — OmniRoute's niche = subscription-OAuth-for-coding-agents + a token-compression stack.

## B — Borrow patterns (zero install, official keys)

- **B5** Borrow the **10-engine compression taxonomy** (Session-Dedup / CCR / RTK / Headroom / Relevance / Caveman / LLMLingua-2 / Lite / Aggressive / Ultra) as a menu of context-compression *ideas* for the vault's own surgical-extract discipline + the headroom v144 pilot.
- **B6** Borrow the **CCR retrieve-marker pattern** (compress-cache-retrieve: keep the original locally, inject a marker, let the model fetch on demand) — this is headroom v144's mechanism, which OmniRoute credits; it's the reversible-compression idea worth wiring into any vault compression step.
- **B7 ⭐** Reinforce hireui's **"official API keys, never subscription-OAuth reverse-engineering / CLI-token extraction"** ADR (already written for v207) and record **OmniRoute v208 as the confirming 2nd instance** of that anti-pattern. One paragraph in hireui's LLM-integration ADR + `CLAUDE.md`.
- **B8** Borrow the **multi-protocol provider-routing architecture** (one `/v1` front → many providers, with priority/weighted/cost-optimized/fallback strategies) as a *reference* for hireui's future vendor-seam (the mosh-ai A2 seam), implemented with **official keys**.
- **B9** Borrow the **4-tier fallback shape** conceptually (best → cheaper → cheapest), re-cast for hireui as "primary official model → cheaper official model → cached/deterministic" — the cost-discipline without the subscription-OAuth.
- **B10** Borrow the **resilience layering** (circuit breaker / connection cooldown / model lockout) as a checklist for any production LLM caller.

## C — Hands-on scratch (⚠️ non-Claude only, disposable account)

- **C11** IF evaluating the mechanics at all: `install-snapshot` → `npm-security-check omniroute` → run it in a scratch VM/dir against a **free, non-Claude** provider on a **disposable account**; observe the dashboard + `/v1` routing. Never the Claude path.
- **C12** Inspect the Docker image (`diegosouzapw/omniroute`) rather than `npm install -g` on your main machine; treat stored OAuth tokens as secrets; pin the tag.
- **C13** Measure a compression engine (e.g. RTK→Caveman) on a scratch JSON/log payload to see real token deltas — pair with the ccusage/OTel cost-measurement pilot.
- **C14** Read `~/.cli-proxy-api/` interop only to understand the credential-store shape — do not import a real Claude subscription.

## D — hireui / Goal-#2 (official keys, behind the CONSTITUTION)

- **D15** Write/confirm the hireui **vendor-seam** so a provider swap is a config change, using OmniRoute's routing taxonomy as the reference and **official keys** (the mosh-ai A2 thread). `agent-*` branch, hireui-rooted.
- **D16** Add a hireui **cost-routing** design note: "primary → cheaper-official → cache" fallback + per-key quotas, drawn from OmniRoute's cost-optimized strategy — no subscription-OAuth.
- **D17** Add a hireui **compression step** design note (compress tool-outputs/RAG chunks before the LLM) drawn from the headroom v144 / OmniRoute compression stack — reversible (CCR-style) so nothing candidate-relevant is silently dropped.
- **D18** Add the **anti-pattern rule** to hireui's ADR: no subscription-OAuth reverse-engineering; official keys only; treat any tool that offers "free Claude via subscription" as a ban-risk supply-chain hazard (cite v207 + v208).

## E — Personal / off-goal

- **E19** Note **OmniGlyph** (Diego Souza's context-as-image compression proxy) as a curiosity in the token-economy space — not a pilot.
- **E20** If you personally use non-Claude free tiers for throwaway experiments, OmniRoute's free-forever list is a map — disposable accounts only, not for anything ToS-sensitive.

## F — Vault-meta / audit

- **F21** Log the **doubly-corpus-recursive #57**: OmniRoute openly cites TWO corpus subjects — CLIProxyAPI v207 (its port-parent) + headroom v144 (its `headroom`/`ccr` engine). A clean data-point for the #57 running set.
- **F22** File the **N=2 instance-strengthening** of the v207 §C standalone (PROMOTION-ELIGIBLE; promotion DEFERRED to the ~v212 audit pending a fully-independent non-port 3rd instance — kRouter/one-api/new-api candidates).
- **F23** Add to the ~v212 audit agenda the **LLM-access-tooling surface synthesis** (cc-switch v73 config-switch / freellmapi v112 free-tier-stack / CodexPlusPlus v117 reseller-relay / ai-switcher v153 multi-account-rotate / opencode-antigravity-auth v67 OAuth-bridge / CLIProxyAPI v207 subscription→API gateway / **OmniRoute v208 subscription→API gateway (TS port + compression platform)**) — and the **A2A-protocol** DEFERRED watch axis + the **token-compression cluster** (headroom v144 / distill v97 / OmniRoute v208).
- **F24** 🔴 The shim is the workflow blocker again (OmniRoute analyzed inline because the ~205K CLAUDE.md overflows every subagent) — F24 = the standing shim-compaction housekeeping item (demote accreted CURRENT/PRIOR head bodies to `_state/03c` pointers to restore workflow capability).
