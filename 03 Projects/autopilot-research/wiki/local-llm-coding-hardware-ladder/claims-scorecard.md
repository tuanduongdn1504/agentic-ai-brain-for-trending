# Claims scorecard

> 21 checkable claims graded. Verification: Workflow **`wf_9dd08c75-e02`** (24 agents — 6 grouped verifiers + 17 refute-first adversarial passes + 1 completeness critic; 1,409,555 tokens, 387 tool calls, **0 errors / 0 empty / 0 skipped**), plus **7 main-loop checks by Opus** where the agents were wrong or incomplete.
>
> **Totals: 12 CONFIRMED · 5 CORRECT-BUT-INCOMPLETE · 1 FALSE · 3 UNRESOLVED · 0 FABRICATED.**

## Verdicts

| ID | Claim | Source | Verdict | Note |
|---|---|---|---|---|
| C1 | LM Studio exposes an Anthropic-compatible endpoint alongside an OpenAI one | Zen van Riel | **CBI** | Capability confirmed in LM Studio docs ("Anthropic-compatible endpoints", Messages API). The literal path `/v1/messages` is **not** stated in the fetched primary docs. |
| C2 | Claude Code redirects to a local server via `ANTHROPIC_BASE_URL` + auth env var | anchor, Zen | **CONFIRMED** | `ANTHROPIC_BASE_URL` plus `ANTHROPIC_AUTH_TOKEN` (bearer) **or** `ANTHROPIC_API_KEY` (x-api-key). [code.claude.com/docs/en/llm-gateway-connect](https://code.claude.com/docs/en/llm-gateway-connect) |
| C3 | **OMLX** exists: MLX-based macOS server, two-tier SSD-persistent KV cache | WEBdoze, Gregory | **CONFIRMED** | [github.com/jundot/omlx](https://github.com/jundot/omlx). Apache-2.0, solo maintainer. Verified across 8 sub-claims incl. safetensors cold tier, restart persistence, OpenAI+Anthropic APIs, `localhost:8000`. All 7 refutation passes upheld it. |
| C4 | Qwen3.6 max context = 262,144 tokens | Gregory, Tim | **CONFIRMED** | ⚠️ **Agent error caught.** The verifier returned UNRESOLVED claiming *"no Qwen3.6 model exists."* False — see [[caveats-and-corrections]]. Qwen3.6-27B released **2026-04-22**, Apache-2.0, dense, **262K native, extensible to 1M**. |
| C5 | LM Studio's default context (~4,000) is small enough that Claude Code's system prompt alone overruns it | Zen, Gregory | **CBI** | **Claude Code's system prompt = 4,200 tokens** — confirmed, [code.claude.com/docs/en/context-window](https://code.claude.com/docs/en/context-window). LM Studio's *default* window not found in primary docs. Mechanism sound, one half unverified. |
| C6a | RTX 4090 memory bandwidth = 1,008 GB/s | Tim | **CONFIRMED** | 384-bit bus × 21 Gb/s ÷ 8 = 1,008. Refuter reproduced the arithmetic. |
| C6b | M4 Max memory bandwidth = 546 GB/s | Tim | **CBI** | True for the **40-core-GPU** M4 Max only; the **32-core** variant is **410 GB/s**. Quoted without the qualifier. Refuter also flagged that only a secondary source was reached. |
| C7a | ~75–80% of Apple unified memory is usable for model work | Tim | **UNRESOLVED** | No Apple primary source found stating any such figure. Treat as folk wisdom. |
| C7b | Apple documents a default max working set (`iogpu.wired_limit_mb`) | — | **UNRESOLVED** | Wired-memory limits are real in Metal/macOS; the documented default value was not located. |
| C8 | Warp open-sourced **its entire codebase** | ForrestKnight | **CBI** | Announced **2026-04-28**; **client only** ([github.com/warpdotdev/warp](https://github.com/warpdotdev/warp)), **AGPL-3.0** (UI crates MIT). **Oz, the cloud agent-orchestration platform, remains proprietary.** "Entire code base" is an overstatement. ⚠️ AGPL — see [[caveats-and-corrections]]. |
| C9 | Qwen3 Coder Next ≈ 80 B MoE, ~3 B active | ForrestKnight, Tim | **CONFIRMED** | HF model card: **80 B total / 3 B activated**, 512 experts / 10 activated per token, **262,144 native context**. Refuter upheld. |
| C10 | Ollama now ships a GUI **and** a hosted cloud tier including Kimi K3 | anchor | **CONFIRMED** | GUI DMG on the download page; **Ollama Cloud Pro $20/mo, Max $100/mo**; Kimi K3 at **$3.00 in / $0.30 cached in / $15.00 out** per 1M. Refuter upheld. |
| C11 | Ollama publishes integrations for Claude Code / OpenCode / **Codex / Copilot / Xcode** | anchor | **FALSE** | The integrations index lists **Claude Code · OpenCode · DeepSeek Harness · OpenClaw · Hermes Agent · VS Code**. Codex, Copilot and Xcode are **absent**. |
| C12 | A 1-bit Kimi K3 quant totals ≈ 610–665 GB | anchor | **CONFIRMED** | Unsloth's published table: **Dynamic 1-bit S = 610 GB**, **1-bit M = 665 GB** combined RAM+VRAM. Exact match. |
| C13 | VRAM ladder 8→7B · 12–16→14B · 24→32B · 64+→70B | Tim | **CBI** | Only holds under aggressive (~4-bit) quantization, which he never states. At FP16 a 7 B model needs ~14 GB. And it is a **chat** ladder — agentic context pushes every rung up. |
| C14 | Claude Code warns on unrecognized models, affecting auto-compact | anchor | **CONFIRMED** | Docs: rejects unknown IDs; sessions on an unrecognized ID *"compact at the context window Claude Code assumes for the ID"*; `CLAUDE_CODE_MAX_CONTEXT_TOKENS` overrides. |
| C16 | Qwen3.5 exists with a ~1M context window | anchor | **CONFIRMED** | Qwen3.5-9B card: *"262,144 natively and extensible up to 1,010,000 tokens."* ⚠️ The first-pass verifier denied Qwen3.5 existed; its own refuter overturned it. |
| C17 | Apple: M5 neural accelerators = 4× matmul vs M4, ≈ prompt-processing speedup | Apple (WWDC26 s232) | **CONFIRMED** | First-party vendor statement, on the record. |
| C18 | Apple: Ollama, LM Studio and vLLM are built on MLX | Apple (WWDC26 s232) | **CONFIRMED** | First-party. *"Chances are you are already running on MLX."* |
| C19 | Apple: latest DeepSeek model = 1.6 T params, >800 GB for weights | Apple (WWDC26 s232) | **CONFIRMED** | First-party, as stated on the record. Not independently re-derived here. |
| C20 | The anchor's "Mac mini M4, 64 GB" is a **base M4** | anchor (implied) | **FALSE→corrected** | Base M4 addresses a **maximum of 32 GB**. A 64 GB Mac mini is necessarily **M4 Pro** — 273 GB/s, not 120 GB/s. Main-loop correction; see [[the-hardware-ladder]]. |

## Recorded as testimony, not fact

Single-operator observations, unverifiable by design. Cite with attribution, never as measurements:

- The anchor's **2 min 45 s** cold start; thermal/acoustic behaviour; the iCloud/Music access prompt
- WEBdoze's **70 → 20 → 18 tok/s** decay and the 20-minute stall
- ForrestKnight's **47 compile errors** and **"at least 5× longer"**
- Samuel Gregory's **36 GB model → ~80 GB RAM**
- Tech With Tim's 25-second response and the non-loading chess game
- All token/sec figures throughout (every source was screen-recording, which they repeatedly note degraded their own results)

## Reading of the scorecard

**Zero fabrications, one FALSE.** The single FALSE is the anchor mis-reading a list off-screen — the failure mode his [[../quanit-becoming-ai-engineer-2026/caveats-and-corrections|prior wiki]] already predicted (specific details overstated, verdicts sound).

**The CBI cluster is the real signal.** C6b, C8, C13 and C5 are all the same shape: **a true statement with its qualifier dropped.** 546 GB/s (which M4 Max?), "entire codebase" (which half?), the VRAM ladder (at what quantization?). This is the dominant error mode of the genre — not lying, but stripping the condition that makes the number mean something.

**Both UNRESOLVEDs are Apple memory-management internals.** Nobody in the bundle sourced them, and neither could we.

## See also
[[caveats-and-corrections]] · [[the-hardware-ladder]] · [[source-provenance]] · [[quality-ceiling-and-failure-modes]]
