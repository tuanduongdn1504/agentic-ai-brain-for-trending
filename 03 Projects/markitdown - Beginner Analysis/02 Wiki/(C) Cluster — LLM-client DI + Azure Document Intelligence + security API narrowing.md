# (C) Cluster — LLM-client DI + Azure Document Intelligence + security API narrowing

> **Type:** Source cluster summary
> **Sources:** README Python API examples + Azure integration + Security Considerations section
> **Coverage:** LLM-client DI pattern, Azure Document Intelligence integration, narrowed-scope API hierarchy, security-motivated design
> **Parent:** [[(C) index]]

---

## 1. Summary

markitdown exposes 3 architectural patterns worth dedicated analysis: (1) **LLM-client dependency injection** for optional vision features, (2) **Azure Document Intelligence bridge** as Microsoft ecosystem integration, (3) **narrowed-scope API hierarchy** as security-motivated design. Together they form **corporate-grade library architecture** distinct from typical solo-T4 library (notebooklm-py, graphify).

## 2. LLM-client DI pattern (Pattern candidate #61)

### Contract

```python
MarkItDown(
    llm_client=<OpenAI-compatible client>,
    llm_model="<model-name>",
    llm_prompt="<optional custom prompt>"
)
```

### Interface requirements

- `llm_client` = OpenAI-compatible client (duck-typed)
  - Accepts `openai.OpenAI()`, `Azure OpenAI`, `OpenRouter`, `LiteLLM`, etc.
  - Must implement `.chat.completions.create(...)` interface
- `llm_model` = model string (e.g., `gpt-4o`)
- `llm_prompt` = optional custom prompt for image descriptions

### Behavior

- If `llm_client` provided → LLM features active (image descriptions in PPTX, OCR via plugin)
- If `llm_client=None` → features silently skipped; core conversion works without

### Why this is pattern-worthy

**Contrast with hard-coded SDK dependency:**
- ❌ Library `import openai` at top — forces openai dep + coupling
- ❌ Library `from langchain.llms import OpenAI` — forces langchain dep
- ✅ markitdown: `llm_client` is DI param; no hard dep

**Contrast with Pattern #28 Multi-Provider AI Support:**
- Pattern #28 (confirmed v25): framework routes between providers (LiteLLM-style)
- **Pattern candidate #61 LLM-Client DI:** library provides DI slot for optional LLM features; user controls client choice

Both patterns serve multi-provider-ness but at different architectural layers:
- #28 = runtime-routing (framework chooses)
- **#61 = compile-time contract (user chooses at instantiation)**

### Why LLM features are optional

markitdown's **core value** is deterministic document structural conversion (headings, lists, tables). LLM features (image descriptions, OCR) are **enhancements**, not baseline. This makes DI + optional-feature pattern natural:

- Users wanting "just convert PDF to markdown" pay zero LLM cost
- Users wanting "PDF with image descriptions" opt in via client injection
- Users in airgapped environments can skip LLM features entirely

### Pattern #61 promotion criteria

N=1 currently (markitdown). Promote at 2+ libraries with `llm_client`-style DI for optional LLM features.

**Hypothesis:** pattern may generalize as LLM-feature-as-plugin-not-dependency design philosophy. Observe future corpus libraries.

## 3. Azure Document Intelligence integration

### Interface

**CLI:**
```bash
markitdown path.pdf -d -e "<az-doc-intel-endpoint>"
```

**Python:**
```python
md = MarkItDown(docintel_endpoint="<endpoint>")
```

### What Azure Document Intelligence provides

Azure Document Intelligence (formerly Form Recognizer) = Microsoft's paid OCR + layout-analysis API:
- Advanced OCR (better than open-source for complex docs)
- Table structure recognition
- Form field extraction
- Handwriting recognition
- Key-value pair extraction

### Why markitdown bridges to Azure DocIntel

**Use case:** when native markitdown PDF parsing is insufficient (complex layouts, forms, scanned documents), users can opt into Azure for higher-fidelity conversion.

**Architecture signal:** open-source Microsoft product provides optional bridge to commercial Microsoft service. Users can stay in OSS track OR pay for Azure upgrade.

### Pattern #31 Open-Core-adjacent — soft commercial-funnel

Not true Pattern #31 Open-Core (confirmed v24) because:
- markitdown has **no paid tier** in the library itself
- markitdown is **fully OSS** (MIT)
- Azure DocIntel is **optional external service**, not markitdown's commercial layer

