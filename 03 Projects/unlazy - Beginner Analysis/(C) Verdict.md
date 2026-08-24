# (C) unlazy — Verdict

**v274** · `Leonxlnx/unlazy` · 2026-08-24 · HEAD `754d9a68` · MIT · v2.1.0 (untagged)

---

## The one-paragraph verdict

A 13-day-old, 2,860-line, zero-dependency agent skill that refuses to let an AI agent call a task finished on its own word. It replaces the confident done-report with a markdown acceptance ledger whose gates carry runnable commands, requires explicit `--approve` before it will execute any of them, and optionally installs a Claude Code Stop hook that structurally blocks the agent from ending while gates remain unmet. **I attacked the trust boundary and it held.** 64 of 64 tests pass on my machine; CI runs them on push *and* pull request across nine platform combinations with both actions SHA-pinned. **And its own README, its CHANGELOG, its method doc, its token doc and a dedicated protocol file all retract the author's own headline benchmark numbers as unreproducible — five documents, six places.** That is the strongest in-tree self-retraction I have measured in 274 subjects.

**The defect is not in the code. It is in the one sentence that lives outside it.** The GitHub repository description still advertises the arithmetic effort-multiplier claim that the repository retracted on day one — because a description is not a file, so no test can reach it and the author's own careful editing pass never touches it.

---

## Scores

| Criterion | Result | Basis |
|---|---|---|
| **(a) Anthropic / vendor-direct** | **FAIL** | Leon Lin, solo indie developer, Munich. `Anthropic` = **0** mentions in the repo. §41 permits no rescue on name, notability or locale. |
| **(b) Goal relevance** | **STRONG** | A Claude Code skill for autonomous-agent completion discipline. Goal #1 dead centre. No §40 needed. |
| **(c) Substance** | **STRONG** | 2,860 lines tested by 1,290; a real threat model; a reproducibility protocol; a fail-closed consent boundary I verified by running it. |
| **(d) Actionability** | **STRONG** | Installable at low risk; and the highest-value part — the ledger format and the authoring rules — needs no install at all. |

**GOAL-ALIGNED INCLUDE 3/4.** Cleanly GA, no override.
**MINT: NO MINT.** Counts **46 / 12 UNCHANGED** · §C-1 **12** · §C-2 **39**.
**Streak:** `GA:131 · OG:13 [7 ov]` — **54 consecutive GA v220→v274**. §35 **CLEAR**. Override review: **14th consecutive discharge**.

---

## What is genuinely excellent

1. **⭐⭐⭐⭐⭐ It retracts its own numbers, five times over.** `research/validation-protocol.md:12` — *"This repository does not contain the exact prompts, model and harness versions, transcripts, token logs … The reported numbers therefore cannot be independently reproduced or audited from source."* `:14` — *"must not be described as proof that unlazy causes a specific improvement or cost multiplier."* `:81` — *"Those software tests validate implementation behavior; **they do not validate broad claims about model psychology or task productivity.**"* Compare v238 (retracted by someone else's issue), v273 ("fastest memory layer in the world", zero measurement, still at HEAD), v272 (a machine-readable file denying a paid tier its own site sells).

2. **⭐⭐⭐⭐⭐ A fail-closed consent gate on the primary execution path.** Three states, verified by running them: `--status` never executes (my sentinel file was never created), normal mode prints the fully-resolved oracle and refuses, `--approve` executes. The approval key is `sha256` over **ten bound fields** including `cwd`, resolved shell, and the full inherited `PATH` (`gate-check.mjs:312/328/340`) — SECURITY.md:16's claim is true field by field. And `:337-344` refuses an approval directory **inside** the repository, so **a hostile repo cannot ship its own pre-approvals.**

3. **⭐⭐⭐⭐ `tests/self-check.mjs` — nine CI checks whose subject is the project's own declared invariants**, including *"zero non-stdlib imports"*, *"**one shared gate parser**"* (the exact defect v269's subject shipped), and *"all executable sources retain the Node 16 floor"*. This is the artifact the vault has been circling since v261.

