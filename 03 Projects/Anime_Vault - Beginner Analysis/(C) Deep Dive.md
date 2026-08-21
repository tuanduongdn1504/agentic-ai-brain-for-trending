# (C) Deep Dive — v260 `mranex/Anime_Vault`

**Shipped:** 2026-08-21 · **Wiki:** v260 · **Verdict:** GOAL-ALIGNED INCLUDE 3/4 · **NO MINT** · counts 46/12 UNCHANGED
**Method:** INLINE, fully hand-verified. **No fleet, no subagents** — see *Method* at the end.

---

## 1. What it is

`mranex/Anime_Vault` — *"ANIME VAULT"*, a **local desktop manager for a personal anime collection spread across multiple external hard drives.** README is in Vietnamese, written in a heavy otaku/cultivation-novel register (section headings like *"THẬP ĐẠI THẦN THÔNG"* / *"ten divine powers"*).

The problem it solves is real and specific, and the README states it plainly: you own tens of terabytes across a dozen removable drives, you cannot remember which drive holds which series, your "Plan to Watch" list is so long you spend two hours browsing and then go to bed, and Plex/Jellyfin are too heavy for what is really a desktop cataloguing job.

**The fourth `mranex` repository in four consecutive ships** — manga (v256) → light novels (v257) → video subtitles (v258) → **this**. It takes the same-author control from N=3 to **N=4**, and it is the first application of routine **§42**, which the operator ratified one ship earlier at the v259 audit.

⚠️ **Register note, stated once and not repeated:** the README contains a jokey parenthetical allusion to adult content and a phrase about 2D "Loli/Waifu" characters. It does not affect any technical finding, but it is a fact the operator needs for the pilot decision: **this repository is not citable in a professional context and nothing in it should be vendored.**

---

## 2. Source verification

✅ **Two independent clones, `diff -rq --exclude=.git` clean in both directions.**

| Fact | Value |
|---|---|
| HEAD | `149fc4092af0dce4bcec1029e6f10109185efeda` |
| Commits | **3** on HEAD, **3** on `--all` (`rev-list --count`, D39) |
| Root commits | **1** — `88c0aed` (`rev-list --max-parents=0`, D39) |
| Merges | **0** · **Tags: 0** · refs: `main` only (D27) |
| Identities | 2 — `mranex <elsgman1999@gmail.com>` ×2, GitHub web noreply ×1 |
| Tracked files | **76** |
| Code | 20 `.py` / 7,999 lines · 7 `.tsx` / 3,172 · 3 `.rs` / 97 · 8 `.json` / 3,243 · 2 `.css` / 577 · 15 PNG · 3 `.gitignore` · 1 `.qss` |
| Licence | **Apache-2.0, real 201-line file, in the FIRST commit** |
| **D46 pack check** | **tree == history.** No file was ever added and later deleted. |

### The 87-minute repository

```
88c0aed  2026-05-27 07:24  "Initial commit"   —   2 files, 222 insertions
b64f936  2026-05-27 08:43  "First Commit"     —  74 files, 20,744 insertions, 21 deletions
149fc40  2026-05-27 08:51  "Readme.md"        —   1 file, 145 insertions
```

Three commits, **87 minutes end to end** — by far the shortest window of the four (v256 = 14 days, v257 = 31 days, v258 = 2.4 days). Commit 2 is a **bulk import**: the whole application arrives at once. This repository was never the workspace; it is a destination for code that already existed locally.

⭐ **And commit 1 — the 2 files, 222 insertions — is `.gitignore` (21 lines) + `LICENSE` (201 lines). Nothing else.** The ignore rule, which names `__pycache__/` three separate ways (lines 26–28), existed **79 minutes before the first `.py` file**.

---

## 3. ⭐⭐⭐ Headline 1 — the manifest is the fossil

The README (145 lines) mentions **FastAPI 9 times** and **Tauri 10 times**. It mentions PyQt/Qt/`.qss` **once**, and `app.py` **zero** times. It contains an accurate Mermaid diagram of a three-layer architecture, and it declares the migration outright:

> *"Được kế thừa và nâng cấp toàn diện từ phiên bản PyQt6 cổ lỗ sĩ"* — **"inherited and comprehensively upgraded from the antiquated PyQt6 version."**

The documented install sequence is three commands:

```
pip install -r requirements.txt      (README:94)
npm install                          (README:100)
npm run tauri dev                    (README:107)
```

And `requirements.txt`, the **only** Python dependency declaration in the repository, is two lines:

```
PyQt6>=6.7,<7
pyinstaller>=6,<7
```

🔴🔴 **`fastapi`, `pydantic` and `uvicorn` — imported at `movie_vault/server.py:10`, `:11`, `:12` and launched at `:661` — appear in it zero times** (extent: 3 manifests in the tree, only `requirements.txt` is Python; `grep -ci` per package = 0, 0, 0).

⇒ ⭐⭐⭐ **The README describes generation 2 nine times over, and the only machine-readable dependency declaration in the repository describes generation 1 — the generation the README itself calls antiquated.** The install list is a fossil of the program the documentation was written to replace.

This is the third distinct mechanism for one outcome across the set:

| Ship | Mechanism | Outcome |
|---|---|---|
| v256 | the web app was deleted; `requirements.txt` was not touched | manifest describes a **deleted** program |
| v257 | README's primary command is `python run.py`, which opens generation 1 | instructions launch an **older** program |
| v258 | no manifest exists at all; the README carries 7 unpinned packages | instructions are **unversioned prose** |
| **v260** | manifest lists the predecessor's deps; the documented app's are absent | manifest describes the **undocumented** program |

⇒ ⭐⭐⭐ **Four repositories, four mechanisms, one outcome: in every one of this author's projects, the instructions for making the program run describe something other than the program.** Under §42 clause 3, an outcome reached through *different* mechanisms is stronger evidence of a disposition than one that repeats identically. **This is the strongest disposition in the set.**

---

## 4. ⭐⭐⭐ Headline 2 — the complete silent-failure chain, and the README documents the part that hides it

The documented app does not run the Python directly. The Rust shell spawns it (`src-tauri/src/lib.rs`, per-file line numbers):

```rust
:42   let mut cmd = Command::new("python");
:46      cmd.arg("-m")
:47         .arg("movie_vault.server")
:48         .arg("--host")
:49         .arg("127.0.0.1")
:50         .arg("--port")
:51         .arg("5000");
      // Prevent command prompt popups on Windows in both dev and production
:57      cmd.creation_flags(0x08000000); // CREATE_NO_WINDOW
:60   match cmd.spawn() {
         Ok(child) => { println!("Successfully launched Python API server"); ... }
:66      Err(err) => eprintln!("Failed to spawn Python API server: {}", err),
```

✅ The port **matches** — the frontend hardcodes `http://127.0.0.1:5000` in **23 places**, and `server.py:657` defaults to `--port 5000`. No mismatch.

🔴 But three independent mechanisms each convert a loud failure into a silent one:

1. **`cmd.spawn()` answers the wrong question.** It returns `Ok` when the `python` **binary** launches. It knows nothing about whether `python -m movie_vault.server` then dies on `ImportError: No module named 'fastapi'`.
2. **`println!("Successfully launched Python API server")` asserts a success it never verified** — printed on the strength of the spawn, not of the server.
3. **`CREATE_NO_WINDOW` deliberately removes the output channel** the traceback would have used, and the comment says it applies *"in both dev and production."*

⇒ 🔴🔴 **The README's own install sequence guarantees this failure.** `pip install -r requirements.txt` installs PyQt6 and pyinstaller and neither FastAPI nor uvicorn nor pydantic. The app then opens, renders its Cyberpunk UI, prints *"Successfully launched Python API server"*, and every one of its 23 API calls fails — with the actual cause suppressed by design on Windows.

