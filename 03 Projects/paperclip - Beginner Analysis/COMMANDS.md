# COMMANDS — paperclip Wiki

## Build wiki
- "Chạy routine" → follow `05 Skills/llm-wiki-routine.md` v1
- "Phase 2-6" → proceed phase by phase

## Source acquisition
- WebFetch: `https://raw.githubusercontent.com/paperclipai/paperclip/master/<path>`
- Key files fetched: README.md, AGENTS.md, ROADMAP.md, adapter-plugin.md, skills/ listing, package.json scripts
- GitHub repo: github.com/paperclipai/paperclip
- Homepage: paperclip.ing
- Discord: discord.gg/m4HZY7xNG3
- Install references:
  - `npx paperclipai onboard --yes` (quick)
  - `git clone + pnpm install && pnpm dev` (manual, requires Node 20+ + pnpm 9.15+)

## Cross-project
- T5 peers for 3-way comparison:
  - `../deer-flow - Beginner Analysis/02 Wiki/(C) index.md` (v9 N=1 ByteDance corporate-generalist)
  - `../autoresearch - Beginner Analysis/02 Wiki/(C) index.md` (v10 N=2 Karpathy solo-specialist)
- T5 2-way precedent: `../autoresearch - Beginner Analysis/03 Published/(C) T5 2-way comparison + Karpathy meta-reflection.md`
- Taxonomy v4 (5-tier): `../deer-flow - Beginner Analysis/03 Published/(C) Agent framework taxonomy v4 - 5 tier with application.md`
- Routine: `../../05 Skills/llm-wiki-routine.md`

## Pattern #9 status heading into v14

| Tier | Validation | Pattern #9 status |
|------|-----------|-------------------|
| T4 (v13) | N=2 | ✅ Confirmed (gws corporate vs notebooklm-py solo) |
| T5 (v10) | N=2 | Initial observation (deer-flow corporate vs autoresearch solo) |
| T5 (v14) | **N=3** | **Testing — paperclip's archetype TBD; may refine bifurcation to triple-categorization** |

## Key Phase 0 findings

- 55.9K stars = 2nd largest in corpus
- No VC/LLC/startup disclosed — unusual for polish + scale
- "paperclipai" org on GitHub; no named individuals
- TypeScript 97.4% monorepo with Express + React + Drizzle + Postgres
- promptfoo for LLM evals (new in corpus)
- OpenClaw adapter 3 runtime modes (join/docker-ui/sse-standalone)
- Direct Nick Bostrom paperclip-maximizer name + "MAXIMIZER MODE" roadmap = unique alignment-theory surface in corpus
