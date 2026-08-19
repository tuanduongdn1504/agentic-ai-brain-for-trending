# (C) ego lite — Deep Dive

**Subject:** `citrolabs/ego-lite` — "ego lite", a macOS browser built so a human and any number of external AI agents can share one browser, plus `ego-browser`, the open connection layer that exposes the browser to any agent CLI as a JavaScript tool surface.
**Wiki:** v247 · **Date:** 2026-08-19 · **Licence:** MIT (repository) · **Page-stated:** 11.9k ★ / 624 forks / 33 watchers
**Source-cloned twice.** Working tree at `main` = `c46a439e7fbad90ad33dbea6c6af329b6009809f` (2026-08-10), **150 tracked files (148 regular + 2 symlinks) / ~26,800 lines**; **23 unit-test files** (22 `.test.mjs` + 1 `.test.js`, ~297 `test()` calls) and **24 real-browser e2e case modules registering 31 cases**. Blobless history: **245 commits on `HEAD`, 415 on `--all`, 70 refs, 21 tags, 2 roots, 13 distinct author identities.**
**Collision:** CLEAN — `ego-lite`, `citrolabs`, `ego.app`, `ego-browser` appear **zero** times in prior vault state (hand-grep across `CLAUDE.md`, `_state/`, `_patterns/`, `PATTERN_LIBRARY.md`).

> ⚠️ **§37.4:** the GitHub API is mocked in this environment. Stars/forks/watchers are **page-stated**, never API-verified. **No Pattern #52 (viral-velocity) claim is made or implied**, and no stars/day figure is computed as fact.

---

## 1. What it is, and where the line is drawn

ego lite is a **Chromium-based daily-use browser** that partitions itself into **Task Spaces** — isolated browsing contexts, each owned by either `agent` or `user`, each with its own tabs, **all inheriting the user's login state by default**. You browse in front; agents work in the background in their own Spaces; neither steals the other's tabs.

`ego-browser` is the open half: a Node.js CDP harness that agents drive by writing a JavaScript snippet into a heredoc:

```bash
ego-browser nodejs <<'EOF'
const task = await useOrCreateTaskSpace('inspect example page')
await openOrReuseTab('https://example.com', { wait: true, timeout: 20 })
cliLog(await snapshotText())
EOF
```

**The boundary is declared, in words, in two places** — and this is the single most important fact about the repository:

- `README.md` (License): *"The contents of this repository are released under the MIT License. **The ego lite browser is a separate, free download.**"*
- `AGENTS.md:3-5` (Project Overview): it drives the browser *"through `globalThis.ego` bindings (**provided by the closed-source ego lite app**)"*, and *"This repo contains the open-source harness and the agent skill package — **not** the browser itself."*

The browser is a `.dmg` from `cdn.ego.app`. So the repository is MIT, and the artifact that does the interesting work is a closed binary you download separately.

**Against v244 → v245 → v246, this closes a set of four.** Those three ships each found a licence in prose that did not describe the artifact that runs: v244 OpenSandbox **over-asserted** an identity its governance doc never named; v245 Unsloth **under-asserted** one its packaging enforced; v246 needle **split** one across two repos and never mentioned the restrictive half in 44 files. **v247 splits one too — and says so, unprompted, in the two files a reader and an agent open first.** It is the counter-example the set needed, and it costs one sentence.

### What the closed half actually holds

The mapping pass located the transport precisely. `ego-browser` opens **no port and no socket**. `src/browser-runtime.ts:27-35` requires `globalThis.ego.sendCDPMessage`; the app injects the SDK into the Node process (`installEgoSdk(globalThis)`). Every CDP message goes out through a function handed in by the binary.

Consequently the README's differentiator — *"the strongest page Snapshot on the market … thanks to **kernel-level customization** … reliably handles deeply nested iframes"* — **is not in this repository.** `src/driver/observe.ts` is ~139 lines and calls `browserEgo().snapshot(options)`: a method of the binary. There is no iframe traversal, no accessibility-tree construction, no "kernel-level" anything in the open code.

🔴 **Do not cite this repository as evidence of snapshot or iframe innovation.** This is **v242's D25 applied to a component**: what is verifiable here is that the claim is *made*, not that it is *true*.

---

## 2. THE HEADLINE — this project writes excellent checks and does not connect them

Its own `CONTRIBUTING.md` states the doctrine, as one of four named Design Principles:

> **Goal-Driven Execution** — *"Translate the task into a verifiable goal; **write the check first**, then iterate until it passes."*

It then writes better checks than most repositories in this corpus, and leaves the best ones wired to nothing.

| Check | What it is | Wired to |
|---|---|---|
| `scripts/mutation-check.mjs` | **Real mutation testing**, hand-rolled in ~370 lines on `acorn`: parses compiled JS, injects operator flips / return swaps / boundary shifts into *named focus functions*, runs that module's test file, reports kill rate | **NOTHING** |
| `scripts/validate-agent-style.mjs` | Lints **agent-facing prose** (`SKILL.md`, `README.md`, every `learnings/**/*.md`, every e2e case) for patterns that teach an agent badly — fixed-coordinate `page.mouse.click(x,y)`, `page.waitForTimeout(>=1000)`, `page.locator("text=")`, `page.evaluate(String.raw + querySelectorAll)` — with an `agent-style-ok` escape hatch | **NOTHING** |
| `.github/workflows/publish-ego-browser-skill.yml` | Version normalisation from the tag, **a token-leak scanner over the release archive**, SHA256-pinned CLI download, dry-run, post-publish verification | **NEVER FIRED** (§4) |
| `npm run validate:site-skills` | Validates every site-learning manifest, rejects temporary `@N` refs in learnings | **ci.yml + quality-gates.yml + publish + pre-commit — all four** |
| `scripts/run-real-browser-e2e.mjs` (24 case modules / 31 registered cases) | The only tests that touch a real browser | **pre-commit hook only** |

