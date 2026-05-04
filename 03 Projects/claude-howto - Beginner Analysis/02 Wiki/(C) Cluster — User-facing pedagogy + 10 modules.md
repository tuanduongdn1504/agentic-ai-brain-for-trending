# (C) Cluster — User-facing pedagogy + 10 modules

> **Cluster 1** of 3 — User-facing content: README (EN 878 lines + VN 73 lines + CN + Ukrainian) + LEARNING-ROADMAP.md (753 lines) + CATALOG.md (539 lines).
> **Source:** `luongnv89/claude-howto` main branch, fetched 2026-04-22.

## 1. Positioning verbatim

> *"A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value."*

Title: **"Master Claude Code in a Weekend"** — weekend-length commitment framing (novel in corpus vs codymaster's indefinite "Code Đi" or spec-kit's "Spec-Driven Development" methodology framing).

Hook: *"Go from typing `claude` to orchestrating agents, hooks, skills, and MCP servers — with visual tutorials, copy-paste templates, and a guided learning path."*

Anti-thesis (verbatim, 2 bullets):
1. *"The official docs describe features — but don't show you how to combine them. You know slash commands exist, but not how to chain them with hooks, memory, and subagents into a workflow that actually saves hours."*
2. *"There's no clear learning path. Should you learn MCP before hooks? Skills before subagents? You end up skimming everything and mastering nothing."*

Closing pitch: *"You're leaving 90% of Claude Code's power on the table — and you don't know what you don't know."*

## 2. 10 modules + learning order

| Order (roadmap) | Module folder | Level | Time | Folder # |
|-----------------|---------------|-------|------|----------|
| 1 | Slash Commands | Beginner | 30 min | `01-slash-commands/` |
| 2 | Memory | Beginner+ | 45 min | `02-memory/` |
| 3 | Checkpoints | Intermediate | 45 min | `08-checkpoints/` |
| 4 | CLI Basics | Beginner+ | 30 min | `10-cli/` |
| 5 | Skills | Intermediate | 1 hour | `03-skills/` |
| 6 | Hooks | Intermediate | 1 hour | `06-hooks/` |
| 7 | MCP | Intermediate+ | 1 hour | `05-mcp/` |
| 8 | Subagents | Intermediate+ | 1.5 hours | `04-subagents/` |
| 9 | Advanced Features | Advanced | 2-3 hours | `09-advanced-features/` |
| 10 | Plugins | Advanced | 2 hours | `07-plugins/` |

**Novel observation:** Folder numbering (alphabetical subject) ≠ learning order (pedagogical difficulty). Unusual — most corpus frameworks align folder numbering with learning sequence. Luong treats folder # as stable reference identity, roadmap as pedagogical sequence. Legitimate design choice but novel.

**Total path time:** 11-13 hours (11-hour lower bound per table arithmetic; 13h accounting for context-switching). Weekend-length, verified.

## 3. Catalog summary (total counts)

Per `CATALOG.md`:

| Feature | Built-in | Examples | Total |
|---------|----------|----------|-------|
| Slash Commands | 60+ | 8 | 68+ |
| Subagents | 6 | 11 | 17 |
| Skills | 5 bundled | 4 | 9 |
| Plugins | - | 3 | 3 |
| MCP Servers | 1 | 8 | 9 |
| Hooks | 25 events | 8 | 8 |
| Memory | 7 types | 3 | 3 |
| **TOTAL** | **99** | **45** | **119** |

45 custom examples bundled — smaller than codymaster v12 (79 skills) but larger than ECC v1's feature set. Module/example ratio (45 examples across 10 modules = 4.5 avg) consistent across modules.

## 4. 10-module feature inventory

**01 Slash Commands** — custom `.md` files copied to `.claude/commands/`. Examples: `optimize.md` (code optimization analysis), `pr.md` (pull request preparation), `generate-api-docs.md` (API doc generator).

**02 Memory** — 3-scope CLAUDE.md variant system:
- `project-CLAUDE.md` — team-wide project standards (copy to `./CLAUDE.md`)
- `directory-api-CLAUDE.md` — directory-specific rules (copy to `./src/api/CLAUDE.md`)
- `personal-CLAUDE.md` — personal preferences (copy to `~/.claude/CLAUDE.md`)

