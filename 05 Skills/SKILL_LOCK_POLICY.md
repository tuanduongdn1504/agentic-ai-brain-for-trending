# Storm Bear Skill-Lock Policy

> **Decided:** 2026-04-28 session 68
> **v27 HIGH bundle item #3: COMPLETE**
> **Builds on:** license decision (MIT) + public-release decision (whole-vault NOW) + publishing strategy (22c AGENTS.md)

---

## Policy summary

Vault `05 Skills/` directory contains skill definitions at varying maturity levels. This policy classifies each skill as **PUBLIC-ARCHIVED (locked)** or **IN-FLUX (continues evolving)** to set operator expectations and external-user trust signals.

## Skill classification (post-v57 / 2026-05-06)

| Skill File | Status | Rationale |
|---|---|---|
| `llm-wiki-routine.md` (v1) | 🔒 **PUBLIC-ARCHIVED** | Superseded 2026-04-19 by v2; v1 frozen as historical record |
| `llm-wiki-routine-v2.md` (v2) | 🔒 **PUBLIC-ARCHIVED** | Superseded 2026-04-22 by v2.1; v2 frozen as historical record |
| `llm-wiki-routine-v2.1.md` (current) | 🟢 **IN-FLUX** | Production-stable across 14+ executions; tightened session 66 STRICT amendment; v2.2 candidate refactor pending; continues evolving |
| `brain-setup.md` | 🟢 **IN-FLUX** | Operator-interview skill; may evolve as new operator-onboarding patterns emerge |
| `new-project.md` | 🟢 **IN-FLUX** | Project scaffolding skill; may evolve as new project archetypes emerge |
| `weekly-update.md` | 🟢 **IN-FLUX** | Operator-interview skill for vault-state refresh; may evolve as vault-state architecture changes |
| `llm-wiki-ingest.md` | 🟢 **IN-FLUX** | Wiki-ingestion skill (Karpathy pattern); may evolve in parallel with routine v2.1 |
| `(C) project-code-analysis-harness.md` | 🟢 **IN-FLUX** | Code-analysis harness skill (paperclip-inspired); client-target redacted 2026-05-06; may evolve |
| `SKILL_LOCK_POLICY.md` (this file) | 📋 **POLICY** | Governance file; not a skill itself |

## Public-archived (locked) skill conventions

Locked skills get this header inserted at top:

```markdown
# [Skill Name] — PUBLIC-ARCHIVED ([archive date])

⚠️ **THIS SKILL IS SUPERSEDED.** Use the current version instead:
→ `[current-version-file].md`

This file is preserved as a historical record of skill evolution. DO NOT modify. DO NOT use in production. For current routine, see [current-version-file].md.

[Original skill content preserved verbatim below the header]
```

Locked skills are public-readable (MIT license) but not actively maintained. External users should treat as reference-only.

## In-flux skill conventions

In-flux skills get this header inserted at top (or skipped if already authoritative):

```markdown
# [Skill Name]

📍 **Status:** IN-FLUX (continues evolving — current version as of [date])

[Skill content...]
```

In-flux skills are public-readable (MIT) AND actively maintained. External users may use in production but should pin to specific git commit if stability matters.

## Phase 4 / item #3 execution

**Required actions to apply policy:**

1. ✅ Create `SKILL_LOCK_POLICY.md` (this file)
2. ⏸ Apply public-archived header to `llm-wiki-routine.md` (v1) — DEFERRED to operator at pre-launch
3. ⏸ Apply public-archived header to `llm-wiki-routine-v2.md` (v2) — DEFERRED to operator at pre-launch
4. ⏸ Verify `llm-wiki-routine-v2.1.md` (current) has IN-FLUX status header — DEFERRED to operator at pre-launch
5. ⏸ Verify `brain-setup.md` + `new-project.md` have IN-FLUX status headers — DEFERRED to operator at pre-launch

**Why deferred:** Vault-internal vs public-archived header changes are mechanical edits operator can do at pre-launch. Policy is committed at this decision; mechanical application happens at pre-launch.

