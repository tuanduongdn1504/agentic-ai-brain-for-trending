# (C) Verdict — `google/artemis` (v285)

**2026-09-13** · HEAD `371aa6df` · Apache-2.0 · ✅ source verified (twin clones, `diff -rq` clean both ways)

---

## Rating

**GOAL-ALIGNED INCLUDE — 3/4**

| Axis | Call | Basis |
|---|---|---|
| **(a) cultural peer** | **FAIL** | Google — corporate, not Anthropic (§41; the v169 NVIDIA precedent). An `ANTHROPIC_API_KEY` slot in `.env.example` is **compatibility, not affiliation** (the v284 precedent). Top committer is a personal Outlook address. |
| **(b) goal relevance** | **STRONG** | An agent perception+control capability layer with a native MCP server that Claude Code can drive — squarely goal #1. |
| **(c) quality** | **STRONG** | 159,769 Python lines, 2,063 test functions, a real 8-node LangGraph state machine, a VLM-backed pre-execution validator. |
| **(d) actionability** | **STRONG** | Apache-2.0, pip-installable, five directly borrowable mechanisms. |

Clean GA. **No §40, no override.**

**Streak:** v284 `GA:141` → **`GA:142 · OG:13 [7 ov]`** — **65 consecutive GA, v220→v285.**
**§35 CLEAR** — window {v283, v284, v285} = 0 OG.
**Override review: 25th consecutive discharge.**

---

## Mint

### NO MINT. Counts **46 / 12 UNCHANGED**. §C-1 **13**, §C-2 **39** — unchanged.

**Collision grep CLEAN** — one hit vault-wide, a binary false positive in an unrelated corpus file. Corpus-first subject; first `google/`-org author in 205 ships.

**Tested against §C-2 C35** (v183 serve-sim) and **declined on that row's own written definition**, which mints an explicit conjunction: *simulator surface × human-watchable live framebuffer stream × camera-injection × Agent-Skill packaging*, on iOS. Artemis is **physical Android**, perceives via **screenshot + UI hierarchy**, has no camera injection, and ships **zero `SKILL.md` / `skills/` / `plugin.json`** — it is MCP + CLI + console. C35's own scope note already names **`mobile-mcp`** among external peers it does not claim, and that is precisely Artemis's class.

> ⭐⭐⭐ **§C-2 earns its keep for the fourth time** — v262 (C37) · v263 (C38) · v284 (C40) · v285 (C35). Reading the row's written definition prevented a false N=2.

**Also declined:** CONFIRMED **#24** (product-first app retrofitted with a first-party MCP server) — Artemis is agent-first from the root commit, never a product retrofitted. **#18 B1-MCP** is a capability match only, no double-count.

**Not world-first.** `mobile-mcp`, `droidrun`, Mobile-Agent, AppAgent and AutoDroid precede — and the project's own leaderboard image lists DroidRun, gbox.ai, Mobile-Agent-v3, MobileUse and UI-TARS as competitors. Corpus-first-for-a-surface ≠ mintable (**v211**).

**⭐ RECORDED, NOT EXECUTED** — for the audit, now ~25 ships overdue:
a §C-2 N=1 candidate, *"Agent-First **Physical**-Mobile-Device Perception+Control Layer whose MCP surface delegates a WHOLE TASK to an autonomous on-device subagent rather than exposing primitive actions."* The distinctive is the **task-not-action MCP interface**; the corpus holds iOS-simulator (C35), browser (C34/C48/C57) and debugger (C58) rows but **no physical-device row**. **Argued against:** not world-first, and the precedent that carried **C58** at N=1 rested on a novel *delivery mechanism* (an in-process debugger plugin) — "an MCP server for a device class" is not that. **I decline it. The audit may disagree.**

---

## ⭐⭐⭐⭐⭐ The rule

> **This repository is rigorous about everything it can COMPUTE and silent or wrong about everything it can only ASSERT — and because the assertions are unusually well written, they read as guarantees.**

Nothing here is careless. The computed parts are excellent; several are the best in recent ships. The asserted parts are false in the specific way well-written prose is false: nobody re-reads a sentence that already sounds right.

