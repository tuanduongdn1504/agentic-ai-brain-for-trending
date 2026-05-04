# markitdown - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`microsoft/markitdown`](https://github.com/microsoft/markitdown) — **"Python tool for converting files and office documents to Markdown."**

**114,339 stars (#3 corpus — behind only build-your-own-x 491K outside + system-prompts-leaks v21 135K outside; surpasses spec-kit v17 89.2K as new largest non-outside-scope wiki), 7,446 forks (6.5%), MIT, Python, main-branch, created 2024-11-13 (~17 months old), pushed 2026-04-20, 4.2 MB, 621 open issues**. Organization: **Microsoft** (corporate) via **AutoGen Team** (explicit README badge). **2nd Microsoft entrant** in Storm Bear corpus after v6 ai-agents-for-beginners (T3). PyPI: `pip install 'markitdown[all]'`.

**Scope status: T4 Agent-as-bridge — 5th T4 entrant.** T4 now largest non-T1 tier at N=5.

**Tagline:** *"A lightweight Python utility for converting various files to Markdown for use with LLMs and related text analysis pipelines."*

**Core product — 11+ file format → Markdown converter for LLM pipelines:**

| Format | Support mechanism |
|--------|------------------|
| PDF | Native + Azure Document Intelligence optional |
| PowerPoint (PPTX) | Native + LLM vision for image descriptions |
| Word (DOCX) | Native |
| Excel (XLSX/XLS) | Native |
| Images (JPG/PNG) | EXIF + OCR + LLM vision |
| Audio (WAV/MP3) | EXIF + speech transcription |
| HTML | Native |
| CSV/JSON/XML | Native |
| ZIP | Iterates over contents |
| YouTube URLs | Transcript fetching |
| EPub | Native |

**Key architecture:**
- **3-surface deployment:** CLI (`markitdown path.pdf`) + Python API (`MarkItDown().convert()`) + Docker
- **Plugin ecosystem:** `#markitdown-plugin` GitHub hashtag discovery + `markitdown-sample-plugin` + `markitdown-ocr` first-party OCR plugin
- **LLM-client DI pattern:** `MarkItDown(llm_client=OpenAI(), llm_model="gpt-4o")` for optional vision features
- **Azure Document Intelligence** bridge: `-d -e "<endpoint>"` flag or Python `docintel_endpoint=` param
- **Optional dependencies per-format:** `[pdf]`, `[docx]`, `[xlsx]`, `[audio-transcription]`, `[youtube-transcription]`, `[az-doc-intel]`, `[all]`
- **Narrowed-scope APIs:** `convert()` (broad) / `convert_local()` (file only) / `convert_stream()` / `convert_response()` — security-motivated
- **Built by AutoGen Team** — Microsoft AutoGen (agent framework) team maintains

**v2 Routine 12-axis classification:**

| Axis | Value |
|------|-------|
| **Tier** | **T4 Agent-as-bridge (5TH entrant)** |
| **Archetype** | **Official-corporate-narrow-utility-bridge** (NEW T4 variant — distinct from T4a gws broad 11 services) |
| **Scale tier** | **114K stars** (#3 in corpus, #1 non-outside-scope; viral at ~220 stars/day) |
| **Primary lang** | Python 3.10+ |
| **Packaging** | pip (`markitdown[all]`) + Docker + uv-compatible |
| **Origin story** | AutoGen Team tool; optimizes LLM document ingestion |
| **Methodology** | Structural-preservation markdown conversion for LLM consumption |
| **Governance files** | Microsoft CLA + Microsoft OSS Code of Conduct + SECURITY.md (inferred) |
| **Feature count** | 11+ file formats, 3 surfaces, plugin ecosystem |
| **i18n** | English-only README |
| **Intellectual influence** | AutoGen Team internal; textract mentioned as comparable prior art |
| **Agent platforms** | AutoGen + LangChain integration (topics tag) |

**Tier placement rationale:** T4 Agent-as-bridge — utility that bridges office/PDF file world to LLM markdown world. Not autonomous (not T5); not assistant-framework (not T1); not deployment platform (not T2); not educational curriculum (not T3). Classic T4 single-purpose tool.

**T4 extends to N=5** — T4 becomes 3rd tier to reach N≥5 (after T1 N=9 v27 + T4 now N=5 v28). T2/T3 remain at N=2.

**v28 pattern implications preview:**
- **Pattern #17 Ecosystem-Layer — 8th data point + variant 5 validation at N=2** — Microsoft joins HuggingFace as 2nd ecosystem-scale commercial platform variant (prior: only HuggingFace at v26 N=1). Structurally-unambiguous promotion candidate for variant 5.
- **Pattern #27 Community-Viral 6th data point** — 114K/17mo = ~220 stars/day; corporate-amplified not community-organic
- **Pattern #20 Solo-Scale Ceiling** — Microsoft corporate-scale 114K reinforces Pattern #20 "corporate breaks solo-scale-ceiling" dictionary observation
- **Pattern #2 Distribution Evolution** — pip + Docker + AutoGen extension + LangChain integration = multi-distribution (corporate standard)
- **Pattern #12 Governance-Depth** — Microsoft CLA + OSS Code of Conduct + explicit Security Considerations = corporate-depth governance
- **Pattern #24 SECURITY.md** — README has explicit Security Considerations section; likely has SECURITY.md
- **Pattern #28 Multi-Provider AI Support** — `llm_client` DI accepts OpenAI-compatible clients + Azure Document Intelligence = 4th data point
- **Pattern #29 License-Category Diversity** — MIT (standard)
- **NEW candidates at v28:**
  - **#60 AutoGen-Extension Ecosystem Archetype** — Microsoft AutoGen agent framework spawns official extensions (markitdown + others). Ecosystem-within-ecosystem pattern. Distinct from HuggingFace 14+ products because AutoGen is itself a product with extensions, not platform with sub-tools.
  - **#61 LLM-Client DI Pattern** — library accepts `llm_client` as dependency-injected param for optional LLM features; contract-based integration (OpenAI-compatible interface). Distinct from Pattern #28 multi-provider (which is provider routing): #61 is library-pluggability-interface.
  - **#62 Hashtag-Based Plugin Discovery** — `#markitdown-plugin` GitHub hashtag for plugin discovery (decentralized). Distinct from Pattern #7 marketplace-emergence (centralized).
  - **#63 Format-Scoped Optional Dependencies** — `pip install 'markitdown[pdf,docx]'` per-format deps. Reduces baseline install size. Might be Python-ecosystem pattern or corpus-novel.

## Claude's Role

Claude là wiki maintainer, chạy bằng routine `llm-wiki-routine-v2.md` (**28th auto-execution, 10th v2 routine execution**):

- **Ingest sources via WebFetch + API probe** — README (282 lines) + inferred governance (Microsoft standard)
- **Cross-reference với 27 sibling wikis** — primarily T4 peers (gws v13 / notebooklm-py v7 / graphify v16 / TrendRadar v19) + v6 ai-agents-for-beginners (Microsoft peer) + Pattern #17 peers (HuggingFace v26)
- **Phase 4b = T4 5-way comparison + Pattern #17 variant 5 N=2 validation + 4 new candidates**
- **Beginner angle** — Python developer converting Office docs to markdown; Storm Bear direct-use for Scrum-coaching-doc ingestion into vault

**Prime directive:** Outcome = wiki + T4 extends to N=5 + Pattern #17 variant 5 promotion evidence + 4 new candidates + Microsoft 2nd corpus entrant validation.

## Process — routine `llm-wiki-routine-v2.md`

7 phases. 10th v2 routine execution. Phase 4b = T4 5-way comparison + ecosystem-scale commercial platform variant validation.

## Key People / Organization

- **Microsoft / AutoGen Team** — builders (explicit README badge)
- **Cross-project:** 27 sibling wikis. This is 28th = T4 extension + Microsoft 2nd entrant.

## Folder Structure

```
markitdown - Beginner Analysis/
├── CLAUDE.md
├── 00 Sources/
├── 01 Analysis/
├── 02 Wiki/              ← 3 cluster summaries + 4 entity pages + index + log
├── 03 Published/         ← Beginner guide + Phase 4b T4 5-way
├── 04 Reviews/           ← Iteration log v28
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ VN + 13-section format
- **Cross-reference 27 siblings MANDATORY** — especially T4 peers + v6 Microsoft + v26 HF (Pattern #17 variant 5 peer)
- **Pattern Library direct update** — 4 new candidates + Pattern #17 variant 5 N=2 validation (potential promotion) + T4 N=5

## Current Status

> **Last updated:** 2026-04-22
> **Status:** 🟡 Routine v2 auto-execute IN PROGRESS — 28th LLM Wiki, 10th v2 execution, T4 N=5 extension, Pattern #17 variant 5 structural validation

### Expected milestones

- [x] Phase 0 Pre-flight (probe + consolidation guard PASS at 0.93:1)
- [x] Phase 1 Scaffold (folder + CLAUDE.md)
- [ ] Phase 2 Source ingestion (3 cluster summaries)
- [ ] Phase 3 Entity pages (4)
- [ ] Phase 4a Beginner published guide
- [ ] Phase 4b **T4 5-way + Pattern #17 variant 5 N=2 validation + 4 new candidates**
- [ ] Phase 5 Iteration log v28 + PATTERN_LIBRARY.md update
- [ ] Phase 6 Vault file updates (root GOALS.md + CLAUDE.md)
