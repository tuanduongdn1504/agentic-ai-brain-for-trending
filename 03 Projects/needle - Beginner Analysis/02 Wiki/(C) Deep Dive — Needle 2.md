# (C) Deep Dive — Needle 2 (`cactus-compute/needle`)

**Wiki v246** · 2026-08-19 · GOAL-ALIGNED INCLUDE 3/4 · **NO MINT** · counts 46/11 unchanged
**Source-cloned twice** — tree at HEAD `f7b64256` (2026-08-18) + a blobless full history.

---

## What it is

A **45M-parameter foundation model for tool calling, device use and structured extraction**. The whole
model is a **14MB binary** running a full session in about **28MB of RAM**. Text goes in; a JSON tool call
comes back. Apache-2.0. `pip install cactus-needle`. Page-stated 7.6k★ / 487 forks.

The repository is *not* the model. It is the **Python package around it**: inference bindings, a JAX
reference implementation, a LoRA fine-tuning pipeline, a quantizing exporter, and a browser playground —
**44 files, 10,824 lines.** The model's weights and its actual inference engine live elsewhere.

That gap is where most of this ship's findings are.

---

## 1. The headline: an Apache-2.0 repository that runs a revenue-capped engine, and says nothing about it

`pip install cactus-needle`, then `Needle(...)`. On first use, `needle/__init__.py:13-28` finds no cached
library and calls `fetch_library()`, which downloads
`python/cactus_needle-2.0.2-py3-none-<platform>.whl` from the **Hugging Face model repo**
`Cactus-Compute/needle2`, unzips **`libneedle.dylib`/`.so`/`.dll`** out of it, and
`ctypes.CDLL`s it into your process (`needle/agent/fetch.py:88-102`, `needle/__init__.py:38`).

Three licences are now in play:

| Artifact | Licence |
|---|---|
| `cactus-compute/needle` — this repo | **Apache-2.0** (changed **MIT → Apache-2.0** on 2026-08-17, `b188e110`, two days before HEAD) |
| `huggingface.co/Cactus-Compute/needle2` — where the binary comes from | declares **apache-2.0** |
| `cactus-compute/cactus` — the C++ engine **source**, 5.9k★, updated 2026-08-17 | **custom licence**; GitHub reports **"Other"** |

That third licence permits free use only by organisations with **under $2,000,000 in total funding *and*
under $2,000,000 in gross annual revenue**. Cross either threshold and permission **automatically
terminates**, with a commercial licence required within **thirty days**.

**What the needle repository says about any of this: nothing.**
`grep -rn -iE "cactus-compute/cactus|commercial licen|proprietar|funding|revenue|dual.?licen"` across all
44 files returns **zero hits**.

⚠️ **This is not concealment, and the wiki says so plainly.** The engine repo is public, prominently
linked from the organisation's page, and its licence is a plain-text file anyone can read. The HF repo
the binary is actually fetched from declares apache-2.0.

**The sufficient claim is narrower and it is enough:** a developer reading `cactus-compute/needle` sees
Apache-2.0, installs the package, and loads a native engine into their process — and **no document in
either repository reconciles the two declarations or states which one governs that binary.** For a
hobbyist this is noise. For anyone deploying commercially it is a question that the repository is not
able to answer.

> ⭐ **Against v244 and v245 this completes a matched set of three.**
> **v244 OpenSandbox** *over*-asserted an identity: CI refused any PR whose files omitted
> `Copyright … Alibaba`, while `GOVERNANCE.md` named Alibaba zero times.
> **v245 Unsloth** *under*-asserted one: metadata declared `Apache-2.0` while the wheel shipped a
> uniformly AGPL CLI.
> **v246 Needle** *splits* one across two repositories, and the restrictive half is the half you execute.
> **Three consecutive ships in which the licence stated in prose does not describe the artifact that
> runs — and in all three, the enforced or executed artifact is the honest one.**

---

## 2. The best idea in the repository is one grep

```bash
grep -rni "silent" .
```

Four hits. Three are the same instinct:

- **`needle/__init__.py:73-77`** — the engine is a process-global singleton that cannot unload weights.
  Constructing a base-model agent after a tuned one therefore raises, *"so this agent would **silently**
  answer with those weights; construct agents that want the base model before any tuned one, or run them
  in separate processes."*
- **`needle/model/export.py:29-31`** — `kv_window` and `kv_bits` are baked into the `.cact` header rather
  than exposed as runtime flags, because *"a model quantized for one must be RUN at it — leaving either
  to a runtime flag **silently** [corrupts]."*
- **`needle/model/export.py:547-554`** — refuses an export that *"would **silently** ship plain W4 —
  numerics it was never post-trained for."*

