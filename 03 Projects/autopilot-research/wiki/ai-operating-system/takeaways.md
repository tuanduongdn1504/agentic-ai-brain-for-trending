# Takeaways — 10 actionable rules

The corpus-distilled actionable list. Each rule has cross-references to the article(s) that go deeper.

## Source

- Raw: [`raw/2026-05-29-ai-operating-system-5-skills-framework.md`](../../raw/2026-05-29-ai-operating-system-5-skills-framework.md), §Takeaways

## The 10 rules

### 1. Adopt progressive disclosure for skills

Skill files load only their **name and description** into the primary context; the agent pulls the full instruction set only when it identifies the skill as necessary for the task. **Simon Scrapes, Ross Mike**.

→ See [[skills-architecture-progressive-disclosure]]

### 2. Implement a self-improving memory loop

Configure the agent to update a persistent `memory.md` file automatically whenever you provide a correction or new preference. Learnings compound across sessions. **Remy Gaskell, Simon Scrapes**.

→ See [[memory-and-context-rot]] + sister-topic [[../claude-cowork/contextual-engineering]] Pattern D

### 3. Separate roles into Builder + Orchestrator + Executor

Use construction-specific tools (**Cloud Code**, **Lovable**) for one-time platform building. Use **OpenClaw** (or similar) to orchestrate workflows. Use specialized executors for research / email / voice / meeting-intel. **Mani Kanasani**.

→ See [[builder-orchestrator-executor-pattern]]

### 4. Optimize tokens by disabling "extended thinking"

Disable reasoning / thinking modes in `.json` configuration for routine tasks. This optimization alone can save **thousands of tokens per API call**. **Mani Kanasani**.

(Cross-reference: this is the missing 11th takeaway from the Claude Cowork corpus — different optimization than Sonnet-default but compatible.)

### 5. Build skills through manual "successful runs"

Never hand-write skills from scratch. Walk an agent through a workflow manually; correct its failures; once a successful run completes, ask: **"review what we just did and create a skill for it."** **Ross Mike**.

