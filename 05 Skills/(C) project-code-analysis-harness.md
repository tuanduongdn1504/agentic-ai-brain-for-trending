# Skill: Project Code Analysis Harness

> **Type:** Orchestration skill (harness pattern, paperclip-inspired)
> **Version:** v1 — initial codification
> **Created:** 2026-04-23
> **Target project:** `/Users/Cvtot/monorepo/<client-monorepo>` (read-only)
> **Report destination:** `03 Projects/product/<client>-harness/reports/` (write-only inside vault)
> **Trigger:** Manual via `/loop run project harness` or direct skill invocation
> **Sibling refs:** `llm-wiki-routine-v2.1.md` (phase structure template), `PATTERN_LIBRARY.md` (Phase 3 audit target)

---

## Purpose

Lightweight code-analysis harness that runs 3 recurring diagnostic tasks against the `<client-monorepo>` monorepo and writes a dated report to the Storm Bear vault. Inspired by the paperclip framework's constitutional governance model — explicit invariants, always-produces-artifact, read-only target.

**Scope boundaries:**
- READS the <client> project codebase and config
- READS the Storm Bear vault's `PATTERN_LIBRARY.md`
- WRITES only to `03 Projects/product/<client>-harness/reports/`
- Never commits, never edits the target project, never pushes

---

## Constitutional Invariants (paperclip-inspired)

These are non-negotiable. A harness run that violates any of these is invalid.

1. **READ-ONLY target** — NEVER write to `/Users/Cvtot/monorepo/<client-monorepo>`. No file creation, modification, deletion, or `git` mutation.
2. **ALWAYS write a dated report** — even if phases fail partially, a report is always produced. Partial data is labeled as such.
3. **ALWAYS end with suggested next actions** — per Storm Bear CLAUDE.md prime directive. One actionable next step per task area.
4. **NEVER fabricate lint, parity, or audit results** — if a command fails, report the error. Do not estimate. Do not infer counts from descriptions.
5. **NEVER skip phases silently** — if a phase cannot run, the report explicitly states "Phase N skipped: <reason>".

---

## Invocation

User says one of:
- `/loop run project harness`
- `run project code analysis harness`
- `run <client> harness`

→ Invoke immediately. Execute all 4 phases in sequence within a single session. No check-ins between phases unless a constitutional invariant is about to be violated.

---

## Phase 0: Pre-flight (2 min)

**Goal:** Verify preconditions and scaffold the report file.

1. Check target project reachable:
   ```bash
   test -d /Users/Cvtot/monorepo/<client-monorepo> && echo OK
   ```
2. Check required scripts present:
   ```bash
   grep -E '"lint:all"|"lint"' /Users/Cvtot/monorepo/<client-monorepo>/package.json
   ```
3. Scaffold report file at `03 Projects/product/<client>-harness/reports/(C) YYYY-MM-DD-code-analysis-harness-report.md` with a stub containing: run timestamp, target project path, harness version.
4. If target project unreachable → abort with clear error message written to report, exit.

**Success criteria:** Report file scaffold exists; all preconditions logged.

---

## Phase 1: Lint & TypeCheck (5-10 min)

**Goal:** Capture current code-quality signal from the monorepo.

Run these commands (read-only, capture stdout+stderr):

```bash
cd /Users/Cvtot/monorepo/<client-monorepo>

# Root lint across workspaces (via Turbo)
pnpm lint:all 2>&1

# Root TypeScript typecheck
pnpm exec tsc --noEmit 2>&1

# Mobile workspace typecheck (Expo React Native)
cd apps/mobile && pnpm exec tsc --noEmit 2>&1
```

**Summarise in report:**
- Total error count (lint + typecheck, separately)
- Total warning count
- Top-5 files by issue count
- Count of blocking issues (errors) vs non-blocking (warnings)
- If any command failed to run (missing deps, config error): report verbatim error, do not estimate.

**Fail-soft:** if one command fails, the other two still run. Report the failure; do not abort the whole harness.

---

## Phase 2: Mobile/Web Parity (5-10 min)

**Goal:** Detect feature gaps between `apps/mobile/` (Expo Router) and `src/` (Vite web).

1. **Extract mobile screens/routes:**
   ```
   Glob apps/mobile/app/**/*.{tsx,ts}
   ```
   Filter to Expo Router route files (exclude `_layout.tsx`, `+not-found.tsx`, etc.). Extract route names from file paths (e.g., `apps/mobile/app/(tabs)/profile.tsx` → `profile`).

