# (C) Deep Dive — `mranex/VOCra` (wiki v258)

**Ship:** v258 · **Date:** 2026-08-21 · **Verdict:** GOAL-ALIGNED INCLUDE 3/4 · **NO MINT** · counts 46/11 UNCHANGED
**Subject:** *"VoCRA & VoCRA Translator"* — a PySide6 desktop toolchain that extracts **hardcoded (burned-in) subtitles** from video by cropping a region, SSIM-deduplicating frames, OCRing the survivors with a local vision model, then LLM-translating the result; plus a second app for translating existing subtitle files (SRT/ASS/VTT). README in Vietnamese.
**Author:** `mranex` — pseudonymous. Not Anthropic, not a registered vendor-direct source (§41 ⇒ **(a) FAILS**).
**⭐ Why this ship exists:** it is the **third** repository by this author in three consecutive ships — manga/image (v256) → light novels/text (v257) → **video (v258)**. That turns the v257 same-author control from N=2 into **N=3**, and §4 is the result. It is the most valuable section here, and it corrected me twice.

---

## §0 — Source verification (D27: ref population declared)

Two independent clones, `diff -rq --exclude=.git` **both directions: identical**.

| Fact | Value | Command |
|---|---|---|
| HEAD | `9cc598bb39d45cd2033c643f35de907e104197b7` | `git rev-parse HEAD` |
| Commits HEAD / all refs | **6 / 6** | `git rev-list --count HEAD` / `--all` |
| Root commits | **1** (`1b8a3ec`, 2026-05-26 09:00 +0700) | `git rev-list --max-parents=0 --all` |
| Merges | **0** | `git rev-list --count --merges --all` |
| Tags | **0** | `git tag` |
| Refs | `main` only | `git branch -a` |
| Tracked files | **93** | `git ls-files \| wc -l` |
| Python | **75 files / 9,641 lines** | `git ls-files '*.py' \| xargs wc -l` |
| Also | **10 `.pyc` TRACKED**, 2 `.qss`, 2 `.png`, 2 `.md`, 1 `.json`, 1 `.bat`; **no `.gitignore` in the tree** | — |
| Window | **2026-05-26 09:00 → 2026-05-28 19:28** ≈ **2.4 days** | `git log` |
| Identities | `mranex <elsgman1999@gmail.com>` **5** · GitHub noreply **1** (the `Initial commit`) | `git shortlog -sne --all` |
| Page-stated | **3 stars / 0 forks / 0 watching** | rendered repo page |

Page-stated figures only — the GitHub API is mocked here (§37.4) ⇒ **no Pattern #52 claim**.

⭐ **Six commits, and their subjects are the whole plot:** `Initial commit` → `First Commit` → `Upload Docs` → `Big update 1` → `Big Update 2` → `Update Burn Video`. ⭐ **9,641 lines of Python in 2.4 days** — the fastest of the three siblings (v256: 54,977 lines in 14 days; v257: 12,561 in 31).

---

## §1 — What it is

Two applications in one repository, and the split is deliberate (§3):

- **VoCRA** (`main.py` → `vocra_gui/` + `vocra_core/`): video in → `frame_extractor` → interactive region `cropper` → `ssim_filter` (drop near-identical frames) → `draft_ocr` (fast/local first pass) → `final_ocr` (PaddleOCR-VL via llama.cpp, an OpenAI-compatible endpoint, or Google Lens) → `segmenter` + `timestamp_utils` (frames → subtitle timings) → `text_cleaner` → `translator` → `exporter` → optional `burner` (re-burn translated subs with ffmpeg).
- **VoCRA Translator** (`vocra_translator_main.py` → `vocra_translator/`): a smaller app that imports an SRT/ASS/VTT file, shows a side-by-side table, batch-translates, and exports back.

The stack: **PySide6** (⭐ note: both siblings used **PyQt6** — a third toolkit choice across three repos), llama.cpp for local inference, ffmpeg for video, SSIM for frame deduplication.

