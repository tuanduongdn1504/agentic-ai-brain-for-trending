# Layer 3 — Integration (MCP / Channels / fastmcp)

How Claude reaches out to external tools — Telegram bot APIs, file systems, browsers, databases. This layer is mostly **Model Context Protocol (MCP)** as of 2026.

## MCP — "USB-C for AI applications"

IBM Technology's framing: MCP is the standardized way agents connect to external data sources and tools. Replaces one-off custom adapters.

### Core advantages
- **Dynamic discovery:** an agent asks an MCP server "what can you do?" at runtime. New capabilities show up without retraining or redeployment.
- **Standardized:** same protocol whether you're connecting Slack, Postgres, GitHub, or your custom internal tool.
- **Decoupled:** agents and tools can evolve independently.

### Three pieces (Michele Torti's framing)
- **Skills** = instructions (markdown SOPs loaded into context)
- **MCPs** = a "new pair of hands" (the agent gets new abilities to manipulate the world)
- **Hooks** = guardrails (deterministic shell scripts on lifecycle events — see [[../claude-code-hooks/_index|Claude Code hooks]])

This is a useful taxonomy. Skills tell the agent **how**, MCPs tell the agent **what's possible**, Hooks tell the agent **what's not allowed**.

## Three flavors of MCP integration for Telegram remote-control

### Flavor 3A — Official Channels plugins (recommended)
The plugins behind `claude --channels`:
- `claude-code-telegram-plugin-official`
- `claude-code-discord-plugin-official` (or similar — check current plugin registry)

These wrap a Telegram/Discord client + an MCP server in one install. You get:
- Bot listener (Layer 1)
- Tool exposure to Claude (Layer 3 mechanics)
- Allow-list / access policy (security)
- Auto-approve toggles (convenience)

**This is the path of least resistance.** Pick this unless you have a specific reason to roll your own.

### Flavor 3B — Custom Python MCP via `fastmcp`
Samir Kharel's approach: build a tiny MCP server in Python with the `fastmcp` library that bridges Claude Desktop to whatever messaging platform you need.

```python
# pseudocode (verify against current fastmcp docs)
from fastmcp import FastMCP

mcp = FastMCP("custom-bridge")

@mcp.tool()
def send_message(channel: str, text: str) -> str:
    """Send a message to the given channel."""
    # call platform API
    return "sent"

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

Then register it in `claude_desktop_config.json` (Claude Desktop) or `mcp.json` (Claude Code). Claude communicates via stdin/stdout.

**When to pick:**
- You need a platform Channels doesn't support (Slack, Teams, Signal, internal IM)
- You need custom IAM logic (per-command permissions, audit logging)
- You're already in Python and want full control

**When NOT to pick:**
- You'd be building maintenance burden for something Channels already does
- Your team has no Python ownership

### Flavor 3C — General-purpose MCP servers (the "extras" stack)
Once you have the Telegram channel set up, you typically want Claude to do MORE than just chat. The bundle showcases several patterns:

- **TradingView MCP (Lewis Jackson):** Claude reads live chart data via Chrome DevTools Protocol — "code-to-code basis" — instead of guessing from screenshots.
- **Supabase / database MCP:** Claude queries production data ("how many users signed up yesterday?") via a connector.
- **Browser MCP:** Claude opens pages, fills forms, scrapes — covered also in [[../10x-claude-code/tactical-tricks|10x-claude-code § visual feedback]].
- **GitHub MCP:** Claude opens PRs, reviews code, comments on issues — wired into the Ralph loop.

These are stacked on top of the Telegram interface. Phone message → Claude → "do X via TradingView MCP" → result back to Telegram.

## The token-cost trap

Michele Torti's contrarian warning: **MCP servers are token-heavy**.

> Just two MCP servers can consume over **10,000 context tokens** at startup, before you've even sent a prompt.

Each MCP server lists its tools + schemas in the system context. Schemas can be hundreds of tokens each. Stack 5 MCP servers and you're starting every conversation 50,000 tokens behind.

This is real and biting. The bundle suggests two mitigations:

### Mitigation 1 — experimental MCPLI mode
[[../10x-claude-code/tactical-tricks|10x-claude-code § Tactical tricks]] § 8 covers this in detail. Short version: load MCP tool schemas on demand via bash commands instead of keeping them all in memory. Trades latency for context.

### Mitigation 2 — convert MCP → Skill (Torti's tactical workflow)
Once you've validated an MCP works for your use case, convert the workflow into a **Skill** (markdown SOP). The Skill describes how to call the underlying tool directly (e.g., curl + jq) without keeping the MCP schema loaded.

This is **a one-way migration** — you lose dynamic discovery, but you save tokens. Worth doing for high-frequency tools. NOT worth doing for tools you use rarely (the schema-loaded cost is amortized over future use).

Decision rule:
- Used daily → convert to Skill
- Used weekly → keep as MCP, evaluate
- Used monthly → keep as MCP

## Configuration files

Two flavors depending on where you run Claude:

| File | Used by |
|---|---|
| `~/.claude/mcp.json` (or project-local) | Claude Code (CLI) |
| `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) | Claude Desktop app |

Format roughly:
```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": { "API_TOKEN": "..." }
    }
  }
}
```

### The plain-text-tokens problem
Both files store secrets in plain text. Bundle creators paste tokens directly:
- BotFather Telegram tokens
- Discord bot tokens
- Database credentials
- Trading API keys

This is a major production gap. See [[gaps-production]] § Secrets management.

For solo/dev use, the bundle's pragmatic answer is: keep the file mode at `chmod 600`, never commit, use environment variables where the MCP server supports it. For team use, you need a vault.

## Stdio vs streamable-http transport

MCP supports multiple transports:
- **stdio** (most common in the bundle) — Claude spawns the MCP server as a child process, talks via stdin/stdout
- **streamable-http** — Claude connects to a remotely-hosted MCP server via HTTP

The bundle is dominated by stdio (local-process pattern). Streamable-http would matter when:
- You have one shared MCP server for a team
- You need to update the server without restarting every Claude instance
- You're running Claude in a container that doesn't have language runtimes

For solo Telegram remote-control: stdio is fine. For team scale: consider streamable-http.

## "OpenClaw" disagreement

The bundle has a notable creator disagreement. Chris Verzwyvelt calls Channels the **"OpenClaw killer"** — implying OpenClaw (a third-party Claude bridge) is now obsolete because of Channels. Mervin Praison disagrees, arguing Channels and OpenClaw are complementary, not competitive.

For an operator picking today: **default to Channels**. Channels is official, supported, and covers the common case. Reach for OpenClaw or custom only if you hit a Channels limitation.

## Cross-references

- [[layer-1-interface-telegram]] — Channels is the integrated Layer 1+3 path
- [[layer-2-engine-headless-claude-code]] — the engine that consumes MCP tools
- [[../10x-claude-code/tactical-tricks|10x-claude-code § MCPLI mode]] — token-cost mitigation
- [[../claude-code-hooks/_index|Claude Code hooks]] — the Hooks side of the Skills/MCPs/Hooks taxonomy
