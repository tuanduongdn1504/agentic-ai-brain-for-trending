# MCP servers + Connectors landscape

What external tools Cowork power users actually connect to. Composition pattern: each Cowork task pulls data from external services via MCP/Connectors, processes in the sandbox, lands output back.

## Source

- Raw: [`raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md`](../../raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md), §Trends-3 + §Outliers-4

## Recurring connectors (corpus consensus)

The most-cited connectors across all 6 speakers:

| Connector | Used for | Speakers citing |
|---|---|---|
| **Google Calendar** | Morning briefs, schedule queries | Bart / Tim / Stefan |
| **Gmail** | Inbox summarization, draft generation | Bart / Stefan / Kenny |
| **Notion** | Output destinations + knowledge base | Bart / Tim / Stefan / Jack |

These three are the **table stakes** Cowork-vs-Connector integration set.

## Speaker-specific specialist tools

| Tool | Used by | Purpose |
|---|---|---|
| **Playwright MCP** | Kenny Liao | Browser control for tasks like posting to Substack (auth-walled sites that don't have direct MCP) |
| **Fireflies** | Jack Roberts | Meeting transcript ingestion |
| **Mercury** | Jack Roberts | Banking / financial reporting (real-money B2B operations) |
| **Linear** | Stefan Wirth | Project management |
| **Context OS MCP** (custom) | Stefan Wirth | Apply "lenses" — Stoic / Lean Startup / etc. — to evaluate output |

## The Vietnamese-anchor outlier — direct browser scraping

- **Duy Luân Dễ Thương** (anchor video) demonstrates a different pattern: Cowork **scrolls and scrapes** data directly from web browsers into Excel sheets
- No MCP layer — Cowork drives the UI directly
- This is closer to RPA (robotic process automation) than to the MCP composition model
- May reflect Vietnamese / SEA market where many target services don't yet have first-party MCP support → fall back to UI automation

## Composition model

```
              [User: scheduled task fires]
                       │
                       ▼
       ┌─────────────────────────────┐
       │  Cowork reads context/.md   │  ← from sandbox
       └──────────────┬──────────────┘
                      │
            ┌─────────┴──────────┐
            ▼                    ▼
   [MCP: Google Calendar]   [MCP: Notion]    ← data pulls
            │                    │
            └─────────┬──────────┘
                      ▼
       ┌─────────────────────────────┐
       │  Sub-agents process         │  ← see [[token-and-cost-management]]
       └──────────────┬──────────────┘
                      ▼
       ┌─────────────────────────────┐
       │  Write to output/ + Notion  │  ← sandbox + connector
       └─────────────────────────────┘
```

## Anthropic Connectors vs custom MCP

- **Anthropic-shipped Connectors** (Google, Notion, Slack, etc.) are the high-trust default
- **Custom MCP servers** (like Stefan's Context OS, Kenny's cron tool, Bart's invoice scripts) unlock the long tail
- Speakers don't sharply distinguish — both are "tools Claude can call"
- No speaker discusses the **security model differences** between Anthropic-vetted Connectors and operator-installed MCP servers

## Read-only Connectors vs write-capable MCP plugins (added 2026-05-30)

**Source:** 2026-05-30 follow-up drain on Anthropic Cowork docs (NotebookLM `b05d3444-6dbb-4955-a8fb-be9b021a0350`), §Trends-6. Darrel Wilson explicitly distinguishes the two integration tiers in a way the original 2026-05-29 drain did NOT capture:

| Tier | Capability | Use case |
|---|---|---|
| **Standard Connectors** | Often **READ-ONLY** access | Pull emails / docs / calendars into context for analysis |
| **MCP plugins** | **WRITE-capable** action authority | Send emails / create calendar events / move tasks |

This is the **single most-actionable security primitive** in either Cowork drain. The intuition:

- A read-only Connector minimizes the attack surface — even if compromised, the agent can't send malicious emails or move customer data outbound
- A write-capable MCP plugin elevates the risk — agent can take real-world actions; needs sandboxing ([[sandboxing-and-workspace-structure]] + [[../ai-operating-system/security-philosophies-and-sandboxing]] NemoClaw)

**Practical implication:** start every Cowork integration as a Connector (read-only). Only upgrade to MCP plugin (write-capable) when the workflow genuinely requires Claude to *act*, not just *read*. Many "automation" workflows are actually "read + summarize + present to operator" — Connector-only is sufficient.

**Compose with security posture:** if using write-capable MCP plugins, infrastructure-level sandboxing (NemoClaw or equivalent) becomes essential — not optional. See [[../ai-operating-system/security-philosophies-and-sandboxing]] §School 2.

**Open question:** can a single MCP server expose BOTH read-only and write-capable surfaces, with the operator controlling which the agent can use per-task? Corpus does not address. Worth a future drain.

## What the corpus doesn't cover

- **Rate limiting / 429 handling** when running parallel sub-agents against the same connector (see [[production-readiness-gaps]])
- **MCP server reliability** when the upstream service changes its UI / API
- **Auth-token refresh** on long-running scheduled tasks (most Anthropic Connectors hide this; custom MCPs hit this directly)

## Key Takeaways

- **Google + Notion are table stakes** — every Cowork power user has these wired
- The **specialist long tail** (Linear / Mercury / Fireflies / Playwright / custom Context-OS) reflects each operator's actual workflow — generalize cautiously
- **Custom MCP servers** appear in 3 of 6 speaker setups — the platform's open architecture is being used, not just the first-party connectors
- The **Vietnamese anchor's RPA approach** is a viable fallback when MCP support is missing for a target service — generalizable to any market with weak MCP coverage
- No speaker discusses **MCP server security model** as distinct from first-party Connectors — this is a gap worth flagging

## Related

- [[overview]] — Cowork product positioning
- [[skills-to-plugins-pipeline]] — skills wrap connector calls
- [[sandboxing-and-workspace-structure]] — connector outputs land in the sandbox
- [[production-readiness-gaps]] — what MCP/Connector reliability really takes at scale
