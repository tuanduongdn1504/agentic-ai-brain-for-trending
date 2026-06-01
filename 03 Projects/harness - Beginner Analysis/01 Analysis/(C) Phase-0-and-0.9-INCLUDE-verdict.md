# (C) harness — Phase 0 + Phase 0.9 verdict (v131)

**Subject:** `revfactory/harness` — "Harness — The Team-Architecture Factory for Claude Code."
**Date:** 2026-06-01. **Routine:** v2.6 (first ship under v2.6 / §35). **Verdict:** **GOAL-ALIGNED INCLUDE (3/4 STRONG).**

---

## Phase 0 — scope / decision gate

In-scope on first read: a **Claude Code plugin** (`.claude-plugin/marketplace.json` + `plugin.json`, v1.2.0, Apache-2.0) containing a single meta-skill `skills/harness/SKILL.md` that **generates multi-agent teams + skills**. This is the corpus's core domain (Claude Code / agentskills.io / autonomous agents for software development). No decision-gate concerns. Proceed to Phase 0.9.

**Metadata (verified, gh API + raw files 2026-06-01):** 4,851★ / 666 forks (fork_ratio 0.137) / 0 open issues / created 2026-03-26 / pushed 2026-05-29 (~67 days) / ~72★/day. License Apache-2.0. primaryLanguage HTML (= the `index.html` GitHub Pages site; content is Markdown). Topics: claude-code, claude-code-plugin, harness, harness-engineering. diskUsage ~9.3MB (PNG banners). `latestRelease: null` (versioned via plugin.json + badge). Homepage revfactory.github.io/harness. Author **Minho Hwang** (`revfactory`, South Korea, @kakao; 2012 account, 278 repos, 528 followers).

---

## Phase 0.9 — STRICT INCLUDE/SKIP (4 criteria)

### (a) cultural-peer / (a)-7 foundational-vendor — **WEAK / geographic PASS (NOT load-bearing)**

Minho Hwang is **South-Korea-located** (employer @kakao). Under the 7-axis (a) taxonomy (v2.3.1 §25) this is an **(a)-6 Asian-LOCATED geographic PASS**, and — as best I can determine — **the first South-Korea-located subject in the corpus** (the tracked Asian-LOCATED cluster has been VN / China-Mainland / Japan; no prior Korean subject I can identify → **flag to verify at audit**, do not assert corpus-first as fact). **But:** he is a **big-company engineer (Kakao), not a solo VN/indie cultural-peer** in the structural sense the (a) axis usually rewards (cf. the v98 Microsoft / v112 Microsoft-Dublin / v113 Google-Cloud-DevRel precedents, which did NOT (a)-PASS). So this is a **geographic-cluster PASS, not a structural-peer PASS**, and it is **explicitly not load-bearing** — (b)(c)(d) carry the verdict. Honest, deliberately un-inflated. (No new (a) sub-axis minted; Korea files under the existing (a)-6 geographic axis.)

### (b) goal-relevance — **STRONG** (verdict-carrier)

Goal #1 = "Master Claude and autonomous agents for software development." harness is a Claude Code meta-skill that **generates coordinated multi-agent teams + their skills** — about as on-the-nose as goal #1 gets. **Doubly relevant** because Storm Bear is a Scrum coach: the 6 team-architecture patterns, team-size guidance ("3 focused members beat 5 scattered"), Producer-Reviewer / Supervisor / Hierarchical-Delegation, and the feedback-and-evolution loop are literally *team-process design*. Cost-of-trial LOW–MINIMUM (reversible plugin install) × DIRECT relevance → STRONG per §10.

**Why STRONG and not STRONGEST (honest brakes):**
1. It requires Claude Code's **experimental Agent Teams** feature (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) — gated, may change.
2. The `SKILL.md` body is **Korean-primary** (the operator reads EN/VI — usable but a real friction).
3. It is a **scaffold generator** run occasionally to design a team, not a daily-use tool.

This is a notch below v126 compound-engineering (which was STRONGEST: no experimental flag, English-primary, immediately usable). I am **not** inflating (b) to STRONGEST to make the ship look maximally goal-aligned — STRONG is the disciplined call.

### (c) instructive-exemplar — **STRONG**

Genuinely instructive at the methodology layer: 6 named orchestration patterns each with when-to-use / example / caveat / **team-mode-suitability**; a teams-vs-subagents **decision tree**; **5 complete worked team examples** (research, SF-novel pipeline+fan-out, webtoon producer-reviewer, code-review fan-out+debate, code-migration supervisor) **with full agent `.md` file bodies**; a **Progressive-Disclosure** skill-authoring doctrine (metadata ~100 words / SKILL.md <500 lines / references unlimited); a skill-**testing** methodology (with-skill vs without-skill A/B; should-trigger / should-NOT-trigger "near-miss" verification); a **QA-agent** guide ("based on 7 real bugs", incremental cross-boundary QA). A compact, usable reference on multi-agent orchestration even if you never install it.

