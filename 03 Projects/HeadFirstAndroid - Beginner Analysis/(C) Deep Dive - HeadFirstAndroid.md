# (C) Deep Dive — `dogriffiths/HeadFirstAndroid`

**Wiki v255 · 2026-08-20 · source-verified · executed on hardware**

> **Method note, stated up front because it is unusual for this corpus:** every load-bearing claim
> in sections C and D of this document was produced by **building, installing and running the code
> on an Android 15 emulator**, not by reading it. Across v250–v254 the vault's own ship notes
> repeatedly recorded *"no code executed."* This one executed. Where a claim is *not* executed it is
> marked **NOT ESTABLISHED** inline.

---

## A. What this is

`github.com/dogriffiths/HeadFirstAndroid` is the official source-code companion to the O'Reilly
book ***Head First Android Development*, 1st edition** (Dawn Griffiths and David Griffiths,
July 2015, ISBN 1449362184). The repository description reads:

> "Source code for the book Head First Android Development by O'Reilly Media"

It is **Java**, not Kotlin — 67 `.java` files, zero `.kt` files on any branch.

### Source verification

Two independent clones, `diff -rq` run **both ways**; the only differences are `.git` internals
(`index`, `logs/HEAD`, `logs/refs/*`), which is expected. The working tree is byte-identical.

### The numbers (all from the clone; ref population declared per rule D27)

| Fact | Value | Command |
|---|---|---|
| HEAD | `8327403926de609ccc12456e0c2c9465ce75d389` (`master`) | `git rev-parse HEAD` |
| HEAD date | **2017-05-23** | `git log -1` |
| Commits on HEAD | **45** | `git rev-list --count HEAD` |
| Commits, all refs | **152** | `git rev-list --count --all` |
| Root commits | **1** — `be7d9e78`, 2014-08-30, *"Initial commit"* | `git rev-list --max-parents=0 --all` |
| Merge commits | **0** | `git rev-list --count --merges HEAD` |
| Tags | **4**, pointing to only **2** distinct commits | `git tag` |
| Authors | **David Griffiths — 152 of 152 = 100%** | `git log --all --format='%an'` |
| Tracked files | **578** | `git ls-files` |
| Java / XML lines | **2,678** / **3,011** | `wc -l` |

Rule **D39** was followed throughout: structural git facts come from the command whose semantics
*are* the definition (`rev-list --max-parents=0`, `rev-list --count`), never `log | head` or
`log | wc`.

Branches, with tip dates:

| Branch | Commits | Tip |
|---|---|---|
| `master` | 45 | 2017-05-23 *"refactor: Add line break"* |
| `secondEdition` | 46 | 2016-09-01 *"Added a test"* |
| `gh-pages` | 97 | **2018-10-16** *"fix: Reload first edition images"* |
| `gh-pages-rss` | 40 | 2015-03-31 |
| `AppCompatChanges` | 35 | 2015-08-16 |
| `AndroidStudio` | 34 | 2015-04-19 |
| `Chapter8` | 27 | 2015-04-11 |

**The most recent commit anywhere in the repository is 2018-10-16** — seven years, ten months ago.

Page-stated GitHub figures (the API is mocked in this environment per §37.4, so these come from the
rendered page and carry **no velocity claim**): **505 stars, 313 forks, 56 watching**, MIT licence,
default branch `master`, not archived.

> **The fork ratio is the interesting number.** 313 forks against 505 stars is **0.62** — several
> times the ratio of a typical library. Forks measure *people who set out to work through it*, not
> people who admired it. That is the signature of a textbook, and it is the strongest available
> evidence that this repository is used rather than merely bookmarked.

### Licence

`LICENSE.txt` is the verbatim MIT text, *"Copyright (c) 2016 Dawn Griffiths and David Griffiths"*,
added 2016-04-17 by commit `e4a8f45` *"Added an open source license"* — roughly **20 months after
the first commit**. Note the asymmetry: **Dawn Griffiths holds copyright and has zero commits.**
The licence names two people; the history names one.

---

## B. The anatomy

### 14 apps across 13 chapter directories

```
chapter01/MyFirstApp      chapter08/Workout
chapter02/BeerAdviser     chapter09/BitsAndPizzas
chapter03/Messenger       chapter10/BitsAndPizzas
chapter04/Stopwatch       chapter11/Starbuzz
chapter06/Starbuzz        chapter12/Starbuzz
chapter07/Workout         chapter13/Joke + chapter13/Odometer
                          chapter14/BitsAndPizzas
```

**There is no `chapter05` directory, and that is correct, not a defect.** The README's chapter-5
section ("The user interface") is a tour of layouts and GUI components and is the only chapter
section with no *"Apps you'll build"* line. There is no app because the chapter builds no app.

