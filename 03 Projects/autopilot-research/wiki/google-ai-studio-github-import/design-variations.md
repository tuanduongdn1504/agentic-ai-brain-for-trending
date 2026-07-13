# Design Variations + Annotation Mode + Nano Banana

## What's real

Three related, confirmed AI Studio Build design capabilities:

1. **Design Variations** — one-click generation of multiple UI interpretations (layout, components, typography, palette) of a built screen, "ready to apply to your project," so iterating no longer means re-writing a prompt. A real Build-mode feature shipped in the July-2026 update batch (dedicated coverage: [techgenyz](https://techgenyz.com/google-ai-studio-design-variations-layout-generator/), [pasqualepillitteri](https://pasqualepillitteri.it/en/news/6571/google-ai-studio-design-variations-en)).
2. **Annotation / edit tool** — Google's own words ([I/O 2026 blog](https://blog.google/innovation-and-ai/technology/developers-tools/google-ai-studio-io-2026/)): *"Our new edit tool lets you annotate right in the preview window. Draw on your app, tweak components and generate new visuals to iterate on your build, right in the flow."* You mark a region of the preview and describe the change.
3. **Nano Banana** image generation — *"The AI Studio Build agent can automatically generate custom images on the fly using Nano Banana"* to fill tailored UI assets instead of placeholders.

## ⚠️ Corrections to the verification pass

- The Haiku agents **deflected Design Variations to "Stitch"** (a separate Google Labs design tool) and claimed *"AI Studio itself does not have design variation capabilities"* — another **docs-lag over-read** (the May I/O blog names the edit tool + Nano Banana but not the July "Design Variations" batch). Overridden: **Design Variations is a native AI Studio Build feature**; Stitch is a related-but-distinct tool. See [[source-provenance]].
- The video's *"circle a region"* = the annotate/draw tool (freehand/highlight); "circle" is not a documented named primitive. ◐
- *"Change to YouTube-style theme"* works as a **descriptive prompt**, not a **named template library** — there's no preset gallery of brand themes; you describe the style and it generates. ◐

## The caveat that matters most (video glosses it)

**Code fidelity when applied to *existing* production components is unverified.** Google's design tooling is documented for **greenfield UI generation** (from prompt/image/sketch). Whether applying a variant to a screen with **complex existing logic + Framer-Motion animations + form state** *preserves* that logic — as the video claims ("motion cards survived") — is **not guaranteed by any first-party source**. Design tools regenerate markup/CSS; they do not promise to keep your event handlers, state, and animation setup intact. Treat "apply variant to real component" as **high-risk without manual review**.

- Nano Banana is **paid, per-image** (~$0.04–$0.24/image depending on model/resolution; current model = "Nano Banana 2" / Gemini 3.x Flash Image, legacy = Gemini 2.5 Flash Image) and images may be trained-on unless on a paid/billing-attached tier. Not free.

## Why it matters for hireui — this is the extractable win

The active [[../../CLAUDE|Candidate-Detail refactor]] is stuck on **drifted design tokens** and a half-done r1→r2 migration. Design Variations is a genuinely useful **exploration** tool for that: fork a **sanitized, synthetic-data-only** clone of the screen, generate 3-5 directions, and **extract the direction/tokens as inspiration** — then implement properly in hireui under its rules (Figma SoT, locked plan paths). **Never ship AI Studio's generated code into the real component** (fidelity risk + it fights the token system). This is pilot **A2 ⭐** — the headline method. Nano Banana → non-sensitive assets only (job-category icons, empty states) = pilot **A3**.

## See also
[[_index]] · [[github-import]] · [[../ai-web-design-workflow/_index|ai-web-design-workflow]] · [[pricing-privacy-data]]
