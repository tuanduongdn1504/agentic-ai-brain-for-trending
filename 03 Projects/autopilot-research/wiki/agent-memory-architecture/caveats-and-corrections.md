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

## 2026-07-04 deepening pass — Dreaming workshop claims, graded

Source pair: BizMate VN dub b1qgIGwBUEI → Anthropic EN original geUv4CjPpxI ("Agents that remember", Kevin Chen). Verified via `wf_c3719baa-7f2` + main-loop docs/repo/blog fetches ([[source-provenance]]).

| # | Claim | Verdict | Detail |
|---|---|---|---|
| D1 | Dream models = "Opus 4.7 or Sonnet 4.6" | ✅ CONFIRMED for its date | Opus 4.7 released 2026-04-16, Sonnet 4.6 2026-02-17; **Opus 4.8 released 2026-05-28 — after the video** — docs now list all three. VN dub disambiguated the EN caption garble ("Opus 47/Sonnet 46") |
| D2 | ~95% cache hit rate expected on dream sessions | ⚠️ WORKSHOP-SPOKEN ONLY | In the transcript (main-loop ground truth); in **zero** written sources — docs, official blogs, press all silent. Don't quote as documented spec |
| D3 | Batch-style ~50% discount for scheduled dreams | ⚠️ EXPLORATORY | Speaker said "exploring"; Batch API 50% is real+documented; **no dreaming discount shipped** as of 2026-07-04. Billing = standard token rates |
| D4 | Orchestrator + 1 sub-agent per transcript, "exhaustive by design" | ⚠️ WORKSHOP-SPOKEN | Demonstrated on camera (dream session observable); not doc-specified — implementation may change without notice |
| D5 | Non-destructive input→output store; partial output persists on failure; mid-run deletion errors | ✅ CONFIRMED | Verbatim in dreams docs |
| D6 | Duration "couple minutes to hours" | ⚠️ CONFLICTS with docs | Docs: "minutes to **tens of minutes**". Surfaced per Rule 7; docs presumed current |
| D7 | Index-file generation by dreams | ⚠️ DEMO-OBSERVED, NOT GUARANTEED | On camera in the workshop; absent from docs as a contract. A verifier's REFUTED verdict over-reached (treated transcript-inaccessibility as nonexistence) — overridden by main-loop transcript ground truth |
| D8 | Harvey ~6x task completion | ⚠️ VENDOR-REPORTED | Verbatim in Anthropic's own blog (new-in-claude-managed-agents, 2026-05-06): "Completion rates went up ~6x in their tests." No independent audit. Same tier as OpenAI's Dreaming-V3 metrics |
| D9 | "Dreaming is scheduled/automatic" (press + even Anthropic's recap wording) | ⚠️ CONFLICT — docs win | Documented API is explicit-invocation only (create+poll, no scheduler endpoint); CMA has separate cron scheduled-deployments for sessions. Read "scheduled" as usage pattern |
| D10 | VN dub fidelity | ✅ HIGH | No dub-added claims found. Garbles: "Ciberry memory"→"CWC memory", "session.mb"→"sessions.md", stray "Anthropic Sonnet of GPT" caption artifact, "code với code"→"Code with Claude" |
| D11 | BizMate dub authorization | ⚠️ ATTRIBUTED, AUTHORIZATION UNVERIFIED | Description links the original + states free-localization mission (Skool community: 648 members, free). No public licensing evidence either way |

### 2026-07-04 (later same day) — recording-venue hedge RESOLVED

- The provenance chain's "venue unconfirmed; London most consistent" hedge for geUv4CjPpxI is now **CONFIRMED London**: during the [[../elicit-verifiable-agent-dsl/_index|elicit-verifiable-agent-dsl]] pass (same London Extended event), two independent verifiers fetched `claude.com/code-with-claude/session/ldn-ext-agents-that-remember` (Kevin Chen, 12:00–12:45, 2026-05-20) and `claude.com/code-with-claude/san-francisco-extended` (SF-Ext 2026-05-07 instance taught by **Tina Vachovsky** — the repo seed data's "with Tina" now has a full name). Upload 2026-05-23 = London +3 days. The hedging discipline worked: nothing to retract, only to upgrade. Note: those verifiers framed this as a "critical correction to the wiki" — over-read; the wiki had hedged correctly, only coarse commit-message shorthand said "CWC-SF".

