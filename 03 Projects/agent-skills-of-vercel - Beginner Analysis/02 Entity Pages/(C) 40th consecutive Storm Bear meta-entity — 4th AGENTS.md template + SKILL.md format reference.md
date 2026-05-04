# (C) Entity Page — 40th Consecutive Storm Bear Meta-Entity

**Type:** Storm Bear vault meta-entity
**Streak:** 40 consecutive wikis with Storm Bear meta-entity (v10-v51 inclusive; first since v10 Karpathy meta-peak)
**Built:** 2026-04-25 — first wiki post-corpus-half-century-milestone (v50)
**Cross-refs:** awesome-claude-skills v50 (39th consecutive Storm Bear meta) / aidevops v47 (Pattern #22 22c — 3rd of 4 AGENTS.md templates) / gh-aw v48 (Pattern #22 22a monolithic — 1st of 4 AGENTS.md templates) / spec-kit v17 (Pattern #22 22a constitutional governance — also 1st of 4 templates) / multica v15 (forward-citation source — Pattern #57 57c) / 05 Skills/llm-wiki-routine-v2.1.md (vault routine itself; SKILL.md format reference target)

---

## 1. Per-wiki applicability check (v2.1 Phase 0.9)

**APPLICABLE — 40th consecutive Storm Bear meta-entity.** Frame as:
1. SKILL.md format template for vault `05 Skills/` directory expansion (HIGH direct utility)
2. 4th AGENTS.md template added to vault CLAUDE.md refactor reference ensemble (HIGH direct utility)
3. Pattern #57 57c forward-citation-then-wiki sub-variant external validity signal (META-OBSERVATIONAL)
4. Pattern #17 variant 5 N=3 default-criterion strengthening as ecosystem-scale platform reference (HIGH observational)

## 2. Direct utility #1 — SKILL.md format reference for vault `05 Skills/`

**Current state of vault `05 Skills/` directory:**

```
05 Skills/
├── (C) project-code-analysis-harness.md
├── brain-setup.md
├── llm-wiki-ingest.md
├── llm-wiki-routine-v2.1.md  ← most-invoked skill
├── llm-wiki-routine-v2.md
├── llm-wiki-routine.md
├── new-project.md
└── weekly-update.md
```

**8 skills, all prose markdown, NO YAML frontmatter. NO trigger phrases. NO on-demand loading semantics. NO version metadata.**

### Vercel SKILL.md format applied to vault skills (proposed)

**Current `llm-wiki-routine-v2.1.md` head:**
```
# Skill: LLM Wiki Routine v2.1

> **Type:** Orchestration meta-skill (Routine pattern)
> **Version:** v2.1 — consolidated from ~205 cumulative action items across v3-v31
> **Codified:** 2026-04-22
> **Supersedes:** llm-wiki-routine-v2.md
> **Parent skill:** llm-wiki-ingest.md
> **Sibling refs:** PATTERN_LIBRARY.md
```

**Proposed Vercel-style SKILL.md head:**
```yaml
---
name: storm-bear-llm-wiki-routine-v2-1
description: |
  Build a structured wiki page for an open-source agent framework or related project.
  Use when the user says "LLM wiki for <URL>", "routine for <topic>", "build wiki on <repo>",
  or asks to ingest a GitHub repo into the Storm Bear vault corpus.
  Triggers on tasks involving WebFetch + 12-axis classification + Pattern Library pre-check
  + 7-phase autonomous workflow (Phase 0 through Phase 6).
license: MIT
metadata:
  author: storm-bear
  version: '2.1'
  parent_skill: llm-wiki-ingest
  supersedes: llm-wiki-routine-v2
---

# Skill: LLM Wiki Routine v2.1

> Type: Orchestration meta-skill (Routine pattern)
> ...
```

**Benefits of Vercel-style SKILL.md adoption:**
1. **On-demand loading** — only YAML frontmatter loads at startup; full body loads when triggered
2. **Trigger-phrase activation** — agent matches user input against verbatim trigger phrases declared in description
3. **Per-skill versioning** — `metadata.version` formalizes the supersession chain
4. **Per-skill license metadata** — formalizes IP framing per skill
5. **`argument-hint` field** — vault routines could declare expected argument shapes (e.g., GitHub URL pattern)

### Pilot proposal (Storm Bear pilot #1 NEW)

**Pilot:** Convert `llm-wiki-routine-v2.1.md` to Vercel-style SKILL.md format as proof-of-concept. Estimated effort: 30-60 min. Compatibility: Claude Code natively reads YAML frontmatter; should work without breaking current invocation.

**Decision:** OPERATOR — pilot reduces vault skill management overhead long-term but adds short-term refactoring. Recommended after v27 diagnostic HIGH bundle (where vault CLAUDE.md refactor would naturally trigger 05 Skills/ refactor).

**Storm Bear pilot ranking refresh post-v51:**

| # | Pilot | Source | Estimated effort | Direct utility |
|---|---|---|---|---|
| 1 | rowboat v1 vault pilot | rowboat v43 | 4 weeks | Knowledge-graph-as-Markdown for Storm Bear vault |
| 2 | claude-hud install | claude-hud v35 | 5 min | Statusline visibility for context budget |
| 3 | spec-kit methodology adoption | spec-kit v17 | 1-2 weeks | SDD for Scrum workflows |
| 4 | claude-howto self-onboarding | claude-howto v32 | 13h weekend | Skill fluency |
| 5 | OMC multi-runtime | oh-my-claudecode v27 | 1 weekend | Cross-runtime ergonomics |
| 6 | pi-mono coding agent alt | pi-mono v36 | 2-4h | Claude Code alternative |
| 7 | aidevops AGENTS.md template adoption | aidevops v47 | 6-8h | 22c authoritative-with-shim hierarchy |
| **8 NEW** | **Vercel SKILL.md format adoption (vault `05 Skills/`)** | **Vercel v51** | **30-60 min single-skill pilot; 3-4h full vault** | **Per-skill YAML + on-demand loading** |
| 9 | claude-code-best-practice 82-tip aggregation | claude-code-best-practice v34 | reference for vault refactor | Tip catalog template |
| 10 | claude-context vault-indexing | claude-context v40 | 2-3h | Semantic search ($0.005 setup) |

## 3. Direct utility #2 — 4th AGENTS.md template added to vault refactor reference ensemble

**v27 diagnostic HIGH item #1 (vault CLAUDE.md refactor) — 30 sessions deferred (BLOCKING-RECOMMENDATION 6× threshold)**

**Current vault root `CLAUDE.md`:** 3,295 lines (per `/usr/bin/wc -l` 2026-04-25). Single monolithic file, accreted across v1-v50 wiki entries + v27 diagnostic + Pattern Library state lines.

**Vault refactor problem:** Single-file is now ~3,300 lines and continues to grow (~30-50 lines per new wiki entry). Unsustainable; needs structural intervention.

**4-template reference ensemble for refactor decision (post-v51):**

### Template 22a Monolithic single-source

**Anchors:**
- gh-aw v48 — 49.8KB single AGENTS.md, corporate-official, ~1,400 lines
- spec-kit v17 — constitutional governance + 9-articles methodology framing

**Vault application:** Keep CLAUDE.md as single source of truth; aggressive consolidation via deduplication / sectioning / archival of older wiki entries.

**Pros:** Single search target; no cross-file consistency burden
**Cons:** Continues to grow; eventual size becomes loading-cost issue

### Template 22b Minimum-viable shim

**Anchor:** bizos v37 — CLAUDE.md is 11-byte `@AGENTS.md` redirect

**Vault application:** Probably not viable for Storm Bear (vault CLAUDE.md is the single source-of-truth; nothing to redirect to).

### Template 22c Authoritative-with-shim 3-layer hierarchy

**Anchor:** aidevops v47 — Layer 0 [CLAUDE.md 440B + AGENT.md 420B shims] / Layer 1 root AGENTS.md 3KB / Layer 2 .agents/AGENTS.md 18KB

**Vault application:** Most-aligned with vault scaling needs. Layer 0 (vault CLAUDE.md as ~500-byte shim pointing to layer 1) / Layer 1 (root vault.md or VAULT.md ~2KB session-overview) / Layer 2 (per-section files in `01 ... / 02 ... /` etc.). Hierarchical scaling addresses growth problem.

**Pros:** Scales structurally; clean separation of concerns
**Cons:** Multi-file consistency burden; harder to grep across

### Template 22d Identical-mirror (NEW v51)

**Anchor:** Vercel v51 — AGENTS.md = CLAUDE.md byte-identical 3,281-byte files

**Vault application:** Probably not viable for Storm Bear (no need for AGENTS.md in vault; CLAUDE.md is canonical for Claude Code; AGENTS.md duplicate would create 2× storage with no benefit).

**However:** 22d demonstrates that "zero-divergence-risk via duplication" is a valid architectural choice when both files must be present. Validates that operator can choose duplication over reconciliation if drift-risk outweighs storage cost.

### Recommendation post-v51

**Most likely viable for vault:** 22c authoritative-with-shim (aidevops v47) for hierarchical scaling.
**Alternative:** 22a monolithic (gh-aw v48 / spec-kit v17) with aggressive consolidation.
**Less likely:** 22b shim (no obvious source-of-truth to redirect to) or 22d identical-mirror (no need for both files).

**Operator decision pending — 30 sessions and counting.**

## 4. Direct utility #3 — Pattern #57 57c forward-citation-then-wiki external validity signal

**multica v15** wiki entry cited `vercel-labs/agent-skills` as a dependency import 36 wikis BEFORE Storm Bear vault built v51 wiki of vercel-labs/agent-skills.

**Significance:** This is the **first observed corpus-selection-validation across ~36 wikis of separation**. multica v15 author (independent of Storm Bear vault) selected vercel-labs/agent-skills as notable enough to import into a skill-locked dependency manifest. That selection retroactively validated by Storm Bear's selection of vercel-labs/agent-skills as v51 wiki subject.

**Implication:** Storm Bear corpus-selection discipline is converging with broader agent-ecosystem judgment. Independent validation of selection criteria (without explicit collaboration).

**Pattern #57 57c registered N=1 stale-flagged at v51.** +5 v56 / +10 v61 review cadence. Promotion-candidate at structural-N=2 if 2nd forward-citation-then-wiki observation emerges.

## 5. Direct utility #4 — Pattern #17 variant 5 N=3 default-criterion as Storm Bear archetype reference

If Storm Bear vault ever publishes a public asset (Scrum coaching framework, Claude Code workflow, etc.), Pattern #17 variant 5 ecosystem-scale commercial platform provides one archetype reference:

| Variant 5 anchor | What they did | Storm Bear analog |
|---|---|---|
| HuggingFace v26 | Built ecosystem (Hub + Transformers + Datasets + Spaces) → educational layer (agents-course) | Storm Bear could build coaching framework → educational layer (Scrum tutorials) |
| Microsoft v28 | Built corporate IT ecosystem → utility layer (markitdown for AI agents) | Storm Bear could build Scrum coaching framework → utility layer (e.g., retrospective-templates skill) |
| Vercel v51 | Built developer platform (Next.js + Cloud) → skill layer (vercel-labs/agent-skills) | **Storm Bear could build Scrum coach platform → skill layer (Scrum-coach-skills repo)** |

**Aspirational; far from current vault state.** Reference archetype for if vault ever scales to public asset publication.

## 6. Storm Bear pilot relevance verdict

**MEDIUM-HIGH overall** — primarily SKILL.md format reference + 4-template AGENTS.md ensemble milestone

**Specific pilot proposals:**

1. **MEDIUM-HIGH (immediate):** Convert `llm-wiki-routine-v2.1.md` to Vercel-style SKILL.md format as proof-of-concept (30-60 min)
2. **MEDIUM (deferred):** Add to v27 diagnostic HIGH item #1 vault refactor decision — 22d identical-mirror NOT recommended for vault (no need for both files)
3. **OBSERVATIONAL ONLY:** Pattern #17 variant 5 archetype reference (aspirational; far from current state)
4. **OBSERVATIONAL ONLY:** Pattern #57 57c external validity signal (no actionable decision)

## 7. Storm Bear meta-entity 40-streak observation

**v10 Karpathy → v50 awesome-claude-skills → v51 Vercel = 42 wikis spanning Storm Bear meta-entity inclusion.**

**Streak preservation rate:** 40 of 42 wikis (95%) — only 1-2 wikis between v10 and v51 had no meta-entity (v23, v24 — based on prior CLAUDE.md state notation observed in vault).

**v2.1 Phase 0.9 per-wiki applicability check is consistently PASS** because:
- Most agent-framework wikis reveal vault-architectural lessons (governance / format / distribution)
- Most are pilot candidates at some priority
- Most have observational pattern relevance

**Forward-looking:** v52+ wikis likely to continue Storm Bear meta-entity inclusion as long as topic selection biases toward agent ecosystem (which it does).

## 8. Cross-references mandatory ≥3

This entity references:
1. **awesome-claude-skills v50** — corpus-half-century milestone; immediate predecessor in Storm Bear meta-entity streak
2. **aidevops v47** — Pattern #22 22c authoritative-with-shim 3-layer hierarchy; primary candidate for vault CLAUDE.md refactor template
3. **gh-aw v48** — Pattern #22 22a monolithic 49.8KB; alternative refactor template
4. **spec-kit v17** — Pattern #22 22a + constitutional governance; methodology framing reference
5. **multica v15** — Pattern #57 57c forward-citation source (cited "Vercel agent-skills import (first)" 36 wikis pre-v51)
6. **HuggingFace agents-course v26** — Pattern #17 variant 5 1st structural-N=2 anchor
7. **Microsoft markitdown v28** — Pattern #17 variant 5 2nd structural-N=2 anchor
8. **Pattern Library** (PATTERN_LIBRARY.md) — patterns #17 variant 5 / #22 / #57 / #29 / #50 / #59 / #19 / #27 / #2 / #18

## 9. Pattern Library impact (this entity contributes)

| Pattern | Action |
|---|---|
| #22 22d identical-mirror | NEW sub-variant N=1 stale-flagged; 4th AGENTS.md template added to vault refactor reference ensemble |
| #57 57c forward-citation-then-wiki | NEW sub-variant N=1 stale-flagged; external validity signal for corpus-selection discipline |
| #17 variant 5 | N=3 default-criterion strengthening (4 wikis × 3 tiers post-v51) |

End of Storm Bear meta-entity.
