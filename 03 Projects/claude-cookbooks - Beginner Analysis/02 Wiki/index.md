# anthropics/claude-cookbooks — Wiki index (v102)

**Subject**: [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)
**Description**: "A collection of notebooks/recipes showcasing some fun and effective ways of using Claude."
**Wiki built**: 2026-05-28 (routine v2.3.1)
**Tier**: T1 Assistant Skill / Foundational-vendor reference cookbook
**Phase 0.9 verdict**: STRONGEST INCLUDE 4/4 with (a)(c) STRONGEST + (b)(d) STRONG
**(a)-7 status**: N=4 STRONGER POST-PROMOTION STRENGTHENING (4th Anthropic-direct-org subject)

---

## Quick facts (verified GitHub API 2026-05-28)

- **Owner**: Anthropic PBC (foundational vendor; (a)-7 cluster)
- **Created**: 2023-08-15 (~1,017 days at fetch)
- **Last push**: 2026-05-28 (today; actively maintained)
- **Stars**: 44,481 (~43.7/d sustained-moderate multi-year)
- **Forks**: 5,100 | **Watchers** (subscribers): 558 | **Open issues**: 212
- **License**: MIT
- **Primary language**: Jupyter Notebook
- **Default branch**: main
- **Repo rename observation**: Internal README links reference `anthropics/anthropic-cookbook` (legacy URL); current repo is `anthropics/claude-cookbooks` = repo was renamed from singular to plural at some point in lifecycle

---

## 12-domain cookbook taxonomy

1. **`capabilities/`** — Classification + RAG + Summarization
2. **`claude_agent_sdk/`** — Claude Agent SDK cookbook
3. **`coding/`** — Coding-specific cookbook
4. **`extended_thinking/`** — Extended Thinking feature cookbook
5. **`finetuning/`** — Fine-tuning cookbook
6. **`managed_agents/`** — Managed Agents API cookbook
7. **`misc/`** — Misc utilities + recipes
8. **`multimodal/`** — Vision cookbook (Claude Sonnet vision capabilities)
9. **`observability/`** — Observability + cost-tracking patterns
10. **`patterns/`** — Agentic-design patterns (`agents/` subdir)
11. **`tool_evaluation/`** — Tool evaluation cookbook
12. **`tool_use/`** — Tool use + integration cookbook
13. **`third_party/`** — Third-party integrations (Pinecone + Wikipedia + Voyage AI + ...)

