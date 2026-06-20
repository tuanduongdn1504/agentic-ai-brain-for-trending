# Original resource #2 — Anthropic "How we built our multi-agent research system"

> **Source:** Anthropic Engineering Blog — "How we built our multi-agent research system" (https://www.anthropic.com/engineering/multi-agent-research-system), cross-walked against the video in [[multi-agent-orchestration/overview]] (Andrew Brown / ExamPro, 2026-04-29). Stats here are from the **Anthropic blog**, not the video.

## System Architecture

**Lead-agent + parallel-subagent topology.**
- Lead agent (Claude Opus 4) analyzes incoming queries, spawns parallel subagents (Claude Sonnet 4), each with **separate isolated context windows**.
- Subagents explore different aspects of the research task **simultaneously**, returning findings to the lead for synthesis.
- **No direct subagent-to-subagent communication**: all results flow back through the lead (hub-and-spoke pattern).
- Separation of concerns materializes through: distinct tool sets per subagent, independent exploration trajectories, parallel information compression across multiple context windows.

## Performance: The 90.2% Improvement

| Metric | Result |
|--------|--------|
| **Single-agent baseline** | Claude Opus 4 (one context window) |
| **Multi-agent system** | Claude Opus 4 (lead) + Claude Sonnet 4 (subagents, parallel) |
| **Improvement** | **90.2% on Anthropic's internal research eval** (source: "multi-agent system with Opus 4 lead + Sonnet 4 subagents outperformed single-agent Opus 4 by 90.2%"). The video does NOT cite this number — it's from the original blog. |

**Token-economics explain performance variance:**
- Agents use ~**4× more tokens** than chat interactions (single LLM call).
- Multi-agent systems use ~**15× more tokens** than chats.
- **Token usage alone explains 80% of performance variance** in the BrowseComp internal evaluation.
- Corollary: model tier upgrades (e.g., Sonnet 4) provide **larger gains than doubling token budget**.
- Three factors collectively explain **95% of the performance variance** (specific factors not named in source digest; inferred to be: model tier, token budget, orchestration clarity).

**FLAG:** "90.2% improvement" and the three-factor claim (95% variance) appear once in source; no breakdown of which three factors or statistical detail provided in digest.

## Prompt Engineering Principles

**Teach the orchestrator to delegate effectively.**
- **Provide objectives:** each subagent receives specific research tasks with distinct purposes.
- **Output format:** specify how subagent findings should be structured for lead-agent synthesis.
- **Tool guidance:** document which tools are available and when to use them.
- **Clear boundaries:** prevent duplication by explicitly marking what each subagent covers and what it explicitly excludes.
- Without detailed task descriptions, agents **duplicate work, leave gaps, or fail to find necessary information** — observed in early system where three cryptocurrency subagents and supply-chain subagents overlapped until refined descriptions improved division of labor.

**Scale effort to query complexity.**
- Simple fact-finding: 1 agent with 3–10 tool calls.
- Complex research: 10+ subagents with divided responsibilities and non-overlapping scopes.
- Dynamic selection: assess query complexity upfront and route accordingly; don't invoke a subagent unless it answers a real question.

**Breadth-first then narrow (wide-then-narrow strategy).**
- Start with broad queries to evaluate the research landscape.
- Progressively narrow focus based on initial findings.
- Reduces path dependency: parallel exploration prevents dead-end tunneling that a single agent might pursue.

**Extended thinking as a controllable scratchpad.**
- Use extended thinking for planning approach (how will the subagent tackle this?).
- Use for assessing available tools and determining task complexity.
- This guides reasoning without forcing a fixed step sequence.

**Parallel tool calling (3+ tools simultaneously per subagent).**
- Reduced research time by **up to 90%** for complex queries (source: Anthropic engineering blog).
- Spades don't wait for one tool result before invoking the next; they batch.

**Teach agents to diagnose and improve themselves.**
- Claude can suggest prompt improvements when task completion fails.
- In production, one tool-testing agent **reduced future task completion time by 40%** through iterative prompt refinement.

## Evaluation: The Multi-Dimensional Rubric

**LLM-as-judge (automated scoring):**
- **Factual accuracy** (0.0–1.0 scale + pass/fail): did the findings match verifiable facts?
- **Citation accuracy** (0.0–1.0 scale + pass/fail): are sources correctly attributed and traceable?
- **Completeness** (0.0–1.0 scale + pass/fail): did the research cover all aspects of the query?
- **Source quality** (0.0–1.0 scale + pass/fail): were authoritative sources prioritized?
- **Tool efficiency** (0.0–1.0 scale + pass/fail): did the subagent use an appropriate mix of tools, or was it wasteful?

**Human evaluation (catch edge cases automation misses):**
- Identified **bias toward SEO-optimized content** over genuinely authoritative sources (e.g., content farms ranking above academic/institutional sources).
- Detected gaps in coverage that LLM-as-judge missed.
- Focus on **end-state outcomes** rather than prescribed step sequences: agents may find alternative valid paths to correct answers.

## Production Engineering Patterns

**Stateful agents with durable execution.**
- Code execution persists across checkpoints; subagents can resume from failure points rather than restart.
- Error handling and graceful degradation embedded: if one subagent fails, others continue and results are synthesized from partial data.

**Observability as a choke point.**
- Centralized lead agent is a single observation point: every message, every tool invocation, every context boundary crossing is visible.
- Monitor decision patterns (which queries trigger which subagent sets?) and interaction structures (how deep does the orchestration tree get?).
- Monitoring does not access conversation contents (privacy-preserved); focuses on **topology and decision frequency**.

**Rainbow deployments.**
- Gradually shift traffic from one system version to another.
- Avoid disrupting long-running research tasks mid-flight by abruptly switching logic.

**Synchronous subagent execution (current); asynchronous is future.**
- Lead agent currently invokes subagents one at a time **synchronously** (waits for each to return before invoking the next).
- Parallel execution achieved by running **independent subagents concurrently** at the start, not by sequential invocation.
- Full asynchronous execution at the lead level could enable additional concurrency but adds coordination complexity (would require centralized result-collection orchestration).

## Crosswalk: Research-System Concepts to Anthropic API Terminology

| Research System Concept | Anthropic Pattern | Video (ExamPro, Andrew Brown) |
|---|---|---|
| Lead agent + parallel subagents, separate contexts | Orchestrator-Workers | Hub-and-spoke architecture (coordinator owns routing, context injection, aggregation; spokes never talk directly) |
| Task decomposition by lead | Dynamic task decomposition + Orchestrator-Workers | Task lifecycle: decompose → delegate → aggregate; coordinator assesses complexity and routes |
| Distinct non-overlapping scopes per subagent | Parallelization—Sectioning variant | Partition planning: static or generated scope-carving to prevent overlapping research |
| Refinement loop: initial run → evaluate → fill gaps → iterate | Evaluator-Optimizer | Coverage evaluation tool; gap detection; targeted follow-up to MAX 3–4 iterations |
| Specific task descriptions (objectives, format, boundaries) | Prompt engineering + Orchestrator-Workers | Teach delegation explicitly; coordinator specifies what subagent owns vs excludes |
| Each subagent receives query context only as lead injects it | Context isolation | Subagent receives only: task description from lead, specific tools, no conversation history |
| Three factors explain 95% variance; model tier > budget | Token economics + model selection | Video pedagogical; source emphasizes model tier as high-impact lever |
| LLM-as-judge + human eval | Evaluation pattern | Video: coverage evaluation tool + human judgment; "real evaluation takes hours" |

**NOTE:** Video disclaimer—"just because it ran doesn't mean it's good" — the ExamPro video built the patterns pedagogically with intentional gaps (weak observability, no persistent spoke outputs, single-pass gaps). Source article reflects production version with rigorous evaluation discipline.

## Token Economics Summary

**When to expect cost vs. benefit tradeoff:**
- 15× token multiplier vs chat means multi-agent is **expensive**.
- Viable for high-complexity research where breadth is necessary (open-ended exploration, synthesis across domains).
- Not viable for simple fact lookups (use single agent + retrieval).
- Model tier choice (Opus vs Sonnet) matters more than token budget for performance; invest in better model first.

## Production Reliability: Key Moves

1. **Clear subagent task descriptions:** prevents duplication, reduces wasted effort.
2. **Non-overlapping partition planning:** upstream routing decision logic separates from downstream coordinator execution.
3. **Refinement loops with coverage checks:** initial run is rarely sufficient; iterate up to MAX iterations (3–4) to close gaps.
4. **Stateful execution + checkpointing:** resumable from mid-flight failures.
5. **Centralized observability:** lead agent as single log point; monitor topology and decision frequency without accessing conversation contents.
6. **Human eval as final gate:** LLM-as-judge catches mechanical errors; humans catch bias and intent mismatches.

## Key Takeaways

- **Hub-and-spoke with clear delegation teaches the model how to orchestrate:** subagents need specific objectives, output format, tool guidance, and scope boundaries. Vague delegation = duplication and gaps.
- **Token economics explain 80% of why multi-agent works:** it's not magic; more tokens + more context windows + parallel exploration = higher coverage. Match token budget to query complexity (1 agent ≤3–10 calls for simple; 10+ subagents for complex).
- **Model tier >> token budget for performance:** upgrading from Sonnet to Opus provides larger gains than 2× token budget; allocate investment accordingly.
- **Parallel tool calling + breadth-first exploration cut research time by up to 90%:** don't make subagents wait for one tool result; batch invocations and explore multiple directions simultaneously.
- **Refinement loops with coverage gaps are expected:** initial run catches ~60–70% of necessary research; iterate up to MAX (3–4) rounds to fill identified gaps. Accept that some iterations may yield lower scores initially (coverage consolidation, not decline).
- **End-state evaluation over prescribed steps:** focus on final answer quality (factuality, completeness, source authority) rather than forcing agents to follow a predetermined decomposition. Agents find valid alternative paths.
- **Observability as topology + decision patterns, not conversation access:** centralized lead agent enables audit of which queries trigger which subagent sets and how deep orchestration trees go, without privacy violations.
- **Scalability requires stateful + durable execution:** checkpoint-resumption at each subagent avoids full restart on failure; enables long-running research across time and load changes (rainbow deployments).