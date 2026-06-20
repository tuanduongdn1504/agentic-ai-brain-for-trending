# cowork-third-party-inference

> **Topic created:** 2026-06-20 · **Path:** 5 yt-dlp-only (operator-submitted single video) + 6-agent original-resource deep-dive · **Status:** compiled (11 articles + index)
> **Verification:** Workflow `wf_4de40f38-856` (28 agents) — full transcript read + per-article adversarial verify. Honest ledger: [[cowork-third-party-inference/source-provenance]].

**What this topic is:** How to run the **Claude Desktop harness (Cowork — and Claude-Code-in-Desktop) on a model you choose** instead of paid Anthropic — **local via Ollama ($0, fully private)** or **cheap cloud via OpenRouter** — through Anthropic's official **"Cowork on 3P" (third-party inference) gateway**. The deep "build knowledge + double-deep-dive the original resource" ask resolved into: the **video walkthrough** (Bart Slodyczka) + first-party deep-dives of the **4 original resources** it's built on (the Cowork-3P gateway docs, Ollama, OpenRouter, the Tailscale HTTPS bridge).

**The big idea:** Anthropic decoupled the **harness** (the desktop app — skills, MCP, scheduling, UI) from the **model**. That's the [[harness-engineering/_index|harness-is-the-box]] thesis made first-party — and it's the lever for **free** (local), **private** (data never leaves the machine), and **cheap** (cloud-3P) Claude knowledge work.

**Key delta the video misses:** Ollama **v0.14.0** (Jan 2026, *before* the video) added a **native Anthropic Messages API** — so the video's Tailscale HTTP→HTTPS workaround is now optional. See [[cowork-third-party-inference/video-to-original-crosswalk]].

---

## Source

- **Primary video:** Bart Slodyczka, "Claude Cowork + Ollama = 100% FREE & PRIVATE (Full Setup)" — [ME4flXK_6tQ](https://www.youtube.com/watch?v=ME4flXK_6tQ) (2026-04-25, 18:41, ~47K views). Transcript: `raw/(C) 2026-06-20-cowork-ollama-3p-local-private.md`.
- **Original resources:** [Cowork-on-3P gateway docs](https://claude.com/docs/cowork/3p/gateway) · [Ollama](https://docs.ollama.com) · [OpenRouter](https://openrouter.ai/docs) · [Tailscale Serve](https://tailscale.com/kb/1312/serve).

## Articles

| Article | What it covers |
|---|---|
| [[cowork-third-party-inference/overview]] | What Cowork-on-3P is; harness-vs-model decoupling; the 3 model sources; same-vs-different from paid Cowork. **Start here.** |
| [[cowork-third-party-inference/setup-local-ollama]] | The local + private walkthrough (Ollama → HTTPS bridge → gateway config), corrected + with the native-no-bridge update. |
| [[cowork-third-party-inference/setup-cloud-openrouter]] | The cheap-cloud walkthrough (OpenRouter account → `/api/v1` → X-API-Key → disable native web_search). |
| [[cowork-third-party-inference/gateway-protocol-deep-dive]] | **Original #1** — the Anthropic Messages API contract a gateway must implement; `inference*` config keys; Apply-locally vs Export-MDM. |
| [[cowork-third-party-inference/ollama-deep-dive]] | **Original #2** — Ollama serving, port 11434, OpenAI-compat + **native Anthropic API (v0.14.0)**, model mgmt, the HTTPS gap. |
| [[cowork-third-party-inference/openrouter-deep-dive]] | **Original #3** — aggregator, pricing shape, **zero-logging + ZDR** privacy controls, model-availability tiers. |
| [[cowork-third-party-inference/tailscale-https-bridge]] | **Original #4** — Tailscale Serve (private) vs Funnel (public); alternatives (Caddy/cloudflared/ngrok); when you need no bridge. |
| [[cowork-third-party-inference/skills-mcp-websearch-byom]] | What you lose with a non-Claude model + how to restore it (manual skills import, Brave Search MCP, disable native tools, the harness-fidelity gotcha). |
| [[cowork-third-party-inference/tradeoffs-and-when-to-use]] | Decision framework — privacy × cost × quality/speed/harness-fidelity; when local vs cloud-3P vs paid. |
| [[cowork-third-party-inference/video-to-original-crosswalk]] | Every video claim → canonical original resource → what the video adds / simplifies / omits / now-outdated. |
| [[cowork-third-party-inference/source-provenance]] | Verification ledger — first-party verified vs speaker-anecdote vs corrected/stripped. |

## Pilot methods (the "apply to my flow" deliverable)

**18 ranked methods** across the operator's working surfaces (autopilot pipeline / hireui Goal-#2 / Claude-Code harness / Scrum coaching) — headline: **hireui candidate-PII → data-sovereignty via a BYOM gateway + local model**: `output/(C) 2026-06-20-cowork-3p-local-models-pilot-methods.md`.

## Cross-links

- **Parent:** [[claude-cowork/_index]] (this is its BYOM / third-party-model extension). · **Thesis:** [[harness-engineering/_index]] (harness-vs-model decoupling).
- **Composes with:** [[claude-api-cost-optimization/_index]] (local = the most extreme cost cut) · [[prompt-evaluation/_index]] (eval a swapped-in model before trusting it) · [[self-hosted-devops-oss/_index]] (same self-host-for-sovereignty ethos) · [[ai-operating-system/_index]] (builder layer).
- **Sibling deep-dives:** [[multi-agent-orchestration/_index]] · [[agentic-analytics-harness/_index]].
