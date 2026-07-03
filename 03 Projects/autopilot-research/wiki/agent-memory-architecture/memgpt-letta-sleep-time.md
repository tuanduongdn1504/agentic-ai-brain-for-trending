# MemGPT → Letta — the OS metaphor and sleep-time compute

## Source

- Paper: **"MemGPT: Towards LLMs as Operating Systems"** — Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, Joseph E. Gonzalez (UC Berkeley). [arXiv:2310.08560](https://arxiv.org/abs/2310.08560), submitted 2023-10-12, revised 2024-02-12.
- Paper: **"Sleep-time Compute: Beyond Inference Scaling at Test-time"** — Kevin Lin, Charlie Snell, Yu Wang, Charles Packer, Sarah Wooders, Ion Stoica, Joseph E. Gonzalez. [arXiv:2504.13171](https://arxiv.org/abs/2504.13171), submitted 2025-04-17.
- Company/product: **Letta** ([letta.com](https://letta.com), [docs.letta.com](https://docs.letta.com)) — founded by the MemGPT creators (UC Berkeley Sky Computing Lab; advisors Ion Stoica + Joey Gonzalez; backers incl. Jeff Dean). Repo [letta-ai/letta](https://github.com/letta-ai/letta): **23.6K★** (2026-07). All claims below double-verified against arXiv/letta.com/docs.
- Note: don't confuse Letta memory stores with **Anthropic Managed Agents memory stores** ([[how-claude-memory-works]]) — same name, different products.

## MemGPT (2023): where "context = RAM" comes from

- Draws explicitly on "hierarchical memory systems in traditional operating systems that provide the appearance of large memory resources through data movement between fast and slow memory" — main context (in-window) vs external context (out-of-window), with the LLM **paging** data between them.
- The LLM **self-edits its memory** via tool calls and uses interrupts for control flow — "agents that remember, reflect, and evolve across long-term conversations."
- The video's "working memory / context RAM" phrase is this paper's metaphor, secondhand.

## Letta today: four memory components (docs-verified)

| Component | What it is | Video analog |
|---|---|---|
| Message buffer | Recent messages | Current chat history |
| **Core memory** | In-context **memory blocks** the agent itself edits — each block has label, description, value, character limit, optional read-only flag; prepended to the prompt XML-style | The always-loaded profile/facts slice |
| **Recall memory** | Complete interaction history, searchable | Episodic memory |
| **Archival memory** | "Semantically searchable database" — unlimited, tag-organized, **vector-based retrieval** ("searching 'artificial memories' finds 'implanted memories'") | Semantic memory in a vector store — **the one major system where the video's substrate claim is true** |

## Sleep-time compute: the production consolidation agent

- Paper result: models "think offline about contexts before queries are presented" — context preparation + query amortization → **~2.5× less test-time compute** for equivalent accuracy on Multi-Query GSM-Symbolic (~5× on Stateful AIME), and **+13–18% accuracy** when scaling sleep-time compute itself. (Metric is benchmark-specific — don't quote "2.5×" as universal.)
- Production architecture: **dual agents** — a primary agent handles user conversations; a **sleep-time agent** edits and refines memory **asynchronously** ("memory management happens asynchronously rather than blocking user interactions"), in an "anytime" fashion the primary agent can read mid-improvement.
- **Trigger**: configurable frequency — "the higher the frequency setting, the more tokens your agent will use." Not a fixed N-conversation gate.
- **The model-assignment nuance that half-inverts the video**: Letta's docs recommend a **fast model on the primary agent** (e.g. gpt-4o-mini) and a **larger/stronger model on the sleep-time agent** "since the latter faces no latency constraints." The video's "cheaper summarizer" is one valid cost profile; Letta's default logic is speed-on-the-hot-path, strength-on-the-background-path. See [[consolidation-gate-design]].
- Follow-on research (letta.com/research, fetched): "Memory Models: Towards Agents That Learn" (2026-06) — memory-native RL that optimizes "the generation and curation of token-space memory"; named failure modes: consolidated memories going "generic and lossy after repeated refinements" or "overly specific rather than generalizable." Those two failure modes are the design checklist for any summarizer agent.

## Key Takeaways

- MemGPT/Letta is the **closest real implementation of the video's whiteboard** — including the one place vector storage genuinely appears (archival memory) — and the strongest evidence that a background consolidation agent is a production pattern, not a fantasy.
- The **latency-vs-strength split** is the transferable design rule: put your cheap/fast model where the user waits; consider your strong model where nobody waits. "Cheaper summarizer" is a budget decision, not an architecture law.
- Letta's memory-quality failure modes (generic-and-lossy vs overly-specific) are the two things to test for in any consolidation pilot — including the vault's own `consolidate-memory` runs.
