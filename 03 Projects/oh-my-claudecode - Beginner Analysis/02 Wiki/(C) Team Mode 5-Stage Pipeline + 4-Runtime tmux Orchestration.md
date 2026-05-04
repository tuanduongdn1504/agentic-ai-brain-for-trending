# (C) Team Mode 5-Stage Pipeline + 4-Runtime tmux Orchestration

> **Type:** Entity — methodology + architecture
> **Parent:** [[(C) index]]
> **Sources:** README Team section + CHANGELOG v4.4.0 + v4.13.1 + CLAUDE.md `<team_pipeline>`
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

OMC's **Team mode** is the canonical orchestration surface (v4.1.7+) — a **staged 5-stage pipeline** (`team-plan → team-prd → team-exec → team-verify → team-fix`) that runs either as **native Claude Code agent teams** (in-session, `/team`) or as **tmux CLI workers** (terminal, `omc team`) supporting **4 first-class AI runtimes**: Claude + Codex + Gemini + Cursor-agent (v4.13.1). First corpus framework with 4-runtime first-class orchestration.

## 2. 5-stage pipeline (canonical)

Stages fire sequentially with fix-loop feedback:

```
team-plan → team-prd → team-exec → team-verify → team-fix (loop back to exec)
```

| Stage | Purpose | Typical agent |
|-------|---------|---------------|
| **team-plan** | Task decomposition, scope, sequencing | `planner` (opus) |
| **team-prd** | Requirements doc, acceptance criteria | `analyst` (opus) |
| **team-exec** | Implementation | `executor` (sonnet/opus) |
| **team-verify** | Evidence-driven verification | `verifier` (sonnet) or `code-reviewer` (opus) |
| **team-fix** | Address verification failures, loop back to exec | Same agents, bounded max-attempts |

**Fix loop** bounded by max attempts. `team ralph` links both modes (Ralph persistence + Team pipeline).

**Parallel agents per stage:** `/team 3:executor "fix all TypeScript errors"` spawns 3 executor agents in parallel.

## 3. Team native vs team CLI distinction

OMC exposes **two surfaces with same pipeline semantics**:

| Surface | Runtime | Invocation | Best for |
|---------|---------|-----------|----------|
| **Native (in-session)** | Claude Code native agent teams | `/team 3:executor "task"` | Coordinated Claude-only work |
| **CLI (tmux)** | Real `claude`/`codex`/`gemini`/`cursor-agent` processes in split panes | `omc team 2:codex "task"` | Multi-runtime work, cross-validation |

**Native requires config** in `~/.claude/settings.json`:
```json
{"env": {"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"}}
```

**CLI requires** `codex`/`gemini`/`cursor-agent` CLIs installed + active tmux session.

If teams disabled, OMC warns and falls back to non-team execution where possible.

## 4. 4-runtime first-class orchestration

### v4.0 — Claude only
Initial release, native Claude Code

### v4.4.0 — Removed Codex/Gemini MCP servers, added CLI-first
> **v4.4.0 removes the Codex/Gemini MCP servers** (`x`, `g` providers). Use the CLI-first Team runtime (`omc team ...`) to spawn real tmux worker panes.

This pivoted OMC from **MCP server architecture** to **tmux CLI worker architecture** — arguably a courageous downshift choosing CLI tooling over the emerging MCP standard.

