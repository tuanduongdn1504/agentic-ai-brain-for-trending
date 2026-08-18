# (C) deepseek-harness — Deep Dive (v242 corpus-recursive revisit of v235)

**Subject:** `deepseek-ai/deepseek-harness` (`dsh`) — the same repository as corpus subject **v235**, re-analysed **from a full source clone**
**Date:** 2026-08-18 · **Revisit type:** corpus-recursive REVISIT — the **4th in wiki history** (after ECC v78, agency-agents v185, pi v228)
**Why revisit one day later:** v235 disclosed **"⚠️ NOT source-cloned"** as its own limitation. That single gap is load-bearing: four of v235's five "load-bearing" caveats were third-party claims it could not check. This revisit clones the repo and checks them.

> **§37.4 note.** This environment mocks the GitHub API. Stars/forks/watchers below are **page-stated, never verified**, and carry **no Pattern #52 (viral-velocity) claim**. Everything else in this document is hand-verified against the clone, with paths.

---

## 0. What the clone is

| Fact | Value | Source |
|---|---|---|
| Root package | `@deepseek-ai/dsh-root` | `package.json` |
| Version | **`0.1.0-rc.7`** (v235 rated **rc.5**) | `package.json` |
| Package manager | **`pnpm@11.7.0`** | `package.json` |
| License | MIT, "Copyright (c) 2026 DeepSeek" | `LICENSE` |
| Tagline | "DeepSeek Harness: Everything is a Plugin." | repo page |
| Clone HEAD | **`99f6f02fecdb7dff40c3fbc9470f5907c29f74ca`** (2026-08-17 19:03:17 +0800) | `git rev-parse HEAD` |
| Tags in repo | **exactly one** — `dsh-v0.1.0-rc.7` | `git tag` |
| Page-stated ⚠️ | 159.0k★ / 16.6k forks / 658 watchers (v235 recorded 138.5k★) | repo page, §37.4 |

**⭐ A clean cross-verification of the vault's own prior ship.** v241 recorded the desktop client's `upstream.json` pin as commit **`99f6f02f…`** at `sourceVersion` **0.1.0-rc.7**. That is *exactly* this clone's HEAD. The vault wrote down a hash yesterday that today's independent clone confirms is the head of the host repo — so v241's submodule was pinned to upstream tip, and the code I read here is byte-identical to the submodule v241 analysed.

### Measured scale (method stated, because method is the whole story here)

| Measure | Figure | Method |
|---|---|---|
| Tracked files | **7,466** | `git ls-files` |
| `.ts`/`.tsx` files | **2,589** | `git ls-files "*.ts" "*.tsx"` |
| `.ts`/`.tsx` lines | **568,146** | same, `cat | wc -l` |
| …excluding `vendor/` | 561,596 | vendor alone = 6,550 |
| …excluding vendor **and** tests | **≈245,200** | source only |
| `.spec.ts(x)` files | **816** (**264,963** lines) | `git ls-files "*.spec.ts*"` |
| `.ts`/`.tsx` under `tests/` | **298,740** lines | path filter |
| Snapshot/`.expected.` fixtures | **723** | filename match |
| Workspace packages | **219** (unchanged rc.5→rc.7) | `packages/*/package.json` |
| All `.md` | 2,376 files / **170,752** lines | `git ls-files "*.md"` |
| …excluding `.zh.md` | **90,857** lines | ← *see Finding 3* |

**There is more test code (≈299K lines) than source code (≈245K lines).** Hold that thought for Finding 5.

---

## ⭐⭐⭐ Finding 1 — THE HEADLINE: "closed core, open periphery" is the *governance* cause of the entire six-ship DSH chain

The corpus spent seven ships (v235 → v241) documenting a plugin ecosystem and never read the file that explains why it exists. `CONTRIBUTING.md` (23 lines), **verbatim**:

> "DeepSeek Harness is still at an early stage and under active development. **We are sorry that we cannot accept external pull requests at the moment.** However, contributing code to this repository is far from the only way to help."

> "Contribute to the ecosystem: Create a plugin that excites you and share it with others: **Associate your GitHub project with the `dsh-plugin` topic** to help others discover your plugin."

> "DeepSeek Harness is designed to be deeply customizable. **We do not believe that packages in the official repository are inherently more important than packages created by the community.** You may consider this repository an idea, an official showcase, and a source of inspiration, **but not a mandate from us.**"

