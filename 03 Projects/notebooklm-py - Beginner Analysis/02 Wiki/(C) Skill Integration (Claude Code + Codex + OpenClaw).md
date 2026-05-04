# (C) Skill Integration (Claude Code + Codex + OpenClaw)

> Entity page — Integration concept
> Sources: SKILL.md invocation patterns + Claude Code integration scenarios + README agent integration section
> Format: 13-section canonical

## 1. What is it / Nó là gì

**Skill Integration** = cách notebooklm-py được packaged + consumed as a **reusable Skill file** cho AI agents (Claude Code, Codex, OpenClaw). Instead of each agent reimplementing NotebookLM integration, library ships `SKILL.md` (26 KB) + `notebooklm skill install` command để populate agent skill directory.

**Three distribution channels:**
1. `notebooklm skill install` — local CLI copies to `~/.claude/skills/notebooklm`
2. `npx skills add teng-lin/notebooklm-py` — npx ecosystem
3. Manual copy SKILL.md into agent skill dir

## 2. Why it matters / Sao quan trọng

**First sibling to ship skill as bundled deliverable.** Other siblings:

- ECC — ships many small skills (per-feature)
- Superpowers — ships skills library (per-pattern)
- gstack — ships specialist roles (per-role)
- GSD — ships commands + agents (per-command)
- goclaw — platform, no skill format
- course — teaches about skills conceptually, doesn't ship any

**notebooklm-py pattern = "one mega-skill consolidates entire library into SKILL.md"**. 26 KB is unusual. Not many small skills; one big reference.

**Why agent-first design matters:**
- Users don't need to read README to use library via agent
- Agent loads SKILL.md, invokes CLI, result flows back via `--json`
- Zero Python code required for consumers

## 3. SKILL.md structure (26 KB)

Sections from SKILL.md:

1. **What the skill is** — positioning + capabilities summary
2. **Invocation patterns** — explicit (`/notebooklm`) + intent-based auto-trigger
3. **Authentication flow** — login + CI/CD alternatives
4. **Core operations** — notebook/source/chat/artifact per-domain matrices
5. **Content generation options** — audio 4-format × video 2-format × slide 2-format × quiz/flashcard/report matrix
6. **Download formats** — per-artifact format options
7. **Autonomy rules** — which ops run without confirmation vs need approval
8. **Workflow patterns** — 5 named patterns (interactive, background, document analysis, deep research, parallel safety)
9. **Output formats** — JSON schemas for each operation
10. **Error handling** — failure scenarios + recovery
11. **Claude Code integration scenarios** — 4 complete Python code samples
12. **Source limits & plan details** — Standard/Plus/Pro/Ultra tiers
13. **Installation verification** — doctor command + smoke tests

→ **Single file covers operational spec, not just API reference.**

## 4. Invocation patterns (from SKILL.md)

### Explicit triggers
- User says `/notebooklm` → agent loads skill
- Agent tool-registry matches name `notebooklm`

### Intent detection (auto-activation)
Skill file lists trigger phrases:
- "Create a podcast about [topic]"
- "Summarize these URLs"
- "Generate a quiz from my research"
- "Turn this into an audio overview"
- "Make flashcards for studying"

When user intent matches, agent pulls SKILL.md into context + executes commands.

## 5. Autonomy rules (trust boundary)

**Agent runs without confirmation:**
- Read-only: status, list, fulltext, history view
- Setup: auth, profile switch, context set (`use`)
- Ephemeral: chat queries (not saved)
- Background waits

**Agent requires confirmation:**
- Destructive: `delete` (notebook, source)
- Expensive: `generate *` (cost + time)
- Filesystem: `download` (writes local disk)
- Persistence: `--save-as-note`, `history --save`

→ **Principled autonomy boundary.** Matches usability + safety. Mirror-able pattern cho agent skill design generally.

## 6. Workflow patterns (5 from SKILL.md)

### Pattern 1: Interactive Research to Podcast
Linear: create → add sources → verify ready → generate → download.
Total time: 15-30 min (audio generation dominant).

### Pattern 2: Automated with Background Agent
Create + generate → spawn subagent to wait + download → main conversation continues.
Total time: non-blocking; agent returns to user.

### Pattern 3: Document Analysis
Create → add docs → multi-turn chat (follow-up Qs).
Total time: minutes per Q.

### Pattern 4: Deep Web Research (Background)
Create → `source add-research --mode deep --no-wait` → subagent `research wait --import-all`.
Total time: 15-30+ min research, non-blocking.

### Pattern 5: Parallel Workflow Safety
Multiple agents → always explicit `-n <id>` + unique `NOTEBOOKLM_PROFILE` per agent.
Rule of thumb: don't rely on context file in parallel work.

## 7. Integration scenarios (from SKILL.md Claude Code examples)

Each scenario = complete Python code sample using `subprocess` to invoke CLI:

### Scenario 1: Generate Podcast and Wait (~50 lines)
```python
result = subprocess.run(["notebooklm", "generate", "audio", ..., "--json"], capture_output=True)
data = json.loads(result.stdout)
artifact_id = data["task_id"]
# Polling loop or subagent wait
# Then: download audio
```

