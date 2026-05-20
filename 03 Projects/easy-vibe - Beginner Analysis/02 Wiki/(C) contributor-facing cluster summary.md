# (C) Cluster: Contributor-facing — VitePress architecture + llms.txt + 13-locale i18n + multi-deploy

## In one sentence

easy-vibe is a **VitePress** documentation site with **Vue 3 SFC `<script setup>` components**, **Prettier (no semicolons + single quotes)** discipline, **Conventional Commits**, **13-locale i18n**, **multi-deploy intelligence** (Vercel + GitHub Pages + Microsoft Azure + Docker + nginx with base-path detection), and a **CORPUS-FIRST `llms.txt` AI-Agent-optimized tutorial index** with 120+ topics + 20+ keywords-per-article + decision tree + dual-layer index + answer specifications.

## Repository topology

```
datawhalechina/easy-vibe/
├── README.md (vibe-coding methodology + curriculum + contributors)
├── CLAUDE.md (Claude-specific routing + commands + architecture)
├── AGENTS.md (cross-agent rules + VitePress conventions + Conventional Commits)
├── llms.txt (CORPUS-FIRST AI-Agent-optimized tutorial index)
├── Dockerfile (containerized deployment)
├── package.json + package-lock.json (npm scripts: dev / build / format)
├── vercel.json (Vercel deploy config)
├── ms_deploy.json (Microsoft Azure deploy)
├── nginx.conf (nginx serving)
├── eslint.config.js
├── .prettierrc + .prettierignore
├── .dockerignore
├── .gitignore
│
├── docs/                  ← VitePress documentation root
│   └── .vitepress/
│       ├── config.mjs     (sidebar + locale + theme config)
│       └── theme/
│           ├── index.js   (enhanceApp + component registration)
│           └── components/
│               └── appendix/
│                   ├── llm/    (LLM-related Vue components)
│                   ├── vlm/    (VLM-related Vue components)
│                   ├── git/    (Git-related Vue components)
│                   └── ...     (more topic-organized components)
│
├── docs-readme/          (additional documentation)
├── assets/               (image + media assets; contributes to 441MB repo size)
├── config/               (additional config)
├── scripts/              (build scripts)
│
├── .github/
│   └── workflows/        (CI/CD: build + deploy to GitHub Pages)
├── .husky/               (git pre-commit hooks)
├── .trae/                (Trae-specific harness config)
├── .vscode/              (VS Code workspace config)
```

## VitePress + Vue 3 architecture

- **Documentation layer:** `docs/` contains Markdown content organized as `stage-{N}/{chapter-directory}/index.md`
- **Theme config:** `docs/.vitepress/config.mjs` (sidebar + locale + theme)
- **Components:** Vue 3 SFC with `<script setup>` exclusively; live in `docs/.vitepress/theme/components/`
- **Registration:** new components register in `theme/index.js` via `enhanceApp` function
- **Constraints:** Node.js ≥ 18.0.0; preserve VitePress configuration integrity; test locally with `npm run dev`

## Build + dev commands

```bash
npm install       # First-time setup
npm run dev       # Local server (http://localhost:5173)
npm run build     # Production build
npm run format    # Prettier formatting (no semicolons, single quotes)
```

## Multi-deploy intelligence

**Base path detection** — site detects deployment environment automatically:

| Environment | Base path |
|-------------|-----------|
| Vercel | `/` |
| GitHub Pages | `/easy-vibe/` |
| Local development | `/easy-vibe/` |
| Microsoft Azure | (per `ms_deploy.json`) |
| Docker | (per `Dockerfile` + `nginx.conf`) |

This is corpus-first **5-deploy-target intelligence at runtime** with environment auto-detection (vs prior corpus subjects that required manual config per deployment target).

## 13-locale i18n (CORPUS-RECORD-HIGH)

| Aspect | Value |
|--------|-------|
| Locale count | 13 |
| Primary | Simplified Chinese (`zh-cn/`) |
| Other documented | English / Japanese + 10 others |
| Structure | Per-locale directory follows `zh-cn/` template |

