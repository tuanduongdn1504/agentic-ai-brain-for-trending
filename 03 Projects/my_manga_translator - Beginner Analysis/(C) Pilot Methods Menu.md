# (C) Pilot Methods Menu — `mranex/my_manga_translator` (v256)

**Headline verdict: READ-AND-BORROW. Install nothing. Run nothing.**

Not because it is dangerous — §11 of the Deep Dive shows it is the best-behaved subject of the last dozen ships on secrets, egress and shell handling — but because **there is nothing here the operator needs to execute, one genuinely valuable design to copy by hand, and four hard fences.**

---

## The fences, first

| Fence | Why it binds |
|---|---|
🔴 **AGPL-3.0** | The repository is AGPL-3.0. hireui is a commercial product. Do not vendor, copy or derive code from this repository into it. **Read it and re-implement from the design, not the source.** Everything in Rung 1 below is a *design*, expressible in a paragraph, and none of it needs a line of this code. |
🔴 **The fonts** | 9.2MB of `fonts/` carries Monotype's Arial ("Any other use is prohibited"), two Blambot fonts marked "All rights reserved", a Comicraft font carrying a **MyFonts `wfkit2` webfont-kit order slug**, a font whose internal family name is literally **"DEMO"**, and at least one fan-modified derivative. **Zero open-font-licence strings across all 24 files; no attribution file has ever existed.** Do not redistribute this directory, and do not treat the pack as a source of fonts for anything. |
🔴 **The documented install cannot succeed** | `pip install -r requirements.txt` has two hard contradictions against PyPI's own published metadata: `transformers==4.57.3` requires `huggingface-hub<1.0,>=0.34.0` (file pins `0.22.2`) and `safetensors>=0.4.3` (file pins `0.4.2`). Do not spend an afternoon fighting it. |
⚠️ **Google Lens ToS** | The Chrome Lens OCR provider drives Google's undocumented consumer *crupload* endpoint. The README itself warns of rate limits and temporary IP bans. **Never point this at a batch of candidate documents** — separately from ToS, it would send candidate PII to a consumer Google endpoint. |

⚠️ **And one module cannot even be imported.** `detectors/comic_text_detector.py:9` imports `assign_text_regions_to_bubbles` from `detectors/matching.py`, which has not defined it since `2aebd41 "Remove CTD"` on 2026-05-17 — so that module raises `ImportError` on load. It is latent (nothing imports it), but if you go exploring `detectors/`, that is the file that will stop you, and it is not your environment's fault.

**Can the operator even run it?** Effectively no, as shipped. The launcher is `PyQt_run.bat` (Windows); `servers/paddleocr_vl/run_server.bat` hardcodes `C:\Nghich\Manga-Translator\...` four times and cannot work on any other machine; `mmt_core/llama_server.py:221` tries to run that `.bat` with `sh`. `python -m mmt_gui.main` is documented and PyQt6 is cross-platform, so the GUI would probably *start* on macOS — but every OCR provider needs a local `llama-server` plus GGUF weights, and the two resolvable pins block the install anyway. **This is the first ship since v255 where "no code executed" is the correct decision rather than an omission** — and unlike v250–v254, it is stated as a decision, with the reason.

---

## Rung 0 — 25 minutes, read only, zero setup

Read these six things in this order. This is the whole intellectual payload.

1. **`mmt_core/prompt_studio.py:31–36`** — the five-line output contract (*preserve every page key; preserve item count; preserve item order; do not merge, split, drop or invent; no commentary outside the structured result*). Ninety seconds, and it is the best-written thing in the repository.
2. **`translator/openai_compatible_translator.py:344–396`** — the validation that actually enforces it, including the **per-item index check** (`"response item index mismatch at position {expected_index}"`), which is the part almost everybody omits.
3. **`translator/deepseek_translator.py:450`** — the recovery policy in one comment: *"If response length mismatches, pad/truncate with originals."* Untranslated-but-aligned beats translated-but-shifted.
4. **`mmt_core/detection_edit.py:29` + `ocr_edit.py:23` + `render_edit.py:29`** — three literal `DOWNSTREAM_STALE_STAGES` lists, then `grep -rn downstream_stale` to see that it is written into the cached JSON, surfaced to the user, and **never enforced** — and then the README's troubleshooting §5, which says so in prose. **The check and its claim match.** That is the ship's lesson.
5. **`mmt_core/ocr_text_filter.py`** — a 263-line taxonomy of one model's hallucination modes, each rejection carrying a named reason (`structured_markup_non_text`, `coordinate_geometry_non_text`, …), scoped honestly to the single provider it was written against. Then `git log -1 --format=%s 2f8a363` for the commit message that produced it.
6. ⭐ **`git show bdcb098:.jules/bolt.md`** — three lines of a deleted AI agent's memory file, whose prescribed fix is still running at `translator/translator.py:43`. **Read it, then read that line.** Nine seconds; it is the most important thing here for the vault's own practice.

