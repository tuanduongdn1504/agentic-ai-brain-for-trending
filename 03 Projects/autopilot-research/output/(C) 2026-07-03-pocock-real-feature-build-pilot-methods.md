# (C) Pilot methods — pocock-real-feature-build (2026-07-03)

> **Source topic:** `wiki/pocock-real-feature-build/` (Matt Pocock "Building a REAL feature with Claude Code", hX7yG1KVYhI, first-party, verified via `wf_8897fa8d-c95` + `gh api` ground-checks).
> **What's NEW vs the pocock-agentic-workflow menu (2026-06-30):** that menu piloted the *philosophy* (blank-slate harness, grill-me-as-plan-mode, Sand Castle spike). This one pilots the **worked-example mechanics**: the ubiquitous-language glossary, the grill→PRD→issues front-half as a pipeline, QA-plans-from-commits, the feedback-button-as-issue-filer, and the harness-evolution upgrades (4-phase loop, dependency selection, two-phase closure).
> **Ranking:** ★ = do-first. Effort = setup time. Angles: A hireui Goal #2 · B the glossary pattern · C QA + feedback loop · D personal harness + vaults · E Scrum coaching.

---

## A. hireui Goal #2 — the front-half pipeline on a real feature

**A1. ★ Run the full Pocock front-half on the Candidate-Detail refactor (zero install).** One session in hireui: dictate the rough goal → grill-me-style interrogation (agent explores GitNexus-first, asks one code-grounded question at a time, you answer WHY + trade-offs) → PRD **with module sketch reviewed by you** (interfaces only) → slice into GitHub issues with `blocked-by` relationships → you right-size the slices (merge the too-smalls). Stop before implementation if you want — the artifact set (grill transcript + PRD issue + sliced issues) is itself Goal-#2 evidence. Composes with the locked plan `.cm/outputs/plans/phase-2-candidate-screen-rework.md`; respects I-2/I-8 (no new skills installed — it's all prompting). ~1.5h. **This is the headline.**

**A2. ★ hireui `CONTEXT.md` ubiquitous-language glossary.** Materialize the Candidate-Detail vocabulary that keeps drifting: canonical tokens (navy `#002D79`, accent `#DC6803`, Roboto), r1-vs-r2 migration terms, "parity" (your locked definition: data/behavior/copy from web + layout from Figma r2), tab names, verified-timeline colors — each with **aliases to avoid** ("demo template", "pixel-copy", old hexes). Drop at repo root or feature dir; agents grep into it exactly as Matt's agents hit his. Directly attacks the drifted-token root cause. ~45 min, zero install.

**A3. Decide tests-per-module at PRD time.** Adopt the to-prd question — "which modules get tests?" — as a required PRD section in hireui's BMAD flow. Answer Matt-style: where harnesses already exist. Pairs with the how-we-claude-code verify pilot (phase-3 verify engine) for where they don't. ~15 min policy change.

**A4. Feedback button in hireui (the steal-the-pattern build).** TalentAxis already has real screens to QA. Build Matt's exact mechanism: an in-app feedback affordance → files a GitHub issue with AI-generated title (**route Haiku**, fall back to first-sentence truncation — his verified design) + current route + free-text/dictation. Suddenly every recruiter-facing QA pass produces agent-consumable tickets. This is a small, deployable LLM feature — nibbles at "hireui has no LLM yet" with a low-stakes first integration, per the cost-optimization spec's build-it-right rules. ~half day on an `agent-*` branch.

