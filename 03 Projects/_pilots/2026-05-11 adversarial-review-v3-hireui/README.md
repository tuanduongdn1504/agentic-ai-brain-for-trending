# Pilot: Adversarial-Review Comparison v3 — hireui real monorepo

> **Started:** 2026-05-12 (Step 0.E vault meta-folder creation; heavy run pending operator-scheduled block)
> **Status:** in-progress (Step 0 prep partial; Steps 0.A-0.F + 1-5 pending heavy run in Session A)
> **Target monorepo:** `/Users/Cvtot/monorepo/hireui` (pnpm monorepo: Next.js 14 web + Expo SDK 55 mobile)
> **Real feature scope:** Concept 6 deferred_count schema implementation (closes last 🔴 HIGH gap in v2 KJ OS integration plan)
> **Pilot branch (when created):** `agent/pilot-2026-05-11-adversarial-review` from `agent-dev`

---

## Pilot intent (3 layers)

1. **Pattern #76 empirical comparison** — BMAD `bmad-review-adversarial-general` (Stratum A baseline, already deployed in hireui) vs codex-plugin-cc `/codex:adversarial-review` (Stratum B, NEW install) on real harness upgrade work
2. **Orthogonal overlay test** — does layering andrej-karpathy-skills (4 behavioral principles) on top of methodology harness change review character?
3. **Skills collection complement test** — do mattpocock/skills (full 19-skill install) add value without colliding with hireui's existing `cm-*` skill family? Tested via §3.5/§3.6 9-mechanism Duplicate-Skill Management Policy.

---

## Architecture (Hybrid Option 3+5)

| Session | CWD | Role |
|---------|-----|------|
| **Session A** | `/Users/Cvtot/monorepo/hireui` | Tool execution + real work + Day 1-4 measurement |
| **Session B** | `/Users/Cvtot/KJ OS Template` | Pilot meta-documentation + Day 5-7 findings + vault state sync |

Monorepo `.pilot-log/` is **ephemeral working memory** (gitignored).
Vault `pilot-log/` (this folder/pilot-log/) is **persistent record** — review outputs copied from monorepo at end-of-day.

---

## Day plan

| Day | Phase | Session | Duration |
|-----|-------|---------|----------|
| 0 (heavy run) | Step 0-5: pre-flight + tool installs + management policy + E2/E3/E4 hooks | Session A primary + Session B (5 min) | ~150-180 min |
| 1-2 | Step 6: Concept 6 deferred_count feature work | Session A | ~2-3h |
| 3 | Step 7: Stratum A vs B reviews on same diff | Session A | ~1-1.5h |
| 4 | Step 8: karpathy-skills overlay ablation | Session A | ~1h |
| 5-7 | Step 9: cross-comparison + findings | Session B | ~2-3h |
| 7 | Step 10: adoption decisions + vault state sync | Session B | ~45 min |

**Total operator time:** ~9-11h spread over 1 week.

---

## Quick links

- **Setup plan (authoritative; v3.2):** `/Users/Cvtot/KJ OS Template/04 Reviews/(C) 2026-05-11 adversarial-review pilot v3 - hireui real monorepo.md` (1,761 lines)
- **v2 KJ OS integration plan (source of Concept 6 feature):** `/Users/Cvtot/KJ OS Template/03 Projects/product/hireui-harness/(C) 2026-05-06 v2 changes - integrating KJ OS concepts.md`
- **hireui CONSTITUTION (I-1 to I-7; I-8 to be added Step 0.F):** `/Users/Cvtot/monorepo/hireui/CONSTITUTION.md`
- **hireui root CLAUDE.md:** `/Users/Cvtot/monorepo/hireui/CLAUDE.md`
- **v61 cc-sdd wiki (Pattern #76 N=1 baseline reference; DROPPED from v3 install):** `03 Projects/cc-sdd - Beginner Analysis/`
- **v62 codex-plugin-cc wiki (Stratum B install target):** `03 Projects/codex-plugin-cc - Beginner Analysis/`
- **v63 andrej-karpathy-skills wiki (overlay layer):** `03 Projects/andrej-karpathy-skills - Beginner Analysis/`
- **mattpocock/skills upstream:** [github.com/mattpocock/skills](https://github.com/mattpocock/skills) (69.7K stars / MIT; full-install per §3.5)
- **Pilot ranking authoritative:** `_state/pilot-ranking-2026-05-07.md`

---

## Outstanding decisions before heavy run

### Advisory 4 — hireui `.gitnexus/` + `.harness-backup/` gitignore

**Status:** DEFERRED — pre-commit hook (per I-2 invariant) correctly blocked commit of `.gitignore` edit on `agent-dev` because `.gitignore` is not in HARNESS_PATTERNS. 4 resolution paths surfaced to operator (see "Advisory 4 status" below).

**Impact if not resolved:** untracked items remain visible in `git status` during pilot — cosmetic only; does NOT block any pilot work.

### Decisions deferred to pilot start (per pilot plan §3.6 D.1-D.4)

- **D.1:** install hooks at `.claude/settings.local.json` (per-developer) — default
- **D.2:** Concept 6 scope = `decisions.json` only Day 1 — default
- **D.3:** verify 4 deferred items still active during Step 6 — runtime decision
- **D.4:** all 8 expected `cm-*` skills verified present (2026-05-12 pre-flight) ✅

---

## Advisory 4 status (NEW 2026-05-12)

Discovered during Option B prep execution: hireui pre-commit hook (`scripts/git-hooks/pre-commit-branch-policy.sh`) classifies `.gitignore` as a project file (no HARNESS_PATTERN match). Modifying `.gitignore` on `agent-dev` (an agent branch) is blocked because project files must commit to `mobile/*` / `test/*` / `feat/*` branches per I-2 invariant.

**Resolution options (operator decision):**

1. **D-skip:** Live with `.gitnexus/` + `.harness-backup/` as visible-untracked during pilot. Cosmetic only. ✅ Lowest friction; recommended unless visual clarity matters.
2. **D-hook-amend:** Add `^\.gitignore$` to `HARNESS_PATTERNS` in `scripts/git-hooks/pre-commit-branch-policy.sh`. The hook script IS a harness file, so amend + .gitignore can commit together on `agent-dev`. Architectural change to team policy.
3. **D-feat-branch:** Create `feat/HIR-XXXX-gitignore-cleanup` branch from `main`, commit `.gitignore` there, PR to main. Respects existing rules. Slow.
4. **D-no-verify:** Use `git commit --no-verify` with explicit operator approval per I-1. Permitted only with operator chat approval.

**Pilot proceeds regardless of choice.** Decision can be made anytime before pilot week ends.

---

## How to resume pilot mid-stream

If pilot interrupted, on resume:

1. Read `.cm/CONTINUITY.md` (hireui) — current branch + last commit + active blockers + skill-management state section (after E5)
2. Read pilot plan v3.2 — find current Step
3. Read most recent `pilot-log/dayN-*.md` (this folder) — find last captured artifact
4. Read most recent `_bmad-output/sessions/(C) YYYY-MM-DD pilot-v3-*.md` (hireui) — find session-level state
5. `git -C /Users/Cvtot/monorepo/hireui status` + `git -C /Users/Cvtot/monorepo/hireui log -10 --oneline` — verify disk state
6. Resume at next-incomplete Step
