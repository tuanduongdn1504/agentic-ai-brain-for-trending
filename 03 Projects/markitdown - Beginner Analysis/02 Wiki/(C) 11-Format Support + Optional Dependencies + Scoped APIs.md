# (C) 11-Format Support + Optional Dependencies + Scoped APIs

> **Type:** Entity — technical architecture
> **Parent:** [[(C) index]]
> **Sources:** README §Installation + §Usage + §Optional Dependencies + Security Considerations
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

markitdown supports **11+ file formats** via modular optional-dependency system + **4-tier narrowed-scope API hierarchy** for security. Combination enables flexible install sizes (install only what you need) + deployment-posture choice (permissive vs strict).

## 2. Supported formats

| Format | Base/Optional | Dep key |
|--------|---------------|---------|
| HTML | Base | — |
| CSV / JSON / XML | Base | — |
| ZIP (recursive) | Base | — |
| EPub | Base | — |
| **PDF** | Optional | `[pdf]`, `[az-doc-intel]` |
| **PowerPoint** | Optional | `[pptx]` |
| **Word** | Optional | `[docx]` |
| **Excel (xlsx)** | Optional | `[xlsx]` |
| **Excel (xls, older)** | Optional | `[xls]` |
| **Outlook (.msg)** | Optional | `[outlook]` |
| **Audio (WAV/MP3)** | Optional | `[audio-transcription]` |
| **YouTube URLs** | Optional | `[youtube-transcription]` |
| **Images (OCR)** | Optional via plugin | `markitdown-ocr` |
| **Azure Document Intel** | Optional | `[az-doc-intel]` |

**Quick install paths:**
- `pip install markitdown` — base formats only
- `pip install 'markitdown[pdf,docx]'` — selective
- `pip install 'markitdown[all]'` — everything

## 3. Pattern candidate #63 — Format-Scoped Optional Dependencies

**Definition:** Library uses pip extras (`[format]`) to scope install size per-feature.

**Why novel in corpus:**
- Most corpus frameworks install fixed set
- codymaster v12 has 79 skills but all-or-nothing
- markitdown: baseline ~5 formats; opt into heavy deps (PDF parsers, audio-transcription models, OCR stacks)

**Why important:**
- Deployment environments with size constraints (containers, Lambda) can install minimum
- Users avoid pulling unused dependencies (security + disk)
- Python-ecosystem pattern — may not generalize beyond Python

**Promotion criteria:** 2+ Python corpus frameworks with format-scoped optional deps (candidates: Unsloth v23, LlamaFactory v22 — both training-infra, may have similar patterns).

## 4. 4-tier narrowed-scope API hierarchy

### From narrowest to broadest:

```python
# Tier 1: Narrowest (user-provided stream)
md.convert_stream(stream, name_hint="optional-filename")

# Tier 2: User pre-fetched HTTP response
response = requests.get(url, timeout=10, stream=True)
md.convert_response(response)

# Tier 3: Local files only
md.convert_local("/path/to/file.pdf")

# Tier 4: Permissive (local + remote URIs + streams)
md.convert(input)
```

### Security threat addressed

**SSRF + privilege-escalation + path-traversal risks** when library has unrestricted I/O at caller-privilege level.

**Mitigation:** user picks narrowest method fitting their case.

### Use case matrix

| Scenario | Recommended API | Why |
|----------|-----------------|-----|
| Desktop user converting local files | `convert_local()` | Local-only, no network |
| Script fetching URL + converting | `convert_response()` | User controls `requests.get()` |
| Server streaming upload | `convert_stream()` | No path, no URL |
| Quick prototype | `convert()` | Permissive, flexible |

## 5. Why 4-tier API is architecturally unusual

### Typical library design (single entry point)

```python
import somelib
somelib.do_thing(input)  # magic dispatch internally
```

### markitdown design (explicit scope choice)

```python
md = MarkItDown()
md.convert(...) OR md.convert_local(...) OR md.convert_stream(...) OR md.convert_response(...)
```

**Tradeoff:**
- ❌ More surface area (4 methods vs 1)
- ❌ User must read Security section to understand nuance
- ✅ Server-side + untrusted-input contexts have narrower surface by default
- ✅ Least-privilege-API design principle

### Corpus novelty

**No prior corpus library** offers this hierarchy. notebooklm-py v7, graphify v16, TrendRadar v19 — all single entry points.

**Hypothesis:** pattern may emerge in security-conscious libraries. Too early for candidate registration (N=1).

## 6. `[all]` vs selective install

### `[all]` install size implications

Installing `'markitdown[all]'` pulls:
- PDF parsers (pdfminer-six + pypdf + possibly others)
- Office libs (python-docx + python-pptx + openpyxl)
- Audio libs (speech_recognition + pydub + OpenAI Whisper or equivalent)
- YouTube libs (youtube-transcript-api)
- Azure SDK (azure-ai-documentintelligence)
- OCR / image libs (PIL, Tesseract bindings optional)

**Estimated install:** 200-500 MB+ including model files.

### Selective install savings

