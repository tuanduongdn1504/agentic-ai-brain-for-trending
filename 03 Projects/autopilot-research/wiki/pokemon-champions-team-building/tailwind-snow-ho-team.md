# Worked Example — Tailwind / Snow Hyper-Offense (the non-Steelix contrast)

> **Built on request** (2026-07-18) from six operator-supplied Pokémon — a deliberate contrast to the slow-nuke Steelix builds: this is a **fast** team. **Validated in PokéSynergy** (all 6 legal; no meta type-gaps; the tool surfaced the refinements below).
> **Why it's here:** it proves the [[pokemon-champions-team-building/reusable-team-building-method|reusable method]] isn't Steelix-specific — the same 5 role-slots hold, but every filling **inverts** (slow→fast). See the contrast table at the end.

## Identity: Snow-backed Tailwind Hyper-Offense

Four fast attackers behind **two speed engines** (Talonflame **Tailwind** + Froslass **Icy Wind**) and a **priority backbone** for when speed control lapses. The mega is **Froslass**, whose ability is **Snow Warning** (verified in PokéSynergy) — so mega-evolving auto-sets **Snow**, which makes **Blizzard 100% accurate** and unlocks **Aurora Veil** (both screens in one move). Team average Speed ≈ **152** (very fast), Attack ≈ **145**.

## The six (PokéSynergy-validated)

| Mon | Ability | Role | Set |
|---|---|---|---|
| **Mega Froslass** | **Snow Warning** | weather + speed control + special breaker | **Aurora Veil** · **Blizzard** · **Icy Wind** · Shadow Ball — Timid, max SpA/Spe, item **Froslassite** |
| **Talonflame** | **Gale Wings** | the speed engine | **Tailwind** · Brave Bird *(priority at full HP)* · Will-O-Wisp · Protect — Jolly, max Atk/Spe, Sharp Beak |
| **Sneasler** | Unburden | lead disruptor | **Fake Out** · Dire Claw · **Close Combat** · Protect — Focus Sash, Jolly |
| **Garchomp** | Rough Skin | fast physical anchor | Dragon Claw · **High Horsepower** · Rock Slide · Protect — Life Orb, Jolly |
| **Kingambit** | **Defiant** | priority + late-game cleaner | Kowtow Cleave · **Sucker Punch** *(priority)* · Iron Head · Protect — Lum Berry, Adamant |
| **Rotom-Wash** | **Levitate** | glue / anti-Charizard | Hydro Pump · Thunderbolt · **Will-O-Wisp** · Protect — Sitrus Berry, bulky |

## Why it works

- **Triple speed layer:** Tailwind (whole team) + Icy Wind (slows *them*) + everyone's already fast → you almost always move first.
- **Priority backbone** (insurance when Tailwind ends): Fake Out (Sneasler) · **Sucker Punch** (Kingambit) · Gale-Wings **Brave Bird** (Talonflame). This is the fast-team analogue of the Steelix team's Choice-Scarf backup.
- **Aurora Veil** (Froslass, in its own snow) is the defensive glue — halving *both* physical and special damage patches an otherwise glass-cannon shell.
- **Defiant Kingambit** turns enemy Intimidate into a +2 Attack gift — your answer to Incineroar/Landorus.
- **Rotom-Wash's Levitate** makes it immune to Garchomp's Ground moves (safe partner) and its Water STAB answers the format's Mega Charizard-Y.

## What the tool flagged (and the fixes)

PokéSynergy's Analysis tab: **type gaps = None** (no glaring meta weakness). Two soft spots:

- **Weak to bulky physical walls** (Kingambit / Incineroar / Sinistcha) → *don't try to out-bulk them*; break with **Close Combat** (Sneasler), Iron Head/Low Kick, and special **Froslass**.
- **Weak to strong special attackers** (Mega Charizard-Y / Sylveon / Mega Venusaur) → **Aurora Veil turn 1** (Froslass) + **Rotom** (burns / answers Charizard). This is exactly why Aurora Veil earns a slot over a 4th attack.

