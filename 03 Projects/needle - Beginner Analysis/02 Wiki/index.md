# Needle 2 — Wiki Index (v246)

**Subject:** [`cactus-compute/needle`](https://github.com/cactus-compute/needle) — "Needle 2", a
45M-parameter foundation model for tool calling, device use and structured extraction.
**Shipped:** 2026-08-19 · **Branch:** `wiki/v246-needle` off the v245 tip (`1353b72`)
**Verdict:** GOAL-ALIGNED INCLUDE 3/4 · **NO MINT** · counts **46/11 unchanged**

---

## Pages

| Page | What it holds |
|---|---|
| [(C) Deep Dive — Needle 2](<(C) Deep Dive — Needle 2.md>) | The narrative analysis — the licence split, the `silent` doctrine, the release-gate finding, the claim-vs-code gaps |
| [(C) Verified Facts Ledger](<../01 Analysis/(C) Verified-Facts-Ledger.md>) | Every fact with its provenance class (SOURCE-VERIFIED / PAGE-STATED / COMPUTED / NOT VERIFIED) |
| [(C) Phase-0.9 Verdict and Mint Decision](<../01 Analysis/(C) Phase-0.9-Verdict-and-Mint-Decision.md>) | The four-criterion call and the five grounds for NO MINT |
| [(C) Pilot Methods Menu](<../01 Analysis/(C) Pilot Methods Menu.md>) | M1–M5, lowest footprint first, with fences |
| [(C) Error Ledger](<../01 Analysis/(C) Error Ledger.md>) | 3 of mine, 2 agent claims rejected |
| `00 Source/needle/` | Source snapshot at HEAD `f7b64256` (2026-08-18) |

---

## The one-paragraph version

Needle 2 is a 14MB tool-calling model that runs in ~28MB of RAM on phones, wearables and robots. This
repository is not the model — it is the **Python package around it**: 44 files, 10,824 lines of
inference bindings, a JAX reference implementation, a LoRA fine-tuning pipeline and a quantizing
exporter. The actual inference engine is a **native binary downloaded from Hugging Face on first use**
and loaded into your process, and everything distinctive about the product — the learned tool-retrieval
head, the byte-level grammar, the confidence score — lives inside it. **The best thing in the repository
is not the model.** It is a design doctrine you can find with `grep -rni silent`: every failure mode that
would produce a confident wrong answer has been converted into a loud one, with the cause, the
consequence and the remedy in the message. And the sharpest finding is the tension around it — the same
project publishes to PyPI automatically every day behind a test suite in which every engine-touching test
is skipped or deselected, and `pytest` reports a skip as a pass.

---

## The five findings

1. **The licence is split across two repos and the restrictive half is the half you execute.**
   This repo is Apache-2.0. The engine's source (`cactus-compute/cactus`, 5.9k★) is under a custom licence
   capped at **$2M funding / $2M revenue**, auto-terminating in 30 days. The fetched binary comes from an
   HF repo declaring apache-2.0. **No document in either repo reconciles the three.** Not concealment —
   a reconciliation gap. → *Third consecutive ship (v244 · v245 · v246) where stated licence ≠ executed
   artifact.*

2. **`grep -rni "silent"` returns the codebase's design doctrine in four lines** — three conversions of a
   silent wrong answer into a loud failure, and one admitted exception that keeps it honest.

3. **The daily automated PyPI release is gated on a suite that cannot fail for an engine regression** —
   5 tests skipped (no engine on a fresh runner), 5 deselected as slow, and skips are green.

4. **Three README claims the code does not support**: the "256-token sliding window" (the code derives
   ~1,472 tokens from an 11.5 MiB byte budget; the 256 is `max_new_tokens`), "CQ2-bit" (the export format
   is documented as **W4A8/INT4**), and the cited arXiv paper — real, same authors, but titled *"A
   Controlled Study of Attention-Only Transformers"* and reporting that dropping FFN layers **costs**
   performance.

5. **The training provenance exists only in a GitHub topic tag.** The repo explains its architecture down
   to the update rule and says nothing about training data; *gemini* and *gemma* appear nowhere in the
   tree but **are two of its five GitHub topics**. → *The exact inversion of v244, where the identity
   lived in 1,674 enforced headers and zero governance docs.*

---

## Corpus effects (recorded, not self-executed — a promotion is an audit act)

- **NO MINT.** Five grounds; the model-tier discipline (`_patterns/06:171`) is decisive.
- **Model/Inference-Substrate tier → descriptive N=5** (GLM-5 v176 · DeepSpec v186 · TimesFM v193 ·
  PixelRAG v211 · Needle v246). Bookkeeping only.
- **Library-vocab #12 "LLM-routing artifacts"** (CONFIRMED, N=5+) — clean instance-strengthening via a
  notably strong `llms.txt`.
- **Pattern #83 Honest-Deficiency-Disclosure** — two instances, one exceptional (the confidence head is
  not updated by fine-tuning, disclosed in four places including a runtime warning).
- **The tool-catalogue thread reaches N=4 and spans two layers for the first time**: v167 (~54K floor) →
  v238 (blank the injections) → v245 (measure it) → **v246 (move it into the weights)**.
- **Collision: clean.** Zero prior corpus mentions of cactus-compute / Needle / Henry Ndubuaku.
- **Streak:** `GA:104 · OG:13 [7 ov]` — 27 consecutive GA (v220→v246). **§35 CLEAR.**

---

## Pilot

**READ-AND-BORROW. Not a hireui component.**
⭐ **M1 → M2 → M3** — the `silent` grep and its rule, the `llms.txt` form, and *"facts, never
instructions"* — ~45 minutes, zero installs, all three land as durable rules.
🔴 Never put candidate data through `generate-data`/`--augment` (OpenRouter egress). Never ship the
fetched binary in a product path. Never rely on `confidence` after fine-tuning — it is `None` by
construction. Never cite its benchmark numbers; there is no eval harness in the repo.
