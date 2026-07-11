# Caveats and Corrections — Verdict Scorecard + Process Ledger

## Verdict scorecard (12 claims)

| # | Claim | Verdict | Confidence |
|---|---|---|---|
| 1 | Title: "How I built an $80K/Mo mobile app" | **MISLEADING** — the figure is a competitor's unverified estimate; presenter is a content creator with no found shipped apps | high |
| 2 | SimplyWise $60K/mo, others $60–80K/mo | **MISLEADING** — unattributed estimates presented as fact; tools carry 5–25% claimed / 55% observed error | high |
| 3 | "As of July 12th you got to use API pricing for Fable 5" | **CONFIRMED** — included-window extended to 2026-07-12; $10/$50 per MTok credits from 07-13 | high (main-loop takeover) |
| 4 | "Opus 4.8 + Sonnet 5 = big upgrade from Sonnet 4.6" | **OVERSIMPLIFIED** — true for Sonnet 5 (direct successor); Opus 4.8 upgrades Opus 4.7, a different line (verifier graded MISLEADING; main loop downgraded per Rule 7 — the natural reading is mostly right) | high |
| 5 | Chat-prompted multi-agent model tiering | **MISLEADING** — capability documented, demo presentational; bugs #44385 (closed) / #47488 (open) verified real | high |
| 6 | ".env keeps your API key safe" | **MISLEADING** — dev-time hygiene only; mobile-bundle extraction is the unaddressed threat; runtime key location never traced | high |
| 7 | Supabase MCP "manages the database for you" | **CORRECT-BUT-INCOMPLETE** — official connector; omits Supabase's dev-only warning, prompt-injection risk, RLS requirement | high |
| 8 | Claude Design "massive upgrade" | **CORRECT-BUT-INCOMPLETE** — 2026-06-17 overhaul real; controls right-side not left; "iOS design" = responsive mockups | high |
| 9 | Lottie "just code, no images" + free commercial use | **CORRECT-BUT-INCOMPLETE** — base64 embedding exists; license permits commercial use, quotes not independently re-verifiable (403) | high / license medium |
| 10 | Arcads "Cidas 2.0 4K + newly released Omni Flash" + MCP | **MISLEADING** — Seedance 2.0 garble; Omni Flash is Google's, not on Arcads' list; MCP connector real | high |
| 11 | B2B sticky + "automatically syncs to QuickBooks" | **MISLEADING** — stickiness unproven for the vertical; QuickBooks = weeks-to-months of deferred OAuth/assessment work | high |
| 12 | Desktop preview + Expo Go QR + shake-reload | **CORRECT-BUT-INCOMPLETE** — pane documented; QR is Expo's; LAN constraint unstated; Fast Refresh automatic | high |

**Totals: 1 CONFIRMED · 4 CORRECT-BUT-INCOMPLETE · 1 OVERSIMPLIFIED · 6 MISLEADING · 0 REFUTED-as-fabricated.** Failure mode: revenue-theater framing + security/production omission. No tool capability was fabricated.

## Process ledger (Rule 12 — fail loud)

- **Workflow `wf_8eed8f7a-008`**: 23 agents, 21 done, ~1.3M tokens, 670 tool calls. Deaths: `dive:claude-vision-receipt` ("Prompt is too long" while loading the claude-api skill — closed by main-loop takeover using the skill directly → [[receipt-scanning-with-claude-vision]]); `dive:expo-pipeline` (StructuredOutput retry cap — closed by main-loop docs fetch + two verifiers' overlapping evidence); `verify:fable5-api-pricing-july12` (completed without StructuredOutput → empty — closed by main-loop takeover below).
- **⚠️ GARBLE-GUARD SAVE (the pass's most important process event):** the Anthropic announcement page (anthropic.com/news/redeploying-fable-5) still says included "through July 7" — a skeptic reading only that page would have REFUTED the video's "as of July 12" claim. The mandated one-search-before-discard found the extension coverage (Android Authority, The New Stack, Forbes, 2026-07-07): Anthropic extended to **July 12 11:59:59 PM PT after backlash**; the announcement was never updated. Same failure shape as the 2026-07-04 Vite×Cloudflare overturned-discard. **Fresh true claims look like errors to a stale-source skeptic — and first-party pages can BE the stale source.**
- **Near-miss on the same fact**: the provenance dive reported "extended through July 12" citing the announcement URL (which doesn't say that); the main loop initially flagged this as a dive misfire, then the search proved the dive's *fact* right even though its *citation* was wrong. Logged as: right-claim/wrong-source — verify the claim, not just the citation.
- **Critic flags, dispositions:** (a) Lottie-license quotes vs 403 — upheld, caveat added; (b) "Cidas=Seedance speculative" — resolved to high confidence via Jason's own Seedance-2.0 video title (`jQO9RAmy5lk`); (c) "bug #44385 not in dive data" — critic misread: verifiers do fresh research; both bug numbers ground-checked real via GitHub API; (d) title verdict's "never ships" overstated — softened to absence-of-evidence phrasing throughout.
- **Main-loop regrade:** claim 4 MISLEADING→OVERSIMPLIFIED (documented in scorecard; Rule 7 pick-one-and-explain).
- **Unresolved / watch:** whether Track Rabbit ever ships (none found as of 2026-07-11); Lottie license page re-check when unblocked; #44385 closed-state resolution (fixed vs stale-closed); whether Arcads actually integrates Omni Flash; Anthropic's promised return of Fable 5 to subscription plans "as capacity allows."

## Key Takeaways
- Verify the claim, not the citation — and never treat a first-party page as automatically fresher than the news about it.
- For this genre (make-money-with-AI tutorials): tool claims verify well; dollar claims never do.
