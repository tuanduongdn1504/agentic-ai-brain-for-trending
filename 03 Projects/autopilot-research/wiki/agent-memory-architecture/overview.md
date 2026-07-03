# Overview — the whiteboard, and what's actually true

## Source

- Video: [You Can Learn AI Agent Memory System In 12 Min](https://www.youtube.com/watch?v=mY3bR9qjZr4) (Sean's AI Stories, 2026-06-19, 12:05, ~16.6K views / 783 likes)
- Raw transcript: `raw/2026-07-03-sean-agent-memory-architecture.md` (~3.6K words, read in full)
- First-party whiteboard explainer — Sean Chen's own system design, aimed at non-technical builders. No code, no dedicated repo (verified against all 91 of his GitHub repos).

## The whiteboard architecture (what the video teaches)

1. **User prompt** flows into a **working memory / "context RAM"** together with the current chat history and the system prompt — this is the only thing the LLM actually sees per call.
2. **The agent session is ephemeral** — "we're literally just making an LLM call"; nothing persists unless you save it to a database.
3. Three long-term pillars enrich working memory:
   - **Procedural memory** — how the agent should behave; skills; "usually saved in files or text… as a skill.md markdown file."
   - **Semantic memory** — durable facts + user/company profile, stored in a **vector store**, fetched by **RAG top-k** ("if K is five, the top five most relevant pieces").
   - **Episodic memory** — a dated log of events and past chats, also vector-stored; every reply/activity is appended ("save the messages/activities").
4. **The consolidation gate** — don't search the giant episodic log every time; wait until N chats pile up ("could be 20 conversations, could be 100 activities"), then feed them to a **cheaper summarizer agent** that "distills into facts" written to semantic memory. The video claims "ChatGPT and Claude and all these AI agents are all doing something similar."
5. **Efficiency rationale** — selective fetch saves tokens and latency; "the context window for most LLMs is roughly 1 million tokens… you don't want to overload your LLMs because that also makes things much slower and not accurate anymore."

## The headline finding of the deep-dive

The video's **conceptual skeleton is right and its intellectual lineage is impeccable** — every element maps onto a verified original (see [[coala-deep-dive]], [[generative-agents-reflection]], [[memgpt-letta-sleep-time]], [[langmem-and-industry-patterns]]). The **consolidation intuition is now production-universal**: OpenAI shipped "Dreaming V3" (June 2026), Anthropic ships "Dreams" for Managed Agents, Letta ships sleep-time agents — background processes that distill episodic history into durable memory.

But the **one load-bearing implementation claim is wrong**: "semantic and episodic memory are saved in vector stores" + "this is how ChatGPT and Claude memory works."

- **ChatGPT**: two independent teardowns (Simon Willison May 2025; Manthan Gupta) + OpenAI docs show **pre-computed summaries injected wholesale** into the system prompt — "No vector databases. No RAG over conversation history" (Gupta). See [[how-chatgpt-memory-works]].
- **Claude**: all four Anthropic memory surfaces — claude.ai (24-hour summary synthesis), the API memory tool (`memory_20250818`, client-side files under `/memories`), Managed Agents memory stores (filesystem-mounted text documents + the Dreams consolidation feature), Claude Code auto-memory (`MEMORY.md`, 200-line/25KB index) — are **file/summary-based with zero vector databases** in any official documentation. See [[how-claude-memory-works]].

So the corrected mental model: **the taxonomy and the gate are the durable knowledge; the substrate is a design choice.** Vector-store RAG is the right substrate when your semantic memory is big and heterogeneous (Letta archival memory, custom product memory over years of data — the video's e-commerce example is actually a good fit). Files-plus-summaries is what the frontier vendors chose for assistant memory — smaller state, auditable, cheap, no retrieval infrastructure.

## Why this topic matters for this vault

- **hireui Goal #2**: hireui's first LLM feature (candidate-feedback summarizer / voice screening per [[../mosh-ai-powered-apps/_index]] and [[../jsm-practical-vibe-coding/_index]]) will immediately face the memory question — what does the agent remember about a candidate, a recruiter, a pipeline? This topic is the design vocabulary + the reality-checked pattern menu.
- **The operator already runs this architecture**: the `~/.claude` memory system is semantic memory (file-based, exactly the Anthropic pattern); session transcripts are the episodic log; skills are procedural memory; the `consolidate-memory` skill is the summarizer agent; MEMORY.md's 200-line budget is the working-memory constraint. The video is a mirror, not news — but it names the parts.
- **Corpus thread**: sibling to [[../claude-code-memory-systems/_index]] (tool-level, operator-facing). This topic completes the pair with the builder-level view.

## Key Takeaways

- The video is a **high-quality conceptual explainer with textbook-accurate taxonomy** — rare for a 12-minute whiteboard piece — marred by presenting one builder pattern (vector RAG) as the universal production mechanism.
- **Grade per claim**: taxonomy CONFIRMED; ephemeral-session TRUE-at-API-level (with Responses-API server-state nuance); consolidation-gate concept CONFIRMED (trigger details differ everywhere); cheaper-summarizer PLAUSIBLE-not-disclosed (and Letta half-inverts it); vector-store-universality REFUTED; "most LLMs ≈ 1M context" OVERSTATED (frontier-only, and usable ≪ advertised).
- The most useful engineering sentence the deep-dive produced: **"start with files and summaries; add embeddings when retrieval — not storage — becomes the bottleneck."**
