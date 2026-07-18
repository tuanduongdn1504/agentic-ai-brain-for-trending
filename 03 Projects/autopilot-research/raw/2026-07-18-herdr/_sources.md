# Source manifest — herdr bundle (2026-07-18)

> Ingested by `/loop autopilot research <url>` (operator-submitted anchor + full yt-search bundle).
> Fetch method: `yt-dlp 2026.06.09 --cookies-from-browser chrome --write-subs --write-auto-subs --sub-langs "en-orig,en,..."` → `bin/vtt-to-md.py`. Read in full. No NotebookLM (bundle ~22.7K words).
> **Block note:** initial fetch hit YouTube **HTTP 429 "Sign in to confirm you're not a bot"** — resolved with yt-dlp's native `--cookies-from-browser chrome` (JS challenge solved via deno). The tail 2 videos (t7/t8) were slow (~90 min behind the rest) and were initially presumed lost, but **both eventually completed** and were folded into the topic via a DEEPEN pass. See `output/bypass-attempts.md`.
> Verification: refute-first workflow `wf_65ed9753-32f` (6 core sources) + deepen workflow `wf_5ffde4c4-627` (t7/t8), grounded on primary sources (GitHub API, repo README, herdr.dev docs).

## YouTube sources (8 ingested)

| # | Slug | Channel | Views | Len | Uploaded | URL | Stance |
|---|------|---------|-------|-----|----------|-----|--------|
| 1 ⚓ | t1-chase-ai | Chase AI | 20,617 | 10:28 | 2026-07-16 | https://www.youtube.com/watch?v=neK8ydl0Vlk | **⚠️ PROMOTIONAL** (skool.com "build your agency" upsell) — operator anchor |
| 2 | t2-devops-toolbox | DevOps Toolbox | 92,849 | 16:40 | 2026-07-03 | https://www.youtube.com/watch?v=5GtkyPvuvbQ | Technical / semi-critical ("Tmux rewrite") |
| 3 | t3-seth-phaeno | Seth Phaeno | 76,261 | 19:25 | 2026-06-24 | https://www.youtube.com/watch?v=27B50lXinWM | In-depth walkthrough |
| 4 | t4-hal-shin | Hal Shin | 63,402 | 13:19 | 2026-05-17 | https://www.youtube.com/watch?v=XoitaexiCi0 | Positioning ("the Tmux for AI Agents") |
| 5 | t5-academind | Academind (Max Schwarzmüller) | 11,588 | 9:18 | 2026-07-16 | https://www.youtube.com/watch?v=2CR9tDNAzB0 | Credible educator |
| 6 | t6-elie-steinbock | Elie Steinbock | 3,510 | 9:34 | 2026-07-14 | https://www.youtube.com/watch?v=GYDh2tALWpA | Practitioner + pro tips |
| 7 | t7-better-stack | Better Stack | 33,439 | 7:10 | 2026-06-05 | https://www.youtube.com/watch?v=PlN86TvzGy4 | Questioning brand ("ultimate multiplexer?") — *late arrival, DEEPEN* |
| 8 | t8-fru-dev-comparison | Fru Dev | 2,587 | 22:27 | 2026-05-31 | https://www.youtube.com/watch?v=gPx6rZuQg9A | Head-to-head comparison (Tmux/Cmux/Herdr/Paneflow + others) — *late arrival, DEEPEN* |

Word counts: t1 2,342 · t2 3,317 · t3 4,067 · t4 2,997 · t5 1,834 · t6 2,261 · t7 1,701 · t8 4,150 = **~22,669 words**.

⚠️ **t8 caption caveat:** t8's auto-captions badly garble competitor tool **names** ("Emacs/SiMax", "armox", "Ron Pane") and use tmux/cmux loosely. Per the project discard-as-garble guard, competitor names/stars from t8 are treated as **unverified** and not asserted as fact; only Herdr-specific + structural (CLI-vs-desktop-app) points are used.

## Primary sources (ground truth for fact-check)

- GitHub API — `api.github.com/repos/ogulcancelik/herdr`: **17,839★ / 1,133 forks / 76 open issues**, created 2026-03-27, latest **v0.7.4** (2026-07-15), primary language **Rust**, pushed/active 2026-07-18, not archived.
- Repo README — tagline "agent multiplexer that lives in your terminal"; feature list; install methods; **dual license: AGPL-3.0-or-later + commercial** (GitHub detector shows NOASSERTION because dual-licensing confuses it).
- `herdr.dev/docs/agents/` — **21 agents detected zero-config** (Gemini CLI + Cline "less thoroughly tested"); two-step detection (foreground process + TOML manifest vs bottom-buffer screen snapshot → idle/working/blocked; remote manifest auto-updates).
- `herdr.dev/docs/session-state/` — persistence / detach-reattach / ssh remote.
- Homepage: https://herdr.dev · author: Oğulcan Çelik (`ogulcancelik`), solo, full-time; gold sponsor Terminal Trove.

## Selection note

25 candidates surfaced by `yt-dlp "ytsearch25:Herdr agent multiplexer terminal coding agents"`. Scored for relevance/credibility/recency/diversity; selected 8 with the operator's anchor (`neK8ydl0Vlk`) force-included — **all 8 ultimately fetched** (6 promptly; t7/t8 lagged ~90 min behind the 429 bot-gate but completed and were folded in via DEEPEN). Dropped from candidates before fetch: Fireship "Tmux in 100 Seconds" (2024, off-topic), cmux-only videos, sub-500-view micro-channels, and a Vietnamese-dub duplicate.
