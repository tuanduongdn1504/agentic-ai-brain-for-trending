# (C) Context Rot Solution

> **Source:** README.md (lines 1-60, 473-556), `hooks/gsd-context-monitor.js`
> **Ingested:** 2026-04-18
> **Type:** Entity page (core concept) — building block #1 cho GSD

---

## One-liner

**VI:** **"Context rot"** là term đặc trưng của GSD — quality degradation khi Claude's context window fill up. GSD's solution = **4-mechanism stack**: (1) file-structured context engineering với size budgets; (2) XML prompt formatting precision; (3) fresh 200k context per subagent execution; (4) `gsd-context-monitor` hook runtime detection. **Unique problem framing** vs 3 sibling Tier 1 frameworks (ECC/Superpowers/gstack).

**EN:** "Context rot" is GSD's distinctive term — quality degradation as Claude's context fills. Solved via 4 mechanisms: file-structured context engineering, XML prompts, fresh 200k per subagent, runtime monitoring hook. Unique framing vs siblings.

---

## Khi nào dùng concept này

**Hữu ích khi:**
- Hiểu vì sao GSD workflow tồn tại (context rot = problem)
- Debug why Claude's output degrades mid-session
- Compare với siblings' implicit context management
- Design own agent framework cho long-running workflows

**Không cần dùng GSD cơ bản** — system handle transparent.

---

## Comparison sibling: context management across Tier 1

| Framework | Context management approach | Problem framing |
|-----------|-----------------------------|-----------------|
| **ECC** | Skill-based ad-hoc via hooks + continuous-learning-v2 | "Production-ready agent" (generic) |
| **Superpowers** | SDD subagent isolation + context-isolation principle (v5.0.2) | "Context window pollution" (addressed in v5.0.2) |
| **gstack** | Conductor parallel sessions + `/learn` cross-session | "Agent has eyes" (tool focus) |
| **GSD** | **"Context rot" named problem** + 4-mechanism stack | **"Quality degradation as context fills"** (specific) |

→ **GSD most explicit.** Others handle context implicitly; GSD names it as core problem.

---

## Sub-types: 4 mechanisms

### 1. File-structured context engineering

Persistent files trong `.planning/` với **size budgets** based on Claude quality degradation:

| File | Purpose | Size focus |
|------|---------|-----------|
| `PROJECT.md` | Vision | Small, always loaded |
| `research/*.md` | Ecosystem knowledge | Scoped per topic |
| `REQUIREMENTS.md` | v1/v2 scoped | Phase-traceable |
| `ROADMAP.md` | Phases | Overview |
| `STATE.md` | Decisions, blockers, memory | Cross-session |
| `PLAN.md` | Atomic task | XML structured |
| `SUMMARY.md` | What happened | Post-execution |

→ "Size limits based on where Claude's quality degrades. Stay under, get consistent excellence."

### 2. XML prompt formatting

Each plan = structured XML optimized for Claude:

```xml
<task type="auto">
  <name>Create login endpoint</name>
  <files>src/app/api/auth/login/route.ts</files>
  <action>
    Use jose for JWT (not jsonwebtoken - CommonJS issues).
    Validate credentials against users table.
    Return httpOnly cookie on success.
  </action>
  <verify>curl -X POST localhost:3000/api/auth/login returns 200 + Set-Cookie</verify>
  <done>Valid credentials return cookie, invalid return 401</done>
</task>
```

**Why XML:**
- Section markers explicit
- Nested structure parseable
- Verification step inline (not afterthought)
- `type="auto"` attribute signals automation mode

→ **Distinctive vs siblings** (ECC/Superpowers/gstack use markdown templates).

### 3. Fresh 200k context per subagent

**Thin orchestrator pattern:**
- Main session = orchestrator (workflow files)
- Orchestrator spawns agents với fresh 200k context windows
- Agent does heavy lifting
- Orchestrator integrates results back

**Key metric:** "Your main context window stays at 30-40%. Work happens in fresh subagent contexts."

→ **Match Superpowers SDD + gstack Conductor.** Same mechanism, different naming.

### 4. `gsd-context-monitor` hook

Runtime detection via `hooks/gsd-context-monitor.js`:
- Tracks current context utilization
- Alerts when approaching threshold (not source-verified, inferred)
- Likely integrates với `gsd-phase-boundary.sh` to trigger session resets

