# (C) PixelRAG — Deep Dive

> LLM Wiki **v211** · shipped 2026-07-17 · subject `StarTrail-org/PixelRAG` · Apache-2.0
> *"PIXELRAG: Web Screenshots Beat Text for Retrieval-Augmented Generation"* — arXiv **2606.28344** (cs.IR, Jun 2026)
> Tagline: **"Search any document by how it _looks_, not just the text it contains."**
> ⚠️ This file was produced by Claude (prefix `(C)`), fully hand-verified per `feedback_wiki_verify_independently_check_collisions`. **NOT source-cloned** — WebFetch + arXiv + README-verified; engineering internals are page/paper-stated where flagged.

---

## 1. One sentence

PixelRAG is a **research retrieval system + a fine-tuned vision-language embedding model + a pip-installable pipeline + a hosted API + a Claude Code plugin** that performs Retrieval-Augmented Generation over **rendered document screenshots** (pixels) instead of parsed text — retrieving the right *tile* and letting a VLM read charts / tables / layout straight off the image — the corpus's **first visual/screenshot-based RAG** and **first general-document (non-code) RAG** subject.

## 2. The problem it attacks

Traditional text RAG parses a document (HTML/PDF) into text chunks, embeds the text, retrieves text, and feeds text to the reader. Everything the eye uses to understand a page — **table structure, chart values, column layout, infographics, diagrams, spatial relationships** — is destroyed at parse time. The paper's framing: text RAG "loses the table"; PixelRAG "retrieves the right tile, and the reader reads the number straight off the image."

The bet, stated in the title: **web screenshots beat text for RAG** — not only on visual questions, but *even on text-centric benchmarks* (NQ, SimpleQA), because the rendered page is a richer, layout-preserving representation than lossy parsed text.

## 3. Architecture (two stages, all in pixel space)

**Stage 1 — Render (`pixelshot`).** Documents (web pages, PDFs, images) → **screenshot tiles** via headless **Chromium (Playwright / CDP)** (+ poppler for PDFs). Output = image tiles, not text.

**Stage 2 — Retrieve (visual embeddings).** Tiles are embedded by a **VLM embedding model** — `Qwen/Qwen3-VL-Embedding-2B`, **LoRA-fine-tuned on screenshot data** — into a vector space where visually-similar/relevant tiles are retrievable. Search happens over the **images themselves**. Retrieved screenshots are then fed **directly as pixel inputs to a reader VLM**, with **no intermediate text conversion** (end-to-end pixel space).

**Backends:** **FAISS** (default, local, single-machine) or **Qdrant** (scalable — configurable quantization, disk-backed vectors, payload filtering, one collection shared by multiple PixelRAG servers). **Serving:** FastAPI (`pixelrag serve`, CPU/GPU).

**Scale (paper-stated):** *first pipeline to operate over a full Wikipedia corpus in pixel form* — a datastore of **~30 million screenshot images** (README: **8.28M Wikipedia pages** pre-indexed) with an efficient visual retrieval index.

## 4. The CLI pipeline

| Command | Job |
|---|---|
| `pixelshot` | Document → image tiles (Playwright/CDP; PDF via poppler) |
| `pixelrag chunk` / `embed` / `build-index` | Tiles → vectors → FAISS index |
| `pixelrag index build` | Orchestrates the full pipeline (config-driven, `pixelrag.yaml`) |
| `pixelrag serve` | FAISS/Qdrant search API (FastAPI) |

**Staged install** (pay for only what you use):
```
pip install pixelrag                    # pixelshot only
pip install 'pixelrag[embed]'           # chunk/embed/index
pip install 'pixelrag[index]'           # full pipeline
pip install 'pixelrag[serve]'           # search API
pip install 'pixelrag[serve,qdrant]'    # + Qdrant backend
```

**Local-PDF quickstart** (config-driven): write a `pixelrag.yaml` (`source: local`, `embed.model: Qwen/Qwen3-VL-Embedding-2B`, `output`), then `pixelrag index build` → `pixelrag serve --index-dir ./paper_index`.

## 5. The Claude Code plugin — `pixelbrowse` (the on-goal bridge)

The corpus-relevant piece. Instead of fetching **raw HTML**, Claude **screenshots a page and reads the image** — "seeing charts, diagrams, tables, and layout the way a person does."

```bash
uv tool install pixelrag                               # puts pixelshot on PATH
claude plugin marketplace add StarTrail-org/PixelRAG
claude plugin install pixelbrowse@pixelrag-plugins
```
Usage: `claude -p "screenshot https://news.ycombinator.com and summarize the top stories"`, or `/screenshot https://example.com` interactively. **No backend server** — it calls `pixelshot` locally.