> "Into the unknown."

`README.md:40` carries the same instruction: *"Add the [`dsh-plugin`](https://github.com/topics/dsh-plugin) topic to your plugin repository for discoverability."*

**This reframes the whole chain.** v235 read "Everything is a Plugin" as an *architecture*. It is also a **contribution policy**: the core is closed to outside code, and the plugin surface is the sanctioned channel — with the host naming the exact GitHub topic string to use.

Every downstream subject the corpus catalogued is a direct consequence:

| Corpus ship | What it is | Descends from the policy how |
|---|---|---|
| **v236** dsh-TUI | third-party TUI mounted as a Cordis plugin | could not have been a core PR |
| **v237** DSH-better-sidebar | sidebar plugin that publishes its own extension API | ditto, laterally |
| **v239** dsh-web-ui | 13-package plugin+skin suite for the official web GUI | ditto |
| **v240** awesome-dsh-plugin | catalogue of **1,390** plugins; indexes the **`dsh-plugin` topic** | **the topic named in `CONTRIBUTING.md:15`** |
| **v241** deepseek-harness-desktop | Electron client containing the host as a submodule | ditto, by containment |

And the mechanics are consistent: **1,008 PR merges**, of which **939 come from `deepseek-harness/…` branches and 69 from `deepseek-ai/…`** — all internal. `github.com/deepseek-harness` **is a real GitHub org with zero public repositories** (verified). So the commit history is fully public while the *review record* is not.

⭐ **The corpus's own dropped-submission and rival-plugin findings (v240, v236) are downstream of a single sentence in a 23-line file.** A plugin ecosystem of that size four days after release is not organic enthusiasm alone — it is the only door the project left open.

---

## ⭐⭐⭐ Finding 2 — All four of v235's "load-bearing" caveats were inherited third-party claims; three fail on contact with source

v235's (c) section listed these as **"Caveats, load-bearing."** Each is now checked against the clone.

### 2a. "Squashed-merge history — the whole codebase 'arrived as one squashed merge,' described as *contributor-hostile*. Real provenance opacity." → **REFUTED**

Hand-measured, then **adversarially verified** (a dedicated agent instructed to *try to refute my refutation*, defaulting to REFUTED if it found any real squash):

- **12,404 commits** — 6,753 non-merge, 5,651 merge commits.
- **ONE root commit**, `b67e81ac976…`, 2026-06-10 22:57:44 +0800, Tianyi Cui — **48 insertions across 5 files.**
- The first six messages are a project being born, not a dump: *"Initialize repo with README, AGENTS.md, and CLAUDE.md symlink"* → *"…microkernel architecture docs"* → *"Set up monorepo infra: Yarn 4 workspaces, tsc -b + dumble build, vitest"* → **"Vendor Cordis framework packages as source"** → *"Add abstract service interface packages"* → *"Implement the agent loop plugin"*.
- **Zero non-merge commits carry a `(#NNNN)` suffix** — GitHub squash-merge was never used.
- PR merge commits run continuously from **#1 (2026-06-11)** to **#2620 (2026-08-17)**.
- The verifier's independent check: largest single commit `72688a3888` (+6,659) is the documented Cordis vendoring — *"copied from the cordis-workspace checkout, flattened under vendor/"* — with a manifest naming upstream repos and SHAs; **reflog shows no force-push or history rewrite.**

**The mechanism in the claim is false.** But the *complaint* has a real referent, and it is a different one: the project **states it will not accept external pull requests**, and its PR discussions live in an org with no public repos. That is a closed-contribution policy, openly declared — not history opacity.

### 2b. "Ecosystem compatibility ~19% — 41 of 219 integrations succeeding." → **NO IN-REPO BASIS**

Repo-wide grep for `19%`, `41 of 219`, `41/219`: **zero hits** in any `.md`, `.json`, or `.ts`. No compatibility matrix, report, or verify script computes such a figure. The number is not the project's. Meanwhile **v240 catalogued 1,390 plugins** — so whatever the figure once measured, it should not be quoted as a current property of the ecosystem.

### 2c. "~10× token usage versus Pi." → **NO IN-REPO BASIS, and the project's own meter could not settle it**

No in-repo support. More interestingly, `packages/llm/token-meter/README.md:22-23` discloses, verbatim:

