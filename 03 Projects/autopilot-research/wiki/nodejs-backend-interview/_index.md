# Node.js Backend Interview — a verified study guide

**A real ~63-minute Vietnamese Node.js/backend internship screening interview, turned into a fact-checked question bank. The study payload is the interviewer's corrections + the canonical answers — not the candidate's (frequently inverted) answers. The corpus' FIRST interview / interview-prep topic.**

- **Source:** single video — [BE Interview Nguyễn Chánh Đạt](https://www.youtube.com/watch?v=6OYzD13GtKs) · channel Tuấn Dương · 2026-06-17 · ~63 min · Vietnamese (auto-captions only). A senior engineer ("anh Hoàng Phạm") Socratically screens a 4th-year Software Engineering student (Đại học Bách Khoa) for a **Node.js intern** role. Full trail in [[source-provenance]].
- **Ingested:** 2026-07-31 (Path 5 yt-dlp only — no NotebookLM, no yt-search) · raw: `raw/2026-07-31-nodejs-backend-interview.md`
- **⚠️ Adversarially verified:** Workflow `wf_a6a465f8-155` — **13 agents** (6 topic drafters → 6 refute-first technical verifiers over MDN / nodejs.org / v8.dev / libuv / GraphQL history → 1 completeness critic; **0 errors / 0 empty / 0 skipped**; ~811K tokens, 110 tool calls, ~5.5 min) + Opus main-loop QA (maker/checker). **Scorecard (86 claims): 82 CONFIRMED · 3 CORRECT-BUT-INCOMPLETE · 1 MISLEADING · 0 FALSE · 0 FABRICATED** — a high-integrity study guide. See [[claims-scorecard]].
- **The one correction that matters:** the **interviewer's** claim that *"GraphQL wasn't built for the frontend"* is **historically inverted** — Facebook built GraphQL (2012) *for* its mobile clients. Preserved as a faithful record, flagged, and corrected. Don't repeat it in an interview. See [[caveats-and-corrections]].
- **⚠️ Heavy ASR garble:** Vietnamese auto-captions mangled nearly every technical term (async→"Singway", GraphQL→"Graql", dependency injection→"defensy injection"). Every term is a reconstruction of intent; the *raw captions* are not quotable. Garble→term map in [[caveats-and-corrections]].
- **Corpus first:** the wiki's **first interview topic** (grep-verified over 72 prior topics — no collision).

## The one framing

**A backend interview grades understanding, not vocabulary.** This one ramps deliberately: JavaScript fundamentals (to filter) → runtime internals ("I expect a fresh grad to answer this") → a ~20-minute dependency-injection design/reasoning centerpiece (where a strong answer separates candidates). The interviewer repeatedly rejects the *textbook* reason for the *working* reason — and rewards reasoning out loud under uncertainty over confident-but-wrong recall.

## Start here

- [[study-guide-and-gaps]] — **the 5 questions that broke the candidate**, ranked hardest-first, each with a 30-second model answer + a drill. The fastest path to interview-ready.
- [[overview]] — the participants, the interviewer's philosophy, the escalation arc, and how to use this topic.

## The six topic articles

- [[01-javascript-core]] — Map vs Object, Set + dedup, arrow vs normal function `this` (the candidate **inverted** it), why arrow callbacks in `.map()`.
- [[02-async-promises-event-loop]] — what Promises solve (callback hell), the **microtask vs macrotask** queue, async/await = a Promise, promisify (fs/promises exists; `net` doesn't).
- [[03-nodejs-runtime-internals]] — CommonJS vs ESM, the V8 garbage collector, and the headline: single-thread + **non-blocking I/O via libuv** (why `console.log` after `fs.readFile` prints first).
- [[04-rest-graphql-api-design]] — REST conventions, HTTP verbs, over/under-fetching, REST vs GraphQL, ORM select-all-vs-select-fields, and the **GraphQL-origin fact-check** + the valid security thesis.
- [[05-dependency-injection]] — the centerpiece: **DI vs Dependency Inversion vs DI Container**, the repository pattern, and DI's real payoff (faking for fast in-memory unit tests; inject the clock).
- [[06-testing-git-docker]] — unit testing (fast/in-memory/no external calls), git flow (the "one branch straight to prod" red flag), Docker (image/Dockerfile/container, docker-compose services).

## Appraisal

- [[claims-scorecard]] — the 86-claim refute-first verdict table + the 4 non-CONFIRMED items.
- [[caveats-and-corrections]] — the ASR-garble map, the corrections applied, and the maker/checker override.
- [[hireui-relevance]] — interview prep + a ready-made screening rubric for a recruiter + the ADR-safe product tie-in.
- [[source-provenance]] — the source, ingestion, and verification trail.

## Deliverable — portable interview-coach agent

`output/(C) 2026-07-31-nodejs-interview-coach-handoff.md` — a self-contained brief another agent can consume to run a mock backend/Node interview (escalating questions, model-answer grading, Socratic probing, the 5 gap drills), carrying its own provenance + the GraphQL correction. See [[hireui-relevance]] §3.

## Cross-links (corpus)

- [[api-types/_index]] — deeper REST/GraphQL/gRPC/WebSocket taxonomy behind Q15.
- [[data-structures-16-in-32-min/_index]] — the CS-fundamentals companion (arrays/hash/trees/graphs) the matcher-style questions rest on.
- [[hoidanit-fullstack-vibe-coding/_index]] — VN-language NestJS/backend educator sibling.
- [[aws-email-at-scale-sqs-lambda-ses/_index]] — VN backend-architecture sibling (queues/async at scale).
- [[fullstack-docker-cicd/_index]] — the deploy layer behind Q12/Q14 (branches → environments → containers).
- [[pocock-software-fundamentals/_index]] · [[quanit-becoming-ai-engineer-2026/_index]] — "fundamentals matter more than ever" thread.
- [[miai-cv-matching-agent/_index]] — recruitment-domain sibling (the operator's product space).
- [[api-security-7-techniques/_index]] — the authz/BOLA layer behind the GraphQL security thesis.
