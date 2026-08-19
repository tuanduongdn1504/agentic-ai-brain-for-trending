---
title: "(C) ToolJet — Deep Dive"
subject: "ToolJet/ToolJet"
wiki: v243
date: 2026-08-19
author: Claude (Opus 5) — (C) AI-generated
method: SOURCE-CLONED (full history + full working tree)
---

# ToolJet — Deep Dive (wiki v243)

> **What this is.** `github.com/ToolJet/ToolJet` — an AGPL-3.0 open-source platform for building
> internal tools, dashboards, workflows and (in the paid tier) AI agents. The repo brands itself
> *"the open-source foundation of ToolJet AI."*
>
> **Why the vault read it.** Not for the low-code product. On **2026-08-18 — the day before this
> analysis — ToolJet committed a complete, harness-agnostic agent-context layer**: `AGENTS.md` as
> the canonical file with `CLAUDE.md` as a literal filesystem **symlink** to it, three git-workflow
> agent skills, ten per-module context files, and a 117-term disambiguation glossary. Its git history
> also carries **905 `Co-Authored-By: Claude` trailers**, model version by model version.
> This is a production engineering organisation's real Claude configuration, in the open.

## 0. Method and provenance of this analysis

✅ **SOURCE-CLONED.** Two clones were used, deliberately:

| Clone | Purpose | Contents |
|---|---|---|
| `tj` | all file reading | `--depth 1 --single-branch main`, HEAD `2f7638c2d7bb0a6eca2e160b687ac994cc8c08e3`, 11,407 tracked files, 2.4 GB checked out |
| `tj-hist` | all history/metadata | `--filter=blob:none`, full 17,101-commit history, no blobs |

**HEAD verified against the live remote**: `git ls-remote --heads … main` returns
`2f7638c2d7bb0a6eca2e160b687ac994cc8c08e3` — the same commit. Subject line:
`chore: update version to 3.21.61-beta across all components (#17558)`, 2026-08-18 11:11 +0530.

⚠️ **§37.4 — the GitHub API is mocked in this environment.** Every star / fork / watcher / issue
figure below is **page-stated**, not API-verified, and **is not a Pattern #52 viral-velocity claim.**

⚠️ **Two counting disciplines were required by this subject and are declared everywhere they matter:**

- **The population.** `git log HEAD` (main, 17,101 commits) and `git log --all` (1,271 refs,
  25,613 commits) differ by **8,512 commits — 33%**. Every count below states which.
- **The unit.** ToolJet squash-merges: **6,087 of 17,101 subject lines (35.6%) end in `(#NNNN)`.**
  A squash concatenates every underlying commit's message, so a grep over commit **bodies** counts
  **pre-squash commits**, not commits. Both numbers are given, labelled.

## 1. Identity — verified from source

