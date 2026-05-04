# (C) 10-Module Pedagogy + Self-Assessment Quiz

> **Entity type:** Core product entity
> **Wiki:** v32 claude-howto
> **Status:** ✅ entity page v1

## 1. What is it?

The core product of `luongnv89/claude-howto` is a **10-module tutorial curriculum** for Claude Code, organized in numbered folders (`01-slash-commands/` through `10-cli/`) with copy-paste templates, Mermaid diagrams, and an **interactive self-assessment mechanism** shipped AS slash commands (`/self-assessment` + `/lesson-quiz [topic]`).

The entity is distinguished by 3 corpus-first characteristics:
1. **Weekend-length onboarding** ("Master Claude Code in a Weekend")
2. **Embedded interactive quizzes** (pedagogy-as-slash-commands)
3. **Folder-numbering ≠ learning-order** — folders are alphabetical-subject; roadmap is pedagogical-difficulty

## 2. 10 modules

| Folder | Module | Recommended learning order | Time | Level |
|--------|--------|---------------------------|------|-------|
| `01-slash-commands/` | Slash Commands | 1 | 30 min | Beginner |
| `02-memory/` | Memory | 2 | 45 min | Beginner+ |
| `03-skills/` | Skills | 5 | 1 hour | Intermediate |
| `04-subagents/` | Subagents | 8 | 1.5 hours | Intermediate+ |
| `05-mcp/` | MCP Protocol | 7 | 1 hour | Intermediate+ |
| `06-hooks/` | Hooks | 6 | 1 hour | Intermediate |
| `07-plugins/` | Plugins | 10 | 2 hours | Advanced |
| `08-checkpoints/` | Checkpoints | 3 | 45 min | Intermediate |
| `09-advanced-features/` | Advanced Features | 9 | 2-3 hours | Advanced |
| `10-cli/` | CLI Reference | 4 | 30 min | Beginner+ |

**Total time:** 11-13 hours for full path.

## 3. Feature inventory (from CATALOG.md)

| Feature | Built-in (Claude Code) | Examples (claude-howto) | Total |
|---------|------------------------|-------------------------|-------|
| Slash Commands | 60+ | 8 | 68+ |
| Subagents | 6 | 11 | 17 |
| Skills | 5 bundled | 4 | 9 |
| Plugins | — | 3 | 3 |
| MCP Servers | 1 | 8 | 9 |
| Hooks | 25 events | 8 | 8 |
| Memory | 7 types | 3 | 3 |
| **TOTAL** | **99** | **45** | **119** |

claude-howto ships **45 custom templates** spanning all 10 modules.

## 4. Interactive self-assessment (corpus-first at T1)

Two bundled slash commands:
- **`/self-assessment`** — guided interactive quiz scoring proficiency across all 10 feature areas → generates personalized learning path
- **`/lesson-quiz [topic]`** — per-module quiz (e.g., `/lesson-quiz hooks`, `/lesson-quiz mcp`) → identifies knowledge gaps after each module

**Pattern insight:** Quizzes are slash commands shipped WITH the product. User installs claude-howto once, then uses it as both reference (static `.md` files) AND assessment engine (runtime slash commands). This is educational-technology-as-UX pattern — novel at T1.

**Related patterns:**
- Pattern #8 Research-Benchmark Integration (CONFIRMED) — new sub-variant "educational-assessment-quiz" candidate
- Proposed **Pattern #71 Interactive Self-Assessment Mechanism** N=1 stale-risk-flagged

## 5. 3-scope CLAUDE.md variant system

`02-memory/` module ships 3 named templates:
- `project-CLAUDE.md` — team-wide standards → copy to `./CLAUDE.md`
- `directory-api-CLAUDE.md` — directory-specific rules → copy to `./src/api/CLAUDE.md`
- `personal-CLAUDE.md` — personal preferences → copy to `~/.claude/CLAUDE.md`

**Corpus-first:** Explicit 3-scope CLAUDE.md documentation as SEPARATE template files. Storm Bear vault itself uses single CLAUDE.md; claude-howto formalizes 3-scope pattern as named variants.

## 6. 25-event hook taxonomy (most comprehensive in corpus)

Per README §"06 Hooks" and cluster 1:

**Tool Hooks (4):** `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`

**Session Hooks (6):** `SessionStart`, `SessionEnd`, `Stop`, `StopFailure`, `SubagentStart`, `SubagentStop`

**Task Hooks (4):** `UserPromptSubmit`, `TaskCompleted`, `TaskCreated`, `TeammateIdle`

**Lifecycle Hooks (11):** `ConfigChange`, `CwdChanged`, `FileChanged`, `PreCompact`, `PostCompact`, `WorktreeCreate`, `WorktreeRemove`, `Notification`, `InstructionsLoaded`, `Elicitation`, `ElicitationResult`

**6 shell script templates:** `format-code.sh`, `pre-commit.sh`, `security-scan.sh`, `log-bash.sh`, `validate-prompt.sh`, `notify-team.sh`

Prior corpus T1 hook coverage (best-in-class comparison):
- gstack v3 — shell hooks as virtual-team mechanism; ~5 event types documented
- paperclip v14 — 4 governance primitives + hooks; ~6-8 event types
- codymaster v12 — Smart Spine hooks; event types in 5-tier memory spec
- **claude-howto v32** — **25 event types with 4-category taxonomy** — most comprehensive

## 7. 5 subagents (role-based, not personality-driven)

