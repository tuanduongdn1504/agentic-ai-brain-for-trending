# claude-md-12-rules

> **Source:** Mnilax tweet thread (https://x.com/Mnilax/status/2053116311132155938)
> **Compiled:** 2026-05-11
> **Status:** Active behavioral contract — **applies to every task in this vault unless explicitly overridden** (per Mnilax's verbatim scope: "These rules apply to every task in this project unless explicitly overridden")
> **Lineage:** Karpathy (Jan 2026 thread on Claude failure modes) → Forrest Chang (4-rule CLAUDE.md template, 120K stars) → Mnilax (8 added rules from 6 weeks testing across 30 codebases)

This topic captures the **12-rule CLAUDE.md** behavioral contract for Claude Code sessions. The rules are now installed at vault-root `/CLAUDE.md` and govern every task in this vault — code-writing AND wiki/markdown work — unless an explicit override is invoked.

## Scope note (corrected 2026-05-11, second-pass)

The **initial paste used an over-restrictive scope** ("ONLY when writing CODE") that I drafted. Audit revealed **11 of 12 rules are universally applicable** — only Rule 9 (Tests verify intent) is genuinely code-specific. Reverted to Mnilax's verbatim per-project scope. See "Open decisions" section for the audit table.

**Override convention (when a rule genuinely doesn't fit):**
- For wiki/markdown work: invoke Rule 9 override explicitly when applicable — "verify intent" semantic still holds (e.g., does this wiki article actually serve the research thread it claims to?) but literal test-writing doesn't apply
- For trivial tasks (per Mnilax's "Bias" clause): use judgment; rules don't have to be ceremoniously invoked for one-line fixes
- For overrides driven by stronger external context (e.g., Storm Bear librarian rules say "ask before editing existing notes" — that DOES still apply on top of Rule 3): both rule sets compose; the strictest wins

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
- [[external|claudekit/_index]] — ClaudeKit infrastructure-implements 7 of 12 rules; see [[external|claudekit/vs-harness-engineering-and-12-rules]] for 3-way comparison including this topic

## Source preservation

Full verbatim text: `raw/2026-05-11-claude-md-12-rules-mnilax.md` (paste-preserved because X.com auth-walled the original tweet at 2026-05-11; mirrors nitter/xcancel were dead at that date).

## Maintenance

When future ingests touch CLAUDE.md best-practices:
- **Independent verification of mistake-rate claim:** append `### Update YYYY-MM-DD` to [[the-12-rules]]'s "Numbers" section
- **Rule modifications or alternative templates:** create new article `vs-<alternative>.md` rather than editing the verbatim text
- **Storm-Bear-specific adaptations:** if specific rules need conditional framing for Storm Bear's wiki-heavy work, document in [[../../CLAUDE.md|autopilot-research/CLAUDE.md]] not here — this article stays close to the source

## Open decisions (active, time-boxed)

### Universal-vs-code-only scope audit — resolved 2026-05-11 (second-pass)

- **Decision date:** 2026-05-11 (resolved same-day)
- **Status:** RESOLVED — revert to Mnilax verbatim per-project scope
- **Context:** Initial scope clause restricted rules to CODE-only. User caught this by quoting Mnilax's actual text: *"These rules apply to every task in this project unless explicitly overridden."* Audit revealed the restriction was over-engineering on my part.
- **Audit table (rule × universal applicability):**

| Rule | Code-specific? | Wiki/non-code interpretation |
|---|---|---|
| 1. Think Before Coding (state assumptions) | ❌ Universal | Apply directly to wiki research, sourcing, summarization |
| 2. Simplicity First | ❌ Universal | Wiki articles benefit from minimum-content discipline |
| 3. Surgical Changes | ❌ Universal | Maps directly to Storm Bear "ask before editing existing notes" |
| 4. Goal-Driven Execution | ❌ Universal | Wiki compile cycle is exactly this pattern |
| 5. Model for judgment only | ❌ Universal | Wiki indexing / cross-linking is often deterministic |
| 6. Token budgets | ❌ Universal | Wiki sessions need budget too (Storm Bear refactored for this reason) |
| 7. Surface conflicts | ❌ Universal | Wiki cross-references conflict regularly |
| 8. Read before write | ❌ Universal | Librarian rules already require master-index read first |
| **9. Tests verify intent** | ✅ **Code-only** | Override for wiki — literal test-writing not applicable; intent-verification semantic still holds |
| 10. Checkpoint per step | ❌ Universal | Multi-step wiki compile needs checkpoint discipline |
| 11. Convention conformance | ❌ Universal | Wiki style (file naming, article structure) needs conformance |
| 12. Fail loud | ❌ Universal | Matches Storm Bear "NEVER fabricate information" |

- **Resolution:** vault-root scope clause replaced with Mnilax verbatim "every task in this vault unless explicitly overridden". Rule 9 implicitly overridden for non-code tasks; other 11 apply universally.
- **Why this resolution is durable:** Mnilax's framing was already universal-per-project. My over-restriction was unforced error; reverting to source removes ambiguity.

### Compliance-ceiling tradeoff — vault-root CLAUDE.md at 229 lines

- **Decision date:** 2026-05-11
- **Status:** Accept current state; observe before optimizing
- **Context:** Mnilax explicitly warns "past 200 lines, compliance drops sharply" — yet pasting all 12 rules INTO Storm Bear's pre-existing vault-root CLAUDE.md pushed it to **229 lines (+14% over the ceiling)**. Meta-paradox: the file violating the rule IS the file containing the rule.
- **Why accept (not premature-trim):**
  - 14% overage is moderate, not extreme
  - Mnilax's "compliance falls off cliff past 14 rules" is about RULE COUNT, not raw line count — and we have 12 rules, well within
  - The line count is inflated by Storm Bear-specific content (Vault State Architecture, Pattern Library state, projects index) — relevant for vault navigation, not rule attention-budget
  - No data yet on actual compliance impact for THIS specific configuration
- **Optimization triggers (any 1 of these → revisit decision):**
  - Observable rule-violation by agents in code-writing tasks within 1-2 weeks
  - Agents skipping rules 9-12 (last rules in the block) noticeably more than rules 1-4 → indicates attention-budget exhaustion
  - Subjective sense that recent agent behavior degraded after the paste
- **If trigger fires → optimization options ranked:**
  1. **Option C (preferred):** Trim Storm Bear's "Vault State Architecture" section (currently ~26 lines documenting a refactor that already shipped) → can shrink to 5-line pointer to chapter files. Brings total ~205 lines.
  2. **Option B (fallback):** Move 12-rule block to project-local CLAUDE.md, lose vault-wide scope
  3. **Option A2:** Compact rule body text — drop sub-bullets where rule is self-explanatory (e.g., Rule 2 could be 1 line instead of 3)
- **Review-by date:** **2026-05-25** (2 weeks from paste). If no observable compliance issue by then, decision becomes permanent — line ceiling treated as soft for this specific vault.
- **Where to look for compliance signal:**
  - Agent code commits that violate Rules 9-12 specifically (tests-verify-intent, checkpoints, conformance, fail-loud)
  - Failure to surface assumptions in chat (Rule 1)
  - Silent skipping of token budgets (Rule 6)