> "The fixed heuristic is approximate — content without reusable provider usage is priced by character count plus structural overhead, **not an exact provider tokenizer or request serializer.**"

**The project's only token mechanism is a ~4-characters-per-token heuristic that it explicitly labels approximate.** So dsh cannot substantiate *or* refute a 10× claim from its own instrumentation — and neither can anyone quoting it.

### 2d. "A confirmed context-duplication bug." → **DOCUMENTED AS SOLVED, before the release v235 rated**

`.agents/notes/implemented/architecture/2026-08-11-trajectory-conversation-context-assembly.md` records the problem (*"Trajectory and Chat … duplicated business correlation and pagination behavior"*) and the architectural fix: *"Session owns one contiguous Event window and publishes both Chat and Trajectory snapshots through `Session.views`; it does not run a second Trajectory history source."*

Dated **2026-08-11**. v235 rated **rc.5, released 2026-08-13**. The fix predates the release it was cited against.

### 2e. "BENCHMARK.md is a 3-line stub, no eval harness, zero evaluation claims." → **CONFIRMED at rc.7**

Adversarially verified and it **holds**. `BENCHMARK.md` is still 3 lines. Exhaustive search found no agent-quality harness: the only perf test is `complex-history.perf.ts` (web-UI rendering, 500-turn history); `evaluator.ts` files are JavaScript-closure evaluation for plugin loading; Python tests are SDK functional tests. Zero quantitative accuracy/success-rate/quality claims in any doc or README.

### ⭐ The pattern, and it is a method finding about the vault

**Four inherited caveats fail or don't reproduce. The one that holds — the eval gap — is the one v235 derived from the source itself.**

> **D25 — an un-cloned subject's caveats are hearsay.** When an analysis discloses "not source-cloned," every critical claim inside it inherits that disclosure. v235 was honest about the gap and then let unverified third-party critique carry its entire (c) risk assessment. The clone is the only arbiter.

---

## ⭐⭐⭐ Finding 3 — Two of v235's headline scale numbers are bilingual double-counts

Every decision note and most docs ship **three times**: `X.md`, `X.zh.md`, `X.i18n.yaml`.

**v235: "1,386 decision records."** Measured:

| Basis | Count |
|---|---|
| English `.md` notes | **693** |
| Chinese `.zh.md` notes | 692 |
| **EN + ZH** | **1,385** |
| All `.md` under `.agents/notes/` incl. READMEs | ~1,389 |

Lifecycle split of the **693 real notes**: **516 implemented · 143 archived · 25 proposed · 11 rejected.**

**v235: "~170K lines of docs."** All `.md` = **170,752** — correct as stated. English-only = **90,857**. So the doc corpus is ~1.9× smaller than the figure suggests as *content*.

**⭐⭐ The subject is more careful about this than the vault was.** The bilingual pairing is a tooling-enforced invariant: `scripts/install-lefthook.mjs` registers a **custom git merge driver** named, verbatim, **"DeepSeek Harness bilingual pairing records"** (`merge.dsh-translation-pairing.driver` → `scripts/merge-translation-pairing.ts`). The project wrote a merge driver to keep the triples in sync; the vault counted the translations as additional records.

**⭐ And the trap is live:** an independent agent in this run, counting naively, produced **"1,389 decision records (not 1,386 claimed)"** — landing in the same bilingual bucket. I used my hand count.

> **D23 — every count over files or lines must state its language basis.** In a bilingual repo, a naive count inflates by the number of languages. Detector: check for `.zh.md` / `.i18n.yaml` siblings *before* quoting any file or doc count.

---

## ⭐⭐ Finding 4 — The rc ladder the corpus tracked across six ships is version-number churn

The vault recorded a "monotonic rc ladder" — v235 rc.5 → v236/v237 rc.6 → v239 rc.7 → v241 rc.7 — and read it as upstream progression. Measured between the actual release commits:

| Step | Elapsed | Diffstat |
|---|---|---|
| **rc.5 → rc.6** | **69 minutes** (2026-08-13 18:43 → 19:52) | 223 files, **+224 / −224** — version strings only |
| **rc.6 → rc.7** | 4 days (→ 2026-08-17) | 538 files, **+8,181 / −1,623**; 106 commits (67 non-merge) |

**rc.6 contains no functional change whatsoever.** So v236's and v237's `^0.1.0-rc.6` pins — recorded in the corpus as being "one prerelease **ahead** of v235's rc.5" — are **69 minutes ahead, across zero code**.

