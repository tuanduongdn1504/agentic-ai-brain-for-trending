# Anthropic Cowork first-party docs — Path 4 multi-URL ingest

**Notebook:** def7ce93-5ef6-4af6-94af-504f2b288ca6
**Sources:** 2 first-party URLs (Anthropic-owned domains)
**Generated:** 2026-05-30 (manual Path 4 — `notebooklm notebook create + source add ×2`)
**Operator:** Claude (in /Users/Cvtot/KJ-OS-autopilot worktree)
**Closes:** claude-cowork wiki surviving gap #1 (Anthropic first-party docs absent)

## Sources

1. **Overview - Claude.ai Documentation** — https://claude.com/docs/cowork/overview
   - Source ID: 9dfccd2c-9d8c-4aa0-8443-2b0123bc6827
   - Status: ready
2. **Get started with Claude Cowork | Claude Help Center** — https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
   - Source ID: f712f0aa-9185-4f6f-82db-9867a33e1eb4
   - Status: ready

---

## 1. Summary

Claude Cowork is an agentic workspace integrated into the Claude Desktop app that enables the AI to perform complex, multi-step tasks autonomously. Unlike standard chat interfaces, this feature can **directly access local files**, execute code in a secure environment, and manage parallel workstreams to produce professional deliverables like spreadsheets and presentations. The system is designed for **paid subscribers** on macOS and Windows, allowing users to schedule recurring jobs or assign tasks remotely via mobile devices. Users can further customize the experience through **projects and plugins**, which provide persistent memory and specialized skills for specific workflows. While the tool offers significant automation, it maintains **safety protocols** by requiring explicit permissions for file deletions and offering different levels of oversight. Ultimately, these sources provide a comprehensive guide on **setting up, managing, and troubleshooting** this high-compute productivity tool.

---

## 2. Cowork-vs-Code-vs-Chat official taxonomy

Claude Cowork "brings Claude Code's agentic capabilities to Claude Desktop for **knowledge work beyond coding**". Cowork and Code use the same agentic architecture; Cowork is accessible within Claude Desktop **without opening the terminal**.

Distinctions from regular chat:
- **Task Execution:** Regular chat = "responding to prompts one at a time" / sequentially. Cowork = "take on **complex, multi-step tasks** and execute them on your behalf."
- **File and Local Access:** Cowork has "**direct local file access**" without manual uploads; standard chat is recommended for tasks that "don't require file access".
- **Automation and Scheduling:** Cowork supports "**scheduled tasks**" that allow Claude to complete work automatically on a cadence; this functionality "**isn't possible in regular chats**".
- **Persistence and Time:** Cowork is intended for "**long-running tasks**" that proceed for extended periods without "conversation timeouts or context limits" interrupting progress.
- **Usage Costs:** Cowork "**consumes more of your usage allocation** than chatting with Claude" — explicitly because it is compute-intensive.

### Summary table

| Feature | Regular Claude Chat | Claude Cowork | Claude Code |
|---|---|---|---|
| Primary Use | Simpler tasks | Knowledge work beyond coding | Coding |
| Interaction | Sequential prompts | Agentic, multi-step tasks | Agentic |
| Interface | Web/Desktop/Mobile | Claude Desktop app | Terminal (implied) |
| File Access | Manual uploads only | Direct local file access | Not explicitly detailed |
| Scheduling | Not supported | Supports recurring tasks | Not explicitly detailed |

(Anthropic's sources focus primarily on Cowork and only mention Code to establish shared agentic architecture; Code-specific feature details are not explicitly detailed in these documents.)

---

## 3. Scheduling: the app-must-be-open constraint is OFFICIAL ANTHROPIC POSITION

Anthropic's first-party docs explicitly state:

- **Direct requirement for scheduled tasks:** "Scheduled tasks only run while your computer is awake and the Claude Desktop app is open."
- **General task requirement:** "The Claude Desktop app must remain open and your computer must be awake for Claude to work on tasks. If you close the app or your computer goes to sleep, active tasks will stop."
- **Session termination:** "The Claude Desktop app must remain open while Claude is working. If you close the app, your session will end."
- **Troubleshooting guidance:** "Ensure the Claude Desktop app was open throughout the entire task. If the app was closed or your computer went to sleep, the session may have ended."
- **Remote control via mobile:** Pro and Max users can message Claude from a mobile device "while your desktop stays active" — confirms the constraint extends to remote scenarios.

**Implication:** The N=4-of-6 creator consensus from the 2026-05-29 claude-cowork drain (Tech With Tim + Bart Slodyczka + Stefan Wirth + Kenny Liao all naming the constraint) was CORRECT. Kenny Liao's cron-plugin workaround is a real (operator-built) circumvention of an officially-documented Anthropic limitation, not a fix for a bug.

---

## 4. Skills + Plugins official Anthropic definitions

### Official definitions

- **Skills:** "**Teach Claude reusable workflows with custom instructions**"
- **Plugins:** "**Shareable packages**" that "**bundle skills, connectors, and more**" — used to "**customize how Claude works for your role, team, and company in Cowork**"

### How Skills differ from Plugins

- **Composition:** A Plugin is a "**single package**" incorporating multiple elements. A Skill is a specific component (a workflow) that can be included within that package.
- **Bundling scope:** Plugins can bundle **Skills + connectors + sub-agents** — broader than just Skills.
- **Distribution:** Skills focus on workflow instruction; Plugins are specifically characterized as "**shareable packages**," designed for broader distribution across teams or organizations.

**This confirms the Prince + Wilson N=2 corpus-first two-tier hierarchy at N=3 with Anthropic first-party verification:**

| Tier | Anthropic's framing | Composition | Distribution |
|---|---|---|---|
| Skills | "Reusable workflows with custom instructions" | Single workflow | Per-operator (not shareability-emphasized) |
| Plugins | "Shareable packages" | Skills + Connectors + Sub-agents | Designed for cross-team/org distribution |

**Plugins bundle sub-agents** is a new architectural detail not in any prior corpus.

---

## What this drain does NOT cover

These 2 sources establish official positioning. They do NOT include:
- API/SDK documentation for programmatic Cowork access (separate docs surface)
- The `setup-cowork` Anthropic-skill content (different surface — vault skill registry, not claude.com docs)
- Specific connector inventory (Anthropic Connectors page is a sibling URL not in this ingest)
- Pricing tiers + usage allocation details (mentioned but not enumerated)

If future drain wants to close these too:
- Path 3 ingest of https://claude.com/docs/connectors/ (or wherever the connector docs live)
- Path 6 custom scraper for setup-cowork skill from vault registry source
- WebFetch on Anthropic pricing page for the Cowork-specific usage allocation