## Future v2.2 candidate refactor

Routine v2.2 candidate refactor is pre-registered (per v56 iteration log lessons):

**Triggers for v2.2 codification:**
- Phase -1 "Subject scale assessment" (lesson from v56 EXTREME-tier 4-tool-use-thrash)
- Pre-distilled facts file pattern (lesson from session 67 main-loop fallback)
- Main-loop direct-write fallback path (3-failure agent threshold)
- Updated chapter-file reading discipline (post-vault-refactor)

**Process for v2.2:**
1. Build accumulated action items list (currently 235+ across v3-v55)
2. Apply consolidation-forward discipline (most action items already absorbed into routine v2.1)
3. Codify v2.2 as new file `05 Skills/llm-wiki-routine-v2.2.md`
4. Lock v2.1 as PUBLIC-ARCHIVED at v2.2 codification
5. Document v1 → v2 → v2.1 → v2.2 lineage in CLAUDE.md

**Estimated v2.2 codification:** Phase 4 mastery (months 3-6) — NOT urgent.

## Anthropic skills marketplace submission (Phase 3 cross-reference)

Skills submitted to Anthropic skills marketplace (per `_state/publishing-strategy-2026-04-28.md`):

1. `llm-wiki-routine-v2.1.md` (IN-FLUX; current production version)
2. `brain-setup.md` (IN-FLUX; current operator-interview skill)
3. `new-project.md` (IN-FLUX; current project-scaffolding skill)

Public-archived skills (`v1` + `v2`) are NOT submitted — they're preserved as GitHub-readable historical records only.

## License compatibility

All vault skills use MIT License (vault-uniform per `LICENSE.md`). MIT compatible with:
- ✅ Anthropic skills marketplace
- ✅ Vercel-labs SKILL.md format precedent
- ✅ Composio marketplace.json convention
- ✅ Forking + modification + commercial use (per Q2=C pure-permissive)

## Pattern Library impact

**Pattern #22 AGENTS.md Industry Standard** — already strengthened at publishing-strategy phase (22c sub-variant N=2 STRUCTURAL).

**Pattern #19 archetype 4** — skill-lock policy is corpus-first explicit skill-archival convention. Could be sub-observation candidate at v57+ if other corpus subjects adopt similar lock-policy. N=1 stale-flagged at this decision.

**No new standalone candidates registered.** **20-streak ZERO-NEW-ACTIVE-CANDIDATES preserved at session 68.**

## Decision freeze

**Skill classification COMMITTED at session 68:**
- v1 `llm-wiki-routine.md` → PUBLIC-ARCHIVED ✅
- v2 `llm-wiki-routine-v2.md` → PUBLIC-ARCHIVED ✅
- v2.1 `llm-wiki-routine-v2.1.md` → IN-FLUX ✅
- `brain-setup.md` → IN-FLUX ✅
- `new-project.md` → IN-FLUX ✅

**Future skill changes require:**
- New skill addition: append to this policy file with IN-FLUX status
- Skill version-up (v2.1 → v2.2): mark v2.1 as PUBLIC-ARCHIVED at codification time
- Skill retirement: mark as PUBLIC-ARCHIVED + deprecation header

## v27 HIGH bundle status

| Item | Status |
|---|---|
| #1 Vault refactor | ✅ COMPLETE session 67 |
| #2 Publishing strategy | ✅ COMPLETE session 68 |
| #3 Skill-lock policy | ✅ COMPLETE session 68 (this file) |
| #4 Public-release decision | ✅ COMPLETE session 68 |
| #5 Vault license decision | ✅ COMPLETE session 68 |

**v27 HIGH BUNDLE: 100% COMPLETE.** 36-session deferral resolved.

**Remaining: pre-launch execution checklist (operator action; ~30-60 min):**
- Anti-leak grep
- (C) prefix audit
- Apply skill-lock headers to v1 + v2
- `gh repo create --public agentic-ai-second-brain` (or final operator-confirmed name)
- Add 11 repo topics
- Submit 3 skills to Anthropic skills marketplace
