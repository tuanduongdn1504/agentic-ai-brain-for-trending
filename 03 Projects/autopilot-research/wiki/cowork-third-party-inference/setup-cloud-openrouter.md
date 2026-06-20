# Setup: cheap cloud models via OpenRouter

The cloud path: add a second third-party configuration for cheap, cloud-hosted models via OpenRouter instead of (or alongside) your local Ollama. This is the faster alternative when your hardware can't run local models, or when you want production-speed inference.

## Source

- **Video:** Bart Slodyczka, "Claude Cowork + Ollama = 100% FREE & PRIVATE (Full Setup)" (YouTube ME4flXK_6tQ, 2026-04-25, 18:41)
- **Transcript:** `/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/(C) 2026-06-20-cowork-ollama-3p-local-private.md` [timestamps 14:07–16:21]
- **First-party docs:** https://claude.com/docs/cowork/3p/gateway, https://openrouter.ai/docs/api/reference/authentication
- **Optional deep-dive articles:** [[cowork-third-party-inference/openrouter-deep-dive]], [[cowork-third-party-inference/skills-mcp-websearch-byom]]

---

## Ritual: add a cloud configuration

The video demonstrates keeping BOTH local (Ollama) and cloud (OpenRouter) configurations in Cowork. You switch between them by selecting different "gateway" profiles in the app.

### Step 1. Add a second gateway profile

In Claude Desktop:

- **Developer > Configure third-party inference**
- Click **Add a new configuration** (if you already have your local Ollama config)
- Name it something like `cloud-models` or `openrouter-demo`
- Select **Gateway** connection type
- Leave the other fields blank for now; you'll fill them next

### Step 2. Get an OpenRouter account + API key

Go to https://openrouter.ai:

