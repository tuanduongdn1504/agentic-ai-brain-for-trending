# Topics Queue

> Topics waiting for autopilot research routine to process.
> One topic per `## ` heading. Topics are processed top-to-bottom.
> When a topic is completed, move it to the "Completed" section at bottom.
>
> Format per topic:
> - **Query:** the search string handed to yt-search
> - **Anchors:** (optional) YouTube URLs to FORCE-INCLUDE in the bundle before yt-search picks the rest.
>   Format: nested bullet list under `**Anchors:**`. Up to `SOURCES_PER_TOPIC` (6) URLs.
>   Added 2026-05-14 after 4 of 6 user-named anchors got dropped by the search-rank rubric on 2026-05-13.
>   Example:
>     - **Anchors:**
>       - https://www.youtube.com/watch?v=ABC123
>       - https://www.youtube.com/watch?v=DEF456
> - **Notes:** optional hints (specific creators, deliverable type, follow-ups)
> - **Queued:** date queued
> - **Status:** pending / in-progress / completed
>
> Tools:
> - `python bin/autopilot-drain.py --list-only` — parse + show queue (no network, no log)
> - `python bin/autopilot-drain.py --dry-run`   — show selection plan (yt-search runs, no NotebookLM)
> - `python bin/autopilot-drain.py`             — full drain

---

## Autonomous Loops with HITL — anchor-injection re-run

- **Query:** `Karpathy autoresearch Ralph loop Claude Code autonomous overnight`
- **Anchors:**
  - https://www.youtube.com/watch?v=vjJwgXsMfjM
  - https://www.youtube.com/watch?v=9jxrmk_Xses
  - https://www.youtube.com/watch?v=o-pMCoVPN_k
  - https://www.youtube.com/watch?v=Yl_GGlAQ4Gc
  - https://www.youtube.com/watch?v=rnvNW-6XniU
  - https://www.youtube.com/watch?v=jfAIKrNMKvM
- **Notes:** 3rd attempt at this topic. **History:**
  - 2026-05-13 1st run: relaxed recency filter, pulled generic 2025 IBM/CNN/"What is Agentic AI" explainers (anchor-miss).
  - 2026-05-21 2nd run (tighter-query re-run, no anchors): 10-keyword AND-query `"Karpathy autoresearch Ralph loop human checkpoint goal driven Claude Code plan mode grill paperclip"` returned **0 yt-search results** → aborted. Tighter query swung too far the other way.
  - 2026-05-22 3rd attempt (THIS one): **anchor injection** per the 2026-05-14 operator-action-item #1. 6 anchors hand-picked 2026-05-22 to cap `SOURCES_PER_TOPIC=6`; yt-search fills 0 additional slots. Query simplified to balance discovery (would only matter if anchor count is reduced below 6 later).
