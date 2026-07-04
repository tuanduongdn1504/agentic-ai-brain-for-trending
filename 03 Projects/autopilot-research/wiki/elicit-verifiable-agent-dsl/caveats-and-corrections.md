# Caveats & corrections

Grading of the softer claims and the things a future reader should not over-trust. Full verification record: [[source-provenance]].

## Caption garbles (EN auto-captions)

| Garble | Truth | Basis |
|---|---|---|
| "Alissa" / "illicit" / "a list" / "Ash Bell" / "SHPL" / "HPL" | **Elicit** / **ÆPL** | Speaker context; VN dub renders both correctly |
| "3.5 Sonar" | **Claude 3.5 Sonnet** | VN dub line 14 renders "3.5 Sonnet" correctly |
| "the tropic color" | "the **Anthropic** color" | Describing the curator's Claude-brand ochre box |
| "AC in the UK" (demo join) | **UK AISI** (AI Safety → AI Security Institute, renamed 2025-02-14) | Anthropic UK MOU Feb 2025 ([[demo-research-landscape]]) |

## VN-dub artifacts (BizMate)

- **Severe mistranslation:** "the Elicit product" → **"sản phẩm chống hàng giả"** (anti-counterfeit product), inheriting the elicit/illicit confusion and inverting the meaning (research assistant → counterfeit-detection tool). Localized-content caveat for any VN reader.
- **Garble preserved, not fixed:** "Brandon Taste" (VN line 32) = the EN garble of "the provider's **brand and taste**" — the dub carried the caption error through.
- **Quality-control positive:** the dub *corrected* "3.5 Sonar" → "3.5 Sonnet" — evidence of some human/model review, not pure passthrough.
- Description links resolve: skool.com/bizmate-ai-community-9131 + anthropic.skilljar.com. Authorization: **attributed but unverified** (same status as the prior two BizMate chains — [[../agent-memory-architecture/caveats-and-corrections]], [[../google-zero-open-web/_index]]).

## Qualified / single-source claims

| Claim | Status |
|---|---|
| **ÆPL name & spelling** | Name CONFIRMED on-camera; spelling is a **reconstruction** (spoken-only; no written first-party rendering found). "ÆPL"/"AshPL" both inferred. |
| **"Zero public mention of ÆPL/curator/event-sourcing on Elicit surfaces"** | Qualified to **"none found on sampled surfaces (homepage, blog, docs, GitHub), 2026-07-04"** — a sampled crawl, not a proof of absence (critic-flagged overreach, [[source-provenance]] #2). |
| **Pi = Earendil/Zechner harness at Elicit** | CONFIRMED-by-convergence but the **Elicit↔pi link is single-source** (Brady's statement). Quote as his claim, not pi marketing. ([[pi-harness-and-curator-models]]) |
| **Session took "a couple of hours"** | Brady's own figure for the demo session; not a benchmark. |
| **Whole-program "statistical guarantees of cohesion and correctness"** | His framing; no published methodology or numbers accompany it. Plausible given purity+memoization, but treat as a design claim, not a proven bound. |
| **Official description "quiver of models"** | T1 (yt-dlp) — Anthropic's word, not Brady's; the transcript shows the interpreter "calling into language models," which corroborates the plurality. |

## Verifier misfires this pass (fail-loud)

1. **Codex "deprecated in 2023" misread** — corrected; Codex is active in 2026 ([[pi-harness-and-curator-models]], [[../codex/_index]]).
2. **Fetch-failure treated as absence** twice (YouTube description; BizMate channel) — both overridden by main-loop yt-dlp ground truth.
3. **Kevin-Chen-venue over-read** — verifiers called it a "critical wiki correction"; the memory-architecture wiki had actually **hedged** correctly. Upgraded, not retracted.

## Cross-topic correction shipped

- Resolved the **recording-venue hedge** for the Kevin Chen "Agents that remember" video (`geUv4CjPpxI`) → **CONFIRMED London 2026-05-20** (SF-Ext instance was Tina Vachovsky). Edited [[../agent-memory-architecture/anthropic-memory-stores-and-dreaming]] provenance line + logged in that topic's [[../agent-memory-architecture/caveats-and-corrections]]. Same London event as this talk.

## Key Takeaways

- The technical spine (language properties, architecture, whole-program mechanism, checklist) is high-confidence, verbatim-sourced.
- The soft edges are: exact spelling of ÆPL, the universal "zero footprint" phrasing, and the Elicit↔pi link — all flagged, none load-bearing for the lessons.
- The VN dub is a *useful but imperfect* source: it fixes some caption errors and introduces its own — never quote the dub for product identity without the EN original.
