# Cluster — Agent-focused CLAUDE.README.md + src architecture

**Sources:** `CLAUDE.md` (4.5 KB, 121 lines — build/arch guide for Claude Code sessions inside the repo) + `CLAUDE.README.md` (13.9 KB, ~398 lines — agent-facing plugin reference with structured XML-like sections) + `src/` folder listing (18 files across src/ + subdirs i18n/, render/, utils/) + `commands/` (configure.md, setup.md) + `package.json` + repo topics.

**Cluster purpose:** Captures how a Claude Code agent (i.e., an LLM helping a user install or modify claude-hud) would understand the project — the "agent-legible" side distinct from the human-facing README.

---

## 1. Dual-documentation pattern (CORPUS NOTABLE)

claude-hud maintains **3 parallel documentation files**:

1. **`README.md`** — human-facing install + config + troubleshoot
2. **`CLAUDE.md`** — build/architecture guide for a Claude Code session *inside this repo* (i.e., for agents modifying claude-hud itself)
3. **`CLAUDE.README.md`** — agent-facing plugin reference for agents *installing claude-hud on a user's machine* (structured with XML-like `<agent_workflow>`, `<architecture>`, `<file_structure>`, `<task_instructions>` tags)

**This is a tri-file split** distinct from Pattern #22 (AGENTS.md emergence) — claude-hud has NO AGENTS.md. Instead it has two CLAUDE-prefixed files serving different agent contexts.

**CLAUDE.README.md novelty:** The name "CLAUDE.README.md" is a claude-hud coinage (not a standard convention in corpus). The file is structured with XML tags for LLM-legibility:
```
<plugin>
  <name>Claude HUD</name>
  <description>...</description>
</plugin>
<requirements>...</requirements>
<architecture>
  <overview>...</overview>
  <data_flow>...</data_flow>
  <data_sources>...</data_sources>
</architecture>
<file_structure>...</file_structure>
<output_format>...</output_format>
<context_thresholds>...</context_thresholds>
<plugin_configuration>...</plugin_configuration>
<development>...</development>
<customization>...</customization>
<troubleshooting>...</troubleshooting>
<key_interfaces>...</key_interfaces>
<task_instructions>
  <install>...</install>
  <modify>...</modify>
  <debug>...</debug>
  <understand>...</understand>
</task_instructions>
```

**Observation — XML-structured agent-reference:** This formatting pattern is notable in corpus. Most T1 corpus entrants use markdown prose or markdown section headers. claude-hud wraps content in XML tags presumably because (a) Claude models are trained to attend to XML-structure in prompts, (b) `<task_instructions>` sub-tags allow agents to branch behavior based on user intent (install vs modify vs debug vs understand).

**Cross-reference:** Pattern #22 (AGENTS.md emergence as T1 industry standard at v17) has been "AGENTS.md adoption" framing. claude-hud introduces an orthogonal axis: **task-branched XML agent reference** vs **flat markdown AGENTS.md**. Observation; not registered.

---

## 2. For-Humans + For-LLM-Agents split

CLAUDE.README.md explicitly segments content:

```
## For Humans
<3-step install>

## For LLM Agents
<6-step agent_workflow with bash commands and consent-gated star action>

## Reference
<architecture + file_structure + task_instructions>
```

**The agent workflow (Step 6) is consent-gated:**
```
Ask the user: "Would you like to star the repository to support the project?"
Only if they explicitly agree, run:
  if gh help repo 2>/dev/null | grep -q "star:"; then
    gh repo star jarrodwatts/claude-hud
  else
    gh api -X PUT /user/starred/jarrodwatts/claude-hud
  fi
Never run this automatically without user consent.
```

**Observation:** This is the **first corpus instance of explicit consent-gated LLM-driven starring mechanism documented in-repo**. Pattern #27 (Community-Viral Scale) in-wiki instances have been Reddit-viral / multi-channel-pedagogical / corporate-amplified / solo-organic-sustained / native-plugin-marketplace. **Consent-gated LLM-asks-for-star** is a new sub-pattern at N=1; not registered per consolidation-forward discipline.

---

## 3. src/ architecture (from CLAUDE.md + contents listing)

