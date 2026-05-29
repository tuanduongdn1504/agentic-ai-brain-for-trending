# guizang-social-card-skill — Wiki (v105)

> 🪧 *"Claude Code / Codex skill — generate Xiaohongshu carousels & WeChat 21:9+1:1 cover pairs. Editorial × Swiss visual systems, 28 layouts, 10 themes, single-file HTML → PNG."*

## 1. Identity & metadata

| Field | Value |
|---|---|
| Repo | `op7418/guizang-social-card-skill` |
| Author | **op7418 = 歸藏 / Guizang** — Chinese-Mainland AI influencer (guizang.ai, @op7418, 150K+ followers, account since Aug 2013); AIGC weekly newsletter; maintains `guizang-s-prompt` AI-prompt repository |
| Tier / archetype | **T1 Assistant Skill / design-language** (7th member of the design-skill cluster: v75 impeccable · v81 taste-skill · v82 huashu-design · v83 open-design · v85 ui-ux-pro-max · v91 html-anything · **v105**) |
| License | **AGPL-3.0** (repo LICENSE). NOT corpus-first (prior AGPL subjects exist in the v1–v60 chapters). `package.json` declares `"license": "ISC"` — license-declaration mismatch (Pattern #83 83f) |
| Primary language | HTML 73.3% + JavaScript 26.7% |
| Stars / forks | 799 ★ / 105 forks |
| Subscribers / open issues | **1 subscriber / 0 open issues** (engagement-deficit despite 105 active forks) |
| Created / pushed | 2026-05-27 / 2026-05-27 (**~2 days old** at fetch) |
| Velocity | **~400 stars/day** = Pattern #52 EXTREME-VIRAL **pulse-class** (>300/d, <90d) |
| Default branch / releases | `main` / 0 releases |
| Repo size | ~1.9 MB |
| Topics (15) | agent-skill, ai-agent, anthropic, claude-code, claude-skill, codex, editorial-design, html-template, image-generation, playwright, rednote, social-cards, swiss-design, wechat, xiaohongshu |
| Locales | README.md (Chinese, primary) + README.en.md (2-locale, modest) |

## 2. What it does

A single Claude-Code / Codex **skill** that produces social-media card layouts for Chinese platforms:

- **Xiaohongshu / Rednote carousels** — 1080×1440 (3:4)
- **WeChat cover pairs** — 2100×900 (21:9) + 1080×1080 (1:1)
- **Two design systems:** **Editorial** (narrative/lifestyle, 16 layouts, 6 themes) and **Swiss** (structured/data-driven, 12 layouts, 4 accent themes)
- **28 layout skeletons**, **10 preset themes** (fixed palettes — no custom hex permitted), **11 Xiaohongshu category adaptations**
- Features: WebGL animated backgrounds, image-overlay masking, face-aware text placement, MapLibre map component
- **Rendering:** single-file HTML + Playwright → `output/*.png` (`node render.mjs`; no build pipeline)

## 3. Architecture

```
guizang-social-card-skill/
├── SKILL.md              ← 7-step workflow (Intake → Style/Theme → Layout → Asset Prep → Compose/Render → Deliver/Review → Iterate)
├── PRODUCT.md            ← vision, design philosophy, roadmap
├── HANDOFF.md            ← handoff documentation
├── README.md / README.en.md
├── validate-social-deck.mjs  ← 6-rule Playwright validator (R1 overflow · R2 type-size · R3 footer-collision · R4 4-band density · R5 frame-overflow · R6 Swiss identity)
├── agents/openai.yaml    ← single OpenAI/Codex agent config
├── assets/               ← editorial + swiss HTML templates, magazine-bg-webgl.js, screenshot backgrounds (9 WebP)
├── references/           ← 15 spec docs (style-system, theme-presets, layout-recipes, components, platform-specs,
│                            category-cookbook, image-overlay, portrait-fill, map-component, background-systems,
│                            content-planning, production-workflow, qa-checklist, screenshot-treatment, title-shortener)
└── package.json (license ISC, dep: playwright ^1.60.0)
```

- **No `skills/` subfolder, no `AGENTS.md`, no `llms.txt`, no `skills-lock.json`** → single-skill repo, not a bundle. Library-vocab #12 (LLM-routing artifacts) footprint is **LIGHT** (just root `SKILL.md` + `agents/openai.yaml`).
- **Image source priority chain:** user images → AI generation → Unsplash → Pexels → Flickr CC → Wallhaven → web search (+ `SOURCES.md` attribution).

## 4. Distribution & install

- **One-liner:** `npx skills add https://github.com/op7418/guizang-social-card-skill --skill guizang-social-card-skill` — the **`npx skills add` convention shared across the op7418 / Chinese design-skill ecosystem** (v82 huashu-design, v83 open-design).
- **Manual:** clone to `~/.claude/skills/guizang-social-card-skill`.
- **Supported harnesses:** Claude Code (native auto-discovery) · Codex (via `agents/openai.yaml`) · Cursor (with file I/O + shell) · other local agents. **Not** generic chatbots (needs persistent storage + render pipeline). 3-harness footprint = Pattern #57 57c-product citation density LOW-MID.

## 5. Corpus position (cross-references)

- **Design-skill cluster, 7th member** — [[v75 impeccable]] · [[v81 taste-skill]] · [[v82 huashu-design]] · [[v83 open-design]] · [[v85 ui-ux-pro-max]] · [[v91 html-anything]] · **v105**.
- **Vendored-author-to-subject (PRIMARY):** op7418's *sibling* product `guizang-ppt-skill` was **bundled** in [[v83 open-design]] (`skills/guizang-ppt/`) and **vendored** in [[v91 html-anything]] — but op7418 had never been a direct subject. v105 promotes the author from vendored-dependency to direct subject (corpus-recursive; relates to but is structurally distinct from v93 anthropics/skills "cited-to-subject"). See Phase 4b proposal.
- **China-Mainland sub-cluster N+1:** v82 alchaincyf (花叔) + v83/v91 nexu-io + v94 Lum1104 + v100 tisfeng + **v105 op7418 (歸藏)** — by-event extension. Asian-LOCATED cluster N+1.
- **Pattern #19 sub-mechanism 19m "Chinese-AI-Native-Coder-Influencer-with-Multi-Product-Portfolio" N=2 STRENGTHENING** — v82 alchaincyf (花叔) anchor + v105 op7418 (歸藏). Both: large-following Chinese AI influencer + multi-product skill/prompt portfolio + `npx skills add` distribution.
- **Pattern #28 sister "Editorial-Build-Validator" N=2 STRENGTHENING** — [[v75 impeccable]] (`npx impeccable detect` + STYLE.md denylist, 27 anti-pattern rules) + **v105** (`validate-social-deck.mjs`, 6 deterministic QA rules). 30-wiki gap.
- **Pattern #88 Anti-Slop-Design-Curation N+1** — op7418 publicly iterates "Stop Slop / 去 AI 味" anti-slop skills (5 core rules + 6-item pre-delivery checklist + 5-dimension quantitative evaluation); the social-card skill's fixed-palette + 6-rule validator + theme constraints embody 88c machinery-with-enforcement, alongside v82 huashu + v83 open-design.
- **Pattern #82 quantitative-marketing** — 28 layouts / 10 themes / 6 rules / 11 categories / 3 canvas sizes / 9 background assets.
- **Pattern #78 LDS** — 15 reference spec documents = mid-density living-domain-standards surface for a single-author skill.
- **Pattern #52 EXTREME-VIRAL pulse N+1** — ~400/d × 2d (pulse, not sustained); joins v63/v68/v78/v82/v83/v94 pulse instances.
- **Pattern #83 83f license-mismatch N+1** — `package.json` ISC (boilerplate default) vs LICENSE AGPL-3.0.

## 6. Honest caveats

- **AGPL-3.0 is NOT corpus-first** — prior AGPL subjects exist in the v1–v60 chapters. Notable only as a strong-copyleft (network-use) choice for a single-author design skill, and as a divergence from op7418's sibling `guizang-ppt-skill` (bundled under Apache-2.0 terms in v83's tree).
- **Functional-fit to Storm Bear is INDIRECT** — output medium is Chinese social platforms (Xiaohongshu/WeChat), which Storm Bear does not publish to. Transferable value is the *methodology* (constraint-based design, deterministic validator, theme-preset discipline) for sprint/Scrum visual artifacts — not the cards themselves.
- **Pulse velocity, not sustained** — 2 days old; the EXTREME-VIRAL rate is a launch-window pulse and should not be read as Multi-Month-Sustained.

## Sources
- [op7418 (歸藏) · GitHub](https://github.com/op7418)
- [歸藏(guizang.ai) (@op7418) / X](https://x.com/op7418)
- [op7418/guizang-s-prompt — Guizang's prompt repository](https://github.com/op7418/guizang-s-prompt)
