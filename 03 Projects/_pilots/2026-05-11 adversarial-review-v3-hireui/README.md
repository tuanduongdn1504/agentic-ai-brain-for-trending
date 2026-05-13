# Pilot: Adversarial-Review Comparison v3 — hireui real monorepo

> **Started:** 2026-05-12 (Step 0.E vault meta-folder creation; heavy run executed 2026-05-12 + 2026-05-13)
> **Status:** ✅ **Day 0 + Step 6 + Step 7 + Step 10 ALL DONE 2026-05-13.** Step 8 operator triage + post-pilot fix sprint remaining (operator-driven). First pilot in vault history to complete full candidate → in-flight → fully-completed lifecycle.
> **Target monorepo:** `/Users/Cvtot/monorepo/hireui` (pnpm monorepo: Next.js 14 web + Expo SDK 55 mobile)
> **Real feature scope:** Concept 6 deferred_count schema implementation (closes last 🔴 HIGH gap in v2 KJ OS integration plan) — ✅ landed Step 6
> **Pilot branch:** `agent/pilot-2026-05-11-adversarial-review` (LOCAL-ONLY per 2026-05-12 branch policy amendment; 20 commits ahead of `agent-dev`, tip `6004dead`)
> **Headline results:** BMAD 18 findings + codex-neutral 2 + codex-adversarial 17 = 37 distinct findings (~19 unique real bugs after dedup). Pass 3 vs BMAD: 44% overlap + 9 codex-unique findings incl. 6 HIGH real bugs. Framing-vs-tool decomposition: MIXED (framing dominates breadth, tool dominates depth-of-execution-trace). Pattern #76 verdict: KEEP STAGED. See `pilot-log/step-10-final-analysis.md` for full ablation.

---

## ✅ FINAL RESULTS (2026-05-13 — Session B close-out vault state appends)

### Adoption decisions (FINAL)

- ✅ **KEEP BMAD `bmad-review-adversarial-general`** — Stratum A baseline; breadth + spec/scope/design-layer adversarial mandate (CRITICAL severity ceiling; 18 findings; 7 initial real bugs)
- ✅ **KEEP codex-plugin-cc `/codex:adversarial-review`** — Stratum B; depth + code-execution-trace + integration defects (HIGH severity ceiling; 17 findings; 12 initial real bugs; 9 codex-unique)
- ❌ **RETIRE codex neutral `/codex:review`** as standalone — only 2 findings on substantive 62-file diff; not standalone-useful (still callable on-demand for spot-checks)
- 🔧 **Stack pattern for next substantive harness diff:** combine BMAD adversarial + codex adversarial in parallel — complementary not redundant

### 4 Session B cross-session decisions — implementation status

| Finding | Resolution (Session B 2026-05-12 evening) | Vault doc ✅ | Code fix-now status |
|---------|-------------------------------------------|--------------|---------------------|
| F-02 Pattern #76 scope mismatch | design-challenge → KEEP STRICT framework-level definition | ✅ evidence-note appended `_patterns/03-active-candidates.md` line 596+ | n/a (doc-only) |
| F-03 B-A17 count doctored | real-bug → RENAME `attention_tag` → `recommended_severity` | n/a (hireui-side schema fix) | 🔜 post-pilot sprint Bucket 2 |
| F-04 Phase 2 auto-increment vapor | design-challenge → RETIRE to manual-only with re-eval trigger (>10 deferred items aging OR >2/week velocity 30 days) | n/a (hireui HIR-1162 ticket amendment) | 🔜 post-pilot doc fix |
| F-07 3 mattpocock misfit skills | real-bug → DELETE (20 → 17) — repeats 2026-05-06 Goodhart anti-pattern recognition | n/a (hireui-side skill deletion) | 🔜 post-pilot sprint |

### Goal #2 ROI ledger (FIRST measurable returns)

- **NEW Pattern #79 Tool-Level Adversarial Review as Skill candidate** for v66 mini-audit deliberation (N=2 evidence already accumulated: BMAD + codex-plugin-cc; potential N=3 if cc-sdd `kiro-review` qualifies independently)
- **5 routine v2.2 codification candidates** surfaced (pilot framing discipline / Phase 0 Pattern #76 verification checklist / skills-bundle-import discipline / scheduled-task auto-retry branch handling / HIR-1162 schema hardening)
- **HIR-1162 deferred_count schema validated under real B-A18 lifecycle** (filed 2026-05-12 count=1 attention_tag=null; resolved 2026-05-13 within 24h; sub-threshold lifecycle works as designed; 5 distinct schema flaws identified for hardening)
- **9-ranked-pilots / 0-deployed → 9-ranked / 1-fully-completed** — operator-deployment imbalance reducing for first time since v60. Pattern-observation > operator-deployment ratio: 100% → 11% (1/9)

### Vault state propagation — Session B FINAL appends

| Vault file | Change | Status |
|------------|--------|--------|
| `_patterns/03-active-candidates.md` | Pattern #76 evidence-note appended at line 596+ (Pass-3-revised numbers; tool-vs-framework distinction codified; NEW Pattern #79 candidate flagged for v66) | ✅ |
| `_state/pilot-ranking-2026-05-07.md` | "Completed pilot (2026-05-13)" section added at top; previous "In-flight" section preserved as historical | ✅ |
| `03 Projects/_pilots/2026-05-11.../README.md` | FINAL RESULTS section (this section) added | ✅ |
| `03 Projects/_pilots/2026-05-11.../pilot-log/STATUS.md` | "Session B FINAL — 2026-05-13" sub-section to be added | 🔜 |

### Remaining post-pilot work (NOT pilot-scope; operator-driven)

1. **Step 8 operator triage** — Session B classified 4 findings (F-02 / F-03 / F-04 / F-07); remaining 33 distinct findings await operator real-bug/false-positive confirmation in `pilot-log/step-8-triage.md` (~30-45 min)
2. **Post-pilot fix sprint** — 5 buckets, ~4-6h total. See `pilot-log/post-pilot-fix-sprint.md` (revised post-Pass-3 with 5 schema-hardening + 4 hook-enforcement-gap additions)
3. **Merge pilot → agent-dev → push origin agent-dev** — only after Step 8 triage + post-pilot fixes land

### Cross-references

- **Step 10 final analysis (canonical):** `pilot-log/step-10-final-analysis.md`
- **Vault Pattern #76 entry (with appended evidence-note):** `_patterns/03-active-candidates.md` lines 588-598
- **Pilot ranking completed-status:** `_state/pilot-ranking-2026-05-07.md` "Completed pilot (2026-05-13)" section
- **Pilot plan v3.2 (authoritative methodology):** `04 Reviews/(C) 2026-05-11 adversarial-review pilot v3 - hireui real monorepo.md`
- **Session A→B handoff doc:** `/Users/Cvtot/monorepo/hireui/_bmad-output/runbooks/session-a-to-b-handoff-2026-05-12.md`
- **hireui Step 10 closeout commit:** `6004dead` on `agent/pilot-2026-05-11-adversarial-review` (LOCAL-ONLY per branch-policy amendment)

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
