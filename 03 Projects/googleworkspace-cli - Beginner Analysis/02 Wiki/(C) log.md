# (C) Log — googleworkspace/cli Wiki

---

## [2026-04-19] setup | Phase 0+1 — Pre-flight + Scaffold (13th routine run)

- **Routine:** `05 Skills/llm-wiki-routine.md` v1 (13th auto-execution — **T4 multi-entrant validation**)
- **Phase 0 pre-flight (API-probe-first):**
  - ✅ GitHub API HTTP 200
  - **Stars: 25,000** — 3rd largest in corpus (after build-your-own-x 491K, BMAD 45K)
  - Forks: 1,300
  - License: **Apache-2.0** — first Apache-2.0 in corpus (prior all MIT except codymaster ISC)
  - Default branch: main
  - Language: **Rust 98.8%** — FIRST Rust project in corpus
  - **283 commits, 44 releases, v0.22.5 pre-1.0** — mature versioning, aggressive pre-release
  - 84 watchers, 71 open issues (active maintenance)
  - Homepage: developers.google.com/workspace
  - Topics: rust, cli, automation, oauth2, google-drive, google-sheets, google-calendar, google-docs, google-api, google-chat, google-workspace, google-admin, ai-agent, discovery-api, agent-skills, gemini-cli-extension
  - Root folders: `.agent/`, `.changeset/`, `.claude/`, `.gemini/`, `.github/`, `.vscode/`, `art/`, **`crates/`** (Rust workspace), `docs/`, `npm/`, `scripts/`, `skills/`
  - Root files: README.md, AGENTS.md, **CLAUDE.md** (1-liner), **CONTEXT.md** (runtime rules — novel), CHANGELOG.md, SECURITY.md, LICENSE, Cargo.toml, package.json, pnpm-lock.yaml, flake.nix, lefthook.yml, gemini-extension.json, demo.gif
  - **Sibling detection: 12 projects** — 6 T1 + 1 T2 + 1 T3 + 1 T4 (notebooklm-py) + 2 T5 + 1 outside
  - **Domain classification: TIER 4 "Agent-as-bridge" ENTRANT #2 — VALIDATES T4 MULTI-ENTRANT**
  - **Subcategorization hypothesis (new v13):** T4 splits along **official-corporate vs unofficial-solo** — parallel to T5's corporate-generalist vs solo-specialist split at v10
  - **Phase 4b routing = T4 2-way comparison** (same pattern as v10 autoresearch T5 2-way)

- **Phase 1 scaffold:**
  - Project folder created via `mkdir -p`
  - 8 subfolders created
  - Source acquisition: WebFetch (README + CLAUDE.md + AGENTS.md + CONTEXT.md + skills/ listing)

- **WebFetch retrievals successful:**
  - README — Tagline, 11+ services, 5 install channels, multi-flow OAuth2, helper `+verb` commands, 110 skills, Model Armor, 2-phase architecture
  - CLAUDE.md — 1-liner: "follow all guidelines outlined in the AGENTS.md file"
  - AGENTS.md (209 lines, 11980 bytes) — 9 sections: Project Overview / Build & Test / Changesets / Architecture / Demo Videos / Input Validation / PR Labels / Helper Commands / Environment Variables
  - CONTEXT.md (44 lines, 2669 bytes) — "Rules of Engagement for Agents": Schema Discovery + Context Window Protection + Dry-Run Safety + Core Syntax
  - skills/ listing — **110 folders total**: 44 gws-* service skills + 10 persona skills + 56 recipe skills

- **Unique findings (Phase 0 — 3 corpus firsts + novel patterns):**
  - **FIRST Rust project** — prior corpus: Python (autoresearch/notebooklm-py/deer-flow-backend/course), JS/TS (gstack/goclaw/codymaster), Markdown-core (ECC/SP/GSD/BMAD)
  - **FIRST Apache-2.0** — prior all MIT (except codymaster ISC)
  - **FIRST official-Google-corporate backing** — prior corporate backers: Microsoft (T3 course), ByteDance (T5 deer-flow), YC (T1 gstack). Google joins as 4th corporate backer but first with agent-tooling repo under main org.
  - **Tri-file agent documentation** (CLAUDE.md + AGENTS.md + CONTEXT.md) — CLAUDE.md is 1-liner pointer (same pattern as BMAD v11), but CONTEXT.md is NOVEL. No prior project had runtime-user agent rules as separate file.
  - **Dynamic Discovery Service architecture** — builds CLI at runtime from Google Discovery JSON; NO generated Rust crates for API types. Architectural novelty.
  - **110 skills in 3 categories** — gws-* service / persona (role-based bundles) / recipe (workflow recipes). Persona + recipe layer is NEW concept in corpus.
  - **Model Armor integration** — Google's response sanitization for agent safety. First appearance in corpus.
  - **Schema introspection built-in** — `gws schema <method>` command. Unique feature.
  - **5 install channels** — binaries / npm / cargo / nix / brew. Second-broadest after codymaster v12 8+.
  - **Multi-flow OAuth2 + AES-256-GCM keyring** — most enterprise-grade auth in corpus.
  - **Input validation as adversarial-input-first discipline** — AGENTS.md explicitly treats CLI args as adversarial. Formalizes ECC AgentShield-style thinking at framework level.
  - **NDJSON streaming** — `--page-all` agent-friendly output. Parallel to codymaster's `cm://` URI + Context Bus (different solution to same problem).
  - **Changeset-driven releases** — every PR has `.changeset/<name>.md`. Same pattern as BMAD v11 + Superpowers.
  - **Two-crate Rust workspace** — library/binary separation. First Rust-idiomatic structure in corpus.
  - **25K stars at v0.22.5 pre-1.0** — aggressive pre-release adoption. Top 3 corpus by stars.
  - **44 releases in ~1 year** — weekly cadence similar to BMAD v4-era iteration speed.

