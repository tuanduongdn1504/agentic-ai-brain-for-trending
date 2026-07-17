# N>1 Comparative Study — winner, incumbent, and the dead

*Deepening Axis 1, and the wiki's own prescribed homework: [[pokesynergy-niche-business-tool/critical-appraisal]] warned that studying only PokéSynergy is survivorship bias, and asked for "a 3-tool comparative study (a winner + an incumbent + a stalled tool) to see the pattern **and its failure modes**." This is that study.*

*Method: background Workflow `wf_adf65593` (5 web-research investigators + 3 adversarial verifiers, refute-first + schema'd) → **main-loop independent verification** of the two load-bearing claims (per wiki-verify). The workflow's auto-synthesis step failed on a schema cap; this synthesis is hand-built in the main loop, which is stricter anyway.*

## The census: the market is crowded and mostly alive

A competitive-Pokémon tooling census found **15+ active tools** — nearly all **free or donation-funded** (Ko-fi / PayPal / "Buy Me a Coffee"), most updated within weeks of July 2026:

| Tool | Category | Status | Monetization |
|---|---|---|---|
| Pokémon Showdown damage calc (`@smogon/calc`, ~2012) | damage-calc (foundational engine most others fork) | alive | free/OSS |
| Pikalytics | usage-stats + calc | alive (~9 yr) | ads + paid app + Ko-fi |
| ChampTeams.gg | builder + calc + "Battle Mode" | alive | free/Ko-fi |
| Porygon Labs | calc + builder (accounts, match history) | alive (v1.5.0) | free/Ko-fi |
| Champions Lab | battle simulator + AI recs | alive (Jul 14 2026) | free/donations |
| ChampDex | Champions-only builder + spread solver | alive (Jul 17 2026) | free |
| Showdex | in-battle browser extension | alive (v1.4.0, Jun 30 2026) | free/OSS |
| VGC Helper | mobile-first (iOS) | alive (v4.1.2) | unknown |
| ChampTeamAI | team generator + EV solver (explicitly *deterministic, no-LLM*) | alive (v3.2) | free |
| ChampCalc / Pokestats.cc / Hohou's Home / MunchStats / Terresquall | converters, dexes, optimizers | alive | free/donations |

**Implication:** automated EV optimization and damage calc are **commodity, and the market is saturated with free tools.** This *strengthens* [[pokesynergy-niche-business-tool/what-it-actually-is-vs-the-pitch]]: PokéSynergy can't win on the math (everyone has it) — its only defensible edge is **beginner-facing explainability + integrated workflow**. (Notably, Pikalytics *also* uses the "Stat Points" abstraction PokéSynergy uses — see [[pokesynergy-niche-business-tool/live-app-teardown]] — so even that UX choice isn't unique.)

## The three roles

| Role | Tool | Monetization | What it is | Why it's where it is | Portable lesson |
|---|---|---|---|---|---|
| **Winner** (new, growing) | **PokéSynergy** | free, monetization deferred | explainable beginner team-builder | rode the Apr-2026 Champions launch + content funnel; differentiates on UX/explainability | pick a *narrating* angle in a commodity market |
| **Incumbent** (survivor) | **Pikalytics** (~9 yr, since Nov 2017) | freemium — display ads + paid ~$5-10 iOS/Android app + Ko-fi | data-dense usage-stats platform for *experts* | **a revenue model (even tiny) + a format that forces data refresh + solo-sustainable side-project economics** | longevity comes from a *sustaining mechanism*, not popularity |
| **Dead — tool** | **VGC-Team-Sheets** (jake-white) | none | a VGC-2017 teamsheet generator | **format-locked**: built for Gen-7 VGC'17; last code push **2021-07-13** (verified via GitHub API), ~5 yr dormant, 4★; someone forked it to rebuild for 2023 | *format-locked tools die when the format dies* |
| **Dead — community** | **Nugget Bridge** | none | competitive-Pokémon community hub (2012–2016) | **hacked May 2016 → founder/community exit**; last post Dec 26 2016; now a static archive | *hubs die when the maintainer/community leaves* |
| **"False death"** (nuance) | **Trainer Tower calc** | free | VGC damage calc (2017–2020) | its **domain died** (`ENOTFOUND`) but the *tool migrated* to Nimbasa City Post (NCP), actively maintained w/ VGC-2026 support | *a tool can outlive its domain via migration/fork — a dead domain ≠ a dead tool* |

*(The false-death catch was made by an adversarial verifier that was told to refute — it proved Trainer Tower alive-by-migration. This is the anti-confabulation gate working; logged in [[pokesynergy-niche-business-tool/caveats-and-corrections]].)*

## Failure-mode taxonomy — what kills niche tools, and who it hits

Six documented modes, each mapped onto PokéSynergy and onto the operator's recruitment SaaS (hireui):

