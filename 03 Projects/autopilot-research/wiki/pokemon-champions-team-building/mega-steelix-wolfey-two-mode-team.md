# Worked Example #3 — Wolfey's two-mode Mega Steelix (the tournament build)

> **Source:** [Wolfey's MEGA STEELIX Team COUNTERED the Meta!](https://www.youtube.com/watch?v=sYzs73TeFR8) — `sYzs73TeFR8`, **MrSteelixYourGirl**, 2026-06-01, 37:14, ~37.5K views. The team is **Wolfey's** ([@WolfeyVGC](https://www.youtube.com/@WolfeyVGC)) — piloted to **2nd place at the Indianapolis Regional**; EV spreads by **Justin Tang** (@Unironicpanda-vgc).
> **Verified** in [PokéSynergy](https://pokesynergy.app): imported clean (1 warning — Talonflame's `Covert Cloak` item unrecognized, swap it); all abilities/moves Champions-legal; the **two-Mega build (Steelixite + Tyranitarite) is accepted**.
> **Visual guide (⭐):** [interactive synergy + game-plan Artifact](https://claude.ai/code/artifact/5f8135b5-13a2-4afa-a3be-3d2af7da0989) · in-vault copy: [`steelix-synergy-guide.html`](steelix-synergy-guide.html). Mermaid maps below render in Obsidian.

## The idea: one team, two win-conditions — pick from the enemy

Where examples [#1](pokemon-champions-team-building/mega-steelix-speed-swap-team) and [#2](pokemon-champions-team-building/mega-steelix-sand-trick-room-team) each commit to *one* engine, this pro team carries **two Megas and two modes** and **chooses which to run based on the opponent** — the exact "read the enemy → follow a plan" idea worth stealing for a tool:

- **Mode B · Sand Trick Room (Mega Steelix):** Sinistcha sets Trick Room → 30-Speed Steelix moves first; Tyranitar's sand powers Sand Force.
- **Mode A · "Protect the Queen" (Mega Tyranitar):** stack Dragon Dance on Mega Tyranitar until it out-speeds and one-shots everything — *no Trick Room needed*.

## Synergy map — Mode B (Trick Room · Mega Steelix)

```mermaid
flowchart TB
    classDef hub fill:#12222b,stroke:#57cbe6,stroke-width:4px,color:#e6eef2;
    classDef sne fill:#141f24,stroke:#e878c8,color:#e6eef2;
    classDef rot fill:#141f24,stroke:#6aa8ff,color:#e6eef2;
    classDef sin fill:#141f24,stroke:#9ede3f,color:#e6eef2;
    classDef tyr fill:#141f24,stroke:#e6b84a,color:#e6eef2;
    SNE["SNEASLER<br/>Fake Out · Pressure"]:::sne --> STE
    ROT["ROTOM-WASH<br/>Light Screen · Will-O-Wisp"]:::rot --> STE
    SIN["SINISTCHA<br/>Trick Room · Heal · Redirect"]:::sin --> STE
    TYR["TYRANITAR<br/>Sets Sand → Sand Force"]:::tyr --> STE
    STE["MEGA STEELIX<br/>focal point"]:::hub
```

## Synergy map — Mode A (Protect the Queen · Mega Tyranitar)

```mermaid
flowchart TB
    classDef hub fill:#241d10,stroke:#e6b84a,stroke-width:4px,color:#f2ece0;
    classDef sne fill:#141f24,stroke:#e878c8,color:#e6eef2;
    classDef rot fill:#141f24,stroke:#6aa8ff,color:#e6eef2;
    classDef sin fill:#141f24,stroke:#9ede3f,color:#e6eef2;
    classDef tal fill:#141f24,stroke:#ff9a52,color:#e6eef2;
    SNE["SNEASLER<br/>Fake Out buys a DD turn"]:::sne --> TYR
    ROT["ROTOM-WASH<br/>Screens · Burn walls"]:::rot --> TYR
    SIN["SINISTCHA<br/>Redirect hits · Heal"]:::sin --> TYR
    TAL["TALONFLAME<br/>Priority Brave Bird"]:::tal --> TYR
    TYR["MEGA TYRANITAR<br/>Dragon Dance sweeper"]:::hub
```

## ⭐ Game plan by enemy team (the feature idea)

The reusable move — a niche tool that reads the enemy lead and hands the player a **step-by-step plan**, not just a damage number:

| If the enemy… | Then… | Mode |
|---|---|---|
| has Tailwind / fast hyper-offense | **Trick Room** (Mega Steelix) — flip their speed | Mode B |
| is slow / bulky / runs its own Trick Room | **Queen** (Mega Tyranitar Dragon Dance) — out-tempo without TR | Mode A |
| leads spread Earthquake (Garchomp etc.) | lead **Steelix + Wide Guard** to shield Tyranitar | support |
| main threat is physical | **Rotom Will-O-Wisp** (burn halves their damage) | every game |
| main threat is special | **Rotom Light Screen** (+ Tyranitar sand SpD) | every game |
| any game, turn 1 | **Sneasler Fake Out** + pivot **Sinistcha** in/out for free Sitrus healing | every game |

## The six

| Mon | Ability | Role | Key set |
|---|---|---|---|
| **Mega Steelix** | Sand Force | TR nuke / **Wide Guard** wall | Heavy Slam · High Horsepower · Wide Guard · Protect |
| **Tyranitar** | Sand Stream | sand setter · **DD sweeper** (the Queen) | Dragon Dance · Rock Slide · Crunch · Protect — *holds Tyranitarite (2nd Mega)* |
| **Sinistcha** | Hospitality | **Trick Room** · heal · redirect | Trick Room · Rage Powder · Life Dew · Matcha Gotcha |
| **Rotom-Wash** | Levitate | damage mitigation (the star) | Will-O-Wisp · Light Screen · Hydro Pump · Protect |
| **Sneasler** | Pressure | disruptor / lead | Fake Out · Dire Claw · Close Combat · Protect |
| **Talonflame** | Gale Wings | priority revenge | Brave Bird · Swords Dance · Tailwind · Protect |

*EV spreads are Justin Tang's (shown in the video, not dictated) — grab Wolfey's rental from the source for exact numbers. Moves above are validated legal in PokéSynergy.*

## Why this belongs in the corpus (the business-tool angle)

The operator's read is the payload: **this graphic format is a product feature.** PokéSynergy (and the niche-tool archetype in [[pokesynergy-niche-business-tool/_index]]) is strongest when it gives a player *"a short reason you can act on"* — and a **"paste the enemy team → get a step-by-step game plan"** view is exactly that, one level up from a damage calculator. It's the same shape as the hireui borrow ([[pokesynergy-niche-business-tool/hireui-translation]]): an **explainable, deterministic, step-by-step recommender** driven by the opponent's constraints. Wolfey's two-mode team is the perfect worked example because the *plan literally changes with the enemy* — so the tool has something non-obvious to tell you.

## Verification notes

- ✅ **Team validated in PokéSynergy** (import): all abilities/moves legal (Sinistcha Hospitality + Rage Powder/Life Dew/Matcha Gotcha, Sneasler Pressure, Gale Wings Talonflame, Sand Force Steelix, Sand Stream Tyranitar). **Two Mega stones on one team accepted** — confirms the dual-Mega, dual-mode plan is buildable. Only warning: Talonflame's `Covert Cloak` item not recognized (swap to a legal item).
- ⚠️ **ASR catch (Rule 12 / wiki-verify):** the auto-caption repeatedly says "Cinccino" for the Trick Room setter; the creator's on-screen graphic **and** the per-Pokémon breakdown both show **Sinistcha** (Hospitality — heal + redirect). Corrected to Sinistcha throughout. ("Cinccino" is not on the team.)
- The exact EVs are Justin Tang's; treat the sets here as validated-legal reconstructions, the rental code (from the video) as the source of truth.

## Key Takeaways

- **Two Megas, two modes, pick by matchup** — the most flexible of the three Steelix builds; the plan is a *decision*, not a fixed line.
- **The "enemy team → step-by-step plan" graphic is the reusable product idea** — a niche tool that recommends a game plan, not just a calc (ties to [[pokesynergy-niche-business-tool/hireui-translation]]).
- **Rotom-Wash is the engine** here (Light Screen + Will-O-Wisp make the sand core un-KO'able), and **Sinistcha** is the glue (TR + heal + redirect).
- Tournament-proven (Wolfey, 2nd @ Indianapolis) — the "meta/pro" counterpart to #1 (off-meta gimmick) and #2 (ladder-traditional).

Cross-links: [[pokemon-champions-team-building/mega-steelix-speed-swap-team]] · [[pokemon-champions-team-building/mega-steelix-sand-trick-room-team]] · [[pokemon-champions-team-building/reusable-team-building-method]] · [[pokesynergy-niche-business-tool/hireui-translation]]
