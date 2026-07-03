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

## Honesty inventory
- Transcript is Vietnamese ASR: tool names/version numbers systematically garbled; every number quoted in this topic was re-verified outside the captions or explicitly flagged ([[caveats-and-corrections]]).
- Videos #1–#3 were ingested as metadata + doc recap only (transcripts not read) at first compile; series-level claims lean on the doc + #4's recap chapter.
- The "Claude Code on screen" observation is caption-derived (95% digest confidence), not visually confirmed.
- Sub count 74.6K: yt-dlp figure, search-corroborated; not browser-confirmed.

## Key Takeaways
- Beginner-tier source, verification-clean at the technical layer — 1 real correction (Copilot price) across ~12 checked claim clusters.
- The recurring corpus misfire pattern (refute-on-fetch-failure / refute-on-secondary-attribute / competitor-source refutations) appeared 3× here and was caught by the main-loop override discipline — the ledger keeps earning its place.
