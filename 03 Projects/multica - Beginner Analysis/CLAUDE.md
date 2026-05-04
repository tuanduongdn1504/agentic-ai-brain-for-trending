# multica - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`multica-ai/multica`](https://github.com/multica-ai/multica) — **"The open-source managed agents platform. Turn coding agents into real teammates — assign tasks, track progress, compound skills."** Tagline: **"Your next 10 hires won't be human."** **16.2K stars, 2K forks, 2,473 commits, 43 releases (v0.2.6 latest), 121 open issues, 73 watchers**. TypeScript 53.4% + Go 43.0%. Homepage: multica.ai. **CN README** (zh-CN, 2nd CN in corpus after deer-flow).

**Tech stack — unique:** Next.js 16 web + **Electron desktop** + Go backend (Chi + sqlc + gorilla/websocket) + PostgreSQL 17 + pgvector + pnpm/Turborepo monorepo. **First native Electron desktop app in corpus.**

**Critical milestone:** **Tier 2 "Agent-as-service" multi-entrant VALIDATED at N=2** (goclaw v4 N=1 + multica v15 N=2). **Only T3 remains single-entrant** after v15 — 4 of 5 tiers now multi-entrant-validated.

**Critical Pattern #9 development:**
- T4 (gws vs notebooklm-py) bifurcated corporate/solo
- T5 (deer-flow vs autoresearch vs paperclip) — paperclip introduced community-platform hypothesis
- **T2 (goclaw vs multica) BOTH appear to fit community-platform archetype — NEITHER corporate nor solo**
- **Hypothesis refinement (v15):** Platform tiers (T2) may be HOMOGENEOUSLY community-platform while bridge/application tiers (T4/T5) bifurcate

**OpenClaw + Hermes ecosystem signal (cross-wiki):**
- Both mentioned in paperclip v14 + multica v15 (and codymaster v12 mentions OpenClaw)
- Likely emerging agent-runtime standards
- nextlevelbuilder org (goclaw v4) contributes skill to multica v15 via skills-lock.json → ecosystem-level cross-pollination

**Philosophical framing:** "Your next 10 hires won't be human" = **parallel to paperclip v14 "zero-human companies"**. Corpus now has **multiple autonomy-maximum framings** — no longer paperclip-unique. Pattern #13 (Autonomy-Framing Spectrum) reinforced.

**Phase 4b routing = T2 2-way comparison** (validates T2 multi-entrant; structurally parallel to T4 2-way v13 + T5 2-way v10; different from T5 3-way v14).

## Claude's Role

Claude là wiki maintainer, chạy bằng routine `llm-wiki-routine` v1 (**15th auto-execution — T2 multi-entrant validation + 4/5 tiers validated + ecosystem-level cross-pollination detected**):

- **Ingest sources via WebFetch** — README + README.zh-CN + CLAUDE.md (21KB largest in corpus) + AGENTS.md + skills-lock.json + CLI_AND_DAEMON + HANDOFF_ARCHITECTURE_AUDIT + SELF_HOSTING triple + CONTRIBUTING
- **Cross-reference với 14 sibling wikis** — goclaw v4 (T2 N=1 direct 2-way peer) + paperclip v14 (explicit competitor) + codymaster v12 (OpenClaw shared)
- **Phase 4b = T2 2-way comparison** — validates T2 multi-entrant; tests Pattern #9 refinement (homogeneous community-platform at platform tiers)
- **Beginner roadmap** — VN operator angle: Electron desktop + CN translation → CJK-adjacent market vs VN; less direct relevance than BMAD/codymaster; but Linear-like task management may fit Scrum context

**Prime directive:** Outcome = wiki + T2 2-way comparison + document Pattern #9 refinement (platform-tier homogeneity hypothesis) + document ecosystem-level cross-pollination (nextlevelbuilder/anthropic/vercel skills imports).

## Process — routine `llm-wiki-routine` v1

7 phases. Continuous execution. Phase 4b = **T2 2-way comparison** (structurally like T4 2-way v13).

## Key People / Organization

- **multica-ai** — GitHub org
- **No individuals named publicly** — org-only attribution (same pattern as paperclip v14)
- **No VC/startup disclosed** (similar to paperclip — possibly community-platform archetype)
- **Homepage:** multica.ai
- **X (Twitter):** @MulticaAI
- **Community:** X + GitHub (no Discord mentioned in README; possibly exists separately)
- **Cross-project:** 14 sibling wikis. This is 15th = T2 multi-entrant validation + ecosystem-level observations.

## Folder Structure

