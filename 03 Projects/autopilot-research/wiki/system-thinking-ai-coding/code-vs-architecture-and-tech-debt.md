# Code (easy) vs Architecture (expensive): "easy, not cheap" + the jagged frontier

## Source

[`raw/2026-07-07-system-thinking-ai-coding.md`](../../raw/2026-07-07-system-thinking-ai-coding.md) [00:07:14]–[00:15:29], [00:10:14]. See [[overview]] and [[compiler-vs-llm]].

## "Easy" is not "cheap"

- He corrects a lazy phrasing: coding isn't getting *cheaper*, it's getting **easier**. **"Dễ nhưng không hề rẻ"** — easy but not cheap.
- **The price is deferred to the future** — the industry calls it **technical debt (nợ kỹ thuật):** wrong folder/structure, short-term hacks, hard-coding, dirty data, missing rate-limiting, no proper error handling.
- Real audit example: an MVP with real users and 3rd-party integrations (Google OAuth, image processing) that *looked* impressive — but the code was 1000+-line God components mixing user logic and business logic, no rate-limiting, no clean error handling.
  - Runs fine locally and at ~10–20 users. **Dies well before thousands of users.** "The app runs normally only because it hasn't reached the moment of collapse yet."
- Diagnostic: ask the [[three-golden-questions]] of such a codebase and you get "stored everywhere / don't know", UI-designed-before-DB, and "no idea what breaks if I delete this."

## The AI-generated "smell"

- Auditing his own team's AI-heavy output, he can spot pure-AI code immediately: **it loops around, lots of lines, but solves nothing** — "the model's blind spot." Many lines ≠ progress.

## The jagged technological frontier

- He cites **"jagged technological frontier"** (VN: *đường/danh giới công nghệ răng cưa*) from **Harvard researchers**: AI is **astonishingly sharp in some places and surprisingly, absurdly dumb in others** — *within the same session, the same model, the same operator.*
- Consequence: the person driving the AI **must know where the frontier is** — which parts the model does well, and which parts it is *silently* getting wrong (security holes, logic errors) for the product owner.
- **Verified:** this is a real paper — Dell'Acqua, McFowland, Mollick, Lifshitz-Assaf, et al., *"Navigating the Jagged Technological Frontier"* (HBS working paper 2023; pub. *Organization Science* 2026), 758 BCG consultants: **inside** the frontier AI users did +12.2% more tasks, 25.1% faster, higher quality; **outside** it they were **19% *less* likely** to produce correct solutions. See [[source-provenance]] and [[junior-crisis-and-hiring-2026]].

## The knock-on: boundaries dissolve

- AI erases the old front-end / back-end / DB / DevOps silos. A developer "must now do everything" — but the competency is **orchestration**, not hand-coding everything. Composer/conductor, not session musician (see [[what-system-thinking-is]]).

## Key Takeaways

- **AI makes code easy, not cheap** — the difference shows up as technical debt that detonates *at scale*, not in the demo.
- "Runs fine" is the trap: local/low-traffic success hides the absence of state ownership, feedback, and bounded blast radius.
- The **jagged frontier is real and cited correctly**; the operator's job is to map it and guard the silent-failure zone.
- Cross-links: [[compiler-vs-llm]] (why silent failure is intrinsic to a probabilistic tool), [[fullstack-docker-cicd]] (production-gap audit as a lens), [[ai-engineering]] (demo→production).
