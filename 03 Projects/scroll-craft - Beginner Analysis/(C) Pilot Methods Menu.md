# (C) scroll-craft — Pilot Methods Menu

**v282** · `nateherkai/scroll-craft` · MIT · HEAD `677619e7`

**Overall pilot rating: ⭐⭐ READ-AND-BORROW, plus one genuinely $0 local run.**

The install is the safest in recent memory — **no `package.json`, no lockfile, zero npm packages added** — but the subject builds *scroll-driven marketing landing pages*, which neither the vault nor hireui needs. **The transferable asset is the method, not the tool.** Three of its mechanisms map onto standing vault problems better than anything shipped in the last twenty subjects.

**Fence for everything below:** clone from the author URL only · pin `677619e7` · scratch dir, never the vault or hireui working tree · no kie.ai key, no spend · never run `serve.mjs` on a shared network · hireui stays DESIGN-only per its CONSTITUTION (I-2/I-8, GitNexus-first, no LLM spend yet).

---

## A · Read (zero install, zero risk)

**A1 ⭐⭐⭐ Read `verify.md` §"What the harness cannot tell you" (:179-190).** Eleven lines. Three items: whether the composition is good, whether the motion is smooth, and *"**Whether the page means anything.** Six acts that each work and together say nothing is the most expensive failure available here."* The cleanest statement in the corpus of where an automated grader stops. **30 min.**

**A2 ⭐⭐ Read `CHANGELOG.md` as a genre specimen.** 33KB in which every rule is attributed to the build that broke it — `(saas)`, `(agency and nateherk both hit it; perkform and saas both had the hole)`. The README calls it *"worth reading on its own"* and it is right. Compare against the vault's own `_state/03c`: same idea, weaker attribution. **45 min.**

**A3 ⭐ Read `EXAMPLES.md:20-31`.** The author documents that his first four builds all collided, names the person who caught it, and keeps the failing rows. **10 min.**

**A4 Read `uniqueness.md` §2 (the eight grammars).** Each grammar *forbids* what the others require. A worked example of making a taxonomy mutually exclusive rather than merely labelled. **40 min.**

---

## B · Borrow into the vault (zero install — the highest-ROI cluster)

