# (C) Hireui Harness Evaluation v2 — Integrating KJ OS Concepts

> **Date:** 2026-05-06 (same-day update to v1)
> **Supersedes:** `(C) 2026-05-06 hireui harness evaluation + best practices.md` (v1)
> **Why v2:** v1 surfaced gaps but didn't deeply mine KJ OS Template's mature concepts. After reading 9 source files (skills + patterns + reports + policies), 14 concepts deserve integration into Hireui Harness with explicit cost/pros tradeoffs.
> **Status:** Proposal — operator decision required per concept (no auto-apply)

---

## Source files reviewed (citations)

| # | File | Concept extracted |
|---|------|-------------------|
| 1 | `CLAUDE.md` (vault root) | 6 behavioral rules + folder structure pattern + chapter-shim refactor |
| 2 | `05 Skills/(C) project-code-analysis-harness.md` | Constitutional invariants + 4-phase workflow + read-only boundary |
| 3 | `05 Skills/llm-wiki-routine-v2.1.md` | 7-phase workflow + audit cadence + 5 promotion criteria + mini-audit + un-stale + counter-evidence |
| 4 | `05 Skills/SKILL_LOCK_POLICY.md` | PUBLIC-ARCHIVED vs IN-FLUX skill classification |
| 5 | `05 Skills/brain-setup.md` | 5-round interview pattern for context personalization |
| 6 | `PATTERN_LIBRARY.md` (root shim) | Vault state architecture + chapter file convention + ratio health classification |
| 7 | `_patterns/05-recent-additions.md` | Fact-verification protocol applied + audit-layer corrections |
| 8 | `03 Projects/product/anspace-harness/CLAUDE.md` | Per-project CLAUDE.md template + scope boundary |
| 9 | `03 Projects/product/anspace-harness/reports/(C) 2026-04-23-...md` | Real harness report format (~600 lines) |

---

## 14 Concepts to Integrate (each with cost / pros / cons)

### Concept 1: Constitutional Invariants pattern

**Source:** `(C) project-code-analysis-harness.md` line 25-34 — 5 explicit non-negotiable rules at top of skill, paperclip-inspired.

**Current Hireui state:** No constitutional layer. Rules scattered across CLAUDE.md, AGENTS.md, branch-policy.sh, lint-staged.config.js. Easy to bypass without anyone noticing intent violations.

**Change proposed:** Add `CONSTITUTION.md` at hireui repo root (or top of root CLAUDE.md) with 5-7 invariants. Examples:
1. Hook compliance is non-negotiable (no `--no-verify` without operator approval per commit)
2. CONTINUITY must be updated at session end if any commit was made
3. Always end with suggested next-action
4. Always produce dated artifact for substantial sessions (>1h work)
5. Never commit secret values (placeholders only in `.env.example`)
6. Branch policy enforced by hook; manual edits to hook require operator approval

| Cost | Pros | Cons |
|------|------|------|
| 30 min to draft + review | Single authoritative anchor; eliminates "did I just violate something?" | Rigid; if invariants are wrong, everything compounds wrong |
| 5 min to add link from CLAUDE.md/AGENTS.md | Goodhart's law corrective — invariants are non-negotiable, not targets | Risk of "constitution-as-decoration" if not enforced in tooling |
| 0 ongoing if well-written | Auditable: every session can be checked against the same 5-7 rules | Harder to evolve than soft conventions |

**Verdict:** ✅ HIGH PRIORITY — addresses the `--no-verify` habituation directly.

---

### Concept 2: Phased workflow with explicit Phase 0 pre-flight

**Source:** `llm-wiki-routine-v2.1.md` lines 91-249 — 9 sub-step pre-flight before any heavy work.

**Current Hireui state:** Sessions just start. No standard pre-flight. Today's session repeatedly hit "wait, what branch am I on?" / "do I have HIR-1149 fix?" / "is MCP loaded?" surprises.

