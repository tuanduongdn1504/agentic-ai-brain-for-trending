# (C) Skill System (Progressive Loading)

> Entity page — Building block
> Sources: README skills framework + CONTRIBUTING skills folder structure
> Format: 13-section canonical

## 1. What is it / Nó là gì

**Skill System** = deer-flow's modular capability framework. Each skill = Markdown file defining specific capability (research, report-gen, slide-creation, web-ops). **Progressive loading** = skills load khi context needs them, NOT all at once. Conserves context window.

Structure:
- `skills/public/` — built-in (deer-flow ships these)
- `skills/custom/` — user-created (community + organization skills)

## 2. Why it matters / Sao quan trọng

### Context window pressure is real

Long-horizon tasks = lots of context accumulated:
- Task description
- Research findings
- Sub-agent outputs
- Tool results
- Memory recalls

If ALL skills + ALL context → context overflow → LLM performance degrades.

**Progressive loading solves:**
- Load only skills relevant to current task
- Unload skills not needed
- Keeps context lean for actual work

### Skill-as-markdown = portability

Compared to code-based skills:
- Markdown = human-readable
- Markdown = editable by non-programmers
- Markdown = version-controllable naturally
- Markdown = shareable across frameworks

**Aligns với trend** — Claude Code skills also often Markdown-first (ECC ecosystem).

## 3. Skill structure (inferred pattern)

Based on README hints + Markdown-based convention:

```markdown
# [Skill Name]

## Description
[When to use this skill]

## Invocation patterns
- Trigger phrases
- Tool name

## Capabilities
- [List of things skill does]

## Parameters
- Input schema

## Examples
[Usage examples]

## Notes / Limitations
[Caveats]
```

→ **Similar to Claude Code skill file format.** Interoperability potential.

## 4. Built-in skills (from README)

| Skill | Purpose |
|-------|---------|
| Research | Multi-angle deep research |
| Report generation | Structured reports với visuals |
| Slide creation | Presentation generation |
| Web operations | Content creation + modification |
| Code execution | Run code in sandbox |
| File operations | Workspace management |
| Image/video | Generation + analysis |

## 5. Progressive loading mechanism

### How it works (inferred)

1. User submits task
2. Lead agent analyzes task
3. Lead agent identifies needed skills (via skill metadata)
4. Only those skills load into context
5. Sub-agents inherit relevant skills only
6. Unused skills stay on disk

### Context-aware loading

- **Task signals:** "research" + "presentation" → load research + slide skills
- **NOT loaded:** image-gen, code-exec (unless mentioned)
- **Dynamic:** if task evolves, additional skills load mid-execution

### Compare to non-progressive approaches

| Pattern | Context load | Trade-off |
|---------|--------------|-----------|
| All-skills-at-once | Heavy | Simple; overflow risk |
| Progressive (deer-flow) | Light | Complex logic; stays lean |
| Lazy function calls | Variable | Tool discovery matters |

## 6. Custom skills (user extension)

### Adding skill workflow (inferred từ CONTRIBUTING)

1. Create Markdown file in `skills/custom/my-skill.md`
2. Follow skill metadata format
3. Restart deer-flow (or hot-reload if available)
4. Skill now available to agents

### Use cases for custom skills

- **Organization-specific workflows** — e.g., "generate Scrum retro report trong company template"
- **Integration with internal APIs** — e.g., "query internal KB via custom skill"
- **Vietnamese-language skills** — e.g., "Vietnamese-content translation skill"
- **Domain specialization** — e.g., "legal compliance check skill"

## 7. Skill vs Tool vs Agent (distinction)

| Concept | Role | Example |
|---------|------|---------|
| **Tool** | Single function | `web_search(query)` |
| **Skill** | Workflow orchestrating tools | "research" = web_search + summarize + structure |
| **Agent** | Long-horizon entity using skills + tools | Lead agent managing research task |

→ **Skills = middle abstraction.** More expressive than tools, less autonomous than agents.

## 8. Trade-offs / Limitations

### Strengths
- **Context-conservation** — critical for long tasks
- **Markdown = editable** — low barrier for custom skills
- **Modular** — skills composable
- **Public + custom split** — organization governance possible
- **Progressive = efficient** — only load what's needed