### The progressive-snapshot design

Three apps appear at multiple stages. Diffing successive copies (excluding `.idea`, `*.iml`,
`build`, `.gradle`) shows a curriculum that is **well executed**, not duplicated-and-drifted:

| Transition | Files changed | Diff lines | What changes |
|---|---|---|---|
| `ch06/Starbuzz → ch11/Starbuzz` | +1 | **6** | adds `StarbuzzDatabaseHelper.java` only |
| `ch11/Starbuzz → ch12/Starbuzz` | 6 | **258** | rewires all three activities to the database |
| `ch07/Workout → ch08/Workout` | +2, ~3 | **30** | adds `StopwatchFragment` + its layout |
| `ch09/BitsAndPizzas → ch10` | +5, ~3 | **238** | adds four fragments + nav-drawer layout |
| `ch10/BitsAndPizzas → ch14` | +7, ~5 | **111** | adds `CaptionedImagesAdapter`, `Pizza`, detail activity, card layouts |

Read that first row carefully: chapter 11 ("SQLite databases") adds the helper and **touches
nothing else**; chapter 12 ("Cursors and AsyncTasks") is where the 258 lines of wiring land. That
is exactly the pedagogical split the chapter titles promise. The structure is a fingerprint of a
curriculum that was actually designed.

All 14 *"Apps you'll build"* links in the README resolve to directories that exist. **Zero broken
internal links.**

### The boilerplate ratio

| Category | Files |
|---|---|
| Per-project scaffolding (`gradlew`, `gradlew.bat`, wrapper jar + properties, `.idea/`, `*.iml`, `.gitignore`, `proguard-rules.pro`, `gradle.properties`, `settings.gradle`) | **266** |
| Teaching content (67 `.java` + 215 resources/manifests) | **282** |
| Remainder (README, LICENSE, `build.gradle` files) | 30 |
| **Total** | **578** |

**266 of 578 files — 46.0% — is scaffolding repeated fourteen times.** That includes **140
IntelliJ IDE files** (`.idea/` + `*.iml`) and **14 copies of `gradle-wrapper.jar`**, all the
identical 49,896-byte blob `8c0fb64a8698`. `local.properties` is correctly *not* committed, so no
SDK path leaks.

A forensic detail worth keeping. The 14 `gradle-wrapper.properties` files differ from each other
by exactly one line — a timestamp comment — and the timestamps run:

```
19:40:05  chapter13/Odometer      <- earliest
19:41:23  chapter01/MyFirstApp
19:42:25  chapter02/BeerAdviser
   ...
19:50:17  chapter14/BitsAndPizzas <- latest
```

All fourteen on **Tue 23 May 2017**, inside a **ten-minute, twelve-second window**. The commit
`b2487c1` *"chore: Upgrade to gradle 2.3.2"* was fourteen manual Android Studio round-trips in ten
minutes — and Odometer was done first, out of chapter order. *(That last inference — that Odometer
was opened first because it was the app under investigation — is an* inference*; the timestamps are
the fact.)*

---

## C. The build is dead — a forensic walkthrough

This section is the reason to read this document. **Every step below was run.**

### C.1 What a 2026 developer actually sees depends on their JDK

There are two different first errors, and neither says what is wrong.

**With a current JDK** (this machine has Temurin 21.0.10 as default):

```
Could not determine java version from '21.0.10'.
```

Gradle 3.3 shipped in January 2017 and its version parser does not recognise modern Java version
strings. The message does not say *"Gradle 3.3 does not support Java 21."* A developer reads
"could not determine java version", runs `java -version`, sees a perfectly good Java 21, and starts
debugging the wrong thing.

**With JDK 8** (also present here, `1.8.0_181`), the wrapper works fine — Gradle 3.3 downloads and
runs, on macOS 26.3.1, in August 2026:

```
Gradle 3.3
Build time:   2017-01-03 15:31:04 UTC
JVM:          1.8.0_181 (Oracle Corporation 25.181-b13)
OS:           Mac OS X 26.3.1 x86_64
```

…and then `./gradlew assembleDebug` dies in **6.2 seconds**, at project configuration, before a
single line of the app is looked at:

```
A problem occurred configuring root project 'MyFirstApp'.
> Could not resolve all dependencies for configuration ':classpath'.
   > Could not find com.android.tools.build:gradle:2.3.2.
     Searched in the following locations:
         https://jcenter.bintray.com/com/android/tools/build/gradle/2.3.2/gradle-2.3.2.pom
         https://jcenter.bintray.com/com/android/tools/build/gradle/2.3.2/gradle-2.3.2.jar
```

