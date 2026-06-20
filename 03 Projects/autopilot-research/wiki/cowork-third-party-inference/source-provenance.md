# Source provenance — Cowork on 3P (third-party inference) verification log

> Same role as the `source-provenance` articles in sibling topics [[multi-agent-orchestration/source-provenance]] + [[agentic-analytics-harness/source-provenance]]: an honest ledger of what is first-party-verified, what is the speaker's interpretation, and what was corrected or stripped during verification.

## Source

- **Primary video:** Bart Slodyczka, "Claude Cowork + Ollama = 100% FREE & PRIVATE (Full Setup)" — [ME4flXK_6tQ](https://www.youtube.com/watch?v=ME4flXK_6tQ), 2026-04-25, 18:41, ~47K views.
- **Transcript:** `raw/(C) 2026-06-20-cowork-ollama-3p-local-private.md` (yt-dlp `en` auto-subs, deduped, read in full).
- **Original resources deep-dived:** Anthropic Cowork-on-3P gateway docs ([claude.com/docs/cowork/3p/gateway](https://claude.com/docs/cowork/3p/gateway)) · [Ollama docs](https://docs.ollama.com) + [v0.14.0 release](https://github.com/ollama/ollama/releases/tag/v0.14.0) · [OpenRouter docs](https://openrouter.ai/docs) · [Tailscale Serve](https://tailscale.com/kb/1312/serve) · [Brave Search MCP](https://github.com/brave/brave-search-mcp-server) · [anthropics/skills](https://github.com/anthropics/skills).

## Verification method

- yt-dlp transcript pulled + read in full (no fabrication of what the video says).
- 6 parallel original-resource research agents (gateway / Ollama / OpenRouter / Tailscale / skills-MCP / ecosystem-evolution), each tiering every fact `first-party` / `secondary` / `speaker-anecdote` / `unverified`.
- Per-article adversarial verify pass (Workflow `wf_4de40f38-856`, 28 agents) — each draft fact-checked against the transcript + first-party docs before publish.
- **Fail-loud note:** two synthesis agents (provenance + the pilot critic) initially returned *meta-descriptions of their work instead of the work itself*; both were recovered/regenerated from the underlying structured data rather than shipped. This article and the pilot menu are the corrected versions.

## First-party verified (load-bearing)

The feature and protocol are real and officially documented:

- **Feature + enable flow:** "Cowork on 3P" is Anthropic-official. Enable via **Help → Troubleshooting → Enable Developer Mode**, then **Developer → Configure third-party inference → Gateway (Anthropic-compatible)**. [docs](https://claude.com/docs/cowork/3p/gateway)
- **Protocol contract:** the gateway must implement the **Anthropic Messages API** — `POST /v1/messages` (streaming + tool use), optional `GET /v1/models` for auto-discovery. Config keys: `inferenceGatewayBaseUrl`, `inferenceGatewayApiKey`, `inferenceGatewayAuthScheme` (bearer | x-api-key), `inferenceModels` (optional override), `inferenceCustomHeaders`. Auto-discovery only surfaces models with recognizably-Claude IDs → set `inferenceModels` for opaque aliases (Gemma/Llama). [docs](https://claude.com/docs/cowork/3p/gateway)
- **Deployment:** **Apply locally** (single machine) vs **Export as MDM profile** (`.mobileconfig` macOS, `.reg` Windows) for fleet rollout — confirms the enterprise BYOM angle. [docs](https://claude.com/docs/cowork/3p/gateway)
- **Privacy boundary (the hinge):** Anthropic docs state *"Data handling is otherwise determined by the gateway you operate and the upstream provider it routes to."* So "private" is only true if your gateway routes to a private model. [docs](https://claude.com/docs/cowork/3p/gateway)
- **Ollama:** port `11434`, HTTP by default; **native Anthropic Messages API since v0.14.0 (2026-01-10)** — predates the video. Claude Code integration uses `ANTHROPIC_BASE_URL=http://localhost:11434` (+ `ANTHROPIC_AUTH_TOKEN=ollama`). [release](https://github.com/ollama/ollama/releases/tag/v0.14.0) · [Ollama×Claude Code](https://docs.ollama.com/integrations/claude-code)
- **OpenRouter:** base URL `https://openrouter.ai/api/v1` (the `/v1` is required); aggregator over 400+ models; **zero-logging by default, no training on user data unless opted-in**; **ZDR controls** (account / model-group / per-request) with a live ZDR-endpoint list. Free tier ≈ 20 req/min, 50–1000 free req/day. [faq](https://openrouter.ai/docs/faq) · [zdr](https://openrouter.ai/docs/guides/features/zdr)
- **Tailscale Serve** issues HTTPS via MagicDNS + automatic TLS and keeps traffic **within the tailnet (private)**; **Funnel** = public internet (do not use for private). [kb](https://tailscale.com/kb/1312/serve)
- **Skills/MCP:** in 3P, skills are imported manually (zip a skill folder → drag in; official set at [anthropics/skills](https://github.com/anthropics/skills)). Non-Claude models lack native web search → add via MCP and disable the built-in `web_search` tool. [mcp-web-search](https://support.claude.com/en/articles/14503775-mcp-web-search)
- **Scheduled tasks** in 3P run only while the app is open (same constraint as paid Cowork). [docs](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)
- **Claude Code does NOT support the 3P gateway UI** — issue [#52572](https://github.com/anthropics/claude-code/issues/52572) closed *not-planned*. The harness-vs-model decoupling benefits **Cowork**, not Claude Code (Claude Code's own offline path is `ANTHROPIC_BASE_URL`).

## Speaker anecdote / interpretation (flagged — attributed to the video, not asserted as fact)

- **"~90% the same as paid Cowork"** — the speaker's estimate; not in Anthropic's docs. Documented *differences* (manual skills import, no dispatch button, scheduled-tasks-need-app-open, no native web search) are confirmed; the parity *percentage* is speculation.
- **"Anthropic released this relatively silently"** — speaker perception. The feature is prominently documented; "silent" is unverified.
- **"Enterprise customers wanted the harness with their own private models"** — plausible and *consistent with* the documented MDM-export + data-residency framing, but the motivation itself is the speaker's interpretation.
- **OpenRouter "assume anything you send is collected"** — too pessimistic: OpenRouter zero-logs by default (see correction below). The speaker is directionally right that cloud ≠ private, but the specifics are softer.
- **Quoted prices / model sizes / "256K context"** — video-era figures; treat as dated, verify before relying.

## Corrected or stripped during verification

| Video claim | Correction | Source |
|---|---|---|
| "Gemma E2B is 7.2 GB" | Doesn't match Ollama's published sizes (Gemma 2 2B ≈1.6 GB Q4_0; Gemma 4 E2B ≈250 MB CoreML). Figure removed; "check the library" substituted. | [ollama.com/library/gemma2:2b](https://ollama.com/library/gemma2:2b) |
| "You **need** Tailscale to get HTTPS" | Optional since Ollama **v0.14.0** native Anthropic API (Jan 2026, *before* the video). For local use you can often point the gateway straight at `http://localhost:11434`. | [ollama blog](https://ollama.com/blog/claude) |
| OpenRouter base URL `…/api` | Must include `/v1` → `https://openrouter.ai/api/v1`; omitting it 404s. | [openrouter auth](https://openrouter.ai/docs/api/reference/authentication) |
| "Assume OpenRouter collects everything" | OpenRouter zero-logs by default; no training unless opted-in; ZDR controls exist. Underlying *providers* still have their own policies. | [openrouter faq](https://openrouter.ai/docs/faq) |
| Brave MCP from `modelcontextprotocol/servers` | Brave Search MCP is now independently maintained: `npx -y @brave/brave-search-mcp-server`. | [brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server) |
| "100% private" (title, both paths) | True only for the **local Ollama** path. The **OpenRouter** path sends data off-machine — not 100% private. Video does warn at [00:55]. | [docs](https://claude.com/docs/cowork/3p/gateway) |
| "Not *trained* on the harness" | More precise: non-Claude models lack Anthropic's deployment-time **system prompting / harness instructions**, not just training-corpus coverage. | transcript [17:46] |

## Open / unverified

- Exact current OpenRouter per-model prices (pricing pages were intermittently unreachable on 2026-06-20; the $0.06/$0.33 Gemma figure is plausible but verify live).
- Whether a given Cowork build accepts a plain `http://localhost` gateway URL (the native-no-bridge path) vs still wanting HTTPS — confirm on your own install.
- Exact Gemma model tags/sizes in the Ollama library at time of use (the family — Gemma 3 / 4 / 3n — keeps expanding).

## Key Takeaways

- The **feature, protocol, and enterprise-rollout path are first-party-verified** — this is a real, documented Anthropic capability, not a hack.
- The **single most important nuance**: "private" depends entirely on *where your gateway routes*. Local Ollama = genuinely private; OpenRouter = off-machine (but better than the video implies); routing back to Anthropic = Anthropic's policy.
- The video's biggest **dated** step is the Tailscale HTTPS bridge — Ollama's native Anthropic API (v0.14.0+) often removes it.
- Treat **prices, model sizes, and "% parity"** as speaker-era estimates; the structural claims are sound, the numbers need a live check.
- **Claude Code ≠ Cowork** for 3P: the gateway UI is Cowork-only; Claude Code goes offline via `ANTHROPIC_BASE_URL`.

## Related

- [[cowork-third-party-inference/_index]] · [[cowork-third-party-inference/overview]] · [[cowork-third-party-inference/gateway-protocol-deep-dive]] · [[cowork-third-party-inference/video-to-original-crosswalk]]
- Parent topic: [[claude-cowork/_index]]. Sibling provenance logs: [[multi-agent-orchestration/source-provenance]] · [[agentic-analytics-harness/source-provenance]].