### Scenario 2: Batch Research (~40 lines)
Add multiple sources parallel, wait all, then ask.

### Scenario 3: Deep Web Search with Subagent (~20 lines)
`source add-research --mode deep --no-wait` + subagent wait.

### Scenario 4: Citation Lookup (~30 lines)
Retrieve source fulltext, locate citation substring, extract context window.

→ **Drop-in usable code.** Agents copy-paste with minimal modification.

## 8. Trade-offs / Limitations

### Strengths
- **One SKILL.md = complete reference** — agent loads once, covers everything
- **Zero-code consumption** — CLI + `--json` enough
- **Multi-agent compat** — Claude Code, Codex, OpenClaw all supported
- **Trust boundary explicit** — autonomy rules prevent surprise

### Weaknesses
- **26 KB context load** — skill consumes agent context window
- **Single file overwhelm** — not browsable like 50 small skills
- **OpenClaw unclear** — listed without explanation; unverifiable compat
- **No plugin marketplace registration** — manual install per agent
- **Update mechanism unclear** — how does agent refresh SKILL.md when library updates?

## 9. Comparison to sibling skill patterns

| Sibling | Skill count | Avg size | Total size | Pattern |
|---------|-------------|----------|------------|---------|
| **ECC** | ~185 skills | ~2-5 KB | ~500 KB | Many small, browsable |
| **Superpowers** | ~50 skills | ~3-10 KB | ~300 KB | Pattern library |
| **gstack** | ~15 roles | ~5-15 KB | ~150 KB | Role specialization |
| **GSD** | ~33 agents + 83 commands | ~3 KB each | ~350 KB | Command + agent mix |
| **goclaw** | Platform-level | N/A | Platform | No per-skill |
| **course** | Teaches concepts | — | — | — |
| **notebooklm-py** | **1 SKILL.md** | **26 KB** | **26 KB** | **Single mega-skill** |

→ **Opposite extreme from ECC.** ECC = 185 small files. notebooklm-py = 1 big file. **Trade-off:** ECC browsable/composable; notebooklm-py complete/contextual.

**Interesting hybrid:** Storm Bear's `llm-wiki-ingest.md` (420 lines) is closer to notebooklm-py pattern — one big file covers entire workflow.

## 10. Common pitfalls

1. **Not installing skill** — agent invents CLI commands, gets syntax wrong
2. **Outdated SKILL.md** — agent uses commands from older version, library rejects
3. **Missing autonomy check** — agent runs destructive op without confirmation
4. **Profile collision** — 2 agents, same profile = credential chaos
5. **Rate limit cascade** — 3 agents generating audio simultaneously → all throttled
6. **Skill not loaded** — agent has no context about NotebookLM; agents guess; guesses fail
7. **Silent SKILL.md update failure** — library updates, skill file doesn't auto-refresh

## 11. When NOT to adopt skill

- **Not using any agent** — just use CLI directly via shell
- **Not using NotebookLM** — skill has zero value without Google NotebookLM subscription
- **Agent doesn't support external skill files** — fallback = include SKILL.md content in prompt
- **Concerned about context bloat** — 26 KB can be significant on small context windows

## 12. Storm Bear vault relevance

**Primary adoption path cho Storm Bear:**

### Install skill in Claude Code
```bash
pip install notebooklm-py
notebooklm login                 # one-time auth
notebooklm skill install         # populates ~/.claude/skills/notebooklm
```

Now Claude Code understands NotebookLM. User says "turn Q1 retro notes into a podcast" → Claude Code loads SKILL.md, executes workflow.

### Storm Bear vault integration opportunities

1. **Per-wiki podcast** — after routine builds wiki, optional NotebookLM podcast for team audio consumption
2. **Cross-wiki synthesis** — ask NotebookLM questions that span multiple wiki guides
3. **Scrum retro pipeline** — transcript → NotebookLM → podcast summary for async team
4. **Published guide quality check** — NotebookLM quiz/flashcards from vault wiki → validates coverage

### Routine v2 optional phase
Could add as **Phase 4c (optional):** "Generate NotebookLM podcast from published guide." Invoked only if user opts in.

### Meta-observation
Storm Bear's `llm-wiki-ingest` skill ≈ notebooklm-py's SKILL.md:
- Both = single mega-skill
- Both = consolidated workflow reference
- Both = orchestrate multiple CLI/API operations
- Difference: Storm Bear builds wiki; notebooklm-py bridges external service

## 13. References / Nguồn

- Source: [[(C) SKILL summary]] (invocation + integration scenarios)
- Related entities:
  - [[(C) CLI Surface]] (skill commands = CLI)
  - [[(C) Python API Architecture]] (skill can also invoke Python)
- Sibling skill patterns:
  - `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) Skills.md` (ECC many small skills)
  - `../../Superpowers - Beginner Analysis/02 Wiki/(C) Skills Library.md`
- Storm Bear skills for comparison:
  - `../../../05 Skills/llm-wiki-ingest.md` (mega-skill pattern)
  - `../../../05 Skills/llm-wiki-routine.md` (orchestration)
