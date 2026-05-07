# Entity 2 — Distribution / Multi-Surface

## 4 client surfaces × 6 backend providers = 24-cell support matrix

### Client surfaces

| # | Surface | How it connects |
|---|---|---|
| 1 | **Claude Code CLI** | Anthropic native; reconfigured via `ANTHROPIC_BASE_URL` env var pointing to local proxy |
| 2 | **VS Code extension** | Inherits CLI config (Claude Code VS Code uses the same env-var protocol) |
| 3 | **JetBrains ACP** | Anthropic Claude Plugin for IntelliJ-family; same env-var redirect mechanism |
| 4 | **Discord + Telegram bots** | Optional chat-bot wrapper with Whisper voice-to-text; bot interfaces with proxy + Claude Code subprocess |

### Backend providers

| # | Provider | Cloud / Local | API protocol |
|---|---|---|---|
| 1 | NVIDIA NIM | Cloud | OpenAI-compatible |
| 2 | OpenRouter | Cloud | OpenAI-compatible (multi-vendor aggregator) |
| 3 | DeepSeek | Cloud | OpenAI-compatible |
| 4 | LM Studio | Local | OpenAI-compatible (localhost) |
| 5 | llama.cpp | Local | OpenAI-compatible (localhost) |
| 6 | Ollama | Local | Ollama-native + OpenAI-compatible shim |

**Distribution Pattern #2 data point:** at T4 bridge tier, 24-cell support matrix is corpus-broadest-at-T4 (claude-context v40 ~12-cell client × 4-embedding × 2-DB; markitdown v28 single-input × multi-output).

## Per-model-tier routing

Claude Code's tier model (Opus / Sonnet / Haiku) maps PER-TIER to user's chosen upstream provider:

```
Opus    → OpenRouter   (for GLM-5 quality)
Sonnet  → DeepSeek     (mid-cost-mid-quality)
Haiku   → Ollama       (free-fast-local)
```

This is **Pattern #28 sub-variant: per-model-tier-routing.** N=1 at v60. Routes within Pattern #28 (consolidation-forward); not standalone candidate.

**Cross-wiki distinction:** Most Pattern #28 multi-provider observations route by USE-CASE (embedding vs. chat) or by USER-PREFERENCE (default vs. fallback). free-claude-code routes by **CLIENT-side model-tier**, which is unique because it requires the proxy to understand Anthropic's tier semantics + map them to upstream provider+model pairs.

## Whisper voice transcription (Pattern #2 surface)

Discord/Telegram bots support voice messages → Whisper transcription → text prompt → Claude Code via proxy. Adds an additional input-modality surface to the distribution matrix.

## Pattern observations

- **Pattern #2 Distribution Evolution** — 4 surfaces × 6 backends = 24-cell matrix at T4 bridge tier
- **Pattern #28 multi-provider per-Claude-tier-routing** sub-variant — N=1
- **Voice-input-surface** — observational; not promotion-tier (not enough corpus N for pattern)

## Cross-references

- Multi-surface T1: claude-howto v32 (CLI + skills) / mattpocock-skills v57 (CLI + skills)
- Multi-surface T2: n8n v56 (CLI + web UI + cloud + Docker) / ruflo v42 (CLI + npm + plugins)
- Multi-surface T4: claude-context v40 (CLI + VS Code + Chrome) / GitNexus v33 (CLI + Cursor)
