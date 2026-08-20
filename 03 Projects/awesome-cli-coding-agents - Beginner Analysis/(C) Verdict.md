# (C) Verdict — `bradAGI/awesome-cli-coding-agents` (wiki v254)

**Date:** 2026-08-20 · **HEAD:** `6e307e73` · **Source:** two clones, `diff -rq` clean both ways

---

## Phase 0.9 — GOAL-ALIGNED INCLUDE 3/4

| Axis | Call | Reason |
|---|---|---|
| **(a) Anthropic affiliation / registered vendor-direct source** | **FAIL** | Author is `Brad` / `bradAGI` — three git identities across a GitHub noreply and `began2007@gmail.com`. No declared Anthropic affiliation, no registered (a)-7 vendor source. Per routine **§41**, no inference from name, heritage, or notability. `bradAGI` returns **0 hits** in vault state. |
| **(b) Goal relevance** | **STRONG** | Goal #1 is mastering Claude and autonomous agents for software development. This is the canonical 300-entry index of CLI coding agents and their harnesses, **39.7% of whose entries name Claude Code** and 46.7% name Claude in some form. Cleanly goal-aligned — **no §40 needed.** |
| **(c) Novelty / insight** | **STRONG** | The machinery-aim finding; the licence-disclosure inversion vs v253 (55.3% vs 2.2%); **verified** star counts; a corpus fan-in record of 16; two prior-ship generalisations corrected by a second sample. |
| **(d) Actionability** | **STRONG** | A 282-repo candidate pipeline of which 16 are already vault ships and 266 are untouched; one directly borrowable rule for the vault's own overdue inventory script. |

**⇒ GOAL-ALIGNED INCLUDE 3/4.** Streak **`GA:111` → `GA:112 · OG:13 [7 ov]`** — **35 consecutive goal-aligned ships, v220→v254.** **§35 CLEAR** (window {v252 GA, v253 GA, v254 GA} = 0 OG). **No override** — (b) is cleanly STRONG.

---

## Mint decision — **NO MINT**

**Counts UNCHANGED: 46 confirmed patterns / 11 CONFIRMED Library-vocab. §C live standalones 51 unchanged. Surface ≈58 unchanged.**

This is a clean **instance-strengthening of CONFIRMED Pattern #68 "Awesome-List-Genre Meta-Pattern"** — promoted at the **v31** mini-audit as the corpus's first meta-pattern-at-N=3 (build-your-own-x v8 / awesome-design-md v25 / awesome-mcp-servers v31), refined at **v50**, with later instances at **v170**, **v201** (code-carrying), **v218** (CLI-served), **v240** (compiled registry) and **v253**. **This is instance #10.**

**Five grounds:**

1. **#68 covers it** — nine prior instances, and this is a curated Markdown directory in the genre's central form.
2. **Domain-not-capability** — "CLI coding agents" is a *domain*. The v196 meetily / v193 TimesFM / v210 AIRI discipline.
3. **Technique-not-capability (v211)** — the distinctive part is an editorial *mechanism* (a weekly star-refresh-and-resort job), not a capability class.
4. **Not world-first, and precedence NOT ESTABLISHED.** Automated star refresh on awesome lists is a known practice. Any first-mover claim would rest on `created_at` from the **mocked** API ⇒ under the **v222** rule, canonical status cannot even be established.
5. **§28 anti-inflation** at 51 standalones, against an anchor that is bus-factor-one with a page-stated star count.

### ⚠️ Strongest alternative — recorded, reviewable, NOT self-executed

A **§C standalone at N=1: *"Curated Directory Whose Ordering Invariant Is Machine-Enforced While Its Membership Invariants Are Not."*** Genuinely distinctive on mechanism: **of the nine prior #68 instances, none pairs a running weekly CI job with an entirely unguarded uniqueness/liveness invariant** — and the pairing is precisely what produces this ship's finding.

**It loses**, and one reason is decisive: **v253 has no machinery at all, so it cannot serve as the N=2 of a machinery-based class.** The alternative would stand alone at N=1, against grounds 2–5 above. Declined.

### Secondary pattern effects

