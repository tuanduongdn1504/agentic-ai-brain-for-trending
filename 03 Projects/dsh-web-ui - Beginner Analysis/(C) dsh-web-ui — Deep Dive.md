# (C) dsh-web-ui — Deep Dive

**Wiki v239 · 2026-08-18 · subject:** [`zhu1090093659/dsh-web-ui`](https://github.com/zhu1090093659/dsh-web-ui)
**Verdict:** GOAL-ALIGNED INCLUDE 3/4 · **NO MINT** · counts 46/11 UNCHANGED
**Provenance discipline:** every fact below is labelled. ⚠️ **NOT source-cloned** — this analysis is built from raw file fetches (`raw.githubusercontent.com`), the npm registry (`registry.npmjs.org`), and rendered GitHub pages. Star/fork/commit counts are **page-stated** per §37.4 (this environment mocks the GitHub API). Two figures circulating in the research pass — **1,477 files** and **66 contributors** — came *only* from the mocked API and are **discarded as UNVERIFIED**; the 70-handle contributor block below is hand-verified from `README.en.md` instead.

---

## 1. What it is, in one paragraph

`dsh-web-ui` is a **13-package pnpm monorepo of community plugins plus 11 skins for the official web GUI of DeepSeek Harness (DSH)** — the agent runtime the vault shipped as **v235**. Its own tagline: 「DeepSeek Harness（DSH）Web GUI 的插件与皮肤全家桶 · 一切皆开发，一切皆插件」 — *"a whole-family bucket of plugins and skins for the DSH Web GUI · everything is development, everything is a plugin."* You install the lot with one row:

```
dsh plugin --profile web add @linxin666/dsh-web-ui-all
```

It adds a kanban **task board with host-side cron scheduling**, a **git graph**, a **QR-paired mobile remote**, an **SSH/SFTP operations console that also hands the agent remote-execution tools**, an **image-understanding tool**, an animated **whale pet**, a **skin centre** with 11 themes, an in-app **community-plugin index**, a **skill explorer**, a settings surface, and a **two-phase agent preset** called 梁神模式 (*Liangshen Mode*). Licence **Apache-2.0** at the root, with BSD-3-Clause, MIT and CC BY-NC-SA-4.0 mixed in (§8).

**Scale:** ~4.4k★ / 269 forks / 846 commits (**page-stated**). Repo created ~2026-08-12; **21 npm versions published between 2026-08-13 and 2026-08-18** (registry-verified) — roughly six days old at the time of this wiki. **70 named contributors.**

**Author:** GitHub `zhu1090093659`, display name **"Solitude"** — no bio, no company, no location, no declared affiliation. Commits carry a QQ-mail address. npm packages publish under the scope **`@linxin666`** with maintainer e-mail `linxin@linux.do`. **Not DeepSeek. Not Anthropic** (§41; Pattern #19 19a). See §7 for the unresolved handle question.

---

## 2. The host, and why the surface matters

DSH's own documented entry point is the **web UI**: v235's wiki recorded `npx @deepseek-ai/dsh web` → `http://127.0.0.1:3080`, and noted that although a `packages/terminal` exists, *"the documented entry point is `dsh web`"* (**SOURCE-VERIFIED** against the DSH README).

That places this subject differently from its two predecessors in the corpus:

| Ship | What it extends | Which surface |
|---|---|---|
| **v236 dsh-TUI** | replaced the front door with a Claude-Code-style TUI | the *secondary* surface |
| **v237 DSH-better-sidebar** | added one right-hand panel, negotiating for the slot | a *panel* on the primary surface |
| **v239 dsh-web-ui** | adds 13 plugins + 11 skins across four extension-point kinds | the host's **primary** surface, broadly |

DSH is moving fast underneath all of it. Latest release **v0.1.0-rc.7 (2026-08-17)** — **SOURCE-VERIFIED** — whose notes read *"Enable plugins to register their own settings cards"* and *"Refine the Cordis dynamic plugin panel."* **The host is racing to sanction what the community is already doing.** The rc pins across four consecutive corpus ships are monotonic:

> **v235 → rc.5 · v236 → rc.6 · v237 → rc.6 · v239 → rc.7** (`@deepseek-ai/dsh-system-prompt: ^0.1.0-rc.7`, registry-verified)

---

## 3. The four-way corpus recursion (Pattern #57)

This subject cites or depends on **four distinct prior corpus subjects**. That is the widest #57 fan-in I can find in the corpus; the prior high-water mark was two (OmniRoute v208: a port-parent plus a bundled engine). Flagged to the audit as a record claim rather than asserted absolutely.

| Prior subject | Relation | Evidence | Confidence |
|---|---|---|---|
| **v235 `deepseek-ai/deepseek-harness`** | the host it mounts into | `@deepseek-ai/*` devDeps pinned `^0.1.0-rc.7`; installs via the host's own `dsh plugin --profile web add` | SOURCE-VERIFIED (registry) |
| **v237 `omdsh-dev/DSH-better-sidebar`** | **exact-pinned npm runtime dependency** | `dsh-web-ui-all` depends on `dsh-better-sidebar: 0.13.0` (exact, no caret); README credits *"外部集成插件 … MIT（omdsh-dev）"* | SOURCE-VERIFIED (registry) |
| **v238 `xiaobright/dsh-anchored-standard`** | **vendored code with attribution** | `dsh-liangshen` names it *"Original experiment"*; `tool-bootstrap.mjs` credited to it under MIT via `NOTICE` | SOURCE-VERIFIED |
| **v216 `Fei-Away/Codex-Dream-Skin`** | **cited design model** | root `package.json`: 「…皮肤集合 + Gallery 预览页（**仿 Codex-Dream-Skin / DreamSkin.cc**）」 = *"imitating Codex-Dream-Skin / DreamSkin.cc"* | SOURCE-VERIFIED |

Plus **lateral siblinghood with v236 dsh-TUI** — unrelated plugins in one host, no mutual dependency (the relation shape v237 established).

And a real, filed consequence of the v237 dependency: **issue #532**, *「与独立安装的 dsh-better-sidebar 共存时插件树加载失败」* — *"the plugin tree fails to load when coexisting with a separately-installed dsh-better-sidebar."* See §9 for what happened to that report.

> **A correction the corpus owes itself.** v238's NO-MINT rested partly on ground (5), *"a weak anchor in an already-crowded class,"* naming external rivals. The corpus already held stronger evidence than that: **v236's own entry records `presets/liangshen/` plus `verify:minimal-preset-tools` and `verify:liangshen-bootstrap`** in dsh-TUI's 11-script verify suite — shipped one day before v238 and never connected to it. The Liangshen convention is crowded *inside the corpus's own subjects*. v238's ruling was right; its evidence was stronger than stated.

---

## 4. 梁神模式 (Liangshen Mode) — the mechanism, and a regex

`dsh-liangshen` (v0.2.0, Apache-2.0, one runtime dependency) is a two-phase agent preset.

**Phase 1** exposes only the host's builtin Minimal pair — persistent **`bash`** plus **`str_replace_editor`** — keeps only the `deployment:persona` prompt section, clears runtime context, and passes the user's own messages with no workspace directives, snapshots, or skill directory.

**Promotion to phase 2** fires on any of: the first persisted `tool/call` *and* a reasoning block that passes the **anchor gate**; `maxBootstrapSteps` reached; or a first response containing no tool calls.

**The anchor gate is a literal regex on the model's chain-of-thought** (SOURCE-VERIFIED). A reasoning block counts as "minimal-like" **iff** it matches `/\bwe\b/gi` **and** has zero matches of `/\blet me\b/gi`. Any other combination — including *"we"* together with *"let me"* — fails. The entire "trajectory anchoring" thesis reduces, in code, to: *does the model say "we" and not "let me."*

**Phase 2 is not a bigger catalog.** It collapses to a **single `run_code` tool** reaching the full registry via generated SDK calls, with all prompt sections restored. Both phases minimise the visible tool surface — the second by making tools *code* rather than schema entries.

⚠️ **`PTC mode` is the host's name, not the subject's.** DSH rc.7's release notes read *"Rename the English `Code mode` preset to `PTC mode`"* (SOURCE-VERIFIED). Both phases are compositions of **first-party** presets.

Other config: `bootstrapMaxTokens` (documented as a community-found window at **1024** against DSH's 256k default, which the docs claim has a **0% hit rate**), `deferredSources`/`deferredGraceSteps`, `instructionHint`, `phase1FirstCallInstruction`, `promoteAfterFirstResponse`, `promotedPresentation: code`. Windows uses `presets/liangshen/custom-bash.mjs`, a Git Bash bridge. Requires DSH ≥ rc.5.

---

## 5. ⭐ The claim that travelled: 98/99

`dsh-liangshen` states — in its README **and in its npm registry description** — 「Windows 原生环境实测（DeepSeek V4 Pro、max、V4.1b 题面）：**98 / 99，均值 98.5**」, framed as measured and 「证明不是抽卡」 (*"proving it's not a lucky draw"*), against 「Standard / PTC 只有 91/92 分，Minimal 达到 99/96」.

Upstream — the project it credits — the same pair has a documented history:

| Upstream artefact | Date | What it establishes | Confidence |
|---|---|---|---|
| **issue #60** *"Docs: attribute the 98/99 runs to the legacy pwsh/read → 25-tool configuration"* | 2026-08-16, opened by **MolecularFullerene**, now **closed** | those runs used Windows **`pwsh` + `read`**, then the full **25-tool Standard catalog** — **not** the two-tool Minimal pair the docs later attributed them to | SOURCE-VERIFIED (fetched independently) |
| **issue #51** | third-party replication, 11 rounds × 3 OSes × 4 presets | **Ability 85–90; 98/99 not reproduced** | SOURCE-VERIFIED |
| **issue #65** | the upstream's own randomised block design | anchoring separated **9/9**, but the ability advantage was **+3.3, 95% CI [−2.6, +9.3]** — **not significant** | SOURCE-VERIFIED |
| **`FAREWELL.md`** | 2026-08-17 | upstream shut down; evaluation cost rose ~¥2 → ~¥12 per round | SOURCE-VERIFIED (v238) |

**The timeline matters, and it exonerates intent.** The 98/99 claim entered `dsh-liangshen`'s README at commit **`2a1ff28` on 2026-08-14** — **two days before** issue #60 was filed. The author could not have known.

**What remains is a maintenance failure, not a fabrication.** Two days on, the number is unchanged, it has been carried into the **npm registry description**, and **no dsh-web-ui issue or note acknowledges either the retraction or the two failed replications.** Whether v239's figure is a genuine independent re-derivation or an inherited one **cannot be resolved from the available sources** — and **neither version reports a sample size or a confidence interval.**

> **⇒ Do not cite 98/99.** The style effect in this family is reasonably established (9/9 separation); the *quality* effect is not (CI crosses zero, two replications disagree). What the corpus has captured here is rarer than either: **a contested empirical claim propagating through a real dependency graph, observed from both ends in two consecutive ships.**

---

## 6. ⭐⭐ The part worth stealing: machinery for invariants a build can't see

This is where the project is genuinely better than its star count would predict, and it is the fifth consecutive ship to hand the vault machinery for its own problems (v234 staleness-tracking → v235 doc-verification gates → v236 CI-enforced architectural boundary → v237 pack-and-mount rendering gate → **v239 documentation integrity**).

**`scripts/verify-docs.mjs`** enforces, per package:
- a **README triplet** — `README.md` + `README.zh.md` + `README.i18n.yaml`;
- **translation pairing via git blob hashes**, so a translation cannot silently drift from its original;
- **markdown link validation**;
- heading-level structure;
- **no scaffold placeholders**;
- with `--list` and `--write` modes for repair.

Alongside it: **`runtime-deps-check.mjs`** (scans committed `lib/` for bare imports that resolve only against devDependencies — a gate *born from issue #70*, a real `ERR_MODULE_NOT_FOUND` boot crash in skin-center); **`sync-shared.mjs --check`** (8 shared files mirrored into consumers as committed copies with generated headers, with drift detection); **`aggregate.mjs --check`** (the aggregate's plugin rows must match the children); a **7-field `skin.json` contract** (`id`, `name`, `author`, `tagline`, `accent`, `bodyAttr`, `package`) hard-failed by the gallery build; and a **CI emoji ban** rejecting four Unicode ranges.

CI is minimal-privilege and hand-verified: **`permissions: contents: read`**, **no npm publish job, no secrets referenced**, 10 check steps (`typecheck`, `gallery:check`, `skin-center:check`, `community:check`, `build`, `test`, `test:scripts`, `runtime-deps:check`, `aggregate:check`, `docs:check`) plus a second job that **packs the plugin, mounts it into a real DSH instance, and headless-renders it under Playwright** — the same gate class v237 introduced.

### And the irony that makes it land

**Everything the build can see is checked. Everything only a human can check has already drifted:**

| Drift | Evidence |
|---|---|
| **Three different plugin counts** | README says the aggregate installs *"all eleven child plugins"*; the README lists **12**; the published aggregate depends on **13 `@linxin666` packages + `dsh-better-sidebar` = 14** |
| **Stale root version** | root `package.json` `version: 0.1.1` vs every published package and release tag at **0.2.0** |
| **A tagline advertising a feature that does not exist** | the GitHub About tagline ends *"…pet, **live token stats**, and skin center"* — yet `README.en.md` contains **no mention** of token stats or TPS, and **no such package appears** in the aggregate's 14 dependencies (a research pass found archive/commit references to a removed `dsh-live-stats`; the *removal* is DOC-STATED, the *absence* is verified) |
| **A template narrower than the repo** | the PR template's affected-package checkboxes list only `dsh-task-board` and `dsh-git-graph` + "other", for a 13-package monorepo |

`verify-docs.mjs` checks **structure**, not content equivalence — headings, fences, table widths, list kinds. Prose numbers are exactly what it cannot catch. **That is the vault's own condition**, precisely: C22–C27 stale rows, a `_state/03c` filename label reading `-v183` while holding entries through v239, a "Current state" block frozen at a v78-era snapshot, and v238's README linking a `HANDOFF.md` that does not exist.

---

## 7. Author identity, and one unresolved handle

**(a) FAILS** under routine §41 — no declared Anthropic affiliation, no registered vendor-direct source. `zhu1090093659` / "Solitude" shows no bio, company, or location. Building DeepSeek tooling is **not** an affiliation with DeepSeek.

An **ecosystem-portfolio** shape is visible (Pattern #19 19a): pinned repos `dsh-web-ui` (4.4k★), **`deepseek-pp`** — a DeepSeek browser extension with MCP tools, memory, skills (~1.6k★) — and **`spec_driven_develop`** (~969★), all page-stated.

**The unresolved question, stated as facts only:** repository commits are authored under `zhu1090093659` with a QQ-mail address; the npm packages publish under scope **`@linxin666`**, maintainer e-mail `linxin@linux.do` (a well-known Chinese developer forum); a GitHub account named `linxin666` exists but shows only unrelated older Android/HTML repositories and no `dsh-*` work. **The relationship between the GitHub author and the npm publishing identity is not established by any source I could reach.** The npm `repository` field does point correctly at `zhu1090093659/dsh-web-ui`, so this is a naming question, not a redirection one. **No inference about any real individual is drawn.**

**Who or what 梁神 is** — the preset's namesake — I could not determine. The package documents no person under that name; it credits `xiaobright`. Left open rather than guessed.

### Not a solo build — 70 contributors in ~6 days

`README.en.md` carries an auto-generated `<!-- CONTRIBUTORS:START -->` block listing **70 handles** (hand-verified, no API). Two are notable:

- **`whitelonng`** — author of `dsh-plugin-describe-image`, the project `dsh-tool-describe-image` was ported from. **The upstream author is a contributor here**: the port is collaborative, not extractive.
- **`Chimney`** — v236's author is `ccch1mneyyy`, display name "Chimney". ⚠️ **Whether these are the same account is UNVERIFIED and I did not resolve it.** Recorded because, if true, it is a person-level link between two corpus subjects; not relied on.

---

## 8. Security: sharply split

### Sound (SOURCE-VERIFIED)

- **Mobile pairing done properly** — a **one-time 32-hex / 16-byte random token with a 10-minute expiry**, consumed on first `accept()` (subsequent attempts return `used`), plus revocable device sessions and live device status. Binding is **inherited from DSH's own webServer** (loopback by default; LAN addresses enter the picture only when the host itself is bound `0.0.0.0`). The Service Worker caches the static shell only — never API responses or secrets.
  > **This is the first subject in the recent gateway-adjacent run to get the auth model right.** It does **not** exhibit the broken-authentication triad — `0.0.0.0` + wildcard CORS + fail-open auth — that v231 CoreOfPotato and v232 gemini-web2api both shipped. Minor gap: no per-request CSRF token on `/api/pair` (token travels in the JSON body; `SameSite=Lax` mitigates).
- **Port forwarding is loopback-only** — `127.0.0.1`, documented and implemented.
- **No telemetry.** Greps for telemetry/analytics/sentry/beacon found no external egress.
- **Supply-chain hygiene that mirrors the corpus's best exemplar.** The aggregate pins all 14 dependencies **exactly** (`0.2.0`, no caret). `pnpm-workspace.yaml` carries an explicit **`allowBuilds` lifecycle allowlist** (`cloudflared`, `cpu-features`, `esbuild`, `node-pty`, `ssh2`) and a **`minimumReleaseAgeExclude`** list. That is **the pi v228 hardening playbook** — pinning, a lifecycle allowlist, minimum release age — independently adopted; a second corpus instance.
- **Scheduling fails closed** (§10).

### Not sound (SOURCE-VERIFIED)

**`dsh-ssh` registers six tools into the agent** — `ssh_list`, `ssh_exec`, `ssh_upload`, `ssh_download`, `ssh_tunnel`, `ssh_cluster` — via `ctx.tools.register(...)`, and *"GUI and Agent share the same host config."* `ssh_exec` accepts an **arbitrary command string**. The plugin ships:

- **no command allowlist**
- **no approval gate or confirmation** — `routes.ts` posts straight to `engine.exec()`; `tools.execute()` calls engine methods directly
- **no audit log**
- **no output redaction** — remote output returns verbatim
- **no read-only or query-only mode**
- **plaintext secrets** — `store.ts`: `writeFileSync(tmp, JSON.stringify(file, null, 2) + '\n', { encoding: 'utf8', mode: 0o600 })`, holding SSH **passwords and key passphrases**

Plus a documented replay hazard: reconnect *"may replay non-idempotent commands."*

> **The corpus already knows the better answer.** **v212 tabularis** — a database GUI with a first-party MCP server — solved this exact secret class with the **OS keychain**, and gated its agent surface with **read-only mode + approval gates + a pre-flight EXPLAIN that fails closed on stacked statements**. Same problem, one ship earlier in the corpus, solved properly.
>
> **And it is disclosed.** Both READMEs state it verbatim: 「SSH 密码与 passphrase 口令以明文保存在 `~/.dsh/dsh-ssh.json`（权限 0600）」. **Careless design, honest documentation** — Pattern #83.

### Watch

The recommended **one-line aggregate install transitively pulls `cloudflared ^0.7.3`**, whose manifest defines `postinstall: "node scripts/postinstall.mjs && node lib/cloudflared.js bin install"` — it **downloads a Cloudflare tunnel binary at install time**, from a single-maintainer package. The subject's own packages define no consumer-facing lifecycle scripts (`prepare` runs `tsdown` for the publisher, not the registry consumer), and `cloudflared` sits *explicitly* in `allowBuilds` — a deliberate, disclosed choice rather than an accident. Know it is there.

### Licence mixing blocks commercial wholesale use

Apache-2.0 (11 packages) + **BSD-3-Clause** (`community-plugins`, `skill-explorer`) + MIT (vendored `tool-bootstrap.mjs`; the `dsh-better-sidebar` dependency) + **CC BY-NC-SA 4.0, non-commercial only** (the `maid-atelier` skin, disclosed in `THIRD_PARTY_NOTICES.md`). Two skins are also named **`minecraft`** and **`miku`** — third-party IP. **A commercial user cannot install the aggregate wholesale.**

---

## 9. ⭐⭐ Governance for a repository that AI writes

The sharpest original finding of this ship, hand-verified from `.github/pull_request_template.md`.

The template carries a section headed **「AI 编码披露（AI Coding Disclosure）」**, marked ⚠️ *Required*, with three mutually exclusive checkboxes:

> - 「完全 AI 编码：全部编程改动由 AI 产出，并由贡献者接受 / 审查。」 — *fully AI-coded: all programming changes produced by AI, accepted/reviewed by the contributor*
> - 「部分 AI 辅助：AI 帮助编写或修改了部分编程改动。」 — *partially AI-assisted*
> - 「未使用 AI 编码辅助。」 — *no AI coding assistance*

followed by two free-text fields:

> 「使用的 AI 模型：（示例：DeepSeek、GPT-5、**Claude Sonnet 4**）」
> 「使用的编码 Agent 工具：（示例：DeepSeek Harness、Codex、**Claude Code**、Cursor）」

The header also mandates Conventional Commits and 「禁止 emoji」.

**This is the corpus's first subject that treats *"which agent wrote this?"* as structured, required provenance metadata in its contribution process** — and Claude Code appears in a rival ecosystem's PR template as a first-class expected contributor tool. It is enforced: **`scripts/pr-review.mjs`** audits external PRs with `REJECT`/`FAIL`/`WARN`/`PASS`/`SKIP`/`ERROR` verdicts, 10K line and file-size limits, worktree build verification, emoji checks, forbidden-path checks, and **missing-template-field checks**. The norm has spread to reporters, too: issue **#499** ends 「大部分为 AI 的测试复现与代码推测，仅供维护者参考」 — *"most of the testing reproduction and code analysis is AI-generated, for maintainer reference only."*

**A note on the emoji ban.** In a repository whose PRs are declared *"fully AI-coded,"* a CI gate that strips emoji is doing more than style enforcement — it suppresses one of the most reliable AI-authorship tells. The repo simultaneously **requires** AI-authorship disclosure and **erases** its most visible signature. Whether or not that is intentional, it is a real tension, and it connects to Pattern #88 (anti-slop curation; cf. hallmark v204's 57 enumerated slop gates).

### The cost of the same rigidity

**Issue #532** — the substantive `dsh-better-sidebar` coexistence bug, with reproduction steps and root-cause analysis — was **auto-closed as `not_planned` for template non-compliance.** The process that produces the good disclosure also suppressed a real bug report about a corpus-subject integration. ⚠️ That report's own root-cause claim (a loader-entry-id mismatch, `web-ui-better-sidebar` vs `better-sidebar`) is **not independently verified**; if wrong it misdirects. Recorded two-sided.

---

## 10. The task board: fail-closed, and not unattended

**SOURCE-VERIFIED** from the package description and `host-runner.ts`:

- **Host-authoritative**, *"mounted without DSH source changes."*
- **Every run creates a separate DSH session** and applies a **pinned workspace, agent preset, and permission** *before* the task prompt is sent.
- **Execution is fail-closed** — a missing workspace, a missing preset, or a **rejected permission** stops execution **before the prompt reaches the agent.**
- **5-field cron** (`*`, `*/n`, ranges, comma lists, Sunday `0/7`) in the host's local timezone.
- **Missed occurrences during host downtime or sleep are skipped, never queued for catch-up.**
- **Runs never overlap** — a task already running skips its due occurrence and rolls to the next match. Sequential.
- Prompts are queued with **`mode: 'queue'`** into the normal interaction flow — **not** unattended auto-approval.

> One honest gap: whether the host's own tool-approval flow then triggers for each tool call is not settled by the plugin's code. The plugin gates *the run*; it does not claim to gate every tool inside it.

**The running theme across five ships:** v233 ClawWork — *evaluation* fails closed. v234 agentic-local-brain — *ingestion* fails soft. v238 dsh-anchored-standard — fail-soft at runtime, fail-fast at config. **v239 — *scheduling* fails closed.** Four independent projects converging on failure-mode discipline as the thing worth being explicit about.

---

## 11. Ecosystem position

**#2 by page-stated stars** among independent DSH plugin projects:

| Project | ★ (page-stated) | In corpus? |
|---|---|---|
| `yjh051108/dsh-routing-suite` | ~5.8k | **no** — named at v238 as the crowded-class rival |
| **`zhu1090093659/dsh-web-ui`** | **~4.4k** | **v239 (this ship)** |
| `xiaobright/dsh-anchored-standard` | ~3.5k | v238 |
| `ccch1mneyyy/dsh-TUI` | ~1.7k | v236 |
| `omdsh-dev/DSH-better-sidebar` | lower | v237 |

Two things follow. The corpus has now shipped four of the five largest community projects in a six-day-old plugin ecosystem — and **the largest one, `dsh-routing-suite`, remains un-shipped.** ⚠️ Directory counts for the ecosystem's total size vary wildly by source and the `dsh-plugin` topic count is self-applied; treated as an unreliable upper bound, not merged into a single figure.

---

## 12. What is *not* claimed

- **NOT #52** (viral velocity) — stars/forks are page-stated per §37.4. 21 npm versions in five days is fast, but velocity is not verifiable in this environment.
- **NOT world-first** on any of its four candidate axes (see the Verdict doc, §Prior art).
- **NOT a new top-level pattern** (max remains #85).
- **NOT first-party DeepSeek.**
- **NOT source-cloned** — raw fetches + registry only.
- **NOT an N=3 of the Multi-Vendor Coding-Agent Orchestration Platform row** (Paseo v150 + ai-maestro v163). That row requires **heterogeneous third-party agents as the orchestration units**; this task board is **single-host, DSH-only**. Read verbatim before ruling.
- **NOT a §C#27 CodePilot v161 instance** — that row wraps a CLI agent *from outside*; these mount in-process.
- **NOT #18 B1-MCP** — it registers tools into the host; it ships no MCP server.
- **1,477 files** and **66 contributors** — GitHub-API-derived only; **discarded as UNVERIFIED** under §37.4.

---

*Companion docs: `(C) dsh-web-ui — Verdict.md` (criteria, pattern ruling, mint alternatives) · `(C) dsh-web-ui — Pilot Methods Menu.md` (what to actually do).*
