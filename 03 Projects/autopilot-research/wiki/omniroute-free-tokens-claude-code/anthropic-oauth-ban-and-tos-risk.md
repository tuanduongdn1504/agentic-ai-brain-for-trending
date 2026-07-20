# Anthropic's OAuth Ban & the ToS/Account-Ban Risk

> The critical context **every video omits**. If you take one thing from this topic: routing a Claude *subscription* through a third-party gateway to get "free Claude" is banned and can get your account terminated.

## Source
Independent WebSearch (The Register, VentureBeat, MLQ, engineerscodex, KERSAI, autonomee) + ground-truth; Workflow verdicts across `all-claude-models-free`, `cliproxyapi-lineage`, `privacy-data-residency`, `replaces-openrouter`. Note: the dedicated `anthropic-tos-ban-risk` verifier returned empty — this article is main-loop (Opus) verified. See [[caveats-and-corrections]].

## The policy (Feb 2026)
- Anthropic's **Feb 19, 2026** Legal/Compliance update states that **OAuth tokens** obtained through **Free / Pro / Max** plans are intended **exclusively** for **Claude Code** and **claude.ai**.
- Using those consumer OAuth tokens in **any other product, tool, or service** — including the Agent SDK — is **not permitted** and **violates the Consumer Terms of Service**.

## The enforcement (Jan 2026)
- Anthropic **actively blocked** the consumer OAuth tokens of third-party harnesses that had reverse-engineered the login flow: **OpenClaw** (ex-Clawdbot), **OpenCode**, **Roo Code**, and **Goose**.
- Anthropic said it "**tightened safeguards against spoofing the Claude Code harness**."
- **What was banned specifically:** tools that intercept the OAuth flow, extract the access token, and call the API while **pretending to be Claude Code** — which had let users get Claude ~**5–10× cheaper** than pay-as-you-go.

## What is still allowed vs banned

| Allowed ✅ | Banned 🚫 |
|---|---|
| Running the real `claude` CLI binary anywhere (local / VPS / CI): `claude -p` | Extracting a subscription OAuth token into a third-party API client |
| Pointing Claude Desktop at your **own** endpoint via the official **third-party-inference** developer feature (built for enterprise Bedrock/Vertex/Foundry) | Re-exposing a Claude subscription as a general API through a gateway |
| Routing a **paid Anthropic API key** through a gateway | Using OpenClaw/CLIProxyAPI-style OAuth spoofing to get discounted/free Claude |

## Where OmniRoute sits
- OmniRoute is a **TypeScript port of CLIProxyAPI**, whose core feature is precisely the banned pattern (wrap CLI subscription OAuth as an API). OmniRoute ships **one-click import from `~/.cli-proxy-api/`**, so the capability is inherited and present.
- **Most of the bundle stays in Path A** (free non-Claude models) — which does *not* trip this ban. But the tool makes **Path C** (subscription-OAuth reuse) easy, and the "free Claude" framing nudges users toward it **without any disclosure of the ban**.
- Note the honest nuance (from t7, the Bifrost video): using Claude Desktop's *official* third-party-inference feature to point at your **own** gateway running a **non-Claude** model is **not** an Anthropic ToS violation — because no Anthropic model or token is involved. You get the Claude Desktop *UI* running, e.g., Nemotron wearing a "Claude Opus 4.8" nametag. That's legal but it isn't Claude. See [[cliproxyapi-lineage-and-the-gateway-ecosystem]].

## Risk if you ignore this
1. **Account suspension / permanent ban** if you re-expose Claude subscription OAuth (Path C).
2. **ToS violations of *other* vendors** (Google Antigravity, AWS Kiro) if you use their free tiers as a "free Claude" source through a proxy (Path B — see [[antigravity-kiro-and-the-free-claude-window]]).
3. **False expectation:** believing you're getting "free Claude" when the working free path only gives non-Claude models.

## Key Takeaways
- Anthropic **banned** consumer-OAuth reuse in third-party tools (policy Feb 2026; enforcement Jan 2026 vs OpenClaw/OpenCode/Roo/Goose).
- Allowed: the real `claude` CLI, a **paid API key**, or Claude Desktop pointed at your own **non-Claude** gateway via the official feature. Banned: extracting a subscription token into a gateway.
- OmniRoute **inherits** the banned capability (CLIProxyAPI lineage); the videos never disclose the ban.
- **Do not run Path C against a real Anthropic account.** Related: [[free-tokens-vs-free-claude-three-paths]] · [[hireui-relevance]]
