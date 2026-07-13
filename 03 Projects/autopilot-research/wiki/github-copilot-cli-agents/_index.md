# github-copilot-cli-agents

> **Topic:** GitHub/Microsoft's own version of the agentic-dev-scaling stack — AGENTS.md → Agent Skills → custom agents → CLI `/delegate` / issue-assign → draft PR — told by a Microsoft Cloud Developer Advocate at the AI Engineer conference, mid-2026.
> **Compiled:** 2026-07-13 from a single operator-submitted YouTube video (path 5, yt-dlp-only, full transcript read in main loop) + a double-dive into the FIRST-PARTY GitHub/Microsoft/Anthropic originals beneath every mechanism it names.
> **Source video:** [GdvKNwMcfd0](https://www.youtube.com/watch?v=GdvKNwMcfd0) — **Chris Noring** (Microsoft, Cloud Developer Advocate; GitHub `softchris`), *"From Writing Code to Designing Systems: How the Developer Role is Changing"* (AI Engineer conference channel `@aiDotEngineer`, 2026-07-11, 23:05, ~8.5K views at ingest).
> **Raw:** [../../raw/2026-07-13-github-copilot-cli-agents.md](../../raw/2026-07-13-github-copilot-cli-agents.md)
> **Verification:** Workflow `wf_a1693ef8-4dc` — 17 agents (8 first-party dives + 8 refute-first skeptics + 1 completeness critic; ~688K tokens, 232 tool calls, 0 errors/0 empty). Agents ran on Haiku 4.5; the critic caught a **suspected confabulated press-release quote** in one verdict, closed by a main-loop independent check (see [[source-provenance]]).

---

## The one-sentence thesis

This is the **first GitHub-Copilot-CLI-native topic in the corpus** — nearly every prior topic here is Claude-Code-centric or observes cross-vendor moves from the outside (e.g. `codex-plugin-cc`). Chris Noring's talk is GitHub/Microsoft's own internal version of the exact same "guardrails for agentic scaling" pattern this vault has been building up from the Claude side: **AGENTS.md** (repo-level intent) → **Agent Skills** (repeatable task recipes) → **custom agents** (persona + tools + orchestration) → **delegate-and-scale** (CLI `/delegate` or GitHub-issue-assign → sandboxed background agent → draft PR → human merges). The pleasant surprise: **it's an unusually high-integrity talk** — every concrete technical claim checks out against first-party docs once you correct one date and drop one likely-confabulated quote (see [[claims-scorecard]]).

## The 3-act structure (mirrors the talk)

| Act | Mechanism | GitHub/Copilot side | Claude Code side | Article |
|---|---|---|---|---|
| 1. Entry point | CLI-first workflow | GitHub Copilot CLI | Claude Code CLI | [[copilot-cli-and-delegate]] |
| 2a. Guardrail 1 | Repo-level intent doc | AGENTS.md (+ `.github/copilot-instructions.md`) | CLAUDE.md (does **not** read AGENTS.md) | [[agents-md-guardrail]] |
| 2b. Guardrail 2 | Repeatable task recipe | "Agent Skills" (`/skills`) | Agent Skills (`.claude/skills/`) — **same open spec** | [[agent-skills-shared-standard]] |
| 2c. Guardrail 3 | Persona + orchestration | Custom agents (`.github/agents/*.agent.md`) | Subagents (`.claude/agents/*.md`) | [[custom-agents-vs-subagents]] |
| 3. Scale | Async delegate → PR | `/delegate` + issue-assign → Copilot coding agent | Routines (GitHub-triggered) + Claude Tag | [[coding-agent-issue-to-pr]], [[claude-code-parity-and-gaps]] |
| (cross-cutting) | Tool access | MCP servers (GitHub MCP, Playwright MCP) | MCP servers (same protocol) | [[mcp-servers-in-copilot]] |

## Articles in this topic

- [[overview]] — the talk, corrected and annotated, act by act
- [[agents-md-guardrail]] — AGENTS.md: GitHub's real adoption (2025-08-28) vs. Claude Code's real non-adoption
- [[agent-skills-shared-standard]] — the best-verified finding: Copilot "Agent Skills" and Claude "Agent Skills" are the *same open spec*, not parallel invention
- [[custom-agents-vs-subagents]] — `.github/agents/*.agent.md` vs `.claude/agents/*.md`, side by side, plus the `argument-hint` caveat
- [[copilot-cli-and-delegate]] — GitHub Copilot CLI: GA history, `/delegate` mechanics, other slash commands
- [[coding-agent-issue-to-pr]] — the "assign issue → sandboxed agent → draft PR" flow, corrected GA date (2025-09-25, not "2026")
- [[mcp-servers-in-copilot]] — Playwright MCP + GitHub MCP, both real, both default-enabled
- [[claude-code-parity-and-gaps]] — what Claude Code has (subagents, skills, Routines, Claude Tag) and doesn't (no native AGENTS.md, no literal issue-assign button)
- [[claims-scorecard]] — all 8 claims graded (6 CONFIRMED / 2 CORRECT-BUT-INCOMPLETE / 0 misleading / 0 false)
- [[caveats-and-corrections]] — the confabulation the critic caught, softened unverified specifics, uncovered rhetorical claims
- [[source-provenance]] — video/channel/speaker provenance + verification workflow record

## Why this matters for Storm Bear / hireui

- **Vendor-neutrality validated.** [[agent-skills-shared-standard]] confirms Claude's `.claude/skills/` bet is a shared open standard (agentskills.io), not an Anthropic-proprietary format Copilot happens to imitate. Lowers lock-in risk for every skills-based hireui pattern already banked (`claude-code-skills-stack`, `google-antigravity-skills`, `jsm-six-file-context`).
- **hireui's CLAUDE.md is not "missing" AGENTS.md.** [[agents-md-guardrail]] confirms Claude Code genuinely does not read AGENTS.md natively — a large, unresolved, 2025-08-vintage community ask. hireui should keep CLAUDE.md as its source of truth; no action needed.
- **Direct construct mapping.** GitHub's "custom agent" (persona + tool allowlist + MCP + orchestration) is architecturally the same shape as a Claude Code subagent at `.claude/agents/*.md` — see [[custom-agents-vs-subagents]] for the field-by-field table. hireui's BMAD harness already uses this shape; nothing new to adopt, but useful vocabulary/framing to borrow.
- **The delegate→draft-PR→human-merge pattern** is GitHub's mature, GA-since-2025-09 version of exactly what Anthropic's Routines (GitHub-triggered) + Claude Tag do on the Claude side — see [[claude-code-parity-and-gaps]] for the honest gap analysis (Routines are event-triggered, not "assign this issue" triggered; there's no literal Claude-side "assign to agent" button yet).

## Cross-links to existing corpus

- [[../claude-code-skills-stack/_index|claude-code-skills-stack]] — the Claude-side Agent Skills ecosystem this topic's [[agent-skills-shared-standard]] directly parallels
- [[../google-antigravity-skills/_index|google-antigravity-skills]] — a third vendor (Google) on the same Agent Skills / AGENTS.md convergence trend
- [[../jsm-six-file-context/_index|jsm-six-file-context]] — AGENTS.md-vs-CLAUDE.md portability already explored from the Claude side (Vercel's "AGENTS.md outperforms skills" eval)
- [[../multi-agent-orchestration/_index|multi-agent-orchestration]] — custom-agent orchestration patterns, cross-vendor
- [[../harness-engineering/_index|harness-engineering]] — "guardrails" framing is this project's harness-over-model thesis, told from Microsoft's side
- [[../claude-tag-multiplayer-agent/_index|claude-tag-multiplayer-agent]] — Anthropic's own async-agent-to-PR product, the direct comparison point for [[coding-agent-issue-to-pr]]
