# (C) Pilot Methods Menu — `bradAGI/awesome-cli-coding-agents` (v254)

**Verdict: READ-AND-APPLY. There is nothing here to install** — the artifact is one Markdown file, one PNG, a stdlib-only script and a workflow. The value is (a) one borrowable rule, (b) a 266-repo candidate pipeline, and (c) a measured ecosystem map. **Rung 1 is where the payoff is, and it costs nothing but two hours.**

---

## Rung 0 — 25 minutes, zero risk

**Read three things, in this order:**

1. **The `Contributing` section (README lines 672–688).** Three inclusion tests, all decidable from a candidate's own README. Compare against v253's four-way functional test — v254's is *narrower and cleaner*, and it has a liveness clause v253's lacks (*"valid, active project (no dead repos)"*) which **the list itself violates**.
2. **The `Agent infrastructure` section (87 entries, lines 492–670).** This is the densest catalogue of agent-adjacent tooling the corpus has seen: memory layers, code graphs, policy gates, provenance trackers, sandbox provisioners, context packers. **Read it as a map of what people are actually building around Claude Code**, not as a shopping list.
3. **`scripts/update-stars.py`, lines 44–52.** Ninety seconds. It is the whole lesson.

🔴 **While reading, hold three facts:** the list will not reliably tell you the licence (10 of its top 20 are silent); one entry is archived and listed as live; and one entry is a Claude Code build with its security guardrails deliberately stripped.

---

## ⭐⭐⭐ Rung 1 — 2 hours, ZERO installs. **The rung that pays.**

### (a) Finally write `bin/verify-vault-inventory.sh` — now with SEVEN clauses from five ships

This has been the recommended action for four consecutive ships (v250, v251, v252, v253) and has not been written. **v254 supplies the clause that makes it urgent and the argument that makes it cheap.**

Use `node` and `awk`. **Not `python3` — it is SIGKILLed in this sandbox (exit 137).** Route all counts to a file and count the file; **zsh silently drops stdout on some pipelines.** Use `/usr/bin/grep`, not `grep` (the `ugrep` shim does not honour `command grep`).

| # | Clause | From | What it catches |
|---|---|---|---|
| 1 | **Bidirectional** inventory check — both set-differences, always | **v250** | An index↔content check run one way is blind to what is missing from the index |
| 2 | **Filename-label vs newest-entry** | **v250** | `_state/03c-projects-v61-v183.md` holds entries through **v254** — wrong for **71 ships** |
| 3 | **Byte-equality** for duplicated content, with the incident in the comment | **v251** | Two copies of one fact silently diverging |
| 4 | **Graveyard / `critical_fail` regression** on retired rows | **v252** | A deleted abstraction being resurrected |
| 5 | **A byte budget on `CLAUDE.md`'s head blocks** | **v253** | The shim broke the `Workflow` tool from v200 to v238; hand-compacted three times |
| 6 | **Dated-stamp freshness** on every `checked YYYY-MM-DD` / "current through vNNN" notice | **v253** | Notices that go stale silently |
| 7 | ⭐ **NEW — a UNIQUENESS clause, and it must compare a count to a count** | **v254** | Duplicate entries, duplicate pattern rows, the same repo shipped twice under two names |

⭐⭐⭐ **Clause 7 is the v254 lesson in one line, and note precisely what form it takes.** The subject's script *already computes* the deduplicated set and *already prints its size* — it just never compares that number to the other number sitting right next to it. **So the clause is not "add a dedupe check." It is: wherever the script already knows a count, assert it against the count it is supposed to equal, and fail if they differ.** In vault terms: `_state/03c` entry count vs the highest `vNNN` present; `_patterns/06` §C row count vs the "51 live standalones" figure in `CLAUDE.md`; the number of `_state/` chapter files vs the rows in the shim's chapter index.

⭐⭐ **And add clause 8, from the same finding — a RENAME clause.** The list carries `ruvnet/claude-flow` when the repo is now `ruvnet/ruflo`, and `Hmbown/CodeWhale` when the vault knows it as `DeepSeek-TUI` (v72). **My own corpus-overlap check missed two vault ships for exactly this reason** until I ran a reverse pass. Any inventory keyed on a name that can change needs either a stable id or a redirect check.

### (b) Take the three-way aim lesson into `CLAUDE.md` as a rule

Write this down, because it is the sharpest formulation the corpus has produced on the subject and it took five ships to reach:

> **A gate's aim, not its quality, decides what rots (v250) — and a declaration is a form of aim (v254).**
> In this subject, three classes of fact had three fates. What the **machine** was aimed at (stars, sort order, the date stamp) is **correct and verifiable**. What the **human declared** (the "110+" agent count) is **exactly correct**, because he bumped it by hand five separate times — declaring it made him watch it. What **nobody declared and nothing was aimed at** (uniqueness, liveness, rename-freshness) is **broken**, and stayed broken through four machine rewrites of the same file.
> **Therefore: before adding a check, ask what you have never declared. That is where the rot is.** The vault's own case is exact — the chapter filename was never declared to mean anything, so it has been wrong for 71 ships.