**Corpus-first observation:** Explicit 3-scope CLAUDE.md documentation as NAMED variant files. Storm Bear vault itself uses single CLAUDE.md; claude-howto documents 3-scope pattern explicitly.

**03 Skills** — auto-invoked `SKILL.md` folders with scripts. 3 bundled + references author's own `luongnv89/skills` sibling repo (58 stars). Examples: `code-review/` (with scripts + templates), `brand-voice/`, `doc-generator/` (with `generate-docs.py` Python utility).

**04 Subagents** — 5 specialized agents as `.md` files in `.claude/agents/`:
- `code-reviewer.md` — code quality analysis
- `test-engineer.md` — test strategy + coverage
- `documentation-writer.md` — technical docs
- `secure-reviewer.md` — security review (read-only)
- `implementation-agent.md` — full feature implementation

All ROLE-based (not personality-driven — contrast agency-agents v18 "Whimsy Injector" + "Reality Checker"). Pattern #25 Personality-Driven Agent Design NOT strengthened.

**05 MCP Protocol** — 4 example configs:
- `github-mcp.json`
- `database-mcp.json`
- `filesystem-mcp.json`
- `multi-mcp.json` (multi-server composition pattern)

Install via `claude mcp add <name> -- npx -y @modelcontextprotocol/server-<name>` or direct `.mcp.json`.

**06 Hooks** — 6 shell scripts + 25 documented event types:
- Scripts: `format-code.sh`, `pre-commit.sh`, `security-scan.sh`, `log-bash.sh`, `validate-prompt.sh`, `notify-team.sh`
- Event types (4 categories):
  - **Tool Hooks** (4): `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`
  - **Session Hooks** (6): `SessionStart`, `SessionEnd`, `Stop`, `StopFailure`, `SubagentStart`, `SubagentStop`
  - **Task Hooks** (4): `UserPromptSubmit`, `TaskCompleted`, `TaskCreated`, `TeammateIdle`
  - **Lifecycle Hooks** (11): `ConfigChange`, `CwdChanged`, `FileChanged`, `PreCompact`, `PostCompact`, `WorktreeCreate`, `WorktreeRemove`, `Notification`, `InstructionsLoaded`, `Elicitation`, `ElicitationResult`

**Corpus-first:** 25-event hook taxonomy = most comprehensive hook documentation in Storm Bear corpus (exceeds codymaster v12, gstack v3, paperclip v14 — all had hooks but fewer event types documented).

**07 Plugins** — 3 bundled plugins (install via `/plugin install <name>`):
- `pr-review/` — PR review workflow
- `devops-automation/` — deployment + monitoring
- `documentation/` — documentation generation

**08 Checkpoints and Rewind** — 5-option rewind menu (`/rewind` or `Esc` twice):
1. Restore code + conversation
2. Restore conversation only
3. Restore code only
4. Summarize from here
5. Never mind

**09 Advanced Features** — 7 capabilities:
- Planning Mode (`/plan`)
- Extended Thinking (`Alt+T` / `Option+T` toggle)
- Background Tasks
- Permission Modes: `default / acceptEdits / plan / dontAsk / bypassPermissions` (5 modes)
- Headless Mode (`claude -p` for CI/CD)
- Session Management: `/resume /rename /fork claude -c claude -r`
- Configuration via `~/.claude/settings.json`

**10 CLI Reference** — complete command-line doc for `claude` binary:
```bash
claude "prompt"              # interactive
claude -p "prompt"           # print mode (non-interactive)
cat log | claude -p "..."    # pipe input
claude -p --output-format json "..."  # JSON output
claude -r "session" "..."    # resume
```

## 5. Interactive self-assessment mechanism (corpus-first)

Two slash commands ship WITH the guide (embedded in the repo as `.md` files in `.claude/commands/`):
- `/self-assessment` — guided interactive quiz scoring proficiency across all 10 feature areas, generates personalized learning path
- `/lesson-quiz [topic]` — per-module quiz pinpointing knowledge gaps

