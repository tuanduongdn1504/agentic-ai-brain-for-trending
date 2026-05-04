# (C) Sub-Agent System (Parallel Fan-out)

> Entity page — Workflow concept
> Sources: README sub-agent section + architecture diagrams
> Format: 13-section canonical

## 1. What is it / Nó là gì

**Sub-Agent System** = deer-flow's pattern for **parallel task decomposition**. Lead agent analyzes complex task → spawns multiple sub-agents → each sub-agent has **isolated context** tackling **one decomposed segment** → lead synthesizes results.

Key innovations:
- **Isolated context per sub-agent** (no shared state pollution)
- **Parallel execution** (throughput improvement)
- **Lead orchestration** (central intelligence decomposes + synthesizes)

## 2. Why it matters / Sao quan trọng

### Single-agent limits

One agent handling complex task:
- **Context bloat** — task + research + code + synthesis = exceeds window
- **Serial execution** — can't parallelize naturally
- **Context interference** — research pollutes coding context

### Sub-agent benefits

- **Specialization** — sub-agent A research, sub-agent B writes, sub-agent C codes
- **Parallelism** — 3 sub-agents concurrent = 3× throughput
- **Isolation** — research context doesn't pollute code context
- **Fault tolerance** — sub-agent B crashes, others continue

### deer-flow's bet

Long-horizon tasks benefit MORE from parallelism than short tasks. **Sub-agents** = infrastructure advantage over single-agent loops (AutoGPT-era).

## 3. Fan-out → Execute → Synthesize pattern

### Phase 1: Fan-out (Lead analyzes)

```
User: "Research quantum computing và write a report"

Lead Agent:
  - Decompose: [Research subtask] + [Writing subtask]
  - For each subtask, spawn sub-agent với isolated context
```

### Phase 2: Parallel Execute (Sub-agents work)

```
Sub-Agent A (Research):
  Context: research skill + web tools + notes storage
  Task: "Research quantum computing, gather 10 key findings"
  Output: research notes file

Sub-Agent B (Writing — awaits A):
  Context: report-gen skill + notes reader + writer tool
  Task: "Write comprehensive report from research notes"
  Output: report file

Sub-Agent C (optional — e.g., Visuals):
  Context: image-gen skill
  Task: "Generate cover image for report"
  Output: image file
```

**Parallelism:** if tasks independent, run concurrent. If dependent (B needs A), sequence.

### Phase 3: Synthesize (Lead merges)

```
Lead Agent:
  - Wait for all sub-agents complete
  - Read outputs from sandbox
  - Merge into final artifact
  - Return to Gateway API
```

## 4. Sub-agent isolation mechanics

### Context isolation

Each sub-agent:
- Own LLM conversation history
- Own skill set (progressive loading within sub-agent)
- Own tool access
- Own sandbox filesystem area

→ **Crash/error contained.** Sub-agent A's failure doesn't invalidate B's work.

### Shared resources (controlled)

Sub-agents share:
- **Sandbox filesystem** (but with namespacing)
- **Memory store** (read-only recall; writes coordinate)
- **LLM provider** (but separate call context)

### Coordination

Lead agent coordinates:
- Task decomposition (what each sub-agent does)
- Dependencies (B waits for A)
- Synthesis (merge outputs)

→ **Hierarchical pattern** — lead controls, sub-agents execute.

## 5. Use cases enabled

### Deep research với multi-angle
- Sub-agent A: historical context
- Sub-agent B: current research
- Sub-agent C: future predictions
- Parallel research → richer synthesis

### Multi-format output
- Sub-agent A: write report
- Sub-agent B: create slides
- Sub-agent C: generate audio version
- Single task → multiple deliverables

### Data pipeline
- Sub-agent A: extract data from source 1
- Sub-agent B: extract from source 2
- Sub-agent C: transform + merge
- Sub-agent D: load to destination
- Parallel extraction, coordinated transformation

### Complex debugging
- Sub-agent A: analyze logs
- Sub-agent B: check config
- Sub-agent C: test hypothesis
- Lead synthesizes root cause

## 6. Comparison to single-agent pattern

| Axis | Single-agent | Sub-agent (deer-flow) |
|------|--------------|----------------------|
| **Context size** | One big context | Multiple small contexts |
| **Specialization** | Generalist | Specialists |
| **Parallelism** | Serial | Parallel (when independent) |
| **Fault tolerance** | Whole-task failure | Partial-failure recovery |
| **Debugging** | Single trace | Multi-trace (harder) |
| **Cost** | N tokens | Often > N (multiple agents) |
| **Throughput** | 1× | Up to K× (K sub-agents) |

**Trade-off:** More complexity + cost for throughput + isolation.

## 7. Trade-offs / Limitations

### Strengths
- **Throughput** — parallelism genuinely faster
- **Isolation** — crashes contained
- **Specialization** — each sub-agent focused
- **Scalability** — add sub-agents as task grows

