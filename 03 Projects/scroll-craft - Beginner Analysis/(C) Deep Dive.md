# (C) scroll-craft — Deep Dive

**Subject:** `nateherkai/scroll-craft` · MIT · plugin `nateherk-design` v0.2.0
**Wiki:** v282 · built 2026-09-03
**Source verified:** two full clones, working trees `diff -rq` clean both directions, **HEAD `677619e74553c006203d9174fe4025f8584a3907`**
**git 2.50.1** — no `git log` truncation pathology (the v267/v281 hazard); every count below is `rev-list`- or enumeration-derived.

---

## 1. What it is

A **Claude Code plugin** shipping one skill, `scroll-craft`, that builds *"premium, scroll-driven interactive landing pages"* and then **screenshots its own output in a headless browser to check its contrast, motion and accessibility**.

The pitch, `README.md:5`:

> Most AI website output fails in one of two directions. It is either well behaved and forgettable, or it is a flashy scroll animation with 2.1:1 body text, a headline that wraps to six lines on a phone, and the same six sections every other AI page has.

Install is the standard plugin path (`README.md:79-85`): `/plugin marketplace add nateherkai/scroll-craft` then `/plugin install nateherk-design`.

### Scale, measured

| Metric | Value | Basis |
|---|---|---|
| Commits (HEAD) | **12** | `git rev-list --count HEAD` |
| Commits (`--all`) | **12** | `git rev-list --count --all` |
| Roots | **1** | `git rev-list --max-parents=0 HEAD \| wc -l` |
| Merges | **0** | `git rev-list --count --merges HEAD` |
| Authors | **1** (Nate Herk) | `git log --format=%ae \| sort -u \| wc -l` |
| Tags | **1** (`nateherk-design--v0.2.0`) | `git tag \| wc -l` |
| Tracked files | **32** | `git ls-files \| wc -l` |
| Repo size | **17 MB** (3 `.webp` = 6.6 MB) | `du -sh` |
| Age | **2026-08-22 → 2026-09-01** (12 days; 2 days stale at wiki) | root/HEAD commit dates |

Root commit: `2ce4014` · 2026-08-22 10:34:35 -0500 · *"Initial commit: scrollcraft as a Claude Code plugin."*

### Layout

```
.claude-plugin/marketplace.json      the marketplace manifest
plugins/nateherk-design/
  .claude-plugin/plugin.json
  skills/scroll-craft/
    SKILL.md            22KB   the procedure (Step 0 interview → Step 5 verify) + 22 hard rules
    references/
      uniqueness.md     24KB   8 page grammars, the signature move, the fingerprint gate
      feel.md           13KB   the feeling curve, the one engineered peak, the feel check
      devices.md        27KB   9 scroll devices + pointer devices, the cue contract
      taste.md          15KB   the design floor: spacing, type, colour, depth, motion
      verify.md         24KB   the harness, and what it cannot tell you
      worldflight.md    16KB   continuous-world mode
      worlds.md          8KB   art direction, the style-preamble method
      assets.md         13KB   generation, camera moves, encoding for scrubbing
      template.html      6KB   a starting skeleton
      device-diag.html   9KB   a real-device scrub diagnostic
    engine/
      scrollcraft.js    59KB / 1,211 lines   the runtime, never edited per project
      scrollcraft.css   20KB
    scripts/            doctor · workspace · kie · encode · serve · shoot · worldflight-assert
    templates/FINGERPRINTS.md   the empty registry a new workspace is seeded from
    CHANGELOG.md        33KB   incident → rule, per build
EXAMPLES.md             37KB   the author's twelve-row filled registry
```

---

## 2. ⭐⭐⭐⭐⭐ The thesis: this artifact is organised around one failure class — **the failure that looks like success**

Applying the **v246 detector** (`grep -rni "silent" .`) returns **22 hits**, and every one names a defect that *presents as working*:

| Citation | The silent failure |
|---|---|
| `serve.mjs:7` | file:// fetches are CORS-blocked so *"the page silently falls back to posters and **looks fine while proving nothing**"* |
| `worldflight.md:234` | *"It fails silently and **it looks like success**. The engine mounted, every leg…"* |
| `verify.md:175` | *"silently, **which looks fine and is not**"* |
| `README.md:60` | *"a clip that silently never decoded, **which looks exactly like a paused film**"* |
| `taste.md:93` | *"an inverted section renders bone type on concrete at **1.15:1**"* while its sibling passes |
| `devices.md:496` | `magnet` and `cue` both write `transform`, so the magnet *"**silently wins**"* and the entrance rise is discarded |
| `doctor.mjs:11`, `encode.sh:28` | a **stripped ffmpeg** carries ~50 filters and *"silently lacks"* `scale` |
| `verify.md:261` | *"Both were **permanent silent freezes**; the engine now releases…"* |
| `verify.md:334` | *"An act that never pins, silently → **The engine now warns in the console**"* |
| `scrollcraft.js:584`, `:609` | *"A pinned act whose stage is not actually sticky **fails silently**"* |
| `SKILL.md:143` | dependencies *"are missing rather than working around them **silently**"* |

**This is the why behind every piece of machinery in the repository.** `serve.mjs` exists because `file://` proves nothing. `doctor.mjs` exists because a stripped ffmpeg misreports its own fault as a syntax error in *your* command. Contrast is measured on the **composited** screenshot because — `shoot.mjs:331-332` — *"the frame beneath a headline changes as you scroll, so it can pass on the poster and fail three [frames later]."*

⭐ And `verify.md:334` shows the doctrine being *upgraded*: when a silent failure was found, the fix was to **make it loud**. That is **v262's fail-loudly rule, rediscovered independently**.

---

## 3. ⭐⭐⭐⭐⭐ THE SHIP'S RULE: every artifact this project's machinery reads is accurate; every artifact only a person reads has drifted

The repository has **zero CI** — no `.github/`, no workflows, no hooks, no pre-commit, no `package.json` (verified: `git ls-files | grep -Ei "workflow|\.github|hook|pre-commit"` → **NONE**). So the split below is not gated-vs-ungated. It is *consumed-by-a-mechanism* vs *read-by-a-human*.

### Accurate — every number a mechanism or a gate consumes

| Claim | Verdict | Basis |
|---|---|---|
| *"Eight mutually exclusive page grammars"* | **EXACT** | `uniqueness.md` §§2.1–2.8, enumerated |
| *"nine scroll devices"* (`README:128`) | **EXACT** | `devices.md` §§1–8 + §10 = 9; §9 is *"Pointer devices: interactivity that is **not** scroll"* |
| *"at least 4 of 6 dimensions"* | **EXACT, and stricter than stated** | `uniqueness.md:427`: *"**Not** 4 of 6 on average across the table. Four against each row, individually."* |
| *"the author's twelve-row table"* | **EXACT** | `EXAMPLES.md:38-49` = 12 data rows (`lane` is a separate worked example at `:277-279`) |
| Design floor: 4px base, 45–75ch, tracking, line-height | **EXACT** | `taste.md:17`, `:41` (`--sc-measure` 62ch), `:38`, `:44` |
| WCAG thresholds | **CORRECT AA** | `taste.md:85-86`: body ≥4.5:1, large ≥3:1, controls and focus ≥3:1 |
| *"450,000-member community"* | **CONFIRMED** | live site states *"Global community · 450,000 members"* |
| Engine is *"Zero dependencies"* | **TRUE** | no `package.json`/lockfile anywhere; engine has zero `import`/`require`/URL lines |
| CHANGELOG *"records what broke… and the rule that came out of it"* | **TRUE** | every item is an incident attributed to the build that surfaced it — `(saas)`, `(agency and nateherk both hit it; perkform and saas both had the hole)` |

### Drifted — every artifact only a human reads

**(i) ⭐⭐⭐ The README's lead showcase is not a scroll-craft build.** `README.md:16-19` presents **AI Automation Society** first, with the first screenshot. Two independent instruments disagree with it:

