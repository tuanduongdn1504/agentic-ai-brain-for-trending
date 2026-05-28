# Phase 0 + Phase 0.9 INCLUDE verdict — anthropics/claude-cookbooks (v102)

**Date**: 2026-05-28
**Routine**: v2.3.1 (CURRENT)
**Audit-cadence context**: FIRST ship post-v101 quadruple-promotion audit; clean audit-cadence runway after v101 cleared the 3-consecutive-1-WIKI-DEFERRAL CRITICAL threshold

---

## Phase 0 Decision-gating

**Subject**: `anthropics/claude-cookbooks` = Anthropic-direct-org repository hosting Jupyter notebook cookbooks/recipes for the Claude API + Claude Agent SDK + Skills + Managed Agents

**Decision-gate**: AUTOMATIC INCLUDE — Anthropic-direct-org subject triggers (a)-7 Foundational-Vendor-Direct-Source PASS per routine v2.3.1 §25 (a)-7 sub-axis (CONFIRMED at v96 audit).

**Phase 0 scale-floor verification**:
- License declared: MIT ✅
- Recent push activity: 2026-05-28 (today; actively maintained) ✅
- ≥1★: 44,481 stars ✅
- Phase 0 PASS

---

## Repo metadata (verified GitHub API 2026-05-28)

| Field | Value |
|---|---|
| Repo | `anthropics/claude-cookbooks` |
| Description | "A collection of notebooks/recipes showcasing some fun and effective ways of using Claude." |
| Created | 2023-08-15 |
| Last push | 2026-05-28 (today) |
| Age | ~1,017 days (~2.78 years) |
| Stars | 44,481 |
| Forks | 5,100 |
| Watchers (subscribers; true) | 558 |
| Stargazers (legacy "watchers") | 44,481 |
| Open issues | 212 |
| Primary language | Jupyter Notebook |
| License | MIT |
| Topics | (empty) |
| Default branch | main |
| Has Discussions | false |
| Has Wiki | true |
| Repo size | 207,347 KB (~207 MB) |
| Stars/day | **~43.7/d** = SUSTAINED-MODERATE-HIGH sub-class (25-150/d) sustained over multi-year window = corpus-novel multi-year-sustenance below Pattern #52 LONG-SUSTAINED-MEDIUM (60-150/d × 1000+d) floor |

**Velocity observation**: 43.7/d × 1017d = sustained-moderate-low at multi-year window. Below LONG-SUSTAINED-MEDIUM 60/d floor but at SUSTAINED-MODERATE-HIGH band with unusual age. Possible NEW Pattern #52 sub-class candidate "MULTI-YEAR-SUSTAINED-MODERATE-LOW" (25-60/d × 1000+d) if N=2 emerges; PROVISIONAL OBSERVATION at v102 — not registered to avoid Pattern #52 sub-class graveyard.

**Repo rename observation**: README internal links reference `anthropics/anthropic-cookbook` (old name); current repo is `anthropics/claude-cookbooks`. **Repo was renamed from `anthropic-cookbook` (singular) to `claude-cookbooks` (plural)** at some point in repo lifecycle. CORPUS-FIRST repo-rename observational note at foundational-vendor-direct-source subject.

---

## Top-level structure (32 directories/files at root)

**12-domain cookbook taxonomy** (Jupyter-notebook-primary):
1. `capabilities/` — Classification + RAG + Summarization
2. `claude_agent_sdk/` — Claude Agent SDK cookbook
3. `coding/` — Coding-specific cookbook
4. `extended_thinking/` — Extended Thinking feature cookbook
5. `finetuning/` — Fine-tuning cookbook
6. `managed_agents/` — Managed Agents API cookbook
7. `misc/` — Misc utilities + recipes
8. `multimodal/` — Vision cookbook
9. `observability/` — Observability/cost-tracking cookbook
10. `patterns/` — Agentic-design patterns (only `agents/` subdir at fetch)
11. `tool_evaluation/` — Tool evaluation cookbook
12. `tool_use/` — Tool use + integration cookbook
13. `third_party/` — Third-party integrations (Pinecone + Wikipedia + Voyage AI + ...)

