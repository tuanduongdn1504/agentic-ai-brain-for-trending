# (C) Phase 4b PRIMARY — NEW Library-vocab "Own-Trained Bundled Expert Language Model at Single-Subject Solo-Founder Scale" PROVISIONAL N=1 registration

**Wiki**: v97 distill (samuelfaj)
**Routine**: v2.3.1 (FIRST execution under v2.3.1)
**Phase 4b vehicle**: #7 Library-vocab observational-layer registration (per routine v2.3 §3)
**Verdict**: REGISTER PROVISIONAL N=1 at observational layer
**Confidence**: HIGH at single-subject scope; promotion-eligibility deferred to N=2 emergence

---

## Definition

A corpus subject that ships its own fine-tuned LLM as the runtime substrate for its product, where:

1. The model is **fine-tuned by the subject's author** (not just bundled via 3rd-party reuse).
2. The model is **distributed via Hugging Face** (or equivalent public model registry) with explicit attribution.
3. The model is **bundled with or auto-downloaded by** the product on install or first-run.
4. The model substitutes for cloud-LLM dependency at the runtime layer.
5. The subject is at **solo-founder scale** (not foundational-vendor scale).

## Anchor evidence at v97

**`samuelfaj/distill`** ships **`samuelfaj/distill-1.7B-MLX`** (1.7B parameters, 4-bit quantization, MLX framework for Apple Silicon Metal) as the default runtime model:

```
## Our Model

Distill uses it's own Expert Language Model

https://huggingface.co/samuelfaj/distill-1.7B-MLX

Only: 1.7B - 4bit

Safe recommendation: machine should have 8 GB+ RAM; 16 GB+ is comfortable.
```

Cross-evidence:
- Hugging Face account `samuelfaj` distinct from cloud LLM vendor
- Model size 1.7B 4-bit = consumer-grade local inference
- MLX = Apple Silicon Metal native framework (hardware-substrate-pinned)
- README declares the model as the product's own ("its own Expert Language Model")

## Distinct from prior corpus observations

| Prior corpus mechanism | Distinction from this Library-vocab |
|---|---|
| BYOK (operator brings their own API key) | Operator runs subject's model locally; no cloud call |
| Zero-API-Key via Reuse-of-Logged-In-Agent-Session (v91 html-anything) | Operator does not reuse another agent's session; subject's model is independent runtime |
| Multi-Vendor BYOK at Asset-Generation Layer (v84 OVERRIDE-provenance, retired at v96) | v84 BYOK was for asset-generation (image/3d/sfx); v97 is for core-product-functionality (compression) |
| Substrate-Tolerance via WASM (v94 Understand-Anything) | v94 = embedding Tree-sitter via WASM (3rd-party tool tolerance); v97 = shipping own model (vertical-integration) |
| Karpathy autoresearch v9 substrate (v79 derivative) | v79 trained tiny model on Karpathy training framework; v79 did not ship pretrained-bundled model; v97 = pretrained-bundled |
| LLM Inversion Architecture (v80 SmartMacroAI) | v80 LLM-as-callable-tool over remote OpenAI/Gemini API; v97 = LLM-as-bundled-substrate, no cloud dependency |
| Foundational-Vendor-Direct-Source (a)-7 cluster | v92-v95 Anthropic-direct-org ships LLM-via-cloud-API; not bundled-at-product-install layer |

**No prior corpus subject** ships an own-fine-tuned bundled LLM at single-subject solo-founder scale. v97 = corpus-first.

## Why this is observational-layer not Pattern-layer at N=1

- N=1 is insufficient for top-level Pattern promotion (routine v2.3 §2 N=3 cross-axis spread requirement).
- Sub-archetype vehicle REJECTED at N=1: subject is T2 Service + T1 side-artifact; load-bearing property "ships own LLM" is a methodology-vocabulary axis, not a tier-membership axis.
- Library-vocab observational registration is the correct N=1 vehicle.

## Promotion-eligibility ladder

| Stage | Trigger | Audit window |
|---|---|---|
| **N=1 PROVISIONAL** (current) | v97 anchor registration | filed 2026-05-25 |
| **First-cycle stale-check** | Detect early-staleness if no N=2 emerges in next 4-5 wikis | v100/v101 audit |
| **N=2 STRENGTHENING** | Second subject in v60+ window ships own-fine-tuned bundled LLM at solo-founder scale | v100-v110 watch |
| **N=3 CONFIRMED** | Third subject crosses solo-founder + bundled + own-fine-tuned + public-registry threshold | v110-v120 watch |
| **15-wiki forced-retire** | If N=2 not reached by v112 | v112 hard-stop |

Compare to Library-vocab #13 (v78 OSS-with-hosted-Pro-SaaS-tier-on-MIT-base) which was retired at v96 §18 forced-retire (15-wiki distance v78→v96 without N=2 emergence). v97 anchor sets clock at 2026-05-25; v112 = 15-wiki forced-retire deadline.

## Cross-axis variance scoping for future N=2/N=3

To strengthen at N=2/N=3, future evidence subjects should:
- Cross-vendor: ship via Hugging Face OR equivalent public registry (not vendor-locked)
- Cross-domain: any product vertical (compression, summarization, code-completion, etc.)
- Cross-framework: MLX (Apple) + GGUF (llama.cpp) + ONNX + native PyTorch all admissible
- Cross-scale: <10B params (consumer-grade local) vs >10B (developer-workstation-grade)
- Cross-license: MIT / Apache / NULL (v97 anchor = NULL) all admissible

The corpus-novelty is the *vertical-integration at solo-founder scale*; the substrate framework is the variation axis, not the membership axis.

## Adjacent corpus-recursive observations

- **Pattern #84 84d Hardware-Substrate-Tolerance** — v97 MLX-Apple-Silicon-bundled-model is N=3 strengthening (v79 PyTorch MPS + v94 WASM + v97 MLX). N=3 cross-substrate-class spread (PyTorch-Metal + WASM-software + MLX-Apple-native). Phase 4b SECONDARY observation. Administrative-promotion-eligible at v100 audit if §3 vehicle #1 (Pattern-promotion at N=3 threshold) is invoked.
- **Library-vocab "Token-Economy-Quantification"** (v87 anchor) — v97 N=2 STRENGTHENING at product-output-level (99% saving claim) distinct from v87's per-style %-impact axis. Promotion-eligibility decision at v100 audit (REGISTER as 2-anchor sub-typology vs maintain as separate Library-vocab).

## v2.4 codification candidate

- **N=3 cross-axis spread requirements for Library-vocab promotion-ladder formalization** — routine v2.3.1 inherits v2.3 §2 promotion ladder for Patterns but does not formally specify the Library-vocab N=3 ladder structure. v97 introduces NEW Library-vocab requiring a formal ladder; v2.4 should codify by analogy to Pattern N=3 promotion-eligibility criteria.
- **Solo-founder scale evidence-threshold** — current Library-vocab #15 (Operator-Elected-Override-with-Honest-Documentation-Trail; v84 anchor) uses ONE-TIME-EXCEPTION qualifier. v97 introduces solo-founder-scale qualifier as an evidence-threshold-axis. v2.4 should codify scale-qualifier vocabulary.
