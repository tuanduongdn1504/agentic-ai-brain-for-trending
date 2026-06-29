# Original #3 — Kimi / Moonshot AI (the model + API)

## Source

[platform.kimi.ai/docs](https://platform.kimi.ai/docs) (API overview, models, thinking-model guide), [kimi.com membership pricing](https://www.kimi.com/help/membership/membership-pricing), Simon Willison on K2 Thinking, multiple 2026 model write-ups, LiteLLM provider PR. Workflow `wf_1ac2a814-456` facets 3 + 4, with adversarial verification that **corrected several secondary-source claims**. This is the deepest original — the operator's cost + 3P-inference threads make Kimi the most actionable piece.

## Timeline (so you don't mix up versions)

| When | Model | Notes |
|---|---|---|
| Nov 2025 | **Kimi K2 Thinking** | 256K ctx, INT4, long-horizon tool use (200–300 sequential calls), Modified-MIT open weights |
| Apr 2026 | **Kimi K2.6** | general-purpose; **the model era at the time of this video (2026-04-23)** |
| **Jun 12 2026** | **Kimi K2.7-Code** | 1T-param MoE (32B active), 256K ctx, ~30% fewer reasoning tokens than K2.6, coding-focused; **released AFTER the video** |

> **So:** the video's "Kimi" + "disable thinking" reflects the **K2.6 / K2-Thinking era**. The current coding flagship is **K2.7-Code**, which behaves differently on the thinking toggle (below).

## The API (this is the integration target)

- **OpenAI-compatible.** Official docs: "OpenAI-compatible HTTP APIs… use the OpenAI SDK directly" by changing `base_url`. Works with the OpenAI Python/Node SDKs, LangChain, LiteLLM, Dify, etc.
- **Base URLs (region-split, keys not interchangeable):**
  - International: **`https://api.moonshot.ai/v1`**
  - China: **`https://api.moonshot.cn/v1`**
- **Model-name strings:** `kimi-k2.7-code`, `kimi-k2.7-code-highspeed`, `kimi-k2.6`, `kimi-k2.5` (multimodal), legacy `moonshot-v1-8k/32k/128k`. (Many older preview names — `kimi-k2-thinking`, `kimi-latest`, etc. — are **deprecated as of June 2026**.)
- **Auth:** API keys come from the **platform console** and are shown once (copy immediately). This is **separate from the kimi.com consumer subscription.**

## The "disable thinking" toggle (precisely)

- Parameter is a JSON object: **`thinking.type: "enabled"` (default) | `"disabled"`**.
- On **K2.5 / K2.6**: you *can* set `"disabled"` → faster + cheaper, lower reasoning depth (this is exactly the video's claim, and it held at video time).
- On **K2.7-Code**: thinking is **always on** — passing `"disabled"` **errors**. (K2.7 instead reduces reasoning tokens ~30% internally + offers a `-highspeed` variant.)
- K2.6 adds `thinking.keep: null | "all"` to carry reasoning across turns.

**Practical:** the video's cost-via-disable-thinking move requires K2.6 (or earlier). On the newest coding model it's not available.

## Pricing (per million tokens; verified)

| Model | Input | Output | Cache-hit input |
|---|---|---|---|
| Kimi K2.5 | $0.60 | $2.50 | ~$0.10 |
| Kimi K2.6 | $0.60 | $2.50 | ~$0.16 |
| Kimi K2.7-Code | ~$0.95 | ~$4.00 | (caching available) |
| **Claude Opus 4.8** (ref) | **$5** | **$25** | (90% off cached) |

- Kimi is **~5–8× cheaper than Claude Opus** on tokens; **prompt caching cuts input ~80–85%** (same lever as your [[claude-api-cost-optimization/_index]] work, cross-provider).
- ⚠️ Fair comparison: against **Claude Sonnet/Haiku** (your likely codegen tiers) the gap narrows — do the math at *your* tier, not just vs Opus.

## The "$39 / 4 plans" correction

The video: "go to kimi.com, you must buy a plan (4 plans), I use the $39 one, then console → API key." Verified reality:

- **kimi.com has 5 consumer tiers:** Adagio (free), Moderato ($19), **Allegretto ($39)**, Allegro ($99), Vivace ($199). The "4 plans" = the 4 *paid* tiers.
- **$39 Allegretto is a *consumer chatbot* subscription** (K2.6 chat + agent/Deep-Research/Kimi-Code credits) — **it does not directly grant API token credits.**
- **API usage (what Omnilogin calls) is pay-as-you-go token billing from the platform console**, separate from the consumer plan.
- → **You don't necessarily need the $39 consumer plan to get an API key.** (Regional flows differ: international `platform.moonshot.ai` vs the Chinese `kimi.com` consumer funnel — the presenter may have hit a regional gate.)

## How good is it for code? (honest read)

- **K2 Thinking**: strong agentic tool-use — 200–300 sequential tool calls; 93% on τ-Bench Telecom (vendor-cited).
- **K2.6**: ties GPT-5.5 at **58.6% SWE-bench Pro** (a real, comparable number).
- **K2.7-Code**: **no independent SWE-bench** (Verified or Pro). Moonshot published only **proprietary** benchmarks (Kimi Code Bench v2 62.0, Program Bench 53.6, MLS Bench Lite 35.1, MCP Atlas 76.0, MCPMark Verified 81.1). Secondary blogs circulating a "60.4% SWE-bench Verified" figure are **unsubstantiated** (our adversarial pass refuted it).
- **Reference:** Claude Opus 4.8 = 88.6% SWE-bench Verified / 69.2% SWE-bench Pro (independently benchmarked).
- **Practitioner signal:** K2.7 reportedly **goes off-track / over-refactors** vs Claude's tighter instruction-following; smaller context (256K vs ~1M).

## Key takeaways

- Kimi is a **commodity OpenAI-compatible swap** — one `base_url` change. That's the whole integration story.
- **Cost win is real (~5–8× vs Opus, more with caching)**; **capability claims for K2.7-Code are vendor-only and unaudited** — pilot on your eval set, don't trust the blog numbers.
- The **thinking toggle is model-dependent** (works on K2.6, errors on K2.7-Code).
- **API access ≠ consumer subscription** — the "$39 plan" is a consumer tier; API is token-billed from the console.
- Open weights (Modified MIT) mean Kimi can also be **self-hosted** (vLLM) — composes with your [[cowork-third-party-inference/_index]] local-inference thread.

## Cross-links

- [byo-model-openai-compatible](byo-model-openai-compatible.md) — the standard the API speaks
- [[cowork-third-party-inference/_index]] — plug Kimi (or local Ollama) into the Claude harness
- [[claude-api-cost-optimization/_index]] — caching + tiering, now cross-provider
- [[prompt-evaluation/_index]] — the bake-off harness to test Kimi vs Claude honestly
