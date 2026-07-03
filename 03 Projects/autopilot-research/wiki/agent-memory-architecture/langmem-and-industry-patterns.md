# LangMem and the industry articulation of the triad

## Source

- **LangMem SDK** — LangChain, released **2025-02-18**: [langchain.com/blog/langmem-sdk-launch](https://www.langchain.com/blog/langmem-sdk-launch) + memory concept docs at docs.langchain.com. Both verifiers CONFIRMED with direct quotes. (⚠️ the workflow's completeness critic declared LangMem "no credible product by this name / confabulation" — a **critic misfire**, overridden by the two verifier fetches of the announcement itself; logged in [[source-provenance]].)

## LangMem's triad (quoted from the announcement)

- **Semantic memory** — "stores facts and knowledge that ground agent responses, such as user preferences; knowledge triplets." Two shapes in the docs: **profile** (one continuously-updated document) vs **collection** (many retrievable items) — a genuinely useful distinction the video doesn't make.
- **Procedural memory** — "saving learned procedures as **updated instructions in the agent's prompt**" — i.e., the agent rewrites its own rules over time. One step beyond static SKILL.md files.
- **Episodic memory** — "the form of **few-shot examples**, with each example distilled from a longer raw interaction" — episodic memory as curated exemplars, not just a log. Another angle the video misses.

Plus the formation-timing axis that names the video's gate: **hot-path** memory formation (write during the conversation) vs **background** formation (a separate process consolidates afterwards — LangChain's own "subconscious" framing). The video's consolidation gate = background formation.

## The adjacent ecosystem (verified where stated)

- **Reflexion** — Shinn et al. 2023, [arXiv:2303.11366](https://arxiv.org/abs/2303.11366): verbal self-reflection stored in an episodic buffer to improve later attempts — consolidation as *learning from failure*.
- **Mem0 / Zep (Graphiti)** — production memory-infrastructure vendors implementing extraction + consolidation as a service; Zep's Graphiti adds a temporal knowledge graph. (Named by the workflow critic as missing originals; existence corpus-known, details not deep-dived here.)
- **HippoRAG** (2024) — hippocampus-inspired consolidation into a knowledge graph for retrieval. (Attribution in the critic's output was garbled — cite the paper only after fetching it; flagged in [[caveats-and-corrections]].)
- **RecMem** ([arXiv:2605.16045](https://arxiv.org/abs/2605.16045), 2026-05) — "Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents": distills episodic memory into semantic memory, explicitly using cheaper summarizer processes — recent academic backing for the video's cost framing.
- **xMemory** (VentureBeat, 2026) — reflector-driven consolidation: detects conversation boundaries, summarizes episodes, extracts semantic facts, synthesizes themes via auxiliary LLM calls, async or micro-batched. The "50–200 episodes" consolidation cadence sometimes quoted for production systems traces to secondary write-ups like this — **treat it as design guidance, not a verified constant** (verifiers: UNVERIFIABLE from primary sources).

## Key Takeaways

- LangMem is the most direct industry restatement of the video's triad — nine months before the video — and adds three distinctions worth adopting: **profile vs collection** semantic memory, **episodic-as-few-shot-examples**, and **hot-path vs background** formation.
- LangMem's procedural memory (self-updating prompt instructions) is the bridge between static skills ([[../claude-skills/_index]]) and Letta's memory-native RL ([[memgpt-letta-sleep-time]]).
- The consolidation-cadence folklore ("every 50–200 episodes") has no primary source — production systems that disclose anything use time-based (Claude 24h), importance-based (Generative Agents ≥150), or continuous-async (Dreaming V3) triggers. See [[consolidation-gate-design]].
