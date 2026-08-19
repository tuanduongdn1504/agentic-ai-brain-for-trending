# (C) Needle 2 — Pilot Methods Menu

**Ship:** v246 · **Subject:** `cactus-compute/needle` · **Overall posture: READ-AND-BORROW.**

**The honest headline: the best things in this repository cost nothing to take and require installing
nothing.** The model itself is not a hireui component and probably never will be. Ranked
lowest-footprint first, in the vault's usual ladder form.

---

## M1 — ⭐ THE ZERO-INSTALL TAKE: run the `silent` grep on your own code (5 minutes)

```bash
grep -rni "silent" .
```

Run it on **hireui** and on the **vault's own `bin/`**. Every hit is a place where a past author noticed
a silent-wrong-answer mode. In Needle that grep returns the codebase's entire design doctrine in four
lines.

Then apply the doctrine where the grep returns *nothing*, which is the more interesting result. The rule
Needle follows, worth writing into `CLAUDE.md` verbatim:

> **Every failure mode that would produce a confident wrong answer must be converted into a loud one.
> Where it cannot be made loud, move the setting out of a runtime flag and into the artifact, so it
> cannot be set wrong.**

Needle's own three applications are worth reading as templates
(`needle/__init__.py:73-77`, `needle/model/export.py:29-31`, `needle/model/export.py:547-554`) — note
that each message states **cause, consequence, and remedy**, which is what separates them from an
ordinary exception.

**Risk: none.** **Value: high, and it compounds** — this is a rule, not a tool.

---

## M2 — ⭐ Steal the `llms.txt` form for hireui (30 minutes, zero install)

Needle's `llms.txt` (202 lines) is the strongest agent-facing API contract the corpus has read, and it is
strong for reasons that are **copyable without copying the content**:

1. It **states its own contract**: *"This file is written for AI coding assistants. It is enough to write
   correct Needle code without reading the source. **Copy the patterns; do not invent API that is not
   listed here.**"*
2. It has a **"Behaviour contract (important for correct code)"** section — not what the API *is*, but
   what an agent will get *wrong*: handle the empty case, do not read keys that may be absent, do not
   construct one instance per turn.
3. It has a **"Common mistakes to avoid"** section — the failure modes, listed as failures.

Write `hireui/llms.txt` with those three sections. The second and third are the ones that pay: they are
the file's answer to *"what will Claude Code do wrong in this repo?"*, which is a question the operator
can already answer from experience.

⚠️ **And copy the flaw as a warning, not a feature:** nothing keeps Needle's `llms.txt` in sync with its
code — it is one of three hand-maintained restatements of the same API (README, `llms.txt`,
`doc/apis.md`) with **no precedence statement and no CI check**. Apply **v245's D32** on the way in:
*declare which copy wins, inside the copy that loses.*

**Risk: none.** **Value: high** — directly on Goal #1, and it makes hireui more legible to the operator's
own agents.

---

## M3 — Adopt "facts, never instructions" as an injection-defence rule (zero install)

`llms.txt` — *"Pass environment state as **facts, never instructions**. Recognized keys: `date`, `locale`,
`device`, `battery`, `network`, `location`, `user`, `assistant`."*

Two ideas worth taking into hireui's LLM work, both consistent with the **RATIFIED candidate-LLM
legibility ADR**:

1. **Environment context enters through a fixed key vocabulary, not free prose.** An allow-list of fact
   keys is a structurally smaller attack surface than a system-prompt paragraph.
2. **Relative language resolves only when a fact licenses it** — *"'tomorrow at 7' resolves only when a
   `date:` fact licenses it."* Generalised: *the model may not infer a value that no supplied fact
   grounds.* That is the anti-fabrication rule the ADR already wants, stated as an input-contract.

⚠️ **In Needle this is a convention, not an enforced boundary** — the vault verified no sanitiser in the
Python; whatever enforcement exists is in the binary and is **NOT VERIFIED**. Take the design, not the
assurance.

**Risk: none.** **Value: moderate–high**, directly on the ADR.

---

## M4 — Borrow the confidence-gated escalation ladder as a *cost* pattern (design only)

```python
if calls and r["confidence"] >= 0.8:
    execute(calls[0])          # cheap local model acts
else:
    escalate_or_reask()        # expensive model, or a human
```

This is the shape the operator's live **claude-api-cost-optimization** thread has been circling: a cheap
model acts when it is confident and escalates when it is not. Needle supplies a clean statement of it.

🔴 **But take the shape and not the mechanism, for a specific and verified reason:** Needle's confidence
head **is not updated by fine-tuning**, and an agent built with `weights=` **reports `confidence` as
`None`** (`needle/__init__.py:57-60,122`). So the two headline features do not compose — *tune it for
your tools*, **or** *gate on calibrated confidence*, not both. Any escalation ladder the operator builds
must derive its own confidence signal (an LLM-judge score, a schema-validity check, a retrieval-support
check), **not** inherit one from a tuned model.

