# (C) deepseek-harness-desktop — Deep Dive

**Wiki v241** · built 2026-08-18 · subject `anywhere-labs/deepseek-harness-desktop`
**Method:** ✅ SOURCE-CLONED with full history + a 16-agent workflow (0 errors, ~1.77M subagent tokens, 549 tool uses, 639s) + hand-verification of every load-bearing claim.

> **Read this first.** Two of this ship's most important findings are corrections — one to an agent, one to **my own framing**, and one to the **method v240 was celebrated for**. They are in §2 and §3. Everything downstream depends on them.

---

## 1. What it is

`anywhere-labs/deepseek-harness-desktop` — 「为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。**万物皆「插件」，桌面本身也是「插件」**。」
("A modern desktop solution for the DSH plugin ecosystem. Everything is a plugin — **the desktop itself is a plugin**.")

An **open-source Electron desktop client for DeepSeek Harness** (= corpus subject **v235**) for Windows and macOS. MIT. Homepage `dshdesktop.cn`. Page-stated ~**13.2k★ / 597 forks** (§37.4 — see §9 for why the star figure is unusable).

Three Yarn-4 workspaces around a **pinned upstream git submodule**:

| Workspace | Version | Code | What it is |
|---|---|---|---|
| `dsh-plugin-desktop` | **2.0.1** | 144 files, ~27,317 LOC | The Electron shell, composed as a Cordis plugin. Publishes its own plugin-services API. |
| `dsh-community-market` | 0.1.0-dev.0 | 64 files, ~18,748 LOC (37 src ~10,229 + 15 tests ~5,799) | A working plugin marketplace with 4 catalog adapters and ~10 install-safety gates. |
| `dsh-community-fabric` | 0.1.0-dev.0 | 1 script, 157 LOC + **20 markdown** | A **4-RFC draft standard** for cross-host plugin interoperability. Documentation-only by design. |

Upstream is pinned in `upstream.json`: commit `99f6f02fecdb7dff40c3fbc9470f5907c29f74ca`, `sourceVersion` **0.1.0-rc.7**, and a `.gitmodules` submodule at `deepseek-harness/`. The rc pin continues the corpus's monotonic ladder: **v235 rc.5 → v236/v237 rc.6 → v239 rc.7 → v241 rc.7**.

`CLAUDE.md` is a committed **symlink → `AGENTS.md`** (the geti v213 cross-harness-symlink axis; v240 had this too).

---

## 2. ⭐⭐⭐ THE FINDING: the clone's git metadata describes a different project

This is the ship's headline, and it is a **hard correction to v240's own celebrated method.**

v240's headline was: *"PROVENANCE MEASURED WITHOUT THE MOCKED API — a clone carries authoritative git metadata: 1,662 commits, 853 unique author emails, ~5 days old."* That method is sound **only when the repository's history belongs to the subject.** Here it does not.

### What the clone says about the repository

| Measure | Value |
|---|---|
| Total commits | **12,637** (page-stated 12,638; clone-verified 12,637) |
| Merge commits | **5,646** (44.7%) |
| Non-merge commits | **6,991** |
| First commit | **2026-06-10 22:57:44 +0800** → ~69 days |
| Unique author emails | **52** (46 unique names) |
| Top author | Tianyi Cui, **5,235 commits (41%)** |
| `@deepseek.com` authors | **10 distinct addresses, 2,219 commits** (1,477 non-merge = **21.1%**) |
| Merge subjects | **915** "from `deepseek-harness/`" · **69** "from `deepseek-ai/`" · **11** from "`anywhere-labs/`" |
| GPG-signed commits | **ZERO** (sample of 200: 187 `N`, 13 `E`, 0 good) |

Every one of those numbers is **true of the repository and false of the product.**

### The proof

- **One root commit** (`b67e81a`, 2026-06-10): *"Initialize repo with README, AGENTS.md, and CLAUDE.md symlink."* A single continuous history — no grafted second history.
- The next four commits: *"Link MVP requirement analysis and **microkernel architecture** docs"* → *"Set up monorepo infra: Yarn 4 workspaces"* → *"**Vendor Cordis framework packages as source**"* → *"Add abstract service interface packages."*
  **That is not a desktop wrapper being born. That is DeepSeek Harness itself being born.**
