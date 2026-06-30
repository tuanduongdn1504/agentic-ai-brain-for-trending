# Strategic vs tactical programming — your edge over the fleet

## Source

The opening framework of [nQwJVHCtDDY](https://www.youtube.com/watch?v=nQwJVHCtDDY), built on **John Ousterhout's** book ***A Philosophy of Software Design***. (The transcript's auto-subtitles mangle his name to "John Asterout"; the correct spelling is **Ousterhout**.) Deep-dive of the original: [[pocock-agentic-workflow/the-originals]].

## Ousterhout's distinction (the primary source)

From **Chapter 3, "Working Code Isn't Enough"** of *A Philosophy of Software Design* (Ousterhout, 2018; 2nd ed. 2021; ~180pp):

- **Tactical programming** — the short-term mindset: get the feature working *now*, accept "a few shortcuts and kludges." It's fast, and it **accumulates complexity** that compounds into bad design. Ousterhout's label for someone stuck here: the **"tactical tornado."**
- **Strategic programming** — make a *great design* the primary goal, via **continual small investments** in code quality. Slower per-feature up front; it pays for itself in long-term velocity. Ousterhout suggests spending on the order of **10–20% of development time** on design quality.

> ⚠️ **Attribution note.** Ousterhout's 2018 book is about *human* software design — it does **not** mention AI or agents. The application below (AI = tactical, human = strategic; the soldier-vs-general metaphor) is **Matt Pocock's own extension**, not Ousterhout's. Ousterhout is also a Stanford CS professor, creator of **Tcl/Tk**, and co-inventor of the **Raft** consensus algorithm.

## Matt's AI extension

- **"AI has basically eaten tactical programming. It's gone."** The actual writing of code, the syntax wrangling, the bug-by-bug grind — AI does it cheaper than you.
- **So you must be great at *strategic* programming** to get value from "this **infinite fleet of tactical programmers** you now have access to." Strategic programming hasn't changed: instead of delegating to junior/mid devs, you delegate to AI. The skills are the same —
  - **design the hard parts up front**
  - **scope tasks tightly**
  - **think about the interfaces between modules**
  - **design good tests / test scenarios**
  - **build a codebase that's easy to work in**, with **just enough documentation** to point the AI to the right places.
- **The general at the top of the army.** Strategic programming is "winning the war, not the battle" — how the codebase needs to look, what strategies raise velocity. Tactical is the day-to-day on the ground.

## "Your skills are the ceiling on what AI can do"

- **AI makes a senior ~10× and a junior a little.** A senior can oversee the codebase, decide how things should be built, and hand the AI rich context — so the AI's output is far better. A junior can't supply that context, so the multiplier is small. (Matt notes CTOs tell him this constantly: "it doesn't make sense to hire that many juniors anymore.")
- Therefore **getting good with AI = getting good at your domain.** "A better teacher can use AI to teach better than a random can." The model amplifies whatever judgment you bring; it doesn't manufacture judgment you lack.
- **Don't delegate your thinking.** Pull *more* of the strategy into your own head; delegate only the tactical execution. The temptation to "delegate everything to AI" is the trap — "you really can't."

## Knowledge / Skills / Wisdom

Matt's trichotomy for getting good at *anything* (his own informal framing, adjacent to but not the same as the **DIKW** pyramid; he encodes it literally into his **teach** skill — see [[pocock-agentic-workflow/skills-procedures-vs-abilities]]):

- **Knowledge** — the fundamental understanding in your head ("what is this thing").
- **Skills** — having done it enough times that it's muscle memory.
- **Wisdom** — knowing *when* to do it and how it fits the real world. **Wisdom is nearly impossible to get without doing the thing in the exact context** — you can gain Anthropic-level knowledge and skills from outside, but you'd have to *be at Anthropic* to gain the wisdom.
- The exciting part of this era: you can now **bundle Knowledge + Skills into reusable, distributable artifacts** (skills) — pulling a repeated procedure out of your own head the way you'd extract a duplicated function. "You raise the floor on what engineers can do."

## Who wins — the senior or the AI-native junior?

David presses: a 15-year senior who gets a 10× boost, *or* a younger AI true-believer who knows every tool but has less experience? Matt's answer:

- **"Enthusiasm beats experience"** in pure output — great juniors who are excited learn and ship faster. Hiring great enthusiastic juniors has always been the goal.
- But the **senior brings DX/AX judgment** (how to build a codebase that works well for humans *and* agents). The ideal is an **experimental mindset + excitement about the harness**, which can live in either a junior or a senior.
- The thing that's *gone*: "you can't be a **code monkey** anymore" — a purely tactical plumber. You have to think strategically; seniors can, and juniors can learn to.

## Key Takeaways

- **Tactical (writing code) is now AI's job; strategic (designing the system) is yours.** Ousterhout's framework, applied to the agent era — the AI extension is Matt's, not Ousterhout's.
- **Strategic programming hasn't changed:** scope tightly, design interfaces, write good tests, keep the codebase legible, document just enough to aim the agent.
- **Your skills are the ceiling.** AI multiplies a senior far more than a junior because the senior supplies richer context. Upskill the human; don't delegate the thinking.
- **Knowledge + Skills are now bundle-able** into shareable skills; **Wisdom still requires being there.**
- **Enthusiasm beats experience for output**, but strategic judgment is the durable moat — and "code monkey" tactical-only work is the role that disappears.