---

## §2 — ⭐⭐⭐ THE HEADLINE: one commit, eight hours in, deleted the application, the ignore rule, and 252KB of its own reasoning

The repository's second commit (`cd647e2`, "First Commit", 09:11) added a **layered application**: an `app/` service layer (`service.py`, `state.py`, `models.py`, `ocr_service.py`, `ocr_run_service.py`, `ocr_compare_service.py`, `prepare_service.py`, `prepare_run_service.py`, `review_service.py`, `package_service.py`), a `cli/` layer (`main.py`, `gui_cmd.py`, `ocr_cmd.py`, `package_cmd.py`), a `gui/` layer (9 files including a **93,391-byte** `main_window.py`), plus `__main__.py` and a `_version.py`.

One minute later (`3c8d5ab`, "Upload Docs", 09:12) it added two documents: **`docs/Plan.md`** (19,771 bytes / 1,178 lines) and **`docs/progress.md`** (**232,097 bytes / 2,064 lines**).

Eight hours and eight minutes after that, **`7e5f67d` "Big update 1"** (17:19) did this:

```
223 files changed, 7158 insertions(+), 20339 deletions(-)
89 deletions (D), including:
   D  .gitignore
   D  app/service.py, app/state.py, app/models.py, app/ocr_service.py, …   (the whole service layer)
   D  cli/main.py, cli/gui_cmd.py, cli/ocr_cmd.py, cli/package_cmd.py       (the whole CLI)
   D  gui/main_window.py, gui/ocr_tab.py, gui/review_tab.py, …             (the whole GUI)
   D  docs/Plan.md
   D  docs/progress.md
   D  __init__.py, __main__.py, _version.py
80 additions of .pyc
```

⭐⭐⭐ **In a single commit on day one, the author deleted a three-layer application, its command-line interface, its GUI, its version file, its `.gitignore`, and 252KB of its own planning and progress documentation — deleting nearly three times as many lines as he added — and began committing bytecode in the same change.**

The `.gitignore` that commit removed had `__pycache__/` on line 2 and `*.py[codz]` on line 3. **The commit that deleted the ignore rule is the commit that added the first 80 files it named.** That is not an oversight in the ordinary sense: the guard was removed and the guarded files arrived together.

⚠️ **What this is not.** This is not a story about a careless developer shipping junk — the *result* of that commit is the current, cleaner `vocra_core/` + `vocra_gui/` architecture, and §7 shows it is in several respects the best-built of the three siblings. It is a story about **what survives a rewrite**: the code was replaced deliberately, and the documentation, the ignore rule and the version file were casualties nobody came back for.

---

## §3 — ⭐⭐⭐ 262KB of planning written in 2.4 days; 98.7% of it deleted; the survivor is the only decision the code honours

Four planning documents exist in this repository's six-commit history. All four, with their fates:

| Document | Size | Lines | Added | Fate |
|---|---|---|---|---|
| `docs/progress.md` | **232,097 B** | **2,064** | `3c8d5ab` 2026-05-26 | **deleted same day** (`7e5f67d`) |
| `docs/Plan.md` | 19,771 B | 1,178 | `3c8d5ab` 2026-05-26 | **deleted same day** (`7e5f67d`) |
| `total_plan.md` | 6,900 B | 157 | `7e5f67d` 2026-05-26 | **deleted next day** (`3eb4023`) |
| `vocra_translator/plan.md` | 3,306 B | 75 | `3eb4023` 2026-05-27 | ✅ **still tracked** |

**Written: 262,074 bytes / 3,474 lines. Surviving: 3,306 bytes / 75 lines — 1.26% by bytes, 2.2% by lines.**

⭐ **And the chain is a ladder, each rung an order of magnitude smaller than the last:** 3,242 lines of `Plan.md` + `progress.md` → replaced by 157 lines of `total_plan.md` → replaced by 75 lines of `plan.md`. **The smallest is the only survivor.**

