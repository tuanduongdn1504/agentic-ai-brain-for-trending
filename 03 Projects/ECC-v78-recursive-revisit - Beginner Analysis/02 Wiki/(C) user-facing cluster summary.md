# (C) Cluster: User-facing — what ECC delivers + how users adopt it

## In one sentence

ECC is an **MIT-licensed harness-native operator system** for AI-assisted software development, shipped as production-ready **agents + skills + hooks + commands + MCP configurations** across 7+ AI harnesses (Claude Code + Codex + Cursor + OpenCode + Gemini + Zed + GitHub Copilot), built by Anthropic Hackathon Winner **Affaan Mustafa** over 10+ months of intensive daily use, with **187K+ stars + 170+ contributors + 10+ locale i18n (including Vietnamese)** and a freemium **ECC Pro** hosted tier ($19/seat/mo) on top of MIT-OSS-free-forever base.

## The 5 core principles (from CLAUDE.md)

> "Agent-First. Test-Driven. Security-First. Immutability. Plan Before Execute."

| Principle | What it means | Outcome |
|-----------|---------------|---------|
| **Agent-First** | Delegate domain tasks to specialized agents | 60 agents covering planning, architecture, TDD, code-review, security-review, build-resolution, e2e, refactoring, docs, language-specialists (Python/Go/Kotlin/C++/F#/Java/Django/Database) |
| **Test-Driven** | Write tests before implementation; 80%+ coverage required | tdd-guide agent; per-skill SKILL.md test sections; tests/ directory |
| **Security-First** | Never compromise on security; validate all inputs | security-reviewer agent; ecc-agentshield npm package; Prompt Defense Baseline in CLAUDE.md |
| **Immutability** | Always create new objects, never mutate existing | applies across agent + skill + hook implementation |
| **Plan Before Execute** | Plan complex features before writing code | planner + architect agents; /plan command |

Plus **Prompt Defense Baseline** as a 6-axis baseline in CLAUDE.md (CORPUS-FIRST explicit at project-CLAUDE.md scope — covers role/persona resistance, secret protection, output validation, unicode/homoglyph awareness, untrusted-data treatment, harmful-content refusal).

## 4 distribution channels

| Channel | Cost | Best for |
|---------|------|----------|
| **git clone affaan-m/ECC** | free MIT | Reading the source, full repo install |
| **npm `ecc-universal`** | free MIT | Cross-harness installer; weekly downloads tracked |
| **npm `ecc-agentshield`** | free MIT | Security-scanning skill collection (standalone) |
| **GitHub App `ecc-tools`** | freemium | PR audits with free tier; 150+ installs |
| **ECC Pro** | **$19/seat/mo** | Private repos + GitHub App with full features |
| **GitHub Sponsors** | $5+/mo | Fund OSS work; supports single-maintainer cadence |

The economic model is explicit: **OSS stays free forever; Pro funds the maintainer.** Sponsors + Pro subscribers underwrite the single-maintainer-weekly-cadence-across-7-harnesses workflow.

## 10+ language locales

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
| **Tiếng Việt** | **docs/vi-VN/README.md** |
| ไทย | docs/th/README.md |

Vietnamese-locale README inclusion makes ECC a **direct cultural-peer-locale subject** for Storm Bear's vault context.

## 7+ harness multi-target

Works across (per README): **Claude Code (primary), Codex, Cursor, OpenCode, Gemini, Zed, GitHub Copilot.** Repo also includes harness dirs for Kiro, Trae, Qwen, Codebuddy = 11+ harness directories at repo-stored layer.

## Key commands (slash commands invoked by users)

- `/tdd` — Test-driven development workflow
- `/plan` — Implementation planning
- `/e2e` — Generate and run E2E tests
- `/code-review` — Quality review
- `/build-fix` — Fix build errors
- `/learn` — Extract patterns from sessions
- `/skill-create` — Generate skills from git history
- 75 total commands (with legacy command shims preserving backward-compat through renames)

## How to start

1. **Visit https://github.com/affaan-m/ECC**
2. **Read the language-appropriate README** — Vietnamese at `docs/vi-VN/README.md`
3. **Choose distribution channel:**
   - Full vibe: `git clone` + read CLAUDE.md + AGENTS.md
   - Quick install: `npm install -g ecc-universal`
   - Security-only subset: `npm install -g ecc-agentshield`
   - Hosted-PR-audits: install ECC GitHub App
4. **Pick a single agent to evaluate** — `planner` + `tdd-guide` are common starting points
5. **Adopt 5-principle workflow** — agent-first + test-driven + security-first + immutability + plan-before-execute

## Target users + outcomes

| User segment | Primary outcome |
|--------------|------------------|
| Solo developers | 60-agent + 232-skill workflow accelerates daily coding |
| Engineering teams | Codified standards + planning + review + security discipline at team scale |
| AI tool builders | Harness-native operator-system as reference architecture |
| Vault users (Storm Bear cohort) | Skill collection deployable directly via `.claude/` install |
| OSS hackathon participants | Reference implementation of Anthropic-Hackathon-Winner project |

## v1 → v78 delta (for users following the project since v1)

If you adopted ECC at v1 (2026-04-17), the meta-architecture has shifted substantially:

- **Renamed**: `everything-claude-code` → `ECC`
- **Cross-harness**: from Claude-Code-only to 7+ supported harnesses
- **Productized**: ECC Pro paid tier launched
- **Versioned**: v2.0.0-rc.1 Hermes operator release
- **Localized**: 10+ locales including Vietnamese
- **Hackathon-validated**: Anthropic Hackathon Winner status added
- **Scaled**: from documented-handful skills → 232 codified skills + 60 agents

## When NOT to adopt ECC

- You need single-harness simplicity (ECC is opinionated multi-harness operator-system; 60 agents is high cognitive surface)
- You want to avoid SaaS dependency (Pro tier creates funding-path; OSS stays free but Pro is incentivized)
- You prefer building skills from scratch (ECC's 232 skills are batteries-included)
- You don't have 5-principle discipline for daily workflow (test-driven + plan-before-execute require commitment)

## Fast facts

- 🌟 **187,238 stars** at 122 days = **1,535 stars/day** (CORPUS-RECORD velocity)
- 🍴 **28,997 forks** = fork ratio 0.155 (strong active-deployment)
- 👥 **170+ contributors** (Anthropic Hackathon-driven community + ongoing PRs)
- 📚 **60 agents + 232 skills + 75 commands**
- 🌐 **10+ locales** including Vietnamese
- 🚀 **7+ supported harnesses** + 11+ harness directories in repo
- 📜 **MIT OSS** forever + paid **ECC Pro** at $19/seat/mo + GitHub Sponsors
- 🏆 **Anthropic Hackathon Winner**
- 📦 **2 npm packages** (ecc-universal + ecc-agentshield)
- 🤖 **GitHub App** ecc-tools with 150+ installs
- 🛡️ **Prompt Defense Baseline** + ecc-agentshield + security-reviewer agent
- 🇻🇳 **Vietnamese-locale README** = direct Storm Bear cultural-peer-locale match
