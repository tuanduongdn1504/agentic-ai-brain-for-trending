# (C) Pilot Methods Menu — `dogriffiths/HeadFirstAndroid` (wiki v255)

**Verdict: READ-AND-APPLY. Nothing to install from the subject.**

The subject itself is a 2015 Java Android textbook's code. You will not adopt it, depend on it, or
run it in anger. Its value is in three things: a **verified legacy-modernization ground truth**, a
**clean zero-agent-surface control case**, and one **portable rule about labels** that lands
directly on a piece of vault debt five consecutive ships have asked you to pay.

**Rung 1 is already done and sitting in this folder.** Read that section first if you read nothing
else.

---

## Rung 0 — 25 minutes, zero installs

Read in this order. Each item earns its place.

1. **`README.md`, lines 91–160** *(5 min)* — the chapter 7–13 sections. Look only at the
   `images/chapNNimg.png` filenames against the chapter headings. Chapter 7 → `chap10img.png`,
   chapter 11 → `chap07img.png`. It looks like an off-by-N bug. **It is correct.** This is the
   whole Rung-1 lesson in ninety seconds, and it is the thing you will want in your hands when you
   decide what clause 2 of your verifier should test.

2. **`chapter13/Odometer/app/src/main/java/com/hfad/odometer/OdometerService.java`, lines 34–56**
   *(4 min)* — 22 lines. `onCreate()` calls `requestLocationUpdates` with no permission check. Then
   read **issue #25**, opened by `DuaneQ` on 5 April 2017, zero comments, still open. He was right.
   I reproduced his crash on Android 15 this afternoon. Nine years, four months.

3. **`_state/03c-projects-v61-v183.md`, lines 1–12** *(6 min)* — not the subject; your own vault.
   Read the v245 source-of-truth notice you wrote. It says the entries *"run through **v250**"*.
   The file holds **v254**. It also contains a paragraph explaining that it had already gone stale
   once before, at v247. **Read the sentence in it that begins "The fix for this file is not another
   prose note".** You wrote the specification for the script five ships ago, inside the file the
   script is meant to check.

4. **Any one `ApplicationTest.java`** *(3 min)* — 12 lines, zero test methods. Then know this: I ran
   `./gradlew connectedCheck` and it printed `BUILD SUCCESSFUL`, `tests="1" failures="0"`. The pass
   comes from a deprecated base class's inherited `testApplicationTestCaseSetUpProperly`, which
   asserts that the harness set itself up. **Green, and it tested nothing.**

5. **`git show 51511f9` on the `secondEdition` branch** *(7 min)* — `StartupTest.java`, 65 lines. A
   real Espresso test with a twenty-line Javadoc explaining what an instrumented test *is*, what
   `onView` and `allOf` and `withText` each do, and how to run it. It is the best-taught file in
   the repository. It was never merged, and the branch died three weeks later. **This is what the
   14 stubs should have been, and the author wrote it — on a branch nobody merged.**

---

## Rung 1 — the rung that pays. **Already written. ~40 minutes to adopt.**

### What it is

`(C) proposed-verify-vault-inventory.sh`, in this folder. It is the script recommended at **v250,
v251, v252, v253 and v254** and never written — I checked, and `bin/` did not exist.

I did not just specify it. **I wrote it, ran it against your vault, found real defects, found two
bugs in my own first draft, fixed them, and re-ran.** Its output is below, unedited.

To adopt:

```bash
mkdir -p bin && cp "03 Projects/HeadFirstAndroid - Beginner Analysis/(C) proposed-verify-vault-inventory.sh" bin/verify-vault-inventory.sh && chmod +x bin/verify-vault-inventory.sh && bin/verify-vault-inventory.sh
```

It is `awk`/`sed`/`grep` only — no `python3` (SIGKILLed in this sandbox), no `node` (inline `-e` is
permission-denied), and `/usr/bin/grep` explicitly because `command grep` does not bypass the
`ugrep` shim (v253). Exit 0 = clean, exit 1 = at least one FAIL.

### What this subject contributed: **the correction to clause 2**

