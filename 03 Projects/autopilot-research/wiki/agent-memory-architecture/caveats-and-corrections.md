# Caveats and corrections (Rule 12 — fail loud)

## Video claims, graded

| # | Claim | Verdict | Detail |
|---|---|---|---|
| 1 | Four-part memory taxonomy | ✅ CONFIRMED | CoALA/Tulving lineage — [[coala-deep-dive]] |
| 2 | "Session is ephemeral — we're literally just making an LLM call" | ⚠️ PARTIAL | True for raw stateless APIs (Anthropic Messages API default). NOT universal: OpenAI's Responses/Conversations APIs persist state server-side via `previous_response_id`/conversation objects (corpus-known from [[../mosh-ai-powered-apps/_index]] — and note chaining bills all prior input tokens); consumer apps keep server-side history |
| 3 | Procedural memory saved as SKILL.md files | ✅ CONFIRMED, incomplete | Agent Skills spec real (launched 2025-10-16, open standard 2025-12-18 at agentskills.io; ~40 products incl. Google Antigravity). Two omissions: CoALA counts LLM *weights* as procedural memory; the Agentic AI Foundation's founding projects were MCP + goose + AGENTS.md (Dec 9, 2025) — Agent Skills was published as a *separate* open standard (a dive claim of "donated alongside" was REFUTED by a verifier) |
| 4 | Semantic + episodic memory live in vector stores; RAG top-k retrieval | ❌ REFUTED as universal | ChatGPT = summary injection; all 4 Anthropic surfaces = files/summaries; valid pattern for custom apps + Letta archival — [[rag-vector-stores-and-context-limits]] |
| 5 | "This is how ChatGPT and Claude memory works" | ⚠️ HALF-TRUE | Consolidation-into-durable-facts: yes, both. Mechanism (vector RAG) and trigger (N chats): no for both |
| 6 | Consolidation gate after N conversations | ⚠️ CONCEPT CONFIRMED, PARAMETER FICTIONAL | No verified count-based production gate — [[consolidation-gate-design]] |
| 7 | Cheaper summarizer agent | ❓ UNVERIFIABLE as production fact | OpenAI undisclosed; Letta recommends *stronger* on the background path; RecMem supports cheaper. Sound design option, not established fact |
| 8 | "Context window for most LLMs ≈ 1M tokens" | ⚠️ OVERSTATED | Frontier Claude/Gemini = 1M (Claude ground truth: Fable 5/Opus 4.6–4.8/Sonnet 4.6/5 = 1M, Haiku 4.5 = 200K); ecosystem median 128K–256K; usable ≪ advertised (Chroma 150–400K safe budgets) |
| 9 | Overloading context → slower, less accurate | ✅ CONFIRMED, under-cited | Liu 2307.03172 / Chroma context rot / NoLiMa — [[rag-vector-stores-and-context-limits]] |
| 10 | "AI turns every word into numbers, then similarity search" | ⚠️ LAY-OK | Conflates tokenization with embeddings |

## Creator ground-check (dimension `sean-identity`, 18/18 verified)

- **Sean Chen** (GitHub [ShenSeanChen](https://github.com/ShenSeanChen), acct created 2017-10-27, 353 followers, 91 public repos). Bio: "Founder AutoManus.io | prev @MIT @Google". LinkedIn: MIT 2019–20 (business analytics / DS & operations research; MIT DesignX finalist; course repos 15.095, 6.435 as corroborating signals — coursework evidence, not degree verification). Google Data-Scientist stint: bio + channel-description sourced — **self-reported tier** (one verifier found LinkedIn showing CVS data-science work; conflict noted, not averaged).
- **AutoManus.io** — real product ("Your Business's Digital Brain For Complex Solution Sales"; pricing Starter $29/mo, Pro $249/mo); **Character Capital portfolio confirmed** (pre-seed fund). The description's "live with 4 pilots and 2 contracts" — **self-reported only**, not on the public site.
- **Repos renamed `yt-*` → `launch-*`** — the video description's `github.com/ShenSeanChen/yt-rag` etc. still resolve via GitHub redirects (main-loop `gh api` check: `yt-rag` → `launch-rag`, 57★). **No dedicated repo for this video** (newest repo before upload: kimi-code, 2026-06-13). Related prior work: `launch-rag` (his RAG video), `launch-agent-skills` (2026-01-28, MIT, 12★ — his skills/teams video).

## Reported-only / unverified flags

- **ChatGPT "Dreaming V3" metrics** (9.4→75.1% etc.) — vendor-reported, relayed by press; no independent audit. The name and 2026-06-04 date are multiply confirmed; one dive initially misdated it "June 2025" (caught by a verifier, REFUTED).
- **Claude Code "AutoDream"** (24h+5-session trigger, 4 phases) — **single third-party source** (zenvanriel.com); absent from official Claude Code docs fetched 2026-07-03. Same rumor-tier as the prior "Kairos daemon" flag in [[../claude-code-memory-systems/_index]]. Do not cite as fact.
- **"Production consolidation every 50–200 episodes"** — secondary/tertiary sources only; UNVERIFIABLE from primary docs.
- **HippoRAG / A-Mem / RecMem attributions** — papers exist in the space, but the workflow critic's author attributions were garbled ("Chen et al." for HippoRAG, "Gur et al." for A-Mem — fetch before citing authors). RecMem (arXiv:2605.16045) and "Anatomy of Agentic Memory" (arXiv:2602.19320) were verifier-fetched and safe to cite by title.
- **The video's whiteboard-simplification pattern**: presents design guidance ("20 conversations", "cheaper model") in the same voice as facts — fine as pedagogy, needs this table before entering any design doc.

## Cross-check flags into the corpus

- The mosh-topic pin "never tiktoken for Claude — use `count_tokens`" applies to any memory-budget code this topic inspires.
- The jsm-practical-vibe-coding pin stands: committed Claude auto-memory (`project_clerk_api.md`) is a live production sighting of surface #4 in [[how-claude-memory-works]].
