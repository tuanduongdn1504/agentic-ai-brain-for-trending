# (C) Cluster 2 — `skill.json` formal manifest + 18-harness NEW CORPUS-RECORD + uipro-cli npm + multi-symlink

**Source bundle**: `skill.json` (902 bytes verbatim) + CLAUDE.md architecture diagram + uipro-cli install commands.

## `skill.json` verbatim (902 bytes)

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
  "keywords": [
    "ui", "ux", "design", "design-system", "color-palette",
    "typography", "accessibility", "ai-skill"
  ],
  "platforms": [
    "claude", "cursor", "windsurf", "copilot", "kiro",
    "roocode", "kilocode", "codex", "qoder", "gemini",
    "trae", "opencode", "continue", "codebuddy", "droid",
    "warp", "augment", "antigravity"
  ],
  "install": "npx uipro-cli init --ai {{platform}}"
}
```

= **CORPUS-FIRST `skill.json` formal Claude-Code-skill manifest in v60+ window** — Library-vocab item #12 LLM-routing artifacts N strengthening (`skill.json` joins prior artifact-type cluster: `AGENTS.md` v76 + `HARNESSES.md` v75 + `llms.txt` v77/v81 + `NOTICE.md` v75 + `skill.json` v85).

## 18-harness multi-platform NEW CORPUS-RECORD

**Verbatim platforms array from skill.json**:

| # | Platform | Corpus reference |
|---|---|---|
| 1 | **claude** | v65 (Claude Code system prompts) |
| 2 | **cursor** | v75/v76 corpus subject (Cursor) |
| 3 | **windsurf** | v76 mention (Windsurf in 10+ AI agents list) |
| 4 | **copilot** | v76 mention (GitHub Copilot) |
| 5 | **kiro** | v75 .kiro/ + v83 Kiro CLI |
| 6 | **roocode** | NEW (not in prior corpus) |
| 7 | **kilocode** | v83 Kilo (similar; not v85 Kilocode confirmed-same) |
| 8 | **codex** | v62 corpus subject |
| 9 | **qoder** | v83 Qoder CLI |
| 10 | **gemini** | v83 Gemini CLI |
| 11 | **trae** | v82 + v83 corpus citations |
| 12 | **opencode** | v67 corpus subject (opencode-antigravity-auth) |
| 13 | **continue** | NEW (not in prior corpus) |
| 14 | **codebuddy** | NEW |
| 15 | **droid** | NEW (Factory droid; per CLAUDE.md .factory/) |
| 16 | **warp** | NEW (Warp terminal AI) |
| 17 | **augment** | NEW |
| 18 | **antigravity** | **v67 corpus-recursive citation** (opencode-antigravity-auth; corpus-recursive sub-chain candidate at platform-layer) |

**18 platforms = NEW CORPUS-RECORD harness count** (exceeds v83's 16-harness prior record by 2).

**10 corpus-subject overlaps** with prior corpus:
- claude (v65)
- cursor (v75/v76)
- codex (v62)
- kiro (v75 + v83)
- qoder (v83)
- trae (v82 + v83)
- windsurf (v76)
- gemini (v83)
- opencode (v67)
- antigravity (v67 corpus-recursive)

= **CORPUS-RECORD-HIGH corpus-subject-citation count within single platforms-list** (10 corpus subjects vs v83's 7).

**8 NEW platforms** (not in prior corpus): roocode + continue + codebuddy + droid + warp + augment + (kilocode if distinct from Kilo v83) + (windsurf if distinct from windsurf-ai v83 topic vs v85 explicit platform).

= **11-consecutive-wiki Pattern #84 84c arc v71→v85 = NEW CORPUS-RECORD** (extends v83 10-wiki record by 1).

## uipro-cli npm package distribution

**Install command (skill.json `install` field verbatim)**:
```
npx uipro-cli init --ai {{platform}}
```

**Per-platform invocation**:
```bash
npx uipro-cli init --ai claude       # → installs Claude Code skill
npx uipro-cli init --ai cursor       # → installs Cursor rules
npx uipro-cli init --ai windsurf     # → installs Windsurf config
# ... 18 platform variants
```

**Distribution architecture** (CLAUDE.md verbatim):
> *"Reference Folders - No manual sync needed. The CLI generates these from templates during `uipro init`."*

= **CLI-generates-native-formats-from-canonical-source** (Pattern #84 sub-mechanism 84c.2 introduced by v76 + N strengthening at v85).

`uipro-cli` is npm-published TypeScript package (`cli/src/commands/init.ts` + `cli/utils/template.ts` template-rendering engine + `cli/assets/` bundled ~564KB).

## Multi-symlink architecture (CORPUS-FIRST in v60+ window)

**Symlink topology** (CLAUDE.md verbatim):

```
src/ui-ux-pro-max/     ← Source of Truth (CSV data + Python scripts + templates)
   ↑
   ├── .claude/skills/ui-ux-pro-max/    ← symlink (Claude Code skill)
   ├── .factory/skills/ui-ux-pro-max/  ← symlink (Droid / Factory skill)
   └── .shared/ui-ux-pro-max/          ← symlink (shared cross-platform)