`04-subagents/` ships 5 specialized agents:
1. `code-reviewer.md` — code quality analysis
2. `test-engineer.md` — test strategy + coverage
3. `documentation-writer.md` — technical docs
4. `secure-reviewer.md` — security review (read-only)
5. `implementation-agent.md` — full feature implementation

**Design philosophy:** Role-based agents (software-engineering roles). No personality layer (contrast agency-agents v18 "Whimsy Injector" + "Reality Checker 3-5 issues default"). Role-based is mainstream T1 convention; personality-driven is agency-agents v18 minority pattern.

Pattern #25 Personality-Driven Agent Design remains RETIRED (v27 audit); claude-howto's role-based subagents add no revival evidence.

## 8. 7 workflow combinations

Per README §"What Can You Build":
| Use case | Combination |
|----------|-------------|
| Automated Code Review | Slash Commands + Subagents + Memory + MCP |
| Team Onboarding | Memory + Slash Commands + Plugins |
| CI/CD Automation | CLI + Hooks + Background Tasks |
| Documentation Generation | Skills + Subagents + Plugins |
| Security Audits | Subagents + Skills + Hooks (read-only) |
| DevOps Pipelines | Plugins + MCP + Hooks + Background Tasks |
| Complex Refactoring | Checkpoints + Planning Mode + Hooks |

**Pedagogical emphasis:** Luong teaches combinations over isolated features. Aligns with anti-thesis that *"official docs describe features but don't show how to combine them."*

## 9. Mermaid-diagram-primary visual pedagogy

Mermaid is the PRIMARY visual teaching modality. Every module has flow diagrams showing:
- How each feature works internally
- How features combine in workflows
- Level-to-level progression in LEARNING-ROADMAP.md

**Novel CI discipline:** `mermaid-syntax` is a pre-commit hook enforcing all ` ```mermaid ` blocks parse correctly. Also `build-epub` pre-commit hook tests EPUB generation (which renders Mermaid).

**Pattern observation:** First corpus T1 with DIAGRAM-CI discipline. Documentation rigor as engineering.

## 10. EPUB offline ebook pipeline

```bash
uv run scripts/build_epub.py
```

Produces `claude-howto-guide.epub` with all content + rendered Mermaid diagrams. Pre-commit hook `build-epub` validates on every `.md` change.

**Corpus-first** — no prior wiki framework shipped EPUB output. Enables:
- Offline reading (flights, commutes)
- Kindle/e-reader use
- PDF-alternative distribution

## 11. 4-language i18n (novel combo)

README ports:
- `README.md` — English (878 lines, primary)
- `vi/README.md` — Tiếng Việt (73 lines, thin summary)
- `zh/README.md` — 中文 Simplified Chinese
- `uk/README.md` — Українська Ukrainian

**Novel combo:** EN + VN + CN + Ukrainian. Ukrainian is first corpus appearance. VN-thinness (8% of EN length) suggests courtesy port, not VN-primary audience — contrast codymaster v12 VN-first.

## 12. Cross-wiki references

| Sibling | Relationship | Wiki |
|---------|-------------|------|
| codymaster v12 | Direct VN-authored T1 peer; codymaster VN-in-VN vs claude-howto VN-diaspora | [[codymaster - Beginner Analysis]] |
| ECC v1 | Closest structural peer (feature-framework with templates) | [[Everything Claude Code - Beginner Analysis]] |
| Superpowers v2 | Methodology + skill library peer | [[Superpowers - Beginner Analysis]] |
| gstack v3 | Virtual-team methodology peer | [[gstack - Beginner Analysis]] |
| GSD v5 | SDD methodology peer | [[get-shit-done - Beginner Analysis]] |
| BMAD v11 | Methodology T1 at scale peer | [[BMAD-METHOD - Beginner Analysis]] |
| spec-kit v17 | T1 corporate peer (anti-vibe Spec-Driven Development) | [[spec-kit - Beginner Analysis]] |
| agency-agents v18 | T1 community-viral peer (Reddit-origin 82.9K) | [[agency-agents - Beginner Analysis]] |
| OMC v27 | Pattern #55 Korean Regional Archetype analog | [[oh-my-claudecode - Beginner Analysis]] |
| awesome-mcp-servers v31 | MCP directory — claude-howto's 05-mcp module uses MCP protocol | [[awesome-mcp-servers - Beginner Analysis]] |

## 13. Corpus-first signature summary

| # | Feature | Corpus-first? |
|---|---------|---------------|
| 1 | Interactive self-assessment slash commands (`/self-assessment` + `/lesson-quiz [topic]`) | ✅ YES |
| 2 | 25-event hook taxonomy | ✅ YES at T1 |
| 3 | 3-scope CLAUDE.md variant system (project/directory/personal) as NAMED files | ✅ YES |
| 4 | EPUB offline ebook pipeline | ✅ YES in corpus |
| 5 | 4-language EN+VN+CN+Ukrainian combo | ✅ YES (Ukrainian first) |
| 6 | mermaid-syntax + build-epub pre-commit hooks | ✅ YES |
| 7 | Folder # ≠ learning order (2 sequencing systems) | ✅ YES |
| 8 | "Master Claude Code in a Weekend" time-framing | ✅ YES |
| 9 | Mermaid-primary visual pedagogy with CI validation | ✅ YES at T1 |
| 10 | Claude Code version-sync badge (v2.1.112 = upstream) | ✅ YES at T1 |
