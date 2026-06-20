# Cowork on 3P — Overview

**Cowork on 3P** is Anthropic's official third-party inference feature that separates the Claude Desktop harness (Cowork AND Claude Code in Desktop) from the underlying LLM model. It lets you run the full desktop agentic experience with:

- **Local models via Ollama** — $0, fully private, slower (depends on your hardware)
- **Cloud models via OpenRouter** — cheap, privacy depends on provider, faster
- **Other gateways** — LiteLLM, Bedrock, custom deployments
- **Paid Anthropic** — stay on Claude API as baseline

The core thesis (from the video): Anthropic separated the harness from the model to serve enterprise customers who want the desktop app (skills, MCP, web search, scheduled tasks) but must use their own private models or cheaper inference providers.

---

## What's the Same vs. Paid Cowork?

**Same as paid version:**
- Full harness (drag-and-drop interface, projects, context panel, task scheduler, MCP integration)
- Scheduled tasks (fires every N minutes/hours, as long as app is open)
- Skills and plugins (must be manually imported)
- MCP connectors (e.g., Brave Search, custom tools)
- Web search via MCP (not built-in; requires manual wiring)

**Different from paid version:**
- No dispatch button (confirmed limitation; status "not planned" for Claude Code)
- Skills/connectors require manual import (download zip, drag in) vs. pre-provided
- Non-Claude models lack built-in harness training; skills often fail on first attempt, requiring manual error correction
- Scheduled tasks only run while app is open (same as paid, but important constraint)
- Model discovery populates only from your gateway's `/v1/models` endpoint (vs. Anthropic's full model roster)