**Plus skills/ directory** (6th implementer in agentskills.io standard chain; see Pattern #57 sub-variant 57k below).

---

## Corpus-recursive ties (cross-references to other wikis)

### (a)-7 Foundational-Vendor-Direct-Source cluster
- **v92** [claude-for-legal](../../anthropics-claude-for-legal%20-%20Beginner%20Analysis) (anchor; 2026-05-23)
- **v93** [anthropics/skills](../../anthropics-skills%20-%20Beginner%20Analysis) (N=2 STRENGTHENING; 2026-05-23)
- **v95** [claude-plugins-official](../../anthropics-claude-plugins-official%20-%20Beginner%20Analysis) (N=3 PROMOTION; 2026-05-25)
- **v102 claude-cookbooks (THIS WIKI)** (N=4 STRONGER POST-PROMOTION STRENGTHENING)

### Pattern #57 sub-variant 57k Standards-Conformance-Layer Chain (6-implementer)
- v76 HoangNguyen0403/agent-skills-standard (anchor; 2026-05-19)
- v93 anthropics/skills (authoritative reference; 2026-05-23)
- v98 mukul975/Anthropic-Cybersecurity-Skills (2026-05-25)
- v99 manaflow-ai/cmux (2026-05-27)
- v100 tisfeng/Easydict (2026-05-27)
- **v102 anthropics/claude-cookbooks (6th implementer; THIS WIKI)** — extends 5-implementer chain at v100 to 6-implementer at v102; 6-implementer-in-9-calendar-days arc-velocity

### uv tooling at corpus subjects (N=3)
- v79 autoresearch_folktales (uv-exclusive packaging)
- v97 distill (uv + Bun hybrid)
- **v102 claude-cookbooks (uv tooling + uv.lock + uv.toml)** — confirms uv-as-emerging-standard

### Library-vocab #12 LLM-routing artifacts (CONFIRMED N=5+)
- Root `CLAUDE.md` + `.claude/`
- `skills/CLAUDE.md` + `skills/.claude/`
- 4-artifact presence at single subject (continues strengthening)

---

## Phase 4b PRIMARY: Pattern #57 57k N=4 STRONGER post-PROMOTION strengthening

See: [Phase 4b PRIMARY proposal-document](../01%20Analysis/(C)%20Pattern-57-57k-6-implementer-N4-STRONGER-post-PROMOTION-strengthening.md)

**Summary**: 6-implementer agentskills.io chain extension with **Anthropic-direct-org INTRA-chain doubling** (v93 anthropics/skills SPEC+TEMPLATE-team + v102 anthropics/claude-cookbooks COOKBOOK+USAGE-team = NEW corpus-novel observation; two-role foundational-vendor implementation discipline).

---

## Phase 4b SECONDARY observations (held at OC layer; not registered to avoid graveyard pressure)

1. **NEW Library-vocab "12-Domain Cookbook Recipe Coverage at Foundational-Vendor-Direct-Source Scale"** PROVISIONAL N=1 — CORPUS-FIRST 12-domain coverage at cookbook-format Anthropic-direct-org subject
2. **NEW Library-vocab "Jupyter-Notebook-Primary at Foundational-Vendor-Direct-Source Subject"** PROVISIONAL N=1 — CORPUS-FIRST within (a)-7 cluster
3. **NEW Library-vocab "registry.yaml registry artifact at single subject"** PROVISIONAL N=1 — CORPUS-FIRST in v60+ window
4. **NEW Library-vocab "authors.yaml authors-metadata artifact"** PROVISIONAL N=1 — CORPUS-FIRST in v60+ window
5. **uv tooling N=3 STRENGTHENING** (v79 + v97 + v102; promotion-eligible at N=3 administrative)
6. **Repo-rename event observational note** (`anthropic-cookbook` → `claude-cookbooks`) — observational only; not corpus-record
7. **Possible NEW Pattern #52 sub-class candidate "MULTI-YEAR-SUSTAINED-MODERATE-LOW"** (25-60/d × 1000+d) — NOT REGISTERED (would worsen Pattern #52 sub-class graveyard)
8. **`anthropic_cookbook/` legacy directory at top-level** = repo-history-complexity observational note

---

## Pilot recommendation

**Tier**: HIGH-RELEVANCE pilot Tier-1 actionable
**Cost-of-trial**: **MINIMUM-LOW** (`git clone https://github.com/anthropics/claude-cookbooks.git` ~1-2 min for read-only browse; ~5 min for executable trial via `uv sync --all-extras`)
**Reversibility**: MINIMUM (`rm -rf claude-cookbooks/`)
**Direct-applicability**: DIRECT for vault-relevant cookbook domains (`patterns/agents/` + `claude_agent_sdk/` + `extended_thinking/` + `managed_agents/` + `observability/` + `coding/`)

**Pilot ranking insertion at position #6** (after v100 Easydict #5; pushing Anthropic-Cybersecurity-Skills v98 from #6 → #7):
1. Understand-Anything v94 (DIRECT vault-utility methodology-influence)
2. claude-plugins-official v95 (MINIMUM cost-of-trial; already-installed-by-default)
3. distill v97 (CLI-pipe compression utility)
4. cmux v99 (DIRECT multi-session AI-agent orchestration)
5. Easydict v100 (Vietnamese ↔ English translation utility)
6. **claude-cookbooks v102 NEW** (canonical Anthropic-authoritative cookbook patterns for daily Claude Code workflow)
7. Anthropic-Cybersecurity-Skills v98 (methodology-extraction read-only) — DISPLACED
8. claude-comstyle v87 (communication-style composition) — DISPLACED

**Recommended pilot trial path** (~10-15 min hands-on):
- `git clone https://github.com/anthropics/claude-cookbooks.git`
- Browse `patterns/agents/` (agentic patterns reference)
- Browse `extended_thinking/` (Extended Thinking patterns)
- Browse `managed_agents/` (Managed Agents API patterns)
- Browse `observability/` (cost-tracking + observability patterns for intensive Claude Code usage)
- Browse `skills/custom_skills/` (agentskills.io implementation reference)
- Reversible: `rm -rf claude-cookbooks/`

**Methodology-influence Tier-1-special multi-track position #5 NEW** (extends v92 #1 + v93 #2 + v94 #3 + v95 #4 to v102 #5).

---

## Storm Bear streak (post-v102 ship)

**34 PASS (v65-v83 + v85-v100 + v102) + 1 OVERRIDE (v84) = "34+1*"** NEW CORPUS-RECORD (first 15-consecutive milestone post-v84 OVERRIDE; extends v100's 14-consecutive milestone by 1)

**36-instance window v65-v102** = 35 PASS + 1 OVERRIDE = **97.2% INCLUDE rate** (uptick from v100's 97.14%)

**Strength categorization v65-v102**: STRONGEST × 15 + STRONG × 13 + MODERATE × 4 + WEAK × 5 + OVERRIDE × 1 (STRONGEST extends lead; v102 = 15th STRONGEST in window)

**Override-frequency**: 1-in-36 well below v2.3 redesign trigger thresholds (2-in-20 / 3-in-30)

---

## Audit-cadence runway

- v101 audit (2026-05-28) cleared 3-consecutive-1-WIKI-DEFERRAL CRITICAL threshold via QUADRUPLE PROMOTION + audit-only session
- v102 = FIRST ship post-v101 audit; clean audit-cadence runway
- v105 = natural-cadence audit window projected at +3 wikis from v102 (~v105 = 2026-05-31 if same daily cadence continues, but likely staggered with operator self-pacing)
- v105 batch projection: ~20-25 items (v102 ~5-8 + v103-v104 carryovers + spillover from v101 ~12) = HEALTHY post-promotion-cycle baseline
