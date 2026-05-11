# ClaudeKit vs Lopopolo vs Mnilax — comparison + personal harness adoption matrix

> **This is the load-bearing article for the topic.** The user's stated goal: "so sánh và cải thiện harness cá nhân". Below: 3-way comparison across all axes, plus a decision matrix for what to borrow from each system.
>
> See also: [[external|claude-md-12-rules/comparison-harness-engineering]] for the 2-way Mnilax vs Lopopolo comparison. This article adds ClaudeKit as third reference.

## Scale + cost-profile context

| Dimension | Mnilax 12-rule | ClaudeKit | Lopopolo harness eng |
|---|---|---|---|
| Target user | Individual developer | Individual + small team | 7-engineer team at OpenAI |
| Token cost profile | Strict budgets (4K/task, 30K/session) | Soft limit (100K bloat threshold) | "Token Billionaire" ($2-3K/day) |
| Codebase scale | Single-repo or modest monorepo | Single project, multi-tool portable | 1M+ LOC, 750 packages |
| Reviewer count | Solo / standard PR | Approval gates + standard PR | Dark Factory (zero human pre-merge) |
| Pipeline complexity | Single Claude Code session | Workflows (sequential phases) | Multi-agent + Symphony orchestration |
| Infrastructure required | None (rules only) | npm install + `.claude/` config | Custom Elixir/Beam + Linear + observability |
| Vendor coupling | Anthropic native | Multi-provider via CCS | OpenAI-internal |

These are **3 rungs of the same ladder**. ClaudeKit sits between Mnilax and Lopopolo: more infrastructure than Mnilax (full framework with commands), less than Lopopolo (no team-scale orchestration).

## Per-rule mapping — how each system addresses Mnilax's 12 rules

| Mnilax rule | Mnilax (text) | ClaudeKit (infra) | Lopopolo (infra) |
|---|---|---|---|
| 1. Think before coding | Rule text | `/ck:brainstorm`, `/ck:plan`, `/ck:scenario` | "Map, Not Manual" methodology — agent-targeted docs |
| 2. Simplicity first | Rule text | None — relies on CLAUDE.md | **Conflicts** — "code is free" stance |
| 3. Surgical changes | Rule text | Approval gates | **Conflicts** — agents refactor freely |
| 4. Goal-driven | Rule text | `/ck:cook` requires success criteria | Spec-driven (Ghost Libraries, WORKFLOW.md templates) |
| 5. Model for judgment only | Rule text | Hooks ARE deterministic layer | Aligned — deterministic CI + lint guard agents |
| 6. Token budgets | Hard rule (4K/30K) | Soft 100K bloat threshold | **Conflicts** — $2-3K/day target |
| 7. Surface conflicts | Rule text | None | **Conflicts** — Symphony trashes + rebuilds |
| 8. Read before write | Rule text | `/ck:scout` explicit command | Agent-legibility + Layers architecture |
| 9. Tests verify intent | Rule text | `/ck:test` + Tester agent | Video evidence (bug repro + fix videos) |
| 10. Checkpoint per step | Rule text | `session-state.cjs` persistent state | Symphony durable execution + Ralph Loop |
| 11. Convention conformance | Rule text | None | **Conflicts** — restructures for agent-legibility |
| 12. Fail loud | Rule text | 3-attempt halt; Research Preview labeling | Observability stack (Prometheus, Grafana) |

**ClaudeKit infrastructure-implements: 7 of 12.** Aligned with Mnilax across 5 axes; partial on 2; gaps on 5.

**Lopopolo infrastructure-implements: 7 of 12 too, BUT in 5 axes conflicts directly with Mnilax** — code-is-free, no budgets, trash-and-rebuild, hyper-modular restructuring, multi-agent autonomy.

## Where each system is uniquely strong

### Mnilax is uniquely strong at...

- **Discipline you can apply tomorrow with zero infrastructure** — just paste 12 rules into CLAUDE.md
- **Behavioral contract framing** — every rule prevents a documented mistake (high signal-to-noise)
- **200-line ceiling enforcement** — the rules themselves prove rules-as-words have a complexity limit
- **Conditional adoption** — drop rules that don't match your real failure modes

### ClaudeKit is uniquely strong at...