| # | Failure mode | Mechanism | Hits PokéSynergy? | Hits hireui? |
|---|---|---|---|---|
| 1 | **IP / legal takedown** | IP holder issues C&D/DMCA | **Partly** — a tool (not a fan-game) is lower-risk, but Nintendo brand risk exists and a solo founder has no legal budget | **No** — owns its data; no IP landlord (Uranium/Prism/Relic-Castle precedents don't apply) |
| 2 | **Platform/API churn** | a depended-on API/scrape target changes or dies | **No** — uses offline-first data snapshots | **No** — owns candidate/job data; "official keys, never OAuth" ADR |
| 3 | **Founder burnout / subsidy collapse** | solo maintainer loses time/funding/motivation | **YES** — solo, free, no revenue; YouTube subsidizes the time | **No** — revenue-bearing; maintenance is a funded business cost |
| 4 | **First-party absorption** | the platform ships an official version | **No** — Nintendo hasn't in 14+ yr of third-party calcs | **No** — not a platform feature |
| 5 | **Monetization collapse** | no viable revenue; costs outrun income | **YES** — zero disclosed monetization | **Partly** — execution risk, but the market pays (large TAM); risk is *how*, not *whether* |
| 6 | **Commoditization / clone glut** | many free look-alikes, no moat | **Partly** — 15+ free tools; differentiated on UX *for now* | **No** — differentiated by domain + candidate data + workflow |

*Documented cases behind the modes:* Pokémon Uranium (C&D 2016), Prism (C&D 2016, 4 days pre-release), Relic Castle (DMCA 2024); Twitch/Twitter-X API breakage killing Tweetbot/Twitterrific (2023); CocoaPods maintainer sunset (2026); indie studio closures.

**The punchline the operator needs:** the two modes that *actually* threaten PokéSynergy — **#3 subsidy collapse and #5 no-monetization** — are precisely the two hireui structurally avoids. Modes #1/#2/#4 don't hit either. Mode #6 hits PokéSynergy but not a differentiated B2B tool. So the comparative study **confirms the contrast in [[pokesynergy-niche-business-tool/business-model-and-risks]] empirically, at N>4**, not just by assertion.

## The N>1 verdict — what generalizes vs. what was survivorship bias

- ✅ **Generalizes (real pattern):** explainability-first UX in a commodity market is a genuine differentiator — the incumbent (Pikalytics) is *data-dense/expert-facing*, leaving the *beginner-narration* lane open, which is exactly the lane PokéSynergy took. The "collapse tool-hopping into one workspace" move is real.
- ✅ **Generalizes:** a **sustaining mechanism** (Pikalytics' tiny freemium + format-forced refresh) is what separates the 9-year survivor from the dead tools — *not* cleverness or virality.
- ⚠️ **Was survivorship bias:** "free tool → audience → monetize later" is a *timeline* only affordable to a subsidized founder. The dead leg (VGC-Team-Sheets) shows the default outcome — dormancy — for a free, solo, unsustained tool once its format moves on.
- ⚠️ **New caution the study adds:** the market is **already saturated** (15+ live tools). "Painful niche + build a tool" is necessary but not sufficient; you also need a lane no incumbent occupies **and** a sustaining mechanism. PokéSynergy has the lane; it does **not** yet have the mechanism.

## Corrections surfaced by this study (logged in [[pokesynergy-niche-business-tool/caveats-and-corrections]])

- **Pikalytics is ~9 years old (launched Nov 21 2017), not a "16-year incumbent"** as [[pokesynergy-niche-business-tool/what-it-actually-is-vs-the-pitch]] and [[pokesynergy-niche-business-tool/market-and-niche]] stated. Independently verified.
- **VGC-Team-Sheets' last code push was 2021-07-13** (GitHub API), not "May 2019" as the research agent first reported — a wiki-verify catch on our *own* deepening.

## Key Takeaways

- **The market is commodity + saturated (15+ live tools)** — reinforcing that the moat is UX/explainability, never the calc.
- **Survivor vs dead is decided by a sustaining mechanism**, not popularity: Pikalytics survives 9 years on a tiny freemium + format-forced refresh; VGC-Team-Sheets died format-locked and unsustained.
- **The two failure modes that threaten PokéSynergy (subsidy collapse, no-monetization) are the two hireui avoids** — the N>1 evidence upgrades [[pokesynergy-niche-business-tool/business-model-and-risks]] from assertion to demonstration.
- **A dead domain ≠ a dead tool** (Trainer Tower → NCP) — check for migration before pronouncing death.

Cross-links: [[pokesynergy-niche-business-tool/critical-appraisal]] · [[pokesynergy-niche-business-tool/business-model-and-risks]] · [[pokesynergy-niche-business-tool/what-it-actually-is-vs-the-pitch]] · [[pokesynergy-niche-business-tool/the-niche-tool-playbook]]
