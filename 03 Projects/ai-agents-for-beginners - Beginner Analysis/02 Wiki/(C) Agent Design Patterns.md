# (C) Agent Design Patterns

> Entity page — Core concept
> Sources: Lessons 01 (agent types) + 03 (design patterns)
> Format: 13-section canonical (llm-wiki-ingest)

## 1. What is it / Nó là gì

**Agent Design Patterns** = systematic frameworks for designing AI agents that combine: (a) **agent type** (from 7 types in L01), (b) **design dimensions** (Space/Time/Core từ L03), (c) **implementation guidelines** (Transparency/Control/Consistency).

Không phải "one pattern fits all" — mỗi agent build = **decision matrix** chọn type + dimensions + guidelines phù hợp bài toán.

## 2. Why it matters / Sao quan trọng

Without explicit patterns, AI agent dev = ad-hoc LLM wrapping. With patterns:
- **Shared vocabulary** — team members đồng ý "this is a goal-based agent với emphasis on temporal context"
- **Reusability** — pattern A works for booking → same scaffolding works for scheduling
- **Risk reduction** — missing "Transparency" = user distrust; missing "Control" = user frustration
- **Systematic coverage** — 3-dimensional design (Space/Time/Core) exposes gaps early

## 3. 7 Agent Types (Lesson 01)

| # | Type | Mechanism | Best for |
|---|------|-----------|----------|
| 1 | Simple Reflex | Predefined rules | Deterministic automation |
| 2 | Model-Based Reflex | World modeling | State-aware tasks |
| 3 | Goal-Based | Plan creation | Task decomposition |
| 4 | Utility-Based | Preference weighting | Ranking / recommendation |
| 5 | Learning | Feedback-driven | Self-improvement loops |
| 6 | Hierarchical | Tiered delegation | Complex orchestration |
| 7 | Multi-Agent | Independent/cooperative | Distributed problem-solving |

**Observation:** Types 1-2 rarely seen với modern LLM agents (LLM inherently more sophisticated). Types 3-7 = real design space.

## 4. 3 Design Dimensions (Lesson 03)

### Space — Environmental design

How agent connects people + operates across platforms.

**Questions:**
- Which devices does user access agent from?
- Which services does agent interact with?
- Is agent embedded (inside app) or standalone (chat interface)?

### Time — Temporal design

How agent manages past, present, future contexts.

**Questions:**
- How does agent use historical data?
- What triggers real-time intervention?
- How does agent evolve as user's needs change?

### Core — Foundational elements

Trust + uncertainty management.

**Questions:**
- How does agent communicate confidence?
- When does agent escalate to human?
- How does agent handle its own errors?

## 5. 3 Implementation Guidelines

- **Transparency** — Disclose AI involvement + functionality. User always knows they're talking to agent, what it can/can't do.
- **Control** — Enable customization + user agency. User can override, adjust, disable.
- **Consistency** — Familiar + multi-modal experience. Same agent behavior across text/voice/UI.

**Non-negotiable.** These aren't optional design trade-offs — they're foundational.

## 6. Design decision matrix (derived)

For each new agent, walk the matrix:

| Question | Answer example |
|----------|---------------|
| Which type? | Goal-Based + Multi-Agent hybrid |
| Space: Where? | Web app + mobile + email |
| Time: History? | Last 30 days conversation |
| Core: Trust? | Show confidence scores + escalate if <70% |
| Transparency: Disclosed? | Opening message + "AI-assistance" badge |
| Control: Overrides? | User can reject all suggestions + disable |
| Consistency: Modes? | Text + voice + API — same persona |

→ **Matrix fills = design doc.** Before code.

## 7. Implementation examples / Ví dụ

### Example 1: Customer support agent

- **Type:** Goal-Based (resolve ticket) + Hierarchical (escalate edge cases)
- **Space:** Web chat + email + phone widget
- **Time:** Access last 90-day ticket history + knowledge base
- **Core:** Confidence score per suggestion, auto-escalate <70%
- **Transparency:** "AI-assisted" badge, always-available "talk to human"
- **Control:** User can reject response + request escalation anytime
- **Consistency:** Same greeting + persona across channels

