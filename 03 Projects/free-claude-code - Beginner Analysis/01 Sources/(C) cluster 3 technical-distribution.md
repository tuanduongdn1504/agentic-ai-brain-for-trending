# Cluster 3 — Technical / distribution / integrations

## Architecture stack

- **Language:** Python 3.14
- **Web framework:** FastAPI (HTTP server)
- **Default port:** 8082 (Anthropic-API-compatible endpoint)
- **Package manager:** uv (Astral; modern Python ecosystem)
- **Code quality:** Ruff (formatter + linter), Ty (type-checker), Pytest, Loguru (logging)
- **ASGI factory:** `api.app:create_app` (production-deployable)

## 6 backend providers

| Provider | Type | API protocol consumed |
|---|---|---|
| **NVIDIA NIM** | Cloud (NVIDIA-hosted) | OpenAI-compatible |
| **OpenRouter** | Cloud (multi-vendor aggregator) | OpenAI-compatible |
| **DeepSeek** | Cloud (DeepSeek-hosted) | OpenAI-compatible |
| **LM Studio** | Local (desktop runtime) | OpenAI-compatible localhost |
| **llama.cpp** | Local (binary inference) | OpenAI-compatible localhost |
| **Ollama** | Local (model server) | Ollama native + OpenAI-compatible shim |

**Pattern #28 strengthening:** 6 providers + per-tier routing. Compared to corpus distribution:
- aidevops v47: 4 providers
- claude-context v40: 4 embedding providers + 2 vector DBs
- ruflo v42: 6+ providers (similar count)
- n8n v56: 16 native LLM providers (corpus-broadest at T2)
- OpenSpec v58: 30+ AI tools (Pattern #18 Layer 1 strongest at T1)

free-claude-code = 6 providers at T4 = MEDIUM-broad provider count for T4.

## Per-model-tier routing (corpus-distinctive)

Claude Code's tier model (Opus / Sonnet / Haiku) maps to user's choice of upstream provider PER TIER:
- Opus → expensive-but-capable (e.g., OpenRouter routed to GLM-5)
- Sonnet → mid-tier (e.g., DeepSeek)
- Haiku → cheap-fast (e.g., Ollama local llama.cpp model)

**Pattern #28 sub-variant: per-model-tier-routing.** N=1 at v60. Strengthens within-pattern; not standalone candidate (consolidation-forward).

## 4 client surfaces (Pattern #2 Distribution)

1. **Claude Code CLI** (Anthropic native CLI, runs against `ANTHROPIC_BASE_URL` proxy)
2. **VS Code extension** (via Claude Code's VS Code support)
3. **JetBrains ACP** (Anthropic Claude Plugin for IntelliJ-family IDEs)
4. **Discord + Telegram bots** (chat-platform clients, with optional Whisper voice transcription)

**4 client surfaces + 6 backend providers** = 24-cell support matrix. Pattern #2 Distribution Evolution corpus data point at T4.

## Comparison to T4 peers

| Subject | T4 sub-archetype | Bridge function |
|---|---|---|
| graphify v16 | code-graph-search | Code → graph index |
| markitdown v28 | doc-conversion | Doc formats → Markdown |
| GitNexus v33 | code-graph-indexing | Repo → searchable graph |
| claude-context v40 | code-vector-search | Code → embedding index |
| **free-claude-code v60** | **api-protocol-translation-proxy** | **Anthropic API ↔ 6 upstream provider APIs** |

**T4 sub-archetype #9 NEW: api-protocol-translation-proxy.** Distinct mechanism from prior 8 T4 entrants (all are content-transformation bridges; free-claude-code is protocol-translation bridge for ALREADY-EXISTING agent client).

## Cluster-level corpus-first observations

| # | Observation | Cross-wiki implication |
|---|---|---|
| 1 | api-protocol-translation-proxy at T4 — corpus-first | T4 9th archetype; route within Pattern #18 Layer 2 (corpus runtime translation layer) |
| 2 | 6 providers + per-tier routing | Pattern #28 strengthening + per-tier-routing sub-variant |
| 3 | 4 client surfaces × 6 backends = 24-cell support matrix | Pattern #2 Distribution data point |
| 4 | Python 100% at T4 | Pattern primary-language T4: Python (vs JS/TS at most T1+T2) |
| 5 | uv + Python 3.14 (bleeding-edge Python) | Pattern #2 Packaging-tooling — uv at T4; modern toolchain |
| 6 | FastAPI + ASGI factory pattern | Standard Python web microservice; not corpus-distinctive |
| 7 | OpenAI-compatible API as upstream-default-protocol (5 of 6 providers) | **Cross-wiki standard observation: OpenAI-API-format-as-de-facto-LLM-protocol** at T4; aligns with broader corpus pattern that OpenAI API spec is the lingua franca for non-Anthropic LLMs |

## Notable absence

- No MCP server exposed by free-claude-code — it's an Anthropic-API-compatible HTTP server, not an MCP tool. Pattern #18 Layer 1 NOT extended at v60.
- No skill / agent / hook collection — pure proxy. Pattern #69 NOT extended.

## Verbatim short quote (≤15 words)

> "drop-in proxy for Claude Code's Anthropic API calls"

(README; positions free-claude-code as protocol-translation utility, not opinionated agent.)
