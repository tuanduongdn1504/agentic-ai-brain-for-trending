---
title: Mobile Engineer Interview Corpus (React Native / React / Flutter) — 5 real mock interviews
date_ingested: 2026-08-06
source_type: youtube-private-operator
path: 5 (yt-dlp only, cookies-from-browser)
videos: 5
language: Vietnamese (English technical terms embedded)
interviewer: Tuấn Dương (+ "Huân" program lead in video 3)
hiring_company: "Innovo" (garbled as Eno/Enovo in ASR — not asserted with certainty)
compiled: 2026-08-06 via Workflow wf_89de7c46-db7 (3/5) + wf_2408264b-657 (2/5 recovery); maker/checker refute-first verify per video; Opus main-loop authorship
verification: per-video refute-first verifier re-read both transcripts; 5 videos, 170 Q&A items, ~166 verified-OK
---
<!-- compiled: 2026-08-06 → wiki/mobile-engineer-interview/ (15 files). Faithful record; model answers live in the wiki, not here. -->

# Mobile Engineer Interview Corpus — faithful extraction

Five real mock/screening interviews from the operator's own private YouTube channel (**Tuấn Dương**), each a candidate for a **mobile/front-end engineer** role (React Native / React / Flutter) at what appears to be **Innovo**. Conducted in **Vietnamese** with English technical terms embedded. Captions were auto-generated (ASR) in Vietnamese-original + auto-translated English — **doubly garbled**; every technical term here is a *reconstruction of intent*, not a quotable transcript. Raw captions are not quotable.

**This file records what was ASKED and what the candidate ANSWERED (+ verdict).** The canonical/model answers are synthesised in the wiki, not here.

## Method / provenance

- **Extraction:** yt-dlp `--cookies-from-browser chrome` (all 5 are Private videos) → `--write-auto-subs --sub-langs vi-orig,en` → awk rolling-caption dedup → per-video extractor agent read BOTH vi + en transcripts and reconstructed garbled terms with a verified garble key + domain knowledge.
- **Verification:** one refute-first verifier per video re-read both transcripts to catch hallucinated questions, dubious term reconstructions, speaker-swaps, and technically-wrong model answers.
- **NO NotebookLM, NO yt-search** (operator-supplied URLs).

## The 5 videos

| # | ID | Candidate (as titled) | Stack | Length | Recorded | Q&A | Verified |
|---|---|---|---|---|---|---|---|
| 1 | OVN_9-15sy0 | Vũ Thành Long | Flutter | 51:47 | 2025-05-27 | 45 | 42/45 |
| 2 | aKMVTOvgjsI | Đỗ Minh Thành | Flutter | 1:04:17 | 2026-06-15 | 34 | 28/30 |
| 3 | 0n8oaue3-y4 | Trương Nhất | React / JS (very junior) | 33:08 | 2026-06-15 | 23 | 22/23 |
| 4 | PVO5AX4YAgQ | Đỗ Thanh Tuấn | React Native + Android | 35:08 | 2026-06-17 | 15 | 14/14 |
| 5 | DztoZaxz79Y | Huỳnh Đinh Hoàng Viên | React | 55:29 | 2026-08-05 | 53 | 32/34 |

⚠️ **Name uncertainty:** in video 1 the candidate at one point says "my name is Duy" while the file is titled "Vũ Thành Long"; ASR garble on names is heavy. Names are provenance only; the value is the questions.

## Verified garble key (recovered by cross-referencing vi + en + domain knowledge)

`Rnative/Reactive/"R"`→React Native/React · `Flashbox`→Flexbox · `GD/GCK`→CSS Grid · `Fet 1/Flash 1`→`flex: 1` · `Isaac/IAC/AC`→Axios · `order function`→higher-order function · `TD tag/card`→`<td>` · `.abb/ABB/.ch/file A`→`.aab` (Android App Bundle) · `SHSH blobs/SH2`→SHA-1/SHA-256 signing fingerprint · `Flter`→Flutter · `đát`→Dart · `bloc`→BLoC · `Bit O`→Big O · `material pay`→MaterialPageRoute · `make it solid`→setState/stateful · `gigit/kick/"g"`→git.

---

## Video 1 — Vũ Thành Long (Flutter) — 51:47

**Profile:** Year-4 Electronics & Telecom student, Da Nang University. One internship (VNPT) reassigned from clustering → Angular web. School + graduation projects only; self-taught via projects + Google. Hands-on Flutter UI, but weak on async patterns, state-management libs, VCS workflow, and API integration. No commercial shipping.

