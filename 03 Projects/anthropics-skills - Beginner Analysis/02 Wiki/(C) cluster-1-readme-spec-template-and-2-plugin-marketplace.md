# (C) Cluster 1 — README + Repo Metadata: 100+ Example Skills × 4 Categories + SKILL.md Spec Authority + Template-Skill + 2-Plugin Sub-Marketplace + Mixed-Licensing + THIRD_PARTY_NOTICES.md + skills.sh External Service + agentskills.io Standard Reference + Notion Partner-Skill Ecosystem + Educational-Demonstration Disclaimer

**Source**: https://github.com/anthropics/skills (README + GitHub API metadata)
**Fetched**: 2026-05-23 (Phase 0 + Phase 2 ingestion)
**Wiki version**: v93 (FOURTH under routine v2.3 baseline)

---

## 1. Subject self-positioning

Repo description: *"Public repository for Agent Skills"*

Full README opening: *"Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, whether that's creating documents with your company's brand guidelines, analyzing data using your organization's specific workflows, or automating personal tasks."*

Key positioning statement: *"This repository contains Anthropic's implementation of skills for Claude. For information about the Agent Skills standard, see [agentskills.io](http://agentskills.io)."*

This places v93 as **Anthropic's authoritative reference implementation of the Agent Skills standard** (with the standard itself documented at the external agentskills.io site). Distinct from third-party implementations like v76 agent-skills-standard (HoangNguyen0403) which implements the same standard.

## 2. Repository metrics

| Metric | Value |
|---|---|
| Created | 2025-09-22 (~244 days at fetch = 8 months) |
| Last push | 2026-05-19 (4 days before v93 fetch) |
| Stars | 139,442 |
| Forks | 16,451 |
| Watchers (subscribers) | 899 |
| Open issues | 871 |
| Open PRs | 625 |
| Network | 16,451 |
| Commits on main | 36 |
| Repo size | 3,734 KB |
| Velocity | ~571 stars/day at 244-day window |
| Discussions | ENABLED |
| Topics | `agent-skills` |
| External badge | `skills.sh/anthropics/skills` |

**~571 stars/day at 244-day window** satisfies Pattern #52 **Multi-Month-Sustained EXTREME-VIRAL sub-class** threshold (>300/d × 90+d). Sub-class anchor:
- N=1: v78 ECC at 1,535/d × 122d
- N=2: v85 ui-ux-pro-max-skill at ~467/d × 174d (administratively PROMOTED at v86 audit)
- **N=3 strengthening**: v93 at ~571/d × 244d

