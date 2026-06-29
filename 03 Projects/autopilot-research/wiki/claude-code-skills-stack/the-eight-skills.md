# The Eight Skills — Per-Skill Catalog

## Source

Eric Tech, [Va-U1dqhwzk](https://www.youtube.com/watch?v=Va-U1dqhwzk) (timestamps below). Originals fetched + verified (`wf_04da379d-ca9`) + `gh api` ground-checked 2026-06-29. Deep-dive articles linked per skill.

---

## 1 — Superpowers (1:11)

- **Problem it solves:** "vibe coding" — Claude writes code with no plan, no tests, fragile output.
- **What:** a Claude Code plugin imposing a spec-first, TDD methodology with composable sub-skills + a `using-superpowers` router that picks the right sub-skill per task.
- **Pipeline (verified order):** brainstorm → git-worktree → write-plan → subagent-driven execution → TDD (red-green-refactor) → code-review → finish/PR. (Video says "write tests *before* execute"; really TDD runs *during* execution — see [[claude-code-skills-stack/original-superpowers]].)
- **Install:** `/plugin install superpowers@claude-plugins-official` (free, MIT).
- **Public/gated:** fully public — `obra/superpowers`, 240.9K★.
- **Operator fit:** TDD discipline + 2–5-min task granularity ≈ Scrum sprint-slicing; hireui Goal #2 build harness.

## 2 — Skill Creator (5:05)

- **Problem:** Superpowers is *someone else's* workflow; you want your own rules/process.
- **What:** the **first-party Anthropic** skill that scaffolds new skills and improves them with **evals** (Create → Eval → Improve → Benchmark).
- **How:** spawns subagents (a `grader`, a blind A/B `comparator`, an `analyzer`); benchmarks pass-rate / latency / tokens; browser eval-viewer for human review.
- **Demo use:** merge best stage of Superpowers + GSD + G-Stack into a custom `build-feature` skill.
- **Install:** built-in to Claude Code / source at `anthropics/skills` (156.4K★). "Skill Creator 2.0" = the 2026-03-03 update.
- **Operator fit:** formalize fuzzy autopilot skills; the eval loop == the operator's [[prompt-evaluation/_index]] grading discipline. See [[claude-code-skills-stack/original-skill-creator]].

## 3 — UI UX Pro Max (9:25)

- **What:** a design-intelligence skill that generates a full design system (styles, palette, typography, patterns-to-avoid) tailored to your niche.
- **How (corrected):** NOT "trained on hundreds of datasets" — it bundles **curated CSV lookup tables** (67 UI styles / 161 palettes / 57 font pairings / 99 UX guidelines / 25 charts) + **161 reasoning rules** driving a deterministic reasoning engine. No API keys, all local.
- **Install:** `npm i -g uipro-cli && uipro init --ai claude` (requires Python 3.x), or `/plugin add nextlevelbuilder/ui-ux-pro-max-skill`.
- **Public/gated:** public, MIT, 97.6K★. **Install-safe** (no postinstall; deps = commander/chalk/ora/prompts; downloads release assets from GitHub on init w/ bundled fallback). `nextlevelbuilder` org ownership is opaque.
- **Operator fit:** alternative to the **Taste Skill** ([[ai-web-design-workflow/_index]]) for the hireui frontend; see [[claude-code-skills-stack/original-design-skills]].

## 4 — Awesome Design MD (14:20)

- **What:** a repo of **73 curated `DESIGN.md` files** (Claude, Stripe, Figma, Apple, Cursor, Lovable, ClickHouse…). Copy one to your project, tell the agent to use it, get that brand's look.
- **`design.md`:** a markdown+YAML design-spec format **created by Google inside Stitch** (launched May 2025), open-sourced by Google Labs ~April 2026 (`google-labs-code/design.md`, 23K★, Apache-2.0). Validate: `npx @google/design.md lint`.
- **Install:** copy-based (not one npm package) — `voltagent/awesome-design-md`, 94.1K★, MIT.
- **Operator fit:** extract a TalentAxis `DESIGN.md` for hireui; version a brand system as markdown. See [[claude-code-skills-stack/original-design-skills]].

## 5 — Playwright CLI (17:25)

- **What:** gives Claude Code "eyes and hands" for browser QA — runs a multi-phase test pass, captures **screenshots + console logs per step**, generates a QA-report table; then fixes the console-log errors (Superpowers subagents) and pushes.
- **CLI vs MCP (the real point):** **CLI** (`microsoft/playwright-cli`, 11.7K★) writes YAML snapshots/PNGs to disk and the agent reads only what it needs (**~68-token schema overhead**); **MCP** (`microsoft/playwright-mcp`, 34.5K★, 49 tools) streams full browser state into context every step (**~4× the tokens** in benchmarks). CLI wins for long test suites; MCP for short exploratory QA.
- **Public/gated (corrected):** Eric's actual skill is **public** — `EricTechPro/startup-claude-skills` ships `playwright-qa-cli` (MIT). Only his Skool *community/templates* are paid.
- **Operator fit:** hireui eval-first QA automation + the Candidate-Detail Figma-parity check. See [[claude-code-skills-stack/original-playwright-cli-vs-mcp]].

## 6 — Obsidian Knowledge System (22:39)

- **What:** turn a markdown folder into a knowledge system Claude can read/write/tag/link — "a miniature RAG with no DB, embeddings, or infrastructure."
- **Attribution (corrected):** built by **Steph Ango (kepano), the CEO of Obsidian** — TRUE, but it's his **personal** repo `kepano/obsidian-skills` (38.8K★, MIT), **not** an official Obsidian-org project (`obsidianmd/obsidian-skills` = 404).
- **What it actually is:** 5 *format-handling* agent skills (obsidian-markdown / obsidian-bases / json-canvas / obsidian-cli / defuddle) — it is **not itself a RAG**. The "zero-overhead markdown knowledge base" is the **Karpathy LLM-Wiki pattern**, which *composes with* this skill (this vault *is* that pattern).
- **Operator fit:** highest relevance, lowest novelty — install it to let Claude maintain Obsidian vault syntax cleanly. See [[claude-code-skills-stack/original-obsidian-kepano]].

## 7 — "43 Marketing Skills" (25:50)

- **What:** a pack of marketing skills (SEO/copywriting/email/CRO/analytics) Eric credits for BookZero's growth + 100 PageSpeed scores.
- **Attribution (corrected):** these are **Eric Osiu's** `ericosiu/ai-marketing-skills` (2.7K★, MIT, ~15 categories) — *cited/used* by Eric, **not authored** by him. The "0→1000 users from these skills" attribution is **unverifiable** (single-channel claim).
- **Operator fit:** low for now (no active consumer-SaaS marketing motion); a few skills (humanizer, SEO) overlap [[claude-skills/_index]].

## 8 — /fix-ticket Workflow (28:51)

- **What:** Eric's own end-to-end bug-fix skill: read Jira/Sentry ticket → reproduce via Playwright CLI → research subagents → plan (approve) → fix via TDD → verify via Playwright → commit/push/deploy to Vercel → Jira/QA handoff. Reports phases, agent count, token estimate.
- **Public/gated:** **public** — `EricTechPro/startup-claude-skills` (51★, MIT; skills: fix-ticket, develop-team, review-team, review-fix, playwright-qa-cli).
- **Integrations are all official:** Telegram (`anthropics/claude-plugins-official`), Sentry MCP, Atlassian/Jira MCP, Vercel MCP.
- **Hype:** "replaces ~90% of junior SWE jobs" = marketing; realistic = automates a large slice of routine bug-fix toil. See [[claude-code-skills-stack/original-fix-ticket-marketing-telegram]].

---

## Bonus mentions (frameworks Eric merges / references)

- **GSD** (`gsd-build/get-shit-done`, 64.6K★, **archived** → `open-gsd/gsd-core`) — per-agent context isolation (fresh 200K window per executor); 5 phases Discuss/Plan/Execute/Verify/Ship.
- **G-Stack** (`garrytan/gstack`, 117.8K★) — 23 persona "specialist" commands (CEO/design/eng/QA/security/ship); `/qa` opens real Chromium, `/cso` does OWASP+STRIDE.
- **Spec Kit, BMAD** — named in Eric's SDD-frameworks playlist (not demoed).
- **GPT Image 2.0, Nano Banana** — image gen for design/marketing assets.

## Key Takeaways

- 6 of 8 are *real, free, public* skills; 2 (UI UX Pro Max, Awesome Design MD) have stronger operator-side alternatives already in the vault.
- The two biggest framing corrections: the Obsidian skill is **personal-not-official + not-a-RAG**, and UI UX Pro Max is a **CSV reasoning engine, not ML-trained**.
- The marketing pack is misattributed (Eric Osiu, not Eric Tech).

## Related

[[claude-code-skills-stack/overview]] · [[claude-code-skills-stack/video-to-original-crosswalk]] · [[claude-code-skills-stack/source-provenance]]
