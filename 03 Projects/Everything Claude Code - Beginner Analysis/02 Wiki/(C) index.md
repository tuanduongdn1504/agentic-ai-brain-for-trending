# (C) Index — Everything Claude Code Wiki

> Catalog toàn bộ wiki pages. Cập nhật sau mỗi lần ingest.
> Catalog of all wiki pages. Updated after every ingest.

## 🎉 Milestones (2026-04-17)

- ✅ **Trinity guides** ingested: Shortform + Longform + Security
- ✅ **Foundation entity pages: 7/7 complete** — Skills, Commands, Hooks, Subagents, Rules/Memory, MCPs, Plugins
- 📊 **Count verified:** 48 agents, 185 skills, 79 commands (match README Quick Start)
- 🚀 **First published guide shipped:** `03 Published/(C) Everything Claude Code - Huong dan cho nguoi moi.md` (v1, bilingual)
- 🐛 **4 contribution opportunities identified:** rules README count, VI translation, mgrep benchmark, plugin.json agents manifest drift (38 vs 48)

## Published guides

| Guide | Version | Audience | Date |
|-------|---------|----------|------|
| `03 Published/(C) Everything Claude Code - Huong dan cho nguoi moi.md` | v1 | Dev team (beginners) | 2026-04-17 |

## Sources (Nguồn gốc)

| Page | Summary | Ingested |
|------|---------|----------|
| [[(C) README summary]] | Tổng quan repo `everything-claude-code` — 48 agents, 183 skills, 79 commands; định vị là "agent harness performance system" | 2026-04-17 |
| [[(C) Shortform Guide summary]] | Foundation guide chính thức của ECC — 7 building blocks (Skills, Commands, Hooks, Subagents, Rules, MCPs, Plugins), context-window discipline, setup mẫu của tác giả, beginner action plan 4 tuần | 2026-04-17 |
| [[(C) Longform Guide summary]] | Advanced layer — token economics (model selection, MCP→CLI+skill, mgrep), memory persistence (session files, dynamic system prompt, memory hooks), continuous learning (Stop-hook), pass@k vs pass^k, parallelization (worktrees, cascade), iterative retrieval, sequential phases, two-instance kickoff | 2026-04-17 |
| [[(C) Security Guide summary]] | Trinity guide cuối — threat model post-CVE (2 real CVE Feb 2026), lethal trifecta, 6 defense layers (sandboxing, sanitization, approval, observability, kill switches, memory discipline), 11-item minimum bar checklist, AgentShield scanner. **"Never let the convenience layer outrun the isolation layer."** | 2026-04-17 |

## Concepts (Khái niệm)

_Chưa có entity page riêng. Concepts được trải khắp 3 summary pages — sẽ tách khi có ≥3 sources nói về cùng concept._

**7 building blocks (foundation) cần entity page:**
- [x] **Skills** — ✅ [[(C) Skills]] created (includes continuous-learning v2 case study)
- [x] **Commands (legacy)** — ✅ [[(C) Commands]] created (79 commands categorized, migration paths documented)
- [x] **Hooks** — ✅ [[(C) Hooks]] created
- [x] **Subagents** — ✅ [[(C) Subagents]] created
- [x] **Rules / Memory** — ✅ [[(C) Rules and Memory]] created (15 rule directories categorized)
- [x] **MCPs** — ✅ [[(C) MCPs]] created (27 pre-configured MCPs, security-aware, OWASP MCP Top 10 integrated)
- [x] **Plugins** — ✅ [[(C) Plugins]] created (manifest anatomy + validator quirks + security)

**Advanced concepts (longform) cần entity page:**
- [ ] Token economics — model selection table (Haiku/Sonnet/Opus), pricing
- [ ] Memory persistence — session files, dynamic system prompt, PreCompact/Stop/SessionStart hooks
- [ ] Continuous learning — Stop-hook pattern (v1); v2 instinct-based (chưa rõ chi tiết)
- [ ] Verification — pass@k vs pass^k, checkpoint vs continuous evals
- [ ] Parallelization — git worktrees, cascade method, two-instance kickoff
- [ ] Iterative retrieval — sub-agent context problem + 4-step loop
- [ ] Sequential phases orchestration — 5-rule pattern
- [ ] `mgrep` — ~50% token reduction vs grep/ripgrep

## Entities (Thực thể: Building blocks, Skills, Agents, Commands)

| Page | Type | Sources synthesized | Status |
|------|------|--------------------|--------|
| [[(C) Hooks]] | Building block #3 | 4 (README + shortform + longform + hooks/README) | ✅ Created — first entity page, format prototype, retrofitted |
| [[(C) Subagents]] | Building block #4 | 6 (README + shortform + longform + planner.md + code-reviewer.md + harness-optimizer.md) | ✅ Created — second entity page, format re-tested |
| [[(C) Skills]] | Building block #1 (primary) | 5 (README + shortform + longform + tdd-workflow/SKILL + continuous-learning-v2/SKILL) | ✅ Created — third entity page, includes case study giải Q15 |
| [[(C) Rules and Memory]] | Building block #5 | 7 (README + shortform + longform + rules/README + 3 rule files) | ✅ Created — fourth entity page, foundation 4/7 done |
| [[(C) MCPs]] | Building block #6 | 6 (README + shortform + longform + security + mcp-configs/mcp-servers.json + mcp-server-patterns SKILL) | ✅ Created — fifth entity page, security-aware, 27 MCPs categorized |
| [[(C) Plugins]] | Building block #7 | 5 (README + shortform + plugin.json + marketplace.json + PLUGIN_SCHEMA_NOTES) | ✅ Created — sixth entity page, flagged 38→48 agent manifest discrepancy |
| [[(C) Commands]] | Building block #2 (LEGACY) | 5 (README + shortform + plan.md + learn.md + cross-ref Skills) | ✅ Created — **seventh entity page; FOUNDATION 7/7 COMPLETE** 🎉 |

## Roadmaps (Lộ trình)

- **Beginner action plan 4 tuần** — đề xuất ban đầu, embed trong [[(C) Shortform Guide summary]]. Sẽ tách thành page độc lập sau khi đọc longform guide.

## Logs

- [[(C) log]] — chronological activity log