**Pattern observation:** This is **"educational-assessment-quiz"** — a NEW variant of Pattern #8 Research-Benchmark Integration. Pattern #8 prior variants:
1. Research-benchmark (autoresearch val_bpb, fish-speech 0.54% WER, Skyvern WebBench 64.4%)
2. Productivity claim (spec-kit 48× speedup, graphify 71.5× token reduction)
3. Course-leaderboard (HF agents-course Unit 4)
4. **NEW: Educational-assessment-quiz (claude-howto `/self-assessment` + `/lesson-quiz`)**

Could register as NEW Pattern #71 Interactive Self-Assessment Mechanism OR refine Pattern #8 formal statement to add educational-assessment-quiz sub-variant. **Recommendation: register #71 as N=1 stale-risk-flagged (novel single observation).**

## 6. Find-Your-Level self-assessment (manual version)

8-question checkbox quiz in LEARNING-ROADMAP.md:
1. I can start Claude Code and have a conversation (`claude`)
2. I have created or edited a CLAUDE.md file
3. I have used at least 3 built-in slash commands (e.g., `/help`, `/compact`, `/model`)
4. I have created a custom slash command or skill (SKILL.md)
5. I have configured an MCP server (e.g., GitHub, database)
6. I have set up hooks in `~/.claude/settings.json`
7. I have created or used custom subagents (`.claude/agents/`)
8. I have used print mode (`claude -p`) for scripting or CI/CD

Scoring → 3 levels:
| Checks | Level | Start at | Time |
|--------|-------|----------|------|
| 0-2 | Beginner | Milestone 1A | ~3h |
| 3-5 | Intermediate | Milestone 2A | ~5h |
| 6-8 | Advanced | Milestone 3A | ~5h |

**Teaching philosophy (verbatim):**
> *"Folders in this repository are numbered in recommended learning order based on three key principles: 1. Dependencies - Foundational concepts come first. 2. Complexity - Easier features before advanced ones. 3. Frequency of Use - Most common features taught early."*

## 7. 6-milestone structured path

Per LEARNING-ROADMAP.md (beyond 10 modules, groups into milestones):

**Level 1 Beginner** (~3h):
- **1A: First Commands & Memory** — Slash Commands + Memory
- **1B: Safe Exploration** — Checkpoints + CLI Basics

**Level 2 Intermediate** (~5h):
- **2A: Automation** — Skills + Hooks
- **2B: Integration** — MCP + Subagents

**Level 3 Advanced** (~5h):
- **3A: Advanced Features** — Planning + Permissions
- **3B: Team & Distribution** — Plugins + CLI Mastery

Each milestone has a Mermaid flow diagram showing progression. Mermaid is PRIMARY visual pedagogy mechanism (claims: *"Mermaid diagrams showing how each feature works internally, so you understand why, not just how"*).

## 8. i18n — 4-language README

URLs per README header:
- `README.md` — English (878 lines, primary)
- `vi/README.md` — **Tiếng Việt** (73 lines — thin summary, not full port; opens with note *"Đây là bản tiếng Việt của tài liệu..."*)
- `zh/README.md` — 中文 (Simplified Chinese; inferred length unknown)
- `uk/README.md` — Українська (Ukrainian; inferred length unknown)

**Novel combo:** EN + VN + CN + Ukrainian. Prior corpus i18n patterns:
- 7-language tier: fish-speech v20, oh-my-claudecode v27, LlamaFactory v22, awesome-mcp-servers v31 (EN+CN-tc+CN-sc+JA+KO+PT-BR+TH)
- CJK-trio: graphify v16 (EN+JA+KO+CN)
- CN+EN: TrendRadar v19, multica v15, ai-agents-for-beginners v6
- VN+EN: BMAD-METHOD v11 (VN translation emerging)
- claude-howto: **EN+VN+CN+Ukrainian**

**Ukrainian observation:** First Ukrainian-language README in Storm Bear corpus. Signals Luong's reach to Eastern European dev community (possibly Montimage cybersecurity network or Medium readership). Could register as PATTERN observation-track if Ukrainian appears again; not sufficient for candidate at N=1.

**VN README gap:** 73 lines vs EN 878 lines = VN README is ~8% length; thin summary. Operator (VN-based) would still read EN-primary. **Contrast:** codymaster v12's README is VN-primary (Tody Le writing for VN audience directly). Luong writes for global audience with VN as courtesy port.

## 9. Claude Code version sync

