# (C) Cluster 1 — README + positioning + ML-classifier scope

> **Sources ingested:** root `README.md` (287 lines) + `python/README.md` (227 lines) + `js/README.md` (149 lines) + `docs/concepts.md` + `docs/js.md` + `assets/models/CHANGELOG.md`
> **Date:** 2026-04-24

## 1. Product positioning (verbatim)

**Tagline:** "Magika is a novel AI-powered file type detection tool that relies on the recent advance of deep learning to provide accurate detection."

**Headline differentiation:**
- Deep-learning model weighs **"about a few MBs"**
- Trained on **"~100M samples across 200+ content types"** (standard_v3_3 model enumerates **216 content types**)
- **~99% average accuracy** on test set
- **~5ms inference time on single CPU** (standard model); **~2ms** for v3_3 optimized
- Near-constant inference regardless of file size (uses limited subset of content)

**Deployment-scale claim (verbatim):**
> "Magika is used at scale to help improve Google users' safety by routing Gmail, Drive, and Safe Browsing files to the proper security and content policy scanners, processing hundreds billions samples on a weekly basis."

**Non-Google integrations:** VirusTotal + abuse.ch (Bazaar malware consortium).

**Disclaimer (verbatim):** "This project is not an official Google project. It is not supported by Google and Google specifically disclaims all warranties as to its quality, merchantability, or fitness for a particular purpose."

This "not an official Google project" framing is corpus-first — contrast with `googleworkspace/cli` (gws v13) which is explicitly official. Magika is Google-authored-but-unofficial — a Google-Research-OSS archetype.

## 2. Technical architecture (from README + concepts)

- **Model format:** ONNX (`model.onnx` ~3.0 MB in standard_v3_3)
- **Model input:** limited file-content subset (not full file)
- **Prediction modes (3):** `high-confidence` / `medium-confidence` / `best-guess`
- **Per-content-type thresholds:** each content type has its own trust threshold; sub-threshold falls back to generic labels ("Generic text document", "Unknown binary data")
- **Output:** both `dl` (deep-learning direct output) and `output` (post-threshold label; same as `dl` if above threshold, generic fallback if below)
- **Label group taxonomy:** code / document / text / image / audio / video / archive / inode / etc.

## 3. Nine model-version evolution (from `assets/models/CHANGELOG.md`)

| Version | Date | Content types | Avg accuracy | Inference speed | Notes |
|---------|------|---------------|--------------|-----------------|-------|
| standard_v1 | early | ~100 | 99%+ | ~2.6ms | Initial release |
| fast_v2_1 | mid | 200+ | ~98.5% | ~1.5ms | 4× faster than standard_v2_1 |
| standard_v2_1 | mid | 200+ | ~99% | ~6.2ms | 2× content types vs v1 |
| standard_v3_0 | late | 216 | ~99% | ~2ms | 3× faster than v2_1 |
| standard_v3_1 | late | 216 | ~99% | ~2ms | Better short-text + JS robustness |
| standard_v3_2 | 2025-03-17 | 216 | ~99% | ~2ms | CSV regression fix |
| **standard_v3_3** | **2025-04-11** | **216** | **~99%** | **~2ms** | **JS/TS balance; UTF-8 non-ASCII; latest** |
| begonly_v2_1 | — | — | — | — | Beginning-only variant |

**Velocity observation:** 7 model iterations over ~2 years; 2ms inference locked in at v3_0+; v3_3 2025-04-11 only 1 month before v44 wiki date = actively-maintained research model.

## 4. 216 content types (citation-not-replication)

Full enumeration in `assets/models/standard_v3_3/README.md` (16.1 KB). Key groups:
- **code** (Python, JavaScript, TypeScript, Rust, Go, Java, C, C++, Ruby, etc. + shell variants)
- **document** (Word, Excel, PowerPoint, PDF, EPUB, etc.)
- **text** (plain, CSV, TSV, INI, XML, markdown, LaTeX, email RFC 822)
- **image** (JPEG, PNG, GIF, SVG, WebP, TIFF, BMP, HEIC, etc.)
- **audio** (MP3, FLAC, WAV, OGG, AAC, etc.)
- **video** (MP4, WebM, AVI, MOV, etc.)
- **archive** (ZIP, TAR, GZIP, BZIP2, 7-Zip, RAR, etc.)
- **inode** (Empty file, Symlink, etc.)
- **executable** (ELF, PE, Mach-O, etc.)

## 5. 22 CLI options + 3 invocation modes

From `magika --help`:
- 22 CLI options total (see README lines 162-222)
- Core flags: `-r` recursive / `--no-dereference` / `--colors` / `--no-colors` / `-s` score / `-i` MIME type / `-l` label / `--json` / `--jsonl` / `--format <CUSTOM>` with 9 placeholders (`%p %l %d %g %m %e %s %S %b %%`)
- Invocation modes: (a) paths as args / (b) recursive directory scan / (c) stdin with dash `-`

## 6. 3 Python API methods

```python
from magika import Magika
m = Magika()
# Method 1: from bytes
res = m.identify_bytes(b'some content')
# Method 2: from path
res = m.identify_path('./file.ini')
# Method 3: from stream
with open('./file.ini', 'rb') as f:
    res = m.identify_stream(f)
print(res.output.label)  # => "ini", "python", "javascript", etc.
```