- **`packages/` — a directory that no longer exists in the tree — has 8,103 commits.**
- The deleted history includes upstream's *own* internal architecture decision records, dated June–July: `custom-schema-dsl`, `tool-schemas-in-prompt-assembly`, `turn-enclosure-invariant`, `package-hierarchy`, `result-time-applied-hunk-diffs`, `filesystem-directory-listing-seam`, `windows-fs-permissions`, `tui-interactive-extension-service`, `unified-session-query-service`.
- **The pivot commit:** `4e3eb91`, **2026-08-15 01:07:13 +0800**, `t4wefan@qq.com`, *"refactor(repo): isolate upstream and desktop workspace"* — **deleted 7,405 files** and in the same commit created `.gitmodules` and `dsh-plugin-desktop/`.
- GitHub shows **no "forked from" banner** — this is an independent repository carrying upstream's history.

### What the clone says about the *product*

| Measure | Value |
|---|---|
| Commits after the pivot | **343** (307 non-merge) |
| Age of the product | **2026-08-15 → 2026-08-18 = ~3.8 days** |
| `dsh-plugin-desktop/` | **142** non-merge commits |
| `dsh-community-market/` | **67** · `dsh-community-fabric/` | **4** · `patches/` | **13** |
| Authors after the pivot | t4wefan (**166** across 5 addresses), Qiuner/`wdst3635` (**118**), `3350903664` (18), kid (3), +2 |
| **`@deepseek.com` commits after the pivot** | **ZERO** |

### The two consequences

**(a) My own earlier framing was WRONG, and this exonerates the project.** I initially read "10 DeepSeek staff addresses, 21% of commits, against a 'not affiliated' disclaimer" as a genuine provenance tension. It is not. **Every single `@deepseek.com` commit predates the product.** They are upstream DSH development that this repository inherited. The README's 「并非 DeepSeek 官方产品」 / *"not affiliated with or endorsed by DeepSeek"* is **accurate for the product**, and the project claims the 12,637 commits nowhere — it advertises no commit count at all.

**(b) THE RULE.** A clone's git metadata is authoritative about the **repository**, never about the **project**. When a repository carries inherited history — fork, graft, or in-place re-purposing — provenance must be measured **from the divergence point**, not over the history. Commit counts, author counts and "age" over an inherited history describe the **parent**.

**The cheap, general detector:** *look for paths with heavy commit history that no longer exist in the tree.* Here one command exposed it — `packages/` with 8,103 commits and zero files. Pair it with `git rev-list --max-parents=0` (root count) and a scan of merge subjects for foreign org names.

> **v240:** "a consistency check between two views of one source cannot see what is **missing** from the source."
> **v241:** "a provenance measurement over an inherited history cannot see **where the subject began** — measure the divergence, not the history."
>
> Two consecutive ships, two complementary boundary failures — and v241 corrects the very method v240 was praised for.

**⚠️ Both agents assigned to this question failed.** The reader (R10) claimed *"3 unique author emails, ZERO @deepseek.com"* — incoherent on its own numbers (25+22+3 = 50 ≠ 12,637) — and excused it by asserting my figures came from the upstream repo, which is impossible: that submodule is **uninitialized and empty**. The adversarial verifier (R15) then **CONFIRMED my original wrong framing** with correct arithmetic and the wrong interpretation. Neither found the pivot commit. The correct answer came from my own hand-analysis of root commits and deleted paths. **An adversarial verifier checks the claim you gave it; it does not reframe the question.**

---

## 3. Doc-integrity: the mechanism is here, and so is the gap

Five consecutive ships have handed the vault machinery for its own `C22–C27` disease. v241 hands over the most, and also supplies the sharpest counter-example.

### 3.1 `scripts/verify-layout.mjs` (136 lines) — the strongest *structural* gate in the run

Verified clause-by-clause. It enforces:

- `packageManager` is exactly `yarn@4.18.0`; the workspace array is exactly the three members; no member declares its own `packageManager`.
- `CLAUDE.md` → `AGENTS.md`, **tolerating Windows checkouts that materialize a symlink as a regular file** (lines 44–53) — a genuinely thoughtful portability detail.
- **8 legacy pnpm paths must not exist.**
- The submodule path *and* URL match `upstream.json`; upstream retains its own `pnpm@` package manager.
- **No dependency may bypass the published-package boundary** — any `workspace:`/`portal:`/`link:` range, or a `file:` range containing `deepseek-harness`, fails the build (lines 76–91). *This is the "unmodified upstream" invariant mechanized.*
- The submodule is tracked at mode `160000`; **the index object equals `upstream.commit`**; the checked-out HEAD equals it; **`git status --porcelain` in the submodule must be empty**; origin URL matches; `upstreamPackage.version === upstream.sourceVersion`.
- **Every `@deepseek-ai/dsh*` dependency must equal `upstream.runtimePackageVersion`** — rc.7 uniformity enforced, and the deps are **exact-pinned**, not caret-ranged (v236 used `^0.1.0-rc.6`). This sidesteps entirely the prerelease-range trap v240 documented.
- Bilingual **blob-hash records** for the README pair and one agent note — hashing **`git rev-parse HEAD:<path>`, the committed blob, not the working tree**, with the reason in a comment: *"checkout line endings differ per host, while HEAD:<path> is identical everywhere."*