```
src/
├── claude-config-dir.ts        # ~/.claude config discovery
├── config-reader.ts            # Count CLAUDE.md / rules / MCPs / hooks
├── config.ts                   # Load/validate user config
├── constants.ts                # Shared constants
├── context-cache.ts            # Context calculation cache
├── cost.ts                     # Optional cost display
├── debug.ts                    # Debug logging
├── effort.ts                   # (likely effort/thinking mode tracking)
├── external-usage.ts           # Fallback usage snapshot path
├── extra-cmd.ts                # (likely extra CLI commands)
├── git.ts                      # Git status (branch / dirty / ahead-behind)
├── index.ts                    # Entry point, orchestrator
├── memory.ts                   # System RAM usage
├── speed-tracker.ts            # Token speed calculation
├── stdin.ts                    # Parse Claude's JSON input
├── transcript.ts               # Parse transcript JSONL
├── types.ts                    # TypeScript interfaces
├── version.ts                  # Version / CC version detection
├── i18n/                       # Language label tables (en, zh)
├── render/                     # Render functions per line type
│   ├── index.ts                # Main coordinator
│   ├── session-line.ts         # Compact single-line mode
│   ├── tools-line.ts           # Tool activity (opt-in)
│   ├── agents-line.ts          # Agent status (opt-in)
│   ├── todos-line.ts           # Todo progress (opt-in)
│   ├── colors.ts               # ANSI color helpers
│   └── lines/
│       ├── index.ts
│       ├── project.ts          # Line 1
│       ├── identity.ts         # Line 2a (context bar)
│       ├── usage.ts            # Line 2b (usage bar)
│       └── environment.ts      # Config counts (opt-in)
└── utils/                      # (likely width / truncation / ANSI helpers)
```

**Module count:** ~22 files including i18n/render/utils subdirs. **Structure signals:**
- Each data-source gets its own module (stdin / transcript / git / config-reader / external-usage / memory)
- Render modules per line — clean separation of concerns
- i18n isolated — labels-only, easy to add languages
- utils/ separation — likely shared pure helpers (width calc, ANSI, truncation)

**Corpus observation:** Module-per-concern discipline is unusually clean for a 3-month-old project. Suggests the author either has strong prior TypeScript engineering habits OR the codebase was refactored early (which CHANGELOG suggests — v0.0.6 "Expanded multi-line layout mode splits the overloaded session line into semantic lines (#76)").

---

## 4. Data flow (CLAUDE.md architecture section)

```
Claude Code invokes the plugin (~every 300ms)
  ↓
Plugin reads JSON from stdin (model, context, tokens)
  ↓
Plugin parses transcript JSONL file (tools, agents, todos)
  ↓
Plugin reads config files (MCPs, hooks, rules)
  ↓
Plugin renders lines to stdout
  ↓
Claude Code displays the statusline
```

**Key constraints implicit in this flow:**
- **Stateless per-invocation** — every ~300ms, plugin starts cold. Explains `context-cache.ts` module (to amortize expensive calcs across invocations).
- **Read-only** — no writes back to Claude Code's state. Pure observer.
- **Bounded latency budget** — 300ms cadence means each invocation must complete well under 300ms or the statusline lags.

**Implication for pattern observation:** claude-hud is an **extension-point consumer** of Claude Code (not an orchestrator, not a wrapper). It lives in Claude Code's lifecycle, invoked at Claude Code's discretion, writing to Claude Code's terminal. Contrast deer-flow v9 (wrapper around Claude Code via OAuth), graphify v16 (Claude-Code-skill-based consumer), oh-my-claudecode v27 (orchestrator of multiple CLI runtimes).

**Pattern #18 Agent Runtime Standardization extension:** claude-hud reinforces Claude Code as runtime standard, but via a NEW consumption mode — **statusline API extension-point consumer**. Prior Pattern #18 observations were MCP-consumer, plugin-marketplace-install, skill-registration. Extension-point (statusline API) is a distinct consumption mode within Pattern #18's umbrella.

---

## 5. commands/ directory — 2 slash commands

```
commands/
├── configure.md    # 12,362 bytes — /claude-hud:configure guided flow
└── setup.md        # 18,706 bytes — /claude-hud:setup initial install
```

Both files are substantial (18 KB setup.md exceeds README.md size). They're Claude Code slash-command definitions — markdown with embedded behavioral instructions that the invoked agent executes.

**Observation:** `setup.md` being 18 KB signals rich conditional logic (platform detection, Windows/Linux caveats, optional feature onboarding, GitHub star prompt, config-preset selection). The setup flow is effectively an onboarding *program* expressed as a prompt-markdown file.

**This is a corpus-visible pattern:** slash-command-as-program. Prior corpus observations include claude-howto v32 (copy-paste templates), codymaster v12 (79 skills, 11 commands), oh-my-claudecode v27 (8 orchestration modes). claude-hud's 2-command minimum with 30 KB of combined slash-command content represents the **concentrated-onboarding** variant: few commands, rich per-command behavior.

---

## 6. Key TypeScript interfaces (from CLAUDE.README.md)

