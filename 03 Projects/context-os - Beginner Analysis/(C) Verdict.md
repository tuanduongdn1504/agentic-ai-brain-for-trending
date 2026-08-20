# (C) context-os — Verdict (v252)

**Subject:** `jacob-dietle/context-os` · HEAD `1027e3f1` · MIT (repo) / closed CLI
**Date:** 2026-08-20

---

## Tier: GOAL-ALIGNED INCLUDE 3/4

| Criterion | Call | Reasoning |
|---|---|---|
| **(a)** Anthropic affiliation | **FAIL** | Jacob Dietle — an independent consultant. No declared Anthropic affiliation. §41: no rescue from name, locale, notability, or the fact that he authors Claude Code skills. |
| **(b)** Goal relevance | **STRONG** | This is **the vault's own architecture** — Karpathy's LLM-wiki pattern — built independently as a Claude Code skill collection for client work. Goal #1 is mastering Claude/agents; the subject is a Claude Code plugin. No §40 needed. |
| **(c)** Substance | **STRONG** ⚠️ *tempered* | 8,243 md lines, 13 skills, a real Claude-Agent-SDK eval harness, a tagged deletion refactor, and two genuinely excellent reference documents. **Tempered:** 26 commits, one author, zero tests, zero CI, and the differentiating engine is a closed binary the author calls unfinished. |
| **(d)** Corpus fit | **STRONG** | Lands directly on the registered Pattern #57 Karpathy-wiki-productization vector (v118 → v134 → [v137] → v234 → **v252**), and on the live code-vs-prose axis (v246→v251). |

**Cleanly GA.** No override. §35 CLEAR.

---

## Pattern outcome: **NO MINT**

**Counts UNCHANGED: 46 confirmed patterns / 11 CONFIRMED Library-vocab · §C live standalones 51 · tracked surface ≈58.**

Declined on **five independent grounds**:

1. **⭐ DECISIVE — direct in-corpus precedent at v234.** `agentic-local-brain` (2026-08-17, three days prior) was a near-identical subject — a personal knowledge system whose headline feature was an auto-compiled LLM wiki — and was declined **NO MINT on four grounds**. v252 is the same class with a different delivery vehicle. Declining v234 and minting v252 would be incoherent.

