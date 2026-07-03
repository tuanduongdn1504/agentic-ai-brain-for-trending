# Grill-me in practice — anatomy of a live requirements interrogation

## Source

- Transcript `raw/2026-07-03-pocock-real-feature-build.md` (first ~22 minutes of [hX7yG1KVYhI](https://www.youtube.com/watch?v=hX7yG1KVYhI)).
- Skill verified in [mattpocock/skills](https://github.com/mattpocock/skills) — `skills/productivity/grill-me/SKILL.md` (see [[the-originals]]).

## How the session actually runs

1. **Dictate the rough idea, unpolished.** "Notice how rough this is… just spewing out to the LLM and making it do all the work." Two pain points + one new concept (ghost courses), dictated, typos and hedges included.
2. **Always explain the WHY.** Matt catches himself giving only the what: "if it doesn't know the why, it can't suggest alternatives." He adds: *"The reason I want this is so that I can plan courses freely without needing to commit to an exact shape on the file system."*
3. **The skill explores before it asks.** First move is an Explore-subagent pass over the codebase. First question back is a **framing challenge grounded in code**: "`deleteLesson` in course-write-service already handles both ghost and real… is there something in the UI that forces the convert-then-delete flow?" — the pain point was a *UI gap*, not a service gap.
4. **One question at a time, each moving the model forward.** Highlights from the session:
   - "When you say a ghost course could have *real* lessons, what does real mean without a file system?" (forces precision on woolly language)
   - "Does direct-create apply inside ghost courses too?" (Matt: "that's such a Willow Reagan question" — his old lead-dev mentor who could "ask smart questions for hours")
   - The **hysteresis edge case**: delete all real lessons from a real course — does it become ghost again? (Matt: "No. Once a course has a file path, it stays real forever." — "super glad it asked; now it's in the context and spelled out")
5. **Model trade-offs WITH the LLM, not in your head.** For create-lesson-in-ghost-course he asks for the trade-offs of option A vs B, agrees with its recommendation (A), and notes: "instead of me thinking about this in my own head, which is not particularly fun viewing…"
6. **Push back when it's wrong.** It claims there's no test harness for the course-write-service. Matt: **"Look harder."** It finds the e2e suite. — the correction pattern: don't accept, don't rage-quit; re-instruct with higher effort.
7. **Converge to an explicit scope list.** The session ends with 8 bullet points ("the eight bullet points we just spent 22 minutes trying to get") that he confirms line by line.

## Deliberate design choices in the skill (verified against SKILL.md)

- **`disable-model-invocation: true`** — grill-me is a *procedure* (user-invoked), consistent with the procedures-vs-abilities doctrine in [[../pocock-agentic-workflow/skills-procedures-vs-abilities]].
- **Two-tier architecture**: a user-invoked dispatcher that delegates to a model-invocable grilling sub-skill.
- **Code-first answering, verbatim rule:** "If a question can be answered by exploring the codebase, explore the codebase instead" — confirmed in the skill text.
- **No AskUserQuestion tool.** Matt's two reasons: (a) he dislikes the option-picker UI for open-ended requirement work; (b) "if you have a choice between calling a tool and not calling a tool, not calling is always more token-efficient — every tool call wraps JSON." See [[caveats-and-corrections]] for the nuance (Claude 4.x token-efficient tool use narrows this gap; the UI/flow argument is the stronger one).

## Supporting cast used mid-session

- **Explore subagent** — used repeatedly; Matt's gloss: sub-agent reads "tons and tons of files" in its own context, hands back a summary — "very token efficient." His complaint: "I just wish it was quicker."
- **`/btw` side-question** — quick question that stays OUT of chat history (exit with space/enter/esc); he uses it to get a tour of the course-write-service without polluting the grilling context. Real Claude Code feature (≤ v2.1.79 — see [[the-originals]]).
- **Context hygiene:** after 20+ minutes, ~40K tokens — the grilling loop is cheap because exploration is delegated and answers are plain text.

## Key Takeaways

- Grilling is **plan-mode as dialogue**: the human supplies why + decisions; the agent supplies code-grounded questions + trade-off analyses.
- The quality bar for the agent's questions is "would my best-ever tech lead ask this?" — and the demo shows it repeatedly clearing that bar (framing challenge, cascading-materialization question, hysteresis edge case).
- **Explain the why** is the highest-leverage habit: it converts the agent from scribe to design partner.
- "Look harder" — a two-word re-instruction beats both silent acceptance and manual takeover.
- The 22 minutes are the point, not the overhead: "we have done the hard bit now. We have done the human-in-the-loop bit."
