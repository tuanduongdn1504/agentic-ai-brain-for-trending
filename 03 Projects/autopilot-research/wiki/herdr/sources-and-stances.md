# Sources & stances

> 6 YouTube transcripts + primary docs. Full manifest: `raw/2026-07-18-herdr/_sources.md`.

## Video sources (6 ingested)

| # | Channel | Stance | Views | Uploaded | Bias note |
|---|---|---|---|---|---|
| 1 ⚓ | **Chase AI** (anchor) | Promotional walkthrough | 20.6K | 2026-07-16 | ⚠️ **Promotional** — skool.com "build your agency / land your first client" upsell. Already a known channel in the corpus (claude-code-plugins-stack). Its claims map closely to ground truth but carry the "free" + "Windows" over-simplifications. |
| 2 | **DevOps Toolbox** | Technical / semi-critical | 92.8K | 2026-07-03 | Most independent/technical of the six; frames Herdr as a "tmux rewrite." Highest views. |
| 3 | **Seth Phaeno** | In-depth walkthrough | 76.3K | 2026-06-24 | Positions Herdr as tmux-inspired-plus-features. |
| 4 | **Hal Shin** | Positioning | 63.4K | 2026-05-17 | Origin of the "the Tmux for AI Agents" framing. Earliest source (state may lag current version). |
| 5 | **Academind** (Max Schwarzmüller) | Credible educator | 11.6K | 2026-07-16 | Established teaching channel; careful definitions. |
| 6 | **Elie Steinbock** | Practitioner + pro tips | 3.5K | 2026-07-14 | Frames Herdr among Conductor/cmux peers; hands-on tips. |

**Bias spread:** 1 promotional anchor + 5 independent, incl. 1 technical-critical (t2) and 1 credible educator (t5). Errors originated in promotional/casual framing (anchor + tmux comparisons), not in the technical sources — a healthy cross-source spread. Total ~16.8K words, read in full.

## Dropped (YouTube 429 bot-gate)

| Channel | Stance | Why dropped |
|---|---|---|
| Better Stack | Questioning ("ultimate multiplexer?") | 429 after 6 fetches; questioning angle partly covered by t2. |
| Fru Dev | Comparison (Tmux/Cmux/Herdr/Paneflow) | 429; comparison angle covered by [[competitive-landscape]] + primary docs. |

See [[caveats-and-corrections]] § fetch-block and `output/bypass-attempts.md`.

## Primary sources (ground truth)

- **GitHub API** — `api.github.com/repos/ogulcancelik/herdr`: 17,839★ / 1,133 forks / 76 open issues; created 2026-03-27; v0.7.4 (2026-07-15); Rust; active 2026-07-18.
- **Repo README / LICENSE** — tagline, features, install, **AGPL-3.0-or-later + commercial** dual license.
- **herdr.dev/docs** — `/concepts` (workspace owns tabs+panes), `/agents` (21 agents, zero-config TOML detection), `/session-state`, `/persistence-remote` (SSH `--remote`).
- **Independently re-checked by main loop:** plugin repos `smarzban/herdr-file-viewer` (156★) + `nikok6/herdr-mirror` (35★); issues #198 (closed) + #1514 (open).

## Author
Oğulcan Çelik (`ogulcancelik`) — solo, full-time "in the open"; funded via GitHub Sponsors + gold sponsor Terminal Trove.

## Related
- [[_index]] · [[claims-scorecard]] · [[caveats-and-corrections]]
