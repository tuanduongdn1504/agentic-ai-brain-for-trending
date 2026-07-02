# (C) loop-engineering — Pilot Methods Menu (24 methods)

**The one-line thesis for YOUR workflow:** you already run loops — the vault's autopilot-research topics, scheduled tasks, `/loop`, and the wiki-ship routine itself are L1/L2 loops that grew organically. loop-engineering gives you the **missing operational discipline**: durable state files, budget governance with a kill switch, a REJECT-first verifier, graduation criteria, and a scorer that tells you what's missing. Most of the value is **borrow-by-hand (zero install)**.

**Fence (applies to all B/D methods):** pin commit `f18df04` · prefer running CLIs **from the pinned clone** (`node tools/loop-audit/dist/cli.js`) over npx — zero install; if npx: `npm-security-check` + `install-snapshot` first (supply chain verified benign at this commit: no postinstall/network calls) · **never start any loop above L1 report-only** (the repo's own week-one rule) · set a token budget + kill switch BEFORE scheduling anything · hireui work per its CONSTITUTION (I-2 `agent-*` branch, I-8 operator-installs, GitNexus-first) · never `--dangerously-skip-permissions`.

---

## A — Read + map (zero risk, ~1–3h total)

- **A1 · Read the spine.** README → `docs/concepts.md` → `docs/primitives-matrix.md` → `docs/loop-design-checklist.md`. You'll recognize your own autopilot pattern formalized. *(~45 min)*
- **A2 · Read the two origin essays.** Osmani's addyosmani.com/blog/loop-engineering + Greyling's Substack companion. You already hold Osmani's other half (agent-skills v184) — this completes the 2026 arc: skills = what the agent knows; loops = the system that runs it.
- **A3 · Gap-map your existing loops.** Table your real loops (autopilot-research, wiki-ship routine, scheduled tasks, memory consolidation) against the loop anatomy: schedule / triage / **state** / worktree / maker / **checker** / gates / **budget** / **run-log**. Prediction: state+gates you have; budget/run-log/formal-verifier you don't.
- **A4 · Failure-mode pre-mortem.** Read `stories/why-we-killed-ci-sweeper.md` (8M tokens in 48h; 4-point cascade: no L1 → verifier same session → no branch allowlist → no budget) + `multi-loop-collision.md` + the dependency-sweeper **verifier-parity** lesson (verifier must run `npm ci` like CI, not cached `npm test`). This is the checklist before you ever let any loop auto-fix.

## B — Score what you have (read-only tooling, lowest-risk tool pilot)

- **B5 · loop-audit the VAULT.** `node tools/loop-audit/dist/cli.js "/Users/Cvtot/KJ OS Template" --suggest` from the pinned clone. The 17-signal score will name your gaps (no loop-budget.md, no run-log, no formal verifier skill). Zero install, read-only — SkillSpector-class safety.
- **B6 · loop-audit HIREUI.** Same command against the hireui monorepo — scores its BMAD/agent-branch harness readiness.
- **B7 · loop-cost your autopilot cadence.** Map your scheduled sessions onto the per-pattern token model (noop/report/action × cadence) → a spend forecast for the claude-api-cost-optimization thread.
- **B8 · loop-sync drift check** on any project where LOOP/STATE/skills conventions get adopted (C-block below) — drift detection as a habit, the #81 discipline as a CLI.

## C — Borrow-by-hand the conventions (no install — the vault's preferred move)

- **C9 · Adopt STATE.md for the autopilot.** The 4-section spine (High Priority / Watch List / Recent Noise / run-log line) replaces ad-hoc thread state; complements MEMORY.md (facts) with *operational* state (what the loop acts on next).
- **C10 · Write the vault's LOOP.md.** Document your ACTUAL loops (wiki-ship, autopilot-research, consolidate-memory) with cadence/phase/gates/handoff — today that knowledge lives only in CLAUDE.md prose. One page, immediately useful to every future session.
- **C11 · Adopt the JSON run-log.** Append one line per wiki-ship/autopilot run: `{run_id, pattern, duration_s, items_found, actions_taken, escalations, tokens_estimate, outcome}` — the CC-observability thread's missing artifact, and it makes routine audits data-driven.
- **C12 · Adopt loop-budget.md + the 80/100 rule.** Daily caps per loop; ≥80% → report-only, ≥100% or `loop-pause-all` → exit. Wire into the claude-api-cost-optimization spec (hireui has no LLM yet → build-it-right, same as the v188 budget-guard steal — these two compose).
- **C13 · Port loop-constraints.md + its enforcer skill** into `05 Skills/`. Binding plain-English guardrails read before every action — your "ask before editing my notes" rule + path denylists, formalized the way the repo does it.
- **C14 · Port loop-verifier as a vault gate skill.** *"Default stance: REJECT until proven otherwise. Do not trust the implementer's claim that tests passed — run them."* Composes with doubt-driven-development (v184) and your verify rule; use as the checker in any maker/checker fan-out.
- **C15 · Port minimal-fix.** One-problem-per-invocation, smallest diff, never mark your own work done — the scope discipline for unattended fixes (ponytail-adjacent, but as a loop skill).

## D — Real loops on hireui (Goal #2 — the standing PILOT lever)

- **D16 · PR Babysitter at L1** (report-only, `/loop 10–15m` during work hours) on hireui PRs, on an `agent-*` branch. Watches CI/rebase/review state, writes `pr-babysitter-state.md`, never touches code. **A completed week of this = the first real Goal-#2 pilot artifact since v153.**
- **D17 · Daily Triage L1 for hireui.** Morning scan (CI, issues, commits) → STATE.md report. Composes with the BMAD harness; the story-verified payoff is calibration ("report-only is not wasted time — it calibrates triage").
- **D18 · Graduate ONE loop to L2 patch-only — only after the criteria:** 2 weeks of L1, <20% noise, verifier proven manually first, denylist documented, loop-audit ≥58 (the repo's own `l1-to-l2-graduation` bar). Candidate: dependency-sweeper with the verifier-parity lesson applied (`npm ci`, not `npm test`).
- **D19 · Maker/checker on the Candidate-Detail refactor.** Implementer agent + independent REJECT-first verifier (+ serve-sim v183 for visual verification) = the how-we-claude-code verify pattern, run as a loop step instead of a one-off.

## E — Vault-meta + corpus

- **E20 · Score the LLM-Wiki routine against the 10-section loop-design checklist.** The routine IS an L2 loop (report+ship with operator gates). Expect it to fail §8 Cost & Limits and §9 Observability — exactly what C11/C12 fix.
- **E21 · Changelog-drafter for `04 Reviews/`.** L1 draft-only weekly review digest from the wiki-ship log — low token cost, human approves.
- **E22 · Primitives inventory.** Walk the matrix's Claude Code column (`/loop`, scheduled tasks, cron, hooks, GitHub Actions, `.claude/agents`) and check what your harness already exposes TODAY — you have nearly the full column; the missing pieces are conventions, not features.
- **E23 · Issue-triage loop for the autopilot topic queue.** Propose-only ranking of pending research topics (2h–1d cadence) → STATE.md — turns topic selection from ad-hoc into a triaged loop.
- **E24 · Contribute a failure story (optional, outward-facing — ask-first).** *"Failures are first-class content"*: the vault's own v56 4-tool-thrash or the v167 subagent-context postmortem is exactly their genre. Publishing = external action → operator decision.

---

**Recommended ladder:** **A1→A3→A4** (map + pre-mortem, ~2h, zero risk) → **B5** (score the vault from the pinned clone, zero install) → **C9+C11+C12** (state file + run-log + budget/kill-switch — the three conventions the score will flag; C12 composes with the v188 OpenMontage budget-guard steal) → **C14** (REJECT-first verifier into `05 Skills/`) → **D16** (hireui PR-babysitter, L1 report-only, `agent-*` branch = **the Goal-#2 artifact**) → only then **D18** (L2, per the graduation criteria).

*Why this ladder:* it follows the repo's own doctrine (L1 before L2; budget before schedule; verifier before autonomy), each rung is independently useful, and rungs 1–5 require installing nothing.
