# (C) Autopilot Loop — 2026-07-11-17

> **Trigger:** interactive `research <topic>` (operator: "build knowledge from this video + double deep-dive into the original resource + pilot to apply, show me many methods")
> **Topic:** local-ai-coding-agents (NEW)
> **Started:** 2026-07-11T17:30:00+07:00
> **Ended:** 2026-07-11T18:35:00+07:00
> **Duration:** ~65m

## Source

- Video `Zof2Oaj14rk` — Code with Beto (Beto Moedano, @codewithbeto), *"Local AI Coding Agents Are Finally Good Enough"* (2026-07-09, 16:55, ~6.6K views).
- Path 5 (yt-dlp-only). EN manual `en-US` captions → dedupe → ~3.1K-word transcript, read in full in the main loop. No NotebookLM.
- First-party video → double-dive targeted the FIRST-PARTY ORIGINALS beneath each stack layer.

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 (video) + 5 first-party originals dived | 1 (cold topic) | 0 | 1.0 |

`gaps_closed_ratio` = **1.0** (cold-start: topic created + fully populated in one pass; 11 wiki files + pilot menu, no stub/TODO markers left).

## Verification workflow

- `wf_830dc448-b7e` — 17 agents (7 first-party dives + 9 refute-first skeptics on 3 headline claims × 3 lenses + 1 completeness critic). ~804K tokens, 328 tool calls, ~7.5 min.
- **Model: Haiku 4.5** (cheaper tier) → mixed quality; corrections applied in main loop (Rule 12 fail-loud):
  1. qwen dive's *"Opus 4.5 doesn't exist → C4 UNVERIFIABLE"* — **WRONG**, overridden (Opus 4.5 real; SWE-bench 80.9 / Terminal-Bench 59.3, independently anchored; also contradicted by presenter dive's own benchlm.ai find). C4 → CORRECT-BUT-INCOMPLETE.
  2. mlx dive's stale *"v0.32.0 July 2024"* — dropped; MLX speed re-grounded on independent 2026 benchmarks (30-50% vs llama.cpp <14B; converges at 27B).
  3. Over-harsh MISLEADING grades on C2 (1-day drift) + C14 (~20GB rounding) softened.
  4. C6 skeptics' unverified specifics (exact tok/s, GH issue IDs, "25% failure") quarantined — only the direction asserted.
- **2 agents died** ("prompt too long" — C12 latency + tiered-routing skeptics invoked `claude-api` skill → context overflow). Closed by the completed TCO skeptic + main-loop reasoning.
- **Main-loop independent anchors** (per "verify collisions/identity independently" discipline): Qwen3.6 specs/benchmarks; Opus 4.5 benchmarks; Locally-AI acquisition; MLX-vs-llama.cpp.

## Scorecard (14 claims)

6 CONFIRMED · 5 CORRECT-BUT-INCOMPLETE · 3 OVERSIMPLIFIED/SPECULATIVE · **0 FALSE · 0 FABRICATED.** Toolchain real + reproducible; failure mode = enthusiasm-over-claim (C6/C12/C13) + one config error (C8 `modalities`). Honest presenter (anti-jasonlee). Full table: [wiki/local-ai-coding-agents/claims-scorecard.md](../wiki/local-ai-coding-agents/claims-scorecard.md).

## Sources ingested

- raw/2026-07-11-local-ai-coding-agents.md (transcript)

## Wiki articles created (11)

- wiki/local-ai-coding-agents/_index.md (NEW)
- overview.md · qwen3.6-27b.md · mlx-runtime.md · lm-studio.md · opencode-local-provider.md · locally-ai-lm-link.md · hardware-economics-and-tco.md · privacy-data-residency.md · claims-scorecard.md · source-provenance.md
- wiki/_master-index.md (UPDATED — prepended local-ai-coding-agents)
- raw/_inventory.md (UPDATED — new compiled row)

## Pilot deliverable

- output/(C) 2026-07-11-local-ai-coding-pilot-menu.md — **13 methods across A–D tiers** (💰cost / 🔒privacy tagged). Headline: A3 local PII-redaction spike → B1 local provider behind Match-Explain seam → B3 recruitment eval gate → B2 hybrid "redact local, reason cloud" routing. Watch-not-build: Apple Foundation on-device + LM Link sleep-mode batch.

## Top-3 unclosed gaps (follow-ups)

1. **Recruitment-domain quality of Qwen3.6 is unmeasured** — every benchmark is coding-domain (SWE-bench). The B3 eval set is the gate before any hireui local-inference decision.
2. **LM Link "sleeping computer" behavior unverified** — parked as HIGH-RISK; needs empirical test before any overnight-batch design.
3. **Apple Foundation Models / "new Macs" (C13)** — post-cutoff, agent-reported; watch WWDC/Apple newsroom, don't bet on it.

## Suggested next action

Run pilot **A1** (30-min viability check: does your Mac have ≥24GB unified memory?). If yes → **A3** local PII-redaction spike this week + open an `agent-*` branch in hireui for **B1**. If <24GB → do **D1 (TCO)** + **D2 (compliance memo)** first to decide whether a box is worth buying. Consider a `local-ai-coding-agents` refresh when Qwen3.7 / Apple Foundation on-device ships.
