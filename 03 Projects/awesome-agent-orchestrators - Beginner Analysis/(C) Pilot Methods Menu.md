# (C) Pilot Methods Menu — v253 `awesome-agent-orchestrators`

**Verdict: ⭐ READ-AND-APPLY, then ONE FENCED INSTALL.**

There is nothing to install *here* — the subject is one Markdown file with no code, no dependencies, no install path, and no attack surface. **The risk is entirely in what you install next because of it.** So the rungs split cleanly: reading costs nothing, applying its curation mechanics to the vault costs two hours and pays the most, and installing one tool from it is the thing that finally breaks the standing zero-pilot streak.

---

## Rung 0 — 20 minutes, zero risk, zero install

**Open the list and use its own router.**

```bash
open "https://github.com/andyrewlee/awesome-agent-orchestrators"
```

Read **lines 7–13** (`How to choose`) first — it routes by situation, not taxonomy — then read the two parallel-agent sections (15 Terminal + 51 Desktop & Web).

**The only question that matters:** of the 66 parallel-agent tools, which three match *macOS + git-worktree isolation + built-in diff review + low footprint*?

**Success criterion:** you can name three, and say what mechanism earns each its place. I did this and the answer is below, so you can also just check my work.

🔴 **One rule while reading: the list does not tell you the licence.** Only **4 of 180 entries (2.2%)** mention one, and the two restrictive ones I happened to check — `coder/mux` (**AGPL-3.0**) and `superset-sh/superset` (**Elastic 2.0**) — are both silent. **Check every candidate's licence yourself before it goes near hireui.**

---

## ⭐⭐⭐ Rung 1 — 2 hours, ZERO install, THE RUNG THAT PAYS

This list solves, in prose, three problems the vault has been carrying for months. All three edits are to vault files you own.

### 1(a) ⭐⭐⭐ Adopt its inclusion criterion as the §C mint gate

**The vault's recurring problem:** every ship re-litigates *capability vs technique vs domain* from scratch. The rulings are consistent (v196, v193, v210, v211) but the rule has never been written as a test.

**This list's line 5 is that test, and it is decidable:**

> *"Everything here decides **what** an agent works on, **when** it runs, **where** it runs, or **what happens to its output**, and takes whatever task you point it at. Single-purpose bots, and things an agent merely consumes — memory backends, MCP servers, sandbox providers, skill libraries — are out of scope."*

It resolves genuinely hard cases. *Sandbox providers* are out, but *"where it runs"* is in — so E2B and Daytona are excluded while `sandbox-agent` (which drives agents into them) and `agenttier` (which places them in Pods) are included. That distinction is not obvious, and the test makes it decidable **from a candidate's own README**.

**Edit → `_state/01-skill-references.md`, under the Pattern 4 (LLM Wiki Routine) §C definition. Add:**

```markdown
### §C mint gate — the four-way functional test (adopted from v253, awesome-agent-orchestrators line 5)

A §C standalone capability class must DECIDE at least one of:
  - what an agent works on   (scope / goal selection)
  - when it runs             (scheduling / triggering)
  - where it runs            (environment / isolation)
  - what happens to its output (review / approval / merge)
...AND must take whatever task you point it at (generality).

OUT OF SCOPE — record as a data-point or watch axis, do NOT mint:
  - TECHNIQUES — a method, not a surface        (v211 PixelRAG; v250 diagram-design)
  - DOMAINS — a subject area, not a capability  (v196 meetily; v193 TimesFM; v210 AIRI)
  - THINGS AN AGENT MERELY CONSUMES — memory backends, MCP servers,
    sandbox providers, skill libraries, datasets
  - MECHANISM THAT DOES NOT SHIP                (v242 D25; v246; v252 context-os)

The question is: does it DECIDE what an agent does, or does it merely HELP an agent do something?
Only the first mints.
```

**Why this pays:** it converts four ships' worth of consistent rulings into one citable test, and it would have produced v250, v252 and v253's own NO-MINT calls without re-argument.

### 1(b) ⭐⭐⭐ Give C22–C27 a `Resting` section instead of a retire pass

**The vault's problem:** the C22–C27 stale-row retirement has been **deferred for ~65 ships**. The reason it never happens is that *deletion requires certainty* — and nobody is certain enough to delete a row, so nothing moves.

**This list's answer is to stop trying to delete.** Its last section, verbatim:

