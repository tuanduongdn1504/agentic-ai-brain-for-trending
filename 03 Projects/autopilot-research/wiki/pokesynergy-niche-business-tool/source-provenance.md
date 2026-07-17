# Source Provenance

## Primary source

- **Video:** [This Tool Solves Pokémon Stat Spreads In Seconds](https://www.youtube.com/watch?v=Vlh3n3WwQZI) — `Vlh3n3WwQZI`, channel **Scoriox** ([@Scoriox](https://www.youtube.com/@Scoriox)), uploaded **2026-07-16**, 11:14, ~336 views, category *Gaming*.
- **Subject:** [PokéSynergy](https://pokesynergy.app) — free Pokémon Champions (VGC 2026 Doubles) team builder. Discord: `discord.gg/88zqNjVnuU`.
- **Ingest path:** 5 (operator-submitted single URL). `yt-dlp` `en-orig` auto-captions → `bin/vtt-to-md.py` → **356 unique cue lines / 25 timestamped paragraphs**; full transcript read in the main loop; `notebook_id: none`. Raw: [`raw/2026-07-17-pokesynergy-niche-business-tool.md`](../../raw/2026-07-17-pokesynergy-niche-business-tool.md).
- **Operator framing:** submitted deliberately, off-corpus-theme, to *"inspire from it and make business tools like this"* → cataloged as a **niche-business-tool archetype**, not Pokémon content.

## Verification

**Workflow `wf_038de11d-243`** ("pokesynergy-verify-analyze") — **10 agents, 0 errors / 0 empty / 0 skipped; ~501K tokens, 143 tool calls, ~5.3 min; all Haiku 4.5.**

- **Investigate (7, parallel):** `dive:product` (live-site anatomy) · `dive:creator` · `dive:landscape` (competitor tools + novelty) · `dive:market` (Pokémon Champions reality + niche size) · `verify:domain` (EV/nature/Choice-Scarf/Mega mechanics, refute-first, schema) · `verify:novelty-monetization` (refute-first, schema) · `verify:ip-risk`.
- **Synthesize (3, parallel, fed investigate digest):** `analyst:playbook` · `analyst:hireui` · `critic:completeness`.
- Script: `…/workflows/scripts/pokesynergy-verify-analyze-wf_038de11d-243.js`; per-agent results in the run's `journal.jsonl`.

**Main-loop independent anchors (Opus, per wiki-verify discipline — verify identity/consequential claims myself):**

- ✅ WebFetch `pokesynergy.app` — product real, free, Next.js, feature suite, explainability-first tagline.
- ✅ WebFetch `pokesynergy.app/vs/pokebase` + `/speed-tiers` — **caught + excluded an agent confabulation** (a fake verbatim "does not auto-optimize EVs" quote); confirmed the pages describe *assisted edit-check-edit tuning*, no auto-optimization claim. See [[pokesynergy-niche-business-tool/caveats-and-corrections]].
- ✅ WebSearch — Scoriox channel identity; Pokémon Champions game + Season M-4 reality.
- ✅ Independent corpus **collision check** (grep of `wiki/_master-index.md` + `raw/_inventory.md`): **no prior Pokémon / gaming / product-archetype topic** → genuinely corpus-first.

## Confidence ledger

| Fact | Confidence | Basis |
|---|---|---|
| Tool real/free/Next.js/feature-set | **High** | main-loop WebFetch + `dive:product` |
| No auto-optimization claim on live site | **High** | main-loop re-fetch (corrected agent quote) |
| Pokémon Champions / Season M-4 / VGC / niche size | **High** | main-loop WebSearch + `dive:market`, multiple sources |
| EV/nature/Choice-Scarf/Mega mechanics | **High** | `verify:domain` vs Bulbapedia/VGC guides/Pikalytics |
| Novelty (EV optimization is commodity) | **High** | `dive:landscape` (named competing tools) |
| Monetization = none/deferred | **High** | site + Terms |
| IP/platform/TAM risk analysis | **Medium-High** | documented enforcement history + niche-size math |
| Scoriox = real solo AU creator, tool is his | **High** | multiple own promo videos + WebSearch |
| ABN / email / @kingscoriox / RMIT / "6K subs Aug 2024" / Illuvium | **Low–Medium** | `dive:creator` only; **not** independently re-verified; Illuvium possibly name-collision |

## Sources (external)

Site: [pokesynergy.app](https://pokesynergy.app) · [/vs/pokebase](https://pokesynergy.app/vs/pokebase) · [/speed-tiers](https://pokesynergy.app/speed-tiers) · [/terms](https://pokesynergy.app/terms).
Creator: [YouTube @Scoriox](https://www.youtube.com/@Scoriox).
Game/market: [Champions gameplay](https://champions.pokemon.com/en-us/gameplay/) · [Play!→Champions transition](https://www.pokemon.com/us/pokemon-news/play-pokemon-competitions-transition-to-pokemon-champions-on-april-and-may-2026) · [ChampsDex ranked](https://champsdex.com/posts/pokemon-champions-ranked-explained-2026/) · [Season M-4](https://www.pokemon.com/us/news/pokemon-champions-july-2026-events-mcs-ranked-battles-season-and-battle-pass) · [LimitlessVGC](https://limitlessvgc.com/).
Mechanics: [Bulbapedia EVs](https://bulbapedia.bulbagarden.net/wiki/Effort_values) · [Choice Scarf](https://bulbapedia.bulbagarden.net/wiki/Choice_Scarf) · [Victory Road regulations](https://victoryroad.pro/champions-regulations/) · [Pikalytics](https://www.pikalytics.com/).
Competitors: [Showdown calc](https://calc.pokemonshowdown.com/) · [ChampTeamAI EV solver](https://www.champteamai.com/ev-calc) · [Terresquall optimiser](https://www.terresquall.com/apps/pokemon-ev-optimiser/).
IP precedent: [Pokémon Showdown (Wikipedia)](https://en.wikipedia.org/wiki/Pok%C3%A9mon_Showdown) · [Prism C&D (Vice)](https://www.vice.com/en/article/nintendo-shuts-down-pokemon-prism-rom-hack-after-eight-years-of-development/).

## Key Takeaways

- **Clean verification run** (10/10 agents) + **main-loop anchors that caught two agent confabulations** before they entered the wiki.
- Confidence is **explicitly ledgered** — product/market/mechanics = high; creator PII details = low-medium and flagged.
- Corpus-first confirmed by an **independent** grep, not an agent's say-so.
