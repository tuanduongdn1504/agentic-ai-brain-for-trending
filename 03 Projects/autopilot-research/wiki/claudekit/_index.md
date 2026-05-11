# claudekit

> **Source:** [vividkit.dev](https://www.vividkit.dev/vi/guides/what-is-claudekit) (Vietnamese documentation, 21 guides)
> **Compiled:** 2026-05-11
> **Bypass needed:** None — Tier 0 fetch direct
> **Why this topic exists:** evaluate ClaudeKit as adoption/inspiration candidate for personal harness improvement; compare with Lopopolo's [[external|harness-engineering/_index|harness engineering]] and Mnilax's [[external|claude-md-12-rules/_index|12 rules]]

ClaudeKit is a **framework that sits on top of Claude Code's `.claude/` configuration** — agents, skills, workflows, hooks as 4 pillars. It transforms Claude Code from interactive chatbot into structured automation system. CLI-first, portable (migrates to Cursor/Windsurf/Codex), multi-provider (CCS switches between Claude/GLM/Kimi/GPT runtimes).

## Articles

- [[architecture-overview]] — 4 pillars (agents/skills/workflows/hooks) + integration layer + runtime layer (CCS) + compatibility layer (migrate)
- [[command-reference]] — full `/ck:*` command table, 50+ commands across 10 categories (basics / planning / execution / UI / testing / security / git / docs / project / utilities)
- [[request-lifecycle]] — how a request flows through ClaudeKit: initiation → hooks → agent pipeline → output gates
- [[setup-and-coexistence]] — install (npm/bun), permission modes (auto / bypass / custom), hook orchestration, IDE config, coexistence with existing setups, migration paths
- [[failure-modes-and-recovery]] — common failures (rate limits, context bloat >100K, circular logic, session timeouts), `/ck:fix` 6-phase debugging pipeline, what state CAN/CANNOT be recovered
- [[gaps-and-niche]] — what ClaudeKit explicitly does NOT solve (model provisioning, hard enforcement, quota generation, infinite context); niche vs Raw Claude Code / Codex CLI / Cursor / Windsurf
- [[vs-harness-engineering-and-12-rules]] — **the load-bearing article for personal harness improvement**: axis-by-axis comparison with Lopopolo + Mnilax; adoption matrix; what to take from each system

## Cross-links to other autopilot topics

- [[external|harness-engineering/_index]] — Lopopolo's OpenAI-scale harness; ClaudeKit is the small-team / individual analog. See [[vs-harness-engineering-and-12-rules]] for axis-by-axis.
- [[external|claude-md-12-rules/_index]] — Mnilax's behavioral rules; ClaudeKit Hooks pattern is a deterministic implementation of similar discipline (Rule 6 token budgets → ClaudeKit's `/ck:fix` 6-phase budget; Rule 12 fail-loud → Hooks injection)
- [[external|claude-code-hooks/_index]] — ClaudeKit's hook architecture is a concrete library built on top of native Claude Code hooks; direct architectural lineage
- [[external|workflow-ai-coding/_index]] — workflow patterns (Ralph Loop, Skills-over-Agents) appear in both this topic and that one; ClaudeKit operationalizes them

## Source preservation

- **Raw guides:** `raw/vividkit-guides/*.md` — 21 markdown files, fetched 2026-05-11 via Tier 0 curl
- **NotebookLM ID:** `d179ac0c-428b-47e6-b859-99a6b7e7bcb1` (21 sources uploaded as text)
- **Synthesis raw:** `raw/2026-05-11-vividkit-claudekit-synthesis.md` (6-section NotebookLM Q&A, 614 lines)

## Empirical claim status

ClaudeKit is **active product documentation, not research**. Claims about effectiveness are aspirational/promotional, not measured. Treat as: "what the maintainers want you to believe the system does", not "what 6 weeks of testing showed".

This is different from:
- Lopopolo's harness-engineering: internal experience report with concrete numbers (1M LOC, 5-10 PRs/day claimed)
- Mnilax's 12-rule: claimed 41%→3% mistake rate over 30 codebases (self-reported but quantified)

When ingesting third-party benchmarks of ClaudeKit (if/when they exist), append to relevant articles.

## Maintenance

When future ingests touch ClaudeKit:
- New feature documentation → update [[command-reference]] OR specific article
- Independent benchmark / user-experience report → create [[user-reports.md]] (doesn't exist yet)
- ClaudeKit version bumps that change architecture → update [[architecture-overview]] with `### Update YYYY-MM-DD` block
