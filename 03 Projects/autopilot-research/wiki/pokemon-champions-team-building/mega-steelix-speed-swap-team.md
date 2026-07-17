# Worked Example — the Speed-Swap Mega Steelix team

> **Source:** [Pokemon Champions: Mega Steelix Doesn't Need Trick Room to Move First...](https://www.youtube.com/watch?v=EC2A3WrWWtQ) — `EC2A3WrWWtQ`, **Mr. Browser**, 2026-05-17, 3:22, ~465 views.
> **Verified** in [PokéSynergy](https://pokesynergy.app) (roster/stats/movepool) + WebSearch (mechanics). This is a real, legal Champions build.

## The problem it solves

**Mega Steelix** is a wall that also hits like a truck (in PokéSynergy: **Def 250**, Atk 145, HP 150) — but its Speed is **30** (base), the lowest tier in the format. Conventionally that means **Trick Room only**: you reverse the speed order for 5 turns, Steelix cleans up, then TR ends and Steelix is dead weight ("Tailwind does nothing for it," and once it can't move first it just faints). The video's thesis: *endgames are won by who moves first and most often* — so give Steelix speed **without** the 5-turn TR clock.

## The solution: Speed Swap

**Emolga** carries **Speed Swap** (a move that trades its Speed stat with the target's). Emolga runs **Motor Drive** (its Hidden Ability — Emolga is the *only* Pokémon that gets Motor Drive as an HA), which **raises Emolga's Speed every time it's hit by an Electric move**. So Emolga soaks an Electric hit → gets fast → **Speed Swaps its high Speed onto Steelix** → Steelix moves first, indefinitely, no Trick Room needed. Because Emolga is **Flying**, it's also immune to Steelix's Earthquake — perfect partner.

> ✅ **Verified:** Emolga legally learns Speed Swap (egg move) and has Motor Drive as its Hidden Ability; the Motor-Drive + Speed-Swap Emolga has real Champions tournament usage. Mega Steelix exists in Champions (usage rank ~#104), item **Steelixite**, Mega ability **Sand Force**.

## The team (4 named; a Doubles bring-4)

| Mon | Type | Ability | Role | Key moves |
|---|---|---|---|---|
| **Mega Steelix** | Ground/Steel | Sand Force | The nuke | **Earthquake** (spread) + Steel STAB + Protect |
| **Emolga** | Electric/Flying | **Motor Drive** | The engine (*fixed piece*) | **Speed Swap**, Helping Hand, Nuzzle (paralysis), Electric move |
| **Rotom-Wash** | Electric/Water | **Levitate** | Safe spread + feeds Emolga | **Discharge** (spread Electric → triggers Emolga's Motor Drive), Water STAB, Thunder Wave |
| **Oranguru** | Normal/Psychic | **Telepathy** | The glue | **Trick Room**, **Gravity**, support (Instruct/Helping Hand), Protect |

## The synergy engine — double-immunity spread spam

Earthquake (Steelix) and Discharge (Rotom-Wash) are both **spread moves**, and the whole team is **immune to both**:

- **Earthquake** hits everything grounded → but Emolga (**Flying**), Rotom-Wash (**Levitate**), and Oranguru (**Telepathy** — ignores allies' moves) all take **zero**.
- **Discharge** hits everything → Emolga **absorbs it** (Motor Drive: immune + Speed boost), Oranguru ignores it (Telepathy), and it triggers the speed engine on purpose.

So the team fires two spread moves a turn, piling damage on **both** opponents while taking none itself — that's the "immunity abuse + spread pressure + positioning" the description names.

> 💡 **Why this matters (a PokéSynergy insight):** on Steelix, **Earthquake sits at only ~35% usage** vs **High Horsepower at ~50%** — because most teams *can't* run a spread Ground move without nuking their own partner, so they settle for the single-target High Horsepower. **The immunity shell is exactly what buys back Earthquake.** That's the whole point of the build.

## Two speed modes (the build is robust)

1. **Speed Swap mode (primary, no clock):** Emolga → Motor Drive up → Speed Swap onto Steelix. Steelix is fast for the rest of the game.
2. **Trick Room + Gravity mode (fallback):** Oranguru sets **Trick Room** (slow Steelix now moves first) **and Gravity**. **Gravity drops Flying-types out of the sky for 5 turns**, so Steelix's Earthquake now hits the format's big Flyers — Talonflame, Skarmory, Corviknight, the Rotoms, Charizards — *all of which are weak to Ground.*

> ⚠️ **The Gravity double-edge:** Gravity also grounds **your own** Emolga and Rotom-Wash, so while it's up they're no longer Earthquake-immune. Sequence carefully (don't Gravity + Earthquake into your own floaters). And Charizard-Y under Gravity still resists Ground? No — it's weak; but if you'd rather not commit Gravity, "just run a Rock move to deal with Charizards anyway."

## Threats & counters (from the video)

- Big Flyers (Talonflame / Corviknight / Charizard) are handled by **Gravity + Earthquake**, or by a **Rock move** on Steelix as a Gravity-free answer.
- Watch your own levitators/flyers under Gravity (see above).

## Importable teamlist (PokéSynergy-validated)

This is the **canonical export straight from PokéSynergy** — I built the team in the tool and every move + ability + item was **accepted as Champions-legal** (Speed Swap on Emolga, Gravity / Trick Room / Telepathy on Oranguru, Levitate Rotom, Sand Force Mega Steelix), and the tool auto-assigned roles (**Steelix = Offense**, the other three = **Support**). Paste it back into PokéSynergy's **Import**:

```
Steelix @ Steelixite
Ability: Sand Force
Level: 50
EVs: 32 HP / 32 Atk / 2 SpD
Brave Nature
- Earthquake
- Heavy Slam
- Protect
- Stone Edge

Emolga @ Focus Sash
Ability: Motor Drive
Level: 50
EVs: 4 HP / 32 SpA / 30 Spe
Timid Nature
- Speed Swap
- Helping Hand
- Nuzzle
- Discharge

Rotom-Wash @ Sitrus Berry
Ability: Levitate
Level: 50
EVs: 32 HP / 4 SpA / 30 SpD
Calm Nature
- Discharge
- Hydro Pump
- Protect
- Thunder Wave

Oranguru @ Mental Herb
Ability: Telepathy
Level: 50
EVs: 32 HP / 4 Def / 30 SpD
Sassy Nature
- Trick Room
- Gravity
- Instruct
- Protect
```

**Two things to know about this export (both learned by round-tripping it through the tool):**
- ⚠️ **Spreads are in Champions "Stat Points" (max 32/stat), NOT 252-EVs.** PokéSynergy and Champions use the Stat-Point system, so `EVs: 32 HP / 32 Atk` means *fully invested* — not "32 out of 252." Re-import this into **PokéSynergy** (or use it for Champions), not standard Pokémon Showdown, or the numbers won't mean what you expect. (Input 252-EV spreads get down-converted on import.)
- **Set the min-Speed IVs by hand** — the export omits IVs. For **Trick Room mode**, give Steelix and Oranguru **0 Speed IVs** (they want to be the slowest). In **Speed-Swap mode** Steelix inherits Emolga's Speed, so 0-Spe-IV is fine either way; Emolga stays max Speed as the donor.

*The 4th-slot picks are flexible:* Steelix's **Stone Edge** = a Gravity-free Rock answer to Charizard (or Body Press / Gyro Ball); Emolga's **Discharge** can be Air Slash (a real Champions Emolga set uses it) and **Nuzzle** can be Thunder Wave; Rotom's **Thunder Wave** can be Will-O-Wisp; Oranguru's **Instruct** can be Helping Hand.

## How PokéSynergy verifies/builds this (the tool loop)

- **Team Builder → search "Speed Swap" (data search):** confirm which mons carry the enabler (Emolga is the pick).
- **Speed tab:** after you decide Emolga's Speed, check what Steelix will outspeed once it receives that number via Speed Swap (tap tiers to see the breakpoints).
- **Calcs tab:** run Steelix's **Earthquake** against the Flying threats **with Gravity assumed** and confirm the KOs; also sanity-check that your own Discharge/Earthquake do 0 to your partners.
- **Analysis tab:** verify the team's type gaps and that the immunity shell actually covers Earthquake + Discharge.

See [[pokemon-champions-team-building/reusable-team-building-method]] to apply this loop to a *different* core.

## Key Takeaways

- **Free a slow nuke from Trick Room with Speed Swap** — Emolga (Motor Drive + Speed Swap) is the engine; it's also EQ-immune (Flying).
- **The immunity shell unlocks the spread move** — that's why Earthquake (not High Horsepower) is the payoff, and why every partner is Ground/Electric-immune.
- **Two modes** (Speed Swap / Trick Room + Gravity) + **Gravity** to ground Flyers make it flexible — mind the self-grounding downside.
- **Verified legal** (Mega Steelix, Emolga Speed Swap + Motor Drive); import the starting list and **tune spreads in PokéSynergy**.

Cross-links: [[pokemon-champions-team-building/reusable-team-building-method]] · [[pokesynergy-niche-business-tool/live-app-teardown]] · [[pokesynergy-niche-business-tool/_index]]
