# agent-development-lifecycle

> **Anchor:** Harrison Chase (LangChain CEO) + Ankush Gola (LangChain CTO) — LangChain Interrupt 2026 keynote, 2026-05-19 (44:58)
> **First compiled:** 2026-05-20
> **Article count:** 3 (1 index + 2 articles)
> **Status:** N=1 anchor, single source. Topic created because the framework introduced (Agent Development Lifecycle — Build/Test/Deploy/Monitor parallel to SDLC) is a distinct conceptual axis, not a sub-claim of any existing topic.

This topic covers the **Agent Development Lifecycle (ADL)** as proposed by LangChain at Interrupt 2026 — a four-phase model (Build → Test → Deploy → Monitor) explicitly positioned as parallel to but distinct from the Software Development Lifecycle (SDLC). The thesis is that agents differ from software along two axes: (1) infinite input space (natural language + multimodal) and (2) LLM non-determinism + prompt-fragility, requiring more iteration than traditional SDLC accommodates.

The Interrupt 2026 keynote ships the framework alongside **6 product launches** (Deep Agents 0.6, LangSmith Sandboxes GA, LangSmith Context Hub, LangSmith LLM Gateway beta, Managed Deep Agents private preview, SmithDB, LangSmith Engine public beta) — all positioned as components of the ADL toolchain. The anchor article covers the framework + launches; the SmithDB article covers the purpose-built agent-observability database in technical detail.

## Articles

- [[langchain-interrupt-26-anchor]] — the ADL framework (4 phases + governance overlay), all 6 product launches with positioning rationale, key claims and trends, divergences/convergences with prior corpus anchors
- [[smithdb-architecture]] — purpose-built database for agent observability: workload characteristics, architecture (object-storage-backed compute/storage separation, Rust + Apache DataFusion + Vortex), three technical challenges solved (distributed spans / top-K queries / leading-edge ingestion), 6x-15x performance gains, Jeff Dean Amdahl's-law quote

## Cross-links to existing autopilot topics

- [[external|harness-engineering/_index]] — **STRONG SIGNAL**: Harrison Chase explicitly adopts Tejas Kumar's term "agent harness" at `[06:35]` and frames Deep Agents AS a harness. This is corpus-first cross-anchor terminology adoption from a major framework vendor — relevant evidence for [[external|harness-engineering/tejas-kumar-anchor]] promotion criteria.
- [[external|agent-dashboard-os/_index]] — LangSmith Observability is one of the named tools in that topic's stack. SmithDB extends that thread with purpose-built infrastructure underneath.
- [[external|claude-md-12-rules/_index]] — Harrison cites `agents.md` and skills as **open standards** at `[17:01]–[17:11]`, and LangChain partners with Redis/Elastic/Mongo/Pinecone to push open memory standard. This positions agents.md (used by 12-rule template) as ecosystem-load-bearing format, not just a personal-discipline convention.
- [[external|autonomous-loops-human-in-the-loop/_index]] — Harrison's "ship early + iterate quickly" + LangSmith Engine ambient-proactive agent pattern are HITL-flywheel positions worth comparing against Karpathy autoresearch.
- [[external|codex/_index]] — Deep Agents 0.6 launches `deep-agents code` as open-source coding agent example with open-model emphasis (DeepSeek V4 / GLM5 / Nemotron). Adds counter-evidence to the Claude Code / Codex dual-frontier framing.

## Cross-links worth flagging for Storm Bear vault

- **Karpathy LLM Wiki explicitly named** at `[17:23]–[17:29]`: Harrison says Context Hub stores "your LLM wikis, so this thing that Karpathy did where he basically ran an LLM and had it generate wikis, which are condensed knowledge in markdown files. We think that's gonna become a more and more common pattern." First corpus evidence of MAJOR FRAMEWORK VENDOR explicitly adopting Karpathy's LLM Wiki pattern as a product feature. Worth a Pattern Library candidate registration in next mini-audit.

## Sources

- `raw/2026-05-19-langchain-interrupt-26-adl-transcript.md` — verbatim auto-caption transcript with `[MM:SS]` timestamps (905 segments, ~7.7K words; cleaned VTT via `/tmp/clean_vtt2.awk` — used the `en.vtt` manual-style caption file, NOT `en-orig.vtt` per-word, so no inline-tag stripping needed)
- [Source 18] Harrison Chase + Ankush Gola — *The Agent Development Lifecycle: Build, Test, Deploy, Monitor | Interrupt 26* — https://www.youtube.com/watch?v=jWy39wavbjY (44:58, ~1.9K views as of 2026-05-20, uploaded 2026-05-19, channel `@LangChain`)
- Path: 5 (yt-dlp-only single-source, no NotebookLM bundle)

## Status

- Single-source N=1 anchor. Topic created on faith of distinct conceptual axis (ADL ≠ SDLC framework explicit; not redundant with harness/dashboard topics).
- **Promotion / consolidation criteria:** if a 2nd ADL-framework source appears (different speaker or org adopting the 4-phase model), the topic stabilizes. If after ~3 wikis the framework is only observed at LangChain, consider folding into a "framework-vendor methodology" sub-topic rather than its own axis.
- All 6 product launches are claims awaiting independent verification — none of these have been pilot-tested. The anchor article preserves the LangChain claim verbatim with timestamps; verification (does SmithDB really deliver 6-15× perf? does Engine reduce time-to-triage?) is future work.
