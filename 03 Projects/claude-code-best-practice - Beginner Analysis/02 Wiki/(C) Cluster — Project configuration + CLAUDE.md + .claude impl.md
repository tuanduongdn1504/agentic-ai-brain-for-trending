# Cluster Summary — Project configuration + CLAUDE.md + .claude/ implementation

**Source:** `CLAUDE.md` + `.mcp.json` + `.claude/` folder tree (repo inspection + WebFetch)
**Retrieved:** 2026-04-23
**Cluster scope:** Maintainer-facing configuration, reference implementation conventions, MCP stack, folder architecture, settings hierarchy, hooks, rules conventions.

---

## 1. CLAUDE.md — maintainer's own project-level context

shanraisshan's CLAUDE.md positions the repo as:
> *"A reference implementation for Claude Code best practices, not a production application."*

This is an important framing. Contrast with:
- **Everything Claude Code v1** — also reference implementation but larger (48 agents + 143 commands + 230 skills per Development Workflows table)
- **spec-kit v17** — actual tool you install (`uv tool install specify-cli`)
- **claude-howto v32** — tutorial repo with EPUB build

claude-code-best-practice occupies "reference implementation + curated knowledge" slot.

### Core architecture documented in CLAUDE.md

**Command → Agent → Skill pattern**, exemplified through Weather Orchestrator:
- Commands (`.claude/commands/`) = entry points
- Agents (`.claude/agents/`) = orchestrators invoking skills
- Skills (`.claude/skills/`) = specialized task performers

**Key patterns:**
- **Subagent orchestration:** Use `Agent(subagent_type="...", prompt="...")` tool, not bash — subagents cannot call each other via terminal
- **Configuration hierarchy cascade:** managed policies → command-line args → `.claude/settings.local.json` → `.claude/settings.json` → global defaults (local configs git-ignored)
- **Hooks system:** Cross-platform sound notifications via `.claude/hooks/` on lifecycle events (PreToolUse, PostToolUse, SessionStart, etc.)

### Key guidelines verbatim

- Keep CLAUDE.md under 200 lines per file for reliable adherence
- Create separate git commits per file (no bundling changes) — **unusual discipline; corpus-observable at this specificity**
- Use `/compact` at ~50% context usage
- When answering best-practice questions, search this repo first before external sources
- Disable hooks via `"disableAllHooks": true` in local settings if needed

**Progressive disclosure emphasis:** refers to `.claude/rules/markdown-docs.md` for documentation standards.

## 2. .mcp.json — MCP server configuration

Verbatim content:
```json
{
  "mcpServers": {
    "playwright": { "command": "npx", "args": ["-y", "@playwright/mcp"] },
    "context7":   { "command": "npx", "args": ["-y", "@upstash/context7-mcp"] },
    "deepwiki":   { "command": "npx", "args": ["-y", "deepwiki-mcp"] }
  }
}
```

### 3 MCP servers — corpus observations

