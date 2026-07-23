---
title: (C) i-have-adhd — Deep Dive
wiki: v225
subject: ayghri/i-have-adhd
date: 2026-07-23
verdict: GOAL-ALIGNED INCLUDE 3/4 · NO MINT · counts 46/11 UNCHANGED
author_note: (C) = Claude-generated. Source hand-fetched (rendered repo page + raw README + SKILL.md + INSTALL.md + repo tree). NOT source-cloned.
---

# i-have-adhd — Deep Dive (LLM Wiki v225)

> `github.com/ayghri/i-have-adhd`
> **"A skill for your coding agent to stop it from burying the answer. ADHD-friendly output."** (repo description, verbatim)

## 0. One-paragraph summary

`i-have-adhd` is a **cross-harness agent skill** — one canonical `skills/i-have-adhd/SKILL.md` distributed as a Claude-Code-first plugin (and to Codex / Zed / Hermes / Pi / Gemini CLI / Antigravity / Cursor / OpenCode / Amp) — that **reformats the coding agent's own conversational output** so an ADHD reader can act on it: lead with the next doable action, number multi-step work, restate state every turn, cap lists, drop preamble/recap/closers, give concrete time estimates, make wins visible. It is grounded in five stated neurocognitive facts and loosely adapted from J. Russell Ramsay & Anthony L. Rostain's *Adult ADHD Tool Kit*. MIT-licensed, ~8.8k★, no releases, i18n (en/ja/zh-CN). It ships an `evals/` harness, `tests/`, `.github/workflows/` CI, and a `SessionStart` hook for an always-on mode. **It shapes how the agent *talks to you*, not the code or UI it produces.**

## 1. What it is (verified)

| Field | Value | Provenance |
|---|---|---|
| Repo | `ayghri/i-have-adhd` | rendered page |
| Description | *"A skill for your coding agent to stop it from burying the answer. ADHD-friendly output."* | rendered page (verbatim) |
| Author | **Ayoub Ghriss** (`ayghri`) — disclosed individual; per his GitHub profile an ML researcher (CLIMB group), 78 repos. **NOT Anthropic.** | WebSearch (profile-stated) |
| License | MIT | rendered page |
| Language | **Python 94.3% / Shell 5.7%** | rendered page |
| Stars / forks | ~8.8k★ / 406 forks (page-stated) | rendered page |
| Releases | **None published** | rendered page |
| Topics | `productivity` `developer-tools` `adhd` `claude-code-plugin` `claude-skills` | rendered page |
| i18n | `README.md` + `README.ja.md` + `README.zh-CN.md` | repo tree |
| Type | Single agent **behavior / output-style skill** (a distributable Claude Code plugin + cross-harness) | derived |

**⚠️ NOT source-cloned.** Per the v200→v224 self-throttle (the ~205K CLAUDE.md shim overflows every subagent > 200K, so the deep-dive workflows fail prompt-too-long), this wiki is built from the rendered repo page + raw `README.md` + `skills/i-have-adhd/SKILL.md` + `INSTALL.md` + the repo file tree. The Python in `evals/`/`hooks/`/`scripts/`/`tests/` is **tree-stated, not source-verified**.

## 2. The "Python 94.3%" resolved

A ruleset skill is Markdown — the 94.3% Python is the **surrounding machinery**, located (per the repo tree) in:

- `evals/` — an evaluation harness (does the skill actually change output? — the SkillOpt v178 / ponytail v168 kind of rigor)
- `tests/` — a test suite
- `scripts/` — install/automation
- `hooks/` — the `SessionStart` hook that loads the ruleset when the always-on flag file is present
- `.github/workflows/` — CI

So the *core artifact* is the Markdown `SKILL.md` (the 10 rules); the Python is the tooling that installs, gates, evaluates, and always-on-enables it. **This is what lifts it above a bare prompt** (see §6, (c) STRONG). *(Exact contents tree-stated, not source-read — flagged.)*

## 3. The 10 rules (the core artifact)