**Domains & questions (verdicts: ✅correct ◑partial ✗wrong ∅did-not-know):**

- **Behavioral:** self-intro ✅ · graduation-project difficulties (state not persisting on edit; dropdown resets changes; ListView/scroll overflow) ◑ · debugging approach (google/ask friends) ✅ · preferred team role (coder+leader) ◑ · conflict resolution as lead ✅ · presentation role ✅ · 1–2yr + 5yr career plans ✅ · English self-rating (rusty, plans cert) ◑ · 5 strengths ✅ · areas to improve ✅ · Flutter communities (only FB group) ◑ · questions for us (none) ◑
- **Git:** common commands ◑ · what before committing ◑ · git rebase ∅ · merge conflicts (his fix: *rename the file* — ✗ wrong) · git fetch vs merge ✗ · #repos created ✅ · other VCS tools ∅
- **Dart:** list data types (mixed modifiers final/const/static with types) ◑ · final vs const ✗ · why const needs a value ∅ · collection methods map/where/sort ◑ · transform an array ✗ · null-checking operators ◑ · `?.` safe-navigation ∅ · toUpperCase ✅ · toTitleCase ∅ · spread `...` ◑ · async/await ◑ · what returns the result in async ◑ · what is Future ◑
- **Flutter:** widget lifecycle + method names ✗ · what is a Widget ◑ · StatefulWidget vs StatelessWidget ◑ · initState ✅ · Scaffold ◑ · is Scaffold required ✅ · Container vs SizedBox ✅ · ListView-in-Column errors ◑
- **Live coding (array ops, ~19:00–31:00):** add element · remove value 6 · sort descending · dedup — struggled to recall APIs under pressure.
- **Other:** HTTP APIs (only file I/O) ∅ · BLoC / Provider heard-of-only ∅

**Interviewer (Tuấn) style:** methodical ramp (background → git → Dart → async/Flutter → live coding → widgets → behavioral); probes "why" on shallow answers; checks fundamentals before frameworks; supportive, non-adversarial; ends with transparent process (1 slot, results by a set Friday).

**Verifier notes:** 42/45 faithful. Tech-imprecision: StatefulWidget "lifecycle methods" model answer conflated classes — only `createState()` is on StatefulWidget; `initState/build/didUpdateWidget/dispose` are on the **State** class. Reconstruction flags: "git rebase" (from garbled "git xưa"), null-operator terminology. Live-coding array section = 4 distinct questions compressed into one.

---

## Video 2 — Đỗ Minh Thành (Flutter) — 1:04:17

**Profile:** Year-4 student; one internship (UI design only, "Freem"); current intern ("Enovo"). Self-taught Flutter (YouTube + docs). Solid UI/design; weak on advanced Dart, state management, and backend/API. Transparent about gaps; strong soft skills.

**Domains & questions:**

- **Git:** regular commands ◑ · checkout variants (used `-B` vs `-b`) ◑ · `.gitignore` ∅ · merge conflicts ◑ · **git pull vs rebase** (⚠️ verifier: likely *rebase vs merge*; timestamp/label uncertain) ∅ · how a PR works ◑ · amend a pushed commit (confused with reset) ✗
- **Dart:** basic data types (mixed modifiers) ◑ · **const vs final — candidate had it BACKWARDS** (said final allows updates / const only-at-declaration) ✗ · Set/Map/List + `every` ◑ · spread `...` ∅ · async/await ✅
- **Live coding:** add two numbers to array ✅ · sort ascending ✗ · remove duplicates ∅
- **Flutter:** Stateful widget lifecycle (order confusion) ◑ · what are widgets + reuse ✅ · Stateless vs Stateful ◑ · Scaffold ✅ · **BuildContext** ∅ · Container vs SizedBox ✅ · ListView-in-Column fix (shrinkWrap/SizedBox) ✅ · MainAxisAlignment vs CrossAxisAlignment ✅ · GetX / BLoC ∅ · HTTP APIs ∅ · navigation push vs pop ✅ · what is a modal ∅
- **Behavioral:** internship project (smart-home UI, fake data) ✅ · Flutter pros/cons ✅ · team conflict ✅ · strengths ✅ · weaknesses + plan ✅ · how you learned Flutter (self-taught) ✅

