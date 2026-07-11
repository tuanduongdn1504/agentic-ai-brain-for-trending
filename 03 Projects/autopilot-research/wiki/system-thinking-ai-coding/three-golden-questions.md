# The 3 golden questions (answer BEFORE running code)

## Source

[`raw/2026-07-07-system-thinking-ai-coding.md`](../../raw/2026-07-07-system-thinking-ai-coding.md) [00:11:16]–[00:14:55]. The speaker frames system thinking as fitting into three questions you must answer *before you hit run*. See [[overview]] and [[what-system-thinking-is]].

## Q1 — State / data flow: where does state live, and who is the single true owner?

- Where is state (the data flow) stored? **Who is the one, unique owner in the system?**
- **Failure mode:** if two components each believe they own the same data, "you've armed a time-bomb" (self-inflicted race/consistency bug).
- Design priority: decide **data/DB architecture first**, not the UI. "What decides what?" — data should decide the interface, not the reverse. (He repeatedly saw UIs designed before the database — a red flag.)

## Q2 — Feedback: where do signals come back from?

- **What tells you the system is healthy vs. erroring? Where is error logic collected?**
- **Failure mode:** without a feedback/observability mechanism, "the system is only *pretending* to run" right up until total collapse — you never know when it will fall over.
- Provocation: do you need **self-destruct / chaos tests** that try to break your own system *before* it ships? The risks of handing everything to AI (security, logic, business correctness) are borne by you and your users.

## Q3 — Blast radius: what breaks if I delete this part?

- **If I remove this component/function/file, what breaks, and how badly?**
- **The real test:** can you trace a component's zone of impact — and the data flow / user flow — **in your head**, just by reading the AI-written code?
- **Failure mode:** "I don't know" = a **cognitive hole**. It means you don't understand the system you're shipping; you've mistaken the AI's product for your own.

## How to use it

- Treat the three questions as a **pre-run checklist / definition-of-ready gate** for any feature — human- or AI-authored.
- They map cleanly onto review: **Q1 = data model & ownership, Q2 = observability & error handling, Q3 = coupling & change-safety.**
- If any answer is "I don't know," that is the signal to stop generating and go build the theory (draw it, spec it) — see [[four-practice-steps]] and [[naur-programming-as-theory-building]].

## Key Takeaways

- **State ownership → Feedback → Blast radius.** Three questions, answered before running code, are the compressed form of "do you actually have the theory of this system?"
- The questions double as a **code-review rubric** for AI-generated code and a **definition-of-ready** for tickets.
- Directly portable to the operator's hireui work as a PR-template / constraint line — see the pilot methods deliverable and [[claude-md-12-rules]] (Rule 1 / Rule 8).