### C.2 The misdirection: the repository it names answers HTTP 200

All 28 `build.gradle` files declare exactly one repository — `jcenter()` — and none declares
`google()` or `mavenCentral()`. JCenter was sunset by JFrog; `jcenter.bintray.com` now **redirects
to Maven Central**:

```
$ curl -sIL -o /dev/null -w "%{http_code} %{url_effective}\n" https://jcenter.bintray.com/
200 https://repo1.maven.org/maven2/
```

So the developer follows the URL in the error message, finds a healthy, live, 200-OK artifact
repository, and concludes the problem must be elsewhere. It is not. **`com.android.support` was
never published to Maven Central**, so the redirect target genuinely does not have it:

```
jcenter → …/com/android/support/appcompat-v7/21.0.3/appcompat-v7-21.0.3.pom   HTTP 404
                                            (final URL: repo1.maven.org)
```

### C.3 JCenter's death was *selective*, and that is the real finding

JCenter's shutdown was survivable for every artifact that had a second home. Watch what happened
when the build finally ran — Gradle logged each download, and the plugin's own transitive
dependencies **still resolved through `jcenter()`**:

```
Download https://jcenter.bintray.com/org/jacoco/org.jacoco.core/0.7.4.../org.jacoco.core-....pom
Download https://jcenter.bintray.com/org/ow2/asm/asm-commons/5.1/asm-commons-5.1.pom
Download https://jcenter.bintray.com/net/sf/proguard/proguard-gradle/5.3.3/proguard-gradle-5.3.3.pom
Download https://jcenter.bintray.com/com/google/protobuf/protobuf-java/3.0.0/protobuf-java-3.0.0.pom
Download https://jcenter.bintray.com/org/jetbrains/kotlin/kotlin-stdlib/1.1.3-2/kotlin-stdlib-....pom
```

Jacoco, ASM, ProGuard, protobuf, kotlin-stdlib — all fine, because all of them are also on Maven
Central, so the redirect finds them.

And Google's own Maven still serves **every 2015-era support-library artifact this repo needs**:

| Artifact | `dl.google.com/dl/android/maven2` |
|---|---|
| `appcompat-v7:21.0.3` | **HTTP 200** |
| `appcompat-v7:22.2.1` | **HTTP 200** |
| `recyclerview-v7:22.2.1` | **HTTP 200** |
| `cardview-v7:22.2.1` | **HTTP 200** |

So what actually died? **Exactly one artifact: the build plugin.**

| Repository | `com.android.tools.build:gradle:2.3.2` |
|---|---|
| `dl.google.com/dl/android/maven2` | **404** |
| `maven.google.com` | **404** |
| `repo1.maven.org` (Maven Central) | **404** |
| `repo.maven.apache.org` | **404** |
| `plugins.gradle.org/m2` | **404** |

AGP **3.0.0 and every later version tested (3.0.1, 3.5.0, 4.0.0, 7.0.0, 8.0.0) return 200** from
Google's Maven. Google moved AGP to its own repository starting at 3.0; **AGP 2.x was never
republished anywhere.** It existed only on JCenter, and JCenter is the one thing that went away.

> **Everything the code depends on survived. The only thing that did not survive is the tool that
> assembles it.** Google is still serving the 2015 libraries and has dropped the 2017 plugin that
> consumes them.

### C.4 The measured fix: three edits

My first hypothesis was that adding `google()` would fix it. **It does not** — I tested it, and the
build fails identically, because AGP 2.3.2 is not there either. The plugin must be *upgraded*, which
drags Gradle with it. The measured minimum is **three one-line edits**:

1. `google()` added to both `repositories` blocks
2. `com.android.tools.build:gradle:2.3.2` → **`3.0.0`**
3. wrapper `distributionUrl`: `gradle-3.3-all.zip` → **`gradle-4.1-all.zip`**

plus a machine-local `local.properties` with `sdk.dir` (gitignored, not a repository change).

Result, on every one of the 14 apps:

```
PASS  chapter01/MyFirstApp        apk=958652B      PASS  chapter11/Starbuzz       apk=1334509B
PASS  chapter02/BeerAdviser       apk=959953B      PASS  chapter12/Starbuzz       apk=1337432B
PASS  chapter03/Messenger         apk=961578B      PASS  chapter13/Joke           apk=960096B
PASS  chapter04/Stopwatch         apk=960689B      PASS  chapter13/Odometer       apk=960287B
PASS  chapter06/Starbuzz          apk=1333965B     PASS  chapter14/BitsAndPizzas  apk=6071956B
PASS  chapter07/Workout           apk=960870B
PASS  chapter08/Workout           apk=963971B      TALLY: PASS=14  FAIL=0
PASS  chapter09/BitsAndPizzas     apk=961657B
PASS  chapter10/BitsAndPizzas     apk=966445B
```

