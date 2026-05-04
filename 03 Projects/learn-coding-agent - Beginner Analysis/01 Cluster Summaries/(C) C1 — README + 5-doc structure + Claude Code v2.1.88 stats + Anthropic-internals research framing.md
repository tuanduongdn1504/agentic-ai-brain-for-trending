# C1 — README + 5-doc structure + Claude Code v2.1.88 stats + Anthropic-internals research framing

> Source cluster: `README.md` (45 KB) + `README_CN.md` + `README_JA.md` + `README_KR.md` + `docs/{en,ja,ko,zh}/README` headers
> Wiki #53 (learn-coding-agent v53)

---

## Repo identity (verbatim)

- **Title (per README h1):** "Claude Code Architecture Study"
- **Repo name:** `sanbuphy/learn-coding-agent` (repo-name + README-title MISMATCH; 1st in corpus to date with this magnitude of mismatch)
- **GitHub description:** "Research on Coding Agents" (generic)
- **Tagline (verbatim README intro):** *"This project is a learning and research repository focused on CLI Agent architecture. All materials are compiled entirely from publicly available online references and discussions, with a particular focus on public information regarding the highly popular CLI Agent `claude-code`."*

## Disclaimer (verbatim README §Copyright & Disclaimer)

```
This repository is provided strictly for technical research and educational purposes.
Commercial use is strictly prohibited.

If you are the copyright owner and believe this repository content infringes your rights,
please contact the repository owner for immediate removal.
```

**No formal license file exists.** This is informal research-only-non-commercial-restriction declaration with DMCA-style takedown clause.

---

## Quadrilingual structure

4 root READMEs at byte-level near-equivalent depth:
- `README.md` (English, 45 KB, primary)
- `README_CN.md` (中文, 43.9 KB)
- `README_JA.md` (日本語, 43.9 KB)
- `README_KR.md` (한국어, 40.5 KB)

5 deep-dive reports × 4 languages = 20 docs total in `docs/{en,ja,ko,zh}/`:
1. Telemetry & Privacy
2. Hidden Features & Codenames
3. Undercover Mode
4. Remote Control & Killswitches
5. Future Roadmap

**i18n breakdown** (sub-files; English file sizes shown):
- `01-telemetry-and-privacy.md` (3,872 bytes / 124 lines)
- `02-hidden-features-and-codenames.md` (4,666 bytes / 112 lines)
- `03-undercover-mode.md` (4,259 bytes / 110 lines)
- `04-remote-control-and-killswitches.md` (4,546 bytes / 161 lines)
- `05-future-roadmap.md` (5,813 bytes / 167 lines)

EN `docs/` total: 23,156 bytes / 674 lines — TINY but information-dense.

---

## Stats from README (about Claude Code itself, NOT this repo)

> ⚠️ All stats below are claims by Sanbu about Claude Code v2.1.88 internals; based on publicly-available sources; not Anthropic-confirmed.

| Item | Count |
|------|-------|
| Files (.ts/.tsx) | ~1,884 |
| Lines | ~512,664 |
| Largest single file | `query.ts` (~785 KB) |
| Built-in tools | ~40+ |
| Slash commands | ~80+ |
| Dependencies (node_modules) | ~192 packages |
| Runtime | Bun (compiled to Node.js >= 18 bundle) |
| Studied version | Claude Code v2.1.88 |

## Stats about the learn-coding-agent repo itself

| Field | Value |
|-------|-------|
| Stars | 11,735 |
| Forks | **19,741 — CORPUS-RECORD 168.2% FORK-TO-STAR INVERSION** (forks > stars by 68%) |
| Watchers | 11,735 |
| Open issues | 59 |
| Repo size (raw) | ~8.2 MB |
| Repo size (extracted) | 316 KB |
| Created | 2026-03-31 |
| Last push | **2026-04-01** (24 days stale at probe time; abandoned-since-day-2) |
| Default branch | main |
| License (formal) | NULL — no LICENSE file |
| License (informal) | README-only "research-only + Commercial use strictly prohibited" |
| Topics | empty |
| Homepage | empty |

---

## README structure — table of contents (verbatim)

