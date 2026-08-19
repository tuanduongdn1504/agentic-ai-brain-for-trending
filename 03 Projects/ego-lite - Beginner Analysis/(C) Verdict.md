# (C) ego lite — Verdict

**v247** · `citrolabs/ego-lite` · 2026-08-19 · MIT (repo) + closed-source browser binary

---

## Rating

**GOAL-ALIGNED INCLUDE — 3/4**

| Axis | Call | Why |
|---|---|---|
| **(a)** Anthropic-affiliated / registered vendor-direct | **FAIL** | CitroLabs is a company with a domain (`citrolabs.ai`) and a contact address, but no declared Anthropic affiliation. §41 forbids inference from name, heritage, locale or notability. The dominant committer is pseudonymous ("Tachikoma", `section9lab@`). |
| **(b)** Relevance to goal #1 (master Claude and autonomous agents) | **STRONG** | An agent capability layer that ships a first-class Claude Code skill, packages for four harnesses, and addresses a real limitation of the operator's daily agent: reaching authenticated web state. Cleanly on the goal-#1 substrate core — no §40 needed. |
| **(c)** Quality / depth of artifact | **STRONG** | 150 tracked files, ~26.8k lines, 23 unit-test files (~297 assertions), a 24-module real-browser e2e harness, hand-rolled mutation testing, an agent-style linter, a runtime-generated help system. ⚠️ Tempered: the distinctive machinery is in the closed binary. |
| **(d)** Readability / analysability | **STRONG** | Cleanly organised, well-commented TypeScript; an unusually good `AGENTS.md`; the open/closed boundary declared in words. |

**Streak:** v246 `GA:104` → **`GA:105 · OG:13 [7 ov]`** — **28 consecutive goal-aligned ships** (v220→v247). **§35 CLEAR** (window {v245 GA, v246 GA, v247 GA} = 0 OG).

**MINT: NO.** Counts **46/11 UNCHANGED**; §C standalones **51 unchanged**; surface ≈58 unchanged. Four grounds, detailed in the Deep Dive §10a: form-factor-within-a-genre (lobehub v222 / hermes-webui v227 decisive), a combination is not a capability class, the distinctive machinery is not in the subject, and §28 + the N=1 gate. **Collision CLEAN** (zero prior mentions). **Pattern #57: NONE.**

⭐ **Recorded, not executed:** a DEFERRED watch axis at N=1 — *"Human+Agent Shared-State Co-Habitation with Per-Workspace Ownership Handoff."* Genuinely repeatable beyond browsers (an IDE, a terminal multiplexer, a shared canvas). A promotion is an audit act. ⚠️ **Do not count this toward the palmier-pro v192 row** — it ships a skill, not an MCP server, and was built agent-first rather than retrofitted; both halves of that row's name fail.

---

## The four things that matter

**1. It declares the boundary that the last three ships hid.** The browser is closed; the repo is MIT. The README's License section and `AGENTS.md:3-5` both say so unprompted — *"provided by the closed-source ego lite app"*, *"not the browser itself"*. v244 over-asserted an identity, v245 under-asserted one, v246 split one across two repos and never mentioned the restrictive half in 44 files. **v247 splits one and says so, in the two files a reader and an agent open first. It closes the set of four, and it costs one sentence.**

**2. It writes excellent checks and does not connect them.** Its own doctrine is *"write the check first"* (`CONTRIBUTING.md` §12, Goal-Driven Execution). It then hand-rolls **real mutation testing** on `acorn`, aimed precisely at the predicates whose silent failure would hurt (`isAgentOwned`, `findMatchingTaskSpace`, `boxModelCenter`) — **wired to nothing**. It writes a linter for **agent-facing prose** — **wired to nothing**. Its skill-publish pipeline (version normalisation, a token-leak scanner over the release archive, a SHA256-pinned CLI, dry-run, post-publish verification) **triggers on a tag pattern no tag in the repo matches — it has never fired.** The one check they wired in all four places validates the site-learning data format.

**3. A committed gate that 66 of 82 merges contradict.** `main-pr-source.yml` fails any PR into `main` not sourced from `dev`. Added 2026-06-01. Since then: **82 PR merges into main, 16 from `dev`, 66 from branches the gate rejects — including HEAD.** Meanwhile `CONTRIBUTING.md:283` says *"branch from latest `main`"*, `CONTRIBUTING.md:322` says merge via `dev`, the pre-commit hook gates on `origin/dev`, and `main` and `dev` have **diverged** (32 ahead / 20 behind). ⚠️ Whether the gate is a *required* check lives in branch-protection settings, invisible in the tree — **v244's D28 in reverse: a committed CI rule is not an enforced one.** No accusation; a measurement.

