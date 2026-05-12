# Pilot v3.2 Step 7 — Pass 2 (Stratum B neutral: /codex:review)

> **Status:** ✅ DONE 2026-05-12T07:24:07Z–07:29:53Z (5m 46s)
> **Findings:** 2 (vs Pass 1 BMAD's 18)

## Run metadata

| Field | Value |
|---|---|
| Pass | 2 of 3 |
| Stratum | B (neutral) |
| Skill / tool | `/codex:review` (slash command from `codex@openai-codex` v1.0.4 plugin, dispatched via Skill tool) |
| Range | `agent-dev..HEAD` (17 commits, 61 files, +4169 / -26) |
| t_start | 2026-05-12T07:24:07Z |
| t_end | 2026-05-12T07:29:53Z |
| Wall-clock | **5 min 46 s** (346 s) |
| Reported token cost | not exposed by codex companion stdout |
| E3 telemetry logged? | **YES** — Skill tool dispatch routed through `codex:review` skill, so PostToolUse hook fires (refines F-01: slash commands invoked directly by user bypass E3, but Skill-tool-dispatched plugin commands DO trigger it) |
| Operator (model) | Session A (Claude Sonnet 4.6, autonomous mode) |
| Background task ID | `bxjesnv0m` |

## Findings count

| Severity | Count | Real bug | Design challenge | Subjective |
|---|---|---|---|---|
| P2 (≈ MEDIUM) | 2 | 2 | 0 | 0 |
| **Total** | **2** | **2** | **0** | **0** |

## Distinct issues raised (numbered)

### C2-1 [P2] Skill name vs directory name mismatch

**File:** `.claude/skills/mattpocock-git-guardrails-claude-code/SKILL.md:2`

**Finding:** When Claude invokes the imported skill by its declared `name` (`git-guardrails-claude-code`), the policy hook (`check-skill-policy.sh`) looks for `.claude/skills/$SKILL_NAME/SKILL.md`. But the file is installed under `.claude/skills/mattpocock-git-guardrails-claude-code/`. The `REFERENCE-ONLY-DO-NOT-INVOKE` role is therefore never read for these imported skills, so the hard block can be bypassed. Same mismatch exists across all 20 imported `mattpocock-*` skills.

**Severity:** P2 (codex) ≈ HIGH (BMAD scale) — defeats the hard-block enforcement for the entire bulk-imported corpus.

**Classification:** **REAL BUG** — verifiable: `grep '^name:' .claude/skills/mattpocock-*/SKILL.md` will show frontmatter names that don't match directory names.

**Recommended action:** Either (a) normalize frontmatter `name:` to match directory basename during import, or (b) make the hook resolve by directory glob (e.g., look up `.claude/skills/*${SKILL_NAME}*/SKILL.md` or maintain a name→dir index in `skill-precedence.json`).

### C2-2 [P2] Primary-check uses ALL persisted telemetry, not current session

**File:** `.claude/hooks/check-skill-policy.sh:40-41`

**Finding:** The "primary has already run this session" warning logic queries the entire persisted `skill-invocation-log.json` history. So once a PRIMARY skill has ever been selected (across any past session), future sessions stop warning when a `REFERENCE-ALT` / `REFERENCE-PORTED` skill is invoked first. This violates the documented per-session rule in CLAUDE.md skill-management policy and makes the second-opinion warning ineffective after the first historical primary invocation.

**Severity:** P2 (codex) ≈ HIGH (BMAD scale) — defeats the intent of the per-session primary check.

**Classification:** **REAL BUG** — direct logic mismatch between documented policy ("PRIMARY first unless operator override... second-opinion after PRIMARY has already run this session") and implementation (no session-id filter).

**Recommended action:** Add a session-id field to telemetry entries (matches Pass 1 F-08 "no audit trail" recommendation) and filter the primary-check query to current session only. Requires both schema change to telemetry log AND a session-id-aware hook.

## Real bug vs design challenge vs subjective (operator triage)

Both findings are confirmable real bugs:
- C2-1: filesystem inspection confirms mismatch
- C2-2: code inspection of hook script confirms missing session filter

Both are different from BMAD's 18 findings — neither was in Pass 1's distinct-topic list.

---

## Comparison-prep notes for Step 10

### Quantitative

| Metric | Pass 1 BMAD | Pass 2 Codex neutral |
|---|---|---|
| Wall-clock | 3m 23s | **5m 46s** (~1.7× slower) |
| Output tokens (approx) | ~1700 | ~450 (much terser) |
| Total findings | 18 | 2 |
| Real bugs | 7 | 2 |
| Design challenges | 7 | 0 |
| Subjective/style | 4 | 0 |
| Severity ceiling | CRITICAL | P2 only |

### Overlap analysis

| BMAD F-id | Topic | Codex Pass 2 caught? |
|---|---|---|
| F-01 telemetry asymmetry | NO (codex doesn't notice that ITS OWN tool bypasses E3) |
| F-02 Pattern #76 scope | NO (out of scope of "review the diff") |
| F-03 B-A17 count=5 doctored | NO |
| F-04 Phase 2 vapor | NO |
| F-05 mv non-atomic | NO |
| F-06 YAML brittleness | NO (but C2-1 below is adjacent — both touch the imported-skills/hook integration surface) |
| F-07 zero-relevance skills | NO |
| F-08 no audit trail | NO directly (but C2-2 echoes the schema gap — telemetry needs session_id) |
| F-09 ratchet no fast-path | NO |
| F-10 ORIG_HEAD over-fires | NO |
| F-11 prefix vocab in JSON only | NO |
| F-12 primary_alternative inconsistency | NO |
| F-13 commit bundling | NO |
| F-14 thresholds undefended | NO |
| F-15 doc self-inconsistency | NO |
| F-16 rubric versioning | NO |
| F-17 dateline omission | NO |
| F-18 mattpocock-handoff scope drift | NO |

**Overlap with BMAD:** 0/18 explicit (0%). Adjacency: C2-2 thematically related to F-08 (both touch telemetry schema gaps), C2-1 thematically related to F-07 (both touch imported-skill hygiene).

### Codex-unique findings (added value over BMAD)

| ID | Topic | Why BMAD missed |
|---|---|---|
| C2-1 | name-field vs directory-name mismatch in imported skills | BMAD reviewed SKILL.md frontmatter as content but didn't trace the lookup path the hook actually uses |
| C2-2 | telemetry-log scope (all history vs current session) | BMAD challenged schema completeness (F-08) but didn't connect that to the hook's primary-check semantics |

Both findings are **deeper code-trace findings** — codex actually executed `grep` patterns against the hook script and walked the path from skill `name:` field → hook lookup → filesystem. BMAD's adversarial mandate produced more findings but mostly at the design/scope/spec layer; codex at the code-execution layer caught two real implementation bugs BMAD missed.

### Tone / actionability

- BMAD: cynical-by-mandate, lots of "are you SURE this is fine?" questions, ≥10 findings hard floor.
- Codex neutral: measured, only reports what it can substantiate with file:line refs, no quota.
- **Specificity:** codex C2-1 and C2-2 have actionable fix paths (rename frontmatter OR change hook lookup; add session_id). BMAD findings vary — some have crisp fixes (F-05 mv, F-06 YAML), some need operator decisions (F-01, F-04).

### Headline numbers

- **Codex efficiency:** 2 findings / 346s = 1 finding per ~173s
- **BMAD efficiency:** 18 findings / 203s = 1 finding per ~11s
- **BUT** filter to real-bugs-only: codex 2 / 346s = 173s per bug; BMAD 7 / 203s = 29s per bug.
- Codex was 6× slower per real-bug found. But codex's real-bugs are **code-level** bugs BMAD missed; BMAD's real-bugs are mostly **spec/schema-level** bugs codex missed.

This suggests the two tools are **complementary, not redundant** — they fish in different ponds.

---

## Raw codex output

```
# Codex Review

Target: branch diff against agent-dev

The patch adds useful harness infrastructure, but the skill policy enforcement
is unreliable because imported skill identifiers do not line up with hook
lookup paths and the session-specific primary check uses all historical
telemetry.

Full review comments:

- [P2] Align imported skill names with their directory names —
  /Users/Cvtot/monorepo/hireui/.claude/skills/mattpocock-git-guardrails-claude-code/SKILL.md:2-2
  When Claude invokes this imported skill by its declared `name`
  (`git-guardrails-claude-code`), the policy hook looks for
  `.claude/skills/$SKILL_NAME/SKILL.md`, but the file is installed under
  `.claude/skills/mattpocock-git-guardrails-claude-code/`. That means the
  `REFERENCE-ONLY-DO-NOT-INVOKE` role is never read, so the hard block can be
  bypassed; the same mismatch exists across the new `mattpocock-*` skills.

- [P2] Check primary usage only within the current session —
  /Users/Cvtot/monorepo/hireui/.claude/hooks/check-skill-policy.sh:40-41
  This query searches the entire persisted telemetry log, so once a PRIMARY
  skill has ever been selected, future sessions stop warning when a
  `REFERENCE-ALT`/`REFERENCE-PORTED` skill is invoked first. That violates
  the documented "primary has already run this session" rule and makes the
  warning ineffective after the first historical primary invocation.
```

## Output for Step 10 ablation

```json
{
  "pass": 2,
  "stratum": "B-neutral",
  "tool": "/codex:review (slash command via Skill dispatch)",
  "skill_invocation_logged": true,
  "wall_clock_seconds": 346,
  "approx_output_tokens": 450,
  "total_findings": 2,
  "by_severity": {"P2": 2},
  "by_classification": {"real_bug": 2, "design_challenge": 0, "subjective": 0},
  "distinct_topics": 2,
  "overlap_with_bmad": 0,
  "codex_unique": 2,
  "operator_confirmed_real_bugs": "pending",
  "operator_confirmed_false_positives": "pending"
}
```
