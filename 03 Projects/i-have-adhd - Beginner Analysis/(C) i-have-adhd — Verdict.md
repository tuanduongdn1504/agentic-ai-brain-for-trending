---
title: (C) i-have-adhd — Verdict
wiki: v225
subject: ayghri/i-have-adhd
date: 2026-07-23
---

# i-have-adhd — Verdict (v225)

**Do this now:** if you use Claude Code daily, run `claude plugin marketplace add ayghri/i-have-adhd` then `/i-have-adhd` for one session and see whether action-first output helps you. That's the whole pilot — it's a free MIT output-style skill, read-only-safe.

## Verdict line

**GOAL-ALIGNED INCLUDE 3/4 [(a) FAIL · (b) STRONG keys the tier, ⚠️ MODERATE-reviewable · (c) STRONG · (d) STRONG] — cleanly GA (no §40); NO MINT; counts 46/11 UNCHANGED; §C live standalones 47 unchanged.**

`ayghri/i-have-adhd` = a cross-harness **agent skill** (Claude Code first + Codex/Zed/Hermes/Pi/Gemini/Antigravity/Cursor/OpenCode/Amp) that reformats the coding agent's **own conversational output** to be action-first / ADHD-friendly via 10 neurocognitively-grounded rules. MIT; ~8.8k★; no releases; author **Ayoub Ghriss** (disclosed individual ML researcher, **NOT Anthropic**).

## Why NO MINT (the honest call)

It shapes **how the agent talks to you**, not the code or UI it produces. That capability **already exists first-party** — Claude Code ships native output styles (Default / Explanatory / Learning + custom `/output-style:new`). i-have-adhd is a community, cross-harness, ADHD-targeted implementation of that recognized surface → a **form-factor within an existing genre**, not a new primitive. Its enumerated removal rules also read as a clean **Pattern #88 "Anti-Slop-Curation"** (88b named-rules + 88c machinery) instance in a NEW conversational-output sub-domain, and it shares the **ponytail v168** agent-behavior-ruleset species (code-axis vs conversation-axis). Corpus-first for the conversational-output-shaping surface + the corpus's **FIRST accessibility/neurodivergence subject** = data-points, NOT §C mints (domain-not-capability + form-factor + NOT world-first + §28).

⚠️ **Reviewable alternative:** a §C-standalone MINT ("Agent Conversational-Output-Style-Shaping Skill") is defensible on corpus-first-for-surface + the ponytail v168 precedent + the positive-accessibility-reshaping-beyond-anti-slop distinctiveness — recorded, LEANED NO-MINT, and flagged to the overdue ~v221+ audit. Either way counts stay 46/11.

## What's genuinely good

1. **Real rigor, not a bare prompt** — 5 stated neurocognitive facts + a clinical source + explicit override conditions + an `evals/` harness + `tests/` + CI + i18n (3 languages). (c) STRONG.
2. **Cross-harness** — one canonical `SKILL.md`, ~9 harnesses, multiple plugin-manifest formats (#84 84c).
3. **The 10 rules are a good template for the vault's own agent-output discipline** — action-first, restate-state, one-concrete-next-step, cap-lists, no-preamble. The vault already ends with a suggested next action; these formalize the rest.

## What to be honest about

- **Narrowest-value skill of the cluster.** Unlike ponytail v168 (cuts token spend) or hallmark v204 / ui-skills v218 (pilotable into hireui's frontend), i-have-adhd has no token-spend lever, no code-output change, and no hireui payoff. Its value is the operator's **reading experience** + a template for the vault's own output style. → the (b) MODERATE-reviewable flag.
- **NOT source-cloned** — the Python `evals/`/`hooks/`/`scripts/` is tree/doc-stated, not source-verified.
- **Auto-updating marketplace fetch** — the always-on `SessionStart` hook loads a ruleset that Claude Code re-fetches from the repo; a compromised upstream would change your agent's behavior. Benign today, but pin a commit if you want stability.
- **NOT a hireui component.** This is an operator-experience skill, not a product feature; hireui stays hand-built per its CONSTITUTION.

## Suggested next action

⭐ **A1 → C11 → B5** — read the 10 rules + 5 neurocognitive facts (zero install) → install into your own Claude Code and try it on one real session → distil the 10 rules into a `05 Skills/` output-discipline note (or the vault's own `CLAUDE.md` response-style guidance), composing with the vault's existing "verify + suggested-next-action" discipline. Fence: install-snapshot before enabling the always-on `SessionStart` hook + inspect what `plugin.json`/the hook do + MIT safe-to-borrow-the-rules-by-hand + pilot on your own Claude Code, not hireui's engineering flow.

**Merge:** review + merge `wiki/v225-i-have-adhd` off the v224 tip (`ec42c19`; the chain … → v223 → v224 → v225 merges in order). Not auto-merged — operator reviews + merges.
