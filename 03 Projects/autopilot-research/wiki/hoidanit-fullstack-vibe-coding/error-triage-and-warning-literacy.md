# Error triage & warning literacy (INFO / WARNING / ERROR)

## Source
- Video #4 tD0Uve-0Ltk, chapter "Phân biệt info, warning, error" (38:32) + npm-audit segment (40:50–42:42)

## The teaching
- Terminal output has three severities, and beginners must learn to *read* them before reacting:
  - **INFO** (white) — narration; ignore.
  - **WARNING** (yellow) — deprecations, outdated packages, audit notices; **safe to defer while learning**. They will reappear; chasing them is not progress.
  - **ERROR** (red) — the app won't start; this is the only class that demands action now.
- Applied on camera: the fresh `nest new` install prints a ~22-package vulnerability notice → explicitly *not* fixed. Quote [00:40:50]: open-source projects can't avoid outdated-package warnings; *"khi các bạn học kiến thức ấy thì nó không ảnh hưởng gì cả"* — while learning, it changes nothing.
- Anti-panic framing: beginners see yellow/red text and assume the machine is broken; the triage lattice replaces panic with classification.

## Transfer to agent workflows
- The same lattice is a cheap **agent guardrail**: a coding agent that "helpfully" chases audit warnings mid-task burns tokens and widens diffs (violates surgical-change discipline — Mnilax Rule 3, [[claude-md-12-rules/_index]]). A one-line constraint ("fix ERRORs; list WARNINGs, don't fix unless asked") encodes this teaching.
- Sister discipline to [[jsm-practical-vibe-coding/_index]]'s "one problem, one fix, one verification" and to cost discipline in [[claude-api-cost-optimization/_index]] — warning-chasing is a token/cost leak, not just a focus leak.
- Learning-vs-production split is stated, not implied: the *same* warning that's ignorable in a tutorial is backlog in production. The context tag, not the warning text, decides the response.

## Key Takeaways
- Triage by severity class, not by text color intensity or panic level.
- npm-audit noise on a fresh scaffold is normal; deferring it is a *decision*, taught explicitly — not an oversight.
- As an agent constraint: "never auto-fix warnings; fix errors; report both" is this lesson in one line.
- The learning/production boundary is part of the lesson — warning tolerance is context-dependent, not absolute.