```
multica - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md
├── 00-07 folders
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ + 13-section format
- **Cross-reference 14 siblings MANDATORY** — especially goclaw v4 (T2 peer) + paperclip v14 (explicit competitor)
- **Document ecosystem cross-pollination** — skills-lock.json shows nextlevelbuilder/anthropics/vercel-labs imports
- **Pattern #9 platform-tier refinement** — if both T2 entrants community-platform, Pattern #9 is tier-dependent not cross-tier universal

## Positioning note

**multica trong taxonomy v4 (v15 update):**

| Tier | Frameworks (n=15 now) | v15 change |
|------|----------------------|------------|
| T1: Agent-as-assistant | ECC, Superpowers, gstack, GSD, BMAD, codymaster (6) | — |
| **T2: Agent-as-service** | **goclaw, multica (2 ← VALIDATED)** | **✅ Multi-entrant validation** |
| T3: Agent-as-education | course (1) | **Only single-entrant tier remaining** |
| T4: Agent-as-bridge | notebooklm-py, googleworkspace/cli (2) | — |
| T5: Agent-as-application | deer-flow, autoresearch, paperclip (3) | — |
| Outside scope | build-your-own-x (1) | — |

→ **4 of 5 tiers validated.** Only T3 pending.

### T2 2-way preview

| Axis | goclaw (v4) | multica (v15) |
|------|-------------|---------------|
| **Stars** | 8K | **16.2K** (2× larger) |
| **Tagline** | "Multi-Tenant AI Agent Platform in Go" | **"Your next 10 hires won't be human"** |
| **License** | CC BY-NC 4.0 | Not yet verified |
| **Primary language** | Go | **TypeScript 53.4% + Go 43.0%** |
| **Apps** | CLI + web | **CLI + web + Electron desktop** (first desktop in corpus) |
| **Stack** | Go + React | Next.js 16 + Electron + Go + pgvector/Postgres 17 |
| **Agent models** | Claude + Gemini | **8 models: Claude Code + Codex + OpenClaw + OpenCode + Hermes + Gemini + Pi + Cursor Agent** |
| **Multi-tenancy** | Multi-Tenant explicit | **Multi-workspace explicit** |
| **Framing** | Service-oriented | **Autonomy-maximum "next 10 hires"** |
| **VN signals** | README.vi.md + Zalo x2 | — (CN instead: README.zh-CN.md) |
| **Author org** | nextlevelbuilder | **multica-ai (different org)** |
| **Community model** | Community-platform (v4 observation) | **Community-platform (v15 observation — hypothesis refinement)** |

## Unique positioning claims của multica (từ Phase 0)

- **16.2K stars** — 4th-5th largest T-tier entrant after BMAD 45K, gws 25K, paperclip 55.9K
- **Linear-analog for agents** — "similar to Linear but with agents as first-class citizens" (from CLAUDE.md)
- **"Your next 10 hires won't be human"** — autonomy-maximum tagline
- **First Electron desktop app in corpus** — apps/web + apps/desktop
- **Heaviest Go presence** (43%) — more Go than pure-Go goclaw (100%) when measured as full stack
- **8 agent models supported** — broadest BYO-agent list in corpus (vs paperclip 6)
- **OpenClaw + Hermes both supported** — shared ecosystem with paperclip v14
- **nextlevelbuilder/ui-ux-pro-max skill imported** — goclaw's org contributes to multica
- **4 external skills locked** via skills-lock.json — first dependency-locked skill manifest in corpus
- **Chinese (zh-CN) README** — 2nd CN in corpus (after deer-flow v9)
- **No VC/corp disclosed** — parallel to paperclip + suggests community-platform archetype
- **Multi-workspace first-class** — not just multi-tenant; multiple workspaces per user
- **pgvector/Postgres 17** — AI-ready DB (embeddings-capable)
- **Cloud-first + self-hosted** — Multica Cloud SaaS available, self-hosting supported
- **Cross-platform discipline** — CLAUDE.md mandates single codebase for web + desktop via packages/views
- **TanStack Query for server state** — explicit separation from Zustand client state (hard rule)
- **WebSocket invalidation pattern** — real-time progress; events invalidate queries, never write stores
- **7 doc files at root** — CLAUDE.md (21KB) + AGENTS.md + CONTRIBUTING + CLI_AND_DAEMON + CLI_INSTALL + SELF_HOSTING × 3 + HANDOFF_ARCHITECTURE_AUDIT = **heaviest root doc load in corpus**
- **Makefile-driven dev** — `make dev` / `make check` / `make test` — mixed-language (Go + TS) makes Make appropriate
- **goreleaser** for Go binary distribution (standard Go ecosystem tool)
- **Turborepo** (first in corpus) — build orchestration for monorepo
- **Electron + Next.js hybrid** — apps/desktop is electron-vite

## Current Status

> **Last updated:** 2026-04-19
> **Status:** 🟡 Routine auto-execute IN PROGRESS — 15th LLM Wiki, T2 multi-entrant validation

### Expected milestones

- [x] Phase 0 Pre-flight (API probe, 16.2K stars, T2 N=2 validation, Pattern #9 refinement hypothesis)
- [ ] Phase 1 Setup
- [ ] Phase 2 Source ingestion (3 — README+CN / CLAUDE+AGENTS+CONTRIBUTING cluster / Skills+Architecture+skills-lock cluster)
- [ ] Phase 3 Entity pages (4 — Linear-Analog Task Management / Electron Desktop + Multi-Platform Architecture / skills-lock + Ecosystem Cross-Pollination / T2 2-way + Pattern #9 Platform-Tier Refinement + Storm Bear meta)
- [ ] Phase 4a Beginner published guide bilingual
- [ ] Phase 4b **T2 2-way comparison** (validates multi-entrant; tests Pattern #9 refinement)
- [ ] Phase 5 Iteration log v15
- [ ] Phase 6 Vault file updates
