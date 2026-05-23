# Raw Inventory — Single Source of Truth for Coverage

> **Purpose:** every ingestion event into `raw/` MUST have a row here, regardless of which path (1-8) brought it in. This file is the canonical answer to "what's been ingested" and "what's compiled vs uncompiled."
>
> **Why this exists:** before 2026-05-08, `topics-queue.md` was used as a coverage proxy — but the queue only tracks paths 1+2 (single-topic burst, scheduled cron). Paths 3-8 (single-URL, bundle, yt-search, custom scraper, query, promotion) bypass the queue and land directly in `raw/`. The Lark Claude course (261 markdown files via custom scraper) sat invisible to coverage audits for 1 day before the gap was noticed. This inventory bịt the gap.
>
> **Maintenance:**
> - Path 1+2 (autopilot-research-routine): Phase 0 auto-appends a row before ingestion + Phase 7 updates `Status` to `compiled`.
> - Path 3 (single notebooklm source add): user/skill MUST append manually. See `(C) notebooklm.md` reminder.
> - Path 4 (multi-URL bundle): same as path 3.
> - Path 5 (yt-search only, no ingest): NO inventory row needed (nothing landed in `raw/`).
> - Path 6 (custom scraper): scraper script SHOULD print the inventory row to append; user pastes it.
> - Path 7 (query mode): NO inventory row needed (nothing landed in `raw/`).
> - Path 8 (promotion to Storm Bear): NO new row, but update existing row's `Status` → `promoted`.
>
> **When the user asks "what topics are done"**, the librarian (Claude) reconciles this file ↔ `wiki/_master-index.md` and reports BOTH compiled and uncompiled artifacts. Never trust `topics-queue.md` alone.

---

## Inventory

