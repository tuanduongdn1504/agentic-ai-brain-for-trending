# (C) Deep Dive — `mranex/translate-LN-pipeline` (wiki v257)

**Ship:** v257 · **Date:** 2026-08-21 · **Verdict:** GOAL-ALIGNED INCLUDE 3/4 · **NO MINT** · counts 46/11 UNCHANGED
**Subject:** *"Manual Studio v3 — Buồng Lái Dịch Thuật Light Novel / Web Novel"*, a PyQt6 desktop workbench for translating Chinese web novels into Vietnamese, README entirely in Vietnamese.
**Author:** `mranex` — pseudonymous. Not Anthropic, not a registered vendor-direct source (§41 ⇒ **(a) FAILS**).
**⭐ Why this ship exists:** it is the **text sibling** of the v256 subject (`my_manga_translator`) by the **same author**, flagged at v256 and requested by the operator — which makes it the corpus's first genuine **same-author control**. §9 is that comparison, and it is the most valuable section here.

---

## §0 — Source verification (D27: the ref population is declared)

Two independent clones, `diff -rq --exclude=.git` **both directions: identical**.

| Fact | Value | Command |
|---|---|---|
| HEAD | `23dd47047a5a5585fbf7ca78c62de76015734128` | `git rev-parse HEAD` |
| Commits HEAD / all refs | **11 / 11** | `git rev-list --count HEAD` / `--all` |
| Root commits | **1** (`71951c5`, 2026-04-26 00:44 +0700) | `git rev-list --max-parents=0 --all` |
| Merges | **0** | `git rev-list --count --merges --all` |
| Refs | `main` only | `git branch -a` |
| Tags | **1**, named **`Windows`** | `git tag` |
| Tracked files | **88** | `git ls-files \| wc -l` |
| Python | **47 files / 12,561 lines** | `git ls-files '*.py' \| xargs wc -l` |
| Also | **18 `.pyc` TRACKED**, 14 `.txt`, 3 PNG, 1 `.spec`, 1 `.bat`, 1 `.json`, `.env.example` | — |
| Window | **2026-04-26 → 2026-05-27** (~31 days) | `git log` |
| Author identities | **three names, ONE email**: `Admin <elsgman1999@gmail.com>` 2 · `mranex <elsgman1999@gmail.com>` 8 · `mranex <…noreply.github.com>` 1 | `git shortlog -sne --all` |
| Page-stated | **7 stars / 3 forks / 0 watching** | rendered repo page |

Page-stated figures only — this environment mocks the GitHub API (§37.4) ⇒ **no Pattern #52 claim**, and 7 stars would not support one anyway.

⭐ **The dating matters for §9:** this repo **predates** the v256 subject by 17 days (2026-04-26 vs 2026-05-13), and **both stop on the same day** — v256's last commit is 2026-05-27 11:39, this one's is 2026-05-27 17:13, five and a half hours apart.