⭐⭐⭐ **And the README documents the mechanism that conceals its own defect.** Section 2 names `CREATE_NO_WINDOW` explicitly, in prose, as a feature: the Python server is summoned *"ở chế độ ẩn danh hoàn toàn"* — in fully anonymous mode. He described the thing that will hide the error, accurately, in the same document that tells you to install the wrong dependencies.

⚠️ **Extent and limits, stated:** this is **read-derived, not executed.** `python3`/`pip` are SIGKILLed in this sandbox and there is no Windows host, so I ran nothing. The chain is legible from code I quoted myself. In `tauri dev` on macOS/Linux the Python traceback would reach the dev console; in a packaged Windows build, per `:57`, it would not.

⭐⭐ **The rule:** `spawn()` tells you a process **started**, not that it is **running** — and a success message printed on the strength of a spawn is a false success. That is v251's FALSE SUCCESS class (exiftool exiting 0 while the original bytes survive) at **N=2 in the corpus, by a different mechanism.**

---

## 5. ⭐⭐⭐ Headline 3 — the shared core, and the direct answer to v258

v258's best finding was that **code moves forward in time and never backward**: an alignment guard invented in v256 was copied into v258 eleven days later and never reached v257, because copy-forward is a one-way ratchet and nothing carries a fix back. The generalisation was that only a **shared library** makes a fix travel in both directions — and the operator's live open decision from the v259 audit is exactly this, applied to `05 Skills/`.

**This repository is the same author solving that problem, correctly, inside one project.**

```
movie_vault/core/          ← ONE shared layer
  db.py               2,134 lines / 66,794 B
  randomizer.py         187 lines
  scanner.py            195 lines
  backup.py             170 lines
  hdd_identifier.py     297 lines
  paths.py              104 lines

THREE front ends over it:
  app.py                     — a CLI          (imports core.backup, core.db, core.hdd_identifier)
  movie_vault/ui/*.py        — the PyQt UI    (6 modules, all importing core.*)
  movie_vault/server.py      — a FastAPI API  (imports db, hdd_identifier, scanner, randomizer, backup, paths)
                                → consumed by frontend/ (React) inside src-tauri/ (Tauri)
```

`server.py:14` carries the comment **`# Import existing core modules`** — the author writing down, in the file that bridges old to new, that he is reusing rather than reimplementing.

⭐⭐⭐ **And the load-bearing function is genuinely shared:** `pick_random_item` — the app's entire point — lives once, in `core/randomizer.py:64`, and is called by **both** UIs: `movie_vault/ui/random_page.py:37` and `movie_vault/server.py:35`. A fix to the picker reaches the PyQt app and the React app at the same time. **That is the ratchet defeated, and it is the thing v258 said nothing in his workflow was doing.**

### ⚠️ But the sharing leaks, and the leak is instructive

Two randomisation sites were reimplemented in TypeScript rather than called over the API:

- `frontend/src/components/Library.tsx:144` — `const pool = [...items].sort(() => Math.random() - 0.5);`
- `frontend/src/components/RandomPicker.tsx:144` — `const shuffledDeck = [...CYBER_TAROT_DECK].sort(() => 0.5 - Math.random());`

Both use the classic **biased comparator shuffle**. `Array.prototype.sort` with a random comparator is not a uniform permutation — the result depends on the sort implementation's comparison order, and the distribution is measurably skewed. Fisher–Yates is the correct algorithm and is four lines.

⭐ **Fairness, and a correction to my own first reading:** the **primary pick is not affected.** `RandomPicker.tsx:156` does `fetch('http://127.0.0.1:5000/api/random/pick', …)` against `server.py:556`, which calls the shared 187-line `pick_random_item`. The two biased shuffles govern the Library's browse pool and a 15-card cosmetic "cyber tarot" deck. My earlier framing — *"the new UI grew its own duplicate randomization anyway"* — was too strong and is withdrawn: **the load-bearing path is shared; two secondary paths were re-implemented in the front end with a biased idiom.**