From `skills/i-have-adhd/SKILL.md` (verbatim-where-quoted; the skill states its output is *"shaped for ADHD cognition, not merely brief"* and rests on **five neurocognitive facts**: small working memory, friction between understanding and doing, startup difficulty, uniform time perception, dopamine scarcity):

1. **Lead with action** — first line is doable now; command or path before prose.
2. **Number multi-step tasks** — each step is one bounded action; cut trivial steps.
3. **End with a concrete next action** — name ONE thing doable in under two minutes.
4. **Suppress tangents** — finish the first issue; offer others separately.
5. **Restate state every turn** — the reader cannot hold multi-step context between messages.
6. **Give specific time estimates** — *"15 minutes"* beats *"some work."*
7. **Make wins visible** — show what works concretely; don't bury progress.
8. **Matter-of-fact tone on errors** — state cause and fix directly.
9. **Cap lists at 5 items** — split large lists into "now" vs "later."
10. **No preamble, recap, or pleasantries** — start with the answer; end when done.

Plus **override conditions**: explicit requests to explain, destructive actions, debug spirals, ambiguity, and conflicts between the rules and task necessity. Trigger `/i-have-adhd`; persists until *"stop adhd mode."*

**Read the rules honestly:** some are anti-slop *removal* (no preamble/recap/closers; cap lists), some are *positive accessibility scaffolding* (restate state; time estimates; make wins visible; action-first). That mix — remove noise **and** add cognition-friendly structure — is what makes it more than "be concise."

## 4. Distribution & always-on (verified)

**Cross-harness (~9 harnesses), one canonical skill, many plugin-manifest formats** (repo tree): `.claude-plugin/` + `plugin.json` (Claude Code) · `.codex-plugin/` (Codex) · `.cursor/skills/i-have-adhd/` (Cursor) · Zed (native Agent Skills) · Hermes (`hermes skills`) · Pi (`npx skills`) · Gemini CLI (`GEMINI.md` + `gemini-extension.json`) · Antigravity (`agy plugin`) · OpenCode / Amp (`npx skills` or manual folder placement) · a generic `.agents/plugins/`.

