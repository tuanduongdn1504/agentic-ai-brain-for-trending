# (C) Pilot methods — applying Google Antigravity Skills/Rules to your flow

> **Source:** wiki topic [[google-antigravity-skills/_index]] — Dũng's tutorial (`UFmV7YsVqlM`) + adversarially-verified deep-dive of Google Antigravity (`wf_1e5cf2f6-5ec`, 16 agents; + operator WebFetch/WebSearch ground-checks).
> **Operator context:** software dev + Scrum coach; **Claude Code** is your primary harness; two L5 markdown vaults (Storm Bear + autopilot-research) already built on `CLAUDE.md` rules + project-local `SKILL.md`-style skills. Deployment target **hireui** (`/Users/Cvtot/monorepo/hireui` — TalentAxis recruitment SaaS, React/TS web+mobile; **no LLM in product yet**; strict CONSTITUTION with **I-2 agent-\* branch** + **I-8 operator-only installs** + **GitNexus-first**; BMAD harness + `.pilot-log`; **Candidate Detail** mobile refactor in flight with **drifted design tokens** navy `#1E2960`→`#002D79`, accent `#E8743C`→`#DC6803`, Inter→Roboto).
> **Goal #2 = *actually deploy* useful methods into a real working flow.** Ranked by that leverage.

---

## The headline (if you do ONE thing)

**Adopt `AGENTS.md` as the portable, cross-tool superset of your `CLAUDE.md` — and internalize that your existing `SKILL.md` skills are *already* Google Antigravity skills.** Then prove it by **harvesting one real workflow (the hireui Candidate-Detail refactor) into a portable `SKILL.md`, guarded by an `AGENTS.md` rule** ("tokens come only from `DESIGN.md`; never invent a 4th navy; I-2 branch; GitNexus-first"). This is the cheapest, most reversible, highest-Goal-#2 move: it makes your whole harness **tool-agnostic** (Claude Code today, Antigravity/Cursor/Kiro for free tomorrow), it directly attacks the token-drift root cause, and it composes with your **cc-sdd #1**, **how-we-claude-code verify**, and **open-design `DESIGN.md`** pilots. **You do not need to install Antigravity to capture 80% of the value** — the standards are the prize. Everything below is depth on top of that.

---

## Ranking at a glance