**Change proposed:** Define a hireui Phase 0 pre-flight checklist:
```
0.1  Read .cm/CONTINUITY.md (current branch + active blockers + last decisions)
0.2  Run `git status` + `git branch --show-current` (confirm clean working state)
0.3  Verify branch matches intended work type per branch-policy
0.4  Check `.cm/memory/learnings.json` for relevant prior lessons (filter by topic)
0.5  Verify gitnexus index fresh (`gitnexus status` if MCP loaded; `arch -arm64 npx -y gitnexus status` otherwise)
0.6  Check operator backlog (any items at ≥3 sessions deferral?)
0.7  Decide session scope + estimated duration
0.8  If scope >1h: schedule iteration log creation at end
```

| Cost | Pros | Cons |
|------|------|------|
| 5 min/session (initial habit) | Eliminates 50%+ of mid-session "oh no" moments | Feels bureaucratic for 5-min tasks |
| 30 min once to codify checklist | Surfaces stale state before it cascades | Operator might skip when in flow |
| Drops to 1 min/session after 2 weeks | Standard handoff between sessions | Adds "ceremony" feeling for trivial work |

**Verdict:** ✅ HIGH PRIORITY — would have prevented today's MCP cwd discovery, branch-switching surprises, and 4 of the 5 documented lessons.

---

### Concept 3: Read-only target boundary

**Source:** `(C) project-code-analysis-harness.md` line 29 — "NEVER write to /Users/Cvtot/monorepo/anspace-space-manager"

**Current Hireui state:** Hireui harness writes to its OWN repo, so direct application doesn't fit. BUT: when Claude reasons about production-deployed code (web app already live), there's no equivalent boundary.

**Change proposed:** Define READ-ONLY boundaries by branch:
- `main` / `dev` branches → READ-ONLY (no direct commits; PR-only)
- Production-deployed paths (e.g., `src/core/services/*`) → require explicit gitnexus_impact analysis before edits
- Database migrations / schemas → READ-ONLY in agent sessions; manual review required

| Cost | Pros | Cons |
|------|------|------|
| 30 min to define paths + scope | Prevents accidental production breakage | Slows down legitimate refactor work |
| 0 ongoing if encoded in skills/hooks | Forces gitnexus_impact discipline (currently weak) | Edge cases: what about hotfixes? |

**Verdict:** 🟡 MEDIUM PRIORITY — defer until agent-dev work touches src/ in earnest. Currently agent-dev is harness-only.

---

### Concept 4: Always-produce-dated-artifact

**Source:** `(C) project-code-analysis-harness.md` line 30 + anspace-harness report `(C) 2026-04-23-code-analysis-harness-report.md` (real example, 600+ lines).

**Current Hireui state:** Today's session = 9 commits + 5 lessons + 4 deferred items + many decisions. **Nothing dated artifact-ed.** All in chat history.

**Change proposed:** Create `_bmad-output/sessions/(C) YYYY-MM-DD session-N.md` per session with substantial work. Use 13-section standardized template from `llm-wiki-routine-v2.1.md` Phase 5 (line 388-401):

```
1. Milestones hit
2. Phase breakdown (duration per phase)
3. What worked
4. What didn't work / friction
5. Action items (next session)
6. Total action items accumulating (running counter)
7. Meta-observations
8. Unique findings
9. Hireui-specific impact
10. Next session candidates
11. Strategic decision point
12. Scorecard (effort / leverage / quality)
13. Backlog escalation (if any item ≥3 sessions deferred)
```

| Cost | Pros | Cons |
|------|------|------|
| 30 min/session at the end | Compounds — each session strengthens the next | Yet another file to maintain |
| 1h to set up template | Iteration logs are how routine compounds (KJ OS proven 67 sessions) | Risk of write-once-read-never |
| Requires operator end-of-session discipline | Surfaces patterns invisible in chat (e.g., 3× --no-verify in one day) | Time pressure → skipped |

**Verdict:** ✅ HIGH PRIORITY — closest to being achievable today. Today's session itself should generate one as proof.

---

### Concept 5: Mandatory "Suggested next action" closing

**Source:** Vault root CLAUDE.md line 28 + `(C) project-code-analysis-harness.md` line 31.

