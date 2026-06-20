# Deep-dive: the Cowork-on-3P gateway protocol (original resource #1)

This is the **authoritative reference** for Anthropic's third-party inference gateway protocol that Cowork on 3P implements. This article covers the API contract, configuration surface, model discovery, deployment modes, and documented gateways. It is foundational to understanding how to wire local/cloud models into Claude Desktop.

## What is Cowork on 3P?

Cowork on 3P (third-party inference) is Anthropic's official feature that separates the **harness** (the desktop app: tasks, skills, context panel, scheduling) from the **model** (the LLM providing completions). This enables enterprises to use Anthropic's desktop harness with their own private models (local or cloud) instead of Anthropic's cloud API.

The "3P" prefix designates **third-party inference provider**, distinguishing it from the paid 1P (Anthropic's own API) mode.

## Enabling Cowork on 3P

**In Claude Desktop:**

1. **Help** → **Troubleshooting** → **Enable Developer Mode**
2. **Help** → **Developer** → **Configure third-party inference**
3. Select **Gateway** as the connection type
4. Fill in three required fields (see "Configuration keys" below)
5. **Apply locally** (single machine) or **Export** as MDM profile for team rollout

Once enabled, the model picker shows all models returned by the gateway's `/v1/models` endpoint (if implemented).

## Gateway API contract

The gateway endpoint MUST implement the Anthropic Messages API. This is the **load-bearing requirement**.

### POST /v1/messages (streaming + tool use)

- **Protocol**: HTTP POST with JSON body
- **Authentication**: Bearer token (Authorization: Bearer <key>) OR x-api-key header (X-API-Key: <key>)
- **Request body**: Standard Anthropic Messages API format (system, messages, model, max_tokens, tools, etc.)
- **Response**: Streaming JSON (Server-Sent Events), identical to Anthropic's API
- **Tool use**: Must support tool_use blocks and tool results in the message stream
- **Streaming**: Required. Cowork does not poll; it expects Server-Sent Events

**Example**: POST to `https://your-gateway.example.com/v1/messages` with the same request shape as `https://api.anthropic.com/v1/messages`.

### GET /v1/models (optional auto-discovery)

- **Protocol**: HTTP GET
- **Response**: JSON array of model objects with `id` and `name` fields
- **Model ID matching**: Only models with recognizably-Claude IDs surface in the picker (e.g., `claude-3-sonnet`, not arbitrary names)
- **Override**: If the gateway does NOT implement `/v1/models`, you can manually specify models via the `inferenceModels` config key

**Example response**:
```json
[
  {"id": "claude-3-5-sonnet-20241022", "name": "Claude 3.5 Sonnet"},
  {"id": "gemma-2-9b", "name": "Gemma 2 9B"}
]
```

Only the first model (claude-3-5-sonnet-...) will auto-populate in the picker unless you use `inferenceModels` to whitelist gemma-2-9b.

## Configuration keys

These are the values you enter in the Claude Desktop Developer panel:

| Key | Required | Type | Purpose |
|---|---|---|---|
| `inferenceGatewayBaseUrl` | Yes | URL string | Base endpoint of your gateway, e.g., `https://ollama.tailnet-name.ts.net:11434` or `https://openrouter.ai/api/v1` |
| `inferenceGatewayApiKey` | Yes | Secret string | API key for the gateway. Can be a default like "Ollama" if the gateway doesn't enforce authentication. |
| `inferenceGatewayAuthScheme` | Yes | Enum: `bearer` or `x-api-key` | Auth header format. Most gateways (Ollama, OpenRouter) use `bearer` token. Some legacy systems use `x-api-key`. |
| `inferenceModels` | No | JSON array | Optional whitelist of model IDs to display in the picker, overriding auto-discovery. Example: `["gemma-4-26b", "llama2-70b"]`. |
| `inferenceCustomHeaders` | No | JSON object | Optional custom HTTP headers to include in every request (e.g., for additional auth, routing, telemetry). |

**Example configuration** (as written in the Claude Desktop UI):
- URL: `https://ollama.my-tailnet.ts.net:11434`
- API key: `ollama`
- Auth scheme: `bearer`
- Models override: (leave blank to auto-discover)

## Model discovery and naming

### Auto-discovery via /v1/models

If your gateway implements `GET /v1/models`, Cowork queries it on startup and on model picker load. The response is filtered to show **only models with Claude-like names** (ID strings that match the pattern "claude-...").

Non-Claude model IDs (e.g., `gemma-4-26b`) are **silently filtered out** unless you explicitly whitelist them via `inferenceModels`.

### Bypassing auto-discovery

If your gateway does not implement `/v1/models` or returns opaque model IDs, you can force-populate the picker with `inferenceModels`:

```json
{
  "inferenceModels": [
    "gemma-4-26b-a4b-it",
    "llama2-13b-chat",
    "mistral-7b-instruct"
  ]
}
```

Cowork will display these models in the picker regardless of whether they match Claude naming conventions or appear in `/v1/models`.

## Data handling and privacy

From Anthropic's first-party docs:

> "Data handling is otherwise determined by the gateway you operate and the upstream provider it routes to."

**Critical implication**: Anthropic makes NO privacy guarantees for Cowork on 3P. If you run a local Ollama instance, data stays on your machine (local network only, with zero cloud ingress). If you point to a cloud gateway like OpenRouter, data leaves your machine and is subject to that provider's data retention policy, independent of Anthropic's.

**Cowork itself does NOT log or retain prompts/completions** when using a third-party gateway (distinct from the 1P paid mode, where Anthropic retains data per contract). The privacy boundary is **between your machine and the gateway**, not between your machine and Anthropic.

## Deployment modes

### Apply locally

Configuration applies to **this machine only**. Useful for personal laptops. Requires Claude Desktop to be running on the same device as the gateway.

### Export as MDM profile

Configuration exports as:
- **macOS**: `.mobileconfig` XML file for Apple Mobile Device Management
- **Windows**: `.reg` registry export file for Group Policy

Allows IT/DevOps teams to push the gateway configuration to all machines in an organization via MDM without manual per-machine setup.

## Gateways implementing this protocol

The following systems are documented or verified to implement the Anthropic Messages API and work with Cowork on 3P:

| Gateway | Purpose | Auth | Notes |
|---|---|---|---|
| **Ollama** | Local model server | Bearer (`ollama` default) | HTTP only by default; requires HTTPS bridge (Tailscale Serve, Caddy, nginx) for Cowork 3P. As of January 2026 (v0.14.0), Ollama supports native Anthropic Messages API and can be wired directly via environment variables for Claude Code. Gemma, Llama, Mistral models. |
| **OpenRouter** | Multi-provider aggregator | Bearer token | Cloud. 400+ models from 70+ providers. Zero Data Retention (ZDR) option for privacy-sensitive use. |
| **LiteLLM** | Open-source gateway proxy | Bearer token (configurable) | Supports 100+ LLM providers (Bedrock, Vertex, Ollama, OpenAI, etc.). Self-hosted or cloud. |
| **Portkey** | Enterprise gateway | Bearer token | Multi-provider load-balancing + fallback. Self-hosted or SaaS. |
| **GitHub Copilot API** | Microsoft/OpenAI gateway | Bearer token | Undocumented third-party support; feature request pending. |
| **AWS Bedrock** | Amazon managed models | Bearer token + AWS auth | Requires AWS credentials + IAM role. |
| **Google Vertex AI** | Google managed models | Bearer token + Google auth | Requires Google credentials. |

**Note**: Ollama, OpenRouter, and LiteLLM are the most battle-tested with Cowork on 3P as of June 2026.

## Documented limitations

### 1. Claude Code does NOT support 3P gateway mode

Claude Code (the command-line coding agent in Claude Desktop) does not accept `inferenceGatewayBaseUrl` or related 3P config keys. Feature request [anthropics/claude-code#52572](https://github.com/anthropics/claude-code/issues/52572) was closed as "not planned" (as of June 2026). This means you can run Cowork on 3P with local/cloud models, but Claude Code will only work with paid Anthropic API.

### 2. No dispatch button in 3P mode

The "Dispatch" button (run a task on any device immediately, no scheduling) is not available in Cowork on 3P. This is documented behavior, not a bug. Dispatch requires Anthropic's infrastructure.

### 3. Scheduled tasks require app-open

Scheduled tasks in Cowork on 3P only run while Claude Desktop is open on the machine where the gateway is configured. There is no background service or daemon mode. This mirrors the 1P (paid) behavior.

### 4. Non-Claude models lack harness training

Third-party models (Gemma, Llama, Mistral, etc.) are not trained on the Claude Desktop harness's system prompting and underlying configuration. As a result:

- Skills often fail on first attempt (the model doesn't know the harness API)
- Workaround: run a skill once, inspect the failure, ask the model to fix itself, then re-run
- This is a **fundamental training gap**, not a configuration issue

### 5. Non-Claude models lack built-in web_search

Only Anthropic's Claude models have the built-in `web_search` tool. For local/cloud models, you must:
- Disable the built-in web_search tool in Sandbox/Workspace settings
- Add a web search MCP server (Brave Search recommended)
- Configure the MCP server in Claude Desktop's `claude_desktop_config.json`

## Skills, plugins, and MCP in 3P mode

### Manual skill import (difference from 1P)

In **paid Cowork (1P mode)**: Skills and Plugins are pre-provided via Anthropic's skill library.

In **Cowork on 3P**: You must manually import skills:

1. Clone/download [anthropics/skills](https://github.com/anthropics/skills) from GitHub
2. Right-click the individual skill folder (e.g., `pptx/`, `pdf/`) and compress it to a zip file
3. Drag the zip file into Claude Desktop
4. Cowork parses the zip and adds the skill to the picker

This is by design — 3P gateways may not have access to Anthropic's skill definitions (security boundary).

### MCP servers (connectors)

Model Context Protocol (MCP) servers are wired via `claude_desktop_config.json` and work identically in 3P and 1P modes. Examples:

- **Brave Search MCP**: add web search capability to any model
- **File system MCP**: read/write files in a sandboxed directory
- **PostgreSQL MCP**: query databases

MCP configuration is **not enforced** by the gateway protocol; it's a Claude Desktop feature. You can use MCP servers with any third-party model.

## How the gateway protocol differs from other backend modes

Cowork on 3P supports three inference modes in the UI:

| Mode | Provider | Harness | Privacy | Use case |
|---|---|---|---|---|
| **1P (Anthropic)** | Anthropic cloud API | Claude Desktop | Anthropic retains data per terms | Paid users, maximum capability |
| **3P Gateway** | Your gateway (local or cloud) | Claude Desktop | Gateway determines retention | Enterprises, BYOM, cost-conscious |
| **Claude Code (CLI)** | Anthropic cloud API | terminal-only | Anthropic retains data | Developers, scripting, no GUI |

The **harness** (Cowork desktop app) is identical between 1P and 3P. The **model backend** is swappable. Claude Code is a separate product with its own limitations.

## Example: wiring Ollama to Cowork on 3P

From the video [Bart Slodyczka, "Claude Cowork + Ollama = 100% FREE & PRIVATE"](https://www.youtube.com/watch?v=ME4flXK_6tQ):

1. **Install Ollama** locally (brew, direct download, or Docker)
2. **Download a model**: `ollama pull gemma2:13b`
3. **Expose Ollama as HTTPS** (Ollama defaults to HTTP on port 11434):
   - **Option A (video method, April 2026)**: Use Tailscale Serve: `tailscale serve https / http://localhost:11434` (generates `https://device-name.tailnet-name.ts.net:443`)
   - **Option B (simpler, January 2026+ native path)**: Ollama v0.14.0 added native Anthropic Messages API support; set `ANTHROPIC_BASE_URL=http://localhost:11434` environment variable for Claude Code and use http://localhost:11434 in Cowork 3P gateway config (HTTP accepted for local gateways in development mode per Anthropic docs)
4. **Configure in Cowork on 3P**:
   - URL: `https://device-name.tailnet-name.ts.net` (or `http://localhost:11434` if using native path)
   - API key: `ollama` (default)
   - Auth scheme: `bearer`
5. **Apply locally**
6. **Model picker populates** with available models (or manually add via `inferenceModels` if not auto-discovered)

## Example: wiring OpenRouter to Cowork on 3P

From the same video:

1. **Create OpenRouter account** and generate an API key at [openrouter.ai/keys](https://openrouter.ai/keys)
2. **Configure in Cowork on 3P**:
   - URL: `https://openrouter.ai/api/v1`
   - API key: your OpenRouter API key
   - Auth scheme: `bearer`
3. **Optionally whitelist models** via `inferenceModels` if auto-discovery fails or returns too many
4. **Apply locally** or export as MDM profile for team deployment
5. **Model picker populates** with all available OpenRouter models (Gemma, Llama, Mistral, etc.)

**Privacy note**: OpenRouter does NOT log or train on prompts by default. However, underlying model providers (Google for Gemma, Meta for Llama) maintain separate data policies. Use OpenRouter's Zero Data Retention (ZDR) feature if you require strict no-logging guarantees.

## Key Takeaways

- **Cowork on 3P** is Anthropic's official harness-model separation feature, enabled via Developer menu in Claude Desktop.
- **Gateway protocol** requires HTTP POST `/v1/messages` (streaming, tool use) and optionally GET `/v1/models` for auto-discovery.
- **Configuration** is three fields: base URL, API key, auth scheme. Optional: model whitelist and custom headers.
- **Model discovery** filters to Claude-like IDs by default; override with `inferenceModels` to support Gemma, Llama, etc.
- **Data privacy** is determined by YOUR gateway, not Anthropic. Local Ollama = private. Cloud gateways = subject to provider's policy.
- **Deployment**: single-machine ("Apply locally") or enterprise-wide MDM profiles (.mobileconfig / .reg).
- **Claude Code is NOT supported** in 3P mode (as of June 2026); only Cowork desktop app.
- **Non-Claude models** lack harness training, requiring skill re-authoring after first failure.
- **Skills must be manually imported** in 3P (zip + drag), unlike 1P where they are pre-provided.
- **Web search requires MCP** for non-Claude models (Brave Search recommended); disable built-in web_search tool to avoid routing errors.
- **Ollama HTTPS bridge is optional** as of January 2026 (v0.14.0 native Anthropic API support); Tailscale is ONE approach but not the only one for development setups.

## Source

- **Anthropic official docs**: [claude.com/docs/cowork/3p/gateway](https://claude.com/docs/cowork/3p/gateway) — the authoritative gateway configuration reference
- **Anthropic Cowork overview**: [claude.com/docs/cowork/3p](https://claude.com/docs/cowork/3p)
- **Anthropic Cowork main**: [claude.com/docs/cowork](https://claude.com/docs/cowork)
- **GitHub issue #52572**: [anthropics/claude-code](https://github.com/anthropics/claude-code/issues/52572) — documents Claude Code 3P non-support
- **GitHub issue #54214**: [anthropics/claude-code](https://github.com/anthropics/claude-code/issues/54214) — documents dispatch button unavailability
- **Ollama v0.14.0 release**: [github.com/ollama/ollama](https://github.com/ollama/ollama/releases/tag/v0.14.0) — native Anthropic Messages API support (January 10, 2026)
- **Video transcript**: [[cowork-third-party-inference/video-to-original-crosswalk]] references `/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/(C) 2026-06-20-cowork-ollama-3p-local-private.md`
- **Video**: Bart Slodyczka, "Claude Cowork + Ollama = 100% FREE & PRIVATE (Full Setup)", YouTube ME4flXK_6tQ, published 2026-04-25

## Related articles

- [[cowork-third-party-inference/overview]] — What is Cowork on 3P and when to use it
- [[cowork-third-party-inference/setup-local-ollama]] — Step-by-step Ollama + Tailscale bridge setup
- [[cowork-third-party-inference/setup-cloud-openrouter]] — Step-by-step OpenRouter configuration
- [[claude-cowork/_index]] — Parent topic: Cowork scheduling, skills, connectors
- [[claude-api-cost-optimization/_index]] — Cost implications of local vs. cloud inference
- [[harness-engineering/_index]] — Harness-model separation thesis and architectural implications
