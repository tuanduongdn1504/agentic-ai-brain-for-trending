# Source provenance & verification record

## The source

- **Video:** [Zof2Oaj14rk](https://www.youtube.com/watch?v=Zof2Oaj14rk) — *"Local AI Coding Agents Are Finally Good Enough"*
- **Channel:** Code with Beto (**Beto Moedano**, `@codewithbeto`), a React Native / Expo educator.
- **Uploaded:** 2026-07-09 · 16:55 · ~6.6K views / 165 likes at ingest · English (manual `en-US` captions).
- **Ingest:** path 5 (yt-dlp-only). Captions → dedupe → full transcript, **read in full in the main loop**. No NotebookLM.
- **Raw:** [../../raw/2026-07-11-local-ai-coding-agents.md](../../raw/2026-07-11-local-ai-coding-agents.md)

## Presenter assessment (credibility)

- **Real practitioner, not a funnel-only creator.** Ships genuine products: **Inkigo** (AI Tattoo Try-On, live on the App Store, ~$650/mo MRR — modest and *honestly* modest), **Platano** (AI app template), a **React Native course**, and the book *"From Idea to App Store with Claude Code."*
- Business framing is **enthusiastic but not fraudulent** — the opposite of the [[../jasonlee-claude-mobile-app/_index|"$80K/Mo"]] pattern. He hedges appropriately ("not going to replace the latest Opus"). The only over-claim to strip is C12's "free."

## First-party originals double-dived

| Original | First-party source | Article |
|---|---|---|
| Qwen3.6-27B | Alibaba Qwen (blog + HF model card) | [[qwen3.6-27b]] |
| Apple MLX / mlx-lm | `ml-explore` GitHub + Apple | [[mlx-runtime]] |
| LM Studio | lmstudio.ai docs + blog | [[lm-studio]] |
| opencode | opencode.ai + `sst/opencode` (Anomaly) | [[opencode-local-provider]] |
| Locally AI / LM Link / Apple Foundation Models | LM Studio blog + Apple Developer | [[locally-ai-lm-link]] |

## Verification workflow

- **Workflow `wf_830dc448-b7e`** — 17 agents: 7 first-party dives + 9 refute-first skeptics (3 headline claims × 3 lenses) + 1 completeness critic. ~804K tokens, 328 tool calls, ~7.5 min.
- **Agents ran on Haiku 4.5** (cheaper tier) → several confabulations, corrected below.
- **2 skeptics died** on "prompt too long" (C12 latency + C12 tiered-routing lenses — they invoked the `claude-api` skill, which ballooned context). Closed by main-loop reasoning + the TCO skeptic that *did* complete.

## Corrections logged (Rule 12 — fail loud)

Independent main-loop anchors **overrode** these Haiku-agent errors:

1. **"Claude Opus 4.5 does not exist" → WRONG.** The qwen dive hit blocked pages and concluded Opus 4.5 was fictional, marking C4 UNVERIFIABLE. **Opus 4.5 is a real, released model** (Anthropic "Introducing Claude Opus 4.5"; SWE-bench Verified **80.9**, Terminal-Bench **59.3** — independently confirmed via Vellum/DataCamp/Anthropic). The presenter dive's own `benchlm.ai` finding also contradicted the qwen dive. **C4 corrected to CORRECT-BUT-INCOMPLETE.**
2. **"Latest MLX is v0.32.0, July 2024" → STALE/WRONG.** MLX is under very active development; a mid-2026 video is not on a 2024 build. The wiki avoids citing any specific version and grounds MLX speed on independent 2026 benchmarks instead ([[mlx-runtime]]).
3. **Over-penalized minor claims.** The qwen dive graded C2 (1-day date drift) and C14 (~20 GB vs 16.8 GB) as "MISLEADING." Main loop softened to CORRECT-BUT-INCOMPLETE / ~CONFIRMED — a 1-day drift and a fair rounding are not "misleading."
4. **Unverified specifics quarantined.** The C6 refute skeptics cited exact tok/s figures, GitHub issue IDs, and a "25% failure rate." These are **not independently verified** and are **not** stated as fact in the wiki — only the *direction* (runtime ≠ reliability; 27B convergence) is asserted, grounded in an independent 2026 benchmark search.

## Garble-guard wins (fresh-true facts a cutoff-bounded skeptic would reject)

Per the project's **discard-as-garble guard**, two date-sensitive claims that *look* like confabulation were verified TRUE before any discard:
- **"Locally AI is from LM Studio"** — TRUE since the **2026-04-08 acquisition**. [[locally-ai-lm-link]]
- **"Qwen3.6 ≈ Opus 4.5 on agentic coding"** — TRUE directionally (Terminal-Bench tied 59.3). [[qwen3.6-27b]]

## Un-fetchable / low-confidence (flagged, not fabricated)

- Qwen's full technical report (GitHub partially blocked to agents) — benchmarks anchored via HF card + independent sources instead.
- WWDC26 / "Core AI" / "new Macs" specifics (C13) — post-cutoff, agent-reported; kept as **watch-items**, not facts.
- LM Link sleep-mode behavior (C9) — undocumented; **verify empirically**.
- Beto's exact on-screen benchmark chart — not independently viewable; the *claim* was checked against public benchmarks.

## See also
[[_index]] · [[claims-scorecard]]
