# Cluster Summary — User-facing README + 82 tips structure

**Source:** `https://raw.githubusercontent.com/shanraisshan/claude-code-best-practice/main/README.md`
**Retrieved:** 2026-04-23 (post-v2.1.116 sync April 21, 2026)
**Cluster scope:** Public-facing positioning, CONCEPTS table, HOT FEATURES, 82 tips across 14 categories, Development Workflows comparison, Displaced Products table, Video Library, Subscription Channels, Billion-Dollar Questions, Reports section.

---

## 1. Positioning verbatim

- **Tagline:** *"from vibe coding to agentic engineering - practice makes claude perfect"*
- **Author self-positioning:** 3rd most-starred repo in Pakistan, #1 GitHub Trending multiple times
- **Maintenance model:** *"Automated workflows running 6 parallel update tasks tracking feature changes"* — maintainer describes own workflow as daily cadence with Claude Code update monitoring
- **Getting Started:** *"1. Read repo like a course before using examples. 2. Clone and experiment with /weather-orchestrator. 3. Reference this repo when asking Claude about improvements."*

## 2. CONCEPTS table (core Claude Code features documented)

15+ features across 8 categories:
- **Subagents** — autonomous actors in isolated contexts with custom tools, permissions, persistent identity (`.claude/agents/`)
- **Commands** — user-invoked prompt templates (`.claude/commands/`)
- **Skills** — configurable, preloadable knowledge modules with progressive disclosure (`.claude/skills/`)
- **Workflows** — multi-step orchestrations combining commands, agents, skills
- **Hooks** — user-defined handlers responding to lifecycle events (PreToolUse, PostToolUse, SessionStart, etc.)
- **MCP Servers** — Model Context Protocol connections to external tools/databases
- **Settings** — hierarchical configuration in `.claude/settings.json`
- **Memory** — persistent context via CLAUDE.md + rule organization

## 3. HOT FEATURES (Beta / Recent Additions — 11 features)

1. **Routines** — cloud automation on Anthropic infrastructure (scheduled/API-triggered)
2. **Ultrareview** — multi-agent code review with independent verification
3. **Devcontainers** — preconfigured development isolation
4. **Channels** — event routing from Telegram, Discord, webhooks
5. **Auto Mode** — background safety classifier (replaces manual permission prompts)
6. **Agent Teams** — multiple agents parallel on shared codebase
7. **Scheduled Tasks** — `/loop` (local, up to 7 days) + `/schedule` (cloud)
8. **Voice Dictation** — push-to-talk, 20-language support
9. **Code Review** — multi-agent PR analysis (bugs + security)
10. **Remote Control** — continue sessions from any device
11. **Computer Use** — Claude controls screen (macOS)

**Corpus-first observation:** No other Storm Bear corpus framework at T1 has documented this breadth of beta-feature tracking. ECC v1 / Superpowers v2 / claude-howto v32 are feature-stable catalogs; claude-code-best-practice is a **live-delta tracker** of Claude Code releases.

## 4. Orchestration Workflow — Command → Agent → Skill pattern

Visual architecture + weather-orchestrator demo.

**Usage pattern:**
```bash
claude
/weather-orchestrator
```

Flagship reference implementation. Entry via slash command → agent orchestrates → skills perform specialized tasks. Documented with animated GIF.

**Corpus observation:** Direct analog to spec-kit v17 workflow orchestration but lighter-weight (no 9-article constitution; emphasis on pattern-via-example, not methodology-via-rules).

## 5. Development Workflows comparison table (10+ frameworks)

Maintained comparison of Claude Code frameworks by star count + components:

| Workflow | Stars (per v34) | Agents | Commands | Skills | Unique features |
|----------|----------------|--------|----------|--------|-----------------|
| Everything Claude Code | 160k | 48 | 143 | 230 | Instinct scoring, AgentShield, multi-lang rules |
| Superpowers | 159k | 5 | 3 | 14 | TDD-first, Iron Laws, whole-plan review |
| Spec Kit | 89k | 0 | 9+ | 0 | Spec-driven, constitution model, 22+ tools |
| gstack | 76k | 0 | 0 | 37 | Role personas, /codex review, parallel sprints |
| Get Shit Done | 55k | 33 | 122 | 0 | Fresh contexts, wave execution, XML plans |

Additional frameworks mentioned (numeric positions not captured in WebFetch excerpt): BMAD-METHOD, OpenSpec, oh-my-claudecode, Compound Engineering, HumanLayer.

**⚠️ Fact-verification note:** The "160k" for ECC and "159k" for Superpowers appear LIVE-UPDATED by shanraisshan's automation. Storm Bear corpus at v1 had ECC much smaller; these numbers reflect April 2026 state. Numbers are plausible at enterprise scale but should be spot-verified against current GitHub API before quoting in Storm Bear Phase 4b.

