---
title: "(C) agent-skills — Beginner Analysis (v184 wiki)"
subject: addyosmani/agent-skills
author_of_subject: Addy Osmani
wiki_version: v184
date: 2026-06-30
source_commit: aba7c4e (2026-06-28)
license: MIT
generated_by: Claude (LLM Wiki Routine v2.6)
---

# Addy Osmani's `agent-skills` — Beginner Analysis & Knowledge Deep-Dive

> **One line:** A cross-harness Claude Code **plugin / skill marketplace** that encodes the full senior-engineering lifecycle — Define → Plan → Build → Verify → Review → Ship — as **24 process-driven skills + 4 review personas + 8 slash commands + hooks + reference checklists**, so an AI coding agent follows the same discipline a senior engineer does instead of taking the shortest path to "done."

- **Repo:** `github.com/addyosmani/agent-skills` · **commit verified:** `aba7c4e` (2026-06-28) · **License:** MIT (© 2025 Addy Osmani)
- **Author:** **Addy Osmani** — Director at Google Cloud AI (Cloud AI Developer Experience); previously led **Chrome Developer Experience for 10+ years** (created **Lighthouse**, co-led **Core Web Vitals**, ran DevTools); author of *Learning JavaScript Design Patterns* (O'Reilly) and *Image Optimization* (Smashing); creator of Yeoman / TodoMVC / Workbox. *(All page-stated from `addyosmani.com/bio` — confidence: stated.)*
- **What it ships:** 24 skills (23 lifecycle + 1 meta `using-agent-skills`) · `agents/` 4 personas · `.claude/commands` + `.gemini/commands` + `commands/` (8 each) · `hooks/` (session-start, sdd-cache, simplify-ignore) · `references/` (7 checklists) · cross-harness setup for **Claude Code, Cursor, Gemini CLI, Antigravity, OpenCode, Windsurf, Copilot, Kiro** · `63 .md / 16 .toml / 7 .sh / 4 .json`.
- **Distribution:** `/plugin marketplace add addyosmani/agent-skills` → `/plugin install agent-skills@addy-agent-skills`. Plain Markdown skills work with any agent that accepts instruction files.

---

## 1. The thesis: this is "Beyond the 70%" turned into runnable scaffolding

`agent-skills` is the executable form of Addy Osmani's well-known **"70% problem"** argument:

- **The 70% problem** (Osmani, Dec 2024): AI tools rapidly produce ~70% of a solution, but the final **30% — edge cases, error handling, accessibility, security, production integration — remains equally time-consuming**, because the bottleneck was never *velocity*; it's *engineering judgment*.
- **The Knowledge Paradox:** AI helps **experienced** engineers more than beginners, because skilled engineers have the mental models to steer, debug, and maintain AI output. Juniors hit the "two-steps-back" wall.
- **The fix Osmani prescribes** ("Beyond the 70%: Maximizing the Human 30%"): seven durable disciplines — system design, edge-case handling, review/testing, debugging, contextual understanding, communication, continuous learning — that AI cannot replace.

`agent-skills` **operationalizes that 30%**: it treats the AI agent as *"an extremely capable junior engineer"* and wraps it in the scaffolding — checkpoints, verification gates, anti-rationalization rebuttals — that a senior engineer carries in their head. Repo tagline of the philosophy: *"A senior engineer's job is mostly the parts that don't show up in the diff."* It also encodes Osmani's **"vibe coding vs. AI-assisted engineering"** split (sketch with vibe; ship with discipline) and his 2025 **"Loop Engineering"** idea — *designing the system that prompts the agent, instead of prompting it yourself* — which is the same philosophy this vault runs on (Karpathy's LLM-Wiki / autopilot pattern). See [[project_multi_agent_orchestration_pilot_thread]] and the vault's own routine.

---

## 2. Architecture — the lifecycle as a router

```
  DEFINE          PLAN           BUILD          VERIFY         REVIEW          SHIP
 ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐
 │ Idea │ ───▶ │ Spec │ ───▶ │ Code │ ───▶ │ Test │ ───▶ │  QA  │ ───▶ │  Go  │
 └──────┘      └──────┘      └──────┘      └──────┘      └──────┘      └──────┘
  /spec          /plan          /build        /test         /review       /ship
```

