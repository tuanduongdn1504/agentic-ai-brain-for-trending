# (C) unlazy — Deep Dive

**Subject:** `github.com/Leonxlnx/unlazy` — *"Completion discipline for substantial AI-agent work, backed by runnable gates."*
**Corpus entry:** v274 · **Shipped:** 2026-08-24 · **Verdict:** GOAL-ALIGNED INCLUDE 3/4 · **Mint:** NO MINT
**Author:** Leon Lin / `Leonxlnx` `<lexn.lin8@gmail.com>` — solo indie developer, Munich. **NOT Anthropic** (§41; `Anthropic` appears **0** times in the repository).
**⭐ SAME AUTHOR AS CORPUS v81** (`Leonxlnx/taste-skill`, shipped 2026-05-20). Routine **§42 same-author control** applies at a **193-ship gap**.

---

## 0. Source verification

| Fact | Value | How established |
|---|---|---|
| Clone integrity | **VERIFIED** | two independent clones, `diff -rq` clean **both** directions |
| HEAD | `754d9a68109e39b836cc72a39fb9a823f9d6b613` | `git rev-parse HEAD`, identical in both clones |
| Commits | **31** on `main`, **31** all refs | `git rev-list --count` (**not** `git log \| wc`) — routine **D39** |
| Roots | **1** (`4471edfb`) | `git rev-list --max-parents=0` |
| Merges | 6 | `git rev-list --merges --count` |
| Tags | **0** | `git tag \| wc -l` |
| Fork? | **No** | root commit is the author's own, no upstream remote |
| Tracked files | **28** | `git ls-files \| wc -l` |
| Age | **13 days** — 2026-08-10 → 2026-08-23 | all 31 commits in `2026-08` |
| Lines | `.md` **1,166** (14 files) · `.mjs` **2,860** (9 files) | `wc -l` |
| Production vs test | `scripts/` **1,570** · `tests/` **1,290** → ratio **0.82** | `wc -l` per file, sums to 2,860 |
| Second branch | `origin/v1`, 3 commits, **ancestor of main** | `git merge-base --is-ancestor` |
| Test result | **64/64 PASS** — 26 + 19 + 10 + 9 | **I ran all four suites**, Node v24.13.1 |

