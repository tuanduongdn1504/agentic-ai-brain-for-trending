# Claims Scorecard

*Checkable claims from the video + the tool's framing, with verdicts. Verified via Workflow `wf_038de11d-243` (10 agents) + main-loop anchors (WebFetch of the live site; WebSearch of creator/market).*

**Tally (14 claims): 8 CONFIRMED · 3 CORRECT-BUT-INCOMPLETE · 2 MISLEADING · 0 FALSE · 0 FABRICATED · 1 corrected-agent-confabulation (see [[pokesynergy-niche-business-tool/caveats-and-corrections]]).** A high-integrity source at the *factual* level; the softness is in *framing* (the auto-optimizer pitch), not fabrication.

| # | Claim | Verdict | Note |
|---|---|---|---|
| 1 | PokéSynergy exists and is a live, free team builder | **CONFIRMED** | Direct WebFetch; free, no login, no ads/Patreon |
| 2 | It's for competitive "Pokémon Champions" (VGC 2026 Doubles) | **CONFIRMED** | Site + game both real |
| 3 | Pokémon Champions is a real TPCi game w/ ranked ladder + seasons | **CONFIRMED** | Switch, launched 2026-04-08; official 2026 Worlds software |
| 4 | "Season 4" is current | **CONFIRMED** | Season **M-4**: Jul 7 – Aug 4 2026; entry opened Jul 16 (= upload day) |
| 5 | EV mechanics (252/stat, 510 total; natures ±10%) | **CONFIRMED** | Standard; "shifting points" = reallocating EVs |
| 6 | Breakpoint-driven spread building is standard practice | **CONFIRMED** | Taught in official VGC guides; industry-standard calcs |
| 7 | Jolly, max-Atk/max-Spe Garchomp is a standard set | **CONFIRMED** | ~22% of Garchomp sets; Jolly ~90% |
| 8 | Choice Scarf = +50% Speed; Mega legal in Reg M-A | **CONFIRMED** | Bulbapedia; Reg M-A allows Mega (59 forms, 1/battle) |
| 9 | "Make **incredibly perfect** stat spreads **in seconds** for **any team**" | **CORRECT-BUT-INCOMPLETE** | Math is fast, but "perfect" needs human meta judgment; no single optimal spread; live site frames it as *assisted tuning*, not an auto-solver |
| 10 | The tool's "click a threat → points auto-shift" is a novel feature | **MISLEADING** | EV optimization is commodity (ChampTeamAI/Terresquall/PokeTools/Showdex); an interactive UI twist at best; not marketed as auto-optimization on the live site |
| 11 | "Big Six" is the current archetype | **CORRECT-BUT-INCOMPLETE** | Legacy VGC16 term; current meta uses usage tiers/archetypes — colloquial here |
| 12 | Creator "wants 10K subs, 97% not subscribed" (micro channel) | **MISLEADING** (framing) | An engagement hook; Scoriox is a growth-stage creator with a larger goal — see [[pokesynergy-niche-business-tool/source-provenance]] |
| 13 | Tool is "actively maintained" | **CORRECT-BUT-INCOMPLETE** | "Last update ~Jun 29–30 2026"; cadence unknown; no public repo/roadmap |
| 14 | Built solo by Scoriox; it's his own tool | **CONFIRMED** | Multiple own promo videos; independent fan-made tool |

## The domain fact-check (from `verify:domain`)

All core competitive mechanics the tool relies on **checked out** against primary sources (Bulbapedia, official VGC guides, Pikalytics usage data, Victory Road regulations). No mechanical errors found — the tool does *real* work on *correct* math. The only softness is the **"perfect/seconds/any team" overclaim** (#9) and the **novelty framing** (#10).

## Key Takeaways

- **Factually clean** (0 false, 0 fabricated) — the game, mechanics, market, and tool are all real and accurately described.
- **The two soft spots are framing, not fact:** the auto-optimizer pitch (#9) and novelty (#10). See [[pokesynergy-niche-business-tool/what-it-actually-is-vs-the-pitch]].
- One **agent confabulation was caught and excluded** during verification (a fake verbatim quote) — logged in [[pokesynergy-niche-business-tool/caveats-and-corrections]].