4. **⭐⭐⭐⭐ It states its own central limitation plainly, in three documents.** `references/gates.md:93` — *"`G1: invoices reconcile` plus `CHECK: node -e "console.log('ok')"` is syntactically valid and **semantically useless**."* `SKILL.md:61` — the checker *"cannot infer whether an English gate title describes what the command actually measures."* `references/orchestration.md:75` — *"**Leaf self-check** … remains **self-certification**."*

5. **⭐⭐⭐ Authoring rules that are the corpus's own method, independently derived:** *"Exercise a negative check against a known positive control before trusting absence"* · *"Measure figures independently; do not copy a supplied number into `EXPECT:` as its own proof"* · *"Re-measure every number and completion claim immediately before reporting"* · and `orchestration.md:35`'s *"**try to refute at least one passed gate**"* — which is this vault's `loop-verifier` maker/checker split, written by someone else.

6. **⭐⭐ Supply chain and community.** 2/2 actions SHA-pinned; `permissions: contents: read`; `persist-credentials: false`; **no `postinstall`/`prepare` script**; zero third-party runtime packages. Seven outside contributors in 13 days, every PR merged inside 48 hours — and **the entire `--approve` consent boundary arrived as an outside contribution** (`b72e5e4`).

---

## Where it does not hold

| 🔴 | Finding | Evidence |
|---|---|---|
| **1** | **A gate can lie, trivially.** A gate titled *"every payment migration path is verified against production data"* with `CHECK: node -e "console.log('migration verification passed')"` is certified `PASS`, flipped to `[x]`, and given an EVIDENCE line. | I ran it. Documented at `SKILL.md:61` / `gates.md:93`, so honest — but it means **a green ledger carries exactly the information content of the human review of its CHECK lines, and no more.** |
| **2** | **The stale-green window.** With an approved gate at `[x]`, mutating its `CHECK` by one character leaves `--status` and normal mode reporting **`ALL MET`, exit 0**. Only `--reverify` catches it (UNMET, exit 1) — and when the mutated oracle is unapproved, `--reverify` does **not** rewrite the ledger, so the next `--status` says `ALL MET` again. | Verified with unpiped exit codes. `--status` is the command `SECURITY.md:11` tells you to run **first** on an inherited ledger. **Declared** at `gates.md:57` and `orchestration.md:35`, so a documented hazard — but the cheap fix is one field: bind the EVIDENCE line to a hash of the oracle that produced it, using the hash `:328` already computes. |
| **3** | **`EXPECT: /.*/` passes.** The opt-in regex form accepts a catch-all. | Bare `.*` correctly fails (expectations are literal), but the `/…/` form does not screen for unfalsifiability. **Open PR #17 — *"lint ledgers for oracles that cannot fail"* — targets exactly this.** |
| **4** | **The Stop hook reimplements a platform guard instead of reading it.** `stop_hook_active` — the documented loop-safety field Anthropic's guide says a hook *"needs to check"* — appears **zero times in the entire repo**. unlazy hardcodes `MAX_BLOCKS = 6` against the platform's 8-block cap. | ⭐ **A tool whose thesis is "check against an authoritative external oracle" substituted its own bookkeeping for the platform's authoritative signal.** In fairness: stricter (6<8) and demonstrably terminating. |
| **5** | **Half the product has no enforcement.** The five declared orchestration states appear **0 times in `scripts/`, 0 in `tests/`, 31 times in `references/`+`templates/`**. | Not hypocrisy — the boundary of the technique, and the docs say so. But *"moved enforcement from prose into runnable checks"* (CHANGELOG:57) is true of the gate half only. |
| **6** | **The link self-check covers 6 of SKILL.md's 8 links.** `self-check.mjs:95`'s regex whitelists three directory prefixes; the two invisible links are **both `SECURITY.md`** — the threat model. | Coverage, not breakage (both resolve). **v269's rule at N=2 in an independent codebase.** |
| **7** | **The Windows timeout path leaks descendants.** `gate-check.mjs:440` kills only the immediate process on win32 while Unix kills the group. The comment at `:445` names the failure mode. | ⭐ **CI runs Windows in 3 of 9 jobs and every suite passes** — because no test covers timeout-orphaning. Open PR #20 fixes it. |
| **8** | **The activation metadata names the wrong harness.** `SKILL.md:3`'s `description` — the field an agent reads to decide whether to fire — says *"Use when **Codex** faces a long or multi-part task,"* while `Claude` appears 46 times, the only deep integration is the Claude Code hook, and the only agent-metadata file is `agents/openai.yaml`. | No test reads that field. |

