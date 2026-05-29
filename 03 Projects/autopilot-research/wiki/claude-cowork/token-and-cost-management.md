# Token + cost management

How power users keep Cowork operations cheap enough to scale. Three independent tactics from three speakers.

## Source

- Raw: [`raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md`](../../raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md), §Trends-5 + §Outliers-2

## Tactic 1 — "Sonnet for most, Opus for hard" (consensus N=3+)

The strongest single signal in the corpus on model selection.

- **Tech With Tim, Kenny Liao, Stefan Wirth** all explicitly advocate:
  - **Claude 3.5 Sonnet** for most automated tasks → saves credits
  - **Opus** only for highly complex reasoning that Sonnet can't handle
- Default to Sonnet; escalate to Opus only when output quality demonstrably suffers
- This holds independent of which speaker — strong cross-source agreement

## Tactic 2 — Script-vs-agentic (Bart Slodyczka)

For data-processing tasks at volume:

- **Wrong** (expensive): let Claude analyze 100 invoices one-by-one — each LLM call burns tokens
- **Right** (cheap): tell Claude to **write a script** that parses the 100 invoices, then **embed that script** in a skill
- The skill runs the script locally; Claude orchestrates but doesn't analyze every file
- **Tokens consumed only for the script-authoring**, not the per-file work

This is the **highest-leverage cost optimization** in the corpus — moves work from per-row LLM to one-shot script generation.

### Counter-tactic from Tech With Tim — parallel sub-agents

- Advocates **parallel sub-agents** for time-sensitive data gathering: run 20-30 searches simultaneously
- Acknowledges this **uses more credits** but views the speed-up as the primary "unlock"
- Use when latency matters more than dollar cost

The two tactics aren't mutually exclusive — script for predictable bulk work, parallel sub-agents for exploratory/time-bound work.

## Tactic 3 — Session cycling for context rot (Jack Roberts)

- **Clear tasks or open new windows every 30-45 minutes** during focused sessions
- Reason: old, irrelevant conversation data **inflates token costs** on every subsequent message (because Claude has to re-read the full context)
- Maps to a quantitative discipline: monitor token usage per message; if context inflation is detectable, cycle the session

This is **context-rot prevention** at the operational layer — distinct from the file-based context-engineering ([[contextual-engineering]]) which addresses across-session consistency.

## The $200/month "headcount" framing (Jack Roberts, outlier)

While others focus on saving credits, Jack reframes:

- **$200/month Max plan** is not a software cost
- It's a **salary headcount** for an AI employee
- Question to ask: is this Cowork instance producing **$200+/month of work**?
- If yes, credit-conservation matters less than throughput

This is a **revenue-vs-credit** mental model — useful for operators using Cowork in actual business workflows vs. personal productivity tinkering.

## Synthesized decision tree

```
For each Cowork task:
  1. Can a script do this without LLM judgment? → Bart's tactic (script-in-skill)
  2. Is it bulk + parallelizable? → Tim's tactic (parallel sub-agents)
  3. Is the per-item work non-trivial reasoning? → use Sonnet first
  4. Did Sonnet fall short on quality? → escalate to Opus
  5. Has session been running 30+ min? → cycle the window (Jack's tactic)
  6. Is the task producing $$$? → Jack's headcount frame; credits matter less
```

## What the corpus doesn't cover

- **Quantitative cost benchmarks** — no speaker says "this scheduled task costs $X per day"
- **Cost vs. wall-clock trade-offs** for parallel sub-agents — only Tim acknowledges, no numbers
- **Token budgeting for organizations** running many Cowork users at once

See [[production-readiness-gaps]].

## Key Takeaways

- **Sonnet-by-default, Opus-on-escalation** is the strongest consensus signal in the corpus
- **Bart's script-in-skill pattern** is the highest-leverage credit-saver for bulk data work
- **Tim's parallel sub-agents** trade credits for latency — appropriate when wall-clock matters
- **Jack's session-cycling** at 30-45 min prevents context-rot inflation
- **Jack's "headcount" reframing** changes the question from "save credits" to "is the work worth its cost"
- The corpus has no quantitative cost data — the gap to fill for any production deployment

## Related

- [[overview]] — Cowork product positioning
- [[skills-to-plugins-pipeline]] — Bart's script tactic produces a script-embedded skill
- [[scheduling-and-the-app-open-constraint]] — scheduled tasks compound cost over time; budget matters
- [[production-readiness-gaps]] — what enterprise needs that the YouTube layer doesn't address