### Example 2: Research assistant (Agentic RAG)

- **Type:** Learning (refines queries based on retrieval success)
- **Space:** Web app only
- **Time:** Session-only (no cross-session memory by default)
- **Core:** Show sources for every claim
- **Transparency:** Process visible ("Searching...", "Found 5 candidates")
- **Control:** User can redirect search, reject sources
- **Consistency:** Same output format (claim + source + confidence)

## 8. Trade-offs / Limitations

- **Over-engineering risk** — small bot may not need full matrix. Use heuristics, not dogma.
- **Dimensions overlap** — Space + Time interact (device-specific history). Not fully orthogonal.
- **Guidelines can conflict** — Transparency (show everything) vs Consistency (UX simplicity). Design choice.
- **Type selection is fuzzy** — modern LLM agents often hybrid (Goal + Learning + Multi).

## 9. Comparison to sibling implementations / So sánh siblings

| Sibling | Type focus | Space handling | Time handling | Core trust |
|---------|-----------|----------------|---------------|-----------|
| **ECC** | Hierarchical (subagents) | CLI + web (plugin) | Session context | User-reviewed commands |
| **Superpowers** | Hierarchical + Goal (7-stage) | CLI | Session + skill library | Iron Law = human approval |
| **gstack** | Hierarchical (specialists) | CLI | Sprint history | Role-gated access |
| **GSD** | Hierarchical + Multi (33 agents) | CLI | Threads + Seeds (time-aware) | TÂCHES voice protection |
| **goclaw** | Multi-Agent (agent teams) | Platform (multi-tenant) | Knowledge Vault (persistent) | RBAC + quotas |

→ **All 5 siblings = Hierarchical** at scaffolding layer. Differ in Time + Space + Core implementations.

## 10. Common pitfalls / Sai lầm thường gặp

1. **Skipping Transparency** — agent seems "smarter" but users feel manipulated. Trust collapse permanent.
2. **Too many types mixed** — "hybrid of everything" = no clear behavior = unpredictable. Pick 2-3 max.
3. **Ignoring Time dimension** — stateless agents feel amnesic. Users abandon.
4. **Over-claiming Control** — "you can customize anything" but config UX terrible = learned helplessness.
5. **Inconsistent across modes** — voice persona cheerful, text persona terse = broken brand.

## 11. When NOT to use these patterns

- **Simple one-shot tasks** — rule-based script sufficient, no agent overhead
- **Deterministic workflows** — if-then cascade cleaner than LLM reasoning
- **High-stakes decisions** — agent design patterns don't replace safety engineering for medical/legal/financial
- **Pre-trained generic chatbot** — Agent design patterns overkill for "GPT-wrapper"

## 12. Storm Bear vault relevance / Ý nghĩa với vault

- **Vault = Simple Reflex + Hierarchical** — Obsidian = rule-based, Claude = delegated task types
- **Space dimension = CLI-only** — no mobile/voice yet
- **Time dimension = vault growth** — compound knowledge = time-awareness
- **Transparency = `(C)` prefix** — AI-generated marked explicitly
- **Control = "ask before editing"** rule — user agency baseline
- **Consistency = bilingual VN/EN** — same persona across both languages

→ Vault CLAUDE.md rules ≈ "implementation guidelines" applied specifically.

## 13. References / Nguồn

- Source: [[(C) Core lessons cluster summary]] (lessons 01 + 03)
- Related entities: [[(C) Multi-Agent Systems]], [[(C) Agentic RAG]]
- Sibling entities:
  - `../../gstack - Beginner Analysis/02 Wiki/(C) Specialist Roles.md`
  - `../../get-shit-done - Beginner Analysis/02 Wiki/(C) 33 Specialized Agents + Commands.md`
  - `../../goclaw - Beginner Analysis/02 Wiki/(C) Agent Teams.md`
- External: Russell & Norvig AI textbook (7 agent types origin); Microsoft Learn course
