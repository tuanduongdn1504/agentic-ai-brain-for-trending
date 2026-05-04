# Entity — Core Product: Command-Agent-Skill reference + 82 tips + HOT FEATURES tracker

> **Entity type:** Core product / framework architecture
> **Tier:** T1 Agent-as-assistant (11th T1 entrant in Storm Bear corpus)
> **Wiki source:** `shanraisshan/claude-code-best-practice`
> **Status:** v1 (2026-04-23)

---

## 1. One-line summary

claude-code-best-practice is a **reference implementation + curated knowledge aggregator** for Claude Code, organized as Command → Agent → Skill reference architecture + 82 tips across 14 categories + live-delta HOT FEATURES tracker for beta Claude Code capabilities.

## 2. Philosophy (verbatim)

- **Tagline:** *"from vibe coding to agentic engineering - practice makes claude perfect"*
- **Core workflow:** Research → Plan → Execute → Review → Ship
- **Context:** *"Context rot kicks in around ~300-400k tokens"* / *"Dumb zone kicks in around ~40% context"*
- **Autonomy:** *"Don't babysit"* (🚫👶) — let Claude work independently on well-scoped tasks
- **Planning:** *"Prototype > PRD"* — 20-30 iterations preferred over specification

### Position on Pattern #51 Vibe-Coding Spectrum

claude-code-best-practice occupies a **progression framing**: names the axis FROM vibe-coding TO agentic-engineering. Distinct from poles:
- **vibe-pro pole:** awesome-design-md v25 (embrace)
- **vibe-anti pole:** spec-kit v17 (predictable-outcomes-over-vibe)
- **claude-code-best-practice v34:** axis-aware progression framing (not pole-committed)

## 3. Reference implementation architecture

### Command → Agent → Skill pattern

```
User → slash command (.claude/commands/)
     → invokes agent (.claude/agents/)
     → agent orchestrates skills (.claude/skills/)
     → writes memory (.claude/agent-memory/<agent-name>/)
```

### Weather Orchestrator — flagship reference

Runnable demo via:
```bash
claude
/weather-orchestrator
```

Demonstrates:
- Single-command entry
- Agent orchestration of multiple skills
- Per-agent memory persistence
- Hooks activation on lifecycle events

Purpose: **pedagogy** — deliberately toy domain (weather) so users focus on the pattern, not the domain.

### Configuration hierarchy (5-layer cascade)

1. Managed policies (enterprise)
2. CLI arguments
3. `.claude/settings.local.json` (per-user, git-ignored)
4. `.claude/settings.json` (team-shared, committed)
5. Global defaults

**Corpus-most-detailed cascade documented** (claude-howto v32 was 3-scope CLAUDE.md; claude-code-best-practice v34 is 5-layer settings).

## 4. 82 Tips across 14 categories

Structure:
- **Foundations:** Prompting (3) + Planning/Specs (6)
- **Context + session:** Context Management (5) + Session Management (6)
- **Configuration + rules:** CLAUDE.md + Rules (8) + Agents (4) + Commands (3) + Skills (9) + Hooks (5)
- **Workflows:** Workflows (5) + Advanced Workflows (9)
- **Operations:** Git/PR (5) + Debugging (6) + Utilities (5) + Daily (2)

### High-signal tips (for Storm Bear operator)

1. **CLAUDE.md under 200 lines / 60 ideal** — Storm Bear vault root CLAUDE.md is 150K+ lines; directly actionable refactor target
2. **Auto-load `.claude/rules/*.md` via paths: YAML** — lazy-loading via glob
3. **Wrap domain rules in `<important if="...">`** — conditional rule activation
4. **Multiple CLAUDE.md for monorepos** — ancestor/descendant loading (reinforces v32 3-scope pattern)
5. **`/compact` at ~50% context** — manual over autocompact
6. **`/rewind` (Esc Esc) over corrections** — cleaner history
7. **`context: fork` in skills** — isolated subagent execution
8. **Skill descriptions as triggers, not summaries** — differentiates selection
9. **Ralph Wiggum plugin** for autonomous long-running tasks
10. **`/sandbox` for 84% reduction** in permission prompts
11. **Auto Mode** — safety-classifier-gated autonomy (vs `dangerously-skip-permissions`)
12. **Keep PRs small (p50: 118 lines)** — squash merge for linear history

