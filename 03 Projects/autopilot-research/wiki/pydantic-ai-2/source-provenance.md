# Source provenance

## Primary source

- **Video:** [Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities](https://www.youtube.com/watch?v=PY7xIxybYNc) (`PY7xIxybYNc`), Cole Medin (@ColeMedin), 2026-07-10, 15:00, ~19.6K views / 578 likes / 216K subs at ingest.
- Ingest path: **5, yt-dlp-only** — EN auto-generated captions (`--write-auto-sub`), stripped of VTT markup and rolling-caption duplication via `grep`/`sed`/`awk` (the project's established fallback after `python3 -c` inline scripts were denied by this session's permission settings — see the loop log for the workaround). ~2.6K-word transcript, read in full in the main loop. No NotebookLM used.
- Video description links (extracted from `yt-dlp --write-info-json`, ground truth — not read off garbled captions): sponsor `nimbalyst.com`, `dynamous.ai/ai-native-engineering-org`, demo repo `github.com/coleam00/orbit-support-agent`, launch article `pydantic.dev/articles/pydantic-ai-v2`, official repo `github.com/pydantic/pydantic-ai`.

## Verification workflow

`wf_01eb5573-0b3` — 18 agents (7 dives + 10 refute-first verifiers + 1 completeness critic), ~737K subagent tokens, 171 tool calls, 0 errors, 0 empty results. All agents ran on the session's default model (no override).

**Dives (7):** launch article · official repo/changelog · demo repo (`orbit-support-agent`) · Nimbalyst sponsor claims · Monty sandbox · Agent-Skills/agentskills.io lineage · Pydantic AI 1.0 composability + LangChain/CrewAI comparison.

**Verifies (10):** one refute-first pass per claim, each independently re-fetching primary sources rather than trusting the dive summaries (see [[claims-scorecard]] for the full ledger).

**Critic:** flagged one real contradiction (Monty shipping status — see below) and one minor concern that turned out to be unfounded (whether Cole himself made the Agent-Skills vendor comparison, or a verifier added it — confirmed from the full transcript that Cole says it on-screen).

## Main-loop follow-up

One additional check beyond the workflow: WebFetch of `pydantic.dev/docs/ai/harness/code-mode/` and `github.com/pydantic/pydantic-ai-harness` to resolve the critic-flagged Monty contradiction. Resolution: Monty/code-mode ships in the separate `pydantic-ai-harness` package (v0.6.0, 2026-07-09), not core `pydantic-ai` — Monty's own README is just stale relative to that release. Full writeup in [[lean-core-vs-harness-and-monty]].

## Known gaps

- `dynamous.ai/ai-native-engineering-org` returned HTTP 404 to one dive agent at fetch time. Not treated as a red flag on Cole Medin's identity/Dynamous affiliation — that fact is already independently verified in this wiki at [[../harness-engineering/archon-harness-builder-anchor]] (2026-04-11 fetch) and the [[../harness-engineering/_index|harness-engineering authoritative anchor]] (2026-05-21 fetch), both predating this pass. Likely a page rename/removal or a transient fetch issue, not evidence against the underlying fact.
- Cole Medin's exact current subscriber count (216K, from this video's metadata) was not independently re-audited by the dive agents beyond confirming the channel is active — treated as ground truth per the yt-dlp metadata pulled directly at ingest time.
