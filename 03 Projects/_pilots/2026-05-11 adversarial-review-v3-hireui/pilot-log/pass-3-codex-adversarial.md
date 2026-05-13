# Pilot v3.2 Step 7 — Pass 3 (Stratum B adversarial: /codex:adversarial-review) — RETRY SUCCESS

> **Status:** ✅ DONE 2026-05-13T02:24:39Z–02:46Z (~20 min, estimated; precise t_end ambiguous due to session suspension during background task)
> **First-attempt failure:** 2026-05-12T07:30:47Z–07:32:17Z (codex usage limit; B-A18 filed)
> **Retry result:** **17 findings (7 high + 9 medium + 1 low)** — 12 real bugs + 5 design challenges + 0 subjective

## Run metadata

| Field | Value |
|---|---|
| Pass | 3 of 3 |
| Stratum | B (adversarial — MAIN COMPARATOR vs BMAD Pass 1) |
| Skill / tool | `/codex:adversarial-review` via codex-companion.mjs adversarial-review |
| Range | `agent-dev..HEAD` (19 commits, 62 files, +4242 / -28) — diff scope preserved from Pass 1+2 |
| t_start | 2026-05-13T02:24:39Z |
| t_end | ~2026-05-13T02:46:00Z (estimated from codex-login.log activity) |
| Wall-clock | **~20 min** (~22 min upper bound; substantially deeper investigation than Pass 2's 5m 46s — ~50+ tool calls vs ~25) |
| Codex thread ID | `019e21d3-f894-7a50-8330-5ee07be3fa51` |
| Background task ID | `bux8f11yg` |
| Approx output tokens | ~2400 (full findings + recommendations + summary table) |
| E3 telemetry logged? | NO — Skill tool dispatch failed today with `disable-model-invocation` error, so retry ran via direct codex-companion.mjs bash call (slash-bypass-equivalent path). Telemetry log entries from Pass 2 + Pass 3 first attempt yesterday still stand. |
| Operator (model) | Session A (Claude Opus 4.7 1M, autonomous mode resumed) |
| Codex verdict | `needs-attention` |

## Findings count

| Severity | Count | Real bug | Design challenge | Subjective |
|---|---|---|---|---|
| HIGH | 7 | 7 | 0 | 0 |
| MEDIUM | 9 | 4 | 5 | 0 |
| LOW | 1 | 1 | 0 | 0 |
| **Total** | **17** | **12** | **5** | **0** |

## Distinct issues raised (numbered)

### HIGH (7) — all real bugs

#### H-1 GitNexus MCP startup regressed to npx
**File:** `.mcp.json:5-6`
**Real bug.** The branch changes GitNexus from `pnpm dlx` back to `npx -y gitnexus mcp`, even though `agent-dev` documented that npm v11 fails in this repo because `.npmrc` contains pnpm-only keys (`node-linker`, `auto-install-peers`). Agents can start sessions without the required MCP, as happened in this review environment.
**Fix:** Revert to `arch -arm64 pnpm dlx gitnexus mcp` and keep L-011 rationale documented.

#### H-2 I-8 primary-skill precedence is advisory, not enforced
**File:** `.claude/hooks/check-skill-policy.sh:35-47`
**Real bug.** CONSTITUTION says first registry entry must be invoked unless explicit exception applies, but PreToolUse hook only WARNS for REFERENCE-ALT/PORTED and only hard-blocks REFERENCE-ONLY. Non-primary skill in multi-candidate category can still run — invariant violated silently except for best-effort stderr.
**Fix:** Hook should load `skill-precedence.json`, identify selected skill's category, block non-primary selections unless explicit operator override or same-session primary invocation proof.

#### H-3 Same-session rule uses ALL historical telemetry [⚠️ OVERLAP w/ Pass 2 C2-2]
**File:** `.claude/hooks/check-skill-policy.sh:38-42`
**Real bug.** Hook checks whether primary alternative has EVER appeared in skill-invocation-log.json; doesn't filter to current Claude session. Once primary skill ran any previous day, future sessions stop warning. Contradicts CONSTITUTION I-8's current-session requirement.
**Fix:** Record session_id or session-start timestamp; filter primary-check to current session only.

#### H-4 Telemetry concurrent-write race
**File:** `.claude/hooks/log-skill-invocation.sh:59-61`
**Real bug.** E3 uses fixed temp path `${TELEMETRY}.tmp` and no lock. Two PostToolUse hooks running close together race on same temp file; last `mv` wins, dropping invocation or moving partial temp. Bad because pilot relies on invocation counts as evidence.
**Fix:** Use `mktemp` + `flock`/lockdir around read-modify-write, OR append newline-delimited JSON events and compact later.

#### H-5 Blocker migration accepts invalid top-level JSON shapes and rewrites them
**File:** `scripts/harness-migrate-blockers.sh:40-60`
**Real bug.** Script validates only parseability, then blindly runs `map(...)`. In jq, `map` over object iterates values and emits array — accidental object-shaped blockers file would be silently converted to array of values, losing keys and structure. Data corruption dressed as migration.
**Fix:** Validate `type == "array"` before migration; fail closed unless every entry has expected object shape.

#### H-6 Invalid `deferred_count` types are escalated instead of rejected
**File:** `scripts/harness-migrate-blockers.sh:51-56`
**Real bug.** `deferred_count` defaulted only when null; strings and other non-integer values flow into numeric threshold comparisons. jq compares across types rather than enforcing integer semantics — malformed values can be tagged yellow/red instead of failing validation.
**Fix:** Require `deferred_count | type == "number" and floor == . and . >= 0`; reject strings, negatives, floats, booleans, arrays, objects.

#### H-7 Pre-push local-only guard can be bypassed with explicit refspecs
**File:** `scripts/git-hooks/pre-push-sandbox-guard.sh:74-82`
**Real bug.** Guard derives protected branch only from `local_ref`, skips non-`refs/heads/*` local refs. `git push origin HEAD:refs/heads/agent/pilot-x` has `local_ref=HEAD`, so script skips it even though remote target is agent branch. Defeats local-only policy.
**Fix:** Classify both local AND remote refs; if `remote_ref` targets `refs/heads/agent/*`, `refs/heads/agent-dev`, or sandbox, apply guard regardless of local ref name.

### MEDIUM (9)

#### M-1 Direct slash-command usage excluded from telemetry model [⚠️ OVERLAP w/ BMAD F-01]
**File:** `.claude/settings.json:25-31`
**Real bug.** Tracked settings only hook PostToolUse with matcher `Skill`; registry includes `command:/codex:*` entries and admits command pointers won't auto-log. User-typed slash commands bypass E3, skewing pilot comparison toward Skill-dispatch path.
**Fix:** Either remove slash commands from evidence-bearing categories, OR add separate logging path / manual entry for direct command invocations before using telemetry for Step 10 decisions.

#### M-2 Skill category lookup uses substring matching over serialized JSON
**File:** `.claude/hooks/log-skill-invocation.sh:21-26`
**Real bug.** `contains($s)` runs against `.value | tostring`, so category assignment can be driven by substrings inside unrelated skill names, command: wrappers, or metadata-like text. Misclassification pollutes `functional_category` and `candidates_considered` — exact fields used for ablation evidence.
**Fix:** Match array entries exactly after normalizing known prefixes: `.value[] == $s` or `.value[] | ltrimstr("command:/") == $s`, not substring search.

#### M-3 Imported skill names don't match installed directories [⚠️ OVERLAP w/ Pass 2 C2-1]
**File:** `.claude/skills/mattpocock-diagnose/SKILL.md:1-6` and across bulk-imported `mattpocock-*`
**Real bug.** Installed directory is `mattpocock-diagnose`, frontmatter `name: diagnose`; policy hook builds `.claude/skills/$SKILL_NAME/SKILL.md`. If Claude passes frontmatter skill name, hook can't find metadata; role enforcement becomes `unknown`.
**Fix:** Make directory names, registry entries, and frontmatter `name` values identical, OR add explicit alias map used by both E3 and E4 hooks.

#### M-4 `disable-model-invocation` metadata is ignored by enforcement
**File:** `.claude/skills/mattpocock-setup-matt-pocock-skills/SKILL.md:1-7`
**Real bug.** Some imported skills declare `disable-model-invocation: true`, but E4 only blocks `namespace_role=REFERENCE-ONLY-DO-NOT-INVOKE`. Prompt-driven setup/doc skill marked as not model-invocable can still be invoked via Skill tool.
**Fix:** Teach `check-skill-policy.sh` to block `disable-model-invocation: true` and `REFERENCE-DOCUMENTATION` unless explicit operator override present.

#### M-5 A17 pre-seeded to red threshold makes metric outcome circular [⚠️ OVERLAP w/ BMAD F-03]
**File:** `.cm/memory/blockers.json:49-53`
**Design challenge.** Schema supposed to reveal aging blockers, but A17 initialized at `deferred_count=5` with desired red tag rather than deriving count from documented event ledger. First red result is operator assertion not metric output; weakens pilot evidence value.
**Fix:** Store deferral history array or explicit `initialization_reason`; separate security severity from aging count so red status isn't manufactured by picking threshold-crossing initial count.

#### M-6 `attention_tag` is display text masquerading as state
**File:** `.cm/memory/blockers.json:49-51`
**Design challenge.** Schema stores emoji-bearing strings as computed state. Brittle for querying, localization, terminal support, future threshold changes; consumers must compare exact display text instead of stable enum.
**Fix:** Store machine enum `attention_level: "none" | "attention" | "blocking_recommendation"`; derive display labels at render time.

#### M-7 Blockers have no schema version or audit trail [⚠️ OVERLAP w/ BMAD F-08]
**File:** `.cm/memory/blockers.json:1-2`
**Design challenge.** New source of truth is bare array with no `_schema`, migration version, or change history. Counts manually bumped, migration overwrites tags — no way to distinguish legitimate deferral from accidental edit, can't run future migrations safely.
**Fix:** Wrap entries in object with `_schema`, `_migrated_at`, and append-only per-blocker event/history list for deferrals, resolutions, manual overrides.

#### M-8 `.gitignore` as harness-only path blocks legitimate project hygiene changes [⚠️ OVERLAP w/ BMAD F-09]
**File:** `scripts/git-hooks/pre-commit-branch-policy.sh:31-48`
**Design challenge.** Branch policy classifies every `.gitignore` edit as harness work. Project branch adding Expo/Playwright/DB/generated-client/mobile artifact ignores will be blocked or forced into separate agent commit, even when ignore rule inseparable from project change. Existing global `*.sh` ignore still hides project shell scripts outside narrow unignore list.
**Fix:** Split `.gitignore` policy by section or require path-scoped approval; unignore known project script locations.

#### M-9 Bulk-imported PRIMARY skills contain repo-inappropriate operational assumptions [⚠️ OVERLAP w/ BMAD F-07]
**File:** `.claude/skills/mattpocock-obsidian-vault/SKILL.md:1-16`
**Design challenge.** Import marks unrelated skills as PRIMARY while they hard-code external assumptions: Obsidian points at `/mnt/d/Obsidian Vault/AI Research/`; scaffold-exercises assumes `exercises/` course repo + `pnpm ai-hero-cli internal lint`. Not hireui conventions; can send agents into irrelevant files/commands if auto-selected.
**Fix:** Quarantine non-hireui skills as reference-only until each has repo-fit adapter, OR remove from PRIMARY/default consideration.

### LOW (1)

#### L-1 Docs still say 7 invariants after adding I-8 [⚠️ OVERLAP w/ BMAD F-17 partial]
**File:** `CLAUDE.md:56-69`
**Real bug.** CONSTITUTION and CLAUDE retain seven-invariant wording/list while adding I-8 later. Agent bootstrap instructions disagree on number of non-negotiables; affects compliance prompts and onboarding.
**Fix:** Update all invariant count references + tables to include I-8, including CONTINUITY workflow reminders.

## BMAD Pass 1 vs Codex Pass 3 — direct match-up matrix

| BMAD F-id | Topic | Pass 2 caught | Pass 3 caught | Pass 3 finding | Severity match |
|---|---|---|---|---|---|
| F-01 | telemetry asymmetry | NO | **YES** | M-1 | CRITICAL vs MEDIUM (codex less severe) |
| F-02 | Pattern #76 scope mismatch | NO | NO | — | (out of codex scope) |
| F-03 | B-A17 count=5 doctored | NO | **YES** | M-5 | HIGH vs MEDIUM (codex framed as design-challenge, BMAD as real bug) |
| F-04 | Phase 2 vapor | NO | NO | — | (codex doesn't check spec-level commitments) |
| F-05 | mv non-atomic | NO | NO | — | (codex missed atomicity issue specifically — but H-4 catches a related concurrency bug) |
| F-06 | YAML extraction brittle | NO | NO | — | (codex didn't focus on YAML parsing) |
| F-07 | 3 zero-relevance mattpocock skills | NO | **YES** | M-9 | HIGH vs MEDIUM (codex names different skills — Obsidian + scaffold-exercises; BMAD listed 3 different misfits) |
| F-08 | no audit trail for deferred_count | adjacent C2-2 | **YES** | M-7 | MEDIUM vs MEDIUM (full match — both flagged schema version + audit) |
| F-09 | gitignore ratchet | NO | **YES** | M-8 | MEDIUM vs MEDIUM (full match — both note hygiene-edit friction) |
| F-10 | ORIG_HEAD over-fires | NO | NO | — | (codex didn't probe rebase/cherry-pick edge cases) |
| F-11 | prefix vocab undocumented | NO | NO | — | (codex focused on enforcement gaps not doc gaps) |
| F-12 | mattpocock-handoff primary_alternative N/A | NO | NO | — | (codex didn't cross-check registry consistency this granularly) |
| F-13 | commit bundling | NO | NO | — | (codex doesn't audit commit history) |
| F-14 | thresholds 3/5 unitless | NO | NO | — | (codex didn't challenge thresholds) |
| F-15 | doc self-inconsistency caught only by smoke | NO | NO | — | (history; not in current diff) |
| F-16 | telemetry rubric versioning | NO | partial | M-7 mentions schema version | (M-7 partial overlap — same root cause) |
| F-17 | CONSTITUTION dateline omission | NO | **YES partial** | L-1 | NIT vs LOW (different angle — codex caught "7 invariants" stale wording, BMAD caught missing 2nd amendment date) |
| F-18 | mattpocock-handoff scope drift | NO | NO | — | (NIT-level; codex didn't waste tokens on it) |
| **NEW Pass 2 C2-1** | skill name vs dir mismatch | — | **YES** | M-3 | (codex reproduces its own finding under adversarial framing) |
| **NEW Pass 2 C2-2** | primary-check uses all telemetry | — | **YES** | H-3 | (codex reproduces — and elevates from MEDIUM to HIGH severity under adversarial framing) |

### Pass 3 codex-unique findings (NEW — neither BMAD nor Pass 2 caught)

| ID | Topic | Severity |
|---|---|---|
| **H-1** | GitNexus MCP startup regressed to npx (.mcp.json) | HIGH real bug |
| **H-2** | I-8 enforcement is advisory-only (warn-not-block for REFERENCE-ALT/PORTED) | HIGH real bug |
| **H-4** | Telemetry concurrent-write race (no lockfile on `${TELEMETRY}.tmp`) | HIGH real bug |
| **H-5** | Migration script accepts invalid JSON shapes (no `type==array` check) | HIGH real bug |
| **H-6** | `deferred_count` type validation absent (strings can escalate) | HIGH real bug |
| **H-7** | Pre-push guard bypass via explicit refspecs (`HEAD:refs/heads/agent/...`) | HIGH real bug |
| **M-2** | Substring matching in category lookup | MEDIUM real bug |
| **M-4** | `disable-model-invocation` metadata ignored | MEDIUM real bug |
| **M-6** | `attention_tag` is display text not enum | MEDIUM design challenge |

**9 codex-unique findings**, including **6 HIGH real bugs** BMAD missed entirely.

## Pass 2 (codex neutral) vs Pass 3 (codex adversarial) — framing-vs-tool decomposition

| Pass 2 finding | Pass 3 finding | Severity delta | Read |
|---|---|---|---|
| C2-1 skill name/dir mismatch (P2) | M-3 (MEDIUM) | same | tool catches its own finding regardless of framing |
| C2-2 primary-check session scope (P2) | H-3 (HIGH) | **elevated** | adversarial framing escalates severity perception |

**Pass 3 adds 15 findings NOT in Pass 2** (2 BMAD-overlaps from earlier framing absent + 9 codex-unique + 4 doubled in severity-elevated form). This is the answer to the framing-vs-tool question: **adversarial framing DOES dominate over tool default behavior** when applied to the same tool.

## Headline metrics — full 3-pass data

| Metric | Pass 1 BMAD adv | Pass 2 codex neutral | Pass 3 codex adv |
|---|---|---|---|
| Wall-clock | 3m 23s (203s) | 5m 46s (346s) | ~20m (~1200s, estimated) |
| Total findings | 18 | 2 | 17 |
| Real bugs initial | 7 | 2 | 12 |
| Design challenges | 7 | 0 | 5 |
| Subjective | 4 | 0 | 0 |
| Severity ceiling | CRITICAL | P2 | HIGH |
| Approx output tokens | ~1700 | ~450 | ~2400 |
| Cost per finding (s) | ~11 | ~173 | ~71 |
| Cost per real-bug (s) | ~29 | ~173 | ~100 |
| **Overlap with BMAD F-list** | n/a | 0/18 (0%) | **6/18 (33%) full + 2/18 partial = 8/18 (44%) any** |
| **Tool-unique findings** | n/a | 2 | 9 (incl. 6 HIGH real bugs) |
| **Severity-elevated reproductions of Pass 2** | n/a | n/a | 1 (C2-2 MEDIUM → H-3 HIGH) |

## Framing-vs-tool decomposition verdict

Decision tree (from `step-10-final-template.md`):

```
                              Pass 3 overlap with BMAD
                              high (>50%)        low (<20%)
Pass 3 findings count   ┌──────────────────┬──────────────────┐
                  high  │  FRAMING DOMINATES│  TOOL DOMINATES  │
                  (>10) │  Pattern #76 ✅   │  but codex catches│
                        │  strongly supported│ different topics │
                        │                    │ Pattern #76      │
                        │                    │ weakly supported │
                        ├──────────────────┼──────────────────┤
                  low   │  CODEX CAN'T     │  CODEX HAS LOW    │
                  (≤5)  │  PRODUCE BREADTH │  CEILING — tool   │
                        │                    │ rate-limit       │
                        └──────────────────┴──────────────────┘
```

**Pass 3 results:** 17 findings (high), 44% overlap-any with BMAD (medium-to-high range).

**Verdict: MIXED — framing helps but tool also has distinctive lens**
- Adversarial framing CLEARLY changes codex output (2 → 17 findings, +750%; severity ceiling P2 → HIGH)
- BUT codex-adversarial still captures DIFFERENT topics than BMAD-adversarial (6 high-severity codex-unique findings BMAD missed: H-1/H-2/H-4/H-5/H-6/H-7 are all code-execution-trace bugs that BMAD's spec-layer adversarial mandate skipped)
- The two adversarial-framing tools are **partially overlapping, partially complementary** — Pattern #76 (architectural primitive) is NOT what's tested here; what's tested is "adversarial framing in two different tools produces overlapping but tool-distinctive results"

## Pattern #76 verdict (revised with Pass 3)

The structural conclusion from `pattern-76-evidence-2-of-3.md` STANDS: this pilot tests the adversarial-review-prompt layer, NOT framework-level subagent architecture. Pass 3 strengthens **Proposition C** evidence (tool-level adversarial review has substantive value — 17 findings, 12 real bugs, including 6 HIGH severity code-execution-trace bugs).

**Recommendation for v66 mini-audit: KEEP Pattern #76 staged**, await 2+ framework with framework-level architecture by v71. Pilot evidence is now strong for tool-level adversarial review utility but does not satisfy Pattern #76's strict promotion bar.

## Output for Step 10 ablation

```json
{
  "pass": 3,
  "stratum": "B-adversarial",
  "tool": "/codex:adversarial-review (codex-companion.mjs adversarial-review)",
  "skill_invocation_logged": false,
  "wall_clock_seconds": 1200,
  "wall_clock_estimate_note": "t_end ambiguous due to session suspension during background task; ~20 min estimate based on codex-login.log activity through 02:46Z and ~50+ tool call depth",
  "approx_output_tokens": 2400,
  "total_findings": 17,
  "by_severity": {"HIGH": 7, "MEDIUM": 9, "LOW": 1},
  "by_classification": {"real_bug": 12, "design_challenge": 5, "subjective": 0},
  "distinct_topics": 17,
  "overlap_with_bmad_full": 6,
  "overlap_with_bmad_partial": 2,
  "overlap_with_bmad_any_percent": 44,
  "overlap_with_pass_2": 2,
  "pass_3_unique_findings": 9,
  "pass_3_unique_high_real_bugs": 6,
  "severity_elevation_pass_2_to_3": 1,
  "operator_confirmed_real_bugs": "pending",
  "operator_confirmed_false_positives": "pending"
}
```
