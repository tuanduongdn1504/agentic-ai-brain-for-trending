# nature-skills — Wiki (v119)

> `Yuan1z0825/nature-skills` · **"符合nature论文学术表达和科研绘图的Skill"** (Skills aligned with *Nature*-journal academic expression and scientific visualization). · A bilingual **Claude Code / Codex skill bundle** — 9 `SKILL.md` skills for *Nature*-family manuscript writing, figure design, citation, and academic search — installable via `/plugin install nature-skills`, with a bundled `nature-academic-search` MCP server. **Independent and explicitly unaffiliated with Nature Publishing Group.**

**(C) Claude-generated wiki page.** Fetched 2026-05-29 (GitHub API + README + author profile). Routine v2.4, wiki #119. Phase 0.9 **STRONG INCLUDE 4/4** — (c)(d) STRONG, (a) PASS (declared China-Mainland), (b) MODERATE. 3rd consecutive clean PASS after the v116 Sana OVERRIDE.

> ⚠️ **v119 was the projected natural-audit window (~v119–v120).** This wiki ships per operator request, but the post-v115 audit queue is now substantial — **v120 = AUDIT strongly recommended** over a 5th straight build.

---

## Identity

| Field | Value |
|---|---|
| Repo | [`Yuan1z0825/nature-skills`](https://github.com/Yuan1z0825/nature-skills) |
| What | **Claude Code / Codex skill bundle** — 9 SKILL.md skills for *Nature*-journal academic writing/figures + a bundled MCP search server |
| Tier / archetype | **T1 Assistant Skill / Domain-Vertical-Skill-Collection** (academic / scientific-publishing vertical; sibling to v90 academic-research-skills) |
| Stars / forks | **13,633★ / 846 forks** (fork_ratio **0.062**) |
| Subscribers / open issues | 13 / 11 |
| Created / pushed | 2026-04-24 / 2026-05-29 (**~35 days** old at fetch) |
| Velocity | **~390 stars/day → Pattern #52 EXTREME-VIRAL pulse-class** (>300/d; 35-day window « 90d so a *pulse*, NOT Multi-Month-Sustained) |
| License | **MIT** (GitHub API `mit`) |
| Language | **Python ~97.7%** (figure-generation scripts + MCP server) |
| Distribution | Claude Code `/plugin marketplace add` + `/plugin install nature-skills`; Codex Desktop plugin marketplace; manual copy to `~/.codex/skills/` or `~/.claude/agents/`; MCP server via `install.sh` |
| Default branch / homepage | `main` / none |
| Topics | codex-skills, nature, nature-skills |
| Author | **Yuan Yizhe (袁一哲)** (`owner.type: User`) — **PhD student at Shanghai Jiao Tong University** (medical AI); declared China-Mainland (SJTU + `sjtu520aimedws@163.com` recruitment email + bilingual zh README + Chinese-PPTX skill). Account 2023, 10 repos, 243 followers. |
| Affiliation | **Independent + explicitly unaffiliated with Nature Publishing Group** — "designed to *emulate* journal standards, not represent them." |

## What it is

A modular set of **nine `SKILL.md` skills** that teach a coding agent to produce *Nature*-style scholarly output:

1. **nature-figure** — matplotlib figures to *Nature* visual standards (SVG + 300 dpi PNG, enforced rcParams, semantic palettes, 10+ chart types)
2. **nature-polishing** — draft prose → *Nature*-style writing (≤30-word sentences, British English, tense calibration)
3. **nature-writing** — drafts manuscript sections (abstract / intro / results / discussion)
4. **nature-citation** — claims → strict Nature/CNS citations; exports ENW / RIS / Zotero RDF
5. **nature-data** — Data Availability statements + FAIR metadata checks
6. **nature-reader** — bilingual full-paper Markdown readers with figure grounding
7. **nature-response** — point-by-point reviewer response letters with action mapping
8. **nature-paper2ppt** — papers → Chinese PPTX for journal clubs
9. **nature-academic-search** — multi-source search (PubMed / CrossRef / arXiv) via a **bundled MCP server** (`search_papers`, `get_paper_by_id`, `get_citation`, `lookup_mesh`)

Repo layout: `skills/nature-*/SKILL.md` (frontmatter + rules) + `references/` subdirectories + `nature-academic-search/mcp-server/`. Skills carry **status levels** (Draft / Beta / Stable).

## Why it's in the corpus

**STRONG INCLUDE 4/4** (no criterion fails; load-bearing on (c)(d)):
- **(a) PASS (declared)** — Yuan Yizhe, SJTU PhD, China-Mainland (declared, not merely inferred — stronger than v117). Extends the China-Mainland sub-cluster (v82+v83+v91+v94+v100+v117+**v119** = 7 by-event). No new (a) sub-axis (China-Mainland established).
- **(b) MODERATE** — it's a Claude Code plugin (goal-adjacent, MINIMUM-cost reversible install), but the **domain — Nature-journal academic/scientific writing — is not Storm Bear's vertical** (software dev + Scrum). Real value = skill-authoring reference + the bundled-MCP-server pattern. Honestly MODERATE (mirrors v98 cybersecurity / v114 gsap), not inflated.
- **(c) STRONG** — exemplary domain-vertical skill-bundle: 9-skill decomposition, plugin-marketplace distribution, a bundled MCP server, status-levels (Draft/Beta/Stable), `references/`, multi-harness.
- **(d) STRONG** — high connectivity: agentskills.io 57k chain (11th implementer); T1 Domain-Vertical-Skill-Collection (academic vertical, sibling v90); the **affiliation-disclaimer Library-vocab N=2 with v98**; Pattern #84 multi-harness (Claude Code + Codex); Pattern #18 B1 MCP; China-Mainland cluster; Pattern #52 pulse.

## Pattern Library contribution (summary)

- **PRIMARY: Library-vocab "Brand-Named Third-Party Repo + Affiliation Disclaimer" → N=2** (v98 Anthropic-Cybersecurity-Skills + **v119 nature-skills**) — both use a famous brand in the repo/skill names (*Anthropic* / *Nature*) with an explicit "not affiliated" disclaimer. Strengthens a PROVISIONAL N=1 → N=2; promotion-eligible at N=3 (audit decision).
- SECONDARY: **T1 Domain-Vertical-Skill-Collection → N=4** (v64 SEO + v90 academic + v98 cybersecurity + v119 academic/scientific-publishing; academic sub-vertical N=2 with v90) post-CONFIRMED strengthening; **Pattern #57 57k agentskills.io chain 11th implementer**; **Pattern #84 multi-harness** (Claude Code + Codex / codex-skills topic); **Pattern #18 B1 MCP** (bundled `nature-academic-search`) + a NEW sub-observation "skill-collection bundles its own domain MCP server" PROVISIONAL N=1; **Pattern #52 EXTREME-VIRAL pulse** (~390/d × 35d); China-Mainland sub-cluster → 7 by-event; Pattern #19 Chinese-academic-PhD profile; honest note: **academic-lab-recruitment + WeChat-donation via a viral OSS skill bundle** (recruiting med+AI interns).
- **Honest non-claims:** (a) PASSES (declared China-Mainland); (b) is MODERATE (domain off-vertical) — not inflated; NO new top-level Pattern (PRIMARY is a Library-vocab N=2 strengthening, secondaries are post-CONFIRMED strengthenings + one N=1 sub-observation); NOT a Pattern #52 promotion (pulse <90d); **zero new standalone Library-vocab minted** (§28) — observations strengthen v98's existing item / file into clusters; no Pattern Library state change at ship.

---

*See `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` and `01 Analysis/(C) Pattern-Library-Phase-4b-Brand-Named-Affiliation-Disclaimer-N2.md`.*
