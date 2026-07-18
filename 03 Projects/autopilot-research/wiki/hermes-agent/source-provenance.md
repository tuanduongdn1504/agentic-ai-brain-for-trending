# Hermes Agent — Source Provenance

## Method
- **Path 1** `/loop autopilot research <url>` — operator anchor `y96gIckJJ2Q` + operator-elected **full yt-search bundle**.
- **Fetch:** `yt-dlp --cookies-from-browser chrome --write-subs --write-auto-subs` → `bin/vtt-to-md.py` (venv Python 3). **No 429** this run (cookies applied up-front per the [[herdr|herdr]] lesson). ~33.1K words EN + 10.5K VN original. **No NotebookLM** (within direct-read range).
- **Verification:** refute-first workflow **`wf_06a79485-687`** — 8 gatherers → 22 merged claims → refute-first verifiers (3-skeptic panels on 6 hype claims) → 2 critics. 44 agents, 0 errors, ~1.83M tokens, 209 tool calls, ~4.6 min.
- **Primary grounding (main loop):** GitHub API ×2 endpoints, official README, [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com) + `/docs/`.
- Full manifest: `raw/2026-07-18-hermes-agent/_sources.md`.

## The 8 sources
| # | Channel | Views | Len | Uploaded | Stance | Notes |
|---|---------|-------|-----|----------|--------|-------|
| 1 ⚓ | Phan Dong Giang - Learn AI (VN) | 4,022 | 39:29 | 2026-07-16 | **promotional** | Operator anchor. No-code A-Z, "Dễ Hơn OpenClaw". EN auto-translation used; VN original retained. |
| 2 | NetworkChuck | 1,321,276 | 32:39 | 2026-05-20 | **promotional** | Mega-reach ("goodbye OpenClaw!!"). Source of several unverified stats (every-10-turn fact-check; "built before OpenClaw"; overtook-OpenClaw). |
| 3 | Tech With Tim | 19,739 | 18:28 | 2026-07-02 | **balanced** | Most credible comparison — Hermes-vs-OpenClaw as *complementary*, not replacement. |
| 4 | Sean's AI Stories | 17,384 | 20:55 | 2026-07-05 | **balanced+caveats** | Recurring corpus creator ([[agent-memory-architecture]]). Source of the **skill-maturity contradiction** + the live cron bug. |
| 5 | Tonbi's AI Garage | 28,879 | 34:20 | 2026-05-18 | **technical-neutral** | Deep memory/Honcho/plugins masterclass; pluggable memory providers (Memo/Hindsight/Supermemory). |
| 6 | Elestio | 5,408 | 11:48 | 2026-05-08 | **promotional** | Hosting-vendor features framing. |
| 7 | Plastic Labs | 5,258 | 1:50 | 2026-03-16 | **first-party-adjacent** | Earliest source; Plastic Labs MAKES Honcho. Authoritative-but-thin on dialectic user modeling (unsupported superlative flagged). |
| 8 | AI LABS | 36,599 | 13:41 | 2026-06-06 | **promotional** | The Claude-Code-interop mechanics (MCP both ways); "greedy Dario" pricing claim; "90 skills default"; Skill Hub security-scan. |

## Stance balance
- **5 promotional / 2 balanced / 1 first-party-adjacent.** The two balanced sources (Tech With Tim, Sean's AI Stories) carried the most corrective weight — the complementary-positioning and the skill-maturity contradiction both came from them. The refute-first panels were what caught the promotional superlatives regardless of stance.
- **Mega-reach skew:** NetworkChuck (1.3M views) dominates attention but was among the most hype-laden — its unique claims are the ones most flagged UNVERIFIED. Reach ≠ reliability.

## Key Takeaways
- **Clean run:** 0 verifier misfires flagged, 0 fabrications; the one internal split (H5 release date) resolved by direct primary check.
- The bundle's **stance diversity did its job** — balanced sources supplied the corrections, panels caught the hype, primary sources settled the numbers.
- Cross-links: [[claims-scorecard]], [[caveats-and-corrections]], [[overview]].
