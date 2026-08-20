# (C) Verdict — `dogriffiths/HeadFirstAndroid` (wiki v255)

**2026-08-20 · GOAL-ALIGNED INCLUDE 3/4 · NO MINT · counts 46/11 UNCHANGED**

---

## 1. The headline

**Four one-line edits take a nine-year-dead repository from "cannot configure" to eight of nine
apps running on Android 15 — and the ninth crashes for the reason a reader wrote down in April 2017
and nobody ever answered.**

Measured, not inferred:

| State | Outcome |
|---|---|
| as shipped, modern JDK | `Could not determine java version from '21.0.10'` |
| as shipped, JDK 8 | fails in **6.2 s**: `Could not find com.android.tools.build:gradle:2.3.2` |
| **+3 edits** (`google()`, AGP → 3.0.0, Gradle → 4.1) | **14 / 14 build**, 14 signed APKs |
| install on API 35 | **0 / 14** — `must target at least SDK version 24, but found 21` |
| **+1 edit** (`targetSdkVersion 24`) | **14 / 14 install**; **8 / 9 run** |
| the ninth | `SecurityException … does not have ACCESS_FINE_LOCATION` = **issue #25, open since 2017-04-05, zero comments** |

### Why this headline and not the others

Three other findings were candidates, and each is real:

- **The deliberately-stale image filenames**, where the obvious fix is the bug (§E of the Deep
  Dive). Elegant, and the closest analogue to the vault's own `-v183` problem — but it is a lesson
  *for the reader of this wiki*, not the most important fact *about the repository*. A learner who
  clones this repo never reaches it, because they hit the build first.
- **`connectedCheck` returns green on tests that test nothing.** Genuinely sharp, fully executed,
  and it is kept as a first-class finding below. It loses the headline only because it describes
  what the repository *fails to teach*, whereas the build/run chain describes what it *is*.
- **Android displays the deficiency disclosure the README withholds.** The best single image in the
  ship. It is a consequence of the headline rather than a rival to it.

The build-and-run chain wins because it is the first thing anyone hits, it is completely executed,
and it carries the intellectual payload: **the code was never the problem.**

---

## 2. Goal-alignment (Phase 0.9)

### (a) Author — **FAIL**

David Griffiths (`dogriffiths`) — O'Reilly author, founder of HereScreen Ltd, 54 public
repositories, sole committer here (152 of 152, 100%). Dawn Griffiths is a credited book co-author,
holds copyright in `LICENSE.txt`, and has **zero commits**.

Per routine **§41**, (a) passes only on a declared Anthropic affiliation or a registered (a)-7
vendor-direct source. A notable, publicly-disclosed individual author is explicitly *not* a pass.
**FAIL, cleanly.**

> One fleet agent justified this FAIL by asserting he is "NOT a disclosed individual with a public
> GitHub identity beyond this repo." That reasoning is wrong — he is a very publicly disclosed
> individual. The verdict is unchanged; §41 makes disclosure irrelevant, not absent.

### (b) Goal-relevance — **MODERATE**

**The honest weak case first.** This is the companion code to a 2015 Java Android textbook. It is
not agent infrastructure, not an agent skill, not MCP, not orchestration, not memory, not a
capability layer. Of 254 prior ships, essentially all concern AI coding agents; this is none of
them. **OFF-GOAL CAPTURE is a defensible reading and is recorded here as the reviewable
alternative.**

**The strong case, three threads that are real rather than manufactured:**

