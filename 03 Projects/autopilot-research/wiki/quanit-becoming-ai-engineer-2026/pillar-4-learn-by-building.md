# Pillar 4 — Learn by building (the most important)

## Source
Quân IT, [`RcF6ofU2nLs`](https://www.youtube.com/watch?v=RcF6ofU2nLs) [16:11–end]. He flags this as the single most important point.

## What he says

- **Tutorials won't make you good.** *"You can watch tutorials all day, all week, all month — you still won't be good."* The fastest way to learn is to **build.**
- **Find a real problem — via genuine curiosity, not a pitch** [16:11–17:07]. Don't approach a friend in another industry with *"I have an AI product/idea, can I ask you something?"* Instead ask *"what's a headache for you?"* His example: a friend in real estate/construction — *"when you dig foundations, what if a drone scanned the excavation?"* If you show sincere interest in **their** domain and problems, people share generously.
- **Then build it — and use AI tools while you do** [17:07–17:35]. You can't credibly build AI systems without *using* AI. Using **Claude Code, open-source coding agents, Codex**, etc. itself teaches you what components an AI system has and how it operates.
- **Watch fewer tutorials; solve one real problem hands-on** [17:35].
- **The payoff is interview war-stories** [17:35–18:32]. Interviewers won't test theory (*"anyone can paste theory into ChatGPT"*). What raises your value is a real narrative: *"I built system X, hit problem Y, weighed options A–F with their trade-offs, picked Z and here's why; after 3 months in production it didn't hold up, so I fixed it / combined approaches."* That beats the identical bootcamp project everyone submits.
- **Deliberately pick projects beyond your ability** [18:32–end]. If a project feels too hard, *"that means you're on the right path."* Do the over-your-head project, find what you're missing, and learn to fill exactly that gap.
- Closes by inviting disagreement in the comments.

## Verified facts behind the pillar

- **Claude Code, Codex, and open-source coding agents** are all real, current tools — consistent with the corpus ([[codesistency-mobile-app-course/_index]], [[harness-engineering/_index]]). No specific factual claim here to refute; the pillar is method/advice.

## The caveat: sound method, missing guardrails

The critical appraisal endorses this pillar's pragmatism but flags one omission:
- "Build first, learn by doing" is right — **but for high-stakes domains** (recruitment fairness, healthcare safety, finance/audit), unstructured build-and-iterate can ship real harm before you notice. Add **ethical guardrails + a visible framework** (a harness) so failures surface early rather than in front of users.
- This is the tension with structured, spec-first approaches ([[jsm-practical-vibe-coding/_index]], and the SDD pole generally): pure iteration vs. structured scaffolding. The right answer is usually **both** — build fast, but inside a legible harness (directly relevant to the [[quanit-becoming-ai-engineer-2026/hireui-pilot|hireui pilot]], where a candidate-facing LLM path must be auditable).

## Key Takeaways

- **The best career advice in the talk:** build a real thing; the *struggle* is the education, and the *story* is the interview edge.
- **"Ask what's a headache, don't pitch an idea"** — a genuinely good heuristic for finding worthwhile problems (and, incidentally, for requirements-gathering).
- **"Pick projects beyond your ability"** — deliberate difficulty as a learning strategy; correct calibration.
- **Add the missing half:** build inside a **legible harness with guardrails**, especially for anything that affects a real person's outcome. See [[harness-engineering/_index]] and the security section of [[quanit-becoming-ai-engineer-2026/pillar-3-seventy-percent-is-normal-engineering|Pillar 3]].
- For the operator, this pillar *is* the argument for actually shipping a hireui LLM feature rather than accumulating more research — see [[quanit-becoming-ai-engineer-2026/hireui-pilot|hireui-pilot]].
