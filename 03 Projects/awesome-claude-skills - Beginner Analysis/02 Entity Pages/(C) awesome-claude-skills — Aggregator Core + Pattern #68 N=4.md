# (C) awesome-claude-skills — Aggregator Core + Pattern #68 N=4

**Type**: Project entity (aggregator surface)
**Wiki**: v50 (corpus half-century milestone)
**Pattern Library role**: Pattern #68 awesome-list-genre meta-pattern **4th data point** + audience sub-type c reaches **N=2**

---

## Identity

- **Repo**: `ComposioHQ/awesome-claude-skills` (https://github.com/ComposioHQ/awesome-claude-skills)
- **Default branch**: master
- **Created**: 2025-10-17 (~6 months at v50 ship date 2026-04-25)
- **Pushed**: 2026-04-21 (active, 4 days before v50 ship)
- **Stars**: 56,200 (#7-8 in corpus)
- **Forks**: 6,039 (10.7%)
- **Watchers**: 56,200
- **Open issues**: 557 (HIGH — community-contribution churn typical of awesome-list-genre)
- **Owner**: Composio Inc. (`ComposioHQ`) — 70 public repos, 1,649 followers
- **License (claim)**: Apache-2.0 (README badge + `## License` section)
- **License (file)**: NONE at root (corpus-first absent-LICENSE-with-README-claim sub-context)

---

## What is awesome-claude-skills?

A **hybrid aggregator + bundled-in-repo skill-library + commercial-product-entry-as-skill** for Claude Skills (Anthropic's official Skills system; portable across Claude.ai, Claude Code, Claude API).

The repo serves three layered functions simultaneously:

1. **Curation surface** (README) — catalogs ~120 external Claude Skills across 10 categories, including ~70 entries that pseudo-link to Composio's own automation catalog.
2. **Skill-library shipping** — 31 top-level subdirectories, each with `SKILL.md` + helper code (some with own `LICENSE.txt`); 9 of these are wholesale-imported from `anthropics/skills` with original Apache-2.0 LICENSE.txt preserved.
3. **Commercial-product distribution** — `connect-apps-plugin/` is Composio's commercial-product entry-point shipped inside the OSS aggregator; Quickstart pushes user to install it and authenticate to dashboard.composio.dev. 832 of 864 SKILL.md files inside `composio-skills/` declare `requires: mcp: [rube]` — the entire automation catalog is non-functional without Composio's commercial Rube MCP product.

---

## Pattern #68 4th data point — strongest meta-pattern strengthening

| Wiki | Year | Sub-type | Audience | Scale at wiki-time |
|------|------|----------|----------|--------------------|
| build-your-own-x v8 | 2026-04-18 | a | human-directed learning input | 491K stars |
| awesome-design-md v25 | 2026-04-20 | b | AI-agent-directed content input | 60.5K stars |
| awesome-mcp-servers v31 | 2026-04-22 | c | AI-runtime infrastructure directory | 85K stars |
| **awesome-claude-skills v50** | **2026-04-25** | **c** (joins awesome-mcp-servers) | **AI-runtime infrastructure directory** | **56.2K stars** |

**Audience sub-type c (AI-runtime-infrastructure-directory) reaches N=2** — first within-sub-type N=2 promotion-candidate within Pattern #68 since meta-pattern was confirmed at v31.

**Hybrid sub-variant observation (corpus-first)**: awesome-claude-skills is the FIRST Pattern #68 data point that ships **bundled-in-repo skill-library content** alongside the aggregator README. Prior 3 data points (build-your-own-x, awesome-design-md, awesome-mcp-servers) were pure-aggregator pointing to external repos. awesome-claude-skills ships 864 SKILL.md files in-repo + curates external skills in README simultaneously.

This is a **hybrid aggregator-with-bundled-content sub-variant within Pattern #68** — observational at N=1; do NOT register as standalone (consolidation-forward discipline).

---

## Comparison axis matrix vs prior 3 awesome-list-genre wikis

| Axis | build-your-own-x v8 | awesome-design-md v25 | awesome-mcp-servers v31 | awesome-claude-skills v50 |
|------|---------------------|------------------------|--------------------------|----------------------------|
| Stars (at wiki-time) | 491K | 60.5K | 85K | 56.2K |
| Age at wiki-time | ~10 years | 20 days | ~17 months | ~6 months |
| Content nature | Pure curation | Pure curation + 69 DESIGN.md templates | Pure curation | Hybrid: curation + 31 in-repo skills + 832 wrappers |
| External skill links | ~30 (build-your-own tutorials) | 69 templates | ~1,200 servers | ~120 + 70 broken-link automations |
| In-repo bundled content | None (markdown-only) | 69 DESIGN.md (markdown-only) | None | **864 SKILL.md + helper code (corpus-first)** |
| License | CC0 | MIT | MIT | **Apache-2.0 claim, no LICENSE file (corpus-first)** |
| Commercial entity | CodeCrafters Inc. (post-acquisition) | VoltAgent (commercial-startup) | punkpeye (solo) + Glama commercial | Composio Inc. (commercial-startup) |
| Commercial-funnel | Indirect (CodeCrafters) | Direct (getdesign.md) | Direct (Glama Chat / glama.ai) | **Strongest (5 surfaces + UTM tracking + 832 wrappers require commercial signup)** |
| Audience sub-type | a | b | c | c |
| AGENTS.md | Absent | Absent | Absent | Absent (4/4 awesome-list-genre absence) |
| Primary lang per GitHub | None (markdown) | None (markdown) | None (markdown) | **Python (62 .py files in helper scripts)** |

**Notable corpus-firsts at v50**:
- First Pattern #68 entry with bundled in-repo skill content (864 SKILL.md files)
- First Pattern #68 entry with absent-LICENSE-at-root + README-claim (Pattern #29 4th sub-context)
- First Pattern #68 entry with directory-scoped marketplace.json (Pattern #59 corpus-first sub-variant)
- First Pattern #68 entry with EXTREME primitive-count tier (5th in corpus overall)
- First Pattern #68 entry with explicit MCP-required skill YAML frontmatters (Pattern #18 corpus-first observation at scale)

---

## Curation philosophy + content topology

- README catalogs across 10 categories. ~30 entries are in-repo (`./folder/`); ~90 are external (GitHub URLs to other repos).
- 9 entries point to `anthropics/skills` (Anthropic-curated official skills).
- 5 entries point to `obra/superpowers` (Storm Bear v2 wiki subject — see Pattern #57 entity page).
- Multiple entries from community contributors with `*By [@username]*` attribution.
- 70+ App Automation entries pseudo-link to `./close-automation/`, `./gmail-automation/`, etc. — but these paths exist ONLY inside `composio-skills/` subdirectory, not at top level. Hypothesis: README is auto-generated from a master Composio toolkit catalog; top-level link paths are aspirational or representational.

---

## Pattern observations summary

| Pattern | Status | Evidence in awesome-claude-skills v50 |
|---------|--------|---------------------------------------|
| **#68 Awesome-list-genre** | STRENGTHEN N=4 + sub-type c reaches N=2 + hybrid sub-variant observation | ✅ confirmed; structurally similar to v31 but with bundled content |
| **#50 Commercial-Funnel** | STRENGTHEN N=9 — corpus-strongest | ✅ 5-surface commercial line + UTM tracking + 96.3% skills require commercial product |
| **#57 Recursive Corpus Reference** | STRENGTHEN N=5 — aggregator-mediated multi-citation | ✅ obra/superpowers cited 5× + anthropics/skills cited 5× |
| **#29 License-Category-Diversity** | STRENGTHEN — absent-LICENSE-with-claim 4th sub-context | ✅ Apache-2.0 README claim + no LICENSE file |
| **#59 Plugin Marketplace Native** | STRENGTHEN — directory-scoped marketplace.json corpus-first | ✅ composio-skills/.claude-plugin/marketplace.json v2.0.0 |
| **#22 AGENTS.md** | STRENGTHEN aggregator-genre absence pattern (4/4) | ✅ no AGENTS.md / CLAUDE.md anywhere |
| **#18 MCP** | STRENGTHEN Layer 1 universal | ✅ 832/864 skills declare `requires.mcp: [rube]` |
| **#19 archetype 4 no-lineage** | STRENGTHEN | ✅ no individual-author citations; org-only branding |
| **#27 Community-Viral** | STRENGTHEN ~22nd observation | ✅ 9.4K stars/month aggregator-amplified-commercial sustained |
| **#17 variant 3 commercial-startup** | STRENGTHEN ~19th data point | ✅ Composio 70-repo ecosystem strongest variant-3 evidence |
| **#2 Distribution Evolution** | STRENGTHEN | ✅ 4 surfaces (clone+copy / marketplace UI / `--plugin-dir` / Skills API) |

**Net Pattern Library delta at v50**: 0 new active candidates / 0 new OBSERVATION-TRACKs / 11 patterns strengthened. **14-CONSECUTIVE-WIKI ZERO-NEW-ACTIVE-CANDIDATES STREAK** (v37-v50; new corpus record extends v49's 13-streak).

---

## Storm Bear pilot relevance

- **Direct utility (MEDIUM)**: 5 in-repo skills directly applicable to Storm Bear vault automation (file-organizer, content-research-writer, meeting-insights-analyzer, tailored-resume-generator, changelog-generator). All MIT-or-Apache-equivalent in spirit; 9 carry verifiable LICENSE.txt.
- **Architectural reference (HIGH)**: 864-SKILL.md catalog is direct reference for Storm Bear publishing strategy (v27 diagnostic HIGH item #2). marketplace.json template is direct reference for any future public skill release.
- **Ecosystem awareness (HIGH)**: Pattern #57 recursion observation puts Storm Bear corpus inside its own knowledge graph (obra/superpowers v2 is corpus member; awesome-claude-skills v50 cites it).
- **Commercial coupling concern (HIGH)**: Operator should AVOID installing connect-apps-plugin or relying on composio-skills/ wrappers without explicit Rube MCP cost/policy evaluation. Quickstart UTM-tracking density indicates aggressive commercial funnel.

See `03 Beginner Guide` for full pilot table.

---

## Cross-references

- `01 Cluster Summaries/(C) Cluster 1` — README aggregator surface
- `01 Cluster Summaries/(C) Cluster 2` — in-repo skill library + 832 wrappers
- `01 Cluster Summaries/(C) Cluster 3` — Composio commercial ecosystem
- `02 Entity Pages/(C) Composio In-Repo Skill Library + 832-Wrapper Catalog.md`
- `02 Entity Pages/(C) Composio Commercial Ecosystem + Rube MCP + Pattern #50 Corpus-Strongest.md`
- `02 Entity Pages/(C) Storm Bear Meta-Entity v50 — 50-Wiki Milestone + Pattern #57 Recursion Vector.md`
- `04 Phase 4b Deliverable/(C) v50 — Pattern #68 4th + Pattern #50 Corpus-Strongest + 50-Wiki Milestone.md`
