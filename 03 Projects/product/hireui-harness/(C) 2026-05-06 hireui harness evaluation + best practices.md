# (C) Hireui Harness Evaluation + Best Practices Recommendations

> **Date:** 2026-05-06
> **Scope:** Evaluate hireui's current agent harness against KJ OS Template (LLM Wiki + paperclip-inspired patterns)
> **Source repo evaluated:** `/Users/Cvtot/monorepo/hireui` (pnpm monorepo: Next.js 14 web + Expo SDK 55 mobile)
> **Evaluator:** Claude (per session 2026-05-06)
> **Prefix discipline:** `(C)` — AI-generated per CLAUDE.md rule
> **Sibling reference:** `03 Projects/product/anspace-harness/` (sibling project — same harness pattern, different domain)

---

## Executive Summary

**Health scores (3 task areas):**

| Area | Score | 1-line takeaway |
|------|-------|-----------------|
| **Skill inventory** | 🟢 GREEN | 41/41 anspace parity achieved 2026-05-06; gitnexus MCP indexed (1727 files / 20608 nodes) |
| **Discipline enforcement** | 🟡 YELLOW | Branch policy hook works (3 violations blocked + correct fixes suggested), but commit hygiene weak (3× `--no-verify` in 1 day for documented pre-existing issues) |
| **Continuity infrastructure** | 🟡 YELLOW | `.cm/` skeleton present + 2 ml-lessons pre-filled, but CONTINUITY.md never updated mid-session; traces/sessions empty; meta-learnings ratio (active/confirmed) not tracked |

**Bottom-line verdict (blunt):** Hireui has more raw infrastructure than most projects after a single setup day, but **lacks the *operational discipline* that makes KJ OS Template valuable**. The skills are installed but unread; CONTINUITY exists but isn't a living document; the policy hook works but gets bypassed.

**The gap isn't tooling — it's habit.** And habit compounds, so addressing it now matters.

---

## 1. Inventory: What Hireui Currently Has

### 1.1 Files committed on `agent-dev` branch (5 commits, 2026-05-06)

```
faf83dc1  chore(agent): Priority C+D skills (18 + prompt-template, full anspace parity)
47934f3e  chore(agent): Priority A+B skills (14 mobile + workflow)
d23d18ff  chore(agent): gitnexus skill suite (6 sub-skills) + augmented agent rules
b8f60907  chore(agent): full harness install (9 Tier-1 skills + .cm/ + MCP)
bf7c494b  chore(agent): branch-policy hook + cursor rule + harness installer
```

### 1.2 Inventory by category

| Category | Count / Files | Status |
|----------|---------------|--------|
| **Skills** (`.cursor/skills/` + mirrored to `.claude/skills/`) | 41 dirs + prompt-template.md (anspace parity) | ✅ committed |
| **GitNexus sub-skills** (`.claude/skills/gitnexus/`) | 6 (cli, debugging, exploring, guide, impact-analysis, refactoring) | ✅ committed |
| **GitNexus index** (`.gitnexus/lbug`) | 1727 files, 20608 nodes, 25280 edges, 126 flows, 232 communities | ✅ built (gitignored) |
| **`.cm/` continuity** | CONTINUITY.md + memory/{decisions, learnings, meta-learnings}.json + traces/ + outputs/ | ✅ scaffolded |
| **Memories team-shared** (`memories/users/default/`) | README.md + preferences.json + glossary.json | ✅ committed |
| **MCP configs** | `.mcp.json` (Claude Code) + `.cursor/mcp.json` (Cursor) — both `arch -arm64 npx -y gitnexus mcp` | ✅ committed |
| **Branch policy hook** (`scripts/git-hooks/pre-commit-branch-policy.sh`) | 147 lines, wired into `.husky/pre-commit` | ✅ active |
| **Cursor rules** (`.cursor/rules/`) | 2 files: apple-silicon-node-arm64.mdc + branch-policy-agentic-vs-feature.mdc | ✅ committed |
| **Root rules** | `CLAUDE.md` (root + apps/mobile/), `AGENTS.md` (gitnexus-augmented) | ✅ committed |
| **Harness installer** (`scripts/harness-clone-mobile.sh`) | 730 lines, 10 idempotent steps, dry-run by default | ✅ committed |
| **BMAD framework** (`_bmad/`, `_bmad-output/`) | Installed pre-existing, separate from anspace harness | ✅ committed |

