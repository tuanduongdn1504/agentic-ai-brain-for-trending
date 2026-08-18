# pokemon-champions-team-building

> **What this is:** a reusable, PokéSynergy-driven resource for building competitive **Pokémon Champions** (VGC 2026 Doubles) teams around a chosen core — worked examples + a transferable method. Distinct from [[pokesynergy-niche-business-tool/_index]], which studies PokéSynergy as a *business archetype*; this topic uses the **tool itself** to build and verify teams.
> **Started:** 2026-07-17 (branch `autopilot-research-pokesynergy-deepen`) from the operator's request to learn a Mega Steelix build and turn it into a reusable resource.

## Articles

| File | What it covers |
|---|---|
| [[pokemon-champions-team-building/mega-steelix-speed-swap-team]] | ⭐ Worked example **#1** — Mr. Browser's **Speed-Swap Mega Steelix** (off-meta): free the slow nuke with Speed Swap (no Trick Room), a double-immunity spread-spam shell, the importable teamlist |
| [[pokemon-champions-team-building/mega-steelix-sand-trick-room-team]] | ⭐ Worked example **#2** — Pokémon Trainer Lucca's **Sand + Trick Room Mega Steelix** (traditional): the *opposite* build choices (High Horsepower not Earthquake, Body Press, Armor Tail glue, Scarf backup) — a direct contrast to #1 |
| [[pokemon-champions-team-building/mega-steelix-wolfey-two-mode-team]] | ⭐ Worked example **#3** — Wolfey's tournament team (2nd @ Indianapolis Regional): **two Megas, two modes, picked from the enemy team**; carries the ⭐ "enemy team → step-by-step plan" feature idea + a visual synergy guide |
| [`steelix-synergy-guide.html`](steelix-synergy-guide.html) · [open Artifact](https://claude.ai/code/artifact/5f8135b5-13a2-4afa-a3be-3d2af7da0989) | 🎨 **Interactive guide** — synergy map **+ a working Game Plan Assistant**: paste the enemy team → get the mode, a step-by-step plan, and a **matchup-risk flag** (deterministic rule engine; built-in finals sand-vs-sun + Top-4 examples). **Multi-team:** a *Piloting* toggle swaps the plan engine across **three teams** — Steelix Sand/TR, Tailwind Snow-HO, and Arcanine Speed-Flex |
| [[pokemon-champions-team-building/reusable-team-building-method]] | ⭐ The transferable pattern — a 5-role template + a step-by-step PokéSynergy workflow to build **your own** variants; the three worked examples show the *same* nuke solved three different ways |
| [[pokemon-champions-team-building/finals-case-study-sand-vs-sun]] | 🏆 **Finals case study** — the #3 Steelix team vs Arsal Puri's *winning* **Sun** team (Mega Charizard-Y + **Mega Floette**) at Indianapolis: the sand-vs-sun matchup, Wolfey's mode-pick, and the honest outcome (**Steelix lost — 2nd**). The "when the matchup is bad" half of the enemy-team feature |
| [[pokemon-champions-team-building/how-to-choose-your-mode]] | 🧭 **Step-by-step: choose your mode from the enemy team** — a 6-step decision procedure + flowchart, grounded in Wolfey's real Indianapolis mode log (Top-4 vs Zhang → Queen; finals vs Arsal → Steelix-TR). The human-readable rulebook behind the Game Plan Assistant |
| [[pokemon-champions-team-building/tailwind-snow-ho-team]] | ❄️ **Non-Steelix contrast** — a **Tailwind / Snow Hyper-Offense** built from operator's 6 mons (Froslass/Sneasler/Rotom/Garchomp/Kingambit/Talonflame): *fast*, priority-backed, Mega Froslass **Snow Warning** → Blizzard/Aurora Veil. Proves the reusable method generalizes (slow-nuke ↔ fast-HO); a **preset in the Game Plan Assistant** |
| [[pokemon-champions-team-building/hisuian-arcanine-speed-flex-team]] | 🔥 **Guide: Hisuian Arcanine "triple speed-control" flex** (Duy Plays Poké VN review): **3 line-ups** + a double Tailwind/Trick-Room mode; dual-Mega **Staraptor (Contrary) + Raichu Y**; Arcanine (Rock Head + Head Smash) locks Charizard. The most flexible team in the topic |
| [[pokemon-champions-team-building/zoroark-illusion-fun-team]] | 🃏 **Fun/gimmick build — the honest anti-thesis** (Thế Giới Anime, 2h VN livestream): a Zoroark **Illusion** troll team — a snow/veil core (Mega Froslass) *wearing a disguise*, with double-Fighting anti-Kingambit tech (Sneasler + Arcanine). The creator says win/loss doesn't matter and **loses several shown games**. The topic's benchmark for *"gimmicks express, tournament teams convert."* **Not** a Game Plan Assistant preset (fixed gimmick, no mode-branching) |
| [[pokemon-champions-team-building/meta-sand-team-scouting-report]] | 🔍 **Scouting report — the #2 meta sand team, and how to beat it** (IanKim counter-guide): the topic's first *enemy* teardown — **dual-Mega sand balance** (Mega Tyranitar + Excadrill Sand Rush + Mega Staraptor Contrary + Milotic/Sinistcha support + Gholdengo nuke) with **per-Pokémon counters** (deny sand, KO Gholdengo early, grass/spread beat Rage Powder). The concrete team behind the Game Plan Assistant's *"vs sand"* branch |
| [[pokemon-champions-team-building/floette-coaching-dual-mega-team]] | 🏆 **The #1 ladder team last season** (CybertronVGC breakdown; built by Jude Lee, Worlds 2025 Top-32): **dual-Mega setup/support** — a bulky Calm Mind **Mega Floette** (Draining Kiss heals 75%, Fairy Aura) made near-unkillable by the signature **Coaching Sneasler** tech, with **Mega Garchomp** as the flex second Mega vs Fire/Steel/sand. Double Fake Out + Intimidate + Sinistcha redirection buy the setup turns. The topic's tournament-proven *"convert"* archetype |

## The core idea (one paragraph)

A very slow, very strong attacker (Mega Steelix, base Speed **30**) is normally trapped in **Trick Room** (5-turn limit). This archetype frees it two ways: **Speed Swap** (Emolga donates its own boosted Speed, no turn limit) and a **Trick Room + Gravity** fallback. Around the nuke sits a **spread-immunity shell** — Earthquake (Steelix) and Discharge (Rotom-Wash) are spread moves the whole team is *immune* to (Levitate / Flying / Telepathy / Motor Drive), so the team spams spread damage while taking none, and **Gravity** drops Flying-types so Earthquake hits everything. The transferable lesson: the immunity shell is what unlocks the *spread* move — on PokéSynergy, Steelix's Earthquake sits at only **35% usage** vs High Horsepower's **50%** precisely because most teams can't run a spread move without hitting their own partner.

## Two approaches to the same core (side-by-side)

Both teams take the same problem — Mega Steelix is a 310-Def monster with ~30 base Speed — and solve it in opposite ways. Studying the pair teaches more than either alone:

| | #1 Speed-Swap (Mr. Browser) | #2 Sand + Trick Room (Lucca) |
|---|---|---|
| **Move first** | Speed Swap (Emolga), no turn limit | Trick Room (Farigiraf) + Choice Scarf backup |
| **Ground move** | **Earthquake** (spread) | **High Horsepower** (single-target) |
| **Why that move** | immunity shell makes spread safe | *no* shell → avoid hitting own Tyranitar |
| **Damage boost** | live meta breakpoints | **Sand** (Tyranitar → Sand Force +30%) |
| **Steelix offense** | physical Atk | **Body Press** (attacks off 310 Def) |
| **Special-def patch** | — | Farigiraf **Light Screen** |
| **Vibe** | off-meta gimmick the tool won't suggest | traditional, meta-standard |

**The transferable insight:** the nuke's own moveset is dictated by the *team around it*, not the nuke — so the reusable method is about choosing an engine (Speed Swap vs Trick Room) and a damage-enabler (immunity shell vs sand), then letting those decide Steelix's moves.

**#3 (Wolfey — [[pokemon-champions-team-building/mega-steelix-wolfey-two-mode-team]]) is the adaptive synthesis:** it carries *both* engines — Trick Room **and** Dragon Dance, via **two Megas** — and picks the mode from the opponent's team. That's the tournament-proven version, and it's where the operator's ⭐ product idea lands: a niche tool that reads the enemy team and hands you a **step-by-step game plan**, not just a damage number (see the [visual guide](steelix-synergy-guide.html) / [Artifact](https://claude.ai/code/artifact/5f8135b5-13a2-4afa-a3be-3d2af7da0989), and the hireui tie-in in [[pokesynergy-niche-business-tool/hireui-translation]]).

## Key Takeaways

- **Top-meta shape = "two Megas, two modes, pick by enemy."** Both finalists at Indianapolis ran it (Wolfey: Steelix/Tyranitar; Arsal: Charizard-Y/Floette) — see [[pokemon-champions-team-building/finals-case-study-sand-vs-sun]]. And the honest coda: the Steelix team **lost the finals** to the Sun team, so the enemy-team tool must also flag *unfavorable* matchups, not just hand you a line.
- **The engine is Emolga** (Motor Drive + Speed Swap) — the one fixed piece; the nuke and the levitator are swappable (the creator says so outright).
- **Immunity shell → spread moves.** Stacking Ground/Electric immunities is what lets the team run Earthquake + Discharge together.
- **Two speed modes** (Speed Swap primary, Trick Room + Gravity fallback) make the build robust.
- **This is an off-meta creative build** — PokéSynergy's default "Top Teammates" for Steelix are meta picks (Talonflame, Mega Charizard Y), *not* this gimmick, so the tool won't hand it to you; you build it deliberately.

Cross-links: [[pokesynergy-niche-business-tool/_index]] · [[pokesynergy-niche-business-tool/live-app-teardown]] (how the Speed/Analysis/Calcs tabs work)
