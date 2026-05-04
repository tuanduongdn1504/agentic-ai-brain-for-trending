# (C) Log — paperclip Wiki

---

## [2026-04-19] setup | Phase 0+1 — Pre-flight + Scaffold (14th routine run)

- **Routine:** `05 Skills/llm-wiki-routine.md` v1 (14th auto-execution — **T5 3-way validation + new archetype hypothesis + alignment-theory framing**)
- **Phase 0 pre-flight (API-probe-first):**
  - ✅ WebFetch successful
  - **Stars: 55,900** — **2nd largest in corpus** (only behind build-your-own-x 491K; surpasses BMAD 45K, gws 25K)
  - Forks: 9,500 (very high engagement)
  - License: MIT
  - Default branch: master (older convention)
  - Language: TypeScript 97.4% (monorepo)
  - **2,264 commits / 6 releases / 1.1K open issues / 314 watchers** — very active, rolling-main model
  - Homepage: paperclip.ing
  - Community: Discord (discord.gg/m4HZY7xNG3), GitHub Discussions, awesome-paperclip plugin registry
  - Tagline: **"Open-source orchestration for zero-human companies"** — radical autonomy framing
  - Root folders: `.agents/`, `.claude/`, `.github/`, `cli/`, `doc/`, `docker/`, `docs/`, `evals/`, `packages/`, `patches/`, `releases/`, `report/`, `scripts/`, `server/`, `skills/`, `tests/`, `ui/`
  - Root files: README.md, **AGENTS.md**, CONTRIBUTING.md, ROADMAP.md, SECURITY.md, **adapter-plugin.md**, LICENSE, Dockerfile, package.json, pnpm-lock.yaml, pnpm-workspace.yaml, tsconfig files, vitest.config.ts, .env.example
  - **Sibling detection: 13 projects** — 6 T1 + 1 T2 + 1 T3 + 2 T4 + 2 T5 + 1 outside
  - **Domain classification: TIER 5 "Agent-as-application" ENTRANT #3 — VALIDATES T5 AT N=3**
  - **Pattern #9 test (corporate-vs-solo bifurcation):** paperclip neither clearly corporate (no VC/LLC disclosed despite 55.9K-star polish) nor solo (full-stack monorepo + polished org). **Possible "community-platform" archetype — new third category.**
  - **Phase 4b routing = T5 3-way comparison** — first triple same-tier non-T1 in corpus

- **Phase 1 scaffold:**
  - Project folder created via `mkdir -p` ("paperclip - Beginner Analysis")
  - 8 subfolders created
  - Source acquisition: WebFetch (README + AGENTS.md + ROADMAP.md + adapter-plugin.md + skills/ listing + package.json scripts)

- **WebFetch retrievals successful:**
  - README — "If OpenClaw is employee, Paperclip is company" metaphor; 9 named features; 3 bind modes; multi-model agnostic (OpenClaw/Claude Code/Codex/Cursor/Bash/HTTP); copyright 2026
  - AGENTS.md — Contributor guidelines; company-scoping discipline; contract synchronization requirement; control-plane invariants (single-assignee tasks, atomic checkout, approval gates, budget hard-stops, activity logging)
  - ROADMAP.md — Completed (plugin system, BYO external agents, org import/export, AGENTS.md config, skill discovery, scheduled routines, budget controls, review/approval); Active (Multi-user collaboration, Sandboxed execution, Artifact visibility, Durable memory, **MAXIMIZER MODE**, Work queues, Self-organizing within governance)
  - adapter-plugin.md — Runtime adapter registration refactor; mutable server + UI registries; `adapterType` + `/detect-model` routes; moving from hardcoded to dynamic
  - skills/ listing — **4 skills total** (paperclip-create-agent + paperclip-create-plugin + paperclip + para-memory-files) — LIGHTEST in recent T1/T5 wikis; orchestration-focused not skill-library-focused
  - package.json scripts — pnpm monorepo (server/ui/db/cli/packages); promptfoo integration (first in corpus); 3 OpenClaw smoke test modes (join/docker-ui/sse-standalone); Playwright E2E + multiuser-authenticated tests; release canary/stable discipline

- **Unique findings (Phase 0):**
  - **2nd largest star count in corpus** — 55.9K behind only build-your-own-x 491K
  - **No VC/LLC/startup disclosed despite 55.9K-star polish** — unusual. Full-stack + professional monorepo + Discord + plugin registry suggests funded organization but attribution is org-only ("paperclipai")
  - **FIRST alignment-theory framing** in corpus — Nick Bostrom "paperclip maximizer" name + "MAXIMIZER MODE" roadmap + "zero-human companies" tagline = explicit AI-safety theory surface
  - **FIRST "MAXIMIZER MODE" as product feature** — roadmap commits to higher-autonomy execution
  - **Direct philosophical opposite of BMAD** — "Zero-human" vs BMAD's "Human Amplification, Not Replacement". Corpus now has explicit autonomy-spectrum poles.
  - **FIRST promptfoo integration** — LLM evaluation framework built into dev workflow (scripts: `evals:smoke`)
  - **Full enterprise-grade feature set** — 9 named features (BYO Agent / Goal Alignment / Heartbeats / Cost Control / Multi-Company / Ticket System / Governance / Org Chart / Mobile Ready). Most comprehensive T5 feature breadth.
  - **Multi-model adapter system under refactor** — runtime registration vs hardcoded (adapter-plugin.md)
  - **OpenClaw companion standard** — 3 smoke test modes suggest OpenClaw is a sister project / agent standard; referenced also in codymaster v12 as install target; adapter-plugin.md mentions moving from hardcoded to dynamic
  - **Lightest skill layer** of multi-skill frameworks — only 4 skills (vs codymaster 79, gws 110); focus is orchestration, not skill breadth
  - **TypeScript 97.4% monorepo** — most TS-heavy T5; parallel to gws's Rust-purity in T4
  - **3 bind modes (local/LAN/tailnet)** — deployment flexibility via Tailscale tailnet
  - **Embedded PGlite (dev) + external Postgres (prod)** — thoughtful DB strategy
  - **Governance-first architecture** — approval gates + budget hard-stops + audit log + manual override = constitutional design (not afterthought)
  - **"Paperclip commit metrics" script** — meta: they measure their own dev velocity
  - **Canary + stable release channels** — mature discipline parallel to BMAD v11's `@next`/`@latest`