## ⚠️ The Garchomp spread-move caveat (same lesson as the Steelix builds)

Garchomp's **Earthquake would hit your own grounded partners** — Sneasler, Kingambit, *and* Froslass all take it. So run **High Horsepower** (single-target Ground) instead — the identical reasoning the Steelix teams used to pick High Horsepower over Earthquake ([[pokemon-champions-team-building/mega-steelix-sand-trick-room-team]]). Likewise **Rock Slide** clips your own **Talonflame** — only click it when Talonflame isn't beside Garchomp. *(Rotom-Wash's Levitate is your one Earthquake-safe partner if you ever want the spread move.)*

## How to pilot it (this team's "modes" = lead choice, not mega choice)

- **vs fast offense / weather sweepers** → lead **Talonflame + Sneasler** (Tailwind + Fake Out), then overwhelm before they set up.
- **vs strong special / Fairy (Charizard-Y, Sylveon)** → lead **Froslass + Rotom** (Aurora Veil turn 1 + burns) → mitigate, then grind.
- **vs their own Trick Room / slow-bulky** → your worst case: a fast team hates Trick Room. Lean entirely on the **priority backbone** (Sucker Punch / Fake Out / Brave Bird still work under TR), don't overextend fast attackers into a TR turn.

## The contrast — the method generalizes (slow-nuke ↔ fast-HO)

The [[pokemon-champions-team-building/reusable-team-building-method|5-role method]] holds; the *fillings* invert:

| Role slot | Steelix builds (slow-nuke) | This team (fast HO) |
|---|---|---|
| **Win-condition** | one slow nuke (Mega Steelix) | spread fast offense (4 attackers) |
| **Speed engine** | Trick Room / Speed Swap (*be slow*, move first) | **Tailwind** (*be fast*, stay fast) + Icy Wind |
| **Damage enabler** | immunity shell / sand (Sand Force) | **Snow** (Blizzard + Aurora Veil) |
| **Insurance when the engine lapses** | Choice-Scarf backup | **priority backbone** (Fake Out / Sucker Punch / Brave Bird) |
| **Glue** | Sinistcha (TR / heal / redirect) + Rotom | Rotom (burns) + Froslass (Aurora Veil) |
| **Mega** | Steelix *or* Tyranitar | Froslass (snow) |

Same skeleton, opposite metabolism. That's the payload: once you can name the five slots, you can build *any* archetype — you're choosing an engine and a damage-enabler, then letting them dictate the rest.

## Notes

- This team is a **preset in the [Game Plan Assistant](steelix-synergy-guide.html)** — flip the "Piloting" toggle to **❄️ Tailwind · Snow HO** and paste an enemy team to get a plan tuned for *this* team (its worst read is enemy Trick Room; its best is fast weatherless offense).
- **Rotom forme = Rotom-Wash** assumed (best defensive fit + anti-Charizard). Swap if you meant Heat/Mow/Frost/Fan.
- EV spreads are sensible starting points — tune in PokéSynergy; the abilities/moves are the validated part.

## Key Takeaways

- **Fast, not slow:** Tailwind + priority is the opposite engine to the Steelix teams' Trick Room — and the reusable method covers both.
- **Mega Froslass = Snow Warning** → snow → **Blizzard (100%) + Aurora Veil**; that snow is the damage-enabler *and* the defensive patch.
- **Two soft spots** (bulky physical walls; strong special) — break the first with fighting moves, cover the second with Aurora Veil + Rotom.
- **High Horsepower over Earthquake** — the friendly-fire lesson is archetype-independent.

Cross-links: [[pokemon-champions-team-building/reusable-team-building-method]] · [[pokemon-champions-team-building/mega-steelix-wolfey-two-mode-team]] · [[pokemon-champions-team-building/how-to-choose-your-mode]] · [[pokemon-champions-team-building/_index]]
