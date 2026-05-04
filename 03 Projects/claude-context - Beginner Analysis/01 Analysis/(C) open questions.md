# (C) Open Questions — claude-context v40

Questions surfaced during wiki build; parked for future investigation or explicit non-answers.

## Product / Architecture

1. **Why MIT (permissive) rather than Apache-2.0 like Milvus parent?** Commercial positioning choice; possibly to maximize downstream AI-tool adoption versus Milvus's big-enterprise use.
2. **Merkle-tree for incremental indexing** — any prior art cited? (None visible in README/CONTRIBUTING. Corpus-first architectural detail.)
3. **Chunk size 1000 / overlap 200** — what empirical tuning produced these numbers? Any benchmark?
4. **Why default to OpenAI `text-embedding-3-small` vs VoyageAI `voyage-code-3` (specialized for code)?** Commercial accessibility vs quality tradeoff.
5. **Chrome Extension "Coming Soon"** — timeline? What does GitHub-browser-plane code search unlock that MCP doesn't?
6. **Python bridge (`python/`)** — temporary testing scaffold or intended production surface?
7. **Why expose 4 separate MCP tools (`index_codebase` / `search_code` / `clear_index` / `get_indexing_status`) instead of 1-2?** Indexing lifecycle granularity.

## Ecosystem / Business model

8. **Zilliz Cloud free Serverless tier** — what usage limits trigger paid upgrade? Cost curve?
9. **What % of claude-context adoption flows into Zilliz Cloud paid tier?** (Unmeasurable externally; commercial funnel design observable.)
10. **Relationship with Milvus community** — claude-context as "loss leader for Milvus" or genuinely separate product team?
11. **memsearch sibling** — coordinated roadmap with claude-context? Competitive? Complementary?
12. **deep-searcher** (7.8K) — related to claude-context but Python + research-focused. Product portfolio strategy unclear.

## Pattern Library

13. **Will Pattern #50 reach N=4 before next full audit?** (N=3 at v40 Zilliz; candidate streak continues with aggregator-genre Pattern #68 correlate.)
14. **Vector-search vs graph-based code-indexing T4 sub-taxonomy** — at what N does this become formal meta-pattern vs observational? Currently 2 graph + 1 vector = N=3 total but 2-axis. Needs 2nd vector for formal.
15. **Pattern #22 T4 AGENTS.md abstention** — 4 of 7 T4 with data lack AGENTS.md. At what N becomes "T4-absence-is-norm" formal refinement?
16. **Merkle-tree incremental-indexing** — if 2nd wiki observes similar mechanism, does it become Pattern candidate?
17. **SWE-bench Verified** — claude-context is 2nd corpus use after OpenHands v30. SWE-bench Verified as emerging empirical-standard?

## Storm Bear vault applicability

18. **Can claude-context index the Storm Bear vault directly?** (markdown is 1 of 14 supported languages; should work but semantic-quality on prose unknown.)
19. **Semantic search quality on VN-language content?** (Embedding models multilingual but VN may be Tier-2; needs empirical test.)
20. **graphify v16 vs claude-context v40 for vault** — graph-based (entity relationships) vs vector-based (semantic similarity). Which better fits Storm Bear wiki-navigation use case?
21. **Free tier Zilliz Cloud usage for vault-indexing** — sufficient for 100K+ lines markdown? Need to check Serverless limits.
22. **Cost projection:** OpenAI embedding cost for ~40 wikis × average ~600 lines each = ~$0.X per full re-index.

## Meta / Routine

23. **3rd v2.1-era GREEN primitive-count** — GREEN-track-3 (bizos + DeepTutor + dive-into-llms + claude-context) confirms GREEN remains default. YELLOW (pi-mono v36) still N=1.
24. **29th consecutive Storm Bear meta-entity** — any wiki where meta-entity NOT applicable since v10?
25. **4th consecutive zero-registration wiki** — consolidation-forward discipline durability signal.