**14 of 14. Zero failures. Fourteen signed APKs**, each with a real `classes.dex` and merged
AppCompat resources. AGP 3.0.0 auto-downloaded the missing `android-21` platform and
`build-tools 26.0.2` on the way, and said so loudly:

```
WARNING: The specified Android SDK Build Tools version (25.0.0) is ignored, as it is below the
minimum supported version (26.0.2) for Android Gradle Plugin 3.0.0.
Configuration 'compile' in project ':app' is deprecated. Use 'implementation' instead.
```

Both warnings are *good* engineering: loud, specific, and they name the remedy. (`compile` was
removed in Gradle 7; AGP 3.0 still accepts it.)

### C.5 Blockers, ranked by what they actually cost

| # | Blocker | Class | Cost |
|---|---|---|---|
| 1 | AGP 2.3.2 exists in no live repository | **unfixable in place** | must upgrade the plugin — 1 line |
| 2 | AGP 3.0.0 requires Gradle ≥ 4.1 | cascade from #1 | 1 line |
| 3 | `jcenter()` cannot serve `com.android.*` | one-line config | 1 line (`google()`) |
| 4 | Gradle 3.3 rejects modern Java version strings | toolchain | moot after #2 |
| 5 | `buildToolsVersion '25.0.0'` no longer distributed | self-healing | AGP overrides it, loudly |
| 6 | `android-21` platform absent | self-healing | AGP auto-downloads it |
| 7 | `compile` configuration | future-only | works on AGP 3.0; removed in Gradle 7 |

Only #1–#3 are real, and all three are single lines. **The distance between "cannot configure" and
"fourteen signed APKs" is three lines of text.**

---

## D. What happens when you actually run it

### D.1 It builds. It does not install.

```
$ adb install app-debug.apk
adb: failed to install …: Failure [INSTALL_FAILED_DEPRECATED_SDK_VERSION:
      App package must target at least SDK version 24, but found 21]
```

**14 of 14 build. 0 of 14 install.** Android 15 (API 35) refuses any package targeting below API 24.
Note the number came from the device, not from a policy page: the floor is **24**, not 23.