**What `docs/progress.md` was.** Its eleven headings are the canonical shape of an AI coding assistant's working-memory file: *Current Goal · Current Status · Completed · In Progress · Not Started · Blockers / Risks · Architecture Decisions · Files Changed · Tests / Checks Run · Next Recommended Steps.* Two thousand and sixty-four lines of it, for a project that was three hours old. ⚠️ **It names no tool** — a grep for `claude|codex|gpt|copilot|antigravity|jules|gemini|cursor` across it returns nothing — so the shape is an agent's and the provenance is not stated. (For context, the v256 sibling carried a Google **Jules** agent memory file, and the v257 sibling has a commit subject reading `Antigravity new version`.)

⭐⭐⭐ **Now the part that matters.** The 75-line survivor, `vocra_translator/plan.md`, states its decisions plainly — among them that the second app is separate but **reuses `vocra_core.translator.*`**, with its own settings and secrets files. **That decision is honoured in code:** `vocra_translator/core/provider_factory.py:3–5` imports `BaseTranslator`, `LlamaLocalTranslator` and `OpenAICompatibleTranslator` from `vocra_core.translator.*`, and `vocra_translator/core/app_config.py:86` reads defaults from `vocra_core/default_config.json`.

**And it protected exactly the surface it named, and nothing else.** The plan discusses the translator core; it says nothing about widgets. So:

| Shared surface | Named by the plan? | Result |
|---|---|---|
| translator providers | **yes** | ✅ **imported** from `vocra_core.translator.*` |
| `scene_nav_button.py` | no | 🔴 **byte-identical copy**, 117 lines, in both apps |
| `log_panel.py` | no | 🔴 near-identical copy, 18 lines, **2 lines differ** |
| `subtitle_table.py` | no | ⚠️ copied then diverged, 52 vs 61 lines, 29 lines differ |
| `theme.qss` | no | ⚠️ near-identical, 215 vs 217 lines, 14 lines differ |
| `icon.png` | no | 🔴 **byte-identical, 788,588 bytes, committed twice** — ~1.5MB of a 3.9MB clone is two copies of one icon |

⭐⭐⭐ **A plan document is a fence around the surfaces it names.** The one layer the surviving plan discussed is shared by import; every layer it did not mention was copy-pasted, one of them byte-for-byte and one of them a 788KB binary duplicated. **So the actionable form of the rule is: name the boring surfaces too.**

---

## §4 — ⭐⭐⭐ THE N=3 SAME-AUTHOR CONTROL

Three repositories, one author, overlapping months. v257 established six replicating "bookkeeping" habits at N=2 and proposed *habits are the constant, quality is the variable*. Here is that table tested at N=3 — **with two corrections to my own first draft, both found by running the command instead of assuming symmetry.**

| # | Habit | v256 (manga) | v257 (novels) | v258 (video) | N=3? |
|---|---|---|---|---|---|
| 1 | ignored-yet-tracked files | rule + exception in **one commit** (`bdcb098`) | files at root, rule **26 days later** (`7a590cb`), never removed | **rule at root, then DELETED by `7e5f67d` — which added 80 `.pyc` in the same commit** | ✅ **three distinct routes, one outcome** |
| 2 | one fact declared many times | stage DAG in 3+ files | threshold in 3 places, **values disagree** (0.72/0.82 vs 0.8) | SSIM `0.95` in **8 places — all agreeing** | ✅ form replicates; **disagreement does not** |
| 3 | committed artifacts carrying the author's machine path | `C:\Nghich\Manga-Translator\` in a generated `.bat` | `C:\Users\Admin\Desktop\` in two screenshots | **`C:\Nghich\vocra\` in a generated `.bat`** | ✅ and **N=2 in the identical form** |
| 4 | dead generations left in the tree | 4 orphan artifacts | 3 coexisting generations | ⚠️ **not in the tree — but a whole app in the pack** (§2) | ✅ *after correction* |
| 5 | no CI, no tests, no agent surface | none ever | none ever | **0 yml in 6 commits · 0 tests of 93 · 0 agent files of 93** | ✅ |
| 6 | unbenchmarked headline number | VRAM figures | "80% token saving" | **"100% of noise", "90%+ of duplicate frames"** | ✅ |

