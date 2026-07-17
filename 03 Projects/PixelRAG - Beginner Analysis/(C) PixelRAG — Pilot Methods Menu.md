# (C) PixelRAG — Pilot Methods Menu (24 methods)

> LLM Wiki **v211** · `StarTrail-org/PixelRAG` · 2026-07-17
> **On-goal + directly pilotable for BOTH goals.** The value is threefold: (1) a free, install-today Claude Code plugin (`pixelbrowse`); (2) a transferable *idea* (a rendered surface can beat a parsed one); (3) a sharp hireui CV-parsing map (visual retrieval vs OCR).
> ⭐ **One-thing path: A1 → C11 → D16.**
> **Fence (read first):** install-snapshot + pip/npm-security-check `pixelrag` + install from **StarTrail-org only** (typosquat forks Puneetb/sp00ler/seco) + Playwright downloads Chromium + the hosted `api.pixelrag.ai` **egresses your queries** → use **local FAISS** for private/candidate data + candidate PII in screenshots ⇒ a **data-residency ADR FIRST** + hireui per its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first; **no LLM spend yet → design/spec, don't retrofit**) + pin **v0.4.0**.

---

## A — Read & learn (zero install, zero risk)

- **A1 ⭐ Read the paper + the pixel-reader idea.** arXiv **2606.28344**. Internalize the two claims: (i) *a rendered screenshot is a richer retrieval surface than parsed text* — enough to win on **text-centric** tasks (NQ/SimpleQA); (ii) *feed retrieved pixels straight to a VLM reader — no text conversion*. This is the durable takeaway, independent of the code.
- **A2** Read the `pixelbrowse` plugin design (README §Plugin) as a case study in "give the agent a curated surface, not raw HTML" — and note it needs **no backend**.
- **A3** Read the training recipe (LoRA on `Qwen3-VL-Embedding-2B` + LLM-augmented query gen + hard-negative mining) as a template for *fine-tuning a retrieval embedder on your own domain's rendered documents*.
- **A4** Read the landscape you now know: ColPali / DSE / ColQwen2 — so you can place PixelRAG (corpus-first, not world-first) and pick the *right* visual-retrieval tool for a real task.

## B — Borrow patterns (zero / near-zero install)

- **B5 ⭐ Put "structured-surface-not-raw-dump" in `CLAUDE.md`** as an explicit rule, now with **both poles**: *page-agent v199 → text-dehydrate; PixelRAG → render-to-pixels; never dump raw HTML at the model.* Pick per task (token budget vs visual structure).
- **B6** Write the **hireui CV-representation ADR**: "for visually-formatted résumés, prefer a rendered/visual representation over lossy text extraction; measure both." Cite PixelRAG + the `miai-iphone-ocr-server` OCR thread as the two candidate mechanisms (visual-embed vs OCR).
- **B7** Steal the **hard-negative-mining + LLM-augmented-query** contrastive recipe for any future hireui retrieval feature (candidate↔job matching evals).
- **B8** Steal the **staged-install** discipline (`pixelrag[embed|index|serve]`) as a template for how to ship a heavy pipeline as thin, opt-in extras.

## C — Hands-on scratch (low-risk, throwaway)

- **C11 ⭐ Install the `pixelbrowse` Claude Code plugin** (`uv tool install pixelrag` → `claude plugin marketplace add StarTrail-org/PixelRAG` → `claude plugin install pixelbrowse@pixelrag-plugins`; **install-snapshot first**). Prove the loop: `/screenshot https://<a-page-with-a-table>` and ask Claude to read a value it would lose from raw HTML.
- **C12** Hit the **hosted API** on a public query (`curl … api.pixelrag.ai/search`) — measure retrieval quality on a Wikipedia question. **Public data only** (queries egress).
- **C13** Build a **tiny local FAISS index** on a scratch PDF (`pip install 'pixelrag[index]'` → `pixelrag index build` → `pixelrag serve`). This is the 100%-local path — the one safe for private data later.
- **C14** A/B it: same question, `pixelbrowse` (pixels) vs a normal `WebFetch`/`crawl4ai` (text). Note where the visual path wins (charts/tables/layout) and where it's overkill (plain prose).

## D — hireui / Goal-#2 (behind the CONSTITUTION fence)

- **D16 ⭐ The CV-screenshot-vs-OCR extraction spike.** On an `agent-*` branch, on a **sanitized/synthetic** CV: render the CV to screenshot tiles → feed tiles directly to a VLM (or embed with a local visual model) → structured extraction (skills/roles/dates) → compare against the OCR→text→parse path (the `miai-cv-matching` / `miai-iphone-ocr-server` threads). Metric: fields correctly extracted from a *visually-complex* CV (2-column, skill-matrix, badges). **LOCAL only** — no hosted API, no real candidate PII.
- **D17** Write the **candidate-PII data-residency ADR** BEFORE any real-CV pilot: screenshots of CVs are PII artifacts + the hosted API egresses queries ⇒ local FAISS + own model + retention/deletion policy. Gate D16 behind this.
- **D18** Feed the result into the **hireui first-LLM-feature spec** (the mosh-ai A2 vendor-seam + the candidate-LLM legibility ADR): if a visual representation grounds Match-Explain better, spec it as an *optional deterministic pre-processing stage*, keeping the legible/audited harness.
- **D19** Bake-off vs the plain-OCR baseline you already scoped (`miai-iphone-ocr-server`): visual-embed vs OCR-text on the *same* CV set — decide which is worth the token/latency cost.

## E — Off-goal / personal (optional)

- **E20** Visual search over your own docs (slide decks, dashboards, scanned notes) via a local FAISS index — the "search by how it looks" use.
- **E21** Use `pixelbrowse` as a general research aid: screenshot-and-read data-dense pages (papers, benchmark tables) where raw HTML mangles the layout.

## F — Vault-meta

- **F22 ⭐** Write the **"structured-surface-not-raw-dump" synthesis** across browser-use v41 / codebase-memory-mcp v172 / fff v194 / video-use v198 / **page-agent v199 (text) / PixelRAG (pixels)** — the perception-modality spectrum — for the ~v212 audit.
- **F23** Log the **NO-MINT §C reviewable alternative** ("Visual/Screenshot-Based Multimodal Document RAG," N=1) + the DEFERRED watch axis for the ~v212 audit; promotion-eligible at a 2nd visual-RAG subject.
- **F24** Add PixelRAG to the **model/research-substrate tier** roster (TimesFM v193 / DeepSpec v186 / GLM-5 v176 / fish-speech v20 / PixelRAG) — the tier-taxonomy question for the audit.

---

### Recommended ladder (blunt)

1. **A1** (read the paper — the idea outlives the code).
2. **C11** (install `pixelbrowse`, prove the pixel-reader loop on one page). Zero backend, install-snapshot first.
3. **D16** (the CV-screenshot-vs-OCR spike, LOCAL + sanitized data, `agent-*` branch) — but **D17 (the PII/residency ADR) gates it**.

Everything else is optional. The two things that will actually change your practice: the **`CLAUDE.md` rule (B5)** and the **hireui CV-representation ADR (B6/D17)**.
