# (C) Cluster 2 — In-repo Composio-built skills + 832 Rube wrappers + skill-creator + plugin manifests

**Source**: `00 Source/awesome-claude-skills/` filesystem (905 directories / 864 SKILL.md / 62 .py files)

**Wiki**: v50 awesome-claude-skills | **Cluster**: 2 of 3

---

## Cluster scope

This cluster covers the **filesystem-shipped content** that the README aggregator points at. Three layers:
- **Layer A**: 31 top-level skill subdirectories (Composio-built + 9 Anthropic-imported with original LICENSE.txt).
- **Layer B**: `composio-skills/` directory containing **832 Rube-MCP-wrapper skills** + a `.claude-plugin/marketplace.json` (corpus-first directory-scoped marketplace.json).
- **Layer C**: `connect-apps-plugin/` — separate Claude Code plugin manifest + commands directory; this is the entry point Quickstart pushes users toward.

---

## Layer A — 31 top-level skill subdirectories

Alphabetical listing (verified via `/bin/ls -d */`):

1. `artifacts-builder/` (LICENSE.txt = Apache-2.0)
2. `brand-guidelines/` (LICENSE.txt = Apache-2.0)
3. `canvas-design/` (LICENSE.txt = Apache-2.0)
4. `changelog-generator/`
5. `competitive-ads-extractor/`
6. `composio-skills/` ← **Layer B container**
7. `connect-apps-plugin/` ← **Layer C container**
8. `connect-apps/`
9. `connect/`
10. `content-research-writer/`
11. `developer-growth-analysis/`
12. `document-skills/`
13. `domain-name-brainstormer/`
14. `file-organizer/`
15. `image-enhancer/`
16. `internal-comms/` (LICENSE.txt = Apache-2.0)
17. `invoice-organizer/`
18. `langsmith-fetch/`
19. `lead-research-assistant/`
20. `mcp-builder/` (LICENSE.txt = Apache-2.0)
21. `meeting-insights-analyzer/`
22. `raffle-winner-picker/`
23. `skill-creator/` (LICENSE.txt = Apache-2.0) — **meta-skill: a skill that teaches Claude how to create skills**
24. `skill-share/` — **meta-skill: collaboration/sharing for skills**
25. `slack-gif-creator/` (LICENSE.txt = Apache-2.0)
26. `tailored-resume-generator/`
27. `template-skill/` — **meta-skill: SKILL.md template scaffold**
28. `theme-factory/` (LICENSE.txt = Apache-2.0)
29. `twitter-algorithm-optimizer/`
30. `video-downloader/`
31. `webapp-testing/` (LICENSE.txt = Apache-2.0)

**Per-skill LICENSE.txt count**: 9 of 31 (29%) carry standalone Apache-2.0 LICENSE.txt. These appear to be wholesale-imported from `anthropics/skills` (verbatim Apache 2.0 text starts with `Apache License / Version 2.0, January 2004`).

**Meta-skills observed**: 3 of 31 are skills-about-skills:
- `skill-creator/` — guides creation of new skills (corpus-first meta-skill at this scale)
- `skill-share/` — collaboration/sharing infrastructure for skills
- `template-skill/` — SKILL.md scaffold template

Sample SKILL.md (skill-creator/SKILL.md):
```yaml
---
name: skill-creator
description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
license: Complete terms in LICENSE.txt
---
```

Note `license:` field in YAML frontmatter — corpus-first observation of in-frontmatter license declaration.

---

## Layer B — `composio-skills/` directory (832 Rube-MCP wrappers)

**Counts (verified)**:
- 832 entries inside `composio-skills/` (all with `-automation` suffix; alphabetical ordering)
- 1 `.claude-plugin/marketplace.json` (v2.0.0, schema-referenced)
- 905 total directories repo-wide
- 864 SKILL.md files repo-wide

**Sample composio-skills entry (slackbot-automation)**:
```yaml
---
name: slackbot-automation
description: "Automate Slackbot tasks via Rube MCP (Composio). Always search tools first for current schemas."
requires:
  mcp: [rube]
---

# Slackbot Automation via Rube MCP

Automate Slackbot operations through Composio's Slackbot toolkit via Rube MCP.

**Toolkit docs**: [composio.dev/toolkits/slackbot](https://composio.dev/toolkits/slackbot)

## Prerequisites
- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Slackbot connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `slackbot`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas
```

