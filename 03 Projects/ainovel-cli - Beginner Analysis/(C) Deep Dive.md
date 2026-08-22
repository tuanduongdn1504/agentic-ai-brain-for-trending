# (C) Deep Dive — v263 `voocel/ainovel-cli`

**Shipped:** 2026-08-21 · **Wiki:** v263 · **Verdict:** GOAL-ALIGNED INCLUDE · **NO MINT**
⚠️ **The operator supplied `mranex/ainovel-cli`. That is a fork with zero commits by the forker. The subject is the upstream, `voocel/ainovel-cli`, and the credit is voocel's.**

---

## 1. D49 first, and it earned its N=2 in one ship

The rule minted at v262 — *a repository's namespace is not a claim about its authorship* — was applied before anything else, and it fired immediately:

```
$ git log --all --format='%an <%ae>' | sort | uniq -c
 185 voocel <voocel@gmail.com>
   7 cheemsadoge <ywjh.net@qq.com>
   6 武穆逸仙 <star8521@vip.qq.com>
   1 不李李李李你 <2926686459@qq.com>
   1 ducat <no.525350@gmail.com>
```

**Zero commits by `mranex`.** The rendered page confirms *"forked from voocel/ainovel-cli"* (1 star, 0 forks on the fork). ⭐ **Two consecutive supplied URLs, two forks by other people** — D49 has N=2 in the ship immediately after it was written.

⭐ **A cheaper refinement, found here:** the upstream was already named *inside the commit log itself* — `78fd97b Merge branch 'main' of github.com:voocel/ainovel-cli`. **A merge commit's message often names the upstream, and that requires no network call at all.**

---

## 2. ⚠️ And it forces a correction to v262

At v262 I wrote that the forker *"forked this on or after 2026-04-29 and then created four more projects over the following twenty-eight days … the example was in his own account the whole time."*

**That is not established, and the reasoning was wrong.** A fork's clone contains the upstream's history **up to the fork moment**, so the fork's HEAD date is a **lower bound** on when the fork was made — never the fork date. GitHub does not expose fork dates in a clone, and the API is mocked here (§37.4).

⭐ **D50: a fork's clone gives you a LOWER BOUND on the fork date, never the fork date. Do not build a timeline argument on when someone forked something.**

And this repository supplies the counter-case that makes the point unavoidable: **its HEAD is `d98aa0f`, dated 2026-06-24** — necessarily *after* all five of the forker's own projects (the latest, `novel_studio`, was created 2026-05-30). So **at least one of the two forks in that account postdates his own work in the same domain.** Building your own thing and later collecting mature alternatives in the same space is ordinary, healthy behaviour and is evidence of nothing.

⇒ **"Forking is not adopting" is walked back** to a claim about the present state — *two repositories in that account have real tests and CI; his own five have none* — which is still true and needs no dates. The v262 documents have been corrected in place as part of this ship.

---

## 3. Source verification

✅ **Two clones, `diff -rq --exclude=.git` clean in both directions.**

