# Deep modules + TDD — feedback loops the AI can actually use

## Source

- Transcript `raw/2026-07-14-pocock-software-fundamentals.md` (failure modes #3+ of [v4F1gFy-hqg](https://www.youtube.com/watch?v=v4F1gFy-hqg)) · skill texts ground-checked via `gh api` 2026-07-14.

## Failure mode: "it built the right thing, but it doesn't work"

- Standard fix = **feedback loops**: static types ("if you're not using TypeScript, that's crazy"), browser access for front-end agents ("absolutely needs that"), automated tests.
- **The twist:** the LLM *has* the loops but uses them badly — it "does way too much at once," generating piles of code before checking anything. PragProg name: **outrunning your headlights** — "the **rate of feedback is your speed limit**."
- Fix: **TDD**, because it *forces* small steps: red → green → refactor. Ground-checked: `skills/engineering/tdd/SKILL.md` exists in mattpocock/skills.
- Note the framing: TDD here is not a quality ideology — it's a **pacing constraint for agents**, a mechanical way to keep the model inside its feedback horizon.

## Why testing is hard → deep modules

- Test-writing decisions (unit size / what to mock / which behaviors) are **interdependent** — and easy codebases to test are *good* codebases. So testability loops back to design.
- **Ousterhout deep modules:** relatively few, large modules — "lots of functionality hidden behind a simple interface." Shallow modules: little functionality, complex interface.
- **The AI-navigability argument (the talk's most original point):** shallow-module sprawl — "a ton of different tiny little blobs" — is "really hard for the AI to explore"; the agent bounces between files, misses the right module, misreads dependencies. **AI is also really good at *creating* codebases like this** — so unmanaged agents manufacture the very structure that blinds them.
- Deep modules put **interfaces on top** (human-designed, carefully controlled) with implementations the AI can own: "test at the interface, verify using that interface" — a codebase that *rewards* TDD.
- Ground-checked: `skills/engineering/improve-codebase-architecture/SKILL.md` exists and is explicitly this talk operationalized — "refactors that turn shallow modules into deep ones. The aim is **testability and AI-navigability**," with a design vocabulary (module/interface/depth/seam/adapter/leverage/locality), the **deletion test**, "the interface is the test surface," git-history hot-spot scoping, and an HTML report of deepening candidates. Bonus find: `skills/in-progress/setup-ts-deep-modules/` — the concept becoming scaffolding tooling.

## Failure mode: "shipping faster than your brain" → gray boxes

- New AI-era exhaustion: throughput exceeds human comprehension ("raise your hand if you've felt more tired than ever" — "it's knackering").
- Deep modules as the fix for the *human*: treat modules as **gray boxes** — design the interface, understand the purpose, **don't review the implementation** (for non-critical modules; he explicitly exempts things like finance).
- **"Design the interface, delegate the implementation."** Consequence: the module map must live in your ubiquitous language and your PRDs — his PRD skill specifies **module changes and interface modifications** explicitly ([[../pocock-real-feature-build/prd-and-issues-pipeline]] shows this in practice).
- Kent Beck anchor: "**Invest in the design of the system every day**" — the daily-investment counter to specs-to-code divestment ([[anti-specs-to-code-thesis]]).

## Key Takeaways

- TDD-for-agents = pacing mechanism: the rate of feedback is the speed limit, and TDD is how you enforce the limit on a model that outruns its headlights by default.
- Deep modules serve **three** constituencies at once: testability (simple boundaries), AI navigation (fewer, findable units), and human sanity (gray-box review budgets).
- Unmanaged agents *generate* shallow sprawl — architecture discipline is a control loop, not a one-time cleanup; the improve-codebase-architecture skill packages the loop.
- Review budget is a design decision: criticality determines which implementations you actually read.
- Cross-links: [[../pocock-agentic-workflow/strategic-vs-tactical]] (interfaces as the strategic layer) · [[../how-we-claude-code/_index]] (agent-native verification = the same "verify at the boundary" instinct) · [[../system-thinking-ai-coding/three-golden-questions]] (blast-radius gate — sibling review-budget heuristic).
