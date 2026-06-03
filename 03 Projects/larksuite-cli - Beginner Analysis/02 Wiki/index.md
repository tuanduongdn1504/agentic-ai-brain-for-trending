# larksuite/cli — Wiki (v143)

> **One line:** The official **Lark/Feishu CLI**, "built for humans and AI Agents" — 200+ commands + 26 bundled AI Agent Skills + agent-auth primitives, the *agent-native CLI* counterpart to v140's MCP-server approach.
> **Tier:** T2 Service (agent-native vendor CLI). **Verdict:** GOAL-ALIGNED INCLUDE 3/4 (a FAIL · b/c/d STRONG).
> **Repo:** `larksuite/cli` (official ByteDance org) · MIT · Go 97.3%.
> **§37 provenance:** ≈13.3k★ / 909 forks (as of 2026-06, repo page — *stated, NOT API-verified; env mocks GitHub API*).

## What it is
README opener (verbatim):
> "The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Slides, Calendar, Mail, Tasks, Meetings, Markdown, and more, with 200+ commands and 26 AI Agent Skills."

A command-line tool that gives **AI agents (and humans) programmatic control of the entire Lark/Feishu platform**. Sibling to v140 google_workspace_mcp — same goal (an agent driving a vendor productivity suite), different delivery (agent-native CLI + skills vs an MCP server).

## Three-layer command architecture
| Layer | Prefix | What |
|---|---|---|
| **Shortcuts** | `+` | Human+AI-friendly: smart defaults, table output, **dry-run previews** |
| **Curated API** | (none) | 100+ commands auto-generated from Lark OAPI metadata, evaluation + quality gates, 1:1 mapping |
| **Raw API** | `api` | Direct calls covering **2,500+ APIs** |

## Why it's agent-native (the goal-#1 substance)
- **26 AI Agent Skills** in `/skills` (`lark-im`, `lark-doc`, `lark-base`, `lark-sheets`, `lark-calendar`, `lark-mail`, `lark-task`, `lark-vc`, `lark-minutes`, `lark-okr`, `lark-approval`, workflow skills, `lark-openapi-explorer`, …) + **`lark-skill-maker`** to author more.
- **Identity-switching** — `--as user` (authenticated user) / `--as bot` (e.g. messaging).
- **Non-blocking agent auth** — `lark-cli auth login --no-wait` returns the verification URL immediately ("extract it and send it to the user"); resume with `--device-code <CODE>`. Built for headless agent workflows.
- "Every command is tested with real Agents."

## Skills format & distribution
The 26 skills are **Lark-native** in content (not the agentskills.io SKILL.md spec internals) but **installable via `npx skills add larksuite/cli -y -g`** — the vercel-labs skills CLI that anchors the corpus's 57k distribution chain. So it *rides the 57k distribution mechanism* with vendor-specific content (a 57k implementer-**candidate**, flagged for the next audit's chain reconciliation).

## Install
```
npx @larksuite/cli@latest install      # npm (recommended)
# or from source: Go 1.23+ and Python 3
npx skills add larksuite/cli -y -g     # the agent skills
```
No MCP server — purely a CLI.

## Tech
Go 97.3%; MIT; official `larksuite` (ByteDance) org; 13.3k★/909 forks.

## Corpus connectivity
- **Productivity-suite agent-connectivity cluster with v140 google_workspace_mcp** (MCP-server vs agent-native-CLI — two patterns, same goal).
- **Pattern #57 / 57k chain** — implementer-candidate (rides `npx skills add`, Lark-native content).
- **Pattern #84** agent-tooling (humans + agents); agent-auth primitives loosely connect to v67's OAuth-bridge thread.
- See `01 Analysis/` for the full verdict + Phase 4b (PRIMARY = NEW Library-vocab "Agent-Native Vendor CLI" N=1 CORPUS-FIRST).

## Pilot note
**Tier-1 pilotable, conditional.** If you want a Claude agent to operate Lark/Feishu (or just to *study* an agent-native CLI's affordances — the dry-run shortcut tier, user/bot identity-switching, device-code auth-handoff are worth borrowing as design ideas), it's low-friction: `npx @larksuite/cli@latest install`, scoped to read/dry-run first. An operational trial needs a Lark/Feishu tenant + OAuth app, so for this vault it's more a **design-study READ** than an install — unless you actually use Lark.
