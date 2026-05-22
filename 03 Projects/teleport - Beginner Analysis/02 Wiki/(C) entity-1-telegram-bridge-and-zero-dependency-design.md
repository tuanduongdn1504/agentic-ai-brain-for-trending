# (C) Entity 1 — Telegram bridge + out-of-band session-handoff + zero-dependency design + 5-harness explicit + canonical-snippet auto-insertion

**Type**: Core-product entity.

## What teleport does

teleport bridges AI coding agents (running on the operator's local machine) to a Telegram chat (accessed via operator's phone or any Telegram client when away from the machine). The bridge is **bidirectional**:

| Direction | Use case | Trigger |
|---|---|---|
| Agent → Telegram | Send brief progress update | Agent receives "ping me on Telegram when done" or variants; sends summary at completion or blocker |
| Telegram → Agent | Receive instructions | Operator replies to Telegram message; agent reads reply, resumes work with new instructions |

The architecture is **out-of-band session-handoff** — operator can step away from machine, get pinged when work completes or stalls, and redirect remotely without remote-desktop or full-session-mirror tooling.

## Zero-external-dependency design

Per the README, teleport ships with **zero external runtime dependencies**:

- No `package.json` with runtime deps (only Node.js built-in modules like `https`, `fs`, `process`, etc.)
- No `npm install` step in the install procedure
- No bundler, no transpilation, no TypeScript build step (JavaScript 100%)

This is **CORPUS-FIRST zero-external-dependency T4 Bridge in v60+ window**. Library-vocab candidate "Zero-External-Dependency Bridge-Tool" PROVISIONAL N=1.

