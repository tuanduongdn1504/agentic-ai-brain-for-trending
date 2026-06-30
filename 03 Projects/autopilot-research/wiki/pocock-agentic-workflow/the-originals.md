# The originals — who originated what

## Source

Provenance of every external idea/resource cited in [nQwJVHCtDDY](https://www.youtube.com/watch?v=nQwJVHCtDDY), deep-dived against primary sources via Workflow `wf_4562f245-5bc` + `gh api` / WebFetch ground-checks. Corrections are flagged ⚠️.

## John Ousterhout — *A Philosophy of Software Design*

- **Who:** Stanford CS professor; creator of **Tcl/Tk**; co-inventor of the **Raft** consensus algorithm (with Diego Ongaro, 2014); led the Sprite OS / log-structured filesystem work at Berkeley; founded Scriptics and Electric Cloud.
- **What Matt borrows:** **tactical vs strategic programming**, from **Ch. 3 "Working Code Isn't Enough"** (§3.1 Tactical, §3.2 Strategic, §3.3 "How Much to Invest?"). Tactical = quick + shortcut-laden + complexity-accruing; strategic = continual small investment in good design (~10–20% of dev time). Book: 2018, 2nd ed. 2021, ~180pp.
- ⚠️ **Correction:** the book **predates LLMs and says nothing about AI/agents.** "AI ate tactical programming," the soldier/general metaphor, and "infinite fleet of tactical programmers" are **Matt's extensions**, not Ousterhout's. Auto-subtitle "John Asterout" → **Ousterhout**.

## Geoffrey Huntley — the Ralph loop

- **Who:** Geoffrey Huntley (**not** "Jeffrey"; X/GitHub `@ghuntley`). Software engineer who publishes AI-development research.
- **What:** **"Ralph Wiggum as a software engineer"** ([ghuntley.com/ralph](https://ghuntley.com/ralph/), **14 July 2025**). A deliberately naive bash loop — `while :; do cat PROMPT.md | claude-code ; done` — that re-runs a coding agent against the **same prompt file** each iteration, using the **file system as state** instead of the context window. **Greenfield-only** by design; single-agent (not multi-agent). Famous example: a ~$50k contract delivered as a tested MVP for ~$297. Companion repo [ghuntley/how-to-ralph-wiggum](https://github.com/ghuntley/how-to-ralph-wiggum) (1,707★, created Jan 2026). Follow-up: ["everything is a ralph loop," ghuntley.com/loop](https://ghuntley.com/loop/) (17 Jan 2026).
- ⚠️ **Stripped fabrications** (deep-read confabulations not in the primary source): a "$10.42/hour Sonnet" operating cost; "previously worked with **Steve Yegge at Sourcegraph**" (Yegge's "Welcome to Gas Town" is cited only as a *conceptual* reference, not employment history); a naming origin story about it "making him want to *Ralph* (vomit)"; a "Ryan Carson 865K-view" virality stat. None appear in ghuntley.com — **excluded.**

## Peter Steinberger — loop-engineering popularizer

- **Who:** Peter Steinberger (**not** "Stanberger"; X `@steipete`). Austrian dev, founder of **PSPDFKit**, creator of **OpenClaw**, now at **OpenAI**.
- **What:** popularized "**stop prompting your agents; design loops that prompt your agents**" on X (~June 2026), which catalyzed the "agentic loops" wave David references.
- ⚠️ **Correction:** **popularizer, not originator** — Ralph (July 2025) predates the June-2026 virality by ~a year. David's hedge "if I'm not mistaken" was warranted. Tweet view-counts (e.g. "6.5M") are **X-gated and unverified** — don't cite a number.

## Richard Sutton — *The Bitter Lesson*

- **Who:** Richard S. Sutton, RL pioneer (TD-learning), Univ. of Alberta professor, **2024 ACM Turing Award** co-winner with Andrew Barto.
- **What:** [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) (March 2019): general methods that scale with **compute** (search + learning) beat hand-engineered domain knowledge — shown across chess (Deep Blue), Go (AlphaGo), speech, vision.
- ⚠️ **Scope note:** the essay is about **algorithmic means on fixed-ground-truth problems**, *not* about execution discipline. So Matt's worry ("am I falling into the Bitter Lesson by optimizing my harness?") is **miscalibrated** — harness work ≠ hand-engineered domain knowledge — and his conclusion (optimize the harness AND expect better models) is actually *compatible* with Sutton. The same essay appears in [[../how-we-claude-code/_index]] used as a looser analogy.

## obra / superpowers — the model-in-control counterpoint

- **Who/what:** **[obra/superpowers](https://github.com/obra/superpowers)** by **Jesse Vincent** (Prime Radiant). MIT, **241,675★**, ~13+ skills across 11 agent platforms; skills **auto-trigger** by default.
- **Verified:** Matt's "**probably the most popular skills repo**" is **correct** — superpowers has **~60% more stars** than his own `mattpocock/skills` (150,757★).
- ⚠️ **Correction:** "**opposite** approach" overstates it. Both support model-invocation; superpowers **defaults** to auto-trigger (model-in-control), Matt **defaults** to user-invoked and lets you opt in. Different defaults, same tooling layer. Transcript "Opera" → **obra**.

## Lev Vygotsky — Zone of Proximal Development

- **What:** ZPD = the gap between what a learner can do **alone** vs. **with guidance** (scaffolding gradually removed). A foundational, heavily-cited concept in educational psychology, originated by **Lev Vygotsky** (1896–1934).
- **Verified:** Matt's **teach** skill **explicitly** encodes ZPD and the Knowledge/Skills/Wisdom split in its `SKILL.md` ("These should be used to calculate the zone of proximal development"). The "Knowledge/Skills/Wisdom" trichotomy is Matt's informal framing (adjacent to the DIKW pyramid), not a single canonical source.
- ⚠️ **Correction:** a specific "101,000 citations" figure was a deep-read fabrication — drop the number; "one of the most-cited concepts in educational psychology" is the safe claim.

## aihero.dev — Matt's platform

- **Verified:** [aihero.dev](https://www.aihero.dev/) is Matt's AI-engineering education site (free guides + a **70,000-developer** "Skills" newsletter + paid workshops, e.g. an AI SDK course ~$149). **[aihero.dev/skills](https://www.aihero.dev/skills)** exists and documents ~9–11 skills (grill-me, grill-with-docs, domain-model, to-prd, to-issues, tdd, triage, handoff, prototype, improve-codebase-architecture, review). `aihero.dev/posts` 404s on fetch — **don't fabricate blog content.**
- ⚠️ **Correction:** the "we're hiring" link in the *video description* is **David Ondrej's** company **Scale Software** (scalesoftware.ai, Katowice) — **not Matt's**, and **unrelated to Scale AI** (scale.com, SF). Matt operates **independently**.

## Peripheral tools (sponsors / mentions)

- **Wispr Flow** (podcast says "Whisper Flow") — AI voice dictation Matt uses (wisprflow.ai). **Glaido** (glaido.com, by indie dev **Jack Roberts**) — David's dictation tool; the `get.glaido.com/david-ondrej` link is an affiliate, not David's product. **SerpApi** — the video's paid sponsor (search-results API, 250 free credits).

## Key Takeaways

- **Ousterhout (tactical/strategic)** and **Sutton (Bitter Lesson)** are real and correctly cited; the **AI applications** of both are Matt's/the speakers' extensions, flagged accordingly.
- **Ralph = Geoffrey Huntley, July 2025**, file-as-state, greenfield-only; **Steinberger popularized** loops (June 2026) but didn't originate them.
- **superpowers (obra/Jesse Vincent)** really is more popular than Matt's repo; "opposite approach" is an overstatement (different defaults).
- **teach genuinely encodes ZPD + Knowledge/Skills/Wisdom** (verified in SKILL.md).
- **Scale Software is David's, not Matt's** — a correction that matters for attribution.
