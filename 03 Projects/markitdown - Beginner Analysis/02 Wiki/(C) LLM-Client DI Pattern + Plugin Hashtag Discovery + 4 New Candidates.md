# (C) LLM-Client DI Pattern + Plugin Hashtag Discovery + 4 New Candidates

> **Type:** Entity — architectural patterns + candidate registrations
> **Parent:** [[(C) index]]
> **Sources:** README Python API + plugin ecosystem + cross-pattern analysis
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

v28 markitdown introduces **4 new pattern candidates** (#60-63) + **validates 1 confirmed-pattern variant at N=2** (Pattern #17 variant 5). This entity consolidates the architectural candidates (#61 LLM-Client DI + #62 Hashtag Plugin Discovery + #63 Format-Scoped Optional Dependencies) + ecosystem candidate (#60 AutoGen-Extension Archetype).

## 2. Pattern candidate #60 — AutoGen-Extension Ecosystem Archetype

### Already detailed in v28 entity "Microsoft AutoGen Team + Pattern 17 Variant 5 Validation"

**Summary here:**
- Sub-pattern of Pattern #17 variant 5 (ecosystem-scale commercial platform)
- Microsoft AutoGen Team = sub-ecosystem within Microsoft
- markitdown = official extension of AutoGen
- N=1 at v28; promote at 2+ similar sub-ecosystem structures

## 3. Pattern candidate #61 — LLM-Client DI Pattern

### Formal definition

> **#61 LLM-Client DI Pattern (NEW v28, N=1).** Library accepts `llm_client` as dependency-injected parameter for optional LLM features; contract-based integration uses duck-typed OpenAI-compatible interface. Core library does not hard-code SDK dependency; LLM features work only if client provided, otherwise silently skipped without breaking core functionality.

### Evidence

markitdown API:
```python
md = MarkItDown(
    llm_client=<OpenAI-compatible client>,
    llm_model="gpt-4o",
    llm_prompt="<optional>"
)
```

**Interface:** client must implement `.chat.completions.create(...)`.
**Fallback:** if `llm_client=None`, LLM features silently skipped, core conversion works.

### Distinct from Pattern #28 Multi-Provider AI Support (confirmed v25)

| Dimension | Pattern #28 | Pattern #61 |
|-----------|-------------|-------------|
| **Scope** | Framework routes between providers | Library accepts user-provided client |
| **Layer** | Runtime routing | Compile-time DI contract |
| **Who chooses provider** | Framework (via config) | User (at instantiation) |
| **Pluggability target** | Multiple providers usable interchangeably | Optional feature enabled via client injection |
| **Example** | LiteLLM routing in TrendRadar v19 | `MarkItDown(llm_client=...)` |

**Both patterns enable multi-provider-ness but at different architectural layers.**

### Why this is novel

Typical library design hard-codes SDK:
```python
# ❌ Hard-coded
import openai
class SomeLib:
    def __init__(self):
        self.client = openai.OpenAI()
```

markitdown design:
```python
# ✅ DI-based
class MarkItDown:
    def __init__(self, llm_client=None, llm_model=None):
        self.llm_client = llm_client  # user-provided
        self.llm_model = llm_model
```

### Why it matters

1. **No forced dependency** — users who don't need LLM features don't install openai
2. **Provider choice user-side** — OpenAI / Azure OpenAI / LiteLLM / Anthropic-via-shim all work
3. **Silent skip** — feature unavailable doesn't break base functionality
4. **Airgapped-friendly** — no LLM client → still works for base formats

### Promotion criteria

N=1 at v28. Promote at 2+ libraries with:
- `llm_client`-style DI parameter
- Duck-typed contract (not hard SDK dep)
- Optional feature with graceful fallback

### Candidates for N=2

- **graphify v16** — has Claude vision integration; re-check if DI-pattern or hard-coded
- **TrendRadar v19** — LiteLLM abstraction; different pattern (routing vs DI)
- Future corpus library with similar contract

## 4. Pattern candidate #62 — Hashtag-Based Plugin Discovery

### Formal definition

> **#62 Hashtag-Based Plugin Discovery (NEW v28, N=1).** Framework enables plugin discovery via public-social-media hashtag (e.g., GitHub repo topics `#framework-plugin`) rather than centralized marketplace. Zero-infrastructure but zero-curation. Appropriate when plugin-quality-risk is low and plugins are narrow-scope extensions.

### Evidence

markitdown README §Plugins:
> *"To find available plugins, search GitHub for the hashtag `#markitdown-plugin`."*

**Commands:**
- `markitdown --list-plugins` — lists installed
- `markitdown --use-plugins path.pdf` — enables

### Contrast with marketplace patterns

| Framework | Mechanism | Pros | Cons |
|-----------|-----------|------|------|
| spec-kit v17 | 80+ marketplace | Curated, quality signals | Infrastructure burden |
| OMC v27 | Claude Code plugin marketplace native | Integrated, discoverable | Lock-in to marketplace |
| BMAD v11 | Community modules | Semi-centralized | Moderate infrastructure |
| **markitdown v28** | **`#markitdown-plugin` GitHub hashtag** | **Zero infrastructure** | **No quality/version signals** |

### Why pattern-worthy

**Lightweight alternative to marketplace** for narrow-extension libraries. Reduces maintainer burden at cost of curation.

### Promotion criteria

N=1 at v28. Promote at 2+ frameworks using hashtag-based plugin discovery.

### Candidates for N=2

- Python packaging ecosystem precedent (`pyproject.toml` entry points + PyPI classifiers)
- Future corpus library adopting hashtag convention

## 5. Pattern candidate #63 — Format-Scoped Optional Dependencies

### Formal definition

> **#63 Format-Scoped Optional Dependencies (NEW v28, N=1).** Library uses pip extras (`[format]`) to scope install size per-feature. `pip install 'library[pdf,docx]'` pulls format-specific deps; `[all]` installs everything. Reduces baseline install size, enables deployment environment flexibility.

### Evidence

markitdown README:
```bash
pip install 'markitdown[all]'              # everything
pip install 'markitdown[pdf,docx,pptx]'    # selective
pip install markitdown                      # base formats only
```

**Available extras:**
- `[all]`, `[pptx]`, `[docx]`, `[xlsx]`, `[xls]`, `[pdf]`, `[outlook]`, `[az-doc-intel]`, `[audio-transcription]`, `[youtube-transcription]`

### Why novel in corpus

- codymaster v12: 79 skills all-or-nothing
- LlamaFactory v22: various optional deps but for training backends, not formats
- Unsloth v23: optional backends but limited scope
- markitdown v28: **per-format scoping** novel

### Why pattern-worthy

- **Deployment flexibility** — Lambda size limits, Docker image size, airgapped environments
- **User choice** — install only needed formats
- **Python-ecosystem aligned** — pip extras are standard Python pattern

### Promotion criteria

N=1 at v28. Promote at 2+ Python corpus libraries with per-format (or per-feature-category) optional deps.

### Likelihood

**Medium** — Python ecosystem pattern may emerge in other corpus Python libraries. Training-infra (Unsloth, LlamaFactory) may have similar. Need specific verification.

## 6. Pattern #17 variant 5 — N=2 validation

Already detailed in entity "Microsoft AutoGen Team + Pattern 17 Variant 5 Validation."

### Summary for this entity

- Pattern #17 confirmed v15
- Variant 5 (ecosystem-scale commercial platform) registered at v26 with HuggingFace N=1
- v28 adds Microsoft → **N=2 structurally unambiguous**
- **Recommendation:** promote variant 5 from candidate-variant to confirmed-variant within Pattern #17

## 7. Candidate registration rationale

### Why 4 new candidates at v28

markitdown introduces unusually-high-density architectural novelty:
1. **Autogen-extension ecosystem structure** (org-level)
2. **LLM-client DI pattern** (library-architecture-level)
3. **Hashtag plugin discovery** (community-level)
4. **Format-scoped optional deps** (packaging-level)

Each operates at distinct architectural layer. Each is observably novel vs prior corpus.

### Candidate density comparison

| Wiki | New candidates | Pattern-density-per-wiki |
|------|----------------|--------------------------|
| v20 fish-speech | 5 (#31-35) | 5 |
| v22 LlamaFactory | 4 (#41-44) | 4 |
| v24 Skyvern | 2 (#47-48) | 2 |
| v25 awesome-design-md | 4 (#49-52) | 4 |
| v26 HF agents-course | 2 (#53-54) | 2 |
| v27 OMC | 5 (#55-59) | 5 |
| **v28 markitdown** | **4 (#60-63)** | **4** |

**Recent corpus average ~3.7 candidates per wiki.** markitdown at 4 is median density.

### Post-v28 Pattern Library state

- Confirmed: 27 (unchanged; Pattern #17 variant 5 promotion is within-pattern refinement not new confirmed)
- Active candidates: 25 + 4 new = **29** (crosses 28+ trigger threshold!)
- Stale: 3
- Retired: 4
- **Ratio:** 29:27 = **1.07:1 — AUDIT TRIGGER HIT (>1:1)**

**⚠️ v28 triggers next audit.** Both conditions (count ≥28 + ratio >1:1) crossed simultaneously — same as v27.

## 8. Cross-candidate relationships

### #60 AutoGen-Extension ⊂ Pattern #17 variant 5

Nested sub-pattern. May eventually absorb into variant 5 formal statement.

### #61 LLM-Client DI vs #28 Multi-Provider AI Support

Related but distinct (library-DI vs framework-routing). Audit should clarify boundary.

### #62 Hashtag Discovery vs #7 Marketplace Emergence

Opposite mechanisms for plugin discovery. Candidate #62 may become "marketplace alternative" sub-observation of #7 instead of standalone.

### #63 Format-Scoped Optional Deps

Standalone; no direct confirmed-pattern relationship at v28.

## 9. Comparison with OMC v27 candidate density

OMC v27 introduced 5 candidates (#55-59):
- Korean Regional Archetype T1
- Multi-Runtime Orchestration
- Recursive Corpus Reference
- Branding-Package Divergence
- Claude Code Plugin Marketplace Native

markitdown v28 introduces 4 candidates (#60-63):
- AutoGen-Extension Ecosystem
- LLM-Client DI Pattern
- Hashtag-Based Plugin Discovery
- Format-Scoped Optional Dependencies

**Combined v27+v28: 9 new candidates in 2 wikis.** Library hitting next audit trigger (post-v27 audit cleared at 0.93:1; v28 pushes to 1.07:1).

## 10. Routine v2 candidate-density observation

**Observation:** after v25 audit cleared backlog, subsequent wikis (v26, v27, v28) produced dense candidate registration:
- v26: 2 candidates
- v27: 5 candidates
- v28: 4 candidates

**Total: 11 candidates in 3 wikis.**

**Hypothesis:** corpus-maturity phase entering "pattern-discovery acceleration" — once broad tier coverage achieved (5/5 at v26), architectural novelty emerges per-wiki at higher rate because each wiki explores sub-archetype-specific structure.

**Action implication for v2.1 routine:** expect 3-5 candidates per wiki going forward; audit triggers reset faster; plan biannual full audit rhythm.

## 11. Related concepts

- [[(C) Cluster — AutoGen Team origin + Microsoft ecosystem + plugin discovery]]
- [[(C) Cluster — LLM-client DI + Azure Document Intelligence + security API narrowing]]
- [[(C) Microsoft AutoGen Team + Corporate Governance + Pattern 17 Variant 5 Validation]]
- [[(C) T4 Extends to N=5 + Storm Bear Vault Applicability + Meta]]
- Pattern #17 variant 5 (N=2 at v28)
- Pattern #28 Multi-Provider AI Support (distinct from #61)
- Pattern #7 Marketplace Emergence (#62 is alternative mechanism)
- Pattern candidates #60, #61, #62, #63

## 12. References

- PATTERN_LIBRARY.md post-v27 audit state
- markitdown README.md
- Cross-corpus pattern analysis (T4 + ecosystem-layer + multi-provider)

## 13. Edges + limitations

- **#60 AutoGen-Extension** may be sub-pattern of #17 variant 5 rather than standalone
- **#61 LLM-Client DI** boundary with #28 Multi-Provider may blur; audit should clarify
- **#62 Hashtag Discovery** has fundamental discoverability limitations; may remain N=1
- **#63 Format-Scoped Optional Deps** may be Python-ecosystem-specific, not agent-space
- **4 candidates at N=1** creates stale-flag load at v32 audit if no follow-on
- **Audit trigger hit at v28** requires consolidation before v29 (same pattern as v27)

---

**v28 markitdown registers 4 new pattern candidates (#60-63) + validates Pattern #17 variant 5 at N=2 (promotion-candidate). 4-candidate density is median for recent corpus wikis. Combined with v27's 5 candidates + v26's 2, post-audit-reset state rebuilds to audit trigger within 3 wikis.**