- **CCS multi-provider routing** — Claude / GPT / GLM / Kimi switchable from single command surface
- **Portability via `ck migrate`** — intelligence layer survives tool migration (Cursor / Codex / Droid)
- **Pre-built command surface** — 50+ commands save framework-building work
- **Hooks for deterministic enforcement** — operationalizes "model for judgment only" (Mnilax Rule 5) as infrastructure
- **State persistence across sessions** — `session-state.cjs` solves multi-step drift (Mnilax Rule 10)
- **Coexistence model** — selective merging + ownership tracking won't break existing setup
- **`/ck:fix` 6-phase pipeline** — most-structured debugging workflow in the comparison

### Lopopolo is uniquely strong at...

- **Org-scale orchestration** — Symphony handles 7-engineer fleets + 1M LOC
- **Multi-agent stack** — Codex + Aardvark working same codebase concurrently
- **Architectural patterns** — Layered architecture (Types → Config → Repo → Service → Runtime → UI), 750-package decomposition, Ghost Libraries
- **Production-tested at scale** — empirical data from actual OpenAI internal deployment
- **Cultural posture insights** — "editor ban", "Dark Factory", "Token Billionaire" — codify cultural changes alongside technical

## Decision matrix — what to borrow from each (for personal harness improvement)

### Always borrow (universally applicable, low cost)

| Pattern | From | Why |
|---|---|---|
| All 12 Mnilax rules in CLAUDE.md | Mnilax | Zero infra, immediate effect, well-tested template |
| 3-attempt halt for failed fixes | ClaudeKit `/ck:fix` | Prevents wicked-problem spiral; Mnilax Rule 12 in code |
| `session-state.cjs`-style persistence | ClaudeKit | Mnilax Rule 10 (checkpoint) becomes durable |
| Hook for privacy file blocking | ClaudeKit `privacy-block.cjs` | Prevents secret leakage; deterministic safety |
| ADR-style decision logging | Lopopolo | Architecture decisions survive sessions + onboarding |
| Read-before-write discipline | Mnilax Rule 8 + Lopopolo agent-legibility | Compound — rule + architecture |
| `llms.txt` for repo entry point | Lopopolo "Map, Not Manual" + ClaudeKit `/ck:llms` | Both systems agree |
| Test-verifies-intent verification | Mnilax Rule 9 (rule) + Lopopolo (video evidence) | Compound — rule + concrete artifact |

### Borrow if you have the infrastructure

| Pattern | From | Required infra |
|---|---|---|
| Multi-agent orchestration | Lopopolo Symphony | Either ClaudeKit `/ck:team` or build/run Symphony fork |
| Multi-provider routing | ClaudeKit CCS | ClaudeKit install |
| Workflow definitions | ClaudeKit `/ck:cook` | ClaudeKit install OR equivalent custom framework |
| Auto-permission classifier | ClaudeKit Auto Mode | ClaudeKit install + acceptance of "Research Preview" |
| Skills as `.md` files | All 3 systems agree on this pattern | Native Claude Code already supports |

### Borrow with caution (depends on scale)

| Pattern | From | Caveat |
|---|---|---|
| "Code is free" + vendor-everything | Lopopolo | Only if your maintenance is also fully agent-driven. Otherwise Mnilax Rule 2-3 wins. |
| Trash-and-rebuild conflict resolution | Lopopolo Symphony | Requires comprehensive tests to verify rebuilt impl. Otherwise Mnilax Rule 7 (surface conflicts) safer. |
| Hyper-modular architecture (750 packages) | Lopopolo | Only valid for "Dark Factory" no-human-reading codebases. Otherwise Mnilax Rule 11 (conformance) wins. |
| Bypass permissions | ClaudeKit | Container/VM only. Never on local dev where productivity > destructive risk. |
| `--fresh` reset without backup | ClaudeKit | NEVER without `tar czf` backup first — no auto-backup. |

### Skip (don't borrow)

| Pattern | From | Why |
|---|---|---|
| Token Billionaire spend rate | Lopopolo | $2-3K/day requires Symphony + observability + team. Without those, just expensive. |
| Dark Factory zero-review | Lopopolo | Org-scale only. Personal use = always review. |
| 18+ rules in CLAUDE.md | Mnilax tested | Compliance falls off cliff past 14 rules. Stick to 12. |
| Examples instead of rules | Mnilax rejected | Already-tested anti-pattern. |

