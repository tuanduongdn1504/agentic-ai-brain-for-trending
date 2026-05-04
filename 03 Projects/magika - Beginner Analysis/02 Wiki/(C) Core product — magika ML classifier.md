# (C) Entity 1 — Core product: magika ML classifier

> **Wiki #:** v44 | **Type:** Core product entity | **Format:** 13-section canonical

## 1. What is this entity?

Magika is a deep-learning-based file-type classifier: a custom ~3 MB ONNX model that, given a limited subset of file bytes, predicts which of **216 content types** the file belongs to — achieving ~99% average accuracy with ~2ms inference on a single CPU.

The classifier is exposed via a Rust CLI (primary interface), Python API, JavaScript/TypeScript library, and Go bindings. A WASM-compiled version runs fully client-side in the browser (Magika web demo).

## 2. Primary positioning (verbatim)

> "Magika is a novel AI-powered file type detection tool that relies on the recent advance of deep learning to provide accurate detection." — `README.md` line 15

## 3. Key architectural choices

### 3.1 Model inputs
- **Not the whole file** — magika uses a limited byte subset, giving it near-constant inference time regardless of file size
- **Binary + textual uniformly** — single model handles 216 content types across code, documents, text, images, audio, video, archives, inodes, executables
- **ONNX format** — cross-runtime compatibility (Python onnxruntime / Rust ort / TensorflowJS for browser)

### 3.2 Per-content-type threshold system
Each of 216 content types has its own empirically-tuned trust threshold. Model output below threshold falls back to generic labels:
- `Generic text document` (below-threshold textual content)
- `Unknown binary data` (below-threshold binary content)
- `Empty file`, `Symlink` (inode category)

This is a **corpus-first classifier primitive observation**: per-output threshold (instead of uniform confidence threshold) allows fine-grained calibration per content type.

### 3.3 Three prediction modes
| Mode | Behavior | Use case |
|------|----------|----------|
| `high-confidence` | Strict thresholds; generic fallbacks common | Security-critical routing (false-positives expensive) |
| `medium-confidence` | Balanced | General classification |
| `best-guess` | Lowest thresholds; returns best label even when uncertain | Informational; low-risk |

### 3.4 Output schema (JSON)
Each classification returns `dl` (deep-learning raw output) and `output` (post-threshold label). When overruled, `dl` differs from `output` and `%b` placeholder marks the override in custom format strings.

## 4. Nine model-version evolution

From `assets/models/CHANGELOG.md`:

| Version | Date | # Content types | Avg accuracy | Inference speed | Key change |
|---------|------|-----------------|--------------|-----------------|------------|
| standard_v1 | 2024-02 (original release) | ~100 | 99%+ | ~2.6ms | Initial |
| standard_v2_1 | 2024 mid | 200+ | ~99% | ~6.2ms | 2× content types |
| fast_v2_1 | 2024 mid | 200+ | ~98.5% | ~1.5ms | 4× faster; lower accuracy tradeoff |
| standard_v3_0 | 2024 late | 216 | ~99% | ~2ms | 3× faster than v2_1 |
| standard_v3_1 | 2024 late | 216 | ~99% | ~2ms | Short-text + JS robustness |
| standard_v3_2 | 2025-03-17 | 216 | ~99% | ~2ms | CSV regression fix |
| **standard_v3_3** | **2025-04-11** | **216** | **~99%** | **~2ms** | **JS/TS balance + UTF-8 non-ASCII; CURRENT** |
| begonly_v2_1 | — | — | — | — | Beginning-only variant |

**Observation:** 7 iterations over ~2 years shows active research-maintenance. v3_3 released only 1 month before v44 wiki date (2026-04-24) — sustained pace.

## 5. 22 CLI options + 3 invocation modes

From `magika --help`:

**Invocation modes:**
1. Positional paths: `magika file1.py file2.txt`
2. Recursive directory: `magika -r directory/`
3. Stdin with dash: `cat file.ini | magika -`

**Output formats:**
- Default: `path: Description (group)`
- `--json` / `--jsonl` structured
- `--format <CUSTOM>` with 9 placeholders (`%p %l %d %g %m %e %s %S %b %%`)
- `-s` prints score; `-i` MIME type; `-l` simple label

