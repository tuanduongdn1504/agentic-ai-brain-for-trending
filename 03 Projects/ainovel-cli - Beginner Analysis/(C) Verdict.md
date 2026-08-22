# (C) Verdict — v263 `voocel/ainovel-cli`

**2026-08-21** · **GOAL-ALIGNED INCLUDE 3/4** · **NO MINT** · counts **46 / 12 UNCHANGED** · §C-1 **12** · §C-2 **38**

⚠️ **Attribution:** the operator supplied `mranex/ainovel-cli`; the page confirms *"forked from voocel/ainovel-cli"* and **all 200 commits are by other people** (voocel 185, plus four contributors). The subject is the upstream; the credit is voocel's.

---

## Phase 0.9 gate

| Criterion | Call | Basis |
|---|---|---|
| **(a) cultural-peer / Anthropic signal** | **FAIL** | `voocel` — a pseudonymous individual, not Anthropic, not a registered (a)-7 source. §41. |
| **(b) goal-relevance** | **STRONG — the strongest of this seven-ship run** | This *is* a long-running autonomous multi-agent harness: a Coordinator dispatching Architect/Writer/Editor sub-agents, a three-way `StopGuard`, a boundary-aware budget sentinel, checkpoint-derived loop detection, an ordered context-eviction policy, per-role/per-model cost accounting, role-level provider fallback, and resumable unattended runs across 500+ chapter works. Goal #1 is *mastering autonomous agents*; this is 43,843 lines of exactly that problem. |
| **(c) substance** | **STRONG** | 200 commits over 3.5 months; 208 Go files / 43,843 lines; 63 test files / 11,868 lines / 403 test functions; 47 docs / 6,047 lines; 5 contributors, 7 merged PRs; MIT. |
| **(d) legibility** | **STRONG** | Clean `internal/` package split (`host`, `store`, `tools`, `entry`, `rules`, `diag`, `domain`, `agents`, `bootstrap`). ⚠️ Code comments and commit messages are largely Simplified Chinese — a real reading cost, not a defect. |

**Cleanly GOAL-ALIGNED. No §40, no override.**

---

## NO MINT — and §C-2 prevented a false N=2 for the second consecutive ship

The candidate was an **N=2 of §C row C38**, the *"Loop-Engineering Codification Kit"* anchored on **loop-engineering v189**. The collision grep surfaced it; reading its definition killed it.

C38 is defined as a *"named-methodology pattern collection + starters + readiness-scoring/audit CLIs for scheduled UNATTENDED **coding-agent** loops — maker/checker split · LOOP.md/STATE.md/loop-budget/loop-run-log durable-state conventions · graduated L0→L3 autonomy ladder · token-budget governance w/ 80% throttle + kill-switch; **cross-harness**."*

This subject is **a single Go application for novel writing**. It has no methodology kit, no starters, no readiness-scoring CLI, no maker/checker split, no L0→L3 ladder, no LOOP.md conventions, and it is not cross-harness. The one genuinely shared element — **token-budget governance with an 80% warn and a kill-switch, which it implements as `WarnRatio: 0.8` + `HardStop`** — is *one bullet* of C38's definition, not the class.

⇒ **Adjacency, not instance. Counts unchanged.**

⭐⭐⭐ **Second consecutive ship in which reading a §C-2 row's definition prevented a false N=2** (v262: C37's *"the coding agent IS the runtime"* clause; v263: C38's codification-kit-versus-application distinction). **The v259 bifurcation's stated justification — that retiring the N=1 catalogue *"would destroy the mechanism that makes collision-detection possible"* — now has a demonstrated mechanism at N=2, three and four ships after the amendment.** Recorded for the audit.

**A fresh §C-2 mint was also declined, on five grounds:**

