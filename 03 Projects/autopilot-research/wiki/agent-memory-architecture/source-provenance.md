# Source provenance — pipeline, verification, misfire log

## Pipeline

1. **Ingest (path 5, yt-dlp)** — `yt-dlp --skip-download --dump-json` + `--write-auto-subs --sub-langs en` for mY3bR9qjZr4; VTT deduped to ~3.6K-word transcript (`raw/2026-07-03-sean-agent-memory-architecture.md`), **read in full by the main loop**. No NotebookLM (single operator-submitted video).
2. **Deep-dive + adversarial verify** — Workflow **`wf_4356f040-686`** (task wa96hzza6): **28 agents** = 10 dimension deep-dives (coala / memgpt-letta / generative-agents / langmem-langchain / chatgpt-memory / claude-memory / skills-procedural / cogsci-lineage / sean-identity / video-claims-audit) + 17 adversarial verifiers (2 lenses on the 7 high-risk dims, 1 on the rest; REFUTE-first prompts carrying the corpus misfire-class warnings) + 1 completeness/confabulation critic. **~1.65M subagent tokens, 555 tool calls, ~7.6 min.** 1 agent died: `verify:coala:L2` (StructuredOutput retry cap) — coala retained single-verifier coverage plus main-loop checks.
3. **Main-loop ground-checks** (pre-empting/overriding verifier drift): direct WebFetch of the Anthropic memory-tool docs (GA, `memory_20250818`), Claude Code memory docs (no AutoDream), Willison's dossier article (exact section names); `gh api` checks of ShenSeanChen repos incl. the `yt-rag`→`launch-rag` redirect; **claude-api skill reference** consulted for authoritative Claude model/context-window facts.

## Source tiers

- **T1**: arXiv pages (2309.02427, 2304.03442, 2310.08560, 2504.13171, 2303.11366, 2307.03172, 2605.16045), Anthropic platform/support/code docs, OpenAI announcement pages, LangChain blog + docs, letta.com + docs.letta.com, agentskills.io, GitHub API.
- **T2 credible**: Simon Willison, Manthan Gupta teardowns (independent, consistent); zenvanriel.com (single-source — flagged).
- **T3**: press relays of Dreaming V3 metrics (TechTimes/opentools/cryptonomist), context-window comparison blogs (two proved stale — see misfires), atlan/apxml explainers (cadence folklore — flagged UNVERIFIABLE).

## Verdict summary

- **CONFIRMED against primary sources**: CoALA taxonomy/venue/authors; Generative Agents mechanisms (α=1 scoring, ≥150 reflection threshold, 21.7K★); MemGPT + sleep-time papers (incl. 2.5×-is-benchmark-specific PARTIAL); Letta 4-component architecture + dual-agent sleep-time + founders/backers/23.6K★; LangMem SDK (2025-02-18) + triad; ChatGPT timeline (2024-04 → 2024-09 → 2025-04 → Dreaming V3 2026-06-04) + summary-injection mechanism + dossier sections; all four Anthropic memory surfaces + Dreams + zero-vector-DB finding; Agent Skills dates (2025-10-16 / 2025-12-18) + ~40 adopters; cog-sci lineage (Tulving/Baddeley/Squire/ACT-R); Sean Chen identity set (18/18); context-degradation evidence (Liu/Chroma/NoLiMa).
- **REFUTED (video)**: vector-store universality; "how ChatGPT and Claude work" as mechanism; ephemeral-session as universal; 1M-for-most-LLMs as stated.
- **UNVERIFIABLE (flagged in wiki)**: cheaper-summarizer in production pipelines; 50–200-episode cadence; Dreaming V3 internals; AutoDream.

## Verifier/critic misfire log (Rule 12 — overridden with ground truth)

