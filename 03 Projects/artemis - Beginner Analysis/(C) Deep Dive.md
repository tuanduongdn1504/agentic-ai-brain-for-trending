# (C) Deep Dive — `google/artemis` (v285)

**Subject:** `google/artemis` — **ARTEMIS**, *"Let AI assistants and test suites use real phones like a human."*
**Ship:** v285 · 2026-09-13
**Licence:** Apache-2.0
**HEAD:** `371aa6df56880643da57b30da936e9812fb0ec66`
**Source verification:** ✅ two independent clones, `diff -rq --exclude=.git` **clean in both directions**.

> ⚠️ **Instrument note.** System git is **2.19.0** (the v267 truncation pathology). Every git figure below is from **2.50.1** at `/Library/Developer/CommandLineTools/usr/bin/git`, and every load-bearing count is by **enumeration**, not `grep -c` (clause (g)).

---

## 1. What it is

An Android device-control agent framework. You give it a natural-language task; it drives a **real, physical phone** (or a Cuttlefish AVD) by reading the screen — screenshots plus the UI-hierarchy/accessibility tree — feeding that to a multimodal model, and issuing taps, swipes, text input and key presses over ADB.

It ships four surfaces:

| Surface | What it is |
|---|---|
| Python framework | `artemis/` — the agent, graph, drivers, tools, data engine |
| CLI | `artemis run` / `ui` / `doctor` / `restart` / `stop` / `status` |
| **MCP server** | `mcp_server/` — **5 tools**, so Claude Code / Antigravity / Windsurf can delegate device tasks |
| Web console | `apps/showcase_ui` (Angular) + `apps/admin_console` |

Two execution profiles:
- **Flash** — a reactive observe-and-act loop. Fast, no ADB shell, **no pre-execution safety net**, no plan, no verification.
- **Pro** — graph orchestration with pre-action checks, recovery, notes, checkpoints, ADB shell, written report.

### Census (enumerated at HEAD)

| Metric | Value |
|---|---|
| Commits | **119** (`rev-list --count`) |
| Root commits | **1** — 2026-08-13 |
| Merges | 20 |
| **Tags** | **0** |
| Distinct author emails | **9** |
| Tracked files | **796** |
| Python files | **590** |
| Python lines | **159,769** |
| Test files | **235** |
| **Test functions** | **2,063** |
| Locked Python packages | **196** |
| Age at ship | **~1 month** (last commit 2026-09-11) |

### Authorship — measured by identity, not by email string

⚠️ **My first pass got this wrong in two directions, and an adversarial check corrected it. The corrected version is below.**

There are **9 distinct author emails but only 6 distinct actors** (5 humans + dependabot), because three people commit under two addresses each:

| Actor | Commits | Share |
|---|---|---|
| **`somew1nd`** — `wfq559@outlook.com` (101) **+ `…+somew1nd@users.noreply.github.com` (6)** | **107** | **89.9%** |
| `yaoyao-open-source` — `@google.com` (2) **+ `yaoyaosuper@gmail.com` (4)** | 6 | 5.0% |
| `Weilin Liu` — `@google.com` (1) **+ `weilinliu55` (1)** | 2 | 1.7% |
| dependabot | 2 | 1.7% |
| 2 others | 2 | 1.7% |

**Counting email strings understates Google's involvement by roughly 4×.** Only 3 commits carry an `@google.com` author address — but **by identity it is 8 commits and 52,967 insertions, 16.6% of all 319,277 non-merge insertions**, and those commits deliver **two entire subsystems**: the Angular web UI / execution visualizer (45 files, 27,863 insertions) and the Admin & Trace Console backend (29 files, 8,889). The gmail-addressed commits merge branches literally named `google/playground-submit`.

⚠️ **So the tempting headline — "not really a Google project" — is NOT established by this tree, and I am not asserting it.** Against it: the repo sits in the `google` org, uses `google/*` branch names, took a Google-OSS inclusive-language cleanup from a `@google.com` account on day one, carries Google copyright from the root commit, and `somew1nd` holds merge rights on a Google org repo. **Whether `somew1nd` is a Google employee is undecidable from the tree** — a personal address in `git config` proves nothing about employment.

