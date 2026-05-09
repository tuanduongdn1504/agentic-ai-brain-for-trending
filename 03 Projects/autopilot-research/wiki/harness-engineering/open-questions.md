# Open questions & hedges

> Lopopolo's explicit "I don't know yet", "TBD", and flagged gaps. Each is a target for subsequent research ingests. When evidence emerges, append a "Status update" block at the bottom of the relevant question — don't quietly resolve them.

## 1. Deployment of high-speed "Spark" models

> "I have not quite figured out how to use it yet" / "I'm not sure how to deploy spark"

GPT-5.3 Spark is a faster, lower-reasoning sibling. Lopopolo says it often exhausts context via auto-compaction before completing complex tasks. Gap: no operational pattern for routing tasks across reasoning tiers.
- *talk [54:00, 55:00]*
- **Where it'd resolve:** future Anthropic / OpenAI guidance on tiered model routing; benchmark showing task-class fit per tier

## 2. Multi-team / multi-human collaboration patterns

> "TBD we have not figured this out in a general way"

How should multiple humans + multiple agents coordinate? Lopopolo questions whether every team builds bespoke internal tooling or whether a standard pattern (issue tracker + Slack as the substrate?) will emerge.
- *talk [39:35]*
- **Where it'd resolve:** comparative study of teams running harness engineering at >1-team scale

## 3. Zero-to-one product scaffolding

> "definitely not there on being able to go from new product idea to prototype one shot"

Models can extend/refactor but struggle to translate raw mocks → playable software for net-new products with no precedent screens.
- *talk [55:41]*
- **Where it'd resolve:** Lovable/Bolt/Replit material (cited but distinguished from harness engineering); GPT-6+ release notes

## 4. Complex architectural refactoring

> "the gnarliest refactorings" — area Lopopolo still spends most human time on

Decomposing monoliths and redefining deep interfaces remains a steering-heavy task. Lopopolo says "expects to get better" — not a solved problem.
- *talk [55:41]*
- **Where it'd resolve:** demonstrated tooling that automates monolith decomposition; or, evidence the gap is fundamental

## 5. Limits of internalizing dependencies (claim #7 ceiling)

Current vendoring works at "low, medium" complexity — few thousand lines. **Datadog and Temporal cited as exceeding the ceiling** because they require massive scale and security posture.
- *talk [26:00, 27:00]*
- **Why it matters:** bounds the most disruptive operational claim (claim #7 in [[core-claims]])
- **Where it'd resolve:** Datadog/Temporal vendoring case study; or, security model for high-fidelity dependency replacement

## 6. Language-specific agent legibility

> "I wonder if any languages struggle more than others because of this... I don't know"

Open question whether some programming languages are inherently harder for agents to navigate. Hints that Elixir's process supervision is unusually agent-friendly, but no comparative claim.
- *talk [46:00]*
- **Where it'd resolve:** controlled experiments comparing agent productivity across languages; or, theoretical argument for legibility properties

## 7. Maintaining "pilot" context at scale

> "I have lost track very often of what the actual state of the code looks like because I'm not in the loop"

Personal admission: humans steering large agentic teams lose intimate context. How to preserve high-level "systems thinking" while not knowing the implementation?
- *talk [35:20]*
- **Where it'd resolve:** observability/visualization tooling for agentic codebase summaries; or, organizational patterns for splitting "pilot" attention

## 8. Automated QA for distribution artifacts

Gap in agents' ability to **smoke-test built artifacts** (Electron apps in their case) before promotion. Team admits "not invested any time in this".
- *podcast [38:09]*
- **Where it'd resolve:** agent-driven E2E test harnesses; existing patterns from Playwright + GH Actions worth surveying

## 9. Utility of "Plan Mode"

Skepticism of tools where agents propose a plan for human approval. Lopopolo flags risk that humans approve plans without reading → "encoding bad instructions".
- *podcast [31:00]*
- **Tension with [[external|workflow-ai-coding/_index]]** which presents plan-first as a mature pattern in Anthropic's stack
- **Where it'd resolve:** comparative data on plan-mode adoption + outcome quality

## 10. Defining "good job" success criteria

> Meta-epistemological question: how to systematically define a "good, acceptable job" across 500 minor decisions per patch when non-functional requirements are underspecified?
- *podcast [08:00]*
- **Where it'd resolve:** frameworks for encoding non-functional requirements for agents; possibly Anthropic Skills, possibly proprietary

## How to extend

Each future research ingest that touches an open question should:
1. Add a `### Update YYYY-MM-DD` block under the relevant question
2. State what was learned + cite source
3. If the question is fully resolved, mark `## N. Question — RESOLVED YYYY-MM-DD` and link to the resolving article
4. Don't delete original framing — preserves audit trail of what we knew when