**Diverging axes** (where quality varies rather than replicating):

| Axis | v256 | v257 | v258 |
|---|---|---|---|
| `shell=True` | 0 in 152 files | **2 in 47**, one from a text field | **0 in 75** |
| alignment validation | **five layers** | **none** | **present** — count + per-item index (§5) |
| README images | broken (never existed) | working | **broken** — a `your-username` placeholder that 404s |
| licence | AGPL-3.0 **file**, final commit | **none at all** | **MIT claimed in prose, no file** |
| planning documents | 1 (inherited, deleted) | **0, ever** | **4 written, 3 deleted** |

**Two corrections to my own draft, both mine and both caught by running the command:**

1. 🔴 **Habit 4 nearly went in the table as "does not replicate."** My import-trace found **zero** unimported modules in the tree — and I sanity-tested that detector against a planted name to confirm it can fire. But the *pack* holds a deleted three-layer application (§2). **The tree is clean; the history is not.** The honest verdict is that the habit replicates, in a different place.
2. 🔴 **I attributed `plan.md` to v257.** It is VOCra's own file (`vocra_translator/plan.md`). A survey of `git ls-files '*.md'` in all three clones settles it: v256 has 3 markdown files, **v257 has exactly one — its README** — and v258 has two. **v257 has never had a planning document of any kind.**

⭐⭐⭐ **And that second correction produced the most interesting result in the ship, because it makes the correlation measurable across three points:**

| | planning docs written | the surface quality that followed |
|---|---|---|
| **v257** | **0, ever** | README launches the wrong program · 3 thresholds that disagree · 2 `shell=True` · no alignment guard |
| **v256** | 1, inherited, deleted | 4 artifacts whose context was deleted · a module that cannot be imported |
| **v258** | **4 written, 1 survives** | ✅ the surviving plan's decision honoured by imports · 0 `shell=True` · alignment guard present · a real provider abstraction |

⚠️ **N=3 is three points and I am not claiming a law.** The direction is consistent and the mechanism is legible — a plan fences the surfaces it names (§3) — but a sample of three from one author supports a hypothesis, not a finding. What it does support is the sharpened statement: **the repository where the most reasoning was written down is the best-built one, the repository where none was is the worst-built one, and within the best one the discipline stops exactly at the edge of what the surviving document mentions.**

---

## §5 — ⭐⭐⭐ Code moves forward in time, never backward

The per-item alignment guard is the corpus's own borrowed pattern from v256, so its travel across the three repositories is measurable.

**Invented in v256:** commit `67af566`, **2026-05-15 23:38** (subject: `New`), introducing the string `"OpenAI-compatible response item index mismatch at position {expected_index}."` — a check that the model returned the same number of items *and* that each item's index matches its position.

**Carried into v258:** `vocra_core/translator/openai_compatible.py:173` checks `len(items) != len(originals)` and `:181` raises **`"Translator item index mismatch at position {expected_index}."`** — the same guard, near-identical message, in a repository created **2026-05-26**, eleven days later. It appears in two further independent paths: `run_translator.py:77` and `vocra_translator/core/translation_service.py:135`, plus count checks in the video pipeline itself (`frame_extractor.py:209`, `segmenter.py:375`).

**Never reached v257:** `grep -rn --include=*.py -E 'index mismatch|len\(...\) != len\(...\)'` across **all 47** of v257's Python files returns **nothing** (exit 1). And v257 was committed to **five times on 2026-05-22 and once on 2026-05-27 17:13** — every one of them after 2026-05-15.