⭐ That last detail **solves v240's CRLF defect one ship later** — and `.gitattributes` (`* text=auto eol=lf`, `patches/*.patch text eol=lf`) closes it from the other side. v240 had one CRLF record in 1,390 and no `.gitattributes`.

**I ran their check by hand: both recorded README blob hashes MATCH.** The bilingual pair is genuinely consistent, and both READMEs carry 14 sections and 34 table rows.

### 3.2 The honest limits — three, and I corrected an agent on one

1. **Blob-hash equality ≠ semantic equivalence.** It proves "neither file changed since last recorded," not "both languages say the same thing." Edit both sides divergently, re-record both hashes, and the gate passes. This is the *same* class of limit v239's linter had.
2. **⚠️ Note coverage is 1-of-12.** There are **12 decision notes**, each with `.md` + `.zh.md` + `.i18n.yaml` — **36 files, perfect 12/12/12 pairing.** But `verify-layout.mjs:21` **hardcodes exactly one note name**. Eleven architecture notes' records are checked by nothing. ⭐ This is the v240 inventory rule inverted: **v240's loader globbed and silently skipped a non-matching file; v241's checker hardcodes a constant and silently ignores eleven files that would match.** Both are inventory failures. A three-line `find`-and-loop would close it.
3. **✅ CORRECTION to an agent.** R13 claimed the gate "runs only on Windows — a Linux push could bypass it entirely (33% of CI jobs)." **False.** The root `check` script *begins* with `yarn check:layout`, and the primary `check` job runs `yarn check` on **ubuntu-latest** (`ci.yml:41`), plus Windows (`:64`) and an explicit third invocation (`:108`). The real gap is **macOS**, which runs only `yarn workspace dsh-community-market check` + a packaging smoke.

### 3.3 ⭐⭐⭐ The composite finding: the inventory rule exists here as working code — in the one place the index cannot see

**`dsh-community-fabric/scripts/verify-docs.mjs` declares an explicit 33-file inventory AND walks the tree recursively to catch additions** — it enumerates **both ways**. That is *precisely* the rule the vault derived at v240: *"pair every equivalence check with an INVENTORY check that enumerates by a DIFFERENT rule than the parser uses."* It exists here, implemented, one ship later.

And then:

- Those 33 files include a **4-RFC suite** — `0001-plugin-manifest-capabilities-events`, `0002-runtime-presentation-invocation-transport`, `0003-service-providers-and-composition`, `0004-provenance-validation-and-diagnostics` — each in both languages.
- **`docs/README.en.md` — the top-level index, which calls itself the full documentation and README map — contains ZERO occurrences of "rfcs."** (Hand-verified: `grep -c "rfcs" docs/README.en.md` → **0**.) Fabric's *own* README lists all four at lines 46–49.
- ~25 files exist and are absent from that index (7 Chinese docs, the 4 RFCs ×2, `compatibility-layer` ×2, `dsh-plugin-needs` ×2, three Chinese research variants).

> **The workspace that solved the inventory problem is invisible from the front door — because the top-level index is hand-maintained and has no inventory check of its own.** The project holds the correct mechanism in one directory and fails the same class of check one directory up.

**Counter-balance, and it is real:** I tested **every relative markdown link** in `README.md`, `README.en.md`, `docs/README.en.md`, `docs/README.md` and `AGENTS.md` — **67 links, ZERO dead.** v240 had `README.ja.md` broken on line 5 of *both* READMEs. v241's links all resolve; its failure is omission, not breakage.

### 3.4 ⭐⭐ `AGENTS.md` is stale — and the machine contract advanced without it

`AGENTS.md` states: *"`dsh-community-market/` owns the community-market shell. Until its runtime is implemented, it remains a private documentation scaffold and **must not declare loadable DSH or package entry points**."*

`dsh-community-market/package.json` declares `main: lib/index.js`, an `exports` map with `./client` and `./contracts`, **and** `dsh.client.inject` of five upstream client packages — behind ~18,748 lines of code and a 15-file test suite. `README.en.md` badges the market **BUILT_IN** and says it is *"complete and built in."*

The verifier earned a real improvement here, and it makes the finding sharper rather than weaker:

- Rule added: `9c2d915154` (2026-08-16 23:14:25)
- Runtime + entry points added: `b5004d92b9` (2026-08-17 15:57:54)
- **In that same commit, `verify-docs.mjs` flipped polarity** — from *forbidding* `main`/`exports`/`dsh` (*"documentation scaffold must not declare …"*) to *requiring* them (*"runtime package must expose the reviewed Host entry"* / *"must declare its Web Client dependency graph"*).
- `AGENTS.md` last touched `168304fead` (2026-08-17 14:39:45) — **before** the runtime commit, and it did not update the market rule.

