# (C) awesome-dsh-plugin — Verdict

**Wiki v240** · 2026-08-18 · `awesome-dsh-plugin/awesome-dsh-plugin` · routine **v2.7**
**Rating: GOAL-ALIGNED INCLUDE 3/4** · **NO MINT** · counts **46/11 UNCHANGED** · §C live standalones **49 unchanged** · surface **≈56 unchanged**

---

## 1. Phase 0.9 — the four criteria

| # | Criterion | Call | Basis |
|---|---|---|---|
| (a) | Author is Anthropic / a registered vendor-direct source | **FAIL** | `fkysly` = a bare handle; the README's Disclaimer states verbatim *"This project is not affiliated with DeepSeek."* No Anthropic link. §41 forbids name/locale/notability rescue. |
| (b) | Goal relevance | **MODERATE** — keys the tier ⚠️ STRONG genuinely arguable | It is the package catalogue for a **rival** harness, and the subject itself is a curated index. Against that: it publishes an **agent-consumed registry API**, its sibling registers a **tool into the agent**, it ships `.claude/skills/`, and its documentation machinery lands squarely on the vault's own live C22–C27 problem. |
| (c) | Analysability | **STRONG** | **Source-cloned** with full history — the first of the DSH run. Every count, threshold, and quote hand-derived from the working tree. |
| (d) | Actionability | **STRONG** | Four independently pilotable mechanisms, zero install required, aimed at a documented vault failure. |

**Tier assignment:** **T3 Reference/Index** with a **registry-infrastructure facet** (it publishes a consumed machine API) — reviewable. Not T4: it is not a plugin.

**§40 note:** operator-requested and goal-adjacent, so **GOAL-ALIGNED per operator direction**; no override consumed, no §35 pressure. The **OFF-GOAL reading is recorded as the reviewable alternative** — a curated markdown list for a competitor's harness is defensibly off both goals, and (b) MODERATE is the honest floor.

---

## 2. ⭐ A governance question this ship must answer first

**v237's Verdict already named this exact repository — and ruled it out:**

> **Pattern #68 cross-ref** — ≥2 curated "awesome" lists have formed around DSH in ~2 weeks (`awesome-dsh-plugin`, `Dominic789654/awesome-deepseek-harness`). **Ecosystem-formation data-point, not a subject.**

So the corpus pre-classified v240's subject as *not a subject*, one ship ago, and is now shipping it on operator request. That is legitimate — the operator sets intake, and there is a precedent, though a weaker one than it first looks: at **v21 → v205** the prompt-leak-archive **genre** was OUTSIDE-SCOPE under the older routine, and a **different** repo in that genre later shipped as v205 once the stance evolved. ⚠️ **That is analogous, not exact:** there a *class* was reopened; here *this specific repo* was ruled not-a-subject and now ships. I looked and found **no verified case of the same repo being re-rated**. So the intake move is defensible but genuinely novel, and it should be **on the record**, not glossed:

- v237's call was made **without reading the source**, on the repo's genre label. It was reasonable and it was **wrong on the facts** — the "list" turned out to hold a data layer, a compiler, a probe suite, a decay scanner, six CI gates, and a published registry API consumed by two independent runtime clients.
- ⭐ **The lesson is not about this repo. It is about intake:** a genre label ("awesome list", "theme", "skin") was allowed to settle a subject question that only source could settle. That is the same failure shape as v216 → v236/v237/v239, where "cosmetic skin" turned out to bound a whole capability class.
- Recorded for the overdue audit as a **method note**: *do not dismiss a candidate on form-factor alone when the form factor is cheap to verify.*

⚠️ It also means the "is this a subject?" question is genuinely close, and I am not pretending otherwise. On the source, my answer is yes — a consumed registry API with an editorial pipeline is infrastructure. On the label alone, v237's answer was defensible.

---

## 3. PATTERN — NO MINT

**Seventh consecutive DSH-run NO MINT, and again on different grounds.** (v236/v237 presentation-not-capability · v238 not-world-first + rationale-not-mechanism · v239 canonical-form-factor + component-not-subject · **v240 canonical genre + decisive external prior art**.)

### 3.1 The §C-mint alternative — RECORDED and DECLINED

**Candidate row:** *"Curated Community Registry — an editorially-verified plugin catalogue that publishes a machine-readable registry API consumed at runtime by third-party storefronts and by the host agent itself."*