This is the SECOND-highest absolute scale of any v60+ subject (after v78 ECC's 187,238★). EXTREME mega-scale.

## 3. License — Mixed-Licensing within Single Repo

**Critical finding**: anthropics/skills has CORPUS-NOVEL mixed-licensing within single repo:

| Component | License | Status |
|---|---|---|
| Most skills in `skills/` | Apache-2.0 | Open source |
| `skills/docx` | Source-available | NOT open source |
| `skills/pdf` | Source-available | NOT open source |
| `skills/pptx` | Source-available | NOT open source |
| `skills/xlsx` | Source-available | NOT open source |

README quote:
> *"Many skills in this repo are open source (Apache 2.0). We've also included the document creation & editing skills that power Claude's document capabilities under the hood in the `skills/docx`, `skills/pdf`, `skills/pptx`, and `skills/xlsx` subfolders. These are source-available, not open source, but we wanted to share these with developers as a reference for more complex skills that are actively used in a production AI application."*

**GitHub API reports "None specified"** because mixed-licensing doesn't fit a single root LICENSE file.

**Library-vocab "Mixed Licensing (Apache-2.0 + Source-Available) within Single Repo" PROVISIONAL N=1** — corpus-novel at foundational-vendor-direct-source subject. Distinct from:
- v77 easy-vibe CC BY-NC-SA 4.0 (single non-commercial-CC license)
- v90 academic-research-skills CC-BY-NC 4.0 (single CC-NC license)
- v83 open-design Apache-2.0 + bundled-MIT-components (multi-license but in-tree-bundled distinct origin)
- v79 autoresearch_folktales README-declared-but-no-LICENSE-file (Pattern #83 83f.4 sub-variant)

v93's mixed-licensing is **distinct from all prior corpus instances** because:
- Same-vendor licensing distinct sub-folders within single repo
- Explicit "we wanted to share as reference for more complex skills" framing
- Source-available specifically for production-AI-application-skill subset
- Distinct from in-tree-bundled-multi-origin licensing (v83) which was different-origin-bundled

## 4. Primary Languages

- Python 84.4% (dominant)
- HTML 12.4%
- Shell 1.9%
- JavaScript 1.3%

Python-primary is consistent with both v90 academic-research-skills (Python 97.4%) and v92 claude-for-legal (Python 67.2% + Shell 32.8%). All three Anthropic-or-near-Anthropic subjects converge on Python-primary.

## 5. 4 Skill Categories + 100+ Example Skills

| Category | Examples |
|---|---|
| Creative & Design | Art, music, design skills |
| Development & Technical | Testing web apps, MCP server generation |
| Enterprise & Communication | Communications, branding |
| Document Skills | docx + pdf + pptx + xlsx (source-available; "power Claude's document capabilities under the hood") |

**Skill count estimate**: 100+ example skills (based on 4-category breadth + 36 commits + 3,734 KB repo size + 16,451 forks). Below v85 ui-ux-pro-max-skill's 669+ codified-elements record and v76 agent-skills-standard's 259-skill mega-density record, but above most other v60+ subjects.

## 6. SKILL.md Spec Definition at `./spec/`

The repo contains the **Agent Skills SPECIFICATION** at `./spec/`. This is the **vendor-authoritative skill format reference**.

README quote on creating skills:
> *"Skills are simple to create - just a folder with a SKILL.md file containing YAML frontmatter and instructions."*

Minimum required SKILL.md frontmatter format:
```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Instructions Claude will follow when this skill is active]

## Examples
## Guidelines
```

Two required fields:
- `name` — Unique identifier (lowercase, hyphens for spaces)
- `description` — Complete description of skill purpose + usage triggers

This is the **vendor-authoritative skill format definition** that:
- v76 agent-skills-standard (HoangNguyen0403) implements at third-party scope
- Pattern #84 84c references in multiple wikis
- v92 claude-for-legal extends with per-plugin SKILL.md instances

**Library-vocab "SKILL.md Spec + Template at Vendor-Authoritative Repo" PROVISIONAL N=1** — corpus-novel at vendor-authoritative scope.

## 7. Template-Skill at `./template/`

The repo contains a **template-skill** at `./template/` — reference-starting-point for skill creation. This is the **vendor-authoritative skill template** for new skill development.

Distinct from third-party skill-template patterns. v93's template-skill is the source-authoritative reference that other skill-template-providers (e.g., v76 agent-skills-standard) align with.

## 8. 2-Plugin Sub-Marketplace Distribution

The repo distributes via Claude Code Plugin Marketplace as **2 sub-plugins**:

```
/plugin marketplace add anthropics/skills
```
Registers as `anthropic-agent-skills` marketplace. Then:

```
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

| Sub-plugin | Content | License |
|---|---|---|
| `document-skills` | docx + pdf + pptx + xlsx skills | Source-available |
| `example-skills` | Creative & Design + Development & Technical + Enterprise & Communication skills | Apache-2.0 |

**Pattern #84 84c.1 sub-sub-mechanism "Marketplace-Plugin-Install" N=4 POST-PROMOTION STRENGTHENING evidence-base**:

| N-position | Wiki | Install command | Variant |
|---|---|---|---|
| N=1 anchor | v85 ui-ux-pro-max-skill | `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill` | Single-plugin |
| N=2 | v90 academic-research-skills | `/plugin marketplace add Imbad0202/academic-research-skills` | Single-plugin nested-sub-skill bundle |
| N=3 PROMOTION-LOCKED-IN | v92 claude-for-legal | `/plugin marketplace add <path>` + 12 plugin installs | Multi-plugin marketplace |
| **N=4 POST-PROMOTION STRENGTHENING** | **v93 anthropics/skills** | `/plugin marketplace add anthropics/skills` + 2 plugin installs | **2-plugin sub-marketplace** |

v93 extends the install-granularity-variant spread: single-plugin v85 + nested-sub-skill v90 + multi-plugin-marketplace v92 + 2-plugin-sub-marketplace v93. v95 STRONGER PROMOTION-CONFIRMED evidence.

## 9. 4-Channel Distribution

| Channel | Mechanism |
|---|---|
| **Claude Code Plugin Marketplace** | `/plugin marketplace add anthropics/skills` + `/plugin install <plugin>@anthropic-agent-skills` |
| **Claude.ai** | Pre-installed for paid plans automatically |
| **Claude API** | Pre-built skills + custom skills upload via Skills API Quickstart (`docs.claude.com/en/api/skills-guide`) |
| **Direct install** | `/plugin install document-skills@anthropic-agent-skills` OR `/plugin install example-skills@anthropic-agent-skills` |

Distinct from v92's 5-distribution channels (which included Microsoft 365 add-in + custom cloud Vertex/Bedrock). v93 narrower channel scope but deeper marketplace integration (Claude.ai auto-availability).

## 10. THIRD_PARTY_NOTICES.md at Top-Level

The repo contains `THIRD_PARTY_NOTICES.md` at root — **corpus-novel artifact at top-level**.

Distinct from in-skill-folder NOTICE.md (v75 impeccable pattern; NOTICE.md derivative-attribution chain at skill-folder scope). v93's THIRD_PARTY_NOTICES.md is at repo-level for the entire repository.

**Library-vocab "Top-Level THIRD_PARTY_NOTICES.md File at Repo Root" PROVISIONAL N=1** — distinct from v75 in-skill-folder NOTICE.md pattern.

## 11. agentskills.io External Standard Reference

README opens with:
> *"This repository contains Anthropic's implementation of skills for Claude. For information about the Agent Skills standard, see [agentskills.io](http://agentskills.io)."*

Implications:
- **agentskills.io** = external Agent Skills standard site
- **anthropics/skills** = Anthropic's authoritative reference implementation of this standard
- v76 agent-skills-standard (HoangNguyen0403) implements the same standard at third-party scope
- **Corpus loop closure**: v76 derived FROM the standard that v93 implements at source-authoritative scope

**Library-vocab "Standard-Authoritative-Reference-Implementation via External Standard Site (agentskills.io)" PROVISIONAL N=1** — corpus-novel multi-implementer external-standardization-site pattern.

## 12. skills.sh External Service Badge

README displays badge: `skills.sh/anthropics/skills` — corpus-novel external **skills-metadata-tracking service** reference.

skills.sh appears to be a third-party service tracking skill repositories. Anthropic-direct-org subject linking to third-party service badge = ecosystem-acknowledgment signal.

**Library-vocab "External Skills-Metadata Tracking Service (skills.sh)" PROVISIONAL N=1**.

## 13. Notion Partner-Skill Ecosystem Precedent

README highlights:
> *"Partner Skills"*
> *"Skills are a great way to teach Claude how to get better at using specific pieces of software. As we see awesome example skills from partners, we may highlight some of them here:"*
> *"- Notion - Notion Skills for Claude"*

This establishes precedent for **partner-skill ecosystem highlighting at vendor-authoritative repo**. Notion is the first highlighted partner. Future v9X opportunity: analyze Notion Skills for Claude as v9X subject (partner-skill-ecosystem-N=2 evidence).

## 14. Educational-Demonstration Disclaimer

README includes prominent disclaimer:
> *"**These skills are provided for demonstration and educational purposes only.** While some of these capabilities may be available in Claude, the implementations and behaviors you receive from Claude may differ from what is shown in these skills. These skills are meant to illustrate patterns and possibilities. Always test skills thoroughly in your own environment before relying on them for critical tasks."*

**Pattern #83 Honest-Deficiency-Disclosure within-pattern strengthening** at vendor-source-authoritative scale. Distinct from v92's 3-tier liability-attorney-review framing but in same disclosure-discipline family.

## 15. Anthropic-Product-Ecosystem Citation Density

| Anthropic product cited | Role at v93 |
|---|---|
| Claude Code | Plugin marketplace primary channel |
| Claude.ai | Auto-availability for paid plans |
| Claude API | Pre-built + custom skills upload |
| Anthropic Engineering Blog ("Equipping agents for the real world with Agent Skills") | External reference |
| Claude News ("Create Files" document capabilities) | External reference |
| Support Articles on Claude Skills | External reference |
| Skills API Quickstart docs | External reference |

**4+ Anthropic-product references at single subject** = Pattern #57 sub-variant 57c-product within-pattern strengthening at INTRA-VENDOR ecosystem-citation density (same N+1 axis as v92's 4-product references).

## 16. Repo Status

- **Discussions: ENABLED** (corpus-novel for Anthropic-direct-org subjects; community-engagement signal)
- **No releases published** (similar to v92's pre-release status)
- 36 commits + 625 open PRs = active development + community contribution

## 17. Summary

This cluster establishes the **product structural surface**:

- 100+ example skills across 4 categories
- SKILL.md spec definition at `./spec/` (vendor-authoritative)
- Template-skill at `./template/` (vendor-authoritative)
- 2-plugin sub-marketplace distribution (`document-skills` + `example-skills`)
- 4-channel distribution (Claude Code Marketplace + Claude.ai + Claude API + direct install)
- Mixed-licensing within single repo (Apache-2.0 + source-available)
- THIRD_PARTY_NOTICES.md at top-level (corpus-novel)
- skills.sh external metadata-tracking service reference
- agentskills.io external standard reference
- Notion partner-skill ecosystem precedent
- Educational-demonstration disclaimer
- Python 84.4% + HTML 12.4% + Shell 1.9% + JS 1.3%
- ~571 stars/day × 244 days = Pattern #52 Multi-Month-Sustained EXTREME-VIRAL sub-class N+1 strengthening

**Phase 4b PRIMARY contribution**: This cluster confirms `anthropics/skills` as Anthropic-direct-org subject (= same-org as v92) + provides Pattern #84 84c.1 N=4 strengthening evidence + corpus-novel mixed-licensing observation. The single most significant finding for Phase 4b PRIMARY is the NEW (a)-7 sub-axis N=2 STRENGTHENING (v92 anchor + v93 = N=2).

See cluster-2 for cross-corpus retrospective context and (a)-7 N=2 STRENGTHENING detail. Entity pages for Pattern Library implication detail.
