# Features & the demo workflow

## Source

`nexu-io/open-design` README + `QUICKSTART.md` (gh-api / WebFetch) + the video demo (`raw/2026-07-01-open-design.md`, chapters *Exploring Features* 01:23, *Creating Prototypes* 13:02). Workflow `wf_4a91a8b2-2bb` agents `opendesign-usage`, `hyperframes`.

## The feature surface

| Artifact type | What it produces | Notes |
|---|---|---|
| **Prototype** | single-page HTML (web / desktop / **mobile**) | **wireframe** (boxes/shapes) or **high-fidelity** (full styled page) |
| **Live artifact / dashboard** | interactive HTML dashboard | data-driven surfaces |
| **Deck** | slides via `guizang-ppt` + `html-ppt` skills | → PPTX / PDF; see [[open-design/the-originals]] |
| **Image** | high-res assets | via media providers (see below) |
| **Video** | MP4 | via media providers |
| **HyperFrame** | HTML→MP4 **motion graphics** | deterministic (headless Chrome + FFmpeg); from [`heygen-com/hyperframes`](https://github.com/heygen-com/hyperframes) |

**Export:** HTML / PDF / PPTX / MP4, all previewed in a **sandboxed iframe**. Everything is **local-first** — your designs stay inside the project directory you're running against (the video stresses this: switch folders and each project keeps its own designs).

**Two things Claude Design makes you do that Open Design doesn't:**
1. Claude Design makes you **start from a design system first**; Open Design gives you **defaults** so you can start from a blank slate, an existing website, or a starter system, and add branding later.
2. Claude Design is one model in the cloud; Open Design lets you **import an existing Claude Design `.zip` export** and continue locally on your own agent (the demo does exactly this — see caveat below).

**Media providers (⚠️ video + hero-image claim, not enumerated in fetched repo docs):** the video lists **Suno** (music), **Midjourney / Fal AI / OpenAI GPT-image ("GPT image 2")** (image), **ElevenLabs / MiniMax** (audio/TTS), and **Composio** for MCP connectors — add your own API keys per provider. The BYOK proxy docs only enumerate OpenAI/Anthropic/Azure/Google/Ollama/senseaudio, so treat the specific creative-media integrations as **single-source (video + hero alt-text)**.

## The exact demo workflow (from the video, 13:02→21:47)

This is the concrete loop, useful as a mental model for a pilot:

1. **Name the prototype + pick fidelity.** Dennis names it "Expensely", picks **high-fidelity**.
2. **Import an existing Claude Design `.zip`.** He imports a design system he'd previously built in Claude Design → Open Design shows the imported design files (a "projections page") in a left-panel file browser, preview on the right — *same feel as Claude Design*.
3. **Prompt.** "A new page projecting expenses for 12 months using the previous 3 months."
4. **Clarifying questions.** The agent asks back (same colors? fidelity? averaging method? chart type? filename?) — you answer inline. (This clarify-first behavior comes from the *agent*, not documented as a distinct Open Design "mode".)
5. **To-do list + generation.** The agent (detected as **Claude Opus 4.7**) writes a to-do list, reads the design system, and builds `projections-v2.html` (plus a JSX/React file) using the imported tokens/components.
6. **Inspect + iterate.** Browse the generated design files, preview each HTML. Ask for "a different look and feel" → it asks a clarifying question (editorial? Monaco?) → generates `projections-v3.html` in a distinct "editorial" direction using the same data. The final artifact is a **working, clickable prototype** (charts respond).

Net: **prompt → clarify → to-do → `.html`/JSX artifact → iterate variants**, all against a locally-held, imported design system, driven by your own Opus 4.7 CLI.

## ⚠️ Verification notes on the workflow

- **Claude Design `.zip` import** is shown in the video and mentioned on the landing page, but the `license-security`/`opendesign-usage` agents **could not find it documented in the repo `QUICKSTART.md`/`docs/`** — treat it as a real-but-lightly-documented feature (or one that evolved since the 2026-05-05 video).
- The video's counts ("31 skills", "72", etc.) are **point-in-time and don't match** the current repo (≈159 skills / ≈152 design systems). Numbers move weekly; see [[open-design/caveats-and-safety]].

## Key Takeaways

- Open Design's output surface is broad: **wireframe & hi-fi prototypes, dashboards, decks (PPTX/PDF), images, video, and HyperFrames motion graphics**, all exported to HTML/PDF/PPTX/MP4 and previewed in a sandboxed iframe — **local-first**, designs stay in the project dir.
- Unlike Claude Design it **doesn't force a design-system-first flow** and can **import a Claude Design `.zip`** to continue locally on your own agent.
- The working loop is **prompt → clarifying questions → to-do list → `.html`/JSX artifact → iterate v2/v3** — a good template for a Candidate-Detail pilot.
- Creative-media integrations (Suno/Midjourney/ElevenLabs/GPT-image/MiniMax) are **claimed in the video/hero image but not enumerated in the fetched repo docs** — verify before relying on them.