⇒ ⭐⭐ **The refined rule: extracting a shared core makes fixes travel, but it does not stop a new front end from re-implementing what it could have called. The ratchet is defeated by architecture and re-created by convenience** — 187 correct lines sat one HTTP call away from two incorrect ones.

---

## 6. ⭐⭐⭐ Headline 4 — the N=4 habit table, and the confound that changes the v257 conclusion

§42 clause 2: *verify every row with commands in every clone; do not assume symmetry.* Done. Repos ordered by **creation date**, not ship order:

| Habit | v257 (Apr 26) | v256 (May 13) | v258 (~May 24) | **v260 (May 27)** | N=4 |
|---|---|---|---|---|---|
| 1 · ignored-yet-tracked bytecode | 18 `.pyc`, rule written 26 days late | tracked, rule same commit | 10 `.pyc`, rule deleted mid-flight | **0 tracked, 0 ever added** — rule 79 min *early* | **BREAKS** |
| 2 · run-instructions describe a different program | launches gen 1 | manifest describes deleted app | no manifest at all | **manifest = the undocumented app** | **REPLICATES** |
| 3 · committed machine paths | `C:\Users\Admin\Desktop\` in 2 screenshots | `C:\Nghich\…` in a generated `.bat` | — | **0** across 15 PNGs, both encodings, and 0 in text | **BREAKS** |
| 4 · dead generations in tree or pack | 3 generations + 2 orphan `.pyc` | 4 context-less artifacts | a deleted app in the pack | **none — D46-verified** | **BREAKS** |
| 5 · no CI, no tests, no agent surface | 0 | 0 | 0 | **0 tests of 76 files · 0 `.yml` across all 3 commits · 0 agent files** | **REPLICATES** |
| 6 · unbenchmarked headline number | *"80% token saving"* | VRAM figures | *"90%+"* dedup | **no numeric claim exists** | **BREAKS** |

**Four of six break.** At N=3 I called these six habits dispositions. At N=4 that claim does not survive — and the reason is one variable I had not been recording.

⭐⭐⭐ **The confound: habits 1, 3, 4 and 6 are only observable in a repository that was the workspace.** Committed bytecode, committed machine paths and dead generations all **accumulate over time in the directory you work in**. v257 ran 31 days in its repo, v256 14 days, v258 2.4 days. **v260 was a bulk import**: the code was finished before the repository existed, so `git init` → `.gitignore` → push produces a clean tree with no change in behaviour whatsoever. Habit 6 breaks for the same structural reason — the README was written **8 minutes** after the code landed, as a stack-badge install sheet, with no room for a performance claim.

⇒ ⭐⭐⭐ **§42 AMENDMENT CANDIDATE (this ship's method contribution): the same-author control must record, per repository, whether the repository was the WORKSPACE or a DESTINATION. Habits that accumulate in a working directory are structurally unobservable in a bulk import, and reading their absence as discipline mistakes workflow for character.**

### ⚠️ This materially corrects a v257 conclusion I set in bold

At v257 I wrote: *"Not a learning curve. Two projects side by side, one tended and one not."* That was the right read of N=2. At N=4, with creation dates visible, the bookkeeping outcomes improve from the first-created repository to the last — but **not monotonically** (v258 regresses on the ignore-rule axis, having *deleted* its `.gitignore` mid-project). And the improvement has a mechanical explanation that requires no learning at all.

⭐ **The honest N=4 statement: neither a learning curve nor mere inattention — a workflow difference that mimics both.** What survives the control are exactly the two habits that are *independent* of where the code was written: **the run-instructions defect (habit 2) and the total absence of any verification (habit 5).** Those two are properties of the author. The other four were properties of the directory.

---

## 7. ⭐⭐ What is genuinely good — and this is the best of the four

- ⭐⭐⭐ **The shared core** (§5). Three front ends, one data layer, the load-bearing function called not copied.
- ⭐⭐ **The architecture documentation is accurate and verifiable.** The Mermaid diagram's claims — WebView ↔ port 5000 ↔ FastAPI, Rust auto-spawning the background Python, Rust killing it on close — all check out against `lib.rs`. **Best README of the four on the architecture axis.**
- ✅ **SQL posture is clean across a 2,134-line data layer:** 68 `execute(` calls, **0** f-string SQL, **0** `%`-format SQL, 85 `?` placeholders. Best of the four.
- ✅ **Zero `shell=True`** anywhere in 20 `.py` files (v257 had two, in the program its README told you to launch).
- ✅ **The only bounded dependency pins of the four** — `PyQt6>=6.7,<7`, `pyinstaller>=6,<7`. Both carry upper bounds. (v256's 24 lines contained two mutually unsatisfiable pins; v257 had an unbounded `openai>=1.0.0` major floor; v258 had no manifest.) The irony is total: the best-formed manifest in the set describes the wrong program.
- ✅ **A real Apache-2.0 licence file, in the first commit** — the clearest grant of the four (v256 AGPL added by the final commit; v257 nothing at all; v258 MIT asserted in prose with no file).
- ⭐ **The claimed features are actually implemented.** `pick_random_item` takes 14 parameters — tag include/exclude with `any`/`all` match modes, `min_rating`, watch-status filtering, `require_videos`, and the README's *"thuật toán kháng lặp"* (anti-repeat algorithm) is real: `avoid_recent=True, avoid_recent_limit=20`, with a `fallback_used` field returned so the caller knows when the filter had to relax. It returns a structured refusal with a human-readable `message` when no watch status is selected rather than raising.
- ⭐ **Two genuinely thoughtful domain designs:** a hidden `.vault_id` UUID file written to each drive, so a catalogue entry survives the drive being unplugged and the library stays browsable offline; and cover art written **into the media folder itself**, so artwork travels with the drive to another machine.

---

## 8. 🔴 Defects beyond the headlines

- 🔴 **CORS wildcard with no authentication.** `server.py:46-49`: `CORSMiddleware` with `allow_origins=["*"]`, `allow_credentials=True`, `allow_methods=["*"]` — and **0** hits for `Depends|api_key|token|Authorization` across the whole file. The server is loopback-only (`127.0.0.1`), which limits the blast radius, but while the app is running **any web page open in any browser on that machine can issue requests to it** — and the API performs filesystem scanning and database writes. The wildcard additionally makes the responses readable. ⭐ **This is the fourth repository in the set and the third with a broken-auth-shaped defect** — the corpus's own v231/v232 triad is the reference class.
- 🔴 **Silent degradation on a missing stylesheet.** `main_window.py:195-199`: `_load_stylesheet` resolves `movie_vault/ui/styles.qss` and returns silently if it does not exist. The app runs unstyled with no warning. Structurally identical to v257's missing `00_json_output_policy.txt` rendering a prompt with no JSON contract and no warning — **N=2 for this idiom in the set.**
- 🔴 **Zero tests of 76 files; zero CI across all 3 commits, on any ref.** Nothing in this repository can notice any of the above. The manifest/README divergence in particular is a one-line CI check away from impossible.
- ⚠️ **A live generation the README calls antiquated and never tells you how to run, or not to.** The PyQt UI is ~130 KB of shipped code (`library_page.py` 37,878 B, `random_page.py` 34,624 B, `hdd_page.py` 18,114 B, plus a wired stylesheet), reachable via `app.py`, which the README names zero times. This is **not** v257's undeclared-three-generations defect — the migration *is* declared in prose. It is the honest twin: the old generation is present, acknowledged as the predecessor, and simply never addressed as a thing still in the tree.
- ⚠️ **The HDD page has no React counterpart file**, but HDD functionality is spread across `App.tsx`, `Dashboard.tsx`, `Sidebar.tsx`, `Library.tsx` and `RandomPicker.tsx`. ⚠️ **This corrects my own intermediate hypothesis** — I inferred from the file listing that the feature was missing from the new UI. Absence of a file named `Hdd.tsx` is not absence of the feature. A §43.1 instance in my own hands: I generalised from where I chose to look.

---

## 9. Non-claims (stated so they cannot be inferred)

- **NOT** a mint of any kind. **NO MINT** — see the Verdict for the five grounds.
- **NOT** #52 — 15 PNGs and page-stated figures only; the GitHub API is mocked here (§37.4). No velocity claim.
- **NOT** #57 — no corpus subject is cited, depended on, or influenced. The only corpus relationship is authorial (the three sibling ships).
- **NOT** world-first, and **not** corpus-first for a capability. It **is** the corpus's first **personal media-library / collection-manager** subject (hand-grep: `Jellyfin` 0, `media server` 0, `media librar` 0, `gacha` 0, `otaku` 0 in both `_state/03c` and `_patterns/06`; ⚠️ `Plex` returned 28 hits which are **all** `multiplexer`/`complex`/`Perplexity` — a false positive of the same family as the `ScrollMode`→`llm` hit in §10). Domain-not-capability ⇒ a corpus-knowledge data-point.
- **NOT** executed. No Python ran; no Windows host. Every runtime claim in §4 is read-derived and labelled.
- **NOT** an LV-C7 Tauri-desktop cluster *instance* worth recording beyond a data-point — it joins cc-switch v73 / CodexPlusPlus v117 / OpenHuman v118 / PilotDeck v175 / meetily v196 / tabularis v212 / voicebox v229 as a bookkeeping cross-reference only.
- **NOT** a v192/§A#24 instance — there is no MCP server, no agent surface, nothing first-party for an agent to call.

---

## 10. Method — and the error ledger

**Shipped INLINE, hand-verified, no fleet.** Three reasons, stated rather than assumed: the standing session instruction is not to use workflow orchestration unless the operator asks for it and this turn did not; §43.1 records that my reliable mode is reading a file and quoting it, which is the entirety of this ship; and the fleet's contribution across v256–v258 was mixed at best — **context bleed for five consecutive ships**, fabricated files, and an anti-critic that proposed repairs to the subject. v236 is the corpus precedent for an inline ship. Every `path:line` in this document is one I read in my own command output.

**Every negative here states the extent of the search that produced it** (§43.1).

### Errors — 3, all mine, all caught before publication

1. 🔴 **I cited Rust line numbers taken from `cat src-tauri/src/*.rs | grep -n`** — a concatenation of three files, so the numbers were offsets into the concatenation, not into any file. Caught before anything downstream used them and re-derived per file. ⇒ ⭐ **New rule candidate D48: line numbers from a `cat` of a glob are not file line numbers. `grep -n` the file list, never the concatenation.**
2. ⚠️ **I inferred the React app had dropped the HDD page** from the absence of `Hdd.tsx`. It has not — the feature is distributed across five components. §43.1 in my own hands.
3. ⚠️ **I framed the biased shuffles as the new UI reimplementing the shared picker.** Partly true — but **not on the primary path**, which correctly calls `/api/random/pick`. Withdrawn and restated in §5.

### Two false positives worth keeping

- **`ScrollMode` matches `llm`** case-insensitively (`Scro`**`llM`**`ode`). My AI/LLM surface grep returned exactly one file, and that was it. The correct finding is **zero LLM or agent surface in the entire tree**.
- **`Plex` matches `multiplexer`, `complex`, `Perplexity`** — 28 corpus hits, none of them Plex.

⇒ ⭐ Both are D42's cousin: **a positive from an unanchored substring is not a positive.** D47 says anchor the basename in filename greps; these say anchor the token in content greps too.

### Sandbox

`python3` and `pip` exist at `/usr/local/bin/` and are **SIGKILLed on invocation** — silently, inside a pipe (**D41**). `timeout` is absent. `git` is 2.19, so `git branch --show-current` does not exist. **Nothing was executed; every runtime claim is labelled read-derived.**