## Recommended compound posture (for individual / small team)

This is the **practical recommendation** based on the 3-way comparison:

### Floor (zero-cost, do today)

1. Paste 12 Mnilax rules into vault-root CLAUDE.md ✅ already done in our session
2. Apply Storm Bear's existing prime directive + librarian discipline
3. Use Mnilax's "behavioral contract" framing — every rule prevents a documented mistake

### Layer 1 (low-cost infra, do this week)

4. Add `privacy-block` style hook for `.env` / secrets / `.git/config` reads (no need for ClaudeKit; native Claude Code hooks)
5. Add `session-state` style hook that persists current plan to `.claude/state/.last-state.md` between sessions
6. Add `pre-commit` git hook running `npm test` or equivalent → catches Mnilax Rule 9 violations
7. Adopt ADR-style decision log in each project (Lopopolo borrow)

### Layer 2 (moderate-cost infra, do this month)

8. Try ClaudeKit `ck init` in ONE sandboxed project (per [[setup-and-coexistence]] decision matrix). Evaluate command surface.
9. Borrow `/ck:fix` 6-phase pipeline structure for your custom debug workflow (don't need ClaudeKit installed)
10. Build `/ck:scout`-equivalent — pre-write codebase scan command using ripgrep + a brief Claude prompt

### Layer 3 (high-cost infra, do this quarter — only if scale demands)

11. Investigate Symphony-equivalent orchestration (community impls in [[external|harness-engineering/symphony-architecture]]) if running 3+ agents simultaneously
12. CCS-equivalent multi-provider abstraction if Anthropic rate-limits become operational bottleneck
13. Observability stack (Prometheus + Grafana) if running >50K tokens/day consistently

### Stop here — don't go further as individual

Past Layer 3, you're recreating Lopopolo's stack without his team. ROI cliff. If you genuinely need org-scale infrastructure, you have a team — at which point standard hiring + product-management applies, not personal-harness optimization.

## Personal harness improvement worksheet

For the user's actual stated goal — "cải thiện harness cá nhân" — answer these in order:

1. **What % of your Claude Code work involves multi-step pipelines >3 steps?**
   - <20% → stick with Mnilax 12 rules only
   - 20-50% → add Layer 1 infrastructure
   - >50% → consider Layer 2 (ClaudeKit trial)

2. **How many AI providers do you actively use?**
   - 1 (Claude only) → CCS routing N/A, no ClaudeKit benefit there
   - 2-3 → CCS becomes valuable; ClaudeKit Layer 2 worth trying
   - >3 → CCS is high-leverage; ClaudeKit highly recommended

3. **How often do you lose work to context bloat / forgotten state?**
   - Rarely → don't bother with state persistence
   - Monthly → Layer 1 session-state hook saves the day
   - Weekly → Layer 2 ClaudeKit's full state mgmt

4. **How many tools do you switch between (Claude Code / Cursor / Codex / Droid)?**
   - 1 → portability irrelevant
   - 2-3 → `ck migrate` becomes valuable
   - >3 → ClaudeKit's portability is unique value

5. **Do you maintain a "behavioral contract" mindset?**
   - Yes → Mnilax 12 rules immediately useful
   - No → start there before any infrastructure

## Key Takeaways

- **3-way comparison reveals 3 rungs** of harness sophistication: rules (Mnilax) → framework (ClaudeKit) → infrastructure (Lopopolo)
- **ClaudeKit infrastructure-implements 7 of 12 Mnilax rules** — strong but incomplete coverage; Rules 2, 7, 11 still require user discipline
- **Lopopolo conflicts with Mnilax on 5 axes** (code-is-free, no budgets, trash-rebuild, restructuring, multi-agent autonomy) — these are scale-dependent
- **Recommended compound posture: Floor + Layer 1 universally, Layer 2 selectively, Layer 3 only at clear scale signal**
- **The "always borrow" list (8 patterns)** is the cheapest highest-ROI portion — apply regardless of framework choice
- **Personal harness improvement worksheet (5 questions)** provides decision data for which layers to invest in
- **Stop at Layer 3** for individual scale — past it, ROI cliffs and you're rebuilding Lopopolo's stack without his team