⭐ **The commit log is eleven lines and three of them are notable:** `Antigravity new version` (2026-04-27 — Google's agentic IDE named in a commit subject), `Version 3.0, update Project Manager to Manual Studio` (2026-05-06), and `Làm đẹp và update readme.md` (*"beautify and update the readme"*, 2026-05-22).

---

## §1 — What it is, and the one architectural fact that matters

Ten-plus workflow steps at three scopes (Volume / Chapter / Segment), all artifacts on disk as JSON and JSONL, every artifact editable in a GUI, and a canon layer that keeps terminology consistent across an entire multi-volume series.

**The central fact, stated in the README's own warning block:** the tool **does not call the API.** It renders a prompt, you copy it into whatever LLM you like — Claude, GPT or Gemini are named — you paste the response back, and the tool checks the syntax and files the result. The human is the transport.

That is not a limitation the author is apologising for; it is the product thesis. `requirements.txt` is three lines (`openai>=1.0.0`, `python-dotenv>=1.0.0`, `PyQt6>=6.0.0`) and the `openai` dependency belongs to an older generation (§3), not to the app the README documents.

⭐ **This makes the subject substantially more on-goal than its sibling** and it is why (b) is rated STRONG here against v256's MODERATE. There is no computer vision, no OCR, no inpainting. What is left is **13 versioned prompt templates, a render engine, an output-policy contract, a response parser, a step registry, a confidence field, a review-flag service, and a knowledge layer whose explicit purpose is keeping prompts small.** The LLM is the whole subject.

**Verified from the screenshot the repo ships** (`Screenshot/Prompt_studio.PNG`, 1920×1043 — a real one, see §9b): window title *"Manual Studio v3 - Buồng Lái Dịch Thuật"*, five tabs (Prompt Room / Editor / Project Progress / Canon Library / Release Station), a left tree of Volume → Chapter → Segment with real segment ids (`c001_s001` …), a rendered prompt in the centre, and on the right a paste box captioned *"paste the AI's JSON response here"* with three buttons: **Check Syntax**, **Import Translation**, **Clear**. The copy-paste architecture is visible in the product, not just claimed in the prose.

---

## §2 — ⭐⭐⭐ THE HEADLINE: the README's primary launch command starts the wrong program

The repository contains **three complete generations of the same idea, all tracked, all present at HEAD**:

| Gen | Entry point | Toolkit | What it is |
|---|---|---|---|
| **1** | `run.py` → `python -m src.main <verb>` | **Tkinter** | A control panel with 13 buttons that shells out to a CLI in `src/` (7 modules, 17 verbs). **This generation calls the API itself** (`src/api_client.py`). |
| **2** | `manual_prompt_studio.py` (52,295 bytes) | **Tkinter** | Self-labelled `APP='Manual Prompt Studio v2'` at line 12. Imports `manual_studio.core.project_bootstrap` — the old generation importing from the new package. |
| **3** | `run.bat` → `python -m manual_studio.qt_app` | **PyQt6** | "Version 3.0", `manual_studio/` (30 modules), `ManualStudioV3.spec` for PyInstaller. **This is the only generation the README describes.** |

And the README's installation section says, under *"Khởi chạy ứng dụng"*:

> `python run.py`
> *(Hoặc nhấp đúp vào tệp `run.bat` trên Windows).*

⭐⭐⭐ **`python run.py` opens generation 1** — a Tkinter window whose title bar reads *"Light Novel Translation Pipeline FINAL - Control Panel"* (`run.py:12`) and whose buttons shell out to `src.main`. Everything the README spends 250 lines describing — the Prompt Room, the Editor, the Canon Library, the Release Station, the PyQt6 Cyberpunk theme, the app icon — lives in generation 3, which is reachable **only** through the parenthetical `run.bat`.

**The primary documented launch path starts a program the documentation does not describe.** A first-time reader follows the instruction, gets a different application with a different window title and a different feature set, and has no way to know the README is about something else.

⭐ **And generation 1's own headline button is broken by construction.** `run.py:open_editor()` targets `ln_pipeline_final_editor.py`, which **has never been committed** (`git log --all --diff-filter=A --name-only | grep -c ln_pipeline_final_editor` → **0**). The author anticipated this: the method checks `os.path.exists` and logs a Vietnamese *"file not found in the current directory"* message. **So the most prominent button in the program the README tells you to launch — "📝 MỞ EDITOR FINAL" — fails with a handled error, every time, for everyone.**

---

## §3 — ⭐⭐⭐ Eighteen committed `.pyc`, two of them fossils of source that was never published

`git ls-files '*.pyc' | wc -l` → **18**. And `.gitignore` **line 2** is `__pycache__/`.

`git check-ignore -v --no-index` confirms the rule **would** exclude every one of them. They survive because git ignores only *untracked* paths.

⚠️ **And here is a correction to my own first draft, because the timing is the whole point.** I assumed this repo repeated the sibling's mechanism and asserted the `.pyc` were added "by the same commit that added the `.gitignore`." **That is false**, and a fleet agent flagged it before I published:

```
.gitignore added by:  7a590cb  2026-05-22 13:08  "Update PyQt6 Studio"
the 18 .pyc added by: 71951c5  2026-04-26 00:44  "Initial commit"   (18 of its 45 files)
```

⇒ **The bytecode predates the ignore rule by twenty-six days.** In the sibling repository the two genuinely did arrive together (`bdcb098`, 2026-05-13 00:27:46, adds both `.gitignore` and `translator/test_translator.py`). Here they did not.

⭐⭐⭐ **The corrected finding is sharper than the one I nearly published.** In the sibling, the ignore rule and its exception were written in the same breath — a single moment's oversight. Here, **the author sat down on 22 May, wrote a `.gitignore` whose second line names `__pycache__/`, and left eighteen already-tracked `.pyc` files exactly where they were.** No `git rm --cached`, no cleanup commit, in the five commits that followed. **The rule was authored after the violation and never applied to it.**

⇒ **What replicates across the two repositories is the *outcome* — ignored-yet-tracked files — not the mechanism.** §9a records it that way, which is the honest version and the more interesting one: two different roads to the same dead artifact.

**Sixteen of the eighteen are ordinary staleness:** `src/__pycache__/` holds the same 8 modules compiled **twice**, once by `cpython-312` and once by `cpython-313` — a fossil of the author moving Python versions mid-project, committed both times.

**The other two are the interesting ones:**

```
__pycache__/manual_prompt_studio_v1.cpython-313.pyc   79,818 bytes
__pycache__/manual_prompt_studio_v2.cpython-313.pyc   92,842 bytes
```

`git log --all --diff-filter=A --name-only` shows that **no `manual_prompt_studio_v1.py` or `_v2.py` has ever existed in this repository.** Only their bytecode is here.

Bytecode carries names and string constants, so it can be read without executing anything. `strings -a` on both returns **`tkinter`** and **`ttk`** — ⭐ **both abandoned generations were Tkinter**, before the PyQt6 rewrite. And `_v1` contains a class `App` with `_build_ui`, `applicable_steps`, `build_prompt`, `generate_prompt`, `copy_prompt`, `import_response`, `validate_response`, `refresh_review_queue`, `run_local_step`, `save_artifact`, `open_workspace`, `populate_steps`, `populate_tree`, plus `build_segment_glossary_local`, `build_segment_pronouns_local`, `assemble_volume`, `chapter_glossary_extract` and `chapter_relationship_extract`.

⭐⭐ **The whole pipeline vocabulary — including the deterministic `*_local` steps the README presents as the product's exclusive feature — was already in place in an unpublished Tkinter prototype.** The names line up one-for-one with the numbered templates in `prompts/`.

**And the measurement that keeps this honest.** Of the **117** `def` names in the tracked `manual_prompt_studio.py`, `_v1.pyc` contains **5** and `_v2.pyc` contains **51**. So `_v2` is not the compiled form of the tracked file — it is an **earlier state of the lineage that became it**, and the tracked file has since grown to more than twice that function count **while still calling itself `v2`** at line 12, inside a repository whose README is titled v3.

⚠️ **Name-presence is weak evidence about behaviour** and I am not claiming to know what those generations did. What is established: two Tkinter generations existed, their source was never committed, their bytecode was, and it still ships.

---

## §4 — ⭐⭐⭐ Three confidence thresholds, in three places, and they disagree

The design intent here is genuinely good: the model is asked to attach a confidence score, and low-confidence output is routed to a human. The execution is the vault's recurring disease in its purest form yet.

**Declaration 1 — `config/config.json`**, a `dialogue_labeling` block declaring `review_confidence_threshold: 0.72`, `auto_accept_confidence_threshold: 0.82`, and four escalation conditions: `force_review_if_unknown_speaker`, `force_review_if_unknown_listener`, `force_review_if_multiple_possible_speakers`, `force_review_if_no_matching_pronoun_rule`.
🔴 **That file is read only by `src/config_loader.py:6` — generation 1.** Generation 3 reads a *different* file, `project_config.json`, via `workspace.py:22–27`. **The canonical policy file is orphaned from the application the README documents.**

**Declaration 2 — the prompt.** `manual_workflow.py:117–118` and `manual_prompt_studio.py:528` hardcode the pair **0.72 / 0.82** as literals and inject them into the prompt as `dialogue_labeling_config`. ⭐ **So the model is told the thresholds.**

**Declaration 3 — the code that actually acts.** `review_flags.py:101` and `:104`, plus `editor_actions.py:455`, test **`confidence < 0.8`**.

⭐⭐⭐ **The model is told 0.72 and 0.82. The application enforces 0.8. The file that declares the canonical pair is not read by the application at all.** Three copies of one policy, in three locations, and **the enforced value matches neither declared value.** And the four `force_review_if_*` conditions — the most valuable part, the part that says *always escalate when you could not identify the speaker* — appear in **zero** of the 47 Python files.

⚠️ **I had this wrong at first and the correction matters.** My first pass concluded the policy was "declared and not implemented." It is not: `review_flags.py` (139 lines) is a **real, working** review service that emits structured `ReviewFlag(severity, source, item_id, message, payload)` objects and aggregates them per segment and per volume. The defect is not absence — it is **triplication with disagreement**, which is worse, because each copy looks authoritative on its own.

⚠️ **The steelman, which the fleet's adversary argued and which deserves recording:** in a render-and-paste architecture, telling the *model* the thresholds is a legitimate design, and code-level gating would be a different product — the numbers are guidance for the model and the human, not an automation contract. **I accept that for declarations 1 and 2 and it does not rescue the position**, for two reasons. First, declaration 3 exists: `review_flags.py` *does* gate in code, at 0.8, so the project is not abstaining from enforcement — it is enforcing a different number than it publishes. Second, the four `force_review_if_*` conditions are not thresholds at all but *rules*, and they are absent from the prompt as well as the code — so the model is not told them either. **A design that delegates a decision to the human still has to tell somebody the rule, and these four are told to nobody.**

---

## §5 — What is actually wired, and it is more than I expected

The vault's habit is to look for the gap. Here the credit column is substantial, and one loop is complete.

⭐⭐⭐ **ONE ESCALATION PATH IS FULLY CLOSED, and it is the model that opens it.** `prompts/03_build_segment_glossary.txt:11` instructs: if a highly important term appears in the segment but is **not** in the volume glossary, put it in `missing_glossary_candidates` **for human review**. `review_flags.py` reads exactly that field and raises a `warning`-severity flag — *"Segment glossary has missing glossary candidates."* — which the UI surfaces. **Prompt, data schema and gate all agree on one field name, and the loop runs from the model's own uncertainty to a human's screen.** That is the single best thing in the repository, and it is the pattern the other three thresholds failed to achieve.

⭐⭐ **The prompts are good.** Reading the rendered prompt in the shipped screenshot: a role line, the `{{genre}}` context injected, explicit scope fences (*do NOT translate the novel; do NOT merge relationship data here; do NOT overwrite existing canon*), a **precedence rule** (existing canon outranks chapter-level guesses), a **conflict protocol** — when a new suggestion contradicts canon, *mark it as conflict* rather than overwrite — and two-tier status semantics that tell the model **how a downstream model will consume the field** (`confirmed` = force this exact term; `tentative` = use as reference, may adapt). Then a strict output contract: JSON only, no markdown, no code fences, no comments, `null` when unknown, `[]` for empty arrays, confidence a number from 0 to 1. **12 of the 13 templates consume the shared `{{JSON_OUTPUT_POLICY}}`** (the 13th *is* the policy).

⭐⭐ **Every canon entry carries its own provenance.** From the Editor screenshot's raw-JSON panel, a glossary row holds `id`, `source`, `vi`, `type`, `status`, `variants[]` with per-variant `source_items: ["c001","c002"]` and `confidence`, plus `appears_in: [1,2]` and a top-level `confidence`. ⭐ **Each entry records which chapters and volumes it came from** — which is exactly the "an artifact carries its own context" rule that v256's synthesis was built on, **satisfied here by the same author who violated it four times next door.**

✅ **`response_parser.py` (57 lines) is careful work.** `strip_fences` removes ```` ```json ```` wrappers; on a parse failure `_extract_outermost_object` walks the string with correct handling of quotes and backslash escapes to pull the outermost `{…}` out of chatty prose. That is the right algorithm, not a regex guess.

🔴 **THE ONE THE FLEET FOUND AND I MISSED, AND IT IS THE SHARPEST DOCS-VS-CODE CONTRADICTION IN THE REPOSITORY.** The README's durability section is headed *"Cơ Chế Nạp Dữ Liệu & Khôi Phục **Siêu Bền Bỉ**"* — *super-durable data loading and recovery* — and its first subsection argues for the JSONL row format on exactly this ground: storing each segment as one JSON line *"makes reading and writing extremely independent, avoiding one line's error ruining the entire large data file."*

The reader is `jsonio.read_jsonl`:

```python
def read_jsonl(path: Path) -> list[Any]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
```

⭐⭐⭐ **A list comprehension with a bare `json.loads` and no per-row `try`. One malformed line raises `JSONDecodeError` and the caller loses every row in the file** — which is precisely the failure the format was chosen to prevent, argued for by name, one section above. And the blast radius is the whole app: `artifact_store.upsert_jsonl`, `progress`, `review_flags` and `editor_index` all read through it, so a single corrupt line takes out that artifact's history, its progress calculation and its review flags together.

⚠️ **Note also that the README's own example row is `{"item_id": "seg_001", "status": "done", …}`** — while the code writes `"success"` (`artifact_store.py:25`) and both release gates test `!= "success"`. **The documented schema value would be silently skipped by the gate that reads it.**

✅ **The `.bak` mechanism is real** — `jsonio.py:39–42`, `shutil.copy2` to a `%Y%m%d_%H%M%S`-stamped sibling, called before every overwrite from `series_canon.py:607` and `artifact_store.py:34,65,71,79`. ⭐ **And it is what actually delivers the durability the JSONL paragraph claims** — just not for the reason, or in the place, the README says.
⚠️ **But the README misattributes it** to `manual_studio/core/workspace.py`, where it does not exist — a MISATTRIBUTION, not a missing feature.
⚠️ **And the durability claim is overstated:** `jsonio.write_json` is a plain `path.write_text` with no temp-file-and-rename, so it is **not crash-atomic**. The `.bak` protects the *previous* version; a crash mid-write can still truncate the current one. The README says *"even if you lose power or the machine hangs."*

✅ **The release path has real diagnostics and one genuinely loud failure.** `release_service.py` computes `missing_segments` / `missing_count` (capped at 200) before publishing, and the Calibre push checks the subprocess return code — `"success": result.returncode == 0` (`:386–401`) — rather than assuming it worked.

✅ **The three-level prompt override exists**, at `workspace.py:34–44`: `prompts_root` walks `root/prompts`, `parent/prompts`, `parent.parent/prompts` and returns the first that exists.
🔴 **But it resolves a *directory*, not a *file*.** `prompt_engine.load_prompt` is one line with no `try/except`, so a project that creates `data/<project>/prompts/` to override **one** template will make `prompts_root` select that directory and then fail to find the other twelve. **The documented per-prompt customisation requires copying all 13 templates**, and nothing says so.

🔴 **And one silent degradation.** `prompt_engine.render` reads `00_json_output_policy.txt` and, if it is absent, sets `json_policy = ""` and renders anyway — so a missing output policy produces a prompt with **no JSON contract at all**, with no warning. The model then answers in prose and the failure surfaces later, at the parser.

---

## §6 — No request/response alignment validation anywhere (extent stated)

The sibling repository defends response alignment in five layers, including a per-item index check and a fall-back-to-source policy. Here:

`grep -rn --include=*.py -E 'len\([^)]*\) *[!=<>]=+ *len\(|mismatch|expected .*items|same length' .` across **all 47 Python files** returns **nothing**. `response_parser.py`, read in full, validates exactly one property: **that the response parses to a JSON object.**

⚠️ **The fair reading, and it is genuinely fair:** the UI button is labelled **"Kiểm Tra Cú Pháp"** — *check syntax* — and the README promises *"kiểm tra cú pháp phản hồi"*, checking the response syntax. **The check claims exactly what it does.** By v256's own rule — *an unenforced check is a defect only when something claims it is enforced* — this is a **gap, not a lie.**

It is still a gap that matters, and here is where it bites: `ArtifactStore.upsert_jsonl` (`artifact_store.py:25`) writes `row.update({"item_id": item_id, "status": "success", "result": obj})`. **The status is the literal string `"success"`, assigned at write time**, meaning *a row was written*, not *the content was right*.

And two release gates read that field: `release_builder.py:354,364` and `release_service.py:140,150`, both `if row.get("status") != "success": continue`.

⭐⭐⭐ **The only code in the repository that can write `"failed"` is `src/pipeline.py:28` — generation 1**, which returns `{"item_id": iid, "status": "failed", "error": str(e)}` when its API call raises. In generation 3, the generation the README documents and `run.bat` launches, **the sole writer of that field is a constant.** So the release gate is correctly written, consumed in two files, and **inert in the generation it ships with** — it can never exclude anything, because nothing can ever be marked excluded.

⭐ **That is the sharpest form yet of the theme the last seven ships have circled: the gate outlived its signal source.** v250 aimed a gate at the wrong thing; v252 labelled unautomated rules "Automated"; v256 kept artifacts whose context had been deleted. Here a working gate reads a field whose only varying writer belongs to a generation that is no longer the product.

---

## §7 — No licence at all (extent stated), and the sibling got one the same day

Searched: **0** of 88 tracked files match `licen|copying|notice`; **0** such files added in any of the 11 commits on any ref; **0** licence headers (`SPDX|Licensed under|GNU General|MIT License|Apache License|Copyright (c)`) across all 47 `.py` files; the README mentions licensing **zero** times.

⇒ **This repository is published with no licence grant whatsoever** — GitHub's default, all rights reserved. It has **3 forks**.

⭐⭐ **And the same-author timing is remarkable.** The sibling repo's *final* commit, `Create LICENSE` on **2026-05-27 at 11:39**, added AGPL-3.0 — from a browser dropdown (it is one of only three commits there made through the GitHub web UI). This repository's final commit is **2026-05-27 at 17:13**, five and a half hours later, and it is `Upload input source`. **On the same afternoon the author licensed one project and did not license the other.** No inference about intent is available or needed; the fact is the fact.

**For the operator this is the harder fence, not the softer one.** AGPL is restrictive but *known*: it tells you what you may do. No licence tells you that you may do **nothing** — no copying, no vendoring, no derivative. §Pilot treats this accordingly.

---

## §8 — Security

✅ **The secrets posture is clean, and I tried to refute it.** `config/config.json` stores **`"api_key_env": "DEEPSEEK_API_KEY"`** — the *name* of the environment variable, not a key. `.env.example` is one line, `DEEPSEEK_API_KEY=sk-...`, a placeholder. `.gitignore` covers `.env`. No key is committed anywhere in the tree.

🔴 **Command injection, confirmed, in the program the README tells you to run.** `run.py:173` is `subprocess.Popen(cmd, shell=True, …)` where `cmd` is an f-string built from `self.get_vol()`, and `get_vol()` (`:135–137`) returns the **raw contents of a text-entry field**, defaulting to `"1"` only when empty. Typing a shell metacharacter into the Volume box therefore executes it. `:197` is a second `shell=True`, for the editor launch. ⚠️ **The sibling repository has zero `shell=True` in 152 files; this one has two in 47** — see §9d.

⚠️ **`openai>=1.0.0` is an unbounded major-version floor** in a three-line requirements file with no lockfile. Generation 1's `api_client.py` is the only consumer, and a future `openai` 2.x is free to break it.

⚠️ **The committed bytecode is a mild disclosure issue in its own right:** committing `.pyc` publishes derived content — names, docstrings, string constants — of source the author chose not to publish (§3).

⚠️ **The shipped screenshots embed the author's local path**, `C:\Users\Admin\Desktop\translate-LN-pipeline`, visible in the status bar of both PNGs. That also corroborates the `Admin` git identity as the same machine. The sibling committed `C:\Nghich\Manga-Translator\…` in a generated `.bat` — the same habit, a different artefact.

---

## §9 — ⭐⭐⭐ THE SAME-AUTHOR CONTROL: which habits replicate, and which do not

One author, two projects, overlapping months, and one ends the day the other does. That is as close to a controlled experiment as this corpus gets. **A habit that appears in both is a much stronger finding than either repo alone can support.**

### Habits that REPLICATE (same-author N=2)

**(a) ⭐⭐⭐ Ignored-yet-tracked files — the same outcome by two different routes.** v256: `.gitignore:49` = `test_*.py`, and `translator/test_translator.py` is tracked. v257: `.gitignore:2` = `__pycache__/`, and 18 `.pyc` are tracked. Verified in both clones with `git check-ignore -v --no-index`: in both cases the rule *would* exclude the files, and git ignores only untracked paths.

⚠️ **The mechanism differs, and I had this wrong at first (§3).** In v256 both arrived in **one commit** (`bdcb098`, 2026-05-13 00:27:46) — a single oversight. In v257 the 18 `.pyc` came with the **root commit** (`71951c5`, 2026-04-26) and the `.gitignore` **twenty-six days later** (`7a590cb`, 2026-05-22) — so the author wrote a rule naming `__pycache__/` while eighteen tracked `.pyc` sat in the tree, and never removed them.

⇒ **What replicates is the outcome, not the route.** That is the weaker claim and the true one; it is also the more interesting one, because two unrelated routes reaching the same dead artifact is better evidence of a *disposition* than one repeated slip would be.

**(b) ⭐⭐ Multiple declarations of one fact, with nothing reconciling them.** v256 declares its stage DAG four or more times (`DOWNSTREAM_STALE_STAGES` in three files plus the GUI panel order). v257 declares its confidence policy three times — and, unlike v256's, **the copies disagree** (§4).

**(c) ⭐⭐ Committing artifacts that carry the author's own machine paths.** v256: a generated `run_server.bat` hardcoding `C:\Nghich\Manga-Translator\`. v257: two screenshots showing `C:\Users\Admin\Desktop\`.

**(d) ⭐⭐ Generations left in the tree rather than removed.** v256: the vendored upstream's dead root scripts, a comic-text detector that cannot even be imported, and a requirements file describing a deleted Flask app. v257: three whole generations coexisting, 18 `.pyc`, two orphan bytecodes, an uncommitted editor the UI still calls, and a config file the current app does not read.

**(e) ⭐ No CI, no tests, no agent surface — in both.** Zero `.yml`/`.yaml` ever on any ref in either repository; zero `CLAUDE.md`/`AGENTS.md`/MCP/skill files in either. Two clean **#12 negatives** by the same hand.

**(f) ⭐ An unbenchmarked headline number.** v256: VRAM figures and model recommendations with no measurement anywhere. v257: *"saves up to 80% token cost"*, appearing **only** at `README.md:119` — no measurement in any file (§10).

### Habits that do NOT replicate — and the ordering is the interesting part

**(g) ⭐⭐⭐ The screenshots.** v256's README embeds `Screenshot/Main_UI.png` and `Screenshot/Editor_UI.png`, **neither of which has ever existed**, with the boilerplate TIP telling the author to add them still sitting underneath. v257's README embeds `Screenshot/Prompt_studio.PNG` and `Screenshot/Editor.PNG`, **both of which exist**, at matching case, committed by `4b6fa8c "Up Screenshot and readme.md"` on **2026-05-22**.
⭐ **And v256's README was last updated on 2026-05-23 — the day after.** So the author added real screenshots to this repository, and then, the next day, edited the other repository's README while leaving its two image references pointing at files that had never existed. **Not a learning curve. Two projects, side by side, one tended and one not.**

**(h) ⭐⭐ `requirements.txt`.** v256: 24 lines, pins spanning two and a half years, **two mutually unsatisfiable constraints** — `pip install -r requirements.txt` cannot resolve. v257: **three lines**, `>=` floors, satisfiable. Same author, same month, opposite outcomes.

**(i) ⭐⭐ `shell=True`.** v256: **zero** across 152 files. v257: **two** in 47, one of them reachable from a text field (§8).

**(j) ⭐ Licensing.** v256: AGPL-3.0, added from a browser on the final day. v257: **none, ever** — five and a half hours later the same afternoon (§7).

**(k) ⭐⭐ Response validation.** v256: five layers, including a per-item index check and a documented fall-back-to-source. v257: **none** (§6) — in the project where the LLM round trip *is* the product.

### What the control actually shows

⭐⭐⭐ **The replicating habits are all about *bookkeeping*: ignore rules, duplicated declarations, committed machine-specific artifacts, dead generations, absent CI, unmeasured numbers. The non-replicating ones are all about *care applied to a particular surface*: this repo's dependency list is clean and the other's is broken; the other's response validation is excellent and this one's is absent; one has screenshots and the other does not; one is licensed and the other is not.**

⇒ **The habits are the constant; the quality is the variable.** The same developer produces disciplined work on whichever surface he happened to be thinking about, and identical structural sloppiness everywhere he was not. That is a more useful model of this author — and of AI-assisted solo development generally — than either repository alone would support, and it is the reason a same-author control was worth spending a ship on.

---

## §10 — The 80% claim

The README's central justification for the Active Volume Canon — scan the source text, include only the entities actually present, keep the prompt lean — is *"tiết kiệm tới 80% chi phí token"*, **saves up to 80% of token cost.**

That string appears at **`README.md:119` and nowhere else in the repository.** No benchmark, no measurement, no eval, no recorded before-and-after — searched across all 47 `.py`, all 14 `.txt`, and the 3 `.md`-class files.

**The mechanism itself is real and simple.** `series_canon.py:124` `build_active_volume_glossary` concatenates the volume's chapter and segment text into one `source_text`, then for each series-canon entry takes its match terms (`glossary_entry_match_terms`, `:487` — the entry's `source` field plus any declared `aliases`) and keeps the entry when **`any(term in source_text for term in terms)`** (`:133–134`). A plain substring test, no tokenisation, no embedding, no index.

⭐ **That is the interesting part: retrieval by presence rather than by similarity.** No vector store, no threshold, just *does this string occur in the text in front of me*. For a bounded, named-entity knowledge base it is a genuinely good trade, and it is the idea worth taking (§Pilot).

⚠️ **And its false-negative mode is structural, not incidental.** An entity present only as a pronoun, or under an alias nobody has declared yet, does not match — so it is dropped from the prompt exactly when the model would most need it. `build_active_volume_relationships` (`:324`) is stricter still: a relationship survives only if **both** parties matched, so one obliquely-referenced character removes the pair. Nothing counts or reports how many entries were dropped, which is also why no measurement of the 80% is possible from the outside.

⭐ **The mechanism is sound, the figure is unsupported**, which is the same shape as v256's VRAM numbers. Take the idea; do not cite the number.

---

## §11 — Method, error ledger, sandbox

**Method.** Orchestrator-first: two clones and `diff -rq` both ways; `git rev-list`/`--max-parents=0`/`shortlog` for every structural count (D39); `git check-ignore --no-index` for the ignore-rule finding; `git log --all --diff-filter=A` for every "never existed" claim; `strings -a` on the orphan bytecode; both shipped screenshots read as images; then a fleet for breadth and adversarial pressure.

**My own errors — three, all caught before shipping, and two are the same class:**

1. 🔴 **I asserted the README's `.bak` claim was false after grepping one file.** The README names `workspace.py`; `backup()` is in `jsonio.py`. A whole-tree search found it immediately. **The feature is real and the README misattributes it** (§5). This is **D42 exactly** — a negative from a narrow search — and it is the *second consecutive ship* where I made that mistake (v256: the fonts behind a `head -60`).
2. 🔴 **I concluded the three-level prompt lookup did not exist**, again from reading one file (`prompt_engine.load_prompt` is a single line). It exists at `workspace.py:34–44`. **The real finding is subtler and better:** the chain resolves a directory, not a file (§5).
3. 🔴 **I first recorded the confidence policy as "declared and not implemented."** Wrong: `review_flags.py` implements it — at a **third, different threshold**. The corrected finding (§4) is stronger than the error would have been.

4. 🔴 **The one that actually reached the fleet: I asserted the `.pyc` were added by the same commit as the `.gitignore`, by analogy with the sibling, without checking.** They were not — twenty-six days apart (§3). **A fleet agent caught it; the anti-critic then repeated my wrong version back to me as "Established GT confirms…".** ⇒ ⭐⭐ **A ground-truth block handed to a fleet is an amplifier: one unchecked assertion propagated into sixteen agents and came back wearing the authority of confirmation.** Everything in a ground-truth block must be a command's output, not an inference from the previous ship — and the corrected finding (a rule authored after the violation and never applied) is better than the symmetry I assumed.

⭐ **The pattern in my first three errors is worth naming, because it is the same one I keep finding in these subjects: I read the file the documentation pointed at, found nothing, and nearly published the absence.** The fix is mechanical — search the tree, then read the file — and it is now three ships in a row that this has mattered (v255 the word-split, v256 the truncated font search, v257 three misattribution traps). **D45** in the Verdict.

**The fleet's errors (16 agents, 14 completed, 2 errored; ~2.05M tokens, 483 tool uses, 14m26s):**

1. 🔴 **Context bleed, for the FIFTH consecutive ship.** An agent reported this repository's `requirements.txt` as containing `transformers==4.57.3` and `huggingface-hub==0.22.2` — **v256's pins**, from the injected vault state. Its verifier refuted it by reading the actual three-line file. **Five ships running, the same failure mode.**
2. 🔴 **Wrong line numbers across three reports** — `release_service.pack_epub_from_html` cited at :458 (actually :288), the Calibre call at :512 (actually :377), a progress function at :73 (actually :75). Caught by the verifier. **Consequence: every `path:line` in this document is one I read in my own command output.**
3. 🔴 **A fleet agent asserted `python run.py` launches `manual_prompt_studio.py` (generation 2).** It launches generation 1. Its verifier caught it.
4. ⚠️ **An agent claimed `config/config.json` is read by `manual_studio/workspace.py` and not by `src/config_loader.py`** — the exact inverse of the truth. I re-verified: `config/config.json` appears in `src/config_loader.py:6` and `src/main.py:19` only; `workspace.py:23` reads `project_config.json`.
5. ⚠️ **The anti-critic mistook the subject's defects for the ship's blockers**, listing "add a LICENSE, fix the shell injection, `git rm --cached` the `.pyc`, delete generation 2" as **"BLOCKERS BEFORE SHIPPING."** Those are recommendations to the author of a repository nobody here controls. **A wiki documents its subject; it does not repair it.** Rejected.
6. ⚠️ **The anti-critic also over-applied my own method rule**, treating the prior-art agent's WebSearch as a violation of "do not import findings from outside the clones" and concluding that *within the vault* this might be a corpus-first. **Prior art is a fact about the world, not about the vault.** No corpus-first is claimed anywhere in this ship.

✅ **What the fleet earned:** the `read_jsonl` contradiction (§5) — the sharpest docs-vs-code finding here and one I had walked straight past; the canon filter's exact matching mechanism and its both-parties relationship rule (§10); the confirmation that the Calibre shell-out is safe and that progress is derived purely from disk; and the correction to my `.gitignore` assertion. ✅ **And the adversary-over-critic caught the critic conflating NO MINT with OFF-GOAL — the third consecutive ship on which that conflation has appeared and the second on which the adversary has rejected it**, with §40 quoted from the routine file. The v255→v256 refinement is holding.

**Sandbox.** `python3` and `pip` exist at `/usr/local/bin/` and are **SIGKILLed on invocation** — no Python ran at any point in this analysis, and inside a pipeline the kill is silent (v256 **D41**). `timeout` does not exist. `git` is 2.19. The fleet's first launch failed to parse on an unescaped backtick inside a template literal, and the failed script was **not persisted**; writing the script to a file and invoking it with `scriptPath` is the reliable path.

**NOT ESTABLISHED — stated so it is not mistaken for a finding:**

- **What the two Tkinter generations actually did.** Bytecode name-presence is weak evidence. Established: they existed, they were Tkinter, their source was never committed, their bytecode ships.
- **Whether `deepseek-reasoner` supports the `json_mode: true` that `config/config.json` sets for it.** If it does not, the shipped config for generation 1 is defective. Referred to the fleet; not asserted here.
- **Whether the 18 `.pyc` are stale relative to their `.py`.** Comparing a PEP 552 header against the source requires reading the file, and no Python could run.
- **Any corpus-first claim.** None is made in this ship. The author's locale is recorded as context only — §41 forbids it touching criterion (a), and the corpus already holds Vietnam-located solo developers (v76, v231).

---

## §12 — Verdict summary

**GOAL-ALIGNED INCLUDE 3/4** — (a) **FAIL** (§41) · (b) **STRONG** ⚠️ *MODERATE recorded as the reviewable alternative* · (c) **STRONG** · (d) **STRONG**. §40 applies: operator-requested, goal-adjacent, no override, no §35 pressure.

**NO MINT.** Counts **46/11 UNCHANGED**; §C live standalones **51** unchanged; surface **≈58** unchanged. Grounds in the Verdict.

**The one sentence:** ⭐ *The habits are the constant and the quality is the variable — the same developer, in the same month, wrote a clean dependency list here and an unsatisfiable one next door, and left the identical bookkeeping mistake in both.*
