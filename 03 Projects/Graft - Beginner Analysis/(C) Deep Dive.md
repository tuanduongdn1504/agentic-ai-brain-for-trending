# (C) Graft — Deep Dive

**Subject:** `NanoNets/Graft` — npm `@nanonets/graft` v0.13.0 — MIT
**Ship:** v275 · 2026-08-25 · GOAL-ALIGNED INCLUDE 3/4 · NO MINT
**Source verification:** two independent clones, `diff -rq` clean **both directions** (only `.git/` index + reflogs differ). HEAD **`ee1ef03538c4e94b1a8552b13984b9fc2992dd29`**.

---

## What it is

> *"Build a repo's context graph as a folder of linked markdown files: a local, regenerable cache that every query keeps in sync with your code."* — `package.json:4`

Graft reads your repository once, has an LLM write a **wiki of it**, and leaves that wiki on disk as plain markdown for your coding agent to read instead of re-exploring the codebase every session. It ships six CLI verbs (`ask` / `grep` / `skeleton` / `callers` / `map` / `check`), a six-tool MCP server, and a `graft init` that wires itself into Claude Code, Cursor, Codex, Gemini CLI, Antigravity, Kiro, Grok and OpenCode.

The on-disk format is stated in the code, not just the README — `src/context/node-file.ts:1-5`:

> *"The files ARE the graph — the frontmatter carries the machine-readable node (identity, source provenance, edges) and the body is human/agent-readable prose. **There is no database.**"*

And it emits **`[[wikilinks]]`** (`src/context/node-file.ts:188`, `src/graph/cards.ts:82`) — Obsidian syntax. Each node keeps a `<!-- context:generated:start/end -->` region that is rewritten on every build, and **everything a human writes below it is preserved verbatim.**

