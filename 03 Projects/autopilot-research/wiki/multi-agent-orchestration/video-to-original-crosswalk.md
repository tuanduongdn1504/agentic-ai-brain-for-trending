# Crosswalk — video patterns ↔ the original Anthropic sources

> **Source:** "Claude Architect: Multi-Agent Orchestration" (ExamPro, Andrew Brown, 2026-04-29, 2h9m) mapped against three Anthropic source documents: (1) "Building Effective Agents" (engineering blog), (2) "How we built our multi-agent research system" (engineering blog), (3) Claude Agent SDK documentation (official docs). Supplementary source: Claude Code sub-agents documentation. **ExamPro is a third-party course — NOT first-party Anthropic**; see [[multi-agent-orchestration/source-provenance]].

---

## Master Mapping Table

| Video term/section | Canonical Anthropic pattern | Original source(s) | What the video adds or changes |
|---|---|---|---|
| **Hub-and-spoke architecture** | Orchestrator-Workers pattern | "Building Effective Agents" + "Multi-agent research system" | Video emphasizes the **topology**: spokes never communicate directly; all communication routes through the coordinator only. Source describes the technical implementation (lead + subagents, separate contexts). Video adds: single choke point for observability + control. |
| **Coordinator role (decompose, delegate, aggregate, decide routing)** | Orchestrator delegation teaching: provide objectives, output format, tool guidance, clear boundaries | "Multi-agent research system" | Video shows the full **task lifecycle** (decomposition → delegation → aggregation). Source teaches HOW to teach delegation and scales (1 agent vs 10+). Video demonstrates the lifecycle loop concretely. |
| **Narrow task decomposition failure** (EV-market example) | Task description specificity — without detailed descriptions, agents duplicate work, leave gaps | "Multi-agent research system" | Video demonstrates the **gap-left-by-narrow-decomposition as a failure mode** via concrete example (missing charging infra, policy, sentiment, supply chain). Source abstracts it as a principle. Video's safeguards: decompose-time review + aggregate-time check. |
| **Dynamic selection** (route based on case, model generates routing on-the-fly) | Scale effort to complexity + wide-then-narrow strategy | "Multi-agent research system" | Video: model makes routing decisions at runtime (e.g., "non-traditional background → check transferable skills"). Source: scaling magnitude (1 vs 10+ agents) + evaluation-then-narrow. Both describe **conditional agent invocation**; video emphasizes dynamism. |
| **Partitioning research** (carve non-overlapping slices) | Separation of concerns through distinct tools + trajectories; subagent partitioning | "Multi-agent research system" | Video introduces **two-role separation**: PARTITION PLANNER (upstream routing rules) vs COORDINATOR (dumb executor). Source describes outcome (non-overlapping trajectories) without the architectural separation. Video adds: where-to-place routing logic. |
| **Refinement loop** (evaluate → identify gaps → re-run → iterate to MAX) | Evaluator-Optimizer pattern + end-state-vs-trajectory | "Building Effective Agents" + "Multi-agent research system" | Video shows **concrete loop structure**: initial run → evaluate_coverage tool → gap detection → targeted follow-up → repeat ≤MAX. Openly admits **coverage score went DOWN** (realism check). Source emphasizes accepting multiple valid paths + human judgment. |
| **Observability** (centralized coordinator sees every message, catches errors, controls context boundaries) | Observability: monitor decision patterns + interaction structures; stateful agents with error handling | "Multi-agent research system" | Video emphasizes **message flow visibility + error catching** as a coordinator responsibility. Source adds production patterns (rainbow deployments). Source's observability is production-focused; video's is debugging-focused. |
| **Coordinator refactoring** (modular code: prompts in files, tools separated, stateless classes, small functions, JSONL logs) | Stateful agents: durable execution with error handling + checkpointing | "Multi-agent research system" | Video focuses on **code organization for understandability** (developer experience). Source focuses on **durable execution with checkpointing** (production resilience). Non-overlapping concerns (dev-time vs prod-time) but both value engineer visibility/control. |
| **Agent SDK porting** (@tool decorator + internal MCP server + simplified tool dispatch) | Agent-computer interfaces (ACI): craft via tool documentation + testing | "Building Effective Agents" + Claude Agent SDK docs | Video shows **SDK implementation details**: @tool decorator removes manual JSON schemas; create_sdk_mcp_server bundles tools into in-process MCP. Source emphasizes thorough tool documentation. SDK docs confirm both: Client SDK (manual loop) vs Agent SDK (Claude handles tools autonomously). |
| **Sequential delegation** (task decomposition, pass results forward) | Prompt chaining: sequential steps with programmatic checkpoints | "Building Effective Agents" | Video shows coordinator breaking complex queries into subtasks, passing results forward linearly. Source defines the pattern formally. Direct alignment. |
| **Extended thinking as planning aid** | Extended thinking: controllable scratchpad for planning + assessing tools | "Multi-agent research system" | Video lists it as a principle; source explains its specific use (planning approach + tool assessment + complexity determination). Direct alignment; source is more detailed. |
| **Error handling + resilience** | Durably execute code with error handling; enable resumption from checkpoints | "Multi-agent research system" | Video shows weak initial error handling (no json.loads try-catch); adds structured logging + error handling in refactor. Source emphasizes checkpoint-based durability as a production pattern. Both value error resilience; source is more mature. |
| **Token economics** (4× agent vs chat, 15× multi-agent vs chat, token usage explains 80% variance, model tier > budget) | NOT discussed in video | "Multi-agent research system" | **Source-only content.** Video does not quantify token costs or discuss cost-performance tradeoffs. Source provides precise metrics + insight: model tier matters more than token budget for performance. |
| **Parallel tool calling** (subagents use 3+ tools simultaneously, 90% time speedup for complex queries) | Parallelization—Sectioning variant; parallel tool calling | "Multi-agent research system" + Claude Agent SDK docs ("Multiple subagents can run concurrently") | Video builds parallel subagent structure but doesn't measure speedup. Source quantifies: 90% time reduction via parallel tool calling. Video shows the pattern; source shows the ROI. |
| **Agent self-improvement** (Claude diagnoses failures + suggests prompt improvements; 40% task-time reduction) | NOT discussed in video | "Multi-agent research system" | **Source-only content.** Video doesn't mention agents improving their own prompts. Source demonstrates this capability with concrete 40% gain example (tool-testing agent). |
| **Evaluation rigor** (multi-dimensional LLM-as-judge + human validation) | LLM-as-judge rubric (factual accuracy, citation accuracy, completeness, source quality, tool efficiency, 0.0–1.0 scores); human evaluation catches automation edge cases | "Multi-agent research system" | Video shows one-shot coverage check + admits coverage actually went DOWN + "needs hours of real eval". Source describes production-rigor evaluation: multi-criteria + human oversight + edge-case detection (SEO-bias example). Source is the production version. |
| **"Just because it ran doesn't mean it's good"** (human judgment required, eval takes hours) | Agent design principle: maintain simplicity + transparency + require human oversight | "Building Effective Agents" | Video's pedagogical stance ("no magic here") maps to source's emphasis on simplicity + transparency. Honest that automation can't replace human judgment. |
| **When NOT to use agents** (start simple, workflows vs agents trade-off) | Core principle: simpler solutions like optimized single LLM + retrieval often suffice for many use cases | "Building Effective Agents" | Video demonstrates a workflow (job screener) with agent-like properties. Source emphasizes: agents suit open-ended problems; for predictable, bounded tasks, use workflows. Video doesn't explicitly cover this boundary. |

