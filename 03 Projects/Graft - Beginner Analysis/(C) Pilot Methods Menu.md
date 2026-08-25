# (C) Graft — Pilot Methods Menu

**v275 · `NanoNets/Graft` · MIT · npm `@nanonets/graft` v0.13.0 · pin HEAD `ee1ef035` / tag `v0.13.0`**

**Overall: ⭐⭐ READ-AND-BORROW FIRST, THEN A FENCED INSTALL.** One of the more genuinely pilotable subjects in a long run — MIT, project-local by default for Claude Code, `--dry-run` before it writes anything, and an idempotent settings merge that refuses to clobber an existing `statusLine`. The fences below are specific and small.

---

## 🔴 The four rules, before anything else

1. **Always `graft init --dry-run` first.** `cli.ts:838` — *"print every file init would touch, then exit without writing."* Read the list. Then run it for real.
2. **Always `--agents claude --no-global`.** Without it, selecting Codex or Antigravity writes **outside your repo**: `~/.codex/hooks.json` (a hook that fires in *every* repository you open with Codex), `~/.codex/config.toml`, `~/.codex/hooks/graft/graft-hooks.cjs`, `~/.gemini/config/mcp_config.json`, `~/.gemini/skills/graft/SKILL.md`.
3. **After init, delete `Bash(node dist/cli.js:*)` from `.claude/settings.json` → `permissions.allow`.** graft adds four entries (`settings-merge.ts:9-14`); three are scoped to its own CLI and this one is not. In *your* repo `dist/cli.js` is your build output, now pre-approved to run unprompted with arbitrary arguments.
4. **Never run `graft build --deep` on a repo with credentials in tracked source.** `src/context/build.ts:181` sends raw file contents to your configured LLM. A full-extent grep of `src/**/*.ts` for `redact|sanitiz|secret|credential` finds **zero** redaction. Gitignored files are safe (`src/ingest/fs.ts:60` sources from `git ls-files`); tracked ones are not.

**Never cite** *"up to 4× cheaper and 3× faster"* — its own evidence section measures **1.27× and 1.16×**, and the hero table blends two different experiments.

---

## Rung 0 — Read it. 40 minutes, zero install, highest value.

The method here is worth more than the tool. In this order:

| File | Why |
|---|---|
| `.claude/skills/graft/SKILL.md` | **The best-written agent skill in the corpus.** It budgets *calls* not tokens (*"Most tasks need one call"*), says when **not** to use itself, and tells the agent what to do when a query fails instead of letting it flail. |
| `.github/workflows/blast-pages.yml:1-20, 60-105` | A `pull_request_target` workflow that names its own hazard in the header and then obeys the invariant exactly. **The best CI security reasoning in this corpus.** |
| `test/telemetry-contract.test.ts` (171 lines) | How to test a privacy promise: feed it a realistic secret path and assert the string cannot appear in the serialized payload. |
| `src/claude/shim-template.ts:1-21` | Why resolution takes the **highest version** not the first hit — *"The upgrade appeared to work and changed nothing."* |
| `.github/workflows/ci.yml:12-18` + `scripts/run-tests.mjs:1-14` | Two written diagnoses of **gates that could not fail**. |
| `CREDITS.md` | Crediting contributors whose PRs you did **not** merge. |
| `TELEMETRY.md` + `src/telemetry/contract.ts:1-10` | The contract, and the rule stated as an instruction to a human rather than a check. |

---

## ⭐⭐⭐ Rung 1 — THE VAULT ITEM. 45 minutes. Do this one.

**v273 told you *where* the inventory script must live. v274 told you *what bug* to avoid writing. v275 tells you *where to aim it*.**

`(C) proposed-verify-vault-inventory.sh` is now **twenty ships old and has never run.** Graft supplies the missing aim:

> Graft's tests read `GEMINI.md`, `INDEX.md`, `AGENTS.md`, `.cursor/rules/graft.mdc` and generated cards. The capability is proven. It is pointed at **every markdown file graft writes** and at **no markdown file graft publishes about itself** — including `TELEMETRY.md`, the file it calls *"the complete, authoritative contract."*

**The vault has the identical shape.** Do this:

