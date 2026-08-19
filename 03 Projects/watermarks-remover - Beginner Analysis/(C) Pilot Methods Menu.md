# (C) watermarks-remover — Pilot Methods Menu

**Subject:** `guillaumemeyer/watermarks-remover` · **Wiki:** v251 · **Date:** 2026-08-19
**Headline verdict: READ-AND-BORROW. Do NOT install.**

---

## Why this is not an install, even though the engineering is good

This is an unusual verdict shape for this corpus, so state the reasoning plainly.

The **security** posture is genuinely LOW-concern: loopback-only bind, no CORS, real SSRF/XXE/zip-bomb guards, non-root read-only containers, env-only API keys, redirect refusal, a careful staged installer with rollback, SHA-pinned CI with `pip-audit` and CodeQL, 465 test functions. On the vault's usual axes this would pass an install fence comfortably — it is better engineered than several tools the corpus has piloted.

**The blocker is purpose, not safety.**

1. The operator ships **hireui**, a recruitment SaaS handling candidate data, under a **RATIFIED ADR** requiring any candidate-touching LLM path to be *fixed, legible, audited, human-in-loop and eval-gated*. A tool whose function is to **remove** provenance from AI output is the categorical opposite of that commitment.
2. **EU AI Act Article 50** transparency obligations are live in the operator's market. Anthropic has signed the Article 50(2) Code of Practice ([verified at source](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)). Hiring is a high-stakes domain under that regime.
3. Recruitment is precisely the context the subject's **own ethics file** names as out of bounds — `references/ethics.md:14-16` lists *"misrepresenting AI assistance where disclosure is required"* and *"Circumventing lawful transparency or platform disclosure rules"* as **not appropriate**.

**There is no configuration in which this belongs near hireui.** That is not a criticism of the project; it is a statement about the operator's use case.

---

## Rung 0 — 20 minutes, zero install, zero risk: read four files

The value here is knowledge, and it is concentrated in four documents already on disk in the clone (or readable on GitHub):

| File | Why |
|---|---|
| `skills/remove-ai-marks/references/removal-matrix.md` | The **"Verifiable today?"** column — a capability matrix that answers *No* on its own headline features. The single most borrowable artifact. |
| `README.md:745-766` — *"Disclaimer: what removing a text watermark costs"* | A project arguing against its own product, with a real technical argument. |
| `skills/remove-ai-marks/references/ethics.md` | 32 lines; the three-way verifiable / best-effort / out-of-scope honesty taxonomy. |
| `README.md:788-800` — the qpdf/exiftool section | The "silent leak" analysis: a tool that exits `0` while the data survives. |

**Do this one regardless of everything below.**

---

## Rung 1 — 2 hours, zero install: port three ideas into the vault and hireui

⭐ **This is the rung that pays.** None of it requires running the subject.

### (a) Add a "How would we know it worked?" column

Port `removal-matrix.md`'s discipline to two places:

- **hireui's feature matrix** — every LLM-touching capability gets a column stating *how you would verify it worked in production*. Anything that cannot answer becomes a labelled gap, not a silent assumption. This directly discharges the eval-gating clause of the RATIFIED candidate-LLM ADR, which still has no implementation.
- **`PATTERN_LIBRARY.md`** — every CONFIRMED pattern gets a verifiability note. The corpus currently asserts N-counts without stating what would falsify them.

### (b) Push the caveat into the response, not the docs

The subject writes *"cannot certify…"* into `rewrite_text.py:495` and `markdiffusion_harness.py:14` — the hedge reaches the **user at runtime**, not just the reader of a README.

Apply to **hireui Match-Explain**: the confidence caveat belongs in the **API response body** alongside the score, so every downstream consumer inherits it. A caveat that lives only in documentation is not a caveat, it is a footnote nobody reads. This composes with the v217 wardrobe CV-parse template (`vision → confidence-scored JSON → anti-fabrication → QA gate`) already recorded in memory.

