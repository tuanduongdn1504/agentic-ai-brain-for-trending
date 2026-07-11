# (C) Autopilot Loop — 2026-07-11-13

> **Trigger:** manual (operator-submitted single video: "build knowledge from this video + double deep dive into the original resource + pilot methods")
> **Topic:** jasonlee-claude-mobile-app
> **Started:** 2026-07-11T13:41+07:00
> **Ended:** 2026-07-11T14:25+07:00 (approx)
> **Duration:** ~45m main-loop wall-clock (workflow ~8m inside it)

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 video (transcript in full) + first-party originals via 23-agent workflow | 1 (new topic) | 0 | 1.0 |

## Sources ingested

- `raw/2026-07-11-jasonlee-claude-mobile-app.md` — `UMjeSU6C4qU` Jason Lee (@jasonleefinance, 189K subs) 2026-07-09, ~29.8K-char EN transcript, **read in full in main loop** (path 5, yt-dlp only; broken `python3` shim → brew python3.12; flaky vault shell → output-to-file workaround per memory)
- Double-dive originals (workflow `wf_8eed8f7a-008`, 23 agents = 10 dives + 12 refute-first verifiers + critic; ~1.3M tokens, 670 tool calls): Anthropic model/pricing/design/subagent docs · Supabase MCP/RLS docs · Expo docs · Lottie spec/license · Arcads · App-Store niche ground truth · local corpus cross-link read
- Main-loop ground-checks: channel forensics (`yt-dlp --flat-playlist` — @jasonleefinance handle, title-formula sweep, 5 sibling videos dated), claude-api skill (model lineup/pricing/vision), `gh api` (bugs #44385/#47488 verified real), anthropic.com/news/redeploying-fable-5 fetch, **Fable-5 extension search (garble-guard save)**, Expo docs fetch, Lottie license fetch (403)

## Wiki articles created/updated

- `wiki/jasonlee-claude-mobile-app/` — **NEW topic, 14 files**: _index + overview + video-summary + the-80k-title-and-revenue-claims + workflow-plan-first-design-first + claude-design-handoff + multiagent-cost-tiering-reality + receipt-scanning-with-claude-vision (main-loop takeover article) + supabase-mcp-and-rls + api-key-handling-in-mobile-apps + expo-go-to-app-store-gap + lottie-and-arcads-layer + caveats-and-corrections + source-provenance
- `wiki/_master-index.md` — UPDATED (topic added, 48 topics total)
- `raw/_inventory.md` — row added (raw) then updated (compiled)
- `output/(C) 2026-07-11-jasonlee-mobile-app-pilot-methods.md` — **NEW pilot deliverable** (17 methods A–D tracks + 5-item skip-list + watch-list + 7-day sequence; headline ⭐ A1 CV-parsing spike = receipt-pattern → hireui CV parsing behind Mosh A2 seam)

## Final metric

- `gaps_closed_ratio` = 1.0 (cold-start topic fully compiled)
- Stop reason: target reached (single-source ingest complete; librarian discipline satisfied)

## Verification summary (Rule 12)

- **Scorecard (12 claims): 1 CONFIRMED / 4 CORRECT-BUT-INCOMPLETE / 1 OVERSIMPLIFIED / 6 MISLEADING / 0 fabricated.**
- Agent health: 21/23 done; 2 dive deaths (claude-vision prompt-overflow; expo-pipeline StructuredOutput-cap) + 1 empty verifier (fable5-pricing) — **all 3 closed by main-loop takeovers**.
- **GARBLE-GUARD SAVE:** Fable-5 "as of July 12" claim TRUE (extension after backlash; $10/$50 credits from 07-13) despite the announcement page still reading "July 7" — one mandated search rescued a true claim from refutation by a stale *first-party* page. Logged loudly in caveats-and-corrections; sibling of the Vite×Cloudflare 2026-07-04 overturn.
- Critic dispositions: Lottie-license 403 caveat upheld; Cidas=Seedance resolved via presenter's own video title; bug-number "fabrication" flag overruled by gh-api ground truth; "never ships" softened to absence-of-evidence.
- Main-loop regrade: claim 4 MISLEADING→OVERSIMPLIFIED (Rule 7, documented).

## Top-3 unclosed gaps

1. Lottie Simple License terms single-sourced (site 403) — re-verify when unblocked before commercial reliance.
2. Whether Arcads actually integrates Gemini Omni Flash (sponsor-read claim, unverified either way).
3. #44385 closed-state resolution (fixed vs stale-closed) — gates trust in frontmatter model tiering (pilot C1).

## Suggested next action

Run pilot **A1** (CV-parsing spike, ~1 evening) from `output/(C) 2026-07-11-jasonlee-mobile-app-pilot-methods.md` on an `agent-*` branch in hireui — it converges this topic + miai-cv-matching-agent + mosh-ai-powered-apps into hireui's first LLM artifact. Zero-cost same-day: adopt A4 (screenshot-fix-loop) + write A5 (key-placement ADR).
