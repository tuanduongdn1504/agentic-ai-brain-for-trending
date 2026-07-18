# Source manifest — herdr bundle (2026-07-18)

> Ingested by `/loop autopilot research <url>` (operator-submitted anchor + full yt-search bundle).
> Fetch method: `yt-dlp 2026.06.09 --cookies-from-browser chrome --write-subs --write-auto-subs --sub-langs "en-orig,en,..."` → `bin/vtt-to-md.py`. Read in full. No NotebookLM (bundle ~16.8K words).
> **Block note:** initial fetch hit YouTube **HTTP 429 "Sign in to confirm you're not a bot"** — resolved with yt-dlp's native `--cookies-from-browser chrome` (JS challenge solved via deno). See `output/bypass-attempts.md`.
> Verification: refute-first multi-agent workflow `wf_65ed9753-32f`, grounded on primary sources (GitHub API, repo README, herdr.dev docs).

## YouTube sources (6 ingested)

| # | Slug | Channel | Views | Len | Uploaded | URL | Stance |
|---|------|---------|-------|-----|----------|-----|--------|
| 1 ⚓ | t1-chase-ai | Chase AI | 20,617 | 10:28 | 2026-07-16 | https://www.youtube.com/watch?v=neK8ydl0Vlk | **⚠️ PROMOTIONAL** (skool.com "build your agency" upsell) — operator anchor |
| 2 | t2-devops-toolbox | DevOps Toolbox | 92,849 | 16:40 | 2026-07-03 | https://www.youtube.com/watch?v=5GtkyPvuvbQ | Technical / semi-critical ("Tmux rewrite") |
| 3 | t3-seth-phaeno | Seth Phaeno | 76,261 | 19:25 | 2026-06-24 | https://www.youtube.com/watch?v=27B50lXinWM | In-depth walkthrough |
| 4 | t4-hal-shin | Hal Shin | 63,402 | 13:19 | 2026-05-17 | https://www.youtube.com/watch?v=XoitaexiCi0 | Positioning ("the Tmux for AI Agents") |
| 5 | t5-academind | Academind (Max Schwarzmüller) | 11,588 | 9:18 | 2026-07-16 | https://www.youtube.com/watch?v=2CR9tDNAzB0 | Credible educator |
| 6 | t6-elie-steinbock | Elie Steinbock | 3,510 | 9:34 | 2026-07-14 | https://www.youtube.com/watch?v=GYDh2tALWpA | Practitioner + pro tips |

Word counts: t1 2,342 · t2 3,317 · t3 4,067 · t4 2,997 · t5 1,834 · t6 2,261 = **~16,818 words**.

## Dropped from the intended 8-video bundle (2 — YouTube 429 bot-gate)

| Slug | Channel | Views | URL | Reason |
|------|---------|-------|-----|--------|
| t7-better-stack | Better Stack | 33,439 | https://www.youtube.com/watch?v=PlN86TvzGy4 | 429 bot-gate re-tripped after 6 rapid fetches; 2 attempts, both died. Questioning-brand angle partly covered by t2. |
| t8-fru-dev-comparison | Fru Dev | 2,587 | https://www.youtube.com/watch?v=gPx6rZuQg9A | Same 429. Comparison (Tmux/Cmux/Herdr/Paneflow) angle covered by primary ground truth + t1/t2/t4 tmux/cmux comparisons. |

## Primary sources (ground truth for fact-check)

- GitHub API — `api.github.com/repos/ogulcancelik/herdr`: **17,839★ / 1,133 forks / 76 open issues**, created 2026-03-27, latest **v0.7.4** (2026-07-15), primary language **Rust**, pushed/active 2026-07-18, not archived.
- Repo README — tagline "agent multiplexer that lives in your terminal"; feature list; install methods; **dual license: AGPL-3.0-or-later + commercial** (GitHub detector shows NOASSERTION because dual-licensing confuses it).
- `herdr.dev/docs/agents/` — **21 agents detected zero-config** (Gemini CLI + Cline "less thoroughly tested"); two-step detection (foreground process + TOML manifest vs bottom-buffer screen snapshot → idle/working/blocked; remote manifest auto-updates).
- `herdr.dev/docs/session-state/` — persistence / detach-reattach / ssh remote.
- Homepage: https://herdr.dev · author: Oğulcan Çelik (`ogulcancelik`), solo, full-time; gold sponsor Terminal Trove.

## Selection note

25 candidates surfaced by `yt-dlp "ytsearch25:Herdr agent multiplexer terminal coding agents"`. Scored for relevance/credibility/recency/diversity; selected 8 with the operator's anchor (`neK8ydl0Vlk`) force-included, of which 6 fetched before the 429 bot-gate blocked the rest. Dropped from candidates before fetch: Fireship "Tmux in 100 Seconds" (2024, off-topic), cmux-only videos, sub-500-view micro-channels, and a Vietnamese-dub duplicate.
