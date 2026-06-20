# Video-to-Original Crosswalk: "Claude Cowork + Ollama = 100% FREE & PRIVATE"

## Source

**Video:** Bart Slodyczka, "Claude Cowork + Ollama = 100% FREE & PRIVATE (Full Setup)" (YouTube ME4flXK_6tQ, published 2026-04-25, 18:41, ~47K views)

**Transcript:** `/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/(C) 2026-06-20-cowork-ollama-3p-local-private.md`

**Primary sources relied on:** https://claude.com/docs/cowork/3p/gateway, https://claude.com/docs/cowork/3p, https://ollama.com/blog, https://tailscale.com/kb/1312/serve, https://github.com/anthropics/skills, https://brave.com/search/api/guides/use-with-claude-desktop-with-mcp/, https://modelcontextprotocol.io

---

## Video Claims → Original Resources Crosswalk

| Timestamp | Video Claim | Canonical Original | Verdict | Notes |
|---|---|---|---|---|
| 00:02–00:29 | Gemma 26B is 18GB with 256K context window | [Google Gemma model card](https://ai.google.dev/gemma/docs/core/model_card_4) | UNVERIFIED | Video specs do not match accessible docs; Ollama library does not list context/size pairs |
| 00:02–00:29 | Gemma E2B is 7.2GB | [Ollama Gemma library](https://ollama.com/library/gemma2:2b) | CONTRADICTS | Gemma 2 2B (Q4_0) is 1.6GB; Gemma 4 E2B is ~250MB (CoreML). 7.2GB figure unmatched |
| 00:29 | OpenRouter Gemma 26B: $0.06/M input, $0.33/M output | [OpenRouter pricing](https://openrouter.ai/google/gemma-4-26b-a4b-it) | UNVERIFIED (page unreachable 2026-06-20) | Pricing cited as April 2026; current access denied. Assume historical accuracy pending verification |
| 00:55 | "Assume information sent to OpenRouter is collected/used" | [OpenRouter FAQ](https://openrouter.ai/docs/faq) | INCOMPLETE | OpenRouter itself logs zero prompts by default. Underlying providers (e.g., Google) have separate policies. ZDR controls exist but video does not mention them |
| 02:17 | "App must be open for scheduled tasks; no dispatch button in 3P" | [Anthropic Cowork Help](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork), [GitHub issue #54214](https://github.com/anthropics/claude-code/issues/54214) | VERIFIED | First-party docs confirm both constraints |
| 02:43–03:11 | Cowork 3P enables third-party model providers; official Anthropic feature | [claude.com/docs/cowork/3p](https://claude.com/docs/cowork/3p) | VERIFIED | Feature is first-party, documented, and official |
| 03:38 | "It's like 90% the same [as paid Cowork]" | [claude.com/docs/cowork/3p](https://claude.com/docs/cowork/3p) | SPEAKER INTERPRETATION | Anthropic docs do not quantify parity. Speaker estimates 90%; first-party confirms dispatch + scheduling constraints but not percentage |
| 03:38 | "[Anthropic] relatively silently released this updated feature" | [claude.com/docs/cowork/3p](https://claude.com/docs/cowork/3p) | SPEAKER INTERPRETATION | Release is documented at docs.claude.com; whether it was "silent" is speaker observation, not first-party claim |
| 04:33–05:01 | Enable Developer Mode: Help > Troubleshooting > Enable Developer Mode > Developer > Configure third-party inference | [gateway docs](https://claude.com/docs/cowork/3p/gateway) | VERIFIED | Path is first-party documented |
| 05:01 | Gateway requires 3 fields: URL, API key, auth type (bearer/x-api-key) | [gateway docs](https://claude.com/docs/cowork/3p/gateway) | VERIFIED | First-party spec |
| 05:29–06:50 | Ollama installation and model download via `ollama pull` + `ollama list` commands | [Ollama docs](https://docs.ollama.com/api) | VERIFIED | Commands are first-party Ollama |
| 06:50–07:18 | "Ollama comes with HTTP only; we need HTTPS for Anthropic compatibility" | [Ollama blog (Jan 2026)](https://ollama.com/blog/claude) | OUTDATED | Ollama v0.14.0 (Jan 2026) added native Anthropic Messages API support. Current integration uses `ollama launch claude-desktop` without Tailscale bridge; video predates or omits this path |
| 07:18–09:07 | Tailscale Serve bridges Ollama HTTP to HTTPS with automatic TLS cert + MagicDNS | [tailscale.com/kb/1312/serve](https://tailscale.com/kb/1312/serve) | VERIFIED | First-party Tailscale feature; traffic stays within tailnet (private). Note: Alternate methods (Caddy, ngrok) exist but not mentioned in video |
| 08:11 | `tailscale serve` creates HTTPS URL; `tailscale down` terminates session | [Tailscale Serve docs](https://tailscale.com/kb/1312/serve) | VERIFIED | First-party commands |
| 09:36 | Default API key value: "Ollama"; auth scheme: bearer | [Video transcript](https://www.youtube.com/watch?v=ME4flXK_6tQ&t=576s) | ANECDOTE | Speaker's choice; Ollama defaults differ; first-party docs do not mandate these values |
| 10:58–11:25 | Skills must be manually imported in 3P (download Anthropic repo zip, re-zip individual skill folder, drag into app) | [Anthropic skills repo](https://github.com/anthropics/skills) | VERIFIED (process) | Manual import is correct for 3P; differs from paid Cowork. Exact drag-and-drop workflow is speaker-anecdote but folder structure matches repo |
| 11:53–13:14 | Non-Claude models lack built-in web search; configure Brave Search MCP via Claude Desktop config file | [Brave Search MCP](https://github.com/brave/brave-search-mcp-server), [MCP docs](https://modelcontextprotocol.io) | VERIFIED | First-party MCP ecosystem; Brave server is now independently maintained (formerly in modelcontextprotocol/servers) |
| 12:47 | Brave Search MCP configuration uses NPX command; requires API key from Brave account | [Brave MCP guide](https://brave.com/search/api/guides/use-with-claude-desktop-with-mcp/) | VERIFIED | First-party Brave docs confirm NPX installation + API key requirement |
| 14:07–15:00 | OpenRouter URL: https://openrouter.ai/api/v1 (backslash + "api"); X-API-Key auth scheme | [OpenRouter API ref](https://openrouter.ai/docs/api/reference/authentication) | INCOMPLETE | Video says "openrouter API" (path unclear in transcript); correct endpoint is https://openrouter.ai/api/v1. Auth scheme X-API-Key is verified. Video may have been imprecise on full URL |
| 15:26 | Disable built-in web_search tool in Sandbox settings to prevent conflicts with MCP | [Support doc](https://support.claude.com/en/articles/14503775-mcp-web-search) | VERIFIED | First-party guidance for non-Claude models |
| 15:53 | Model availability tiers: available / partially available / fully unavailable; unavailability may indicate privacy standards non-compliance | [OpenRouter docs](https://openrouter.ai/docs/guides/overview/models) | UNVERIFIED | OpenRouter docs do not explicitly state that "unavailable" means privacy rejection. Availability reflects integration/metadata status but privacy interpretation is speaker speculation |
| 17:18–18:14 | Non-Claude models struggle with skills because "not trained on the Claude desktop app harness"; workaround: run skill once, let it fail, ask model to correct itself | [Anecdotal video testing](https://www.youtube.com/watch?v=ME4flXK_6tQ&t=1038s) | ANECDOTE + PARTIAL VERIFICATION | The observation that non-Claude models lack harness training is accurate (Anthropic tunes Claude's system prompting for the desktop app). The retry workaround is speaker-tested but not first-party documented. The framing is imprecise: issue is system-level prompting, not corpus "training" |
| 18:01–18:14 | Document creation skill succeeds after manual correction loop | [Video demo](https://www.youtube.com/watch?v=ME4flXK_6tQ&t=1081s) | ANECDOTE | Speaker demonstrates one successful use case; generalizability to other skills unverified |

---

## What the Video Gets Right & Teaches Well

- **Cowork 3P is official, documented, and accessible.** The video correctly identifies the feature path (Developer mode → gateway config) and explains the primary use case (harness + BYOM for enterprise).
- **Manual skill import is the correct process for 3P.** Unlike paid Cowork (pre-loaded skills), 3P requires manual import via the GitHub skills repo. Video's zip-and-drag workflow matches the folder structure.
- **Tailscale Serve is a valid HTTPS bridge.** The technical setup (MagicDNS, automatic TLS, tailnet-only privacy) is accurate. Traffic does not leave the tailnet, making the "private" claim true for this path.
- **MCP ecosystem enables web search for non-Claude models.** Brave Search MCP is the first-party recommended solution; configuration via Claude Desktop config file is standard.
- **Scheduled tasks require the app to be open.** This constraint is correctly identified and matches first-party documentation.
- **Speed/reliability tradeoff is real.** Local models (Ollama) run slower than cloud models (OpenRouter) or paid Claude; this is a correct simplification.

---

## What the Video Omits

- **Ollama v0.14.0+ native Anthropic API path (Jan 2026, pre-video):** The video uses Tailscale to work around Ollama's HTTP-only limitation. However, Ollama v0.14.0 (released January 10, 2026, ~3.5 months before this video) added native Anthropic Messages API support via `ollama launch claude-desktop`, eliminating the need for Tailscale. The video either predates awareness of this or chose not to mention the simpler path.
- **Claude Code lacks 3P gateway support:** The video focuses on Cowork; Claude Code does NOT support third-party inference gateways as of June 2026 (feature request #52572 closed as "not planned"). This is a significant limitation for developers using the CLI.
- **OpenRouter privacy depth:** While the video warns "assume data is collected," it omits OpenRouter's Zero Data Retention (ZDR) feature, which enforces provider policies at account/request level. ZDR is critical for sensitive workflows.
- **MDM export & team deployment:** The video is single-machine focused. First-party docs confirm Cowork 3P exports as .mobileconfig (macOS) or .reg (Windows) for organizational rollout, which the video does not cover.
- **Alternative HTTPS bridges:** The video uses Tailscale; alternatives like Caddy (single-machine reverse proxy with auto-HTTPS), ngrok (cloud tunnel), or self-hosted Ollama behind nginx are not mentioned.
- **Gateway alternatives beyond Ollama/OpenRouter:** LiteLLM, Portkey, and native Anthropic-compatible gateways (e.g., GitHub Copilot API) exist but are not mentioned.
- **Dispatch button absence rationale:** The video notes the dispatch button is missing in 3P but does not explain why (likely technical/UX decision by Anthropic, not documented).

---

## Now-Outdated Claims (Since 2026-04-25)

- **Tailscale bridge is necessary for Ollama.** Ollama v0.14.0 (Jan 2026) shipped native Anthropic Messages API support, making manual Tailscale bridging optional. Current recommended path is `ollama launch claude-desktop` with direct gateway URL `http://localhost:11434/v1/`. The Tailscale method in the video is still valid but no longer the simplest approach for local-only setups.
- **Brave Search MCP configuration requires manual JSON editing.** As of May 2026, Brave Search MCP moved to independent github.com/brave/brave-search-mcp-server (out of modelcontextprotocol/servers) with simplified NPX installation. Video's reference to the shared MCP servers repo is now outdated.
- **Gemma 4 26B file size/context specifications.** Video quotes 18GB + 256K context; accessible Google Gemma docs and Ollama library do not confirm these figures. If Ollama's quantization or caching changed post-April, the 18GB figure may be irrelevant.
- **OpenRouter pricing ($0.06/$0.33 for Gemma 26B).** As of 2026-06-20, OpenRouter pricing page is unreachable (access denied 404). Video's April 2026 prices cannot be verified; assume outdated and verify directly before planning cost estimates.

---

## Verdict Summary

| Dimension | Grade | Notes |
|---|---|---|
| **Technical accuracy (core setup)** | A | Cowork 3P enable path, gateway config, skill import, MCP wiring are first-party verified |
| **Completeness** | B− | Omits Ollama v0.14 native path; Claude Code limitation; ZDR; MDM export; dispatch rationale |
| **Currency** | C+ | Tailscale bridge now optional (Ollama v0.14+); Brave MCP repo moved; pricing unreachable; some model specs unverified |
| **Verifiability** | B | Claims map well to first-party docs; ~3 unverifiable vendor specs (Gemma sizes, OpenRouter pricing, "fully unavailable" = privacy failure) |
| **Pedagogical value** | A | Excellent walkthrough for newcomers to Cowork 3P; clear separation of local (Ollama) vs. cloud (OpenRouter) paths |

**Recommendation:** Use this video as an **entry point to Cowork 3P**, then supplement with:
1. [[cowork-third-party-inference/setup-local-ollama|setup-local-ollama]] (Ollama v0.14+ native path)
2. [[cowork-third-party-inference/gateway-protocol-deep-dive|gateway-protocol-deep-dive]] (Messages API spec)
3. [[cowork-third-party-inference/tradeoffs-and-when-to-use|tradeoffs-and-when-to-use]] (when to use each path)

---

## Key Takeaways

- **Cowork 3P is official.** Anthropic deliberately separated the harness (desktop app) from the model to enable enterprise BYOM; the feature is documented and stable.
- **Tailscale bridge is ONE valid approach but increasingly optional.** Ollama v0.14+ (Jan 2026) has native Anthropic API support; `ollama launch claude-desktop` is now the simpler local path. Video's Tailscale method remains valid for advanced setups (e.g., multi-machine access via tailnet).
- **Manual skill import in 3P is correct.** Unlike paid Cowork, skills must be downloaded, zipped, and dragged in. This is a documented operational difference, not a bug.
- **Web search requires MCP for non-Claude models.** Brave Search MCP is first-party recommended; disable the built-in web_search tool to avoid fallback failures.
- **Non-Claude models lack harness training.** They struggle with Cowork's underlying system prompts. Workaround: run skills once, inspect failures, ask model to self-correct, re-run. This is expected (not a defect) and applies to any non-Claude model provider.
- **Speed/reliability tradeoff is real.** Local Ollama is slower than paid Claude; OpenRouter cloud models are faster than local but slower than paid + more expensive than fully local. Choose based on latency + privacy + cost priorities.
- **"100% private" claim is conditional.** True for local Ollama + Tailscale (data stays in your tailnet). False for OpenRouter (cloud) path. Video acknowledges this but title conflates both paths.

---

## Related Articles

- [[cowork-third-party-inference/overview|overview]] — What is Cowork 3P and when to use it
- [[cowork-third-party-inference/setup-local-ollama|setup-local-ollama]] — Step-by-step Ollama v0.14+ native setup
- [[cowork-third-party-inference/setup-cloud-openrouter|setup-cloud-openrouter]] — OpenRouter gateway configuration
- [[cowork-third-party-inference/gateway-protocol-deep-dive|gateway-protocol-deep-dive]] — Messages API + model discovery spec
- [[claude-cowork/_index|Claude Cowork overview]] — Parent topic: Anthropic's scheduled-agent desktop app
- [[claude-api-cost-optimization/_index|Cost optimization]] — How Cowork 3P + local/cheap models cut API costs to $0
- [[prompt-evaluation/_index|Prompt evaluation]] — Methodologies for testing swapped-in local/cloud models
