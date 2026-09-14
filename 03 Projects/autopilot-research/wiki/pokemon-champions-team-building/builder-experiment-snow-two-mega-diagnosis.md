# Builder experiment #1 — diagnosing (and fixing) a two-Mega Snow/TR pile

> **What this is:** the topic's **first "diagnose-and-fix" case study** — not a creator team. The operator supplied a screenshot of a six-Pokémon team built in **[pokechampdex.com/team-builder](https://pokechampdex.com/team-builder)** (Vietnamese UI, "In-game" view) and asked to run the new **two-tool workflow** on it: build/read it in **pokechampdex** *in parallel* with a **web-verify fleet**, then make it coherent.
> **Source:** operator screenshot, 2026-09-14 (a personal build, not a tournament/creator list). Sets read off the image; **species/typings/abilities/moves/items web-verified**, SP/EVs not set.
> **Method note:** this is the reference example for the standing workflow — see [[pokemon-champions-team-building/reusable-team-building-method]].

## The two-tool workflow (new)

For every Champions team experiment going forward:

1. **pokechampdex.com/team-builder** (drive it in the browser) — the authoritative Champions surface. It encodes the exact model — **"In-game = Lv 50 (IV 31) + SP + tính cách (±10%)"** — lists **Mega / regional / gender formes as separate selectable entries**, auto-loads each mon's popular set, and outputs a live **analysis panel**: shared weaknesses, uncovered types, top-30 meta threats, and an In-game **speed table**. ⚠️ It returns **HTTP 403 to WebFetch**, so it must be read *in the browser*, never delegated to a fetch agent.
2. **Web-verify fleet** (Serebii / Bulbapedia / Game8 Champions / Pikalytics / op.gg / PokéBase / Pokémon-Zone) — adversarial verifiers + a completeness critic, to confirm mechanics and catch the tool's (and my own) blind spots.

On this run the two disagreed productively: pokechampdex **settled the Indeedee gender** (it auto-loaded the Female support set), and the fleet's critic **overturned one of its own verifiers** on the Z-Mega question (below).

## The team as read (image → verified)

