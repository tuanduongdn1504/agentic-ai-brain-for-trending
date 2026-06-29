# Pillar 1 — Let Claude Interview You (Bitter Lesson)

## Source

Workshop transcript ([IlqJqcl8ONE](https://www.youtube.com/watch?v=IlqJqcl8ONE) ~04:00–10:00) + `phase-1-exploration/PROMPT.MD` + Thariq Shihipar's interviews (ChatPRD, Lenny's). The **Ask User Question** tool confirmed in [[how-we-claude-code/claude-code-primitives]].

## Bad prompting vs. good prompting

- ❌ **Bad:** *"Just make it better."* Arno: *"A lot of people that I watch using Claude code just type 'make it better.' … that's not good prompting."*
- ✅ **Good:** *"Encourage Claude to extract from you specific details. Give the domains. Don't over-specify the outcome, but specify the areas that you are interested in."* — e.g. name the audience, leave answers open-ended, and let Claude **iteratively interview** you.

## The Bitter Lesson framing

Arno invokes **Richard Sutton's "The Bitter Lesson"** (2019): general methods that leverage computation beat hand-engineered human knowledge. His analogical extension:

> *"You should accept that the model is probably better at extracting requirements from you than you are at defining your requirements. The requirements are latent within you, just like when you talk to your users. … you probably know what you want when you see it, but Claude is likely better at extracting what you want and what you need from you than you are in specifying it to Claude."*

The motivation is economic: **longer agent runs make a wrong spec expensive.** *"The longer you let an agent run, the more important it is that the spec is comprehensive, the less likely it is that you will be able to up-front define everything."*

> ⚠️ **Honest caveat (flagged in deep-dive):** the *"model extracts requirements better than you"* line is **Arno's analogy, not something Sutton wrote.** Sutton's lesson is about *means* (don't hand-engineer features; let search/learning find them) on problems with a **fixed objective and ground truth**. Requirement-*definition* is about *ends* and has **no ground truth** without you. A fair reading: *use the interview to surface latent requirements collaboratively* — not *"trust the model to decide what you want."* You still own the objective. See [[how-we-claude-code/caveats-and-when-not-to-use-html]].

## How it works in practice (phase 1)

`phase-1-exploration/PROMPT.MD` (verbatim):
> *"I want to build a bill-splitting app, can you help me brainstorm with me on who the audience is, and then interview me in-depth using the AskUserQuestion tool about what to build, focusing on pulling out any ambiguities to create a spec."*

- The literal trigger is **referencing the AskUserQuestion tool in your prompt.** Claude then presents tap-through multiple-choice questions (audience? secondary audience? edge cases?) and writes the spec from your answers.
- Thariq's independent phrasing: *"The magic word for prompting is **'interview me.'**"* He says it clicked with **Opus 4.5+** ("with Sonnet it just wasn't as good").

## Key Takeaways

- **Specify *areas of interest*, not the finished outcome** — then let Claude interview.
- The literal mechanism is the **AskUserQuestion tool**; the magic words are *"interview me"* / *"use the AskUserQuestion tool."*
- Rationale is cost: a comprehensive, interview-derived spec prevents long agent runs from going the wrong way.
- **You still own the objective.** The Bitter Lesson analogy is directionally useful but over-reaches if read as "the model knows what you want better than you do."
- Pairs naturally with vault **Rule 1 (Think before coding) / "grill-me"** patterns and [[../workflow-ai-coding/_index]].
