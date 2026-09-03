# (C) scroll-craft — Verdict

**v282** · `nateherkai/scroll-craft` · MIT · plugin `nateherk-design` v0.2.0 · HEAD `677619e7` · 2026-09-03

---

## The call

**GOAL-ALIGNED INCLUDE 3/4** · (a) **FAIL** · (b) **STRONG** · (c) **STRONG** · (d) **STRONG**
**NO MINT** · counts **46/12 UNCHANGED** · §C-1 **13** · §C-2 **39** UNCHANGED
**Streak `GA:139 · OG:13 [7 ov]`** — 62 consecutive GA v220→v282 · **§35 CLEAR** · override review **22nd** discharge

| Axis | Call | Why |
|---|---|---|
| (a) Anthropic / cultural-peer | **FAIL** | Nate Herk(elman) — AI-automation educator, n8n Verified Expert Partner, founder of AI Automation Society (450k members). **Not Anthropic.** §41 forbids inferring affiliation from shipping a Claude Code plugin. |
| (b) Goal-relevance | **STRONG** | The artifact **is** a Claude Code plugin and skill — Goal #1 directly, not adjacently. No §40 needed, no override. |
| (c) Quality / depth | **STRONG** | 22 hard rules, 8 grammars, 9 devices, a WCAG-correct design floor, a real headless-browser harness measuring composited-pixel contrast, an incident-attributed 33KB CHANGELOG, a dependency-free 1,211-line engine, and a production deployment that verifies. |
| (d) Transferability | **STRONG** | The append-only registry + gate, the silent-failure doctrine, and the "gate the invisible, trust the eye for the visible" policy transfer directly to the vault and to hireui. |

---

## The one sentence

**Every artifact this project's machinery reads is accurate, and every artifact only a person reads has drifted — in a repository whose entire thesis is that the dangerous failure is the one that looks like success.**

Applying the vault's own v246 detector, `grep -rni "silent"` returns **22 hits**, each naming a defect that presents as working: *"the page silently falls back to posters and **looks fine while proving nothing**"* · *"It fails silently and **it looks like success**"* · *"a clip that silently never decoded, **which looks exactly like a paused film**."* That is the why behind every piece of machinery here — and when a silent failure was found, the fix was to make it **loud** (`verify.md:334`), which is **v262's rule rediscovered independently.**

There is **zero CI** in this repository — no `.github/`, no hooks, no `package.json`. So the split is not gated-vs-ungated; it is **consumed-by-a-mechanism vs read-by-a-human**, and it is clean:

- **Right:** 8 grammars, 9 scroll devices, the 12-row registry, the 4-of-6 gate (*stricter* than the README states), the 4px/45–75ch/62ch design floor, WCAG AA thresholds, the 450,000 figure, "zero dependencies", and a CHANGELOG whose every rule is attributed to the build that broke it — `(saas)`, `(agency and nateherk both hit it)`.
- **Drifted:** the README's **lead showcase**, the one em dash, and `lab/` paths that exist only upstream.

---

## The three findings that matter

**1. ⭐⭐⭐ The README's flagship example is not a scroll-craft build, and two independent instruments say so.**
`README.md:16` leads with **AI Automation Society** and the first screenshot. But the registry that states *"Every site built with scroll-craft gets one row here"* has **no AIS row** (13 rows: `perkform` ✓, `nateherk` ✓, `agency`, `saas`, `vesper-v2`, `descent`, `airfield`, `pigment`, `maison`, `orrery`, `scrollcraft-showcase`, `phase`, `lane`) — and the live page carries **0** `data-sc-*` attributes, **0** `sc-*` classes, no `scrollcraft.js`, **0** `<video>` elements, and loads **`vendor/lenis.min.js`**, a third-party scroll library, in a project pitched as built *"rather than on an animation library."*
⭐ **The registry's own append-only rule kills the innocent reading:** *"A build that has been superseded stays in the table."* Supersession is explicitly covered, so absence is not staleness.
✅ **The control passes:** `nateherk.com` **is** a real build — 11 distinct `data-sc-*` attributes over 30 elements, 28 `sc-*` classes, `scrollcraft.js` from its own origin, plus a separate `glass.js` (bespoke page JS, exactly as the hard rule prescribes) and `data-sc-verify-state` — the harness's own hook — **live in production**.

