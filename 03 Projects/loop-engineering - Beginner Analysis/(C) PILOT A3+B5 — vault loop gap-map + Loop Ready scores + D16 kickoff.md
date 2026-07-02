# (C) PILOT A3+B5 — vault loop gap-map + Loop Ready scores + D16 kickoff

**Executed:** 2026-07-02 · **Fence honored:** pinned clone `f18df04` · CLIs run from the clone (`node tools/loop-audit/dist/cli.js`) — **zero installs** · read-only (nothing scheduled, nothing written into vault/hireui) · no loop started (L1 rule intact — nothing running at any level yet).
**Status:** A3 ✅ DONE · B5 ✅ DONE (+ the D16 baseline half of B6) · **D16 = NEXT, kickoff pack below (blocked only on the I-8 operator gate).**
**Corpus note:** this is the first executed pilot motion against the standing PILOT lever ("zero piloted" since v153) — the *completed Goal-#2 artifact* bar is D16's week of committed runs, not this doc. Shim's pilot-lever line will need updating when D16 completes (flag for the next ship/audit).

---

## 1 · A3 — inventory: what actually loops around this vault today

Enumerated live (session 2026-07-02): `mcp scheduled-tasks list` → **0 tasks** · `CronList` → **0 jobs** · vault root has **AGENTS.md but no STATE.md / LOOP.md / loop-budget.md / loop-run-log.md** · `.claude/skills` + `.claude/agents` exist but are **empty** · `.claude/worktrees` exists (branch/worktree isolation is real) · no `.github/workflows`, no `bin/`, no `evals/` (the autopilot-drain/evals infrastructure from the pilot-thread memories lives in a **different repo**, not this vault).

**Headline A3 finding: the vault has NO always-on layer at all right now — every loop is operator-fired.** That is a *choice* consistent with L1 discipline (human fires, human gates). The gap is not autonomy, it's **instrumentation**: the loops that do run (wiki ships, ~1–2M workflow tokens each) leave no structured run-log, no budget accounting, and no formal verifier artifact.

### Gap-map: vault loop systems × the loop anatomy

| Anatomy element | Wiki-ship routine (v2.6) | Autopilot-research | Memory consolidation | Ad-hoc `/loop` / ScheduleWakeup |
|---|---|---|---|---|
| **Schedule** | ✗ operator-fired | ✗ operator-fired (other repo) | ✗ manual | session-scoped only |
| **Triage** | ✅ Phase 0.9 gate (strong, bespoke) | ✅ anchor-validation gate | ✗ | ✗ |
| **Durable state** | ⚠️ rich but bespoke (shim + `_state/03c` + `_patterns/06`) — prose, not machine-readable | ⚠️ memory files + output docs | ⚠️ MEMORY.md | ✗ none persists |
| **Worktree/branch isolation** | ✅ every ship on `wiki/*` branch; `.claude/worktrees` | ✅ own repo | n/a | ✗ |
| **Maker/checker** | ⚠️ REAL discipline (`feedback_wiki_verify_independently_check_collisions`, hand-verify) but **no separate verifier artifact** — the checker lives in a memory rule + habit | ⚠️ partial (validation gate) | ✗ | ✗ |
| **Human gate** | ✅ strongest element — operator merges every ship | ✅ operator reads output | ✅ | ⚠️ varies |
| **Budget / kill switch** | ✗ none formal (~1–2M subagent tok/ship, unaccounted) | ✗ | ✗ | ✗ |
| **Run-log** | ⚠️ prose (03c entries + commit messages) — no structured per-run record | ⚠️ prose | ✗ | ✗ |
| **Constraints file** | ⚠️ rules live in CLAUDE.md prose ("ask before editing", (C)-prefix, branch rule) — not a machine-checkable `loop-constraints.md` | — | — | — |

**Verdict on ourselves (the loop-engineering framing):** the wiki-ship routine is an **L2-equivalent loop running on L0 instrumentation** — excellent triage + gates + isolation, zero cost observability, no structured run history, checker-as-habit instead of checker-as-artifact. Exactly the profile the repo's scorer predicts for organically-grown loops.

## 2 · B5 — Loop Readiness scores (run 2026-07-02, from the pinned clone)

| Target | Score | Level | Signals present | Signals absent |
|---|---|---|---|---|
| **Vault** (`KJ OS Template`) | **25/100** | **L0** | AGENTS.md (+9) · loop-activity (+6, git history — amusingly the v189 ship commit itself) · base 10 | state file · triage skill · verifier · LOOP.md · safety doc · constraints · budget doc · run-log · budget skill · .github · MCP-mention · worktree-mention · registry |
| **hireui** (D16 baseline) | **32/100** | **L0** | AGENTS.md · `.github/workflows` ("strong dogfooding signal") · base | same as vault **plus zero loop-activity evidence** — which is precisely what D16 week-one manufactures |

Full JSON + `--suggest` output archived in the session scratchpad; re-run anytime with:
`node <clone>/tools/loop-audit/dist/cli.js "/Users/Cvtot/KJ OS Template" --json`

### Which auditor recommendations actually apply to a knowledge vault (my read)

