# Task decomposition, dynamic selection & research partitioning

> **Source:** ExamPro "Claude Architect: Multi-Agent Orchestration" (Andrew Brown, 2026-04-29, 2h9m); sections 4–6. Cross-references: [[multi-agent-orchestration/multi-agent-research-system-deep-dive]], Anthropic "Building Effective Agents", Anthropic "How we built our multi-agent research system". **Venue note:** pedagogical demo (job-application screener case study) built LIVE in Python (Anthropic SDK then Claude Agent SDK); explicit caveats on eval ("needs hours of real data").

## Narrow task decomposition — the EV-market example (why decompose-time specificity matters)

- **The failure case:** "Give me a comprehensive EV market analysis" decomposes into only sales volume, battery tech, and manufacturers — each sub-agent sees ONLY its own isolated context window, so none can flag what's missing.
- **Silent gaps:** each agent executes independently and returns to the coordinator. No inter-agent **direct** communication, and each spoke is **fully context-isolated** (it sees only its own slice) — which is exactly why none of them can flag what's missing. Result: missing charging infrastructure, policy/subsidies, second-hand market, consumer sentiment, supply chains (lithium/cobalt sourcing), grid capacity. The coordinator never knows gaps exist.
- **Why it happens:** a narrow decomposition **looks complete on the surface.** No agent throws an error. No agent says "wait, that's incomplete." The system just... ships silence.

### The fix (two safeguards)

1. **Decompose-time review tool:** before delegating subtasks, ask the coordinator explicitly "What information is needed to answer this?" and have it **add subtasks to cover identified gaps.** This forces specificity at decompose-time, not at aggregate-time.
   - Pragmatic: this may balloon task count, but narrowness is worse (silent gaps vs explicit overreach).

2. **Aggregate-time coverage check:** before finalizing the response, ask "Before writing the answer, did you cover X, Y, Z?" (each being a critical information category for the domain). Blocks submission until coverage is confirmed.

- **Video author's realization:** for the job-application screener case (a simpler domain), the "better decomposition" turned out to **collapse the three originally hard-coded screening spokes (keyword scanner, deep evaluator, red-flag detector) into ONE screening agent contextualized N ways** — i.e. the coordinator *generates* the specialized screening angles instead of routing to three fixed agents. (The score aggregator stayed a distinct step.) The lesson: **decomposition-narrowness is more dangerous than decomposition-redundancy** — being too specific costs a few extra tokens; being too narrow silently drops whole dimensions. Source: Anthropic "How we built our multi-agent research system" confirms — *"without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information."*

## Dynamic selection — route by case, never invoke an agent unless answering a real question

- **Static pipeline fallacy:** run the same agents for every query (wastes tokens).
- **Dynamic fix:** tell the coordinator to **route based on the case.** Provide it with routing options to consider under conditions:
  - "If non-traditional background → check transferable skills"
  - "If strong match → skip keyword scan"
  - "If red flags detected → escalate to deep evaluator"
- **Model generates routing on the fly:** the model decides which agents are necessary *per query,* not per hardcoded path.
- **Optional routing-quality tool:** can add a separate validation step to check routing quality (e.g., "did we choose the right agents?"). Hybrid code-driven + model-driven routing is fine — *"there are no rules here"* (video author's phrase).

### Why it matters

- Tokens are expensive. Running all agents on every query multiplies cost unnecessarily.
- Source (Anthropic multi-agent research blog): agents use ~4× more tokens than chat; multi-agent uses ~15× more. Token usage explains 80% of performance variance.
- **Scaling to complexity rule:** simple fact-finding needs 1 agent with 3–10 calls; complex research needs 10+ subagents with divided responsibilities. Dynamic routing is how you **scale the agent count to the problem.**

## Research partitioning — carve non-overlapping scope slices to prevent duplicate work

- **The waste case:** three research agents given the same brief produce three overlapping answers covering the same ground.
- **The partition fix:** generate a JSON partition structure (agent + scope + cover + exclude) that **carves the problem into non-overlapping slices.**
  - Example: resume screening for three aspects (technical fit, cultural alignment, growth potential), each with its own agent, each with explicit exclusion boundaries.

### Partition planner vs. coordinator separation (two roles, not one)

- **Partition Planner:** sees the input (e.g., job posting + resume), owns the **routing RULES** (which partitions exist and who does what), **decides which partitions to create.** Static (code-driven) or generated (model-driven). **This agent decides the scope structure.**
- **Coordinator:** now becomes a **"dumb" executor**: invoke exactly one screening call **per partition**, aggregate results, don't invent extra angles — the decision was already made upstream.
- **Why the split matters:** putting routing logic in BOTH planner and coordinator = two places fighting over the same decisions. Conflicts, duplication, confusion.

**Source alignment:** Anthropic's "Building Effective Agents" calls this pattern **Orchestrator-Workers** (central agent decomposes, delegates, synthesizes). The partition-planner-vs-coordinator split is **the video's own structural refinement** of that pattern (not an Anthropic-named variant): move the "decompose" step **upstream and apart** from the "execute" step.

## Refinement loop (evaluator-optimizer pattern) — when one pass isn't enough

- **Initial pass:** run partitions or initial agent calls.
- **Coverage evaluation:** call an evaluate_coverage tool that checks: "Did we cover the key dimensions?" (factual accuracy, completeness, source quality per Anthropic's LLM-as-judge rubric).
- **Gap detection:** if coverage insufficient, the evaluator identifies which partitions or angles are incomplete.
- **Targeted follow-up:** invoke additional agents to fill ONLY the identified gaps (not re-run everything).
- **Iterate up to MAX:** repeat 3–4 times, then force a submit_final gate (no more iterations).

### Honest caveat from the video

- Coverage score **actually went DOWN across iterations** in the demo. Andrew Brown's explicit commentary: "Is it good? Unknown — needs hours of real eval on actual data." The refinement loop is a **pattern, not a magic bullet.**
- Lesson: iterate and measure, but don't assume iteration improves outcomes without evidence.

## Key Takeaways

- **Decompose with explicit specificity:** use a decompose-time review tool to identify information gaps before delegating. Aggregate-time coverage checks block incomplete responses.
- **Never invoke an agent unless it answers a real question:** dynamic routing by case (model decides which agents to run) saves tokens; scale agent count to problem complexity, not to hardcoded pipeline.
- **Partition for non-overlapping scope:** carve research tasks into distinct slices (agent + scope + cover + exclude in JSON structure) to prevent duplication. Partition planner upstream; coordinator as executor downstream.
- **Planner-coordinator separation prevents conflicts:** don't put routing logic in both; one decides structure, the other executes it.
- **Evaluator-optimizer requires measurement:** refinement loops (evaluate → fill gaps → iterate) work, but only if you measure against real data. Iteration ≠ improvement without evidence.
- **Hub-and-spoke bottleneck is a feature:** centralized coordinator controls context injection, error handling, and observability — the single choke point prevents inter-agent miscommunication.