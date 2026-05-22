# (C) Cluster 1 — README install + multi-harness + canonical-snippet auto-insertion + design philosophy

**Source**: [`README.md`](https://github.com/thith/teleport/blob/main/README.md) verbatim content (fetched 2026-05-22).

## What the product is

`teleport` is a **lightweight Telegram bridge** for AI coding agents (Claude Code 4.7+, Codex, Gemini CLI, Cursor, Antigravity, and others) that enables agents to:

1. **Send brief progress updates** to Telegram while the operator is away from the machine
2. **Receive reply-based instructions** from Telegram and resume work autonomously

The design intent is **out-of-band session-handoff** — the operator can leave the machine, get a Telegram ping when significant progress (or blockers) emerge, reply with new instructions, and have the agent continue working unattended. The full conversation stays local; only summaries + replies transit Telegram.

This is a **NEW T4 Bridge sub-archetype** — corpus-first messaging-platform-as-operator-notification-channel for AI-coding-agents.

## 3-step install procedure (from README)

1. **Clone-as-sibling-directory**: `teleport/` must live as a direct sibling to each project that will use it. Standard pattern:

```
your-workspace/
├── teleport/
├── project-A/
├── project-B/
└── project-C/
```

2. **Obtain Telegram credentials**: BotFather creates a bot → token; operator chats with bot once → chat ID extracted via Telegram API call

3. **Configure `.env`**: `TELEGRAM_BOT_TOKEN=...` + `TELEGRAM_CHAT_ID=...` saved in `teleport/.env`

This is **CORPUS-FIRST clone-as-sibling-directory install pattern in v60+ window**:

| Wiki | Install mechanism |
|---|---|
| v75 impeccable | File-copy into `.claude/skills/<harness>/` |
| v76 agent-skills-standard | `npm install` + CLI sync command |
| v82 huashu-design | `npx skills add owner/repo` shorthand |
| v85 ui-ux-pro-max-skill | `npm install -g uipro-cli` + `npx uipro-cli init --ai <platform>` |
| v87 claude-comstyle | Single-file copy into `.claude/skills/style-switcher/` |
| **v88 teleport** | **Clone-as-sibling-directory + per-project canonical-snippet auto-insertion** |

The sibling-directory pattern is unusual: instead of installing INTO each project, teleport sits NEXT TO projects and is referenced via relative path (`../teleport/rules/telegram-guide.md`). This avoids per-project duplication and keeps bot credentials in one place.

## Canonical-snippet auto-insertion mechanism

After clone + env setup, the operator pastes a **wiring prompt** into their AI agent. The agent then inserts a canonical Telegram-aware snippet into **global config files**:

| Harness | Global config target |
|---|---|
| Claude Code | `~/.claude/CLAUDE.md` |
| Gemini CLI | `~/.gemini/GEMINI.md` |
| Codex | `~/.codex/AGENTS.md` |

The canonical snippet instructs the harness: when the user says *"send a Telegram report"* (or variants in multiple languages including Vietnamese), the agent must:

1. Consult `../teleport/rules/telegram-guide.md` for current send-rules
2. Send a concise update via the teleport script
3. Enter listening-mode for replies
4. Resume work with new instructions when replies arrive

**CORPUS-FIRST canonical-snippet auto-insertion across 3 global config files** in v60+ window. This is a Pattern #84 84c.2 sub-mechanism strengthening (CLI-generates-native-formats variant at install layer): one shared snippet automatically deployed into 3 harness-specific global config files.

Alternative project-local install: snippets can also be inserted into per-project config (`.claude/CLAUDE.md` / `.gemini/GEMINI.md` / `.codex/AGENTS.md`) if the operator prefers project-scope over global-scope.

## Trigger phrases (multi-language)

Per README, the canonical snippet recognizes multiple trigger phrasings, including English ("ping me on Telegram when done") and Vietnamese (implied via multi-language variant claim). Operator can say things like:

- *"ping me on Telegram when done"*
- *"send me a Telegram report"*
- (VN variants per multi-language support claim)

CORPUS-FIRST multi-language trigger-phrase support for natural-language-invocation of bridge functionality in v60+ window. Library-vocab candidate.

## Multi-harness explicit support (Pattern #57 sub-variant 57c-product MID-STRONG)

README explicitly lists **5+ harness corpus-subject overlaps**:

| Harness | Corpus subject |
|---|---|
| Claude Code 4.7+ | v65 |
| Codex | v62 (T4 Bridge — codex-plugin-cc cross-vendor cooperation) |
| Gemini CLI | (not in corpus directly but referenced extensively in v76 + v83 + v85 ecosystem) |
| Cursor | v75 + v76 (referenced in v75 impeccable 14-harness + v76 agent-skills-standard 10+-harness) |
| Antigravity | v67 (T4 Bridge — opencode-antigravity-auth OAuth-credential-plugin) |
| "Other agents" | open-ended for any harness with global config file support |

Pattern #57 sub-variant 57c-product MID-STRONG density (5 explicit overlaps; vs v85 10-citation CORPUS-RECORD high; v83 7; v82 4; v87 1; v88 = 5 in mid-range).

Particularly notable: **antigravity citation** links v88 → v67 corpus-recursive sub-chain candidate Pattern #57 sub-variant 57j strengthening (v85 already registered 57j N=1; v88 = potential N=2 if v67 antigravity-citation counts as 57j evidence).

## Design philosophy (per README "Design Philosophy" section)

> *"Unlike full-session mirrors, Teleport maintains the complete conversation locally while transmitting only brief updates and receiving concise replies — minimizing phone-screen friction during remote oversight."*

Three explicit design choices:

1. **Conversation stays local** — no full-session-mirror to Telegram (vs other remote-control AI tools)
2. **Minimum phone-screen friction** — brief summaries + concise replies only (vs verbose remote-debugging UX)
3. **Out-of-band oversight, not remote-control** — agent operates locally; Telegram is for status + redirect, not for issuing every command

This design philosophy distinguishes teleport from existing remote-control AI tools (which typically mirror full conversations). Library-vocab candidate "Local-Conversation-Plus-Bridge-Summaries Design Philosophy".

## Critical prerequisites (per README)

Three prerequisites for unattended operation:

1. **AI agent runs in auto-execution mode** — permission dialogs would stall unattended operation
2. **Machine stays awake** — no remote-wake mechanism; operator's machine must remain on
3. **Every project sits as direct sibling to teleport/ folder** — relative-path-reference requirement

The "auto-execution mode" prerequisite is interesting — it implicitly requires the operator to accept higher autonomy-level agent operation (matching v71 agents-best-practices L0-L4 autonomy-level taxonomy at L3+ "executes-with-approval-on-destructive" or higher). Library-vocab candidate "Auto-Execution-Mode Prerequisite for Out-of-Band Operation".

## Zero external dependencies — Pattern #66 supply-chain discipline

teleport ships with **zero external runtime dependencies** — Node.js built-ins only (likely `https`, `fs`, `dotenv` via process.env, etc.). No `package.json` runtime deps section, no `npm install` step in the install procedure beyond the implicit Node.js runtime requirement.

CORPUS-FIRST zero-external-dependency T4 Bridge in v60+ window. Library-vocab candidate "Zero-External-Dependency Bridge-Tool" PROVISIONAL N=1.

This is Pattern #66 supply-chain discipline within-pattern strengthening at the bridge-tool layer. Sister to:

- v76 agent-skills-standard 6-axis supply-chain integrity discipline
- v79 autoresearch_folktales minimal-dependency-discipline-by-constraint
- v85 multi-symlink architecture (no extra deps)
- v88 zero-dependency-by-design

## What is NOT in the README

- **No telemetry / measurement** — design choices stated, not measured
- **No multi-bot / multi-chat support documented** — single-bot + single-chat per `.env`
- **No e2e encryption discussion** — Telegram channel security inherited from Telegram (not E2E by default for bots)
- **No prompt-injection-defense at the message-channel boundary** — operator's Telegram replies are essentially user-input to the agent; trust-boundary not explicitly discussed
- **No CI tests / eval harness** — JavaScript file collection, no test framework
- **No release tags / changelog** — small-scale-active-development profile
- **No formal API documentation** — README is the entire docs surface
- **No multi-operator / shared-team support** — single operator + single chat-id pattern

These absences fit the **micro-scale-personal-tooling profile** that originated as internal tooling for trumviahe.com. Operator should consider these gaps before adopting at higher trust-level.

## Storm Bear direct-applicability (synthesis)

Storm Bear session context already includes **`plugin:telegram:telegram` MCP server** with reply/edit/react tools wired up. teleport is **complementary infrastructure**:

| Layer | Existing operator setup | teleport addition |
|---|---|---|
| MCP-server reply tool | ✅ already configured | (unchanged) |
| Operator-initiated DM to Storm Bear | ✅ existing flow | (unchanged) |
| **Agent-initiated session-handoff updates** | ❌ NOT currently | ✅ **NEW capability** |
| **Agent-receive-reply unattended resumption** | ❌ NOT currently | ✅ **NEW capability** |

The operator's existing Telegram infrastructure (bot + chat configured via `plugin:telegram` MCP) means **incremental cost-of-trial is minimum**: only sibling-directory clone + chat-ID config (already known via MCP) + canonical-snippet auto-insertion into operator's `~/.claude/CLAUDE.md`.

**Recommended pilot composition** (if adopted):

```
1. Clone teleport/ as sibling to KJ OS Template/
2. Copy existing Telegram bot token + chat ID from MCP config into teleport/.env
3. Auto-wire canonical snippet into ~/.claude/CLAUDE.md
4. Set Claude Code to auto-execution mode for trusted operations
5. Use "ping me on Telegram when done" for wiki-build sessions where operator steps away
```

Estimated 5-10 minute setup. Reversible-via-delete + remove canonical snippet from `~/.claude/CLAUDE.md`.