v254 specified clause 2 as *"filename-label-vs-newest-entry."* **Implemented literally, that clause
is wrong** — and HeadFirstAndroid is the counter-example that proves it. Its README maps chapter 7
to `chap10img.png`. A "label must match content" check flags that as a defect. It is not a defect;
the images were named under an earlier draft numbering and the README compensates at the reference
site. The "fix" breaks every image in the README.

So clause 2 does not test *does the label match the content*. It tests **is the lag declared**:

```
PASS   label == content                                    (no lag)
PASS   label != content  AND a source-of-truth declaration exists in the file's first 40 lines
FAIL   label != content  AND nothing says so
```

That is rule **D32** (v245, from `unslothai/unsloth`'s `BUDGET.md`) promoted from prose into a
predicate, plus the rule this ship adds:

> **A stale label is safe when DECLARED and dangerous when merely COMPENSATED.**

Griffiths reached correctness without the declaration. It works today and it survives only until
someone helpful tries to tidy it up. Your `03c` reached correctness *with* the declaration, which
is why the wrong filename has been harmless for 71 ships.

### And the clause I did not expect to need: **2b**

If a file carries a declaration that states a version, **that version is a claim and needs checking
too.** The script found this on its first honest run:

```
FAIL  03c-projects-v61-v183.md: THE DECLARATION IS ITSELF STALE
      — it says 'through v250' but the file holds v254
```

Your v245 notice has now gone stale three times: v247 → v250 → v254. The notice's own text
documents the first two. **The D32 fix is working exactly as v245 predicted — the drift is harmless
and self-diagnosing — but nothing was diagnosing it.** Now something does.

### What it actually found (verbatim, unedited)

```
== CLAUSE 1 — bidirectional chapter inventory (v250) ==
        indexed in CLAUDE.md: 10 | on disk: 14
  FAIL  named in CLAUDE.md but ABSENT from _state/:
        03c-projects-v61-v177.md
  FAIL  present in _state/ but NEVER MENTIONED in CLAUDE.md (the v240 blind spot):
        license-decision-2026-04-28.md
        public-release-decision-2026-04-28.md
        publishing-strategy-2026-04-28.md
        v60-mini-audit-pre-registration.md
        v60-mini-audit-results-2026-05-07.md

== CLAUSE 2 — label lag must be DECLARED, not merely compensated (v250 + v255) ==
  PASS  03c-projects-v61-v183.md: label v183 lags content v254 — lag is DECLARED (D32 satisfied)
  FAIL  03c-projects-v61-v183.md: THE DECLARATION IS ITSELF STALE — says 'through v250', file holds v254
  WARN  03a / 03b / 03d / 04 / 05: no vNNN found in entry headings

== CLAUSE 5 — CLAUDE.md size budget (v253) ==
        CLAUDE.md = 200352 bytes (budget 200000, ~50088 tokens)
  FAIL  CLAUDE.md is 352 bytes over budget
        accreted head blocks (lines starting **★): 30
  WARN  30 head blocks — demote the oldest to _state/03c (they duplicate it)

== CLAUSE 6 — dated-stamp freshness (v253) ==
  PASS  CLAUDE.md's currency marker (v254) is not behind _state (v254)

== CLAUSE 7 — assert a count against a count (v254) ==
        CLAUDE.md claims §C live standalones = 51
  WARN  not machine-derivable from _patterns/06 without a stable row marker
        distinct 'N confirmed patterns' values in CLAUDE.md: 46
  PASS  the confirmed-pattern count is stated consistently

  5 FAIL   3 WARN
```

### Reading the results

| Finding | Real? | Fix |
|---|---|---|
| **`03c-projects-v61-v177.md` named in `CLAUDE.md`, does not exist** | **Yes** | A dangling reference left over from the `-v177` → `-v183` rename. One line in the "Where the detail lives" paragraph. **This is v254's rename clause firing through clause 1** — exactly the class that cost me two missed ships at v254. |
| **5 `_state/` files never indexed in `CLAUDE.md`** | **Yes** | The **v240 inventory rule, live in your own vault**: an index↔content check cannot see what is missing from the index. Five real decision documents are invisible to the chapter index. Add them, or add a line saying the index covers chapter files only. |
| **The v245 declaration says v250, file holds v254** | **Yes** | Update the number — and now it is checked, so it stays updated. |
| **`CLAUDE.md` 352 bytes over, 30 accreted ★ head blocks** | **Yes, advisory** | The 200 KB budget is *mine*, not yours — treat the byte count as a tripwire and **30 head blocks** as the real signal. v238 compacted this after every deep-dive workflow failed *prompt-too-long*. It is regrowing. |
| **5 chapters "no vNNN found in entry headings"** | **Honest WARN, not a defect** | Only `03c`'s newer entries use `## v254 — …` headings; the older chapters use `### <project> - Beginner Analysis` with no version. So no automated label check is possible for them. Either adopt the `## vNNN — <subject>` heading convention going forward, or accept that clause 2 covers `03c` only — which is the only chapter that actually accretes. |

### Two bugs I found in my own first draft, both on your recurring-error list

1. 🔴 **The first draft resolved the vault root with `cd "$(dirname $0)/.."`.** Run from this project
   folder that landed in `03 Projects`, where there is no `CLAUDE.md` and no `_state/` — and
   **clause 1 reported PASS**, because `comm` found no difference between two *empty* sets. A green
   check that checked nothing: this ship's own §D.6 finding, reproduced inside the tool built from
   it. Fixed by resolving the root **by signature** (walk up until a directory has both `CLAUDE.md`
   and `_state/`) and by adding a **`nonvacuous`** guard so any clause that examined zero items
   FAILs instead of passing. `Clause 3` now prints `SKIPPED`, not `PASS`.
2. 🔴 **`grep -o 'v[0-9]\{1,4\}'` over the whole file body.** Two errors at once: it reported the
   newest version *mentioned* rather than *held*, and with no word boundary it matched **`v89`
   inside the GitHub username `luongnv89`**, making `04-projects-v30-v39.md` appear to hold a v89
   entry. Fixed by parsing **heading lines only** with a word boundary — which is what your own
   `03c` notice specified all along (*"the newest `**vNNN` entry it actually contains"*).

**Both bugs were the same bug the subject teaches: a check that reports success without having
looked.** If you adopt nothing else from this ship, adopt the `nonvacuous` guard.

### Then write the aim rule into `CLAUDE.md`

Three lines, joining the two already there:

> - **v250:** a gate's *aim*, not its quality, decides what rots.
> - **v254:** a **declaration** is a form of aim — before adding a check, ask what you have never declared.
> - **v255:** a stale label is **safe when declared** and **dangerous when merely compensated**. And a declaration is itself a claim: check its number too.

---

## Rung 2 — 0–90 minutes, optional, pick one

### (a) The Android screening rubric — the Goal #2 item *(60–90 min)*

The strongest connection to hireui, and it is the one thing here that becomes an asset rather than a
note. This repository is a ready-made set of judgement questions **with known answers**, because I
verified them by execution:

| Ask a candidate | Correct answer | Why it discriminates |
|---|---|---|
| `SQLiteOpenHelper`, `RelativeLayout`, `ListView` | **Still supported.** Old-fashioned, not wrong. | A weak candidate calls everything old "deprecated" |
| `ActionBarActivity`, install-time permissions, `android.app.Fragment` | **Genuinely obsolete** | Requires knowing *which* things actually moved |
| `AsyncTask` | Deprecated in **API 30 (Android 11, 2020)** | A date, not a vibe |
| "This app builds. Will it install on a modern phone?" | **No** — `targetSdk 21` < the OS floor of 24 | Separates build-literacy from ship-literacy |
| "Chapter 13's notification doesn't appear. No crash. Why?" | Channels mandatory at `targetSdk ≥ 26`; the post is **silently dropped**, one line in logcat | **The best question here.** Debugging a silent failure is the actual skill |

Deliverable: one page in `hireui/interview-rubrics/`. The last row is worth the whole exercise —
*"here is a system that fails silently, find out why"* is a far better signal than any trivia.

### (b) The modernization fixture — honestly, **not yet** *(defer)*

Tempting: 14 comparable targets, MIT, no network, and a **measured ground truth** (3 edits to
build, 4 to install and run). But **you cannot verify a migration succeeded.** There are no real
tests; `connectedCheck` returns green on an empty stub, so the obvious success signal is worthless.
I verified the 14 apps by launching each one and *looking at it*.

To make this a benchmark you must first write the oracle: one Espresso assertion per app that the
main screen shows what it should. The repository contains exactly one file demonstrating how — and
it is on the abandoned branch. **Good fixture, not yet a benchmark.** Do (a) instead.

### (c) The one-line reading list *(10 min)*

`dogriffiths/HeadFirstAndroid3rdEd` — 6 commits, 19 chapters, Kotlin, last touched 2022-01-15 by
**Dawn Griffiths**, who has zero commits in the repository we just analysed. **134★ / 78 forks**
against this repo's **505★ / 313 forks**. The obsolete edition outranks the current one 3.8× in
stars and 4.0× in forks, and points nowhere.

---

## What to install

**Nothing from the subject.**

From this ship: one shell script that is already written, already run, and already found five
failures in your own vault.

---

## Hard fences

🔴 **Do not clone this and expect `./gradlew` to work.** It cannot configure. With a current JDK you
get `Could not determine java version from '21.0.10'`; with JDK 8 you get
`Could not find com.android.tools.build:gradle:2.3.2` — and **AGP 2.3.2 exists on no live public
repository** (404 on Google's Maven, Maven Central, `maven.google.com`, `plugins.gradle.org`).

🔴 **Do not treat this code as current Android practice.** It is the **first** edition (2015, Java).
The book in print is the **third** (2021, Kotlin, Jetpack Compose). Nothing in this repository says
so.

🔴 **Do not put this in front of a candidate as a modern-Android reference.** As a *deprecation
exercise* (Rung 2a) it is excellent. As an example of how to write Android in 2026 it is actively
misleading.

🔴 **Do not "fix" the README's image references.** They are correct. Renumbering them to match the
filenames breaks all 14 images. Same for: deduplicating the 14 identical wrapper jars, unifying
`appcompat` on 21.0.3 (chapter 14 needs 22.2.1), or "implementing" the 14 empty test stubs.

🔴 **Do not trust `./gradlew connectedCheck`.** It returns `BUILD SUCCESSFUL`, `tests="1"
failures="0"`, having tested nothing.

⚠️ **The 14 committed `gradle-wrapper.jar` binaries are unverifiable** — sha256
`e2b8212…824a14`, all identical, and `./gradlew` *executes* them. I could not obtain an
authoritative reference hash. Almost certainly the genuine Android Studio wrapper; "almost
certainly" is not "verified." If you do run the wrapper, do it in a scratch directory.

⚠️ **Never cite this repository's star or fork figures as velocity.** The GitHub API is mocked in
this environment (§37.4); 505 / 313 / 134 / 78 are all page-stated.

⚠️ **Do not repeat the fleet's numbers.** Not `HttpGetTask.java` (**does not exist** — the real file
is `DrinkActivity.java:80`). Not "the notification code is in Odometer" (it is in **Joke**). Not
"Joke crashes with `IllegalArgumentException` on API 26+" (**it does not crash — it fails
silently**). Not "~1.5k stars" (that figure bled out of the injected `CLAUDE.md` shim from v253; the
real page-stated figure is **505**). Not "28 ApplicationTest files" (**14**). Not
"`android.app.Fragment` in chapters 7, 8, 9" (**7, 8, 10, 14** — chapter 9 has none).

---

## Time-boxed verdict

**READ-AND-APPLY.** Rung 0 is 25 minutes and three of its five items are about your vault rather
than the subject. Rung 1 is the payoff and it is already written, run, and validated — it turns
five ships of accumulated recommendation into a 40-minute copy, and it found a dangling file
reference, five unindexed state files, a stale declaration, and a regrowing shim on its first honest
pass. Rung 2a is the only item that produces a lasting asset, and it exists because this repository
happens to be a perfectly preserved museum of exactly the judgement calls a senior mobile hire has
to make.

**Nothing here is worth installing. One thing here is worth forty minutes, and it has been worth
forty minutes since v250.**