| Slot | Read from image | Verified correction |
|---|---|---|
| "Mega Baxcalibur" — Dragon/Ice, Thermal Exchange, Adamant, **item = none**, Protect/Glaive Rush/Ice Shard/Icicle Crash | ⚠️ **Illegal as shown** — a Mega must *hold* its stone (Baxcalibrite). No item ⇒ it cannot Mega Evolve; the card is a **stat preview, not a battle state** |
| Ninetales-Alola — Ice/Fairy, Snow Warning, Timid, Occa Berry, Blizzard/Weather Ball/Aurora Veil/Icy Wind | ✅ all legal; Snow → Blizzard 100% acc, Weather Ball→Ice (100 BP), enables Aurora Veil, +50% Ice Def |
| Typhlosion-Hisui — Fire/Ghost, Blaze, Modest, **Choice Scarf**, Eruption/Shadow Ball/Heat Wave/**Protect** | ⚠️ **Protect is a dead slot on a Choice item** (Choice locks the first move) |
| Kingambit — Dark/Steel, Defiant, Adamant, Focus Sash, Kowtow Cleave/Sucker Punch/Low Kick/Protect | ✅ all legal (Low Kick weight-based, ≤120 BP) |
| "Indeedee" — Psychic/Normal, Psychic Surge, Relaxed, Colbur Berry, Follow Me/Trick Room/Helping Hand/Psychic | ✅ but it's **Indeedee-Female** (Follow Me is female-only within the species; pokechampdex confirmed by auto-loading exactly this set) |
| Mega Skarmory — Steel/Flying, Stalwart, Adamant, **Skarmorite**, Iron Head/Brave Bird/Protect/Dual Wingbeat | ✅ legal; **this is the only mon holding a stone → the intended, legal battle-Mega** |

## Diagnosis — 4 build errors + 3 incoherencies

**Build errors (illegal / wasted as shown):**
1. **Two Mega forms, one stone.** Champions allows **one Mega Evolution per team per battle**, triggered by *holding* the stone. Only Skarmory holds one → Baxcalibur, shown as "Mega" with no item, **cannot Mega**. The builder previews a Mega spread without enforcing the stone.
2. **Baxcalibur has no held item at all** — dead weight even as a base attacker.
3. **Protect on a Choice-Scarf Typhlosion** — Choice locks the first move, so Protect is unusable.
4. *(forme mislabel)* "Indeedee" with no gender — it must be **Indeedee-Female**.

**Incoherencies (legal but self-defeating):**
5. **The team fights its own priority.** Indeedee-F's **Psychic Surge auto-sets Psychic Terrain**, which makes **grounded** targets immune to increased-priority moves → it **nullifies the team's own Ice Shard (Baxcalibur) and Sucker Punch (Kingambit)** vs the grounded meta (Rillaboom, Incineroar, Kingambit, Tyranitar, Sneasler). Priority still lands on airborne foes — degraded, not dead.
6. **Trick Room vs a fast core.** Indeedee-F carries **Trick Room** (slower-first), but Ninetales-Alola, Mega Skarmory, and **Choice-Scarf** Typhlosion are all built to *outspeed*. TR inverts and wastes them.
7. **Choice Scarf under Trick Room** is doubly counterproductive.

pokechampdex's own panel corroborated: a **speed table** topped by Ninetales/Skarmory/Typhlosion (a fast team) — flatly contradicting the Trick Room — plus a **Fire 3/6, Rock 3/6** shared-weakness profile with meta threats Incineroar / Charizard-Y / Torkoal / Arcanine-Hisui / Tyranitar.

## Verified Champions mechanics (the reusable payload)

- **"Z-Mega" vs regular Mega** *(fleet critic overturned a verifier here)*: **Z-Mega Evolution IS the headline M-C feature** (official Pokémon Co. press release 2026-08-30; live 2026-09-09) — a *verifier wrongly said it wasn't in Champions*. A **"Z-Mega" is a SECOND Mega** for a species that already had a **Gen-6 Mega** — [[pokemon-champions-team-building/mega-absol-z-sharpness-team|Mega Absol Z]], [[pokemon-champions-team-building/mega-lucario-z-salamence-special-team|Mega Lucario Z]], Mega Garchomp Z. A species with **no prior Mega** gets a **regular first-time Mega** — so **Mega Baxcalibur (Gen 9) and Mega Skarmory (Gen 2) are NOT Z-Megas**. (This validates the topic's existing "…Z" guide titles — they're correct.)
- **Mega rule:** one Mega per team **per battle**; you may *carry* several; a mon must **hold** its stone. Stones: **Baxcalibrite**, **Skarmorite** (2000 Victory Points each).
- **Stat model (SP):** always **Lv 50, fixed IV 31**; EVs replaced by **Stat Points — 66 total, max 32 per stat, 1 SP = 8 EVs**. Natures are renamed **"Stat Alignment"** (+10% / −10%, mechanically identical; Mints removed, re-align for 500 VP). pokechampdex "In-game" view = this conversion.
- **Psychic Terrain** boosts grounded Psychic moves **×1.3 (not ×1.5)** and blocks increased-priority on grounded targets, 5 turns.
- **Stalwart** (Mega Skarmory): the user's moves **ignore redirection** (Follow Me / Rage Powder / Lightning Rod / Storm Drain / Ally Switch).
- **Thermal Exchange** (Baxcalibur): **+1 Atk when hit by a Fire move + burn immunity** (does *not* reduce Fire damage).
- **Glaive Rush** drawback in Champions is named the **"Wide Open"** status — until the user's next action, attacks on it can't miss and deal double damage.
- **Snow** (Snow Warning, not Hail): +50% Ice-type Def, Blizzard 100% acc, enables Aurora Veil.

## The patched build — a legal Snow Aurora-Veil hyper-offense

Fixes the 4 build errors + the two speed contradictions, keeping all six species (fleet-verified legal, no illegal component):

| Slot | Patch | Set |
|---|---|---|
| **Skarmory → Mega** (sole Mega) | designate the one stone-holder as the Mega | Skarmorite · Stalwart · Adamant · Iron Head / Brave Bird / Dual Wingbeat / Protect |
| **Baxcalibur (base)** | drop the second Mega; give a real item | Focus Sash (or Life Orb) · Thermal Exchange · Adamant · Glaive Rush / Icicle Crash / Ice Shard / Protect |
| **Typhlosion-Hisui** | **drop Protect** (dead on Choice) | Choice Scarf · Blaze · Modest · Eruption / Heat Wave / Shadow Ball / **Overheat** *(matches Game8's recommended set verbatim)* |
| **Indeedee-Female** | **drop Trick Room** | Colbur · Psychic Surge · Bold · Follow Me / Helping Hand / Psychic / **Dazzling Gleam** *(Expanding Force is **not** legal on the Female — avoid)* |
| Ninetales-Alola | keep (snow/screens engine); Light Clay optional | Snow Warning · Timid · Blizzard / Aurora Veil / Icy Wind / Protect |
| Kingambit | keep | Focus Sash · Defiant · Adamant · Kowtow Cleave / Sucker Punch / Low Kick / Protect |

## "Legal ≠ coherent" — the critic's roadmap to a real team

The patch is **tournament-legal** but the adversarial critic downgraded "legal ⇒ done": it **trades the Trick-Room contradiction for a Psychic-Terrain-vs-own-priority one**, and leaves **Fire 4/6 wide open**. Two further swaps make it a genuine screens-HO:

- **(a) Indeedee-Female → Clefable** (Follow Me / Moonblast / Helping Hand / Protect · **Magic Guard**, no terrain) — removes the Psychic-Terrain anti-synergy entirely, restoring Ice Shard + Sucker Punch. *(Clefable is the same Follow-Me support used in [[pokemon-champions-team-building/priority-stack-baxcalibur-kingambit-team|Victrelian's priority team]].)*
- **(b) Cut Kingambit → a bulky Fire-resisting Water** — patches the Fire hole **and** removes the second terrain-blocked priority user. (Kingambit is the least coherent member on both axes: Fire-weak *and* Sucker-Punch-reliant; pin the exact Water against live Reg M-C usage.)

Nuance the critic corrected in *my* reasoning: the right reason to drop Trick Room is the **Scarf+TR conflict**, not "we're fast" — base Baxcalibur (Spe 87) and Kingambit (Spe 50) are actually slow, which is exactly why the terrain hurts them.

## Key Takeaways

- **A team-builder screenshot is a planning preview, not a legal team.** pokechampdex will show a "Mega X" stat line with no stone; the **one-Mega-per-battle / must-hold-the-stone** rule is yours to enforce. Read the *held stone* to learn the intended Mega.
- **Psychic Surge is a double-edged support.** Great when you *want* to shut off priority (see [[pokemon-champions-team-building/japan-sand-dual-mega-salamence-tyranitar-team|Japan Sand]], which uses Indeedee-M terrain to turn off *enemy* Fake Out/Grassy Glide) or when your win-con is slow ([[pokemon-champions-team-building/mega-golisopod-hatterene-magic-powder-team|BlindJon's TR Golisopod]], a **coherent** Indeedee-F + Terrain + Trick Room team). **Hostile** when your own plan is priority + speed, as here.
- **Follow Me is female-only within Indeedee** — the move settles the forme.
- **Never run Protect on a Choice item.** Obvious in hindsight, easy to miss in a builder that lets you.
- **"Z-Mega" ≠ every new Mega.** It's specifically a *second* Mega for a Gen-6-Mega species; Baxcalibur/Skarmory are regular first Megas.
- **Legal ≠ coherent.** A build can pass every legality check and still lose to itself. The fleet's *coherence critic* is what catches that; the *legality verifier* won't.

Cross-links: [[pokemon-champions-team-building/_index]] · [[pokemon-champions-team-building/reusable-team-building-method]] · [[pokemon-champions-team-building/tailwind-snow-ho-team]] (the topic's other Snow-HO) · [[pokemon-champions-team-building/mega-baxcalibur-terrain-team]] (Psychic Terrain used *deliberately* as defense) · [[pokemon-champions-team-building/mega-golisopod-hatterene-magic-powder-team]] (a coherent Indeedee-F + TR team)

Sources: operator screenshot (2026-09-14); [pokechampdex.com/team-builder](https://pokechampdex.com/team-builder) (In-game analysis panels); web-verify fleets over Game8 Champions, Pikalytics Reg M-C, op.gg, Serebii, MetaVGC, and the official Pokémon Co. Asia press release (2026-08-30). SP/EVs not shown in the image; species/typing/ability/move/item legality web-verified; the "coherent" build swaps (Clefable, the Water) are recommendations, not yet piloted.
