# Caveats & Corrections (Rule 12 — fail loud)

Everything the ingest, the auto-captions, or a casual viewer would get wrong — surfaced loudly. Grading in [[claims-scorecard]]; deeper argument analysis in [[failure-modes]] and [[vs-harness-engineering-corpus]].

## Load-bearing corrections

1. **⚠️ Event: AI Engineer *Europe* 2026 (London, Apr 8–10) — NOT World's Fair 2026.**
   The video was uploaded to the AI Engineer channel on **2026-07-07**, which sits inside the World's Fair 2026 upload wave (SF, Jun 28–Jul 2) — so the natural assumption (and this ingest's first guess) was World's Fair. **Wrong.** Chandegra is London-based and gave this in person at **AI Engineer Europe 2026**; the July upload is a *delayed publication*. Confirmed via `ai.engineer/europe/2026`, [StartupHub.ai coverage](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/ai-s-future-from-fixed-to-adaptive-engineering), [BigGo Finance](https://finance.biggo.com/news/769403a199262394), and Latent.Space's AINews Europe recap. *(Minor unresolved: one secondary source lists a "recorded 21 May 2026" date that post-dates the April event — likely an outlet error; the venue = Europe 2026 is multi-source solid.)*

2. **⚠️ "Annicha Labs" — not "Anitcha Labs."** The auto-captions render it "Anitcha" (and StartupHub.ai repeats that misspelling). First-party sources confirm **Annicha** ([annicha.co](https://annicha.co/), [rajivchandegra.com](https://rajivchandegra.com/)). This wiki uses **Annicha** throughout.

3. **⚠️ "Cline" — not "Klein."** In the harness list ([[the-two-paradigms]]) the speaker/caption renders **Cline** (formerly *Claude Dev*, rebranded v2.0 in May 2026) as "Klein." Corrected.

4. **⚠️ Pi repo has moved.** The talk cites **Pi** as a current example. Since the talk, Pi migrated from **`badlogic/pi-mono` → `earendil-works/pi`** (repo) and **`@mariozechner/pi-coding-agent` → `@earendil-works/pi-coding-agent`** (npm), around **April–May 2026**, when Mario Zechner joined the venture-backed **Earendil Inc.** (public-benefit corp co-founded by Armin Ronacher, creator of Flask). Zechner's own announcement: *"I've sold out"* (2026-04-08). MIT; ~62K★ by June 2026. The corpus's **pi-mono** entry (Storm Bear v36) predates this move — flag for update.

## Attribution gaps (correct content, missing credit)

5. **Cynefin / Dave Snowden — unnamed.** The complicated-vs-complex distinction and "probe–sense–respond" are **Cynefin** (Snowden, 1999), used accurately but never credited. Attach the name whenever this idea is reused from the vault.
6. **Boids / Craig Reynolds — unnamed.** The flocking rules (align / don't collide / stay close) are the **boids** model (Reynolds, 1986). Accurate, uncredited.

*(Ackoff's "mess" and the Taylor/Taylorism reference **are** correctly attributed in the talk — a point in the speaker's favor.)*

## Thesis critique (steelman + objections + novelty)

The independent critique agent's assessment — carry this whenever the topic is cited as "the future of engineering."

**Steelman (the strongest version of the thesis):**
> As AI leaves chatbot contexts for autonomous, multi-agent, real-world domains where capability and problem structure vary unpredictably at runtime, pre-runtime specification hits a hard wall — *you cannot specify what you cannot predict.* The alternative is constraint-based design: specify only invariants/rules-of-play and let viable agent configurations self-organize and stabilize emergently. This flips the failure mode from *brittle over-specification* to *graceful degradation under deviation.*

**Four objections the talk does not answer** (full version in [[failure-modes]]):
1. **Falsifiability/actionability gap** — a research direction, not a Monday-morning practice; boid physics is deterministic, LLM orchestration isn't.
2. **Rebrand without attribution** — MAS, swarm intelligence, polycentric governance (Ostrom), constraint programming are decades deep and uncited; not shown to be mechanically different for LLMs.
3. **Legibility collapse is reckless in regulated domains** (medicine, recruiting, finance) — "the agents self-organized" is not a defense. *(The speaker is a physician — the domain least tolerant of this.)*
4. **No working-implementation proof** — fixed harnesses have shipped wins; emergent orchestration has a simulation.

**Novelty verdict:** *Not novel* (complexity science, boids 1987, Ostrom, constraint programming). *Possibly domain-novel* as a **strategic hypothesis** (horizontal > vertical intelligence for LLMs), but that's a bet, not a mechanism. **"A research question, not a validated principle. A direction to watch, not a practice to adopt"** — until an emergent system beats a fixed harness on a non-toy problem while staying legible.

## What is solid vs speculative

- **Solid:** the science/history references (10/11 CONFIRMED), the harness definition, the complicated/complex framing, the self-named failure modes, the "harness > model" premise.
- **Speculative (by the speaker's own admission):** the entire adaptive-engineering prescription "rests on two assumptions" — that models keep improving exponentially, and that AI moves off-screen into the physical/social world. Both are plausible but unproven; the talk is explicitly about *what comes next*, not what works now.

## Key takeaways

- The only content **error** is the **venue** (Europe, not World's Fair) — everything else is spelling/attribution/currency.
- Fix on reuse: **Annicha** (spelling), **Cline** (spelling), **Pi → earendil-works** (currency), **Cynefin + boids** (credit).
- The talk is **honest and well-read**; its weakness is **prescriptive, not factual** — no implementation, no evidence it beats a fixed harness.
- Treat as **frontier-watch**, and pair every citation with the four objections.
