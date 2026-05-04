# (C) Index — multica Wiki

## 🎯 Project status (2026-04-19)

- ✅ Phase 0: Pre-flight — PASSED (API probe, 16.2K stars, T2 N=2 validation, Pattern #9 refinement hypothesis)
- ✅ Phase 1: Setup
- ✅ Phase 2: Source ingestion (3 cluster summaries)
- ✅ Phase 3: Entity pages (4)
- ✅ Phase 4a: Beginner published guide
- ✅ Phase 4b: **T2 2-way comparison** (validated multi-entrant + Pattern #9 refinement)
- ✅ Phase 5: Iteration log v15
- ✅ Phase 6: Vault file updates

**Repo:** multica-ai/multica
- **Description:** "The open-source managed agents platform. Turn coding agents into real teammates — assign tasks, track progress, compound skills."
- **Tagline:** "Your next 10 hires won't be human" (CN: "你的下一批员工，不是人类")
- **Stats:** 16,200 stars, 2,000 forks, 2,473 commits, 43 releases (v0.2.6), 121 open issues, 73 watchers
- **Languages:** TypeScript 53.4% + Go 43.0% + MDX 1.1%
- **License:** (in LICENSE file, not extracted in Phase 0)
- **Author:** "multica-ai" org (no individuals disclosed)
- **Homepage:** multica.ai
- **Community:** X (@MulticaAI), GitHub
- **Routine:** `05 Skills/llm-wiki-routine.md` v1 — 15th auto-execution, T2 validation
- **Domain:** **Tier 2 "Agent-as-service" entrant #2** (validates T2 multi-entrant)
- **Unique:** First Electron desktop app + first skills-lock.json dependency manifest + 21KB CLAUDE.md (largest in corpus) + 8 agent models supported (broadest BYO); Linear-analog positioning

## Sources (planned)

| Page | Summary | Status |
|------|---------|--------|
| [[(C) README + zh-CN summary]] | "Your next 10 hires won't be human" + features + install + Multica vs Paperclip + CN translation quality | ✅ |
| [[(C) CLAUDE + AGENTS + CONTRIBUTING cluster summary]] | Tri-file agent docs pattern + hard architectural constraints + package boundaries + state management rules | ✅ |
| [[(C) Skills + Architecture + skills-lock cluster summary]] | 8 agent models + 4 external locked skills + Electron desktop + Go backend + pgvector | ✅ |

## Concepts (planned)

- **Linear-analog for agents** — task management with agents as first-class citizens
- **Managed agents platform** — T2 positioning (SaaS + self-hosted)
- **Task lifecycle** — enqueue → claim → start → complete/fail (atomic state machine)
- **Multi-workspace** — workspace-level isolation (per-workspace agents + issues + settings)
- **Compound skills** — "every solution becomes a reusable skill for the whole team"
- **BYO agent (8 models)** — Claude Code + Codex + OpenClaw + OpenCode + Hermes + Gemini + Pi + Cursor Agent
- **Electron desktop app** — apps/desktop with electron-vite (first in corpus)
- **pgvector/Postgres 17** — AI-ready DB with embeddings
- **sqlc** — Go SQL codegen
- **Turborepo** — monorepo build orchestration
- **Cross-platform discipline** — packages/views shared between web + desktop
- **TanStack Query + Zustand separation** — server state vs client state (hard rule)
- **WebSocket invalidation pattern** — real-time; WS events invalidate queries, never write stores
- **skills-lock.json** — first skill dependency manifest with SHA-256 hashes
- **Ecosystem cross-pollination** — imports skills from nextlevelbuilder (goclaw team) + anthropics + shadcn + vercel-labs

## Entities (planned)

| Page | Type | Sources | Status |
|------|------|---------|--------|
| [[(C) Linear-Analog Task Management for Agents]] | Core product | README + CLAUDE.md + task lifecycle | ✅ |
| [[(C) Electron Desktop + Multi-Platform Architecture]] | Novel architecture | CLAUDE.md packages + apps section | ✅ |
| [[(C) skills-lock + Ecosystem Cross-Pollination]] | Novel pattern | skills-lock.json + cross-wiki references | ✅ |
| [[(C) T2 2-way Validation + Pattern #9 Platform-Tier Refinement + Storm Bear]] | **Tier meta + Storm Bear** | T2 comparison + Pattern #9 history | ✅ |

## Roadmaps / Published

- ✅ [[../03 Published/(C) multica - Huong dan cho nguoi moi]] — beginner bilingual guide
- ✅ [[../03 Published/(C) Tier 2 2-way comparison]] — T2 multi-entrant validated; Pattern #9 refinement supported (platform-tier homogeneity)

## Cross-project siblings (14 total)

- **T2 peer (1) — 2-way target:**
  - `../../goclaw - Beginner Analysis/02 Wiki/(C) index.md` (v4 T2 N=1)
- **Explicit competitor (v14):**
  - `../../paperclip - Beginner Analysis/02 Wiki/(C) index.md` (T5; "Multica vs Paperclip" section in multica README)
- T1: ECC, Superpowers, gstack, GSD, BMAD, codymaster (6)
- T3: course (1)
- T4: notebooklm-py, googleworkspace/cli (2)
- T5: deer-flow, autoresearch, paperclip (3)
- Outside: build-your-own-x (1)

## Logs

- [[(C) log]]