For completeness on the publishing question — from
[developer.android.com/google/play/requirements/target-sdk](https://developer.android.com/google/play/requirements/target-sdk):
from **31 August 2026** (eleven days after this analysis) *"New apps and app updates must target
Android 16 (API level 36) or higher to be submitted to Google Play."* These target **21**.

### D.2 A fourth edit, and they all install

Changing `targetSdkVersion 21` → `24` in each app's `build.gradle` — one line, the fourth edit:

```
INSTALL_OK  ×14        INSTALL_FAIL=0   BUILD_FAIL=0
```

Verified from the artifact itself with `aapt dump badging`:
`package: name='com.hfad.odometer' … sdkVersion:'16' targetSdkVersion:'21' → '24'`,
`uses-permission: name='android.permission.ACCESS_FINE_LOCATION'`.

### D.3 Android writes the deficiency disclosure the README never did

The moment an app launches, Android 15 puts up a modal dialog of its own:

> **Joke**
> *"This app was built for an older version of Android. It might not work properly and doesn't
> include the latest security and privacy protections. Check for an update, or contact the app's
> developer."*
> [ Check for update ] [ OK ]

The README says nothing about the repository's age, edition, target API, or build viability — a
case-insensitive grep for *first edition / 2nd edition / deprecat / outdated / no longer / legacy /
unmaintained / archive* over `README.md` returns **one** hit, and it is the phrase "API level 21"
inside the chapter-14 *content* description, not a warning. **The operating system supplies the
disclosure the document withholds.**

*(This dialog is also a trap for automation: it sits above the app and swallows taps. My first
attempt to test the notification path silently hit the dialog scrim instead of the button and
reported "no crash" — a false negative I caught only by taking a screenshot.)*

### D.4 Eight of nine run. The ninth is a nine-year-old open issue.

Launching each distinct app on Android 15:

| App | Result |
|---|---|
| ch01 MyFirstApp | **RUNNING** |
| ch02 BeerAdviser | **RUNNING** |
| ch03 Messenger | **RUNNING** |
| ch04 Stopwatch | **RUNNING** |
| ch06/11/12 Starbuzz | **RUNNING** |
| ch07/08 Workout | **RUNNING** |
| ch09/10/14 BitsAndPizzas | **RUNNING** |
| ch13 Joke | **RUNNING** |
| **ch13 Odometer** | **CRASHED** |

The chapter-14 Material Design app — RecyclerView, CardViews, navigation drawer,
ShareActionProvider — renders correctly on a 2026 Android release. A screenshot is in this folder
(`bap_clean.png`).

The crash:

```
java.lang.RuntimeException: Unable to create service com.hfad.odometer.OdometerService:
java.lang.SecurityException: uid 10214 does not have android.permission.ACCESS_COARSE_LOCATION
                             or android.permission.ACCESS_FINE_LOCATION.
  at android.location.LocationManager.requestLocationUpdates(LocationManager.java:1212)
  at com.hfad.odometer.OdometerService.onCreate(OdometerService.java:54)
```

`OdometerService.java:54` calls `locManager.requestLocationUpdates(...)` in `onCreate()`. A grep
across both of the app's two Java files for `checkSelfPermission` or `requestPermissions` returns
**zero**. The code uses the pre-Marshmallow install-time permission model, which is correct for
`targetSdkVersion 21` and wrong for anything at or above 23.

Now the part that matters. **Issue #25, *"Chapter13 Odometer Service Requires Permissions"*, opened
by `DuaneQ` on 5 April 2017, has ZERO comments and is still open.** The reporter wrote:

> "It appears as if the code isn't working in Chapter 13 because when using a dangerous service you
> explicitly need to ask for permissions from the user."

He was right. Nine years, four months, and fifteen days later I reproduced it with the exact stack
trace, and nobody has ever replied to him.

### D.5 The notification chapter fails *silently* — and the census was wrong about it

One fleet agent reported that Joke *"crashes with IllegalArgumentException on API 26+"*. **Refuted
by execution.** Rebuilding Joke at `targetSdkVersion 26`, installing, dismissing the OS dialog,
tapping the button, and waiting out the service's `wait(10000)`:

```
E NotificationService: No Channel found for pkg=com.hfad.joke, channelId=null, id=5453,
    notification=Notification(channel=null … defaults=VIBRATE flags=AUTO_CANCEL …)
```

No crash. No `FATAL EXCEPTION`. No notification either — `dumpsys notification` shows nothing
posted. The user presses **"WHAT IS THE SECRET OF COMEDY?"**, waits ten seconds, and *nothing
happens*, forever, with one line in a log nobody reads.

`DelayedMessageService.java:57` builds a `new Notification.Builder(this)` with no channel.
Notification channels became mandatory for `targetSdk ≥ 26` — **introduced in Android 8.0, August
2017, three months after this repository's last commit to `master`.**

There is a narrow window here that is worth naming, because it is the whole modernization problem
in one number: **the OS will not install below targetSdk 24, and notifications break silently at
targetSdk 26.** The four-edit fix works because 24 is the lowest value the platform accepts, which
happens to be one below the level at which this code starts failing. The usable window is 24–25.
Google Play requires 36.

### D.6 The tests are green and test nothing

Fourteen files named `ApplicationTest.java`, all exactly 12 lines, six distinct blobs (copied
between chapters). Each is the Android-Studio-generated stub:

```java
public class ApplicationTest extends ApplicationTestCase<Application> {
    public ApplicationTest() { super(Application.class); }
}
```

Zero test methods, zero assertions. So far, unremarkable. But run them:

```
$ ./gradlew connectedCheck
:app:connectedCheck
BUILD SUCCESSFUL in 4s
```

```xml
<testsuite name="com.hfad.myfirstapp.ApplicationTest"
           tests="1" failures="0" errors="0" skipped="0">
  <testcase name="testApplicationTestCaseSetUpProperly" … />
</testsuite>
```

**One test. Zero failures. Green.** The author wrote no test methods; the deprecated JUnit3 base
class `android.test.ApplicationTestCase` supplies one, called
`testApplicationTestCaseSetUpProperly`, which asserts that *the test harness set itself up*. It
tests the framework, not the application. Any metric that counts test files, or test results, or
CI green, reports this repository as tested.

This is the v246 *needle* pattern — *"pytest reports skips as success"* — in a different language,
and slightly worse: this is not a skip being counted as a pass. It is a pass, of a test whose only
subject is its own existence.

**And the one real test in the repository is on a branch nobody merged.** Commit `51511f9`
*"Added a test"* (2016-09-01) on `secondEdition` adds `StartupTest.java`, 65 lines, a genuine
Espresso test with a twenty-line Javadoc that patiently explains what an instrumented test *is*,
what `onView`, `allOf`, `isAssignableFrom` and `withText` each do, and how to run it. Alongside it,
`5e82ba6` *"Added some sonar and test coverage config."* It is the best-taught file in the
repository. It was never merged to `master`, and `secondEdition` died three weeks later.

*(I initially flagged the doc-comment's `./gradlew connectCheck` as a typo for `connectedCheck`.
It is not a defect — Gradle resolves camelCase task-name abbreviations, and I verified
`./gradlew connectCheck` does execute `connectedDebugAndroidTest`.)*

---

## E. The things that are stale and correct

Read the README's chapter-to-image mapping:

| Chapter | Image referenced |
|---|---|
| 1–6 | `chap01`…`chap06` |
| **7 Fragments** | **`chap10img.png`** |
| **8 Nested fragments** | **`chap11img.png`** |
| **9 Action Bars** | **`chap12img.png`** |
| **10 Navigation Drawers** | **`chap13img.png`** |
| **11 SQLite databases** | **`chap07img.png`** |
| **12 Cursors and AsyncTasks** | **`chap08img.png`** |
| **13 Services** | **`chap09img.png`** |
| 14 | `chap14img.png` |

It looks like a rotation bug. It is not. **I opened the images.** `chap10img.png` depicts the
Workout app showing two fragments side by side on a tablet — that is chapter 7's content.
`chap07img.png` depicts Starbuzz with a SQLite Helper and a database — that is chapter 11's content.
**The mapping is correct. The filenames are stale.**

The history explains it: `030762a` *"Renamed the folders so that they will appear in numeric
sequence"*, `c43e68d` *"Corrected section numbering"*, `69a3b7c` *"Fixed image paths"*. The book's
chapters were renumbered during writing. The directories were renamed and the README's references
were updated to compensate. The image *filenames* were left at their draft numbers.

So a stale label sits in the middle of this repository, and **it is load-bearing.** An agent — or a
tidy-minded contributor — asked to "fix the mismatched image references" would renumber them to
match the filenames and silently break every picture in the README.

This is the vault's own disease, and it is instructive precisely because Griffiths solved it the
*other* way. At v245 the vault adopted rule **D32** from `unslothai/unsloth`: *when two documents
must carry the same fact and mechanising it is impractical, declare which copy wins, inside the copy
that loses.* The vault applied that to `_state/03c-projects-v61-v183.md` — a filename that has been
wrong for 71 ships — by writing a source-of-truth notice **inside the file**. The drift remained;
the declaration made it **harmless and self-diagnosing**.

Griffiths achieved the same correctness **without the declaration**. Nothing anywhere says
"the image filenames use the pre-publication chapter numbering; the README compensates." The result
is correct today and fragile forever: it survives only as long as nobody helpful comes along.

> **The lesson, stated precisely: a stale label is safe when it is declared and dangerous when it
> merely happens to be compensated.** Correctness that depends on nobody noticing the
> inconsistency is not correctness; it is luck with a long half-life.

### The one image defect that was real, and how it got fixed

`gh-pages` commit `4bfd979` (2017-05-08, *"Updated for second edition"*) rebuilt the site as a
Create React App for the second edition's 19 chapters, moved the 14 first-edition images to `ed1/`,
and **removed the `images/` directory** — the exact path `master`'s README points at. Two commits
on 2018-10-16, `c54abe2` *"fix: Correct image locations"* and `ac4252a` *"fix: Reload first edition
images"*, restored it. All 14 `images/` blobs are now byte-identical to their `ed1/images/`
counterparts, and `chap07img.png` currently returns HTTP 200, 106,987 bytes.

So the first-edition README displayed **broken images for roughly seventeen months**. And the fix
was reactive: **issue #29, *"img links are broken"*, was closed on 16 October 2018 — the same day as
the fix commits.** A reader had to notice and report it.

*(I initially hypothesised that `images/` was serving second-edition artwork today. Wrong: I
hash-compared all 14 blobs against `ed1/images/` and they are identical. Correcting that was what
led to the real seventeen-month finding.)*

---

## F. What an agent sees

**The agent-facing surface is empty.** A grep of all 578 tracked filenames for
`CLAUDE|AGENTS.md|.cursor|copilot|llms.txt|SKILL|CONTRIBUTING|.github` returns **zero**. No CI has
ever existed, on any branch, in eleven years.

What a coding agent pointed at this repository cannot know, and would have to guess:

| Unknown | Consequence | One line of `AGENTS.md` fixes it |
|---|---|---|
| Which JDK | Two different cryptic failures depending on the answer | "Requires JDK 8." |
| That there is no aggregate build | "Fix the build" is ambiguous across 14 targets | "Each `chapterNN/AppName/` is an independent Gradle project. There is no root `settings.gradle`." |
| Which edition this is | Will assume it is the current book | "This is the 1st edition (2015, Java). Current edition code: `dogriffiths/HeadFirstAndroid3rdEd` (Kotlin)." |
| That `chapter05` has no app by design | Will "fix" the gap | "Chapter 5 builds no app." |
| That the image filenames are deliberate | Will break the README | "Image filenames use pre-publication chapter numbers. Do not renumber." |
| That the build cannot resolve as shipped | Will report a broken clone | "`jcenter()` cannot serve `com.android.*`; AGP 2.3.2 no longer exists. Add `google()`, bump AGP to 3.0.0, Gradle to 4.1." |

### The hazard list: where the obvious fix is wrong

1. **Renumber the image references** → breaks all 14 README images. (§E)
2. **Deduplicate the 14 identical `gradle-wrapper.jar` files** → breaks the independent-project
   structure that lets a reader open one chapter in isolation.
3. **Unify `appcompat` on 21.0.3** → chapter 14 needs 22.2.1 to match its `recyclerview-v7` and
   `cardview-v7`.
4. **"Implement" the 14 empty test stubs** → invents behaviour the book never specified, and the
   stubs' base class is deprecated anyway. Deleting them is defensible; filling them is not.
5. **Delete the 4 tags** → they are `build-7/9/10/11` pointing at only two commits, both on
   `secondEdition`, neither on `master`. Harmless, but they are the only trace of a CI system that
   once existed.
6. **Bump `targetSdkVersion` to something modern** → breaks Joke silently at 26. (§D.5)

### Security

Proportionate assessment: this is a static teaching repository with no server, no ports, no
credentials, no network calls in app code, and no third-party dependencies beyond Google's own
support libraries.

- **Manifest permissions:** exactly one, in one app — `ACCESS_FINE_LOCATION` in Odometer. The other
  13 request nothing.
- **Secrets:** none found; `local.properties` correctly gitignored.
- **Transport:** the Gradle wrapper's `distributionUrl` is **https** (good). `jcenter()` is https.
  The README's image URLs are **plain `http://`** to `dogriffiths.github.io` — cosmetic here (they
  are decorative PNGs on a GitHub-hosted page), but it is 2026 and they should be https.
