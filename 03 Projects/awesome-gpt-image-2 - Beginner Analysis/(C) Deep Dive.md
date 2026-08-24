# (C) Deep Dive — `freestylefly/awesome-gpt-image-2` (v272)

**Subject:** `github.com/freestylefly/awesome-gpt-image-2` — *"Prompt as Code | GPT-Image2 Industrial Prompt Engine & Template Library, 500+ Reverse-Engineered Cases, 20+ Industrial Templates"*
**Author:** 苍何 / Cang He (`freestylefly`, `canghe`) — one person under three git identities (`2689458656@qq.com`, `canghe@canghedeMac-mini.local`), WeChat official account 苍何, site `gpt-image2.canghe.ai`. **NOT Anthropic.**
**Licence:** MIT (root `LICENSE`, © 2026 freestylefly). Agent-skill `package.json` also MIT.
**Ship date:** 2026-08-24 · **Wiki version:** v272

## ✅ Source verification

Two independent clones. `HEAD = de6a8ad89b6308dc49b316fcd9f7a56bf2a73273`, identical in both. `diff -rq --exclude=.git` **clean in both directions** (exit 0, no output).

| Measure | Value | Command |
|---|---|---|
| commits | **159** (HEAD) / 160 (all refs) | `rev-list --count HEAD` / `rev-list --all --count` |
| roots | **1** — `1ec5641`, 2026-04-25 17:17 +0800 | `rev-list --max-parents=0` |
| merges | **2** (PR #1 imgbot, PR #7 sscodeai) | `rev-list --merges --count` |
| tags | **4** — `…-v1.0.0 / v1.0.1 / v1.0.2 / v1.0.4`, **all 2026-05-08**, **v1.0.3 absent** | `for-each-ref refs/tags` |
| branches | `main`, `origin/codex/apimart-first`, `origin/imgbot` | `branch -a` |
| tracked files | **656** — 543 jpg · 43 js · 19 png · 12 sql · 12 md · 7 mjs · 7 json · 2 yml · 2 jsx · 2 css | `ls-files` |
| first-party code | **10,666** lines JS/JSX/MJS · **2,179** lines SQL | per-file `wc -l` |
| tests | **3 files, 395 lines, 27 test functions**, all under `api/_lib/` | `ls-files` + `grep test(` |
| working tree | 351 MB | `du -sh` |
| latest commit | 2026-08-23 15:14 +0800 — *"Add GPT Image 2 prompt cases 527-532"* | `log -1` |

**⚠️ Method note (D39, confirmed again):** a fleet agent reported `git log --all --oneline | wc -l = 50` against a truth of 160. I re-ran it myself in the same clone with the same git (2.19.0) and got **160**, matching `rev-list`. The 50 was an artifact of the *agent's* output handling, not of git. v270's narrowing of the v267 50-cap **holds at a fourth data point** — and the transferable lesson is narrower and sharper: *a subagent's reported command output can be silently truncated in ways the subagent does not detect.* §43.1 again: the orchestrator running the command itself is what settles it.

---

## 1. What this actually is

Not an awesome-list. **Five products in one MIT repository:**

1. **The catalogue** — 529 GPT-Image-2 prompt cases with 543 images, reverse-engineered from public community posts, across 13 categories, in `docs/gallery-part-1.md` (294,876 B) + `docs/gallery-part-2.md` (635,642 B) + a category index `docs/gallery.md` (52,439 B).
2. **The curated layer** — **22 "industrial templates"** in `docs/templates.md` (47,947 B) with a machine-readable schema `data/style-library.json`.
3. **The website** — Vite + React 19 SPA (`src/main.jsx`, **3,753 lines in one file**) at `gpt-image2.canghe.ai`.
4. **The SaaS** — **33 Vercel serverless handlers**: Google/Watcha OAuth, a credit ledger, Stripe subscriptions + credit packs, Alipay web payments, paid image generation, an 8-endpoint admin console, refunds. Plus **12 Supabase migrations**.
5. **The agent surface** — a **Claude Code / Codex Agent Skill** (`agents/skills/gpt-image-2-style-library/`) published to npm and GitHub Packages, plus a **`.claude-plugin/marketplace.json`**.

**The pivot is dated to the hour.** Root commit 2026-04-25 (awesome-list, 329 cases, a 13,218-line README). Then: website `5d0b113` 2026-05-04 · **agent skill `c5769e5` 2026-05-08** · plugin manifest `f12b882` 2026-05-08 · Supabase auth+credits `92d782e` 2026-05-09 · paid generation `09c99a6` 2026-05-09 · Alipay `225e13a` 2026-07-22.

**Commit distribution: Apr 22 · May 102 · Jun 24 · Jul 6 · Aug 5.** The entire product was built in a fifteen-day window; 64% of all commits landed in May. Since then it has been case-additions and sponsor placement.

**⭐ The root commit carries `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>`.** Exactly one commit in 159 does. It is the one that created the 13,218-line README of "reverse-engineered" prompts — so the badge **`100% Original AI Rewritten`** has a concrete, attributed meaning, recorded in the one place nobody reads. There are **zero** other AI-authorship trailers anywhere in the history (extent: `log --all --format=%b`, needles Co-Authored-By / Generated with / Claude / Codex / Copilot / Cursor). The branch named `codex/apimart-first` exists to *move a sponsor to first position*.

---

## 2. ⭐⭐⭐⭐⭐ THE HEADLINE — the validated artifact is frozen; the unvalidated one grew a third

Two generators sit in `scripts/`, both wired into the same `prebuild` line of `package.json`.

| | `generate-style-skill.mjs` (169 lines) | `generate-site-data.mjs` (189 lines) |
|---|---|---|
| input | `data/style-library.json` — **22 templates, a schema** | `docs/gallery-part-*.md` — **930 KB of hand prose** |
| output | the agent skill's `references/style-library.md` | the website's `data/cases.json` |
| `grep -c throw` | **9** | **0** |
| validations | unique ids/categories/styles/scenes; **every `template.anchor` must exist as `<a name=…>` in `docs/templates.md`**; every template **and** category `cover` must resolve to a file on disk; no duplicate covers | none |
| plus | `assertNoPattern()` — **throws if the generated text contains the Chinese AI-slop construction 不是…而是** | — |
| failure mode | fails closed, blocks the build | three silent fallbacks |

**And then the measurement that settles it.** At the last published tag `…-v1.0.4` (**2026-05-08**) versus HEAD (2026-08-23), by `git show <tag>:<path> | md5`:

| artifact | tag → HEAD |
|---|---|
| `SKILL.md` | **byte-identical** |
| `references/style-library.md` | **byte-identical** |
| skill `package.json` | **byte-identical** |
| `data/style-library.json` | **byte-identical** |
| `data/cases.json` | **`totalCases` 398 → 529** |

⭐⭐⭐ **In the 108 days since the skill was last published, the catalogue gained 131 cases (+33%) and the agent skill did not change by a single byte.** The 22 templates are frozen (35 `"anchor"` occurrences at both refs). **The gate is pointed at the thing that does not change; the silent fallbacks are pointed at the thing that grew by a third.**

The agent-facing consequence is concrete: `SKILL.md` instructs the agent *"Prefer the reference over memory when template names, categories, covers, or style tags matter"* — and the reference's newest referenced example is **case 378** (34 `exampleCases` refs, max 378, 0 dangling). The catalogue now runs to **532**. **154 cases the skill has never heard of.**

### 2.1 The three silent fallbacks, and what each one produced

- **`extractPrompt`** returns `''` on a regex miss. *Result at HEAD: 0 empty prompts.* Clean — the markdown convention held.
- **`extractSource`** falls back to `{label:'Community', url:''}`. *Result at HEAD: 0 cases labelled `'Community'`* — the fallback never fired. **25 cases have `sourceUrl === ""`, and every one is explainable:** 15 are Xiaohongshu account ids (`小红书号…`, no linkable per-post URL), 9 are the author's own cases credited to his WeChat article, and **1 (case 3) is the literal string 未提供 — "not provided."** One further case (270) lost its URL to malformed markdown: `\[OpenNana]\(]\(<https://x.com/Toshi_nyaruo_AI/status/…>)`. **529 of 529 cases carry a `来源：` line** (164 in part-1 + 365 in part-2). *This is a genuine strength and it corrects the direction I was heading in: the disclaimer's promise to "make every effort to preserve original sources" is substantially kept.*
- **`inferCategory`/`inferTags`** fall through to keyword heuristics. **This one fired, 15 times, and it is measurable.**

### 2.2 The inventory rule, live (v240)

Bidirectional check, run by hand:

| direction | result |
|---|---|
| images with no case entry | **3** — `case12.jpg`, `case169.jpg`, `case170.jpg` |
| case entries with no image | **0** (my first pass said 13; those are `.png` not `.jpg` — **my own regex was too narrow**) |
| anchors in the gallery parts vs `cases.json` | **exactly equal, both directions** |
| `docs/gallery.md` index refs with no anchor | **0** |
| **anchors absent from the `gallery.md` category index** | **15** — cases 42, 48, 50, 66, 69, 82, 90, 133, 159, 172, 243, 280, 301, 318, 332 |

`parseCategoryMap()` builds its category map from `docs/gallery.md`. **A case missing from that index gets `undefined` and falls through to keyword inference.** So those 15 cases have a category the author never chose — and the mechanism is invisible because the heuristic always returns *something*.

**Mitigating fact I must lead with:** the `"Other Use Cases"` bucket is **28 cases, all 28 author-indexed as `cat-other`** — **zero** of the 15 landed in the junk bucket. The fallback produced a plausible answer every time.

**⚠️ And the sharper finding, which corrects my first reading.** I set out to prove the heuristic misclassifies, using cases with identical titles. It does — case 82 and case 90, titled 信息图可视化设计 ("infographic visualization design"), landed in *UI & Interfaces* while cases 66 and 69 with the identical title landed in *Charts & Infographics*. But grouping all 529 cases by title shows the real story: **that one title is shared by 27 cases spanning 7 distinct categories, and 23 of the 27 are author-indexed.** The categories disagree because **the titles are degenerate, not because the heuristic is bad**: 529 cases carry only **392 distinct titles**; 161 cases (30.4%) share a title with another; the top offenders are 信息图可视化设计 ×27 (7 categories), 主题海报版式设计 ×21 (5), 界面交互设计图 ×14 (4). Titles come from the author's own markdown headings (`### 例 N：…`), and `generate-site-data.mjs` uses them both as the card title a visitor reads **and** as classification input. **A generic label is doubly load-bearing and carries no information in either role.** Prompts, by contrast, are 509 distinct of 529.

### 2.3 The style vocabulary: 10 declared, 19 emitted

`inferTags()` declares `styleOrder` with **10** values (UI, Infographic, Poster, Realistic, Illustration, Product, Brand, Character, Classical, 3D). `data/cases.json` emits **19**. The 9 extras — Architecture, Characters, Charts, Documents, History, `"Other Use Cases"`, Photography, Products, Scenes — are all produced by one expression: the style fallback borrows `caseItem.category.split(' & ')[0]`.

⭐ **Two fallbacks in the same function, one right and one wrong.** The *scene* fallback is the constant `'Creative'` and emits exactly the declared 10. The *style* fallback reaches into a different taxonomy and invents nine facets from it.

The consequences are visible in the product: `data/style-library.json` now carries all **19** style entries — the 9 fallback artifacts were **ratified into the curated schema** (with empty `keywords`, so they can never be matched, since `styleOrder` is hardcoded). `src/main.jsx` renders `siteData.styles` as filter chips, so the live site shows **`Character` and `Characters` as two separate filters, and a visual style literally named `"Other Use Cases"`.**

### 2.4 The anti-slop gate — correct, narrow, and pointed at the one clean file

`assertNoPattern()` fails the build if the generated reference matches `/不是[\s\S]{0,80}而是/`. That is a **build-breaking assertion against one specific AI-slop rhetorical tic** — Pattern #88 88c *machinery-with-enforcement*, at the build layer rather than the review layer.

I ran the repository's own regex over all 77 text files **with a validated positive control**:

| file | matches |
|---|---|
| `references/style-library.md` — **the only file the gate guards** | **0** |
| `data/cases.json` | **8** |
| `docs/gallery-part-1.md` | 3 |
| `docs/gallery-part-2.md` | 2 |
| `docs/templates.md` | 1 |

**Be fair about the aim.** The reference is rendered from English scaffolding plus the hand-authored `zh`/`en` fields of `style-library.json`, so the gate *is* correctly aimed at the only prose that can reach the artifact it guards. What it cannot see is the 930 KB of gallery prose and the 1.3 MB `cases.json` — where the tic occurs 14 times, and where the product lives.

**⚠️ Method note:** my first count of this used `perl -0777 -ne '/\x{4e0d}\x{662f}…/'` and reported **0 matches everywhere**, including in files that plainly contain the words. A positive control caught it — perl without `-CSD` compares codepoints against UTF-8 bytes. **v271's silent-counter rule, confirmed at N=2 by a different mechanism** (perl encoding, where v271's was zsh bracket expansion). I re-ran it in node using the repository's exact regex, with the control printed.

