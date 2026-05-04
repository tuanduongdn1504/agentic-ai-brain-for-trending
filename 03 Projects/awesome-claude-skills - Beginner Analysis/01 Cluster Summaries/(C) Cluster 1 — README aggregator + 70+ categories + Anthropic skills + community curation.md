# (C) Cluster 1 — README aggregator + 70+ categories + Anthropic skills + community curation

**Source files**: `00 Source/awesome-claude-skills/README.md` (33,168 bytes / 477 lines)

**Wiki**: v50 awesome-claude-skills | **Cluster**: 1 of 3

---

## Cluster scope

The README is the aggregator surface. It curates **120+ external skill links + cross-references 31 in-repo top-level skills + indexes 70+ App Automation entries** (which point to subdirectories inside `composio-skills/`, not top-level). Plus quickstart, contribution flow, resources, license claim, community channels.

This is the user-facing front door. Everything in clusters 2 and 3 is what the README *links to*.

---

## Structural anatomy (README sections)

1. **Header banner** — UTM-tracked Composio banner image linking to `dashboard.composio.dev/login?utm_source=Github&utm_medium=Youtube&utm_campaign=2025-11&utm_content=AwesomeSkills`. **Marketing-tracking is the very first element**.
2. **Badges** — `awesome.re` + `PRs welcome` + `Apache-2.0` (badge-only claim; no LICENSE file).
3. **Social CTAs** — X (@composio) + LinkedIn (composiohq) + Discord (discord.com/invite/composio).
4. **Tagline** — "A curated list of practical Claude Skills for enhancing productivity across Claude.ai, Claude Code, and the Claude API."
5. **Quickstart** — `claude --plugin-dir ./connect-apps-plugin` + `/connect-apps:setup` + paste API key from dashboard.composio.dev. **First action README pushes user toward = installing Composio's commercial product entry-point.**
6. **Contents** — 10 skill categories + Getting Started + Creating Skills + Contributing + Resources + License.
7. **What Are Claude Skills?** — 1-paragraph definition (Anthropic's framing).
8. **10 Skill Categories** with curated entries (mix of in-repo `./folder/` links and external `https://github.com/...` links):
   - **Document Processing** (5 items: docx, pdf, pptx, xlsx — all `anthropics/skills/tree/main/skills/...` + Markdown to EPUB by @smerchek)
   - **Development & Code Tools** (24 items including `obra/superpowers` 4×: test-driven-development, brainstorming, root-cause-tracing, finishing-a-development-branch, using-git-worktrees + 1× via separate skill)
   - **Data & Analysis** (4 items)
   - **Business & Marketing** (5 items, all in-repo)
   - **Communication & Writing** (7 items)
   - **Creative & Media** (7 items)
   - **Productivity & Organization** (8 items)
   - **Collaboration & Project Management** (5 items)
   - **Security & Systems** (4 items)
   - **App Automation via Composio** — **70+ in-repo subdirectory links to non-existent paths** (e.g., `./close-automation/`, `./hubspot-automation/`, etc. — these are NOT top-level dirs; they exist only inside `composio-skills/`). Confirmed broken-relative-link pattern: README pseudo-links work because users browsing GitHub UI follow the link manually OR these are aspirational/placeholder paths.
9. **Getting Started** — 3 install paths (Claude.ai marketplace UI / Claude Code copy-to-`~/.config/claude-code/skills/` / Claude API programmatic via `skills=["skill-id"]`).
10. **Creating Skills** — folder structure template + YAML frontmatter SKILL.md template + 6 best practices.
11. **Contributing** — link to CONTRIBUTING.md; 5-step PR flow.
12. **Resources** — Official Anthropic docs (5 links) + Community Resources (Anthropic Skills Repo + Claude Community + Skills Marketplace) + Inspiration (Lenny's Newsletter "50 ways" + Notion Skills).
13. **Community** — Discord + Twitter + support@composio.dev.
14. **CTA** — "Join 20,000+ developers building agents that ship" + UTM-tracked "Get Started Free" → `platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills`.
15. **License** — *"This repository is licensed under the Apache License 2.0. Individual skills may have different licenses - please check each skill's folder for specific licensing information."* — **CLAIM ONLY; no root LICENSE file**.
16. **AgentsKB footer** — sister product link `agentskb.com`.

---

## Curation philosophy observed

- **Mixed in-repo + external** — README does not distinguish typographically between `./changelog-generator/` (in-repo, ships with this repo) and `https://github.com/...` (external, separate repo). User must hover/click to disambiguate.
- **70+ App Automation entries are broken relative links at top level** — they only resolve inside `composio-skills/`. README wins by pseudo-cataloging Composio's full toolkit list (≈70 most-popular SaaS apps from the 832-entry composio-skills/ catalog).
- **Anthropic-published skills curated front-and-center** — Document Processing's first 4 entries (docx/pdf/pptx/xlsx) all link to `anthropics/skills/tree/main/skills/...` via external GitHub URL.
- **Community attribution explicit** — `*By [@username](https://github.com/username)*` annotation appended to community-contributed entries (~15 attributions visible).
- **No category for Composio's own commercial product** — Rube MCP / Composio platform is woven through skills (Quickstart references it; App Automation section header says *"via Rube MCP (Composio)"*) rather than separated as standalone product line.

---

## Pattern observations from cluster 1

| Pattern | Observation in cluster 1 |
|---------|--------------------------|
| **#68 Awesome-list-genre** | README structure follows the awesome-list-genre template precisely (badges + curated category lists + contributing guide + license). 4th data point in confirmed meta-pattern. Extends sub-type c (AI-runtime-infrastructure-directory) to N=2. |
| **#50 Commercial-Funnel** | Banner UTM tracking is line 4-6 (above tagline); Quickstart pushes user to dashboard.composio.dev signup; "Get Started Free" UTM CTA at footer. Strongest funnel placement observed (above the fold). |
| **#57 Recursive corpus reference** | `obra/superpowers` cited 5× in single README (test-driven-development / brainstorming / root-cause-tracing / finishing-a-development-branch / using-git-worktrees). 5 distinct skills from same Storm Bear v2 wiki subject. |
| **#29 Absent-LICENSE** | README claims Apache-2.0 in section header AND badge AND footer note, but no LICENSE file at root. |
| **#22 AGENTS.md** | NO AGENTS.md, NO CLAUDE.md at root — consistent with awesome-list-genre absence pattern (build-your-own-x v8 / awesome-design-md v25 / awesome-mcp-servers v31 / awesome-claude-skills v50 = 4/4 awesome-list-genre wikis without AGENTS.md). |
| **#19 archetype 4 no-lineage** | No individual-author lineage cited; only Composio org-level branding. |
| **#27 Community-Viral** | 56,200 stars / ~6 months ≈ 9.4K/month sustained-aggregator-amplified-commercial-viral. |
| **#2 Distribution Evolution** | 4 surfaces documented: clone+copy / marketplace UI / `--plugin-dir` / Skills API. |

---

## Cross-references

- See `Cluster 2` for in-repo skill structure + 832 Rube-wrapper catalog + per-skill licensing variation.
- See `Cluster 3` for Composio commercial ecosystem + Rube MCP + AgentsKB.
- See `02 Entity Pages/(C) awesome-claude-skills — Aggregator Core + Pattern #68 N=4.md` for synthesized aggregator entity.
- See `02 Entity Pages/(C) Storm Bear Meta-Entity v50` for Pattern #57 recursion analysis.

---

## Open questions / verification flags

- **Why are App Automation links broken at top level?** Hypothesis: README is auto-generated from a master catalog; `composio-skills/` subdirectory is the "source of truth" for the 832 wrappers; top-level pseudo-paths exist only as user-discoverability surface, not as actual filesystem links. Operator should treat App Automation README links as conceptual catalog entries, not clickable paths inside this repo.
- **License-claim-without-file**: Operator deserves to know that Apache-2.0 is README-claim-only. For derivative or commercial use, the safest assumption is per-skill LICENSE.txt where present + assume "all rights reserved" elsewhere.
- **20,000+ developers claim** — unverified marketing number; not corpus-validatable.
