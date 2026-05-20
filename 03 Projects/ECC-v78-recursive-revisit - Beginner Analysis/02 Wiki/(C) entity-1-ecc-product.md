# (C) Entity 1 — ECC product (v78 corpus-recursive revisit)

## Identity (verified 2026-05-20)

- **Name:** ECC (Everything Claude Code — repo renamed from `everything-claude-code` since v1)
- **Tagline:** "The harness-native operator system for agentic work. From an Anthropic hackathon winner."
- **Secondary:** "Not just configs. A complete system: skills, instincts, memory optimization, continuous learning, security scanning, and research-first development."
- **Repo:** https://github.com/affaan-m/ECC
- **Homepage / Pro:** https://ecc.tools
- **License:** MIT (verified GitHub API 2026-05-20)
- **Tier:** T1 Assistant Skill / **Multi-Harness Operator System** (cross-archetype)
- **Created:** 2026-01-18 → wiki probe 2026-05-20 = 122 days
- **Last push:** 2026-05-20 (active today; weekly-ship cadence)
- **Primary lang:** Shell + TypeScript + Python + Go + Java + Perl + Markdown (12+ language ecosystems)
- **Scale:** **187,238 stars / 28,997 forks / 1 open issue / 1,974 commits / 170+ contributors**

## Velocity (CORPUS-RECORD)

