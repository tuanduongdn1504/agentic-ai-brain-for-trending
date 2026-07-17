# Caveats & Corrections

*Prime directive: don't repeat the same mistake twice — in either direction. Recording both source-level corrections and our own verification catches.*

## ⚠️ Verification catch — an agent confabulation excluded (Rule 12 / wiki-verify)

- A Workflow agent (`verify:novelty-monetization`) reported that PokéSynergy's `/vs/pokebase` page **explicitly states**: *"No, PokeSynergy does not auto-optimize EVs."*
- **Main-loop re-fetch found no such sentence.** The page simply **does not mention** EV auto-optimization at all; it describes an "edit-check-edit" tuning loop.
- **Action:** the confabulated quote was **excluded** from the wiki. [[pokesynergy-niche-business-tool/what-it-actually-is-vs-the-pitch]] states only the independently confirmed version (the pages make *no auto-optimization claim*). This is the exact "agents confabulate exact quotes / corpus facts" failure mode the vault guards against — caught by re-verifying a consequential claim before use.

## ⚠️ Version-number confabulation stripped (recurrent agent artifact)

- The `analyst:hireui` agent inserted Storm-Bear-style version numbers ("v190–v191", "v192") into its roadmap. The **autopilot wiki does not version topics.** These were **removed** (same artifact caught in [[quanit-becoming-ai-engineer-2026/_index]]). Sequencing in [[pokesynergy-niche-business-tool/hireui-translation]] is phrased as now / next / later.

## Framing corrections (source-level)

- **"Perfect stat spreads in seconds for any team"** → **overclaim / marketing gloss.** The math is fast and the interaction is real, but "perfect" requires human metagame judgment (no single optimal spread; role-dependent), and the live product frames itself as *assisted tuning*, not an autonomous optimizer. (Scorecard #9.)
- **"Novel click-to-solve" feature** → **not novel.** Automated EV optimization is a commodity capability across the ecosystem (ChampTeamAI, Terresquall, PokeTools, Hohou's Home, Showdex). PokéSynergy's real edge is workflow + explainability, not algorithm. (Scorecard #10.)
- **"Big Six"** → legacy VGC16 term; not the current formal archetype label (usage tiers/archetypes dominate now). Colloquial in the video. (Scorecard #11.)
- **"Wants 10K subs, 97% not subscribed"** → an engagement hook, not literal channel status; Scoriox is a growth-stage creator (see confidence notes below).

## Correcting our own earlier ingest doubt

- The raw-file header flagged a possible conflict between the video's **"season 1…4"** and the official **"M-A/M-B regulation sets."** **Resolved / no conflict:** ranked **seasons** are numbered (M-1…M-4); **regulation sets** (M-A/M-B) are a separate axis (which Pokémon are legal). "Season 4" = **Season M-4**, live at upload. (Scorecard #4.)

## Creator-identity confidence levels

- **CONFIRMED (main-loop + strong agent support):** real channel [@Scoriox](https://www.youtube.com/@Scoriox); solo Australian indie creator who vibe-codes gaming tools; PokéSynergy is his own tool; growth-stage.
- **AGENT-SOURCED, NOT independently re-verified (treat as lower-confidence):** the specific ABN (31 525 890 100), email (scorioxyt@gmail.com), X handle (@kingscoriox), RMIT Industrial Design degree, "~6,000 subs as of Aug 2024," and an **Illuvium GameFi** crossover. The completeness critic itself flagged the Illuvium reference as a **possible name-collision**. None of these load-bearing for the topic's payload; cited with this caveat, not asserted as fact.

## ASR / caption garbles (English auto-subs)

The transcript garbles Pokémon/move names; corrected on substance, not spelling — e.g. **"flow it" → Florges**, **"Glim mora" → Glimmora**, **"Catch Out Leaf" → Kowtow Cleave**, **"Arcalidon" → Archaludon**, **"King's Gambit" → Kingambit**, **"Pal Por" → (unresolved; likely Palafin/Palkia)**. These don't affect any conclusion.

## ⚠️ Deepening corrections & overturns (2026-07-17 — branch `autopilot-research-pokesynergy-deepen`)

*A second research pass added live-app testing, an N>1 comparative study, and channel-data analysis. It produced five corrections to earlier articles — logged here per the prime directive (don't repeat a mistake in either direction).*

- **⚠️ OVERTURNED — the Illuvium connection is REAL.** The creator-identity note above flagged "Illuvium GameFi crossover" as low-confidence / *"possibly a name-collision, do not assert."* Direct `yt-dlp` extraction of the [@Scoriox](https://www.youtube.com/@Scoriox) channel shows **dozens of Illuvium videos** (staking/earnings breakdowns, an "Illuvium Revdis Calculator", a "Team Builder Guide"). Scoriox is a **crypto/Web3-gaming creator who pivoted to Pokémon Champions in 2026** — the link is central, not a collision. Upgraded to **high confidence**. (The discard-guard in reverse: a claim we *under*-weighted was true.) → [[pokesynergy-niche-business-tool/distribution-deep-dive]].
- **⚠️ REFINED — the "no auto-optimization" finding overcorrected.** [[pokesynergy-niche-business-tool/what-it-actually-is-vs-the-pitch]] said the product is "assisted tuning, *not* a click-a-threat auto-solver." **Live testing proved clicking a threat DOES auto-configure** (Spe SP 0→31 on tapping Mega Blaziken; rank #435→#204 live). "Click → points shift" is literally true *per breakpoint*; only the *holistic* "perfect spread for any team in seconds" remains an overclaim. → [[pokesynergy-niche-business-tool/live-app-teardown]].
- **⚠️ CORRECTED — Pikalytics is ~9 years old, not "16-yr."** It launched **Nov 21 2017** (Griffin Ledingham; independently verified via Smogon announcement + search) → ~9 years. Fixed in-place in [[pokesynergy-niche-business-tool/what-it-actually-is-vs-the-pitch]] + [[pokesynergy-niche-business-tool/comparative-niche-tools]].
- **⚠️ SELF-CATCH — an agent got a date wrong in THIS pass.** A research agent reported VGC-Team-Sheets' last commit as "May 2019"; the GitHub API shows the last code push was **2021-07-13**. Caught by main-loop verification before publishing — the same Rule-12 discipline applied to our own deepening.
- **NUANCED — "336 views" was the wrong denominator** ([[pokesynergy-niche-business-tool/critical-appraisal]] / [[pokesynergy-niche-business-tool/distribution-deep-dive]]): the subject video was 1 day old; the campaign is ~106K cumulative. Scorecard #12 reclassified MISLEADING→CORRECT-BUT-INCOMPLETE after verifying 8,460 subs.

## Key Takeaways

- **Two agent confabulations caught + excluded** (fake verbatim quote; fabricated version numbers) — verification worked as designed.
- Source is **factually clean**; corrections are about **framing** (auto-optimizer pitch, novelty, "Big Six") and **creator-identity confidence**.
- The "season 4" doubt from ingest is **resolved** — the video was right.
