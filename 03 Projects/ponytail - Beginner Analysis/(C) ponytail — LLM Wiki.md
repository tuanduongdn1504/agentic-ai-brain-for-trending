# (C) ponytail — LLM Wiki (v168)

> **Ship:** v168 · 2026-06-20 · branch `wiki/v168-ponytail` off `main` (at `b55e0d4` = v167)
> **Verdict:** GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG (near-STRONGEST) · (c) STRONG · (d) STRONG
> **Pattern outcome:** 1 NEW Library-vocab §C standalone (CORPUS-FIRST) — *"Quantified Anti-Over-Engineering / Code-Minimalism Agent-Behavior Ruleset"* (N=1) + a clean **Pattern #84 84c** "Provider-Agnostic-By-Design" instance-strengthening (no mint) + a **Library-vocab #12** LLM-routing-artifacts high-density instance (no mint). NO new top-level pattern. NO confirmed-count change (46 / 10).
> **Tier:** T1 Assistant Skill / cross-harness ruleset-plugin (code-minimalism methodology for AI coding agents; 14 platforms).
> ✅ **VARIES THE DOMAIN.** This is the **first ship to break out of the 14-consecutive "tool for operating/monitoring AI coding agents" niche (v153→v166)** — ponytail is a *code-minimalism methodology that modifies how the agent writes code*, not a tool that watches/hosts/orchestrates agents. It is exactly the "vary the domain" move the v167 audit's standing lever asked for. (The *pilot* lever still stands — ZERO of the catalogued tools piloted.)

---

## 1. What it is

`DietrichGebert/ponytail` — verbatim tagline:

> *"He says nothing. He writes one line. It works."* / *"Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote."*

A **cross-harness ruleset-plugin** that makes AI coding agents write *minimal, necessary* code by injecting a **decision-ladder** into the agent's pre-generation planning. It is **not** a tool you run *around* the agent (monitor, dashboard, multiplexer); it is a behavior layer that changes **what the agent writes**. Installable as a Claude Code plugin (`/plugin marketplace add DietrichGebert/ponytail` → `/plugin install ponytail@ponytail`), a Codex/Copilot-CLI plugin, an MCP server, or by copying native rule files into 14 different agent platforms.

**The decision-ladder (verbatim from `AGENTS.md`):**

1. *"Does this need to be built at all? (YAGNI)"*
2. *"Does the standard library already do this? Use it."*
3. *"Does a native platform feature cover it? Use it."*
4. *"Does an already-installed dependency solve it? Use it."*
5. *"Can this be one line? Make it one line."*
6. *"Only then: write the minimum code that works."*

**Explicit NOT-lazy carve-outs** (the safety spine): input validation at trust boundaries, error handling that prevents data loss, security, accessibility, calibration for real hardware. Non-trivial logic must carry *"ONE runnable check behind — the smallest thing that fails if the logic breaks."* Documentation philosophy: *"Boring over clever. Fewest files possible."*

The canonical "lazy" example (from the README):

```html
<!-- ponytail: browser has one -->
<input type="date">
```

— replacing the agent's habitual move of installing `flatpickr`, building a wrapper component, adding stylesheets, and debating timezones.

## 2. Capabilities

- **Mode levels** — `lite` / `full` (default) / `ultra` / `off`; set via `/ponytail [mode]` or `PONYTAIL_DEFAULT_MODE`. The runtime hook writes the active mode to a `.ponytail-active` file and re-injects the ruleset per turn.
- **Slash commands:**
  - `/ponytail [mode]` — set intensity / report current level.
  - `/ponytail-review` — scan the current diff for over-engineering; returns a delete-list tagged `delete` (dead code) / `stdlib` (reinvented stdlib) / `native` (platform duplication) / `yagni` (single-use abstraction) / `shrink` (line reduction), formatted `L[line]: [tag] [description]. [replacement]`, with a final sum of removable lines.
  - `/ponytail-audit` — same scan across the **whole repo**, ranked by removal impact; outputs total removable lines + dependencies.
  - `/ponytail-debt` — harvest `# ponytail:` / `// ponytail:` comment markers into a tracked technical-debt ledger (file / line / ceiling / trigger); flags markers without an upgrade trigger as silent debt-rot.
  - `/ponytail-gain` — display the benchmark scoreboard. **Notably forbids per-repo savings claims** (an honest-discipline guardrail).
  - `/ponytail-help` — quick reference.