**What *is* established:** one person wrote ~90% of it in 29 days, and **the `google/` namespace tells you nothing on its own** — you have to go and count. *(The vault's **v262 D49** — a namespace is not a claim about authorship — at an instance where the namespace is as strong as namespaces get.)*

**(a) axis: FAIL.** Google is corporate-not-Anthropic (§41; the v169 NVIDIA precedent). An `ANTHROPIC_API_KEY` slot in `.env.example` is **compatibility, not affiliation** — the v284 precedent.

---

## 2. ⭐⭐⭐⭐⭐ THE RULE

> **This repository is rigorous about everything it can COMPUTE and silent or wrong about everything it can only ASSERT — and because the assertions are unusually well written, they read as guarantees.**

Nothing here is sloppy. The computed parts are genuinely excellent, several of them better than anything in the surrounding corpus. The asserted parts are false, and they are false in the specific way that well-written prose is false: nobody re-reads a sentence that already sounds right.

**Computed → holds:**

| Mechanism | Evidence |
|---|---|
| `check_dependency_sources.py` walks `uv.lock` + `package-lock.json`, fails CI | 68 lines, stdlib-only, runs **before** `uv sync` |
| `quality_ratchet.py` AST-walks for broad/silent handlers | baseline **754 / 0 / 18 — exact at HEAD, zero headroom** |
| Lockfile integrity | **2,788 `sha256` hashes**, 1:1 with artifacts |
| Pre-execution safety net | XML-hierarchy validation **+ a VLM pixel comparison of the target crop** |
| `secrets.compare_digest` in the real OTP path | `otp_service.py:75` |
| Network egress | only user-configured LLM/OCR endpoints; **zero telemetry, zero analytics, zero phone-home** |
| MCP bind | `stdio` default; SSE binds **127.0.0.1**, never `0.0.0.0` |

**Asserted → false:**

| Assertion | Reality |
|---|---|
| `CONTRIBUTING.md:24` *"the same suite used by pull-request CI"* | Python tests **never run on PR** |
| `JWT_SECRET_KEY = "…-change-in-prod"` | still the default; published in git |
| `DEV_MOCK_OTP = "123456"  # dev/test environments` | **not environment-gated** |
| `APP_ENV` | **never appears in a single conditional** |
| `README.md:11` *"secure tenant separation"* | signing key is public |
| `locked_app_package` | locks nothing after launch |
| *"99%+ SOTA on AndroidWorld"* | one PNG; **no harness** |

---

## 3. ⭐⭐⭐⭐⭐ The benchmark: the claim and its evidence were never in the repository at the same time

The README states it four times — a shields.io badge (`README.md:24`), a Key Highlight (`:41`), a section heading (`:275`) and the body (`:277`):

> *"Artemis achieved a **99%+ completion rate** on AndroidWorld, Google Research's benchmark spanning 20+ apps and 100+ multi-step tasks."*

**Verified by hand:**

- **2026-08-13, `206a9ce9` (initial release):** ships `artemis/interfaces/cli/commands/bench.py` — **157 lines**, a real AndroidWorld integration (`from android_world import registry`, `env_launcher.load_and_setup_env()`, and the benchmark's own ground-truth `task_instance.is_successful(env)`), registered as `artemis bench`. Its README makes **zero** benchmark claims (`grep -ci "androidworld|99%|sota"` → **0**).
- **2026-08-18, `9a5aaf9`:** **one commit** — `M README.md`, `D artemis/interfaces/cli/commands/bench.py`, `A docs/assets/androidworld_benchmark_comparison.png`. The harness is deleted, the claim and its chart arrive. The commit message — *"feat: introduce MCP server, cross-platform runtime, and Showcase UI reorganization"* — mentions **neither**.

> **The repository held a working benchmark harness and no claim. It now holds a claim and no harness. The exchange happened in a single commit.**

Three further facts, each verified:

1. **`android_world` is not a dependency** — absent from all **196** locked packages, and from `pyproject.toml` runtime and dev extras.
2. **Even the deleted harness never computed a percentage.** It logged a per-task boolean (`logger.info(f"… Benchmark Verified: {success}")`) with no counter, no accumulator, no summary, no file write. **No code that has ever been in this repository could produce "99.1%."**
3. The harness loaded AndroidWorld from an **unpinned sibling directory** (`workspace_root / "android_world-main"`) on the author's disk. The task definitions that decide what counts as success were never versioned.

At HEAD, `docs/` contains **no prose whatsoever** — 21 files, all assets. The entire documentation surface is the two READMEs.

### ⭐⭐⭐ And the evidence image was stripped of its provenance

The sole evidence is `docs/assets/androidworld_leaderboard.png`. On **2026-08-25**, across three commits in **four minutes**, it was revised. I extracted both versions and looked at them.

**`9a5aaf9` (original)** carried:
- *"Data as of August 2026"*
- footer: *"Benchmark: Google Research AndroidWorld (116 Tasks · Pass@1)"* | *"Official Community Leaderboard (Cutoff: August 2026)"*
- a **model subtitle on all twelve entries** — *"Gemini 3 Pro + Claude Sonnet 4.5"* (AutoDevice), *"GPT-5 + Gemini 2.5 Pro · Hybrid A11y"* (DroidRun), *"Claude Code + Sonnet 4.5 (MCP Agent)"* (gbox.ai), *"UI-TARS 72B End-to-End GUI Model"*, *"AndroidWorld Human Benchmark Study"* (Human Performance) …

**`4bf1160` — *"docs: refresh AndroidWorld benchmark visual"*** removed **every one of those**: the date, the source line, the benchmark attribution, and all twelve model labels. It kept the ranks, the names, the percentages, and the `OURS` badge.

> **Every element that would let a reader check the chart was removed. Every element that makes it look impressive was kept.**

⚠️ **Stated fairly:** the new image is lighter and matches an architecture diagram added in the same commit, and the message says *"streamline."* **Decluttering is a plausible motive, and I cannot establish intent.** The *effect* is certain and does not depend on intent: the only evidence for a headline claim lost its date and its source.

⭐ **The sharpest detail cuts before the edit.** In the *original, fully-sourced* chart, every competitor's model stack is named — and **ARTEMIS's own row says only *"Closed-Loop Multi-Agent · Self-Healing."*** The one row that needed to disclose a model never did. The chart also claims **99.1% against a stated Human Performance of 80.0%** — an agent 19 points better than people.

🔴 **Never cite the 99%+ figure, in any form, from this repository.**

---

## 4. ⭐⭐⭐⭐ CI: the counters always run; the tests never do

`.github/workflows/ci.yml` triggers on `push`, `pull_request`, `workflow_dispatch`. Three jobs.

**`python-quality`** runs, unconditionally, on every push and PR:
`check_dependency_sources.py` → `uv sync --locked` → `ruff format --check` → `ruff check` → `quality_ratchet.py` → `pyright --project pyright-core.json`.

Then:

```yaml
- name: Run deterministic Python tests
  if: github.event_name == 'workflow_dispatch'
  run: uv run pytest tests/unit tests/tools packages/artemis-client/tests -q
       --cov=… --cov-fail-under=60
```

That is **the only `if:` in the entire file** — and the commit that added it, `5821010`, has a diff of **1 file, 1 insertion: that line alone.** The `frontend` and `package` jobs predate it unchanged. **The gating was surgical and deliberate.**

**2,032 test functions and a 60% coverage floor, behind a manual button.** A change that lints clean, passes the ratchet and type-checks can break every test and merge green.

⚠️ **Two honest qualifiers, both of which I initially got wrong.**

**First, more executes than "the counters" implies.** `frontend` runs `npm test` unconditionally — a real surface: **12 spec files, 42 `describe(`, 128 `it(`**. `package` unconditionally builds two wheels and an sdist, installs into a clean venv, then imports `artemis`, runs four asserts and executes `artemis --version` / `--help`. And CI unconditionally runs two of the repo's own Python scripts (`check_dependency_sources.py` at `:41`, `quality_ratchet.py` at `:59`). **Python does execute in CI — just never a test.**

**Second, the gated step is not "the Python test suite."** It names exactly pyproject's three `testpaths`, and its own name says *"Run **deterministic** Python tests."* The precise distribution:

| Tree | Test functions | Runs in CI? |
|---|---|---|
| `tests/unit` + `tests/tools` + `packages/artemis-client/tests` | **2,032** | only on `workflow_dispatch` |
| `tests/integration` | **24** | **never — absent from CI under every event** |
| `tests/e2e` | **7** | **never — absent under every event** |

✅ **Fair to the project:** integration and e2e need devices and credentials, and `CONTRIBUTING.md` documents them as `make test-device` / `make test-integration`. Their absence from GitHub runners is the **documented design**. It is the *deterministic* suite — the one with no such excuse, the one the docs call required — that was switched off.

> **The Angular frontend is test-gated on every PR. The Python core is not.**

### ⭐⭐⭐⭐⭐ The 80 minutes

| Time (2026-09-02) | Commit | Event |
|---|---|---|
| 21:43:57 | `67248c8` | **Creates `.github/workflows/ci.yml`** (175 insertions; `.github` did not exist before) **and** adds to `CONTRIBUTING.md`: *"This is the same suite used by pull-request CI."* |
| 23:04:19 | `5821010` | *"ci: run Python tests only on manual dispatch"* — adds the `if:`. Diff: **1 file, 1 insertion.** |

**1 h 20 m 22 s.**

**And the sentence was not loosely true — it was exactly true.** At `67248c8` the workflow carried a bare `pull_request:` trigger and the test step had **no `if:` at all**; `make test` is bare `uv run pytest`, whose `testpaths` are `tests/unit`, `tests/tools`, `packages/artemis-client/tests` — **the identical three paths CI passed explicitly**, under the same hermetic `-m` filter from `addopts`. Same collected set. The claim was precise.

> ⭐ **One commit created the CI and the sentence describing it. Eighty minutes later the same author gated the tests off in a one-line diff. The sentence never described a CI that existed for longer than eighty minutes — and it has stood wrong for the eleven days since.**

*(A new shape for the corpus. **v284**'s number was false the day it was typed; **v274**'s claim never had a gate or a habit; **v270**'s promise was about the future. **Here the claim was exactly true, and its own author falsified it eighty minutes later without looking one directory over.**)*

### Pre-commit agrees

`.pre-commit-config.yaml` runs `ruff check`, `ruff format --check`, `quality_ratchet.py`. **No pytest. No pyright.** Both automation layers run the counters and neither runs the tests.

---

## 5. ⭐⭐⭐⭐⭐ The dependency leak — three times, and every one rode in on a commit about something else

⚠️ **This section was materially corrected by adversarial checking. My first pass found two leaks and misquoted a diffstat; there were three.**

The published lockfiles pointed at a **Google-internal host over plaintext HTTP**:

```
http://airlock-proxy.uplink.goog:999/python/artifact-foundry-prod/ah-3p-staging-python/simple/
```

| Commit | Time | Leak | Commit title |
|---|---|---|---|
| `9a5aaf9` | 2026-08-18 13:56 | **2,955** lines in `uv.lock` | *"feat: introduce MCP server, cross-platform runtime…"* |
| `7b00560` | 2026-08-18 22:13 | → 0 | ***"delet uv.lock"*** — **deletes the file** |
| `d23a4f6` | 2026-09-03 14:38 | **1** entry in `package-lock.json` (of 625) | *"feat: handle mid-stream LLM resets and deduplicate UI action stream events"* |
| `3047c9c` | 2026-09-10 17:54 | **2,982** lines in `uv.lock` | *"Fix Python code format check issues"* |
| `b86c371` | 2026-09-10 18:15 | 2,982 | merged via **PR #24** |
| `0860788` | 2026-09-11 01:48 | → 0 | *"fix: use public dependency sources in lockfiles"* + **the gate** |

> ⭐⭐⭐⭐⭐ **All three leaks arrived inside commits about something else. Not one carries the word "dependency" or "lockfile" in its title.** The first fix removed the *instance* — by deleting the file. The class returned twice, the second time **through a reviewed pull request**, and only then was a gate written.

⭐ **The npm leak is the instructive one: a single poisoned entry among 625.** Nobody spots one line in a lockfile, and nobody reads a 6,000-line diff — which is precisely why review did not catch either.

✅ **Severity, stated fairly:** all **2,788 artifacts carried `sha256` hashes** throughout, and `uv` verifies them. This was **availability and internal-infrastructure disclosure**, *not* an integrity compromise. Outside Google's network, installation simply failed.

### The gate is very good — and its npm half runs in the one job that never uses npm

`check_dependency_sources.py` is 68 stdlib-only lines, deliberately import-free so it can run **before installation**: it asserts every locked package resolves to `https://pypi.org/simple` with artifacts on `files.pythonhosted.org`, and every npm `resolved` on `registry.npmjs.org` — **checking the scheme too**, which is what catches plaintext HTTP. It is the defence **v271** lacked.

⚠️ **But four precision corrections, all of which I had wrong or overstated:**

1. **`uv.lock` alone changed 3,025 / 3,025** — my "3,097 / 3,026" was the **whole-commit** total across three files. *(A diffstat quoted as if it described one file: clause (g), on me.)* Even 3,025 overstates; a positional comparison shows **2,982 of 4,908 lines actually differ**, the rest being diff re-anchoring noise.
2. **It is the *third* step, not the first** — after checkout and Python setup. The accurate phrase is *"the first step before installation"*, which is literally the step's own name.
3. **Not "every" package.** 194 of 196 for Python (two workspace editables are allowlisted — legitimate); for npm, line 57 is `if "resolved" in package:`, so a `file:`/`link:`/bundled dependency **is skipped silently**.
4. ⭐⭐⭐⭐⭐ **And the scope error is the finding.** `check_dependency_sources.py` is invoked at **exactly one place tree-wide** — `ci.yml:41`, inside `python-quality`, **the only job that never installs npm packages.** The two jobs that *do* run `npm ci` — `frontend` (`:99`) and `package` (`:136`) — never invoke it, and there is **no `needs:` anywhere in the file**, so all three jobs run in parallel and both npm installs proceed regardless of the gate's verdict.

> **The npm half of the dependency-source gate runs only in the job where npm is never used.** *(v271's rule — a gate's scope is inherited from where it lives — reproduced inside the best artifact in the repository.)*

---

## 6. 🔴 The playground: a real auth service outside every gate

`playground/backend_manager/` is **18 Python files** of FastAPI. Its own README:

> *"The central orchestration, API gateway, **authentication**, and container lifecycle service … Issues signed JWT access tokens for **secure tenant separation**."*

It is **not** in `quality_ratchet.py` SOURCE_ROOTS. **Not** in `pyright-core.json`. **Not** in pytest `testpaths`. **Zero of the three gates reach the only component that handles authentication.**

**`config.py`:**
```python
JWT_SECRET_KEY: str = "artemis-cos-production-super-secret-key-change-in-prod"
DEV_MOCK_OTP: str = "123456"   # Bypass code for dev/test environments
APP_ENV: str = "development"
HOST: str = "0.0.0.0"
DEBUG: bool = True
```

**`otp_service.py:59`:**
```python
if settings.DEV_MOCK_OTP and code == settings.DEV_MOCK_OTP:
    return True          # ← before any record lookup
```

Truthiness only. **`APP_ENV` is never consulted.** I searched every conditional across `playground/`, `apps/`, `artemis/` and `mcp_server/`:

> ⭐⭐⭐⭐⭐ **`APP_ENV` is declared in config, set to `production` in both deployment files, printed by the health endpoint and logged at startup — and never once used in a conditional. It is a variable that describes the environment to humans and to nothing else.**

And both deployment paths — `docker-compose.yml:30` and `deploy_to_cos.sh:107` — set `APP_ENV=production` while setting **neither `JWT_SECRET_KEY` nor `DEV_MOCK_OTP`**. Following the repository's own production instructions yields a service where `123456` authenticates as any identifier and the JWT signing key is in public git. `docker-compose.yml` also mounts **`/var/run/docker.sock`** into that container, and **neither Dockerfile carries a `USER` directive** (both run as root).

⚠️ **Fair framing:** it is called `playground` and is a hosted demo/sandbox. But it is architected and documented as a real multi-tenant service, it has a production deploy script, and the phrase *"secure tenant separation"* is a **security property asserted in the README of the component that does not have it**.

⭐ The most telling detail: `otp_service.py:75` uses **`secrets.compare_digest`** — textbook constant-time comparison — for the real code path, sixteen lines below a bypass compared with `==`. **The cryptography is computed and correct; the control flow is described and wrong.**

---

## 7. 🔴 `locked_app_package` locks nothing

`mobile_run_task` accepts `locked_app_package`. It reads like a fence: confine the agent to one app.

`get_current_foreground_package_async` has **exactly three call sites, all inside `artemis/utils/app_launch_utils.py`** — the launch path. The comparison `current_package == app_package` happens at lines 202 and 236, during launch-and-wait. A behaviour grep across `artemis/graph/` and `artemis/agents/validator/` — the entire execution path — returns **nothing**.

`task_request_builder.py:103` says it plainly: *"ensures the specified app is launched and in the foreground **before**."* A **precondition**, not an invariant.

⭐⭐⭐⭐⭐ **And it is worse than "not enforced."** `git grep -n "get_locked_app_package"` over the **entire repository, tests included**, returns **exactly one line — the `def` itself, at `artemis/context.py:168`.** The accessor that would let anything read the lock during execution has **never been called.**

> **The app lock is stored in a field, exposed by a getter, and that getter has zero call sites. The fence exists as a data structure and never as a behaviour.** *(A direct echo of **v283**, where the function producing the untrusted-content tags was called zero times at every commit in history.)*

> ⭐⭐⭐⭐⭐ And `data_engine/engine.py:901-909` **stamps `foreground_app` onto every recorded step** — for the search/recall surface. **The foreground package is measured on every single step, written to the database, and never once compared against the lock that exists to constrain it.** The data is right there. Nothing reads it for that purpose.

🔴 **You cannot use `locked_app_package` to fence an agent away from your banking app.**

---

## 8. The agent, calibrated

**Genuinely substantial.** The perception stack is real: screenshots plus UI hierarchy (Accessibility Helper with a UIAutomator2 fallback, selectable via `ARTEMIS_HIERARCHY_BACKEND`), element-index targeting with coordinate and visual fallbacks. The **pre-execution safety net** (`artemis/agents/validator/`) validates an action's preconditions against the live screen two ways: XML-hierarchy validation with a short retry loop, and a **VLM comparison of the target crop** before the tap lands. A second model checks the crop. That is more care than most of this corpus shows.

⚠️ Two honest limits: **burst mode** (`execution_loop.py:24`) executes chained actions *"back to back with no safety net, no retries and no screenshots in between"*, and **Flash has no safety net at all** — which the MCP docstring discloses.

⭐⭐ **The "graph orchestration" claim is honest** — `artemis/graph/graph.py` has **8 nodes, 6 static edges and 3 conditional edges**: a real LangGraph state machine. *(Worth saying plainly, because **v284** claimed "multi-agent orchestration (LangGraph)" for 2 nodes and one conditional edge. Artemis delivers what that one inflated.)*

### ⭐⭐⭐ The MCP surface is a *task* interface, not an *action* interface

The IDE-facing server exposes exactly **5 tools**, enumerated: `mobile_run_task`, `mobile_manage_task`, `mobile_get_device_state`, `mobile_inspect_trace`, `mobile_diagnose`.

⭐ **But there are four `FastMCP` instances in the tree** — `mcp_server/base.py:33` (the external one), `artemis/mcp/adb_server.py:88` (**13 tools**: tap, swipe, press_key, launch_app, stop_app, open_link, take_screenshot, get_ui_hierarchy, focus_and_input_text, focus_and_clear_text, erase_one_char, long_press_on, back), `artemis/mcp/xml_search_server.py:41` (2, read-only), and `action_server.py:77` (12 `ActionSpec` wire dialects). **Artemis uses MCP internally as its own action/perception bus**, not merely as an external interface — a notable #18 observation.

The calling IDE agent does not tap. It hands over a goal and an autonomous on-device subagent runs it. That cuts both ways: the IDE agent cannot issue arbitrary coordinates — **and there is therefore no approval surface at all**. "Book a flight" becomes two hundred taps with no further checkpoint.

⚠️ **No MCP tool annotations** (`readOnlyHint` / `destructiveHint`) are declared. `mobile_run_task`, which drives a real phone, and `mobile_get_device_state`, which reads, are **indistinguishable to the protocol**. *(Contrast **v278**, which annotated all 80 of its tools.)*

⭐ **But the `mobile_run_task` docstring is one of the better tool descriptions in the corpus.** It discloses Flash's missing safety net *in the text the agent reads*; it gives honest latency (*"the agent's own inference adds ~5 s per step (Flash) or ~30 s per turn (Pro)"*); and it ends by telling the caller to stop using it: *"For recurring workflows, run once to discover the path, then author a deterministic script instead."* **That is v271's *name where to go INSTEAD*, at N=2.**

### ⭐⭐⭐⭐ The operator prompt is a masterpiece about truth and silent about harm

`artemis/agents/operator/operator.json` — **25,027 bytes, one key, `main_template`**. Its rules are obsessive about the agent not deceiving itself:

- *"Never write an action's expected outcome as if it had already been observed."*
- *"…so never declare a check passed or record a conclusion on its behalf."*
- *"Take no extra actions for `assert:` lines and **never construct state to satisfy one**."*
- *"Nothing is inferred on your behalf: it is recorded as your own statement."*
- *"…never a generic 'element' or 'button'."*

That is a superb epistemic discipline, and the anti-gaming clause is better than most eval harnesses manage.

**Word counts in those 25 KB:** `password` **0** · `credential` **0** · `purchase` **0** · `payment` **0** · `privacy` **0** · `personal` **0** · `irreversible` **0** · `destructive` **0** · `refuse` **0**.

I read all eleven `never`, five `do not` and three `confirm` in context. **Every one is about task-execution discipline. Not one concerns the user, their money, their messages or their data.**

> **It is a magnificent document about truthfulness that contains nothing at all about harm** — on an agent that taps a phone logged into Gmail, Messages, Photos, Maps, Play Store and whatever banking app is installed.

### 🔴🔴🔴 The trust hierarchy is described in detail, computed nowhere — and the description is the exploit

There is **no untrusted-content boundary anywhere**: no data-not-instructions framing, no marking of screen-derived text. ⚠️ Established by **behaviour** search, not by name — the word "injection" appears 20+ times in this codebase and means **dependency injection** every single time.

What the prompt *does* say, verbatim, runs in the **opposite** direction:

> *"**Vision-First Priority**: The screenshot is **the primary source of truth** for the real device state."*
>
> *"Treat recorded notes as **verified ground truth**."*
>
> *"**User Guidance**: A `--- User Guidance ---` block **in your observation** is an instruction from the user watching the run, relayed by the system as an external interruption like the stop signal. **It outranks the task plan and its check lines**: edit the plan to match, check lines included."*

OCR text and accessibility-node text are interpolated into that same observation **with no escaping of the `---` delimiters** (`prompt_assembly.py` / `prompts.py` contain no escaping or sanitisation of any kind). A second privileged delimiter, `--- Execution Incident (OPEN) ---`, is documented the same way.

> 🔴 **Any app that renders the literal string `--- User Guidance ---` followed by text gets that text treated as a user instruction outranking the agent's plan. The system prompt is a published specification for how to hijack the agent.**

### ⭐⭐⭐⭐⭐ And the absence is TEST-ENFORCED

`tests/unit/agents/test_operator_prompts.py:55-59`:

```python
def test_operator_prompt_omits_environment_trust_and_explorer_directives():
    for template in load_operator_prompts().values():
        prompt = apply_operator_prompt_contract(template)
        assert "Untrusted Screen Content & Instruction Priority" not in prompt
        assert "Visual Explorer Rule" not in prompt
```

`git grep "Untrusted Screen Content"` over the whole tree returns **exactly that one line**. The only appearance of the phrase in this repository is **an assertion that it is not in the prompt**, and the word *trust* is in the **test's own name**.

⚠️ **The fair reading:** the block almost certainly existed in an internal pre-open-source build and this is a do-not-reintroduce guard — likely removed for prompt length or measured behaviour, not malice. **Either way a regression test now actively prevents the prompt-injection boundary from coming back.**

⭐⭐⭐ **And the two findings compose into the ship's bleakest joke:** that test **does not run on push or pull request** (§4). *A test that forbids adding a safety boundary, which never executes.* It prevents nothing and records the intent permanently.

> ⭐ **Method rule earned here — a refinement of v284's:** *a zero-hit identifier search is evidence about the identifier, never about the mechanism* — **and a high-hit search is exactly as uninformative.** Twenty hits on "injection", not one of them the mechanism; one hit on "Untrusted Screen Content", and it was the negation.

> ⭐ **Method rule earned here — a refinement of v284's:** *a zero-hit identifier search is evidence about the identifier, never about the mechanism* — **and a high-hit search is exactly as uninformative.** Twenty hits on "injection" and not one of them the mechanism.

### 🔴🔴 And the boundary's absence has a reachable consequence

`artemis/controllers/unified_controller.py:224`:

```python
async def open_url(self, url: str) -> bool:
    await self._driver.execute_shell(f"am start -a android.intent.action.VIEW -d '{url}'")
```

A caller-supplied string is interpolated into a shell command inside single quotes **with no escaping**. It is **agent-reachable**: `action_specs.py:655` registers `open_link` as one of the twelve device `ActionSpec`s the LLM operator can emit → `_wire_open_link` (`:232`) → `adb_server.open_link` (`:324`) → `controller.open_url` → that line. A URL containing a single quote terminates the quoted argument.

> 🔴 **The complete chain: text on the screen of an arbitrary app → the model, with no trust boundary → an emitted `open_link` action → arbitrary `adb shell` execution on the device.**

⭐ **And the rule accounts for even this.** `shlex.quote` **is** used in this codebase — twice, at `command_tool.py:604` and `:606`, for a `cd` and an `export`. The escaping is present exactly where a developer was visibly reasoning about shell construction, and absent where the parameter was called `url` — because a URL does not look like a command.

---

## 9. What is genuinely excellent

Set against the above, and not cancelled by it:

- ⭐⭐⭐ **`check_dependency_sources.py`** — the best incident→invariant conversion in recent ships, and the exact gate v271 lacked.
- ⭐⭐⭐ **Privacy posture.** A tool that continuously screenshots your phone and ships **zero telemetry, zero analytics, no phone-home**. Only the LLM/OCR endpoints you configure. `artemis/telemetry/` is a **local** trace store.
- ⭐⭐ **`quality_ratchet.py`** — AST-based, not regex, and its `silent_broad_exception_handlers` metric is the vault's own **v246** `grep -rni "silent"` detector implemented as a hard CI gate, held at **0** with zero headroom.
- ⭐⭐ **No `0.0.0.0` anywhere** in `artemis/`, `mcp_server/` or `apps/`; MCP defaults to stdio, SSE to `127.0.0.1`.
- ⭐⭐ **`start.sh`'s `request_sudo()`** — consent-gated privilege escalation that **prompts interactively and falls back to user-space on refusal** (*"Skipped sudo. Using user-space fallback"*).
- ⭐ **`.env.example` thinks about personal phones** — `ARTEMIS_KEEP_DEVICE_AWAKE` and `ARTEMIS_HELPER_AUTO_INSTALL` each carry written rationale about shared or personal devices. ⚠️ Both default to the more invasive value, with safety as opt-out (**v265**: the discipline stops where the safe choice would cost something).
- ⭐ **The CI smoke test** asserts the wheel's bundled resources exist and that `node_modules` did not leak into the package.
- ⭐⭐ **The one README count that diverges from the tree diverges by being too MODEST.** The README advertises MCP setup for three IDEs (Antigravity, Claude Code, Windsurf); `artemis/interfaces/cli/commands/mcp.py:464-478` enumerates **nine** install targets — `antigravity, cursor, claude, windsurf, vscode, cline, roo, openclaw, codex`. In a repository whose headline claim is unbacked, the only under-claim is the one nobody would have checked.
- ⭐ **`CONTRIBUTING.md`'s four-layer test taxonomy** is a genuinely good piece of thinking — `test` / `test-integration` / `test-device` / `test-all`, with markers `android`/`cloud`/`manual`/`e2e` and the rule that tests "must remain safely collectable" without their dependency. ⚠️ Only `integration` and `e2e` are enforced (by directory path in `tests/conftest.py`); `android`, `cloud` and `manual` are pure convention.

### Scope, measured

| Gate | Coverage |
|---|---|
| `quality_ratchet.py` | **319 of 590** `.py` files (54%) |
| `pyright-core.json` | **~14 of 590** (2.4%) — CI names this honestly (*"protected core modules"*); `make typecheck`'s help text (*"Run type checking"*) does not |
| Copyright header | 553/590, **no gate at all** — the 37 without it are 26 tests, 5 playground `__init__.py`, 4 scripts and one example, ⭐ including **`scripts/quality_ratchet.py` itself** |

⚠️ **A fleet claim I could not replicate and am not shipping.** An agent reported **7 silent broad handlers** in the 271 files outside SOURCE_ROOTS. My matcher — validated against the AST ground truth, returning exactly **0** on the in-scope control the ratchet says is 0 — finds **1**, at `scripts/run_ui.py:113`, and it is a **benign optional-import guard**. Outside-scope broad handlers: **37** (my line-based instrument undercounts multi-line clauses by ~4, so treat as a floor). **The scope gap is real; the "silent" scandal is not.** Reported here because fairness shrank the finding.

---

## 9b. ⭐⭐⭐⭐⭐ The attribution: two upstream projects, one NOTICE, one revert — and only one survives

⚠️ **Two of my own claims were wrong here and are corrected below.** I first praised this as *"the best attribution discipline in recent ships"*; an adversarial check refuted the tense. I then reported *"zero hits for the removed upstream authors"* — that was a grep of **HEAD**. Searching **all 119 commits** finds them, and what it finds is the sharpest thing in this repository.

### The allegation, stated as an allegation

**Minitap, Inc. publicly alleges that ARTEMIS is derived from their Apache-2.0 project `minitap-ai/mobile-use` with authorship removed.** That is a claim made by a party to a dispute. What follows separates **what I verified mechanically from two clones** from **what is web-sourced**, and I have deliberately verified the exculpatory half as carefully as the incriminating half.

### Verified from the tree — the derivation itself is not in question

| Fact | How |
|---|---|
| Root commit `206a9ce` (2026-08-13) declares **`version = "3.6.3"`** — mobile-use's own release tag — in a commit titled *"initial release"* | `git show 206a9ce9:pyproject.toml` |
| `artemis/agents/hopper/hopper.md` at the root commit is **byte-identical** to mobile-use v3.6.3's copy (sha256 `7335d897…`) | `cmp` / `shasum -a 256` |
| The root tree contains **0 references** to Minitap, mobile-use or mobile_use — anywhere | `git grep -Ini … 206a9ce9` → 0 |
| mobile-use's `LICENSE` fills the Apache appendix with **`Copyright 2025 Minitap, Inc`**. Artemis's `LICENSE` **restores the stock boilerplate and writes `Copyright 2026 Google LLC.`** | `diff` of the two LICENSE files |
| mobile-use ships a **`NOTICE`** carrying an explicit **`ATTRIBUTION REQUEST`** — *"we kindly request that derivative works … include a prominent attribution to 'Minitap, Inc.'… This is a request, not a legal requirement."* | read from the clone |

⚠️ **This closes the gap I flagged in the previous draft** (*"whether mobile-use ships a NOTICE, which I did not fetch"*). It does. **I am not offering a legal conclusion** — whether Apache-2.0 §4(c)/§4(d) is satisfied is a question for lawyers. The facts above are mechanical; the verdict is not mine to render.

### ⭐⭐⭐⭐⭐ The NOTICE lived for 3 hours 12 minutes, in 1 of 119 commits

The full lifecycle, enumerated commit-by-commit (clause (g) — never `grep -c`):

| 2026-09-11 (PDT) | Commit | Who | Event |
|---|---|---|---|
| 16:19:42 | `54fcef9` | somew1nd | *"clean up legacy code, **rename hopper to entity_extractor**, and **add third-party notices**"* — **`NOTICE` created** |
| 19:32:22 | `1d82d59` | **yaoyao-open-source** *(a different person)* | **`Revert "…"`** → **`D  NOTICE`** |
| 19:37:23 | `1d9eb44` | somew1nd | Merge PR #60 |
| *19:39:39* | — | — | *(web-sourced: the Hacker News story is created here — **7 minutes after the revert**)* |
| 19:59:21 | **`371aa6d` = HEAD** | somew1nd | *"fix: complete README and relevant file headers **per Apache 2.0 requirements**"* — **21 per-file headers** |

**That deleted `NOTICE` credited two upstream projects and eight named individuals:**

- **mobile-use** — Minitap, Inc. + *Pierre-Louis Favreau, Jean-Pierre Lo, Nicolas Dehandschoewercker, Clément Guiguet, Karun Agarwal*
- **finalrun-agent** — FinalRun Inc. + *Ashish Yadav, Arnold Laishram, Srinidhi G S*

**And here is the controlled experiment.** One NOTICE, one revert, two upstreams — then per-file headers were added for **one** of them. At HEAD:

| At HEAD | Hits | Files |
|---|---|---|
| Minitap / mobile-use | **44** | **23** (20 `.py` + `hopper.md` + both READMEs) |
| **finalrun-agent / FinalRun Inc.** | **0** | **0** |
| The **eight named individuals** | **0** | **0** |

> ⭐⭐⭐⭐⭐ **Attribution written INSIDE the files it describes survived a revert aimed at something else. Attribution written in one central file died with that file — and took a second company and eight people with it.**

**Nobody decided to delete finalrun-agent's credit.** The notices were bundled into a commit that *also* performed a breaking rename, a different maintainer reverted the whole commit — almost certainly for the rename — and the compliance fix was collateral. **The commit boundary decided what attribution survived.** ⇒ **v283's rule at an independent instance** (*a false or fragile statement is one written about something, in a different file from the thing it describes*) — and **v284's rule too**: a `NOTICE` is a hand-typed list of upstreams with no gate, so nothing went red when it vanished.

⚠️ **Effect certain, intent not.** The revert **precedes** the HN story by seven minutes, so *"HN forced the fix"* is **not supported**; the final commit lands twenty minutes after it. I state the ordering and decline to assert motive — the same discipline this ship applied to the stripped leaderboard image.

### ⚖️ For fairness: the viral "228 of 229 files" figure does NOT survive

The widely-republished claim is that **228 of 229 files were exactly the same**. **229 is the artemis root tree's file count** — and I measured the rest myself, from both clones:

| Measurement (artemis root tree vs mobile-use v3.6.3) | Result |
|---|---|
| Files in the artemis root tree | **229** |
| Files in mobile-use v3.6.3 | **169** |
| Shared paths after normalising the `minitap/mobile_use/` → `artemis/` rename | **74** |
| **Byte-identical** | **2** (`hopper.md`, `pyrightconfig.json`) |
| Identical after stripping the rename + comment headers (≤20% line delta) | **13** |
| **Substantially different** | **59** |

**At most 74 of the 229 files could even be compared, and 2 are byte-identical.** The figure is not supported by the trees. ⭐ **This matters for the vault's own discipline, not for Google's benefit:** the number is the kind of claim that travels because it is vivid, and it is exactly the sort I would be embarrassed to repeat unchecked. *(A fleet agent reports it does not appear in Minitap's own blog post either — **web-sourced, not verified by me**.)*

### What the remedy does and does not cover

✅ 21 files plus `README.md:318` and `README_CN.md:316` now credit **Minitap, Inc.** by name and link.
🔴 **No `NOTICE` at HEAD.** 🔴 **finalrun-agent is credited nowhere.** 🔴 **Not one of the eight individuals is named anywhere in the tree.** `pyproject.toml` lists a single author, `Farley Wang <farleyw@google.com>` — entered at `9a5aaf9`, replacing the root commit's `somew1nd <wfq559@outlook.com>`.

⭐⭐⭐⭐⭐ **And the rule accounts for the whole shape.** The Google copyright is a **stamp** — mechanical, applied to **191 of 192** `.py` files at the root commit, right immediately. The upstream attribution required someone to **know a fact about provenance and assert it** — it took twenty-nine days, a commit message naming its prompt (*"per Apache 2.0 requirements"*), and it still reaches only the upstream that got per-file headers.

> **The claim that could be computed was correct on day one. The claim that required knowledge arrived on day thirty — and reached one of the two upstreams it owed.**

*(Corpus placement, corrected: **not** the positive pole. **v181** cortex-hub bundled GitNexus v33 uncredited; **v267** Obscura never named Lightpanda; **v265** and **v284** credited upstreams with no NOTICE. Artemis is the case that **got there on the last day under an Apache-2.0 prompt, for one upstream of two** — better than v181 and v267; not better than a project that did it from the start.)*

---

## 10. Mint

### NO MINT. Counts **46 / 12 UNCHANGED**; §C-1 **13**, §C-2 **39** unchanged.

**Collision grep CLEAN** — `grep -rn -i "artemis"` across the whole vault returns **one** hit, a binary false-positive inside an unrelated corpus file's tokenizer model. Corpus-first subject, first `google/`-org author.

**Not an N=2 of §C-2 C35** (v183 serve-sim, *"Agent-First Mobile-Simulator Perception+Control Layer"*) — decided by reading **that row's own written definition**, which mints an explicit **conjunction**:

> *(agent-FIRST design for a native-app **SIMULATOR** surface) × (**human-watchable live framebuffer stream** + accessibility + forwarded logs as the perception surface) × (a full action channel) × (**Agent-Skill packaging**)*

Artemis matches the first and third and fails the rest: **physical Android devices**, not a simulator; **screenshot + UI-hierarchy** perception, not a streamed framebuffer (its web console is an operator view, not the perception channel); **no camera-injection**; and **zero `SKILL.md` / `skills/` / `plugin.json`** — it is MCP + CLI + console. C35's own scope note already names **`mobile-mcp`** among external peers it does *not* claim, and that is precisely Artemis's class.

> ⭐⭐⭐ **§C-2 earns its keep for the fourth time** (v262 C37 · v263 C38 · v284 C40 · now v285 C35). Reading the row's written definition prevented a false N=2.

**Also not world-first** — `mobile-mcp`, `droidrun`, Mobile-Agent, AppAgent and AutoDroid precede; the project's own leaderboard image lists DroidRun, gbox.ai, Mobile-Agent-v3, MobileUse and UI-TARS as competitors. Corpus-first-for-a-surface ≠ mintable (**v211**).

**⭐ RECORDED, NOT EXECUTED — for the badly overdue audit:**
A §C-2 N=1 candidate, *"Agent-First **Physical**-Mobile-Device Perception+Control Layer whose MCP surface delegates a WHOLE TASK to an autonomous on-device subagent rather than exposing primitive actions."* The distinctive is the **task-not-action MCP interface** (contrast `mobile-mcp`, which exposes tap/swipe as tools), and the corpus holds iOS-simulator (C35), browser (C34/C48/C57) and debugger (C58) rows but **no physical-device row**. **Argued against:** not world-first; the seven-row capability-layer precedent that carried **C58** at N=1 leaned on a genuinely novel *delivery mechanism* (an in-process debugger plugin), and "MCP server for a device class" is not that. **I decline it; the audit may disagree.**

**Other rows tested and declined:** not CONFIRMED **#24** (product-first native app retrofitted with a first-party MCP server) — Artemis is agent-first from the root commit, not a product retrofitted; **#18 B1-MCP** is a capability-vs-distribution match only.

---

## 11. Verdict inputs

**GOAL-ALIGNED INCLUDE 3/4** — **(a) FAIL** (Google, corporate-not-Anthropic; §41) · **(b) STRONG** (an agent perception+control capability layer, squarely goal #1) · **(c) STRONG** · **(d) STRONG). Clean GA; no §40, no override.

**Streak:** v284 `GA:141` → **`GA:142 · OG:13 [7 ov]`** — **65 consecutive GA v220→v285**. **§35 CLEAR** ({v283, v284, v285} = 0 OG). **Override review: 25th consecutive discharge.**

**Tier:** T2 product / platform — reviewable.
