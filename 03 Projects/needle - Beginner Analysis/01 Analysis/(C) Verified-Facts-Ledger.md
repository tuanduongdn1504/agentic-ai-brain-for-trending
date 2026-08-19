# (C) Needle 2 — Verified Facts Ledger

**Ship:** v246 · **Date:** 2026-08-19 · **Subject:** `cactus-compute/needle`

Every line below was verified by the orchestrator by hand against a source clone, or by a live
WebFetch. Each carries its provenance class: **SOURCE-VERIFIED** (read from the clone),
**PAGE-STATED** (read off a rendered page — the GitHub API is mocked in this environment, §37.4),
**COMPUTED** (arithmetic shown), or **NOT VERIFIED**.

---

## 1. Identity and scale

| Fact | Value | Class |
|---|---|---|
| Repo | `cactus-compute/needle` | PAGE-STATED |
| Tagline | "14MB foundation model for tiny devices; phones, wearables, smart home, and robots." | PAGE-STATED |
| Licence (this repo) | Apache-2.0 | SOURCE-VERIFIED (`LICENSE`) |
| Stars / forks / watchers | 7.6k / 487 / 48 | PAGE-STATED — **NOT Pattern #52** |
| PyPI package | `cactus-needle` | SOURCE-VERIFIED (`pyproject.toml:2`) |
| HEAD | `f7b64256ff9507ff80083c3d0c8f85a4cf470301`, 2026-08-18, `rshemet` | SOURCE-VERIFIED |
| Tracked files | 44 | SOURCE-VERIFIED (`git ls-files \| wc -l`) |
| Tracked lines | 10,824 | SOURCE-VERIFIED |
| Largest source file | `needle/model/architecture.py`, 630 lines | SOURCE-VERIFIED |
| Commits | **268 on `HEAD`** (259 non-merge + 9 merges); **452 on `--all`** | SOURCE-VERIFIED (D27: ref population declared) |
| Root commits | **1** — `12d98f69`, 2026-02-23, "Initial commit", Henry Ndubuaku | SOURCE-VERIFIED |
| Authors on `HEAD` | 17 distinct; `HenryNdubuaku` 225 + `Henry Ndubuaku` 9 ≈ 87% | SOURCE-VERIFIED |
| Commits/month on `HEAD` (commit date) | 2026-02: 17 · 2026-03: **167** · 2026-04: 34 · 2026-05: 16 · 2026-07: 2 · 2026-08: 32 | SOURCE-VERIFIED |

> ⚠️ **Counting-method note.** The first run of the month histogram printed only 50 of 268 commits.
> This is the vault's own known **zsh stdout-drop** defect, not a repo fact. The table above is the
> re-run routed to a file. *Any long pipeline in this environment must be routed to a file and `cat`-ed.*

---

## 2. The licence split — the load-bearing finding

| Artifact | Licence | Class |
|---|---|---|
| `cactus-compute/needle` (this repo — Python wrapper, JAX training/export) | **Apache-2.0** | SOURCE-VERIFIED |
| `LICENSE` changed **MIT → Apache-2.0** | commit `b188e110`, **2026-08-17** — two days before HEAD | SOURCE-VERIFIED |
| `huggingface.co/Cactus-Compute/needle2` (where the runtime binary is fetched from) | **apache-2.0** declared | PAGE-STATED |
| `cactus-compute/cactus` (the C++ engine **source**, 5.9k★, updated 2026-08-17) | **custom proprietary licence** — GitHub reports "Other" | PAGE-STATED |
| That licence's terms | Free use only for orgs with **< $2,000,000 USD total funding AND < $2,000,000 USD gross annual revenue**; above either threshold permission **auto-terminates**, commercial licence required within **30 days** | PAGE-STATED (raw `LICENSE`) |

**What the needle repo says about any of this: nothing.**
`grep -rn -iE "cactus-compute/cactus\|commercial licen\|proprietar\|funding\|revenue\|dual.?licen"` over the
entire tree returns **zero hits**. SOURCE-VERIFIED.

