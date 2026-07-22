# Caveats & Corrections

> Every non-plain-CONFIRMED verdict from Workflow `wf_dabc1f67-f9f`, with the corrected statement + sources. Scorecard: [[engineer-of-the-future/claims-scorecard]].

## Caption garbles fixed (mechanical)

Corrected silently in the articles: "re-bumbling" → **rebundling**; "Boris Cherney/Churnney" → **Boris Cherny**; "Michelle Hashimoto / Ghosty" → **Mitchell Hashimoto / Ghostty**; "Simon Willis" → **Simon Willison**; "Adam Wan" → **Adam Wathan**; "Armen Ronacher" → **Armin Ronacher**; "Andre Carpathy" → **Andrej Karpathy**; Peter Steinberger "2019" → garbled year (he shared a PR-review guide years ago; joined OpenAI **Feb 2026**).

## MISLEADING (1)

- **"Boris Cherny stopped opening his IDE / Opus 4.5 wrote every line of his PRs."** The exact quote — *"The last month was my first month as an engineer that I didn't open an IDE at all. Opus 4.5 wrote around 200 PRs, every single line"* — is **Hamel Husain's** (X post). **Boris Cherny only replied "I feel this way most weeks"** and did not make the original claim. Outlets misattributed it to "the Claude Code creator." Gergely Orosz's talk repeated the misattribution. *Source: x.com/HamelHusain/status/2004670741623845026.* → The *phenomenon* (senior engineers barely touching an IDE) is real and multiply-attested; the *specific attribution* to Cherny is wrong.

## UNVERIFIABLE (2)

- **Ng's "Federal Reserve Bank of Philadelphia study."** No source confirms Ng cited a specific Philadelphia Fed study. His documented citations for the "no job apocalypse" case are **Jevons paradox, BLS 15%-growth-through-2034 projections, and James Bessen's ATM-teller research.** Treat the Philadelphia-Fed attribution as unconfirmed (likely a caption/memory slip).
- **"Star Wars premiered at what is now Cursor's office."** The premiere (Northpoint Theatre, 2290 Powell St, SF, May 1977) and the **Dykstraflex** are real, and a developer *did* buy that building — but there is **no evidence Cursor operates from it** (verified Cursor HQ = 33 New Montgomery St). Presented as a rhetorical framing, not a verified fact.

## CONFIRMED-BUT-IMPRECISE (21) — corrections

**Osmani / conference**
- Keynote's **official title** = **"Don't build agents you can't answer for."** The quoted line ("the engineer of the future…") is a prominent theme, not the title. Conference = **AI Engineer World's Fair 2026 (AIEWF)**, June 29–July 2 2026 — not "AIE."
- **Dex Horthy** talk = **"Harness Engineering is not Enough: Why Software Factories Fail"** (HumanLayer). Osmani discussed the same ideas in a parallel essay ("Software Factories, Light and Dark"), not as a direct citation of Dex's talk — complementary, mildly contrasting views.

**Cherny taxonomy**
- Archetype names are **Prototyper / Builder / Sweeper / Grower / Maintainer** (noun "-er" forms), from Cherny's **June 28 2026** Threads/X post. "Rebundling around the work" is **secondary-commentary paraphrase**, not Cherny's own phrase; his framing: roles "melt away from job titles" and reorganize around work phase/type.

**Taste**
- **Mitchell Hashimoto's** definition is *"the ability to **consistently** make high-quality qualitative judgments where no objective metric exists"* — the transcript dropped **"consistently"** and added "yet."

**Wharton study**
- Shaw & Nave, *"Thinking, Fast, Slow, and Artificial"* (Jan 2026; 1,372 participants, ~10,000 trials). **73% = "cognitive surrender"** (accepted wrong answers) — the researchers' own term; **80%** is the broader "followed the wrong answer" figure. Confidence rose **~11.7–12 pp** even when the AI was wrong. "Borrowed confidence" is Osmani's characterization, not the paper's label. *(Osmani's failure-mode #2 name matches the paper's term.)*

