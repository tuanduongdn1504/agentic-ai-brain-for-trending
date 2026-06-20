# Deep-dive: Ollama as a local inference server

## Overview

Ollama is an open-source model server that runs large language models (LLMs) locally on your machine via HTTP on port 11434. It is the primary vehicle for running local models with Claude Cowork on 3P (third-party inference gateway), enabling 100% private inference without cloud routing or per-token costs. This deep-dive covers installation, model management, API compatibility, and the privacy guarantees of the local execution model.

## Source

- **Primary video transcript:** `/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/(C) 2026-06-20-cowork-ollama-3p-local-private.md` (Bart Slodyczka video, YouTube ME4flXK_6tQ, 2026-04-25, 18:41)
- **First-party docs:**
  - https://github.com/ollama/ollama (repository + releases)
  - https://github.com/ollama/ollama/releases/tag/v0.14.0 (Anthropic Messages API support announcement, Jan 10, 2026)
  - https://docs.ollama.com/api (Ollama API reference)
  - https://docs.ollama.com/integrations/claude-code (Ollama + Claude Code integration guide)
  - https://claude.com/docs/cowork/3p/gateway (Anthropic Cowork on 3P gateway configuration)
  - https://tailscale.com/kb/1312/serve (Tailscale Serve documentation)
- **Video timestamps:** [06:50-07:18] (HTTP-only default, HTTPS bridge need); [06:23-06:32] (LM Studio alternative); [06:50] (Ollama pull/list commands)

## Installation & Setup

### Install Ollama

The video demonstrates terminal-based installation via a curl command. Ollama also offers a GUI app download from https://ollama.com.

```bash
# Terminal install (Mac/Linux)
curl -fsSL https://ollama.ai/install.sh | sh

# Or install from GUI app (https://ollama.com)
# Downloads available for macOS, Windows (beta), and Linux
```

The video shows the author re-installing a newer version to ensure Anthropic API compatibility.

### Launch the Ollama daemon

Once installed, Ollama serves on `http://localhost:11434` by default (HTTP only, no native HTTPS).

```bash
# Ollama daemon runs automatically on install (background service on macOS/Windows)
# To manually start: just open the Ollama app or run `ollama serve`
```

## Model Management

Ollama provides CLI commands to download, list, and run models. The video demonstrates these with Gemma models.

### Pull a model

```bash
ollama pull gemma:4-26b-a4b-it    # Downloads Gemma 4 26B variant
ollama pull gemma2:2b             # Downloads Gemma 2 2B (lighter)
```

Model downloads are stored in `~/.ollama/models/`. Sizes vary by quantization. The video claims Gemma 4 26B is approximately 18GB (full model); actual download size depends on the quantization variant selected.

### List installed models

```bash
ollama list    # Shows all downloaded models, their sizes, and last-modified dates
```

Example output:
```
NAME                 ID              SIZE    MODIFIED
gemma:4-26b-a4b-it   1234567890ab    18GB    2026-06-20 10:15:00
gemma2:2b            abcdef123456    1.6GB   2026-06-20 10:12:00
```

### Run a model

```bash
ollama run gemma:4-26b-a4b-it      # Interactive chat with the model
# Ctrl+D or Ctrl+C to exit
```

## API Compatibility

### OpenAI-compatible API (HTTP endpoint)

Ollama exposes an HTTP API at `http://localhost:11434/v1/` that is compatible with OpenAI's API specification. This endpoint supports:

- **POST `/v1/messages`** — Anthropic Messages API (as of v0.14.0, January 2026)
- **GET `/v1/models`** — List available models for auto-discovery
- **POST `/v1/completions`** — OpenAI-style completions (older spec)

The video demonstrates the `/v1/` endpoint path but does not explicitly show API calls; instead, it uses Ollama as a backend for Cowork on 3P gateway configuration.

### Native Anthropic Messages API support

