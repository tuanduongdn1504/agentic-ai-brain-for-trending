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

## Completed


### AI text watermarking — Anthropic's invisible mark on Claude output (EU AI Act Article 50) ✅
- **Drained:** 2026-08-21 by `/loop` (operator anchor `5R9Nw8eKDCA` BizMate AI Official + yt-search ×5 on query `Anthropic Claude watermark AI generated text`, selected via `bin/autopilot-drain.py --dry-run` after probing 3 candidate queries; anchor validation **PASS 1/1, overlap 100%**; **fetch guard PASS 6/6** — the ⭐⭐ deepen candidate from topic #78, implemented)
- **Raw analysis:** `raw/2026-08-21-ai-text-watermarking-claude-eu-ai-act.md`
- **Wiki output:** [[../wiki/ai-text-watermarking/_index]] — 13 files; 70 wikilinks validated 0 broken; **101 claims: 76 CONFIRMED / 8 UNVERIFIED / 6 CBI / 3 CORRECTED / 2 MISLEADING / 2 FALSE / 2 UNFALSIFIABLE / 1 TIME-BOUND / 1 CONTRADICTED-IN-BUNDLE / 0 FABRICATED** (largest scorecard + highest confirmation rate in corpus; tallied programmatically)
- **NotebookLM:** none (yt-dlp captions read in full — a claims scorecard cannot grade a paraphrase)
- **Result:** the anchor is **right about the fact, wrong about the frame** — Anthropic really does watermark Claude's text output and it really does persist through proofread/translate/summarize, but "all their models" is **CORRECTED** (models launched on/after 2026-08-02; earlier ones by 2026-12-02), "detects whether Claude is the author" is **MISLEADING** (Anthropic: *"may have been **processed** by Claude"*), and the video **never names the EU AI Act** that caused it. **The mark comes from Article 50(2); the ratified hireui candidate-LLM ADR comes from the same Act** — 50(2) binds providers, 50(4) binds deployers, and the ADR's "eval-gated" clause is currently unimplementable (no public detector, no published false-positive rate). **The anchor's other story is a confirmed real-world BOLA**: a Claude-powered OpenClaw agent in Melbourne found *"zero authorization checks on cancelling other people's reservations"* and deleted a stranger's booking — the exact class `api-security-7-techniques` flags as this operator's #1 risk. ⚠️ **6 verification-process failures recorded** incl. 2 lenses CONFIRMING the anchor's one material error and a critic that falsely reported "no disagreements detected". ⚠️ **The source bundle is NOT reproducible** — 1 of 3 selection runs drifted.
- **Deepen candidates:** ⭐⭐ **non-English watermark/detector performance** (the topic's largest real gap — every number is English, the anchor is Vietnamese, and hireui screens non-native-English candidates) · ⭐⭐ **make `--dry-run` emit video IDs and let a drain accept an ID list**, so a selection can be replayed rather than re-rolled (the non-reproducibility finding) · ⭐⭐ **re-read `support.claude.com` verbatim** rather than through `WebFetch`'s summarizing layer, and pick up the detection API when it ships (release date, access tier, error rates) · ⭐ **does the mark degrade code?** the one unresolved contradiction (A09 vs C16), and the question that matters most for Claude Code · ⭐ the **2027-02-02 Code-of-Practice interoperability deadline**, absent from all 6 sources · ⭐ **C2PA as a topic in its own right** (the corpus has none) · ⭐ the **12 unverified items** in the anchor's roundup, listed in `the-anchor-audit` so a later ingest need not re-derive them · ⭐ **fix `eng_ratio * 3` unboundedness** — surfaced again here at score 313.39 vs 49.58 for a video with 3.5× the views

### Homebrew — the macOS package-manager layer (VN anchor + 6.0 release) ✅
- **Drained:** 2026-08-21 by `/loop` (operator anchor `A_nvIGTNfuw` Kunkka + yt-search ×5 on query `Homebrew macOS package manager terminal setup`, selected via `bin/autopilot-drain.py --dry-run`; anchor validation **PASS 1/1, overlap 100%**)
- **Raw analysis:** `raw/2026-08-21-homebrew-macos-package-manager-layer.md`
- **Wiki output:** [[../wiki/homebrew-macos-package-manager/_index]] — 11 files; 109 wikilinks validated 0 broken; **46 claims: 29 CONFIRMED / 5 CORRECTED / 4 CBI / 3 UNVERIFIED / 2 TIME-BOUND / 1 MISLEADING / 1 UNFALSIFIABLE / 1 CONTRADICTED-IN-BUNDLE / 0 FABRICATED**
- **NotebookLM:** none (yt-dlp captions read in full — a claims scorecard cannot grade a paraphrase)
- **Result:** the anchor is a design-history essay, not a tutorial, and its three central critiques of Homebrew are confirmed verbatim by `docs.brew.sh`. **The headline finding is original to the ingest**: this machine (Apple M4 Pro) runs its primary Homebrew as **x86_64 under Rosetta 2** at `/usr/local` while a native arm64 install sits unused at `/opt/homebrew` — which diagnoses the long-standing "broken `python3` shim" note in the project `CLAUDE.md`, and lands on Homebrew's **Intel → Tier 3 September 2026** deprecation path.
- **Deepen candidates:** ⭐⭐ run the prefix migration and write it up (bounded, measurable, Sept-2026 deadline) · ⭐⭐ assert one transcript file per selected video before compiling (silent-fetch-failure guard) · ⭐ a **docs-first** ingest of `docs.brew.sh` Tap-Trust + Support-Tiers (the docs outperformed every video here) · ⭐ **Nix on macOS** — two sources place the boundary there and the corpus has no Nix topic · Rosetta 2's own deprecation timeline (deliberately unverified) · `brew bundle` vs real fleet reproducibility · Kunkka's back catalogue
### Local LLM coding on Apple Silicon — the 64GB Mac mini M4 hardware ladder ✅
- **Drained:** 2026-08-20 by `/loop` (operator anchor `GBf_mKxGqtk` Quân IT + yt-search ×5: WEBdoze / ForrestKnight / Samuel Gregory / Zen van Riel / Tech With Tim; anchor validation **PASS 1/1** — *after* fixing a delimiter bug in `bin/autopilot-drain.py` that had silently dropped it as "unreachable")
- **+1 main-loop addition:** Apple WWDC26 session 232 `wykPErJ8M-8` (first-party; the rubric ranks engagement, not authority)
- **Raw analysis:** `raw/2026-08-20-local-llm-coding-apple-silicon-hardware-ladder.md`
- **Wiki output:** [[../wiki/local-llm-coding-hardware-ladder/_index]] — 11 files; 123 wikilinks validated 0 broken; **21 claims: 12 CONFIRMED / 5 CBI / 1 FALSE / 3 UNRESOLVED / 0 FABRICATED**
- **NotebookLM:** none (yt-dlp captions read in full)
- **Result:** TESTS AND CORRECTS `local-ai-coding-agents` — its "≥24 GB practical minimum" is **refuted** for agentic coding. Memory capacity is the wrong axis; prefill/bandwidth/repo-size are binding.
- **Deepen candidates:** ⭐ an **M5-generation** agentic test against a real repo (the biggest open question — Apple claims 4× matmul, nobody has measured it on a large codebase) · Apple WWDC26 session **233** (distributed inference) · **OMLX** hands-on (SSD-persistent prefix cache) · **Alex Ziskind** bandwidth/TCO bundle (appeared in all 3 test queries, never won a slot) · Asad Tinkers "Ultimate Local Mac Agentic AI Coding Workflow" (951 views — **below `MIN_VIEWS=1000`, rubric structurally cannot pick it, needs an anchor**)

### DeepSeek Harness — YouTube commentary layer vs source-verified corpus ✅
- **Drained:** 2026-08-20 by `/loop` (operator anchor `f51ICIoHcjY` Chase AI + yt-search ×5: The Cef Experience / Turing Post TV / Code Bug VN / Better Stack / Firecrawl; anchor validation **PASS 1/1**)
- **Raw analysis:** `raw/2026-08-20-deepseek-harness-youtube-commentary-vs-source.md`
- **Wiki output:** [[../wiki/deepseek-harness/_index]] — 15 files; 32 wikilinks validated 0 broken; **47 claims: 24 CONFIRMED / 10 CBI / 4 PLAUSIBLE-NOT-PRIMARY / 4 MISLEADING / 1 FALSE / 3 UNRESOLVED / 1 UNVERIFIABLE / 0 FABRICATED**
- **NotebookLM:** none (yt-dlp captions read in full — a claims scorecard cannot grade a paraphrase)
- **Deepen candidates:** Cloud Codes architecture deep-dive (49,192 views) + NeuralNine (196,090, largest reach) + CloudYeti "Is the Hype Real? LIVE Testing" (891 views, below `MIN_VIEWS` so the rubric cannot pick it — **needs an anchor**)

### Engineer of the future — Addy Osmani AIEWF-2026 keynote + role-under-AI-agents bundle ✅
- **Drained:** 2026-07-22 by `/loop` (operator anchor `n97BCfyFIvw` + yt-search ×5: Karpathy / Ng / Cursor-Truell / Gergely Orosz / Harrison Chase)
- **Raw analysis:** `raw/2026-07-22-engineer-of-the-future-osmani-aie-keynote-bundle.md`
- **Wiki output:** [[../wiki/engineer-of-the-future/_index]] — 15 files (0 FALSE / 0 FABRICATED; workflow `wf_dabc1f67-f9f`)
- **NotebookLM:** none (yt-dlp captions read in full)

### API types explained (REST, SOAP, GraphQL, gRPC, WebSocket, webhook) ✅
- **Drained:** 2026-07-21 by overnight orchestrator
- **Raw analysis:** `raw/2026-07-21-api-types-explained-rest-soap-graphql-grpc-websock.md`
- **NotebookLM:** `ed17cc3d-952c-4fe0-9572-27a418d0f390`
### Harness Engineering — getting started / beginner introduction (Vietnamese anchor) ✅
- **Drained:** 2026-05-30 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-30-harness-engineering-getting-started-beginner-intro.md`
- **NotebookLM:** `4c7d51e4-b450-4504-933b-3bb4be28b393`
### Anthropic Cowork first-party documentation + setup-cowork skill ✅
- **Drained:** 2026-05-30 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-30-anthropic-cowork-first-party-documentation-setup-c.md`
- **NotebookLM:** `b05d3444-6dbb-4955-a8fb-be9b021a0350`
### AI Operating System — 5-skills framework ✅
- **Drained:** 2026-05-29 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-29-ai-operating-system-5-skills-framework.md`
- **NotebookLM:** `1f5811fb-60c1-4857-a039-c784508b2ec4`
### Claude Cowork — Anthropic scheduled-agent feature ✅
- **Drained:** 2026-05-29 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md`
- **NotebookLM:** `f851b538-c0cb-405f-9a8b-c46837464930`
### Autonomous Loops with HITL — anchor-injection re-run ✅
- **Drained:** 2026-05-23 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-23-autonomous-loops-with-hitl-anchor-injection-re-run.md`
- **NotebookLM:** `94db9216-eb26-489d-8f06-fd65fbea3fd4`
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

- TODO: hoidanit fullstack-vibe-coding series — re-drain playlist PLPTXD_6Mbmh4 when episode >=5 lands; **cadence now deterministic (ep-3 deepening 2026-07-04): live Mondays 19:30 ICT, VOD Wednesdays → ep-5 (React fundamentals) expected ~Wed 2026-07-08**; PRIORITY when the AI-consult-agent episode ships (wiki/hoidanit-fullstack-vibe-coding gap)