**And v283's rule explains which is which:** the statements *co-located with the thing they describe* are correct — the **21** `mobile-use` headers, living inside the derived files. The statements living in **a different file from their subject** are wrong or fragile: the CI claim in `CONTRIBUTING.md`, `change-in-prod` in a config, the 99% in a README describing a deleted harness — and, decisively, **a `NOTICE` that credited two upstreams from outside them and took both down when one revert removed the file.**

---

## The six findings

**1. ⭐⭐⭐⭐⭐ The claim and its evidence were never in the repository at the same time.**
2026-08-13 `206a9ce9`: a **157-line** AndroidWorld harness, **zero** benchmark claims. 2026-08-18 `9a5aaf9`, **one commit**: `D bench.py` + `M README.md` + `A androidworld_benchmark_comparison.png`. The commit message mentions neither. `android_world` is in **none of the 196** locked packages, and the deleted harness **never computed a percentage** — it logged per-task booleans with no accumulator. **No code that has ever been in this repository could produce "99.1%."** `docs/` contains **zero prose**: 21 files, all assets. Then a commit titled *"refresh AndroidWorld benchmark visual"* stripped the sole evidence image of its date, its source line, its benchmark attribution and **all twelve model labels** — keeping the ranks, names and percentages. ⚠️ Decluttering is a plausible motive and intent is not established; the effect does not depend on intent.

**2. ⭐⭐⭐⭐ The counters always run; the tests never do.**
`ruff`, the quality ratchet, `pyright` and the dependency-source gate run on every push and PR. **2,032 test functions and a 60% coverage floor sit behind `if: github.event_name == 'workflow_dispatch'`** — the **only `if:` in the file**, added by a commit whose entire diff is **one line**. `CONTRIBUTING.md:24` says that suite *"is the same suite used by pull-request CI."* It entered at **21:43:57**; the gate that falsified it entered at **23:04:19 the same evening** — **80 minutes**, by the same author, in a commit titled *"ci: run Python tests only on manual dispatch."*
⚠️ **Two qualifiers I got wrong first time.** (a) More executes than "counters" suggests: `frontend` runs `npm test` unconditionally (12 specs, 128 `it(`), `package` builds wheels and runs a CLI smoke test, and CI runs two of the repo's own Python scripts — **Python executes, just never a test.** (b) A further **24 integration + 7 e2e** test functions run under **no CI event at all** — though ✅ that is the *documented* design, since they need devices and credentials. It is the **deterministic** suite, the one the docs call required, that was switched off. The Angular frontend stayed test-gated; the Python core did not.

