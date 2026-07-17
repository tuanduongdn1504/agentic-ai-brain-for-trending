# (C) PixelRAG — Verdict

> LLM Wiki **v211** · `StarTrail-org/PixelRAG` · 2026-07-17 · routine v2.7
> Produced **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions` — **no workflow / no subagent** (the ~205K shim overflows every subagent >200K → prompt-too-long; the v202→v210 self-throttle precedent).

---

## Decision: GOAL-ALIGNED INCLUDE · 3 of 4

| Criterion | Call | Reasoning |
|---|---|---|
| **(a)** author = Anthropic / registered (a)-7 | **FAIL** | UC Berkeley SkyLab/BAIR/NLP + Princeton + EPFL + Databricks (authors incl. Matei Zaharia). **NOT Anthropic.** §41 = no notability/heritage/locale rescue; Zaharia's fame does not rescue. #19 19a first StarTrail-org author. |
| **(b)** goal-relevance | **STRONG** (⚠️ MODERATE-reviewable) | **keys the tier.** RAG is core Goal-#1 agent substrate (the retrieval seam agents ground on) + it ships a first-class **Claude Code plugin `pixelbrowse`** (directly, zero-backend pilotable) + a sharp **hireui (Goal #2)** map (visual CV parsing vs OCR). STRONG-not-STRONGEST + the MODERATE-reviewable note below. |
| **(c)** substance / quality | **STRONG** | A real pipeline + a fine-tuned VLM embedding model + published LoRA + a live hosted API over 30M tiles + a Claude plugin + an arXiv paper with Berkeley/Databricks authors. Caveats §"Caveats". |
| **(d)** corpus cross-references | **STRONG** | claude-context v40 (vector-code RAG sibling) · crawl4ai v29 · the "structured-surface-not-raw-dump" thread (⭐ page-agent v199 text-dehydration CONTRAST) · Playwright-CDP browser cluster · the model/research-substrate tier (TimesFM v193 etc.) · hireui CV-parsing. |

**(b) STRONG vs MODERATE — the one judgment to record.** STRONG keys the tier because RAG is *on-domain* (retrieval is core agent tooling — unlike TimesFM's off-domain forecasting), the Claude Code plugin is a first-class, install-today bridge, and the hireui CV-parsing map is concrete. The **MODERATE-reviewable** reading: PixelRAG's primary artifact is a **research retrieval system whose hard AI is the upstream-fine-tuned VLM (Qwen3-VL)** over a **general-document (Wikipedia-QA) domain** a notch off the software-agent core — the TimesFM v193 model-substrate pole. **Either reading → GOAL-ALIGNED** (RAG is on-domain; **no §40 / no OFF-GOAL** needed — this is *not* the AIRI v210 / TimesFM v193 goal-adjacent situation, it's cleaner).

---

## Pattern outcome: NO MINT · counts UNCHANGED 46 / 11

PixelRAG is **corpus-first** (collision-clean, sanity-anchored hand-grep) for **visual / screenshot-based general-document RAG** — but that earns **no §C mint**, for two converging reasons:

1. **Corpus-first-for-a-technique ≠ a mintable §C capability class.** The §C vocabulary is tool/capability-shaped; a single **research retrieval system + a fine-tuned model** introducing a *modality variant* of RAG enters as a **corpus-knowledge data-point**, not a §C standalone — the **TimesFM v193 / meetily v196 / AIRI v210** discipline (§28 anti-inflation). PixelRAG's center of gravity (a paper + a fine-tuned VLM + a hosted API) sits on the **research/model-substrate pole**, not the fff-v194 / serve-sim-v183 "capability-layer-tool" pole.
2. **NOT world-first.** **ColPali** (2024) and **DSE — Document Screenshot Embedding** (arXiv 2406.11251, 2024) precede; visual-document retrieval is an established, active research area (ColPali→ColQwen2→ColFlor→ModernVBERT→DSE). Corpus-first ≠ world-first.

→ Recorded as a **corpus-knowledge data-point + a DEFERRED watch axis**: *"visual / pixel-space multimodal RAG (retrieval over rendered document screenshots) + pixel-surface agent perception (screenshot-not-HTML)."*

### ⚠️ The reviewable alternative (recorded, per the routine)

**§C-standalone MINT** — *"Visual / Screenshot-Based Multimodal Document RAG (retrieval + reading over rendered document images, no text conversion)"* — **N=1**, defensible on the **fff v194 / serve-sim v183 / page-agent v199** "corpus-first-for-surface, NOT world-first" precedent: a genuinely distinct retrieval **modality** (pixels, not text) that is unrepresented in the corpus's retrieval subjects (all code-context: §C#23 graph / claude-context v40 vector / fff v194 lexical / openwiki v195 doc-gen), and it is **consumable** (pip pipeline + hosted API + Claude plugin). **This alternative LOSES** to NO-MINT on: research-system-not-tool + §28 phantom-count + not-world-first (ColPali/DSE) + the TimesFM/meetily/AIRI domain-not-capability discipline. **Operator/audit may elect the mint at the ~v212 audit if the class recurs** (a 2nd visual-RAG subject → promotion-eligible).

**Either reading counts UNCHANGED 46/11; §C surface ≈49 unchanged.**

---

## Secondary observations (NOT minted)

- **pixelbrowse → the "structured-surface-not-raw-dump" perception thread** (pixel-modality member; ⭐ the page-agent v199 text-dehydration CONTRAST — thesis/antithesis). A Claude-Code-**plugin** distribution facet — **NOT a #18 B1-MCP subject** (the search API is REST/FastAPI; no MCP server evidenced — the "MCP-compatible" phrasing is not load-bearing and is not asserted).
- **claude-context v40 / crawl4ai v29** retrieval cross-refs (vector-code-RAG sibling / text-web-extraction alternative).
- **#19 19a** — first StarTrail-org / Berkeley-SkyLab / Matei-Zaharia-Databricks author cluster (institutional data-point).
- **#66 supply-chain** — install BENIGN (Apache-2.0, standard pip/plugin, Playwright Chromium download); real notes = hosted-API query egress (→ local FAISS for private data), typosquat forks (Puneetb/sp00ler/seco — StarTrail-org only), PII-in-screenshot artifacts.
- **LV #20 Token-Economy** — QUALIFIED-ADJACENT (pixel-reader vs parsed-text token/latency implications; the +18.1% is an **accuracy** claim, not a token-economy benchmark → **N stays 4**).

### NON-claims

NOT **#52** (~6.7k★/560 forks/4 releases/v0.4.0 page-stated §37.4 → velocity unestablishable) · NOT **#57** (cites ColPali/DSE/Qwen3-VL/FAISS/Qdrant — none corpus subjects; mentions ≠ recursion) · NOT **#18 B1-MCP** as a subject · NOT **world-first** · NOT a **new top-level pattern** (max #85) · NOT the **first model-subject** (fish-speech v20; PixelRAG fine-tunes one) · NOT a §C mint (declined; reviewable alt recorded).

---

## Tier

**Research retrieval system / model-substrate flavor** (the TimesFM v193 provisional-tier precedent — a fine-tuned model + a paper at the center). **Secondary reading: T2 Service** (self-hosted pip pipeline + FastAPI search + hosted API + a Claude plugin).

## Streak / §35

- Streak **GA:70 → GA:71** — **57 consecutive goal-aligned ships v153→v211**.
- **§35 CLEAR** — rolling-3-ship window {v209 GA, v210 GA, **v211 GA**} = 0 OFF-GOAL.
- inflation_check HELD: 0 mints; the §C mint DECLINED per §28 + recorded as the reviewable alternative; counts 46/11 unchanged; max top-level pattern #85; no N-bumps.

## Verification method (per `feedback_wiki_verify_independently_check_collisions`)

- **Source** hand-fetched: repo page + raw `README.md` + arXiv abstract 2606.28344.
- **Identity** by WebSearch (Berkeley SkyLab/BAIR + Princeton + EPFL + Databricks; Matei Zaharia; NOT Anthropic).
- **World-first landscape** by WebSearch (ColPali + DSE arXiv 2406.11251 precede).
- **Collision** by sanity-anchored hand-grep of `_state/` + `_patterns/` (anchors HIT: claude-context/crawl4ai/RAG/screenshot; subject terms 0 hits).
- **§C registry** hand-read (`_patterns/06`): no RAG / visual-RAG standalone; claude-context v40 = the vector-code sibling; fff v194 / serve-sim v183 / page-agent v199 mint precedents read directly.
- **No workflow / no subagent relied on** (shim overflows subagent context; the v202→v210 precedent).

## PILOT (one line)

Directly pilotable + on-goal for both goals — **read the seam, install the Claude plugin, borrow the modality.** ⭐ **A1 → C11 → D16.** Full 24-method menu in `(C) PixelRAG — Pilot Methods Menu.md`.