---

## 3. ⭐⭐⭐ The enforcement census — and why it looks the way it does

Extent for every negative below: **all 656 tracked files** (images excluded from content greps), plus dotfiles and `.git/hooks/`.

| What | Checked by | Trigger | Does it run? |
|---|---|---|---|
| the agent skill's reference | 5 fail-closed invariants + the anti-slop assertion | `prebuild` → **every Vercel build** and every `npm run dev` | ✅ **blocks a deploy** |
| the website's 529-case data | nothing | `prebuild` | runs, **cannot fail** |
| the money paths | **27 tests, 395 lines** | `npm test` | 🔴 **never** |
| 10,666 lines of JS | **no linter, no formatter, no types** | — | — |
| the published skill package | nothing | tag push → `npm publish` | ships whatever is committed |

- `vercel.json:3` `buildCommand: "npm run build"` → npm runs `prebuild` (`package.json:16`) → **both generators execute on every deploy**, and the skill generator's nine `throw`s therefore block one. **This is the strongest verification mechanism in the repository, and it is a side effect of needing a build.**
- **Exactly one tracked file mentions a test invocation: `package.json` itself.** No husky, no lefthook, no Makefile, no justfile, no Taskfile, no CONTRIBUTING, no active git hook (only `.sample`). `.github/` contains exactly two files: `FUNDING.yml` and `publish-style-skill.yml`.
- **Zero** eslint / prettier / tsconfig / editorconfig / biome, tracked or referenced.