Three more in the same spirit: a `warnings.warn` at construction when `weights=` is passed
(`__init__.py:57-60`), the same disclosure printed at the end of every fine-tune run
(`finetune.py:401`), and an unparseable-envelope error that says *"this is an engine bug — please report
it with the prompt and schema"* (`__init__.py:92-96`).

**The doctrine:** *every failure mode that would produce a confident wrong answer is converted into a
loud one; where it cannot be made loud, the setting is moved out of a runtime flag and into the artifact
so it cannot be set wrong.*

Note what these messages have that ordinary exceptions do not: each states the **cause**, the
**consequence**, and the **remedy**.

**The fourth hit is a counter-example, and it is what keeps this honest.**
`doc/finetuning.md:19` — *"longer examples are **silently truncated**."* A silent data-loss path,
documented in prose, with no warning emitted. So the doctrine is real but not total: three places
convert a silence into a noise; the fourth admits one and leaves it.

⭐ **And the grep is portable.** Run it on any codebase to find every place its author thought about
silent corruption. Cost: one command.

---

## 3. The irony: the doctrine is not applied to their own release gate

`.github/workflows/release.yaml` is a **daily automated release train** — cron at 16:00 and 17:00 UTC with
a DST guard selecting 09:00 Pacific, auto-bumping the patch version, building, `twine check`-ing,
publishing to PyPI, and pushing a tag. **No human between a merge to `main` and a public release.**

It is verifiably real: PyPI shows **7 releases, 2.0.0 → 2.0.6, 2026-08-10 → 2026-08-17** — one per day.

Much of it is genuinely good practice: top-level `permissions: contents: read`, escalated only in the
release job; `id-token: write` with `pypa/gh-action-pypi-publish` = **PyPI Trusted Publishing (OIDC)**, so
no long-lived token; and version discovery via `git tag --list 'v*' --sort=-v:refname`, a **correct
version sort**. (Worth naming: the naive `git tag | tail` sorts *lexically* — the exact error the vault's
own v245 ship made. This project got it right.)

**🔴 But look at the gate.** It is `pytest -q -m "not slow"` on a fresh `ubuntu-latest`:

| File | Tests | In CI |
|---|---|---|
| `tests/test_inference.py` | 5 | **SKIPPED** — `pytestmark = requires_engine`; `conftest.py:20` skips when no engine is cached, and a fresh runner has none |
| `tests/test_build.py` | 3 | **DESELECTED** — `pytest.mark.slow` |
| `tests/test_finetune.py` | 2 | **DESELECTED** — `pytest.mark.slow` |
| six other files | 35 | run — but `test_weights.py:33-38` monkeypatches `_lib` with a **stub** |

**Every test that exercises the shipped inference engine is either deselected as slow or skipped for a
missing engine — and `pytest` reports skips as success.** The daily automated publish to PyPI is gated on
a suite that **cannot fail for an engine regression.**

The most silent-failure-conscious codebase in the corpus ships behind a silent pass.

---

## 4. Where the interesting machinery actually is: not here

`needle/__init__.py:38-48` binds exactly **four** C symbols — `needle_init`, `needle_complete`,
`needle_reset`, `needle_load`. Everything the marketing is about lives behind them:

- **Tool retrieval.** *"With more than 5 declared tools, a built-in retrieval head renders only the top-5
  per turn and constrains the grammar to that subset."* Python's entire contribution is passing
  `tool_index_path` through `needle_init` (`__init__.py:64, 89`). **The "5" is not in this repository.**
- **The byte-level grammar** compiled from your schemas. In the binary.
- **Confidence at inference.** The JAX side has a `ConfidenceHead` (`architecture.py:463-488`) and exports
  it (`export.py:289`), but the score you read comes from the binary's JSON envelope.

The JAX code here is the **training, export and reference** side. The **inference** side is the blob.

**⇒ This governs the mint decision.** v242's **D25** — *an un-cloned subject's caveats are hearsay* —
applies to a component rather than a subject: the vault has verified that the tool-retrieval claim
**exists in documentation**, not that it works. There is no benchmark data, no eval harness and no
reproduction script anywhere in the repository.

---

## 5. Three claims the code does not support

**The context window.** README line 13 claims *"a 256-token sliding window with the tools pinned as KV
sinks."* The code computes something else: `architecture.py:597-611` derives the window from an
**11.5 MiB byte budget** (`KV_BUDGET_BYTES = 11*1024*1024 + 512*1024`), floors it at 160, and clamps to
`max_seq_len`. Run that arithmetic on the actual named presets (`architecture.py:38-43`):

