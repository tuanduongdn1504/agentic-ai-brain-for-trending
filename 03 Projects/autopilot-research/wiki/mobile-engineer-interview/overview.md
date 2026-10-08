# Overview — the interviewer, the five candidates, and how to use this

## The interviewer

**Tuấn Dương** conducts all five (a program lead, **"Huân"**, joins for the very-junior React one to cover motivation/logistics). His method is consistent and worth studying if you'll be interviewed by him — or if you want to *run* interviews like this:

- **Broad concept → "why?" follow-up.** He rarely stops at "what is X"; he asks "why does `const` need a value?", "why was async/await created?". Rote recall doesn't survive one follow-up.
- **Fundamentals before frameworks.** He won't ask about BLoC/hooks until async/await, types, and widget/component basics are established.
- **Live coding to expose the gap.** Mid-interview he switches to a console/editor and asks for array transforms or an IIFE. This separates *recognising* a concept from *using* it — where most junior candidates fall down.
- **Supportive, not adversarial.** He teaches during the interview (Set, spread, TS benefits), scaffolds when a candidate is stuck, and names gaps without shaming. He's assessing *growth potential*, not gatekeeping trivia.
- **Behavioral last, scenario-based.** Team conflict, a slacking teammate, a thesis-vs-release deadline clash, group-of-three hiring dynamics. He wants judgment, not textbook virtues.
- **Transparent process.** States the number of open roles, timeline, and the intern ramp openly.

## The five candidates (level spread is the point)

| Candidate | Stack | Level | What they showed |
|---|---|---|---|
| Vũ Thành Long | **Flutter** | Y4 student, UI-only | Hands-on Flutter UI; weak async, state-mgmt, VCS, APIs |
| Đỗ Minh Thành | **Flutter** | Y4 intern, UI-only | Solid UI/design; had **const/final backwards**; no BuildContext/state-mgmt/API |
| Trương Nhất | **React/JS** | **Very junior** (1 semester) | Career-changer; honest + motivated; almost no CS/JS depth yet |
| Đỗ Thanh Tuấn | **React Native** | Junior, ships apps | **3 apps on Play Store**; knows deployment hands-on; weak ES6/algorithms |
| Huỳnh Đinh Hoàng Viên | **React** | Strongest | Real grasp of event loop, hooks, Virtual DOM; team-lead experience |

The value of the spread: you can see **the same questions** answered at four different competence levels, so you can calibrate what a "good", "partial", and "did-not-know" answer sounds like for each.

## The escalation arc (typical order)

1. **Background / self-intro** → 2. **Git & tooling** (foundational hygiene) → 3. **Language fundamentals** (JS or Dart types, operators, async) → 4. **Framework** (React hooks / Flutter widgets) → 5. **Live coding** (array ops, IIFE, deployment walk-through) → 6. **Architecture & practice** (SPA/SSR, testing, clean code) → 7. **Behavioral / culture / career**.

## How to use this topic

- **Interviewing soon?** Go straight to [[study-guide-and-gaps]] — the cross-interview high-yield list + the failure modes. Then drill your stack's article ([[03-react-and-hooks]], [[04-flutter-and-dart]], or [[05-react-native-and-mobile-deployment]]).
- **All stacks share** [[01-javascript-core]], [[02-async-and-event-loop]], [[07-git-testing-and-engineering-practice]], and [[08-behavioral-and-interview-craft]] — Tuấn asks these regardless of stack.
- **Trust the model answers, not the transcript.** The captions are doubly-garbled ASR; the wiki's answers are the *verified canonical* ones. Where a candidate or even the extraction was wrong, [[caveats-and-corrections]] flags it.
- **Running your own screens?** [[hireui-relevance]] turns this into a reusable, ADR-safe rubric.

## Key Takeaways

- One interviewer, five competence levels, one consistent method: **concept → why → prove it in code**.
- The junior candidates fail on a **small, repeating set** of items — that's the highest-ROI drill list.
- Foundations (types, async, array transforms, Git, widget/component basics) are asked in every stack; framework depth is stack-specific.

**Source:** `raw/2026-08-06-mobile-engineer-interview.md` (5 videos, channel Tuấn Dương). See [[source-provenance]].
