# deepseek-harness

> **The agent harness where every capability above the Node runtime is a hot-swappable plugin** — graded as a *commentary layer* against the vault's nine existing source-level DSH analyses.
> Compiled 2026-08-20 · Path `/loop` · 6-video bundle (~127 min / 22,853 words) · anchor validation PASS · captions read in full, NotebookLM skipped by design.

## Why this topic exists

DeepSeek Harness had **zero coverage in this 78-topic YouTube corpus** and **nine shipped source-level analyses in the other vault** (v235–v242, including a 201MB source clone). So this is not an explainer — it is a **method experiment**: give six commentary videos to a corpus that already read the source, and record who was right about what.

**The answer is genuinely two-sided.** The source read won on governance and provenance. The video layer caught a formal paper the source read walked past, an ecosystem 6.3× larger than the vault had measured, and the only evidence of the thing actually breaking.

## The finding

**Both layers made the same class of mistake: a boundary error.** The source read treated the repository as the edge of the subject and missed the paper the repository links. The video layer treated the demo as the edge and missed the contribution policy that produced the ecosystem it was celebrating.

> **For a subject with both a repo and a commentary layer, the cheap complement to a source read is not a better source read — it is the commentary layer.** v242 was a *recursive revisit* that re-read the same artifact more carefully and still missed the paper. One 14-minute video caught it.

## What DSH is

- [[deepseek-harness/overview]] — what a harness is, the runtime shape, what "everything" excludes. **169.1k★ / 18.1k forks / MIT / developer preview** (2026-08-20).
- [[deepseek-harness/everything-is-a-plugin]] — the five independent enumerations; the agent-loop-is-editable claim; **Firecrawl's dissent** (*"solving a problem I'd say never existed"*); and the half no video mentions — it is also a **contribution policy**.
- [[deepseek-harness/cordis-and-the-paper]] — **the paper the source read missed.** *"A Programming Paradigm for Spatiotemporal Composability"*, PKU + DeepSeek, effects-and-coeffects, confluence **with its stated limits**. Cordis is **shigma's**, from Koishi, 4 years / 4,000+ plugins — DeepSeek recognized it, didn't invent it.
- [[deepseek-harness/creator-mode-and-self-modification]] — the four modes; what persists and what doesn't; **the hot-reload claim one source gets wrong**; why nobody demonstrates self-improvement.
- [[deepseek-harness/trajectory-and-observability]] — **the feature worth stealing.** Full per-turn record of what the model saw, searchable, exportable.

## The gradings

- [[deepseek-harness/hype-vs-source-scorecard]] — **the centerpiece.** What each layer caught and was blind to; five corrections owed to the other vault, recorded not executed.
- [[deepseek-harness/plugin-security-model]] — the one finding with **primary-source confirmation**: DSH's own docs call the sandbox *"containment for honest code, not a security boundary."* Four videos + three prior ships + the vendor all agree.
- [[deepseek-harness/ecosystem-and-the-catalogue-gap]] — **original finding: the `dsh-plugin` topic holds 8,874 repos; the curated catalogue is a ~16% sample.** An N=2 instance of v240's own inventory rule, applied to v240.
- [[deepseek-harness/star-velocity-and-the-superlative]] — the trajectory is real and coherent across seven readings; **"fastest growing repo EVER" is press-consensus, not primary-sourced.** The 70:1 harness-to-paper star ratio is the most informative number here.
- [[deepseek-harness/install-and-operational-reality]] — **the failure log.** Node ≥ 22.19, pnpm, the web-search-needs-a-DeepSeek-key gate, and the RC6→RC7 episode that extends v242's D24 rather than refuting it.
- [[deepseek-harness/claims-scorecard]] — **47 claims: 24 CONFIRMED / 10 CBI / 4 PLAUSIBLE-NOT-PRIMARY / 4 MISLEADING / 1 FALSE / 3 UNRESOLVED / 1 UNVERIFIABLE / 0 FABRICATED.**
- [[deepseek-harness/caveats-and-corrections]] — including **my own miscounted totals**, a PIN I nearly misapplied, and 8 unresolved items carried forward.
- [[deepseek-harness/source-provenance]] — the 6 videos, ingest method, every independent verification performed.

## Application

- [[deepseek-harness/hireui-relevance]] — **install nothing; take the trajectory.** DSH's per-turn context record is nearly a spec for the candidate-LLM legibility ADR's "answerability record." ~2h, zero install: write the trajectory-record ADR before hireui's first LLM call ships.

## Rules earned

1. **A source read that stops at the repository boundary misses the literature the repository cites.** Follow the outbound links in the file you are already quoting.
2. **A zero-code-delta version bump is not a zero-impact version bump** when third-party plugins pin your kernel's version. (Extends v242's D24.)
3. **A totals line you hand-count from a table you wrote is a second guess, not a check.** Tally the table.
4. **Cite star figures only date-stamped and marked page-stated;** never from the subject's own UI; never a velocity record.

## Cross-links

[[harness-engineering/_index]] · [[claude-code-plugins-stack/_index]] · [[claude-code-skills-stack/_index]] · [[local-ai-coding-agents/_index]] · [[open-design/_index]] · [[claude-code-observability/_index]] · [[prompt-evaluation/_index]] · [[api-security-7-techniques/_index]] · [[elicit-verifiable-agent-dsl/_index]] · [[autonomous-loops-human-in-the-loop/_index]] · [[agent-development-lifecycle/_index]] · [[agent-memory-architecture/_index]] · [[system-thinking-ai-coding/_index]] · [[wecommit-tokens-and-context-window/_index]] · [[claude-api-cost-optimization/_index]] · [[fullstack-docker-cicd/_index]] · [[miai-cv-matching-agent/_index]]