### Weaknesses
- **Cost multiplier** — N sub-agents = N× LLM spend
- **Coordination overhead** — lead's decomposition + synthesis burden
- **Debugging harder** — 5 traces vs 1 trace
- **Race conditions** — shared sandbox = write conflicts possible
- **Over-decomposition** — split when single would do = waste
- **Under-decomposition** — single sub-agent hits context bloat

## 8. Comparison to sibling multi-agent approaches

| Sibling | Multi-agent pattern |
|---------|---------------------|
| **ECC (T1)** | Subagents concept (Claude Code native) |
| **Superpowers (T1)** | Subagent-driven development (7-stage) |
| **gstack (T1)** | Specialist roles (sprint pipeline) |
| **GSD (T1)** | 33 specialized agents + 83 commands |
| **goclaw (T2)** | Agent teams per tenant (platform) |
| **course (T3)** | Teaches multi-agent pattern (Lesson 08) |
| **notebooklm-py (T4)** | N/A (single library) |
| **build-your-own-x (outside)** | N/A |
| **deer-flow (T5)** | **Lead + parallel sub-agents với isolated context** |

### Key differentiators
- **deer-flow: autonomous fan-out** — lead decides decomposition at runtime
- **gstack: predefined roles** — pipeline stages fixed
- **GSD: library of agents** — user picks agent
- **ECC/Superpowers: subagents feature** — more lightweight than deer-flow

## 9. Sub-agent vs parallelism in Storm Bear context

### Storm Bear routine current

Sequential phases:
- Phase 1: scaffold (single task)
- Phase 2: 3 source summaries (serially)
- Phase 3: 4 entity pages (serially)
- Phase 4: 2 published guides (serially)

**All serial.** Claude Code session.

### Sub-agent pattern adoption potential

If routine refactored với sub-agents:
- **Phase 2 parallel:** 3 source summaries simultaneously (3× speedup)
- **Phase 3 parallel:** 4 entity pages simultaneously (4× speedup)
- **Overall:** routine time ~2h → potentially ~45 min

**Requirements:**
- Isolate sub-agent contexts (Claude Code subagent feature)
- Lead coordinates (Phase orchestration)
- Synthesis at end (Phase 6 vault sync)

### Pilot proposal

Routine v2 could add optional **parallel mode** (Phase 2+3 concurrent). User opts in when willing to pay 3-4× cost for 3-4× speed.

## 10. Common pitfalls

1. **Over-decomposition** — split 2-step task into 5 sub-agents = waste
2. **Dependency oversight** — sub-agent B starts before A done = works with stale data
3. **Shared sandbox collisions** — sub-agents write same file = race condition
4. **Cost surprise** — parallel = simultaneous LLM calls = bill shock
5. **Synthesis ignored** — lead ignores sub-agent outputs = wasted work
6. **Infinite spawning** — sub-agent spawns sub-agent spawns... = runaway
7. **Lost context** — sub-agent isolation = can't reference lead's full task context

## 11. When NOT to use sub-agents

- **Simple task** — single-agent sufficient
- **Strict sequential logic** — all steps dependent = no parallelism benefit
- **Latency-critical** — coordination overhead adds time
- **Budget-tight** — N× cost prohibitive
- **Debugging-first** — complex traces harder to follow
- **Real-time** — sub-agent spawning adds delay

## 12. Storm Bear vault relevance

**Sub-agent pattern is potential routine v2 feature.**

### Current routine constraint
Claude Code session = effectively 1 agent. Phases serial.

### Future routine với sub-agents
- Enable parallel source research (Phase 2)
- Enable parallel entity writing (Phase 3)
- **Velocity potentially 2× speed (v9 ~2h → ~1h)**

### Implementation path
- **Option 1:** Storm Bear routine stays in Claude Code, uses Claude Code's native subagent feature
- **Option 2:** Port routine to deer-flow, leverage deer-flow's fan-out pattern
- **Option 3:** Hybrid — Claude Code for interactive, deer-flow for long-batch

### Trade-off analysis
- Current routine ~2h + solid quality = acceptable
- Parallelism could be 2-3× faster = meaningful
- **Cost:** Parallel = 3-4× LLM spend
- **Complexity:** Harder to debug
- **Recommendation:** Low priority until routine v2 upgrade addresses other 26+ action items first

## 13. References / Nguồn

- Source: [[(C) README summary]] (sub-agent headline feature) + [[(C) Architecture + Contributing cluster summary]] (agents/ folder)
- Related entities:
  - [[(C) SuperAgent Harness Architecture]] (sub-agent = 1 of 5 components)
  - [[(C) Skill System (Progressive Loading)]] (sub-agents inherit skills)
  - [[(C) Message Gateway (Multi-Channel)]] (task submission origin)
- Sibling multi-agent implementations:
  - `../../get-shit-done - Beginner Analysis/02 Wiki/(C) 33 Specialized Agents + Commands.md`
  - `../../gstack - Beginner Analysis/02 Wiki/(C) Specialist Roles.md`
  - `../../ai-agents-for-beginners - Beginner Analysis/02 Wiki/(C) Multi-Agent Systems.md` (Lesson 08 concepts)
