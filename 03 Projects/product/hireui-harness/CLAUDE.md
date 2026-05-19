# hireui-harness — Claude Context

> **Project type:** Agent harness artifact store (evaluations + refactor plans + harness reports)
> **Status:** Active; manual artifact deposits + on-demand harness runs
> **Created:** 2026-05-06 (first artifacts) / **CLAUDE.md added:** 2026-05-18
> **Parent vault:** Storm Bear (`/Users/Cvtot/KJ OS Template`)
> **Target project:** `/Users/Cvtot/monorepo/hireui` (read-only during diagnostic harness runs; agent-dev branch writes happen on the hireui side, not here)
> **Sibling reference:** `03 Projects/product/anspace-harness/` — same harness pattern, different target

---

## Purpose

Artifact store for hireui agent-harness work. Three artifact types live here:

1. **Evaluations** — harness-system reviews (e.g. the v1 / v2 evaluations from 2026-05-06 comparing hireui to KJ OS + anspace patterns)
2. **Refactor plans** — proposals for code changes in the hireui monorepo, verified against vault patterns before they get executed in `/Users/Cvtot/monorepo/hireui`
3. **Harness reports** — dated execution outputs from on-demand harness runs (lint / typecheck / web-mobile parity / Pattern Library audit)

This is NOT a wiki-ingest project. It does not follow the `(wiki / log / summary / index)` folder layout used by `Beginner Analysis` projects.

---

## Structure

```
hireui-harness/
├── CLAUDE.md              ← You are here
├── (C) YYYY-MM-DD <artifact title>.md  ← Evaluations + refactor plans at root
└── reports/
    └── (C) YYYY-MM-DD-<harness>-report.md  ← Generated per harness run
```

---

## How to run a harness

From any Claude Code session in the vault:

```
/loop run project harness
```

Or directly invoke the skill defined in `05 Skills/(C) project-code-analysis-harness.md`. Same 4-phase workflow as anspace-harness:

1. **Phase 0** — Pre-flight (verify target project reachable)
2. **Phase 1** — Lint & TypeCheck (`pnpm lint:all` + `tsc --noEmit` web & mobile)
3. **Phase 2** — Web/Mobile parity diff (routes in web app vs `apps/mobile/`)
4. **Phase 3** — Pattern Library audit (read-only health check on the vault)
5. **Phase 4** — Report generation (dated artifact in `reports/`)

---

## Constitutional invariants

Same 5 invariants as anspace-harness (defined in the skill file):

1. **READ-ONLY target during diagnostic harness runs** — harness never writes to `/Users/Cvtot/monorepo/hireui`
2. **ALWAYS writes a dated report** to `reports/`, even on partial failure
3. **ALWAYS ends with suggested next actions** per Storm Bear prime directive
4. **NEVER fabricate counts** (lint errors, TS errors, file counts) — re-run the command or cite the run
5. **NEVER skip phases silently** — record skipped phases + reason in the report

Refactor plans deposited here are NOT bound by the READ-ONLY invariant — they propose changes to hireui that get reviewed + executed separately, on the appropriate hireui branch.

---

## Claude's rules for this project

- **Do NOT modify `/Users/Cvtot/monorepo/hireui` during diagnostic harness runs**
- **Do NOT edit prior artifacts** — each plan / report is a dated snapshot; history is append-only. New version = new dated file (v2 = newer file, never edit-in-place)
- **Ask before changing this CLAUDE.md** — per Storm Bear user rule
- **Verify plans against current vault state before saving** — plans should cite routine v2.2 (current; supersedes v2.1 as of 2026-05-14), Pattern Library state at write-time, and actual hireui repo state where applicable
- **NEVER fabricate** — package names, file paths, line numbers must be verifiable. If a plan cites `@talentaxis/mobile`, grep `apps/mobile/package.json` before saving

---

## Reading a report or plan

Each artifact in this folder is self-contained. Recommended onboarding order for a new agent in this folder:

1. Read this CLAUDE.md
2. Read the most-recent root-level artifact (refactor plan or evaluation)
3. Read the most-recent harness report in `reports/` (if any)
4. Defer older artifacts unless current work requires history

Reports and plans sort by filename (date), so newest is at the bottom when listed.

---

## Relationship to Storm Bear

- Patterns observed while running the harness (e.g. "harness reports a recurring kind of parity gap") should be noted in the operator log but NOT auto-registered in `PATTERN_LIBRARY.md`
- Pattern registration requires a separate wiki-ingest session or a deliberate audit
- Refactor plans live here, NOT in the hireui repo, until / unless operator approves moving them inline
- This harness is a **diagnostic + planning tool**, not a wiki-building tool

---

## Next action

If running a harness for the first time, invoke `/loop run project harness`. Otherwise read the most-recent root-level artifact.