**Install (Claude Code):**
```
claude plugin marketplace add ayghri/i-have-adhd
claude plugin install i-have-adhd@i-have-adhd
/i-have-adhd
```
No local clone — Claude Code fetches + keeps it updated from the repo (a supply-chain note: a compromised upstream would change your agent's behavior on the next fetch).

**Always-on (Claude Code):** `touch ~/.claude/.i-have-adhd-always` → the `SessionStart` hook loads the rules automatically each session (`rm` to disable). Other harnesses achieve always-on by pasting the ruleset into a persistent config (`AGENTS.md` / `SOUL.md`).

## 5. What it is NOT (non-claims, verified)

- **NOT world-first.** Claude Code ships **native output styles** (`Default` / `Explanatory` / `Learning`) + custom output styles via `/output-style:new` (which scaffolds a Markdown communication-style file). i-have-adhd is a **community, cross-harness, ADHD-targeted output style** — a distinctive *preset + cross-harness distribution + neurocognitive grounding*, on a recognized, first-party-existing surface. (Claude Code output styles are Claude-Code-only; i-have-adhd's distinctive is cross-harness + accessibility-grounded + an eval harness.)
- **NOT a skill collection** — a single skill (contrast agent-skills v184 / marketingskills v202 / ui-skills v218).
- **NOT an MCP server** — ships no MCP server (a skill + a hook).
- **NOT #52** — ~8.8k★ / 0 releases page-stated (§37.4 mocks the GitHub API → velocity unestablishable).
- **NOT #57** — cites Ramsay & Rostain (a non-corpus clinical source) + names harnesses as install targets; no corpus-subject influence-citation.

## 6. Four-criterion scoring

**GOAL-ALIGNED INCLUDE 3/4 [(a) FAIL · (b) STRONG keys the tier · (c) STRONG · (d) STRONG] — cleanly GA (no §40).**

- **(a) FAIL.** Ayoub Ghriss = a disclosed individual ML researcher, not Anthropic (§41 — no name/heritage/locale/notability rescue; the disclosed-individual (a)-axis answers NO). #19 19a first `ayghri` author.
- **(b) STRONG keys the tier (⚠️ MODERATE-reviewable).** A Claude-Code-first, cross-harness **agent-behavior / output-style skill** = dead-center on the agent-skills substrate the vault studies (agent-skills-standard v76 / CodexKit v121 / agent-skills v184 / hallmark v204 / ui-skills v218) + the operator's own `05 Skills/` + daily Claude Code use; **immediately, zero-risk pilotable** (MIT, plugin-marketplace, a read-only output style — SkillSpector-class safe); ships an eval harness + tests + CI. STRONG-not-STRONGEST = third-party + Claude one of ~9 harnesses + a **single narrow output-STYLE skill** (shapes response formatting, not a software-dev capability, not code/UI quality; its payoff is the operator's *reading experience* of Claude, not a hireui feature). ⚠️ **MODERATE-reviewable**: "a narrow response-formatting preset" (the awesome-ai v170 calibration). Cleanly GA either reading — agent-skills is on-domain, no §40.
- **(c) STRONG (⚠️ MODERATE-reviewable).** More than a bare ruleset: a well-authored SKILL.md grounded in 5 neurocognitive facts + a clinical source + explicit override conditions; cross-harness distribution (~9 harnesses, multiple plugin-manifest formats); an `evals/` harness + `tests/` + a `SessionStart` hook + CI + i18n (en/ja/zh-CN); ~8.8k★ real traction. Caveats: the core artifact is a **single narrow prompt/ruleset** (the hard part is prompt-authoring, not engineering); no releases / young; ⚠️ **NOT source-cloned** (the Python rigor is tree/doc-stated); stars page-stated → NOT #52.
- **(d) STRONG.** Agent-skills ecosystem (agent-skills-standard v76 / CodexKit v121 / agent-skills v184 / marketingskills v202 / karpathy v63) + **ponytail v168 §C** (the agent-behavior-ruleset *species* — code-axis vs conversation-axis) + **Pattern #88 Anti-Slop-Curation** (88b named-rules + 88c machinery; impeccable v75 / taste-skill v81 / hallmark v204 = the design/UI sub-domain, i-have-adhd = the conversational-output sub-domain) + **Claude Code native output styles** (the world-first denial + closest first-party analogue) + #84 84c cross-harness + #12 LLM-routing-artifacts (`GEMINI.md` + `plugin.json` + `.claude-plugin/` + hooks + `gemini-extension.json`) + a NEW **accessibility / neurodivergence** thread.

## 7. Pattern outcome — NO MINT

**Primary:** i-have-adhd is a clean instance of the **agent-behavior / output-STYLE skill** genre — the **ponytail v168** agent-behavior-ruleset *species* in the **conversational-output-style vertical** (ponytail v168 shapes the CODE the agent writes; i-have-adhd v225 shapes HOW the agent communicates back). Its removal rules (no preamble/recap/closers; cap lists) also read as a clean **Pattern #88** 88b-named-rules + 88c-machinery instance in a NEW **conversational-output sub-domain**, distinct from the design/UI 88-sub-domain (impeccable v75 / taste-skill v81 / hallmark v204).

**Corpus-first for the conversational-output-shaping surface + the corpus's FIRST accessibility/neurodivergence-focused subject = data-points, NOT §C mints**, because:
1. **Form-factor within an existing genre.** Claude Code ships native output styles + custom `/output-style:new`; i-have-adhd is a community implementation of an already-recognized, first-party capability, packaged cross-harness. That's a form-factor, not a new primitive (the ui-skills v218 / hallmark v204 NO-MINT discipline).
2. **Domain-not-capability.** Accessibility / ADHD is a DOMAIN; §C vocab is agent-capability-shaped (the meetily v196 / little-book-rl v220 rule).
3. **NOT world-first** (Claude Code native output styles Default/Explanatory/Learning + custom output styles + a saturated "be-concise" preset/prompt space precede).
4. **§28 anti-inflation** on a single narrow output-style skill.

**⚠️ §C-standalone MINT recorded as the operator/audit-reviewable ALTERNATIVE:** *"Agent Conversational-Output-Style-Shaping Skill — a distributable cross-harness skill that reformats the agent's OWN conversational response to the human for a target reader (action-first / ADHD-friendly / anti-verbosity), as opposed to shaping the code (ponytail v168) or UI (hallmark v204) it produces."* Defensible on the corpus-first-for-surface + ponytail v168 mint precedent + the positive-accessibility-reshaping-beyond-anti-slop distinctiveness — but **LOSES** to NO-MINT on the Claude-Code-native-output-styles form-factor + domain-not-capability + §28 grounds. Recorded + a **DEFERRED watch axis**: "agent conversational-output-style / communication-style-shaping skill (+ the accessibility/neurodivergence sub-thread)."

**Counts 46/11 UNCHANGED; §C live standalones 47 unchanged; §C surface ≈54 unchanged.**

**SECONDARY (NOT minted):** #19 19a first `ayghri` author + first accessibility/neurodivergence subject · #84 84c cross-harness (one canonical SKILL.md → ~9 harnesses via multiple plugin-manifest formats; NO N-bump; **NOT** the ponytail-v168 14-platform native-rule-file *generator* — i-have-adhd distributes ONE skill many hosts consume) · #12 LLM-routing-artifacts (`GEMINI.md` + `plugin.json` + `.claude-plugin/` + `hooks` + `gemini-extension.json` + `AGENTS.md`/`SOUL.md` always-on) · ponytail v168 §C cross-ref (behavior-ruleset sibling; NO N-bump — different axis) · Pattern #88 88b/88c conversational-sub-domain cross-ref · Claude Code native output styles cross-ref · #66 install BENIGN (MIT; plugin-marketplace fetch; a `SessionStart` hook that loads a ruleset markdown; ⚠️ the `evals/`/`hooks/`/`scripts/` Python NOT source-cloned → install-snapshot fence before enabling always-on; the auto-update marketplace fetch = a mild supply-chain note) · the accessibility/neurodivergence-for-agents watch axis.

**Tier:** T1 Skill/Methodology Collection (single agent-behavior / output-style skill flavor — the ponytail v168 / hallmark v204 / karpathy v63 family).

## 8. Streak / §35

v224 GA:82 → **`GA:83 · OG:13 [7 ov]`** (cleanly GA on (b) STRONG; 6 consecutive GA post the v219 OG break). **§35 CLEAR** (window {v223 GA, v224 GA, **v225 GA**} = 0 OG).

## 9. Verification (per `feedback_wiki_verify_independently_check_collisions`)

Verdict produced **INLINE + fully hand-verified** — no workflow / no subagent (the ~205K shim overflows every subagent > 200K → prompt-too-long, the v200→v224 self-throttle). Source hand-fetched (rendered repo page + raw README + SKILL.md + INSTALL.md + repo tree). Identity (Ayoub Ghriss / CLIMB / not-Anthropic) + the world-first landscape (Claude Code native output styles) by WebSearch. **Collision by sanity-anchored hand-grep of `_state/` + `_patterns/` + `03 Projects/`:** zero `i-have-adhd`/`ayghri`/`ghriss`/`\badhd\b` hits (collision-clean + the corpus's first ADHD/accessibility subject); the `ponytail` + `hallmark`/`Pattern #88` sanity anchors hit richly (grep confirmed working). The ponytail v168 §C row read directly (`_patterns/06:78`, scoped to "Code-Minimalism" → a different axis, no N-bump). `inflation_check` HELD (0 mints; §C-mint DECLINED per §28 as a form-factor; NO-MINT alt recorded; counts 46/11 unchanged; max #85; no N-bumps).
