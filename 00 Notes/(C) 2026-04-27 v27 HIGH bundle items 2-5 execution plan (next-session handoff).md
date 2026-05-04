# v27 HIGH Bundle Items #2-5 — Execution Plan

> **Status:** Approved 2026-04-27 session 67 by operator. Deferred to next session for clean context budget (session 67 burned through 5 agent-thrash retries + vault refactor + v56 ship + post-v56 mini-audit; ~6-8h of v27 HIGH work needs fresh `/clear` context).
>
> **Why now:** 36 sessions deferred = 7.2× routine v2.1 5-session threshold. Pattern Library is decisively NOT bottleneck (0.436:1 ratio preserved 6 cycles; 0.514 buffer; 13-candidate runway). Operator-facing-backlog is the overwhelming highest-ROI focus. Reference templates from v34-v56 are well-accumulated. v56 SUL-N=3 + Pattern #29 6-sub-context taxonomy makes license decision (#5) low-effort relative to backlog cost.

---

## Bundle scope (4 interdependent items)

**#2 — Storm Bear publishing strategy**
- When/whether to publish vault content (selective vs whole-vault)
- Public repo posture (separate publishing repo vs vault-as-repo)
- AI-attribution policy (already partially covered by `(C)` prefix rule)
- Skill catalog organization (use vercel-labs v51 SKILL.md format reference + composio v50 marketplace.json template)

**#3 — Vault skill-lock**
- Decide which `05 Skills/` definitions should be public-release-frozen vs in-flux
- Current skills: brain-setup / new-project / llm-wiki-routine.md (v1 superseded) / llm-wiki-routine-v2.md (v2 superseded) / llm-wiki-routine-v2.1.md (current; tightened session 66)
- Recommendation: lock v1 + v2 (superseded; archived); leave v2.1 in-flux pending v2.2 candidate refactor

**#4 — Public-release decision**
- WHAT gets released publicly: skills only? skills + pattern library? skills + selected wikis? whole vault?
- WHEN: now / Phase 4 mastery / never
- HOW: GitHub public repo / npm package / Anthropic skills marketplace / claude.ai project knowledge / Obsidian community plugin / multiple

**#5 — Vault license decision**
- Choose license that supports #2/#3/#4 decisions
- License taxonomy from v56 mini-audit Pattern #29 6-sub-context taxonomy:
  - **OSI-permissive** (MIT / Apache 2.0) — vercel-labs v51 / spec-kit v17 / many corpus precedents
  - **OSI-copyleft** (AGPL-3.0 / GPL) — bizos v37 / pi-mono v36 / others
  - **Custom-non-OSI-commercial-restriction** (SUL family / PolyForm) — omo v52 + GitNexus v33 + n8n v56 = corpus N=3 sub-context
  - **No-license / informal** (29-absent-1 through 29-absent-5) — bizos v37 / dive-into-llms v39 / awesome-claude-skills v50 / vercel-labs v51 / learn-coding-agent v53 / automate-faceless-content v55

**Item interdependencies:**
- #5 (license) is FOUNDATIONAL — determines what's possible for #2-4
- #4 (public-release) depends on #5 + influences #2/#3
- #2 (publishing strategy) depends on #4 + #5
- #3 (skill-lock) depends on #4 + influences #2

**Recommended execution order:** #5 → #4 → #2 → #3

---

## Reference templates accumulated (v34-v56)

| Template | Source wiki | Use for |
|---|---|---|
| 82-tip aggregation | v34 claude-code-best-practice | #2 publishing strategy |
| 327B minimum-viable AGENTS.md | v37 bizos | #3 skill-lock template |
| GREEN primitive-count | v44 spec-kit | #2 vault size discipline |
| 22c authoritative-with-shim | v47 aidevops | #2 vault structure (CLOSEST ARCHETYPE — solo-multi-runtime) |
| 49.8KB AGENTS.md | v48 gh-aw | #3 skill-lock content depth |
| 864-SKILL.md catalog | v50 awesome-claude-skills | #2 skill catalog organization |
| composio marketplace.json | v50 awesome-claude-skills | #2 distribution registry config |
| SKILL.md format spec | v51 vercel-labs | #3 skill format authoritative reference |
| 22d identical-mirror | v51 vercel-labs | #2 AGENTS.md ensemble option |
| don't-be-Chris-Porter checklist | v55 automate-faceless-content | #2/#5 anti-pattern guardrails |
| SUL-N=3 license-family + Pattern #29 6-sub-context taxonomy | v56 n8n + v56-mini-audit | #5 license decision framework |