**Current Hireui state:** Claude often suggests next actions but inconsistently. No enforcement.

**Change proposed:** Add to constitutional invariants (Concept 1) AND add to root CLAUDE.md as mandatory closing pattern. Example template:

```
## 🎯 Suggested Next Action
**[1 highest-leverage action]** — [effort estimate]. [1-line rationale.]

(Optional: 2-3 alternatives with trade-offs)
```

| Cost | Pros | Cons |
|------|------|------|
| 0 (habit) | Operator never wonders "what now?" | Sometimes obvious — feels redundant |
| Add to CLAUDE.md template | Cross-session continuity | Can become rote ("...what's next?") |
| Encode in iteration log section 5 | Forces ranking of options | If wrong recommendation, operator follows blindly |

**Verdict:** ✅ HIGH PRIORITY — easiest to adopt + highest cumulative effect.

---

### Concept 6: Operator-facing backlog discipline with BLOCKING-RECOMMENDATION tag

**Source:** `llm-wiki-routine-v2.1.md` line 79-83 — escalate at 5+ sessions deferral.

**Current Hireui state:** 4 items already at 2-3 sessions deferral (EAS init, Microsoft OAuth, HIRE_AGENT staging, Sentry rotation). No escalation mechanism. They'll silently age.

**Change proposed:**
- `.cm/memory/decisions.json` gets schema with `deferred_count` field
- Each session-end iteration log re-counts
- At ≥3 sessions: tag with 🟡 ATTENTION
- At ≥5 sessions: tag with 🔴 BLOCKING-RECOMMENDATION (operator must address before new work in same scope)

