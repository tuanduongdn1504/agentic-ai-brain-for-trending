# (C) unlazy — Pilot Methods Menu

**v274** · `Leonxlnx/unlazy` @ `754d9a68` · MIT · zero runtime dependencies · Node ≥16

**Verdict: ⭐⭐ READ-AND-BORROW FIRST, THEN A FENCED INSTALL.** This is the most genuinely pilotable subject in a long run — 2,860 lines of readable stdlib-only Node, 64/64 tests passing on my machine, a default install that touches only the project directory, and an inspection mode I *proved* never executes. And the highest-value rungs need no install at all.

🔴 **THE ONE RULE.** `--approve` is a flag, not a human gate. There is no prompt, no confirmation, no TTY check anywhere in the code. **Never let an agent pass `--approve` on a ledger it wrote itself** — the consent boundary is real against an *inherited* ledger executed by a *human*, and meaningless when the author and the approver are the same agent.

---

## Rung 0 — Read six things (35 minutes, zero risk, do this first)

| Read | Lines | Why |
|---|---|---|
| `research/validation-protocol.md` | 81 | The strongest in-tree self-retraction in 274 subjects. §2 alone is a reusable pre-registration checklist. |
| `references/gates.md` §"Author gates that can fail" | 91-100 | Six authoring rules. This is the whole method; the code is an implementation detail. |
| `references/orchestration.md` §"Verification hierarchy" | 73-91 | Four tiers, and `:75`'s *"remains self-certification."* |
| `SECURITY.md` | 64 | A short, honest threat model for arbitrary-shell-execution-by-agent. |
| `CONTRIBUTING.md` rules 1-10 | 13-24 | Ten numbered ground rules; rule 6 is a claims-accuracy policy worth stealing verbatim. |
| `tests/self-check.mjs` | 120 | Nine CI checks whose subject is the project's own declared invariants. |

**Do not** read `gate-check.mjs` end to end on the first pass. Read `oracle()`/`signature()`/`approvalPath()` at **`:312-344`** — that is the trust boundary in 33 lines.

---

## ⭐⭐⭐ Rung 1 — The vault item (45 min, no install, highest value)

**v273 told us `(C) proposed-verify-vault-inventory.sh` has never run in nineteen ships because of *where it lives*. v274 supplies the missing half: what the file should contain, and the bug to avoid while writing it.**

unlazy's `tests/self-check.mjs` is exactly the artifact the vault needs — **a check whose subject is "am I still doing what I said I do."** Nine checks, 120 lines, no dependencies, and it runs on every push because it lives in `package.json`'s `test` script which `.github/workflows/test.yml` invokes.

**And its bug is our bug.** `self-check.mjs:95` derives its population from a hand-written list of three directory prefixes, so the two `SECURITY.md` links in SKILL.md are invisible to a check named *"every reference doc the skill links to exists."* Our inventory script's clauses are a hand-written list too.

**Do this:**