2. **NOT corpus-first for the domain.** **v134** (`obsidian-second-brain`, explicitly *"an evolution of Karpathy's LLM Wiki pattern"*) and **v118** (OpenHuman's Memory Tree) precede it; **v234** precedes it by three days. This is the **5th instance** on the already-registered Pattern #57 sub-variant *"Productized/Automated Karpathy-LLM-Wiki-Pattern at the Methodology-Influence Layer."*

3. **🔴 THE MACHINERY DOES NOT SHIP (v242 D25 / v246).** The only mechanically novel thing here — **file heat + behavioural co-access driving which knowledge survives** — lives entirely in the **closed-source `context-os` binary**, which the README itself calls *"not fully finished yet."* You cannot mint a capability class on a mechanism that is not in the artifact. This ground alone is sufficient.

4. **Technique/domain-not-capability** (the v211 PixelRAG / v196 meetily / v234 discipline). "Instrument your knowledge base and delete what nobody reads" is a *technique*; personal knowledge management is a *domain*. Neither is §C-vocab-shaped.

5. **§28 anti-inflation** at 51 live standalones, and this is emphatically **not the exemplar** of its class (26 commits, one author, against a genre with 34k★/63k★ incumbents — the v180/v234 "weak anchor" precedent).

### ⚠️ Strongest alternative — RECORDED, reviewable, NOT self-executed

A §C standalone at N=1: ***"Stigmergically-Instrumented Knowledge Base — an agent-maintained graph whose retention is driven by measured access rather than declared taxonomy."***

**Why it is genuinely interesting:** every prior instance on the #57 vector *builds* the wiki. This is the first to **measure whether the wiki is being read and delete what isn't** — v118/v134/v137/v234 all accumulate; this one prunes on evidence. The "desire paths" framing is a real idea, and the v1→v2 refactor is that idea applied to itself.

**Why it loses:** grounds 3–5 above, decisively ground 3 — the heat/co-access engine is the closed binary. It would also be *drawing the circle to make it first* (the camofox v179 discipline).

### ⚠️ AUDIT FLAG (load-bearing, inherited and now aggravated)

The **v137** entry deferred a *"promote-broad-class-vs-split"* question on this exact Karpathy-productization vector to the *"~v139–v140 audit"* — **which never resolved it.** v234 was the 4th data point and re-flagged it. **v252 is the 5th, and structurally new again:**

| Instance | Shape |
|---|---|
| v118 | an agent harness's memory |
| v134 | a skill over *your existing* vault |
| v137 | a one-shot source→skill converter |
| v234 | a standalone app that compiles **and maintains** the wiki |
| **v252** | **a skill collection + closed CLI that scaffolds the wiki as a consulting deliverable, with behavioural instrumentation deciding what survives** |

Five instances, four distinct shapes, one unresolved class question, deferred ~113 ships.

---

## Secondary — recorded, NOT minted

- **⭐ The code-vs-prose axis, 7th consecutive ship** (v246→v252). v252's contribution is a **new species**: v250 called unguarded rules *"non-negotiable"* (a **normative** overclaim); v252 heads them **"Hard Limits (Automated, Zero Tolerance)"** — a **factual** assertion about mechanism that the artifact does not implement. *Overclaiming enforcement in the indicative mood is worse than in the imperative.*
- **⭐⭐⭐ v246's `grep -rni "silent"` detector — 7th CONSECUTIVE REPLICATION, and the richest species yet: SILENCE AS THE ORGANISING PRINCIPLE OF A SEVERITY TAXONOMY.** 22 hits. The entire `code-service-defrag` skill is built on the axis *does this failure announce itself?*, and severity is assigned by how silent the failure is — `SKILL.md:123` 🔴 Landmine = *"A single deploy silently regresses production, no warning"* vs 🟡 Drift = eventually detectable; `:127` *"The 🔴 rule that never relaxes: account/org-global name + identical bindings — the shape that fires silently with zero warning"*; `landmine-patterns.md:1` is titled *"Silent-Overwrite Shapes"*; and the rationale is compiled into the scanner itself (`scan_deploy_target_names.sh:7`, `:92`, `:105`). ⭐⭐⭐ **THE BEST LINE IN THE REPOSITORY, and it diagnoses this vault: `SKILL.md:25` — *"Code drift fails loud (eventually — when a deploy detonates). **Context drift fails silent** — an agent reads the wrong context and nothing announces it."*** That is the `-v183` label and the C22–C27 stale-claim backlog, named exactly. ⚠️ **I first recorded this as a NULL RESULT without running the grep; running it refuted me.** See the error ledger.
- **#88 Anti-Slop-Curation** — instance, at the *specification* pole. Rules are grep-precise (the table ships the detection command) but nothing runs them, and 20 of the commands use `grep -P`, which fails on stock macOS. Joins impeccable v75 / taste-skill v81 / huashu v82 / open-design v83 / ui-ux-pro-max v85 / hallmark v204 / diagram-design v250. **No N-bump asserted.**
- **#83 Honest-Deficiency-Disclosure — a genuine POSITIVE**, twice: the *"not fully finished yet"* caveat sits **at the install site**, and `statistical-validity-checks.md` closes by disclaiming its own novelty (*"not novel; they are table stakes"*).
- **Domain-Vertical-Skill-Collection — considered and REJECTED.** The skill set is heterogeneous (GTM/content/SEO **+** codebase defrag **+** eval **+** epistemics), so it is not a single-vertical collection in the v202-marketing / v187-finance / v64-SEO sense. Closer to a **consultant's personal toolkit**.
- **#12** ships `CLAUDE.md` (no `AGENTS.md`). **No N-bump.**
- **#66 supply chain — MODERATE.** Unpinned `curl|bash` / `irm|iex` from a vendor domain, no checksum, no signature, no release pin, no manual path. Milder than v234's plaintext `http://` (this is TLS), but the closed-source disclosure is the README's **final line**, 102 lines after the install command.
- **NOT #52** — stars/forks page-stated only; the GitHub API is mocked in this environment.
- **NOT #57 corpus-recursive** — no dependency on any prior corpus subject.
- **NEW DEFERRED watch axis (N=1):** *"behavioural instrumentation of a knowledge base — access-frequency and co-access as the signal for what to keep, and 'delete what has no heat' as a maintenance doctrine."*

**Tier:** T1 agent-skill collection, with a T2 closed-CLI facet.

**Streak:** v251 `GA:109` → **`GA:110 · OG:13 [7 ov]`** (**33 consecutive GA**, v220→v252). **§35 CLEAR** (window {v250 GA, v251 GA, v252 GA} = 0 OG).

---

## The one-paragraph verdict

A consultant productised the same pattern this vault runs by hand, and then did the thing almost nobody does: he asked whether anyone was actually reading the scaffolding he had told clients to build, concluded they weren't, and deleted it — tagging both sides so the deletion is diffable. That instinct is right and rare. The execution has one hole straight through the middle. He built a proper three-arm eval harness with pass, fail and **critical-fail** criteria — every critical-fail naming an abstraction he had just deleted, which is the best idea in the repository — then ran only the arm that could not fail, never created the baseline file, graded nothing automatically, published the comparison as settled fact in a six-row table, and deleted the data in the same commit. Meanwhile the repository ships a 256-line document on ground-truth contamination whose own checklist says *"N=8 fits ANY pattern perfectly by accident"* and *"below N=30, do not iterate."* His evidence base was N=8, single-arm, ungraded. **The best document in the repository forbids the inference the README makes.** Take the two documents — they are better than most published work on their subjects — take the critical-fail idea, and install nothing.

---

## Error ledger — 11 caught, 3 MINE

### Mine (all corrected pre-ship)

1. 🔴 **I recorded the v246 `silent` detector as a NULL RESULT without running the grep.** Running it returned **22 substantive hits** and the strongest replication in the series — including the best line in the repository (*"Context drift fails silent"*). **Never assert the outcome of a check you have not run, least of all a null.**
2. 🔴 **I counted 2 `Co-Authored-By` trailer lines; the real number is 19.** Cause: **zsh dropped stdout on a piped grep** — the vault's own documented sandbox hazard. Routing to a file gave 19. *Settle counts by writing to a file, then counting the file.*
3. ⚠️ **I hypothesised two defects that the evidence refuted**, and reported the clean results instead: (a) `scan_worker_names.sh` was deleted **with every reference cleaned up** — no dangling script ref; (b) `applied-example-mcp-retention.md` is **explicitly labelled synthetic**, no client data. I also nearly filed a false `grep -P` portability finding because *this* machine has `ugrep` aliased as `grep`; testing `/usr/bin/grep` confirmed the real defect.

### The fleet's (8)

4. 🔴 **The critic asserted the CLI "does not exist publicly — install.tastematter.dev returns 404, no GitHub releases."** **REFUTED by direct fetch:** the URL returns a valid 5.4 KB installer and the binary ships. This was the run's worst error — publishing it would have been a false claim about a live product. Verifying it myself instead produced the ship's best security material (§13).
5. 🔴 **The critic called `eval-loop`'s Step 0 route *"a REAL hard stop… genuinely fail-closed"*.** Wrong on both halves: it is a markdown table cell (prose, not code), and it routes to a skill that **does not exist**. A stop whose destination is missing is a dead end, not a gate.
6. 🔴 **A mapper claimed the v1→v2 diff had "only 3 files added, 0 deleted."** Refuted by the verifier and by me: **8 files, 158 insertions, 448 deletions, 4 files deleted outright.**
7. 🔴 **A mapper fabricated the README comparison table's row labels** (*"Validation / Accessibility / Agent behavior / Measurement / Iteration"*). The real rows are *Graph health / Tag governance / Node lifecycle / System structure / Navigation / CLI tooling*. Caught by the verifier.
8. 🔴 **A mapper claimed `taxonomy.yaml`/`ontology.yaml` never appear in the git history.** Refuted — they existed as `templates/*_starter.yaml` and were deleted between the tags. The nuance that survives is different and better: the *access-count measurement* is absent, not the files.
9. 🔴 **A situating agent invented external prior art with specific dates** — a Karpathy publication dated 2026-04-04, a "Stigmem v1.0" dated 2026-05-04, a "KeepALifeUS/autonomous-agents" repo. All marked **NOT ESTABLISHED** and **discarded, not published**. ⭐ The v249→v251 fix held a **4th time**: pointing a contradiction stage at the *situating* reports contained the fabrication class.
10. ⚠️ **Line-number citations were wrong throughout two lenses** (off by 50–150 lines); the verifiers corrected them. Every line number in this ship's documents is one I obtained myself.
11. ⚠️ **A mapper claimed `ARCHITECTURE.md` and `ROADMAP.md` exist.** They do not.

### Method notes

- **17-agent `Workflow`** (5 map → 5 pipelined contradiction → 3 situate → 3 contradiction-over-situate → 1 critic): **16/17 done, 1 ERROR** (a verify-situate stage exceeded the StructuredOutput retry cap — the same failure mode as v251; that surface hand-checked). **~2.10M tokens, 496 tool uses, 850 s.**
- ⭐⭐ **The v250/v251 lesson held a 4th time, and paid the most it ever has:** the run's single worst error (#4) was caught only because **I ran the check myself**. The fleet is good at breadth and unreliable on decision-relevant specifics.
- ⭐ **The v251 measurement replicates:** every claim I formed by *reading and quoting a file* held; the claims that broke were **counts, inventories, and generalisations** — mine and the fleet's alike.
- ⚠️ **Sandbox:** `python3` is SIGKILLed · `node -e` is permission-denied · **zsh silently drops stdout on some piped greps → route to a file and count the file** (this caused error #2) · `git branch --show-current` unsupported (old git) · `%(trailers:...)` unsupported by this git.