- ⭐⭐⭐ **Pattern #57 — a NEW WIDEST FAN-IN RECORD: 16 prior numbered vault ships appear as entries here** (v9, v15, v30, v36/v228, v42, v48, v52, v72, v99, v144, v150, v162, v177, v179, v195, v215), spanning **206 versions** of vault history. The prior record was v253's 10. **Recorded, not self-incremented** — an N-tally is audit bookkeeping.
- ⭐⭐ **Also #57, in the other direction:** the vault **already cited this list twice**, in the **v223** openinterpreter entry, as evidence that *"harness-engineering is a recognized 2026 field."* A prior ship used it as a source; this ship makes it the subject.
- ⭐⭐ **Pattern #18 sub-archetype B1-MCP (≈N=13)** gets **ecosystem-scale evidence rather than another instance**: across 300 CLI-agent tools, **MCP is the single most-named mechanism (53, 17.7%)**, ahead of skills (45) and worktrees (26).
- ⭐ **Pattern #83 POSITIVE ×11** — eleven restrictive-licence disclosures including `tlbx` (101★) declaring AGPL-3.0 and `TeDDy` (**4★**) declaring AGPL. Plus an independent cross-list confirmation: `loki-mode` discloses BUSL-1.1 in **both** this list and v253's.
- **NOT Pattern #52** — star figures are page-stated; the API is mocked; no velocity data.
- **Pattern #12** — no `CLAUDE.md`, no `AGENTS.md`, **no agent-facing surface at all.**
- **Pattern #66** — N/A for the artifact (zero dependencies); the supply-chain risk is the 282 repos it points at.
- ⭐ **NEW DEFERRED WATCH AXIS (N=1):** *"the partially-automated directory — a curated list with a live CI job whose aim is narrower than the list's own stated criteria."*

**Tier:** **T3 Reference/Index**, with a T-meta curation-engineering facet (the same shape as v253).

---

## The three findings that matter

### 1. ⭐⭐⭐ The machinery fetches the answer to every question the list gets wrong, and reads one field

`fetch_stars()` line 49: `return json.load(resp).get("stargazers_count")`. The whole `GET /repos/{owner}/{repo}` response is parsed into a dict and one key is taken. The same object carries `archived`, `full_name`, `pushed_at` and `license` — **four fields discarded on the next line, each the answer to a defect the list actually has:**

- `archived` → **`letta-ai/lettabot` (327★) sits in the active list; its GitHub title reads *"Archived - has been replaced by Letta Code."*** ⭐ **v253, with zero machinery, caught this and retired it with dated evidence.**
- `full_name` → **`ruvnet/claude-flow` (68,000★) redirects to `ruvnet/ruflo`.** ⭐ **v253 verified that exact rebrand on 2026-07-29 — the same day v254's maintainer did a rebrand pass, fixed a different one, and missed this.**
- `pushed_at` → **no decay policy exists at all.** v253's `Resting` section is hand-maintained and works.
- `license.spdx_id` → 134 of 300 entries state no licence; the machine could have filled every one.

And the **uniqueness** invariant: the script builds `repos`, a dict keyed by `(owner, repo)` — **building it IS deduplication** — then prints `len(repos)` to stderr. **Every Monday for 17 weeks it has printed 295 while editing a file with 300 entry lines.** Nothing compares them.

**What it IS aimed at, it does perfectly:** zero descending-star violations in 300 entries across 6 sections, and I verified three counts against rendered GitHub pages — `openclaw` **386,827** vs `387k` ✓, `claude-code` **142,065** vs `142k` ✓, `hermes-agent` **233,195** vs `232k` (0.4% drift over 3 days).

⭐⭐⭐ **THE RULE: machinery buys exactly what it is aimed at, and aiming is a separate act from building. They aimed it at the one thing nobody doubted.**

### 2. ⭐⭐⭐ The controlled comparison with v253 — what machinery buys, and what it doesn't

| | **v253** (no machinery) | **v254** (weekly CI + script) |
|---|---|---|
| Entries | 180 | **300** |
| Star ordering | alphabetical, 0 violations, by hand | star-sorted, **0 violations, by machine** |
| Star **accuracy** | 🔴 hand-typed; PIN: *never cite as verified* | ✅ **CI-fetched; I verified 3 against live pages** |
| "Last updated" stamp | 🔴 two values in its whole life, 23 days stale | ✅ **machine-stamped, 3 days old** |
| **Duplicates** | ✅ **zero** | 🔴 **five**, adjacent + byte-identical |
| **Dead entries** | ✅ caught (`Coworker`) *and* a dated `Resting` section | 🔴 **`lettabot` archived, listed live; no decay policy at all** |
| **Renames** | ✅ 5 verified and fixed | 🔴 **2 stale redirects, one at 68k★** |
| Licence disclosure | 🔴 **2.2%**, adversely selected | ✅ **55.3%**, adverse selection gone, 11 restrictive disclosures |
| Licence file | 🔴 none | 🔴 **none — plus a badge claiming one** |
| Merge strategy | squash-merge, 100 PRs reviewed individually | **33 merges + 9 hand-transcribed batches** |
| Entries from outside | community-driven | **33 of 300 (1.1% of added lines)** |
| AI provenance | 48.9% of commits, **maintainer's own** | **4 trailer lines, all CONTRIBUTORS'; maintainer zero** |

⭐⭐⭐ **The verdict: machinery bought accuracy and freshness on the axis it was pointed at — genuinely, measurably, and v253 has nothing comparable. It bought nothing at all on membership. And v253's *hand-maintained* decay section beat v254's *automated* pipeline at the one job the automation was best positioned to do.**