- **The 14 committed `gradle-wrapper.jar` binaries:** sha256
  `e2b82129ab64751fd40437007bd2f7f2afb3c6e41a9198e628650b22d5824a14`, all identical.
  **NOT ESTABLISHED:** I could not obtain an authoritative reference hash for an official Gradle
  wrapper jar of this vintage to compare against. This matters because `./gradlew` *executes* that
  jar. It is almost certainly the genuine Android-Studio-generated wrapper; "almost certainly" is
  not "verified."
- **Risk:** cloning and reading — **negligible**. Running `./gradlew` — **low**, contingent on the
  unverified wrapper jar. Installing a built APK — **low**, and the OS itself warns you.

### Would this make a good legacy-modernization benchmark?

**For:** small (5,689 lines of teaching content), MIT, self-contained, no network services, no
secrets, 14 comparable targets, and — now — a **verified ground-truth fix at two levels**: three
edits to build, four to install and run.

**Against, and this is the decisive objection:** *you cannot verify a migration succeeded.* There
are no real tests. `connectedCheck` returns green on an empty stub (§D.6), so the obvious success
signal is worthless. Verifying a modernization means launching each app on a device and looking at
it — which is exactly what I did, by hand, and exactly what an automated eval cannot do without
someone first writing the assertions that do not exist.

