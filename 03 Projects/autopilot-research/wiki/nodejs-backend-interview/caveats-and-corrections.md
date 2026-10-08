# Caveats & Corrections

## ⚠️ This source is a heavily-garbled auto-caption

The only transcript available was YouTube's **Vietnamese auto-caption** track (no human subtitles). Auto-captioning mangled nearly every technical term. Every technical term in the wiki is the librarian's **reconstruction of intent** from context, not a literal caption. The compiled articles are trustworthy; the *raw captions* are not quotable. Treat any single "quote" from this source with caution.

## ASR garble → intended term (map)

| Caption garble (examples) | Actual term |
|---|---|
| "M data structure", "M", "MC" | **Map** (and Map-vs-Object) |
| "set structure" | **Set** |
| "errow / error / lamda function" | **arrow function** |
| "comback", "call back" | **callback** |
| "Singway", "Singabaya", "Sing", "ing function", "away" | **async / await** |
| "cost", "call ST", "constat" | **call stack** |
| "ST overflow", "ST flow" | **stack overflow** |
| "de quy" | **đệ quy** (recursion) |
| "comment js / comment chs" | **CommonJS** |
| "is modal / yes modal" | **ES Module** |
| "grap q", "Graql", "RQL", "grap" | **GraphQL** |
| "abbi", "Wing API", "and ai" | **API / REST API** |
| "defensy / depending / defensive injection", "de injection", "independent eject decy ejection" | **dependency injection** |
| "in version" | **dependency inversion** |
| "container di", "di container" | **DI container** |
| "loosely couping" | **loosely coupling** |
| "user repo / user report" | **UserRepository** (repository pattern) |
| "Gabage collector", "grap slector", "gravit collector", "máy dòng/dọn rác" | **garbage collector** |
| "event lo / event loot" | **event loop** |
| "in blocking operation" | **non-blocking operation** |
| "M thread", "một tay trading", "M trading" | **single-thread / multi-thread** |
| "SCM" | **SCRUM** |
| "spring" | **sprint** |
| "tch", "sub tch", "x" | **task / subtask** |
| "con request" | **pull request** |
| "con lọc for" | **for loop** |
| "ber", "do container" | **Docker / Docker container** |
| "op / OB" | **OOP** |
| "impar programming" | **imperative programming** |
| "dân bách khoa" | **Bách Khoa (Polytechnic University) student** |
| "B time" | **part-time** |

### Terms garbled beyond confident recovery (flagged, not asserted)

- The candidate's to-do-app UI language ("code bằng **ship**") — could not be recovered; **not asserted** in the wiki.
- The design pattern the candidate gestured at before the DI pivot ("**chest**") — possibly Strategy; **not asserted**.
- The functional-programming languages he named in coursework ("**dòng list / prolog / HCO**") — likely Lisp / Prolog / Haskell; **not asserted** as fact.
- A stray year "**2016**" in the scheduling small-talk — context unclear; **not asserted**.

## Corrections applied at compile (4)

These came from the refute-first verifiers ([[claims-scorecard]]) and were applied to the article bodies:

1. **GraphQL origin (🟠 MISLEADING — the interviewer's claim).** He said GraphQL "wasn't built for the frontend." The real history is the opposite (Facebook 2012, for mobile clients). Preserved as a faithful record of what he said, flagged inline as inverted, corrected fully in [[04-rest-graphql-api-design]] Q15f. **The single most important thing to un-learn from this interview.**
2. **async/await "via generators" (🟡).** Softened: modern engines implement it natively, not by transforming to generators. [[02-async-promises-event-loop]]
3. **"CommonJS cannot require ESM" (🟡).** Corrected: modern Node can `require()` a *synchronous* ESM; only top-level-`await` ESM forces dynamic `import()`. [[03-nodejs-runtime-internals]]
4. **"docker-compose must have a DB service" (🟡).** Reframed as an architectural *signal* for an intern's project, not a universal rule. [[06-testing-git-docker]]

## Maker/checker override (fail-loud)

One verifier-suggested edit was **rejected** by main-loop QA: it wanted to overwrite the faithful "Interviewer taught" record of the GraphQL claim with the correction. Applying it would have made the article falsely report that the interviewer taught the *correct* history. Instead the claim is kept verbatim-in-substance with an inline ⚠️ flag and the correction placed alongside. Reporting the override here per the vault's "fail loud" rule (Rule 12).

## Small-talk excluded

The interview opens with ~1 minute of pre-roll chatter (study-abroad plans, French-language program, 3-vs-4-year tracks) that is partly about a third party and is not part of the technical screen. It is excluded from the articles as noise; noted here for completeness.

## Not independently verified

- The **individual's identity/school** beyond what the video states (name in title; "Bách Khoa" + "software engineering" self-reported). Held to what the source says; not cross-checked, and not the point of this topic.
- The **company** is never named on camera; the internship logistics (~4 interns, train-to-convert, part-time) are the interviewer's own statements.
