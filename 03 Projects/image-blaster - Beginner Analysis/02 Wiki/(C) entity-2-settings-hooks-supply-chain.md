# (C) Entity 2 — Settings + hooks + supply-chain: per-skill allowlist + 2-hook agent-runtime-enforcement + Bun-primary + 1-harness

**Entity scope**: How `image-blaster` enforces agent-runtime behavior via `.claude/settings.json` permission allowlist + 2-hook combination + tight Bash scoping + Bun-primary packaging.

## `.claude/settings.json` (1,004 bytes verbatim)

### `permissions.allow` array — per-skill + tight-Bash

**Per-skill allowlist (8 entries)** — explicit `Skill(name)` syntax for all 8 image-blast skills:
- `Skill(image-blast-project)`
- `Skill(image-blast-uncover)`
- `Skill(image-blast-world)`
- `Skill(image-blast-3d)`
- `Skill(image-blast-sfx)`
- `Skill(image-blast-plate)`
- `Skill(image-blast-image-edit)`
- `Skill(image-blast-wildcard)`

**Bash allowlist (8 entries) — tight scoping; no broad `Bash(*)`**:
- `Bash(ls:*)`
- `Bash(node .claude/scripts/*:*)`
- `Bash(node .claude/scripts/project/show-url.mjs:*)` (specific script)
- `Bash(bun install:*)`
- `Bash(bun run dev:*)`
- `Bash(lsof:*)`
- `Bash(mkdir:*)`
- `Bash(cd:*)`

= **CORPUS-FIRST tight Bash-scoping (no broad shell) at settings.json scope in v60+ window**. Library-vocab candidate PROVISIONAL N=1.

### `hooks` object — 2 lifecycle events

| Hook | Trigger | Script | Inferred purpose |
|---|---|---|---|
| **SessionStart** | When Claude Code session begins | `setup-check.sh` | Verify environment (API keys + dependencies + project state) |
| **UserPromptSubmit** | Every user prompt | `input-check.sh` | Validate input (images in `input/` + sanity-check pre-emission) |

= **CORPUS-FIRST 2-hook SessionStart + UserPromptSubmit combination at project-CLAUDE.md scope in v60+ window**. Library-vocab candidate PROVISIONAL N=1.

**Comparison with prior corpus**:
- v83 open-design: Anti-AI-slop machinery + P0/P1/P2 gates as enforcement layer, but NOT via Claude-Code hooks system specifically
- v76 agent-skills-standard: MCP Transparent-Interception server with audit logs (similar enforcement intent at MCP layer)
- v71 agents-best-practices: 7-loop invariant agentic-harness-execution-separation (methodology layer)
- v84: **First subject in v60+ window using Claude Code `hooks` settings.json mechanism with both SessionStart + UserPromptSubmit**

## Bun-primary packaging (CORPUS-FIRST candidate in v60+ window)

| Signal | Evidence |
|---|---|
| `bun.lock` (114,106 bytes) | Present at root |
| `bun install` allowed | settings.json Bash allowlist |
| `bun run dev` allowed | settings.json Bash allowlist |
| `package.json` (316 bytes) | Small/minimal |
| No `package-lock.json` at root | (Bun lock instead) |
| Separate `app/package-lock.json` for sub-app | Yes (163,722 bytes — npm sub-app lock) |

= **Bun-primary at top-level + npm at sub-app level** = hybrid packaging discipline.

Comparison with prior packaging-tool taxonomy in v60+ window:
- npm + `npx skills add` (v75 + v81 + v82)
- pnpm 10.33.x (v83 open-design)
- npm + pnpm-workspace (v76)
- uv (v74 LLMs-from-scratch; Python)
- Tauri + Rust (v73 cc-switch)
- .NET 8.0 + WPF (v80 SmartMacroAI)
- **Bun + sub-app npm** (v84 image-blaster)

= **CORPUS-FIRST Bun-primary packaging in v60+ window** PROVISIONAL N=1.

## 1-harness Claude-Code-only distribution

**Harness directories observed**:
- `.claude/` — full structure (agents + hooks + rules + scripts + settings + skills + .claudeignore)
- `.cursor/rules` — minimal (depth unverified)

**Harness directories NOT observed**:
- No `.codex/` / `.opencode/` / `.gemini/` / `.kiro/` / `.qoder/` / `.trae/` / `.pi/` / `.rovodev/` / `.windsurf/`

= **1 primary harness = Claude Code only**.

**Contrast with prior T1 skill cluster**:
- v75 impeccable: 14 harnesses (prior CORPUS-RECORD before v83 surpassed)
- v83 open-design: 16 harnesses (NEW CORPUS-RECORD)
- v82 huashu-design: 6 harnesses
- v81 taste-skill: ~4 harnesses
- **v84 image-blaster: 1 harness** (lowest in v60+ T1 skill cluster)

