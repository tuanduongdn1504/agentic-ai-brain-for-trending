# Entity 1 — Core Product: Drop-in Anthropic-API Proxy

## Identity

**free-claude-code** is a **drop-in proxy server** that intercepts Claude Code's outbound Anthropic Messages API requests and routes them to one of 6 alternative model backends. It runs locally on port 8082 and Claude Code is reconfigured (via env vars `ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN`) to talk to it instead of `api.anthropic.com`.

## What it does

1. **Receives Anthropic-formatted Messages API calls** (streaming or non-streaming, with tool-use, with system prompts) from Claude Code clients (CLI, VS Code, JetBrains, chat bot wrappers).
2. **Translates each request** to the upstream provider's API format (OpenAI-compatible for 5 of 6 providers; Ollama-native for Ollama).
3. **Selects the right upstream model** based on:
   - The Claude tier requested (Opus / Sonnet / Haiku)
   - The configured per-tier routing rule (each Claude tier can map to a different provider)
4. **Streams the response back** to Claude Code in Anthropic format, preserving tool-use semantics.
5. **Optionally wraps the proxy** in a chat-bot interface (Discord / Telegram) with voice transcription via Whisper.

## Why it exists

Cost reduction + model experimentation + infrastructure control. Stated stack-implicit goals:
- Use cheaper non-Anthropic models for non-critical agentic work
- Route specific tiers to specific providers (e.g., Opus to OpenRouter for capability + Haiku to local Ollama for cost)
- Operate entirely offline with local runtimes (LM Studio / llama.cpp / Ollama)

## Architecture

Per PLAN.md:
```
config → providers → api
                ↑
        core.anthropic (neutral foundation)
```

5 domains:
- **api/** — HTTP routes + request orchestration + model routing
- **providers/** — 6 upstream adapters
- **messaging/** — Discord/Telegram bot integration
- **cli/** — Claude Code subprocess management
- **config/** — env-driven settings + logging

Architectural-discipline-via-encoded-rules: PLAN.md explicitly enumerates import boundaries (e.g., `api/` may only import `providers.base / providers.exceptions / providers.registry`).

## Tech stack

Python 3.14 / uv / FastAPI / Pytest / Ruff / Ty / Loguru. ASGI factory pattern (`api.app:create_app`). 5 mandatory CI checks (format / lint / type-check / unit-test / smoke-test).

## Pattern observations

- **Pattern #28 Multi-Provider** — 6 providers (3 cloud + 3 local) + per-Claude-tier routing
- **Pattern #18 Layer 2** — recognizes OpenClaw runtime standard via tagline citation
- **Pattern #57 57c forward-citation** — POSITIVE-COMPARISON-PARALLEL polarity sub-variant (NEW; sister to anti-pattern-foil at v57+v58)
- **Pattern #2 Distribution Surfaces** — 4 client surfaces × 6 backends = 24-cell matrix
- **Pattern #22 22c** — AGENTS.md identical-to-CLAUDE-with-explicit-sync-comment (corpus-first variant)
- **Pattern #19 archetype 4** — first-mover-no-methodology-citation utility-tool sub-variant (sister to v59 AutoGPT corpus-historical-foundational)

## Cross-references

- **Multi-provider siblings:** aidevops v47 / claude-context v40 / ruflo v42 / n8n v56 / OpenSpec v58
- **Claude-Code-adjacent siblings:** claude-howto v32 (T1) / claude-hud v35 (T1) / claude-code-best-practice v34 (T3) / claude-context v40 (T4) / awesome-claude-skills v50 / mattpocock-skills v57
- **OpenClaw cross-references** (in-corpus runtime standard cited by tagline): codymaster v12 / paperclip v14 / multica v15 / graphify v16 / agency-agents v18 / OMC v27 / oh-my-openagent v52
- **T4 sibling archetypes:** graphify v16 / markitdown v28 / GitNexus v33 / claude-context v40

## Verbatim short quote (≤15 words)

> "drop-in proxy for Claude Code's Anthropic API calls"

(README; defines the bridging function.)