This is the direct analogue of every prior corpus "give the agent a compact perception surface instead of raw bytes" move — but the surface is **pixels** (a rendered screenshot), not text-dehydrated DOM. (See §9.)

## 6. Hosted API

`https://api.pixelrag.ai` — a pre-built index over 8.28M Wikipedia pages, **no key / no setup**. Accepts **text queries** and **visual queries** (an image as the query):
```
curl -X POST https://api.pixelrag.ai/search \
  -H "Content-Type: application/json" \
  -d '{"queries":[{"text":"What is the capital of France?"}],"n_docs":5}'
```
⚠️ Sensitive queries egress to their hosted service — for private/candidate data use a **local FAISS** index (§13).

## 7. The model & training

- **Base:** `Qwen/Qwen3-VL-Embedding-2B` (a VLM embedding model). The **hard AI is upstream** — PixelRAG *fine-tunes* it.
- **Adapter:** LoRA, published at `Chrisyichuan/wiki-screenshot-embedding-lora`.
- **Training:** a separate `uv` project (`train/`), pinned env (`torch==2.9.1+cu129`, `transformers==4.57.1`). **Contrastive training** with **LLM-augmented query generation + filtering + hard-negative mining**. Public dataset `Chrisyichuan/screenshot-training-natural-filtered-v2`.

## 8. Benchmark claims (paper-stated — treat as authors' own)

- Outperforms **both** no-retrieval and **text-based RAG** baselines.
- Surprisingly, wins on **text-centric** tasks too — **NQ**, **SimpleQA**.
- Gains on **multimodal open-domain QA**, **noisy news corpora**, and **agentic benchmarks**.
- **Up to +18.1% accuracy** over text-based baselines.
- The README itself carries **no** headline numbers (the claim there is conceptual); the numbers live in arXiv 2606.28344. **These are the authors' own results — not independently reproduced here.**

## 9. ⭐ The sharpest corpus cross-reference: pixels vs text-dehydration

PixelRAG's `pixelbrowse` joins the corpus's **"structured-surface-not-raw-dump" perception thread** — but at the *opposite modality pole* from the most recent member:

