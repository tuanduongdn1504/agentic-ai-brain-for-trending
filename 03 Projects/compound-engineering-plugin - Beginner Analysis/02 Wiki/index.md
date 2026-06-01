# compound-engineering-plugin — Wiki (v126)

> `EveryInc/compound-engineering-plugin` · **"Official Compound Engineering plugin for Claude Code, Codex, Cursor, and more"** · **"AI skills and agents that make each unit of engineering work easier than the last."** · A multi-harness agent plugin codifying Every's **Compound Engineering** methodology — a Brainstorm → Plan → Execute → Review → Compound workflow, installable into Claude Code (+ 8 other harnesses) as 37 skills / 51 agents.

**(C) Claude-generated wiki page.** Fetched 2026-06-01 (GitHub API + README + recursive tree). Routine **v2.5, wiki #126** — the **FIRST ship under v2.5**, so it carries the new §33 tier-tag. Phase 0.9: **GOAL-ALIGNED INCLUDE** — (a) FAIL (US media/tech org), (b) **STRONGEST**, (c)(d) STRONG. **First GOAL-ALIGNED INCLUDE under v2.5** and the most directly goal-#1-actionable subject in the recent corpus = **Tier-1 pilot**.

---

## Identity

| Field | Value |
|---|---|
| Repo | [`EveryInc/compound-engineering-plugin`](https://github.com/EveryInc/compound-engineering-plugin) |
| What | **Multi-harness agent plugin** codifying the **Compound Engineering** methodology (Brainstorm→Plan→Execute→Review→Compound); 37 skills + 51 agents (compound-engineering plugin) |
| Tier / archetype | **T1 Assistant Skill / Claude-Code-Plugin Marketplace** (multi-plugin: `compound-engineering` + `coding-tutor`) + **agentskills.io 57k implementer** (44 SKILL.md in-repo) + methodology-influence node |
| Stars / forks | **18,810★ / 1,415 forks** (fork_ratio **0.075**) |
| Subscribers / open issues | 103 / 85 |
| Created / pushed | 2025-10-09 / 2026-06-01 (**~235 days**, pushed today — very active) |
| Velocity | **~80 stars/day → Pattern #52 SUSTAINED-MODERATE-HIGH** (25–150/d band, sustained 235d) |
| License | **MIT** (GitHub API `mit`) |
| Language | **TypeScript** (the converter/build tooling; the skills/agents are Markdown) |
| Distribution | Claude Code `/plugin marketplace add EveryInc/compound-engineering-plugin` → `/plugin install compound-engineering`; + Cursor / Codex / Copilot (VS Code + CLI) / Factory Droid / Qwen Code / OpenCode·Pi·Gemini·Kiro (via the `bunx @every-env/compound-plugin install … --to [target]` converter) |
| Default branch / homepage | `main` / [every.to/guides/compound-engineering](https://every.to/guides/compound-engineering) |
| Topics | compound, engineering |
| Author | **Every** (`EveryInc`, `owner.type: Organization`; every.to; US media/software co — Dan Shipper) — credits **Kieran Klaassen, Dan Shipper, Every**. Org 2020, 39 repos, 760 followers. |

## What it is

An installable, multi-harness agent plugin that codifies **Compound Engineering** — Every's named methodology, **"each unit of engineering work should make subsequent units easier—not harder."** It inverts the usual ratio: **~80% planning/review, ~20% execution**, with explicit knowledge-codification so each cycle improves the next ("brainstorms sharpen plans, plans inform future plans, reviews catch more issues").

**Core loop:** `Brainstorm → Plan → Execute → Review → Compound → [repeat with better context]`, anchored upstream by a product `STRATEGY.md`.

**Primary slash commands (the `/ce-*` suite):**
- `/ce-strategy` — maintain `STRATEGY.md` (product anchor) · `/ce-ideate` — ranked idea generation · `/ce-brainstorm` — interactive requirements · `/ce-plan` — implementation planning · `/ce-work` — execution + task tracking · `/ce-debug` — systematic failure diagnosis · `/ce-code-review` — **multi-agent code review** · `/ce-compound` — learning/knowledge documentation · `/ce-product-pulse` — time-windowed usage/perf reports · `/ce-setup` — cross-platform bootstrap.

**Scale:** README states **37 skills + 51 agents** for the compound-engineering plugin; the repo carries **44 `SKILL.md`** total (incl. a 2nd bundled plugin, `coding-tutor`, + test fixtures), **46 agent `.md`**, 12 commands. Per-harness manifests (`.claude-plugin/` + `.codex-plugin/` + `.cursor-plugin/` `plugin.json`) + three marketplace manifests = a **Claude Code plugin marketplace** (v95 sibling) that is also genuinely cross-harness.

**It dogfoods its own methodology:** the repo ships `docs/brainstorms/*` and `docs/plans/*` — the actual brainstorm + plan artifacts for its *own* features (e.g. `2026-03-26-001-feat-adversarial-review-agents-plan.md`), produced by running `/ce-brainstorm → /ce-plan` on itself.

## Why it's in the corpus

**GOAL-ALIGNED INCLUDE** (v2.5 §31 tier — (b) PASSes, so this is the corpus's core, not an off-goal capture):
- **(a) FAIL** — Every is a **US media/software company** (Dan Shipper, NYC). Not a VN/Asian cultural-peer; not (a)-7 (Every is a methodology *publisher*, not a vault-substrate foundational vendor like Anthropic). Honest FAIL.
- **(b) STRONGEST** — this is *the* intersection of goal #1 ("master Claude and autonomous agents **for software development**") **and** Storm Bear's Scrum-coaching domain: it is an agent-assisted **software-engineering process/workflow** plugin. MINIMUM cost (reversible Claude Code plugin install), DIRECT relevance, HIGH applicability (usable on real projects). The most directly goal-actionable subject in the recent corpus.
- **(c) STRONG** — exemplary: a full methodology codified as 37 skills + 51 agents with a clear staged workflow, multi-agent review, and an external published guide (every.to). Self-dogfooded.
- **(d) STRONG** — high connectivity: agentskills.io 57k chain (13th implementer); Claude Code plugin marketplace (v95 sibling); Pattern #84 multi-harness + converter; Pattern #80 adversarial multi-agent review; agentmemory v66 (auto-memory-integration); Library-vocab #12 routing artifacts; conceptual adjacency to the vault's own compounding-knowledge premise (Karpathy LLM-wiki, Pattern 1).

## Pattern Library contribution (summary)

- **PRIMARY: LV-C1 "Vendor-Official Agent-Tooling for Own Product/Offering" → N=2** (v114 gsap-skills [software-library vendor] + **v126 compound-engineering** [methodology/editorial vendor — Every ships the executable form of its own published methodology]). Strengthens v114's CORPUS-FIRST item; **promotion-eligible at N=3**. Honest sub-distinction noted (library-vendor vs methodology/editorial-vendor) — watch whether it diverges into two sub-types. *Filed to registry LV-C1.*
- **SECONDARY (administrative / strengthening, no new mint — §28):**
  - **agentskills.io 57k chain → 13th implementer** (44 SKILL.md; after v124's 12th). CONFIRMED N=3 unchanged — administrative count.
  - **Pattern #84 cross-vendor ecosystem-tolerance + 84c provider-agnostic-by-design + "CLI-generates-native-formats-from-canonical-source" (v76 sub-mechanism) N+1** — Claude + Codex + Cursor manifests + the `@every-env/compound-plugin` converter targeting 8+ harnesses.
  - **Claude Code plugin marketplace** → v95 claude-plugins-official sibling (multi-plugin marketplace.json).
  - **Pattern #80 Tool-Level Adversarial Review** — `/ce-code-review` multi-agent + in-repo `adversarial-review-agents` plan; the corpus's own adversarial-verify methodology, productized.
  - **LV-C3 "Self-Referential-Methodology-Demonstration" → N=2** (v87 + v126's in-repo `docs/brainstorms/` + `docs/plans/` dogfooding the loop). *Filed to registry LV-C3.*
  - **Pattern #52 SUSTAINED-MODERATE-HIGH N+1** (~80/d × 235d); **Library-vocab #12** routing artifacts (AGENTS.md + CLAUDE.md + .claude-plugin/ + .agents/ + .cursor-plugin/); **agentmemory v66 / Pattern #85** (auto-memory-integration); **Pattern #82** quantitative-marketing (80/20; 37 skills / 51 agents).
- **Honest non-claims:** **(a) FAILS** (US org — not laundered); **NO new top-level Pattern; ZERO new Library-vocab standalones** (the value is a strong goal-aligned pilot + two N=2 strengthenings, not a novel mint — §28 disciplined, mirrors v119/v124); **NOT a 3rd instance of Pattern #57 corpus-recursive-at-methodology-influence** — "compound engineering" shares the *compounding* theme with the vault's Karpathy-LLM-wiki premise but is a *different* methodology (compounding engineering work, not a knowledge-wiki); noted as conceptual adjacency only, **not** claimed as v94/v118's pattern. **NO Pattern Library state change at ship** (46 confirmed / 8 Library-vocab CONFIRMED unchanged).

## Pilot

**Tier-1 pilot — YES, the actual goal-#1 move.** This is the directly-installable, directly-on-goal subject the last several ships + two audits kept pointing at. Recommended: `install-snapshot` first (it's large — 44 skills / 46 agents), then `/plugin marketplace add EveryInc/compound-engineering-plugin` → `/plugin install compound-engineering` on a scratch or real software project; run one `/ce-brainstorm → /ce-plan → /ce-work → /ce-code-review → /ce-compound` loop. Doubly relevant for a Scrum coach (it's an agentic dev *process*). Fully reversible (`/plugin uninstall`).

---

*See `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` and `01 Analysis/(C) Pattern-Library-Phase-4b-LV-C1-Vendor-Official-Tooling-N2.md`.*
