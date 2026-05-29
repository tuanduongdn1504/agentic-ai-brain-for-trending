# Sana — Wiki (v116)

> `NVlabs/Sana` · **"SANA: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer."** · NVIDIA Labs' efficiency-oriented framework for high-resolution text-to-image (and now text-to-video / world-model) generation built on a linear Diffusion Transformer + a 32× deep-compression autoencoder + a decoder-only LLM text encoder. Generates 4K images in ~20 s and runs on an 8 GB consumer GPU via 4-bit quantization.

**(C) Claude-generated wiki page.** Fetched 2026-05-29 (GitHub API + README). Routine v2.4, wiki #116. **⚠️ Built under the 2nd operator-elected Phase 0.9 OVERRIDE in corpus history — STRICT verdict was 0/4 SKIP (out of corpus scope). See the OVERRIDE verdict doc in `01 Analysis/`.**

---

## Identity

| Field | Value |
|---|---|
| Repo | [`NVlabs/Sana`](https://github.com/NVlabs/Sana) |
| What | **Efficient high-resolution image/video generation framework** (linear DiT) |
| Tier / archetype | **Corpus-outlier** — does NOT fit the agent-centric T1–T5 taxonomy. Closest = T5 Application (research model + training/inference framework). **CORPUS-FIRST pure generative-vision research model.** |
| Stars / forks | **7,919★ / 607 forks** (fork_ratio **0.077**) |
| Watchers / open issues | 95 subscribers / **123 open** |
| Created / pushed | 2024-10-11 / 2026-05-28 (**~595 days / ~1.6 yr** old at fetch) |
| Velocity | **~13.3 stars/day → sustained-low, NOT a Pattern #52 instance** (below all sub-class floors; profile like v100 Easydict ~10.3/d — a long-lived steady-accrual repo, not a viral pulse) |
| License | **Apache-2.0** (code; GitHub API agrees). **Model weights are licensed separately** on Hugging Face per-collection — a code-vs-weights license boundary. |
| Language | **Python** (~93.5%) |
| Distribution | `git clone` + `environment_setup.sh`; HF **Diffusers** (`SanaPipeline`, diffusers ≥ 0.32); community **ComfyUI** nodes; **SGLang** serving with an **OpenAI-compatible API**; Replicate |
| Default branch / homepage | `main` / nvlabs.github.io/Sana/docs/ |
| Author | **NVIDIA Labs** (`owner.type: Organization`) — research division of NVIDIA Corp (US). Algorithm work co-credited to **MIT Han Lab (Song Han)** and **Tsinghua**. |
| Topics | diffusion, dit, linear-transformer, nvfp4, pytorch, reinforcement-learning, text-to-image, text-to-video, video-generation, world-models |

## What it is

SANA is a research-grade, efficiency-first generative-vision stack. The headline pitch: image quality competitive with much larger diffusion models, at a fraction of the parameters and latency. Per the README: *"20× smaller and 100× faster than Flux-12B"* — Sana-1.6B renders a 1024×1024 image in ~1.2 s vs FLUX-dev's ~23 s, generates 4096×4096 in ~20 s, and (with 4-bit SVDQuant/Nunchaku quantization) runs inside **8 GB of VRAM**.

It is **not** an agent, a coding tool, a Claude-Code skill, or anything in the agentskills.io ecosystem. It is a peer-reviewed ML model family with a strong publication record (ICLR 2025 Oral, ICML 2025, ICCV 2025 Highlight, ICLR 2026 Oral). It lands in this corpus only by an explicit operator override (below).

## Core architecture (the genuinely instructive part)

Four efficiency ideas carry the work:

1. **DC-AE — Deep Compression Autoencoder (32×).** Compresses images 32× into latent space vs the conventional 8×, cutting the number of latent tokens the transformer must process by ~16× at a given resolution. This is the single biggest lever for high-resolution speed.
2. **Linear Diffusion Transformer.** Replaces quadratic self-attention in the DiT with **linear attention** (+ a Mix-FFN), so cost scales ~linearly with token count — essential once you're at 4K.
3. **Decoder-only LLM text encoder.** Uses a modern decoder-only LLM (Gemma-family) with in-context-learning prompting instead of the usual T5/CLIP encoder, for better prompt adherence. *(This is the one thin thread to the LLM world the corpus otherwise tracks — but it's an internal component choice, not an agent surface.)*
4. **Few-step sampling.** Flow-DPM-Solver + sCM continuous-time consistency distillation (Sana-Sprint) push toward one/few-step generation.

## Model family

| Variant | Params | What |
|---|---|---|
| SANA | 0.6B / 1.6B | base text-to-image |
| SANA-1.5 | 1.6B / 4.8B | scaling + train/inference-time compute optimization (ICML 2025) |
| SANA-Sprint | — | few-step distilled generator (ICCV 2025 Highlight) |
| SANA-Video / LongSANA | 2B | text-to-video to 720p; "27 FPS real-time minute-length" (ICLR 2026 Oral) |
| SANA-WM | 2.6B | world model with 6-DoF camera control |
| Sol-RL | — | RL post-training framework ("4.64× faster convergence") |

## Quantitative-marketing surface (Pattern #82)

The README header is dense with comparative claims: *20× smaller · 100× faster than Flux-12B · 23.3× speedup · 4K in 20 s · 2K in 4 s · runs in 8 GB VRAM · VBench 84.05 · GenEval 0.82 · FID 5.70.* Textbook **Pattern #82 quantitative-marketing** — the one pattern this subject exhibits cleanly, because #82 is domain-agnostic (it's about how repos *present* themselves, not what they do).

## Why it's in the corpus (and the honest caveat)

It's here because the operator chose to override the include/skip gate. The disciplined verdict was **SKIP**:

- **(a)** NVIDIA Labs is a US mega-corporation research division — not a cultural peer, not a foundational vendor the vault depends on. **FAIL.**
- **(b)** Zero relevance to the documented #1 goal ("master Claude and autonomous agents for software development"); high cost-of-trial (needs a GPU); not a vault tool. **FAIL.**
- **(c)** Genuinely well-engineered and instructive — *in efficient generative vision*, a different field. Teaches nothing about the agent/skill methodology the Pattern Library tracks. **WEAK.**
- **(d)** No agentskills.io chain, no Karpathy lineage, no Claude adjacency. Only tangential threads (decoder-only LLM text encoder; SGLang OpenAI-compatible serving; MIT Han Lab quantization). **FAIL.**

→ **0/4 clear PASS → STRICT SKIP → operator OVERRIDE INCLUDE** (2nd in corpus history after v84 image-blaster). Treat this page as corpus-knowledge-of-an-outlier, not as a vault pilot or a goal-aligned subject.

## Honest non-claims

- **NOT** an agent / skill / Claude-Code artifact in any form.
- **NOT** a Pattern #52 velocity instance (sustained-low ~13/d).
- **NO** new top-level Pattern; **NO** Pattern Library state change. (Out of scope → contributes nothing to the agent/skill pattern corpus.)
- The only real Pattern observations are domain-agnostic: **#82 quantitative-marketing** (STRONG) and a thin **#45 code-vs-weights license boundary** + **#18 B3 OpenAI-compatible-API** (both tangential N+1).

---

*See `01 Analysis/(C) Phase-0-and-0.9-OVERRIDE-verdict.md` for the full gate decision and `01 Analysis/(C) Pattern-Library-Phase-4b-2nd-override-observation.md` for the (deliberately thin) Pattern Library contribution.*
