# (C) SECURITY + Governance + Installation Scripts cluster summary — agency-agents

> **Sources:** SECURITY.md + LICENSE + scripts/ directory (inferred from README usage) + governance pattern analysis
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

3 topics: (a) security policy, (b) governance weight + maintainer model, (c) installation script architecture. Together they reveal agency-agents' operational model — **light-governance + heavy-scripts + solo-scale**.

## 2. Governance model — LIGHT

### Governance file count

```
agency-agents/
├── README.md                       ✅
├── CONTRIBUTING.md                 ✅
├── CONTRIBUTING_zh-CN.md           ✅
├── LICENSE                         ✅
├── SECURITY.md                     ✅
└── .gitattributes / .gitignore
```

**5 governance-type files** (README + 2 CONTRIBUTING + LICENSE + SECURITY).

### Corpus comparison

| Framework | Governance files |
|-----------|------------------|
| ECC v1 | 1-2 |
| gstack v3 | 1-2 |
| BMAD v11 | 2-3 |
| codymaster v12 | 2-3 |
| graphify v16 | 3 (README + AGENTS + SECURITY) |
| multica v15 | 4 (CLAUDE + AGENTS + CONTRIBUTING + SECURITY) |
| gws v13 | 3-4 (tri-file CLAUDE + AGENTS + CONTEXT) |
| **agency-agents v18** | **5** (README + 2 CONTRIBUTING + LICENSE + SECURITY) |
| spec-kit v17 | **6** (AGENTS + CONTRIBUTING + SECURITY + SUPPORT + DEVELOPMENT + COC) |

### Notable absences