⭐ **This is the vault's own founding pattern, automated, in the vault's own file format** — the fourth third-party productisation of it in recent memory (v252 context-os · v268 `lat.md` · v269 OpenViking's `llm-wiki` skill · v275 Graft), and the closest yet: this vault is a hand-curated LLM wiki of a knowledge domain in Obsidian; Graft is a generated LLM wiki of a codebase in the same syntax.

---

## Measured facts (all `rev-list`-derived — D39)

| Fact | Value |
|---|---|
| Commits | **402** on `main`; 554 all refs |
| Root commits | **1** — `33e6d6bc`, 2026-07-03, *"Initial commit: Context Graph Engine"* |
| Merges | 45 (28 say "pull request") |
| Tags | **6** — `v0.7.1 v0.8.1 v0.8.2 v0.9.0 v0.12.1 v0.13.0` |
| Tracked files | 267 |
| Age | 2026-07-03 → 2026-08-24 = **52 days** (243 commits in July, 159 in August) |
| Authors | **28 distinct emails** |
| TypeScript | 209 files / **41,918 lines** |
| `src/**.ts` | 106 files / 21,948 lines |
| `test/` | 96 `.test.ts` files / 19,006 lines — **test-to-code 0.87** |
| Test cases | **904** `test(`/`it(` · **2,858** `assert.` calls |
| Workflows | 6 — every action SHA-pinned, `permissions: contents: read`, `persist-credentials: false` |

**Author split:** `dwi.shrish@gmail.com` 190 · `anirudhkumar@nanonets.com` 108 · `shhdwi` 24 · `qoole` (Alex Matthews) 24 · dependabot 13 · `Frankie-Xu` 8 · `shrish@nanonets.com` 3 · **`noreply@anthropic.com` 2**. Shrish Dwivedi across three identities = **217 of 402 (54%)**. NanoNets-domain commits = 111.

⚠️ **Sandbox correction (§43.1):** I first recorded "7 days old / 50 commits" from `git log`. `git log` truncates at 50 here (SIGPIPE — the v267 quirk). Every count above comes from `git rev-list` or a dumped file. **This is the second consecutive ship where the same quirk produced a wrong headline number, and re-measurement caught it, not re-reading.**

---

## ⭐⭐⭐⭐⭐ THE HEADLINE: the correction existed, was right, and was reverted

`README.md:20`, the largest text under the product name:

> `### Up to **4× cheaper** and **3× faster**, with better or no loss of correctness.`

That sentence is sourced to `## Tested on your popular repos` (README:504-558), whose prose is **plural throughout** — *"popular open-source repos"*, *"**Across these repos** graft runs up to 4× cheaper and 3× faster"*, *"**Per-repo detail below.**"*

**It contains exactly one repository.** Verified: `awk 'NR>500 && /^#+ /' README.md` returns only lines **504** (the section), **510** (`### PocketBase (Go, ~350 files)`), **560** (`## Development`), **573** (`## License`).

PocketBase's own aggregate table:

| | Standard Claude Code | With graft |
|---|---|---|
| Cost | $13.91 | $11.02 **(−21%)** |
| Wall-clock | 2,044s | 1,762s **(−14%)** |

**−21% and −14% are 1.27× and 1.16×.** The best single figure disclosed anywhere in the README is one task going $2.19 → $0.84 = **2.6×**. Nothing in 575 lines reaches 4× or 3×.

### The commit chain

| Commit | Date | Author | What |
|---|---|---|---|
| `94a5d80` | 2026-07-24 | Shrish Dwivedi | Added the hero headline **and** a footnote: *"The 'up to 4× cheaper / 3× faster' figures are the biggest single-task wins from a separate real-repo sweep (**PocketBase, ollama, Excalidraw**)."* |
| `630cd1d` | 2026-08-11 | **`Claude <noreply@anthropic.com>`** (Co-Authored-By Claude Sonnet 5, carries a `Claude-Session:` URL) | Changed the headline to **2×/2.5×** and **deleted that footnote**. Message: *"'4x cheaper / 3x faster' was sourced from a separate real-repo sweep, not the 162-run table directly beneath it (46%/42%/60% savings ≈ 1.8x-2.5x), so the headline **overstated what the adjacent table showed**."* |
| `35ac2ae` | 2026-08-12 | Shrish Dwivedi | *"docs: revert hero headline to 'up to 4x cheaper, 3x faster'"* — **one line, no rationale.** Restored **only the headline.** |

⭐⭐⭐ **At HEAD the strong claim stands and its attribution footnote does not.** `README.md:29` contains no "biggest single-task wins" sentence — I checked. **Neither party authored the current state:** the AI's correction removed the disclosure, the human's revert restored the claim, and the composition is a stronger claim with weaker sourcing than either commit produced on its own.

⭐⭐ **And the sweep was never published.** I scanned **all 402 commits**: a `### Excalidraw` or `### ollama` heading has **never existed** (0/402). The string "Excalidraw" appears in exactly **two** commits — the one that added the footnote and the one that deleted it. The three-repo sweep that justifies the headline exists nowhere in this repository in any form, and the plural language in the section is a fossil of it.

---

## The rest of the claim audit — and it is mostly good

**No benchmark artifacts exist.** `git ls-files | grep -iE "bench|swe|eval|result"` is **empty**. `git grep -il "swe-bench"` returns **README.md only**. The 162-run sweep and the SWE-bench Verified result have no harness, no data, no transcripts in-tree.

But the **detail sections are markedly more disciplined than the hero**, and that must be said plainly:

- The SWE-bench section states **"50 instances"** in its own body, names the model (Claude Sonnet 5), the grader (**official `swebench` 4.1.0**, native x86_64), and both arms' configuration.
- It declares its own subsetting: *"tokens, cost and calls over the instances **both arms resolved**, for a like-for-like comparison."*
- It **names the self-measurement problem out loud**: *"The sweep above is our harness measuring our mechanism. So we ran the industry-standard one too."*
- It **reports a null result against itself**: in the 162-run sweep, correctness is **93% vs 93% (equal)**.
- The cost model is cache-aware (reads ≈0.1×, writes 1.25×) — the real billing shape.
- The PocketBase method block discloses that both arms were verified graft-free/graft-used by transcript audit.

⇒ **The composite hero table is the problem, not the research.** It takes the efficiency rows (+46% / +42% / +60%) from the experiment where **correctness was flat**, and the correctness row (54% → 66%) from the experiment whose efficiency numbers were roughly half as good (+25% / +23% / +32%). The footnote does say which is which. The table does not.

### Claims that check out

| Claim | Verdict |
|---|---|
| *"~3ms"* freshness probe | ✅ `src/graph/fingerprint.ts:6` — *"**Measured at ~3ms for 280 files.**"* A stated measurement with its population. |
| *"every query rebuilds the graph against the working tree first"* | ✅ `src/graph/refresh.ts` + `fingerprint.ts` — stat-only, no LLM, no key. |
| *"`graft init` … never clobbers your existing `.claude/settings.json`"* | ✅ `src/claude/settings-merge.ts:30,33` — spreads existing, drops old graft entries → idempotent; refuses to overwrite an existing `statusLine` and warns instead. |
| 17 README table-of-contents anchors | ✅ **17/17 resolve.** |
| *"on this repo, 124 files: 0.74s cold, 0.18s after one edited file"* | ⚠️ Appears in `README:180` and `CHANGELOG:344` and **nowhere else in 267 tracked files.** A one-off measurement, never re-run. |
| *"~10× cheaper than reading the file"* (skeleton) | ⚠️ A comment at `src/claude/format.ts:45`; no benchmark. |

**The `[graft] tokens saved ≈ N` figure** is `Math.round(chars / 4)` — in **three** places (`src/context/savings.ts:26`, `src/ask/ask.ts:954`, `src/claude/format.ts:86`). It is honestly labelled at every layer: `≈` in the user-facing string, `(est.)` at `src/claude/state.ts:30`, *"estimate"* in the docblock. Fair — you cannot measure the road not taken. ⭐ But note the shape: the SKILL instructs the agent to report this number to the user **every turn**, a statusline aggregates it by **regex-scraping the tool's own output** (`src/claude/hooks.ts:241`), and the SKILL therefore forbids the agent from piping graft through `head`/`tail` because that *"silently drops the savings line the statusline's running total is parsed from."* **A vendor-computed benefit metric, surfaced inside the product's own output, that breaks if the consumer reformats it.**

---

## ⭐⭐⭐⭐ The telemetry contract: an exceptional mechanism, an ungated document

`TELEMETRY.md:8-13` makes an unusually strong, explicitly falsifiable promise:

> *"This document is the complete, authoritative contract: **if an event or property is not listed here, graft does not send it.** … enforces this list as a hard allowlist … **The code and this file are kept in lockstep**, and because the repo is open source you can verify that yourself."*

**So I verified it.**

**The mechanism is the best-tested privacy surface in this corpus.** `test/telemetry-contract.test.ts` (171 lines) and its siblings assert, among other things:
- An unlisted event is dropped whole; an unlisted **property** is dropped while the event survives.
- Fed a realistic payload `/Users/someone/secret/repo/src/auth.ts`, it asserts **`'path' in ev.properties === false`** *and* **`JSON.stringify(ev).includes('secret') === false`** — a negative control against actual exfiltration.
- A raw number under a legal key is dropped (`files_bucket: 4127` → gone) — every count is bucketed so it cannot fingerprint a repo.
- Prototype keys (`constructor`, `__proto__`, `toString`, …) are rejected as both event names and property names.
- `langsValue` drops anything that isn't a plain language token — including `'src/secret project/auth.ts'` and `'../../etc/passwd'`.
- `errorCode` maps to a fixed enum and **never returns the message**, tested with an error string containing a private path.

**⭐ I ran it.** `npx tsx --test` over the telemetry + settings-merge + shim-template + savings suites: **55 tests, 55 pass, 0 fail, 115ms.** It honours **`DO_NOT_TRACK`** and never notices in CI (*"CI gets no notice — there is no one there to read a disclosure"*). Telemetry is **opt-out, on by default** — established by an executed test literally named *"never chosen means on — the documented default."*

**🔴 But nothing reads `TELEMETRY.md`.** A full-extent grep for `TELEMETRY.md` across every `.ts`/`.mjs`/`.cjs`/`.yml` in the tree returns **seven hits: five comments, one user-facing string, one URL.** Zero reads. The test that pins the event set does it against **a list typed a third time inside the test file**:

```js
assert.deepEqual(Object.keys(EVENTS).sort(), [
  'build_completed','build_failed','first_run','init_completed','query','session_summary' ]);
```

And `src/telemetry/contract.ts:3-5` states the rule as an instruction to a **human**: *"one that is not in `TELEMETRY.md` **must not be added** here."*

⇒ **Three copies of the event list — the published document, the code, and the test — and the gate pins copy 2 against copy 3. The document users are told is authoritative is the one copy nothing checks.** They agree today; I verified all three list the same six events. It is held by attention, exactly as v274 predicted.

⭐⭐ **And the sharpest part: this codebase demonstrably knows how to assert on markdown.** `test/hosts-init.test.ts:31` asserts `GEMINI.md` includes `'graft ask'`; `covers.test.ts`, `graph-posix-paths.test.ts` and `context.test.ts` all read generated `.md` files. **The capability is aimed at every markdown file graft *writes*, and at none of the markdown files graft *publishes about itself*.** That is v250's rule — *a gate's aim, not its quality, decides what rots* — reached independently.

---

## ⭐⭐⭐ The `pull_request_target` workflow: the invariant is stated AND obeyed

`blast-pages.yml` publishes a per-PR interactive viewer to GitHub Pages under **`pull_request_target`** with **`contents: write` + `pull-requests: write`** — the highest-risk pattern in GitHub Actions. Its header (lines 6-13):

> *"`pull_request_target`, not `pull_request`, because publishing needs write access … **That choice carries the standard hazard: this workflow runs with the BASE repo's permissions while the PR's code is attacker-controlled on a fork.** So it checks out the base ref for the tooling, builds the CLI from the BASE commit, and **only ever reads the PR's files as data — never runs a script from the PR (no `npm ci` on the PR's package.json, no postinstall).**"*

**D34 test — I checked the predicate against what the file actually does:**

- `:64-67` checkout → `path: base`, **no `ref:`** (so the base ref), `persist-credentials: false` ✅
- `:73-75` **the only `npm` invocation in the file**: `working-directory: base` / `npm ci && npm run build` ✅
- `:84-90` checkout → `ref: refs/pull/N/merge`, `path: pr`, `persist-credentials: false`, `allow-unsafe-pr-checkout: true` ✅
- `:103-104` the graph build runs with `working-directory: pr` — but the binary it runs was built in `base` ✅

**The invariant holds absolutely.** ⭐ And `:79-83` carries the best sentence in the file — the `allow-unsafe-pr-checkout` flag *"refuses a fork's PR ref … unless the workflow opts in — **the review that opt-in asks for is the header of this file**."* The author treats a required override flag as a forcing function for a written security review, and then points at the review. **This is a direct cross-author N=2 of v273's finding** one ship later, in an unrelated codebase.

**Zero `paths:` filters across all six workflows** — so unlike v271, the gate's *scope* is right. CI simply has nothing to say about the README, because no test reads it.

---

## Where it does not hold

**🔴 1 — The rename is unfinished in 7 places / 5 files.** `NanoNets/context-graph-engine` → `NanoNets/Graft`:

| Location | Why it matters |
|---|---|
| `package.json:17,19,21` | `repository` / `homepage` / `bugs` |
| `README.md:563` | **the literal `git clone` command under `## Development`** — the first thing a contributor runs |
| `src/telemetry/notice.ts:22` | `TELEMETRY_DOC_URL` — **the privacy-policy link shown to users** |
| `.claude/helpers/graft-hooks.cjs:7`, `graft-statusline.cjs:7` | `BAKED = "/Users/shrishdwivedi/Documents/Context graphs/context-graph-engine/dist/claude"` |

⭐ **That last one is more interesting than it first looks.** `src/claude/shim-template.ts` shows the `.cjs` helpers are **generated by `graft init`** with the local package path baked in, and they resolve through four candidates so a stranger's machine falls through harmlessly. The author ran `graft init` in his own repo and committed the result. `.gitignore` explicitly reasons about exactly this line — it ignores `.claude/settings.json` as *"regenerated per machine … never shared"* while stating *"the hook helpers/skills alongside them stay tracked."* **The rule was written, was correct in intent, and its population was typed by hand — and one member was misclassified. The evidence is the author's home directory in a public repository.**

**🔴 2 — Twelve stale `.context/` doc-comments across seven source files**, describing an output directory the product no longer uses (it writes `graft/`). Two are worse than stale — they are **contradictory**:
- `src/context/check.ts:2` — *"is the **committed** `.context/` graph still in sync with the code?"*
- `src/engine.ts:70` — *"Report whether the **committed** `.context/` markdown graph is in sync"*

The product's headline design decision is that the graph is **never committed** (`.gitignore`, the README, and a remote branch literally named `docs/graft-cache-not-committed`). ⭐ The pivot reached the README, the `.gitignore`, the `.ignore`, the SKILL and the CLI. **It did not reach the doc-comments inside the files that implement it** — which is the prose an agent reads when it opens the source, i.e. precisely the thing Graft exists to replace. *(Whether graft's own generated graph would inherit the error is a mechanism I can state but did not measure — building requires an API key and native bindings I could not compile here.)*

