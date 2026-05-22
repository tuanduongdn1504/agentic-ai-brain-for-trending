# (C) Entity 2 — Distribution: 18-harness NEW CORPUS-RECORD + `skill.json` formal manifest + multi-symlink + uipro-cli

**Entity scope**: How `ui-ux-pro-max-skill` reaches users — 18-platform NEW CORPUS-RECORD harness ecosystem + `skill.json` formal manifest + multi-symlink SSOT architecture + uipro-cli npm distribution + Claude Marketplace.

## 18-harness multi-platform NEW CORPUS-RECORD

**From skill.json `platforms` array (verbatim 18 entries)**:

| # | Platform | Corpus reference / notes |
|---|---|---|
| 1 | **claude** | v65 Claude Code system prompts corpus subject |
| 2 | **cursor** | v75/v76 Cursor corpus subject |
| 3 | **windsurf** | v76 mention (Windsurf in 10+ AI agents list) |
| 4 | **copilot** | v76 mention (GitHub Copilot CLI) |
| 5 | **kiro** | v75 .kiro/ directory + v83 Kiro CLI |
| 6 | **roocode** | NEW (not in prior corpus) |
| 7 | **kilocode** | v83 Kilo (variant; same vendor likely) |
| 8 | **codex** | v62 Codex CLI corpus subject |
| 9 | **qoder** | v83 Qoder CLI |
| 10 | **gemini** | v83 Gemini CLI |
| 11 | **trae** | v82 + v83 corpus citations |
| 12 | **opencode** | v67 opencode-antigravity-auth corpus subject |
| 13 | **continue** | NEW (Continue Dev assumed) |
| 14 | **codebuddy** | NEW |
| 15 | **droid** | NEW (Factory droid per `.factory/` symlink in CLAUDE.md) |
| 16 | **warp** | NEW (Warp terminal AI) |
| 17 | **augment** | NEW (Augment Code) |
| 18 | **antigravity** | **v67 corpus-recursive citation** (opencode-antigravity-auth at platform-layer) |