**Page-stated only (§37.4 — the GitHub API is mocked here; these are NOT velocity or Pattern #52 claims):** 1,468 stars exact (the repo header rounds to "1.5k"), 96 forks, 5 watchers, 1 open issue, 3 open PRs, 13 closed PRs.

**Authorship:** 9 author identities across 8 emails. `Leon Lin` and `Leonxlnx` share one email = **17 of 31 commits**. **Seven outside contributors supplied 14 commits in 13 days** — a 45% outside-commit rate.

---

## 1. What it is

A **cross-harness agent skill** that refuses to let an agent declare a task finished on its own word. The mechanism is a markdown **acceptance ledger** (`GATES.md`) written *before* implementation, where each gate is an observable outcome with an optional runnable oracle:

```markdown
- [ ] G1: valid fixture imports completely
  CHECK: node scripts/check-import.mjs fixtures/valid.json
  EXPECT: import verification passed
  EVIDENCE: pending
```

Three parts ship: `gate-check.mjs` (690 lines — the runner), `lib/gates.mjs` (575 — one shared strict parser), and `stop-hook.mjs` (132 — an **optional Claude Code Stop hook** that returns `decision: "block"` while the session's pipeline has unmet gates, i.e. it structurally prevents the agent from ending). Zero runtime dependencies; Node 16 floor; MIT.

Install is `npx skills add Leonxlnx/unlazy` (the `vercel-labs/skills` CLI) or a clone into `~/.claude/skills/unlazy` / `~/.codex/skills/unlazy`.

---

## 2. ⭐⭐⭐⭐⭐ The headline — the retracted claim that survives outside the tree

The repository's GitHub **description**, fetched today on **two independent GitHub surfaces** (the repo page and the owner's `?tab=repositories` listing), reads:

> "Anti-laziness skill for AI agents. Core: the Depth Tree method, which splits a task N layers deep and gives every leaf **the full time budget of the whole task, so effort multiplies with depth.**"

That claim has been **retracted inside the repository, in three places, since 2026-08-10**:

| Location | Text |
|---|---|
| `CHANGELOG.md:59` | "Reframed the Depth Tree as decomposition and integration **rather than an arithmetic effort multiplier**." |
| `references/method.md:3` | "**Do not treat depth as an arithmetic promise about effort or tokens.**" |
| `references/method.md:5` | "**The original v1 method claimed that each binary split multiplied effort.** A small maintainer-run comparison later suggested that agents treated depth as a thoroughness cue rather than following that arithmetic." |

**A grep for the claim across all 28 tracked files returns the CHANGELOG retraction and nothing else.** The arithmetic promise exists in **zero** files and in the description.

⭐ `references/method.md:3` is, read literally, **an instruction to the reader not to believe the repository's own sidebar.**

**Why it survives is the finding.** The description is not a file. It is a GitHub metadata field. It is outside CI, so no test can reach it — and it is outside the tree, so the author's own careful editing pass, which reaches every `.md` in the repo, never touches it.

### The rule this ship adds

> **A claim is safe when a gate covers it, or when a habit covers it. This one had neither.**

The ladder:

- **v267** — the discipline stops where the artifact stops being code.
- **v268** — a gate exists where a reader can refuse; what rots is coverage.
- **v269** — no gate can see an entry that was never added.
- **v270** — no gate can fire on a claim that was true when it was written.
- **v271** — a gate's scope is inherited from where it lives.
- **v272** — a gate holds when something else already requires it.
- **v273** — a check is only as permanent as the place you put it.
- **v274** — **neither a gate nor a habit reaches a claim stored outside the repository.**

### The proof that the habit is real

CONTRIBUTING.md:23 carries an unenforced style rule: **"Use no em dash or en dash."** I measured every tracked file:

```
em dashes in tracked files: 0
en dashes in tracked files: 0
(positive control — ' - ' hyphen matches: 9)
```

**Zero violations across 4,150+ lines, enforced by nothing.** I went looking for a violated unenforced rule and found perfect compliance — which is the more interesting result, and it is what makes the description finding precise rather than merely a nitpick. The prose rules hold because **one careful person writes all the prose**. The code rules are gated because **seven strangers touch the code**. The description is the only surface that is neither.

---

## 3. ⭐⭐⭐⭐⭐ The §42 same-author control (v81 → v274)

I cloned `taste-skill` and measured it myself rather than relying on the v81 entry.

| | **taste-skill** (v81) | **unlazy** (v274) |
|---|---|---|
| Shipped to corpus | 2026-05-20 | 2026-08-24 |
| Age at measurement | 2026-02-19 → 2026-08-22 (**6 months, still active**) | 2026-08-10 → 2026-08-23 (**13 days**) |
| Commits | **153** main / 271 all refs | 31 main |
| Tracked files | 64 | 28 |
| Author share | **265 of 271** commits | 17 of 31 |
| Stars (page-stated) | **79,622** (was **18,264** at v81 → **4.36×**) | 1,468 |
| `.github/` contents | **`FUNDING.yml` + `copilot-instructions.md`** | `workflows/test.yml` |
| CI workflows | **ZERO** | 9 jobs (3 OS × Node 16/20/24), push **and** PR |
| `package.json` | **ZERO** | present |
| Test files | **ZERO** | 4 suites, **64 assertions**, all passing |
| Enforcement | prose instruction | runnable gates + parser + hook |

**The same developer, in the same six-month window, maintains a 79,622-star repository with no test suite and no CI at all, and a 13-day-old repository with a four-suite regression harness on nine platform combinations.**

⭐ **The engineering discipline is not a property of the developer. It is a property of what the artifact claims.** taste-skill claims *taste* — judged by a human looking at a UI, so nothing is checkable and nothing is checked. unlazy claims *verification* — and a tool whose thesis is "prove outcomes against a ledger instead of relying on a confident done report" cannot ship untested without its own thesis indicting it.

Per **§42**, separating the two categories:

- **Dispositions (replicate across both):** the `npx skills add` multi-harness install path · the "the model does the lazy/generic thing, here is discipline against it" framing (anti-**slop** → anti-**laziness**) · README-as-product-page polish · overwhelming solo authorship · accepting outside PRs.
- **Attention (varies):** test suites, CI, a threat model, a research protocol, and a shared strict parser — all present in the artifact that claims checkability, all absent from the one that does not.

**Sample size: N=2.** That supports "these habits recur" and a legible mechanism. It does not support a law, and I am not stating one.

---

## 4. What I attacked, and what held

I ran the checker adversarially rather than reading it. Every command and its **unpiped** exit code (routine **D41** — a pipeline's status is the last command's; my first pass read `head`'s status and nearly produced a false finding).

| Experiment | Result |
|---|---|
| `--status` on a gate whose CHECK writes a sentinel file | **Sentinel NOT created.** Non-execution is real. |
| Normal mode, unapproved oracle | Prints the **fully resolved** oracle — CHECK, EXPECT, CWD, SHELL, full PATH — then `NOT RUN: inspect this oracle, then re-run with --approve`. **Sentinel NOT created.** |
| `--approve` | Writes a sha256-named approval record, executes, `PASS`. **Sentinel created.** |
| exit 0 + non-matching EXPECT | **FAIL** ✅ |
| matching EXPECT + exit 3 | **FAIL** ✅ |
| Empty `EXPECT:` | **Refused, exit 2**, clear diagnostic ✅ |
| `EXPECT: .*` | **FAIL** — expectations are literal substrings, not regex ✅ |
| `EXPECT: /.*/ ` | **🔴 PASS** — the opt-in regex form (`gates.mjs:51`) accepts a catch-all |

**The consent boundary is genuinely fail-closed** — the best consent implementation I have measured since v244's exact-`YES` gate, and unlike that one it sits on the execution path of the product's primary function.

**The approval binding is exactly as documented.** `gate-check.mjs:312` `oracle()` returns `{schema, check, expect, cwd, shell, timeoutMs, maxOutputBytes, regexTimeoutMs, platform, path}`; `:328` `signature()` = `sha256(JSON.stringify(oracle(...)))`; `:340` `approvalPath()` = `sha256(absLedger + NUL + gateId + NUL + signature)`. SECURITY.md:16's claim is true **field by field** — I checked each one.

⭐ And `gate-check.mjs:337-344` refuses an `UNLAZY_APPROVAL_DIR` **inside the repository root**, so a hostile repository cannot ship its own pre-approvals. **A repository cannot vouch for itself.** That hole was closed by an *outside contributor* (`6e23038`, marce: *"fix: keep approval state out of the directory being checked"*).

### 🔴 Where it does not hold

**A gate can lie, trivially.** A gate titled *"every payment migration path is verified against production data"* with `CHECK: node -e "console.log('migration verification passed')"` was certified `PASS`, its box flipped to `[x]`, and the ledger now carries an EVIDENCE line reading `exit=0; shell=/bin/sh; cwd=…; output=migration verification passed`. **The ledger is now an evidence-bearing document asserting production verification that never happened.**

This is **documented, not hidden** — `SKILL.md:61` and `references/gates.md:93`, which states the case with unusual candour: *"`G1: invoices reconcile` plus `CHECK: node -e "console.log('ok')"` is syntactically valid and **semantically useless**."*

⭐ **unlazy makes incompleteness visible; it cannot make completeness true.** The green checkmark carries exactly as much information as the human review of the CHECK line, and no more.

**🔴 The stale-green window.** With an approved gate at `[x]`, mutating its `CHECK` by one character produces:

```
--status     → ALL MET, exit 0     🔴
normal mode  → ALL MET, exit 0     🔴
--reverify   → UNMET,   exit 1     ✅
```

`--status` is the command `SKILL.md:14-17` and `SECURITY.md:11` tell you to run **first** on an inherited ledger — and it cannot see that the evidence was produced by a command no longer in the file. Worse: when the mutated oracle is unapproved, `--reverify` reports UNMET **but does not rewrite the ledger**, so the file keeps `[x]` and the next `--status` says `ALL MET` again.

**Narrowed in the project's favour:** this is *declared*. `references/gates.md:57` — *"`--status` … **does not revalidate old evidence**"*; `references/orchestration.md:35` — *"**`--status` alone is not re-verification.** If an approved oracle changed, inspect it and approve the new oracle before continuing."* So it is a documented hazard with a documented mitigation, not a concealed bug.

⭐ But note the structural tension, which is real and unresolved: **you cannot verify evidence without re-executing, and you cannot re-execute what you are refusing to run.** The non-executing inspection path *structurally* cannot detect a swapped oracle. The cheap fix is one field — **bind the evidence line to a hash of the oracle that produced it** — using a hash `gate-check.mjs:328` already computes.

---

## 5. ⭐⭐⭐ The enforcement census

### `tests/self-check.mjs` — a CI check that polices the project's own declared invariants

Nine checks, and they are meta-checks on the project's claims rather than on its behaviour:

1. zero non-stdlib imports → enforces README:36's "no third-party runtime packages"
2. **one shared gate parser** → the exact defect v269's subject shipped, gated here
3. no index-arithmetic argument filtering → enforces the fix for the bug PR #3 reported
4. gate files are written atomically
5. checks wait for close and cap output
6. approval identity binds execution semantics
7. the hook resolves a scope rather than globbing the tree
8. every reference doc the skill links to exists
9. all executable sources retain the Node 16 floor

**This is the artifact the vault has been looking for since v261** — a check whose subject is *"am I still doing what I said I do."*

### 🔴 And check 8 has the v269 defect, verified in my own read

`tests/self-check.mjs:95`:

```js
for (const m of skill.matchAll(/\]\((references\/[^)]+|templates\/[^)]+|scripts\/[^)]+)\)/g)) {
```

The check is named **"every reference doc the skill links to exists."** SKILL.md contains **8** links. The regex whitelists **three directory prefixes**, so it sees **6**. The two it cannot see are **both `SECURITY.md`** (`SKILL.md:26` and `:84`) — the threat model, the one document SKILL.md tells you to read before executing code from an untrusted repository.

Both links resolve today, so this is a **coverage** defect, not breakage (the v268 distinction). **A hand-written prefix list cannot see a link class nobody listed** — v269's rule at N=2, in an independent codebase, one ship later.

### Gated vs ungated

| Enforced | Declared, not enforced |
|---|---|
| `npm test` on push **and** PR, 9 jobs, no path filters | the GitHub description |
| 2/2 actions **SHA-pinned**; `permissions: contents: read`; `persist-credentials: false` | 12 research URLs — **no link checker, no liveness check** |
| No `postinstall`/`prepare`/`preinstall` script | CONTRIBUTING rule 6 ("make claims exact") |
| Parser, approval, lease, hook, installer behaviour (64 assertions) | CONTRIBUTING rule 9 (no em/en dash) — trivially lintable, unlinted |
| 4 installer tests + 6 hook tests | version↔tag relationship |
| | **the entire orchestration state machine** |

**⭐⭐⭐ The structural finding: unlazy is two products in one repository, and only one is enforced.** The five declared leaf states — `WAITING`, `READY`, `IN-FLIGHT`, `VERIFIED`, `ABANDONED` — appear:

```
scripts/  = 0 occurrences
tests/    = 0 occurrences
references/ + templates/ = 31 occurrences
```

The **gate half** is 1,570 lines of code with 1,290 lines of tests and a fail-closed trust boundary I attacked and could not break. The **orchestration half** — a five-state machine, a rolling-dispatch driver loop, a four-tier verification hierarchy — is **instructions to a model, with zero lines of enforcement.**

That is not hypocrisy; it is the boundary of the technique, and the project says so. `references/orchestration.md:75`: *"**Leaf self-check:** catches ordinary incompleteness but **remains self-certification**."* `:91`: *"Do not call a leaf `VERIFIED` merely because every runnable gate passed."* CHANGELOG:57 states the ambition — *"Moved completion enforcement from prose into gate files, runnable checks, evidence"* — and the project achieved it **for the half where completion is a fact about a file, and could not for the half where completion is a judgement about work.**

---

## 6. ⭐⭐⭐⭐⭐ The research honesty — the strongest I have measured in 274 subjects

**`research/validation-protocol.md` retracts the maintainer's own headline numbers, in-tree, unprompted:**

> `:12` — "Earlier documentation reported output-token ratios, self-found defect counts, one live failure, and report-number errors. **This repository does not contain the exact prompts, model and harness versions, transcripts, token logs, output repositories, reviewer forms, browser recordings, or calculation code for those six runs. The reported numbers therefore cannot be independently reproduced or audited from source.**"
> `:14` — "Treat the historical comparison as design provenance only. It is too small for broad model claims and **must not be described as proof that unlazy causes a specific improvement or cost multiplier.**"
> `:81` — "Those software tests validate implementation behavior; **they do not validate broad claims about model psychology or task productivity.**"

**The retraction appears in five separate documents, six places:** `README.md:209` · `CHANGELOG.md:65` · `references/method.md:5` · `references/token-economy.md:39` · `research/validation-protocol.md:12` and `:14`.

Contrast the recent run: **v238**'s inflated "98/99" was retracted by *someone else's issue*. **v273**'s *"fastest memory layer in the world"* had **zero** measurement and stayed at HEAD. **v272** shipped a machine-readable file denying a paid tier its own landing page sells. Here the author removed his own best marketing numbers from his own README and wrote a five-section reproducibility protocol explaining how someone could earn them back.

⭐ `:81` deserves its own line, because it is the distinction v262 reached for and this project wrote down first: **a green test suite proves the things the tests test, and nothing beyond.**

### The citations

**12 sources.** The fleet's citation dimension verified all 12 exist, with titles verbatim, dates matching the README's declared ordering rule, and correct newest-first ordering. I spot-checked the two most load-bearing myself:

- ✅ **SlopCodeBench** (`arXiv:2603.24755`, v2 dated 7 May 2026 = the README's `2026-05-07`): the abstract says *"no agent fully solves any problem end-to-end"* and *"the best agent passes 14.8% of checkpoints"*. **README:204 is exact, both clauses.**
- ⚠️ **METR Time Horizon 1.1** — **NOT ESTABLISHED by me.** README:206 claims a `196.5`-day overall P50 doubling-time fit and `130.8` days post-2023. The page contains **195.8, 196.5, 165.3 and 130.8**, and a markdown conversion cannot reliably attribute figures to labels (the v270 lesson). I will not call it right or wrong. Noting in the project's favour: CONTRIBUTING.md:20 requires contributors to *"distinguish … **an overall fit from a subset fit**"*, and README:206 itself warns *"The shorter figure must not be described as the all-years estimate"* — a sophisticated distinction that argues for care, though it is evidence about care, not about the number.

⭐ Every research claim carries a hedge that *limits* it: *"it is not a claim that one token always improves work"* · *"Checkpoint success is not task completion"* · *"Research supports the failure modes that motivate explicit structure; **it does not prove that unlazy produces a fixed improvement**"* (README:200).

---

## 7. The Claude-specific surface, and the sharpest technical defect

**Vendor census across all 28 files:** `Claude` **46** · `Codex` **4** · `OpenAI` **3** · `GPT` **1** · `Anthropic` **0** · Cursor/Gemini **0**.

⚠️ **And the asymmetry:** `SKILL.md:3`'s `description` frontmatter — the field an agent reads to decide whether to activate the skill — says *"Use when **Codex** faces a long or multi-part task."* The only deep harness integration is the **Claude Code Stop hook**; the only agent-metadata file is **`agents/openai.yaml`** (there is no `agents/claude.yaml`). The product is Claude-Code-first in its engineering and Codex-first in its activation metadata — and **no test reads that field.**

### 🔴 The Stop hook reimplements a platform guard instead of reading it

I checked the contract three ways, because a first-pass agent returned a **CRITICAL** defect here that turned out to be **wrong**.

**REFUTED:** the claim that unlazy emits the wrong JSON shape. Anthropic's hooks guide states: *"PostToolUse and **Stop** hooks use a **top-level `decision: "block"`** field, while `PermissionRequest` uses `hookSpecificOutput.decision.behavior`."* unlazy emits `{"decision":"block","reason":…}` at `stop-hook.mjs:126-127` — **the documented form.** Its README claim is **true**. The agent appears to have mistaken the PermissionRequest schema for Stop's and reported a nonexistent contradiction between two Anthropic pages. *(My own fetch of the hooks page truncated before the per-event section, so the "two pages contradict" claim is NOT ESTABLISHED either way; the top-level form is confirmed documented.)*

**CONFIRMED, and it is the better finding:**

```
grep -n "stop_hook_active\|stopHookActive" scripts/*.mjs tests/*.mjs
>>> ZERO OCCURRENCES IN THE ENTIRE REPO <<<
```

The hook reads `payload.cwd` (`:29`) and `payload.session_id` (`:30`) and nothing else. Anthropic's guide says: *"Claude Code overrides a Stop hook after it blocks **eight times in a row** without progress. Your hook script **needs to check** whether it already triggered a continuation. **Parse the `stop_hook_active` field** from the JSON input and exit early if it's `true`."* unlazy instead hardcodes `MAX_BLOCKS = 6` (`:11`) with its own state file and sha256 progress hash.

⭐⭐⭐ **A tool whose entire thesis is "do not self-certify — check against an authoritative external oracle" substituted its own bookkeeping for the platform's authoritative signal.** It is a small, precise instance of exactly the error the product exists to prevent. In fairness the reimplementation is *stricter* (6 < 8) and demonstrably terminating — I traced the release path — so it is a correctness-of-approach defect, not a hang.

⭐⭐ **And a missed connection worth more than the defect.** `stop-hook.mjs:130` tells the model: *"Use `ABANDON: <id> <non-blank reason>` only when a gate is **genuinely impossible**."* Claude Code documents a Stop-hook response field **`impossible: true`**, whose meaning is "this condition can never be satisfied — allow the stop." **unlazy invented `ABANDON:` for a concept the platform models natively, and the two never meet.** A hook that knows a gate is abandoned could set `impossible: true` and let the turn end cleanly. *(Recorded as an observation; per §43.3 a wiki documents its subject and does not repair it.)*

Minor: `stop-hook.mjs:17` emits `{systemMessage: …}` on the allow path — documented for PreToolUse/PermissionRequest, not for Stop. Harmless (unknown fields are ignored on exit 0), but undocumented for this event.

---

## 8. ⭐⭐⭐ The community — and what is sitting open

Seven outside contributors, 14 of 31 commits, 13 days. **16 PRs total** (13 closed, 3 open). Real fixes, not cosmetics:

- `e70a5da` **silvereyes137-eng** — *"gate-check drops the first file argument when `--timeout` is absent"* (an argument-parsing bug; the fix became self-check #3)
- `b72e5e4` **marce** — *"run a gate file's CHECK commands only after `--approve`"* — **the entire consent boundary arrived as an outside contribution**
- `6e23038` **marce** — *"keep approval state out of the directory being checked"* — closed the self-approval hole
- `983dc01` **Heeyun Cho** — scoped gate enforcement to one pipeline + concurrency-safe writes
- `ce2092b` **Vishal Sachdev** — *"docs(gates): three authoring rules for gates that cannot fail"*
- `83be6b4` **chrono-meta** — added the COLM 2026 source

⭐⭐⭐ **Note `ce2092b`'s title.** An outside contributor independently arrived at *"gates that cannot fail"* — the exact concept this corpus named at **v262**. And the still-open **PR #17** (Dalydoo) is titled *"**feat: lint ledgers for oracles that cannot fail**"* — a mechanical detector for the false-green hole I demonstrated in §4. The community converged on the corpus's own finding twice: once as merged documentation, once as an unmerged linter.

⚠️ **All three open PRs were opened 2026-08-23 — one day before this ship.** This is **not** v266's pathology (fixes rotting for 82 days); it is a maintainer who has not yet had a day. The interesting fact is *what* is offered, not that it is unmerged. Also open: **PR #20** (win32 orphaned-process kill on timeout) and **PR #18** (parallel dispatch launch waves).

**Issue #19** (joshuaswarren) reports a real production user — *"We are using the skill + `gate-check.mjs` heavily"* — whose Claude Code Stop hook misbehaves inside **omp (Oh My Pi)** / **herdr** panes, and offers a companion extension (`joshuaswarren/omp-unlazy-guard`, MIT, credits unlazy) as *"a soft offer, not a request to merge."*

⭐ **A web search indicates `oh-my-pi` is by can1357 (Can Bölük) and is a fork of `pi-mono` by Mario Zechner** — which is **corpus v36** (matured into `earendil-works/pi` at **v228**) — and **`herdr` is an existing vault topic** ("Rust tmux for AI agents"). ⚠️ **Extent of my check:** the fork relationship is **search-derived only**; the companion repo names no URL for either project, and I did not verify the fork in-repo. So this is a **#57-adjacent ecosystem link, not a dependency** — unlazy does not depend on omp; a third-party user is wiring the two together. Recorded with that caveat, not claimed.

### ⭐⭐⭐ The octopus merge — and a correction to my own first reading

I initially recorded that CHANGELOG:44-53 credits eight PRs while "only five have merge commits," inferring the other four were rewritten rather than merged. **That was wrong, and I caught it by reading parents instead of titles.**

```
git cat-file -p 19d1b04 | grep ^parent   →  5 parents
```

**`19d1b04` — titled merely *"feat: harden scoped gates and complete 2.1.0"*, with no "Merge" prefix — is a 5-parent octopus merge.** Its parents are `380f8c9` (the PR #15 merge), `40570e1` (elkaix), `7766214` (abhil), `6e23038` (marce) and `983dc01` (Heeyun Cho). Diffstat: **27 files changed, +3,730 −818**.

So **all eight credited PRs are genuinely in the history** — four through ordinary merges, four through the octopus. The CHANGELOG's credit is **accurate**, not merely generous. And the three duplicate commit messages are explained: the maintainer **cherry-picked** contributor fixes onto `main` early, then the octopus brought the original branches in with authorship preserved. The duplication is a consequence of the integration strategy, not carelessness.

⭐ **And the octopus created the entire test suite in one commit** — `hardening-tests.mjs` 460, `run-tests.mjs` 435, `self-check.mjs` 120, `stress-tests.mjs` 264. **All 64 assertions, and the whole self-check idea, are one day old** (2026-08-23), not the product of 13 days of accretion.

**Merge latency is genuinely fast:** PR #14 11h · PR #15 17h · PR #8 1d 23h · PR #3 2d 16h — every PR integrated inside 48 hours, no backlog.

### 🔴 PR #20's Windows bug is real, and the code knows

`scripts/gate-check.mjs:437-447`:

```js
const stopChild = () => {
  if (closeStreamsTimer) return;
  try {
    if (process.platform === "win32") child.kill("SIGKILL");
    else process.kill(-child.pid, "SIGKILL");
  } catch { … }
  // A descendant that escaped the shell can otherwise keep inherited pipes
  // open forever. …
```

With `detached: process.platform !== "win32"` at `:470`, the Unix path puts the child in its own process group and `kill(-pid)` kills **the group**. Windows has no group here, so `child.kill()` kills only **the immediate process**, leaving descendants alive holding the inherited pipes — the exact failure the comment at `:445` names. The author saw the failure mode, fixed it on Unix, and left Windows with a mitigation (destroy stdio after a grace period) rather than a fix.

⭐⭐⭐ **And this is the sharpest instance of the ship's theme inside the code:** the CI matrix runs **Windows in 3 of its 9 jobs**, every suite passes on Windows, and the Windows process-kill path is still wrong — because **no test covers timeout-orphaning**. A green three-OS matrix proves the tests pass on three operating systems. That is v262's rule, in the repository best equipped to have avoided it: *tests do not make you honest, they make you honest about the things they test.*

**Minor blemishes:** one commit carries the placeholder author email `abhil@example.com`; and the `origin/v1` branch pointer added at `ed9e8d2` (2026-08-11) was **deleted by `19d1b04`** — so the branch preserved for users of the original single-file skill still exists with its only signpost removed. Note the direction: here the tree **lost a true statement** while the description **kept a false one**.

---

## 9. Verdict, mint, and bookkeeping

**Phase 0.9:** **GOAL-ALIGNED INCLUDE 3/4** — (a) **FAIL** (solo Munich indie developer; `Anthropic` = 0 mentions; §41 permits no rescue on name, notability or locale) · (b) **STRONG** (a Claude Code skill for autonomous-agent completion discipline — Goal #1 dead centre, no §40 needed) · (c) **STRONG** · (d) **STRONG**. Cleanly GA; no override.

**MINT — NO MINT.** Counts **46 / 12 UNCHANGED**; **§C-1 12**; **§C-2 39**.

**Corpus-first VERIFIED at full vault extent** (every file, all dotdirs, `.git/` excluded): `unlazy` 0 · `Depth Tree` 0 · `gate-check` 0 · `GATES.md` 0 · `lexn.lin` 0. Positive controls all fire: `taste-skill` 113, `munder-difflin` 6, `OpenViking` 9, `HiThink` 10. `Leon Lin` = 26 files — the v81 same-author collision, correctly detected.

**Declined a fresh §C-2 row** on: form-factor-within-a-genre (an agent skill — a genre ruled on at v168, v204, v218); **not world-first** (the vault's own v107 registered an enforced-gate operating loop, and v189's loop-engineering ships a REJECT-first verifier and a budget kill-switch); and because the subject is worth far more resolving a standing N=1 than adding a 40th catalogue row. **§28 was not the sole ground** (§44.5).

### ⭐⭐⭐⭐⭐ The audit item this ship hands forward

**`_state/03c:246` registered, at v107 (2026-05-29), a T1 sub-archetype: "Autonomous Plan→Work→Review Operating-Loop Harness (Enforced-Gate)" at PROVISIONAL N=1.** `_patterns/01-audit-history.md:1407` records it *"HELD PROVISIONAL N=1 (N=2 watch)"*, and **:1439** schedules it: *"**Spillover to ~v115:** … v107 Enforced-Gate sub-archetype **N=2**."*

**It is now v274. The watch has been open for 167 ships.**

**unlazy is the cleanest possible N=2** — independent author, cross-domain (v107 was Japan-located `claude-code-harness`), non-port, and it is *literally* an enforced-gate operating loop whose gates are runnable. **Recorded, NOT self-executed** — a promotion is an audit act (§42.5, the v235 discipline).

⭐ And the item is thematically exact: **a watch the vault declared, scheduled, and never enforced — handed forward by a ship about enforcement.**

**Recorded instance-strengthening (not self-incremented):** Pattern **#88** 88c machinery-with-enforcement, on a new sub-domain axis (anti-**laziness**/completion rather than aesthetic slop) · Pattern **#84** 84c cross-vendor ecosystem tolerance (Claude Code + Codex CLI + `agents/openai.yaml` via the `npx skills` CLI) · Pattern **#83** honest-deficiency-disclosure — **at its corpus maximum**, five documents retracting the author's own numbers.

**Two DEFERRED watch axes:** *a retracted claim surviving in repository metadata that is outside both CI and the author's editing habit* (N=1) · *a skill whose activation `description` names a different harness than the one it integrates with* (N=1).

**Streak:** v273 `GA:130` → **`GA:131 · OG:13 [7 ov]` — 54 consecutive GA v220→v274. §35 CLEAR** ({v272, v273, v274} = 0 OG). **Override review: 14th consecutive discharge.**

---

## 10. Method notes

⚠️ **My own errors, all caught by re-measurement rather than re-reading (§43.1, fourth consecutive ship):**

1. **I called this ship v271 for most of the session.** HEAD is `14387b7` = **v273** and the state file's highest entry is v273, so this is **v274**. I anchored on a stale first `git log` read and carried the number forward without re-measuring — the exact failure class this ship documents.
2. **I read exit codes through a pipe** (`node … | grep | head; echo $?`) and briefly had an inverted picture of the `--reverify` behaviour. **D41.** Re-running unpiped produced the correct — and much sharper — stale-green finding.
3. I initially wrote that the mutation test "failed the project's claim." The fair test (`--reverify`) showed the tool fail-closed correctly; the real finding was narrower and better.
4. **I mis-framed the PR-credit story** by reading merge *titles* instead of merge *parents*, and concluded four contributions had been rewritten-but-credited. `19d1b04` is a **5-parent octopus merge**; all eight credited PRs are in the history. **The fleet caught this and I did not** — the correction is theirs, and it made the community section better. Reading `git cat-file -p <sha> | grep ^parent` is now the habit; a merge does not have to say "Merge".

⭐ Errors 1 and 4 share one cause and it is **§43.1 verbatim**: both came from generalising off a surface I had chosen to look at (a stale `git log` line; a set of merge subjects) rather than from a command whose semantics *are* the definition. Both were caught by re-measuring, not by re-reading.

⚠️ **Fleet reliability — four claims REFUTED by my own hand-checks:**

| Fleet claim | Reality |
|---|---|
| "CWD does not invalidate approvals" | **REFUTED** — `cwd` is bound at `gate-check.mjs:312`, and the project's own hardening test asserting it passed in my run |
| "README repository map omits 7 files (HIGH defect)" | **REFUTED** — the map is directory-level for `scripts/`/`tests/`/`templates/`; complete at its own granularity |
| "ZERO tests cover the installer / uninstall sibling-preservation" | **REFUTED** — 4 installer + 6 hook tests; I watched *"install: uninstall removes our entry and leaves others alone"* pass |
| "CRITICAL: wrong Stop-hook JSON shape; two Anthropic pages contradict" | **REFUTED** — top-level `decision:"block"` is the documented form; the contradiction was not established and looks like PermissionRequest confusion |

⚠️ **D51 at three data points in one ship:** the same CHANGELOG retraction was cited by three agents at lines **32**, **57** and **59** (it is **59**), and the approval machinery at **441/449/460** (it is **312/328/340**). **Line numbers drift; the underlying facts were right.** Every `path:line` in this document is from my own command output.

⚠️ **NOT ESTABLISHED, stated with extent:** the METR figures (four numbers on one page, markdown conversion cannot attribute them) · whether a separate Anthropic per-event reference page shows a `hookSpecificOutput` wrapper for Stop (my fetch truncated before that section) · the `oh-my-pi` ← `pi-mono` fork relationship (search-derived only) · whether *"the skill validator"* at CONTRIBUTING.md:48 refers to an external tool — **no such tool is in the tree, declared as a dependency, or invoked by CI**, and I could not establish what it means · whether the author's public-repo count genuinely fell from 104 (v81) to 39 (today), since a paginated listing may undercount.

**Fleet:** 13 dimensions attempted across two workflows. First run: 8 of 10 finders returned, all 10 refuters and 2 finders died (host sleep + retry-cap); recovered from `journal.jsonl` per **D43** rather than re-run. Second run: 2 of 4 returned. **Hand-coverage filled every gap**, and the two most load-bearing findings in this document (the description drift and the same-author control) were established by me before the fleet launched.

**Sandbox:** `python3` is SIGKILLed; **`node -e` is blocked** (write a `.js` file and run it); git is 2.19 (`git branch --show-current` does not exist).