**2. ⭐⭐⭐ The harness gates only what the eye cannot catch — and the one rule that decayed is one you can see.**
`shoot.mjs` implements four checks, all requiring a running browser: dead scroll, cues that never reach full opacity, **contrast on the composited page** (*"Sampling the video directly ignores every scrim, gradient and blend on top"*), and clips stuck on a poster (*"a poster looks exactly like a paused film"*). It checks **zero** grep-able rules — tested `em dash`, `—`, `transition: all`, `01 /`, `counter`, `scroll cue`: 0 hits each.
Commit `f6bf655` swept em dashes from **17 files, 96-for-96** by hand. **28 hours later** `e957985` added `device-diag.html` with an em dash in a **visible `<h1>`** — the tree's only one, still there 11 days on.
⭐ **And its location closes the loop:** `verify.md:238` admits *"Headless Chrome on the build box cannot reproduce an iPhone's video decoder, Low Power Mode, or touch"* — `device-diag.html` **is** the artifact built to cover that blind spot, a page a human opens on a phone. The rule the eye was supposed to catch went uncaught in the one file where a person is the instrument.
✅ **Two of three checkers do fail closed** — `doctor.mjs` (`:166`, 9 checks, each with a `fix` hint) and `worldflight-assert.mjs` (`:273`, 24 assertions) — and **both gate the environment.** The one measuring the *design* reports only, **by stated policy**: `verify.md:179` *"What the harness cannot tell you"* → *"**Whether the page means anything.** Six acts that each work and together say nothing is the most expensive failure available here."* That is **v250's behaviour independently repeated** — the line drawn exactly where decidability ends, and written down.

**3. ⭐⭐ It keeps the embarrassing rows, and that is what makes the disclosure real.**
`EXAMPLES.md:20-31` documents that its **first four builds all share one grammar with no signature move on any of them** — against a hard rule requiring one — names the person who caught it, and preserves the failing rows *"as-built, warts included"*, because *"rewriting a fingerprint row makes the file worthless."* The strongest **Pattern #83** instance the design cluster has produced, load-bearing precisely because an append-only rule makes deletion illegitimate.

---

## Provenance: a downstream mirror, openly so

Five tree-verified lines: CHANGELOG entries dated **2026-08-21**, before the root commit (08-22 10:34) · commit `82e6853` *"sync upstream engine work"* · citations to `lab/min-contrast.mjs` and `lab/worldflight-rig/`, paths absent from the tree · the upstream **named** — `OtherWorlds/Ultimate Websites/`, holding *"twelve builds and the live registry"* · and the production engine (56,688 B / 1,177 lines) matching **no commit** (nearest `e957985`, +345 B / +10 lines).

Not concealment — the v0.2.0 commit title is *"make the skill **portable**."* But the extraction is what produced the residue: `worldflight-assert.mjs:6` documents `node lab/worldflight-assert.mjs` for a file shipping at `scripts/`, and `lab/` never appears in the README's layout tree.

---

## 🔴 Security

- 🔴 **`serve.mjs:50` binds all interfaces while `:51` prints `http://localhost`** — `.listen(PORT, cb)` with no host.
- 🔴 **The traversal guard is a near-miss.** `:35` `!file.startsWith(ROOT)` lacks a trailing separator, so a **sibling** directory extending the root's name passes: with `ROOT=builds/perkform`, `/../perkform-secrets/…` resolves inside `builds/perkform-secrets/` and is accepted. Ordinary `../../etc/passwd` **is** blocked — they thought about traversal (`:34`). One-character fix: `ROOT + path.sep`.
- ⚠️ **An undocumented upload host.** `kie.mjs:27` POSTs base64 **local files** to `kieai.redpandaai.co` — on every `shot` (mandatory input image), every `--ref`, every `--tail`. The file's header documents `api.kie.ai` twice and never names it; the string appears **once in the whole tree, in code, in zero docs.**
- ✅ Key read from env/`.env`, sent as Bearer, **never logged**. ✅ **Supply chain nil** — no manifest, no lockfile, no postinstall, **zero npm packages added**. ✅ Cost published **with its own basis declared** (*"observed billing has run well under the published numbers"*) — the v281 discipline, unprompted.

---

## Why NO MINT

1. **Form-factor within a genre** — v168 · v204 · v218 · v250 · v274. **v274 is decisive in its own words:** *"A skill that adds a runnable checker is a stronger instance of the genre, not a new class."*
2. **Clean CONFIRMED Pattern #88 / 88c instance** — the refuse list *is* the pattern's vocabulary. Joins v75/v81/v82/v83/v85/v91/v105/v204/v218/v250. N-tally recorded, not self-incremented.
3. **Domain-not-capability** — the v212 tabularis precedent (+v196/v210/v197).
4. **Not world-first** — GSAP ScrollTrigger, Lenis, scrollytelling all precede.