**Architectural pattern**: Each composio-skills entry is a **thin instruction wrapper around Rube MCP** (Composio's commercial product). Without Rube MCP, none of these 832 skills function. They:
- Declare `requires: mcp: [rube]` in YAML frontmatter (corpus-first explicit MCP-requirement declaration in skill YAML)
- Reference Composio toolkit docs at `composio.dev/toolkits/<name>`
- Instruct Claude to call Rube-namespaced tools (`RUBE_SEARCH_TOOLS`, `RUBE_MANAGE_CONNECTIONS`)
- Provide tool-sequence hints + parameter guidance + known pitfalls per toolkit

**This is the corpus-first observation of "commercial-product-as-fulfillment-layer-for-aggregated-skills"** (Pattern #50 sub-variant). Every wrapper is unfunctional without commercial signup.

**marketplace.json structure** (composio-skills/.claude-plugin/marketplace.json):
```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "awesome-claude-skills",
  "version": "2.0.0",
  "description": "A curated marketplace of practical Claude Skills...",
  "owner": {"name": "ComposioHQ", "email": "tech@composio.dev"},
  "plugins": [
    {"name": "brand-guidelines", "description": "...", "source": "./brand-guidelines", "category": "business-marketing"},
    ...
  ]
}
```

**Pattern #59 corpus-first sub-variant**: directory-scoped marketplace.json (vs 59a marketplace+npm OMC v27 / 59b marketplace-only claude-hud v35). The marketplace.json indexes the in-repo skills as a Claude Code plugin marketplace consumable via Claude Code's `/plugin marketplace add ComposioHQ/awesome-claude-skills` flow.

---

## Layer C — `connect-apps-plugin/` (commercial product entry-point)

**Files (verified via `/bin/ls -la connect-apps-plugin/`)**:
- `.claude-plugin/plugin.json` (manifest)
- `README.md` (1,179 bytes)
- `commands/` (Claude Code custom slash commands)

**Plugin manifest** (`.claude-plugin/plugin.json`):
```json
{
  "name": "connect-apps",
  "description": "Manage auth and connect to 500+ apps using Composio. Perform real actions from Claude Code - send emails, create issues, post messages, and more.",
  "author": {"name": "Composio", "email": "support@composio.dev"}
}
```

**Install flow** (verbatim from README Quickstart):
```bash
claude --plugin-dir ./connect-apps-plugin
/connect-apps:setup
# Paste API key from dashboard.composio.dev
exit
claude
```

**Architectural significance**: connect-apps-plugin is **Composio's commercial product entry-point shipped INSIDE the open-source aggregator**. The README's Quickstart (very first action README pushes users toward) is to install this commercial-product plugin and authenticate to dashboard.composio.dev. Pattern #50 sub-variant: **commercial-product-entry-as-bundled-skill** corpus-first.

---

## Filesystem tree summary

```
awesome-claude-skills/
├── README.md                              [33 KB; aggregator surface]
├── CONTRIBUTING.md                        [4.4 KB]
├── (NO LICENSE file at root)              [absent-LICENSE-with-README-claim]
│
├── 31 top-level skill subdirs/
│   ├── 9 with own LICENSE.txt (Anthropic-imported, Apache-2.0)
│   ├── 3 meta-skills (skill-creator, skill-share, template-skill)
│   └── 19 Composio-built skills
│
├── composio-skills/                       [832 entries]
│   ├── .claude-plugin/marketplace.json    [v2.0.0; corpus-first directory-scoped marketplace]
│   └── 832 *-automation/ subdirs          [each: SKILL.md with requires.mcp:[rube]]
│
└── connect-apps-plugin/                   [commercial product entry-point]
    ├── .claude-plugin/plugin.json         [Claude Code plugin manifest]
    ├── README.md
    └── commands/                          [/connect-apps:setup slash command]
```

Total: 905 directories / 864 SKILL.md / 62 .py files / 9 LICENSE.txt / 1 marketplace.json / 1 plugin.json.

---

## Pattern observations from cluster 2

| Pattern | Observation in cluster 2 |
|---------|--------------------------|
| **#50 Commercial-Funnel** | 832/864 skills (96.3%) require Rube MCP commercial signup to function. Strongest commercial-funnel coupling observed in corpus. |
| **#59 Plugin Marketplace Native** | Corpus-first directory-scoped marketplace.json (vs 59a / 59b). NEW SUB-VARIANT: marketplace-as-subdirectory-of-aggregator. |
| **#29 License-Category-Diversity** | Per-skill licensing variation: 9 Apache-2.0 (Anthropic-imported), 22 unlicensed (Composio-built top-level), 832 unlicensed (composio-skills wrappers). 4-tier license-presence within single repo. |
| **#18 MCP** | 832 SKILL.md frontmatters declare `requires.mcp: [rube]` — corpus-first observation of explicit MCP-requirement field in skill YAML at scale. Layer-1 MCP-universal-adoption reinforced. |
| **#22 AGENTS.md** | NO AGENTS.md / CLAUDE.md anywhere in 905-directory tree — consistent with awesome-list-genre absence. |
| **#68 Hybrid Sub-Variant** | aggregator-with-bundled-in-repo-skills + commercial-product-entry-as-bundled-skill = corpus-first hybrid observation within Pattern #68. |
| **EXTREME primitive count** | 864 SKILL.md = 5th EXTREME tier in corpus (after ruflo v42 ~500 / aidevops v47 ~2,665+). Skill-catalog-density-tier sub-observation. |

---

## Cross-references

- See `Cluster 1` for README aggregator surface that catalogs these subdirs.
- See `Cluster 3` for Composio commercial ecosystem the wrappers funnel into.
- See `02 Entity Pages/(C) Composio In-Repo Skill Library + 832-Wrapper Catalog.md` for synthesized in-repo entity.
- See `02 Entity Pages/(C) Composio Commercial Ecosystem + Rube MCP + Pattern #50 Corpus-Strongest.md` for commercial product analysis.

---

## Open questions / verification flags

- **What is Rube MCP's actual provenance?** Composio's commercial product; marketed at `https://rube.app/mcp`. Out of scope for v50 wiki — flagged as follow-up deep-dive.
- **Why 832 wrappers when README only catalogs ~70?** Hypothesis: README curates the most-popular subset of Composio's 1000+ toolkit catalog; the full 832-entry catalog is in-repo for completeness/discoverability but only top apps appear in README. The 70+ App Automation README links may be auto-generated from a popularity threshold.
- **Per-skill license enforcement**: The 9 LICENSE.txt skills have legally-clean Apache-2.0 standing. Other 856 SKILL.md files in this repo carry no per-file license declaration; the README's repo-level Apache-2.0 claim is the only license signal — but no actual LICENSE file at root means even that claim is legally weak.