**🔴 3 — Raw source goes to your LLM with no secret-scanning.** `src/context/build.ts:181` — `await opts.summarizer.summarize(code, { path: rel })`. A full-extent grep over `src/**/*.ts` for `redact|sanitiz|secret|credential` finds **zero** redaction logic. **Mitigation, and it is a real one:** `src/ingest/fs.ts:60-61` sources the file set from `git ls-files`, so indexing *"gives exactly Git's nested `.gitignore`"* semantics — a gitignored `.env` is never read. But a credential **hardcoded in a tracked source file** is indexed, summarised and sent. `SECURITY.md` is 18 lines and says nothing about what leaves your machine.

**🔴 4 — `graft init` grants four `permissions.allow` entries** (`src/claude/settings-merge.ts:9-14`):
```
'Bash(graft:*)', 'Bash(npx graft:*)', 'Bash(graft-dev:*)', 'Bash(node dist/cli.js:*)'
```
Three are scoped to graft's own CLI. **`Bash(node dist/cli.js:*)` is not** — in *your* repo, `dist/cli.js` is whatever your build produces, now pre-approved to run unprompted with arbitrary arguments. A development convenience leaked into every user's config.

**🔴 5 — Global writes for two hosts.** `graft init` is **project-local for Claude Code** (a real improvement on v273, which wrote your global `~/.claude/settings.json`). But selecting Codex or Antigravity writes **outside the repo**: `~/.codex/hooks.json` (a hook that fires in *every* repo), `~/.codex/config.toml`, `~/.codex/hooks/graft/graft-hooks.cjs`, `~/.gemini/config/mcp_config.json`, `~/.gemini/skills/graft/SKILL.md`. ✅ **The escape hatches exist and are documented**: `--dry-run` (*"print every file init would touch, then exit without writing"*, `cli.ts:838`), `--no-global` (`:840`), `--agents claude` (`:832`).

