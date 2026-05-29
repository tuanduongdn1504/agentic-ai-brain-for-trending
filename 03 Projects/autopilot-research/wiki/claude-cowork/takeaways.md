# Takeaways — 9 actionable rules

The corpus-distilled list of what to actually do when implementing Claude Cowork. Each rule has cross-references to the article(s) that go deeper.

## Source

- Raw: [`raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md`](../../raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md), §Takeaways

## The 9 rules

### 1. Enforce strict sandboxing

Create a dedicated **"Claude Workspace"** or sandbox folder; grant Cowork access ONLY there. Prevents irreversible file modifications + accidental deletion of system data. **No Cowork undo exists** (Tech With Tim).

→ See [[sandboxing-and-workspace-structure]]

### 2. Maintain persistent context files

Store "Business Brain" / preferences in persistent `.md` files. Set a **Global Instruction** for Claude to read these first → consistent tone + strategy across sessions.

→ See [[contextual-engineering]] for the 4 patterns (minimalist / specialist / strategic-injection / automated brain-dump)

### 3. Optimize for script-based processing

For bulk data work: ask Claude to **write a local script** that parses the data; embed the script in a skill. Don't have the LLM analyze every file individually.

→ Bart Slodyczka's tactic — see [[token-and-cost-management]]

### 4. Circumvent the app-open requirement (if needed)

Standard Cowork scheduling requires the desktop app open. If you need true background autonomy: use **Kenny Liao's custom cron plugin** or **Jack Roberts's Railway alternative**.

→ See [[scheduling-and-the-app-open-constraint]] for both workarounds

### 5. Prevent context rot

Clear task history or open new windows **every 30-45 minutes** during focused sessions. Old conversation data inflates token costs on every subsequent message.

→ Jack Roberts's tactic — see [[token-and-cost-management]]

### 6. Leverage parallel sub-agents

For time-sensitive data gathering: explicitly instruct Claude to **"run in parallel"** to dispatch multiple sub-agents simultaneously. Trades credits for wall-clock speed.

→ Tech With Tim's tactic — see [[token-and-cost-management]]

### 7. Apply the handover test

Codify a workflow into a **Plugin** (not just a Skill) only if it passes the **handover test**: someone else could execute the process from the file alone, without asking questions.

→ Jack Roberts's criterion — see [[skills-to-plugins-pipeline]]

### 8. Inject strategic context

Give Claude access to local folders containing **roadmaps + vision documents**. Lets it evaluate outputs against your business goals, not generic best practices.

→ Stefan Wirth's tactic — see [[contextual-engineering]] (Pattern C)

### 9. Utilize remote dispatch

Enable Cowork's **"Dispatch" feature** in settings → trigger tasks on your computer from your mobile phone while away from desk. Only the corpus's Tech With Tim mentions this; underexplored elsewhere.

## Implicit rule the corpus doesn't enumerate but should

### 10. Default to Sonnet, escalate to Opus

Strongest consensus signal in the corpus across N=3+ speakers, despite not being in the "Takeaways" section of the raw analysis. **Sonnet handles most Cowork tasks**; escalate to **Opus only when quality demonstrably suffers**.

→ See [[token-and-cost-management]]

## How to apply these rules

For a **first Cowork deployment**: rules 1, 2, 7, 10 are the baseline. Skip the cost-optimization ones (3, 5, 6) until you have actual cost data.

For a **scaled Cowork deployment**: add rules 3, 4, 5, 8. Cost management becomes load-bearing once multiple scheduled tasks compound daily.

For **enterprise / business deployment**: see [[production-readiness-gaps]] — the 9 takeaways don't cover what enterprise needs.

## Storm Bear vault application

The autopilot-research project itself satisfies several of these rules:

| Rule | Vault instance |
|---|---|
| 1 (sandbox) | Constitutional rule #1: READ-ONLY outside `03 Projects/autopilot-research/` |
| 2 (persistent context) | `CLAUDE.md` at vault + project + topic levels |
| 4 (cron workaround) | `bot-start.sh` + launchd UserAgent (closer to Kenny's pattern than Cowork's default) |
| 7 (handover test) | Promotion criteria for autopilot wiki → Storm Bear curated wiki |
| 8 (strategic context) | Vault `GOALS.md` + per-project goals folders |
| 10 (Sonnet default) | Routine v2.2 default model choice in skills |

The vault is essentially a **Cowork-shaped deployment at the vault-management layer**.

## Key Takeaways

- **9 explicit rules** from the corpus + 1 implicit (Sonnet-default) makes 10
- **Rules 1, 2, 7, 10** are the minimum viable Cowork deployment
- **Several rules map directly to existing Storm Bear vault discipline** — validates the vault's pattern as Cowork-aligned at a higher level of abstraction
- **For production**: the 9 rules are necessary but not sufficient — see [[production-readiness-gaps]]

## Related

- [[overview]] — start here
- [[sandboxing-and-workspace-structure]] — rule 1
- [[contextual-engineering]] — rules 2, 8
- [[token-and-cost-management]] — rules 3, 5, 6, 10
- [[scheduling-and-the-app-open-constraint]] — rule 4
- [[skills-to-plugins-pipeline]] — rule 7
- [[production-readiness-gaps]] — what these rules don't cover