- **Real gaps, worth closing (map to the menu's C-block):** STATE.md (→C9) · LOOP.md documenting the real loops (→C10) · loop-run-log.md JSON appends (→C11) · loop-budget.md + 80%-report-only/100%-kill-switch (→C12) · loop-constraints.md + enforcer (→C13) · a **verifier artifact** in `.claude/agents/loop-verifier.md` (→C14 — turns the verify habit into an inspectable, reusable checker) · a triage skill for the wiki/topic backlog (→E23 later).
- **Partial / document-only:** worktree + MCP signals — the vault already *does* both; a LOOP.md section naming them flips the signals honestly.
- **N/A for this vault (do NOT chase the score):** `.github/ISSUE_TEMPLATE` + CI workflows, `patterns/registry.yaml` — reference-repo conventions; adopting them here would be scaffolding-for-the-scorer, the exact failure the Deep Dive flagged ("the scorer measures scaffolding, not quality").
- **Projected score if C9–C14 land + one committed report-only run:** comfortably ≥78 numerically — but the honest bar is *maintained* run-log/budget after two weeks, not the number.

### ⚠️ Operator decision needed before the C-block (naming rule conflict)

loop-audit only detects the conventions under their **exact names at repo root** (`STATE.md`, `LOOP.md`, `loop-budget.md`, `loop-run-log.md`, `loop-constraints.md`). The vault rule says Claude-authored files carry a `(C)` prefix. **These five would be Claude-authored root files without the prefix — needs your explicit sign-off** (or we keep the prefix and accept that the scorer won't see them; the discipline still works, the badge doesn't). Not executed in this pilot step for exactly this reason.

## 3 · D16 kickoff pack — hireui PR-Babysitter, L1 report-only (the Goal-#2 artifact)

**Baseline:** 32/100 L0 · no state file · no verifier · no loop-activity evidence. **Target:** one week of L1 report-only runs, committed on an `agent-*` branch = the first completed Goal-#2 pilot artifact since v153.

**Step 1 — operator installs (I-8 gate; ~5 min, from the pinned clone):**
```bash
CLONE="/private/tmp/claude-501/-Users-Cvtot-KJ-OS-Template/78024afc-4d5a-417a-a0c8-1b107c4c8057/scratchpad/loop-engineering"  # or re-clone + git checkout f18df04
cd /Users/Cvtot/monorepo/hireui && git checkout -b agent-loop-pr-babysitter
mkdir -p .claude/skills .claude/agents
cp -r "$CLONE/starters/pr-babysitter/.claude/skills/pr-review-triage" .claude/skills/
cp "$CLONE/starters/pr-babysitter/.claude/agents/loop-verifier.md" .claude/agents/
cp "$CLONE/starters/pr-babysitter/pr-babysitter-state.md.example" pr-babysitter-state.md
cp "$CLONE/starters/pr-babysitter/LOOP.md" LOOP.md          # then edit: L1, cadence 15m work-hours, hireui gates
cp "$CLONE/templates/loop-budget.md.template" loop-budget.md # then edit: caps below
cp "$CLONE/templates/loop-run-log.md.template" loop-run-log.md
```
*Read each file after copying (they're short markdown).* Note: root `LOOP.md`/state files inside hireui follow **hireui's** conventions, not the vault's (C)-prefix rule — but confirm against its CONSTITUTION.

**Step 2 — budget + kill switch BEFORE scheduling (the fence, and the repo's own rule):** in `loop-budget.md`: PR Babysitter **max 2 runs/hour · max 500k tokens/day · 0 sub-agent spawns in week one (L1)**; kill switch = `loop-pause-all` line in `pr-babysitter-state.md` (any run must exit immediately if present) + simply stopping the `/loop`.

**Step 3 — run it, week one, report-only.** From hireui root, during work hours, in a Claude Code session:
`/loop 15m` → *"Run the pr-review-triage skill in L1 REPORT-ONLY mode: read open PRs' CI/review/rebase state, update pr-babysitter-state.md (High Priority / Watch / Noise), append one JSON line to loop-run-log.md ({run_id, pattern:"pr-babysitter", duration_s, items_found, actions_taken:0, escalations, tokens_estimate, outcome:"report-only"}). First read loop-budget.md — if ≥80% of the daily cap, note it and exit; if ≥100% or loop-pause-all is set, exit immediately. NO pushes, NO PR comments, NO fixes, NO merges — propose in the state file only."*
Commit the state + run-log diffs on the `agent-*` branch daily.

**Step 4 — the artifact + the graduation decision.** After ~1 week: the branch holds real state diffs + a JSON run history → **that branch IS the Goal-#2 artifact**. Then apply the repo's own L1→L2 bar before any auto-fix: 2 weeks L1 · <20% noise · verifier proven on a manual case first · denylist documented in `loop-constraints.md` · `loop-audit . ≥58`. (Week-one lesson to pre-load from the stories: if it ever graduates, the **verifier must run hireui's exact CI install path** — the cached-`npm test` false-APPROVE story.)

**Fence recap (unchanged):** pin `f18df04` · never above L1 without the graduation bar · budget + kill switch exist BEFORE the first scheduled run · `agent-*` branch (I-2) · operator installs the skills (I-8) · never `--dangerously-skip-permissions`.

---
*A3+B5 executed inline this session; loop-audit outputs archived at `scratchpad/b5-audit.txt` + `scratchpad/d16-baseline.txt` (session-scoped). Next after D16: E20 (score the wiki routine against the 10-section checklist) + the C-block pending the naming-rule sign-off above.*
