# Topics Queue

> Topics waiting for autopilot research routine to process.
> One topic per `## ` heading. Topics are processed top-to-bottom.
> When a topic is completed, move it to the "Completed" section at bottom.
>
> Format per topic:
> - **Query:** the search string handed to yt-search
> - **Notes:** optional hints (specific creators, deliverable type, anchors)
> - **Queued:** date queued
> - **Status:** pending / in-progress / completed

---

## Workflow for AI Coding — champions roundup

- **Query:** `Workflow for AI Coding Matt Pocock Karpathy AI engineer`
- **Notes:** Source video appears to be a "Full Walkthrough" featuring Matt Pocock, Andrej Karpathy and other top AI engineers describing their personal AI-coding workflows. Look for: model choice (Claude/GPT/local), tool stack (Cursor/Claude Code/Aider), context-management strategies, agent vs pair-programming preferences, debugging loops, when-to-trust-AI heuristics.
- **Queued:** 2026-05-07
- **Status:** pending

## How to 10x Claude Code — tips & tricks roundtable

- **Query:** `10x Claude Code tips tricks nateherk EricWTech iamseankochel Boris Chase`
- **Notes:** Roundtable / panel format — @nateherk, @EricWTech, @iamseankochel, Boris (likely Boris from Anthropic / Claude Code team), @Chase-H-AI. Look for: speed multipliers, custom commands, hook patterns, plugin / MCP usage, project-CLAUDE.md tactics, hidden flags, common pitfalls. Cross-reference with existing `wiki/claude-code-hooks/` topic — should produce complementary not duplicate content.
- **Queued:** 2026-05-07
- **Status:** pending

## Telegram bot — remote control Claude Code/Desktop from phone

- **Query:** `Telegram bot Claude Code remote control MCP agent`
- **Notes:** Operator goal — issue commands from phone via Telegram → execute against Claude Desktop or Claude Code on home machine → reply results back. Look for: existing MCP Telegram servers, repo names + maintainers, message → trigger pattern, file/screenshot delivery back to Telegram, multi-tenant vs single-user setups. Highest priority of the remote-control bundle.
- **Queued:** 2026-05-07
- **Status:** pending

## Claude Code SDK — headless / programmatic automation

- **Query:** `Claude Code SDK headless programmatic automation Anthropic`
- **Notes:** Foundation layer for any remote-trigger pattern. Look for: SDK install + auth, programmatic invocation (not interactive), session reuse vs one-shot, output capture (JSON / streamed), system prompt overrides, working-directory control, hook/permission interception. Output should feed the Telegram bot topic above (the bot calls SDK).
- **Queued:** 2026-05-07
- **Status:** pending

## MCP servers for messaging platforms — Telegram, WhatsApp, Discord

- **Query:** `MCP server Telegram WhatsApp Discord messaging integration LLM`
- **Notes:** Comparative scan across 3 platforms to surface alternatives if Telegram-specific server is weak. Look for: bot-API pattern, polling vs webhook, file/voice support, rate-limit behavior, self-host vs hosted, security model (token storage). Output: matrix of which platform suits which use case.
- **Queued:** 2026-05-07
- **Status:** pending

## Remote agent control — tunneling, SSH, ngrok, tailscale

- **Query:** `Run AI agent from phone remote SSH ngrok tailscale tunnel home`
- **Notes:** Networking layer — Telegram bot needs to reach machine at home. Look for: ngrok vs cloudflare tunnel vs tailscale tradeoffs, persistence across reboots, security (auth on tunnel endpoint), latency for interactive commands, free vs paid tiers. Pairs with the Telegram bot topic — tunnel choice affects bot architecture (webhook vs poll).
- **Queued:** 2026-05-07
- **Status:** pending

---

## Completed

_(none yet)_
