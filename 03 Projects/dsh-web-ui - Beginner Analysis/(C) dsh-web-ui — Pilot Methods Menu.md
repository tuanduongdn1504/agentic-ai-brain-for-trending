# (C) dsh-web-ui — Pilot Methods Menu

**Wiki v239 · `zhu1090093659/dsh-web-ui`**
**Headline: ⚠️ read-and-borrow. Do NOT install. NOT a hireui component.**

An honest menu — most entries are *read*, *borrow*, or *don't*. Nine methods, not a padded twenty-four. Ranked by value per unit of risk.

---

## Why not install

Five independent reasons, each sufficient on its own:

1. **It is a plugin suite for a rival lab's agent runtime** at `0.1.0-rc.7`, which shipped **yesterday** and promises breaking changes. Nothing here runs under Claude Code.
2. **v0.2.0 on a ~6-day-old repo**, 21 npm versions in five days. Nothing has settled.
3. **`dsh-ssh` is a genuine hazard** — see §D14 below.
4. **Licence mixing blocks commercial use wholesale**: CC BY-NC-SA-4.0 on the `maid-atelier` skin, plus skins literally named `minecraft` and `miku`.
5. **The one-line aggregate install transitively pulls `cloudflared`**, whose `postinstall` downloads a Cloudflare tunnel binary from a single-maintainer package.

If you install anything anyway: **never `dsh-ssh` against production**, never the aggregate on a machine holding real credentials, and run `install-snapshot` first.

---

## ⭐ The recommended chain: A1 → B5 → C11

### A1 — Read three files (~30 minutes, zero install) ⭐ START HERE

