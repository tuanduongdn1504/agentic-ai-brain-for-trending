# The two originals that ARE this project's foundation

> The strangest thing about this roundup: two of Chase's 17 picks are not tools the operator *might* adopt — they're the tools this very vault is **already built on**. `karpathy/autoresearch` is the pattern the autopilot routine ports; `teng-lin/notebooklm-py` is the engine the yt-pipeline drives. The action here is **refine/upgrade**, not "install."

---

## autoresearch — `karpathy/autoresearch` (the routine's ur-pattern)

### Verified facts (gh api, 2026-06-29)
- **89,055★** · Python · created **2026-03-06** · **last pushed 2026-03-26** (static ~3 months) · not archived.
- **License: MIT is declared in the README, but there is NO `LICENSE` file** — the GitHub API returns `license: null`. For legal/dependency purposes treat it as *self-declared MIT, not formally registered*. (Confirmed by the adversarial pass + a direct `gh api repos/karpathy/autoresearch/contents` showing no LICENSE in root.)

### What it actually is
An autonomous research harness for **single-GPU nanochat pretraining** (a small GPT-style model). Three files matter:
- `prepare.py` — **read-only** data prep + tokenizer + the evaluation harness (the agent can't touch it).
- `train.py` — the **only** file the agent edits (architecture, optimizer, hyperparameters, model size).
- `program.md` — **human-editable Markdown** that steers the agent's research direction.

Each cycle: edit `train.py` → `git commit` → run `uv run train.py` for **exactly 5 minutes** → parse the metric **`val_bpb`** (validation bits-per-byte, lower-is-better, vocab-size-independent) from `run.log` → append to `results.tsv` → keep/discard/retry → loop autonomously overnight.

### Chase's framing — corrected
- **"ML in a box — point it at any app you want to improve" → PARTIAL/overstated.** It is **domain-specific to nanochat pretraining** with a *fixed* eval harness and *locked* data. The agent cannot modify `prepare.py` or install packages. It is a hyperparameter/architecture search loop for one fixed task — **not a general-purpose "improve any system" harness.**
- **"requires an objective success criterion (time/numbers)" → CONFIRMED** — the whole design hinges on `val_bpb`; it cannot work without a ground-truth numeric signal.
- **"83 experiments → 15 improvements" → UNVERIFIED.** This exact statistic does **not** appear in the README, `program.md`, code, commits, or any release. The README only gives an *estimate*: "~12 experiments/hour and ~100 experiments while you sleep." The 83/15 figure is likely from a live demo or a Karpathy tweet — **do not cite it as a documented baseline.**
- **"lightweight" → CONFIRMED** for code (3 core files), but it needs a real GPU (tested on H100; community forks for MPS/AMD).

### Why this is load-bearing for the operator
The vault's [[autopilot-research-routine]] is an **explicit, admitted port** of autoresearch to knowledge work (it says so in its own header). The mapping:

| autoresearch | this vault's routine |
|---|---|
| `val_bpb` (lower-is-better metric) | `gaps_closed_ratio` |
| fixed 5-minute experiment budget | wall-clock + NotebookLM-call budgets |
| git checkpoint per experiment | `loop-log/` markdown audit trail |
| `program.md` agent skill | `(C) autopilot-research-routine.md` (8 phases + constitutional invariants) |
| read-only `prepare.py` (agent can't break eval) | "READ-ONLY outside scope" rule |

**The takeaway is not "adopt autoresearch."** It's: *the foundation you ported is now a 89K-star, static-since-March reference.* Two concrete moves: (1) **revisit the analogy** — autoresearch is rigorous *because the metric is a hard ground-truth number*; your `gaps_closed_ratio` is softer (gap-counting is judgment), which is worth being honest about when you cite the lineage; (2) **note the license gap** if you ever vendor or quote its code — MIT is README-only.

---

## notebooklm-py — `teng-lin/notebooklm-py` (the yt-pipeline engine)

### Verified facts (gh api, 2026-06-29)
- **16,968★** · **MIT** · Python · created **2026-01-07** · pushed 2026-06-29 (daily-active). **27 contributors** (not solo — though teng-lin is sole owner/gatekeeper).
- **Current version: v0.7.2** (PyPI, 2026-06-18). **Your vault is pinned to v0.3.4** (2026-03-12).

### What it is
An **unofficial** Python/CLI bridge to Google NotebookLM — Playwright browser-automation for login + direct calls to undocumented Google endpoints. 50+ Click commands: notebook CRUD, source ingestion (URLs/YouTube/PDFs/Drive), artifact generation (audio/video/slides/quizzes/flashcards/mind-maps), and chat — including features the web UI **doesn't** expose (batch downloads, structured JSON/MD/HTML quiz/flashcard export, chat-to-notes).

### Chase's framing — verdicts
- **"Connects Claude Code to NotebookLM" → CONFIRMED** (this *is* the PyPI `notebooklm-py` your `yt-pipeline` drives — verified the operator's own `skills/(C) yt-pipeline.md` calls it).
- **"NotebookLM has no official API; this works around it" → now PARTIAL.** Google shipped a **NotebookLM *Enterprise* API** (Preview, GCP-only, docs updated 2026-06-18). For free-tier/personal use, the undocumented-API workaround is still necessary — but a first-party path now exists for enterprise.
- **"CLI exposes more than the web UI" / "best with YouTube" → CONFIRMED.**

### The actionable findings for the operator
1. **Version gap (v0.3.4 → v0.7.2).** Three minor versions of breaking changes accumulated: new retry behavior, exception-hierarchy/exit-code changes, changed return signatures, cookie-based auth (`--browser-cookies`), and `NOTEBOOKLM_AUTH_JSON` for CI. **A v0.7.2 upgrade audit is overdue** — but your conservative pin is defensible; schedule the audit on a branch, don't upgrade blind.
2. **Correct the "bus factor = 1" note.** The vault's `notebooklm.md` says "solo maintainer." It's actually **27 contributors** — single-*owner* risk is real (teng-lin gatekeeps releases), but it's not a one-person project. Worth amending the caveat.
3. **The undocumented-API fragility is real** ("APIs can change without notice") — relevant if hireui ever depends on it in production (it currently doesn't; this is research-layer only).

---

## The meta-point

Chase recommends, to a general audience, the two tools the operator has *already* operationalized at the right abstraction level (CLI-in-a-skill, not embedded in product code). That's a quiet validation of the vault's architecture — and a prompt to do the unglamorous maintenance (upgrade audit, license note, caveat fix) that "install the new shiny thing" content never covers.

## Cross-links

- [[autopilot-research-routine]] — the routine that ports autoresearch
- [[harness-engineering/_index]] — autoresearch as the autonomous-loop reference; bounded-autonomy discipline
- [[claude-code-memory-systems/_index]] — the Karpathy LLM-Wiki lineage (sibling Karpathy pattern this vault also runs)
- [[graphify-codebase-graph/_index]] — the other "Karpathy-pattern automation" topic
- [[claude-code-plugins-stack/source-provenance]] — the autoresearch license-gap + "83-experiments" flags + notebooklm-py bus-factor correction