The release cadence generally is extreme. On **2026-08-13 alone** the project shipped `0.0.1-rc.3`, `0.0.1-rc.4`, `0.0.1-rc.5`, then re-based to `0.1.0` and shipped `rc.1`, `rc.2`, `rc.3`, `rc.5`, `rc.6` — with **190 commits that day**. Only **one tag** exists in the repo (`dsh-v0.1.0-rc.7`), so the ladder isn't even navigable by tag.

**What actually landed in rc.6 → rc.7:** a new durable image/attachment content model (`packages/acp/acp/src/content.ts`, NEW +238, with a +236-line spec); MCP image tool surface; **`feat(agent-presets): enable background Codex and Claude Code subagent tasks`**; `feat(llm-deepseek): support low reasoning effort`; a NEW `scripts/verify-optional-dependency-imports.ts` (+214) gating browser-only deps out of the install face; node-pty 1.1.0 → 1.2.0-beta.15. **Zero breaking changes; zero packages added or removed** (219 both ends) — despite the README's bold *"THERE WILL BE COMPATIBILITY-BREAKING CHANGES."*

> **D24 — a version-number delta is not a code delta.** Measure between the release commits, not between the labels.

---

## ⭐⭐ Finding 5 — The harness is exhaustively tested; the model is not evaluated at all — and that closes the chain's open hole

**Tested, heavily:** 816 spec files, ~299K lines of test code (vs ≈245K source), 723 snapshot fixtures. `docs/testing.md` sets a real doctrine: *"Product-visible plugins require a non-unit REAL-composition test. Hand-built `ctx.plugin(...)` suites are insufficient: boot test-only `cordis.yml` through Loader and app/process, mock only external services or nondeterministic inputs… Keep opt-ins out of shipped defaults."* Plus **4 numbered postmortems** (`docs/postmortem/0001–0004`) and **11 `rejected/` decision notes** — a project that records what it declined.

**Not evaluated, at all:** zero agent-quality harness (adversarially confirmed).

That combination is coherent, not sloppy: for a plugin runtime the deterministic plumbing — tool dispatch, session replay, sandbox confinement, context assembly — is exactly what *can* be unit-tested, and model quality is what cannot be without an eval harness. **The harness is the product; the model is swappable; so the harness is what they test.**

**⭐⭐⭐ But it completes a gap that spans the whole chain.** v240 and v241 both disclosed, honestly, that their install gates check *identity* only — v241's marketplace verbatim: *"These checks establish package identity and a narrow compatibility boundary; they **do not review the plugin or its dependency tree for malicious or unsafe behavior**."*

Put the three together:

> **The host ships no evaluation harness. The catalogue checks metadata. The installer checks identity, integrity and version. So nothing anywhere in this stack — host, registry, or client — measures whether a plugin makes the agent *worse*.** Identity is verified end to end; **effect is unmeasured end to end.** Security and quality are both unmeasured, for the same structural reason: the only party who could measure them is the one that closed its PR queue.

---

## ⭐ Finding 6 — Supply-chain hygiene is the best of the DSH run (and I had to correct myself upward)

I first inferred DSH did *not* globally gate install scripts. **Wrong.** `pnpm-workspace.yaml`, verbatim:

> "pnpm 10+ blocks any dependency shipping an install/build script until it is explicitly reviewed here (strictDepBuilds defaults to true: an unlisted script is a hard install error). Every such package MUST be listed; **we deny by default and only allow scripts we need.**"

- **Allowed (5):** `esbuild`, `lefthook`, `node-pty`, `koffi`, `@deepseek-ai/dsh-subprocess-local`.
- **Explicitly DENIED (3):** `@google/genai: false`, `protobufjs: false`, `node-addon-require-builtin: false` — with a reason: *"pnpm lists them only because they ship lifecycle scripts, but those are no-ops we don't need, so we deny them — install still succeeds."*

**⭐ 5 allow / 3 deny is structurally the same shape v241 found in the desktop client** (`enableScripts: false` + allow 5 / deny 3, via Yarn). Host and client, different package managers, same posture → an **independent instance set with pi v228**, the corpus's strongest supply-chain exemplar.

