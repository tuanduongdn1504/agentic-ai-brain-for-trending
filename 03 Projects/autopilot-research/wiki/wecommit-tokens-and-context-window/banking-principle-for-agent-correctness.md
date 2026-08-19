# The Banking Principle for Agent Correctness

> **Source:** [`QgDsHhy9Cpo`](https://www.youtube.com/watch?v=QgDsHhy9Cpo) (2026-08-13, 21:52) — *"15 năm kinh nghiệm các dự án ngân hàng dạy tôi 1 nguyên tắc giúp AI Agent làm đúng"*.
> ⭐ **The most operationally valuable video in the bundle, and the one that most sharply converges with this vault's own doctrine.**

## The diagnosis: it isn't your prompt

His opening ([00:01]): people assign work to AI, it comes back wrong, they redo it, repeatedly — burning time and money. The reason is **not** a bad prompt.

Why detailed step-by-step instructions still fail ([08:41]–[11:59]):

- Traditional software is **deterministic** — "fetch cell A5" returns a guaranteed result.
- An LLM predicts the **next token from statistical patterns**. It is word-probability, not semantic understanding, so **100% intent-comprehension is unreachable by describing harder.**
- Tokenization is itself a lossy communication step between you and the model ([10:32]) — which ties this video back to [[tokenization-mechanics]].

> **The core insight** ([11:01]): *AI has no idea what "pass" versus "fail" means for your task.* From his consulting work: businesses describe the task in exhaustive detail and **never state the success criteria.**

## Solution 1 — Quantifiable criteria plus a self-correction loop

1. List the **pass/fail criteria** explicitly ([12:26]).
2. Have the agent **report its own score** — e.g. "5/6 criteria met" — before submitting.
3. On a failure, instruct it to **retry only the failed criterion while preserving the ones already passed** ([12:55]), looping until all pass. The final output must satisfy 100%.
4. **Criteria must be measurable** — true/false, pass/fail, or numeric ([17:43]). Ban subjective words: *"good"*, *"clear"*, *"nice"* — because you and the model define them differently.
5. **Never deploy without criteria** ([13:59]): working without acceptance criteria is playing, not production.

This is **CLAUDE.md Rule 4 (Goal-Driven Execution)** arrived at independently: *"Define success criteria. Loop until verified. Don't follow steps. Strong success criteria let you loop independently."* His step 3 — preserve passed criteria while retrying the failed one — is a genuinely sharp refinement that the vault's own rule does not spell out.

## Solution 2 — The banking principle: rollback capability

> *"Every production step must be reversible. If a step fails in production, you must be able to undo it."* — [14:28]

This is what 15 years on banking, securities, hospital and telecom systems taught him, and he uses it to place the **human gate**:

- **Reversible steps** → let the agent run them.
- **Irreversible steps** → require **human review after the agent's self-check** ([15:50]). His example of an irreversible step: **sending a price-quote email to a customer.** You cannot un-send it.

He reports two payoffs: less rework (the agent learns what correct looks like), and enough confidence in quality to actually deploy. His dashboard implements it as an **"Awaiting your review"** status on every task before execution ([07:44]).

### What the standard names are

The verification pass flagged that he never uses the textbook vocabulary, and that is a fair criticism of the framing:

- Reversibility of a unit of work is **transaction atomicity** (the A in ACID, formalised by Haerder & Reuter in 1983).
- Undoing an already-committed external effect is a **compensating transaction** (the saga pattern).
- In deployment terms it is **reversible migrations** and **blast-radius control**.

So the *principle* is decades old and not a personal discovery. **What is genuinely his** — and what makes the video worth its runtime — is using reversibility as the **gate-placement rule for autonomous agents**: not "review everything" (unaffordable) and not "review nothing" (unsafe), but *review exactly the steps you cannot undo.* That decision rule is not standard, it is correct, and it is immediately portable.

## Solution 3 — Never let the agent be its own verifier

> *"Never let AI self-check its own output; AI has inherent bias."* — [18:39]

His method ([19:06]–[19:34]): separate **"AI generates"** from **"independently verify"**, and do the verifying with **external tools the AI does not control** — `curl`, a SQL query, a function. His example: if the agent claims a database is in some state, run your own SQL query and compare its claim to ground truth. That, he says, is what eliminates the fabrication worry.

### An automated verifier called this FALSE. It is not, and this run is the proof.

A refute-first verifier in this run marked the claim **FALSE**, citing Constitutional AI as evidence that models can self-critique. **That verdict is overridden.** Three reasons:

1. It cited **no URL**, in a run where every CONFIRMED verdict was required to carry one.
2. Its own proposed correction concedes the speaker's actual point — *"independent verification is more reliable than self-check, especially for critical steps."*
3. **This very compilation is empirical evidence for him.** The extraction stage fabricated model names that do not exist ("Claude 3 Opus", "Claude 3.5 Opus"); the agent that produced them did not catch itself. An **independent** verifier stage caught it, and a **third** pass — reading the raw transcript — settled it ([[caveats-and-corrections]]). Self-check would have shipped the fabrication.

His claim is more precisely stated as **CORRECT-BUT-INCOMPLETE**: self-critique has real value as a cheap first pass (his own Solution 1 depends on it — the agent scoring itself 5/6), but it cannot be the *last* gate. Generation and verification must not share a context.

This is the **maker/checker split** the vault already runs as doctrine — the `loop-verifier` agent exists precisely because "the implementer's claims are not evidence."

## The final framework — work backwards

From [20:32]:

```
desired outcome  →  define what "correct" means  →  list quantifiable criteria
                 →  assign to the agent  →  review at the gates you cannot undo
```

And his closing observation ([20:59]), which is the strategic point: for non-technical deployers — owners, managers — **defining criteria is easier and more durable than prompt engineering**, because models keep improving on their own while your criteria stay valid. Criteria are an asset; prompts are a depreciating one.

## Cross-links

- [[four-rules-for-token-discipline]] — rule 4's partition-by-strength, extended here into criteria and gates
- [[agent-org-chart-architecture]] — the dashboard this review gate is built into
- [[tokenization-mechanics]] — the lossy-communication premise underneath the argument
- [[claude-md-12-rules/_index]] — Rule 4 (goal-driven execution) and Rule 12 (fail loud), independently derived here
- [[prompt-evaluation/_index]] — criteria-as-evals, the formal version of Solution 1
- [[autonomous-loops-human-in-the-loop/_index]] — where to place the human
- [[hireui-relevance]] · [[claims-scorecard]] · [[caveats-and-corrections]]
