# Subject — claude-plugins-official

**Repo**: https://github.com/anthropics/claude-plugins-official
**Homepage**: https://code.claude.com/docs/en/plugins
**Owner**: Anthropic PBC (organization)
**Tier**: T1 Plugin Marketplace (distribution-infrastructure-anchor)
**License**: NULL at root (per-subplugin LICENSE delegation; NEW Pattern #45 sub-typology candidate)
**Primary language**: Python
**Created**: 2025-11-20 (186 days old at v95 ship)
**Last push**: 2026-05-24 (1 day before fetch — actively maintained)
**Description**: "Official, Anthropic-managed directory of high quality Claude Code Plugins"

## Core metrics (v95 fetch, 2026-05-25)

| Metric | Value |
|---|---|
| Stars | 27,357 |
| Forks | 2,912 |
| Watchers (subscribers) | 189 |
| Open issues | **700** (CORPUS-RECORD-HIGH for engagement-density at vendor-direct-source) |
| Velocity | ~147.1 stars/day = Pattern #52 SUSTAINED-MODERATE-HIGH upper-edge |
| Discussions | Disabled |
| Wiki | Disabled |
| Topics | claude-code, mcp, skills |

## What it is

The **official Anthropic-managed plugin marketplace** for Claude Code. Curated directory of internal Anthropic-developed plugins + third-party partner plugins + community-submitted plugins. All distributed via `/plugin install {name}@claude-plugins-official` slash command.

## Three-layer plugin organization

### `/plugins/` — Internal Anthropic-developed (36 plugins)

| Category | Plugins |
|---|---|
| Dev tools | agent-sdk-dev / claude-md-management / commit-commands / feature-dev / hookify / mcp-server-dev / mcp-tunnels / plugin-dev / playground |
| Code quality | code-modernization / code-review / code-simplifier / pr-review-toolkit / security-guidance |
| Output styles | explanatory-output-style / learning-output-style / session-report |
| LSP integration | clangd-lsp / csharp-lsp / gopls-lsp / jdtls-lsp / kotlin-lsp / lua-lsp / php-lsp / pyright-lsp / ruby-lsp / rust-analyzer-lsp / swift-lsp / typescript-lsp |
| Skill / design | **frontend-design** (CORPUS-ANCHOR for v75 + v82 + v83) + **skill-creator** + example-plugin |
| Misc | claude-code-setup / cwc-makers / math-olympiad / ralph-loop |

### `/external_plugins/` — Third-party partner repos (15 plugins)

asana / context7 / discord / fakechat / firebase / github / gitlab / greptile / imessage / laravel-boost / linear / playwright / serena / **telegram** / terraform

### `.claude-plugin/marketplace.json` — Marketplace manifest (~40+ source references)

Pulls in additional partners via `git-subdir` / `url` source declarations: 42Crunch + Adobe + Salesforce + Endor Labs + Aikido + Airtable + many more enterprise partners. Schema-referenced at `https://anthropic.com/claude-code/marketplace.schema.json`.

## Installation

```
/plugin install {plugin-name}@claude-plugins-official
```

Or browse via `/plugin > Discover` interface.

## Pattern Library cross-references

### Phase 0.9 (a)-7 sub-axis N=3 PROMOTION-LOCKED-IN

PRIMARY at v95. See Phase 4b proposal-document for full reasoning. (a)-7 advances from PROVISIONAL N=2 STRENGTHENING (v93) to **N=3 CONFIRMED** with v95 (cross-author + cross-vertical + cross-scale spread all PASS).

### Pattern #84 84c.1 Marketplace-Plugin-Install N=6 POST-PROMOTION STRENGTHENING

v85 + v90 + v92 + v93 + v94 + **v95** = 6-instance arc. **Subject IS the marketplace** that materializes the 84c.1 sub-sub-mechanism canonical install-pattern (`/plugin install {name}@claude-plugins-official`).

### Pattern #52 SUSTAINED-MODERATE-HIGH upper-edge N+1

~147/d × 186d sustained. Sits at the 150/d boundary between SUSTAINED-MODERATE-HIGH (25-150/d) and HIGH-NOT-EXTREME (150-300/d) sub-classes. Could promote to HIGH-NOT-EXTREME sub-class watch if 150+/d velocity sustained at v100+.

### Pattern #45 NEW sub-typology candidate

**"No-Root-LICENSE with Per-Subplugin-LICENSE-Delegation at Foundational-Vendor-Direct-Source Scale"** PROVISIONAL N=1. Corpus-novel for vendor-direct-org subjects. Distinct from existing 45a/b/c/d/e + Pattern #29 absent-LICENSE + Pattern #83 sub-mechanism 83f.4 README-Declared-but-no-LICENSE-file (v79 anchor).

### Pattern #66 supply-chain awareness

Explicit "⚠️ Important: Make sure you trust a plugin before installing, updating, or using it. Anthropic does not control what MCP servers, files, or other software are included in plugins and cannot verify that they will work as intended or that they won't change" disclaimer at README top. Honest supply-chain-risk acknowledgment at vendor-source-authoritative scale.

### Pattern #83 Honest-Deficiency-Disclosure

Three-layer honest disclosure: (1) supply-chain trust caveat above; (2) "Please see each linked plugin for the relevant LICENSE file" license-non-uniformity acknowledgment; (3) external-plugin "must meet quality and security standards for approval" but does not warrant downstream behavior.

### Pattern #57 sub-variant 57c-product within-pattern strengthening

Single subject contains ~36 internal-plugin self-citations + 15 external-partner citations + ~40 marketplace.json source-citations = **CORPUS-HIGH intra-vendor + intra-marketplace citation density** at single subject.

### Distribution-Infrastructure-Anchor for corpus-recursive chain

**v95 is upstream of**:
- v92 claude-for-legal 12-plugin bundle (distributed via `/plugin install`)
- v93 anthropics/skills sub-marketplace (sibling-marketplace pattern)
- v75 impeccable + v82 huashu-design + v83 open-design (all reference Anthropic `frontend-design` which is HERE at `/plugins/frontend-design/`)
- v88 teleport (sibling to `/external_plugins/telegram/`)
- v62/v88 Linear (corpus-recursive to `/external_plugins/linear/`)

Corpus-novel observational class. Library-vocab PROVISIONAL N=1.

## Library-vocab PROVISIONAL N=1 registrations at v95

1. **Two-Tier Plugin Directory (Internal + External + Marketplace.json) at Vendor-Authoritative Scope**
2. **External-Plugin-Submission-Process via Vendor-Curated Form (clau.de/plugin-directory-submission)**
3. **Anthropic-Managed Curated-Marketplace Framing**
4. **No-Root-LICENSE with Per-Subplugin-LICENSE-Delegation at Foundational-Vendor-Direct-Source Scale**
5. **Schema-Referenced Marketplace.json with $schema URL**
6. **Distribution-Infrastructure-Anchor for Corpus-Recursive Chain**

## Direct vault-applicable plugins (Storm Bear pilot candidates)

| Plugin | Vault-applicability |
|---|---|
| `claude-md-management` | Directly applicable to ~22KB root CLAUDE.md shim work + per-project CLAUDE.md governance |
| `skill-creator` | Directly applicable to routine v2.3 → v2.4 codification work + `_state/01-skill-references.md` skill refresh |
| `session-report` | Potentially useful for vault session-handoff discipline (currently distributed across Weekly Update narrative + Latest activity sections) |
| `frontend-design` | CORPUS-RECURSIVE — Anthropic's foundational design skill that v75 impeccable + v82 huashu-design + v83 open-design all reference; pilot at minimum-cost to understand the upstream source |
| `pr-review-toolkit` | Useful if/when vault becomes shared-edit |
| `security-guidance` | Useful for routine v2.4 supply-chain-discipline enhancements |
| `commit-commands` | May help standardize vault commit message style |

## Outstanding questions for operator review

1. **Pilot decision**: trial first-batch plugins (`claude-md-management` + `skill-creator` + `session-report`) now?
2. **Audit deferral**: v95 = 1-WIKI-DEFERRAL of natural audit cadence. Strongly recommend v96 = audit-only (projected ~66-74-item batch = NEW CORPUS-RECORD if executed)
3. **(a)-7 sub-axis administrative-promotion**: confirm v96 audit administrative-promotion to formal Phase 0.9 (a) sub-axis member (v2.3 §9 6-axis → 7-axis taxonomy expansion)
4. **v2.4 codification trigger**: cumulative v90-v95 codification candidates now ~17-20 items; (a) taxonomy expansion is candidate for early mini-codification ahead of normal cadence
