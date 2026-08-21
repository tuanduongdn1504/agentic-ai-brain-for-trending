# (C) Pilot Methods Menu — `mranex/VOCra` (v258)

**Headline verdict: READ-AND-BORROW. One idea is worth ninety minutes; nothing here is worth installing.**

This is the third repository by this author in three ships, and the honest position is that **most of what is valuable was already banked at v256 and v257.** What is new is one pattern (§Rung 1) and one rule (§Rung 2). The rest of the value in this ship is the comparison, not the code — and that lives in the Deep Dive, not here.

---

## The fences

| Fence | Why it binds |
|---|---|
| ⚠️ **MIT claimed in prose, with no licence file** | `README.md:169` states the project is distributed under MIT. There is **no licence file** among the 93 tracked files and none in any of the 6 commits. This is the **most permissive of the three siblings** — v257 grants nothing at all, v256 grants AGPL — but it is not the conventional artifact. Treat it as *an express grant in a non-standard place*: safe to read and learn from, and if you were ever to reuse a line of it, you would want the grant in a file first. Everything below is re-derivable from a paragraph anyway. |
| 🔴 **Not reproducible: there is no dependency manifest** | No `requirements.txt`, no `pyproject.toml`, nothing. The install instruction is a bare `pip install PySide6 numpy opencv-python Pillow pillow_heif requests scikit-image` at `README.md:129` — **seven packages, zero pins.** You cannot reconstruct the environment this was written against, so any "it works for me" is unverifiable. |
| 🔴 **The committed launcher is one machine's** | `servers/run_server.bat` hardcodes `C:\Nghich\vocra\tools` and `C:\Nghich\vocra\models\paddleocr_vl\`. It is **generated output** (`llama_server_manager.py:48` builds it, `:99–100` writes it), so the committed copy is a fossil of the author's machine — the same habit as v256's `C:\Nghich\Manga-Translator\`. |
| ⚠️ **A launcher path that cannot work off Windows** | `llama_server_manager.py:131` is `subprocess.Popen(["sh", str(bat_path)])` — the POSIX shell invoked on a Windows `.bat`. Identical to v256's `llama_server.py:221`. On macOS this fails; on Windows the branch is never taken. |
| ⚠️ **No CI, no tests, ever** | Zero `.yml`/`.yaml` across all 6 commits; zero test files among 93. Nothing here has been checked by anything but its author's own use. |
| ⚠️ **Use context** | The tool exists to lift burned-in subtitles off video files. Whether any given input is yours to process is a question about the input, not the tool — worth stating plainly because it is the actual reason to keep this at arm's length from anything client-facing. |

**Can the operator run it?** Probably partially — PySide6 is cross-platform and there is no Windows-only import at the entry point — but there is no reason to. The OCR path needs a local `llama-server` plus GGUF weights, the launcher path is Windows-shaped, and nothing in the pilot requires execution.

---

## Rung 0 — 25 minutes, read only

Four artifacts, in this order. This is the whole intellectual payload.

1. ⭐ **`vocra_translator/plan.md`** (75 lines). Read it, then open `vocra_translator/core/provider_factory.py:3–5` and see the decision honoured by three import lines. **This is the only place in three repositories where a written decision demonstrably shaped the code**, and it takes four minutes to confirm.
2. ⭐⭐ **`git show 3c8d5ab:docs/progress.md | head -40`** — a 2,064-line agent-style working-memory file (*Current Goal · Completed · Blockers / Risks · Architecture Decisions · Next Recommended Steps*), committed three hours into the project and **deleted eight hours later** by `7e5f67d`. Then `git show --shortstat 7e5f67d` for the commit that removed it, the `.gitignore`, and an entire three-layer application in one change.
3. **`vocra_core/final_ocr/base.py`** (19 lines) and **`provider_factory.py`** (17 lines) — a Protocol and a dispatch function that raise on an unknown provider. Thirty-six lines doing the work that took 1,342 lines of ad-hoc clients in the sibling.
4. **`vocra_core/translator/openai_compatible.py:173–181`** — the alignment guard, carried forward from v256 and *not* present in v257. The Deep Dive §5 is the chronology; the code is four lines.

---

## Rung 1 — 90 minutes, the one genuinely new transfer: a cheap deterministic filter in front of the expensive model

**The pattern.** VOCra never sends every frame to the OCR model. It crops to the subtitle region, then runs **SSIM** (structural similarity) between consecutive frames at a `0.95` threshold and drops the near-identical ones, because a subtitle sits still for dozens of frames. Only the survivors reach the model.

That is not a video trick. It is the general shape: **when the expensive step is a model call, put a cheap deterministic comparison in front of it and only pay for what is actually different.** It is the same family as v257's Active Volume Canon (filter the knowledge base to what is present) but on the *input* side rather than the *context* side.

**Where it lands in hireui.** Three concrete places, in descending value:

1. **Near-duplicate CV detection before parsing.** One candidate applying to five roles, or re-uploading a document with a title tweaked, should not cost five LLM parses. Normalise the extracted text, hash it, and compare cheaply — then reuse the cached structured result and record that you did.
2. **Unchanged job descriptions across postings.** The same requirement text re-posted should not be re-analysed.
3. **Re-parse suppression after a trivial edit.** If a recruiter fixes a typo in a note, the expensive downstream inference does not need to re-run.

