# (C) Log — multica Wiki

---

## [2026-04-19] setup | Phase 0+1 — Pre-flight + Scaffold (15th routine run)

- **Routine:** `05 Skills/llm-wiki-routine.md` v1 (15th auto-execution — **T2 multi-entrant validation + 4/5 tiers validated + ecosystem cross-pollination**)
- **Phase 0 pre-flight:**
  - ✅ WebFetch successful
  - **Stars: 16,200** — 4-5th largest T-tier entrant (after BMAD 45K, paperclip 55.9K, gws 25K)
  - Forks: 2,000
  - License: LICENSE file present (content not extracted Phase 0 — likely MIT)
  - Default branch: main
  - Languages: TypeScript 53.4% + Go 43.0% + MDX 1.1% + Shell/CSS/JS 1.9%
  - **2,473 commits / 43 releases / v0.2.6 latest / 121 open issues / 73 watchers** — active
  - Homepage: multica.ai
  - Community: X (@MulticaAI) + GitHub (no Discord in README)
  - Tagline: **"Your next 10 hires won't be human"** — autonomy-maximum framing (parallel to paperclip v14)
  - Description: "open-source managed agents platform. Turn coding agents into real teammates — assign tasks, track progress, compound skills"
  - **Non-EN READMEs:** README.zh-CN.md (Simplified Chinese — 2nd CN in corpus after deer-flow v9)
  - **38 root items** — heaviest root doc load in corpus (7 substantial .md docs)
  - Root structure: .github/ + apps/ (web + desktop) + docker/ + docs/ + e2e/ + packages/ + scripts/ + server/ (Go) + 7 .md docs + Dockerfile×2 + docker-compose×2 + Makefile + turbo.json + .goreleaser.yml + pnpm-workspace.yaml + **skills-lock.json (NOVEL)**
  - **Sibling detection: 14 projects** — 6 T1 + 1 T2 (goclaw) + 1 T3 + 2 T4 + 3 T5 + 1 outside
  - **Domain classification: TIER 2 "Agent-as-service" ENTRANT #2 — VALIDATES T2 MULTI-ENTRANT**
  - **Phase 4b routing = T2 2-way comparison** — structurally like T4 2-way (v13) + T5 2-way (v10); different from T5 3-way (v14)

- **Phase 1 scaffold:**
  - Project folder created via `mkdir -p` ("multica - Beginner Analysis")
  - 8 subfolders created
  - Source acquisition: WebFetch (README + README.zh-CN + CLAUDE.md + AGENTS.md + skills-lock.json + root listing)

- **WebFetch retrievals successful:**
  - README (9KB) — "Your next 10 hires won't be human" tagline, Multica vs Paperclip comparison section, Quick Install (Homebrew/script/PowerShell), 8-agent BYO list
  - README.zh-CN.md (8KB) — Chinese translation; quality assessment: **machine-translated** (like BMAD VN, codymaster VN). No CN-specific models (Zhipu/Qwen/DeepSeek). No WeChat/QQ/Zhihu channels.
  - **CLAUDE.md (21,846 B — LARGEST IN CORPUS)** — role definition + architecture + state management rules + package boundaries + development commands + testing requirements + coding conventions + cross-platform rules + desktop-specific rules + verification workflow. Node 22 / Go 1.26.1 / pgvector-Postgres 17.
  - AGENTS.md (1,892 B) — "pointer with content" — says see CLAUDE.md but includes substantial architectural notes too. Not pure pointer like paperclip/gws.
  - skills-lock.json — **FIRST skill dependency manifest in corpus**. 4 external skills locked with SHA-256:
    - frontend-design (anthropics/skills — Anthropic official)
    - shadcn (shadcn/ui)
    - ui-ux-pro-max (**nextlevelbuilder** — same org as goclaw v4!)
    - web-design-guidelines (vercel-labs/agent-skills)

