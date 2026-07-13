# agent-memory-architecture — Topic Index

> **Topic:** Sean Chen's 12-minute whiteboard "AI Agent Memory System" — and the double deep-dive into the real originals behind every element on the whiteboard (CoALA, Generative Agents, MemGPT/Letta, LangMem) plus how ChatGPT and Claude memory ACTUALLY work in production (mid-2026)
> **Source video:** [You Can Learn AI Agent Memory System In 12 Min | Semantic & Episodic Memory, RAG, Vector Database](https://www.youtube.com/watch?v=mY3bR9qjZr4) (mY3bR9qjZr4, Sean's AI Stories, 2026-06-19, 12:05, ~16.6K views, 12,342 subs at launch — **FIRST-PARTY** whiteboard design, no code/repo)
> **Compiled:** 2026-07-03 (path 5 yt-dlp + workflow `wf_4356f040-686`, 28 agents = 10 dives + 17 adversarial verifiers + critic; ~1.65M tokens, 555 tool calls + main-loop ground-checks)
> **Deepened:** 2026-07-04 — first-party Anthropic treatment of Memory Stores + Dreaming via the "Agents that remember" CWC-2026 workshop (VN dub b1qgIGwBUEI → EN original geUv4CjPpxI) + full docs/repo/announcement deep-dive (workflow `wf_c3719baa-7f2`, 18 agents; both transcripts + both docs pages read in full in main loop)
> **Deepened again:** 2026-07-13 — direct video sequel `GrNbuWWJYiI` ("...Agent Harness & Loop Engineering In 19 Min") extends the whiteboard into harness/loop-engineering/LLMOps; scouted first against all existing articles (~90% already covered), so this pass is narrow — Langfuse first-party dive + LangGraph/LangChain/PydanticAI status check (workflow, 5 agents, ~195K tokens)

## Articles

- [[overview]] — what the video teaches, the whiteboard architecture, and the headline finding (the taxonomy is real; the vector-store substrate is NOT how the big vendors do it)
- [[memory-taxonomy-and-cogsci-lineage]] — working/episodic/semantic/procedural: Tulving 1972 → Baddeley & Hitch 1974 → Cohen & Squire 1980 → ACT-R → CoALA, and where AI usage diverges from psychology
- [[coala-deep-dive]] — the canonical taxonomy paper (arXiv:2309.02427, Princeton, TMLR 2024) the video re-derives without citing
- [[generative-agents-reflection]] — Park et al. 2023: memory stream, recency×importance×relevance retrieval, and the reflection threshold — the true origin of the "consolidation gate"
- [[memgpt-letta-sleep-time]] — the OS metaphor (context = RAM), Letta's four memory components, and sleep-time compute: the production implementation of the background summarizer agent
- [[langmem-and-industry-patterns]] — LangChain's LangMem SDK triad (Feb 2025), hot-path vs background memory formation, and the adjacent ecosystem (Reflexion, Mem0, Zep, HippoRAG)
- [[how-chatgpt-memory-works]] — saved memories + injected dossier (Willison/Gupta teardowns) + the June 2026 "Dreaming V3" rewrite: summary-injection, NOT per-query vector RAG
- [[how-claude-memory-works]] — all four Anthropic memory surfaces (claude.ai 24h synthesis, API memory tool, Managed Agents memory + Dreams, Claude Code auto-memory): file/summary-based, ZERO vector DBs
- [[anthropic-memory-stores-and-dreaming]] — **(2026-07-04 deepening)** the first-party deep treatment of surface #3: CWC-2026 workshop + docs + `anthropics/cwc-workshops` repo — limits tables, dream API lifecycle, harness internals (orchestrator + 1 sub-agent per transcript), index-file demo, cost economics, Harvey 6x, press-vs-docs conflicts
- [[rag-vector-stores-and-context-limits]] — top-k RAG, the vector-store-universality correction, real context-window numbers (2026), and the context-rot evidence base (Lost-in-the-Middle, Chroma, NoLiMa)
- [[consolidation-gate-design]] — the design space of consolidation triggers (count vs time vs importance vs continuous-async) and the cheaper-vs-stronger summarizer-model decision
- [[harness-loop-llmops-sequel]] — **(2026-07-13 deepening)** the video sequel's harness/loop-engineering/LLMOps framing, cross-linked to where each piece is already covered in depth (autonomous-loops, claude-code-hooks, LangSmith, LLM-as-judge) + the "harness" variant-definition note
- [[langfuse-and-harness-tools]] — **(2026-07-13 deepening)** Langfuse first-party deep-dive (founding, YC W23, ClickHouse acquisition Jan 2026, pricing, tracing+eval features, a corrected feature claim) + verified 2026 status of LangGraph/LangChain/PydanticAI (incl. a caught fabricated GA date)
- [[caveats-and-corrections]] — every video claim graded + creator ground-check (Sean Chen, AutoManus, repo renames) + reported-only flags
- [[source-provenance]] — pipeline, workflow stats, verdicts, verifier-misfire log (incl. a critic that wrongly declared LangMem "confabulated")

## One-line thesis

A clean, teachable whiteboard model of agent memory — working memory + procedural (SKILL.md) + semantic + episodic + a consolidation gate feeding a summarizer agent — whose taxonomy is textbook-correct (CoALA lineage all the way to Tulving 1972) and whose consolidation concept is now production-universal (OpenAI "Dreaming V3", Anthropic "Dreams" — both vendors literally converged on dream-naming in 2026), but whose one load-bearing implementation claim ("semantic and episodic memory live in vector stores, fetched by RAG top-k") is **refuted by both major vendors' actual systems**: ChatGPT injects periodically-regenerated summaries wholesale, and every Anthropic memory surface is plain files.

## Pilot methods (how to apply this to your flow)

**24 ranked methods** in `output/(C) 2026-07-03-agent-memory-architecture-pilot-methods.md` — five angles: **(A) hireui Goal #2** (design the memory layer for hireui's first LLM feature — candidate-profile semantic store + interaction episodic log + a Haiku consolidation gate, composing with the [[../mosh-ai-powered-apps/_index|Mosh vendor seam]]), **(B) files-first discipline** (adopt the Anthropic file-based pattern before reaching for a vector DB), **(C) your own memory system** (name and tune the consolidation gate you already run), **(D) the vaults** (the wiki IS semantic memory; loop-logs ARE episodic), **(E) Scrum coaching** (the taxonomy as a design-review vocabulary).

## Cross-topic links

- **Sister topic (tool-level memory):** [[../claude-code-memory-systems/_index]] — the 6-level taxonomy of how YOUR Claude Code remembers; this topic is the builder-level view (how to design memory INTO a product). The two share the Karpathy LLM-Wiki and consolidation threads.
- **The book chapter this operationalizes:** [[../ai-engineering/_index]] (Ch.6 agents + memory) — Huyen's assembly diagram; this topic is the memory-subsystem detail.
- **The app that would host it:** [[../mosh-ai-powered-apps/_index]] — the vendor-seam chatbot architecture hireui's first LLM feature will use; memory is the layer the course never builds.
- **Cost discipline:** [[../claude-api-cost-optimization/_index]] — selective retrieval, caching, and compaction are the same context-budget economics.
- **Skills as procedural memory:** [[../google-antigravity-skills/_index]] + [[../claude-skills/_index]] — the SKILL.md standard the video correctly identifies as the procedural pillar.
- **Context-rot evidence:** [[../claude-code-observability/_index]] + [[../graphify-codebase-graph/_index]] — the token-efficiency thread.
- **Voice/agent features that need this memory:** [[../multi-agent-orchestration/_index]] (job-screener) + [[../jsm-practical-vibe-coding/_index]] (D2 voice-screening agent).

## Key Takeaways

- **The taxonomy is real and canonical.** Working/episodic/semantic/procedural for agents comes from CoALA (Sumers/Yao/Narasimhan/Griffiths, arXiv:2309.02427), which explicitly borrows Tulving's 1972 psychology. The video re-derives it accurately without citing anyone.
- **The consolidation gate is real — but the trigger is never "N conversations" in production.** Generative Agents used an importance-score threshold (≥150); claude.ai uses a 24-hour timer; ChatGPT's Dreaming V3 runs continuous async synthesis; Letta's sleep-time agents are configurable-frequency. Count-based gates are a teaching simplification.
- **The substrate claim is the video's one big error.** Anthropic memory = files (memory tool, Managed Agents mounts, MEMORY.md). ChatGPT memory = injected summaries ("yet another system prompt hack" — Willison). Vector-store + top-k RAG is ONE builder pattern (Letta archival, custom apps), not "how ChatGPT and Claude work."
- **Both vendors converged on "dreaming."** OpenAI shipped "Dreaming V3" (2026-06-04, vendor-reported 9.4%→75.1% time-sensitive accuracy) and Anthropic announced **Dreaming for Managed Agents at Code with Claude SF 2026-05-06** (research preview; explicit API, 1–100 sessions per dream, non-destructive input→output stores, reviewable diff; Harvey vendor-reported ~6x). Background consolidation by a separate process is now the production norm — the video's core intuition is right. Full mechanics: [[anthropic-memory-stores-and-dreaming]].
- **Letta partially inverts the "cheaper summarizer" economics:** its docs recommend the FAST model on the latency-critical hot path and the STRONGER model on the background memory path (no latency constraint). Cheaper-model consolidation is common practice, but it's a cost choice, not a law.
- **Context windows (2026 ground truth):** frontier Claude (Fable 5, Opus 4.6–4.8, Sonnet 4.6/5) and Gemini are 1M-class; Haiku 4.5 is 200K; the broader ecosystem is 128K–256K — and usable context is far below advertised (Chroma context-rot: safe budgets 150K–400K even on 1M models). "Most LLMs are roughly 1M" overstates; "don't overload the window" is strongly evidence-backed.
