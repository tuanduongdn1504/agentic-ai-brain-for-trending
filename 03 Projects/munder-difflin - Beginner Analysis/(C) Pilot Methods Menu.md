# (C) Pilot Methods Menu — v273 `munder-difflin`

> **Overall: ⭐ READ-AND-BORROW, with a fenced install available and one hard warning about your `~/.claude`.**
> This is the most directly pilotable subject in the last ten ships — it is a harness for the exact thing you already do by hand.

---

## ⚠️ Read this before anything else

Running this app **modifies your global Claude Code configuration.** `src/main/config.ts:768-790` writes `~/.claude/settings.json` with:

```
skipDangerousModePermissionPrompt: true
skipAutoPermissionPrompt: true
```

That is **global, not app-scoped.** After one launch, your own hand-typed `claude --permission-mode bypassPermissions` in an unrelated project will also stop warning you. It also writes `~/.claude.json` → `projects[cwd].hasTrustDialogAccepted = true`, reads and writes `~/.claude/skills`, and reads `~/.claude/projects`.

And `autoMode` defaults to **`true`** (`config.ts:425`), which means every agent it spawns runs `claude --permission-mode bypassPermissions`.

**If you install it, use `install-snapshot` first, and back up `~/.claude/settings.json` by hand.** You run Claude Code daily on this machine; this is a change to your primary tool, not to a sandbox.

---

## Rung 0 — Read five files, 40 minutes, zero risk ⭐⭐⭐

The whole value of this subject is available without installing anything.

| # | File | Lines | Why |
|---|---|---|---|
| 1 | `src/main/breaker.ts` — **the header comment only** | 24 | *"Claude Code exposes `--max-turns` but NO dollar ceiling, so we enforce one ourselves."* Policy/enforcement separation, a steer→constrain→stop ladder that de-escalates, `hardStop` off by default, and the Δ-velocity trap named outright. |
| 2 | `src/main/reflect.ts` — the header | 22 | **"backup-first → verify-don't-trust gate → atomic swap"** — a fail-closed check around an LLM rewriting an agent's long-term memory. Read this one twice. |
| 3 | `.github/workflows/pr-evidence.yml` | 157 | The best-reasoned CI file in this corpus arc. It documents what it *cannot* do, states the one invariant that makes `pull_request_target` safe, and obeys it. |
| 4 | `tools/check-release-links.cjs` | 104 | A gate built from a measured incident (downloads 118 → single digits), with two modes, extended after it went green on a fact it wasn't watching. **And nothing runs it.** |
| 5 | `HIVE.md` §2 "Locked design decisions" | ~40 | Five invariants with their reasons and their research citations. Decision 4 on why *not* to use a vector store is the sharpest paragraph on agent memory in the corpus. |

Add `src/main/hive.ts:1333` — the god orchestrator's system prompt, one paragraph, quoted in Rung 2.

---

## ⭐⭐⭐ Rung 1 — About us. Thirty minutes. Nineteen ships overdue.

`03 Projects/HeadFirstAndroid - Beginner Analysis/(C) proposed-verify-vault-inventory.sh` was written at **v255**. It is now **v273**. It has never run.

v272 said the reason was that running it requires someone to remember. **This ship says something more useful: it has never run because of where it lives.** A shell script in a project-analysis folder is this vault's `package.json`. The checks that actually run in this vault — the collision grep with positive controls, the two-clone `diff -rq`, the ground-truth-block rule — run because they live in **routine files that a session loads**.

So:

1. **Move it out of the project folder.** `bin/verify-vault-inventory.sh`, and drop `proposed` from the name.
2. **Put its invocation in a place that is already read.** The per-ship append in the routine is the analogue of `.github/workflows/` — it happens every ship whether anyone remembers or not.
3. **Add the clause this ship earns**, alongside v272's clause 11: *for every declared check, record where it lives and what already reads that place. A check whose only caller is a person is a one-off script, not a gate.*
4. **Then apply it to itself**: run it once, and audit the result against `_state/` on disk.

Cheap companion, ten minutes: `docs/llms-full.txt` is this subject's machine-facing summary and it has been wrong for thirteen days. **`CLAUDE.md` is ours.** The shim is 195 KB of claims that agents read and nobody re-verifies. Pick the three most load-bearing numbers in it (the counts, the streak, the §C sizes) and check them against `_patterns/06` today.

---

## Rung 2 — Borrow four things by hand, 45 minutes ⭐⭐

**(a) The 4-part dispatch contract** — paste this into the vault's fleet-prompt template. From `src/main/hive.ts:1333`:

> *"When you DISPATCH a task, write it as a 4-part contract so the agent can run autonomously: (1) OBJECTIVE — the concrete goal; (2) OUTPUT — the expected deliverable/format; (3) TOOLS — what to use or avoid, and any references to read instead of re-deriving; (4) BOUNDARIES — scope limits + the definition of done. **Pass references (file paths, message ids, board sections), not pasted content** — keep dispatches short."*

That last clause is a direct answer to **§43.2**: a ground-truth block handed to a fleet is an amplifier, and the smaller it is, the less it can amplify. It also answers the shim's own size problem.

**(b) The delegation rule that avoids duplicate agents** — same prompt: *"BEFORE you spawn anything, CHECK THE LIVE ROSTER … prefer routing to an EXISTING agent that fits … only spawn a fresh agent when no existing one is a sensible fit, **and say that you checked.** One capable owner beats a duplicate."* The "say that you checked" clause is the enforceable half.

**(c) The hook rule** — from `src/main/hooks.ts`: **in a hook you can afford to say no immediately; you cannot afford to wait for a yes.** DENY is race-free and locally computable; APPROVE must be delegated to the tool's own prompt or it will hit the shim timeout. Write this into the vault's hooks note before you ever add a hook.

