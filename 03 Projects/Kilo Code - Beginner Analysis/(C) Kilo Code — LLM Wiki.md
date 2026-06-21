# (C) Kilo Code — LLM Wiki (v177)

> **Subject:** [`Kilo-Org/kilocode`](https://github.com/Kilo-Org/kilocode) — an open-source AI **coding agent**.
> **Shipped:** 2026-06-21 · **Verdict:** GOAL-ALIGNED INCLUDE 3/4 [(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG] · **Tier:** T5 Agent-as-application (interactive-IDE flavor).
> **Pattern outcome:** 1 NEW §C standalone (CORPUS-FIRST, N=1) — *"Open-Source IDE-Embedded Multi-Model AI Coding-Agent Platform."* Counts UNCHANGED 46/10; §C surface ≈33 → ≈34.

---

## 1. What it is (one paragraph)

**Kilo Code is a full open-source AI coding agent** that runs as a **VS Code extension, a JetBrains plugin, a CLI, and a cloud surface** — *"the open source coding agent for building with AI in VS Code, JetBrains, or the CLI"* / *"an AI coding agent that meets you everywhere you work"* (README, verbatim). Its GitHub/marketing positioning is broader: *"the all-in-one agentic engineering platform … the most popular open source coding agent"* (repo description / kilo.ai — **stated, NOT in the README**). Unlike the bulk of the recent corpus — which is **tooling *around* coding agents** (observability, MCP servers, switchers, inspectors, capability layers) — **Kilo Code IS the coding agent itself**: it is the editor-embedded, interactive pair-programmer you drive to write, edit, plan, debug and review code, and it routes that work to whichever LLM you pick.

## 2. Lineage — the Cline → Roo Code → Kilo Code fork chain

This is the structurally important fact and it took **independent verification** (the README understates it):

- **Kilo Code = a fork of Roo Code, which was itself a fork of Cline.** Kilo *"forked both Cline and Roo,"* positioning as *"best of both worlds"* — Roo's multi-mode + customizability, Cline's stability + integration, plus its own *"zero barrier, extensible, smarter"* layer. *(high confidence — multiple independent secondary reviews: [adam.holter.com](https://adam.holter.com/kilo-code-the-hybrid-ai-coding-assistant-that-combines-cline-and-roo-code-for-cost-effective-development/), [ai505.com](https://ai505.com/kilo-code-vs-roo-code-vs-cline-the-2026-ai-coding-battle-nobody-saw-coming/), [addozhang/Medium](https://addozhang.medium.com/efficiency-on-a-budget-why-kilo-code-became-my-preferred-coding-agent-2bf2bfc6a61f))*
- **The Kilo CLI is a fork of OpenCode** — *"Kilo CLI is a fork of OpenCode, enhanced to work within the Kilo agentic engineering platform"* (README, verbatim).
- **Corpus relevance of the lineage:** Cline, Roo Code and OpenCode all appear in the corpus **only as landscape/comparison references** (OpenHands v30; the v167-era audit history; the multi-harness support-matrices) — **none has ever been a subject.** Kilo Code is the first member of this exact family to get its own wiki. *(This lineage is a landscape/code-heritage cross-reference, NOT a Pattern #57 corpus-recursive influence-citation — see §6.)*

## 3. Model economics — 500+ providers, mid-task switch, provider pricing

> *"You pick from 500+ models, switch between them mid-task, and pay the model provider's rate with zero markup. No API keys required to start."* (README, verbatim)

Named models in the repo overview: **GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, Gemini 3.1 Pro Preview** *(repo page, as of 2026-06)*. **Kilo runs Claude as a first-class backend** — this is why it is on-goal as a *Claude consumer/harness*, not merely a competitor. The "zero markup / no API keys to start" model is a **cost-economics** posture (Kilo AI fronts credits/routing) — adjacent to cluster LV-C2 (cost/capacity economics of cheap inference) and to the operator's **claude-api-cost-optimization** pilot thread.

## 4. Capabilities

- **Specialized modes** *(README, verbatim):* **Code** (default — implement/edit from NL) · **Plan** (architecture + implementation plan before code) · **Ask** (answer questions, no file edits) · **Debug** (troubleshoot/trace) · **Review** (surface issues across performance, security, style, test coverage).
- **Orchestrator mode** — breaks complex tasks into coordinated subtasks across **planner / coder / debugger** sub-agents *(secondary-stated; inherited from Roo's "Boomerang/Orchestrator")*. → directly on the operator's **multi-agent-orchestration** pilot thread.
- **Inline autocomplete** (ghost-text suggestions) — a differentiator vs Cline/Roo *(secondary-stated)*.
- **Terminal and browser control**; **autonomous mode for CI/CD pipelines**; **automated PR code review** *(repo overview)*.
- **MCP marketplace** — *"to find and wire up MCP servers that extend what the agent can do"* (README). This is the **consumer/host** side of MCP (discover + wire servers), NOT the one-server-many-clients distribution shape (Pattern #18 B1-MCP).

## 5. Verdict — GOAL-ALIGNED INCLUDE 3/4

| Criterion | Call | Why |
|---|---|---|
| **(a)** cultural-peer / Anthropic axis | **FAIL** | Kilo AI is a VC-funded commercial company (raised ~$8M, Dec 2025 — secondary-stated), **not Anthropic** ((a)-7 is Anthropic-only) and not the individual cultural-peer axis. Declared-non-Anthropic-institution — same situation as Google v140 / ByteDance v143 / NVIDIA v169 / OpenBMB v175. No heritage rescue; a **#19 19a** institutional data-point only. |
| **(b)** goal-relevance *(tier-keying)* | **STRONG** | Kilo Code **IS** an open-source autonomous AI coding agent for software development = dead-center on Goal #1. It **runs Claude** (Opus 4.7 / Sonnet 4.6) as a backend → a Claude consumer/harness and the direct **open-source peer to Claude Code's editor integrations**. Orchestrator mode → multi-agent-orchestration thread; provider economics → cost-optimization thread; MCP marketplace native. **STRONG-not-STRONGEST:** it is a *competitor/peer* harness (third-party, not Claude/Anthropic substrate) and Goal #1 centers Claude specifically. ⚠️ Contrast **GLM-5 v176** (b) MODERATE — that was a *raw model* ("nothing to pilot but swap the backend"); Kilo Code is the full **agent you install and use**, exactly the *kind of thing* the goal names → (b) is a tier stronger here. |
| **(c)** engineering substance | **STRONG** | TS 83.6% / Kotlin 12.0% / CSS 3.5%; VS Code + JetBrains + CLI + cloud; **434 releases**, latest **v7.3.50**; 5 specialized modes + Orchestrator; inline autocomplete; terminal/browser control; MCP marketplace; 500+ provider aggregation with mid-task switching; autonomous/CI mode + PR review. Mature, large, multi-platform. **Honest caveat:** much of the foundation is **inherited code** from the Roo/Cline/OpenCode forks. |
| **(d)** cross-references | **STRONG** | OpenHands v30 (T5 SWE-agent) / AutoGPT (autonomous agents) / DeepSeek-TUI v72 (coding client); cc-switch v73 + ai-switcher v153 (Kilo bakes provider-switching in); Pattern #18 #8 Multi-Source-LLM-aggregator (500+ providers); the **multi-harness support-matrices that already name Kilo Code** (ui-ux-pro-max v85, agentmemory v66, codebase-memory-mcp v172, OpenSpec); GLM-5 v176 (a backend it can run); LV-C2 economics; the multi-agent-orchestration + cost-optimization pilot threads. |

**§31 keys the tier on (b), not (a)** → (b) STRONG ⇒ **GOAL-ALIGNED INCLUDE**. Shape matches v171–v175.

## 6. Pattern outcome — 1 NEW §C standalone (CORPUS-FIRST, N=1)

**MINT:** *"Open-Source IDE-Embedded Multi-Model AI Coding-Agent Platform (interactive VS Code / JetBrains extension + CLI, multi-provider mid-task-switchable at provider pricing, specialized modes + orchestrator, MCP marketplace) — the Cline / Roo-Code / Cursor peer class."* (N=1)

**Why a mint, not instance-strengthening:** the corpus has analyzed ~177 subjects, overwhelmingly **tooling-around-agents**, and has **never** taken an **editor-embedded interactive coding-agent product** (the Cline / Cursor / Roo / Windsurf / Copilot category) as a primary subject. That category is large and clearly recurring in the world; Kilo Code is the corpus's first member. Minting one §C standalone at N=1 (≤2 cap honored) credits a real, recurring, on-goal capability class — the same discipline used at v169/v171/v173/v174/v175.

**DISTINCT from:**
- **OpenHands v30** (T5 autonomous **SWE-agent platform** — sandboxed/batch/SDK/cloud; *not* editor-embedded-interactive). Same tier, different product shape: autonomous-SWE vs interactive-IDE pair-programmer.
- **AutoGPT** (general autonomous agent, not coding-IDE-embedded).
- **DeepSeek-TUI v72** (terminal client, single-vendor — not a multi-model IDE platform).
- **The entire tooling-AROUND-agents surface:** cc-switch v73 / devspace v171 / claude-tap v173 / codebase-memory-mcp v172 / Agent-Reach v174 (augment/bridge/inspect/feed an agent) — Kilo Code *is* the agent.
- **PilotDeck v175** (self-contained agent OS — desktop-task-productivity, organized around per-project WorkSpaces; not an IDE-embedded coding agent).
- **GLM-5 v176** (a raw *model* — the engine; Kilo Code is the *harness* that runs such engines).

**SECONDARY (recorded, NOT minted):**
1. **Cited-to-Subject Elevation** (§C N=2: v93 anthropics/skills + v135 open-slide) → Kilo Code is a strong candidate **N=3** and adds a **third sub-flavor**: *cited-as-supported-harness*. It appeared in the corpus only as a supported-harness/distribution-target **name** — in ui-ux-pro-max-skill v85's 18-harness matrix, agentmemory v66, codebase-memory-mcp v172's 11-agent auto-config, and OpenSpec's 30+-tool list — and is now elevated to its own wiki. **Promotion DEFERRED to the next audit** (one-class-vs-sub-flavors is an audit question; do not self-promote at ship, per the §28 / v162 "don't generalize-to-fit" discipline).
2. **Pattern #18 #8 Multi-Source-LLM-Aggregator** — 500+ providers with mid-task switching = an aggregator instance **at the agent-product layer** (the agent itself aggregates, vs cc-switch's external switcher). Scoped cross-ref; N-bookkeeping is an audit item, not asserted here.
3. **LV-C2 cost economics** — "provider rate, zero markup, no API keys to start" = a free/cheap-inference economics data-point (Kilo AI fronts credits/routing — the relay-adjacent economy).
4. **#19 19a** — first **Kilo AI / Kilo-Org** subject (commercial VC-funded org).
5. **#66** supply-chain/security cross-ref — a VS Code extension with terminal/browser control + autonomous mode = a real install attack-surface → pilot fence (§7).
6. **Multi-agent-orchestration** — Orchestrator mode (planner/coder/debugger) is an *in-agent* orchestration feature → operator pilot thread.

**NON-claims:**
- **NOT a new top-level pattern** (max stays #85).
- **NOT #52** — 23.6k★ / 2.8k forks / 434 releases / v7.3.50 are **page-stated, NOT API-verified** (§37.4) → viral-velocity unestablishable.
- **NOT #57** — forking OpenCode + descending from Roo/Cline is **code-lineage to landscape references**, not citation of corpus *subjects* as influences (mentions/lineage ≠ corpus-recursion; the v172/v173/v174 discipline).
- **NOT #18 B1-MCP** — it *consumes* an MCP marketplace (host side); it is not a single MCP server distributed to many clients.

**Tier: T5 Agent-as-application** (the interactive-IDE flavor) — consistent with OpenHands v30 (T5 autonomous-SWE flavor).

## 7. Pilot note

Highly pilotable in principle (install the VS Code extension or CLI, point it at Claude) and **on two pilot threads at once** — multi-agent-orchestration (Orchestrator mode) and claude-api-cost-optimization (500+ models / provider pricing). But it is the **heaviest agent-as-application** candidate: a full IDE extension with terminal/browser control + autonomous mode, and piloting it means evaluating a **competitor harness** against the vault's existing Claude Code workflow (a comparison/cost play, not a replacement). **Fence:** install-snapshot the extension/CLI · scratch project first · review any MCP-marketplace servers before wiring · pin **v7.3.50**. **Ranking:** below the lightweight read-only pilots (SkillSpector v169 first; claude-tap v173 second). PILOT lever still stands (zero piloted).

## 8. §37 provenance

- Tagline / modes / model-economics quotes — **stated** (README, github.com/Kilo-Org/kilocode, as of 2026-06).
- "most popular open source coding agent" / "all-in-one agentic engineering platform" — **stated** (GitHub repo description / kilo.ai marketing; **NOT in the README**).
- Roo Code/Cline fork lineage; Orchestrator mode; inline-autocomplete differentiator; ~$8M Dec-2025 funding — **high / medium** (multiple independent secondary reviews; not in the repo README).
- TS 83.6% / Kotlin 12.0% / CSS 3.5%; **license MIT** — **stated** (repo page). ⚠️ **Discrepancy flagged:** one secondary review states **Apache-2.0** (the Roo/Cline heritage license). Repo-page is authoritative; **unreconciled — verify the LICENSE file before relying on the SPDX.**
- 23.6k★ / 2.8k forks / 434 releases / v7.3.50 (2026-06-19) — **page-stated, NOT API-verified** (§37.4; this environment mocks the GitHub API) → **NOT a #52 claim.**

## 9. Sources

- Repo: https://github.com/Kilo-Org/kilocode · README: https://github.com/Kilo-Org/kilocode/blob/main/README.md · site: https://kilo.ai/
- Lineage/funding (secondary): [adam.holter.com](https://adam.holter.com/kilo-code-the-hybrid-ai-coding-assistant-that-combines-cline-and-roo-code-for-cost-effective-development/) · [ai505.com](https://ai505.com/kilo-code-vs-roo-code-vs-cline-the-2026-ai-coding-battle-nobody-saw-coming/) · [addozhang/Medium](https://addozhang.medium.com/efficiency-on-a-budget-why-kilo-code-became-my-preferred-coding-agent-2bf2bfc6a61f) · [apidog.com](https://apidog.com/blog/kilo-code/) · [vibecoding.app](https://vibecoding.app/blog/kilo-code-review)
