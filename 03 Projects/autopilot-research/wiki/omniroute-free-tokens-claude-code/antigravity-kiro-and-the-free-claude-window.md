# AntiGravity, Kiro & the "Free Claude" Window

> How t6 shows "free Claude models," why it's expired/prohibited, and why a July-16 live demo can still appear to work.

## Source
Video **t6** (AI with FZ, "Claude Desktop Is Now FREE?! Use ALL Claude Models"); independent WebSearch on Antigravity Claude removal + Kiro ToS; OmniRoute GitHub discussion #2651; Workflow verdict `all-claude-models-free` (FALSE). Load-bearing date-sensitive claims **main-loop re-verified**.

## What t6 actually demonstrates
t6 pipes **Claude Desktop** → OmniRoute → free tiers, and shows real Claude models by connecting **OAuth providers** that bundle Claude:
- **Google AntiGravity** — "AntiGravity CLI, add connection → your Gmail opens → sign in → connected," then imports **Claude Opus 4.6 / Sonnet 4.6** plus Gemini 3.1 "for free."
- **AWS Kiro (Curo)** — "AWS Builder… you get credits on every new account… all through OAuth," giving Claude Sonnet/Haiku.
- Plus Nvidia, OpenCode free models for the non-Claude fallback.
- t6 also tells viewers to **rotate the API key every 30 days** — a tell that this leans on throwaway/multi-account behaviour.

So the "free Claude" here is **Path B**: proxying *other vendors'* free tiers that resell Claude. It is **not** Anthropic giving away Claude.

## Why it's expired / prohibited
- **AntiGravity removed Claude (~May 2026).** Claude Sonnet/Opus 4.6 were briefly in AntiGravity's model selector, then **"completely disappeared from the Antigravity provider"** (corroborated by OmniRoute discussion #2651 and multiple May-2026 write-ups). As of the video dates (July 16–20) you can only reach Claude in AntiGravity by **adding your own Anthropic API key** — i.e. **not free**. → t6's "free Claude via AntiGravity" is **FALSE/expired**.
- **Kiro prohibits proxies.** Kiro's FAQ **explicitly** bans "use with OpenClaw and similar tools that leverage third-party harnesses," and AWS/Bedrock abuse-detection (with extra checks on the free tier) applies. Kiro's free grant is also **capped** (≈50 credits/month), not unlimited. → Using Kiro through OmniRoute **violates Kiro's ToS**.

## Why a July-16 live demo can still look like it works
Reasonable, non-accusatory explanations for a video that appears to show free Claude *after* the removal:
1. **Pre-removal footage** re-used in a later upload.
2. **Transitional/intermittent availability** while Google wound the integration down.
3. **Stale model listings** — Claude Desktop's model discovery surfaces anything with "Opus/Sonnet/Haiku" in the name; a cached combo name can *appear* even if the upstream 404s.
4. A **different upstream** actually answering behind a Claude-named combo (the t7/Bifrost pattern — a non-Claude model wearing a Claude nametag).

The wiki does **not** claim t6 is deliberately deceptive — only that, verified against current provider status, **its central promise ("ALL Claude models, free, right now") does not hold as of July 2026.**

## The honest sibling (t7 / Bifrost)
t7 ("Claude Desktop Without Anthropic") uses a *different* gateway (**Bifrost**, not OmniRoute) but the same trick — and is refreshingly candid: the free model (Nvidia Nemotron) just **wears a Claude nametag** via a ~7,000-token system prompt. Its money quote: *"the cockpit is the same, the engine is just different… it's NOT Claude Opus."* That is the accurate mental model for **all** "free Claude Desktop" videos. See [[cliproxyapi-lineage-and-the-gateway-ecosystem]].

## Key Takeaways
- t6's "free Claude" = **Path B** (proxying AntiGravity/Kiro free tiers), not Anthropic generosity.
- **AntiGravity's free Claude was removed ~May 2026** (now API-key-only) → the July claim is expired/FALSE.
- **Kiro's ToS prohibits third-party proxy use** → routing it through OmniRoute violates Kiro's terms.
- t7/Bifrost is honest that the "Claude" you get is a **non-Claude model in a Claude UI**.
- Related: [[free-tokens-vs-free-claude-three-paths]] · [[anthropic-oauth-ban-and-tos-risk]] · [[claims-scorecard]]
