# Caveats & corrections (Rule 12 fail-loud)

## Source
- Raw records: `raw/2026-07-04-hoidanit-fullstack-vibe-coding.md` (ep-4 anchor) + `raw/2026-07-04-hoidanit-ep3-mvp-frontend.md` (ep-3 full treatment) · verify workflows `wf_b1314fa6-590` + `wf_f3c7237f-4c4` · deepen/review `wf_8bf5253d-aa2` — full chain in [[source-provenance]]

## ⚠️ OVERTURNED by the ep-3 full treatment (2026-07-04) — discards that were wrong
1. **"Vite possibly acquired by Cloudflare — garble-grade, DISCARDED, do not quote"** (below, deepening-pass flags) — **OVERTURNED: TRUE.** Cloudflare acquired VoidZero (Evan You's company behind Vite) on **2026-06-04**, 18 days before the ep-3 live; the vite.dev banner Eric noticed is real ("Cloudflare supports Vite's mission"); $1M Vite ecosystem fund; team joins Cloudflare ETI. Primary: Cloudflare press release + voidzero.dev post + blog.cloudflare.com. **Meta-lesson: a secondary digest downgraded a TRUE fresh-news claim to garble — "discard-as-garble" is itself a misfire class; date-sensitive claims deserve a search before discarding.**
2. **"Vite 81K stars — plausible magnitude, NOT verified, do not quote"** — now verified: **81,727★** (GitHub API, 2026-07-04). The caption number was accurate.
3. **"Livestream day treated as unconfirmed"** — RESOLVED: ep-3 transcript says "Hôm nay là thứ hai" (today is Monday) + "đăng vào thứ tư hàng tuần" (VOD Wednesdays) + closes "hẹn gặp lại tối thứ hai tuần sau"; calendar check: 2026-06-22 = Monday, all four VOD dates = Wednesdays. **Live = Monday 19:30 (the doc was right); VOD = Wednesday.** The ep-1/ep-4 digest "Tue/Thu" day-claims were caption artifacts.

## Ep-3 corrections & precision notes (wf_f3c7237f-4c4)
- **Tailwind economics understated, not wrong:** his story (downloads ↑ since ChatGPT, maintainer revenue "gần như không có", debate about the future) has a real primary source — Adam Wathan, Jan 2026: *"Tailwind is growing faster than it ever has... and our revenue is down close to 80%"* + **75% of engineering laid off** + docs traffic −40% since early 2023. Reality is a *collapse from ~$2M+/yr*, not perpetual-poverty; direction right, shape imprecise.
- **"Vite 8 needs minimum Node 22"** — simplification: engines = `^20.19.0 || >=22.12.0` (Node 20.19+ also works). Course pins Node 24, so no practical impact.
- **React Compiler "React 19+ has it"** — simplification: stable Oct 2025, defaults to React 19, but supports 17/18 with explicit config.
- **"shadcn/Chakra pull in Tailwind"** — half right: shadcn/ui REQUIRES Tailwind ✅; **Chakra does not** (Emotion CSS-in-JS); AntD does not (own CSS-in-JS).
- **create-vite menu**: React Router v7 / TanStack / RedwoodSDK are real MENU entries but `customCommand` hand-offs to external CLIs, not built-in templates; `react-compiler-ts` ("TypeScript + React Compiler") is literally the 2nd React variant — matches his pick.
- **Magento "~100–200+ tables"** — understated for modern versions: Magento 2.4.3 = 411 tables (mage2db.com); his figure fits the older era of his job. Anti-panic point stands.
- **ncu "version 21"** (caption) — latest is 22.2.9; behavior claims (list vs `-u` rewrite-only vs separate install) all verified exact.
- **Node 24.14.0 (doc) vs 24.16.0 (on-screen)** — both real releases (2026-02-24 / 2026-05-21); doc pinned earlier patch, site showed newer LTS patch on live day; no conflict, doc wins for the cohort.
- **Template drift warning:** the current create-vite react-ts template ships **oxlint** and no typescript-eslint (verified 2026-07-04); the video's 8.59→8.61 ncu row matches typescript-eslint's registry timeline (8.61.0 = 2026-06-08; 8.62.0 landed hours after the live). A fresh scaffold today won't reproduce the video's dependency list.
- **Copilot "$15" reprise:** ep-3 caption ~00:05:37 repeats "rẻ rẻ khoảng 15 đô" about an AI tool (garbled name "gilus") — segment caption-unreliable; the $15-as-price refutation from the ep-4 ship stands (Pro = $10/mo). Ep-3 does confirm he *pays for Claude Code ("dùng nhiều nhất") + ChatGPT/Codex* and was only then buying the third tool.
- **Verifier/dive misfires this pass (main-loop overrides):** (a) one dive declared lightningcss absent from vite@8 deps — registry shows `lightningcss ^1.32.0` present (WebFetch-summarizer miss; 3-source override); (b) the node-releases dive called Node 26 "odd-numbered" (it's even; Current in June 2026, LTS due ~Oct 2026) and mis-phased Node 24 as "Maintenance LTS" (it's Active LTS until ~Oct 2026 per the policy it itself quoted); (c) the critic suggested re-verifying Copilot pricing (already ground-truthed in the ep-4 ship) and referenced a "npm-security-check plugin claim (video intro)" that exists nowhere in the video — critic noise, ignored.

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
- **Caption-derived popularity numbers** (ep 2/3: "React 246K stars", "Vite 81K stars", "Vue ~53K") — plausible magnitudes, NOT verified at digest time. ~~do not quote~~ → **Vite 81K verified TRUE (81,727★) in the ep-3 full treatment**; React/Vue figures remain unverified.
- ~~**"Vite possibly acquired by Cloudflare"** (ep-3 digest aside) — garble-grade... DISCARDED, do not quote.~~ → **OVERTURNED 2026-07-04: the acquisition is REAL (Cloudflare acquired VoidZero 2026-06-04).** See the overturned-discard ledger at the top of this file.
- The series-scope "~20–50 videos vs prior ~100-video series" is caption-derived (~3:26) — kept with approximate flag only.

## Known verifier-misfire notes (for the corpus misfire ledger)
- The 'series' verifier returned REFUTED **on the title-language attribute only** while confirming the substantive items (course URL; video-1 identity) — the playlist composition itself was already primary-source-verified in the main loop via yt-dlp. Pattern: refute-on-secondary-attribute while primary claim stands; main-loop override applied (cf. the recurring wiki-verify misfire ledger in [[source-provenance]]).
- A TS verifier dated TypeScript 5.9.3 to "Oct 1, 2024" — the 5.9 line is 2025; existence verdict stands, date discarded.

## Key Takeaways
- One genuine content correction (Copilot price) in an otherwise verification-clean beginner source — noteworthy in itself.
- Auto-caption ASR on Vietnamese technical content reliably garbles tool names + version numbers; anything numeric from captions needs a second source before quoting.
- Competitor blogs are not neutral ground truth for "standard tool" claims — downgrade, don't adopt.