### Excluded dive claim (Rule 12 — fail loud)

- A dive agent asserted an official Anthropic certification **"Claude Certified Architect (CCA-F)"** ($99, 60-question proctored, "launched 2026-03-12") on anthropic.skilljar.com. This **collides with the corpus pin** from [[../multi-agent-orchestration/_index]] (CCA-F = ExamPro **third-party** construct; don't re-fabricate). Main-loop fetch of anthropic.skilljar.com (2026-07-04): official Anthropic Academy, 20+ courses, **no named certification program on the page** (only course "completion certificates"). Claim EXCLUDED from the wiki; logged as a corpus-pin-catches-agent-confabulation instance.

## 2026-07-13 deepening pass 3 — sequel video claims, graded

Source: `GrNbuWWJYiI`, direct video sequel (see [[harness-loop-llmops-sequel]], [[langfuse-and-harness-tools]]).

| # | Claim | Verdict | Detail |
|---|---|---|---|
| S1 | "Harness" = memory+loop control tools for an LLM | ⚠️ VARIANT DEFINITION | Real and internally consistent, but a different scope than this corpus's `harness-engineering` topic (codebase/org restructuring) — see [[../harness-engineering/terminology]] Variant definitions note |
| S2 | LangGraph/LangChain/Pydantic as harness tools | ✅ CONFIRMED (with correction) | All three real and current; "Pydantic" almost certainly means PydanticAI. A researched-not-video-stated "LangGraph GA Oct 2025" date is fabricated — see [[langfuse-and-harness-tools]] |
| S3 | Loop engineering + "end loop guardrails" | ✅ CONFIRMED, not new mechanism | Standard agentic tool-calling loop + stopping condition, already covered generically in [[../autonomous-loops-human-in-the-loop/overview]] |
| S4 | Claude Code permission-prompt notification hook | ✅ CONFIRMED | Matches existing [[../claude-code-hooks/core-patterns]] hook mechanics; auto-captions garble "Claude Code" as "Clockwork"/"clock code"/"cloud code" throughout — same tool, not new ones |
| S5 | LangFuse + LangSmith as tracing tools | ✅ CONFIRMED | LangSmith already deep in [[../agent-development-lifecycle/langchain-interrupt-26-anchor]]; Langfuse newly dived — see [[langfuse-and-harness-tools]] (incl. new fact: ClickHouse acquired Langfuse Jan 2026) |
| S6 | LLM-as-judge for eval | ✅ CONFIRMED, not new | Already covered in depth in [[../prompt-evaluation/llm-as-judge-methodology]] |
| S7 | Consolidation "every 2,000 conversations" | ⚠️ REPEAT of claim #6 above | Not a new claim — same count-based teaching simplification already flagged; real triggers remain importance-sum/24h-timer/continuous-async/explicit |
| S8 | AutoManus.io named as example CRM | ✅ CONFIRMED, not new | Already verified in the "Creator ground-check" section above (real product, Character Capital pre-seed, "4 pilots/2 contracts" self-reported-only) |

**Note on S1/S2:** the two corrections in [[langfuse-and-harness-tools]] (wrong Langfuse investor name; fabricated LangGraph GA date) were errors introduced by this pass's own dive agents, not claims made by the video — the video only named the tools, nothing more specific. Logged in [[source-provenance]], not counted against the video's scorecard.

## Cross-check flags into the corpus

- The mosh-topic pin "never tiktoken for Claude — use `count_tokens`" applies to any memory-budget code this topic inspires.
- The jsm-practical-vibe-coding pin stands: committed Claude auto-memory (`project_clerk_api.md`) is a live production sighting of surface #4 in [[how-claude-memory-works]].