But **soft commercial funnel** exists:
- User tries markitdown baseline → works well for simple docs
- User hits complex PDFs → documentation points to Azure DocIntel option
- User subscribes to Azure → continues using markitdown as wrapper

**Distinct from:**
- Pattern #31 Open-Core (fish-speech 39 AI INC commercial tier)
- Pattern #50 Commercial-Funnel (awesome-design-md → getdesign.md — explicit companion)
- Pattern #45 Dual-License (Unsloth Apache + AGPL UI)

**New candidate observation (not yet candidate #):** Passive ecosystem-funnel via optional-integration-only. Too speculative for candidate status at v28. Track in future Microsoft/Google corpus entries.

## 4. Narrowed-scope API hierarchy (security-motivated)

### API hierarchy (narrowest → broadest)

| Method | Scope | Network | Filesystem | Streams |
|--------|-------|---------|-----------|---------|
| `convert_stream(stream)` | Narrowest | ❌ | ❌ | ✅ user-provided |
| `convert_response(response)` | Narrow | ❌ (user pre-fetches) | ❌ | ✅ from response |
| `convert_local(path)` | Local only | ❌ | ✅ local files | ❌ |
| `convert(input)` | **Permissive** | ✅ remote URIs | ✅ local files | ✅ streams |

### Security rationale (README verbatim)

> *"MarkItDown's `convert()` method is intentionally permissive and can handle local files, remote URIs, and byte streams. If your application only needs to read local files, call `convert_local()` instead. If you need more control over URI fetching, call `requests.get()` yourself and pass the response object to `convert_response()`. For maximum control, open a stream to the input you want converted and call `convert_stream()`."*

### Threat model addressed

**Process-privilege I/O risk:** markitdown runs at calling-process privilege. If user passes untrusted URI to `convert()`, library could:
- Fetch from private network endpoints (SSRF risk)
- Access cloud metadata service (169.254.169.254)
- Read arbitrary local files if path controlled

**Mitigation via API narrowing:**
- Server-side app reading only uploaded files → use `convert_local()` — eliminates network surface
- Server-side app fetching URIs → use `convert_response()` — user controls `requests.get()` with allowlist/timeout/size-limit
- Streaming from pre-validated source → use `convert_stream()` — minimum surface

### Why this is architecturally unusual

**Most libraries offer single permissive API:** `convert(anything)` with internal dispatch. Simple DX, higher security risk in untrusted environments.

**markitdown offers opt-in-narrowness:** each narrower method is more verbose but safer. User **must** pick scope explicitly.

**Principle:** *"Call only the conversion method you need"* — least-privilege-API-design.

### Corpus observation

**Novel design pattern in Storm Bear corpus.** Prior corpus libraries (notebooklm-py v7, graphify v16) have single permissive API.

Potential future candidate (not registered at v28 — single observation): "Least-Privilege-API-Design Pattern." Observe if recurring.

## 5. Security considerations section significance

### README section structure

markitdown's `## Security Considerations` section is **400+ words**, separate from install/usage. Explicit security posture.

### Corpus comparison

| Framework | Dedicated security section | SECURITY.md | Pattern #24 |
|-----------|----------------------------|-------------|-------------|
| graphify v16 | No | **Yes** (first-party) | Contributes |
| spec-kit v17 | Implicit | Yes (6-file corporate) | Contributes |
| agency-agents v18 | No | Yes | Contributes |
| OMC v27 | Implicit | Yes | Contributes |
| **markitdown v28** | **Yes (explicit README section)** | **Yes (inferred)** | **Contributes + exemplar** |

markitdown has **both** SECURITY.md (inferred from Microsoft corporate standard) AND explicit README section. Stronger posture than most corpus.

### Corporate governance signal

Microsoft AutoGen Team security awareness high:
- Warning callout at README top
- Dedicated section
- Narrowed-scope API as structural mitigation
- CLA process (legal governance)

**Pattern #12 Governance-Depth reinforced** — Microsoft corporate security posture exemplary.

## 6. Composition: 3 patterns work together

markitdown's three architectural patterns compose:

### (a) LLM-client DI — enables optional vision without forcing dependency

User who doesn't want LLM features: doesn't install `openai`, doesn't pass `llm_client`. Library works.

User who wants LLM features: installs preferred client, passes it in.

### (b) Azure DocIntel bridge — enables Microsoft ecosystem upgrade path

Users hitting conversion quality ceiling can upgrade to Azure without leaving markitdown.

### (c) Narrowed-scope APIs — enables security-aware server-side deployment

Server-side apps can pick narrowest API for minimum attack surface.

### Composition result

markitdown is **flexible library** serving:
- Individual user: `pip install 'markitdown[all]'` + `markitdown file.pdf` — works
- LLM-enhanced user: + `llm_client` DI — better
- Enterprise user: + Azure DocIntel — enterprise-grade
- Security-conscious deploy: use `convert_stream()` — minimum surface

**Matches corporate-library design philosophy** — flexibility without forcing complexity on basic users.

## 7. LangChain integration (topic tag signal)

**README doesn't elaborate** on LangChain integration, but `langchain` topic tag suggests:
- markitdown works as LangChain document loader
- Community likely wraps markitdown in LangChain's document-loader interface

**Corpus observation:** framework-agnostic design (OpenAI-compatible + works in LangChain + AutoGen extension) = multi-framework applicability via clean interfaces. Matches Pattern #28 Multi-Provider AI Support philosophy at usage layer.

## 8. LLM-model as string (decoupled from SDK)

Example: `llm_model="gpt-4o"` — model is just a string, not an SDK constant.

**Implication:** user provides string; library passes through to their chosen `llm_client`. No hard-coded model list. Works with:
- OpenAI: `gpt-4o`, `gpt-4-turbo`, `gpt-4o-mini`
- Azure OpenAI: deployment name
- Anthropic via compatible shim
- Local via Ollama OpenAI-compatible mode
- Any OpenAI-compatible endpoint

**Contract-based not enum-based.**

## 9. `llm_prompt` customization

Optional custom prompt for image descriptions:
```python
md = MarkItDown(llm_client=client, llm_model="gpt-4o", llm_prompt="Describe the image focusing on data visualizations and text content.")
```

**Use case:** user tailors image description style (technical / human-friendly / specific-domain).

**Design insight:** library exposes prompt-level customization without hiding it. User retains control.

## 10. Error handling philosophy

README doesn't document extensively, but examples show:
- Plugin loads silently skip if no `llm_client`
- `convert()` errors propagate (standard Python exceptions)
- Docker path: piped failure exits with code

**Minimal-wrapping philosophy** — library doesn't hide errors or provide wrapped exception types. Standard Python idioms.

## 11. Testing infrastructure (hatch)

README mentions:
```bash
pip install hatch
hatch shell
hatch test
```

**Hatch** = Python-packaging + testing tool (Astral-era Python tooling). Used alongside `uv`.

**Pattern observation:** corporate Microsoft tool uses hatch (not tox/poetry) — cutting-edge Python ecosystem adoption.

## 12. Cross-wiki signals

- **Pattern candidate #61 LLM-Client DI Pattern** — new candidate at v28, N=1
- **Pattern #28 Multi-Provider AI Support 4th data point** (markitdown supports via `llm_client` DI + Azure DocIntel)
- **Pattern #31 Open-Core-adjacent** — Azure DocIntel soft commercial-funnel
- **Pattern #12 Governance-Depth** reinforced — Microsoft explicit security section + CLA + Code of Conduct
- **Pattern #24 SECURITY.md** — probable full compliance (README section + file)
- **Corporate-quality architectural patterns** — narrowed-scope API novel in corpus

## 13. Edges + limitations

- **LLM features limited to pptx + images** — not applied to full text content (would 10× token cost)
- **LLM-client interface coupling to OpenAI-compatible** — if Anthropic-native SDK users, need adapter
- **Azure DocIntel cost opacity** — README doesn't document Azure pricing (users must research)
- **Security section could be longer** — 400 words is good but SSRF-specific threats not fully enumerated
- **Narrowed-scope API discoverability** — users land on `convert()` first; may not read security section
- **LLM-prompt optimization burden on user** — default prompt may not suit all domains

---

**Cluster signal:** markitdown's 3 architectural patterns (LLM-client DI + Azure bridge + narrowed-scope APIs) compose into corporate-grade library architecture. Pattern candidate #61 (LLM-Client DI) registered. Soft ecosystem-funnel to Azure DocIntel observed as Pattern #31-adjacent. Security-motivated design more explicit than corpus peers.
