# (C) Pilot Methods Menu — `mranex/translate-LN-pipeline` (v257)

**Headline verdict: READ-AND-RE-DERIVE. Install nothing, run nothing, copy nothing.**

The emphasis differs from v256. There the fence was AGPL — restrictive but *legible*: it tells you what you may do. Here there is **no licence at all**, which tells you that you may do **nothing**. Every rung below is therefore a **design** you re-derive from a paragraph, never a line you lift.

---

## The fences

| Fence | Why it binds |
|---|---|
| 🔴 **No licence — none, ever** | 0 of 88 tracked files match `licen\|copying\|notice`; no such file added in any of the 11 commits on any ref; 0 licence headers across all 47 `.py`; the README mentions licensing zero times. **GitHub's default is all rights reserved.** ⇒ You may read it. You may not copy, vendor, adapt or derive from it — not one function, not one prompt template. ⭐ **This is a harder fence than the sibling's AGPL, not a softer one**, and it is worth noticing that the same author licensed the sibling five and a half hours earlier on the same afternoon. |
| 🔴 **Command injection in the program the README tells you to launch** | `run.py:173` is `subprocess.Popen(cmd, shell=True, …)` where `cmd` is an f-string containing `get_vol()`, and `get_vol()` (`:135–137`) returns the **raw contents of a text-entry box**. A shell metacharacter typed into the Volume field executes. Do not run `python run.py`. |
| ⚠️ **Three generations, and the docs describe only one** | `python run.py` starts generation 1 (Tkinter, shells out to `src/`); the README describes generation 3 (PyQt6), reachable only via `run.bat`. If you explore this tree expecting the README's program, you will be reading the wrong code. |
| ⚠️ **No CI, no tests, ever** | Zero `.yml`/`.yaml` on any ref; no test file anywhere. Nothing here has been verified by anything but its author's own use. |

**Can the operator run it?** Generation 3 probably would start on macOS — PyQt6 is cross-platform and `python -m manual_studio.qt_app` has no Windows-specific import — but there is no reason to. Nothing in the pilot requires execution, and the only documented entry point is both Windows-shaped and pointed at the wrong generation.

---

## Rung 0 — 25 minutes, read only

1. ⭐ **`Screenshot/Prompt_studio.PNG`** — open the image first. Ninety seconds, and you see the whole architecture: a rendered prompt on the left, a paste box on the right captioned *"paste the AI's JSON response here"*, and three buttons — **Check Syntax**, **Import**, **Clear**. The product is visible in one picture.
2. **The prompt visible in that screenshot.** It is the best-engineered artifact in the repository: a role line, injected genre, explicit scope fences (*do NOT translate; do NOT merge relationship data here; do NOT overwrite existing canon*), a **precedence rule** (existing canon outranks new chapter-level guesses), a **conflict protocol** — mark contradictions as conflicts rather than overwrite — and two-tier status semantics that tell the model *how a downstream model will consume the field*.
3. **`prompts/03_build_segment_glossary.txt:11`** — one line, and it is the pattern worth taking (Rung 1): *if an important term is in the segment but not in the volume glossary, put it in `missing_glossary_candidates` for human review.*
4. **`manual_studio/core/review_flags.py`** (139 lines) — the other half of that loop, and the only complete one in the repository.
5. ⭐ **The three thresholds, in this order:** `config/config.json` (0.72 / 0.82, plus four `force_review_if_*` conditions) → `manual_workflow.py:117-118` (0.72 / 0.82, injected **into the prompt**) → `review_flags.py:101` (**0.8**, what the app enforces). Then note that nothing reads the config file and the four conditions exist in no Python file. **This is the lesson of the ship and it takes four minutes to see.**
6. **`Screenshot/Editor.PNG`** — the glossary schema in the raw-JSON panel: every entry carries `source_items` and `appears_in`. **Each canon entry records where it came from.**

---

## Rung 1 — 2 hours, the main asset: hireui's review-routing policy

**What this buys:** the ratified candidate-LLM legibility ADR requires a human in the loop with defined escalation. It has no implementation. This subject contains a *shape* for that — declared, partly built, and instructively broken — and re-deriving it is a two-hour desk job with no code to copy.

### 1a — Take the loop that actually closes, not the one that doesn't

The subject has four escalation mechanisms. **Exactly one works**, and it is the cheapest:

> **Ask the model to nominate its own gaps into a named field, then have code read exactly that field.**

`prompts/03` asks for `missing_glossary_candidates`; `review_flags.py` reads `missing_glossary_candidates`; the UI shows the flag. Prompt, schema and gate agree on one string, so the loop runs from the model's own uncertainty to a human's screen.

The confidence-threshold mechanism, by contrast, is declared three times at two values and enforced at a third — and its four best conditions are implemented nowhere.

⭐ **The rule for hireui: prefer a named-field admission over a numeric threshold.** A model saying *"I could not resolve this employer"* into `unresolved_entities[]` is checkable, greppable, and testable. A confidence score requires you to pick a number, agree on it in three places, and keep them in sync — which this repository demonstrates you will not.

### 1b — The forced-review conditions, translated to hiring

The subject's four `force_review_if_*` conditions are the most valuable thing in its config file and exist in none of its code. They translate almost directly, because they are all the same shape: **escalate when the extraction could not be anchored to a known entity.**