Collision grep **CLEAN** — zero prior vault hits for the subject, author or `worldflight`.

**⭐⭐ RECORDED FOR THE AUDIT, NOT EXECUTED:** *"a design skill that numerically verifies its own rendered output"* is now **N=2, cross-author** — **v250** (`verify-treemap.py` checks *"its own chart does not lie"*) is N=1; scroll-craft is the **first to render in a real browser and measure composited pixels**, and the only one shipping its verification hook to production. A promotion is an audit act.

---

## Method

One read-only fleet (`wf_eb4fadf2-177`): **17 agents, 0 errors, 3 empty**, ~**2.24M** subagent tokens → with main-loop ≈**83% of the 3M soft cap** → **report-only mode entered per the binding rule, no further fan-outs.** The three empty dimensions were already hand-covered pre-launch, so coverage held. **Zero fabricated quotes.**

⭐ **Every fleet error was a count from summarising, fixed by enumerating** (taste.md 8→**11**, worldflight-assert 31→**24**, doctor.mjs 6→**9**) — v278 clause (g) replicating on my own fleet. **And I made two of the same error myself**: `grep -c` said **10** devices (truth: **9**, because §9 is explicitly *not* scroll) and three instruments said 17/15/13 registry rows (truth: **12**, plus a separate one-row worked example). **Both times the README was right and my instrument was wrong** — the inverse of the last four ships.

⚠️ **I corrected the fleet's headline.** Two agents independently asserted *"neither site contains any `data-sc-*` attributes"* — refuted by direct DOM measurement. Both had used markdown-converting fetches, which strip attributes.
⭐ **New method-rule candidate:** *agreement between two agents using the same instrument is correlated error, not corroboration.*

**Not overcome:** nothing executed (no Playwright/Chrome/ffmpeg/kie key; `node -e` permission-denied, so the traversal finding rests on a verified string property plus a code read); PERKFORM has no URL and was not found; stars unfetched (§37.4).

---

## Pilot

**⭐⭐ READ-AND-BORROW, then one genuinely $0 local run.** The install is unusually safe — **zero npm packages added** — but the value here is the *method*, not the tool: the vault does not build landing pages.

- ⭐⭐ **Rung 1 (30 min, the vault item):** copy the **append-only registry + differ-on-4-of-6 gate** into the wiki routine. This vault has a **catalogue of 52 §C rows whose whole purpose is collision detection** and no mechanical novelty test; scroll-craft has a six-dimension one with an explicit *"four against each row individually, not on average"* and a law against editing rows to make room. That is the vault's own §C problem, already solved, by a stranger.
- ⭐ **Rung 2 (20 min):** run `grep -rni "silent"` over the vault and over hireui. It is the v246 idea and it worked here immediately — 22 hits, all one failure class.
- ⭐ **Rung 3 (45 min):** lift *"what the harness cannot tell you"* verbatim into `hireui/evals/METHOD.md`. A candidate-matching eval has exactly this shape: the machine can prove a score computed and cannot tell you it means anything.
- **Rung 4 ($0):** `node scripts/doctor.mjs` in a scratch dir — read-only preflight, fails closed, no network, no key. The one thing worth *running*.

🔴 **NEVERs:** never run `serve.mjs` on an untrusted network (all interfaces, and a sibling-directory read) · never point `kie.mjs` at a candidate photo (undocumented upload host) · never cite AI Automation Society as a scroll-craft build · never quote a device or row count from this repo without naming the basis (**9** scroll devices of 10 sections; **12** registry rows plus 1 worked example).

---

**Suggested next action:** review and merge the chain — **`main` is at v226; v227→v281 plus this ship are outstanding.** Then ⭐ **Rung 1**: put the 4-of-6 fingerprint gate into the routine, because the vault's §C catalogue is the exact artifact it was designed for. ⚠️ **The ~v268 audit is now TWENTY-TWO SHIPS OVERDUE** and inherits from this ship the **N=2 self-verifying-design-skill row**, the **#88/88c** and **#83** instances, and the **correlated-error method rule**.

---

**Artifact:** https://claude.ai/code/artifact/4b040cf6-f310-4b54-b590-c568bdcdc3b6