1. **Playwright** — browser automation. Pattern #18 consumer. 4th corpus framework shipping Playwright MCP (after Skyvern v24, crawl4ai v29, OpenHands v30).
2. **Context7** (`@upstash/context7-mcp`) — Upstash-hosted documentation retrieval. Corpus-first Context7 mention (though MCP itself is established Pattern #18).
3. **Deepwiki** (`deepwiki-mcp`) — deepwiki-style knowledge retrieval. Corpus-first Deepwiki mention.

**Corpus pattern strengthening:** Pattern #18 Agent Runtime Standardization — claude-code-best-practice is MCP consumer at Layer 1 (MCP protocol universal). 3-server composition pattern + npx-based transient servers (not persistent-process pattern). 

**Absence note:** No OpenClaw integration (contrast codymaster / paperclip / multica / graphify / agency-agents / OMC which adopt OpenClaw). This is an **official-Anthropic-aligned T1** not a community-platform-T1. Pattern #18 refinement preserved: Western-community-platforms adopt OpenClaw; Anthropic-aligned official/personal frameworks often don't.

## 3. .claude/ folder structure (reference implementation)

Subdirectories:
- `agents/` — feature-specific autonomous actors
- `commands/` — orchestration templates
- `skills/` — configurable knowledge modules
- `hooks/` — event-driven handlers
- `rules/` — rule definitions (auto-loaded via paths: YAML per tip tracker)
- `agent-memory/weather-agent/` — memory storage for Weather Orchestrator reference

Files:
- `settings.json` — configuration
- `.gitignore` — excludes `settings.local.json` + `hooks-config.local.json` + agent memory

**Corpus observation:** `agent-memory/<agent-name>/` subfolder pattern is novel. Prior corpus frameworks reference agent memory abstractly; this is a **concrete filesystem convention** for per-agent memory isolation.

## 4. Weather Orchestrator — flagship reference implementation

Flow:
```
User runs: claude
User invokes: /weather-orchestrator
Command file (.claude/commands/weather-orchestrator.md) loads
→ Triggers weather-agent (.claude/agents/weather-agent.md)
→ Agent invokes weather skills (.claude/skills/weather/*)
→ Agent persists memory to .claude/agent-memory/weather-agent/
```

**Pedagogical purpose:** demonstrate Command → Agent → Skill + per-agent memory in a single, runnable, educational example. Easy to clone, copy, customize.

**Corpus analog:** spec-kit v17 demonstrates Constitution → Specify → Plan → Tasks → Implement via structured workflow. claude-code-best-practice demonstrates via minimal runnable example (weather is toy domain).

## 5. Configuration cascade (5-layer hierarchy)

Documented in CLAUDE.md:
1. Managed policies (enterprise deployment)
2. Command-line arguments
3. `.claude/settings.local.json` (git-ignored, per-user)
4. `.claude/settings.json` (committed, team-shared)
5. Global defaults

**Corpus observation:** 5-layer cascade is corpus-most-detailed. claude-howto v32 documented 3-scope CLAUDE.md variants (project/directory/personal); claude-code-best-practice documents 5-layer settings (managed/CLI/local/shared/global).

Together, these v32 + v34 observations form a **multi-scope configuration lineage** — possible candidate #74 but per v2.1 consolidation-forward discipline, this strengthens existing patterns rather than registering new (insufficient structural N=2 clarity).

## 6. Hook conventions

- Cross-platform sound notifications (lifecycle events)
- Configurable per-user in `hooks-config.local.json`
- Disable all via `"disableAllHooks": true` in local settings
- PreToolUse / PostToolUse / SessionStart / Stop (standard Claude Code events)

**82-tips reinforcement:** 5 tips in "Hooks" category emphasize:
- On-demand hooks (`/careful`, `/freeze`) in skills for safety
- Measure skill usage with PreToolUse
- Auto-format with PostToolUse
- Route permission requests to Opus for safety scanning
- Use Stop hooks to verify work completion

**Corpus observation:** hooks-as-safety-layer (separate from hooks-as-sound-notifications) is a distinct use-case framing.

## 7. Rules conventions (`.claude/rules/`)

Per 82-tips CLAUDE.md + Rules category:
- Auto-load via `paths:` YAML (lazy-loading by file path glob)
- Wrap domain-specific rules in `<important if="...">` tags
- `.claude/rules/markdown-docs.md` referenced as documentation standard example
- Multiple CLAUDE.md for monorepos (ancestor/descendant loading)

**Pattern #22 AGENTS.md Industry Standard status:** claude-code-best-practice does NOT adopt AGENTS.md. Uses CLAUDE.md + rules subfolder instead. **T1 solo archetype continued AGENTS.md abstention** (confirms pattern refinement from v17 spec-kit that corporate T1 adopts, solo T1 often skips).

## 8. GitHub `.github/` folder + automation

- Per tree: `.github/` folder present (contents not fully enumerated via WebFetch)
- Maintainer describes *"Automated workflows running 6 parallel update tasks tracking feature changes"* — implies GitHub Actions stack
- Latest version badge: v2.1.116 (April 21, 2026) — frequent versioning (sync-with-Claude-Code-releases pattern parallels claude-howto v32 v2.1.112 sync)

**Corpus pattern strengthening:** Claude-Code-release sync badge at T1 emerging as sub-pattern (2 data points: claude-howto v32 + claude-code-best-practice v34). Not registered as standalone (consolidation-forward + N=2 single-tier).

## 9. .codex/ folder (sibling config)

Per tree listing, `.codex/` folder exists alongside `.claude/`. Suggests **dual-runtime configuration** — parallel configs for Claude Code + OpenAI Codex CLI.

**Corpus observation:** OMC v27 has 4-runtime orchestration (Claude + Codex + Gemini + Cursor). claude-code-best-practice has 2-runtime configuration scope (Claude + Codex, evidenced by sibling `codex-cli-best-practice` repo). Partial data point for Pattern #56 Multi-Runtime Orchestration (N=1 still; shanraisshan dual-runtime is lighter than OMC 4-runtime).

Not registered as #56 un-stale because (a) depth is lighter (configuration-parallel vs orchestration-meta-framework), (b) per consolidation-forward, wait for 3rd clean multi-runtime observation before promoting.

## 10. Other top-level folders observed

From tree:
- `agent-teams/` — team-configuration examples (parallel to HOT FEATURES "Agent Teams" documentation)
- `best-practice/` — official patterns
- `changelog/` — version history (v2.1.116 tracking)
- `development-workflows/` — comparison implementations (mirrors README table?)
- `implementation/` — concrete examples
- `orchestration-workflow/` — weather-orchestrator + flagship patterns
- `presentation/` — HTML slides (explains primary-lang HTML)
- `reports/` — 9+ technical analyses
- `tips/` — 82-tip source files
- `tutorial/` — tutorial pathway
- `videos/` — video library source
- `!/` — documentation assets + badges (leading-exclamation sort-first convention)

**Corpus novelty:** `!/` folder naming convention (sort-first via exclamation) is corpus-first. Mirrors Storm Bear vault's numbered-folder convention (`00 Notes/`, `01 Journals/`, etc.) for sort control, but via exclamation not number.

## 11. Governance files present / absent

| File | Present | Notes |
|------|---------|-------|
| README.md | ✅ | Primary entry |
| CLAUDE.md | ✅ | Maintainer-framing |
| LICENSE (MIT) | ✅ | |
| .gitignore | ✅ | |
| .mcp.json | ✅ | 3 MCP servers |
| CONTRIBUTING.md | ❌ | |
| SECURITY.md | ❌ | |
| CODE_OF_CONDUCT.md | ❌ | |
| AGENTS.md | ❌ | Pattern #22 T1-solo abstention |
| package.json | ❌ | |
| Gemfile | ❌ | (HTML primary but no Jekyll config surfaced via probe) |

**Governance depth:** 5 files at root. Medium-light. Consistent with solo-T1 profile (Pattern #12).

## 12. Commit discipline

- 498 commits by shanraisshan in ~6 months
- 501+ total commits on main branch (per tree WebFetch)
- Rate: ~2.8 commits/day sustained
- **Convention:** "Create separate git commits per file (no bundling changes)" — maintainer's own CLAUDE.md rule

**Corpus observation:** File-per-commit discipline is corpus-first T1 convention. Most T1 wikis don't surface commit discipline explicitly. Unique to claude-code-best-practice.

## 13. Implications for Phase 3 + 4b

- Entity 1 (Core Product) will document Command→Agent→Skill pattern with .claude/ reference implementation structure
- Entity 2 (Ecosystem) will document MCP stack + Anthropic-aligned positioning + Development Workflows comparison role
- Entity 3 (Shayan Rais) will document ecosystem-portfolio (3 pinned repos) + multi-runtime config (.claude + .codex) + multi-channel content
- Entity 4 (Storm Bear meta) will document #73 Regional-Archetype-Registry consolidation proposal

---

*(C) Claude-generated 2026-04-23 per routine v2.1 Phase 2.*