**Important evolution:** Ollama v0.14.0 (released January 10, 2026, before the video's April 25, 2026 publication) added **native Anthropic Messages API support**. This means:

- Ollama now natively implements POST `/v1/messages` with streaming and tool use support
- Claude Desktop can be configured to point directly at Ollama via the third-party inference gateway
- The command `ollama launch claude-desktop` reportedly automates the gateway wiring (May 2026 post-video development)

**What this means for the video:** The video uses a Tailscale HTTPS bridge workaround because Ollama's default HTTP endpoint requires HTTPS for Anthropic's gateway. However, as of v0.14.0, the simpler `ollama launch claude-desktop` command may eliminate this need. The video (April 25, 2026) predates or does not reference this evolution.

### HTTP-only limitation

Ollama serves HTTP (port 11434) by default; it does NOT natively provide HTTPS. The video states:

> "Ollama comes with a default URL that we can use to tap into our model, but that URL has a HTTP connection. And for Anthropic, in order for us to use a third-party model, we actually need a HTTPS connection, which is a secure connection. Now, unfortunately, Ollama doesn't natively give the HTTPS connection."

**Workaround (video's approach):** Use Tailscale Serve to bridge HTTP → HTTPS (see [[cowork-third-party-inference/tailscale-https-bridge]]).

**Simpler alternative (post-video):** Ollama v0.14.0+ implements native Anthropic API support; check current Ollama documentation for HTTPS-in-the-box solutions or use environment variables to set `ANTHROPIC_BASE_URL=http://localhost:11434` for local-only development.

## Model Library

### Gemma models

The video focuses on Gemma models (Google's open-source family):

| Model | Size (approx.) | Context | Notes from video |
|---|---|---|---|
| Gemma 4 26B | ~18 GB (full) | 256K | Full-size variant; slower on consumer hardware |
| Gemma 2 2B | ~1.6 GB | Not stated | Lightweight alternative |
| Gemma E2B | [unverified] | Not stated | Edge variant; speaker claims 7.2 GB (unverified) |

**Note on sizes:** The video quotes "Gemma 26B is 18 gigs" (confirmed for full Gemma 4 26B A4B) and "Gemma E2B is 7.2 gigs," but the E2B figure does not align with published specifications. Standard Ollama quantized variants (Q4_0, Q5_K_M) are smaller than full-precision models. Users should check the Ollama library for actual download sizes before pulling: https://ollama.com/library.

### Other models available

Ollama's library includes:

- **Llama 2/3** (Meta's open-source family)
- **Mistral** (European open-source family)
- **Neural Chat** (Intel)
- **Orca** (Microsoft)
- Hundreds of other quantized and fine-tuned variants

Browse the full library at https://ollama.com/library.

## Quantization & Resource Requirements

The video does not deeply cover quantization, but it is essential for understanding model sizes and RAM requirements.

**Quantization rule of thumb:** Lower-bit quantizations (Q4_0, Q5_K_M) use ~25-50% of the full model's VRAM. Example:

- **Gemma 4 26B full precision (FP32):** ~104 GB VRAM needed
- **Gemma 4 26B Q4_0 quantized:** ~8-12 GB VRAM needed (typical consumer GPU range)

Ollama automatically uses quantized versions from its library unless you explicitly pull the full-precision variant. The `ollama list` command shows the actual file size.

## Alternatives to Ollama

The video briefly mentions **LM Studio** as an alternative:

> "There are alternatives to using Ollama. You can use something called LM Studio. Once you download this app and you browse AI models, LM Studio will be able to read your device and understand what kind of models you can run and it's either going to say, 'Yep, you can run this model on your computer.' or 'No, this is too big to run.'"

**LM Studio advantages:**
- GUI-based (no terminal required)
- Auto-detects hardware constraints
- Simpler for non-technical users

**Other alternatives:**
- **llama.cpp** (command-line inference engine, C++)
- **vLLM** (high-throughput inference framework, more complex)
- **Text Generation WebUI** (feature-rich UI wrapper)

Ollama remains the simplest bridge to Claude Desktop because of explicit first-party Anthropic integration (v0.14.0+).

## Privacy: Traffic stays local

When using local Ollama (not routed through OpenRouter or other cloud services), the privacy guarantee is simple:

- **All inference traffic stays on your machine.** No data leaves your computer.
- **Ollama daemon is localhost-only by default.** It does not expose to the public internet.
- **Tailscale bridge keeps traffic inside your tailnet.** When using Tailscale Serve to generate HTTPS, traffic is encrypted and routed only within your Tailscale network (not exposed to Tailscale's cloud).

The video emphasizes:

> "This means you could use something like Ollama to then download a free local AI model onto your computer... I'm going to show you how to use Claude CoWork completely for free and 100% privately by using a local AI model that you're running on your computer."

**Important caveat:** This is true ONLY for local Ollama. If you route Ollama through a cloud service (e.g., via ngrok public tunnel or OpenRouter), traffic is no longer private.

## HTTPS Gap & Native Anthropic API

### The video's context (April 2026)

At the time of the video, Ollama defaulted to HTTP on port 11434 and lacked explicit native Anthropic Messages API support (or the support existed but was not documented/highlighted). The video's solution was:

1. Run Ollama on `http://localhost:11434/v1/`
2. Use Tailscale Serve to wrap it in HTTPS
3. Configure Cowork on 3P to point at the Tailscale HTTPS URL

### Post-video evolution (January 2026 → now)

Ollama v0.14.0 (released January 10, 2026, BEFORE the video) implemented native Anthropic Messages API support. This means:

- Ollama now natively implements `/v1/messages` endpoint compatible with Anthropic's gateway requirements
- The `ollama launch claude-desktop` command (May 2026) reportedly automates the setup
- Developers can now point Claude Desktop directly at `http://localhost:11434` for local development

**Implication:** The Tailscale Serve workaround in the video may no longer be necessary. New users should check current Ollama documentation before following the video's manual HTTPS-bridge approach.

## Integration with Claude Desktop & Claude Code

### Claude Desktop (Cowork on 3P)

Claude Desktop can be configured to use Ollama as a third-party inference provider via the gateway feature:

1. Enable Developer Mode in Claude Desktop (Help > Troubleshooting > Enable Developer Mode)
2. Go to Developer > Configure third-party inference
3. Enter Ollama's base URL (`http://localhost:11434` or Tailscale HTTPS bridge)
4. Set API key (can be `Ollama` as a placeholder)
5. Choose Bearer token auth

Once configured, Cowork on 3P uses Ollama models for all tasks (conversations, skills, web search via MCP).

### Claude Code (command-line)

Claude Code can integrate with Ollama using environment variables:

```bash
export ANTHROPIC_BASE_URL=http://localhost:11434/v1/
export ANTHROPIC_AUTH_TOKEN=ollama
claude code <file-or-query>
```

However, the video does not explicitly cover Claude Code with Ollama; it focuses on Cowork on 3P (desktop app).

## Model Context Protocol (MCP) servers with Ollama

When using non-Claude models (Gemma, Llama, etc.), they lack native integration with Claude Desktop's built-in tools. To add capabilities like web search, you must use MCP servers:

### Brave Search MCP example

```bash
npx -y @brave/brave-search-mcp-server
```

Configure in `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@brave/brave-search-mcp-server"],
      "env": {
        "BRAVE_API_KEY": "your-api-key"
      }
    }
  }
}
```

The video demonstrates this for restoring web search to local/cloud models. Brave Search MCP free tier allows 2,000 queries per month.

## Skill Execution & Harness Limitations

A key limitation discovered in the video: **non-Claude models struggle to execute Cowork skills** because they are not trained on the underlying Claude Desktop harness system prompting.

The video states:

> "The cloud model here is not necessarily trained on the like how to use the Claude desktop app. There's a lot of underlying configuration, underlying prompting, that is actually sent with each request. So, when you're using Opus or Sonnet, those models know how to interact with this harness, with this Claude desktop app."

**Workaround:** Run the skill once, let it fail, inspect the error, ask the model to amend the skill, then re-run.

This limitation does NOT apply to Claude models (Opus, Sonnet) because they have built-in training on the Cowork harness.

## Cost & Speed Tradeoffs

### Ollama (local)

- **Cost:** Free (after hardware investment)
- **Speed:** Slow (depends on GPU/CPU; typically 5-50 tokens/sec on consumer hardware)
- **Privacy:** Excellent (100% local)
- **Skill compatibility:** Poor (non-Claude models struggle with harness)

### OpenRouter (cloud models via gateway)

- **Cost:** Cheap (e.g., Gemma 26B $0.06/M input, $0.33/M output per the video — **pricing not independently verified as current**)
- **Speed:** Fast (cloud-grade GPUs)
- **Privacy:** Moderate (OpenRouter sees requests; use Zero Data Retention controls)
- **Skill compatibility:** Moderate (non-Claude models still struggle; depends on model)

### Anthropic API (paid Cowork)

- **Cost:** Higher per-token (Opus 4 / Sonnet 4.5)
- **Speed:** Fast (enterprise infrastructure)
- **Privacy:** Anthropic's standard (data retention policies apply)
- **Skill compatibility:** Excellent (models trained on Cowork harness)

The video's thesis: **local Ollama is free and private, but slow and skill-limited.** Cloud models (OpenRouter) are faster but less private. Paid Cowork is the gold standard for skill execution but costs more.

## Key Takeaways

- **Ollama runs LLMs locally on port 11434 (HTTP only).** It is the simplest way to run private, on-device inference with Claude Cowork.
- **Ollama v0.14.0+ (January 2026) added native Anthropic Messages API support,** eliminating the need for HTTP→HTTPS translation layers for new setups; the video's Tailscale bridge approach may no longer be necessary.
- **Model management is simple:** `ollama pull <model>`, `ollama list`, `ollama run <model>`. Gemma and Llama models are popular; check actual download sizes in the library before pulling.
- **HTTPS gap:** Ollama defaults to HTTP; the video's Tailscale Serve workaround keeps traffic private within your tailnet but adds complexity. Modern Ollama may offer simpler native HTTPS alternatives.
- **Privacy is excellent for local Ollama** — no data leaves your machine. Traffic stays on localhost (or inside your Tailscale network if using Serve).
- **Non-Claude models struggle with Cowork skills** because they lack training on the desktop harness's system prompting. Workaround: run once, inspect failure, ask model to fix, re-run.
- **Alternatives exist** (LM Studio, llama.cpp, vLLM) but Ollama remains the simplest bridge to Claude Desktop's third-party inference gateway.
- **Cost is zero after hardware investment**, making Ollama ideal for users with powerful enough machines. Speed is the main tradeoff (slower than cloud).
- **MCP servers (Brave Search, etc.) restore missing capabilities** to non-Claude models by adding web search and other integrations.
- **Quantization matters:** Smaller quantizations (Q4_0) fit in consumer VRAM; check Ollama library for actual sizes before pulling a model.

## Related articles

- [[cowork-third-party-inference/tailscale-https-bridge]] — HTTPS bridge workaround (video's approach)
- [[cowork-third-party-inference/skills-mcp-websearch-byom]] — Restoring web search to local models
- [[claude-cowork/_index]] — Parent topic: Cowork scheduling agent + harness
- [[claude-api-cost-optimization/_index]] — Cost levers: local models are the extreme (free)
- [[harness-engineering/_index]] — Harness vs model decoupling: this feature IS that thesis
