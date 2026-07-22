# Three Things to Avoid: Cognitive Debt, Cognitive Surrender, Orchestration Tax

> **Source:** Addy Osmani keynote [`n97BCfyFIvw`](https://www.youtube.com/watch?v=n97BCfyFIvw), AI Engineer World's Fair 2026.

Osmani names three failure modes that erode an engineer's ability to *stay accountable* as they delegate more to agents.

## 1. Cognitive debt

> "The erosion of your understanding and memory around how to solve problems."

- Accrues the more you defer problem-solving to AI every day (Osmani: "I feel this a lot").
- For code specifically it's **delegation debt**: the gap between *how much code exists in your repo* and *how much any human on your team genuinely understands.*
- The trap: **a build that passes + a PR you can merge — while the team loses the ability to explain the system it ships to production.**
- Aggravated by long-horizon agents: a 30-second run feels like an interaction, but an hour- or day-scale task is a *work stream* — the human "loses the thread." Especially when many run in parallel, **review can't be a glance at the end; it has to become a control system.**

## 2. Cognitive surrender

> "Blindly accepting AI's responses… saying *your answer is now my answer before I've formed any opinion myself.*"

- Distinct from healthy delegation. **Delegation** = "do the work, then show me enough evidence that I can judge it" (you still make a judgment). **Surrender** = skipping the judgment.
- **The warning light — a Wharton study** (confirmed; Steven Shaw & Gideon Nave, *"Thinking, Fast, Slow, and Artificial,"* Jan 2026; 1,372 participants, ~10,000 trials):
  - When the AI was **wrong**, ~**73% still went with the wrong answer** (the researchers call this **"cognitive surrender"** — the same term Osmani uses); the broader "followed the wrong answer" figure was ~80%.
  - Participants' **confidence rose ~12 percentage points even when the AI was wrong.**
- Osmani's name for it: **"borrowed confidence."** The failure mode isn't *using* AI — it's borrowing its confidence without earning your own.

## 3. Orchestration tax

> "More AI agents running does not mean there is more of you available. **Your cognitive bandwidth does not parallelize.**"

- Every loop you spin up creates more decisions to route, merge, verify, and integrate.
- The "laptops open, hundreds/thousands of agents" flex (Osmani gently mocks the Bay Area version) doesn't add human capacity.
- **The fix is not fewer agents — it's designing your attention like a system:** where you enter, what you require, what you reuse. Be intentional about it.

## Why these three matter together

All three attack **answerability** (see [[engineer-of-the-future/osmani-answerability-thesis]]): cognitive debt destroys *understanding*, cognitive surrender destroys *judgment*, and orchestration tax destroys the *bandwidth* to verify. If any collapses, you can no longer "explain it" — so you shouldn't ship it. This is the human-cost counterpart to Karpathy's "keep the AI on a leash" (see [[engineer-of-the-future/karpathy-software-is-changing]]).

## Key Takeaways

- **Cognitive debt / delegation debt** — code outruns team understanding; "build passes, nobody can explain it." Long-horizon + parallel agents make review a *control system*, not a glance.
- **Cognitive surrender** — accepting AI output before forming your own view. Wharton: ~73% follow wrong AI answers *and feel more confident* = "borrowed confidence."
- **Orchestration tax** — bandwidth doesn't parallelize; more agents ≠ more you. Fix = design your attention like a system.
- All three erode **answerability**; guarding them is what keeps "explain it or don't ship it" achievable.

## See also

- [[engineer-of-the-future/osmani-answerability-thesis]] · [[engineer-of-the-future/inner-loop-outer-loop]]
- [[engineer-of-the-future/karpathy-software-is-changing]] — "keep the AI on a leash" (the tooling-side version)
- [[engineer-of-the-future/caveats-and-corrections]] — precise Wharton figures + terminology
- [[claude-md-12-rules/_index]] — rules that operationalize not-surrendering to the model