**License decision framework from v56-mini-audit Pattern #29 6-sub-context taxonomy:**

```
                                     ┌─ 29-non-commercial-restriction-custom-license (SUL/PolyForm; N=3 STRUCTURAL)
                                     │   → omo v52 + GitNexus v33 + n8n v56
                                     │   → Allows internal-use; restricts hosting-as-service
                                     │   → Non-OSI; commercial-protective
                                     │
                ┌─ Custom non-OSI ────┤
                │                    │
                │                    └─ Other custom commercial-restriction variants
                │
Pattern #29 ────┤
                │                    ┌─ 29-absent-1 commercial-cold-start (bizos v37)
                │                    ├─ 29-absent-2 academic-public-welfare (dive-into-llms v39)
                │                    ├─ 29-absent-3 README-OSI-license-claim (awesome-claude-skills v50 + vercel-labs v51, N=2)
                │                    ├─ 29-absent-4 research-only-non-commercial-restriction (learn-coding-agent v53)
                │                    └─ 29-absent-5 commercial-content-creator-affiliate-funnel (automate-faceless-content v55)
                │
                └─ No-license/informal ┘ (5 absent-LICENSE sub-contexts; all N=1 stale-flagged or N=2 structural)
```

**Operator decision dimensions:**
1. Do I want commercial protection? (If yes → SUL family; if no → OSI-permissive)
2. Do I want public-release at all? (If no → no-license OK for purely-internal vault; if yes → must pick license)
3. Do I want copyleft / share-alike? (If yes → AGPL; if no → MIT / Apache)
4. Do I need geographic restrictions? (Q6 from v56 OPEN-QUESTIONS — not currently relevant)

---

## Suggested next-session execution (~4-6h compressed scope)

