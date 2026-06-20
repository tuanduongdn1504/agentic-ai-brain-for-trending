# Setup: local + private model via Ollama (the video walkthrough, corrected + updated)

## Overview

This article walks through the **end-to-end ritual** for running Claude Cowork with a LOCAL model via Ollama, exactly as Bart Slodyczka's April 2026 video demonstrates. It covers every step:
- Installing Ollama
- Downloading a model via `ollama pull`
- Bridging HTTP to HTTPS using Tailscale Serve (the video's original approach)
- Filling the three gateway fields in Cowork on 3P settings
- Testing with a local model
- A "**Updated since the video**" box covering simpler paths available NOW

**Key principle:** This setup keeps ALL computation on your machine. No data leaves your network except the Tailscale bridge itself (which remains within your private tailnet, not the public internet).

---

## Prerequisites

- **Claude Desktop app** installed (from claude.com/download)
- **A machine with enough RAM** to run a local AI model (≥8GB recommended for Gemma 2B, ≥24GB for Gemma 26B)
- **Tailscale account** (free tier is fine) — to bridge Ollama's HTTP → HTTPS
- **Terminal access** (macOS: Terminal.app; Windows: PowerShell)

If your machine cannot run local models, skip to the [[cowork-third-party-inference/setup-cloud-openrouter]] article instead.

---

## Step 1: Enable Cowork on 3P Developer Mode

**What:** Activate the third-party inference gateway feature in Claude Desktop.

1. Open Claude Desktop
2. Go to **Help > Troubleshooting > Enable Developer Mode**
3. Then go to **Developer > Configure third-party inference**
4. Select **Gateway** (not Bedrock or any other provider type)
5. You'll see three empty fields:
   - `Gateway base URL` (will be your Ollama/Tailscale URL)
   - `API key` (will be "Ollama" by default for local)
   - `Auth scheme` (bearer token or x-api-key)

Leave these empty for now. You'll fill them in Step 5 below.

**Source:** The video shows [04:33–05:01] how to navigate this menu. First-party Anthropic docs: https://claude.com/docs/cowork/3p/gateway

---

## Step 2: Install Ollama

**What:** Download and install the Ollama model server on your machine.

**Terminal command:**

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

Or install via the GUI app from https://ollama.com/.

**After install:**
Verify Ollama is running:

```bash
ollama --version
```

If the command fails, restart your terminal or check if the install completed.

**Source:** [05:29–05:55] in the video. First-party Ollama docs: https://docs.ollama.com/

---

## Step 3: Pull a Model

**What:** Download a model to your machine. The video demonstrates pulling Gemma models.

**Terminal command — recommended (smaller, faster):**

```bash
ollama pull gemma2:2b
```

This downloads the Gemma 2 2B model (~1.6GB on disk with Q4_0 quantization).

**Alternative — larger model (requires ≥24GB RAM):**

```bash
ollama pull gemma4:26b-a4b-it
```

The video claims this is "18 gigs" with "256K context window" (unverified against first-party specs; verify against your hardware before pulling).

**The video's specific choice — Gemma E2B [00:02, 06:23–06:50]:**

The video references pulling a model called `gemma4:e2b` described as "7.2 gigs." This specification does NOT match documented Gemma model sizes. Gemma 2 2B is ~1.6GB; Gemma 4 26B is larger. Ollama's model library does not list a standard "E2B" variant with the claimed size. **Before pulling, verify the exact model name and size exist in your Ollama version:**

```bash
ollama pull gemma2:2b    # Safe, documented choice
```

**Check your local models:**

```bash
ollama list
```

You'll see installed models with their size and digest hash.

**Source:** [06:23–06:50] in the video shows `ollama pull` and `ollama list`. Gemma size claims at [00:02, 00:29] are unverified against first-party Google Gemma documentation.

---

## Step 4: Bridge Ollama HTTP → HTTPS with Tailscale Serve

**Why:** Ollama's default API endpoint is `http://localhost:11434/v1/` (HTTP only). Anthropic's Cowork on 3P gateway requires HTTPS. Tailscale Serve automatically provisions TLS certificates and exposes your local Ollama to Claude Desktop via HTTPS, all within your private tailnet (no public internet exposure).

**Caveat — Newer approach available:** As of January 2026 (Ollama v0.14.0), Ollama natively supports Anthropic's Messages API. Test direct HTTP integration first before using Tailscale; see "Updated since the video" section below.

### 4a. Create a Tailscale account and install Tailscale

1. Go to https://tailscale.com/
2. Create a free account (no credit card required)
3. Download and install the Tailscale app for your OS
4. Log in and run the onboarding (this adds your machine to your private tailnet)

**Command to verify installation:**

```bash
tailscale status
```

You should see your machine listed with a Tailscale IP (100.x.x.x).

**Source:** [07:18–07:44] in the video.

### 4b. Enable Tailscale Serve setting

When you first run the `tailscale serve` command, Tailscale will prompt you to enable "Serve" mode in the Tailscale app settings. The terminal will give you a direct link to click.

**Do this once only.**

### 4c. Create the HTTPS bridge (temporary session)

**Terminal command:**

```bash
tailscale serve https / http://localhost:11434
```

This creates a temporary session that routes traffic from your Tailscale hostname (e.g., `my-machine.tail12345.ts.net`) to your local Ollama HTTP endpoint.

**Output:** The terminal will print a URL like:

```
https://my-machine.tail12345.ts.net
```

**Copy this URL — you'll paste it into Cowork on 3P settings in Step 5.**

**Source:** [08:11–09:07] in the video shows the exact Tailscale commands.

### 4d. Tear down the bridge (when done for the day)

```bash
tailscale serve off
```

This disables the Tailscale bridge and stops routing Ollama traffic. Your local Ollama is still running; you just can't reach it from Claude Desktop anymore.

**Source:** [09:07] shows `tailscale serve reset` (video terminology; modern Tailscale uses `serve off`).

---

## Step 5: Fill Cowork on 3P Gateway Settings

**What:** Tell Claude Desktop where your Ollama is and how to authenticate.

1. **Open Claude Desktop > Help > Developer > Configure third-party inference**
2. **Paste the Tailscale URL** you copied from Step 4c into the `Gateway base URL` field
   - Example: `https://my-machine.tail12345.ts.net`
3. **Set API key** to `Ollama` (or leave blank if Ollama has no custom API key configured)
4. **Set Auth scheme** to `Bearer` (the default; Ollama uses bearer token auth)
5. **Click "Apply locally"** to save settings to this machine only

**Verify:** Relaunch Claude Desktop. In the model picker, you should now see your Gemma model listed alongside (or instead of) Claude models.

**Optional — switch between gateway + paid account:** The video [10:04–10:31] shows that after relaunching, you can toggle between:
- **Gateway connection** (your local Ollama model)
- **Your paid Anthropic account** (Claude models like Opus, Sonnet)

Switch by clicking the gear icon and selecting "Gateway" or your account name.

**Source:** [09:36–10:04] in the video. First-party docs: https://claude.com/docs/cowork/3p/gateway

---

## Step 6: Test the Setup

**In Cowork:**

1. Select your Gemma model from the model picker
2. Type a simple message: "Hi, who are you?"
3. You should get a response from your local Gemma model within 10–30 seconds (depending on hardware)

**What to expect:**
- Response time is **SLOWER** than cloud models (Ollama runs locally, not optimized for latency)
- Responses are **100% private** — never leave your machine (except the Tailscale bridge stays within your tailnet)
- The model may struggle with **skills** (document creation, code execution) — more on this below

**Source:** [01:23–01:50] shows the video testing a local model with a simple conversation.

---

## Updated since the video

### Native Ollama + Anthropic Messages API (Ollama v0.14.0+, January 2026)

**Major simplification — the simpler path you should try first:** Ollama v0.14.0 (released January 10, 2026) added native Anthropic Messages API support. This happened BEFORE the video was published (April 2026), but the video does not reference this evolution.

**What this means:**
- Ollama now natively speaks the Anthropic Messages API at `http://localhost:11434/v1/`
- Claude Desktop can point directly to Ollama without a Tailscale bridge
- Simpler setup; no third-party VPN tool required
- **Caveat:** HTTP-only by default (no HTTPS). Anthropic docs indicate local development gateways may accept HTTP for testing environments.

**Recommended first step — test direct HTTP integration (no Tailscale):**

1. **In Cowork 3P gateway settings**, set:
   - `Gateway base URL`: `http://localhost:11434`
   - `API key`: `ollama`
   - `Auth scheme`: `Bearer`
2. **Click "Apply locally" and test.** If it works, you're done — no Tailscale needed.
3. **If HTTP is rejected**, only then add Tailscale Serve as a bridge (steps 4a–4d above).

**Alternative command (if your Ollama is v0.14.0+ and supports it):**

The video and some Ollama documentation reference `ollama launch claude-desktop`, which reportedly wires Claude Desktop directly to Ollama with zero manual configuration. Verify this command exists and is appropriate for your Ollama version:

```bash
ollama help | grep launch
```

If the command exists and you trust it, it may be faster than manual gateway config. Proceed at your own risk; this article uses the manual approach for transparency.

**First-party source:** https://github.com/ollama/ollama/releases/tag/v0.14.0 (January 10, 2026 release notes confirming Anthropic Messages API support). https://docs.ollama.com/integrations/claude-code (integration guide).

### Alternatives to Tailscale bridge

If Anthropic rejects HTTP and you prefer not to use Tailscale, other HTTPS-bridging options exist (not tested in the video):

- **Caddy reverse proxy** — lightweight, auto-HTTPS via Let's Encrypt, CLI-based (https://caddyserver.com/)
- **nginx** — production-grade reverse proxy with TLS support (requires manual cert setup)
- **ngrok** — cloud tunnel (creates public-internet exposure, NOT recommended for private setup)

**None of these alternatives are documented in the video. Use at your own risk.**

---

## Adding Web Search to Your Local Model

**Why:** Local models (Gemma, Llama, etc.) do NOT have built-in web search like Claude Opus/Sonnet do. If you ask a local model to browse the web, it will fail.

**Solution:** Use MCP (Model Context Protocol) to wire Brave Search into Cowork.

### 6a. Get a Brave API key

1. Go to https://api.search.brave.com/
2. Sign up for a free account
3. Create an API key
4. Copy it

### 6b. Edit Claude Desktop config

The video [11:53–13:14] shows how to manually edit the `claude_desktop_config.json` file to add Brave Search as an MCP server.

**File location:**
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

**Add this block to the `mcpServers` section:**

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@brave/brave-search-mcp-server"],
      "env": {
        "BRAVE_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

Replace `your-api-key-here` with the key you copied from Brave.

**Then:** Restart Claude Desktop. You should see Brave Search available in the tools/connectors panel.

**Note on MCP server maintenance:** Brave Search MCP server is now independently maintained at https://github.com/brave/brave-search-mcp-server. Earlier references to modelcontextprotocol/servers may be outdated.

### 6c. Disable built-in web_search tool (important)

The video [15:00–15:26] notes that non-Claude models will try to use the built-in `web_search` tool (which only works with Claude models). This causes errors.

**Workaround:** Go to **Developer > Sandbox and Workspace > Disabled tools** and add `web_search` to the disabled list. Now your local model will route web search requests to Brave Search MCP instead of trying the built-in tool.

**Source:** [15:00–15:26] in the video; first-party MCP docs: https://modelcontextprotocol.io/

---

## Adding Skills to Cowork on 3P

**Why:** Cowork on 3P does NOT come with pre-loaded skills like the paid version does. You must import them manually.

### 7a. Download Anthropic skills

1. Go to https://github.com/anthropics/skills
2. Click the green **Code** button > **Download ZIP**
3. Unpack the zip file on your machine

### 7b. Import a skill

1. In Cowork, go to **Customize > Skills > Manage skills > + Create skill > Upload**
2. Find the skill folder you want (e.g., `docx`, `pdf`, `pptx`, `xlsx`)
3. Right-click the folder > **Compress** (macOS) or **Send to > Compressed folder** (Windows) to turn it back into a zip
4. Drag the zip file into Cowork

The skill will appear in your Customize panel.

**Source:** [10:58–11:25] in the video; first-party skills repo: https://github.com/anthropics/skills

---

## Known Limitations & Workarounds

### 1. Local models struggle with skills

**Problem:** The video [17:18–18:14] demonstrates that Gemma and other non-Claude models are "not trained on the Claude Desktop app harness." They fail at skill execution (e.g., creating documents, running code) and get stuck in retry loops.

The underlying issue is that non-Claude models lack the system-level prompting and harness-specific instructions that Anthropic's Claude models receive at deployment time.

**Workaround (video's suggestion):**
1. Run the skill once, let it fail
2. Inspect the error in the model's output
3. Ask the model: "Here's what went wrong. Can you fix the skill so it works next time?"
4. Run the skill again

This manual amendment loop is a significant friction point compared to paid Cowork with Claude models.

**Source:** [17:18–18:14] in the video.

### 2. No dispatch button in Cowork on 3P

The video [02:17–02:43] notes that Cowork on 3P is missing the **dispatch** button (which lets you delegate tasks to Claude while you step away). This is a documented limitation of the 3P feature as of April 2026.

**Source:** [02:17–02:43] in the video; confirmed in first-party Anthropic GitHub issue #54214 (Claude Code dispatch limitation).

### 3. Scheduled tasks only run while Cowork is open

Unlike paid Cowork, there is no background service or daemon. Scheduled tasks [02:17–02:43] only fire while the Claude Desktop app is actively running on your machine.

**Source:** [02:17–02:43] in the video; corroborated by first-party Anthropic documentation on scheduled tasks.

### 4. Model discovery requires correct API format

The video [09:36] assumes Ollama's API key can be left as "Ollama" or a default value. If Cowork cannot auto-discover your models from the gateway, you may need to explicitly set `inferenceModels` in the config to list them by ID. See first-party docs: https://claude.com/docs/cowork/3p/gateway#model-discovery

---

## Teardown (when done)

To completely stop the bridge and return to baseline:

```bash
tailscale serve off   # Disable the HTTPS bridge
tailscale logout      # Log out of Tailscale (optional)
```

Ollama will continue running locally. If you want to stop it entirely:

- **macOS:** Close the Ollama app, or run `brew services stop ollama`
- **Linux:** `systemctl stop ollama`
- **Windows:** Close the Ollama app

---

## Key Takeaways

- Cowork on 3P is Anthropic's official feature for third-party model providers (local or cloud)
- **Local path (Ollama + optional Tailscale):** Free, 100% private (Tailscale-only variant), slow, requires manual skill fixes
- **Install order:** Ollama → model pull → optional Tailscale → Cowork config → test
- **Ollama v0.14.0+ native API (January 2026)** eliminates Tailscale as a requirement; **test direct HTTP first** before adding complexity
- **Web search:** Add via Brave Search MCP; disable built-in web_search tool to route to MCP
- **Skills:** Import manually from GitHub; expect non-Claude models to fail on first attempt and require manual amendment due to harness training mismatch
- **Scheduled tasks:** Only run while Cowork is open (no background service)
- **Teardown:** `tailscale serve off` stops the bridge; Ollama stays running unless you explicitly stop it

---

## Source

**Video:** Bart Slodyczka, "Claude Cowork + Ollama = 100% FREE & PRIVATE (Full Setup)" (YouTube ME4flXK_6tQ, published 2026-04-25, 18:41, ~47K views)

**Transcript:** `/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/(C) 2026-06-20-cowork-ollama-3p-local-private.md`

**First-party Anthropic docs:**
- https://claude.com/docs/cowork/3p/gateway (gateway configuration reference)
- https://claude.com/docs/cowork/3p (Cowork on 3P overview)

**First-party tooling:**
- https://ollama.com/ (Ollama homepage)
- https://github.com/ollama/ollama (Ollama releases; v0.14.0+ for native Anthropic API)
- https://github.com/ollama/ollama/releases/tag/v0.14.0 (v0.14.0 release notes confirming Anthropic Messages API support)
- https://docs.ollama.com/integrations/claude-code (Ollama + Claude Code integration guide)
- https://tailscale.com/kb/1312/serve (Tailscale Serve documentation)
- https://github.com/anthropics/skills (official Anthropic skills repository)
- https://modelcontextprotocol.io/ (MCP specification)
- https://api.search.brave.com/ (Brave Search API signup)
- https://github.com/brave/brave-search-mcp-server (Brave Search MCP server, officially maintained)

---

## Related Articles

[[cowork-third-party-inference/overview]] — why third-party inference exists and when to use it

[[cowork-third-party-inference/setup-cloud-openrouter]] — simpler alternative if your machine can't run local models

[[cowork-third-party-inference/gateway-protocol-deep-dive]] — how the Anthropic Messages API works and what your gateway endpoint must implement

[[claude-cowork/_index]] — the parent Cowork topic; this article extends Cowork for offline/private use cases

[[claude-api-cost-optimization/_index]] — local + cloud models are the most extreme cost lever: $0 for Ollama

[[harness-engineering/_index]] — this feature IS the "harness-model separation" thesis made first-party
