# Overview — Chase AI's 17 Claude Plugins

## Source

- **Video:** Chase AI — "Use These 17 Claude Plugins, It Will Make You 10x Better." ([V2RIVnGCy74](https://www.youtube.com/watch?v=V2RIVnGCy74), 2026-06-26, 17:30, 16.5K views).
- **Transcript:** `raw/2026-06-29-claude-code-plugins-17-chase-ai.md` (yt-dlp `en` auto-subs, deduped to ~3,840 words, read in full).
- **Creator:** Chase AI (@Chase-H-AI) — already cited in [[10x-claude-code/_index]] and was the named anchor for [[agent-dashboard-os/_index]]. Runs a paid Skool community (skool.com/chase-ai, "Claude Code Masterclass"); the video is competent top-of-funnel content.

## The thesis

> *"Claude Code out of the box is one of the strongest AI tools on the planet, [but] we can make it way better by simply adding plugins, skills, and CLIs to our stack... there are hundreds... so how do you know what is actually worth your time?"*

Chase answers with 17 of his daily drivers, organized into three buckets. He's loose with the category labels (says "data, design, productivity" but presents Design → Productivity → Data), and loose with "plugin/skill/CLI" (he uses the three interchangeably — they are genuinely different things; see the crosscutting theme below). But the picks are real, mostly free, and mostly high-quality.

## The three buckets (presentation order)

**Design (0:37):**
1. **Taste Skill** — anti-slop frontend design skill (3 dials + pre-flight gate). *Already deep-dived in [[ai-web-design-workflow/_index]].*
2. **Impeccable** — rival anti-slop design skill; 44 deterministic detector rules + 23 commands + a beta(→**alpha**) live visual editor. *NEW.*
3. **Awesome Design MD** — 73+ brand `DESIGN.md` files in Google-Stitch format; "clone the design *language*, not the site." *Already in [[claude-code-skills-stack/_index]].*
4. **Ponytail** — "the laziest senior dev": a decision ladder that makes the agent write less code. *NEW; fastest-growing repo in the set.*

**Productivity (5:01):**
5. **notebooklm-py** — CLI bridge to Google NotebookLM. *This is the engine your `yt-pipeline` runs on.*
6. **Playwright CLI** — browser automation, "way less tokens than the MCP." *Already in [[claude-code-skills-stack/_index]].*
7. **Codex Plugin** — official OpenAI plugin; Codex as adversarial reviewer + `/codex:rescue`. *Already in [[codex/_index]] + Storm Bear v62.*
8. **GWS** — Google Workspace CLI; "got the guy fired." *NEW.*
9. **GitHub CLI** — "should be the first thing you install." *NEW (as a topic).*
10. **Skill Creator** — first-party Anthropic; create/improve/**measure** skills. *Already in [[claude-code-skills-stack/_index]] + [[claude-skills/_index]].*
11. **Last 30 Days** — deep multi-platform research (Reddit/X/YouTube/HN/Polymarket…). *NEW.*

**Data (11:07):**
12. **Firecrawl** — web scraping past bot-protection; paid + open-source. *NEW.*
13. **autoresearch** — Karpathy's "ML in a box" overnight loop. *This is the ur-pattern your routine ports.*
14. **Supabase CLI** — Postgres + auth + edge functions from the terminal. *NEW; the #1 hireui fit.*
15. **Obsidian** — `obsidian-skills` to "improve Claude Code memory." *Already in [[claude-code-skills-stack/_index]] + [[claude-code-memory-systems/_index]].*
16. **LightRAG** — "the real deal" graph + embeddings RAG. *Already mentioned in [[claude-code-memory-systems/_index]] (L5).*
17. **Stripe CLI** — payments from the terminal. *NEW.*

## The headline for THIS operator: 9 of 17 you already have

This is the most-overlapping roundup the vault has ingested. Of the 17:

- **2 are this project's own foundation/toolchain** — `karpathy/autoresearch` (the [[autopilot-research-routine]] is an explicit port of its `val_bpb`→`gaps_closed_ratio`, 5-min-budget→wall-clock-budget, git-checkpoint→loop-log design) and `teng-lin/notebooklm-py` (the engine your `yt-pipeline` skill drives). See [[claude-code-plugins-stack/originals-this-project-runs-on]].
- **7 are already deep-dived** in other topics (Taste Skill, Awesome Design MD, Playwright CLI, Codex Plugin, Skill Creator, Obsidian, LightRAG). See [[claude-code-plugins-stack/already-deep-dived-crosswalk]].
- **8 are genuinely new** to the wiki: Impeccable, Ponytail, GWS, GitHub CLI, Last 30 Days, Firecrawl, Supabase CLI, Stripe CLI.

So the value of this ingest is **(a) a verified map of where the picks land in your existing knowledge, (b) full deep-dives of the 8 new tools, and (c) the corrections** — Chase makes several overstated or wrong claims that the adversarial pass caught.

## Seven cross-cutting themes (the synthesis worth keeping)

1. **CLI-over-MCP token thesis** — the most concrete idea in the video. Playwright CLI (writes state to disk vs streaming the a11y tree into context), notebooklm-py (CLI > web UI features), Firecrawl CLI. *Caveat: the famous "27K vs 114K tokens, ~4× cheaper" Playwright figure is a third-party benchmark, not first-party Microsoft data.*
2. **Design anti-slop cluster (3 orthogonal layers)** — **tokens** (Awesome Design MD: drop a `DESIGN.md`, agent reads it natively) + **mechanical detection** (Impeccable: 44 deterministic rules, no LLM, + a live visual editor) + **aesthetic guidance** (Taste Skill: dials + pre-flight gate). They *compose*; they're not substitutes.
3. **Two tools that ARE this project's foundation** — autoresearch and notebooklm-py. You don't "adopt" these; you already run them. The action is *upgrade/refine*, not *install*.
4. **Cost-discipline / minimalism cluster** — Ponytail (write less code: −54% LOC on Haiku), Playwright CLI (token-cheap), and free-tier infra (Supabase, GWS, LightRAG-OSS). Composes directly with [[claude-api-cost-optimization/_index]].
5. **"Works WITH Claude Code, not integrated INTO it"** — at least 6 of the 17 (Obsidian-skills nuance, autoresearch manual loop, Firecrawl REST/MCP, GWS CLI, LightRAG server, Stripe CLI) are tools you *shell out to* from a Claude Code session, not native skills/plugins. Chase's "connect X to Claude Code" framing blurs this. It matters for setup expectations.
6. **Free ≠ free-of-limits** — only autoresearch and Awesome Design MD are truly free/open. The rest are freemium with real limits: Supabase **auto-pauses after 1 week** + no auto-backups on free tier; Firecrawl is 1 credit/page after 1K free/month and self-host loses bot-evasion; LightRAG is "lightweight" in architecture but needs a capable LLM.
7. **hireui Goal #2 infra cluster** — the recruitment SaaS (zero LLM today) maps cleanly onto: **Supabase CLI** (⭐⭐⭐ — Postgres/auth/types/edge functions: candidate forms, applicant data), Stripe CLI (⭐⭐ — *if* monetized), Firecrawl (⭐⭐ — candidate/job scraping), Playwright CLI (⭐ — QA for the Candidate-Detail refactor).

## Source provenance (summary)

- **Transcript:** primary, read in full (path 5 yt-dlp).
- **Every original** independently fetched + `gh api`-verified 2026-06-29; an adversarial verifier re-checked each tool's load-bearing claims with fresh web search + `gh api`.
- **Corrections** (full list in [[claude-code-plugins-stack/source-provenance]]): Impeccable→Copilot REFUTED; Obsidian "founder"→CEO REFUTED; autoresearch "any app" overstated + "83 exp" unverified; Firecrawl open-source "same functionality" REFUTED; Stripe CLI "natural language in Claude Code" REFUTED; GWS firing real-but-nuanced; Ponytail "50%"→−54% + Opus-claim unverified; Playwright "70+ commands"→~40-50; Taste Skill gate-count unverifiable; LightRAG perf-vs-GraphRAG contradicted by 2025 meta-eval.

## Next

Read [[claude-code-plugins-stack/the-17-plugins]] for the per-tool catalog, or jump to the pilot menu in `output/(C) 2026-06-29-claude-code-plugins-stack-pilot-methods.md`.