1. **Critic declared LangMem SDK "no credible product / confabulation"** → OVERRIDDEN: two verifiers had already fetched the 2025-02-18 LangChain announcement with quotes. Classic stale-cutoff critic misfire (the recurring corpus pattern: Claude Design, Antigravity 2.0, Sandcastle, visionagents.ai…).
2. **Critic declared the ChatGPT dossier section names "fabricated; no Willison source uses these labels"** → OVERRIDDEN by the main loop's own fetch of simonwillison.net returning those exact four names.
3. **Critic flagged Agent Skills dates as "unverified back-projection"** → OVERRIDDEN: verifier had fetched the Anthropic engineering post ("Published Oct 16, 2025") and the Dec-18 open-standard coverage; a related dive claim (skills donated to the Agentic AI Foundation) was correctly REFUTED (founding projects = MCP + goose + AGENTS.md).
4. **"Claude models max out at 200K"** (dive fact via crazyrouter blog; echoed by one verifier) → OVERRIDDEN by Anthropic docs + claude-api reference: current frontier Claude = 1M (Haiku 4.5 = 200K). Stale-third-party-source misfire; conflicting GPT-window numbers (128K vs 1.05M) from the same blog class → neither published.
5. **"No separate 'API memory tool' exists"** (generative-agents verifier, PARTIAL) → OVERRIDDEN: it checked only code.claude.com; platform.claude.com documents `memory_20250818` (GA). Wrong-scope-lookup misfire (same class as the how-we-claude-code local-FS greps).
6. **Dive misdated Dreaming V3 as "June 2025"** → caught and REFUTED by its own verifier (correct: 2026-06-04) — the verify layer working as designed.
7. **One video-claims verifier couldn't find the video/channel** and marked identity UNVERIFIABLE → superseded by the sean-identity dimension's direct fetches (video ID + channel confirmed). Fetch-failure ≠ refutation, correctly handled.
8. **Critic's "missing originals" list contained garbled attributions** (HippoRAG "Chen et al.", A-Mem "Gur et al.", "Gemini 2.0 Advanced native Memories (June 2026)") → names/versions not corroborated; excluded from wiki claims, noted in [[caveats-and-corrections]].

## 2026-07-04 deepening pass (Anthropic Memory Stores + Dreaming)

1. **Ingest (path 5, yt-dlp):** operator-submitted VN dub b1qgIGwBUEI (BizMate AI Official) → description revealed the EN original geUv4CjPpxI (official Claude channel). Both auto-caption tracks deduped and **read in full in the main loop** (~26K + ~37K chars) → `raw/2026-07-04-anthropic-dreaming-memory-stores.md`.
2. **Main-loop primary fetches (before agent fan-out):** platform.claude.com managed-agents `/memory` + `/dreams` **in full**; later `/overview`, claude.com/blog CWC-SF recap, anthropic.skilljar.com, and `gh api` + raw fetches of `anthropics/cwc-workshops` (`agents-that-remember/` README + `bootstrap.sh` in full).
3. **Deep-dive + adversarial verify:** Workflow **`wf_c3719baa-7f2`** — **18 agents** = 7 dives (repo / event / announcement / cma-platform / cc-autodream / bizmate / models) + 10 refute-first verifiers on pre-registered claims (with the discard-as-garble guard verbatim in prompts) + completeness critic; **~989K subagent tokens, 281 tool calls, ~5.3 min**. 3 dives died on structured-output failures (repo, event, cma-platform) — all three closed by main-loop fetches instead.
4. **Source tiers:** T1 = platform docs, claude.com blogs, anthropics/cwc-workshops, anthropic.com model announcements, yt-dlp metadata; T2 = Simon Willison CWC liveblog, SiliconANGLE; T3 = letsdatascience/mindstudio/buildfastwithai explainers (echo-chain risk), claudefa.st/tessl.io AutoDream posts.

### Misfire log (this pass)

1. **BizMate-nonexistence misfire:** dive + critic declared the dub video/channel "404 / possible confabulation" and the critic demanded the dub verdict be "retracted" — the main loop had **already fetched the video's metadata, captions, and description via yt-dlp** (1,467 views, 7,320 subs). US-search-index blindness to a small VN channel ≠ nonexistence. Overridden. (Recurring fetch-failure-≠-refutation class.)
2. **V18 index-file over-reach:** verifier correctly found docs-absence but escalated to "no evidence the feature exists at all" — the feature is on camera in the transcript the verifier couldn't access. Downgraded to demo-observed/not-guaranteed, not refuted.
3. **V1/V2/V6 transcript-blindness:** verifiers marked workshop quotes "unlocatable" — all three quotes are in the main-loop transcript. Closed with ground truth; docs-absence findings retained.
4. **CCA-F re-fabrication echo:** bizmate dive asserted an official "CCA-F" certification — caught by the corpus pin (multi-agent-orchestration: ExamPro third-party) + main-loop skilljar fetch showing no named cert. EXCLUDED. First observed instance of a **memory pin functioning as a confabulation tripwire**.
5. **Announcement-dive scope miss (minor):** declared Harvey absent from "the official blog" — it checked the May-12 recap post; Harvey is in the May-6 `new-in-claude-managed-agents` post (V9 verifier had the exact quote). Rule 7 resolved with both URLs on the table.

