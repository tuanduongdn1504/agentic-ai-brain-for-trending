# (C) Composio In-Repo Skill Library + 832-Wrapper Catalog

**Type**: Project entity (in-repo content layer)
**Wiki**: v50 awesome-claude-skills

---

## Identity

The 31 top-level skill subdirectories + the 832-entry composio-skills/ wrapper catalog + the connect-apps-plugin commercial-product-entry — all shipping inside the awesome-claude-skills repo as filesystem content.

---

## 31 top-level skill subdirectories — segmented inventory

### Anthropic-imported skills (9, with LICENSE.txt = Apache-2.0)
- `artifacts-builder/` — multi-component HTML artifacts using React + Tailwind + shadcn/ui
- `brand-guidelines/` — Anthropic's official brand colors and typography
- `canvas-design/` — visual art generation in PNG and PDF
- `internal-comms/` — 3P updates, newsletters, FAQs, status reports
- `mcp-builder/` — guides creation of MCP servers
- `skill-creator/` — meta-skill: guides creation of new skills
- `slack-gif-creator/` — animated GIFs optimized for Slack
- `theme-factory/` — professional font + color themes for artifacts
- `webapp-testing/` — Playwright-based web app testing

### Composio-built top-level skills (19, no LICENSE)
- `changelog-generator/` — git commits → user-facing changelogs
- `competitive-ads-extractor/` — competitor ad library analysis
- `connect/` — generic Claude-app connector
- `connect-apps/` — auth + connect to 500+ apps
- `connect-apps-plugin/` — **commercial-product entry-point** (Layer C)
- `content-research-writer/` — research + citations + section-by-section feedback
- `developer-growth-analysis/` — developer growth analytics
- `document-skills/` — generic document skill scaffold
- `domain-name-brainstormer/` — domain name ideas + TLD availability
- `file-organizer/` — context-aware file organization
- `image-enhancer/` — resolution/sharpness enhancement
- `invoice-organizer/` — invoice + receipt tax-prep organization
- `langsmith-fetch/` — LangSmith trace debugging
- `lead-research-assistant/` — lead generation + qualification
- `meeting-insights-analyzer/` — meeting transcript behavioral analysis
- `raffle-winner-picker/` — cryptographically-secure random selection
- `tailored-resume-generator/` — job-description-tailored resumes
- `twitter-algorithm-optimizer/` — Twitter algorithm-based tweet optimization
- `video-downloader/` — YouTube/multi-platform video download

### Meta-skills (3, observational sub-category)
- `skill-creator/` — guides skill authoring (also in Anthropic-imported list)
- `skill-share/` — collaboration/sharing infrastructure for skills
- `template-skill/` — SKILL.md scaffold template

**Pattern observation**: 3 of 31 (10%) skills are skills-about-skills. Recursive self-referential design. Distinct from awesome-list-genre prior 3 (which had no meta-content).

---

## composio-skills/ — 832-entry Rube MCP wrapper catalog

**Counts**:
- Total entries: 832
- Naming convention: `<toolkit-name>-automation/` (alphabetical)
- Marketplace manifest: `composio-skills/.claude-plugin/marketplace.json` (v2.0.0)
- All entries declare `requires: mcp: [rube]` in YAML frontmatter

**Sample entries** (alphabetical first 20 from `/bin/ls composio-skills/`):
```
-21risk-automation
-2chat-automation
ably-automation
abstract-automation
abuselpdb-automation
abyssale-automation
accelo-automation
accredible-certificates-automation
acculynx-automation
active-campaign-automation
addresszen-automation
adobe-automation
adrapid-automation
adyntel-automation
aero-workflow-automation
aeroleads-automation
affinda-automation
affinity-automation
agencyzoom-automation
agent-mail-automation
```

**Anomaly observed**: First two entries (`-21risk-automation`, `-2chat-automation`) have leading hyphens — likely a slugification artifact for toolkit names that begin with digits. Cosmetic but potentially breaks some shell tools.

**Architectural pattern (verified via slackbot-automation sample)**:
```yaml
---
name: slackbot-automation
description: "Automate Slackbot tasks via Rube MCP (Composio). Always search tools first for current schemas."
requires:
  mcp: [rube]
---
```

