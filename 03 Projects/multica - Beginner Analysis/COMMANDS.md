# COMMANDS — multica Wiki

## Build wiki
- "Chạy routine" → follow `05 Skills/llm-wiki-routine.md` v1
- "Phase 2-6" → proceed phase by phase

## Source acquisition
- WebFetch: `https://raw.githubusercontent.com/multica-ai/multica/main/<path>`
- Key files fetched:
  - README.md (9KB) + README.zh-CN.md (8KB)
  - CLAUDE.md (21KB — largest in corpus!)
  - AGENTS.md (2KB — pointer with content)
  - skills-lock.json (first skill dependency lock in corpus)
  - Root listing (38 items)
- GitHub repo: github.com/multica-ai/multica
- Homepage: multica.ai
- X: @MulticaAI
- Install: `brew install multica-ai/tap/multica` (Homebrew) / install script / PowerShell (Windows)

## Cross-project
- T2 peer for 2-way comparison: `../goclaw - Beginner Analysis/02 Wiki/(C) index.md` (v4 T2 N=1)
- **Explicit competitor:** `../paperclip - Beginner Analysis/02 Wiki/(C) index.md` (v14 T5 — README has "Multica vs Paperclip" section)
- Cross-ecosystem: `../codymaster - Beginner Analysis/` (mentions OpenClaw)
- Taxonomy v4 (5-tier): `../deer-flow - Beginner Analysis/03 Published/(C) Agent framework taxonomy v4 - 5 tier with application.md`
- T4 2-way precedent: `../googleworkspace-cli - Beginner Analysis/03 Published/(C) Tier 4 2-way comparison.md`
- Routine: `../../05 Skills/llm-wiki-routine.md`

## Pattern #9 test status heading into v15

| Tier | Validation | Pattern #9 status |
|------|-----------|-------------------|
| T4 v13 | N=2 | ✅ Bifurcation (gws corp vs notebooklm solo) |
| T5 v10 | N=2 | Initial bifurcation (deer-flow corp vs autoresearch solo) |
| T5 v14 | N=3 | ⚠️ Tested — paperclip ambiguous, community-platform hypothesis |
| **T2 v15** | **N=2** | **Testing — both goclaw + multica appear community-platform (no corp, no solo)** |

**v15 test result (predicted):**
If both T2 entrants community-platform → Pattern #9 refined to tier-dependent:
- T2 platform tier = homogeneous community-platform
- T4/T5 bridge/application = can bifurcate corporate/solo
- T1 assistant = widest diversity

## Key Phase 0 findings

- 16.2K stars = 4-5th in corpus
- TypeScript 53.4% + Go 43.0% (polyglot)
- First Electron desktop app in corpus
- First skills-lock.json dependency manifest
- 21KB CLAUDE.md = largest in corpus
- 8 agent models supported (BYO broadest)
- OpenClaw + Hermes cross-ecosystem signal (paperclip parallel)
- nextlevelbuilder skill imported → goclaw-team ecosystem contribution