**The case for it** (all source-verified): a structured per-entry data layer; generated bilingual READMEs plus a generated site; a submission gate on manifest/age/commit-count; four external probes; a weekly decay scan; a published `plugins.json` + `readmes.json` + `count.json` + feed; and two independent runtime consumers, one of which exposes the catalogue to the model as a **tool**.

**Why it is DECLINED — four grounds:**

1. ⭐ **Decisive external prior art, verified not assumed.** **awesome-selfhosted** already splits into a data repo of per-entry YAML that generates its README *and* a website; **HACS (Home Assistant Community Store)** is already a curated community registry consumed at runtime by an in-app storefront in the host application. Between them they cover the data layer, the generated document, the generated site, the automated link/decay checking, and the host-app storefront. The adversarial verifier's independent verdict on the "nothing structurally new" claim was **"CLAIM SUBSTANTIALLY CONFIRMED … a well-executed curated list with good engineering, but it is not a structural innovation."**
2. **The agent-facing part is not this subject.** `find_dsh_plugin` — the genuinely newest element — lives in **`dsh-find-plugin`**, a *separate repository*, and its primary index is the live GitHub `dsh-plugin` topic, not this list (the list overlays better descriptions). Minting this subject for a sibling's capability is the **component-not-subject** error v239 declined on. And agent-facing package discovery is itself prior-arted by the MCP registry ecosystem.
3. **§28 anti-re-accumulation** + the **DSH precedent chain now seven deep** (v216 → v222 → v227 → v236 → v237 → v239 → v240). v239 ruled the plugin/theme-pack form factor *"canonical and decades old"*; a curated index of that ecosystem is one step further from a capability, not one step closer.
4. **Corpus-first-for-a-domain ≠ mintable** — the meetily v196 / TimesFM v193 / AIRI v210 discipline. Being the corpus's first *plugin-registry* subject is a data-point.

→ Recorded as a **DEFERRED watch axis**: *"curated community registry publishing a runtime-consumed machine API + agent-callable package discovery."* If the corpus later takes an MCP-registry or Smithery-class subject, this is its N=1 precedent — and it should be credited then.

### 3.2 Pattern #68 Awesome-List-Genre — instance-strengthening, with a NEW form-factor sub-variant

**Sub-variant recorded:** *"awesome-list as a compiled artefact over a structured data layer, publishing a machine-readable registry API to third-party runtime consumers."*

⭐ Note the pairing: **v239 minted a #68 sub-variant one ship ago** — *"an awesome-list compiled into a host-app panel — static, index-only, no runtime registry."* v240 is precisely the runtime registry that panel lacked. **#68 gains two complementary form-factor sub-variants in two consecutive ships.** N-tally is audit bookkeeping; recorded, not self-incremented.

### 3.3 ⚠️ Pattern #16 "Skill Dependency Locking" — revival DECLINED

`skills-lock.json` pins **two corpus subjects** by content hash — `nextlevelbuilder/ui-ux-pro-max-skill` (**v85**) and `vercel-labs/agent-skills` (**v51**) — with committed cross-harness symlinks into `.claude/skills/`. Same filename, same purpose, and **Vercel skills in both instances**, 225 wikis after the corpus retired the pattern.

The retired record sets the bar: *"**Revive if:** 2+ frameworks adopt version-locked skill dependency manifests."* It is **not met**:

1. **Not a framework** — multica v15 was a platform whose *architecture* locked skill dependencies; this is a curated list using two design skills as build-time tooling.
2. **Not load-bearing** — the adversarial check returned **"PARTIAL REFUTE — decoration, not load-bearing"**: nothing verifies `computedHash`, nothing refreshes the skills, no script or workflow consumes them, and there is no `AGENTS.md`/`CLAUDE.md`. The consistent reading is one-time design-time use (the repo ships `design-mocks/{a-minimal,b-warm,c-dark}.html`), pinned as a record.

→ **Recorded as a non-qualifying data point, flagged to the overdue audit, NOT self-revived.** Reviving a retired pattern is an audit act (the v232 rule) — and on this evidence the audit should decline as well. ⚠️ This reverses my own initial reading; the verifier earned its keep.

### 3.4 Other pattern touches (recorded, no N self-increment)