### v4.13.1 — Cursor-agent 4th runtime
> **feat(team): Add cursor-agent as 4th tmux worker type (executor-only)** (#2736)

Cursor IDE agent added as tmux worker. Executor-only (not full pipeline-spanning).

### Worker spawn mechanics

Workers **spawn on-demand, die when task completes** — no idle resource usage.

```
omc team 2:codex "review auth module for security issues"
omc team 2:gemini "redesign UI components for accessibility"
omc team 1:claude "implement the payment flow"
omc team 1:cursor-agent "fix type errors in components/"
omc team status auth-review
omc team shutdown auth-review
```

## 5. Pattern #56 Multi-Runtime Orchestration candidate

**Definition:** Framework treats multiple AI CLI tools as first-class runtime workers orchestrated in tmux panes (vs provider abstraction or single-runtime).

**Observed at N=1 (OMC v27):**
- Claude Code CLI
- Codex CLI (OpenAI)
- Gemini CLI (Google)
- Cursor-agent CLI

**Distinct from Pattern #28 Multi-Provider AI Support (confirmed v25):**
- #28 = abstraction layer (LiteLLM 100+ providers; TrendRadar v19, Skyvern v24, HF agents-course v26)
- **#56 = runtime-level multi-CLI orchestration** (spawn real processes, not abstraction calls)

**Pattern #56 candidate** — will validate at N=2 when next framework adopts multi-runtime CLI orchestration (candidates: awaiting).

## 6. CCG tri-model synthesis

OMC `/ccg` skill = 3-model consensus via `/ask codex` + `/ask gemini` + Claude synthesis:

```
/ccg Review this PR — architecture (Codex) and UI components (Gemini)
```

Routing:
- Codex = architecture + security angle
- Gemini = UI + large-context angle (1M token)
- Claude = synthesis + final output

**Cost note from README:** "3 Pro plans (Claude + Gemini + ChatGPT) cover everything for ~$60/month."

## 7. Comparison: T1 orchestration approaches

| Framework | Orchestration mode | Runtime | Multi-AI |
|-----------|-------------------|---------|----------|
| ECC v1 | Feature-based commands | Claude Code native | No |
| Superpowers v2 | 7-stage workflow methodology | Claude Code native | No |
| gstack v3 | Virtual engineering team metaphor | Claude Code native | No |
| GSD v5 | SDD workflow (context-rot spec) | 14+ AI harnesses abstract | Abstract/multi |
| BMAD v11 | 12+ agents + 5 modules + party mode | Claude Code + others | Limited |
| codymaster v12 | 79 skills + 11 commands + 8+ platforms | Multi-platform | No explicit |
| spec-kit v17 | SDD 7-step + 30+ agents | 30+ agents | Broad |
| agency-agents v18 | 144 personalities + 12+ divisions | Shell scripts + Claude | Limited |
| **OMC v27** | **5-stage Team pipeline + 8 modes + tmux workers** | **4 native CLIs** | **First-class 4-runtime** |

**OMC uniqueness at v27:** Only T1 with tmux CLI worker architecture + 4-runtime first-class + staged pipeline with bounded fix-loop.

## 8. Ralph mode (persistent verify/fix)

Named after Mitchell Hashimoto's "ralph wiggum" coding style — persistent, won't-give-up execution.

**Ralph includes Ultrawork** — when activated, auto-includes parallel execution.

Use case: Tasks that **must complete fully** — no silent partials. Contrast Autopilot (can give up if stuck) and Ultrawork (parallel burst may miss edge cases).

## 9. Ultrawork vs Team vs Ralph decision matrix

| Use case | Recommended mode |
|----------|-----------------|
| Coordinated work across agents with verification | **Team** (canonical) |
| Burst parallel fixes/refactors, no team coordination needed | **Ultrawork** |
| Task MUST complete, no partials accepted | **Ralph** |
| End-to-end feature with minimal ceremony | **Autopilot** |
| Codex + Gemini mixed work | **omc team** (CLI) or **/ccg** |
| Strict multi-step transformation ordering | **Pipeline** |

## 10. tmux platform support

OMC + tmux requirement dependency chain:

| Platform | tmux provider | Install |
|----------|---------------|---------|
| macOS | tmux (BSD/GNU) | `brew install tmux` |
| Ubuntu/Debian | tmux | `sudo apt install tmux` |
| Fedora | tmux | `sudo dnf install tmux` |
| Arch | tmux | `sudo pacman -S tmux` |
| **Windows native** | **psmux** (first Windows-native) | `winget install psmux` |
| Windows WSL2 | tmux inside WSL | `sudo apt install tmux` |

**psmux** = 76 tmux-compatible commands, native Windows binary, no WSL required. **First Windows-native tmux-alternative in Storm Bear corpus.**

## 11. Related concepts

- [[(C) Cluster — README + Team mode + 8 orchestration modes]]
- [[(C) Cluster — AGENTS.md + 19 agents + child-agent protocol + tools]]
- [[(C) 5-Source Multi-Lineage + Recursive Corpus Reference + Pattern 57 Candidate]]
- Pattern #18 Agent Runtime Standardization (confirmed v15; 6th data point at v27)
- Pattern #28 Multi-Provider AI Support (confirmed v25; distinct from #56)
- **Pattern #56 Multi-Runtime Orchestration Meta-Framework** (NEW candidate at v27)

## 12. References

- README.md (Team section, tmux workers section)
- CHANGELOG.md (v4.4.0, v4.13.1 entries)
- CLAUDE.md `<team_pipeline>` block
- docs/REFERENCE.md (per-role provider/model routing)

## 13. Edges + limitations

- **4-runtime coordination overhead** — spawning Codex/Gemini/Cursor CLIs requires per-runtime auth + config
- **tmux dep** blocks users without tmux access (especially Windows without psmux)
- **Executor-only cursor-agent** (v4.13.1) — not full pipeline-spanning; may limit Cursor team usage
- **CCG $60/month baseline** — 3 Pro subscriptions cost floor
- **MCP servers removed v4.4.0** — CLI-first pivot may leave MCP-stack users stranded (though MCP support via `.mcp.json` remains at project level)
- **Fix-loop bounded** — unclear what happens after max-attempts exhaustion (partial success? silent failure? explicit error?)

---

**Team Mode = canonical OMC orchestration surface with 5-stage pipeline + 4-runtime first-class support. Pattern #56 candidate registered. First corpus framework combining staged pipeline + multi-runtime tmux CLI workers.**
