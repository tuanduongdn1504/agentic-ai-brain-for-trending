# local-llm-coding-hardware-ladder

> **Topic index.** Seven sources on running a local LLM for real coding work on Apple silicon — compiled to **test a standing corpus claim**, not to open a new subject.
> **Compiled:** 2026-08-20 · path 1 anchored bundle (operator anchor + yt-search ×5 + 1 first-party main-loop addition). All transcripts read in full; **no NotebookLM**.
> **Anchor:** [`GBf_mKxGqtk`](https://www.youtube.com/watch?v=GBf_mKxGqtk) — Quân IT, *"Thử local LLM, coding trên Mac mini M4, 64GB ram"* (VN, 48:34). Anchor validation **PASS 1/1**.
> **Raw:** [`raw/2026-08-20-local-llm-coding-apple-silicon-hardware-ladder.md`](../../raw/2026-08-20-local-llm-coding-apple-silicon-hardware-ladder.md)
> **Verification:** Workflow `wf_9dd08c75-e02` — 24 agents, 1.41M tokens, 387 tool calls, 0 errors — plus 7 main-loop Opus checks. **Scorecard: 12 CONFIRMED · 5 CBI · 1 FALSE · 3 UNRESOLVED · 0 FABRICATED.**

## Why this topic exists

[[../local-ai-coding-agents/_index|local-ai-coding-agents]] left the hardware question with **two endpoints and nothing between them** — an 18 GB MacBook that failed, a 96 GB Mac Studio that worked — and published **"≥24 GB is a practical minimum."** The operator submitted a 48-minute hands-on at **64 GB, the untested middle**, against a **large real production repo**. The rubric filled the rest of the ladder, including a 24 GB rung.

**The claim did not survive.**

## The one-sentence finding

> **Memory capacity is the wrong axis.** Agentic coding is dominated by *prefill* — re-processing accumulated context every loop — so the binding constraints are **memory bandwidth** and **repository size**, not whether the weights fit. A machine that comfortably chats with a model can fail outright at agentic coding with the same model. **"Is N GB enough?" is unanswerable without naming the workload.**

And the finding that should decide anyone's next purchase: **every positive "good enough" verdict in this bundle sits on toy or greenfield work. Both sources that tested real production repositories returned negative verdicts** — at 64 GB and at 128 GB-class hardware. Apple's own demo uses a blank Xcode project.

## Articles

- [[the-hardware-ladder]] — **start here.** The eight-rung ladder, the memory/bandwidth table, and the three corrections to the standing claim (incl. why the anchor's "M4" must be an M4 Pro)
- [[why-agentic-differs-from-chat]] — the mechanism: prefill dominance, the 4,200-token harness floor, KV-cache scaling, and why spill is catastrophic rather than gradual
- [[apple-mlx-stack]] — the **first-party** source: Apple's four-layer stack, M5's 4× matmul, continuous batching, distributed inference, and *"Ollama, LM Studio and vLLM are built on MLX"*
- [[anchor-quanit-64gb]] — the anchor in full: the only real-production-repo test in the bundle, and its unprompted **filesystem-scope security** finding
- [[the-tooling-layer]] — Ollama / LM Studio / OMLX / MLX-LM server; wiring Claude Code via `ANTHROPIC_BASE_URL`; and why three of seven sources route *around* Claude Code
- [[quality-ceiling-and-failure-modes]] — the type-checker-invisible bug, the 47-error give-up, the silent hang, the model-identity trap
- [[corpus-correction]] — the precise diff against `local-ai-coding-agents`, and recommended (unapplied) edits
- [[claims-scorecard]] — 21 claims graded
- [[caveats-and-corrections]] — source overstatements, sponsor disclosures, **two verification-agent errors caught**, and **a real bug found in this vault's own drain script**
- [[source-provenance]] — the seven sources, method, collision greps, and deepen candidates

## What to actually do with this

| If you… | Then… |
|---|---|
| Have a **≤64 GB M-series** and a **large repo** | Don't expect agentic local coding to work. Two sources measured it; both said no. |
| Have any Mac and a **small/greenfield** project | It works. Apple, ForrestKnight and Tech With Tim all demonstrate it. |
| Are buying **for this purpose** | Bandwidth and generation matter more than GB. **M5** has dedicated neural accelerators for exactly this bottleneck — and nobody has yet tested one on a real repo ([[source-provenance]] deepen #1). |
| Must keep code **in the building** (ITAR/HIPAA/IP) | This is the real use case. ForrestKnight's framing, not the cost framing, is the honest one. |
| Are trying it **tonight** | Raise the context window **before** anything else — a default window hangs silently under Claude Code's 4,200-token system prompt. Then use **subagents**, and consider **OpenCode** over Claude Code. |

## Key cross-links

[[../local-ai-coding-agents/_index|local-ai-coding-agents]] (the topic corrected) · [[../quanit-becoming-ai-engineer-2026/_index|quanit-becoming-ai-engineer-2026]] (same creator) · [[../kimi-k3-worlds-most-powerful-ai/_index|kimi-k3-worlds-most-powerful-ai]] · [[../deepseek-harness/_index|deepseek-harness]] · [[../harness-engineering/_index|harness-engineering]] · [[../claude-api-cost-optimization/_index|claude-api-cost-optimization]]