- **Anchor selection rationale (2026-05-22):**
  - `vjJwgXsMfjM` — AI Andy, "Claude Code + Karpathy's Autoresearch = GOD MODE!" (58K views) — combines both halves of the topic
  - `9jxrmk_Xses` — Tonbi's AI Garage, "Karpathy's Autoresearch: We Achieved Near-Human Scores in 2 Hours!" (44K views) — direct Karpathy autoresearch coverage
  - `o-pMCoVPN_k` — Developers Digest, "How to Run Claude Code For Hours Autonomously" (88K views) — Ralph-loop-adjacent autonomous workflow
  - `Yl_GGlAQ4Gc` — WorldofAI, "Claude Code Ralph Loop: Run Claude Code For Hours Autonomously & Code ANYTHING!" (33K views) — explicit Ralph loop
  - `rnvNW-6XniU` — Nemanja Mirkovic, "Claude code shipped this while I slept (Ralph Loop explained)" — corpus-author follow-up (Nemanja's other work already ingested as sources 23-24). Note: dry-run 2026-05-22 surfaced this resolves to current title "Ralph loop shipped this with claude code while I slept" — same video ID, recent rename.
  - `jfAIKrNMKvM` — Siggi, "Karpathy Autoresearch & The Ralph Wiggum Loop: The Future of Autonomous AI Agents" — perfect title-match (combines BOTH halves of the topic explicitly). Replaced `8T3lMCfZHQM` (Nick Puru, dry-run-unreachable on 2026-05-22 — likely deleted/private/region-blocked).
- **Target:** supplement or supersede `wiki/autonomous-loops-human-in-the-loop/` (anchor-miss content from 2026-05-14).
- **Queued:** 2026-05-14 (re-queued with anchors 2026-05-22)
- **Status:** pending

---

## Completed


### Open Source Claude Design clones — anchor-corrected re-run ✅
- **Drained:** 2026-05-14 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-14-open-source-claude-design-clones-anchor-corrected.md`
- **NotebookLM:** `de7bec64-846d-486b-8661-4784d3cf0a1f`
### Codex — anchor-corrected re-run (3 anchors) ✅
- **Drained:** 2026-05-14 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-14-codex-anchor-corrected-re-run-3-anchors.md`
- **NotebookLM:** `3561e31a-5cfa-4fe6-9d5f-bec48b84d029`
### Agent Dashboard / Agent OS — anchor-corrected re-run ✅
- **Drained:** 2026-05-14 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-14-agent-dashboard-agent-os-anchor-corrected-re-run.md`
- **NotebookLM:** `1cd445b9-d834-4686-9fd0-12f4d67ce9d6`
### AI daily news — May 2026 weekly snapshot ✅
- **Drained:** 2026-05-13 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-13-ai-daily-news-may-2026-weekly-snapshot.md`
- **NotebookLM:** `9f08f424-31bc-4fe9-8e8b-3a91862171a1`
### Open Source Claude Design clones — alternative agent CLIs ✅
- **Drained:** 2026-05-13 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-13-open-source-claude-design-clones-alternative-agent.md`
- **NotebookLM:** `5155a280-86ce-49ce-8328-d4b75c0119ce`
### Codex — long-running agentic harness alternative to Claude Code ✅
- **Drained:** 2026-05-13 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-13-codex-long-running-agentic-harness-alternative-to.md`
- **NotebookLM:** `01707594-d36a-4a2f-b3f8-7fa9044528ba`
### Harness Engineering — personal-repo continuation (Vietnamese practitioner take + more) ✅
- **Drained:** 2026-05-13 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-13-harness-engineering-personal-repo-continuation-vie.md`
- **NotebookLM:** `58c51d8e-ab36-4331-993f-8a61dfd0a2c4`
### Auto-Loop Goals with human-in-the-loop ✅
- **Drained:** 2026-05-13 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-13-auto-loop-goals-with-human-in-the-loop.md`
- **NotebookLM:** `abe1647e-c9c3-4ad1-8e63-5e93fac50865`
### Agent Dashboard / Agent OS — Claude Code observability + dashboards ✅
- **Drained:** 2026-05-13 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-13-agent-dashboard-agent-os-claude-code-observability.md`
- **NotebookLM:** `54d7812d-2305-4eac-b250-43ba577cb1dc`
### Remote agent control — tunneling, SSH, ngrok, tailscale ✅
- **Drained:** 2026-05-07 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-07-remote-agent-control-tunneling-ssh-ngrok-tailscale.md`
- **NotebookLM:** `46ee01f8-81e3-47d6-b617-4c322359b6b9`
### MCP servers for messaging platforms — Telegram, WhatsApp, Discord ✅
- **Drained:** 2026-05-07 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-07-mcp-servers-for-messaging-platforms-telegram-whats.md`
- **NotebookLM:** `183e3635-ea8c-4c52-9c16-11aa32e19c78`
### Claude Code SDK — headless / programmatic automation ✅
- **Drained:** 2026-05-07 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-07-claude-code-sdk-headless-programmatic-automation.md`
- **NotebookLM:** `dafc8c4f-840b-41a1-b125-bfe973c919f0`
### Telegram bot — remote control Claude Code/Desktop from phone ✅
- **Drained:** 2026-05-07 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-07-telegram-bot-remote-control-claude-codedesktop-fro.md`
- **NotebookLM:** `5f514e9c-d8e4-42be-af1e-c456dfa1e4c7`
### Workflow for AI Coding — champions roundup ✅
- **Drained:** 2026-05-07 by autopilot loop `(C) 2026-05-07-15-autopilot-loop.md`
- **Wiki output:** [[../wiki/workflow-ai-coding/_index]] — 5 articles + index
- **NotebookLM:** `ec93ea09-b589-4103-95a9-3fb2c13d5a2e`

### How to 10x Claude Code — tips & tricks roundtable ✅
- **Drained:** 2026-05-07 by autopilot loop `(C) 2026-05-07-15-autopilot-loop.md`
- **Wiki output:** [[../wiki/10x-claude-code/_index]] — 5 articles + index
- **NotebookLM:** `d1d18b0b-ab85-4773-a999-98f36fb39cf5`