**LLM-routing artifacts (Library-vocab #12 CONFIRMED N=5+)**:
- `CLAUDE.md` (root project-level)
- `.claude/` directory (CC integration)
- `skills/` directory + `skills/CLAUDE.md` + `skills/.claude/` (NEW 6th implementer in agentskills.io chain; extends Pattern #57 57k from N=5-implementer to N=6-implementer post-PROMOTION at v101)

**Build/tooling artifacts**:
- `uv.toml` + `uv.lock` (uv tooling — joins v79 + v97 prior corpus-uv-users)
- `pyproject.toml`
- `Makefile`
- `.pre-commit-config.yaml`
- `lychee.toml` (link checker artifact)
- `tox.ini` (testing artifact)
- `requirements-dev.txt`

**Registry/metadata artifacts**:
- `registry.yaml` (registry artifact; CORPUS-FIRST registry.yaml at single subject in v60+ window)
- `authors.yaml` (authors metadata file; CORPUS-FIRST authors.yaml in v60+ window)

**Legacy/migration artifact**:
- `anthropic_cookbook/` (top-level directory; possibly legacy from pre-rename `anthropic-cookbook` repo era)

---

## Phase 0.9 STRICT INCLUDE 4/4 verdict

### (a) Operator-cultural-peer / 7-axis taxonomy evaluation

**Applicable sub-axis**: **(a)-7 Foundational-Vendor-Direct-Source** (PROMOTED to formal (a) sub-axis at v96 audit; routine v2.3.1 §25 codified).

**(a)-7 4-criteria evaluation**:

| Criterion | Evidence | Verdict |
|---|---|---|
| 1. Owner is foundational-vendor org itself | `anthropics/*` primary GitHub org; Anthropic PBC owner | ✅ PASS |
| 2. Subject's product layer is upstream of operator's typical work | Cookbook for Claude API + Agent SDK = directly upstream of Storm Bear's daily Claude Code usage | ✅ PASS |
| 3. Methodology-influence source-authoritative | Anthropic-authoritative cookbook = DEFINES canonical patterns for Claude API + Agent SDK + Skills + Managed Agents | ✅ PASS |
| 4. Subject at foundational-vendor's primary GitHub org | `github.com/anthropics/claude-cookbooks` = primary org | ✅ PASS |

**4-of-4 PASS = (a) STRONGEST verdict**

**(a)-7 cluster strengthening at v102**:
- v92 claude-for-legal (anchor; 2026-04-21)
- v93 anthropics/skills (N=2 STRENGTHENING; 2026-05-23)
- v95 claude-plugins-official (N=3 PROMOTION-LOCKED-IN at v96 audit; 2026-05-25)
- **v102 claude-cookbooks (N=4 STRONGER POST-PROMOTION STRENGTHENING; 2026-05-28)**

= **(a)-7 N=4 STRONGER POST-PROMOTION STRENGTHENING** — administrative-only at v105 audit (no further promotion needed; (a)-7 already PROMOTED at v96; v102 = first strengthening evidence post-promotion).

### (b) Vault-deployability + cost-of-trial

**Cost-of-trial**: **MINIMUM-LOW** (`git clone https://github.com/anthropics/claude-cookbooks.git` ~1-2 min + selectively browse Jupyter notebooks; no install required for read-only browsing; `uv sync --all-extras` ~5 min for executable trial)

**Reversibility**: MINIMUM (`rm -rf claude-cookbooks/` single command)

**Direct-applicability**: **DIRECT** for multiple vault-relevant cookbook domains:
- `patterns/agents/` — agentic patterns directly applicable to vault routine
- `claude_agent_sdk/` — Agent SDK patterns for Claude Code workflow
- `extended_thinking/` — Extended Thinking patterns for vault analysis
- `managed_agents/` — Managed Agents API patterns
- `observability/` — Observability + cost-tracking patterns for intensive Claude Code usage
- `coding/` — Coding-specific cookbook directly relevant to Storm Bear's software-developer day-job
- `tool_use/` — Tool use patterns for vault tool ecosystem
- `skills/` — agentskills.io standard implementation reference (6th implementer)

**Existing-infrastructure-overlap**: HIGH (Storm Bear uses Claude Code daily; cookbook patterns directly applicable)

**(b) verdict**: **STRONG PASS** (MINIMUM-LOW cost-of-trial × DIRECT-applicability × HIGH existing-infrastructure-overlap; STRONG not STRONGEST because cookbook is reference-material not single-action-pilot like v100 Easydict 3-5-min brew install).

### (c) Methodology-influence-node

**Anthropic-authoritative cookbook** = canonical source for Claude API + Agent SDK + Skills + Managed Agents methodology. Highest possible methodology-influence-source within (a)-7 Foundational-Vendor-Direct-Source cluster.

**Methodology-influence axes**:
1. **12-domain cookbook taxonomy** — CORPUS-FIRST 12-domain coverage at foundational-vendor-direct-source cookbook-format subject in v60+ window (capabilities + claude_agent_sdk + coding + extended_thinking + finetuning + managed_agents + misc + multimodal + observability + patterns + tool_evaluation + tool_use + third_party)
2. **Jupyter Notebook primary** — CORPUS-FIRST Jupyter-Notebook-primary at foundational-vendor-direct-source subject in v60+ window (vs prior (a)-7 cluster: v92 Python+Shell + v93 Python+HTML+Shell+JS + v95 NULL-root-with-per-plugin)
3. **skills/ directory** — extends agentskills.io chain to 6th implementer (Pattern #57 sub-variant 57k post-CONFIRMED at v101 N+1 STRENGTHENING)
4. **patterns/agents/ subdir** — agentic-design patterns reference at foundational-vendor scale
5. **registry.yaml + authors.yaml** — CORPUS-FIRST registry + authors metadata artifacts at single subject

**(c) verdict**: **STRONGEST PASS** — Anthropic-authoritative cookbook + 12-domain coverage + canonical patterns source.

### (d) Corpus-recursive

**Corpus-recursive evidence**:
1. **(a)-7 cluster N=4 STRONGER STRENGTHENING** — 4th Anthropic-direct-org subject (v92 + v93 + v95 + v102)
2. **Pattern #57 sub-variant 57k 6-implementer agentskills.io chain** — N=4 STRONGER POST-PROMOTION STRENGTHENING (5-implementer at v101 → 6-implementer at v102; CORPUS-FIRST agentskills.io chain extension to 6th implementer at FOUNDATIONAL-VENDOR-DIRECT-SOURCE subject = unusual since v76 anchor was third-party not Anthropic-direct-org)
3. **Pattern #84 84d.4** — possibly extends if claude-cookbooks demonstrates native-macOS or substrate-tolerance evidence (NOT evident from notebook structure; SKIP)
4. **Library-vocab #12 LLM-routing artifacts** — continues strengthening (CLAUDE.md + .claude/ + skills/CLAUDE.md + skills/.claude/)
5. **uv tooling** — N=3 corpus-instance (v79 + v97 + v102; uv at foundational-vendor-direct-source subject confirms uv-as-emerging-standard observation)

**(d) verdict**: **STRONG PASS** — multiple corpus-recursive ties at established Patterns/Library-vocab; not STRONGEST because corpus-novel observations at v102 are extensions of already-PROMOTED items, not standalone corpus-firsts at recursion layer.

---

## Final verdict: STRONGEST INCLUDE 4/4 with (a)(c) STRONGEST + (b)(d) STRONG

**Strength categorization at v65-v102 window**: STRONGEST × 15 + STRONG × 13 + MODERATE × 4 + WEAK × 5 + OVERRIDE × 1

**Storm Bear streak**: 33 PASS (v65-v83 + v85-v100) + 1 PASS (v102) = **34 PASS + 1 OVERRIDE = "34+1*"** NEW CORPUS-RECORD (first 15-consecutive milestone post-v84 OVERRIDE; extends v100's 14-consecutive milestone by 1)

**Override-frequency**: 1-in-36 (further below v2.3 redesign trigger 2-in-20 + 3-in-30)

**36-instance window v65-v102 INCLUDE rate**: 35 PASS + 1 OVERRIDE = **97.2%** (precise 97.22%; uptick from v100's 97.14%)

**Audit-cadence runway**: v102 is first ship post-v101 audit; no audit-deferral pressure; v105 natural-cadence audit window projected at +3 wikis from v102.

---

## PHASE 4b PRIMARY candidate

**Primary proposal**: Pattern #57 sub-variant 57k Standards-Conformance-Layer Corpus-Recursive Chain N=4 STRONGER POST-PROMOTION STRENGTHENING via 6-implementer chain extension (claude-cookbooks = 6th implementer; ALL at Anthropic-direct-org or third-party-conformant subjects).

**Secondary observations**:
- (a)-7 N=4 STRONGER STRENGTHENING (administrative; no further promotion needed)
- ~5 NEW Library-vocab PROVISIONAL N=1 candidates (12-domain cookbook taxonomy + Jupyter-notebook-primary at foundational-vendor + registry.yaml + authors.yaml + uv tooling N=3)
- Possible NEW Pattern #52 sub-class candidate "MULTI-YEAR-SUSTAINED-MODERATE-LOW" (25-60/d × 1000+d) — NOT REGISTERED to avoid Pattern #52 sub-class graveyard
- Repo-rename event observational note (anthropic-cookbook → claude-cookbooks)

**Pilot recommendation**: HIGH-RELEVANCE pilot Tier-1 actionable position TBD (will displace claude-comstyle from #7 or insert at #6 between Easydict v100 #5 and Anthropic-Cybersecurity-Skills v98 #6).

**Cost-of-trial**: MINIMUM (`git clone` + selectively browse 12-domain cookbook); recommended IMMEDIATE pilot trial path = clone repo + browse `patterns/agents/` + `extended_thinking/` + `managed_agents/` notebooks for vault routine application (~10-15 min).

---

## Honest dissent / caveats

- **Repo-rename observation** (anthropic-cookbook → claude-cookbooks) is observational note not corpus-record; verifiable via internal README link patterns showing legacy URLs
- **Jupyter Notebook primary** at foundational-vendor = corpus-first within (a)-7 cluster but Jupyter Notebooks have appeared at other corpus subjects (v74 LLMs-from-scratch + others) so claim scope must be (a)-7-cluster-limited not v60+-window-limited
- **6-implementer agentskills.io chain at v102** strengthens existing Pattern #57 57k CONFIRMED but does not promote further (sub-variant already CONFIRMED at v101)
- **(a)-7 N=4 STRONGER STRENGTHENING** is administrative-only post-promotion at v96; not load-bearing audit decision at v105
- **`anthropic_cookbook/` legacy directory** at top-level suggests repo-history complexity worth documenting in v105 audit if structural-evidence reveals method-divergence pre-rename vs post-rename
