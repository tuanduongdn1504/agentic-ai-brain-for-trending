# (C) context-os — Deep Dive (v252)

**Subject:** [`jacob-dietle/context-os`](https://github.com/jacob-dietle/context-os)
**Tagline:** *"Build your first context operating system in 10 minutes. A structured knowledge graph where AI compounds intelligence over time."*
**Licence:** MIT (© 2026 Jacob Dietle) — **repo only**; the `context-os` CLI is closed-source
**Analysed:** 2026-08-20 | **Wiki:** v252

---

## 0. Source verification

✅ **Two independent `git clone`s, `diff -rq` clean both ways** (only `.git` internals differ).

| Fact | Value | Command |
|---|---|---|
| HEAD | `1027e3f19a6b3d2ba573ee0fec92fa0a0aaaa977` | `git rev-parse HEAD` |
| Commits | **26** (`HEAD` and `--all` agree) | `git rev-list --count` |
| Git roots | **ONE** (`f219c65`) | `git rev-list --max-parents=0` |
| Merge commits | **1** (`884773e` "Merge staging: context-os-cli skill") | `git log --merges` |
| Tracked files | **48** | `git ls-files \| wc -l` |
| Paths ever tracked | **57** | `git log --all --name-only \| sort -u` |
| Tags | **2** — `v1.0-ceremony`, `v2.0-stigmergic` | `git for-each-ref` |
| First commit | 2025-12-10 | `git log --reverse` |
| Last commit | 2026-08-13 | `git log -1` |
| Markdown lines | **8,243** | `find -name "*.md" \| xargs cat \| wc -l` |
| Shell lines | **641** (7 scripts) | `find -name "*.sh" \| xargs wc -l` |
| Python lines | **253** (`eval_quickstart.py`) | `wc -l` |
| Skills on disk | **13** `SKILL.md` | `find .claude/skills -name SKILL.md \| wc -l` |

**Identities — 4 strings, effectively ONE person** (⚠️ D26/D27: summing is mandatory):

| Identity | Commits |
|---|---|
| `jacob-dietle <128077360+…@users.noreply.github.com>` | 18 |
| `Jacob Dietle <jacob@jdietle.me>` | 5 |
| `Jacob Dietle <128077360+…@users.noreply.github.com>` | 2 |
| `Smoke <smoke@example.com>` | 1 |

The three Jacob variants sum to **25 of 26**. `Smoke <smoke@example.com>` is a **placeholder git identity** — an unconfigured machine, not a second contributor. It shipped the newest commit (`1027e3f`, the `bottleneck-attack` skill).

**AI provenance:** **19 `Co-Authored-By` trailer lines across 19 of 26 commits (73%)** — Claude Opus 4.6 (1M context) ×8, Claude Opus 4.7 (1M context) ×8, Claude Opus 4.5 ×2, Claude Opus 4.6 ×1.

> ⚠️ **My own corrected count:** I first measured 2 trailer lines. That was **zsh dropping stdout on a piped grep** — the vault's own documented sandbox hazard. Routed to a file: **19**. *Settle counts by writing to a file, then counting the file.*

---

## 1. What it actually is

An **agent-skill collection + templates** that scaffolds a personal knowledge graph the AI reads and writes over time:

- **`knowledge_base/`** — atomic concept notes, `[[wiki-links]]`, frontmatter, lifecycle `emergent → validated (2+ citations) → canonical`
- **`00_foundation/`** — strategic docs that *compose from* the graph and "don't redefine" concepts
- **The loop** — `SENSE → ORIENT → ACT → DEPOSIT`
- **`context-os` CLI** — graph queries, "file heat", behavioural "co-access". **Closed-source.**

Neither `knowledge_base/` nor `00_foundation/` exists in the repo — they are structures the `quickstart` skill *creates in your project*.

⭐ **The stated principle is stigmergy:** *"Desire paths are stigmergy. Agents coordinate by reading and modifying the shared environment — not by following procedures. If a file has zero heat, it's the concrete path nobody walks. Pave the desire paths."*

**This is the same architecture as this vault** (an LLM wiki on Karpathy's pattern), built by someone else for client work. That makes it unusually on-goal — and a fair mirror.

---

## 2. ⭐⭐⭐ THE HEADLINE — the repository contains the exact document that forbids its own README's central claim

### 2a. The claim

`README.md` builds its whole v1→v2 narrative on a measurement:

> *"In practice, agents never read those files. We measured it — taxonomy.yaml had 2 accesses in 90 days, ontology.yaml had 1, and the node lifecycle doc had zero. The ceremony was concrete paths nobody walked."*

**The refactor is real.** `git diff --stat v1.0-ceremony..v2.0-stigmergic` → **8 files, 158 insertions, 448 deletions**. Deleted outright: `templates/taxonomy_starter.yaml` (38), `templates/ontology_starter.yaml` (36), `.claude/commands/graph-health.md` (132), `.claude/agents/ingestion-agent.md` (76). They shipped a **net −290-line deletion** and tagged both sides so it is diffable. That is genuinely rare and genuinely good.

**But the access-count measurement is nowhere in the repository.** The `taxonomy`/`ontology` files existed here only as *starter templates*; the 2/1/0 access counts describe instantiated copies in the author's client deployments. No log, no artifact, no data. ⚠️ **NOT ESTABLISHED — and unfalsifiable from the artifact.**

### 2b. The instrument that *was* here, and was deleted

`eval_quickstart.py` (253 lines, still shipped) is a real Claude-Agent-SDK harness: 8 test cases (T1–T8), each with `pass_criteria`, `fail_criteria`, and **`critical_fail`**. It supports a **three-arm design**:

```
--version old    # Test v1.0-ceremony
--version new    # Test v2.0-stigmergic (default)
--version both
```

`eval_results.jsonl` **was committed** (`d100183` "feat: add cleanroom eval harness"), then **deleted** by `f7619ba` — *"docs: rewrite README with v1→v2 narrative, **drop eval results**"* / *"Removed eval_results.jsonl (eval harness script kept for reuse)."*

I recovered it (`git show f7619ba^:eval_results.jsonl`). Settled by command:

| Measure | Value |
|---|---|
| Rows | **8** |
| `"version": "new"` | **8** |
| `"version": "old"` | **0** |
| `tool_count: 0` | **7 of 8** |
| `tool_count: 5` | 1 (T2) |

- **The baseline arm was never run.** `--version old` requires `eval_old_claude.md`; that file **was never committed** (0 of 57 historical paths).
- **7 of 8 runs used ZERO tools.** Five responses open *"Based on your CLAUDE.md, here's…"* — the agent **described** the SENSE→ORIENT→ACT→DEPOSIT loop instead of executing it. In a system whose thesis is that agents coordinate by *reading and modifying the environment*, its own recorded runs mostly didn't touch it.
- **Nothing is graded.** `pass_criteria` / `fail_criteria` / `critical_fail` appear only in their definitions (lines 44–95) and in `print_result` (lines 175–177) — **printed for a human to eyeball**. Zero hits for `score`, `judge`, `verdict`, `assert`, `grade`. The JSONL records `duration_s`, `tool_count`, `response_length` — **mechanics, never correctness**. The single computed metric is a substring search for `[VERIFIED`/`[INFERRED`/`[UNVERIF`.

### 2c. ⭐⭐⭐ And the repository ships the document that forbids the inference

`.claude/skills/eval-loop/eval/statistical-validity-checks.md` (256 lines) is a rigorous runbook against *"the backwards-reasoning failure mode: agent derives scoring rules from known positives, declares victory, real deployment falls over."* Its own Common Traps checklist:

> - *"**'N=8 is enough to see the pattern' — no, N=8 fits ANY pattern perfectly by accident**"*
> - *"'The scoring model has 90% accuracy on our test set' — same test set you iterated on?"*

And §5: *"Labeled N < 30 → **do NOT iterate.** Produce a 'hypothesis-generating' output labeled as directional."*

**The repo's own evidence base is N=8, single-arm, no baseline, no holdout, ungraded — and the README states the comparison as settled fact in a six-row table.** By its own §5 rule that result is *directional at best*.

⭐ **The borrowable rule:** *an instrument you only point at the arm that cannot fail is not a measurement.* The harness was kept and the reading was dropped — the exact inverse of v251, where the instrument shipped and no reading did.

> ⚠️ **Stated fairly:** the *deletion* was honest housekeeping (the commit says what it did), the harness is real and reusable, and none of this makes the v2 design wrong. The v2 design is probably better. The claim that it was **measured** is what does not survive.

---

## 3. ⭐⭐⭐ The best idea in the repo: a regression test against your own deleted abstractions

Every one of the 8 `critical_fail` criteria names something they **deleted**:

| Test | `critical_fail` |
|---|---|
| T1 | *"References taxonomy.yaml or ontology.yaml as key system files"* |
| T2 | *"Checks taxonomy.yaml for blessed tags before creating, or creates a staging file"* |
| T3 | *"References taxonomy.yaml tag sprawl checking or `_system/knowledge_graph/`"* |
| T4 | *"References ingestion staging workflow or taxonomy validation"* |
| T8 | *"References node_lifecycle.md or says to check the lifecycle documentation"* |

Plus T3's `fail_criteria`: *"Says to run /graph-health (**removed command**)"*.

⭐⭐⭐ **The pattern: when you delete an abstraction, the test is that the agent does not resurrect it.** That is a genuinely excellent instinct and the single most transferable idea here — and the fact that nothing *evaluates* it does not make the idea worse, only unfinished.

---

## 4. Code vs prose — the whole repository is prose, and one heading says otherwise

The v246→v251 axis, applied:

| Enforcement surface | Result |
|---|---|
| CI workflows | **0** — no `.github/`, no `*.yml`, no Makefile (searched; none exist) |
| Shell scanners that can fail | **0 of 7** — zero `exit 1`, zero `set -e` across all 641 lines |
| Automated grading in the eval harness | **0** (one substring count) |
| Tests shipped | **0** (`find` for `test_*`/`*_test*`/`tests` → empty) |
| README-vs-disk skill drift gate | **0** |

For an agent-skill collection this is *largely correct* — a skill **is** prose addressed to a model, and v250's rule applies: you can only compile the part that becomes a lie when violated.

⚠️ **The exception is a labelling problem.** `anti-slop-rules.md` heads its rule block **"Hard Limits (Automated, Zero Tolerance)"**. Nothing in the repository automates them. v250 called unguarded rules *"non-negotiable"* (a normative overclaim); this calls them **"Automated"** — a **factual** assertion about mechanism that is not true of the shipped artifact. The 142 tests that do run are elsewhere (see §6).

✅ **A gotcha I went looking for and did not find:** the repo does **not** violate its own banned-word rules. All hits for *Furthermore / Moreover / Revolutionary / Game-changing* are inside rule definitions and grep patterns, confined to 3 content-strategy files. **Zero genuine prose violations.** The em-dash cap (≤2) is scoped to *generated content*, not the repo's docs, so applying it to the README would be a category error.

🔴 **One verified portability defect:** **20 shipped detection commands use `grep -P`**. Stock macOS `/usr/bin/grep` (BSD grep 2.6.0-FreeBSD) rejects it — `grep: invalid option -- P`, **exit 2**. On a default Mac, the entire anti-slop detection layer errors out. *(This machine has `ugrep` aliased as `grep`, which does support `-P` — I nearly filed a false negative; the defect is real only against the stock toolchain, which is what a Mac reader has.)*

---

## 5. 🔴 A hard STOP that routes nowhere

`eval-loop/SKILL.md` references a sibling skill **`eval-driven-scoring` 10 times**, including:

- `:27` — *"**LLM scoring / classification / predictive ranking — use `/eval-driven-scoring`. This is a HARD route, not a suggestion.**"*
- `:43` — *"**STOP. Route to `/eval-driven-scoring` and read `references/statistical-validity-checks.md`. Do not proceed with this skill.**"*

**`eval-driven-scoring` does not exist in this repository.** Only `eval-loop` ships.

Existence-testing every relative path cited in that file:

| Cited path | Status |
|---|---|
| `references/backpressure-patterns.md` | ✅ OK |
| `references/llm-judge-rubrics.md` | ✅ OK |
| `eval-driven-scoring/references/statistical-validity-checks.md` (`:446`) | 🔴 **DANGLING** |
| `references/statistical-validity-checks.md` (`:43`) | 🔴 **DANGLING** — the file is at `eval/statistical-validity-checks.md` |
| `references/shakespeare-rubric.md` (`:212`) | 🔴 **DANGLING** — never tracked (0 of 57 paths) |

⚠️ **Why this matters more than ordinary doc rot:** a predictive/scoring problem — *lead scoring, candidate matching* — hits a **hard STOP** and is routed to a skill that isn't installed, then told to read a file at a path that doesn't resolve. The 256-line statistical doc **is** present, but its own skill never cites it correctly. The reference paths still point at the private parent skill it was carved out of: **the gate shipped, the gatekeeper didn't.**

---

## 6. The closed-source boundary — narrower than the framing suggests

README's last line: *"The **context-os CLI** … is a separate product. It's free to download and use, but **the source is not open**."* Install is `curl -fsSL https://install.tastematter.dev/install-context-os.sh | bash` (and `irm | iex`).

**Measured dependency** — `context-os` mentions per skill directory:

| Skill | Mentions |
|---|---|
| `context-os-cli` | 46 |
| `quickstart` | 6 |
| `epistemic-context-grounding`, `context-os-basics`, `code-service-defrag` | 1 each |
| **8 others** | **0** |

✅ **8 of 13 skills never mention the CLI at all.** The v242 **D25** / v246 "the machinery is not here" pattern applies to the *headline* features — graph queries, heat, co-access, the things the README leads with — but **not** to most of the skills, which are portable prose that works without the binary. That is a real and important correction to the obvious reading.

**Disclosure quality — mixed:**
- ✅ The *unfinished* caveat is at the install site: `:40` *"(FYI: this part of Context OS v2 is not fully finished yet)"*. Credit where due.
- ⚠️ The *closed-source* fact is **line 148 of 148 — the final sentence**. The `curl | bash` is at `:46`. You pipe a remote script to your shell **102 lines** before learning the binary is proprietary.
- 🔴 That same sentence is **inaccurate**: *"the install script **in this repo** points at those releases."* `install-context-os.sh` is **not in the repo and never was** (0 of 57 historical paths). It lives on `install.tastematter.dev`.

**Security, stated without inflation:** unpinned, unversioned `curl|bash` from a vendor domain — no checksum, no signature, no release-pinned URL, no manual path, TLS-only trust. Nothing in the repo treats fetched or ingested content as untrusted (no `injection`/`sanitiz`/`data not instructions` anywhere). A `context-os daemon start` that *"auto-tracks file access"* runs in the background with **no privacy or telemetry statement anywhere in the repository** — that absence is the finding; I did **not** establish that anything is transmitted.

---

## 7. Documentation drift, and where it actually bites

**13 skills on disk, 8 named in the README table.** The 5 absent: `bottleneck-attack`, `code-service-defrag`, `content-strategy-and-assembly`, `decision-accountability`, `seo-aeo-expert-perspectives`. Both set-differences run: **no phantoms** — the README names nothing that doesn't exist. Drift is one-directional.

⭐ **The subject's own `CLAUDE.md` lists the same 8** (lines 17–24), so 5 of 13 shipped skills are invisible in **both** human-facing surfaces.

✅ **But the functional routing surface is fine.** Claude Code discovers skills from frontmatter, not from a table — and these descriptions are **good**: long, trigger-rich, with explicit *"Use when user says…"* hooks. The five undocumented skills have some of the **best** descriptions in the set. So this is a documentation defect, **not** a routing failure — exactly the v250 ADR-0004 lesson, passed.

Two genuine frontmatter defects:
- 🔴 `seo-aeo-expert-perspectives` — `name: SEO & AEO Expert Perspectives`, the **only** name that doesn't match its directory (spaces + `&`); all 12 others are the kebab-case dir name.
- ⚠️ `context-os-basics` — `description: Foundation patterns for building context operating systems`. Eight words, no trigger conditions, no *"use when"*. The weakest routing surface in the repo, on its smallest skill (2,983 bytes).

**Naming drift, four ways:** repo `context-os` · README title *"Context OS Quickstart"* · `CLAUDE.md:1` *"# GTM Context OS Quickstart"* (the old GTM name) · README's compare link → `jacob-dietle/gtm-context-os-quickstart`.

✅ **Fairness correction:** I expected that compare link to be broken. **It is not** — I fetched it, and GitHub's rename redirect resolves `gtm-context-os-quickstart` → `context-os` correctly. The four-way naming inconsistency is real and cosmetic; **the link works.**

---

## 8. What is genuinely good

**⭐⭐⭐ `statistical-validity-checks.md` (256 lines) — the best artifact in the repository.** An operational runbook on ground-truth contamination in LLM scorers:

- **§1 Ground Truth Provenance — The First Gate.** A CONTAMINATED / CLEAN / ACCEPTABLE-WITH-CAVEAT table. *"Contacts associated with closed/won deals"* → *"Pre-filtered on the outcome you're predicting. Using outcomes as predictors = tautology."* *"Leads that our sales team engaged with"* → *"Sales engagement is already scored informally — you're copying existing bias."*
- **§2 Selection Bias Audit** — a formal template (Population `P` / filter `F` / inclusion rate / excluded subpopulation `E`) with a worked example: 8 labelled from 2,000, where the filter selects on the target.
- **§3 Base Rate Denominator** — *"If you don't know this, you cannot compute discriminative power of any rule."* With SQL.
- **§4 Discriminative Ratio** `DR = P(fire|pos)/P(fire|neg)` with a verdict band. ✅ **All four worked examples check out arithmetically** (0.85/0.15=5.67, 0.60/0.25=2.4, 0.50/0.30=1.67, 0.60/0.55=1.09), plus an honest instability warning below n=20.
- **§5 Holdout** — 30% split, *"commit the holdout IDs, do not read during iteration"*, run **once**, and a gap-interpretation band (<3pp ship / 3–10pp caveat / >10pp revert).
- **§8 Backwards Reasoning Detector** — *"Did I derive this hypothesis by examining known positive examples?"* and *"What would FALSIFY this rule? … If you cannot describe falsification → the hypothesis is unfalsifiable. Do not use."*
- ✅ **#83-grade honesty about its own novelty:** *"train/test split, base rates, discriminative power are not novel; they are table stakes… This document codifies them at the skill level so they become unavoidable."*

**⭐⭐ `landmine-patterns.md` — the best engineering content.** Pattern 1: two directories declaring the same deploy-target name with identical bindings → *"A deploy from either location overwrites the other's code with zero warning."* Translated across Cloudflare / Railway / Vercel / Fly / Compose, with a real detection method (*diff a live `/health` or version endpoint against each directory's source*) and a **conditional** severity taxonomy (🟡 Drift → 🔴 Landmine **on schema change**). Self-imposed hygiene: *"anonymized — no real IDs, domains, or user counts"*, and `scan_bindings.sh` *"reads host/project identity only, never credentials."*

**⭐ `bottleneck-attack`** — *"Speeding up something that should not exist is not progress."* Has a **"Do not use it when"** section (good skill design). Its algorithm — Question → Delete → Simplify → Accelerate → Automate — is Musk's five-step process, and *"Attack the tip of the spear"* is Theory-of-Constraints lineage; **both unattributed**. Its own addition is the better line: *"A local improvement that transfers cost to people who cannot consent is debt, not optimization."*

✅ **Client-data hypothesis REFUTED:** `applied-example-mcp-retention.md` opens *"# Synthetic Worked Example… This fictional example demonstrates the workflow without using client, user, or private operational data."* No leaked client names, credentials, or real metrics found anywhere in the tree.

✅ **A clean inventory result:** `scan_worker_names.sh` was deleted in `4373a79` (*"generalize to first-principles, multi-platform"*) **with every reference cleaned up** — 7 scripts on disk, exactly 7 referenced. No dangling script reference. I hypothesised a defect here and the evidence refuted it.

**Audience tell:** `CLAUDE_CODE_SETUP_GUIDE.md` teaches *"Invisible Password Typing"* and the *"Terminal Restart Rule"*, and installs **Cursor IDE** (31 mentions) as the host on both platforms. This is **client-onboarding collateral for non-technical GTM users** — which explains the "10 minutes" framing and the whole repo's shape.

---

## 9. Not established

- Whether the taxonomy/ontology **access counts** (2/1/0 in 90 days) were ever measured — no artifact, unfalsifiable from the repo
- Whether the `context-os` CLI works, or exists as a shipping binary (**not downloaded, not executed**)
- Whether the daemon transmits anything
- The **142 automated anti-slop tests** and the **5 verified multi-agent builds** cited as provenance — neither ships here
- Stars/forks/watchers — **page-stated only; the GitHub API is mocked in this environment ⇒ NO Pattern #52 claim**
- Any subject code was executed — **none was**

---

## 10. Verdict

**GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL §41 (Jacob Dietle, no declared Anthropic affiliation) · (b) **STRONG** (this is the vault's own architecture, built independently for client work) · (c) STRONG · (d) STRONG.

**NO MINT.** See `(C) Verdict.md`.

**Quality, honestly:** the *thinking* is well above average and the *plumbing* is below it. `statistical-validity-checks.md` and `landmine-patterns.md` are better than most published material on their topics. The eval harness has the right architecture and was run in the one configuration that could not produce a negative result. The refactor is brave, correctly motivated, tagged, and diffable — and its headline justification is an unfalsifiable claim about files that were never in this repo. Nothing here is enforced by anything, one heading says otherwise, and a hard STOP routes into a skill that was never published.


---

## 11. ⭐⭐⭐ Addendum — the `silent` detector, and the best line in the repository

Running the v246 portable detector (`grep -rni "silent"`) returns **22 hits**, and they are not incidental. The entire `code-service-defrag` skill is organised around one axis — **does this failure announce itself?** — and **severity is assigned by how silent the failure is**:

- `SKILL.md:123` — 🔴 **Landmine** = *"A single deploy silently regresses production, no warning"*; 🟡 **Drift** = eventually detectable
- `SKILL.md:127` — *"**The 🔴 rule that never relaxes:** account/org-global name + identical bindings … the shape that fires silently with zero warning"*
- `landmine-patterns.md:1` — the file is titled *"Landmine Patterns — **Silent-Overwrite Shapes**"*
- `bottleneck-attack/SKILL.md:172` — *"What observation will detect silent failure?"*
- And the rationale is **compiled into the scanner**: `scan_deploy_target_names.sh:7` — *"a deploy from either silently overwrites the other. Identical resource bindings make it certain"*; `:92`/`:105` carry the same reasoning into the severity assignment

**⭐⭐⭐ The best line in the repository, and it diagnoses this vault:**

> `code-service-defrag/SKILL.md:25` — *"Code drift fails loud (eventually — when a deploy detonates). **Context drift fails silent** — an agent reads the wrong context and nothing announces it."*

That is a one-sentence diagnosis of this vault's own chronic disease: the `_state/03c-projects-v61-**v183**.md` filename that has been wrong for 69 versions, and the C22–C27 stale-claim backlog. A wrong deploy detonates; a wrong context just quietly produces worse work forever. **This is why the vault's inventory checks matter more than its style rules** — and it is the strongest argument yet for the bidirectional `bin/verify-vault-inventory.sh` that v250 specified and that still does not exist.

> ⚠️ **Error-ledger entry (mine):** I first recorded this detector as a **NULL RESULT** — "zero substantive hits" — **without running the grep.** Running it refuted me and produced the strongest replication in the series. *Do not assert the outcome of a check you have not run, least of all a null.*

---

## 12. Reception — independently verified, page-stated only

| Fact | Value |
|---|---|
| Stars | **108** |
| Forks | **33** |
| Watchers | **3** |
| Open issues | **1** |
| Releases | **ABSENT (0)** |
| Topics | **ABSENT** |
| Licence shown | MIT |

⚠️ **Page-stated (§37.4), NOT API-verified — the GitHub API is mocked in this environment ⇒ NO Pattern #52 claim, and no velocity or growth claim of any kind.**

Two observations that matter for placement:

- **This is a 108-star repository.** It is a small, personal, single-author project — which materially supports the "not the exemplar / weak anchor" mint ground (the v180 / v234 precedent). It is not competing with the 34k★–63k★ incumbents in its genre; it is a consultant's toolkit published openly.
- **33 forks against 108 stars (~31%) is an unusually high ratio**, and it is *by design*: the README's step 1 is *"Fork this repo (or clone it)."* Forks here are the intended installation mechanism, **not** a popularity signal — do not read them as one.

---

## 13. 🔴 The installer — fetched and read (NOT executed)

The fleet's critic asserted that *"the CLI does not exist publicly (install.tastematter.dev returns 404, no GitHub releases)."* **That is REFUTED.** I fetched the URL: it returns a **valid 5.4 KB shell script**, `# Context OS CLI installer`. The CLI ships. Had I repeated the critic's claim I would have published a false statement about a live product.

Reading the installer produces a much better-grounded security picture than the repo alone allows — every item below is from the script's own lines:

| Finding | Evidence |
|---|---|
| 🔴 **The only integrity check is a size floor** | `:92` *"Verify binary exists and is not truncated (should be at least 10 MB)"*; `:95` `MIN_SIZE=$((10 * 1048576))`. A grep for `sha\|checksum\|signature\|gpg\|cosign` returns **nothing else**. Any ≥10 MB blob served from that host installs and runs. |
| 🔴 **Version resolved at install time from a mutable server file** | `:9` `VERSION="${VERSION:-latest}"`; `:59` `VERSION=$(curl -fsSL "$BASE_URL/latest.txt")`. `curl \| bash` installs whatever `latest.txt` points at that second. *(Pinnable only if you set `VERSION=` yourself.)* |
| ⚠️ **A staging channel, switchable by env var** | `:10` `CHANNEL="${TASTEMATTER_CHANNEL:-production}"`; `:52-55` flips `VERSION` to `staging`. |
| 🔴 **It auto-registers a login-persistent daemon at a 30-second interval** | `:126` *"Register daemon to run on login (best-effort, warn on failure)"*; `:128` `daemon install --interval 30`. |
| Install target | `:8` `INSTALL_DIR="${INSTALL_DIR:-$HOME/.local/bin}"` — one directory, no sudo. ✅ |

⭐ **The daemon point is the sharpest.** README presents it as a step *you* choose to run later — *"`context-os daemon start`  # Background sync (auto-tracks file access)"*. In fact **the installer registers it to run on login, every 30 seconds, without asking.** Combine that with: the binary is closed-source, and there is **no privacy or telemetry statement anywhere in the repository**. I did **not** establish that anything is transmitted off-machine — but a closed binary that polls your file access every 30 seconds from login, installed by an unpinned pipe-to-shell whose only integrity check is a size floor, is a footprint no reader should accept on a machine holding client or candidate data.

✅ **Stated fairly:** the script is competently written — it detects OS/arch properly, refuses a truncated download, warns rather than failing hard on daemon registration, and installs to a single user-owned directory with no `sudo`. The problem is not craftsmanship; it is the **trust model**.

---

## 14. Two count disputes, both settled — and both are D26/D27

The fleet contradicted two of my numbers. Settling them:

**(1) 18 vs 17 commits for `jacob-dietle`.** *Both are right; they measure different things.*

```
git shortlog -sne --all              → 18   (includes the merge commit 884773e)
git shortlog -sne --all --no-merges  → 17
```

`884773e` ("Merge staging: context-os-cli skill") is authored by `jacob-dietle`. **Neither number is an error — failing to declare whether merges are counted is.** Textbook **D26/D27**: *declare the ref population and the merge basis.* This repo's totals: **26 commits including 1 merge; 25 excluding it.**

**(2) The critic called `eval-loop`'s Step 0 route *"a REAL hard stop… genuinely fail-closed and immediately borrowable."* I disagree, with evidence, and the critic is wrong on both halves:**

- It is **not code** — it is a markdown table cell reading *"STOP. Route to `/eval-driven-scoring`… Do not proceed with this skill."* Prose addressed to a model. Nothing enforces it.
- It is **not fail-closed** — it routes to a skill that **does not exist in this repository** (§5), and tells the reader to open a file at a path that does not resolve.

A stop instruction whose destination is missing is not a gate; it is a **dead end**. The *idea* is right and worth borrowing — refuse to evaluate a predictive problem with a deterministic-quality loop — but what ships is an instruction, not a mechanism.