## 7. JavaScript/TypeScript bindings (MagikaJS)

- **Node usage:** `import { MagikaNode as Magika } from "magika/node";`
- **Browser usage:** `import { Magika } from "magika";` (uses TensorflowJS + WASM model)
- **CLI (less featureful):** `magika-js <paths>` — only via npm install; "please use the official CLI (pip install magika) for batch/recursive"
- **Model loading:** URL or local path — flexibility for server-side vs browser contexts

## 8. Legal / governance (from README)

- **License:** Apache-2.0
- **Security contact:** `magika-dev@google.com` (direct email, not github security advisory)
- **CLA required:** Google CLA via `cla.developers.google.com`
- **Code of Conduct:** Google's Open Source Community Guidelines

## 9. 12 authors (from CITATION.cff)

```
Yanick Fratantonio, Luca Invernizzi, Loua Farah, Kurt Thomas,
Marina Zhang, Ange Albertini, Francois Galilee, Giancarlo Metitieri,
Julien Cretin, Alexandre Petit-Bianco, David Tao, Elie Bursztein
```

**Elie Bursztein** (last author by convention = senior author) is prominent Google security researcher — leads Google's Anti-Abuse Research team. Yanick Fratantonio (first author) is the primary research + engineering lead.

## 10. Paper lineage

- **arXiv:** [2409.13768](https://arxiv.org/abs/2409.13768) — "Magika: AI-Powered Content-Type Detection"
- **ICSE 2025** — IEEE/ACM International Conference on Software Engineering — accepted April 2025
- **Paper PDF:** Bundled in repo `assets/2025_icse_magika.pdf` (943 KB — CORPUS-FIRST in-repo paper PDF bundling)

## 11. Verbatim citation (BibTeX)

```bibtex
@InProceedings{fratantonio25:magika,
  author = {Yanick Fratantonio and Luca Invernizzi and Loua Farah and Kurt Thomas and Marina Zhang and Ange Albertini and Francois Galilee and Giancarlo Metitieri and Julien Cretin and Alexandre Petit-Bianco and David Tao and Elie Bursztein},
  title = {{Magika: AI-Powered Content-Type Detection}},
  booktitle = {Proceedings of the International Conference on Software Engineering (ICSE)},
  month = {April},
  year = {2025}
}
```

## 12. Pattern Library observations (Phase 2 per cluster)

1. **Pattern #42 Academic-Published Peer-Reviewed Framework** — ICSE 2025 is **3rd venue class** after ACL 2024 (LlamaFactory v22) + ICLR 2025 (OpenHands v30). Strengthens pattern with software-engineering-conference-class diversity.
2. **Pattern #44 Academic-Lab Affiliation Archetype** — Google Research **corporate-research-lab** as **4th sub-variant 44d** (distinct from 44a-c academic-university variants Lab4AI / UIUC+CMU / HKU+SJTU+NUS+Huawei).
3. **In-repo paper PDF** (`assets/2025_icse_magika.pdf`) — corpus-first observational within #42.
4. **CITATION.cff** — corpus-first Citation File Format — within #42 academic-citation-discipline observation.
5. **"Not an official Google project" disclaimer** — NEW observation: Google-Research-OSS archetype distinct from Google-corporate-official (gws v13). Observational; does NOT warrant new candidate (consolidation-forward discipline).

## 13. Absences (informative)

- **No AGENTS.md** — consistent with outside-scope academic/ML tools (LlamaFactory v22, fish-speech v20, Unsloth v23 all absent)
- **No CLAUDE.md** — not agent-targeted
- **No methodology or SDD/BMM/TDD-style prescriptive framework** — pure classifier library
- **No MCP integration** — not agent-scope
- **No multi-language i18n** (EN-only) — consistent with academic/security-research genre
- **No commercial tier / no open-core** — fully OSS; distinct from #31 Open-Core pattern (observational counter-evidence, not invalidation)

## 14. Corpus-first observations (from cluster 1)

1. **In-repo ICSE paper PDF** (`assets/2025_icse_magika.pdf`)
2. **CITATION.cff** (explicit Citation File Format)
3. **Per-content-type adaptive threshold system** (corpus-first classifier primitive)
4. **9-model-version changelog in single repo** (corpus-first ML-model-evolution-artifact)
5. **"Not an official Google project" disclaimer at Google-authored-project** (corpus-first Google-Research-OSS archetype distinct from Google-corporate-official)

## 15. Cross-references

- Pattern #42: lineage v22 LlamaFactory → v30 OpenHands → v44 magika (3-venue-class coverage)
- Pattern #17 variant 2: v6 + v28 + v34 + v13 gws + v44 magika = 5 data points (Google 2-entrant at variant 2)
- Pattern #44: sub-variant 44d corporate-research-lab NEW
- Pattern #2 Distribution Evolution: cluster 2 documents 6-channel distribution
- Outside-scope 8th sub-type ML-security-classifier: distinct from v8 / v20 / v21 / v22 / v23 / v25 / v31 / v37