---

## Rung 1 — 90 minutes, the only lasting asset: the segment-alignment guard for hireui

**This is the reason to have read this repository.** It discharges a clause of the ratified candidate-LLM legibility ADR that still has no implementation.

**The problem, in hireui's terms.** You send N extracted regions of a CV — or N candidates, or N job requirements — to a model in one request, and you get back a list. If that list is shifted by one, merged two entries, or silently dropped an empty one, **every subsequent item is attributed to the wrong person or the wrong role, and nothing throws.** A shifted list is the single most dangerous failure in LLM-based structured extraction because the output is well-formed, plausible, and wrong. It is also the failure mode most likely to survive a demo and reach a hiring decision.

**The five-layer guard to write into `hireui/evals/METHOD.md` and the extraction path.** Re-implement, do not copy (AGPL):

1. **Send indices, not just text.** Every item in the request carries a stable id. The subject uses `indexed_texts` — `[(index, text), …]`.
2. **Assert the count inside the prompt.** Interpolate the number: *the array must contain exactly N items* (`gemini_translator.py:373`). A contract the model can read is cheaper than a retry.
3. **State the five prohibitions verbatim.** Preserve keys, preserve count, preserve order, do not merge/split/drop/invent, no commentary outside the structure. Lift the shape from `prompt_studio.py:31–36`.
4. **Validate twice: length, then per-item index.** A length check passes a swap. `raise` on the first index that does not match its expected position, and name the position in the error.
5. **On mismatch, fall back to the source, never to a guess.** Pad or truncate with the *original* values so that alignment is preserved and the failure is visible as untranslated/unextracted text rather than as someone else's data.

⭐ **And the reason layer 4 is load-bearing, which is worth writing down next to the code:** the reconciliation is a `zip()`, and **Python's `zip` silently truncates to the shorter sequence.** In the subject, the length check sits three lines above the `zip` for exactly that reason (`context_memory.py:91` guarding `:94`). Remove the guard and the misalignment becomes invisible. Put that sentence in the comment — this ship's other lesson is that **the reason is the part that gets deleted.**

**Because the licence forbids copying the source, here is the whole guard as pseudocode — write it from this, not from their file.** This is the distillation, not a transcription: their implementation is ~50 lines of nested conditionals specific to manga pages, and none of that shape is needed.

```
send(items):                       # items = [(id, text), ...] — ids are stable and OURS
    request = { "count": len(items),
                "items": [ {"id": i, "text": t} for (i, t) in items ] }
    prompt  = CONTRACT + f'The "results" array must contain exactly {len(items)} objects.'
    return model(prompt, request)

CONTRACT = """Preserve every id exactly as provided.
Preserve item count exactly.  Preserve item order exactly.
Do not merge, split, drop, or invent items.
Return only the structured result — no prose, no markdown, no commentary."""

receive(response, items):
    results = parse_or_fail(response)                  # a parse error is a failure, not a warning

    if len(results) != len(items):                     # LAYER 1: the count
        log(FAILURE, expected=len(items), got=len(results))
        return realign_from_source(results, items)     # never guess

    for position, (result, (id, text)) in enumerate(zip(results, items)):
        if result.id != id:                            # LAYER 2: the identity, per item
            raise AlignmentError(
                f"item id mismatch at position {position}: sent {id!r}, got {result.id!r}")
            # a count check passes a SWAP; this does not.
            # NOTE: zip() truncates to the shorter sequence — the length check above
            #       is what makes this loop safe. Do not remove it.

    return results

realign_from_source(results, items):
    # Alignment is worth more than completeness. Pad or truncate to the ORIGINAL
    # length and fill any hole with the SOURCE text, flagged unprocessed.
    # Untranslated-but-correctly-placed beats translated-but-shifted:
    # the first is visible to a reviewer, the second is invisible and wrong.
    out = []
    for position, (id, text) in enumerate(items):
        r = results[position] if position < len(results) else None
        out.append(r if (r and r.id == id) else Unprocessed(id=id, text=text))
    return out
```

