# (C) Deep Dive — `mranex/my_manga_translator` (wiki v256)

**Ship:** v256 · **Date:** 2026-08-20 · **Verdict:** GOAL-ALIGNED INCLUDE 3/4 · **NO MINT** · counts 46/11 UNCHANGED
**Subject:** `https://github.com/mranex/my_manga_translator` — *"Manga Translator Studio"*, a PyQt6 desktop workbench for translating manga/comics, README entirely in Vietnamese.
**Author:** `mranex` — a pseudonymous individual. Not Anthropic, not a registered vendor-direct source (§41 ⇒ **(a) FAILS**).

---

## §0 — Source verification (D27: the ref population is declared)

Two independent `git clone`s into separate directories, then `diff -rq --exclude=.git` **in both directions**: **identical both ways**.

| Fact | Value | Command |
|---|---|---|
| HEAD | `f2318d384692192fc20e29425b8801c8bd5032e5` | `git rev-parse HEAD` |
| Commits on HEAD | **62** | `git rev-list --count HEAD` |
| Commits all refs | **62** | `git rev-list --count --all` |
| Root commits | **1** (`a5dc742`, 2026-05-13 00:21:54 +0700) | `git rev-list --max-parents=0 --all` |
| Merge commits | **1** | `git rev-list --count --merges --all` |
| Tags | **0** | `git tag` |
| Refs | `main`, `origin/master` | `git branch -a` |
| Tracked files | **186** | `git ls-files \| wc -l` |
| Python | **152 files / 54,977 lines** | `git ls-files '*.py' \| xargs wc -l` |
| Other | 24 `.ttf`, 3 `.md`, 2 `.qss`, 2 `.bat`, 1 `requirements.txt`, 1 `LICENSE` | — |
| First commit | **2026-05-13** | `git log --reverse` |
| Last commit (anywhere) | **2026-05-27 11:39:51 +0700** | `git log --all -1` |
| Authors | `mranex` only, two identities: `elsgman1999@gmail.com` **59**, GitHub noreply **3** | `git shortlog -sne --all` |
| Page-stated | **32 stars / 12 forks / 0 watching** | rendered repo page |

**Page-stated figures only** — this environment mocks the GitHub API (§37.4) ⇒ **not a Pattern #52 claim.** 32 stars is nowhere near viral in any case.

⭐ **The build window is 14 days.** 54,977 lines of Python, 186 files, first commit to last: **2026-05-13 → 2026-05-27**. That is ~3,900 lines/day sustained by one person. There is **no `Co-Authored-By`, no Claude/Codex/Copilot trailer, and no AI-provenance metadata anywhere in the 62 commit messages** — the single AI-related string in the entire log is the commit subject **`Ditme GPT`** (Vietnamese profanity), and §M shows what it produced.

---

## §1 — What it is

A ten-stage, human-in-the-loop desktop pipeline: **Detection → OCR Prepare → OCR → Translation Init → Translation → Mask Prepare → Inpaint → Render Prepare → Render → Export.** Every stage writes its intermediate result to a per-stage JSON cache under the project's `cache/` directory, and every stage's output is editable in the GUI before the next stage consumes it.

The README's framing is explicit and it is the reason this subject is worth a wiki. Its `> [!WARNING]` block opens: **"ĐÂY KHÔNG PHẢI LÀ MỘT CÔNG CỤ ĂN SẴN KHÔNG NÃO"** — *"this is not a brainless ready-made tool"* — and the design philosophy section attacks *"one-button automatic translation tools"* for deforming art and mangling bubbles. The product thesis is that the human is not a fallback for a missing gate; **the human is the gate, and the software's job is to make each stage's state legible enough to correct.**

That thesis is the goal thread, and §3–§5 are where it either holds up or does not.

---

## §2 — ⭐⭐⭐ THE HEADLINE: the second commit imported a different program, and the dependency list still describes it

`git show --shortstat bdcb098` — commit #2, timestamped **00:27:46**, five minutes and fifty-two seconds after `Initial commit`:

> **68 files changed, 8,675 insertions(+), 1 deletion(-)**

The files it added are not a manga-translation library. They are a **Flask web application**:

```
app.py                     .dockerignore              run.bat
templates/index.html       templates/translate.html
static/css/style.css       static/js/app.js
static/img/{back.jpg, header.png, loading.gif, logo.png}
examples/{0,1,2,3,ex0,ex1,ex2,ex3}.png       model/model.pt
model/model_training.ipynb  test_translator_batch.py   .jules/bolt.md
```

…plus all 24 fonts, `detect_bubbles.py`, `add_text.py`, `process_bubble.py`, `font_analyzer.py`, `ocr/`, `translator/translator.py`, `translator/test_translator.py`, `.gitignore` and `requirements.txt`.

