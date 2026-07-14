# Shared language with AI — the DDD move, stage version

## Source

- Transcript `raw/2026-07-14-pocock-software-fundamentals.md` (failure mode #2 of [v4F1gFy-hqg](https://www.youtube.com/watch?v=v4F1gFy-hqg)).
- **The deep treatment of this pattern already lives at [[../pocock-real-feature-build/ubiquitous-language-for-llms]]** (verified glossary contents, skill lineage, prior art). This article records only what the *talk* adds.

## The failure mode

- The AI is **too verbose** — "talking at cross-purposes," burning words to communicate. Matt's analogy: developer meets a **domain expert** in an unfamiliar domain (microchips) — without a shared vocabulary, every exchange is lossy translation.

## What the talk adds beyond the worked example

- **The verbosity framing is new here.** The March video sold the glossary as *precision* ("look how much cleaner that language is"); the stage version sells it as **compression** — a shared language lets the model say the same thing in fewer tokens.
- **The thinking-trace observation:** Matt reports reading the model's thinking traces and finding the glossary "allows the AI to **think in a less verbose way**," which he says improves both planning *and* implementation alignment. (Self-reported, no metric — but it is the corpus' first claim that a glossary changes *reasoning traces*, not just outputs.)
- **Workflow detail:** he keeps the ubiquitous-language file **open on screen the whole time he's grilling** — the glossary is a *live instrument during planning*, not a background reference.
- Mechanically per the talk: the skill "scans your code base, looks for terminology, and creates a markdown file" of term tables — matching the deprecated skill's design documented in the sibling article.

## Skill lifecycle note (ground-checked 2026-07-14)

- `skills/deprecated/ubiquitous-language/SKILL.md` — still present, still deprecated; active successor remains `skills/engineering/domain-modeling/` (glossary + lazy ADRs). The talk (April) predates the deprecation — it captures the skill's **original, standalone form**. Lifecycle: stage demo (Apr) → daily-work maturation (documented in March video's repo) → folded into domain-modeling (by July).

## Key Takeaways

- Same pattern, second independent framing: glossary-as-precision (March) vs glossary-as-**token-compression and reasoning hygiene** (April stage) — the two sell the same artifact to different audiences.
- "Glossary open while grilling" is the cheapest process tip in the talk — pairs the two skills into one planning ritual.
- The thinking-trace claim is interesting and unverified; treat as hypothesis worth a measured pilot, not established fact.
- Cross-links: [[../pocock-real-feature-build/ubiquitous-language-for-llms]] (the deep dive — read that first) · [[design-concept-and-grill-me]] (the ritual it pairs with) · [[../claude-code-memory-systems/_index]] (glossary-as-curated-memory).
