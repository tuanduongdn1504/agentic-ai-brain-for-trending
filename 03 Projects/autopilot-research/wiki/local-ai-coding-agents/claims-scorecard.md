# Claims scorecard — all 14 claims graded

> Grades reconciled in the main loop from the [[source-provenance|17-agent workflow]] + independent anchors. Where Haiku agents confabulated, the anchor wins (noted).
> **Legend:** ✅ CONFIRMED · ◐ CORRECT-BUT-INCOMPLETE · ⚠️ OVERSIMPLIFIED/SPECULATIVE · ❌ FALSE/FABRICATED

| # | Claim (paraphrased) | Grade | One-line verdict |
|---|---|---|---|
| C1 | Qwen3.6-27B: agentic-coding, multimodal, low-VRAM, runs offline | ✅ | Real dense 27B, Apache-2.0, vision, offline. [[qwen3.6-27b]] |
| C2 | "Announced April 21" | ◐ | Off by one day — actually **2026-04-22**. |
| C3 | Surpasses Qwen3.5 flagship; fully open-source | ✅ | Beats Qwen3.5-397B on SWE/Terminal/Skills bench; Apache-2.0. |
| C4 | ≈ Opus 4.5 for agentic coding, "a bit worse" | ◐ | **Directionally right**: Terminal-Bench tied 59.3; SWE-bench 77.2 vs **80.9**. Incomplete: it's a 4-bit quant vs a 3-gen-old Opus. [[qwen3.6-27b]] |
| C5 | Non-Mac needs ≥RTX 4090 / ≥16 GB (rec 24) | ◐ | Works but over-specs; 16 GB 4080/5070Ti run Q4; 24 GB is the practical floor. [[hardware-economics-and-tco]] |
| C6 | MLX makes it "more reliable than ever" + faster | ⚠️ | Runtime ≠ reliability; speedup **converges with llama.cpp at 27B**. [[mlx-runtime]] |
| C7 | LM Studio: OpenAI server, dev tab, max concurrency, KV-cache quant | ✅ | All confirmed against LM Studio docs. [[lm-studio]] |
| C8 | opencode local via JSON; "pass **modalities**" for vision; subagents; 31 tool calls | ◐ | baseURL ✓, subagents ✓, 31-calls plausible — but **no `modalities` setting exists** (vision = drag-drop). [[opencode-local-provider]] |
| C9 | "Locally AI from LM Studio" + phone chat while computer sleeps | ◐ | Acquired Apr-8-2026 ✓; LM Link phone↔desktop ✓; **"sleeping" dubious**. [[locally-ai-lm-link]] |
| C10 | Qwen3.6 vision named SF Symbols locally | ✅ | Plausible + strong V* score; local multimodal genuinely works. |
| C11 | ~10 min/fans; 18 GB MacBook fails, 96 GB works | ✅ | Memory math checks out; latency honest. [[hardware-economics-and-tco]] |
| C12 | "Didn't pay for anything"; cancel ChatGPT, keep Claude, local for simple | ⚠️ | "Free" ignores ~$4K capex + latency + quality gap; **but tiered-routing is sound**. [[hardware-economics-and-tco]] |
| C13 | Apple Foundation in Locally AI; new Macs "this year" for local LLMs | ⚠️ | Foundation Models real; integration unconfirmed; new-Macs = speculation. [[locally-ai-lm-link]] |
| C14 | Download "~20 GB" | ✅ | Q4 16.8 / Q5-Q6 ~19.5–22.5 GB — fair round number. |

## Tally

- ✅ CONFIRMED: **6** (C1, C3, C7, C10, C11, C14)
- ◐ CORRECT-BUT-INCOMPLETE: **5** (C2, C4, C5, C8, C9)
- ⚠️ OVERSIMPLIFIED/SPECULATIVE: **3** (C6, C12, C13)
- ❌ FALSE / FABRICATED: **0**

## Reading of the video

**High-integrity.** Zero fabrications, zero outright-false claims. The toolchain is real, reproducible, and does what's shown. The failure mode is **enthusiasm-over-claim** on three points — *"more reliable"* (C6), *"free"* (C12), *"new Macs coming"* (C13) — plus **one concrete config error** (C8 `modalities`). The headline — *"Local AI Coding Agents Are Finally Good Enough"* — is **defensible**.

**Contrast:** unlike the [[../jasonlee-claude-mobile-app/_index|Jason Lee "$80K/Mo" video]] (where the business framing was theater), Beto's economics are modest and honest (his real app **Inkigo** earns ~$650/mo), and he repeatedly hedges ("not going to replace the latest Opus"). The one thing to strip is the **"free"** framing; keep everything else. See [[source-provenance]] for the presenter assessment.

## See also
[[_index]] · [[source-provenance]] · [[overview]]
