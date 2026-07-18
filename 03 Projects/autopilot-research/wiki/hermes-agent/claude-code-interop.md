# Hermes Agent × Claude Code — What the Integration Actually Is

## Source
`raw/2026-07-18-hermes-agent/t8-ai-labs-claude-code.md` (AI LABS, "Hermes Agent under Claude Code Is Insane") + official docs. Verified via `wf_06a79485-687` (**C17 = FALSE as literally phrased**; the real mechanism is documented below).

## The correction first (Rule 12 — fail loud)
- The video's framing — **"run Hermes *under* Claude Code"** — is **inaccurate**. Claude Code (Anthropic's coding agent) and Hermes (Nous Research's standalone agent process) are **independent systems from different vendors**. Official Hermes docs list **no Claude Code integration** among their 20+ platforms/providers. Hermes does not "run under" Claude Code, nor vice-versa.
- What *is* real is **DIY interop via MCP** — which the video actually demonstrates. So the honest statement is: *"Hermes and Claude Code can be wired together through MCP; neither runs 'under' the other."*

## The actual mechanism (accurate)
Two independent bridges, both user-configured:
1. **Hermes-as-MCP-server → for Claude Code:**
   - `hermes mcp serve` starts Hermes as an **MCP server** (no terminal output when up — a documented gotcha).
   - Add it to `.mcp.json` at **project scope**, or to the root `.claude` config for **all projects**.
   - Effect: Claude Code (which "doesn't remember anything about you and whose skills don't self-improve") gains access to **Hermes' memory, skills, and every channel/app already connected to Hermes** — without wiring each app to Claude Code separately.
2. **Hermes → launches Claude Code (bundled skill):**
   - Hermes ships a **"Claude Code skill"** with guidance on driving Claude Code in **non-interactive mode**.
   - Effect: Hermes (always-on) can **launch Claude Code to build/fix features** on a schedule — e.g. a cron job watches a Slack channel → maintains a PRD skill → invokes Claude Code to implement, and syncs updated skills back to the local project so Claude Code keeps context.

## Example workflow shown (business automation)
- Cron job monitors a team Slack channel → builds an **evolving PRD skill** from the discussion → pulls relevant PRD slices into context on demand → runs every 30 min, syncing changes **both ways** between the Hermes skill and the project.
- Also: "bolt Hermes onto a deployed app" — Claude Code authors monitoring/health-check skills (it has best context on the app) → imported into Hermes → Hermes cron-runs them and syncs fixes back.

## ⚠️ Secondary claims NOT verified here (do not assert)
- **The "greedy little Dario" / Anthropic pricing claim** (t8): that after **June 15** you can't use a Claude Code *subscription* to run third-party agents (like Hermes) "for free" — that plans include a monthly **agent-SDK credit** consumed when a third-party app connects, and that non-interactive mode is affected. This is an **unverified secondary claim about Anthropic policy** wrapped in ad-hominem framing; it was not part of the primary fact-check and should be checked against Anthropic's own pricing docs before being relied on. (Relevant to [[claude-api-cost-optimization|claude-api-cost-optimization]].)
- Skill/tool counts vary by source and version ("90 skills default" t8 vs "68 skills / 28 tools" t1 vs "60+ tools" docs) — version-dependent; don't pin one number.

## Key Takeaways
- **"Hermes runs under Claude Code" is FALSE** — but a real, useful **MCP-based interop exists in both directions** (Hermes-as-MCP-server for Claude Code; Hermes launching Claude Code via a bundled skill).
- The genuinely interesting pattern: **Hermes gives Claude Code persistent memory + self-evolving skills + always-on channel access it otherwise lacks** — this is the Goal-relevant angle (an orchestration/memory layer *around* Claude Code, not a replacement).
- Verify the Anthropic June-15 subscription-pricing claim independently before acting on it — it is unconfirmed here.
- Cross-links: [[claude-code-memory-systems|claude-code-memory-systems]], [[multi-agent-orchestration|multi-agent-orchestration]], [[harness-engineering|harness-engineering]].