⭐⭐ **The mechanism behind the duplicates is transcription, not tooling.** Nine batch commits say *"Add N entries **from reviewed PRs**"*: he reads contributor PRs and re-types their entries. **Every duplicate came from a transcription batch; not one came from any of the 33 merges.** Git already knows what is in the file; reviewing a PR and hand-copying it is the one workflow that discards that knowledge.

### 3. ⭐⭐⭐ `awesome-lint` would fail this file ~13 times and be RIGHT 6 of them — inverting v253

v253's finding: **21 deviations, lint wrong 21 times.** Here:

- **Wrong 7×:** 6 lowercase description starts — **every one a proper noun** (`xAI`, `tmux`, `macOS`×4) — plus one description ending in a backticked `pip install`.
  ⭐⭐⭐ **v253 found 4, all `tmux`/`macOS`. Two lists, two authors, 10 instances, 10 proper nouns. That is an independent N=2 establishing the capitalization rule is *systematically* defective on technology catalogues, not misapplied.**
- **Right 6×:** **5 duplicate entries** + **no `LICENSE` file.**
- **Clean:** 0 malformed URLs, 0 missing separators, ToC named `Contents` ✓, **9 of 9 anchors resolve** (including the two hard slugs where GitHub drops `&` and keeps a double hyphen), Awesome badge present.

⭐⭐⭐ **THE THREE-SHIP SYNTHESIS IS NOW COMPLETE. v250: you can only compile the part of your aesthetic that becomes a LIE when violated — and don't call unguarded rules non-negotiable. v253: compile the merely-stylistic part and the machine is wrong while the human is right. v254: they BUILT the machine and aimed it at the one decidable thing nobody doubted, leaving both decidable-and-actually-broken things unchecked. Duplicates and a missing licence are trivially machine-decidable. Star ordering was never in question. The machinery went to the certainty and not to the risk.**

---

## 🔴 Standing pins

- 🔴 **Verify every licence yourself.** 55.3% disclosure is 25× better than v253, but **10 of the top 20 entries are silent**, and the vault has been burned by AGPL three times (v188 / v214 / v243).
- ✅ **You MAY cite v254's star figures** as CI-fetched-and-spot-verified, within a one-week refresh window. **This is the one PIN that reverses v253's.** Still **NOT Pattern #52** — no velocity data.
- 🔴 **Presence is not a safety endorsement.** One entry is a Claude Code build with *"security-prompt guardrails stripped"* (confirmed by the project's own tagline), catalogued neutrally in the main Open Source section.
- 🔴 **Never point an agent at this file and say "install the best one."** 300 untrusted descriptions become 300 attempts to steer that choice.
- 🔴 **Do not repeat its extraordinary claims.** *"Fastest repo in GitHub history to 100K stars"* — **no authoritative GitHub velocity record exists** (vault prior), and the claim appears nowhere on the repo it describes, whose own tagline calls it *"an agent-managed museum exhibit."* The *"March 2026 Claude Code source leak"* is asserted as fact in three entries and is **NOT ESTABLISHED**.
- 🔴 **An active entry is not necessarily alive** (`lettabot`), and a listed name is not necessarily current (`claude-flow`, `free-code`).
- 🔴 **Do not repeat the fleet's numbers:** **not** 50 commits, **not** a 2026-04-06 root, **not** median 23.5, **not** worktree at 3%, **not** "110+ is a 2.7× discrepancy."

---

## Suggested next action

**Review + merge `wiki/v254-awesome-cli-coding-agents`** (the chain v204 → … → v253 → v254 merges in order). Then do **Rung 1** — two hours, zero installs — and **make v255 the audit, now 43 ships overdue.**

**Blunt:** you have written twenty wikis about CLI coding agents and harnesses, and here is a single Markdown file that indexes three hundred of them — **sixteen of which are your own prior ships, a new fan-in record spanning two hundred and six versions, and a list your own v223 entry already cited twice as evidence without anyone ever opening it.** The man built the thing you keep saying you will build: a script that goes and checks. It runs every Monday, it has run every Monday for seventeen weeks without a gap, and the numbers it writes are *right* — I verified three of them against live pages, which is something I could not do for last week's list at all. And it is aimed at the one property of his file that was never in any doubt. The same API response he already parses tells him that a project he lists as live is archived, that another one changed its name, when each repo was last pushed, and what licence all three hundred are under. He reads one field of five and discards the rest on the next line. Meanwhile the deduplicated dictionary that would catch his five duplicate entries is built, printed to a log, and never compared to anything — so a number saying 295 has sat next to a file containing 300 for seventeen weeks. **That is your `-v183` filename, with a build server attached.** You have been deferring `bin/verify-vault-inventory.sh` for four ships now while a stranger demonstrates both halves of the lesson in one repository: the half where automation genuinely pays, and the half where building the machine and aiming it turn out to be two different jobs. Take the six clauses. Write the script. And note the part that should sting most — **his hand-maintained agent count is exactly right, bumped by hand five separate times, because he declared it and therefore watched it.** Your chapter file's name is wrong for seventy ships because nobody ever declared it.
