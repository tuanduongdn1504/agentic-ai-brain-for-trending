# (C) Pilot methods — Archon / harness-builder knowledge → Storm Bear working flow

> **Source ingest:** srx9iwnjK2M (Cole Medin Archon live guide) + coleam00/Archon double deep-dive, 2026-07-04. Wiki: `wiki/harness-engineering/archon-*` (4 articles). Verification: `wf_8a0f2da5-1d0`.
> **Context:** pilot pressure standing (cc-sdd #1 / codex-plugin-cc #1.5 / free-claude-code #2 ranked, 0 deployed). Archon is a direct contender in the same decision: **cc-sdd = adopt a harness; Archon = build your own**. That's the exact fork the video frames.
> **22 methods, 5 buckets.** ⭐ = headline. Each method: what / where / effort / measure.

---

## A. hireui (Goal #2 — real-software deployment target)

**⚠️ Constitution first:** any Archon-adjacent pilot in hireui must respect ITS rules (I-2 `agent-*` branch prefixes — Archon's `--branch` flag makes this trivial; I-8 operator-only skills; GitNexus-first). Archon runs the Agent SDK in `bypassPermissions` — treat any Archon host as a **privileged CI runner**, single-developer only.

- **A1 ⭐ The comparison-pilot that resolves the fork: Archon vs cc-sdd on the same ticket class.** Pick 2-3 real hireui GitHub issues (bug-class, bounded). Week 1: fix via cc-sdd discipline (already ranked #1). Week 2: fix the siblings via Archon `archon-fix-github-issue` (~30-min quick install on your machine, `--branch agent/fix-issue-N`). Measure: wall-clock-to-mergeable-PR, review findings caught, tokens (ccusage), operator interventions. Write-up in `04 Reviews/` feeds the v66 mini-audit AND finally converts "0 pilots deployed" → 1-2. Effort: ~1h setup + 2 weeks background.
- **A2 Zero-install pattern extraction — the 5-lens parallel review.** Archon's shipped review fan-out (code-review / error-handling / test-coverage / comment-quality / docs-impact) is a prompt architecture, not a product. Encode it as a hireui Claude Code command or graft into the RUNNING v189 D16 PR-babysitter (read the loop-engineering memory file before touching the loop). Effort: ~1h. Measure: findings per PR vs current single-pass review.
- **A3 `until_bash` discipline — deterministic loop exits.** Anywhere an agent loop decides "I'm done" in hireui work, replace self-report with a test-suite exit condition (loop ends when `pnpm test` exits 0, hard `max_iterations` cap). This is Archon's strongest primitive and it's portable to plain Claude Code loops/hooks. Effort: constraint-line + hook, <1h.
- **A4 Subscription/ToS ADR before any team harness use.** Policy flipped 3× in 3 months (04-03 restriction → reinstate-with-catch → credits plan PAUSED; current: Agent SDK draws from sub limits, **multi-user on plan auth prohibited**). Record the fork as an ADR next to the CMA data-residency ADR: personal pilots = subscription; anything multi-user/team = API keys. Re-check support article #15036540 the week of any deploy. Effort: 30 min.
- **A5 Security constraint lines from Archon's own docs:** (1) secrets are collected in a separate terminal the agent never sees — adopt for any hireui credential flow involving agents; (2) `stripCwdEnv` expectation: agents must not inherit target-repo `.env` — verify hireui's harness does the equivalent; (3) read-only reviewer tool-allowlists (`[Read, Grep, Glob]`). Effort: audit + 3 constraint lines, ~1h.
- **A6 Advisor-tool leg (model layer, no Archon needed).** The advisor tool is real (Claude Code v2.1.98+): Sonnet/Haiku executor + Opus advisor, vendor-claims −11.9% cost at +2.7pts. Try it on the Candidate-Detail refactor sessions; measure with the claude-code-observability OTel leg. Effort: config flag + 1 week of normal work.

## B. Vault + autopilot-research pipeline (this loop improving itself)

- **B1 ⭐ Pre-registered claim contracts (adversarial-dev port).** Archon's adversarial-dev encodes: negotiate a contract of 5-15 *verifiable* criteria → build → attacker scores ALL criteria ≥7 or fail. Our verify passes already attack, but the **contract step** is only ad-hoc (hoidanit ep-3 pre-registered 8 claims; this pass enumerated claims after reading). Make it standard: every ingest writes the high-risk claim list BEFORE articles, and the verify workflow scores against it. Effort: routine-skill edit, ~30 min; candidate for routine v2.2 codification list.
- **B2 ⭐ Deterministic ship-gate (`until_bash` for wiki ships).** The hoidanit ship's 18 false BROKEN_LINK findings came from reviewers re-deriving state. Replace with a bash link-validator script (grep `[[...]]` targets against the file tree) run as a hard gate before commit — reviewer agents only judge content. Effort: ~40-line script in `bin/`, 1h.
- **B3 Silent-failure catalog for OUR skills.** Archon documents 12 params that silently no-op. Our pipeline has the same class of traps (flaky-shell stdout drops, grep-vs-awk, python3 shim, worktree branch races). Write `skills/(C) silent-failures.md` as a first-class catalog agents read before running the routine. Effort: 1h, mostly harvesting from memory files.
- **B4 Maintainer-workflow discipline into the v189 loop.** Port repo-triage's guards into the PR-babysitter: state-file idempotency (never re-comment), DRY_RUN flag, conservative matching (prefer false negatives), 3-day clocks before anything destructive, stale-nudge at N days. Effort: ~2h against the existing loop files (read `project_loop_engineering_pilot_thread` memory first — fence + graduation bar apply).
- **B5 Staged model-downgrade for cron runs.** Archon's `-minimax` maintainer variants encode: expensive model validates the workflow first, cheap model takes routine runs. Apply to the nightly autopilot cron: first run of any new topic on the default model, subsequent routine digests on Haiku. Effort: routine config note, 30 min.
- **B6 Dynamic skill content.** Archon's SKILL.md injects live state at load time (`!`archon workflow list``). Our project-local skills are static; add live-state injection (e.g., yt-pipeline skill showing current `_inventory.md` tail, topics-queue status) so agents stop re-deriving coverage. Effort: 1h.

## C. Personal harness / research thread

- **C1 Sandbox-feel session.** `brew install coleam00/archon/archon` on a throwaway repo (NOT the vault — scope clamp; NOT hireui first) and run `archon-piv-loop` + the visual builder once. Decide adopt/extract/drop with hands-on data before A1. Effort: 30-60 min.
- **C2 Watch-list → topics-queue:** (a) **Omnigent** "meta-harness for EVERY coding agent" (oGE_Dwz-rMk, 2026-06-15) — possible layer above harness builders; (b) `coleam00/dark-factory-experiment` repo — does the no-human-gate experiment actually run?; (c) **The Book of Archon** (10 chapters) as pedagogy-tier drain; (d) Pi+Archon video (XSmI7OYd7iM) — pairs with the elicit pi thread. Effort: 4 queue lines.
- **C3 Workflow-builder meta-pattern for the vault:** Archon ships a workflow that builds workflows (scan → intent JSON → YAML → validate → save). Our equivalent: a skill that drafts new project-local skills from a transcript of a manual session. Park as v2.2 candidate — don't build speculatively (Rule 2). Effort: 0 now.

## D. Scrum coaching practice

- **D1 ⭐ "Encode YOUR process, don't adopt mine" as a coaching module.** Archon's enterprise pitch — teams can't adopt B-MAD/GSD because it changes how they work; a builder wraps the process they already trust — is the agile-adoption argument transposed to AI. Build a 1-pager: DoD/DoR/working-agreements → workflow gates (plan gate, deterministic test gate, human approval gate, review fan-out). Use the GSD "enterprise theater" quote as the foil. Effort: 2h deck work.
- **D2 The review-gate maturity spectrum datum set:** Stripe (1,300 AI PRs/wk, **human-reviewed**) ↔ Archon maintainer layer (auto-merge only lowest-risk file class, 3-day clocks) ↔ StrongDM (32K lines, **zero review**). Three verified poles for a team conversation on where review belongs as AI throughput grows. Effort: talking points, 30 min.

## E. Evals / measurement (falsify before believing)

- **E1 ⭐ "Sonnet + harness ≥ Opus bare" falsification.** Cole's claim is self-reported (sibling of Lopopolo claim #4). Run our `evals/` harness on a small hireui-shaped task set 3 ways: Opus bare / Sonnet bare / Sonnet + structured multi-stage workflow. Even N=10 tasks would be the corpus's first measured datapoint. Effort: ~half day; composes with prompt-evaluation pilot.
- **E2 `persist_session` vs fresh-context cache economics.** Fresh context kills bias AND cache warmth (cache-read ≈0.1×). Nobody has measured the trade. Instrument one repeated workflow both ways via ccusage/OTel. Feeds harness-economics article + claude-api-cost-optimization. Effort: ~2h.
- **E3 Edit-format micro-check.** Can Bölük's 6.7→68.3 was an *edit-format* effect (Hashline). Before trusting any agent's diff-application in our loops, note which edit format the harness uses; if a loop shows silent mis-edits, this is the first suspect. Effort: awareness line in silent-failure catalog (B3).

## Skip-list (explicitly not doing)

- **Don't build a harness builder** — Archon exists, MIT, 22.7K★; extraction beats reimplementation (Rule 2).
- **Don't run a dark factory on anything real** — StrongDM's zero-review is an experiment by its own authors; hireui CONSTITUTION forbids it anyway.
- **Don't deploy Archon multi-user on subscription auth** — clearly prohibited; API keys or nothing.
- **Don't install Archon into the vault repo** — scope clamp + it's a coding harness, not a librarian.
- **Don't quote "60% model / 40% harness" or "6.7%→70% PR acceptance" in any deck** — both corrected; use the verified formulations from the ledger.

## Recommended composition (if picking 3)

1. **A1** comparison-pilot (Archon vs cc-sdd) — converts the standing 0-deployed-pilots pressure into data on the exact adopt-vs-build fork.
2. **B1+B2** contract pre-registration + deterministic ship-gate — zero-install, this pipeline, this week.
3. **E1** Sonnet+harness falsification eval — cheapest way to know if the whole economic pitch holds on our tasks.

**Note for the operator:** the standing pilot ranking (`_state/pilot-ranking-2026-05-07.md`, outside autopilot write scope) lists cc-sdd #1 / codex-plugin-cc #1.5 / free-claude-code #2 — A1 makes Archon a co-#1 as the build-side of the same decision. Update the ranking file when you next touch Storm Bear state.