- **Unique findings (Phase 0):**
  - **T2 MULTI-ENTRANT VALIDATED at N=2** — goclaw v4 (N=1) + multica v15 (N=2). **4 of 5 tiers now multi-entrant-validated; only T3 single-entrant remaining.**
  - **Pattern #9 refinement hypothesis (v15):** Both T2 entrants appear to fit **community-platform archetype** (no VC/corp disclosed). If confirmed, Pattern #9 becomes tier-dependent:
    - T2 platform tier = homogeneous community-platform
    - T4/T5 bridge/application = can bifurcate corporate/solo
    - T1 assistant = widest diversity (6 archetypes at N=6)
  - **Ecosystem cross-pollination detected** — multica's skills-lock.json imports from:
    - anthropics/skills (Anthropic's official skill registry)
    - shadcn/ui (popular UI lib)
    - **nextlevelbuilder/ui-ux-pro-max-skill** (SAME ORG as goclaw v4)
    - vercel-labs/agent-skills (Vercel official)
  - **nextlevelbuilder org connection** = goclaw's parent + contributes to multica → emerging ecosystem around this org
  - **Linear-analog framing** — CLAUDE.md: "AI-native task management platform (similar to Linear but with agents as first-class citizens)". First Linear-analog in corpus.
  - **Electron desktop app** — first native desktop app in corpus (apps/desktop + electron-vite)
  - **First skills-lock.json** — dependency-locked skill manifest. NEW corpus pattern. SHA-256 integrity verification.
  - **Largest CLAUDE.md** at 21KB — substantial Claude Code instructions with hard architectural constraints (package boundaries + state management rules + cross-platform discipline)
  - **8 agent models supported** — broadest BYO-agent list in corpus (vs paperclip 6, codymaster 79 skills but fewer models)
  - **OpenClaw + Hermes cross-ecosystem signal** — both mentioned in paperclip v14 AND multica v15; Hermes also in paperclip fork note. Emerging agent-runtime standards.
  - **Autonomy-maximum framing parallel to paperclip** — "Your next 10 hires won't be human" (multica) vs "Open-source orchestration for zero-human companies" (paperclip). Pattern #13 (Autonomy-Framing Spectrum) reinforced; no longer paperclip-unique.
  - **Direct competitor positioning** — multica README has "Multica vs Paperclip" section. Competes on: team focus + multi-user roles + cloud-first + lightweight governance vs paperclip's heavier org + heavier governance.
  - **Turborepo + pnpm workspaces** — first Turborepo in corpus
  - **goreleaser** for Go binary distribution — standard Go release tool
  - **pgvector/Postgres 17** — AI-ready DB with embeddings (first in corpus)
  - **Go 43%** — heaviest Go stack in T-tier entrants after pure-Go goclaw
  - **Cloud-first + self-hosted dual model** — Multica Cloud SaaS + self-hosting option (parallel to BMAD's marketplace model evolution v11)
  - **Heaviest root doc load** — 7 substantial .md docs (CLAUDE/AGENTS/CONTRIBUTING/CLI_AND_DAEMON/CLI_INSTALL/SELF_HOSTING×3/HANDOFF_ARCHITECTURE_AUDIT)

- **Source strategy:**
  1. README + zh-CN summary (positioning + features + install + Multica vs Paperclip + CN translation quality)
  2. CLAUDE + AGENTS + CONTRIBUTING cluster summary (architectural discipline + package boundaries + state management)
  3. Skills + Architecture + skills-lock cluster summary (8 agents + 4 external skills + Electron + Go + pgvector)

- **Phase 0+1 status:** ✅ COMPLETE
- **Next:** Phase 2 source summaries

---

## 2026-04-19 Phase 2-6 complete

### Phase 2 — 3 cluster source summaries shipped ✅

- [[(C) README + zh-CN summary]] — positioning + tagline + features + Multica vs Paperclip + honest CN translation verdict (machine-translation minimal polish)
- [[(C) CLAUDE + AGENTS + CONTRIBUTING cluster summary]] — 21KB CLAUDE.md (largest in corpus), 5 non-negotiable package boundaries, state management rules, cross-platform rules, desktop-specific rules
- [[(C) Skills + Architecture + skills-lock cluster summary]] — skills-lock.json verbatim, 4 external skills, 8 agent models, hybrid local-daemon+cloud architecture, 8 corpus-firsts inventoried

### Phase 3 — 4 entity pages (13-section canonical) ✅

- [[(C) Linear-Analog Task Management for Agents]] — core product: atomic lifecycle (enqueue→claim→start→complete/fail) + WebSocket invalidation pattern + Linear-analog positioning
- [[(C) Electron Desktop + Multi-Platform Architecture]] — first Electron in corpus + 5 cross-platform rules + 5 desktop-specific rules + dual-app discipline
- [[(C) skills-lock + Ecosystem Cross-Pollination]] — corpus-first dependency-locked skill manifest + nextlevelbuilder cross-project + Pattern #16 + #17 + #18 candidates
- [[(C) T2 2-way Validation + Pattern 9 Platform-Tier Refinement + Storm Bear]] — tier meta + 7-criteria community-platform fit (goclaw 6.5/7, multica 7/7) + Pattern #9 refinement (55% prob)

### Phase 4a — beginner guide ✅

- [[../03 Published/(C) multica - Huong dan cho nguoi moi]] — bilingual VN/EN, 12 parts, ethical framing note, 4-week roadmap, Storm Bear relevance verdict (medium)

### Phase 4b — T2 2-way comparison ✅

- [[../03 Published/(C) Tier 2 2-way comparison]] — 20-axis goclaw vs multica + Pattern #9 refinement (tier-dependent resolution) + 3 new pattern candidates + Storm Bear strategic implications

### Phase 5 — iteration log ✅

- [[../04 Reviews/(C) 2026-04-19 v15 build learnings]] — 8 new routine v2 action items, CRITICAL escalation, 10-wiki velocity plateau confirmed

### Phase 6 — vault sync ✅

- Project `(C) index.md` → all ✅
- Project `(C) log.md` → this entry appended
- Root `CLAUDE.md` → multica project entry added
- Root `GOALS.md` → v15 session milestone + version log

### Summary

- **Wikis built:** 15 total (15/15 this session for v15)
- **T2 multi-entrant VALIDATED** (N=2: goclaw + multica)
- **4/5 tiers validated** — only T3 remains N=1
- **Pattern #9 refined** to tier-dependent (55% prob)
- **3 new pattern candidates** (#16-#18)
- **Velocity plateau 10 consecutive wikis** (~2h v6-v15)
- **Routine v2 escalated to CRITICAL** (68+ backlog)

**Phase 2-6 status:** ✅ COMPLETE

