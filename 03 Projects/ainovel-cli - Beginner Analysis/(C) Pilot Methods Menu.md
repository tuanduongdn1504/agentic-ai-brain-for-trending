# (C) Pilot Methods Menu — v263 `voocel/ainovel-cli`

## Verdict: **READ-AND-BORROW — the richest borrow-list of this seven-ship run.**

Do not install it: it is a novel-writing engine, it needs a `scripts/install.sh`, and it trusts two libraries by the same single author. **There is nothing here hireui needs as software.** But there are five patterns here worth having, and they are the best answers to *"how do you run an agent unattended for hours without it lying to you or bankrupting you"* that this corpus has produced.

⚠️ Reading cost, stated plainly: most comments and all commit messages are Simplified Chinese. The Go identifiers are English, so the code is followable; the *reasoning* is not, unless you read Chinese or translate as you go.

---

## Rung 0 — 25 minutes, five files in this order

1. **`internal/host/reminder/stop_guard.go`** — the three-way stop decision. Read the three `return` statements.
2. **`internal/host/budget.go:17-18,56`** — the two pending states and the sentinel constructor.
3. **`internal/host/budget_test.go`** — read the *test names*. `TestBudgetSentinelWarnOnceThenBoundaryStop`, `TestBudgetSentinelJumpStraightPastLimit`. The names are the specification.
4. **`internal/diag/runtime.go:37-38`** — `StuckStep` / `StuckCount`, and `analyzeCheckpoints`.
5. **`internal/tools/novel_context.go:477`** — one comment line containing an entire eviction policy.

Then: `grep -rn 'go test' .github/` → nothing. Hold those two facts together.

---

## ⭐⭐⭐ Rung 1 — 45 minutes, and it is about this vault, not about hireui

**The uncomfortable parallel: the vault is in exactly this subject's position.**

`(C) proposed-verify-vault-inventory.sh` now has **nine clauses and reports 0 FAIL**. It caught a dangling `_state/` reference, five unindexed files, a regrowing shim, a stale source-of-truth declaration, and an audit cadence 46 ships overdue. It is a real gate.

**And nothing invokes it.** It runs when I remember to run it, in the middle of a ship, by hand. That is *precisely* v263's defect — 403 excellent test functions and no CI — one level up, in your own repository.

**The fix is small and it is the whole lesson of this ship:**

1. **Wire it to a git hook.** A `pre-commit` (or `pre-push`) hook in `.git/hooks/` that runs the script and refuses the commit on any FAIL. Ten lines. It cannot be forgotten, because it runs on the action you always take.
2. **Or a scheduled task**, if you would rather not block commits — but understand the trade: a scheduled check tells you *afterwards*, a hook tells you *before*.
3. ⭐ **And promote the script out of `03 Projects/HeadFirstAndroid - Beginner Analysis/` into `bin/`.** It is vault infrastructure living in a ship's folder, which is itself a small instance of the drift it exists to catch.

**Cost: 45 minutes. Installs nothing. And it closes the exact gap this subject demonstrates** — the gap between having a check and having it run.

---

## ⭐⭐ Rung 2 — 60 minutes: the budget sentinel, for hireui's LLM path

This is the pattern to take, and it is already half-specified in the corpus by **loop-engineering v189** (an 80%/100% throttle-and-kill-switch). v263 implements it **and adds the refinement v189 does not describe:**

> **Warn once at 80%. Hard-stop at 100%. But do not stop mid-operation — enter a pending state and stop at the next safe boundary.**

`budget.go` names those states `budgetStopPending` (*"crossed the line; wait for a sub-agent boundary"*) and `budgetStopped`. Killing an agent mid-write corrupts the state you would resume from; stopping at a boundary keeps the checkpoint clean.

**For hireui:** any LLM path with a per-tenant or per-job spend ceiling needs all three parts — a warn threshold, a hard stop, and a **boundary definition**. Write down what your boundary *is* (end of a candidate, end of a batch, end of a transaction) before you write the cap, because that is the part everyone omits. ⭐ **And test the jump case**: cost can leap past the warn threshold in a single call, so the warn and the stop must be independent checks, not an if/else. `TestBudgetSentinelJumpStraightPastLimit` exists precisely because that bug is easy.

---

## ⭐⭐ Rung 3 — 30 minutes: two more patterns, cheap and general

1. **Loop detection out of the state you already keep.** `analyzeCheckpoints` reads the tail of the checkpoint log, counts consecutive identical steps, and raises `SevCritical` past a threshold. **It costs nothing extra because the checkpoints exist for resume.** Any hireui job queue with a retry/state log can detect a stuck job the same way, for free. ⭐ The general form: *if you persist progress for resumability, you have already persisted a stuck-detector.*
2. **An ordered eviction policy, declared once.** `novel_context.go:477` writes the trim order in a single comment — `< recent_state_changes < foreshadow_ledger < relationship_state < 其余（不裁剪）` — with a **protected tail that is never trimmed**. Most systems trim ad hoc at the call site and nobody can say what gets dropped first. **Declare the order in one place and derive from it.** For a CV-summarisation prompt that is: what goes first when the context is tight, and what must never go.

⭐ **And the smallest one:** `notify.go`'s channel is a user-supplied command, event-filtered, and **killed on timeout** (`TestCommandChannelTimeoutKill`). Alerting for an unattended run is the worst possible place to introduce a hang.

---

## 🔴 NEVER

- **Never attribute this repository to `mranex`** — it is a fork with zero commits by the forker; all 200 commits are by voocel and four contributors.
- **Never cite star counts for it.** I fetched the *fork's* page (1 star); the upstream's figures are unmeasured and the API is mocked here.
- **Never cite its behaviour as verified.** Nothing was executed — there is no Go toolchain in this sandbox. Every claim here is read from source.
- **Never treat its 403 tests as evidence the code works.** They have never run in CI. They are evidence that someone *thought carefully about behaviour*, which is valuable and different.
- **Never install `scripts/install.sh`** without reading it, and understand that `voocel/agentcore` and `voocel/litellm` concentrate trust in one individual.
- ⚠️ **Do not confuse `voocel/litellm` with the Python `litellm` by BerriAI.** Same name, different library, different author.
