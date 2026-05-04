# (C) Cluster — README + 11 format support + 3 surfaces

> **Type:** Source cluster summary
> **Source:** README.md (282 lines)
> **Coverage:** Format support, CLI + Python API + Docker surfaces, installation, optional deps, plugin system, Azure integration, security considerations
> **Parent:** [[(C) index]]

---

## 1. Summary

markitdown is a **lightweight Python utility for converting files to Markdown for LLM consumption**. Built by Microsoft AutoGen Team. 11+ formats supported. 3 deployment surfaces (CLI + Python API + Docker). Plugin ecosystem via `#markitdown-plugin` hashtag. Optional LLM vision integration via `llm_client` DI. Azure Document Intelligence bridge.

**Comparable to:** `textract` (deanmalmgren/textract) — README explicit comparison. Difference: markitdown **preserves document structure** (headings/lists/tables/links) via markdown; textract is plain-text extraction.

## 2. 11+ file format support

| Format | Mechanism | Optional dep |
|--------|-----------|--------------|
| **PDF** | Native + Azure Document Intelligence | `[pdf]`, `[az-doc-intel]` |
| **PowerPoint (PPTX)** | Native + LLM vision for image descriptions | `[pptx]` |
| **Word (DOCX)** | Native | `[docx]` |
| **Excel (XLSX/XLS)** | Native | `[xlsx]`, `[xls]` |
| **Images (JPG/PNG)** | EXIF metadata + OCR + LLM vision | `[all]` |
| **Audio (WAV/MP3)** | EXIF metadata + speech transcription | `[audio-transcription]` |
| **HTML** | Native | (base) |
| **CSV** | Native | (base) |
| **JSON** | Native | (base) |
| **XML** | Native | (base) |
| **ZIP** | Iterates over contents recursively | (base) |
| **YouTube URLs** | Transcript fetching | `[youtube-transcription]` |
| **EPub** | Native | (base) |
| **Outlook messages** | Native | `[outlook]` |

**Why Markdown (README §2):**
> *"Mainstream LLMs, such as OpenAI's GPT-4o, natively 'speak' Markdown, and often incorporate Markdown into their responses unprompted. This suggests that they have been trained on vast amounts of Markdown-formatted text, and understand it well. As a side benefit, Markdown conventions are also highly token-efficient."*

## 3. 3-surface deployment

### CLI

```bash
markitdown path-to-file.pdf > document.md
markitdown path-to-file.pdf -o document.md
cat path-to-file.pdf | markitdown
markitdown path-to-file.pdf -d -e "<azure-endpoint>"
markitdown --list-plugins
markitdown --use-plugins path-to-file.pdf
```

### Python API

```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False)
result = md.convert("test.xlsx")
print(result.text_content)
```

**With LLM vision:**
```python
from markitdown import MarkItDown
from openai import OpenAI

md = MarkItDown(llm_client=OpenAI(), llm_model="gpt-4o")
result = md.convert("example.jpg")
print(result.text_content)
```

**With Azure Document Intelligence:**
```python
md = MarkItDown(docintel_endpoint="<endpoint>")
result = md.convert("test.pdf")
```

### Docker

```sh
docker build -t markitdown:latest .
docker run --rm -i markitdown:latest < ~/your-file.pdf > output.md
```

**3-surface pattern observed at corpus N=3+:** gws v13 (CLI + Python + services) + OMC v27 (CLI + in-session + Docker) + markitdown v28. Emerging corpus pattern.

## 4. Installation options

**Standard pip:**
```bash
pip install 'markitdown[all]'
```

**From source:**
```bash
git clone git@github.com:microsoft/markitdown.git
cd markitdown
pip install -e 'packages/markitdown[all]'
```

**uv (documented!):**
```bash
uv venv --python=3.12 .venv
source .venv/bin/activate
uv pip install 'markitdown[all]'
```

**Conda:**
```bash
conda create -n markitdown python=3.12
conda activate markitdown
```

**Per-format installs** (reduce baseline size):
```bash
pip install 'markitdown[pdf, docx, pptx]'
```

**Available optional deps:**
- `[all]` — all optional
- `[pptx]` / `[docx]` / `[xlsx]` / `[xls]` / `[pdf]` — format-specific
- `[outlook]` — Outlook `.msg`
- `[az-doc-intel]` — Azure Document Intelligence
- `[audio-transcription]` — WAV/MP3
- `[youtube-transcription]` — YouTube transcripts

**Pattern candidate #63 Format-Scoped Optional Dependencies** — novel pip-extras usage for per-format install.

## 5. Plugin ecosystem

### Discovery

**Decentralized via GitHub hashtag `#markitdown-plugin`.** Authors add hashtag to repo; users search GitHub for discovery.

**Command:** `markitdown --list-plugins`.

**Plugins disabled by default** — `--use-plugins` flag to enable.

### First-party example: `markitdown-ocr`

OCR plugin using LLM vision:
```bash
pip install markitdown-ocr
pip install openai  # or OpenAI-compatible client
```

```python
from markitdown import MarkItDown
from openai import OpenAI

md = MarkItDown(
    enable_plugins=True,
    llm_client=OpenAI(),
    llm_model="gpt-4o",
)
result = md.convert("document_with_images.pdf")
```

**Key architecture:** plugin reuses `llm_client`/`llm_model` DI contract from core MarkItDown. If no client provided, OCR silently skipped.