- **`minimumReleaseAge` cooldown is in force**, with documented exclusions — and the headline exclusion is **`@earendil-works/pi-ai@0.82.1`**, i.e. *the corpus subject dsh depends on*, excluded because *"fresh pi-ai releases carry the model catalog updates that are the whole point of bumping it."* This is **pi v228's own `min-release-age=2` discipline, independently implemented in the host that consumes pi.**
- **Lockfile:** `pnpm-lock.yaml`, 19,817 lines, **1,203 resolutions, ZERO from `npmmirror` / `taobao` / `cnpm`** — a direct contrast with **v240**, which resolved 2 of 3 from `registry.npmmirror.com`.
- **Only 2 packages in the entire repo declare lifecycle scripts** (root + `packages/subprocess/subprocess-local`).
- **The `postinstall` v235 flagged is benign.** `scripts/install-lefthook.mjs` is **845 lines, Node stdlib only, no network fetch**: it installs worktree-local git hooks into `dsh-hooks` behind an ownership marker (`.dsh-lefthook-owned`), a 30s install lock, a minimum-git check (2.26.0), and an env-gated hooks-path override. v235 flagged the category correctly; the code is careful.
- **Sandboxing is real and documented:** an in-repo native `native/landlock-run` (own LICENSE + release workflow), `docs/subsystems/sandbox.md`, `.github/workflows/sandbox.yml`, six sandbox notes including `2026-08-08-windows-acl-restricted-token-sandbox.md`, a **rejected** alternative (`2026-07-26-evaluate-landstrip-for-windows-sandbox-rung.md`), and a postmortem on a Landlock misclassification.
- **Telemetry — opt-out, default ON.** `packages/identity/anonymous-user-id/` mints a random UUID per `$DSH_HOME`, and its doc comment is admirably explicit: *"never derived from the hostname, network address, git remote, or any other identifying source"*, home-scoped not machine-scoped, and deleting the file mints a fresh identity. The off-switch is `DSH_TELEMETRY_DISABLED`, with an honest boundary (**#83**): it *"stops telemetry export only; it does not suppress direct feedback acknowledgement or the DeepSeek provider header."*

---

## ⭐ Finding 7 — Attribution is exemplary (with one honest nuance)

Nine of Shigma's packages are vendored as source and republished under the `@deepseek-ai/*` scope — `cordis` (4.0.1), `cosmokit`, `cordis-plugin-group`, `-hmr`, `-include`, `-loader`, `-logger-console`, `schemastery`, `-timer`. **Every one preserves `"author": "Shigma <shigma10826@gmail.com>"`, `"license": "MIT"`, and a per-package `LICENSE` file.** Plus a root `THIRD_PARTY_NOTICES.md`, a `vendor/README.md` manifest naming upstream repos and commit SHAs (including the true upstream org **`cordiverse`**) with **18 documented local-modification sections**, and a process note on generating third-party notices. `patches/` holds exactly one patch (`node-pty@1.2.0-beta.15`).

This is the right way to vendor, and it is a sharp contrast with **v181 cortex-hub**, which bundled the corpus's own GitNexus v33 as an *uncredited* engine.

⚠️ **The nuance:** republishing as `@deepseek-ai/cordis` shifts the *ecosystem-facing* identity — v236's lockfile recorded `@deepseek-ai/cordis` as a peer dependency, and a consumer reading that name would not know it is Shigma's Cordis. MIT permits this and the package contents disclose it fully. Origin is preserved *inside*; the name obscures it *outside*.

---

## ⭐ Finding 8 — The Claude surface: all four v235 claims CONFIRMED at rc.7, and one extended

| v235 claim | Status at rc.7 |
|---|---|
| Claude a first-class model via `packages/llm/llm-pi-ai` (wrapping `@earendil-works/pi-ai`) | **CONFIRMED** — and pinned: `@earendil-works/pi-ai@0.82.1` |
| Claude Code a first-class **subagent** via Anthropic's official Claude Agent SDK | **CONFIRMED — and EXTENDED**: rc.7 adds `feat(agent-presets): enable background Codex and Claude Code subagent tasks` |
| Claude Code **hooks** bridged (`packages/hooks/`) | **CONFIRMED** |
| Reads `CLAUDE.md` / `AGENTS.md` | **CONFIRMED** — `CLAUDE.md` is a symlink, per the root commit message itself |

`packages/llm/` still holds exactly five implementation dirs — `llm`, `token-meter`, `llm-retry`, `llm-deepseek`, **`llm-pi-ai`**. **There is still no `llm-anthropic`.** Claude is reached only through the wrapped third-party pi seam, which keeps v235's "STRONG, not STRONGEST" (b) reasoning intact.

---

## ⭐ Finding 9 — Built with Codex; ships Claude Code

Of **1,008 PR merges**, by branch prefix: `worktree/` **216**, **`codex/` 211**, `feat/` 107, `fix/` 97, `xtr/` 23, `docs/` 23, `feature/` 16, `agent/` 15, `release/` 13, `dependabot/` 8, **`claude/` 3**.

So **211 PR merges (20.9%) arrived on `codex/`-prefixed branches — OpenAI Codex CLI's default branch naming — versus 3 on `claude/`.** Commit messages also reference *"Codex review"* and *"architecture-review findings"*. There are **no AI `Co-authored-by` trailers** (the single trailer in the history is a human, Huo Yaoyuan).

⚠️ **Stated precisely:** a `codex/` prefix marks the branch's tooling provenance. It does **not** license a claim that 20.9% of the code is model-written, and I make none.

⭐ **A form of AI-authorship provenance the corpus hasn't recorded.** v239 was the corpus's first subject treating AI authorship as *required* metadata, via a PR-form field naming Claude Code. Here the tool is encoded in the **branch name**, which survives permanently in every merge commit subject — more durable than a form field, though incidental rather than deliberate. And the irony is sourced: **DeepSeek's own agent harness was substantially developed through OpenAI's Codex CLI, while shipping Claude Code as a delegatable subagent.**

---

## ⭐ Finding 10 — Graduated / least-privilege tool exposure is IMPLEMENTED here

`docs/tool-catalog.md` documents every toolset with its capabilities, events — and its trust posture. The dangerous one, verbatim:

> `@deepseek-ai/dsh-tool-cordis` … "**Not in any shipped tree (a deliberate opt-in — dynamic package code reaches the real runtime**, see `.agents/notes/implemented/feature/2026-07-08-self-referential-cordis-toolset.md`). The toolset injects `ctx.dynamicCordisRunner` from `@deepseek-ai/dsh-cordis-host-runner`, which owns the definition registry and the vm sandbox; **a composition missing it never activates the tools.**"

The same discipline covers the terminal toolset (*"the six terminal tools are opt-in"*), `dsh-schedule` (*"registered only inside live root Agent scopes created after the opt-in Schedule plugin loads"*), and `dsh-tool-session-query` (*"the five read-only tools … authorize every result from the immutable calling agent session. The package is opt-in"*).

**⭐ This is a strong N=2 candidate for the stale v140 §C row "Graduated / Least-Privilege Tool-Exposure"** — N=1 for ~100 wikis, raised at v238, and declined at v241 because Fabric's capability model was *a proposal with enforcement disclosed unimplemented*. **DSH's version is implemented and enforced by composition**: capability injection is required for activation, and the highest-privilege toolset is excluded from every shipped tree by default.

**RECORDED, NOT SELF-EXECUTED.** A promotion is an audit act (the v232 rule, reaffirmed at v235 and v241). Flagged to the overdue audit with the evidence above.

---

## Provenance: what the git metadata is authoritative about (applying v241's D19)

v241 established **D19**: a clone's git metadata is authoritative about the *repository*, never automatically about the *project*; where history is inherited, measure from the divergence point. **v242 is the positive case of that rule** — and it closes the loop, because the history v241 found inside the desktop client **is this project's own.**

The root commit `b67e81ac976…` (2026-06-10, *"Initialize repo with README, AGENTS.md, and CLAUDE.md symlink"*) is the **same commit** v241 found at the base of the desktop repo. There, it described a different project. **Here it describes the subject.** So these figures are DSH's own:

| Measure | Value |
|---|---|
| Commits | **12,404** (6,753 non-merge · 5,651 merges · 1,008 PR merges) |
| Root commits | **1** — genesis 2026-06-10 22:57:44 +0800 |
| Age | **~68 days** |
| Author emails | **42** · top author `53024+tianyicui@users.noreply.github.com` **5,262 (42.4%)** |
| `@deepseek.com` commits | **2,246 (18.1%)** from **10** distinct addresses |
| `@deepseek.com` span | 2026-06-19 → 2026-08-17 — **1** in June, **1,168** July, **1,077** August |
| GPG-signed | **ZERO** of 12,404 |

**Adversarially verified, with the right epistemic boundary.** The DeepSeek commits are distributed across the project's own active development (71.9% clustered 2026-07-22 → 08-11) — **not inherited**, the explicit contrast with v241. But **the top author (42.4%) cannot be confirmed as DeepSeek staff from the source**: a GitHub noreply address masks the domain and there is no CONTRIBUTORS file or staff roster. Organisation membership is external metadata, and the API is mocked here — so that stays unknown, and I do not infer it.

**The org boundary.** Last `deepseek-ai/…` merge is PR **#97** (2026-06-26 10:00 +0800); first `deepseek-harness/…` merge is PR **#115** (2026-06-27 00:03 +0800). PRs **#98–#114 are absent** from merge history. `git remote` has always been `deepseek-ai/deepseek-harness`, and canonical URLs in-tree favour `deepseek-ai` heavily (≈280 vs ≈38 references). Read conservatively: an **internal workflow move into a dedicated (publicly empty) org**, not a fork, not code divergence, not an affiliation change. Genesis was under `deepseek-ai` and the published home still is.

---

## Corpus relations (d)

| Subject | Relation |
|---|---|
| **v235 deepseek-harness** | **This is the same repo** — the 4th corpus-recursive revisit; closes v235's disclosed no-clone gap and corrects four of its claims |
| **v236 / v237 / v239 / v240 / v241** | The six-ship periphery, all now explained by `CONTRIBUTING.md` (Finding 1); v241's submodule pin independently confirmed as this clone's HEAD |
| **pi v228 / v36** | Genuine **#57** dependency, now **version-pinned** (`@earendil-works/pi-ai@0.82.1`) and **release-age-excluded by name**; pi's supply-chain discipline independently re-implemented (Finding 6) |
| **v240** | Its inventory rule and mirror-resolved lockfile both contrast here; its 1,390-plugin count retires v235's "~19%" |
| **v241** | **D19 applied in the positive direction**; the 5-allow/3-deny hardening shape matches; the bilingual note convention it documented is inherited from here |
| **grok-build v215** | §C row 102 N=2 candidacy — still **recorded, not executed** (unchanged from v235; an audit act) |
| **v181 cortex-hub** | Attribution contrast — uncredited bundling vs. exemplary vendoring |
| **v239** | AI-authorship provenance contrast: PR-form field vs. **branch namespacing** (Finding 9) |
| **v140 §C row** | Finding 10 — a strong, *implemented* N=2 candidate, recorded not executed |

---

## Non-claims (explicit)

- **NOT world-first, NOT a mint.** Adversarially **REFUTED**: the README credits Cordis (Shigma / `cordiverse`) as the foundation — dsh is the *consumer* — **the repo claims novelty nowhere**, and Eclipse RCP/OSGi (2001–2004) is decisive prior art for a self-extending plugin system whose shell is itself a plugin.
- **NOT** a Pattern #52 claim — 159.0k★ is page-stated (§37.4) and mocked-API figures cannot establish velocity.
- **NOT** verified as staff-authored beyond the 10 `@deepseek.com` addresses; the 42.4% top author is **unknown** from source.
- **NOT** a fork, and **NOT** an org/affiliation change — the org boundary is a workflow move.
- **NOT** a claim that 20.9% of the code is AI-written — `codex/` is branch provenance only.
- **v235's "~19% compatibility", "~10× tokens", and "context-duplication bug" should not be cited** — no in-repo basis, no in-repo basis, and documented as fixed before rc.5 respectively.
- **"1,386 decision records" and "~170K lines of docs" should be cited as 693 notes and ~90.9K English lines** when the intent is content volume.

---

## Bottom line

The revisit earns its place. One clone — the thing v235 flagged it lacked — **falsified three of that ship's four load-bearing caveats, halved two of its headline scale figures, reduced a six-ship version ladder to 69 minutes of version strings, and found the 23-line file that explains why the corpus had six plugin subjects to write about in the first place.**

What the project actually is: a **68-day-old, closed-to-external-PRs, MIT, developer-preview agent runtime** with unusually good engineering discipline in the places that can be mechanised — deny-by-default install scripts, a mirror-free lockfile, exemplary vendor attribution, real cross-platform sandboxing, ~299K lines of tests, numbered postmortems, recorded rejections, and a git merge driver for its own bilingual invariant — and **a complete absence of evaluation**, which is the one gap the whole ecosystem inherits.
