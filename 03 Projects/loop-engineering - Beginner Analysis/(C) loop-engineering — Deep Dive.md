# (C) loop-engineering — Deep Dive (v189)

**Subject:** `cobusgreyling/loop-engineering` — https://github.com/cobusgreyling/loop-engineering
**Ship date:** 2026-07-02 · **Cloned + source-verified at commit `f18df04`** (f18df044362adc5ec1ea78c1bd87dd3bc888bd57, last commit 2026-07-01) · **First commit 2026-06-09 (clone-verified) → ~22 days old, 123 commits, 20+ release tags**
**License:** MIT · **Repo v1.5.0** (2026-06-30) · **4.7k★ / 596 forks (as of 2026-07, repo page — confidence: stated, NOT API-verified §37.4)**
**Languages (page-stated):** JavaScript 55.5% / TypeScript 35.6% / Shell 5.7% / Python 3.2%. Local count: 333 files (198 MD / 13 TS / 11 JS-MJS / 29 JSON / 26 YAML); ~7.4K lines TS/JS vs ~8.7K lines Markdown — **a methodology repo with tooling, not a platform.**

> **"Stop prompting. Design the loop. Get a score."** (README tagline)
> **"Loop engineering replaces you as the person who prompts the agent — you design the system that does it instead."** (README line 46)

---

## 1. What it is

A **reference implementation + toolkit for "loop engineering"** — designing the scheduled, stateful, verified control systems that prompt AI coding agents, instead of prompting them yourself. Repo description: *"Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost."*

Three load-bearing quotes it is built on (all in README + `resources/sources.md`):
- **Boris Cherny (Head of Claude Code, Anthropic):** *"I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops."* — with his community-shared usage `/loop 5m /babysit`, `/loop 30m /slack-feedback`, `/loop /post-merge-sweeper`; sources.md notes *"`/loop`, `/goal`, and `/schedule` as first-class primitives in Claude Code"* + related commentary from the Claude Code team *"including @_catwu"*.
- **Peter Steinberger:** *"You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."*
- **Addy Osmani:** *"Build the loop. But build it like someone who intends to stay the engineer, not just the person who presses go."*

## 2. Author + lineage (hand-verified)

**Cobus Greyling** — disclosed individual: Chief Evangelist at **Kore AI** (conversational-AI vendor), South Africa; prolific AI/NLP writer (cobusgreyling.medium.com, cobusgreyling.substack.com, X @CobusGreylingZA); 129 repos incl. the sibling **goal-engineering** ("loops discover, goals finish") and **fleet-engineering** — a serial "X-engineering" portfolio builder. **Not Anthropic** (verified: GitHub profile WebFetch + web research — no Anthropic affiliation anywhere).

**Concept lineage (June 2026, web-verified by workflow researchers; dates from fetched sources):** Peter Steinberger's viral framing post (2026-06-07, ~6.5M views reported) → **Addy Osmani's "Loop Engineering" essay** (addyosmani.com blog 2026-06-07 + Substack 2026-06-08, both fetched/VERIFIED) — `resources/sources.md` calls it *"the most complete written synthesis of the concept, including the five primitives + memory table"* and links *"the originating X thread"* (x.com/addyosmani/status/2064127981161959567) → **Boris Cherny / Anthropic** operationalizing loops in Claude Code (`/goal` shipped v2.1.139 2026-05-11 per research; `/loop`, `/schedule`). Precursors: ReAct (2022), Ralph overnight loops (2025). **This repo (first commit 2026-06-09, two days after the Osmani/Steinberger posts) is the practical codification layer** — `resources/sources.md`: *"We treat the above sources as the current best articulation of the idea and aim to turn the abstract framework into practical, copyable patterns, templates, and tool-specific guidance (with special attention to the Grok Build TUI, which has strong native support for the primitives)."*

⚠️ Corpus note: **Addy Osmani = corpus subject v184 (agent-skills)** — the v184 docs already recorded his "Loop Engineering" essay as philosophy. v189 now ships the codification of that essay: the corpus holds **both halves of Osmani's 2026 agent-engineering arc** (the skills half at v184, the loops half here). Cherny + Cat Wu are Pattern #19 Anthropic-team lineage nodes (claude-howto-era), not corpus subjects.