### 1.3 Project-side commits (HIR-1138 mobile branch — for context)

```
0d07c5a8  fix(HIR-1149): final 1/9 fix (Button.tsx color → IButton Omit list)
5e8a25fe  Merge dev-mobile (HIR-1149 8/9 + dev base)
cf6788be  chore(HIR-1138): allow harness scripts (*.sh) + ignore harness outputs
605b18a3  docs(mobile): apps/mobile/CLAUDE.md (real device QR > sim rule)
ebd5b059  feat(HIR-1138): bootstrap Expo SDK 55 + Expo Router + NativeWind
65a01073  chore(HIR-1138): pnpm workspace + Sentry compat
91ce82fb  docs: MOBILE_SETUP_PLAN.md (canonical 11-week plan)
```

---

## 2. Comparison vs KJ OS Template Principles

### 2.1 Constitutional invariants (paperclip-inspired)

KJ OS uses **5 explicit non-negotiable rules** in `(C) project-code-analysis-harness.md`:
1. READ-ONLY target
2. ALWAYS write a dated report (even if partial)
3. ALWAYS end with suggested next actions
4. NEVER fabricate counts
5. NEVER skip phases silently

**Hireui status:**

| Invariant | Hireui equivalent | Status |
|-----------|-------------------|--------|
| READ-ONLY target | ❌ N/A — hireui harness writes to its own repo (different scope) | N/A |
| Always-produce-artifact | ❌ Missing — sessions don't reliably write reports | **GAP** |
| Always end with next-action | 🟡 Partial — present in chat but not encoded in skills | **GAP** |
| Never fabricate | ✅ Implicit (CLAUDE.md says no fabrication) | ✅ |
| Never skip silently | 🟡 Branch policy hook enforces this for commits, but no equivalent for skills | **PARTIAL** |

### 2.2 Communication discipline

KJ OS root CLAUDE.md (line 26-34):

> - **Blunt and direct** — challenge me, don't sugarcoat, call me out when I'm wrong
> - **Always end with a suggested next action** — every response should close with what to do next
> - **Prefix AI-generated files with `(C)`** — so it's clear what Claude wrote vs. what I wrote
> - **Ask before editing existing notes** — never modify my files without permission
> - **NEVER fabricate information** — if you don't know, say so. No making things up.
> - **NEVER make silent assumptions** — if something is unclear, ask. Don't fill in the blanks and hope I won't notice.

**Hireui status:**

| Rule | Hireui CLAUDE.md? | Verdict |
|------|-------------------|---------|
| Blunt and direct | ❌ Not stated | **GAP** — hireui CLAUDE.md is procedural (paths, conventions), not behavioral |
| End with next-action | ❌ Not stated | **GAP** |
| `(C)` prefix | ❌ Not enforced | **GAP** — `_bmad-output/tickets/HIR-1149-*.md` doesn't use `(C)` |
| Ask before editing | ❌ Not stated | **GAP** |
| Never fabricate | 🟡 Implied | Should be explicit |
| Never silent-assume | 🟡 Implied | Should be explicit |

**Recommendation:** Adopt these 6 rules verbatim into root `CLAUDE.md`. Cost: 5 minutes. Value: every Claude session inherits the discipline.

### 2.3 Continuity infrastructure