**The design, in five lines:**

```
for each incoming document:
    key = normalise(text)                  # casefold, collapse whitespace, strip boilerplate
    if similarity(key, seen_keys) >= T:    # cheap: hash equality, then a shingle/Jaccard pass
        reuse(cached_result); record(SKIPPED, reason, similarity)
    else:
        result = expensive_model_call(doc)  # the only place money is spent
        seen_keys.add(key); record(PROCESSED)
emit_metric(skipped / total)               # <-- the part VOCra does not do
```

⭐⭐⭐ **And here is the discipline to add that VOCra lacks, which is the real lesson.** Its README claims the SSIM filter removes *"up to 90%+"* of duplicate frames. **Nothing in the repository measures it** — no counter, no log, no benchmark, searched across all 75 `.py`, both `.md` and the config. So the filter's actual drop rate is unknown to its own author.

**A deduplication filter is a silent lossy stage.** Set the threshold slightly wrong and it discards real inputs — a subtitle that changed by one character, a CV that differs only in the one line that matters — and **nothing fails.** So:

- **Emit the drop rate as a metric on every run**, not as a README claim.
- **Log what was dropped and why**, with the similarity score, so a wrong threshold is discoverable after the fact.
- **Make the threshold a single named constant** with one owner. (VOCra gets this right by accident: `0.95` appears as a default in six places and **all six agree** — where v257's three copies of a threshold disagreed. Do it deliberately: declare it once and derive.)

**Deliverable:** a section in `hireui/evals/METHOD.md` plus the guard in the ingest path, and a test that feeds two near-identical documents and asserts (a) the second is skipped and (b) the skip is recorded with its score. **Nothing installed, nothing copied.**

---

## Rung 2 — 60 minutes: the plan-as-fence rule, pointed at your own vault

**The finding, measured** (Deep Dive §3): the surviving 75-line plan names the translator core, and the translator core is genuinely **shared by import**. It says nothing about widgets — so `scene_nav_button.py` is a **byte-identical 117-line copy** in both apps, `log_panel.py` differs by two lines, `theme.qss` by fourteen, and a **788,588-byte icon is committed twice** (roughly 1.5MB of a 3.9MB clone).

⭐ **A plan document is a fence around exactly the surfaces it names. Name the boring ones too.**

**Why this is about your vault and not about him.** The companion finding (Deep Dive §5) is that **code moves forward in time and never backward**: the alignment guard invented in v256 travelled into v258 eleven days later and never reached v257, which was edited six times after the guard existed — including on the last recorded day of all three repositories. Copy-forward is a one-way ratchet.

**The vault has the same shape.** `05 Skills/` holds skills that are copied and re-versioned rather than shared; the routine exists in v2.1 through v2.7 as separate files; the same disciplines are restated in `CLAUDE.md`, in `_state/`, and in each ship's documents. **A fix made in the newest copy will not reach the older ones, for exactly the reason it did not reach v257: nothing carries it back.**

**Two concrete moves, both cheap:**

1. **Write down which surfaces are shared and which are copied** — one short section, named explicitly, in `CLAUDE.md`. Per the fence rule, an unnamed surface will drift.
2. **For anything genuinely shared, make it a single file with one owner** and reference it, rather than restating it. The vault already proved this works: the v245 source-of-truth notice inside `_state/03c` is a shared fact with one declared owner, and the v255 script now machine-checks it.

---

## Rung 3 — DECLINED

There is no rung that installs or runs this. The OCR stack needs local GGUF weights and a Windows-shaped launcher; the environment is unpinned; and for document extraction the better-aimed corpus sources remain **v217 wardrobe** (vision → confidence-scored JSON → anti-fabrication → QA gate) and **v256**'s five-layer alignment guard — which is, note, the same author's earlier repository and still the best thing he has written on that axis.

---

## 🔴 NEVER

- **Cite the "90%+ frames removed" or "100% of noise eliminated" claims.** Both appear only in the README; nothing in the repository measures either.
- **Expect `pip install -r requirements.txt` to work** — there is no manifest of any kind.
- **Run the committed `servers/run_server.bat`** — it points at `C:\Nghich\vocra\` on a machine that is not yours, and it is generated output that the app rewrites anyway.
- **Trust the README's top-of-page links** — the logo URL contains the literal placeholder `your-username` and returns HTTP 404.
- **Assume the tree is the repository.** The interesting parts of this subject are in the pack: a deleted three-layer application, a deleted CLI, a deleted GUI, and 252KB of deleted documentation. `git ls-files` shows none of it.
- **Point this at any video you do not have the right to process** — the fence is the input, not the tool.

---

## The one sentence

⭐ *Put a cheap deterministic filter in front of every expensive model call — and then measure what it drops, because a dedupe stage that silently discards the input you needed is exactly the failure nobody notices.*

**Next action:** Rung 1. Ninety minutes, nothing installed, and it converts a claim this author never measured into a metric your own ingest path will emit on every run.
