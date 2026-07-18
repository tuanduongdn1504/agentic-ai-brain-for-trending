# License & adoption caveats

## Source
- GitHub API + repo README/LICENSE + issue tracker (verified 2026-07-18). Raw: `raw/2026-07-18-herdr/`.

## License (read this before adopting)

- **DUAL-LICENSED:**
  1. **Open source — GNU AGPL-3.0-or-later.**
  2. **Commercial** — a paid license for organizations that cannot comply with AGPL. Contact `hey@herdr.dev`.
- **The "NOASSERTION" trap:** GitHub's license detector reports `NOASSERTION` / "Other" — **not** because the license is unspecified, but because dual-licensing confuses the detector. The README badge and LICENSE file are explicit: **AGPL-3.0-or-later**. [CORRECT-BUT-INCOMPLETE — C02]
- **"Completely free" is incomplete.** Free under AGPL, yes — but AGPL is **strong copyleft**: if you **modify Herdr and distribute it, or expose a modified Herdr over a network**, you must release your source. For most developers using Herdr **as an unmodified local dev tool, this imposes nothing**. It matters only if you fork/embed/redistribute it or offer it as a network service. [do-not-quote the bare "free" claim without this context]

## Copyleft: what actually triggers it (important for the operator)

- **Using Herdr as a local tool to develop other software → no obligation.** AGPL attaches to *the AGPL'd work itself* (Herdr), not to unrelated software you happen to build while running it. Your hireui codebase is unaffected by running Herdr on your machine.
- **Embedding/linking Herdr's code into a product, or serving a modified Herdr over the network → copyleft triggers.** Don't vendor Herdr source into an AGPL-incompatible product. (Borrow its *ideas* — the socket-API pattern — not its code.) See [[hireui-translation]].

## Maintainer & maturity risk

| Risk | Severity | Detail |
|---|---|---|
| **Solo maintainer** | Medium | One author, **Oğulcan Çelik** (`ogulcancelik`), building full-time "in the open." No corporate backing; funded via GitHub Sponsors + gold sponsor Terminal Trove. Bus-factor 1. |
| **Young + fast-moving** | Medium | Created 2026-03-27 (~3.7 months old at capture), already at **v0.7.4** (2026-07-15) with frequent releases — pre-1.0, API/behavior may churn. |
| **Open bugs** | Medium | **76 open issues** (2026-07-18). Documented **status-detection** bugs — the core feature — e.g. #198 (closed) *"Agent status latches on working and never returns to idle after a turn ends"*; #1514 (open) Windows Claude Code panes get no agent label; plus a cluster (#1441 Pi wrong status, #1243 omp no live status). Actively maintained (pushed 2026-07-18). [CONFIRMED — C29] |
| **Windows beta** | Low | Windows works but is labeled beta; not for Windows-first teams yet. [C13] |
| **Young plugin ecosystem** | Low | Marketplace exists but small/community-maintained. [[supported-agents-and-install]] |

## Do-not-quote list (from verification)

- **"completely free"** — true under AGPL, but omits copyleft + the commercial-license path.
- **State names as a fixed 4-tuple** (idle/working/blocked/done) — sources disagree; authoritative set is idle/working/blocked. [C10]
- **Socket API "returns JSON"** — response format not documented in primary sources. [C21]
- **Binary size ("~10MB"), exact Rust %, "hit HN front page"** — secondary-blog claims, not primary-verified.
- **A "reviewer" plugin** — could not be located; don't cite it. [C22]

## Related
- [[claims-scorecard]] · [[caveats-and-corrections]] · [[hireui-translation]]