| # | Method | Angle | Effort | Goal #2 | Install Antigravity? |
|---|---|---|---|---|---|
| **A1** | Adopt `AGENTS.md` as your portable rules layer (vault + hireui) | Portability | S | ★★★ | No |
| **A2** | Recognize + inventory your skills as portable `SKILL.md` (audit `description`s) | Portability | S | ★★★ | No |
| **A3** | Harvest the Candidate-Detail refactor into a `SKILL.md` + `AGENTS.md` guard rule | hireui | M | ★★★ | No |
| **A4** | Split every skill's `description` for progressive-disclosure quality | Portability | S | ★★★ | No |
| **B1** | Free multi-model *second-opinion* surface: run the same skills in Antigravity | hireui/personal | M | ★★ | Yes (sandbox) |
| **B2** | Antigravity-vs-Claude-Code bake-off on one hireui ticket, measured | hireui | M | ★★ | Yes (sandbox) |
| **B3** | "Report-automation" skill for hireui recruiter metrics (the video's use case) | hireui | M | ★★ | No |
| **C1** | Skill-vs-Rule lint of the Storm Bear `CLAUDE.md` (constraints → rules) | vault | S | ★★ | No |
| **C2** | Refactor hireui CONSTITUTION into `AGENTS.md` rules + task skills | hireui | M | ★★★ | No |
| **C3** | "Never overwrite raw data" → an `AGENTS.md` data-safety rule for hireui/vault | hireui/vault | S | ★★ | No |
| **D1** | Teach "teach once / clone yourself" as your agent-adoption coaching frame | Scrum | S | ★★ | No |
| **D2** | Run the Excel-report demo *live* as a non-coder onboarding exercise | Scrum | S | ★ | Optional |
| **D3** | Sprint-report / velocity skill your team can reuse each sprint | Scrum | M | ★ | No |
| **D4** | Skill-vs-Rule as a metaphor for team "Definition of Done" vs "how-to" | Scrum | S | ★ | No |
| **E1** | Make the autopilot project-local skills tool-agnostic (`SKILL.md` + `AGENTS.md`) | vault | M | ★★ | No |
| **E2** | Convert `(C) autopilot-research-routine.md` into a proper `SKILL.md` skill | vault | M | ★★ | No |
| **E3** | The "harvest a session into a skill" habit for your own Claude Code work | personal | S | ★★ | No |
| **E4** | A `~/.gemini/AGENTS.md` (or `~/.claude`) global rules file = your personal defaults | personal | S | ★★ | No |
| **F1** | One-way skill portability test: copy a vault skill → `.agents/skills/` → verify | Portability | S | ★ | Yes (sandbox) |
| **F2** | Use Antigravity's Stitch design-to-code MCP as a `DESIGN.md` render check | hireui | M | ★ | Yes (sandbox) |
| **F3** | Track `AGENTS.md`/`SKILL.md` standards as a Pattern-Library observation | vault | S | ★ | No |
| **F4** | ADR: "our harness targets open standards, not one IDE" (anti-lock-in) | hireui/vault | S | ★★ | No |

**M0 (prerequisite before you install/run Antigravity for anything):** it's a **free public preview** with real mid-2026 caveats (token overhead, weekly-quota lockouts, reported 403 bans, no SLA — see [[google-antigravity-skills/caveats-and-limitations]]). So: sandbox only, a throwaway Google account, **no hireui production / candidate-PII data**, meter the quota, cap agent loops. Inside hireui, **you** install (I-8); the agent proposes. Most methods below need **no install at all**.

---

## Angle A — Standards portability (the cheapest, highest-leverage angle)

### A1 — Adopt `AGENTS.md` as your portable rules layer ★★★ · S · *no install*
**What:** Create an `AGENTS.md` at the root of the autopilot-research project (and later hireui) holding the tool-agnostic rules currently living only in `CLAUDE.md`. Keep Claude-Code-specific bits in `CLAUDE.md`; let `AGENTS.md` carry the universal ones.
**Why:** `AGENTS.md` is a **Linux-Foundation cross-tool standard** read by Claude Code, Antigravity, Cursor, and Kiro (see [[google-antigravity-skills/rules-and-customization]]). One file, every tool. This is the single most durable, lock-in-proof move — and it's pure Goal #2 (a real standard deployed into your working flow).
**Output:** `AGENTS.md` in the repo; a one-line `CLAUDE.md` note that universal rules live in `AGENTS.md`.
**Caveat:** don't blindly duplicate — put shared rules in `AGENTS.md`, tool-specific in native files, and note precedence (`GEMINI.md` > `AGENTS.md` in Antigravity; Claude Code reads both).

### A2 — Inventory your skills as portable `SKILL.md` ★★★ · S · *no install*
**What:** Recognize that your project-local skills (`(C) yt-pipeline.md`, `(C) autopilot-research-routine.md`, `(C) notebooklm.md`, `(C) yt-search.md`) are the *same primitive* Antigravity uses. Audit them against the real `SKILL.md` spec (`agentskills.io/specification`): YAML frontmatter with a **`description` that says what-it-does + when-to-use**, optional `scripts/`.
**Why:** They're already 90% there. Framing them as `SKILL.md` makes them portable and forces the discipline that makes auto-discovery work.
**Output:** a short audit note in `output/` listing each skill + whether its `description` is discovery-grade.

### A3 — Harvest the Candidate-Detail refactor into a `SKILL.md` + `AGENTS.md` guard ★★★ · M · *no install*
**What:** Turn the in-flight hireui Candidate-Detail refactor into a reusable **skill** (`hireui-screen-refactor`: read `DESIGN.md` → apply tokens → keep 3 tabs / 72px avatar / verified timeline colors → parity checklist) and a **rule** (`AGENTS.md`: "design tokens come *only* from `DESIGN.md`; never introduce a new hex; agent-\* branch per I-2; GitNexus-first per the CONSTITUTION").
**Why:** This is the video's exact lesson (capability in a skill, constraint in a rule) applied to your real, in-flight work — and it hardwires the anti-token-drift discipline from your [[../open-design/_index]] `DESIGN.md` pilot. Reusable for the *next* screen refactor.
**Output:** `.claude/skills/hireui-screen-refactor/SKILL.md` + rules in `AGENTS.md`, exercised on Candidate Detail. Composes with **cc-sdd #1** (spec discipline) and **how-we-claude-code** (agent-native verify on the same screen).

### A4 — Split every skill's `description` for progressive-disclosure quality ★★★ · S · *no install*
**What:** For each skill, rewrite the `description` to be a crisp semantic trigger ("*Analyze a monthly recruiter-pipeline export and produce a formatted sprint report; use when asked to summarize hiring metrics*"), not a vague label ("reporting tools").
**Why:** Both Antigravity and Claude Code route by the `description` (progressive disclosure). A vague description = a skill that never fires (or fires wrongly). This measurably improves your *current* Claude Code skill hit-rate, independent of Antigravity.
**Output:** updated `description` fields; note the before/after in the A2 audit.

---

## Angle B — hireui Goal #2 (the deployment target)

### B1 — Free multi-model second-opinion surface ★★ · M · *sandbox install*
**What:** Install Antigravity in a **sandbox** (throwaway account, no prod data), point it at a **staging mirror / scratch copy** of hireui, and run your ported skills there — with a *Claude* model selected (Antigravity is multi-model). Use it as a **second opinion** on refactors, not a primary tool.
**Why:** It's free and multi-model; you get a parallel agent surface for the cost of a directory rename (`.claude/skills/` → `.agents/skills/`). Good for "does another harness+model agree with this change?" checks.
**Caveat:** M0 applies hard — preview instability + reported bans; keep it off the critical path.

### B2 — Antigravity-vs-Claude-Code bake-off on one ticket ★★ · M · *sandbox install*
**What:** Take one well-scoped hireui ticket (e.g. a Candidate-Detail sub-task). Run it in Claude Code and in Antigravity from the **same `SKILL.md` + `AGENTS.md`**. Measure: output quality, tokens, wall-clock, # of corrections, whether the skill/rule fired identically.
**Why:** Turns "portable in theory" into measured evidence, and tells you if Antigravity is worth any ongoing use. Mirrors your prompt-eval bake-off discipline (`evals/`).
**Output:** a short comparison in `.pilot-log` / `output/`.

### B3 — Recruiter-metrics report-automation skill ★★ · M · *no install*
**What:** The video's Excel-report demo maps almost 1:1 onto hireui: a recruiter's pipeline export → a skill that segments candidates by stage, computes time-to-hire / fill-rate / source mix, charts it, and produces a hiring-manager-ready report. Build it as a Claude Code skill now (Antigravity later if you pilot it).
**Why:** It's a real, non-LLM-in-product-safe internal tool (runs on exported data, not in the app), and a concrete Goal-#2 deployment. Also a great Scrum-coaching artifact (D3).
**Output:** `.claude/skills/recruiter-pipeline-report/SKILL.md` (+ a "never mutate the raw export" rule — see C3).

---

## Angle C — The Skill-vs-Rule discipline (governance)

### C1 — Skill-vs-Rule lint of the Storm Bear `CLAUDE.md` ★★ · S · *no install*
**What:** Read your root `CLAUDE.md` through the video's lens: which lines are **rules** (always-on constraints: "prefix `(C)`", "ask before editing", "never fabricate") vs which are **skills** (reusable procedures)? Move constraints into a rules block (portable to `AGENTS.md`); factor procedures into skills.
**Why:** Your `CLAUDE.md` mixes both. The split makes it cleaner, more portable, and easier for the model to honor. Directly strengthens the harness you run every day.

### C2 — Refactor the hireui CONSTITUTION into `AGENTS.md` rules + task skills ★★★ · M · *no install*
**What:** The hireui CONSTITUTION (I-2 agent-\* branch, I-8 operator-only installs, GitNexus-first) is a *rules* document. Express its always-on invariants as `AGENTS.md` rules so **any** agent tool (Claude Code today, Antigravity/Cursor tomorrow) enforces them; keep the "how we do X" parts as skills.
**Why:** Makes the CONSTITUTION tool-portable and machine-enforced rather than prose. High Goal-#2 value: it's your real governance layer, deployed as a standard.
**Caveat:** respect I-8 — you author/commit; the agent proposes.

### C3 — "Never overwrite raw data" → a data-safety `AGENTS.md` rule ★★ · S · *no install*
**What:** Steal the demo's single best rule verbatim. For the vault: "never edit source files in `raw/`; only write to `wiki/`/`output/`." For hireui: "never mutate candidate/PII source data; read-only on production exports." Add the escape hatch ("ask + wait for confirmation before any overwrite").
**Why:** A one-line rule that prevents a class of expensive mistakes — and it's exactly the vault's existing scope-clamp discipline, now expressed as a portable rule.

---

## Angle D — Scrum coaching (your second hat)

### D1 — "Teach once / clone yourself" as your agent-adoption frame ★★ · S · *no install*
**What:** Use the video's metaphor when coaching teams: stop re-prompting; capture the repeated task as a skill; guard it with a team rule. "Clone the senior, don't babysit the junior."
**Why:** It's a vivid, non-technical framing that lands with mixed-skill teams — turns "AI adoption" into a concrete, low-threat habit (harvest a workflow → skill).

### D2 — Run the Excel-report demo live as a non-coder exercise ★ · S · *optional install*
**What:** Reproduce the demo (or B3's recruiter version) in a coaching session: do a task once, then "make a skill from what we did," then one-shot the next month. Great for showing non-coders the payoff.
**Why:** Concrete, ~15-minute "aha"; de-mystifies skills.

### D3 — A reusable sprint-report / velocity skill for the team ★ · M · *no install*
**What:** Build a skill that turns your board export into a sprint review deck / velocity + burndown summary (compose with the guizang/html-ppt deck skills from [[../open-design/_index]] and the Scrum deck methods there).
**Why:** Recurring coaching deliverable, automated once, reused every sprint.

### D4 — Skill-vs-Rule ↔ "how-to" vs "Definition of Done" ★ · S · *no install*
**What:** Teach the Skill/Rule split as an analogy your teams already know: **skills = the how-to / playbook**; **rules = the Definition of Done / team working agreements** the agent must always honor.
**Why:** Maps a new AI concept onto an existing Scrum mental model — faster adoption.

---

## Angle E — Vault & personal Claude Code

### E1 — Make the autopilot project-local skills tool-agnostic ★★ · M · *no install*
**What:** Add proper `SKILL.md` frontmatter (or a portable mirror) to the four `skills/*.md` files and an `AGENTS.md` for the autopilot project's rules (scope clamp, block-handling, coverage discipline). Keep the `(C)`-prefixed Storm Bear docs as-is; add the standards-compatible layer alongside.
**Why:** Future-proofs your own research harness against tool changes; makes the "12-rule" governance portable (ties to [[../claude-md-12-rules/_index]]).

### E2 — Convert the autopilot routine into a real `SKILL.md` ★★ · M · *no install*
**What:** Express `(C) autopilot-research-routine.md`'s 8-phase orchestration as a `SKILL.md` with a discovery-grade `description` ("run an autonomous YouTube→wiki research loop; use when asked to research a topic and build wiki articles"). Scripts go in `scripts/`.
**Why:** It *is* a skill; formalizing it improves auto-discovery and portability, and dogfoods the very pattern this topic is about.

### E3 — Adopt the "harvest a session into a skill" habit ★★ · S · *no install*
**What:** After any non-trivial Claude Code session you'll repeat (a refactor pattern, a review checklist, a data transform), end with "write a `SKILL.md` capturing what we just did" — then verify and keep it.
**Why:** This is the video's Method 2 as a personal habit; it's how your skill library compounds instead of re-deriving. Verify the generated file (no magic — the agent just writes it).

### E4 — A global personal-defaults rules file ★★ · S · *no install*
**What:** Put your cross-project personal preferences (writing voice, commit style, "always surface uncertainty", branch discipline) in a **global** rules file — `~/.claude/CLAUDE.md` today, mirrored to `~/.gemini/AGENTS.md` if you ever run Antigravity globally.
**Why:** The video's "global skill = street lamp" scope, applied to *your* defaults so they follow you into every repo and every tool.

---

## Angle F — Depth / optional

- **F1 — Portability smoke test** ★ · S · *sandbox*: copy one vault skill into `.agents/skills/`, open Antigravity, confirm it's discovered + runs. Proves the "directory-rename portability" claim with your own eyes.
- **F2 — Stitch design-to-code as a `DESIGN.md` render check** ★ · M · *sandbox*: Antigravity ships a Stitch MCP; feed it your hireui `DESIGN.md` and compare the render to your Figma r2 — a cross-tool token-drift check (compose with [[../ai-web-design-workflow/_index]] + [[../how-we-claude-code/_index]]).
- **F3 — Pattern-Library observation** ★ · S: log "`SKILL.md` + `AGENTS.md` as cross-vendor open standards (Anthropic format adopted by Google; LF-stewarded rules)" as a candidate observation-track for the Storm Bear Pattern Library (cross-vendor cooperation, cf. v62 codex-plugin-cc).
- **F4 — Anti-lock-in ADR** ★★ · S: write a one-page ADR — "our agent harness targets open standards (`SKILL.md`/`AGENTS.md`), not a single IDE" — anchoring the portability principle for hireui + the vault.

---

## Skip-list (what NOT to do)

- **Don't switch off Claude Code.** Antigravity is a *free second surface for the harness you already have*, not a replacement. Your depth is in Claude Code.
- **Don't put hireui production or candidate-PII data into the Antigravity preview.** Unclear retention + reported 403 bans + no SLA (see [[google-antigravity-skills/caveats-and-limitations]]). Sandbox + staging only.
- **Don't trust the video's `.antigravity/skills` path.** It's `.agents/skills/` (project) / `~/.gemini/config/skills/` (global).
- **Don't adopt the "6-persona / version-number / 60K-repos" specifics** — they're unverified (see [[google-antigravity-skills/source-provenance]]).
- **Don't over-engineer `AGENTS.md`.** It's plain Markdown with no schema — a page of clear rules beats a baroque config.
- **Don't wait for an install to start.** A1–A4, C1–C3, E1–E4 are the real prize and need **zero** Antigravity install.

---

## Critic's reframe

The durable lesson here is **not "try Google Antigravity."** It's: **your harness (skills + rules) is now a set of open, cross-vendor standards — `SKILL.md` (Anthropic) and `AGENTS.md` (Linux Foundation) — so invest in *those*, not in any one IDE.** The video's real gift is the **Skill (capability) vs Rule (constraint)** discipline and the **harvest-a-session-into-a-skill** habit. Do A1–A4 (portability) + A3/C2 (hireui rules-as-standards) this week — that's real Goal-#2 deployment with zero install risk — and treat an Antigravity sandbox (B1/B2) as an optional, metered experiment, not the point.

---

## Suggested next action

Do **A1 + A2 today** (create `AGENTS.md` for the autopilot project; audit your four skills' `description`s) — ~1 hour, no install, immediately improves your live Claude Code hit-rate and makes the harness portable. Then schedule **A3** (harvest the Candidate-Detail refactor into a `SKILL.md` + `AGENTS.md` guard) as the week's real Goal-#2 deliverable, composing with your cc-sdd #1, how-we-claude-code verify, and open-design `DESIGN.md` pilots. Only after that, decide whether a metered Antigravity sandbox (B1/B2) is worth the preview caveats.