| Metric | Value | Signal |
|--------|-------|--------|
| Repo age | 122 days | sustained multi-month window |
| Stars/day | **1,535** | **CORPUS-RECORD top-velocity** — exceeds v63 Karpathy (~1,186/d) + v68 zero (1,050/d) |
| Fork ratio | **0.155** | strong active-deployment (5× v76 agent-skills-standard 0.296 prior record? Actually 0.155 < 0.296 — within active-deployment-norm band) |
| Watcher/star | (not probed at this pass) | — |
| Issue/star | **0.0000053** | engagement-deficit-extreme territory (Library-vocab #11 candidate) |

## What it is

**ECC = the harness-native operator system for agentic work** — production-ready agents + skills + hooks + rules + MCP configurations + legacy command shims evolved over 10+ months of intensive daily use building real products. Works across Claude Code + Codex + Cursor + OpenCode + Gemini + Zed + GitHub Copilot + 4+ other AI agent harnesses.

The v1 anchor described "Everything Claude Code" as a Claude-Code-centric framework collection (8 documented entity domains: Skills / Commands / Hooks / Plugins / Subagents / MCPs / Rules-and-Memory / Security). The v78 corpus-recursive revisit observes the same subject as having undergone meta-architecture transformation:

- **From Claude-Code-only → multi-harness operator system** (11+ harness directories in repo)
- **From small skill collection → 232 skills + 60 agents + 75 legacy command shims** (CORPUS-RECORD codification density)
- **From OSS-only → dual-tier OSS + paid ECC Pro at $19/seat/mo**
- **From individual project → Anthropic Hackathon Winner + 170+ contributors + 187K star community**
- **From English-only → 10+ locale i18n including Vietnamese**
- **From v1 unversioned → v2.0.0-rc.1 Hermes operator release** (semver-versioned product layer)

## 5 core principles (from CLAUDE.md)

1. **Agent-First** — Delegate to specialized agents for domain tasks
2. **Test-Driven** — Write tests before implementation, 80%+ coverage required
3. **Security-First** — Never compromise on security; validate all inputs
4. **Immutability** — Always create new objects, never mutate existing ones
5. **Plan Before Execute** — Plan complex features before writing code

Plus explicit **Prompt Defense Baseline** (corpus-first explicit prompt-injection-defense baseline at project-CLAUDE.md scope; v71 agents-best-practices had threat-model coverage but ECC ships in-CLAUDE.md prompt-defense rules).

## 11+ harness directory topology

```
.claude/         .codex/          .cursor/        .opencode/
.gemini/         .kiro/           .trae/          .qwen/
.zed/            .codebuddy/      .agents/        + .vscode/ .github/ .claude-plugin/
```

Compare to v75 impeccable (14 harness-dirs CORPUS-RECORD) and v76 agent-skills-standard (15+ harnesses via CLI-generated native formats). ECC at 11+ harness-dirs at repo-stored layer is comparable Pattern #84 84c.1 evidence.

## 60 agents + 232 skills + 75 commands (CORPUS-RECORD codification density at single subject)

- **60 specialized agents** (planner, architect, tdd-guide, code-reviewer, security-reviewer, build-error-resolver, e2e-runner, refactor-cleaner, doc-updater, cpp-reviewer, fsharp-reviewer, docs-lookup, go-reviewer, kotlin-reviewer, database-reviewer, python-reviewer, django-reviewer, etc.)
- **232 skills** (CORPUS-RECORD — exceeds v76 agent-skills-standard's 259 only by count-class; semantics differ: ECC skills are workflow-definitions vs v76 skills are framework-bound reusable codification)
- **75 legacy command shims** (Pattern #21 within-pattern — backward-compat for renames during 10+ month development)
- **12+ language ecosystem coverage** (Python + Go + Kotlin + C++ + F# + Django + TypeScript + Shell + Java + Perl + Markdown + others)

## Distribution + economic model (corpus-first dual-tier)

| Channel | Mechanism | Status |
|---------|-----------|--------|
| **Direct repo clone** | git clone affaan-m/ECC | MIT free |
| **npm `ecc-universal`** | cross-harness installer (weekly downloads) | MIT free |
| **npm `ecc-agentshield`** | security-scanning skill collection | MIT free |
| **GitHub App `ecc-tools`** | hosted PR audits + free tier (150+ installs) | freemium |
| **ECC Pro** | Private repos + GitHub App + $19/seat/mo | **paid SaaS tier** |
| **GitHub Sponsors** | Fund OSS work from $5/mo | community-funded |

This is **CORPUS-FIRST explicit dual-license-economic-model**: MIT-OSS base + hosted-Pro-SaaS-tier + community-sponsor channel. Prior corpus subjects were either pure-OSS (v74 + v75) or pure-commercial (v69 wrapper-with-binary-proprietary). ECC's "OSS stays free forever; Pro funds the maintainer" framing is corpus-first NEW Library-vocabulary item #13 candidate.

## i18n (10+ locales including Vietnamese)

| Locale | Path |
|--------|------|
| English | README.md (primary) |
| Português (Brasil) | docs/pt-BR/README.md |
| 简体中文 | README.zh-CN.md |
| 繁體中文 | docs/zh-TW/README.md |
| 日本語 | docs/ja-JP/README.md |
| 한국어 | docs/ko-KR/README.md |
| Türkçe | docs/tr/README.md |
| Русский | docs/ru/README.md |
| **Tiếng Việt** | **docs/vi-VN/README.md** (Storm Bear locale present) |
| ไทย | docs/th/README.md |

**Vietnamese-locale presence** = direct Storm Bear cultural-peer evidence at i18n layer. This is the first corpus subject in v60+ window with explicit VN locale (v77 easy-vibe has 13-locale CORPUS-RECORD-HIGH i18n but did not confirm VN locale at probe-level).

## v1 → v78 entity-page staleness map

The v1 wiki documented 11 entity pages at single-harness Claude-Code scope. v78 revisit observes which v1 entities are still accurate vs stale:

| v1 entity | v1 scope | v78 reality | Stale? |
|-----------|----------|-------------|--------|
| (C) Skills.md | Claude-Code skills (handful documented) | 232 skills + cross-harness | STALE (major) |
| (C) Commands.md | /commands at single-harness | 75 commands + legacy-shim layer | STALE (significant) |
| (C) Hooks.md | hooks at single-harness | hooks/ dir (preserved as architecture component) | partially valid |
| (C) Plugins.md | plugins concept | .claude-plugin/plugin.json + plugins/ dir | STALE (rename/restructure) |
| (C) Subagents.md | subagents | agents/ dir + 60 agents (rename) | STALE (rename) |
| (C) MCPs.md | MCP configs | mcp-configs/ + .mcp.json | partially valid |
| (C) Rules and Memory.md | rules-and-memory | rules/ + contexts/ + Hermes operator memory layer | STALE (significant) |
| (C) Security Guide summary.md | security guide | ecc-agentshield npm package + security-reviewer agent + Prompt Defense Baseline in CLAUDE.md | STALE (productized) |
| (C) Longform Guide summary.md | longform guides | Hermes operator setup guide + multi-locale guides | STALE (refactored) |
| (C) Shortform Guide summary.md | shortform guides | docs/architecture/cross-harness.md + release notes | STALE (refactored) |
| (C) README summary.md | v1 README | v78 README expanded (multi-locale + multi-harness + Pro tier) | STALE |

**Verdict:** 9/11 v1 entity pages are STALE at v78. v78 wiki entity pages (this set) form the current-state record; v1 entity pages remain as historical 2026-04-17 baseline.

## Trade-offs

- **Strength:** single-maintainer weekly-ship cadence at scale (rare in OSS at this size); explicit hackathon-winner provenance; multi-harness portability; 5-core-principle clarity; Vietnamese-locale + 10 languages; dual-tier economic model preserves OSS-free promise while funding maintainer; CORPUS-FIRST multi-month-sustained EXTREME-VIRAL velocity profile
- **Weakness:** 60 agents + 232 skills + 75 commands = high cognitive surface for newcomers; cross-harness applicability claims need per-harness verification; "ECC Pro vs free" boundary requires user understanding of feature-split; Hermes operator narrative is v2.0.0-rc.1 (release-candidate not stable); 1 open-issue at 187K stars suggests issue-tracker not the primary feedback channel (community discussion + GitHub App private channels) — visibility cost for outside contributors
- **Cost:** following 5 core principles + 80%+ coverage + plan-before-execute = significant team-adoption commitment; ECC Pro $19/seat/mo for organizations + sponsor model for individuals creates funding-path-divergence to manage

## Pattern Library implications (see entity 3)

- **Pattern #52 NEW sub-class "Multi-Month-Sustained EXTREME-VIRAL" N=1 PROMOTION-LOCKED-IN** (Phase 4b PRIMARY)
- Pattern #84 84c.1 N+1 evidence at repo-stored distribution layer (11+ harness-dirs)
- Pattern #57 STRONGEST corpus-recursive citation at maximum depth (7+ corpus-subject citations in single-subject product surface)
- NEW Library-vocabulary item #13 candidate "OSS-with-hosted-Pro-SaaS-tier-on-MIT-base"
- NEW observational candidate "Anthropic-Hackathon-Winner-Status as corpus-signal-axis"
- Pattern #19 sub-mechanism strengthening (Affaan Mustafa solo-maintainer + multi-product portfolio)
- Pattern #82 quantitative-marketing N+1 (5+ quantitative claims in README first 25 lines)
- Pattern #78 N+1 STRONGEST LDS-tracking (6-layer LDS surface)
- Pattern #66 supply-chain integrity (ecc-agentshield security-scanning skill collection)
- CORPUS-FIRST single-maintainer-N-harness-weekly-ship discipline