**Pattern #66 supply-chain discipline within-pattern strengthening**: bridge-tool supply-chain attack-surface = minimum. The supply-chain narrows to:
- Node.js runtime (operator's host responsibility)
- Telegram Bot API (Telegram's responsibility)
- The teleport JavaScript code itself (auditable + ~JavaScript-only)

Compared to bridge-tools that ship full dependency trees (typical Node.js bridge tools pull in 50-500+ transitive deps), teleport's attack-surface is **orders of magnitude smaller**. This is meaningful for an operator-notification channel that handles instructions to a high-autonomy AI agent.

## 3-step install procedure detail

### Step 1: Clone-as-sibling-directory

```bash
cd ~/Code/  # or wherever your projects live
git clone https://github.com/thith/teleport.git
ls
# teleport/   project-A/   project-B/   project-C/
```

The sibling-directory pattern means **one teleport install serves N projects**. Each project references teleport via relative path (`../teleport/...`) rather than installing teleport into the project itself.

### Step 2: Get Telegram credentials

```
1. Open Telegram → search @BotFather → /newbot → get TELEGRAM_BOT_TOKEN
2. Send a message to your new bot
3. Open https://api.telegram.org/bot<TOKEN>/getUpdates → extract chat.id field → TELEGRAM_CHAT_ID
```

### Step 3: Configure `.env`

```bash
cat > teleport/.env <<EOF
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
EOF
```

### Step 4 (optional but recommended): Auto-wire canonical snippet

Operator pastes the README's wiring-prompt into Claude Code (or Codex / Gemini CLI / Cursor). The agent then writes Telegram-aware boilerplate into:

- `~/.claude/CLAUDE.md` (global Claude Code config)
- `~/.gemini/GEMINI.md` (global Gemini CLI config)
- `~/.codex/AGENTS.md` (global Codex config)

The boilerplate teaches the agent that when the user says trigger phrases (e.g. "ping me on Telegram when done"), the agent must:

1. Read `../teleport/rules/telegram-guide.md` for current rules
2. Call the teleport script with the progress summary
3. Enter listening-mode (poll Telegram for replies)
4. Resume work when replies arrive

## CORPUS-FIRST observations on install mechanism

1. **CORPUS-FIRST clone-as-sibling-directory install pattern** in v60+ window (vs file-copy / npm install / npx / single-file copy)

2. **CORPUS-FIRST canonical-snippet auto-insertion across 3 global config files** simultaneously — agent writes itself into 3 harness-specific configs from one wiring prompt = Pattern #84 84c.2 sub-mechanism strengthening (CLI-generates-native-formats variant at install layer)

3. **CORPUS-FIRST natural-language-trigger-phrase-recognition** — operator says English or Vietnamese trigger phrases; agent reads canonical snippet from CLAUDE.md/GEMINI.md/AGENTS.md and recognizes the intent without bespoke command syntax

4. **CORPUS-FIRST out-of-band-operator-notification-via-messaging design philosophy** in 88-wiki corpus

## Multi-harness coverage

Per README explicit claim: **Claude Code 4.7+ + Codex + Gemini CLI + Cursor + Antigravity + "other agents through global config files"**.

5+ explicit corpus-subject overlaps:

| Harness | Corpus subject | Status |
|---|---|---|
| Claude Code 4.7+ | v65 | Direct corpus-subject match |
| Codex | v62 | Direct match (note: v62 was itself a T4 Bridge — Codex-plugin-Claude-Code) |
| Cursor | v75 / v76 | Direct match (referenced in v75 14-harness + v76 10+-harness lists) |
| Antigravity | v67 | Direct match (v67 was T4 Bridge — Opencode-Antigravity OAuth) |
| Gemini CLI | (not direct corpus-subject) | Mentioned in v76 + v83 + v85 ecosystems |
| Other agents | open-ended | "global config files" pattern is portable |

**Pattern #57 sub-variant 57c-product MID-STRONG citation density**: 5 explicit overlaps, mid-range vs v85 10 (CORPUS-RECORD high) and v87 1 (low).

**Pattern #84 84c.1 sub-mechanism strengthening at 5+-harness data-point**: teleport sits in mid-range of the full distribution (v87 2 LIGHT-end to v85 18 ceiling). Provider-agnostic-by-design intent strong; mechanism = "global config files at standardized paths".

## Pattern #21 session-handoff sub-variant detail

Pattern #21 "Session-Longevity-Discipline-As-Pattern" was registered at v72 (DeepSeek-TUI) and strengthened with sub-variant "Session-Handoff-Via-README-Checkpoint" at v73 (cc-switch).

teleport extends Pattern #21 with a 2nd sub-variant:

| Sub-variant | Wiki anchor | Mechanism | Operator role |
|---|---|---|---|
| 21a Session-Handoff-Via-README-Checkpoint | v73 cc-switch | Operator manually writes status to repo README before stepping away | Manual, sync |
| **21b Out-of-Band Session Handoff via Messaging Platform** | **v88 teleport** | **Agent automatically pings operator with summary; replies resume work** | **Automated, async** |

**Pattern #21 NEW sub-variant 21b candidate "Out-of-Band Session Handoff via Messaging Platform"** PROVISIONAL N=1. With v73 21a + v88 21b = 2-instance sub-variant layer with 2-distinct-mechanism axes (manual-sync vs automated-async).

If a future wiki introduces a 3rd session-handoff variant (e.g. via email / GitHub issues / Notion), Pattern #21 sub-variant layer reaches N=3 = formalization candidate.

## Trigger-phrase multi-language support

Per README, the canonical snippet recognizes multi-language variants of "ping me on Telegram when done":

| Language | Sample trigger phrase |
|---|---|
| English | "ping me on Telegram when done" / "send me a Telegram report" |
| Vietnamese | (implied per multi-language variant claim; likely *"thông báo cho tôi qua Telegram khi xong"* or similar) |
| Others | (open-ended via canonical snippet customization) |

**CORPUS-FIRST multi-language trigger-phrase support for natural-language-invocation of bridge functionality** in v60+ window. Library-vocab candidate "Multi-Language Natural-Language-Trigger for Bridge Functionality".

This matters because: the canonical snippet is itself a small piece of prompt-engineering that needs to recognize varied operator intent. Multi-language support means the snippet is robust to operator code-switching (a common pattern for VN developers who mix EN+VN in casual chat).

## Critical prerequisites (operator commitment)

Three prerequisites for unattended operation:

1. **Auto-execution mode** — agent must operate without permission-dialog stalls. Implication: operator commits to L3+ autonomy-level (per v71 agents-best-practices L0-L4 taxonomy).

2. **Machine awake** — host machine cannot sleep / hibernate. Implication: operator either keeps laptop plugged in + sleep disabled, OR runs on always-on desktop / cloud-VM.

3. **Sibling-directory placement** — teleport must be a direct sibling of each project. Implication: operator's directory structure must allow sibling layout (cannot use deeply-nested project trees).

These prerequisites are **honestly disclosed** in the README (Pattern #83 honest-deficiency-disclosure within-pattern). Operator should evaluate before adoption.

## Library-vocab "Engagement-Deficit-Extreme-With-Active-Forks" N=3 PROMOTION-ELIGIBLE

v88 stats: 23 stars / **14 forks** / 0 open issues / 0 watchers.

This is **0 open issues despite 14 active forks** = high active-deployment-intent + zero maintenance friction. Sister observations:

| Wiki | Stars | Forks | Open issues | Pattern |
|---|---|---|---|---|
| v76 agent-skills-standard | 496 | 147 | 0 | CORPUS-RECORD-LOW engagement-deficit (at higher scale) |
| v87 claude-comstyle | 28 | 4 | 0 | Engagement-deficit at micro-scale |
| **v88 teleport** | **23** | **14** | **0** | **Engagement-deficit at micro-scale with 60.9% fork ratio** |

**Library-vocab "Engagement-Deficit-Extreme-With-Active-Forks" N=3 PROMOTION-ELIGIBLE at v90** (v76 + v87 + v88 = 3-instance evidence; PROMOTION-ELIGIBLE administrative).

## Library-vocab "Try-Once-and-Move-On Profile" N=3 PROMOTION-ELIGIBLE

v88 stats: 0 watchers despite 14 forks.

Sister observations:

| Wiki | Watchers | Forks | Profile |
|---|---|---|---|
| v79 autoresearch_folktales | 0 | 15 | Try-Once-and-Move-On anchor |
| v87 claude-comstyle | 0 | 4 | Sister at micro-scale |
| **v88 teleport** | **0** | **14** | **Sister with high fork-ratio** |

**Library-vocab "Try-Once-and-Move-On Profile" N=3 PROMOTION-ELIGIBLE at v90** (v79 + v87 + v88 = 3-instance evidence; PROMOTION-ELIGIBLE administrative).

## What this entity does NOT include

- **No e2e encryption discussion** for the Telegram channel — operator should consider whether agent-to-operator messages should be on E2E channel (Telegram bots are NOT E2E by default; Telegram Cloud Chats are server-stored)
- **No prompt-injection-defense at message-channel boundary** — operator's Telegram replies are direct user-input to the agent; trust-boundary not explicitly enforced
- **No multi-operator / shared-team support** — single operator + single chat-id pattern
- **No release tagging / changelog** — small-active project profile
- **No CI / eval / testing infrastructure** — JavaScript file collection only

These gaps are acceptable at the micro-scale-personal-tooling tier but should be evaluated before scaling adoption to team/org contexts.
