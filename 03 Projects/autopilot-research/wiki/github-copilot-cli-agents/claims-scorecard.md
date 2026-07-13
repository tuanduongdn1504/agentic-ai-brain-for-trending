# Claims scorecard — all 8 claims graded

> Grades reconciled in the main loop from the [[source-provenance|17-agent workflow]] + independent main-loop checks. Where the verification workflow's own claim-mapping or a Haiku verifier drifted, the main-loop correction wins (noted).
> **Legend:** ✅ CONFIRMED · ◐ CORRECT-BUT-INCOMPLETE · ⚠️ MISLEADING · ❌ REFUTED/FABRICATED

| # | Claim (paraphrased) | Grade | One-line verdict |
|---|---|---|---|
| C1 | Copilot CLI `/delegate` sends session to GitHub, opens draft PR, runs async | ✅ | Exactly as demoed; GA Feb 2026, active dev. [[copilot-cli-and-delegate]] |
| C2 | Custom agents at `.github/agents/*.agent.md`, frontmatter incl. tools allowlist, one level above skills | ◐ | Location/hierarchy/tools all confirmed; `argument-hint` field support is unclear/possibly regressed — held as unverified, not asserted. [[custom-agents-vs-subagents]] |
| C3 | Skills are folder-based contracts, and "all the big vendors" (incl. Anthropic) converge on this | ✅ | Better than claimed — both vendors implement the **same open Agent Skills spec** (agentskills.io), not independent convergence. [[agent-skills-shared-standard]] |
| C4 | Issue "assign to agent" → sandboxed coding agent → draft PR, GA | ✅ | Real, GA — **corrected date: 2025-09-25**, not the "2026" date one verifier asserted (see [[caveats-and-corrections]]). [[coding-agent-issue-to-pr]] |
| C5 | Agent uses MCP servers (Playwright MCP, GitHub MCP) | ✅ | Both real, first-party, default-enabled. [[mcp-servers-in-copilot]] |
| C6 | AGENTS.md is the "bare minimum" repo-guardrail, and GitHub reads it | ✅ | Confirmed; GitHub added support 2025-08-28 alongside `.github/copilot-instructions.md`. **Separately** (not something Chris claimed, but worth knowing): Claude Code itself does not natively read AGENTS.md. [[agents-md-guardrail]] |
| C7 | Channel = AI Engineer conference; Chris Noring = genuine Microsoft practitioner | ◐ | Both confirmed real; minor imprecision — his historical public bio reads as general cloud/JS advocacy rather than "AI engineering" specifically (plausible his focus has shifted into 2026; not a red flag). [[source-provenance]] |
| C8 | Auto-captions render "AI slop" as "AI slope" | ✅ | Confirmed directly from the raw transcript ("many of you have heard the term AI slope... I see nods here") — a caption/ASR error, not a real term. "AI slop" itself is a well-established industry term. |

## Tally

- ✅ CONFIRMED: **6** (C1, C3, C4, C5, C6, C8)
- ◐ CORRECT-BUT-INCOMPLETE: **2** (C2, C7)
- ⚠️ MISLEADING: **0**
- ❌ REFUTED / FABRICATED: **0**

## Reading of the video

**High-integrity.** Zero misleading claims, zero fabrications from the speaker himself. Every concrete technical mechanism he demonstrates — AGENTS.md, skills, custom agents, `/delegate`, issue-assignment, MCP servers — checks out against GitHub's/Microsoft's own first-party documentation. The only corrections needed were (a) a minor uncertainty about one frontmatter field's current support status, and (b) a date correction for the coding agent's GA — and that correction was needed to fix a **verification-workflow artifact** (a Haiku verifier's likely-confabulated quote/date), not a speaker error. Compare this to [[../jasonlee-claude-mobile-app/_index|jasonlee-claude-mobile-app]] (6/12 misleading, business framing as theater) or [[../local-ai-coding-agents/_index|local-ai-coding-agents]] (0 false, "enthusiasm-over-claim" pattern) — this talk sits closer to the latter: measured, hedge-forward, no revenue claims, no hype metrics.

## See also
[[_index]] · [[caveats-and-corrections]] · [[overview]]
