# (C) Pilot menu — applying `github-copilot-cli-agents` to your working flow

> **From:** wiki topic [[github-copilot-cli-agents]] (video: Chris Noring/Microsoft, *"From Writing Code to Designing Systems"*, AI Engineer conference, 2026-07-11).
> **For:** Storm Bear — the **hireui** recruitment SaaS (Goal #2: ship software with these tools) + vault harness work.
> **Date:** 2026-07-13.
> **How to read:** 9 methods in 4 tiers, each with *what / why / effort / risk / success signal*. Threads tagged: 🚢 async-delegation · 🧩 harness/vocabulary · 🔍 MCP tooling · 📎 governance. Ranked recommendation at the bottom.

**The one big idea to carry across every method:** this isn't a "steal Copilot's tools" topic the way the AI-Studio or local-AI topics were — hireui is Claude-Code-only by constitution (I-8/I-2), and nothing here argues for changing that. What it *is* good for: (1) borrowing GitHub's own clean vocabulary for constructs hireui already has (custom agents ≈ subagents), (2) confirming zero lock-in risk on the skills bet already made, (3) **one genuinely testable pilot** — whether Claude Code's Routines-with-GitHub-triggers can replicate the exact "assign issue → walk away → draft PR" workflow Copilot has GA'd since 2025-09-25.

---

## Tier A — Try-it-this-week (zero hireui-repo risk)

### A1 · Confirm/add Playwright MCP + GitHub MCP to hireui's Claude Code config 🔍 ⭐
- **What:** Check whether hireui's `.mcp.json` (or equivalent) already wires up [`microsoft/playwright-mcp`](https://github.com/microsoft/playwright-mcp) and [`github/github-mcp-server`](https://github.com/github/github-mcp-server). If not, add them — both are first-party, actively maintained, and usable from Claude Code exactly as they are from Copilot (same protocol, same servers).
- **Why:** This is the single cleanest, lowest-risk adoption in the whole topic — GitHub's own demo treats these as *default-enabled*, and they cost nothing to try since MCP is vendor-neutral by design.
- **Effort:** ~30-60 min. **Risk:** none.
- **Success signal:** a subagent can drive a browser (Playwright MCP) or read/manage a hireui issue/PR (GitHub MCP) from a Claude Code session without custom glue code.

### A2 · Relabel hireui's subagent docs with the "persona + tools + orchestration" vocabulary 🧩
- **What:** hireui's `.claude/agents/*.md` subagents already have the shape GitHub calls a "custom agent" (persona, `tools:` allowlist, optional MCP access, can delegate to sub-agents). Update the harness docs to use this cleaner three-part framing (persona / tool-constraint / orchestration-level) when explaining *why* a construct is a subagent vs. a skill.
- **Why:** Cheap clarity win for onboarding juniors — see [[custom-agents-vs-subagents]] for the side-by-side field table to lift directly.
- **Effort:** ~1 hour (docs only, no functional change). **Risk:** none.
- **Success signal:** a junior can correctly explain "skill vs subagent" using the persona/tools/orchestration framing without re-deriving it.

---

## Tier B — Goal #2 (deploy-layer / async-workflow parity)

### B1 · Pilot a Routine-with-GitHub-trigger to replicate "issue → draft PR" on hireui 🚢 ⭐
- **What:** On a **throwaway or `agent-*` sandbox branch**, configure a Claude Code Routine with a GitHub-event trigger (e.g. "issue opened with label X") that spins up a session, does the work, and opens a PR — the direct Claude-side test of the exact workflow Copilot's coding agent has had GA since 2025-09-25 (see [[coding-agent-issue-to-pr]] and [[claude-code-parity-and-gaps]]).
- **Why:** This is the one place this topic identified a genuine capability question rather than a "already have it" or "doesn't apply" answer. Routines-on-events is the closest documented Anthropic mechanism, but nobody in this corpus has actually run it against a real repo's issue-driven workflow yet.
- **Effort:** ~half a day (setup + one test issue end-to-end). **Risk:** low — sandbox branch only, draft PR requires human merge either way.
- **Success signal:** an issue opened on the sandbox branch results in an unattended Claude Code session opening a PR, with a clear note on what triggers worked/didn't and how it compares in setup time to Copilot's issue-assign button.

### B2 · One-line bake-off note for the deploy-layer decision log 🚢
- **What:** If B1 is run, add its findings (setup time, trigger reliability, cost) as a data point next to the existing [[fullstack-docker-cicd/_index|fullstack-docker-cicd]] deploy-layer bake-off notes — not because hireui will ever run Copilot, but because "async-agent-to-PR setup cost" is a comparable axis worth having a number for.
- **Why:** Keeps Goal-#2 tooling decisions evidence-based rather than assumption-based.
- **Effort:** ~15 min, only after B1. **Risk:** none.
- **Success signal:** one added row in the existing comparison doc.

---

## Tier C — Watch, don't build

### C1 · Track the Claude Code AGENTS.md issue cluster (#6235 + duplicates) 🧩
- **What:** No action now — just note that if/when Anthropic ships native AGENTS.md support in Claude Code, hireui gets free interop with any Copilot-based collaborator on the same repo, at zero migration cost (CLAUDE.md stays authoritative either way per GitHub's own "reads both" behavior).
- **Why:** Free optionality; costs nothing to simply know this is pending.
- **Effort:** 0 (watch-item). **Risk:** none.
- **Success signal:** n/a — revisit if Anthropic ships it.

### C2 · Track custom-agent `argument-hint` field stability 🧩
- **What:** GitHub's own docs reportedly flag this frontmatter field's support as uncertain as of early 2026 (see [[custom-agents-vs-subagents]] caveat). Not relevant to hireui directly (Claude Code subagents don't use this field), but worth a mental note if hireui ever collaborates with a Copilot-custom-agent-using team.
- **Effort:** 0. **Risk:** none.

---

## Tier D — Governance (cheap, protective)

### D1 · ADR: hireui stays on CLAUDE.md, no parallel AGENTS.md 📎 ⭐
- **What:** A one-paragraph CONSTITUTION note: *do not add an AGENTS.md file to hireui "for portability" — Claude Code does not read it, so it would be dead weight that could drift out of sync with the real CLAUDE.md.* If cross-tool interop is ever needed, revisit once Anthropic ships native support (see C1).
- **Why:** This is exactly the kind of thing a well-meaning contributor does after watching a talk like this one — add a file that looks like best practice but does nothing on Claude Code, and then two files silently disagree.
- **Effort:** ~15 min. **Risk:** none — pure protection.
- **Success signal:** the ADR merged; nobody accidentally forks hireui's repo intent across two files.

### D2 · Teaching note: Agent Skills is a shared open spec, not a Claude bet 📎
- **What:** A short note for the team: hireui's `.claude/skills/` investment is portable (agentskills.io, also used by GitHub Copilot) — it is not vendor lock-in, and the folder+`SKILL.md` shape would transfer largely unchanged if hireui ever needed a Copilot-side collaborator to read the same skill definitions.
- **Why:** Removes a hypothetical objection to the skills investment before anyone raises it.
- **Effort:** ~15 min. **Risk:** none.

---

## Ranked recommendation

1. **A1 — add Playwright MCP + GitHub MCP** 🔍⭐ — zero-risk, immediate, matches what's already default-enabled on the other side of the fence.
2. **D1 — the AGENTS.md non-adoption ADR** 📎⭐ — cheap insurance against a well-intentioned but wasted file addition.
3. **B1 — the Routines-with-GitHub-trigger pilot** 🚢⭐ — the one genuinely open question this topic surfaced; half a day to get a real answer instead of an inference.
4. **A2 / D2** — cheap documentation/framing wins, slot in anytime.
5. **C1 / C2 / B2** — watch-items and follow-on notes, no urgency.

**What NOT to do:** don't add AGENTS.md to hireui expecting Claude Code to read it (it won't); don't treat this topic as a reason to evaluate switching hireui off Claude Code (nothing here suggests Copilot is ahead — the constructs are architecturally equivalent, and Claude Code's subagent config surface is documented as richer).

## Next action
Run **A1** today (near-zero effort), write **D1** in the same sitting, and schedule **B1** for the next half-day slot available for Goal-#2 tooling work.