So the transition was **deliberate and is mechanically enforced** — as a *state machine*: scaffold-phase forbids entry points, runtime-phase requires them. That is prose-vs-code enforcement done better than v240's category check. **The one artifact left stale is `AGENTS.md` — the file the AI agents read.** Nothing ties it to the manifests.

`dsh-community-fabric` still complies exactly: no `main`, no `exports`, no `dsh` key, a docs-only `files` list.

> **The vault application is exact.** `CLAUDE.md` *is* an `AGENTS.md`: the agent-facing prose. And it is precisely what goes stale while the chapters advance — `_state/03c-projects-v61-v183.md` holds entries through **v240** under a `-v183` label. Content advanced; the agent-facing label didn't. Same failure, same file class, same cause: **nothing ties the prose to the inventory.**

---

## 4. Architecture: the shell as a plugin of the runtime it launches

The inversion is real and mechanically true, whatever its novelty (§7).

**Boot chain:** `bin.ts` (144 LOC, the `dsh-desktop` bin) → `launchElectron()` spawns Electron with `main.js` → `main.ts` (810 LOC) reaches `app.whenReady()`, resolves the login-shell environment, selects and composes a profile, then calls:

```ts
const ctx = await boot(BIN_NAME, prepared.rootConfig, prepared.patches, async (hostCtx) => {
  hostCtx.provide('desktopRuntime', runtime)          // inject the Electron adapter INTO the Host
  hostCtx.provide('desktopPnpmBootstrap', desktopPnpmBootstrap)
  await hostCtx.plugin(DesktopActionsService, {...})
  await hostCtx.plugin(DesktopPluginsService, {...})
  await hostCtx.plugin(DesktopProfileService, {...})
}, prepared.bareModuleBaseUrl)
```

The Electron launcher is neither the host nor embedded in one. It **starts the Cordis Host**, **provides the Electron adapter into it**, and **mounts its own services as ordinary Cordis plugins**. The Host then loads ordinary DSH plugins — one of which is `dsh-plugin-desktop` itself, inserted via `cordis.patch.yml`. `src/index.ts` exports `name = 'desktop-shell'` and a standard `apply(ctx, config)`; if `desktopRuntime` is absent it **silently returns without mounting**.

**Manifest:**
```json
"dsh": {
  "client": { "inject": ["@deepseek-ai/dsh-client-runtime", "@deepseek-ai/dsh-client-ui-theme"], "platform": "web" },
  "bundle": { "patch": "./cordis.patch.yml" }
}
```

**Compatibility mode** is the default and is deliberately additive — `cordis.patch.yml` comments: *"Desktop Host operations compose around the existing Web bundle. Compatibility mode keeps upstream ownership of the browser carrier and rendered UI."* Advanced mode is an all-or-nothing desktop-owned generation keyed on a single source of truth, `dsh-desktop.mode` in `settings.yaml`.

**Work profiles** are real on-disk directories under `$DSH_HOME/profiles/<name>/` with a `package.json` declaring `dsh.profile.bundles`, a `cordis.yml` rewritten before each boot, a shared `node_modules`, and `dsh.lock`. Selection is persisted in Electron user-data via a `0600` temp file and same-directory atomic rename, with `active` / `pending` / `lastKnownGood` — promotion to last-known-good only after the app boots **and** the window loads. That is careful engineering.

**It publishes an API for other plugins** (`docs/plugin-services.md`): `desktopProfiles` (`current`, `list()`, `select()`) and `desktopPnpm` (`run()`, `runPlugin()` returning a handle with `stdout`/`stderr`/`done`/`cancel()`). `runPlugin` deliberately routes through `dsh plugin --profile <active> add …` to **preserve DSH CLI authority** rather than shelling pnpm directly. Services are **generation-scoped** — stale after a profile switch. This is the v237 axis (a plugin that publishes its own extension API) at N=3.

---

## 5. The marketplace — and the answer to v240's open limit

`dsh-community-market` is a **working runtime**, not a scaffold: 4 JSON schemas → generated TypeScript types (with a `--check` drift gate), 4 adapters, a 1,211-line install service, React client UI, ~5,799 LOC of Vitest.

**Catalog sources, verified in code:**
- `src/adapters/dshfind.ts` → `https://api.dshfind.com/v1/plugins`
- `src/adapters/dsh-1024store.ts` → `https://deepseek1024.com/api/v1/plugins`
- `standard-http` for any user-added HTTPS source following the published schemas · `manual-install`

