# Original: Seedance 2.0 (image→video)

> The model the video uses to **animate a static hero image into a short looping video background**. The transcript's **"C dance"** is a phonetic mishearing of **"Seedance."** Confidence **high**. See the meta-correction below — this is the one original the workflow's own synthesis brief got *wrong*.

## ⚠️ Meta-correction (Rule 7 conflict, resolved by evidence)

The verification workflow's **synthesis brief** declared Seedance *"not a real product — skip it entirely."* **That conclusion was wrong.** The same workflow's dedicated `seedance-2.0` research agent — **confidence: high**, T1-confirmed against the Higgsfield product page and corroborated across fal.ai/WaveSpeedAI/getimg/aimlapi — established that **Seedance 2.0 is a real, shipping ByteDance video model.** Per Rule 7 (surface the conflict, pick the better-evidenced side) and Rule 4 (never fabricate — *and never falsely declare something fabricated*), the wiki records **Seedance as real** and flags the brief's over-correction. Logged in [[ai-web-design-workflow/source-provenance]].

## What it is

- **Seedance 2.0** — ByteDance's **multimodal AI video generation model**. Announced **2026-02-12**, widely available April 2026; launched on **fal.ai 2026-04-09**, also hosted on **Higgsfield** (the video's link, `higgsfield.ai/seedance/2.0`) and **WaveSpeedAI**. Higgsfield is a **platform aggregator**, not the maker.
- Transforms **text, image, audio, and video** inputs into video with **native synchronized audio** in one pass.

## Verified facts (T1 unless noted)

- **Architecture:** Dual-Branch Diffusion Transformer (DiT for spatial generation + RayFlow for temporal coherence); video + audio processed together — no post-production stitching.
- **Inputs:** up to 9 images, up to 3 videos (≤15s total), up to 3 audio clips (≤15s total); **output 4–15s per shot**, multi-shot for longer sequences.
- **Aspect ratios:** 16:9, 9:16, 4:3, 3:4, 21:9, 1:1 (confirmed on WaveSpeed; ⚠️ Higgsfield's page doesn't list ratios explicitly). **Resolution** up to 1080p (some tiers 2K).
- **Native audio by default** — dialogue (lip-sync, 8+ languages), ambient, music in a single pass. **This matches the video exactly:** the hero clip came back *with sound*, and the creator had to ask the tool to remove it.
- **Leaderboard:** #1 on Artificial Analysis image-to-video (Elo **~1,195** current; the **1,351** figure was a **March-2026** number — corrected).
- **Pricing:** WaveSpeedAI pay-per-use **$0.60** (5s, 480p) → **$5.40** (15s, 1080p), no subscription. Higgsfield **Business $49/seat/mo** (min 2 seats) confirmed; ⚠️ consumer tiers (Starter/Plus/Ultra ~$15–$84) appear in aggregators but are **not confirmed on the official Higgsfield page**; ~25 credits per 5-second clip.

## How the video uses it (reproducible)

1. Take the generated hero image (from [[ai-web-design-workflow/original-chatgpt-images-2-0|Images 2.0]]).
2. Prompt Seedance 2.0: *"8-second animation, 16:9, model Seedance 2.0, slowly animate the sound waves."*
3. It returns a short clip **with audio** → ask it to **remove the sound**.
4. Hand to the coding agent: *"replace the attached video with a background image of the hero section"* → embed as a `<video>` hero background.

The sub-loop ("animate a static image → use as hero background, audio off") is **tool-agnostic** — Veo, Runway Gen-4.5, Pika, Sora-class models do the same. The *pattern* transfers; the vendor doesn't matter.

## What's flagged

- Synthesis-brief "doesn't exist" verdict — **refuted** (see meta-correction).
- Elo 1,351 → corrected to ~1,195 (stale March figure).
- Higgsfield consumer-tier pricing + explicit aspect-ratio support — unverified on the official page.
- Exact motion-prompt grammar; whether audio can be disabled *at generation time* vs removed after.

## Key takeaways

- **Seedance 2.0 is real** (ByteDance, on Higgsfield/fal.ai/WaveSpeed); the "C dance" mishearing and a buggy synthesis verdict were the only confusion.
- **Audio-on-by-default** is the gotcha for website hero backgrounds — plan to strip it.
- For a hero-background animation, the pattern (image→short loop→mute→embed) is the durable knowledge; pick any image→video model on cost/quality.
- A clean demonstration of **why conflict-surfacing matters**: averaging the two agent outputs would have buried a real, useful tool.

## Cross-links

[[ai-web-design-workflow/the-redesign-workflow]] · [[ai-web-design-workflow/original-chatgpt-images-2-0]] · [[ai-web-design-workflow/source-provenance]] · [[ai-web-design-workflow/overview]]