⭐⭐⭐ **He touched the novel tool six times after inventing the guard, including on the last recorded day of all three repositories, and never backported it.**

⚠️ **The steelman, and it partly holds.** v257's architecture is render-and-paste: the human carries the prompt to a chat model and pastes the reply back, so there is no in-process request object to compare a response against, and its validation button is honestly labelled *check syntax*. **A literal port of this guard is genuinely harder there.** But it is not impossible — v257 renders a numbered batch of segments and imports a JSON reply, so the count of returned items *is* checkable against the count sent, and v257 does not check it. **The barrier is not architecture alone; it is that nothing in a copy-forward workflow ever runs in reverse.**

⇒ **The generalisation: in a solo multi-project toolchain, an improvement invented in project N reaches project N+1 by copy-forward and never reaches project N−1, because nothing carries it back — no shared library, no package, no dependency, no CI.** The oldest repository keeps the oldest mistakes permanently, *even while being actively edited*. Copy-forward is a one-way ratchet, and the argument for extracting a shared library is exactly this: it is the only mechanism that makes a fix travel backwards.

---

## §6 — ⭐⭐ The carried-over subsystem got smaller and gained an abstraction — and its bug rode along unchanged

The OCR/inference layer is the clearest case of the same code in two generations.

| | v256 `mmt_core/` | v258 `vocra_core/final_ocr/` |
|---|---|---|
| files | 5 (ad-hoc clients) | 8 |
| lines | **1,342** | **971** |
| shared base | none — each provider a standalone dataclass | ✅ **`base.py`, 19 lines**: a `FinalOCRProvider` Protocol (`provider_key`, `validate`, `recognize_image`, `close`, `metadata`) |
| dispatch | scattered | ✅ **`provider_factory.py`, 17 lines**: one function, dispatch on a provider string, **`raise ValueError` on unknown** |

⭐ **Same subsystem, third project, 28% fewer lines and an actual interface.** That is direct evidence for §4's correlation: the surface he kept re-using improved.

🔴 **And the defect came with it, verbatim.** v256 `mmt_core/llama_server.py:221` and v258 `vocra_core/final_ocr/llama_server_manager.py:131` are the same two functions, structurally line-for-line — an `os.name == "nt"` branch calling `os.startfile`, and an `else` branch calling **`subprocess.Popen(["sh", str(bat_path)])`: the POSIX shell invoked on a Windows `.bat` file.** Both also use `xdg-open` for the folder case. The refactor improved one thing (v258 generates the `.bat` before launching it, where v256 raised `FileNotFoundError` if absent) and preserved the nonsense untouched.

⇒ ⭐⭐ **Structure improves on a carried-forward surface; bugs ride along.** Refactoring moves the shape and copies the content, and a defect that lives inside a function body is content.

---

## §7 — What is genuinely good, and it is the best of the three siblings on several axes

