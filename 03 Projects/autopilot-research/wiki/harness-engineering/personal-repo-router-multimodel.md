# Personal-repo extension — router-mediated multi-model with built-in sub-agent

> **Source:** howznguyen — [Kết hợp Opus + GPT trong Claude Code bằng Router và Sub-agent](https://howznguyen.dev/blog/router-opus-gpt-subagent-workflow), 2026-05-19, Vietnamese, ~20 min read
> **Raw:** `raw/2026-05-19-howznguyen-router-opus-gpt-subagent.md`
> **Compiled:** 2026-05-20
> **Status:** N=1 single-source extension to [[personal-repo-overview|individual-scale layer]]; not a new anchor. Distinct contribution: concrete router-mediated multi-provider setup playbook for Claude Code's 3-slot model config (opus/sonnet/haiku).

This article extends the [[personal-repo-overview|individual-scale]] sub-thread with a **specific architectural pattern** that none of the prior 6 personal-repo sources covered explicitly: **using Claude Code's built-in sub-agent feature combined with a router to drive two different model providers — Opus from Kiro as the supervisor, GPT-5.5 from Codex as the executor — through Claude Code's 3 fixed model slots.**

The pattern is corpus-first as an explicit setup playbook with config-level concrete examples. Prior personal-repo coverage of multi-Claude (e.g., [[personal-repo-patterns|sub-agents technique]]) treated sub-agents as same-vendor parallelism; howznguyen's contribution is cross-vendor parallelism via routing infrastructure that exploits an undocumented quirk of Claude Code's config schema.

---

## The load-bearing infrastructure quirk

Claude Code's `~/.claude/settings.json` exposes exactly **three model slots** by name: opus, sonnet, haiku. These are not arbitrary — they are the only valid model-class identifiers in the config schema:

```json
{
  "ANTHROPIC_BASE_URL": "http://127.0.0.1:20128/v1",
  "ANTHROPIC_AUTH_TOKEN": "YOUR_ROUTER_API_KEY",
  "ANTHROPIC_DEFAULT_OPUS_MODEL": "kr/claude-opus-4.6",
  "ANTHROPIC_DEFAULT_SONNET_MODEL": "cx/gpt-5.5",
  "ANTHROPIC_DEFAULT_HAIKU_MODEL": "cx/gpt-5.5"
}
```

The undocumented opportunity: **point each slot at an arbitrary model behind a router**. The slot names become role assignments rather than literal model identifiers:

| Slot | Author's role mapping | Model behind router |
|---|---|---|
| `opus` | Supervisor (planner / reviewer / context-owner) | Kiro Opus 4.6 (`kr/claude-opus-4.6`) |
| `sonnet` | Sub-agent default executor | Codex GPT-5.5 (`cx/gpt-5.5`) |
| `haiku` | Lightweight tasks | Codex GPT-5.5 (`cx/gpt-5.5`) |

When the user invokes `spawn agent sonnet` (or Opus internally chooses to delegate), Claude Code dispatches to whatever model the sonnet slot has been configured to — bypassing any assumption that "sonnet" means Anthropic Sonnet.

Combined with Claude Code's built-in sub-agent support — *"sub-agent là tính năng có sẵn trong Claude Code. Bạn không cần cài plugin, không cần MCP server riêng, không cần script wrapper"* — the operator gets cross-vendor delegation **with zero plugin or MCP infrastructure**, only a router process.

---

## Why this pattern (operator's stated motivation)

At the post's opening the author enumerates 3 pain points from single-model-does-everything:

1. **Credit waste.** Opus is wasted on rename / add-test / type-fix / lint-run / format work that needs no deep reasoning.
2. **Context drift on long tasks.** Even strong models lose mid-conversation constraints when conversations grow long, many files are read, and many small decisions accumulate.
3. **Speed.** Some tasks don't need "thinking deep" — they need fast + accurate + instruction-following.

Resolution: split roles. Author's terse summary — **"Opus think big, GPT do fast."**

The trade-off framing is consistent with [[contrarian-stances|Lopopolo's stance on credit allocation]] but operates at consumer scale. Where Lopopolo's [[core-claims|$2-3K/day token cost]] is the org-scale operating point, howznguyen's "tốn credit" is the consumer-scale operating point — different absolute budget, same allocation logic.

---

## The 4 ecosystem components

| Component | Author's choice | Equivalent alternatives noted in post |
|---|---|---|
| **Router / Proxy** | 9Router | OmniRoute, CLI API Proxy, "any proxy with Anthropic/OpenAI-compatible endpoint" |
| **Supervisor model source** | Kiro (Opus 4.6) | Any provider exposing Opus-class model |
| **Executor model source** | Codex (GPT-5.5) | Any provider exposing GPT-class model |
| **Context / handoff store** | Knowns (MCP-based project memory) | Backlog.md, `TODO.md`, `tasks.md`, `docs/`, `decisions.md`, Notion/Linear/Jira |

This 4-component stack is positioned as **tool-agnostic** — the author repeatedly emphasizes that 9Router, Kiro, Codex, and Knowns are his choices but interchangeable: *"Đừng cố chấp vào một tool duy nhất. Hệ thống tốt là hệ thống giúp supervisor agent giữ context đúng, không phải hệ thống có tên nghe xịn nhất."*

---

## File-based handoff between sub-agent phases

A corpus-first concrete primitive surfaced in this post: **markdown files as inter-agent handoff artifacts.** Pattern:

Phase 1 sub-agent writes to a file:
```
spawn agent sonnet
Research database usage tracking. Write findings to .agent/notes/billing-research.md
Include: current schema, what's tracked, what's missing, suggested additions.
```

Phase 2 sub-agent reads from that file:
```
spawn agent sonnet
Backend implementation for billing usage feature.
Read .agent/notes/billing-research.md for context.
Implement following the gaps and suggestions listed there.
```

Conventions observed in the post:
- `.agent/notes/` or `.agent/handoff/` folder
- `.gitignore` if not commit-worthy
- One file per phase / per domain

This converges with [[external|agent-development-lifecycle/langchain-interrupt-26-anchor|LangSmith Context Hub]]'s framing of agents.md / skills as memory layer, but at a different abstraction level: Context Hub centralizes; howznguyen's `.agent/notes/` is per-task-ephemeral. Both reduce the supervisor's context-window pressure.

Compare with [[personal-repo-patterns|the existing 12-technique catalog]]: the `progress.md` / `#`-corrections / `/context` audits patterns already gesture at file-as-context, but none specify the **inter-phase sub-agent handoff** discipline as a discrete pattern with conventions.

---

## Task-allocation rubric (concrete and actionable)

The post's most reusable contribution is a 3-bucket rubric for which model handles what:

### Opus (supervisor) — should handle

- Ambiguous requirement analysis
- Architecture reading
- Risk-finding
- Task decomposition
- Implementation-order decisions
- Code review
- Drift detection
- Multi-source context synthesis
- Spec / plan writing
- Hard-bug solving
- Trade-off decisions

### GPT sub-agent (executor) — should handle

- Single-function implementation
- Adding tests
- Type updates
- Lint fixes
- Small refactors
- Simple config migrations
- Pattern-following component additions
- Outline-driven docs
- API-usage search across repo
- Specific file-group inspection

### Sub-agent should NOT handle (without supervisor plan)

- Large architecture changes
- New database schema decisions
- Public API changes
- Cross-module refactors
- Code deletions
- Security-sensitive flow modifications
- Multi-agent output merging
- Product trade-off decisions

The "should NOT" bucket is what makes the rubric load-bearing — it explicitly defines where supervisor authority is non-delegable, preventing the runaway-sub-agent failure mode.

---

## Parallel-research-then-implement pattern

The post documents a 3-stage workflow that's distinct from naive parallel-sub-agents:

1. **Opus analyzes brief alone** — produces feature analysis with phases + dependencies + parallelism opportunities
2. **Parallel research sub-agents** — each scoped to one domain (database / frontend / API / etc.), each writes findings to a `.agent/notes/<domain>-research.md`
3. **Opus reviews research files + spawns implementation sub-agents** — implementation agents read their domain's research file plus only their own implementation scope

This is a corpus-first explicit articulation of a **research-then-implement** sub-agent staging discipline. Prior personal-repo coverage of parallelism focused on git-worktree concurrent edits; howznguyen's pattern is single-worktree sequential-phases with parallel-within-phase.

Convergence flag: [[external|agent-development-lifecycle/langchain-interrupt-26-anchor|LangChain's Deep Agents]] supports the same parallel-sub-agent staging at framework level; howznguyen achieves equivalent capability with `spawn agent sonnet` alone (no Deep Agents needed). Two independent paths to similar capability.

---

## Cross-link mapping

### Where this CONVERGES with prior corpus anchors

- [[external|harness-engineering/anchor-bundle-overview|Lopopolo (org-scale)]]: same supervisor-delegates-to-executors pattern, but Lopopolo's executors are humans + Symphony processes; howznguyen's executors are GPT sub-agents
- [[personal-repo-patterns|Existing 12 individual-scale techniques]]: extends the "sub-agents" technique with specific cross-vendor + handoff-file conventions
- [[tejas-kumar-anchor|Tejas Kumar's harness primitives]]: this pattern is an applied case of Tejas's [[tejas-kumar-anchor#The 5-component definition (load-bearing)|5-component harness]] — Claude Code provides components 1-5 (tool registry / model / context / guardrails / loop), howznguyen adds component 6 (verify-via-supervisor-review) plus an **inter-model orchestration layer** Tejas didn't enumerate
- [[external|agent-development-lifecycle/langchain-interrupt-26-anchor|LangChain Deep Agents]]: same supervisor + sub-agent + delegation pattern, but framework-level vs config-level. Howznguyen's path requires no Deep Agents installation — only router + settings.json

### Where this DIVERGES from prior corpus anchors

- **Cross-vendor by design.** Most prior individual-scale sources stay within a single vendor (Anthropic via Claude Code). Howznguyen explicitly routes opus-slot to Kiro and sonnet-slot to Codex — making cross-vendor parallelism the default mode of operation.
- **No CLAUDE.md emphasis.** Tù Bà Khuỳm's anchor (and 5 of 6 supporting English-language YouTube sources) treats CLAUDE.md as load-bearing; howznguyen barely mentions it, focusing instead on `~/.claude/settings.json` routing + file-based handoff. Different load-bearing-primitive identification within the same individual-scale operating point.
- **Task-allocation rubric is more crisp than prior sources.** The "should NOT do without supervisor plan" bucket is explicitly enumerated — most prior sources gesture at this but don't formalize it.

### New cited references

- **9Router** (https://9router.com) — author's primary router choice; local proxy port 20128
- **OmniRoute** (https://omniroute.online) — alternative
- **CLI API Proxy** — alternative (no URL given)
- **Kiro** — provider exposing Claude Opus 4.6 via API (already in [[cited-references]] from the v61 wiki via Pattern Library cross-reference; this post grounds it operationally)
- **Codex** — provider exposing GPT-5.5 (cross-link to [[external|codex/_index|codex topic]])
- **Backlog.md** (https://github.com/MrLesk/Backlog.md) — markdown task management
- **Knowns** — MCP-based project memory system (no URL given in post)

---

## Operator caveats / open questions

1. **Router latency overhead.** Adding a local proxy introduces 1-2ms per call + bandwidth-doubling on the local network. Not quantified by howznguyen. Worth pilot measurement.
2. **Auth-proxy stance unclear.** [[tejas-kumar-anchor|Tejas's auth-proxy pattern]] (secrets in harness, not agent) doesn't appear in howznguyen's setup — sub-agent inherits Claude Code's full filesystem + secrets access. Different security posture; worth tracking which becomes the prevailing pattern.
3. **9Router itself is a black box.** No mention of its open-source status, pricing model, or audit-ability. If pilot-deploying this pattern, the router process becomes a privileged piece of operator infrastructure handling all Anthropic+OpenAI tokens. Cross-reference with [[external|claude-code-clones/_index|free-claude-code (Storm Bear Pattern Library v60)]] which similarly routes between providers — different posture (free-claude-code is OSS-self-hosted; 9Router posture undocumented in this post).
4. **`spawn agent sonnet` syntax.** The post asserts this is built-in Claude Code syntax. Worth independently verifying — current Claude Code docs may use different invocation grammar.
5. **3-slot exploitation longevity.** If Anthropic adds a 4th model class (e.g., a future "novella" slot) or revises the schema to enforce vendor identity per slot, this pattern breaks. The pattern's load-bearing-ness depends on Anthropic NOT closing this configuration loophole.
6. **Pricing math not provided.** Author claims credit savings without quantifying. A pilot with 30-day before/after measurement would corroborate.

---

## Pilot-readiness assessment

This pattern is **Tier-A operationally pilotable**:

- Setup time: ~1 hour (install router, configure settings.json, restart Claude Code, smoke-test with simple `spawn agent sonnet` call)
- Reversibility: full (delete settings.json overrides, kill router process)
- Pre-requisites: existing Kiro + Codex accounts (or equivalents)
- Measurement plan: 30-day before/after on (a) credit consumption (b) average task completion time (c) task-completion correctness rate

If running this pilot, recommended journal entries:
- `04 Reviews/(C) YYYY-MM-DD-router-multimodel-pilot.md` per Storm Bear convention
- Cross-link to this article in the review

---

## Cross-links

- [[_index|harness-engineering index]]
- [[personal-repo-overview]] — the individual-scale anchor this article extends
- [[personal-repo-patterns]] — 12-technique catalog (this is technique #13 by extension)
- [[personal-repo-vs-org-scale]] — axis-by-axis comparison; howznguyen's pattern fits "tactical workflow" axis
- [[personal-repo-gaps]] — open questions (#1, #2, #5 above are candidates for that gap-list)
- [[tejas-kumar-anchor]] — definitional 5-component harness; howznguyen is an applied case
- [[external|agent-development-lifecycle/langchain-interrupt-26-anchor]] — Deep Agents = same supervisor/sub-agent pattern at framework level
- [[external|codex/_index]] — GPT-5.5 via Codex is the executor source in this pattern
- [[external|claude-code-clones/_index]] — 9Router-class proxies are a sibling category to claude-code-clones (router-for-frontier-models vs clone-of-Claude-Code)
- [[external|claude-md-12-rules/_index]] — howznguyen's task-allocation rubric is a workflow-level extension of the 12-rule discipline
