# Pilot v3.2 Step 8 — Operator triage worksheet

> **Purpose:** classify every Pass 1 + Pass 2 (+ Pass 3 when retry lands) finding into one of:
> - `real-bug` — verifiable defect with reproducible failure mode
> - `design-challenge` — legitimate trade-off worth discussing but not a bug; operator may accept or reject the recommendation
> - `subjective` — style/judgment call; honor only if the operator agrees
> - `false-positive` — finding is factually wrong (tool misread the code/context)
>
> **Pre-fill assumption:** initial classifications below come from Pass 1 BMAD's self-assessment + Pass 2 codex's tone. Operator overrides anything.
>
> **Output:** this file becomes the source of truth for Step 10 ablation's "operator-confirmed" columns. Step 10 currently has `pending` placeholders for these.

## How to use

For each finding:
1. Read the finding in its source pass file (`.pilot-log/pass-N-*.md`)
2. Inspect the cited file/line in the repo
3. Decide: real-bug / design-challenge / subjective / false-positive
4. Note: **fix-now** (commit on pilot branch, but only AFTER pilot Step 10 closes) / **fix-later** (separate post-pilot ticket) / **wontfix** (accept the trade-off as-is)
5. Record any operator notes (e.g., "F-14 thresholds: discussed with vault session B 2026-05-13, agreed 3/5 are defensible because…")

## Pass 1 — BMAD adversarial findings (18)

### CRITICAL (4)

| F-id | Topic | File:line | Initial class | Operator class | Fix-when | Operator notes |
|---|---|---|---|---|---|---|
| F-01 | Telemetry asymmetry: E3 only catches Skill calls | `.claude/settings.json` matcher field | real-bug | **REFINED in Pass 2 — only true for direct slash; Skill-dispatched slash DOES log** | doc-only fix | F-01 partially refuted; update CLAUDE.md skill-management policy to clarify dispatch path |
| F-02 | Pattern #76 scope mismatch (tool-level vs framework-level) | vault `_patterns/03-active-candidates.md` Pattern #76 | real-bug (operator) / design-challenge (vault) | _operator fill_ | _operator fill_ | Cross-session decision: discuss with Session B vault perspective |
| F-04 | Phase 2 auto-increment hook is vapor | `_bmad-output/tickets/HIR-1162-deferred-count-schema.md` Phase 2 section | real-bug (admitted in doc) | _operator fill_ | _operator fill_ | Operator decision: commit to Phase 2 by what date, or formally accept "manual increment until further notice"? |
| F-07 | 3 of 20 mattpocock skills are repo-pollution | `.claude/skills/mattpocock-edit-article/`, `mattpocock-obsidian-vault/`, `mattpocock-scaffold-exercises/` SKILL.md | real-bug (per SKILL.md content) | _operator fill_ | _operator fill_ | Decision: delete the 3 misfit skills OR keep all 20 for parity-discipline experiment |

### HIGH (5)

| F-id | Topic | File:line | Initial class | Operator class | Fix-when | Operator notes |
|---|---|---|---|---|---|---|
| F-03 | B-A17 count=5 doctored | `.cm/memory/blockers.json` B-A17 + `_bmad-output/tickets/HIR-1162-*.md` | real-bug (doc admits) | _operator fill_ | _operator fill_ | Schema split (count vs severity) or rename to `recommended_severity`? |
| F-05 | mv non-atomic on macOS cross-fs | `scripts/harness-migrate-blockers.sh` mv command | real-bug | _operator fill_ | fix-now (after Step 10) | Add `mktemp -p .` to ensure same-fs temp file |
| F-06 | YAML extraction brittle (grep+sed) | `.claude/hooks/check-skill-policy.sh` namespace_role extraction | real-bug | _operator fill_ | fix-now (after Step 10) | Replace with `yq` (mature) or python yaml stdlib |
| F-10 | Post-merge hook fires on rebase/cherry-pick/reset | `.husky/post-merge` + `scripts/git-hooks/post-merge-blockers-check.sh` | real-bug (git docs) | _operator fill_ | fix-now (after Step 10) | Guard with `[ -f .git/MERGE_HEAD ]` or check `$GIT_REFLOG_ACTION` |
| F-13 | Commit bundling Step 6 [2/3] | commit `f59c6b26 --stat` | real-bug | _operator fill_ | doc-only / wontfix | Bundling has shipped; lesson recorded for future commits |

### MEDIUM (5)

| F-id | Topic | File:line | Initial class | Operator class | Fix-when | Operator notes |
|---|---|---|---|---|---|---|
| F-08 | No audit trail for deferred_count | `.cm/memory/blockers.json` schema | real-bug | _operator fill_ | fix-now (after Step 10) | Add session_id + actor + ts to each deferral event; same change resolves C2-2 |
| F-09 | `.gitignore` ratchet has no fast-path | `scripts/git-hooks/pre-commit-branch-policy.sh` HARNESS_PATTERNS | real-bug (mechanical workflow) | _operator fill_ | doc-only or fix | Document operator override path for project-side `.gitignore` edits |
| F-11 | command:/script: prefix vocab undocumented | `.cm/memory/skill-precedence.json` _meta vs CLAUDE.md/CONSTITUTION.md | real-bug | _operator fill_ | doc fix | Add prefix vocab table to CLAUDE.md skill-management policy section |
| F-12 | mattpocock-handoff `primary_alternative: N/A` | `.claude/skills/mattpocock-handoff/SKILL.md` frontmatter vs `.cm/memory/skill-precedence.json` | real-bug | _operator fill_ | fix-now (after Step 10) | Update SKILL.md frontmatter to match registry |
| F-14 | Thresholds 3/5 unitless and undefended | `_bmad-output/tickets/HIR-1162-*.md` | subjective | _operator fill_ | doc-only | Add empirical-validation deferred ticket; current values are heuristics |