## 3. The concept model — Five Primitives + Memory, and the L0→L3 ladder

A loop = **schedule → triage skill → durable state → isolated worktree → implementer sub-agent → verifier sub-agent → MCP/git/tickets → human gate → commit-or-escalate → repeat** (README Mermaid). Harness vs loop: *a harness is a single session; a loop is harness + schedule + state + verification* (docs/concepts.md).

| Primitive | Job in the loop |
|---|---|
| **Automations / Scheduling** | "the heartbeat" — cron, `/loop`, GitHub Actions, `/goal` |
| **Worktrees** | safe parallel execution, one worktree per attempt |
| **Skills** | persistent project knowledge (SKILL.md) — *"without skills the loop re-derives everything from scratch on every run (intent debt)"* |
| **Plugins & Connectors (MCP)** | reach into real tools — least-privilege scopes |
| **Sub-agents** | **maker/checker split** — *"the single most important structural pattern for reliable loops. The agent that wrote the code is a terrible judge of its own work."* |
| **+ Memory/State** | durable spine outside any conversation (STATE.md / LOOP.md / run-log) |

**Graduated autonomy:** **L0 Draft** (intent only) → **L1 Report** (triage → state, NO auto-action) → **L2 Assisted** (small fixes + verifier) → **L3 Unattended**. *"Week one rule: report only. No auto-fix, no auto-merge. Read what the loop writes before you let it act."* (QUICKSTART).

## 4. The 7 patterns (machine-readable in `patterns/registry.yaml` + JSON-schema validated in CI)

| Pattern | Cadence | Week 1 | Token cost (registry cost-model) |
|---|---|---|---|
| Daily Triage | 1d–2h | L1 report | low (noop 5k / report 50k / action 200k; cap 100k/day) |
| PR Babysitter | 5–15m | L1 watch | high (noop 3k / report 80k / action 250k; cap 2M/day; `early_exit_required: true`) |
| CI Sweeper | 5–15m | L2 cautious | very high |
| Dependency Sweeper | 6h–1d | L2 patch-only | medium |
| Changelog Drafter | 1d/tag | L1 draft | low |
| Post-Merge Cleanup | 1d–6h | L1 off-peak | low |
| Issue Triage | 2h–1d | L1 propose-only | low |

Each pattern doc encodes: goal, cadence, risk, tools, skills, state file, phases, **human_gates** (e.g. security/payments/auth/max-fix-attempts), starter, week-one mode, and the per-run token cost model.

## 5. The tooling — "get a score"

