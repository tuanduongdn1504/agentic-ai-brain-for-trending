# Claude Tag (Multiplayer @Claude in Slack) — topic index

> **Claude Tag** — Anthropic's proactive, multi-user Claude agent in Slack channels (beta 2026-06-23, Enterprise + Team ≥10 seats, Opus 4.8, Anthropic-hosted sandboxes on Managed Agents, org billing + launch credits). Ingested from the operator-submitted BizMate VN dub → resolved to the first-party original **"The future of work with @Claude"** (Boris Cherny + Cat Wu, official Claude channel, 2026-07-02) + double-dive into claude.com/tag, docs, announcement, support articles, Slack Marketplace, METR, and press.
>
> **Compiled:** 2026-07-06 (main loop, both transcripts read in full) · verify Workflow `wf_36db963e-d86` (dive + refute-first, split across a session-limit outage and resumed; ~1.33M tokens / 440 tool calls cumulative; 11 machine verdicts + 7 main-loop takeover closures; 0 REFUTED)
> **Pilot deliverable:** [`output/(C) 2026-07-06-claude-tag-pilot-methods.md`](../../output/(C)%202026-07-06-claude-tag-pilot-methods.md)

## Articles

| File | What it covers |
|---|---|
| [[overview]] | What Claude Tag is; launch-fact table (dates, tiers, credits, model, connectors, ZDR constraint); why it's corpus-significant |
| [[launch-video-annotated]] | The Boris/Cat interview claim-by-claim against docs + verification; what the video omits |
| [[architecture-and-execution-model]] | Ephemeral sandboxes, **Managed Agents (not Agent SDK — corrected)**, Opus 4.8, Agent Proxy credential model, agent-centric service accounts, thread-locked permissions, billing architecture |
| [[memory-model]] | Workspace-shared public memory / asymmetric private isolation, 20/50/100 context windows, multi-author standing instructions, admin controls, ZDR incompatibility, memory-poisoning risk |
| [[security-and-governance]] | Agent Proxy + default-deny egress vs the four seams: ambient-mode injection surface, membership-as-ACL, audit fragmentation, the DM loophole; governance checklist |
| [[admin-rollout-and-migration]] | Setup hierarchy, spend caps, **2026-08-03 forced migration (no rollback)**, **2026-09-01 credit expiry**, rollout sequencing |
| [[metr-16-hour-claim]] | Grading "16 hours": 50%-time-horizon of Claude Mythos Preview (CI 8.5–55h, 5/228 tasks), not runtime; self-scheduling as the real long-horizon mechanism |
| [[the-65-percent-claim]] | Three non-equivalent first-party wordings; scope (product org); vs prior 80-100% claims; press distortion; PLAUSIBLE-UNVERIFIED discipline |
| [[competitive-landscape]] | vs Copilot Coworker, OpenAI Workspace Agents (write-access one day earlier), Devin, Glean, Gemini Spark; category emergence |
| [[slack-salesforce-context]] | Marketplace scopes, Real-Time Search API, $300M token commitment + ~1% equity, Agentforce tension, Anthropic-driven legacy sunset |
| [[reception-and-risks]] | Five risk clusters (injection, elevation, audit, cost, compliance), dogfood signal, unresolved buyer questions |
| [[corpus-positioning]] | ToS tension (resolved-not-violated), Cowork constraint superseded, CMA/ZDR memory links, operator's Telegram stack = 5/7 self-built Tag, 65% on the factory ladder, N-tracking candidates |
| [[caveats-and-corrections]] | Full verify ledger, 3 agent misfires overridden, known unknowns, blocked fetches |
| [[source-provenance]] | BizMate dub → original chain, name-garble note, ingest method |

## One-paragraph verdict

Claude Tag is the first first-party product where **the agent owns the trigger and the team shares the session** — proactivity + multiplayer + memory on a chat surface, shipped with an unusually explicit identity/credential architecture (Agent Proxy, service accounts, channel-scoped isolation) and unusually loud unknowns (ambient-mode injection, GA pricing, Teams timing). Its two headline numbers (16h METR, 65% PRs) are both real-but-compressed; this wiki quotes them only in corrected form. For the operator, it is vendor validation of the already-running Telegram/loop/memory stack — with the two missing capabilities (ambient proactivity, multi-user steering) doubling as the two biggest security seams.

## Cross-links

- [[../claude-cowork/_index]] — the reactive→proactive axis; app-must-be-open constraint superseded by Tag's hosted execution
- [[../agent-memory-architecture/_index]] — CMA Memory Stores + ZDR-ineligibility confirmed; new multi-author memory species
- [[../telegram-remote-control-stack/_index]] — the operator's self-built analog (5/7 patterns)
- [[../harness-engineering/_index]] — multi-user ToS line, factory-empirics ladder, cost discipline
- [[../claude-code-memory-systems/_index]] — taxonomy extension (server-side org-governed L2)
- [[../multi-agent-orchestration/_index]] — team-of-humans-steering-one-agent as the inverse shape
- [[../codex/_index]] + [[../competitive-landscape]] — vendor-role positioning race