**A5. QA-plan-from-commits ritual.** After any agent-built PR (including D16 babysitter output): "Take the last N commits and create a QA plan as a GitHub issue — step-by-step, every user-visible part." Label it `human-only`. Close it when behavior drifts (Matt's source-of-truth hygiene). Zero install; adoptable today on PR #744's successor.

**A6. Dependency-graph issue selection for the loop pilot.** The verified harness upgrade: issues declare `blocked-by`; the loop picks only zero-blocker issues, and **closure happens at merge, not at implementation** (two-phase). Retrofit both rules into the v189 loop-engineering conventions (LOOP/STATE files) — they're the difference between a queue and a pile. ~30 min of convention edits.

**A7. Sandcastle comparison-spike (compose, don't duplicate).** The prior menu already has the Sand Castle spike; this topic adds the evaluation rubric from the real repo: 4-phase Plan→Implement→Review→Merge prompts, MAX_ITERATIONS=10, 4-parallel semaphore, per-commit tests+types. If/when you run that spike, score it against these five verified design points rather than "does it work."

## B. The glossary pattern everywhere (cheapest cross-cutting win)

**B1. ★ Vault `CONTEXT.md` for the autopilot project.** This vault already HAS a ubiquitous language nobody wrote down: *topic / drain / compile / anchor-miss / promotion / stale-flag / corpus-first / verifier-misfire / don't-re-fabricate*. Write the glossary with aliases-to-avoid; future sessions (and workflow subagents) grep it instead of re-deriving meanings. ~30 min. (Scope-safe: inside `03 Projects/autopilot-research/`.)

**B2. Port Matt's `domain-modeling` discipline into Brain-setup v2.** The vault's Brain-setup already cross-ported lazy-ADRs from `/grill-with-docs` (v57). The matured skill adds: **challenge-against-the-glossary** ("your glossary defines X, you seem to mean Y — which?") + `CONTEXT-MAP.md` for multi-context repos + create-files-lazily. Fold those three rules into the Brain-setup skill text next time it's touched. ~20 min.

**B3. Post-session glossary update habit.** Matt's loop: after each grilling/planning session, have the agent update the glossary with newly-minted terms, review the diff, commit it yourself. Adopt for hireui planning sessions and vault chess-moves sessions alike. Zero setup — a closing prompt.

**B4. Glossary-aware bug reports.** Once A2/B1 exist, report bugs *in glossary terms* ("bug in the materialization cascade" → "drift in the r2 token mapping") and watch retrieval precision jump. Free once the files exist.

## C. QA + feedback loop (day shift / night shift)

**C1. ★ Parallelize your QA with the running loop pilot.** You already run `/loop 15m` work-hours on hireui (v189, D16). Add the missing half: while the loop works, YOU hand-QA the latest merged output and file feedback issues (via A4's button or plain `gh issue create` with a title-generation alias). The loop consumes them next cycle. This is the exact day-shift/night-shift split, live, this week — and it's the strongest Goal-#2 artifact this topic offers beyond A1.

**C2. Per-commit gates in the loop verifier.** Matt's "crucial to success": tests + typecheck on EVERY commit, not per-run. The v189 verifier already proved `npm ci` parity; tighten it to reject any loop commit lacking a green test+typecheck run. ~15 min convention change.

**C3. Ship-one-way-then-correct for UI ambiguity.** Codify Matt's judgment call as a rule-of-thumb in the Candidate-Detail plan: when UI options are debatable (his ghost/real buttons → checkbox modal), skip the prototype phase, ship the cheapest option, and let a structured QA pass decide. Bounded by C1's feedback loop so corrections are cheap. Policy, zero setup.

**C4. Walk-back invariant for destructive flows.** His QA showstopper (not-a-git-repo → dir/DB desync → "walk back the creation") generalizes: any hireui flow that touches two stores (DB + storage/files) needs an explicit compensating-action note in its issue. Add as an acceptance-criteria template line. ~10 min.

## D. Personal Claude Code harness + vaults

**D1. ★ Allow-list curation pass (the 89-entry pattern).** Matt's `settings.local.json` is a curated 89-entry ALLOW-list — the live answer to "what does permission discipline look like." Run the existing `fewer-permission-prompts` skill over your transcripts, then hand-prune the result Matt-style (fine-grained: per-command git, per-domain WebFetch). ~30 min, immediate friction drop.

**D2. `/btw` side-questions habit.** Stop polluting long grilling/planning contexts with tangents — `/btw` keeps quick questions out of history (exit: space/enter/esc). Free; retrain the reflex.

**D3. Two-tier skill architecture audit.** Matt splits: global reusable skills (mattpocock/skills, 37) vs in-repo project skills (`.claude/skills/DB-TDD`, `to-prd-project`). Audit your `~/.claude` + per-repo skills against that split — anything repo-specific living globally gets moved into the repo (and hireui's live under I-8 registry). ~45 min.

**D4. Adopt grill-me + to-prd + to-issues from the source.** They're MIT, 154.5K★, verified verbatim (`skills/productivity/grill-me/SKILL.md` — two-tier, `disable-model-invocation: true`, code-first answering). Install into the vault sandbox first (I-8 keeps hireui operator-gated); compare against your A1 hand-rolled run to decide if the skills earn a permanent slot. ~30 min + one comparison session.

**D5. Explain-the-WHY prompt discipline.** The single highest-leverage grilling habit: every feature ask carries a why-clause so the agent can propose alternatives. Add one line to your personal CLAUDE.md/AGENTS.md: "If the user gives a WHAT without a WHY, ask for the WHY before planning." ~5 min.

**D6. "Look harder" as the standard correction.** When an agent claims something doesn't exist (a test harness, a file, a skill), the first response is a re-instruction with higher effort — not acceptance, not manual takeover. Note it in the vault's verifier discipline too: this run's ddd-verifier proved (again) that *can't-find ≠ doesn't-exist*. Free.

**D7. QA-plan skill authoring (close Matt's open loop).** He said "I haven't come up with a skill for this yet" — you can: a small `qa-plan` skill (input: N commits or a PR; output: step-by-step QA issue, human-labeled). Ship it to the vault skills dir; candidate for the skill-creator flow. ~1h.

## E. Scrum coaching angle

**E1. ★ Ubiquitous language as a team practice.** The DDD glossary is the classic dev↔domain-expert bridge — now with a third party at the table (the team's AI agents). Coach teams to keep ONE glossary consumed by all three audiences; acceptance criteria written in glossary terms. Workshop-ready with Matt's ghost/materialize example as the demo.

**E2. Grilling as refinement facilitation.** The Willow-Reagan model — "sit in a meeting and ask smart questions for hours" — is literally backlog refinement. Teach POs to run grill-me sessions against their own feature ideas before bringing them to the team; the 8-bullet convergence artifact IS the refined story set.

**E3. Day-shift/night-shift as a sprint pattern.** Humans do discovery/QA during the day; bounded agent queues burn down implementation between sessions. Frame for teams adopting agents: the human calendar shifts toward requirement-hardening + QA, and "velocity" moves to queue-throughput. Pairs with E1's shared vocabulary for writing the queue items.

**E4. Right-sizing stories for agent consumption.** Matt's slicing rubric (too small = agent-startup waste; too big = incoherence; merge the trivial into the substantive) is a concrete, teachable story-splitting heuristic for AI-augmented teams — more actionable than generic INVEST.

---

## Skip-list (deliberately not piloting)

- **Effect adoption** — Matt loves it; orthogonal to every current goal. Note the pattern (big testable service modules), skip the library.
- **Building a Sandcastle clone** — the package exists (`@ai-hero/sandcastle`); if AFK-in-Docker is wanted, spike the package (A7), don't rebuild.
- **Abandoning AskUserQuestion** — his token argument is dated (Claude 4.x token-efficient tool use) and his UI gripe is personal taste; your interview-first pilots (how-we-claude-code) already use it well. Keep both modes.
- **Anti-spec absolutism** — his "specs-to-code will never work" contradicts the running cc-sdd #1 pilot. Don't resolve by opinion: A1 (Pocock front-half) vs cc-sdd on comparable tickets IS the measurement; note he front-loads 22 min of grilling + a PRD anyway, so the two camps are closer than the rhetoric.
- **1,200-commit-scale imitation** — his repo earned its harness incrementally; don't pre-build harness for repos without the traffic.

## Critic's reframe

The video's surface lesson is "get an AFK loop." The durable lesson is the **shape of the human's remaining job**: explain the why, mint the vocabulary, review interfaces not implementations, right-size the queue, QA by hand, and feed everything back as structured issues. Every method above that costs under an hour (A2, B1–B4, C2–C4, D1–D2, D5–D6) is an instance of that shape — and they compound with the pilots already running (cc-sdd #1, loop-engineering v189, how-we-claude-code verify) rather than competing with them.

## Suggested composition (if you only do three)

1. **A1 + A2 together** (one session): grill→glossary→PRD→issues on Candidate Detail — the front-half, materialized, zero install.
2. **C1** (this week, alongside the running v189 loop): file feedback issues while the loop works — day/night shift live.
3. **D1** (any 30 min): the allow-list curation pass — permanent friction reduction.
