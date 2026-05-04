# (C) Log — notebooklm-py Wiki

---

## [2026-04-18] setup | Phase 0+1 — Pre-flight + Scaffold (7th routine run)

- **Routine:** `05 Skills/llm-wiki-routine.md` v1 (7th auto-execution — **second different-domain**, first after v6 course)
- **Phase 0 pre-flight (API-probe-first per routine v2 rule from v6 retries):**
  - ✅ GitHub API HTTP 200, 20KB metadata JSON
  - Size: 26,580 KB (~26 MB) — **manageable**, WebFetch preferred over clone for doc-only build
  - Stars: 11,043 | Forks: 1,466 | Language: Python | License: MIT
  - Pushed 2026-04-17 (1 day stale — very active)
  - Default branch: main | Fork: false (original work by teng-lin)
  - Archived: false
  - Root contents: 13 files + 5 dirs (README 11KB, SKILL.md 26KB, CLAUDE.md 7.5KB, CHANGELOG 21KB, AGENTS.md 2.2KB, pyproject.toml, LICENSE, CONTRIBUTING, SECURITY, plus docs/ src/ tests/ scripts/)
  - **Sibling detection: 6 projects** — 4 Tier 1 + 1 Tier 2 + 1 Tier 3
  - **Domain classification: DIFFERENT-DOMAIN** → proposed **Tier 4 "Agent-as-bridge"** (first bridge/connector library in corpus)
  - **Phase 4b routing = Tier 4 proposal + cross-tier positioning** (extends v6 3-tier → v7 4-tier OR bridge as cross-cutting axis)

- **Phase 1 scaffold:**
  - Project folder created via `mkdir -p`
  - 8 subfolders created
  - Source acquisition: WebFetch (applying routine v2 size-aware rule — though 26MB clone-able, WebFetch faster for doc-heavy build)

- **WebFetch-based source retrieval (successful):**
  - README.md — positioning, installation, 3 integration approaches, CLI overview, Python API surface, web-UI-exclusive features, auth, agent integration
  - SKILL.md (26KB) — invocation patterns, core operations matrix (notebook/source/chat/generate/download), autonomy rules, workflow patterns, Claude Code integration examples, output formats, error handling
  - CLAUDE.md — 4-layer architecture, pre-commit workflow, testing strategy, common pitfalls, PR requirements
  - CHANGELOG.md — release cadence 1-2 weeks, v0.3.x production trajectory, breaking changes, RPC fragility flag
  - AGENTS.md — agent isolation rules, auth requirements, recording flags, technical conventions, commit standards

- **Unique findings:**
  - **First bridge/connector library in corpus** — wraps external service (Google NotebookLM) for agent consumption
  - **Three-surface design** — Python API + CLI + agent Skill (unique vs siblings which are 1-2 surfaces)
  - **11K stars** — comparable to mature Tier 1 frameworks
  - **Web-UI-exclusive features** — unique value prop (beyond wrapping official UI)
  - **Explicit agent compatibility** — Claude Code, Codex, OpenClaw named (only sibling to list multiple by name)
  - **Undocumented RPC fragility** — stability policy documented (acknowledged limitation)
  - **v0.3.4 in 3 months** — ~10 releases since Jan 2026 = aggressive cadence
  - **Python 3.10-3.14 support** — forward-compat (unusual to claim 3.14 which is future)
  - **Cross-reference with Tier 3** — could feed ai-agents-for-beginners course as concrete example of Lesson 11 MCP-adjacent patterns
  - **Storm Bear relevance** — Scrum coaches + researchers use NotebookLM heavily for Source→Podcast workflows; library makes Storm Bear agents (Claude Code) able to automate this

- **Source strategy:**
  1. README summary (11KB, full coverage of positioning + features)
  2. SKILL summary (26KB, the invocation reference — extensive operations matrix)
  3. Architecture + Release cluster (CLAUDE.md + CHANGELOG + AGENTS.md combined for context)

- **Phase 0+1 status:** ✅ COMPLETE (scaffold + source retrieved via WebFetch; foundational files written)
- **Next:** Phase 2 source summaries

---

## [2026-04-18] ingest | Phase 2 — Source summaries (3 files)

- **Source #1:** `(C) README summary.md` — positioning ("Unofficial Python API + agentic skill"), 3 integration approaches (Python/CLI/Skill), CLI command groups, Python API surface (5 namespaces), 9 web-UI-exclusive features, auth flow, agent compatibility (Claude Code/Codex/OpenClaw), version status
- **Source #2:** `(C) SKILL summary.md` — 26KB SKILL.md consolidated: invocation patterns (explicit + intent auto), core operations matrix (5 domains × CRUD), content generation options (11 types × format/length/style), download formats, autonomy rules (auto vs confirm), 5 workflow patterns, 4 Claude Code integration scenarios với complete Python code, output JSON schemas, error handling với exit codes, processing time table
- **Source #3:** `(C) Architecture + Release cluster summary.md` — CLAUDE.md 4-layer architecture (CLI → Client → Core → RPC), 9 key modules, development workflow (ruff+mypy+pytest), 3-tier testing (unit/integration/E2E), common pitfalls + PR requirements. CHANGELOG 1-2 week release cadence, v0.3.x production trajectory, breaking changes via deprecation warnings, RPC fragility acknowledged. AGENTS.md isolation rules (NOTEBOOKLM_HOME/PROFILE), --json convention, commit standards
- **Key findings:**
  1. **Triple-surface design** (Library + CLI + Skill) — unique vs siblings
  2. **26KB single SKILL.md** — opposite extreme from ECC's 185 small skill files
  3. **4-layer architecture** isolates fragile RPC from stable user-facing API
  4. **11K stars** — high adoption despite "unofficial" status
  5. **v0.3.4 current** với 1-2 week cadence → aggressive maintenance
  6. **Google API fragility intrinsic** — stability policy documented openly
  7. **Agent autonomy rules explicit** — trust boundary for safe invocation