| Fact | Value |
|---|---|
| HEAD | `d98aa0fbdaede88c26c7c9f0fb1160e8c5633185` (2026-06-24) |
| Commits | **200** on HEAD and `--all` (D39) |
| Roots | **2** — `eb13358` *"Initial commit"* and `27bd85e` *"init"*, both 2026-03-07 |
| Merges | **7** · Tags: 0 · refs: `main` only (D27) |
| Span | 2026-03-07 → 2026-06-24 (**~3.5 months**) |
| Authors | voocel 185 · cheemsadoge 7 · 武穆逸仙 6 · 不李李李李你 1 · ducat 1 |
| Merged PRs | **7** (#2, #18, #23, #29, #42) from outside contributors |
| Tracked files | **273** |
| Code | **208 `.go` / 43,843 lines** · 47 `.md` / 6,047 lines |
| Tests | **63 `_test.go` / 11,868 lines / 403 `func Test`** |
| Licence | MIT, `LICENSE` file present |

**Layout:** `internal/` (214 files) — `host` 47, `store` 29, `tools` 28, `entry` 28, `rules` 18, `diag` 16, `domain` 15, `agents` 8, `bootstrap` 7 — plus `cmd/`, `assets/`, `docs/`, `scripts/`.

**Stack:** Go 1.25, `charmbracelet/bubbletea` v1.3.10 for the TUI, and — notably — **`github.com/voocel/agentcore` v1.7.2 and `github.com/voocel/litellm` v1.6.18, both by the same author.** ⚠️ `voocel/litellm` is a Go library distinct from the well-known Python `litellm` by BerriAI.

---

## 4. What it is

**"全自动 AI 长篇小说创作引擎"** — a fully automatic AI long-form novel creation engine. From a one-sentence premise it coordinates an **Architect / Writer / Editor** team under a **Coordinator**, writes chapter by chapter, reviews on seven dimensions, and is designed to run **unattended across 500+ chapter works** with chapter-level breakpoint recovery, rolling volume/arc planning, and live user intervention that does not pause the run.

⭐ **This is a long-running autonomous multi-agent harness**, and the harness engineering — not the novels — is the substance. It is the most substantial subject of this run by a wide margin.

---

## 5. ⭐⭐⭐ The engineering that is worth the ship

I read these myself rather than taking them from the fleet.

### StopGuard — a three-way decision on "the agent wants to stop"

`internal/host/reminder/stop_guard.go:26-62`:

```go
func NewStopGuard(st *store.Store, onBlock func(reason string, consecutive int32)) agentcore.StopGuard {
    return func(_ context.Context, info agentcore.StopInfo) agentcore.StopDecision {
        ... return agentcore.StopDecision{Allow: true}
        ... return agentcore.StopDecision{Allow: false, Escalate: true}
        ... return agentcore.StopDecision{Allow: false, InjectMessage: inject}
```

⭐⭐⭐ **Three outcomes, not two: allow the stop, refuse and escalate, or refuse and inject a message telling the model what to do instead.** Premature termination is the characteristic failure of a long-running agent, and this is the cleanest treatment of it I have seen in this corpus. It is a first-class hook in the author's own `agentcore` (`agentcore.StopGuard`, `agentcore.StopDecision`), with a sibling `subagent_guards.go` and a `reminder_test.go`.

### BudgetSentinel — warn, then stop *at a boundary*

`internal/host/budget.go:17-18,56`:

```go
budgetStopPending   // 已越线，等子代理边界停机   (crossed the line; wait for a sub-agent boundary to stop)
budgetStopped       // 已执行停机                (stop executed)

func NewBudgetSentinel(cfg bootstrap.BudgetConfig, costNow func() float64,
                       abort func(reason string), report func(level, summary string)) *BudgetSentinel
```

And the tests name the behaviour precisely: **`TestBudgetSentinelWarnOnceThenBoundaryStop`**, **`TestBudgetSentinelJumpStraightPastLimit`**, and `TestBudgetSentinelHardStop` with `BudgetConfig{BookUSD: 10, WarnRatio: 0.8, HardStop: true}`.

⭐⭐⭐ **This is loop-engineering v189's 80%/100% budget kill-switch, implemented — plus a refinement v189 did not have: it does not kill mid-operation.** On breach it enters `budgetStopPending` and waits for a **sub-agent boundary**, so the checkpoint stays consistent. And the nastiest case — cost jumping straight past the limit in a single step, skipping the warn threshold — **has its own test.**

### diag — loop detection for free, out of the checkpoints you already keep

`internal/diag/` is a sixteen-file rule engine: `rules_context.go`, `rules_flow.go`, `rules_planning.go`, `rules_quality.go`, `runtime_rules.go`, a `planner.go`, a `snapshot.go`, **a `redact.go`**, and tests for the rules.

`internal/diag/runtime.go:37-38,83,90`:

```go
StuckStep   string  // 尾部连续同 step；"" = 不卡   (trailing consecutive identical step; "" = not stuck)
StuckCount  int     // 连续次数                     (consecutive count)
...
rc.CurrentStep, rc.StuckStep, rc.StuckCount = analyzeCheckpoints(s.Checkpoints.All())
```

with severities asserted in `runtime_rules_test.go`: `"StuckStep": SevCritical`, `"ArgsInvalidLoop": SevWarning`, and a fixture `StuckCount: 9, // 卡住 critical`.

⭐⭐⭐ **Loop detection is: read the tail of the checkpoint log, count consecutive identical steps, raise a severity. It costs nothing extra, because the checkpoints already exist for resume.** That is the cheapest general stuck-agent detector I have seen, and it is the idea most worth stealing. ⭐ And `redact.go` means the diagnostic bundle is scrubbed before it leaves the machine.

### notify — alerting that cannot hang the thing it is watching

`internal/notify/notify.go:36,48,56,64,82` — `New(command string, events []string)`, an `allows(kind)` event filter, and `runCommand(ctx, ...)`. The test set includes **`TestCommandChannelTimeoutKill`**.

⭐⭐ **The notification channel is a user-supplied command, filtered by event kind, and killed on timeout.** An unattended run's alerting is exactly the wrong place to introduce a hang, and they tested for it.

### An explicit, ordered context-eviction policy

`internal/tools/novel_context.go:477` declares the trim order in a comment, and `:497` implements against it:

```
< recent_state_changes < foreshadow_ledger < relationship_state < 其余（不裁剪）
```

⭐⭐⭐ **An ordered eviction policy for context, declared in one place, with a protected tail that is never trimmed.** Most agent systems trim ad hoc at the call site. This one writes the order down. And `foreshadow_ledger` is a real domain type (`domain.ForeshadowEntry`) — the mechanism behind the commit *"久挂未回收伏笔按账龄回填上下文,降低长篇遗忘"* (**back-fill long-unresolved foreshadowing into context by age, to reduce long-form forgetting**), which is a genuinely novel idea: treat dangling plot threads like aged receivables.

---

## 6. 🔴🔴🔴 The defect, and it completes a three-ship ladder

**403 test functions. 11,868 lines of tests. 63 test files. Nothing has ever run them.**

Verified with the widest extent I could construct:

- `grep -rn 'go test\|go vet\|gotestsum\|golangci' .github/` → **zero hits.**
- Only **four** `.yml` files have existed on **any ref**: `docker.yml`, `release.yml`, `.goreleaser.yml`, `docker-compose.yml`. I grepped the **content of every yml blob ever committed** across all 200 commits for `go test` → **no hit.**
- **No Makefile, justfile or Taskfile exists.** The only scripts are `.github/scripts/gen-changelog.sh` and `scripts/install.sh`; neither runs tests.
- 🔴 **And the triggers are the kicker:** both workflows fire **only** on `push: tags: v*` (docker also `workflow_dispatch`). **Nothing runs on a branch push. Nothing runs on `pull_request`.**

⇒ 🔴🔴 **There is no CI on commits at all. The only automation is release packaging, triggered by a tag. And seven pull requests from four outside contributors were merged with zero automated checks of any kind — not a test, not a build, not a vet, not a lint.**

### ⭐⭐⭐ The ladder

Three consecutive ships, three distinct failure modes of the same thing:

| Ship | Tests | Gate | Failure mode |
|---|---|---|---|
| **v261** novel_studio | **0** (`pytest` declared in requirements) | a `Verification:` command naming two directories that never existed | **the claim without the test** |
| **v262** Auto-Create-Video | 9 files / 116 assertions | CI runs `npm test` — with `--passWithNoTests` | **the gate that cannot fail** |
| **v263** ainovel-cli | **63 files / 403 functions / 11,868 lines** | **none — CI fires only on tags and never runs a test** | **the test without the gate** |

⭐⭐⭐ **And v263 is the most poignant, because the tests are genuinely good** — a 916-line test for the novel-context builder, 579 for chapter commit, 496 for foundation saving, 416 for usage accounting — **and the only thing that has ever run them is a person who remembered to type `go test ./...`.**

⇒ ⭐⭐⭐ **This sharpens v262's rule into its final form: "tests don't make you honest, they make you honest about the things they test" — and only if something runs them. A test that nothing invokes is documentation.**

⭐⭐⭐ **And the irony is the ship's sentence: this is the most carefully engineered agent-safety machinery in the entire run — a three-way StopGuard, a boundary-aware budget sentinel, checkpoint-derived loop detection, timeout-killed alerting, an ordered eviction policy — in a repository where nothing has ever run a test. Every gate was built for the agent. None was built for the code.**

*(Minor, and worth naming only because it is the same shape: `t.Run` appears just 9 times across 403 test functions, so the suite is almost entirely flat rather than table-driven — which makes it harder to extend, and nothing is measuring that either.)*

---

## 7. ⭐⭐⭐ The centrepiece I missed, and the fleet found: routing is code, deciding is the model

My own read got StopGuard, the budget sentinel, loop detection and the eviction policy. **It missed the architecture those hang off**, which is the single most valuable thing in the repository. A fleet agent found it; its adversarial reviewer then corrected three fabricated numbers in the same report. Both halves are recorded below, and I verified every claim myself before using it.

### The Host does not decide anything, and says so

`internal/host/host.go:32-34`:

```
// Host 是运行时薄外壳。
// 职责：启动/恢复/干预注入/事件投影/模型管理。
// 不做任何调度决策，不做空闲续跑。
```

*"Host is a thin runtime shell. Responsibilities: start / resume / intervention-injection / event-projection / model-management. **It makes no scheduling decisions and does no idle continuation.**"*

⭐ A declared architectural boundary, at the top of the file that would otherwise be tempted to violate it.

### Scheduling is a pure function over persisted state

`internal/host/flow/router.go` is **160 lines** ending in `func Route(s State) *Instruction` — a **numbered decision table, cases 1 through 12**, over `State` (Progress + Checkpoints + arc boundaries):

```
 1. 终态：让 LLM 输出总结              terminal → let the LLM write the summary
 2. 规划阶段由 Coordinator 裁定         planning → the Coordinator adjudicates
 3. 重写/打磨队列优先                  rewrite/polish queue takes priority
 4. 审阅中：…路由不介入                 review in flight → the router does not intervene
 5. 用户干预处理中：Host 不抢占          user intervention in flight → Host does not preempt
 6-10. 分层模式的弧末后处理             layered-mode arc-end post-processing
12. 正常续写                          otherwise → writer(next chapter)
```

The Coordinator is an `agentcore` agent configured with **`agentcore.WithMaxTurns(100_000)`** — at **`internal/agents/build.go:314`**. ⚠️ *(The fleet report cited this to `host/host.go:32-34`, which is the comment block above; its reviewer caught the error and was right. I checked.)*

⇒ ⭐⭐⭐ **The pattern: the agent does not choose what to do next. Code chooses, from state that is already persisted for resumability, and the agent executes. Semantic work — adjudication, planning, writing — stays with the model; sequencing does not.** Cases 2, 4 and 5 are the discipline that makes it work: the router explicitly **declines** to route when a decision is genuinely the model's, rather than pretending everything is mechanical.

### And he measured why, before he built it

`docs/refactor-flow-driven.md` is the design rationale for that refactor, **retained at HEAD**. Lines 95–99:

- per chapter the Coordinator reads *"~3000 tokens system prompt + ~200 reminder + history + ~500 CommitResult → generates ~50 tokens of tool_call"*;
- a 200-chapter novel is *"200-400 turns"* of Coordinator calls;
- of those, ***"~90% 是纯路由（LLM 复述 reminder），~10% 是裁定"*** — ~90% is pure routing, the model restating an instruction, and ~10% is real adjudication;
- ⭐ ***"每章 ~3500-7000 tokens 花在 Coordinator 决策上，95% 是冗余"*** — *~3,500–7,000 tokens per chapter spent on Coordinator decisions, 95% of it redundant.*

And lines 443–448 state the target: the Coordinator prompt compressed *"从 ~3000 tokens 压到 ~800"*, still one turn per chapter, **总计 ~1000-1500 tokens** — a total of ~1,000–1,500 tokens per chapter.

⚠️ **Do not repeat the fleet's numbers for this.** Its report claimed *"~100 tokens per chapter for routing"* and *"3.5M tokens saved (~$175)"*; **the reviewer refuted both** — the repo's own figure for the new architecture is ~1,000–1,500 tokens per chapter, not ~100, and no file contains a dollar amount. **The sourced claim is the 3,500–7,000 → 1,000–1,500 range and the 90%/95% redundancy diagnosis, all of it his own analysis.**

⭐⭐⭐ **And this is where the run's arc closes.** v252 built a three-arm eval and **deleted the results** in the commit that claimed the win. v261 wrote a 676-line plan and **deleted it** in the commit titled *"Done 11 phase."* **v263 wrote the token analysis, kept it, and the code matches it.** The design document is the reason any of this is checkable.

### The stall detector, which is the best twenty lines in the repository

`internal/host/flow/dispatcher.go:112-140`, `trackRepeat`:

```
// trackRepeat 记录连续相同指令的下达次数并返回当前次数（1 = 新指令）。
// 用 Agent+Task 相等性（不比 Reason，因为 Reason 是给人看的辅助文本）。
// 次数恰好到 repeatNotifyAt 时在锁外触发一次 onRepeat（键变更重计数后重新武装）。
```

Four separate pieces of care, in one small function:

1. ⭐⭐⭐ **Equality on `Agent+Task` only, deliberately excluding `Reason`** — *"because Reason is human-facing helper text."* A stall detector that compared the whole instruction would be defeated by prose that varies while the instruction does not. **He identified that failure mode and wrote down why he excluded the field.**
2. **Fires once, exactly at `== repeatNotifyAt`** — one alert, not a storm. `router_test.go:289-290` asserts precisely that: *"应恰好在第 N 次触发一次"* — should fire exactly once, on the Nth.
3. **Fires outside the lock** — a slow notification handler cannot block the dispatcher.
4. **`ResetRepeat()` on Resume/Start**, so *"the first instruction after recovery is issued with '1st-time' semantics"* — **resume does not inherit a stale repeat count.**

And `dispatcher.go:33` describes `onRepeat` as *"纯 telemetry 回调（无人值守告警用）"* — a pure telemetry callback for unattended alerting. ⇒ ⭐⭐⭐ **The chain is complete and end-to-end: the router detects a stall from persisted state → the dispatcher counts it on the semantic key → fires exactly once, outside the lock → notify runs a user command → killed on timeout if it hangs.** That is the most complete unattended-safety path in this corpus.

⭐ **And the philosophy underneath it is the transferable half:** the router does not hard-fail on a repeat. It **injects the evidence and lets the model reason about the stall** — the same move as StopGuard's `InjectMessage`. *Instead of a retry limit, block the attempt, hand over the evidence, and let the agent decide.*

### Checkpoints: idempotent by digest, and the degenerate case is tested

`internal/store/checkpoints.go:51-59`:

```
// 幂等：相同 Scope + Step + Digest 已存在则跳过写入，直接返回已有记录。
```

*"Idempotent: if the same Scope + Step + Digest already exists, skip the write and return the existing record."* So a retried tool call finds its own prior result instead of duplicating work.

⭐⭐ **And `checkpoints_test.go:71` is `TestCheckpointStore_EmptyDigestNotIdempotent`** — *"空 digest 不参与幂等去重"*, an empty digest does not participate in dedup. **Two artifacts with no digest must not be treated as the same artifact.** That is the case where the mechanism would silently betray him, and it has its own test — the same instinct as `TestBudgetSentinelJumpStraightPastLimit`.

⇒ ⭐⭐ **Twice, in the two places where his own safety mechanism could produce a false negative, he wrote the test for it. Which makes the absence of anything to run those tests the sharpest fact in the ship.**

---

## 8. The fleet audit

17 agents across 8 dimensions, each assessment followed by an adversarial reviewer aimed at its own citations and numbers. 363 seconds, 2.24M subagent tokens, 0 errors, 0 empty results.

**What it earned:** the Flow Router architecture, the `docs/refactor-flow-driven.md` token analysis, and the digest-idempotency design — **the three best findings in the ship, none of which I had.** A single reader working through 43,843 lines of Chinese-commented Go was not going to enumerate `internal/host/flow/` and `docs/` and `internal/store/` systematically in one pass. **That is exactly what breadth is for.**

**What the adversarial layer caught, in the same report that carried the best finding:**

| Fleet claim | Reviewer's correction — verified |
|---|---|
| `WithMaxTurns(100_000)` at `host/host.go:32-34` | **Wrong file.** It is `agents/build.go:314`; `host.go:32-34` is a comment block |
| *"Routing = ~100 tokens per chapter"* | **Unsupported.** The repo's own doc says the new architecture costs ~1,000–1,500 tokens per chapter |
| *"3.5M tokens saved (~$175 on fast models)"* | **Arithmetic inconsistent with its own premises, and no file contains a dollar figure** |

⭐⭐ **Method result, and it is the counterpart to both of the last two ships:** at v261 the *aggregating* stage produced every error while file-readers were reliable; at v262 a file-reader overturned the orchestrator. **Here a file-reader produced the ship's three best findings *and* three fabrications in the same report, and the adversarial reviewer separated them.** ⇒ **The value is not that agents are reliable — it is that a reader and a refuter disagree in checkable ways. Aim an adversary at every stage, then verify what survives.**

⭐ **And a third instance of one specific trap:** the collision grep's `agentcore` hits turned out to be `PageAgentCore` from page-affiliated prior work — an unanchored substring, so **this is not a corpus-recursive dependency.** That is the third time in three ships (`ScrollMode`→`llm`, `Plex`→`multiplexer`, `agentcore`→`PageAgentCore`), and each time it was caught by looking at *where* the matches were rather than *how many*.