| Subject | Perception surface handed to the agent |
|---|---|
| browser-use v41 | text-extracted interactive-element list |
| codebase-memory-mcp v172 (§C#23) | pre-indexed code graph (Cypher) |
| fff v194 | lexical/fuzzy file search results |
| video-use v198 | a word-level **transcript** (read, don't watch) |
| **page-agent v199** | **DOM dehydrated to `[index]<tag>text</tag>` TEXT** |
| **PixelRAG (pixelbrowse) v211** | **the page rendered to a SCREENSHOT — PIXELS** |

page-agent v199 and PixelRAG are a clean thesis/antithesis: both refuse to dump raw HTML at the model, but page-agent compresses the page **to text** (cheap, token-lean, loses visual structure) and PixelRAG renders it **to pixels** (preserves visual structure, costs vision tokens). The whole corpus thread is "don't give the model raw bytes; give it a curated surface" — PixelRAG is the pixel-modality member and the visual counterpoint to page-agent.

## 10. Corpus placement (the other cross-refs)

- **claude-context v40** — the corpus's vector-embedding RAG **for CODE** (semantic code search). PixelRAG = vector RAG for **general documents**, **visual modality**. The §C registry explicitly names claude-context v40 as "the vector-based sibling" of the code-knowledge-graph family (§C#23).
- **crawl4ai v29** — web-content extraction *to markdown/text* for LLMs. PixelRAG's `pixelbrowse` is the **visual** alternative (screenshot, don't parse).
- **The Playwright/Chromium-CDP browser cluster** — browser-use v41 / Skyvern v24 / camofox v179 / serve-sim v183 / page-agent v199. PixelRAG renders with the same CDP substrate but for a different purpose (embed the pixels, not drive the DOM).
- **The model/research-substrate tier** — TimesFM v193 (forecasting FM) / DeepSpec v186 (spec-decoding) / GLM-5 v176 (frontier LLM) / fish-speech v20 (TTS model) / LLMs-from-scratch v74. PixelRAG's center of gravity (a fine-tuned VLM + a paper) puts a foot in this tier.
- **hireui (Goal #2) — CV parsing.** CVs/résumés are visually-formatted PDFs (columns, skill matrices, badges, tables) where text extraction is brittle. Screenshot-based visual retrieval/reading is a genuine alternative to OCR→text→parse (see the `miai-cv-matching` and `miai-iphone-ocr-server` memory threads).

## 11. Identity (hand-verified)

- **Repo/org:** `StarTrail-org/PixelRAG`. Landing page `pixelrag.ai`.
- **Authors (equal contribution):** Yichuan Wang, Zhifei Li, Zirui Wang, Paul Teiletche, Lesheng Jin. **Advisors (equal):** **Matei Zaharia** (Databricks co-founder / Apache Spark creator), Joseph E. Gonzalez, Sewon Min.
- **Affiliations:** **UC Berkeley (SkyLab / BAIR / Berkeley NLP), Princeton, EPFL, Databricks.**
- **NOT Anthropic.** Per routine §41, the authors' notability (Zaharia) earns **no (a)-axis rescue** — (a) passes only on a declared Anthropic affiliation or a registered (a)-7 vendor-direct source. First `StarTrail-org` / Berkeley-SkyLab / Zaharia-cluster author in the corpus (#19 19a institutional data-point).
- ⚠️ **Typosquat/fork forks exist** — `Puneetb/pixelrag`, `sp00ler/pixelrag`, `seco/pixelrag` all carry the same "The end of web parsing" tagline. **Install from `StarTrail-org` only.**

## 12. Collision check (sanity-anchored hand-grep, `_state/` + `_patterns/`)

- **Anchors HIT** → grep works: `claude-context` (11 files), `crawl4ai` (14), `RAG` (6), `screenshot` (many).
- **CLEAN (0 hits):** `pixelrag`, `startrail`, `colpali`, `visual rag / screenshot rag / screenshot-based / visual document / multimodal retrieval / visual retrieval`, `qwen3-vl embedding`, `zaharia / skylab / BAIR / berkeley nlp / sewon min`, `pixelbrowse / pixelshot`.
- Only `qwen-vl`-family hit = **Qwen2-VL** GUI-agent fine-tuning in dive-into-llms v39 ch.9 (LLaMa-Factory) — *not* a visual-RAG/embedding subject.
- → **Corpus-first for visual/screenshot-based RAG, confirmed by hand.**

**World-first? NO.** **ColPali** (2024, PaliGemma-3B + ColBERT patch embeddings) and **DSE — Document Screenshot Embedding** (arXiv 2406.11251, 2024, "encode document screenshots into vectors, bypassing OCR") both precede; the visual-document-retrieval area is active (ColPali → ColQwen2 → ColFlor → ModernVBERT → DSE). PixelRAG's distinctive claims = **full-Wikipedia web-screenshot scale (30M images)**, an efficient index, **end-to-end pixel reader**, and **beating text RAG on text-centric tasks**. So: **corpus-first, NOT world-first.**

## 13. Install & data-privacy surface (#66)

- Install surface: `uv tool install pixelrag`, `pip install pixelrag[...]`, `claude plugin marketplace add StarTrail-org/PixelRAG`, `claude plugin install pixelbrowse@pixelrag-plugins`. **Playwright downloads Chromium.** Apache-2.0. Install itself is **BENIGN** (standard Python/plugin install; no `curl|bash` observed).
- Real risks: (1) the **hosted `api.pixelrag.ai` egresses your queries** → use a **local FAISS** index for private/candidate data; (2) **typosquat forks** (§11) → StarTrail-org only; (3) `pixelbrowse` screenshots arbitrary URLs locally (fine) but a screenshot of a page with PII is now an artifact on disk; (4) v0.4.0 / 4 releases = young — pin the version.

## 14. Honest caveats (what to distrust)

- **The hard AI is upstream** (Qwen3-VL-Embedding-2B + a LoRA + a reader VLM). PixelRAG orchestrates + fine-tunes; it does not invent the vision model.
- **Benchmarks are the authors' own** paper-stated results; "+18.1%" / "beats text on NQ/SimpleQA" are not independently reproduced here.
- **NOT world-first** (ColPali/DSE precede — §12).
- **NOT source-cloned** (WebFetch + arXiv + README only).
- **Young** (v0.4.0, 4 releases, 2026).
- Vision retrieval + pixel-reader has **token/latency cost** (feeding a screenshot to a VLM is heavier than feeding parsed text) — the accuracy gain has an efficiency price the README doesn't quantify.

## 15. So what (the takeaways worth keeping)

1. **A rendered surface can beat a parsed one.** The layout you'd throw away at parse time is signal — for retrieval *and* for reading. This generalizes beyond RAG.
2. **The perception-surface question is modality-agnostic.** page-agent v199 says "compress to text"; PixelRAG says "render to pixels." The right answer is task-dependent (token budget vs visual structure) — and *both* beat "dump raw HTML."
3. **`pixelbrowse` is a free, zero-backend Claude Code plugin you can install today** — the one immediately-actionable piece.
4. **For hireui, the CV-parsing map is real** — visual retrieval/reading sidesteps OCR brittleness, but drags in candidate-PII + data-residency (local FAISS + own model, not the hosted API).