- ✅ **Zero `shell=True`, zero `os.system`** across all 75 files (verified with grep run alone, exit 1 — not through a pipe). **Eight `subprocess` sites, all argv-list form.** v257 had two `shell=True`, one reachable from a text field.
- ✅ **Zero hardcoded HTTP(S) URLs in any `.py` file.** Every endpoint comes from `vocra_core/default_config.json`, whose translator `base_url` and `api_key` default to empty strings. Neither sibling managed this.
- ✅ **Secrets handled deliberately:** `app_config.py:11` puts them in a separate `secrets.json`; `:37–39` allow a `VOCRA_TRANSLATOR_API_KEY` environment override; **`:52` pops `api_key` out of the settings payload before saving**, so the key cannot leak into `settings.json`. And `secrets.json` **is not tracked and never was** in any of the 6 commits. ⚠️ Note the tension: that file is now protected by nothing but luck, because the `.gitignore` was deleted (§2).
- ✅ **A real provider abstraction and factory** in both the OCR and translator layers (§6).
- ✅ **The alignment guard** (§5), in three independent code paths.
- ✅ **A documented architectural decision that the code honours** (§3) — the only instance of that across the three repositories.
- ⭐⭐⭐ **AN INVALIDATION MECHANISM THAT ACTUALLY ENFORCES — and this completes a three-point arc the corpus has been circling since v250.** `segmenter.py:_invalidate_downstream_outputs()` does not warn, it acts: it **deletes** the downstream cache files (`ocr_final`, `translation`) with `cache_path.unlink()`, then resets four status flags — `preprocessed_done`, `ocr_final_done`, `translation_done`, `export_done` — to `False` and persists them via `save_progress`. So re-segmenting a video genuinely forces the OCR and translation stages to re-run.

  **Set that against the siblings, because the contrast is exact.** v256 wrote `DOWNSTREAM_STALE_STAGES` into the cached JSON, surfaced it as a GUI warning, and **enforced nothing** — a message to a human. v257 had **no staleness mechanism at all** (grep across the whole tree). **v258 deletes the artifacts.** ⇒ **The repository with the most written-down reasoning is also the only one of the three that enforces its own invalidation** — an independent confirmation of §4's correlation, arrived at from a completely different surface, and found by the fleet rather than by me.
- ✅ **The SSIM threshold is duplicated eight times and all eight agree** at `0.95` — `draft_ocr.py:159,177`, `ssim_filter.py:37,136`, `project_manager.py:61`, `app_config.py:125`, `scene_config.py:71,190`. v257's three copies of a threshold disagreed; these do not. ⚠️ **I first counted six; a fleet agent found the two I missed** (both in the GUI), and the corrected count makes the point stronger. ⚠️ **One of the eight is a real hazard rather than mere duplication:** `scene_config.py:190` is a *reset-to-default* control that hardcodes `0.95` instead of re-reading the config default, so if the declared default ever changed, that button would silently restore the old value.

---

## §8 — Defects, and the licence

🔴 **The README's logo is an unfilled template placeholder.** Its first visual element links to `https://github.com/your-username/vocra` and loads its image from the matching `raw.githubusercontent.com` path. **Both return HTTP 404** (verified with `curl -o /dev/null -w "%{http_code}"`), and `your-username` occurs twice. The very top of the document is a broken image for every visitor.

⚠️ **Two unmeasured headline claims.** The README states that the region cropper eliminates **100%** of surrounding-scene noise and that SSIM filtering removes up to **90%+** of duplicate static frames at threshold `0.95`. The threshold is real and consistently defaulted; **no measurement, counter, benchmark or log of the actual removal rate exists** — searched across all 75 `.py`, both `.md` and the config. ⭐ Better than its siblings' equivalents in one respect: the claim is at least tied to a named, greppable threshold.

⚠️ **`subprocess.Popen(["sh", …])` on a `.bat`** (§6) — dead on both platforms it could plausibly target.

🔴 **THE TIMEOUT IS ON THE WRONG CALL — found by the fleet, verified here, and it is exactly backwards.** `burner.py` has two ways to invoke ffmpeg:

- `_run_capture` (`:582–583`) — a short probe — is `subprocess.run(command, …, timeout=timeout)`, with `timeout` a **required keyword-only parameter**.
- `_run_ffmpeg_stream` (`:534`) — **the long-running video encode** — is `subprocess.Popen(...)` followed by a bare **`process.wait()`** with no timeout at all.

⇒ **The call that finishes in milliseconds is guarded by a mandatory timeout; the call that can run for hours has none, so a stalled ffmpeg hangs the encode indefinitely.** This is not ignorance of the parameter — the author made it *compulsory* in the helper right below. ⭐ **It is the same shape as the ship's other findings: the discipline exists, and it was applied to the surface that did not need it.**

