# (C) markitdown — Hướng dẫn cho người mới / Beginner's Guide

> **Project:** [microsoft/markitdown](https://github.com/microsoft/markitdown)
> **Tagline:** *"Python tool for converting files and office documents to Markdown."*
> **Audience:** Developer chuyển Office/PDF documents sang Markdown cho LLM consumption
> **Language:** Bilingual VN/EN
> **Complexity:** Thấp — install pip + 1 lệnh CLI. Nâng cao: LLM vision + Azure DocIntel.

---

## 1. markitdown là gì? / What is markitdown?

**VN:** markitdown là Python utility của **Microsoft AutoGen Team** (đội xây AutoGen agent framework). Mục đích: **convert files sang Markdown cho LLM consumption.** Hỗ trợ 11+ formats: PDF, PowerPoint, Word, Excel, Images (OCR), Audio (transcription), HTML, CSV/JSON/XML, ZIP, YouTube URLs, EPub.

**EN:** markitdown is a lightweight Python utility by Microsoft AutoGen Team for converting files to Markdown for LLM consumption. 11+ formats supported.

**Key stats:**
- **114,339 GitHub stars** (#3 in Storm Bear corpus, #1 non-outside-scope)
- **MIT license**
- **Python 3.10+**
- **PyPI:** `pip install 'markitdown[all]'`
- **Maintained by:** Microsoft AutoGen Team (README badge explicit)
- **Docker supported**

## 2. Vì sao Markdown? / Why Markdown?

README §Why Markdown:
> *"Mainstream LLMs như GPT-4o natively 'speak' Markdown... suggest họ đã được train trên vast amounts of Markdown-formatted text. Markdown conventions cũng token-efficient."*

**Lợi ích:**
1. **LLM-friendly** — models hiểu Markdown natively
2. **Token-efficient** — ít tokens hơn HTML/XML
3. **Structure-preserving** — giữ được headings, lists, tables, links
4. **Human-readable** — vẫn đọc được trong editor thường

## 3. Cài đặt / Installation

### Cách 1: pip (all formats)

```bash
pip install 'markitdown[all]'
```

**Cài tất cả optional deps** (~200-500 MB). Đủ cho hầu hết use cases.

### Cách 2: pip selective

```bash
pip install 'markitdown[pdf, docx, pptx]'
```

**Cài chỉ formats cần** (~50-100 MB). Phù hợp Lambda/Docker/airgapped.

**Available extras:**
- `[all]` — tất cả
- `[pdf]`, `[docx]`, `[pptx]`, `[xlsx]`, `[xls]` — Office formats
- `[outlook]` — Outlook .msg
- `[audio-transcription]` — WAV/MP3
- `[youtube-transcription]` — YouTube transcripts
- `[az-doc-intel]` — Azure Document Intelligence

### Cách 3: uv (modern Python tooling)

```bash
uv venv --python=3.12 .venv
source .venv/bin/activate
uv pip install 'markitdown[all]'
```

### Cách 4: conda

```bash
conda create -n markitdown python=3.12
conda activate markitdown
pip install 'markitdown[all]'
```

### Cách 5: Docker

```bash
docker build -t markitdown:latest .
docker run --rm -i markitdown:latest < file.pdf > output.md
```

## 4. Sử dụng cơ bản / Basic usage

### CLI

**Convert + output stdout:**
```bash
markitdown file.pdf
```

**Convert + save file:**
```bash
markitdown file.pdf -o output.md
```

**Pipe từ stdin:**
```bash
cat file.pdf | markitdown
```

### Python API

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("document.xlsx")
print(result.text_content)
```

## 5. Advanced — LLM vision cho images

**Use case:** PDF có embedded images + bạn muốn LLM mô tả nội dung images.

```python
from markitdown import MarkItDown
from openai import OpenAI

md = MarkItDown(
    llm_client=OpenAI(),           # OpenAI-compatible client
    llm_model="gpt-4o"              # model name
)
result = md.convert("document_with_images.pdf")
print(result.text_content)
```

**Cost:** mỗi image → 1 OpenAI call ($0.001-0.01 tùy model).

**Alternative clients** (OpenAI-compatible):
- Azure OpenAI (corporate)
- OpenRouter (aggregator)
- LiteLLM (abstraction)
- Anthropic via shim
- Ollama local mode

## 6. Advanced — Azure Document Intelligence

**Use case:** PDF phức tạp (forms, handwriting, complex layouts) cần high-fidelity OCR.

**CLI:**
```bash
markitdown file.pdf -o output.md -d -e "<az-doc-intel-endpoint>"
```

**Python:**
```python
md = MarkItDown(docintel_endpoint="<endpoint>")
result = md.convert("complex.pdf")
```

**Cost:** Azure DocIntel paid service (~$1.50 per 1000 pages).

**Alternative to Azure:** OpenAI vision via `llm_client` DI đã đủ cho nhiều use cases.

## 7. Advanced — Plugin system

### List installed plugins

```bash
markitdown --list-plugins
```

### Use plugins

```bash
markitdown --use-plugins file.pdf
```

### Find plugins

Tìm GitHub theo hashtag `#markitdown-plugin`.

### First-party plugin: markitdown-ocr

**Install:**
```bash
pip install markitdown-ocr
pip install openai
```

**Use:**
```python
from markitdown import MarkItDown
from openai import OpenAI

md = MarkItDown(
    enable_plugins=True,
    llm_client=OpenAI(),
    llm_model="gpt-4o",
)
result = md.convert("scanned.pdf")
```

## 8. Security — Narrowed-scope APIs

**markitdown có 4 APIs với độ permissive khác nhau:**

```python
# Tier 1: Narrowest (stream user-provided)
md.convert_stream(stream)

# Tier 2: User pre-fetched response
response = requests.get(url, timeout=10)
md.convert_response(response)

# Tier 3: Local files only (no network)
md.convert_local("/path/to/file.pdf")

# Tier 4: Permissive (everything)
md.convert(input)
```

**Nguyên tắc:** "Call only the conversion method you need."

**Trong server-side apps với untrusted input:**
- Nếu chỉ đọc local files: `convert_local()`
- Nếu fetch URLs: `convert_response()` để control timeout/size/destinations
- Nếu stream: `convert_stream()` — minimum surface

**Tránh `convert()` với user-controlled input** (SSRF + path-traversal risks).

## 9. Lộ trình 2 tuần cho beginner / 2-week roadmap

### Tuần 1: Basics

- **Day 1:** `pip install 'markitdown[all]'` + convert 1 PDF
- **Day 2:** Convert 3-5 files khác nhau formats (DOCX, PPTX, XLSX)
- **Day 3:** Python API với `from markitdown import MarkItDown`
- **Day 4:** Enable LLM vision với OpenAI API key
- **Day 5:** Test với multiple file types + document observations
- **Weekend:** Convert personal documents → markdown folder

### Tuần 2: Advanced

- **Day 8:** Selective install `[pdf,docx]` vs `[all]`
- **Day 9:** Explore plugins via `#markitdown-plugin` hashtag
- **Day 10:** Narrowed-scope APIs nếu build server-side
- **Day 11:** Azure Document Intelligence test (optional, requires Azure account)
- **Day 12:** Docker deployment
- **Day 13:** Integration vào Claude Code workflow
- **Day 14:** Write summary của markitdown capabilities cho team

## 10. Storm Bear use cases — RẤT CAO

**Storm Bear operator = Scrum coach + developer.** Document formats phổ biến:
- Sprint Review decks (PPTX)
- Retrospective templates (PPTX/DOCX)
- Scrum certification study materials (PDF)
- Client proposals (DOCX)
- Reference books (PDF)

### Use case 1: Ingest Scrum materials vào vault

```bash
markitdown sprint-review-template.pptx -o /vault/00\ Notes/sprint-review.md
markitdown retrospective-guide.docx -o /vault/05\ Skills/retro.md
markitdown scrum-cert-study.pdf -o /vault/02\ Wiki/scrum-notes.md
```

### Use case 2: Client document intake

```bash
markitdown client-charter.docx -o /vault/clients/charter.md
markitdown audit-report.pdf -o /vault/clients/audit.md
```

### Use case 3: Audio notes transcription

```bash
pip install 'markitdown[audio-transcription]'
markitdown lecture.mp3 -o /vault/notes/lecture.md
```

### Use case 4: Storm Bear corpus extension

markitdown có thể dùng trong routine v2 Phase 2 để fetch + convert non-markdown sources (academic PDFs, PPTX slide decks).

## 11. Ưu điểm / Pros

- ✅ **Microsoft corporate stability** — well-maintained, long-term viability
- ✅ **MIT license** — commercial use OK
- ✅ **11+ formats** broadest coverage in corpus
- ✅ **3 deployment surfaces** (CLI + Python + Docker)
- ✅ **Plugin ecosystem** — extensible via `markitdown-plugin` hashtag
- ✅ **LLM vision integration** optional via `llm_client` DI
- ✅ **Security-conscious** — narrowed-scope APIs + documented threat model
- ✅ **Format-scoped installs** — cài chỉ cần thiết, tiết kiệm size
- ✅ **Active development** — 114K stars, 621 open issues, push daily

## 12. Caveats / Nhược điểm

- ⚠️ **Microsoft CLA** required cho contributions
- ⚠️ **English-only README** — không có VN/CN translations
- ⚠️ **Plugin hashtag discovery** không có quality signals
- ⚠️ **[all] install size** lớn (~200-500 MB)
- ⚠️ **Azure DocIntel paid** (optional nhưng cost-opaque)
- ⚠️ **Narrowed-scope API discoverability** thấp — users lãnh `convert()` dễ missed Security section
- ⚠️ **621 open issues** triage backlog lớn

## 13. References

- [GitHub: microsoft/markitdown](https://github.com/microsoft/markitdown)
- [PyPI: markitdown](https://pypi.org/project/markitdown/)
- [AutoGen](https://github.com/microsoft/autogen)
- [Azure Document Intelligence docs](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)
- [uv (Python tooling)](https://github.com/astral-sh/uv)

**Storm Bear wiki cross-refs:**
- [[(C) 11-Format Support + Optional Dependencies + Scoped APIs]]
- [[(C) Microsoft AutoGen Team + Corporate Governance + Pattern 17 Variant 5 Validation]]
- [[(C) LLM-Client DI Pattern + Plugin Hashtag Discovery + 4 New Candidates]]
- [[(C) T4 Extends to N=5 + Storm Bear Vault Applicability + Meta]]

---

**markitdown v28 = T4 bridge framework #5 trong Storm Bear corpus. Microsoft corporate quality + utility-focus + LLM-integration-optional = high Storm Bear operator applicability. Pilot priority #4. Direct utility for Scrum documentation → vault markdown ingestion.**
