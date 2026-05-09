# Core claims (8 falsifiable)

> Lopopolo's testable claims, ordered most-concrete → most-speculative. Each is a hypothesis subsequent research ingests should attempt to corroborate or falsify with independent evidence. Citations point to the anchor bundle (see [[anchor-bundle-overview]]).

## 1. Zero-code development at scale

The OpenAI Frontier team shipped a functional internal product with **zero human-written code** over 5 months, accumulating **1M+ LOC** in the repository.
- *talk [03:00]* · *anchor synthesis: cross-medium agreement #2*
- **Falsifier:** independent audit showing >0% human-authored lines; or, a definition of "human-written" that differs materially from Lopopolo's
- **What to check:** is "code" inclusive of config, schemas, build files? Lopopolo doesn't define explicitly.

## 2. Token-budget threshold for harness engineering

Effective enterprise-scale harness engineering requires ≈**1B tokens/day** throughput, costing roughly **$2,000–$3,000/day** at current rates.
- *podcast (cost only — talk gives volume)* · *synthesis: podcast-only #1*
- **Falsifier:** demonstrated harness-engineering productivity at <10% the token volume
- **Open:** is this a floor (below = insufficient) or a current operating point (could fall with model efficiency)?

## 3. One-minute build-loop constraint

The "inner loop" of the build system must complete in **<1 minute** or agents lose patience and productivity drops materially.
- *talk [04:43, 06:02]* · *podcast (specifies Turbo/NX migration)*
- **Falsifier:** team demonstrating high agent productivity with multi-minute inner loops
- **Why it matters:** elevates build-tooling investment from nice-to-have to operational requirement

## 4. Symphony-driven throughput

Symphony orchestration increases output from a baseline of **3.5 PRs/day/eng** to **5–10 PRs/day/eng**.
- *talk [32:46]*
- **Falsifier:** independent measurement showing Symphony adds <1.5x throughput, OR Symphony-equivalent open-source orchestrators failing to reproduce
- **Note:** baseline 3.5 not contextualized — high or low for OpenAI standards?

## 5. Hyper-modular agent-legible architecture

Repositories should be sharded into hundreds of isolated packages (Lopopolo cites **750 packages** for one small team) — superior to standard human-centric architecture for both agent context-scoping and merge-conflict avoidance.
- *podcast [01:12:24]* · *talk*
- **Falsifier:** team operating at similar agent density with monolithic architecture and equal merge-conflict rates
- **Tension:** conflicts with "premature abstraction" advice common in human-centric engineering

## 6. Post-merge code review

Humans should shift entirely to **post-merge** code review; synchronous pre-merge approval is the primary remaining bottleneck in agentic workflows.
- *talk [08:19]* · *cross-medium agreement #3*
- **Falsifier:** measurable defect-cost increase from post-merge model that exceeds throughput gains
- **Implication:** changes incident-response playbook (rollback over block-on-review)

## 7. Disposable dependencies / "vendoring"

Standard software dependencies are becoming obsolete because agents can **internalize and "vendor"** thousands of lines of external code into bespoke implementations at near-zero cost.
- *talk [26:00, 27:00]* · *Bret Taylor cited as agreeing*
- **Falsifier:** vendored implementations showing material defect rates vs upstream packages; OR, dependency complexity ceiling demonstrably stable (Lopopolo admits Datadog/Temporal exceed current capacity — open #5 in [[open-questions]])
- **Adjacent:** Postel's Law cited as explanation for upstream "bloat" that vendoring sidesteps

## 8. Model-human isomorphism (GPT-5.2+)

Reasoning models starting with **GPT-5.2** are **isomorphic to human engineers** for end-to-end software work.
- *podcast [01:53]* · *talk [04:43]*
- **Falsifier:** demonstrated task class where GPT-5.2+ systematically fails where median human engineers succeed; OR, "isomorphic" defined narrowly (e.g., "in our codebase, on our task distribution")
- **Most speculative claim** — relies on subjective judgment of equivalence

## How to use these claims

When future research ingests touch any claim above:
1. Add a section to the article referencing the claim by number (`Confirms claim 3` / `Challenges claim 7`)
2. If a falsifier emerges, append a "Status update" block at the bottom of THIS article — don't quietly edit the original claim
3. Cross-tabulate evidence in a future `claims-evidence-tracker.md` once we have ≥3 corroborating/contradicting sources per claim
