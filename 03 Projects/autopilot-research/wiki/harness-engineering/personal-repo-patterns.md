# Personal-repo harness — concrete patterns

> Tactical recipes the 6 sources [Source 11-16] recommend for a single developer's repository. Patterns are ordered most-foundational → most-advanced. Each pattern has at least one explicit citation; where speakers disagree, the divergence is flagged and routed to [[personal-repo-vs-org-scale]]. See also [[personal-repo-overview]] for context.

## 1. Bootstrap `CLAUDE.md` via `/init`

- Run `/init` inside Claude Code to have it analyze the codebase and auto-generate a draft `CLAUDE.md` [Source 11]
- John Kim then trims the draft to **<300 lines**; longer files bloat the context budget on every turn [Source 11]
- Avthar layers project goals, design style guide, and "repository etiquette" rules into the file — e.g. "never push directly to main" [Source 12]
- Simon Scrapes frames the file as an SOP that explicitly lists **what good looks like AND what to avoid** [Source 16]
- Pattern: write declarative rules ("always X / never Y") not narrative — declarative survives compaction better

## 2. Use Plan Mode before any non-trivial feature

- Toggle Plan Mode via **`Shift+Tab`** before kicking off a feature [Source 15]
- Avthar's "Plan" phase in PSB: force the AI to ask clarifying questions and surface architectural assumptions before any code is written [Source 12]
- This is a load-bearing checkpoint — the speakers describe it as the difference between "the agent guesses" and "the agent confirms"
- **Divergence flag:** Lopopolo at org-scale dismisses plan mode (see [[contrarian-stances#9]]) on the grounds that humans rubber-stamp plans without reading. At personal scale, the speakers argue the human IS reading because there's only one author. See [[personal-repo-vs-org-scale#plan-mode]]

## 3. Structure prompts with GCAO

- Productive Dude's framework: every prompt has slots for **Goal, Context, Action, Output** [Source 15]
- Concrete: attach a CSV of analytics or a screenshot as "Context"; specify "Output" as the file path/format you want
- Pattern emerges across speakers under different names — Avthar's PSB-Build phase fills the same slots implicitly [Source 12]
- The shared design intent: never let the agent infer the scope; encode it

## 4. Manual summarization to `progress.md` (anti-autocompact)

- GritAI Studio argues autocompact is **"a problem"** because Claude unilaterally decides what to discard — often discarding important decisions [Source 14]
- Their alternative: maintain a `progress.md` file in the repo, save state to it before clearing context, start fresh with a clean window plus the progress file as input [Source 14]
- The AI Automators' equivalent pattern is **"context reset"** — a new agent starts clean but reads a tracking file [Source 13]
- **Divergence flag:** John Kim *trusts* autocompact and "lets it work" [Source 11]. See [[personal-repo-vs-org-scale#autocompact]]

## 5. Isolate research in sub-agents

- GritAI's **"Explore" sub-agent** reads dozens of files in its own context window and returns a clean summary to the main session [Source 14]
- John Kim uses sub-agents for **atomic tasks** so research and tool-call noise don't bloat the main thread [Source 11]
- Pattern: anything that requires reading many files (codebase exploration, dependency audit, error log triage) is offloaded to a sub-agent
- This is the personal-scale analog of agent-legibility decomposition (see [[terminology#agent-legibility]]) — same intent, sub-agent boundary instead of package boundary

## 6. Git worktrees for parallel Claudes ("multi-clauding") {#worktrees}

- Avthar uses **Git worktrees** to allow multiple Claude instances to work on different branches inside the same repository [Source 12]
- John Kim describes the experience as **"juggling" Claude instances** — comparable to **playing Starcraft**, switching focus across 3-5 terminals [Source 11]
- Concrete: `git worktree add ../feature-x feature-x` creates an isolated checkout, one Claude per worktree, zero file-system collisions
- This is the solo-developer personal-scale analog of Symphony orchestration — see [[personal-repo-vs-org-scale#orchestration]]

## 7. Adversarial evaluation (Generator + Skeptical Evaluator)

- The AI Automators run a **two-agent setup**: one "Generator" writes code, a separate **"Skeptical Evaluator"** probes for edge cases and design "slop" [Source 13]
- Justification: out-of-the-box Claude **"praises mediocre work"** and **"talks itself into approving"** issues it just identified [Source 13]
- Sub-pattern: the evaluator prompt explicitly instructs skepticism — without that framing, the second agent inherits the same approval bias
- **Divergence flag:** John Kim says a simple **validation loop** (build/compile feedback) is sufficient for self-improvement, no separate evaluator needed [Source 11]. See [[personal-repo-vs-org-scale#self-eval-vs-adversarial]]

## 8. Curated skill library (20-30, not thousands)

- Simon Scrapes' **contrarian take**: limit yourself to **20-30 well-built skills** rather than the hundreds-to-thousands available in marketplaces [Source 16]
- "Skill bloat" makes agents slower and triggers **cannibalization** — multiple skills compete for the same command name, none reliably activate [Source 16]
- His DBS pattern for high-quality skills: **Direction** (step-by-step workflow), **Blueprints** (examples to follow), **Solutions** (reusable scripts) [Source 16]
- **Divergence flag:** John Kim is **liberal**: "download hundreds of skills" and use specific keywords to trigger them [Source 11]. See [[personal-repo-vs-org-scale#skill-density]]

## 9. MCP for external integrations (universally adopted)

- All speakers reach for **Model Context Protocol (MCP)** to wire Claude into Google Drive, GitHub, Notion, databases [Source 11, Source 12, Source 15, Source 16]
- John Kim flags MCPs as **"the biggest offenders"** for token bloat — audit with `/context` regularly [Source 11]
- **Divergence flag:** Lopopolo is **"pretty bearish on" MCP** (see [[contrarian-stances#8]]) — argues it injects tokens into context and breaks autocompact. The personal-scale sources accept the trade-off; Lopopolo at org scale does not. See [[personal-repo-vs-org-scale#mcp-stance]]

## 10. Regression prevention via `#` shorthand

- Avthar's pattern: when Claude makes a mistake, type **`#` followed by the correction** [Source 12]
- The correction is automatically incorporated into project rules — patches the AI's behavior on the fly so it never repeats the same error [Source 12]
- This is the personal-scale embodiment of the vault-root "don't repeat the same mistake twice" prime directive — encoded as an editor shortcut rather than a doctrine

## 11. Frequent `/context` audits

- John Kim runs `/context` frequently to see a **visual breakdown of what is consuming the attention budget** [Source 11]
- Common offenders: bloated MCPs, large attached files, accumulated tool-call output
- GritAI's framing: context is an **"attention budget"** — too much causes confusion, too little causes hallucinations [Source 14]
- Pattern: treat token usage as an operational metric, not a billing concern

## 12. Long-running tasks via Dispatch

- Productive Dude highlights **Dispatch** — a feature that acts as a "computer harness" letting Claude interact with file systems and apps while the user is away [Source 15]
- Pattern: not every task needs human attendance; the harness is what makes unattended work safe
- This is the personal-scale prefiguration of org-scale autonomous agents — the operating principle ("the harness keeps the agent safe when no human is watching") is identical

## 13. PSB system (Plan → Setup → Build) (added 2026-05-30)

- **AI with Avthar's** project-lifecycle framework — a 3-phase discipline applied before each new project / feature [Source: getting-started drain 2026-05-30]
- **Plan** — force the agent to outline logic, identify technical risks, ask clarifying questions before touching code (~15 min)
- **Setup** — scaffold the project structure, install dependencies, prepare context files
- **Build** — actual coding phase, now bounded by Plan + Setup decisions
- More project-scoped than GCAO (which is per-prompt) — PSB is per-project-or-feature
- **Compose with:** [[#2-use-plan-mode-before-any-non-trivial-feature|pattern #2 Plan Mode]] (Plan phase) + [[#1-bootstrap-claudemd-via-init|pattern #1 CLAUDE.md bootstrap]] (Setup phase). PSB is the umbrella; patterns 1+2 are mechanisms inside the Plan + Setup phases.

## 14. DBS framework (Direction → Blueprints → Solutions) for Skill creation (added 2026-05-30)

- **Productive Dude's** skill-authoring framework — distinct from GCAO (which is for individual prompts) [Source: getting-started drain 2026-05-30]
- **Direction** — what the Skill is for; one-line purpose
- **Blueprints** — structure templates / scaffolding the Skill should follow
- **Solutions** — concrete worked examples the agent learns from
- Compatible with [[../claude-cowork/skills-vs-plugins-hierarchy]]'s Skill = recipe framing — DBS provides authoring discipline for the recipe content itself
- **Compose with:** Ross Mike's build-via-failure recipe ([[../ai-operating-system/skills-architecture-progressive-disclosure]]) — failure produces Solutions content; Direction + Blueprints come from the operator's initial framing

## 15. SQLite-trace pattern for project memory (added 2026-05-30)

- **Tù Bà Khuỳm's** V2 harness contribution — local SQLite database stores: project decisions, agent action traces, friction logs [Source: getting-started drain 2026-05-30; full article: [[personal-repo-tu-ba-khuym-getting-started]]]
- **Corpus-first non-Markdown approach** to project memory across the 22-article harness-engineering topic + 14-article claude-cowork sister-topic
- Closed loop: traces → identify friction → backlog for harness refinement → improved harness reduces future friction
- **Rationale:** SQLite is more precise + less prone to being ignored or filled incorrectly by the agent compared to a text file
- **Trade-offs vs Markdown:** lower token cost (agent reads via tool calls, not context inclusion) + schema enforces correctness; harder for operator to eyeball + requires SQLite-capable MCP server or scripts
- **Composition with [[#1-bootstrap-claudemd-via-init|pattern #1]]:** SQLite REPLACES the `CLAUDE.md` brain for state; operator can keep `CLAUDE.md` for instructions and use SQLite for state/traces
- **Unaddressed:** schema migration / multi-machine sync / cross-project memory / version control (see [[open-questions]] §11-14 for the 4 specific open questions)

## Compositional pattern: the full personal stack

A maximalist personal harness composes most of the above:
1. `CLAUDE.md` (<300 lines) + `progress.md` for state checkpointing
2. `/init` to bootstrap, Plan Mode for every feature, GCAO for every prompt
3. 20-30 curated skills + MCP integrations for tools
4. Sub-agents for research, adversarial evaluator for QA
5. Git worktrees + multi-Claude for parallel execution
6. `/context` audits + `#` corrections as continuous-improvement loop
7. Dispatch for long-running unattended work

Speakers don't all run the full stack — they cherry-pick. The pattern is composable, not monolithic.

## Key takeaways

- `CLAUDE.md` + Plan Mode + GCAO is the minimum viable harness — everything else is an optimization [Source 11, Source 12, Source 15]
- Manual summarization (`progress.md`) and adversarial evaluation are **defensive** patterns where speakers don't trust the model's defaults [Source 13, Source 14]
- Sub-agents and Git worktrees are **scaling** patterns — same purpose as Symphony at radically smaller scope [Source 11, Source 12]
- Skill curation discipline (20-30 high-quality) is the personal-scale echo of Lopopolo's 5-10 skills (see [[terminology#skills]]) — both reject marketplace bloat [Source 16]
- Several patterns directly invert Lopopolo positions (MCP adoption, Plan Mode use, self-eval trust) — see [[personal-repo-vs-org-scale]] for the full disagreement axis
- The compositional stack assumes a solo developer; multi-developer collaboration is not in scope for these sources (see [[personal-repo-gaps]])
- Cross-reference [[../claude-md-12-rules/_index]] for the rules layer that complements these tactical patterns at personal scale, and [[../claudekit/_index]] for a higher-rung framework if the curated-skill stack grows beyond manual curation