**Andrew Ng**
- Precise quote: **"100% of my tasks now run through AI agents"** (tasks broadly), though in-talk he clearly extends it to coding. AI Dev 26 = ~April 28–29 2026.
- PM-ratio: the video's "1 PM ⇄ 8 engineers" ≈ Marty Cagan's classic ~**1:6–10**; some reports frame Ng's proposed direction as **~2 PMs per engineer** rather than a literal 1:1. The *direction* (PM work becomes the constraint; roles merge into generalists) is confirmed.
- **Context Hub** is real (open-source, ~March 2026, up-to-date docs for agents). **Contributor names are uncertain** — one source lists different names than the transcript; attributed here as "Ng and colleagues," not pinned.
- **"Code Dream" / "Code Realm"** learning product — **no product by that name could be found**; treated as unconfirmed (possible caption garble / very new).

**OpenAI API**
- **Chat Completions is NOT deprecated** — it remains actively supported indefinitely. The **Responses API** is newer and recommended *for new projects*. Ng's practical point (agents on old training data default to the older API) is valid; the word "deprecated" is inaccurate.

**Karpathy**
- **MenuGen** domain = **menugen.app** (not menu.app). His point was infra/config overhead (browser tabs, API keys, auth, payments, deploy) dominating time — phrased as "most of the work was not code," slightly softer than "far harder than the coding."
- **Vercel/Stripe** serve Markdown to agents via **content negotiation (Accept headers)**; the "replace *click here* with curl" is illustrative, not a literal doc-text substitution.

**Cursor**
- Browser experiment = **"FastRender"**: hundreds of GPT-5.2 agents, ~1 week, ~3M LOC — but used a **Planner/Worker/Judge agent hierarchy** (so "no humans" ≠ "no oversight"); maintainability **~1.3/5**; explicitly nascent.
- Senior-engineer amplification research = **Suproteem Sarkar (University of Chicago)**, not "Eric" (Eric Zakariasson is a Cursor engineer, not the researcher). Finding confirmed (~39% more PRs merged, no revert-rate rise).

**Gergely Orosz**
- Author of the **book** *The Software Engineer's Guidebook*; **"The Pragmatic Engineer" is his newsletter**, not a book. Bio (Uber/Skyscanner/Microsoft-Skype/JP Morgan) correct.
- **Kent Beck** ~**50 years in computing** counts from 1979 CS education; strictly *professional* programming is ~30+ years.
- **Martin Fowler** is the **primary author** of *Refactoring* (1999) with co-authors (Beck, Brant, Opdyke, Roberts); "authored" is fair but not sole.
- **Armin Ronacher** = **one of the first engineers hired at Sentry** (later Principal Architect), not strictly a "founding engineer."
- **Adam Wathan** = **one of four creators** of Tailwind CSS (with Reinink, Hemphill, Schoger); most visible (CEO, Tailwind Labs).

**LangChain**
- **Meta-Harness** = **Stanford-led** (Yoonho Lee, Roshen Nair, Qizheng Zhang, Chelsea Finn) with **one MIT co-author** (Omar Khattab) + Kangwook Lee (KRAFTON); arXiv **2603.28052**, Terminal-Bench 2 76.4%. "MIT and Stanford" overstates MIT's share.
- **LangSmith Fleets** "~200 built-in tools" count is **unverified**; Arcade **7,500 tools**, MCP support, and **Deep Agents** harness are confirmed.
- OpenAI native speech-to-speech "v2" = **GPT-Realtime-2, released May 7 2026** (early summer, not "mid-2026").

## Key Takeaways

- **1 MISLEADING** (Cherny/Hamel-Husain misattribution) + **2 UNVERIFIABLE** (Ng's Philadelphia-Fed study; Cursor-office-as-Star-Wars-venue) are the only non-imprecision issues; **0 FALSE / 0 FABRICATED.**
- All 21 CBI items are attribution/figure/name precision — corrected above; the underlying ideas stand.
- Discard-as-garble guard honored: date-sensitive claims (Opus 4.5 / GPT-5.2 dates, Steinberger→OpenAI, GPT-Realtime-2) were **search-confirmed true**, not dismissed as garble.

## See also

- [[engineer-of-the-future/claims-scorecard]] · [[engineer-of-the-future/source-provenance]]
