# Qwen3.6-27B — the model at the center

> **First-party:** Alibaba Qwen team ([qwenlm.github.io/blog](https://qwenlm.github.io/blog/), [huggingface.co/Qwen](https://huggingface.co/Qwen)). Benchmarks cross-checked in the main loop against independent sources ([Vellum](https://www.vellum.ai/blog/claude-opus-4-5-benchmarks), Qwen model card, [MarkTechPost](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/)).

## What it is

- **Released 2026-04-22** by Alibaba's Qwen team. (Video says "April 21" — off by one day.)
- **Dense 27-billion-parameter** open-weight model. Notable: a *dense 27B* that beats the previous-gen *397B Mixture-of-Experts* flagship (Qwen3.5-397B-A17B) on coding — small model, flagship results.
- **Apache-2.0** license (genuinely, fully open — you can self-host commercially).
- **Natively multimodal** (vision) + **hybrid-thinking** (reasoning) + **tool-calling**.
- **Native 262,144-token context**, extensible to ~1M.
- **Quantized sizes** (what you actually download): Q4_K_M ≈ **16.8 GB**, Q5_K_M ≈ 19.5 GB, Q6_K ≈ 22.5 GB, Q8_0 ≈ 28.6 GB. ([[hardware-economics-and-tco]].)

## Published benchmarks (the FULL model)

| Benchmark | Qwen3.6-27B | Beats prior Qwen3.5-397B |
|---|---|---|
| SWE-bench Verified | **77.2** | 76.2 |
| Terminal-Bench | **59.3** | 52.5 |
| SkillsBench | **48.2** | 30.0 |
| Multimodal (V*) | **94.7** | — |
| MMMU | 82.9 | — |
| AndroidWorld (GUI agent) | 70.3 | — |

## The "basically the same as Opus 4.5" claim, decoded (C4)

Beto shows a benchmark chart and says: *"for agentic terminal you can compare this to basically Opus 4.5 … it's literally the same value … a bit worse than 4.5."* Independent anchor (main loop):

| Benchmark | Qwen3.6-27B | **Claude Opus 4.5** |
|---|---|---|
| **Terminal-Bench** (agentic terminal) | 59.3 | **59.3** ← *literally tied* |
| **SWE-bench Verified** | 77.2 | **80.9** ← Qwen ~3.7 pts lower ("a bit worse") |

**Verdict: CORRECT-BUT-INCOMPLETE — and more right than wrong.** On the specific benchmark Beto names (agentic terminal), Qwen3.6 *ties* Opus 4.5 at 59.3; on SWE-bench it's a bit behind. His directional claim holds. **The three things he leaves out:**

1. **He runs a ~4-bit LOCAL QUANT, not the full model.** Benchmark scores are for the full-precision model with an optimal harness. Quantization + a local agent loop degrade quality below these numbers — so "the thing on your Mac" is *worse* than "the model in the benchmark table."
2. **Opus 4.5 is ~3 generations old.** The current frontier is **Opus 4.8** (via 4.6 Feb-2026, then 4.7). Parity with a months-old Opus ≠ parity with today's Opus. He is honest that "it's not going to replace the latest Opus."
3. **Real-world gap shows in his own demo:** it "trips" on complex mobile-app code (imports things that don't exist), and the hard task took ~10 minutes. Benchmark parity ≠ production parity.

> **Correction logged (fail-loud):** a Haiku dive agent claimed *"no evidence Claude Opus 4.5 exists"* and marked C4 UNVERIFIABLE. **That is wrong** — Opus 4.5 is a real, released model (Anthropic "Introducing Claude Opus 4.5"; SWE-bench 80.9). Overridden with the anchor above. See [[source-provenance]].

## Vision + tool-calling (C10)

- Correctly named the **SF Symbols** in a pasted screenshot — plausible and confirmed by the strong V*/MMStar scores. **Local multimodal genuinely works.** This is the seed for local **CV/receipt image parsing** with zero data egress ([[privacy-data-residency]] + the pilot menu).

## Takeaways

- A dense 27B that ties a recent frontier model on agentic-terminal benchmarks is a genuine step-change for *local* coding.
- Treat published scores as a **ceiling**; the local 4-bit quant you run is below it.
- The right mental model: **"a very capable last-generation frontier model that runs on your desk for free-after-hardware"** — not "Opus at home."

## See also

- [[mlx-runtime]] — the runtime that executes it · [[lm-studio]] — the host · [[opencode-local-provider]] — the agent
- [[../miai-cv-matching-agent/_index|miai-cv-matching-agent]] — CV↔job matching (the domain hireui cares about; SWE-bench ≠ recruitment quality)