**Corpus observation:** This is an **external meta-reference** cross-validating Storm Bear T1 selections. 5 of 5 listed here are Storm Bear wikis (ECC v1 / Superpowers v2 / spec-kit v17 / gstack v3 / GSD v5) — 100% overlap. Independent convergence signal.

## 6. 82 Tips and Tricks across 14 categories

Organized structure (category : tip count):

| Category | Count |
|----------|-------|
| Prompting | 3 |
| Planning/Specs | 6 |
| Context Management | 5 |
| Session Management | 6 |
| CLAUDE.md + Rules | 8 |
| Agents | 4 |
| Commands | 3 |
| Skills | 9 |
| Hooks | 5 |
| Workflows | 5 |
| Advanced Workflows | 9 |
| Git/PR | 5 |
| Debugging | 6 |
| Utilities | 5 |
| Daily | 2 |

**Total: 81 enumerated** (repo claims 82 — 1 discrepancy, likely a counting artifact; tracked as low-severity probe item).

### Notable tips extracted (corpus-relevant)

**Context management:**
- "Context degradation around 300-400k tokens"
- "Dumb zone at ~40% context utilization"
- Use `/rewind` (Esc Esc) over corrections to clean history
- Manual `/compact` beats autocompact
- Leverage subagents for context isolation

**CLAUDE.md discipline:**
- Target under 200 lines per file (60 lines ideal) — **Storm Bear vault CLAUDE.md currently 150K+ lines; flagged for refactor at v32**
- Auto-load `.claude/rules/*.md` with lazy-loading via paths: YAML
- Wrap domain-specific rules in `<important if="...">` tags
- Multiple CLAUDE.md for monorepos (ancestor/descendant loading)
- 3-scope CLAUDE.md pattern (reinforces claude-howto v32 observation)

**Skills architecture:**
- Use `context: fork` to isolate skill execution in subagents
- Structure skills in folders with progressive disclosure (references/, scripts/, examples/)
- Build Gotchas sections documenting failure points
- Write skill descriptions as triggers, not summaries
- Avoid railroading with prescriptive step-by-step instructions
- Embed `!command` in SKILL.md for dynamic shell output injection

**Advanced workflows:**
- ASCII diagrams for architecture understanding
- `/loop` for local recurring monitoring (≤7 days)
- `/schedule` for cloud tasks running offline
- Ralph Wiggum plugin for autonomous long-running tasks
- `/permissions` with wildcard syntax over `dangerously-skip-permissions`
- `/sandbox` for 84% reduction in permission prompts
- Build `/go` skill combining end-to-end testing + simplification + PR creation

**Voice + utilities:**
- `/voice` or Wispr Flow for voice prompting ("10x productivity" claim)
- iTerm/Ghostty/tmux over IDE

## 7. Video / Podcast Library

