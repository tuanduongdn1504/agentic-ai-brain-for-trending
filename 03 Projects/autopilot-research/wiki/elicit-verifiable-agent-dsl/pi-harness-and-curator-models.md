# The curator's harness — "Pi with the Anthropic models"

## Source

- EN transcript lines 301–320; pi identity ground-truthed 2-lens + main-loop pi.dev fetch 2026-07-04 ([[source-provenance]]).

## What Brady said (verbatim-verified)

- The **wrapper** in front of the curator "lets us swap in and out different harnesses."
- "We have an **agent SDK implementation** for the curator. We also have tried using **Pi with Claude** and **Pi with Codex**. *Probably not supposed to say Codex*, but we did try that out."
- "It's really important to us that the curator is using the best models and harnesses available. So at the moment we're using **Pi with the Anthropic models**. That's the best combination for us."

## Pi = the pi coding agent (Earendil Inc. / Mario Zechner) — identification near-certain

Ground truth (main-loop fetch of pi.dev, 2026-07-04 + verifier fetches):

- **pi** is a "minimal agent harness" by **Earendil Inc.** — created by **Mario Zechner** (badlogic); repo moved `badlogic/pi-mono` → `earendil-works/pi` on **2026-04-08** (Zechner's "I've sold out" post; also covered by Armin Ronacher). npm: `@mariozechner/pi-coding-agent`.
- Runs as "interactive, print/JSON, RPC, **and SDK**" — the SDK mode makes it **embeddable** as a curator harness (pi.dev cites OpenClaw as an integration example — cross-link [[../claude-code-clones/_index]]).
- Providers: "Anthropic, OpenAI, Google, Azure, Bedrock, Mistral, Groq, Cerebras, xAI... and more" — so "Pi with Claude" and "Pi with Codex" are both natively expressible.
- Philosophy fit: pi ships no MCP/sub-agents/plan-mode in core — extensions supply them. Elicit doesn't need any of that for a curator that only writes ÆPL.
- The vault already holds a Storm Bear curated wiki on pi-mono ([[external|Storm Bear: pi-mono]], `_state/04-projects-v30-v39.md`; ~39K★ era April 2026) — this is the **first corpus sighting of pi embedded as a production product component** rather than used as a terminal coding agent.

**Honesty line:** no public partnership/deployment evidence links Elicit↔pi beyond Brady's own on-stage statement. Identification rests on: unique name fit among agent harnesses + SDK embeddability + exact provider fit + timeline fit (Earendil transition 42 days before the talk). Alternatives refuted: Inflection's Pi is a consumer chatbot, not a harness. Verdict: CONFIRMED-by-convergence, single-source on the link itself.

## The Codex aside — and a verifier misfire worth remembering

- "Probably not supposed to say Codex" reads as **naming a rival's product at the host vendor's conference** (an Anthropic event, an OpenAI harness/model family) — and possibly hinting at unannounced evaluation work.
- One refute-lens verifier explained the aside as "Codex was deprecated in 2023, awkward to reference" — **stale-cutoff misread**. The 2023 deprecation hit the *original Codex API*; by May 2026 Codex is OpenAI's **active** agentic-coding family, as this vault's own [[../codex/_index]] topic and the Storm Bear v62 codex-plugin-cc entry document. Logged in [[caveats-and-corrections]] (misfire class: refuting retired-then-relaunched brands from stale memory — sibling of the mosh pass's GPT-4.1 misfire).

## Why this matters beyond trivia

- **Harness-swappability paid off**: SDK-impl → pi, Claude ↔ Codex experiments — the wrapper (checklist item 2, "would recommend") is what made "use the best available" an operational reality instead of a rewrite.
- It's a live datapoint for the corpus harness thread ([[../harness-engineering/_index]]): a company whose *product* is an agent still chose a third-party harness for the planning brain, and kept the interpreter in-house.

## Key Takeaways

- Elicit's production curator = **pi harness + Anthropic models** (as of 2026-05-20), after real cross-vendor experiments.
- Pi's SDK/RPC modes are the embeddable-harness category the corpus predicted pi-mono would seed — first production sighting.
- Keep the harness behind a wrapper; treat harness+model as a swappable pair, benchmark, and move.
- The Elicit↔pi link is single-source (the talk) — quote it as Brady's statement, not as pi marketing.
- Misfire lesson: before explaining a vendor aside via "deprecated," check whether the brand was relaunched after your knowledge cutoff.