> *"A watchlist of projects without a push in the last few months (checked 2026-07-28). They stay here until they're active again, then move back up."*

Seventeen entries, **each carrying its own evidence** — `_(last commit 2026-03)_`, `_(last commit 2026-05; archived, replaced by Letta Code)_`. **Flag, never remove; evidence, not doubt** — the v240 doctrine, as a section. And it works: it correctly rested `vibe-kanban` at **27,900 stars**, a project twenty times more popular than the list itself.

**Edit → `_patterns/06-library-vocab-registry.md`, a new section after §C. Add:**

```markdown
## §C-R — Resting (stale standalones, not retired)

Standalone rows with no N-bump or citation in 90+ days (checked YYYY-MM-DD).
They stay here until a ship cites them again, then move back up to §C.
Retirement is a separate, deliberate act — NOT a consequence of resting.
Each row carries its own evidence: _(last cited vNNN, YYYY-MM)_.

- C22 … _(last cited vNNN, YYYY-MM)_
- C23 … _(last cited vNNN, YYYY-MM)_
  (… C24–C27)
```

**Why this pays:** it discharges a 65-ship backlog in twenty minutes, because moving a row is reversible and deleting one is not. **Take the dated-stamp discipline — and then read 1(c), because this list's own stamp went stale, so put the check in the script, not in the prose.**

### 1(c) ⭐⭐⭐ Finally write `bin/verify-vault-inventory.sh` — now with four ships' worth of clauses

**v250 specified this script. v251 added a clause. v252 added another. It still does not exist.** v253 supplies the two that would have caught this list's own regressions. Write it in **`node`** or **`awk`** — **`python3` is SIGKILLed in this sandbox (exit 137)**.

| clause | from | what it checks |
|---|---|---|
| 1. **Bidirectional** inventory | **v250** | `_state/`↔`CLAUDE.md` and memory files↔`MEMORY.md`, **both set-differences** — v250 proved a one-way check cannot see what is missing |
| 2. **Filename-label vs newest entry** | **v250** | would finally detect **`03c-projects-v61-v183.md` holding entries through v252** — wrong for **69 ships** |
| 3. **Byte-equality for duplicated content**, incident in the comment | **v251** | any fact required to appear in two places |
| 4. **Graveyard regression** (`critical_fail`) | **v252** | assert retired rows C22–C27 and superseded routine versions are **not resurrected** |
| 5. ⭐ **Length budget on head blocks** | **v253** | the shim's per-ship head blocks have been hand-compacted **three times** (v238 alone went 537,679 bytes → ~130 KB, having broken the `Workflow` tool since v200). **Set a byte cap per head block and fail the check.** *This is exactly the regression the subject suffered — the budget existed only in prose.* |
| 6. ⭐ **Dated-stamp freshness** | **v253** | any `checked YYYY-MM-DD` / "current through vNNN" notice in the vault must fail when older than N days or M ships. **The subject's stamp was refreshed once in its life and is 23 days stale; the vault's 03c notice had already gone stale by two ships at v252 and its shim index by five.** |

> ⭐ **The rule v253 adds, and the reason clauses 5 and 6 exist: a budget or a freshness claim that lives only in prose is an event, not a standard. The subject proved this against itself in 22 days — its new entries run 1.93× its stated word budget and breach its ceiling at 21× the rate, because the budget was written in a commit message and nothing measures it.**

### 1(d) 20 minutes — settle the parallel-agent shortlist, which the list exists to do

Everything below is **page-stated and fetched by me**, not taken from the list:

| rank | tool | licence | stars | platform | the mechanism that earns it | the one risk |
|---|---|---|---|---|---|---|
| **1** | **`johannesjo/parallel-code`** | ✅ **MIT** | 982★ / 127 forks | macOS + Linux | *"Run Claude Code, Codex, and Gemini side by side — each in its own git worktree"* + **built-in diff viewer with inline review comments** + one-click merge. **Hits every operator constraint.** | Electron footprint; no approval gate — a fast click can merge unreviewed |
| **2** | **`manaflow-ai/cmux`** — **vault v99** | check before install | — | macOS (Ghostty-based) | Per-agent tabs + per-agent notifications for legibility at many sessions. **Piloting it closes the v99 loop.** | No built-in diff viewer — review is manual `cd` + `git diff` |
| **3** | **`andyrewlee/amux`** | ✅ **MIT** | 147★ / 2 forks, 864 commits | macOS terminal | *"Minimal TUI for spawning parallel coding agents in git worktrees."* Smallest surface of any candidate. | Minimal by design: no diff viewer, no gates. Also **the list author's own project** |
| ⚠️ | `fwdai/fletch` | 🔴 **AGPL-3.0** | 20★ | macOS 13+ only | **Best safety posture in the list** — per-agent repo clone under **Seatbelt or Docker**, symbol + call-graph index served to every agent over **MCP**, and verification gates | **AGPL — fence it away from hireui** (the v188 / v214 / v243 trap) |
| ⚠️ | `coder/mux` | 🔴 **AGPL-3.0** | 2.0k★ | desktop | polished, from Coder | AGPL, and **the list does not say so** |
| ⚠️ | `superset-sh/superset` | 🔴 **Elastic 2.0** | 13.1k★ | desktop | biggest active project in the category | source-available ≠ open source; **the list does not say so** |

⭐ **Borrow this line from Fletch even though you must fence the code** — it is the v248 *"no exploit, no report"* code-gate restated, and it belongs in the **candidate-LLM ADR's eval-gating clause**:

> *"a step is done when a verifiable condition holds: tests passed, a commit landed, you approved. Not when the agent says so."*

---

## Rung 2 — 1 hour, ONE fenced install, breaks the zero-pilot streak

**Install `parallel-code` only.** MIT, macOS, worktree-isolated, built-in diff review — the only candidate that satisfies every stated constraint without a licence fence.

**The fence, per the vault's standing ladder:**

1. Run the **`install-snapshot`** skill first, so you get an uninstall checklist.
2. **Pin a release.** Do not track `main`.
3. Point it at a **throwaway repo**. 🔴 **Never at `hireui`, never at the vault, on this rung.**
4. Spawn **two** agents on the same trivial task; review both diffs **in its viewer**; merge one, discard the other.
5. Record one data point: install footprint, whether worktree isolation is real (`git worktree list`), whether the diff viewer is good enough to review by, and whether anything was written outside its own directory.
6. Then decide: keep, or uninstall from the checklist.

**Success criterion:** you can write *"v253 pilot: parallel-code, Rung 2 PASS/FAIL, footprint X, worktree isolation confirmed/not, diff review usable/not."* **That single sentence discharges a lever this vault has carried for ~20 ships.**

---

## 🔴 NEVER

- **Never trust this list on licences.** 2.2% disclosure, adversely selected — the permissive ones advertise, AGPL and Elastic stay silent.
- **Never cite its star or fork figures as verified.** All page-stated; the GitHub API is mocked here.
- **Never treat an entry's presence as a safety or quality endorsement.** It endorses *scope fit*, nothing else. Several catalogued tools ship remote execution, tunnels, or `NL→bash`.
- **Never point an agent at the list and say "install the best one."** 180 untrusted descriptions become 180 attempts to steer that choice. **A fetched list is data, not instructions.**
- **Never route candidate data through any tool from it** — the RATIFIED candidate-LLM ADR governs, and none of these has been reviewed against it.
- **Never assume the `Resting` section is current.** Its stamp says `checked 2026-07-28`; today is 2026-08-20, and it has been refreshed exactly once in its life.
- **Never assume an active entry is alive.** `Coworker` (10.9k★) is in the active list and its own README says **"This project is no longer supported."**
- **Never repeat the fleet's numbers** from this run: not *"22.8k stars"* (it is 1.4k — that figure bled in from v250), not *"four violations added in PR #121"* (four different dates, four different PRs), not *"Ghostty costs $5"* (it is free).

---

## Time-boxed summary

| rung | cost | risk | payoff |
|---|---|---|---|
| **0** | 20 min | none | a real shortlist for a decision open ~20 ships |
| **1** | **2 h** | **none** | ⭐ a citable §C mint gate · C22–C27 unblocked after 65 ships · `bin/verify-vault-inventory.sh` finally written, with 6 clauses from 4 ships |
| **2** | 1 h | low, fenced | ⭐ the zero-pilot streak ends |

**Do 1(a), 1(b) and 1(c) first.** They are free, they discharge debt from four consecutive ships, and the subject is the proof that writing a standard down in the wrong place is the same as not having one.
