# Hardware, economics & TCO — decoding "I didn't pay for anything"

> Verified in the [[source-provenance|economics-privacy + presenter dives]] + main-loop anchors. Numbers are approximate mid-2026 and vary by market.

## What it takes to run Qwen3.6-27B (C5, C11)

**VRAM / unified memory needed = model weights + KV cache (grows with context) + OS headroom.**

| Quant | Model size | Comfortable machine |
|---|---|---|
| Q4_K_M | ~16.8 GB | 24 GB+ VRAM / unified memory |
| Q5_K_M | ~19.5 GB | 24–32 GB |
| Q6_K | ~22.5 GB | 32 GB+ |
| Q8_0 | ~28.6 GB | 36 GB+ |

- **Beto's 18 GB MacBook could NOT run it** — correct: 16.8 GB weights + KV cache + macOS won't fit in 18 GB. **His 96 GB M3 Ultra Mac Studio runs it comfortably.** ✅ (C11 plausible.)
- **KV cache is the hidden cost:** at large context it can add **tens of GB** on top of the weights. This is why 24 GB is a *practical minimum*, not a ceiling.

### Minimum-viable specs

| Path | Min-viable | Cost (approx) |
|---|---|---|
| **Apple (unified memory)** | Mac with **≥24 GB** unified memory (32 GB+ comfortable) | M-series with 24–36 GB: ~$1,600–2,500 |
| **Beto's actual rig** | M3 Ultra Mac Studio, 96 GB | **$3,999** |
| **NVIDIA (VRAM)** | Beto says "≥RTX 4090"; realistically a **16 GB** RTX 4080 / 5070 Ti runs Q4 (he over-specs) | 16 GB cards ~$800–1,200; RTX 4090 24 GB ~$1,800–3,500 |

> C5 is **CORRECT-BUT-INCOMPLETE:** the RTX 4090 works but is over-specced for Q4; cheaper 16 GB cards run it, and 24 GB is really the *practical* floor once you add context.

## The "free" claim, decoded (C12)

Beto: *"I didn't pay for anything … cancel ChatGPT, keep Claude for complex work, use the local model for simple things."*

**Verdict: OVERSIMPLIFIED.** "Free" hides four real costs:

1. **Hardware capex** — ~$1,600–4,000 up front (he admits the 18 GB laptop failed, so the box is *mandatory*).
2. **Electricity** — a Mac Studio draws ~30–80 W under load; an RTX 4090 rig 300–400 W. Roughly **$30–200/yr** depending on load and rates.
3. **Latency** — the hard task took **~10 minutes** vs seconds on a cloud frontier model. Developer-time cost is real.
4. **Quality gap** — a 4-bit local quant is below the benchmarked full model, which is itself a bit behind Opus and *3 generations* behind today's Opus 4.8.

Also self-contradictory: he says *"keep the Claude subscription"* — so cost is **not** zero.

### The honest framing: **high-capex, zero-marginal-cost**

| Model | Cost shape |
|---|---|
| Cloud API (Claude/OpenAI) | $0 upfront, **$ per token** forever |
| Local | **$$$ upfront hardware**, ~$0 per token after |

**Break-even** (independent 2026 analyses): local pays off once cloud spend exceeds roughly **$80–100/month**, with a **~7–24-month payback** on the hardware. Below that, local is a *worse* deal on pure cost — you buy it for **privacy/offline**, not savings.

## But the tiered-routing insight is SOUND

The *strategy* underneath the theater is correct and is the [[../claude-api-cost-optimization/_index|model-tiering]] discipline:

- **Cheap/bulk/mechanical** (refactor, rename, dedup, boilerplate, bulk parse) → **local, $0 marginal**.
- **Hard/nuanced/customer-facing** → **cloud frontier**.
- Route **deterministically in code** (Rule 5: code routes, model judges) — not with an LLM.

## Takeaways
- Budget for the box: **≥24 GB** memory, ~$1,600–4,000. There is no "free."
- Local is a **capex-for-opex swap** — justified by **volume** (high API spend) or **privacy/offline** (see [[privacy-data-residency]]), not by small-scale savings.
- Keep the tiered-routing takeaway; drop the "free" framing.

## See also
[[qwen3.6-27b]] · [[privacy-data-residency]] · [[claims-scorecard]] · [[../claude-api-cost-optimization/_index|claude-api-cost-optimization]]
