# (C) DSH-better-sidebar — Deep Dive

**Subject:** `omdsh-dev/DSH-better-sidebar` (npm `dsh-better-sidebar`)
**Wiki:** v237 · **Date:** 2026-08-18 · **Author of wiki:** Claude (per CLAUDE.md `(C)` prefix rule)
**Verification:** INLINE + fully hand-verified. No workflow, no subagent (the ~970 KB shim overflows subagent context — the v200→v236 self-throttle). Source hand-fetched; collision by sanity-anchored hand-grep; landscape + identity by WebSearch.

---

## 1. What it is, in one sentence

A **VS Code-style right sidebar + bottom panel mounted as a plugin inside DeepSeek Harness** — file explorer, CodeMirror editor, real terminal, Git panel, embedded browser, and a sub-agent topology view, all isolated per conversation session — **which also re-exposes its own public extension API (`ctx.betterSidebar`) so that *further* third-party plugins can register new sidebar tabs and file viewers into it.**

The repo's own Chinese description leads with exactly that second half:

> 开放的侧边栏底座，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/Git/子代理页面
> *("An open sidebar base supporting third-party extensions registering new sidebar pages. Built-in file rendering/editing, terminal, Git, sub-agent pages.")*

The English README calls it *"a service-oriented sidebar framework… a complete workbench out of the box."*

---

## 2. Where it sits in the corpus

**This is the third consecutive ship inside the same dependency graph.**

| Ship | Subject | Role |
|---|---|---|
| **v235** | `deepseek-ai/deepseek-harness` (`dsh`) | The **host runtime** — *"Everything is a Plugin"* on the Cordis kernel |
| **v236** | `ccch1mneyyy/dsh-TUI` | A plugin that **replaces the terminal front door** with a Claude-Code-style TUI |
| **v237** | `omdsh-dev/DSH-better-sidebar` | A plugin that **adds a right panel** — and becomes an extension host itself |

v236 and v237 are **sibling plugins in the same host**, by unrelated authors, with **no dependency on each other**. That is a lateral corpus relation the corpus has not held before (prior recursions were vertical: port, fork, bundled dependency, citation).

**The machine-checkable link:** `package.json` declares **17 `peerDependencies`**, the `@deepseek-ai/*` ones pinned at **`^0.1.0-rc.6`** — the *same release-candidate pin* v236 carried, and one prerelease ahead of the `0.1.0-rc.5` recorded at v235. This is a lockfile edge, not a README citation.

---

## 3. Provenance — who actually wrote this

**Author: `omdsh-dev`, display name "Oh My DSH."** Self-described (page-stated, verbatim):

> DeepSeek Harness 的非官方社区插件生态｜Unofficial community plugins, tools, and experiments for DeepSeek Harness.

