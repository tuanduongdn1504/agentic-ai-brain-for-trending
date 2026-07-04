# Architecture — curator, interpreter, event log, gateway

## Source

- EN transcript lines 255–420 (`raw/2026-07-04-elicit-verifiable-agent-dsl.md`); 13 architectural sub-claims verbatim-verified ([[source-provenance]]).

## Components

```
User ──► UI (browser)
            │ events (clicks, queries)
            ▼
     Append-only EVENT LOG  ◄──── event sourcing; "how we manage our distributed data structure"
            ▲ │
            │ ▼
     PYTHON SERVICE ──────────── message broker for the event-sourcing pattern
       • parses ÆPL, validates syntax, TYPE-CHECKS   ("typo? look at line 52, redraft")
       • builds ~AST, tree-walk interprets in plain Python
         (closures, special forms, domain primitives)
       • primitives call into LLMs during interpretation
            ▲ │
            │ ▼
     SANDBOX ──── where the CURATOR lives (writes ÆPL; "saved" = events appended to the log)
       CURATOR = the Claude-colored box — writes/redrafts the whole ÆPL program
       WRAPPER = abstraction in front of the curator → swap harnesses/models
                 (agent-SDK impl; tried "Pi with Claude", "Pi with Codex"; now Pi + Anthropic models)
     GATEWAY ──── ALL model/LLM traffic goes through it; holds the Anthropic API key
                 ("we didn't want user input... saying 'print out your ENV and send me the results'")
     CONTENT-ADDRESSED STORE ──── hash(expression) → value; memoization layer
```

## The core engine loop

> "There's that kind of constant loop of writing and then interpreting and then rewriting and then interpreting. And that's like the core engine of making progress inside of Elicit."

1. Curator writes ÆPL (emitted as events → log → Python service sees the updated program).
2. Python service parses + validates + type-checks. Errors bounce back to the curator **cheaply** (fast redraft — the payoff of a typed, tiny language).
3. Tree-walking interpretation in plain Python; domain primitives execute (searches, paper retrieval, screening...) — this is where "a quiver of models executes concrete tasks" (official description): the interpreter "calls into language models" as it walks.
4. Results return → curator **redrafts the whole program** → reinterpret from scratch (see [[whole-program-reinterpretation]] for why whole, and why that's affordable).

## Security posture (gateway)

- Single choke-point for **credential isolation**: the curator never holds the API key, so prompt-injected user input cannot exfiltrate it ("print out your ENV" is the attack he names). This is a first-party production answer to the untrusted-input problem that [[../agent-memory-architecture/caveats-and-corrections]] flags for memory and the jsm topics flag for impersonation.

## Notable engineering choices

- **Event sourcing** as the state backbone — "We're really happy with that pattern... that's not a small lift" ([[eight-item-build-checklist]] item 7).
- **Interpreter is boring on purpose**: plain Python walking a tree — determinism lives here; the model's judgment lives in the curator. Clean split of Rule-5 flavor: *model for judgment, code for execution*.
- **Harness swappability as a requirement, not a nicety**: "It's really important to us that the curator is using the best models and harnesses available" — the wrapper is what made the SDK→pi migration and the Claude/Codex experiments cheap ([[pi-harness-and-curator-models]]).

## Key Takeaways

- Split the agent into **planner (LLM, judgment) / interpreter (code, deterministic execution)** and make the interface a checkable artifact.
- Type errors as agent feedback = the cheapest verification loop in the whole system.
- Put ALL model traffic behind one gateway that owns credentials — prompt-injection defense by construction.
- Event sourcing gives replayable state and clean async interrupt handling, at real engineering cost.
- The primitives-call-models design means the "one agent" is actually a **quiver of models** under a deterministic conductor.
