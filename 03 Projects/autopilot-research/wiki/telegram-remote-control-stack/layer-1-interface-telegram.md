# Layer 1 — Interface (Telegram / Discord / Native Remote Control)

How a message from your phone reaches Claude Code. Three competing options, plus the cross-cutting security pattern.

## Option 1A — Telegram via Claude Code Channels (recommended default)

Anthropic's official plugin for Telegram. Released 2026 Q1. The dominant pattern across 4 of 6 creators in the bundle.

### Setup ritual (verified 2026-05-08 — see [[setup-recipe-a]] for full deviations)

```bash
# Prereq: Bun runtime (the plugin's MCP server is server.ts, requires Bun)
command brew install oven-sh/bun/bun

# 1. Add the marketplace + install plugin
command claude plugin marketplace add anthropics/claude-plugins-official
command claude plugin install telegram@claude-plugins-official

# 2. Configure with BotFather token (DM @BotFather → /newbot to get one)
command claude     # interactive REPL
> /telegram:configure 8123456789:AAH-Abcdef...

# 3. Launch with --channels + plugin spec
command claude --channels plugin:telegram@claude-plugins-official

# 4. Pair from your phone
#    DM your bot → receive 6-char code → in terminal:
> /telegram:access pair 76a7e5
```

> ⚠️ **The ritual in pre-2026-05 tutorials uses out-of-date commands.** Many bundle creators (Chris Verzwyvelt / Mervin Praison / Kumo Explains / Developers Digest) reference `claude --install-plugin claude-code-telegram-plugin-official` and `/telegram:access-policy allow-list` — these don't work with the current 2.1.x CLI + plugin v0.0.6. The verified pilot caught **5 deviations**; full debug story in [[setup-recipe-a]].

### Lock down immediately

```bash
> /telegram:access policy allowlist
```

This is the **most-cited security command** across the bundle. Without it, anyone who discovers your bot's username can DM it and execute commands on your machine. Note: command syntax is `policy allowlist` (no hyphen), not `access-policy allow-list` as older docs say.

### Pros
- Official + supported (no third-party MCP server to maintain)
- BotFather setup is well-documented
- Voice memos, file uploads, threading all work natively
- Free tier of Telegram is generous

### Cons
- BotFather UX is non-obvious for non-Telegram users
- Allow-list is tied to Telegram User IDs (sharing requires manual ID exchange)
- Token in config file (see [[gaps-production]] § Secrets management)

## Option 1B — Discord via Claude Code Channels

Same plugin family, different platform. Kris Torrington's preferred path.

### Discord-specific gotcha
Discord requires you to **enable "Message Content Intent"** in the Discord Developer Portal — without this, the bot literally cannot read incoming messages. This is a non-obvious failure mode that Kris Torrington flags hard. (Telegram has no equivalent toggle — bot reads messages addressed to it by default.)

### Discord-specific access control
Allow-list uses **User IDs + Channel IDs** in `access.json`:
```json
{
  "allowed_users": ["123456789"],
  "allowed_channels": ["987654321"]
}
```

Multi-channel scoping is **richer than Telegram** — you can have a `#prod-bot` channel restricted to senior staff and a `#dev-bot` channel open to all team members. Telegram has chats (DMs or groups) but no native channel tagging.

### When to pick Discord over Telegram
- You already use Discord for team comms
- You want per-channel access scoping (e.g. team vs individual)
- You want voice channels for hands-free operation (not yet covered in the bundle, but architecturally available)

### When NOT to pick Discord
- Solo operator who lives in Telegram (Chris Verzwyvelt: "I just like doing things in Telegram")
- Stricter privacy (Discord servers may have mods/admins beyond your control if shared)

## Option 1C — Native Claude Remote Control

The `/remote-control` command. NetworkChuck's flagged "game-changer". Different mechanism: not a bot, not a tunnel — Anthropic-hosted bridge that resumes your laptop's CLI session inside the **native Claude mobile app**.

### Setup
```bash
# In your Claude Code session on the laptop:
/remote-control
```
That's it. Open the Claude mobile app, sign in with the same account, the session is there.

### Pros
- Zero networking config — Anthropic handles the bridge
- No VPN, no tunnel, no bot
- Native app UX (better than Telegram for long sessions)
- Same auth as Claude desktop — no separate token to leak

### Cons
- **You can't START a new session from the phone yet** — only resume one started on your laptop. NetworkChuck explicitly flags this as a feature gap. The laptop must be running Claude Code first.
- Manual interaction only. Not for automated reactions to events.
- Locked to Anthropic's auth — can't substitute alternative LLM backends.

### Best use case
Manual interaction during a session. You started a long task on your laptop, walk away, want to check progress + steer course on your phone.

## Option 1D — Custom MCP server (the niche path)

Samir Kharel's pattern: build your own MCP server in Python with `fastmcp` to bridge Claude Desktop ↔ Discord (or any platform).

This sits at Layer 3 (integration) more than Layer 1, but it functionally provides the interface. Detailed in [[layer-3-mcp-integration]] § custom servers.

**When to pick:** you need a feature Channels doesn't support (e.g. Slack, Microsoft Teams, Signal, custom internal messaging). Otherwise, Channels is faster and supported.

## Comparison matrix

| Feature | Telegram Channels | Discord Channels | Native Remote Control | Custom fastmcp |
|---|---|---|---|---|
| Setup time | 5 min | 10 min (Intent toggle) | 30 sec | hours |
| Cost | $0 | $0 | $0 | dev time |
| Multi-user scoping | User-ID allow-list | User+Channel IDs | Single account | custom |
| Trigger autonomous reaction | yes | yes | no | yes |
| Voice memos | yes (Telegram-native) | yes (Discord-native) | tbd | custom |
| File transfers in/out | yes | yes | tbd | custom |
| Cross-device session resume | partial | partial | excellent | custom |
| Auth model | bot token | bot token + intent | Claude account | custom |

## The "warm session" advantage

Across the bundle, **Developers Digest** flags a key tactical distinction: **warm vs cold sessions**.

- **Cold session:** every message from the phone spawns a new Claude Code subprocess. Loses context. Smaller window. Slower (subprocess startup).
- **Warm session:** one long-running Claude Code process listens via `--channels`. Each message is a new turn in the same conversation. Larger context window, faster response, continuity.

Channels (Options 1A + 1B) give you warm sessions by default. Custom fastmcp servers (1D) typically give cold sessions unless you architect for warmth. Native Remote Control (1C) is always warm (you're literally resuming the existing session).

Pick warm wherever possible. See [[layer-2-engine-headless-claude-code]] for engine-side implications.

## Cross-references

- [[overview]] § decision matrix — which interface fits your recipe
- [[layer-3-mcp-integration]] — the layer 3 mechanics underneath Channels
- [[layer-4-network-tunneling]] — once your bot connects, how the message physically reaches your machine
- [[../claude-code-hooks/_index|Claude Code hooks]] — Stop Hooks fire to your Telegram bot when CI fails