| Config | geometry | **effective KV window** |
|---|---|---|
| **`needle` preset** | d_model 768 · 12 heads · 6 kv-heads · **27 layers** | **480 tokens** |
| `base` preset | d_model 512 · 8 heads · 4 kv-heads · **27 layers** | **704 tokens** |

Meanwhile the `256` that appears all over the API — `complete`, `run`, `extract` — is
**`max_new_tokens`, the output cap** (`__init__.py:109,125,147,165`). The README appears to have collided
the two. ⚠️ Which preset the distributed 14MB model is, is **NOT VERIFIED** — `export.py:20-30` shows
`kv_window` rides inside the `.cact` header, so the deployed geometry is authoritative and is not in this
repo.

**The surviving claim: the real bound is a byte budget, not a token count — and for the `needle` preset
it is ~480, roughly double the documented figure.** Either way it is small enough that the practical
consequence is the same one the pilot has to live with: **a whole document does not fit.**

**The quantization.** README line 5: *"compressed to **CQ2-bit** with Cactus Quants."* `export.py:5-7`:
*"Format is **W4A8**: the matmul weights … are Cactus-Quants **INT4**; norms, Hadamard diagonals, and
gates stay FP16."* `cli.py:156`: `--bits` accepts `2` or `4`, defaulting to `None` → 4. The two numbers
describe different artifacts — the distributed model versus what `needle build` emits — and no document
says so.

**The paper.** README line 23 cites **arXiv:2607.18363** for *"our Simple Attention Network findings."*
The paper is real and shares the author list — but it is titled **"A Controlled Study of Attention-Only
Transformers"**, and its reported result is that removing feed-forward layers **incurs a performance
cost**, substantially but not fully recovered by reallocating capacity to attention depth, with the
residual gap concentrated on *tasks requiring knowledge retrieval from weights rather than context*.
⚠️ Precision matters here: the paper studies *attention-only* stacks, while Needle uses a **Hadamard MLP
in place of** the FFN; whether the ablations cover that variant is **NOT VERIFIED**. The defensible
statement is narrow — *the citation supports the architecture less enthusiastically than the README's
framing implies.*

---

## 6. 🔴 The training provenance lives in a GitHub topic tag

The README explains the architecture down to the update rule: Walsh-Hadamard transforms, Sinkhorn
iteration, engram sites firing at two layers, sandwich-normed gated residuals. It says **nothing about
what the base model was trained on.**

`grep -rn -iE "distil|teacher|trained on|gemini|gemma"` across the whole tree: **zero** hits for the base
model. Every "dataset" reference is about *your* fine-tuning JSONL. The words *gemini* and *gemma* appear
**nowhere in the repository.**

The repository's **GitHub topics** are: `cactus`, **`gemini`**, **`gemma`**, `llm`, `on-device-ai`. And
third-party coverage describes Needle as *"a 26M-parameter model distilled from Gemini 3.1"* — a
secondary-source claim the project does not make anywhere.

**The only thing in the entire project connecting Needle to Gemini is a topic tag** — the one piece of
metadata that is not in the git tree, not versioned, and invisible to anyone who clones the repo.

⚠️ Distillation from a frontier model is ordinary and may be fully licensed; this is **not** an
accusation. The checkable point is narrower: **the training provenance of a model marketed for commercial
on-device deployment cannot be established from its repository.**

⭐ Note the exact inversion of **v244**, where the affiliation lived in 1,674 CI-enforced file headers
while the governance document named it zero times. **Both projects put a load-bearing identity fact in
the one place their own tooling does not check.**

---

## 7. Also true: a 26m/45M disagreement between two live repos

`cactus-compute/needle` (README, `llms.txt`, the BibTeX title) and the HF model card all say **45M**.
`cactus-compute/cactus` — the same organisation's engine repo, **updated 2026-08-17** — says *"Needle is a
**26m** parameter model for on-device tool calling"* and points users at `Cactus-Compute/needle`, not
`needle2`.

Almost certainly Needle 1 versus Needle 2. **Neither repository says so**, and nothing disambiguates the
two HF repos.

---

## 8. What is genuinely good here

**The behaviour contract.** `llms.txt` is the strongest agent-facing API document the corpus has read, and
its strength is in what it refuses: *"Copy the patterns; do not invent API that is not listed here."* It
carries a **"Behaviour contract (important for correct code)"** section and a **"Common mistakes to
avoid"** section — i.e. it documents the *failure modes* an agent will hit, not just the API surface.
A clean instance-strengthening of Library-vocab **#12 "LLM-routing artifacts"** (CONFIRMED, N=5+).