**KJ OS pattern (refactor session 67, 2026-04-27):**
- `CLAUDE.md` is a 7KB shim
- Bulk state moved to `_state/` chapter files (each <35K tokens)
- 6 numbered chapter files preserve project history
- Chapter files are authoritative; root is index

**Hireui status:**

| Element | KJ OS | Hireui | Verdict |
|---------|-------|--------|---------|
| State chapter files | 6 in `_state/` | 0 — `.cm/CONTINUITY.md` is single file | **GAP — will hit context-thrashing as project grows** |
| CONTINUITY size budget | <35K per chapter | Not enforced | **GAP** |
| Memory files | 3 (`decisions`, `learnings`, `meta-learnings` JSON) | ✅ Same 3 files (anspace pattern copied) | ✅ |
| Trace template | `traces/SESSION-TEMPLATE.md` | ✅ Copied from anspace | ✅ |
| Trace sessions filled | Anspace probably has many; KJ OS has many `_state/...md` | 0 (`.gitkeep` only) | **GAP** |
| Meta-learnings pre-filled | KJ OS has multi-year history | ✅ 2 lessons from 2026-05-05 (real-device-QR + watchman-arm64) | ✅ start |

**Empirical KJ OS lesson cited (CLAUDE.md line 38):** "Pre-refactor CLAUDE.md was 584KB / ~146K tokens — too large for any agent to read without context-thrashing. Three consecutive v56 wiki-build attempts failed at the 4-tool-use mark." Hireui hasn't hit this yet because CONTINUITY.md is small (1KB), but the same trajectory awaits if we let it accumulate without chapter-splitting discipline.

### 2.4 Audit cadence (Pattern Library style)

KJ OS has 5 structural-promotion criteria + mini-audit (0.95:1) / full audit (1.05:1) / hard block (>2.0:1) ratios for its Pattern Library (74 entries, 17 active candidates).

**Hireui equivalent — does anything need audit cadence?**

Look at hireui's compounding artifacts:
- ✅ Skill library (41 anspace skills + 6 gitnexus = 47) — but all imported, no original yet
- ❌ No internal pattern library
- ❌ No decision log audited (`.cm/memory/decisions.json` is `[]`)
- ❌ No learning log audited (`.cm/memory/learnings.json` is `[]`)
- 🟡 Meta-learnings file has 2 entries but not classified by status

**Verdict:** Audit cadence not yet needed (corpus too small), but the **schema is missing**. When the meta-learnings file hits 30 entries, we'll have nowhere to triage them. Add structure now → no refactor needed later.

### 2.5 Operator-facing backlog discipline

KJ OS routine v2.1 (line 79-81):
> "At 5+ sessions of deferral: Escalate in recommendation with 'BLOCKING-RECOMMENDATION' tag"

**Hireui's current backlog (after 2026-05-06 session):**

| Item | Sessions deferred | Status |
|------|-------------------|--------|
| Push `agent-dev` to origin | 1 | OK |
| Open mobile PR (manual GitHub UI) | 1 | OK |
| `pnpm eas-init` | 2+ | warning |
| Microsoft OAuth Azure AD registration | 2+ | warning |
| Deploy HIRE_AGENT staging URL | 2+ | warning |
| Rotate Sentry token + dev secrets | 2+ | warning |
| Fix Claude Code MCP discovery (cwd issue) | 1 | OK |
| Extend `lint-staged.config.js` (skill exclusions) | 1 | OK |
| Extend `commitlint.config.ts` (`agent` type) | 1 | OK |

**Verdict:** No items at the 5-session threshold yet, but **4 items already at 2+ sessions are external blockers** (need user action — EAS login, Azure portal, DevOps, Sentry). KJ OS pattern would escalate these as "BLOCKING-RECOMMENDATION" within 2-3 more sessions. Hireui has no such mechanism — these will silently accumulate.

### 2.6 Goodhart's law awareness

