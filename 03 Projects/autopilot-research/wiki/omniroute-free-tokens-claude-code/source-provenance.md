# Source Provenance

## Raw bundle
[`raw/2026-07-20-omniroute-free-tokens-claude-code/`](../../raw/2026-07-20-omniroute-free-tokens-claude-code/_sources.md) — operator-submitted anchor + yt-search bundle. Captions via `yt-dlp --cookies-from-browser chrome` → `bin/vtt-to-md.py`. `notebook_id: none` (read directly). Path 1 (`/loop`).

## The 7 videos

| # | ID | Channel | Title | Lang | Dur | Views | Uploaded | Role |
|---|----|---------|-------|------|-----|-------|----------|------|
| anchor/t1 | `x2BmXTur4oo` | DEVKIT AI | Nhận 1,6 Tỷ Token Miễn Phí Cho Claude Code Bằng OmniRoute | vi | 39:15 | 1.7K | 2026-07-16 | headline "1.6B tokens" + VPS install (Path A demo → DeepSeek) |
| t2 | `fXke2rmwOps` | AI Stack Engineer | OmniRoute + OpenCode: 100% Free AI Coding Setup | en | 9:02 | 25K | 2026-07-10 | setup; provider/feature detail |
| t3 | `AQm1ig0GrP4` | Cloud Codes | OmniRoute + OpenCode is INSANE (Why I Dropped Claude Code) | en | 9:13 | 11K | 2026-07-19 | **most balanced** — Path A, "Opus still wins hard problems" |
| t4 | `Zm5VCZXaH0Y` | Real World Devs | Omniroute Free LLM API Setup in 10 Minutes | en | 13:38 | 767 | 2026-07-17 | setup walkthrough |
| t5 | `ibo5PvEBFao` | Panda Making Money | This FREE AI Gateway Gives You Every LLM API for $0 | en | 24:30 | 3.1K | 2026-07-04 | gateway economics; token methodology |
| t6 | `Xsn4a7TdAeI` | AI with FZ | Claude Desktop Is Now FREE?! Use ALL Claude Models | en/hi | 25:11 | 13K | 2026-07-17 | **Path B** (AntiGravity/Kiro OAuth) — the FALSE "free Claude" claim |
| t7 | `4DlNb2weD_s` | NetworkCoder | Claude Desktop Without Anthropic (AI Gateway Basics) | hi | 27:53 | 18K | 2026-06-05 | **Bifrost, not OmniRoute** — most honest ("not Claude Opus") |

> Note: **t7 covers Bifrost**, a sibling gateway, not OmniRoute — included for the shared "route Claude Desktop → free model" mechanism and its unusual candor.

## Dropped by the selection rubric
- `uEGOAjYA7yM`, `0Pao0_xNDIk`, `C1bVD2mAGLk` — 30–35s Shorts.
- `WdfXy5hf0VA` (Decoded AI, Korean) — 11 views / 260 subs.
- `PkC03I5fKak` (Julian Goldie SEO, "Claude Code is FREE Forever") — 145 views; noted as evidence of the claim's viral spread, not authority.
- `LOrjVQnA4EY` (NetworkCoder, Bifrost) — same channel as t7 (diversity cap).

## Independent ground-truth (main-loop, not agent-asserted)
- **GitHub API:** [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) (★20,322, MIT, TS, 257 contributors), [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) (★43,679, Go, MIT).
- **OmniRoute docs:** `FREE_TIERS.md`, `COMPRESSION_GUIDE.md`, `PROVIDER_REFERENCE.md`, `ENVIRONMENT.md`, README Acknowledgments; GitHub issue #7387, discussion #2651.
- **Anthropic ToS / OAuth ban:** The Register, VentureBeat, MLQ, engineerscodex, KERSAI, autonomee (Jan/Feb 2026 enforcement vs OpenClaw/OpenCode/Roo/Goose).
- **AntiGravity Claude removal** + **Kiro proxy prohibition:** WebSearch (AntiGravity docs/Medium; Kiro FAQ/AWS Service Terms).

## Verification workflow
- `wf_e3d4a558-e70` — 23 agents (7 digest + 14 refute-first cluster verifiers + synthesizer + completeness critic), ~1.42M tokens, 226 tool calls, 419s, 0 errors, 2 empty (re-done main-loop). All agents Haiku 4.5; load-bearing facts re-verified on Opus. See [[caveats-and-corrections]].

## Corpus context
- **NEW topic — #70** in the autopilot-research corpus (69 existing; independently collision-checked). No prior OmniRoute/CLIProxy topic here (`omnilogin-ai-coding` is unrelated OmniLogin).
- Cross-links: [[harness-engineering/personal-repo-router-multimodel]] (operator's own multi-model router pilot) · [[hermes-agent/_index]] (t69, prior "personal agent" hype-verification) · [[local-ai-coding-agents/_index]] (the local/private alternative to upstream routing) · [[claude-api-cost-optimization/_index]] · [[cowork-third-party-inference/_index]] (Claude Desktop third-party-inference feature).

## Key Takeaways
- 7-video promotional bundle (VN/EN/Hindi, 7 channels); **t3 most balanced, t6 the FALSE claim, t7 = Bifrost not OmniRoute**.
- All load-bearing facts grounded in **GitHub API + primary docs + independent WebSearch**, not agent assertion.
- Related: [[claims-scorecard]] · [[caveats-and-corrections]] · [[overview]]