⭐ **v240 documented the publisher side of this pattern; v241 is the consumer side.** v240's `docs/plugins.json` was a *"Public registry API"* read by a separate org's storefront and by an in-agent `find_dsh_plugin` tool. v241 is a third-party client consuming two *different* registries — **neither of which is v240's.**

**Install-safety gates — ~10, all structural:**
- **Lifecycle scripts REJECTED:** if the candidate's `package.json` has `preinstall`/`install`/`postinstall`/`prepare`, install is **blocked** (`src/install/service.ts:26`, checked `:314-318`).
- SHA-512 `dist.integrity` verified; tarball URL must be the official npm registry.
- **Repository backlink:** the catalog item's `repository.url` must match the npm manifest's `repository.url` + `directory` (`:335-360`).
- **Exact stable version only** — no ranges, no tags, no prereleases (`stableExactVersion()`); the install command hardcodes `add --save-exact --registry=https://registry.npmjs.org`.
- Deprecated packages rejected; runtime compatibility asserted (Cordis 4.0.1 / DSH 0.1.0-rc.7 / Node 24.18.1).
- Approval gate showing exact `packageName@version` and the target profile.
- **Self-protection:** installing `dsh-plugin-desktop` or `dsh-community-market` is blocked.

**And the disclosed limit, in their own words:** *"These checks establish package identity and a narrow compatibility boundary; they **do not review the plugin or its dependency tree for malicious or unsafe behavior**."*

> **v240's unclosed gap was: "if a description claims '46 tools', someone counts them" — with no mechanism, and nothing listed is scanned.** v241 gates the *install* structurally and states with equal clarity that structural gating is not code review. **Publisher and consumer, one ship apart, both honest about the same hole — and the hole remains open across the whole ecosystem: nothing anywhere scans plugin code.**

⭐ Notably scrupulous neutrality for a storefront: *"dshfind is another optional cooperating catalog source … not selected by default, preferred, recommended, or used as a fallback"* — and the same disclaimer for 1024Store, explicitly *"not … an endorsement."*

---

## 6. `dsh-community-fabric` — a 4-RFC draft standard written in five hours

**Proposes:** a static `dsh-plugin.json` manifest (identity, `apiVersion`, entrypoints, `capabilities.required/optional`, `subscriptions`, `contributes`); a machine-readable **Host Descriptor** (supported `apiVersions`, capabilities, `execution.environment`, `trustMode`, platforms); a **capability negotiation** model in four stages — **support → request → grant → enforcement**; lifecycle contracts (`discover → validate → negotiate → authorize → activating → active → deactivating → disposed`); and one immutable event `messages.observe` with a versioned envelope carrying **`privacyClass`** and **`redactions`**.

**Its own disclosures are unusually clean:**
- *"Draft and documentation only … There is no Fabric runtime, SDK, schema release, compatibility badge, or loadable plugin in this workspace yet."*
- ⚠️ **enforcement is NOT implemented** — v0.1 is `trusted-in-process`; enforcement is promised for a future isolated mode. A declarative capability model with no teeth, said out loud.
- *"This is a community discussion draft, not an official DeepSeek or DSH standard."*
- *"It must not create a second plugin-loading ecosystem beside DSH and Cordis."*
- A versioned **DSH Adapter** marks a capability `unsupported` rather than approximating it through private APIs.

⚠️ **Written in ~5 hours on 2026-08-17** (created 00:11:56, last substantial update 03:14:13), **4 commits, 100% `t4wefan`**. Adoption by anyone else: **none**. It cites `omdsh-dev/community` issue #23 as incorporated feedback — ⭐ **`omdsh-dev` is v237's author org**, making this a **governance** link to a prior corpus subject rather than a dependency link.

---

## 7. Novelty: REFUTED — and the project never claimed it

The tempting mint is *"the desktop shell composed as a plugin of the runtime it hosts — the container is a plugin of the contained."* My two agents split, so I adjudicated.

**Decisive prior art: Eclipse RCP / OSGi.** The official Eclipse plug-in-architecture article states that a prominent example of a self-extending plug-in is the workbench UI itself, which contributes editors to its own extension points. Eclipse 1.0 shipped 2001-11-29; Eclipse 3.0 (2004-06-21) made the whole platform OSGi bundles. Twenty-plus years, thousands of plugins. The design space is further populated by JupyterLab (lumino, where the shell is provided by a plugin) and Theia (DI-composed core).

⭐ **The tiebreaker is the fairest possible one: the subject does not claim novelty.** `dsh-community-fabric/docs/research/` contains `mature-plugin-frameworks.md` **and `vscode-extension-model.md`** — they studied Eclipse, Chrome and VS Code and drew on them. The README's 「桌面本身也是「插件」」 is a **design-commitment statement, not a priority claim.** Minting here would be over-claiming *on the subject's behalf*.

