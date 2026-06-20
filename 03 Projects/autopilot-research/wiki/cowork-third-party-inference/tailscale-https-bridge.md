# Deep-dive: the HTTP→HTTPS bridge — Tailscale Serve + alternatives

## Overview

Anthropic's Cowork on 3P gateway requires HTTPS endpoints implementing the Messages API. Ollama (the local model server) serves HTTP only on port 11434 by default. This article covers why the bridge is needed, how Tailscale Serve solves it, the exact commands from the video, alternatives ranked by privacy/ease, and the critical privacy distinction between **Serve (private)** and **Funnel (public)**.

## The core problem

- **Ollama default:** `http://localhost:11434/v1/` (HTTP, port 11434)
- **Cowork on 3P requirement:** HTTPS endpoint (TLS-encrypted, certificate required)
- **The gap:** Ollama has no native HTTPS listener by default

The video demonstrates this gap: "Ollama comes with a default URL that we can use to tap into our model, but that URL has a HTTP connection. And for Anthropic, in order for us to use a third-party model, we actually need a HTTPS connection... Unfortunately, Ollama doesn't natively give the HTTPS connection."

## Why the bridge is necessary (historical context)

As of April 2026 (video publication), Ollama v0.14.0 (released January 2026) already supported native Anthropic Messages API. However, the video did not reference this simpler path. The bridge approach shown remains valid for:

1. **Distributed setup** — if running Ollama on a different machine than Claude Desktop, the bridge handles the HTTPS boundary
2. **Tailscale network isolation** — the bridge is not just HTTPS termination; it's also your private VPN tunnel (see [[cowork-third-party-inference/tailscale-https-bridge#privacy-critical-serve-vs-funnel]] below)
3. **Pre-v0.14 Ollama versions** — users on older versions needed the bridge

**Modern alternative:** Ollama v0.14.0+ users can use `ollama launch claude-desktop` to skip the bridge entirely. See [[cowork-third-party-inference/setup-local-ollama]] for the native path.

## Tailscale Serve: how it works

Tailscale Serve provides automatic HTTPS via Let's Encrypt certificates issued for your tailnet DNS names. The architecture:

```
Claude Desktop (Cowork)
  ↓ (HTTPS to device-name.tailnet-name.ts.net)
Tailscale Serve (reverse proxy + TLS termination)
  ↓ (HTTP to localhost:11434)
Ollama (local model server)
```

### Key properties

- **MagicDNS:** Tailscale automatically issues DNS names in the form `device-name.tailnet-name.ts.net` for each device in your tailnet
- **Let's Encrypt certificates:** Serve automatically provisions TLS certificates for those DNS names (no manual cert management)
- **Tailnet = private network:** Traffic stays encrypted and confined to authenticated tailnet members only. Not accessible from the public internet
- **Traffic flow:** Local to your machine (device → localhost) or within your tailnet (if using Ollama on a different device)

### Free tier availability

Tailscale Serve is available on the **free tier** (the video confirms: "I'm actually running a free account. I haven't paid for anything").

## The video's exact commands

From the transcript, the setup involves three terminal commands:

### Step 1: Enable Tailscale in the CLI

```bash
tailscale serve
```

The video notes: "This first command that we're going to run in the terminal is going to give us the ability to run Tailscale commands in our terminal."

On first run, Tailscale will prompt you to enable the feature via a provided URL in your Tailscale admin console.

### Step 2: Create the HTTPS bridge (temporary session)

```bash
tailscale serve --https=device-name.tailnet-name.ts.net http://localhost:11434
```

The video shows this as a temporary session: "this is going to be a temporary session where we're creating that HTTPS URL and then we're deploying a version of Ollama with some configurations that are going to work for the Claude CoWork connection."

The resulting URL (e.g., `https://device-name.tailnet-name.ts.net`) is then pasted into Cowork's gateway configuration under "Inference Gateway Base URL."

### Step 3: Teardown

```bash
tailscale down
```

Or, to just disable Serve without dropping the full Tailscale connection:

```bash
tailscale serve --remove=https/device-name.tailnet-name.ts.net
```

The video notes: "if we're done with the session for the day, we want to fully terminate all those things that we set up, you can run this command. It's going to turn off your Ollama from emitting any AI into Tailscale and it's also going to turn off Tailscale. So, at this stage, you'll be basically back to zero."

## API key and authentication scheme

Once you have the Tailscale HTTPS URL, configure Cowork with:

- **Inference Gateway Base URL:** `https://device-name.tailnet-name.ts.net`
- **Inference Gateway API Key:** If Ollama has no API key configured, use the default value `ollama` (the video confirms: "if you haven't set an API key for your connection right now, you can just put a default value of Ollama")
- **Authentication Scheme:** Bearer token (the video notes: "we can just leave it as bearer like it is right now")

After pasting these into Cowork Developer > Configure third-party inference > Gateway, click "Apply Locally" to activate.

## Privacy guarantee: Tailscale Serve vs. Funnel

**CRITICAL DISTINCTION (from Tailscale docs):**

- **Serve:** traffic stays PRIVATE within your tailnet. NOT accessible from the public internet. Your data remains encrypted end-to-end; Tailscale nodes relay encrypted traffic but cannot read it.
- **Funnel:** exposes the endpoint PUBLICLY to the internet. Anyone with the URL can access your Ollama instance. **Do NOT use Funnel for private model serving.**

The video emphasizes local privacy: "this is going to let us create a secure connection between Ollama and Claude CoWork, which gives us that HTTPS... Tailscale will let us create a secure connection between Ollama and Claude CoWork."

## Cost and platform support