**B5 ⭐⭐⭐⭐⭐ THE VAULT ITEM: port the fingerprint gate to `_patterns/06` §C.**
The vault maintains **52 live §C rows** whose stated purpose is collision detection, and has **no mechanical novelty test** — every mint decision is a hand argument, and v182 caught a real anchor error (#23 at N=2 that was actually N=4) only by hand-grep. scroll-craft ships exactly the missing instrument:
- **six named dimensions** (grammar · nav · hero · act shape · close · signature move);
- a threshold stated to defeat the obvious cheat — `uniqueness.md:427` *"**Not** 4 of 6 on average across the table. Four against each row, **individually**"*;
- one dimension **free by construction** (the signature move is unique by definition, so the real test is 3 of the remaining 5);
- and a law: *"change the plan, not the log"* / *"rewriting a fingerprint row makes the file worthless."*

Vault translation: define 4–6 dimensions for a §C candidate (capability layer vs domain · primitive vs form-factor · N-anchor · corpus-first-for-surface vs world-first) and require a new mint to differ from **every existing row individually**. **This is the §C-2 catalogue's design brief, already written.** **60–90 min, zero install.**

**B6 ⭐⭐⭐ Adopt the append-only + supersession rule.** `EXAMPLES.md:270-271`: *"Rows are append-only. A build that has been superseded stays in the table, because the space it occupies is still occupied."* This is precisely the **v259 §C bifurcation** argument (23 rows past both §39 floors, retire pass deferred five times) **stated as a rule instead of a deferral** — and it is what let me kill the innocent reading of the missing AIS row. **20 min.**

**B7 ⭐⭐⭐ Run `grep -rni "silent"` over the vault and hireui.** The v246 idea, revalidated: 22 hits here, all one failure class, and they explain every piece of machinery in the repo. **20 min.**

**B8 ⭐⭐ Write the "gate the invisible, trust the eye for the visible" policy into `CLAUDE.md`.** scroll-craft built machinery for four properties only a running browser can see and left 18 grep-able rules to habit — a coherent policy, and its one failure landed exactly where predicted. The vault's converse question: *which of our rules are grep-able and ungated?* (The v281 AI-provenance policy item is one of them.) **30 min.**

**B9 ⭐ Steal the incident→rule changelog format** for `_state/03c`: name the artifact, what broke, and **which ship surfaced it**. **30 min.**

---

## C · Run it, locally, $0

**C10 ⭐⭐ `node scripts/doctor.mjs` in a scratch clone.** The one thing worth executing: read-only preflight, **fails closed** (`:166`), 9 checks each carrying a `fix` hint, no network, no key, no spend. It is also a small masterclass in diagnosing *misreporting* dependencies — a stripped ffmpeg reports a missing filter as a syntax error in *your* command. **15 min, $0.**

**C11 ⭐ `node scripts/workspace.mjs --ensure`** in the same scratch dir — creates a workspace and an empty registry so you can see the gate's data model. **10 min, $0.**

**C12 Read `template.html` + open it from a `file://` URL and watch it fail as designed** — the engine falls back to posters and *looks fine*. A 5-minute demonstration of the project's entire thesis. ⚠️ Do **not** fix it by running `serve.mjs` on a shared network (see E-class). **15 min, $0.**

**C13 ⚠️ NOT RECOMMENDED: a full build.** Needs Chrome + `playwright-core` + a full ffmpeg, and a real build wants a kie.ai key (~520 credits for a six-act page, ~2,000 for a ten-leg world flight, per `.env.example`). No vault or hireui deliverable justifies it.

---

## D · hireui / Goal #2

**D14 ⭐⭐⭐ Lift "what the harness cannot tell you" into `hireui/evals/METHOD.md`.** A candidate-matching eval has exactly this shape: the machine can prove a score was computed, is deterministic, and stayed inside its rubric — and **cannot** tell you the match means anything. Write the three-item limit section verbatim-in-structure, then name hireui's own three. Composes with the **RATIFIED candidate-LLM legibility ADR** (fixed + legible + audited + human-in-loop + eval-gated) and with **v249**'s `METHOD.md` and **v276**'s two-evaluators-reported-side-by-side discipline. **45 min, design-only.**

**D15 ⭐⭐ Borrow the *report-only vs fail-closed* split for Match-Explain.** scroll-craft fails closed on the **environment** and reports on the **judgement**. hireui's inverse is the correct one: fail closed on *legibility* invariants (no fabricated fields, every claim traceable to a CV span, no protected attribute in the prompt) and report-only on *quality*. Write it as an ADR amendment. **45 min, design-only.**

**D16 ⭐⭐ The composited-contrast lesson → the CV-rendering path.** `shoot.mjs:331-332` — a headline *"can pass on the poster and fail three frames later"*, so contrast must be measured on the composited render, per line, direction-aware. hireui renders candidate data over themed surfaces; the same class of failure applies to the **Candidate Detail** refactor's drifted tokens. Measure on the render, not on the token. **60 min.**

**D17 ⭐ The design floor as an accessibility checklist.** `taste.md:85-86` states correct WCAG AA (body ≥4.5:1, large ≥3:1, controls **and focus indicators** ≥3:1) plus the documented escape for pages that hard-cut between light and dark grounds — a real problem hireui's theming has. **30 min.**

**D18 🔴 NEVER: candidate imagery through kie.ai.** `kie.mjs` base64-uploads local files to **`kieai.redpandaai.co`**, a host named **once in the tree, in code, in zero documentation**. A candidate photograph must never traverse it.

---

## E · Method, security and hygiene

**E19 ⭐⭐⭐⭐ Adopt the correlated-error rule (new, from this ship).** Two fleet agents independently asserted *"neither site contains any `data-sc-*` attributes"* — both wrong, because both used markdown-converting fetches, which strip attributes. **Agreement between two agents using the same instrument is correlated error, not corroboration.** Add to `feedback_wiki_verify_independently_check_collisions`: a second opinion counts only if it uses a *different instrument*. **20 min.**

**E20 ⭐⭐⭐ Re-confirm v278 clause (g) — enumerate, never summarise.** Every fleet error this ship was a count (taste.md 8→**11**, worldflight-assert 31→**24**, doctor 6→**9**), and **I made two myself** (devices 10→**9**, registry rows 13→**12**). Both of mine were *false accusations against a correct subject*. Clause (g) should gain a clause: **when your count disagrees with the subject's, enumerate before publishing — the subject may be right.** **20 min.**

**E21 ⭐⭐ The one-character fix worth internalising.** `serve.mjs:35` `!file.startsWith(ROOT)` → a sibling directory extending the root's name passes. Correct form compares `ROOT + path.sep`. Grep hireui and any vault tooling for prefix-compared path guards. **30 min.**

**E22 ⭐ Provenance: measure at the divergence point (v241 D19), and note the inverse.** Here git **understates** the work — the CHANGELOG predates the root commit, the upstream is named (`OtherWorlds/Ultimate Websites/`), and the production engine matches **no commit**. v241 was the overstating case; this is the understating one. Both are answered by asking *where the work actually happened.* **20 min.**

**E23 ⭐ npm-security-check is a no-op here — record why.** There is nothing to check: no manifest, no lockfile, no postinstall, zero packages added. Worth logging as the corpus's cleanest install surface. **10 min.**

**E24 🔴 Fence check before any run.** `serve.mjs` binds **all interfaces** (`:50`, no host argument) while printing `http://localhost` (`:51`). Loopback-only networks, or bind explicitly. **5 min.**

---

## F · Pattern Library

**F25 ⭐⭐⭐ Record the N=2 for the audit (do not promote).** *"A design skill that numerically verifies its own rendered output"* — **v250** diagram-design is N=1 (`verify-treemap.py:305-313`, *"its own chart does not lie"*); **scroll-craft** is a cross-author N=2 and the **first that renders in a real browser and measures composited pixels** rather than checking its own drawing model, and the only one shipping its verification hook (`data-sc-verify-state`) to production. **A promotion is an audit act — recorded, not executed.**

**F26 ⭐⭐ Log the #83 exemplar.** `EXAMPLES.md:20-31` is the strongest honest-deficiency-disclosure the design cluster has produced, and it is load-bearing *because* an append-only rule makes deletion illegitimate.

**F27 ⭐ Log the #88/88c instance and the cluster count.** The design-skill cluster now reads v75 / v81 / v82 / v83 / v85 / v91 / v105 / v204 / v218 / v250 / **v282**. N-tally is audit bookkeeping.

---

## The ladder, if you do only three things

1. **B5** — port the 4-of-6 fingerprint gate to §C. The vault's §C catalogue is the exact artifact it was designed for. *(90 min, zero install)*
2. **B7** — `grep -rni "silent"` over the vault and hireui. *(20 min)*
3. **D14** — *"what the harness cannot tell you"* into `hireui/evals/METHOD.md`. *(45 min)*

Then **C10** (`doctor.mjs`, $0) if you want to have actually run something.
