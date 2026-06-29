# Original: ChatGPT Images 2.0

> The image model the video uses to **restyle section images from page context + a reference image**, then feed back into the coding agent. Verified live; confidence **medium** (several specifics rest on single secondary sources). See [[ai-web-design-workflow/source-provenance]].

## What it is

- OpenAI's image model/feature, **rolled out ~2026-04-21–22**, **integrated into Codex by ~2026-04-24**. Used inside ChatGPT and inside the Codex coding flow.
- In the video's workflow it does **image-to-image restyling**: give it an existing website section (as an image) + a reference image + the original page prompt, and it returns a restyled section image consistent with the page's design language.

## Verified facts (T2 — secondary sources)

- **One-shot generation of visual assets** for complex web UIs and games (the headline capability that makes the "redesign this section as an image" loop work).
- **Text rendering** much improved — cited as **~95–99%** accuracy across scripts (Latin/CJK/Arabic/Indic). ⚠️ Approximate and **not independently benchmarked** (MacRumors says "roughly 95%"; TechCrunch only says "improved").
- **Access:** part of paid ChatGPT tiers + Codex; a "thinking" image mode is paid-tier only. ⚠️ Specific per-tier prices ($20 Plus / $200 Pro) **were not confirmed** in fetched sources.
- **API image output pricing:** ~**$32 / 1M tokens** (corrected from a "$30/M" draft figure). ⚠️ A "$5/M text input" figure could **not** be confirmed.
- **Resolution:** up to **2K (2560×1440, experimental)**. ⚠️ A draft "4K upscaling" claim was **not** confirmed — do not cite 4K.

## The video's restyle workflow (reproducible, tool-agnostic)

1. Screenshot/select a website section that needs work.
2. Prompt: *"This is an image of a section in a website. Can you redesign it as an image based on the following prompt: \<the original page prompt\>"* — optionally attach a reference image (the video pulls references from Pinterest, and a community member supplied a gradient-section image).
3. Get the restyled image → hand it to the coding agent: *"replace the background image of \<X\> with this image"* (attach the generated file).
4. The agent swaps the asset into the code.

This loop is **not specific to Images 2.0** — any capable image model (Gemini/Imagen, Flux, Ideogram, Midjourney via export) supports "restyle from a reference + prompt." It's the *pattern* that transfers.

## What's flagged

- ⚠️ **QR-code generation** — a draft claimed it; **no fetched source mentions it**. Treated as a **likely fabrication** and **dropped**. (A good example of the verify pass catching an invented capability.)
- Exact model architecture / training data — undisclosed.
- Image format support (JPEG/PNG/WebP), batch capacity, failure modes (hallucinated UI elements, text edge cases) — undocumented.
- The programmatic **API model id** for Images 2.0 — not surfaced (matters if you'd script it rather than use the UI).

## Key takeaways

- The transferable idea is **"restyle a section image from page context + a reference, then let the agent swap it in"** — reproducible with **any** image model; not an OpenAI lock-in.
- Treat the quality numbers (~95–99% text, 2K) as **directional**; verify on your own assets before relying on them.
- A capability that "sounds plausible" (QR codes) was invented by a draft and removed in verification — a reminder to ground every product claim in a fetched source (Rule 4).

## Cross-links

[[ai-web-design-workflow/the-redesign-workflow]] (where this slots into the loop) · [[ai-web-design-workflow/original-seedance-2-0]] (the next stage: animate the image) · [[ai-web-design-workflow/overview]] · [[ai-web-design-workflow/source-provenance]]
