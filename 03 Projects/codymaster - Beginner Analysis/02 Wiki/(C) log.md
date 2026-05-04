# (C) Log — codymaster Wiki

---

## [2026-04-19] setup | Phase 0+1 — Pre-flight + Scaffold (12th routine run)

- **Routine:** `05 Skills/llm-wiki-routine.md` v1 (12th auto-execution — **T1 re-opening + VN-author-native discovery**)
- **Phase 0 pre-flight (API-probe-first):**
  - ✅ GitHub API HTTP 200
  - **Stars: 38** — smallest analyzed to date (tiny by corpus standard)
  - Forks: 21 (high-for-star-ratio)
  - License: **ISC** — unusual (first ISC in corpus vs predominant MIT)
  - Default branch: main
  - Languages: Python 43.8% + JS 18.5% + HTML 13.8% + TS 13.8% + CSS 6.1% + Shell 3.8% (polyglot)
  - **11 git tags = 11 releases**, 120 commits
  - **6 language READMEs:** EN + VI + ZH + RU + KO + HI (**most multi-lingual in corpus**)
  - Root folders: `.agent-tasks/`, `.agent/skills/`, `.claude-plugin/`, `.claude/`, `.codegraph/`, `.codex/`, `.cursor-plugin/`, `.github/`, `.opencode/`, `adapters/`, `assets/`, `codybench/`, `commands/`, `content-output/`, `dist/`, `docs/`, `openspec/changes/`, `projects/`, `public/dashboard/`, `scripts/`, `skills/`, `src/`, `templates/`, `test/`
  - Config: `.env.example`, `.gitleaks.toml`, `.mcp.json`, `.project-identity.json`, `.snyk`
  - **Sibling detection: 11 projects** — 5 T1 + 1 T2 + 1 T3 + 1 T4 + 2 T5 + 1 outside
  - **Domain classification: TIER 1 ENTRANT #6 — RE-OPENS T1 after v11 closure at N=5**
  - **Justification for re-opening:** codymaster clears "genuinely different" bar via 5 signals (VN-authored / 79 skills largest / 8+ platforms broadest / novel primitives 5-Tier+Smart-Spine+CodeGraph / empirical SkillsBench research)
  - **Phase 4b routing = Tier 1 6-way comparison** (updates v11's 5-way)

- **Phase 1 scaffold:**
  - Project folder created via `mkdir -p`
  - 8 subfolders created
  - Source acquisition: WebFetch (README + README-vi + package.json + plugin.json + skills/ listing + commands/ listing + docs/ listing)

- **WebFetch retrievals successful:**
  - README.md — Vibe Coding Framework, Tody Le author, 60+ skills + 20+ commands claims, 5-Tier Memory + Smart Spine + CodeGraph + Self-Healing + Cloud Brain, SkillsBench +18.6pp
  - README-vi.md — machine-translated from EN, Tody Le author (Vietnamese), "Code Đi" tagline, no VN-specific examples
  - package.json — name codymaster, version 5.1.0, ISC license, author todyagent <aitodyle@gmail.com>, bin: cm + codymaster
  - plugin.json — name "cm", version 5.0.0, description "68+ AI agent skills", author Tody Agent
  - skills/ listing — **79 folders** (not 60+ as README)
  - commands/ listing — **11 .md files** (not 20+ as README)
  - docs/ listing — 16 dirs + 4 files (rich doc structure)
  - CLAUDE.md — **404 not found** (no CLAUDE.md at repo root; unusual for Claude Code plugin)

- **Unique findings (Phase 0 corrections caught pre-emptively):**
  - **79 skills actual vs 60+ README / 68+ plugin.json** — marketing UNDERSELLS (surprising direction)
  - **11 commands actual vs 20+ README** — marketing OVERSELLS (the typical direction)
  - **Version skew:** package.json 5.1.0 / plugin.json 5.0.0 / website v6.0.0 / 11 git tags — rolling publish channels, different per artifact
  - **First VN-AUTHORED framework** — Tody Le is Vietnamese author. Previous v11 BMAD was VN-translated (EN-origin). codymaster is EN-primary-written but VN-authored. Distinct category.
  - **First ISC license** — all prior T1 were MIT. ISC is permissive but different lineage.
  - **"Can't code" author positioning** — Tody Le explicit claim. Framework designed by product-lead who doesn't write code, for same audience. Radical.
  - **"Code Đi" tagline** in VN — Vietnamese "Go code!" — informal, youth-culture-adjacent
  - **6 languages = most multi-lingual** in corpus (vs BMAD 3: EN/VI/CN)
  - **SkillsBench empirical research** — first T1 framework to publish empirical benchmark (+18.6pp with 2-3 dynamic skills vs 4+ static)
  - **8+ platforms distribution** — broadest multi-harness T1 (Claude Desktop / Claude Code / Cursor / Gemini / OpenCode / OpenClaw / Codex / Antigravity / npm global+local)
  - **5-Tier Memory architecture** — deepest memory model in T1 (Sensory/Working/Long-term/Semantic/Structural with Ebbinghaus decay)
  - **Smart Spine** — SQLite+FTS5 + progressive L0/L1/L2 + cm:// URI + context bus + MCP 18 tools + 200k budget. Most engineered brain in T1.
  - **CodeGraph** — AST-based ~95% token compression. Novel structural memory approach.
  - **Cloud Brain NotebookLM sync** — cross-machine "soul" + auto podcasts/flashcards. Integrates T4-tier (notebooklm-py) functionality into T1-framework.
  - **Self-Healing Skills FIX/DERIVED/CAPTURED** — auto-repair + auto-graduation of recurring tasks. Novel ops primitive.
  - **Full Lifecycle scope** — Idea→Plan→Design→Test→Code→Debug→Quality→Security→Deploy→Monitor→Document→Learn. Broadest T1 lifecycle coverage.
  - **No CLAUDE.md at repo root** — unusual for Claude Code plugin; likely `.claude-plugin/` manifest covers this role
  - **Author matches Storm Bear peer profile** — Vietnamese + Head of Product + non-coder who ships via AI. Storm Bear (VN + dev + Scrum coach) is peer-category.

- **Source strategy:**
  1. README + README-vi summary (positioning + VN-author + tagline + reality corrections)
  2. Novel Primitives cluster summary (5-Tier Memory + Smart Spine + CodeGraph + Self-Healing + Cloud Brain + SkillsBench)
  3. Skills + Commands + Lifecycle cluster summary (79 skills 8 domains + 11 commands + Full Lifecycle + 4-Layer Protection)

- **Phase 0+1 status:** ✅ COMPLETE
- **Next:** Phase 2 source summaries

---

## [2026-04-19] complete | Phases 2-6 shipped

### Phase 2 — 3 source summaries
- ✅ `(C) README + VN summary.md` — Vibe Coding positioning, Tody Le VN author, 3 numeric corrections (79 skills / 11 commands / version skew), honest VN quality assessment (machine-translated despite VN author)
- ✅ `(C) Novel Primitives cluster summary.md` — 5-Tier Memory + Smart Spine + CodeGraph + Self-Healing + Cloud Brain + SkillsBench — 8 novel primitives clustered
- ✅ `(C) Skills + Commands + Lifecycle cluster summary.md` — 79 skills 8 domains + 11 commands + Full Lifecycle + 4-Layer Protection

### Phase 3 — 4 entity pages (13-section canonical)
- ✅ `(C) 79 Skills 8 Domains + 11 Commands Architecture.md`
- ✅ `(C) 5-Tier Memory + Smart Spine + CodeGraph.md`
- ✅ `(C) Self-Healing Skills + SkillsBench Dynamic Selection.md`
- ✅ `(C) VN-Author Native + Tody Le + Storm Bear Peer-Relevance.md` — Storm Bear meta-entity (peer-category)

### Phase 4a — Beginner VN-first bilingual guide
- ✅ `(C) codymaster - Huong dan cho nguoi moi.md` (~600 lines, 10 parts)
- First VN-FIRST guide in corpus (prior 11 were bilingual parallel)

### Phase 4b — T1 6-way comparison
- ✅ `(C) Tier 1 6-way comparison.md` — 20 axes, 8 emergent patterns (including new Pattern 8 Empirical Research Emergence)
- Re-opening justification documented: 5 distinct outlier signals clear "genuinely different" bar after v11 closure at N=5
- Scope outlier vs scale outlier distinction introduced

### Phase 5 — Iteration log v12
- ✅ `04 Reviews/(C) 2026-04-19 v12 build learnings.md` — 8 new routine v2 action items (cumulative 53 v3-v12)

### Phase 6 — Vault sync
- ✅ Project index updated to all ✅
- ✅ This log appended
- ✅ Root `CLAUDE.md` — codymaster project entry added
- ✅ Root `GOALS.md` — v12 milestone entry + version log entry

### Phase 2-6 unique findings
- **3 numeric corrections caught in Phase 0** — 79 vs 60+ skills / 11 vs 20+ commands / version skew. No downstream cascade (improvement over v11).
- **Scope outlier new type** — BMAD v11 was scale outlier; codymaster v12 is scope outlier. Different kinds of "genuinely different".
- **Pattern 6 sub-divided** — VN-translated (BMAD 6a) vs VN-authored EN-primary (codymaster 6b) vs VN-primary (not in corpus — 6c future).
- **Pattern 8 invented** — Empirical Research Emergence (SkillsBench is only T1 published benchmark).
- **Scale-depth orthogonality** — codymaster 38 stars + deepest primitives falsifies implicit "stars = value" assumption.
- **Storm Bear peer-category entity** pattern stabilizing (v10 Karpathy + v11 VN + v12 VN-author = 3 consecutive).

### Velocity
~2h for all of Phases 2-6. Stable with v9-v11 (7 consecutive wikis at ~2h plateau). No regression.

### v12 status: ✅ COMPLETE — 13 files, T1 re-opened at N=6, first VN-authored framework, Scope outlier framing

---