**(d) The concurrency invariants, if you ever run agents on one repo in parallel** — single committer, single-writer-per-file, router-mediated delivery, atomic temp-file+rename, stale-lock clearing at 10 s. `HIVE.md` §2 has all five with reasons; `src/main/hive.ts` has the implementation.

---

## Rung 3 — hireui, 60 minutes ⭐⭐

1. **The reflector pattern for any LLM that rewrites a record.** `reflect.ts`'s three layers — lossless cold backup → verify-don't-trust gate → atomic swap, with the original left byte-for-byte on any failure and a single `condense-abort` log line — is the shape every hireui LLM write-path should have. It composes directly with the **RATIFIED candidate-LLM legibility ADR**: fixed, legible, audited, human-in-loop, eval-gated. Add *recoverable*.
2. **A dollar ceiling, not a token cap.** `breaker.ts` enforces a cost cap because the tool doesn't. hireui's first LLM feature should ship with the cap and the ladder (steer → constrain → stop, de-escalating on recovery) before it ships with the feature.
3. **The measurement discipline, taken from this subject's failure rather than its success.** Δ-of-cumulative, never a single sample as an increment — and **no performance claim in hireui without a committed measurement in the repo.** This subject published "~12ms" and "fastest in the world" across four surfaces with zero instruments; do not do that in a product a candidate relies on.
4. **The `llms.txt` lesson, applied before you have one.** If hireui ever publishes a machine-facing summary, its claims go in the same gate as its version string, or they go stale in the direction that flatters you.

---

## Rung 4 — Four greps, ten minutes ⭐

Run these against your own repositories, including this vault:

```bash
# 1. Which of my declared checks are in a place that runs them?
grep -rl "npm run\|node tools\|\.sh" .github/workflows/ 2>/dev/null; grep -o '"[a-z:]*":' package.json 2>/dev/null
```

```bash
# 2. Any gate that cannot fail
grep -rn "continue-on-error\|--passWithNoTests\||| true\|exit 0" .github/ 2>/dev/null
```

```bash
# 3. Every superlative or number I have published, so I can ask what measured it
grep -rniE "fastest|best|world|[0-9]+ ?(ms|x faster|%)" README.md docs/ 2>/dev/null | head -40
```

```bash
# 4. Machine-facing claims that no gate watches
ls docs/llms*.txt AGENTS.md CLAUDE.md 2>/dev/null && grep -rn "free\|no paid\|forever\|always" docs/llms*.txt 2>/dev/null
```

---

## Rung 5 — Install, if you want the thing itself (fenced) ⭐

**Value:** this is a working multi-agent Claude Code orchestrator with per-agent memory, mailboxes, worktree isolation, a cost breaker and a visual floor. It is the closest thing the corpus has offered to the operator's own hand-run parallel-agent workflow, as a product. 43 supporters, ~20 outside contributors merged to `main`, 35 releases in three months.

**Fence, in order:**
1. `install-snapshot` **before** anything, and `cp ~/.claude/settings.json ~/.claude/settings.json.bak` by hand.
2. `npm-security-check` the release — note `postinstall` = `electron-rebuild -f && node tools/ensure-pty-perms.cjs && node tools/patch-node-pty-conpty.cjs`.
3. Prefer the **signed release DMG** over a source build, but know that **notarisation is a best-effort `afterSign` hook that does not block a release**.
4. **Turn `autoMode` OFF in onboarding.** It is the first toggle and it defaults on. With it off, agents keep Claude's permission prompts.
5. Leave `orchestratorMaySpawn` **off** (it already is) until you have watched the floor for an hour.
6. Point it at a **scratch repository**, never the vault and never hireui.
7. Telemetry: a source build sends nothing (the PostHog key is injected only in release CI). A release build is on by default with six anonymous events — read `TELEMETRY.md` and decide.
8. Leave **Slack/webhook tunnels off**. They open a public `tunnelmole` URL into a machine running autonomous agents. Secret-gated and rate-limited, but off is better.
9. Auto-update is **on** by default (6-hour poll). Decide deliberately.
10. Pin the version you audited: **0.4.5**.

---

## 🔴 Hard NEVERs

1. **Never let it edit `~/.claude/settings.json` without knowing.** The `skipDangerousModePermissionPrompt` change is global and outlives the app. If you install and later uninstall, **check that file.**
2. **Never run it with `autoMode` on against a repository you care about** — that is `bypassPermissions` on every agent, and the documented HITL gate is exactly the prompt it removes.
3. **Never point it at the vault or at hireui.** Autonomous agents with write access, a public-tunnel option and a 12-agent roster do not belong near candidate data or your knowledge base.
4. **Never cite "the fastest memory layer in the world" or "~12ms."** There is no measurement behind either, and the project's own design document says its retrieval was never validated end-to-end.
5. **Never cite `docs/llms-full.txt` on the commercial model.** It says "Free forever; no paid tier"; the landing page sells a $20 PRO tier and a $39 team seat with a calculator.
6. **Never treat the 611 assertions as a passing test suite.** Nothing runs them, in CI or anywhere else. They may all pass; nobody has been told either way since the day each was written.
7. **Never assume `main` is what a release contains** without checking — `ci.yml`'s build job carries `continue-on-error: true`, so a release can be cut from a tree whose build was red.
8. **Never hand-edit files under `<harnessHome>/hive/agents/<id>/`.** Single-writer-per-file and single-committer are the invariants keeping `.git/index.lock` intact under concurrency; you are not the writer.

---

## The one-line answer

**Read `reflect.ts`, `breaker.ts` and `pr-evidence.yml` tonight; paste the 4-part dispatch contract into your fleet template tomorrow; and move that inventory script out of a project folder before v274.**