---

## ⭐⭐⭐⭐⭐ The rule, and the ladder

> **A claim is safe when a gate covers it, or when a habit covers it. The GitHub description had neither.**

The habit is real and I measured it: CONTRIBUTING.md:23 forbids em and en dashes, nothing enforces it, and there are **zero of either across all 28 tracked files** (positive control: 9 hyphen matches). **The prose rules hold because one careful person writes all the prose; the code rules are gated because seven strangers touch the code.** The description is outside CI *and* outside the file that careful person edits.

**v267** discipline stops where the artifact stops being code → **v268** a gate exists where a reader can refuse → **v269** no gate sees an entry never added → **v270** no gate fires on a claim true when written → **v271** a gate's scope is inherited from where it lives → **v272** a gate holds when something else already requires it → **v273** a check is only as permanent as the place you put it → **v274 neither a gate nor a habit reaches a claim stored outside the repository.**

---

## ⭐⭐⭐⭐⭐ The §42 same-author result

The same developer, in the same six months: **taste-skill** (corpus v81) — 153 commits, 64 files, **79,622 stars**, `.github/` containing exactly `FUNDING.yml` and `copilot-instructions.md`, **zero workflows, zero `package.json`, zero tests**. And **unlazy** — 13 days old, 1,468 stars, four test suites, 64 assertions, nine CI jobs.

**The engineering discipline is not a property of the developer. It is a property of what the artifact claims.** taste-skill claims *taste*, which no test can decide. unlazy claims *verification* — and a tool arguing "prove outcomes against a ledger instead of trusting a confident done report" cannot ship untested without its own thesis indicting it.

**Dispositions** that replicate: the `npx skills` multi-harness install path, the anti-slop→anti-laziness framing, README-as-product-page, overwhelming solo authorship. **Attention** that varies: everything checkable. **N=2 — this supports a mechanism, not a law.**

---

## The audit item

**The vault registered "Autonomous Plan→Work→Review Operating-Loop Harness (Enforced-Gate)" at PROVISIONAL N=1 at v107**, held it as an *"N=2 watch"*, and scheduled that watch for **~v115** (`_patterns/01-audit-history.md:1439`). **It is now v274 — 167 ships.**

**unlazy is the cleanest possible N=2:** independent author, cross-domain, non-port, and literally an enforced-gate operating loop with runnable gates. **Recorded, not self-executed** — a promotion is an audit act.

⭐ The item is exact: **a watch the vault declared, scheduled, and never enforced, handed forward by a ship about enforcement.**

---

## Pilot

**⭐⭐ READ-AND-BORROW FIRST, THEN A FENCED INSTALL.** See `(C) Pilot Methods Menu.md`.

🔴 **The one rule that matters:** **never let an agent pass `--approve` on a ledger it authored itself.** `--approve` is a flag, not a human gate — there is no prompt, no confirmation, no TTY check anywhere in the code. The consent boundary is real against an *inherited* ledger run by a *human*. It is not a boundary against the agent, and the product's primary consumer **is** an agent, which puts the agent on both sides of its own consent gate.

**Never:** `--global` install (writes `~/.claude/settings.json`) · trust `--status` to detect oracle drift on inherited work · cite the six-run numbers (retracted five times) · treat a green ledger as evidence of its English title · treat the green 3-OS matrix as Windows correctness · run without pinning a commit (zero tags exist).
