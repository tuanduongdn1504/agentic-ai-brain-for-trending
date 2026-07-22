# Andrew Ng — Building Blocks, the PM Bottleneck & No Job Apocalypse

> **Source:** Andrew Ng, "The Future of Software Engineering," **AI Dev 26** (DeepLearningAI, San Francisco, ~April 28–29 2026) (`g8um2AEf5ZA`).

## Software = assembling building blocks

- Ng's core metaphor: software = **LEGO bricks** (tools, frameworks, APIs). More distinct bricks → combinatorial explosion of what you can build.
- AI coding agents make **assembling** blocks dramatically faster — both AI blocks (LLMs, RAG, agentic workflows) and non-AI (UI components, databases, auth). Blocks are **proliferating daily.**
- Implication: **knowing the building blocks** (which is hard — they change fast) is what lets you assemble quickly.

## ~100% AI coding

- Ng says his own work is **"pretty much 100% AI"** (his precise phrasing elsewhere: *"100% of my tasks now run through AI agents"*), and frontier teams trend toward ~100% AI-written code.
- The last gap (80% → 100%) matters: at 80% AI, **human review of the remaining code becomes the bottleneck**; near-100% moves much faster.
- Not a religion — hand-write the 50-line spaceship code for NASA if you must.

## The product-management bottleneck

- When building speeds up **10–100×**, **deciding what to build** becomes the new bottleneck.
- The PM-to-engineer ratio collapses: historically ~**1:8** (the video's figure; Marty Cagan's classic range is ~1:6–10), trending toward 1:1 — then **collapsing PM + engineer into a single generalist.** "Engineers who shape products, or PMs who code, move really fast."
- Other bottlenecks surface too: **design, legal/compliance, marketing, sales.** Small **AI-native generalist teams** use AI to cover these functions (e.g. AI drafts legal, a human lawyer signs off).
- Scaling past one team: **many AI-native teams with limited communication + clear API boundaries.**

## No job apocalypse

- Ng doesn't see the "AI job apocalypse"; business media (paid to get it right) increasingly agrees it's overhyped. *(He grounds this in Jevons paradox and BLS growth projections; a specific "Federal Reserve Bank of Philadelphia study" he appears to cite is **unverifiable** — see [[engineer-of-the-future/caveats-and-corrections]].)*
- **Hiring criteria for AI engineers:** (1) use coding agents effectively (Claude Code / Gemini / Codex / opencode), (2) robust knowledge of building blocks, (3) **generalist skills** (basic PM etc.). "We can't find enough of these people."
- **Parallel skill development:** as coding agents get more capable, humans need complementary skills to *drive* them well.

## Tools he showed

- **Context Hub** (open-source, released ~March 2026): feeds coding agents **up-to-date documentation** so they stop hallucinating deprecated APIs (his example: agents defaulting to OpenAI's older *Chat Completions* instead of the newer *Responses* API — note: Chat Completions is *older/not-recommended*, **not deprecated**; see caveats). Generates a ~600-line markdown doc *for the agent to read.* *(Exact co-author names are uncertain across sources — attributed here to "Ng and colleagues"; see caveats.)*
- A conversational learning product (name unclear in captions — "Code Dream" / "Code Realm" / Codoji build environment): a "conversation, not a course" with a voice agent. **The product name could not be externally verified** — treated as unconfirmed.

## Key Takeaways

- Software = **assembling proliferating building blocks**; AI agents make assembly fast, so **knowing the blocks** is the leverage.
- Frontier teams trend to **~100% AI-written code**; the last 20% matters because human review becomes the bottleneck.
- The **PM bottleneck**: deciding *what* to build now gates delivery; PM+engineer collapse into **generalists** on small AI-native teams.
- **No job apocalypse** — bright future for generalist AI engineers; hiring = use agents + know blocks + generalist skills.
- **Context Hub** fixes stale-API hallucination by feeding agents current docs.

## See also

- [[engineer-of-the-future/osmani-answerability-thesis]] — Ng's "deciding what to build" ≈ Osmani's "choose what is worth doing"
- [[engineer-of-the-future/convergent-thesis]] — building/verification/judgment as the new bottleneck
- [[quanit-becoming-ai-engineer-2026/_index]] · [[ai-engineering/_index]] — career/skill counterparts
- [[engineer-of-the-future/caveats-and-corrections]] — Context Hub authors, "Code Dream" name, Fed study, API "deprecation"