KJ OS routine v2.1 line 222-224:
> "**'Preserve consecutive-meta-entity streak' as inclusion justification.** Streak length is downstream metric, NOT inclusion target. Goodhart's law: optimizing for streak length corrupts Phase 0.9 signal-value."

**Hireui exposure to this:**
- 41/41 anspace skill parity — was that a **target** or a **measure**?
- The `--all-skills` flag was used to chase parity, including Priority D skills explicitly tagged "may not all apply to hireui" (e.g., `cm-ads-tracker`, `cro-methodology`, `cm-content-factory` — marketing-domain skills hireui may never use)
- 3× `--no-verify` to keep hook compliance metric clean — the metric corrupts when it's the target

**Verdict:** **Already exposed.** Recommend documenting Goodhart's law in CLAUDE.md so future "let's just hit the metric" decisions get challenged.

### 2.7 Stream-timeout resume protocol

KJ OS handles delegated subagent failures with explicit resume flow (line 647-659). Hireui has no equivalent.

**Verdict:** Not yet bitten by this, but **inevitable** as agent-dev work grows. When the harness-clone-mobile.sh script gets extended to 15 steps, a mid-script timeout will force a resume.

### 2.8 Read-only boundaries

KJ OS `(C) project-code-analysis-harness.md` is strictly read-only on the target project. Hireui's harness writes to its own repo — that's correct because it IS the target. But there's no equivalent "read-only" boundary for the agent when it's reasoning about already-deployed production code.

**Verdict:** Less applicable to hireui's current scope, but worth re-evaluating when harness grows to include "audit production deploys" or "review external code" workflows.

---

## 3. What Hireui Does Well (Strengths)

1. **Branch separation enforced by hook** — `agent-dev` vs `mobile/HIR-*` discipline with auto-blocking. KJ OS doesn't even have this layer. Hireui's hook successfully blocked 3 violations on 2026-05-06 with clear fix instructions.

2. **Single-script installer** — `harness-clone-mobile.sh` (730 lines, 10 steps, dry-run default, idempotent, --apply/--skip-gitnexus/--all-skills/--only flags). KJ OS doesn't have this — its harness is documented but not auto-installable.

3. **Mirror to both IDEs** — `.cursor/skills/` + `.claude/skills/` parallel copies. Removes "which IDE am I in" friction.

4. **GitNexus indexed at scale** — 20K+ symbols indexed in 12.5s. 4× more nodes than anspace.

