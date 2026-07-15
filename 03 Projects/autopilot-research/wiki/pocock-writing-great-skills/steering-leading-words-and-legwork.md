# Steering: leading words + legwork

Pocock calls steering "the main thing I want you to get from this talk." Two levers.

## Leading words

- **Definition:** words that "pack a bunch of meaning into a very small space." You put the leading word in the skill text; the agent **repeats it back in its reasoning/thinking tokens and its output**, and because the word encodes the behaviour you want, re-emphasising it steers the agent.
- **The literary root — "Leitwort":** Pocock says "leading words, or *[light vert]* if you like literary theory." The auto-caption "light vert" is a garble of **Leitwort** (German, "leading word") — the literary-theory term (Leitwortstil, popularised by Martin Buber's Bible translation) for a keyword deliberately repeated to anchor a theme. ✅ Confirmed real term; Pocock himself has posted about *Leitwörter* in skill design ([x.com/mattpocockuk](https://x.com/mattpocockuk/status/2066922013000671731)). See [[pocock-writing-great-skills/caveats-and-corrections]].
- **The example — "vertical slice":** rather than "don't code layer-by-layer," use the leading word **"vertical slice."** It's well-established dev terminology (a slice through every layer — UI→DB — delivering one thin complete feature; the opposite of horizontal/layer-by-layer), so it **triggers the model's priors**. ✅ "Vertical slice" confirmed as canonical Agile/dev terminology.
- **Verification by reasoning trace:** "you can know if it's worked because you say vertical slice in your skill, and then you'll notice in the reasoning traces that it's saying 'we're going to do this as a thin vertical slice.'" A sound, observable heuristic — reasoning models echo salient prompt vocabulary.
- **Repo note:** the published `writing-great-skills` GLOSSARY defines "Leading Word" ("compact concept leveraging the model's pretraining… through repetition") and its own canonical examples are **"tight"** and **"red"**, not "vertical slice" — the talk's example is illustrative; the repo's are its house examples. (This talk-vs-repo example difference is why a verify agent flagged CL7 before the main loop confirmed the technique + terminology are both real — see [[pocock-writing-great-skills/caveats-and-corrections]].)

## Legwork per step

- **The problem:** an agent under-invests effort on a step when it can *see the future goal* — it does a little and rushes to the goal.
- **The classic case — plan mode:** plan mode has two steps, "ask clarifying questions" then "create a plan." Because the ultimate goal (a plan) is visible, the agent does a tiny bit of clarifying and eagerly jumps to the plan. Pocock says this happens in "every single implementation of plan mode I've tried." *(This is a practitioner observation, not documented Anthropic behaviour — a reasonable hypothesis about goal-visibility driving premature convergence; rated CONFIRMED-as-his-claim, plausible in general.)*
- **The fix — split into separate skills so the agent sees one step at a time:**
  - **`grill-with-docs`** = the clarifying-questions/interview phase, as its *own* skill. ✅ Confirmed: description *"A relentless interview to sharpen a plan or design, which also creates docs (ADRs and glossary) as we go"*; body *"Run a `/grilling` session, using the `/domain-modeling` skill."*
  - Then, only after it completes, **`2PRD`/`to-spec`** does the planning. ✅ Confirmed: `to-spec` explicitly says *"Do NOT interview the user — just synthesize what you already know"* — i.e. the interview was already done by `grill-with-docs`. The two skills enforce the ordering by each refusing the other's job.
  - Because the agent running `grill-with-docs` **can't see the future planning step**, it does the full interview legwork.
- **When to use it:** "not always necessary to split skills into individual steps, but in cases where you really want an extra chunk of legwork, there's no technique like it."

## Corpus ties

- The **legwork split** is the skill-level implementation of [[how-we-claude-code/_index]]'s "interview-first" instinct and [[pocock-real-feature-build/_index]]'s grill→plan pipeline front half.
- **Leading words** are the prompt-level lever under [[system-thinking-ai-coding/_index]]'s "design before you prompt" and [[pocock-agentic-workflow/_index]]'s procedures-over-abilities worldview.
- Pilot application (leading words in hireui/vault skills; the grill→spec split for the autopilot routine): [[pocock-writing-great-skills/hireui-and-vault-pilot]].