---

## (A) What the video gets RIGHT that the originals emphasize

**These are the points where the video demonstrates strong alignment with first-party Anthropic guidance:**

- **Hub-and-spoke topology as the primary pattern.** Video's explicit no-direct-spoke-communication rule matches both sources' orchestrator-worker emphasis. The isolation is load-bearing for observability and error handling.
- **Task decomposition as the first critical step.** Video devotes a full section to the narrow-decomposition pitfall. Source ("Multi-agent research system") emphasizes this same failure mode: "without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information."
- **Dynamic routing by case complexity.** Video's on-the-fly routing ("non-traditional background → check transferable skills") aligns with source's "scale effort to complexity" principle and wide-then-narrow exploration.
- **Coordinator as the observability choke point.** Video and source agree: centralized control enables consistent error handling, message visibility, and context-boundary management.
- **Refinement loops (evaluator-optimizer).** Video's concrete loop structure (evaluate → identify gaps → targeted follow-up → iterate) matches "Building Effective Agents" pattern naming and "Multi-agent research system" practice.
- **The honesty about evaluation.** Video says "is it good? unknown — needs hours of eval" and explicitly shows a coverage score going DOWN. This aligns with source's human-evaluation emphasis: "Human evaluation catches edge cases automation misses." Video rejects the vibe that automation solves everything.
- **Structured error handling as load-bearing.** Both video and source stress that error messages (not just retry loops) are high-ROI. Source: "invest in error recovery."

