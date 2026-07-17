# Claims scorecard — BridgeMind vibe-coding livestream

> The 6 load-bearing *incremental* claims from [[vibe-coding-livestream-bridgemind]] (i.e. claims not already covered by the flagship [[claims-scorecard]]), each adversarially verified. Verified via Workflow `wf_b9762e52-36b` (6 refute-first verifiers) + main-loop Opus anchors. Verdicts reconciled by the main loop; two agent errors overridden (see [[caveats-and-corrections-vibe-coding]]).

| # | Claim (as framed on-stream) | Verdict | Correction |
|---|---|---|---|
| CL-A | "$3/$15 is a **5×** price increase over K2.7 ($0.72/$3.50), and = Sonnet 5 pricing" | **MISLEADING** | ~**3.2–3.8×** over K2.6/K2.7's official **$0.95/$4** (his "$0.72/$3.50" is a discounted reseller rate). "= Sonnet 5" true at standard $3/$15, but Sonnet 5 is **$2/$10 intro** (33% cheaper) through Aug 31. Direction (frontier-tier, no longer budget) is right. |
| CL-B | "K3 ~25–27 tok/s while Fable 5 runs **38 tok/s**; huge speed gap" | **CORRECT-BUT-INCOMPLETE** | K3 ~26–28 tok/s at launch = real (OpenRouter). But **Fable 5 ≈ 63–70**, not 38; and on the **official** API K3 ≈ 62 vs Fable ≈ 65 (near-parity). The gap is **launch-day serving immaturity**, not architecture. |
| CL-C | "K3 2.8T > GPT-5.6 Sol's **~2.2T**; one of the largest from China" | **MISLEADING** (params) / **CONFIRMED** (largest) | GPT-5.6 Sol param count is **not disclosed** by OpenAI; "2.2T" is social-media speculation (he hedged "I'm pretty sure"). But 2.8T **is the largest Chinese open model** (> DeepSeek-V4-Pro 1.6T, Qwen 3 Max 1T+) — if anything an understatement. |
| CL-D | "#1 BrowseComp, #1 SpreadsheetBench, #2 JobBench, #3 GDPval; smarter than Opus 4.8 in knowledge work; **no coding benchmarks published**" | **MISLEADING** (+1 FALSE) | Specialist rankings **CONFIRMED** (BrowseComp #1, SpreadsheetBench #1, JobBench #2, GDPval #3). But "**no coding benchmarks**" is **FALSE** — 11+ exist (DeepSWE 67.5, FrontierSWE 81.2, Terminal-Bench 2.1 88.3…). "Smarter than Opus 4.8" over-generalizes one metric; K3 is **#3–4 overall** (see [[benchmarks-fact-vs-hype]]). Exact GDPval-vs-Opus-4.8 numbers are contested across sources — see caveats. |
| CL-E | "Not locally runnable (~700GB VRAM / $3M H200 / 2 DGX Sparks); best local = Qwen 3.6 35B/27B, Gemma 4 31B" | **CORRECT-BUT-INCOMPLETE** | Not consumer-hostable = **CONFIRMED** (~650GB–1.7TB / 8–16 H100). Named alternatives **real** (Qwen 3.6-27B, Qwen 3.6-35B-A3B, Gemma 4 31B). But "$3M" is a loose overstatement, and it omits that **quantization (~July 27 weights)** will widen local options. Precise capex counter-figures **not adopted** (uncertain). |
| CL-F | "BridgeMind (ARR $251K) ran K3 on his own BridgeBench (~68★, judges Gemini 3.1/Grok 4.5/GLM 5.2); **87–90% of chat think K3 beat Fable 5**" | **CONFIRMED** (poll real, methodology weak) | Vendor identity, ARR, benchmark all real; **structural conflict of interest** (owns test + venue + products + verdict). The poll **is real** (transcript [1:07:12], [1:09:41]) — a selection-biased YouTube-chat vote on one game, **not** a benchmark. Repo has **96★** (not 68); judges unverified outside the stream. |

## Tally (6 load-bearing incremental claims)

- **CONFIRMED (with methodology caveat):** 1 — CL-F (the facts are real; the *interpretation* is marketing)
- **CORRECT-BUT-INCOMPLETE:** 2 — CL-B, CL-E
- **MISLEADING:** 3 — CL-A, CL-C, CL-D — **CL-D also contains 1 outright FALSE sub-claim** ("no coding benchmarks published")
- **FALSE / FABRICATED (standalone):** 0
- **Net:** every load-bearing claim carries either a factual error or unsupported framing. **Hype profile: spec sound, framing inflated** — the same pattern as the sibling [[claims-scorecard|TheAIGRID scorecard]], but from a *financially-interested* source and with one hard arithmetic error (the 5× price).

## Key Takeaways

- The video's **underlying facts are mostly real** (specs, specialist benchmark rankings, launch-day speed, real local alternatives) but its **comparative framing is consistently inflated** in the streamer's favor.
- **One clean falsehood:** "no coding benchmarks published" (11+ exist). **One arithmetic error:** the "5×" price increase (~3.2–3.8× real).
- The headline "K3 beats Fable 5" rests on a **biased chat poll on a single game**, not evidence — even though the poll itself really happened.
- What survives as genuinely useful: independent **corroboration of K3's frontend/game-gen strength** (see [[hands-on-capability-evidence]]) and a real-codebase debugging data point.