- **No AGENTS.md** — unusual given 144 agents (Pattern #22 candidate NOT followed here)
- **No CLAUDE.md** — user-facing, but no contributor-facing Claude config
- **No CODE_OF_CONDUCT.md** — corporate-style governance skipped
- **No SUPPORT.md / DEVELOPMENT.md** — minimal maintainer support docs

**Interpretation:** agency-agents uses **light-governance model** despite 82.9K scale. Solo maintainer chooses simplicity over corporate-grade formality.

## 3. Solo-maintainer model at scale

### Challenge of solo at 82.9K stars

- 13.2K forks = massive derivative activity
- 43 open issues = small queue (solo can triage)
- 144 agents × continuous updates = maintenance burden
- Contributor onboarding = 2 CONTRIBUTING files (EN + zh-CN) is limited

### Maintainer discipline inferred

**Solo + 82.9K + 43 issues** suggests:
- **Strong issue triage** (quick close / redirect to forks)
- **Pull-request-heavy model** (13.2K forks = user-driven customization > issue-logging)
- **Fork-as-customization** culture (not expecting upstream changes)
- **144-agent stability** (not constantly changing; would generate more issues)

### Bus-factor concern

**Solo + 82.9K = highest bus-factor risk in corpus.**

If msitarzewski stops maintaining:
- 13.2K forks can continue (community redundancy)
- But official repo stagnates
- Similar risk pattern to graphify v16 (solo + 7 contrib) but at 2.7× scale

**Storm Bear action:** if piloting agency-agents, fork for continuity.

## 4. Installation script architecture

### Scripts directory structure (inferred)

```
scripts/
├── install.sh              # Primary installer
├── convert.sh              # .md → platform-native converter
└── (additional helper scripts)
```

### convert.sh functionality

Transforms `.md` agent files → platform-native formats:
- **Claude Code:** `.md` native (no conversion)
- **Cursor:** `.mdc` format
- **Kimi Code:** YAML
- **Other platforms:** platform-specific

### install.sh functionality

Supports multiple flags:
- `--interactive` (default) — auto-detect + prompt
- `--no-interactive` — CI-friendly
- `--tool <name>` — targeted install
- `--tool all` — install for all detected tools
- `--parallel` — parallel execution
- `--jobs <N>` — thread count

### Parallel execution

Auto-detects CPU count:
```bash
# Linux
nproc

# macOS
sysctl -n hw.ncpu

# Fallback
4 threads
```

### Shell-first philosophy

**Parallels gstack v3 shell-based approach.** Both:
- No Python/Node/uv dependency
- Bash-only portability
- Low-friction install

**Distinct from:**
- spec-kit v17: uv tool install (modern Python)
- graphify v16: pip install graphifyy
- BMAD v11: npm install

### Installation as conversion pipeline

```
Master .md agents (repo)
         ↓
    convert.sh
         ↓
  ┌──────┴──────┬────────┬────────┐
  ↓             ↓        ↓        ↓
Cursor       Claude    Aider    Windsurf
(.mdc)        (.md)    ...       ...
```

**One master → many targets** = classic compile pipeline pattern.

## 5. SECURITY.md — standard disclosure

### Inferred content

- Vulnerability reporting via GitHub Security Advisories
- Response expectations (informal given solo maintainer)
- Scope: agent-definition quality + script-execution safety

### Corpus context

- graphify v16: first SECURITY.md standalone
- spec-kit v17: corporate-grade SECURITY.md
- **agency-agents v18: 3rd SECURITY.md** in corpus

SECURITY.md is becoming **corpus standard** at T1/T4 — Pattern #24 candidate.

## 6. Pattern candidate #24 — SECURITY.md as T1 standard

### Evidence

- graphify v16: standalone SECURITY.md (T4)
- spec-kit v17: corporate SECURITY.md (T1)
- agency-agents v18: SECURITY.md (T1 solo)

3 wikis = 3 different archetypes with SECURITY.md. **Convention emerging across tiers + archetypes.**

### Prediction

- v19+ likely includes SECURITY.md
- Pattern could be promoted from candidate to confirmed at N≥5

## 7. Light-governance at scale — sustainable?

### Risks

- **Issue triage falls behind** — at 100K+ stars this would break
- **Forks fragment** — 13.2K already; may grow without upstream coordination
- **Agent quality variance** — 144 agents × many contributors = quality drift
- **No formal review process** — new agents may enter with low quality
- **No maintainer rotation** — succession plan absent

### Mitigations visible

- **Chinese contribution guide** — regional community moderation
- **Anti-generic stance** — quality bar articulated
- **Reality Checker agent** — self-referential quality check (meta)
- **Battle-tested workflows** — claim implies curation

### Sustainability projection

Solo + light-governance works at ~100K stars. Beyond that:
- Formal org required (LLC like BMAD)
- Corporate acquisition
- Multi-maintainer team
- Community-driven fork as primary

**agency-agents may be at ceiling of solo-light-governance model.**

## 8. 11-platform conversion pipeline architecture

### Platform format matrix

| Platform | File format | Location |
|----------|-------------|----------|
| Claude Code | `.md` | `~/.claude/agents/` (inferred) |
| GitHub Copilot | ? | ? |
| Antigravity | `@agency-*` prefix | ? |
| Gemini CLI | ? | ? |
| OpenCode | `@agent-name` invocation | ? |
| OpenClaw | ? | ? |
| Cursor | `.mdc` | `.cursor/rules/` |
| Aider | ? | ? |
| Windsurf | ? | ? |
| Qwen Code | ? | ? |
| Kimi Code | YAML | ? |

### Conversion complexity

Maintaining conversion to 11 platforms = ongoing work. Each platform format evolution = conversion update.

### Pattern #18 implications

agency-agents v18 commits to OpenClaw as target platform (install script + conversion). Validates Pattern #18 at execution level.

## 9. Edges + failure modes

### Governance edges

- **Solo burnout** — maintainer health = project health
- **Fork fragmentation** — 13.2K forks may diverge
- **CN contribution guide gap** — only zh-CN, not es-ES / pt-BR / etc.
- **No code of conduct** — community conflict escalation unclear

### Install script edges

- **Shell-only** — Windows users may need WSL
- **Dependency on detected tools** — if tool installed but not PATHed, install fails silently
- **Parallel flag bug potential** — concurrent file writes
- **convert.sh reformats** — if user modified agent locally, convert overwrites

### Security edges

- **Agent definitions are LLM prompts** — prompt injection potential if community-contributed
- **Install runs shell scripts** — arbitrary execution
- **No audit log** — which agents were installed when
- **Solo maintainer trust** — supply-chain risk at 82.9K scale

## 10. Corpus-first observations

- **First shell-first T1 at enterprise scale** (82.9K)
- **Second shell-first T1** (after gstack v3 shell, 6K)
- **First 11-platform shell-based conversion**
- **Minimal-governance at maximum-solo-scale** — corpus unique
- **First Chinese contribution-guide localization** (not README)
- **Third SECURITY.md** in corpus (graphify + spec-kit precedent)

## 11. Cross-references

- [[(C) README + CONTRIBUTING + zh-CN cluster summary]] — user positioning
- [[(C) 12 Divisions + 144 Agents Taxonomy cluster summary]] — agent details
- [[(C) 11-Platform Install + OpenClaw 5th Wiki Validation]] (entity)
- Cross-wiki: `../../gstack - Beginner Analysis/` (shell-primary peer)

## 12. Open questions

- Q1: Why no tagged releases at 82.9K stars?
- Q16: Bus factor mitigation plan?
- Q19: Why only zh-CN CONTRIBUTING? (No zh-CN README?)
- Q30: msitarzewski prior public writings?

## 13. Decision log

- **Initial:** Reddit thread → viral launch (50+ requests 12h)
- **Months of iteration:** 144 agents + 12 divisions emerged
- **Current state:** 82.9K stars, solo, main-branch only, no releases
- **Future (inferred):** May formalize as LLC (BMAD path) or accept acquisition; or maintain light-governance with community fork ecosystem