---

## (B) Where the video SIMPLIFIES or DIVERGES from the originals

**These represent the video's own design choices, elaborations, or pedagogical simplifications:**

- **"Partition Planner vs Coordinator" separation.** The video introduces this two-role architectural split to prevent routing logic from living in two places. Anthropic sources don't name this pattern. It's a sound harness-engineering move (following the separation-of-concerns principle) but video-author framing.

- **"Is it good? Unknown" honesty + single-pass coverage going DOWN.** The video explicitly runs refinement and *shows the coverage score decline*. This is a deliberate pedagogical choice ("no magic") that goes further than sources' neutral stance. Sources say evaluation is hard; video demonstrates *why* (non-deterministic improvement, reversal risk). This is a strengthen-the-critique choice by Andrew Brown, not original-source guidance.

- **MAX-STEPS cap for runaway-loop safety.** Video sets coordinator loop cap ~10 steps (2× expected ~5). Sources don't specify loop limits or recommend caps. This is a practical safety valve the video author added; it's good practice but not an original-source pattern.

- **Modular code structure for "human readability" as a load-bearing goal.** The refactoring section (prompts in files, tools separated, stateless classes, small functions) is framed as "technical ownership — you must know exactly what the code does." This is sound engineering but the emphasis on readability-over-abstraction is video-author voice. Sources value durability + observation; video adds: *understandability by the human steering it*.