If only PDF + DOCX needed: `pip install 'markitdown[pdf,docx]'` = ~50-100 MB.

**Deployment context:**
- AWS Lambda: 250 MB limit unzipped → selective install critical
- Docker container: smaller image = faster deploy
- Airgapped: minimize dep count

## 7. Plugin architecture (base + extension)

### Core-plus-plugin design

```python
md = MarkItDown(enable_plugins=True)
```

**Plugins extend without modifying core.** Registered via entry points.

### First-party plugin: `markitdown-ocr`

```bash
pip install markitdown-ocr
pip install openai
```

```python
md = MarkItDown(
    enable_plugins=True,
    llm_client=OpenAI(),
    llm_model="gpt-4o",
)
```

**Plugin contract reuses core DI** (`llm_client`/`llm_model`). Consistency pattern.

### Plugin discovery

- **GitHub hashtag `#markitdown-plugin`** (decentralized)
- Authors add hashtag to repo
- `markitdown --list-plugins` lists installed

**No centralized marketplace** (unlike spec-kit, OMC).

## 8. CLI + Python API + Docker = 3 surfaces

### CLI surface

```bash
markitdown file.pdf                           # stdout
markitdown file.pdf -o output.md              # file
markitdown --use-plugins file.pdf             # plugins on
markitdown file.pdf -d -e "<az-endpoint>"     # Azure
cat file.pdf | markitdown                     # stdin
```

### Python API surface

Full programmatic access as documented Cluster #3.

### Docker surface

```sh
docker build -t markitdown:latest .
docker run --rm -i markitdown:latest < file.pdf > output.md
```

**Stdin + stdout interface** — pipe-friendly for Docker-based workflows.

### Why 3 surfaces matter

- **CLI:** shell pipelines, simple scripts
- **Python API:** library integration (AutoGen, LangChain, custom agents)
- **Docker:** isolated deployment, CI/CD integration

Each surface serves different operator context. Corporate-quality tool trait.

## 9. uv support (Astral toolchain)

README explicit:
```bash
uv venv --python=3.12 .venv
source .venv/bin/activate
uv pip install 'markitdown[all]'
```

**Corpus uv-support observations (N=2):**
- spec-kit v17 (first `uv tool install`)
- markitdown v28 (uv venv + uv pip)

**Observation:** Microsoft corporate AutoGen Team adopts modern Python tooling (uv + hatch). Not yet pattern but trend.

## 10. Security Considerations formalization

### Threat scenarios

From README §Security Considerations:

1. **Path-traversal via `convert(user_path)`** — user-controlled paths
2. **SSRF via `convert(user_url)`** — attacker submits `http://169.254.169.254/...`
3. **Zip-bomb via ZIP recursion** — not explicitly mentioned but known risk
4. **XXE via XML parsing** — XML input untrusted

### Mitigations (explicit in README)

1. **Sanitize inputs:** validate path + URI scheme + destination
2. **Call narrowest API:** least-privilege
3. **Block network destinations:** loopback, link-local, metadata-service

### Mitigations (implicit)

- CLA process ensures contributor accountability
- Pre-commit hooks enforce code hygiene
- Hatch test suite

### Corporate governance strength

Microsoft AutoGen Team takes security seriously — markitdown is **strongest security documentation in corpus** for a T4 bridge library.

## 11. Related concepts

- [[(C) Cluster — README + 11 format support + 3 surfaces]]
- [[(C) Cluster — AutoGen Team origin + Microsoft ecosystem + plugin discovery]]
- [[(C) Cluster — LLM-client DI + Azure Document Intelligence + security API narrowing]]
- [[(C) T4 Extends to N=5 + Storm Bear Vault Applicability + Meta]]
- Pattern candidate #63 Format-Scoped Optional Dependencies
- Pattern candidate #61 LLM-Client DI Pattern
- Pattern candidate #62 Hashtag-Based Plugin Discovery
- Pattern #12 Governance-Depth (reinforced)
- Pattern #24 SECURITY.md (compliance via README section + probable SECURITY.md)

## 12. References

- README.md §Installation, §Usage, §Optional Dependencies, §Plugins, §Python API, §Docker, §Security Considerations
- Microsoft AutoGen ecosystem context
- PyPI: `pip install markitdown`

## 13. Edges + limitations

- **Plugin hashtag discovery** has no quality signal (abandoned plugins rank equally)
- **`[all]` install size** (~200-500 MB+) may surprise users
- **Narrowed-scope API** requires security-section awareness (discoverability issue)
- **Base formats (HTML/CSV/JSON/XML) limited** to unopinionated conversion
- **No batch API in README** — single file per call (implicit in `convert()` signature)
- **Error handling undocumented** in README — users discover via trial
- **Conda instructions mention but uv/hatch preferred** — mixed Python-tooling guidance

---

**11+ format support via modular optional-dependency system + 4-tier narrowed-scope API hierarchy = corporate-grade library architecture. Registers Pattern candidate #63 Format-Scoped Optional Dependencies. Contributes to Pattern #12 Governance-Depth and Pattern #24 SECURITY.md standards.**