### Weaknesses
- **Skill discovery latency** — analysis step before load = small overhead
- **Skill conflicts** — 2 skills claiming same trigger = ambiguous
- **Quality variance** — custom skills unvetted
- **Upgrade friction** — built-in skill change may break custom skills depending on it
- **Documentation gap** — adding skill detailed docs not in CONTRIBUTING

## 9. Comparison to sibling skill systems

| Sibling | Skill model | Count | Size pattern |
|---------|-------------|-------|--------------|
| ECC (T1) | Many small skills | ~185 | ~2-5 KB each |
| Superpowers (T1) | Pattern library skills | ~50 | ~3-10 KB each |
| gstack (T1) | Specialist roles | ~15 | ~5-15 KB each |
| GSD (T1) | Commands + agents mix | 33 + 83 | ~3 KB each |
| goclaw (T2) | Platform-level | N/A | Per-tenant config |
| course (T3) | N/A (teaches concepts) | — | — |
| notebooklm-py (T4) | Single mega-SKILL | 1 | 26 KB |
| build-your-own-x (outside) | N/A | — | — |
| **deer-flow (T5)** | **Progressive public+custom** | **Variable** | **Markdown, progressive-loaded** |

→ **deer-flow skill system unique** — not many-small (ECC) not one-big (notebooklm-py) but **progressive library** splitting public vs custom.

## 10. Common pitfalls

1. **Custom skill conflicts** — 2 users' skills claim same capability → first-wins ambiguity
2. **Missing metadata** — skill file without proper metadata won't load
3. **Skill dependencies unmanaged** — skill A depends on skill B; missing B = skill A silently fails
4. **Old skill references old API** — LangGraph or backend updates break custom skills
5. **Hot-reload confusion** — some changes need full restart; unclear which
6. **Progressive loading debug nightmare** — "why didn't my skill load?" hard to diagnose
7. **Context leaking** — skill that was relevant yesterday still loaded today = bloat

## 11. When NOT to use progressive skills

- **Simple script automation** — cron + bash simpler than Skills framework
- **Single-purpose task** — monolithic prompt enough
- **Real-time chat** — context loading latency matters
- **Debugging complex flow** — progressive loading adds surprise

## 12. Storm Bear vault relevance

### Storm Bear's skill pattern vs deer-flow

**Storm Bear current:**
- `05 Skills/` folder với 5 skills (`brain-setup`, `llm-wiki-ingest`, `llm-wiki-routine`, `new-project`, plus built-in from ECC)
- ALL skills loaded via Claude Code's skill system
- Not progressive; all-at-once

**deer-flow progressive advantage:**
- If Storm Bear vault grows to 50+ skills, all-at-once breaks
- Progressive = solution for scale

### Potential Storm Bear adoption

1. **Port Storm Bear skills to deer-flow Markdown format** — test cross-framework portability
2. **Adopt progressive loading concept** — routine v2 could lazy-load skill definitions
3. **Custom skills for Scrum coaching** — e.g., `retro-synthesis`, `team-health-report`, deployable in deer-flow

### Meta-pattern

**Skill-as-Markdown convention emerging** across frameworks (ECC, Superpowers, deer-flow, Storm Bear vault). Shared convention = interoperability potential.

Future: Skill Portability Standard? Currently informal.

## 13. References / Nguồn

- Source: [[(C) README summary]] (skills framework section) + [[(C) Architecture + Contributing cluster summary]] (skills/ folder)
- Related entities:
  - [[(C) SuperAgent Harness Architecture]] (skill = 1 of 5 components)
  - [[(C) Sub-Agent System (Parallel Fan-out)]] (sub-agents inherit skills)
- Sibling skill patterns:
  - `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) Skills.md` (if exists)
  - `../../notebooklm-py - Beginner Analysis/02 Wiki/(C) Skill Integration (Claude Code + Codex + OpenClaw).md`
- Vault skills:
  - `../../../05 Skills/llm-wiki-routine.md`
  - `../../../05 Skills/llm-wiki-ingest.md`