## 5. HOT FEATURES live-delta tracker (11 beta capabilities)

Unique corpus-positioned format:

| Feature | Use case |
|---------|----------|
| Routines | Cloud automation (scheduled / API-triggered) |
| Ultrareview | Multi-agent code review with independent verification |
| Devcontainers | Preconfigured dev isolation |
| Channels | Event routing (Telegram / Discord / webhooks) |
| Auto Mode | Background safety classifier replacing manual permission prompts |
| Agent Teams | Multiple agents parallel on shared codebase |
| Scheduled Tasks | `/loop` (local ≤7d) + `/schedule` (cloud) |
| Voice Dictation | Push-to-talk, 20-language support |
| Code Review | Multi-agent PR analysis (bugs + security) |
| Remote Control | Continue sessions from any device |
| Computer Use | Claude controls screen (macOS) |

**Corpus-first observation:** No other T1 wiki tracks beta Claude Code features as headline section. ECC v1 / Superpowers v2 / claude-howto v32 are feature-stable catalogs; claude-code-best-practice is live-delta tracker.

**Maintenance infrastructure:** *"Automated workflows running 6 parallel update tasks tracking feature changes"* — maintainer's own self-description implies scripted Claude Code release monitoring.

## 6. MCP stack — .mcp.json verbatim

```json
{
  "mcpServers": {
    "playwright": { "command": "npx", "args": ["-y", "@playwright/mcp"] },
    "context7":   { "command": "npx", "args": ["-y", "@upstash/context7-mcp"] },
    "deepwiki":   { "command": "npx", "args": ["-y", "deepwiki-mcp"] }
  }
}
```

### Corpus-first notes

- **Context7 (Upstash)** — 1st corpus mention
- **Deepwiki MCP** — 1st corpus mention
- **3-server composition + npx-transient invocation** — Pattern #18 MCP consumer Layer 1

## 7. What's NOT in the repo (Pattern #22 solo T1 continuation)