**🔴 6 — Release bookkeeping drifts.** 6 tags vs 9 CHANGELOG versions: **`v0.7.1` and `v0.12.1` have no CHANGELOG entry**; **`0.12.0`, `0.11.0`, `0.8.0`, `0.7.0`, `0.6.0` have no tag.** No `0.10.x` anywhere.

**🔴 7 — `scripts/graph-quality.mjs` is invoked by nothing.** A 124-line structural invariant checker with `--strict` — dangling edges, span validity, unique ids — described in its own header as *"Tier-0 of the quality strategy."* Extent of search: all of `.github/`, `package.json`, `test/`. **Zero references.** ⭐ v273's rule, reproduced exactly: the checks in `.github/workflows/` run forever; this one lives in `scripts/` and requires someone to remember.

---

## What is genuinely excellent

- **904 test cases / 2,858 assertions** over 41,918 lines, ratio **0.87** — among the densest in the corpus.
- **CI comments that name the failure mode.** `ci.yml:12-18` justifies the Windows leg because a path-separator leak *"matches nothing rather than erroring… it shipped in 0.8.2 and took three user reports to find."* `run-tests.mjs` exists because `node --test test/*.test.ts` under `cmd.exe` meant *"the Windows CI leg reported failure while actually running zero tests"* — **a gate that could not fail, found and fixed.** `shim-template.ts:15-21` documents why resolution takes the **highest version** not the first hit: *"The upgrade appeared to work and changed nothing."*
- **Telemetry that cannot send from a fork by construction** — the PostHog key is stamped only at publish (`stamp-telemetry-key.mjs`), the repo holds an empty string, so *"a clone, a fork, a CI build, and a contributor's local `npm run build` all produce a graft whose telemetry module short-circuits on the very first check."*
- **Supply chain is clean.** All **76** lockfile entries carry sha512 integrity and resolve to **`registry.npmjs.org`** — 100% single registry (the sharp inverse of v271's 206/206 npmmirror). `postinstall` prints one line, exits 0 under CI, and *"never fail an install."* Every CI action SHA-pinned. CodeQL + OpenSSF Scorecard on a schedule.
- **`.ignore`** — *"graft's cards are gitignored but should stay greppable: ripgrep reads `.ignore` before `.gitignore`, so this re-admits the tree to search only."* A small, exactly-right piece of craft.
- ⭐⭐ **`CREDITS.md` credits people whose PRs were *not* merged.** It thanks eight contributors by handle and PR number for language support, then explains that *"that wave of one-language-at-a-time PRs is exactly what motivated the generic breadth tier that now covers most of them"* — i.e. their code was superseded and they are credited for the idea. It closes: *"If you contributed a language PR and aren't listed here, please open an issue — **the omission is an oversight, not a slight**."* I verified five of the credited handles (`@williamdes`, `@kapelner`, `@dbianco`, `@jhouserizer`, `@qoole`) appear as real commit authors. **Set this beside v270**, whose README said *"everyone who has raised an issue, we list them all here"* above four blank lines, against 62 issues.
- **The SKILL.md is the best-written agent skill in the corpus.** It budgets *calls*, not tokens: *"Most tasks need one call."* It says when **not** to use graft (*"Reserve `graft ask` for when you don't yet know where the code lives"*), what to do on failure (*"If a grep misses, **loosen it**… do NOT switch to raw `grep -rn`"*), and a scenario table where nine of twelve rows are "1 call".

---

## Corpus position

**Corpus-first: VERIFIED at full vault extent** (`.git` excluded). `NanoNets` **0** · `nanonets` **0** · `context-graph-engine` **0** · `Shrish` **0** · `graft.nanonets` **0**. The eight `\bgraft\b` markdown hits are all the **git term** — *"a graft hides a young project inside an old repository's age"*, from the vault's own v240/v241/v245 provenance findings. Positive controls fire: `codegraph` 167 · `GitNexus` 259 · `codebase-memory-mcp` 66 · `code-review-graph` 9 · `unlazy` 6.

**NO MINT.** Graft is a clean instance of **CONFIRMED Library-vocab #23** — *"Pre-Indexed Read-Only Code Knowledge-Graph Queried by Coding Agents via MCP"* — taking it from N=5 to **N=6** (graphify v16 · GitNexus v33 · codegraph v70 · codebase-memory-mcp v172 · code-review-graph v226 · **Graft v275**). All six MCP tools are read-only.

⭐ It is however the **first #23 instance whose store is human-readable markdown rather than a database** (SQLite/Cypher/networkx in the prior five). That is a genuine sub-axis and it is **recorded as a DEFERRED watch axis, not minted** — *"agent code-knowledge-graph persisted as an editable linked-markdown wiki rather than a queryable database"* (N=1). Declined on: capability-not-storage-format, §28 (and **not on §28 alone** — §44.5), and the standing discipline that a sub-variant within a CONFIRMED pattern strengthens rather than mints.

**Second DEFERRED watch axis (N=1):** *a documentation claim corrected by an AI collaborator and reverted by the human maintainer, leaving a composite neither authored.*

**Pattern #57:** `.claude/proven-config.json` declares `"schema": "ruflo.proven-config/v1"` and `"compatibility": {"ruflo": ">=3.24.0"}` — `ruflo` is corpus **v42**. ⚠️ **NOT ESTABLISHED as the same project**: `git grep -in ruflo` over all 267 tracked files returns **only those two lines**; there is no dependency, no documentation, no other reference. Recorded as a **candidate** #57 link and an orphan config artifact, not a confirmed one.

**Recorded instance-strengthening (not self-incremented):** **#18** sub-archetype B1-MCP · **#19** 19a (NanoNets is a company, **not** Anthropic — §41) · **#66** supply-chain (a `postinstall`, a `prepare`, native builds).

---

## ⭐⭐⭐⭐⭐ THE SHIP'S RULE

**A check cannot survive someone with standing to overrule it — and a partial correction composed with a partial revert produces a claim neither party wrote.**

Everything in this repository that faces a *maintainer* is gated to an exceptional standard: 904 tests, an allowlist with negative controls against real PII, a `pull_request_target` workflow that names its own hazard and then obeys the invariant absolutely, CI comments that document silent-failure modes by name. Everything that faces a *buyer* — the hero multiplier, the plural section with one repo, the benchmark numbers with no harness — is held by nothing at all. That is not carelessness; the same hands wrote both. It is that **a maintainer is afraid of getting the code wrong and nobody is afraid of getting the pitch wrong.**

And the proof is that **the correction actually happened.** The repository's own AI collaborator read the hero, diagnosed it precisely, and fixed it. A human reverted it the next day in one line with no reason given — and because the revert targeted only the sentence above the footnote, the disclosure the AI had removed stayed removed. **The gate was not missing. It was overruled, and the overruling was free.**

**THE LADDER:** v270 no gate fires on a claim true when written · v271 a gate's scope is inherited from where it lives · v272 a gate holds when something else already requires it · v273 a check is only as permanent as the place you put it · v274 neither a gate nor a habit reaches a claim stored outside the repository · **v275 a check that reaches the claim, is correct, and is applied can still be reverted by someone with the standing to do it.**

---

## Method, and my own errors

**Fleet:** 13 dimensions × (read → adversarially refute) = **26 agents, 0 errors, 0 empty**, 3.15M subagent tokens, 434s. The adversarial layer earned its cost: it caught the tests agent claiming **19 test cases** where the true figure is **904** (a 47× undercount), refuted hallucinated YAML and an invented runner name, refuted a shell-injection finding (`resolveCommand()` is only ever called with entries from a hardcoded `LSP_SERVERS` array), and refuted a path-traversal finding (`skeleton()` does zero file I/O). **D51 at another data point.** I re-verified every load-bearing claim by hand before using it.

**My errors, both caught by re-measurement rather than re-reading (§43.1, second consecutive ship):**
1. **"7 days old / 50 commits"** — read from `git log`, which truncates at 50 in this sandbox. The true figure is **52 days / 402 commits**. The tell was that commits dated 2026-07-24 predated my claimed "first commit."
2. **"Corpus-first, `graft` = 11 files"** — an unanchored substring grep. Word-boundary + context inspection showed all hits are the *git* term.

⚠️ **Extent limits I did not overcome:** `npm ci` fails here because node-gyp requires Python, which this sandbox SIGKILLs. With `--ignore-scripts` the full suite reached **242 pass / 85 fail** before stalling, and **86 of the failures are `No native build was found for platform`** — the environment, not the code. **I did run 55 tests to completion: 55/55 pass.** I did not run `graft build`, so nothing about the generated graph's *quality* is measured here.

---

*Deep dive by Claude (Opus 5) under operator direction. Ship v275, branch `wiki/v275-graft` off the v274 tip (`5678ea0`).*
