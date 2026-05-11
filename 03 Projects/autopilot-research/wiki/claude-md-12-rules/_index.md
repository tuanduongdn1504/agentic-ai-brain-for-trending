# claude-md-12-rules

> **Source:** Mnilax tweet thread (https://x.com/Mnilax/status/2053116311132155938)
> **Compiled:** 2026-05-11
> **Status:** Active behavioral contract — applies vault-wide when writing/modifying CODE (Python, shell, JS, etc.), NOT to wiki/markdown work
> **Lineage:** Karpathy (Jan 2026 thread on Claude failure modes) → Forrest Chang (4-rule CLAUDE.md template, 120K stars) → Mnilax (8 added rules from 6 weeks testing across 30 codebases)

This topic captures the **12-rule CLAUDE.md** behavioral contract for Claude Code sessions. The rules are now installed at vault-root `/CLAUDE.md` and govern code-writing tasks across all Storm Bear projects.

## Articles

- [[the-12-rules]] — verbatim text of all 12 rules + the "moment" anecdotes that justified each addition + author's empirical data (41% → 3% mistake rate)
- [[comparison-harness-engineering]] — axis-by-axis comparison with Lopopolo's harness-engineering stances (see [[external|harness-engineering/_index]]) — where the 2 systems agree, where they disagree, what to keep when both can't coexist

## Why this is wiki-worthy (not just a rule paste)

1. **Behavioral contract worth understanding, not just following** — each rule has a documented failure-mode it prevents; commentary preserves the WHY
2. **Comparison surface with harness-engineering** — Lopopolo's stances overlap and conflict with Mnilax's rules; understanding both informs personal harness design
3. **Historical lineage data** — Karpathy → Forrest Chang → Mnilax is a 4-month methodology evolution; the rules' shape is itself a data point about how Claude Code best-practices evolve
4. **Empirical claims worth tracking** — Mnilax claims 41% → 3% mistake rate after 6 weeks / 30 codebases. Independent verification belongs in this wiki when it emerges.

## Cross-links to existing autopilot topics

- [[external|harness-engineering/_index]] — Lopopolo's harness stance overlaps + conflicts with these rules. See [[comparison-harness-engineering]] for the axis-by-axis map.
- [[external|harness-engineering/contrarian-stances]] — Lopopolo's MCP-bearish, plan-mode-skeptical positions contrast with Mnilax's emphasis on explicit imperatives (Rule 1)
- [[external|harness-engineering/core-claims]] — Mnilax's empirical 41%→3% claim is testable in the same falsifier-check framework as Lopopolo's claim #4

## Source preservation

Full verbatim text: `raw/2026-05-11-claude-md-12-rules-mnilax.md` (paste-preserved because X.com auth-walled the original tweet at 2026-05-11; mirrors nitter/xcancel were dead at that date).

## Maintenance

When future ingests touch CLAUDE.md best-practices:
- **Independent verification of mistake-rate claim:** append `### Update YYYY-MM-DD` to [[the-12-rules]]'s "Numbers" section
- **Rule modifications or alternative templates:** create new article `vs-<alternative>.md` rather than editing the verbatim text
- **Storm-Bear-specific adaptations:** if specific rules need conditional framing for Storm Bear's wiki-heavy work, document in [[../../CLAUDE.md|autopilot-research/CLAUDE.md]] not here — this article stays close to the source
