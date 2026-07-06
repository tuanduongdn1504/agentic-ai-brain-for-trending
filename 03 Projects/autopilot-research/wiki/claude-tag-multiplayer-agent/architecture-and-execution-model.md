# Architecture & Execution Model

## Execution: ephemeral vendor-hosted sandboxes

- Work runs in **Anthropic-hosted sandboxes** — "created when Claude starts work, discarded during idle periods"; per-conversation/per-thread isolation ([docs overview](https://claude.com/docs/claude-tag/overview), docs security-and-data). Nothing executes on user machines — the opposite pole from Claude Code's local-first model and from [[external|Storm Bear: claude-cowork]]'s app-must-be-open desktop constraint.
- Boris in the launch video: same remote sandbox family used by Claude mobile + desktop apps, "using the same agent SDK. So it's just as intelligent." **Verify-PARTIAL:** docs describe Tag's substrate as **Claude Managed Agents** (Anthropic's *hosted* agent service — the CMA line already tracked in [[external|Storm Bear: agent-memory-architecture]] for Memory Stores), which is a distinct product from the self-hosted **Agent SDK** library. Read Boris's line as "same agent runtime family," not as a literal Agent-SDK dependency; the docs' Managed-Agents framing is authoritative.
- Model: **Opus 4.8 exclusively** (announcement; the docs publish no model-selection page — model-spec endpoints 404'd in the docs dive). No tier routing, no model picker — a notable contrast to the per-tier routing patterns in [[external|Storm Bear: harness-engineering]] cost ladders.
- **Thread-locked permissions:** a thread locks in its connections/permissions at creation — admin changes don't reach in-progress threads (docs). Small but operationally important for credential rotation.
- **Connectors:** 25+ at launch per docs add-connections (GitHub, BigQuery, Snowflake, Redshift, Linear, Jira, Asana, HubSpot, Salesforce, Datadog, PagerDuty, Sentry, Google Drive, Notion, Confluence, …).
- **Ephemerality consequence:** continuity across days/weeks lives in **memory + scheduled follow-ups + the channel transcript itself**, not in a long-lived process. The long-horizon story is *checkpointed recurrence* — same architecture conclusion as [[metr-16-hour-claim]].

## Identity: agent-centric access model

- First-party framing ([agent-identity blog](https://claude.com/blog/agent-identity-access-model)): "Claude isn't acting on behalf of a single user. **It has its own account in each system it touches**" — workspace-managed **service accounts**, not user-credential impersonation.
- **Agent Proxy** credential model (docs security-and-data): credentials stored outside the sandbox, **never exposed to the model**, injected at request time; **default-deny egress** — outbound traffic only to allowlisted hosts.
- **Channel-scoped identities**: each channel's Claude has its own memory + tool grants; "engineering Claude cannot access HR memory/tools" — isolation is admin-defined and architectural.
- Config is gated to Slack **Primary Owner/Owner** roles (Admin role explicitly cannot), at `claude.ai/admin-settings/claude-tag`, org-wide — no per-user setup.

## Self-scheduling

- Claude sets its own reminders/follow-ups ("after days, or weeks, or months" — video; standing instructions + scheduled operations in docs). Combined with per-channel memory this is the mechanism behind month-long "sessions": recur → check data → post readout → occasionally PR a fix.

## Billing architecture

- **Channel work bills the org balance** (hard org cap + per-channel limits + 75%/95% alerts); **DMs bill the individual's own Claude account** — a clean architectural line between org agent and personal assistant, but also a governance seam (DM memory lives on the sender's personal account, outside org controls — see [[security-and-governance]]).
- Spend-limit enforcement is **decline-work, not degrade** (announcement dive) — a budget breach stops new work rather than silently truncating it. Fail-loud as a product decision.

## Composition picture

```
Slack channel (multi-user surface, Real-Time Search API)
   │  @mention / ambient trigger / schedule fire
   ▼
Claude Tag orchestration (proactivity judgment + memory recall)
   │  spins up
   ▼
Ephemeral sandbox (Opus 4.8 + Agent SDK) ── Agent Proxy ──► connectors (GitHub/Linear/Datadog…)
   │  posts artifacts back                        (service-account creds, allowlisted egress)
   ▼
Channel: results, charts, PR links, videos + updated channel memory + scheduled follow-up
```

## Key Takeaways

- Tag = **the Claude agent runtime re-homed to a shared surface via Managed Agents, with vendor-hosted execution and org-owned identity** — the three swaps (local→hosted, single-user→channel, user-creds→service-accounts) are the whole architecture story.
- The **Agent Proxy + default-deny egress + channel-scoped identity** triple is the most concrete first-party answer yet to the credential-isolation problems this corpus tracks (cf. Elicit's gateway isolation in [[external|Storm Bear: elicit-verifiable-agent-dsl]] — independent convergence on *credentials never enter the model's context*).
- Ephemeral sandboxes + memory-as-continuity mirrors the corpus' fresh-context⇒artifact-state convergence (TNT/Archon/Pocock) — now with a fourth, first-party instance.

Cross-links: [[overview]] · [[memory-model]] · [[security-and-governance]] · [[metr-16-hour-claim]]
