# hireui translation

> How Herdr maps to the operator's Goal-#2 target, **hireui** (TalentAxis recruitment SaaS). Companion to the operator's `multi-agent-orchestration` and `loop-engineering` pilot threads.

## Framing: Herdr is an OPERATOR tool, not a product feature

Herdr runs on **your** dev machine to orchestrate **your** coding agents. It is **not** a candidate-facing feature and never should be. That means:

- ✅ It does **not** touch the **hireui candidate-LLM legibility ADR** (RATIFIED) — that ADR governs candidate-facing LLM paths; Herdr is a local terminal for the operator. No EU-AI-Act Annex III surface here.
- ✅ AGPL copyleft does **not** infect hireui: using Herdr as an **unmodified local dev tool** to build software imposes **no** obligation on that software. (Only forking/embedding/network-serving Herdr itself triggers AGPL — see [[license-and-adoption-caveats]].)

So the whole translation is at the **operator-workflow / harness-engineering** layer, not the product layer.

## BORROW (ideas, not code)

| Idea | From Herdr | Apply to hireui workflow |
|---|---|---|
| **Socket-API agent orchestration** | Agents spawn panes, read output, wait on each other via a pure socket API | The cleanest expression yet of "agents coordinating agents." Reference model for the operator's `multi-agent-orchestration` pilot and for how a hireui recruitment-agent feature might one day sequence sub-agents — **as a design pattern**, kept legible + human-gated per the ADR. Do **not** vendor Herdr's AGPL code. |
| **Zero-config state detection** | Foreground-process + TOML-manifest-vs-screen-snapshot → idle/working/blocked | Pattern for observing a long-running agent's state from its **output** rather than bespoke callbacks — relevant to the `loop-engineering` v189 babysitter and any future multi-LLM monitoring. |
| **Persistent detach/reattach sessions** | Server survives client detach; resume over SSH | Architectural precedent for "detach a running loop, reattach later" — the v189 loop already resumes; Herdr shows the mature version of the pattern. |

## PILOT — one concrete, low-risk experiment

**Run Herdr locally as the orchestration surface for the multi-agent hireui dev loop.**

- **Setup (~15 min):** `brew install herdr`; open one workspace for the hireui repo.
- **Panes:** Claude Code (feature work) · a GitNexus-MCP / git-monitor pane · a Figma-MCP / design-check pane · the **v189 loop-engineering** background-task loop (`pilot/v189-loop-a3-b5`). The agent sidebar shows which is blocked/working at a glance.
- **Test:** detach (`ctrl+b q`), close the laptop lid, reattach — confirm the v189 loop + agents survived. This is the "persistence" value proposition against the operator's actual workflow.
- **Measure:** does the unified agent-state view + persistence meaningfully reduce context-switching vs the current N-terminals setup? One week, note it in `04 Reviews/`.
- **Fit:** **HIGH** as an *operator-UX* pilot; composes with existing pilots rather than replacing them. This is the natural "visible orchestration layer" under the **cc-sdd (adversarial review) + loop-engineering v189** compound pilot.

**Lower-priority pilot:** multi-reviewer orchestration (parallel adversarial reviewers in separate panes). **Fit MEDIUM-LOW** — cc-sdd (v61) already does framework-level adversarial review, and the current hireui loop is sequential (plan→code→review→QA). Defer until a genuinely *parallel* multi-reviewer workflow exists; Herdr adds little to a sequential one.

## AVOID

| Don't | Why |
|---|---|
| Expose Herdr to candidates or put it in the hireui product | It's a dev tool; candidates see the hireui SPA only. Keeps you clear of the candidate-LLM ADR entirely. |
| Vendor / embed Herdr's code into hireui | AGPL copyleft. Borrow the socket-API **pattern**, not the source. |
| Bet on the plugin ecosystem | Young, community-maintained, no hireui-specific plugins. Rely on the socket API only. |
| Windows-first reliance | Herdr Windows is beta (open bug #1514). Use macOS/Linux for operator work. |
| Treat status detection as ground truth | Documented status-latch bugs (#198 etc.) — the sidebar is a convenience, not an authority. |

## Next action

Run the **HIGH-fit operator-UX pilot** above for one week alongside the v189 loop, then log a short verdict in `04 Reviews/`. If it earns its keep, document Herdr in the hireui `CLAUDE.md` as a **recommended local dev tool** (explicitly *not* a product dependency, per the AGPL note). Revisit the socket-API pattern when the `multi-agent-orchestration` pilot next advances.

## Related
- [[architecture-and-detection]] · [[license-and-adoption-caveats]] · [[competitive-landscape]]
- [[external|Storm Bear: multi-agent-orchestration]] · [[external|Storm Bear: loop-engineering v189]]