This exceeds all prior corpus i18n records. v75 impeccable had EN + `.trae-cn` (2 locales); v74 LLMs-from-scratch was EN-only; v66+ corpus subjects largely EN-only with occasional CJK additions.

## `llms.txt` — CORPUS-FIRST AI-Agent-optimized tutorial index

This is a NEW artifact-type in the corpus. The file is designed for AI Agent consumption (Claude, GPT-4, Cursor, etc.), not human reading.

**Structure:**

```
[Document type declaration]
[3+1-stage architecture: Stage 0-1 + Stage 2 + Stage 3 + Appendix-9-knowledge-domains]
[Quick decision tree: user-intent → tutorial-section routing priority]
[Dual-layer index]
  Layer 1: Directory structure quick-reference (physical file path mapping)
  Layer 2: Detailed article index (keyword-tagged + file-location + content-summary)
[120+ articles with 20+ search keywords each]
[Answer specifications]
  - Citation format
  - Code-first strategy
  - Stage-matching principle
[Version management: update dates + article counts]
[10+ language versions]
```

**Position vs prior corpus artifacts:**

| Wiki | Subject | LLM-optimization artifact | Mechanism |
|------|---------|---------------------------|-----------|
| v75 | impeccable | HARNESSES.md | Cross-harness spec compliance matrix |
| v76 | agent-skills-standard | AGENTS.md router | 3-tier hierarchical lookup (router → category-index → skill) |
| **v77** | **easy-vibe** | **llms.txt** | **AI-Agent-optimized tutorial index with intent-routing** |

3 corpus subjects in v75-v77 each introduced a distinct LLM-optimization artifact-type. This is a NEW Library-vocabulary item #12 candidate "AI-Optimized Tutorial Index via llms.txt".

## Code style + governance

- **Prettier:** no semicolons + single quotes
- **Conventional Commits:** `feat:` / `fix:` / `docs:` prefixes
- **Vue 3 SFC:** `<script setup>` syntax exclusively
- **CSS:** VitePress theme variables for consistency
- **Diff discipline:** "Keep diffs small and avoid reformatting unrelated files"
- **Build validation:** `npm run build` as primary correctness mechanism

## License discrepancy

| Surface | Declaration |
|---------|-------------|
| README | "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License" |
| GitHub API license field | **"None specified"** |

This is **Pattern #83 sub-mechanism 83f N=3 PROMOTION-LOCKED evidence**:
- v74 LLMs-from-scratch (CITATION.cff "Apache-2.0" vs LICENSE.txt modified Apache)
- v76 agent-skills-standard (README "MIT License" vs LICENSE Apache-2.0)
- **v77 easy-vibe** (README CC BY-NC-SA 4.0 vs GitHub API "None specified")

3-instance arc within 3 wikis = CORPUS-RECORD sub-mechanism promotion-arc-speed.

## Trae harness presence

`.trae/` top-level directory = corpus-second-explicit Trae harness mention after v76 agent-skills-standard. Combined with v75 impeccable's `.trae-cn/` Chinese-variant directory, Trae has now appeared in 3 consecutive wikis (v75 + v76 + v77).

## Repository scale + contribution model

- 13,202 stars / 1,258 forks / 44 watchers / 10 open issues / 505 commits
- 441MB repo size (large — includes image/video assets for VLM components + multi-language content)
- Datawhalechina open-source community organizes contributions via established project governance framework
- Project lead **Sanbu** + mentor **Fang Ke** (Tsinghua University) + 5+ student contributors (Yerim Kang + Zhilin Zhao + Yixuan Li + Siyi Liu + Lixin Liu)

## What's missing / what to watch

- LICENSE file existence not confirmed (Pattern #83 sub-mechanism 83f N=3 evidence assumes README declaration without corresponding LICENSE file)
- Python content absence is unusual for a Chinese AI/ML education org's modern AI curriculum (JavaScript 89.1% only)
- Vibe Stories feature (launched 2026-03-29) — long-term sustainability of community-contributed real-user journey content unclear
- 13-locale translation maintenance burden — release-cadence per locale not visible at probe-level