- **Tailscale Serve:** Free tier supported
- **Platforms:** macOS (via Tailscale app), Windows (via Tailscale app), Linux (via `tailscale` CLI)
- **No affiliated endorsement in the video:** The speaker explicitly states: "I'm not affiliated with these guys. I just use them for different things that I do."

## Alternatives ranked (privacy + ease)

| Approach | Privacy | Setup Ease | Notes |
|---|---|---|---|
| Ollama native Anthropic API (v0.14.0+) | **100% private** (no bridge) | ⭐⭐⭐ Easiest | `ollama launch claude-desktop` or env var `ANTHROPIC_BASE_URL=http://localhost:11434` |
| Tailscale Serve (video approach) | **100% private** (tailnet only) | ⭐⭐ Moderate | Requires Tailscale account (free) + CLI commands; decouples Ollama and Claude Desktop machines |
| Caddy reverse proxy | **100% private** (local only) | ⭐⭐ Moderate | Single-machine setup; auto-TLS via Let's Encrypt; no third-party account needed |
| nginx + manual TLS | **100% private** (local only) | ⭐ Complex | Full control; requires cert management (mkcert or manual Let's Encrypt) |
| cloudflared | **100% private** (Cloudflare tunnel) | ⭐⭐ Moderate | Uses Cloudflare's infrastructure; requires Cloudflare account |
| ngrok | **NOT private** (public URL) | ⭐⭐⭐ Easiest | Public internet exposure; free tier has rate limits and session timeouts |
| Tailscale Funnel | **NOT private** (public URL) | ⭐⭐⭐ Easiest | Public internet exposure; same as Funnel — avoid for private models |

### Recommendation for "100% private" requirement

If the goal is "100% private" (as stated in the video title), use **Ollama native path** (modern) or **Tailscale Serve** (if running Ollama remotely). Do NOT use ngrok, Funnel, or any public tunnel — those expose your model to the internet.

## Decision tree: when to bridge

**Use a bridge (Tailscale Serve or Caddy) when:**
- Running Ollama on a **different machine** than Claude Desktop (e.g., server in closet, Ollama on M-series Mac, Claude Desktop on Intel)
- Need **automatic TLS** without manual cert management
- Want **private-network isolation** (Tailscale Serve) or **localhost-only** (Caddy)

**Skip the bridge (use Ollama native path) when:**
- Running Ollama and Claude Desktop on the **same machine**
- Using Ollama **v0.14.0 or later** (January 2026+)
- Willing to accept HTTP for local-only development (Cowork 3P allows HTTP for gateways in dev mode per Anthropic docs)

## Troubleshooting

- **Tailscale commands not found:** Install Tailscale app from https://tailscale.com/download/
- **Serve command fails on first run:** Check your Tailscale admin console (https://login.tailscale.com); enable "Serve" under DNS settings for your device
- **HTTPS certificate mismatch:** Clear Cowork caches (`~/Library/Application Support/Claude/` on macOS) and restart
- **Ollama not reachable at `localhost:11434`:** Verify Ollama is running (`ollama list` in terminal; if empty, pull a model first: `ollama pull gemma2:2b`)

## Related articles

- [[cowork-third-party-inference/setup-local-ollama]] — Installing Ollama and the native Anthropic API path (v0.14.0+)
- [[cowork-third-party-inference/setup-cloud-openrouter]] — Cloud models via OpenRouter (no bridge needed; uses HTTPS natively)
- [[cowork-third-party-inference/gateway-protocol-deep-dive]] — Anthropic's Messages API requirements for 3P gateways
- [[cowork-third-party-inference/overview]] — Cowork on 3P feature overview and when to use it
- [[claude-cowork/_index]] — Parent topic: Cowork (Anthropic's desktop agentic app)
- [[harness-engineering/_index]] — Harness-model separation thesis
- [[self-hosted-devops-oss/_index]] — Related: self-hosted infrastructure (Ollama is the self-hosted model layer)

## Key Takeaways

- Ollama serves HTTP by default; Anthropic Cowork on 3P requires HTTPS. A bridge is needed unless using Ollama v0.14.0+ native path.
- **Tailscale Serve** provides automatic HTTPS via MagicDNS + Let's Encrypt and keeps traffic private within your tailnet (free tier available).
- **Serve != Funnel.** Serve is private; Funnel is public. For "100% private" setups, use Serve or skip the bridge entirely with native Ollama.
- The video's exact commands: `tailscale serve` → `tailscale serve --https=... http://localhost:11434` → paste the URL into Cowork gateway config → `tailscale down` to teardown.
- Alternatives (Caddy, nginx, cloudflared) exist but require more setup. Native Ollama (v0.14.0+) is now the simplest for single-machine deployments.
- The bridge is most useful for **distributed setups** (Ollama on a different machine from Claude Desktop) or **older Ollama versions** pre-v0.14.0.

## Source

- **Primary:** Bart Slodyczka, "Claude Cowork + Ollama = 100% FREE & PRIVATE (Full Setup)", YouTube video ME4flXK_6tQ, published 2026-04-25, transcript: `/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/(C) 2026-06-20-cowork-ollama-3p-local-private.md`
- **Verified facts:**
  - Tailscale Serve documentation: https://tailscale.com/kb/1312/serve
  - Tailscale tailnet concept: https://tailscale.com/docs/concepts/tailnet/
  - Ollama v0.14.0 release (Anthropic API support): https://github.com/ollama/ollama/releases/tag/v0.14.0
  - Anthropic Cowork on 3P gateway docs: https://claude.com/docs/cowork/3p/gateway

## Secondary sources

- OpenRouter pricing verification: https://openrouter.ai/google/gemma-4-26b-a4b-it (as of April 2026 video publication)
