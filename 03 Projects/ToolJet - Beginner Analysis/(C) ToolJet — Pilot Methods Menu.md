---
title: "(C) ToolJet — Pilot Methods Menu"
subject: "ToolJet/ToolJet"
wiki: v243
date: 2026-08-19
---

# ToolJet — Pilot Methods Menu (wiki v243)

Ranked by **value per unit of risk**. The top three cost minutes, touch nothing external, and are the
reason this wiki exists. Everything below rung 4 is optional.

---

## A1 — Symlink the vault's own agent-context files ⭐⭐⭐ *(2 minutes, zero risk, do it first)*

**The idea, borrowed verbatim from `AGENTS.md` line 3:** *"Canonical file: `AGENTS.md`; `CLAUDE.md` is
a symlink to it."*

The vault maintains `CLAUDE.md`. If it ever grows an `AGENTS.md` — and it should, because Claude Code
does not read `AGENTS.md` while Codex, Cursor and Gemini CLI do — **do not maintain two files.** Make
one a symlink to the other. A symlink cannot drift; the failure mode is removed, not policed.

```bash
cd "/Users/Cvtot/KJ OS Template" && ln -s CLAUDE.md AGENTS.md && ls -l AGENTS.md
```

**Why this direction:** `CLAUDE.md` is already the real file with all the history, so it stays the
target. Any harness that looks for `AGENTS.md` now finds the same bytes. ToolJet points the arrow the
other way (`CLAUDE.md → AGENTS.md`) because they wrote `AGENTS.md` first; the direction does not matter,
only that there is exactly one file.

⚠️ **Two caveats worth knowing before you run it.** Git stores the symlink as a 9-byte blob, which is
what you want. But ToolJet's own deployment shows the trap: **their bridge exists at 3 of the 13
directories that have an `AGENTS.md`** — the ten per-module files have no `CLAUDE.md` beside them, so
59 KB of their best context is invisible to the harness their own commit trailers prove they use. If
the vault ever adds directory-scoped context, symlink *every* level or the exercise is half-done.

---

## A2 — Add a `Flagged Ambiguities` section to `CLAUDE.md` ⭐⭐⭐ *(15 minutes, zero risk)*

**The idea:** `UBIQUITOUS_LANGUAGE.md`'s closing section is 10 entries of the form *"X appears in the
code as A, but the canonical term is B; the code name is a legacy artifact."* It is **a catalogue of
the codebase's own false friends** — written because an agent infers meaning from identifier names, and
these names lie.

The vault has the same disease. Start the section with the instance three consecutive ships have
flagged and none has fixed:

```markdown
## Flagged Ambiguities

- **`_state/03c-projects-v61-v183.md`** holds per-wiki entries through **v242**, not v183. The
  filename label lags by ~59 versions and is a historical artifact. Trust the entries, not the name.
  (Flagged at v239, v240 and v242; unfixed. Fix = rename + reference sweep, or mechanise via A3.)
- **"Pattern count 46/11"** means 46 confirmed top-level patterns and 11 CONFIRMED Library-vocab
  items — not 46 of anything else, and not the ≈56 §C surface.
- **"GA:n"** counts goal-aligned *ships*, forward-only from v126; the historical "49+3*" figure is
  frozen at v125 and is not recomputed.
- **"Audit" vs "ship"** — an audit is not a ship; it does not increment the streak.
```

⭐ **Why this is the highest-leverage documentation change available.** ToolJet's `docs/docs/widgets/`
case is *precisely* the vault's `-v183` case: a directory name that is historical while its contents
say otherwise. **Their answer to a name they could not cheaply rename was to write down that it lies,
in the file the agent reads first.** That costs fifteen minutes and immunises every future session
against an error the vault has now made three times.

---

## A3 — The label check: the ninth piece of `verify-vault-docs` ⭐⭐ *(1–2 hours, zero risk, read-only)*

Nine ships have now handed the vault parts of this tool. Build the smallest useful piece:

**Assert that every `_state/*.md` filename's declared version range matches the entries it contains.**

```bash
# sketch — for each _state/03*.md: parse the vNN-vMM range from the filename,
# grep the "**vNNN " entry headers inside, and fail if max(entry) > max(filename range).
```

**Then add ToolJet's two contributions to the same script:**

- 🔴 **The dangling-reference check.** ToolJet's `plans/widget-css-class.md` cites three companion
  documents — a PRD, a `frontend/CONTEXT.md`, and `frontend/docs/adr/0001-…` — and **all three are
  missing from the repository.** It says *"See ADR 0001."* There is no ADR 0001. Eight weeks, unnoticed.
  A link-existence check over the vault's `[[wikilinks]]` and relative paths is a dozen lines.