= **Deliberate single-harness narrowness** as design choice — v84 is opinionated about Claude Code as primary runtime; not portable-by-default.

= **Pattern #84 84c.1 NEGATIVE-evidence contrast** — first v60+ T1 subject to consciously NOT pursue multi-harness portability.

## Owner identity: Neilson K-S = SF solo indie creative-tech

| Field | Value | Storm Bear contrast |
|---|---|---|
| Login | `neilsonnn` | |
| Name | Neilson K-S | |
| Bio | *"gamer"* | (Storm Bear bio = software developer + Scrum coach) |
| Location | San Francisco | Vietnam |
| Personal domain | neilsonks.com | (Storm Bear has vault, not personal domain) |
| Twitter | @neilsonks | |
| Public repos | 10 | (Storm Bear vault scale unknown public) |
| Followers | 115 | |
| Following | 14 | |
| GH account age | ~12 years (since 2014-05) | |
| Type | User (individual) | |

= **Storm Bear (a) axis-call**: solo-indie axis SHARED but cultural-locale + domain-vertical DISTINCT. WEAK PASS at most.

= **Pattern #19 NEW sub-mechanism candidate "SF-Indie-Creative-Tech-Solo-Developer-with-Personal-Domain-and-Game-Vertical"** PROVISIONAL N=1 — distinct from prior 19a-19m sub-mechanisms.

## Pattern #66 supply-chain posture: STRONG within-pattern

| Axis | v84 posture |
|---|---|
| Text-only skill content | ✅ 8 SKILL.md + settings.json |
| **Per-skill explicit `Skill(name)` allowlist** | ✅ CORPUS-FIRST |
| **Tight Bash scoping (no broad `*`)** | ✅ CORPUS-FIRST |
| **SessionStart hook (setup-check.sh)** | ✅ NEW |
| **UserPromptSubmit hook (input-check.sh)** | ✅ CORPUS-FIRST |
| Per-skill SKILL.md spec | ✅ 8 files |
| Local-first asset loading | ✅ world skill discipline |
| Multi-vendor BYOK isolation | ✅ at asset-generation layer |
| Zero-telemetry | ✅ implicit |
| Schema validation | ⚠️ Not Phase 0 observed |
| No SECURITY.md | ❌ Not observed |

= **3 CORPUS-FIRST sub-mechanism candidates contributed** at v84 (per-skill allowlist + tight-Bash + UserPromptSubmit hook). STRONG within-pattern Pattern #66 strengthening at agent-runtime permission + hook layer.

## Pattern Library implications (Entity 2 scope)

| Pattern / Item | Evidence | Strength |
|---|---|---|
| **CORPUS-FIRST per-skill `Skill(name)` allowlist at settings.json scope** | 8-skill explicit enumeration | Library-vocab PROVISIONAL N=1 |
| **CORPUS-FIRST 2-hook SessionStart + UserPromptSubmit combination** | settings.json hooks object | Library-vocab PROVISIONAL N=1 |
| **CORPUS-FIRST tight Bash-scoping (no broad `Bash(*)`)** | 8 specific Bash entries | Library-vocab PROVISIONAL N=1 |
| **CORPUS-FIRST Bun-primary packaging in v60+ window** | bun.lock + Bash allowlist `bun install:*` + `bun run dev:*` | Library-vocab PROVISIONAL N=1 |
| **Pattern #84 84c.1 NEGATIVE-evidence contrast** | 1-harness Claude-Code-only deliberate single-harness narrowness | Within-pattern observation |
| **Pattern #19 NEW sub-mechanism "SF-Indie-Creative-Tech-Solo-Developer"** | Neilson K-S profile | PROVISIONAL N=1 |
| **Pattern #66 STRONG within-pattern at agent-runtime permission + hook layer** | 3 CORPUS-FIRST sub-mechanism candidates | STRONG strengthening |

## Cross-wiki siblings (Entity 2)

- **v83 open-design** — 16-harness CORPUS-RECORD CONTRAST vs v84 1-harness narrowness
- **v71 agents-best-practices** — 6-axis supply-chain methodology vs v84 5-axis with 3 NEW agent-runtime sub-mechanisms
- **v76 agent-skills-standard** — MCP Transparent-Interception vs v84 Claude-Code-hooks (both enforcement-at-agent-runtime intent at different layers)
- **v80 SmartMacroAI** — Windows-only platform-pin vs v84 Claude-Code-only harness-pin (both deliberate-narrowness; different axes)

## Open questions specific to Entity 2

- Content of `.claude/hooks/setup-check.sh` + `input-check.sh` scripts
- `.claude/agents/` + `.claude/rules/` directory content
- `.cursor/rules` content depth (1-line vs full ruleset)
- Whether `image-blast-wildcard` skill has settings.json-level distinction or is pure-prose-skill
- Whether Bun-primary observation is INTENTIONAL design choice or coincidental