1. Move the script to `bin/verify-vault-inventory.sh`, drop `proposed` from the name.
2. Add its invocation to the **per-ship append** — the one procedure that provably runs every ship (v273's rule: put the check where something already reads).
3. **Derive every clause's population from the tree, never from a list you typed.** Three consecutive ships have now handed us this same fix from three directions:
   - **v271** — a sha256 manifest pinning all 84 files, so one comparison covers 84 by construction.
   - **v272** — a 32-line test that recurses `readdir` over `api/`, so its list cannot drift.
   - **v274** — the counter-example: a three-prefix regex that silently covers 6 of 8.
4. Add the clause v274 earns: **for every declared invariant, record whether a gate covers it *or* a habit covers it. A claim with neither is the one that rots.** Our own instance: the shim's `_state/03c` filename label, and the artifact URLs and star counts that live in prose no check reads.

⭐ **Concretely, the first three clauses to write:** (a) every `_state/` file on disk is named in the CLAUDE.md chapter index — *derived by `ls`, not by a list* (this is the v256 CLAUSE-1 failure and it recurred in `MEMORY.md` at v271); (b) every `[[wikilink]]` and relative markdown link in `_state/`, `_patterns/`, `_goals/` resolves; (c) the highest `v###` in `_state/03c` equals the version in the CLAUDE.md CURRENT HEAD block — **which would have caught my own v271→v274 numbering error in this very session.**

---

## ⭐⭐ Rung 2 — Borrow the authoring rules into our ship method (30 min, no install)

Every per-ship note in this vault makes dozens of numeric claims. unlazy's rules map onto that work almost without translation — and several are things we already do, which is itself worth recording as independent convergence:

| unlazy rule | Our practice |
|---|---|
| *"Exercise a negative check against a known positive control before trusting absence"* (`gates.md:97`) | **We do this** — the positive controls in every corpus-first grep. Independent derivation. |
| *"Measure supplied figures independently; do not copy a supplied number into `EXPECT:` as its own proof"* (`:98`) | **§43.2** — a ground-truth block is an amplifier. Same rule, arrived at from the other side. |
| *"try to refute at least one passed gate"* (`orchestration.md:35`) | **Our `loop-verifier`** maker/checker split. |
| *"Re-measure every number and completion claim immediately before reporting"* (`SKILL.md:72`) | **New for us as a hard step.** Adopt it — it is the rule that would have caught error 1 and error 4 in this ship. |
| *"A checked box with missing or pending evidence counts as unmet"* (`SKILL.md:28`) | **New.** Directly applicable to our own NOT-ESTABLISHED discipline. |
| *"Do not silently remove an impossible gate — `ABANDON: <id> <reason>` and surface it in the final report"* (`SKILL.md:30`) | **New and valuable.** Our deferred items vanish quietly; an abandonment with a reason is louder. |

⭐ **The single best sentence to paste into `CLAUDE.md`:** *"The checker proves only the declared command oracle. It cannot infer whether an English gate title describes what the command actually measures."* Substitute "grep" for "checker" and it is our own standing hazard.

---

## ⭐⭐ Rung 3 — hireui (60 min, no install)

The gate ledger is a natural fit for the **RATIFIED candidate-LLM legibility ADR** (any hireui LLM path touching a candidate must be fixed, legible, audited, human-in-loop and eval-gated).

- Write `GATES.md` for the **Match-Explain** feature *before* the first LLM call ships. Each ADR requirement becomes one gate with a runnable oracle where possible and an explicit manual gate where not.
- Steal the **evidence discipline** verbatim: record resolved environment, exit status and decisive output — not a full log. That is exactly what an audit trail for a candidate-facing decision needs.
- Steal `ABANDON:` for the BOLA-audit backlog: an abandonment with a named reason and a handoff is strictly better than a TODO.
- ⚠️ Do **not** wire `gate-check.mjs` into hireui CI on a pilot. Borrow the format; the runner is a 13-day-old single-maintainer dependency.

---

## Rung 4 — The 10-minute audit of our own gates

```bash
grep -rn "stop_hook_active" ~/.claude/ 2>/dev/null | head
```

Then, for each check the vault declares: **name the place it lives, and name what already reads that place.** A check whose only caller is a person is a one-off script (v273). A check whose population is a list you typed is a partial check (v274).

---

## Rung 5 — The fenced install (only after Rungs 0-2)

**Risk profile, measured rather than assumed.** A **default** install writes only inside the project: `.claude/settings.local.json` (modified), `.claude/settings.local.json.unlazy.bak` (created), `.unlazy/` and `.unlazy-hook-state.json` (created at runtime). Approvals go to `~/.unlazy/approved` — **outside** the project — but **only** when you first run `--approve`, never by installing. Uninstall preserves unrelated hooks (4 installer tests cover this; I watched them pass).

```bash
# 1. Snapshot first — invoke the install-snapshot skill before anything else.

# 2. Clone at a pinned commit. There are ZERO tags, so a commit is the only immutable pin.
git clone https://github.com/Leonxlnx/unlazy.git /tmp/unlazy-trial
cd /tmp/unlazy-trial && git checkout 754d9a68109e39b836cc72a39fb9a823f9d6b613

# 3. Verify it yourself. No dependencies to install — this is the whole point.
npm test        # expect: 26/26, 19/19, 10/10, self-check ok (9/9)

# 4. Read the trust boundary before running anything against your own work.
sed -n '312,344p' scripts/gate-check.mjs

# 5. Use it on a SCRATCH repo, in the only always-non-executing mode.
cp templates/gates-leaf.md /tmp/scratch/GATES.md
node /tmp/unlazy-trial/scripts/gate-check.mjs --status /tmp/scratch/GATES.md
```

**Then stop and decide.** Steps 1-5 give you the entire method with **zero** mutation of your Claude Code configuration.

**If you go further — the fence:**

- ✅ `UNLAZY_APPROVAL_DIR=/tmp/unlazy-approvals` while trialling, so approvals never accumulate in `$HOME`.
- ✅ Default (local) hook install only. **Never `--global`.**
- ✅ Add `.unlazy/`, `.unlazy-hook-state.json`, `.claude/settings.local.json*` to the project's ignore rules *before* installing the hook.
- ✅ Diff `.claude/settings.local.json` before and after. Keep the `.unlazy.bak`.
- ✅ Approve **one oracle at a time**, reading the printed resolved command, CWD, shell and PATH each time.
- ✅ Use `--reverify`, never `--status`, to check returned work.

🔴 **NEVERs:**
- Never let an agent run `--approve` on a ledger it authored.
- Never `--global`, and never `--shared` (embeds absolute machine paths into a committed file).
- Never point it at this vault or at hireui on a first trial.
- Never trust `--status` to detect that an oracle changed — it does not revalidate evidence, by design.
- Never cite the six-run comparison numbers. The project retracted them in five documents; repeating them would be repeating a claim its own author withdrew.
- Never read `$?` through a pipe when checking exit codes (my own D41 slip this session).
- Never treat the green 3-OS matrix as evidence of Windows correctness — the win32 timeout path leaks descendants and no test covers it.

---

## What I would actually do

**Rungs 0, 1 and 2, and skip the install.** The runner is good — better than I expected, and it survived my attacks — but it is 13 days old with one maintainer and three open PRs fixing real defects. The *method* is the asset, it is fully readable in 35 minutes, and Rung 1 converts it into the vault's own long-deferred gate.

⭐ The sharpest thing this subject offers is not the tool. It is that a developer with a 79,622-star repository containing zero tests wrote a 1,468-star repository with sixty-four, **because the second one claimed to be about verification** — and then still left the one claim that lives outside his own files pointing at a thing he had retracted on day one.