I rejected R12's "NOVEL" verdict: its table asserted "Eclipse RCP ❌ NO — no inversion" against R16's verbatim primary-source quote, and cited nothing.

The secondary claim — "pinned-upstream submodule + published-package-only boundary, CI-enforced" — is excellent engineering but standard practice, not novel.

---

## 8. Security & supply chain

### ⭐ The strongest positive in the run

`.yarnrc.yml`:
```yaml
enableScripts: false
nmHoistingLimits: workspaces
nodeLinker: node-modules
```

**Install-time lifecycle scripts are globally DISABLED**, then `dependenciesMeta` **allow-lists exactly five** packages to build (`@deepseek-ai/dsh-subprocess-local`, `electron`, `esbuild`, `koffi`, `node-pty`) and **explicitly denies three** (`@google/genai`, `electron-winstaller`, `protobufjs`). **Deny-by-default plus a curated allowlist** — an independent instance of the discipline the corpus recorded as **pi v228**'s strongest supply-chain positive exemplar, in a different package manager by a different author.

⚠️ **Correction to R9,** which claimed "no `dependenciesMeta` entries with `built:true`." There are five — and the true reading is *stronger* than the agent's: not "no build scripts run," but "build scripts are off by default and five are deliberately enabled."

- **`yarn.lock`: 1,001 resolutions, ZERO from `npmmirror`/`taobao`/`cnpm`.** ⭐ A direct contrast with **v240**, which resolved 2 of 3 packages from `registry.npmmirror.com`. 7 `patch:` resolutions.
- **No `postinstall`/`preinstall`/`prepare` anywhere**; only `prepack: yarn run check` (publish-time) in all three workspaces.
- **Electron hardening is good:** `contextIsolation: true`, `nodeIntegration: false`, **`sandbox: true`**, `webSecurity: true`; a minimal preload exposing only `getPathForFile()`; a strict CSP (`default-src 'none'; … frame-ancestors 'none'`) on the recovery window; **no remote `loadURL`**.
- Crash reporting is **local-only** (`uploadToServer: false`). `koffi` is used only for kernel32 `GetDriveTypeW`/`GetVolumeInformationW`. Windows workspace paths are validated for NTFS/ReFS on fixed drives (removable/network rejected).
- macOS release enforces a `Developer ID Application` certificate, notarization, and **withholds signing credentials from the build subprocess** — only the release subprocess sees them.
- `dsh-plugin-desktop` runs **seven `verify:*` gates** (`closure`, `cli`, `loader`, `profile`, `licenses`, `notices`) plus `afterPack: verify-packaged-runtime.ts`, and `check:win-package` runs 11 named spec files. `verify:notices` validates `THIRD_PARTY_NOTICES.md`. CI is clean: `permissions: contents: read`, `on: pull_request`/`push`, **no `pull_request_target`**, concurrency cancel-in-progress.

### 🔴 The risks

1. **Update infrastructure is a third-party domain.** `update-checker.ts:90` polls `https://www.dshdesktop.cn/api/desktop/version`; `update-download.ts:33-34` hardcodes `https://www.dshdesktop.cn/api/downloads/{mac,windows}`. There is **no `electron-updater`** and **no GitHub Releases fallback**. Mitigations are real but thin: a 4 KiB response cap, strict SemVer parsing, and post-download DMG-magic/PE-header validation with a 1 GiB cap — **format validation, not signature or digest verification against a trusted manifest.**
2. **Windows builds are not code-signed.** macOS is `hardenedRuntime` + notarized; the `win` config has **no certificate configuration at all**, while `nsis` sets `allowElevation: true`. A signing asymmetry on the platform that is the *only* one shipping an installer target.
3. **`electronFuses: { runAsNode: true }`.** A documented hardening gap — the packaged binary can be driven as a plain Node process. ⚠️ Fair caveat: this app *must* run Node (it launches the harness and a bundled pnpm), and `windows-pwsh-sandbox.ts` sets `ELECTRON_RUN_AS_NODE` deliberately. A considered trade-off, not carelessness — but it weakens the notarized-and-hardened story.
4. **Telemetry is opt-out, default-ON.** `profile.ts:576` disables the upstream `session-telemetry-otel` plugin **only** when `DSH_TELEMETRY_DISABLED` is non-empty. The v221 llm-space finding class.
5. Minor: `README.md` embeds star-history `sealed_token` URLs (read-only chart tokens, not credentials); `win.artifactName` says `…-Portable.${ext}` for an NSIS target that `nsis.artifactName` overrides to `…-Setup.${ext}` — dead/misleading config.

