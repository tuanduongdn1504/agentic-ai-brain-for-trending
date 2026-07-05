# Source Provenance

## How this topic was built (2026-07-05, operator-submitted)

1. **Video**: `yt-dlp` metadata + Vietnamese auto-subs for `7gIwR5SwM_0`; VTT deduped to ~35.4K chars; **read in full in the main loop** (no summarizer between source and librarian).
2. **Original resource (double deep-dive target)**: `thangnch/MiAI_CV_Matching_AI_Agent` — created 2026-07-03, 2 stars at fetch, no license. All 8 files fetched from raw.githubusercontent and **read in full in the main loop** (~36KB). Repo = ground truth over captions wherever they conflict.
3. **Workflow `wf_dd724957-cac`**: 9 dive agents (author-channel / prior-videos / langchain-api / crawlability / code-audit / matching-architecture / claude-stack / cost-economics / regulatory-corpus) + 8 refute-first verifiers = **17 agents, ~965K tokens, 255 tool calls**. Verify stance: every load-bearing claim wrong-until-independently-re-derived; discard-as-garble guard (one search before discarding date-sensitive claims) included verbatim in verifier prompts.
4. **Agent death + main-loop takeover**: dive `claude-stack` died on "Prompt is too long" (it invoked the full claude-api skill). Gap closed in the main loop: claude-api skill reference (cached 2026-06-24 tables) + live fetch of platform.claude.com embeddings docs (Voyage recommendation, model tables) → [[claude-stack-port]].
5. **Verify outcomes**: headline code findings 5/5 CONFIRMED; crawl claim REFUTED; cost dive PARTIAL ×2 (arithmetic corrected); langchain dive PARTIAL ×4 (doc-precision corrections); regulatory CONFIRMED ×3 / PARTIAL ×2; author identity CONFIRMED via GitHub API + miai.vn + nguyenchienthang.vn.
6. **Raw bundle**: `raw/2026-07-05-miai-cv-matching-agent.md` (transcript + all 8 files + metadata).

## Ground-truth hierarchy used

repo code > official docs (LangChain/OpenAI/Anthropic/Voyage, fetched) > live probes (robots.txt, job-board 403s, GitHub API) > video transcript > dive-agent assertions (never trusted unverified).

## Corpus cross-links

- [[external|Storm Bear: multi-agent-orchestration]] — job-screener worked example (architecture-level sibling; zero regulatory coverage, verified — this topic supplies it).
- [[external|Storm Bear: mosh-ai-powered-apps]] — A2 vendor-seam thread this topic's pilot composes with.
- [[external|Storm Bear: ai-engineering]] — the eval-first demo→production discipline the upgrade path follows.
- [[external|Storm Bear: hoidanit-fullstack-vibe-coding]] — prior VN first-party channel; Mì AI is the second, at senior-practitioner level.
- [[external|Storm Bear: claude-api-cost-optimization]], [[external|Storm Bear: prompt-evaluation]] — cost and eval harness threads.

## Key Takeaways

- First-party source + tiny public repo = the cheapest possible full-provenance treatment: everything load-bearing was re-derivable from primary artifacts.
- The refute-first pass earned its cost: 1 refuted claim, 2 arithmetic corrections, 4 doc-precision corrections, 1 stale-verifier catch.
- Pattern repeated from prior ships: agent dies → main loop closes the gap with primary sources rather than shipping a hole.
