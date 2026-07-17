# Live-App Teardown — hands-on primary research

*Deepening Axis 2. Everything here was verified by **driving the live app in a browser** on **2026-07-17** (signed out, no account, no PII entered — the app requires no login). This is the wiki's first primary interaction evidence; earlier articles rested on a single WebFetch + the video transcript. Where this corrects an earlier article, it is flagged and logged in [[pokesynergy-niche-business-tool/caveats-and-corrections]].*

## Correction 1 — the real information architecture is 5 sections, not 9 tools

The live app's actual top navigation is **five sections**: **Teams · Team Builder · Speed · Analysis · Calcs** (+ a settings gear, an optional *Sign in*, and a Discord link). The 9-tool table in [[pokesynergy-niche-business-tool/product-anatomy]] was assembled from the marketing `/vs` comparison pages and lists *capabilities by their marketing names* (Weakness Checker, Type Coverage, MetaDex, SynerDex, PokeBox, Tier List…). In the product those are **folded into the five sections** — e.g. weakness/coverage/meta-team analysis all live inside **Analysis**. The capabilities are real; the "9 separate tools" framing is a marketing-page artifact.

## The Team Builder — expert-defaults are visible everywhere

Adding a Pokémon opens a picker that is **usage-sorted by default** (#1 Garchomp, #2 …, #3 Basculegion) — the meta ranking is the default sort, not an afterthought. On each mon:

- a **base-stat hexagon** + bars on hover;
- **abilities annotated with usage %** (Garchomp → "Rough Skin **98%** / Sand Veil 2%");
- once picked, **moves arrive pre-ranked by tournament usage %** (Dragon Claw 89% · Rock Slide 84% · Earthquake 79% · Protect 73% · Stomping Tantrum 32% · Poison Jab 16%);
- inside Edit Build, move suggestions carry an **explainable reason tag** — e.g. "Dragon Claw 100% · **Team gap**", "Earthquake 88% · Team gap" — i.e. *why* it's suggested, not just a score;
- a **"Cores" / Suggestions** panel proposes synergistic partners after you pick one mon ("Pick one Pokemon first") — this is the *Synergy* the product is named for;
- **Auto Build** fills sets for *existing* mons (it is disabled on an empty team — it does not conjure a whole team from nothing, matching the video's flow: load a team, then auto-build).

## Correction 2 — the crux: "click a threat → points auto-shift" IS real (per-breakpoint)

This resolves the wiki's central honesty question with direct evidence.

The **Stats** editor has three views — **Speed · Offense · Defense** (the three the video showed). The Speed view header literally reads **"Tap a speed tier to auto-configure."** I tested it on a blank (all-zero) Garchomp spread:

| Action | Result (read from the live DOM) |
|---|---|
| Tapped **Sceptile** (row said *"Cannot outspeed with legal spread"*) | **Nothing changed** — the tool honestly does nothing when the breakpoint is unreachable |
| Tapped **Mega Blaziken** (Spe 167, 61.3% usage — outspeedable) | **Spe SP auto-set 0 → 31**; final Speed 102→**168** (outspeeds by 1); a "**SPEED TARGET: Mega Blaziken – 167**" chip appeared; **"Your rank" jumped #435 → #204** live |

**So the video's "click a threat and the points automatically shift to hit the breakpoint" is literally true** — for a single stat, against a single target, with live meta-rank recompute. [[pokesynergy-niche-business-tool/what-it-actually-is-vs-the-pitch]] slightly **overcorrected**: it framed the product as "assisted tuning, *not* a click-a-threat auto-solver." Clicking a threat **does** auto-configure the spread. The genuine overclaim is narrower and survives: **"perfect stat spreads in seconds for *any team*"** implies a *holistic, whole-team, all-six-stats, one-click* optimizer. What exists is **single-breakpoint, one-target auto-config**, repeated by a human who composes the overall spread across Speed/Offense/Defense and manages the point budget. Logged as an ⚠️ overturn in [[pokesynergy-niche-business-tool/caveats-and-corrections]].

Other verified Stats-editor details:
- EVs are abstracted as **"Stat Points" (SP)**, **max 32 per stat**, not raw 0–252 EVs — a deliberate beginner-friendly simplification (the video's "shifting points"). Layout per stat = `[base] [SP] [final]` with `+/-` and **Nature boost/drop** toggles.
- **"STATS BY USAGE → Choose a usage spread (Top 4…)"** applies a real ladder spread = the **expert-defaults** move.
- One-tap archetype presets: **Slow / Neutral / Fast** and **Atk / SpA / Def / SpD / Bulk**.
- Field-state toggles (Tailwind, Trick Room) and a **"Meta threats 234/234"** count slider — the video's "threat filter / meta-threat count."
- Threat rows are richly explainable: each shows the threat's assumed spread, its **usage %**, its speed stat, and a plain-language verdict (*"Cannot outspeed with legal spread"*).

## Analysis — the "Synergy Score" is the product's real spine

The **Analysis** section states its own data scope: *"Synergy Score uses **M-B tournament priors** from the selected MetaDex tiers"* (Majors/Online scope toggle). It provides, at **whole-team** level:

- **Defensive & offensive type-gap** analysis (which types the team is weak to / can't hit) with suggested fillers;
- **support-move gap** coverage (Fake Out / Weather / Speed Control / Pivot / Redirect);
- "Weak to physical walls / special attackers" call-outs with named culprits;
- **Threat Analysis against real Top-8 tournament rosters** — e.g. a pinned "Top 8 ×6" team (Mega Aerodactyl / Mega Charizard Y / Farigiraf / Garchomp / Kingambit / Sylveon), with dozens more Top-8 rosters selectable.

This is materially more sophisticated than the wiki's "Weakness Checker / Type Chart" description.

## Calcs — a batch damage calculator against the whole meta

The **Calcs** view is not a 1-v-1 calculator; it runs your attacker against **327 opponents at once**, with full battlefield modeling (Singles/Doubles, weather Sun/Rain/Sand/Snow, terrains, Gravity/Magic Room/Wonder Room, and per-target effects like Burn/Reflect/Helping Hand). Each result is an **explainable KO verdict** — "Dragon Claw 2× **Guaranteed OHKO**", "Earthquake **79.7% chance to 2HKO**", "Poison Jab **No 4HKO**" — with opponent filters (Wall / Threat / Neutral / Mitigated / Crushed).

## The through-line: explainability on every surface

The single most transferable observation from touching the product: **every number is paired with a human-readable reason or verdict.** Move suggestion → "Team gap". Speed tier → "Cannot outspeed with legal spread". Damage → "Guaranteed OHKO / 90.6% chance to 2HKO". This is the exact ethos the wiki flagged as the best idea to steal, and it is pervasive, not cosmetic. See [[pokesynergy-niche-business-tool/hireui-translation]].

## Trust posture — confirmed hands-on

- **No login required** — the entire build → tune → analyze → calc flow worked signed out. "Sign in" is optional (cloud save).
- **No cookie/consent wall** appeared.
- A **Discord** invite is one click from every screen (the community funnel — see [[pokesynergy-niche-business-tool/distribution-deep-dive]]).

## Key Takeaways

- **The IA is 5 sections** (Teams/Team Builder/Speed/Analysis/Calcs); the "9 tools" list was a marketing-page artifact — [[pokesynergy-niche-business-tool/product-anatomy]] corrected.
- **The auto-configure claim is real** (verified: tap Mega Blaziken → Spe SP 0→31, rank #435→#204 live). The only true overclaim is the *holistic whole-team* "perfect spread for any team" framing — [[pokesynergy-niche-business-tool/what-it-actually-is-vs-the-pitch]] refined.
- **Expert-defaults and explainability are pervasive and verified** — usage-sorted picker, usage-% moves/abilities, "Team gap" reasons, KO verdicts, Synergy Score. This is the borrowable core for [[pokesynergy-niche-business-tool/hireui-translation]].
- **EVs are simplified to "Stat Points" (max 32/stat)** — a beginner-friendly abstraction worth stealing for any expert-tool-for-novices.
