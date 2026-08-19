# (C) Unsloth v245 — Verdict

**`unslothai/unsloth`** · ship v245, 2026-08-19 · **5th corpus-recursive revisit, ↺ v23 (2026-04-20)** · source-cloned twice at `cabed07f`

---

## The one-paragraph verdict

The corpus read this repository sixteen weeks ago and filed it OUTSIDE-SCOPE with the words *"not agent infrastructure — training-only"* and *"Direct adoption: NONE."* That was accurate on the day. It is now false, and no criterion changed — **the subject walked across the boundary while the file was closed.** `unslothai/unsloth` today ships an MCP server that can start and stop training runs, a Claude Code **plugin** that registers a locally-served model as a delegatable subagent with a separately-tested read-only plan-mode variant, a one-command connect layer for six coding-agent CLIs, and a CI job that installs and drives all six against a live server. The fine-tuning library everyone knows it for is **4.3% of the tree**; the desktop app is 75.9%; the README's own first line is *"Unsloth is the first desktop app to run and train models."* **GOAL-ALIGNED INCLUDE 3/4, (b) flipped FAIL → STRONG on the same repo, ⭐ one new §C standalone at N=1, three new rules, and — unusually for this corpus — the single most useful thing in it is not the mint but a sentence in a CI budget file.**

---

## Classification

| criterion | v23 (2026-04-20) | **v245 (2026-08-19)** | why it moved |
|---|---|---|---|
| **(a)** author | FAIL — Han brothers, not Anthropic | **FAIL** | unchanged; §41 forbids name/notability rescue. Now "Unsloth AI Inc." |
| **(b)** goal-relevance | **FAIL → OUTSIDE-SCOPE** | **⭐ STRONG** | MCP server + Claude Code plugin + 6-harness connect layer + agent CI. **Goal-#1 core, not adjacent — no §40 needed** |
| **(c)** verifiability | (page-fetch era) | **STRONG** | source-cloned twice; every claim file:line'd; every count declares its ref population (**D27**) |
| **(d)** actionability | *"Direct adoption: NONE"* | **STRONG** | 5 zero-install borrows, 3 of them one-edit |

**Tier:** T2 product + T4 agent-capability layer. **Streak `GA:102` → `GA:103 · OG:13 [7 ov]`** — 26 consecutive GA (v220→v245). **§35 CLEAR:** {v243 GA, v244 GA, v245 GA} = 0 OG. **Counts 46 / 11 UNCHANGED.**

---

## Findings, ranked

### ⭐⭐⭐ 1. A scope verdict expired and nothing noticed → **D31**