Each wrapper:
1. Declares MCP requirement explicitly in YAML
2. References Composio toolkit docs at `composio.dev/toolkits/<name>`
3. Instructs Claude to call `RUBE_SEARCH_TOOLS` first to fetch live schemas
4. Provides toolkit-specific tool sequences + parameter guidance + pitfalls
5. **Is non-functional without Rube MCP commercial signup**

This is the corpus-first observation of:
- Explicit MCP-requirement declaration in skill YAML at scale (Pattern #18 corpus-first)
- Commercial-product-as-fulfillment-layer for an aggregated catalog (Pattern #50 sub-variant)
- "Live-schema-first" skill design (skill instructs Claude to fetch tool schemas at runtime rather than embedding stale schemas in skill text)

---

## connect-apps-plugin/ — commercial product entry-point as bundled skill

**Manifest** (`.claude-plugin/plugin.json`):
```json
{
  "name": "connect-apps",
  "description": "Manage auth and connect to 500+ apps using Composio. Perform real actions from Claude Code - send emails, create issues, post messages, and more.",
  "author": {"name": "Composio", "email": "support@composio.dev"}
}
```

**Install flow (verbatim from README)**:
```bash
claude --plugin-dir ./connect-apps-plugin
/connect-apps:setup
# Paste API key from dashboard.composio.dev
exit
claude
```

**Pattern #50 sub-variant: "commercial-product-entry-as-bundled-skill"** — corpus-first observation. Composio ships their commercial product's auth-and-connect entry-point as a Claude Code plugin shipped INSIDE the OSS aggregator. Quickstart pushes user to install + authenticate to dashboard.composio.dev within 4 commands.

**Pattern #59 sub-variant: "directory-as-marketplace"** — corpus-first directory-scoped marketplace.json (`composio-skills/.claude-plugin/marketplace.json`) is structurally distinct from prior Pattern #59 sub-variants (59a marketplace+npm OMC v27 / 59b marketplace-only claude-hud v35).

---

## License variation summary

| License presence | Count | Skills |
|------------------|-------|--------|
| **Apache-2.0 LICENSE.txt** at skill level | 9 of 31 top-level (29%) | artifacts-builder, brand-guidelines, canvas-design, internal-comms, mcp-builder, skill-creator, slack-gif-creator, theme-factory, webapp-testing |
| **No LICENSE** at skill level (relies on root claim) | 22 of 31 top-level + 832 composio-skills (97% by file count) | All Composio-built skills + all 832 Rube wrappers |

**Pattern #29 corpus-first observation**: a SINGLE repo with **4 license-presence tiers** simultaneously:
1. Root LICENSE: ABSENT
2. README claim: Apache-2.0 (badge + License section)
3. Per-skill LICENSE.txt: Present in 9 skills (Apache-2.0 verbatim from Anthropic-import)
4. YAML frontmatter `license:` field: Present in skill-creator only (`license: Complete terms in LICENSE.txt`)

This 4-tier license-presence structure is corpus-first.

---

## Storm Bear pilot relevance

**Direct-pilot candidates** (clone-and-copy to `~/.config/claude-code/skills/`; zero commercial coupling; verifiable Apache-2.0 in 5 of these 5):
1. `file-organizer/` — vault organization (HIGH leverage)
2. `content-research-writer/` — Storm Bear publishing assistance (MEDIUM)
3. `meeting-insights-analyzer/` — Scrum retrospective analysis (HIGH for Scrum-coach role)
4. `changelog-generator/` — Storm Bear corpus version-history automation (MEDIUM)
5. `tailored-resume-generator/` — Storm Bear self-positioning when publishing (LOW priority)

**Pilot estimate**: 30-60 minutes to clone + place 5 skills + verify activation.

**AVOID for Storm Bear without commercial-policy review**:
- `connect-apps-plugin/` (commercial signup required)
- All 832 `composio-skills/*-automation/` (Rube MCP commercial dependency)

See `03 Beginner Guide` for full pilot protocol.

---

## Cross-references

- `01 Cluster Summaries/(C) Cluster 2` — full filesystem inventory
- `02 Entity Pages/(C) Composio Commercial Ecosystem + Rube MCP + Pattern #50 Corpus-Strongest.md` — Rube MCP commercial product analysis
- `02 Entity Pages/(C) Storm Bear Meta-Entity v50` — 5-skill pilot rationale + Pattern #57 recursion