**Verdict:** a genuinely good *fixture*, and not yet a *benchmark*. The missing piece is not the
code and not the fix — it is the oracle. Anyone wanting to use it this way must first write, per
app, one Espresso assertion that the main screen shows what it should. The repository contains
exactly one file that demonstrates how to do that, and it is on the abandoned branch.

---

## G. What is genuinely good

Credit where it is due, because a lot of this repository is well made.

- **The curriculum is real.** The progressive-snapshot diffs (§B) show deliberate, correctly-sized
  increments that match the chapter titles. Chapter 11 adds the database helper and nothing else;
  chapter 12 does the wiring. That is designed, not accreted.
- **The early git history is a teaching artifact.** *"Up to Test Drive on page 16"*, *"Code up to
  page 27"*, *"Up to Test Drive on page 42"* — the author committed at the book's own checkpoints so
  a reader could `git checkout` to the exact page they were on. That practice was used for the
  Stopwatch chapter and then abandoned for chapter-sized dumps, which is a pity.
- **The code is clean and consistent.** Uniform package naming (`com.hfad.*`), consistent
  formatting across 67 files, `onDestroy()` in `OdometerService` correctly removes its location
  listener and nulls its references. There is no cleverness anywhere, which for teaching code is
  the right choice.
- **The commented-out earlier stages are deliberate pedagogy.** `DelayedMessageService` still
  carries its `Log` version and its `Toast` version commented out above the `Notification` version,
  each labelled *"Used in log version"* / *"Used in Toast version"* — the reader can see all three
  stages of the chapter in one file.
