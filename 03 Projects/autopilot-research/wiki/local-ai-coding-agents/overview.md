# Overview — the local-coding-agent walkthrough (corrected)

> **Source:** [[_index]] · video [Zof2Oaj14rk](https://www.youtube.com/watch?v=Zof2Oaj14rk).
> Every step below is what the video demonstrates, annotated with what the [[source-provenance|first-party dive]] confirmed or corrected.

## The pitch

- "If you've ever tried to run a local LLM… it's pretty trash." — true, historically.
- What changed (Beto's claim): **Qwen3.6-27B** (2026-04-22) + **Apple MLX** make local coding "finally good enough." **Verdict: defensible.** The stack is real, it works, and it builds real features. The over-claims are about *reliability*, *speed*, and *"free"* — not about whether it works.

## The stack, step by step

1. **Get the model into LM Studio.**
   - Download [LM Studio](https://lmstudio.ai) → enable **Developer mode** (Settings) to see the developer tab.
   - Model-search tab → download `Qwen3.6-27B` → "it's going to be like 20 gigabytes." (Q4_K_M is ~16.8 GB; a Q5/Q6/MLX quant is ~19.5–22.5 GB, so ~20 GB is a fair round number — [[hardware-economics-and-tco]].)
   - Load it in the Chat tab. It's a **reasoning model with vision + tool-calling** ([[qwen3.6-27b]]).

2. **Turn LM Studio into a local server.**
   - The **developer tab** streams tokens + logs live, lets you raise the **context window**, set **max concurrency** (e.g. 4 parallel sessions), and toggle **KV-cache quantization** ("faster but can hurt quality" — accurate tradeoff).
   - Toggle the server on → LM Studio exposes an **OpenAI-compatible** endpoint (`/v1/chat/completions`, `/v1/models`, …) at `http://localhost:1234/v1` ([[lm-studio]]).

3. **Point opencode at the local endpoint.**
   - Add a custom provider in `opencode.json` with the LM Studio `baseURL` → run `opencode` in your project ([[opencode-local-provider]]).
   - ⚠️ **Correction:** Beto says "you need to pass the **modalities** here" to enable image recognition. **opencode has no `modalities` setting.** Vision works by **drag-and-drop** of images by default on a vision-capable model. (See [[opencode-local-provider]].)

4. **It works agentically, offline.** In his real **AI Tattoo app (Inkigo)** codebase, Qwen3.6 via opencode:
   - built a new tab; identified **SF Symbols** from a pasted **screenshot** (vision, local); wrote a Markdown doc; built HTML **Minesweeper + Snake** games; and on a hard task ran **31 tool calls**, scanned the whole codebase, detected it uses **Better Auth**, and rendered a dev-only user-info card.
   - That hard task **"took almost 10 minutes," machine "on fire," fans loud** — honest about the latency ([[hardware-economics-and-tco]]).

5. **Chat from your phone.** **Locally AI** (an app **acquired by LM Studio** on 2026-04-08) + the **LM Link** feature (Tailscale-based) let you talk to the desktop model from an iPhone ([[locally-ai-lm-link]]). His "your computer can be sleeping" aside is dubious (sleep usually drops the network).

## The honest takeaway (the part worth keeping)

Beto's closing advice — *"cancel ChatGPT, keep Claude for complex/agentic work, use the local model for simple things (refactoring, moving code around)"* — is the real insight: **tiered routing**, cheap model for cheap tasks, frontier model for hard ones. The **"I didn't pay for anything"** framing is theater (it ignores the ~$4,000 Mac Studio), but the *strategy* is sound and is exactly the [[../claude-api-cost-optimization/_index|model-tiering]] discipline. See [[claims-scorecard]] C12 and [[hardware-economics-and-tco]].

## What the video does NOT cover (gaps a builder must fill)

- No quantization-vs-quality measurement (he runs a **4-bit quant**, not the full model the benchmarks describe).
- No throughput/latency numbers, no batch behavior for many requests.
- No security/ops discussion of self-hosting (model updates, the box's own security).
- Everything is coding-domain; nothing about whether local quality holds on **other domains** (e.g. recruitment/CV matching — see [[privacy-data-residency]] + the pilot menu).