- **Pattern #9 TEST at T5 N=3 — hypothesis:**
  - v10 observed T5 N=2 bifurcation: deer-flow corporate-generalist vs autoresearch solo-specialist
  - v13 confirmed same pattern at T4 N=2: gws official-corporate-broad vs notebooklm-py unofficial-solo-narrow
  - v14 paperclip doesn't fit cleanly into either existing T5 subcategory
    - NOT corporate (no backing disclosed)
    - NOT solo (55.9K stars + polish + full team signals)
  - **Hypothesis: "community-platform" archetype emerges** — third category alongside corporate + solo
  - Will formalize in Phase 4b T5 3-way comparison
  - **If confirmed:** Pattern #9 refined from bifurcation → triple-categorization
  - **If falsified:** paperclip is stealth-corporate (hidden commercial entity); Pattern #9 bifurcation holds

- **Source strategy:**
  1. README summary (positioning + features + architecture + governance + BYO Agent)
  2. AGENTS + ROADMAP + adapter-plugin cluster (contributor discipline + trajectory + adapter refactor + MAXIMIZER MODE)
  3. Skills + Architecture + package.json cluster (4 skills + monorepo + stack + promptfoo + smoke tests)

- **Phase 0+1 status:** ✅ COMPLETE
- **Next:** Phase 2 source summaries

---

## [2026-04-19] complete | Phases 2-6 shipped

### Phase 2 — 3 source summaries
- ✅ `(C) README summary.md` — "zero-human" framing + 9 features + 3 bind modes + BYO Agent + governance + Bostrom reference
- ✅ `(C) AGENTS + ROADMAP + adapter-plugin cluster summary.md` — 5 control-plane invariants + MAXIMIZER MODE + adapter refactor + PR template discipline
- ✅ `(C) Skills + Architecture + package.json cluster summary.md` — monorepo + PGlite + promptfoo + 3-channel release + 6 test categories + only 4 skills (lightweight orchestrator)

### Phase 3 — 4 entity pages
- ✅ `(C) Zero-Human Companies Orchestration + Governance Layer.md` — company-as-primitive + 4 governance + 5 invariants architectural constitution
- ✅ `(C) BYO Agent Adapter System + OpenClaw Standard.md` — runtime adapter registration + OpenClaw 3 modes + cross-wiki references
- ✅ `(C) Paperclip-Maximizer Framing + Alignment-Theory Surface.md` — **Storm Bear philosophical meta-entity** (Bostrom context + architectural response + tension with Scrum coaching role)
- ✅ `(C) T5 3-Way Validation + Community-Platform Archetype Hypothesis.md` — **Tier meta-entity** (Pattern #9 test + 3 resolutions A/B/C + community-platform archetype formalization)

### Phase 4a — Beginner bilingual guide with ethical framing
- ✅ `(C) paperclip - Huong dan cho nguoi moi.md` (~600 lines, 10 parts)
- NEW pattern in corpus: ⚠️ ethical framing section BEFORE technical content

### Phase 4b — T5 3-way comparison (first triple non-T1)
- ✅ `(C) Tier 5 3-way comparison.md` (~750 lines, 20 axes, Pattern #9 tested, 3 new pattern candidates #13-15)
- First 3-way same-tier comparison non-T1 in corpus
- Milestone: corpus transitions from observation to pattern-TESTING

### Phase 5 — Iteration log v14
- ✅ `04 Reviews/(C) 2026-04-19 v14 build learnings.md` — 8 new routine v2 action items (cumulative 69)

### Phase 6 — Vault sync
- ✅ Project index updated to all ✅
- ✅ This log appended
- ✅ Root `CLAUDE.md` — paperclip project entry added with ethical framing
- ✅ Root `GOALS.md` — v14 milestone + version log entry

### Phase 2-6 unique findings
- **T5 validates at N=3** — FIRST non-T1 tier to reach triple
- **Pattern #9 gets FIRST pattern-TEST** (prior observations only)
- **Community-platform archetype hypothesis** emerges from paperclip's neither-corp-nor-solo profile
- **3 resolutions framework** (A refined / B invalidated / C stealth-corporate) — honest empirical uncertainty
- **Alignment-theory framing** documented as corpus-first (Bostrom paperclip-maximizer direct reference + MAXIMIZER MODE roadmap)
- **Philosophical pole documentation** — BMAD v11 human-centric vs paperclip v14 zero-human = explicit autonomy spectrum poles
- **3 new pattern candidates** (#13 autonomy-framing spectrum / #14 alignment-theory visibility / #15 governance-depth correlation)
- **5 invariants + 4 primitives** = first constitutional governance architecture in corpus
- **Corpus transitions from descriptive to predictive** — pattern library now testable

### Velocity
~2h for all of Phases 2-6. Stable with v6-v13 (**9 consecutive wikis at ~2h plateau**).

### v14 status: ✅ COMPLETE — 13 files, T5 validated at N=3, Pattern #9 tested, 3 pattern candidates, philosophical framing preserved

---