2. **Extract web pages/routes:**
   ```
   Glob src/**/*.{tsx,ts}
   ```
   Filter to page-level files. Extract page names. (If the project uses react-router, also scan `src/App.tsx` for `<Route path="..." />` definitions.)

3. **Diff into three buckets:**
   - `both`: route/feature exists on both platforms
   - `mobile-only`: exists in `apps/mobile/` but not `src/`
   - `web-only`: exists in `src/` but not `apps/mobile/`

4. **Flag high-signal gaps** — features that appear user-facing (profile, settings, main flows) missing on a platform get highlighted.

**Report output:**
- Table: route | mobile? | web? | status
- Called-out asymmetric routes
- Limitations note (heuristic, not ground truth)

---

## Phase 3: Pattern Library Audit (3-5 min)

**Goal:** Quick health check of Storm Bear's `PATTERN_LIBRARY.md`.

1. Read `/Users/Cvtot/KJ OS Template/PATTERN_LIBRARY.md`.
2. Count patterns by status: confirmed / active-candidate / stale-candidate / retired / observation-track.
3. For each **stale-candidate**: count wikis passed since registration. Flag if ≥10 wikis (retire threshold per routine v2.1).
4. For each **active-candidate**: check if it meets any promotion criterion (per routine v2.1, 5 paths: default-≥3-cross-tier / structural-N=2 / spectrum-N=2 / variant-within-pattern-N=2 / meta-pattern-at-N=3-consolidation).
5. Compute ratio = active / confirmed. Classify:
   - `≤ 0.95:1` — healthy
   - `0.95–1.05:1` — mini-audit available
   - `1.05–2.0:1` — full audit recommended
   - `> 2.0:1` — HARD BLOCK on new wikis

**Report output:**
- Status counts
- Promotion-ready list (patterns meeting criteria)
- Aging stale-candidates (nearing retirement)
- Ratio + health classification
- No edits to `PATTERN_LIBRARY.md` — audit is read-only; actual changes require a separate audit session.

---

## Phase 4: Report Generation (5 min)

**Goal:** Compile findings into a single dated artifact.

Write to `03 Projects/product/<client>-harness/reports/(C) YYYY-MM-DD-code-analysis-harness-report.md`.

**Required sections:**

1. **Metadata**
   - Harness version, target project, run timestamp, phase durations

2. **Executive Summary**
   - Health score for each of the 3 task areas: ✅ green / 🟡 yellow / 🔴 red
   - 1-line takeaway per area

3. **Lint & TypeCheck Results** (Phase 1)
   - Error/warning counts
   - Top offending files
   - Raw command outputs in a collapsed details block

4. **Mobile/Web Parity** (Phase 2)
   - Diff table
   - Flagged asymmetric features

5. **Pattern Library Audit** (Phase 3)
   - Counts, ratio, promotion-ready list, stale list

6. **Suggested Next Actions** (REQUIRED — constitutional invariant #3)
   - One concrete next step per task area
   - Ordered by impact (highest-leverage first)

7. **Blockers & Skipped Phases**
   - Any phase that could not run fully, with reason

---

## Error handling

- **Command failures:** captured verbatim in the report; do not retry more than once
- **Phase failures:** do not cascade — each phase is independent; report stays partial
- **Absolute failures (e.g., vault missing):** abort Phase 0, write a stub report explaining the block, exit

---

## How this mirrors paperclip

| Paperclip principle | This harness |
|---|---|
| Constitutional invariants | 5 explicit invariants above |
| Always produces an artifact | Phase 0 creates report scaffold first |
| Deterministic governance | Phases always run in same order; no agent discretion |
| Read-only boundary when appropriate | Target project is strict read-only |
| Session-scoped orchestration | All phases in one `/loop` session |

---

## Relationship to other skills

- **Does NOT** invoke `llm-wiki-routine-v2.1` — different purpose (code analysis vs wiki ingestion)
- **READS** `PATTERN_LIBRARY.md` — same read-target as audit sessions
- **DOES NOT** modify `PATTERN_LIBRARY.md` — Phase 3 is pure reporting; mutations happen elsewhere

---

## Future evolution (not v1)

- v2 candidate additions (deferred to after first real runs):
  - Automatic delta-report (diff against previous run)
  - Integration with `mcp__scheduled-tasks` for cron-based runs
  - Per-workspace breakdown (web vs mobile vs supabase)
  - GitNexus MCP queries to enrich parity analysis with dependency graph
  - Hookable pre/post phases for project-specific extensions

---

## Next action (per Storm Bear prime directive)

After creating this skill: invoke `/loop run project harness` once to produce the first baseline report, then review the report to calibrate thresholds for v2.