### (d) corpus-connectivity — **STRONG**

- **agentskills.io SKILL.md** + **Claude Code plugin marketplace** (own `marketplace.json`) → v95 claude-plugins-official + v126 compound-engineering siblings.
- **Multi-agent orchestration siblings:** v126 compound-engineering (51 agents), v94 Understand-Anything (7-agent pipeline), v99 cmux (13-agent multiplexer), v95 skill-creator (skill generation).
- **Pattern #57 corpus-recursive:** the README "Coexistence" table explicitly cites **ECC = `affaan-m/everything-claude-code` (corpus v1/v78)** as the "L2 cross-harness workflow" neighbor.
- **Progressive-Disclosure doctrine** → v93 anthropics/skills + v76 agent-skills-standard.
- **Trilingual i18n** (EN/KO/JA) → i18n cluster.
- **Name-space note:** sister repo `revfactory/claude-code-harness` ≠ corpus v107 `claude-code-harness` (Chachamaru, Japan). Same name, different author/repo — do **not** conflate.

---

## Verdict

| Criterion | Call | Note |
|---|---|---|
| (a) cultural-peer / (a)-7 | **WEAK / geographic** | S-Korea @kakao; (a)-6 geographic, likely corpus-first KR (verify); big-co employee not solo peer; NOT load-bearing |
| (b) goal-relevance | **STRONG** | Claude Code multi-agent-team generator; goal #1 ∩ Scrum; not STRONGEST (experimental flag + Korean skill) |
| (c) instructive | **STRONG** | 6 patterns + decision trees + 5 full worked examples + skill-authoring/testing/QA methodology |
| (d) connectivity | **STRONG** | agentskills.io/marketplace + multi-agent siblings + cites ECC v1/v78 + Progressive Disclosure |

**→ GOAL-ALIGNED INCLUDE (3/4 STRONG)** (v2.5 §31 tier: (b) PASSes MODERATE+, so this is the corpus's core, **not** an off-goal capture). The INCLUDE rests on (b)(c)(d); (a) is a non-load-bearing geographic bonus.

---

## §35 soft off-goal-rate ceiling — analysis

- **Entering this ship the ceiling was BREACHED:** the last 3 wiki-ships were v127 (OG, override) + v128 (OG, (a)-rescue) + v129 (OG, (a)-rescue) = **3 off-goal in 3**. Per **§35.2**, the next wiki-ship MUST be a GOAL-ALIGNED INCLUDE (or carry an explicit logged `[ceiling-override]`).
- **v131 harness is a GOAL-ALIGNED INCLUDE on its own merits** → it **satisfies the §35.2 mandate legitimately. NO `[ceiling-override]` is used or needed.** (The operator's request happened to land on a genuinely goal-aligned subject — this was not a verdict laundered to clear the ceiling; (b) is honestly STRONG, see the brakes above.)
- **Rolling-3-ship window after v131** = {v128 OG, v129 OG, **v131 GA**} = **2 OG → still technically BREACHED.** §35.2's *requirement* (next ship goal-aligned) is met; the **ceiling fully clears** only once another goal-aligned ship scrolls v128 out — i.e. a goal-aligned **v132** → window {v129 OG, v131 GA, v132 GA} = 1 OG ≤ 1 → **CLEAR** (§35.3).
- **Override-frequency triggers (2-in-20 / 3-in-30):** UNCHANGED — v131 is **not** an override, so it adds nothing to the override count (`[1 ov]` holds) and trips nothing.

## Streak (v2.5 §32 forward / carried under v2.6)

Historical **"49+3\*" FROZEN @v125** (not recomputed). Forward: **`GA:1 · OG:3 [1 ov]` → `GA:2 · OG:3 [1 ov]`** — v131 = the **2nd GOAL-ALIGNED PASS** under v2.5/v2.6 (the consecutive-GA stream, broken by v127, restarts: v126 GA … v131 GA, with v127/v128/v129 OG between). Override subset `[1 ov]` UNCHANGED.

## Honest summary

A clean, genuinely on-corpus GOAL-ALIGNED INCLUDE that — fortunately and legitimately — discharges the §35.2 mandate. The one thing I refused to do: inflate (b) to STRONGEST to make the ceiling-satisfaction look stronger. (b) is honestly STRONG (experimental-flag dependency + Korean-primary skill body keep it off STRONGEST), and that is still comfortably MODERATE+ = goal-aligned. (a) is a non-load-bearing geographic PASS (likely corpus-first Korea, flagged to verify, with a big-company-employee caveat).
