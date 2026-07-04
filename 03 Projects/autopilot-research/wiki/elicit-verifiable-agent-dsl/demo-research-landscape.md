# Demo — biology foundation-model research landscape

## Source

- EN transcript lines 432–717; demo orgs/agreements ground-truthed against primary sources ([[source-provenance]], demo-claims verdict CONFIRMED, zero refutations).

## What the demo did

- Entry point: elicit.com templates (create table, slides, draft report) → **"research landscape."**
- Initial query: *"map the companies and institutions investing in foundation models for biology."*
- Elicit **asked one narrowing question first** (broad landscape vs. a specific model vs. academic-vs-companies) — the "clarifying question first" behavior documented in Elicit's Dec-2025 Research Agents launch. Brady chose "broad landscape."
- Then ÆPL drove every step: academic-paper searches (genomic foundation-model pre-training, transformers), web searches, full-text fetch ("enrichment"), screening ("curating" = filtering), joins.
- Output = an **artifact** (a table): each row an org with attributes (foundation models created, modalities, notable collaborations).

## The two artifacts and the "join"

1. **Orgs table** — surfaced **Howard Hughes Medical Institute, Stanford University, GDM (Google DeepMind), Meta, Microsoft Research**.
2. Brady layered on: open- vs closed-source strategy comparison → commercialization/GTM → a table of **government oversight bodies**.
3. Final step: a natural-language **join** — "see how the labs interacted with the oversight bodies" — producing a table showing e.g. **Anthropic × US AI Safety Institute** and (caption-garbled "AC in the UK") the **UK AI Safety/Security Institute**.
- The join's program was ~1,000+ lines; its head was byte-identical to the first artifact's ÆPL, replayed from cache ([[whole-program-reinterpretation]]).

## Two legibility surfaces exposed to the user

1. **The ÆPL itself** — "for each of these artifacts we can actually look at the ÆPL code that was used to generate it... literally the executable DSL behind the table." Useful mainly for **other agents** to critique ("you missed a key search... a part of the user's query you didn't take into account").
2. **A derived graph** — "derived directly from the ÆPL... not a made-up nice visualization" — searches → enrichment → extract → curate → more searches. Brady uses it to decide whether he'd "endorse the process Elicit took" and to spot when "something looks a bit skewiff."

## Real-world grounding (verification, not from the video)

The demo's named entities all have real bio-foundation-model activity, so the output isn't a hallucinated prop:

- **DeepMind** — AlphaFold 3 (2024-05-08; proteins/DNA/RNA/ligands).
- **Meta lineage** — ESM protein language models; ESM3 by EvolutionaryScale (ex-Meta founders), 2024-06-25.
- **Microsoft Research** — EvoDiff (protein generation), BioEmu, etc.
- **Stanford** — Center for Research on Foundation Models (CRFM).
- **HHMI** — AI@HHMI, ~$500M/10yr AI-in-life-sciences investment.
- **Anthropic × US AISI** — MOU signed 2024-08-29 (NIST); **UK AISI** — renamed **AI Security Institute** 2025-02-14; Anthropic UK MOU Feb 2025. So the garble "AC in the UK" ⇒ **AISI**.

(These are *external corroboration that such a landscape is real*; the demo's specific cell contents weren't independently audited row-by-row.)

## Key Takeaways

- The demo is the thesis in miniature: identical-looking table, but the process is exposed two ways (executable ÆPL + derived graph), so trust is earned, not assumed.
- "Clarify first, then plan" is a shipped Elicit behavior, not a demo flourish.
- The join shows compositionality: tables become inputs to further plans via natural language, while the plan stays a checkable program.
- Sessions are long ("a couple of hours") and layered — the artifact is a research *investigation*, not a one-shot answer.
- The output entities are real-world-grounded, which is the whole point of a data-provenance-branded product.