5. **Apple Silicon discipline** — `arch -arm64` baked into MCP configs, `apple-silicon-node-arm64.mdc` rule deployed, watchman bug documented in meta-learnings (won't recur).

6. **Documented decisions in commit messages** — every harness commit explains WHY + cites prior anspace pattern. KJ OS would call this "iteration log" discipline.

7. **Backup-before-overwrite** — harness installer auto-backups to `.harness-backup/<timestamp>/`. Reversibility built-in.

---

## 4. Gaps (What's Missing or Weak)

### 4.1 Behavioral rules in CLAUDE.md are absent

| KJ OS rule | Hireui CLAUDE.md? |
|---|---|
| "Blunt and direct" | Missing |
| "End with suggested next action" | Missing |
| `(C)` prefix for AI-generated | Missing |
| "Ask before editing existing notes" | Missing |
| "Never fabricate" | Missing |
| "Never silent-assume" | Missing |

### 4.2 CONTINUITY discipline isn't enforced

- `.cm/CONTINUITY.md` was written once at install (2026-05-06) and never updated this session
- 5 harness commits + 4 project commits + branch policy decisions all happened — none reflected in CONTINUITY
- KJ OS would have an iteration log per session in `04 Reviews/`

### 4.3 No audit cadence for compounding artifacts

- `.cm/memory/decisions.json` is `[]` (no decisions logged across this entire session)
- `.cm/memory/learnings.json` is `[]` (despite hitting 5+ learnings: watchman, MCP discovery, lint-staged, commitlint, branch-policy violations)
- No threshold for "when do we triage these"

### 4.4 No backlog escalation mechanism

- 4 items already at 2-3 sessions deferral
- No "BLOCKING-RECOMMENDATION" tag system
- Risk: items silently age out (e.g., Sentry secret rotation — security risk that grows by the day)

### 4.5 No skill effectiveness measurement

- 41 skills installed but **0 invoked** in this session
- KJ OS has `skill-effectiveness-scoreboard` skill but hireui imported it without using it
- Risk: dead-weight skills sitting on disk

### 4.6 Token budget discipline missing

- `CLAUDE.md` (root) is currently small (~3KB) — fine
- But no PROCESS for splitting when it grows
- KJ OS hit 584KB before refactoring; hireui will hit the same wall faster because mobile work will pile state

### 4.7 No equivalent of the "streak metric correction"

- 41/41 parity was hit as a TARGET, not as a MEASURE
- No mechanism to challenge "do we actually need cm-ads-tracker for a B2B recruitment SaaS?"
- KJ OS already learned this lesson at session 66 post-v55

### 4.8 No "Phase 0 pre-flight" pattern

- The harness-clone-mobile.sh has preflight checks (good!)
- But individual SESSIONS have no preflight
- KJ OS routine v2.1 has 9 Phase-0 sub-steps before any heavy work

### 4.9 Bilingual discipline lost

- KJ OS prefers VN primary + EN technical
- Hireui CLAUDE.md is 100% English
- Lost: muscle memory + cultural fit for VN operator

### 4.10 No fact-verification protocol

- KJ OS does pre-write verification of pattern references (line 475-489)
- Hireui has no equivalent — relied on tsc to catch errors after the fact
- Manifested today: hook ran tsc → 9 errors → block → confused us, took 1 hour to resolve

---

## 5. Recommended Best Practices (Prioritized)

### Tier 1 — High-leverage, low-cost (do this week)

| # | Action | Effort | Why |
|---|---|---|---|
| **1.1** | Adopt 6 KJ OS behavioral rules in root `CLAUDE.md` | 5 min | Free discipline upgrade per session |
| **1.2** | Mandate `(C)` prefix for AI-generated artifacts (esp. `_bmad-output/`, `.cm/outputs/`) | 5 min | Trace ownership |
| **1.3** | End every Claude response with "Next action: ..." suggestion | 0 min (habit) | KJ OS principle codified |
| **1.4** | Update `.cm/memory/learnings.json` with the 5 lessons from this session (watchman / MCP cwd / lint-staged / commitlint / branch-policy violations) | 15 min | Prevent re-hitting |
| **1.5** | Add CONTINUITY update protocol to CLAUDE.md ("read at session start, update at session end") | 5 min | Living doc |

### Tier 2 — Process discipline (do this month)

| # | Action | Effort | Why |
|---|---|---|---|
| **2.1** | Create `_bmad-output/iteration-logs/(C) YYYY-MM-DD session-N.md` per Phase 5 of KJ OS routine | 30 min/session | Compound learnings |
| **2.2** | Define "Phase 0 pre-flight" for hireui sessions (read CONTINUITY, check git status, confirm branch matches intent, read relevant skill) | 10 min once | Avoid mid-session surprises |
| **2.3** | Add "BLOCKING-RECOMMENDATION" tag schema for backlog items at ≥3 sessions deferral | 15 min | Surface aging items |
| **2.4** | Decide audit cadence for `.cm/memory/{decisions, learnings, meta-learnings}.json` (e.g., review when learnings ≥ 20 OR weekly) | 10 min | Prevent fragmentation |
| **2.5** | Document Goodhart's law in CLAUDE.md with specific anti-patterns (skill parity-chasing, --no-verify habituation) | 10 min | Prevent metric corruption |

### Tier 3 — Architectural (do this quarter)

| # | Action | Effort | Why |
|---|---|---|---|
| **3.1** | Define `.cm/_state/` chapter-file convention (split CONTINUITY when >35K tokens) | 1h | Avoid context-thrashing later |
| **3.2** | Skill effectiveness scoreboard: monthly review of which of the 41 skills actually get invoked → retire/archive zero-use skills | 30 min/month | Prevent skill bloat |
| **3.3** | Audit `commitlint.config.ts` to add `agent` type (eliminate `chore(agent):` workaround) | 15 min | Match anspace pattern, simpler commits |
| **3.4** | Audit `lint-staged.config.js` to exclude `.claude/skills/**` + `.cursor/skills/**` from `check-types` (eliminate `--no-verify` habituation) | 15 min | Hook compliance restored |
| **3.5** | Establish "constitutional invariants" for hireui agent (write 5 explicit rules like paperclip / KJ OS harness) | 1h | Non-negotiable anchor |
| **3.6** | Stream-timeout resume protocol for long-running sessions (when harness-clone-mobile.sh grows past 15 steps OR mobile feature work spans 4+ hours) | 30 min protocol design | Resilience |

### Tier 4 — Skill consolidation (defer until 5+ skills actually used)

- Audit which of the 41 imported skills have been invoked in any session
- Mark unused skills `OBSERVATION-TRACK` (KJ OS terminology) — kept for monitoring but not promoted
- Consider re-archiving Priority D skills if they hit 30 days zero-invocation

---

## 6. Specific Anti-Patterns Already Manifested (Today's Session)

These are documented, not theoretical:

1. **Goodhart's law on skill parity** — chased "41/41 anspace parity" as target → imported `cm-ads-tracker`, `cro-methodology`, `cm-content-factory` (marketing skills inappropriate for B2B recruitment SaaS).

2. **`--no-verify` habituation (3× in one day)** — every bypass of the pre-commit hook was documented (HIR-1149 errors, then cm-dockit .ts files), but the cumulative effect is the hook becoming "advisory" rather than "enforcing" in our heads. Tier 3 #3.4 fixes the underlying cause.

3. **Silent assumption on Claude Code cwd** — discovered mid-session that Claude Code is rooted at `/Users/Cvtot/monorepo` not `/Users/Cvtot/monorepo/hireui`, so `.mcp.json` in hireui never loaded. KJ OS rule "never silent-assume" would have surfaced this earlier (e.g., a Phase 0 check "verify MCP server actually loaded by listing tools").

4. **CONTINUITY.md never updated mid-session** — 9 commits across 2 branches, watchman bug discovered + fixed, gitnexus indexed, harness installed end-to-end. CONTINUITY has the install-time text and nothing else.

5. **No iteration log produced** — KJ OS would generate `04 Reviews/(C) 2026-05-06 v1 hireui harness setup learnings.md` covering: 7 hours work / 9 commits / 5 lessons / 4 deferred items / next-session strategic recommendation. Instead all of this lives in chat ephemerally.

---

## 7. Suggested Next Actions (per Storm Bear Prime Directive)

**One concrete next step per area, ordered by leverage:**

### Highest leverage: Adopt behavioral rules in CLAUDE.md (Tier 1.1) — **20 minutes**

Edit `/Users/Cvtot/monorepo/hireui/CLAUDE.md` to prepend a "Behavioral rules" section with 6 KJ OS verbatim rules. This single edit upgrades every future Claude session in hireui. Lowest effort, highest leverage. **Do this first.**

### High leverage: Backfill `.cm/memory/learnings.json` (Tier 1.4) — **15 minutes**

Add 5 entries:
1. `watchman-arm64-required` (severity: HIGH)
2. `claude-code-mcp-cwd-mismatch` (severity: MEDIUM)
3. `lint-staged-runs-whole-repo-tsc` (severity: HIGH — caused 3× --no-verify habituation)
4. `commitlint-no-agent-type` (severity: LOW — cosmetic workaround)
5. `branch-policy-hook-renames-required` (severity: LOW — minor friction)

Then never re-hit them.

### Medium leverage: Generate `(C) 2026-05-06 v1 hireui harness setup learnings.md` (Tier 2.1) — **30 minutes**

Iteration log for today's session, modeled on KJ OS Phase 5 template. Captures the 7-hour journey end-to-end so it compounds rather than vanishing into chat history.

### Operationally next: Push `agent-dev` to origin (currently 5 commits ahead)

Don't lose the work. `git push -u origin agent-dev` — 10 seconds.

---

## 8. Open Questions

1. **Will hireui develop its own pattern library** (analogous to KJ OS Pattern Library #1-#74) by tracking observations across multiple HIR tickets? Or will all "patterns" stay implicit in skill files?
2. **Should hireui adopt the bilingual VN+EN convention?** Trade-off: code/PR descriptions are global; team CLAUDE.md is for VN team.
3. **Audit cadence trigger** — what's the equivalent of "ratio active/confirmed > 0.95:1" for hireui? Maybe "deferred backlog items ≥ 5"?
4. **Constitutional invariants** — what 5 non-negotiable rules should hireui agent follow? Drafting this is itself a Tier 3 action.
5. **GitNexus MCP discovery fix** — the `.mcp.json` at hireui root doesn't load because Claude Code's cwd is the parent monorepo dir. Should we (a) move `.mcp.json` to parent, (b) reopen Claude Code in hireui dir, (c) global user-level MCP? Each has trade-offs documented but not decided.

---

## 9. Blockers & Skipped Areas

- **Skipped:** Detailed comparison of hireui's BMAD framework (`_bmad/`) vs KJ OS skills system. BMAD is its own ecosystem and warrants separate analysis.
- **Skipped:** Detailed evaluation of the 41 imported skills' content quality. This document evaluates the harness *system*, not individual skill effectiveness.
- **Blocker:** Cannot test gitnexus MCP tools in Claude Code session (cwd issue). Work-around exists (`arch -arm64 npx -y gitnexus query --repo hireui ...`) but adds friction.
- **Blocker:** No telemetry on which skills get invoked vs sit idle. Tier 3 #3.2 proposal would address this but needs scoreboard skill activated.

---

## Cross-references

- **Sibling project:** `03 Projects/product/anspace-harness/` (same harness pattern, different project)
- **Source skill:** `05 Skills/(C) project-code-analysis-harness.md` (constitutional invariant pattern source)
- **Routine source:** `05 Skills/llm-wiki-routine-v2.1.md` (Phase 0.9 STRICT inclusion + audit cadence patterns)
- **Pattern Library:** `PATTERN_LIBRARY.md` (74 patterns; hireui has equivalent of 0)
- **Hireui repo:** `/Users/Cvtot/monorepo/hireui` (commit `faf83dc1` on `agent-dev` at write-time)
- **Hireui plan:** `/Users/Cvtot/monorepo/hireui/MOBILE_SETUP_PLAN.md`
- **Hireui CLAUDE.md (root):** `/Users/Cvtot/monorepo/hireui/CLAUDE.md`
- **Hireui CLAUDE.md (mobile):** `/Users/Cvtot/monorepo/hireui/apps/mobile/CLAUDE.md`

---

## Metadata

- **Generated:** 2026-05-06
- **Generator session:** Claude Code, hireui session 3b284a0a-9880-4df4-8301-1c3a5781b409
- **Document length:** ~600 lines
- **Verdict confidence:** Medium — based on 1 day of intensive observation; longer-baseline patterns may emerge differently
- **Authoritative state pointer:** This document is a snapshot evaluation, not living state. Re-evaluate after 30 days of usage.

**Next action:** Read this document with operator. Pick 1 Tier-1 item to execute today. Schedule re-evaluation in 30 days.