- Create a free account (email / Google sign-in)
- Add credits: the video recommends starting with $10 USD minimum to test
- Navigate to **API Keys** section
- Click **Create new key** and give it a name (e.g., `claude-cowork`)
- Copy the generated key (you'll paste this next)

### Step 3. Fill in gateway credentials

Back in Claude Desktop's new configuration:

| Field | Value | Notes |
|---|---|---|
| **Base URL** | `https://openrouter.ai/api/v1` | Must include `/v1` suffix; omitting it causes "not found" errors. The video shows copying a URL from OpenRouter's browser interface and editing it to this form. |
| **API Key** | `<paste your key from step 2>` | The actual credential from OpenRouter. |
| **Auth scheme** | `X-API-Key` | Drop-down selection. Different from Ollama's `bearer` token. |

The video shows copying the base URL from the OpenRouter interface, then editing it to ensure it ends with `/api/v1`.

### Step 4. Disable built-in web_search tool (important!)

Non-Claude models don't have Anthropic's built-in web search tool. If you leave it enabled, the model will fail trying to call a tool that doesn't exist. To avoid this:

- While still in **Configure third-party inference**, navigate to **Sandbox / Workspace**
- Scroll down and find the list of **Built-in tools**
- Toggle **web_search** to **disabled**
- This tells non-Claude models: "don't try to use the built-in web search; fall back to MCP instead (Brave Search)"

The video demonstrates this at [15:00–15:26]. Without this step, you'll see model errors like "tool not found" or "web_search unavailable" when the model tries to search the web.

### Step 5. Apply + relaunch

- Click **Apply locally** (applies to this machine only)
- Relaunch Claude Desktop
- On relaunch, you should now see OpenRouter models in the model picker (e.g., Gemma 4 26B A4B, MiniMax 2.7)

---

## Model selection & availability tiers

OpenRouter surfaces **three tiers** of model availability under your API key:

| Tier | Status | Meaning | Action |
|---|---|---|---|
| **Available** | ✅ Ready to use | Model works on your account. | Pick and use. |
| **Partially available** | ⚠️ Limited access | Model may have rate limits or intermittent availability. | Test before relying on it. |
| **Fully unavailable** | ❌ Cannot use | Model is blocked on your account. Per the video, possible reasons include privacy or region restrictions. | Choose a different model. |

To check availability, go to OpenRouter, log in, click your API key, and scroll down to see the three-tier list. For example, the video shows **GPT-5.5 as unavailable** (grayed out) while **MiniMax 2.7 is available** (usable).

---

## Pricing shape (April 2026 video — verify current rates)

The video quotes example pricing for Gemma 4 26B A4B on OpenRouter:

- **Input tokens:** $0.06 per million tokens
- **Output tokens:** $0.33 per million tokens

⚠️ **Unverified as of June 2026.** The video is dated April 25, 2026; current rates may differ. Verify on https://openrouter.ai/pricing before relying on these figures for cost estimates.

OpenRouter does **not mark up** provider pricing—the rates you see match the upstream provider (Google, in this case) exactly. This contrasts with some aggregators that add overhead.

**Free models exist** on OpenRouter (Gemma 4 26B A4B has a free tier) but are subject to:
- 20 requests/minute rate limit
- 50 free requests/day (without $10+ credits) or 1000/day (with credits)
- No SLA (availability not guaranteed)

The video notes the free tier is "hit and miss."

---

## Privacy / data handling warning

The video includes an explicit caveat at [00:55]:

> "If you are going to use OpenRouter, I would assume that any information you share it's going to be collected and used in some way."

Clarification:
- **OpenRouter itself** does not log or train on your prompts by default (zero-logging policy, first-party verified).
- **Underlying providers** (Google for Gemma, etc.) maintain separate data retention policies independent of OpenRouter. Your data goes to them, not to OpenRouter as an intermediary.
- Use OpenRouter's **Zero Data Retention (ZDR)** control to route only to privacy-compliant providers if sensitive data is involved.

This differs from the [[cowork-third-party-inference/setup-local-ollama]] path, which is 100% private (data stays on your machine via Tailscale).

---

## Key Takeaways

- **Two configurations are better than one.** Keep local (Ollama, 100% private) and cloud (OpenRouter, faster) configs side-by-side; switch between them with a model picker, don't delete the local one.
- **OpenRouter base URL must include `/v1` suffix.** Common mistake: copy `https://openrouter.ai/api` without the `/v1/`; include it or the API calls fail with "not found."
- **Disable built-in web_search in Sandbox settings** or non-Claude models will crash trying to call a tool that doesn't exist.
- **Auth scheme is X-API-Key, not bearer.** Different from Ollama's token style (per the video).
- **Model availability is tiered.** Some models on OpenRouter are fully unavailable on your account. Possible reasons: privacy, region, or account restrictions (per the video). Check the tier list before assuming a model works.
- **Assume data is handled by the underlying provider.** If using Gemma, Google sees it. Use ZDR controls if your data is sensitive.
- **Speed trade-off: cloud > local.** OpenRouter models run in the cloud and are faster than local Ollama inference, at the cost of privacy and per-token cost.
- **Skills struggle on non-Claude models.** Even on OpenRouter, MiniMax and Gemma lack training on the Claude Desktop harness. Workaround: run the skill once, let it fail, ask the model to fix itself, then re-run (per the video [17:18–18:14]).

---

## Cross-links

- [[cowork-third-party-inference/overview]] — the full 3P feature positioning + harness-model separation thesis
- [[cowork-third-party-inference/setup-local-ollama]] — the private alternative (Ollama on your machine)
- [[cowork-third-party-inference/openrouter-deep-dive]] — pricing, provider ecosystem, ZDR + data policies
- [[cowork-third-party-inference/skills-mcp-websearch-byom]] — how to wire Brave Search MCP when your model lacks web search
- [[claude-cowork/_index]] — parent topic; overview of Cowork features + scheduled tasks + dispatch button differences
- [[claude-api-cost-optimization/_index]] — cost levers; 3P inference is the most extreme cost reduction ($0 local, $0.06M input cloud)
- [[harness-engineering/_index]] — the conceptual thesis: harness (desktop app) separable from model (inference provider)