**4. The best agent-facing contract in the corpus has one silence.** `SKILL.md` (209 lines) is better than v246's `llms.txt` because it governs *behaviour*: a **write-probe** discipline against silent wrong writes, a tabulated ownership model, and a rule naming deference as success — *"Honoring it is the correct outcome here; pushing the goal forward anyway is the failure."* 🔴 And **not one word about a hostile page.** The loop is *read untrusted web content → an LLM decides → it runs JavaScript against your authenticated sessions*, and `grep` for `malicious|hostile|untrusted|prompt inject` across `SKILL.md` + `AGENTS.md` + `CONTRIBUTING.md` returns **nothing**. There is no `SECURITY.md`. They reasoned carefully about one adversary — an impatient agent — and not at all about the other.

---

## Security, in one paragraph

⭐ **No broken-auth triad, structurally:** `ego-browser` opens **no port and no socket** — the transport is a function the app injects (`globalThis.ego.sendCDPMessage`). It notably declines the usual shortcut of exposing Chrome's `--remote-debugging-port`, which is exactly the failure mode this corpus documented at v231 and v232. ⚠️ The authorization model therefore lives in the closed app and **cannot be audited**. 🔴 The residual risk is the premise itself: inside a Space that inherits your logins, `js()` is arbitrary evaluation and `browserFetch()` returns authenticated response bodies — so with §6's silence, **prompt injection from page content is the entire threat model and it is unaddressed.** Two smaller items: `.env` is auto-loaded from the installed skill directory into agent-script environment (`env.ts:47-48`), and **validating a site-learning imports it** (`validate-learning-format.ts:66`), so `validate:site-skills` executes learning JavaScript in CI — correctly configured as `pull_request` (no secrets), not `pull_request_target`.

**Supply chain: mid-table with two standout practices.** ⭐ Exactly **one runtime dependency** (`acorn`, reused three ways). ⭐ `npm audit --audit-level=moderate` in both CI and the pre-commit hook. ⭐ A mutable `latest.tar.gz` URL made immutable by a **committed SHA256** — better than v246's *"pinned-but-unverified over TLS"* and far better than v234's plaintext `http://`. ⚠️ Deps are caret-ranged not pinned; `prepare` installs git hooks; and the `.dmg` is **an opaque fixed filename with no version in it**, so you cannot pin, diff, or name what you installed.

---

## PILOT: DO NOT INSTALL — and the reason is precise

The fleet's pilot pass recommended *install behind a strict fence: a profile with no ATS or Gmail login*. **That fence is correct, and it is also the refutation.**

> **The only configuration in which this is safe for you is the one that deletes the reason to use it.** Its headline feature is inheriting your real logins. Decline the Chrome migration and log into nothing sensitive, and you have a closed-source browser binary from an unidentified team driving pages you don't care about — which Playwright already does, in the open, on three platforms.

And the use case that *would* pay for itself — sourcing candidates from LinkedIn — fails on three counts:

1. **Your ratified policy.** Any LLM path touching a candidate must be fixed + legible + audited + human-in-the-loop + eval-gated. An agent free-writing JavaScript against a logged-in session, reading untrusted page content with no injection defence and no approval gate, satisfies **none** of those, and there is no read-only mode to fall back to.
2. **Account risk is asymmetric.** Automated LinkedIn access breaches its terms; the account you'd risk is your professional identity, and a ban is not reversible by a rollback.
3. **Accountability is unestablished.** The binary that would hold your sessions comes from an org whose principals are not named anywhere in the repository — and the repository is the only thing you can audit. ⚠️ For a laptop holding candidate PII that is the whole argument, independent of anyone's good faith.

**🔴 Never:** migrate your real Chrome profile into it · run it on a machine logged into the ATS, Gmail, GitHub, or a cloud console · point it at candidate data · let it touch a candidate-facing decision · cite its 2.5× or 5× numbers · treat `takeOverTaskSpace` as safe · rely on the never-fired publish pipeline's protections.

**✅ What you should actually do:** take the four ideas, install nothing. See the Pilot Methods Menu — **M1 → M2 → M3, about 40 minutes, zero installs.**

---

## The one sentence

**A team built the most thoughtful set of instructions for an AI agent in this entire corpus — including a rule that says stopping when the human intervenes is not a failure but the correct outcome — and then wrote a mutation tester, a prose linter and a token-leak scanner aimed at their own worst failure modes and wired none of them to anything, while the one gate they did commit is contradicted by sixty-six of their own last eighty-two merges.**

---

## Suggested next action

Review and merge **`wiki/v247-ego-lite`** off the v246 tip (`4321bee`) — the chain v204 → … → v246 → v247 merges in order. Then run **M1** (the write-probe rule into `CLAUDE.md`) and **M2** (test a vault gate against the history it governs — one command, and the vault has gates worth testing). ⚠️ And the standing item is now past embarrassing: **the ~v221 audit is 35 ships overdue** (last v212; v213–v247 all shipped). This ship alone hands it three items: the new watch axis, the D22 refinement, and a D28-inverse rule. **Seriously consider making v248 the audit instead of a wiki.**
