# (C) Phase 0 + Phase 0.9 INCLUDE verdict — obsidian-second-brain (v134)

**Subject:** [`eugeniughelbur/obsidian-second-brain`](https://github.com/eugeniughelbur/obsidian-second-brain)
**Routine:** v2.6. **Date:** 2026-06-01. **Verdict:** **GOAL-ALIGNED INCLUDE 3/4.**

---

## Phase 0 — intake

Operator handed the URL directly with "build LLM wiki for …". At intake the *name* ("obsidian-second-brain") read like a PKM/Obsidian-vault template = likely (b)-FAIL → OFF-GOAL CAPTURE → §35 re-breach risk (flagged to operator up front). **Fetching the actual repo overturned that read:** it is not a vault template but a **cross-CLI Claude Code skill** (Claude Code / Codex CLI / Gemini CLI / OpenCode) driven by autonomous scheduled agents, explicitly extending Karpathy's LLM Wiki pattern. That moves it from off-goal to goal-aligned. No decision-gate needed; proceeded to Phase 0.9 STRICT.

⚠️ **Data caveat:** the sandbox returns mocked responses for `curl`, so GitHub-API fields (exact created_at, exact star count) could not be API-verified. All metadata is from the GitHub repo page + README + SKILL.md + the releases list. Stars ≈ 1,700 (README: "1,000+ stars in 7 weeks"); age ≈ 8 weeks (first public release v2.2.0 ~2026-04-05 → today). Flagged as best-effort, not authoritative.

## Phase 0.9 — STRICT 4-criterion test

### (a) Cultural-peer / (a)-7 foundational-vendor — **FAIL**
Author **Eugeniu Ghelbur** — Moldovan/Romanian name; **AI Automation Engineer @ Single Grain** (US digital-marketing agency); X @eugeniu_ghelbur; Substack "The AI Operator"; location undeclared. Not a VN/Asian cultural-peer; not (a)-7 (no vault-substrate vendor relationship). It *could* be a corpus-first Eastern-European/Moldovan locale, but the location is undeclared and the employer is US — so this is **WEAK-geographic at best, not load-bearing**, and consistent with the §25 / v98 (Indian-diaspora-Berlin) / v112 (Pakistani-Dublin) / v113 (London-Indian-heritage) precedent, **no new (a) sub-axis is minted** (cascade-dilution avoidance). Clean FAIL. The INCLUDE rests on (b)(c)(d).

### (b) Goal-relevance — **STRONG** (the load-bearing criterion; this is what makes it GOAL-ALIGNED, not OFF-GOAL)
Goal #1 = "Master Claude and autonomous agents for software development."
- **For:** It's a **multi-harness Claude Code skill** — the corpus's core medium — and its subject is **autonomous knowledge agents** (4 scheduled background agents: morning / nightly / weekly / vault-health; + parallel subagents that touch 5–15 files per write). It is also **the most directly-applicable-to-this-vault subject in corpus history**: the KJ OS Template vault *is* a hand-maintained Obsidian + Claude + Karpathy-LLM-wiki, and this skill automates exactly those maintainer jobs (rewrite-not-append, reconcile contradictions, synthesize, lint/health, AI-first notes-for-future-Claude). The `/obsidian-architect` command scans codebases and maintains architecture notes (a direct software-dev surface). Cost-of-trial is LOW-to-MEDIUM × applicability is DIRECT → STRONG per §10.
- **Against STRONGEST (held honestly):** (i) the domain is **PKM/knowledge-management, not software-dev shipping** — only `/obsidian-architect` is a direct dev surface; (ii) **influencer/marketing positioning** ("compounds while you sleep", trending badge, Substack funnel); (iii) the install is a **`curl|bash` skill that rewrites 5–15 of your files per write** — non-trivial footprint that argues against treating it as a turnkey daily tool.
- **Verdict: STRONG.** STRONG is the goal-aligned tier and clears §35 on its own — there is no incentive to inflate to STRONGEST, and I did not.

### (c) Skill / engineering exemplar — **STRONG**
An ~8,500-line monolithic `SKILL.md` (~200 sections) + 43 commands across 4 layers + a 4-CLI build system (`scripts/build.sh` compiles one canonical source → Claude/Codex/Gemini/OpenCode native formats + dispatchers) + hooks (SessionStart / PostCompact / PostToolUse) + 4 scheduled agents + 13 Core Operating Principles + bi-temporal facts + Two-Output Rule + documented anti-patterns (false-absence, fabrication). A genuine model for "how to author a large multi-harness Claude skill."

### (d) Corpus connectivity — **STRONGEST**
The highest-connectivity ship in a long stretch:
- **Explicitly extends Karpathy's LLM Wiki** (the corpus's ECC v1/v78 foundational anchor AND this vault's stated premise) on the **Obsidian** substrate (the vault's literal home), implementing the exact maintainer jobs.
- **3rd instance of the corpus-recursive-at-methodology-influence thread** (v94 consume + v118 generate + v134 generate — see the Phase-4b doc).
- Pattern #84 84c.2 (CLI-generates-native-formats); Library-vocab #12 (CLAUDE/AGENTS/GEMINI/SKILL routing artifacts); Pattern #18 B1 (MCP vault-access); research-toolkit BYOK/aggregator threads (xAI/Perplexity/Gemini/YouTube/OpenAI).

### Verdict
**GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL + (b) STRONG + (c) STRONG + (d) STRONGEST.

## §35 ceiling check (v2.6)
- Entering v134, the ceiling was **CLEAR** (after v133, rolling-3 window = {v131 GA, v132 GA, v133 OG} = 1 OG ≤ 1).
- **v134 = GOAL-ALIGNED → new window {v132 GA, v133 OG, v134 GA} = 1 OG ≤ 1 → STAYS CLEAR (§35.3).**
- This is exactly the move that **avoids the re-breach flagged at v133** (a 2nd consecutive off-goal at v134 would have made the window 2 OG and forced a `[ceiling-override]`).
- **No override.** v134 is not a Phase-0.9 override and not a ceiling-override. Override-frequency triggers UNCHANGED (lifetime 4: v84+v116+v122+v127; 3-in-30 last tripped at v127).

## Streak (v2.5 §32 forward / v2.6)
Historical **"49+3\*" frozen @v125**. Forward: **`GA:3 · OG:4 [1 ov]` → `GA:4 · OG:4 [1 ov]`** (v134 = 4th GOAL-ALIGNED PASS under v2.5/v2.6). Consecutive-GA stream restarts at 1 (v133 OG broke the v131→v132 run). Override subset `[1 ov]` UNCHANGED.

## Calibration note (per the Finding-2 discipline)
(a) genuinely FAILED — a healthy rubric-discrimination data point, not laundered into a soft PASS via a manufactured Moldovan locale axis. (b) is honestly **STRONG, not STRONGEST**, on stated grounds. The honest tension worth recording: this is simultaneously the **most on-corpus subject in months** AND a subject whose *install philosophy collides with the vault's hand-curation discipline* — both true, both recorded (see the pilot note).