| File | Why |
|---|---|
| [`scripts/verify-docs.mjs`](https://github.com/zhu1090093659/dsh-web-ui/blob/main/scripts/verify-docs.mjs) | **The single most directly applicable artefact any of the last five ships has offered.** A documentation linter: required file triplets per unit, translation pairing by **git blob hash**, markdown link validation, heading structure, no-scaffold-placeholder, with a `--write` repair mode. |
| [`.github/pull_request_template.md`](https://github.com/zhu1090093659/dsh-web-ui/blob/main/.github/pull_request_template.md) | The **required AI-authorship disclosure** field — three checkboxes plus "which model" and "which agent tool" (Claude Code named). |
| [`packages/dsh-liangshen/README.zh.md`](https://github.com/zhu1090093659/dsh-web-ui/blob/main/packages/dsh-liangshen/README.zh.md) | The downstream half of the v238 story — read it **against** v238's issues #60 / #51 / #65. |

**Read it as a mirror, not a tutorial.** The project mechanises every invariant its build can see, and its human-written prose has already drifted in four places.

### B5 — Write the vault doc-lint spec into `CLAUDE.md` (~1 hour, zero install) ⭐

A short, explicit contract for the vault's own documentation set — the thing this project has and the vault does not:

- **Required-file rules** — every `03 Projects/<subject> - Beginner Analysis/` carries the four expected docs.
- **Index ↔ content agreement** — a `_state/` filename label must not disagree with what the file holds. *(The live bug: `03c-projects-v61-v183.md` holds entries through v239.)*
- **Dead-link validation** — markdown links and `[[wikilinks]]` must resolve. *(v238's subject linked a `HANDOFF.md` that did not exist; the vault should not be able to do the same silently.)*
- **Chapter-size cap** — no `_state/` chapter over the 35K-token discipline; no shim over the subagent-context floor. **This is load-bearing infrastructure, not hygiene** — v238 proved it by breaking the `Workflow` tool, and this ship proved the fix by using it.
- **Stale-row floors** — any §C row past both §28.3/§39 floors is flagged, not silently carried. *(C22–C27.)*
- **Count reconciliation** — a §C count in prose must equal the §C table's row count.

### C11 — Implement `verify-vault-docs` (~half a day) ⭐ THE PAYOFF

Turn B5 into a script that **fails** on each of those conditions. This is the **C22–C27 retire-pass problem, mechanised** — and five consecutive ships have now handed over the parts:

| Ship | Part contributed |
|---|---|
| v234 agentic-local-brain | staleness tracking + automatic recompilation |
| v235 deepseek-harness | doc-verification gates (`verify-doc-refs` / `verify-doc-budgets` / `verify-md-links`) |
| v236 dsh-TUI | CI-enforced architectural boundary (`verify:boundary` / `verify:patch-surface`) |
| v237 DSH-better-sidebar | pack → mount into a real host → headless-render |
| **v239 dsh-web-ui** | **documentation integrity — triplets, blob-hash pairing, links, placeholders, counts** |

The vault has taken the *idea* five times and built it zero times. This is the ship where the idea arrives as a readable ~200-line script.

---

## Also worth borrowing

### B6 — Adopt an AI-authorship disclosure field in hireui's PR template (~20 minutes) ⭐

Three checkboxes — fully AI-coded / partially AI-assisted / no AI — plus **which model** and **which agent tool**. Near-zero cost, and it answers a question that will matter more every quarter: *for this change, what wrote it and what reviewed it?*

⚠️ **Borrow the field; do not borrow the enforcement severity.** This project's `pr-review.mjs` **auto-closed issue #532** — a substantive bug report with root-cause analysis — for template non-compliance. Make the field required for *merge*, never a trigger for *auto-closing an issue*.

### B7 — Steal the fail-closed scheduling contract for any hireui scheduled LLM job (~1 hour)

Five rules, verbatim from the task board's behaviour:

1. Every run gets its **own session** — no shared state between runs.
2. **Pin workspace + preset + permission and apply them *before* the prompt** is sent.
3. **Fail closed** — a missing workspace, missing preset, or rejected permission aborts *before* the prompt reaches the model.
4. **Skip, do not queue** — a missed occurrence is skipped, never backfilled. (Backfill storms are how scheduled agents produce surprise bills.)
5. **Never overlap** — a run in progress skips its due occurrence.

Composes with **loop-engineering v189**'s budget kill-switch and **ClawWork v233**'s fails-closed eval gate. Running theme across four ships: *evaluation* fails closed (v233), *ingestion* fails soft (v234), *runtime* fails soft while *config* fails fast (v238), **scheduling fails closed (v239)**.

### D14 — Write the tool-layer gating rule into the hireui LLM ADR (~30 minutes) ⭐

> **An agent that can reach production must be gated at the tool, not at the prompt.**

`dsh-ssh` is the counter-example, source-verified: six tools registered into the agent (`ssh_list`, `ssh_exec`, `ssh_upload`, `ssh_download`, `ssh_tunnel`, `ssh_cluster`), `ssh_exec` taking an arbitrary command, with **no allowlist, no approval gate, no audit log, no output redaction, no read-only mode**, and passwords plus key passphrases written **plaintext** to `~/.dsh/dsh-ssh.json`.

The **reference implementation is already in the corpus**: **tabularis v212** put the same secret class in the **OS keychain** and gated its agent surface with **read-only mode + approval gates + a pre-flight EXPLAIN that fails closed on stacked statements.** Cite both in the ADR — the wrong way and the right way, one ship apart.

This extends the **RATIFIED candidate-LLM legibility ADR** from *legibility* to *reach*.

### B8 — Note the supply-chain hygiene worth copying (~15 minutes)

`pnpm-workspace.yaml` carries an explicit **`allowBuilds` lifecycle allowlist** and a **`minimumReleaseAgeExclude`** list, and the aggregate pins all 14 dependencies **exactly**. That is **the pi v228 hardening playbook**, independently arrived at — a second corpus instance. Worth mirroring in hireui's `pnpm`/`npm` config regardless of anything else here.

---

## Read-only curiosities

### A2 — The anchor gate, as a lesson in fragility (~10 minutes)

`dsh-liangshen` decides whether the model's reasoning is "on the right trajectory" by testing whether the chain-of-thought matches `/\bwe\b/gi` **and** contains no `/\blet me\b/gi`. A whole architecture of phase machines and durable-event promotion rests on a two-token string test over model prose.

**The transferable lesson:** when a heuristic over model output gates a control-flow decision, write down what happens when the heuristic is wrong. Here, a false negative means the agent stays in a two-tool sandbox longer than intended — benign. Get the same shape wrong in a hiring pipeline and it is not benign. This is a small, concrete argument for the legibility ADR.

### A3 — The provenance story, end to end (~20 minutes)

Read v238's `FAREWELL.md` and issues #60 / #51 / #65, then read this project's `dsh-liangshen` README and its **npm registry description**. One claim — **98/99, mean 98.5** — introduced downstream on 2026-08-14 in good faith, publicly corrected upstream on 2026-08-16, and still in the registry on 2026-08-18 with no acknowledgment of either the correction or the two failed replications.

Nobody lied. The number simply outran its own correction through a dependency graph. **This is the strongest argument the corpus has produced for its own habit of pinning every claim to its provenance and confidence label** — and for the routine's §37.4 discipline.

🔴 **Do not cite 98/99 anywhere.**

---

## Explicitly don't

| Don't | Why |
|---|---|
| 🔴 **Install `dsh-ssh` — anywhere near anything you care about** | An LLM with unconstrained `ssh_exec` + `ssh_cluster`, no approval, no audit, no redaction, plaintext passwords. The worst realistic outcome is a model unilaterally running a destructive command across a fleet with no record of having done it. |
| 🔴 **Cite the 98/99 / 91/92 / 99/96 numbers** | Attribution publicly corrected upstream; two replications failed; no sample size or CI anywhere. |
| 🔴 **Install the aggregate on a machine with real credentials** | It transitively fetches a tunnel binary at install time and bundles the SSH plugin. |
| 🔴 **Treat the skins as usable commercially** | CC BY-NC-SA-4.0 on one skin; `minecraft` and `miku` are third-party IP. |
| 🔴 **Point any of this at candidate data** | A rival lab's rc-stage runtime with PRC-default egress, an image-understanding tool wired to third-party vision endpoints, and a fleet-exec tool. Straightforwardly incompatible with the legibility ADR. |
| ⚠️ **Cite "1,477 files" or "66 contributors"** | GitHub-API-derived; this environment mocks that API (§37.4). Use the hand-verified **70-handle** `README.en.md` block instead. |

---

## Suggested next action

**⭐ A1 → B5 → C11.** Read `verify-docs.mjs`, write the vault doc-lint contract into `CLAUDE.md`, then build `verify-vault-docs`.

The vault currently carries a filename label that lags six ships, a "Current state" block frozen at a v78-era snapshot, six §C rows past both stale floors, and — until yesterday — a shim large enough to break its own fan-out tooling. This ship arrived with a working linter for exactly that disease, written by seventy strangers in six days for a project whose own prose had already drifted in four places while their build stayed green.

**Take the linter.**
