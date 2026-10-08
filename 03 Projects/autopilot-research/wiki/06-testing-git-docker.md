# Engineering Practice — unit testing, git flow, Docker

Three fundamentals that separate junior from professional Node.js/backend work: **testing discipline**, **branching hygiene**, and **containerization**. Each one is where candidates frequently conflate what they've heard with what actually works.

## Source

- **Interview:** BE Interview Nguyễn Chánh Đạt, YouTube video `6OYzD13GtKs`, uploaded 2026-06-17 (~63 min, Vietnamese, auto-captions)
- **Extraction:** `raw/2026-07-31-nodejs-backend-interview.md`
- **Questions covered:** Q12 (git flow / environment separation), Q13 (unit testing), Q14 (Docker image/container distinction, Dockerfile purpose, docker-compose services)

---

### Q12 — Describe the git flow you used on your team project

**Asked:** What was your branching strategy? How did you separate code between environments (development, staging, production)?

**Candidate answered:** Team used SCRUM: split each sprint into tasks/subtasks. One branch per subtask. Open a PR to review and merge. When pressed on "push to which branch / do you separate environments?" → only one branch; code goes straight to production.

**Interviewer taught:** Flagged it plainly: "code done → straight to production… ok." (The pause-and-acceptance is deliberate — marking a **maturity red flag**, not lecturing.)

**Canonical answer:** A mature git flow separates concerns:
- **Short-lived feature branches** off `main`/`develop` (one branch per feature/task)
- **Protected main branch** requiring PR + code review + CI/CD checks before merge
- **Environment separation:** separate git branches or tags for dev / staging / production (e.g., GitHub-Flow or Git-Flow)
- **Promotion gates:** code merges to main → deploy to staging (automated); staging validated → tagged/branched for production deploy
- **No direct-to-prod:** never bypass review and testing; all changes flow through the promotion pipeline

Single-branch-to-production is the canary sign of "no deployment discipline." It trades speed now for risk later.

**Gotcha / red flag:** ⚠️ One branch from inception to production means every accidental commit, incomplete feature, or untested change can reach users. The interviewer's acknowledgment here is calibrated — experienced teams immediately recognize "straight to production" as a **critical missing discipline**, not a minor oversight.

---

### Q13 — Do you know unit testing?

**Asked:** Have you written unit tests? What's the difference between a unit test and manual testing?

**Candidate answered:** Heard of it. Never written one.

**Interviewer taught:** Empathetic but firm: students "just get it done for grades" and ignore tests. Many juniors test only via **Postman / manual clicking after deploy** — "that is NOT how you build software properly." The key reframe: proper software = **everything is testable** (even the compose file; he gestures at Q14). Learning testing basics is non-negotiable.

**Canonical answer:** A **unit test** is a **small unit in isolation**, characterized by:
- **Fast** — runs in milliseconds; you run the whole suite hundreds of times per day without friction
- **Deterministic** — same result every run; no time-based or randomness flakiness
- **No external dependencies** — no database, network, filesystem, or real clock. Replace them with **fakes/mocks/stubs**:
  - **Fake:** a simplified working implementation (e.g., `FakeUserRepository` with an in-memory array instead of a database)
  - **Mock:** a spy that records calls and can assert on how it was used
  - **Stub:** a minimal placeholder that returns a canned response
- **Example:** `UserService.createUser(userData)` with a faked `UserRepository` → in-memory store, no DB calls, test runs in RAM in <10ms

**Manual vs. automated testing:**
- **Postman / clicking the UI** = manual testing. You catch bugs in THIS test run, but no regression safety for future developers. Not repeatable at scale.
- **Automated unit tests** = regression safety. When you refactor, the suite runs automatically and tells you if you broke anything.

**Test pyramid:**
```
        few ▲  e2e (slow, real DB, real server)
            │
       more │  integration (in-memory DB, real code paths)
            │
     many ▼ unit (mocked deps, fast)
```

Most tests should be unit; fewer integration; fewest e2e.

**Tooling:** Jest, Vitest, Mocha+Sinon (all Node.js standard).

**Gotcha / red flag:** ⚠️ The candidate conflated "I've heard of testing" with "I know how to write a test." Testing requires **mental model shifts** — thinking about fakes, isolation, and determinism. Juniors often write "integration tests pretending to be unit tests" (real database, real network) and are shocked when they flake. The interviewer's framing — "that is NOT how you build software properly" — is calibrated to convey: **this is not optional; it's the table stakes.**

---

### Q14 — What is Docker for? Why write a Dockerfile if images already exist? What was in your docker-compose?