| Fact | Value | How verified |
|---|---|---|
| Repository | `ToolJet/ToolJet` | clone |
| Organisation | **ToolJet Solutions Inc** | `LICENSE`, README footer |
| Founder / CEO | **Navaneeth Padanna Kalathil** | root commit author `navaneeth <navaneethpk@outlook.com>`; name from web |
| Licence | **AGPL-3.0** | `LICENSE` |
| Licence history | GPLv3 `2021-06-04` → **AGPL `2021-09-28`** (`b51550b56`, PR #854, "Switch to AGPL license") | `git log -- LICENSE` |
| Version at HEAD | **`3.21.61-beta`** | `.version`, HEAD subject |
| Tags | **722** | `git tag \| wc -l` |
| Remote refs | **1,271** | `git ls-remote --heads` |
| Page-stated ⚠️ | ~40.4k ★ / 5.4k forks / 200 watchers / 551 open issues / **605 open PRs** | repo page |
| Investment | **M12 (Microsoft's venture fund) + GitHub**, announced July 2023 | web (BusinessWire) |
| Anthropic affiliation | **None.** Criterion (a) FAILs under routine §41 — no declared affiliation, no registered vendor-direct axis, and no name/locale inference is permitted | — |

### 1.1 It began as a Ruby on Rails application

The root commit is not what a reader of today's README would expect:

```
e6dcdcf3d  2021-03-31  navaneeth <navaneethpk@outlook.com>  "Initial commit for rails API"
```

The root tree contains `Gemfile`, `Gemfile.lock`, `Rakefile`, `config.ru`, `.ruby-version`. The
second commit, the same day, is `"Initial commit for react app"`. Then:

| Date | Commit | Event |
|---|---|---|
| 2021-03-31 | `e6dcdcf3d` | Rails API + React app, one root commit |
| 2021-07-08 | `b68c56a16` | `"Initial commit for nestjs"` |
| 2021-07-31 | `a2a46bb8e` | `"Remove Rails files 👋"` |

**ToolJet ran on Rails for about four months and has run on NestJS for five years since.** One root
commit, no rewrite, no grafted history — the pivot is visible in the record.

### 1.2 Provenance shape (population: `HEAD`/main unless stated)

| Metric | Value |
|---|---|
| Commits | **17,101** (13,800 non-merge, 3,301 merges) |
| Commits, all refs | **25,613** |
| Root commits | **1** |
| Span | 2021-03-31 → 2026-08-18 (**~5.4 years**) |
| Distinct author names | **711** |
| Commits per year | 2021: 1,864 · 2022: 1,828 · 2023: 2,241 · 2024: 2,900 · **2025: 5,051** · 2026: 3,217 (partial) |
| Company-domain commits | `tooljet.com` 786 + `tooljet.io` 191 = **977** |
| Other domains | `gmail.com` 11,801 · `users.noreply.github.com` 3,033 · `outlook.com` 1,134 |
| Squash-merge signature | **6,087 / 17,101 subjects (35.6%)** end `(#NNNN)` |

Top authors on main: Adish M 1,345 · navaneeth 1,060 · Johnson Cherian 957 · Shaurya Sharma 762 ·
Nakul Nagargade 692. No single-author concentration; this is a real multi-year team.

⚠️ **Note the contrast with the previous ship.** v242 (deepseek-harness) inherited a third-party
claim of a *"squashed-merge, contributor-hostile"* history and **refuted** it — zero `(#NNNN)`
suffixes. ToolJet genuinely does squash-merge, in 35.6% of its history, and it **materially changes
a headline number** (§3.2). The lesson from v242 was that an unverified caveat is hearsay; the lesson
here is that the same mechanism, when it *is* present, must be measured rather than assumed absent.

## 2. The architecture, and the thing it caused

### 2.1 Three editions, two of them behind a locked door

`AGENTS.md`, verbatim:

> *"Three editions: `ce` (community), `ee` (enterprise), `cloud`. Controlled by `TOOLJET_EDITION` env var."*
> *"Cloud is a deployment config of EE, not a third code tree."*

`.gitmodules` at HEAD:

```ini
[submodule "frontend/ee"]
	path = frontend/ee
	url = https://github.com/ToolJet/ee-frontend.git
	branch = lts-3.16
[submodule "server/ee"]
	path = server/ee
	url = https://github.com/ToolJet/ee-server.git
	branch = lts-3.16
```

🔴 **Both submodule repositories are private.** Verified at the git protocol level, not from a web
page:

```
git ls-remote https://github.com/ToolJet/ee-server.git
  → fatal: could not read Username for 'https://github.com': terminal prompts disabled
git ls-remote https://github.com/ToolJet/ee-frontend.git
  → fatal: could not read Username for 'https://github.com': terminal prompts disabled
git ls-remote --heads https://github.com/ToolJet/ToolJet.git main      ← control
  → 2f7638c2d7bb0a6eca2e160b687ac994cc8c08e3	refs/heads/main
```

**So `git clone --recurse-submodules https://github.com/ToolJet/ToolJet` cannot succeed for anyone
outside the company.** The public tree declares two paths it cannot populate.

**This is not, by itself, a criticism.** It is a clean open-core layout, and the CE build is designed
to work without them — `AGENTS.md` documents the mechanism precisely:

> Backend, *"Edition pattern: **inheritance**"* — `SubModule` base class, and `getImportPath()`
> *"routes to `src/modules/` (CE) or `ee/` (EE/Cloud) based on `TOOLJET_EDITION`"*.
>
> Frontend, *"Edition pattern: **composition** via registries + webpack module replacement"* —
> `NormalModuleReplacementPlugin` *"replaces `@ee/` and `@cloud/` imports with empty modules for
> lower editions (compile-time isolation)"*, and the invariant *"Never import `@ee/` or `@cloud/`
> from CE code — webpack enforces this at compile time."*

⭐ **An architectural rule with a mechanical enforcer, not a code-review convention.** That is the
right way to hold an open-core boundary, and it is worth borrowing on its own.

The submodule branch is pinned to **`lts-3.16`** while main ships `3.21.61-beta`. Both `lts-3.16` and
`develop` exist as real remote branches — which is why the `merge` skill has to say out loud
*"ToolJet's default base is `lts-3.16`, not `develop`."*

### 2.2 The private split created a three-repository fan-out problem — and ToolJet solved it twice

This is the spine of the whole repository, and it is fully dated in the record.

| Date | Commit | Event |
|---|---|---|
| **2025-02-25** | `5bdfbe6de` | *"Adding sub-modules and Ops changes"* — `.gitmodules` created. **The problem is born:** every git operation now spans root + `server/ee` + `frontend/ee`. |
| **2025-02-26** | `a32580f14` (#12050, Adish M) | *"Adding .gitconfig with git alias commands"* — **12 fan-out aliases. Solved for humans, the next day.** |
| 2025-02-27 | `a45744a89` (#12061) | 13th alias (`status-all`) |
| 2026-03-19 | `9bbb1dc09` | `.claude/worktrees/dreamy-satoshi` gitlink **leaks into the repo**; removed, and `.claude/` gitignored. Trailer: `Co-Authored-By: Claude Sonnet 4.6`. |
| **2026-08-18** | `e416bc08e` (#17315, Akshay) | *"Docs: add agent context files and git workflow skills"* — **the whole agent layer. Solved for agents, ~17.7 months later.** |

The committed `.gitconfig` holds **13 aliases**: `checkout-all`, `pull-all`, `add-all`,
`create-branch-all`, `create-feature-all`, `create-hotfix-all`, `create-release-all`,
`create-revamp-all`, `create-sprint-all`, `create-tag-all`, `commit-all`, `push-all`, `status-all`.
Every one is built on `git submodule foreach` and shell control flow.

⭐⭐⭐ **The agent skills are not a port of the human aliases. They are a reimplementation under a
constraint the human toolkit never had** — and the skills say so, in a block that appears in all
three of them:

> **"IMPORTANT: The Bash tool executes in zsh via `eval`. `for` loops cause `git: command not found`
> — never use loops. Use inline per-repo commands instead. Use full paths for coreutils:
> `/usr/bin/head`, `/usr/bin/sed`."**

and, as a numbered rule in two of the three:

> **"Always use `git -C <path>` — never `cd <path> && git`."**

**The human tool depends on the exact construct the agent tool forbids.** Same problem, same team,
same repository, two incompatible implementations — because the executor changed.

⭐⭐ **This matters to the vault directly, and it is the finding with the shortest path to use.**
The vault's own memory carries `project_vault_shell_flaky_workarounds.md`: *"zsh drops stdout … no
`cd` … QUOTE absolute paths … route output to a file."* The vault has been treating this as its own
environmental flakiness. **It is not.** ToolJet — a different organisation, a different machine, a
production repo — hit the same behaviour hard enough to write a warning block into three committed
skill files, and **independently derived the same "no `cd`" rule**, in the stronger constructive form
(`git -C <path>`). This is **N=2, cross-organisation, independent, on a Claude Code execution
defect.** It also bit *this analysis* twice: a `git log … | sort | head -3` returned wrong dates, and
a `git log --reverse | head -8` garbled its output. Every number in this document was therefore
written to a file and re-read.

## 3. The agent-context layer

**Age, stated precisely — because it took two attempts to get right.** On main, every file in this
section arrives in **one commit, `e416bc08e`, 2026-08-18** — the day before this analysis (verified
per-file: `git log --reverse -- <path>` returns `e416bc08e` for all of `AGENTS.md`,
`UBIQUITOUS_LANGUAGE.md`, `server/AGENTS.md`, `frontend/AGENTS.md`, all three `SKILL.md`,
`server/docs/*`, and the per-module files). But that commit is a **squash of 15 commits**, and the
original — `75eef168d`, *"docs: add agent-agnostic AI context files (AGENTS.md)"*, Akshay Sasidharan —
is dated **2026-07-28**. It is **not an ancestor of main** (`git merge-base --is-ancestor` → false);
it survives on exactly one branch, `origin/test/abilities-and-guards-test-suite-update`.

⭐ **So: authored 2026-07-28, iterated over ~3 weeks across 15 commits, squash-merged onto main
2026-08-18.** New either way — but three weeks of review, not a one-day drop. And the 15 bullet
subjects preserved in the squashed body are a **visible self-correction log**:

> `* docs: revise glossary against current code and docs`
> `* docs: prune glossary aliases to genuine collisions only`
> `* docs: clarify Cloud is a deployment config of EE, not a third code tree`
> `* docs: merge testing philosophy and conventions into one file`
> `* docs: align lint guidance with CI lint jobs and forbid --no-verify`
> `* docs: remove accidentally committed context-mode tooling block`

⭐⭐ **Three of those fifteen are the prose-versus-code check, performed by hand** — revising the
glossary against the code, aligning the lint doc to the actual CI jobs, and catching their own
accidental leak of agent tooling. That is exactly what v240's build does in CI. **Hold onto this: it
is the evidence that makes §3.6 an argument rather than a complaint.**

### 3.1 The structure: a canonical file and symlinked views of it

```
AGENTS.md                                  ← real file, 5,898 B, canonical
CLAUDE.md                    → AGENTS.md   ← symlink (9 bytes)
frontend/AGENTS.md  (8,081 B) ; frontend/CLAUDE.md → AGENTS.md
server/AGENTS.md    (9,208 B) ; server/CLAUDE.md   → AGENTS.md

.agents/skills/commit/SKILL.md      (5,070 B)  ← real files, canonical
.agents/skills/merge/SKILL.md       (8,070 B)
.agents/skills/create-pr/SKILL.md  (11,657 B)
.claude/skills/{commit,merge,create-pr} → ../../.agents/skills/{…}   ← symlinks

server/src/modules/{app,apps,auth,data-queries,data-sources,git-sync,
                    group-permissions,licensing,versions,workflows}/AGENTS.md   ← 10 files, 59,088 B
UBIQUITOUS_LANGUAGE.md             (21,069 B, 117 terms)
server/docs/agents-module-template.md ; server/docs/testing.md
```

**≈128 KB across 20 files.** The convention is documented in the first paragraph of `AGENTS.md`:
*"Canonical file: `AGENTS.md`; `CLAUDE.md` is a symlink to it."*

⭐⭐ **Why the symlink is the right primitive, and not merely a tidy one.** Claude Code does not read
`AGENTS.md` natively (the vault already holds this pin, from
`project_github_copilot_cli_agents_pilot_thread.md`, referencing anthropics/claude-code issue #6235).
The usual workaround is to keep two files and try to remember to update both. ToolJet's answer is
structural: **a symlink cannot drift from its target.** One file to write, two names served, zero
possibility of disagreement. This is the cleanest available answer to v241's **D22 — *agent-facing
prose goes stale first*** — because it removes the *possibility* of the failure rather than
policing it.

⚠️ **The bridge is built at 3 of the 13 directories that have an `AGENTS.md`.** Root, `frontend/`
and `server/` get a `CLAUDE.md`; the **ten per-module files do not**. Claude Code picks up nested
`CLAUDE.md` files as it works in a directory — so **59 KB of ToolJet's most specific, highest-value
context is invisible to the harness the trailers show they actually use.** The design is right and
the deployment is 3/13.

`AGENTS.md` also declares a precedence rule, which is the part most teams never write down:

> *"Context is layered — the closest file to the code you're changing wins."*

followed by a seven-row table mapping each file to its scope.

### 3.2 The trailers: 905 of them, and ToolJet did not ask for a single one

**Population: `HEAD`/main. Unit: declared on every row.**

| Measure | Value |
|---|---|
| **Distinct commits** carrying ≥1 `Co-Authored-By: Claude … <noreply@anthropic.com>` | **165** (0.96% of 17,101) |
| **Trailer lines** across those 165 commits | **905** |
| Mean trailers per commit | **5.48** |
| Most in a single squashed commit | **143** (`53c6a1478`) |
| Trailer lines on **all refs** (`--all`, 25,613 commits) | **1,412** |
| `Claude-Session: https://claude.ai/code/session_…` trailers | **11** |

The 165-vs-905 gap **is** the squash mechanism: one commit absorbed 143 AI-assisted commits' worth of
trailers. **905 is therefore a good estimate of pre-squash AI-assisted commits and a 5.5× overstatement
of AI-touched commits.** Reporting "905 Claude-co-authored commits" would have been wrong by that factor.

**The model census** (905 trailer lines on main, families merged across case and the `(1M context)` variant):

| Model named in the trailer | Lines |
|---|---:|
| Claude Opus 4.6 | **378** |
| Claude Opus 4.8 | **231** |
| Claude Opus 4.7 | **122** |
| Claude Sonnet 4.6 | 59 |
| Claude Fable 5 | 58 |
| Claude Opus 4.5 | 38 |
| Claude Opus 5 | 8 |
| Claude Sonnet 5 | 4 |
| Claude Sonnet 4.5 | 1 |
| unversioned `Claude` | 6 |
| **Total** | **905** |

⭐ **586 of the 905 (64.8%) name the `(1M context)` variant.** Adoption over time, from the first
trailer (`b0c63a64c`, 2025-07-10) onward: 2025-07: 1 · 2025-11: 1 · **2026-01: 30 · 02: 15 · 03: 11 ·
04: 29 · 05: 32 · 06: 34 · 07: 8 · 08: 4.** Against monthly commit totals that is roughly **6–8% of
commits from January 2026 on**, having been ~0 before.

**And the other vendor.** On main: **130 Copilot trailer lines** — `Copilot <175728472+Copilot@…>` 82,
`Copilot <copilot@github.com>` 21, `Copilot Autofix powered by AI` 16, `copilot-swe-agent[bot]` 11.
On all refs: 156.

⭐⭐ **So a company that took investment from Microsoft's M12 fund and GitHub carries roughly seven
Claude trailers for every Copilot trailer on its main branch (6.96 : 1), and nine to one across all
refs (9.05 : 1).** Stated as a fact about attribution trailers, which is all it is — it is not a
statement about lines of code, and a trailer marks assistance, not authorship.

⭐⭐⭐ **The correction that matters: ToolJet gets no credit for any of this.** A grep for
`Co-Authored-By`, `Claude-Session`, or `noreply@anthropic.com` across `.agents/`, `.claude/`, all
thirteen `AGENTS.md` files, `UBIQUITOUS_LANGUAGE.md`, `.github/`, `.husky/`, `.gitconfig` and
`CONTRIBUTING.md` returns **zero hits.** The `commit` skill — the one place a provenance policy would
live — says nothing about trailers at all. **These 905 trailers are Claude Code's own default
behaviour, left on.** My first reading of this repo credited ToolJet with the strongest AI-provenance
practice in the corpus; that reading was wrong and is withdrawn.

⭐ **The finding survives in a better form.** Precisely *because* nobody wrote a policy, the record is
**uncurated**: no selection effect, nobody performing for posterity. It is accidental longitudinal
telemetry of one engineering organisation's real Claude usage — which model, which context window,
which month — and it is more evidentially trustworthy than a designed disclosure would be. Set against
the corpus:

| Ship | Mechanism | Deliberate? | Durability |
|---|---|---|---|
| **v239** dsh-web-ui | a PR-form field naming Claude Code | **yes**, required metadata | lives in the PR, not the commit |
| **v242** deepseek-harness | branch-name prefix (`codex/` 211, `claude/` 3) | no — incidental | permanent in merge subjects; marks tooling, not authorship |
| **v243 ToolJet** | commit trailer naming the **model version**, + 11 session URLs | **no — a default nobody turned off** | permanent, immutable, model-versioned |

**The richest data came from the mechanism nobody designed.**

### 3.3 The three skills are good, and they drifted on the day they were born

All three share one house template: frontmatter → `$ARGUMENTS` parsing → **Shell environment notes**
→ Phase 1 Analysis → Phase 2 Execution → a specified summary table → Rules → **Related skills**
(a cross-linked skill graph).

The `commit` skill's substance:

- **Fan-out order is a rule, with its reason**: *"always server/ee → frontend/ee → root (submodules
  before root so pointers can be updated)"*, and the pointer bump is *"a separate commit in root with
  message `chore: update submodule pointers`."*
- **Non-destructive default**: *"if files are already staged, commit only those — don't add more."*
- **Safety rails**: *"**Never** force-push, reset --hard, clean, or use `--no-verify`. If a hook
  fails, fix what it reports."* (The vault's own loop-engineering thread carries a `--no-verify`
  caveat; ToolJet writes the rule.)
- **Message policy**: conventional prefixes, subject <72 chars, *"No file lists, no function names
  unless they ARE the change."*
- ⭐ **A harness-behaviour instruction**: *"Commit hooks can be slow — allow a generous timeout rather
  than assuming the call hung."* Teaching the agent not to misdiagnose latency as a hang is a level of
  care most skill files never reach.

The `merge` skill adds the best single line in the set:

> ⭐ **"Do NOT ask for confirmation — merges are reversible with `git merge --abort`."**

**Autonomy granted on the basis of reversibility.** That is the correct principle for deciding when an
agent should stop and ask, and it is rarely written down anywhere. It also uses **named stashes**
(`merge-auto-stash-<timestamp>`) so a human can find what the agent put aside, and it
*"continue[s] through all repos even if one has conflicts — report everything at the end."*

`create-pr` opens its description with **`TRIGGER when:`** — the trigger-first convention the vault
already holds from `project_pocock_writing_great_skills_pilot_thread.md`. The other two do not. It
also mandates an emoji-headed PR body (`📝 What this does`, `🏗️ Architecture`, `🔌 API Reference`,
`🧪 How to test`) and requires `gh` *"authenticated against both ToolJet and the submodule repos"* —
the private-submodule dependency reaching all the way into the PR flow.

⚠️ **And now the defect, which is exact.** The "Shell environment notes" block — the most important
paragraph in the set, the one that encodes the environment constraint — was **hand-copied into three
files and already disagrees with itself**:

| Skill | zsh/`eval` | never loop | full-path coreutils | which coreutils named |
|---|:--:|:--:|:--:|---|
| `commit` | ✓ | ✓ | ✓ | `head`, `sed` |
| `create-pr` (the largest, 11,657 B) | ✓ | ✓ | **✗ missing entirely** | — |
| `merge` | ✓ | ✓ | ✓ | `head`, `sed`, **`find`** |

**All three were created in the same commit.** ToolJet built a symlink so that `AGENTS.md` and
`CLAUDE.md` *could not* diverge — and in the same breath duplicated a rule by hand into three files,
where it diverged immediately. Their own `AGENTS.md` says **"Stale context is worse than no context."**

### 3.4 `UBIQUITOUS_LANGUAGE.md` — the best artifact in the repository

**117 term rows**, three columns (`Term | Definition | Also appears as`), thirteen topical sections,
a `Relationships` section, and a closing **`Flagged Ambiguities`** section of **exactly 10 entries**
(222 lines total; counted `grep -c '^- \*\*'` — a workflow agent reported 12 while enumerating 10, and
my own first pass said 11). Its own editorial rule, verbatim:

> *"The 'Also appears as' column maps only names that genuinely occur in code, docs, or issues (legacy
> names, overloaded terms) back to the canonical term — **it is a translation map, not a synonym
> list.** '—' means the term has no known collision."*

⭐⭐⭐ **This is not a glossary. It is a catalogue of the codebase's own false friends** — the places
where an agent that trusts identifier names will be actively misled. A sample of the ten:

- **`Organization` (entity, columns, tables) = "Workspace" (all UI and docs).** *"The code entity name
  is a legacy artifact."*
- **`docs/docs/widgets/` contains content that says "Components".** *"The `widgets` folder name is
  historical. Use **Component** everywhere."*
- **Licence code counts `editor` / `viewer`; the product says Builder / End User.**
- ⭐ **Plan IDs lie about plan names**: *"`basic` = **Basic** (the free tier), `flexible` = **Pro**,
  `business` = **Team**, `enterprise` = **Enterprise**."* An agent reasoning about pricing from
  `flexible` would be wrong in a way nothing in the code would reveal.
- ⭐ **"Branch" is now three different things** — a `Workspace Branch` entity, a branch-head Version
  (`versionType: BRANCH`), and a plain git branch. *"never use bare 'branch' for an app Version."*
- **`Event` (component interaction) vs `Trigger` (starts a Workflow)**: *"Do not use them
  interchangeably."*
- **`Module` is "heavily overloaded"** — a NestJS module in the backend, a reusable app building block
  in the frontend.

⭐⭐ **The vault has this exact disease, and ToolJet's `widgets/` case is literally the same class of
it.** `_state/03c-projects-v61-v183.md` holds entries through **v242** — a filename that lies about
its contents, flagged by three consecutive ships and fixed by none. **ToolJet's answer to a name it
cannot cheaply rename is to write down that it lies, in the file the agent reads first.** Combined
with §3.1 the rule generalises cleanly: **rename what you can, symlink what you must, and document
the rest where the agent looks first.**

### 3.5 The doctrine — and the missing enforcer

`AGENTS.md` closes with a policy, verbatim:

> **"Living-docs rule:** when you meaningfully change a module (new service, changed invariant,
> renamed concept, new gotcha discovered), update its `AGENTS.md` in the same PR. If the module has
> none yet, create one from `server/docs/agents-module-template.md`. Introducing or renaming a domain
> term means updating `UBIQUITOUS_LANGUAGE.md` in the same PR — every glossary term should map to a
> real code identifier or user-facing feature. **Stale context is worse than no context.**"

Three things are right about this: the update is **required in the same PR** (not a backlog item),
there is a **template** to create a missing file from, and the closing sentence is the correct
principle stated in seven words.

🔴 **Nothing checks it.** There is no linter, no CI job, and no script anywhere in `.github/workflows/`
or the `package.json` scripts that verifies any `AGENTS.md` against the code it describes. And the
consequence is already visible in the tree.

### 3.6 The orphan: what a policy without a check looks like eight weeks later

`plans/` contains **exactly one file**, `plans/widget-css-class.md`, added **2026-06-24**
(`8451da269`, PR #16851). It is a genuinely impressive document — a phased implementation plan with a
*"Durable decisions that apply across all phases"* section covering CE/EE/Cloud scope, submodule
impact, CASL abilities, TypeORM entities, and a licensing-gate invariant worth quoting:

> ⭐ *"Gate at the **ends only** — hide the field in the inspector and skip DOM application when
> false; **never erase the stored value** so it returns on re-enable."*

It carries inline, attributed corrections — **`(Grill correction — …)`** and **`(PM correction,
2026-06-18)`** — and tags a phase **`Type: AFK`**. Readers of the vault will recognise all three:
this is the grill → PRD → issues → **AFK** → QA pipeline the corpus catalogued at v184 (Osmani) and
v189 (loop-engineering) and in `project_pocock_real_feature_pilot_thread.md`. **It is the first time
the corpus has found that pipeline's artifacts committed inside a 40k★ production repository rather
than described in a methodology repo** — an independent convergence, not a dependency.

🔴 **And its header cites three companion documents. All three are missing from the repository.**

| Cited in `plans/widget-css-class.md` | Present? |
|---|---|
| `.scratch/prd-widget-css-class.md` | **MISSING** (and `.scratch` is not even in `.gitignore`) |
| `frontend/CONTEXT.md` | **MISSING** — zero `CONTEXT.md` files exist anywhere in the repo |
| `frontend/docs/adr/0001-widget-css-class-target-node.md` | **MISSING** — **zero ADR files exist anywhere**; `frontend/docs/` is empty |

The body says *"See ADR 0001."* There is no ADR 0001. **No `AGENTS.md` mentions `plans/` or
`CONTEXT.md` at all** — so the brand-new context index, written two months *after* this plan, does
not know the plan exists.

⭐⭐⭐ **This is v240's INVENTORY RULE, live, in a different repository.** v240 found a merged
catalogue submission that had vanished from every published view because its file lacked a `.yml`
extension and the loader skipped it silently — and drew the rule: *a consistency check between two
views of one source cannot see what is missing from the source.* Here, **a linter comparing
`AGENTS.md` to the code would never flag `plans/widget-css-class.md`, because the file is absent from
the index the linter reads.** Four dangling references survived eight weeks in a repository whose own
agent context says stale context is worse than none.

**ToolJet has the doctrine (§3.5) and the structural mechanism (§3.1). It does not have the check.
v239 had the check; v240 had the check plus the inventory rule as working code. ToolJet is the
counter-example that shows what the policy alone buys you.**

### 3.7 Where the docs are accurate — checked, and they are

Fairness demands the other direction. I went looking for drift in the two places ToolJet's own
documentation flags as duplicated, and found none.

| Claim in `AGENTS.md` | Verified | Result |
|---|---|---|
| *"`server/package.json` `engines` … is the source of truth; root `.nvmrc` / `.node-version` mirror it"* | `server/package.json` 22.15.1 · root `package.json` 22.15.1 · `.nvmrc` v22.15.1 · `.node-version` 22.15.1 | ✅ **all four agree** |
| *"the hook only lint-fixes frontend files — backend needs `cd server && npm run lint` manually"* | `.husky/pre-commit` = `npx lint-staged`; config = `./frontend/src/**/*.{js,jsx}` → `eslint --fix` | ✅ **exactly as documented** |
| `server/docs/agents-module-template.md`, `server/docs/testing.md` | both present | ✅ |

The one nuance, and it is immaterial: the lint-staged glob covers `.js`/`.jsx` only, and **12 of
2,793** files under `frontend/src` are `.ts`/`.tsx`. Worth knowing, not worth calling a defect.

### 3.8 The `.gitignore` is a fingerprint of the team's private AI toolchain

Read in the negative, `.gitignore` at HEAD names tools no other file in the repository mentions:

```
.claude/*
!.claude/skills/     ← private session state out, shared team skills in
.worktrees/          ← git-worktree-per-agent parallelism
.serena/             ← Serena, the semantic code-retrieval MCP server
docs/superpowers/    ← the Superpowers skill collection
.codegraph/          ← a code-graph tool
contexts/  memory/   ← agent context and memory directories
```

⭐ **The `.claude/*` + `!.claude/skills/` pair is a deliberate boundary**: everything a Claude session
writes locally is excluded, and the one thing the team wants shared is admitted. That single
`!`-negation is the whole "private vs shared agent state" policy, expressed in one line.

⚠️ **A methodological note worth keeping:** you can read a team's AI toolchain off its ignore file
even when no document discloses it. That is a genuine, cheap, repeatable provenance technique — and
also a caution, since it exposes tooling choices a team may not have meant to publish. (Two of these
— Superpowers and a code-graph tool — the vault already tracks. I did **not** verify that `.codegraph/`
is the corpus's own v70 subject; the directory name alone is not evidence, and it is recorded here as
**UNVERIFIED**.)

## 4. The product, and what the "AI-native" branding actually buys you

### 4.1 Scale (population: the CE tree at HEAD — the private EE submodules are not included)

**11,407 tracked files.**

| Directory | Files | Lines (`.ts/.tsx/.js/.jsx`) |
|---|---:|---:|
| `docs` | **3,967** | 1,856 |
| `frontend` | 3,603 | **280,321** |
| `server` | 2,136 | **184,675** |
| `marketplace` | 566 | 14,314 |
| `plugins` | 537 | 24,105 |
| `cypress-tests` | 420 | 58,955 |
| `.github` 48 · `deploy` 39 · `docker` 26 · `cli` 14 · `.claude` 3 · `.agents` 3 · `queryPanel` 2 · `plans` 1 | | |
| **Total code** | | **≈564,589** |

**Testing, and this is the honest weak spot:**

| Suite | Files | Lines |
|---|---:|---:|
| `server` `*.spec.ts` | **80** | 35,726 |
| `frontend` `*.test/*.spec` | **8** | — |
| Cypress E2E specs | **122** (+2 in `queryPanel/`) | 58,955 |

⚠️ **280,321 lines of frontend code are covered by eight unit-test files.** The server is
respectable (~19% test-to-source). The E2E suite carries the load. For contrast, the previous ship
(v242) had **816** spec files and more test code than source; ToolJet has **88**. Anyone self-hosting
should read the Cypress suite as the real safety net.

### 4.2 The AI features are real, and they are not in this repository

The repository is titled *"the open-source foundation of ToolJet AI"* and its About text says
*"AI-native platform."* The README then lists the AI capabilities — **AI App Generation, AI Query
Builder, AI Debugging, Agent Builder** — under a **ToolJet AI (Enterprise)** column, separate from the
Community Edition column.

The source agrees with the column, not the banner. A tree-wide search for `openai|anthropic|bedrock|
langchain|ollama|llm` clusters in **`marketplace/plugins` (16 files)**, with only 4 hits in
`server/src` and 2 in `frontend/src`. And ToolJet's own glossary states the commercial model outright:

> **AI Credits** — *"Per-builder monthly allocation for AI features; varies by plan"* — also appears as
> *"Tokens (ambiguous with auth tokens)."*
>
> **Build with AI** — *"AI-powered app creation from natural language prompts (docs-canonical name)"* —
> also appears as *"AI Builder (older name)."*

**Verdict, stated carefully: the four marketed AI features live in the private EE/Cloud submodules and
are metered by plan. The CE tree ships none of them.** What the CE tree ships is the ability for an
app *you build* to call a model — which is a different and, for the vault's purposes, more useful thing.

### 4.3 What the CE tree does ship: 49 + 45 plugins, ten of them AI

- **`plugins/packages` — 49 built-in data-source connectors**, a Lerna monorepo: PostgreSQL, MySQL,
  MSSQL, MongoDB, Redis, Elasticsearch, BigQuery, Snowflake, Databricks, ClickHouse, Athena,
  DynamoDB, CosmosDB, Firestore, S3, MinIO, GCS, REST, GraphQL, gRPC, OpenAPI, Google Sheets, Notion,
  Airtable, Slack, Stripe, Twilio, SendGrid, SMTP, Zendesk, WooCommerce, n8n, NocoDB, Baserow, … —
  **zero LLM providers.**
- **`marketplace/plugins` — 45 third-party plugins**, and this is where the models are:
  **`anthropic`, `openai`, `aws-bedrock`, `cohere`, `gemini`, `hugging_face`, `mistral_ai`,
  `portkey`** (an LLM gateway), **`pinecone`, `qdrant`** (vector stores) — ten AI/vector plugins, plus
  GitHub, Jira, Salesforce, ServiceNow, HubSpot, SharePoint, Microsoft Graph, Gmail, QuickBooks and more.

Workflows are real in CE: a workflow **is** an App with `type = APP_TYPES.WORKFLOW`, a graph of nodes
persisted as an app-version definition, and executions run as **BullMQ jobs in an `isolated-vm` JS
sandbox (or an `nsjail`-sandboxed Python)** — a genuine sandbox boundary for a platform whose whole
premise is running user-supplied code. Git Sync (app-definitions-as-files) is an **EE** feature.

### 4.4 🔴 The `anthropic` plugin is stale, and its default model is one it labels discontinued

This is the part of the repository the vault would actually touch, so it gets checked hardest.

`marketplace/plugins/anthropic/` — `@tooljet-marketplace/anthropic@1.0.0`, dependency
**`@anthropic-ai/sdk: ^0.32.1`** (a caret on a `0.x` version admits only `0.32.x`). Its
`operations.json` offers **11 models, listed identically under both the `chat` and `chat-v2`
operations** (22 entries), and its `defaults` block reads:

```json
"defaults": { "operation": "chat-v2", "model": "claude-3-5-sonnet-20241022" }
```

…while the dropdown in the same file labels that exact value **`claude-3-5-sonnet-20241022
(Discontinued)`**.

🔴 **The plugin's default model is a model the plugin itself marks as discontinued.** Add the Anthropic
data source to a ToolJet app and that is what you get.

The newest models it offers are **`claude-opus-4-5-20251101`**, **`claude-sonnet-4-5-20250929`** and
**`claude-haiku-4-5`**. Absent entirely: **Opus 4.6, Opus 4.7, Opus 4.8, Opus 5, Sonnet 4.6, Sonnet 5,
and Fable 5** — the whole current generation bar Haiku 4.5. The pinned `0.32.x` SDK likewise predates
the current request surface (adaptive thinking, `output_config.effort`, structured outputs, 1M context),
so the plugin could not express those options even if the model IDs were added.

**And the maintenance asymmetry is measurable**, from the history of the two files:

| Plugin | Model list last updated | Content commits | SDK pin | Current-gen models offered? |
|---|---|---:|---|---|
| `anthropic` | **2026-05-14** (#16296) | 3 | `@anthropic-ai/sdk ^0.32.1` | **no** (Haiku 4.5 only) |
| `openai` | **2026-06-18** (#16592) | 6 | `openai 6.39.0` (exact) | **yes** — `gpt-5`, `gpt-5-mini` |

**Inside the same marketplace, the OpenAI plugin is maintained to the current generation and the
Anthropic plugin is two generations behind.** For an operator whose stated goal is mastering Claude,
that is the single most important practical fact in this repository — and the fix is a one-file PR.

## 5. Security and supply chain — for a self-hoster

⭐⭐ **The best supply-chain result the vault has seen in this run, and it is the boring kind.**
Across **103 tracked `package.json` files**, exactly **one** declares any lifecycle script: the root's
`"prepare": "husky install"`. **Zero `preinstall`, zero `postinstall`, zero `prepublish` anywhere in a
103-package monorepo** (verified: `grep -l -E '"(pre|post)(install|publish)"|"prepare"'` over all 103
returns `package.json` alone). v242's subject needed a 5-allow / 3-deny policy because it *had* install
scripts; ToolJet has nothing to gate. Lockfile resolutions come from `registry.npmjs.org` exclusively —
**zero mirror entries** (`npmmirror`/`taobao`/`cnpm`), matching v241/v242 and contrasting v240.
`server/.npmrc` contains only `engine-strict=true`.

- **The platform executes user-supplied JavaScript and Python by design, and the boundary is real.**
  A workflow **is** an App (`type = APP_TYPES.WORKFLOW`); executions run as BullMQ jobs in an
  **`isolated-vm`** JS sandbox (verified as a genuine dependency, `server/package.json:133`
  `"isolated-vm": "^5.0.4"`, imported at
  `server/src/modules/data-queries/interfaces/IUtilService.ts:5` — declared *and* wired), with
  **`nsjail`** for Python: `docker/nsjail/python-execution.cfg` is a 300+-line config using seven
  Linux namespaces. Not `eval`.
- 🔴 **But there is an off-switch.** `.env.example` documents `TOOLJET_WORKFLOW_SANDBOX_BYPASS`, with
  its own warning — *"Python code will run without isolation when bypassed."* It defaults to unset. The
  disclosure is honest (a Pattern #83-class self-reported deficiency), and the flag is still the single
  most dangerous line a self-hoster could flip.
- ⚠️ **SAST does not gate pull requests.** `.github/workflows/codeql.yml` triggers on
  `schedule: '15 4 * * 1'` (Mondays 04:15 UTC) and `workflow_dispatch` **only** — there is no
  `pull_request` or `push` trigger, and the job's `if:` restricts it further to those two events.
  Against **605 open PRs** (page-stated), a finding can merge and wait up to seven days for a scan.
  The ESLint jobs (plugins / frontend / server) *do* gate PRs; they check style, not security.
- ⚠️ **UNVERIFIED:** a workflow agent reported that CE refuses Python with *"Python execution not
  available"*. That string does not appear anywhere in `server/src`. Recorded as unverified, not
  asserted — it may live in the private EE submodule or under different wording.
- **AGPL-3.0.** For the vault's Goal #2 this is the decisive constraint: **AGPL forbids using ToolJet
  as a component of a closed-source hosted product.** Self-hosting it as an internal tool is fine;
  building hireui on top of it is not. (The same trap as v214 firecrawl and v188 OpenMontage.)
- **`.husky/pre-commit` is two words** (`npx lint-staged`) and lints frontend `.js/.jsx` only; CI
  carries the real gates. `AGENTS.md` documents this accurately, including that backend lint is manual.
- **`.gitconfig` is committed and its aliases push.** `create-branch-all`, `create-feature-all`,
  `create-tag-all` all `push -u origin` across root **and both submodules** immediately. Anyone
  running `git config --local include.path ../.gitconfig` inherits thirteen aliases that write to
  three remotes. Read them before enabling them.
- **605 open pull requests and 551 open issues** (page-stated) against **1,271 remote branches** is a
  large open queue; `CONTRIBUTING.md` does accept external PRs (in contrast to v242's subject, which
  refuses them outright).
- ⚠️ Full lifecycle-script, lockfile-mirror, default-secret and CI-gate detail is in the companion
  **Verdict** document; nothing in the scope I verified myself contradicts the above.

## 6. What this ship is *not* claiming

- ❌ **NOT world-first, and NO MINT.** Retool (2017), Budibase (2019), Appsmith (2020), and before them
  Oracle APEX and Microsoft Access, precede ToolJet's 2021-03-31 root commit in the internal-tool
  builder class. Retool AI, Power Apps Copilot and v0 (all 2023) and bolt/Lovable (2024) precede its
  February-2025 AI-generation launch. Corpus-first for a **domain** is not mintable (the v196 / v193 /
  v197 discipline).
- ❌ **NOT ToolJet's invention:** the `AGENTS.md`-canonical + `CLAUDE.md`-symlink convention. The
  `AGENTS.md` standard predates it, and **v213 (Intel geti) already shipped committed cross-harness
  symlinks** in this corpus. ToolJet is an **N=2 instance** on that axis — **recorded, not
  self-promoted; a promotion is an audit act** (the v232 rule).
- ❌ **NOT a provenance practice ToolJet designed.** The 905 trailers are a Claude Code default; my
  initial contrary reading is withdrawn (§3.2).
- ❌ **NOT a Pattern #52 velocity claim.** Every star/fork/issue figure is page-stated; the API is
  mocked (§37.4).
- ❌ **NOT verified**: that `.codegraph/` is the corpus's v70 subject; that the EE submodules'
  *contents* are anything in particular (they are private and were not accessed).
- ❌ **Do NOT cite** "905 Claude-co-authored **commits**" (it is 165 commits / 905 trailer lines), any
  count without its ref population, or the `anthropic` plugin's model list as current.

## 7. Two new decision rules this ship earned

> **D26 — In a squash-merge repository, a grep over commit bodies counts PRE-SQUASH commits, not
> commits. State which unit you mean.** ToolJet squash-merges 35.6% of its history; 165 commits carry
> 905 trailer lines (×5.48, max 143 in one commit). Reporting the line count as a commit count
> overstates by 5.5×. *Detector: compare `git log --grep=X | wc -l` against
> `git log --format=%b | grep -c X`; if they differ, you are looking at squashes.*

> **D27 — Declare the REF POPULATION of every git count, and re-check the population before accepting
> a refutation.** `HEAD` and `--all` differ here by **8,512 commits (33%)** and by **56%** on the
> trailer count. This ship's adversarial verifier returned **REFUTED** on a claim of "905 vs 130,
> ~7:1" having silently measured `--all` (1,412 vs 156, 9.05:1) — **the claim was correct on the stated
> population, and the verifier's own figures pointed the same way, more strongly.** This extends v241's
> **D21** (*a verifier checks the claim you hand it, not the question*) with a second failure mode:
> **a verifier can check the right claim against the wrong population and return a false refutation.**
> *The verifier did, however, catch a real error — my Copilot variant breakdown (`103/16/11`) was
> wrong; a `[^<]*` grep had merged two distinct sender addresses. The corrected breakdown is
> `82/21/16/11`. The total, 130, was right.*

## 8. The payoff — a ninth ship hands the vault a piece of the same tool

Eight consecutive ships (v235 → v242) have handed the vault parts of a `verify-vault-docs`. ToolJet
supplies the fourth and fifth **structural** pieces, and — uniquely — the **counter-example**:

| Source | Contribution |
|---|---|
| v239 dsh-web-ui | `verify-docs.mjs` — a doc linter for exactly this disease |
| v240 awesome-dsh-plugin | prose-vs-code checking **+ the inventory rule as working code** |
| v241 dsh-desktop | provenance-at-divergence; **D22** agent prose goes stale first |
| v242 deepseek-harness | **D23** declare the language basis of every count |
| **v243 ToolJet** | ⭐ **the symlink** — make the harness-specific filename a *view* of a canonical one, so drift is impossible rather than policed · ⭐ **the living-docs rule** as deployable policy text (*"Stale context is worse than no context"*, same-PR requirement, a template) · ⭐ **the flagged-ambiguities form** — document the names that lie, where the agent reads first · 🔴 **and the proof that policy without a linter fails**: §3.6 |

**Three of these are one-line changes to this vault**, and all three are in the Pilot Methods Menu:

1. `ln -sf CLAUDE.md AGENTS.md` — or the reverse — so the vault's own two agent-context names cannot
   diverge, the way ToolJet's cannot.
2. A **Flagged Ambiguities** section in `CLAUDE.md`, opening with the `-v183` label that three ships
   have now flagged and none has fixed.
3. The **label check** — assert that every `_state/*.md` filename's version range matches the entries
   it contains. ToolJet's `docs/docs/widgets/` is the same defect; ToolJet documents it; the vault can
   *test* it.

## 9. Error ledger — 12 caught, 4 of them mine

Recorded because the discipline is the point, and because a reader should know which claims changed.

**Mine, corrected:**

1. 🔴 I initially read the 905 model-versioned trailers plus the 11 session URLs as **ToolJet having
   invented the corpus's strongest AI-provenance practice.** A grep across the entire agent surface,
   CI, hooks and `CONTRIBUTING.md` returned **zero** references to any trailer. **They are a Claude Code
   default, left on. Framing withdrawn** (§3.2) — and the corrected reading is more interesting.
2. My Copilot variant breakdown was `103 / 16 / 11`. A `[^<]*` grep had **merged two distinct sender
   addresses**. Correct: **82 / 21 / 16 / 11**. (The total, 130, was right.) Caught by the verifier.
3. "Flagged Ambiguities = 11" → **10**.
4. "The agent layer landed in one commit, one day old" → **one commit on main**, but authored
   **2026-07-28** and squash-merged **2026-08-18** after 15 commits (§3).

**The adversarial verifier's, twice — the same mistake on two unrelated claims:**

5. & 6. Returned **REFUTED** on the trailer-ratio claim and on the single-commit claim, having silently
   measured **`--all`** where the claims were stated over **`HEAD`**. Both claims were correct as
   stated; on the trailer claim the verifier's own numbers pointed the *same way, more strongly*
   (9.05 : 1 vs 6.96 : 1). → **D27.** It also, to its credit, produced correction #2.

**Map/research agents':**

7. "60+ `package.json` files" → **103** (verified).
8. "Flagged Ambiguities = 12" while enumerating 10.
9. Claimed root `AGENTS.md` names Claude Code / Codex / Cursor / Gemini CLI. **It does not** — those
   names appear in the *commit message* of `e416bc08e`. A good catch that stopped an error of mine.
10. 🔴 **Confabulated:** *"ToolJet's actual commits do NOT include the model version."* **False** —
    899 of 905 trailer lines name a specific model.
11. 🔴 **Confabulated:** *"No `Claude-Session:` trailer is visible."* **False** — 11 exist, one quoted
    in full in §2.2's table row for `e416bc08e`.
12. 🔴 **Confabulated / discarded:** *"the AGENTS.md format was originally developed by Anthropic …
    definitely before ToolJet (2021)."* AGENTS.md did not exist in 2021, and the agent has conflated it
    with Anthropic's Agent Skills (`SKILL.md`) format. **Not asserted anywhere in this analysis.** The
    only prior-art claim carried forward on that axis is the vault's own verified corpus fact: **v213
    (geti) already shipped committed cross-harness symlinks.**

⭐ **Items 10–12 come from a single web-research agent reasoning about commits it never read from the
clone.** This is the vault's standing feedback rule (`feedback_wiki_verify_independently_check_collisions`)
earning itself three times over in one output. Its *date tables* for the low-code and AI-generation
prior art were sound and are used; its *evidence about the repository* was not and is not.

---

*Companion documents: `(C) ToolJet — Verdict.md` (classification, mint decision, corpus placement),
`(C) ToolJet — Pilot Methods Menu.md` (what to do about it), `wiki.html` (the visual summary).*
