# Locally AI + LM Link + Apple Foundation Models

> **First-party:** [LM Studio blog — "Locally AI joins LM Studio"](https://lmstudio.ai/blog/locally-ai-joins-lm-studio), [LM Link docs](https://lmstudio.ai/docs/lmlink), [Apple Foundation Models](https://developer.apple.com/machine-learning/). Verified in the [[source-provenance|Locally-AI dive]] + a main-loop anchor search.

## Locally AI — and the acquisition (a garble-guard win)

- **Locally AI** is an elegant iOS/iPadOS/macOS app to run AI models **on-device** (via **Apple MLX**), built by independent developer **Adrien Grondin**.
- **LM Studio acquired Locally AI on 2026-04-08**; Grondin joined LM Studio to lead native mobile AI.
- So Beto's *"Locally AI which is from LM Studio"* is **CORRECT — but only recently** (post-acquisition). A training-cutoff-bounded skeptic would wrongly call this false ("it's Adrien Grondin's app"). This is a **[[source-provenance|discard-as-garble-guard]] win**: a fresh true acquisition looks exactly like a confabulation.

## LM Link (C9)

- **LM Link** = an LM Studio feature to reach a model running on **powerful hardware** (your desktop) from a **lightweight device** (laptop, or iPhone via the **Locally** app).
- Uses **Tailscale** for a secure, **end-to-end-encrypted** device-to-device connection. Announced ~2026-06-04.
- ⚠️ **"Computer can be sleeping"** — the dubious sub-claim. Standard macOS sleep drops the network; remote access needs the host awake (or Power-Nap/wake-on-LAN tricks). No docs support chatting to a sleeping Mac. **Verify empirically before building an overnight-batch workflow on it** (pilot method — see the "sleep-mode inference window" idea, flagged HIGH-RISK).

## Apple Foundation Models (C13)

- **Apple Foundation Models** is Apple's framework exposing an **on-device** (~3B) model + a Private Cloud Compute path, via a Swift API — the engine behind Apple Intelligence.
- Beto says you can pick "Apple Foundation or Qwen3.6" in Locally AI. **Locally AI ↔ Foundation Models integration is unconfirmed** in the acquisition/first-party docs (roadmap-plausible, not documented). Treat as **OVERSIMPLIFIED**.
- **"Apple set to announce new Macs this year optimized for local LLMs"** = **speculation.** Apple's developer materials feature *software* directions ("Run local agentic AI on the Mac using MLX," a "Core AI" framework per agent reports), but there is **no first-party hardware announcement** of Macs "optimized for local LLMs." Do not treat as fact. *(These WWDC/Core-AI specifics are post-cutoff and agent-reported; low confidence.)*

## Why it matters for the operator

- The mobile angle (phone → desktop model) is a **novelty**, not a product primitive for hireui.
- **The load-bearing fact is the Apple-Foundation-Models on-device path**: if a recruiter's *existing* Mac can run a good-enough on-device model, that's **local inference with zero extra hardware** — a real (if future/uncertain) route to the data-residency posture in [[privacy-data-residency]]. Watch it; don't bet on it yet.

## Takeaways
- Locally AI **is** now an LM Studio product (since Apr 2026) — Beto is right.
- LM Link (phone↔desktop over Tailscale) is real; **sleep-mode chat is unverified**.
- Apple Foundation Models is real; its integration into Locally AI and any "new Macs" claim are **not** established — keep as watch-items.

## See also
[[lm-studio]] · [[mlx-runtime]] · [[privacy-data-residency]] · [[source-provenance]]