### The patches — a disclosure gap, not deception

Four of five patches modify **upstream's published `@deepseek-ai/*` npm packages** at install time; the fifth patches `app-builder-lib`.

| Patch | What | Verdict |
|---|---|---|
| `dsh-llm-deepseek` (4 lines) | `if (call.id !== void 0)` → `if (call.id)` — preserves the first non-empty streamed tool-call `id`/`name` when continuation deltas arrive empty. Ships with a 100-line spec. | **Real bug fix** in the LLM streaming path; without it the agent loses tool identity mid-stream. |
| `dsh-sandbox-windows-acl` (4 lines) | `dwFlags: 256 → 257` + `wShowWindow: 0`. | **Presentation fix, NOT a weakening.** ACL confinement unchanged. Documented in an agent note explaining that upstream omits `CREATE_NO_WINDOW` because restricted children fail DLL init with it — so a GUI host gets a visible console per shell execution unless hidden this way. |
| `dsh-client-ui-directory-picker-browse` (20.9 KB) | Adds a native Windows folder picker via injected `window.__DSH_DESKTOP_PICK_DIRECTORY__` / `__VALIDATE_DIRECTORY__`. | Feature enablement; the validate callback lets the shell gate selections. |
| `dsh-client-ui-workspace` (508 B) | Adds `data-dsh-workspace-drop-target=""`. | Inert drag-drop marker. |
| `app-builder-lib` (1.6 KB) | Passes the **keychain** password (not the cert password) to `security set-key-partition-list`. | An electron-builder bug fix that **strengthens** signing. |

**The tension:** `README.en.md` says *"DSH Desktop does not fork or modify upstream source"* and *"Official DeepSeek Harness runs unchanged at a pinned version."* Narrowly true — the submodule genuinely is unmodified, and CI proves it. But an installed product's `node_modules/` contains **four patched upstream packages**. The patches are documented in `.agents/notes/` (internal) and **nowhere in `README`, `AGENTS.md`, `docs/plugin-development`, or `docs/user-guide`.**

**Fair verdict: a real disclosure gap, not dishonesty.** All five patches are benign or beneficial; none is hidden from the repository; the strongest one is explained at length in an agent note. ⭐ And the shape is the **inverse of v240's** — there, documentation was *more precise* than marketing; here, the **internal agent notes are more complete than the user-facing docs.** The fix is one sentence in the README plus a link to the notes.

---

## 9. Ecosystem: fragmenting, and the directories are demonstrably unreliable

