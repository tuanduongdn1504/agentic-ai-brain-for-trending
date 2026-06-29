# Source provenance & verification log

## Method

- **Primary source:** the video transcript (Vietnamese auto-captions via `yt-dlp --write-auto-subs vi` + `bin/vtt-to-md.py`) — see [raw/2026-06-20-omnilogin-ai-coding.md](../../raw/2026-06-20-omnilogin-ai-coding.md). Title/channel/date/views confirmed via `yt-dlp` metadata.
- **Originals deep-dive + verification:** Workflow `wf_1ac2a814-456` — 6 research facets, each piped through an adversarial verification stage (24 agents, 334 tool calls, ~803K subagent tokens). Risky claims were independently re-checked against primary sources (official docs / pricing pages) with a refute-first stance.

## Tiering

### Tier 1 — primary-source solid (video shows it + docs confirm)
- The AI Coding interface (Script / UI code / Output panes; chat + prompt box). **Shown on screen.**
- BYO-model config fields (provider type / base URL / API key / model / disable-thinking). **Shown on screen + docs.omnilogin.net/en lists providers.**
- The generate → accept → verify → fix → scale workflow. **Shown on screen.**
- Kimi API is **OpenAI-compatible**; base URLs `api.moonshot.ai/v1` (intl) / `api.moonshot.cn/v1` (China). **Official docs.**
- OpenAI Chat Completions as the de-facto BYO-model standard (Ollama/OpenRouter/LiteLLM/Dify). **Official docs/READMEs.**

### Tier 2 — confirmed but vendor-sourced (not independently audited)
- Omnilogin "~95% task coverage," anti-bot bypass claims. **Vendor marketing.**
- Kimi K2.7-Code architecture (1T MoE / 32B active / 256K / ~30% fewer reasoning tokens). **Moonshot.**
- Kimi token pricing (K2.5/K2.6 $0.60/$2.50; K2.7-Code ~$0.95/$4.00; caching ~$0.10–0.16). **Provider/aggregator pages.**

### Tier 3 — corrected or flagged by verification
| Claim | Original status | Corrected to |
|---|---|---|
| "AI Coding is BYO-model" | one agent **refuted** (consumer homepage hides config) | **CONFIRMED** — video shows fields + docs.omnilogin.net/en lists ChatGPT/Claude/Gemini/DeepSeek/Grok/OpenRouter/Custom. Marketing page simplifies. (Rule 7 conflict, resolved toward primary source.) |
| "$39 plan (1 of 4) to use Kimi" | video claim | **CORRECTED** — kimi.com has 5 consumer tiers (free + 4 paid); $39 = Allegretto consumer sub; **API access is separate pay-as-you-go from the platform console** |
| "disable thinking" universally | video claim | **PARTLY** — works on K2.5/K2.6; **K2.7-Code (Jun 2026) errors if disabled** |
| "K2.7-Code 60.4% SWE-bench Verified" | secondary blogs | **REFUTED** — no independent SWE-bench; Moonshot published only proprietary benchmarks |
| "AI writes the complete script" (one-shot) | video framing | **CORRECTED** — ~62% agentic task success; verify-fix loop required |
| "agents generate their own config UI" | facet 5 | **CORRECTED** — they compose from pre-approved component catalogs (A2UI/AG-UI), not arbitrary UI |
| Omnilogin's "GoLogin is trial-only" comparison | Omnilogin blog | **CORRECTED** — GoLogin has a permanent free plan (3 profiles) |
| Ollama "backed by llama-cpp-python" | facet 6 | **CORRECTED** — llama.cpp C/C++ `llama-server` (MLX on Apple Silicon 0.19+); not the Python binding |

### Tier 4 — video-only / unverifiable
- Exact runtime the generated Omnilogin script executes in (Node/Deno/Chromium context) — **docs.omnilogin.net has no dedicated AI Coding technical page (404s)**; uncertain.
- How the generated "UI code" is structured (HTML/React/declarative) — undocumented.
- Whether Allegretto ($39) bundles any API credits — docs ambiguous.
- The presenter's exact Kimi model string at video time (K2.6 inferred from date).

## Conflicts surfaced (Rule 7 — surfaced, not averaged)

1. **BYOM refute vs confirm** → resolved to **confirmed** (primary source = video + docs beats consumer marketing page).
2. **K2.7-Code SWE-bench 60.4% (secondary) vs no-independent-benchmark (verify)** → resolved to **no independent benchmark**; do not cite 60.4%.

## What to NOT repeat from the video

- Don't tell anyone they "need the $39 plan" — API is token-billed separately.
- Don't cite Kimi coding benchmarks as proven — pilot on your own eval set.
- Don't present BYO-model as Kimi-specific — it's universal.
- Don't paste raw provider keys into closed-source apps — use a scoped gateway key.
- Don't replicate the bulk-Gmail-login use case (ToS).

## Cross-links

- [_index](_index.md) · [video-to-original-crosswalk](video-to-original-crosswalk.md) · [overview](overview.md)
