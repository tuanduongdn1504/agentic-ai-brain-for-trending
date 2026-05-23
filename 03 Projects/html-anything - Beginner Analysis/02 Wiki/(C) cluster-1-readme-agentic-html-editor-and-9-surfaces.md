# (C) Cluster 1 — README + Repo Metadata: Agentic HTML Editor + 75 Skills × 9 Surfaces + 8-Agent CLI Detection + Zero-API-Key + Hard-Constraint Template Discipline

**Source**: https://github.com/nexu-io/html-anything (README + GitHub API metadata)
**Fetched**: 2026-05-23 (Phase 0 + Phase 2 ingestion)
**Wiki version**: v91 (SECOND under routine v2.3 baseline)

---

## 1. Subject self-positioning

Repo description: *"✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it."*

Tagline: *"75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key"*

Core philosophy: *"Markdown is the draft. HTML is what humans read. Your local agent writes it."*

The product positions itself as **agentic HTML editor with local-first execution + zero-API-key dependency + multi-surface output from single markdown input + multi-agent CLI compatibility**.

## 2. Repository metrics

| Metric | Value |
|---|---|
| Created | 2026-05-11 (12 days old at fetch) |
| Last push | 2026-05-22 |
| Stars | 4,624 |
| Forks | 479 |
| Watchers (subscribers) | 15 |
| Open issues | 32 |
| Open PRs | 16 |
| Network | 479 |
| Commits on main | 27 |
| Repo size | 15,067 KB |
| Velocity | ~385 stars/day pulse-window |

The **~385 stars/day at 12-day pulse-window** places v91 at the HIGH-NOT-EXTREME Pattern #52 sub-class boundary (150-300/d). It's marginally above the upper edge of HIGH-NOT-EXTREME but below the EXTREME-VIRAL pulse-class (which historical anchors v63 Karpathy ~1,186/d and v68 zero 1,050/d defined). At pulse-class duration (12 days), this is upper-edge HIGH-NOT-EXTREME, not multi-month-sustained EXTREME-VIRAL.

## 3. License + Tech stack

- **License**: Apache-2.0 © 2026 HTML Anything contributors
- **Primary languages**: HTML 62.3% + TypeScript 37.4% + Other 0.3%
- **Frontend**: Next.js 16 (App Router + Turbopack) + React 19 + Tailwind v4 + zustand state management
- **Processing libraries**: juice (CSS-inlining for WeChat) + modern-screenshot (PNG export) + xlsx + papaparse + marked + highlight.js + dompurify
- **Deployment model**: "Local or Vercel — agent stays local"
- **Workspace structure**: monorepo with `next/` (Next.js app `@html-anything/next`) + `e2e/` (Playwright tests `@html-anything/e2e`)

The tech stack is current-era (Next.js 16 + React 19 + Tailwind v4 + Turbopack = bleeding-edge releases). The processing-library set (juice + modern-screenshot + dompurify + papaparse) reveals the multi-surface-export concern — HTML-to-various-formats pipelines.

## 4. 8-Agent CLI Ecosystem Detection

Supported coding agents:

| # | Agent | Binary detection name |
|---|---|---|
| 1 | Claude Code | `claude` |
| 2 | OpenAI Codex | `codex` |
| 3 | Cursor Agent | `cursor-agent` |
| 4 | Gemini CLI | `gemini` |
| 5 | GitHub Copilot CLI | `copilot` |
| 6 | OpenCode | `opencode-cli` / `opencode` |
| 7 | Qwen Coder | `qwen` |
| 8 | Aider | `aider` |

The agent-detection-by-CLI-binary mechanism is **Pattern #84 84c.1 sub-sub-mechanism strengthening** at the agent-detection layer. The 8-agent count places v91 mid-range in the v60+ ecosystem-citation density spectrum:
- v85 ui-ux-pro-max-skill: 18-platform `skill.json` formal manifest CORPUS-RECORD
- v83 open-design: 16-harness multi-target distribution
- v90 academic-research-skills: 2-harness narrow Claude+Codex
- v91 html-anything: 8-agent CLI detection (mid-range)

**Corpus-subject ecosystem citation density at v91**:
- Claude Code = v65 corpus subject
- OpenAI Codex = v62 corpus subject (codex-plugin-cc)
- Cursor Agent = v75/v76 corpus subjects (multiple)
- Gemini CLI = non-corpus (referenced but not yet subject)
- GitHub Copilot CLI = non-corpus
- OpenCode = v67 corpus subject (opencode-antigravity-auth)
- Qwen Coder = non-corpus (referenced)
- Aider = non-corpus

**6+ corpus-subject citations** (Claude Code + Codex + Cursor + OpenCode = 4 direct corpus subjects + 4 non-corpus harnesses; including transitive references through Cursor v75/v76 separate wikis = 6 corpus-references at the agent-detection-list layer). Pattern #57 sub-variant 57c-product STRONG density.

## 5. 75 Skills × 9 Surfaces

The product ships **75 composable skill templates across 9 deliverable surfaces**:

| # | Surface | Use-case |
|---|---|---|
| 1 | Magazine articles | Long-form readable web articles |
| 2 | Keynote decks | Slide-deck presentations (1920×1080 canvas from `1weiho/open-slide` convention) |
| 3 | Résumés | CV-style single-page documents |
| 4 | Posters | Single-page visual posters |
| 5 | Xiaohongshu cards | China-Mainland social network format |
| 6 | Tweet cards | Twitter/X social cards |
| 7 | Web prototypes | Interactive HTML prototypes |
| 8 | Data reports | Charts + tabular data presentations |
| 9 | Hyperframes videos | Frame-script schema from `heygen-com/hyperframes` |

The 9-surface output spectrum maps to **multi-modal content creation use-cases** — articles + decks + résumés + posters + social cards + prototypes + data reports + videos. This is CORPUS-FIRST 9-surface output diversity from single markdown input in v60+ window.

**Library-vocab "Multi-Surface-Output from Single-Markdown-Input (9 surfaces)" PROVISIONAL N=1**.

## 6. Zero-API-Key via Reuse-of-Logged-In-Agent-Session

The README emphasizes: *"Zero API key required — reuses the session you already have logged in"*. This is CORPUS-FIRST paradigm in v60+ window — most prior subjects assumed BYOK (Bring-Your-Own-Key) or self-hosted-model. v91 reuses the active session of whichever of the 8 supported agents is already logged in.