The README's "Related Links" table was verified entry by entry. It names **four prior corpus subjects**: **v235** (upstream), **v236** dsh-TUI, **v237** DSH-better-sidebar, **v239** dsh-web-ui — tying v239's record for the widest `#57` fan-in. Plus Cordis (v235's kernel) and its own sibling `anywhere-labs/Agents-Anywhere` (the "Mobile Remote Control COMING SOON" feature; page-stated 641★, supports **Codex + Claude Code**).

**⚠️ The subject is absent from v240.** v240's catalogue does not list `anywhere-labs/deepseek-harness-desktop`; it lists **`ningbainb/deepseek-harness-desktop#packages/dsh-desktop-base`**. `0xsline/awesome-deepseek-harness` lists **four forks** (`chyra-moon`, `baiyuscc13724-max`, `fendouai`, `chokwinlee`) and **not** anywhere-labs. So the ecosystem's leading desktop client is missing from two of four catalogues, which instead list forks and namesakes of it — a second, independent confirmation of v240's own dropped-submission finding.

**Registry count and divergence:** `dshfind` · `DSH 1024Store` (`deepseek1024.com`) · **v240's** `awesome-dsh-plugin` (~1,390) · `0xsline/awesome-deepseek-harness` — over a raw GitHub `dsh-plugin` topic of **~7,309** repos (page-stated). Search surfaced three more directory front-ends (`dsharness.org`, `deepseek-harness-plugin.com`, `dshfind.com`).

**⚠️ A third consecutive claim caught propagating wrong.** The README's table says 1024Store has **"4,120 plugins"**; the target repo itself states **"3,100+"**. Joining **v239** (republished a retracted 98/99 benchmark) and **v240** (republished an unsubstantiated "live token stats" feature). Three ships, three inflated downstream claims — banal each time, and a consistent ecosystem hygiene failure.

**Star figures are unusable (§37.4).** The repo page states **13.2k**; `dshfind` states **11,974**; another directory summary said **494**. I cite none as verified. ⭐ Second instance of the **v236** finding that third-party DSH directories publish figures inconsistent with the repo.

**Also verified:** `dsh-market.com` does **not resolve** (ENOTFOUND) though `gallery.dsh-market.com` is live; `@anthropic-ai/sdk@0.91.1` sits in `yarn.lock` as a **transitive** dependency (not direct in any workspace) — consistent with v235's finding that upstream ships Claude Code as a delegatable subagent via Anthropic's official Agent SDK.

---

## 10. Corpus-recursive relations (`#57`)

- **A NEW relation shape — history-inheriting re-purposing.** The subject's repository *is* a prior subject's repository, re-pointed: 8,103 commits touching upstream's now-deleted `packages/`, 915 upstream PR merges, then one commit that deleted 7,405 files and added upstream back as a submodule. Prior shapes: dependency fan-in (v239), port (v207→v208), credited priority (v231→v232), host↔plugin (v235↔v236), mutual indexing (v240). **This is the deepest structural relation the corpus holds.**
- **Four-way outbound fan-in** — v235 / v236 / v237 / v239, tying v239's record.
- **A governance link** — Fabric incorporates feedback from `omdsh-dev/community#23`; `omdsh-dev` is **v237**'s author org. Not a dependency: a standards-process link.
- **v237's publish-your-own-API axis at N=3** — `dsh-plugin-desktop` publishes `desktopProfiles`/`desktopPnpm` for other plugins.
- **v235's plugin thesis at its limit** — v236 swapped the UI seam, v237 proved re-entrancy, v241 makes **the entire application container** a plugin of the runtime it launches.
- **pi v228's supply-chain hardening axis** — an independent instance (`enableScripts: false` + a 5-package allowlist).

---

## 11. Non-claims (stated to prevent later drift)

NOT world-first on shell-as-plugin (**Eclipse RCP** decisive) · NOT a new top-level pattern (max #85) · NOT first-party DeepSeek (**zero** `@deepseek.com` commits post-pivot) · NOT Pattern #52 (star figures page-stated *and* mutually contradictory) · NOT an N=k of the Multi-Vendor Orchestration-Platform row · NOT `#18` B1-MCP (ships no MCP server) · NOT a fork *banner* on GitHub (independent repo carrying inherited history) · NOT a v236 N=2 of DeepSeek-TUI v72 · NOT verified as DeepSeek-endorsed or DeepSeek-opposed (no public statement found either way) · the domain registrant name an agent reported is **UNVERIFIED and not repeated** · "12,637 commits / 69 days / 52 authors" are **repository** facts, **not** product facts.

---

## 12. Errors caught this ship — six, and three were mine

1. ⚠️ **Mine, and the biggest:** I framed the `@deepseek.com` commits as an affiliation tension. The pivot commit proved every one predates the product. **Reversed by my own analysis.**
2. **An agent's, incoherent:** R10's "3 authors, ZERO @deepseek.com" (25+22+3 ≠ 12,637), excused by an impossible claim about an empty submodule. **Rejected.**
3. **An adversarial verifier's:** R15 **confirmed my wrong framing** with right arithmetic. **Rejected** — a verifier checks the claim it is handed; it does not reframe the question.
4. **An agent's, falsifiable in one command:** R13's "the gate runs Windows-only, a Linux push bypasses it." The root `check` script begins with `check:layout` and runs on ubuntu (`ci.yml:41`). **Corrected to: macOS is the gap.**
5. **An agent's, where the truth was stronger:** R9's "no `built:true` entries." There are five, behind `enableScripts: false` — a curated allowlist, which is a *better* finding. **Corrected upward.**
6. **Mine, adjudicated:** two agents split on novelty; I ruled for the one with a primary-source quote, and found the fairest ground — **the project never claimed novelty.**

Also: two page-fetched figures discarded per §37.4; the "4,120 plugins" table claim falsified against its own target.

---

## 13. Bottom line

A three-day-old desktop product sitting on a sixty-nine-day-old repository that used to be DeepSeek Harness itself. The engineering in the parts that exist is genuinely careful — deny-by-default install scripts, a lockfile with no mirrors, real Electron hardening, atomic profile promotion with last-known-good, seven verify gates, a marketplace that refuses any package carrying a lifecycle script, and a CI-enforced boundary that makes "we do not modify upstream" a property of the build rather than a promise in a README.

And the failures are all in the same family, one directory up from where the mechanism lives: an `AGENTS.md` that still calls a shipped 18,000-line marketplace a documentation scaffold; a docs index that omits the project's own four RFCs; a bilingual checker wired to one note out of twelve; and four patched upstream packages disclosed to agents but not to users.

The thing worth taking is not the product. It is the **method correction** in §2 and the **two mechanisms** in §3 — because the vault is running the exact failure it found here, and has been for fifty wikis, under a filename that says `-v183`.
