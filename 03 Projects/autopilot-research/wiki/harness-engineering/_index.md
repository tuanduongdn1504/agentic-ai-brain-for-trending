# harness-engineering

> **Anchor:** Ryan Lopopolo (OpenAI Frontier & Symphony) — AI Engineer 2026 keynote + Latent Space podcast 2026-04-07
> **First compiled:** 2026-05-09 — extended 2026-05-14 with individual-scale layer (Tù Bà Khuỳm anchor + 6 English-language YouTube sources)
> **Article count:** 14 (10 org-scale + 4 individual-scale)
> **Status:** Anchor seeded — designed for ongoing ingestion; expect 10-20+ articles as research thread expands

This topic is the autopilot wiki's research thread on **harness engineering** — Lopopolo's discipline for restructuring software work around the assumption that humans steer and agents execute. The anchor defines the conceptual surface; subsequent ingests fill gaps, falsify claims, or expand cited references. The 2026-05-14 extension adds an **individual-scale axis** (single developer, single repo) to test which Lopopolo positions are scale-invariant vs scale-bounded.

## Articles

### Org-scale (Lopopolo anchor)

- [[anchor-bundle-overview]] — what the anchor is, what it covers, how to navigate (3 sources after 2026-05-09 blog ingest)
- [[core-claims]] — 8 falsifiable claims with timestamp citations (the testable core of harness engineering)
- [[terminology]] — Harness Engineering, Token Billionaire, Symphony, Frontier, Ghost Libraries, Agent-Legibility, Dark Factory, Ralph Loop, Skills, Isomorphic
- [[cited-references]] — 35+ external references (tools, people, papers, companies) — the downstream research surface
- [[open-questions]] — 10 explicit hedges and gaps (where Lopopolo says "I don't know yet")
- [[contrarian-stances]] — 10 positions Lopopolo argues against (manual coding, pre-merge review, MCP, plan mode, etc.)
- [[blog-talk-evolution]] — Feb blog vs Apr talk+podcast: 6 position-hardenings + 10+ blog-exclusive technical details (Layers / Map-Not-Manual / Doc-Gardening / Aardvark / Friday-Slop / etc.)
- [[symphony-architecture]] — 6-source triangulation (3 OpenAI + 3 community implementations) covering convergence + divergence + community-added capabilities + falsifier check on claim #4 throughput (NOT INDEPENDENTLY CORROBORATED as of 2026-05-09)
- [[research-roadmap]] — prioritized next 5-10 ingests to expand this thread

### Individual-scale (Tù Bà Khuỳm anchor + 6 YouTube sources, added 2026-05-14)

- [[personal-repo-overview]] — what individual-scale harness means and the load-bearing primitives (`CLAUDE.md`, validation loops, multi-Claude); how the framing differs from Lopopolo
- [[personal-repo-patterns]] — 12 concrete techniques (`/init` bootstrap, Plan Mode, GCAO prompting, `progress.md`, sub-agents, Git worktrees, adversarial eval, skill curation, MCP, `#` corrections, `/context` audits, Dispatch)
- [[personal-repo-vs-org-scale]] — axis-by-axis comparison: 5 convergences + 6 divergences + claim-by-claim challenge map ([[core-claims]] #2 partially falsified, #5 silent, #6 doesn't translate)
- [[personal-repo-gaps]] — 5 production-readiness gaps + 5 structural gaps + 5 NotebookLM follow-up topics routed to [[research-roadmap]]

## Cross-links to existing autopilot topics

- [[external|workflow-ai-coding/_index]] — Lopopolo is one of 6 practitioners covered there; this topic deep-dives his specific contribution
- [[external|10x-claude-code/_index]] — tactical overlap on tooling (CLI-first, status lines, hooks)
- [[external|claude-code-hooks/_index]] — Lopopolo's "Skills" pattern is conceptually adjacent
- [[external|claude-md-12-rules/_index]] — Mnilax's individual-scale rules vs Lopopolo's org-scale harness; see [[external|claude-md-12-rules/comparison-harness-engineering]] for 8 agreement + 4 conflict axes + compound-posture decision rules
- [[external|claudekit/_index]] — vividkit's ClaudeKit framework, the "middle rung" between Mnilax (rules-only) and Lopopolo (org-scale infrastructure); see [[external|claudekit/vs-harness-engineering-and-12-rules]] for 3-way decision matrix

## Sources

### Org-scale anchor (Lopopolo)

- `raw/2026-05-09-harness-engineering-anchor.vtt` — auto-sub VTT (44KB)
- `raw/2026-05-09-harness-engineering-anchor-transcript.md` — verbatim transcript with `[MM:SS]` timestamps (99 paragraphs)
- `raw/2026-05-09-harness-engineering-anchor-structured.md` — 6-section NotebookLM synthesis (469 lines)
- NotebookLM ID: `d772d58b-ff6c-41c5-aec1-7cd83637226e` (2 sources: YouTube + Latent Space)
- Sources 1-10: Lopopolo's talk + podcast + Feb blog + 3 community Symphony implementations (used in `core-claims`, `contrarian-stances`, `symphony-architecture`)

### Individual-scale extension (added 2026-05-14)

- `raw/2026-05-13-harness-engineering-personal-repo-continuation-vie.md` — NotebookLM 5-section synthesis (Summary / Trends / Outliers / Gaps / Takeaways)
- NotebookLM ID: `58c51d8e-ab36-4331-993f-8a61dfd0a2c4` (6 YouTube sources, anchored on Tù Bà Khuỳm — "Chia sẻ về bộ khung Harness Engineering cho chính repository của bạn" — https://www.youtube.com/watch?v=SloXHfkYk34)
- Sources used in `personal-repo-*` articles:
  - [Source 11] John Kim — *How I use Claude Code (Meta Staff Engineer Tips)* — https://www.youtube.com/watch?v=mZzhfPle9QU (46:12, 420K views, 2026-02-07)
  - [Source 12] AI with Avthar — *How I Start EVERY Claude Code Project* — https://www.youtube.com/watch?v=aQvpqlSiUIQ (34:15, 108K views, 2025-12-17)
  - [Source 13] The AI Automators — *Anthropic Just Dropped the New Blueprint for Long-Running AI Agents* — https://www.youtube.com/watch?v=9d5bzxVsocw (16:58, 172K views, 2026-03-25)
  - [Source 14] GritAI Studio — *Master Context in Claude Code in 5 Minutes* — https://www.youtube.com/watch?v=I1EGbrH5Xdk (7:08, 19K views, 2026-02-05)
  - [Source 15] Productive Dude — *FULL Claude Tutorial For Beginners in 2026!* — https://www.youtube.com/watch?v=Xg55nTrbYYY (112:38, 316K views, 2026-04-13)
  - [Source 16] Simon Scrapes — *How to Use Claude Code Skills Like the 1%* — https://www.youtube.com/watch?v=6-D3fg3JUL4 (16:33, 180K views, 2026-03-04)
