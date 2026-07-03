# pocock-real-feature-build

> **Topic index.** Matt Pocock's **end-to-end worked example** of shipping a real feature with Claude Code — the hands-on companion to the philosophy-level [[../pocock-agentic-workflow/_index|pocock-agentic-workflow]] topic. One 44-minute unscripted session covering the full pipeline: **grill-me → ubiquitous-language glossary → write-a-PRD (modules first) → PRD-to-issues (right-sizing) → Sandcastle/Ralph AFK loop in Docker → QA plan → in-app feedback button → Ralph fixes bugs while the human QAs in parallel**.
>
> **Entry point:** [hX7yG1KVYhI](https://www.youtube.com/watch?v=hX7yG1KVYhI) — **"Building a REAL feature with Claude Code: every step explained"**, Matt Pocock's **own channel** (FIRST-PARTY, unlike the third-party Ondrej podcast), uploaded **2026-03-18**, 44:16, 162,785 views. Full ~50K-char transcript read.
>
> **Why this video matters in the corpus:** it is the **public origin moment of Sandcastle** — the `mattpocock/sandcastle` repo was created **2026-03-17, ~16.5 hours before the video published**; in the video Matt calls it "provisional name Sandcastle… been cooking my setup over the last 24 hours". The npm package `@ai-hero/sandcastle` v0.0.1 followed 9 days later (2026-03-26). The June podcast (already compiled) discusses the *mature* package; this video shows it being born.
>
> **Originals (double deep-dived against primary sources):** **[mattpocock/course-video-manager](https://github.com/mattpocock/course-video-manager)** (the real work repo — public, 506★, harness in-source at `.sandcastle/`) · **[mattpocock/skills](https://github.com/mattpocock/skills)** (154.5K★, 37 skills / 6 categories — grill-me / to-prd / to-issues verified verbatim) · **[@ai-hero/sandcastle](https://www.npmjs.com/package/@ai-hero/sandcastle)** timeline · **aihero.dev** five-daily-skills article + cohort · **Eric Evans — *Domain-Driven Design* (2003)** ubiquitous language · Claude Code official features (**Explore subagent**, **/btw side-question**, AskUserQuestion, devcontainers).
>
> **Verification:** Workflow `wf_8897fa8d-c95` (15 agents: 7 deep-dive gatherers + 7 adversarial REFUTE-first verifiers + completeness critic; ~880K tokens, 400 tool calls) + operator `gh api` ground-checks. **One verifier misfired** (declared the `/ubiquitous-language` skill "non-existent" and the skills repo "impossible before June 2026" — refuted by operator ground-truth: the skill exists at `skills/deprecated/ubiquitous-language/` and the repo was created 2026-02-03). Full ledger in [[source-provenance]].

---

## Articles

- [[overview]] — the whole session in one screen: the feature (ghost courses + direct create/delete), the 8 workflow phases, the time economics (22 min of grilling = "the hard bit"), and what Matt reviews vs ignores.
- [[grill-me-in-practice]] — anatomy of a live grilling session: dictate the rough idea, **always explain the why**, code-first answering, trade-off modeling, the "look harder" correction, and why grill-me deliberately avoids the AskUserQuestion tool.
- [[ubiquitous-language-for-llms]] — the DDD move: human = domain expert, LLM = dev, `CONTEXT.md` glossary as the bridge (ghost lesson / **materialize** / materialization cascade / "aliases to avoid"); Evans-2003 lineage; the skill lineage (`/ubiquitous-language` → deprecated → `domain-modeling` with lazy ADRs); prior-art convergence.
- [[prd-and-issues-pipeline]] — write-a-PRD sketches **modules before prose**, asks *which modules get tests*, files the PRD as a GitHub issue; to-issues slices it with blocking relationships; the human's only edit = merging two too-small slices; "am I going to review this PRD? No."
- [[sandcastle-ralph-afk-loop]] — the harness at birth (video: Dockerfile + patch-out-commits + `pnpm ralph`) vs the verified current source (`.sandcastle/main.ts`: 4-phase Plan→Implement→Review→Merge, MAX_ITERATIONS=10, 4 issues in parallel, dependency-based selection, tests+typecheck before every commit, two-phase issue closure).
- [[qa-plan-and-feedback-loop]] — "take the last five commits and create a QA plan" as a GitHub issue; AFK vs human-in-the-loop labels; the in-app feedback button (verified: `api.feedback.ts`, **Haiku**-generated issue titles); day-shift/night-shift; why Matt says specs-to-code "is never going to work".
- [[course-video-manager-as-artifact]] — the repo itself as verified evidence: stack (React Router / TS / Drizzle / Postgres+PGLite / Vitest / **Effect**), 89-entry permissions allow-list, in-repo skills (`DB-TDD`, `to-prd-project`), Ralph co-authored commit trail, `CONTEXT.md` glossary.
- [[the-originals]] — provenance of every artifact: the two repos, the npm package, the five-daily-skills article (/grill-me /to-prd /to-issues /tdd /improve-codebase-architecture), Evans DDD, and the Claude Code features with ship-version evidence.
- [[caveats-and-corrections]] — the don't-re-fabricate list (89 not 170+; 10 not 100; skill deprecated not deleted; 154.5K★; cohort ends Apr 8; /btw ≤v2.1.79; Ralph=technique vs Sandcastle=package) + what remains unverified (Jaman attribution, dictation tool).
- [[source-provenance]] — capture method, workflow stats, the verifier-misfire override, and video-vs-current-repo drift notes.

## Pilot methods (how to apply this to your flow)

A ranked menu of **26 methods + a skip-list + a critic's reframe** lives in **`output/(C) 2026-07-03-pocock-real-feature-build-pilot-methods.md`** — across five angles: hireui Goal #2 (grill→PRD→issues→AFK on the Candidate Detail refactor), the ubiquitous-language/CONTEXT.md pattern for hireui + vaults, QA-plan + feedback-button loops, personal Claude Code (/btw, Explore, skill hygiene), and Scrum coaching (day-shift/night-shift, DDD glossary as backlog language).

## Cross-topic links

- [[../pocock-agentic-workflow/_index]] — the **sister topic**: same author, philosophy layer (harness>model, queues-not-loops, procedures-vs-abilities). This topic is the *practice* layer; that one is the *theory*. Its [[../pocock-agentic-workflow/sandcastle-deep-dive|sandcastle-deep-dive]] covers the package this video births.
- [[../workflow-ai-coding/_index]] — already features Pocock + Ralph + grill-me at survey level.
- [[../harness-engineering/_index]] — org-scale sibling; the 89-entry allow-list + in-repo skills are textbook individual-scale harness engineering.
- [[../how-we-claude-code/_index]] — Anthropic's interview-first pillar ≈ grill-me; agent-native verification ≈ the QA-plan step.
- [[../multi-agent-orchestration/_index]] — the 4-phase Plan→Implement→Review→Merge loop is an orchestrator-worker pattern.
- [[../claude-code-memory-systems/_index]] — `CONTEXT.md` glossary = a curated memory file; Karpathy LLM-Wiki lineage.
- [[../claude-skills/_index]] · [[../claude-code-skills-stack/_index]] — skills landscape; grill-me/to-prd appear across both.
- [[../claude-md-12-rules/_index]] — Rule 1 (think before coding) ≈ grilling; Rule 9 (tests verify intent) ≈ TDD-in-issues; Rule 12 (fail loud) ≈ per-commit tests+types.
- [[../prompt-evaluation/_index]] — the QA-plan-as-checklist is a lightweight eval harness over shipped commits.
- [[../ai-engineering/_index]] — the feedback-button → issue → fix loop is Huyen's user-feedback flywheel in miniature.

## Key Takeaways

- **The human's job is the front of the pipeline.** 22 of 44 minutes were spent grilling requirements; after that "it's pretty much all on rails" — PRD, issues, implementation, even the PRD review are delegated ("LLMs are really good at summarizing; I'm not going to review it").
- **A shared glossary is cheap leverage.** The DDD ubiquitous-language file (`CONTEXT.md`) lets Matt say "there's a bug in the materialization cascade" and be understood exactly — and agents grep into it when exploring. Verified in-repo with "aliases to avoid" columns.
- **Right-size the queue items.** Issues too small waste agent-startup cost; too big lose coherence. The human's judgment call in the whole pipeline was merging two slices — that's the skill that remains.
- **Verification is per-commit, not per-run.** The harness requires tests+typecheck before *every* commit, and Matt reviews *inputs and outputs* (interfaces, module shapes, QA behavior) — "notice how little I looked at the code."
- **QA parallelizes with fixing.** The feedback button turns every QA observation into a Ralph-consumable GitHub issue while the human keeps testing — the sharpest live demo of "day shift / night shift" in the corpus.
- **Edge cases emerge in QA, not in specs.** The not-a-git-repo showstopper was found by hand-testing, not planning — Matt's argument for iterating-with-QA over big-upfront-specs (his stance; the SDD topics in this vault disagree).
