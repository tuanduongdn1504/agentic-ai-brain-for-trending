# (C) larksuite/cli — Pattern Library Phase 4b (v143)

**Routine v2.6 · §28 (single registry / ≤2-new-standalones / clustering-first / filing-is-an-act).**

## PRIMARY — 1 NEW Library-vocab standalone (FILED to registry 06 §C)

### "Agent-Native Vendor CLI: a CLI surface co-designed for AI-agent consumption" — N=1 CORPUS-FIRST
- **What:** a vendor's official CLI whose *command surface is architected for AI agents*, not just humans — specifically the combination: (1) an agent-friendly **shortcut tier** (`+`, smart defaults + table output + **dry-run previews** so an agent can preview before mutating), (2) **identity-switching** (`--as user|bot`) as a first-class agent primitive, (3) a **non-blocking device-code auth handoff** (`--no-wait` returns the auth URL immediately for the agent to relay to its user; resume via `--device-code`) built for headless agent operation, (4) a **bundled AI-Agent-Skills layer** (26 skills + `lark-skill-maker`), over (5) a graceful three-layer command model (shortcuts / curated-API / raw-API).
- **Why it's its own mechanism:** the corpus has MCP servers that expose a vendor to agents (v140 google_workspace_mcp, v66, v70, v132) and standalone skill collections (the 57k chain), but this is the first subject where the **CLI itself** is the agent-native surface, with **agent-auth affordances** (identity-switching + device-code handoff) that neither an MCP server nor a skills repo carries. The novel axis = "the CLI is the agent interface, with auth/identity primitives designed for headless agents."
- **Distinct from:** v140 google_workspace_mcp (MCP-server delivery of the same goal); Pattern #18 B1 MCP (this has no MCP); the agentskills.io skill collections (a CLI, not a skills-only repo).
- **Promotion-eligibility:** N=2 if a 2nd vendor ships an explicitly agent-native CLI with comparable agent-auth affordances. **Stale-watch ~v158.**
- **§28 new-standalone count this ship = 1 (≤ 2).** Registry 06 §C edited (rule-5).

## SECONDARY — observations / instance notes (NOT minted)

- **Productivity-suite agent-connectivity cluster — OBSERVATION (v140 + v143, N=2-forming).** Two delivery patterns for the same goal ("give an autonomous agent control of a vendor productivity suite"): **MCP server** (v140 google_workspace_mcp, Google Workspace) vs **agent-native CLI + skills** (v143 larksuite/cli, Lark/Feishu). A genuinely useful comparison; logged as a cluster, NOT minted (the two members are structurally different deliveries — clustering-first, mint a class only if a 3rd appears).
- **Pattern #57 / agentskills.io 57k chain — implementer-CANDIDATE (honest, NOT asserted).** The 26 skills are Lark-native in *content* but **distributed via `npx skills add larksuite/cli`** = the vercel-labs skills CLI that anchors the 57k distribution chain. So it rides the 57k *distribution* mechanism without adopting the SKILL.md *spec* internals. Recorded as a candidate for the next audit's 57k-chain reconciliation (the chain's count is already flagged ~13-14 approximate); NOT counted as a confirmed implementer here.
- **Pattern #84 agent-tooling / multi-consumer — N+1 (modest).** A CLI explicitly for humans AND agents; not N native harness formats, so weaker than a true 84c multi-format generator.
- **Agent-auth affordances — sub-note (folded into the PRIMARY).** Non-blocking device-code auth-handoff + user/bot identity-switching are the most novel single elements; kept inside the PRIMARY standalone rather than minted separately (anti-inflation). Loosely connects to the v67 opencode-antigravity-auth OAuth-credential-bridge thread.

## Pattern Library state change: NONE
46 confirmed / ~25 active / 8 Library-vocab CONFIRMED → UNCHANGED. PROVISIONAL standalone surface +1 (Agent-Native Vendor CLI). NO top-level Pattern, NO tier sub-archetype, NO confirmed-count movement.

## Audit hand-off note
v143 hands the overdue ~v139–v140 audit: (1) the **productivity-suite agent-connectivity cluster** (v140 MCP + v143 CLI) as a candidate class to watch; (2) one more data point for the **57k-chain reconciliation** (larksuite rides `npx skills add` but with Lark-native content — does "distributes via the skills CLI" count toward the chain?); (3) NOTHING for the override-frequency / generate-vector threads (v143 is a clean goal-aligned ship, unrelated). §35 is now clear again after the v142 off-goal override.