**Risk: none (design only).** **Value: high** — it converts a vague cost intuition into a testable gate.

---

## M5 — LOW-RISK SANDBOX TRIAL: `pip install cactus-needle` in a throwaway venv

The only pilot that installs anything. Worth doing **only** to answer one question the docs cannot:
*how good is a 45M model at structured extraction, really?*

**Fences — all of them, in order:**

1. **`/install-snapshot` first.** This package downloads and `dlopen`s a **native shared library**.
2. Fresh venv in a scratch directory. **Never** the vault, **never** the hireui tree.
3. Read `needle/agent/fetch.py` before running anything — know that first use pulls
   `cactus_needle-2.0.2-py3-none-<tag>.whl` from the HF repo `Cactus-Compute/needle2` and extracts
   `libneedle.*` from it. **Version-pinned; not hash-pinned; not signature-verified.**
4. **Synthetic inputs only.** Invented CVs, invented invoices.
5. **Do not set `OPENROUTER_API_KEY`.** Never run `generate-data` or `finetune --generate`.
6. Playground defaults to `127.0.0.1:7860` — **leave `--host` alone.**
7. Pin the version. Uninstall via the snapshot checklist when done.

**What to actually measure** (30 minutes, and it is a real experiment):

- Feed it 10 synthetic CV *fragments* against a Pydantic schema via `extract()`.
- Record: schema validity rate, field-level accuracy, **hallucinated-field rate** (the contract says
  unevidenced optional fields are omitted, not guessed — **test that claim**), and the confidence
  distribution on correct vs. incorrect extractions.
- That last one is the whole point: **is the confidence score actually discriminative?** If it is, the
  escalation ladder in M4 is real and can be built with any model. If it is not, M4 needs its own signal.

🔴 **Context budget — the binding constraint, and it is tighter than the README suggests.**
`architecture.py:597-611` derives the window from an **11.5 MiB byte budget**, not a token count. Run on
the actual named presets (`architecture.py:38-43`), that gives **480 tokens** for the `needle` preset and
**704** for `base` — while the README says *"256-token sliding window"* and the `256` that appears
throughout the API is `max_new_tokens`, the **output** cap. Which preset ships is **NOT VERIFIED**.

**At ~480 tokens of context, a CV does not fit — and neither does a large section of one.** Plan the
test around **single fields or short fragments** (one employment entry, one contact block), not
documents. If the operator's mental model was "cheap local CV parser," this number is the answer: **no.**

**Risk: low-moderate.** **Value: moderate** — it answers one real question and settles M4.

---

## 🔴 What the operator must NOT do

| Never | Why |
|---|---|
| Put **candidate data** through `needle generate-data` or `finetune --augment` | It POSTs your tool schemas **and your existing training examples** to **OpenRouter**, default model `deepseek/deepseek-v4-flash` (`finetune.py:56-66`, `cli.py:134,148`). That is third-party egress of whatever the data was derived from. |
| Ship the fetched engine in any **hireui** path | An unverified native binary loaded via `ctypes.CDLL` into a product process. **Version-pinned, not hash-pinned, not signed.** |
| Rely on `confidence` after fine-tuning | It is `None` by construction (`__init__.py:122`). The project says so in four places. |
| Let a Needle extraction touch a **candidate-facing decision** | The **RATIFIED candidate-LLM legibility ADR** requires fixed + legible + audited + human-in-the-loop + eval-gated. A 45M model with an in-binary grammar and no shipped eval harness satisfies none of it. |
| Cite its **benchmark** claims | *"trades wins with FunctionGemma 270M, LFM2.5 230M and Apple FM"* has **no in-repo data, no eval harness, no reproduction script** — only `assets/frontier.png`. |
| Cite the **HF download count** as usage | `_register_download()` force-downloads `config.json` on every engine fetch (`fetch.py:56-63`), so the counter includes the package's own traffic. |
| Assume the licence is settled | This repo is Apache-2.0; the engine's **source** repo is a custom licence with a **$2M funding / $2M revenue cap** that auto-terminates. **No document in either repo reconciles them.** For a commercial deployment this is a question for a lawyer, not a wiki. |
| Assume you know what it was trained on | **Nothing in the repository discloses it.** The only link to Gemini/Gemma is an **unversioned GitHub topic tag**. |

---

## Recommended order

**M1 → M2 → M3** in one sitting (~45 minutes, zero installs, all three land in `CLAUDE.md` or hireui as
durable rules). **M4** as a design note on the cost thread. **M5** only if the operator actually wants the
extraction-quality number — and behind every fence above.

**The single best thing here is M1.** A 45M tool-calling model for wearables is not going to change how
the operator works. A one-line grep that finds every place an author worried about a silent wrong answer —
and a written rule that says convert those into loud ones — will.