## 3. The benchmark (honest, dual-methodology)

Ponytail ships an unusually rigorous and **self-caveating** benchmark in `benchmarks/`:

- **Single-shot** (5 everyday tasks × Haiku 4.5 / Sonnet 4.6 / Opus 4.8, 10 runs each): 80–94% fewer lines — but the authors **explicitly flag this as partly a "conversational artifact"** (prose-heavy baseline) and label it the *un-defensible* number.
- **Agentic (primary, "corrected, defensible version"):** headless Claude Code agents (Haiku 4.5) edit `tiangolo/full-stack-fastapi-template` across **12 feature tickets + 6 safety tasks**, **n=4 runs/task**, **3 arms** (baseline / `caveman` control skill / ponytail), measured by `git diff` line counts + Anthropic API telemetry, with a **secondary Sonnet-4.6 LLM judge** (published rubric) for the safety arm.

**Agentic headline results:** **−54% lines · −22% tokens · −20% cost · −27% time · 100% safety** (20/20 adversarial runs; the YAGNI one-liner variant scored 95% — failing a path-traversal guard — *demonstrating the safety↔minimalism trade-off honestly*).

**Disclosed limitations (verbatim-grade):** small n (n=4), **Haiku-only** agentic arm, six safety checks are *"a floor, not a comprehensive security proof"*, large frontend variance (300–570 LOC), and — crucially — cost savings are **Claude-scoped** (authors recommend narrowing the headline from "47-77% cheaper" to "42-75% cheaper"; *"the picture flips"* cross-provider, and **reasoning models show cost increases** because the ruleset is re-sent each call). This is real honest-deficiency-disclosure (Pattern #83 83b).

## 4. Architecture / distribution mechanism

**Canonical sources:** `skills/<name>/SKILL.md` (the six skills) + `AGENTS.md` (the universal ruleset read by generic platforms).

**14 declared platforms**, three injection mechanisms:
- **Hook-injected** (Claude Code, Codex, Copilot CLI): `.claude-plugin/plugin.json` → `hooks/claude-codex-hooks.json` declares a `SessionStart` hook (`ponytail-activate.js`, on startup/resume/clear/compact) + a `UserPromptSubmit` hook (`ponytail-mode-tracker.js`); the runtime emits context per-platform (JSON `additionalContext` for Copilot, `systemMessage` `PONYTAIL:{MODE}` for Codex, stdout for Claude).
- **Project-rule files** (Cursor `.cursor/rules/ponytail.mdc`, Windsurf `.windsurf/rules/ponytail.md`, Cline `.clinerules/`, Kiro `.kiro/steering/`, Copilot editor `.github/copilot-instructions.md`).
- **Always-on instruction file** (`AGENTS.md` at repo root for Antigravity / CodeWhale / Cline / generic); OpenCode via `experimental.chat.system.transform` per turn; Gemini/Antigravity CLI via `gemini-extension.json`; **MCP** via `ponytail-mcp/`.

**The alignment discipline (the engineering wrinkle):** the 6 platform-native rule copies are **hand-maintained but CI-drift-gated** — `scripts/check-rule-copies.js` does **byte-for-byte** comparison against canonical `AGENTS.md` and validates **7 critical rule-phrase invariants**, run on every push/PR via `.github/workflows/test.yml`. The OpenClaw skill package (`.openclaw/skills/`) is **auto-generated** from `skills/` via `scripts/build-openclaw-skills.js` (preserves rule body verbatim, rewrites frontmatter), with `tests/openclaw-skills.test.js` failing the build if the committed copy is stale. So the cross-harness distribution is a **hybrid**: repo-stored copies under invariant-CI enforcement (Pattern #84 84c.1) + CLI-generated package (84c.2).

**The MCP server (`ponytail-mcp/`)** is a **stateless, read-only distribution facade**: it exposes a `ponytail_instructions` tool + a `ponytail` prompt resource that return the ruleset at the requested mode. No persistent state, no runtime coordination → it is *another distribution surface*, **not** a shared-backend service (see §6, NOT Pattern #18).

**Stack:** JavaScript 57% / Python 42%; Node.js lifecycle hooks; `@modelcontextprotocol/sdk` + `zod` for the MCP server; MIT (*"The shortest license that works."*).

## 5. Phase 0.9 verdict — GOAL-ALIGNED INCLUDE 3/4

- **(a) FAIL.** `DietrichGebert` is a bare pseudonymous handle — GitHub profile and repo disclose **no real name, bio, affiliation, location, or links** (552 followers, 2 public repos). "Gebert" reads phonetically German, but that is a *heritage/name hint, not a disclosed identity*. Per the v151-audit rec (ii) + the v160 / v164 / v165 discipline (**no cultural-peer inferred from a name-looking handle**), **no axis is minted and no (a)-rescue is taken** — ponytail does not need one; it is goal-aligned via (b).
- **(b) STRONG (near-STRONGEST).** A *benchmarked code-minimalism methodology* injected into the agent's pre-generation planning across 14 harnesses = dead-center goal #1 ("master Claude and autonomous agents for software development"), and it changes **how the agent writes code** rather than sitting *around* it — more goal-central than the entire v153→v166 observability/operating run, and directly **pilotable into the vault's own heavy-Claude-Code workflow to cut token spend**. Held **STRONG-not-STRONGEST** = it is still a third-party ruleset layered *onto* the agent, not the substrate (Claude/Anthropic) or a methodology the vault itself has adopted (the v161 CodePilot "near-STRONGEST" calibration).
- **(c) STRONG.** Canonical-source + CLI generator + byte-for-byte drift checker + 7-invariant CI gate + a rigorous dual-methodology agentic benchmark (n=4, 3 arms incl. a control skill, secondary LLM judge) + MCP server + 14-platform adapters + hooks runtime. Mature for a days-old project (9 releases in 5 days; see §7).
- **(d) STRONG.** Pattern #84 84c family (v71/v72/v73/v75/v76); Library-vocab #12 LLM-routing-artifacts (generates the whole family of routing files); Pattern #83 83b honest-disclosure; sibling to v75 impeccable in the forming "rulesets that constrain the agent toward LESS" meta-theme.

## 6. Pattern Library outcome — 1 NEW §C standalone + clean #84 84c strengthening

**PRIMARY (the v158/v165 shape — clean instance + 1 corpus-first standalone):**

- **NEW Library-vocab §C standalone N=1 — "Quantified Anti-Over-Engineering / Code-Minimalism Agent-Behavior Ruleset."** An opinionated decision-ladder ruleset that constrains the agent toward *less code* (YAGNI → stdlib → native → installed-dep → one-line → minimum, with explicit safety carve-outs) + review-tooling (`/ponytail-review|audit|debt|gain`) + an agentic LOC/token/cost/time benchmark. **CORPUS-FIRST** — no prior subject is a *code-quantity* minimalism methodology. **Distinct from** the OC-layer **"Anti-Slop-Design-Curation"** track (v81/v85 taste-skill = *design aesthetics*) and **"voice-calibration personalization"** (v108 humanizer = *human voice*). **v75 impeccable is the design-quality SIBLING — NOT counted as N=2** (different dimension: code-quantity vs design-aesthetics). The forming meta-theme *"opinionated cross-harness rulesets that constrain the agent toward LESS"* (code / design / voice) is a **WATCH, not a pre-merge.** Promotion-eligible at a genuine 2nd code-minimalism ruleset. §28: **1 new standalone (≤2 cap honored).**

**Clean strengthening (NO mint):**

- **Pattern #84 84c "Provider-Agnostic-By-Design"** — a premium instance: 14 declared platforms; **hybrid mechanism** strengthens *both* 84c.1 (repo-stored copies, here under a byte-for-byte drift-checker + 7-invariant CI gate) *and* 84c.2 (CLI-generated `.openclaw/skills/`). Continues the v71→v72→v73→v75→v76 arc. The CI invariant-validation discipline is a more-rigorous take on multi-target alignment than v75's plain repo replicas — recorded as an **observation, not a mint.**
- **Library-vocab #12 LLM-routing artifacts** — a high-density multi-artifact instance: ponytail generates/maintains the whole family (`AGENTS.md` + `.cursor`/`.windsurf`/`.clinerules`/`.agents` rules + `.github/copilot-instructions.md` + `.kiro/steering` + `.openclaw/skills` + `gemini-extension.json` + `.claude-plugin/plugin.json` + `opencode.json`). Instance-strengthening of CONFIRMED #12.

**SECONDARY observations (NOT minted):**

- **Pattern #83 83b methodology-disclosure** — a genuine instance: honest benchmark caveats (small n, Haiku-only, "floor not comprehensive proof," recommends narrowing the headline claim, notes cross-provider flip + reasoning-model cost increase) + `/ponytail-gain` **forbids per-repo savings claims.**
- **Library-vocab #20 Token-Economy-Quantification** — *qualified-adjacent*: the benchmark explicitly quantifies token/cost impact (−22% / −20%), but it is **model-scoped** (Haiku-agentic; flips on reasoning models) and measures *intervention-effect* not *artifact-footprint* → recorded as a qualified instance with caveat, **not** a clean N+1 bump (anti-inflation).
- **`ponytail-mcp` = a distribution surface, NOT Pattern #18** (stateless read-only MCP facade; no shared backend / runtime coordination — REFUTED in verification).
- **NO corpus-recursion (Pattern #57 does NOT apply)** — verified: ponytail cites **zero** corpus subjects (no impeccable, agent-skills-standard, Anthropic skills, Karpathy, LLM-wiki). Only external references = `tiangolo/full-stack-fastapi-template` (benchmark testbed) + `JuliusBrussee/caveman` (control-arm skill).

## 7. §37 provenance

- **Page-stated:** ≈**40k★** / **1.9k forks** / **9 releases** (v1.0.0 → v4.7.0, **all within Jun 12–16 2026** — a front-loaded 5-day launch burst; benchmarks doc dated Jun 18). MIT. JS 57% / Python 42%. Owner `DietrichGebert` (no disclosed identity).
- **NOT API-verified (§37.4):** this environment **mocks the GitHub API** — stars/forks/dates are page-stated only. **Creation date not shown** on the rendered repo → age/velocity not establishable.
- ⚠️ **40k★ against a ~8-day-old release history would be extreme launch-week virality IF accurate — but it is unverifiable, so it is explicitly NOT a Pattern #52 claim.** Treat the magnitude as page-stated-only. (In a mocked-API sandbox the figure may itself be synthetic; §37.4 exists precisely for this.)
- No `CHANGELOG.md` (404); per-platform rule-evolution timeline not documented.

## 8. Streak / state

- **Streak:** `GA:29 · OG:11 [7 ov]` → **`GA:30 · OG:11 [7 ov]`** (30th GOAL-ALIGNED PASS; NOT an override).
- **§35:** window {v165 GA, v166 GA, **v168 GA**} = 0 OG → **STAYS CLEAR.** (v167 was an audit, not a ship.) 15 consecutive goal-aligned ships v153→v168 — **but v168 finally VARIES THE DOMAIN.**
- **Counts:** 46 confirmed patterns / 10 CONFIRMED Library-vocab **UNCHANGED**. Tracked PROVISIONAL surface ≈26 → **≈27** (+1 §C standalone).

## 9. Pilot note

**Strong, genuinely on-goal pilot candidate — and the most directly useful-to-the-vault subject in a long while:** ponytail is a Claude Code plugin (MIT, reversible) whose entire purpose is to make Claude Code write *less* code → it could **measurably cut the vault's own token/cost spend** on wiki builds and pilots. ⚠️ **Pilot fence:** it installs **hooks into your CLI configs** (`.claude-plugin`, `~/.claude/...`, a `.ponytail-active` state file) and injects a system-level ruleset that changes agent behavior → `install-snapshot` first + snapshot the configs + trial in `lite`/`full` on a scratch repo before `ultra` on real work; mind the disclosed safety↔minimalism trade-off (the YAGNI variant dropped a path-traversal guard) — keep the NOT-lazy carve-outs and run `/ponytail-review` rather than blind-trusting the cut.

✅ **And unlike a pilot of any v153→v166 tool, piloting ponytail is BOTH a pilot AND a domain-variation** — it directly addresses both standing levers at once.

## Suggested next action

Commit the v168 ship on `wiki/v168-ponytail` (don't merge — operator reviews + merges). Then **pilot ponytail in the vault's own Claude Code workflow** (`lite`/`full` on a scratch wiki build, measure the token delta) — it is the rare subject that is both on-goal and immediately useful, and it discharges both the "vary the domain" and "pilot one" levers from the v167 audit.