- **#57 corpus-recursion — a new relation shape: mutual indexing.** The subject **catalogues three corpus subjects** (v236, v237, v239 — all listed **2026-08-14**, before the corpus shipped any of them) while the corpus had **already named the subject by URL** in v237's Verdict. Prior #57 shapes were dependency (v239's four-way fan-in), port (v207→v208), credited priority (v231→v232), and host↔plugin (v235↔v236). **Subject-and-corpus-index-each-other is new.** Also: it vendors v85 and v51 by hash (§3.3), and its `contributing.md` semver guidance addresses exactly the `^0.1.0-rc.6`/`rc.7` peer pins v236/v237/v239 ship.
- **#83 honest-deficiency-disclosure — the *mild* pole, and unusually clean.** The README's *"if a description claims '46 tools', someone counts them"* has **no mechanism** behind it; `contributing.md` **says so first** (*"CI … cannot tell whether a plugin does what its entry says"*), as does the security warning (*"Being on this list is not a security review"*) and the Disclaimer (*"not affiliated with DeepSeek"*). Compare v239, where the honest README sat beside genuinely careless engineering; here the documentation is *more precise than the marketing line*, which is the rarer direction.
- **#81 manifest/doc drift** — three instances, each in a place the checks structurally cannot reach: a dead `README.ja.md` link on line 5 of both READMEs (no `ja` locale exists); one CRLF record in 1,390; and a **merged submission silently dropped for a missing file extension** (PR #1192).
- **#66 supply chain — two-sided.** *Positive:* least-privilege CI throughout, no lifecycle scripts, two current devDependencies, and a `pr-gate.yml` header that correctly diagnoses and avoids the **`pull_request_target` footgun**. *Negative:* `package-lock.json` resolves 2 of 3 packages from **`registry.npmmirror.com`**, and `npm ci` runs in four workflows (integrity-hashed → availability/visibility exposure, not integrity). **The pi v228 hardening axis gains a partial third instance** after v239.
- **#19 19a** — bare-handle non-Anthropic authorship.
- **Observability / metering:** none. This is not an observability subject.

---

## 4. ⭐⭐ The findings that actually matter