**Interviewer style:** structured depth (VCS → language → framework → live coding); mentoring tone; "title doesn't matter, foundation does"; sketches a 3-month intern ramp. Self-rated candidate ~7/10.

**Verifier notes:** 28/30 faithful. ⚠️ const/final extractor *summary* inverted the candidate's own (already-wrong) claim; the **verdict "wrong" is correct**. `-B` vs `-b` distinction under-called (lowercase `-b`=create; uppercase `-B`=create-or-reset/force). Missed: rebase-vs-merge use-case detail; Dart parameter-passing; internship-phase detail.

---

## Video 3 — Trương Nhất (React / JavaScript) — 33:08 — VERY JUNIOR

**Profile:** Career-changer (military → IT), **1 semester** formal study (~3 months), self-taught CSS/JS via F8. No deployed projects (one GitHub repo, not live). Critical gaps in async, higher-order functions, algorithms, data structures. Strong behavioral maturity + honesty. Two interviewers: **Tuấn** (technical) + **Huân** (program lead).

**Domains & questions:**

- **JavaScript:** "JS is asynchronous — what does async mean / why?" (confused it with type mismatch) ✗ · higher-order functions ∅ · Axios (knew "a JS library", missed HTTP purpose) ◑
- **HTML/CSS:** `<td>` tag ∅ · Flexbox vs Grid (missed 1D-vs-2D) ◑ · `flex: 1` (intuitive, no shorthand) ◑ · CSS `position` **values** (listed offset props top/left/… instead) ✗
- **CS-fundamentals:** bubble sort (vague) ✗ · data structures in depth ∅ · Big O ∅
- **Web:** domain vs hosting ◑
- **React:** framework knowledge (hasn't reached React yet; it's the gating requirement) ∅
- **Portfolio:** deployed/live projects (none shipped) ✗
- **Behavioral:** English level (reading>listening) ✅ · learning path (military→IT) ✅ · why switch to IT (intrinsic interest) ✅ · challenges entering the market ◑ · specific self-study obstacles (no mentor/materials) ✅ · why intern so early ✅ · handling a no-mentor/no-roadmap job ◑ · internship expectations ✅ · study plan pre-internship (8–16h/day — earnest but unrealistic) ✅ · researched the program? (only browsed site) ∅

**Interviewer style:** Tuấn = knowledge-checkpoint, corrects misunderstandings immediately, compassionate about junior level; Huân = behavioral, motivation & handling-ambiguity, offers mentorship + explains the 3-month program roadmap.

**Verifier notes:** 22/23 faithful; ASR reconstructions all defensible (Axios, higher-order fn, Flexbox/Grid, flex:1, bubble sort, Big O). No major violations.

---

## Video 4 — Đỗ Thanh Tuấn (React Native + Android) — 35:08

**Profile:** Year-4 CS student (Bách Khoa Đà Nẵng), 2 yrs Java/Android → ~2–3 months serious React Native. **Shipped 3 Android apps to Google Play.** JS is surface-level (weak ES6+, algorithms). Pragmatic (JS over TS for speed). Honest, mature career planning (wants Kotlin/Swift eventually).

**Domains & questions:**

- **Mobile / App-Store:** walk through uploading an Android app to Play Store (keystore + SHA-256, export `.aab`, Console project, screenshots, review ~2–3 days, fix policy rejections) ◑ · Fastlane ∅ · deployment environment config (UAT/Dev/Prod) *(verifier: discussed, not a discrete item)*
- **System/API:** GraphQL vs REST (uses REST+SQL; no GraphQL) ∅ · HTTP client (knows Axios, uses fetch/built-in for now) ◑
- **JavaScript:** confidence on JS fundamentals ◑ · loop 1→9 in browser console (worked, but console mechanics confusion) ✅ · remove duplicates (learned Set + spread *during* the interview) ◑ · ES6 features (very vague) ✗ · reverse a string (needed time to recall) ◑ · palindrome check (concept only, no clean code) ◑
- **TypeScript:** TS vs JS (knows "must declare types"; uses JS for velocity) ◑ · TS team benefits (restated well after coaching) ✅
- **Behavioral:** RN vs Java vs Flutter preference (RN, open to others) ✅ · long-term mobile plan (master RN → Kotlin → Swift) ✅ · group-of-3 hiring dynamics / not all hired together ✅

