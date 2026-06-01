# harness — Wiki (v131)

> `revfactory/harness` · **"Harness — The Team-Architecture Factory for Claude Code"** · **"A meta-skill that designs domain-specific agent teams, defines specialized agents, and generates the skills they use."** · A Claude Code plugin that turns a one-sentence domain description into a coordinated multi-agent team (`.claude/agents/`) + the skills they use (`.claude/skills/`) + an orchestrator, picked from **six team-architecture patterns**.

**(C) Claude-generated wiki page.** Fetched 2026-06-01 (GitHub API + README + recursive tree + SKILL.md + 6 reference guides + a `_workspace/` artifact). Routine **v2.6, wiki #131** — the **first ship under v2.6** (§35 soft off-goal-rate ceiling). Phase 0.9: **GOAL-ALIGNED INCLUDE (3/4 STRONG)** — (a) WEAK/geographic, (b) **STRONG**, (c) STRONG, (d) STRONG. **This satisfies the breached §35 ceiling legitimately (a genuine goal-aligned ship), no ceiling-override used.**

---

## Identity

| Field | Value |
|---|---|
| Repo | [`revfactory/harness`](https://github.com/revfactory/harness) |
| What | **Claude Code plugin / meta-skill** — a "Team-Architecture Factory": domain sentence → an **agent team** (`.claude/agents/`) + the **skills** they use (`.claude/skills/`) + an orchestrator, via 6 team patterns |
| Tier / archetype | **T1 Assistant Skill / Claude-Code-Plugin (single meta-skill)** + **agentskills.io SKILL.md implementer** + Claude Code plugin marketplace (own `marketplace.json`) + **CORPUS-FIRST "Agent-Team-Architecture Factory" sub-archetype** (a skill that *generates* a multi-agent team) |
| Stars / forks | **4,851★ / 666 forks** (fork_ratio **0.137**) |
| Open issues | 0 |
| Created / pushed | 2026-03-26 / 2026-05-29 (**~67 days**, active) |
| Velocity | **~72 stars/day → Pattern #52 SUSTAINED-MODERATE-HIGH** (25–150/d band, sustained 67d; just under the 90d "multi-month" threshold) |
| License | **Apache-2.0** (LICENSE + GitHub API agree; each plugin.json `license: Apache-2.0`) |
| Language | **HTML 100%** = the GitHub Pages landing site (`index.html` + `privacy.html`); the **actual content is Markdown** (SKILL.md + 6 reference guides) |
| Distribution | Claude Code `/plugin marketplace add revfactory/harness` → `/plugin install harness@harness-marketplace`; or direct `cp -r skills/harness ~/.claude/skills/harness` |
| Default branch / homepage | `main` / [revfactory.github.io/harness](https://revfactory.github.io/harness/) |
| Topics | claude-code, claude-code-plugin, harness, harness-engineering |
| i18n | Trilingual README: **English + 한국어 + 日本語**; SKILL.md body is **Korean-primary** |
| Author | **Minho Hwang** (`revfactory`, `owner.type: User`; plugin.json author "robin"; revfactory@gmail.com) — **South Korea, @kakao**. Account 2012 (~13y), 278 repos, 528 followers. |
| Version | **v1.2.0** (plugin.json + README badge; `latestRelease: null` — no GitHub Releases) |
| Requires | Claude Code **experimental Agent Teams** (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) |

## What it is

A Claude Code **meta-skill**: say *"build a harness for this project"* (or 하네스 구성해줘 / ハーネスを構成して) and it analyses your domain, designs an agent team, and **generates the agent definitions + skills + orchestrator** for you. The author frames it as an **"L3 Meta-Factory / Team-Architecture Factory"** — the layer that *generates* harnesses rather than being one.

**The skill is a single `skills/harness/SKILL.md` (Korean-primary) running an 8-phase workflow:**
- **Phase 0 — Audit:** read existing `.claude/agents/`, `.claude/skills/`, `CLAUDE.md`; branch to new-build / extend / operate-maintain; detect drift.
- **Phase 1 — Domain analysis** (incl. *user-skill detection* to tune communication).
- **Phase 2 — Team architecture:** pick execution mode (Agent Teams / Subagents / Hybrid) + one of 6 patterns + agent-separation criteria.
- **Phase 3 — Agent definitions:** every agent gets a `.claude/agents/{name}.md` file (mandatory, even for built-in types), with team-communication protocol; `model: "opus"` enforced.
- **Phase 4 — Skill generation:** `.claude/skills/{name}/SKILL.md` with **Progressive Disclosure** (metadata ~100 words / SKILL.md <500 lines / references unlimited) + "pushy" trigger descriptions.
- **Phase 5 — Integration & orchestration:** an orchestrator skill ties the team together; data-passing protocol (message / task / file / return-value); `_workspace/{phase}_{agent}_{artifact}` file convention; registers a minimal **harness pointer in `CLAUDE.md`** (trigger rule + change-log only).
- **Phase 6 — Validation & testing:** structure check + **with-skill vs without-skill A/B** + should-trigger / should-NOT-trigger ("near-miss") verification + dry-run.
- **Phase 7 — Evolution:** post-run feedback → updates agents/skills/CLAUDE.md; a harness is "an evolving system, not a fixed artifact."

**Six team-architecture patterns** (each with explicit "team-mode suitability"): **Pipeline** (sequential), **Fan-out/Fan-in** (parallel + integrate — "must use Agent Teams"), **Expert Pool** (router → selective expert), **Producer-Reviewer** (generate → review → retry, max 2–3), **Supervisor** (central dynamic task distribution), **Hierarchical Delegation** (recursive, ≤2 levels recommended).

**Two execution modes + hybrid:** **Agent Teams** (default — `TeamCreate` + `SendMessage` + `TaskCreate`, peers self-coordinate) vs **Subagents** (`Agent` tool, `run_in_background`, results to main only) vs **Hybrid** (per-phase mix).

**Six reference guides** (the instructive payload): `agent-design-patterns.md` (6 patterns + mode decision tree + separation/reuse criteria), `team-examples.md` (5 *complete* worked teams incl. full agent `.md` bodies), `orchestrator-template.md`, `qa-agent-guide.md` (incremental QA + boundary-bug patterns, "based on 7 real bugs"), `skill-writing-guide.md`, `skill-testing-guide.md`.

**It dogfoods itself:** `_workspace/` holds artifacts following harness's own `{phase}_{agent}_{artifact}` convention — `01_auditor_repo_audit.md` (a "GitHub Trending Readiness Audit" of the harness repo *itself*), `02_content_launch_contents.md`, `03_scout_outreach_map.md`, `04_strategist_launch_plan.md` — i.e. a harness-generated auditor/content/scout/strategist team applied to harness's own launch.

**Sister repos:** [`harness-100`](https://github.com/revfactory/harness-100) (100 production harnesses × 10 domains, EN+KO = 200 packages, 1,808 markdown files — all generated by this plugin) and [`claude-code-harness`](https://github.com/revfactory/claude-code-harness) (an A/B research repo: **+60% avg quality (49.5→79.3), 15/15 win-rate, −32% variance**, with the honest disclosure "n=15, author-measured, third-party replications pending"). ⚠️ Note: `revfactory/claude-code-harness` is a *different* repo from corpus **v107 `claude-code-harness`** (Chachamaru, Japan — Enforced-Gate Operating-Loop); same name, unrelated authors.

## Why it's in the corpus

**GOAL-ALIGNED INCLUDE** (v2.5 §31 tier — (b) PASSes, so this is the corpus's core, not an off-goal capture). **It satisfies the breached §35 ceiling legitimately** (v127/v128/v129 were all off-goal; §35 mandated the next ship be goal-aligned — harness is, on its own merits, no ceiling-override needed):

- **(a) WEAK / geographic PASS** — Minho Hwang is **South-Korea-located** (@kakao). That's an Asian-LOCATED (a)-6 geographic PASS and **likely the first South-Korea-located subject in the corpus** (flag to verify at audit). But he's a **big-company engineer, not a solo VN/indie cultural-peer** — so this is a geographic-cluster PASS, *not* a structural-peer PASS, and it is **not load-bearing** for the verdict.
- **(b) STRONG** — a Claude Code meta-skill that **generates multi-agent teams + their skills** is dead-center on goal #1 ("master Claude and autonomous agents **for software development**"), and **doubly relevant to Storm Bear as a Scrum coach**: the 6 patterns + team-size guidance ("3 focused members beat 5 scattered") + Producer-Reviewer/Supervisor/Hierarchical-Delegation + feedback-and-evolution loop are literally *team-process design*. MINIMUM-cost reversible install × DIRECT relevance. **Not STRONGEST** because (i) it requires the **experimental** Agent Teams flag (gated, may change) and (ii) the SKILL.md body is **Korean-primary** (usable but a friction), and it's a *scaffold generator* run occasionally, not a daily-use tool.
- **(c) STRONG** — genuinely instructive: 6 named orchestration patterns each with when-to-use / example / caveat / team-mode-suitability; a teams-vs-subagents decision tree; **5 complete worked team examples with full agent `.md` file bodies**; a Progressive-Disclosure skill-authoring doctrine; a skill-testing methodology (with-skill vs without-skill A/B; should/should-NOT-trigger); a QA-agent guide built on 7 real boundary bugs.
- **(d) STRONG** — high connectivity: agentskills.io SKILL.md chain + Claude Code plugin marketplace (v95 / v126 siblings); multi-agent-orchestration siblings v126 compound-engineering (51 agents), v94 Understand-Anything (7-agent pipeline), v99 cmux (13-agent multiplexer), v95 skill-creator; **explicitly cites corpus-anchor ECC (`affaan-m/everything-claude-code` = v1/v78)** as its "L2 cross-harness workflow" neighbor = Pattern #57 corpus-recursive thread; Progressive-Disclosure doctrine → v93 anthropics/skills + v76 agent-skills-standard; trilingual i18n cluster.

## Pattern Library contribution (summary)

- **PRIMARY — NEW T1 sub-archetype "Agent-Team-Architecture Factory" (PROVISIONAL N=1, CORPUS-FIRST):** a meta-skill whose **output is a coordinated multi-agent team** — agent definitions + their skills + an orchestrator + a `CLAUDE.md` pointer — synthesised from a domain sentence via named team-coordination patterns. Distinct from prior corpus subjects: **skill-creator** (v95) generates *single skills*; **compound-engineering** (v126) *ships a fixed* 37-skill/51-agent team as its product; **Understand-Anything** (v94) *runs* a fixed pipeline. harness *generates a bespoke team per domain*. The author's own "L3 Meta-Factory / Team-Architecture Factory" framing names the layer. **N=1 honestly** — promotion-eligible at N=2 (the README names non-corpus neighbors Archon / meta-harness / harness-init / OpenRig in the same layer; a 2nd corpus instance would cluster it). *Lives at the tier-sub-archetype layer; NOT a Library-vocab standalone.*
- **SECONDARY (cluster strengthening / observations — §28 disciplined):**
  - **LV-C3 "Self-Referential-Methodology-Demonstration" → N=3** (v87 + v126 + **v131**): harness's `_workspace/` holds auditor/content/scout/strategist artifacts that audit + plan harness's *own* launch, following harness's *own* output convention = a self-application of the factory. **N=3 makes it promotion-eligible** (promotion-to-CONFIRMED is a next-audit act). **Honest caveat:** the `_workspace/` files are *not explicitly stamped* "generated by harness" — the evidence is structural (naming-convention match + self-as-subject), so this is a soft 3rd instance. *Filed to registry LV-C3.*
  - **agentskills.io SKILL.md chain → another implementer** (single meta-skill SKILL.md + own plugin marketplace). CONFIRMED N=3 unchanged — administrative; **exact implementer-count flagged for audit reconciliation** (v115 noted the running count has been mislabeled; was ~13–14 by v126).
  - **Pattern #82 quantitative-marketing + Pattern #83 honest-deficiency-disclosure** — the sister-repo "+60% / 15-15 / −32%" claim, paired *in the same sentence* with "n=15, author-measured, replications pending" + a FAQ Q1 "Isn't +60% oversold?" = a clean honest-disclosure specimen.
  - **Pattern #84 — negative evidence:** deliberately **single-harness** ("Claude-Code-native, deep" over "multi-runtime, shallow"; points Codex users to the SaehwanPark/meta-harness port). A counter-instance to the multi-harness norm (cf. v84 image-blaster's 1-harness).
  - **Pattern #57 corpus-recursive:** the Coexistence table cites **ECC (v1/v78)** as a neighbor layer.
  - **Library-vocab #12 routing artifacts** N+1 (CLAUDE.md harness-pointer + AGENTS-style SKILL.md + plugin.json/marketplace.json).
- **Honest non-claims:** **(b) is STRONG, not STRONGEST** (experimental-flag dependency + Korean-primary skill body) — not inflated to clear the ceiling; **ZERO new Library-vocab standalones** (§28 — only the LV-C3 N=3 strengthening filed); the NEW sub-archetype is **N=1** (not a cluster); the LV-C3 3rd instance carries a **no-explicit-stamp caveat**; **NOT identical to v107 claude-code-harness** (same-name, different repo/author); **NO Pattern Library state change at ship** (46 confirmed / 8 Library-vocab CONFIRMED unchanged).

## Pilot

**Goal-aligned, but a CONDITIONAL / fenced pilot — not Tier-1-unconditional.** harness is directly on goal #1 and in your Scrum wheelhouse, but it **requires the experimental Agent Teams flag** (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) and its skill body is Korean-primary. Recommended path **if** you want to try it: `install-snapshot` first → `/plugin marketplace add revfactory/harness` → `/plugin install harness@harness-marketplace` → enable the flag → on a **scratch** project run *"build a harness for code review"* and inspect the generated `.claude/agents/` + orchestrator + the with-skill/without-skill test. Fully reversible (`/plugin uninstall` + delete `~/.claude/skills/harness`). **Highest-value read even without installing:** `skills/harness/references/agent-design-patterns.md` + `team-examples.md` — a compact, genuinely good reference on multi-agent orchestration you can apply by hand (and a model for authoring your own team skills). **Note:** the still-un-piloted **v126 compound-engineering** remains the more turnkey goal-#1 pilot (no experimental flag, English-primary); harness is the *generator/architecture-study* complement to it.

---

*See `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` and `01 Analysis/(C) Pattern-Library-Phase-4b-T1-Agent-Team-Architecture-Factory-N1.md`.*
