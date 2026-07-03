# Caveats & corrections (Rule 12 fail-loud)

## Source
- Raw record: `raw/2026-07-04-hoidanit-fullstack-vibe-coding.md` · verify workflow `wf_b1314fa6-590` · deepen/review workflow `wf_8bf5253d-aa2` — full chain in [[source-provenance]]

## Corrections (claims that did NOT survive verification)
1. **"Github Copilot (15$)" (course doc, verbatim)** — REFUTED as a price. GitHub's published individual tiers as of 2026-07: **Pro $10/mo** (Pro+ $39, Business $19/user). No individual tier costs $15. Most plausible source of the figure: third-party billing write-ups describe Pro as including **"$15 in AI credits"** under 2026 usage-based billing — a credits *allowance*, not a price (that explanation is third-party, flagged as plausible-not-primary). Treat the doc's number as wrong-or-stale on price.
2. **"Video #1 has an English title"** (early draft observation) — artifact of YouTube **auto-translated titles** in flat-playlist fetches. Direct fetch: "#1. Tôi Vibe Coding Để Tự Động Hóa Công Việc?…" (Vietnamese). Corrected before publish.
3. **"Ex-HUST" phrasing** — Eric is a former HUST *student* (CS), not former staff; wiki wording adjusted.

## Caption-derived items (reported, not fully verifiable from captions)
- **Claude Code as the on-screen error-fixing tool** — captions garble ("Clot Code"); digest confidence 95% (he also sells a Claude Code course — URL verified). Treat as *reported-high-confidence*, pending a visual check.
- **TypeScript-vs-ESLint version numbers around 43:00–52:25 are cross-contaminated** in the auto-captions. Solid: project TS **5.9.3** vs VS Code-bundled TS **6.0.x** (chapter title names the TypeScript mismatch; both versions real — 6.0.3 released 2026-04-16; ESLint's current major is **10**, so caption mentions of "ESLint 10/9/6" can't be cleanly attributed). Exact ESLint versions in this episode: **UNRELIABLE — do not quote.**
- **"VS Code bundled TS 6.0.3" exact patch** — VS Code 1.114 (2026-04-01) release notes confirm "TypeScript 6.0" without patch number; 6.0.3 shipped Apr 16, so *some later* VS Code bundles it; exact on-screen patch unconfirmed.
- **Playwright "63M downloads/week"** — Snyk reports ~62M/wk; the video figure is right within ~1.6%; third-party trackers vary 30–58M by methodology.

## Weaker refutations & context flags
- **MySQL Workbench "standard beginner tool"** — a verifier marked this PARTIAL citing 2026 roundups (Beekeeper/DBeaver recommendations); note the loudest source is a **competitor's own blog**. Workbench remains Oracle-official and current (v8.0.47). Keep as *contested-by-competitor-marketing*, not refuted.
- **Subscriber count 74,600** — yt-dlp + search-snippet corroborated (~74K); still flag: single-method family. Verify in-browser before quoting externally.
- **90/10 SQL-vs-NoSQL** — instructor's experience heuristic, not a measured statistic; wiki quotes it as such.
- **Livestream "Monday 19:30"** — the course doc's own claim (its primary source); upload dates (Tue/Wed) reflect the edited-upload lag, not the live schedule.
- **Antigravity course slug** — catalog course names come from the course doc; the Claude Code course URL was independently verified, the Antigravity slug was not (site 403s direct fetch).

## Deepening-pass flags (eps 1–3 digests, wf_8bf5253d-aa2)
- **Digest-agent confabulation caught:** the ep-1 digest asserted the channel has "5M+ subscribers" — contradicts yt-dlp ground truth (74.6K). DISCARDED; logged as the recurring digest-embellishment class.
- **Livestream-day conflict:** course doc says Monday 19:30; ep-1 digest says Tuesday 19:30; ep-4 digest said Tue+Thu. All caption-derived except the doc. Kept: the doc's own claim, day treated as unconfirmed; uploads land Wednesdays.
- **Caption-derived popularity numbers** (ep 2/3: "React 246K stars", "Vite 81K stars", "Vue ~53K") — plausible magnitudes, NOT verified; do not quote as fact.
- **"Vite possibly acquired by Cloudflare"** (ep-3 digest aside) — garble-grade; the real-world event is VoidZero/Vite funding lore; DISCARDED, do not quote.
- The series-scope "~20–50 videos vs prior ~100-video series" is caption-derived (~3:26) — kept with approximate flag only.

## Known verifier-misfire notes (for the corpus misfire ledger)
- The 'series' verifier returned REFUTED **on the title-language attribute only** while confirming the substantive items (course URL; video-1 identity) — the playlist composition itself was already primary-source-verified in the main loop via yt-dlp. Pattern: refute-on-secondary-attribute while primary claim stands; main-loop override applied (cf. the recurring wiki-verify misfire ledger in [[source-provenance]]).
- A TS verifier dated TypeScript 5.9.3 to "Oct 1, 2024" — the 5.9 line is 2025; existence verdict stands, date discarded.

## Key Takeaways
- One genuine content correction (Copilot price) in an otherwise verification-clean beginner source — noteworthy in itself.
- Auto-caption ASR on Vietnamese technical content reliably garbles tool names + version numbers; anything numeric from captions needs a second source before quoting.
- Competitor blogs are not neutral ground truth for "standard tool" claims — downgrade, don't adopt.