- **Phase 2 status:** ✅ COMPLETE

---

## [2026-04-18] entities | Phase 3 — Entity pages (4 building blocks)

- **Entity #1:** `(C) CLI Surface.md` — ~50 CLI ops organized by 10 command groups (notebook/source/chat/artifact/generate/download/language/profile/auth/research), universal flags (--json, -n, -p, --wait), example workflows, output format philosophy, Unix-pure design (similar git/kubectl)
- **Entity #2:** `(C) Python API Architecture.md` — 4-layer architecture (CLI/Client/Core/RPC), namespaced async client (notebooks/sources/artifacts/chat/sharing), from_storage() credential pattern, error handling hierarchy, comparison to sibling architectures (both goclaw T2 and notebooklm-py T4 use 4-layer)
- **Entity #3:** `(C) Skill Integration (Claude Code + Codex + OpenClaw).md` — SKILL.md 26KB structure, invocation patterns (explicit + intent), 3 distribution channels, autonomy rules trust boundary, 5 workflow patterns, 4 Claude Code integration scenarios, comparison to sibling skill patterns (ECC 185 small vs notebooklm-py 1 mega-skill opposite extremes)
- **Entity #4:** `(C) Web-UI-Exclusive Capabilities.md` — 9 exclusive features detailed (batch downloads, JSON/MD/HTML export, PPTX, slide revision, report customization, chat persistence, fulltext access, programmatic sharing), strategic categorization (Portability/Automation/Customization), 5 real-world use cases, capability matrix by user type (researcher/educator/consultant/Scrum coach/dev team lead)
- **Format compliance:** 13-section canonical format
- **Cross-references:** Each page links 6 sibling projects + internal entities
- **Phase 3 status:** ✅ COMPLETE

---

## [2026-04-18] publish | Phase 4 — Published guides (2 deliverables)

- **Phase 4a:** `03 Published/(C) notebooklm-py - Huong dan cho nguoi moi.md` — bilingual beginner guide (~620 lines, 11 parts). Parts: intro, install + auth, 3 surfaces, 9 web-UI-exclusive capabilities, Storm Bear use cases, sibling comparison, autonomy rules, 2-week roadmap, risks, next steps, contribution opportunities. Different angle: not "pick daily tool" but "integrate service into existing agent workflow."
- **Phase 4b:** `03 Published/(C) Agent framework taxonomy v3 - 4 tier with bridge.md` — **EXTENDS v6 3-tier → 4-tier** (~720 lines, 18-axis analysis, 8 personas). **Tier 4 "Agent-as-bridge" added.** Orthogonality model also documented (T4 as cross-cutting plug-in axis). 4 emergent patterns: Purpose→Format correlation (validated from v6), vendor consolidation vs solo maintainer (T4 systematically bus factor 1), learning progression recursive (validated), orthogonality of T4 (new).
- **Phase 4 status:** ✅ COMPLETE
- **Insight:** v7 Phase 4b = **4th distinct taxonomy output type** — 2-way (v2) → 3-way (v3) → 4-way (v5) → 2-tier taxonomy (v4) → 3-tier extension (v6) → **4-tier extension + orthogonality (v7)**. Taxonomy evolution visible across wikis.

---

## [2026-04-18] iterate | Phase 5 — Iteration log v7

- **Output:** `07 Iteration Logs/(C) 2026-04-18 v7 build learnings.md`
- **Velocity stable** — ~2h (same as v6). Plateau confirmed.
- **Key insights:**
  1. Routine handles 6 distinct routing modes (same-domain + adjacent + same-tier + 2 different-domain types)
  2. 4-tier taxonomy with T4 Bridge orthogonality
  3. API-probe-first = new standard practice
  4. Bridge maintainer = systematically solo / bus factor 1
  5. Triple-surface (Library + CLI + Skill) emerging pattern for T4
  6. Meta-relevance chain reaches 5 consecutive wikis
  7. 7 wikis = substantial knowledge asset
- **19+ action items** carryover to routine v2
- **Recommendation:** Option D **Storm Bear + notebooklm-py integration pilot** (dual-win: real-use data + T4 validation). OR Option B routine v2 upgrade.
- **Phase 5 status:** ✅ COMPLETE

---

## [2026-04-18] vault-sync | Phase 6 — Vault file updates

- Updated project `(C) index.md` — all phases ✅, deliverable tables populated
- Updated project `(C) log.md` — all phase entries appended
- Updated root `CLAUDE.md` — notebooklm-py project entry + 7-wiki milestone + 4-tier taxonomy note
- Updated `GOALS.md` — mark v7 shipped, Tier 4 established, version log append
- **Phase 6 status:** ✅ COMPLETE

---

## 🎉 v7 ALL PHASES COMPLETE

**7th auto-execution của routine successful.** Second different-domain wiki (bridge/connector library). 4-tier taxonomy with orthogonality established.

**Routine v1 = production-stable across 7 runs** covering 6 distinct domain routing types. 4 tiers now covered: Learn/Use/Deploy/Integrate. 19+ action items accumulated for v2 upgrade.