**Asked:** Explain the difference between a Docker image and a container. Why do you write your own Dockerfile instead of just using an existing base image? What services did you include in your docker-compose for the to-do app?

**Candidate answered:** Image = built from your code (Dockerfile) → container runs on any machine. Why write a Dockerfile: each project has different libraries/dependencies, so you customize. Wrote docker-compose for a personal to-do app with web UI, list, add/pick-date, delete. When pressed on "which services did you define (database? web server?)": answer was thin / incomplete.

**Interviewer taught:** Accepted it as "experience-level" exposure. Probed for services and a database tier, but didn't get a solid answer from the candidate. (Left it as a gap to flag.)

**Canonical answer:**

**Image vs. container:**
- **Image** = an immutable **blueprint/snapshot**: your application code + dependencies + runtime + configuration, all layered and versioned. Built from a `Dockerfile` at build time; stored as a `.tar` archive on disk or in a registry (Docker Hub, ECR).
- **Container** = a running **instance** of an image. Ephemeral; starts from the image, runs with its own isolated filesystem, network, and process. When you stop it, the container vanishes; the image remains.

**Why write a Dockerfile instead of using a base image alone:**
Base images (`node:20`, `postgres:15`) are **generic**. Your project is **specific**. A Dockerfile **layers your code, env, and exposed ports** on top:

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "index.js"]
```

You could run `docker run node:20` directly, but then you'd have to manually mount your code and set env vars every time. The Dockerfile **codifies your app's exact setup** so anyone can `docker build` it identically.

**docker-compose:**
A **declarative YAML file** that defines a **multi-container application**:
- Services (each is a container)
- Shared network (containers talk to each other by service name)
- Volumes (persistent data, shared code)
- Environment variables
- Port mappings

**Example (to-do app):**
```yaml
version: '3.9'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgres://user:pass@db:5432/todoapp
    depends_on:
      - db
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: todoapp
    volumes:
      - postgres_data:/var/lib/postgresql/data
volumes:
  postgres_data:
```

**The red flag in the candidate's answer:** a to-do app's docker-compose had the **web service but no database service**. In a real setup, the **app writes todos to a database** — that requires a database container in the compose. Missing it signals: the candidate either (a) doesn't understand that docker-compose coordinates **multiple services**, or (b) didn't think through "where do the todos live?" A stateless web server + no persistence is a hollow demo.

**Gotcha / red flag:** ⚠️ Beginners conflate "I can run `docker run node`" with "I can docker-compose a real app." Docker-compose is where the **architectural thinking** emerges — you must reason about service boundaries, network, state, and data flow. The missing-database-service is a **concrete tell** that separates thoughtful from checkbox engineering.

---

## Key takeaways

- **Git flow:** one-branch-to-prod is a maturity red flag. Mature flows use protected main, feature branches, PR reviews, and environment separation (dev → staging → production).
- **Unit tests are NOT optional.** Postman / manual clicking is regression theater, not actual testing. Real unit tests are fast, deterministic, in-memory, mocked — not integration tests in disguise.
- **Fakes/mocks/stubs are how you isolate.** Inject them via constructor (Q16's DI theme) so your test never touches a database, network, or clock. Determinism comes from controlling the collaborators.
- **Image vs. container:** image = blueprint, container = running instance. You build the image once; spin up containers as needed.
- **Dockerfile layers your code on a base.** You don't use a base image raw; you customize it. docker-compose declares the full app: app + database + cache, all wired together.
- **The missing-database-service is a tell.** If your app's docker-compose doesn't include a database service, you haven't thought about where state lives. Stateless APIs are fine; stateful apps need to compose their data layer.
- **Testing discipline, branching discipline, and containerization are all about "real-world thinking."** They separate "works on my machine" from "works in production."

## Interviewer red flags (what to avoid saying)

- ❌ "I test with Postman / by clicking the UI." (Not automated, not regression-safe; interviewer will note this as missing discipline.)
- ❌ "I commit straight to main / production" or "We don't do code review." (Immediate red flag for engineering maturity; no recovery once flagged.)
- ❌ "I don't know what a unit test is / never written one." (The interviewer was empathetic here but firm: this is expected knowledge. Saying "never heard of it" is worse than "tried but struggled.")
- ❌ "My docker-compose has only the app service, no database." (Signals you haven't reasoned about the full system — where do your todos live?)

---

[[02-async-promises-event-loop]] [[03-nodejs-runtime-internals]] [[05-dependency-injection]] [[study-guide-and-gaps]]
