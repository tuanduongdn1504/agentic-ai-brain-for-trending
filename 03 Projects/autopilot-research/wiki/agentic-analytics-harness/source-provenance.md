# Source provenance & verification

> **Why this article exists:** the primary video is **uncaptioned**, so this topic was built by **triangulation**, not transcription. Per autopilot constitutional rule #4 (NEVER fabricate) and Storm Bear Rule 12 (fail loud), every claim is tiered here so a reader knows exactly what's first-party-confirmed vs. talk-recap. Mirrors the discipline of [[claude-api-cost-optimization/source-provenance]] and [[prompt-evaluation/source-provenance]].

## The caption gap (load-bearing caveat)

- The video [K4-flzsPraE](https://www.youtube.com/watch?v=K4-flzsPraE) has **no captions and no subtitles.** Confirmed **twice**: with stale `yt-dlp 2026.03.17` *and* after upgrading to `yt-dlp 2026.06.09` (`brew upgrade yt-dlp`). Both report "has no automatic captions / has no subtitles." Forcing `web`/`mweb` clients didn't expose any caption track.
- **No local transcription** available in this worktree (`whisper`, `whisper-cpp`, `mlx_whisper`, `ffmpeg` all absent; no `.venv`/NotebookLM).
- **Consequence:** there is **no verbatim transcript.** Direct quotes in this topic come from the *written* sources below (Omni blogs, Anthropic's video description), **not** from the spoken talk.

## Source tiers

| ID | Source | Tier | What it backs |
|---|---|---|---|
| S1 | Video description (Anthropic) | **T1 first-party** | 99% code in Claude Code; "multi-agent system, design & size tools, evaluate effectiveness"; Chris Merrick = CTO |
| S2 | omni.co/blog/building-omnis-architecture-for-agentic-analytics | **T1 first-party (Omni)** | coordinator + summarization sub-agent; 4 core tools; SQL + Arrow→CSV; semantic layer; validation/guardrails; conversation-memory rebuild; prompt caching; run-as-current-user; the 5 lessons |
| S3 | omni.co/blog/improving-ai-quality-with-context | **T1 first-party (Omni)** | metadata fields; 3 injection levels; ~200k/175k char budget; feedback loop; dbt seeding |
| S4 | claude.com/code-with-claude/london-extended | **T1 first-party** | session title, speaker, slot (11:30 AM Founder stage, 2026-05-20) |
| S5 | ai-heartland.com/agent/omni-agentic-analytics-harness/ | **T2 third-party recap of THIS talk** | 45 tools; 50-iteration outer loop; "Blobotomy" naming + ~5 count; Blobotomy 1/2 stories; Haiku→Sonnet date; token figures; 8 eval criteria; error-recovery-ROI; ~30 engineers; 18 months; SQL 3–4→1 |
| S6 | WebSearch snippets | T2 corroboration | **103.3B tokens/month** independently restated |

## What is first-party-confirmed (high confidence)

- 99% of platform code written with Claude Code [S1].
- Coordinator + one summarization sub-agent (its own context window); adapt/retry/stop [S2].
- 4 core tools; SQL generation; Arrow results → CSV transform [S2].
- Semantic layer stores business context (not a global prompt); `ai_context`/`sample_values`/`synonyms`/`descriptions`; model/topic/field injection levels; ~200k total / ~175k semantic char budget; feedback via AI-usage dashboard; dbt seeding [S2, S3].
- Strict input/output validation, malformed-state detectors, integration tests, "don't re-query unless filters changed" [S2].
- Conversation memory rebuilt each turn via a translator [S2]; prompt caching relied on [S2]; agent runs only as the current user [S2].
- The five production lessons (demo≠prod, AI-optimism-is-risk, foundations-first, security, trust-over-cleverness) [S2].

## What is single-source talk-recap (flag before reuse)

These come **only** from S5 (plus S6 for the token figure). Plausible and internally consistent with T1, but **not independently first-party-verified**:

- **45 tools** (vs first-party "4 core") — see reconciliation in [[agentic-analytics-harness/tool-design-and-sizing]].
- **50-iteration** outer-loop cap; checkpoint recovery.
- **"Blobotomy"** as the internal name; **~5** cycles; the specific Blobotomy 1 (split-brain) and Blobotomy 2 (SQL) narratives.
- **Haiku → Sonnet** migration dated **Aug 2025.**
- **Token growth 1.2B → 103.3B/month** (103.3B cross-confirmed by S6; the 1.2B and dates are single-source).
- **8 eval criteria** for benchmark-question construction.
- **Error-recovery = highest-ROI** claim; **3–4 → 1 attempt** after the SQL switch; **~30 engineers**; **18 months.**

## The one reconciliation (Rule 7 — surfaced, not blended)

**"4 core tools" (S2) vs "45 tools" (S5)** is **not a contradiction**: different granularity at different times. S2's blog (~Aug 2025) names the load-bearing tool *categories*; S5's talk (May 2026) reports the matured portfolio count. Documented in both [[agentic-analytics-harness/tool-design-and-sizing]] and [[agentic-analytics-harness/overview]].

## Open verification items

- **Verbatim transcript** — unobtainable until captions are published or a whisper pass is run (needs `ffmpeg` + a whisper install; out of scope for this worktree).
- **First-party confirmation of T2 numbers** — would need an Omni engineering deep-dive post or an Anthropic customer story with the figures. Not found as of 2026-06-20.
- **Optional adversarial-Workflow verification** — the last two ships ([[claude-api-cost-optimization/_index]], [[prompt-evaluation/_index]]) each ran a multi-agent verification Workflow. Available on request for the T2 claims here.

## Key Takeaways

- **Bulk architecture = first-party-solid** (Omni's own blogs); **talk-specific numbers = single-source recap** — cite accordingly.
- **The caption gap is the headline risk** — anyone extending this topic should know there's no transcript behind it.
- When reusing a number from this topic, check this table first: if it's **T2-only**, hedge it.