→ **Runtime guard** vs static planning. Siblings have similar hooks (Superpowers context-isolation v5.0.2) but GSD makes it named-feature.

---

## Anatomy: How context rot accumulates (the problem)

Without GSD:
```
Session starts
  ↓
Claude reads 50k of context
  ↓
User asks question, Claude responds (adds 5k to context)
  ↓
Claude reads file (adds 10k)
  ↓
Tool calls + results (adds 20k)
  ↓
[...10 iterations later]
  ↓
Context at 180k / 200k
  ↓
Claude says "I'll be more concise now" ← degradation starts
  ↓
Claude forgets earlier constraints ← rot accelerates
  ↓
Final output = inconsistent garbage
```

### With GSD (prevention)

```
Session starts
  ↓
Orchestrator reads .planning/STATE.md (small, 2k)
  ↓
Orchestrator decides: spawn executor for task
  ↓
Executor spawns with fresh 200k
  ↓
Executor reads PLAN.md (XML, 3k)
  ↓
Executor does work (uses 30k max)
  ↓
Executor writes SUMMARY.md
  ↓
Executor terminates — context freed
  ↓
Orchestrator reads SUMMARY.md back
  ↓
Main context still at 30-40% usage
```

→ **Orchestrator never fills up.** Rot prevented structurally.

---

## Cơ chế

### Mechanism 1: Size-awareness at file level

`.planning/` files có implicit budgets. Agent trained to respect limits. If file grows too large, system prompts chunking.

### Mechanism 2: Subagent fresh context

Fresh context per subagent = isolated work. When subagent done, context discarded. No accumulation.

### Mechanism 3: Wave execution (parallel)

Multiple subagents parallel = parallel clean contexts. None leak into each other.

### Mechanism 4: State persistence via files

`STATE.md` preserves decisions across sessions **without filling current context.** Sessions restart fresh, reload minimum.

### Mechanism 5: Agent size-budget enforcement (v1.37.0)

Per CHANGELOG:
> "Tiered line-count limits (XL: 1 600, Large: 1 000, Default: 500) keep agent prompts lean; violations surface in CI"

→ **Prompt-level size guards** enforce at dev time. Not just runtime.

### Mechanism 6: Shared boilerplate extraction (v1.37.0)

> "Mandatory-initial-read and project-skills-discovery logic extracted to reference files, reducing duplication across a dozen agents"

→ Prompts import shared refs instead of duplicating → smaller per-agent prompts.

---

## Out-of-box behavior

**Default GSD install:**
- Context monitor hook active
- `.planning/` structure created on first `/gsd-new-project`
- Agents use XML plans by default
- Fresh context per execution automatic

**User doesn't configure anything.** Context management transparent.

---

## Configuration knobs

| Knob | Default | Effect |
|------|---------|--------|
| `hooks/gsd-context-monitor.js` | enabled | Disable via remove from hooks config |
| Agent size budgets (XL/Large/Default) | CI-enforced | `.gsdrc` or config override (inferred) |
| `.planning/` file size limits | implicit | Soft limits, not hard |
| Fresh-context-per-subagent | always | Architectural, not knob |

---

## Recipes

### Recipe 1: Debug "quality dropped mid-session"

Per GSD philosophy:
1. Check `.planning/STATE.md` — is it current?
2. Run `/gsd-health` — check `.planning/` integrity
3. Run `/gsd-next` — auto-detects state and runs next step
4. If still degraded: `/gsd-pause-work` → new session → `/gsd-resume-work`

### Recipe 2: Session recovery from context overflow

```bash
/gsd-pause-work   # Creates HANDOFF.json
# Restart Claude Code
/gsd-resume-work  # Restores from last session, fresh context
```

→ **Explicit recovery path** vs "just restart and hope."

### Recipe 3: Audit context for stale info

```bash
/gsd-session-report   # Summarize current session
/gsd-forensics        # If workflow stuck, diagnose
```

→ **Introspection built-in.** Not just debug print.

### Recipe 4: Minimize context rot in custom agents

Follow v1.37.0 size budgets:
- Agent prompts ≤ 500 lines (Default)
- Large agents ≤ 1000 lines (must justify)
- XL agents ≤ 1600 lines (exceptional)