README badges + footer:
- **Version:** v2.1.112
- **Claude Code Compatibility:** 2.1+
- **Last Updated:** April 16, 2026
- **Compatible Models:** Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
- **Sources cited:**
  - https://docs.anthropic.com/en/docs/claude-code
  - https://www.anthropic.com/news/claude-opus-4-7
  - https://support.claude.com/en/articles/12138966-release-notes

**Pattern observation:** Explicit versioning matched to Claude Code version = corpus-first at T1 (spec-kit v17 had v0.7.3 matched to its own release cycle; claude-howto matches UPSTREAM Claude Code binary). Demonstrates maintenance discipline.

## 10. 7 workflow example use cases

Per README "What Can You Build With This?":
| Use Case | Combination |
|----------|-------------|
| Automated Code Review | Slash Commands + Subagents + Memory + MCP |
| Team Onboarding | Memory + Slash Commands + Plugins |
| CI/CD Automation | CLI + Hooks + Background Tasks |
| Documentation Generation | Skills + Subagents + Plugins |
| Security Audits | Subagents + Skills + Hooks (read-only) |
| DevOps Pipelines | Plugins + MCP + Hooks + Background Tasks |
| Complex Refactoring | Checkpoints + Planning Mode + Hooks |

Each use case = 3-4 feature combinations. **Teaching emphasis:** the feature-list is a means; the combinations are the actual power. Aligns with anti-thesis: *"official docs describe features but don't show how to combine them."*

## 11. Offline ebook — EPUB generation

Novel tooling:
```bash
uv run scripts/build_epub.py
```

Creates `claude-howto-guide.epub` with all content including rendered Mermaid diagrams. Corpus-first offline ebook format — none of 31 prior wikis shipped EPUB output.

`uv` = Astral's Python package manager (also seen at spec-kit v17 `uv tool install specify-cli`). 2nd corpus `uv` adoption.

## 12. FAQ signals

Selected FAQ entries:
- **Free?** *"Yes. MIT licensed, free forever. Use it in personal projects, at work, in your team — no restrictions beyond including the license notice."*
- **Maintained?** *"Actively. The guide is synced with every Claude Code release. Current version: v2.1.112 (April 2026), compatible with Claude Code 2.1+."*
- **Difference from official docs?** *"The official docs are a feature reference. This guide is a tutorial with diagrams, production-ready templates, and a progressive learning path. They complement each other."*
- **How long?** *"11-13 hours for the full path. But you'll get immediate value in 15 minutes — just copy a slash command template and try it."*
- **Models?** *"Yes. All templates work with Claude Sonnet 4.6, Claude Opus 4.7, and Claude Haiku 4.5."*
- **Contribute?** *"Absolutely. See CONTRIBUTING.md for guidelines."*
- **Offline read?** *"Yes. Run uv run scripts/build_epub.py to generate an EPUB ebook with all content and rendered diagrams."*

## 13. Corpus-first observations from Cluster 1

1. **"Master Claude Code in a Weekend"** — weekend-length commitment framing (novel time-framing pedagogy)
2. **Interactive self-assessment as slash commands** (`/self-assessment`, `/lesson-quiz [topic]`) — first corpus framework embedding quiz mechanism inside the product
3. **3-scope CLAUDE.md variant pattern** (project / directory / personal) explicitly documented as separate template files
4. **25-event hook taxonomy** — most comprehensive hook event documentation in corpus
5. **EN + VN + CN + Ukrainian 4-language combo** — Ukrainian first appearance in Storm Bear corpus
6. **EPUB offline ebook** — first corpus framework shipping ebook output
7. **Claude Code upstream version badge sync** (v2.1.112 = Claude Code release, not claude-howto's own numbering)
8. **Folder # ≠ learning order** — alphabetical folders + pedagogical-sequence roadmap as separate concepts
9. **10 → 6-milestone pedagogical grouping** (4 beginner + 4 intermediate + 4 advanced milestones)
10. **Testing infrastructure for tutorial repo** — pytest + Ruff + Bandit + mypy + Codecov (signals Luong treats content as code)
11. **Mermaid-diagram-primary** visual pedagogy (visual-first explanation as core teaching modality)
12. **Weekend-commitment** time-framing vs codymaster "Code Đi" open-ended vs BMAD methodology-paced vs spec-kit ambitious-48× productivity