- **Documentary.** `EXAMPLES.md:3-4` states *"Every site built with **scroll-craft** gets one row here, appended after it ships."* The registry holds 13 rows — `perkform` ✓, `nateherk` ✓, `agency`, `saas`, `vesper-v2`, `descent`, `airfield`, `pigment`, `maison`, `orrery`, `scrollcraft-showcase`, `phase`, `lane`. **`ais`/`aiautomationsociety` is absent entirely.**
- **Mechanical.** Executing JS in the live page: **0** `data-sc-*` attributes, **0** `sc-*` classes, **0** `--sc-*` variables, no `scrollcraft.js`, HTML never mentions scrollcraft, **0** `<video>` elements — and it loads **`vendor/lenis.min.js`**, a third-party smooth-scroll library, in a project whose plugin description says it is built *"on a full design floor … rather than on an animation library."*

⭐ **The registry's own rule rules out the innocent explanation.** `EXAMPLES.md:270-271`: *"Rows are append-only. A build that has been superseded stays in the table, because the space it occupies is still occupied."* So "it was rebuilt since" does not account for the absence — the rule explicitly covers supersession.

**The control passes.** `nateherk.com` **is** a verified build: **11** distinct `data-sc-*` attributes across **30** elements (`data-sc-smooth`, `-progress`, `-act`, `-span`, `-stage`, `-verify-state`, `-cue`, `-rise`, `-in`, `-tilt`, `-pan`), **28** `sc-*` classes, and `scrollcraft.js` served from its own origin. It also loads a separate `glass.js` — **bespoke page JS, exactly as the hard rule prescribes** (*"Editing the engine to get a bespoke behaviour → Bespoke JS in the page"*). Note `data-sc-verify-state` is live **in production**: the harness's own hook shipped.

⭐ And the un-linked example is the registered one: PERKFORM (`README:26`) is the only showcase without a URL, and `perkform` is the registry's first row.

**(ii) The em dash.** `SKILL.md` hard rule: *"**Em dash anywhere visible**"* → forbidden. Commit `f6bf655` (2026-08-22 12:52) swept em dashes out of **17 files, 96 insertions for 96 deletions** — a thorough hand pass. Commit `e957985` (2026-08-23 16:24, **28 hours later**) added `device-diag.html` (214 lines) carrying an em dash in a **visible `<h1>`**, present at introduction:

> `device-diag.html:53` — `<h1>scrub diagnostic — SCROLL UP AND DOWN A FEW TIMES, then read the verdicts</h1>`

`merge-base --is-ancestor f6bf655 e957985` → **TRUE**. It is the **only** em dash in the tree (31 text files scanned) and there are **zero** en dashes. It has stood 11 days.

⭐ **And its location is the point.** `verify.md:238` states the harness's admitted blind spot: *"Headless Chrome on the build box cannot reproduce an iPhone's video decoder, Low Power Mode, or touch."* `device-diag.html` **is the artifact built to cover that blind spot** — a page a human opens on a real phone. So the one file that breaks the style rule is the one where **a person is the instrument** — and the rule the eye was supposed to catch went uncaught precisely there.

**(iii) Extraction residue.** `worldflight-assert.mjs:6` documents its own invocation as `node lab/worldflight-assert.mjs`; it ships at `scripts/worldflight-assert.mjs`. `shoot.mjs` defaults output to `lab/shots` / `lab/mobile` / `lab/reduced` (`:11-13`, `:39`), and **`lab/` appears nowhere in the README's layout tree**.

---

## 4. Provenance: this repository is a downstream mirror, not the development line

Five independent, tree-verified lines of evidence:

1. **CHANGELOG entries predate the repo.** Earliest heading is **2026-08-21**; the root commit is **2026-08-22 10:34:35**.
2. **A commit says so.** `82e6853` — *"v0.2.0: make the skill portable, and **sync upstream engine work**."*
3. **It cites paths absent from the tree.** `CHANGELOG.md:349` — the contrast checker was *"Ported from the working checker nateherk shipped at `lab/min-contrast.mjs`"*; also `lab/worldflight-rig/` (`:219`). `git ls-files | grep ^lab/` → **nothing**.
4. **The upstream has a name.** `OtherWorlds/Ultimate Websites/` at `CHANGELOG.md:4`, `:219`, `:542`, `:580-581` — holding `builds/`, `lab/worldflight-rig/` and, per `:580-581`, *"**twelve builds** and the live registry."* This is where `EXAMPLES.md`'s twelve rows come from.
5. **Production matches no commit.** `nateherk.com/scroll/scrollcraft.js` = **56,688 bytes / 1,177 lines**; the nearest repo state is `e957985` (56,343 / 1,167, **+345 bytes / +10 lines**), and HEAD is 58,540 / 1,211. The deployed engine sits *between* two commits — consistent with a third, private lineage.

**This is not concealment.** The v0.2.0 commit title is literally *"make the skill portable"*; the extraction is the stated purpose and the CHANGELOG discusses migrating workspace resolution so the private builds still resolve. But the extraction is exactly what produced the one defect class — paths that only exist upstream (§3(iii)).

---

## 5. The machinery, audited

### 5.1 The gates — two of three fail closed, and both gate the *environment*

| Checker | Behaviour | Scope |
|---|---|---|
| `doctor.mjs` | **FAILS CLOSED** — `:161` filters `sev === "required"`, `:166` `process.exit(1)` with *"required check(s) failed. Fix these before building."* Each row carries a `fix` hint printed dimmed (`:158`). **9** `add()` calls (`:41,79,85,101,121,138,145,146,150`). | setup preflight |
| `worldflight-assert.mjs` | **FAILS CLOSED** — `:273` `process.exit(fail ? 1 : 0)`. **24** assertions by enumeration (desktop 19 + reduced-motion 5). | worldflight mode only |
| `shoot.mjs` | **REPORTS ONLY.** Its only two `process.exit(1)`s are `:31` (playwright-core unresolved) and `:65` (no Chrome found) — both **setup**. No design finding ever exits nonzero. | the actual design checks |

**So the checker that measures the design cannot fail anything** — and that is deliberate. `verify.md:179` heads a section *"What the harness cannot tell you"*, whose three items are *"Whether the composition is any good"*, *"Whether the motion is smooth"*, and:

> *"**Whether the page means anything.** Six acts that each work and together say nothing is the most expensive failure available here."*

`README.md:64`: *"a machine can prove a page works and cannot tell you it means anything."*

⭐ **This is v250's behaviour independently repeated: the author drew the line exactly where decidability ends and wrote the criterion down.** Report-only is a stated policy, not an oversight — *"Read the sheet for these. They are the ones that matter most."*

### 5.2 What the harness measures — and the asymmetry

`shoot.mjs` implements exactly four checks, all of which require a *running* browser:

1. **dead scroll** — `:516-518` (`DEAD SCROLL between:` / `no dead scroll detected`), deliberately tuned against false positives: `:276` panning reads as dead scroll, `:290` the run-up to a pinned act, `:295` a dissolve in progress.
2. **cues that never reach full opacity** — `:155`, and `:565` for worldflight legs.
3. **contrast on the composited page** — `:326`, `:357` (`page.evaluate`), direction-aware per line (`:405`). Justified at `:327`: *"Sampling the video directly ignores every scrim, gradient and blend on top."*
4. **legs/clips stuck on a poster** — `:544-545`, `:567-569`: *"a poster looks exactly like a paused film."*

⭐ **It checks zero grep-able rules.** Tested: `em dash`, `—`, `eyebrow`, `transition: all`, `01 /`, `counter`, `scroll cue` → **0 hits each** in `shoot.mjs`. The single `gradient` hit (`:327`) is the comment above.

