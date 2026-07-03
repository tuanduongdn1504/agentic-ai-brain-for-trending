# Ubiquitous language for LLMs — the DDD move

## Source

- Transcript `raw/2026-07-03-pocock-real-feature-build.md` · glossary verified in-repo: [`CONTEXT.md` in mattpocock/course-video-manager](https://github.com/mattpocock/course-video-manager) · skill lineage verified in [mattpocock/skills](https://github.com/mattpocock/skills).

## The idea

- From Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software* (2003): a **ubiquitous language** is a shared, model-based vocabulary that bridges **developers ↔ domain experts**, used consistently in speech, docs, and code.
- **Matt's twist:** in AI-assisted development, **the human is the domain expert and the LLM is the dev.** "This is exactly what the LLM has to have with me… we need some kind of shared language so that we can talk together precisely."
- The artifact: a glossary file in the repo (**`CONTEXT.md`** in course-video-manager) that agents naturally hit when they grep/explore — "whenever the LLM is searching for stuff about ghost lessons, it's going to come across this ubiquitous language file."

## What the verified glossary contains (course-video-manager `CONTEXT.md`)

- **Ghost lesson** — exists in the DB but not on the filesystem (until materialized). Sibling entries: ghost section, ghost course (no file path).
- **Materialize** — "the act of transitioning a ghost entity to a real entity by creating its on-disk representation."
- **Materialization cascade** — the chain reaction when materializing a lesson inside a ghost course: assign file path to course → materialize section → materialize lesson.
- **"Aliases to avoid"** — each term lists banned synonyms (e.g. "create on disk", "realize") — negative guidance, not just definitions.
- **Lesson authoring status** (todo/done) kept distinct from fsStatus (ghost/real) — a schema-level invariant, not just prose.

## The payoff, demonstrated live

- Mid-grilling Matt fumbles: "when you press um convert-to or reveal-in-file-system or whatever the button is…" then recovers via the glossary: **"when you materialize a ghost lesson, you should have a modal that forces you to materialize the course as well."** — "Look how much cleaner that language is."
- Later payoffs: PRD module names come out right "because we've got this concept of the ubiquitous language"; future bug reports can say "there's a bug inside the materialization cascade" and land precisely.
- **Maintenance loop:** after each grilling session he has the LLM **update the glossary** with any new terms ("I've been trying this for a few days"), accepts the edit, and commits it himself.

## Skill lineage (verified 2026-07-03, operator ground-check)

- `skills/deprecated/ubiquitous-language/SKILL.md` — the original skill (`disable-model-invocation: true`): scan conversation → flag ambiguities/synonyms/overloads → propose canonical glossary → write `UBIQUITOUS_LANGUAGE.md` with **term / definition / aliases-to-avoid** tables. **Deprecated, not deleted.**
- Superseded by **`skills/engineering/domain-modeling/`** (SKILL.md + CONTEXT-FORMAT.md + ADR-FORMAT.md): the *active* discipline — "challenging terms, inventing edge-case scenarios, and writing the glossary and decisions down the moment they crystallise"; supports multi-context repos via `CONTEXT-MAP.md`; creates files **lazily**; pairs the glossary with **lazy ADRs**. It explicitly distinguishes *changing* the model (this skill) from merely *reading* `CONTEXT.md` (a one-line habit any skill can do).
- Note: this vault's Brain-setup v2 pattern already cross-ported the lazy-ADR idea from Matt's `/grill-with-docs` (Storm Bear v57) — the domain-modeling skill is the same lineage, matured.

## Prior art and convergence (from the deep-dive, verified subset)

- **Eric Evans (2003)** — the origin; also see Martin Fowler's bliki entry on UbiquitousLanguage.
- **Daniel Schleicher (Jan 2026)** and **Dev|Journal (May 2026)** independently proposed living glossaries to de-ambiguate specs for AI agents — community convergence, not lineage from Matt.
- The **AGENTS.md** ecosystem includes glossary sections — institutional recognition of the pattern (cf. [[../google-antigravity-skills/_index]] portability findings).
- **Attention rationale (interpretation, not proven):** Matt argues Q&A co-location and glossary hits create attention "hot spots". Related research is about **relative distance** between facts degrading retrieval (arXiv:2410.01985 is *Lost-in-Distance*, distinct from lost-in-the-middle). Directionally supportive; no controlled study validates the glossary→quality causal link.

## Key Takeaways

- A repo glossary is the **cheapest alignment artifact in the corpus**: one markdown file, no infra, immediately improves both human dictation and agent naming.
- Write **aliases to avoid**, not just definitions — disambiguation is the hard half.
- Make maintenance part of the loop (post-grill update), or the glossary rots like any doc.
- The matured form pairs **glossary + lazy ADRs** (domain-modeling skill) — vocabulary AND decisions, created only when something crystallizes.
- Cross-links: [[grill-me-in-practice]] (where terms get minted) · [[prd-and-issues-pipeline]] (where they pay off) · [[../claude-code-memory-systems/_index]] (glossary-as-curated-memory).
