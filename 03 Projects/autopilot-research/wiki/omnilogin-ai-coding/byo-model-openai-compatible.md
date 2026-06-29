# Original #4 — The BYO-model / OpenAI-compatible config pattern

## Source

OpenAI Python SDK docs (base_url override), Ollama OpenAI-compatibility docs, LiteLLM (130+ providers), Dify, Vercel AI SDK, Supabase key-security guidance. Workflow `wf_1ac2a814-456` facet 6 + verifications.

## Why every app now has the same four fields

The video's model-config screen (`provider type / base URL / API key / model name` + a thinking toggle) isn't an Omnilogin invention — it's the **industry-standard BYO-model form**, and it exists because the **OpenAI Chat Completions API became the de-facto wire format**. Once dozens of providers implement `POST /v1/chat/completions`, an app only needs three things to talk to *any* of them:

- **Base URL** — which endpoint (`api.moonshot.ai/v1`, `openrouter.ai/api/v1`, `localhost:11434/v1`, …)
- **API key** — auth
- **Model name** — which model to route to

Change the three strings, talk to a different brain. No code change. That's the entire value proposition.

## Who speaks OpenAI-compatible (confirmed)

- **Kimi / Moonshot** — `api.moonshot.ai/v1` (this video)
- **Ollama** — `localhost:11434/v1` (local, free, private). On Apple Silicon (0.19+) it runs the **MLX** backend; elsewhere **llama.cpp** — the OpenAI endpoint is implemented at the C/C++ `llama-server` level.
- **OpenRouter** — `openrouter.ai/api/v1` — one key, **hundreds of models**, cost routing
- **LiteLLM** — a gateway standardizing **130+ providers** (OpenAI, Anthropic, Bedrock, Azure, Mistral, Cohere, Ollama, OpenRouter…) behind the OpenAI format
- **Dify, Vercel AI SDK, LocalAI, LM Studio** — all expose the same `base URL + key + model` plumbing
- ⚠️ **Anthropic's own SDK does *not* natively accept an OpenAI `base_url` override** for arbitrary endpoints — Claude is reached via the Anthropic Messages API (or a gateway that translates). This is exactly the [[cowork-third-party-inference/_index]] "gateway implements the Messages API" story, in reverse.

## The two strategic uses

1. **Cost arbitrage** — route the same call to the cheapest acceptable model (Kimi, a cheap OpenRouter model, or local Ollama) without rewriting the app.
2. **Privacy / sovereignty** — point `base_url` at **local Ollama** so keys *and* data never leave the machine. (For hireui candidate-PII, this is the load-bearing option — see [[cowork-third-party-inference/_index]].)

## The security angle (the one real risk in the video)

The video casually pastes a Kimi API key into a **closed-source desktop app**. Handing any third-party app your model API key means:

- **Full account access + spending authority** on that key (it can run *any* model call and bill you).
- The app can **read every prompt/response** that flows through it.

Best practice (verified): **per-component keys** (a dedicated key for each app, not your master key), **env-based secret storage**, **immediate rotation on compromise** (deletion is irreversible), and **prefer a gateway you control** (OpenRouter with a scoped key, or your own LiteLLM) over pasting a raw provider key into someone else's binary.

## Key takeaways

- `base URL + key + model` is the **universal swap interface** — the video's config screen is generic, not special.
- The OpenAI Chat Completions format is the **lingua franca**; LiteLLM/OpenRouter exist to make even non-compatible providers fit it.
- **Claude is the exception** — reached via the Messages API / a translating gateway, not a raw OpenAI `base_url`.
- **Don't paste raw provider keys into closed apps** — use a scoped gateway key; rotate; store in env. This is the single anti-pattern to *not* copy from the video.

## Cross-links

- [kimi-moonshot-deep-dive](kimi-moonshot-deep-dive.md) — the provider behind the base URL here
- [[cowork-third-party-inference/_index]] — first-party version: swap the *model* under the Claude *harness* (Ollama / OpenRouter / gateway)
- [[claude-api-cost-optimization/_index]] — the cost lever this enables
- [[self-hosted-devops-oss/_index]] — own-your-keys / secrets-management ethos (Infisical)