1. **A legacy-modernization fixture with verified ground truth (Goal #1).** The corpus talks
   constantly about what coding agents can do; it has never once handed one a dead build and
   checked. This subject is small (5,689 lines of teaching content), MIT, self-contained,
   network-free, secret-free, has 14 comparable targets, and now has a **measured two-level ground
   truth**: three edits to build, four to install and run. That is a usable fixture, with one
   named gap (no oracle — see §5).
2. **Agent legibility at the zero end (Goal #1).** The corpus has catalogued dozens of subjects
   *by* how well they serve agents. This is the control condition: **zero** agent-facing surface,
   no CI ever, and six specific places where the naive fix is wrong. Pattern #12 has never had a
   clean negative instance to sit against its positives.
3. **Android deprecation as a screening rubric (Goal #2).** The live mobile-engineer-interview
   thread needs concrete material. This repository is a ready-made set of judgement questions with
   *known* answers: which of these is genuinely obsolete (`ActionBarActivity`, install-time
   permissions, `android.app.Fragment`), which is merely old-fashioned but still supported
   (`SQLiteOpenHelper`, `RelativeLayout`, `ListView`), and which failure is silent rather than
   loud. Distinguishing "deprecated" from "wrong" is exactly the judgement a senior mobile hire
   should have — and it is the same hook the vault used at **v191**, whose value was recorded as
   *"L24's flagship fairness example is literally hiring bias → the hireui responsible-AI gate
   spec."*

**Rating: MODERATE.** Under routine **§40**, an operator-requested subject touching a live goal
thread with (b) MODERATE+ is **GOAL-ALIGNED per operator direction**, no override consumed, no §35
pressure, OFF-GOAL recorded as the reviewable alternative. The request — *"build LLM wiki for
https://github.com/dogriffiths/HeadFirstAndroid"* — is operator direction.

> **⚠️ Correcting the fleet on precedent, because both the critic and the anti-critic got this
> backwards.** The critic argued this should be OFF-GOAL because *"v191 (AI-For-Beginners, a
> Microsoft textbook) was rated NO MINT on grounds domain-not-capability… By v191's logic, this
> should be OFF-GOAL CAPTURE"*, and the anti-critic **UPHELD** that point as *"structurally sound."*
> Both conflated two orthogonal decisions. **NO MINT** is a pattern-library ruling; **OFF-GOAL** is
> a Phase-0.9 intake ruling. `05 Skills/llm-wiki-routine-v2.7.md` names v191 explicitly:
>
> > *"**Precedents now covered by §40**…: GLM-5 v176, DeepSpec v186, **AI-For-Beginners v191
> > (curriculum)**, TimesFM v193, meetily v196, **mlsysbook v197 (textbook)**. Under §40 these are
> > simply **GOAL-ALIGNED** (goal-adjacent, operator-requested, (b) MODERATE+), with the OFF-GOAL
> > alternative on record."*
>
> v191, v197 and v220 were each **GOAL-ALIGNED *and* NO MINT**. This ship follows that shape
> exactly. The critic's underlying caution — do not inflate (b) — is sound and is why (b) is
> MODERATE and the alternative is on the record.

### (c) Rigour / quality of the subject as a source — **STRONG**

A canonical, professionally produced, MIT-licensed teaching corpus. The curriculum is measurably
well-designed (§B of the Deep Dive: the increments match the chapter titles). The code is clean and
consistent across 67 files. Reader-reported bugs were fixed and credited by name.

### (d) Novelty for this corpus — **STRONG**

Zero corpus recursion. A case-insensitive grep over **5,047,488 characters** of vault state
(`CLAUDE.md` + `_state/*.md` + `_patterns/*.md`) returns:
`HeadFirstAndroid` **0**, `Head First` **0**, `dogriffiths` **0**, `Griffiths` **0**, `AsyncTask`
**0**, `gradle` **0**, `jcenter` **0**.

The corpus's **first Android-domain subject**, **first book/textbook code-companion**, **first
Gradle/JVM-Android build subject** — and **the first subject in 255 ships that was built, installed
and executed on real hardware.**

### Tier

**GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) MODERATE · (c) STRONG · (d) STRONG.
OFF-GOAL CAPTURE recorded as the reviewable alternative.
Tier **T3 Education**, joining v74 / v191 / v197 / v220.

---

## 3. NO MINT

**Counts UNCHANGED: 46 confirmed patterns / 11 CONFIRMED Library-vocab / 51 live §C standalones /
surface ≈58.**

Four candidate §C standalones were considered and all four declined:

| Candidate | Declined because |
|---|---|
| "Book/Textbook Code-Companion Repository as a Frozen Pedagogical Corpus" | **domain-not-capability** — the decisive ground. §C vocab is tool/capability-shaped. Precedents: mlsysbook v197 (*"a single-domain educational curriculum is not a recurring capability class"*), AI-For-Beginners v191, little-book-rl v220, LLMs-from-scratch v74. The T3-education sub-archetype candidates v111/v113 were **retired at the v151 audit** under §28.3 after ~40 wikis at N=1. |
| "Progressive-Snapshot Curriculum Repository" | form-factor-within-a-genre, not a capability; and not world-first — every textbook with code does this. The claude-cookbooks v102 cookbook-not-minted precedent applies. |
| "Legacy Build Artifact Whose Sole Blocker Is a Repository-Coordinate Change" | describes a **status**, not a capability. Also factually narrowed by this ship's own measurement: the blocker is *not* a coordinate change — AGP 2.3.2 exists nowhere, so the plugin must be upgraded. |
| "Load-Bearing Stale Label, compensated at the reference site" | a **portable rule, not a pattern**. The vault distinguishes minted patterns from D-class rules. This belongs with **D32**. |

**§28 anti-inflation** independently blocks all four at 51 standalones.
**Pattern #68 (Awesome-List-Genre) is out of scope** — this is not a list, index, or registry.

### Instance effects on confirmed patterns

| Pattern | Effect | Evidence |
|---|---|---|
| **#12** agent-facing surface | **NEGATIVE instance — the corpus's cleanest** | 0 of 578 filenames match any agent-facing convention; no CI ever, on any branch |
| **#83** honest-deficiency disclosure | **NEGATIVE instance** | README discloses nothing about edition, age, target API or build viability; **Android supplies the disclosure instead** |
| **#66** supply chain | **negative data-point** (victim, not exemplar) | `jcenter()` only; `compile`; 14 unverified committed wrapper jars |
| **#57** corpus recursion | **ZERO** — a rare no-recursion ship | 0 hits across 5.05 M chars |
| **#52** viral velocity | **N/A** | API mocked (§37.4); 505★ is page-stated |
| **#19** ecosystem-portfolio | **not applicable** | single author, single-purpose companion repo |
| **#88** anti-slop | **not applicable** | — |

### Recorded, not self-executed

- **A new D-class rule (D40 candidate), extending D32:** *a stale label is safe when it is
  **declared** and dangerous when it merely happens to be **compensated**.* v245 adopted D32 —
  declare which copy wins, inside the copy that loses — and applied it to `_state/03c`. Griffiths
  achieved the same correctness with **no** declaration, which works until someone helpful arrives.
  This is an independent, cross-domain **N=2** on the D32 phenomenon: same disease, one declared
  fix, one undeclared one. A rule addition is an audit act; recorded here.
- **A new displacement-vs-divergence distinction** (Deep Dive §H) — offered as a framing for the
  overdue audit, not as a mint.
- **A refinement of the v246 `silent`-detector rule** — see §6.

---

## 4. Defect ledger, ranked by harm to a learner today

Excluded as **non-defects** (both established, both would be broken by "fixing" them): the absent
`chapter05` directory, and the stale image filenames.

| # | Defect | Evidence | Who it hurts |
|---|---|---|---|
| 1 | **Nothing tells the reader this is the obsolete first edition.** No pointer to `HeadFirstAndroid3rdEd`, which holds the Kotlin code for the book currently in print. Zero hits for every variant of "second/third edition", "Kotlin", "3rdEd". | grep over README + LICENSE, all branches | **Everyone.** And it is the most-discoverable Head First Android repo: **505★ / 313 forks vs 134★ / 78 forks — 3.8× the stars and 4.0× the forks of the current edition.** |
| 2 | **The build cannot configure as shipped**, and the error names a repository that answers HTTP 200. | executed; §C | Everyone who clones it |
| 3 | **Issue #25 is correct, reproduced, and unanswered since 2017-04-05 with zero comments.** | executed stack trace | Chapter 13 readers |
| 4 | **`connectedCheck` reports BUILD SUCCESSFUL, `tests="1" failures="0"`, having tested nothing** — the pass comes from a deprecated base class's `testApplicationTestCaseSetUpProperly`. | executed | Any reader who concludes the repo is tested; any metric that counts tests |
| 5 | **Notifications fail silently at `targetSdk ≥ 26`** — `No Channel found … channelId=null`, no crash, no notification. | executed | Anyone modernizing chapter 13 |
| 6 | **No build instructions of any kind.** No JDK, no SDK, no prerequisites, no "open this in Android Studio". | grep: all 20 "build" hits are chapter prose | Beginners, who are the entire audience |
| 7 | **12+ open issues, all 2016–2017, none answered.** #24, #23, #19, #17, #16, #15, #14, #13, #12, #11, #9 alongside #25. | rendered issue list | Readers who hit a real bug and search |
| 8 | **Two PRs open since 2015** (#1, #2 — eleven years). A third, #18, was opened 2016-11-24 and **closed by its own author on 2023-11-30** after seven years of silence. | rendered PR pages | Contributors |
| 9 | **17 months of broken README images** (2017-05-08 → 2018-10-16), fixed only after issue #29 was filed. | gh-pages history + issue close date | Historic |
| 10 | **46% of the repository is scaffolding** repeated 14×, incl. 140 IDE files and 14 identical committed jars. | 266 / 578 | Anyone diffing or reviewing |
| 11 | **The 14 committed `gradle-wrapper.jar` binaries are unverifiable.** `./gradlew` executes them. | sha256 computed; no reference hash obtainable — **NOT ESTABLISHED** | Anyone who runs the wrapper |
| 12 | **The `secondEdition` branch holds the only real test** (65-line Espresso, beautifully documented) plus sonar/coverage config, never merged, abandoned 2016-09-01. | `git show 51511f9` | Everyone — it is the best-taught file in the repo |

---

## 5. What is genuinely good

- The curriculum is **measurably** well-designed — the diffs between successive app copies match
  what the chapter titles promise (ch11 adds the DB helper *only*; ch12 does the 258 lines of
  wiring).
- The early commits are a **page-by-page checkpoint trail** (*"Up to Test Drive on page 16"*) so a
  reader can `git checkout` to the page they are on. Abandoned after chapter 4, and a shame.
- **Chapter 14's Material Design app renders correctly on Android 15** — RecyclerView, CardViews,
  navigation drawer, ShareActionProvider. Screenshot in the folder.
- Commented-out **Log → Toast → Notification** stages preserved in one file, each labelled, so all
  three stages of the chapter are visible together.
- Clean, consistent, unclever code; correct listener teardown in `OdometerService.onDestroy()`.
- Reader-reported bugs fixed **and credited by name** (`j8s0n`, `@tomjohnson1492`).
- Zero broken internal links; `local.properties` correctly excluded; wrapper `distributionUrl` is
  https.
- AGP's two warnings during the repaired build are exemplary: loud, specific, and they name the
  remedy.

---

## 6. The synthesis: displacement, not divergence

v250 → v254 were all one story with five costumes: a check that was missing, misaimed, or
unenforced, and an artifact that drifted from its own claims. v254 sharpened it to a rule — *the
machinery went to the certainty and not to the risk; a declaration is a form of aim.*

**This subject inverts the sequence, and that is the reason it was worth a ship.** It has no
machinery at all — zero CI in eleven years — and **it did not drift.** Not one byte has changed
since 2017-05-23. Measured against its own claims it is *more* faithful than any of the last five
subjects: the curriculum is coherent, the links resolve, the images load, the chapter mapping is
right. And it is nearly unusable, because JCenter closed, Google relocated its Maven coordinates
and left AGP 2.x behind, and Android made permissions run-time, then channels mandatory, then set
an install floor at targetSdk 24.

- **Divergence** is defended by a gate.
- **Displacement cannot be gated.** No predicate over these 578 files is true in 2017 and false in
  2026. The bytes are identical; only their meaning changed.

The only available defence is far duller than a gate: **date your work.** Not "this is deprecated"
— unknowable — but *"first edition; targets API 21; last verified May 2017; current edition's code
is over there."* Six lines, free in 2017, worth a great deal now.

**Refinement of the v246 `silent` detector — third consecutive null, and the rule's third
correction.** `grep -rni "silent"` returns **0**. v253 explained its null as *"the detector's domain
is artifacts that RUN"*; v254 refuted that (it had a runtime and still returned zero) and proposed
*"artifacts whose authors have DEBUGGED them."* Griffiths debugged these apps page by page — the
commit log proves it — and the grep is still zero. So: **the detector finds artifacts whose authors
wrote down their reasoning about failure.** Nothing more. And here the null sits directly on top of
a genuine silent failure (§4 #5) that was **invented three months after the last commit**. You
cannot document a failure mode that does not exist yet.

---

## 7. Error ledger

**22 caught. 6 mine, all corrected before shipping.**

**Mine:**
1. ⚠️ I hypothesised that `gh-pages`'s `images/` now serves **second-edition** artwork. **Wrong** —
   hash-comparing all 14 blobs against `ed1/images/` showed them identical. Correcting it produced
   the real finding (the 17-month outage, 2017-05-08 → 2018-10-16).
2. ⚠️ I read the chapter→image mapping as a **rotation bug**. **Wrong** — I opened the images;
   `chap10img.png` is fragments-on-a-tablet (ch7) and `chap07img.png` is the SQLite helper (ch11).
   The mapping is correct and the filenames are stale, which is a better finding.
3. ⚠️ I predicted the fix was **one line** (`google()`). **Wrong, and I proved it wrong** — AGP
   2.3.2 is 404 on every live repository. The measured fix is three edits.
4. ⚠️ I flagged `./gradlew connectCheck` in the ed2 test's Javadoc as a **typo**. **Wrong** —
   Gradle resolves camelCase task abbreviations; I ran it and it executed
   `connectedDebugAndroidTest`.
5. 🔴 A `for pair in "a b"; set -- $pair` loop **silently produced zero diffs** because zsh does not
   word-split there, so `diff` ran with an empty second argument. I nearly recorded "the
   progressive snapshots are identical," which is spectacularly false. Caught by noticing the
   echoed label was blank.
6. 🔴 My first notification test reported **"no crash"** — because the OS's *"built for an older
   version of Android"* dialog was above the app and swallowed the tap. **The experiment never
   ran.** Caught only by taking a screenshot. A false negative from an unrun test is exactly the
   class this corpus keeps recording.

**The fleet's (16), from 20 agents:**
7. 🔴🔴 **Fabricated file and code.** The deprecation census reported
   `chapter12/Starbuzz/…/HttpGetTask.java` containing
   `public class HttpGetTask extends AsyncTask<String, Void, String>`. **The file does not exist.**
   The real usage is `DrinkActivity.java:80`, `private class UpdateDrinkTask extends
   AsyncTask<Integer, Void, Boolean>` — different name, different generics, different file, and a
   nested private class rather than a top-level one.
8. 🔴 **Misattributed the notification code to Odometer.** It is in
   `chapter13/Joke/…/DelayedMessageService.java:57`. I had read `OdometerService.java` in full;
   it contains no notification code at all.
9. 🔴 **Claimed Joke "crashes with IllegalArgumentException on API 26+".** **Refuted by
   execution**: no crash; the notification is silently dropped.
10. 🔴 **Context bleed — again.** The pattern agent wrote *"Stars are page-stated (~1.5k at the time
    of the clone)."* The real page-stated figure is **505**; ~1.5k is **v253's** number, from the
    injected `CLAUDE.md` shim. This is the third consecutive ship where a figure has leaked out of
    the shim into a finding.
11. 🔴 **The critic and the anti-critic both got the v191 precedent backwards** (§2) — one asserted
    it, the other **UPHELD** it without checking the routine text that names v191 as GOAL-ALIGNED.
    The adversary-over-critic stage caught other things but not this.
12. 🔴 **"28 identical empty ApplicationTest.java files"** — actual 14. Caught by that lens's own
    verifier.
13. 🔴 **`android.app.Fragment` in "chapters 7, 8, 9"** — actual 7, 8, 10, 14. Chapter 9 has none.
    Caught by that lens's verifier.
14. 🔴 **The census had no network** and self-marked every API-status claim "NOT VERIFIED", then
    published a confident per-chapter verdict table anyway — built on a chapter mapping that looks
    like the *second* edition's ordering.
15. ⚠️ **The buildchain agent's recipe was wrong at 95% stated confidence** — *"add `google()`,
    keep AGP 2.3.2"*, which I executed and it fails. Its own headline finding (Gradle 3.3 cannot
    parse `21.0.10`) was **correct and valuable**, and I would not have found it, having reached
    for JDK 8 immediately.
16. ⚠️ The critic's *"most likely wrong claim"* (AsyncTask deprecated 2019, not 2020) was **right**:
    API 30 / Android 11 is 2020.
17. ⚠️ An "Open Issues (4 total)" summarisation that conflicts with the badge's 14 and with a
    later enumeration of 12. **Unresolved and reported as such** — see below.
18. ⚠️ Claimed *"jcenter shut down in 2024"* with no citation. The observable fact is the redirect
    to Maven Central; the date is not established here.
19. ⚠️ Asserted *"Modern Google Play forbids `com.android.support`"* — not established.
20. ⚠️ Rated Google Play's minimum as *"likely 34+, NOT ESTABLISHED"*; it is **36** for new apps and
    updates from 2026-08-31, cited.
21. ⚠️ The critic argued the goal-alignment rating was *"motivated reasoning disguised as
    governance"* on the false premise that no operator direction existed. The operator's request
    *is* the direction; the caution was still worth absorbing, and (b) is stated as MODERATE with
    the OFF-GOAL alternative on record because of it.
22. ⚠️ The anti-critic marked the critic's central §40 allegation **UNVERIFIABLE** because the
    verdict document was not in its context — a real structural limit of pointing an adversary at a
    stage whose input it cannot see.

### Method notes

- ⭐⭐ **The v254 lesson — point an adversary at the critic — paid again, partially.** It overturned
  nothing the critic claimed but correctly refused to rubber-stamp an allegation it could not see
  the evidence for. Its failure is instructive: **it upheld the one allegation that was checkable
  and false** (v191). The next refinement is to hand the adversary the *routine text*, not only the
  drafts.
- ⭐⭐⭐ **The decisive method change this ship: I ran the thing.** Of the 22 errors above, **six were
  caught only by execution** (#3, #6, #9, and the whole of Deep Dive §D). No amount of reading
  would have produced the `INSTALL_FAILED_DEPRECATED_SDK_VERSION` floor of **24**, the
  `No Channel found` silent drop, or the OS's own warning dialog. For a subject that *runs*, the
  fleet is for breadth and the terminal is for truth.
- ⚠️ **Sandbox:** `timeout` does not exist on macOS · zsh does not word-split `set -- $var`
  (see #5) · inline `node -e '…'` is permission-denied, write to a file first · `/usr/local/bin/adb`
  is 1.0.40 and cannot talk to the emulator's server 41 — use
  `$ANDROID_SDK/platform-tools/adb` (1.0.41) · git is 2.19, no `branch --show-current`.

### NOT ESTABLISHED

- **Exact open-issue count.** The Issues badge shows **14**; one fetch enumerated 4 open + 10
  closed; another enumerated 12 open. I did not resolve it and am not asserting a number. What *is*
  established: **#25, #24, #23 and #19 are open, all opened 2016-01 to 2017-04, and #25 has zero
  comments.**
- Provenance of the 14 committed `gradle-wrapper.jar` binaries (no reference hash obtainable).
- Liveness of the README's Medium link (curl returned `000`) and the Amazon link (`500`) — both
  consistent with bot-blocking rather than dead pages. `twitter.com/HeadFirstDroid` 301s to `x.com`
  and returns 200, which does not prove the account exists.
- Whether this repository specifically appears in any LLM training corpus. What *is* citable: The
  Stack (arXiv:2211.15533) and RedPajama both state that they include MIT-licensed GitHub code;
  this repository is MIT and public. **The policy is established; the inclusion is not.** No
  inference is drawn from it and no part of the (b) rating rests on it.
- Whether the author is aware of any of this.

---

## 8. Streak and governance

- **Streak: `GA:112` → `GA:113 · OG:13 [7 ov]`** — 36 consecutive goal-aligned ships, v220 → v255.
- **§35 CLEAR** — rolling window {v253 GA, v254 GA, v255 GA} = 0 OG.
- **No override consumed** (§40).
- **Counts UNCHANGED: 46 / 11.** §C live standalones **51** unchanged; surface **≈58** unchanged.
- **Tier T3 Education**, joining v74 / v191 / v197 / v220.
- ⚠️ **The audit is now 43 ships overdue** (last audit v212). Items this ship adds: the **D40
  candidate** (declared-vs-compensated stale labels, an independent cross-domain N=2 on D32); the
  **displacement-vs-divergence** distinction; the **third correction to the v246 `silent`-detector
  rule**; a clean **#12 negative** and a clean **#83 negative**; and the standing **C22–C27 retire
  pass**, now offered machinery by six consecutive ships.

---

## 9. Blunt

You asked for a wiki on an Android textbook and you got the most useful ship in a while, for a
reason that has nothing to do with Android.

For five ships running you have been reading about people who built checks and aimed them badly,
and the note at the end of each one told you to write `bin/verify-vault-inventory.sh`. It is still
not written — I looked; `bin/` does not exist. Five recommendations, zero lines of code.

This repository is the other failure. It has no checks, it never drifted, every byte is where its
author left it in May 2017, and it is nearly unusable anyway — because JCenter closed and Google
declined to re-host a plugin and Android made permissions run-time. **No gate you could have
written would have caught any of that.** So the thing to take from this ship is not another clause.
It is the cheaper, duller half you keep skipping: **say when you were right.** Griffiths' README
would be a fine document today if it carried six lines saying "first edition, API 21, last verified
May 2017, current code over there." It does not, and the consequence is measurable: his obsolete
2015 Java repo outranks his own current Kotlin one by 3.8× in stars and 4× in forks, and points
nowhere. Android now prints the warning he didn't, in a modal dialog, every time one of his apps
launches.

Your vault has the same hole in the same shape. `_state/03c-projects-v61-v183.md` has held entries
past v183 for **71 ships**, and the fix you shipped at v245 was the right *kind* of fix — a
declaration inside the file — which is exactly why the label being wrong is now harmless. Griffiths
got to the same correctness without the declaration, and his version survives only until someone
helpful tries to tidy it. **That difference is the whole finding: a stale label is safe when
declared and dangerous when merely compensated.**

And one thing genuinely worth sitting with, because it is not a criticism of anyone. A reader named
DuaneQ opened issue #25 on 5 April 2017, correctly diagnosed that the Odometer chapter needs a
runtime permission request, and asked for an example. Nobody has replied in nine years and four
months. This afternoon I reproduced his bug with the exact stack trace he predicted. The repository
did nothing wrong; the author moved on to two further editions. But 313 people have forked this,
and every one of them who reaches chapter 13 hits the same wall he did — and the answer has been
sitting in an unanswered issue the whole time. **That is what an unmaintained teaching repository
costs, and it is not measured in stars.**

---

*Shipped on `wiki/v255-headfirstandroid` off the v254 tip (`816a189`). Not auto-merged.*