### (c) Give `C22–C27` a `Resting` section in `_patterns/06`

**Unchanged from v253's recommendation, and v254 makes the case stronger.** The retire pass has been deferred ~66 ships because **deletion demands certainty while MOVING a row is reversible.** Use v253's form — per-entry evidence, `_(last cited vNNN, YYYY-MM)_`.

⭐ **v254 is the argument for doing it by hand rather than waiting for automation:** v253's `Resting` section is entirely hand-maintained and it correctly caught an archived project that v254's weekly CI job missed. **The hand-maintained decay policy beat the automated pipeline at the automation's own best job.** Stop waiting for the script to retire the rows.

---

## Rung 2 — the candidate pipeline (0–1 h, zero installs)

**282 unique GitHub repos. 16 are prior vault ships. 266 have never been looked at.** That is the largest, most on-goal candidate pool the corpus has ever had handed to it in one file — bigger than v253's 153.

**Highest-value slices for goal #1:**

| Slice | Entries | Why |
|---|---|---|
| **Agent infrastructure** | 87 | memory, code graphs, policy gates, provenance — the substrate layer |
| **Session managers & parallel runners** | 61 | the niche with ~20 vault ships and **still zero pilots** |
| **Orchestrators & autonomous loops** | 41 | directly on the loop-engineering v189 thread |
| **Open Source agents** | 83 | the peer set for everything the vault has read |

**Three specific entries worth a look, each verified by me:**

1. ⭐ **`johannesjo/parallel-code`** — **still the best Rung-2 install candidate, and v253's pick.** MIT, macOS+Linux, worktree isolation + a built-in diff viewer. **Its author submitted it here himself.** Appears in **both** lists. One fenced install (`install-snapshot` first, pin a release, throwaway repo, two agents on one trivial task, review both diffs) **discharges a lever the vault has carried for ~20 ships.**
2. ⭐ **`fastxyz/skill-optimizer`** — *"benchmarks SDK, CLI, and MCP guidance docs (SKILL.md) across multiple LLMs … iteratively rewrites docs until every configured model meets a PASS/FAIL score floor."* **Directly on the SkillOpt v178 thread**, and pointable at the vault's own `05 Skills/`. ⭐ **It was submitted by an AI agent** (`OpenClaw Agent (basd) <basd@openclaw.ai>`).
3. ⭐ **`Zandereins/schliff`** — *"deterministic quality linter for agent instruction files (`AGENTS.md`, `SKILL.md`, `CLAUDE.md`) … no LLM in the scoring path."* **MIT.** A linter for exactly the file class the vault's whole drift problem lives in. **Read it before writing clause 1** — it may already implement half of `bin/verify-vault-inventory.sh`.

🔴 **For every candidate: verify the licence yourself.** The list is silent on 10 of its top 20, and AGPL has cost this vault three times.

---

## Rung 3 — the ecosystem map (30 min, analysis only)

Two measurements worth keeping, both corrections to prior ships:

1. **Harness targeting, word-boundary matched over 300 entries:** Claude (any) **140 (46.7%)** · Claude Code **119 (39.7%)** · Codex **104 (34.7%)** · OpenCode 49 · Gemini 43 · Cursor 36. ⭐ **v253 concluded Codex was marginally ahead; on this larger sample Claude Code leads by 15 entries.** Both lists agree these two lead by a wide margin with OpenCode third — **that finding is now N=2 and solid.** ⚠️ It measures what authors *advertise*, not usage.
2. **Mechanisms:** **MCP 53 (17.7%)** · skills 45 · memory 28 · **worktree 26 (8.7%)** · sandbox 25. ⭐⭐ **This corrects v253's strongest generalisation** — it measured worktree at 16.1% and called it *"the load-bearing primitive of the whole category,"* with MCP at just 3.3%. **Not a contradiction, a scoping correction: parallelism is solved with git worktrees; capability is solved with MCP and skills.** The primitive depends on which problem the tool solves.

⭐ **For the overdue audit:** point #2 is **ecosystem-scale evidence for Pattern #18 sub-archetype B1-MCP (≈N=13)** — across 300 CLI-agent tools, MCP is the single most-named mechanism. That is a different kind of support than another instance, and worth recording as such.

---

## 🔴 Never

- Trust this list on licences.
- Treat presence as a safety or quality endorsement (one entry has its guardrails stripped by design).
- Point an agent at it and say *"install the best one."*
- Assume an entry marked active is alive (`lettabot` is archived) or that a listed name is current (`claude-flow`, `free-code`).
- Repeat *"fastest repo in GitHub history to 100K stars"* or the *"March 2026 Claude Code source leak"* as established fact.
- Route candidate or interview data through any tool from this list without reading it first.
- Cite the fleet's numbers: **not** 50 commits, **not** a 2026-04-06 root, **not** median 23.5 words, **not** worktree at 3%.

## ✅ May

- ⭐ **Cite v254's star figures** as CI-fetched and spot-verified within a one-week refresh window. **This reverses v253's PIN**, and it is the one thing the machinery unambiguously bought.
