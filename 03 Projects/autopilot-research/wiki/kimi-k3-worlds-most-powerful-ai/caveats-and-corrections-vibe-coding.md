# Caveats & corrections — vibe-coding deepening (Rule 12 log)

> Fail-loud record for the [[vibe-coding-livestream-bridgemind]] deepening pass: agent errors caught + overridden, contested numbers flagged, and figures deliberately **not** adopted. Verification: Workflow `wf_b9762e52-36b` (15 agents, ~691K tokens, 135 tool calls, 0 errors, **1 empty result**) + main-loop Opus WebSearch/skill anchors.

## Agent errors caught & overridden (Rule 12)

1. **CL-F poll-existence doubt — OVERRIDDEN.** The CL-F verifier and the completeness critic both flagged the "87–90% think K3 beat Fable 5" poll as *"no searchable public record; may be conflated or fabricated."* This is a **can't-watch-the-video artifact** — the poll is **verbatim in the transcript** ([1:07:12] "90% out of 300 votes"; [1:09:41] "729 votes and 87%"; the drafted X-post at [1:12:26]). The main loop read the primary source and **overrode the doubt**: the poll is real; the correct critique is its *methodology* (selection-biased chat vote), not its existence. Same failure mode as prior Haiku-can't-watch ships (local-ai, google-ai-studio, miai-iphone-ocr).

2. **Contested GDPval / knowledge-work numbers — NOT SHIPPED as fact (Rule 7 surface-don't-average).** Across sources the exact GDPval figures conflict:
   - Community-benchmarks dive: **Opus 4.8 = 1,890** on GDPval-AA (K3 1,687 loses by ~200).
   - CL-D verifier: **Opus 4.8 = 1,600** (K3 wins).
   - Corpus baseline (flagship [[claims-scorecard]], shipped 2026-07-17): K3 1,687 "beats Opus 4.8," **but #3–4 overall**; Fable 5 Max **1,815**.
   - Workflow also flagged an AA reading of **Fable 5 = 1,760** (vs corpus 1,815).
   These are exactly the confabulation-prone numerics the wiki-verify discipline warns about. **Resolution:** ship only the robust, source-agreed claim — *K3 is a specialist that tops a few narrow benchmarks but sits #3–4 on the aggregate index, behind Fable 5 and GPT-5.6 Sol* — and do **not** assert a confident K3-vs-Opus-4.8 GDPval ranking or import either Haiku number. **Flagged for the next audit:** re-verify Fable 5 (1,815 vs 1,760) and Opus 4.8 (1,890 vs 1,600) GDPval-AA figures in the flagship [[benchmarks-fact-vs-hype]] against a fresh Artificial Analysis read; the flagship's numbers were **not** retro-edited on the strength of conflicting Haiku readings.

3. **Local-hosting capex — precise counter-figures NOT adopted.** The CL-E verifier "corrected" the streamer's loose "$3M" to ~$150–200K (5× H200) or ~$28–37K (6–8 DGX Sparks). These rest on a shaky "700GB VRAM" premise and **conflict with the corpus's own 8–16 H100 / 650GB–1.7TB** figure. Shipped conclusion: *not consumer-hostable; data-center hardware; exact capex uncertain* — the precise dollar figures are **left out** rather than presented as fact.

## Verified factual corrections (shipped)

- **"5× price increase" → ~3.2–3.8×** over K2.6/K2.7's official $0.95/$4. His "$0.72/$3.50" baseline is a discounted reseller rate. (CL-A)
- **"Fable 5 = 38 tok/s" → ~63–70 tok/s** (workflow, medium-confidence on the exact number; direction safe). Official-API K3 ≈ 62 ≈ Fable 5 ≈ 65 (near-parity). (CL-B)
- **"GPT-5.6 Sol ~2.2T" → undisclosed** (OpenAI does not publish; "2.2T" is social-media speculation). (CL-C)
- **"No coding benchmarks published" → FALSE** — 11+ exist (DeepSWE, FrontierSWE, Terminal-Bench 2.1, ProgramBench…). (CL-D)
- **"68 stars" on BridgeBench repo → 96 stars.** (CL-F)
- **Model-name precision:** the streamer's "Qwen 3.6 35B" is **Qwen 3.6-35B-A3B** (an MoE — 35B total / ~3B active). Real, on Hugging Face.

## Confirmed (survived refutation)

- K3 launch-day **~25–27 tok/s** on OpenRouter (his figure = accurate for his provider).
- **2.8T = the largest Chinese open model** (> DeepSeek-V4-Pro, Qwen 3 Max).
- **$3/$15 = Sonnet 5 *standard* pricing** (asterisk: Sonnet 5 intro is $2/$10 through Aug 31).
- **BridgeMind / BridgeBench real; ARR $251,136 verifiable; the poll real.**
- **Remotion** is a real React programmatic-video framework.
- Named local alternatives (Qwen 3.6-27B/35B-A3B, Gemma 4 31B) all real.

## Process disclosures

- **Workflow model-override limitation:** per-agent `opus`/`sonnet`/`effort:high` overrides in the workflow script were **silently ignored** — all 15 agents ran **Haiku 4.5** (same as the OKF, kimi-k3, and aws-email ships). Every load-bearing correction was therefore independently re-verified in the main loop on Opus before shipping; `main-loop-anchors.md` (scratchpad) holds those anchors.
- **1 empty agent result:** the `dive:local-hosting` agent finished without emitting structured output (last tool = WebFetch on Qwen3.6-27B). Fully covered by the CL-E verifier + the corpus's existing local-hosting facts; no coverage gap.
- **Creator PII:** held to the **@bridgemindai** handle + "BridgeMind" brand only; no real-name assertion (the "Day X to $1M" series is public but the person's legal name is not load-bearing).

## Key Takeaways

- Two Haiku errors caught: the poll-existence doubt (overridden from the transcript) and the contested GDPval numbers (flagged, not shipped).
- One clean falsehood shipped as a correction ("no coding benchmarks"); one arithmetic error corrected (5× → ~3.2–3.8×); one repo-stars fix (68 → 96).
- Deliberately **not** shipped: precise local-hosting capex figures and any confident K3-vs-Opus-4.8 GDPval ranking — both rest on conflicting/ungrounded numbers.