| Cost | Pros | Cons |
|------|------|------|
| 1h to define schema + tooling | Surfaces aging items before they bite | Easy to game (don't log = no count) |
| 5 min/session to update count | Forces conversation about deferred items | Some items are genuinely external (waiting on team) |
| 0 if integrated into iteration log template | Restores "honest signal" to backlog | Risk: every item gets classified blocking → noise |

**Verdict:** ✅ HIGH PRIORITY — Sentry token rotation in particular is a security risk that grows daily.

---

### Concept 7: 5 structural-promotion criteria for compound artifacts

**Source:** `llm-wiki-routine-v2.1.md` lines 545-567.

**Current Hireui state:** No promotion criteria for anything. `.cm/memory/learnings.json` is `[]` — no schema for "candidate observation" → "confirmed pattern".

**Change proposed:** Adopt parallel structure for hireui's compound artifacts:
- **Decisions:** new → tentative (1 use) → established (2 uses) → canonical (3+ uses across different contexts)
- **Learnings:** observation → candidate → confirmed (after 2nd hit on same root cause)
- **Skills:** imported → invoked-once → battle-tested → core (used >5× in 30 days)

Each tier has criteria + audit trigger.

| Cost | Pros | Cons |
|------|------|------|
| 2h to define criteria for each compound artifact | Compounding becomes measurable | Bureaucracy if applied too early |
| 30 min/month review | Goodhart-resistant (criteria check, not metric chase) | Hard to define "use count" without telemetry |
| Requires audit cadence (Concept 8) | Promotes vs retires explicitly | Risk of "everything is candidate forever" |

**Verdict:** 🟡 MEDIUM PRIORITY — defer until learnings.json has 10+ entries. Today: not urgent.

---

### Concept 8: Mini-audit vs full audit cadence

**Source:** `llm-wiki-routine-v2.1.md` lines 498-541.

**Current Hireui state:** No audit cadence. Weekly/monthly review is undefined.

**Change proposed:** Adapt KJ OS audit ratios to hireui:
- **Trigger 1:** weekly check on `.cm/memory/learnings.json` count
- **Trigger 2:** when learnings ≥ 20 → mini-audit (30-60 min): re-classify, retire stale, promote ready
- **Trigger 3:** when learnings ≥ 50 OR ratio (open/closed) > 2:1 → full audit (1-2h): comprehensive review
- **Hard block:** when deferred items ≥ 10 → no new harness work until cleared

| Cost | Pros | Cons |
|------|------|------|
| 30-60 min/audit | Prevents accumulation cliff | Easy to skip when "things are fine" |
| 0 if no triggers hit | Forces explicit debt management | Cadence overhead for low-volume projects |
| 1h once to define triggers | KJ OS proven across 67 sessions | Ratios may not transfer 1:1 to code project |

**Verdict:** 🟡 MEDIUM PRIORITY — schema first (Concept 7), then cadence layered on. Defer 30 days.

---

### Concept 9: OBSERVATION-TRACK sub-category

**Source:** `llm-wiki-routine-v2.1.md` lines 627-644.

**Current Hireui state:** No way to record one-off observations (e.g., "watchman crashed on 2026-05-06") that aren't reusable patterns. They either get committed-as-decisions (overweight) or lost in chat (underweight).

**Change proposed:** Add `.cm/memory/observation-track.json` for episodic events:
- Event-based (specific incident, not reusable architectural choice)
- Retained for monitoring, not promotion
- Reclassify to architectural candidate if 2+ similar incidents

Examples for hireui:
- Watchman 4.9.0 hang event (2026-05-06) — observation, not pattern (until 2nd hang)
- Specific HIR-1149 chain (PR #632 → #633 → 0d07c5a8) — observation
- Claude Code MCP cwd discovery (2026-05-06) — observation

| Cost | Pros | Cons |
|------|------|------|
| 1h to set up file + schema | Captures episodic learning without forcing pattern-fit | Yet-another-JSON to maintain |
| 5 min/incident to log | Reclassification path when patterns emerge | Could blur with learnings.json |
| 30 min/month review | Honest signal about what's truly recurring vs one-off | Risk: dump-everything → noise |

**Verdict:** 🟢 LOW-MEDIUM PRIORITY — useful but not urgent. Add when learnings.json becomes ambiguous.

---

### Concept 10: Goodhart's law correction (streak/parity as downstream metric, NOT target)

**Source:** `llm-wiki-routine-v2.1.md` lines 222-230.

**Current Hireui state:** Already exposed today. Chased "41/41 anspace skill parity" as target → imported marketing skills (cm-ads-tracker, cro-methodology) inappropriate for B2B recruitment SaaS. KJ OS hit identical pattern at session 66 (v55 streak preservation via cautionary-contrast framing).

**Change proposed:** Add explicit anti-pattern section in CLAUDE.md:

> **Goodhart's law: any metric that becomes a target loses meaning.**
> Anti-patterns to challenge:
> - "Hit X/X parity with [reference]" (parity is downstream, not target)
> - "Maintain 0-failure streak on hooks" (streak is downstream of correct work, not target)
> - "Always commit cleanly" (cleanliness is downstream of small commits, not enforce-via-bypass)
>
> When a metric is being optimized as primary goal, STOP and ask: "what's the underlying value this metric is supposed to measure?"

| Cost | Pros | Cons |
|------|------|------|
| 5 min to write anti-pattern section | Surfaces metric corruption early | Hard to spot in real-time |
| 0 ongoing | Trains discipline to question targets | Can be over-applied (every metric becomes "Goodhart" excuse) |

**Verdict:** ✅ HIGH PRIORITY — already manifested in 1 day. Document while example is fresh.

---

### Concept 11: Stream-timeout resume protocol

**Source:** `llm-wiki-routine-v2.1.md` lines 647-659.

**Current Hireui state:** Today's `harness-clone-mobile.sh` is 730 lines / 10 steps — completed in single Bash run. But future complex sessions (e.g., 4-hour Phase 1 Auth implementation across 7 files) will hit timeout / context limits / interruptions.

**Change proposed:** Define hireui resume protocol:
1. After interruption, agent reads `.cm/CONTINUITY.md` for current state
2. Reads `git status` + `git log -10` for actual disk state
3. Cross-references against last `.cm/traces/sessions/...md` if exists
4. Proposes resume plan with: (a) completed work to skip, (b) remaining work, (c) verification steps

| Cost | Pros | Cons |
|------|------|------|
| 1h to define protocol | Resilience to interruption | Won't matter until first long session |
| 5 min per resume | Saves 30-60 min per resume avoided redo | Complex to encode well |

**Verdict:** 🟡 MEDIUM PRIORITY — defer until first interruption-incident.

---

### Concept 12: Fact-verification protocol (pre-commit / pre-write)

**Source:** `llm-wiki-routine-v2.1.md` lines 475-489 + `_patterns/05-recent-additions.md` lines 73-79 (audit-layer fact-verification 2× corpus history).

**Current Hireui state:** Today: hook ran tsc → 9 errors → block → 1h confusion. KJ OS pattern: re-verify numbered references BEFORE Phase 6 (commit/write).

**Change proposed:** Add pre-commit verification skill (callable via slash command or auto-invoked):
- Verify all referenced HIR-tickets exist (Jira API or local cache)
- Verify all file paths in commit message exist
- Verify gitnexus_impact analysis was run for any function/class edit (auto-check git diff)
- Verify CONTINUITY.md mentions current branch (consistency check)

| Cost | Pros | Cons |
|------|------|------|
| 2-4h to build skill | Catches silent assumption errors | Adds friction to every commit |
| 10 sec/commit | Fact-verification proven 2× in KJ OS corpus to catch errors | Some checks need external services (Jira) |

**Verdict:** 🟡 MEDIUM PRIORITY — start with manual checklist in CLAUDE.md, automate later.

---

### Concept 13: Skill lock policy (PUBLIC-ARCHIVED vs IN-FLUX)

**Source:** `SKILL_LOCK_POLICY.md` lines 11-53.

**Current Hireui state:** All 41 imported skills are status-unknown. No way to tell which are "use this" vs "historical reference" vs "experimental".

**Change proposed:** Apply 3-tier classification:
- 🔒 **PUBLIC-ARCHIVED:** anspace-original skills not yet adapted for hireui (e.g., cm-ads-tracker for marketing)
- 🟢 **IN-FLUX:** actively maintained for hireui (e.g., link-expo-router, refactor-mobile-ui)
- 🟡 **EXPERIMENTAL:** untested in hireui context (most Priority C+D imports)

Add header to each `.claude/skills/<skill>/SKILL.md`:
```markdown
# [Skill Name]
📍 **Status:** EXPERIMENTAL (imported from anspace 2026-05-06 / not yet hireui-adapted)
```

| Cost | Pros | Cons |
|------|------|------|
| 2h to classify 41 skills | Operator + Claude both know which to invoke | Bureaucracy |
| 5 min/skill to add header | Surfaces dead-weight skills (Priority D scoring) | Status drift if not maintained |
| Annual re-classification | Foundation for skill-effectiveness-scoreboard later | Risk: "EXPERIMENTAL forever" |

**Verdict:** 🟢 LOW PRIORITY — defer until first 5 skills are battle-tested. Then classify all.

---

### Concept 14: Vault state architecture — chapter file convention

**Source:** `CLAUDE.md` (vault root) lines 36-59 + `PATTERN_LIBRARY.md` lines 35-77.

**Current Hireui state:** `.cm/CONTINUITY.md` is single file. `MOBILE_SETUP_PLAN.md` is single 345-line file. Neither has chapter convention. Hireui will hit context-thrashing trajectory KJ OS hit at 584KB / ~146K tokens.

**Change proposed:** Define `.cm/_state/` chapter file convention NOW (before files grow):
- Root `.cm/CONTINUITY.md` becomes shim (~5KB max)
- Bulk state moved to `.cm/_state/` chapters: each <35K tokens (≈ 35K chars)
- Numbered chapters: `01-current-focus.md`, `02-active-blockers.md`, `03-recent-decisions.md`, `04-session-history.md`
- Reading discipline: never read >1 chapter per session (KJ OS proven rule)

Same convention for MOBILE_SETUP_PLAN.md eventually:
- `MOBILE_SETUP_PLAN.md` (root, shim)
- `_plan/01-context-and-goals.md`, `_plan/02-architecture.md`, `_plan/03-phases.md`, etc.

| Cost | Pros | Cons |
|------|------|------|
| 1h to define convention + script | Prevents 6-month-from-now refactor crisis (KJ OS hit 584KB before refactoring) | Premature for current size |
| 0 if files stay small | Future-proof | Adds indirection for trivial reads |
| Adds split-script for automated chapter generation | Empirically validated by KJ OS session 67 | Operator must maintain authoritative-state-pointer |

**Verdict:** 🟡 MEDIUM PRIORITY — define convention today, apply lazily when files cross 30KB. Cheap insurance.

---

## Prioritization Matrix

| # | Concept | Priority | Cost | Pros | When to do |
|---|---------|----------|------|------|------------|
| 1 | Constitutional Invariants | 🔴 HIGH | 30 min | Single auth anchor, --no-verify cure | Today |
| 5 | Mandatory next-action closing | 🔴 HIGH | 0 (habit) | Universal cumulative effect | Today |
| 10 | Goodhart's law correction | 🔴 HIGH | 5 min | Document while example fresh | Today |
| 2 | Phase 0 pre-flight checklist | 🔴 HIGH | 30 min once | Prevents 50%+ mid-session "oh no" moments | This week |
| 4 | Always-produce-dated-artifact | 🔴 HIGH | 30 min/session | Compounding learning | This week (start with today's session log) |
| 6 | Operator backlog discipline | 🔴 HIGH | 1h setup + 5min/session | Sentry rotation security risk | This week |
| 14 | Vault state architecture | 🟡 MED | 1h once | Future-proof | This month (define, apply lazy) |
| 7 | 5 structural-promotion criteria | 🟡 MED | 2h | Compounding becomes measurable | When learnings ≥10 |
| 8 | Mini/full audit cadence | 🟡 MED | 1h once | KJ OS proven across 67 sessions | After Concept 7 |
| 12 | Fact-verification protocol | 🟡 MED | 2-4h | Catches silent-assumption errors | After 1 more incident |
| 11 | Stream-timeout resume protocol | 🟡 MED | 1h | Resilience | After first interruption |
| 3 | Read-only target boundary | 🟡 MED | 30 min | Prevents accidental prod break | When agent-dev touches src/ |
| 9 | OBSERVATION-TRACK sub-category | 🟢 LOW | 1h | Captures episodic learning | When learnings.json ambiguous |
| 13 | Skill lock policy | 🟢 LOW | 2h | Operator clarity | After 5 skills battle-tested |

---

## Recommended rollout — 4 days

### Day 1 (today, 1.5h)

Execute the 3 🔴 HIGH "today" items:

1. **Concept 1** — Draft `CONSTITUTION.md` with 5-7 hireui-specific invariants (30 min)
2. **Concept 5** — Add mandatory "Next Action" template to root CLAUDE.md (5 min)
3. **Concept 10** — Add Goodhart's law anti-pattern section to root CLAUDE.md with today's 41/41 example (10 min)
4. **Generate today's session iteration log** as proof of Concept 4 (45 min)

### Day 2-3 (this week, 2h)

Execute the 3 🔴 HIGH "this week" items:

1. **Concept 2** — Codify Phase 0 pre-flight checklist as `.claude/skills/cm-pre-flight/SKILL.md` (30 min) + `.cursor/skills/cm-pre-flight/SKILL.md` mirror
2. **Concept 4** — Set up `_bmad-output/sessions/` template (15 min)
3. **Concept 6** — Add `deferred_count` schema to `.cm/memory/decisions.json`; rebuild current backlog with counts (1h)

### Day 4 (this month, 1h)

Execute Concept 14 — define chapter convention, apply lazily:

1. Document `.cm/_state/` chapter convention in CLAUDE.md (15 min)
2. Define MOBILE_SETUP_PLAN.md split convention (15 min)
3. Write `scripts/split-to-chapters.sh` helper (30 min) — call when file >30KB

### Deferred (this quarter)

Concepts 7, 8, 12, 11, 3, 9, 13 — execute when triggers fire (defined per concept above).

---

## Cost Summary

| Tier | Total cost (one-time) | Total cost (ongoing) | Cumulative session-time saved (est.) |
|------|----------------------|----------------------|--------------------------------------|
| Day 1 (3 HIGH "today") | 1.5h | 0 | ~30 min/session × 30 sessions = **15 hours/month** |
| Day 2-3 (3 HIGH "this week") | 2h | 5 min/session | ~30 min/session × 30 sessions = **15 hours/month** |
| Day 4 (Concept 14 setup) | 1h | 0 | Prevents ~10h refactor crisis at month 6 |
| **Investment Day 1-4** | **4.5h** | **5 min/session** | **30+ hours/month** + crisis-avoidance |

ROI: ~6× in first month, compounding thereafter.

---

## Pros & Cons of Adopting v2 (vs Sticking with v1)

### Pros (adopting v2)

1. ✅ Each concept has explicit cost — no "we'll figure it out" hand-waving
2. ✅ Prioritized by trigger condition, not arbitrary timeline
3. ✅ Cites KJ OS empirical evidence (not theory)
4. ✅ Acknowledges deferred items rather than ignoring them
5. ✅ Day-1 actions are 1.5h total — committed before context loss
6. ✅ Documents Goodhart's law BEFORE the next metric-chase incident

### Cons (adopting v2)

1. ❌ More to read (this doc is 600+ lines vs v1's 411)
2. ❌ Some concepts (audit cadence, structural-promotion) are over-engineered for hireui's current scale
3. ❌ Risk of "harness-on-harness-on-harness" infinite regress if every concept becomes its own skill
4. ❌ KJ OS context is wiki-building (different domain); some concepts may not transfer cleanly
5. ❌ Cost estimates assume continuity of operator attention — may be optimistic

### Mitigations

- Re-read v2 as a reference (not commitment) — pick 3-5 concepts maximum to actually adopt
- Re-evaluate after 30 days; retire concepts that haven't paid off
- Keep CLAUDE.md additions short (paragraphs, not pages)

---

## Cross-references

- **v1 evaluation:** `(C) 2026-05-06 hireui harness evaluation + best practices.md` (sibling file)
- **Source skill (constitutional invariants):** `05 Skills/(C) project-code-analysis-harness.md`
- **Source skill (phased workflow):** `05 Skills/llm-wiki-routine-v2.1.md`
- **Source skill (skill lock policy):** `05 Skills/SKILL_LOCK_POLICY.md`
- **Source skill (interview pattern):** `05 Skills/brain-setup.md`
- **Pattern Library shim:** `PATTERN_LIBRARY.md` (vault root)
- **Pattern Library audit history:** `_patterns/01-audit-history.md`
- **Real harness report (anspace):** `03 Projects/product/anspace-harness/reports/(C) 2026-04-23-code-analysis-harness-report.md`
- **Hireui repo:** `/Users/Cvtot/monorepo/hireui` (commit `faf83dc1` on `agent-dev` at write-time)
- **Hireui CLAUDE.md (root):** `/Users/Cvtot/monorepo/hireui/CLAUDE.md`

---

## Metadata

- **Generated:** 2026-05-06 (same-day update to v1)
- **Generator session:** Claude Code, hireui session 3b284a0a-9880-4df4-8301-1c3a5781b409
- **Document length:** ~610 lines
- **Verdict confidence:** Higher than v1 — based on 9 source files (vs v1's general impression)
- **Source-verification:** All 14 concepts cite specific files + line numbers in KJ OS Template
- **Authoritative state:** This is a proposal, not commitment. Operator decides per concept.

---

## 🎯 Suggested Next Action

**Pick 3 concepts from Day 1 list (Concepts 1, 5, 10) to commit to TODAY** — total cost 45 min for the 3 + 45 min for today's session log = 1.5h. Lowest-cost / highest-leverage subset. Defer the rest pending re-evaluation in 30 days.

If only 1 concept can be done today: **Concept 5** (mandatory next-action closing) — costs 0, applies to every future response, accumulates passively.