### LOW (3)

| F-id | Topic | File:line | Initial class | Operator class | Fix-when | Operator notes |
|---|---|---|---|---|---|---|
| F-15 | Doc self-inconsistency caught only by smoke | history | low (already-fixed by smoke test) | _operator fill_ | wontfix | Recorded as a lesson; smoke-test caught it |
| F-16 | Telemetry rubric versioning | `.cm/memory/skill-precedence.json` _meta | subjective | _operator fill_ | doc-only | Add schema_version field if/when format changes |
| F-17 | CONSTITUTION dateline omission | `CONSTITUTION.md` Amendment History | low (doc hygiene) | _operator fill_ | doc fix | Add 2nd 2026-05-12 amendment entry |

### NIT (1)

| F-id | Topic | File:line | Initial class | Operator class | Fix-when | Operator notes |
|---|---|---|---|---|---|---|
| F-18 | mattpocock-handoff scope drift (was outside expected 19) | `_bmad-output/runbooks/session-a-to-b-handoff-2026-05-12.md` | nit (not harmful) | _operator fill_ | wontfix | Trivial scope creep; output is valuable handoff doc |

## Pass 2 — Codex neutral findings (2)

| C-id | Topic | File:line | Initial class | Operator class | Fix-when | Operator notes |
|---|---|---|---|---|---|---|
| C2-1 | Skill name vs directory name mismatch | `.claude/skills/mattpocock-*/SKILL.md:2` frontmatter `name:` field | real-bug | _operator fill_ | fix-now (after Step 10) | Defeats hard-block for 20 imported skills. Pick: (a) normalize frontmatter, OR (b) glob lookup in hook. Recommend (a) — explicit > implicit |
| C2-2 | Primary-check uses all telemetry not current session | `.claude/hooks/check-skill-policy.sh:40-41` | real-bug | _operator fill_ | fix-now (after Step 10) | Same root cause as F-08 (audit-trail). Add session_id to telemetry log + filter query. One fix resolves both |

## Pass 3 — Codex adversarial findings (PENDING retry 2026-05-13T02:03Z)

_table will be filled by the auto-retry task; structure mirrors Pass 2 above_

## Triage roll-up (to populate after Step 8 complete)

| Pass | Total | Real bug (operator-confirmed) | Design challenge | Subjective | False positive |
|---|---|---|---|---|---|
| 1 BMAD | 18 | _N_ | _N_ | _N_ | _N_ |
| 2 codex neutral | 2 | _N_ | _N_ | _N_ | _N_ |
| 3 codex adversarial | _pending_ | _N_ | _N_ | _N_ | _N_ |
| **Combined deduplicated** | _N_ | _N_ | _N_ | _N_ | _N_ |

## Fix-now backlog (after Step 10 closes, NOT before — preserves diff scope)

| Finding | Fix description | Effort | Branch | Notes |
|---|---|---|---|---|
| F-05 | mktemp on same fs + atomic mv | XS | new agent/HIR-XXXX sub-task | Quick shell fix |
| F-06 | Replace grep+sed with yq | S | same as F-05 | `brew install yq` prerequisite |
| F-10 | Guard hook with MERGE_HEAD check | XS | same | One-line addition |
| F-12 | Align mattpocock-handoff primary_alternative | XS | doc-only commit | trivial frontmatter edit |
| F-08 + C2-2 | Add session_id to telemetry + filter primary-check | M | same | Schema + hook logic both need update |
| C2-1 | Normalize mattpocock-* frontmatter name fields | S | same | 17 SKILL.md edits (3 misfit + 17 keepers per F-07 decision) |

## Doc-only backlog

| Finding | Doc fix |
|---|---|
| F-01 (refined) | Update CLAUDE.md skill-management section to note slash-vs-Skill-dispatch telemetry path |
| F-09 | Document `.gitignore` operator override path |
| F-11 | Add command:/script: prefix vocab table to CLAUDE.md |
| F-14 | Add deferred empirical-validation note to HIR-1162 doc |
| F-16 | Add schema_version to skill-precedence.json _meta |
| F-17 | Add 2026-05-12 2nd amendment entry to CONSTITUTION |

## Wontfix / accept

| Finding | Reason |
|---|---|
| F-13 | Bundling shipped; lesson recorded |
| F-15 | Already-fixed by smoke test |
| F-18 | Trivial scope creep, output valuable |

## Decisions blocked on operator (NOT mechanical)

| Finding | Operator question |
|---|---|
| F-02 | Pattern #76 scope mismatch — keep current pilot scope (tool-level) or expand to framework-level subagent architecture? Cross-session call with vault |
| F-04 | Phase 2 auto-increment hook — commit to it by what date, or formally retire to "manual increment only"? |
| F-07 | Keep all 20 mattpocock skills (parity discipline) or delete the 3 misfits? |
| F-03 | Schema rename `attention_tag` → `recommended_severity`, OR split `count` from `severity` entirely? |

## After Step 8 close-out

1. Roll-up table populated → feeds Step 10 final ablation
2. Fix-now backlog → sequence into post-pilot sprint (see `.pilot-log/post-pilot-fix-sprint.md` to be drafted)
3. Doc-only backlog → batch into one harness commit on agent-dev after pilot merges
4. Operator-decision items → bring to next Session A or vault Session B working block