**Interviewer style:** pedagogical/guided-discovery (teaches Set, spread, TS benefits during the interview); real-world grounding ("how many apps on the store?"); supportive scaffolding on live coding; open about hiring constraints (3 roles, 3 stacks).

**Verifier notes:** 14/14 faithful, clean — reconstructions (Axios, Fastlane, GraphQL, TypeScript) accurate; model answers correct. Missed as discrete items: env-config split, Kotlin-as-3rd-platform, specialization-sequencing.

---

## Video 5 — Huỳnh Đinh Hoàng Viên (React) — 55:29 — STRONGEST

**Profile:** University student (final 2 yrs). React front-end with genuine grasp of core JS (data types, event loop, async/await, hooks). Led multiple school team projects; built the "Bravo" peer-review platform comment/annotation feature. Medium English. Seeking Innovo internship.

**Domains & questions:**

- **JavaScript:** map vs for-loop ◑ · reduce ✅ · list data types + primitives vs objects ✅ · null vs undefined (+ API payload insight) ✅ · `==` vs `===` ✅ · event loop ◑ · call stack + web APIs (⚠️ said vars live in **heap** — see correction) ◑ · IIFE ◑ · write+run an IIFE (live) ◑ · shallow vs deep copy ◑ · Promise (states, resolve/reject, then/catch) ✅ · why async/await + how it differs from Promise ◑
- **Testing / Quality:** testing stages dev→release ◑ · clean code ◑ · SOLID (only knew S) ◑ · DRY ✅ · debugging tools / DevTools tabs ✅ · unit testing (never written one) ◑
- **React:** Virtual DOM vs Real DOM ✅ · JSX + common hooks ✅ · when hooks introduced (16.x) + class components before ✅ · lifecycle (mount/update/unmount) + useEffect parts ✅ · useEffect 3 dependency-array cases ✅ · useMemo vs useCallback ◑ · SPA vs multi-page ✅ · CSR vs SSR (conflated with MVC) ◑ · MVC (Java, yr3) ✅ · Excel file upload (used a lib) ◑ · UI libs Ant vs Material ✅ · Vue vs React (SFC vs JSX) ✅ · project folder structure ✅ · deployment of current project ✅
- **Behavioral (extensive):** strengths/weaknesses (responsive design) ✅ · school+internship workload ✅ · focus in noise ✅ · team role (de-facto lead) ✅ · why lead ✅ · lead responsibilities ◑ · handling a slacker ✅ · resolving 2-member conflict ◑ · working with seniors ✅ · knowledge sharing ✅ · Bravo project ✅ · English level ✅ · 2-yr goals ✅ · graduation timing ✅ · thesis-vs-release deadline scenario ◑ · project competitions/awards ◑ · willingness to teach ✅ · questions for us (onboarding timeline) ✅ · onboarding = 3-month ramp ✅
- ⚠️ **Missed by extractor:** a TypeScript-experience question (~mid-interview) — candidate: just started, not applied.

**Interviewer style:** question-and-probe (broad concept → clarifying sub-question); hands-on verification (live IIFE); tests "why" not just "what"; smooth technical→behavioral pivot; scenario-based behavioral; validates candidate self-corrections; values practical over theoretical.

**Verifier notes:** 32/34 faithful. FIX applied in wiki: **call stack** holds function calls + local variables; the **heap** holds objects (candidate/extract said vars in heap — wrong). 1 timestamp shift (testing-stages is ~[00:21], not [00:15]).

---

## Cross-interview patterns (the study signal)

**Asked in ≥3 of 5 interviews** (highest-yield prep): async/await + how it works · array transforms (map/filter/reduce/sort/**dedup with Set + spread**) · data types (JS primitives / Dart types) · **const vs final** (Dart) or `==`/`===` (JS) · widget lifecycle + Stateless/Stateful (Flutter) · Container vs SizedBox + **ListView-in-Column** (Flutter) · Git commands + merge conflicts + **rebase** · state management (BLoC/GetX/Provider — Flutter; hooks — React) · strengths/weaknesses + team-conflict + career-plan + English self-rating.

**Recurring candidate failure modes:** confusing type **modifiers** (final/const/static) with **types**; can't transform an array under pressure (forgets Set/spread); can't explain widget **lifecycle** vs listing widget names; "fix" merge conflicts by **renaming the file**; know a term visually (spread, `?.`) but never used it; behavioral answers default to "I'll work harder / all-nighter" instead of **communicate/negotiate/escalate**.
