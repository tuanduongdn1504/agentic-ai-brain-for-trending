# CoALA — the canonical taxonomy the video re-derives

## Source

- Paper: **"Cognitive Architectures for Language Agents"** — Theodore R. Sumers, Shunyu Yao, Karthik Narasimhan, Thomas L. Griffiths (Princeton). [arXiv:2309.02427](https://arxiv.org/abs/2309.02427), submitted 2023-09-05, v3 2024-03-15, published in **TMLR (2024)**. (Verified via arXiv abstract + HTML fetches; verifier lens-1 CONFIRMED; lens-2 agent died on a schema retry-cap and is logged in [[source-provenance]].)
- Companion list: [ysymyth/awesome-language-agents](https://github.com/ysymyth/awesome-language-agents) — "List of language agents based on paper 'Cognitive Architectures for Language Agents'" (~80+ papers organized by the framework: ReAct, Reflexion, Voyager, AutoGen, MetaGPT…).

## What CoALA defines (fetched, quoted)

**The four memories:**

- **Working memory** — "maintains active information as symbolic variables for the current decision cycle, including perceptual inputs, active knowledge, and core information carried over from previous cycles."
- **Episodic memory** — "stores experiences from earlier decision cycles… training pairs, historical event flows, game trajectories, or other representations of the agent's past experiences."
- **Semantic memory** — "the agent's knowledge about the world and itself." Traditionally initialized from external databases; "language agents can autonomously write new knowledge derived from reasoning."
- **Procedural memory** — "divided into **implicit knowledge stored in LLM weights** and **explicit knowledge in agent code**." (The half the builder ecosystem usually drops: the model itself is procedural memory.)

**The decision cycle:** planning stage — *Proposal* (generate action candidates via LLM sampling) → *Evaluation* (heuristics, learned values, or LLM reasoning) → *Selection* (argmax/softmax) — then *Execution*, observation, repeat. Memory reads/writes are **internal actions**; tool/API/environment calls are **external actions**.

**The consolidation lineage:** CoALA explicitly describes Generative Agents as the episodic→semantic model — "Generative Agents uses retrieval and reasoning to generate reflections on their episodic memory (e.g., 'I like to ski now.') which are then written to long-term semantic memory." That sentence is the video's consolidation gate, in a 2023 paper. See [[generative-agents-reflection]].

## Mapping the video's whiteboard onto CoALA

| Video element | CoALA concept | Fidelity |
|---|---|---|
| Working memory / "context RAM" | Working memory | High (plus MemGPT's RAM metaphor) |
| Procedural = skills as SKILL.md | Procedural memory (explicit half) | High — but drops the weights half |
| Semantic = durable facts/profile | Semantic memory | High on role; the vector-store substrate is the video's addition, not CoALA's |
| Episodic = dated events/chats | Episodic memory | High |
| Consolidation gate → summarizer → semantic | Memory-update internal actions; the Generative-Agents reflection pattern CoALA cites | High on concept; trigger details are the video's invention |

## Key Takeaways

- CoALA is the **single best citation** for the taxonomy — peer-reviewed, explicit cog-sci grounding ([[memory-taxonomy-and-cogsci-lineage]]), and an organizing framework ~80+ agent papers already use.
- Its sharpest under-used idea: **memory operations are actions** in the same decision loop as tool calls — designing "when do I write/consolidate memory" deserves the same rigor as designing the tool surface.
- The video's whiteboard is essentially CoALA-with-a-vector-DB-drawn-in — valuable pedagogy, but read CoALA (or this page) before citing the architecture in a design doc.