### (c) Byte-equality assertion for duplicated content

`tests/test_lightweight_skill.py:79-85` asserts two vendored copies of a file are byte-identical, and `:89` carries the incident that motivated it.

The vault has this disease: the `_state/03c-projects-v61-v183.md` filename label lags **68 versions** behind its contents, and the shim-vs-registry counts diverge. Fold this into the **`bin/verify-vault-inventory.sh`** already specified as v250's Rung 1 (bidirectional inventory over `_state/` ↔ `CLAUDE.md` and memory files ↔ `MEMORY.md`, in `node`/`awk` — **not** `python3`, which is SIGKILLed in this sandbox). Add a fourth clause: any file that exists in two places must be byte-identical, and the check's comment records why.

---

## Rung 2 — the defensive read, 1–2 hours, zero install

⭐ Treat the repository as a **map of where AI provenance marks live**, which is what a defender wants.

Read `service/scripts/image_meta.py` and `service/scripts/container_meta.py` (**153,786 bytes combined**) as a per-format reference for which bytes carry provenance across PNG, JPEG, WebP, AVIF, HEIC, BMP, GIF, TIFF, SVG, PDF, DOCX, XLSX, PPTX, EPUB, ODT, HTML, MD, MP4/MOV/M4A/M4V, WAV and MP3.

**Concrete hireui application:** if hireui ever generates a document for a candidate or client (an offer letter, a generated summary, an exported report), this tells you exactly where a C2PA manifest or an AI generator tag would live in that format — i.e. **what you must preserve** rather than strip, and what your pipeline might be destroying by accident. Note that many upload/re-encode pipelines strip C2PA silently; if hireui re-encodes uploads, it may already be destroying provenance it should keep.

Pair with `score_stylometry.py` — zero-LLM cadence/burstiness scoring, **detection only, no model required**. This is the cheapest thing in the repo to reason about and the only part with a defensible read-only use.

---

## Rung 3 — NOT RECOMMENDED: running the service

Documented for completeness only, since the ethical fence above is the binding constraint, not the technical one.

If it were ever run for research on **your own** files, the fence would be:
- `install-snapshot` first (standing vault skill)
- `docker compose up` core profile only — **never** `--profile heavy` (that builds `ctrlregen` and `reverse-SynthID`, which carry a non-commercial Research License and a no-LICENSE-at-all upstream respectively; see `README.md:224`)
- keep the default `127.0.0.1:8765` binding; set `WATERMARKS_SERVER_API_KEY` anyway (it fails open without one)
- Layer A / metadata only — **never** Layer B, which sends your text to a model
- scratch files only; **never** anything containing candidate or client data
- pin to a tag (`v0.5.0`), auto-update off

**Do not do this for the vault's purposes.** There is no question the vault needs answered that requires executing it.

---

## What NOT to do — hard lines

🔴 Never point it at candidate CVs, cover letters, or any submitted document.
🔴 Never use it to make AI-assisted output appear human-written in a hiring, academic, or compliance context — the subject's own ethics file forbids this.
🔴 Never cite its removal capability as verified. **Its own matrix answers "No" to "Verifiable today?"** on statistical text and pixel watermarks.
🔴 Never repeat *"Google confirmed … DETECT_TEXT_WATERMARK is rejected"* — the cited forum thread does not say that, and the responder's affiliation is unestablished (see Deep Dive §10.1).
🔴 Never cite the star count as verified — page-stated only; the GitHub API is mocked in this environment.
🔴 Never install the Cursor skill on a machine used for client work — not because it is unsafe (it is well-built), but because its presence in a professional toolchain is itself a fact you would have to explain.

---

## Suggested sequence

**Rung 0 (20 min) → Rung 1(a) and 1(b) (2 h) → Rung 1(c) folded into the v250 `verify-vault-inventory.sh` item → Rung 2 only if hireui adds document generation.**

Stop there.
