# Deep-dive: OpenRouter as a cloud model gateway

OpenRouter is a **multi-provider LLM aggregator** offering 400+ models from 70+ providers via a unified API gateway. It enables Anthropic Cowork on 3P and Claude Code to access dozens of models (Gemma, Llama, Mistral, etc.) at provider cost without markup, with zero-knowledge retention controls for sensitive deployments.

## What OpenRouter is (role in the 3P ecosystem)

OpenRouter operates as an **API intermediary** between Claude Desktop (via Cowork on 3P) and underlying model providers. Instead of managing separate API accounts with 70 providers, you authenticate once to OpenRouter and route requests through its unified gateway.

- **API base URL:** `https://openrouter.ai/api/v1` (Anthropic Messages API compatible)
- **Auth:** Bearer token authentication via `Authorization: Bearer <API_KEY>` header (first-party standard; note: Cowork UI dropdown may show "X-API-Key" option but Bearer is documented default)
- **Protocol:** Implements OpenAI-compatible and Anthropic-compatible message protocols; Cowork on 3P uses the Anthropic Messages API variant with streaming + tool use support
- **Model library:** 400+ models from ~70 providers; auto-discovers model availability per your account's credential scope
- **Availability tiers:** Available / Partially Available / Fully Unavailable per model per account

The video describes setting up OpenRouter as a "cloud demo" secondary gateway alongside a local Ollama instance, each stored as a separate "configuration" in Cowork on 3P.

## Pricing model: provider cost pass-through

OpenRouter implements **zero-markup** pricing: posted rates match provider websites exactly.

Example from the video (April 2026, unverified current rates):
- **Gemma 4 26B A4B (paid tier):** $0.06 per million input tokens, $0.33 per million output tokens
- **Gemma 4 26B A4B (free tier):** $0.00 input, $0.00 output (subject to rate limits)

**Caveat:** These prices are from April 2026 and may have shifted. Verify current pricing directly on openrouter.ai before budgeting.

### Rate limits & free-tier behavior

The video claims free models are "hit and miss" with "no SLA." First-party OpenRouter docs confirm:
- **Free tier rate limits:** 20 requests/minute, 50 free requests/day (without 10+ credits); 1,000/day (with 10+ credits)
- **No service-level agreement** for free models; reliability not guaranteed
- **Recommendation:** Start with $10 credits; cost/token is negligible for learning setups

## Authentication & configuration in Cowork on 3P

The video walks through the setup flow:

1. Create OpenRouter account at `openrouter.ai`
2. Add credits (recommend $10 minimum)
3. Generate API key from account settings
4. In Cowork on 3P: **Developer > Configure third-party inference > Add configuration**
5. Fill in:
   - **Base URL:** `https://openrouter.ai/api/v1`
   - **API Key:** your OpenRouter API key
   - **Auth scheme:** Bearer token (default per first-party docs; the video's UI shows "X-API-Key" dropdown but Bearer is the documented standard)

**Note:** The video shows the speaker initially entering `https://openrouter.ai/api` then correcting to add `/v1` — the `/v1` suffix is required per first-party docs.

## Data privacy & retention policy

This is the **hinge decision** for using OpenRouter with sensitive data.

### OpenRouter's own data handling

OpenRouter itself **logs zero prompts/completions by default**. From first-party docs:
- No training on user data unless you opt-in for a 1% cost discount (not recommended for sensitive data)
- No data retained after request completes
- Logs are audit-only (request count + token count, no payload)

The video explicitly warns: "I would assume that any information you share [with OpenRouter] is going to be collected and used in some way." This is a **speaker-anecdote privacy-conscious framing** — technically OpenRouter itself doesn't retain data, but the video suggests assuming the worst-case.

### Upstream provider policies

**Critical:** OpenRouter does not control upstream provider data policies. When you use a model on OpenRouter (e.g., Gemma via Google, Llama via Meta), that provider's separate data policy applies.

Examples:
- **Google Gemma:** Google's data policies apply; Gemma models may be used for model improvement unless you configure otherwise
- **Other providers:** Vary widely; some promise ZDR, others train on data by default

### Zero Data Retention (ZDR) controls

OpenRouter provides **ZDR mode** to restrict routing to privacy-compliant provider endpoints only:
- Available per-account, per-model-group, or per-request
- OpenRouter maintains `/api/v1/endpoints/zdr` endpoint (auto-updated when provider policies change)
- **Use case:** If you're processing PII or proprietary data, enable ZDR to route only to providers with explicit zero-retention SLAs

The video does NOT mention ZDR (feature may have existed but wasn't highlighted in April 2026). By June 2026, ZDR is a critical control for any sensitive data use.

## Model availability tiers & privacy-standards filtering

The video shows OpenRouter's model listing with three tiers:

1. **Available** — your API key can access this model
2. **Partially Available** — restricted or experimental access
3. **Fully Unavailable** — cannot access via your account

The video speculates: "For fully unavailable models, one reason might be if that model doesn't meet some privacy standards that OpenRouter sets."

**Verification:** OpenRouter documentation does not explicitly confirm this privacy-standards interpretation. The unavailability likely reflects:
- Provider integration status (incomplete API wiring)
- Geolocation restrictions
- API key tier limitations
- Provider request (withdrawn from marketplace)
- Privacy policy non-compliance (video's interpretation, but unverified in first-party docs)

**Honest assessment:** The video's interpretation is plausible but not documented. Use ZDR controls if privacy is the constraint, rather than relying on availability-tier interpretation.

## Available model categories (as of video date)

The video references:
- **Gemma 26B** (Google; video claims 18GB with 256K context — unverified against Google Gemma docs)
- **Gemma 4 26B A4B** (specific Gemma variant)
- **MiniMax 2.7** (demonstrated in cloud demo)
- **GPT-5.5** (unavailable, used as example)

Video does NOT provide a complete list. Actual available models depend on:
1. Your account age / credit history
2. API key tier (free vs paid)
3. Provider enablement at OpenRouter (varies monthly)

**Always check openrouter.ai directly for current model roster.**

## Limitations & gotchas

### Non-Claude models lack Cowork harness training

The video demonstrates that cloud models (MiniMax 2.7) struggle with Cowork skills because they "are not trained on the Claude desktop app harness." When executing a skill (e.g., create a Word document), non-Claude models get stuck in retry loops.

Workaround shown: run the skill once, inspect failure, ask the model to fix itself, then re-run. This is labor-intensive compared to paid Cowork with Opus/Sonnet. The video's framing is that non-Claude models lack "training" on the harness; more precisely, they lack the deployment-time system prompting Anthropic bakes into Claude models.

### No built-in web search

Non-Claude models on OpenRouter do not natively support Anthropic's `web_search` tool. To restore web search:
- Configure a Brave Search MCP server (as of June 2026, independently maintained at github.com/brave/brave-search-mcp-server, though video references modelcontextprotocol/servers)
- Disable the built-in `web_search` tool in Cowork Sandbox settings so the model routes to Brave instead of failing

### Dispatch button unavailable

Cowork on 3P (with any 3P model) lacks the "Dispatch" button, preventing one-click task delegation. This is a first-party limitation, not OpenRouter-specific.

## Comparison: local Ollama vs. cloud OpenRouter

The video demonstrates both in parallel:

| Dimension | Local Ollama | OpenRouter Cloud |
|---|---|---|
| **Speed** | Slower (depends on your hardware) | Faster (cloud inference) |
| **Privacy** | 100% (traffic stays in tailnet via Tailscale) | None (data leaves machine; OpenRouter + provider see it) |
| **Cost** | $0 | $0.06–$0.33 per million tokens (Gemma 26B, April 2026; verify current) |
| **Reliability** | Limited to your machine's uptime | Better (managed cloud service) |
| **Model choice** | Limited (what fits your hardware) | 400+ models |
| **Skill execution** | Same struggles as cloud models | Same struggles as local models |

## Ollama native integration evolution

**Important:** The video uses Tailscale to bridge Ollama's HTTP API to HTTPS (required by Anthropic's gateway). However, Ollama v0.14.0 (released January 2026, ~3 months before the April video) added **native Anthropic Messages API support**, potentially eliminating the Tailscale bridge for local setups.

The current recommended path (post-April 2026):
```bash
ollama launch claude-desktop
```

This reportedly wires Claude Desktop directly to Ollama without requiring an HTTPS bridge. The video predates or doesn't reference this simpler integration path, suggesting the Tailscale approach is legacy but still valid.

## First-party docs

- **OpenRouter:** https://openrouter.ai/docs/api/reference/authentication, https://openrouter.ai/docs/guides/features/zdr
- **Cowork on 3P:** https://claude.com/docs/cowork/3p/gateway
- **Ollama (native integration):** https://ollama.com/blog (January 2026 Anthropic API post)

## Key Takeaways

- OpenRouter is a **no-markup API aggregator** for 400+ models from 70+ providers; pricing reflects upstream provider cost
- **Authentication:** Bearer token to `https://openrouter.ai/api/v1` (note: Cowork UI may show X-API-Key option, but Bearer is documented standard)
- **Privacy posture:** OpenRouter itself doesn't retain data; upstream providers' policies vary. Use **Zero Data Retention (ZDR) mode** for sensitive data
- **Model availability tiers** (Available/Partially/Unavailable) may reflect privacy-standard filtering, but this is unconfirmed per first-party docs; verify before relying on tier for compliance
- **Free models** are rate-limited and unreliable; start with $10 credits
- **Non-Claude models** lack Cowork harness training, causing skill failures; workaround = run-fail-fix-rerun loop
- **Web search** requires manual Brave Search MCP configuration (now at github.com/brave/brave-search-mcp-server); built-in tool must be disabled to prevent failures
- **Ollama v0.14.0+** (Jan 2026) offers native Anthropic API support, making the Tailscale HTTPS bridge optional for local setups
- **No Dispatch button** in Cowork on 3P (any provider) — first-party limitation

## Related articles

- [[cowork-third-party-inference/overview]] — Cowork on 3P ecosystem overview
- [[cowork-third-party-inference/setup-cloud-openrouter]] — Step-by-step setup walkthrough
- [[cowork-third-party-inference/setup-local-ollama]] — Ollama local setup (including Tailscale bridge)
- [[cowork-third-party-inference/gateway-protocol-deep-dive]] — Anthropic gateway API protocol + Messages API compatibility
- [[claude-cowork/_index]] — Parent Cowork topic; Cowork on 3P is BYOM extension
- [[claude-api-cost-optimization/_index]] — Cloud model cost levers; OpenRouter pricing is extreme end of cost-cut spectrum
- [[harness-engineering/_index]] — Harness-model decoupling thesis; this feature IS that thesis first-party

## Source

**Video transcript:** `/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/(C) 2026-06-20-cowork-ollama-3p-local-private.md`
- Bart Slodyczka, "Claude Cowork + Ollama = 100% FREE & PRIVATE (Full Setup)"
- YouTube: https://youtu.be/ME4flXK_6tQ
- Published: 2026-04-25, 18:41, ~47K views

**First-party docs consulted:**
- https://openrouter.ai/docs/api/reference/authentication
- https://openrouter.ai/docs/guides/features/zdr
- https://openrouter.ai/docs/guides/overview/models
- https://claude.com/docs/cowork/3p/gateway
- https://ollama.com/blog (January 16, 2026: Anthropic Messages API support announcement)
