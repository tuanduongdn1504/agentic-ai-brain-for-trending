# Open-weights reality — the headline correction

The video's single most-repeated claim is that K3 is **open source — "the weights will be open for anyone to download," "you can pretty much do whatever you want."** This is the equivalent of the corpus' other headline corrections (cf. the AWS "SQS rate-limits for you" error): **it is false at video time.**

## What was actually true on 2026-07-17 (COR1 / FALSE, UPHELD high)

- As of the video date, **Kimi K3 weights were NOT downloadable.** Moonshot's HuggingFace organization listed **only K2-series** models — **no K3 checkpoint**.
- K3 launched as a **hosted service only**: Kimi app, Playground, Kimi API, Kimi Code, Kimi Work.
- Open weights were **promised for 2026-07-27** (~11 days after launch) under a **"Modified MIT"** license, alongside a technical report covering architecture/training/evals.
- So at video time K3 was an **announced open-weight model, not an available one.** "Download the weights and do whatever" described a **future** capability as a **present** one.

## Even after July 27, "do whatever you want" is oversimplified

1. **License caveats.** K3 will likely follow the K2 precedent — Modified MIT that **permits commercial use but adds a monthly-active-user (MAU) clause** for large commercial deployments. Full terms weren't published at launch; "do whatever" is not accurate for big deployments.
2. **The 2.8T hardware wall.** Self-hosting is out of reach for almost everyone:
   - Quantized: **~650 GB–1 TB** combined memory. Full precision: **~1.7 TB**.
   - A top consumer GPU (RTX 6000 Pro, 96 GB) is **~12× short**. Practical inference needs **8–16 H100-class GPUs (~$150K–$300K)** plus infrastructure.
   - Moonshot's own guidance points to **supernode configs (64+ accelerators)**.
3. **Ecosystem lag.** `llama.cpp` / Ollama / LM Studio support arrives **weeks-to-months after** a weight drop. Practical local use of a 2.8T model is a **months-out** proposition even for well-resourced teams, and likely only via **quantized/distilled variants**.

## Why this matters

- For a viewer, the gap between "open, download it today" and "hosted-only, weights in 11 days, and you can't run it anyway" is the difference between a usable plan and a dead end.
- For the operator's **data-residency** calculus specifically: "open weights → self-host in the EU" is the *only* path that would soften K3's residency problem — and this section shows that path is **blocked for months** by hardware + tooling, even after July 27. See [[hireui-translation]].

## Key Takeaways

- **Hosted-only at launch. Weights promised July 27. Not self-hostable in practice for months.**
- The video's "open source, do whatever" is the clearest false-framing in the piece — it conflates *announced* with *available* and *licensed-open* with *runnable*.
- The checkable moment is **July 27**: weights + technical report. Until then, treat every "open" claim as a forward promise.
