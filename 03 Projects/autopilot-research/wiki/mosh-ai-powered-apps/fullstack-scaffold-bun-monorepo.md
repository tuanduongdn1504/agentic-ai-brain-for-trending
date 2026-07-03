# Full-Stack Scaffold — Bun Monorepo

## Source

Video PtETUYa3i2Q, chapters "Setting Up a Modern Full-Stack Project" (47:07) → "Automating Pre-Commit Checks With Husky" (1:31:02). Repo ground truth: `mosh-hamedani/ai-powered-apps-course` (packages/client + packages/server confirmed).

## Stack decisions

- **Bun** (bun.sh, v1.2.17 in video) as runtime + package manager + task runner + TS transpiler in one — runs `.ts` natively, replaces npm/ts-node/nodemon. `bun add`, `bun add -d`, `bun run --watch`.
- **Not Next.js** — deliberate plain Express + React/Vite split so front/back responsibilities stay visible (contrast: JSM builds on Next.js 16 — [[external|Storm Bear: jsm-six-file-context]]).
- Monorepo via **Bun workspaces**: root `package.json` with `workspaces: ["packages/*"]`; `packages/server` (Express + TypeScript + @types/express) and `packages/client` (`bun create vite .` → React + TS). Single shared root `node_modules`.

## Wiring

- **Env:** dotenv; `.env` gitignored + `.env.example` committed (names, no values); `require('dotenv').config()` at entry-top; `.env` changes need a restart (`--watch` ignores it).
- **Ports/proxy:** server on `process.env.PORT ?? 3000`; Vite dev server 5173; `vite.config.ts` → `server.proxy: { '/api': 'http://localhost:3000' }` so the client fetches `/api/*` with no CORS pain in dev.
- **Run both:** `concurrently` at root — `dev: 'concurrently "bun run --cwd packages/server dev" "bun run --cwd packages/client dev"'` → one `bun run dev`.
- **UI:** Tailwind (`bun add -D tailwindcss @tailwindcss/vite` + Vite plugin) + **shadcn/ui** (CLI init, tsconfig path aliases across three config files, theme pick, `bunx shadcn@latest add button`). Repo confirms React 19 + React Query on the client.
- **Quality gates:** Prettier (`.prettierrc`: singleQuote/semi/trailingComma/printWidth/tabWidth + `.prettierignore` + format-on-save) and **Husky + lint-staged** (`bunx husky init` → `.husky/pre-commit` runs lint-staged → `.lintstagedrc` maps file patterns to commands) — every commit auto-formats staged files.

## Key Takeaways

- The scaffold IS a harness: env discipline, proxy isolation, one-command dev loop, and pre-commit formatting are all agent-legibility wins too (a codebase this predictable is easy for coding agents to operate in — cf. [[external|Storm Bear: harness-engineering]]).
- Bun-workspaces + `--cwd` scripts is the lightest-weight JS monorepo recipe in the corpus (vs Turborepo/Nx everywhere else).
- `.env.example` as committed documentation-of-secrets-shape is the exact pattern hireui's cost-optimization spec assumes.
- The Vite `/api` proxy pattern is dev-only — the video defers production topics (CORS, deploy) entirely; flag when reusing.
- Cross-links: [[chatbot-validation-and-errors]] (what gets built on this scaffold), [[the-originals]] (repo layout).
