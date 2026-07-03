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

## Fabrication-stripping note

No dive fabricated sources outright this run; the failure surface shifted to (a) stale third-party comparison blogs entering as "fetched-primary" and (b) the critic over-flagging real things. The countermeasure that worked: **main-loop primary-source fetches on the highest-risk claims before synthesis**, plus the misfire-class warnings embedded in every verifier prompt.