Four layers, all composed:

1. **`using-agent-skills` (the meta-router).** A dispatcher skill that maps incoming work to the right skill and enforces **six non-negotiable operating behaviors that apply to ALL skills**: **Surface Assumptions · Manage Confusion Actively · Push Back When Warranted · Enforce Simplicity · Maintain Scope Discipline · Verify, Don't Assume.** A full feature typically runs ~13–16 skills in sequence.
2. **8 slash commands** mapped 1:1 to phases: `/spec` `/plan` `/build` `/test` `/review` `/code-simplify` `/ship` (+ `/webperf`). `/build auto` generates the plan and implements every task in one approved pass — removing the human *between* tasks, not the verification (each task still test-driven + committed individually, pauses on failure).
3. **4 review personas** (`agents/`) fanned out **in parallel by `/ship`** → a single go/no-go: `code-reviewer` (Senior Staff Eng, five-axis), `security-auditor` (STRIDE + OWASP), `test-engineer` (Prove-It + coverage), `web-performance-auditor` (Core Web Vitals; via `/webperf`, **not** in `/ship` because it's web-only). **Hard orchestration rule: personas never invoke other personas** — keeps each focused, prevents context contamination, makes parallelism safe.
4. **Hooks + references.** `SessionStart` injects the meta-skill; `sdd-cache-pre/post` revalidates spec docs without relying on memory; `simplify-ignore` protects perf-critical code from being "simplified." 7 reference checklists (definition-of-done, testing-patterns, security, performance, accessibility, observability, orchestration-patterns) load on demand.

### Skill anatomy (the format that makes it work)
Every `SKILL.md`: **Overview → When to Use → Process (numbered steps / decision-ladder) → Common Rationalizations (excuse → rebuttal table) → Red Flags → Verification (evidence gates).** Four design choices: **process not prose** (workflows, not reference docs) · **anti-rationalization** (every skip-worthy step has a documented counter-argument) · **verification non-negotiable** ("seems right" is never sufficient) · **progressive disclosure** (only name+description sit in context at startup; the body loads on demand; keep `SKILL.md` < 500 lines). This is the single most distinctive mechanic in the pack — the **"Common Rationalizations" table is the immune system against an agent talking itself out of doing the work.**

---

## 3. The knowledge — what all 24 skills actually teach

> This is the "double deep dive." Each entry distills the real heuristics, exact thresholds, and the rebuttal-to-the-excuse that the skill ships.

### DEFINE — clarify what to build

**`interview-me`** — one-question-at-a-time requirement interrogation until ~95% confidence.
- **Process:** hypothesize the ask in one sentence + an honest confidence number (0–100; if <70%, attach a one-line reason). Ask **one** question at a time, each with **your guess attached** ("Q: … GUESS: …"). Restate intent in the user's words (Outcome / User / Why now / Success / Constraint / **Out of scope**). Confirm with an **explicit yes** — *"whatever you think," "sounds good," silence are NOT yes.*
- **Stop condition (checkable):** *"Can I predict the user's reaction to the next three questions I'd ask?"* If yes → done.
- **Key move:** when the user signals sophistication ("scalable," "clean," "modern") without specifics, probe: *"If you didn't have to justify this to anyone, what would you actually want?"*

**`idea-refine`** — divergent → convergent idea sharpening.
- Phase 1 (expand): restate as a "How Might We," generate **5–8** variations via lenses (Inversion / Constraint-removal / Audience-shift / Combination / Simplification / 10×). Phase 2 (converge): cluster into 2–3 directions, stress-test on User value / Feasibility / Differentiation, **surface hidden assumptions** (the #1 killer of good ideas). Phase 3: a one-pager whose **"Not Doing" list is the most valuable part** — focus is saying no to good ideas.

**`spec-driven-development`** — write the PRD before code.
- **Six non-negotiable areas:** Objective · Commands (full, with flags) · Project Structure · Code Style (*one real snippet beats three paragraphs*) · Testing Strategy · **Boundaries (three-tier: Always do / Ask first / Never do)**.
- Surface assumptions up front: *"Correct me now or I'll proceed with these."* Reframe vague asks as testable criteria ("make faster" → "Dashboard LCP < 2.5s on 4G, CLS < 0.1"). The spec is a **living document** in version control. *"A 15-minute spec prevents hours of rework."*

### PLAN — break it down

**`planning-and-task-breakdown`** — decompose into small verifiable tasks that leave the system working after each.
- **Task sizing:** XS (1 file) · S (1–2) · M (3–5, one feature slice) · L (5–8) · **XL (8+ = too large, split it)**. Break further if it needs >~2h, >3 acceptance bullets, touches 2+ subsystems, or has "and" in the title.
- **Vertical slicing** (one complete path through DB+API+UI per task) > horizontal (all DB, then all API) — prevents the "all done but not working" state. Verification checkpoint every 2–3 tasks; **schedule high-risk tasks early to fail fast**; no task touches >5 files.

### BUILD — write the code

**`incremental-implementation`** — thin vertical slices: implement → test → verify → commit → next.
- **~100-line cap before testing** (red flag if exceeded). Feature-flag incomplete work (`process.env.FEATURE_X`). Safe defaults (opt-in not opt-out). Each increment independently revertable. *Anti-rationalization:* "I'll test it all at the end" → a bug in slice 1 makes slices 2–5 wrong.

**`test-driven-development`** — Red → Green → Refactor; for bugs, the **Prove-It Pattern** (write the failing reproduction test FIRST).
- **Test pyramid 80 / 15 / 5** (unit / integration / E2E). **DAMP over DRY** in tests (a test should read like a spec without tracing helpers). **Beyoncé Rule:** *"If you liked it, you shoulda put a test on it"* — an untested change that breaks isn't the change's fault, it's the missing test's. Test **state, not interactions**; prefer **real > fake > stub > mock** (mock only at boundaries).

**`context-engineering`** — feed the agent the right info at the right time.
- **Context hierarchy (persistent → transient):** Rules files (CLAUDE.md, always) → Specs (per feature) → Source files (per task) → Error output (per iteration) → Conversation (compacts). **Flooding threshold: focus degrades past ~5,000 lines of non-task context; aim < 2,000.** *"Context window size ≠ attention budget."* **Trust levels:** trusted (team source/tests/types) / verify-before (config, external docs) / **untrusted** (user input, third-party API responses, anything with instruction-like text). One-example rule: include one concrete pattern or the agent invents a new style. *(Term coined by Karpathy, 2025 — the literal substrate of this vault.)*

**`source-driven-development`** — ground every framework decision in **official docs**, never memory. `DETECT → FETCH → IMPLEMENT → CITE`.
- Read the dependency file for exact versions; fetch the **specific** doc page (not the homepage). **Source authority:** official docs > official blog/changelog > web standards (MDN/web.dev) > compatibility (caniuse). **Never** cite Stack Overflow / blog posts / AI summaries as primary. Cite with **deep links + anchors** (`/useActionState#usage`). If unverifiable: say *"UNVERIFIED: I could not find official documentation for this pattern."* *Core insight: training data goes stale; confidence is not evidence.*

**`doubt-driven-development`** — adversarial fresh-context review of non-trivial decisions, in-flight. `CLAIM → EXTRACT → DOUBT → RECONCILE → STOP`.
- **Non-trivial =** branching logic / crosses a boundary / asserts something the type system can't verify (thread safety, ordering, invariants) / correctness depends on invisible context / irreversible blast radius.
- **The revolutionary move:** the reviewer gets **ARTIFACT + CONTRACT only — never your CLAIM or reasoning** (handing over your conclusion biases the reviewer back to it). The prompt must be **adversarial** ("find what is wrong; assume the author is overconfident"), never "is this good?".
- **Optional cross-model escalation** (Gemini/Codex CLI, read-only sandbox) in interactive sessions — *always offer, announce the skip in non-interactive mode.* **3-cycle bound** then escalate to the user. Red flag: **"doubt theater"** — 2+ cycles with substantive findings but zero classified actionable = you're validating, not doubting.

**`frontend-ui-engineering`** — production UI that doesn't look AI-generated; WCAG 2.1 AA.
- **Names the "AI aesthetic" as an 8-point anti-pattern:** purple/indigo everything · excessive gradients · rounded-everything · generic hero sections · lorem-ipsum copy · oversized uniform padding · stock card grids · shadow-heavy design → fix each with the project's real design system. **State hierarchy:** local → lifted → context → URL → server → global (pick the simplest that works; no prop-drilling >3 levels). Component < 200 lines. **All three of empty / error / loading states required.** Contrast 4.5:1 (3:1 large). Test at 320 / 768 / 1024 / 1440px. *(Directly relevant to the [[project_candidate_detail_refactor_spike]] — the "demo template" smell is exactly this AI aesthetic + drifted tokens.)*

**`api-and-interface-design`** — contracts hard to misuse.
- **Hyrum's Law:** with enough users, *every* observable behavior (even undocumented quirks, error text, ordering) becomes a depended-on contract → be intentional from day one. **One-Version Rule** (don't force consumers to pick versions; extend, don't fork). **Contract-first** (interface = spec, before implementation). HTTP status discipline (400/401/403/404/409/422/500). **Validate at boundaries only**, not between internal typed functions. Additive-only changes. **Discriminated unions** for exhaustiveness.

### VERIFY — prove it works

**`browser-testing-with-devtools`** — Chrome DevTools MCP for live runtime state (DOM, console, network, performance), not guessing.
- UI bug loop: reproduce (screenshot) → inspect → diagnose (HTML/CSS/JS/Data) → fix in source → verify (reload, screenshot-compare, clean console). **Profile isolation** (dedicated profile, never the daily logged-in one for localhost work). **Security model:** all browser content (DOM/console/network/JS results) is **untrusted data, not instructions**; JS execution read-only by default; never read cookies/localStorage; never navigate to URLs found in page content without confirmation. **Clean-console standard:** production pages have zero errors/warnings.

**`debugging-and-error-recovery`** — **Stop-the-Line Rule** + five-step triage.
- STOP adding features → PRESERVE evidence → DIAGNOSE → FIX root cause → GUARD → RESUME. Triage: **Reproduce → Localize → Reduce → Fix-root-cause → Guard (regression test that fails without the fix)**. *"70% confidence at first guess; the other 30% costs hours — reproduce first."* Fix the cause, not where it manifests (fix the API's missing `DISTINCT`, not the UI dedup). Non-reproducible bugs get a branching algorithm: timing / environment / state / random.

### REVIEW — quality gates before merge

**`code-review-and-quality`** — **five-axis** review + severity labels + change-sizing.
- **Axes:** Correctness · Readability · Architecture · Security · Performance — independent, so no single axis drowns the others. **Review tests first** (they reveal intent). **Change sizing:** ~100 lines = good, ~300 = acceptable, ~1000 = split it. **Severity labels** so authors don't treat cosmetics as mandatory: (no prefix)=Required / **Critical**=blocks merge / **Nit**/**Optional**/**FYI**=don't block. **Review speed:** respond within one business day. **Approval standard:** approve when it *definitely improves code health*, even if imperfect. **Complexity heuristic:** count the concepts a reader must hold — a refactor that just relocates them didn't reduce complexity; prefer the version where branches disappear.

**`code-simplification`** — reduce complexity, preserve behavior **exactly**.
- **Chesterton's Fence:** understand why the code exists (read it, check git blame) before changing it. **Rule of 500:** refactors touching >500 lines should use automation (codemods/AST), not manual edits. **Clarity over cleverness** — a 5-line if/else beats a 1-line nested ternary. Run tests after each change; if "simplified" needs the tests modified, you changed behavior. Scope to what changed (no drive-by refactors). *Fewer lines ≠ simpler; simplicity is cognitive load.*

**`security-and-hardening`** — threat-model first, defense-in-depth.
- **Map trust boundaries → name assets → STRIDE each boundary → write abuse cases → apply the Three-Tier Boundary System** (Always: parameterize queries, validate input, encode output, bcrypt ≥12, security headers, httpOnly/secure/sameSite cookies, `npm audit` / Ask-first: new auth, new data storage, CORS changes, file uploads / Never: commit secrets, log PII, trust client-side validation, `eval`/`innerHTML` with user data, sessions in localStorage). Covers **OWASP Top 10** *and* **OWASP LLM Top 10** — key insight: **the system prompt is NOT a security boundary; enforce permissions in code.** Treat all model output as untrusted input.

**`performance-optimization`** — **measure first.** `MEASURE → IDENTIFY → FIX → VERIFY → GUARD`.
- **Core Web Vitals:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (Good). Synthetic (Lighthouse, for CI) + RUM (web-vitals/CrUX) are complementary, not interchangeable. **Perf budget:** JS < 200KB gz initial, CSS < 50KB, TTFB < 800ms, Lighthouse ≥ 90. Fix N+1 with joins; paginate; modern image formats + explicit dimensions (CLS); chunk long tasks > 50ms with `scheduler.yield()` for INP; `React.memo`/`useMemo` only where profiling proves it.

### SHIP — deploy with confidence

**`git-workflow-and-versioning`** — git as save-points + sandboxes.
- **Trunk-based** (main always deployable; feature branches 1–3 days; DORA correlation). **Atomic commits** (one logical thing). ~100 lines/commit. **Commit messages explain WHY, not what** (`feat:`/`fix:`/`refactor:`…). Save-point pattern: a failed test costs you at most one increment. Feature flags > long branches; never force-push shared branches.

**`ci-cd-and-automation`** — quality gates as enforcement. **Shift Left · Faster is Safer.**
- Pipeline: lint → types → unit → build → integration → E2E → security audit → bundle-size. No gate skippable. CI target < 10 min. **Feature-flag lifecycle:** Deploy OFF → team → canary 5% → 25/50/100% → clean up within 2 weeks. **Rollout thresholds:** advance if error rate within 10% baseline + p95 within 20%; **roll back if error > 2× baseline or p95 > 50% above.**

**`deprecation-and-migration`** — **code is a liability, not an asset.**
- Decision questions (unique value? consumer count? replacement exists? migration cost vs maintenance cost?). **Default to advisory** deprecation unless security/blocking forces compulsory. **The Churn Rule:** if you own the deprecated infra, *you* migrate the users (don't announce-and-abandon). Strangler / adapter patterns. Plan deprecation **at design time** ("how would we remove this in 3 years?"). Remove only after verified zero usage.

**`documentation-and-adrs`** — document the **why**, not the what.
- **ADRs** (Architecture Decision Records, Michael Nygard format) in `docs/decisions/` numbered, never deleted (supersede with a new one). Capture Context / Decision / Alternatives / Consequences. *"A 10-minute ADR prevents a 2-hour debate six months later."* Comment the why (the sliding-window rate-limit), not the obvious. Delete commented-out code; no lingering TODOs.

**`observability-and-instrumentation`** — *"code you can't observe is code you can't operate."*
- **Define 2–4 on-call questions BEFORE instrumenting**; every signal answers one. **Metrics tell you THAT, traces tell you WHERE, logs tell you WHY.** **RED** (Rate/Errors/Duration) per endpoint + dependency; **USE** (Utilization/Saturation/Errors) for resources. **Cardinality rule:** labels from small fixed sets — never user IDs / raw URLs / error text. **Percentiles always (p50/p95/p99), never averages.** Correlation ID on every log line. **Alert on symptoms** (error rate > 1% for 5 min, p99 > 2s), **not causes** (CPU 85%). Two severities: page / ticket. Never log secrets/PII. *(Directly feeds [[project_cc_observability_pilot_thread]].)*

**`shipping-and-launch`** — reversible, observable, incremental.
- 6-category pre-launch checklist (code / security / perf / a11y / infra / docs, 30+ checkpoints). Feature flags decouple **deploy** from **release**. Staged rollout: Staging → Prod (OFF) → team 24h → canary 5% (24–48h) → 25/50/100%. **Rollback times:** flag < 1 min, revert < 5 min, DB < 15 min. Monitor the first hour. *"It's Friday afternoon, let's ship it" is a red flag.*

---

## 4. The upstream canon (where the principles come from)

The pack deliberately bakes in **Google's engineering culture** (*Software Engineering at Google*, `google/eng-practices`). The named principles and their origins:

| Principle (in the skill) | Origin | Confidence |
|---|---|---|
| **Hyrum's Law** | Hyrum Wright (Google); coined by Titus Winters in *SWE at Google* | high |
| **Beyoncé Rule** | *SWE at Google* (testing chapter) | high |
| **Chesterton's Fence** | G.K. Chesterton parable, applied to refactoring | high |
| **Test pyramid / TDD / Red-Green-Refactor** | Kent Beck, XP, late-1990s (*TDD By Example*, 2002) | high |
| **Trunk-based development** | 1990s VCS lineage; Google since 1998; DORA research | high |
| **Shift Left** | Agile/DevOps QA practice | high |
| **Context engineering** | Andrej Karpathy, 2025 (*"filling the context window with just the right info"*) | high |
| **Core Web Vitals / Lighthouse** | Google — **co-created by Osmani himself** | stated |
| **RED metrics / USE metrics / OpenTelemetry** | Google (RED) / Brendan Gregg (USE) / CNCF (OTel) | high |
| **ADR format** | Michael Nygard | stated |

The point: **this isn't invented methodology — it's the canonical SDLC discipline, compressed into step-by-step workflows an agent can't rationalize its way out of.**

---

## 5. How it compares (all three peers are corpus subjects)

Addy ships an honest `docs/comparison.md` against two peers — **both already in this vault's corpus**:

| | **agent-skills** (v184) | **Superpowers** — obra / Jesse Vincent *(corpus, ~v2-era)* | **Matt Pocock's skills** *(corpus, v57)* |
|---|---|---|---|
| Core idea | Full SDLC as skills + router | Complete autonomous *methodology* | One expert's daily `.claude` toolkit |
| Organizing principle | SDLC phases + meta-router | brainstorm → plan → execute loop | curated focused commands |
| Distinctive mechanism | **anti-rationalization tables + Red Flags + parallel review personas** | subagents + git-worktree isolation + skills-that-write-skills | `/grill-me` requirement interrogation + strict agent TDD |
| Best for | guided lifecycle, human checkpoint per phase | long autonomous / exploratory runs | sharp low-ceremony daily TS loop |

- Addy's honest note: *"None is 'best' in the abstract."* Cherry-pick **individual** skills freely (Markdown, not runtimes), but **never run two as your active router at once** — they fight over command names (`/tdd` in two places) and routing logic. Pick one primary router; borrow the rest à la carte.
- He cites a controlled head-to-head (Om Mishra, LinkedIn): same model/repo/prompt — agent-skills moved to code faster (~8 vs ~12 min) and ran **more validation passes** (7 vs 5, catching an out-of-feature regression); Superpowers invested more upfront architectural reasoning. *"Pick the tool to the task."* **One-developer single-task experiment, not a benchmark** — flagged as such.
- **Honest-disclosure signal:** the comparison doc deliberately **omits adoption/star numbers** (*"cited wildly differently across blogs; we've left them out rather than repeat unverified figures"*) and invites correction PRs. (Pattern #83 family.)

---

## 6. Verdict (inline, hand-verified — not delegated to the build workflow)

> Per the standing discipline ([[feedback_wiki_verify_independently_check_collisions]]), all corpus-fact / collision / identity claims below were verified **by hand** (grep over `_state/` + `_patterns/` + `03 Projects/`; the §C standalone list; the precedent rows). The 10-agent workflow did **source-reading + upstream research only** — safe, factual knowledge extraction.

**GOAL-ALIGNED INCLUDE 3/4** — `[(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG]`.

- **(a) FAIL.** Addy Osmani is a **notable individual industry figure** (Google Cloud AI / ex-Chrome DevEx), **not Anthropic**, and "notable framework author / industry authority" is not a registered (a) axis. The disclosed-notable-builder (a)-axis is held **operator-reviewable at N=3 per the v182 audit** (Waishnav v171 + Neo Reid v174 + Jack Le v181) — **not reopened here.** Addy is arguably the **most prominent disclosed individual author the corpus has had** (after Evan Bacon v183), reinforcing the open question but not resolving it. First Addy-Osmani author → **#19 19a**. *Not relied on; the tier keys on (b).*
- **(b) STRONG — keys the tier.** A library of production-grade **engineering-discipline skills for AI coding agents, Claude-Code-first** = dead-center on Goal #1 ("master Claude and autonomous agents for software development") **and on the vault's own `05 Skills/` substrate**, and **immediately pilotable** into the operator's workflow (install the plugin, run the commands). STRONG-not-STRONGEST: third-party + Claude is one of 8 supported harnesses + it's process-scaffolding, not Anthropic substrate. Calibrates above ponytail v168 (single ruleset) — this is a full SDLC suite.
- **(c) STRONG.** 24 SDLC skills + 4 personas + 8 commands × 3 harness command-dirs + hooks + 7 reference checklists + cross-harness setup + validation scripts + CI, by a top-tier author, with an honest self-comparison doc. Caveat: the *hard* engineering is the canon (Google SWE) Addy packages, not novel CS — but the packaging + anti-rationalization design is real and substantial.
- **(d) STRONG.** Dense agent-skills-ecosystem web (see §7).

### Pattern outcome — RE-REGISTER §C standalone #4 at N=2

**RE-REGISTER "Multi-Domain (Cross-Functional) Skill Collection" → N=2** (CodexKit **v121** + agent-skills **v184**). This §C standalone was N=1 (CodexKit) and **RETIRED at the v151 audit** (§28.3, ~30 wikis at N=1) **with an explicit rule: *"Re-registerable; N=2 if a 2nd horizontal/cross-functional skill collection appears."*** Addy's pack is that genuine, cross-author 2nd instance — a multi-domain collection spanning many engineering verticals (frontend, security, perf, testing, CI/CD, docs, debugging, git, API…), structurally contrasting the **CONFIRMED Domain-Vertical-Skill-Collection** pattern (N=4, *single*-vertical each — **NOT incremented** by this multi-domain instance). Re-registration at N=2 credits CodexKit's priority, exactly the **codebase-memory-mcp v172 / camofox v179** N=2 precedent.

**The distinguishing facet is recorded, NOT separately minted** (anti-"draw-the-circle", the camofox v179 declined-separate-mint precedent): Addy's pack differs from CodexKit's flat 90-skill (eng + business-ops) bundle by being **full-SDLC-coherent + cross-harness-plugin-packaged + persona/command/hook-bearing + by a notable individual** — a complete *engineering operating system*, not a flat skill list. That richness is a within-class variation, not grounds for a fresh N=1. Surfaces a clean **audit note:** whether §C #4 (multi-domain, coherent) and §C #10 (khazix v138 "Personal Daily-Driver, eclectic") should merge — they shouldn't yet; Addy's is coherent-SDLC, sharpening the distinction.

**Counts UNCHANGED: 46 patterns / 11 CONFIRMED Library-vocab.** §C live standalones **29 → 30** (re-register #4 back to live). Tracked PROVISIONAL surface ≈36 → **≈37**.

### Secondary observations (NOT minted)
- **#84 84c provider-agnostic-by-design** — cross-harness distribution (`.claude` / `.gemini` / `.opencode` + Cursor/Windsurf/Copilot/Kiro docs; 3 native command-dirs). NO N-bump per v86. (Distinct from the v168 ponytail "14-platform rule-file generator" mechanism — Addy distributes one skill set many harnesses consume; no drift-checker/CLI-generator.)
- **#12 LLM-routing-artifacts** — high-density instance (AGENTS.md + CLAUDE.md + GEMINI/`.gemini` commands + plugin.json + marketplace.json + hooks.json + per-harness configs). NO N-bump.
- **#83 honest-disclosure family** — the `comparison.md` deliberately omits unverified adoption numbers + invites correction ("we'd rather be fair than flattering").
- **Spec-driven cross-reference** — `spec-driven-development` ties to **spec-kit v17 / cc-sdd v61 / OpenSpec** (the [[project_hireui_pilot_target]] runs cc-sdd as method #1).
- **#80/#83 honest comparison** — a tool-level honest peer comparison (vs Superpowers + Pocock).

### Non-claims
- **NOT a new top-level pattern** (max stays #85). **NOT corpus-first** (CodexKit v121 holds skill-collection priority; mattpocock v57 / Superpowers ~v2 / karpathy v63 / vercel v51 / khazix v138 / agent-skills-standard v76 already populate the genre).
- **NOT #52 (viral velocity)** — README/Trendshift-badge/blog star figures (~27K cited) are **page-stated, NOT API-verified** (§37.4) → velocity unestablishable. Notably **Addy himself omits the numbers** in `comparison.md`.
- **NOT #57 (corpus-recursive)** — the comparison doc *compares against* corpus subjects (Superpowers, Pocock) as landscape peers and cites Google SWE canon as influence; **mentions/comparison ≠ recursion**. (A genuine cross-reference, recorded under (d), not a citation-of-influence promotion.)
- **NOT #18 B1-MCP** — a plugin/skill pack, not an MCP server.
- **NOT the Domain-Vertical-Skill-Collection pattern** (that's single-vertical; this is multi-domain → re-registers §C #4 instead).

**Tier: T1 Skill/Methodology Collection** (agent-skill library, the karpathy-skills v63 / mattpocock v57 / CodexKit v121 / khazix v138 family).

**Streak:** `GA:44 → GA:45` (under the v176 OFF-GOAL reading → GA:44·OG:12). **§35 CLEAR** — rolling-3 window {v181 GA, v183 GA, **v184 GA**} = 0 OG (v182 audit excluded). **30 consecutive goal-aligned ships v153 → v184.**

---

## 7. Cross-references (the (d) web)

- **Skill-collection genre (corpus):** CodexKit v121 (the §C #4 N=1 anchor) · karpathy-skills v63 · mattpocock-skills v57 · agent-skills-of-vercel v51 · khazix-skills v138 (§C #10) · agent-skills-standard v76 (the codification) · awesome-claude-skills v50 · Superpowers (~v2) · ui-ux-pro-max v85.
- **Skill tooling around the genre:** SkillSpector v169 (defensive scanner — could vet this pack) · SkillOpt v178 (text-space optimizer — could optimize one of these skills) · ponytail v168 (code-minimalism ruleset — composes with `code-simplification`).
- **Spec-driven lineage:** spec-kit v17 · cc-sdd v61 · OpenSpec · BMAD (hireui harness).
- **Vault philosophy:** Karpathy LLM-Wiki pattern (this vault's foundation) + Addy's "Loop Engineering" = the same idea; "context engineering" (Karpathy) = the literal substrate.
- **Operator pilot threads it lands on:** [[project_candidate_detail_refactor_spike]] (frontend-ui-engineering's "AI aesthetic" anti-pattern) · [[project_cc_observability_pilot_thread]] (observability skill) · [[project_prompt_eval_pilot_thread]] / cc-sdd (spec + verify) · [[project_hireui_no_llm_yet]] (the security skill's OWASP-LLM section when hireui adds an LLM) · [[project_multi_agent_orchestration_pilot_thread]] (the `/ship` parallel-persona fan-out).

---

## 8. Provenance & caveats (§37)
- Source-verified at commit **`aba7c4e`** (clone read-only). Structure/skill content read directly from `SKILL.md` files (24 skills + 7 references + 4 personas + docs).
- **Star/adoption counts** (~27K agent-skills, 120k+ Superpowers, 20.4k Pocock) — **page-stated, NOT API-verified** (§37.4). Used as rough indicators only.
- **Author identity facts** — "stated" from `addyosmani.com/bio` (self-reported, generally reliable, not third-party-confirmed).
- The "70% / 30%" split is **illustrative, not measured**; Osmani uses it as a concept.
- Two referenced supporting files in `idea-refine/` (`frameworks.md`, `refinement-criteria.md`, `examples.md`) were noted by the reader as **referenced-but-not-present** in the clone — minor packaging gap, flagged.

---

## 9. Bottom line
For a software developer + Scrum coach mastering AI-assisted engineering, `agent-skills` is the single most directly-pilotable subject in the recent run: it's a free, MIT, Claude-Code-first plugin that turns "the parts that don't show up in the diff" into rules the agent follows. It re-registers the corpus's **multi-domain skill-collection** standalone at N=2 and sits cleanly in the genre this vault already documents deeply. **→ See the companion `(C) agent-skills — Pilot Methods Menu.md` for how to apply it.**
