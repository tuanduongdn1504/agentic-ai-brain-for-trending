# (C) awesome-dsh-plugin — Deep Dive

**Wiki v240** · built 2026-08-18 · subject `awesome-dsh-plugin/awesome-dsh-plugin`
**Verification:** ✅ **SOURCE-CLONED** (full history, `git fetch --unshallow`) + a 16-agent research workflow + hand-verification of every load-bearing claim. First source-cloned subject of the DSH run (v236–v239 were all "NOT source-cloned").

---

## 1. What it is, in one paragraph

`awesome-dsh-plugin/awesome-dsh-plugin` is the community plugin catalogue for **DeepSeek Harness** (`dsh`) — corpus subject **v235**. Tagline, verbatim:

> A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

Licence **CC0-1.0**. `package.json` version `0.1.0`, homepage `https://awesome-dsh-plugin.com`. Page-stated **8.3k★ / 1.2k forks** (§37.4 — the GitHub API is mocked in this environment; treat as page-stated, **not** a Pattern #52 velocity claim).

Calling it "an awesome list" is the description on the tin and it is also the thing that misleads. What is actually in the repository is a **small package registry with a human editorial layer**: one YAML record per plugin, a compiler that renders those records into two 350 KB+ READMEs and a static site, a set of probes that re-verify the outside world, a weekly decay scan, six CI workflows, and a **published machine-readable registry API** that third-party software consumes at runtime.

---

## 2. Provenance — git-verified, not API-derived

This is the first subject in the run where the corpus can measure the project's own tempo **without** the mocked GitHub API, because a clone carries authoritative commit metadata:

| Fact | Value | Source |
|---|---|---|
| First commit | **2026-08-13 21:55:28 +0800** — `fkysly`, `init: awesome-dsh-plugin` | `git log --reverse` |
| Latest commit | 2026-08-18 19:38 +0800 | `git log -1` |
| Age | **~5 days** | derived |
| Commits | **1,662** | `git rev-list --count HEAD` |
| Unique author emails | **853** | `git log --pretty=%ae \| sort -u` |
| Commits/day | 25 / 381 / 403 / 416 / 239 / 198 (Aug 13→18) | `git log` |

⭐ **A 5-day-old repository with 1,662 commits and 853 distinct contributor emails.** Those numbers are hand-derived from the clone and are as trustworthy as git itself.

**Maintainership is far more concentrated than the contributor count suggests** — also git-verified:

- `fkysly` — **243 commits**, and **86 of the ~93 commits touching `scripts/` + `.github/`**
- `github-actions[bot]` — **113 commits** (probes committing refreshed data back)
- then a long tail: PerryLink 23, ahmed isam 17, John Tsui 15, zoahdev 8, LeemanCheung 8, JinHyuk Sung 8 … most of the 853 have exactly one

So: **one volunteer wrote essentially all of the machinery**, and 850-odd people submitted entries. `scripts/maint-rebase.sh` exists for exactly this shape — a maintainer rebasing a large queue (a code comment references **~150 open PRs**).

**Affiliation.** The README's Disclaimer states plainly: *"This project is not affiliated with DeepSeek."* No Anthropic connection anywhere. `fkysly` is a bare handle. → **(a) FAIL** under routine §41 (no declared Anthropic affiliation, no registered vendor-direct axis; no name/locale inference permitted).

---

## 3. The architecture — a compiled document

### 3.1 One record per plugin

`data/plugins/<owner>__<repo>.yml`, five fields:

```yaml
url: https://github.com/01Virex/dsh-status-rotator
name: 01Virex/dsh-status-rotator
category: ui
description:
  en: Replaces the "Deep diving..." turn-status label with rotating meme-worthy phrases, with typewriter and gradient effects.
  zh: 把回合状态那句 "Deep diving..." 替换成更有梗的自定义文案，按阶段轮换，支持打字机与流动渐变。
```

Optional `tarball:` (and rarely `npm:`). Field frequency across the whole set, hand-counted: `name` 1390, `description` 1390, `category` 1390, `url` 1365, `tarball` 21, `npm` 4.

⭐ **Bilingual completeness is 1390/1390** — every single record carries both `en:` and `zh:` (verified by per-file loop; zero misses). The schema treats `zh` as optional and `generate-readme.mjs` prints an "awaiting translation" report, but right now the set is complete.

### 3.2 The README is generated, and the numbers reconcile exactly

`scripts/generate-readme.mjs` replaces two marked regions in each README:

```js
toc:     ['<!-- BEGIN TOC -->',     '<!-- END TOC -->'],
plugins: ['<!-- BEGIN PLUGINS -->', '<!-- END PLUGINS -->'],
```

Hand-verified count reconciliation:

- `data/plugins/*.yml` → **1390**
- `README.md` lines matching `^- \[` → **1393**; minus **3** TOC navigation links (lines 42, 63, 64) → **1390**
- `README.zh.md` → **1393** → likewise **1390**
- 20 category headings summing to **1390** (UI Enhancements 185, Tools & Capabilities 174, Development & Runtime 118, Sessions & Messages 86, Usage & Billing 83, Workflow & Automation 82, Notifications & Integrations 80, Memory 79, Vision & Multimodal 60, Themes & Appearance 57, Just for Fun 57, Security & Permissions 55, Skills 48, Plugin Markets & Managers 47, Git & Code Review 38, Models & Providers 35, Browser & Web 33, Voice & Audio 26, Remote & Mobile 25, Docs & Rendering 22)

⭐ **Exact agreement, in both languages, across 1,390 entries.** Set the contrast: **v239's subject stated 11 plugins, listed 12, and shipped 14.** This one cannot disagree with itself, because both renders come from one record — a *prevention* guarantee, strictly stronger than v239's blob-hash translation *detection*.

And the drift check is **enforced, not merely available**. `generate-readme.mjs` runs a whole-file set check:

```js
// Set check: the README as a whole (markers or not) must parse to exactly
// the URLs data/plugins declares — no smuggled or missing entries anywhere.
```

`smuggled` (in README, no data file) and `missing` (in data, not in README) both `console.error` and set `stale`, then `process.exit(1)`.

### 3.3 ⭐⭐⭐ It checks its *prose* against its code — the gap v239 could not close

The single most vault-relevant twelve lines in the subject, verbatim from `generate-readme.mjs`:

```js
// contributing.md lists the valid category values for contributors to copy.
// It drifted once already — `usage` and `vision` were added to the taxonomy
// and the docs kept advertising the old twelve — so the list is checked here
// rather than trusted to stay in step by hand.
{
  const doc = fs.readFileSync('contributing.md', 'utf8')
  const want = CAT_IDS.map((c) => `\`${c}\``).join(' ')
  if (!doc.includes(want)) {
    console.error(`contributing.md: the category list is out of date — it should read\n  ${want}`)
    process.exit(1)
  }
}
```

A **documentation-content** consistency check — born from a real drift incident, failing the build when a prose enumeration disagrees with the code's source of truth. The v239 ship's conclusion was that `verify-docs.mjs` *"checks structure, not content equivalence → prose numbers are exactly what it cannot catch."* **This is the missing half.**

---

## 4. The verification pipeline — and honestly, its limits

### 4.1 What runs

Six workflows, **all `permissions: contents: read`** except `decay-scan.yml` (`issues: write`, to file its report):

| Workflow | Trigger | Does |
|---|---|---|
| `pr-check.yml` | `pull_request` (fork-safe, **no token**) | `npm ci`, `npx awesome-lint`, `build-site.mjs` smoke build |
| `pr-gate.yml` | `workflow_run` after PR check | `check-submission.mjs` — needs the API, so runs in base context |
| `pr-guard.yml` | schedule | PR hygiene sweep (`pull-requests: read`) |
| `regate.yml` | schedule | re-checks gated submissions |
| `build-site.yml` | schedule / push | 4 probes → `build-site.mjs` → Pages |
| `decay-scan.yml` | schedule (weekly) | `scan-decay.mjs` → one tracking issue |

### 4.2 ⭐⭐ The `pr-gate.yml` header is the best CI-security artifact of the run

Verbatim:

> SECURITY: a token is in scope here, so nothing from the pull request is ever executed. The checkout stays on the base repo's default branch — trusted code, trusted lockfile — and the only thing taken from the PR is the content of `data/plugins/*.yml`, extracted into a scratch directory and read as data. Checking out `refs/pull/N/merge` and running `npm ci` there would hand the token to fork-supplied install scripts, which is the **`pull_request_target` footgun this workflow exists to avoid**.

A textbook-correct mitigation of a known GitHub Actions privilege-escalation class, written down at the site of the decision. Directly pilotable.

The same file records an incident in a comment: paginating every open PR per fire *"is what exhausted the installation rate limit on 2026-08-18."*

### 4.3 What the gate actually checks

`check-submission.mjs` verifies **structure and metadata**: a `dsh.bundle` manifest in the target repo's `package.json` (root or a `packages/`·`plugins/`·`apps/` subpackage; `dsh.client` alone fails), **repo age ≥ 1 day**, **commit count ≥ 10**, archived status. Plus `awesome-lint` and locale parity.

### 4.4 ⚠️ The honest limit — and the project states it first

The README's boast is *"if a description claims '46 tools', someone counts them."* There is **no mechanism** behind that sentence. It is a human promise — and `contributing.md` says so itself, before anyone else can:

> A green CI run is the **precondition**, not the decision. CI verifies the shape of a submission — manifest, repo age, formatting, that the READMEs regenerate. **It cannot tell whether a plugin does what its entry says**, whether the category fits, or whether an entry duplicates one already on the list. A maintainer reads the target repository before merging.

The adversarial verifier's verdict on "this is a verification pipeline" was **PARTLY** — automation covers structure; functional accuracy is human. That is not a dishonesty finding. It is a **disclosure** finding: the project's own documentation is more precise than its marketing line. (#83 — careless-claim-with-honest-documentation, the mild pole.)

Likewise, `probe-tarballs.mjs` does **not** extract or scan tarballs — it issues a ranged `GET bytes=0-0` to confirm the URL still resolves. No security scanning of any listed artifact happens anywhere. The README says as much: *"Being on this list is not a security review."*

---

## 5. ⭐⭐ The governing philosophy: automate the evidence, never the irreversible decision

Three independent scripts, one consistent rule.

**`scan-decay.mjs`** — 4 signals (`gone` 404, `archived`, `dormant` = no push in **`DORMANT_MONTHS = 6`**, `unbundled` = `dsh.bundle` gone), weekly, into one tracking issue updated in place:

> Flags — never removes. […] removal stays a human decision because it is irreversible and a scan can be wrong — an outage, a rename, a rate-limit blip. Anything inconclusive (API errors) is skipped, not flagged: **a decay report must only ever contain evidence, not doubt.**

**`check-bleed.mjs`** — detects one entry's description bleeding into another's, born from incident **#1348**:

> a PR whose stated purpose was refreshing the dsh-notifier entry also appended dsh-notifier's new sentence to `AKS1st/dsh-cyber-particle`, an unrelated plugin. **It happened twice**, and every existing check passed both times — the YAML was valid, the READMEs regenerated, lint was clean. Nothing looked at whether a PR touched entries it had no business touching.

Mechanism: a shared run of ≥ **`RUN = 40`** description characters is the fingerprint; same-owner pairs skipped; **"reported, not enforced"** because similar plugins are legitimately described similarly. The threshold is *empirically calibrated*: *"At 40, a full pass over ~1170 entries surfaced five pairs, all genuine similarity."*

**`build-site.mjs`** — a publish-time plausibility floor, from incident **#1673** dated **today**:

> On 2026-08-18 `plugins.json` went out with `stars: null` for all 1,362 entries (#1673) because `probe-stars.mjs` was handed an exhausted API quota and a cold cache at the same time, wrote `{}`, and nothing between it and the deploy asked whether that was plausible. […] keeping yesterday's stars live beats publishing nulls, because a stale number degrades gracefully and a null does not.

→ `STARS_MIN_COVERAGE = 0.66`.

⭐ **This is a coherent doctrine: machines establish evidence; humans make decisions that cannot be undone.** And it is the sharpest available contrast with the immediately-prior ship — **v239's `pr-review.mjs` auto-closed issue #532, a substantive bug report, for template non-compliance.** One ship apart: **v239 automated the decision and got it wrong; v240 automated the evidence and left the decision to a person.**

Every non-obvious constant in this codebase carries a comment naming the incident that motivated it and the measurement that calibrated it. `locales.mjs` even records an SEO finding: dropping the brand suffix from sub-pages, because when every page claimed the brand *"these pages entered the same results and lost — measured at a third of the click-through their position should earn."*

---

## 6. ⭐⭐⭐ Why it is a registry, not a document

`scripts/build-site.mjs:675`:

```js
// Public registry API: /plugins.json — deterministic; consumed by the find
```

It writes `docs/plugins.json`, plus `docs/readmes.json`, `docs/count.json` (the README's own count badge), `feed.xml`, `sitemap.xml`, per-locale JSON-LD, and per-plugin detail pages. Two locales are registered in `site/locales.mjs` — `en` and `zh`, and only those two.

Two independent runtime consumers, both confirmed by fetching them:

1. **`dsh-market/dsh-market`** — *"The plugin market inside DeepSeek Harness. Open Settings → Plugin Market → browse, search, one-click install."* MIT, page-stated 967★/62 forks, and a **separate organisation**. Its README, verbatim: *"Live from awesome-dsh-plugin.com/plugins.json — curated entries, npm mapping, and star counts refreshed daily by CI — with a bundled snapshot as offline fallback"* and *"This repo is the market app, not the catalog."*
2. **`awesome-dsh-plugin/dsh-find-plugin`** — *"Find DSH plugins inside the agent — live GitHub `dsh-plugin` topic search, star-ranked."* MIT, page-stated 55★. It registers a **`find_dsh_plugin` tool into the agent**, so the model itself searches for plugins and hands back a ready-to-run `dsh plugin add` command. ⚠️ Nuance worth keeping straight: its primary index is the live GitHub topic; the curated list supplies **better descriptions** over the top.

The org owns exactly **2 repositories** (this list + the finder). `dsh-market` is somebody else's.

⭐ So the shape is: **a curated editorial list that publishes a machine registry, consumed at runtime by a third-party in-harness storefront and by an agent-callable discovery tool.** The README is one rendering; the site is another; `plugins.json` is the interface.

**Corpus note.** v239's `community-plugins` panel earned a #68 form-factor sub-variant described as *"an awesome-list compiled into a host-app panel — static, index-only, **no runtime registry**."* v240 is the runtime registry that panel lacked.

---

## 7. ⭐⭐⭐ The three drift defects — and the rule they teach

A project this disciplined is the right place to look for what discipline *cannot* reach. All three found by hand.

### 7.1 A dead link on line 5 of both READMEs

```
English | [中文](README.zh.md) | [日本語](README.ja.md)
```

`README.ja.md` **does not exist** — verified three ways: absent from disk, absent from `git ls-files`, and **no `ja` entry in `site/locales.mjs`** (only `en`, `zh`). Zero `.ja.` files anywhere in the repo.

Why the machinery misses it: `generate-readme.mjs` line 2 — *"Everything outside the marker blocks (badges, banner, …)"* is not regenerated. The language switcher is hand-written preamble. ⭐ **1,390 generated lines are perfect; the one hand-written navigation line is broken.**

### 7.2 One CRLF record in 1,390

`data/plugins/paicat1__dsh-screenshot.yml` is the only file with `\r\n` line endings (confirmed with `od -c`: `v i s i o n \r \n`). There is no `.gitattributes`. js-yaml tolerates it, so it renders correctly and nothing complains. Genuinely trivial in impact — its interest is only that it is the *byte-level* variance the semantic validator was never asked about.

### 7.3 ⭐⭐⭐ A merged contribution that silently never appeared

`data/plugins/zmm863-commits__dsh-paperclip` — **no `.yml` extension.** The record itself is flawless: url, name, `category: ui`, and both `en` and `zh` descriptions.

`scripts/lib/entries.mjs:69`:

```js
if (!f.endsWith('.yml')) continue
```

Skipped silently, no warning. Consequences, each hand-verified:

- `README.md` → **0** occurrences of `dsh-paperclip`; `README.zh.md` → **0**
- `data/screenshots.json`, `data/added-dates.json`, `data/stars.json` → **0**
- therefore absent from the site, from `plugins.json`, and so from **dsh-market's storefront** and **`find_dsh_plugin`'s results**
- merged as **PR #1192 on 2026-08-17** by `zmm863-commits`, *"Add dsh-paperclip plugin"*

A contributor's plugin was accepted and has never existed anywhere downstream. And note *why* no check catches it: every check compares the README against the parsed data — **two views of one source the file is not in.** There is even a filename-must-match-the-url validator at `entries.mjs:133` (`expected ${want}.yml`) — but it only inspects entries that were *read*, and this one is never read. **The validator that would have caught it sits downstream of the glob that excludes it.**

⭐ **The generalisable rule — the D-level lesson of this ship:**

> A consistency check between two views of one source cannot see what is missing from the source. Any generate-from-data pipeline needs a separate **inventory** check that enumerates the input directory by a *different* rule than the parser uses.

The vault's condition exactly: an index↔content check between `CLAUDE.md` and `_state/03c` would never notice a chapter file absent from the index.

---

## 8. ⭐⭐ A contested claim caught propagating — again, one ship later

The list's editorial policy says a reviewer checks *"Does the code do what the entry claims — including any numbers or API names in the description."* Its verified entry for the **v239 subject** reads:

> Plugin and skin collection for the DSH Web UI: task board, Git graph, right-side panel, remote mobile UI, pet, **live token stats**, and a skin center.

**v239's ship recorded "live token stats" as a GitHub tagline claim absent from every README and every published package.** I re-checked the live source myself rather than lean on the prior ship: the current `zhu1090093659/dsh-web-ui` README (33,162 bytes, fetched raw) contains **zero** occurrences of `token` in any case, and zero of `usage`. Its single 令牌 hit is on line 81, in the **mobile-pairing** section — the pairing token v239 documented, not usage statistics.

⭐ So the phantom feature has been copied from the plugin's own tagline into a registry that feeds `plugins.json`, a storefront, and an agent's tool results. **Structurally the same event as v239's, one ship later and pointing the other way:** v239 republished upstream's retracted benchmark into its npm description; v240 republishes v239's unsubstantiated feature into its registry API. A claim moving downstream through a live dependency graph faster than anyone re-checks it.

⚠️ Fair caveats: the feature may exist in code or a sub-package I did not exhaust (v239's ship checked "every README and every published package"; I checked the root README of the aggregate). And the mechanism is banal, not malicious — the description was almost certainly copied from the subject's own tagline, which is precisely what the policy warns against.

**Also worth recording:** all three corpus DSH subjects were listed on **2026-08-14** — day two of this list's life, *before* the corpus shipped any of them (v236 on 08-17, v237 and v239 on 08-18). The list beat the wiki to all three.

| Corpus subject | Listed | The list's own one-liner |
|---|---|---|
| v236 `ccch1mneyyy/dsh-TUI` | 2026-08-14 | "Claude Code-style full-screen terminal UI: pixel-whale header, live status line, and streaming thought expansion." |
| v237 `omdsh-dev/DSH-better-sidebar` | 2026-08-14 | "Full sidebar workbench with file rendering and editing, terminal, Git, and subagents; third-party plugins can register new tabs." |
| v239 `zhu1090093659/dsh-web-ui` | 2026-08-14 | "…pet, **live token stats**, and a skin center." |
| v238 `xiaobright/dsh-anchored-standard` | — | **not listed** (two same-named third-party presets are: `ruby1304__dsh-preset-anchored-standard`, `Jungod1121__dsh-anchored-standard`) |

---

## 9. The vendored agent skills — a corpus link, but weaker than it looks

`skills-lock.json` pins two upstream skills by content hash:

```json
"ui-ux-pro-max":          { "source": "nextlevelbuilder/ui-ux-pro-max-skill", "computedHash": "523b8063…" },
"web-design-guidelines":  { "source": "vercel-labs/agent-skills",             "computedHash": "f3bc47f8…" }
```

Both sources are **corpus subjects**: `nextlevelbuilder/ui-ux-pro-max-skill` = **v85**, `vercel-labs/agent-skills` = **v51**. The content is vendored into `.agents/skills/` (ui-ux-pro-max ships a large CSV/JSON data corpus across ~20 UI stacks) and re-exposed via **committed symlinks**:

```
.claude/skills/ui-ux-pro-max        -> ../../.agents/skills/ui-ux-pro-max
.claude/skills/web-design-guidelines -> ../../.agents/skills/web-design-guidelines
```

— the **geti v213** committed-cross-harness-symlink shape, and a `.claude/` directory is a direct Claude Code hook.

⚠️ **But the adversarial check returned "PARTIAL REFUTE — decoration, not load-bearing," and it is right.** Nothing in the repo verifies `computedHash`, refreshes the skills, or consumes them in any script or workflow; there is **no `AGENTS.md` and no `CLAUDE.md`** at root. What the repo *does* ship is `design-mocks/{a-minimal,b-warm,c-dark}.html` and a hand-built `site/template.html`. The consistent reading is **one-time design-time use, pinned by hash as a record** — not architecture. Intent is nowhere stated, so that reading stays inferential.

### ⚠️ Pattern #16 — a revival that does *not* qualify, and I am recording it as such

The corpus retired **Pattern #16 "Skill Dependency Locking"** at the v27 audit. Its file states the terms:

> **Originally:** v15 multica (`skills-lock.json` with Anthropic + Vercel skill imports).
> **Retirement rationale:** multica-specific architecture. No follow-on framework adopted version-locked skill dependencies.
> **Revive if:** **2+ frameworks adopt version-locked skill dependency manifests.**

Same filename, same purpose, hash-locked, and **Vercel skills in both instances** — 225 wikis later. That is a striking recurrence. It is also **not a revival**, on two independent grounds:

1. **This is not a framework.** multica was a platform whose architecture locked skill dependencies. This is a curated list using two design skills as build-time tooling.
2. **The manifest is not load-bearing** — nothing enforces or consumes it (§9 above).

→ Recorded as a **non-qualifying data point**, flagged to the overdue audit, **not** self-revived. Reviving a retired pattern is an audit act (the v232 rule), and on the evidence the audit should decline too.

---

## 10. Risk read

**Positives**, all source-verified:

- **CC0-1.0** — the list data is public domain; reuse, including commercially, is unencumbered. (The *plugins* carry their own licences.)
- **Least-privilege CI** — every workflow `contents: read`; only `decay-scan` adds `issues: write`. No publish job, no secrets beyond `GITHUB_TOKEN`.
- **No lifecycle scripts.** Two devDependencies only: `js-yaml ^5.3.0`, `marked ^18.0.9` — both current (npm's `latest` for js-yaml **is** 5.3.0, with `v4-legacy: 4.3.1`; I checked the registry after wrongly doubting it).
- **A genuinely good privacy posture.** Self-hosted webfonts; the privacy page names **Cloudflare Web Analytics** explicitly, and states cookie-less, no fingerprinting, no ad networks, no social widgets, no tag managers, and that the published data *"contains nothing about visitors."*
- **Provenance discipline on downloads** — a `tarball:` must be an `https` `.tgz` on GitHub's own release hosting, *"the list won't hand users a download link it can't vouch for"*; screenshots must be GitHub-hosted because third-party image hosts are *"rejected by the build for user-privacy reasons."*
- **An unusually blunt top-of-page warning** — *"Installing a plugin runs third-party code on your machine with your own permissions… Tool approvals don't sandbox plugin code. Being on this list is not a security review."*
- **Real semver expertise** in `contributing.md`: a precise explanation of why a peer range like `>=0.0.1-rc.1 <0.2.0` **silently excludes** `0.1.0-rc.6` under node-semver, with the correct `||`-branch fix. Directly relevant to the corpus — v236 pins 21 `@deepseek-ai/*` peers at `^0.1.0-rc.6`, v239 at `rc.7`.

**Concerns:**

- 🔴 **Single point of failure.** One volunteer wrote all the machinery of a 5-day-old repository that a 967★ storefront and an agent tool now read **live**. Bus factor 1, on infrastructure.
- ⚠️ **A listing reads as endorsement no matter what the disclaimer says.** 1,390 install-me entries, no security scanning of any of them, ~49% with promotional screenshots (`data/screenshots.json`, 675 entries). The text is honest; the psychology of a curated storefront is not something a disclaimer fixes.
- ⚠️ **A lockfile finding no agent surfaced.** `package-lock.json` resolves 2 of 3 packages from **`registry.npmmirror.com`** (`js-yaml`, `argparse`) and only `marked` from `registry.npmjs.org`, and `npm ci` runs in **four** workflows. Integrity hashes are present, so content substitution would fail the install — the exposure is **availability and install-traffic visibility, not integrity**. Almost certainly an artefact of a maintainer installing behind the China mirror and committing the result.
- ⚠️ **The one place the no-ranking principle bends** is above the fold: the list's first recommendation is a specific storefront (`dsh-market`, a different org, which depends on this list's API), and its second is the org's own `dsh-find-plugin` — in a document that says *"we are not judges of plugin quality."* Both links are inline and visible; neither is disclosed as first-party. Not misconduct — but the recommendation that entrenches the list as the ecosystem's canonical registry is the recommendation it makes loudest.
- ⚠️ **`fkysly` and the 853 handles are unverified identities.** Predominantly QQ/163/foxmail/gmail addresses. No claims inferred from that beyond what is written.

---

## 11. What the corpus should take

The take is not the list. It is the **machinery around the list**, which is the fifth-plus consecutive DSH ship to hand the vault tooling for its own documented disease (v234 staleness → v235 doc gates → v236 boundary CI → v237 pack-and-mount → v239 `verify-docs.mjs` → **v240 compile-from-data + prose-vs-code + decay-with-evidence + bleed detection**).

The vault's `CLAUDE.md` is a hand-maintained index over `_state/` chapters. Its documented failures are exactly this class: `03c-projects-v61-v183.md` labelled `-v183` while holding entries through **v240**; the v78-era "Current state" snapshot; the stale C22–C27 rows whose retire pass has been deferred for ~50 wikis *because retirement is irreversible and judgement-laden.*

v240 answers that last objection directly: **scan weekly, report evidence never doubt, skip the inconclusive, update one tracking issue in place, and leave removal to a human.**

---

## 12. Verification log

✅ **Source-cloned** (`--depth 50` then `--unshallow`); all structural facts derived from the working tree and `git log`, not the mocked API.
✅ 16-agent workflow: **0 errors**, ~1.70M subagent tokens, 355 tool uses, **382 s**. (v239's ran 16 agents / 411 s; v238's failed entirely at ~207.2K vs a 200K ceiling. The shim compaction remains the fix.)
✅ Collision grep run **before** analysis: `awesome-dsh-plugin` already had **7 vault hits** — v237's Verdict names this repo as *"Ecosystem-formation data-point, **not a subject**"* (§13 of the Verdict handles that).
✅ Every count in this document hand-derived: 1390/1393/3, 1390 en + 1390 zh, 20 categories summing to 1390, 1391 files, 1662 commits, 853 emails, 243/113 top committers.

**Six errors caught — four of them mine:**

1. ⚠️ **My own suspicion was wrong** — I doubted an agent's "js-yaml 5.3.0 is latest," expecting 4.x. The npm registry says `latest` → **5.3.0**. Corrected; the agent was right.
2. ⚠️ **An agent claim I declined to repeat** — that js-yaml's `load()` uses an unrestricted schema constructing arbitrary objects. `load()` has been the safe-by-default entry point since v4, I could not confirm v5's schema from the source or the README, and a security claim has to be right. Recorded as **UNVERIFIED**; what *is* verified is that the parsed object is strictly validated immediately (`entries.mjs:120–161`).
3. ⚠️ **An agent's arithmetic** — "1390 documented vs 1391 data files = a 2-entry discrepancy." It is **1** file, and README↔data agree **exactly** at 1390. The orphan is real (§7.3) and became the ship's best finding; the framing was wrong.
4. ⚠️ **My own over-excitement, reversed by the verifier** — I initially read `skills-lock.json` as reviving retired Pattern #16. The adversarial check found nothing consumes or verifies it, and the retire criterion says *frameworks*. **Revival declined** (§9).
5. ⚠️ **My own risk framing corrected** — the README's "someone counts them" is a human promise with no mechanism, but `contributing.md` **discloses that itself**, so this is a disclosure finding, not a dishonesty finding.
6. ⚠️ **The mocked GitHub API (§37.4)** — star/fork figures are page-stated only and carry **no** Pattern #52 claim. The velocity numbers in §2 are git-derived and stand on their own.

**Sources hand-fetched or hand-read:** the full clone (README.md, README.zh.md, contributing.md, all 6 workflows, all 14 scripts, `lib/entries.mjs`, `site/locales.mjs`, `site/privacy.en.html`, `package.json`, `package-lock.json`, `skills-lock.json`, `data/*`); rendered pages for `dsh-find-plugin`, the org's repository list, `dsh-market/dsh-market`; `registry.npmjs.org/js-yaml`; raw `dsh-web-ui/README.md`.
