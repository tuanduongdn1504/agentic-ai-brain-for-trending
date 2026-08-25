# (C) DeepSeek-Balance-Whale-Widget — Deep Dive

**Wiki v277 · 2026-08-25 · subject `MeteorNOX/DeepSeek-Balance-Whale-Widget` · npm `dsh-whale-widget` · MIT**

> *"DSH Web 界面右下角的 DeepSeek 余额小鲸鱼挂件"* — a little balance whale that lives in the bottom-right corner of the DeepSeek Harness web UI.

---

## 1. What it is

A **DeepSeek Harness (DSH) bundle plugin** that parks a cartoon whale in the corner of the harness's web GUI. The whale's speech bubble shows three things: your **DeepSeek API account balance**, **today's spend**, and — after each conversation turn ends — **what that turn just cost**. You can drag it; it snaps to any of the four edges; it mirrors itself when it snaps left; it squashes when pressed and plays a rubber-duck noise; clicking its bubble cycles weighted random dialogue.

Underneath the toy is real engineering: a host-side plugin (`lib/index.js`, 2,023 lines, ESM, **zero dependencies**) that registers **eight HTTP routes** on the harness's own web server, injects a browser widget via `tapIndex`, listens to the harness's session-event stream to meter per-turn cost from the model's *real* usage counts, and maintains a local spend ledger.

Two ways to get "today's spend", and the default one is the interesting idea:

- **小鲸鱼记账 / whale bookkeeping (default, no token needed)** — poll the balance; every time it goes *down*, add the difference to today's total. No usage API, no token counting, no log parsing.
- **实时·令牌 / live token mode (optional)** — call DeepSeek's platform usage endpoint for hourly token buckets and convert to money with a built-in peak/valley price table.

⚠️ **And the repository contains a second, different product** — see §11. It is a Windows desktop app that rewrites your **global Claude Code settings**. That is the single most important fact in this document for the vault operator.

**Author:** `MeteorNOX` (`moonlightqihaoran@gmail.com`) — a pseudonymous individual. **NOT Anthropic**, not DeepSeek.

---

## 2. Source verification

**Two independent clones, `diff -rq` clean in BOTH directions** (only per-clone `.git/index` and reflogs differ, as expected).

```
HEAD = 4448c61db7d180c4c307aa3fa734db7c8507658d
       "fix: 紧急修复 dsh-market 安装报错"  2026-08-25 01:12:49 +0800
```

| Fact | Command | Value |
|---|---|---|
| Tracked files | `git ls-files \| wc -l` | **15** |
| Commits on main | `git rev-list --count HEAD` | **30** |
| Commits all refs | `git rev-list --count --all` | **49** |
| Roots on main | `git rev-list --max-parents=0 HEAD` | **1** (`306e660`) |
| Merges | `git rev-list --count --merges HEAD` | **9** |
| Tags | `git tag \| wc -l` | **9** |
| Age | first → last commit | **2026-08-20 → 2026-08-25 (5 days)** |
| Author emails | `git log --format=%ae \| sort \| uniq -c` | **4** |

`lib/index.js` 2,023 lines / 79,272 bytes · `README.md` 232 lines · `whale-widget-prompt.md` 202 lines · `publish.yml` 124 lines · `package.json` 34 lines · `LICENSE` 21 lines.

**Contributors** — 20 commits `moonlightqihaoran@gmail.com` (MeteorNOX, owner) · 6 `fangletian2008@outlook.com` (方便面 / `fangbm`) · 2 `under-the-ocean@…` · 2 `3179818449@qq.com` (`21253soursweetlemon`); PR #26 came from `xiaolinnnnnnn`. Merged PR numbers in commit subjects run to **#46**, with 13 distinct issue/PR references (`#6 #7 #13 #15 #16 #18 #19 #27 #28 #30 #31 #33 #46`). **A third of the commits and most of the bug fixes came from outside the owner** — a genuine little community, five days old.

**Environment limits (§43.1):** **no network** — npm registry contents, GitHub's rendered release list, DeepSeek's live API and any world-first priority claim are **UNVERIFIED**. `python3` is silently SIGKILLed here (D41), so all measurement used `grep`/`awk`/`sed`/`wc`. **I did not install or run either product** — there is no DSH instance and no Windows host, so every behavioural claim is read from source.

---

## 3. THE SHIP'S RULE

⭐⭐⭐⭐⭐ **Every failure in this repository sits on a boundary it does not own — and every success sits inside one it does.**

Inside its own walls the work is careful to the point of elegance: a never-throw route contract, retry-with-stale-fallback, in-flight request de-duplication, per-session cost bucketing that anticipates subagent parallelism, an explicit memory-leak disposer, an 8 KB body cap, a price rule **versioned by date** so historical buckets are priced under the rule in force when they happened, and 21 `textContent` writes against 2 `innerHTML` — both static literals.

Everything wrong is wrong at a seam owned by **someone else**:

| The broken thing | Whose contract it was |
|---|---|
| `package.json` missing `repository` → marketplace install failed | **another project's** probe script |
| `~/.codex/config.toml` overwritten wholesale | **OpenAI's** file format (and a missing TOML parser) |
| `v1.0.0` is the highest release and points at a dead commit | **semver's** sort order + GitHub's release list |
| `"license": "MIT"` declared 40 h before a LICENSE file existed | **npm's** metadata field vs the file |
| `Access-Control-Allow-Origin: *` on account-balance routes | **the browser's** same-origin model |
| the `[0]` currency bug that over-booked thousands of ¥ | **DeepSeek's** unstable array order |
| the price table needing hand-maintenance | **DeepSeek's** pricing decisions |
| the exported plugin name still `whale-balance-widget` | **its own** written invariant, ungated (§4) |
| `whale-widget-prompt.md` declaring `v0.2.5` at package `0.2.10` | **its own** version header (§6) |