**And that is the coherent policy, not a gap:** machinery for what the eye cannot catch, habit for what it can. Contrast at 1.15:1 under a bright video frame at 62% scroll is invisible; an em dash in an `<h1>` is not. The policy's one visible failure landed in the one file whose reader is a human on a phone.

### 5.3 The engine

**Genuinely dependency-free**, verified three ways: no `package.json` or lockfile anywhere in the tree; zero `import`/`require`/`http(s)://` lines in `scrollcraft.js`; header reads *"Vanilla JS. Zero dependencies. Zero DOM generation. The engine does NOT build your page."* **Installing this plugin adds zero npm packages** — the one dependency, `playwright-core`, is installed by the user in their own build folder (`shoot.mjs:24-32`, resolved from `process.cwd()` with a graceful message).

**40** distinct `data-sc-*` attributes (identical count in repo and production). Accessibility is real, not decorative: `prefers-reduced-motion` handled in JS (`:142` `matchMedia`) and CSS (`:98`, `:387` full media block). Pointer devices are gated to `(hover: hover) and (pointer: fine)` and disabled under reduced motion (`devices.md:504-506`) — they are enhancements on real links, so keyboard equivalence is not owed. ⚠️ The engine itself has **0** `keydown`/`tabindex`/`Escape`; the keyboard behaviours EXAMPLES.md claims (`orrery`: *"Click or tab to keep it held, Escape releases"*) live in bespoke page JS, outside both engine and harness.

`devices.md:495-502` documents a real **race condition** — `magnet`, `parallax` and `cue` all write `transform`, the magnet's own rAF loop wins, so set `data-sc-rise="0"` or drive an inner wrapper from `--sc-p`.

### 5.4 Security surface

| Finding | Detail |
|---|---|
🔴 **`serve.mjs` binds all interfaces while advertising localhost** | `:50` `.listen(PORT, cb)` — no host argument, so Node binds the unspecified address; `:51` prints `http://localhost:${PORT}`. |
🔴 **Path-traversal guard is a near-miss** | `:35` `if (!file.startsWith(ROOT))` → 403. The comparison lacks a trailing separator, so a **sibling** directory whose name extends the root's passes: with `ROOT=builds/perkform`, `/../perkform-secrets/key.txt` resolves to `builds/perkform-secrets/key.txt`, which `startsWith(ROOT)` accepts (verified as a string property; the `path.join` normalisation half is a code read against documented Node behaviour). Ordinary `../../etc/passwd` **is** blocked. One-character fix: `ROOT + path.sep`. |
⚠️ **An undocumented upload host** | `kie.mjs:27` `UPLOAD = "https://kieai.redpandaai.co/api/file-base64-upload"`. `uploadLocal()` (`:63-78`) base64-encodes a **local file** and POSTs it there. Called at `:161` (`still --ref`), `:177` (`shot` head image — **mandatory** for every generated clip) and `:184` (`--tail`). The file's own header documents `api.kie.ai` **twice** and never names this host; `redpandaai` appears **once in the entire tree, in code, and in zero documentation**. |
✅ **API key handling** | Read from `process.env` or a `.env` walked up from cwd (`:47-56`), sent as `Authorization: Bearer` (`:58`), never logged. `.env.example` says *"Never commit .env."* |
✅ **Supply chain** | Nil. No manifest, no lockfile, no postinstall, zero added packages. |
✅ **Cost disclosed with its basis** | `.env.example` publishes rates (28 credits/still, 160/5-s clip, *"a modest six-act page is around 520 credits"*) **and declares its own uncertainty**: *"though observed billing has run well under the published numbers."* This is the v281 basis-declaration discipline, unprompted. |

---

## 6. ⭐⭐⭐ Genuinely excellent: the registry keeps the embarrassing rows

`EXAMPLES.md:20-31`, the section headed *"Why this file exists"*:

> The first four builds were run before there was a structure axis. Read the rows and the collision is obvious: **all four sit in the same grammar**, with the same nav, the same hero device, the same close, and no signature move on any of them. `saas` (Vesper) and `perkform` are the pair the owner named, but the problem is the whole table. Only the act order and the palette actually moved.
>
> Those four rows are recorded as-built, **warts included**.