1. 🔴 **Domain-not-capability** — "AI writes a long novel" is a domain, and a crowded one.
2. 🔴 **Not world-first** — autonomous long-form AI novel generators are numerous.
3. 🔴 **The differentiating primitive does not ship here.** `StopGuard` and `StopDecision` are types in **`github.com/voocel/agentcore`**, a *separate* library by the same author. The harness composes primitives it does not define — v242's **D25** applied to a component.
4. 🔴 **Form-factor within a genre** (the v236/v227/v222 chain).
5. 🔴 **§28 as a supporting ground only** per v2.8 §44 clause 5, measured against **§C-1 = 12**, and not load-bearing alone — grounds 1–3 each suffice.

**`inflation_check` HELD** — 0 mints, 0 N-bumps, 0 promotions, 0 retires.

---

## ⭐⭐⭐ The finding: every gate was built for the agent, none for the code

**403 test functions. 11,868 lines of tests. Nothing has ever run them.**

Extent, stated: zero hits for `go test`/`go vet`/`gotestsum`/`golangci` in `.github/`; only four `.yml` files have existed on **any ref** and the **content of every yml blob ever committed** contains no `go test`; no Makefile, justfile or Taskfile exists; and both workflows fire **only on `push: tags: v*`** — nothing on a branch push, nothing on `pull_request`. **Seven PRs from four outside contributors were merged with zero automated checks of any kind.**

Set that against what the same author *did* build, for the agent:

- a **three-way `StopGuard`** — allow the stop, refuse and escalate, or refuse and **inject a corrective message** (`stop_guard.go:26-62`);
- a **`BudgetSentinel`** that warns at 0.8, hard-stops at 1.0, and **waits for a sub-agent boundary rather than killing mid-operation** (`budget.go:17-18,56`) — with the cost-jumps-past-the-limit edge case given **its own test**;
- **loop detection derived from the checkpoint tail** (`runtime.go:37-38,83`) at `SevCritical`, costing nothing because the checkpoints already exist for resume;
- **alerting that cannot hang the run** (`notify.go`, `TestCommandChannelTimeoutKill`);
- an **explicitly ordered context-eviction policy with a protected tail** (`novel_context.go:477`).

⇒ ⭐⭐⭐ **This is the most carefully engineered agent-safety machinery in the entire run, in a repository where nothing has ever run a test.**

### The three-ship ladder

| Ship | Tests | Gate | Failure mode |
|---|---|---|---|
| **v261** | 0 (`pytest` declared) | a verification command naming directories that never existed | **the claim without the test** |
| **v262** | 9 files / 116 assertions | `npm test` — with `--passWithNoTests` | **the gate that cannot fail** |
| **v263** | **63 files / 403 functions** | **none; CI fires only on tags** | **the test without the gate** |

⇒ ⭐⭐⭐ **v262's rule reaches its final form: tests don't make you honest — they make you honest about the things they test, *and only if something runs them*. A test that nothing invokes is documentation.**

---

## Bookkeeping

- **Counts:** 46 patterns · **12** CONFIRMED Library-vocab · §C-1 **12** · §C-2 **38** · max pattern #85. **All unchanged.**
- **Streak:** v262 `GA:119` → **`GA:120 · OG:13 [7 ov]`** — **43 consecutive goal-aligned ships, v220→v263**.
- **§35:** **CLEAR.** Window {v261 GA, v262 GA, v263 GA} = 0 OG.
- **Override:** none.
- **Tier:** T5 Application with a substantial **harness/runtime facet** — the harness is the subject, the novels are the payload. Reviewable.
- **Secondary, not minted:**
  - ⭐ **#19 ecosystem-portfolio-builder, a clean data-point:** voocel authored **`agentcore`** (the agent framework), **`litellm`** (the Go LLM gateway) *and* this application. The harness sits on two of his own libraries. ⚠️ Note for readers: `voocel/litellm` is a Go library **distinct** from the well-known Python `litellm` by BerriAI.
  - **#12 MIXED — a new species.** Tests: strongly POSITIVE (403 functions). CI-that-runs-them: **absent**. Previous ships were POSITIVE or NEGATIVE on both together; this splits them.
  - **#66 MIXED** — MIT with a licence file, `redact.go` scrubbing diagnostic exports, and alerting killed on timeout, against **two same-author dependencies** requiring single-point trust, a `scripts/install.sh`, and no automated check on merged community PRs.
  - **loop-engineering v189 cross-reference** — an implemented instance of C38's *budget-throttle-plus-kill-switch* bullet, with a **boundary-aware stop** refinement C38 does not describe. Recorded, not an N-bump.