## Fabrication-stripping note

No dive fabricated sources outright this run; the failure surface shifted to (a) stale third-party comparison blogs entering as "fetched-primary" and (b) the critic over-flagging real things. The countermeasure that worked: **main-loop primary-source fetches on the highest-risk claims before synthesis**, plus the misfire-class warnings embedded in every verifier prompt.

## 2026-07-13 deepening pass 3 (harness/loop/LLMOps sequel + Langfuse)

1. **Ingest (path 5, yt-dlp):** operator-submitted direct video sequel `GrNbuWWJYiI` (Sean's AI Stories, 2026-06-26, one week after this topic's primary source `mY3bR9qjZr4`) → EN auto-captions only (no manual track), VTT deduped, **read in full in the main loop** (~7K words) → `raw/2026-07-13-sean-agent-harness-loop-llmops.md`.
2. **Main-loop scouting pass (before any agent fan-out) — the key move this pass:** read all 14 existing articles in this topic plus four adjacent topics (`agent-development-lifecycle/langchain-interrupt-26-anchor`, `claude-code-hooks/`, `prompt-evaluation/`, `harness-engineering/terminology`) to establish what was already verified. Result: ~90% of the new video's content (memory taxonomy, Sean-identity/AutoManus/Character-VC, consolidation-gate mechanics, Claude Code hooks, LLM-as-judge, and LangSmith at deep detail) was already on file. This pass was scoped to the narrow remainder rather than re-running a full mega-workflow.
3. **Deep-dive + adversarial verify:** Workflow (5 agents = 2 dives [Langfuse; LangGraph/LangChain/PydanticAI status] + 2 refute-first verifiers + 1 completeness critic); **~195K subagent tokens, 72 tool calls, ~75 min wall-clock** (one verifier ran long — 2 tool calls short of 35 min — but completed cleanly). 0 agent deaths, 0 empty results.
4. **Source tiers:** T1 = langfuse.com (handbook, pricing, docs, blog), GitHub API (langfuse, langgraph, pydantic-ai repos), PyPI (pydantic-ai); T2 = Simon Willison's PydanticAI launch post (independent, consistent with GitHub dates).

### Misfire log (2026-07-13 pass)

1. **Dive-agent investor-list error:** the Langfuse dive drafted "Lightspeed, General Catalyst/La Famiglia" as seed investors — the refute-first verifier checked langfuse.com/handbook directly and found the actual list is **Lightspeed, La Famiglia, and Y Combinator** (no General Catalyst). Corrected in [[langfuse-and-harness-tools]]. This error originated in this pass's own research, not in the video.
2. **Dive-agent fabricated date:** the harness-tools dive drafted "LangGraph reached GA on October 22, 2025" — the verifier checked the GitHub releases API and found zero releases in October 2025 (earliest visible: January 2026). REFUTED; excluded from the wiki. Same stale/hallucinated-date failure class this corpus has caught in prior topics (Rule 12 — verify layer working as designed, not a corpus gap).
3. **Dive-agent overstated feature:** the Langfuse dive implied dataset-version-locked experiments are live — the verifier found Langfuse's own docs say this is "coming soon." Corrected in [[langfuse-and-harness-tools]].
4. **Completeness critic:** found no new independently-checkable claims beyond confirming the video's "every 2,000 conversations" consolidation framing is a repeat of the already-flagged teaching-fiction simplification (see [[consolidation-gate-design]], [[caveats-and-corrections]] claim #6) — not a new or contradicting claim. Also confirmed the "Clockwork"/"clock code"/"cloud code" auto-caption garbles all read as "Claude Code" given context.

## Fabrication-stripping note (2026-07-13 pass)

Unlike the 2026-07-03 and 2026-07-04 passes (which caught mostly *critic* over-flagging of real things), this pass's misfires were the inverse: the **dive agents themselves introduced two wrong specifics** (an investor name, a fabricated date) into their own draft findings, both caught cleanly by the refute-first verify stage before reaching the wiki. This is the adversarial-verify architecture working exactly as designed — no correction required past the verify stage, and nothing reached [[caveats-and-corrections]] as a "video error" because the errors were never the video's; the video only named the tools, not these details.