**Sufficient claim (not a legal conclusion):** a user reading `cactus-compute/needle` sees Apache-2.0,
installs `cactus-needle`, and loads a native engine into their process; the source of that engine lives
in a sibling repo under a revenue-capped licence, and **no document in either repo reconciles the two
declarations or states which governs the fetched binary.**

⚠️ **Fairness pins.** This is *not* concealment: the engine repo is public, prominently linked from the
org page, and its licence file is plain text. The HF repo the binary actually comes from declares
apache-2.0. The finding is a **reconciliation gap**, not a hidden term.

---

## 3. The runtime is a fetched native binary

- `needle/__init__.py:13-28` — `_library_path()`: env override `NEEDLE_LIB_PATH` → package-local lib →
  `~/.cache/cactus-needle/<ENGINE_VERSION>/` → else **download**.
- `needle/agent/fetch.py:88-102` — `fetch_library()` pulls
  `python/cactus_needle-<version>-py3-none-<platform-tag>.whl` from the **Hugging Face model repo**
  `Cactus-Compute/needle2`, opens it as a zip, and extracts `needle/libneedle.{dylib,so,dll}`.
- `needle/__init__.py:38` — `ctypes.CDLL(_library_path())` loads it into the host process.
- `needle/agent/fetch.py:8` — `ENGINE_VERSION = "2.0.2"` — the engine **is version-pinned by name**.
- `needle/agent/fetch.py:63-86` — `download_platform()` **sets the executable bit** (`S_IXUSR|S_IXGRP|S_IXOTH`)
  on files named `needle`/`needle.exe`.

**Fair security reading:** transport is HTTPS via `huggingface_hub`, and the artifact is
**version-pinned**. What is absent is **hash pinning and signature verification** — integrity rests on
Hugging Face's own etag/sha bookkeeping, i.e. on the server's claim. Threat model: a compromise of the
HF repo (or of a token with write access to it) yields **arbitrary native code execution in every user's
process on next fetch**. This is *not* the plaintext-`http://` MITM class of v234; it is the weaker
"unverified-but-pinned-over-TLS" class.

⚠️ `NEEDLE_LIB_PATH` (`__init__.py:16`) will `CDLL` **any** path given in the environment. Documented as
the air-gap escape hatch; noted for completeness, low marginal severity.

---

## 4. `_register_download()` — the download counter

`needle/agent/fetch.py:56-63`:

```python
def _register_download():
    from huggingface_hub import hf_hub_download
    try:
        hf_hub_download(repo_id=HF_REPO, filename="config.json", repo_type="model",
                        force_download=True)
    except Exception:
        pass
```

Called at the top of **both** `download_platform()` and `fetch_library()`. `force_download=True` bypasses
the cache, so it is **not** cache-warming — it is a deliberate, repeated hit on the model repo.

**Consequence (checkable):** the Hugging Face download counter for `Cactus-Compute/needle2` —
**PAGE-STATED 14,219 downloads last month** — is incremented by the package's own code on every engine
fetch, in addition to any genuine model download. That figure therefore **cannot be read as unique users
or unique model pulls**.

⚠️ **Characterisation, not accusation.** The function name is candid (`_register_download`), and
"register that a download happened" is a defensible reading of intent. What distinguishes the readings
is the `force_download=True` and the empty `except` — both consistent with telemetry, both also
consistent with counter inflation. **The vault's claim is limited to the measurable effect on the counter.**

---

## 5. The context window — the README does not match the code

The README (line 13) claims: *"a 256-token sliding window with the tools pinned as KV sinks."*

The code says something different:

- `needle/model/architecture.py:597-611` —
  `KV_BUDGET_BYTES = 11*1024*1024 + 512*1024` (**11.5 MiB**), `KV_GROUP = 32`, `KV_WINDOW_MIN = 160`.
  `kv_budget_window(config)` derives the window from a **byte budget**, then clamps to `max_seq_len`.
- `needle/model/architecture.py:66` — `max_seq_len: int = 2048`.
- The `256` that appears throughout the API (`complete`, `run`, `extract`, `generate`) is
  **`max_new_tokens` — the OUTPUT cap**, not the context window
  (`needle/__init__.py:109,125,147,165`; `llms.txt:22,23,27`).