Extract shared boilerplate to `references/` files.

---

## Advanced patterns

### Pattern 1: Named problem as positioning

GSD's most distinctive move = **naming the problem** ("context rot"). Siblings imply context issues; GSD makes it explicit.

→ **Marketing insight:** Specific problem framing > generic value proposition. Storm Bear could adopt ("Solves __" framing per project).

### Pattern 2: Orchestrator-as-router, not worker

Orchestrator's job = spawn + route. **Never do heavy work.** Work = subagent responsibility.

→ **Match thin-controller pattern** từ MVC/web frameworks. Applied to AI agent orchestration.

### Pattern 3: State via files, not session memory

`STATE.md` = persistent state. Session = ephemeral. Decouples durability từ session lifetime.

→ **Match Redux store pattern** in frontend. State store separate từ rendering.

### Pattern 4: 3-tier agent size budget

XL/Large/Default tiers. Justification required for upgrades. **Forces intentionality.**

→ Reusable cho Storm Bear: wiki entity pages could have tier (Overview/Standard/Deep), budgets enforced.

### Pattern 5: Size-budget CI enforcement

Violations surface in CI. Not just runtime warnings.

→ **Shift-left discipline.** Catch prompt-rot before ship.

---

## Combination với building blocks khác

### + 5-Step Workflow
Workflow designed around context rot prevention. Each step = fresh subagent + file I/O, không accumulate in main.

### + 33 Specialized Agents
Each agent has own size budget. Tiered enforcement.

### + 14 Harnesses
Context rot problem exists across all harnesses. GSD's mechanisms (file structure + XML + fresh subagents) work cross-harness.

### + Hooks System
`gsd-context-monitor.js` runtime guard. Other hooks (prompt-guard, workflow-guard) add protection layers.

### Cross-project: + Superpowers context-isolation
Convergent concept. Superpowers's v5.0.2 release added "All delegation skills include context isolation principle." Same intent, different mechanism (skill-level vs framework-level).

### Cross-project: + goclaw PruneStage
goclaw's V3 pipeline PruneStage = runtime context trimming (soft/hard). GSD = structural prevention. Different tier (runtime vs architectural).

### Cross-project: + Storm Bear vault
Storm Bear's wiki pattern = external "persistent state" similar to `.planning/STATE.md`. Both preserve knowledge beyond session.

---

## Anti-patterns

❌ **Ignore size budgets** — "My agent needs 3000 lines" = red flag. Extract shared refs first.

❌ **Stuff everything into orchestrator context** — orchestrator is router, not worker. Move logic to subagents.

❌ **Disable context-monitor hook** — it's your canary. Keep it.

❌ **Chain contexts manually** — if long session, use `/gsd-pause-work` → `/gsd-resume-work` instead of forcing through.

❌ **Treat context rot as runtime-only** — it's also architectural. Size budgets = dev-time fix.

❌ **Name feature "better context management"** — ambiguous. GSD names "context rot solution." Specificity > generality.

---

## Cross-references

- [[(C) 5-Step Workflow]] — operationalizes context rot prevention
- [[(C) 33 Specialized Agents + Commands]]
- [[(C) 14-Harness npm Distribution]]
- [[(C) README summary]]
- [[(C) USER-GUIDE summary]]
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) Subagent-Driven Development.md` — context isolation analog
- Cross-project: `../../goclaw - Beginner Analysis/02 Wiki/(C) 8-Stage Agent Pipeline.md` — PruneStage analog

## Citations

- README.md line 9 (core problem statement: "Solves context rot...")
- README.md lines 473-555 (Why It Works section — 4 mechanisms)
- README.md v1.37.0 Highlights (size budgets)
- `hooks/gsd-context-monitor.js` (filename — implementation not source-verified)
- CHANGELOG.md v1.37.0 entry (size budget + boilerplate extraction)

## TODO

- ⏸ Source-verify `gsd-context-monitor.js` implementation
- ⏸ Document exact XL/Large/Default budgets enforcement mechanism
- ⏸ Compare XML prompt format vs Superpowers's markdown template performance
- ⏸ Measure: does GSD demonstrably reduce context rot vs baseline?