| Date | Slug | Path | Source(s) | Size | NotebookLM ID | Status | Wiki link |
|---|---|---|---|---|---|---|---|
| 2026-05-07 | claude-code-hooks | 1 yt-pipeline | YouTube ×5 | 16K | (in raw file) | compiled | [wiki/claude-code-hooks/](../wiki/claude-code-hooks/_index.md) |
| 2026-05-07 | workflow-ai-coding | 1 yt-pipeline | YouTube ×6 | 20K | `ec93ea09-b589-4103-95a9-3fb2c13d5a2e` | compiled | [wiki/workflow-ai-coding/](../wiki/workflow-ai-coding/_index.md) |
| 2026-05-07 | 10x-claude-code | 1 yt-pipeline | YouTube ×6 | 20K | `d1d18b0b-ab85-4773-a999-98f36fb39cf5` | compiled | [wiki/10x-claude-code/](../wiki/10x-claude-code/_index.md) |
| 2026-05-07 | remote-agent-control-tunneling | 2 cron-overnight | YouTube ×N | 20K | `46ee01f8-81e3-47d6-b617-4c322359b6b9` | merged-into-stack | [wiki/telegram-remote-control-stack/](../wiki/telegram-remote-control-stack/_index.md) |
| 2026-05-07 | mcp-messaging-platforms | 2 cron-overnight | YouTube ×N | 20K | `183e3635-ea8c-4c52-9c16-11aa32e19c78` | merged-into-stack | [wiki/telegram-remote-control-stack/](../wiki/telegram-remote-control-stack/_index.md) |
| 2026-05-07 | claude-code-sdk-headless | 2 cron-overnight | YouTube ×N | 20K | `dafc8c4f-840b-41a1-b125-bfe973c919f0` | merged-into-stack | [wiki/telegram-remote-control-stack/](../wiki/telegram-remote-control-stack/_index.md) |
| 2026-05-07 | telegram-bot-remote-control | 2 cron-overnight | YouTube ×N | 20K | `5f514e9c-d8e4-42be-af1e-c456dfa1e4c7` | merged-into-stack | [wiki/telegram-remote-control-stack/](../wiki/telegram-remote-control-stack/_index.md) |
| 2026-05-07 | lark-claude-course | 6 custom-scraper | Lark wiki, 261 pages | 1.9M | `2a42eeff-a797-44cd-86d5-f8b8a4ee491b` ("Claude Couse 2026", 319 sources) | uncompiled | — |
| 2026-05-08 | telegram-remote-control-stack | (compile-merge) | 4 raw bundles + live pilot | (synthesis) | (multiple, see merged rows) | compiled | [wiki/telegram-remote-control-stack/](../wiki/telegram-remote-control-stack/_index.md) |
| 2026-05-09 | harness-engineering-anchor (VTT) | 5 yt-dlp-only | YouTube am_oeAoUhew (Lopopolo talk 46:20) | 394K | — | compiled | [wiki/harness-engineering/](../wiki/harness-engineering/_index.md) |
| 2026-05-09 | harness-engineering-anchor (transcript) | 5 yt-dlp-only | derived from VTT via vtt-to-md.py | 44K | — | compiled | [wiki/harness-engineering/](../wiki/harness-engineering/_index.md) |
| 2026-05-09 | harness-engineering-anchor (structured) | 4 multi-bundle | YouTube + Latent Space podcast (2 sources, 6-section synthesis) | 22K | `d772d58b-ff6c-41c5-aec1-7cd83637226e` | compiled | [wiki/harness-engineering/](../wiki/harness-engineering/_index.md) |
| 2026-05-09 | openai-blog-harness-engineering (HTML) | bypass-403-tier-1 | Playwright vanilla after curl Tier 0 failed | 478K | — | compiled | [wiki/harness-engineering/](../wiki/harness-engineering/_index.md) |
| 2026-05-09 | openai-blog-harness-engineering (clean MD) | bypass-403-tier-1 | derived from HTML via html-to-clean-md.py (readability-lxml + pandoc) | 21K | `d772d58b-…26e` (uploaded as 3rd source) | compiled | [wiki/harness-engineering/](../wiki/harness-engineering/_index.md) |
| 2026-05-09 | openai-blog-delta-synthesis | 4 multi-bundle | NotebookLM 3-source delta-analysis (blog vs talk vs podcast) | 8K | `d772d58b-…26e` | compiled | [wiki/harness-engineering/blog-talk-evolution](../wiki/harness-engineering/blog-talk-evolution.md) |
| 2026-05-09 | openai-symphony-spec (FAILED) | bypass-403-tier-2 | Tier 1+2 failed (backend-gate Cloudflare); pivoted to community | 396K HTML (Next.js error page only) | — | dropped (pivot) | — |
| 2026-05-09 | symphony-community-implementations | 4 multi-bundle | 3 GitHub repos: ACNoonan/symphony-restate (Elixir+Restate) + ryanjdillon/symphony (Go) + howardpen9/symphony-rs (Rust) | (NotebookLM-indexed) | `d772d58b-…26e` (added as sources 4-6) | compiled | [wiki/harness-engineering/symphony-architecture](../wiki/harness-engineering/symphony-architecture.md) |
| 2026-05-09 | symphony-community-synthesis | 4 multi-bundle | NotebookLM 6-source triangulation (3 OpenAI + 3 community) | 9K | `d772d58b-…26e` | compiled | [wiki/harness-engineering/symphony-architecture](../wiki/harness-engineering/symphony-architecture.md) |
| 2026-05-11 | claude-md-12-rules-mnilax | 3 manual-paste | X.com tweet thread (auth-walled — mirrors dead) | 14K | — | compiled | [wiki/claude-md-12-rules/](../wiki/claude-md-12-rules/_index.md) |
| 2026-05-11 | vividkit-claudekit-guides (HTML) | bypass-403-tier-0 | curl 21 guides from vividkit.dev | ~600K HTML total | — | compiled | [wiki/claudekit/](../wiki/claudekit/_index.md) |
| 2026-05-11 | vividkit-claudekit-guides (clean MD) | bypass-403-tier-0 | html-to-clean-md.py with `main` selector | 250K MD total | — | compiled | [wiki/claudekit/](../wiki/claudekit/_index.md) |
| 2026-05-11 | vividkit-claudekit-synthesis | 4 multi-bundle | NotebookLM 21-source synthesis (6 sections) | 24K | `d179ac0c-428b-47e6-b859-99a6b7e7bcb1` | compiled | [wiki/claudekit/](../wiki/claudekit/_index.md) |
| 2026-05-13 | agent-dashboard-agent-os-claude-code-observability | 2 cron-overnight | YouTube ×6 | 18K | `54d7812d-2305-4eac-b250-43ba577cb1dc` | compiled ⚠️ anchor-miss | [wiki/agent-dashboard-os/](../wiki/agent-dashboard-os/_index.md) |
| 2026-05-13 | auto-loop-goals-with-human-in-the-loop | 2 cron-overnight | YouTube ×6 | 18K | `abe1647e-c9c3-4ad1-8e63-5e93fac50865` | compiled ⚠️ low-signal | [wiki/autonomous-loops-human-in-the-loop/](../wiki/autonomous-loops-human-in-the-loop/_index.md) |
| 2026-05-13 | harness-engineering-personal-repo-continuation-vie | 2 cron-overnight | YouTube ×6 | 19K | `58c51d8e-ab36-4331-993f-8a61dfd0a2c4` | compiled (extension) | [wiki/harness-engineering/](../wiki/harness-engineering/_index.md) |
| 2026-05-13 | codex-long-running-agentic-harness-alternative-to | 2 cron-overnight | YouTube ×6 | 18K | `01707594-d36a-4a2f-b3f8-7fa9044528ba` | compiled ⚠️ anchor-miss | [wiki/codex/](../wiki/codex/_index.md) |
| 2026-05-13 | open-source-claude-design-clones-alternative-agent | 2 cron-overnight | YouTube ×6 | 19K | `5155a280-86ce-49ce-8328-d4b75c0119ce` | compiled ⚠️ off-target | [wiki/claude-code-clones/](../wiki/claude-code-clones/_index.md) |
| 2026-05-13 | ai-daily-news-may-2026-weekly-snapshot | 2 cron-overnight | YouTube ×3 | 17K | `9f08f424-31bc-4fe9-8e8b-3a91862171a1` | compiled ⚠️ rumor-heavy | [wiki/ai-news-2026-w19/](../wiki/ai-news-2026-w19/_index.md) |
| 2026-05-20 | tejas-kumar-harnesses-deep-dive | 5 yt-dlp-only | YouTube C_GG5g38vLU (Tejas Kumar IBM, AI Engineer 2026 talk, 20:26, 38.7K views) | 31K | — | compiled (definitional anchor candidate N=1) | [wiki/harness-engineering/tejas-kumar-anchor](../wiki/harness-engineering/tejas-kumar-anchor.md) |
| 2026-05-20 | langchain-interrupt-26-adl-transcript | 5 yt-dlp-only | YouTube jWy39wavbjY (Harrison Chase + Ankush Gola, LangChain Interrupt 2026 keynote, 44:58, ~1.9K views) | 67K | — | compiled (new topic agent-development-lifecycle, N=1 anchor) | [wiki/agent-development-lifecycle/](../wiki/agent-development-lifecycle/_index.md) |
| 2026-05-20 | howznguyen-router-opus-gpt-subagent | 3-webfetch | Blog howznguyen.dev (Vietnamese, ~20 min read, 2026-05-19) | 14K | — | compiled (individual-scale 5th sibling article) | [wiki/harness-engineering/personal-repo-router-multimodel](../wiki/harness-engineering/personal-repo-router-multimodel.md) |
| 2026-05-21 | anthropic-large-codebases-blog | 3-webfetch | claude.com/blog (Anthropic first-party, published 2026-05-14) | 8K | — | compiled (authoritative anchor) | [wiki/harness-engineering/anthropic-large-codebases-anchor](../wiki/harness-engineering/anthropic-large-codebases-anchor.md) |
| 2026-05-21 | cole-medin-anthropic-masterclass-transcript | 5-yt-dlp-only | YouTube efRIrLXoOVA (Cole Medin, 28:10, 2.1K views as of 2026-05-21, uploaded 2026-05-21) | 47K | — | compiled (authoritative anchor walkthrough) | [wiki/harness-engineering/anthropic-large-codebases-anchor](../wiki/harness-engineering/anthropic-large-codebases-anchor.md) |
| 2026-05-21 | coleam00-helpline-readme | 3-webfetch | github.com/coleam00/helpline README + API metadata (Python repo, created 2026-05-19, 2 stars at fetch) | 7K | — | compiled (worked-example sibling article) | [wiki/harness-engineering/helpline-worked-example](../wiki/harness-engineering/helpline-worked-example.md) |
| 2026-05-21 | nemanja-codex-claude-hermes-orchestrator-transcript | 5-yt-dlp-only | YouTube O-PEeD7fymo (Nemanja Mirkovic, 13:48, 2175 views as of 2026-05-21, uploaded 2026-05-20) | 11K | — | compiled (individual-scale 6th sibling article — orchestrator-mediated cross-vendor) | [wiki/harness-engineering/personal-repo-hermes-orchestrator](../wiki/harness-engineering/personal-repo-hermes-orchestrator.md) |
| 2026-05-21 | nemanja-goal-vs-ralph-transcript | 5-yt-dlp-only + 3-webfetch | YouTube CKtz9lp8X-8 (Nemanja Mirkovic, 19:09) + GitHub API NousResearch/hermes-agent recursive tree (repo audit, negative finding on profile defaults) | 13K | — | compiled (orchestrator-prerequisite article on `/goal` mechanics + repo audit) | [wiki/harness-engineering/hermes-goal-mechanics](../wiki/harness-engineering/hermes-goal-mechanics.md) |
| 2026-05-21 | nemanja-goal-video-resources-repo | 3-webfetch + 5-yt-dlp-only (comments) | github.com/nemanjadotcom/goal-video-resources (4 verbatim files: PROMPT.md + AGENTS.md + SOUL-codexbuilder.md + SOUL-claudereviewer.md) + YouTube O-PEeD7fymo comments (13 comments incl. billing corroboration from @kikserthg233 + cross-vendor pattern N=2 evidence from @aichess.online) | 10K | — | merged-into-stack (findings folded into [[personal-repo-hermes-orchestrator]] + [[hermes-goal-mechanics]] + subscription-billing audit) | [wiki/harness-engineering/hermes-goal-mechanics](../wiki/harness-engineering/hermes-goal-mechanics.md) |
| 2026-05-21 | zen-van-riel-agentic-engineer-workflow | 5-yt-dlp-only + 3-webfetch | YouTube ElYxdpYi4U0 (Zen van Riel, 17:10, 3389 views as of 2026-05-21, uploaded 2026-05-20) + companion repo AI-Engineer-Skool/zen-agentic-engineer-config (ALL 7 files verbatim — initial 4 + follow-up 4: shell.zsh + tmux.conf + .claude/commands/smell.md + README.md + install.sh + statusline.sh + statusline-daemon.sh + bin/clip) + 14 video comments incl. @priitraag pattern refinement + @elpepelucho N=2 anti-SDD corroboration | 31K | — | compiled (individual-scale 7th sibling — mixed-effort parallel-streams + catalog-driven /smell; pilot-readiness verified post-full-repo-audit; surfaces Claude Code v2.0.65+ `.context_window` JSON API as corpus signal) | [wiki/harness-engineering/personal-repo-zen-mixed-effort-parallel](../wiki/harness-engineering/personal-repo-zen-mixed-effort-parallel.md) |
| 2026-05-21 | herdr-agent-multiplexer-shin-celik | 5-yt-dlp-only + 3-webfetch | YouTube XoitaexiCi0 (Hal Shin explainer, 13:19, 25,219 views as of 2026-05-21, uploaded 2026-05-17) + ogulcancelik/herdr Rust repo (2020★ AGPL-3.0; 6 files verbatim: README.md + SKILL.md + AGENTS.md + quick-start.mdx + configuration.mdx + agents.mdx + install.mdx; default branch is `master` not main; full tree of ~60 files via GitHub API) + 91 video comments incl. top-liked critical (6♥) "tmux is enough" + top-liked pro-tip (12♥) "use the SKILL.md" + 7+ competing tools surfaced (cmux/agent-deck/Workmux/Conductor/T3 Code/Agent of Empires/Claude `/remote-control`) | 28K | — | compiled (individual-scale 8th sibling — Herdr agent multiplexer as terminal substrate; includes explicit tmux-vs-Herdr best-practices decision tree per user framing; 2nd corpus instance of skill-files-as-engineering-artifacts pattern) | [wiki/harness-engineering/personal-repo-herdr-agent-multiplexer](../wiki/harness-engineering/personal-repo-herdr-agent-multiplexer.md) |
| 2026-05-23 | autonomous-loops-with-hitl-anchor-injection-re-run | 1 yt-pipeline (manual trigger via `python bin/autopilot-drain.py`) | YouTube ×6 anchor-injected: vjJwgXsMfjM (AI Andy 58K) + 9jxrmk_Xses (Tonbi's AI Garage 44K) + o-pMCoVPN_k (Developers Digest 88K) + Yl_GGlAQ4Gc (WorldofAI 33K) + rnvNW-6XniU (Nemanja Mirkovic 321) + jfAIKrNMKvM (Siggi 231) — all 6 force-included via Anchors mechanism, 0 from yt-search. 3rd attempt at this topic — closes 2026-05-14 operator-action-item #1 (anchor-URL injection) after 2026-05-13 1st run anchor-miss + 2026-05-21 2nd tighter-query-rerun 0-results-abort | 17K | `94db9216-eb26-489d-8f06-fd65fbea3fd4` | raw (awaiting compile — supersede vs supplement decision pending on `wiki/autonomous-loops-human-in-the-loop/`) | TBD compile target — likely supersede [[wiki/autonomous-loops-human-in-the-loop/_index]] anchor-miss content from 2026-05-14 |

## Status legend

- **raw** — landed in `raw/`, not yet compiled
- **uncompiled** — same as `raw` but explicitly waiting for compile (vs in flight)
- **partial** — some articles compiled, more pending
- **compiled** — fully synthesized into `wiki/<topic>/`
- **merged-into-stack** — content folded into a larger compiled topic; raw file kept for audit trail
- **promoted** — already compiled here AND lifted to Storm Bear curated wiki via `llm-wiki-routine-v2.1`
- **dropped** — deliberately not compiled (e.g., low signal, off-scope); reason should be in a comment row below

## Path legend (8 ingestion surfaces)

1. `/loop autopilot research <topic>` — single-topic burst (yt-pipeline)
2. `/schedule autopilot nightly` — overnight cron, drains `topics-queue.md`
3. `notebooklm source add <url>` — single URL/PDF/YouTube
4. `notebooklm notebook create + source add ×N` — multi-URL bundle
5. `yt-dlp ytsearch20:"<q>"` — search only, no ingest (NO inventory row)
6. Custom scraper (Playwright + SPA) — Lark/Notion/Confluence
7. `notebooklm ask` — query mode (NO inventory row)
8. Promotion → Storm Bear curated wiki (UPDATE existing row, no new row)

## Coverage summary (auto-derivable; manually maintained until Lớp 3 ships)

- **Total ingestions logged:** 41 rows (8 added 2026-05-21 [see prior bullet history] + 1 added 2026-05-23: autonomous-loops-with-hitl-anchor-injection-re-run via 1 yt-pipeline manual trigger — closes 2026-05-14 anchor-miss with 6 force-included anchors)
- **Compiled (or merged):** 38 (was 30 → +8 from 2026-05-21 work); +1 raw awaiting compile (autonomous-loops anchor-injection-re-run)
- **Uncompiled / raw (awaiting compile):** 2 (lark-claude-course 261 pages — biggest remaining backlog + autonomous-loops-with-hitl-anchor-injection-re-run 17K — fresh from 2026-05-23 manual drain)
- **Dropped (intentional):** 1 (Symphony spec page failed Tier 2; pivoted to community impls)
- **Uncompiled / raw (awaiting compile):** 1 (lark-claude-course 261 pages — biggest remaining backlog)
- **Promoted to Storm Bear:** 0
- **New topics 2026-05-11:** 2 added — claude-md-12-rules (3 articles, Mnilax behavioral contract) + claudekit (7 articles, vividkit.dev framework comparison with harness-engineering + 12-rules)
- **2026-05-13 overnight drain:** 6 topics drained ~20 min (22:43→23:03). All in Status: raw, awaiting morning compile. Loop log: `loop-log/(C) 2026-05-13-22-autopilot-overnight.md`. Note: topic 2 (Auto-Loop Goals) had to relax recency filter — selection pulled in generic 2025 IBM/CNN/"What is Agentic AI" videos rather than Karpathy autoresearch / Ralph loop content; signal may be lower than other 5. Worth a re-run with tighter query.
- **2026-05-14 morning compile:** All 6 overnight-drain topics compiled into wiki/ (5 NEW topics + 1 extension to harness-engineering). 33 new wiki articles + 6 _index.md (5 new + 1 updated harness extension). **CRITICAL META-FINDING:** 4 of 6 raw bundles had **anchor-miss** — the yt-search auto-selection rubric (log(views) + engagement×3 + recency×2 with channel-cap-2) did NOT surface the user-provided anchor URLs. Topics affected: agent-dashboard-os (Chase AI anchor missing), codex (all 3 anchors missing), claude-code-clones (off-target — bundle was developer-workflow not clone-focused), autonomous-loops (recency-filter relaxation → generic 2025 explainers). Only harness-engineering-personal partially captured anchor framing (Tù Bà Khuỳm). Implication: query-only search rubric is too weakly weighted toward operator-named anchors. **Operator action items:** (1) for next overnight, consider anchor-URL injection into the drain script (force-include named URLs before yt-search top-K); (2) tighten queries (add specific creator names / video keywords); (3) flag all anchor-miss compiles for re-run with refined queries. Loop log: `loop-log/(C) 2026-05-14-XX-autopilot-compile.md`.
- **Path 9 emerged:** manual paste when source is auth-walled + mirrors dead (X.com 2026-05-11). Update CLAUDE.md "8 ingestion surfaces" table when this pattern occurs ≥3× total.
- **Bulk fetch pattern emerged:** 21-URL fetch via `bin/bulk-fetch-vividkit.sh` (Path 6 custom scraper variant for sites without Cloudflare) — codify as reusable pattern when 2nd bulk-fetch occurs.