Verified: rows 1–4 (`perkform`, `nateherk`, `agency`, `saas`) all read Grammar = *Filmic one-shot* and Signature move = **none** — against a hard rule requiring a signature move on every build. The author documents the violation, credits the person who caught it, and preserves the failing rows, because `uniqueness.md:433-436` says *change the plan, not the log* and *"rewriting a fingerprint row makes the file worthless."*

**This is the strongest form of Pattern #83 honest-deficiency-disclosure the design cluster has produced:** the disclosure is load-bearing rather than decorative *because* an append-only rule makes deletion illegitimate. Rows 5–13 then show the gate working — `lane` states in-row that it *"Shares the grammar cell with `airfield` and differs from it on the other five dimensions"*, and signature moves cross-reference each other for distinctness (`pigment`: *"Distinct from descent's lamp (reveals vs deposits) and maison's tray (authored tokens vs visitor-made marks)"*).

⭐ The registry — an artifact the *skill* maintains and the *gate* consumes — is more accurate about what this author built than his README is.

---

## 7. Identity

**Nate Herk** (Nate Herkelman) — AI-automation educator and entrepreneur, Chicago; University of Iowa (Business Analytics & Marketing); ex-Business Intelligence Analyst, Goldman Sachs; **n8n Verified Expert Partner**; founder of **AI Automation Society** (Skool, **450,000 members** confirmed on the live site); ~950k YouTube subscribers. Reported co-founder/CGO of TrueHorizon AI (web-sourced, not tree-verified).

**NOT Anthropic** → **(a) FAILS** per **§41**. No inference from notability, from publishing a Claude Code plugin, or from the community distributing Claude Code skills.

⚠️ **§37.4:** stars/forks are page-stated or unfetched — **no Pattern #52 claim**.

---

## 8. Method — what was verified, and what was corrected

**Fleet:** one read-only workflow (`wf_eb4fadf2-177`), **17 agents, 0 errors, 3 empty** (StructuredOutput failures on `skill-procedure`, `verify-harness`, `engine`), **~2.24M subagent tokens**, 396 tool uses, 1,050 s. With main-loop that reached ~83% of the 3M per-ship soft cap → **report-only mode entered per the binding rule; no further fan-outs.** The three failed dimensions had **already been hand-covered before launch**, so coverage held.

**Zero fabricated quotations** across every refuter (`"fabrications": []` in all).

⭐ **Every fleet error was a count produced by summarising, and every fix came from enumerating** — `taste.md` sections 8 → **11**; `worldflight-assert` assertions 31 → **24**; `doctor.mjs` checks 6 → **9**. This is **v278's clause (g) replicating on my own fleet.**

**Two corrections I made on myself, both count errors, both fixed by enumeration:**
1. `grep -c` gave **10** numbered device sections and I nearly reported *"README says nine, tree holds ten"* — but §9 is *"Pointer devices: interactivity that is **not** scroll"*, so nine scroll devices is **exact**. The README was right and my instrument was wrong.
2. Three instruments gave **17 / 15 / 13** registry rows. Enumeration showed **two tables**: a 12-row registry and a separate one-row worked example. The README's *"twelve-row table"* was **right**.

⭐ **So in this ship the subject's counts survived every instrument, and every wrong count was produced by a reader** — the inverse of v276/v278/v279/v280.

**Two corrections I made on the fleet:**
1. ⚠️ **A false negative, asserted twice.** Both the `web:live-sites` agent and the `critic` concluded *"neither aiautomationsociety.ai nor nateherk.com contain any `data-sc-*` attributes."* **Refuted by direct measurement:** executing JS in `nateherk.com` returned 11 distinct `data-sc-*` attributes, 30 elements, 28 `sc-*` classes and `scrollcraft.js`. Both agents had used markdown-converting fetches, which strip attributes.
   ⭐ **New method-rule candidate:** *agreement between two agents using the same instrument is correlated error, not corroboration* — the multi-modal-sweep requirement stated as a verification rule.