- 🔴 **The inventory check (v240's rule).** No `AGENTS.md` in ToolJet mentions `plans/` at all — so a
  linter comparing the context index to the code **would never have flagged that file, because it is
  absent from the index the linter reads.** The vault's equivalent: assert that every `_state/*.md` on
  disk appears in the `CLAUDE.md` chapter index, and vice versa.

⭐ **The case for automating rather than resolving to be careful is made by ToolJet's own history.**
Their 15-commit review of the agent layer includes `docs: revise glossary against current code and
docs`, `docs: align lint guidance with CI lint jobs`, and `docs: remove accidentally committed
context-mode tooling block` — **they ran the prose-vs-code check three times, by hand, and produced
genuinely excellent documentation.** The one artifact outside that review's scope rotted anyway. Care
does not scale; a script does.

---

## A4 — Fix the `anthropic` marketplace plugin (upstream PR) ⭐⭐ *(1 hour, low risk, real contribution)*

🔴 **The bug, in one line:** `marketplace/plugins/anthropic/lib/operations.json` sets
`"defaults": { "model": "claude-3-5-sonnet-20241022" }` — and the dropdown **in the same file** labels
that value `(Discontinued)`. **The plugin's out-of-the-box default is a model it itself marks as dead.**

**And the model list is two generations behind.** Newest offered: `claude-opus-4-5-20251101`,
`claude-sonnet-4-5-20250929`, `claude-haiku-4-5`. Absent: **Opus 4.6, 4.7, 4.8, Opus 5, Sonnet 4.6,
Sonnet 5, Fable 5.** Last touched **2026-05-14** (#16296) — while the sibling `openai` plugin was
updated **2026-06-18** (#16592) and does carry `gpt-5`.

**The fix is one file** (the list appears twice, under `chat` and `chat-v2`): add the current model
IDs and change the default to a current model. Use the exact ID strings — `claude-opus-5`,
`claude-sonnet-5`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-fable-5` — **with no date suffix
appended.**

⚠️ **The SDK pin is the harder half and should be a separate PR.** `@anthropic-ai/sdk: ^0.32.1` is a
caret on a `0.x` version, so it admits only `0.32.x`. That generation predates adaptive thinking,
`output_config.effort`, structured outputs and the 1M context window — the plugin could not express
those options even with the model IDs fixed. Bumping it is a real compatibility exercise, not a
one-liner. **Ship the model-list PR first; it is small, obviously correct, and immediately useful.**

⭐ **Why this rung is worth a Saturday.** It is a genuine open-source contribution to a 40k★ project,
in exactly the operator's declared area of mastery, on a file whose defect is self-evident from a
single diff. And `CONTRIBUTING.md` accepts external PRs — unlike the previous ship's subject, which
refuses them outright.

---

## A5 — Borrow the three agent skills' *rules*, not the skills ⭐⭐ *(30 minutes, zero risk)*

Do not install ToolJet's skills — they are hard-wired to a three-repository submodule layout the vault
does not have. **Lift the four rules that generalise:**

1. ⭐ **Reversibility-gated autonomy** (from `merge`): *"Do NOT ask for confirmation — merges are
   reversible with `git merge --abort`."* **This is the correct principle for when an agent should stop
   and ask, and almost nobody writes it down.** Put it in `CLAUDE.md`: *proceed without confirmation
   where the action is cheaply reversible; stop where it is not.*
2. ⭐ **Latency is not a hang** (from `commit`): *"Commit hooks can be slow — allow a generous timeout
   rather than assuming the call hung."*
3. ⭐ **Named stashes** (from `merge`): `merge-auto-stash-<timestamp>`, so a human can find what the
   agent set aside.
4. ⭐ **The `--no-verify` rule** (all three): *"**Never** force-push, reset --hard, clean, or use
   `--no-verify`. If a hook fails, fix what it reports."* The vault's loop-engineering thread already
   carries a `--no-verify` caveat; this is the rule that closes it.

⚠️ **And take the negative lesson too.** ToolJet hand-copied its most important paragraph — the shell
environment warning — into three skill files, **in a single commit**, and it already disagrees with
itself: `commit` names two coreutils, `merge` names three and numbers the constraints, and `create-pr`
**omits the rule entirely**. If the vault's skills share a preamble, put it in one file and reference
it. **A6 is the concrete case of why this matters.**

---

## A6 — Update the vault's flaky-shell memory: it is not your machine ⭐⭐⭐ *(10 minutes, zero risk)*

The vault's `project_vault_shell_flaky_workarounds.md` records the flaky shell as a local quirk. **It
is not.** ToolJet — a different organisation, a different machine, a production repo — hit the same
behaviour hard enough to write a warning into three committed skill files:

> *"The Bash tool executes in zsh via `eval`. `for` loops cause `git: command not found` — never use
> loops. Use inline per-repo commands instead. Use full paths for coreutils: `/usr/bin/head`,
> `/usr/bin/sed`, `/usr/bin/find`."*
>
> *"Always use `git -C <path>` — never `cd <path> && git`."*

**This is N=2, cross-organisation, independent, on a Claude Code execution defect** — and ToolJet
independently derived the vault's own "no `cd`" rule, in the stronger *constructive* form. Amend the
memory to record:

- the constraint is **harness behaviour, not the vault's environment** (N=2, second party = ToolJet
  `.agents/skills/*/SKILL.md`, 2026-08-18);
- **`git -C <path>`** replaces "don't `cd`" — a rule that tells you what to do instead;
- **full paths for coreutils** (`/usr/bin/head`, `/usr/bin/sed`, `/usr/bin/find`) — the workaround the
  vault did not have;
- **never `for`-loop in a Bash tool call** — inline per-target commands instead.

⭐ It bit *this analysis* twice: a `git log … | sort | head -3` returned wrong dates and a
`git log --reverse | head -8` garbled its output. Every number in this ship was written to a file and
re-read because of it. **Ten minutes here saves the next session an hour.**

---

## A7 — Stand up ToolJet CE (optional, last, and only in a scratch environment) ⚠️

Only if the operator specifically wants to evaluate the internal-tool builder itself.

**What CE actually gives you:** 49 built-in data-source connectors + 45 marketplace plugins (including
`anthropic`, `openai`, `aws-bedrock`, `pinecone`, `qdrant`, `portkey`), a visual app builder, a
workflows engine (BullMQ + `isolated-vm`), and self-hosting on Docker/K8s/Helm/AWS/GCP/Azure.

**What it does not give you:** *any* of the four marketed AI features. **AI App Generation, AI Query
Builder, AI Debugging and Agent Builder all live in the two private EE submodules** and are metered by
plan (`AI Credits` — *"per-builder monthly allocation … varies by plan"*). The CE tree ships the
ability for an app *you build* to call a model. That is a different product from the banner.

**Fence, if you do it:**

- 🔴 **Do not clone with `--recurse-submodules`.** It will fail: `ToolJet/ee-frontend` and
  `ToolJet/ee-server` are **private** (proved at the git protocol level). Use a plain clone; CE builds
  without them by design — webpack's `NormalModuleReplacementPlugin` swaps `@ee/` imports for empty
  modules.
- 🔴 **Never set `TOOLJET_WORKFLOW_SANDBOX_BYPASS`.** `.env.example` carries its own warning:
  *"Python code will run without isolation when bypassed."*
- 🔴 **Never point it at candidate or production data.** Scratch Postgres, synthetic records only.
- ⚠️ **Do not enable the committed `.gitconfig`.** Its 13 aliases (`create-branch-all`,
  `create-tag-all`, `push-all`, …) `push -u origin` across root **and both submodules** immediately.
- ⚠️ **AGPL-3.0.** Self-host it internally as much as you like; **it can never be a component of
  hireui.** Same trap as v214 firecrawl and v188 OpenMontage.
- ✅ **The one genuinely reassuring fact:** across **103 `package.json` files there is exactly one
  lifecycle script** (the root's `husky install`) — zero `postinstall`, zero `preinstall` — and every
  lockfile resolution comes from `registry.npmjs.org` with **zero mirrors**. `npm install` here is
  about as boring as a monorepo of this size gets. Still run `/install-snapshot` first.
- ⚠️ **Know the test story before you trust it:** 280,321 lines of frontend covered by **8** unit-test
  files; the server is respectable (80 specs / 35,726 lines); **122 Cypress E2E specs carry the load**.
  And CodeQL runs **weekly on a schedule and never on a pull request**, against 605 open PRs.

---

## Recommended order

**A1 → A2 → A6 → A3 → A4**, and stop there unless the operator wants the product itself.

A1, A2 and A6 together are under thirty minutes, touch nothing outside the vault, and close a
documentation defect the vault has now shipped three times plus a shell-environment misdiagnosis it has
been carrying as a personal quirk. A3 is the ninth instalment of a tool nine ships have now argued for.
A4 is a real contribution to a real project in the operator's own field of study.

**A7 is a different kind of decision and should be made on its own terms, on the product, not on this
wiki.**