⭐ **The generalisation: an external contract is the one thing you cannot test from inside your own repository.** You can lint your code, assert your invariants and gate your merges, and none of it tells you that a stranger's install script needs a field you never wrote, or that the config file you are helpfully rewriting belongs to a tool whose format you cannot parse.

⭐⭐ **And the corollary this ship supplies, twice over: a written invariant with no gate is a wish.** The spec document states, in as many words, that the exported plugin name must match `package.json`'s — and it does not. The document states its own version — and that is the only false sentence in it.

**The ladder** — v270 *no gate fires on a claim true when written* · v271 *a gate's scope is inherited from where it lives* · v272 *a gate holds when something else already requires it* · v273 *a check is only as permanent as the place you put it* · v274 *a claim is safe when a gate covers it or a habit covers it* · v275 *a check cannot survive someone with standing to overrule it* · v276 *the reliability of a number is predicted by its audience* · **v277 — the gate you cannot write is the one whose requirement lives in someone else's code.**

---

## 4. ⭐⭐⭐⭐⭐ The invariant the spec states and nothing enforces

`whale-widget-prompt.md:27`, architecture rule #2, states the export contract explicitly:

> **导出形式**：`const name = 'dsh-whale-widget'; const inject = ['webServer', 'credentials']; function apply(ctx) {...}; export { name, inject, apply }`（具名导出，**与 `package.json` 的 `name` 一致**）