Named creators cited (corpus-firsts partial):
- **Boris Cherny** (Anthropic engineer, Claude Code creator) — multiple appearances (Pragmatic Engineer podcast, Lenny's Podcast, Y Combinator). **4th corpus mention of Boris Cherny** (after claude-howto v32, OMC v27 indirect, and other framework ambassadors).
- **Dex Horthy** — "Everything We Got Wrong About Research-Plan-Implement" (24 Mar 2026). 1st Dex Horthy corpus mention.
- **Cat Wu** — "Secrets of Claude Code From the Engineers". 1st Cat Wu corpus mention.

**Corpus pattern:** Intellectual lineage node is Anthropic team (Boris Cherny = Claude Code creator). Pattern #19 archetype 1 (individual-author lineage) strengthened by 6 touchpoints across 4 wikis on Boris Cherny. Karpathy + John Lam + Boris Cherny emerging as Storm Bear corpus's 3 primary individual-author lineage nodes.

## 8. Subscription Channels (community infrastructure)

**Reddit:** r/ClaudeAI, r/ClaudeCode, r/Anthropic
**X/Twitter:** Official @Claude, @ClaudeDevs, @Anthropic + community builders
**YouTube:** Official Anthropic channel + podcast networks

**Corpus observation:** Western-community-platform (Pattern #18 Western-community variant). No CN/VN/KR community channels documented — EN-only community curation.

## 9. Startups/Businesses Displaced table

Documents Claude Code features replacing existing products:

| Claude Feature | Replaced Products |
|---|---|
| Code Review | Greptile, CodeRabbit, Devin Review, OpenDiff |
| Voice Dictation | Wispr Flow, SuperWhisper |
| Remote Control | OpenClaw |
| Computer Use | OpenAI CUA |
| Chrome Integration | Playwright MCP, Chrome DevTools MCP |

**Corpus-first observation:** Storm Bear corpus does NOT have a comparable "commercial-displacement" table in any prior wiki. claude-code-best-practice introduces **commercial-ecosystem-impact-tracking** as corpus-first observation at T1.

Note: "OpenClaw" appears in the Remote Control row — interesting since Pattern #18 has OpenClaw as a community-platform runtime standard. shanraisshan frames OpenClaw as displaced-by-Claude-Code-built-in-remote-control. This is a notable narrative framing but doesn't invalidate OpenClaw's corpus role.

## 10. Billion-Dollar Questions (13 unanswered research questions)

Open research questions posed by maintainer spanning:
- Memory and instruction optimization
- Agent vs skill vs command selection criteria
- Specification versioning and maintenance
- Persona effectiveness for specialized agents
- Community vs personal skill integration
- Full codebase → spec → regeneration feasibility

**Corpus observation:** Naming open research questions as "billion-dollar" frames them as commercial-value-pending, not pure-research. Unique positioning in corpus — Storm Bear has had open-questions files in project-local but not repo-level "billion-dollar" framing.

## 11. Reports Section (technical deep-dives)

9+ analytical reports mentioned:
- Agent SDK vs CLI system prompts
- Browser automation MCP comparison
- Global vs project settings architecture
- Skills organization in monorepos
- Agent memory patterns
- Advanced tool use
- Usage and rate limits
- LLM day-to-day degradation
- Harness importance

**Corpus observation:** Report-genre content within a framework repo = novel format. Prior corpus wikis document patterns in README or docs; shanraisshan partitions analysis into dedicated report subfolder.

## 12. Philosophies verbatim

- **Core workflow pattern:** Research → Plan → Execute → Review → Ship
- **Context management:**
  - "Context rot kicks in around ~300-400k tokens"
  - "Dumb zone kicks in around ~40% context"
  - Rewind preferred over corrections
- **Autonomy philosophy:** "Don't babysit" (marked 🚫👶) — let Claude work independently on well-scoped tasks
- **Planning:** "Prototype > PRD" — build 20-30 versions instead of writing extensive specifications

**Positioning on Storm Bear corpus axes:**
- vs Pattern #51 Vibe-Coding Spectrum: "from vibe coding to agentic engineering" frames progression FROM vibe-pro TOWARD vibe-anti. Occupies the axis — not a pole.
- vs Pattern #13 Autonomy-Framing: "Don't babysit" + "Auto Mode" = autonomy-forward but with safety classifier guardrails. Between paperclip v14 (zero-human) and BMAD v11 (human amplification, not replacement).

## 13. Attribution + governance signals

- **Solo maintainer** with 498 commits (4 contributors total, 3 others with 1 each)
- Author: Shayan Rais (shanraisshan@gmail.com)
- **Badges claimed:** Claude for OSS / Claude Community Ambassador / Claude Certified Architect
- Governance files: README.md + CLAUDE.md + LICENSE + .gitignore + .mcp.json
- **Absent:** CONTRIBUTING.md / SECURITY.md / CODE_OF_CONDUCT.md / AGENTS.md
- Issue count: 16 open (low for 47K stars — may indicate rapid close-rate or selective triage)

**Pattern #12 Governance-Depth Correlation:** Solo T1 light-governance consistent (contrast spec-kit v17 6-file heavy governance at corporate T1).

## 14. Corpus-first observations (within this cluster)

1. **Live-delta tracker** of Claude Code releases (vs static catalog) — novel maintenance model
2. **Development Workflows comparison table** within a framework README — external meta-reference genre
3. **Startups Displaced table** — commercial-ecosystem-impact tracking
4. **Billion-Dollar Questions framing** — research questions as commercial-value-pending
5. **Automated 6-parallel-update-workflows** maintenance (maintainer describes infrastructure)
6. **"82 tips across 14 categories"** as headline structure (claude-howto v32 had 45 templates + 10 modules; this is denser tip-density)
7. **HTML primary language at T1** — 10 of 11 T1 wikis are TypeScript/Python/Shell/JS primary; HTML is novel primary-lang for T1
8. **Pakistani author archetype** at T1 — 1st Pakistani-authored framework in corpus
9. **3rd-most-starred Pakistan repo** self-attribution — regional-ranking metadata
10. **"Practice makes claude perfect"** pedagogical positioning — emphasis on iteration over specification

## 15. Implications for Phase 3 + Phase 4b

- Entity 1 (Core Product): document Command→Agent→Skill + 82-tip structure + HOT FEATURES tracker
- Entity 2 (Ecosystem positioning): Development Workflows table + 10-framework meta-reference role
- Entity 3 (Shayan Rais): Pakistani individual-publisher + multi-channel content + Pattern #17 11th data point
- Entity 4 (Storm Bear meta): regional-archetype meta-pattern #73 proposal + pilot-HIGH relevance + 82-tip adoption for vault refactor

Phase 4b will build T1 regional-archetype analysis (not 11-way — unwieldy) with #73 registration + sub-variant classification for Korean/VN/Pakistani.

---

*(C) Claude-generated 2026-04-23 per routine v2.1 Phase 2.*
