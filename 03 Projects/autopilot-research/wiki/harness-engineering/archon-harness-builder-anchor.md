# Archon — the harness-builder platform layer (anchor)

> **Layer:** NEW third layer for this topic — **platform layer** (a tool that *builds* harnesses), above org-scale harness instances (Lopopolo/Symphony, Stripe Minions) and individual-scale harnesses (personal-repo siblings).
> **Compiled:** 2026-07-04 · **Verification:** Workflow `wf_8a0f2da5-1d0` (6 dives + 10 refute-first verifiers, ~815K tokens, 324 tool calls) + main-loop overrides. Ledger at bottom.

## Source

- **Video:** "Full Archon Guide - Build AI Coding Harnesses That Actually Ship (LIVE)" — https://www.youtube.com/watch?v=srx9iwnjK2M — Cole Medin, streamed **2026-04-11**, 2:45:30, 85.5K views at fetch. Full 163K-char transcript read in main loop (`raw/srx9iwnjK2M/`).
- **Intro video (3 days earlier):** "The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them" (qMnClynCAmM, 2026-04-08 CDT / 04-09 UTC, 30:47, 50.6K views).
- **Original resource:** https://github.com/coleam00/Archon — **22,699★** / 3,409 forks at fetch (host said 16.2K on stream day → +6.5K in 84 days ≈ 77★/day), TypeScript, MIT, docs at https://archon.diy. README + Archon skill + CHANGELOG read in full in main loop.

## The claim and what it means

