# (C) Phase 0 + Phase 0.9 INCLUDE verdict — nature-skills (v119)

**Routine:** v2.4. **Fetched:** 2026-05-29. **Verdict:** **STRONG INCLUDE 4/4** ((a) PASS + (b) MODERATE + (c)(d) STRONG). 3rd consecutive clean PASS after the v116 Sana OVERRIDE.

> ⚠️ **Audit-cadence flag:** v119 was the projected natural-audit window (~v119–v120) and v116–v119 = 4 wikis since the v115 audit. Shipping v119 per operator request defers the audit; **v120 = AUDIT strongly recommended** (queue: Pattern #18 #8 → N=3, Pattern #57 corpus-recursive N=2, LV-C7 N=3, T1 Domain-Vertical N=4, the affiliation-disclaimer N=2, agentmemory identity, 44-vs-45-PASS discrepancy, override-frequency).

---

## Phase 0 — scope gate

| Gate | Result |
|---|---|
| Repo reachable + readable | ✅ `Yuan1z0825/nature-skills` |
| License present | ✅ **MIT** (GitHub API `mit`) |
| Active / recently pushed | ✅ pushed 2026-05-29; created 2026-04-24 (~35 days) |
| Scale floor (≥1★) | ✅ **13,633★** |
| Tier classification | **T1 Assistant Skill / Domain-Vertical-Skill-Collection** (academic / scientific-publishing vertical; sibling v90) |

**Phase 0 = PASS.** Squarely in-scope: an agentskills.io implementer + Claude Code plugin with SKILL.md, `.claude/`, `.agents/plugins/`, and a bundled MCP server.

---

## Phase 0.9 — STRICT 4-criterion INCLUDE filter

### (a) Author cultural-peer to Storm Bear — **PASS (declared)**

Yuan Yizhe (袁一哲), **PhD student at Shanghai Jiao Tong University**, medical-AI research. China-Mainland is **declared/strongly-evidenced** (SJTU affiliation, recruitment email `sjtu520aimedws@163.com`, bilingual zh README, a Chinese-PPTX skill), not merely inferred — a firmer PASS than v117's community-signal inference. Extends the China-Mainland sub-cluster (v82+v83+v91+v94+v100+v117+**v119** = 7 by-event). No new (a) sub-axis (China-Mainland established). **(a) PASS.**

### (b) Goal-relevance / vault-utility — **MODERATE**

It is a Claude Code plugin (`/plugin install nature-skills`) — goal-adjacent, MINIMUM-cost, fully reversible. **But the domain — Nature-journal academic/scientific manuscript writing + figures — is not Storm Bear's vertical** (software development + Scrum coaching). He is not preparing Nature submissions. The genuine value is (i) a **skill-authoring reference model** (9-skill domain decomposition + plugin packaging + bundled MCP) and (ii) the bundled-MCP-server pattern. High install-reversibility × off-target domain = **MODERATE**, mirroring v98 cybersecurity (MEDIUM) and v114 gsap (MODERATE). Not inflated to STRONG.

### (c) Instructive / exemplary — **STRONG**

A clean reference for a domain-vertical skill bundle: nine well-scoped SKILL.md skills, status-levels (Draft/Beta/Stable), `references/` per skill, plugin-marketplace distribution across two harnesses, and a **bundled domain MCP server** (`nature-academic-search`: search_papers / get_paper_by_id / get_citation / lookup_mesh). Directly instructive for Storm Bear's own skill-authoring. **STRONG.**

### (d) Corpus connectivity — **STRONG**

- **agentskills.io 57k chain** — 11th implementer (post the 10-implementer reconciliation at the v2.4 consolidation).
- **T1 Domain-Vertical-Skill-Collection** (CONFIRMED N=3 at v101) — academic vertical, direct sibling to **v90 academic-research-skills** → N=4.
- **Affiliation-disclaimer Library-vocab N=2 with v98** (brand-named repo + "not affiliated" disclaimer).
- **Pattern #84 multi-harness** (Claude Code + Codex; `codex-skills` topic + `.agents/`).
- **Pattern #18 B1 MCP** (bundled server); China-Mainland cluster; Pattern #52 pulse; Pattern #19.

**(d) STRONG.**

---

## Verdict

| Criterion | Result |
|---|---|
| (a) cultural-peer | **PASS** (declared China-Mainland SJTU PhD; cluster → 7 by-event) |
| (b) goal-relevance / vault-utility | **MODERATE** (Claude Code plugin + skill-authoring study-value; domain off-vertical) |
| (c) instructive | **STRONG** (exemplary domain-vertical skill bundle + bundled MCP) |
| (d) corpus connectivity | **STRONG** (57k 11th impl + Domain-Vertical N=4 + affiliation-disclaimer N=2 + multi-harness + MCP) |

**STRONG INCLUDE 4/4** — no criterion fails; load-bearing on (c)(d) with (a) a firm declared PASS and (b) an honest MODERATE.

**Finding-2 calibration note:** (b) deliberately held at MODERATE (academic-writing domain is not the operator's work; install-reversibility alone doesn't make a niche bundle broadly applicable). Healthy rubric discrimination.

**Streak:** "46+2\*" → **"47+2\*"** (47 PASS + 2 OVERRIDE; v119 = 3rd consecutive clean PASS after the v116 Sana override). Pre-existing 44-vs-45-PASS discrepancy + 2-data-point override-frequency review remain flagged for the (now-due) audit.

**Pilot:** **CONDITIONAL (not Tier-1)** — `/plugin install nature-skills` is a MINIMUM-cost reversible trial, but only worth it IF academic/scientific writing enters the workflow. Otherwise a skill-authoring + bundled-MCP reference. Does NOT join the Claude-Code-adjacent operational stack (claude-mem / harness / humanizer / cclog-cli).
