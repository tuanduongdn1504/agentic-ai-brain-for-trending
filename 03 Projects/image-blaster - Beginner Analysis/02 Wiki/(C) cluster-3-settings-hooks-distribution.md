# (C) Cluster 3 — `.claude/settings.json` per-skill allowlist + 2-hook supply-chain + Bun-primary + 1-harness Claude-Code-only

**Source bundle**: `.claude/settings.json` (1,004 bytes; decoded verbatim) + repo tree + owner profile + Bun packaging signal.

## `.claude/settings.json` verbatim structure

```json
{
  "permissions": {
    "allow": [
      "Skill(image-blast-project)",
      "Skill(image-blast-uncover)",
      "Skill(image-blast-world)",
      "Skill(image-blast-3d)",
      "Skill(image-blast-sfx)",
      "Skill(image-blast-plate)",
      "Skill(image-blast-image-edit)",
      "Skill(image-blast-wildcard)",
      "Bash(ls:*)",
      "Bash(node .claude/scripts/*:*)",
      "Bash(node .claude/scripts/project/show-url.mjs:*)",
      "Bash(bun install:*)",
      "Bash(bun run dev:*)",
      "Bash(lsof:*)",
      "Bash(mkdir:*)",
      "Bash(cd:*)"
    ]
  },
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/setup-check.sh"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/input-check.sh"
          }
        ]
      }
    ]
  }
}
```

## Per-skill `Skill(name)` allowlist (CORPUS-FIRST observation in v60+ window)

Explicit allowlist syntax `Skill(image-blast-project)` etc. — **per-skill permission gate at settings.json scope**. All 8 image-blast skills enumerated.

= **CORPUS-FIRST per-skill explicit-allowlist syntax in v60+ window** Library-vocabulary candidate PROVISIONAL N=1.

## Tight Bash scoping (CORPUS-FIRST in v60+ window)

Bash allowlist is **deliberately narrow** — only:
- `ls:*`
- `node .claude/scripts/*:*` (sub-scripts)
- `node .claude/scripts/project/show-url.mjs:*` (specific script)
- `bun install:*`
- `bun run dev:*`
- `lsof:*`
- `mkdir:*`
- `cd:*`

= **No broad `Bash(*)`** + **no general shell access** = supply-chain discipline at agent-runtime permission layer.

Library-vocabulary candidate "Tight-Bash-Allowlist-as-Supply-Chain-Discipline-at-Settings.json-Scope" PROVISIONAL N=1.

## 2-hook combination (CORPUS-FIRST in v60+ window)

| Hook | Trigger | Script | Purpose |
|---|---|---|---|
| **SessionStart** | When Claude Code session begins | `setup-check.sh` | Verify environment readiness (API keys + dependencies + project state) |
| **UserPromptSubmit** | Every time user submits a prompt | `input-check.sh` | Validate input (e.g., images in `input/` directory + check sanity) |

= **CORPUS-FIRST SessionStart + UserPromptSubmit 2-hook combination at project-CLAUDE.md scope** in v60+ window.

Both hook scripts unverified at Phase 0 (not fetched). Library-vocabulary candidate "Agent-Runtime-Input-Validation-via-UserPromptSubmit-Hook" PROVISIONAL N=1.

## Bun-primary packaging (CORPUS-FIRST in v60+ window candidate)

- `bun.lock` (114,106 bytes) present at root
- Bash allowlist explicitly permits `bun install:*` + `bun run dev:*`
- `package.json` (316 bytes — small/minimal) present
- No `package-lock.json` at root (Bun lock instead); separate `app/package-lock.json` for sub-app

= **CORPUS-FIRST Bun-primary packaging in v60+ window candidate** (subject to verification across v60-v83 packaging-tool taxonomy). Distinct from:
- v83 open-design: pnpm 10.33.x primary
- v75/v81/v82 design-skills: `npx skills add` distribution
- v74 LLMs-from-scratch: `uv` (Python) primary
- v73 cc-switch: Tauri 2 + Rust
- v76 agent-skills-standard: npm + pnpm-workspace monorepo

Library-vocabulary candidate "Bun-Primary-Packaging-in-v60+-Window" PROVISIONAL N=1.

## 1-harness Claude-Code-only distribution

- `.claude/` directory present (full structure: agents/ + hooks/ + rules/ + scripts/ + settings.json + skills/)
- `.cursor/rules` directory present (depth unverified at Phase 0; likely Cursor-rules-only minimal)
- No `.codex/` / `.opencode/` / `.cursor/agents/` / `.gemini/` / `.kiro/` / `.qoder/` / `.trae/` / `.pi/` / `.rovodev/` directories

= **1 primary harness = Claude Code only** (vs v83's 16-harness CORPUS-RECORD + v75's 14-harness; lowest harness count in v60+ T1-skill cluster).

## Neilson K-S owner profile

| Field | Value |
|---|---|
| Login | `neilsonnn` |
| Name | Neilson K-S |
| Bio | *"gamer"* |
| Location | San Francisco |
| Blog | `https://neilsonks.com/` (personal domain) |
| Twitter | `@neilsonks` |
| Public repos | 10 |
| Followers | 115 |
| Following | 14 |
| GH account created | 2014-05-16 (~12-year-old account) |
| Type | User (individual, not org) |

