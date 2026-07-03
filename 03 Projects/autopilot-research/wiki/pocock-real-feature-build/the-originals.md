# The originals — provenance of every artifact in the video

## Source

- Deep-dive Workflow `wf_8897fa8d-c95` dossiers + operator `gh api` ground-checks (2026-07-03). See [[source-provenance]] for the verification ledger.

## 1. mattpocock/course-video-manager (the work repo)

- Public, real, created 2025-07-24; 506★; the demo's stage and the harness's home. Full treatment: [[course-video-manager-as-artifact]].

## 2. mattpocock/skills (the skills repo)

- [github.com/mattpocock/skills](https://github.com/mattpocock/skills) — MIT, **created 2026-02-03**, **154,511★** (2026-07-03), **37 skills across 6 categories** (productivity / engineering / deprecated / …).
- **grill-me** (`skills/productivity/grill-me/SKILL.md`) — two-tier: user-invoked dispatcher with **`disable-model-invocation: true`** delegating to a model-invocable grilling sub-skill. Verbatim-confirmed rule: *"If a question can be answered by exploring the codebase, explore the codebase instead."*
- **to-prd** + **to-issues** — confirmed; module sketching, testing-decisions question, PRD-as-GitHub-issue, slice-with-blockers all match the video behavior. (Video's spoken "write a PRD" / "PRD to issues" = these skills.)
- **ubiquitous-language** — exists at `skills/deprecated/ubiquitous-language/` (writes `UBIQUITOUS_LANGUAGE.md`; term/definition/aliases-to-avoid tables); **deprecated in favor of `skills/engineering/domain-modeling/`** (CONTEXT.md + CONTEXT-MAP.md + lazy ADRs, "challenge against the glossary"). See [[ubiquitous-language-for-llms]].
- Also spotted: `teach/GLOSSARY-FORMAT.md`, `writing-great-skills/GLOSSARY.md` — the glossary idea recurs across his skill designs.

## 3. Sandcastle (@ai-hero/sandcastle)

- Repo [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) created **2026-03-17** (~16.5h pre-video); npm **v0.0.1 on 2026-03-26**; this video = the public origin moment. Mature-package analysis lives in [[../pocock-agentic-workflow/sandcastle-deep-dive]]. Timeline table in [[sandcastle-ralph-afk-loop]].

## 4. aihero.dev (articles + cohort)

- **The five-daily-skills article** (the "top five skills" Matt references) — the five, verified: **/grill-me** (stress-test plans with relentless questions) · **/to-prd** (synthesize context into requirements) · **/to-issues** (break PRD into vertical-slice GitHub issues) · **/tdd** (red-green-refactor loops) · **/improve-codebase-architecture** (deep modules, simple interfaces).
- **"Claude Code for Real Engineers" cohort** — $795, ran **2026-03-30 → 2026-04-08** (two weeks; not Apr 13). The video's 40%-off promo was for this cohort.
- ⚠️ The description's shortlinks (`aihero.dev/s/FpvIa6`, `/s/BQGSo5`) **now 404** — link rot; the articles are findable on aihero.dev directly.

## 5. Eric Evans — Domain-Driven Design (2003)

- *Domain-Driven Design: Tackling Complexity in the Heart of Software* — origin of **ubiquitous language** (model-based shared vocabulary, devs ↔ domain experts). Matt's on-screen book is this one ("I've been reading a book called domain-driven design"). His application (human=domain-expert, LLM=dev) is his extension, converging with independent 2026 prior art (Schleicher Jan-2026; Dev|Journal May-2026). See [[ubiquitous-language-for-llms]].

## 6. Claude Code features used on camera

- **Explore subagent** — official read-only search agent (docs: code.claude.com sub-agents); isolates exploration in its own context, returns a summary; since v2.1.198 inherits the main conversation's model (capped at Opus on the Claude API).
- **`/btw` side-question** — real feature: quick question that does NOT enter chat history; shipped **by v2.1.79 or earlier** (v2.1.187 only added arrow-navigation improvements); documented only in passing (no standalone docs page).
- **AskUserQuestion** — exists as a core tool but **publicly undocumented** (tracked in claude-code issues #10346 / #20275). Matt's avoidance rationale: UI preference (strong) + token-overhead of tool-call JSON (weaker today — Claude 4.x has built-in token-efficient tool use; treat as his March-2026 opinion).
- **Devcontainers/Docker** — official docs exist for containerized Claude Code (egress-firewalled devcontainer reference), consistent with the Sandcastle architecture.

## 7. Unverified attributions (reported-only)

- **"Day shift / night shift"** — attributed to "my friend Jaman on Twitter"; not independently located. Keep as reported.
- **Willow Reagan** — Matt's former boss/lead-dev mentor, cited as the archetype of ask-smart-questions leadership; personal anecdote, nothing to verify.
- **Dictation tool** — not named in this video (his known tool from the podcast corpus is Wispr Flow); do not assert.

## Key Takeaways

- Every load-bearing artifact in the video is **real, public, and inspectable** — repo, skills, package, article, cohort — an unusually verifiable creator claim-set.
- The skills repo is the **reusable layer** (37 generic skills); course-video-manager holds the **project-tuned layer** (DB-TDD, to-prd-project) — a two-tier skill architecture worth copying.
- The deprecation trail (ubiquitous-language → domain-modeling) shows the glossary pattern *maturing into* decision-records territory — glossaries and ADRs are one discipline.
