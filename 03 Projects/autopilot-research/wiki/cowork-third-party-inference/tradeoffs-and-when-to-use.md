# Tradeoffs & When to Use Local vs Cloud-3P vs Paid Anthropic

## Three deployment modes, three different tradeoff profiles

Cowork on 3P enables three distinct ways to run Claude Cowork and Claude Code: **local Ollama models** (free, private, slow), **cloud 3P models via OpenRouter** (cheap, faster, data collected), and **paid Anthropic API** (best quality, most expensive, Anthropic terms). This article maps the tradeoff space so you can choose the right path for your work.

---

## The three axes: Privacy, Cost, Quality + Speed + Harness fidelity

### Privacy

- **Local Ollama**: 100% private within your tailnet (if using Tailscale Serve); traffic never leaves your network; **your data is yours alone**
- **OpenRouter cloud models**: OpenRouter itself logs zero prompts/completions by default (no training on user data); however, the underlying provider (Google Gemma, Mistral, etc.) maintains separate data retention policies; use the Zero Data Retention (ZDR) feature to route only to privacy-compliant providers
- **Paid Anthropic API**: Governed by [Anthropic's data policy](https://www.anthropic.com); broadly, Anthropic does not train on API inputs unless you explicitly opt in; see Anthropic's privacy terms for full details

**Nuance**: "local = private" is TRUE only if you do NOT expose Ollama beyond your machine or VPN. Ollama defaults to HTTP localhost:11434; exposing it to the internet with a default API key is a security risk.

### Cost

- **Local Ollama**: $0 per token after hardware amortization (one-time Ollama install + model download to your machine)
- **OpenRouter cloud models**: Varies by model; example from the video: Gemma 26B A4B $0.06/M input tokens, $0.33/M output tokens; free models exist but are rate-limited (20 req/min, unreliable for production); OpenRouter passes provider pricing through with no markup
- **Paid Anthropic API**: Pricing varies by model; Claude 3.5 Sonnet is a common baseline for cost-quality tradeoffs; check current pricing at [pricing.anthropic.com](https://pricing.anthropic.com) for latest rates; higher per-token cost but better quality may reduce total cost (fewer retries)

**Calculation example**: Running 1M input tokens daily for a month
- Local Ollama: $0
- OpenRouter Gemma: ~$1.86 (with modest usage assumptions)
- Anthropic: varies by model (check current pricing)

### Quality, Speed, and Harness Fidelity

This is the core tradeoff that shapes real-world user experience:

- **Paid Anthropic (Opus/Sonnet)**: Fastest inference, excellent tool use and skill execution, **trained on Claude Desktop harness system prompting**, meaning skills and connectors work reliably out of the box; dispatch button available
- **Cloud 3P models (OpenRouter Gemma, Mistral, etc.)**: Moderate inference speed (faster than local, slower than Anthropic), **not trained on Claude Desktop harness**; skills often fail on first attempt because the model doesn't understand the desktop app's underlying instructions; web search, document handling, and skill composition can require manual correction loops
- **Local Ollama models**: Slowest inference (depends on your hardware; 2-10 min per response on mid-range machines), **not trained on Claude Desktop harness**; same skill failure patterns as cloud 3P; model inference fully local means no cloud round-trip latency, but raw token/second throughput is much lower

**The harness-model separation thesis** (per the video speaker): Anthropic deliberately separated the desktop app harness from the model to enable enterprise BYOM (bring-your-own-model). The harness itself — skills, connectors, scheduled tasks, project management, code execution — is feature-rich. But it assumes Claude's system prompting and training; swap in Gemma or Llama, and the harness still works, but the model doesn't know how to drive it.

**Workaround for non-Claude models**: Run the skill once, let it fail, read the error, ask the model to amend the skill to correct itself, run again. The video demonstrates this: on the second attempt, the same skill succeeds because the model has been taught the correct pattern.

---

## When to use each

| Use Case | Recommendation | Why |
|---|---|---|
| **Private/sensitive work** (legal, medical, financial contracts) | Local Ollama | Zero external data transmission; complies with strict data residency requirements (EU GDPR, HIPAA, etc.) |
| **Offline-first environment** (no cloud connectivity, field work, air-gapped network) | Local Ollama | Only choice; cloud 3P and paid Anthropic require internet |
| **Cost-sensitive bulk processing** (overnight batch jobs, research analysis, email/document triage) | OpenRouter cloud 3P or Local Ollama | Bulk work tolerates slower inference; cost per operation drops to cents; Gemma 26B 1-2 orders of magnitude cheaper than Sonnet |
| **Best-quality agentic work** (complex multi-skill workflows, dispatch-heavy tasks, production automation) | Paid Anthropic (Sonnet/Opus) | Models trained on harness; skills work first-time; no retry loop overhead; dispatch button available for async scheduling |
| **Team rollout / enterprise SaaS integration** | Paid Anthropic API or Cloud 3P via MDM export | Local Ollama scales to 1 machine; cloud 3P or Anthropic API support team provisioning via OAuth/MDM profiles |
| **Experimentation / prototyping** (trying new skills, debugging harness integration) | Local Ollama first, then Paid Anthropic for final test | Local is free and immediate feedback; final validation on Paid ensures production readiness |
| **Cost optimization WITHOUT sacrificing reliability** (your baseline is Paid Anthropic, but you want to cut spend) | OpenRouter 3P for non-critical tasks + Paid Anthropic for critical tasks | Hybrid: use cheap models for web search, summarization, draft writing; use Sonnet for final review, code generation, complex reasoning |

---

## The "free & private" tradeoff is real — you trade quality for it

The video's title claims "100% FREE & PRIVATE" but this applies **only to the local Ollama path**. The OpenRouter cloud path is NOT private (data leaves your machine). Choosing either path means accepting real operational costs:

- **Inference latency**: Expect 2-10x slower response times on local hardware vs cloud models, and 10-50x slower vs Anthropic's optimized Sonnet/Opus
- **Skill reliability**: Non-Claude models require manual correction loops; simple tasks (web search, summarization) work; complex multi-step tasks (conditional logic, nested skills, code execution) often require re-authoring after first failure
- **Operator overhead**: You manage Ollama server, Tailscale bridge setup (or equivalent HTTPS proxy), model downloads, and skill debugging — this is 1-2 hours upfront + ongoing troubleshooting
- **Hardware cost**: Running large models requires modern CPU/GPU; budget $1,500-3,000 for adequate hardware, amortized over 2-3 years
- **Scheduled tasks constraint**: Tasks only run while the app is open (same as paid Cowork, but no background daemon option with local Ollama)

**Net result**: Local Ollama is genuinely "$0 per token" if you already own the hardware. But it costs time, mental load, and accepts reduced reliability in exchange. If your hourly rate is >$20, the time spent debugging non-Claude models may exceed OpenRouter's cloud bill.

---

## Harness-vs-model decoupling: enterprise BYOM and the broader thesis

[[harness-engineering/_index]] documents the principle that **the harness (desktop app + skill execution environment + CLI tools) is the box; the model is the engine you swap**. Cowork on 3P is the first-party realization of this thesis at consumer scale.

Enterprise BYOM scenarios (where this matters most):

- Financial institution wants Cowork's skill library but must route inference through private VPC with proprietary models
- Biotech firm needs Claude's desktop productivity tools but has models running locally for IP protection
- Government agency wants Cowork's scheduling/project-management but data must never leave classified networks

For these cases, the harness-model split is essential; you get Anthropic's opinionated UX + skill ecosystem without the Anthropic API subscription.

**Implications for builders**: If you are designing multi-tenant or enterprise software, consider whether the harness and the model can be separated. Cowork on 3P shows that the cost of separation is modest (gateway protocol + model discovery); the benefit is substantial (enterprise dataflow compliance + custom/proprietary models).

---

## Related decisions

### Should I add MCP servers if I'm using a local/cloud-3P model?

**Yes, strongly.** Non-Claude models lack native web search, advanced retrieval, and vendor-specific tooling. MCP servers (like Brave Search) add back critical capabilities. Overhead: edit Claude Desktop config JSON, acquire API key (Brave ~$5-10 setup), test once. The video shows this is worth the 10 minutes.

### What if I start with OpenRouter and want to migrate to local Ollama later?

**Gateway config is portable.** If you set up `https://openrouter.ai/api/v1` as your 3P gateway, switching to `http://localhost:11434` (or `https://localhost:11434` via Tailscale bridge) is a one-line URL change in Developer > Configure third-party inference. Your skills, connectors, and MCP servers stay the same. Execution speed/reliability will differ (as documented above), but plumbing-wise it's seamless.

### Does Claude Code support 3P models?

**Not yet.** As of June 2026, Claude Code does NOT have native third-party inference gateway support; [GitHub issue #52572 is closed as "not planned"](https://github.com/anthropics/claude-code/issues/52572). You can use 3P models in Cowork (desktop app), but Claude Code (CLI) still routes to Anthropic's API only. This is a major limitation for developers who want to keep code-generation local or private.

### Should I use the Tailscale bridge for local Ollama, or is there a simpler path?

**Tailscale is ONE approach, but may be outdated.** The video (April 2026) demonstrates Tailscale Serve because Anthropic's gateway documentation explicitly requires HTTPS (`inferenceGatewayBaseUrl` must be `https://`). However, **Ollama v0.14.0 (released January 2026, before the video) added native Anthropic Messages API support**. Many users report that the simpler command `ollama launch claude-desktop` now wires Claude Desktop directly to Ollama's native API endpoint without needing an external HTTPS bridge. Check current Ollama documentation — the native path may have made the Tailscale workaround optional for local development setups.

Alternatives if you want HTTPS without VPN:
- Caddy reverse proxy (local HTTP → HTTPS via self-signed certs in dev; Let's Encrypt in prod)
- nginx with `upstream` pointing to Ollama
- ngrok (cloud tunnel; data leaves your network, negating "private" benefit)

---

## Key Takeaways

- **Privacy-first work**: local Ollama = genuinely private; accept 5-10x slower inference + skill retry loops. OpenRouter cloud path is NOT private.
- **Cost-first work**: OpenRouter cloud 3P = 50-100x cheaper than Anthropic; inference speed acceptable; reliability gaps for complex skills
- **Reliability-first work**: Paid Anthropic Sonnet/Opus = best quality, dispatch available, skills work first-time; most expensive; baseline recommendation for production automation
- **Harness-model separation is real**: Cowork on 3P proves the principle; the desktop app is feature-rich but assumes Claude's training; non-Claude models require workarounds (MCP servers, skill re-authoring, manual correction loops)
- **Hybrid approach is practical**: Use OpenRouter 3P for non-critical batch work + Paid Anthropic for critical path / high-quality tasks; split the difference in cost and quality
- **Local hardware cost is hidden**: Running models locally requires adequate CPU/GPU; budget $1,500-3,000 for good hardware or accept slower inference on mid-range machines
- **Scheduled tasks only run when app is open** (local, cloud-3P, and paid Cowork all share this constraint; no background daemon)
- **Claude Code doesn't support 3P yet** — major blocker for developers seeking local/private code generation; track [issue #52572](https://github.com/anthropics/claude-code/issues/52572)
- **The "100% free & private" title conflates two paths**: local Ollama is private (but slow), OpenRouter is cheap (but not private). Choose based on your actual priority, not the marketing claim.

---

## Source

- **Video**: Bart Slodyczka, "Claude Cowork + Ollama = 100% FREE & PRIVATE (Full Setup)", YouTube ME4flXK_6tQ, published 2026-04-25, 18:41
- **Raw transcript**: `raw/(C) 2026-06-20-cowork-ollama-3p-local-private.md`
- **First-party documentation**:
  - https://claude.com/docs/cowork/3p/gateway — Anthropic Cowork on 3P gateway configuration
  - https://claude.com/docs/cowork/3p — Cowork on 3P feature overview
  - https://ollama.com/blog (January 16, 2026) — Ollama Anthropic Messages API support announcement
  - https://openrouter.ai/docs/guides/features/zdr — OpenRouter Zero Data Retention feature
  - https://tailscale.com/kb/1312/serve — Tailscale Serve HTTPS bridging documentation
- **Video timestamp references**: see raw transcript for exact speaker claims on model specs (Gemma 26B ~18GB, Gemma E2B ~7.2GB) and pricing; video speaker interpretation of "~90% feature parity" and "relatively silently released" are not first-party Anthropic claims

---

## Related articles

- [[cowork-third-party-inference/overview]] — What is Cowork on 3P? Feature overview and enterprise BYOM thesis
- [[cowork-third-party-inference/setup-local-ollama]] — Step-by-step: install Ollama, configure Tailscale bridge, wire to Cowork
- [[cowork-third-party-inference/setup-cloud-openrouter]] — Step-by-step: OpenRouter account + API key + gateway config
- [[cowork-third-party-inference/skills-mcp-websearch-byom]] — Add web search and other capabilities to local/cloud models via MCP
- [[claude-cowork/_index]] — Parent topic: Claude Cowork (Anthropic's desktop agentic app for humans + scheduled agents)
- [[claude-api-cost-optimization/_index]] — Cost levers across all Claude products; local/cheap-3P models as the extreme cut
- [[harness-engineering/_index]] — "Harness is the box": the principle of model-agnostic desktop environments and BYOM
- [[self-hosted-devops-oss/_index]] — Related ethos: kill SaaS bills by self-hosting; Ollama as part of that stack
