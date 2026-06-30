---
title: "(C) agent-skills — Pilot Methods Menu (24 ways to apply it)"
subject: addyosmani/agent-skills
date: 2026-06-30
companion: "(C) agent-skills — Beginner Analysis.md"
---

# Applying `agent-skills` to your workflow — 24 methods

**Why this is a strong pilot target:** it's a free, MIT, **Claude-Code-first plugin** you can install today; it's *process* (no API spend, no remote tunnel, no compiled binary); and it lands directly on five of your live pilot threads + the hireui Goal-#2 deployment target. **Lowest-risk substantial pilot in the recent run.** Risk surface = it adds **slash commands, skills, and session hooks** to a Claude Code config → snapshot first, and on hireui follow the CONSTITUTION (operator installs per **I-8**, work on an **agent-`*` branch** per **I-2**, run **hireui-rooted**).

> **Read me first — the one fence that matters:** before `/plugin install`, run **`install-snapshot`** (it diffs `~/.claude` so you have a clean uninstall checklist) and skim the **`hooks/`** scripts (SessionStart + sdd-cache + simplify-ignore run shell). Don't run agent-skills as your *active router* at the same time as another skill framework (Superpowers/Pocock) — they fight over `/tdd` etc. Pick one primary; borrow the rest à la carte.

---

## START HERE — the 4-rung ladder (do these in order)

1. **M1 (prove the loop, ~10 min):** install into a **scratch repo**, run `/spec` on a tiny throwaway feature, watch the anti-rationalization + verification gates fire. Zero risk.
2. **M9 (Goal-#2 evidence):** take **one real hireui ticket** through `/spec → /plan → /build → /review` on an `agent-*` branch — your first "AI-assisted engineering with discipline" deployment artifact.
3. **M14 (the obvious win):** run `frontend-ui-engineering` + `/review` on the **CandidateDetailScreen** drift — the skill's "AI aesthetic" anti-pattern *is* your "demo template" smell.
4. **M19 (vault payoff):** **borrow-by-hand** the anti-rationalization-table + verification-gate format into your own `05 Skills/` routine. This is the compounding win — it upgrades how *every* future vault skill is written.

---

## Group A — First loop & install (low risk, prove it works)

**M1 · Scratch-repo smoke test.** `/plugin marketplace add addyosmani/agent-skills` → install into a throwaway project (NOT the vault, NOT hireui). Run `/spec` on a trivial feature; confirm the six-area spec + boundaries appear and it asks for approval before coding. *Payoff:* see the loop. *Fence:* `install-snapshot` first. *Effort:* 10 min.

**M2 · Read-only skill audit (no install).** The skills are plain Markdown — just `git clone` and **read** the 3 you care about (`spec-driven-development`, `code-review-and-quality`, `frontend-ui-engineering`) to harvest the heuristics without changing any config. *Payoff:* knowledge, zero footprint. *Effort:* 15 min.

**M3 · Cherry-pick ONE skill via Cursor/Markdown.** Copy a single `SKILL.md` into a project's `.cursor/rules/` (or paste into a Claude Code session) instead of installing the whole router. Good for testing `doubt-driven-development` in isolation. *Payoff:* à-la-carte adoption, no router conflict. *Effort:* 5 min.

**M4 · The `using-agent-skills` decision tree as a checklist.** Even without installing, keep the meta-router's six operating behaviors (Surface Assumptions / Manage Confusion / Push Back / Enforce Simplicity / Scope Discipline / Verify-Don't-Assume) as a literal pre-flight you ask Claude to honor in any session. *Payoff:* the bedrock discipline, free. *Effort:* trivial.

---

## Group B — Drive a real feature through the lifecycle (Goal #2 evidence)

