# Overview — vibe-designing with a coding agent + a taste skill

## Source

- **Video:** Lukas Margerie, "Redesigning Websites with GPT-5.5 & Images 2.0" ([PFO01z7Qe38](https://www.youtube.com/watch?v=PFO01z7Qe38), 2026-04-24, 7:18). Transcript: `raw/2026-06-20-ai-web-design-gpt55-taste-skill.md`.
- **Originals double-deep-dived:** [[ai-web-design-workflow/taste-skill-deep-dive|Taste Skill]] · [[ai-web-design-workflow/original-gpt-5-5-codex|GPT-5.5/Codex]] · [[ai-web-design-workflow/original-chatgpt-images-2-0|Images 2.0]] · [[ai-web-design-workflow/original-seedance-2-0|Seedance 2.0]].

## What "vibe-designing" is

- The 2026 sibling of vibe-coding: **describe** a website in natural language, let an agent build it, then iterate on *taste* and *assets* through more natural language — "human taste as the driving force." (T2-confirmed industry term; Adobe's 2026 Creative Trends report: 58% of pro designers use AI generation tools weekly; platforms: Cursor, Lovable, Bolt, v0, **Claude Code**, Figma Make.)
- The video is one worked instance of it, on the OpenAI stack. The *pattern* is vendor-neutral.

## The 5-step loop the video demonstrates

1. **Scaffold** — open Codex (GPT-5.5), paste a landing-page prompt → first-draft page. (Video runs Claude Opus 4.7 and Codex/GPT-5.5 side-by-side on the same prompt; creator subjectively prefers Codex's output — **opinion, not benchmark**, see below.)
2. **Fix the taste** — install the **Taste Skill**, run its `redesign` command → the page is restyled to a less-"AI-generated" look (better Bento grid, real background image, scroll/hover/fade interactions). *This is the step that actually moves quality.*
3. **Redesign section images** — feed a section + a reference image + the original page prompt to **ChatGPT Images 2.0** → a restyled image; drop it back into the page via the agent.
4. **Animate the hero** — send a static hero image to **Seedance 2.0** ("8-second, 16:9, slowly animate the sound waves") → a short video; it generates audio by default, so ask it to remove the sound; embed as a hero background.
5. **Asset-swap + polish** — the agent replaces images/video in the code; use **"annotate → delete this"** (point at an element, say "delete this") to remove unwanted pieces. Final: clean hero with video background, real section images, motion.

## Why the Taste Skill is the real prize

- The coding agent, the image model, and the video model are all **swappable**. The thing with durable, transferable knowledge is the **Taste Skill** — an open, MIT-licensed, *portable* design discipline.
- It encodes **what makes LLM-generated UI look generic** as **mechanical, checkable rules** (em-dash ban, no-Inter-default, hero ≤ 2 lines, no three-equal-column cards, Bento with zero empty cells, real images required, motion isolated in client components, WCAG AA contrast…) gated by a **62-point all-or-nothing pre-flight checklist**.
- Crucially: it **runs in Claude Code** (it ships a `.claude-plugin/plugin.json`) — so a Claude-centric operator gets the whole quality lever without touching OpenAI. Full anatomy: [[ai-web-design-workflow/taste-skill-deep-dive]].

## The Claude-native translation (for a Claude-centric operator)

| Video step | OpenAI tool used | Claude-native / vendor-neutral equivalent |
|---|---|---|
| Scaffold + edit code | Codex + GPT-5.5 | **Claude Code + Opus 4.8** (evidence says Claude is the *stronger* front-end model — see below) |
| Taste / redesign | Taste Skill (in Codex) | **Same Taste Skill, installed in Claude Code** (`npx skills add …`) + Anthropic's own **`frontend-design`** skill |
| First-party "design" surface | — | **Claude Design** (Anthropic, launched 2026-04-17 — for prototypes/wireframes/pitch decks/marketing visuals) |
| Restyle section images | ChatGPT Images 2.0 | Any image model (Images 2.0, Gemini/Imagen, Flux, Ideogram) — the loop is tool-agnostic |
| Animate hero | Seedance 2.0 (Higgsfield) | Seedance / Veo / Runway / Pika — any image→video model |
| Annotate-to-edit | Codex annotate | Claude Code + a screenshot/`get_page_text` loop, or Claude-in-Chrome |

## The one claim to discard: "Codex beats Claude at front-end"

- The video's framing (run both, prefer Codex) is a **single-prompt subjective impression**, not a benchmark.
- The evidence runs the **other way**: a multi-prompt UI comparison (blog.kilo.ai) rates **Opus 4.7 more polished and more custom**, and **Sam Altman publicly acknowledged GPT-5.5 trailed on front-end at launch**. On SWE-bench the two are within ~5 points (Opus ahead); GPT-5.5 leads on *agentic* benchmarks (Terminal-Bench/OSWorld), not design. There is **no published design-quality benchmark** for either.
- **Implication for the operator:** staying on Claude Code is not a compromise here — it's the stronger-evidenced front-end choice. The Taste Skill is what closes the remaining "taste" gap, regardless of model.

## Key takeaways

- The transferable asset is a **portable design-discipline skill**, not a model choice. Adopt the skill; stay model-agnostic.
- "AI-generated look" is **mechanically diagnosable** — em-dashes, Inter, three-equal cards, fake-screenshot divs, purple gradients. A checklist beats taste-by-vibes.
- The image/video sub-loops (restyle-from-reference, animate-a-hero) are **tool-agnostic** and reproducible with any image/video model.
- For a Claude shop, the whole workflow runs on **Claude Code + the same Taste Skill** — and the evidence says Claude is the better front-end builder.

## Cross-links

[[ai-web-design-workflow/taste-skill-deep-dive]] · [[ai-web-design-workflow/the-redesign-workflow]] · [[ai-web-design-workflow/original-gpt-5-5-codex]] · [[ai-web-design-workflow/video-to-original-crosswalk]] · [[codex/_index]] · [[claude-skills/_index]] · [[harness-engineering/_index]]