**The refusal design.** Off-topic input returns an **empty `function_calls` list** — there is no free-text
fallback, and *"the answer is the tool results, no free text is generated."* Combined with a byte-level
grammar that makes every emitted call schema-valid by construction, the result is a model that is
**structurally unable to produce fluent prose about something it does not know.** For a class of
extraction problems that is a better safety property than any amount of prompt engineering. ⚠️ The
adjacent claim — *"arguments contain only values evidenced in the input; optional fields with no evidence
are omitted, not guessed"* — is a **training-time property asserted in prose**, not something enforced in
code. Test it; do not assume it.

**Honest-deficiency disclosure (#83), in four places.** Fine-tuning does not update the confidence head,
so an agent built with `weights=` reports `confidence` as `None`. The project says this in `llms.txt`, in
`doc/apis.md`, in a **runtime `warnings.warn`** at construction, and in the **fine-tune job's own
stdout**. It is a disclosure that the product's two headline features **do not compose** — tune it for
your tools, *or* gate on calibrated confidence, not both — delivered at the moment of the mistake.
A second instance: `doc/finetuning.md:64` states that the shipped `--epochs` default of 3 *"barely moves
a rank 16 adapter"* and tells you to use 10–30.

**Security posture.** The playground defaults to **`127.0.0.1`** (`cli.py:174`), has no CORS handling at
all, and calls `complete()` rather than `run()` — so it shows the proposed tool call without executing
user Python. **No broken-auth triad** (contrast v231/v232), and per v245's **D33** the absent auth is
minor on loopback with no credential held.

---

## 9. The corpus contribution: the tool-catalogue thread reaches the model layer

Every prior corpus treatment of tool-schema bloat has been at the **harness** layer:

- **v167 audit** — the vault's own **~54K tool-catalogue floor**, named as a standing constraint.
- **v238 dsh-anchored-standard** — a preset blanking auto-injections; Anthropic ships the mechanism
  first-party as `defer_loading` (77K → 8.7K on request #1).
- **v245 Unsloth** — **measured** it (*"~28k tokens of which ~18k is System tools"*) and named `--tools`
  as the flag that restricts schemas.

**Needle 2 is the first subject in the corpus to move the problem into the weights.** A learned retrieval
head selects the top-5 tools from a large declared catalogue per turn, and the grammar is then constrained
to that subset — so the catalogue never has to fit in the prompt at all.

⇒ **The thread reaches N=4 and, for the first time, spans two layers.** Three harness-layer instances
(prompt engineering, a first-party API flag, a measurement) and one model-layer instance.

⚠️ With the standing caveat from §4: the retrieval head is in the binary, and nothing in this repo
measures whether it works.

---

## 10. Verdict

**GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL (Cactus Compute, Inc., corporate-not-Anthropic per §41) ·
(b) **MODERATE**, keys the tier, per §40 on operator direction (the OFF-GOAL reading is defensible and
recorded) · (c) STRONG · (d) STRONG.

**NO MINT.** Declined on five independent grounds, three of them the vault's own written discipline:
the **model-tier rule** (`_patterns/06:171` — *"a single goal-adjacent frontier model is not a recurring
capability class; §C vocab is tool/capability-shaped"*), **not world-first** in a crowded band
(FunctionGemma 270M, LFM2.5, Apple FM, Octopus v2; grammar-constrained decoding is standard practice),
**domain-not-capability**, **§28 anti-inflation**, and the fact that **the distinctive machinery is not in
the subject**. The Model/Inference-Substrate tier becomes descriptive **N=5** (GLM-5 v176 · DeepSpec v186 ·
TimesFM v193 · PixelRAG v211 · Needle v246) — bookkeeping only. Counts **46/11 unchanged**; §C standalones
**51 unchanged**.

**Pilot: READ-AND-BORROW. Not a hireui component.** The takeaways cost nothing: the `silent` grep and its
rule, the `llms.txt` form, *"facts, never instructions,"* and the confidence-gated escalation shape.
See the Pilot Methods Menu.

**Blunt:** a fourteen-megabyte model that fits on a watch is a real engineering achievement, and almost
none of the achievement is in this repository — the retrieval head, the grammar and the confidence score
all live in a binary that gets downloaded into your process from a model host, version-pinned and
otherwise unverified, and whose source sits in a sibling repo under a licence that expires the day your
company crosses two million dollars. What *is* in this repository, and what is worth taking, is smaller
and better: an author who kept noticing the places where his software could be confidently wrong and
turned each one into an error message that names the cause, the consequence and the fix. You can find all
of them with `grep -rni silent`. And then — because this is the finding, not the compliment — you can
notice that the same author automated a daily publish to PyPI behind a test suite that skips every test
touching the thing being published, and that `pytest` calls a skip a pass. The discipline was applied
everywhere the user could be hurt and nowhere the project could be.