- **NON-claims:** NOT #52 (the fork shows 1 star; **the upstream's figures are unmeasured — I fetched the fork's page**, and the API is mocked per §37.4) · **NOT #57** — the `agentcore` collision hits are `PageAgentCore` from page-agent v199, an unanchored substring, and `voocel/agentcore` is not a corpus subject · NOT world-first · NOT a C38 instance · **NOT executed** — there is no Go toolchain in this sandbox.

⭐ **RECORDED FOR THE AUDIT — D49 at N=2 and new rule D50.** Two consecutive supplied URLs were forks by other authors, so **D49** (*a namespace is not a claim about authorship*) earned its second instance in the ship immediately after it was minted. ⭐ And a cheaper detector surfaced here: **a merge commit's message often names the upstream** (`78fd97b Merge branch 'main' of github.com:voocel/ainovel-cli`) — no network call needed. ⭐ **D50: a fork's clone gives you a LOWER BOUND on the fork date (its HEAD date), never the fork date.** This corrected a v262 claim; see the Deep Dive §2, and the v262 documents were amended in place as part of this ship.

---

## The one-line verdict

**The most substantial and most goal-relevant subject of this seven-ship run — a genuinely well-engineered autonomous agent harness whose author built a three-way stop guard, a boundary-aware budget kill-switch, free loop detection and 403 test functions, and then never pointed a single gate at his own code.**

---

## Appendix — what the fleet earned, and what it fabricated

17 agents across 8 dimensions, each with an adversarial reviewer aimed at its own citations and numbers. 363s, 2.24M subagent tokens, 0 errors.

**Earned — the three best findings in the ship, none of which I had:** the **Host Flow Router** architecture (`router.go`, a 12-case pure function over persisted state, with the Host declaring at `host.go:32-34` that it *"makes no scheduling decisions"*); **`docs/refactor-flow-driven.md`**, the retained design document whose own numbers diagnose *~90% of Coordinator turns as pure routing* and *95% of ~3,500–7,000 tokens per chapter as redundant*; and the **digest-based checkpoint idempotency** with its degenerate-case test.

**Fabricated, in the same report, and caught by its reviewer:** the `WithMaxTurns(100_000)` citation (wrong file — it is `agents/build.go:314`); *"~100 tokens per chapter for routing"* (the repo says ~1,000–1,500); and *"3.5M tokens saved (~$175)"* (arithmetic inconsistent with its own premises, and **no file contains a dollar figure**).

⭐⭐ **Method result — the counterpart to both preceding ships.** At v261 the aggregating stage produced every error while file-readers were reliable. At v262 a file-reader overturned the orchestrator. **Here one file-reader produced both the best findings and three fabrications, and the adversarial reviewer separated them.** ⇒ **The value is not that agents are reliable; it is that a reader and a refuter disagree in checkable ways. Aim an adversary at every stage, then verify what survives.** I verified every claim above against the source before using it.

⭐ **And a third consecutive instance of one trap:** the collision grep's `agentcore` hits were `PageAgentCore` from an unrelated prior subject — an unanchored substring, so **this is not a #57**. Third ship running (`ScrollMode`→`llm`, `Plex`→`multiplexer`, `agentcore`→`PageAgentCore`), and each time it was caught by looking at *where* the matches were, not *how many*.
