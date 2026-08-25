# (C) Graft — Verdict

**v275 · 2026-08-25 · `NanoNets/Graft` · MIT · npm `@nanonets/graft` v0.13.0 · HEAD `ee1ef035`**

---

## Rating: GOAL-ALIGNED INCLUDE — 3/4

| Axis | Verdict | Basis |
|---|---|---|
| **(a) Cultural peer / Anthropic** | **FAIL** | NanoNets is a company; authors are Shrish Dwivedi + Anirudh Kumar. **Not Anthropic**, not a registered (a)-7 vendor-direct source (§41; #19 19a). No name/heritage inference applied. |
| **(b) Goal relevance** | **STRONG** | Goal #1 core substrate. It is a context layer *for coding agents*, wires into Claude Code first-class (statusline, four lifecycle hooks, a skill, MCP), and its entire thesis is Claude Code token/latency economics. Cleanly GA — no §40, no override. |
| **(c) Quality / rigour** | **STRONG** | 904 test cases / 2,858 assertions over 41,918 lines (ratio 0.87); all CI actions SHA-pinned; CodeQL + OpenSSF Scorecard; a `pull_request_target` workflow that states its hazard and obeys the invariant; 76/76 lockfile entries integrity-hashed from a single registry. |
| **(d) Novelty / corpus value** | **STRONG** | Corpus-first subject, verified at full vault extent. First #23 instance storing the graph as an editable markdown wiki. Supplies the ship's rule and a cross-author N=2 of v273's `pull_request_target` finding. |

**Streak:** v274 `GA:131` → **`GA:132 · OG:13 [7 ov]`** — **55 consecutive goal-aligned ships v220→v275.**
**§35:** CLEAR — window {v273, v274, v275} = 0 OFF-GOAL.
**Override review:** 15th consecutive discharge (v153→v275 = 0 overrides).

---

## Mint decision: **NO MINT**

**Counts UNCHANGED: 46 top-level patterns / 12 CONFIRMED Library-vocab · §C-1 12 · §C-2 39.**

Graft is a clean instance of **CONFIRMED Library-vocab #23** — *"Pre-Indexed Read-Only Code Knowledge-Graph Queried by Coding Agents via MCP"* — taking the anchor from **N=5 → N=6**:

> graphify **v16** · GitNexus **v33** · codegraph **v70** · codebase-memory-mcp **v172** · code-review-graph **v226** · **Graft v275**

All six MCP tools (`graft_find_code`, `graft_find_all`, `graft_file_api`, `graft_trace_calls`, `graft_repo_map`, `graft_check_freshness`) are read-only. *(N-tally is audit bookkeeping — recorded, not self-incremented.)*

**Declined on:** capability-not-storage-format · sub-variant-within-a-CONFIRMED-pattern strengthens rather than mints · not world-first for the class. **§28 was NOT the sole ground** (§44.5).

### Two DEFERRED watch axes (N=1, recorded not minted)

1. **"Agent code-knowledge-graph persisted as an editable linked-markdown wiki rather than a queryable database."** Graft is the first #23 instance whose store is human-readable `[[wikilinked]]` markdown with human-written regions preserved verbatim across rebuilds — the prior five use SQLite / Cypher / networkx. `src/context/node-file.ts:4`: *"There is no database."* A genuine sub-axis; eligible at a clean N=2.
2. **"A documentation claim corrected by an AI collaborator and reverted by the human maintainer, leaving a composite neither party authored."**

### Recorded instance-strengthening (not self-incremented)
**#18** sub-archetype B1-MCP · **#19** 19a · **#66** supply-chain awareness.

### Candidate Pattern #57 — **NOT ESTABLISHED**
`.claude/proven-config.json` declares `"ruflo.proven-config/v1"` and `"ruflo": ">=3.24.0"`; `ruflo` is corpus **v42**. But `git grep -in ruflo` across all 267 tracked files returns **only those two lines** — no dependency, no docs, no other reference. Recorded as a candidate link and an undocumented orphan config artifact. **Not counted as a #57.**

---

## The one-paragraph verdict

Graft is a serious piece of engineering by people who are demonstrably careful — 904 tests, a privacy allowlist with negative controls against real PII, a `pull_request_target` workflow that names its own attack surface and then obeys the invariant absolutely, and CI comments that document silent-failure modes by name (*"the Windows CI leg reported failure while actually running zero tests"*). It is also carrying a hero claim of **"up to 4× cheaper and 3× faster"** whose own evidence section is plural about repositories and contains one, and whose measured aggregates are **1.27× and 1.16×**. The interesting thing is not that the claim is inflated; it is that **the repository already caught it.** On 2026-08-11 a commit authored by `Claude <noreply@anthropic.com>` diagnosed it exactly — *"the headline overstated what the adjacent table showed"* — corrected the number to 2×/2.5× and removed the footnote that had attributed 4×/3× to single-task peaks from a three-repo sweep. On 2026-08-12 the human maintainer reverted the headline in one line with no rationale, and **only the headline**. At HEAD the strong claim stands and its disclosure does not, and neither commit produced that state. The three-repo sweep it rests on has never appeared in this repository: I scanned all 402 commits and the word "Excalidraw" exists in exactly two of them — the one that added the footnote and the one that deleted it.

---

## ⭐⭐⭐⭐⭐ The ship's rule

**A check cannot survive someone with standing to overrule it — and a partial correction composed with a partial revert produces a claim neither party wrote.**

Every surface in this repo that a *maintainer* reads is gated to an exceptional standard. Every surface a *buyer* reads is held by nothing. Same hands, same week. The difference is not care; it is that a maintainer is afraid of getting the code wrong and nobody is afraid of getting the pitch wrong. **The gate was not missing here. It fired, it was right, and it was overruled for free.**

**LADDER:** v270 no gate fires on a claim true when written · v271 a gate's scope comes from where it lives · v272 a gate holds when something else already requires it · v273 a check is only as permanent as the place you put it · v274 neither gate nor habit reaches a claim stored outside the repo · **v275 a check that reaches the claim and is correct can still be reverted.**

---

## What the vault takes from this

1. ⭐⭐⭐ **Aim a markdown assertion at your own published docs, not only at generated ones.** Graft's tests read `GEMINI.md`, `INDEX.md` and generated cards, and read `TELEMETRY.md` — the document it calls *"the complete, authoritative contract"* — **never**. The vault has the identical shape: `(C) proposed-verify-vault-inventory.sh` is now **twenty ships old and still unrun**.
2. ⭐⭐⭐ **Three copies is the smell.** Graft's event list exists in `TELEMETRY.md`, in `contract.ts`, and typed a third time inside the test that pins it — so the gate compares copy 2 to copy 3 and the authoritative copy is unchecked. **Derive the population from the tree** (v271's sha256 manifest, v272's `readdir`), never from a list you typed.
3. ⭐⭐ **A revert is an unreviewed commit.** `35ac2ae` changed a load-bearing public claim with a one-line message and no rationale, and silently left a deletion in place. The vault's per-ship append is exactly this kind of surface.
4. ⭐ **Credit people whose work you superseded.** `CREDITS.md` thanks eight contributors whose language PRs were *not* merged, for the idea that motivated the generic tier. Set beside **v270**, whose *"we list them all here"* sat above four blank lines.

---

## Pilot verdict: ⭐⭐ READ-AND-BORROW, THEN A FENCED INSTALL

Genuinely pilotable — MIT, project-local by default for Claude Code, `--dry-run` available, idempotent merge that refuses to clobber an existing statusLine.

🔴 **Four fences, all specific:**
- **`--agents claude --no-global`** or you write `~/.codex/hooks.json` (a hook firing in *every* repo) and `~/.gemini/skills/graft/SKILL.md`.
- **Remove `Bash(node dist/cli.js:*)`** from `permissions.allow` after init — it is not scoped to graft, and in your repo `dist/cli.js` is your own build, pre-approved to run unprompted with arbitrary arguments.
- **`graft build --deep` sends raw source to your LLM with zero secret-scanning.** It inherits `git ls-files` semantics so gitignored files are safe, but a credential hardcoded in a *tracked* file will be summarised and sent. `SECURITY.md` does not mention this.
- **Telemetry is opt-out, on by default.** It is honest, bucketed, path-free, honours `DO_NOT_TRACK`, and cannot send from a clone — but it is on unless you turn it off.

🔴 **Never cite the 4×/3× figure, or the hero table as a single experiment** — its efficiency rows come from the run where correctness was flat, and its correctness row from a 50-instance SWE-bench subset with roughly half those efficiency numbers.

**Full ladder → `(C) Pilot Methods Menu.md`.**

---

*Verdict by Claude (Opus 5) under operator direction.*