**The configuration that matters is a named PRESET, not the dataclass defaults.**
`needle/model/architecture.py:38-43`:

```python
PRESETS = {"needle": dict(d_model=768, num_heads=12, num_kv_heads=6, num_layers=27,
                          engram_layers=(2, 15))}
PRESETS["base"] = dict(d_model=512, num_heads=8, num_kv_heads=4, num_layers=27,
                       engram_layers=(2, 15))
```

Note that the `TransformerConfig` dataclass defaults (`d_model=512, num_layers=12`) match **neither**
preset — both presets use **27 layers**.

**COMPUTED** (`awk`; `python3` is silently broken in this sandbox — a known vault defect):

| Config | d_model | heads | kv_heads | layers | head_dim | kv | per_pos bytes | **effective KV window** |
|---|---|---|---|---|---|---|---|---|
| **`needle` preset** | 768 | 12 | 6 | 27 | 64 | 384 | 25,056 | **480 tokens** |
| `base` preset | 512 | 8 | 4 | 27 | 64 | 256 | 16,704 | **704 tokens** |
| *dataclass defaults (neither preset)* | 512 | 8 | 4 | 12 | 64 | 256 | 8,064 | *1,472* |

> 🔴 **My error, corrected (E4).** The first pass computed **1,472** from the *dataclass defaults* and
> reported it as the answer. The defaults are not a shipped configuration — `num_layers=12` appears in
> neither preset. The `needle` preset gives **480**. Caught by the workflow's architecture mapper, which
> found `PRESETS` at `architecture.py:38-43`. **Same error family as E1 and E2: I took a default for the
> configuration.**

⚠️ **NOT VERIFIED:** which preset the distributed 14MB model is. `export.py:20-30` shows `kv_window` and
`kv_bits` ride **inside the `.cact` header** (`kv_window=0` = "size it from the budget alone"), so the
deployed geometry is authoritative and is not in this repo. Establishing it would require downloading
the weights, which this analysis did not do.

**Surviving claim:** the README's "256-token sliding window" is not a number the repository's own window
arithmetic produces for either preset (**480** / **704**), and it collides with the `max_new_tokens=256`
default that appears throughout the API. **The real bound is an 11.5 MiB byte budget, not a token count** —
and for the `needle` preset the true figure is roughly **2× the documented one**.

**⚠️ This materially changes the pilot assessment.** At ~480 tokens of context, **a whole CV cannot be
processed**, and even large sections will not fit. See the Pilot Methods Menu, M5.

---

## 6. The quantization claim

- README line 5: *"compressed to **CQ2-bit** with Cactus Quants."*
- `needle/model/export.py:5-7`: *"Format is **W4A8**: the matmul weights … are Cactus-Quants **INT4**;
  norms, Hadamard diagonals, and gates stay FP16."*
- `needle/cli.py:156`: `--bits` accepts only `choices=["2","4"]`, `default=None`.

