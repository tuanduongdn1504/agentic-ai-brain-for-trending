# (C) Open Questions — ai-agents-for-beginners

> Placeholder. Append findings as wiki build progresses.

## Questions surfaced Phase 0

1. **Fork vs upstream divergence** — cvtot fork có custom content/VN additions vs microsoft upstream không? (check git log)
   - ✅ **RESOLVED 2026-04-18 (retry session):** Via GitHub API probe.
     - Fork (`cvtot`): pushed `2026-01-12`, 0 stars, 0 forks, size 3.4 GB, fork=true
     - Upstream (`microsoft`): pushed `2026-04-12`, **56,913 stars**, 19,718 forks, size 3.7 GB, fork=false
     - **Divergence:** Fork is **3 months stale**. cvtot has not synced since January 2026. Upstream added ~300 MB of content (likely lesson 14 MAF + refinements).
     - **Pure personal fork** (0 stars, 0 forks) — not a maintenance fork, not a translation fork. cvtot forked for personal learning.
     - **Implication:** Wiki content reflects ~January 2026 snapshot. For latest (including any post-Jan additions), cross-reference `microsoft/ai-agents-for-beginners` directly.
     - **Clone failure explained:** 3.4 GB repo + network instability = RPC connection reset during pack transfer. Not a git config issue.
     - **Description confirmed:** "12 Lessons to Get Started Building AI Agents" (README expanded this to 14 in the fork).
2. **Coming Soon timing** — lessons 15-18 (CUA/Scalable/Local/Securing) release date? (affects wiki freshness)
3. **Tool Use (lesson 4) vs Agentic RAG (lesson 5)** — overlap với Tier 1 siblings' tool-use patterns?
4. **Lesson 10 "AI Agents in Production"** — bridge to Tier 2 (goclaw) territory? Worth highlighting?
5. **Semantic Kernel vs MAF migration path** — does MAF replace SK, or coexist? (lesson 14 MAF is merger of SK+AutoGen, SK still maintained)
6. **Azure-first bias** — course is Azure-centric; applicability to OSS/non-Microsoft stacks?
7. **Sample code quality** — Jupyter notebooks production-ready or teaching-only?
8. **Metacognition (lesson 9)** — unique concept in course, absent from Tier 1 siblings. Worth entity page?

## Meta-questions from 6-wiki corpus

9. **Tier 3 stability** — will other educational resources emerge (LangChain Academy? DeepLearning.AI courses?) making Tier 3 a genuine multi-entrant tier?
10. **Education → Tool pipeline** — is there a natural progression: ai-agents-for-beginners → Tier 1 tool adoption → Tier 2 deployment? Worth codifying?
11. **Framework-agnostic learning** — course teaches concepts; Tier 1 teaches specific tool. Can learners map 1:1? (e.g., Lesson 08 multi-agent → gstack specialists?)
