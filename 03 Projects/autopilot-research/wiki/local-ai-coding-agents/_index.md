# local-ai-coding-agents

> **Topic:** Running a genuinely-useful coding agent 100% locally/offline — no subscription, no API, no data egress — on a high-RAM Apple Silicon Mac, as of mid-2026.
> **Compiled:** 2026-07-11 from a single operator-submitted YouTube video (path 5, yt-dlp-only, full transcript read in main loop) + a double-dive into the FIRST-PARTY originals beneath every tool it names.
> **Source video:** [Zof2Oaj14rk](https://www.youtube.com/watch?v=Zof2Oaj14rk) — **Code with Beto** (Beto Moedano, `@codewithbeto`), *"Local AI Coding Agents Are Finally Good Enough"* (2026-07-09, 16:55, ~6.6K views at ingest).
> **Raw:** [../../raw/2026-07-11-local-ai-coding-agents.md](../../raw/2026-07-11-local-ai-coding-agents.md)
> **Verification:** Workflow `wf_830dc448-b7e` — 17 agents (7 first-party dives + 9 refute-first skeptics + 1 completeness critic, ~804K tokens, 328 tool calls). Agents ran on Haiku 4.5; several confabulations were caught and **overridden with main-loop independent anchors** (see [[source-provenance]]). 2 skeptics died on "prompt too long"; closed by main-loop reasoning.

---

## The one-sentence thesis

The 2026-04-22 release of **Qwen3.6-27B** (dense, Apache-2.0, multimodal, agentic-coding) — run through **Apple MLX** inside **LM Studio** (which exposes an OpenAI-compatible local server) and driven by the **opencode** terminal agent — is the first time a *fully local, offline, zero-subscription* coding agent is good enough to build real app features. The catch: it needs a lot of unified memory (Beto uses a 96GB M3 Ultra Mac Studio; his 18GB MacBook couldn't run it).

## The 4-layer local stack (how the pieces connect)

| Layer | Tool | Role | Article |
|---|---|---|---|
| **Model** | Qwen3.6-27B (Alibaba) | the weights — dense 27B, multimodal, agentic-coding | [[qwen3.6-27b]] |
| **Runtime** | Apple MLX | executes the model fast on Apple Silicon (unified memory) | [[mlx-runtime]] |
| **Server/host** | LM Studio | downloads/loads the model, serves an **OpenAI-compatible** endpoint | [[lm-studio]] |
| **Agent** | opencode (Anomaly/SST) | the terminal coding agent that calls the local endpoint | [[opencode-local-provider]] |
| *(mobile)* | Locally AI + LM Link | chat with your desktop model from your phone | [[locally-ai-lm-link]] |

## Articles in this topic

- [[overview]] — the video walkthrough, corrected + what actually happens step-by-step
- [[qwen3.6-27b]] — the model: specs, benchmarks, the "≈ Opus 4.5" claim decoded
- [[mlx-runtime]] — Apple MLX: what it is, the real speedup, and why it converges with llama.cpp at 27B
- [[lm-studio]] — LM Studio: OpenAI server, developer tab, max concurrency, KV-cache quantization, LM Link
- [[opencode-local-provider]] — opencode: pointing it at a local endpoint (the `modalities` correction)
- [[locally-ai-lm-link]] — Locally AI (acquired by LM Studio Apr 2026) + Apple Foundation Models
- [[hardware-economics-and-tco]] — what it really costs: quant/VRAM table, capex, break-even, "free" decoded
- [[privacy-data-residency]] — **the killer app**: local inference = strongest PII/data-residency posture (the hireui angle)
- [[claims-scorecard]] — all 14 video claims graded (0 fabricated / 0 false)
- [[source-provenance]] — provenance, verification record, and the Haiku-confabulation corrections

## Pilot menu (apply it to real work)

The operator-facing "many methods to apply this to hireui" deliverable lives in **[../../output/(C) 2026-07-11-local-ai-coding-pilot-menu.md](../../output/(C)%202026-07-11-local-ai-coding-pilot-menu.md)** — 13 ranked methods across 4 tiers (try-it-this-week → hireui first-LLM-feature → harness → cost/compliance instrumentation).

## Why this matters for Storm Bear

Two standing threads converge here:
- **Cost-optimization** — local inference = **$0 marginal cost** for cheap/bulk tasks (sibling to [[../claude-api-cost-optimization/_index|claude-api-cost-optimization]] model-tiering + free-claude-code proxy). But "free" hides ~$4K hardware capex — the honest framing is *high-capex / zero-marginal-cost*.
- **Data-residency / privacy** — local inference = candidate PII **never leaves the machine** = the strongest possible GDPR/PDPL/EU-AI-Act posture for a recruitment SaaS. See [[privacy-data-residency]].

## Cross-links to existing corpus

- [[../cowork-third-party-inference/setup-local-ollama|cowork-third-party-inference: local Ollama setup]] — the Claude-Cowork sibling of this stack (local + private, Ollama instead of LM Studio)
- [[../graphify-codebase-graph/opencode-integration|graphify: opencode integration]] — deeper opencode config (AGENTS.md, opencode.json, plugins)
- [[../claude-code-clones/_index|claude-code-clones]] — opencode is one of the named Claude Code clones
- [[../claude-api-cost-optimization/_index|claude-api-cost-optimization]] — model-tiering / the "cheap model for cheap tasks" discipline