- **loop-audit** (npm `@cobusgreyling/loop-audit`, v1.5.2): scores **Loop Readiness 0–100 → L0/L1/L2/L3** from **17 weighted file/behavior signals** (source-read `auditor.ts`): stateFile 18, triage 14, skills≥2 14, verifier 14, loopConfig 9, AGENTS.md 9, github 6, loopActivity 6, constraintsFile 4, safety 4+4, workflows 4, mcp 3, worktree 3, budgetDoc 3, runLog 3, registry 2… Thresholds **L1≥38 / L2≥58 / L3≥78**, and **L3 additionally hard-gates on verifier + cost observability (loop-budget.md + loop-run-log.md + LOOP.md budget section) + PROVEN loop activity** (git-log/STATE.md "Last run" evidence). Output: human/JSON/MD/**shields badge**; `--suggest` prints copy-commands from starters/templates. 12 unit tests.
- **goal-audit** (v1.0.2): the companion (goal-engineering) G0–G3 scorer for GOAL.md projects — 10 signals; only 2 tests (thin vs loop-audit).
- **loop-init** (v1.3.2): scaffolds a pattern per tool (`--tool grok|claude|codex|opencode`; falls back to Grok paths) — state + LOOP.md + skills + budget files, then prints your Loop Ready score.
- **loop-cost**: per-pattern token-spend estimator from the registry cost model.
- **loop-sync** (v1.0.0): **drift detection** between STATE.md ↔ LOOP.md ↔ skills ↔ starter configs.
- **loop-mcp-server** (repo v1, npm pending): a small read-only MCP lookup server exposing the pattern registry, LOOP.md, budget, run-log, safety docs, skills and state to agents at runtime.

## 6. Skills, templates, constraints (the copyable discipline)

4 root skills (mirrored 1:1 in `templates/`): **loop-verifier** (*"You are the checker in a maker/checker split… Default stance: REJECT until proven otherwise. Do not trust implementer's claim that tests passed — run them. If you cannot run tests → ESCALATE_HUMAN."* Output: APPROVE | REJECT | ESCALATE_HUMAN + evidence), **minimal-fix** (*"one specific problem with the smallest diff… never mark your own work done — the verifier decides"*; respect denylist paths), **loop-triage** (4-section output: High-Priority / Watch / Noise / State-Updates; *"signal, not invention"*), **loop-budget** (runs at start AND end of every iteration: **≥80% of daily cap → report-only mode; ≥100% or `loop-pause-all` → exit immediately**; appends a JSON run entry: run_id/pattern/duration_s/items_found/actions_taken/escalations/tokens_estimate/outcome). Plus **loop-constraints** — a binding plain-English guardrail file at project root (path denylists `.env`/auth/payments/secrets, never auto-merge to main, never disable tests, max 3 fix attempts then escalate) read + enforced before every action.

## 7. Dogfooding (real, commit-verified)

Root **LOOP.md**: *"It eats its own dogfood aggressively"* — 5 active loops on the repo itself. Root **STATE.md** live: *"Last run: 2026-07-01T10:58:40Z (automated daily-triage workflow)"*, readiness 100/L3. **loop-run-log.md: 15 real JSON entries (2026-06-11 → 2026-07-01) with GitHub Actions `workflow_run` IDs**; commit history shows `chore(loop): daily triage update STATE.md + run log [automated]` merged PRs. `daily-triage.yml` runs weekday 08:00 UTC, re-scores the repo, updates state, opens an auto-PR — and *"the loop cannot mark its own change green unless the real gates passed"* (workflow comment, verbatim). `audit.yml` posts the Loop Readiness score on every PR. → a genuine **Self-Referential-Methodology-Demonstration** (LV-C3 family).

## 8. Cross-harness mechanism

**7 patterns × 6 surfaces** = ~46 hand-translated examples (`examples/{grok,claude-code,codex,openclaw,opencode,github-actions}/`) + **16 starters** across 4 harnesses; the primitives-matrix maps 7 environments (Grok / **Claude Code** / Codex / OpenClaw / Opencode / Cursor / Windsurf). SKILL.md files are **byte-identical across Grok/Claude/Codex within a starter**; Opencode variants are hand translations (flat `skills/` + AGENTS.md + opencode.json). Claude Code is first-class: `.claude/skills/` + `.claude/agents/loop-verifier.md`, and the matrix's Claude column = `/loop`, scheduled tasks, cron, hooks, GitHub Actions. Drift gate: `scripts/check-loop-init-sync.mjs` fails CI if a registry pattern is missing from the loop-init CLI (uni-directional check, no generation). Grok gets first attention (default `--tool grok`, the essay's "Grok mapping").

## 9. Failure modes + anti-patterns (the transferable engineering wisdom)

**9 failure modes** (S1–S3): Infinite Fix Loop (hard cap 3 attempts), State Rot (prune every run), **Verifier Theater** (verifier too weak / same session as implementer), Notification Fatigue, Token Burn (early-exit), Over-Reach, Comprehension Debt, Cognitive Surrender, Parallel Collision (worktree isolation). **10 anti-patterns**: same agent verifies own work · no attempt cap · vague triage · L3 before L1 quality · shared state without schema · MCP write-everything scope · no kill switch · fixing flakes with code · auto-merge without allowlist · no run log.

**Stories** (honestly labeled): 2 canonical failures — **why-we-killed-ci-sweeper** (*"Honest failure story"*: `/loop 5m` on red main → **~8M tokens in 48h**, 11 PRs, 1 broke prod config; root causes: no L1 phase, verifier same session, no branch allowlist, no daily budget) and **multi-loop-collision** (two loops spawned conflicting fixes on PR 318 5 minutes apart, ~400k vs ~80k tokens; fix = branch lock + `acting_on` collision check in state). The dependency-sweeper story's verifier-parity lesson: verifier APPROVEd on cached `npm test` while CI's `npm ci` failed — *"Verifier must run the same install path as CI."* L1→L2 graduation criteria: 2 weeks L1, <20% noise, verifier proven manually first, denylist documented, loop-audit ≥58. ⚠️ The "week-one" stories are explicitly labeled *"Anonymized production-style narrative for contributors. Replace with your real metrics via PR"* — narratives/templates, NOT verified external adoption; the repo's own run-log + failure stories are the real data. Adopters list: 4 entries, all self-dogfood.

## 10. Safety + supply chain

Documented safety model: path denylists (secrets/.env/migrations/auth/payments; k8s/prod auto-escalate), auto-merge default NO (allowlist only), MCP least-privilege (github-readonly vs github-propose scoped configs; *"Sign all comments… Never auto-merge. Use draft PRs."*), human gates (security/PII/infra/deps/>10 files/3rd failed attempt), kill switch (`loop-pause-all`). SECURITY.md explicitly catalogs **unattended-automation risks**. **Supply chain BENIGN (source-verified):** zero postinstall across 8 package.json, zero curl|bash, zero network calls in tool source (static URLs only); npm publish via GitHub OIDC `--provenance`. The real risk is the domain itself — unattended loops burn tokens and merge code; the repo's own L1-first discipline IS the fence.

## 11. Honest caveats (doc-vs-code, verified)

- **Young:** first commit 2026-06-09 (~22 days at clone); adoption evidence = self-dogfood + labeled narratives.
- **The scorer measures scaffolding, not quality:** loop-audit's 17 signals are file-presence/regex heuristics (has STATE.md? has verifier skill? git log matches /triage|loop/i) — a well-scaffolded bad loop can score L2; L3's activity gate helps but is still heuristic.
- **README says "Cursor"** in the audience line, but there is **no Cursor starter** (matrix + examples cover it only descriptively).
- **ci-sweeper starter is missing its LOOP.md** (every other starter has one).
- **Root loop-budget.md diverges from its own template** (dogfood instance ≠ generic template — intended, but a reader can conflate them); run-log entries carry extra fields (readiness_score, workflow_run) beyond the documented JSON spec.
- `--suggest` recommendations reference starters/templates that are **not bundled in the npm packages** — you need the repo clone for them.
- npm package existence is badge- + git-tag-stated (npmjs blocked direct verification; 20+ local release tags corroborate).
- Cost numbers are **estimates/budgets, not metered API bills** (the repo says so itself).

## 12. Where it sits in the corpus (hand-verified positioning)

- **gh-aw v48** (`github/gh-aw`, T4 agentic-workflow compiler for GitHub Actions) = the **domain neighbor at the platform layer** — scheduled agentic workflows as a *product/compiler*; loop-engineering is the vendor-neutral **methodology + pattern + audit-kit layer** above any one scheduler. (No mention of gh-aw/Continuous-AI/ralph in the repo — grep-verified zero results.)
- **agent-skills v184** (Osmani) = session-internal SDLC discipline; loop-engineering = the **session-external control system** (schedule/state/budget/verifier around the sessions). Same author-lineage, different layer.
- **Paseo v150 / ai-maestro v163** (§C orchestration platforms) = interactive multi-agent hosting; this = unattended scheduled loops as METHODOLOGY.
- **ponytail v168** (code-minimalism ruleset) = sibling genre (behavior ruleset); minimal-fix's "smallest diff" overlaps in spirit.
- Observability sub-archetype (metering/run-state tools) = adjacent; loop-run-log/readiness-score is the *convention* those tools would consume.
- The vault itself: the LLM-Wiki routine + autopilot-research + `/loop` + scheduled tasks **already form L1/L2 loops** — see the Pilot Methods Menu.

**Full verdict + pattern outcome:** `(C) loop-engineering — Verdict.md`. **Apply-it menu:** `(C) loop-engineering — Pilot Methods Menu.md`.