**Phase 1: License decision (#5) — ~60-90 min**

1. Operator interview (5 questions):
   - Q1: Do you intend to ever publish any vault content publicly?
   - Q2: If yes, do you want commercial protection (prevent others from monetizing your skills) or pure-permissive?
   - Q3: Do you want copyleft (derivatives must share alike) or permissive (no derivative restrictions)?
   - Q4: Do you have any AI-attribution requirements beyond `(C)` prefix?
   - Q5: Do you anticipate cross-licensing (vault as MIT + commercial subscription tier)?
2. Map answers to corpus license taxonomy (SUL / MIT / AGPL / no-license)
3. Draft LICENSE.md for vault root
4. Document decision rationale in `_state/license-decision-2026-04-XX.md` (new chapter)
5. Pattern Library impact: Pattern #29 sub-context Storm Bear instance enters corpus (vault becomes self-referential corpus subject — Pattern #57 sub-variant 57e candidate?)

**Phase 2: Public-release decision (#4) — ~60-90 min**

1. Decide release granularity (skills-only vs skills+patterns vs whole-vault)
2. Decide release timing (now vs Phase 4 vs never)
3. Decide release platform(s) (GitHub / npm / Anthropic skills / claude.ai / Obsidian community)
4. Document decision in `_state/public-release-decision-2026-04-XX.md`
5. If public-release approved: prepare separate `storm-bear-public/` working directory (clone-on-publish pattern, NOT public-vault)

**Phase 3: Publishing strategy (#2) — ~60-90 min**

1. Choose AGENTS.md template (22c authoritative-with-shim from v47 aidevops most-likely; matches Storm Bear solo-multi-runtime archetype)
2. Choose SKILL.md format (Vercel v51 spec — closest reference for vault skill ecosystem)
3. Choose distribution registry config (composio marketplace.json from v50 if Anthropic-skills-marketplace path chosen)
4. Apply don't-be-Chris-Porter cautionary checklist v55 to publishing artifacts
5. Document publishing strategy in `05 Skills/publishing-strategy.md` or `_state/publishing-strategy.md`

**Phase 4: Skill-lock (#3) — ~30-60 min**

1. Lock superseded skills: `llm-wiki-routine.md` (v1) + `llm-wiki-routine-v2.md` (v2) → archive with deprecation notice
2. Leave in-flux: `llm-wiki-routine-v2.1.md` (current; v2.2 refactor pending) + `brain-setup.md` + `new-project.md` (these continue evolving)
3. Document skill-lock policy in `05 Skills/SKILL_LOCK_POLICY.md`
4. If public-release approved Phase 2: tag v1 + v2 as "public-archived"; v2.1 + others as "in-flux-internal"

**Phase 5: Verification + integration — ~30 min**

1. Verify all decisions consistent across LICENSE / publishing / skill-lock / release
2. Update root CLAUDE.md "Vault State Architecture" section with new chapter file references
3. Update GOALS.md "Master Plan 4 Phases" — Phase 4 mastery items partially-complete
4. Commit v27 HIGH items #2-5 as PARTIAL-COMPLETE in next post-execution mini-audit

**Total estimated time:** 4-6h compressed scope. Could expand to 6-8h if license interview surfaces complex requirements (e.g., dual-license + CLA + DCO).

---

## Discipline mechanisms to apply

1. **Fact-verification protocol** — re-check license name + version + clauses + OSI status before commit
2. **Reference template direct citation** — cite specific v34-v56 templates rather than re-deriving
3. **Don't-be-Chris-Porter cautionary checklist** — applied to publishing artifacts
4. **Phase 0.9 STRICT criteria** — vault license decision becomes Storm Bear meta-entity input for all v57+ wikis (criterion d evidence: vault becomes self-referential corpus subject)

---

## Output artifacts (post-execution)

After v27 HIGH items #2-5 complete:
- `LICENSE.md` (vault root)
- `AGENTS.md` (vault root) per chosen template
- `_state/license-decision-2026-04-XX.md` (chapter)
- `_state/public-release-decision-2026-04-XX.md` (chapter)
- `05 Skills/publishing-strategy.md` (skill definition)
- `05 Skills/SKILL_LOCK_POLICY.md` (skill definition)
- Updated root CLAUDE.md / GOALS.md with new chapter pointers
- `04 Reviews/(C) 2026-04-XX v27 HIGH items #2-5 execution log.md` (audit trail)

---

## Suggested next-session opener (copy-paste-ready)

```
Execute v27 HIGH bundle items #2-5 per execution plan in 
"00 Notes/(C) 2026-04-27 v27 HIGH bundle items 2-5 execution plan 
(next-session handoff).md".

Order: #5 (license) → #4 (public-release) → #2 (publishing 
strategy) → #3 (skill-lock).

Start with operator interview: 5 license-decision questions.
```

---

## Why this is the right move now

1. **Library is decisively NOT bottleneck** — 0.436:1 ratio preserved 6 cycles; 0.514 buffer NEW LARGEST sustained 6 cycles; 13-candidate runway; 2-consecutive-CONSERVATIVE-DISCIPLINE mini-audits = pattern formalization is in steady-state harvest mode
2. **Backlog escalation is anomalous** — 36 sessions deferred = 7.2× threshold; routine v2.1 BLOCKING-RECOMMENDATION mechanism predictive but not actuating until session 67 partial v27-HIGH-#1
3. **Reference templates are well-accumulated** — v34-v56 inventory contains direct templates for every v27 HIGH item
4. **License decision framework is corpus-mature** — Pattern #29 6-sub-context taxonomy gives operator a structured decision tree
5. **Vault refactor session 67 demonstrates infrastructure-readiness** — chapter-file pattern established; new chapters can be added without bloat
6. **20-streak discipline is at its peak** — operator-discipline is firing well; right time to commit to high-leverage operator-facing-backlog work
7. **Storm Bear meta-entity legitimacy restored** — v56 STRICT amendment + 2-criteria-PASS + post-v56 audit Q1 resolution shows operator-discipline-restoration cycle is complete; ready for next-cycle operator-actionable work

The gravity has shifted from "library compounds" (decisively NOT bottleneck) to "operator-facing-backlog" (overwhelmingly highest-ROI for 36 sessions running).
