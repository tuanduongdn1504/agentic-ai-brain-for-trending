# (C) Phase 0 + Phase 0.9 INCLUDE verdict — gsap-skills (v114)

**Routine:** v2.3.1. **Fetched:** 2026-05-29.

---

## Phase 0 — scope gate

| Gate | Result |
|---|---|
| Repo reachable + readable | ✅ `greensock/gsap-skills` |
| License present | ✅ **MIT** (LICENSE file + GitHub API `mit` agree — clean; each SKILL.md frontmatter also `license: MIT`) |
| Active / recently pushed | ✅ pushed 2026-04-21; created 2026-03-04 |
| Scale floor (≥1★) | ✅ **5,710★** |
| Tier classification | **T1 Assistant Skill** (library-usage skill bundle) |

**Phase 0 = PASS.** In-scope. T1 skill bundle; adjacent to the design/front-end-skill cluster (v75/v81/v82/v83/v85/v105) and the agentskills.io 57k implementer chain.

---

## Phase 0.9 — STRICT 4-criterion INCLUDE filter

### (a) Author cultural-peer to Storm Bear — **FAIL**

Owner = **GreenSock** (GitHub `type: Organization`; Chicago; blog gsap.com; @GreenSock; est. 2012; 5 public repos; 592 followers). The official vendor of GSAP, a widely-used JS animation library now owned by Webflow.

7-axis (a) taxonomy (§25):

| Sub-axis | Evidence | Verdict |
|---|---|---|
| (a)-1 Direct VN/small-team peer | US commercial org (Webflow-owned); not VN/small-team | FAIL |
| (a)-2 Native-language fluency (Tiếng Việt) | English-only | FAIL |
| (a)-3 Product-locale-inclusion (`vi-VN`) | None | FAIL |
| (a)-4 Community-org cultural-peer | Commercial vendor, not a VN/Asian community-org | FAIL |
| (a)-5 Multi-org-founder cultural-peer | n/a | FAIL |
| (a)-6 Cluster-extension cultural-peer | US-commercial; does not extend the VN/Asian cluster | FAIL |
| (a)-7 Foundational-Vendor-Direct-Source | **FAIL** — (a)-7 is reserved for *substrate vendors the vault depends on* (Anthropic). GSAP is a third-party UI library; the vault has **no GSAP dependency**. Criterion-2 ("upstream of the operator's typical work") FAILS. | FAIL |

**(a) = FAIL.** Important nuance: at the *methodology layer* this subject is a clean **sister to (a)-7** ("the maker of X ships the authoritative skill for X") — but (a)-7 as a Phase 0.9 PASS axis is operator-substrate-specific (Anthropic-tier), and GSAP is not in that set. No new (a) sub-axis is coined (cascade-dilution avoidance per §25; mirrors the v98/v112 discipline of not minting axes for single non-cluster instances). Honest FAIL.

> **Finding-2 calibration note:** (a) genuinely FAILS and is recorded as FAIL. The INCLUDE rests on (b)(c)(d).

### (b) Vault-deployability / operator-applicability — **MODERATE**

- **Cost-of-trial (§10): MINIMUM** — `npx skills add greensock/gsap-skills` installs into Claude Code / Cursor / etc.; fully reversible by removing the skill. The vault already runs an agent harness.
- **Applicability: conditional + narrow.** GSAP is specifically a *JavaScript web-animation* library. Storm Bear is a software dev + Scrum coach; front-end animation is **not core vault work**. This is useful **only IF** he builds GSAP-based animated UI in a given window — exactly the CONDITIONAL-pilot bucket the v81–v85 design-skills landed in.
- MINIMUM cost × conditional/narrow applicability ⇒ **MODERATE** (a real but weak PASS). Deliberately **not** inflated to STRONG: low cost alone doesn't make a niche tool broadly applicable.

### (c) Instructive / methodology value — **STRONG**

A genuinely exemplary *model* for authoring official vendor skills:
- Tight **8-skill decomposition** (core / timeline / scrolltrigger / plugins / react / frameworks / utils / performance) with an explicit **cross-skill routing graph** ("for sequencing use gsap-timeline; for scroll use gsap-scrolltrigger…").
- Clear **"When to Use This Skill"** + **"When to recommend GSAP over other libraries"** framing — a template for trigger-scoping a skill.
- **5-surface multi-harness packaging** (AGENTS.md + CLAUDE.md + GEMINI.md + copilot-instructions.md + per-topic `.instructions.md` + Claude/Cursor plugin marketplaces).
- Directly instructive for (i) Storm Bear's own skill-authoring and (ii) the ongoing agentskills.io 57k chain study. STRONG.

### (d) Corpus connectivity — **STRONG**

- **agentskills.io 57k chain** implementer #7-candidate (v76 → v93 → v98 → v99 → v100 → v113 → v114).
- **Pattern #84 84c.1/84c.2** multi-harness (Claude + Cursor + Copilot + Gemini + AGENTS.md; vercel-labs `skills` CLI → 40+ agents incl. Antigravity).
- **Design/front-end-skill cluster adjacency** (v75 impeccable / v81 taste-skill / v82 huashu / v83 open-design / v85 ui-ux-pro-max / v105 guizang) — though this is a *library-usage* skill, not a *design-language* skill.
- **Library-vocab #12** LLM-routing artifacts (strong 5-artifact instance).
STRONG.

---

## Verdict

**STRONG INCLUDE 3/4** — (a) FAIL · (b) MODERATE · (c) STRONG · (d) STRONG.

Honest, uninflated: the standout is (c)+(d) — an exemplary official-vendor-skill model and a clean agentskills.io chain node. (b) is a weak/conditional PASS. (a) fails cleanly.

**Streak:** **"44+1*"** — 25th consecutive clean Phase 0.9 PASS post-v84 OVERRIDE (v113 was 24th). 46-instance window v65-v114 (v106 + v110 audits not counted) = 45 PASS + 1 OVERRIDE = **~97.8% INCLUDE rate** (45/46 = 97.83%).

**Pilot:** **CONDITIONAL** — IF GSAP/web-animation work appears in a 30-day window, a MINIMUM-cost reversible `npx skills add` trial. Otherwise a corpus-knowledge + skill-authoring-reference subject. Not part of the operational install stack.