- **Bugs reported by readers were fixed and credited by name.** *"Fix rotation bug in the workout
  app reported by j8s0n"*, *"Upgrade to Android Studio 2. Issue reported by @tomjohnson1492"*.
- **Zero broken internal links** across all 14 README app references.
- **`local.properties` is correctly excluded**, which a surprising number of Android repositories
  of that era got wrong.
- **The seventeen-month image outage was actually fixed**, and the fix was done the careful way —
  restoring the original blobs rather than re-exporting new ones.

---

## H. The lesson

Every recent subject in this corpus failed in the same direction. v250 wrote six rules it called
non-negotiable and gated one. v251 built a measurement instrument and pointed it only at the arm
that could not fail. v252 ran a three-arm eval, ran one arm, and published the comparison. v253
wrote a word budget into a commit message and watched it breach at twenty-one times the rate. v254
built a weekly CI job and aimed it at the single property of its file nobody doubted. In every case
a *check* was missing, misaimed, or unenforced, and the artifact drifted away from its own claims.

**This repository has no checks at all, and it did not drift.** Not one byte has changed since
2017-05-23. Every file is exactly as its author left it. The curriculum is still coherent, the code
still compiles, the internal links still resolve, the images still load, and the chapter-to-image
mapping is still correct. Measured against its own claims, this artifact is *more* faithful than any
of the last five subjects.

And it is nearly unusable — because the world moved.

That is a different failure mode, and it deserves its own name. The last five ships were about
**divergence**: the artifact changed, or its claims did, and nothing was watching the gap. This one
is about **displacement**: the artifact held still and the ground moved under it. JCenter was
retired. Google relocated its Maven coordinates and declined to bring AGP 2.x along. Android made
permissions run-time, then made notification channels mandatory, then set an install floor at
targetSdk 24. Each of those was somebody else's decision, taken years after the last commit.

The two modes fail differently and demand different remedies:

- **Divergence** is defended by a gate. A check, aimed at the thing that can drift, that fails
  loudly. This is what v250–v254 kept getting wrong, and it is a solved problem in principle.
- **Displacement cannot be gated at all.** No CI job Griffiths could have written in 2017 would
  have failed in 2021 when JCenter closed, because the failure is not in the artifact. There is no
  predicate over these 578 files that is true in 2017 and false in 2026. **The bytes are the same;
  only their meaning changed.**

What *can* be done about displacement is much smaller and much duller: **say when you were right.**
Not "this is deprecated" — the author could not have known — but *"this is the first edition, it
targets API 21, it was last verified in May 2017, and the current edition's code is over there."*
Six lines. They would have cost nothing in 2017 and they would be worth a great deal now, because
they convert an artifact that appears current into one that is honestly dated.

The repository does not say them, and the consequence is measurable. **Its 505 stars and 313 forks
make the obsolete first edition the most discoverable Head First Android repository on GitHub —
3.8× the stars and 4× the forks of `HeadFirstAndroid3rdEd`, which has 134 stars, 78 forks, and the
Kotlin code for the book that is actually in print.** A learner searching GitHub finds the 2015
Java code first, and nothing in it points onward. Meanwhile Android itself, at every app launch,
displays the sentence the README declined to write.

There is one more turn. The vault's own `silent`-detector grep — `grep -rni "silent" .` — returns
**zero** here, the third consecutive null. v253 explained its nulls by saying the detector's domain
is artifacts that *run*; v254 refuted that, having a runtime and still returning zero, and proposed
*artifacts whose authors have debugged them*. Griffiths debugged these apps page by page — the
commit log proves it — and the grep is still zero. So the rule needs its third correction:
**the detector finds artifacts whose authors wrote down their reasoning about failure.** Nothing
more.

And here that null sits directly on top of a real silent failure. Push `targetSdkVersion` to 26 —
which Google Play now demands at 36 — and chapter 13's notification vanishes with a single line in
a log. The author never reasoned about that failure mode in writing, and could not have: it was
invented three months after he stopped committing.

**You cannot document a failure mode that does not exist yet. You can only date your work.**

---

*Verified 2026-08-20. Clone HEAD `8327403926de609ccc12456e0c2c9465ce75d389`. Builds, installs and
runs executed against a Pixel_3_API_35 AVD (Android 15, API 35) with Temurin JDK 1.8.0_181, AGP
3.0.0, Gradle 4.1. Screenshots in this folder. Star/fork figures are page-stated; the GitHub API is
mocked in this environment (§37.4) and no velocity claim is made.*
