# Sources & stances

> 6 YouTube transcripts + primary docs. Full manifest: `raw/2026-07-18-herdr/_sources.md`.

## Video sources (8 ingested)

| # | Channel | Stance | Views | Uploaded | Bias note |
|---|---|---|---|---|---|
| 1 ⚓ | **Chase AI** (anchor) | Promotional walkthrough | 20.6K | 2026-07-16 | ⚠️ **Promotional** — skool.com "build your agency / land your first client" upsell. Already a known channel in the corpus (claude-code-plugins-stack). Its claims map closely to ground truth but carry the "free" + "Windows" over-simplifications. |
| 2 | **DevOps Toolbox** | Technical / semi-critical | 92.8K | 2026-07-03 | Most independent/technical; frames Herdr as a "tmux rewrite." Highest views. |
| 3 | **Seth Phaeno** | In-depth walkthrough | 76.3K | 2026-06-24 | Positions Herdr as tmux-inspired-plus-features. |
| 4 | **Hal Shin** | Positioning | 63.4K | 2026-05-17 | Origin of the "the Tmux for AI Agents" framing. Earliest source (state may lag current version). |
| 5 | **Academind** (Max Schwarzmüller) | Credible educator | 11.6K | 2026-07-16 | Established teaching channel; careful definitions. |
| 6 | **Elie Steinbock** | Practitioner + pro tips | 3.5K | 2026-07-14 | Frames Herdr among Conductor/cmux peers; hands-on tips. |
| 7 | **Better Stack** | Questioning ("ultimate multiplexer?") | 33.4K | 2026-06-05 | Dev-tooling brand; skeptical framing. *Late arrival — folded in via DEEPEN.* |
| 8 | **Fru Dev** | Head-to-head comparison | 2.6K | 2026-05-31 | Compares Herdr to tmux/cmux/Paneflow + others; ranks Herdr highly but leans cmux as daily driver. ⚠️ **Auto-captions garble competitor names** (Emacs/SiMax/armox/Ron Pane) — those treated as unverified. *Late arrival — folded in via DEEPEN.* |

**Bias spread:** 1 promotional anchor + 7 independent, incl. 1 technical-critical (t2), 1 credible educator (t5), 1 questioning brand (t7), and 1 cross-tool comparison (t8). Errors originated in promotional/casual framing (anchor + tmux comparisons), not in the technical sources — a healthy cross-source spread. Total ~22.7K words, read in full.

**Fetch note:** t7/t8 lagged ~90 min behind the YouTube 429 bot-gate and were initially presumed lost; both completed and were added via a DEEPEN pass (workflow `wf_5ffde4c4-627`). See [[caveats-and-corrections]] § fetch-block and `output/bypass-attempts.md`.

## Primary sources (ground truth)

- **GitHub API** — `api.github.com/repos/ogulcancelik/herdr`: 17,839★ / 1,133 forks / 76 open issues; created 2026-03-27; v0.7.4 (2026-07-15); Rust; active 2026-07-18.
- **Repo README / LICENSE** — tagline, features, install, **AGPL-3.0-or-later + commercial** dual license.
- **herdr.dev/docs** — `/concepts` (workspace owns tabs+panes), `/agents` (21 agents, zero-config TOML detection), `/session-state`, `/persistence-remote` (SSH `--remote`).
- **Independently re-checked by main loop:** plugin repos `smarzban/herdr-file-viewer` (156★) + `nikok6/herdr-mirror` (35★); issues #198 (closed) + #1514 (open).

## Author
Oğulcan Çelik (`ogulcancelik`) — solo, full-time "in the open"; funded via GitHub Sponsors + gold sponsor Terminal Trove.

## Related
- [[_index]] · [[claims-scorecard]] · [[caveats-and-corrections]]
