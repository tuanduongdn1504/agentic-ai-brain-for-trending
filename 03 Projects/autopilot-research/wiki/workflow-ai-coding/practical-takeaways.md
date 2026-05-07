# Practical Takeaways — 10 adoptable rules

Synthesized across the 6 speakers. Each rule is attributable; ordering is mine, biased toward "do this first if you're starting today."

## Quick-adopt list (do this in week 1)

### 1. Run a "Grill Me" alignment phase before any nontrivial work
Force the AI to interview you relentlessly about every aspect of your plan until you reach a shared design concept. Prevents misalignment during execution. *(Pocock)*

> Concretely: use a `grill-me.md` skill or system prompt that says "act as a skeptical adversary; interview me; do not propose solutions until I confirm understanding."

### 2. Maintain `claude.md` / `agents.md` per project
Persistent agent memory: tech stack, coding conventions, dos and don'ts, lessons learned. Update it whenever the AI repeats a mistake. *(Pocock, Boris, Anthropic)*

### 3. Implement test-driven development for every agent task
Require agents to write a failing test first, then make it pass. Forces small deliberate steps. Universal advocacy across speakers. *(Pocock, Lopopolo, others)*

### 4. Adopt skills over custom agents
Instead of building a domain-specific agent for every workflow, create skill folders (markdown + scripts) that a general-purpose agent loads at runtime. *(Zhang & Murag, Anthropic)*

> See [[../claude-code-hooks/_index|Claude Code hooks]] for the complementary deterministic-event layer.

## Architectural rules (do this in month 1)

### 5. Restructure toward "deep modules"
Hide complex logic behind simple interfaces. Agents navigate, test, and refactor deep modules far more reliably than shallow tightly-coupled module trees. *(Pocock)*

### 6. Use "tracer bullets" / vertical slices
Force agents to work in slices that touch every layer (DB → API → UI) in a single task. Integrated feedback from minute one beats horizontal "all DB then all UI" decomposition. *(multiple)*

### 7. Decompose features into atomic user stories
Small tasks with verifiable acceptance criteria. Lets autonomous agents complete and self-verify without your supervision. *(Carson, Pocock, Isenberg)*

## Workflow rules (do this when running production loops)

### 8. Manage the "dumb zone" by clearing context
Avoid performance degradation in long conversations: clear the context window frequently to return the model to its sharp zone near the system prompt. *(Pocock)*

> Note: Lopopolo disagrees — see [[expert-disagreements]] § 5. If your model has good autocompaction, trust it.

### 9. Automate review with reviewer-agent personas
Deploy specialized reviewer agents in CI/CD: security expert, reliability expert, accessibility reviewer. Each catches a different class of slop before merge. *(Lopopolo, OpenAI)*

### 10. Embrace harness engineering — your job is steering
Shift primary role from writing code to designing the harness (prompts, guardrails, tests) that lets autonomous agents execute the full job while you steer strategy and review outcomes. *(Lopopolo)*

## Anti-patterns to avoid

The speakers explicitly warn against:

- **"Specs-to-code" with no code reading** *(Pocock)* — abandoning the codebase is "vibe coding". You lose the battleground.
- **Compacting context naively** *(Pocock)* — sediment strains attention.
- **Building per-domain agents** *(Zhang & Murag)* — fragments the skill library; doesn't scale.
- **Approving AI-generated plans without reading them** *(Lopopolo)* — encodes instructions you didn't intend.
- **Long individual sessions in the dumb zone** *(multiple)* — quality drops; costs rise; nobody benefits.

## Ranking by ROI

If you can only adopt 3 things this month:

1. **Rule #1 (Grill Me)** — pays back on every nontrivial task.
2. **Rule #2 (`claude.md`)** — pays back forever; cumulative.
3. **Rule #3 (TDD)** — pays back on every commit; gates quality.

Rule #4 (skills) and Rule #10 (harness) are higher leverage but require infrastructure setup. Tackle after #1-3 are habitual.

See [[overview]] for the philosophical frame and [[gaps-and-followups]] for what's NOT covered in these talks.