- **106 repositories**, 5 members, 280 followers, its own hub at `hub.omdsh.dev`
- **NOT DeepSeek.** NOT Anthropic. An explicitly unofficial community org (§41 → (a) FAIL; #19 19a first `omdsh-dev` author)
- Sibling repos include `dsh-at-file` (352★), `dsh-genui` (200★), `dsh_workflow` (78★), `dsh-lark`, `dsh-security-audit`, `dsh-session-health`, `dsh-hub` (a discovery platform), and a `community` governance repo

This matters for the corpus far beyond one plugin: **an unaffiliated community has stood up a 106-repo plugin org, a discovery hub, and written governance around a rival lab's agent runtime.** That is ecosystem formation, observed live.

---

## 4. Facts, with provenance labels

| Fact | Value | Source class |
|---|---|---|
| License | **MIT** | repo page |
| Version | **v0.13.0** | repo page + `package.json` + `dsh.plugin.json` (three-way agreement) |
| Language | TypeScript | repo page |
| Stars / forks | ~2,038★ / 129 forks | **page-stated §37.4 → NOT a #52 claim** |
| Commits | 216 (main) | page-stated |
| Open issues | 43 shown / 97 (API) | page-stated / API-mocked |
| Releases | 10 shown: **v0.4.1 (11 Aug) → v0.13.0 (17 Aug)** | **page-stated with explicit dates** |
| Node | ≥20 (pnpm ≥10) | `package.json` / README_EN |
| Deps / peers / dev | 21 / **17** / 25 | `package.json` |
| `contributes` | **`{ tools: [], skills: [] }` — both empty** | `dsh.plugin.json` |

⚠️ **The GitHub API is mocked in this environment (§37.4).** API-returned `created_at` (2026-08-07) and star counts are **not** relied on. The **release dates are page-stated and carry explicit timestamps** — those are the trustworthy velocity signal: **ten releases across seven days (11 → 17 Aug)**, with v0.4.1 already the tenth-shown (earlier v0.1–v0.4.0 releases exist off the first page). Recorded as an **LV-C4 cadence data-point, not #52.**

---

## 5. The architecture — what is actually novel here

### 5.1 It is a plugin that became a platform

`ctx.betterSidebar` is published as a **Cordis context service from the client half** (v0.4.0+). Source-verified interface:

```ts
interface BetterSidebarService {
  registerTab(descriptor: TabDescriptor): () => void
  registerFileViewer(descriptor: FileViewerDescriptor): () => void
  getTabs(): readonly TabDescriptor[]
  getFileViewers(): readonly FileViewerDescriptor[]
  matchFileViewer(path: string, head?: Uint8Array): FileViewerDescriptor | undefined
  openTab(seed, scope?); closeTab(tabId, scope?); activateTab(tabId, scope?)
  openFile(scope, path, title?); updateTab(tabId, patch)
  subscribe(listener): () => void
  subscribeState(listener): () => void
  readonly version: string
  readonly features: readonly string[]
  getSnapshot(): SidebarSnapshot
}
```

A consuming plugin registers in five lines:

```ts
export const inject = ['betterSidebar']

export function apply(ctx: Context): void {
  ctx.effect(() =>
    ctx.betterSidebar.registerTab({
      id: 'my-plugin:db',
      title: 'Database',
      order: 50,
      component: ({ scope }) => <DbView sessionId={scope.sessionId} />,
    })
  )
}
```

### 5.2 The design decisions worth stealing

These are the reason this subject is worth reading even though you should not install it:

1. **Dogfooded API — no privileged internal path.** The docs state it outright: the built-in tabs and viewers *"use the same API as third-party plugins"* (吃自己的狗粮 — "eating our own dog food"). Built-in IDs are simply **non-overridable**; duplicate registration throws `tab type "X" already registered`.
2. **Graceful absence.** The host is declared an **optional peer dependency**; when better-sidebar isn't installed, `ctx.betterSidebar` is `undefined` and registration code silently skips. A consumer plugin does not break by depending on it.
3. **Capability gates, not version sniffing alone.** `features: readonly string[]` advertises `'badge' | 'tabLifecycle' | 'updateTab' | 'openFile' | 'targetedOpen' | 'stateSubscription' | 'tabMeta' | 'pluginSettings' | 'urlTarget' | 'settingSelect'`. Consumers ask *"can you do X?"* rather than *"are you new enough?"*.
4. **Disposal is mandatory.** Every registration must be wrapped in `ctx.effect()` so the Cordis fiber calls the disposer on HMR or plugin unload — preventing double-registration on reactivation.
5. **Type-only across bundle boundaries.** `import type {} from 'dsh-better-sidebar'` merges the `Context` augmentation and is **erased at build**; a **build purity gate blocks value-imports** from `@dsh-external/*` or unlisted `@deepseek-ai/*`. All runtime interaction flows through service method calls. Cross-plugin `require()` is blocked by the loader.
6. **Orphan degradation.** A persisted tab whose plugin is gone renders as a labelled placeholder ("plugin not loaded" + close button) and **auto-restores** when the plugin returns — instead of corrupting layout state.
7. **Declarative settings as part of the contract.** A registered tab/viewer can declare `toggles` (host prefs fields), `pluginToggles` (plugin-local, persisted under `pluginSettings[id]`), or a custom `render` panel — so extensions get first-class settings UI without touching host code.

### 5.3 Built-ins (source-verified from `AGENTS.md`)

| id | order | single | note |
|---|---|---|---|
| `editor` | 10 | no | file window; path dedup |
| `git` | 20 | yes | Git panel |
| `subagent` | 30 | yes | **child-agent topology** |
| `terminal` | 40 | no | auto-incrementing ids |
| `browser` | 50 | no | sandboxed iframe |
| `diff` | −1 | no | hidden |

Viewers: `image`, `pdf`, `markdown`, `html`, `code` (catch-all, priority −100), `binary-download` (−50). Office previews were **moved out to a recommended plugin** — the extension point being used to shed weight from core.

⚠️ **Doc-drift caught by hand:** both READMEs say *"7 built-in tabs + 6 viewers,"* but `AGENTS.md`'s builtin table lists **six** rows and its reference section says *"6 tabs + 6 viewers."* The external-plugin guide's non-overridable ID list has **seven** (`explorer, git, subagent, terminal, browser, editor, diff`). Reconciliation: **`explorer` was folded into the `editor` "file window" at v0.13.0** (whose release note is *"file window and resource manager integration"*), so the READMEs' "7" is stale by one release. Minor, but it is exactly the kind of count the corpus should not repeat unchecked.

### 5.4 Engineering discipline

- **Lazy loading:** ~325 KB core at startup; xterm, CodeMirror and Mermaid ship as separate chunks (`lib/client-<name>.js`) fetched via a `/sidebar/bundle` route.
- **Client/host split:** `ctx.betterSidebar` exists **only** in the browser half. The host half never touches the service — it goes through `/sidebar/api/*` HTTP routes (`session.cwd`, `fs.tree`, `fs.read`, `fs.write`, `git.*`, `settings.*`).
- **Theming by token:** consumes `--dsw-alias-bg-layer-1` etc. so it survives all ten `dsh-web-ui` skins; explicitly documents *"never consume `--dsw-specific-sidebar-fill`"* (left-nav exclusive). CSS-module hashes are declared **not** a contract.
- **Real-terminal stack:** xterm.js + **node-pty** (a native module) — an actual shell, not an emulation.

---

## 6. Boundary discipline toward the host (the load-bearing part)

`AGENTS.md` states the house rules in the imperative:

- 「禁止修改 DeepSeek Harness (DSH) 源码」 — **zero writes** to the DSH checkout at `~/.dsh/source/current`; no harness-package modifications; no commits to official branches.
- Mounting happens **only** through `cordis.patch.yml` + the profile mechanism. The patch file itself does exactly one thing: **inserts a plugin row** (`id: better-sidebar`, `name: dsh-better-sidebar`) into the host's bundle stack at profile boot. **No host core file is modified.**
- Feature/fix work routes through `feat/*` / `fix/*` branches and `gh pr create`; only pure doc changes may push to main.

### The CI gate is stronger than v236's

v236 mechanised non-invasiveness with static checks (`verify:boundary`, `verify:patch-surface`). v237 goes further — its `plugin-mount` CI job is an **integration contract test**:

```
pnpm build && pnpm pack && pnpm test:mount
```

…which packs the tarball, **mounts it into a real DSH instance on a scratch profile**, and renders it headlessly under **Playwright Chromium**, asserting: the shell and `[data-dsh-better-sidebar]` root mount, no `dsh-better-sidebar:` error bars, no page errors, no plugin console errors, panel expansion via menu, and that the terminal/editor **lazy chunks actually load**.

Plus unit suites: `service.spec.ts` (registration lifecycle, matching, dedup, enablement gating), `builtins.spec.ts` (registry assertions), `plugin-list.spec.ts`, `theme.spec.ts` (token consumption).

**This is the fourth consecutive ship handing the vault machinery for its own invariants** — v234 staleness-tracking → v235 doc-verification gates → v236 CI boundary gates → **v237 a real-host mount smoke test**. Pointed, again, at the C22–C27 stale-row backlog and the deferred retire pass.

---

## 7. Supply chain — genuinely mixed, and worth stating both ways

**Positive (a real exemplar):**
- **npm Trusted Publishing via OIDC** — `pnpm publish --provenance --access public`, **no `NPM_TOKEN` secret in the repo**, provider/org/repo/workflow pinned at npmjs.com, and the tag must match `package.json` exactly.
- Zero-source-write rule + build-purity gate + the mount smoke test above.
- **Sandbox by default with visible, user-initiated unlock:** embedded content runs in **opaque-origin sandboxed iframes with CSP**, sandbox status is *shown in the UI*, and unlocking is a deliberate, temporary, per-content action.
- **#83 honest-deficiency disclosure:** the README volunteers its own gaps — no file watcher, no git push/pull/fetch, terminal remounts when dragged between panes, unusable below a 768 px viewport.

**Negative (why you still should not install it):**
- A **`prepare` lifecycle script** (runs on install from git).
- **`node-pty`** — a native module that compiles at install.
- The sandbox-escape settings exist at all: `browserNoSandbox`, `htmlViewerNoSandbox`, `htmlViewerDefaultUnsafe`. Disclosed and default-safe, but they are one toggle away inside a panel that also holds **a real shell and an embedded browser**.
- **17 peer dependencies pinned to a release candidate** (`^0.1.0-rc.6`) of a host still labelled a developer preview with breaking changes promised.
- A **~2-week-old public plugin ecosystem** with ≥6 competing, operator-undisclosed directory sites (v236 already caught one publishing the wrong licence for a different plugin).
- ⚠️ **NOT source-cloned.** Everything above is from the rendered repo, raw README/README_EN/`package.json`/`dsh.plugin.json`/`cordis.patch.yml`/`AGENTS.md`/`docs/external-plugin-guide.md`. Treat the tree as untrusted until inspected.

---

## 8. Ecosystem observations (corpus-knowledge, not mints)

- **The land-rush is real and now has structure.** Beyond the ≥8 SEO directories v236 catalogued, there are now: a 106-repo community org with governance (`omdsh-dev`), a rival plugin+skin *collection* (`zhu1090093659/dsh-web-ui` — task board, git graph, right-side panel, mobile UI, pet, token stats, skin center), and **at least two curated "awesome" lists** (`awesome-dsh-plugin/awesome-dsh-plugin`, `Dominic789654/awesome-deepseek-harness`) — a Pattern #68 genre instance forming around a two-week-old surface.
- **Plugins are already colliding at runtime.** v0.13.0 added **mutual exclusion with `aionui-panel`**: if that plugin claims the right panel, better-sidebar *unmounts itself entirely* (`externalDisable: true`, pushed live via `settings/document-updated`). Two independent authors negotiating a scarce UI slot through a settings protocol.
- **A corpus-adjacent collision.** `aionui-panel` (inside `zhu1090093659/dsh-web-ui`) is a pixel-faithful port of **AionUi**'s Explorer + Preview — and AionUi is built by **iOfficeAI, the author org of corpus subject v206 OfficeCLI**. ⚠️ Different author, no citation, no dependency → **NOT #57**; an ecosystem-collision data-point only.

⚠️ **Correction to the corpus:** v236's head describes *"a four-day-old ecosystem."* That conflates *when the corpus noticed DSH* with *how old it is*. DSH's own page shows **12,404 commits and ~154.1k stars** (page-stated), while this plugin's releases run **11 → 17 Aug**. The accurate statement: **the public plugin ecosystem is roughly two weeks old; the DSH codebase is not.** Flagged for the audit.

---

## 9. What this proves about v235 and v236

1. **v235's plugin thesis holds at a second, independent seam.** v236 swapped the *front door*. v237 adds a *panel* and gets a service published on the host context — a different extension surface, an unrelated author, the same kernel, still zero core writes. Two independent confirmations in two days.
2. **The session-scoped isolation claim is load-bearing too.** Every tab and viewer receives a `SessionScope`; state, layout and terminals are per-conversation; `getSnapshot()` returns `sessionId` + panel geometry + open tabs + prefs. The host's session identity is the axis the whole UI hangs on — consistent with v235/v236's append-only session log finding.
3. **The extension kernel is genuinely re-entrant.** A plugin can publish a service that other plugins inject. That is a stronger claim than "the UI is swappable," and it is the thing v235's *"Everything is a Plugin"* tagline actually cashes out to.

---

## 10. Honest limits of this analysis

- **Not source-cloned** — no line-level verification of `src/`.
- Stars, forks, commit and issue counts are **page-stated** (§37.4); the GitHub API is mocked here and was not relied on.
- The "216 commits" and release cadence come from the repo surface, not from a cloned history.
- The extension API is documented thoroughly *by the project itself*; I verified internal consistency across README / README_EN / `AGENTS.md` / `docs/external-plugin-guide.md` / `dsh.plugin.json` (and caught the 7-vs-6 drift), but I did not execute it.
- No independent third-party review of this plugin's security posture was found.

---

## 11. Sources

- Repository: https://github.com/omdsh-dev/DSH-better-sidebar
- Org: https://github.com/omdsh-dev · hub: `hub.omdsh.dev`
- Raw: `README.md`, `README_EN.md`, `package.json`, `dsh.plugin.json`, `cordis.patch.yml`, `AGENTS.md`, `docs/external-plugin-guide.md`
- Host: https://github.com/deepseek-ai/deepseek-harness (corpus v235)
- Sibling plugin: https://github.com/ccch1mneyyy/dsh-TUI (corpus v236)
- Ecosystem: `zhu1090093659/dsh-web-ui`, `awesome-dsh-plugin/awesome-dsh-plugin`, `Dominic789654/awesome-deepseek-harness`, `iOfficeAI/AionUi`