1. `git mv` the script to `bin/verify-vault-inventory.sh`, drop *"proposed"*.
2. **Put its invocation in the per-ship append** — the one procedure that provably runs every ship (v273's mechanism, proven by the D32 notice bumping five ships running).
3. **Derive every clause's population from the tree, never from a list you type** (v271: sha256 manifest over 84 files · v272: `readdir` recursion · v274 + v275: the counter-examples).

**First four clauses:**
- **(a)** every `_state/` file on disk is named in the `CLAUDE.md` index — derived by `ls`. *(The v256 CLAUSE-1 failure, which recurred in `MEMORY.md` at v271.)*
- **(b)** every relative link and `[[wikilink]]` in `_state/`, `_patterns/`, `_goals/` resolves.
- **(c)** the highest `v###` in `03c` equals the version in the `CLAUDE.md` CURRENT HEAD block. *(Would have caught v274's session-long mis-numbering — and it caught nothing this ship because I checked it by hand instead, which is the point.)*
- **(d) NEW, from v275** — **every number and multiplier asserted in the CURRENT HEAD block appears somewhere in `_state/03c`.** A headline figure with no body to source it is exactly the 4×/3× defect.

---

## ⭐⭐ Rung 2 — Borrow into `CLAUDE.md`. 20 minutes.

Four rules this ship earned:

- **"Three copies of a fact is the smell."** Graft's event list lives in `TELEMETRY.md`, in `contract.ts`, and typed a third time inside the test that pins it — so the gate compares copy 2 to copy 3 and the authoritative copy is unchecked. *(Extends D32: when you must have two copies, declare which wins **and** make the check read the winner.)*
- **"A revert is an unreviewed commit."** `35ac2ae` changed a load-bearing public claim in one line with no rationale, and left a related deletion standing. Require a reason on any commit that changes a claim.
- **"A rule's population is the part that rots, not the rule."** Graft's `.gitignore` reasons correctly about per-machine files and misclassifies one member — the evidence is the author's home directory in a public repo.
- ⭐ **Best sentence to paste verbatim**, from `src/graph/fingerprint.ts:6`: *"**Measured at ~3ms for 280 files.**"* A measurement, its population, in the file that does the work. That is the format every number in the vault's head block should be in.

---

## ⭐ Rung 3 — Fenced install on a scratch repo. 30 minutes.

```bash
npm install -g @nanonets/graft@0.13.0
```

Then, **in a throwaway clone, never in hireui**:

```bash
graft init --dry-run --agents claude --no-global
```

Read every path it prints. Then run it without `--dry-run`, and immediately:

```bash
git diff -- .claude/ .mcp.json
```

Confirm: `.claude/settings.json` merged not replaced, your `statusLine` untouched, four hooks registered, and **remove the `Bash(node dist/cli.js:*)` allow entry**. Run `graft build` (structural tier — **no API key, no model call**) and read `graft/INDEX.md` and one node file by hand. This tier is `$0` and touches no network.

**Run `install-snapshot` first** — there is a `postinstall` (benign: prints one line, exits 0 under CI, *"never fail an install"*) and native tree-sitter builds.

---

## Rung 4 — hireui. 60 minutes. **Read-only tier only.**

Point `graft build` (structural, no `--deep`) at the hireui monorepo and use `graft callers <symbol> --depth all` before touching anything in the Candidate-Detail refactor. That is the **blast-radius** question the standing spike keeps needing, and it is the one graft answers best — precomputed edges, not a text search.

🔴 **Do not run `--deep` on hireui** until you have grepped its tracked source for credentials. The LLM tier sends file contents to your provider with no redaction.
🔴 **Do not wire the MCP server into any agent that touches candidate data** until the RATIFIED candidate-LLM legibility ADR has been applied to it.

---

## Rung 5 — The bake-off worth running

The vault holds **six** instances of this class now (#23 at N=6). You have never piloted any of them. Graft vs **GitNexus v33** vs **codebase-memory-mcp v172** vs **code-review-graph v226**, on the same repo, measuring the same thing: how many tool calls does Claude Code need to answer *"what breaks if I change this signature?"*

Graft's distinguishing bet is that **the store should be readable markdown you can hand-edit** rather than a database — `src/context/node-file.ts:4`, *"There is no database"*, and human-written regions survive every rebuild. That bet is testable in an afternoon, and it is the one axis the other five do not offer.

---

## 🔴 NEVERs

- Never cite **4× / 3×** — measured aggregates are 1.27× / 1.16×.
- Never present the **hero table** as one experiment — the efficiency rows come from the run where correctness was **flat (93% vs 93%)**; the correctness row from a **50-instance** SWE-bench subset with roughly half those efficiency numbers.
- Never quote the **SWE-bench 54%→66%** without saying **50 of 500 instances** — the README's own body says it; the hero does not.
- Never run `graft init` **without `--dry-run`** the first time, or **without `--no-global`** ever.
- Never leave `Bash(node dist/cli.js:*)` in your `permissions.allow`.
- Never `--deep` a repository whose tracked files may hold secrets.
- Never read `.context/` in the source comments as current — **12 stale references across 7 files**, two of which claim the graph is *committed* when the product's central design says it never is.
- Never trust `git log` in this sandbox — it truncates at 50. **`git rev-list`.**

---

*Pilot menu by Claude (Opus 5) under operator direction. Every path:line here was read in my own command output.*
