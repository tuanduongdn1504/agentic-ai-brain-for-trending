# ⭐ The Niche-Business-Tool Playbook

*The operator's payload: "inspire from it and make business tools like this." This is the extraction — 6 transferable moves, each with the move, why it works for PokéSynergy, and how to port it. What's Pokémon-specific is called out at the end.*

---

## Move 1 — Problem selection: a painful, recurring, multi-tool manual optimization inside a passionate niche

Pick a task that is (a) **repeated often** by many practitioners, (b) today requires **switching between 3+ tools + tribal knowledge + manual tweaking**, (c) has a **real failure cost**, and (d) is done by people **passionate enough to tell friends** about a good solution.

**PokéSynergy fit:** building a competitive team means hopping Showdown → multiple damage calculators → LimitlessVGC for threats → a spreadsheet to tweak EVs → re-test, ~5–10 loops = 1–2 hrs per team; failure cost = tournament loss; audience = obsessive VGC players.

**Port:** ask of your domain — what do users repeat weekly? which tools do they juggle? what tribal knowledge gates it? what's the cost of getting it wrong? are they passionate enough to evangelize?

---

## Move 2 — Core product move: collapse "tool-hopping + spreadsheet tweaking + re-testing" into click-to-tune with live feedback

Don't ship *another calculator*. Ship an **interactive constraint workspace**: the user states a goal/threat, the tool adjusts the variable and **re-renders instantly** (no "Calculate" button), and they can **lock** constraints so later moves don't undo them.

**PokéSynergy fit:** click "survive Wave Crash" → points shift → instantly see if you now survive; lock Speed; click "outspeed Meowscarada" → re-render. The tool does the arithmetic; the human keeps the strategy. *(Nuance: the live site frames this as an assisted edit-check-edit loop, not a one-click auto-solver — see [[pokesynergy-niche-business-tool/what-it-actually-is-vs-the-pitch]].)*

**Port:** identify your domain's *optimization variable* and *breakpoints*. Recruitment → requirement weights / thresholds; breakpoints = "pass the screen with 0 false-negatives", "≥3 yrs backend", "in-budget salary". See [[pokesynergy-niche-business-tool/hireui-translation]].

---

## Move 3 — Encode expert knowledge as defaults ("auto-build") so a novice gets an expert-grade result

Give one button that fills the hard parts from **best-practice / live-meta data**, then let the user override. Novices start at expert-grade; experts skip it.

**PokéSynergy fit:** "auto-build" seeds moves/item/spread "from the top spreads people are using" (drawn from tournament results). A beginner gets a tournament-winning starting point.

**Port:** find your *expert-defaults data source*. If you **own** it (your own successful hires, your prior approved designs), that's a moat competitors can't copy. If not, use public/community data (PokéSynergy uses LimitlessVGC).

---

## Move 4 — Progressive disclosure: a one-click fast path + a power-user deep mode

Bifurcate the UI: a beginner path (one click per goal, no options) and a deep mode (all parameters exposed). Both reachable; user picks.

**PokéSynergy fit:** Speed Tiers (click, see if you outspeed) = fast; Damage Calculator (weather/terrain/item/ability/modifiers) = deep.

**Port:** each domain has an "obvious decision" and a "deep tuning." Surface both. Recruitment → "show me who passes" (fast) vs "configure per-skill thresholds, weights, tolerances" (deep).

---

## Move 5 — Content-led distribution: demonstrate the pain→fix to the *exact* audience → app → community feedback loop

Make a screen-share that **shows the old pain then the new fix**, aimed at the precise niche; link to the app + a **Discord**; let the community become your QA + feature-request engine; iterate in public.

**PokéSynergy fit:** an 11-min demo (336 views — but *alignment beats scale*; every viewer is a target user) → app link → Discord bug reports/feature requests → next video shows the new feature. Multiple videos angle the same tool ("The Best Tool in Competitive Pokemon", "The ONLY App Beginners Should Use…").

**Port:** find where your niche consumes content (LinkedIn/Slack/Reddit for recruiters), demo the pain, funnel to app + community. ⚠️ This requires being the *builder-in-public voice* — not every founder wants that. And note the survivorship caveat in Move-6 / [[pokesynergy-niche-business-tool/critical-appraisal]].

---

## Move 6 — Ship fast, iterate in public, be honest about bugs and roadmap

Release at ~70% coverage; **publicly list known bugs + upcoming features**; show a roadmap; be transparent about scale ("built by one person part-time"). Honesty builds trust; hidden roadmaps read as abandonment or an incoming paywall.

**PokéSynergy fit:** the video openly names bugs and coming features; the site defers monetization transparently.

**Port:** a changelog + public roadmap + a "solo, part-time" honesty badge. Cheap; disproportionately trust-building.

---

## What's replicable vs Pokémon-specific

**✅ Replicable (any domain):** problem-selection filter · click-to-tune UX · expert-defaults · progressive disclosure · content-led distribution · public iteration.

**❌ Pokémon-specific (can't port):** the domain math (damage formulas, type chart) · the data source (LimitlessVGC/Showdown) · the community + its channels · the threat vocabulary.

## Seed: the recruitment analogue

The pain is *structurally identical*: recruiters manually review 200 CVs in a spreadsheet, run separate skill-match tools, search comps, second-guess rejections, and lose half-qualified candidates to false negatives. The tool: click "show candidates meeting all hard constraints" → deterministic re-rank by fit → click "relax Python to 2 yrs" → pool expands live, false-negative impact shown → power mode tunes per-skill weights → **the moat is explainability + your own hires as defaults, not the algorithm.** Full, ADR-safe sketch in [[pokesynergy-niche-business-tool/hireui-translation]].

## Key Takeaways

- The playbook is a **shape**, not a recipe: painful manual optimization → click-to-tune → expert defaults → progressive disclosure → content distribution → public iteration.
- The **durable moat** is *explainability + a proprietary defaults corpus*, not a clever algorithm (which competitors can and did replicate — see [[pokesynergy-niche-business-tool/what-it-actually-is-vs-the-pitch]]).
- Two moves carry hidden costs: distribution demands a builder-in-public temperament; and "iterate slowly in public" only works if something **subsidizes** the founder (see [[pokesynergy-niche-business-tool/critical-appraisal]]).