**18 platforms = NEW CORPUS-RECORD harness count** (exceeds v83's prior 16-harness record by 2).

**10 corpus-subject overlaps** (CORPUS-RECORD-HIGH at single-subject scope):
- claude (v65) + cursor (v75/v76) + codex (v62) + kiro (v75/v83) + qoder (v83) + trae (v82/v83) + windsurf (v76) + gemini (v83) + opencode (v67) + antigravity (v67)

= **Pattern #57 sub-variant 57c-product STRONGEST in v60+ window** (exceeds v83's 7-citation density by 3).

**11-consecutive-wiki Pattern #84 84c arc v71→v85 = NEW CORPUS-RECORD** (extends v83's 10-wiki arc by 1).

## `skill.json` formal manifest (CORPUS-FIRST in v60+ window)

**Full verbatim** (902 bytes):

```json
{
  "name": "ui-ux-pro-max",
  "displayName": "UI/UX Pro Max",
  "description": "AI-powered design intelligence with 67 UI styles, 161 color palettes, 57 font pairings, 99 UX guidelines, and 25 chart types across 15+ tech stacks.",
  "version": "2.5.0",
  "author": "NextLevelBuilder",
  "license": "MIT",
  "homepage": "https://uupm.cc",
  "repository": "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill",
  "keywords": ["ui", "ux", "design", "design-system", "color-palette",
               "typography", "accessibility", "ai-skill"],
  "platforms": ["claude", "cursor", "windsurf", "copilot", "kiro",
                "roocode", "kilocode", "codex", "qoder", "gemini",
                "trae", "opencode", "continue", "codebuddy", "droid",
                "warp", "augment", "antigravity"],
  "install": "npx uipro-cli init --ai {{platform}}"
}
```

**Structural elements**:
- `name` + `displayName` separation (programmatic-id + human-readable)
- `version` 2.5.0 (semver discipline; corpus-first version-tracking via skill.json field)
- `author` (singular field; not multi-author)
- `homepage` URL (product domain `uupm.cc`)
- `repository` URL (GitHub origin)
- `keywords` 8-entry array (npm-compatible discoverability)
- `platforms` 18-entry array (harness-target enumeration)
- `install` template string with `{{platform}}` placeholder

= **CORPUS-FIRST `skill.json` formal Claude-Code-skill manifest in v60+ window** — Library-vocab item #12 "LLM-routing artifacts" N strengthening.

**Artifact-type cluster** (Library-vocab item #12 cumulative):
- `NOTICE.md` (v75 NOTICE.md 2-source attribution)
- `HARNESSES.md` (v75 14-harness routing)
- `AGENTS.md` (v76 agent-skills-standard 3-tier router)
- `llms.txt` (v77 easy-vibe + v81 taste-skill)
- `skill.json` (v85 ui-ux-pro-max formal manifest)

= 5-instance LLM-routing-artifact taxonomy at Library-vocab #12; PROMOTION-ELIGIBLE at v86 audit administrative.

## Multi-symlink SSOT architecture (CORPUS-FIRST in v60+ window)

**Topology**:

```
src/ui-ux-pro-max/                     ← SOURCE OF TRUTH
   ├── data/      (CSV databases)
   ├── scripts/   (Python search engine)
   └── templates/ (Markdown + JSON)
        ▲
        │  (symlinks ↓)
        │
   ┌────┼────────────────────────────────┐
   │    │                                │
   ├ .claude/skills/ui-ux-pro-max/       │  ← Claude Code skill
   ├ .factory/skills/ui-ux-pro-max/      │  ← Factory droid skill
   └ .shared/ui-ux-pro-max/              │  ← shared cross-platform
        │
        └─────────────────────────────────┘

cli/                                    ← npm package distribution
   └── assets/                          ← bundled assets (~564KB)
        ├── data/                       ← COPY of src/ data/
        ├── scripts/                    ← COPY of src/ scripts/
        └── templates/                  ← COPY of src/ templates/
```

**Sync rules** (verbatim CLAUDE.md):
> *"Data & Scripts - Edit in `src/ui-ux-pro-max/`: Changes automatically available via symlinks in `.claude/`, `.factory/`, `.shared/`"*

**Manual sync required only for CLI** (verbatim):
> *"CLI Assets - Run sync before publishing: cp -r src/ui-ux-pro-max/data/* cli/assets/data/..."*

= **CORPUS-FIRST multi-symlink-architecture-for-cross-platform-SSOT in v60+ window** Library-vocab candidate PROVISIONAL N=1.

**Distinction from prior corpus distribution architectures**:
- v75 impeccable: 14 harness directories × repo-stored REPLICAS (no symlinks)
- v83 open-design: 16 harness directories × repo-stored REPLICAS (no symlinks)
- v76 agent-skills-standard: CLI-generates-native-formats (template-generation; no symlinks)
- **v85 ui-ux-pro-max: multi-symlink SSOT + CLI-bundled-assets HYBRID** (symlinks for in-tree harnesses + CLI assets-copy for npm-published variant)

## uipro-cli npm package distribution

**Install entry-point** (skill.json `install` field):
```
npx uipro-cli init --ai {{platform}}
```

**Per-platform invocation** (18 variants):
```bash
npx uipro-cli init --ai claude       # → Claude Code skill
npx uipro-cli init --ai cursor       # → Cursor rules
npx uipro-cli init --ai windsurf     # → Windsurf config
npx uipro-cli init --ai copilot      # → GitHub Copilot
npx uipro-cli init --ai kiro         # → Kiro
# ... 13 more
```

**CLI source** (CLAUDE.md architecture):
- `cli/src/commands/init.ts` — install command with template generation
- `cli/utils/template.ts` — template rendering engine
- `cli/assets/` — bundled ~564KB (data + scripts + templates copies)

= **CLI-generates-native-formats-from-canonical-source** (Pattern #84 sub-mechanism 84c.2) N strengthening from v76; **13 stack templates × 18 platforms = 234 potential template combinations**.

## Claude Marketplace via `.claude-plugin/` directory

**CLAUDE.md verbatim**:
> *".claude-plugin/   # Claude Marketplace publishing"*

= **CORPUS-FIRST `.claude-plugin/` artifact-type in v60+ window** Library-vocab candidate PROVISIONAL N=1; distinct distribution-channel from `npm install` + `npx skills add` + Claude Code internal skill resolution.

## 4-distribution-channel summary

| Channel | Mechanism | Discovery |
|---|---|---|
| 1 | `npm install -g uipro-cli && uipro init --ai claude` | npm registry global install |
| 2 | `npx uipro-cli init --ai {{platform}}` | npm registry zero-install |
| 3 | Claude Marketplace via `.claude-plugin/` | Claude's curated marketplace |
| 4 | `git clone` + direct symlink to `.claude/` etc. | Manual install (dev mode) |

= 4-distribution-channel matrix (sister to v83's 4-method matrix; different mechanism mix but same axis-count = N=2 STRENGTHENING for Library-vocab "4-Distribution-Method Matrix at single subject" candidate, registered at v83).

## Pattern Library implications (Entity 2 scope)

| Pattern / Item | Evidence | Strength |
|---|---|---|
| **NEW CORPUS-RECORD 18-harness count** | skill.json 18-entry platforms array | NEW CORPUS-RECORD by 2 |
| **11-consecutive-wiki Pattern #84 84c arc v71→v85 = NEW CORPUS-RECORD** | Extends v83 10-wiki record by 1 | STRONG |
| **CORPUS-FIRST `skill.json` formal Claude-Code-skill manifest** | 902-byte manifest with platforms + keywords + install | Library-vocab item #12 N strengthening to N=5 |
| **CORPUS-FIRST multi-symlink-architecture-for-cross-platform-SSOT** | .claude/ + .factory/ + .shared/ → src/ | Library-vocab PROVISIONAL N=1 |
| **CORPUS-FIRST `.claude-plugin/` artifact-type** | Claude Marketplace distribution mechanism | Library-vocab PROVISIONAL N=1 |
| **Pattern #84 84c.2 CLI-generates-native-formats N strengthening** | uipro-cli template-generation; 13 × 18 = 234 combinations | Within-pattern strengthening |
| **Pattern #57 sub-variant 57c-product STRONGEST in v60+ window** | 10 corpus-subject overlaps in 18-platform list | STRONG strengthening (exceeds v83 7) |
| **Pattern #57 corpus-recursive sub-chain v85 → v67** | "antigravity" topic + platform citations | Sub-variant 57j candidate |
| **4-distribution-channel matrix N=2 STRENGTHENING with v83** | npm install + npx + Claude Marketplace + git clone | Library-vocab strengthening |
| **Library-vocab item #12 LLM-routing artifacts N=5** | NOTICE.md + HARNESSES.md + AGENTS.md + llms.txt + skill.json | PROMOTION-ELIGIBLE at v86 audit |

## Cross-wiki siblings (Entity 2)

- **v83 open-design** — 16-harness prior CORPUS-RECORD now SURPASSED; 4-distribution-method N=2 strengthening
- **v76 agent-skills-standard** — CLI-generates-native-formats sub-mechanism 84c.2 anchor; v85 N strengthening
- **v75 impeccable** — repo-stored-N-harness-replicas (14) vs v85 symlink-architecture
- **v67 opencode-antigravity-auth** — "antigravity" corpus-recursive citation at platform-layer + "opencode" platform overlap
- **v77 easy-vibe / v81 taste-skill** — llms.txt artifact-type siblings in Library-vocab item #12 cluster

## Open questions specific to Entity 2

- `uipro-cli` actual npm registry status (verify package exists + download count)
- Bundled assets ~564KB — Claude Marketplace size constraint compliance
- Whether all 18 platforms have actual template files in `templates/platforms/` or some are placeholders
- `roocode` / `continue` / `codebuddy` / `warp` / `augment` corpus-eligibility scoring
- Multi-symlink architecture: how does it behave on Windows (symlink-permission constraints)?