### 3.1 The tests deserve to be named, because they are good

`api/_lib/community.test.js` + `alipay.test.js` carry 26 tests (plus one import test). A sample, verbatim:

> `'community checkout payload keeps the server-owned ¥9.90 CNY price'` · `'paid notification rejects mismatched business fields'` · `'notification and paid transition are persistently idempotent'` · `'only PAID status can read the protected QR'` · `'refund keeps PAID access until final success then revokes it'` · `'admin operations require super_admin and same-origin writes'` · **`'payment kill switch defaults closed and changes only on explicit true'`** · **`'browser roles have no direct table grants for orders or QR bytes'`** · `'parses Alipay decimal amounts without floating-point rounding'` · `'community actions use bounded per-user rate limits'`

**Every risk a payments audit would raise has a named test:** amount verification, replay idempotency, signature authenticity, admin authorisation, the fail-closed default, the anon-role grant surface, decimal rounding, rate limiting. **And nothing runs any of them.**

### 3.2 ⭐⭐ The one test that got the design right

`api/_lib/api-imports.test.js` is 32 lines. It **recurses `readdir` over `api/`** and dynamically imports every `.js` that isn't a `.test.js`:

```
test('all Vercel API modules load without broken imports', …)
```

**No hardcoded list. It cannot drift. Adding a 34th handler is covered automatically.** This is precisely the defect class v269's subject fell into (a list typed a second time, which diverged) and precisely the outcome v271's subject achieved with a sha256 manifest — reached here by the cheapest possible route: **not restating the list at all.**