**Navigation flags:**
- `--no-dereference` — treat symlinks as symlinks (don't follow)
- `--colors` / `--no-colors` — override terminal color detection

## 6. Python API (3 methods)

```python
from magika import Magika
m = Magika()

# From bytes
res = m.identify_bytes(b'function log(msg) {console.log(msg);}')

# From path
res = m.identify_path('./file.ini')

# From stream
with open('./file.ini', 'rb') as f:
    res = m.identify_stream(f)

print(res.output.label)  # => "javascript", "ini", etc.
```

## 7. Distribution channels (covered in Entity 2)

See `(C) Distribution ecosystem + Pattern 2 strengthening.md`.

## 8. Deployment-scale signals

Magika is deployed at Google-infrastructure scale:
- **Gmail**: file-type-routing for attachment security scanners
- **Google Drive**: upload classification
- **Safe Browsing**: URL-associated file classification
- **Aggregate**: "hundreds billions samples on a weekly basis" (verbatim)

Third-party integrations:
- **VirusTotal** — classifier feed (malware research)
- **abuse.ch (Bazaar)** — malware consortium

This is **industrial-deployment-scale** — distinct from **community-viral-scale** (16.6K stars is medium by star-count metric). Within-Pattern-#27 observational sub-distinction.

## 9. Comparison to classical file typing

Traditional file-type detection (libmagic / `file(1)` Unix command) uses:
- Magic-byte signature database
- Heuristic-based text analysis
- File extension fallback

Magika's architectural innovation:
- **Deep-learning classifier** (not signature-based)
- **Unified treatment of binary + text** (single model)
- **Per-content-type threshold** (calibrated per output, not global)
- **Subset-input inference** (near-constant time)

From the README: "outperforming existing approaches -- especially on textual content types." (Textual content is where libmagic struggles most — many text formats share byte-level similarity.)

## 10. Novel primitive observations (corpus-first)

1. **Per-content-type adaptive threshold system** — corpus-first classifier primitive
2. **Limited-byte-subset inference for near-constant time** — corpus-first ML-classifier architectural choice
3. **9-model-version changelog bundled in single repo** — corpus-first ML-model-evolution-artifact
4. **In-repo ICSE 2025 paper PDF** (`assets/2025_icse_magika.pdf`) — corpus-first in-repo peer-reviewed paper
5. **216 content-type enumeration in model README** — corpus-first fine-grained classifier output catalog (not enumerated in this wiki; cite `assets/models/standard_v3_3/README.md`)

## 11. Cross-references

- **Cluster 1:** README + positioning + ML-classifier scope
- **Cluster 2:** 5-language multi-binding distribution
- **Cluster 3:** ICSE 2025 peer-review + 12 authors + governance
- **Entity 2:** Distribution ecosystem
- **Entity 3:** Pattern implications
- **Pattern #42:** Academic-Published Peer-Reviewed — 3rd data point ICSE 2025

## 12. Storm Bear relevance

**LOW-MEDIUM (observational primary):**
- Could be invoked by Scrum-coach agent for client-document-file-type-validation (e.g., client sends PPTX-as-ZIP; magika verifies it's actually a Word-wrapped-ZIP vs compressed-archive)
- Python API composes with markitdown v28 pipeline (`magika` to classify → `markitdown` to convert)
- Observational: demonstrates Google-Research-OSS archetype + peer-review-discipline + per-content-type threshold as design primitive

**NOT a direct pilot candidate** for Scrum-coach workflow (narrow utility; not conversational; not agent-scope).

## 13. Next action / open questions

- Run `pipx install magika && magika --help` to verify CLI primitives (1 minute)
- Review `assets/models/standard_v3_3/README.md` for full 216-content-type catalog if building file-type-validation workflow
- Cross-check ICSE 2025 paper (`assets/2025_icse_magika.pdf`) for per-content-type threshold methodology if adapting approach
- Consider magika as first-pass classifier in any document-intake pipeline (e.g., client Scrum Master uploads for coaching review)
