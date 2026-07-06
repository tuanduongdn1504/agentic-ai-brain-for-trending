# Claude Tag — Overview

## What it is

**Claude Tag** is Anthropic's proactive, multi-user Claude agent living inside Slack channels — tag `@Claude` (or let it jump in on its own once added) and it reads thread context, does work in an Anthropic-hosted sandbox, posts results back, remembers per-channel standing instructions, and schedules its own follow-ups. Positioned by Anthropic as "the beginning of the evolution of Claude Code" into team surfaces; built by the Claude Code team (Boris Cherny / Cat Wu).

## Launch facts (all first-party unless noted)

| Fact | Value | Source |
|---|---|---|
| Launch | **2026-06-23, beta** | [anthropic.com/news/introducing-claude-tag](https://www.anthropic.com/news/introducing-claude-tag) |
| Availability | **Claude Enterprise + Claude Team (min 10 paid seats)** — no Free/Pro/Max path | support.claude.com 15594475 |
| Platform | **Slack only** at launch; video mentions Microsoft Teams as roadmap (video-only — not in written announcement) | claude.com/tag; launch video |
| Model | **Opus 4.8 exclusively** | announcement (via press dive) |
| Execution | Anthropic-hosted **ephemeral sandboxes**, per-conversation/thread, discarded on idle | [docs overview](https://claude.com/docs/claude-tag/overview) |
| Identity | **Agent-centric service accounts** ("its own account in each system it touches"), not user impersonation | [agent-identity blog](https://claude.com/blog/agent-identity-access-model) |
| Memory | Per-channel, persistent, admin-manageable; private-channel memory isolated | docs security-and-data; see [[memory-model]] |
| Billing | **Org-funded usage balance** for channel work; DMs bill the sender's personal Claude account | docs overview |
| Launch credits | **$25,000 (Enterprise) / $2,500 (Team)**, auto-applied, **expire 2026-09-01** | support.claude.com 15575654 |
| Legacy migration | Claude-in-Slack app auto-switches **2026-08-03**, no rollback | support.claude.com 11506255; see [[admin-rollout-and-migration]] |
| Connectors (launch) | **25+** per docs (GitHub, BigQuery, Snowflake, Linear, Jira, Asana, HubSpot, Salesforce, Datadog, PagerDuty, Sentry, Drive, Notion, Confluence…); Slack Real-Time Search API underneath | docs add-connections; Slack blog |
| ZDR constraint | Organizations on **Zero Data Retention cannot use Claude Tag** (memory/transcripts architecturally required) | docs setup-overview |
| Named customers | Hebbia, Descript, GitLab, Fractional AI, Gusto | claude.com/tag |

## The feature set (product page language)

- **Tag & react** — reads threads, full context, responds in real time.
- **Standing instructions / scheduled operations** — ongoing monitoring, weekly digests, urgent flagging.
- **Proactive (ambient) engagement** — initiates without being mentioned; admin can disable ambient mode per high-sensitivity channel.
- **Work products in-channel** — metrics, charts, summaries, draft PRs from bug reports, meeting prep, bug triage.

## Why it's a corpus-significant subject

1. **First Anthropic surface where the agent owns the trigger** — Chat/Cowork/Claude Code are all open-it-yourself; Tag inverts to agent-initiated (the video says this explicitly). Completes the reactive→proactive axis this corpus has tracked across [[external|Storm Bear: claude-cowork]] (scheduled but app-must-be-open) and self-built loops.
2. **First first-party multiplayer agent** — one shared session steered by a whole team; every prior corpus subject (harnesses, clones, bridges, Cowork) assumes a single human operator. New pattern-library-relevant axis: *multi-user steering of one agent session*.
3. **Vendor-validation of the operator's own stack** — proactive channel agent + per-channel memory + self-scheduling + verification artifacts posted back = precisely the architecture of the operator's Telegram remote-control + PR-babysitter + memory-file setup. See [[corpus-positioning]].
4. **Two headline claims that reward forensics** — [[metr-16-hour-claim]] and [[the-65-percent-claim]] are both real-but-compressed; this wiki quotes them only in corrected form.

## Key Takeaways

- Claude Tag = **proactivity + multiplayer + memory** on Slack, gated to org tiers, billed to the org, executed in vendor sandboxes on Opus 4.8.
- The operationally sharp dates: **2026-08-03** (forced legacy migration) and **2026-09-01** (launch credits expire → real spend visible).
- Written-announcement facts and video claims diverge in places (Teams roadmap, 65% wording) — this wiki treats docs as ground truth and the video as positioning; see [[launch-video-annotated]].

Cross-links: [[architecture-and-execution-model]] · [[memory-model]] · [[security-and-governance]] · [[admin-rollout-and-migration]] · [[competitive-landscape]] · [[corpus-positioning]]
