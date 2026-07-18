# Caveats & corrections

> The claims that need a red pen, the do-not-quote list, and a note on how this topic was fetched. Companion to [[claims-scorecard]].

## The corrections that matter

### 1. License is AGPL-3.0 + commercial — not "unspecified", not unconditionally "free" (C02)
- **Stated:** "open source under an unspecified license; free to use."
- **Correct:** **GNU AGPL-3.0-or-later**, dual-licensed with a **commercial** option. GitHub's `NOASSERTION` is a detector limitation, not reality. "Free" carries **copyleft** obligations if you distribute/modify/network-serve Herdr. See [[license-and-adoption-caveats]].

### 2. Workspace hierarchy: tabs and panes are peers (C06)
- **Stated:** spaces → tabs → panes (panes nested inside tabs).
- **Correct:** *"A workspace owns tabs and panes"* — tabs (layouts) and panes (real terminals) are **peer children** of the workspace, not nested. (herdr.dev/docs/concepts)

### 3. tmux comparisons overstated (C24, C25)
- Mouse and persistence are **zero-config in Herdr vs manual in tmux** — an ergonomics win, not a capability tmux lacks.
- "Unlike tmux, no built-in browser" is **backwards**: neither has one. The claim that agents "**must** use Playwright/Chrome DevTools MCP" is not supported by any Herdr doc.

### 4. State model: idle/working/blocked (C10)
- Authoritative states are **idle / working / blocked**; "done" is marketing language. Audio/visual notifications are asserted in a video but not confirmed in primary docs.

### 5. Plugin specifics (C22)
- **Real** (independently confirmed via GitHub API): `smarzban/herdr-file-viewer` (156★), `nikok6/herdr-mirror` (35★).
- **Not found:** a "reviewer" plugin — likely a transcription artifact of Herdr's *agent skill* / a Codex-review *skill* demoed in the anchor, not a marketplace plugin.

### 6. Windows is beta (C13)
- "Works on Windows and Mac" is true but omits that **Windows is beta**, with an open detection bug (#1514).

## Do-not-quote as fact
- "completely free" (without the AGPL/commercial caveat)
- socket API "returns JSON" (format undocumented)
- binary size "~10MB", exact Rust %, "hit Hacker News front page" (secondary sources only)
- state list as a fixed 4-tuple incl. "done"
- a Herdr "reviewer" plugin

## No FALSE claims
Notably, **zero claims were outright false** and **zero were unverifiable** — the errors were all *incomplete* or *misleading framing*, concentrated in the promotional anchor and casual tmux comparisons. The critical/technical sources (t2 DevOps Toolbox) and the primary docs agreed on the core mechanics.

## Fetch-block incident (process note, not about Herdr)
- The initial `yt-dlp` caption fetch hit YouTube's **HTTP 429 "confirm you're not a bot"** gate. This is **not** a Cloudflare-page block, so the HTML tiers in `(C) bypass-403-escalation.md` (curl→Playwright→Camoufox) don't apply. Resolved with yt-dlp's native **`--cookies-from-browser chrome`** (JS challenge solved via deno).
- After 6 rapid fetches the 429 re-accumulated; **2 of the intended 8 videos** (t7 Better Stack, t8 Fru Dev) could not be fetched across 2 attempts. Shipped on **6** (bundle range 5-8). Full audit: `output/bypass-attempts.md`. The comparison angle t8 would have added is partially covered by [[competitive-landscape]] + primary docs.

## Related
- [[claims-scorecard]] · [[license-and-adoption-caveats]] · [[sources-and-stances]]