- Repo tagline: **"The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable."** README analogies: *"Like what Dockerfiles did for infrastructure and GitHub Actions did for CI/CD"* + *"Think n8n, but for software development."*
- **Harness vs harness builder** — the load-bearing distinction of the whole ingest: B-MAD, GitHub Spec Kit, GSD, Claude Flow, Ralph loop = single opinionated harnesses; Stripe Minions, Shopify Roast, AWS AgentCore = corporate harnesses (mostly closed); **Archon = meta-level platform for encoding YOUR process as a versioned YAML workflow**. "You don't change how you work — you package what you already have (skills, commands, rules) into a workflow."
- **First-claim assessment (dive verdict):** defensible on narrow grounds — no other OSS project self-identifies as a *builder-of-harnesses platform* (OpenHarness IS a harness; Conductor orchestrates but doesn't build; GSD/B-MAD/Spec Kit are frameworks/methods). But "harness builder" is Archon's own category coinage — first-in-a-category-you-named. Sister rhetoric to Storm Bear [[external|Storm Bear: Pattern #19]] first-mover-authority observations.

## Evolution thesis (Cole's framing, video §1)

**Prompt engineering (2022, GPT-3.5 Turbo era) → context engineering (2025) → harness engineering (2026)** — cumulative, not substitutive ("prompt engineering is a part of context engineering"). Context engineering attribution verified with a correction: **Tobi Lütke initiated (X, 2025-06-19), Karpathy amplified 6 days later (2025-06-25)** — not joint coinage. Cole's definition of harness: *"the tooling and process you build on top of the coding agent to make it more reliable… taking your whole process for building software and enforcing it in the layer on top."* Matches Lopopolo's [[core-claims]] and Tejas Kumar's [[tejas-kumar-anchor]] definitional decomposition; the pitch "shepherding between sessions is what a harness removes" is the same session-orchestration gap the [[personal-repo-hermes-orchestrator]] and [[personal-repo-router-multimodel]] siblings each solve one slice of.

## The corporate-harness evidence base (all refute-verified)

- **Stripe Minions — CONFIRMED:** official Stripe blog 2026-02-09 "Minions: Stripe's one-shot, end-to-end coding agents"; Stripe's own X post: **"Over 1,300 Stripe pull requests merged each week are completely minion-produced, human-reviewed, but contain no human-written code."** Built on a heavily modified fork of Block's open-source **Goose**; Minions itself closed-source. Video's "viral last month" ≈ right (coverage peaked March 2026). Video's "more powerful version of the Ralph Loop" = **Cole's characterization, not Stripe's** (UNVERIFIED as sourced claim).
- **The "6.7% → almost 70%" study — CORRECTED:** real but materially different: **Can Bölük** (blog.can.ac, 2026-02-12, "The Harness Problem" + `oh-my-pi/react-edit-benchmark`): **Grok Code Fast 1** went **6.7% → 68.3% task-success** (not PR-acceptance) on a 180-task React benchmark, by changing the **edit format** to hash-anchored "Hashline" — a harness-level change, but a *narrow* one (edit format), not a full workflow harness. Cross-link: **pi lineage** — oh-my-pi is the pi ecosystem ([[external|elicit-verifiable-agent-dsl/pi-harness-and-curator-models]]).
- **Claude Code source leak — CONFIRMED:** 2026-03-31, 59.8MB `cli.js.map` shipped in `@anthropic-ai/claude-code` v2.1.88 (missing `.npmignore` entry, packaging error not breach), ~512K lines unobfuscated TS, found by Chaofan Shou. Video's "60% model-wrapping / 40% harness features" = **post-leak commentary math, PARTIAL** — not a quantification from the source itself; treat the ratio as folklore. **Agent teams CONFIRMED** as experimental Claude Code feature (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`).
- **StrongDM "dark factory" — CONFIRMED:** 3-person team (Justin McCarthy, Jay Taylor, Navan Chauhan), Feb 2026: **32,200 lines of production security software (`strongdm/cxdb`) with zero human-written code AND zero human review**, via NLSpec spec-driven development + scenario validation + digital twins of Okta/Jira/Slack/Google-Workspace. Willison covered it 2026-02-07.
- **Shopify Roast — CONFIRMED:** `Shopify/roast` (MIT, Ruby, ~1.2K★, blog 2025-06-18) "Structured AI workflows made easy" — an open-source corporate harness, contradicting the video's "all corporate harnesses are closed-source" sweep (minor).
- **AWS — CONFIRMED via AgentCore:** Amazon Bedrock AgentCore ships a managed **harness** (docs literally use the term) + awslabs sample repos.
- **Anthropic "quite a few harnesses" — PARTIAL:** ~2-3 public artifacts (defending-code-reference-harness, cwc-long-running-agents, engineering-blog reference harnesses) — "a few," not "quite a few."

## Dark factory (terminology + Cole's experiment)

- Codebase-sense coinage: **Dan Shapiro, "The Five Levels: from Spicy Autocomplete to the Dark Factory" (2026-01-23)**, amplified by Simon Willison (2026-01-28); Lopopolo used it in Feb-2026 blog/talk *after* Shapiro; StrongDM = the flagship instance. See updated [[terminology]] entry — three independent 2026 usages now tracked (Shapiro→Lopopolo→Medin).
- Cole's planned **public dark-factory experiment**: a repo where issues are the only human input; Archon workflows do triage → implement → review → release, no human approval, straight to main. Use case = RAG chat over his YouTube/Dynamous content. **Repo exists: `coleam00/dark-factory-experiment`** (created 2026-04-02 — pre-provisioned before the stream; pushed through 2026-06-10; "AI chat app for conversational RAG over YouTube video transcripts"). Dedicated dark-factory stream/series NOT yet found as of 2026-07-04 — the stream itself deferred it ("would take another hour and a half").
- The repo's own maintainer workflows are the *incremental* version of this — see [[archon-default-workflows-and-dogfood]].

## Pivot history (dive-verified)

- Repo created **2025-02-07**. **Old Archon** = "command center for AI coding assistants": task management + RAG knowledge base + MCP server for Claude Code/Cursor/Windsurf ("Introducing Archon - The Revolutionary Operating System for AI Coding", 8pRc_s2VQIo, 2025-08-14). Preserved on branch `archive/v1-task-management-rag`.
- Origin of the rewrite: private Dynamous-community project **"remote coding agent"** (talk to Claude Code/Codex via Slack/Telegram/GitHub) built for the agentic-coding course → generalized into the harness builder.
- **Pivot inflection: v0.2.6 (2026-02-21) introduced the DAG workflow engine; v0.3.0 (2026-04-08) completed the harness-builder repositioning — 8 weeks, with the public reveal (intro video 04-08/09 + this live stream 04-11) coordinated to the release.** Old-version lesson Cole states on stream: they over-built configuration features nobody used — feature-bloat caution now governs (e.g., web-terminal request deferred).
- Post-video velocity (CHANGELOG read in full): v0.4.0 (2026-05-28) GitHub App auth, Slack overhaul, **OpenCode + GitHub Copilot community providers**, Codex MCP; v0.5.0 (2026-06-26) per-user credential vault (AES-256-GCM, PKCE for ChatGPT/Codex), run-centric Console UI, **model tiers small/medium/large + @custom aliases**, typed artifacts, structured-output validate+repair+reask, **Pi SDK migrated to `@earendil-works`** — pi is now a first-class provider ([[external|elicit-verifiable-agent-dsl/pi-harness-and-curator-models]] — same Earendil/Zechner lineage; Cole's Pi+Archon video XSmI7OYd7iM, 2026-04-20, "No Claude Code Bloat").

## Who's who (verified)

- **Cole Medin** (@ColeMedin, **214K subs** by yt-dlp ground truth 2026-07-04 — a verify agent's "204K, inflated" verdict OVERRIDDEN by primary data; 200K milestone ~2026-04-10 self-reported on stream). Channel tagline since 2024: "Join me as I push the limits of what is possible with AI." Runs the paid **Dynamous** community (AI Agent Mastery + Agentic Coding courses + second-brain bootcamp). Also the walkthrough presenter of our [[anthropic-large-codebases-anchor]] (2026-05-21) — same person now anchors two layers of this topic.
- **Rasmus = Wirasm (Rasmus Widing) — the #1 contributor at 971 contributions vs Cole's 417.** The "solo creator" impression the video gives is wrong in commit terms; Cole says on stream "I'm not the one that's built everything."
- **Thomas = leex279 (GitHub display name literally "DIY Smart Code", 45 contributions)** — verify agent missed this; main-loop `gh api users/leex279` override.

## Key Takeaways

- The **harness/harness-builder distinction** is the sharpest new vocabulary this topic has gained since Lopopolo's org/individual split — Archon closes the [[research-roadmap]] Tier-5 #9 ask ("Symphony-class orchestrators, open-source equivalents") from the builder side.
- The corporate convergence story is **real and now fully sourced**: Stripe (1,300 AI PRs/wk, human-reviewed), StrongDM (32K lines, zero review), Shopify Roast (OSS), AWS AgentCore, Anthropic reference harnesses — plus the Claude Code leak showing harness code shipping inside the product.
- The famous 6.7→70 number is **narrower than its retellings**: one model, one benchmark, one edit-format change (Hashline). Use it as "harness details dominate model choice," never as "PR acceptance."
- Archon's actual differentiators vs siblings: **worktree-isolated parallel runs, deterministic (no-AI) nodes, per-node model routing, human approval gates that pause/resume across CLI/web/Slack, and skill-mediated invocation** ("use archon to fix issue #42" is the whole interface).
- Anti-vibe positioning is explicit and matches this topic's consensus: Ralph-loop-style full autonomy = compounding-error risk; "take as many decisions away from the coding agent as you possibly can" (deterministic steps), keep human gates. Cole: "better results using Archon with Sonnet than Opus by itself in Claude Code" (self-reported, uncorroborated — sibling claim to Lopopolo's uncorroborated throughput claim #4).
- Star velocity (16.2K→22.7K in 12 weeks post-pivot) + B-MAD v6 shipping + GSD's original repo getting archived into a community org in the same window = the harness-layer market is consolidating fast.

## Verification ledger (Rule 12)

| Claim (video) | Verdict |
|---|---|
| Stripe Minions, 1,300 AI-only PRs/week | CONFIRMED (Stripe blog + X) |
| Minions = "more powerful Ralph loop" | UNVERIFIED (Cole's gloss) |
| 6.7%→~70% PR acceptance, harness-only | CORRECTED → 6.7→68.3% task-success, Grok Code Fast 1, Hashline edit format (Can Bölük) |
| Claude Code source leak "last month" | CONFIRMED (2026-03-31, v2.1.88 sourcemap) |
| Leak shows 60/40 model/harness split | PARTIAL (commentary math, not source quantification) |
| StrongDM dark factory | CONFIRMED (32,200 lines, cxdb, Feb 2026) |
| Dark-factory term origin | CORRECTED → lights-out mfg (1980s Fanuc; Autofac 1955 fiction) → codebase sense Dan Shapiro 2026-01-23 |
| Shopify Roast harness | CONFIRMED (and it's OSS — video implied closed) |
| Tobi/Karpathy context-engineering | CORRECTED → Lütke first 2025-06-19, Karpathy amplified 06-25 |
| Boris Cherny "made it very clear" sub+SDK OK | PARTIAL/CONTESTED → see [[harness-economics-and-tos-timeline]] |
| 16.2K stars at stream | CONFIRMED (curve-consistent with 22.7K now) |
| "Thomas & Rasmus helped most" | CONFIRMED + upgraded: Rasmus is the top contributor outright |
| GSD README quotes ("enterprise theater") | CONFIRMED (repo since archived → open-gsd org, ~June 2026) |
| Gemma 4 runs Archon workflows | PARTIAL (Gemma 4 real, 2026-04-02; community-Archon claim unverified) |
| "GPT-5.4 Codex high reasoning" | REFUTED as a name (GPT-5.4 and GPT-5.3-Codex are distinct; GPT-5.5 landed 2026-04-23) |
| Gemini CLI has no SDK | CONFIRMED — and Gemini CLI is being discontinued for most users 2026-06-18 in favor of Antigravity CLI ([[external|google-antigravity-skills/_index]]) |
| GitHub Copilot SDK "just released" | CONFIRMED (public preview 2026-04-02, GA 2026-06-02) |

**Agent-misfire log:** (1) verify:cole-channel called 214K "inflated" against a stale tracker — overridden by yt-dlp `channel_follower_count=214000`; (2) verify:cole-channel failed to find the 2026-04-08 intro video — main-loop channel listing found qMnClynCAmM; (3) verify:cole-channel found "no DIYSmartCode identity" — `gh api users/leex279` name field IS "DIY Smart Code"; (4) dive:default-workflows counted 20 defaults vs README's 19 — main-loop recount agrees with 20 (README table omits `archon-test-loop-dag`).
