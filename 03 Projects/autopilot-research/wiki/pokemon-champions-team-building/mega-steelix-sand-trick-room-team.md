# Worked Example #2 — the Sand + Trick Room Mega Steelix team

> **Source:** [SAND e TRICK ROOM com MEGA STEELIX 🏆 Pokémon Champions](https://www.youtube.com/watch?v=3bllP_QXAzU) — `3bllP_QXAzU`, **Pokémon Trainer Lucca** (Brazilian, PT), 2026-05-26, 32:24, ~5.2K views. A 3-battle replay video; the team + EVs are revealed at **27:09**.
> **Verified** in [PokéSynergy](https://pokesynergy.app): the full team was rebuilt and every ability/move validated Champions-legal (Sand Force, Sand Stream, **Armor Tail**, Pixilate, Intimidate, Adaptability all accepted).
> **This is the *traditional* answer to the same problem** as [[pokemon-champions-team-building/mega-steelix-speed-swap-team]] — and it makes the **opposite** build choices, which is why it's worth studying alongside it.

## The approach: Sand + Trick Room (dual engine)

Same problem as video 1 (Steelix is a Def monster but painfully slow), solved the **standard** way — two supporting engines instead of Speed Swap:

- **Sand (Tyranitar's Sand Stream)** — sandstorm turns on Mega Steelix's **Sand Force**, boosting its Ground/Rock/Steel moves by **30%**. Steelix, Tyranitar (Rock), and Steel types take no sand chip. So the weather isn't just chip — it's a damage buff for the whole Ground/Steel core.
- **Trick Room (Farigiraf)** — reverses the speed order for 5 turns so the slow mons (Steelix ~45 Spe, Tyranitar, Sylveon) move first.

## The team

| Mon | Ability | Role | Key set (verified legal in PokéSynergy) |
|---|---|---|---|
| **Mega Steelix** | Sand Force | Offense (Def wall-attacker) | **Body Press** + **High Horsepower** + Heavy Slam + Protect; full **HP/Def** (maxed = **310 Def**) |
| **Tyranitar** | Sand Stream | Offense | Rock Slide / Crunch / **Ice Punch** / Protect; **Chople Berry** (survive a super-effective Fighting hit); slow (for TR) |
| **Farigiraf** | **Armor Tail** | Support (TR setter) | **Trick Room** + **Light Screen** + Foul Play + Helping Hand |
| **Incineroar** | Intimidate | Support/offense pivot | Fake Out + Close Combat + Flare Blitz + Knock Off; full HP/Atk |
| **Sylveon** | Pixilate | TR special attacker | **Hyper Voice** (→ Fairy via Pixilate) + Mystical Fire + Helping Hand + Protect; Quiet, **Fairy Feather** |
| **Basculegion** | Adaptability | non-TR cleaner | **Choice Scarf**, Wave Crash / Aqua Jet / Head Smash / Final Gambit — the backup when Trick Room isn't up |

## The build choices — and why they're the *opposite* of the Speed-Swap team

This is the payload. Same Mega Steelix, inverted decisions:

| Decision | Sand + TR team (this) | Speed-Swap team ([video 1](pokemon-champions-team-building/mega-steelix-speed-swap-team)) | Why |
|---|---|---|---|
| **Move first** | Trick Room (5-turn clock) + a Scarf backup | Speed Swap (no clock) | different speed engines for the same slow nuke |
| **Ground move** | **High Horsepower** (single-target) | **Earthquake** (spread) | Lucca **explicitly avoids Earthquake "to not hit my own Tyranitar"** — he has *no immunity shell*. Video 1 runs Earthquake *because* its Levitate/Flying/Telepathy shell makes spread safe. **Same mon, opposite move, because of the surrounding team.** |
| **Steelix's STAB attacker** | **Body Press** (uses its 310 Def as the attack stat) | physical Atk | Body Press turns the maxed Def into offense — a Def-wall that also nukes |
| **Speed-side patch** | Farigiraf **Light Screen** (halves special damage) | — | both teams flag Steelix's weak **special defense (~87)**; here Light Screen covers it |
| **Priority control** | Farigiraf **Armor Tail** (blocks *enemy* priority → you win the Fake Out war) | — | Armor Tail lets Incineroar's Fake Out land first uncontested |
| **Non-TR fallback** | **Choice Scarf Basculegion** | Speed Swap already covers it | the classic TR-team insurance: a fast Scarfer for when TR is down |

**The one-line lesson:** *the nuke's spread move is decided by the team around it, not the nuke.* No immunity shell → single-target High Horsepower. Immunity shell → spread Earthquake. This is exactly the invariant in [[pokemon-champions-team-building/reusable-team-building-method]].

## Lucca's exact build (team code)

He shares an in-game **team code: `6D3DJQJS3Q`** (spoken in the video at ~27:00).

> ⚠️ **Transcription caveat:** that code is transcribed from *spoken* characters in an auto-caption — single-character errors are likely. Treat it as a lead, **verify the exact string in-game**, and use it as the source of truth for his precise EVs (which he shows on-screen but doesn't dictate). The teamlist below is my **PokéSynergy-validated reconstruction**, not his exact numbers.

## Importable teamlist (PokéSynergy-validated reconstruction)

Canonical export from PokéSynergy after rebuilding the team — all abilities/moves accepted as Champions-legal. **Spreads are in Champions "Stat Points" (max 32/stat), not 252-EVs** — re-import into PokéSynergy/Champions, not standard Showdown (see [[pokemon-champions-team-building/mega-steelix-speed-swap-team]] for the SP explanation). Set **0 Speed IVs** by hand on Steelix / Tyranitar / Farigiraf / Sylveon for Trick Room (the export omits IVs).

```
Steelix @ Steelixite
Ability: Sand Force
Level: 50
EVs: 32 HP / 32 Def / 2 SpD
Relaxed Nature
- Body Press
- High Horsepower
- Heavy Slam
- Protect

Tyranitar @ Chople Berry
Ability: Sand Stream
Level: 50
EVs: 32 HP / 32 Atk / 2 SpD
Brave Nature
- Rock Slide
- Crunch
- Ice Punch
- Protect

Farigiraf @ Sitrus Berry
Ability: Armor Tail
Level: 50
EVs: 32 HP / 4 Def / 30 SpD
Sassy Nature
- Trick Room
- Light Screen
- Foul Play
- Helping Hand

Incineroar @ Sitrus Berry
Ability: Intimidate
Level: 50
EVs: 32 HP / 32 Atk / 2 Def
Adamant Nature
- Fake Out
- Close Combat
- Flare Blitz
- Knock Off

Sylveon @ Fairy Feather
Ability: Pixilate
Level: 50
EVs: 32 HP / 32 SpA / 2 SpD
Quiet Nature
- Hyper Voice
- Mystical Fire
- Helping Hand
- Protect

Basculegion @ Choice Scarf
Ability: Adaptability
Level: 50
EVs: 4 HP / 32 Atk / 30 Spe
Jolly Nature
- Wave Crash
- Aqua Jet
- Head Smash
- Final Gambit
```

*Reconstruction flags (verify against the code):* the video says "**Basculin** (Scarf)" — I used **Basculegion** (the meta Adaptability Scarf water cleaner) as the closest legal fit; swap if his is base Basculin. Filler slots (Incineroar's Flare Blitz/Knock Off, Sylveon's Mystical Fire, Basculegion's Head Smash/Final Gambit, Tyranitar's exact rock/ice moves) are sensible standards, not dictated in the video.

## How it maps to the reusable method

Same 5 roles as [[pokemon-champions-team-building/reusable-team-building-method]], filled differently:

- **Nuke:** Mega Steelix (same).
- **Speed engine:** **Trick Room (Farigiraf) + Scarf (Basculegion)** here — *not* Speed Swap/Emolga. (The method's "Emolga = fixed" only holds for the *Speed-Swap variant*; the general problem — "make the slow nuke move first" — has multiple solutions, and this is the other big one.)
- **Damage enabler:** **Sand (Tyranitar → Sand Force)** here instead of an immunity shell.
- **Glue:** Farigiraf (Armor Tail + Light Screen) + Incineroar (Intimidate + Fake Out).

## Key Takeaways

- **Two legitimate ways to move a slow Steelix first:** Speed Swap (no clock, off-meta) vs **Trick Room + Scarf backup** (traditional, this team).
- **The team decides the spread move:** no immunity shell here → **High Horsepower (single-target)** so you don't hit your own Tyranitar — the exact inverse of video 1's Earthquake.
- **Body Press** makes Steelix's maxed **310 Def** its offense; **Sand Force + Tyranitar's sand** adds +30% to its Ground/Steel moves.
- **Both teams share Steelix's special-def hole** (~87) — patched here by Farigiraf's **Light Screen**.
- Exact numbers live in the **team code `6D3DJQJS3Q`** (verify in-game); the list above is a tool-validated reconstruction.

Cross-links: [[pokemon-champions-team-building/mega-steelix-speed-swap-team]] · [[pokemon-champions-team-building/reusable-team-building-method]] · [[pokemon-champions-team-building/_index]]
