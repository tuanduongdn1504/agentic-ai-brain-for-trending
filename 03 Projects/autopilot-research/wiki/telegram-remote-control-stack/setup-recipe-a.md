# Setup Recipe A — Solo dev, free tier, local Mac/PC

The verified ritual to make `@your_bot` on Telegram drive `claude --channels` on a local Mac/PC. **This recipe has been pilot-tested 2026-05-08 on macOS.** Every step below was either confirmed working or documented as a deviation from the official README.

> **What "Recipe A" means:** local machine (Mac Mini or laptop you keep awake), free Telegram, free Bun, no VPS, no tunneling. Single user. ~$0/mo external cost. ~10-30 min setup if everything goes right; pilot took ~45 min including the 5 deviations below.

## Prereqs (verify ALL of these before starting)

```bash
# 1. Claude Code CLI installed AND native binary working
command claude --version    # expect a version string, NOT "Error: claude native binary not installed"

# 2. Bun runtime — REQUIRED, not optional. Plugin's MCP server is server.ts (TypeScript)
command bun --version       # expect 1.x.x

# 3. brew (for installing Bun cleanly) — or use the official install script
command brew --version

# 4. A working Telegram account on your phone
```

If `claude --version` errors, see [Deviation 4](#deviation-4-native-binary-postinstall-failed) below.
If `bun` not found, run: `brew install oven-sh/bun/bun` (preferred over `curl | bash`).

## The 7-step ritual

### Step 1 — Create the bot (in Telegram, ~2 min)

1. Open Telegram, DM `@BotFather`
2. Send `/newbot`
3. Provide **display name** — anything (e.g., `My Claude Code`)
4. Provide **username** — must end in `bot` (e.g., `cvtot_research_bot`). Becomes `t.me/<username>`
5. BotFather replies with token `8123456789:AAH-Abcdef...`. **Copy the whole thing including the digits before `:`.**

Keep the token handy. You can always retrieve it later via BotFather → `/mybots` → pick bot → API Token.

### Step 2 — Add the official Anthropic plugin marketplace ⚠️ [Deviation 1](#deviation-1-marketplace-must-be-added-explicitly)

```bash
command claude plugin marketplace add anthropics/claude-plugins-official
```

Expected: `✔ Successfully added marketplace: claude-plugins-official`.

### Step 3 — Install the Telegram plugin ⚠️ [Deviation 2](#deviation-2-plugin-name-differs-from-many-tutorials)

```bash
command claude plugin install telegram@claude-plugins-official
command claude plugin list   # verify: telegram@claude-plugins-official enabled
```

### Step 4 — Configure the bot token

```bash
command claude   # opens interactive REPL
```

Inside the REPL:
```
/telegram:configure 8123456789:AAH-Abcdef...
```

(Or `/telegram:configure` alone — it'll prompt for the token.)

Writes `TELEGRAM_BOT_TOKEN=...` to `~/.claude/channels/telegram/.env` (file mode 600). Exit the REPL with `/quit` or `Ctrl-D`.

### Step 5 — Launch with channels enabled

```bash
command claude --channels plugin:telegram@claude-plugins-official
```

You should see banner ending with `Listening for channel messages from: plugin:telegram@claude-plugins-official`.

> ⚠️ **Banner alone does NOT mean it's working.** Bun must be running too — see [Deviation 3](#deviation-3-bun-runtime-is-a-hard-prereq).

Verify in a **second terminal** that the actual Bun MCP server started:
```bash
command ps aux | command grep -E "(bun|server\.ts|claude --channels)" | command grep -v grep
```

Expect 3 processes: `claude --channels ...`, `bun run ... start`, `bun server.ts`. If `bun server.ts` is missing, see [Deviation 3](#deviation-3-bun-runtime-is-a-hard-prereq).

### Step 6 — Pair from your phone

1. From Telegram, find your bot by the username from Step 1 (`@cvtot_research_bot` etc.)
2. Tap **Start** or send any message (e.g., `hi`)
3. Bot replies with a 6-character pairing code (e.g., `76a7e5`). Code expires in ~1 hour.
4. Back in your `claude --channels` terminal:

```
/telegram:access pair 76a7e5
```

⚠️ [Deviation 5](#deviation-5-pair-syntax-takes-the-code-as-an-argument): the code goes on the same line; don't expect a second prompt.

Expected: `✓ Paired user 1443607501`.

### Step 7 — Lock down the bot

By default the policy is `pairing` — anyone who finds your bot username can DM and get a pairing code. Switch to `allowlist`:

```
/telegram:access policy allowlist
```

Verify:
```
/telegram:access show
```

Should show `dmPolicy: allowlist`, `allowFrom: [<your-id>]`. Only you can talk to the bot now.

### Smoke test

DM your bot from Telegram:
```
pwd
```

Within ~5-10 sec, bot replies with the working dir of your `claude --channels` process. ✅ done.

---

## Deviations from the official README and tutorial blogs

These caused ~30 min of debugging during the 2026-05-08 pilot. Hard-coded into the recipe above so future-you can skip them.

### Deviation 1 — Marketplace must be added explicitly

Most tutorials show `/plugin install telegram@claude-plugins-official` and stop. But on a fresh machine `claude plugin marketplace list` shows `No marketplaces configured` — install will fail until you've added the marketplace explicitly via `claude plugin marketplace add anthropics/claude-plugins-official`. The plugin search/install flow has no automatic discovery.

### Deviation 2 — Plugin name differs from many tutorials

Some tutorials reference `claude-code-telegram-plugin-official`. The actual canonical name in the Anthropic marketplace is **`telegram@claude-plugins-official`** (short namespace, marketplace as suffix).

### Deviation 3 — Bun runtime is a hard prereq

The plugin v0.0.6 ships `server.ts` (TypeScript) with `bun.lock`. The `.mcp.json` specifies `"command": "bun"`. **Without Bun installed, `claude --channels` shows the "Listening" banner but NO MCP server starts.** Symptoms:

- Bot does not reply to DMs
- `~/.claude/channels/telegram/access.json` does NOT contain a `pending` entry after you DM the bot (it never gets created because the server doesn't exist)
- `~/.claude/channels/telegram/bot.pid` is missing
- `ps aux | grep bun` shows no bun process

Fix: `brew install oven-sh/bun/bun`. Then quit + relaunch `claude --channels` so it can spawn the now-runnable Bun MCP server.

### Deviation 4 — Native binary postinstall failed (sometimes)

`/usr/local/bin/claude` may symlink to a 500-byte stub `claude.exe` text file if npm's `--ignore-scripts` or `--omit=optional` was active during install. `claude --version` then errors with "Native package not found". Fix:

```bash
command npm install -g @anthropic-ai/claude-code --include=optional
```

### Deviation 5 — `/telegram:access pair` syntax

Older docs and the in-flight pilot tutorials say "type `/telegram:access pair`, then it asks for the code". Actual v0.0.6 syntax is `/telegram:access pair <code>` — single command, code as positional arg. No follow-up prompt.

---

## Verified test environment (pilot 2026-05-08)

| Component | Version | Source |
|---|---|---|
| Claude Code CLI | 2.1.133 | npm (Sonnet 4.6, Claude Max) |
| Plugin | telegram@claude-plugins-official 0.0.6 | Anthropic marketplace |
| Bun | 1.3.13 | brew (oven-sh/bun) |
| Node | 24.13.1 | nvm |
| OS | macOS (Cvtot machine) | — |
| MCP server | server.ts via Bun | plugin |

End-to-end ritual time after deviations resolved: ~3 min (pure happy path).

---

## What this recipe doesn't cover

- **Persistence** beyond an open terminal — see [[persistence-and-tunneling]]
- **Production hardening** (audit logs, rate limits, IaC) — see [[gaps-and-followups]]
- **VPS deployment** (Recipe C) — covered in [[overview]] §recipes; full VPS recipe deferred to a separate topic
- **Multi-user / team allowlists** — see [[security-model]] § Multi-user

## See also

- [[overview]] — the 3 recipes (A/B/C) compared
- [[security-model]] — what allowlist actually protects against
- [[architecture]] — what's running under the hood
- [[expert-disagreements]] — Telegram vs Discord, local vs VPS, auto-approve