**3. ⭐⭐⭐⭐⭐ Leaked three times, and every one rode in on a commit about something else.**
The published lockfiles pointed at `http://airlock-proxy.uplink.goog:999/...` — a **Google-internal host over plaintext HTTP** — at `9a5aaf9` (2,955 lines, *"introduce MCP server…"*), at `d23a4f6` (**one** npm entry of 625, *"handle mid-stream LLM resets…"*), and at `3047c9c` (2,982 lines, *"Fix Python code format check issues"*, merged via **PR #24**). **Not one commit title contains "dependency" or "lockfile."** The first fix was titled ***"delet uv.lock"*** and simply **deleted the file** — the instance, not the class. ✅ Severity: all artifacts were `sha256`-pinned throughout and `uv` verifies hashes, so this was availability and internal-infrastructure disclosure, **not** an integrity compromise. ⭐⭐⭐ **And the gate they finally wrote is genuinely good — except its npm half is invoked at exactly one place tree-wide, inside `python-quality`, the only job that never installs npm; the two jobs that do run `npm ci` never call it and there is no `needs:` to sequence them.** *(v271's rule reproduced inside the best artifact in the repo.)*

**4. 🔴🔴🔴 The trust hierarchy is described in detail and computed nowhere — and the description is the exploit.**
The prompt declares the screenshot *"the primary source of truth"* and tells the model that a **`--- User Guidance ---` block in its observation "outranks the task plan."** Screen text enters that observation **unescaped**. So any app rendering that literal delimiter issues a privileged instruction. `open_link` — one of the twelve actions the model can emit — reaches `execute_shell(f"… -d '{url}'")` **unescaped** (`unified_controller.py:224`), while `shlex.quote` *is* used twice elsewhere in the codebase. ⭐⭐⭐ **And the boundary's absence is test-enforced:** the only occurrence of *"Untrusted Screen Content & Instruction Priority"* in the tree is a unit test **asserting it is not in the prompt** — a test which, per finding 2, **never runs.**

**5. 🔴 `locked_app_package` locks nothing, and the proof is one line.**
`git grep "get_locked_app_package"` over the entire repo, tests included, returns **exactly one line: the `def` itself.** Zero call sites. The lock is applied at launch and never again — while `data_engine/engine.py:901-909` **stamps the foreground package onto every recorded step** and never compares it. **The value is measured every step, written to the database, and never checked against the fence that exists to constrain it.**

Plus, in `playground/backend_manager/` — the only component that handles authentication, and outside **all three** gates — `JWT_SECRET_KEY = "…-change-in-prod"`, `DEV_MOCK_OTP = "123456"` accepted on truthiness alone, and:

> ⭐⭐⭐⭐⭐ **`APP_ENV` is declared in config, set to `production` in both deployment files, printed by the health endpoint and logged at startup — and never once used in a conditional. It is a variable that describes the environment to humans and to nothing else.**


**6. ⭐⭐⭐⭐⭐ Two upstream projects, one `NOTICE`, one revert — and only one survives.**
The project is at the centre of a live attribution dispute; **Minitap, Inc. alleges ARTEMIS derives from their Apache-2.0 `mobile-use` with authorship removed.** Verified from my own clones, not from either side: the root commit declares **`version = "3.6.3"`** — mobile-use's own tag — in a commit titled *"initial release"*; `hopper.md` is **byte-identical** there; the root tree holds **0** references to Minitap anywhere; and artemis's `LICENSE` **replaced mobile-use's `Copyright 2025 Minitap, Inc` appendix with `Copyright 2026 Google LLC.`** ⭐⭐⭐⭐⭐ **The sharpest fact is a controlled experiment the repository ran on itself.** A `NOTICE` crediting **two** upstreams — mobile-use *and* `finalrun-agent` — plus **eight named individuals** was added at `54fcef9` (16:19:42), then **deleted at 19:32:22 by a different maintainer reverting the whole commit**, which had bundled the notices with a breaking `hopper`→`entity_extractor` rename. Twenty-seven minutes later, per-file headers were added — **for one upstream only.** At HEAD: Minitap **44 hits / 23 files**; **finalrun-agent 0**; **the eight individuals 0**. **Nobody decided to erase finalrun-agent. The commit boundary decided it.** ⚠️ Effect certain, intent not: the revert **precedes** the Hacker News story by seven minutes, so *"HN forced the fix"* is **not supported**. ⚖️ **And the viral "228 of 229 files identical" figure does not survive contact with the trees** — 229 is merely artemis's file count; **74** paths are shared after normalising the rename and **2** are byte-identical.
---

## What is genuinely excellent

- ⭐⭐ **Attribution — arrived on the last day, for one upstream of two.** 21 files plus both READMEs credit `minitap-ai/mobile-use` by name and link. ⚠️ **I twice got this wrong**: first praising it as the best attribution discipline in recent ships (the headers landed **in HEAD itself**, `371aa6d`, *"per Apache 2.0 requirements"* — at `HEAD~1`, **zero** files carried upstream credit), then reporting zero hits for the removed upstream authors, which was a grep of HEAD only. **A `NOTICE` crediting two upstream projects and eight named people existed for 3 h 12 m, in 1 of 119 commits, and was deleted by a different maintainer's revert of a bundled refactor.** Meanwhile the Google copyright sat on **191 of 192** files **from the root commit**. ⭐⭐⭐ **The stamp that could be applied mechanically was right on day one; the credit that required knowing a fact about provenance took twenty-nine days.** Better than v181 and v267; not a project that did it from the start.
- ⭐⭐⭐ **`check_dependency_sources.py`** — 68 stdlib-only lines running *before* `uv sync`, asserting public registries and HTTPS for every locked artifact. **The exact gate v271 lacked.**
- ⭐⭐⭐ **Privacy.** A tool that continuously screenshots your phone and ships **zero telemetry, zero analytics, no phone-home**. Only the LLM/OCR endpoints you configure.
- ⭐⭐ **`quality_ratchet.py`** — AST-based, and its `silent_broad_exception_handlers` metric is the vault's own **v246** detector as a hard CI gate. Baseline **754/0/18 exact at HEAD, zero headroom**.
- ⭐⭐ **No `0.0.0.0`** in `artemis/`, `mcp_server/` or `apps/`; MCP defaults to stdio, SSE to `127.0.0.1`.
- ⭐⭐ **The "graph orchestration" claim is honest** — 8 nodes, 6 static edges, 3 conditional. *(v284 claimed the same phrase for 2 nodes.)*
- ⭐ **`start.sh`'s `request_sudo()`** prompts interactively and falls back to user-space on refusal.
- ⭐ **The one README count that diverges does so by being too modest** — 9 IDE install targets in code, 3 advertised.

---

## 🔴 NEVERs

1. **Never cite the 99%+ / "SOTA" AndroidWorld figure in any form.** No harness, no dependency, no methodology, no model named, no trial count; the evidence image had its date and source removed.
2. **Never point it at a phone holding real accounts** — banking, email, messages, payments. There is no untrusted-content boundary, no approval gate, and `--- User Guidance ---` is a documented escalation token.
3. **Never rely on `locked_app_package` as a fence.** Its accessor has zero call sites.
4. **Never deploy `playground/backend_manager/` as shipped** — `docker-compose.yml` and `deploy_to_cos.sh` both set `APP_ENV=production` while leaving the published JWT key and `123456` OTP bypass in place, and mount the Docker socket into a root container.
5. **Never assume the Python tests ran.** They do not run on push or PR.
6. **Never treat `mobile_run_task` as annotated** — no `readOnlyHint`/`destructiveHint`; the tool that drives the phone and the tool that reads state are indistinguishable to the protocol.
7. **Never repeat the "228 of 229 files were exactly the same" figure.** I measured it: **74** shared paths after normalising the package rename, **2** byte-identical. The claim is not supported by the trees.
8. **Never say "Google restored attribution" without qualifying it.** The company is credited in 23 files; **finalrun-agent — a second upstream — is credited nowhere, and not one of the eight named individuals appears anywhere in the tree.**

---

## Pilot

**⭐⭐ READ-AND-BORROW. Do not install against anything real.**

The five borrowable mechanisms and the two vault fixes are in **`(C) Pilot Methods Menu.md`**. The highest-value items are `check_dependency_sources.py`'s shape (walk the lockfile, assert the registry *and* the scheme, run before install), and the operator prompt's **anti-self-deception clauses** — *"never write an action's expected outcome as if it had already been observed"*, *"never construct state to satisfy"* an assertion — which are directly portable to `hireui/evals/METHOD.md`.

**Tier:** T2 product / platform — reviewable.

---

## Blunt

A Google-owned repository, written almost entirely by one person in a month, built a device-control agent with a VLM that double-checks the target crop before a tap lands, a supply-chain gate better than anything in the last twenty ships, and an operator prompt so disciplined about self-deception it forbids the agent from claiming an outcome it has not observed.

Then it deleted its benchmark harness and added a 99% claim in the same commit; told contributors that pull-request CI runs a test suite it had switched off eighty minutes earlier; shipped a JWT signing key whose own value says *change-in-prod*; and wrote a unit test to keep the prompt-injection boundary out of the prompt — a test that never runs.

And on its last day it wrote a `NOTICE` crediting two upstream projects and eight people by name, bundled it into a commit that also renamed something, watched a colleague revert the whole commit three hours later, and re-landed the credit as headers **inside** the derived files — which saved the upstream that had files to put them in, and lost the one that did not.

**Every one of those failures is a sentence. Every one of the successes is a computation. The engineering is not the problem and the care is not in doubt — the problem is that this team, like most teams, proofreads its code and merely re-reads its prose.**

> ⭐⭐⭐⭐⭐ **And the attribution is the cleanest proof of the rule the corpus has: the same words, written in two places, had two fates. Inside the files, they survived a revert aimed at something else. In a file of their own, they did not survive at all.**
