# `/ck:*` command reference

> 50+ commands documented across vividkit's 21 guides. Source synthesis: `raw/2026-05-11-vividkit-claudekit-synthesis.md`.
>
> Use this as a lookup table when scanning what ClaudeKit offers AND as a comparison surface — many of these commands have equivalents in other harnesses or could inspire personal-harness additions.

## 1. Basics & Getting Started

| Command | What it does | When to use |
|---|---|---|
| `/ck:coding-level` | Set programming experience level (0-5) — tailors AI explanation depth | Switch between "Junior" and "God Mode" technical detail |
| `/ck:ask` | Technical/architectural advice WITHOUT implementing code | Second opinion on technology trade-offs |
| `/ck:brainstorm` | Generate solutions + analyze trade-offs via design-first approach | Start of a feature, before planning |
| `/ck:ck-help` | Interactive guide for commands/skills/workflows | When unsure which command fits |

## 2. Planning & Research

| Command | What it does | When to use |
|---|---|---|
| `/ck:plan` | Detailed implementation plan with research + red-teaming + task hydration | Complex features needing a structured roadmap |
| `/ck:research` | Deep technical research + best-practices evaluation | New frameworks, third-party API integrations |
| `/ck:scout` | Parallel-agent scan of codebase to identify relevant files | Find all call sites or related logic |
| `/ck:sequential-thinking` | Multi-step reasoning with self-correction + hypothesis testing | Architectural deadlocks, complex logic |
| `/ck:problem-solving` | Breaks complex issues into simpler variables to unblock | Circular logic, "wicked" problems |
| `/ck:predict` | Forecast architectural / security / performance impacts of changes | Before major refactor |
| `/ck:xia` | Research + extract + port features from external GitHub or local repos | "Borrow" feature pattern from high-quality OSS |
| `/ck:loop` | Automated optimization cycles for specific metrics (perf, coverage) | Iteratively improve bundle size or test coverage |

## 3. Execution & Implementation

| Command | What it does | When to use |
|---|---|---|
| `/ck:cook` | All-in-one engine: research → plan → implement → test → review | Fast autonomous implementation of known requirements |
| `/ck:bootstrap` | Full project init: stack + architecture + design + implementation | Brand-new application from scratch |
| `/ck:backend-development` | Build APIs / server-side logic (Node.js / Python / Go) | Scaffold NestJS, FastAPI, Django |
| `/ck:web-frameworks` | Monorepo + modern frontend framework config (Next.js) | App Router, SSR, Turborepo |
| `/ck:databases` | Schema design, query optimization, migrations | PostgreSQL, MongoDB, SQL relationships |
| `/ck:tanstack` | TanStack patterns (state, forms, AI streaming) | Advanced React data-fetching, chat interfaces |
| `/ck:deploy` | Auto-detects project type + deploys to 15+ cloud platforms | Vercel, Railway, AWS, Cloudflare |
| `/ck:ship` | Full delivery pipeline: merge → version → PR | Feature branch ready for production/beta |
| `/ck:agentize` | Wrap codebase into AI-friendly CLI tools + MCP servers | Make code consumable by other AI agents |
| `/ck:team` | Coordinate multiple specialized agents in parallel on large tasks | Massive projects where one agent hits context limits |

## 4. UI/UX & Frontend Design

| Command | What it does | When to use |
|---|---|---|
| `/ck:ui-ux-pro-max` | Design partner with 50+ styles + pro UX guidelines | Create accessible UI without a designer |
| `/ck:frontend-design` | Build UI from text / screenshot / video references | Replicate UI from reference image |
| `/ck:frontend-development` | React/TypeScript components with Radix + Tailwind | Standard component building |
| `/ck:ui-styling` | Themed styles via shadcn/ui + Tailwind | Dark-mode-ready theme-consistent components |
| `/ck:web-design-guidelines` | Audit code vs WCAG AA + standard guidelines | Ensure professional + accessible UI |
| `/ck:stitch` | Text-to-UI via Google Stitch pipeline | Rapid prototyping + asset export |
| `/ck:threejs` | 3D web apps + visualizations | Interactive 3D elements (globes, models) |
| `/ck:shader` | GLSL fragment shaders for procedural graphics | Performance visual effects in Three.js |
| `/ck:mermaidjs-v11` | Flowcharts / sequence diagrams / timelines via Mermaid v11 | Document logic in Markdown |

## 5. Testing, Debugging & Quality

| Command | What it does | When to use |
|---|---|---|
| `/ck:fix` | 6-phase pipeline: Scout → Diagnosis → Routing → Fix → Verification → Prevention | Repair errors from logs / failed tests, regression-safe |
| `/ck:debug` | Systemic root-cause analysis via call-stack trace + assumption validation | Bug with unknown origin |
| `/ck:test` | Local test suite + visual UI tests with deep analysis | Verify code changes, test live URL |
| `/ck:code-review` | Audit for quality / performance / edge cases via specialized agents | Pre-commit standards + security check |
| `/ck:web-testing` | E2E / load / accessibility testing via Playwright + k6 | Verify complex flows + performance under load |
| `/ck:agent-browser` | AI-optimized browser automation | Agent needs to "see" + interact with website |
| `/ck:scenario` | "What-if" architectural scenarios + edge cases | Simulate failures before implementation |
| `/ck:react-best-practices` | React/Next.js optimization per industry patterns | SSR/RSC performance refactor |