**The test that makes it an eval gate** — and the reason this rung is worth doing at all: take any real model response and mutate it four ways — **drop one item, duplicate one, reorder two, renumber one id** — and assert the guard fires on each. That is a real gate for a hiring-adjacent LLM path, and **it needs no ground-truth corpus**, which is exactly what has kept the ADR's eval clause unimplemented.

**Deliverable:** one section in `hireui/evals/METHOD.md`, plus the guard in the extraction path and a test that feeds the model's response through a mutator (drop one, duplicate one, reorder two) and asserts the guard fires each time. **That test is the eval gate the ADR asks for, and it needs no ground-truth corpus** — which is what has been blocking it.

---

## Rung 2 — 60 minutes, optional: the staged-artifact legibility pattern

Borrow the *shape* of `DOWNSTREAM_STALE_STAGES` for any hireui pipeline where a human corrects an intermediate result (a parsed CV field, a match explanation, a screening note):

- Persist the staleness **in the artifact**, as a list of named downstream steps — not in memory, and **not as an `mtime` comparison** (v244 **D29**: `mtime` is not drift).
- **Surface it to the human** who is already in the loop.
- **Do not enforce it** unless you intend to, **and do not claim to.** v250 called six rules "non-negotiable" and gated one; v252 headed a block "Automated, Zero Tolerance" and automated nothing. This subject's mark is unenforced and its README says so — which is why it is the honest one.
- ⚠️ **But fix the flaw the subject has:** it declares the stage DAG four or more times (three literal lists plus the GUI ordering) with **nothing reconciling them**, and the three lists do not even share a convention. If you adopt the pattern, **derive the downstream set from one declared DAG** and assert it — the v240 inventory rule, and v254's *assert a count against a count*.

---

## Rung 3 — DECLINED, and why

There is no rung that installs or runs this software. The OCR pipeline is not a better CV parser than what hireui will build: it is tuned for speech bubbles in vertical CJK, its three providers are two local `llama.cpp` servers and a consumer Google endpoint, and the vision-LLM path the README advertises **does not exist** (`OCRConfig` has no `api_key` field — §6). For document extraction the operator already has the better-aimed source in **v217 wardrobe** (the vision→confidence-scored-JSON→anti-fabrication→QA-gate template) and **v211 PixelRAG** for the screenshot-vs-OCR question. **This subject's contribution is the alignment guard, and that is a paragraph, not an installation.**

---

## 🔴 NEVER

- Vendor, copy or adapt any code from this repository into hireui (**AGPL-3.0**).
- Redistribute or reuse `fonts/` (Monotype Arial, two Blambot faces, a Comicraft MyFonts webfont kit, a "DEMO" font, fan-modified derivatives, zero open licences, no attribution).
- Run `pip install -r requirements.txt` expecting it to resolve — two pins are unsatisfiable, and ten of twenty-four requirements are imported by zero files, including a Flask/Werkzeug/gunicorn stack that is pure vulnerable dead weight.
- Point the Chrome Lens provider at candidate documents (ToS **and** PII to a consumer Google endpoint).
- Load models with the pinned `transformers==4.57.3` — the four `from_pretrained` sites are exactly the path in **`CVE-2026-4372` / `PYSEC-2026-2290`**, unfixed until 5.3.0.
- Cite this subject's model recommendations or VRAM figures as measurements. They are one enthusiast's opinions, written in the second person, with no benchmark anywhere in the repository.
- Repeat the README's OCR menu as a feature list. **"Online LLM (Claude, GPT, Gemini)" is not implemented**, and the config object structurally cannot authenticate to any of them.
- Treat `translator/test_translator.py` as a test suite. It asserts exact string equality against four live network services, `pytest` is not in `requirements.txt`, and the project's own `.gitignore:49` (`test_*.py`) excludes it.

---

## The one sentence

⭐ *An unenforced check is a defect only when something claims it is enforced — and the check most likely to survive is the one whose reason was written down beside it.*

**Next action:** do Rung 1. It is ninety minutes, it needs nothing installed, it closes an open clause of a ratified ADR, and the test it produces is the first eval gate in hireui that does not require a ground-truth corpus to be useful.
