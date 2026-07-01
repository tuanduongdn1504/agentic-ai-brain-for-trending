# huashu-design — the design-philosophy original (deep-dive)

> **The load-bearing original for *your* design goals.** Open Design credits `alchaincyf/huashu-design` as its *"design-philosophy compass."* It composes directly with the **Taste Skill** you already run ([[../ai-web-design-workflow/_index]]) and answers the hireui token-drift problem at the *methodology* level.

## Source

[`alchaincyf/huashu-design`](https://github.com/alchaincyf/huashu-design) — gh api (2026-07-01): **20,457★**, **MIT**, **HTML**, created **2026-04-19**. README + `SKILL.md` + `references/brand-asset-protocol.md` + `references/design-styles.md` (fetched by Workflow `wf_4a91a8b2-2bb` agent `huashu`, which read the Chinese-language sources directly).

- **Author:** `alchaincyf` (花叔 / "huā-shū"), a solo AI-content creator (X `@AlchainHust`, WeChat/B站/YouTube, site huasheng.ai). **Not corporate.** Used in production for his own product **FanBox** (a coding-agent dashboard — its 3 UI skins are all made with huashu-design).
- **License history:** started "personal free, commercial restricted" → **relicensed MIT on 2026-05-14** (fully free incl. commercial). Install: `npx skills add alchaincyf/huashu-design`.
- **Multilingual:** default docs are Chinese (`SKILL.md` is Chinese-only) but there's a `README.en.md`. It is a **CLI-native `SKILL.md` skill**, agent-agnostic (Claude Code / Cursor / Codex / OpenClaw / Hermes) — **not a Figma plugin** ("no Figma plugin, no buttons, no panels — purely skill-driven").

## The 5-element methodology

huashu-design is not vibes — it's a **codified 5-element system** for making an LLM produce non-generic, brand-faithful design:

### 1. Junior-Designer workflow (communicate before executing)
Core philosophy #2: write your **assumptions + reasoning + placeholders at the top of the HTML file and *show them early*** before building the real thing. "Understanding it wrong early is 100× cheaper to fix than late." Iterate from feedback, not speculation. (Directly mirrors interview-first / grill-me discipline in [[../how-we-claude-code/_index]] and [[../pocock-agentic-workflow/_index]].)

### 2. Brand Asset Protocol (the operational core)
A **5-step hard process** (each step has a fallback, "never silently skip") that *reverses* conventional design order — it starts from **assets, not colors**:

- **Priority: Logo (highest) > Product Image (very high) > UI Screenshot (very high) > Color Value (medium) > Font (low).**
- Steps: **Ask** → **Search official channels** → **Download assets** → **Verify + extract** → **Codify a `brand-spec.md`** that every HTML file then references (change a color = edit the spec first).
- Rule: **use real images** (Wikimedia / Unsplash / AI-generated), **never** CSS silhouettes or hand-drawn SVG standing in for a real product image.

This is *exactly* hireui's missing piece: an **authoritative, single-source brand record** instead of drifted tokens. It's the methodology sibling of Open Design's `DESIGN.md` ([[open-design/design-md-as-source-of-truth]]).

### 3. Anti-AI-slop checklist
A concrete **prohibited-patterns table** — the statistical clichés an LLM defaults to, and *why* each is banned:
- ❌ radical purple gradients · ❌ emoji-as-icons · ❌ rounded card + left colored-border accent · ❌ hand-drawn SVG "imagery" · ❌ CSS silhouettes replacing real product images · ❌ generic GitHub-dark palette.
- ✅ approved signals of intentional design: `text-wrap: pretty`, `oklch()` colors, real AI-generated images, proper typographic rhythm.

This is the **same job as your Taste Skill's 62-point gate**, from a second independent author — run both as a two-gate anti-slop pass (see pilot method H4 / S2).

### 4. The 40-style design library (20 web + 20 PPT)
An "ammunition when stuck, not a mandate" catalog — each style annotated with a **fidelity/accuracy %**, a **temperature** (bold / neutral / quiet), pure-HTML/CSS implementation notes, and open-source font alternatives (e.g. "Editorial Brutalism ~98%", "Neo-Brutalism colliding-color feed ~95%"). Deliberately **front-loaded with bold options** to counteract the model's natural bias toward quiet minimalism. Default is pure HTML/CSS — **image generation is optional, not required.**

### 5. Design Direction Advisor (break single-aesthetic dependence)
When you're unsure of direction, spawn **3 parallel logic paths**, each producing a *real* visual prototype to choose from — not three text descriptions:
- **Logic 1 · "Seconds Roulette"** — forced randomness (`date +%S % 20` picks a style) to escape the model's default.
- **Logic 2 · Real-world reference** — port an award-winning site/deck/app.
- **Logic 3 · Best-designer philosophy** — "deep breath, top-tier custom."

Plus a **5-dimensional expert review** (philosophy consistency · visual hierarchy · execution detail · functionality · innovation, scored 0–10) for critique.

### (0) Fact-verification-first (highest-priority principle)
Principle #0: **WebSearch before asserting any fact** about a product/spec/release (esp. 2024+ releases, version numbers). Don't design from memory — ground it. (This is the same anti-fabrication discipline this vault enforces.)

## Why it matters to hireui

huashu-design maps 1:1 onto the Candidate Detail refactor's actual failure modes:
- **Brand Asset Protocol → `brand-spec.md`** = the fix for drifted navy/accent/font (the authoritative record hireui lacks).
- **Junior-Designer workflow** = "show assumptions before coding" = surface the 3-tabs / 72px-avatar / timeline-color decisions *before* the agent writes CSS.
- **Anti-slop checklist** = a second gate to compose with your Taste Skill.
- **Design Direction Advisor** = when the team disagrees, generate 3 real prototypes (e.g. vs LinkedIn/Indeed references) instead of debating text.

Concrete pilot methods: `output/(C) 2026-07-01-open-design-pilot-methods.md` (S2, H4, H8).

## Key Takeaways

- `alchaincyf/huashu-design` (20.5K★, MIT, solo Chinese author 花叔) is Open Design's **design-philosophy engine** — a codified **5-element methodology**, not aesthetic vibes.
- The **Brand Asset Protocol** (logo>product>UI>color, codified to `brand-spec.md`) is the *methodology* version of `DESIGN.md` and the direct answer to hireui's token drift.
- Its **anti-AI-slop checklist** is a second, independent gate that composes with your existing **Taste Skill** — run both.
- It's a **`SKILL.md` skill, not a Figma plugin** — installable standalone (`npx skills add alchaincyf/huashu-design`) *without* Open Design.