| Subject's condition | hireui equivalent — force human review when… |
|---|---|
| `force_review_if_unknown_speaker` | the employer or institution named in a role cannot be resolved against the known-organisation list |
| `force_review_if_unknown_listener` | a role's dates cannot be resolved into a bounded range (open-ended, missing, or contradictory) |
| `force_review_if_multiple_possible_speakers` | a field has more than one candidate value — two employers overlapping one date range, two spellings of one name |
| `force_review_if_no_matching_pronoun_rule` | an extracted job title or skill matches **no** entry in the taxonomy, i.e. the model invented a category |

Add the two this domain does not need and hiring does: **force review when a protected characteristic could be inferred from the extracted text**, and **force review when the candidate's own words were paraphrased rather than quoted** (the ADR's legibility clause).

### 1c — Write the threshold once, and derive

⭐ **The single most transferable defect in this ship.** Put the numbers in **one** place — the code that enforces them — and derive every other appearance from it: the value injected into the prompt, the value shown in the UI, the value in any config. If a number must appear in a prompt, interpolate it from the enforcing constant rather than typing it.

Then **assert it**, in the manner of v254's *assert a count against a count*: a test that renders the prompt and greps the rendered text for the enforced threshold value. That single test would have caught this subject's entire §4 defect, and it is four lines.

**Deliverable for Rung 1:** a section in `hireui/evals/METHOD.md` — the named-field admission pattern, the six forced-review conditions, and the write-once-derive rule — plus the four-line assertion test. Nothing installed; nothing copied.

---

## Rung 2 — 90 minutes, optional but genuinely interesting: the Active Volume Canon

The subject's persistent canon can grow to thousands of entries across a long series, and stuffing all of it into every prompt would be ruinous. Its answer: **scan the current unit's source text and include only the entities that actually appear in it.** The README claims this saves up to 80% of token cost.

⚠️ **Do not cite that number.** It appears at `README.md:119` and nowhere else in the repository — no benchmark, no measurement, searched across all 47 `.py`, all 14 `.txt` and the README. The mechanism is sound; the figure is unsupported.

**Two places it maps:**

1. **hireui matching.** Before prompting about a candidate, filter the skill/title ontology to the terms actually present in that candidate's document. Cheaper, and it also removes the ontology entries most likely to seduce the model into inventing a match that isn't there.
2. ⭐ **The vault's own context budget.** This is retrieval-by-presence rather than retrieval-by-embedding: no vector store, no similarity threshold, just *is this term in the text in front of me*. That is the same idea as the tool-catalog problem the vault has been circling since v238 — and it is far simpler than the alternatives already considered.

⚠️ **The failure mode to design around, which the subject does not appear to handle:** an entity referred to **only by pronoun or by an alias not yet in the canon** is absent from the scan and therefore dropped from the prompt — so the model loses exactly the context it most needed. If you adopt this, **include an entity when any of its aliases match, and keep a floor set that is always included.**

---

## Rung 3 — DECLINED

There is no rung that installs or runs this. The prompts cannot be copied (no licence), the code cannot be vendored (no licence), and the product solves a problem the operator does not have. For document extraction the better-aimed corpus sources remain **v217 wardrobe** (vision → confidence-scored JSON → anti-fabrication → QA gate) and **v256**'s five-layer alignment guard, which — note — is the same author's *other* repository and is materially better on exactly the axis this one lacks.

---

## 🔴 NEVER

- **Copy, vendor, adapt or re-license any part of this repository.** There is no licence. Read and re-derive only.
- **Run `python run.py`** — that is generation 1, and it interpolates a text field into a `shell=True` command.
- **Cite the "80% token saving."** One README line, no measurement anywhere.
- **Trust the `"status"` field as evidence of anything.** In the generation that ships, `artifact_store.py:25` writes the literal `"success"` on every row; the only code that can write `"failed"` belongs to a generation the README does not document. Two release gates read that field and therefore cannot fire.
- **Trust "Check Syntax" as content validation.** It verifies that the response parses to a JSON object — nothing about item counts, ids, or ordering. There is **no** request/response alignment validation in any of the 47 files. (⭐ To be fair to the subject: the button says *syntax*, and the README says *syntax*. It is a gap, not a lie.)
- **Assume the README's file references are right.** It attributes the `.bak` backup mechanism to `manual_studio/core/workspace.py`; the function is in `jsonio.py`. Three of my own near-misses this ship came from believing a documented location.
- **Rely on the `.bak` files as crash protection.** `jsonio.write_json` is a plain `path.write_text` — no temp-file-and-rename, so it is not crash-atomic, whatever the README says about losing power.
- **Expect the per-project prompt override to work as documented.** `prompts_root` selects a *directory*, not a *file*, and `load_prompt` has no fallback — overriding one template appears to require copying all thirteen.

---

## The one sentence

⭐ *Prefer a model that admits its gaps into a named field over a model you score and threshold — the named field is the only escalation loop in this repository that actually closes.*

**Next action:** Rung 1. Two hours, nothing installed, nothing copied, and it turns a policy this author declared three times and enforced at none of them into the one hireui's ADR has been missing.
