# (C) Log — Superpowers Wiki

> Append-only timeline. Format: `## [YYYY-MM-DD] type | title` để parse được bằng grep.
> Append-only timeline. Each entry starts with `## [YYYY-MM-DD] type | title` for grep-friendly parsing.

---

## [2026-04-18] setup | Phase 1 — Wiki khởi tạo / Wiki initialized

- **Project scaffolded** từ skill `new-project` (2026-04-18)
- **Source cloned:** `git clone https://github.com/obra/superpowers.git` → `00 Sources/superpowers/`
- **Initial repo survey:**
  - Total .md files: 73
  - Total files: 142
  - README.md: 7.4KB (small, full-read in 1 pass)
  - CLAUDE.md: 6.5KB (project-level)
  - RELEASE-NOTES.md: **58KB** (large, skim-first strategy)
  - Main folders: `agents/`, `commands/`, `docs/`, `hooks/`, `skills/`, `tests/`
  - Cross-harness explicit: `.claude-plugin/`, `.codex/`, `.cursor-plugin/`, `.opencode/`, `.gemini/` (5 harnesses)
- **Foundational files created:**
  - `02 Wiki/(C) index.md` — catalog với candidate concepts list
  - `02 Wiki/(C) log.md` — this file
  - `01 Analysis/(C) open questions.md` — template
- **Initial cross-project observations** (vs ECC):
  - Smaller scope: 7.4KB README vs ECC 67KB → focused, less feature-creep
  - Cross-harness explicit per-folder vs ECC plugin-based — different distribution philosophy
  - Same building block convention (agents/skills/commands/hooks) — convergent design
  - Author: Jesse Vincent (obra) — OG developer, different style từ Affaan
- **Phase 1 status:** ✅ COMPLETE
- **Next:** Phase 2 source ingestion. Recommended order:
  1. README.md (7.4KB) — full read, foundational
  2. CLAUDE.md (6.5KB) — project methodology
  3. RELEASE-NOTES.md (58KB) — skim headings first cho timeline overview
  4. Key SKILL.md files trong `skills/` — sample 1-2 cho format understanding

---

## [2026-04-18] ingest | Phase 2 — Source summaries (3 files)

- **Source #1:** `(C) README summary.md` — bilingual TL;DR, 7-stage workflow listed, 14 skills categorized, 7-harness installation matrix, 7 distinctive features vs ECC, 7 open questions resolved
- **Source #2:** `(C) Philosophy and Contribution Culture summary.md` — quoted "94% PR rejection rate", 5 mandatory PR checks, 8 categories of rejected changes, Iron Law framing exemplar (TDD), Common Rationalizations + Red Flags tables (anti-pattern detection), `<HARD-GATE>` XML pattern, "your human partner" terminology rationale
- **Source #3:** `(C) Release Notes overview.md` — skim-first applied (58KB file), full-read v5.0.0 → v5.0.7 (5 latest), grep-skim 45 versions; 5 major themes extracted (multi-harness expansion, review loop optimization, zero-dependency push, breaking change discipline, architecture guidance integration)
- **Cross-project pattern map** updated trong Release Notes summary — table 6 axis convergence/divergence với ECC
- **Phase 2 status:** ✅ COMPLETE
- **Insight:** Source ingestion faster than ECC v1 (no prototype tax — format established). ~30% time saved.

---

## [2026-04-18] entities | Phase 3 — Entity pages (4 building blocks)

- **Entity #1:** `(C) The 7-Stage Workflow.md` — 7 stages detail, comparison ECC Sequential Phases, hard gates table, instruction priority hierarchy
- **Entity #2:** `(C) Skills Library.md` — 14 skills categorized (Testing 1, Debugging 2, Collaboration 8, Meta 2 + Foundation 1), Skill anatomy với hard-gate XML, comparison Skill vs Hook vs Agent vs Command, modification restrictions
- **Entity #3:** `(C) Subagent-Driven Development.md` — Stage 4 mechanism deep dive, 3 sub-prompts (implementer/spec-reviewer/code-quality-reviewer), 2-stage review pattern, structured status protocol (DONE/DONE_WITH_CONCERNS/BLOCKED/NEEDS_CONTEXT), context isolation principle, comparison ECC Iterative Retrieval
- **Entity #4:** `(C) Distribution Model.md` — single-repo multi-harness pattern, 7 harness installation flows, 2 distribution channels (marketplace + git URL), per-harness manifest anatomy, AGENTS.md symlink convention, tool name mapping pattern
- **Format compliance:** All 4 follow 13-section canonical format từ vault skill `llm-wiki-ingest`
- **Cross-references:** Each page links siblings + ECC analogs (cross-project knowledge graph established)
- **Phase 3 status:** ✅ COMPLETE
- **Insight:** Pattern generalization VERIFIED. 13-section format works for methodology project (Superpowers) same as feature framework project (ECC). Vault skill `llm-wiki-ingest` proven cross-domain.

---

## [2026-04-18] publish | Phase 4 — Published guides (2 deliverables)

- **Phase 4a:** `03 Published/(C) Superpowers - Huong dan cho nguoi moi.md` — bilingual beginner guide (~500 lines, 7 parts: overview / 7-stage workflow / 14 skills / 2-week setup roadmap / SDD+TDD discipline / FAQ / resources). Parallel structure với ECC v1 guide.
- **Phase 4b:** `03 Published/(C) ECC vs Superpowers comparison.md` — **special deliverable** unique cho Storm Bear vault (~600 lines, 8 sections: TL;DR / cheat sheet / bản chất khác biệt / 12-axis comparison / decision tree / khi dùng cả 2 / migration paths / FAQ).
- **Cross-project synthesis:** comparison guide build từ scattered observations đã embed trong từng entity page và source summary. Cost ~1 hour, không phải 4-5 hours nếu compare from scratch.
- **Phase 4 status:** ✅ COMPLETE
- **Insight:** Cross-project synthesis = unique vault value. Không có ai khác có thể build comparison guide này — chỉ tồn tại vì 2 wiki cùng tay, cùng vault, cùng format.

---

## [2026-04-18] iterate | Phase 5 — Iteration log v2

- **Output:** `07 Iteration Logs/(C) 2026-04-18 v2 build learnings.md`
- **Velocity comparison vs ECC v1 baseline:** 30-40% faster (no format iteration tax), 100% format consistency
- **Key insights:**
  1. Skill `llm-wiki-ingest` compounds — 30-40% time saved on v2 vs v1
  2. Cross-project synthesis = unique vault value (comparison guide không reproducible elsewhere)
  3. Skim-first scales (saved ~1 hour on RELEASE-NOTES 58KB)
  4. Continuous execution mode > batched (autonomous directive trust)
- **Action items issued:** Update skill `llm-wiki-ingest`, root CLAUDE.md, GOALS.md (Phase 2 target #5 = ✅)
- **Phase 5 status:** ✅ COMPLETE
- **v2 ALL PHASES COMPLETE.** Pattern generalization VERIFIED. Vault ready cho 3rd LLM Wiki project.
