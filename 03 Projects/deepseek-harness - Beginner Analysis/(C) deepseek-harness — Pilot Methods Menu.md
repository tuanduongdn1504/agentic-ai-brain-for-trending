# (C) deepseek-harness — Pilot Methods Menu

**Honest framing:** this is a **read-and-borrow** subject. `dsh` is a four-day-old developer preview whose own critics recommend waiting 3–6 months. There is no version of "adopt this into hireui" that is defensible today. What *is* valuable is unusually high: 453K lines and 1,386 decision records of a frontier lab's answer to *"what are an agent runtime's seams?"* — and two architectural ideas that transfer directly.

**16 methods, not a padded 24.** ⭐ = recommended path.

---

## A — Read & learn (zero install, zero risk)

**⭐ A1 — Read the capability-seam taxonomy.**
`docs/capability-seams.md`, `docs/architecture.md`, `docs/agent-lifecycle.md`, `docs/tool-execution-pipeline.md`. This is the payload: a frontier lab's enumeration of *where an agent runtime can be cut*. Even if you never run dsh, the seam list (models · tools · skills · sessions · sandboxes · storage · loops · scheduling · UI) is the best available checklist for "what should be swappable in an agent system." ~1–2h.

**A2 — Read `subagent-claude-code`.**
How a rival frontier lab embeds Claude Code as a delegatable child through Anthropic's **official Claude Agent SDK**, plus `packages/hooks/` bridging your real `hooks.json`. Directly on Goal #1: this is a competitor's read of what Claude Code's integration surface is *for*.

**A3 — Read the Cordis primer.**
`docs/cordis-primer.md` + `docs/cordis-tutorial/`. The disposability idea (`ctx.effect` reversible side effects + `ready`/`dispose`/`fork`) is the mechanism that makes "everything is a plugin" real rather than decorative. Transferable to any long-lived process you write.

**A4 — Read the postmortems.**
`docs/postmortem/` and `docs/defensive-patterns.md`. Rare: a shipped project publishing its own failure analyses.

**A5 — Read the critique, not just the repo.**
The 19%-ecosystem-compatibility figure, the ~10×-token-vs-Pi number and the 3-line `BENCHMARK.md` are the honest counterweight to a 138k-star launch. Practice: hold both.

---

## B — Borrow into your own work (zero install, highest ROI)

**⭐ B5 — Name your seams.**
Take A1's taxonomy and write hireui's own seam list: which parts of an LLM feature are swappable (model, prompt, tool set, storage, eval gate) and which are fixed. This composes directly with the standing **vendor-seam thread** — meetily v196 `generate_summary()`, AIRI v210 `xsAI`, lobehub v222, and now dsh's `llm` seam + `llm-pi-ai` adapter. Deliverable: a short seam spec in hireui's LLM-integration ADR.

**⭐ B6 — Steal "append-only session logs."**
dsh's rule — *anything visible to the model is permanently recorded* — is traceability as an **architectural guarantee** rather than a logging policy. That is almost verbatim the audit requirement in the **RATIFIED candidate-LLM legibility ADR**. Write it in as an invariant: hireui's candidate-facing LLM path records every prompt-visible token, append-only, before it is allowed to run.

**B7 — Consider Code Mode.**
Batching several tool calls into one TypeScript execution block instead of N round-trips. A real token-economy idea for the `claude-api-cost-optimization` thread. ⚠️ Weigh against the 10×-token critique — dsh is not evidence that its own techniques save tokens.

**B8 — Steal the doc-verification CI gates.**
`verify-doc-refs`, `verify-doc-budgets`, `verify-md-links`, `verify-doc-site-fragments`, `gen-*-catalog --check`. Machine-checked documentation freshness. ⭐ This is the **second consecutive ship** offering machinery for the vault's own stale-derived-artifact problem (agentic-local-brain v234's staleness-tracking + auto-recompilation). Together they are a pointed comment on the **C22–C27 stale-row backlog** and the deferred retire pass: the vault's lint duties are hand-run and overdue, and two independent subjects in a row have shipped the automation for exactly that.

**B9 — Steal the decision-record habit.**
1,386 decision records alongside the code. The vault already does this in `04 Reviews/`; dsh is a scale reference for what it looks like inside a codebase.

---

## C — Hands-on (scratch only, fenced)

**C10 — Run it once, in a throwaway directory.**
`npx @deepseek-ai/dsh web` → `http://127.0.0.1:3080`. Install-snapshot **first** (it has a `postinstall` that installs lefthook). Purpose: see the plugin tree and the web UI, not to do work.

**C11 — Point the pi-ai seam at Claude rather than the DeepSeek default.**
`llm-pi-ai` exposes Anthropic. This keeps a trial off DeepSeek's PRC-hosted inference and doubles as a check on whether the seam actually works end-to-end.

**C12 — Measure the token cost yourself.**
The single most decision-relevant number is the ~10×-vs-Pi claim, and it is unreplicated. One identical small task through dsh and through your normal Claude Code, with `ccusage`/OTel on both. If it reproduces, that settles adoption for a year.

**C13 — Try the Claude Code subagent path.**
Enable `subagent-claude-code` (off by default) on a scratch repo and watch dsh drive a real Claude Code child. This is the most interesting thing in the repo to *see* rather than read.

---

## D — hireui (Goal #2)

**D14 — Spec inputs only.** B5 (seam list) and B6 (append-only traceability) become lines in hireui's LLM-integration ADR on an `agent-*` branch, per hireui's CONSTITUTION (I-2 `agent-*` branch · I-8 operator-installs · GitNexus-first). hireui has no LLM spend yet, so this is design, not retrofit.

**⚠️ D15 — What NOT to do.** dsh is not a hireui dependency, not a candidate-facing runtime, and not a substitute for Claude Code. Developer preview + promised breaking changes + no eval harness + 19% ecosystem compatibility + PRC-default inference is a disqualifying combination for anything touching candidate data.

---

## F — Vault-meta

**⭐ F16 — File the two open pattern questions for the overdue audit.**
(1) Is deepseek-harness the **N=2 of §C row 102** (grok-build v215)? It meets every essential axis and differs only on two descriptive clauses ("terminal-TUI-first", "single-vendor-model") of the kind the v212 audit has generalized before — **and calling it N=2 fires that row's promotion-to-CONFIRMED trigger**, which is why this ship recorded it rather than executed it. (2) Or is it a new §C standalone ("Frontier-Lab Plugin-Composable Agent Runtime / Harness Kernel")? Also record the **#57 pi-ai dependency**, the **Pi-is-now-a-two-lab-dependency** observation, and the new **"harness delegation vs harness emulation"** watch axis.

---

## Fence (applies to every C-method)

`install-snapshot` before any install (there is a **`postinstall`**) · scratch directory only, never a real project · pin **`0.1.0-rc.5`** and expect it to break · BYO key; prefer routing pi-ai at Claude over the **DeepSeek default (PRC cloud egress)** · **never point it at candidate or client data** · **never** enable self-modifying toolsets · check which sandbox backend engages on your platform (**Windows leaves reads, network and process visibility unrestricted**) · **NOT source-cloned** → treat the 219-package tree as untrusted until inspected · hireui stays hand-built per its CONSTITUTION.