- No AGENTS.md (corporate T1 adopts; solo T1 often skips per Pattern #22 refinement)
- No CONTRIBUTING.md
- No SECURITY.md (contrast claude-howto v32's 334-line SECURITY.md)
- No CODE_OF_CONDUCT.md
- No package.json (HTML primary language; no Jekyll config surfaced)

**Pattern #12 Governance-Depth:** Light (5 root files). Consistent solo-T1 profile.

## 8. Development Workflows comparison table (10+ frameworks)

Living comparison maintained in README:

| Framework | Stars (per v34) | Primary pattern |
|-----------|-----------------|-----------------|
| Everything Claude Code | 160K | 48 agents + 143 commands + 230 skills |
| Superpowers | 159K | TDD-first + Iron Laws |
| Spec Kit | 89K | Spec-driven + 9-article constitution |
| gstack | 76K | Role personas + /codex review |
| Get Shit Done | 55K | Fresh contexts + wave execution |
| + BMAD-METHOD, OpenSpec, oh-my-claudecode, Compound Engineering, HumanLayer | | |

**Storm Bear corpus overlap:** 5 of 5 explicitly ranked = 100% match with Storm Bear T1 wikis (ECC v1 + Superpowers v2 + spec-kit v17 + gstack v3 + GSD v5). Independent external validation of Storm Bear T1 selection completeness.

## 9. "Billion-Dollar Questions" framing

13 unanswered research questions framed as commercial-value-pending:
- Memory + instruction optimization
- Agent vs skill vs command selection criteria
- Specification versioning + maintenance
- Persona effectiveness for specialized agents
- Community vs personal skill integration
- Full codebase → spec → regeneration feasibility
- (+ 7 more)

**Corpus observation:** Naming research questions as "billion-dollar" = unique framing. Prior corpus wikis have open-questions files (project-local) but not repo-level commercial-value framing.

## 10. Startups/Businesses Displaced table

Corpus-first **commercial-ecosystem-impact-tracking** at T1:

| Claude Feature | Replaced Products |
|---|---|
| Code Review | Greptile, CodeRabbit, Devin Review, OpenDiff |
| Voice Dictation | Wispr Flow, SuperWhisper |
| Remote Control | OpenClaw |
| Computer Use | OpenAI CUA |
| Chrome Integration | Playwright MCP, Chrome DevTools MCP |

**Note:** OpenClaw listed as displaced-by-Claude-Code-Remote-Control. Pattern #18 Western-community-platform observation stays valid — many community frameworks still use OpenClaw; shanraisshan's framing is forward-looking (Claude Code adds Remote Control → OpenClaw's niche narrows).

## 11. Installation + usage flow

```bash
git clone https://github.com/shanraisshan/claude-code-best-practice
cd claude-code-best-practice

# The repo IS the reference — read like a course
open README.md

# Try the flagship reference
claude
/weather-orchestrator
```

**No package manager install path** — HTML + markdown content delivered via git clone. Reading order recommended: README → concepts → weather-orchestrator → 82 tips → reports.

## 12. Cross-references

### Direct sibling wikis (strong cross-references)

- `../claude-howto - Beginner Analysis/` (v32) — T1 pedagogical peer + Boris Cherny citation + regional-archetype (VN-diaspora)
- `../oh-my-claudecode - Beginner Analysis/` (v27) — Korean T1 + individual-multi-publisher variant
- `../Everything Claude Code - Beginner Analysis/` (v1) — listed in v34's Development Workflows table (160K stars claimed)
- `../Superpowers - Beginner Analysis/` (v2) — listed in v34's Development Workflows table (159K stars claimed)
- `../spec-kit - Beginner Analysis/` (v17) — listed in v34's Development Workflows table (89K)
- `../gstack - Beginner Analysis/` (v3) — listed in v34's Development Workflows table (76K)
- `../get-shit-done - Beginner Analysis/` (v5) — listed in v34's Development Workflows table (55K)
- `../BMAD-METHOD - Beginner Analysis/` (v11) — listed in v34's Development Workflows table
- `../agency-agents - Beginner Analysis/` (v18) — community-viral T1 peer
- `../codymaster - Beginner Analysis/` (v12) — VN regional T1 peer

### Pattern Library references

- Pattern #17 Ecosystem-Layer Organizations — **11th data point** (strengthening only)
- Pattern #18 Agent Runtime Standardization — MCP consumer (3 servers)
- Pattern #19 Intellectual Lineage — Boris Cherny 4th citation + Dex Horthy + Cat Wu first citations
- Pattern #20 Solo-Scale Ceiling — NEW ROW Pakistani-solo-multi-channel 47K/6mo
- Pattern #22 AGENTS.md — T1 solo abstention continues
- Pattern #27 Community-Viral Scale Path — **11th data point** (Pakistani-multi-channel-pedagogical sub-path ~260 stars/day)
- Pattern #51 Vibe-Coding Spectrum — progression-framing observation (axis-aware not pole-committed)
- **#73 Regional-Archetype-Registry T1 Meta-Pattern — NEW candidate** (sub-variant 73c Pakistani)

## 13. Open questions

See `01 Analysis/(C) open questions.md` — 30 open questions including:
- Exact file counts in `.claude/agents/commands/skills/hooks/rules/`
- Whether HTML primary language indicates Jekyll/GitHub Pages build
- How "automated 6 parallel update workflows" maintenance operates
- Storm Bear operator adoption pathway (fork vs upstream contribution)

---

*(C) Claude-generated 2026-04-23 per routine v2.1 Phase 3.*
