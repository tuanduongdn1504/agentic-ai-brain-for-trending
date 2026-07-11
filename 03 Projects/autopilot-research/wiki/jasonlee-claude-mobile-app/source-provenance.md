# Source Provenance — Channel Forensics and the Funnel

## The channel
- **@jasonleefinance** (channel ID `UCSm7riYU-NTWWFlG9XJBcRA`), 189K subs at ingest. The handle's "finance" suffix records the channel's genealogy: launched 2023-04-27 as a creator/money channel (monetized within a month), now a make-money-with-AI content operation.
- **Jason Lee is a content creator, not (verifiably) an app operator**: Creator Academy course self-reports ~$26K/mo from AdSense + courses + sponsorships + affiliates; The Breadcrumb newsletter (19K+ readers, startup ideas); no App Store developer page or shipped app found under his identity (searched 2026-07-11; "Jason Lee Limited" is an unrelated developer).
- This is the corpus' first entry from the **revenue-titled vibe-coding tutorial** genre — adjacent to but distinct from the educator cohort ([[external|Storm Bear: hoidanit-fullstack-vibe-coding]], [[external|Storm Bear: jsm-practical-vibe-coding]]): the educators sell pedagogy; this genre sells opportunity.

## The title formula (channel sweep, 2026-07-11)
Recent uploads show the systematic pattern — the dollar figure is always the *target niche's estimated* revenue:
- `UMjeSU6C4qU` "How I built an **$80K/Mo** mobile app..." (2026-07-09) — this topic
- `hDOUzlJwM1E` "How I Vibe Coded a **$400K/mo** App..." (2026-04-24, 293K views) — subject app CoinSnap is owned by Next Vision Limited (HK)
- `Z6C4CY2rLp4` "How I Vibe Coded a **$900K** App in 13 Minutes (Claude Design + Codex)"
- `kU-DqrT-C50` "I sat on my couch and built a **$100K** app (without coding)"
- `sw-OPsJEgac` "I discovered a rare product that makes **$21,000/month**"

## Key sibling videos (dated via yt-dlp, main loop)
| Video | Date | Views | Relevance |
|---|---|---|---|
| `ThKDUQCq50I` "7 Tiny Apps Making at Least $40,000/month (Vibe coding)" | 2026-06-18 | 49K | The declared idea-source for this video; same no-source revenue numbers; kit.com "20 Tiny Apps" lead magnet |
| `jQOSIPgGqY0` "Anthropic just dropped Claude Design 2.0 (MASSIVE Upgrades)" | 2026-06-30 | 27K | His coverage of the verified 2026-06-17 Claude Design overhaul → [[claude-design-handoff]] |
| `f8XargL0g2A` "I Tested Claude Fable 5 to Build Apps: Surprising Results" | 2026-06-11 | 92K | Confirms his "I made a video about it when it came out" line |
| `jQO9RAmy5lk` "Claude + Seedance 2.0: Creates Viral UGC Videos on Autopilot" | 2026-05-01 | 146K | Resolves the "Cidas 2.0" caption garble; prior Arcads-adjacent content |
| `c-rz9tLBuRQ` "Hermes Agent Tutorial: Beginner to Pro in 15 Mins" | — | — | Cohort overlap: Hermes is already in the corpus as [[external|Storm Bear: harness-engineering]]'s hermes-orchestrator sibling |

## The funnel (per-video monetization surface)
1. Sponsor read + affiliate link ("Best Deal on Arcads": go.heyjasonlee.com/arcads)
2. Lead magnet (heyjasonle.kit.com/arcadsprompts — the UGC prompts; note the typo'd kit handle "heyjasonle")
3. Newsletter (thebreadcrumb.co)
4. Course (Creator Academy — teaching YouTube monetization, i.e., the channel itself is the product)
5. End-screen funnel to the next ideas video

Reading: the video's economics run on attention, not on Track Rabbit. That doesn't invalidate the tooling content — it explains why the demo optimizes for visible progress over shippable completeness ([[expo-go-to-app-store-gap]]).

## Ingest record
- Path 5 (yt-dlp only): `--dump-json` metadata + EN auto-captions → dedupe → ~29.8K-char transcript, **read in full in the main loop**; description + timestamps preserved in `raw/2026-07-11-jasonlee-claude-mobile-app.md`. No NotebookLM. Channel/sibling forensics via `yt-dlp --flat-playlist` in the main loop (subagents commonly hit YouTube bot-checks).
- Double-dive + verification: Workflow `wf_8eed8f7a-008` — inventory row and [[caveats-and-corrections]] carry the full process ledger.

## Key Takeaways
- Provenance grade: **first-party demonstration** of a real workflow, wrapped in **third-party (estimated) revenue claims** — trust the screen recording, not the thumbnail.
- The channel is a useful *tool-news radar* (Claude Design 2.0, Fable 5, Seedance) with consistent title inflation — ingest with the scorecard from [[caveats-and-corrections]] as the default prior.
