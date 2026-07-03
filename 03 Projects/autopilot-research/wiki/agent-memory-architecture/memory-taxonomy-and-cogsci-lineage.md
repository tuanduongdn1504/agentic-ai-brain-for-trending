# The memory taxonomy and its cognitive-science lineage

## Source

- Deep-dive dimension `cogsci-lineage` of workflow `wf_4356f040-686` (all claims verified CONFIRMED/PARTIAL, zero refutations)
- Primary anchors: Tulving 1972; Baddeley & Hitch 1974; Cohen & Squire 1980; Anderson ACT-R; CoALA arXiv:2309.02427

## The psychology originals (verified)

- **Episodic vs semantic — Endel Tulving (1972).** "Episodic and Semantic Memory," in *Organization of Memory* (eds. Tulving & Donaldson, Academic Press, pp. 381–403). Episodic = temporally-dated personal events; semantic = a "mental thesaurus" of meanings and general knowledge ("Paris is in France" without remembering when you learned it).
- **Working memory — Baddeley & Hitch (1974).** *Psychology of Learning and Motivation* 8, 47–89. Multi-component model: a capacity-limited **central executive** plus slave systems (phonological loop, visuo-spatial sketchpad). Key property: **active selection and transformation**, not passive storage.
- **Procedural vs declarative — Cohen & Squire (1980).** *Science* 210, 207–209 ("Preserved learning and retention of pattern-analyzing skill in amnesia"): amnesic patients kept learning skills while losing declarative recall — two independent systems. Human procedural memory is **unconscious** (riding a bike), basal-ganglia/cerebellum-dependent.
- **ACT-R — John Anderson (from 1976, *Language, Memory, and Thought*).** Cognitive architecture splitting declarative memory (semantic network) from procedural memory (if-then production rules); all knowledge begins declarative and is proceduralized through practice. The direct ancestor of "agent rules/skills as procedural memory."

## The migration into AI agents

- **CoALA (2023) is the explicit bridge**: the paper states it "borrow[s] terminology from cognitive science as a useful analogy" and its four-way memory decomposition (working/episodic/semantic/procedural) "echoes Tulving's trichotomy." See [[coala-deep-dive]].
- LangChain's LangMem SDK (Feb 2025) then industrialized the triad for builders; Letta, Mem0, Zep and the agent-memory vendor landscape all speak this vocabulary today. See [[langmem-and-industry-patterns]].
- The video teaches this vocabulary accurately — with no citations, presenting it as engineering intuition.

## Where AI usage diverges from the psychology (the wiki-grade nuances)

| Term | Psychology meaning | Agent-engineering meaning | Divergence |
|---|---|---|---|
| Working memory | Active, executive-controlled selection + transformation (Baddeley) | The context window | The context window is a **passive buffer** — no executive control; the "selection" is done by the harness (retrieval, compaction), not the memory itself |
| Semantic memory | Unbounded general world knowledge | App-scoped durable facts ("user_email: …", "API endpoint retired 2025-03") | Agent semantic memory is **narrow and application-specific**; the LLM's weights are the closer analog of Tulving's semantic memory |
| Episodic memory | Autobiographical events with subjective time | Dated event/interaction log | Close analog — the cleanest mapping of the four |
| Procedural memory | Unconscious motor/cognitive skill | Explicit SKILL.md files, rules, system-prompt instructions | **Inverted consciousness**: human procedural is implicit; agent procedural is the MOST explicit, human-readable artifact in the stack. CoALA also counts **implicit knowledge in LLM weights** as procedural — the video (and most builder content) drops that half |

- The video's framing "working memory = context RAM" is the MemGPT inheritance ([[memgpt-letta-sleep-time]]) — an OS metaphor layered on top of the psychology metaphor. Both are load-bearing analogies, not mechanisms.
- The consolidation gate has its own psychology echo — sleep-dependent memory consolidation (hippocampus → neocortex) — which is exactly why OpenAI ("Dreaming"), Anthropic ("Dreams"), and Letta ("sleep-time compute") all reached for sleep vocabulary. See [[consolidation-gate-design]].

## Key Takeaways

- The four-part taxonomy is 50-year-old settled psychology, imported deliberately by CoALA — the video's vocabulary is trustworthy and worth adopting as team language.
- Every term shifts meaning in the import; the two that bite in design reviews: **agent "semantic memory" is app state, not world knowledge**, and **agent "procedural memory" is explicit files, not implicit skill** — which is why it's versionable, reviewable, and portable ([[../google-antigravity-skills/_index]]).
- When someone says "the context window is the agent's working memory," the useful correction is: it's the working memory **store** without the working memory **executive** — the harness has to supply the selection function (RAG, compaction, memory files).