*(…named exports, **consistent with `package.json`'s `name`**.)*

`lib/index.js:1417`:

```js
const name = 'whale-balance-widget'
```

Three surfaces carry this plugin's identity. Two say `dsh-whale-widget` — `package.json`'s `"name"`, and `cordis.patch.yml:14-15`'s `id:` and `name:`. The third, the runtime export, says **`whale-balance-widget`**. The document names the invariant that binds them; nothing checks it.

⭐⭐⭐ **And the stale value is a fossil I can date.** `whale-balance-widget` is the *old manual-install identifier* — and the README proves it, because its "从旧手动安装升级" section tells users to delete exactly this stanza from their profile:

```yaml
- insert:
    - id: whale-balance-widget
      name: ./whale-balance.mjs?v=1
```

So the name belongs to the pre-package era — **the era whose tag is the orphaned `v1.0.0`** (§5). When the project was rebuilt as an installable package, two of three identity surfaces were renamed. The one nobody reads kept the dead name, and `lib/index.js:1753`'s log prefix `'[whale-balance]'` kept it too.

**Severity, honestly: low, and I want to be exact rather than dramatic.** Installation is unaffected — Cordis resolves the bundle by the patch's `name: dsh-whale-widget`, which maps to the npm package, not by the export. The consequences are (i) the plugin's registered identity inside Cordis and its log lines carry the old name, and (ii) a user upgrading from the legacy manual install has **both** artifacts registering as `whale-balance-widget` — which is precisely the collision the spec warns about at line 30: *「若环境中存在旧版动态插件占用同名路由，先 `cordis_stop`/`cordis_undefine` 释放，否则注册会因路径重复抛错」* (release the old plugin first, or registration throws on duplicate paths). The rename would have made the new package distinguishable from the old one. It did not happen, in the one place the project's own documentation said it must.

---

## 5. The HEAD commit is the finding

The newest commit — about a day old at the time of this wiki — is **「fix: 紧急修复 dsh-market 安装报错」** *(emergency fix: dsh-market install error)*:

> 插件市场的 DSH Desktop 安装走 npm 精确版本路径，但因 package.json 缺少 repository 字段，市场探测脚本无法将本包关联到 GitHub 仓库，导致「DSH Desktop managed installation requires an npm package with an exact published version」错误，市场安装不可用。

*(The marketplace's DSH Desktop install path goes through npm's exact-version route, but because `package.json` lacked a `repository` field, the marketplace's probe script could not associate this package with its GitHub repository, producing the error "DSH Desktop managed installation requires an npm package with an exact published version". Marketplace installation was unusable.)*

The diff adds three fields — `repository`, `bugs`, `homepage` — and bumps to `0.2.10`.

⭐⭐⭐ **Read what that means.** For an unknown stretch, a plugin auto-published to npm nine-plus times was **not installable from the marketplace most of its users would use**, and nothing in the repository could have detected it. There is no test for "a field a third party's script requires". The requirement was never written anywhere this author could read. The failure surfaced as an error string **inside someone else's software**.

⭐⭐ **Note which gate did exist.** The repository's sole automation is a *publisher*. It fired on every push, checked the version wasn't already on npm, pushed the tarball, cut a release. It verified **that publication happened**. It never asked whether anything could be installed. **A publisher is not an installer**, and the difference was one metadata field wide.

⭐ **Corpus-recursive:** `dsh-market` is a package in `zhu1090093659/dsh-web-ui` — **corpus subject v239**. Verified directly: a clone of that repository has `packages/dsh-market` in its tree.

---

## 6. The version story

⭐⭐⭐⭐ **The highest-numbered release in this project is an orphaned commit from before the project's own history began.**

| Tag | Created | Target |
|---|---|---|
| **`v1.0.0`** | **2026-08-18 11:14:20** | `8b86e7b` |
| `v0.1.0`, `v0.2.0` | 2026-08-20 21:18:21 | `306e660` (main's root) |
| `v0.2.2` / `v0.2.5` / `v0.2.7` | 08-21 / 08-22 / 08-22 | `e18577d` / `973076b` / `9251b7f` |
| **`v1.0.0+win`** | **2026-08-22 20:58:59** | `b4df1a2` |
| `v0.2.9` / `v0.2.10` | 08-23 / 08-25 | `52cbe34` / `4448c61` |

`git merge-base --is-ancestor 8b86e7b X` returns **NO for all three branches** (`main`, `origin/For-Windows`, `origin/For–WinDesktop`). Commit `8b86e7b` — *"Add files via upload"*, 2026-08-18, **two days before main's root** — holds exactly two files: `README.md` and **`dsh-whale-widget.zip`**. Nothing but the tag keeps it alive.

**This is not carelessness; it is a deliberate re-baseline whose cost is permanent.** `v1.0.0` *is* the manual-install era the README documents — a zip you download and unpack. When the project became a real installable package, the author restarted at `0.2.0`, because `0.x` honestly describes a five-day-old plugin and `1.0.0` did not.

⭐ **The judgment was right and the consequence is unfixable.** Every tool that orders releases by semantic version — GitHub's release list, dependency resolvers, a human skimming a dropdown — sorts `v1.0.0` and `v1.0.0+win` above `v0.2.10` forever. The project's newest work is permanently ranked below a dead zip file. **No gate applies, because nothing was violated: semver did exactly what semver does.**

### 6a. The two versions published and never tagged

`package.json`'s `version` at every HEAD-reachable commit, in commit-date order, is **non-monotonic**:

| Commit | Time | version |
|---|---|---|
| `ac4f8d0b` | 15:00:54 | **0.2.6** |
| `95fad7ba` (merge PR #18) | 15:01:15 | **0.2.5** |
| `bbacbe68` (merge PR #16) | 15:02:29 | **0.2.5** |
| `73236779` (merge PR #19) | 15:07:48 | **0.2.6** |

Three PRs landing in seven minutes, each with its own view of the version field, sent it **up, back down, and up again** — on a repository that auto-publishes `package.json`'s version on every push. And `0.2.6` and `0.2.8`, both declared on main, have **no tag**: the series jumps `v0.2.5 → v0.2.7 → v0.2.9 → v0.2.10`.

⭐⭐ **Why those two is the point.** The workflow step that creates a Release and its tag was added at `7feb2419` on **2026-08-24** (PR #46). Every tag before `v0.2.10` was made **by hand** — and the two the hand missed are exactly the two a merge race scrambled. **v272's rule in a foreign codebase: the checks you must remember to run are the checks you do not have.**

✅ **And then they fixed the class.** PR #46 automated tag-and-release creation off the same version field the publish step uses, idempotently (`gh release view … && exit 0`). The habit became a gate. Most projects never get there.

*(Whether npm holds `0.2.6`/`0.2.8` is **UNVERIFIED** — no network. Verified: main declared them, the workflow publishes on push, no tag exists.)*

---

## 7. The spec that is also a prompt

⭐⭐⭐⭐ `whale-widget-prompt.md` (202 lines) is titled 「**完整生成提示词**」 *(complete generation prompt)* and says of itself:

> 本提示词汇总了完整需求、架构、全部行为规格、视觉参数与踩坑结论，**可直接交给 AI 复现或维护**。

*(…can be handed directly to an AI to reproduce or maintain the project.)*

The README designates it the authority: consult it when changing text position, colours, animation, snap logic, dialogue groups **or the price table**. So the spec, the design doc, the onboarding doc and the maintenance interface are **one file, written as a prompt for an LLM**. For a vault whose founding thesis is *"the LLM is the programmer, the wiki is the codebase"*, this is the same idea reached independently — and the **third consecutive corpus ship to productise something this vault does** (v268 `lat.md`, v269's Karpathy-named `llm-wiki` skill, v277).

Its section 六 is the best part: **12 numbered 「关键技术结论（踩坑记录）」** — hard-won conclusions, each with its reason:

- **#5** an async `webServer` handler that throws is swallowed into an empty 400, so **every route must always return JSON**. The code obeys: `balance.json`'s catch returns `200` with `{ok:false,…}`.
- **#6** you cannot CSS-transition to `auto`, so all positioning is pixel `left/top` — otherwise right-edge snapping visibly jumps.
- **#7** a transition delay contaminates every property, so the mirror-flip needs the per-property longhand `transition:opacity .16s ease .36s,transform .3s ease`.
- **#10** the ledger accumulates from *observed* balance drops, so **spend while DSH is closed is silently missed**; only token mode is exact.

⭐ **#10 is honest deficiency disclosure of the strongest kind** — volunteering the error model of the project's own headline feature, in the file a maintainer is told to read.

### 7a. The drift census, and its shape is the finding

| # | The document says | The code says | Class |
|---|---|---|---|
| 1 | 「当前版本：**v0.2.5**」 | `package.json` = **0.2.10** | **FALSE** |
| 2 | `size.json` — **`GET / PUT`** | `:1923` `req.method === 'PUT' \|\| req.method === 'POST'` | omission |
| 3 | GET returns **9** fields | `writeSizeConfig` persists **11** (`scrollGapOn`, `scrollGapPx`) | omission |
| 4 | prices 0.05/0.10, 1.5/3.0, 4.5/9.0 | those are `BASE_PRICE`; **`PRO_PRICE` is 3×**, untabulated | omission |
| 5 | *(silent)* | `readBody` caps at **8192 bytes**, `req.destroy()` | omission |
| 6 | *(silent)* | `lastTurn` is **one global slot** across all sessions | omission |
| 7 | export name must equal `package.json`'s | `:1417` says `whale-balance-widget` | **FALSE** (§4) |

⭐⭐⭐⭐⭐ **Five of seven divergences are omissions. The two false statements are the document's claim about its own currency, and its claim about the export name.**

Every rule the document states *about the system's behaviour* is still true. It even runs **ahead** of its own header — it documents the 2026-08-23 weekend-valley rule and `WEEKEND_VALLEY_FROM_SEC`, both of which arrived at `v0.2.8`, three releases after the `v0.2.5` it declares. So the version header is wrong in **both directions at once**: under-claiming what the document contains, over-claiming how fresh it is. A reader cannot use it to tell which half to trust.

⭐ **This sharpens v270 (*the only defence is a date*) and D40 (*a stale label is safe when declared*).** A declared version is a safe compensation **only while the declaration is itself maintained**. An unmaintained version header is worse than none, because it licenses confidence in precisely the parts that moved — and it is the one line no substantive edit ever *forces* you to revisit. You change the snap logic, you update the snap section; nothing anywhere sends you back to line 7.

---

## 8. The gate census: the only automation publishes

**Extent: full-extent grep for test/lint/typecheck/build invocations across all 15 tracked files, plus `ls -a .github/`.**

- `.github/` contains **exactly one file**: `workflows/publish.yml`.
- `package.json` has **no `scripts` field at all**, no `dependencies`, no `devDependencies`.
- **No test file, no test framework, no linter, no formatter config, no typechecker, and no lockfile** on main. *(Positive control: `npm` returns multiple hits in the workflow, so the search works.)*

⇒ **Zero automated checks of any kind run against 2,023 lines of JavaScript that handle a paid API credential.** The one workflow is `on: push: branches: [main]` and its job is to publish.

⭐⭐⭐ **`--provenance=false`.** The workflow grants `permissions: id-token: write` and adds a step *"Upgrade npm for OIDC support"* whose comment states the requirement precisely — 「必须：npm >= 11.5.1 才支持 Trusted Publishing (OIDC) 自动交换；npm 10.x 会直接 ENEEDAUTH」. Real effort was spent obtaining a cryptographic build identity. Then:

```
npm publish --access public --registry https://registry.npmjs.org --provenance=false
```

**Provenance is the attestation that OIDC identity exists to produce** — the signed, publicly verifiable link between this tarball, this commit, this repository and this workflow. It is exactly what would let a user of a plugin that reads their API key confirm the npm bytes match the GitHub source. It is switched off by an explicit flag. *(The likeliest cause is pragmatic — the workflow supports both OIDC and `NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}`, and provenance interacts with that choice — but the effect stands: the identity authenticates and does not attest.)*

⚠️ **`npm install -g npm@latest`** — an unpinned global package-manager install on every run, in the job holding publish rights. And **`npm ci || npm install`** in a repo with no lockfile, so `npm ci` can only ever fail through. With zero declared dependencies the blast radius is small; the pattern is not.

✅ **Well-built parts of the same file:** `concurrency: { group: npm-publish, cancel-in-progress: false }` stops two pushes racing a publish; the "already published" check makes a re-push idempotent instead of a red build; the changelog step compares `mergedAt` against the previous tag using **Unix timestamps**, with a comment explaining why — 「mergedAt 是 UTC(Z)，%cI 带本地时区偏移，字符串比较跨时区会错判」 (*string comparison across time zones misjudges*); release creation is idempotent. Someone thought hard about the failure modes **of the publish path**. Only of the publish path.

---

## 9. Security surface — precise, with the severity honest

`lib/index.js:110-114`:

```js
const JSON_HEADERS = {
  'Content-Type': 'application/json; charset=utf-8',
  'Access-Control-Allow-Origin': '*',
  'Cache-Control': 'no-store',
}
```

Eight routes are registered (lines 1853, 1872, 1891, 1906, 1919, 1979, 1988, 1997) plus a `tapIndex`. **Three carry `JSON_HEADERS`**: `balance.json`, `last-turn.json`, `size.json`. The image, gif, two sound routes and `widget.js` set their own headers and do **not**.

🔴 **The real issue is the read side.** DSH's web server binds `127.0.0.1:3080`, and localhost binding *is* the security control. `Access-Control-Allow-Origin: *` **is the hole in it**: any page in any tab can `fetch('http://127.0.0.1:3080/dsh-whale/balance.json')` cross-origin and read the response.

- `balance.json` → `{ok, totalBalance, currency, updatedAt, todayUsage, isPeak, usageMode}` — **the account balance and today's spend.**
- `last-turn.json` → `{seq, turn, amount, tokens, ts}` — **the ¥ cost, token count and timestamp of the most recent agent turn**, polled once per second by the widget and therefore always fresh.

A silent, unauthenticated cross-origin disclosure of financial and activity metadata with a concrete exploitation path. It is **not** credentials and **not** conversation content, and I would rather be exact than inflate it.

🟡 **The write side is bounded to a nuisance — and I over-rated it before reading the code.** `size.json:1923` accepts `PUT` **or `POST`**, and `POST` is the method that qualifies as a CORS *simple request* needing no preflight. But `writeSizeConfig` (`:1791`) is a **strict whitelist**: 11 positional scalars, each coerced (`normalizeUsageMode`; `peakMode === 'liangwen' || 'qiangqiang' ? … : 'default'`; `soundSet === 'fx1' ? 'fx1' : 'duck'`; booleans via `!== false`; numbers via `typeof === 'number'`), reassembled into a **fresh object literal** with a server-generated `updatedAt`, written to a **fixed candidate path list**. No request key reaches the file; no path is attacker-controlled; no prototype-pollution or traversal path exists. `readBody` (`:1835-1851`) caps the body at **8192 bytes** and calls `req.destroy()`.

⇒ **Worst realistic outcome: a web page flips your widget's size, sound and usage mode.** ⚠️ `usageMode` *is* writable and a write invalidates the balance cache, so a hostile page can toggle which accounting mode the whale reports from — annoying, not compromising.

⭐ **The undocumented method is the dangerous one.** Both README and spec say `GET / PUT`. The code accepts `POST` — the one that needs no preflight.

✅ **No XSS.** 21 `textContent` assignments against **2** `innerHTML`, both static author-written literals (`:197` the hamburger's three `<span>`s; `:372` the bubble SVG geometry), no interpolation. The only network-derived string is the balance error, landing at `:715` as `hint = state.message.slice(0, 14)` into `hintEl.textContent`. For a framework-free 2,000-line hand-written widget that is real discipline.

✅ **No path traversal in `?set=`.** `soundSetFromUrl` extracts the query value and it is used only as a **key lookup** — `SOUND_SETS[…] || SOUND_SETS.duck` — against an object with two hardcoded keys. A traversal string misses and falls back to `duck`.

✅ **Credential handling is clean.** `ctx.credentials.resolve('DEEPSEEK_API_KEY')` at `:1527`; used only as a `Bearer` header (`:1539`, and `:1595` for the platform token). Never written to disk, never placed in a response body, never logged. The file's **only** `console.error` is `:1753` — `'[whale-balance]', payload.code, payload.error` — a code and message. *(Extent: grep across all 2,023 lines. Note `:1532` contains the literal string `'未配置 DEEPSEEK_API_KEY'` — a credential **name** in an error message, not a value.)*

⚠️ **The author's workstation ships in the package.** `IMAGE_CANDIDATES`, `SIZE_FILE_CANDIDATES`, `USAGE_FILE_CANDIDATES`, `SOUND_SETS` and `RUA_GIF_CANDIDATES` each end with hardcoded absolute paths under **`D:/TestBox/deepseek/`** — for the two config files these are **write** fallbacks. The spec *declares* them (*「本机旧绝对路径仅作 fallback」*), which is the honest thing to do, and on a machine without that path the risk is nil. It is still a developer's disk layout shipped to every installer.

---

## 10. Privacy and the ledger

### 10a. Privacy: verified clean, by construction

I read the session-event handler in full (`:1425-1482`). It reads **exactly**: `event.type` · `event.data.turn` · `event.data.usage.{inputTokens, cacheReadTokens, outputTokens, reasoningTokens}` · `event.data.message.source.model`.

**No prompt text. No model output. No tool arguments. No file paths.** The aggregate holds only numbers; the published record is `{turn, amount, tokens, ts}`. A plugin sitting inside an agent harness, watching every turn go by, takes **four token counts and a model name**. That is the correct posture and it is correct *by construction* — there is no content in the data structure to leak.

⭐ **The best twenty lines in the codebase**, and what makes them good is that each avoids a named bug:

```js
let turnAggs = new Map() // sessionId -> { turn, cost, tokens, lastTs }
…
function finalizeTurn(sessionId) {
  const agg = turnAggs.get(sessionId)
  if (agg && agg.cost > 0) {
    lastTurn = { turn: agg.turn, amount: agg.cost, tokens: agg.tokens, ts: agg.lastTs }
    lastTurnSeq++
  }
  turnAggs.delete(sessionId)
}
```

with the comment 「用 Map 分桶避免主会话与子代理（spawn/fork）并行时串账」 — **bucket by Map so the main session and spawned subagents running in parallel do not cross-book each other's spend.** He anticipated subagent parallelism in a cost meter. Then: a turn number changing *without* a `turn/end` still settles the previous turn, so a dropped lifecycle event settles late instead of vanishing; `if (agg.cost > 0)` suppresses no-op turns; every numeric read is `Number(x) || 0`; the whole handler is `try/catch`-wrapped so a malformed event cannot take down the host; and a second listener on `session/disposed` deletes stale aggregates, commented 「避免内存泄漏」.

🔴 **The one real defect in it:** aggregation is per-session but **`lastTurn` is a single global slot**. With two sessions running, the widget shows whichever settled most recently, with no indication which conversation it belongs to. Tokens are never cross-booked — the money is right — but the *attribution shown to the user* can be wrong. Neither README nor spec mentions this.

### 10b. The ledger, and the bug that shaped it

`recordLedgerUsage` (`:1665-1698`) is three branches: new day → archive and re-baseline; **currency changed → re-baseline only, record nothing**; otherwise → if the balance fell, add the difference. History is capped by `Object.keys(led.history).sort()` then shifting off the oldest while `> 30` — correct, since `YYYY-MM-DD` keys sort chronologically.

⭐⭐ **The currency guard, and the incident that earned it, are documented in the code at the fix site** (`:1663-1664`):

> 币种感知：观测币种与上次不同时只重置基准、不记差值——数值跳变来自币种切换而非真实消费（`[0]` 选币时代 CNY/USD 随机切换曾记出巨额假账，见 **#13**）。

*(…in the `[0]`-currency-selection era, random CNY/USD switching once recorded huge false accounts, see #13.)*

DeepSeek's `balance_infos` is a multi-currency array **whose order is not stable**. Taking `[0]` made the displayed balance flip between CNY and USD, and the ledger **booked every flip as a purchase — fabricating thousands of yuan of spend in a single day.** ⭐ *A derived number, computed from an upstream field the project did not control, was confidently wrong by three orders of magnitude, and the only reason anyone knows is that a user noticed the total.* This is D44 done right: the artifact carries its own context, with the issue number, at the line that fixes it.

🔴 **Two residual edges I can derive from the code, neither documented:**
1. `currencyChanged` requires `typeof led.lastCurrency === 'string' && led.lastCurrency !== ''`. On a **legacy ledger written before the field existed**, `lastCurrency` is absent, the guard cannot fire, and the first post-upgrade observation takes the `else` branch — comparing today's balance against a `lastBalance` possibly recorded in a *different currency*. The #13 bug can therefore still book one bogus delta, once, on upgrade.
2. On day rollover the code sets `lastBalance = currentBalance` and books nothing — so spend between the last observation of one day and the first of the next is **attributed to neither day**. With a 60 s poll that silently drops up to a minute of spend at every midnight, on top of the disclosed "missed while closed" case.

✅ **Verified arithmetic:** `PRO_PRICE` is exactly **3×** `BASE_PRICE` across all six values (0.05→0.15, 0.1→0.3, 1.5→4.5, 3.0→9.0, 4.5→13.5, 9.0→27.0), with the source dated in a comment — 「deepseek-v4-pro 为 flash 的 3 倍价（官方 2026-08-17 生效）」.

⭐⭐⭐ **Price rules are versioned by date, not by flag.** `WEEKEND_VALLEY_FROM_SEC = Math.floor(Date.UTC(2026, 7, 22, 16, 0, 0) / 1000)` — Beijing 2026-08-23 00:00, arithmetically correct — and `isPeakTime(timeSec)` takes **the bucket's own timestamp**, so historical hourly buckets are priced under the rule in force *when they happened*. The comment states the reason: 「生效时刻之前的历史分桶仍按旧规则计价，所以周末判定带生效分界」. Most people would have flipped a boolean and silently re-priced last week. **The vault's own v270 rule was "the only defence is a date"; this author put the date in the code.** ⭐ And the fixed-offset local time is done correctly without a library: `new Date(n*1000 + 8*3600*1000)` read with `getUTCDay()`/`getUTCHours()` yields Beijing calendar fields regardless of host timezone — with the comment saying exactly that.

✅ **Balance fetch robustness:** 20 s `AbortSignal.timeout` (`:1541`), 25 s cache (`BALANCE_TTL_MS`, `:59`), in-flight de-duplication, one retry at 500 ms for network/timeout/5xx, **no retry on 4xx** (`:1570` `const transient = !(lastErr && /^HTTP 4\d\d/.test(lastErr.message))`) — correct, a 401 will not fix itself — and a transient failure returns the last good balance marked `stale: true` rather than flashing an error.

---

## 11. 🔴 There are two products here, and the second one rewrites your Claude Code config

`origin/For–WinDesktop` — **note the EN DASH (U+2013)**, sitting beside a separate `origin/For-Windows` with an ordinary hyphen — holds **121 files**: a standalone **Tauri v2 Windows desktop application**, `package.json`/`Cargo.toml` name **`ds-desktop-whale`**, version **`1.0.0`**, described as 「DS Desktop Whale · DeepSeek 余额查询与记账 · 独立 Windows 桌面版」. Contributed by `xiaolinnnnnnn`, merged as PR #26, tagged **`v1.0.0+win`**.

It is not a cosmetic pet. Its `src-tauri/src/service/` holds two modules whose entire purpose is writing other vendors' agent configs.

### 11a. `claude_config.rs` — writes your global `~/.claude/settings.json`

Header comment: 「把本应用的 base_url / api_key / 模型写入 `~/.claude/settings.json` 的 `env` 字段，**使 Claude Code 命令行使用所配置的模型**」 *(…so that the Claude Code CLI uses the configured model)*. `write_claude_settings` inserts **seven** environment variables:

```rust
env.insert("ANTHROPIC_BASE_URL",              json!(cfg.base_url));
env.insert("ANTHROPIC_AUTH_TOKEN",            json!(cfg.api_key));
env.insert("ANTHROPIC_MODEL",                 json!(primary));
env.insert("ANTHROPIC_DEFAULT_HAIKU_MODEL",   json!(haiku));
env.insert("ANTHROPIC_DEFAULT_SONNET_MODEL",  json!(sonnet));
env.insert("ANTHROPIC_DEFAULT_OPUS_MODEL",    json!(opus));
env.insert("ANTHROPIC_MODEL_CONTEXT_WINDOW",  json!(…));
```

with `DEFAULT_BASE_URL = "https://api.deepseek.com/anthropic"` (`config/model.rs:9`).

🔴 **In plain terms: installing this app and saving its config repoints every Claude Code invocation on the machine at DeepSeek** — all four model aliases (haiku/sonnet/opus/primary) remapped to DeepSeek models, authenticated by a **DeepSeek key written in plaintext into the global settings file**. For an operator whose Goal #1 is mastering Claude, this is a hard NEVER (§13).

✅ **Credit where due:** it *merges* rather than clobbers, and the comment says so — 「保留其它字段如 mcpServers」 (*preserves other fields such as mcpServers*). ⚠️ **But** `serde_json::from_str(&raw).unwrap_or_else(|_| json!({}))` means **an existing `settings.json` that fails to parse is silently replaced by an empty object and written back** — a total loss of your Claude Code configuration, from one stray comma. ⚠️ And the comment concedes `ANTHROPIC_MODEL_CONTEXT_WINDOW` is a **knowingly inert write** — 「Claude Code 无独立的上下文窗口字段（由模型名决定），此处按最佳努力注入自定义字段」.

### 11b. `codex_config.rs` — and the asymmetry that explains everything

Same directory, same author, same job for OpenAI Codex: writes `~/.codex/config.toml` (a `[model_providers.custom] name = "DeepSeek"` block, plus `model_reasoning_effort = "high"` and the privacy-positive `disable_response_storage = true`) and `~/.codex/auth.json` = `{"OPENAI_API_KEY": cfg.api_key}` — your DeepSeek key under OpenAI's variable name.

🔴 **But it is `fs::write(codex_config_path(), config_toml)` — a wholesale overwrite.** Any existing `~/.codex/config.toml` — your MCP servers, profiles, approval policy — is destroyed and replaced by a nine-line block.

⭐⭐⭐⭐ **Why one merges and one clobbers is the finding, and it is not carelessness.** `Cargo.toml` lists `serde` and `serde_json`; `grep -c "^toml"` over it returns **0**. There is **no TOML parser in the dependency tree**. Merging JSON was free because `serde_json` was already there for everything else; merging TOML would have cost a new dependency. ⇒ **the safety of your agent config depended on which serialization format your agent's authors chose.** This is **v265's rule at an independent, cross-author instance: a discipline travels freely wherever it is FREE and stops wherever the safe choice would COST something.**

### 11c. Corpus-recursive: it credits `cc-switch` twice

**Two in-source credits to `cc-switch` — corpus subject v73** (`farion1231/cc-switch`):

- `service/codex_config.rs:2` — 「参考 **cc-switch** 的 `to_codex_provider`」
- `config/store.rs:4` — 「借鉴 **cc-switch** 的 `settings.rs` 模式」

⇒ **Pattern #57 at a verified N=3 in one subject:** **v235** (DeepSeek Harness — host runtime, Cordis kernel, `session/event` stream, `dsh plugin` installer), **v239** (dsh-web-ui — the `dsh-market` probe the HEAD commit exists to satisfy), **v73** (cc-switch — credited by name in source, twice).

### 11d. The rest of the desktop app, fairly

✅ **Tauri capabilities are genuinely minimal**: `capabilities/default.json` grants only `["core:default"]` scoped to two windows, with an honest comment explaining why (custom commands go over IPC, so the webview needs no `fs`/`shell` permission). ⚠️ Worth naming, though: **the capability manifest describes what the webview may ask for, not what the app does** — all the config writing happens in Rust via `std::fs`, entirely outside Tauri's permission model. ⚠️ `tauri.conf.json` sets **`"csp": null`** and `withGlobalTauri: true` — two hardening defaults off, low practical risk for a local-only frontend. ✅ NSIS installer, `installMode: "currentUser"` (no admin elevation). ✅ The self-updater fetches a version manifest **over HTTPS** and spawns no process (`grep` for `Command|exec` in `update.rs`: nothing) — ⚠️ but from `https://www.xiaolin.help/update/dswDesktopVersion.json`, **a personal domain belonging to the contributor, not the repository owner**: the update channel of a product in MeteorNOX's repo is controlled by someone else. It also carries a **nine-expression emotion system** (`angry`, `exhausted`, `shy`, `stroking`, …), `auto-launch` + `winreg` autostart, and a `package-lock.json` **that main does not have**.

⚠️ **Main's README mentions none of this.** *(Extent: grep main's `README.md` for `Tauri`, `desktop`, `桌面`; the only `Windows` hits are PowerShell install lines.)* A visitor sees a release list whose two highest versions are `v1.0.0` and `v1.0.0+win` — neither being the thing the README documents, and one being a dead commit.

⚠️ **Claude's presence, stated precisely.** Across all 15 tracked files on **main**, `Claude`, `claude`, `Anthropic`, `anthropic`, `Opus`, `Sonnet`, `MCP` each return **zero** hits (`git grep` over the full HEAD tree; positive controls `DeepSeek` = 4 files, `dsh` = 7). Claude appears in this project **only on the desktop branch** — where it is the point.

---

## 12. Licence and assets

`LICENSE` is MIT, *"Copyright (c) 2026 MeteorNOX"*, added at `d3b37653` on **2026-08-22 13:49** — the **9th of 30 commits**, ~40 hours after the root.

⭐⭐ **But `package.json` declared `"license": "MIT"` from the root commit onward.** Checked at six commits across that window: at `306e660`, `ef9fdd3b`, `1559272c`, `e18577dd` and `973076b4` the field says MIT and `git cat-file -e <commit>:LICENSE` **fails**. **The licence was a metadata claim for 40 hours before it was a document** — and the auto-publish workflow went live at PR #6 on 08-21, so at least `0.2.0` and `0.2.2` were published under a claim whose text did not exist in the repository.

⭐ **This is v271's finding from the opposite direction, in an unrelated codebase.** There, `pyproject.toml` declared `Proprietary` while a `check-license.mjs` verified only that a filename existed. Here the field claimed MIT while the file did not exist. Same defect class: **the licence claim and the licence text are two separately-maintained surfaces, and nothing in either project compared them.**

⚠️ **Asset provenance is the unresolved question.** The repo ships anime-style artwork — `DSniang1.png`, `DSniang02.png`, `DSH2.png` (「DS娘」 is a *moe* personification of DeepSeek), `rua.gif` — and four mp3 clips the README labels 「小黄鸭」 and 「音效1」. **Extent: full-repository grep across all tracked files plus all 30 commit messages (`git log --format=%B`) for any attribution, credit, source or asset-licence statement — nothing found**, and a `strings` pass over the binaries surfaced no creator. MIT covers the code with certainty. Whether it can cover the artwork and audio depends on where they came from, which the repository does not say and I will not speculate about. For anyone forking or redistributing, **that is the open question** — and it is the same shape as everything in §3: *a licence you grant over content you may not own is a claim on someone else's contract.*

---

## 13. Corpus positioning — NO NEW MINT

**Corpus-first check, full vault extent** (24,116 `.md`/`.html`/`.sh` files; positive controls fire: `dsh-web-ui` 16 files, `deepseek-harness` 29, `Cordis` 18, `DSH` 27): `MeteorNOX` → **0** · `dsh-whale` → **0** · `余额` → **0** · `balance widget` → **0**. **The subject is new to the corpus.**

⚠️ **The near-collision, checked myself rather than trusted.** The v239 `dsh-web-ui` entry describes *"an animated whale pet"*, and its Verdict assigns it as the **6th instance of the observability sub-archetype's sub-flavour (b)**. Two whales in one ecosystem needed resolving. I cloned `zhu1090093659/dsh-web-ui`: `packages/` holds **`dsh-pet`** and **`dsh-miku-pet`**, and `grep -ri "MeteorNOX|dsh-whale-widget|DeepSeek-Balance-Whale"` over that clone returns **zero hits**. ⇒ **Different projects, different authors, different npm scopes.** The convergence is over-determined anyway — DeepSeek's own brand mark is a whale.

**Recorded instance-strengthenings (recorded, NOT self-promoted — a promotion is an audit act, the v232/v235/v237/v239 rule):**

1. ⭐⭐ **v237's generalised axis *"sanctioned in-process UI-LAYER PLUGIN on a host agent's own extension kernel"*: N=3 → N=4** (v236 dsh-TUI, v237 DSH-better-sidebar, v239 dsh-web-ui, v277) — independent author, non-port, different function, mounted on Cordis via first-party `dsh plugin`. **PROMOTION-ELIGIBLE since N=3; now over-satisfied.**
2. ⭐⭐ **Observability sub-archetype, sub-flavour (a) metering: N=6 → N=7** (joining v89, v109, v157, v158, v159, v165). ⚠️ **It is (a), not (b), on (b)'s own written definition** — (b) requires *"a reactive desktop-pet/avatar whose state tracks aggregate agent **run-state** as the primary display"*. This whale's primary display is **money**; its animations react to *user touch*, not agent state. It is a **meter wearing a pet**, and the sub-archetype's **first (a) metering instance mounted in-process inside the host agent's own web UI** rather than as a separate app, menu-bar item or TUI. *(Reading the definition before counting is the v262 discipline; it changed the answer.)*
3. ⭐⭐⭐ **Pattern #57 corpus-recursive at a verified N=3 in one subject** — **v235** (host runtime/Cordis/session-events/installer), **v239** (`dsh-market` probe → the HEAD commit), **v73** (`cc-switch`, credited by name twice in desktop-branch source).

**Mints DECLINED, ground stated:**

- **"Affective/character-vehicle cost meter"** (the pet-that-is-a-meter) — **DECLINED on presentation-not-capability**, the ground that decided v236 dsh-TUI, v216 Codex-Dream-Skin, v227 hermes-webui and v222 lobehub. Recorded as the sub-flavour observation above instead.
- **"Balance-delta-derived spend ledger"** (metering spend by differencing an account balance — no usage API, no token counting, no log parsing, genuinely unlike every existing (a) metering member) — **DECLINED on technique-not-capability**, the v211 PixelRAG discipline, and **not world-first** (balance-polling is not novel; with no network I could establish priority neither way). **Filed as a DEFERRED watch axis at N=1.**
- **"Agent-config rewriter that repoints Claude Code at a rival backend"** (the desktop branch) — **DECLINED**: `cc-switch` (**v73**) already occupies this class in the corpus, and this is an **openly-credited derivation** of it, not an independent instance. Recorded as **instance-strengthening of the v73 class, N=2, credited-port flavour** — the v208-OmniRoute handling exactly.
- ⚠️ **§28 anti-inflation was not used as a ground for any decline** (§44.5).

⇒ **Counts 46 / 12 UNCHANGED · §C-1 13 UNCHANGED · §C-2 38 UNCHANGED.**

**Two DEFERRED watch axes minted (N=1, recorded, not filed as §C rows):**
- *Balance-delta-derived spend ledger* — metering spend by differencing an account balance rather than counting tokens, with a disclosed error model.
- *The generating prompt as the maintained authoritative spec* — a repository whose design doc, onboarding doc and maintenance interface are one file explicitly written to be handed to an LLM. **Third consecutive corpus ship touching this vault's founding pattern from outside** (v268 `lat.md`, v269 `llm-wiki`, v277).

---

## 14. Method, and what I got wrong

**Fleet:** 12 dimensions × (read → adversarially refute) = **24 agents, 24 completed, 0 errors, ~3.08M subagent tokens, ~447 s.** All 24 launched, independently re-confirming the v259 finding that the compacted shim no longer blocks multi-agent work.

⭐ **The adversarial layer earned its cost.** It caught a reader placing the `size.json` method test at line 1906 (the true line is **1923**, which I then verified myself), caught another **fabricating a YAML block that appears in no commit**, caught line citations off by 10–30 lines, and caught a reader claiming `rua.gif` was undocumented when `README.md:35` lists it. ⭐⭐ **And its single most valuable catch was a REFUTATION that turned into this ship's best finding** — a reader asserted the spec's export-name lesson was satisfied; the refuter checked and found `const name = 'whale-balance-widget'`. **I then verified it myself** (§4). ⚠️ One reader also **conflated the main and desktop branches**, attributing desktop-only files to main — the §43.2 amplification hazard, caught by its refuter.

⚠️ **My own errors, all caught by re-measurement rather than re-reading** (§43.1 — the fourth consecutive ship where my error was generalising from where I chose to look):

1. **I over-rated the `size.json` write as compromise-grade** before reading `writeSizeConfig`. It is a strict whitelist with a fixed path list and an 8 KB cap — a **nuisance**. Corrected downward in §9.
2. **I first read the tag list as sloppy versioning.** The README's legacy-install section and the orphan commit's tree (a **zip file**) show a **deliberate re-baseline** — defensible, with a permanent cost. That reframing exonerates the author and is the better finding.
3. **I assumed v239's whale pet might be this project vendored.** Cloning dsh-web-ui and grepping refuted it. Unchecked, I would have claimed a dependency that does not exist.
4. **I nearly shipped (b) MODERATE on the main product alone**, before reading the desktop branch. `claude_config.rs` changes the rating and the pilot verdict entirely — the most goal-relevant code in the repository is on a branch the README never mentions. **D45: read the tree, not only the file the documentation names.**
5. **`git rev-list --format=… --no-commit-header` is unsupported by this sandbox's git** and failed loudly; I re-derived the version history with a per-commit `git show` loop. *(D39 holds — but check the flag exists.)* Separately, `git show "origin/For–WinDesktop:path"` **mangles the revision** because of the en dash; I resolved the branch to a SHA first.

---

*Prefix `(C)` — Claude-authored under operator direction. Shipped on `wiki/v277-whale-widget` off the v276 tip (`56f35cb`).*