1. Deep Analysis Reports (`docs/`) — Telemetry, codenames, undercover mode, remote control, future roadmap
2. Directory Reference — Code structure tree (Claude Code's `src/` tree, ~250 lines of ASCII diagram)
3. Architecture Overview — Entry → Query Engine → Tools/Services/State (ASCII block diagram)
4. Tool System & Permissions — 40+ tools, permission flow, sub-agents
5. The 12 Progressive Harness Mechanisms — How Claude Code layers production features on the agent loop

## README content beyond ToC

- **The Agent Pattern** — minimal agent loop diagram + production-grade harness framing
- **Data Flow: A Single Query Lifecycle** — ASCII flow `processUserInput → fetchSystemPromptParts → recordTranscript → query loop → tool execution → tool_result append → loop or yield`
- **Tool System Architecture** — Tool interface lifecycle (validateInput / checkPermissions / call / isConcurrencySafe / isReadOnly / isDestructive / interruptBehavior + rendering + AI-facing prompt)
- **Complete Tool Inventory** — 40+ tools grouped (FILE OPS / SEARCH / EXECUTION / WEB / AGENT / MCP / SKILLS / INTERACTION / PLANNING / SYSTEM)
- **Permission System** — validateInput → PreToolUse hooks → permission rules (alwaysAllow/Deny/Ask) → interactive prompt → checkPermissions → APPROVED → tool.call()
- **Sub-Agent & Multi-Agent Architecture** — FORK / REMOTE / IN-PROCESS TEAMMATE; spawn modes (default / fork / worktree / remote); SendMessageTool / TaskCreate / TeamCreate; SWARM mode feature-gated
- **Context Management (Compact System)** — autoCompact (summarize) + snipCompact (trim) + contextCollapse (restructure)
- **MCP Integration** — stdio / sse / http / ws / sdk transports + OAuth 2.0 + Cross-App Access (XAA / SEP-990) + `mcp__<server>__<tool>` naming
- **Bridge Layer** — Claude Desktop / Web / Cowork ↔ Claude Code CLI via JWT + work secret + session lifecycle + capacityWake
- **Session Persistence** — `~/.claude/projects/<hash>/sessions/<session-id>.jsonl` append-only log + resume / continue / fork-session
- **Feature Flag System** — Bun compile-time DCE + `feature('FLAG_NAME')` + 21+ flags listed (KAIROS / VOICE_MODE / DAEMON / etc.)
- **State Management** — AppState Store (toolPermissionContext + fileHistory + attribution + verbose + mainLoopModel + fastMode + speculation)
- **The 12 Progressive Harness Mechanisms** — s01-s12 numbered breakdown of agent-loop layers
- **Key Design Patterns** — AsyncGenerator streaming / Builder + Factory / Branded Types / Feature Flags + DCE / Discriminated Unions / Observer + State Machine / Snapshot State / Ring Buffer / Fire-and-Forget Write / Lazy Schema / Context Isolation

---

## Anthropic-internals research framing (verbatim or paraphrased)

The README positions the work as:
1. **Educational** — "help developers better understand and utilize Agent technologies"
2. **Compiled-from-public-sources** — explicit non-claim of original reverse-engineering or insider-leak
3. **Continuing series** — "We will continue to share more insights and practical discussions on Agent architecture in the future"
4. **Subject-respectful but disclosure-forward** — full ASCII architecture diagrams + named feature flags + ant-only feature enumeration
5. **Removal-on-request** — DMCA-style "If any content infringes upon your legal rights ... please contact us and we will verify and remove it immediately"

This framing parallels system-prompts-leaks v21 (sister-archive same pattern family) but with **subject-narrowness** difference:
- v21: 31 AI tools (multi-tool prompt collection)
- v53: 1 AI tool (Claude Code single-tool internals deep-dive)

→ Pattern #38 sub-variant 38b candidate at structural-N=2.

---

## Cluster takeaway

**learn-coding-agent v53** is a CN-author solo research-archive of Claude Code v2.1.88 internals, quadrilingual EN+CN+JA+KO, 4 READMEs + 20 deep-dive reports = ~24 primitives total, abandoned 24 days after creation despite 11.7K stars and CORPUS-RECORD 168.2% fork-to-star inversion. Structurally sister-archive to system-prompts-leaks v21 with single-tool-deep-dive vs multi-tool-collection axis distinction. Operationally relevant to Storm Bear vault as Claude Code daily-use caveat reference (telemetry / undercover / killswitches) but NOT pilot-candidate (informal research-only-non-commercial-restriction blocks commercial re-use).