**NOT supported in Cowork on 3P (as of June 2026):**
- **Claude Code lacks 3P gateway mode entirely** (feature request #52572 closed "not planned"). The 3P gateway is **Cowork-only**; Claude Code only works with Anthropic's paid API or Bedrock/Vertex.

---

## Three Model Sources at a Glance

### Local: Ollama + Gemma or your choice

```
Free + Private: ✓
Speed: Depends on hardware (slow for 26B+)
Data flow: Stays on your machine
Setup: ~10 minutes
```

- Ollama runs models locally on port 11434 (HTTP only by default; requires HTTPS bridge for Anthropic's gateway)
- **Note:** Ollama v0.14.0 (released January 2026) added native Anthropic Messages API support, potentially eliminating the need for a Tailscale bridge. The video (April 2026) predates or does not reference this simpler path; the Tailscale approach remains valid for older Ollama versions.
- Example model: Gemma 4 26B (video claims 18GB, 256K context window; exact specifications not independently verified against Google docs)

**Gotcha:** Non-Claude models don't know how to drive the Cowork harness. Skills often fail or loop. Workaround: run the skill once, let it fail, ask the model to fix itself, re-run.

### Cloud: OpenRouter (aggregator)

```
Cost: Cheap (~$0.06/$0.33 per million tokens for Gemma, per video)
Speed: Much faster than local
Privacy: Depends on provider; OpenRouter itself logs zero by default
Setup: ~5 minutes (create account, add credits, generate API key)
```

- OpenRouter multiplexes 400+ models from 70+ providers via a unified Anthropic-compatible gateway
- Zero Data Retention (ZDR) available to route only to privacy-compliant providers
- Free model tier available but rate-limited and unreliable for production
- Pricing is transparent (no OpenRouter markup); matches provider costs exactly

**Gotcha:** Same as local — non-Claude models struggle with skills.

### Paid: Anthropic API (baseline)

```
Cost: Standard Claude API pricing ($5/million input, ~$15/million output for Opus)
Speed: Fastest (Anthropic's servers)
Privacy: Governed by Anthropic's Privacy Policy
Data governance: Can be routed through Microsoft Foundry (enterprise)
```

Keep paid Cowork as a fallback or for high-stakes tasks where harness reliability matters.

---

## How It Works: The Harness-vs-Model Separation

Anthropic's official architecture:

1. **Enable Developer Mode** → Help > Troubleshooting > Enable Developer Mode
2. **Configure 3P Gateway** → Help > Developer > Configure third-party inference
3. **Provide three fields:**
   - `inferenceGatewayBaseUrl` — your local Ollama or cloud OpenRouter endpoint
   - `inferenceGatewayApiKey` — bearer token (or x-api-key, depending on provider)
   - `inferenceAuthScheme` — bearer or x-api-key
4. **Model discovery** — gateway's GET /v1/models endpoint auto-populates the model picker
5. **Deploy locally or export** — Apply to current machine only, or export as MDM profile (.mobileconfig macOS, .reg Windows) for team rollout

The gateway must implement the Anthropic Messages API: POST /v1/messages (streaming + tool use) + optional GET /v1/models.

---

## Setup Path (Ollama Local Example)

**Install Ollama:**
```bash
brew install ollama  # or download from ollama.com
```

**Download a model:**
```bash
ollama pull gemma4:26b  # or gemma2:2b for smaller hardware
ollama list  # verify
```

**Bridge HTTP→HTTPS (Tailscale method from video):**
```bash
# Enable Tailscale on your machine (free account)
tailscale up

# Serve Ollama over HTTPS via Tailscale
tailscale serve tcp/11434 http://localhost:11434
```

This creates an HTTPS URL in your tailnet (device-name.tailnet-name.ts.net:11434) that the Cowork gateway can reach.

**Alternative (newer Ollama, v0.14.0+, January 2026):**
Ollama added native Anthropic Messages API support. The simpler path may be:
```bash
ollama launch claude-desktop  # may auto-wire the gateway
```
This eliminates the need for the Tailscale HTTPS bridge.

**Configure Cowork 3P:**
- Enable Developer Mode, go to Developer > Configure third-party inference
- Gateway base URL: `https://device-name.tailnet-name.ts.net:11434/v1` (Tailscale path) OR `http://localhost:11434` (if using native Anthropic API support)
- API key: `ollama` (default) or your custom key
- Auth scheme: bearer
- Apply locally

**Test:** Open a new chat, model picker should show Gemma.

---

## Setup Path (OpenRouter Cloud Example)

**Create OpenRouter account:**
- Sign up at openrouter.ai
- Add $10+ credits (prepay model)
- Create API key from API keys page

**Configure Cowork 3P:**
- Gateway base URL: `https://openrouter.ai/api/v1` (note: `/v1` is required)
- API key: your OpenRouter API key
- Auth scheme: x-api-key
- Apply locally

**Test:** Model picker will show available models (Gemma 26B, MiniMax, others).

---

## Adding Skills & Web Search

### Manual skill import (required in 3P)

Unlike paid Cowork, skills don't auto-load. To import:

1. Download `anthropics/skills` GitHub repo as ZIP
2. Unpack, select the skill folder (e.g., `docx/`)
3. Right-click → Compress → Create a new ZIP
4. Drag the ZIP into Cowork
5. Restart app if needed

Repeat for each skill (PDF, Excel, PowerPoint, etc.).

### Web search via MCP (required in 3P)

Non-Claude models lack built-in web_search tool. Add Brave Search:

1. Go to Settings > Developer > add MCP server
2. Copy Brave Search NPX command: `npx -y @brave/brave-search-mcp-server`
3. Acquire Brave API key from brave.com/search/api
4. Configure MCP in Claude Desktop config file with API key
5. In Sandbox/Workspace settings, disable the built-in `web_search` tool (so model doesn't try to call the non-existent Claude-native tool)

---

## Key Gotchas

### 1. Non-Claude models don't know the harness

The Cowork desktop app has underlying system prompting + configuration tuned for Claude models. When you swap in Gemma, Llama, or MiniMax, they see the same harness prompts but aren't trained to interpret them. Result: **skills fail or loop on first attempt.**

**Workaround:** Run the skill once, observe the failure, ask the model to fix itself, re-run. The model can learn from one example. Not ideal, but functional.

### 2. Scheduled tasks only run while app is open

There is no background daemon or "always on" execution. If you close Cowork, scheduled tasks stop. This applies to both 3P and paid Cowork.

### 3. Model discovery is picky

The model picker auto-populates only models returned by your gateway's `/v1/models` endpoint AND with Claude-recognizable IDs. If a model doesn't show up, you may need to explicitly list it in `inferenceModels` config field (advanced).

### 4. Privacy depends on your gateway

- **Local Ollama + Tailscale Serve:** All traffic stays in your tailnet (private). But Tailscale sees the encrypted packets.
- **OpenRouter:** OpenRouter itself logs zero prompts by default (unless you opt-in for 1% discount). BUT the underlying provider (Google Gemma, etc.) sees the data. Use ZDR feature to route only to privacy-approved providers.
- **Custom private gateway:** Depends on who runs it and where data flows.

Anthropic's official disclaimer: "Data handling is otherwise determined by the gateway you operate and the upstream provider it routes to."

---

## Enterprise (MDM) Deployment

Export your 3P gateway configuration as a managed profile:

- **macOS:** Export as `.mobileconfig`, deploy via MDM (e.g., Jamf, Kandji)
- **Windows:** Export as `.reg`, deploy via Group Policy

This lets IT teams standardize Cowork on 3P across the organization without per-machine setup.

---

## Key Takeaways

- Cowork on 3P is first-party Anthropic, not a workaround or hack.
- It enables three deployment modes (local free, cloud cheap, paid Claude) switchable on the fly within the same harness.
- **Local Ollama = $0 + fully private,** but slower and non-Claude models struggle with skills (fixable via one-shot failure + correction loop).
- **OpenRouter = fast + cheap,** but data leaves your machine; use ZDR for privacy.
- Per the video, Anthropic may have developed this feature for enterprise customers wanting harness + private models, but this interpretation is not confirmed by first-party documentation.
- The "~90% feature parity" claim from the video is the speaker's estimate, not documented by Anthropic.
- Skills and MCP connectors require manual import in 3P, unlike paid Cowork.
- Scheduled tasks only run while app is open.
- **Dispatch button is not available** in Cowork on 3P.
- **Claude Code does NOT support 3P gateways** (Cowork-only feature as of June 2026).
- Enterprise teams can MDM-deploy via `.mobileconfig` or `.reg` exports.
- Ollama v0.14.0+ (January 2026) added native Anthropic API support, potentially simplifying setup without Tailscale.

---

## Source

- Primary: Bart Slodyczka, "Claude Cowork + Ollama = 100% FREE & PRIVATE (Full Setup)", YouTube ME4flXK_6tQ (published 2026-04-25, 18:41, ~47K views)
  - Transcript: `raw/(C) 2026-06-20-cowork-ollama-3p-local-private.md`
- First-party Anthropic: https://claude.com/docs/cowork/3p/gateway
- First-party Anthropic: https://claude.com/docs/cowork/3p
- Ollama: https://github.com/ollama/ollama (v0.14.0 release notes, January 2026, for native Anthropic Messages API support)
- Tailscale: https://tailscale.com/kb/1312/serve
- OpenRouter: https://openrouter.ai/docs/api/reference/authentication
- GitHub issue (Claude Code 3P support status): https://github.com/anthropics/claude-code/issues/52572