Everything that made this in-scope landed **after** the v23 ship: Local Agent Guides CI `264f1a04f` (#6547, 2026-06-22) → `unsloth start` `b8400f40d` (#6613, 07-03) → **local subagents for Claude Code, Codex, OpenCode and Pi `968e6230a` (#7326, 07-22)** → Claude plan-mode delegation `387547980` (#7329, 07-24, by **oobabooga**).

**⇒ D31: a scope verdict is a claim about a date, not a property of a subject.** The corpus re-tests facts on revisit (D25) and provenance on revisit (D19). It has never re-tested **scope** — and OUTSIDE-SCOPE is the one verdict that closes the file, which makes it the one most likely to rot unobserved. **Every prior OUTSIDE-SCOPE subject in the corpus is un-audited by construction.** Cheap detector: re-read the repo's *description field* and its top-level directory shares. Both would have caught this in seconds — the tagline the vault recorded (*"Train 500+ models…"*) is gone, replaced by *"Local UI to **run** and train…"*, and `studio/` is now three-quarters of the tree.

### ⭐⭐⭐ 2. The best Claude Code integration in the corpus — and a defect three projects found independently

`unsloth start claude` (`start.py:2394-2410`, `:146`, `:2384-2391`):

- **It strips your credentials.** `_CLAUDE_ENV_UNSET = ("ANTHROPIC_API_KEY", "CLAUDE_CODE_OAUTH_TOKEN")`. **The exact inverse of v207/v208/v231/v232**, every one of which harvested or re-exposed a credential. First subject in the corpus to treat the vendor credential as blast radius to shrink. **Two lines; copy them.**
- **It refuses to lie to Claude's safety check.** `IS_SANDBOX` deliberately unset on the user's host — *"we don't want to falsely claim one"* — and set in CI, where *"the CI runner IS the sandbox."* The disciplined pole against the v209 config-override class.
- **It sets `CLAUDE_CODE_ATTRIBUTION_HEADER=0` and `--exclude-dynamic-system-prompt-sections`, and has a CI A/B test that proves why.** `agent-guides-drive.sh:568-613` asserts a KV-cache **HIT** with the suppression and a **MISS** without it — it requires the *unfixed* configuration to fail, which makes it a regression test on the claim, not on the fix. Mechanism: Claude Code ≥2.1.36 injects a per-request `x-anthropic-billing-header` at the **front** of the system prompt; a moving prefix is a new cache key. Both knobs are **real and undocumented** — open Anthropic docs issues [#50085](https://github.com/anthropics/claude-code/issues/50085) and [#45930](https://github.com/anthropics/claude-code/issues/45930); neither string is in the current settings docs.
- **⭐⭐ N=3 cross-organisation convergence, one arm already a corpus subject:** Unsloth, `musistudio/claude-code-router` (PR #1220), and **`farion1231/cc-switch` = v73** (issue #2025) each independently hit this and each shipped a workaround.
- **It measures the prompt.** *"measured via `claude -p /context`, the default prompt is ~28k tokens of which ~18k is 'System tools' alone"*; `--tools` is the flag that shrinks it, `--allowedTools` is not. **Anthropic's docs confirm the central claim** (*"To restrict which tools are available, use `--tools` instead"*); one clause of theirs is now inaccurate (a bare `--disallowedTools` name *does* remove from context).

**⚠️ THE GUARDRAIL, and it is the most important line in this ship: the mechanism transfers, the number does not.** *"~90% slower"* is measured against **local llama.cpp on a CPU runner at ~16 tok/s**, and the documentation issue is explicitly scoped to **`ANTHROPIC_BASE_URL`** — third-party, proxied and local endpoints. **Do not claim this cuts an Anthropic bill.** First-party effect: **NOT VERIFIED**.

### ⭐⭐ 3. The inversion — your model as a subagent *inside* Claude Code → **the mint**

`--as-subagent` writes a Claude Code plugin and launches `claude --plugin-dir … --allowedTools mcp__plugin_unsloth-local-agent_unsloth__unsloth_agent,…__unsloth_plan_agent`. Two variants: a working subagent, and a **read-only plan-mode** one (*"Do not modify files"*) with its own test (`test_claude_plan_gate.py`) and a follow-up hardening commit (#7437). Codex gets an MCP server with routing instructions that override its built-in `spawn_agent`; Pi gets a 409-line TypeScript extension shipped in the wheel.

**⇒ The exact inverse of v235**, which shipped **Claude Code as a subagent of the runtime** via Anthropic's Agent SDK and left a *"delegation-vs-emulation watch axis"* DEFERRED. Same axis, opposite arrow, different economics: v235 buys capability, this buys cost and privacy — and the plan-mode variant buys **cheap reconnaissance before expensive reasoning**, which is the one form of this that is obviously worth doing.

### ⭐⭐ 4. Executable documentation: CI drives six real agent CLIs

`local-agent-guides-ci.yml` + `agent-guides-{install,drive}.sh` install and drive **claude, codex, hermes, openclaw, opencode, pi** against a live server. The mechanism is the point:

> **Self-updating:** we obtain the exact env + command from **`unsloth start <agent> --no-launch`** and run **THAT**, so a recipe change is exercised automatically.

**Eleven ships have handed this vault a piece of `verify-vault-docs`. Every prior piece either prevents duplication (v243/v244 symlink, v244's renderer) or detects it (v239's linter, v240's build gate). This is a third kind: remove the prose from the loop — the documented recipe is a command's output, so there is nothing to lint.** Plus a three-way failure taxonomy that isolates flaky installs from real drift, a `curl|bash` that downloads-then-executes so a truncated fetch can't run, the **Hermes installer pinned to a full commit SHA**, and portable GNU/BSD secret redaction *"so the redaction is never silently skipped."*

⚠️ **Its limit is instructive:** Unsloth's docs live off-repo at `unsloth.ai/docs` (27 `.md` in tree). **A doc check reaches only the docs in the repository** — which is why their answer had to be a generator rather than a linter, and why ours can be either.

### ⭐⭐⭐ 5. **THE PAYOFF — `BUDGET.md` declares which copy wins → D32**

> **The workflow header is the source of truth.** … **If the two ever disagree, the workflow is right and this file is stale; fix this file.**

**⇒ D32: when two documents must carry the same fact and mechanisation is impractical, declare which copy wins — inside the copy that loses.**

The cheapest doc-drift answer in the corpus and the only one needing no machinery. Prevention (symlink, generator) requires the copies to be *the same artifact*, which fails when they serve different readers. Detection requires writing and maintaining a checker. **Declaring subordination costs one sentence and converts a silent contradiction into a resolved one: the reader who finds the disagreement is instructed, not misled.**

**Applied now:** `_state/03c-projects-v61-v183.md` has held entries through v245 for **sixty-two versions**; v239, v240, v242 and v243 each diagnosed it; the rename has never run because it is a multi-file change. **D32 says the cheap fix is not a compromise — it is a different and complete one.** One header line, today.

*(The file is also a masterclass in its own right: measured demand — 479 commits/wk, 567 PRs/wk, 9.4% touching the paths filter — measured supply, measured session cost from **named Kaggle kernel IDs**, the arithmetic `231 × r × 0.25 = 30 → r = 0.52, set to 40%`, the **rate vs reserve** distinction, and `--budget-hours` **derived** from `launch.py` with a test that recomputes it.)*

### 🔴 6. The licence boundary is stated in prose and contradicted by the packaging

`pyproject.toml:11` → `license = "Apache-2.0"`. `pyproject.toml:79-81` → `include = ["unsloth*", "unsloth_cli*", "studio", "studio.backend*"]`. **`unsloth_cli` is uniformly AGPL-3.0-only — 36 of 36 files, zero Apache headers — and it is in the default package list.** README:452 says *"The core Unsloth package remains licensed under Apache 2.0, while **certain optional components, such as the Unsloth Studio UI**"* are AGPL. **The CLI and the Studio backend are not optional components; they are in the wheel.** 3,164 AGPL-tagged files total (2,693 in `studio/`); two core modules carry an AGPL tag paired with the 2023 core copyright line (a template slip, incl. the weight-loading path `_uma_safetensors.py`); **no CI job enforces any header.**

**⚠️ NOT concealment** — disclosed in README, both licence texts at root, GitHub's sidebar shows *"Apache-2.0, AGPL-3.0"*, and v23 recorded the arrangement. **NOT a legal conclusion** — that needs a lawyer and depends on what a downstream user imports and whether they serve it over a network. **The sufficient claim is narrower: the README's boundary does not describe the wheel's contents.**

⭐ **Against v244 this is a matched pair.** OpenSandbox had a licence gate and used it to **over-assert** an identity its governance doc never named; Unsloth has no gate and **under-asserts** one its packaging enforces anyway. Both repos' prose disagrees with their packaging, and in both the *enforced artifact* is the truthful one — there `verify-license.yml`, here `packages.find`.

**⇒ hireui: read-and-borrow only.** The v214 / v188 / v243 AGPL precedent. Nothing worth taking here requires importing the package.

### ⭐ 7. Best security posture in the corpus, and the triad needs a fix → **D33**

| leg | verdict | evidence |
|---|---|---|
| bind | ✅ **`127.0.0.1` default** | `studio.py:1709`, `:2268` |
| auth | ✅ **real + mandatory** | `routes/auth.py` (30 KB): password + JWT + refresh, forced default-admin change, API keys, **per-IP and per-user lockout** |
| CORS | ⚠️ **`["*"]` default** | `utils/host_policy.py:50-56` |

Plus `--secure` **forcing** loopback so the raw port is never public (`run.py:2258-2266`), remote access only via authenticated Cloudflare tunnel, and stdio-MCP defaulted on **only** at loopback — with Colab excluded because *"even its loopback is a hosted VM reachable through Colab's proxy."*

**⇒ D33: the broken-auth triad is not additive.** The CORS leg's severity is set by the **token transport** — and `grep set_cookie` across the backend returns **nothing**; the session is a header-borne `Authorization: Bearer` (`HTTPBearer`). A browser does not attach that cross-origin unprompted, so what was critical in v231/v232 is minor here — because of a decision the triad does not mention. **Ask how the token travels before weighting leg 3.** ⚠️ **NOT VERIFIED:** whether the frontend persists the JWT in `localStorage` (which would make XSS the real vector).

⭐ And the calibre of the work: `max_age = 60` on the CORS preflight cache, justified by *"**Measured in WebKit**: with Starlette's 600s default, a state-changing request still REACHED the server after remote access was stopped."* They found a browser-specific gap in their own kill switch and closed it.

**Supply chain — new corpus high-water mark, displacing pi v228.** `studio/frontend/.npmrc`: `min-release-age=7` (**N=2** on the technique, pi had 2), `save-exact`, pinned registry, `audit-level=high`, *"use `npm ci` (never `npm install`)"*, **zero npm lifecycle scripts** in all three `package.json`. ⭐ **And it documents its own defeat condition:** *"this does NOT block an ambient `NPM_CONFIG_REGISTRY` … **That is exactly why Unsloth does not read `NPM_CONFIG_REGISTRY`**."* **The best security comment states what its control does not cover.** `dependabot.yml` committed and reasoned to the same standard. **D28 does not apply — they have both the config and the checks** (codeql, semgrep, pip-audit, trivy, scorecard, snyk, npm audit across 41 workflows, 35 on `pull_request`).

### ⭐ 8. Three git roots → **D19 extended**

`1e2ba1b1d` (2023-11-30, Daniel Han, the library) · `42490cfbc` (**2025-12-10, Dan Saunders, "train CLI"**, 43 commits) · `b5aa137b7` (**2026-01-27, Roland Tannous, "first commit"**, the studio skeleton) — **all three ancestors of HEAD**, plus a *"Restore non-studio files from main after history recovery"* commit (2026-03-12). **⇒ Count the roots and date each one: a graft hides a young project inside an old repository's age.** "Since 2023" is true of 4.3% of this tree; 76% of it is ~6.5 months old.

### 9. Provenance — and a 100× trap

**46 Claude-trailered commits / 137 trailer LINES on `HEAD`** (121 commits `--all`). Mean **2.98** — sitting neatly between v244's 1.73 (merge-dominant) and v243's 5.48 (squash-dominant), which is exactly this repo's mixed strategy (570 merges, 3,267 `(#NNNN)`). **⇒ D26 confirmed at a third point.** Census: **Opus 4.8 = 91**, 4.6 = 17, Fable 5 = 9, 4.7 = 6, 4.5 = 6, Sonnet 4.6 = 3, Sonnet 5 = 2, Sonnet 4.5 = 1 — ~98.5% versioned. ⚠️ Both capitalisations are used; a case-sensitive grep under-counts ~25%.

🔴 **The trap fires in both directions, and I took both.** *Over-count:* a body grep returns `openai` 829, `gemini` 546, `codex` 390, `Cline` 191 — **all file paths and feature names**, because the repo *is about* AI tools. *Under-count (mine):* having dodged that, I grepped the **key** form (`Made-with: X`) and reported 1. Enumerating `Co-Authored-By` **values** gives **104 non-Claude AI trailer lines on `HEAD`**: **`gemini-code-assist[bot]` 86** (Google's PR-review **bot** — the largest AI co-author here, and it *reviews*, it doesn't author), Cursor 12, Copilot 4, Codex 2. ⭐ Two of the Copilot lines are **`Copilot Autofix powered by AI <…github-advanced-security[bot]>`** — **v244's D28 detector firing again**, proving GitHub Advanced Security scanning runs on top of the committed workflows. For scale, `pre-commit-ci[bot]` carries **1,309** co-author lines. **⇒ The rule needs both halves: check the key form AND the value form.**

**298 authors**; Daniel Han 4,204 (~56%); **oobabooga 151**, all `Studio:`-prefixed, since 2026-05-26.

### ⭐⭐ 9b. The tag list dates the identity shift — and my first reading was wrong

I published "79 tags, all `v0.1.NNN-beta`, no non-beta tag ever." **False: 26 of 79 are non-beta.** Cause: **`git tag | tail -20` sorts lexically, not by date.** The corrected shape is a far better finding:

| era | dates | tags | convention |
|---|---|---|---|
| **library** | 2024-07-03 → 2026-03-17 | **24** | `July-2024`, `July-Mistral-2024`, `2025-02-v2` … `March-2026` — **month/model milestones, not versions** |
| **product** | **2026-03-20** → 2026-08-14 | **53** | `v0.1.0-beta` … `v0.1.800-beta` + `desktop-v0.1.52x-beta` |

**`v0.1.0-beta` was cut 2026-03-20 — eleven days after AGPL landed on `studio/` and three days after `cli/`→`unsloth_cli/`.** A library tags months; a product that ships installers needs version numbers. **The versioning scheme changed because the artifact did, and the tag list records the date.** Rate: 24 tags in 20 months → **53 in 5 months**, including **8 in five days** (08-10→08-14). And **two schemes now coexist, one per identity:** `_version.py` (*"the single source of truth"*) says **`2026.8.18`** — calendar versioning — while the app is `v0.1.800-beta`. **The claim that survives: the product line has never left beta**, on a 73.7k★ project shipping signed installers.

### 10. Doc defects found by hand, and one non-defect

🔴 **The README's agent table lists five agents; the code and CI support six.** Pi is contract-checked in CI, ships in `package-data`, and has its own test — and appears nowhere in `README.md:106-110`. Prose-vs-code drift in the exact feature that is this ship's headline. 🔴 **A duplicated bullet:** `README.md:78` and `:80` carry the same sentence under *"Search & RAG:"* and *"Search:"*.

✅ **The non-defect.** 2,897 headers point at `/studio/LICENSE.AGPL-3.0`; I went looking for v240's dead-link case and **the file exists**. **D29 cuts both ways — test the claim you *want* to be true, too.**

---

## The mint

**⭐ ONE new §C standalone, N=1: "Self-Hosted / Locally-Trained Model Registered as a Delegatable Subagent Inside a Frontier Coding-Agent Harness."** §C live standalones **50 → 51**; surface ≈57 → ≈58. **Counts 46/11 unchanged.**

**Grounds:** the corpus holds only the opposite arrow (v235: Claude Code as a subagent *of* a runtime, with the delegation axis logged DEFERRED). v171 devspace bridges a hosted host down to a machine — a different object (the whole agent, not a delegate). No §C row describes downward delegation from a frontier harness into a self-hosted model. Unsloth ships it three ways with a separately-tested read-only plan variant: implemented, not gestured at. **Capability, not domain.**

**⚠️ NO-MINT alternative RECORDED and non-trivial (audit-reviewable):** (i) this is a *direction* on an axis v235 opened — the disciplined move may be to restate that axis mechanism-agnostically and call this its **N=2**; (ii) drawn one notch wider it would be born stale at N≈6 (claude-code-router, LiteLLM, **cc-switch v73**, opencode-antigravity-auth **v67**, the GLM/Kimi vendor guides). **I drew the boundary at delegation, deliberately excluding redirection — and that boundary is what an audit should test.** Corpus-first for the surface; **world-first NOT established.**

**NOT minted:** the six-harness connect layer (decisive prior art; cc-switch v73 is already the corpus's harness-endpoint switcher) · the desktop train+run GUI (**textgen/text-generation-webui has shipped a QLoRA Training tab since 2023 and now calls itself "an open-source desktop app for local LLMs… OpenAI/Anthropic-compatible API" — and its author has 151 commits here**; domain-not-capability anyway) · training-infrastructure framework (Pattern #41 CONFIRMED since v23) · executable-documentation CI (a technique, not a capability class — the v238 discipline; recorded as a **DEFERRED watch axis**).

### ⭐⭐ The collision the mint discussion walks past: Studio is **v192 N=5**

The **v192 palmier-pro standalone — *"Product-First Native Application Retrofitted with a First-Party MCP Server"*** stands at **N=4**, all non-port (v192 → tabularis v212 → voicebox v229 → worldmonitor v230), promotion **awaiting an audit** and the trigger already *"doubly reinforced"* at v230. **Unsloth Studio satisfies every clause:** product-first (*"the first desktop app to run and train models"* — its own first line) · native (Tauri v2, 34 `.rs`, signed installers on four platforms) · **retrofitted** (MCP is opt-in and later: `UNSLOTH_STUDIO_ENABLE_MCP=1` + mandatory token, off by default) · first-party MCP server (11 tools incl. `start_training`, `stop_training`, `load_checkpoint`, `export_gguf`).

**⇒ RECORDED: v192 goes N=4 → N=5, non-port, cross-domain. No new row.** ⚠️ **The third consecutive ship to reinforce a promotion no audit has executed** (v229 N=3, v230 N=4, v245 N=5) — and the corpus's only §C→CONFIRMED promotion to date happened at **N=4**. Flagged, not self-executed (v232 rule), but **the audit is now declining at N=5 what it once granted at N=4.**

*(Two artifacts, two findings, no conflict: Studio is v192 N=5; `--as-subagent` is the new mint.)*

**Other pattern touches, flagged not executed:**
- 🔴 **#45 Dual-Licensing — CONFIRMED at v60, but sub-variant 45a is STALE AS WRITTEN.** 45a reads *"Apache core + AGPL UI"*; the AGPL side is now 76% of the tree and in the wheel's default package list. ⭐ **The irony is exact: the vault celebrates #45's promotion as a "35-wiki stale-then-un-stale corpus-record" proving stale-tracking works — and the anchor that validated the machinery has itself gone stale.**
- 🔴 **#46 Duo-Founder — still a CANDIDATE at N=1, and its only anchor is this subject, 222 wikis on.** No N=2 in v24→v244. **A candidate whose sole anchor has now been revisited without yielding a second instance is a retire candidate, not a live hypothesis.** (The revisit does *not* create N=2 — same subject.)
- **#66** — `min-release-age` at **N=2**; Unsloth displaces pi v228 as the strongest supply-chain exemplar.
- **#18 B1-MCP** +1 (two distinct MCP surfaces). **#83** — the `UNWIRED` dict (a disabled `grpo` leg carrying its own verbatim CUDA error, reproduction rate and re-wiring condition) is the strongest honest-deficiency instance recorded.
- **#57** — unusually dense: Pi v36/v228 (v228's own scope-migration finding quoted in Unsloth's CI), cc-switch v73, opencode v67, hermes v227, GLM-5 v176 (which listed Unsloth as a *deploy path* — that dependency ran the other way), and the v23 anchor itself.

---

## New rules

| rule | statement |
|---|---|
| ⭐⭐ **D31** | A **scope verdict is a claim about a date**, not a property of a subject. OUTSIDE-SCOPE closes the file, so it rots unobserved. Detector: the description field and the directory shares. **Work-list:** the population is enumerable — v8 build-your-own-x, v20 fish-speech, v21 system-prompts-leaks, **v22 LlamaFactory**, v23 Unsloth (crossed). ⭐ **Re-check LLaMA-Factory v22 first** — same domain, same era, same ruling, Pattern #41's co-anchor. One WebFetch. |
| ⭐⭐ **D32** | When two documents must carry the same fact and mechanisation is impractical, **declare which copy wins, inside the copy that loses.** One sentence; no tooling; turns a silent contradiction into a resolved one. **⭐ And it is PROVEN, by its own author's file:** `BUDGET.md` teaches `--percent 40 / 40 GPU-h`; the workflow runs **`--percent 15 / 15 GPU-h`** (`:78`, `:129`, `:368`) because a second GPU consumer appeared and the allowance was re-split (`:136-137`). **The declaration did not prevent the drift — it made the drift harmless and self-diagnosing.** Set against **v243**, which had the doctrine, no precedence line, and a plan file that misled for eight weeks: same failure, opposite outcome, one sentence of difference. |
| ⭐ **D33** | **The broken-auth triad is not additive.** Wildcard-CORS severity is set by token transport (cookie = critical, header-borne bearer = minor). Ask how the token travels first. |
| ⭐ **D19 ext** | **Count the roots.** A single-root provenance check misses a graft. |
| ⭐ **D26** | Confirmed at a third point: 1.73 merge-dominant → **2.98 mixed** → 5.48 squash-dominant. |
| ⭐ **D29** | **Cuts both ways** — test the claim you want to be true; and do not test a claim the subject has withdrawn. |

---

## Error ledger — 13 caught, 10 mine

**Withdrawn / corrected:** "the AGPL header pointer is a dead link" (the file exists) · "Unsloth conceals its licensing" (fully disclosed — **exonerating**) · "auth may fail open / CORS is critical" (loopback default, real auth, no cookies — **downgraded, and the downgrade produced D33**) · **"80 of 95 core files carry no licence header"** (**56 carry the Apache *prose* header**; "zero Apache *SPDX*" was a true statement about **notation** masquerading as a finding about **substance** — and the finding got *stronger* by moving onto `packages.find`) · **"79 tags, all beta, no non-beta ever"** (**26 are non-beta**; `git tag | tail` sorts **lexically** — corrected reading became finding 9b) · **"non-Claude trailers = 1"** (**104**; I checked the key form, not the value form) · "3,164 AGPL files" (**3,162 files / 3,164 occurrences**) · "~2,700 AGPL files reach the wheel" (**~2,110** — `exclude-package-data` drops 622) · "LlamaFactory is v37" (**v22**) · "`run.py:214` sets the bind default" (a display-IP fallback) · "test the '500+ models' claim" (**withdrawn from the README** — the mirror of D29's error). Method: case-sensitive trailer grep (−25%); body-grep AI counts (100× over).

**⚠️ The pattern is worth more than the individual fixes.** Errors 10–13 are **all counting-method errors, not reading errors** — lexical sort read as recency, key-form grep read as all trailers, occurrences read as files, tree read as wheel. The vault already carries **D26** and **D27** for exactly this family, and I made four of them in one ship anyway. The fleet's adversarial stage caught three of them; I caught the rest. **That is the case for the verify stage in one sentence: the errors it finds are in the commands, not the prose, so re-reading your own draft will never surface them.**

---

## Non-claims

NOT world-first as a desktop train+run app · **NOT Pattern #52** (stars page-stated, §37.4; the 62,218 → ~73.7k / 121-day delta is page-stated-to-page-stated, not verified velocity) · do **NOT** cite "137 Claude commits" (46 commits / 137 lines, `HEAD`) · do **NOT** claim `CLAUDE_CODE_ATTRIBUTION_HEADER=0` cuts an Anthropic bill, or repeat "~90% slower" as an API figure · do **NOT** claim Unsloth re-exposes a Claude subscription — **it unsets the credential** · **NOT resolved:** whether Studio's `/v1` endpoints can be backed by a connected ChatGPT/Codex subscription, which would make it a **v207-class gateway** (`inference.py:16699` says `/v1/models` exposes *"one per loaded **local** backend"*, which points against it — **flagged, not concluded**) · **NOT VERIFIED:** JWT storage location; whether the wheel's AGPL contents create a real obligation downstream; whether Dan Saunders' root was an acquisition, a hire or a contribution; whether Unsloth employs oobabooga; the generated-vs-hand-written split of the 24,449-line `inference.py`.

---

## Pilot

⚠️ **READ-AND-BORROW — not a hireui component** (§6). **M1 → M2 → M3 in one sitting: ~30 minutes, three edits, zero installs.**

1. **M1** — unset `ANTHROPIC_API_KEY` / `CLAUDE_CODE_OAUTH_TOKEN` in any script that repoints an agent. Two lines.
2. **M2** — `claude -p /context` in the vault root, then diff against `--tools "Bash,Read,Edit,Write,Grep"`. **The first real measurement of the vault's own ~54K prompt floor**, which v167 established and v238 asked for.
3. **M3** — apply **D32** to `_state/03c-projects-v61-v183.md`: one header line naming the entries authoritative and the filename stale. **Four ships have diagnosed this; one sentence resolves it today.**
4. Then **M5** — make `verify-vault-docs` a *generator*, not a linter.

🔴 Never point it at candidate data (the RATIFIED candidate-LLM-legibility ADR) · never `-H 0.0.0.0` without `--secure` · never meter a routed Claude Code with `cache_read_input_tokens` (hardcoded 0 on the Anthropic path).

---

## Blunt

**A fine-tuning library became an agent host in ninety days and the corpus only found out because someone asked for a wiki.** v23 filed it OUTSIDE-SCOPE with "Direct adoption: NONE" — a defensible reading of a training framework in April. By July it was writing Claude Code plugins. Nothing in our criteria changed; the file was simply closed, and a closed file does not get re-read. That is the finding, and it is about us: **the one verdict that ends the conversation is the one that most needs an expiry date.**

What they built is genuinely good, and better than the corpus's usual band. They point Claude Code at a local model and **delete your Anthropic key on the way** — after four ships in a row whose whole business model was harvesting exactly that credential. They refuse to set `IS_SANDBOX` on your machine because it would be a lie, then set it in CI where it isn't. They found an undocumented Claude Code default that moves the system-prompt prefix every turn and kills the KV cache, fixed it, and then wrote a CI test that **fails if the unfixed version stops failing** — and two other projects, one of them our own v73, found the same thing independently. Their `.npmrc` documents its own defeat condition. Their CORS preflight window is 60 seconds because someone measured WebKit still landing a state-changing request after the kill switch was pulled.

And the most valuable thing in 1.75 million lines is one sentence in a file about Kaggle GPU quotas: *"If the two ever disagree, the workflow is right and this file is stale; fix this file."* We have spent eleven ships collecting machinery for a problem that a sentence solves. `_state/03c-projects-v61-v183.md` has been lying about its own contents for sixty-two versions. v239 found the defect, v240 built the check, v242 named the rule, v243 shipped the symlink, v244 handed us a third instance — and the file is still called `-v183`, because every proposed fix was a project. **Unsloth's fix is not a project. It is a line of prose that tells the reader which of two disagreeing things to believe, written into the one that's wrong.** Do that one today, and keep the rename on the list.

The catch is boring and real: the licence. `pip install unsloth` ships a uniformly AGPL CLI inside a wheel stamped Apache-2.0, and the README calls the AGPL side "certain optional components." Nobody is hiding anything — it's in the sidebar, and v23 wrote it down in April — but the sentence people will rely on is not the sentence the packaging supports. So: take the five ideas, install none of it, and note that the two best-engineered repositories this corpus has read back-to-back both ended up with prose that disagrees with their build. In both, the build was the honest one.

---

*Claude Opus 5 for Storm Bear, 2026-08-19. Twice-cloned at `cabed07f`. v23 anchor preserved at `03 Projects/Unsloth - Beginner Analysis/`. Companions: `(C) Unsloth v245 — Deep Dive.md`, `(C) Unsloth v245 — Pilot Methods Menu.md`.*