⚠️ **The SSIM filter is greedy-sequential, which bounds the 90% claim.** `ssim_filter.py:78` compares each frame only against `last_unique_image`, and the reference advances only when a frame misses the threshold (`:88–89`). There is no rolling history. So a subtitle that disappears and **reappears** (A → B → A) produces three "unique" frames and the second A is OCRed again. ⭐ **This is the right algorithm for the common case** — a subtitle sits still for dozens of frames, then changes — and it under-deduplicates on repeats. The consequence for the README's figure: the removal rate depends on the length of subtitle *runs*, not on the number of *distinct* subtitles, so "90%+" is a property of the input, not of the filter.

⚠️ **A cascade risk worth recording:** `draft_ocr.py:61–76` has duplicate frames inherit their leader's recognised text via `frame_map`, with no check that the leader was OCRed successfully. If a leader returns empty, every frame that deduplicated onto it inherits the empty result and the subtitle is lost silently for that whole run.

⚠️ **REJECTED from the fleet, with the reason.** An agent reported `exporter.py:152` (`centis = int(round(millis / 10.0))`, clamped to 99) as a precision defect. **It is not a defect: ASS timestamps are `H:MM:SS.cc` — centiseconds are the format's resolution**, so rounding is required and the clamp is a correctness guard, not data loss. Recorded because it is exactly the kind of "defect" that looks real until you check the specification.

⚠️ **The licence: MIT claimed in prose, with no licence file.** `README.md:169` states in Vietnamese that the project is distributed under the MIT License. There is **no licence file among the 93 tracked files and none added in any of the 6 commits**. This is the third distinct posture across three repositories — AGPL file (v256), nothing at all (v257), **MIT asserted in prose** (v258) — and for the operator it is the *most* permissive of the three: unlike v257, an express grant is at least stated, even if the conventional artifact is missing.

⚠️ **Ten committed `.pyc`**, in `cpython-311` **and** `cpython-312` pairs — the same "two Python versions, both committed" fossil v257 had (there in 312/313).

🔴 **UNDECLARED CONFIG — the inventory rule firing in the reverse direction, found by the fleet.** `vocra_core/default_config.json` declares exactly five top-level sections: `ssim_filter`, `segmenter`, `final_ocr`, `translator`, `burn_video`. **`draft_ocr` is not among them** — and code reads it in five places: `app_config.py:77` (`global_config.get("draft_ocr", {})`), `app_config.py:85` (`merged["draft_ocr"].update(...)`), `draft_ocr.py:49` (`progress["draft_ocr"]`, an unguarded subscript), and `scene_config.py:62,119` (the GUI reading and writing `config["draft_ocr"]["language"]`).

⇒ **The draft-OCR configuration section exists only as a runtime construction and is never declared in the defaults file.** This is the **v240 inventory rule**, but the *other* way round from its usual form: not dead config (declared, unread) but **undeclared config (read, never declared)** — so a reader auditing `default_config.json` to learn what is configurable would not discover that an entire pipeline stage has settings. ⭐ Worth recording because the vault's own bidirectional-check discipline (v250 Rung 1b, v255's script) exists precisely to catch this direction, and it took an agent explicitly asked to check both ways to find it.

---

## §9 — Method, error ledger, sandbox

**Method.** Orchestrator-first: two clones and `diff -rq` both ways; `git rev-list`/`--max-parents=0`/`shortlog` for every count (D39); `git show --name-status` for the purge commit; `git log --diff-filter=A|D` for every added/deleted claim; `git cat-file --batch-check` over `rev-list --objects --all` to find the deleted blobs, **which is what exposed §2 and §3**; `curl` for the 404s; `strings`-free reading of the docs from the pack. Then a 14-agent fleet for the surfaces I had not read.

**My own errors — four, all caught before publication, and two changed the ship:**

