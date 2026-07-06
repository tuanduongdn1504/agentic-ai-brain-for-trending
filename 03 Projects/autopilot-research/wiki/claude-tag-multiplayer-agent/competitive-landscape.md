# Competitive Landscape — AI Teammates in Team Chat (July 2026)

## The category Claude Tag claims

Four differentiators per Anthropic's positioning: **multiplayer** (one shared agent per channel, all members steer), **persistent per-channel memory**, **proactive ambient mode** (monitors, flags, follows up unprompted), **asynchronous delegation** (tag it, move on). [Latent Space](https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive) calls it Anthropic's "first product that is natively multiplayer and proactive."

## The field

| Product | Surface | Proactive? | Multi-user memory? | Long-running autonomous tasks? | Notes |
|---|---|---|---|---|---|
| **Claude Tag** (Anthropic) | Slack (Teams "excited to bring" — video-only) | Yes (ambient mode, admin-toggleable) | Yes (per-channel, isolated) | Yes (self-scheduling, ephemeral sandboxes, Opus 4.8) | Enterprise/Team ≥10 seats only |
| **Microsoft Copilot Coworker / Cloud Agent** | Teams + M365 | Partially (Graph-context surfacing) | Org-graph context, not channel-personality memory | Via Copilot agents | Deepest compliance/governance story (native 365, [GitHub cloud-agent Teams integration](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/integrate-cloud-agent-with-teams)) |
| **OpenAI Workspace Agents** | ChatGPT Enterprise + Slack | Write-access in Slack since **2026-06-22 — one day before Tag's launch** | Workspace-level | Yes | The timing collision reads as deliberate enterprise land-grab season ([TechTimes](https://www.techtimes.com/articles/318982/20260624/chatgpt-enterprise-gains-slack-write-access-ai-agent-can-now-join-channels-upload-files.htm)) |
| **Devin** (Cognition) | Slack/Teams tags → coding sessions | On-mention | Org knowledge base | Yes (coding-scoped) | 20+ integrations; valuation $10.2B→$25B in 7 months; stays coding-domain |
| **Glean Assistant** | Cross-app search + actions | Proactive templates | Org index (search-first) | 100+ app actions, not sandboxed compute | Search/knowledge company approaching from retrieval side |
| **Google Gemini Spark** | Gemini Enterprise / Workspace Chat | Yes (24/7 background, daily briefings) | Workspace context | Background agent | Closest architectural cousin on the proactive axis ([Google Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform)) |

## Analyst framing

- [HyperFRAME Research](https://hyperframeresearch.com/2026/06/30/ai-agents-move-out-of-the-dm-anthropic-launches-claude-tag-in-slack/): a "land grab to dominate the contextual control plane of enterprise collaboration" — while conceding Anthropic solved "hard systems work" (tools, compute, memory, security) others haven't. The control-plane framing directly parallels [[external|Storm Bear: google-zero-open-web]] platform-economics: whoever owns the surface where work is *described* owns the demand routing.
- [TechCrunch](https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/): the memory accumulation is the moat *and* the governance story ("learning your company one Slack message at a time").
- Ramp May 2026 AI Index (via [AI News](https://www.artificialintelligence-news.com/news/anthropic-slack-workplace-ai-agents/)): Anthropic 34.4% vs OpenAI 32.3% enterprise adoption — the context in which both vendors shipped Slack write-access within 24h of each other. (Third-party index, methodology not checked here.)

## Segmentation reading

- **By task domain:** Devin/Copilot coding-scoped vs Tag/Spark general knowledge-work.
- **By surface ownership:** Microsoft and Google own their collaboration surfaces; Anthropic and OpenAI are *tenants* on Slack — which makes the Salesforce relationship load-bearing (see [[slack-salesforce-context]]).
- **By market tier:** Tag is deliberately upmarket (no Free/Pro path at all) — opposite of the bottom-up Claude Code adoption motion.

## Key Takeaways

- Proactive-agent-in-chat went from zero to **four vendors in ~6 weeks** (Tag, OpenAI write-access, Spark, Copilot Coworker iterations) — this is a category now, not a feature.
- Claude Tag's defensible deltas are **channel-scoped memory-with-identity** and **sandboxed execution with org billing** — not chat presence per se.
- Being a tenant on a rival-owned surface (Salesforce/Slack) is the structural risk every analyst flags.

Cross-links: [[overview]] · [[slack-salesforce-context]] · [[external|Storm Bear: codex]] (vendor-role positioning) · [[external|Storm Bear: google-zero-open-web]]
