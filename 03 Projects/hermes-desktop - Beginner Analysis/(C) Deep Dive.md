# (C) Deep Dive — hermes-desktop (Hermes One) — v268

**Subject:** [`fathah/hermes-desktop`](https://github.com/fathah/hermes-desktop) — *"Hermes One is a community maintained native desktop app for installing, configuring, and chatting with [Hermes Agent](https://github.com/NousResearch/hermes-agent)"* (`README.md:44`)
**Licence:** MIT, "Copyright (c) 2026 github.com/fathah"
**Author:** Fathah KA (`fathah` / `abdulfathahkodag@gmail.com`) — a disclosed individual, **NOT Anthropic** (§41; #19 19a)
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG
**Mint:** **NO MINT.** Counts **46 / 12 UNCHANGED**; §C-1 **12** unchanged; §C-2 **39** unchanged.
**Ship date:** 2026-08-23 · branch `wiki/v268-hermes-desktop` off the v267 tip (`a2c439b`) · **not auto-merged**

---

## 0. Source verification

✅ **SOURCE VERIFIED.** Two independent clones, `diff -rq` clean in both directions, `-x .git`.

**HEAD = `3aaadb01076a749d7f9389dca4ffce081cf8ebaa`**, 2026-08-06 19:57:28 +0530, *"Merge pull request #880 from eachann1024/fix/settings-i18n-alignment"*.

Ground truth, all via `rev-list` (git here is 2.19 — **D39**, and v267's hard-won rule that `git log` is a display command, not a counting command):

| Fact | Value | Command |
|---|---|---|
| Commits, all refs | **1301** | `rev-list --count --all` |
| Commits on HEAD | 1293 | `rev-list --count HEAD` |
| Roots | **1** — `3865859c`, 2026-04-02 19:26:42 +0400, *"Initial commit"* | `rev-list --max-parents=0 --all` |
| Merges | 396 | `rev-list --count --merges --all` |
| Distinct author emails | **82** | `log --all --format=%ae \| sort -u` |
| Tags | **50** (`v0.0.3` → `v0.7.6`) | `tag \| wc -l` |
| Span | 2026-04-02 → 2026-08-06 (**~4.1 months**) | — |
| Tracked files | **1003** — 608 `.ts`, 136 `.tsx`, 63 `.md`, 55 `.svg`, 28 `.glb` | `ls-files` |
| Fork? | **No.** Single root, owned by the account. **D49 inapplicable.** | — |

⚠️ **HEAD is 2026-08-06; today is 2026-08-23.** The default branch has been quiet for 17 days. Not established why.

---

## 1. What it is

An **Electron desktop application that installs, configures, and drives someone else's self-hosted AI agent.** Not a chat window bolted onto an API — a control plane:

- **Guided first-run install** of Hermes Agent: runs the upstream's official install script with `--skip-setup` (`README.md:336`), resolves Git/uv/Python 3.11+, stores the agent in `~/.hermes`
- **Local or remote backend** — `http://127.0.0.1:8642` with SSE streaming, or a remote Hermes API server, or an SSH tunnel
- 12 screens: Chat, Sessions, Agents, Skills, Models, Memory, Soul (`SOUL.md` persona editor), Tools, Schedules, Gateway, **Office**, Settings
- 16 messaging gateways, a cron builder, SQLite FTS5 session search, profile isolation
- **Hermes Office (Claw3d)** — a 3D office with agent avatars, 28 `.glb` models, `three` + `@react-three/fiber`
- An **Ethereum wallet** on Base mainnet (`ethers ^6.17.0`)

Substantial and real: 1301 commits in 4.1 months, 82 contributors, 50 tags, 187 test files, working CI.

---

## 2. ⭐⭐⭐⭐ The centrepiece: `lat.md`, and the empirical result nobody has produced before

### 2.1 What is in the repository

There is a directory called **`lat.md/`**. It holds **29 markdown files, 244 sections, 597 `[[wiki links]]`**, and the source tree holds **79 `@lat:` code refs** pointing back into it. It is a cross-linked knowledge graph of the project's architecture, design decisions and test specifications — **the LLM Wiki pattern this vault is built on, implemented by a third-party tool.**

The tool is **[`lat.md`](https://www.lat.md/)** — *"Agent Lattice: a knowledge graph for your codebase, written in markdown"* — published by **`1st1` = Yury Selivanov**: CPython core developer (asyncio, PEP 492 `async`/`await`), formerly co-founder & CEO of Gel/EdgeDB and MagicStack, **now at Vercel** (bio: *"Leading the Ministry of Silly Walks @ @vercel"*). His pinned repo is **`vercel-labs/lat.md`**.

⚠️ **`vercel-labs` is the same GitHub org as corpus subject v68 `zero`. That is an ORG-LEVEL COINCIDENCE, not a #57 dependency** — no corpus subject is a dependency of hermes-desktop. Recording it explicitly so a later ship does not mistake it for recursion. (This is precisely the v267 error-shape — inferring provenance from the shape of a name — declined here.)

It offers five commands (`CLAUDE.md:22-28`): `lat locate`, `lat refs`, `lat search`, `lat expand`, and **`lat check` — validate all links and code refs.**

`lat check` enforces four documented rules:
1. every `@lat:` code ref points at a real section
2. every `[[wiki link]]` resolves — to a section **or to a source symbol** (`[[src/config.ts#getConfigDir]]`)
3. every section has a leading paragraph, ≤250 chars
4. under `require-code-mention: true`, every leaf section is referenced by exactly one `@lat:` comment

And `CLAUDE.md:6-12` makes it mandatory:

> **# Post-task checklist (REQUIRED — do not skip)**
> After EVERY task, before responding to the user:
> - [ ] Update `lat.md/` if you added or changed any functionality, architecture, tests, or behavior
> - [ ] Run `lat check` — all wiki links and code refs must pass
> - [ ] **Do not skip these steps. Do not consider your task done until both are complete.**

### 2.2 I re-implemented `lat check` and ran it across the graph's entire history

`lat` is not installed here and I will not install it. So I hand-built the four rules in Node and ran them against **25 commits sampled across all 169 commits that touch `lat.md/`**, spanning **2026-06-17 (the graph's first commit) → 2026-08-06 (HEAD)**.

🔴 **My first run reported 66 violations. It was wrong, and catching it is the method result of this ship.** I had put the file's H1 into the section-id chain, so `[[wallet-token-balances#Wallet Store]]` failed to resolve — while `## Wallet Store` sits at `lat.md/wallet-token-balances.md:5`. `lat`'s own example (`# Tests` / `## User login` addressed as `[[tests#User login#…]]`, `CLAUDE.md:70`) excludes the H1. **I only caught it because I grepped the actual headings before believing my own output** — §43.1, and the fifth consecutive ship where my error was generalising from where I chose to look. It was caught **pre-publication** this time.

Corrected, the sweep:

| Probe date | files | wiki links | `@lat:` refs | **dangling links** | **dangling refs** | lead-para |
|---|---|---|---|---|---|---|
| 2026-06-17 | 3 | 7 | 4 | **0** | **0** | 0 |
| 2026-06-19 | 7 | 33 | 5 | **0** | **0** | 1 |
| 2026-06-23 | 15 | 161 | 11 | **0** | **0** | 1 |
| 2026-07-07 | 17 | 306 | 21 | **0** | **0** | 2 |
| 2026-07-14 | 22 | 432 | 43 | **0** | **0** | 2 |
| 2026-07-24 | 28 | 561 | 75 | **0** | **0** | 2 |
| **2026-08-06 (HEAD)** | **29** | **597** | **79** | **0** | **0** | **2** |

*(7 of 25 rows shown; **all 25 read `0` / `0`.**)*

⭐⭐⭐⭐ **Across 169 commits, seven weeks, and a graph that grew from 7 edges to 597, the dangling-link count and the dangling-code-ref count were ZERO at every single probe.** After v239's 97 dangling pointers, v254's and v265's citations into directories that never existed, and v267 being *"the FIRST subject to pass the v240 inventory check in BOTH directions"* — **this is a 597-edge cross-reference graph plus 79 bidirectional prose↔code refs, clean at every point in its history.** It is the strongest documentation-integrity result in 268 subjects, by a wide margin.

**And the only rule ever violated is the one whose violation breaks nothing.** Two leading paragraphs exceed the 250-character budget:

- `lat.md/model-selection.md:3` — **256 bytes**, present since the file was created on **2026-06-19**
- `lat.md/provider-setup.md:9` — **258 bytes**, appearing around **2026-07-07**

Neither contains a wiki link, so the *"excluding `[[wiki link]]` content"* clause is moot and the counts are unambiguous. They have stood **48 and 30 days**, across the remaining ~500 commits, and are still there at HEAD.

⭐⭐⭐ **Same tool, same checklist, no gate for either — and the outcome split cleanly along one line: a dead `[[link]]` announces itself to the next agent that follows it; a 256-character paragraph announces itself to nobody.** The 597 self-announcing edges are perfect. The two silent ones rotted and stayed rotten.

### 2.3 ⭐⭐⭐ Nothing has ever enforced any of it

| Surface | Runs `lat check`? |
|---|---|
| `.github/workflows/ci.yml` (44 lines) | **No.** `npm ci` → `npm run typecheck` → `npm test` (both gating) → `npm run lint` (`continue-on-error: true`, with a written reason at `:39-41`) |
| `.github/workflows/release.yml`, `beta-release.yml` | **No.** |
| `package.json` scripts (23 of them) | **No.** `lat` appears nowhere in the file. |
| `.husky/pre-commit`, `.husky/pre-push` | **No** — and see below. |
| `.claude/settings.json`, `.codex/hooks.json` | `lat hook claude UserPromptSubmit` + `Stop` — **yes, on a developer's machine, if `lat` is installed globally.** |

⭐ **`lat.md` is not a dependency.** `grep '"lat' package.json` returns nothing. The only runnable invocation anywhere in 1003 files is **`npm exec --yes --package=lat.md -- lat check`** at `docs/superpowers/plans/2026-07-14-remote-dashboard-oauth.md:228` — one line, in one plan document, for one feature.

⭐⭐ **And `.husky/pre-commit` opens with four lines that switch it off:**

```bash
BRANCH=$(git symbolic-ref --short HEAD 2>/dev/null)
if [[ "$BRANCH" != "release" && "$BRANCH" != release/* ]]; then
  exit 0
fi
```

`.husky/pre-push` is identical. So the lint+test hook and the build hook are inert on `main` and on all 90+ feature branches. **A committed hook is not an enforced one** — D34, at N=2.

⭐⭐⭐⭐ **THE FAIRNESS TEST, AND IT PRODUCED THE SHIP'S SHARPEST LINE.** Does anything tell a contributor to install the tool? Yes — exactly one place:

> `lat.md/lat.md:1` — *"It is managed by [lat.md](https://www.npmjs.com/package/lat.md) — a tool that anchors source code to these definitions. **Install the `lat` command with `npm i -g lat.md`** and run `lat --help`."*

**The instruction for installing the validator lives inside the artifact the validator validates.** Meanwhile:

- **`Development.md`** — the file titled *"Development / Prerequisites"* — lists Node.js, a Unix shell, network access. Its *"Run checks"* section is `npm run lint` and `npm run typecheck`. **No `lat`. No `lat check`.** (Read in full; 48 lines.)
- **`CONTRIBUTING.md`** — *"Run checks before submitting: `npm run lint` / `npm run typecheck`"*. **No `lat`.** (Read in full; 104 lines.)

⇒ **The human onboarding path and the agent onboarding path disagree about what is required, and neither is wrong from where it sits.** The agent is told the checklist is mandatory. The human is told to lint and typecheck. CI enforces the human's list, minus lint. Nothing anywhere enforces the agent's.

### 2.4 ⭐⭐⭐⭐ So who actually maintains the graph — and the answer is the finding

Of the **169 commits touching `lat.md/`**:

| Author | commits | share |
|---|---|---|
| Fathah KA (2 identities) | **149** | **88.2%** |
| `= <im@jai.gay>` | 9 | |
| Nazmus Samir | 4 | |
| hanlujie | 3 | |
| AmirF194 | 3 | |
| 关俊江 | 1 | |
| **five outside contributors** | **20** | **11.8%** |

Good news first: **outside contributors do edit the graph — 20 commits from 5 different people — and it never broke.** The convention travelled.

🔴 **Then the number that matters. `pmos69` / Pedro Simoes is the #2 contributor to this repository: 187 commits, 159 of them touching `src/` — across `src/shared`, `src/renderer`, `src/main` and `src/preload`, including the IPC security boundary — plus tests. His commits touching `lat.md/`: ZERO.** He also performed the product rebrand (§4). He is not a drive-by contributor; he is core, and he is absent from the knowledge graph entirely.

⭐⭐⭐ **An ungated documentation convention did not produce WRONG documentation. It produced INCOMPLETE documentation — and incompleteness is the one failure mode no link-checker can see.** `lat check` validates every edge that exists and is structurally incapable of noticing the subsystem nobody wrote down. **This is v240's inventory rule arriving from the opposite direction and confirmed empirically:** a consistency check between two views of one source cannot see what is missing from the source.

### 2.5 ⭐⭐⭐ The one enforcement flag, documented four times, used zero times

`require-code-mention: true` is `lat`'s only enforcement primitive: switch it on in a file's frontmatter and every leaf section must be referenced by exactly one `@lat:` comment.

It appears **12 times** in the repository. **All 12 are inside documentation about the feature**: `.agents/skills/lat-md/SKILL.md` ×5, `.claude/skills/lat-md/SKILL.md` ×5, `AGENTS.md:48`, `CLAUDE.md:48`.

**Zero of the 29 `lat.md/` files have frontmatter at all.**

And the cost is measurable. `lat.md/remote-dashboard-oauth.md` declares **12 test specifications** (`:59`–`:103`). **10** have a matching `@lat:` ref, from 7 test files. Two do not:

- **`Atomic first-run connection`**
- **`Raw gateway classification`**

One line of frontmatter — a feature described four times over in this very repository — would have failed the check and named exactly those two.

⇒ ⭐⭐⭐ **This extends the corpus's gate ladder to a new position:**

| ship | shape |
|---|---|
| v261 | the claim without the test |
| v262 | the gate that cannot fail |
| v263 | the test without the gate |
| v265 | the gate that prints `PASS` on the file it exists to block |
| v267 | the number computed, displayed, never compared |
| **v268** | **the gate that was never switched on** |

---

## 3. ⭐⭐⭐⭐⭐ The positive pole, in the same codebase — and it explains the whole ship

`src/main/secrets/` is a 13-file module: **4 source files (581 lines) and 9 test files (1,133 lines)** — a test-to-source ratio over 1.9:1 on the security-critical path, including **property-based testing with `fast-check`** (used in exactly 2 files in the repo, both here).

`src/main/secrets/securityInvariants.test.ts:4-24`:

> *"**SECURITY-INVARIANT SUITE** for the secrets system. This file is a **living checklist**: each `it` encodes ONE invariant that must hold for ANY secrets provider, forever. These are the cross-function properties that **diff-only review misses** and that an invariant-reasoning reviewer (e.g. Greptile) catches. **All three review-found bugs on this feature were violations of an invariant below:**
> — `resolvedSecrets()` bypassed the spawn floor → INV-2 (single spawn path)
> — `list()`/`get()` disagreed on whitespace → INV-3 (list⇔get agreement)
> — S2 guard leaked a comment-prefixed wrong key → INV-1 (no cross-key leak)
> When you add a provider or change resolution, run this. **A red line here is a security regression, not a style nit.**"*

⭐⭐⭐ **This is the best example in 268 subjects of converting review findings into permanent invariants.** Three real bugs were found; rather than fix and move on, the author **generalised each into a named invariant, encoded it as a property test, and wrote down which bug taught which invariant.** It goes further: it explains why the layer split exists (parser invariants property-style in `commandProvider.property.test.ts`, system invariants here behind a fake provider *"so a future provider can't silently break the contract"*), and documents a subtle mock requirement at `:34-36` (the fake must set `id = "command"` or the cache never engages).

⭐ It also names the reviewer: **Greptile**, the README sponsor. The sponsorship is not just a logo — the AI reviewer found three real security bugs and the response was a permanent invariant suite.

⭐⭐⭐⭐ **AND HERE IS THE SHIP'S SENTENCE. The invariant suite is `src/**/*.test.ts`, so CI runs it on every pull request. The knowledge-graph checklist runs nowhere. The difference between them is not care — the same person built both, and the ungated one is immaculate. The difference is who the next reader is. The invariant suite's next reader is `vitest`, which fails loudly and blocks the merge. The graph's next reader is an agent in a future session, which will read whatever is there and never object.**

**A gate exists where a reader can refuse. Agents don't refuse.**

That is why v267's *"the discipline stops where the artifact stops being code"* is true, and this is the mechanism underneath it.

---

## 4. ⭐⭐⭐ The rebrand, and the incumbent that is never named

The timeline, by pickaxe (`log -S`, all refs):

| Date | Event |
|---|---|
| **2026-04-02** | `fathah/hermes-desktop` first commit |
| **2026-06-02** | **NousResearch ships its own official "Hermes Desktop"** — v0.15.2 public preview, MIT, mac/Windows/Linux, with streaming tool output, preview pane, file browser, voice and a settings UI |
| **2026-06-03** | `1a6317d` *"complete Hermes One branding"* — **by pmos69**, the next day |
| 2026-06-03→05 | branch `codex/hermes-one-branding` |
| **2026-06-17** | `20e0756` *"Update download link from hermesagents.cc to hermesone.org"* |
| **2026-07-02** | `37449bc` *"Provider Agnostic"* introduces `HERMESONE_API_KEY` — **their own inference gateway as a provider** |

The product is now **"Hermes One"**: `README.md` says *"Hermes One"* ×2 and *"Hermes Desktop"* ×0, while the repo slug stays `hermes-desktop`.

⚠️ **The causal link is INFERRED, not established.** No commit message, doc or issue in the repository states a reason for the rename. What is established is the one-day gap.

⭐ **What it verticalised into:** `inference.hermesone.org/v1` is listed **first** in `PROVIDERS.setup`, `PROVIDER_CARDS` and the Settings "LLM Providers" items (`lat.md/provider-setup.md:9`), plus a Hermes One account with device login, cloud agent sync, a token wallet, a `$HD` token on bankr.bot, and a console with *"Credits → API keys"*. **A community client for someone else's open-source agent became a commercial platform that is its own default provider.**

**Honest on the disclosure:** `README.md` carries a clear disclaimer — *"This repo is not affiliated to **Nous Research**. This is a community maintained project."* — links the upstream repo, and discloses that the installer runs the official script with `--skip-setup` (`:336`).

⚠️ **But the README never mentions that a first-party desktop app exists.** All three occurrences of *"official"* refer to the install **script**, never the official **app**. ⭐ **The disclaimer discloses what the project is NOT; it does not disclose what you could have instead** — and for a reader choosing between them, that is the single most decision-relevant fact. This is **v267's silence-is-the-finding at N=2 in a different domain** — but **materially milder, and I want that said plainly**: the disclaimer exists, the upstream is linked and credited, the install script is disclosed. v267's subject named a competitor's protocol namespace with zero mentions of the competitor anywhere. This one just doesn't advertise a rival. Calling the two the same would be unfair.

---

## 5. The wallet: alarming on the surface, sound in the code

An `ethers` dependency and a `$HD` token badge in an AI-agent desktop app is exactly the shape that should trigger suspicion, so I went looking for the money path.

**It isn't there.**

- Only **2 files** import `ethers`: `src/main/wallet-store.ts`, `src/main/wallet-balances.ts`
- `git grep` for `sendTransaction | signTransaction | populateTransaction | .transfer( | sendRawTransaction | signMessage | signTypedData` across **all of `src/`, `tests/` and `scripts/`** returns **ZERO hits.** **The wallet is read-only. There is no signing path.**
- Recovery phrases are encrypted with Electron `safeStorage` (OS keychain) and `wallet-store.ts:55-59` **throws** if encryption is unavailable — **fail-closed**, the opposite of the v231/v232/v265 broken-auth triad
- `publicWallet()` at `:33-37` destructures `encryptedRecoveryPhrase` out before returning, so the renderer never receives even the ciphertext
- Entropy from `crypto.randomBytes` (`:49-53`), not `Math.random`; `MAX_WALLETS_PER_PROFILE = 10`
- `wallet-store.ts:1` is `// @lat: [[wallet-token-balances#Wallet Store]]` — **the code ref is the file's first line**

⭐ And `account-store.ts:11` comments *"keychain via Electron safeStorage — same approach as wallet-store.ts"* ⇒ **the pattern was deliberately propagated** to the account-token store. A discipline that *did* travel — the direct counter-example to v264/v265/v267.

So the risk is not "the agent drains your wallet"; no code path exists. It is a mnemonic in a per-profile `wallets.json`, encrypted at rest by the OS keychain. That is a reasonable design.

---

## 6. Electron hardening — exemplary, and centrally enforced

All five window-creating sites set the safe values: `nodeIntegration: false`, `contextIsolation: true`, `sandbox: true`, `webSecurity: true`, `allowRunningInsecureContent: false` — at `app/start.ts:188-192`, `askpass.ts:148-152`, `remote-oauth.ts:370-374`, `sudoCreds.ts:121-125`, and centrally in **`src/main/security.ts:93-97`**.

⭐ `webviewTag` is `true` **only** for the main window (`app/start.ts:193`) and **`false`** in the credential-prompt windows (`askpass.ts:153`, `sudoCreds.ts:126`) — the windows that handle sudo and SSH secrets deliberately deny webviews.

⭐⭐ **And the contrast is the ship's thesis in miniature: the security settings have a single enforcement point (`security.ts`); the agent instructions are a duplicated blob.** `CLAUDE.md` and `AGENTS.md` are **byte-identical** (md5 `4c75ca92…`, both blob `c54415023b…`, both mode `100644` — **copies, not symlinks**, so v243's 9-byte-symlink fix is unapplied). The right pattern was used exactly where a compiler or reviewer would notice.

⚠️ **The copy-forward hazard here is latent, not realised:** only **2 commits in 1301** ever touched either file, and they have **never diverged**. They are safe because nobody edits them — which is not the same as being safe by construction. *(This vault has the same shape: v259 flagged `05 Skills/` holding copied, re-versioned skills.)*

---

## 7. ⭐⭐ A hash-based staleness detector detects EDITS, not OBSOLESCENCE

`lat.md/.cache/lat_init.json` is **committed** (`.gitignore`, 546 bytes, does not exclude `.cache`) and records SHA-256 hashes of the two files `lat init` generated:

```
CLAUDE.md                      5fd49383be7fd33d…
.claude/skills/lat-md/SKILL.md 39c77385d4243678…
```

I checked both. **Both match exactly at HEAD.** The staleness marker reports "in sync".

⚠️ And it is right about the only question it asks. But `CLAUDE.md:32` still instructs the agent to explain that *"semantic search requires a key provided via `LAT_LLM_KEY`…"* — and **`lat` v0.12.0, released 2026-07-15, shipped offline embeddings via a bundled local WASM model, removing the API-key requirement.** The file was generated 2026-06-17 and is byte-identical at HEAD, 2026-08-06 — **22 days after the requirement it describes ceased to exist.**

⭐⭐ **A hash answers "has this file changed?" It can never answer "is this file still true?"** And the file it guards is the *agent's* instruction file — so the obsolescence is invisible to humans and authoritative to the machine.

⚠️ **Severity: low, and I want that stated.** The instruction is conditional (*"If `lat search` fails because no API key is configured…"*) and with v0.12 it does not fail. Nobody is harmed. The **structure** is the finding, not the damage. *(The v0.12 year is inferred from release ordering plus the March-2026 launch coverage; I did not read the full release notes.)*

---

## 7b. The install path is the real risk surface — not the wallet

⭐⭐ **`src/main/installer.ts:942`:**

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash -s -- --skip-setup
```

- **From `main`** — a moving target, not a tag or a pinned commit
- **No verification.** `grep -i "sha256\|checksum\|gpg\|signature\|verifyHash"` over `src/main/installer.ts` returns **zero hits**
- Run via `spawn("bash", ["-c", …])` after `source "$shellProfile"` (`:939-941`), so it inherits the user's full shell environment
- The same command, minus `--skip-setup`, is shown to users at `src/renderer/src/constants.ts:1340`

⚠️ **And `installer.ts:967-975` overrides the exit code:** if the script exits non-zero but `existsSync(HERMES_PYTHON) && existsSync(HERMES_SCRIPT)`, it emits *"Install script exited with warnings, but Hermes is installed successfully"* and resolves. This is **v260's FALSE-SUCCESS class at N=3 — but materially the most defensible instance yet**: the reason is written down (`:971-973`, *"can exit non-zero due to benign issues (e.g. git stash pop failure on already-clean repo)"*) and the fallback is a real two-path existence check, not a bare `spawn()` returning `Ok`. It is a *reasoned* override, not a blind one. It still means a partially-failed install where those two paths exist reports success.

**Supply chain (the gap the fleet failed on, closed by hand).** Across all three workflows there are **34 `uses:` lines and ZERO are SHA-pinned** — every one is a floating tag (`@v4`, `@v2`). Both release workflows declare **top-level `permissions: contents: write`** (`release.yml:14-15`, `beta-release.yml:25-26`), so *every* job in them — including the jobs that check out and build repository code — carries write. `ci.yml` declares no `permissions:` block at all.

⭐ **The contrast with v267 is stark and worth stating plainly: v267 had 12/12 actions SHA-pinned, a written threat model, a read-only default token, and write confined to one job that never executes repository code. This has 0/34 and blanket write** — in a project that ships signed-or-unsigned desktop binaries to end users behind an auto-updater.

**Signing, honestly disclosed:** macOS **is** signed and notarized (`electron-builder.yml:41` `notarize: true`; `release.yml:114` `CSC_LINK`). Windows is not, and the RPM is not GPG-signed — **and the README says so itself**, in the Install section, with the SmartScreen workaround and the `--nogpgcheck` note. **#83** positive.

---

## 7c. ⭐⭐⭐ Analytics — the best-documented subsystem, and an honestly-disclosed opt-out default

`lat.md/analytics.md` is a model design document, and the finding is as much about the doc as the code.

⚠️ **Telemetry is opt-OUT — on by default** (`:17`: *"Analytics is opt-out: enabled by default when the endpoint is configured"*). That is the default I would flag on any subject. **It is disclosed in the doc, in the Settings Privacy pane, and in the privacy string of every locale.**

And the surrounding engineering is genuinely good:

- ⭐ *"Replaces the former PostHog integration; **no third-party analytics SDK is bundled**"* (`:3`) — a third party was **removed** in favour of a direct `fetch`, and `:33` records that the PostHog `script-src`/`connect-src` CSP allowances were removed with it. **CSP tightened on the way out.**
- ⭐⭐ Keys are injected from GitHub Actions secrets at build time, so *"analytics is **silently disabled in local and unofficial builds** where neither is configured"* (`:5`) ⇒ **build from source and you are not measured at all.**
- ⭐ `:27` enumerates the payload and the exclusions: `app_version`, `electron_version`, `node_version`, `platform`, screen views, feature-usage events, plus a random localStorage UUID — and *"**No chat content, prompts, model responses, file paths, or credentials are ever collected**."* Session recording and auto-pageview capture are explicitly off.
- ⭐⭐ `:5` explains **why** it is disabled on the dev server *with the mechanism*: the `localhost:5173` origin fails the service's CORS preflight, so *"every request would just fail preflight and spam the console."* That is the v267 `nextest`-comment quality of documentation.

⇒ This is the strongest argument **for** `lat.md` in the whole repository: `analytics.md` is exactly the "what and why" that makes a codebase legible, it cites five source symbols by wiki link, and **it discloses an opt-out default rather than burying it.**

---

## 7d. ⭐⭐ The 3D office's model→action bridge is a closed allowlist (gap 2, closed by hand)

`src/renderer/src/screens/Office/office3d/interactions/worldActions.ts` — 173 lines — lets chat drive an avatar through the 3D office ("go to the bank and check my balance"). The design is sound:

- `:45` `const ABILITIES: WorldAbility[] = [...]` — a **fixed array**. A closed allowlist, not an open eval.
- `:66` the injected prompt: *"When — and only when — the user asks you to physically do something in that world that matches an ability below, append ONE fenced code block with the language tag `world-action` at the very end of your reply, containing a JSON array of ability objects to perform in order."*
- ⭐⭐ `:9-11` states the **extensibility contract**: *"every ability is one `ABILITIES` entry (the prompt is derived from it) … unknown `do` values parse to nothing — an older desktop ignores abilities a newer [one sends]"* ⇒ **the prompt cannot advertise an ability that does not exist, because both are derived from one array** — which is exactly what the test *"Prompt advertises every ability"* pins.
- ⭐ `:119` *"design: malformed JSON or unknown abilities are dropped silently"* — **fail-closed on parse, deliberately, with the reason written down.**

Combined with §5 (no signing primitive anywhere in `src/`, `tests/` or `scripts/`), **the blast radius of a hostile or confused model output here is: open a modal, walk an avatar, read a balance.** That is a safe design and it deserves to be said as plainly as the criticisms.

⚠️ Minor: *"dropped silently"* means a user whose request fails gets no diagnostic — the v266 single-terminal-state cost, at low severity.

---

## 7e. ⭐⭐ The README undersells itself — v267's refinement at N=2

`README.md:156` claims:

> *"**i18n ready** — internationalization framework with **English locale** covering all screens, ready for community translations"*

`src/shared/i18n/locales/` contains **12 locales**: `ar`, `en`, `es`, `he`, `id`, `ja`, `pl`, `pt-BR`, `pt-PT`, `tr`, `zh-CN`, `zh-TW` — including **two RTL languages**, with a test named *"RTL and narrow preference layout"* (`AppearancePane.test.tsx:126`) and a HEAD commit that is a merge of `fix/settings-i18n-alignment`.

⭐ **The community translations the README says it is "ready for" have already arrived, and the README still says English-only.** This is **v267's refinement confirmed at N=2 across independent authors: claims verifiable from inside the repository drift toward UNDERSELLING** (v267's README advertised ~10 CDP domains while the code implemented 189 methods across 16). The inflated claims in both subjects live only where the repository cannot check them.

---

## 7f. ⭐⭐⭐ What it verticalised into — seven subdomains

`git grep -o "[a-z0-9.-]*hermesone\.org"` over all tracked files:

| Host | hits | role |
|---|---|---|
| `inference.hermesone.org` | 16 | their own OpenAI-compatible LLM gateway, listed **first** in the provider picker |
| `analytics.hermesone.org` | 12 | first-party telemetry endpoint (§7c) |
| `api.hermesone.org` | 6 | account/credits backend |
| `registry.hermesone.org` | 4 | an **MCP registry** |
| `hermesone.org` / `www.` / `.hermesone.org` | 13 | downloads, cookie domain |
| `console.hermesone.org` | 1 | *"Credits → API keys"* |

Plus a Hermes One account with device-login OAuth, cloud agent sync, a token wallet, and a `$HD` token on bankr.bot.

⇒ **A community client for someone else's open-source agent, which grew its own inference gateway, MCP registry, analytics service, credits console and token — and became its own default provider.** That is the subject's most distinctive property, and it is the reviewable mint alternative in §10.

---

## 8. Provenance — human and AI

**Human.** Fathah across 3 identities = **849 of 1301 commits (65.3%)**. **Pedro Simoes / pmos69 = 189 (14.5%)**. The remaining ~20% spreads across 80 addresses. *"Community maintained"* is substantially true: **452 commits (34.7%) are not the owner's.**

**AI — and this is the richest disclosure in the corpus after v243.** `log --all --format=%B | grep -c` over **all 1301 commits**: **94 `Co-Authored-By` trailers.**

| Co-author | count |
|---|---|
| `Claude Opus 4.7 (1M context)` | 51 |
| `Claude Fable 5` | 8 |
| `Claude Opus 4.7` | 5 |
| `Claude Opus 4.6 (1M context)` | 5 |
| `Claude Opus 4.8` | 4 |
| `Claude Opus 4.8 (1M context)` | 3 |
| `Claude Sonnet 4.6` | 1 |
| `Claude Opus 4.6` | 1 |
| **Claude, total** | **78** |
| `Copilot` (2 addresses) | 11 |
| `Cursor <cursoragent@cursor.com>` | 2 |
| ⭐ **`Hermes Agent <hermes@local.invalid>`** | **2** |
| `greptile-apps[bot]` | 1 |
| **total** | **94** ✅ (sums exactly) |

⭐⭐ **Eight distinct Claude model versions**, a version time-series across the repo's life. ⭐⭐⭐ **And the app's own agent co-authored its own source code twice** — `Co-authored-by: Hermes Agent`.

⭐ `grep -c 'generated with'` and `grep -c '🤖'` over all commit messages: **0 each** — so these are bare trailers, not the default Claude Code footer form. **Whether the trailers are curated or a tool default is NOT ESTABLISHED** (v243's answer there was "an uncurated default"; the mixed presence of Copilot, Cursor, Greptile and Hermes trailers here is not explained by any single default).

⭐ **`codex` appears 59 times in commit messages** and there are ~12 `codex/*` remote branches — so OpenAI Codex was used heavily and leaves **no** trailer. **Claude discloses via trailers; Codex discloses via branch names. Both are visible; only one is machine-countable.**

---

## 9. Tests, and the three that are switched off

- **187 test files** (108 in `tests/`, 79 colocated in `src/`), **1,637 `it(`** + 204 `test(` + 331 `describe(`
- CI runs `npm test` (`vitest run`) on **every PR and every push to `main`**, gating. **This is not v263** — the tests have a gate and it fires.
- ⚠️ **`vitest.config.ts:14` sets `passWithNoTests: true`.** v262 found the same flag as *"a gate that cannot fail"* — **here it is latent, not active:** 1,841 test functions currently match. I checked all 187 test files against the three `include` globs: **all 187 match, zero orphans.** The `include` list covers `tests/**/*.test.ts` but **not** `tests/**/*.test.tsx`; no `.tsx` exists in `tests/` today, so that is a dormant hazard, and I am not going to inflate it into a live one.
- 7 `skip`/`only` hits. Four are legitimate platform/dependency guards (`process.platform === "win32" ? it.skip : it`; `python3Path ? it : it.skip`). **Three are real `it.skip` in `tests/config-value-paths.test.ts:122, 156, 166`** — and ⭐ **all three are the negative assertions**: *"ignores grandchildren"*, *"does NOT match a nested occurrence when called with a flat key"*, *"does NOT pick the first nested occurrence across siblings"*. The recall tests run; the precision tests are off. **To their credit the reason is written down** (`:118-121`): *"getYamlPath (introduced by #243) is currently permissive on grandchildren and flat-key column-0 enforcement. The strictness these cases document is desired but not yet present; tracked as a follow-up."* That is a disclosed deficiency, not a hidden one — **#83** positive.

---

## 10. Mint decision — NO MINT

**Counts 46 / 12 UNCHANGED. §C-1 12 unchanged. §C-2 39 unchanged.**

**The form factor is a genre the corpus has ruled on three times:**

| ship | subject | decision |
|---|---|---|
| **v222** lobehub | flagship self-hosted provider-agnostic chat/agent platform | NO MINT — *world-canonical not world-first* |
| **v227** hermes-webui | **a community WEB front-end for the SAME upstream, Hermes Agent** | NO MINT — form-factor-within-a-genre; *"an adjacency, not an instance"* |
| **v236** dsh-TUI | a terminal UI mounted inside a general agent runtime | NO MINT — presentation-not-capability |
| **v241** dsh-desktop | **an Electron desktop client for a general agent runtime it also launches** | NO MINT |

v268 is the fourth pass at the same class and the second community front-end for **Hermes Agent specifically**. The consistent answer is NO MINT.

**Two rows were tested and both are declined on their own written definitions** — the third consecutive-plus ship where reading a row's definition prevented a false N:

- **CONFIRMED #22 "Tauri-Desktop Management-GUI for a *Coding* Agent"** (N=3: v73 + v117 + v153). hermes-desktop *is* a desktop management-GUI that **controls** rather than observes — and it is **Electron**, which triggers the row's own written clause: *"if a 4th is non-Tauri, generalize the name to 'Desktop Management-GUI'."* ⚠️ **But the row is scoped to a CODING agent, and Hermes Agent is a general-purpose personal agent** — the exact discrimination v227 made. **So it is not a clean 4th either.** ⭐ **RECORDED for the audit: hermes-desktop is the strongest candidate yet for generalising #22 from "Tauri" and from "Coding Agent" — a promotion is an audit act and I did not self-execute it.**
- **C42 "Agent-First Codebase-Documentation Generator/Maintainer"** (N=1, v195 openwiki). `lat.md` is close but **not an instance**: C42 requires an agent that **AUTHORS** docs autonomously via *"a git-diff-scoped, human-gated CI loop"*. `lat.md` authors nothing and has no CI loop — it **validates and retrieves** while the agent authors. ⭐ **Recorded as a DEFERRED watch axis: the *validate-and-retrieve* pole against C42's *generate* pole.**

**And the decisive discipline point: `lat.md` is a DEPENDENCY, not the subject.** Minting for it would be minting for a third-party tool the subject happens to use — the v181 cortex-hub discipline. Declined.

⭐ **The reviewable mint alternative, recorded and declined:** *"a community front-end for someone else's open-source agent that verticalises into its own commercial platform — own-brand inference gateway, accounts, cloud sync and a token — while remaining the upstream's client."* That is a **business-model** shape, not a capability, so it belongs near **LV-C2 "OSS-with-hosted-Pro-SaaS-tier-on-MIT-base"** (v78) — but with a genuine twist worth an audit's attention: **v78 was an author monetising their own OSS; this is a client author monetising someone else's by becoming its default provider.**

**Instance-strengthening recorded, not self-incremented:** **#83** SPLIT — strongly honest (the written `continue-on-error` reason, the three documented skips, the non-affiliation disclaimer, the `--skip-setup` disclosure, the unsigned-installer warnings in the README) and not honest (the unadvertised first-party alternative; a mandatory checklist with no gate) · **#19 19a** · **#12** · **#66** mixed.

**NON-CLAIMS.** NOT **#57** — no corpus subject is a dependency; Hermes Agent and Superpowers are corpus **entities**, which is **convergence, not recursion** (the v264 precedent, by name), and `vercel-labs` is an org coincidence · NOT **#52** (stars page-stated, §37.4) · NOT a new top-level pattern · **nothing was installed, built or executed; no third-party service was contacted beyond public web pages.**

---

## 11. Scoring

| Criterion | Verdict | Reason |
|---|---|---|
| **(a) Anthropic affiliation** | **FAIL** | Fathah KA, a disclosed individual. §41 — no name/locale inference; the disclosed-individual axis answers NO. |
| **(b) Goal relevance** | **STRONG** ⚠️ *MODERATE reviewable* | The **product** is a general-agent desktop client, adjacent to goal #1. The **engineering surface** is squarely on it: a generated `CLAUDE.md`, Claude Code skills and hooks, 78 Claude co-author trailers, and a load-bearing finding about agent-maintained knowledge — this vault's own practice. Stronger claim to STRONG than v236 had, where Claude appeared only as something deleted. |
| **(c) Technical depth** | **STRONG** | 1003 files, 1301 commits, 82 authors, gating CI, 187 test files, property-based security invariants. |
| **(d) Actionable** | **STRONG** | `lat.md` is directly evaluable for this vault at zero risk, and §2.4 hands over a two-command audit. |

⇒ **GOAL-ALIGNED INCLUDE 3/4.** Cleanly GA — no §40, no override.
**Streak: v267 `GA:124` → `GA:125 · OG:13 [7 ov]`** (**48 consecutive GA**, v220→v268). **§35 CLEAR** ({v266 GA, v267 GA, v268 GA} = 0 OG).

---

## 12. Method — my errors, and what the fleet did

🔴 **Error 1 (the big one).** My `lat check` re-implementation put the H1 in the section-id chain and reported **66 violations**. The true figure is **2**. Caught pre-publication by grepping the real headings before trusting my own tool. **Fifth consecutive ship where my error was concluding from where I chose to look — §43.1.**

🔴 **Error 2.** My first `AGENTS.md`-vs-`CLAUDE.md` divergence scan used an unquoted `rev-parse "$c:AGENTS.md"` that the shell mangled into a vault path; it printed nonsense that I initially read as "diverged". Redone with `ls-tree`: they never diverged.

⚠️ **Error 3 (hypothesis, refuted by my own check).** I predicted the `include` globs would orphan a committed test file. I checked all 187 and **all 187 match**. Reported as a dormant hazard, not a defect.

**Fleet: 19 agents, 17 completed, 2,433,348 subagent tokens, 688 tool uses, 626s.** ⚠️ **Five of eleven dimensions FAILED on the StructuredOutput retry cap** — `security-posture`, `office-3d-and-agent-actions`, `release-supply-chain`, `provenance-and-contributors`, `docs-integrity-beyond-lat` — the same failure mode as v267.

⚠️ **And here the honest accounting differs from v267 in the way that matters.** v267 recorded that all five of its failures landed on ground already hand-covered, and called that *"luck presenting as redundancy."* This time **three of five landed on covered ground** (security-posture, provenance, docs-integrity — §6, §8, §2.3) **and two did not**: release-supply-chain and office-3d were genuine holes. **I closed both by hand rather than declare them unknown** (§7b, §7d) — and the supply-chain gap turned out to hold one of the ship's harder numbers (0/34 SHA-pinned). **Four consecutive ships of "the failures happened to land on covered ground" has now broken. The fix is not better luck: two of the nine dimensions I most wanted were the two that died, and I only noticed because I diffed the failure list against my own coverage.**

**What the fleet did contribute:** the `installer.ts:942` `curl | bash` line and the `hermesone.org` subdomain fan-out — both of which I then re-derived myself before publishing (**D51**). A refuter correctly downgraded a `passWithNoTests` line-number claim (11 → the real 14) to **citation drift rather than fabrication** — the distinction I asked for explicitly, applied correctly.

**⚠️ NOT ESTABLISHED.** Whether the app builds, installs or runs · whether `lat check` actually passes when the real tool runs it (**my re-implementation is a reading of the four documented rules, not the tool** — the 0/0 result is a claim about those rules, not a claim about `lat`'s output) · why HEAD has been quiet for 17 days · whether the Claude co-author trailers are curated or a tool default · whether the rebrand was caused by the official app's release (one-day gap, no in-repo reason) · star/download counts (§37.4) · the 90+ remote branches · the full 404-line and 386-line release workflows beyond pinning, permissions and signing · Nous Research's stance on `hermesone.org`.

---

## 13. Pilot — ⭐ READ-AND-BORROW, and evaluate one dependency

**Do not install the app.** The install path runs a third-party shell installer with dependency resolution, wants passwordless sudo on WSL, ships an unsigned Windows installer and an unsigned RPM (both disclosed in the README), and wires 16 messaging gateways into an agent with tools. None of that is needed to get the value.

**Rung 0 — 20 minutes, read these in order.**
`CLAUDE.md:6-12` (the mandatory checklist) → `.github/workflows/ci.yml:33-44` (what is actually gated) → `.husky/pre-commit:1-4` (the hook that exits 0) → `lat.md/lat.md:1` (the install instruction, inside the artifact) → `Development.md` and `CONTRIBUTING.md` (which never mention it) → then **`src/main/secrets/securityInvariants.test.ts:4-24`**, which is the best twenty lines in the repository.

**⭐⭐⭐ Rung 1 — 30 minutes, and it is about this vault.**
v267 handed over *"derive the counts, wire it into the script nothing invokes."* v268 sharpens it: **integrity is the cheap half. Coverage is the half that rots silently.** The vault's `lat check` equivalent would verify every `[[link]]` in `_state/` and `_patterns/` and say **nothing** about a ship whose findings were never filed — which is exactly how the v259 audit came to find a count wrong twice. So:
1. derive 46/12, §C-1, §C-2 and the `GA:` streak from the `C##` markers and per-ship tags — **integrity**;
2. then add the **coverage** check: for every `vNNN` tag in the shim, assert an entry exists in `_state/03c`, and for every entry in `03c`, assert the shim references it. Both directions, per **D15**.
3. Wire both into `(C) proposed-verify-vault-inventory.sh` — **the nine-clause script v263 found nothing invokes.**

**⭐⭐ Rung 2 — 45 minutes, the highest-value transferable artifact.**
Port the **security-invariant suite pattern** into hireui: one file, each `it` encoding one invariant that must hold forever, a header comment mapping each past review finding to the invariant it taught, property-tested where the input space is wide. This composes directly with the standing **BOLA authorization audit** (recorded as hireui's #1 risk) — every BOLA finding becomes INV-n instead of a patch.

**⭐⭐ Rung 3 — 45 minutes, evaluate `lat.md` for the vault, seriously.**
It is the closest thing yet to a productised version of this vault's founding pattern, from a highly credible author, and its `lat check` is the validator the vault has wanted for five ships. Evaluate on a scratch repo, not the vault. The two questions that decide it: does it scale to `_state/03c`'s 2.3 MB single-line entries, and does `@lat:`-style bidirectional linking survive prose that isn't source code? ⚠️ Fence it: `npm i -g` on a package you have not read, so `install-snapshot` first and `npm-security-check` before that.

**⭐ Rung 4 — 20 minutes, the disposition question.**
Fix the vault's own instance of §6: `CLAUDE.md` here duplicates content the way this repo duplicates `AGENTS.md`. v243's answer is a 9-byte symlink. v259 left the `05 Skills/` copy-forward decision open. Close it.

🔴 **NEVER:** install the app to try it — the documented install path is **`curl … | bash` from a moving `main` branch with no checksum or signature** (`installer.ts:942`), run with your shell profile sourced · grant the passwordless sudo the README's WSL workaround asks for · trust its release binaries as if the CI were hardened — **0 of 34 Actions are SHA-pinned and both release workflows carry blanket `contents: write`** · point its 16 gateways or its cron scheduler at anything touching candidate data · forget that **telemetry is opt-out, on by default** in official builds (§7c) · read *"community maintained"* as *"the only option"* — a first-party MIT desktop app has existed since **2026-06-02** and the README does not mention it · cite the wallet as a fund-loss risk (**there is no signing path anywhere in the tree**) · assume `lat check` passes because my re-implementation says so.

---

**Suggested next action:** review + merge the chain — `main` is at **v226**; 45 commits / 41 ships (v227→v265) were outstanding before v266, plus v266, v267 and now v268. Then **Rung 1**, because three consecutive ships have now handed over the same lesson from three directions and v268 supplies the missing half: v263 found a script nothing invokes, v267 found that the one surface with no gate carries the claims, and **v268 found that even a perfectly clean graph tells you nothing about what was never written down.**

⚠️ **And the ~v268 audit is now DUE** — v259 named it, v260→v268 have all shipped. It gains from this ship: the **#22 generalisation** (non-Tauri **and** non-coding-agent), the **C42 validate-vs-generate** watch axis, the business-model mint alternative, and the fourth pass at the community-front-end genre.