1. 🔴 **I nearly published habit 4 as "does not replicate."** My tree-level import trace found zero dead modules — and I *did* sanity-test the detector against a planted name before trusting it, which is the right discipline. What I had not done was look in the **pack**. The blob listing exposed a deleted 93KB GUI, a deleted `app/` service layer, a deleted `cli/`, and 252KB of deleted documentation. **A clean tree is not a clean history.**
2. 🔴 **I attributed `plan.md` to the wrong repository** (v257 rather than v258) — and I had written that attribution into the fleet's ground-truth block before catching it, which is the **v257 amplifier hazard** repeating. Corrected by `git ls-files '*.md'` in all three clones, and the correction *improved* the ship: v257 turns out to have had **no** planning document ever, which is what makes §4's correlation measurable.
3. 🔴 **A `|| echo NONE` attached to `head` rather than `grep`.** My first security pass ran `grep … | head -5 || echo "ZERO"` and printed nothing at all — neither hits nor the fallback — because `head` exits 0 on empty input. **That is v256's D41 exactly**, in my own hands, one ship later. Re-run standalone: grep exit 1, genuinely zero `shell=True`.
4. ⚠️ **A regex false positive I nearly reported as claims.** Grepping the README for `[0-9]+%` returned "20%/6%/20%" — all of which were URL-encoded `%20%7C%20` inside shields.io badge links, not claims. The real claims are the 100% and 90%+ figures in §8.

⭐ **Three of my last four ships have turned on the same discipline**: v256's truncated font search, v257's three misattribution traps (**D45**), and here the tree-versus-pack blind spot. The pattern is consistent enough to name: **I am reliable when I read a file and quote it, and unreliable when I generalise from where I looked.**

**Sandbox.** `python3` and `pip` exist at `/usr/local/bin/` and are **SIGKILLed on invocation** — no Python ran at any point. `timeout` does not exist. `git` is 2.19. Per the v257 lesson, the fleet script was written to a file and launched with `scriptPath` rather than inline (an unescaped backtick in a template literal fails to parse *and* the failed script is not persisted).

**NOT ESTABLISHED:**

- **What tool produced `docs/progress.md`.** Its structure is an agent working-memory file's; a grep across it for every common assistant name returns nothing. **The shape is evidence; the provenance is not stated.**
- **Whether the 90%+ frame-reduction claim is true.** It is unmeasured in the repository; nothing here says it is false.
- **Any corpus-first claim.** None is made. Prior art in burned-in-subtitle extraction (VideoSubFinder and others) long predates this, and the author's locale is context only (§41).
- **Whether `PaddleOCR-VL` runs as a GGUF under `llama-server` as the project assumes.** Referred to the fleet; not asserted here.

---

## §10 — Verdict summary

**GOAL-ALIGNED INCLUDE 3/4** — (a) **FAIL** (§41) · (b) **MODERATE** ⚠️ *OFF-GOAL recorded as the reviewable alternative* · (c) **STRONG** · (d) **STRONG**. §40 applies: operator-requested, goal-adjacent, no override, no §35 pressure.

**(b) is MODERATE, not STRONG, and the reasoning is worth stating** because it moves *down* from v257. v257 rated STRONG because the LLM was the entire subject — thirteen prompt templates, a render engine, a response parser, a step registry. **VOCra is a computer-vision pipeline with an LLM stage bolted to the end**: frame extraction, cropping, SSIM deduplication, OCR, segmentation and timestamping are the bulk of the 9,641 lines, and the translation layer is ~490 of them. That is v256's shape, and v256 was MODERATE. What is genuinely on-goal: the provider-abstraction/factory pattern, the alignment guard (already banked at v256), and — the real contribution — **the N=3 control method itself.**

**NO MINT.** Counts **46/11 UNCHANGED**; §C live standalones **51** unchanged; surface **≈58** unchanged. Grounds in the Verdict.

**The one sentence:** ⭐ *He wrote two hundred and sixty-two kilobytes of reasoning in two and a half days, deleted ninety-nine percent of it, and the surviving seventy-five lines are the only place in three repositories where a stated decision is actually honoured by the code.*
