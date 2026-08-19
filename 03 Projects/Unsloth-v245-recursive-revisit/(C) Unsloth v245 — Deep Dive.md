# (C) Unsloth — v245 Deep Dive

**Subject:** `unslothai/unsloth` — *"Local UI to run and train LLMs and diffusion models, including Qwen3.8, Kimi K3, MiniMax-H3, Gemma 4, DeepSeek-V4, FLUX and more."*
**Ship:** v245, 2026-08-19. **The 5th CORPUS-RECURSIVE REVISIT in wiki history** (after v78 ↺ v1 ECC · v185 ↺ v18 agency-agents · v228 ↺ v36 pi · v242 ↺ v235 deepseek-harness) — and **the first whose anchor was rated OUTSIDE-SCOPE.**
**Anchor:** v23, 2026-04-20, `03 Projects/Unsloth - Beginner Analysis/` (preserved unmodified).
**Method:** ✅ **SOURCE-CLONED TWICE.** A `--depth 1` tree at HEAD **`cabed07f95676ef6267ce0fd64115b1e9c51e74a`** (2026-08-18 23:18 −0700, Daniel Han) = **3,972 tracked files / 1,752,665 tracked lines**; plus a `--filter=blob:none` history = **7,476 commits on `HEAD`** / 21,442 with `--all`. Every count below declares its ref population (**D27**).
**License:** dual — root `LICENSE` Apache-2.0, root `COPYING` AGPL-3.0. GitHub's own sidebar shows **"Apache-2.0, AGPL-3.0"**.
**Page-stated (§37.4, API mocked — NOT a Pattern #52 claim):** ~**73.7k★ / 6.7k forks / 375 watchers / 911 open issues / 429 open PRs**.

---

## 0. Why this ship exists, and what it costs the corpus to admit

v23 read this repository on 2026-04-20 and wrote, in the entry that is still the vault's record of it:

> **Scope:** **OUTSIDE-SCOPE training-infrastructure** (2nd entrant after LlamaFactory v22). … **Not agent infrastructure — training-only** — for Storm Bear operator, observational value only (not direct adoption).
> **Storm Bear operator relevance:** **Direct adoption: NONE** … **Wiki is reference asset, not implementation backlog.**

That verdict was **correct when it was written** and is **wrong today**, and nothing about the vault's criteria changed. The subject moved.

**⭐⭐⭐ THE HEADLINE — A SUBJECT CROSSED THE SCOPE BOUNDARY, AND THE CORPUS HAD NO MECHANISM THAT WOULD HAVE NOTICED.**

Between the v23 ship and this one, `unslothai/unsloth` acquired, in this order and all after 2026-04-20:

| date | commit / PR | what landed |
|---|---|---|
| 2026-06-22 | `264f1a04f` (**#6547**) | **Local Agent Guides CI** — installs and drives real coding-agent CLIs against a live Unsloth server |
| 2026-07-03 | `b8400f40d` (**#6613**) | `unsloth connect` renamed **`unsloth start`** |
| 2026-07-22 | `968e6230a` (**#7326**) | **"Unsloth start: add local subagents for Claude Code, Codex, OpenCode and Pi"** |
| 2026-07-24 | `387547980` (**#7329**) | "Complete local subagent delegation for Codex, **Claude plan mode**, and Pi" — authored by **oobabooga** |
| 2026-07-27 | `7a9749eb4` (**#7437**) | "keep the local subagent unattended and out of plan mode" |

*(`git -C hist log --format='%h|%ai|%an|%s' --reverse -- <path>`)*

So the thing the vault called "not agent infrastructure" now ships an MCP server, a plugin for Claude Code, a six-harness connect layer, and a CI job that boots six agent CLIs. **The scope verdict had a shelf life of 63 days and nobody re-checked it.** The four prior revisits were all triggered by something the analyst noticed (a rename, a submodule, a disclosed method gap); this one is the first where the *classification itself* is the thing that expired.

**⇒ D31 (new): a scope verdict is a claim about the world on a date, not a property of the subject.** The corpus tests facts on revisit (D25: an un-cloned subject's caveats are hearsay) and provenance on revisit (D19: measure at the divergence point). It has never re-tested **scope**. An OUTSIDE-SCOPE ruling is the one verdict that closes the file — which makes it the one verdict most likely to rot unobserved. Every prior OUTSIDE-SCOPE subject in the corpus is now un-audited by construction.

Fair to the v23 analyst, and this matters: **v23 got the facts right.** It recorded the dual Apache/AGPL license, it recorded `studio/` existing (studio's first commit is `544d6944d`, 2026-02-02 — 77 days *before* v23), it recorded the Han-brothers authorship, and it named "MLX training (coming)" before it shipped. It read the repository accurately. What it could not do is predict that a fine-tuning library would spend the following quarter becoming an agent host.

---

## 1. What Unsloth is now, measured

The famous part is 4.3% of the repository that bears its name.

| surface | tracked lines | share |
|---|---|---|
| `studio/` (the desktop/web app) | **1,330,957** | **75.9%** |
| `tests/` (top-level suite only) | 220,365 | 12.6% |
| `unsloth/` — **the fine-tuning library** | **76,215** | **4.3%** |
| `unsloth_cli/` (CLI + agent-connect) | 31,888 | 1.8% |
| **total tracked** | **1,752,665** | 100% |

Excluding lockfiles, `studio/backend` alone is 744,962 lines and `studio/frontend` 497,299 — the app is **~16× the library**. The repository's own README now opens, at line 9, with:

> **"Unsloth is the first desktop app to run and train models."**

and its GitHub About text leads with **"Local UI to run and train"** — *run* before *train*. In the Features list, `### Run & Build with AI` (line 75) precedes `### Train & Deploy` (line 86). The v23-era tagline the vault recorded — *"Train 500+ models up to 2× faster with up to 70% less VRAM"* — is gone from the description field.

**The repository is three projects grafted together, and its git metadata says so.** There are **three root commits, all ancestors of `HEAD`**:

| root | date | author | subject | what it became |
|---|---|---|---|---|
| `1e2ba1b1d` | 2023-11-30 | Daniel Han | "Initial commit" | the library |
| `42490cfbc` | **2025-12-10** | **Dan Saunders** | **"train CLI"** | 43 commits: context parallelism, VLM DDP checkpointing, "CLI command for UI" |
| `b5aa137b7` | **2026-01-27** | **Roland Tannous** | **"first commit"** | the studio skeleton → `0ef09af00` "git repo skeleton structure", `52bd5ebeb` "feat: add frontend UI codebase" |

*(`git rev-list --max-parents=0 HEAD`; `git merge-base --is-ancestor <root> HEAD` → YES for all three)*

There is also a **history-recovery event**: `c26aa1a1e` (2026-03-12) *"Restore non-studio files from main after history recovery."* The AGPL licence arrived three days earlier — `ac2906f35` (2026-03-09) *"Add AGPL-3.0 license to studio folder."*

**The v241 D19 lesson applies in a new shape.** D19 said: measure provenance at the divergence point, because a repo's aggregate history can describe a different project than the tree. Here the aggregate history is *honest* about the graft — three roots, all reachable — but the aggregate **age** is misleading in the other direction: "since 2023-11-30" is true of the library and false of 76% of the tree, which is ~6.5 months old. **D19 extended: a single-root check is not enough; count the roots and date each one, because a graft hides a young project inside an old repository's age.**

Activity, `HEAD`, by month — the inflection is unmistakable:

```
2025-12  183     2026-04  202   ← v23 ships 2026-04-20
2026-01  123     2026-05  346
2026-02  807 ←   2026-06  538
2026-03  761 ←   2026-07  539
                 2026-08  936 ← busiest month in repo history, on the 19th
```

The project measures this itself. `.github/scripts/kaggle_t4_ci/BUDGET.md` records, "Measured 2026-08-11 … 7-day window": **479 commits/week to `main`, 567 PRs opened/week.**

**298 distinct author emails** on `HEAD`; Daniel Han **4,204 commits (~56%)**, Michael Han 410, Roland Tannous 372+311, **oobabooga 151** (`oobabooga4@gmail.com`, first commit 2026-05-26, every subject prefixed `Studio:`). 570 merge commits, 6,906 non-merge, **3,267 subjects ending `(#NNNN)`** — a mixed squash+merge strategy, which is what the Claude-trailer arithmetic below has to be read against (**D26**).

---

## 2. ⭐⭐⭐ The Claude Code integration is the best in the corpus, and it contains a finding the vault has been hunting for months

`unsloth start claude` points Claude Code at a locally-served model. The env it builds (`unsloth_cli/commands/start.py:2394-2410`) is worth reading line by line, because almost every line is a decision:

```python
def _claude_local_env(base: str, key: str, entry: dict) -> dict:
    """Build the local endpoint, cache, display, and compaction environment."""
    env = {
        "ANTHROPIC_BASE_URL": base,
        "ANTHROPIC_AUTH_TOKEN": key,
        "ANTHROPIC_MODEL": model_id,
        "CLAUDE_CODE_ATTRIBUTION_HEADER": "0",
        "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
        "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS": "1",
        "CLAUDE_CODE_NO_FLICKER": "1",
    }
    window = entry.get("context_length") or entry.get("max_context_length")
    if window:
        env["CLAUDE_CODE_AUTO_COMPACT_WINDOW"] = str(int(window))
        env["CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"] = "90"
```

and the paired line at `start.py:146`:

```python
_CLAUDE_ENV_UNSET = ("ANTHROPIC_API_KEY", "CLAUDE_CODE_OAUTH_TOKEN")
_CODEX_ENV_UNSET  = ("OPENAI_API_KEY", "CODEX_API_KEY", "CODEX_ACCESS_TOKEN")
```

### 2a. ⭐⭐ It **strips** your real credentials — the exact inverse of the v207/v208/v231/v232 band

Every prior gateway-class subject in this corpus **harvested** a credential: v207 CLIProxyAPI re-exposed CLI-tool OAuth subscriptions as APIs; v208 ported it; v231 and v232 drove logged-in consumer web sessions. Unsloth does the opposite — it **unsets `ANTHROPIC_API_KEY` and `CLAUDE_CODE_OAUTH_TOKEN`** in the child process before launching Claude Code, so a request cannot silently fall through to Anthropic and be billed, and a local endpoint cannot be handed the real key. Same for `OPENAI_API_KEY` / `CODEX_API_KEY` / `CODEX_ACCESS_TOKEN`.

**This is the first subject in the corpus to treat the user's frontier-vendor credential as something to remove from the blast radius rather than something to monetise.** It is a ~2-line practice and it is the single cheapest thing in this repo to copy.

### 2b. ⭐ It refuses to lie to Claude Code's own safety check

`start.py:4359-4362`, in the comment above the launch command:

> `IS_SANDBOX` is left unset on purpose: Claude refuses bypass mode as root unless a sandbox is detected, and **we don't want to falsely claim one on the user's host.**

And in CI, `.github/scripts/agent-guides-drive.sh:~48`, where it *is* true:

> Claude refuses `--dangerously-skip-permissions` outside a sandbox; **the CI runner IS the sandbox, so declare it.**

They set the flag exactly where the claim holds and refuse to set it where it does not. Against the v209 config-override class and the standing v187 "never `--dangerously-skip-permissions`" warning, this is the disciplined pole: a third party that had every incentive to shortcut Claude's guard, documenting why it didn't.

### 2c. ⭐⭐⭐ THE FINDING: a Claude Code default breaks prompt caching on non-Anthropic endpoints, and Unsloth built a CI A/B test that proves it

`.github/scripts/agent-guides-drive.sh:568-613` implements a mode called `attribution-ab`, and it exists to hold a **measured, falsifiable claim about Claude Code** in place:

> **Phase A**: the suppression `start.py` ships (`CLAUDE_CODE_ATTRIBUTION_HEADER=0` + `--exclude-dynamic-system-prompt-sections` + `--settings` overlay) → **expect a HIT** on the continued turn, since the system-prompt prefix is stable.
> **Phase B**: vanilla Claude with the header **ENABLED** → **expect a MISS**. We flip the env var to 1 and strip the suppression flags … **without them the dynamic attribution line is included and changes every turn, so the shared prefix moves and the KV cache is invalidated, ~90% slower.**

Two turns per arm, `--continue` on the second, and the verdict read from the llama-server log sliced by a byte offset captured immediately before the measured turn, so an earlier turn's reuse cannot leak in. It asserts **HIT** in Phase A and **MISS** in Phase B — it does not merely hope for a hit, it *requires the unfixed configuration to fail*, which is what makes it a regression test on the claim rather than on the fix.

The mechanism is **independently confirmed and undocumented by Anthropic.** Claude Code ≥ 2.1.36 sends an `x-anthropic-billing-header` that is injected as a text block at the **front** of the system prompt and changes on every request; a changing prefix is a new cache key. There are open documentation issues for both knobs — [anthropics/claude-code#50085](https://github.com/anthropics/claude-code/issues/50085) *"[DOCS] missing: CLAUDE_CODE_ATTRIBUTION_HEADER - prompt cache with ANTHROPIC_BASE_URL"* and [#45930](https://github.com/anthropics/claude-code/issues/45930) *"[DOCS] CLI docs missing `--exclude-dynamic-system-prompt-sections` for print mode"*. Neither string appears in the current settings documentation (verified 2026-08-19).

**⭐⭐ And it is a three-way independent convergence, one arm of which is already a corpus subject.** The same defect was found and worked around by:

- **Unsloth** (this repo, `start.py:2401` + the CI A/B),
- **`musistudio/claude-code-router`** — PR #1220, *"Fix: use CLAUDE_CODE_ATTRIBUTION_HEADER to avoid breaking cache"*,
- **`farion1231/cc-switch`** — issue #2025, *"Add 'Disable Attribution Header' toggle to Quick Settings"* — **= corpus subject v73.**

Three unrelated projects, one un-documented default, three separate workarounds. That is the same shape as v243's flaky-shell N=2 and it is stronger: an **N=3 cross-organisation convergence on a Claude Code defect**, discovered because this ship happened to grep for it.

**⚠️ THE HONESTY GUARDRAIL — read this before acting on it.** Two claims here have very different reach, and conflating them would be the most damaging error this wiki could make:

- **The mechanism transfers.** A system-prompt section that varies per turn defeats prefix caching. That is true of any cache keyed on a prefix.
- **The "~90% slower" number does NOT transfer.** It is measured against a **local llama.cpp server on a CPU runner at ~16 tok/s**, where a miss means re-prefilling from scratch. Anthropic's own cache economics are different (cache write 1.25×, cache read ~0.1×), and the documentation issue is explicitly scoped to **`ANTHROPIC_BASE_URL`** — i.e. third-party, proxied, and local endpoints. **Do not tell anyone this will cut their Anthropic bill by 90%.** Whether `CLAUDE_CODE_ATTRIBUTION_HEADER=0` changes anything at all against Anthropic's first-party endpoint is **NOT VERIFIED** by this analysis, and the natural assumption is that Anthropic handles its own header without breaking its own cache.
- `--exclude-dynamic-system-prompt-sections` has a distinct and more general rationale: it moves per-session context (cwd, git-ness, platform, shell, OS version, auto-memory paths) out of the system prompt into the first user message, so identical configurations share a cache entry across machines. For a single operator, the honest benefit is a prefix that stops moving when the working directory does.

### 2d. ⭐ Measured facts about Claude Code's prompt, from someone who had to pay for the prefill

`.github/scripts/agent-guides-drive.sh:~186-204` — a comment block written because a CPU runner made every token visible:

> The bulk of Claude Code's prompt is the built-in tool JSON schemas: measured via `claude -p /context`, the **default prompt is ~28k tokens of which ~18k is "System tools" alone**. `--allowedTools`/`--disallowedTools` only gate PERMISSION to call a tool; they do NOT remove its schema from what is sent to the model … **`--tools` is the flag that restricts which schemas are sent.** (The ~8k "Memory files" chunk is auto-loaded `CLAUDE.md`; the unsloth repo ships none, so it is 0 in CI.)

They then use `--tools ""` for a connection probe (~20 tokens total) and `--tools "Bash,Edit,Write,Read"` for a file-edit task (~2.3k vs ~18k).

**Checked against Anthropic's documentation (2026-08-19): their central claim is right and their generalisation is one clause too wide.** The CLI reference documents `--allowedTools` as *"Tools that execute without prompting for permission… **To restrict which tools are available, use `--tools` instead**"* — exactly their point. But `--disallowedTools` is documented as *"A bare tool name **removes the matching tools from Claude's context**"*, so lumping it in with `--allowedTools` is inaccurate as of today's docs. Their measured experience ("the earlier whitelist left the full ~18k in the prompt") is consistent with having tested `--allowedTools`.

**Why this matters here and not just there.** The vault has an open, self-inflicted version of this exact problem: the standing note that *"the tool catalog (~54K) remains the floor"* for subagent context, and v238's whole thesis that the first request's tool schema conditions the model's reasoning — with the recommendation to *"trial Anthropic's Tool Search Tool + `defer_loading` and MEASURE it."* Unsloth supplies the measurement instrument (`claude -p /context`) and the flag that actually moves the number.

### 2e. Version-gated, because Claude Code's CLI moves

`start.py:2384-2391`: the cache-preserving flags are only added when the local `claude` is **≥ 2.1.98**, because *"claude < 2.1.98 rejects unknown flags; no local binary means a printout for another machine, so assume a current build."* A third party tracking a first-party CLI's flag-acceptance boundary by version, with a documented fallback for the no-binary case.

---

## 3. ⭐⭐ The inversion: your own fine-tuned model as a **subagent inside** Claude Code

`unsloth start claude --as-subagent --model unsloth/model-GGUF:quant` does not repoint Claude Code. Claude Code keeps Anthropic's model and gains a tool.

`start.py:4321-4353` writes a **Claude Code plugin** into a session-scoped config directory and launches:

```
claude --plugin-dir <session>/… --allowedTools <unsloth_agent>,<unsloth_plan_agent> …
```

with the server env `UNSLOTH_CLAUDE_SUBAGENT_{BASE_URL,API_KEY,MODEL,BYPASS_PERMISSIONS,CONTEXT_WINDOW}`, then prints:

> "Unsloth is available as a local agent. Ask Claude to spawn an Unsloth or local agent."

The MCP module is `unsloth_cli/claude_subagent_mcp.py` (469 lines) and the tool identifiers are constructed at `start.py:117-120`:

```
mcp__plugin_unsloth-local-agent_unsloth__unsloth_agent
mcp__plugin_unsloth-local-agent_unsloth__unsloth_plan_agent
```

**Two variants, and the second is the interesting one.** The plain subagent gets *"Complete the assigned task directly, use the available tools when useful, verify your work"*; the plan variant is described as a **"Read-only local coding subagent … Use this local agent when Claude is in plan mode"** and instructed *"Investigate the assigned task with read-only tools … **Do not modify files.**"* There is a dedicated test — `unsloth_cli/tests/test_claude_plan_gate.py` — and a follow-up commit (`7a9749eb4`, #7437) whose subject is *"keep the local subagent unattended and out of plan mode."* So the plan-mode path was not a naming accident; it was iterated.

Codex gets the mirror treatment: an MCP server `unsloth_local_agent` exposing `spawn_local_agent`, with routing instructions (`start.py:~108-113`) that tell Codex *"you must call the `spawn_local_agent` MCP tool once with the complete task. Do not answer, simulate the result, call wait, or use a built-in subagent before calling the tool."* Pi gets a **TypeScript extension**, `unsloth_cli/pi_subagent.ts` (409 lines), shipped inside the pip package via `[tool.setuptools.package-data] unsloth_cli = ["codex_fallback_prompt.md", "pi_subagent.ts"]`.

**⇒ This is the exact inverse of v235.** deepseek-harness shipped **Claude Code as a delegatable subagent of the runtime**, via Anthropic's official Agent SDK, and the vault recorded a *"delegation-vs-emulation watch axis."* Unsloth runs the arrow the other way: **the frontier harness stays in charge and delegates downward to a model you trained.** Same axis, opposite direction, different economics — v235's version buys capability, this one buys cost and privacy, and the plan-mode variant buys *cheap reconnaissance before expensive reasoning*.

**Pi is corpus-recursive, and Unsloth's own comment documents the v228 finding.** `.github/scripts/agent-guides-install.sh`, in the `pi)` case:

> The CLI moved from the now-deprecated `@mariozechner` scope to `@earendil-works` (the old scope is frozen, so installing it would test a stale Pi against the API).

That is v36 → v228 — Mario Zechner's `pi-mono` becoming Earendil Inc.'s `pi` — written down as an operational hazard by a third party. **Pi is now depended on by three frontier-adjacent projects the corpus tracks** (DeepSeek's harness at v235, llm-space at v221, and this).

---

## 4. ⭐⭐⭐ Executable documentation: CI that installs six agent CLIs and drives them at a live server

This is the most unusual thing in the repository, and it is the piece the vault has spent eleven ships trying to build.

`.github/workflows/local-agent-guides-ci.yml` + `.github/scripts/agent-guides-install.sh` + `agent-guides-drive.sh` install and then **drive six real coding agents** — `claude`, `codex`, `hermes`, `openclaw`, `opencode`, `pi` — against a live `unsloth run` server. The install script's own header states the contract:

> The install recipes **mirror the `install_hint` strings in `unsloth_cli/commands/start.py` at HEAD.**

and the drive script's states the mechanism:

> **Self-updating:** for all six agents … we obtain the exact env + command from **`unsloth start <agent> --no-launch`** and run **THAT**, so a recipe change is exercised automatically.

**⭐ That sentence is the whole idea, and it is not a linter.** Every answer this corpus has found to documentation drift has been either *prevention* (v243/v244's symlink, v244's `render_skill_for_target()`) or *detection* (v239's `verify-docs.mjs`, v240's prose-vs-`CAT_IDS` build gate). Unsloth's answer is a third thing: **make the documented recipe a command's output, then execute the output.** There is no prose to lint, because the prose is generated by the code under test. Drift cannot be reported late; it fails the build.

The failure taxonomy is deliberately three-way so a red build says *which* thing broke:

- **(a)** server preflight — the server never came up
- **(b)** *"agent package install failed"* — npm/curl flakiness, isolated *because* "it is the single biggest source of false reds"; retries 3× with linear backoff
- **(c)** **"guide drift"** — *"the server preflight already passed and the agent CLI already installed, so a failure here means the documented recipe … no longer produces a working flow."*

And beyond running the recipe, `crosscheck_contract()` asserts the *knobs* so a silent refactor also fails: Codex's env key is still `UNSLOTH_STUDIO_AUTH_TOKEN`, Codex's `wire_api` is still `"responses"`, Claude still exports `ANTHROPIC_AUTH_TOKEN` (hard fail) and still sets `CLAUDE_CODE_ATTRIBUTION_HEADER` (warning), OpenClaw's and Pi's provider api is still `"openai-completions"`.

Three more details that mark this as production-grade rather than aspirational:

- **`curl | bash` is de-fanged.** `curl_bash()` downloads to a temp file and *only executes on a fully successful fetch*, "so a truncated download (network hiccup mid-stream) can never run a half-written installer." Against v234's plaintext-`http://` installers, this is the corrective.
- **The Hermes installer is pinned to a full commit SHA.** `_HERMES_INSTALL_COMMIT = "f1af945f6c576eccb126fa955edc9be258b33020"`, threaded into *both* the fetched script and the checkout it performs, *"so a later change to either upstream branch cannot silently replace code that Unsloth executes with the user's privileges."* Pinning a `curl|bash` to a commit is the best handling of that anti-pattern the corpus has recorded.
- **Secrets are redacted on the way to artifacts, and the redaction is portable.** `redact()` handles GNU *and* BSD `sed` explicitly "so the redaction is never silently skipped"; the *executed* script is the un-redacted one from a temp path outside the artifact dir, because redacting `export TOKEN=sk-…` into `export TOKEN=<REDACTED>` would be invalid bash and "silently breaks every agent."

**⚠️ What it does not cover.** This tests the *recipe*, not the prose. Most Unsloth documentation lives **off-repo** at `unsloth.ai/docs` — the tree holds only 27 `.md` files and the README links out ~30 times. So the CI validates behaviour the website describes without ever reading the website. That is a real limit and a real lesson: **a doc-consistency check can only reach the docs in the repository; moving your documentation to a website moves its drift outside CI's reach.** Unsloth's mitigation is the right one available to them — test the command, not the sentence — but the sentences on the website are unguarded.

---

## 5. ⭐⭐⭐ The payoff for this vault: BUDGET.md declares which copy wins

`.github/scripts/kaggle_t4_ci/BUDGET.md` exists to justify one number — the `--percent 40` sampling rate in `kaggle-t4-notebook-ci.yml`, which spends the project's free Kaggle T4 quota as CI GPUs. It is a derived budget: measured demand (479 commits/wk, 9.4% touching the paths filter → 88–231 eligible invocations/wk), measured supply (60 GPU-h/wk, 30h guaranteed, 40h allotted), measured session cost from **named kernel IDs** (`066cd463`, `8161ceb9`, `7ab727f1` → ~0.25 h/invocation), and then the arithmetic: `231 × r × 0.25 = 30 → r = 0.52, set to 40%`. It distinguishes the **rate** (expected spend) from the **reserve** (`--reserve-hours 20` = the ceiling), notes `--budget-hours` is *derived* from `launch.py`'s constants, and points at the test that recomputes it (`tests/kaggle/test_t4_smoke_harness.py:2781`, `test_the_reserved_budget_covers_every_billable_launcher_phase`).

But the sentence that matters to us is in the second paragraph:

> **The workflow header is the source of truth.** The BUDGET block at the top of `kaggle-t4-notebook-ci.yml` carries the same arithmetic beside the settings it justifies, so it cannot drift from them silently the way this file can. **If the two ever disagree, the workflow is right and this file is stale; fix this file.**

**⭐⭐⭐ AND THE RULE HAS ALREADY BEEN TESTED IN PRODUCTION — BY THIS VERY FILE, WHICH IS NOW STALE.**

`BUDGET.md` and the workflow header now disagree on the headline number, and the disagreement is not subtle:

| | `BUDGET.md` | `kaggle-t4-notebook-ci.yml` |
|---|---|---|
| allowance | *"This workflow is allotted **40 GPU-h/week** of it"* | **`:78`** *"This workflow is allotted **15 GPU-h/week** of it"* |
| the arithmetic | `231 × r × 0.25 h = 30 h → r = 0.52, set to 40%` | **`:129`** `231 × r × 0.25 h = 9 h → r = 0.156, set to 15%` |
| the flag actually run | *"the workflow runs `--percent 40`"* | **`:368`** `--percent 15` |
| busy-week spend | 23.1 GPU-h | **`:133`** 8.7 GPU-h |

And the workflow header explains exactly why, at **`:136-137`**:

> An earlier revision of this block ran **40% for ~23 GPU-h/week**, sized against **a 40h allowance from before the Studio leg existed.**

A second GPU consumer (Studio GPU CI) appeared, the account allowance was re-split, the workflow was updated to `--percent 15` — **and `BUDGET.md` still teaches the 40% arithmetic.** The prose drifted on the exact number it exists to justify.

**⭐⭐⭐ This is the proof, and it is better than the rule.** The declaration did not prevent the drift. It made the drift **harmless and self-diagnosing**: a reader who finds the two disagreeing is told, by the stale file itself, that the workflow wins and that *this* file is the one to fix. The drift cost a reader nothing.

**Set that against v243, which is the control condition.** ToolJet had the doctrine — *"Stale context is worse than no context"* — a same-PR update policy, and a template. It had no precedence declaration and no linter. Its one committed plan file cited **three non-existent documents for eight weeks**, and it *misled*. Unsloth has no linter either. Same failure mode, opposite outcome, and **the entire difference is one sentence.**

**⭐⭐ D32 (new) — when two documents must carry the same fact and you cannot mechanise it away, declare which copy wins, *inside the copy that loses*.**

This is the cheapest answer to doc drift the corpus has found, and it is the only one that needs no machinery at all. The prevention answers (symlink, generator) require the two copies to be *the same artifact*, which fails as soon as the copies serve different readers — a prose explainer and a workflow header genuinely need to be two files. The detection answers (linter, build gate) require someone to write and maintain the checker. **Declaring subordination requires one sentence, and it converts a silent contradiction into a resolved one:** a reader who finds the two disagreeing is not confused, they are instructed.

**Applied to this vault, immediately.** `_state/03c-projects-v61-v183.md` has held entries through v245 for sixty-two versions. Four ships (v239, v240, v242, v243) have diagnosed exactly this defect and the fix has never been run, because every proposed fix was a multi-file project. **The rename is still the right fix. But D32 says the rename is not the only fix, and a one-line header inside the file — "the entries are authoritative; the filename's version range is stale, see CLAUDE.md's chapter index" — costs one edit and removes the ambiguity today.** The corpus has been holding out for the clean solution and shipping nothing; Unsloth's answer is that the cheap solution is not a compromise, it is a different and complete one — **and their own stale `BUDGET.md` is the experiment that proves it.**

⭐ **One more thing worth taking from this file: the honest-deficiency discipline.** `legs.py:376-401` keeps a `grpo` leg **written and deliberately unwired**, in an `UNWIRED: dict[str, str]` whose value is the *reason* — including the verbatim error (`torch.AcceleratorError: CUDA error: an illegal memory access was …`), the reproduction rate (*"one session in three"* on Turing), what was already ruled out, and the condition for re-wiring (`:433-434`: *"`grpo` held that seat before, and returns to it once the illegal memory access in UNWIRED is understood"*). A disabled test that says why it is disabled, in a data structure, is the strongest Pattern **#83** instance this corpus has recorded — the opposite of a silently-skipped test.

---

## 6. 🔴 The licence boundary: stated in prose, contradicted by the packaging

`README.md:452`:

> Unsloth uses a dual-licensing model of Apache 2.0 and AGPL-3.0. **The core Unsloth package remains licensed under Apache 2.0**, while **certain optional components, such as the Unsloth Studio UI** are licensed under … AGPL-3.0.

The tree says something narrower is true and something wider is shipped.

**Counted (`grep -rlE 'SPDX-License-Identifier: *AGPL' <dir> | wc -l`):**

| location | AGPL-headered files |
|---|---|
| `studio/` | 2,693 |
| `tests/` | 311 |
| `.github/` | 73 |
| `scripts/` | 42 |
| `unsloth_cli/` | **36** |
| **`unsloth/`** (the Apache "core") | **3** |
| root (`install.sh`, `install.ps1`, `cli.py`, `build.sh`) | 4 |
| **total distinct FILES** | **3,162** |

*(⚠️ **3,162 files / 3,164 occurrences** — two files carry the tag twice. My first draft reported 3,164 as a file count. `grep -rl \| wc -l` counts files; `grep -rho \| wc -l` counts occurrences, and conflating them is the same error class as commits-vs-trailer-lines.)*

**How many reach the wheel: ~2,110, not 2,732.** `pyproject.toml:98-100` adds `[tool.setuptools.exclude-package-data] "studio.backend" = ["tests/*"]`, which removes **622 AGPL-headered files** under `studio/backend/tests/`. So the shipped package carries roughly `3 + 36 + (2,693 − 622) = 2,110`. ⭐ **And the reason that exclusion exists is documented in the same file, in the best packaging comment in this corpus:**

> `packages.find` only decides what is **importable**. `include-package-data` then hands **every tracked file to the nearest parent package that survived**, so dropping `studio.backend.tests` above just **re-shipped the same 505 files as data of `studio.backend`** (pypa/setuptools#3260). `exclude-package-data` has the highest precedence … so the veto has to be repeated here.

They hit a real setuptools footgun, understood it, cited the upstream issue, and wrote down why the fix has to be stated twice. *(Their comment says 505 files; I count 622 AGPL-headered files under that path today — the number grew, the mechanism is the same.)*

**Files carrying an Apache *SPDX* identifier: ZERO — but that is a fact about notation, not about licensing, and I nearly published it as if it were the latter.** The two halves of this repository use two different conventions, and they are cleanly separated:

| `unsloth/` (95 `.py` files) | count |
|---|---|
| Apache-2.0 **prose** header (*"Licensed under the Apache License, Version 2.0"*) | **56** |
| **AGPL-3.0-only SPDX tag** | **2** |
| no licence marking of any kind | 24 |
| other / vendored third-party headers | 13 |

`unsloth_cli/`: **zero** Apache prose headers, **36 of 36** AGPL SPDX tags.

So the header hygiene is mostly fine and the real finding is not about headers at all. Three facts, in order of weight:

1. **🔴 The wheel.** `pyproject.toml:11` declares `license = "Apache-2.0"`; `pyproject.toml:79-81` declares `[tool.setuptools.packages.find] include = ["unsloth*", "unsloth_cli*", "studio", "studio.backend*"]`. So `pip install unsloth` produces a package whose metadata says Apache-2.0 and whose contents include **`unsloth_cli`, which is uniformly AGPL-3.0-only (36/36, zero Apache headers)**, plus `studio.backend`. **AGPL is not confined to an "optional component" you opt into — the CLI and the Studio backend are in the default package list.** That is the claim that matters, and it does not depend on any header being wrong.
2. **Two core modules carry an AGPL tag that looks like a template slip** — `unsloth/dataset_num_proc.py` and `unsloth/models/_uma_safetensors.py`, both headed `# SPDX-License-Identifier: AGPL-3.0-only` above `# Copyright 2023-present Daniel Han-Chen & the Unsloth team`. The other 2,891 AGPL files use the *new* line, `Copyright 2026-present the Unsloth AI Inc. team … See /studio/LICENSE.AGPL-3.0`. Era-2023 copyright paired with an era-2026 licence tag is the signature of a copy-pasted header, not a relicensing — and `_uma_safetensors.py` is a **weight-loading path**, not a peripheral. Six files total show this pairing (the other four under `tests/`). **Minor on its own; it matters only because of fact 1.**
3. **Nothing enforces either convention.** No CI job checks a licence header — the exact inverse of v244 OpenSandbox, where `verify-license.yml` failed every PR whose file omitted the copyright line and thereby *propagated* an identity across 1,674 files. Unsloth has 3,164 AGPL tags, 56 Apache prose headers, 24 unmarked files and no gate, so the two anomalies can persist indefinitely. **v244 had a gate and used it to over-assert an identity; v245 has no gate and under-asserts one. Neither repo's prose matches its packaging, and in both cases the enforced artifact is the one that tells the truth** — there it was the CI job, here it is `packages.find`.

**⚠️ Two things I am NOT claiming, because both would be unfair.**

- **Not concealment.** The dual licence is disclosed in the README, both licence texts are committed at root, GitHub's own sidebar shows *"Apache-2.0, AGPL-3.0"*, and v23 recorded the arrangement in April. `studio/LICENSE.AGPL-3.0` exists (34,523 bytes) and the 2,897 headers pointing at it are **valid pointers** — I checked, expecting a dead link, and there isn't one.
- **Not a legal conclusion.** Whether shipping AGPL-headered modules inside an Apache-2.0-declared wheel creates an obligation for a downstream commercial user is a question for a lawyer, and depends on what that user imports and whether they run it over a network. What I can say is narrower and sufficient: **the README's boundary ("core Apache, optional components AGPL") does not describe the wheel's contents, and a reader who relies on it to decide what they may build on will be relying on a sentence the packaging does not support.**

**For hireui this is decisive regardless of how the ambiguity resolves.** The AGPL precedents in this corpus — v214 firecrawl, v188 OpenMontage, v243 ToolJet — all blocked productization. **Unsloth is a read-and-borrow subject, not a component.** The ideas in §2–§5 are all free to take; none of them requires importing the package.

---

## 7. The security posture is the strongest in the corpus, and it breaks the v231/v232 triad properly

The vault has recorded a **broken-authentication triad** three times — bind `0.0.0.0`, wildcard CORS, auth fails open (v231 CoreOfPotato, v232 gemini-web2api, and partially v244 OpenSandbox). v244 was the first *positive* counter-example, and its answer was a consent gate around an insecure default. **Unsloth's answer is better: it does not have the insecure default.**

| leg | Unsloth Studio | evidence |
|---|---|---|
| **bind** | ✅ **`127.0.0.1` by default** | `unsloth_cli/commands/studio.py:1709`, `:2268` — `typer.Option("127.0.0.1", "--host", "-H")` |
| **auth** | ✅ **real, mandatory** | `studio/backend/routes/auth.py` (30,483 B): password login + JWT + refresh, `requires_password_change` on the default admin, API-key create/list/revoke, **per-IP *and* per-user failure buckets with lockout** (`_record_login_failure`, `_login_blocked`, `_overflow_blocked`), `set_desktop_initial_password` gated to the desktop app |
| **CORS** | ⚠️ **default `["*"]`** | `studio/backend/utils/host_policy.py:50-56` — *"Default is any-origin (`["*"]`); api-only locks down to the Tauri desktop app"* |

Plus a `--secure` mode that **forces loopback**: `studio/backend/run.py:2258-2266` rejects `--secure --no-cloudflare` and then sets `host = "127.0.0.1"` *"so the raw port is never public (even `-H 0.0.0.0`)"* — remote access is published **only** through the authenticated Cloudflare tunnel.

**⭐ The nuance that is worth a rule.** The CORS leg *is* wide open by default and `allow_credentials = True` (`studio/backend/main.py:1324-1334`), and `RemoteAccessCORSMiddleware.is_allowed_origin` additionally returns true for **any** origin while a Cloudflare URL is published. In v231/v232 that combination was a live hole. Here it is much smaller, for a reason located somewhere else entirely: **`grep -rn 'set_cookie'` across `studio/backend/**/*.py` (excluding tests, vendor and assets) returns nothing** — the session token travels as `Authorization: Bearer` via `HTTPBearer` (`studio/backend/core/inference/llama_keepwarm.py:289`: *"Every tracked media route depends on `get_current_subject` (HTTPBearer)"*). A browser does not attach a bearer header cross-origin on its own, so a malicious page cannot ride the session the way it could ride a cookie.

**⇒ D33 (new): the broken-auth triad is not three independent sins. The severity of the wildcard-CORS leg is contingent on the token transport — cookie-borne sessions make it critical, header-borne bearer tokens make it minor.** The corpus has been scoring these three legs as if they were additive. They are not: leg 3's weight is set by a design decision (cookies vs headers) that the triad does not even mention. Any future subject scored on this triad must be asked how it carries the token before the CORS finding is weighted.

**⚠️ NOT VERIFIED:** whether the frontend persists the JWT in `localStorage` (which would make XSS→token-theft the real vector and would matter more than the CORS default). I did not read the frontend auth store.

And one comment that shows the level they are operating at — `main.py:1329-1333`, justifying `max_age = 60` on the CORS preflight cache:

> `is_allowed_origin` closes the moment the tunnel URL clears, but a preflight already cached by the browser does not. **Measured in WebKit: with Starlette's 600s default, a state-changing request still REACHED the server after remote access was stopped** (Chromium/Firefox/Edge re-preflighted). Keep the stale window short so revocation is nearly as immediate as every other trust signal here.

They found a browser-specific revocation gap in their own remote-access kill switch, measured which engines exhibited it, and shortened the window.

### Supply chain: `studio/frontend/.npmrc` is the new high-water mark

pi v228 held the corpus's title for supply-chain hardening with `min-release-age=2`. Unsloth's file is stronger, and stronger in a specific way — **it documents the limits of its own controls**:

- `min-release-age=7`, named as *"Mini Shai-Hulud / Axios-style supply chain defense … closing the typical 4-72h attack window between malicious publish and upstream removal"*
- the parsing footgun: *"npm interprets the bare integer as DAYS; do not append `d`, npm 11.x will parse `7d` as a Date string and abort"*
- `save-exact=true`, `audit-level=high`, `registry=` pinned — **and then the pin's own defeat condition**: *"this does NOT block an ambient `NPM_CONFIG_REGISTRY` env var: npm and bun honor that at a higher precedence than this project file. **That is exactly why Unsloth does not read `NPM_CONFIG_REGISTRY`** and instead exposes one deliberate, explicit opt-in"* (`UNSLOTH_NPM_REGISTRY`, tied to issue #6491)
- *"use `npm ci` (never `npm install`)"*

**ZERO npm lifecycle scripts** (`preinstall`/`postinstall`/`prepare`) across all three `package.json` files. **⇒ min-release-age reaches N=2 in the corpus (pi v228 at 2 days, Unsloth at 7), and the practice of stating what your own control does not cover is worth copying on its own.**

`.github/dependabot.yml` is present and unusually well-reasoned — per-ecosystem cooldowns, security-update groups that bypass the version-PR cap, and a paragraph explaining why `glib`/`gdk-pixbuf` are pinned below 0.19 (archived GTK3 bindings; `native_clipboard.rs` stops compiling) *including* the admission that this "also suppresses security PRs above 0.18, leaving alerts only." It even documents a **removed** stray `bun` entry and why it was a no-op.

**D28 does not apply here.** v244's rule — an absent config file is not an absent check — was needed because OpenSandbox's scanning ran invisibly through repository settings. Unsloth has both: `dependabot.yml` is committed, and the workflows name codeql (2 files), semgrep (2), pip-audit (3), trivy, scorecard, snyk and `npm audit` (13). **41 workflows, 35 on `pull_request`, 11 scheduled.** Test surface: **1,071 Python test files + 393 TypeScript test files.**

---

## 8. Studio, the application: what a 24,449-line route file means

`studio/backend/routes/inference.py` is **24,449 lines in one file** (1.1 MB); `studio/backend/core/inference/llama_cpp.py` is 23,170; `routes/training.py` 190,929 bytes; `routes/settings.py` 104,338; `routes/models.py` 209,554. These are not generated — they are dense, heavily-commented, hand-written accretion, and the comment quality (see every quote above) is the highest this corpus has recorded. It is genuinely hard to call: the same repository that documents a WebKit preflight-revocation measurement in a code comment also has a single route module the size of a small operating system.

Studio serves **`/v1/chat/completions`, `/v1/messages`, `/v1/responses`, `/v1/completions`** (`inference.py:137-138`) — i.e. **both an OpenAI-compatible and an Anthropic-compatible API**, which is how `unsloth start claude` works at all: Claude Code speaks the Anthropic Messages API, so Studio implements it locally in front of a GGUF. README line 267 confirms the intent: *"through Unsloth's OpenAI- and Anthropic-compatible APIs."*

**And a self-inflicted observability gap, disclosed by the project itself.** `.github/scripts/assert-prompt-cache.sh:15-28` explains why the CI has to read a log rather than an API field:

> the Anthropic `/v1/messages` path builds `AnthropicUsage(input_tokens=…, output_tokens=…)` at `inference.py:8787-8790` / `:8829-8832` and **NEVER sets `cache_read_input_tokens`**, which therefore stays at its model default of 0 … So an Anthropic-path client (Claude Code) **can get a real KV-cache hit that the API usage field reports as 0.** The only ground truth for the Anthropic path is the llama-server log.

⚠️ **Direct consequence for anyone metering a routed Claude Code**: if you point Claude Code at Unsloth and read `cache_read_input_tokens` to measure cache efficiency, **you will read 0 on every request regardless of the truth.** The corpus's own cost-optimisation thread (ccusage → OTel) depends on that field. Their OpenAI `/v1/chat/completions` path *does* forward the real number (`inference.py:482-489` → `:519`); only the Anthropic dialect drops it.

**Other modalities** (README §Features, corroborated by route files): diffusion image + **video** (`routes/video.py`, `core/inference/diffusion.py`, `video.py`), **whisper** (`routes/whisper.py`), TTS, embeddings, RAG (`routes/rag.py`, 39,705 B), deep research (`routes/research_runs.py`), YouTube ingest, and **Data Recipes** for dataset construction from PDF/CSV/DOCX. Studio is a local-AI workstation, not a fine-tuning front end.

The **MCP surface is separate and opt-in** (`studio/MCP.md`): `UNSLOTH_STUDIO_ENABLE_MCP=1` + a mandatory `UNSLOTH_STUDIO_MCP_TOKEN`, exact-Bearer-checked on HTTP *and* WebSocket, at `http://127.0.0.1:8888/mcp/`. Tools include `studio_status`, `list_local_models`, `start_training`, `stop_training`, `get_training_status`, `list_training_runs`, `validate_recipe`, `load_checkpoint`, **`export_gguf`**. The doc states the reason for opt-in plainly: *"tools can consume GPU memory, write model artifacts, and stop active work."* `start_training` is validated by the existing Pydantic `TrainingStartRequest` before any subprocess starts. **⇒ An MCP client can start and stop training runs and export weights — a genuine capability, correctly fenced.**

---

## 9. Provenance

**Claude:** **46 commits** on `HEAD` match `Co-Authored-By: Claude` (**121** with `--all`), carrying **137 trailer lines** on `HEAD`. Mean 2.98 lines/commit — between v244's 1.73 (merge-dominant) and v243's 5.48 (squash-dominant), consistent with this repo's mixed strategy (570 merges, 3,267 `(#NNNN)` squashes). **D26 holds and the gradient is now three-point.**

Model census (trailer lines, `HEAD`, both capitalisations summed): **Opus 4.8 = 91** (59 + 17 + 8 + 7, incl. 15 naming `(1M context)`), **Opus 4.6 = 17**, **Fable 5 = 9**, **Opus 4.5 = 6**, **Opus 4.7 = 6**, **Sonnet 4.6 = 3**, **Sonnet 5 = 2**, **Sonnet 4.5 = 1**, unversioned = 2. So ~**98.5% name a model version** and the fleet is current — Opus 4.8 is two-thirds of it. Note the casing split (`Co-Authored-By` vs `Co-authored-by`) — a naive case-sensitive grep under-counts by ~25%.

**⚠️ The trailer-counting trap fires in BOTH directions here, and I walked into the second one.**

*Direction 1 — the over-count.* A naive body grep returns `openai` 829, `gemini` 546, `codex` 390, `Cline` 191. **Essentially all of those are file paths and feature names**, because this repo *is about* AI tools (`openai_codex_auth.py`, `test_gemini_provider.py`, `codex-reasoning.ts`). This is v244's error class (a critic's "51 Cursor commits" → ~46) with a 100× multiplier available.

*Direction 2 — the under-count, which is mine.* Having avoided direction 1, I grepped for trailers with the tool as the **key** (`Made-with: Cursor`) and reported **1**. That was wrong. Enumerating every `Co-Authored-By` **value** on `HEAD` (`git log --format='%B' HEAD | grep -ihE '^ *Co-Authored-By:' | sed … | sort | uniq -c`) gives **104 non-Claude AI trailer lines**:

| co-author | lines | what it actually is |
|---|---|---|
| `gemini-code-assist[bot]` | **86** | Google's PR-review **GitHub App** — a bot, not a human using an AI tool |
| `Cursor <cursoragent@cursor.com>` | **12** | Cursor's background agent |
| `Copilot <…Copilot@…>` | 2 | GitHub Copilot |
| **`Copilot Autofix powered by AI <…github-advanced-security[bot]>`** | **2** | ⭐ a **bot** — and **v244's D28 detector firing again**: this is proof GitHub Advanced Security scanning runs, independent of the committed workflows |
| `Codex <noreply@…>` | 2 | OpenAI Codex |

For scale, the largest co-author of all is `pre-commit-ci[bot]` at **1,309** lines — a lint bot, not an AI coding tool.

**⇒ The rule needs both halves: report AI-tool usage from trailer *structure*, not from body text — and check both the key form (`Made-with: X`) and the value form (`Co-Authored-By: X`). v244 established the over-count half; this ship supplies the under-count half, and the corrected picture changes the story** (Gemini's bot is the single largest AI co-author here, and it is doing review, not authoring).

**Corporate domains** among the 298 authors include `intel.com` (Lei Zhenyuan, 22) and `gravityq.ai` (Roland Tannous, 372).

### ⭐⭐ The tag list dates the identity shift, and my first reading of it was wrong

I reported "79 tags, all `v0.1.NNN-beta`, no non-beta tag in history." **That is false — 26 of 79 are non-beta** — and the true shape is a much better finding. (My error: `git tag | tail -20` sorts **lexically**, so `v0.1.*` sorts last and the calendar tags never appeared. **`tail` on `git tag` is a sampling bias, not a recency view** — use `for-each-ref --sort=creatordate`.)

| era | dates | tags | convention |
|---|---|---|---|
| **library** | 2024-07-03 → 2026-03-17 | **24** | `July-2024`, `July-Mistral-2024`, `July-Llama-2024`, `August-2024` … `2025-01`, `2025-02-v2` … `February-2026`, `March-2026` — **month/model milestones, not product versions** |
| *(vendored)* | 2026-03-20, 03-22 | 2 | `b8457`, `b8475` — llama.cpp build numbers |
| **product** | **2026-03-20 → 2026-08-14** | **53** | `v0.1.0-beta` … `v0.1.800-beta`, plus `desktop-v0.1.526-beta` / `desktop-v0.1.527-beta` |

**`v0.1.0-beta` was cut on 2026-03-20 — eleven days after the AGPL licence landed on `studio/` (`ac2906f35`, 03-09) and three days after `cli/` became `unsloth_cli/` (`0c8d40779`, 03-17).** A library that ships continuously tags months. A product that ships installers needs version numbers, and a `desktop-` tag. **The versioning scheme changed because the artifact changed, and the tag list records the date the identity flipped.**

Two further facts:

- **The rate.** 24 tags in the 20 months to 2026-03, then **53 in the 5 months since** — including **8 in five days**, 2026-08-10 → 08-14 (`v0.1.60`, `.61`, `.62`, `.70`, `.701`, `.702`, `.71`, `.800`).
- **Two versioning schemes coexist, one per identity.** `unsloth/_version.py` — *"The single source of truth for this package's version"* — reads **`__version__ = "2026.8.18"`**, calendar versioning, the library's convention. The desktop product is `v0.1.800-beta`. **The pip package and the app it ships do not share a version scheme.**

**And the claim that does survive, restated correctly: the product line has never left beta.** All 53 `v0.1.*` tags are `-beta`; a 73.7k★ project shipping signed macOS/Windows/Linux installers has never cut a stable release.

---

## 10. Doc defects found by hand (and one non-defect)

Applying **D29** — *`mtime` is not drift; test the claims, not the date* — I tested README claims against the tree rather than dating them.

- 🔴 **The README's own agent table is missing an agent.** `README.md:106-110` lists **five**: Claude Code, OpenAI Codex, Hermes Agent, OpenClaw, OpenCode. The code and CI support **six** — `agent-guides-install.sh` states *"agent in: claude codex hermes openclaw opencode pi"*, `pi_subagent.ts` ships in `package-data`, `write_pi_config` is contract-checked in CI, and `unsloth_cli/tests/test_pi_subagent.py` exists. **Pi is a first-class supported agent that the README's feature table omits** — prose-vs-code drift in the exact feature that is this ship's headline. (Line 116's `--as-subagent` example and line 267's news entry also both stop at five.)
- 🔴 **A duplicated bullet.** `README.md:78` — *"**Search & RAG:** Use private and unlimited web search, deep research, and RAG."* — and `README.md:80` — *"**Search:** Use private and unlimited web search, deep research, and RAG."* The same sentence under two bold labels, two lines apart, in the Features list.
- ✅ **The non-defect I expected to find.** 2,897 headers point at `/studio/LICENSE.AGPL-3.0`. I went looking for a dead pointer — v240's `README.ja.md` case. **The file exists.** Reporting it as broken would have been the error; **D29 cuts both ways, and "test the claim" includes testing the claim you want to be true.**

**Docs live off-repo.** 27 `.md` files in tree; the documentation home is `unsloth.ai/docs` (including a page literally titled *"How to Run Local LLMs with Claude Code"*). The in-tree markdown is mostly design notes and CI budget. This is why §4's mechanism matters more than a linter would: they cannot lint the website from CI, so they test the command the website documents.

---

## 11. Corpus decision

**Classification: GOAL-ALIGNED INCLUDE 3/4.**

- **(a) FAIL** — Unsloth AI Inc. (Daniel Han + Michael Han). Corporate, not Anthropic; no registered (a)-7 vendor-direct axis. Per **§41** no name/notability/heritage inference rescues it. Same call as v23 by different reasoning.
- **(b) STRONG — and this is the whole event.** v23 keyed this subject as **(b) FAIL / OUTSIDE-SCOPE, "not agent infrastructure."** At HEAD it ships an MCP server, a Claude Code plugin, a six-harness connect layer, and CI that drives six agent CLIs. **(b) has flipped FAIL → STRONG on the same repository without any criteria change** — goal-#1 core, not adjacent, no §40 needed.
- **(c) STRONG** — source-cloned twice, everything above is file:line evidenced.
- **(d) STRONG** — directly actionable: §2a credential-stripping, §2c the cache knobs, §2d the `--tools`/`/context` measurement, §4 the executable-recipe mechanism, §5 D32, §7 the `.npmrc`.

**Streak: v244 `GA:102` → `GA:103 · OG:13 [7 ov]`** (26 consecutive GA, v220→v245). **§35 CLEAR** — window {v243 GA, v244 GA, v245 GA} = 0 OG.

**Counts: 46 confirmed patterns / 11 CONFIRMED Library-vocab — UNCHANGED.**

### The mint

**⭐ ONE NEW §C standalone at N=1: "Self-Hosted / Locally-Trained Model Registered as a Delegatable Subagent Inside a Frontier Coding-Agent Harness."** §C live standalones **50 → 51**; surface ≈57 → ≈58.

**Grounds.** The corpus holds the *opposite* arrow and nothing else: v235 deepseek-harness ships **Claude Code as a subagent of the runtime** via Anthropic's Agent SDK, and the vault explicitly logged a *"delegation-vs-emulation watch axis"* as DEFERRED. v171 devspace bridges a hosted chat host down to a local machine (a different object: the whole agent, not a delegate). No §C row describes downward delegation from a frontier harness into a self-hosted model. Unsloth ships it three ways (Claude Code plugin + MCP, Codex MCP server, Pi TypeScript extension) with a **read-only plan-mode variant** that is separately tested — i.e. it is implemented, not gestured at. Capability, not domain.

**⚠️ NO-MINT alternative RECORDED and non-trivial (audit-reviewable).** Two arguments against: (i) this is a *direction* on an axis v235 already opened, and the disciplined move might be to state that axis mechanism-agnostically and call this its N=2 rather than open a new row; (ii) *pointing* a harness at a self-hosted model has heavy prior art (claude-code-router, LiteLLM, **cc-switch v73**, the GLM/Kimi vendor guides, opencode-antigravity-auth v67) and if the row were drawn one notch wider it would be born stale at N=6. I have drawn it at the **subagent/delegation** boundary specifically to exclude the redirection class, and that boundary is the thing an audit should test. **Corpus-first for the surface; NOT world-first** — pending the prior-art sweep, treat world-first as unestablished.

**Explicitly NOT minted:**

- **The `unsloth start` six-harness connect layer** — decisive prior art above; and cc-switch **v73** is already the corpus's harness-endpoint switcher.
- **The desktop fine-tuning GUI.** The README's line 9 — *"**Unsloth is the first desktop app to run and train models**"* — is a **world-first claim I am not repeating, because the most obvious counter-example is staffed inside this repository.**

  `oobabooga/text-generation-webui` — since renamed **textgen** — ships a **Training tab for LoRA fine-tuning**, documented at `docs/05 - Training Tab.md`, which opens *"Training Your Own LoRAs"* and covers dataset configuration, parameter tuning, checkpoint resumption, and training 4-bit quantized models (QLoRA in substance). Its own current GitHub description reads: *"**Open-source desktop app for local LLMs.** Text, vision, tool-calling, **OpenAI/Anthropic-compatible API.** 100% private."* That is every element of Unsloth's claim — desktop app, local models, run **and** train, and even the same dual OpenAI+Anthropic API surface — from a project that predates Unsloth Studio by roughly three years. H2O LLM Studio (2022) precedes on function too.

  ⚠️ **One of my own fleet agents asserted textgen is "inference only … no GUI for fine-tuning." That is REFUTED by the repository's own documentation**, fetched directly. Recorded as a caught agent error, because it was the load-bearing premise under that agent's verdict of *"world-first for the desktop fine-tuning GUI form factor"* — a verdict I therefore do not adopt.

  **And the author of textgen has 151 commits in this repository, every one prefixed `Studio:`** — author `oobabooga <oobabooga4@gmail.com>`, co-author line `oobabooga <112222186+oobabooga@users.noreply.github.com>`, first commit 2026-05-26, latest 2026-08-19, including `387547980` (#7329) *"Complete local subagent delegation for Codex, Claude plan mode, and Pi."* GitHub usernames are unique, and `oobabooga` is the account that owns `oobabooga/textgen`. **So the person who built the strongest counter-example to Unsloth's world-first claim is now building the product that makes it.** *(⚠️ Whether Unsloth **employs** them is **NOT VERIFIED** — a contributor is not necessarily a hire. And the only reading under which Unsloth's claim survives is "first *packaged native* desktop app" — a Tauri binary versus a locally-served Gradio UI — which textgen's own "desktop app" self-description undercuts, and which the README does not qualify.)*

  ⭐ **The dates line up with the tag archaeology and close the loop.** Unsloth Studio (web) went beta around **2026-03-17**, matching `v0.1.0-beta` on 03-20; **Unsloth Desktop (Tauri) went beta 2026-08-11→14**, which is exactly the **8-tags-in-5-days burst** (`v0.1.60` → `v0.1.800-beta`) and the `desktop-v0.1.52x-beta` variants that appear on 08-08/09. **The tag list, the versioning-scheme change, and the world-first claim all date to the same two events: the web app in March, the native app in August.**

  ⭐ **This is the grok-build v215 primitive-convergence axis reaching the local-inference layer:** two independent local-AI apps have converged on the same self-description — desktop app, local models, OpenAI **and** Anthropic-compatible API — because the second API is what a coding agent needs. Neither started there.

  And domain-not-capability rules out a mint regardless (the meetily v196 / AIRI v210 / mlsysbook v197 discipline).
- **Training-infrastructure framework** — Pattern #41 is CONFIRMED since v23 (LlamaFactory v22 + Unsloth v23). No re-mint on a revisit.
- **Executable-documentation CI** — the mechanism of §4 is the most valuable thing here for the vault, but a *CI technique* is not a §C capability class (the v238 discipline: a rationale and a measurement are not a capability). Recorded as a **DEFERRED watch axis**: *"CI that installs and drives N third-party agent CLIs against a live server to test a documented recipe by deriving it from the code."*

### ⭐⭐ The collision I nearly missed: Studio is **N=5** of the v192 standalone

The vault-collision sweep caught something the mint discussion above walks straight past. The **v192 palmier-pro §C standalone — *"Product-First Native Application Retrofitted with a First-Party MCP Server"*** — currently stands at **N=4**, all non-port (palmier-pro v192 → tabularis v212 → voicebox v229 → worldmonitor v230), with promotion to a CONFIRMED Library-vocab item **awaiting an audit** and the trigger already *"doubly reinforced"* at v230.

**Unsloth Studio is a clean N=5 of that row, and on every clause:**

| v192 clause | Unsloth Studio |
|---|---|
| **product-first** | The README's own first line is *"Unsloth is the first desktop app to run and train models."* Decisively a product. |
| **native application** | Tauri v2, `studio/src-tauri/` (57 files, 34 `.rs`), signed installers for Windows/macOS/Linux/ARM64 |
| **retrofitted** | The MCP server is **opt-in and later** — `UNSLOTH_STUDIO_ENABLE_MCP=1` + a mandatory token, disabled by default |
| **first-party MCP server** | `studio/MCP.md` + `routes/mcp_servers.py`; 11 named tools incl. `start_training`, `stop_training`, `load_checkpoint`, `export_gguf` |

**⇒ RECORDED as instance-strengthening: the v192 standalone goes N=4 → N=5, non-port, cross-domain.** No new row. **This is the third consecutive ship to reinforce a promotion trigger that no audit has executed** (v229 N=3, v230 N=4, v245 N=5), and the corpus's only §C→CONFIRMED promotion to date (#23) happened at N=4. **⚠️ Flagged, not self-executed — a promotion is an audit act (the v232 rule). But the audit is now refusing a promotion at N=5 that it granted at N=4 once before.**

**Two different artifacts, two different findings, no conflict:** Studio (a product with a retrofitted MCP server) is v192 N=5; `unsloth start --as-subagent` (a local model registered as a delegate inside a frontier harness) is the new mint. They are different surfaces of the same repository.

**Other pattern touches (recorded, not self-promoted):**

- 🔴 **Pattern #45 Dual-Licensing — CONFIRMED since v60, but its v23-anchored sub-variant 45a is now STALE AS WRITTEN.** #45 was promoted at v60 on N=2 (Unsloth v23 Apache+AGPL + AutoGPT v59 MIT+PolyForm), and the vault celebrates that promotion as a *"35-wiki stale-then-un-stale latency = corpus-record"* proof that stale-tracking works. **The irony is exact: the anchor that validated the vault's stale-tracking machinery has itself gone stale.** 45a reads *"Apache core + AGPL UI"*; at HEAD the AGPL side is 76% of the tree and inside the wheel's default package list. **The pattern stands; the sub-variant description needs rewriting.**
- 🔴 **Pattern #46 Duo-Founder — still a CANDIDATE at N=1, and its sole anchor is *this subject*, 222 wikis later.** Registered at v23 on the Han brothers; **no second instance in v24→v244.** This ship is the natural moment to decide it: **a candidate whose only anchor has now been revisited without producing an N=2 in 222 versions is a retire candidate, not a live hypothesis.** Flagged to the (long overdue) audit. *(The revisit does **not** create an N=2 — same subject.)*
- **Pattern #66 supply-chain** — `min-release-age` reaches **N=2** (pi v228 = 2 days, Unsloth = 7), and Unsloth is now the corpus's strongest positive exemplar, displacing pi.
- **#18 B1-MCP** — +1 (two distinct MCP surfaces: the Studio server, and the subagent servers for Claude/Codex).
- **#57 corpus-recursive** — this ship is unusually dense: **Pi v36/v228** (with the v228 scope-migration finding quoted in Unsloth's CI), **cc-switch v73** (independent discovery of the same Claude Code cache defect), **opencode v67**, **hermes-agent / hermes-webui v227**, **GLM-5 v176** (which listed Unsloth as a deploy path — the dependency ran the other way), plus the **v23** anchor itself.

### New rules

- **⭐⭐ D31 — a scope verdict is a claim about a date, not a property of a subject.** OUTSIDE-SCOPE is the one verdict that closes the file, therefore the one most likely to rot unobserved. Detector: re-read the *description field* and the top-level directory shares, not the code.

  **And D31 comes with a work-list, because the population is small and enumerable.** The vault's outside-scope subjects are **v8 build-your-own-x, v20 fish-speech, v21 system-prompts-leaks, v22 LlamaFactory, v23 Unsloth** (now crossed), plus later off-goal captures. ⭐ **The highest-priority re-check is `hiyouga/LLaMA-Factory` v22** — same domain, same era, the *same* OUTSIDE-SCOPE ruling, and Pattern #41's co-anchor. If a fine-tuning framework can grow an MCP server and a Claude Code plugin in ninety days, its closest competitor is the single most likely place for it to have happened twice. **That check is one WebFetch of a description field.**
- **⭐⭐ D32 — when two documents must carry the same fact and mechanisation is impractical, declare which copy wins, inside the copy that loses.** The cheapest doc-drift fix in the corpus; needs no tooling; converts a silent contradiction into a resolved one. Immediately applicable to `_state/03c-projects-v61-v183.md`.
- **⭐ D33 — the broken-auth triad is not additive.** The wildcard-CORS leg's severity is set by the token transport (cookie = critical, header-borne bearer = minor). Ask how the token travels before weighting leg 3.
- **⭐ D19 EXTENDED — count the roots.** A single-root provenance check misses a graft: three roots here, and the repo's 2023 age is true of 4.3% of the tree.
- **⭐ D26 confirmed at a third point** — trailer-lines-per-commit tracks merge strategy: 1.73 merge-dominant (v244) → **2.98 mixed (v245)** → 5.48 squash-dominant (v243).
- **⭐ D29 cuts both ways** — testing the claim includes testing the claim you *want* to be true; I nearly shipped a dead-link finding that wasn't.

---

## 12. Error ledger

| # | error | whose | correction |
|---|---|---|---|
| 1 | "the AGPL header pointer `/studio/LICENSE.AGPL-3.0` is a dead link" | **mine** — assumed before checking | The file exists (34,523 B). **Withdrawn.** |
| 2 | "Unsloth conceals its licensing" | **mine** — opening framing | Fully disclosed: README, both root licence files, GitHub sidebar, and v23 recorded it in April. **Withdrawn**; the surviving finding is narrower and about the *wheel*, not disclosure. |
| 3 | "LlamaFactory is corpus v37" | **mine** — inferred from a chapter-index filename | It is **v22**. Caught by reading the v23 entry. |
| 4 | "auth may fail open / wildcard CORS is critical" | **mine** — pattern-matched the v231/v232 triad | Default bind is `127.0.0.1`, auth is mandatory with lockout, and no cookies are set. **Downgraded**, and the downgrade produced **D33**. |
| 5 | "Codex = 390 / Gemini = 546 / Cline = 191 AI-tool commits" | a naive body grep | These are file paths and feature names. Real non-Claude trailers: **`Made-with: Cursor` = 1.** |
| 6 | "`return "0.0.0.0"` at `run.py:214` is the bind default" | **mine**, briefly | It is a display-IP fallback inside `_resolve_external_ip`. The bind default is `127.0.0.1` at `studio.py:1709`. |
| 7 | Case-sensitive `Co-Authored-By` grep | method | Under-counts ~25%; the repo uses both capitalisations. |
| 8 | "80 of 95 core files carry no licence header, so the only files stating a licence in the Apache core state AGPL" | **mine** — drafted, then caught before publication | **56 carry the Apache-2.0 *prose* header.** The two halves use two notations (prose vs SPDX); "zero Apache SPDX identifiers" is true and **misleading**. Rewritten — and the finding got *stronger*, because it now rests on `packages.find` rather than on header hygiene. |
| 9 | "test the README's '500+ models' claim" | **mine** — carried a claim forward from the v23 entry | That claim is **no longer in the README** (`grep -niE '[0-9]+\+? models\|500\+'` → no match). Testing a claim the subject has withdrawn is the mirror of D29's error. |
| 10 | **"79 tags, all `v0.1.NNN-beta`; no non-beta tag in history"** | **mine** — published in draft, caught by a fleet verifier and then re-verified by hand | **26 of 79 are non-beta calendar/model tags** (`July-Mistral-2024` … `March-2026`) plus 2 llama.cpp build tags. Cause: **`git tag \| tail -20` sorts lexically, not by date** — a sampling bias I read as recency. The corrected reading is a *better* finding (§9: the scheme changed on 2026-03-20 and dates the identity shift). Surviving claim: **the product line has never left beta.** |
| 11 | **"real non-Claude trailers: `Made-with: Cursor` = 1"** | **mine** — the mirror of the error I was warning about | **104 non-Claude AI trailer lines on `HEAD`**: `gemini-code-assist[bot]` 86, Cursor 12, Copilot 4 (2 of them Autofix, a bot), Codex 2. I checked the *key* form and not the *value* form. **I avoided the over-count and committed the under-count in the same paragraph.** |
| 12 | "3,164 AGPL files" | **mine** | **3,162 files / 3,164 occurrences.** Two files carry the tag twice. Same class as commits-vs-lines. |
| 13 | "all ~2,700 AGPL files reach the wheel" | a fleet agent, and my draft was silent where it should have been explicit | `pyproject.toml:98-100` excludes `studio/backend/tests/*` = **622 AGPL files** → **~2,110** reach the wheel. Corrected in §6 **with** the setuptools footgun Unsloth documented. |

**13 caught, 10 mine.** Three moved the analysis *toward* the subject (#2, #4, #8) and two of those produced rules. But the pattern in #10–#13 is the one to take away: **every single one is a counting-method error, not a reading error** — lexical sort read as recency, key-form grep read as all trailers, occurrences read as files, tree read as wheel. **The vault already has D26 and D27 for exactly this family and I still made four of them in one ship.** The fleet's adversarial layer caught #10, #11 and #13; #8 and #12 I caught myself. **That is the argument for the verify stage in one line: the errors it catches are not the ones you would find by re-reading your own prose, because they are in the commands, not the sentences.**

---

## 13. Non-claims

- **NOT world-first** as a desktop train+run app (H2O LLM Studio 2022; text-generation-webui's training tab 2023) — and the README's claim is quoted, not endorsed.
- **NOT Pattern #52** — stars are page-stated (§37.4); the API is mocked here. The v23→v245 delta (62,218 → ~73.7k over 121 days) is page-stated-to-page-stated and is **not** verified velocity.
- **Do NOT cite "137 Claude commits"** — 46 commits / 137 lines on `HEAD`.
- **Do NOT claim `CLAUDE_CODE_ATTRIBUTION_HEADER=0` will cut an Anthropic bill.** The documented scope is `ANTHROPIC_BASE_URL` (third-party/local endpoints). First-party effect **NOT VERIFIED**.
- **Do NOT repeat "~90% slower"** as an API figure — it is local-CPU-prefill.
- **Do NOT claim Unsloth re-exposes a Claude subscription.** It does the opposite: it unsets the credential. *(Whether Studio's `/v1` endpoints can be backed by a connected ChatGPT/Codex subscription — which would make it a v207-class gateway — is **NOT resolved by me**; `inference.py:16699` says `/v1/models` exposes "one per loaded **local** backend", which points against it. Flagged, not concluded.)*
- **NOT VERIFIED:** whether the frontend stores the JWT in `localStorage`; whether `studio.backend`'s presence in the wheel creates a real AGPL obligation for a downstream commercial user; whether Dan Saunders' 43-commit root was an acquisition, a hire, or a contribution; the generated-vs-hand-written split of the 24,449-line `inference.py`.

---

## 14. Pilot

**⚠️ READ-AND-BORROW. The AGPL/Apache ambiguity in §6 makes Unsloth a non-component for hireui** — the v214 / v188 / v243 precedent. Nothing below requires installing it.

**Zero-install, highest value first:**

1. **Copy the credential-stripping practice (§2a)** into any script that points a coding agent at a non-Anthropic endpoint: unset `ANTHROPIC_API_KEY` and `CLAUDE_CODE_OAUTH_TOKEN` before launch. Two lines; removes a whole class of accidental billing and key leakage.
2. **Measure your own prompt** with `claude -p /context` (§2d) and then try `--tools` — not `--allowedTools` — against the vault's ~54K tool-catalog floor. This is the v238 recommendation with an instrument attached.
3. **Apply D32 to `_state/03c-projects-v61-v183.md` today** (§5): one header line naming the entries as authoritative and the filename range as stale, while the rename stays on the list. Four ships have diagnosed this; one sentence resolves the ambiguity now.
4. **Steal `studio/frontend/.npmrc`** (§7) — `min-release-age`, `save-exact`, pinned registry, and above all the habit of writing down what your control does *not* cover.
5. **Take §4's mechanism, not its scale:** if a vault routine documents a command, make the doc print the command and then run it. `verify-vault-docs` has been specified as a linter for five ships; the cheaper version is a generator plus an execution.

**Do NOT:** install the package into any hireui environment; point Studio at candidate data (the RATIFIED candidate-LLM-legibility ADR); expose Studio beyond loopback without `--secure`; or rely on `cache_read_input_tokens` when metering a Claude Code session routed through it (§8 — it is hardcoded 0 on the Anthropic path).

**⭐ Route: A1 → A2 → D32-fix.**

---

*Analysis by Claude Opus 5 for Storm Bear, 2026-08-19. Source-cloned twice at `cabed07f`. Every count declares its ref population. The v23 anchor is preserved unmodified at `03 Projects/Unsloth - Beginner Analysis/`.*
