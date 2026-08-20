# The hardware ladder — and why "is N GB enough?" is the wrong question

> The core article of this topic. Supersedes the two-endpoint framing in [[../local-ai-coding-agents/hardware-economics-and-tco|local-ai-coding-agents/hardware-economics-and-tco]].

## The standing corpus claim being tested

`local-ai-coding-agents` (2026-07-11) established the corpus position from a single source (Code with Beto) with **two data points and nothing between them**:

- **18 GB MacBook** — could not run Qwen3.6-27B
- **96 GB M3 Ultra Mac Studio** — ran it comfortably
- Conclusion published: **"≥24 GB is a practical minimum"**, with a quant→machine table keyed on model weights.

This topic fills the gap with five more rungs. **The conclusion does not survive contact with them.**

## The ladder, as measured

| Memory | Machine | Bandwidth | Model | Workload | Outcome |
|---|---|---|---|---|---|
| 18 GB | MacBook (Beto) | — | Qwen3.6-27B | — | **Could not run** |
| **24 GB** | Mac mini **M4 Pro** (WEBdoze) | 273 GB/s | **4 B @ 4-bit** | small Astro site | **Stalled on an SVG for 20 min, went dark** |
| 32 GB VRAM | RTX 5090 (Zen van Riel) | 1,792 GB/s | Qwen3.5 35B MoE | greenfield Next.js | Works **fully on GPU**; *"much worse"* on any spill |
| 32 GB VRAM + 128 GB | Threadripper + R9700 (ForrestKnight) | — | Qwen3.6-27B / Coder Next | **real** Excalidraw + Warp | Easy tasks pass; hard task **47 compile errors, gave up**; **5× slower** than Opus |
| **64 GB** | Mac mini **M4 Pro** (Quân IT, anchor) | **273 GB/s** | Qwen3.5 | **large multi-service repo** | Hot, loud, laggy, context-blown API errors → **"not good enough"** |
| 64 GB | **M5 Max** (Tech With Tim) | — | Qwen3.6 35B-A3B | toy chess game | ~600 lines, **wrong language, didn't run** |
| 128 GB | M5 Max (Samuel Gregory) | — | 36 GB model | — | **~80 GB RAM consumed** once context loaded |
| 96 GB | M3 Ultra (Beto) | *(not verified here)* | Qwen3.6-27B | small feature | *"Good enough"* |

**Read the workload column, not the memory column.** The two sources that ran **real production repositories** are the two that returned **negative** verdicts — at 64 GB and at 128 GB-class hardware. Every positive verdict sits on greenfield or toy work.

## Correction 1 — the anchor's machine is not a base M4

Quân IT titles his video *"Mac mini M4, 64GB ram"* and says "Max Mini M4". **Apple's own specs make that configuration impossible:** the base M4 addresses a **maximum of 32 GB** unified memory. Only the **M4 Pro** offers 64 GB in a Mac mini.

His machine is therefore a **Mac mini M4 Pro, 64 GB — 273 GB/s**. This matters because it is the number that actually predicts his experience:

| Chip | Max unified memory | Memory bandwidth |
|---|---|---|
| M4 (base) | 32 GB | **120 GB/s** |
| **M4 Pro** | **64 GB** | **273 GB/s** ← anchor + WEBdoze |
| M4 Max (32-core GPU) | — | 410 GB/s |
| M4 Max (40-core GPU) | 128 GB | 546 GB/s |
| RTX 4090 | 24 GB VRAM | **1,008 GB/s** |
| RTX 5090 | 32 GB VRAM | 1,792 GB/s |

The anchor is running agentic coding at **~27% of an RTX 4090's memory bandwidth**, and at **half** the M4 Max figure Tech With Tim quotes when he compares Mac to PC. Memory *capacity* let him load the model. Memory *bandwidth* is why it crawled.

## Correction 2 — capacity is not the binding constraint

Every source in the bundle, independently, lands on the same mechanism. Required memory is **not** `weights`:

```
weights  +  KV cache(context)  +  harness system prompt  +  OS/app headroom
```

- **Samuel Gregory** measured it directly: a **36 GB model consumed ~80 GB of RAM** once context was loaded. *"Even though the model's 36, this is how the context indeed has an impact on the amount of RAM that you need."*
- **Zen van Riel:** *"Especially for agent coding, you're going to be using very big context windows, where the compute cost basically scales exponentially."*
- **Apple, first-party** ([[apple-mlx-stack]]): *"Agentic sessions usually comprise hundreds of thousands of tokens, and most of those are not generated."*

`context` is driven by **repository size**. The harness contributes a large fixed floor before your code is read at all — **Claude Code's system prompt is 4,200 tokens** (Anthropic's own documented figure). See [[why-agentic-differs-from-chat]].

The existing corpus article already names KV cache as "the hidden cost" — then publishes a table keyed on weights alone and calls 24 GB a minimum. That is the error this topic corrects.

## Correction 3 — the 24 GB floor is refuted outright

The corpus called 24 GB a *practical minimum*. At 24 GB, with an agent attached and a 132 K context configured, **a 4-billion-parameter 4-bit model failed to finish a static marketing page.** WEBdoze's own conclusion:

> *"M4 Pro Mac Mini is not powerful enough even to run a four bits and four billion parameter model."*

24 GB is not a floor for agentic coding. It is below it.

## What Tech With Tim's ladder actually assumes

His cheat sheet — 8 GB→7 B · 12–16 GB→14 B · 24 GB→32 B · 64 GB+→70 B — is **CORRECT-BUT-INCOMPLETE**. At FP16 a 7 B model needs ~14 GB, so the ladder only works under aggressive quantization (roughly INT4), which he never states. Treat it as a **4-bit-quantized chat** ladder, and subtract again for agentic context. He does state the two qualifiers that matter:

- On Mac, only **~75–80%** of unified memory is usable — the rest is OS and other processes. *(Unverified against any Apple primary source — see [[caveats-and-corrections]].)*
- A model that overflows into system memory or disk is *"like 100 times slower."* Zen van Riel independently: spilling even part of a model to system RAM means *"much worse"* performance, and *"just because you can fit a model on your system... doesn't mean it's actually going to be usable in practice."*

## The corrected rule of thumb

> **"Is N GB enough?" is unanswerable without naming the workload.** State it as a pair — *(memory, repository size)* — or don't state it.

And add the second axis the corpus never had: **bandwidth**, which determines prefill speed, which is where agentic sessions actually spend their time.

## Key Takeaways

- **The corpus's "≥24 GB practical minimum" is refuted.** A 24 GB M4 Pro failed a small static site with a 4 B 4-bit model.
- **The anchor's "Mac mini M4 64 GB" is necessarily an M4 Pro** (base M4 caps at 32 GB) — 273 GB/s, ~27% of an RTX 4090.
- **Capacity loads the model; bandwidth and context determine whether agentic work is usable.** A 36 GB model measured at ~80 GB RAM in use.
- **Every positive "good enough" verdict in the corpus sits on toy or greenfield work.** Both sources testing real repositories returned negative verdicts.
- **Quantify the workload or don't quantify the answer.**

## See also
[[why-agentic-differs-from-chat]] · [[apple-mlx-stack]] · [[anchor-quanit-64gb]] · [[corpus-correction]] · [[claims-scorecard]] · [[../local-ai-coding-agents/hardware-economics-and-tco|local-ai-coding-agents/hardware-economics-and-tco]]