`mutation-check.mjs` is the sharpest of these. Its `MODULE_MAP` targets exactly the predicates whose silent failure would hurt: `isAgentOwned` and `findMatchingTaskSpace` (does the agent own this Space, or is it about to seize the human's?), `boxModelCenter` (is the click landing on the element or the viewport corner?), `isStaleBackendNodeError`, `hasReturnStatement`. **It is a mutation tester aimed precisely at the functions where a confident wrong answer does damage — and no gate runs it.** Verified: `grep -rn "mutation" .github/ lefthook.yml CONTRIBUTING.md AGENTS.md` returns one unrelated line about DOM mutation.

`validate-agent-style.mjs` is the rarer artifact: **a style linter whose target is the prose that instructs a language model.** It is not a prose-vs-code consistency check (v240's rule) — it is prose-vs-*doctrine*. I initially suspected it was theatre, since the shipped skill uses ego's own helpers rather than Playwright's `page.*` API. **That was wrong:** the e2e layer exposes a Playwright-compatible surface (`cases/playwright-*.mjs`, and 122 `page.mouse.click|page.waitForTimeout|page.locator` occurrences across the linted case files), and there is exactly one `agent-style-ok` suppression in the tree, with a stated reason (`cases/helper-surface.mjs:80`, a deliberate `text=` compatibility assertion). **The linter is real, targeted, and has been run and tuned by hand. Nothing invokes it automatically.**

### The e2e placement is the *right* answer to v246's problem

v246 needle shipped a **daily automated PyPI publish** behind `pytest -q -m "not slow"` where every engine-touching test was skipped or deselected — and `pytest` reports a skip as success. The gate could not fail for the thing being shipped.

ego lite faces the same structural problem — its real tests need a closed macOS browser that cannot run on `ubuntu-latest` — and solves it in the opposite direction: **it moves the test to where the dependency exists.** `lefthook.yml` runs seven pre-commit gates, and the last is `e2e-test: npm run e2e`, the real-browser suite, on the developer's machine where the browser is installed. CI then runs only what CI can honestly run: prettier on changed files, `npm audit --audit-level=moderate`, `tsc --noEmit`, `npm test`, `validate:site-skills`. **Nothing in CI pretends to have exercised the browser.**

That is a genuinely better answer than v246's, and it generalises: **put the test where the dependency is, and let the gate claim only what it ran.**

⚠️ **The honest caveat, and the mapping pass found the sharp end of it:** a pre-commit hook is opt-in (it exists only if `npm install` ran `prepare` → `lefthook install`), bypassable with `--no-verify`, and **the e2e requirement is not stated in `CONTRIBUTING.md`.** So the coverage is real, unenforced, and undocumented — a silent contract. Nothing anywhere proves the browser suite ever ran before a merge.

---

## 3. THE SHARPEST FINDING — a committed gate that 66 of 82 merges contradict

`.github/workflows/main-pr-source.yml` is nine lines and one rule:

> *"Pull requests into main must come from the dev branch."* — it fails any PR into `main` whose `github.head_ref != "dev"`.

It was added **2026-06-01** (`aefa07f`, *"Require developer branch for main PRs"*) and is an ancestor of `main`.

Measured against the history it governs:

- PR merges into `main` **since 2026-06-01: 82**
- of those, from `citrolabs/dev`: **16**
- of those, from a branch the gate is written to reject: **66** — including **HEAD itself** (`#248 from citrolabs/section9-lab-patch-3`), plus `#249`, `#247`, `#164`, `#147`, `#141`, `#124`, `#114`, `#112`, `#106`, `#103`…

And the documentation disagrees with itself about the same process:

| Source | Says |
|---|---|
| `main-pr-source.yml` | PRs into `main` **must** come from `dev` |
| `CONTRIBUTING.md:322` | *"merge features into `dev`, cut beta tags from `dev`, then merge `dev` to `main`"* — agrees |
| `CONTRIBUTING.md:283` | *"**Branch from latest `main`**: `git checkout -b <type>/<short-description>`"* — **contradicts both** |
| `lefthook.yml` pre-commit | fetches **`origin/dev`** and refuses to commit unless it is an ancestor of your HEAD |
| Branch topology | `main` is **32 commits ahead of** `dev`; `dev` is 20 ahead of `main` — **they have diverged**; `main` carries PR #248, `dev` only #128 |

Follow `CONTRIBUTING.md:283` — branch from latest `main`, which is what a cloner gets — and the project's own pre-commit hook blocks your first commit, because `main` is not a descendant of `dev`; then the CI gate rejects your PR, because your head ref is not `dev`.

⚠️ **What I can and cannot claim.** Verifiable: the workflow exists, its predicate, its add date, and that 66 of 82 post-gate merges have head refs it rejects. **Not verifiable from the repository:** whether the workflow is configured as a *required* status check — that lives in GitHub branch-protection settings, which are not in the tree. This is **v244's D28 run in reverse**: D28 said an absent config file is not an absent check; the converse holds too — **a committed CI rule is not an enforced one.** No accusation is made. The finding is a measurement: *the rule this repository commits and the history this repository records disagree 66 times.*

⭐ **And the detector is portable, which is this ship's method contribution.** v246 handed the vault `grep -rni "silent" .`; v247 hands it a second one-command audit: **take a gate's own predicate and test it against the history it was supposed to govern.** Any repo, any gate.

---

## 4. The version fact exists in five places; the one machine that would reconcile them has never run

| Location | Declares |
|---|---|
| `skills/ego-browser/SKILL.md` frontmatter | `version: "1.2.6"` (`date: "2026-07-20"`) |
| `.claude-plugin/marketplace.json` → plugin | `1.2.5` |
| `.codex-plugin/plugin.json` | `1.2.5` |
| `.claude-plugin/marketplace.json` → metadata | `1.0.0` |
| `package/ego-browser/package.json` | `0.1.0` (name: `ego-browser-v2`) |
| newest git tag (`--sort=-v:refname`) | `v1.3.1-beta.6` |

`publish-ego-browser-skill.yml` **rewrites `SKILL.md`'s `metadata.version` from the git tag** at publish time, so the committed `1.2.6` is meant to be a placeholder CI normalises. That mechanism would make one of the six authoritative.

🔴 **It has never executed.** The workflow triggers on tags matching `[0-9]+.[0-9]+.[0-9]+` — **no leading `v`**. All 21 tags in the repository are `v`-prefixed (18 matching `v*.*.*`) or legacy two-component (`1.1`, `1.2`, plus a mutable `latest`). **Zero tags match the publish trigger.** So the version normalisation, the token-leak scanner, the dry-run, the post-publish verification and the SHA256-pinned CLI download have all sat unexecuted since the workflow landed.

⚠️ **This corrected my own earlier framing**, and the corrected version is the better finding: I had credited CI with keeping the skill's version honest. The mechanism is written; the tag convention the project actually uses does not match the trigger it declares; nothing has ever normalised anything. That also *explains* the drift instead of merely noting it.

They have been here before. `322b20b` — *"chore: align Codex and Claude plugin versions"* — aligned the two plugin manifests **by hand**. They have since drifted from `SKILL.md` again. **This is exactly v245's D32 case: hand-alignment does not hold, and there is no precedence sentence.** One line in `SKILL.md` — *"the git tag is the source of truth; if this file disagrees, this file is stale"* — would make the drift harmless and self-diagnosing. It is absent.

⚠️ The documented install paths are unaffected: `npx skills add citrolabs/ego-lite` reads the GitHub repo directly, and the `.dmg` is a CDN download. What has never happened is the **registry** publish to ClawHub and SkillHub.

---

## 5. The documentation ledger — and a refinement of the vault's own D22

Five verified defects, all in **human-facing** docs. The **agent-facing** doc is clean.

| # | Defect | Evidence |
|---|---|---|
| 1 | `CONTRIBUTING.md` links to `skills/ego-browser/SKILL.zh.md` — **deleted** | link at `CONTRIBUTING.md:6`; file absent; deleting commit `1a7f293` *"Delete skills/ego-browser/SKILL.zh.md"* |
| 2 | `CONTRIBUTING.md` attributes the Four Principles to `AGENTS.md` — *"(see `AGENTS.md`)"* — and **`AGENTS.md` contains none of them** | grep for all four principle names across the tree returns **only** `CONTRIBUTING.md` |
| 3 | `CONTRIBUTING.md:46,198,274` and `package/ego-browser/README.md:66` teach snapshot refs as **`@eN`** — the format `AGENTS.md:17` explicitly flags as wrong: *"refs are numeric `backendNodeId`s (`@21`, **not `@e21`**)"* | 4 occurrences vs 1 explicit warning |
| 4 | `AGENTS.md:33` names `scripts/run-e2e.sh` — absent from the tree (the file is `run-real-browser-e2e.mjs`) | in history at `f4ae5dc`/`6c443f8`/`44d19a7`, gone from HEAD |
| 5 | `AGENTS.md:41` describes `npm run e2e` as the *"task-space e2e suite (`src/taskspace-e2e.test.mjs`)"*; `package.json` maps `e2e` → `node scripts/run-real-browser-e2e.mjs` | the taskspace test runs under `npm test`, not `npm run e2e` |

`SKILL.md` — 209 lines, the file that ships to every agent — carries **none** of these. It uses `@N` correctly throughout, and every path it references resolves.

⭐ **This refines D22.** The vault's rule (v241) says *agent-facing prose goes stale first*. **Here the agent-facing prose is the freshest artifact in the repository**, and the developer-facing prose has rotted in five places. Same repo, same authors, same 73 days — a controlled comparison.

The mechanism is not audience, it is **contact**. `SKILL.md` is read on every single agent run, is the artifact CI rewrites, is what publishes to two registries, and its errors surface immediately to a user who complains. `CONTRIBUTING.md` is read by almost nobody and checked by nothing. So the corrected rule:

> **Prose goes stale in proportion to how little machinery and how few readers touch it — not by whether its audience is a human or a machine.** D22's prediction was right about ToolJet and inverted here; the underlying variable is consumption.

For the vault this cuts directly: `CLAUDE.md` is read every session (high contact — and indeed it is maintained), while `_state/03c`'s filename label has lagged since v183 and `_patterns/06` drifted from the shim — the two lowest-contact surfaces. **The v246 E3 error (a stale premise from the shim fed to 14 agents) is the same mechanism.** And `help()` below is the fix pattern.

---

## 6. The best artifact: an agent-facing contract, and the one thing it never mentions

`skills/ego-browser/SKILL.md` is, on the merits, **the strongest agent-facing contract in the corpus** — ahead of v246's `llms.txt`, because it does something llms.txt does not: it tells the agent how to *behave*, not just what to call.

**Three things it does that are worth stealing outright.**

**(a) The write-probe discipline** — an empirical self-check against a known silent-failure mode:

> *"Before writing substantial content into a rich editor, perform a tiny **write probe**, then verify it … If the probe appears in the title bar, toolbar search, hidden input, or any wrong field, **stop using DOM/input helpers for that surface** and switch to screenshot-guided mouse actions plus real keyboard operations."*

This is **v246's doctrine at the instruction layer**: it converts "I filled the form and the document is unchanged" from a confident wrong answer into a detected one, for the price of one small write. It generalises to any agent action whose effect is hard to observe.

**(b) Failure as the correct outcome.** On losing control of a Space:

> *"A 'user is controlling' error is a **hard stop on the whole task** — not an obstacle to route around. It means the user has deliberately taken the browser back, often because your current approach is going wrong. **Honoring it *is* the correct outcome here; pushing the goal forward anyway is the failure.** The only thing you may do is ask the user and wait."*

That is a rule written by someone who has watched an agent grind past a human's intervention. Naming deference as *success* rather than as a constraint is the right way to instruct a model that is optimising for task completion.

**(c) A named, tabulated ownership model.** Every Task Space is `agent` / `agentDelegatedToUser` / `user`, and `SKILL.md` tabulates what each of seven helpers does when the target is user-owned (`switchTaskSpace` throws; `handOffTaskSpace` resolves `{done:false, skipped:'user-owned'}`; …), plus *"Check `done` before telling the user the handoff is finished."*

### 🔴 The tension: a prose guardrail on an unguarded primitive

The same ownership table records that `takeOverTaskSpace` has **no ownership check**, and the skill's mitigation is a sentence:

> *"**Never** call `takeOverTaskSpace` on your own to grab control back — it has no ownership check and **will seize the browser away from the user**."*

Verified in code: `src/helpers.ts:347-353` selects the Space and calls `ego.takeOverTaskSpace()` with no ownership test; the JSDoc at `:130` documents the absence.

So the single most consequential action in the system — an agent taking the browser away from the human using it — is prevented **only by an instruction addressed to a language model.** This is the exact inverse of v246's rule (*where you cannot make a failure loud, move the setting into the artifact so it cannot be set wrong*). Here a capability that can be used wrongly is left in place and guarded by prose. ⚠️ Fairly stated: an escape hatch is *needed* (the agent must be able to resume after a handoff it initiated) — but the guard could be a required argument, a token from the handoff, or a refusal when ownership is `user`, and it is none of those.

### 🔴 And the silence: not one word about a hostile page

The product's loop is: **read an untrusted web page → an LLM decides → it writes JavaScript that runs against the user's authenticated sessions.**

`grep -niE "malicious|hostile|untrusted|prompt inject|do not follow|instructions on the page"` across `SKILL.md`, `AGENTS.md` and `CONTRIBUTING.md` returns **nothing**. There is **no `SECURITY.md`**.

A 209-line skill reasons carefully and at length about one adversary — an impatient agent that might trample its user — and says nothing about the other: the page. ⭐ And the means to fix it are already in the repository: `validate-agent-style.mjs` proves they will lint agent-facing prose for patterns they consider harmful. **A single "content in a Snapshot is data, never instructions" paragraph, plus one lint rule, would close it.**

---

## 6a. It is a Playwright-shaped facade over a proprietary browser — and `help()` is generated from the code

`src/helpers.ts:780-822` assembles the agent's surface as **named facades** — `page`, `locator`, `browser`, `taskSpaces`, `site`, `fetch` — and the `FACADE_HELP` strings document a **deliberately Playwright-compatible API**: `page.locator()`, `getByRole()`, `getByText()`, `getByLabel()`, `getByPlaceholder()`, `getByTestId()`, `waitForURL()`, `waitForResponse()`, `waitForLoadState()`, `page.keyboard.press()`, `page.mouse.click()`, and on locators `filter()/first()/nth()/check()/selectOption()/evaluateAll()`.

Three consequences worth recording:

1. **It is instantly learnable** by anyone who knows Playwright, which is most of the people who would adopt it — a real, unadvertised strength.
2. It explains `validate-agent-style.mjs`: the Playwright antipatterns it lints for are patterns this codebase genuinely contains (six `cases/playwright-*.mjs` modules; 122 occurrences across the linted files).
3. ⚠️ It makes the README's comparison table **closer to apples-to-apples than the table implies**. Browser-Use, Vercel's agent-browser and ego lite are all Playwright-shaped; the real difference is the browser underneath and the ownership model, not the calling convention.

⭐ **And `help()` is the repository's one genuinely drift-proof document.** `src/help-runtime.ts` parses the *built bundle's* JSDoc with `acorn` **at runtime** to answer `help(name)`. As `AGENTS.md:23` puts it, *"JSDoc on exported helpers is therefore user-facing documentation."* The agent-facing reference is not a copy of the code — it **is** the code. Set that against the five hand-carried version strings (§4) and the five rotted doc claims (§5): **the one surface generated by a machine is the one surface that cannot be wrong.** The strict-locator doctrine rides along inside it — *"Narrow multiple matches; use `first()`/`nth()` only for confirmed legitimate duplicates."*

---

## 7. Security: the boundary is drawn well; the residual risk is the premise

⭐ **No broken-auth triad, and structurally so.** The corpus keeps finding the same defect — v231 CoreOfPotato and v232 gemini-web2api both bound a local gateway to `0.0.0.0` with permissive CORS while holding live authenticated sessions. ego-browser **cannot** have that bug in this layer: it opens **no listener at all**. There is no port, no socket, no HTTP server; the transport is a function the app injects (`globalThis.ego.sendCDPMessage`). It notably does **not** take the usual shortcut of exposing Chrome's `--remote-debugging-port`, which is how most "connect your agent to your logged-in browser" hacks work and is precisely the failure mode this corpus has documented twice. Credit where due.

⚠️ The consequence for a reader: **the authorization model — who may drive the browser — lives entirely in the closed app and cannot be audited.** Fairly stated: the open layer cannot be faulted for lacking auth, and cannot be credited with having it.

**The residual risk is the product's own premise, and it is large.** Within a Space that inherits the user's logins:

- `js()` is `Runtime.evaluate` — arbitrary JavaScript in the authenticated page (`src/cdp-eval.ts`).
- `browserFetch()` issues requests **from the page context** and returns the body (`src/http.ts:29-52`) — i.e. arbitrary authenticated reads, exfiltratable to any origin.
- `serverFetch()` fetches from Node with a spoofed `User-Agent: Mozilla/5.0` default (`src/http.ts:11-27`).
- `uploadFile()` puts local files into a page; `driver/downloads.ts` pulls files down.

Combined with §6's silence, **prompt injection from page content is the whole threat model, and it is unaddressed.** A page that says the right thing to an agent holding your session can move money, mail, or data.

Two smaller, precise items:

- **`.env` is loaded from two locations** — `src/env.ts:47-48` reads `.env` from the repo root *and* from `agentWorkspace()`, which is `EGO_BROWSER_AGENT_WORKSPACE` or the installed skill directory. Whatever `.env` sits beside the installed skill becomes environment for agent-authored JavaScript. Mitigating: it only sets variables that are currently undefined.
- **Validating a site-learning executes it.** `src/learning/validate-learning-format.ts:66` does `await import(pathToFileURL(toolPath).href + "?validate=" + Date.now())` — so `npm run validate:site-skills`, which runs in CI, in the publish job and in the pre-commit hook, **imports every learning's JavaScript**, executing top-level module code, with a cache-buster so it re-runs every time. ⭐ Correctly, `quality-gates.yml` triggers on `pull_request` (not `pull_request_target`), so fork PRs run **without secrets**, and the publish job runs only on tags. The exposure is CI compute, not credentials — the right configuration, and worth saying so.

---

## 8. Supply chain — better than v246's, with one gap

⭐ **One runtime dependency.** `package.json` declares exactly **`acorn ^8.16.0`**, plus 9 devDependencies (esbuild, rollup, typescript, prettier, lefthook, tslib, types/node, two rollup plugins). No Playwright, no Puppeteer — because the CDP transport is the binary's. A browser-automation harness with a single production dep is a genuinely small attack surface. ⚠️ The trade is explicit: the dependency surface is small *because* the heavy code is a closed binary.

⭐ And `acorn` is reused rather than duplicated: it powers `mutation-check.mjs`, `extract-help-docs.mjs`, and `help-runtime.ts`. Consistent with their **Simplicity First** principle.

⭐ **`npm audit --audit-level=moderate` runs in both the pre-commit hook and CI.**

⭐ **The strongest single line in the release path** — a token-leak scanner over the artifact about to be published:

```
if grep -R -E '(clh_|skh_|pt-)[A-Za-z0-9_-]{16,}' "$RELEASE_DIR"; then
  echo "Release archive contains a token-like value." >&2; exit 1; fi
```

It scans for **its own registries' token prefixes** and fails closed. ⚠️ It has never run (§4).

⭐ **A mutable URL made immutable by a committed hash.** The SkillHub CLI is fetched from a Tencent Cloud bucket at `…/install/latest.tar.gz` — a mutable `latest` — and then verified: `SKILLHUB_CLI_SHA256: af9e0763…` piped through `sha256sum --check -`. That is the correct way to consume a `latest` URL, and it fails closed when the upstream rotates. **This is better than v246's "pinned-but-unverified over TLS" and far better than v234's plaintext-`http://` installers.**

⚠️ Gaps, stated plainly: deps are **caret-ranged, not pinned** (a lockfile exists); `npx -y clawhub@0.21.0` is version-pinned but not hash-pinned and auto-installs; `prepare` installs git hooks into `.git/hooks` on a developer `npm install` (skipped when `CI=true`, and documented in `lefthook.yml`'s header comments); and the `.dmg` URL is **an opaque fixed filename with no version in it** (`egolite-Y7MbxKIuhzFB.dmg`), so you cannot pin, diff, or name what you installed. Compared to the corpus's positive exemplar (pi v228: pinned + `save-exact` + `min-release-age` + `--ignore-scripts` + shipped shrinkwrap), this is mid-table with two standout individual practices.

---

## 9. Provenance

**AI authorship: 102 `Co-Authored-By` trailer lines across the 415-commit `--all` population, on 102 distinct commits** (ratio exactly 1.0 — consistent with **merge-based** integration, not squash; per v244's D26 extension, and corroborated by HEAD being a merge commit). Of those:

- **Claude: 91 lines across five model strings** — Opus 4.8 (1M context) ×36, Opus 5 (1M context) ×21, Opus 4.8 ×15, Fable 5 ×11, Opus 5 ×4, Opus 4.7 ×4
- Copilot App ×10

⚠️ **Both the key form and the value form were counted** (v245's error was a key-form grep missing 104 value-form lines). And **no policy asks for them**: `CONTRIBUTING.md`, `AGENTS.md` and `pull_request_template.md` mention no AI-disclosure or trailer requirement. **A left-on default, not a practice** — the v243 finding, third instance (v243: 905 lines; v246: 21; v247: 102).

⭐ Branch names carry the provenance instead: of 70 refs, **15 are `codex/*`** and one is `agents/playwright-style-refactor-v2` — the v242 pattern (*built with one tool, ships for another*) again, and here the repo packages for **both** Claude Code and Codex as first-class targets.

**Two roots** (v245's D19 EXTENDED — count the roots): `144b0734` (2026-05-27) and `f4ae5dcf` (2026-05-29). **`f4ae5dcf` is HEAD's ancestor; `144b0734` is not** — an orphan lineage in the ref graph. So the live history is ~73 days, and the 415-vs-245 gap is 70 refs of PR branches, not a hidden second project. **D27 declared:** every count above states its ref population.

**Identity (§41 → (a) FAIL).** Copyright *"(c) 2026 CitroLabs"*; contact `contact@citrolabs.ai`; site `lite.ego.app`. The dominant committer is **"Tachikoma" `<section9lab@gmail.com>`** (216 of 415), and ClawHub publishes under `--owner section9-lab`. *Tachikoma* and *Section 9* are Ghost in the Shell references. No real name, company registration, or funding statement appears anywhere in the tree. Facts about the repository, recorded as facts and not as conclusions about people: commit timezone is `+0800`; the SkillHub host is `api.skillhub.cn` with a Tencent Cloud Guangzhou bucket; an e2e fixture is modelled on a Chinese ticketing flow. **No inference is drawn from any of these** — §41 answers (a) NO on the absence of a declared Anthropic affiliation, nothing else.

⚠️ Worth stating for a product that asks to inherit your entire logged-in browser state: **who is accountable for the closed binary is not established anywhere in the repository.**

---

## 10. Claims audit

| Claim | Status |
|---|---|
| *"up to **2.5×** faster"* vs Vercel's agent-browser on "four complex tasks" | 🔴 **Backed by one PNG.** `docs/assets/ego-vs-agent-benchmark.png`. No data file, no task list, no harness, no reproduction script anywhere in 148 files. README says *"Check the comparison."* with **no link**. **Do not cite this number.** ⚠️ Sharper than v246's equivalent: ego lite **has** a 24-module / 31-case real-browser harness and did not use it for the one number in its README. |
| *"substantially fewer tokens"*, *"higher task success rates"*, *"far fewer tool calls"* | 🔴 Unsupported by any artifact in the repo. |
| *"up to **5×** faster"* (Experience accumulation) | ⚠️ A claim about a feature the same table marks **"(coming soon)"**. |
| *"strongest page Snapshot on the market"* / *"kernel-level customization"* / *"deeply nested iframes"* | 🔴 **Not in this repository** (§1). Unverifiable here. |
| *"Zero cost, zero config"* | ⚠️ Zero cost: yes, both halves are free. Zero config: substantially true — install adds the skill to every agent's skills directory, and the documented flow is one `npx` command or one paste. |
| The 10-row comparison table | ⚠️ Mostly defensible as a *category* claim; two rows deserve care. **"Reusable skills — Browser-Use: —"** is contestable: Browser Use ships its own MIT Claude Code skill (this corpus's **v198 video-use**). Under a narrow reading — *per-site, machine-consumable capability packs* — ego lite's `learnings/` format is genuinely distinct and the ✓ is fair. Under the plain reading a reader will take, it is misleading. **"Free — Atlas / Comet: —"** compares a free browser against subscription tiers of paid assistants; directionally true, imprecise. |
| *"Experience accumulation … distills every successful action into reusable tools"* | ⚠️ **Consume-side works; accumulate-side does not exist here.** `src/learning/` (701 lines across 3 files) discovers, validates and executes learnings; the only `writeFile`/`mkdir` calls are in `learning/index.test.mjs`, creating fixtures. **Nothing in this repository writes a learning.** The two shipped packs (`google/`, `x-com/`) are hand-curated. ⭐ The README's **"(coming soon)"** label is therefore **accurate** — this is honest labelling, not a false claim. |

⭐ **What the `learnings/` format actually is, and it is good:** a typed per-site capability manifest — `id`, `name`, `domains` (with wildcards), `notes[]`, `nodeTools{}` and `browserTools{}`, each tool carrying `description`, `path`, `callable`, `args` (typed, with `required` and per-arg descriptions) and `returns`. It is **an MCP-style tool schema for a website, stored as files**, validated by the one check they wired everywhere, which also **rejects temporary `@N` refs** so a learning cannot encode a throwaway snapshot ref. Whether or not anything ever generates one, the format and its runtime are real.

---

## 10a. Prior art, world-firstness, and the mint

**Verdict: NOT world-first. NO MINT.** Each of the three components has strong, established prior art:

| Component | Prior art that defeats a firstness claim |
|---|---|
| A daily-use browser whose agent reaches your real logins | **Anthropic's Claude in Chrome** (drives your Chrome with your sessions), **ChatGPT Atlas**, **Perplexity Comet** — the README's own table concedes Atlas and Comet inherit Chrome data |
| Isolated parallel workspaces inside one browser | **Arc Spaces** (the name is literally Arc's), **Firefox Multi-Account Containers** (cookie isolation), **Chrome profiles**, and the entire **anti-detect browser** category — multi-profile isolation *is* that category's product (this corpus: CloakBrowser v69, camofox v179) |
| A browser drivable by an external agent | **CDP / Playwright**, **Playwright MCP**, **Chrome DevTools MCP**, **browser-use** (v41), **Vercel agent-browser**, Stagehand/Browserbase |

⚠️ And a live competitive fact from the search: **Arc and Brave are shipping first-class agent APIs, and Arc's includes a permission system letting developers declare in a JSON config what an agent may touch** — a control ego lite does not have (§7).

**What actually is distinctive** is narrower than the marketing and worth naming precisely: **the per-Space ownership state machine** — `agent | agentDelegatedToUser | user`, with `handOff` / `takeOver` / `claim` / `waitForAgentControl` as first-class operations, a tabulated policy for what each helper does against a user-owned Space, and a doctrine that names deference as success. I did not find that primitive elsewhere. ⚠️ But per the vault's own discipline — **absence of evidence is not evidence of firstness** (the argument a v246 agent got wrong and had rejected) — "I did not find it" is not "it does not exist."

**NO MINT, on four independent grounds** (the collision agent and the critic reached the same conclusion independently):

1. **Form-factor-within-a-genre.** A browser is a product genre. The corpus has ruled this way twice — **lobehub v222** (*fame is not a mint*: world-*canonical* is not world-*first*) and **hermes-webui v227**.
2. **A combination is not a capability class.** All three components are occupied; what is new is the intersection plus a state machine. §C vocabulary is tool/capability-shaped.
3. **The distinctive machinery is not in the subject** (§1) — the same ground on which v246 declined.
4. **§28** anti-re-accumulation, with the N=1 gate: one instance of an ownership model is not a recurring pattern.

⭐ **Recorded, not executed — the losing alternative.** The strongest mint framing is *not* the browser but the pattern: **"Human+Agent Shared-State Co-Habitation with Per-Workspace Ownership Handoff."** It is genuinely repeatable — any browser, and arguably any shared resource an agent and a human contend for (an IDE, a terminal multiplexer, a design canvas). If a second independent implementation ships, that is a real N=2 and a real candidate. **Recorded as a DEFERRED watch axis at N=1; not minted, and not self-promoted — a promotion is an audit act** (the v232 rule).

⭐ **Instance-strengthening, recorded not incremented:** this is a clean further instance of **Library-vocab #12 (LLM-routing / agent-facing artifacts, CONFIRMED N=5+)** by way of `SKILL.md` + `llms`-class contracts, and of the **cross-harness packaging** family (`.claude-plugin/marketplace.json` + `.codex-plugin/plugin.json` + two real symlinks + `agents/openai.yaml` = **four harness targets from one canonical skill**). N-tallies are audit bookkeeping.

⚠️ **Not a v192 instance.** The palmier-pro v192 standalone ("Product-First Native Application Retrofitted with a First-Party MCP Server") is at N=5 and promotion-flagged, so its boundary must not be blurred casually. Two reasons it does not cover this: ego lite ships **a skill, not an MCP server** (there is no MCP server anywhere in the tree — verified), and it was **built agent-first from the start rather than retrofitted**. Both halves of that row's name fail. **Do not count v247 toward it.**

### The commercial tier — a suspicion tested and dropped

CitroLabs sells a subscription **`ego`** (the full personal agent) and a **Business** tier; `ego (lite)` is the free community edition. The repository mentions this **nowhere** (verified: no `enterprise|subscription|pricing|commercial|premium` hit across all 148 files outside unrelated test identifiers).

Given §1's framing I expected this to be a second, quieter omission. **It is not, and the fair finding is the opposite.** `lite.ego.app/enterprise` prices the free tier at *"$0 forever"* and the Business tier as *"priority support with response SLA, custom integrations and guided onboarding, volume and deployment terms"* — **services, not withheld features.** No capability is paywalled and no licence expires. The v246 omission mattered because the omitted fact changed *what you were permitted to do*; this one changes nothing about your rights or your software. **The README's "Free ✓" row is defensible.** ⚠️ The enterprise page also asserts *"100% local & private: no account, no email, bring your own model API key"* and no telemetry — a stronger privacy claim than the README's, unverifiable for a closed binary, but a public commitment a user can hold them to.

---

## 11. What to borrow (zero install)

1. ⭐⭐⭐ **The write probe.** Before any hard-to-observe write, do a tiny one and verify where it landed; if it landed wrong, change *technique*, not parameters. Straight into `CLAUDE.md` — it is the cheapest known defence against a confident wrong answer, and it composes with v246's loud-failure rule.
2. ⭐⭐⭐ **Test a gate against the history it governs.** One command; found 66 of 82. Portable to any repo, and pointable at the vault's own `bin/` checks.
3. ⭐⭐ **Declare deference as success.** Rewrite the vault's own agent instructions so that stopping when the operator intervenes is stated as the *correct outcome*, not as a limit.
4. ⭐⭐ **Generate the reference from the code.** `src/help-runtime.ts` parses the built bundle's JSDoc with `acorn` **at runtime** to answer `help(name)` — so the agent-facing helper reference *is* the code and cannot drift. Contrast the five hand-maintained version strings. The vault's analogue: derive index lines from the chapter files rather than hand-maintaining them.
5. ⭐ **The D32 sentence.** One line naming which copy wins, inside the copy that loses. They aligned two manifests by hand once (`322b20b`) and drifted again — the vault applied this at v245 for exactly this reason.

---

## 12. Errors caught this ship

**Mine, self-caught (4):**

- **E1** I credited the publish workflow with normalising `SKILL.md`'s version. **It has never fired** — no tag matches its non-`v` trigger. My characteristic error shape again: *inferring that a mechanism is operative from its existence.* The corrected finding is stronger, because it explains the drift instead of noting it.
- **E2** I hypothesised `dev` was the integration branch and `main` lagged. **Wrong** — `main` is 32 ahead of `dev`, and the two have diverged. Checking before publishing turned a wrong hypothesis into the ship's sharpest finding.
- **E3** I suspected `validate-agent-style.mjs` was theatre because its Playwright rules don't match the shipped skill's API. **Wrong** — the e2e layer is Playwright-compatible; 122 occurrences in the linted files, plus one deliberate, reasoned suppression.
- **E4** I nearly reported that `SKILL.md` documents four helpers that do not exist (`cliLog`, `js`, `snapshotText`, `wait`). **My grep could not answer the question** — the helper surface is assembled indirectly (`helperContext()` at `helpers.ts:822` returns a namespaced object; `run.ts` injects the callable surface). Recorded **NOT VERIFIED** rather than published. A narrow grep over an indirectly-assembled surface cannot test an inventory.

- **E5** I expected the unmentioned commercial tier to be a second quiet omission (§10a). **It is not** — the paid tier sells support, not features. Suspicion tested against the vendor's own pricing page and dropped. Three of this ship's five self-caught errors were suspicions that did not survive checking (E3, E5, and the `damai-rush` fixture, which I checked for ticket-scalping implications and found to be a **local** fixture that its own README states *"never contacts a real ticketing, payment, or identity service"* — verified: zero external URLs).

**The fleet's, rejected or corrected (4):**

- **A1 — a confabulation imported from my own briefing.** The critic described ego lite's closed binary as *"`libneedle.*` downloaded from cdn.ego.app"*. **`libneedle` is v246 needle's binary**, which appeared in the vault context I supplied. **Rejected and excluded.** ⚠️ The lesson is mine, not the agent's: *context supplied to ground an agent can also contaminate it*, and a prior ship's specifics are the most dangerous thing to paste into the next ship's briefing. This is the v246 E3 failure mode in a new costume.
- **A2 — "173 files".** The critic corrected my 148 to 173 and rated my number a counting error. **I re-derived all four ways: 148 regular files excluding `.git`, 150 tracked (`git ls-files`, i.e. 148 + the 2 symlinks), 173 only if you count `.git/` internals as repository files, 190 if you count directories.** The critic's 173 *is* the error — and it is the vault's signature error shape ("the number I measured was not the number I claimed to measure") committed by the agent assigned to hunt it. ⭐ The corpus rule earns its keep: **adjudicate a counting dispute with a command, not with authority.**
- **A3 — "17 test files".** A contradiction pass said 17; the critic said 23. **23 is right** (22 `.test.mjs` + 1 `.test.js`). Adopted, verified, and the header corrected. The critic was right here and wrong in A2 — which is why each number was re-derived rather than each agent being trusted or distrusted wholesale.
- **A4 — "41 helpers".** Unverified as stated; the surface is **facade-organised**, not a flat list (§6a), so a single integer misdescribes it. Replaced with the structural description.

⚠️ **Fleet reliability, stated plainly:** 11 of 12 agents completed, but **3 contradiction passes and the prior-art agent failed to produce valid structured output**, so the CI/governance, security and provenance chains dropped their verification stage and the prior-art verdict had to be researched by hand. Those are the three areas I had already covered by hand — which is why the loss was recoverable. **The mapper outputs survived in `journal.jsonl` and were recovered from there rather than assumed empty.**

⭐ **Method note, testing v246's finding.** v246 concluded that agents asked to *check a claim* rubber-stamp it (7 CONFIRMED of 8 against a "default to REFUTED" brief) while agents asked to *read the code* caught the lead's worst error. This ship acted on that: the verify stage was rewritten as a **contradiction** stage — each agent got the mapper's report as a *suspect document*, was told its job was to produce corrections by independent reading, was required to check at least six specific citations, and had to file a **read receipt** naming the files and line ranges it actually read. It produced corrections rather than confirmations. **The v246 method finding replicates, and the fix works: do not ask an agent whether a claim is true; ask it what the claim gets wrong, and make it show you what it read.**

---

*Related: v246 needle (the `silent` grep; "the machinery is not here"; the release gate that cannot fail) · v245 Unsloth (D32; D19 roots; D33) · v244 OpenSandbox (D28; the symlink-vs-stub class) · v243 ToolJet (the symlink; left-on Claude trailers; D26/D27) · v241 (D22, refined here) · v240 (the inventory rule) · browser-use v41 · camofox v179 · CloakBrowser v69 · Agent-Reach v174 · page-agent v199 · video-use v198.*