**Surviving claim:** the headline advertises 2-bit; the export pipeline's documented format is **W4A8**,
and 2-bit is an opt-in flag. The README does hedge elsewhere ("`--bits 2` for a smaller model … falling
back to 4"). The two numbers describe **different artifacts** — the distributed model vs. what
`needle build` emits by default — and no document says so.

---

## 7. The cited paper reports a *cost*

- README line 23: *"See the paper for the design and ablations: arXiv:2607.18363."* The architecture is
  called **"Simple Attention Network."**
- **The paper exists** and shares the author list. Its actual title is
  **"A Controlled Study of Attention-Only Transformers"** (submitted 2026-07-20). PAGE-STATED via arXiv.
- Its reported finding: removing feed-forward layers **incurs a performance cost**, substantially — but
  not fully — recovered by reallocating capacity to attention depth; the residual gap concentrates on
  **tasks requiring knowledge retrieval from weights rather than context**. Scale range studied:
  **6M–87M parameters** (which brackets 45M).

⚠️ **Precision required.** The paper studies *attention-only* stacks (no FFN); Needle 2 uses a
**Hadamard MLP in place of** the FFN. Whether the paper's ablations cover that variant is **NOT VERIFIED**
from the abstract. The defensible statement is narrower: *the paper cited in support of the architecture
is titled differently from the name the README gives it, and its headline result is that the defining
choice carries a cost — a framing the README does not carry across.*

---

## 8. Cross-repo fact drift: 26m vs 45M

- `cactus-compute/needle` README line 5, `llms.txt:3`, the BibTeX title (`README.md:140`) and the HF model
  card all say **45M**.
- `cactus-compute/cactus` README — the org's own engine repo, **updated 2026-08-17**, two days before this
  HEAD — says: *"Needle is a **26m** parameter model for on-device tool calling"*, and directs users to
  `cactus run Cactus-Compute/needle` (note: **`needle`**, not **`needle2`**). PAGE-STATED.

Most likely Needle 1 vs Needle 2 — but **neither repo says so**, and nothing disambiguates the two HF
repos. Two current repos of one organisation state different parameter counts for a model of the same name.

---

## 9. The release train, and what its gate does not cover

**Verified externally (PyPI JSON):** 7 releases, **2.0.0 → 2.0.6, 2026-08-10 → 2026-08-17** — one per day.
The daily release train is real.

`.github/workflows/release.yaml`:
- Cron `0 16 * * *` and `0 17 * * *` with a DST guard selecting **09:00 Pacific**; `workflow_dispatch` too.
- Top-level `permissions: contents: read`; escalated to `contents: write` + `id-token: write` only in the
  release job — **least privilege**, and `id-token: write` + `pypa/gh-action-pypi-publish` = **PyPI Trusted
  Publishing (OIDC)**, i.e. no long-lived token. Both good.
- Version discovery uses `git tag --list 'v*' --sort=-v:refname | head -1` — a **correct version sort**.
  (Worth naming: the naive `git tag | tail` sorts *lexically*. This project got right what the vault's own
  v245 ship got wrong.)
- Bootstrap when no tag exists: `curl -s https://pypi.org/pypi/cactus-needle/json` — the workflow reads
  **its own published state** to decide the next version. Works; also means an outage or a PyPI hiccup
  feeds an empty version into the `awk` bump.
- No human in the loop between a merge to `main` and a public PyPI release.
- **Tags: 6** — `v2.0.1` … `v2.0.6` (correct version sort). **`v2.0.0` has no tag**, yet PyPI shows 2.0.0
  on 2026-08-10 — which corroborates that the `curl pypi.org` bootstrap path was genuinely exercised on
  the first run. SOURCE-VERIFIED + PAGE-STATED.
- Merge subjects carry `(#NN)` PR suffixes (`#18` on 2026-05-16 … **`#79` at HEAD**), so the project runs
  a normal squash/PR flow with at least 79 PRs.

**🔴 The gate: `pytest -q -m "not slow"`, on a fresh `ubuntu-latest`.** SOURCE-VERIFIED:

| File | Tests | Status in CI |
|---|---|---|
| `tests/test_inference.py` | 5 | **SKIPPED** — `pytestmark = requires_engine` (`:3`), and `conftest.py:20` skips when no engine is cached. A fresh runner has none. |
| `tests/test_build.py` | 3 | **DESELECTED** — `pytestmark = pytest.mark.slow` (`:6`) |
| `tests/test_finetune.py` | 2 | **DESELECTED** — `pytestmark = pytest.mark.slow` (`:8`) |
| `test_tools.py`, `test_generate.py`, `test_render.py`, `test_lora.py`, `test_weights.py`, `test_fetch.py` | 35 | run |

`tests/test_weights.py:33-38` monkeypatches `needle._lib` with a **stub**, so it exercises the Python
envelope, not the engine.

**Surviving claim:** every test that exercises the shipped inference engine is either deselected as slow
or skipped for a missing engine — and **`pytest` reports skips as success**. The daily automated publish
to PyPI is therefore gated on a suite that **cannot fail for an engine regression**.

---

## 10. Version strings in the tree are stale by design

- `pyproject.toml:3` → `version = "2.0.0"`; `needle/__init__.py:9` → `__version__ = "2.0.0"`.
- PyPI is at **2.0.6**. The release workflow `sed`s both files at build time and **never commits the
  change back**.
- Consequence: the published wheel reports correctly, but **the repository permanently reports 2.0.0** —
  and the documented dev path `./setup` runs `pip install -e .`, so a developer's `needle.__version__`
  reads 2.0.0 whatever they actually have.

This is the **v245 D32 situation without the D32 sentence**: two copies of one fact, the artifact
authoritative, the file stale — and **no precedence statement anywhere**.

---

## 11. Where the interesting machinery actually lives: the binary

`needle/__init__.py:38-48` binds exactly **four** C symbols: `needle_init`, `needle_complete`,
`needle_reset`, `needle_load`. Therefore:

- **Tool retrieval** ("top-5 of a large catalogue", grammar re-constrained to the subset) is
  **in the binary**. Python only passes `tool_index_path` through `needle_init`
  (`__init__.py:64, 89`). The "5" is **not** in this repo. NOT VERIFIABLE from source.
- **The byte-level grammar** is in the binary.
- **Confidence** is computed in the binary and returned in the JSON envelope; the JAX side has a
  `ConfidenceHead` (`architecture.py:463-488`) and exports it (`export.py:289`
  `HEAD_CODES = (("contrastive_head",1),("confidence_head",2))`), but the runtime path is the binary's.

**The JAX code in this repo is the training/export/reference side. The inference side is the blob.**

---

## 12. ⭐ The best thing in the repository: a doctrine you can grep for

`grep -rn -i "silent" .` returns **exactly four hits**. Three are the same idea:

1. `needle/__init__.py:73-77` — constructing a base-weights agent after a tuned one raises, because the
   engine cannot unload weights and *"this agent would **silently** answer with those weights"*. The
   message states the cause, the consequence **and** the remedy ("construct agents that want the base
   model before any tuned one, or run them in separate processes").
2. `needle/model/export.py:29-31` — `kv_window` and `kv_bits` are baked into the `.cact` header rather
   than left to a runtime flag, because *"a model quantized for one must be RUN at it — leaving either to
   a runtime flag **silently** [corrupts]"*.
3. `needle/model/export.py:547-554` — refuses an export that *"would **silently** ship plain W4 — numerics
   it was never post-trained for"*, and names the fix.

⚠️ **And the doctrine's one gap, which is also the tell.** That third message tells you to
*"Migrate it (`scripts/migrate_checkpoint_numerics.py`)"* — **`export.py:553`**. There is **no `scripts/`
directory and no tracked file matching `migrate*`** in the 44-file tree. SOURCE-VERIFIED. It is the
**only** dangling path reference in the repository: every `doc/*.md` link resolves
(`README.md:7,64,79`, `llms.txt:192`).

That single dangling path is evidence for a larger reading: **this repo is a curated public slice of a
bigger internal tree.** The same shape shows up three times — a migration script that is referenced but
not shipped; checkpoint stages (`qapt`, `HEAD_STAGES`) that no shipped code path produces; and the
inference engine itself, which lives in a different repository under a different licence.

Three more in the same spirit:
- `needle/__init__.py:57-60` — `warnings.warn` at construction when `weights=` is passed: *"finetuning does
  not update the confidence head … this agent reports confidence as None."*
- `needle/model/finetune.py:401` — the **same** disclosure printed at the end of every fine-tune run.
- `needle/__init__.py:92-96` — an unparseable envelope raises *"this is an engine bug — please report it
  with the prompt and schema."*

**The doctrine:** *every failure mode that would produce a confident wrong answer is converted into a
loud one; where it cannot be made loud, the setting is moved out of runtime flags and into the artifact
so it cannot be set wrong.*

⭐ **And `grep -rn "silent"` is a portable detector** — run it on any codebase to find the places its
author thought about silent corruption. Cost: one command.

**⚠️ The fourth hit is a counter-example, and it is what makes the finding honest.**
`doc/finetuning.md:19` — *"Each rendered example must fit within `--max-len` (default 1024) tokens; longer
examples are **silently truncated**."* Here a silent data-loss path is **documented rather than made
loud** — no warning is emitted when a training example is cut. So the doctrine is real but not total:
**three places convert a silence into a noise; the fourth admits a silence and leaves it in prose.**

> 🔴 **My own counting-method error, recorded.** The first pass ran this grep with `--include="*.py"` and
> reported **three** hits. The correct scope returns **four**, and the fourth *inverts* the finding's
> shape. This is the vault's own D26/D27 family — *a filtered grep is a claim about the filter* — and it
> is the second such error this ship (the first being the truncated month histogram, §1). Both were
> caught by re-running with the scope stated. **The lesson is the vault's own: state the population, then
> count.**

**⚠️ The irony, stated plainly:** this is the most silent-failure-conscious codebase the corpus has read,
and **its own release gate is a silent pass** (§9).

---

## 13. Honest-deficiency disclosure (#83) — unusually strong

The confidence-head disclosure appears in **four** independent places:
`llms.txt` ("Confidence gating"), `README`-linked `doc/apis.md`, a **runtime `warnings.warn`**
(`__init__.py:57`), and the **fine-tune job's own stdout** (`finetune.py:401`).

It is a disclosure that **the product's two headline features do not compose**: fine-tune it for your
tools, *or* gate on calibrated confidence — not both. Disclosed by the vendor, in code, at the moment
of the mistake.

---

## 13b. 🔴 Training provenance is disclosed **only** in a GitHub topic tag

The README explains the architecture down to the update rule — Walsh-Hadamard transforms, Sinkhorn
iteration, engram sites, sandwich norms. It says **nothing about what the base model was trained on.**

SOURCE-VERIFIED: `grep -rn -iE "distil|teacher|trained on|gemini|gemma"` across the whole tree returns
**zero** hits for the base model's training. Every `dataset` / `training data` hit in the docs refers to
**your** fine-tuning JSONL (`README.md:79`, `doc/finetuning.md:3,19,64,68,70`). The words *gemini* and
*gemma* appear **nowhere** in the repository's files.

But the repository's **GitHub topics** are: `cactus`, **`gemini`**, **`gemma`**, `llm`, `on-device-ai`
(PAGE-STATED). And third-party coverage describes Needle as *"a 26M-parameter model **distilled from
Gemini 3.1**"* (PAGE-STATED, secondary source, **NOT** confirmed by the project).

**Surviving claim:** the only place in the entire project that connects Needle to Gemini or Gemma is a
**GitHub topic tag** — the one piece of project metadata that is not in the git tree, not versioned, and
not visible to anyone who clones the repo.

⚠️ **This is a due-diligence gap, not an accusation.** Distillation from a frontier model is ordinary
practice and may be entirely licensed. The point for a prospective adopter is narrower and checkable:
**the training provenance of a model marketed for commercial on-device deployment cannot be established
from its repository**, and the one hint that exists lives outside version control.

⭐ Note the exact inversion of **v244 OpenSandbox**, where the affiliation lived in 1,674 enforced file
headers while `GOVERNANCE.md` named it zero times. Here the lineage lives *only* in the unversioned
metadata and zero times in the tree. **Both projects put a load-bearing identity fact in the one place
their own tooling does not check.**

---

## 13c. The project documents its own default as inadequate

`doc/finetuning.md:64` — *"the default 3 epochs is 39 steps total, which barely moves a rank 16 adapter at
the default learning rate. For a few hundred examples run 10 to 30 epochs."*

The shipped default (`cli.py:124`, `--epochs` default **3**) is described by the project's own
documentation as insufficient for a realistic dataset — which is also why `README.md:98` uses
`--epochs 10` in its example while `llms.txt:180` states the default as 3. **Not drift: the docs and the
code agree, and the docs tell you the default is wrong.** A second #83 instance.

---

## 14. Security posture — no broken-auth triad

- `needle/cli.py:174` — playground `--host` **defaults to `127.0.0.1`**; `:173` `--port 7860`.
  **Loopback by default.** Leg 1 of the triad: absent.
- `needle/playground/server.py:181` — `ThreadingHTTPServer((args.host, args.port), _Handler)`.
- `grep -n -iE "cors|access-control"` over `server.py` → **no hits**. Leg 2: absent.
- No auth at all — but on loopback, and the server holds no credential. Per **v245 D33** (leg 3's severity
  is set by the token transport) this is minor.
- The playground calls `agent.complete()` (`server.py:29-40`), **not** `run()` — so it returns the model's
  proposed call and **does not execute user Python**.

**Assessment:** clean for its class. Not a v231/v232 specimen.

---

## 15. Data egress

`needle generate-data` / `needle finetune --generate N` POST to OpenRouter
(`needle/model/finetune.py:56-66`) with `Authorization: Bearer $OPENROUTER_API_KEY`,
`HTTP-Referer: https://github.com/cactus-compute/needle`, `X-Title: needle`.

- **What leaves the machine:** your **tool schemas** and, for `--augment`, your **existing JSONL training
  examples** — the prompt asks a remote model to produce more like them.
- **Default remote model:** `deepseek/deepseek-v4-flash` (`cli.py:134,148`).
- Disclosed in README and `llms.txt` only as "Needs `OPENROUTER_API_KEY`" — the *content* of the egress is
  not spelled out.

🔴 **Operator rule: never point `--augment` at anything derived from candidate data.**

---

## 16. AI provenance

- **21 `Co-Authored-By: Claude` trailer LINES** on `--all` (D26: lines, not commits):
  Opus 4.6 ×14 · Opus 4.7 ×4 · Fable 5 ×2 · Opus 5 ×1 — every one annotated **"(1M context)"**.
- **Zero** commit *subjects* mention claude / mcp / agent.
- `grep` over the tree for any policy referencing them: **none** — no CONTRIBUTING, no CI check.
  Consistent with a **left-on Claude Code default**, as at v243.
- Other trailers present: `LeonSGP43`, `nyxst4ck`, `tchivs` sign-offs/co-authors.

**Anton Osika** has exactly **one** commit: `1c6fa930`, 2026-05-16, *"Fix typo and enhance clarity in
README (#18)"* — **README.md, 2 insertions / 2 deletions.** SOURCE-VERIFIED. A drive-by documentation
fix. ⚠️ The repository says nothing about who he is; per §41 the vault asserts nothing further.

---

## 17. Governance: what is absent

`.github/` contains **exactly one file** — `workflows/release.yaml`. SOURCE-VERIFIED.
No `CONTRIBUTING.md`, no `CODE_OF_CONDUCT.md`, no `SECURITY.md`, no issue or PR template,
no dependency scanning config, no `dependabot.yml`, no CodeQL.

⚠️ **v244 D28 applies:** an absent config file is **not** an absent check — GitHub settings can enable
scanning invisibly. The detector is bot trailers; none were found here, so the honest statement is
*no evidence of scanning either way*.

**Dependencies are entirely unpinned** (`pyproject.toml:7-15`: `huggingface_hub, numpy, jax, jaxlib,
flax>=0.10.2, optax, sentencepiece`) — while the `metal` extra pins **exactly**
(`jax==0.4.38, jaxlib==0.4.38, flax==0.10.2, optax==0.2.4`). The project knows how to pin; it pins only
where a version conflict already bit it.

---

## 18. Non-claims (stated so they are not later mis-cited)

- **NOT world-first** for tiny tool-calling models — see the prior-art analysis.
- **NOT Pattern #52** — star/fork figures are page-stated; the GitHub API is mocked here (§37.4).
- Do **not** cite "45M" as source-verified — it is stated in README/`llms.txt`/BibTeX/HF card and is
  **not** derivable from the reference config in this repo.
- Do **not** cite the HF download count as a usage measure (§4).
- **NOT VERIFIED:** the shipped model's real KV window; whether the fetched wheel is a build of
  `cactus-compute/cactus`; which licence governs that binary; whether the arXiv ablations cover the
  Hadamard-MLP variant; Anton Osika's relationship to the project beyond one commit.
