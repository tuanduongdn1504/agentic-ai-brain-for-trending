# Post-pilot fix sprint plan

> **Trigger:** runs AFTER pilot Step 10 closes (when full 3-pass data + operator triage complete).
> **Goal:** convert pilot-derived real bugs into committed fixes on agent-dev, then merge pilot → agent-dev.
> **Constraint:** do NOT start any of these BEFORE Pass 3 retry + Step 10 finalization. Diff scope must stay frozen during Step 7 review window.

## Sequencing rationale

Three buckets, ordered by risk and dependency:

1. **Bucket 1 — Quick-fix harness bugs** (XS effort, no schema change, mechanical): F-05, F-06, F-10, F-12. Land as separate small commits on a new `agent/HIR-XXXX-pilot-followup` branch (per local-only-by-default branch policy 2026-05-12). Merge → `agent-dev` → push.
2. **Bucket 2 — Schema + hook changes** (M effort, touches blockers.json schema AND hook logic, needs migration path): F-08 + C2-2 (telemetry session_id), C2-1 (skill name/dir normalization). These need design upfront — short ticket each.
3. **Bucket 3 — Doc-only batch** (S effort, no code execution risk): F-09, F-11, F-14, F-16, F-17, F-01-refinement. One harness commit covering all CLAUDE.md / CONSTITUTION.md / HIR-1162 doc edits.

## Bucket 1 — Quick-fix backlog

### Ticket HIR-XXXX-pilot-followup-quickfix (S total)