- **Source strategy:**
  1. README summary (tagline + 11 services + install + architecture + 110 skills overview)
  2. CONTEXT + CLAUDE + AGENTS cluster summary (tri-file agent documentation pattern)
  3. 110 Skills + Helper Commands cluster summary (gws-* + persona + recipe + `+verb` orchestration)

- **Phase 0+1 status:** ✅ COMPLETE
- **Next:** Phase 2 source summaries

---

## [2026-04-19] complete | Phases 2-6 shipped

### Phase 2 — 3 source summaries
- ✅ `(C) README summary.md` — tagline, 11+ services, 5 install channels, 4-flow OAuth2, helper commands, 110 skills, Model Armor
- ✅ `(C) CONTEXT + CLAUDE + AGENTS cluster summary.md` — tri-file agent docs pattern (novel); CLAUDE.md 1-liner pointer + AGENTS.md 209 lines + CONTEXT.md runtime rules
- ✅ `(C) 110 Skills + Helper Commands cluster summary.md` — 44 gws-* + 10 personas + 56 recipes + `+verb` helper anti-patterns

### Phase 3 — 4 entity pages
- ✅ `(C) Dynamic Discovery Service Architecture.md` — runtime CLI generation, novel in corpus
- ✅ `(C) 110 Skills (44 gws-_ + 10 personas + 56 recipes).md` — persona + recipe layer NOVEL taxonomy
- ✅ `(C) Multi-Flow OAuth2 + Model Armor + Validation Discipline.md` — enterprise-grade security + adversarial-input policy
- ✅ `(C) T4 Multi-Entrant Validation + Official-vs-Unofficial + Storm Bear Enterprise Angle.md` — Storm Bear meta-entity, T4a/T4b formalized, Pattern #9 confirmed cross-tier

### Phase 4a — Beginner bilingual guide
- ✅ `(C) googleworkspace-cli - Huong dan cho nguoi moi.md` (~600 lines, 10 parts, bilingual)

### Phase 4b — T4 2-way comparison
- ✅ `(C) Tier 4 2-way comparison.md` — 15 axes, 4 new patterns (#9 cross-tier, #10 official-vs-unofficial T4, #11 Dynamic Discovery requires official, #12 corporate formalizes docs)
- T4 validated at N=2 (fourth tier to validate after T1/T5)

### Phase 5 — Iteration log v13
- ✅ `04 Reviews/(C) 2026-04-19 v13 build learnings.md` — 8 new routine v2 action items (cumulative 61)

### Phase 6 — Vault sync
- ✅ Project index updated to all ✅
- ✅ This log appended
- ✅ Root `CLAUDE.md` — googleworkspace-cli project entry added
- ✅ Root `GOALS.md` — v13 milestone + version log entry

### Phase 2-6 unique findings
- **3 corpus firsts:** First Rust + First Apache-2.0 + First official-Google-corporate
- **4 new patterns invented (9-12):** cross-tier corporate-vs-solo / T4 official-vs-unofficial axis / Dynamic Discovery requires official / Corporate formalizes agent docs
- **T4 subcategorization formalized:** T4a official-corporate-broad / T4b unofficial-solo-narrow
- **Pattern #9 promoted** to cross-tier observed law (T4 v13 confirms T5 v10 pattern)
- **Tri-file agent documentation** (CLAUDE.md + AGENTS.md + CONTEXT.md) — novel in corpus
- **Dynamic Discovery architecture** — only runtime-generated CLI in corpus
- **Model Armor integration** — first response-sanitization safety layer in corpus
- **Persona + recipe skill layers** — novel 3-axis skill taxonomy (function × role × workflow)
- **Storm Bear enterprise pilot candidate** — Google Workspace ubiquity VN + enterprise auth + Apache-2.0

### Velocity
~2h for all of Phases 2-6. Stable with v9-v12 (8 consecutive wikis at ~2h plateau).

### v13 status: ✅ COMPLETE — 13 files, T4 validated at N=2, 4 patterns invented, 3 corpus firsts documented

---