```

**Sync rules** (verbatim):
> *"Data & Scripts - Edit in `src/ui-ux-pro-max/`: Changes automatically available via symlinks in `.claude/`, `.factory/`, `.shared/`"*

= **CORPUS-FIRST multi-symlink-architecture-for-single-source-of-truth in v60+ window**. Library-vocab candidate "Multi-Symlink-Architecture-for-Cross-Platform-SSOT" PROVISIONAL N=1.

Distinct from prior corpus distribution patterns:
- v75 impeccable: 14-harness × repo-stored replicas (no symlinks)
- v83 open-design: 16-harness × repo-stored replicas (no symlinks)
- v76 agent-skills-standard: CLI-generates-native-formats (template-generation, no symlinks)
- **v85 ui-ux-pro-max-skill: symlinks + CLI-generates-templates combo** = hybrid architecture

## CLI sub-app distribution (`cli/` directory)

**`cli/` structure** (per CLAUDE.md):
- `cli/src/commands/init.ts` — install command with template generation
- `cli/utils/template.ts` — template rendering engine
- `cli/assets/data/` — copy of `src/ui-ux-pro-max/data/` (~564KB bundled)
- `cli/assets/scripts/` — copy of `src/ui-ux-pro-max/scripts/`
- `cli/assets/templates/` — copy of `src/ui-ux-pro-max/templates/`

**Sync discipline** (verbatim):
> *"Run sync before publishing: `cp -r src/ui-ux-pro-max/data/* cli/assets/data/`"*

= Manual-sync-before-npm-publish discipline; bundled assets ~564KB inside the npm package.

## `.claude-plugin/` for Claude Marketplace

Verbatim CLAUDE.md:
> *".claude-plugin/   # Claude Marketplace publishing"*

= CORPUS-FIRST `.claude-plugin/` artifact-type observation in v60+ window (Claude Marketplace distribution mechanism distinct from `npx skills add` + skill.json install). Library-vocab candidate "Claude-Marketplace-Distribution-via-.claude-plugin-Directory" PROVISIONAL N=1.

## 13-stack template generation taxonomy

Per CLAUDE.md verbatim:
> *"Available stacks: `html-tailwind` (default), `react`, `nextjs`, `astro`, `vue`, `nuxtjs`, `nuxt-ui`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`, `jetpack-compose`"*

13 stacks × 18 platforms = **234 potential template combinations** generated by `uipro-cli`.

= **CORPUS-RECORD template-generation matrix density** in v60+ window.

## Pattern Library implications (Cluster 2 scope)

| Pattern / Item | Evidence | Strength |
|---|---|---|
| **NEW CORPUS-RECORD 18-harness count** | 18-platform skill.json (exceeds v83 16 by 2) | NEW CORPUS-RECORD |
| **11-consecutive-wiki Pattern #84 84c arc v71→v85 = NEW CORPUS-RECORD** | Extends v83 10-wiki record by 1 | STRONG |
| **CORPUS-FIRST `skill.json` formal Claude-Code-skill manifest** | Formal 902-byte manifest with platforms + keywords + install | Library-vocab item #12 N strengthening |
| **CORPUS-FIRST multi-symlink-architecture for cross-platform SSOT** | .claude/ + .factory/ + .shared/ symlinks to src/ | Library-vocab PROVISIONAL N=1 |
| **CORPUS-FIRST `.claude-plugin/` artifact-type** | Claude Marketplace distribution mechanism | Library-vocab PROVISIONAL N=1 |
| **Pattern #84 84c.2 CLI-generates-native-formats N strengthening** | uipro-cli template-driven per-platform per-stack generation; 13 × 18 = 234 combinations | Within-pattern strengthening |
| **Pattern #57 sub-variant 57c-product STRONGEST in v60+ window** | 10 corpus-subject overlaps in 18-platform list | STRONG (exceeds v83 7) |
| **Pattern #57 corpus-recursive sub-chain v85 → v67** | "antigravity" platform citation → v67 opencode-antigravity-auth | Sub-chain candidate |
| **CORPUS-RECORD template-generation matrix density** | 13 stacks × 18 platforms = 234 combinations | Within-pattern observation |

## Cross-wiki siblings (Cluster 2)

- **v83 open-design** — 16-harness prior record now SURPASSED by v85 18; 4-distribution-method matrix vs v85 1-method (npx uipro-cli)
- **v76 agent-skills-standard** — CLI-generates-native-formats N strengthening; 259-skill vs v85 669+ different LDS axes
- **v75 impeccable** — repo-stored-N-harness-replicas (14) vs v85 symlink-architecture
- **v67 opencode-antigravity-auth** — "antigravity" corpus-recursive citation at v85 platform-layer

## Open questions specific to Cluster 2

- Whether `uipro-cli` npm package source is fully in this repo or external (assumed in `cli/` per CLAUDE.md)
- Whether `kilocode` ≠ `kilo` (v83 named "Kilo")
- Whether `continue` is Continue Dev CLI or different product
- Whether `.claude-plugin/` is shipped or build-step-only
- Bundled assets ~564KB — is this within Claude Marketplace size limit?
