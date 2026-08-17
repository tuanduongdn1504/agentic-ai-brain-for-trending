# (C) dsh-TUI — Pilot Methods Menu

**Honest count: 14 methods, not 24.** This is a presentation-layer plugin for a runtime the operator does not use. Most of the value is read-and-borrow; a padded menu would be dishonest. Methods are ordered by return-per-risk, and the ⭐ path is marked.

**Standing fence for everything below:** the host (`@deepseek-ai/dsh`) is a **four-day-old developer preview** that promises compatibility-breaking changes; dsh-TUI pins **21 peer deps at `^0.1.0-rc.6`**; the plugin has a `prepare` lifecycle script; the host's default models are DeepSeek's (**PRC cloud egress**); the surrounding ecosystem is ~1,120 unvetted plugins indexed by anonymous directories that publish the **wrong licence** for this very plugin. **NOT source-cloned** → treat the tree as untrusted.

---

## A — Read and learn (zero install, zero risk)

**⭐ A1. Read `docs/architecture.md` end to end.** ~20 minutes. The payoff is the seam discipline: what the plugin consumes (agent, model, tool, session, persistence), what it refuses to own (「不要在组件中复制 DSH Agent、session 或 tool 服务」), and how it reconstructs everything from the host's `session/event` log while keeping only a projection. This is the doc that makes the rest of the menu unnecessary.

**A2. Read the Claude-Code feature inventory** (§3 of the Deep Dive) as a competitor's checklist of what Claude Code's terminal UX does that was worth copying — streaming thought expansion, context-pressure bar, TPS/cache-hit/reasoning-level readouts, `Esc Esc` rewind-as-fork, structured tool cards, `@` refs, history search, `/resume` `/new` `/compact` `/export`. Then note where the imitation **stops**: `/vim`, `/connect`, `/hooks` ship as inert placeholders. The gap is as informative as the coverage.

**A3. Read the `verify:*` script list in `package.json`** (11 scripts). Ask one question of your own work: *which of my architectural claims are enforced by a build step, and which are just prose?*

**A4. Read the peer-dependency block as an architecture diagram.** 21 `@deepseek-ai/*` packages at `^0.1.0-rc.6` is a legible map of a frontier lab's agent-runtime decomposition — `dsh-agent`, `dsh-llm`, `dsh-session`, `dsh-skill`, `dsh-storage`, `dsh-terminal`, `dsh-user-approval`, `dsh-workspace`, `cordis`. Compare against your own mental model of where an agent should be cut. Composes with v235's `docs/capability-seams.md`.

---

## B — Borrow, zero install (the real return)

**⭐ B5. Write the invariant into hireui's LLM-integration ADR: *the event log is the source of truth; the UI holds only a projection.*** dsh-TUI proves a full interactive front end — history, streaming, time-travel, forking — can be built on nothing but an append-only event log. v235 supplied that invariant; v236 proves it is cheap rather than ceremonial. This is precisely what the **RATIFIED candidate-LLM legibility ADR** already demands of any hireui path touching a candidate (fixed, legible, audited, human-in-loop, eval-gated). Two consecutive ships converging on one rule is the strongest signal the corpus has produced this month.

**⭐ B6. Steal `verify:boundary` / `verify:patch-surface`: encode an architectural boundary as a CI gate.** The plugin does not ask to be believed about non-invasiveness — it fails its own build if it starts patching the host. Apply to hireui (e.g. "the candidate-facing path must not import the free-text LLM client") and, more pointedly, to the vault's own invariants. ⭐ Note this is the **third consecutive ship** offering machinery for the vault's unattended-staleness problem (v234 staleness tracking + recompilation, v235 doc-verification gates, v236 boundary gates) — the C22–C27 backlog has now been handed three tools in a row.

**B7. Borrow the observability readouts as a spec for any agent surface you build.** Context-window progress, TPS, cache-hit rate, reasoning level, token counts, live working status. Cheap to render, and they turn an opaque agent into a legible one. Composes with the `claude-api-cost-optimization` thread and the ccusage/OTel measurement layer.

**B8. Borrow "rewind is a fork, not a mutation."** dsh-TUI's double-Esc time-travel is implemented as a session **fork** off an event-log boundary — never an in-place edit. That is the same discipline as an `agent-*` branch, and the right shape for any hireui feature that lets a recruiter "undo" an AI action: branch the record, never rewrite it.

**B9. Borrow the honest-placeholder habit.** Shipping `/vim` `/connect` `/hooks` as declared-but-inert, and documenting them as such, is better practice than silently omitting them or faking them. Cheap credibility for the vault's own skills.

---

## C — Hands-on (optional, fenced, low value)

**C10. Inspect the published tarball without installing.** `npm view @deepseek-harness-tui/dsh-tui@0.8.0` and `npm pack --dry-run` to see the real file list, then read `bin/dsh-tui.js`. Confirms the `prepare` script's blast radius and whether anything unexpected ships. No global install, no execution.

**C11. If you must run it: scratch container only.** Pin `@deepseek-harness-tui/dsh-tui@0.8.0` and the exact `0.1.0-rc.6` peer set, `--ignore-scripts`, no real repository mounted, **route the model at Claude through the host's `llm-pi-ai` seam** (not the DeepSeek default — PRC egress), and expect it to break on the next `rc`. Value: seeing the CC-clone UX in motion. That is the whole return; weigh it against the setup.

**C12. Compare the two DeepSeek terminal experiences.** If C11 is done anyway, contrast dsh-TUI (a UI plugin *inside* a coding-agent runtime) with **DeepSeek-TUI v72** (`Hmbown` — a standalone terminal *client* for DeepSeek *models*). The delta is the whole client-vs-plugin, models-vs-runtime boundary that kept v236 out of v72's class.

---

## D — Explicit do-nots

**D13. Do NOT `npm i -g` on your working machine.** Global install + a release-candidate 21-package peer set + a `prepare` script + a preview promising breaking changes. There is no upside that justifies it.

**D14. Do NOT trust the DSH plugin directories, and do NOT install from them.** `dshhub.org` publishes this plugin as **v0.3.3 / BSD-3-Clause** against the repo's **v0.8.0 / MIT** — stale version *and* wrong licence. Eight-plus competing directories, several automated, none disclosing an operator, ~1,120 plugins indexed. Read the repo and the npm package; ignore the aggregators. (Repo authoritative — the Kilo Code v177 precedent.)

**D15. Do NOT point this, or the host, at candidate data.** Nothing here is a hireui component, and hireui stays hand-built per its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first).

---

## Not on the menu, and why

- **No "adopt as a daily driver."** It fronts a rival lab's preview runtime, not Claude Code.
- **No hireui feature.** A terminal UI for a coding agent has no recruitment-product surface.
- **No "contribute upstream."** The host is pre-1.0 and moving; a third-party UI plugin pinned to `rc.6` is not a stable place to invest.
- **No benchmark.** The plugin has no automated end-to-end tests with real credentials (author-stated: manual terminal verification), so there is nothing to measure that would mean anything.

---

**⭐ The whole menu in one line:** read `docs/architecture.md`, take *event-log-as-truth* into hireui's ADR and *boundary-as-CI-gate* into the vault, and leave the plugin uninstalled.