This is structurally different from:
- **BYOK** (typical Pattern #45 + Pattern #66 supply-chain dependency)
- **Self-hosted model** (typical T5 Application substrate dependency)
- **OAuth-credential-plugin** (v67 opencode-antigravity-auth T4b Credential-Bridge sub-archetype)

The reuse-of-logged-in-session paradigm avoids credential-handling entirely — the local agent CLI already holds its own session/credentials; html-anything just invokes the local CLI binary. Zero credentials touch the html-anything code-path.

**Library-vocab "Zero-API-Key via Reuse-of-Logged-In-Agent-Session" PROVISIONAL N=1**.

## 7. Streaming Render via SSE + Sandboxed-Iframe Preview

**SSE (Server-Sent Events) streaming**: *"watch the page render line by line"* — the agent's HTML output streams to the browser preview in real-time as it's generated. This is a UX-pattern observation distinct from typical batch-render or button-click-render flows.

**Sandboxed-iframe preview**: *"allows scripts and same-origin, quarantines cookies"* — the preview iframe uses `sandbox` attribute with explicit `allow-scripts` + `allow-same-origin` flags, but cookies are quarantined from the parent context. This is CORPUS-FIRST explicit sandbox-discipline at agentic-editor-preview-layer in v60+ window.

**Library-vocab "Sandboxed-Iframe-Preview with allow-scripts-same-origin-quarantines-cookies" PROVISIONAL N=1**.

## 8. One-Click Export Targets

| Target | Mechanism |
|---|---|
| WeChat | juice-inlined CSS (WeChat strips external stylesheets; juice inlines all styles) |
| X / Weibo / Xiaohongshu | PNG via modern-screenshot (image-based posting) |
| Zhihu | HTML with LaTeX placeholders (Zhihu has native LaTeX support) |
| Standalone HTML | Single-file portable HTML |
| High-DPI PNG | 2x-3x retina-grade PNG output |

The 5-target export matrix is **CJK-Asian-locale-anchored**: WeChat (Tencent ecosystem) + Weibo + Xiaohongshu + Zhihu = 4 of 5 are China-Mainland-specific platforms. Combined with the CJK-first font stack (see §9), v91 is **explicitly Chinese-Mainland-content-creation-anchored**.

This is the (a)-3 STRONG axis-call for Phase 0.9 — product-locale-inclusion at output-layer (stronger than docs-layer locale-inclusion like v90's 3-Asian-locale docs).

## 9. 5-Rule Hard-Constraint Template Discipline

Every template must satisfy:

1. **CJK-first font stack** — Noto Sans/Serif SC + Inter + Manrope (Simplified-Chinese-first ordering)
2. **8 px baseline grid** — vertical rhythm constraint
3. **Contrast ≥ 4.5:1** — WCAG AA accessibility
4. **No pure black/white** — softer-palette discipline
5. **No lorem ipsum** — must use real user data; placeholder text disallowed

This is **CORPUS-FIRST 5-rule hard-constraint template discipline at agentic-HTML-editor layer** — encoded directly into every skill template, not aspirational README text.

**Library-vocab "Hard-Constraint Template Discipline (5-rule)" PROVISIONAL N=1**.
**Library-vocab "CJK-First Font-Stack at Template-Level Hard-Constraint" PROVISIONAL N=1** (distinct sub-axis: the CJK-first specificity at template-level rather than i18n-docs-level).

## 10. Inspirations & Attribution Chain

The README explicitly cites and credits these inspirations (cross-product skill-vendoring + acknowledged influence):

| Source | Role |
|---|---|
| `mdnice/markdown-nice` | WeChat/Zhihu paste compatibility precedent |
| `gcui-art/markdown-to-image` | iframe-to-PNG export pipeline reference |
| `alchaincyf/huashu-md-html` | **Anti-AI-slop discipline source** (= v82 huashu-design family / 花叔) |
| `op7418/guizang-ppt-skill` | **Vendored as `deck-guizang-editorial`** (= bundled in v83 open-design too — CORPUS-FIRST same-org-cross-product-skill-vendoring) |
| `tw93/kami` | Warm-parchment editorial style (`doc-kami-parchment`) |
| `1weiho/open-slide` | 1920×1080 canvas convention for decks |
| `heygen-com/hyperframes` | Frame-script schema for Hyperframes video |
| `remotion-dev/remotion` | MP4 rendering target |
| `multica-ai/multica` | Daemon-and-runtime architecture reference |

**Cross-wiki corpus-recursive density at v91**:
- v82 huashu-design / 花叔 → `alchaincyf/huashu-md-html` cited
- v83 open-design → `op7418/guizang-ppt-skill` SAME vendoring as v91
- v78 ECC corpus-recursive → `heygen-com/hyperframes` possibly architecturally adjacent to ECC Hermes operator at multi-surface-output axis (NOT confirmed corpus-recursive, requires v95 audit deeper-investigation)

**Pattern #57 sub-variant 57c-product** strengthening + **NEW sub-variant candidate "Same-Org Cross-Product Skill-Vendoring within Indie-Org Portfolio"** PROVISIONAL N=1 — distinct from existing 57i Multi-Tier Corpus-Recursive Citation Density at Single Subject (v83) because v91 is the **cross-product** layer not the **citation-tier** layer.

## 11. Workspace Structure & Distribution

- `next/` — Complete Next.js app package `@html-anything/next`
- `e2e/` — Playwright test package `@html-anything/e2e`

**Install path**: `git clone + cd + pnpm install + pnpm -F @html-anything/next dev` → localhost:3000.

This is **single distribution channel** (clone + pnpm), unlike v83's 4-distribution-method matrix (source + Docker + Desktop + Vercel) or v90's 3-channel matrix (Marketplace + git+symlink + Codex sibling). v91 leans on local-development setup.

**Cost-of-trial calibration**: MODERATE (5-15 min depending on Node ecosystem state) — heavier than v87 single-file-copy ≤1-min or cc-switch single-binary install but lighter than full design-system deployment.

## 12. Status Claims

| Feature | Status |
|---|---|
| Agent detection (8 CLIs) | ✅ stable |
| Skill registry (75 skills) | ✅ stable |
| SSE streaming | ✅ stable |
| Sandboxed preview | ✅ stable |
| Export functionality | ✅ stable |
| Multi-template compare | 🛠 in progress |
| Hyperframes → MP4 | 🛠 in progress |

5-of-7 features marked stable + 2 in-progress = **honest-feature-status-disclosure** discipline echoing Pattern #83 Honest-Deficiency-Disclosure CONFIRMED N=5 (v69 promotion). At 12 days old this is unusually mature feature-status accounting — suggests pre-v91 internal development at nexu-io before public release.

## 13. Live demo / community

- **Live overview page**: `open-design.ai/html-anything/` — **CORPUS-FIRST same-org-cross-product domain-hosting** (open-design.ai is v83's product domain; v91 marketing surface is hosted under v83's domain)
- **Community**: Discord channel + Twitter @nexudotio

The domain-sharing observation (open-design.ai/html-anything/) is a corpus-novel signal of **same-org coordinated-product-portfolio strategy** — distinct from v83's standalone open-design.ai positioning.

## 14. Summary

This cluster establishes the **product structural surface**:

- Agentic HTML editor with 75 skills × 9 surfaces (multi-modal output)
- 8-agent CLI ecosystem detection (Claude/Codex/Cursor/Gemini/Copilot/OpenCode/Qwen/Aider; 6+ corpus subjects)
- Zero-API-key via reuse-of-logged-in-agent-session (corpus-first paradigm)
- SSE streaming render + sandboxed-iframe preview with quarantined cookies
- 5-rule hard-constraint template discipline (CJK-first font + 8px grid + contrast + no-pure-BW + no-lorem)
- 5-target export matrix (WeChat juice / X-Weibo-Xiaohongshu PNG / Zhihu LaTeX / HTML / High-DPI PNG = CJK-Asian-anchored)
- Cross-product skill-vendoring with corpus-recursive attribution chain (op7418/guizang shared with v83 + alchaincyf/huashu-md-html from v82 family)
- Live demo hosted under v83 sister-product domain (open-design.ai/html-anything/) = same-org coordinated-product-portfolio signal
- Apache-2.0; Next.js 16 + React 19 + Tailwind v4 tech stack
- Single-channel distribution (clone + pnpm); MODERATE cost-of-trial

**Phase 4b PRIMARY contribution**: This cluster's most novel finding is the **same-org-cross-product skill-vendoring + sister-product domain-hosting + sub-90-day release cadence at indie-org-portfolio scale** — feeding the NEW Library-vocab PRIMARY proposal.

See cluster-2 for nexu-io org profile and 5-product portfolio context. Entity pages for Pattern Library implication detail.