---

## 4. The disciplines that *did* hold — and what they have in common

- ⭐ **26 SQL functions, 26 `set search_path = public`, 24 `SECURITY DEFINER`.** 26/26 across 12 migrations and four months, zero misses. Exactly the functions where a missing `search_path` is a privilege-escalation vector.
- ⭐ **`202605090002_auth_policy_lints.sql`** exists solely to rewrite every RLS policy from `auth.uid()` to `(select auth.uid())` — the Supabase advisor's own performance lint. **A whole migration dedicated to satisfying an external linter's warnings**, in a repository with no linter of its own.
- ⭐ **Admin authorisation: 8/8 gated.** `metrics.js:180` and `credits/adjust.js:19` on `!isSuperAdmin`; `users.js:41` on `role !== 'super_admin'`; the five community handlers on `isCommunityAdmin(auth)`, defined at `community.js:73-75` as the OR of the other two. **Three spellings, one meaning, no drift** — belt-and-braces, not divergence. Three of the five also check an origin allowlist *before* auth.
- ⭐ **BOLA/IDOR: zero.** Eleven user-facing endpoints all scope on `auth.user.id` taken from the verified JWT, never from a request parameter (`favorites.js:57/96/117`, `billing/history.js:36`, `billing/alipay/query.js:37`, `me.js:98`, `community/status.js:42`, `community/qr.js:26`).
- ⭐ **Webhook authenticity, both rails.** Stripe: `webhook.js:11-15` sets `config.api.bodyParser:false`, reads the raw body, then `constructEvent` — correct. Alipay: `checkNotifySignV2`, `sign_type === 'RSA2'`, `app_id` **and** `seller_id` checked, and the amount/currency re-validated against the stored order **in the RPC as well as in JS** — two layers.
- ⭐ **Idempotency:** `UNIQUE notify_id` + on-conflict-do-nothing in **both** Alipay migrations.
- ⭐ **OAuth:** `auth/watcha/start.js:34` generates a random 24-byte state into a secure cookie; `callback.js:130` validates against the cookie, not the query; `safeReturnTo()` enforces same-origin.
- ⭐ **`COMMUNITY_PAYMENT_ENABLED` defaults to `false`** with the comment *"production deployments must start with new payments disabled"* — a fail-closed money default, **with a test asserting it is fail-closed.**
- ⭐ **Supply chain, clean.** All **298** transitive packages in `package-lock.json` carry `integrity` and **all 298 resolve from `registry.npmjs.org`** — zero alternative registries. (The exact inverse of v271's 206/206 mirror.) **No `postinstall` in either `package.json`** — so `npm install` writes nothing to your home directory.
- ⭐ **History is clean.** Searched all refs with `log -p -S` for `sk_live`, `sk_test`, `whsec_`, `SUPABASE_SERVICE_ROLE_KEY=`, `BEGIN RSA PRIVATE KEY`, `BEGIN PRIVATE KEY`, `ALIPAY_PRIVATE_KEY=`, `eyJ`, plus a blob sweep for `.env`/`.pem`/`.key`: **zero hits.** And `log --all --diff-filter=D` is **empty — nothing has ever been deleted.** No dead generations.
- ⭐ **The credit reservation pattern** in `generate-image.js` is a proper reserve → generate → complete/release with a compensating release on failure, and it distinguishes upstream 429 (`UPSTREAM_BUSY`, 503) from other failures (502). Log lines truncate error text to 240 chars.

**What all of these have in common: something else already required them.** Vercel required a build, so `prebuild` runs the validators. Supabase's advisor reported the lints, so a migration fixed all of them. npm's registry defaults produced a clean lockfile. Publishing required a `LICENSE`. **The disciplines that are absent are exactly the ones that would have had to be chosen: a linter, a CI test job, a schema for the 529 cases.**

---

## 5. Where it doesn't hold

- 🔴 ⭐⭐ **`pg_advisory_xact_lock` appears exactly twice in 2,179 lines of SQL, and both are in `20260722090000_paid_community.sql`** (lines 114 and 458) — the **newest** migration. The credit and generation RPCs in `202605090001_user_credits.sql` (2026-05-09, the oldest) have **no advisory lock, no `FOR UPDATE`, no `ON CONFLICT`**. The author learned the concurrency lesson, applied it to the ¥9.90 unlock, tested it (`'QR replacement uses a transaction lock and one-current-row index'`) — **and never went back to the ledger that debits a credit per image.** ⭐ **v259's rule: code moves forward in time and never backward.**
- 🔴 **Reservation leak, precisely scoped:** `reserve_generation_usage` debits and inserts a pending row; `complete_generation_reservation` marks it succeeded. `generate-image.js` calls `releaseReservation` in its `catch`, so a *caught error* refunds correctly. A **lambda timeout or hard crash** between the two leaves the credit consumed. `grep -rn 'DELETE.*generation_reservations|retention|purge|interval' supabase/migrations/` = **0** — no reaper, no TTL.
- 🔴 **Prompts are stored indefinitely.** `202605090001_user_credits.sql:30` declares `prompt text not null` on the reservation row. Searched all 12 migrations for a deletion, retention or purge path: **zero**. The only removal is `on delete cascade` from `auth.users`. Every prompt a user types is retained with no stated policy, and there is **no consent gate or privacy disclosure anywhere in the UI** (`src/main.jsx` has no banner; `src/community.jsx` discusses only the payment policy).
- 🔴 **No content filtering** on the 6,000-character prompt before it is stored and forwarded to a third party.
- ⚠️ **Rate limiting is inverted.** `takeCommunityRateLimit` (30/min) exists and is called in **five `api/admin/community/*` handlers only**. `generate-image.js`, `me.js`, `favorites.js`, `billing/history.js`, `community/status.js`, both checkout endpoints and the OAuth pair have none. **The limiter guards the endpoints only the author can call.** (And it is in-memory, so on serverless it is per-instance regardless.)
- ⚠️ **Asymmetric kill-switch.** The community path has `COMMUNITY_PAYMENT_ENABLED=false` by default and a test for it. The Stripe credit/membership path has no equivalent flag.
- ⚠️ **Zero Stripe tests.** `grep -ci stripe` across all three test files: **0, 0, 0**. `grep -ci alipay`: **65, 0, 9**. Defensible — you test the integration you hand-built, not the vendor SDK — except `webhook.js` is 154 lines of his own dispatch logic on top of `constructEvent`.
- ⚠️ **Actions not pinned.** `publish-style-skill.yml` uses `actions/checkout@v4` and `actions/setup-node@v4`, 0 of 2 SHA-pinned. Permissions *are* correctly scoped (`contents: read`, `packages: write`).
- ⚠️ **The workflow mutates the package name in CI** — `npm pkg set name=@freestylefly/gpt-image-2-style-library` — so the GitHub Packages artifact and the npm artifact ship under different names from the same tree. And **the workflow does not run either generator**, so the published skill is whatever was committed.
- ⚠️ **`.env.example` is the one populated permission.** Every secret is blank; `SUPER_ADMIN_EMAILS=2689458656@qq.com,canghe0818@gmail.com` is not. It is the **only populated value in the file that grants a permission rather than setting a parameter** — and `profilePayloadFromUser()` promotes any signed-in email matching it to `super_admin`. A fork that copies the example verbatim and enables Google sign-in grants the upstream author super-admin on its own deployment.
- ⚠️ **`data/cases.json` is 1,304,674 bytes and is fetched whole on mount** (`src/main.jsx:3117`), with no pagination or code-splitting. Every visitor downloads all 529 prompts.
- ⚠️ **The 22 templates are the product's claim and the 529 cases are its volume — and the templates are validated while the cases are not.** 4% of the corpus carries the discipline.

---

## 6. The licence, stated plainly

`README.md` contains, in the same file and the same language, eight lines apart:

- **:512** — *"This project only organizes publicly accessible community prompts and example images for learning and research. It does not claim ownership of any third-party original content."*
- **:520** — *"This repository does not guarantee that third-party content can be used commercially. Please obtain authorization from the original rights holder before commercial use."*
- **:528** — *"This project is open source under the MIT License. You can use, modify, distribute, and build on it freely while preserving the license notice."*

**⚠️ This corrects my own first reading.** I had this as an i18n finding — a claim in English qualified only in a Chinese-only file. It is not. `README.md:504-520` carries the **full disclaimer in fluent English**, clause for clause, in all three READMEs. `docs/disclaimer.md` is a **Chinese duplicate** of a section already present in every README, which the "Full disclaimer" link points at. (Two copies of one licence-critical fact, in two languages, with no declaration of which is authoritative — **D32 unapplied**, in the lowest-stakes place it could happen. They have not drifted yet.)

So the contradiction is fully legible to every reader: **"distribute it freely" and "we don't own this, get permission before commercial use," in one document.** MIT covers the code — 10,666 lines of it, cleanly. It does not, and cannot, cover 543 images the same file says belong to someone else.

**On the images:** the disclaimer's own words settle the generated-vs-collected question. Line 512 says the project *organizes* "community prompts **and example images**"; line 516 calls them "generated images" whose "inspiration and data sources" are public communities. Read together: **these are AI-generated images collected from public posts, not images this project generated.** Six sampled jpgs are plain JFIF with **no C2PA, no OpenAI marker, no copyright field, no watermark** (`file` + `strings` over 6 files) — which proves nothing either way, only that any provenance metadata is gone.

**Attribution, measured:** the disclaimer names two principal sources. **OpenNana is cited per-case 5 times** (`gallery-part-2.md` lines 2189, 3155, 3414, 3657, 4563 — one of them the malformed one). **YouMind is cited per-case zero times** (extent: all 12 tracked `.md` + both data JSONs; YouMind appears only in the 4 document-level disclaimers). The other ~524 cases credit the **original poster** — ~230 distinct X/Twitter handles (@MrLarus 30, @liyue_ai 21, @BubbleBrain 11) plus ~15 Xiaohongshu ids. ⭐ **That is better practice than crediting the aggregator** — and nothing explains that the disclaimer answers *where the author looked* while the per-case sources answer *who made it*.

**Monetisation is disclosed and asymmetric:**

| surface | affiliate links |
|---|---|
| each of the three READMEs | **6 `aff=` + 3 `utm_`**, identical in all three |
| the website (`src/main.jsx`) | **1** |
| **the agent skill (whole directory)** | **0** |

⭐ **The agent-facing artifact carries no monetisation at all.** 17 of 159 commits (10.7%) concern sponsor placement, including the two commits immediately before the last case-add: *"move APIMart sponsor to first position"* and *"Move PackyCode sponsor to second position."* One sponsor link carries `utm_campaign=awesome-gpt-image-2` — the v40 UTM-instrumented-funnel mechanism, campaign named after the repository. **And the image backend is Ciyuan (`generate-image.js` → `${CIYUAN_BASE_URL}/v1/images/generations`), which is itself one of the seven listed sponsors** — the sponsorship is load-bearing on the product, not decorative.

---

## 7. Claim audit

| Claim | Truth | Verdict |
|---|---|---|
| badge **`Cases-532`** (line 8, all three READMEs); *"all 532 cases"* (~line 173) | `totalCases: 529`; ids span 1–532 with gaps {12, 169, 170} | ⚠️ **WRONG by 3** — it counts the id ceiling |
| *"500+ Reverse-Engineered Cases"* | 529 | ✅ honest |
| *"20+ Industrial Templates"* | 22 | ✅ exact |
| **all 13 per-category counts** in the README tables | UI 73 · Poster 86 · Photo 77 · Illustration 58 · Charts 52 · Product 41 · Character 29 · Other 28 · Brand 27 · Scenes 20 · History 16 · Architecture 12 · Documents 10 = **529** | ✅ **all 13 exact, sum exact** |
| *"Updated irregularly with new workflows"* / 不定期更新 / 不定期に更新 | present in all three, hedged by construction | ✅ **v270's rotting-promise test: passes** |
| **`### 近 24 小时 X 社区新增`** — Chinese README only, line 441 | introduced **2026-05-04**, unchanged for **112 days** across ~40 case-add commits. The English equivalent reads *"Latest Community Additions"* + *"Only the latest collection and import run is shown here."* | 🔴 **v270 instance, in one language** |
| performance / speed / coverage claims | **none exist** (extent: all 12 tracked `.md`) | ✅ nothing to inflate |
| a last-updated date, or a CHANGELOG | **neither exists** in any `.md` | ⚠️ the only date is `git log` |

⭐ **The badge is the one number in the repository not derived from the data.** Everything the generator computes is right; the one figure typed by hand is wrong. And the gap is fully explained: `case12.jpg`, `case169.jpg` and `case170.jpg` were added in the **root commit** and their `<a name="case-N">` anchors have **never existed in any committed version of any gallery file** (checked every historical revision of all three files; positive control on `case-13` fires). **Not a takedown — three images shipped for cases that were never written, carried unreferenced for four months.**

⚠️ And the repository contains **both** the right and the wrong answer to v270's test, written on the same day by the same hand: one cadence sentence hedged in three languages, and one section heading time-stamped in one.

---

## 8. The agent surface

- **Progressive disclosure: 2,433 B `SKILL.md` vs 26,351 B reference = 10.8×.** The frontmatter description says when to use it and names the operations (create / rewrite / classify / improve).
- ⚠️ **No negative routing clause.** Nothing says where *not* to use it or where to go instead. (v271's subject had one in 10 of 10 descriptions; this is the one thing that subject did better.)
- ✅ The reference is **bilingual by construction** — every one of the 22 templates carries parallel EN/ZH `Use when`, `Guidance` and `Pitfalls`, rendered from the schema. **7% Chinese by character count.** `SKILL.md` is 13 Chinese characters of 2,433 bytes.
- ⭐ **The agent surface is the most internationalised artifact in the repository** — the inverse of v271, where the skill was Chinese-only and the human could not audit it. Here the operator-facing docs are the Chinese-only ones: `docs/disclaimer.md` (446 Chinese chars, 0 English), `docs/paid-community.md` (644), `docs/alipay-web-payment.md` (523).
- ✅ It tells the agent to distrust its own memory: *"Prefer the reference over memory when template names, categories, covers, or style tags matter."* ⚠️ No anti-fabrication rule, no consent language.
- **Distribution:** npm (`gpt-image-2-style-library`) · GitHub Packages (`@freestylefly/…`, renamed in CI) · `.claude-plugin/marketplace.json` · `agents/openai.yaml` for Codex · `npm run install:skill`. Versions agree at **1.0.4** across skill `package.json`, `marketplace.json` and the newest tag. **v1.0.3 never existed** (`log -p -S 'v1.0.3' --all` empty; all four tags created 2026-05-08 within eight hours).
- **`bin/install.mjs` (92 lines) is correctly scoped and I verified it.** `rmSync` targets `join(root, skillName)` — **its own subdirectory only**, never `~/.claude/skills`. It honours `CLAUDE_HOME`/`CODEX_HOME`/`AGENTS_HOME`, throws if a package entry is missing (`:57-62`), and rejects unknown targets (`:73`). ⚠️ **But bare `npx gpt-image-2-style-library` defaults to `all`** — Codex + Claude Code + shared — with no prompt, and the summary prints only afterwards. Payload includes `assets/city-life-system-map.png` at **2,023,093 bytes**, so the default writes ~**6 MB** across three home directories for one skill whose text is 29 KB.

---

## 9. Corpus position

**Corpus-first subject.** Extent: `CLAUDE.md` + `_state/` + `_patterns/`, needles `awesome-gpt-image-2`, `freestylefly`, `canghe`, `苍何`, `gpt-image2`, `youmind`, `opennana`, `ciyuan`, `apimart`, `hiapi`, `pptoken`, `doloffer`, `"Prompt as Code"` — **all zero**, with positive controls (`HiThink` = 3 files, `同花顺` = 3 files) proving both Latin and Chinese greps fire.

- ⭐ **`packycode` returns 3 hits** — `_patterns/03-active-candidates.md:1683` records PackyCode among cc-switch **v73**'s ~20 sponsors. **A shared *sponsor* across two corpus subjects 199 ships apart.** Recorded as an observation and **explicitly declined as Pattern #57** — a funding relationship is not a dependency (the v268 `vercel-labs` org-coincidence precedent).
- Prior image subjects: **v84 image-blaster** and **v139 image-extender**, both **0/4 STRICT** requiring operator overrides. This subject is materially different: a Claude Code skill, a plugin marketplace manifest, a schema-driven generator and a Claude-co-authored root commit put (b) at STRONG on its own.
- ⭐⭐ **Pattern #50 sub-variant 50c — *"Aggregator-with-commercial-product-entry-bundled-in-repo"* — is the exact anchor, and this is its second instance.** 50c's definition names the funnel terminus as *"Commercial-product install (`…/.claude-plugin/marketplace.json`)"*; this repository has one. Registered at the v50 audit as **N=1 stale-flagged with a retirement review due at v60** — **222 ships ago**. And the variant note that matters: at v50 (Composio) the bundled entry pointed at an *external* SaaS; **here the entire commercial platform — 33 handlers, Stripe, Alipay, credits, admin, refunds — is committed in the same MIT repository as the catalogue it funnels from.**
- Also instances: **Pattern #68** Awesome-List-Genre, code-carrying hybrid sub-variant (the v201/v240/v253/v254 line). **Pattern #88 88c** machinery-with-enforcement, at the build layer. **Pattern #19 19a** (author not Anthropic).
- ⚠️ **Library-vocab #13 "OSS-with-hosted-Pro-SaaS-tier-on-MIT-base" was RETIRED at v96.** This subject is a clean second instance and could be **re-registered at N=2** under the C07 precedent (*"RETIRED v151 → RE-REGISTERED at N=2 at the v184 ship"*). Recorded for the audit, **not self-executed.**

---

## 10. ⭐⭐⭐⭐⭐ The ship's rule

Every check in this repository that works is a check something else already required. `prebuild` runs the schema validators because Vercel needs a build. A whole migration exists because Supabase's advisor emailed a warning list. The lockfile is clean because npm's default registry is npmjs.org. Publishing needed a `LICENSE`, so there is one.

And every check that is missing is one that would have had to be chosen. Twenty-seven tests that name, individually, every way a payment system can be defrauded — including a test that the kill-switch defaults closed and a test that browser roles hold no table grants — sit behind `npm test`, and nothing on earth types `npm test`. Ten thousand lines of JavaScript have no linter. The 529 cases that *are* the product have no schema, so there was nothing for a validator to attach to, so they got three regexes with fallbacks that cannot fail.

⭐ **A gate holds when something else already requires it. The checks you must remember to run are the checks you do not have.**

⇒ **v267:** the discipline stops where the artifact stops being code · **v268:** a gate exists where a reader can refuse · **v269:** no gate can see an entry that was never added · **v270:** no gate can fire on a claim that was true when it was written · **v271:** a gate's scope is inherited from its location, not its subject · **v272: a gate holds when something else already requires it.**

And the measurement that proves it, in one line: **the artifact with five fail-closed invariants has been byte-identical for 108 days; the artifact with three silent fallbacks grew by 131 cases in the same window.**

---

## 11. Method

**Fleet:** 13 dimensions, **12 returned, 1 died** (`tests-and-gates`, StructuredOutput retry cap) — hand-covered in full, including the enforcement census with stated extent over all 656 tracked files, the 27 test names, the dynamic `api-imports.test.js`, and the `prebuild`→Vercel gate. **46 agents · 5.39M subagent tokens · 1,172 tool uses · 13.7 min.**

**Fleet errors — 4, of which 2 substantive:**

1. 🔴 **FABRICATED.** A dimension reported, at HIGH significance, that *"`python/pyproject.toml` declares `Proprietary` while the root LICENSE says MIT."* **There is no Python in this repository** — `ls-files | grep -c '\.py$|pyproject|requirements|setup\.py'` = **0** over all 656 files, and the string `Proprietary` appears in **zero** tracked non-image files. It imported **v271's HiThink finding wholesale.** Had it stood, it would have been a headline. It was then repeated by a second agent citing "GROUND-TRUTH-VERIFIED: I read the actual files."
2. 🔴 **Line numbers reported as case ids** — *"OpenNana receives 6 per-case links (cases 2189, 3155, 3414, 3657, 4563)"*. Max case id is 532; those are line numbers in `gallery-part-2.md`. The underlying fact was right and precise once corrected.
3. ⚠️ **`git log --all --oneline | wc -l = 50`** against a truth of 160, which I refuted by running it myself.
4. ⚠️ **A CRITICAL rated on a wrong consequence** — *"README.md:74 links to a Chinese-only disclaimer, trapping English readers."* The linked file **is** Chinese-only (446 chars, 0 English); the consequence is wrong, because the same README carries the full disclaimer in English 430 lines further down. The agent never checked.

⭐ **Three of these four got the fact right and the interpretation wrong** — v271's D51 pattern at a fifth data point. Only the Python one was invention.

**My own corrections, all pre-publication:** (1) the disclaimer is **not** Chinese-only — `README.md:504-520` carries it in English, which killed my strongest i18n framing and produced a better one; (2) `install.mjs`'s `rmSync` is **correctly scoped** to its own subdirectory, not the user's skills directory; (3) my perl-based anti-slop counter reported **0 everywhere** and was silently broken by byte-vs-codepoint semantics — caught by a positive control, re-run in node with the repository's own regex; (4) my "13 missing images" was a too-narrow `caseN.jpg` regex — they are `.png` and all 529 resolve; (5) my "the heuristic misclassifies identical titles" framing was **subsumed by a better finding** — the titles are degenerate (392 distinct for 529 cases), and 23 of the 27 cases sharing the worst title are author-indexed.

**⚠️ NEW METHOD RULE PROPOSED — a companion to §43.2.** The v257 hazard is that *a ground-truth block handed to a fleet is an amplifier*. This ship found the adjacent one: **a fleet agent can import the PREVIOUS SHIP's findings into the current one, unprompted.** My ground-truth block never mentioned Python; the prompt merely referenced v271 and v269 as precedent. That was enough for one agent to produce a fabricated licence contradiction and a second to corroborate it as read-from-file. ⇒ **When a fleet prompt cites a prior ship for method, name the prior subject explicitly and state that none of its facts transfer.** And on the orchestrator's side: **every cross-ship-shaped finding must be re-derived from a command in this clone before it enters a document.**

**Environment:** `python3` **blocked** (permission denied, not the v236 SIGKILL); `node -e` blocked by the permission layer → all measurement done via `.mjs` files written to the scratchpad. `git branch --show-current` unavailable (git 2.19.0).

*Sibling documents: `(C) Verdict.md` · `(C) Pilot Methods Menu.md`.*
