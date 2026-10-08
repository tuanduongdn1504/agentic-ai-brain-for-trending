# Overview — a Node.js backend internship interview, decoded

**A real ~63-minute Vietnamese Node.js/backend internship screening, turned into a verified study guide. The payload is not what the candidate said — it's the interviewer's corrections plus the canonical answers, organized as a question bank you can drill.**

## The setup

- **Candidate:** Nguyễn Chánh Đạt — 4th-year Software Engineering student, Đại học Bách Khoa (Polytechnic). Prior work: a team **cinema-booking system** (SCRUM) and a personal **to-do-list app**.
- **Interviewer (technical):** "anh Hoàng Phạm" — senior engineer, Socratic, repeatedly contrasts *"what juniors/textbooks say"* with *"what actually happens in 3–4 years of real work."*
- **Role:** Node.js intern (backend). ~4 interns taken; trained toward full-time conversion (mutual, no obligation).

## The interviewer's philosophy (worth modeling)

Stated up front: *"Answer what you understand. If you don't understand a question, ask me to rephrase. If you know the concept but can't map my wording to it, say so — I'll explain, then you explain your understanding back."* He grades **understanding**, not vocabulary recall, and gives partial credit for reasoning out loud. The best answers in the transcript are the ones where the candidate says "I'm not sure, but here's how I'd reason about it."

## The escalation arc (how the interview is structured)

1. **JavaScript core** — Map vs Object, Set, arrow vs normal functions, callbacks → [[01-javascript-core]]
2. **The async model** — Promises, the event loop, async/await, promisify → [[02-async-promises-event-loop]]
3. **Node runtime internals** — CommonJS vs ESM, garbage collection, single-thread + non-blocking I/O → [[03-nodejs-runtime-internals]]
4. **API design** — REST conventions, REST vs GraphQL, over/under-fetching, ORM trade-offs → [[04-rest-graphql-api-design]]
5. **Dependency injection** (the ~20-min centerpiece) — DI vs Dependency Inversion vs DI Container, and why → [[05-dependency-injection]]
6. **Engineering practice** — unit testing, git flow, Docker → [[06-testing-git-docker]]

The difficulty deliberately ramps: fundamentals to filter, then internals ("I expect a fresh grad to answer this"), then a design-and-reasoning centerpiece where a strong answer separates candidates.

## Where the candidate struggled (the study hit-list)

These are the highest-value questions to master, because they're the ones that **broke** a real internship candidate — see [[study-guide-and-gaps]] for full model answers:

- **Arrow vs normal function `this`** — answered, but **inverted** (a subtle, common mistake).
- **How a Promise is handled in the event loop** — could not explain (microtask vs macrotask queue).
- **Single thread + non-blocking I/O** — could not explain why `console.log` after `fs.readFile` prints first (libuv thread pool).
- **Garbage collector** — recognized the term, couldn't define it.
- **Unit testing** — never written one (and the interviewer treats this as the dividing line between "getting it to run" and "building software").

## What makes this source unusual for the corpus

Most corpus topics fact-check a creator's marketing hype. Here the "claims" are **technical concepts**, and there are two verification jobs: (1) make sure the **canonical study answers** are correct, and (2) catch where the **interviewer himself** taught something questionable — most notably his **GraphQL-origin claim** ("not built for the frontend"), which the real history contradicts. See [[claims-scorecard]] and [[caveats-and-corrections]].

## How to use this topic

- **Interviewing soon?** Read [[study-guide-and-gaps]] first (the hit-list + model answers), then the six topic articles.
- **Interviewing others (recruiter/lead)?** See [[hireui-relevance]] — this is a ready-made backend/Node screening rubric.
- **Handing this to another agent?** A self-contained interview-coach brief lives at `output/(C) 2026-07-31-nodejs-interview-coach-handoff.md` — see [[hireui-relevance]].
