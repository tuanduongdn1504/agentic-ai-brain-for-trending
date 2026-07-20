# CLIProxyAPI Lineage & the AI-Gateway Ecosystem

## Source
OmniRoute README Acknowledgments; [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) + `9router` repos; video t7 (Bifrost); t3 (OpenCode); Workflow verdict `cliproxyapi-9router-lineage` (MISLEADING re "inspired by OpenRouter").

## OmniRoute's actual lineage
The anchor repeatedly says OmniRoute is "inspired by OpenRouter" — an **attribution slip** (the ASR mangles "OpenRouter" as "Nouter/Narrator/NRT"). Per the repo's own Acknowledgments:
- **9router** (~22.7K★) — "the original project this fork is built on."
- **[CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI)** (Go, ~43.6K★, MIT, created 2025-07-01) — "the Go implementation that inspired this JavaScript/TypeScript port."

**CLIProxyAPI's purpose:** *"Wrap Antigravity, ChatGPT Codex, Claude Code, Grok Build as an OpenAI/Gemini/Claude/Codex-compatible API… enjoy the free Gemini/GPT/Grok/Claude model through API."* i.e. it turns CLI **subscription OAuth** into a general API — the **Path C** mechanism Anthropic banned. OmniRoute inherits it (one-click `~/.cli-proxy-api/` import). See [[anthropic-oauth-ban-and-tos-risk]].

## The gateway family (how they relate)
"AI gateway" is now a crowded category. The bundle touches several — worth distinguishing because they're conflated:

| Tool | Lang / license | Role | Notes |
|---|---|---|---|
| **OmniRoute** | TS / MIT | multi-provider aggregator + free-tier pooling | subject of this topic; CLIProxyAPI port |
| **CLIProxyAPI** | Go / MIT | subscription-OAuth-as-API proxy | OmniRoute's ancestor; the banned pattern's origin |
| **9router** | — | original fork base | OmniRoute forked it |
| **Bifrost** | Go / Apache-2.0 | fast AI gateway (routing rules) | **t7's** tool (≠ OmniRoute); "~50× faster than LiteLLM" per its own benchmark |
| **LiteLLM** | Python | the well-known gateway baseline | referenced as the thing Bifrost/others out-speed |
| **OpenRouter** | hosted service | provider **marketplace** (you pay, or use its free tier) | what the anchor *meant* — a comparison, not the lineage |
| **OpenCode** | TS / MIT | the **coding agent** (SST/Anomaly) paired with the gateway | ~187K★ (t3 said 160K — understated); model-agnostic terminal agent |

## The shared mechanism (t7 makes it concrete)
Every "free Claude Desktop" setup is the same shape, whichever gateway:
1. Claude Desktop/Code has a feature to point at a **custom endpoint** (for Claude Desktop this is the official **third-party inference** developer mode, built for enterprise Bedrock/Vertex/Foundry).
2. Put a **gateway** in the middle with a routing rule: *"if model name contains 'claude' → send to a free model."*
3. The client still shows "Anthropic Opus 4.8," but a **free non-Claude model** (Nemotron, Gemma, DeepSeek) actually answers — impersonating Claude via a ~7,000-token "you are Claude Code" system prompt.

t7's honest takeaway: you get **Anthropic's front-end feature set** (Cowork, Code, scheduled tasks, artifacts) running **someone else's brain**. Useful, free, and **not Claude**.

## Key Takeaways
- OmniRoute = **CLIProxyAPI (Go) ported to TypeScript** + a 9router fork — **not** "inspired by OpenRouter."
- The ancestor's whole point is **subscription-OAuth-as-API** (the banned pattern); OmniRoute inherits it.
- The category (OmniRoute / Bifrost / LiteLLM / OpenRouter) is easy to conflate; **Bifrost is t7's tool, not OmniRoute**, and **OpenCode is the agent**, not a gateway.
- The universal "free Claude Desktop" trick swaps the engine while keeping Anthropic's cockpit — legal when the engine is your own non-Claude model, banned when it's reused Claude OAuth.
- Related: [[what-omniroute-is]] · [[free-tokens-vs-free-claude-three-paths]] · [[how-it-works-setup-and-clients]]
