# (C) Pilot Methods Menu — v261 `mranex/novel_studio`

## Verdict: **READ-AND-BORROW.** The borrowable artifact is the one the author deleted.

Do not install it: 62 unauthenticated local endpoints that read and write arbitrary project folders, and a plaintext API key with no warning. There is nothing here you need as software.

**But this is the first of the five siblings with something genuinely worth taking, and it is not code.** It is `Agent.md` plus the phase-document structure — the specification machinery — which you can only read because `git` kept what the author threw away.

---

## Rung 0 — 20 minutes, and read it in this order

1. **`git show 006e321:Agent.md`** — the 149-line, nine-section agent operating protocol. Read §4 (evidence records) and §6 (verify before claiming completion) closely.
2. **`git show 006e321:master_plan.md`** — §7 ID Convention, §8 Relationship Time Semantics, §17 Open Decisions.
3. **`git show 006e321:phase/00_app_foundation.md`**, line 156: `Basic schema tests pass.`
4. **`git ls-files | grep -c test`** → `0`.
5. **`git log -1 --format=%s`** → `Done 11 phase + code review round 2`.

⭐ Those five commands, in that order, are the entire lesson.

---

## ⭐⭐⭐ Rung 1 — 90 minutes: take the protocol, and add the one thing it lacked

`Agent.md` is better than most human-team process docs. It has a ranked source-of-truth list, a scope fence, a multi-agent handoff rule (*"continue from existing evidence instead of restarting blindly"*), a mandatory per-phase evidence record with a named field list including **what was tested** and **deviations from the plan**, a concurrent-agent filename convention, an anti-silent-skip rule, and an append-only correction discipline.

**Adopt it. Then close the hole that made all of it decorative:** every one of those nine sections is a *request to the agent*, and not one of them is a **gate**. Zero evidence records were ever written and nothing noticed.

The fix is small and it is the shape this corpus keeps arriving at:

- **Make the evidence record a precondition, not an instruction.** A phase is not done until its `Working/phase_XX_summary.md` exists. That is one `test -f` in a pre-commit hook or one CI clause — the same move as v255's inventory script and v250's decidability test: *compile the part of the protocol whose violation is checkable.*
- **Make the acceptance criteria machine-readable.** `phase/00`'s criterion was the sentence *"Basic schema tests pass."* A criterion phrased as prose in a file you will delete is not a criterion. One line of CI beats it.
- ⭐ **And the rule this subject contributes: never let a completion claim and the deletion of its specification be the same commit.** If a plan is genuinely finished with, archive it under a path the tooling still reads — the v245 **D32** move (declare which copy wins, inside the copy that loses) — rather than removing it.

**Direct application to this vault:** the `05 Skills/` shared-owner question v259 left open and v260 pointed at is the same problem one level up. Your routine deltas *are* phase documents. This subject is what happens when they stop being readable.

---

## ⭐⭐ Rung 2 — 30 minutes: two patterns for hireui's LLM path

1. **The prompt-seeding pattern, with loud reads.** `DEFAULT_PROMPTS` is a dict keyed by filename; project creation writes all six files to disk (`projects/service.py:160`); the reader **raises** if one is missing (`storage/files.py:98-104`), with an opt-in `default` parameter for callers that genuinely want a fallback. ⭐ That is the right shape for hireui's candidate-facing prompts: **versioned files on disk that a human can edit and audit, seeded from code so they always exist, and loud when they do not** — and it directly discharges part of the ratified candidate-LLM legibility ADR (*fixed, legible, audited*).
2. **Validate-then-atomically-replace.** `write_json_atomic` validates against a Pydantic schema *before* writing, then `mkstemp` + replace, with an optional backup — and it **refuses to back up without being told where** (`files.py:118-120`). Take the fail-closed precondition, not just the atomic write.

---

## Rung 3 — DECLINED

The application itself is not a hireui component and not a tool you need. Its domain (serial-novel translation) is off both goals; its value here is entirely methodological.

---

## 🔴 NEVER

- **Never install or run it** — 62 unauthenticated endpoints with filesystem read/write, and a plaintext provider key.
- **Never trust its `Verification:` command.** `pytest backend\tests tests` names two directories that have never existed.
- **Never trust `## Current Status`** as evidence of verification. The features are largely real; the *acceptance criteria* were not met, and the documents recording them were deleted.
- **Never cite "code review round 2."** A search of all 122 pack paths for `review` returns one hit, and it is a UI screen name.
- **Never copy the plaintext-API-key handling.** The plan itself required a warning; the warning does not exist.
- ⭐ **And never read this repository's clean tree as a clean history.** Its most valuable content is only in the pack. `git rev-list --objects --all` before you conclude anything about a four-commit repository.
