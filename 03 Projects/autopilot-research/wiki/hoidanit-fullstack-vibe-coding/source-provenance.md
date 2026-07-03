# Source provenance & verification log

## Source
- Raw record: `raw/2026-07-04-hoidanit-fullstack-vibe-coding.md` (video #4 anchor + eps 1–3 deepening digests)

## Ingest chain
| Layer | Artifact | Method | Status |
|---|---|---|---|
| Video #4 | tD0Uve-0Ltk (2026-07-01, 1:33:39) | yt-dlp metadata + VN auto-subs (1.2MB VTT → ~110K-char dedupe; EN track HTTP 429) | read in full (digest agent) |
| Series | playlist PLPTXD_6Mbmh4, videos 1–3 metadata | yt-dlp direct per-video fetch | ✅ primary |
| Course doc | Google Doc 13sSoDBvFItcvH5BPwkeh8IQ8basnd7UgymQZx8maM9U | WebFetch `/mobilebasic` (export?format=txt → 401; block-discipline: switched route, no same-route retry) | ✅ fetched 2× (structure + verbatim pins) |
| NestJS ground truth | docs.nestjs.com (SPA — body not served) → migration-guide via search + nestjs/nest GitHub package.json | WebSearch + raw.githubusercontent | ✅ primary |
| React ground truth | react.dev/learn/creating-a-react-app + registry.npmjs.org/react/latest + react.dev blog | WebFetch | ✅ primary |
| Node ground truth | nodejs.org/download/release/v24.14.0/ | curl HTTP 200 | ✅ primary |
| Instructor identity | hoidanit.vn/about (direct fetch 403) → search snippets + facebook.com/askITwithERIC | WebSearch | ✅ corroborated |
| Copilot pricing | github.com/features/copilot/plans + docs.github.com | verifier WebFetch | ✅ primary |

## Verification
- **Workflow `wf_b1314fa6-590`** — 11 agents (10 refute-first verifiers on pre-registered claims + completeness critic), ~446K subagent tokens, 133 tool calls, ~90s.
- Verdicts: **6 CONFIRMED** (nestjs11, nestcli, react19, playwright, node24*, mysql-ports) · **1 REFUTED-as-claimed** (copilot $15 → $10 correction adopted) · **3 PARTIAL** (eric — student-vs-staff refinement; ts — patch-version unconfirmed; mysql — Workbench "beginner standard" contested by competitor sources) · **1 REFUTED-on-secondary-attribute** (series — title-language; substantive items confirmed; main-loop yt-dlp override on playlist composition).
- *node24 verifier died without structured output (1 of 11); claim already primary-source-verified in main loop (HTTP 200 release dir).
- **Critic's 3 open flags, closed in main loop:** docs-first philosophy = STATED on camera (verbatim [00:13:06] quote, not our inference — though the *label* is ours); Node 24.14.0 = the course doc's own verbatim pin ("Cài chính xác Node.js version 24" + release link); e-commerce-AI-agent = the doc's own declared series project (verbatim VN quote). All three were doc/transcript-grounded before the critic asked.

## Deepening + review pass
- **Workflow `wf_8bf5253d-aa2`** — 6 agents (3 episode-digesters for eps 1–3 with own yt-dlp sub-fetch + 3 reject-first wiki reviewers: facts / links / conventions), ~424K subagent tokens, 122 tool calls.
- Facts lens: caught 1 raw-vs-wiki gap (the "~20–50 videos" scope claim was in the ep-4 digest but omitted from the raw record) — raw + wiki both corrected with caption-derived flags.
- Conventions lens: 2 missing `## Source` sections — fixed.
- **Links lens: all 18 BROKEN_LINK findings were artifacts of a mid-session branch switch** — a concurrent session checked this worktree out from `autopilot-research` to `main` at ~03:05 (reflog: `checkout: moving from autopilot-research to main` + fast-forward merge of `wiki/v193-timesfm`), which removed every sibling topic from the working tree while the reviewers ran. Links re-validated deterministically against the `autopilot-research` branch tree before commit (script; 0 broken). Logged as a NEW review-environment failure mode: **reviewers must pin the git ref they review against.**
- Ep-digest quality: ep-1 digest confabulated "5M+ subscribers" (vs 74.6K ground truth) — discarded; see [[caveats-and-corrections]].

## Misfire ledger (this topic)
1. `verify:series` — REFUTED on an attribute (title language) that was a YouTube auto-translation artifact; playlist composition was main-loop-verified. **Override applied.**
2. `verify:ts` — dated TS 5.9.3 "Oct 1, 2024" (wrong year for the 5.9 line); existence verdict kept, date discarded.
3. `verify:mysql` — "beginner standard" refutation sourced largely from a competitor's blog; downgraded to contested.
4. WebFetch summarizer on docs.nestjs.com returned only the page title (SPA, no SSR body) — routed around via GitHub raw + search; no verdict was based on the empty fetch.

## Ep-3 full treatment (2026-07-04 deepening)
- **Ingest:** VN auto-subs for osISSsyTJJ8 (`--sleep-requests 2`) → 1.13MB VTT → 2,631-line / ~131K-char timestamped transcript — **read in full in the main loop** (not a digest agent). Raw: `raw/2026-07-04-hoidanit-ep3-mvp-frontend.md`.
- **Workflow `wf_f3c7237f-4c4`** — 27 agents (10 original-resource dives + 16 refute-first skeptics [2 lenses × 8 pre-registered high-risk claims] + completeness critic), ~1.09M subagent tokens, 471 tool calls, ~3.6 min.
- **Verdicts:** Vite→Cloudflare acquisition CONFIRMED (press release 2026-06-04 + voidzero.dev + vite.dev banner) · vite 8.0.16-latest-at-live-date CONFIRMED (8.1.0 landed the day after) · react-compiler-ts-as-2nd-variant CONFIRMED (create-vite src) · rolldown+lightningcss deps CONFIRMED (registry; one dive misfired, overridden) · typescript-eslint 8.59/8.61 timeline CONFIRMED · Tailwind economics PARTIAL (real, worse than told: −80% revenue + 75% layoffs Jan 2026) · shadcn-yes/AntD-no/Chakra-no Tailwind matrix CONFIRMED · live-Monday/VOD-Wednesday CONFIRMED (deterministic calendar) · Node v24.14.0+v24.16.0+v26.3.0 all real, npm-11-with-Node-24, even=LTS policy quotes · nvm 94,012★ · nvm-windows (coreybutler) active · ncu behavior exact · npm→GitHub(2020)→Microsoft(2018) chain · MVP lineage Robinson-2001/Ries-2011 · Magento 2.4.3 = 411 tables · COD-VN 60–85% · exactly **4 vibe-coding courses** on hoidanit.vn (ChatGPT&Codex / Claude Code / Claude AI Zero / Antigravity) · "Git Zero" free course page found.
- **Main-loop overrides (misfire ledger additions):** lightningcss-absent dive verdict (WebFetch-summarizer miss; registry override) · Node-26-"odd" parity error + Node-24-"Maintenance-LTS" phase error (both corrected against the policy text the agent itself quoted) · critic's spurious "npm-security-check plugin" reference (nothing in the video) + redundant Copilot-pricing re-check (already ground-truthed in ep-4 pass).
- **Course-doc agent honesty:** this pass's mobilebasic fetch returned AI-processed summary (not verbatim); it confirmed the Node-24 pin + v24.14.0 link + Drive starter + git links; the "Copilot (15$)" and "Mon 19:30" verbatim pins remain sourced from the ep-4 pass's fetches.
- **Notable meta-result:** two prior-ship skeptical discards were OVERTURNED as true (Vite×Cloudflare; Vite-81K stars) — logged in [[caveats-and-corrections]] as the "discard-as-garble" misfire class.

## Honesty inventory
- Transcript is Vietnamese ASR: tool names/version numbers systematically garbled; every number quoted in this topic was re-verified outside the captions or explicitly flagged ([[caveats-and-corrections]]).
- Videos #1–#2 were ingested as metadata + doc recap + digest-grade transcripts; **video #3 upgraded to full first-party treatment 2026-07-04**; series-level claims lean on the doc + #4's recap chapter + #3's full transcript.
- The "Claude Code on screen" observation is caption-derived (95% digest confidence), not visually confirmed.
- Sub count 74.6K: yt-dlp figure, search-corroborated; not browser-confirmed.

## Key Takeaways
- Beginner-tier source, verification-clean at the technical layer — 1 real correction (Copilot price) across ~12 checked claim clusters.
- The recurring corpus misfire pattern (refute-on-fetch-failure / refute-on-secondary-attribute / competitor-source refutations) appeared 3× here and was caught by the main-loop override discipline — the ledger keeps earning its place.
