# Reusable Method — free a slow nuke with Speed Swap, behind a spread-immunity shell

> **The point of this file:** the Mega Steelix team ([[pokemon-champions-team-building/mega-steelix-speed-swap-team]]) is one instance of a *transferable pattern*. Mr. Browser says it outright — *"does it need to be Steelix? Rotom-Wash? Probably not. You can use any Earthquake-er you like — Garchomp, Mamoswine. Emolga probably needs to stay."* This is the reusable template + the PokéSynergy workflow to build **your own** variants for future cores.

## The pattern in one line

**Take a slow, hard-hitting Pokémon that's normally Trick-Room-only, and instead move it first via Speed Swap — then surround it with partners immune to its spread move so you can spam that spread move for free.**

## The 5 roles (a slot template)

| Role | Job | Fixed or flexible? | Options |
|---|---|---|---|
| **1. The Nuke** | slow, high-damage, ideally a **spread** attacker | **Flexible** | any slow spread/EQ user — **Garchomp, Mamoswine**, other slow Earthquake-ers; or a slow special spread attacker |
| **2. The Speed Engine** | donates Speed via **Speed Swap**; survives to do it | **Fixed = Emolga** | Emolga (Motor Drive → self-accelerates off Electric; Flying → EQ-immune). *This is the piece you keep.* Alakazam also learns Speed Swap but lacks the immunities |
| **3. The Immunity Partner(s)** | be immune to the nuke's spread move; ideally feed the engine | **Flexible** | any **Levitator** (any Rotom, Bronzong, …) for Earthquake immunity; an Electric spread move (Discharge) to trigger Motor Drive |
| **4. The Field Glue** | **Trick Room** (fallback) + **Gravity** (ground Flyers) + ally-move immunity | **Flexible** | any **Telepathy** user (Oranguru) that learns Trick Room/Gravity; Telepathy = immune to partner spread moves |
| **5. (optional) flex/answer** | patch the matchup (e.g. a Rock move vs Charizard, a redirector, a second immunity) | **Flexible** | matchup-dependent |

**The invariant:** whatever the nuke's spread move is (Ground → Earthquake, Electric → Discharge/Earth Power, etc.), **every teammate must be immune to it** (by typing, ability, or Telepathy). That immunity is what makes the spread move worth running — it hits both opponents and none of you.

## Build workflow in PokéSynergy (repeat for any core)

1. **Pick the nuke** and confirm it's slow + hits hard: Team Builder → add it → read the base-stat hexagon (low Spe, high Atk/SpA). If it's fast enough already, this pattern isn't the one you need.
2. **Confirm the enabler:** data-search **"Speed Swap"** → keep **Emolga** as the donor (or verify an alternative carries it). Add Emolga; give it **Motor Drive**.
3. **Choose immunity partners for the nuke's spread move.** Ground nuke → add a **Levitate** mon (data-search "Levitate") + Emolga's Flying already covers it. Make sure *all four* are immune (typing / Levitate / Motor Drive / Telepathy).
4. **Add the glue:** a **Telepathy** mon with **Trick Room** + **Gravity** (Oranguru). Telepathy makes it immune to your own spread moves; Gravity lets the Ground nuke hit Flyers; Trick Room is the fallback speed mode.
5. **Set spreads:** nuke = max offense, **min Speed**; Emolga = **max Speed** (donor); glue = bulk + min Speed. Use the **Speed tab** to confirm what the nuke outspeeds once it inherits Emolga's Speed.
6. **Verify the payoff in Calcs:** run the nuke's **spread move under Gravity** vs the meta's relevant Flyers/threats and confirm the KOs; confirm your spread moves do **0** to your own partners.
7. **Check coverage in Analysis:** type gaps, threat list, whether the immunity shell holds. Iterate.
8. **Export** the finished list (Showdown format) and save it.

## Checklist / pitfalls

- ☑ **Every teammate immune to the nuke's spread move?** If one isn't, either swap it or don't run the spread move.
- ⚠️ **Gravity grounds your own floaters** (Flying/Levitate) — while Gravity is up, they're no longer immune to Earthquake. Sequence around it.
- ⚠️ **Emolga is frail** (Focus Sash helps) — it must survive one turn to Speed Swap. Protect the turn you set up, or paralyze first (Nuzzle).
- ⚠️ **This is off-meta** — PokéSynergy's "Top Teammates" suggestions are usage-based and will point you at the *standard* partners for your nuke, **not** this gimmick shell. Build it deliberately; don't expect the tool to suggest it.
- ☑ **Have a no-Gravity answer** to your worst matchup (e.g. a Rock move for Charizard) so you're not forced into Gravity every game.

## Key Takeaways

- **One transferable template:** slow nuke + Emolga (Speed Swap engine, *fixed*) + immunity partners + Telepathy/Trick-Room/Gravity glue.
- **The immunity shell is the enabler** — it's what makes a spread move (Earthquake/Discharge) run for free.
- **PokéSynergy is the build/verify loop:** data-search the enabler → Speed tab for the swap target → Calcs for the Gravity payoff → Analysis for coverage → Export.
- Worked instance: [[pokemon-champions-team-building/mega-steelix-speed-swap-team]]. Swap Steelix for Garchomp/Mamoswine to make your own.
