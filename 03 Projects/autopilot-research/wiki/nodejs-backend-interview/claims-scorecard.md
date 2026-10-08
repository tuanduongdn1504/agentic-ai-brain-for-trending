# Claims Scorecard

**86 load-bearing technical claims across the six articles, each refute-first fact-checked against authoritative sources (MDN, nodejs.org, v8.dev, libuv source, GraphQL history) by an independent verifier per article.**

## Tally

| Verdict | Count |
|---|---|
| ✅ CONFIRMED | **82** |
| 🟡 CORRECT-BUT-INCOMPLETE | **3** |
| 🟠 MISLEADING | **1** |
| ❌ FALSE | 0 |
| ❓ UNVERIFIABLE | 0 |
| **Total** | **86** |

**Faithfulness:** all 6 articles passed the faithfulness check — **0 fabricated interview content** (nothing attributed to the candidate or interviewer that isn't in the transcript extraction).

**Profile:** a **high-integrity technical study guide**. Unlike most corpus topics (which fact-check a creator's marketing hype), the verification target here was the *correctness of the canonical study answers* plus catching where the *interviewer himself* taught something questionable. The canonical answers hold up almost entirely; the single MISLEADING item is the **interviewer's** claim, not the wiki's.

## Per-article

| Article | CONFIRMED | Other |
|---|---|---|
| [[01-javascript-core]] | 8 | — |
| [[02-async-promises-event-loop]] | 12 | 1 CBI |
| [[03-nodejs-runtime-internals]] | 20 | 1 CBI |
| [[04-rest-graphql-api-design]] | 20 | 1 MISLEADING |
| [[05-dependency-injection]] | 12 | — |
| [[06-testing-git-docker]] | 10 | 1 CBI |

## The 4 non-CONFIRMED verdicts (all corrected in the articles)

### 🟠 MISLEADING — GraphQL's origin (the interviewer's claim) — [[04-rest-graphql-api-design]]

- **The interviewer said:** GraphQL was built by Facebook as an abstraction layer *between the web API and backend microservices*, **not for the frontend**.
- **Fact-check:** **Inverted.** GraphQL was created at Facebook in **2012** (public 2015) by Lee Byron, Nick Schrock, Dan Schafer **specifically to power Facebook's native mobile clients' News Feed** — i.e. *for the frontend*, to kill over-fetching and multiple round-trips on mobile networks. Using GraphQL as an internal gateway in front of microservices is a *later deployment pattern*, not its origin.
- **His security thesis, by contrast, is VALID:** don't hand raw query power to an untrusted client (a hacked frontend could query `password`); gate it with persisted/allow-listed queries, field-level authorization, and depth/cost limits.
- **Source:** postman.com/what-is-graphql-part-one-the-facebook-years · graphql.org
- **Applied:** the interviewer's claim is preserved as a faithful record but flagged inline as inverted, with the full correction in the Canonical-answer section. **Do not repeat this claim in an interview.**

### 🟡 CORRECT-BUT-INCOMPLETE — async/await = "syntactic sugar via generators" — [[02-async-promises-event-loop]]

- Conceptually equivalent to a generator + Promise state machine (and older transpilers *did* use generators), but modern engines (V8, SpiderMonkey, JSC) implement `async/await` **natively**, not by transforming to generators. Softened in the article.
- **Source:** v8.dev/blog/fast-async

### 🟡 CORRECT-BUT-INCOMPLETE — "CommonJS cannot `require` an ES module" — [[03-nodejs-runtime-internals]]

- Overstated. Modern Node **can** `require()` a *synchronous* ES module (one without top-level `await`); only ESM with **top-level `await`** forces dynamic `import()`. Corrected in the article.
- **Source:** nodejs.org/api/esm.html

### 🟡 CORRECT-BUT-INCOMPLETE — "a stateful app's docker-compose must include a database service" — [[06-testing-git-docker]]

- It's a best-practice/architectural signal, not a hard rule — a stateful app can point at an *external* managed database not defined in the same compose file. But for an **intern's personal to-do app**, a missing DB service is a valid red flag that state/persistence wasn't thought through. Framed as a signal, not a law, in the article.
- **Source:** docs.docker.com/compose

## Verification method

- **Workflow `wf_a6a465f8-155`** — 13 agents (6 drafters → 6 refute-first verifiers → 1 completeness critic), 0 errors / 0 empty / 0 skipped, ~811K tokens, 110 tool calls, ~5.5 min. Each verifier was instructed to *try to disprove* every load-bearing claim via live WebSearch/WebFetch, defaulting to skepticism.
- **Main-loop QA (maker/checker):** the two verifier-suggested edits were reviewed before applying. The GraphQL edit was **not** applied verbatim — the verifier wanted to overwrite the faithful "what the interviewer said" record with the correction, which would have broken faithfulness; instead the claim is kept as-recorded with an inline flag + the correction alongside.

See [[caveats-and-corrections]] for the ASR-garble map and every correction applied at compile.
