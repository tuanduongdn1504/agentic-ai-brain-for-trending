# Caveats & corrections

Read this before quoting anything. The source is **doubly-garbled ASR** and the extraction had one failure-and-recovery. Everything load-bearing is surfaced here (Rule 12: fail loud).

## ⚠️ The captions are doubly garbled — not quotable

Each video had two auto-caption tracks: **Vietnamese-original** (ASR of Vietnamese speech with English tech terms) and **English** (machine translation *of* that ASR). Both introduce errors; the English one mangles nearly every technical term. **Every technical term in this wiki is a reconstruction of intent**, cross-referenced across both tracks + domain knowledge. Do not quote the raw captions as anyone's exact words.

### Garble → term map (verified reconstructions)

| Heard (en/vi ASR) | Actual term |
|---|---|
| `Rnative`, `Reactive('s) technology`, lone `R` | React Native / React |
| `Flashbox` | Flexbox |
| `GD`, `GCK` | CSS Grid |
| `Fet 1`, `Flash 1` | `flex: 1` |
| `Isaac`, `IAC`, `AC` ("a JS library") | Axios |
| `order function` | higher-order function |
| `TD tag` / `TD card` | `<td>` HTML tag |
| `.abb`, `ABB`, `.ch`, `file A` | `.aab` (Android App Bundle) |
| `SHSH blobs`, `SH2` | SHA-1 / SHA-256 signing fingerprint |
| `Flter` | Flutter · `đát` → Dart |
| `bloc` | BLoC · `getx`/`provider` → state-mgmt libs |
| `Bit O` | Big O |
| `material pay` | MaterialPageRoute |
| `make it solid` | setState / stateful |
| `gigit`, `kick`, `g` | git · `gig fake`/`gig m` → rebase/merge |
| `hit` (video 5, storage) | heap |
| `git xưa` (video 1) | git rebase (context inference) |

## ⚠️ Technical corrections applied (candidate/extraction was wrong; wiki is right)

1. **Dart `const` vs `final` — inverted by the candidate (video 2).** Correct: `const` = compile-time constant; `final` = assigned once at runtime; both immutable. The interviewer corrected him live. Extraction note: the extractor's *summary* echoed the candidate's inverted claim, but tagged the verdict "wrong" correctly — the wiki states the correct version. → [[04-flutter-and-dart]]
2. **Flutter lifecycle methods are on the `State` class, not `StatefulWidget` (video 1).** Only `createState()` belongs to `StatefulWidget`; `initState/build/didUpdateWidget/dispose` are `State` methods. Minor at junior level, but stated correctly in the wiki. → [[04-flutter-and-dart]]
3. **Call stack vs heap (video 5).** Candidate said local variables live in the heap. Correct: the **call stack** holds function calls + local variables; the **heap** holds objects/reference types. → [[02-async-and-event-loop]]
4. **`git checkout -B` vs `-b` (video 2).** Candidate used uppercase `-B`; the everyday create-and-switch is lowercase `-b`. `-B` is create-or-reset (force). → [[07-git-testing-and-engineering-practice]]

## ⚠️ Candidate misconceptions preserved as *cautionary examples* (not corrected into fact)

These are recorded faithfully as "what a candidate said wrong", because the *learning value is seeing the mistake*:

- Async means "data types not consistent" (video 3) — **wrong**; async = non-blocking. → [[02-async-and-event-loop]]
- "Fix merge conflicts by renaming the file" (video 1) — **dangerous anti-pattern**. → [[07-git-testing-and-engineering-practice]]
- CSS `position` "values" = `top/left/bottom/right` (video 3) — those are **offset properties**, not position values. → [[06-css-html-and-web-fundamentals]]
- SSR ≡ MVC (video 5) — conflates a **rendering strategy** with a **code-organisation pattern**. → [[03-react-and-hooks]]

## ⚠️ Faithfulness / timestamp flags (recorded, don't change any answer)

- **Video 2:** "git pull vs rebase" item is probably **rebase-vs-merge** and/or shifted to ~[00:11]; the const/final summary inverted the candidate's words (verdict still correct).
- **Video 5:** "testing stages" is ~[00:21] not [00:15] (~6-min shift); a **TypeScript-experience** question was missed by the extractor.
- **Video 1:** live-coding array section = **4 distinct questions** (add / remove-6 / sort-desc / dedupe) compressed into one item.
- **Video 4:** three items discussed but not split out (env-config UAT/Dev/Prod, Kotlin-as-3rd-platform, specialisation-sequencing).

## ⚠️ Extraction failure & recovery (the process fault, surfaced)

The first Workflow (`wf_89de7c46-db7`) extracted **3/5** videos. Videos **2 (aKMV, the 64-min one)** and **3 (0n8o)** hit the **StructuredOutput retry cap (5×)** — the most likely cause is *too-long output truncating the JSON* against a strict schema (`additionalProperties:false`, many required fields). A second Workflow (`wf_2408264b-657`) **recovered both** with a **looser schema + a ~30-item cap + a compact-output instruction** (≤55-word model answers). No content was silently dropped; the recovery is logged and the counts reconcile (170 items total). This is recorded so the next multi-hour interview build uses the looser schema from the start.

## ⚠️ Name / identity uncertainty

Video 1's candidate at one point says "my name is Duy" while the file is titled "Vũ Thành Long"; ASR garbles names heavily and video 2's interviewer style notes also surfaced a "Duy". Names are **provenance only** — the value is the questions, not who answered. The hiring company "Innovo" is a best-guess reconstruction of garbled "Eno"/"Enovo".

## Key Takeaways

- **Trust the wiki's verified answers, never the raw captions.**
- 4 technical corrections applied; 4 candidate misconceptions preserved as cautionary examples.
- One extraction pass failed on 2/5 and was recovered with a looser schema — surfaced, not hidden.

**Back to** [[_index]] · **verdicts:** [[claims-scorecard]] · **sources:** [[source-provenance]].
