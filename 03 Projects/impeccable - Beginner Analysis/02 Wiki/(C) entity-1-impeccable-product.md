# (C) Entity 1 — impeccable (T1 Assistant Skill / Design-Language)

## Identity

- **Name:** impeccable
- **Tagline:** "The design language that makes your AI harness better at design."
- **Repo:** https://github.com/pbakaus/impeccable
- **Homepage:** https://impeccable.style
- **License:** Apache 2.0 (with NOTICE.md derivative-attribution chain)
- **Latest release:** Skill 3.1.1 (2026-05-14)
- **Tier:** T1 Assistant Skill
- **Primary lang:** JavaScript 93.2% + Astro 2.3% + CSS 3.3%
- **Scale:** 28,816 stars / 1,559 forks / 57 watchers / 21 open issues / 669 commits

## Velocity-screen

| Metric | Value | Signal |
|--------|-------|--------|
| Repo age | 185 days (created 2025-11-16) | mid-launch |
| Stars/day | **155.8** | **Pattern #52 HIGH-NOT-EXTREME sub-class N=4** |
| Fork ratio | 0.054 | drive-by-stars-dominant |
| Watcher/star | 0.00198 | low engagement-per-star |
| Issue/star | 0.00073 | low issue-rate |

## What it is

A **plug-and-play frontend-design skill** for AI coding tools. Single skill ID (`/impeccable`), 23 sub-commands, 7 reference domains, 27 deterministic anti-pattern rules, standalone CLI detector (`npx impeccable detect`).

Built by Paul Bakaus as a derivative of Anthropic's official `frontend-design` skill (Apache 2.0), with additional tactical content incorporated from ehmo's `typecraft-guide-skill`.

## What it does (3-layer interaction model)

1. **Skill** — installable into 14 different AI harnesses; invoked via `/impeccable <command> [target]`; loads `PRODUCT.md` + `DESIGN.md` context before any command
2. **CLI detector** — `npx impeccable detect <path-or-URL>` scans HTML / directories / URLs for 27 anti-pattern violations without API key required
3. **Browser extension + plugin** — additional packaging surfaces from `extension/` and `plugin/` directories

## Command surface (23 commands in 6 category-tints)

| Category (tint) | Commands |
|-----------------|----------|
| Create (magenta) | craft / shape / teach / document |
| Evaluate (purple) | critique / audit |
| Refine (blue) | bolder / quieter / distill |
| Simplify (amber) | (refine variants) |
| Enhance / Harden (green) | animate / colorize / typeset / layout / harden |
| System (gray) | live / polish / clarify / document |

Plus 35 markdown files in `/skill/reference/` covering both reference domains and command-specific guidance.

## Design system (7 domains)

| Domain | Anchor rule |
|--------|-------------|
| Color | OKLCH-only; warm paper neutrals + one decisive magenta accent (≤10% screen coverage) |
| Typography | Cormorant Garamond italic (display) + Instrument Sans (body); 65-75ch line cap |
| Elevation | Flat-by-default; shadows respond to state-change only |
| Components | Squared buttons; minimal inputs; periodic-table-grid command surface |
| Spacing | 8/16/24/32/48/80/120px (4px deliberately omitted) |
| Motion | Expo-out easing `cubic-bezier(0.16, 1, 0.3, 1)`; 150-1200ms |
| Layout | Max-width 900-1400px; asymmetric grids; 65-75ch prose constraints |

## 27 anti-pattern rules (deterministic)

A non-exhaustive list of banned moves: pure black/white, left-border color stripes, gradient text, dark mode defaults, glassmorphism, second accent colors, bounce easing, layout animation, nested cards, identical card grids, hero-metric templates, hedging copy, non-standard spacing tokens, plus ~14 others.

Detection: `npx impeccable detect <target>` runs all 27 rules against an HTML file, directory, or URL. Reports violations with rule-name + line/selector + severity. Zero API key.

## Distribution surface (CORPUS-RECORD 14 harness-target directories)

```
.agents/skills/impeccable          (generic agents/ convention)
.claude/skills/impeccable          (Claude Code)
.claude-plugin                     (Claude plugin marketplace)
.codex/agents                      (Codex CLI / TOML)
.cursor/skills/impeccable          (Cursor)
.gemini/skills/impeccable          (Gemini CLI)
.kiro/skills/impeccable            (Kiro)
.opencode/skills/impeccable        (OpenCode)
.pi/skills/impeccable              (Pi)
.qoder/skills/impeccable           (Qoder)
.rovodev/skills/impeccable         (Atlassian Rovo Dev)
.trae/skills/impeccable            (Trae)
.trae-cn/skills/impeccable         (Trae Chinese variant)
.impeccable                        (own metadata)
```

Compatibility differences (from HARNESSES.md): Claude Code = most comprehensive spec support / Cursor = reads from multiple directories / Gemini CLI = validates only `name`+`description` ignoring other fields / Codex = TOML sidecar / GitHub Copilot = moderate spec compliance / Trae = "no official skills docs found yet". Distribution is **research artifact AND product** — the HARNESSES.md spec-compliance matrix itself is corpus-first cross-harness research.

## Governance (9-file extensive discipline)

| File | Purpose |
|------|---------|
| `README.md` | Entry point + install + multi-harness compatibility |
| `CLAUDE.md` | Claude-specific routing (auxiliary) |
| `AGENTS.md` | Repository Guidelines: code style + build + testing |
| `DESIGN.md` | 7 design domains + 27 anti-patterns + critical restraint rules |
| `DEVELOP.md` | Build system + skill architecture v3.0+ |
| `HARNESSES.md` | 11-harness spec-compliance matrix |
| `PRODUCT.md` | Vision + target user + restraint philosophy |
| `STYLE.md` | Editorial voice + denylist + read-aloud test |
| `NOTICE.md` | Apache-2.0 + 2-source derivative-attribution chain |

## Build/release

- Runtime: Bun + ESM + 2-space indentation
- Lockfiles: bun.lock + pnpm-lock.yaml (dual packaging target)
- Tests: Bun `--test` + node `--test`; `*.test.js` / `*.test.mjs`
- TDD discipline for anti-pattern detection: fixture → failing test → rule → adapter
- Per-component versioning: skill 3.1.1 (2026-05-14) versioned separately from CLI / extension / plugin
- Site: Astro + biome.json + wrangler.toml (Cloudflare Worker for bundle downloads)

## Trade-offs

- **Strength**: opinionated discipline produces visually-coherent output; anti-pattern detector provides deterministic enforcement; multi-harness distribution surface eliminates lock-in risk
- **Weakness**: editorial denylist + 27 anti-patterns are deliberately restrictive — projects with brand requirements outside Bakaus's aesthetic (heavily-decorated SaaS landings, gaming UIs, retail e-commerce) will fight the system
- **Cost**: 9-file governance is heavyweight relative to lighter-weight Anthropic-original skill (1-2 files); contributor onboarding requires reading the governance docs

## Pattern Library implications (see entity 3)

- Pattern #84 84c N=4 strengthening with CORPUS-RECORD 14-harness multi-target distribution
- Pattern #57 STRONG corpus-recursive citation
- Pattern #52 HIGH-NOT-EXTREME sub-class N=4 lower-edge evidence
- Pattern #78 78a CLI-enforceable-LDS strengthening
- 3 NEW observational candidates (OC-U / OC-V / OC-W)