- **"There are no rules here" (hybrid routing allowed).** Video states: "some coordinator-driven, some code-driven is fine." This is pragmatism not found in source guidance, which tends to prescribe patterns more formally. (Note: the related "don't fragment knowledge across agent boundaries" lesson is a *real* finding — but it comes from Omni's [[agentic-analytics-harness/_index|"Blobby" harness talk]], NOT this video. This video does not use the term "Blobotomy.")

---

## (C) What the originals cover that the video OMITS

**These are significant first-party Anthropic insights the video doesn't address:**

- **Token cost discipline (4×, 15×, 80% variance, model tier > budget).** Source ("Multi-agent research system") provides hard numbers: agents use ~4× more tokens than chat; multi-agent uses ~15× more; token usage explains 80% of performance variance. **Critical insight:** model upgrades (e.g., Sonnet 4) provide larger gains than doubling token budget. Video doesn't discuss cost at all. For production systems, this is material.

- **Parallel tool calling speedup quantified (up to 90%).** Source quantifies the parallelization ROI: "parallel tool calling cut research time by up to 90% for complex queries." Video shows the pattern (subagents in parallel) but doesn't measure or claim the speedup.

- **Agent self-improvement (failure diagnosis + prompt suggestions, 40% gain).** Source: "Claude 4 can diagnose failures and suggest prompt improvements; one tool-testing agent reduced task completion time by 40%." Video doesn't mention agents iterating their own prompts. This is a capability gap in the pedagogy.

- **Rainbow deployments for production (gradual traffic shift).** Source describes a production-specific pattern: "Gradually shift traffic between versions to avoid disrupting running agents." Video focuses on dev-time observability; source adds ops-time resilience.

- **Synchronous lead-agent bottleneck + asynchronous execution trade-offs.** Source: "Lead agents currently execute subagents synchronously; asynchronous execution could enable additional parallelism but adds coordination complexity." Video doesn't discuss this constraint or the coordination tradeoff.

- **When to use agents vs workflows (the bounded-task boundary).** Source ("Building Effective Agents") emphasizes: "Agents suit open-ended problems where step counts cannot be predicted and fixed paths cannot be hardcoded. Simpler solutions like optimized single LLM calls with retrieval often suffice for many use cases." Video builds an agent-like system but doesn't discuss the agents-vs-workflows trade-off.

- **Start simple as a discipline.** Source emphasizes: "Maintain simplicity in agent design" is a core principle. Video demonstrates a moderately complex system (3-4 spokes + evaluator + planner) but doesn't discuss *when* this complexity is justified. For a simple job screener, could a single well-prompted LLM suffice?

- **ACI (Agent-Computer Interface) rigor.** Source emphasizes: "Craft agent-computer interfaces via thorough tool documentation and testing." Video shows SDK tools briefly but doesn't deep-dive tool design rigor (schema quality, boundary clarity, error modes).

- **Evaluation dimensions (factual accuracy, citation accuracy, completeness, source quality, tool efficiency).** Source provides a multi-dimensional rubric. Video shows one-dimensional coverage scoring.

- **Structured Outputs for enforcing response shape.** Source doesn't mention structured outputs explicitly in the "Multi-agent research system" article, but "Building Effective Agents" and Agent SDK docs emphasize JSON Schema enforcement as a tool-design lever. Video doesn't cover this.

---

## (D) Video pedagogical gaps (not source omissions — inherent to the format)

**Context the video couldn't include due to format / scope / time:**

- **No production dataset.** Video is pedagogical with a toy job-screener use case. Source ("Multi-agent research system") is backed by internal Anthropic research eval with real performance deltas (90.2% improvement). The video explicitly flags: "no real eval, needs hours."

- **No code examples beyond the demo.** The video builds live (Haiku → Sonnet iterations) but doesn't publish the final code. Source papers and SDK docs include runnable examples.

- **No observability integration depth.** Video mentions OpenTelemetry as a future layer (containers + instrumentation). Source assumes observability is already in place; video is learning from a starting point with "only print statements."

- **No multi-model coordination.** Video hints (Andrew muses "coordinator could route to different models") but doesn't build it. Source doesn't address multi-model either. SDK docs show single-model examples.

---

## Key Takeaways

- **Hub-and-spoke is the right foundation.** Both video and sources agree: central coordinator + isolated subagents + communication through coordinator only is the pattern that enables observability + error handling + controlled context boundaries.

- **Task decomposition is the highest-leverage step.** Narrow decomposition that misses scopes (video's EV-market example) leaves gaps that refinement loops can't fully fill. Get decomposition right first.

- **Dynamic routing by complexity beats hard-coded paths.** Let the model decide (with guidance) which agents to invoke based on the input case. This is more resilient than static decomposition.

- **Evaluation rigor is non-negotiable for production.** Video's "coverage score went DOWN" and "needs hours of eval" is honest. Source backs this up with multi-dimensional rubrics + human validation. Don't ship without measurement.

- **Observability is load-bearing, not a nice-to-have.** Both video and sources emphasize: centralized logging, error catching, message visibility, decision tracking. This is how you diagnose failures at scale.

- **Token cost and model tier matter more than prompt magic.** Source quantifies: token usage explains 80% of performance variance; model upgrades beat doubling budget. Video skips this entirely; for production, it's critical.

- **Simplicity is a discipline, not a default.** Source's core principle: "maintain simplicity in agent design." The video builds a moderately complex system for pedagogy; when does complexity become justified?

- **Code readability as engineer stewardship.** Video's refactoring emphasis (modular, self-documenting structure, stateless classes, small functions) goes beyond source's durability focus. Both are right: durability + readability = ownership.

- **Agent self-improvement is possible but underexplored in pedagogy.** Source mentions it (40% task-time reduction example); video doesn't. This capability deserves more attention in teaching.

- **Anthropic's original sources are complementary, not redundant.** "Building Effective Agents" is the pattern dictionary. "Multi-agent research system" is the production playbook. SDK docs are the implementation reference. Video synthesizes all three into a coherent pedagogical arc. Start with video for intuition, then read sources for depth.