= **Solo SF-located indie creative-tech developer with personal-domain + Twitter + modest-scale 10-repo / 115-follower portfolio**.

Pattern #19 NEW sub-mechanism candidate "SF-Indie-Creative-Tech-Solo-Developer-with-Personal-Domain-and-Game-Vertical" PROVISIONAL N=1 — distinct from prior sub-mechanisms 19a-19m which cluster around:
- Engineering / methodology-influence-node (Karpathy + Raschka + Bakaus + Hoang + Lin + 花叔)
- Standards-codifier (Hoang VN + DenisSergeevitch)
- Community-org (Datawhalechina + Tsinghua + nexu)

Neilson = pure indie-creative-tech archetype distinct from prior sub-mechanisms.

## Supply-chain posture (Pattern #66) summary

| Axis | v84 image-blaster posture | Comparable to |
|---|---|---|
| Text-only skill content | ✅ 8 SKILL.md + settings.json | v75 + v81 + v82 + v83 ✅ |
| Per-skill explicit allowlist | ✅ `Skill(name)` syntax for all 8 | CORPUS-FIRST in v60+ window |
| Tight Bash scoping | ✅ 8 specific Bash entries (no broad `*`) | CORPUS-FIRST in v60+ window candidate |
| SessionStart hook | ✅ setup-check.sh | NEW in v60+ window |
| UserPromptSubmit hook | ✅ input-check.sh | CORPUS-FIRST in v60+ window |
| Per-skill SKILL.md spec | ✅ 8 files | v75 + v81 + v82 + v83 ✅ |
| Schema validation | ⚠️ Not Phase 0 observed | v76 ✅ |
| Local-first asset loading | ✅ world skill local-first discipline | v82 ✅ |
| Multi-vendor BYOK isolation | ✅ at asset-generation layer | NEW at non-LLM layer |
| No SECURITY.md | ❌ Not observed | v75 + v81 + v82 + v83 same |
| Zero-telemetry | ✅ implicit (no telemetry observed) | v83 ✅ |

= **STRONG within-pattern Pattern #66 supply-chain discipline at agent-runtime permission + hook layer** (3 NEW sub-mechanism candidates contributed: per-skill allowlist + tight Bash scoping + UserPromptSubmit input-check hook).

## Pattern Library implications (Cluster 3 scope)

| Pattern / Item | Evidence | Strength |
|---|---|---|
| **CORPUS-FIRST per-skill `Skill(name)` allowlist syntax at settings.json scope** | Explicit 8-skill enumeration in settings.json `permissions.allow` array | Library-vocab candidate PROVISIONAL N=1 |
| **CORPUS-FIRST 2-hook SessionStart + UserPromptSubmit combination** | settings.json `hooks` object with both keys | Library-vocab candidate PROVISIONAL N=1 |
| **CORPUS-FIRST tight Bash scoping (no broad `Bash(*)`)** | 8 specific Bash entries in allowlist | Library-vocab candidate PROVISIONAL N=1 |
| **CORPUS-FIRST Bun-primary packaging in v60+ window** | bun.lock 114KB + Bash allowlist permits `bun install:*` + `bun run dev:*` | Library-vocab candidate PROVISIONAL N=1 |
| **1-harness Claude-Code-only distribution** | Only `.claude/` (full) + `.cursor/rules` (minimal); no other harness dirs | Pattern #84 84c.1 NEGATIVE-evidence contrast (deliberate single-harness narrowness) |
| **Pattern #19 NEW sub-mechanism candidate "SF-Indie-Creative-Tech-Solo-Developer-with-Personal-Domain-and-Game-Vertical"** | Neilson K-S profile | PROVISIONAL N=1 |
| **Pattern #66 within-pattern STRONG strengthening at agent-runtime permission + hook layer** | 5 supply-chain axes including 3 CORPUS-FIRST observations | STRONG within-pattern |

## Cross-wiki siblings (Cluster 3)

- **v83 open-design** — 4-distribution-method matrix vs v84 1-method; 16-harness vs v84 1-harness (deliberate inversions)
- **v82 huashu-design** — solo creative-influencer archetype sibling (花叔 China + Neilson SF; both creative-tech)
- **v71 agents-best-practices** — 6-axis supply-chain (vs v84's 5-axis with 3 NEW); both discipline-focused at supply-chain layer
- **v80 SmartMacroAI** — solo VN creative-tech (RPA) + dual-LLM-API vs v84 solo SF creative-tech (image-to-3D) + multi-vendor-non-LLM-API

## Open questions specific to Cluster 3

- Content of `.claude/hooks/setup-check.sh` + `input-check.sh` scripts (not Phase 0 fetched)
- `.cursor/rules` content depth (1-line vs full ruleset)
- `.claude/agents/` + `.claude/rules/` directories — what's inside?
- Whether Bun-primary observation generalizes (need to check v60-v83 packaging-tool taxonomy)