## 6. Security & Intelligence

| Command | What it does | When to use |
|---|---|---|
| `/ck:security` | Threat modeling + red-team discovery | High-stakes audits + risk mitigation |
| `/ck:security-scan` | Scan for hardcoded secrets + dependency vulns | Pre-commit security gate |
| `/ck:better-auth` | TypeScript auth (OAuth + 2FA + passkeys) | Login + identity management |
| `/ck:cti-expert` | Cyber threat intelligence + open-source investigations | Forensics, breach checking |

## 7. Git & Version Control

| Command | What it does | When to use |
|---|---|---|
| `/ck:git` | Git ops (commit / push / PR) via natural language | Conventional commits + security-checked staging |
| `/ck:worktree` | Isolated Git worktrees for parallel feature dev | Monorepo multi-branch work |

## 8. Documentation & Content

| Command | What it does | When to use |
|---|---|---|
| `/ck:docs` | Analyze codebase → init/update/summarize project docs | Sync READMEs with code |
| `/ck:docs-seeker` | Find official library docs via `llms.txt` endpoints | Latest API info without manual browsing |
| `/ck:preview` | Render files as visual explanations / slides / diagrams | Visualize plan or complex Markdown |
| `/ck:tech-graph` | Publication-quality technical SVG diagrams (7 design styles) | Pro docs, blogs, slide decks |
| `/ck:llms` | Generate `llms.txt` standard for AI-discoverable repos | Make codebase AI-friendly |
| `/ck:show-off` | HTML showcases + social media screenshots | Marketing assets for technical project |
| `/ck:copywriting` | Headlines / CTAs / conversion copy | Landing pages, emails, campaigns |

## 9. Project & Session Management

| Command | What it does | When to use |
|---|---|---|
| `/ck:watzup` | Summarize recent changes + wrap up working session | End of day, see what got done |
| `/ck:journal` | Record technical thoughts / decisions / lessons learned | Historical record of "the why" behind changes |
| `/ck:retro` | Data-driven sprint retro via Git metrics + health indicators | Sprint end churn + velocity analysis |
| `/ck:plans-kanban` | Visualize all implementation plans on timeline dashboard | Track long-term feature dev |
| `/ck:project-organization` | Analyze + restructure project file layout | When folder structure becomes messy |

## 10. Specialized Utilities

| Command | What it does | When to use |
|---|---|---|
| `/ck:graphify` | Queryable knowledge graph via tree-sitter AST | Understand "god nodes" + surprising connections in legacy code |
| `/ck:ai-multimodal` | Analyze images / audio / video via Gemini APIs | Alt-text, video summaries |
| `/ck:ai-artist` | Generate images via curated prompts + validation | Project assets, logos, icons |
| `/ck:remotion` | Programmatic React-based videos / animations | Code-driven video demos, social content |
| `/ck:skill-creator` | Create or update custom Claude skills with eval benchmarks | Extend ClaudeKit with own logic |
| `/ck:repomix` | Package entire repo into AI-friendly XML/JSON/MD | Full-context handoff to another AI tool |

## Commands worth borrowing for personal harness (regardless of adopting ClaudeKit)

Even if you don't install ClaudeKit, these specific patterns are reusable ideas:

- **`/ck:scout`** — parallel-agent codebase scan before writing. Implements Mnilax Rule 8 (Read before write) at scale.
- **`/ck:fix` 6-phase pipeline** — Scout → Diagnosis → Routing → Fix → Verification → Prevention. Explicit structure prevents the Mnilax-Rule-10 "lose track during multi-step" failure.
- **`/ck:journal`** — automatic "why" capture. Operationalizes ADRs (Architecture Decision Records) which Lopopolo cites in harness-engineering [[external|harness-engineering/cited-references|cited references]].
- **`/ck:scenario`** — pre-implementation what-if exploration. Captures Mnilax Rule 1 (Think Before Coding) at architectural level, not just tactical.
- **`/ck:plans-kanban`** — visualizing in-flight plans. Operationalizes Mnilax Rule 10 (Checkpoint after every significant step) across sessions, not just within.
- **`/ck:llms`** — `llms.txt` generation. Implements Lopopolo's "agent-legibility" at repo entry-point.
- **`/ck:repomix`** — full-context handoff for cross-tool. Useful when context-budget constraints (Mnilax Rule 6) require fresh-start with curated handoff.

## Key Takeaways

- 50+ commands grouped across 10 functional categories — comprehensive coverage of development lifecycle
- Heaviest density in **execution** (10 commands) and **UI/UX** (9 commands) — the maintainers' target user is a full-stack developer building production UIs
- **No native test-generation command beyond `/ck:test`** — tests are run/verified, not authored. Gap relative to Mnilax Rule 9 emphasis.
- **No explicit token-budget command** — gap relative to Mnilax Rule 6. Budget discipline is implicit (per `/ck:fix` 3-attempt halt) but not codified.
- Several commands (`/ck:scout`, `/ck:fix`, `/ck:journal`, `/ck:plans-kanban`) operationalize concepts from Mnilax + Lopopolo — these are the load-bearing pattern borrows even if you don't adopt the framework