### Sample plugin for devs

`packages/markitdown-sample-plugin` — reference implementation for plugin authors.

**Pattern candidate #62 Hashtag-Based Plugin Discovery** — distinct from centralized marketplace (spec-kit 80+ marketplace / OMC plugin marketplace native / BMAD community modules).

## 6. Azure Document Intelligence integration

Microsoft Azure bridge:
```bash
markitdown path-to-file.pdf -o document.md -d -e "<endpoint>"
```

or Python:
```python
md = MarkItDown(docintel_endpoint="<endpoint>")
```

**Ecosystem signal:** Microsoft corporate product publishes open-source tool that bridges to Microsoft's commercial AI service. Pattern #17 ecosystem-scale commercial platform behavior.

## 7. Narrowed-scope API pattern (security-motivated)

README Security Considerations section documents:

> *"MarkItDown's `convert()` method is intentionally permissive and can handle local files, remote URIs, and byte streams. If your application only needs to read local files, call `convert_local()` instead. If you need more control over URI fetching, call `requests.get()` yourself and pass the response object to `convert_response()`. For maximum control, open a stream to the input you want converted and call `convert_stream()`."*

**API hierarchy (narrowest → broadest):**
1. `convert_stream(stream)` — maximum control
2. `convert_response(response)` — user controls fetching
3. `convert_local(path)` — local files only
4. `convert(input)` — permissive (local + remote URI + streams)

**Security philosophy:** "Call only the conversion method you need" = least-privilege API design. Novel in corpus (most libraries have single permissive entry point).

## 8. LLM-client dependency injection

Core contract:
```python
MarkItDown(llm_client=<OpenAI-compatible>, llm_model="gpt-4o", llm_prompt="<optional>")
```

**Contract-based integration:**
- Library doesn't hard-code OpenAI SDK
- User provides OpenAI-compatible client (`openai.OpenAI()` or Azure OpenAI or any compatible)
- Features using LLM are **optional** (image descriptions in pptx + OCR via plugin)
- If no client → features silently skipped; core conversion still works

**Pattern candidate #61 LLM-Client DI Pattern** — library-pluggability-interface distinct from Pattern #28 provider-routing.

## 9. uv support (2nd corpus mention)

README explicitly mentions `uv venv` + `uv pip install` as install path.

**Corpus history:**
- spec-kit v17 (first `uv tool install` mention)
- **markitdown v28 (second)**

**Emerging:** uv (Astral's Rust-based Python tooling) becoming corpus-visible. Not yet confirmed pattern but N=2 trend.

## 10. Security considerations (explicit README section)

**Noted concerns:**
1. **Process-privilege I/O:** markitdown accesses resources at calling-process privilege level (`open()` / `requests.get()` style)
2. **Untrusted input sanitization:** if input may come from untrusted source, validate + restrict (path restrictions, URI scheme limits, block loopback/link-local/metadata-service addresses)
3. **Narrowest-API principle:** prefer `convert_local()` over `convert()` when possible

**Corporate governance signal:** explicit security section + warning callout at README top = Microsoft corporate security posture.

## 11. Contributing process

- **CLA required:** Microsoft Contributor License Agreement (standard Microsoft OSS practice)
- **Code of Conduct:** Microsoft Open Source Code of Conduct
- **Testing:** `hatch test` + pre-commit checks
- **Devcontainer provided**
- **Labels:** "open for contribution" + "open for reviewing" issues/PRs

**Pattern #12 Governance-Depth:** Microsoft CLA + Code of Conduct + explicit security section + devcontainer + test infrastructure = corporate-depth governance.

## 12. Cross-wiki signals

- **Pattern #17 Ecosystem-Layer 8th data point + variant 5 N=2 validation** — Microsoft joins HuggingFace as ecosystem-scale commercial platform (variant 5)
- **Pattern #27 Community-Viral 6th data point** — 114K stars, corporate-amplified (not organic-community like agency-agents)
- **Pattern #28 Multi-Provider AI Support 4th data point** — `llm_client` DI + Azure DocIntel dual-integration
- **Pattern #12 Governance-Depth** — Microsoft corporate-depth pattern continues (matches v6 + gws v13 + spec-kit v17)
- **Pattern candidate #60 AutoGen-Extension Ecosystem Archetype** — markitdown is official AutoGen Team product
- **Pattern candidate #61 LLM-Client DI** — library-pluggability interface
- **Pattern candidate #62 Hashtag-Based Plugin Discovery** — decentralized
- **Pattern candidate #63 Format-Scoped Optional Dependencies** — pip extras per-format

## 13. Edges + limitations

- **No AGENTS.md** — library, not agent framework (reasonable Pattern #22 exemption)
- **English-only README** — Microsoft corporate defaults EN
- **621 open issues** — high backlog reflects 114K-user scale
- **Corporate CLA** — contribution friction for casual contributors
- **3-surface deployment complexity** — 3 APIs means 3× docs + 3× test surface
- **Plugin hashtag discovery limitations** — no quality signal (stars / age / maintainer); spec-kit-style marketplace has better UX

---

**Cluster signal:** markitdown is corporate-produced narrow-utility bridge at enterprise-scale (114K stars). Microsoft AutoGen Team ownership + Azure integration + corporate governance + explicit security posture = professional-grade bridge tool distinct from corpus's solo-maintainer T4 peers (notebooklm-py, graphify, TrendRadar).