The repository is **not a GitHub fork** (the rendered page shows no "forked from"; the author's only fork is an unrelated TypeScript repo). So an entire upstream project was copied in wholesale, without a fork relationship and **without any attribution file** — then reshaped over 14 days into a PyQt6 desktop app.

The web app was deleted in one commit: **`a41abd7 "Clean new"`, 2026-05-18** — `app.py`, `templates/`, `static/`, `.dockerignore`, `run.bat` and `.jules/` all removed together.

⭐⭐⭐ **And `requirements.txt` was not touched by that commit.** Its complete history is six commits, **all between 2026-05-13 and 2026-05-14** — four days *before* the purge:

```
5aa9c9c 2026-05-14 Update PyQt6 GUI      ← last edit, ever
617d044 2026-05-13 Fix detector v1
3ca667a 2026-05-13 Fix OCR Part 1
5f733d0 2026-05-13 Clean repo + Delete old OCR
dff54a1 2026-05-13 Upgrade PaddleOCR-VL
bdcb098 2026-05-13 New                    ← the import
```

So at HEAD, a desktop GUI application's documented install still pulls a web server stack:

| Requirement | Direct imports across all 152 `.py` files |
|---|---|
| `Flask==2.2.5` | **0** |
| `flask-socketio==5.3.6` | **0** |
| `python-socketio==5.10.0` | **0** |
| `python-engineio==4.8.1` | **0** |
| `Werkzeug==3.0.1` | **0** |
| `gunicorn==21.2.0` | **0** |
| `tqdm==4.66.2` | **0** |
| `cryptography==42.0.4` | **0** |
| `sentencepiece==0.2.0` | **0** |
| `huggingface-hub==0.22.2` | **0** |

Verified by `grep -rlE "^\s*(import|from)\s+<mod>" --include=*.py .` per package. Ten of twenty-four pinned requirements have no direct importer. (`huggingface-hub` and `sentencepiece` are legitimate transitive dependencies of `transformers`; the other eight are fossils.) `gunicorn`'s own PyPI classifiers list only **`Operating System :: MacOS :: MacOS X`** and **`POSIX`** — a UNIX-only WSGI server pinned into a project whose only launcher is a Windows `.bat`.

**The rule:** ⭐⭐ **deleting a program is not deleting its dependencies, and a dependency list is the last place anybody looks for dead code.** The purge commit removed 100% of the web application's source and 0% of its install cost. Nothing in the repository — no CI, no linter, no import check — could have noticed, because there is no CI at all (§8).

---

## §3 — ⭐⭐⭐ The agent's memory was deleted; the fix it prescribed is still running

Among the 68 imported files was **`.jules/bolt.md`** — a directory convention belonging to **Jules**, Google's asynchronous coding agent. The file is three lines. It is a dated agent learning journal, and it has exactly one entry:

> `## 2024-05-23 - Heavy Model Re-initialization`
> **Learning:** in Flask apps, heavy ML models should never be initialized inside request handlers or per-request `__init__` methods, because the model is re-loaded from disk for every user request.
> **Action:** always use class-level caching or global singleton patterns. Use **`_model_cache`** class attributes or a global registry.

That file was deleted on **2026-05-18** by `a41abd7 "Clean new"`. The remedy it prescribes is still in the tree at HEAD, **named exactly as the agent named it**:

```python
# translator/translator.py:38
        # self._nllb_model and self._nllb_tokenizer are now cached in _model_cache
...
# translator/translator.py:43
    # Class-level cache for heavy models (shared across instances)
    _model_cache = {
        "nllb_model": None,
        "nllb_tokenizer": None,
        "hf_pipeline": None
    }
    _nllb_lock = threading.Lock()
```

…and the *other* half of the same sentence — "or a global registry" — is at `detect_bubbles.py:6`, `_yolo_model_cache = {}`, with a `clear_model_cache()` at `:390`.

⭐⭐⭐ **Two comments survive that refer to a decision whose reasoning has been deleted from the working tree.** `translator/translator.py:38` is a *migration note* — "are **now** cached in `_model_cache`" — pointing at a refactor whose rationale exists only inside the git pack. The next maintainer who tidies `_model_cache` into a normal instance attribute reintroduces the exact latency and memory blow-up the agent recorded, and the only document that explained why is gone.

**This is v255's D40 arriving from the opposite direction.** At v255 a *stale* label was safe **because it was declared**. Here a *correct* mechanism is fragile **because its declaration was thrown away**. The compensation outlived the rationale. It is also the precise inverse of the vault's own **D22** (*agent-facing prose goes stale first*): here the agent-facing prose did not go stale — it was **deleted while still accurate**, which is worse, because staleness is detectable and absence is not.

---

## §4 — ⭐⭐⭐ The best thing in the repository: a staleness mark that is declared, persisted, displayed — and deliberately not enforced

The README's central claim is that editing one stage does not cost you the others: *if inpaint fails or you want a different render font, you do not re-run OCR and Translation — the system reuses the cache. Saves 100% of API token cost.*

Tested against the code, the claim holds, and the mechanism is better than the prose. Three hand-written constants declare the blast radius of each kind of manual edit:

```python
mmt_core/detection_edit.py:29   DOWNSTREAM_STALE_STAGES = ["ocr", "translation", "inpaint", "render", "export"]
mmt_core/ocr_edit.py:23         DOWNSTREAM_STALE_STAGES = ["translation", "inpaint", "render", "export"]
mmt_core/render_edit.py:29      DOWNSTREAM_STALE_STAGES = ["render", "export"]
```

When the user hand-edits a detection box, `detection_edit.py:107` and `:154` write **`payload["downstream_stale"] = list(DOWNSTREAM_STALE_STAGES)`** into the stage's cached JSON. The mark is therefore **persisted in the artifact**, in machine-readable form, naming the stages by name — it survives process exit, and it is **not inferred from `mtime`** (the v244 **D29** trap, avoided). *(Phrasing corrected after review: an earlier draft said "not held in memory," which conflates the constant with the mark. The three `DOWNSTREAM_STALE_STAGES` lists are of course module-level and in memory from import; the point is that the **mark** is written down, in the file it invalidates, rather than recomputed or held only for the session.)* `detection_io.py:129`, `ocr_io.py:86`, `render_io.py:72` all round-trip it defensively (`if isinstance(..., list)`), and `render_stage.py:133–158` **preserves** an existing mark when it rewrites the payload rather than clearing it.

The GUI reads it: `main_window.py` has `_mark_detection_downstream_stale`, `_mark_ocr_downstream_stale`, `_mark_render_downstream_stale` and `_update_detection_stale_warning`, and `stages/detection_panel.py:251–253` renders the stale stage list into a warning string for the user.

**Then it stops.** Grep across all 152 files: **36 mentions, 5 write sites, and zero enforcement.** No `*_stage.py` runner reads `downstream_stale` to gate execution; there is no `raise`, no refusal, no abort, no `if` that branches on it into a failure path. The pipeline records that five downstream stages are now wrong, shows you, and lets you run anything you like.

⭐⭐⭐ **And the README says exactly that, in its troubleshooting section, as the answer to "cache data is out of sync":** the cause is *"you edited an earlier stage manually but have not re-run the later ones"*; the fix is *"remember to re-run the following steps (OCR → Translation → Render)"*.

This is the synthesis of the last six ships, and it is the first subject in the sequence that gets it **right**:

- **v250** called six connector rules *"non-negotiable"* and gated one.
- **v252** headed a rule block *"Hard Limits (Automated, Zero Tolerance)"* and automated none.
- **v247** committed a CI gate its own merge history violates 66 times out of 82.
- **v254** built a weekly job and aimed it at the one decidable thing nobody doubted.
- **v256 has an unenforced check, and claims nothing else.** The label matches the mechanism. The stale mark is a *message to a human who is already in the loop by design*, and the document that describes it describes it accurately.

⭐ **The rule: an unenforced check is a defect only when something claims it is enforced.** A declared, persisted, human-addressed staleness mark in a tool whose stated philosophy is human-in-the-loop is not a missing gate — it is a correctly-scoped one. The failure mode the last five ships kept finding was never "no automation"; it was **automation claimed and not delivered**.

⚠️ **The real defect here is a different one, and it is the v240 inventory rule:** the stage DAG is declared **four or more times** — in the stage modules themselves, in these three literal lists, and in the GUI's panel ordering — and **nothing reconciles them.** Insert a stage and three hand-maintained lists must be edited by hand. The three lists do not even share a convention: `detection_edit` and `ocr_edit` are strictly downstream (neither names its own stage) while `render_edit` includes `"render"` itself. That is defensible on the merits — editing render config must re-render — but it means the reader cannot tell a convention from a typo, which is exactly the drift surface v240 named.

---

## §5 — ⭐⭐⭐ The operator payoff: the segment-alignment problem, defended at five layers

This is the most transferable thing in the repository, and it maps 1:1 onto **hireui**.

The problem: you send N text regions to an LLM in one request and get back a list. If the list is shifted by one, or merged two items, or dropped an empty one, then every subsequent item is attributed to the wrong region — and **nothing crashes.** In manga you get a character speaking someone else's line. In a CV parser you get one candidate's employer attached to another's degree. It is the single most dangerous failure mode in LLM-based structured extraction, because it is silent and plausible.

Every translation backend in this repository defends it, and the defence is layered:

**1 — the contract is stated in the prompt as machine-checkable rules.** `mmt_core/prompt_studio.py:31–36`:

> `- Preserve every page key exactly as provided.`
> `- Preserve item count exactly.`
> `- Preserve item order exactly.`
> `- Do not merge, split, drop, or invent items.`
> `- Do not add explanations, notes, markdown, or commentary outside the structured result.`

**2 — the expected count is interpolated into the request.** `translator/gemini_translator.py:373`: *the `"translations"` array must have exactly `{len(texts_to_translate)}` items*; `:276–277` *keep exactly the same page names / exactly the same number of bubbles per page.*

**3 — the response length is checked, in every backend.** `deepseek_translator.py:238` and `:516`, `gemini_translator.py:396` and `:640`, `local_llm_translator.py:186`, `openai_compatible_translator.py:344` and `:384`, `batch_orchestrator.py:65`, `context_memory.py:91` — all `if len(translated) != len(original)`.

**4 — the per-item *index* is checked, not merely the count.** `openai_compatible_translator.py:355` raises *"response item index mismatch at position {expected_index}"*, and `:396` does the same per page. A count check passes a swap; an index check does not.

**5 — the fallback preserves alignment instead of preserving translation.** `deepseek_translator.py:450`: *"If response length mismatches, pad/truncate with originals."* ⭐ **Untranslated-but-correctly-placed beats translated-but-shifted.** That is the right call and it is the one most implementations get wrong.

⭐ **Why layer 3 is load-bearing, in the code's own shape:** the reconciliation is done with `zip(indexed_texts, translations)` (`deepseek:476`, `gemini:201`, `local_llm:195`, `context_memory:94`). **Python's `zip` silently truncates to the shorter sequence.** The length check at `context_memory.py:91` sits three lines above the `zip` at `:94` for exactly that reason. Remove the guard and the misalignment becomes invisible — which is what an unguarded implementation looks like.

**Take this whole ladder into hireui.** It is the concrete, borrowable answer to the eval-gating clause of the ratified candidate-LLM legibility ADR, and it costs nothing to adopt: an index-carrying request format, the count asserted inside the prompt, a length check, a per-item index check, and a fail-safe that reverts to source text rather than mis-attributing it.

---

## §6 — ⭐⭐ The flagship feature in the README is unreachable by construction

The README's OCR section leads with **`Online LLM (Claude, GPT, Gemini)`** — *send the cropped image straight to a vision-capable large language model's API* — and recommends it in the most memorable line in the document: **"Giàu thì cứ Claude mà vã"** *(roughly: "if you're rich, just go hard on Claude")*.

The authoritative provider registry, `mmt_core/ocr_models.py:18–22`, has **three** entries:

```python
OCR_PROVIDER_CHOICES = (
    (OCR_PROVIDER_PADDLE_VL_LLAMA, "PaddleOCR-VL Local"),
    (OCR_PROVIDER_DEEPSEEK_OCR_LLAMA, "DeepSeek OCR (llama.cpp)"),
    (OCR_PROVIDER_CHROME_LENS, "Chrome Lens"),
)
```

`OCR_PROVIDER_LABELS` (`:34–38`) has the same three. There is no vision-LLM provider. `grep -rniE 'anthropic|claude' --include=*.py .` across all 54,977 lines returns **six hits, all in one file**: a hardcoded model-name list at `translator/local_llm_translator.py:46–50` (`claude-sonnet-4.5`, `claude-sonnet-4`, `claude-opus-4.5`, `claude-haiku-4.5`) — the **translator**, not OCR. (⚠️ And that list is internally inconsistent with its own docstring at `:64`, which gives the example `claude-3.5-sonnet` — a different naming generation.)

The nuance that could have rescued the claim, and does not: the two llama.cpp OCR clients (`deepseek_ocr_client.py:116–117`, `paddleocr_vl_client.py:140–141`) post an **OpenAI-shaped `chat/completions` payload with an `image_url` data URI** to a configurable `server_url`. So the wire format is already right for a cloud vision endpoint. But `OCRConfig` (`ocr_models.py`) has **no `api_key` field at all** — its fields are `server_url`, `host`, `port`, `llama_cpp_dir`, `model_path`, `mmproj_path`, `gpu_layers`, `ctx_size`, `temperature`, `extra_args` and five `chrome_lens_*` settings. There is nowhere to put a credential, and no code path sets an `Authorization` header.

⭐⭐ **So the README's headline OCR option is not merely unimplemented — it is unreachable by construction, and the thing that makes it unreachable is a missing field in a dataclass.** This is a **MISMATCH, not displacement**: nothing in the world changed. The feature was described and never built, and the description is the part users read.

---

## §7 — ⭐⭐ AGPL-3.0 asserted over Monotype's Arial and a MyFonts webfont kit

`fonts/` is **9.2MB of the repository** — larger than all 54,977 lines of Python — and it is the one part of the tree the author did not write. The `LICENSE` file (AGPL-3.0) was added by the **final commit of the project**, `f2318d3 "Create LICENSE"`, 2026-05-27, fourteen days after the first.

I extracted the embedded name tables from all 24 `.ttf` files (`strings -a` plus `strings -a -e b` for UTF-16BE records). Reporting only what the binaries themselves say:

| File | Embedded strings found |
|---|---|
| `ariali.ttf` (717KB) | *"Arial Italic"*, *"Arial-ItalicMT"*, **"© 2017 The Monotype Corporation. All Rights Reserved."**, *"Arial is a trademark of The Monotype Corporation"*, designers *"Robin Nicholas, Patricia Saunders 1982"*, and a licence clause beginning **"Microsoft supplied font. You may use this font to create, display, and print content as permitted by the license terms or terms of use, of the Microsoft product…"** and ending **"Any other use is prohibited."** |
| `animeace_i.ttf` | **"Copyright (c) 2006 by Nate Piekos. Blambot.com. All rights reserved."**, *"Anime Ace 2.0 BB is a trademark of Nate Piekos. Blambot.com."*, licence URL `blambot.com/license.shtml` — **plus a modified name record containing a Vietnamese fragment and a `blogspot.com` URL** ⇒ a fan-*Việt-hóa* derivative, i.e. a modified commercial font |
| `mangati.ttf` | **"(C)2001 Nate Piekos. www.piekosarts.com/blambotfonts"** (Blambot again) |
| `Yuki-CCMarianChurchlandJournal.ttf` | **`com.myfonts.easy.comicraft.marian-churchland-journal.regular.wfkit2.version.3oJp`** — a **MyFonts `wfkit2` webfont-kit order slug** for a **Comicraft** font |
| `Yuki-Gingerline DEMO Regular.ttf` | family name is literally **"Yuki-Gingerline DEMO"** — *DEMO* is baked into the font's internal family name |
| `Yuki-Nagurigaki Crayon.ttf` (5.5MB) | *"(C) 2015 Do-Font"* |

And the negatives, which matter as much:

- `grep -aiE 'SIL Open Font|OFL|Apache Licen|GNU General|free for (personal\|commercial)'` across **all 24 fonts** → **zero hits.** Not one font in the pack carries an open-font licence string.
- **No font licence, credits or attribution file has ever existed** in the repository's history (`git log --all --diff-filter=A --name-only | grep -iE 'font.*(licen|credit|attrib)|OFL|SIL'` → nothing).
- The README mentions fonts **seven times** and their licensing **zero times**.

⭐ **21 of 24 files carry a `Yuki-` prefix** — the signature of a bulk-renamed community font pack — and the Vietnamese fragment inside `animeace_i.ttf` identifies the practice: fonts *"Việt hóa"* (Vietnamized, i.e. re-drawn to carry Vietnamese diacritics), which is a well-established scanlation-community activity and, mechanically, the production of derivative works.

⭐⭐ **And the licence was applied from a browser.** Three of the 62 commits use the GitHub `users.noreply` identity, and they are precisely the three actions GitHub performs on your behalf through the web UI, each carrying GitHub's own default message: `Initial commit`, `Merge pull request #1`, and **`Create LICENSE`** — the licence-picker dropdown. The other 59 commits are from the author's machine. **The two identities partition perfectly into "browser" and "editor," and the licence is on the browser side.**

⭐ **And for its entire development the project had no licence at all.** `LICENSE` arrives with commit 62 of 62, on the last day — so the 14 days during which all 54,977 lines were written, and the 61 commits that wrote them, were published with **no grant of any kind** (the GitHub default: all rights reserved). Anyone who cloned it in that window — and the fork count is 12 — took a copy they had no licence to use. The AGPL was then applied, from a dropdown, retroactively in effect and to a tree that already contained Monotype's Arial.

**This is the fourth instance of the vault's licence-vs-artifact class** (v244 de-branding CI, v245 an AGPL wheel under Apache metadata, v246 an Apache-2.0 repo executing a revenue-capped engine) — and **the first where the mismatched artifact is not code at all.** No legal conclusion is asserted here and none is needed for the operator's purposes: the practical effect is in the Pilot Menu's fences.

---

## §8 — The tests, the CI, and the one test the project's own rules would have excluded

- **Zero CI, ever.** `git log --all --diff-filter=A --name-only | grep -Ei '\.github|\.gitlab|\.yml|\.yaml'` returns only two false positives on filenames (`workflow_sidebar.py`, `workflow_tabs.py`). **No `.yml` or `.yaml` file has ever existed in this repository.**
- **Zero agent surface.** `git ls-files | grep -Ei 'claude|AGENTS\.md|\.cursor|copilot|llms\.txt|SKILL|CONTRIBUTING|\.github'` → **nothing.** A clean **#12 negative** — and a sharper one than v255's, because §3 shows the agent surface was *inherited and deleted*, not merely absent.
- **Exactly one test file**, `translator/test_translator.py`, 23 lines. It is a real pytest module: a `translator()` fixture, `@pytest.mark.parametrize("method", ["google", "hf", "baidu", "bing"])`, and the assertion `translated_text.lower() == EN_TRANSLATION` for `JA_TEXT = "こんばんわ!"` → `"good evening!"`.

⭐⭐⭐ **Three separate things make that test incapable of providing signal:**

1. **It asserts exact string equality against four live third-party network translation services.** Google, HuggingFace, Baidu and Bing must all return the byte-string `"good evening!"`. (The input is also itself a misspelling — こんばんわ for こんばんは.)
2. **`pytest` is not in `requirements.txt`.** Following the README's documented install produces an environment that cannot run it.
3. ⭐⭐⭐ **The project's own `.gitignore` excludes it.** Line 49 is `test_*.py`, under a comment reading `# Local`. `git check-ignore -v --no-index translator/test_translator.py` → **`.gitignore:49:test_*.py`**. The file survives only because it was tracked by the same commit that added the `.gitignore` (`bdcb098`), and git ignores only *untracked* paths.

**That ignore rule is the project's actual testing policy, written down:** tests are local scratch, not repository content. It is not an oversight — it is a declaration. And the single test in the tree is the exception the rule cannot evict.

**Set against v255:** v255 had fourteen test files that ran green and asserted nothing. v256 has one test that asserts something real, cannot pass, is not installable, and is excluded by policy. **Both deliver exactly zero signal — reached from opposite ends.** The v255 lesson was *a green suite is not evidence*; this one adds *a test that nobody can run is not a test, and a `.gitignore` can encode a testing policy more honestly than a README can.*

---

## §9 — Supply chain: a requirements file that is unsatisfiable as written

`requirements.txt` is 24 lines, pinned `==` on 20 of them. Release dates from PyPI:

| Pin | Uploaded |
|---|---|
| `torch==2.0.1` | **2023-05-08** |
| `huggingface-hub==0.22.2` | **2024-03-29** |
| `transformers==4.57.3` | **2025-11-25** |

⭐ **A 2.5-year span in one file** — the fossil half (2023-era `torch`, `numpy==1.24.2`, `Flask 2.2.5`, `gunicorn`) inherited from the imported web app, with the desktop app's needs bolted on top (`transformers==4.57.3`, `chrome-lens-py>=3.0.0`, `google-genai`, `PyQt6==6.7.1`).

**The two halves are mutually unsatisfiable.** From PyPI's own published `requires_dist` for `transformers==4.57.3`:

- `"huggingface-hub<1.0,>=0.34.0"` — the file pins **`huggingface-hub==0.22.2`**
- `"safetensors>=0.4.3"` — the file pins **`safetensors==0.4.2`**

⇒ **`pip install -r requirements.txt`, the exact command the README documents, has two hard contradictions.** And it was born that way: `transformers==4.57.3` was published 2025-11-25, so the conflict existed on the day the pin was written in May 2026. This is a **DEFECT, not displacement** — nothing moved underneath it.

⚠️ **Method limit, stated plainly:** this rests on PyPI's published dependency metadata, which is what pip resolves against. **I did not execute pip.** `python3` exists on this machine at `/usr/local/bin/python3` but is **SIGKILLed** on invocation in this sandbox, so no Python ran at any point in this analysis. See §12.

**Known advisories against the pinned versions** (ids from PyPI's OSV-backed `vulnerabilities` array):

- `transformers==4.57.3` — **7 records**, including `PYSEC-2026-2288/2289/2290`, `GHSA-fgcw-684q-jj6r`, and `CVE-2026-4372` **fixed in 5.3.0**: a remote-code-execution path where a malicious `config.json` names an attacker-controlled Hub repo via `_attn_implementation_internal`. This app loads Hugging Face models.
- `torch==2.0.1` — **10 GHSA records.**
- `pillow==10.3.0` — 5+ records. `Flask==2.2.5` — 2 records.

⭐ **The single most-advisory-laden component of the install (`Flask` / `Werkzeug` / `gunicorn`) is imported by zero files.** You would be installing vulnerable code that cannot even run.

No lockfile, no hashes, no `--require-hashes`, no transitive pinning.

---

## §10 — ⭐⭐⭐ `Ditme GPT`: the most disciplined file in the repository, committed under an obscenity aimed at the model

`2f8a363`, 2026-05-17 01:56, subject **`Ditme GPT`**. Diffstat: `canon_overlap.py` +55/−21, `deepseek_ocr_client.py` +8, and a new file **`mmt_core/ocr_text_filter.py`, +121 lines** (263 at HEAD).

The file is a **hallucination filter for OCR output**, and its taxonomy is precise. DeepSeek-OCR is a *document* OCR model, so when pointed at a speech bubble it sometimes returns document structure instead of dialogue. The filter names each failure mode and rejects it with a machine-readable reason:

```python
STRUCTURED_TAG_MARKERS = ("<table", "</table>", "<thead", "<tbody", "<tr", "<td",
                          "<svg", "<path", "<math", "<figure", "<chart")
...
@dataclass(slots=True)
class OCRTextFilterResult:
    text: str
    rejected: bool
    reason: str = ""
```

Reasons emitted: `empty_ocr_output`, `structured_json_non_text`, `structured_markup_non_text`, `coordinate_geometry_non_text`, `structured_hallucination_non_text`. It also recursively unwraps JSON payloads (bounded, `depth > 3`), and detects coordinate geometry by counting numeric-pair matches.

⭐⭐ **And it is scoped honestly:** `if provider_key != DEEPSEEK_PROVIDER_KEY: return OCRTextFilterResult(text=cleaned, rejected=False, reason="")`. **The filter is a no-op for every provider except the one whose failure mode it was written against.** It does not pretend to be a general safety net.

⭐⭐⭐ **This is the v246 `silent` doctrine, independently re-derived and applied.** The naive pipeline would have typeset a plausible HTML table into a speech bubble and shipped it. This converts a confident wrong answer into a **loud, named rejection** carrying its cause. That is exactly what v246's four-line doctrine prescribes — and this author arrived at it by hitting the failure, swearing at the model in a commit message, and then writing down the taxonomy.

⚠️ **v246 `silent` detector on this subject: `grep -rni "silent"` → ZERO** (also zero for the Vietnamese equivalents *âm thầm*, *im lặng*, *lặng lẽ*). **Fourth consecutive null** — and the most instructive of the four, because *the doctrine is unmistakably present in the code and simply not present in that vocabulary.* v253 said the detector's domain is artifacts that run; v254 refuted that; v255 narrowed it to *artifacts whose authors wrote down their reasoning about failure*. **v256 refines it once more: the author here DID write down his reasoning about failure — in five reason-strings and a commit-message obscenity — and the grep still returns zero.** ⇒ **The detector finds a specific English word, not a discipline. Its four nulls are a measurement of vocabulary, not of quality**, and on a Vietnamese-authored codebase it is structurally blind. ⭐ **Portable fix for the vault's own use: grep the reason-strings, not the adjective** — `rejected`, `reason=`, `_non_text`, `mismatch` found this file instantly.

---

## §11 — Everything else that is true and worth recording

**The README-vs-tree inventory** (all verified; `git log --all --diff-filter=A` used for the "never existed" claims):

| README claims | Reality |
|---|---|
| `mmt_core/project.py` | **MISSING** — `project.py` is in `mmt_gui/` |
| `mmt_core/pipeline.py` — *"the orchestrator that sequences the stages"* | **HAS NEVER EXISTED** in any commit on any ref |
| `mmt_gui/workers/` (a package) | a single 70,428-byte module, `mmt_gui/workers.py` |
| `![](Screenshot/Main_UI.png)`, `![](Screenshot/Editor_UI.png)` | **NEITHER HAS EVER EXISTED** ⇒ both images in the "Visual Showcase" section are broken |
| translators: Gemini, OpenAI, DeepSeek, Google, **NLLB, Baidu, Bing** | the latter three exist only inside `translator/translator.py`, the inherited file |

⭐ **And directly beneath the two broken images sits the template instruction that produced them**, a `> [!TIP]` telling the author to take screenshots and save them into `Screenshot/`. **The boilerplate note-to-self was published as documentation.**

⭐⭐ **The GitHub repository description — the single most-read string the project owns — is `"Chưa có thời gian viết hướng dẫn mn ơi T-T"`: *"haven't had time to write a guide, folks."*** Beneath it sits a 312-line, 25,250-byte README with ten diagrams, a Mermaid pipeline graph, a model zoo with VRAM figures, a troubleshooting section and a design-philosophy essay. **The most exposed surface in the project contradicts the most laboured one** — v250's rule (*a gate's aim decides what rots*) with nothing aimed at the description at all.

**Dead code, measured.** `ebac2dc` (2026-05-13, subject `Con di me may` — profanity) deleted the committed `model/model.pt`; `2aebd41` (2026-05-17, `Remove CTD`) removed the comic-text-detector from the pipeline, followed by `ca8869f "Fix inpaint after remove CTD"` — and `detectors/comic_text_detector.py` plus the five-file `detectors/comic_text_backend/` (vendored YOLOv5) remain in the tree. The README's own Developer Notes concede the root scripts are *"reference code or old helper tools"* and tell you not to edit them. ⭐ **The author documents his own dead code — a genuine #83 positive, in the same document that advertises an unbuildable feature (§6).**

**Git-pack cost of the deleted upstream.** `.git` is **22MB** (`size-pack 21.88 MiB`) against a working tree whose largest asset class is 9.2MB of fonts. The largest blobs ever written: `model/model.pt` **6.23MB** (deleted), `fonts/Yuki-Nagurigaki` 5.46MB (live), `static/img/back.jpg` 1.37MB, eight `examples/*.png` at ~1MB each, `static/img/loading.gif` 1.24MB — **every one of those except the font is deleted.** ⭐ **Roughly two-thirds of every clone, forever, is the web application that was removed on 18 May.**

**The 03:06–04:37 spiral.** On 2026-05-16, nine commits in ninety-one minutes with subjects `A`, `B`, `AAAA`, `bbbbb`, `CCCCCCCCAÂ`, `DDDDDDD`, `EEEEEEEEEE`, `fffffffffffff`, `Final fix` — carrying real work throughout (`+651/−243`, then `+746/−130`). ⭐ An unretouched debugging session preserved in the commit log; a squash-merge policy would have deleted the most human artifact in the repository.

**Security — and this is the section where the subject does best.** Verified, not assumed:

- ✅ **No bind-all, no CORS, no auth-bypass.** `grep -rnE '0\.0\.0\.0|allow_origins|CORS'` → **zero hits.** All three OCR clients default to **`http://127.0.0.1:8080`**. **This subject does not have the v231/v232 broken-authentication triad** that v231, v232 and (positively) v244 established as a class.
- ✅ **No plaintext egress and no hardcoded model downloads.** Complete URL census across 152 files: **12× `127.0.0.1`, 4× `localhost`**, and exactly four external hosts, all HTTPS — `api.openai.com/v1`, `api.deepseek.com`, `api.deepseek.com/chat/completions`, `openrouter.ai/api/v1`. Every `http://` in the codebase is loopback. **No model-weight download URL is hardcoded anywhere** (contrast v234, whose installers fetched over plaintext `http://`).
- ✅ **No `shell=True`, no `os.system`.** All seven `subprocess` sites use argv-list form.
- ✅ ⭐ **API keys are handled correctly, and it matters here.** The three key fields live on `TranslationConfig` (`translation_models.py:105–118`); the GUI collects them in `QLineEdit`s with **`setEchoMode(QLineEdit.EchoMode.Password)`** (`translation_panel.py:117, 121, 131`); app settings go to **`QSettings`** — the OS-native store (`app_settings.py:20`); and `project.json` is written from `ProjectData.to_dict()` (`project.py:148–151`), which carries pages and indices, **not** the translation config. Keys never enter the project folder or the shared `cache/`. This is the right answer, and the README specifically invites users to package, back up and hand-edit their project folders — so a leak here would have been a real one.
- ⚠️ **The latent hazard, recorded because it is exactly the kind that ships silently:** `TranslationConfig.to_metadata()` (`translation_models.py:238–253`) **does** serialize all three API keys, and it is **currently never called** — the only `to_metadata()` callers in the tree are `ocr_config` and `render_config`, both of which *are* written into stage metadata. **The only thing preventing a key leak is that asymmetry, and nothing documents it.** Anyone adding translation metadata to the cache "for symmetry" leaks three credentials into a file users are told to share.
- ⚠️ **The model-loading path is the real exposure, and it is narrower and sharper than the usual one.** `torch.load` and `pickle.load`: **zero hits** — no raw checkpoint deserialization. Instead there are exactly **four `transformers.AutoModel*.from_pretrained` / `AutoImageProcessor.from_pretrained` sites** (`detectors/ogk_manga_rtdetr.py:222,226`, `detectors/pp_doclayout_v3.py:374,379`) plus two in `translator/translator.py:128–129`. That is precisely the path named by **`CVE-2026-4372` / `PYSEC-2026-2290`**, which is unfixed in the pinned `transformers==4.57.3` (fixed in 5.3.0): a malicious `config.json` can name an attacker-controlled Hub repository via `_attn_implementation_internal`. ⇒ **The app has no `torch.load` problem and has, in its place, the four call sites its own pinned dependency's RCE advisory is about.**
- ⚠️ **Google Lens.** The `chrome_lens_*` settings (`chrome_lens_chrome_path`, `chrome_lens_user_data_dir`, `chrome_lens_headless`, `chrome_lens_max_retries=5`, `chrome_lens_language="ja"`) drive Google's consumer Lens OCR via `chrome-lens-py`, whose own PyPI summary names the *"crupload endpoint"* — an undocumented consumer endpoint. ⭐ The README discloses the consequence plainly — *rate limits and temporary IP bans if you abuse large batch scans* (**#83 positive**) — but the config expresses a retry count of 5 and **no backoff**, so the disclosure is in the prose and not in the mechanism.
- ⭐⭐⭐ **`servers/paddleocr_vl/run_server.bat` is committed *generated output*, and the generator is the thing that makes it wrong.** The file hardcodes four absolute paths under `C:\Nghich\Manga-Translator\` — the author's own working directory. My first reading was that this is a hand-written launcher that cannot work on anyone else's machine, and a fleet agent independently reported it as a hand-duplicated port constant drifting from `OCRConfig.port`. **Both are wrong, and the truth is better.** `mmt_core/llama_server.py:198` is `bat_path.write_text(self.build_bat_content(), encoding="utf-8")`, and `build_bat_content()` renders the `.bat` from `build_command()` — `@echo off`, an optional `cd /d "…"`, then **one command token per line** with `subprocess.list2cmdline` quoting, `" ^"` continuations on every line but the last, and a fixed trailing `echo.` / `echo Server stopped. Press any key to close this window.` / `pause >nul`. The committed file has **exactly that shape**, down to the lone `--port ^` on its own line — a form no human writes by hand. ⇒ **The project mechanises the launcher so the port and paths cannot drift from the config, and then committed one machine-specific instance of the generated output into the repository**, where it is not gitignored (`git check-ignore` → not ignored), was committed twice (`26242fb` 2026-05-20, touched `12f503c` 2026-05-22), and sits at a path the README's troubleshooting section does not describe (it tells you to look for a *relative* `tools/llama.cpp/`). **The mechanism is right; the committed artifact contradicts it.**
- ⭐ Also `PyQt_run.bat` still titles its window **"Manga Translator Gemini"**, a stale label from the Gemini-only era — undeclared, and therefore the v255 D40 hazard in miniature.
- 🔴 **A cross-platform bug that cannot work:** `mmt_core/llama_server.py:221` is **`subprocess.Popen(["sh", str(bat_path)])`** — invoking a Windows `.bat` file with the POSIX shell — and `:211` uses `xdg-open`, while `main_window.py:4199–4201` correctly branches `open`/`xdg-open`. The tree contains partial POSIX support in a project whose only documented launcher is a Windows batch file, and the POSIX branch of the server launcher is nonsense on both platforms.

---

## §11½ — ⭐⭐⭐ THE SYNTHESIS: three artifacts outlived the context that produced them, and one carries its own

Read separately, §2, §3 and the `run_server.bat` finding are three unrelated pieces of untidiness. Read together they are one thing, and it is the thing this ship is for.

| Artifact | The context that made it correct | Where that context is now |
|---|---|---|
| **`requirements.txt`** — installs Flask, Werkzeug, socketio, engineio, gunicorn | `app.py` and `templates/`, a Flask web application | **deleted 2026-05-18** (`a41abd7`); the file's last edit predates the deletion by four days |
| **`_model_cache`** + its two comments at `translator/translator.py:38,43` | `.jules/bolt.md` — an AI agent's recorded lesson, which names `_model_cache` by name and says why an instance attribute is wrong | **deleted 2026-05-18**, in the same commit |
| **`servers/paddleocr_vl/run_server.bat`** with `C:\Nghich\…` paths | one run of `build_bat_content()` against one machine's config | **the machine**, which nobody else has — and the generator that supersedes the file is still in the tree |
| ⭐⭐⭐ **`detectors/comic_text_detector.py`** — 512 lines | `matching.py`'s `assign_text_regions_to_bubbles`, which the file imports on **line 9** and calls at **line 456** | **deleted by `2aebd41 "Remove CTD"`, 2026-05-17** — the import was not. **The module raises `ImportError` on load, and nobody has noticed because nothing imports it.** |

⭐⭐⭐ **That fourth row is the sharpest instance of the whole pattern, and I missed it — the critic caught it and I verified it.** `detectors/matching.py` defines exactly six functions (`bbox_center`, `point_in_bbox`, `point_in_mask`, `bbox_area`, `bbox_intersection_area`, `bbox_iou`) and **`assign_text_regions_to_bubbles` is not among them**; `git show 617d044:detectors/matching.py` has it at line 143, and `git log -S` puts its removal in **`2aebd41 "Remove CTD"`**. The symbol now appears exactly twice in the entire tree, both times inside the file that cannot resolve it. So `import detectors.comic_text_detector` fails at line 9 — and the failure is **latent**, because a tree-wide grep shows nothing imports that module (the `"comic_text_detector"` hits in `render_item_utils.py:213,276` are string literals, not imports).

⭐⭐ **This is what "no CI, ever" actually costs, in one line.** A Python project with 152 modules, one of which has been unimportable since 17 May, and **nothing in the world would tell you** — no CI, no test that imports the package, no linter, no import check. A single `python -c "import detectors.comic_text_detector"` would have caught it the day it was made. The file is not merely dead: it is **broken, and its brokenness is invisible precisely because the deadness is total.**

Each of the three still *looks* authoritative. A dependency list looks like a statement of what the program needs. A `# Class-level cache for heavy models` comment looks like a design note. A committed `.bat` looks like the way you start the server. **All three are fossils, and none of them says so.**

Now the counter-example, and it is in the same repository: **`downstream_stale` carries its own context.** The mark is written into the very artifact it invalidates; it names the invalidated stages in machine-readable form rather than implying them; the GUI states it to the person who must act; and the README declares that acting is the human's job. Nothing about it depends on knowledge that lives somewhere else.

⭐⭐⭐ **The rule: an artifact is safe when it carries its own context, and dangerous when its context lived somewhere else and has since gone.** This generalises v255's D32/D40 — *a stale label is safe when declared, dangerous when merely compensated* — by naming what "declared" actually buys you. Declaring the lag is one instance of the artifact carrying its own context. And it identifies the failure mode that is *worse* than staleness: **a deleted rationale leaves an artifact that is currently correct and unmaintainable**, because staleness can be detected by comparison and absence cannot be detected at all.

**The vault's own application is immediate and uncomfortable.** The v245 source-of-truth notice in `_state/03c` works precisely because it lives *inside the file whose name is wrong* — the artifact carries its context. Set against that: the five `_state/` files that were on disk and named nowhere (the CLAUSE-1 FAIL closed by this ship, §12) were artifacts whose context — *why does this file exist, and what supersedes it* — lived only in the memory of the session that wrote them. **That is the same defect as `requirements.txt`, in the operator's own vault, and the script found it in under a second because a machine was finally asked to look.**

---

## §12 — Method, error ledger, sandbox

**Method.** Orchestrator-first: I established the whole spine myself — clone twice and `diff -rq` both ways, `git rev-list` for every structural count, `git check-ignore --no-index` for the test policy, `strings -a -e b` for the fonts, `git show bdcb098` for the import event, `git show bdcb098:.jules/bolt.md` for the deleted agent memory, PyPI `requires_dist` for the pins — then ran a 20-agent `Workflow` (6 surface maps → 6 adversarial checks → 3 situating reports → 3 checks → critic → adversary-over-critic) for breadth and to attack my own findings.

**My own errors, all caught before shipping:**

1. 🔴 **I recorded "all 152 files byte-compile cleanly, exit 0" and it was false.** `python3 -m compileall` was **`Killed: 9`** by the sandbox; the `exit: 0` I read was the exit status of the `tail` at the end of the pipeline, not Python's. This is v255's `set -- $pair` error in a new costume — **a pipeline's `$?` is the last command's, and a killed process at the head of a pipe is invisible.** No Python was executed in this analysis at any point; every claim here is from `git`, `grep`, `strings`, `curl` or reading.
2. ⚠️ **I hypothesised the fonts would be clean and the finding would be trivial.** The first `strings | head -60` pass returned almost nothing and I nearly moved on — TTF name tables sit deep in the file and are frequently UTF-16BE. **Adding `strings -a -e b` and dropping the `head` produced the entire §7 finding.** A negative from a truncated search is not a negative.
3. ⚠️ **I predicted a hard dependency conflict before verifying it, then had to correct the specifics.** My first comma-split `grep` returned the fragment `"huggingface-hub<1.0` and I could have published `<1.0` as the whole constraint; the real string is `"huggingface-hub<1.0,>=0.34.0"`, and the `safetensors` conflict — the cleaner of the two — I had not predicted at all.
4. ⚠️ **A `WebFetch` of the raw README reported 339 lines; `wc -l` says 312** (25,250 bytes, trailing newline present). The fetch summary was a model estimate. **I used the local count.** Recorded because it is precisely the class of number that has bled into three previous ships.

**The fleet's errors (13 reports recovered; the run crashed before the critic stages — see below).** Its adversarial verifiers were the most valuable part, because most of what they caught was other agents' line numbers:

1. 🔴 **A fabricated corpus-first.** One agent claimed "first Vietnamese-authored subject." Its verifier refuted it by naming **v76 agent-skills-standard**, a Vietnam-located solo developer. Not adopted.
2. 🔴 **A fabricated threshold.** One agent cited an unsourced viral-velocity band ("25–150/d MODERATE") to argue about Pattern #52. Its verifier flagged it as citing nothing. Not adopted — and #52 is inapplicable here anyway at 32 page-stated stars.
3. 🔴 **A wrong transport for Chrome Lens** (`google-genai`) — refuted by its verifier and by me: `mmt_core/chrome_lens_client.py:188` and `ocr/chrome_lens_ocr.py:10` both import `chrome_lens_py`; `google-genai` is used by `translator/gemini_translator.py:9–23,45`. ⭐ This also **fixed my own broken dependency census**: my per-package grep pattern was malformed for exactly those two packages, which is why they read as "0 files." They are imported; my list of ten zero-importer requirements correctly excluded them, but the reason it did was luck, not method.
4. ⚠️ **Six wrong line numbers** across three reports (`render_item_utils.py`, `detectors/selection.py`, `text_rendering/layout.py`, `local_llm_translator.py`, and three thresholds in `ocr_text_filter.py`), each caught by a verifier that opened the file. **Consequence for this document: every `path:line` cited here is one I read in my own command output, not one a subagent reported.**
5. ⚠️ **A wrong "hand-duplicated port" finding — which produced the ship's best small finding.** An agent reported the `8080` port as hand-duplicated between `OCRConfig` and `run_server.bat` and therefore drift-prone. Chasing it revealed `llama_server.py:198`: the `.bat` is **generated**. The agent's conclusion was wrong and its instinct was right, and the corrected finding (§11) is stronger than either.
6. ⚠️ **A hallucinated self-correction.** One agent "corrected" a PyQt-vs-PySide statement that no one had made. Its verifier called it a phantom.
7. ⚠️ **A wrong description of `OCRConfig`** ("only provider and model_name") from an agent that reached the right conclusion (no `api_key`) by the wrong route. The dataclass has roughly twenty fields; §6 lists them.
8. 🔴 **The run itself failed, and the bug was mine.** Four agents completed without producing schema-valid output, which dropped those pipeline items to `null`; my final `return` then did `mapResults.map(r => r.key)` with no null guard and threw. 17 of 18 agents had finished (~2.39M tokens, 675 tool uses, 18m40s), and **all 13 non-empty reports were recoverable from `journal.jsonl`** — which is why the harness tells you to read it before assuming anything is lost. The critic and adversary-over-critic never ran and were re-launched separately.

**Sandbox notes (for the next ship).** `python3` and `pip` exist at `/usr/local/bin/` but are **SIGKILLed on invocation** — this finally pins down the vague "python3 is silently broken" note carried since v236: it is not broken, it is killed, and it will fake success inside a pipeline. `timeout` does not exist. `git` is 2.19. Inline `python3 -c` triggers a permission prompt; writing a script to a file and running it does not, but the kill happens either way.

**NOT ESTABLISHED — stated so it is not mistaken for a finding:**

- 🔴 **The upstream project was not identified.** Commit #2 is unmistakably an import (§2), and the repository is not a GitHub fork, but **no agent named the source repository and I did not either.** The evidence for *an* upstream is strong and internal (a Flask app plus `.jules/bolt.md` plus `test_translator_batch.py` arriving in one commit six minutes after repo creation; a `MangaTranslator` class over `deep_translator`/`translators`; a dependency list describing a program that was then deleted). The identity of that upstream is **open**, and every provenance statement in this ship is therefore about *structure*, not about a named source.
- **Whether the fonts' licences are actually violated.** I report what the binaries say. That is a matter for a human, and nothing in the operator's use of this ship depends on resolving it.
- **The exact behaviour of `pip` on this requirements file.** The two constraints are unsatisfiable per PyPI's published metadata; **pip was not run** (§ sandbox note).
- **Any corpus-first claim about the author's locale or the GUI toolkit.** A fleet agent proposed "first Vietnamese-authored subject"; that is **false** — `agent-skills-standard` **v76** is a Vietnam-located solo developer, and `CoreOfPotato` **v231**'s author is in Hà Nội. A second agent proposed "first PyQt6 application," which would need a full corpus grep to support and did not get one. **Neither claim is made anywhere in this ship**, and §41 forbids the locale inference from touching criterion (a) in any case.

**Continuity — the v255 script was run against the vault, and it earned its keep.** `(C) proposed-verify-vault-inventory.sh` reported **1 FAIL / 9 WARN**: the FAIL was **CLAUSE 1**, five `_state/` files present on disk and never named in `CLAUDE.md` (`license-decision`, `public-release-decision`, `publishing-strategy`, `v60-mini-audit-pre-registration`, `v60-mini-audit-results`) — **exactly the finding v255 made and recommended fixing without executing it.** ⭐ **That is the difference a script makes: a recommendation in prose evaporated, the same recommendation in a command re-asserted itself on demand at the next ship.** Fixed this ship; the script now reports **0 FAIL**. Also noted: **31 accreted `★` head blocks** in `CLAUDE.md` (v255 counted 30 — it grew), so this ship **replaces** the v255 head block rather than prepending.

---

## §13 — Verdict summary

**GOAL-ALIGNED INCLUDE 3/4** — (a) **FAIL** (§41: `mranex` is a pseudonymous individual; no declared Anthropic affiliation, no registered vendor-direct source) · (b) **MODERATE** (⚠️ OFF-GOAL recorded as the reviewable alternative) · (c) **STRONG** · (d) **STRONG**. §40 applies: operator-requested, goal-adjacent, no override consumed, no §35 pressure.

**NO MINT.** Counts **46/11 UNCHANGED**; §C live standalones **51** unchanged; surface **≈58** unchanged. Grounds in the Verdict.

**The one sentence:** ⭐ *An unenforced check is a defect only when something claims it is enforced — and the check most likely to survive is the one whose reason was written down next to it.*