Single agent/* branch covering F-05/F-06/F-10/F-12. Each fix is one small commit; bundle is acceptable here because all four are "pilot-derived real bug fix" theme.

| Finding | Fix | File | LOC | Test |
|---|---|---|---|---|
| F-05 | mv → atomic same-fs | `scripts/harness-migrate-blockers.sh` | -3/+5 | Re-run migration on test fixture twice, verify idempotent + no half-written file |
| F-06 | grep+sed → yq | `.claude/hooks/check-skill-policy.sh` | -8/+5 | Test with both quoted-value frontmatter and unquoted; need `brew install yq` prerequisite documented |
| F-10 | Guard with MERGE_HEAD | `scripts/git-hooks/post-merge-blockers-check.sh` | +3/-0 | Manual: trigger via `git rebase`, `git cherry-pick`, `git reset`; verify hook does NOT fire for any. Then `git merge agent/test-branch`; verify hook DOES fire |
| F-12 | Frontmatter alignment | `.claude/skills/mattpocock-handoff/SKILL.md` | ±1 | Verify registry consistency: `bash scripts/harness-check-skill-precedence.sh` (or grep both files) |

**Prereq:** `brew install yq` if not present on operator machine.

**Risk:** F-06 yq dependency on operator dev env. If yq not preferred, fallback to python3 yaml.safe_load (already on macOS by default).

## Bucket 2 — Schema + hook design

### Ticket HIR-XXXX-telemetry-session-id (M)

**Problem:** F-08 (blockers.json has no audit trail per `deferred_count`) + C2-2 (skill-invocation-log primary-check queries entire history not current session). Both stem from missing session-id field in the telemetry schema.

**Design steps:**
1. Add `_meta.schema_version: 2` to `.cm/memory/skill-invocation-log.json` (was implicit v1, no version field — per F-16)
2. Append `session_id` field to each invocation entry. Source: env var `CLAUDE_SESSION_ID` (or auto-derive from a session-start hook write)
3. Append `session_id` field to each blocker deferral event (need sub-entry array? OR `deferred_history: [{session_id, ts, deferred_count}, ...]`?) — design call
4. Update `check-skill-policy.sh:40-41` primary-check query to filter by current session_id
5. Migration: existing entries get `session_id: "pre-migration-2026-05-12"` placeholder via re-run of `harness-migrate-blockers.sh` (extend script to handle telemetry log too)
6. Document new schema in `_bmad-output/tickets/HIR-XXXX-telemetry-session-id.md`

**Effort:** ~60-90 min. Touches: blockers.json + skill-invocation-log.json + 2 hooks + 1 migration script + 1 design doc.

### Ticket HIR-XXXX-skill-name-dir-normalize (S)

**Problem:** C2-1 — mattpocock-* SKILL.md frontmatter `name:` doesn't match directory basename, so `check-skill-policy.sh` lookup fails. 20 imported skills affected.

**Design options:**

| Option | Pros | Cons |
|---|---|---|
| A. Normalize frontmatter to match directory | Explicit; survives any hook implementation change | 20 file edits |
| B. Glob lookup in hook | Hook handles convention drift gracefully | Implicit naming convention; obscures the assumption |
| C. Maintain name→dir index in skill-precedence.json | Decouples enforcement from naming | Adds index that can drift from filesystem |

**Recommend Option A.** Lowest cognitive load; explicit > implicit. 20 edits is mechanical.

**Effort:** ~30 min mechanical edits + 5 min hook test.

## Bucket 3 — Doc-only batch

### Single commit: `chore(agent): pilot v3.2 doc-only follow-up batch (F-01/09/11/14/16/17)`

| Finding | Doc fix | File |
|---|---|---|
| F-01 (refined) | Note slash-vs-Skill-dispatch telemetry distinction | `CLAUDE.md` skill-management policy section |
| F-09 | Document `.gitignore` operator override path | `CLAUDE.md` branch policy section |
| F-11 | Add command:/script: prefix vocab table | `CLAUDE.md` skill-management policy section |
| F-14 | Add deferred empirical-validation note for 3/5 thresholds | `_bmad-output/tickets/HIR-1162-deferred-count-schema.md` |
| F-16 | Add schema_version to `_meta` (paired with Bucket 2 ticket) | `.cm/memory/skill-precedence.json` + `.cm/memory/skill-invocation-log.json` |
| F-17 | Append 2026-05-12 2nd amendment dateline | `CONSTITUTION.md` Amendment History |

**Effort:** ~30 min total. Single commit, no test required (doc-only).

## Operator-decision-blocked work (NOT in this sprint)

Cannot start without operator call:

- F-02 Pattern #76 scope mismatch → cross-session decision with vault Session B
- F-04 Phase 2 auto-increment hook → operator commitment date OR formal retire
- F-07 3 mattpocock misfit skills → keep all 20 (parity discipline) OR delete 3 (correctness)?
- F-03 schema rename `attention_tag` → `recommended_severity` OR split count/severity entirely?

Each of these becomes its own sub-ticket once the operator decides direction.

## After all 3 buckets land

1. Merge `agent/HIR-XXXX-pilot-followup-quickfix` → `agent-dev` locally
2. Merge `agent/HIR-XXXX-telemetry-session-id` → `agent-dev`
3. Merge `agent/HIR-XXXX-skill-name-dir-normalize` → `agent-dev`
4. Doc-only commit lands directly on `agent-dev`
5. Merge pilot branch `agent/pilot-2026-05-11-adversarial-review` → `agent-dev` (pilot work itself)
6. Single `AGENT_PUSH_CONFIRMED=1 git push origin agent-dev` push of all 5 streams
7. Delete pilot branch (`git branch -d agent/pilot-2026-05-11-adversarial-review`)
8. Final vault sync: copy `.pilot-log/*` → vault `_pilots/.../pilot-log/`
9. Append Pattern #76 evidence note to vault `_patterns/03-active-candidates.md`
10. Update `_state/pilot-ranking-2026-05-07.md` with pilot outcome

## Estimated total effort

| Bucket | Effort |
|---|---|
| Quick-fix backlog (F-05/06/10/12) | 60-90 min |
| Telemetry session-id (F-08 + C2-2) | 60-90 min |
| Skill name/dir normalize (C2-1) | 30-45 min |
| Doc-only batch (6 findings) | 30 min |
| Merge dance + push + vault sync | 20-30 min |
| **Total** | **~3-5 hours** |

Spread across 1-2 working blocks after Step 10 closes.

## Dependencies

- All work depends on Step 10 closing successfully (Pass 3 retry lands + operator triage in `step-8-triage.md` complete)
- Bucket 2 (telemetry session-id) depends on operator's decision on F-03 — if schema changes anyway, can bundle both schema concerns into one migration
- Doc-only batch depends on F-01 refinement being operator-confirmed (currently described in `.cm/CONTINUITY.md` Step 7 PARTIAL block)

## Risk register

| Risk | Mitigation |
|---|---|
| F-06 yq prereq fails on operator dev env | Fallback to `python3 -c "import yaml; ..."` (stdlib) |
| F-10 MERGE_HEAD guard breaks existing valid merges | Test on a real `agent/test-XX → agent-dev` merge before landing |
| Bucket 2 schema migration corrupts existing telemetry data | Extend `harness-migrate-blockers.sh` to back up `skill-invocation-log.json` to `.harness-backup/` (already gitignored) before mutation |
| C2-1 frontmatter rename breaks any external reference | Grep entire repo for old skill names before/after to ensure no breakage |
| Pilot merge to agent-dev surfaces conflict with newer agent-dev commits | Rebase pilot branch onto agent-dev tip before merge; resolve conflicts inline |