2. Specific competitor names the landscape agent produced (a starred "Scroll World", "let's-scroll", "Landing", "UITest", "AgentScreenshots", and an "Obscura" that collides with corpus v267's subject) are **UNVERIFIED and not cited**. Only the mature, independently-known prior art is relied on below.

**Not overcome:** **nothing was executed** — 0 of the repo's scripts run (no Playwright/Chrome install, no ffmpeg, no kie.ai key, no spend); `node -e` was permission-denied, so the traversal finding rests on a verified string property plus a code read. GPU/asset generation unexercised. PERKFORM has no URL and was **not** located. Star counts unfetched (§37.4).

---

## 9. Verdict and mint

**GOAL-ALIGNED INCLUDE 3/4** — (a) **FAIL** (§41) · (b) **STRONG** · (c) **STRONG** · (d) **STRONG**. Cleanly goal-aligned; **no §40 invoked, no override.** (b) is STRONG not MODERATE because the artifact *is* a Claude Code plugin and skill — Goal #1 directly, not adjacently.

**NO MINT. Counts 46/12 UNCHANGED · §C-1 13 · §C-2 39 UNCHANGED.** Four grounds (§28 supporting only, per §44.5):

1. **Form-factor within a genre**, ruled on repeatedly: **v168** ponytail, **v204** hallmark, **v218** ui-skills, **v250** diagram-design, **v274** unlazy. **v274's own words are decisive:** *"A skill that adds a runnable checker is a stronger instance of the genre, not a new class"* — and it names v204 as *"a design skill with enforcement machinery."*
2. **A clean instance of CONFIRMED Pattern #88 "Anti-Slop-Curation," sub-typology 88c "machinery-with-enforcement."** Its refuse list is literally the pattern's vocabulary. Joins impeccable **v75** / taste-skill **v81** / huashu-design **v82** / open-design **v83** / ui-ux-pro-max **v85** / html-anything **v91** / guizang **v105** / hallmark **v204** / ui-skills **v218** / diagram-design **v250**. N-tally is audit bookkeeping — **recorded, not self-incremented**.
3. **Domain-not-capability.** Scroll-driven landing pages are a domain — the settled **v212** tabularis precedent (+**v196**, **v210**, **v197**).
4. **Not world-first.** GSAP ScrollTrigger and Lenis are mature prior art for the mechanism; scrollytelling is an established genre. (Ironically, the un-verified showcase runs Lenis.)

**Collision grep: CLEAN.** `scroll-craft`, `scrollcraft`, `nateherk`, `Nate Herk`, `AI Automation Society`, `worldflight` → **zero** prior hits in the vault.

### ⭐⭐ RECORDED, NOT EXECUTED — the audit item

**A design skill that numerically verifies its own rendered output** now stands at **N=2, cross-author.** **v250** diagram-design is N=1 — `verify-treemap.py:305-313` checks *"its own chart does not lie"* by comparing `area_share` to `value_share`. scroll-craft is the **first that renders in a real browser and measures composited pixels** rather than checking its own drawing model, and the only one whose verification hook (`data-sc-verify-state`) ships **in production**. Recorded for the overdue audit; **a promotion is an audit act and is not self-executed.**

**Secondary (not minted):** Pattern **#83** exemplary instance (§6) · Pattern **#66** install surface nil · **#12** (SKILL.md + plugin.json + marketplace.json) · **#19 19a** first Nate Herk / AI-Automation-Society author · **NOT #57** (no corpus subject cited) · **NOT #52** (§37.4).

**Tier:** T1 Assistant Skill / design-language, with a T4 plugin-marketplace facet — reviewable, not asserted.

**Streak:** v281 `GA:138` → **`GA:139 · OG:13 [7 ov]`** — **62 consecutive GA v220→v282**; **§35 CLEAR** ({v280, v281, v282} = 0 OG); **override review 22nd consecutive discharge.**
