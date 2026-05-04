# oh-my-claudecode - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`Yeachan-Heo/oh-my-claudecode`](https://github.com/Yeachan-Heo/oh-my-claudecode) — **"Teams-first Multi-agent orchestration for Claude Code. Zero learning curve."**

**30,366 stars (#9 corpus), 2,812 forks (9.3%), MIT, TypeScript, main-branch, created 2026-01-09 (~3.5 months old), pushed 2026-04-21 (today), 40 MB repo, 0 open issues, homepage oh-my-claudecode.dev**. Author: **Yeachan Heo** (solo, Korean) — 1st **Korean-authored T1** in corpus. Top team: JunghwanNA (65 commits) + riftzen-bit (52) + Seunggwan Song + BLUE + Junho Yeo. Ambassador: Sigrid Jin. Doc specialist: devswha. npm: `oh-my-claude-sisyphus@latest` (**branding ≠ package name divergence**). Sibling product: `oh-my-codex` (same orchestration for OpenAI Codex CLI). Discord: discord.gg/PUwSMR9XNk.

**Scope status: T1 Agent-as-assistant — 9TH T1 ENTRANT.** T1 continues as largest tier in corpus.

**Tagline:** *"Your Claude Just Have been Steroided."* / *"Don't learn Claude Code. Just use OMC."*

**Core product — 8 orchestration modes + 19 agents + 15+ skill surface:**
- **Team (canonical, v4.1.7+):** staged pipeline `team-plan → team-prd → team-exec → team-verify → team-fix (loop)`
- **omc team (CLI, v4.4.0+):** tmux workers — real `claude`/`codex`/`gemini`/**`cursor-agent`** (v4.13.1) CLI processes in split panes
- **CCG:** tri-model synthesis (Claude + Codex + Gemini)
- **Autopilot:** single-lead autonomous execution
- **Ultrawork:** maximum parallelism
- **Ralph:** persistent verify/fix loops (includes ultrawork)
- **Pipeline:** sequential staged
- **Ultrapilot (deprecated):** legacy alias

**Additional skills:** Deep Interview (Socratic clarification) / Autoresearch (bounded stateful loop) / Provider Advisor (ask) / Rate Limit Wait (auto-resume) / HUD statusline / Skill Learning (`/learner` auto-extract patterns) / Cost tracking / OpenClaw integration / Notification tags (Telegram/Discord/Slack).

**Explicit intellectual lineage (5 sources acknowledged):** [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) • [claude-hud](https://github.com/ryanjoachim/claude-hud) • **[Superpowers](https://github.com/obra/superpowers)** (Storm Bear v2) • **[everything-claude-code](https://github.com/affaan-m/everything-claude-code)** (Storm Bear v1) • [Ouroboros](https://github.com/Q00/ouroboros).

**⚠️ FIRST wiki in Storm Bear corpus to EXPLICITLY CITE BACK to Storm Bear corpus items** — ECC v1 + Superpowers v2 both appear in OMC's inspiration list. Recursive corpus reference = NEW meta-pattern.

**v2 Routine 12-axis classification:**

| Axis | Value |
|------|-------|
| **Tier** | **T1 Agent-as-assistant (9TH entrant — largest tier extends)** |
| **Archetype** | **Solo-led Korean OSS with 5-source multi-lineage + ecosystem-layer individual (sibling `oh-my-codex`)** |
| **Scale tier** | 30K stars in 3.5 months (~289 stars/day — viral below extreme-velocity 1K/day) |
| **Primary lang** | TypeScript |
| **Packaging** | Claude Code plugin marketplace + npm (`oh-my-claude-sisyphus`) |
| **Origin story** | 5-source inspiration fusion (oh-my-opencode naming + claude-hud HUD + Superpowers skills + ECC commands + Ouroboros loops) |
| **Methodology** | Team-first canonical orchestration + 8 modes + plugin architecture |
| **Governance files** | AGENTS.md (21 KB) + CLAUDE.md (6.6 KB) + CONTRIBUTING.md (12 KB) + SECURITY.md + CHANGELOG.md |
| **Agent/skill count** | 19 agents + 15+ skills + 8 orchestration modes |
| **i18n** | **7 languages (en+ko+zh+ja+es+vi+pt)** — ties fish-speech v20 (7 langs) for broadest i18n in corpus |
| **Intellectual influence** | **5-source multi-lineage including 2 Storm Bear corpus items (ECC v1 + Superpowers v2)** |
| **Agent platforms** | **4 runtimes native:** Claude Code + Codex CLI + Gemini CLI + Cursor-agent (v4.13.1) |

**Tier placement rationale:** T1 Agent-as-assistant — meta-orchestration framework extending Claude Code with multi-agent coordination + multi-runtime support. Direct peer to spec-kit v17 (corporate), agency-agents v18 (community-viral), codymaster v12 (VN solo), BMAD v11 (LLC).

**v27 pattern implications preview:**
- **Pattern #17 Ecosystem-Layer Orgs — 7th data point** — Yeachan publishes `oh-my-claudecode` + `oh-my-codex` (5th archetype variant: individual-multi-runtime-publisher; distinct from nextlevelbuilder individual-led-dev)
- **Pattern #18 Agent Runtime Standardization — 6th data point** — OpenClaw integration confirmed (Western-community N=6)
- **Pattern #19 Intellectual Lineage — 5-source multi-lineage** — first corpus example combining individual-author + methodology + community-viral archetypes in one framework
- **Pattern #20 Solo-Scale Ceiling — revision candidate** — 30K Korean solo in 3.5 months (velocity factor)
- **Pattern #22 AGENTS.md Industry Standard — strengthens** — 21 KB (among largest in corpus)
- **Pattern #52 Extreme-Viral-Velocity — below threshold** (289 stars/day < 1K/day) but noteworthy velocity class
- **NEW candidates at v27:**
  - **#55 Korean Regional Archetype T1** — first Korean-authored T1 framework in corpus (distinct from US/CN/VN/unattributed)
  - **#56 Multi-Runtime Orchestration Meta-Framework** — 4 AI runtimes (Claude Code + Codex + Gemini + Cursor) as first-class tmux workers (distinct from Pattern #28 provider-abstraction)
  - **#57 Recursive Corpus Reference** — framework explicitly cites prior Storm Bear corpus items (meta-structural pattern)
  - **#58 Branding vs Package-Name Divergence** — repo brand `oh-my-claudecode` vs npm `oh-my-claude-sisyphus`
  - **#59 Claude Code Plugin Marketplace Native** — first framework using `/plugin marketplace add` in corpus

## Claude's Role

Claude là wiki maintainer, chạy bằng routine `llm-wiki-routine-v2.md` (**27th auto-execution, 9th v2 routine execution**):

- **Ingest sources via WebFetch + API probe** — README (25 KB) + AGENTS.md (21 KB) + CLAUDE.md (6.6 KB) + CHANGELOG + CONTRIBUTING
- **Cross-reference với 26 sibling wikis** — primarily spec-kit v17 (T1 corporate peer) + agency-agents v18 (T1 solo-viral peer) + codymaster v12 (T1 Asian-solo peer) + Superpowers v2 + ECC v1 (cited sources — recursive reference)
- **Phase 4b = T1 9-way comparison + Pattern #17 7th data point + Pattern #18 6th data point + 5 new candidates**
- **Beginner angle** — Claude Code user wanting zero-config multi-agent orchestration; Storm Bear Scrum-coach applicability HIGH

**Prime directive:** Outcome = wiki + T1 extends to N=9 + 5 new candidates + recursive corpus reference meta-pattern + Korean archetype + multi-runtime orchestration + Pattern #17 + #18 strengthening.

## Process — routine `llm-wiki-routine-v2.md`

7 phases. 9th v2 routine execution. Phase 4b = T1 N=9 extension + pattern analysis.

## Key People

- **Yeachan Heo** (`@Yeachan-Heo`) — creator, solo lead, Korean
- **Sigrid Jin** (`@sigridjineth`) — ambassador
- **devswha** — document specialist
- **JunghwanNA / riftzen-bit / Seunggwan Song / BLUE / Junho Yeo** — top 5 collaborators (Korean team)
- **Cross-project:** 26 sibling wikis. This is 27th = T1 extension + recursive corpus reference first occurrence.

## Folder Structure

```
oh-my-claudecode - Beginner Analysis/
├── CLAUDE.md
├── 00 Sources/           ← WebFetch README + AGENTS + CLAUDE + CHANGELOG
├── 01 Analysis/
├── 02 Wiki/              ← 3 cluster summaries + 4 entity pages + index + log
├── 03 Published/         ← Beginner guide + Phase 4b T1 extension
├── 04 Reviews/           ← Iteration log v27
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ VN + 13-section format
- **Cross-reference 26 siblings MANDATORY** — especially T1 peers (spec-kit / agency-agents / codymaster / BMAD) + cited sources (ECC v1 / Superpowers v2) + Pattern #17 peers + Pattern #18 peers
- **Pattern Library direct update** — 5 new candidates + Pattern #17 7th + #18 6th data points

## Current Status

> **Last updated:** 2026-04-21
> **Status:** 🟡 Routine v2 auto-execute IN PROGRESS — 27th LLM Wiki, 9th v2 execution, T1 N=9 extension, recursive corpus reference meta-pattern debut

### Expected milestones

- [x] Phase 0 Pre-flight (probe + consolidation guard PASS at 0.81:1)
- [x] Phase 1 Scaffold (folder + CLAUDE.md)
- [ ] Phase 2 Source ingestion (3 cluster summaries)
- [ ] Phase 3 Entity pages (4)
- [ ] Phase 4a Beginner published guide
- [ ] Phase 4b **T1 9-way extension + 5 new candidates**
- [ ] Phase 5 Iteration log v27 + PATTERN_LIBRARY.md update
- [ ] Phase 6 Vault file updates (root GOALS.md + CLAUDE.md)