→ See [[skills-architecture-progressive-disclosure]] (build-via-failure section) + sister-topic [[../claude-cowork/skills-to-plugins-pipeline]] (Jack Roberts's handover test composes here)

### 6. Enforce infrastructure-level security

Secure production agents using **NemoClaw** to sandbox the environment. Security policies live at the **infrastructure level**, not in the model's internal guardrails. **Mani Kanasani**.

→ See [[security-philosophies-and-sandboxing]] — and the conservative-access counter (Ross Mike + Remy Gaskell)

### 7. Standardize context with a Markdown folder structure

Organize your "Second Brain" with dedicated folders for `Context`, `Daily` logs, and `Intelligence`. Use `claude.md` as a navigational **"map"** for the agent. **Ben AI, Simon Scrapes**.

→ See [[instruction-layer-markdown-files]] + sister-topic [[../claude-cowork/sandboxing-and-workspace-structure]]

### 8. Use MCP as a universal translator

Connect all third-party software (Slack, Notion, etc.) via the **Model Context Protocol (MCP)** for standardized, scalable access. **Remy Gaskell**.

→ See sister-topic [[../claude-cowork/mcp-connectors-landscape]] for the full connector landscape

### 9. Perform weekly "context hygiene" audits

Conduct routine audits of `.md` instruction files: merge duplicates, delete irrelevant data, resolve conflicting information. Prevents context rot at the structural level. **Ben AI, Simon Scrapes**.

→ See [[memory-and-context-rot]] §OS Optimizer

### 10. Orchestrate via an autonomous Kanban loop

Manage multi-agent teams using a **shared Kanban board** (e.g., via Superbase). Agents autonomously pick up tasks, move them through stages (To Do → Doing → Review → Done), and file reports. **Mani Kanasani**.

→ See [[builder-orchestrator-executor-pattern]] §Kanban orchestration

## Synthesized priority order

For a **first AIOS deployment**: rules 1, 5, 7, 8 are the minimum viable stack. Add rules 3 + 10 when scale demands multi-agent.

For a **growing AIOS** (3-5 executors): add rules 2, 4, 9. Context-rot management becomes load-bearing.

For **production AIOS** (5+ executors, business-critical): add rule 6. See also [[production-readiness-gaps]] — rules 1-10 are necessary but not sufficient for enterprise.

## Vault application

The vault's `autopilot-research` project satisfies 8 of 10 rules:

| Rule | Vault instance |
|---|---|
| 1 (progressive disclosure) | ✓ Storm Bear `05 Skills/SKILL_LOCK_POLICY.md` + on-demand skill loading |
| 2 (self-improving memory) | ✓ `_state/` chapter files updated on every audit cycle |
| 3 (Builder/Orchestrator/Executor) | ✓ Template + drain script + Claude session executors |
| 4 (disable thinking) | Per-task choice; not codified at routine level |
| 5 (build skills via successful runs) | ✓ `05 Skills/SKILL_LOCK_POLICY.md` tracks active-from-usage |
| 6 (infrastructure-level security) | Partial — scope-clamp + git but not container sandbox |
| 7 (Markdown folder structure) | ✓ `CLAUDE.md` hierarchy at vault + project + skill |
| 8 (MCP universal translator) | ✓ Multiple MCP integrations |
| 9 (weekly context hygiene) | ✓ Mini-audit cadence at v66 / v69 / v72 |
| 10 (autonomous Kanban loop) | Partial — `topics-queue.md` is a primitive Kanban |

The two partial-coverage rules (4, 6, 10) are real gaps — production-pilot would need to address them.

## Cross-topic synthesis: comparing to the Cowork 9-rules + this 10-rules

Significant overlap (sister-topic synthesis):

| Concept | Cowork rule | AIOS rule | Notes |
|---|---|---|---|
| Sandboxing | 1 | 6 | Cowork: workspace folder · AIOS: NemoClaw sandbox |
| Persistent context files | 2 | 7 | Same pattern, different naming |
| Token efficiency | 3, 5, 6, 10 | 1, 4 | AIOS adds progressive disclosure + thinking-off |
| Skill codification | 7 | 5 | Cowork: handover test · AIOS: build-via-failure |
| Strategic context injection | 8 | (implicit) | Cowork rule 8 ≈ AIOS rule 7 |
| Remote dispatch | 9 | (not in AIOS) | Cowork-specific |
| Kanban orchestration | (not in Cowork) | 10 | AIOS-specific |

Net result: 9 + 10 rules, ~6 overlap, ~3-4 distinct each. This is **two different operator personas studying the same architecture** — Cowork operator is the consumer; AIOS operator is the builder.

## Key Takeaways

- **10 explicit rules** + 1 implicit cross-from-Cowork (Sonnet-default) = effective stack of 11 production-validated practices
- **Rules 1, 5, 7, 8** are the minimum viable AIOS — anything less is incomplete
- **Vault satisfies 8 of 10 rules** — the 2 partial-coverage rules (infrastructure sandbox + Kanban) are real production-pilot gaps
- **6 rules overlap with sister Cowork corpus** — strong evidence this is a single underlying pattern, not two separate disciplines
- **For enterprise**: rules 1-10 are necessary but not sufficient — see [[production-readiness-gaps]]

## Related

- [[overview]] — start here
- [[instruction-layer-markdown-files]] — rule 7
- [[skills-architecture-progressive-disclosure]] — rules 1, 5
- [[memory-and-context-rot]] — rules 2, 9
- [[builder-orchestrator-executor-pattern]] — rules 3, 10
- [[security-philosophies-and-sandboxing]] — rule 6
- [[off-the-shelf-vs-handbuilt-skills]] — rule 5 supplementary
- [[production-readiness-gaps]] — what rules 1-10 don't cover
- [[../claude-cowork/takeaways]] — sister 9-rule list
