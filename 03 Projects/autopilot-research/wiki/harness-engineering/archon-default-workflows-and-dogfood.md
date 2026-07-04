# Archon's shipped workflows + "using Archon to build Archon"

> Companion to [[archon-harness-builder-anchor]]. Two halves: (1) what the **20 bundled default workflows** actually encode (ground truth from the YAMLs, not the README), (2) how the Archon repo itself is harness-engineered — the closest running instance of the "dark factory" direction.

## Source

- `.archon/workflows/defaults/` (20 YAMLs; dive read fix-github-issue, piv-loop, adversarial-dev, ralph-dag, idea-to-pr, workflow-builder in full) + `.archon/workflows/maintainer/` + `.claude/skills/archon-dev/` (SKILL + plan/review cookbooks) + repo CLAUDE.md/AGENTS.md — Workflow `wf_8a0f2da5-1d0`.

## The 20 defaults (README says 19 — table omits `archon-test-loop-dag`)

- **`archon-fix-github-issue` — 28 nodes**, Cole's stated daily driver: classify (haiku-tier) → bug/feature routing → investigate/plan → implement → deterministic validation → PR → smart review → self-fix.
- **`archon-idea-to-pr`** — plan → implement → validate → PR → **5 parallel review agents** (code-review, error-handling, test-coverage, comment-quality, docs-impact) → self-fix. The same 5-lens review fan-out recurs in fix-github-issue.
- **`archon-piv-loop`** — the Dynamous "PIV" (Plan-Implement-Validate): 9 nodes = 6 AI + 3 deterministic, fresh-context implementation loop, human review between iterations.
- **`archon-ralph-dag`** — Ralph loop as a *bounded* DAG: PRD-input detection, implement loop `max_iterations: 15` + `fresh_context`, state in JSON/markdown files — the "Ralph but with rails" answer to [[external|workflow-ai-coding/overview]].
- **`archon-adversarial-dev`** ⭐ — **three-role GAN-inspired state machine** in one loop node, state via `$ARTIFACTS_DIR/state.json`: **Contract Negotiator** (proposes 5–15 verifiable sprint criteria, then re-reads them *as its own adversary* and tightens) → **Generator** ("build defensively — the evaluator's job is to break you"; on retry must address every failed criterion) → **Evaluator** (read-only on source, Bash-only runtime testing, "You are not helpful. You are not generous. You are an attacker.", scores 1-10, **no curve, ALL criteria ≥7 to pass**, feedback with file:line + failing curl commands). Fresh evidence for Storm Bear **Pattern #76** (adversarial subagent review) — a THIRD implementation stratum: **workflow-encoded role state machine** (vs cc-sdd's architectural role-separation and codex-plugin-cc's prompt-framing).
- **`archon-workflow-builder`** — a workflow that builds workflows (scan codebase → extract intent JSON → generate YAML → validate → save). Meta-level dogfood.
- Rest: architect, assist, comprehensive-pr-review, create-issue, feature-development, interactive-prd, issue-review-full, plan-to-pr, refactor-safely, remotion-generate, resolve-conflicts, smart-pr-review, test-loop-dag, validate-pr.
- **Model routing in the shipped YAMLs matches the video's economics:** haiku/small for classification, medium for planning/review, large only for implementation loops. **The live-built GSD workflow was never shipped** — no `archon-gsd.yaml` exists (video: "I might push it").

## Maintainer layer — the incremental dark factory

`.archon/workflows/maintainer/`:

- **`repo-triage`** — 5-node DAG: label+dedup issues, link PRs↔issues, 90-day closed-dedup check, stale-nudge at 60d. **Conservative matching (prefer false negatives), 3-day clock guards before any destructive action, idempotent via `.archon/state/`, `DRY_RUN` + `SKIP_<NODE>=1` flags.**
- **`maintainer-standup`** — parallel gather (git, GitHub API) → Sonnet synthesis → dated brief; **`-minimax` variants swap synthesis to Pi/MiniMax M2.7** for token economy + to dodge nested-Claude-Code hangs (#1067). Docs: run the Claude version first to validate state, then let the cheap variant take routine runs — **staged model-downgrade discipline**.
- **`maintainer-review-pr`** — diff-aware dynamic review-aspect selection (error-handling lens only if try/catch touched, etc.), parallel aspect nodes, consolidated draft comment. **`marketplace-pr-review-and-merge`** — Haiku + deterministic security scan, **auto-merges** clean marketplace submissions (the one true no-human-gate path, scoped to lowest-risk file class).

## The dev-skill layer

`.claude/skills/archon-dev/` routes intents to **10 cookbooks** (research / investigate / prd / plan / implement / review / debug / issue / commit / pr). Plan cookbook: 8 phases, parallel explorer/analyst/researcher agents, **actual code snippets + file:line citations required** before writing the plan ("one-pass implementation success"). Review cookbook: 9 phases, 2-4 parallel lenses incl. a **silent-failure-hunter**, dedupe against implementation artifacts, verdict → `gh pr review`. Repo CLAUDE.md: 13 rules (KISS/YAGNI/fail-fast/strict-TS/Zod, **"no autonomous cross-process mutation — surface ambiguous state to users"**, no AI attribution in commits).

## Key Takeaways

- **The defaults are the real product.** Cole's stated primary use of them ("two uses: run out of the box, or reference points for your coding agent to build something custom") makes the 20 YAMLs a public corpus of harness patterns — the open-source equivalent of what Stripe/StrongDM keep private.
- **Adversarial-dev is the headline artifact**: contract-negotiate → build-defensively → attack-and-score with hard thresholds, state on disk, evaluator write-blocked from source. Registerable evidence for Pattern #76 at v66 mini-audit (3rd mechanism stratum).
- **The maintainer workflows are a dark factory with brakes**: conservative dedup, 3-day clocks, DRY_RUN, auto-merge only for the lowest-risk file class. That's the production-shaped version of the no-human-review experiment — and it contradicts the hype reading of "dark factory" in a useful way.
- The `-minimax` maintainer variants are the first corpus instance of **per-workflow model-vendor downgrade for routine maintenance runs** — cost discipline one level above per-node model routing.
- Our own loop-engineering pilot (v189 PR-babysitter) is convergent with `repo-triage` + `maintainer-standup` at smaller scale — see pilot menu method B-block.

## Cross-links

[[archon-harness-builder-anchor]] · [[archon-workflow-primitives]] · [[external|multi-agent-orchestration/_index]] (orchestrator-worker shape) · [[external|workflow-ai-coding/core-patterns]] (Ralph bounded) · Storm Bear Pattern #76 evidence queue (v66)
