# Vault Publishing Strategy — 2026-04-28 session 68

> **Status:** ✅ DECIDED (Phase 3 / v27 HIGH item #2 COMPLETE)
> **Builds on:** `_state/license-decision-2026-04-28.md` (MIT) + `_state/public-release-decision-2026-04-28.md` (whole-vault / NOW / GitHub+Anthropic / single-repo / Q5=G)

---

## Artifacts created at this phase

✅ `LICENSE.md` (vault root) — MIT license + AI-attribution notes (created in #5 phase)
✅ `AGENTS.md` (vault root) — 22c authoritative-with-shim template per v47 aidevops corpus reference
✅ `README.md` (vault root) — bilingual VN+EN; ~5KB; standard sections

## AGENTS.md decision rationale

**Template chosen: 22c authoritative-with-shim**

Rationale (from corpus 4-template ensemble per v53 mini-audit):

| Template | Source corpus | Why NOT chosen for Storm Bear |
|---|---|---|
| 22a monolithic | gh-aw v48 (49.8KB) | Vault uses chapter-file architecture; monolithic AGENTS.md would duplicate state across files |
| 22b minimum-shim | bizos v37 (327B) | Too sparse; Storm Bear has rich operator-context worth signaling to multi-runtime agents |
| **22c authoritative-with-shim** ✅ | **aidevops v47** | **Closest archetype: solo-multi-runtime + vault-as-knowledge-base** |
| 22d identical-mirror | vercel-labs v51 | Duplicates content unnecessarily; CLAUDE.md is already comprehensive |

**22c characteristics applied to Storm Bear:**
- AGENTS.md is **authoritative-as-shim** — short file pointing agents to CLAUDE.md as source-of-truth
- ~1.5KB content (less than gh-aw 49.8KB monolithic; more than bizos 327B minimum)
- Multi-runtime compatibility (OpenCode / Aider / Cursor / future agentic harnesses can read AGENTS.md)
- Avoids content duplication (no second source-of-truth to keep in sync)

## SKILL.md format compliance

**Skills published to Anthropic skills marketplace:**

1. `05 Skills/llm-wiki-routine-v2.1.md` — current; production-stable across 14+ executions
2. `05 Skills/brain-setup.md` — operator interview for CLAUDE.md generation
3. `05 Skills/new-project.md` — project scaffolding

**Format compliance:** Vercel-labs SKILL.md format (corpus reference v51) is the closest authoritative spec. Skills currently use vault-internal markdown convention; minor format reconciliation may be needed for Anthropic skills marketplace submission. Defer format-conversion to actual marketplace submission process.

**v1/v2 archived skills:** `llm-wiki-routine.md` (v1) + `llm-wiki-routine-v2.md` (v2) — archived as superseded; flagged "DO NOT USE" header at top of file (Phase 4 / item #3 skill-lock). NOT submitted to Anthropic marketplace.

## Distribution registry config

**Decision: NO `marketplace.json` at v56 launch.**

Rationale:
- Composio marketplace.json (v50 corpus reference) is for npm-distributed multi-skill packages
- Storm Bear is GitHub-public-repo first; npm package is NOT in Q3=F=A+C platform decision
- Anthropic skills marketplace submission process is independent of npm marketplace.json
- Future iteration: add `marketplace.json` if npm package path is added (deferred to post-Phase-4)

## Bilingual VN+EN README structure

**Sections (final):**
1. Title + tagline (bilingual)
2. What is this / Đây là gì (bilingual)
3. Who built / Ai xây (bilingual)
4. Scope + caveats / Phạm vi + lưu ý
5. Install (3 paths: clone / browse / copy-skills)
6. Use cases (4 audience segments)
7. Pattern Library overview (numerical state)
8. Skills catalog (5 skills inventory)
9. License (MIT pointer)
10. Contributing (no contributions yet — observational repo)
11. Repository topics (11 topics committed)
12. References (Karpathy / Anthropic / Obsidian / MIT)
13. Inspiration acknowledgments (lineage credits)
14. Project status (Phase 1 ✅ / Phase 2 🟢 exceeded / Phase 3 🟢 exceeded / Phase 4 in progress)

**Length:** ~5KB. Within corpus-typical T2/T4 README range.

## Anthropic skills marketplace submission (deferred)

**Process:** Research at pre-launch (within 1-2 weeks per Q2=A timeline). Steps:
1. Verify SKILL.md format compatibility (Vercel-labs v51 reference + Anthropic-imported skills in awesome-claude-skills v50)
2. Submit 3 skills (llm-wiki-routine-v2.1 + brain-setup + new-project)
3. Track submission status

**Operator action item:** Schedule 30-60 min for marketplace submission at pre-launch.

## Pattern Library impact

**Pattern #22 AGENTS.md Industry Standard** — Storm Bear vault enters corpus at 22c authoritative-with-shim sub-variant. **N=2 STRUCTURAL data point at sub-variant level** (joins aidevops v47 22c origin). This is consolidation-forward strengthening (no new candidate; routes to existing 22c sub-variant within already-confirmed Pattern #22).

**Pattern #57 Recursive Corpus Reference** — Storm Bear vault becomes self-referential corpus subject. README cites multiple corpus subjects (n8n / spec-kit / aidevops / claude-code / etc.) explicitly. Pattern #57 NEW sub-variant **57e meta-corpus-self-reference** candidate (vault publishes content ABOUT its own corpus). N=1 stale-flagged at this decision; await N=2 confirmation if Storm Bear becomes wiki subject in future corpus iteration.

**Pattern #19 archetype 4 individual-lineage** — Storm Bear vault explicitly cites 6+ lineage influences (Karpathy / Tiago Forte / John Lam / Lance Martin / Boris Cherny / SDD community) — corpus-typical at archetype 4 (no novel mechanism).

**No new standalone candidates registered.** **20-streak ZERO-NEW-ACTIVE-CANDIDATES preserved at session 68 mid-execution.**

## Pre-launch checklist status (Q5=G items)

| Item | Status |
|---|---|
| A) `(C)` prefix audit | ⏸ Deferred to pre-launch (within 1-2 weeks) |
| B) Anti-leak grep | ⏸ Deferred to pre-launch (within 1-2 weeks) |
| C) Don't-be-Chris-Porter cautionary checklist | ✅ COMPLETE — vault PASSES 7-point self-audit at decision time |
| D) AGENTS.md template choice | ✅ COMPLETE — 22c authoritative-with-shim chosen + AGENTS.md created |
| E) README.md polish | ✅ COMPLETE — bilingual VN+EN ~5KB created |
| F) Repository topics | ✅ COMPLETE — 11 topics committed in decision doc |

**Next operator action:** Execute Items A + B (anti-leak grep + (C) prefix audit) before `gh repo create --public`. ~30-60 min effort.

## Phase 3 outcome

**v27 HIGH item #2 (Publishing strategy formalization): COMPLETE** ✅

3 vault-root artifacts created:
- LICENSE.md (MIT)
- AGENTS.md (22c authoritative-with-shim)
- README.md (bilingual VN+EN)

Plus 3 decision-rationale chapter files in `_state/`:
- license-decision-2026-04-28.md
- public-release-decision-2026-04-28.md
- publishing-strategy-2026-04-28.md (this file)

**Next phase:** v27 HIGH item #3 (Skill-lock policy) — decide which skills are public-archived (lock) vs in-flux (continue evolving). Estimated 30-60 min.