1. ⭐⭐⭐ **It checks its prose against its code.** `generate-readme.mjs` fails the build when `contributing.md`'s category enumeration disagrees with `CAT_IDS` — *"It drifted once already."* **This is exactly the gap v239's `verify-docs.mjs` was recorded as unable to close** (structure, not content equivalence). Two consecutive ships now supply the complete mechanism.
2. ⭐⭐⭐ **The inventory rule.** A merged, well-formed, bilingual submission (`zmm863-commits__dsh-paperclip`, PR #1192) is **absent from both READMEs, the site, `plugins.json`, the storefront, and the agent's tool results** — because it lacks a `.yml` extension and `entries.mjs:69` skips it silently. The filename validator that would have caught it sits *downstream of the glob that excludes it*. → **A consistency check between two views of one source cannot see what is missing from the source.** Directly the vault's C22–C27 class.
3. ⭐⭐ **Automate the evidence, never the irreversible decision.** `scan-decay.mjs` *"Flags — never removes"* with *"a decay report must only ever contain evidence, not doubt"*; `check-bleed.mjs` is *"reported, not enforced"* on an empirically calibrated threshold; `build-site.mjs` holds a `STARS_MIN_COVERAGE = 0.66` publish floor. ⭐ **The sharpest one-ship-apart contrast of the run: v239's `pr-review.mjs` auto-closed a substantive bug report (#532); v240 refuses to auto-remove anything.**
4. ⭐⭐ **A claim caught propagating, again.** The list's verified entry for the v239 subject asserts *"live token stats"* — the phantom feature v239 flagged. I re-verified against the live 33 KB README myself: **zero** `token`/`usage` hits; the only 令牌 is the mobile **pairing** token. v239 republished a retracted benchmark downstream; v240 republishes an unsubstantiated feature downstream. Same failure mode, opposite direction, one ship apart.
5. ⭐ **Velocity measured without the mocked API.** The clone gives **1,662 commits / 853 unique author emails / ~5 days**, git-verified — while maintainership is **one person** (`fkysly`, 243 commits, 86 of ~93 touching `scripts/`+`.github/`). A 967★ storefront and an agent tool read this bus-factor-1 repo's API **live**.
6. ⭐ **`pr-gate.yml`'s security header** — a correct, documented mitigation of the `pull_request_target` privilege-escalation class, plus a rate-limit incident dated today.

---

## 5. Non-claims — stated explicitly

- ❌ **NOT Pattern #52.** Star/fork figures are page-stated (§37.4, mocked API). The git-derived commit/contributor velocity is real but is **not** the verified *star* velocity #52 requires.
- ❌ **NOT world-first** on any axis — awesome-selfhosted and HACS precede on the registry shape; MCP registries precede on agent-facing discovery.
- ❌ **NOT a new top-level pattern** (max remains #85).
- ❌ **NOT first-party DeepSeek** — explicitly disclaimed in the README.
- ❌ **NOT a Pattern #16 revival** (§3.3) — recorded, declined.
- ❌ **NOT the corpus's first CC0 subject** — v205 `system_prompts_leaks` precedes.
- ❌ **NOT #18 B1-MCP** — it ships no MCP server. Its agent surface is a `dsh` tool in a *sibling* repo.
- ❌ **NOT an N=k of the Multi-Vendor Orchestration-Platform row** — nothing here orchestrates agents.
- ❌ **The "1,658 commits" and "500+ plugins" figures from the first page-fetch are DISCARDED** in favour of hand-derived **1,662** and **1,390**.
- ⚠️ **UNVERIFIED and not repeated:** an agent's claim that js-yaml 5's `load()` uses an unrestricted schema. `load()` has been safe-by-default since v4; I could not confirm v5 from source or README. What *is* verified: the parsed object is strictly validated at `entries.mjs:120–161`.

---

## 6. Bookkeeping

- **Counts: 46 confirmed patterns / 11 CONFIRMED Library-vocab — UNCHANGED.** §C live standalones **49 unchanged**; surface **≈56 unchanged**. Zero mints, zero promotions, zero retires, zero revivals.
- **Streak: v239 `GA:97` → `GA:98 · OG:13 [7 ov]`** — **21 consecutive goal-aligned ships** (v220→v240).
- **§35 CLEAR** — rolling window {v238 GA, v239 GA, **v240 GA**} = 0 OFF-GOAL.
- **Overrides: none consumed** (§40 applies).
- **Audit debt:** the ~v221 audit is now **egregiously overdue** (last audit v212; v213–v240 all shipped). This ship adds five items to its agenda: the §3.1 registry watch axis; the §3.3 Pattern #16 non-qualifying revival; the §3.2 second #68 form-factor sub-variant in two ships; the §2 **intake method note** (do not dismiss on form-factor alone); and the new **#57 mutual-indexing** relation shape. Standing items unchanged: the v192 standalone at non-port N=4, the v207-row generalisation, the stale v140 row, and the **C22–C27 retire pass** — which **six consecutive ships have now supplied machinery for**.

---

## 7. Blunt

A curated list is the most boring artefact on the internet, and this one is a small piece of infrastructure wearing that costume. In five days, 853 people filed 1,390 entries, and one volunteer built the thing that keeps them honest: one record per plugin so two submissions can never collide, a compiler so the English and Chinese pages cannot disagree, a check that fails the build when the contributing guide's category list drifts from the code, a bleed detector born from a PR that silently rewrote a stranger's description, a decay scan that refuses to delete anything on its own, and a publish-time floor added the day a bad probe shipped 1,362 null star counts to everything downstream. Every threshold in that list carries a comment naming the incident that produced it.

Then look at what slipped through anyway. A dead Japanese-README link on line 5 of both files, for a locale that was never registered. One record with Windows line endings. And a contributor whose plugin was reviewed, approved and merged on 17 August, and which has never appeared in the README, the website, the registry API, the storefront, or the agent's search results — because the file is named `zmm863-commits__dsh-paperclip` instead of `zmm863-commits__dsh-paperclip.yml`, and the loader skips anything that does not end in `.yml` without saying a word. Every check in the repository compares the README against the parsed data. Both are views of the same glob. Neither can see a file that is outside it.

That is the finding, and it is worth more than the mint I declined. **A consistency check between two views of one source is blind to what is missing from the source.** The vault has been running that exact check on itself for fifty wikis — the index says `03c-projects-v61-v183`, the file holds entries through v240 — and the retire pass keeps getting deferred on the grounds that removal is irreversible and needs judgement. This repository already solved that objection: flag weekly, report evidence and never doubt, skip anything inconclusive, keep one issue updated in place, and let a person pull the trigger.

Take the four scripts' *shapes*. Take the pull_request_target write-up. Do not install anything, and do not cite this list as a safety signal — it says so itself, more plainly than most projects manage, right above 1,390 install commands.