**M5 · `/spec` → kill ambiguity on your next real ask.** Use `spec-driven-development` to turn a vague hireui ticket into the six-area spec (Objective / Commands / Structure / Code Style / Testing / **Boundaries**). *Payoff:* the "15-min spec prevents hours" effect; a written contract. *Pairs with:* cc-sdd (your existing method #1).

**M6 · `interview-me` before you even spec.** When a request is underspecified, run the one-question-at-a-time, guess-attached interrogation to ~95% confidence. *Payoff:* this is the same discipline as Matt Pocock's `/grill-me` (v57) and your own brain-setup interview — now enforced. *Note:* great for scoping the next CandidateDetail sub-task.

**M7 · `/plan` with vertical slicing + task sizing.** Feed the spec to `planning-and-task-breakdown`; enforce XS–XL sizing, no task >5 files, checkpoints every 2–3 tasks, high-risk-first. *Payoff:* avoids the "all done but not working" state; gives BMAD/`.pilot-log`-style atomic units.

**M8 · `/build` incrementally (or `/build auto`).** `incremental-implementation` enforces the ~100-line cap + test-each-slice + feature-flag-incomplete-work. Try `/build auto` on a *small* approved plan to feel the autonomous-but-verified pass. *Fence:* scratch first; on hireui keep it human-checkpointed.

**M9 · ⭐ Full lifecycle on ONE hireui ticket (the headline Goal-#2 play).** `/spec → /plan → /build → /test → /review` on an `agent-*` branch, hireui-rooted, operator-installed. Capture the run in `.pilot-log`. *Payoff:* concrete "AI-assisted engineering with senior discipline, deployed to real software" evidence for Goal #2 — the thing the vault has been missing (zero pilots completed since v153). *Fence:* I-2 branch, I-8 install, GitNexus-first.

**M10 · `/ship` parallel-persona go/no-go before a merge.** Fan out `code-reviewer` + `security-auditor` + `test-engineer` in parallel → one go/no-go verdict. *Payoff:* a structured pre-merge gate; also a live demo of the multi-agent fan-out you're piloting ([[project_multi_agent_orchestration_pilot_thread]]).

---

## Group C — hireui-specific high-value plays

**M11 · ⭐ `frontend-ui-engineering` on CandidateDetailScreen.** The skill's **8-point "AI aesthetic" anti-pattern** (purple/gradients/rounded-everything/oversized-padding/stock-grids) is *exactly* the "demo template" smell you diagnosed — plus its design-token + spacing-scale discipline targets the drifted navy/accent/Inter→Roboto tokens. Run it against the Figma SoT handoff. *Pairs with:* the Taste-Skill redesign gate ([[project_ai_web_design_pilot_thread]]) + serve-sim v183 (to *see* the running iOS UI). *Fence:* keep operator-locked deviations (3 tabs, 72px avatar, verified timeline colors).

**M12 · `code-review-and-quality` five-axis pass on the refactor PR.** Severity-labelled (Critical/Required/Nit), ~100-line sizing, the "count the concepts the reader holds" complexity heuristic. *Payoff:* a disciplined review of the CandidateDetail rework before it lands.

**M13 · `security-and-hardening` + OWASP-LLM section — pre-stage hireui's LLM.** hireui has **no LLM integration yet** ([[project_hireui_no_llm_yet]]); the skill's **OWASP LLM Top 10** section ("system prompt is NOT a security boundary; treat model output as untrusted") is a build-it-right spec for when you add one. *Pairs with:* your `claude-api-cost-optimization-spec`.

**M14 · `performance-optimization` + `/webperf` on the hireui web frontend.** Measure-first (Lighthouse + web-vitals), Core Web Vitals targets, the perf-budget defaults. *Payoff:* concrete CWV numbers; the `web-performance-auditor` persona's **Metric-Honesty Rule** prevents fabricated metrics. *Note:* Addy literally co-created Core Web Vitals — this is his home turf.

**M15 · `observability-and-instrumentation` as the hireui telemetry spec.** Define the 2–4 on-call questions first; RED metrics per endpoint; symptom-based alerts; correlation IDs. *Pairs directly with* [[project_cc_observability_pilot_thread]] (ccusage → OTel stack) — this skill is the *application* layer to that *measurement* layer.

---

## Group D — Compose with your existing pilot threads

**M16 · `source-driven-development` for any framework-touching hireui/Expo work.** DETECT→FETCH→CITE forces Claude to ground React-Native/Expo decisions in official docs (deep links + anchors) and flag UNVERIFIED. *Payoff:* kills the stale-training-data bug class; pairs with the GitNexus-first constitution.

**M17 · `doubt-driven-development` as your adversarial-verify default.** This is the productized version of your own [[feedback_wiki_verify_independently_check_collisions]] discipline: ARTIFACT+CONTRACT to a fresh-context reviewer, never the CLAIM; adversarial prompt; 3-cycle bound. *Payoff:* a reusable harness for the "verify independently" rule you already enforce by hand — and it offers cross-model (Gemini/Codex) escalation.

**M18 · `context-engineering` to tune your own CLAUDE.md discipline.** The skill's context-hierarchy (rules > specs > source > errors > history) + the **<2,000-line focus / >5,000-line flooding** thresholds are a direct lens on the vault's own shim-size lessons (the 584KB→29KB refactor). *Payoff:* validates + sharpens your CC-memory-systems thread ([[project_cc_memory_systems_pilot_thread]]).

---

## Group E — Vault-meta: upgrade how YOU build skills (the compounding win)

**M19 · ⭐ Borrow-by-hand the SKILL.md format into `05 Skills/`.** Adopt three of Addy's mechanics into the vault's own routine/skill files: **(a)** a "Common Rationalizations" excuse→rebuttal table, **(b)** explicit "Verification" evidence-gates, **(c)** progressive disclosure (keep `SKILL.md` < 500 lines, push detail to supporting files). *Payoff:* every future vault skill gets harder to rationalize around — this upgrades the *factory*, not one product. *(Same "borrow-by-hand" move you used for §37/§38 from obsidian-second-brain.)*

**M20 · Run `SkillOpt` (v178) on one of Addy's skills — or one of yours.** Use the corpus's text-space skill optimizer to validation-gate-optimize, say, `spec-driven-development` against a held-out set, with Claude Code as harness. *Payoff:* turns "borrow the format" into "measure whether the edits actually help." *Fence:* SkillOpt's own install fence (scratch skill + small validation set).

**M21 · Scan the pack with `SkillSpector` (v169) before trusting the hooks.** Point the v169 defensive scanner (`--no-llm` = free static pass) at the cloned `agent-skills` (it ships shell hooks). *Payoff:* a supply-chain check on the very plugin you're about to install — closes the loop between two corpus subjects.

**M22 · Codify the `using-agent-skills` router idea into the autopilot routine.** Addy's meta-router (map work → skill, enforce 6 behaviors) is a clean template for a vault "which-skill-applies" dispatcher in your autopilot-research flow. *Payoff:* methodology import into Goal #1's own machinery.

---

## Group F — Evaluation & comparison plays

**M23 · Honest head-to-head on a real ticket: agent-skills vs cc-sdd (vs Superpowers/Pocock).** Same hireui ticket, swap only the framework (Addy's own `comparison.md` + the Om Mishra experiment are the template). Measure: time-to-code, validation passes, regressions caught. *Payoff:* picks your primary router with evidence, not vibes — and is itself Goal-#2 evidence. *Caution:* one ticket = illustration, not benchmark (Addy says so too).

**M24 · Mine the upstream canon as a study list.** Use §4 of the Beginner Analysis as a reading path: *Software Engineering at Google* (Hyrum's Law, Beyoncé Rule), Kent Beck TDD, Karpathy on context engineering, Osmani's "70% problem" / "Beyond the 70%" / "Loop Engineering" essays. *Payoff:* the durable principles behind the skills, for the Scrum-coach side of your role.

---

## Fence & risk table

| Risk | Mitigation |
|---|---|
| Plugin writes skills/commands/**hooks** into `~/.claude` | `install-snapshot` before install; read `hooks/*.sh` first; keep the uninstall diff |
| Router conflict with another framework | Run only ONE active router; cherry-pick the rest (Markdown, à la carte) |
| hireui CONSTITUTION | Operator installs per **I-8**; work on **agent-`*`** branch per **I-2**; run **hireui-rooted**; GitNexus-first |
| `/build auto` autonomy | Scratch repo first; keep human checkpoint per phase on real code |
| Trusting adoption claims | Star counts page-stated, NOT API-verified — ignore for decisions |
| Over-adopting at once | Start with ONE skill on ONE ticket (M9); expand only after the loop proves out |

**Recommended sequence: M1 → M9 → M11 → M19.** Prove the loop in a scratch repo, get one real hireui-ticket lifecycle as Goal-#2 evidence, win the obvious CandidateDetail play, then bank the compounding vault-meta upgrade.
