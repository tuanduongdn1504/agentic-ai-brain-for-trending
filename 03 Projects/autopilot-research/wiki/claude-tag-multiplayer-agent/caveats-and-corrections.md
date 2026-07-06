# Caveats & Corrections (Rule 12 — fail loud)

## Verification ledger

Workflow `wf_36db963e-d86` (split run: 10 dives pre-outage ~484K tokens/239 calls; resume added docs+corpus dives, 11/18 verifiers, critic — cumulative ~1.33M tokens/440 calls). **11 machine verdicts returned (5 CONFIRMED / 6 PARTIAL / 0 REFUTED); 7 verifiers died on StructuredOutput schema-compliance and were closed by main-loop takeover** (below). 2 dives + 18 verifiers + critic were killed once mid-run by an account **session-limit outage** (resets 12:10 Asia/Saigon) — recovered via workflow resume with cached dive results; no data loss.

### Machine verdicts (11)

| Verdict | Claim | Note |
|---|---|---|
| CONFIRMED | Launch 2026-06-23, beta, Enterprise+Team, Slack-only | |
| CONFIRMED | Legacy Claude-in-Slack auto-switch 2026-08-03 | |
| CONFIRMED | Boris Cherny = Head of Claude Code; Cat Wu = Head of Product, Claude Code | Cat's remit also includes Cowork |
| CONFIRMED | Private-channel memory isolation, asymmetric (read workspace / write own store) | docs how-it-works |
| CONFIRMED | (memory isolation duplicate angle) | |
| PARTIAL | "50-message context" → actually **20 channel-mention / 50 thread / 100 forwarded** | wiki uses corrected numbers |
| PARTIAL | METR 16h — figure real (Mythos Preview ≥16h, CI 8.5–55h) | see misfire #1 below on attribution |
| PARTIAL | Repo ops — PRs + edits confirmed; "clone/push branches" not documented as independent ops | |
| PARTIAL | Standing instructions — channel-wide store (not per-user), member-editable **unless admin restricts** | |
| PARTIAL | "same Agent SDK" (video) → docs say substrate = **Claude Managed Agents** (hosted), distinct from self-hosted Agent SDK | architecture article corrected |
| PARTIAL | Config-vuln governance claim — CVEs cited are **Claude Code's**, not Tag's; Anthropic's own "How we contain Claude" names **approval fatigue (93% approve-rate)** as a top failure mode | kept out of Tag-specific claims |

### Main-loop takeover closures (7 dead verifiers)

| Claim | Closure |
|---|---|
| 65% PR/code claim | **PLAUSIBLE-UNVERIFIED, self-reported** — pr-65 dive found 3 non-equivalent first-party wordings; no methodology. [[the-65-percent-claim]] |
| Microsoft Teams expansion | **PARTIAL** — named **only in the launch video** (verbatim in official captions read in main loop); written announcement says only "more platforms" |
| Self-scheduling days/weeks/months | **CONFIRMED (feature)** via docs scheduled-operations/standing-instructions; the *months*-scale is video anecdote only |
| Spend enforcement = decline-work | **CONFIRMED, single-source** (announcement dive, first-party) — not independently re-fetched |
| Zenity "runtime control gap" | **Third-party analysis, reported as opinion** — kept in [[security-and-governance]] as analysis, not fact |
| Pricing disclosed? | **CONFIRMED-ABSENCE** — docs publish no per-token/per-task pricing; org spend caps only (set-spend-limit docs) |
| "Can't even accurately detect how long" | **PARTIAL** — fair paraphrase of METR task-suite saturation (5/228 tasks ≥16h), rhetorically inverted. [[metr-16-hour-claim]] |

## Verifier/agent misfires (overridden — recorded per prime directive)

1. **METR verifier called the Boris attribution "unsupported — not in any launch video."** WRONG: the exact words are in the official EN captions of `MhfnicQVkgY` (~02:34), read in full in the main loop pre-workflow. The verifier couldn't fetch the video and mistook fetch-failure for absence. **Legitimate residue:** captions carry no speaker labels, so *which* of the two speakers says it is inferred (context strongly suggests Boris; treat speaker-of-quote as probable-not-certain). Same misfire class as the miai/jsm video-fetch failures — video-content claims need main-loop caption ground-truth, not WebFetch.
2. **Corpus agent claimed "Anthropic violates its own multi-user ToS."** Overreach — Tag runs on dedicated org billing, not plan-auth reuse; see [[corpus-positioning]] §1. Also called the operator's Telegram stack "2 years old" (it was piloted 2026-05-08) and floated **"78% of IT leaders report agentic overages" with no source** — critic caught it; treat as confabulated until sourced. **Do not quote any of the three.**
3. **One verifier graded Tag using Claude Code Channels docs** (`channelsEnabled`, code.claude.com/authentication, WIF) — different product surface; its "correction" about credential scoping mechanisms is recorded but weighted low for Tag specifically.

## Known unknowns (watch-list)

- **GA pricing** after credits expire **2026-09-01**; per-channel spend telemetry in practice.
- **Microsoft Teams** timing (video-only roadmap).
- **Region/data-residency availability** (EU/APAC unaddressed in docs read).
- **Data-training/product-improvement policy for channel memory** specifically (conversations excluded by default per Marketplace; memory-store handling not explicit).
- **Third-party buildability**: can external devs build Tag-class multi-user agents on Managed Agents? (Ties to the harness-economics per-user-credit line.)
- **Prompt-injection mitigations for ambient mode** — absent from docs at ingest; watch for a security page.
- **Post-launch incidents**: none found in the 2-week window (status.claude.com clean for Tag; HN thread 48648039 rate-limited mid-dive) — reaction coverage is thin, re-drain ~2026-08.
- Boris/Cat X-post wordings for the 65% claim were quoted **via search results** (x.com fetches 402'd) — wording verbatimness is one step removed.

## Blocked fetches this pass

VentureBeat (429), TechRepublic (403), TechTimes (403), x.com (402), Reddit (search-blocked), HN item page (429 mid-dive), web.archive.org (tool-blocked), youtube watch pages for agents (bot-gate; captions obtained via main-loop yt-dlp instead). None escalated past Tier 0-1 — nothing here was load-bearing enough to justify the bypass skill; all load-bearing facts closed via first-party pages.