```typescript
interface StdinData {
  transcript_path?: string
  cwd?: string
  model?: { id?: string, display_name?: string }
  context_window?: {
    used_percentage?: number
    context_window_size?: number
    current_usage?: { input_tokens?: number }
  }
}

interface ToolEntry {
  id: string
  name: string
  target?: string
  status: 'running' | 'completed' | 'error'
  startTime: Date
  endTime?: Date
}

interface AgentEntry {
  id: string
  type: string
  model?: string
  description?: string
  status: 'running' | 'completed'
  startTime: Date
  endTime?: Date
}

interface TodoItem {
  content: string
  status: 'pending' | 'in_progress' | 'completed'
}

interface RenderContext {
  stdin: StdinData
  transcript: TranscriptData
  claudeMdCount: number
  rulesCount: number
  mcpCount: number
  hooksCount: number
  sessionDuration: string
}
```

**Observations:**
- Interfaces mirror Claude Code's internal JSON shape — plugin is effectively a schema-matcher for Claude Code's extension-point contract.
- `ToolEntry.status` includes `'error'` — plugin handles tool-failure visually. Implied: red color for errored tools.
- `RenderContext` aggregates from 6 sources (stdin + transcript + 4 config count fields + session duration) into a single render argument.

---

## 7. Customization section (CLAUDE.README.md)

Documented extension procedure:

```
<extending description="How to add new features">
  <step>Add new data extraction in transcript.ts or stdin.ts</step>
  <step>Add new interface fields in types.ts</step>
  <step>Create new render file in src/render/ or modify existing</step>
  <step>Update src/render/index.ts to include new line</step>
  <step>Run npm run build and test</step>
</extending>

<adding_new_line>
  1. Create src/render/new-line.ts with a render function
  2. Import and call it from src/render/index.ts
  3. Add any needed types to src/types.ts
  4. Add data extraction logic to transcript.ts if needed
</adding_new_line>
```

**Observation:** The extension guide is the smallest-possible 5-step surface. Suggests author intends modification to be approachable by other LLM agents reading CLAUDE.README.md directly.

---

## 8. package.json — minimal build surface

```json
{
  "name": "claude-hud",
  "version": "0.1.0",
  "type": "module",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "dev": "tsc --watch",
    "test": "npm run build && node --test",
    "test:coverage": "npm run build && c8 --reporter=text --reporter=lcov node --test",
    "test:update-snapshots": "UPDATE_SNAPSHOTS=1 npm test",
    "test:stdin": "npm run build && echo '{...}' | node dist/index.js"
  },
  "engines": { "node": ">=18.0.0" },
  "devDependencies": {
    "@types/node": "^25.6.0",
    "c8": "^11.0.0",
    "typescript": "^6.0.3"
  }
}
```

**Observations:**
- **ZERO runtime dependencies.** (No `dependencies` field.) Pure stdlib + Node.js built-in test runner + TypeScript + c8 for coverage. Tree-shaking at its extreme — the product is TypeScript + stdin parsing + JSON parsing + ANSI output.
- **Native Node test runner** — `node --test` (built-in since Node 18). No Jest, Vitest, Mocha. Matches "minimal dependency story."
- **Version in package.json is `0.1.0`** — but CHANGELOG last tagged entry is `[0.0.12] 2026-04-04`. Suggests `0.1.0` is Unreleased (CHANGELOG shows `[Unreleased]` as first heading). **Version-skew caveat** for downstream fact-verification.

---

## 9. Topics (GitHub metadata)

```
anthropic, claude, claude-code, cli, plugin, statusline, typescript
```

7 topics. **Observations:**
- Includes `cli` despite being a Claude-Code-only plugin (arguably minor misnomer — the plugin isn't a standalone CLI).
- Includes `anthropic` (company) + `claude` (model) + `claude-code` (tool). Triple-tagging across the Claude product family for discoverability.
- `statusline` is a niche topic — likely narrow corpus coverage for this tag.

---

## 10. Observations for downstream phases

1. **Tri-file documentation split** (README / CLAUDE.md / CLAUDE.README.md) is corpus-notable; the CLAUDE.README.md naming is claude-hud coinage.
2. **XML-structured agent reference** in CLAUDE.README.md is distinct formatting convention; observation only (not N=2 yet in corpus).
3. **Module-per-concern** in src/ suggests strong TypeScript engineering discipline at 3-month project age.
4. **Zero runtime dependencies** extreme tree-shake signals intent for long-term maintainability and easy audit.
5. **Extension-point consumer** architecture (statusline API) is a NEW Pattern #18 consumption mode alongside prior MCP / skill / plugin-install modes.
6. **Consent-gated LLM-ask-for-star** mechanism documented in CLAUDE.README.md is corpus-first; not registered.
7. **Task-branched agent reference** (`<task_instructions>` with install/modify/debug/understand sub-tags) is a unique agent-legibility pattern.

---

*(C) Claude-generated 2026-04-23 per routine v2.1 Phase 2.*
