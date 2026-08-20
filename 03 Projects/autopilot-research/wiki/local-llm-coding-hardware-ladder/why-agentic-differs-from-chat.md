# Why agentic coding is a different hardware problem from chat

> The mechanism all seven sources converge on — including Apple's own engineers. This is the article that explains every failure in [[the-hardware-ladder]].

## The claim

**A machine that comfortably chats with a model can fail at agentic coding with the same model.** Not slower — *fail*. The benchmarks people quote (tokens/sec, parameter count, "runs on 18 GB") measure the wrong thing.

## Why: agentic sessions are dominated by prefill, not generation

Apple states it first-party in [[apple-mlx-stack|WWDC26 session 232]]:

> *"In an agentic workflow, every time the model receives tool output, it has to process all that new context before it can reason about the next step. This happens over and over throughout the agentic loop, and it adds up fast. **Agentic sessions usually comprise hundreds of thousands of tokens, and most of those are not generated.**"*

That last clause is the whole article. In a chat session, most tokens are **generated** — and generation speed is what "tokens per second" measures. In an agentic session, most tokens are **read**: file contents, tool output, build errors, diffs, subagent reports. Every loop iteration re-processes the accumulated context before producing anything.

So the relevant metric is **prompt-processing (prefill) throughput**, which is governed by **memory bandwidth and matmul throughput** — not by whether the weights happen to fit.

**This is why the ladder in [[the-hardware-ladder]] does not sort by memory.** A 24 GB M4 Pro at 273 GB/s and a 64 GB M4 Pro at 273 GB/s have the *same* prefill characteristics; the extra memory buys a bigger context, which makes the prefill problem **worse**, not better.

Apple's fix is a hardware generation away: **M5 neural accelerators make matrix multiplication 4× faster than M4**, and Apple says this "translates almost exactly" into prompt-processing speedup. The anchor is on **M4 Pro** — the generation immediately *before* the silicon designed for exactly the bottleneck he hit.

## Three multipliers stack before your code is read

### 1. The harness system prompt is a fixed floor

**Claude Code's system prompt is 4,200 tokens** — Anthropic's own documented figure ([code.claude.com/docs/en/context-window](https://code.claude.com/docs/en/context-window)). That is spent on *every* session before a single file is opened.

Zen van Riel found the sharp edge: with LM Studio's small default context, the request **hangs forever with no error**:

> *"It will hang indefinitely because the Claude Code system prompt is thousands of tokens long. We are actually going to be hitting the limit of my local model immediately and **there's no clear error message indicating this**."*

A cloud model never exposes this because its window is enormous. Point the same harness at a local model with a default window and it dies silently. See [[quality-ceiling-and-failure-modes]].

### 2. KV cache scales with context, and context scales with your repo

Samuel Gregory measured the multiplier directly on a 128 GB M5 Max:

> a **36 GB model** consuming **~80 GB of RAM** once context was loaded. *"Even though the model's 36, this is how the context indeed has an impact on the amount of RAM that you need."*

Zen van Riel names the curve: *"Especially for agent coding, you're going to be using very big context windows, where **the compute cost basically scales exponentially**."*

### 3. Spill is catastrophic, not gradual

- **Tech With Tim:** a model that overflows VRAM into system memory or disk is *"like 100 times slower."*
- **Zen van Riel:** *"just because you can fit a model on your system by putting some of the parameters on your system RAM doesn't mean that it's actually going to be usable in practice."*

There is no graceful degradation. You are either resident or you are unusable.

## The receipts, in order of severity

| Source | Machine | What the mechanism did to them |
|---|---|---|
| **Quân IT** (anchor) | 64 GB M4 Pro | Repeated **API errors** on a large repo; correctly self-diagnosed *"cái context của mình nó bị lớn quá"* — my context got too big. 2 min 45 s to first token. |
| **WEBdoze** | 24 GB M4 Pro | Throughput decayed **70 → 20 → 18 tok/s** as context filled: *"the context is already at 35K. That's why it's that slow."* Then died. |
| **Zen van Riel** | 32 GB RTX 5090 | Silent indefinite hang at default context; slow first response purely from the Claude Code system prompt. |
| **Samuel Gregory** | 128 GB M5 Max | 36 GB model → ~80 GB resident. |
| **Apple** | — | *"most of those are not generated."* |

## What the ecosystem is building in response

Every serious tool in the bundle is attacking prefill, not generation:

- **OMLX** — persists the KV cache to SSD in safetensors format (hot RAM / cold SSD tiers) so *"on the next request with a matching prefix, they're restored from disk instead of recomputed from scratch — even after a server restart."* Prefix reuse *is* the prefill fix. See [[the-tooling-layer]].
- **MLX LM server** — **continuous batching**, so parallel subagents don't queue behind each other.
- **M5 neural accelerators** — 4× matmul.
- **MLX distributed** — parallelizes prompt processing across Macs, which Apple says "directly speeds up the agentic loop."

## The mitigation you can apply today: subagents

Zen van Riel's recommendation, independently mirrored by Apple's continuous-batching design:

> *"I'm explicitly asking it to create sub-agents for each task. This means they will create new instance of Cloud Code with a fresh context window... **I definitely recommend you to work with sub-agents more than ever if you're doing local AI coding**."*

Subagents cap the per-context prefill cost instead of letting one conversation grow without bound. ForrestKnight arrives at the same place from the quality side: *"break those tasks into much smaller tasks and give it one by one by one."*

Note the corpus resonance — the anchor observed Claude Code doing exactly this against his local model, launching a background general-purpose subagent to read the repo.

## Key Takeaways

- **Agentic sessions are prefill-dominated.** Apple, first-party: *"most of those are not generated."* Tokens/sec measures the wrong half.
- **Prefill is governed by bandwidth and matmul, not capacity.** More RAM buys more context, which costs more prefill.
- **Three fixed multipliers stack before your code is read:** a 4,200-token harness system prompt, KV cache scaling with repo size, and catastrophic (100×) spill.
- **A default context window is a silent-failure landmine** for any local model behind a real harness.
- **Subagents are the one mitigation available without new hardware** — and the ecosystem's other fixes (SSD prefix cache, continuous batching, M5 accelerators, distributed inference) all target prefill too.

## See also
[[the-hardware-ladder]] · [[apple-mlx-stack]] · [[the-tooling-layer]] · [[quality-ceiling-and-failure-modes]] · [[anchor-quanit-64gb]]
