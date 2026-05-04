# (C) magika — Hướng dẫn cho người mới / Beginner Guide

> **Wiki #:** v44 | **Source:** https://github.com/google/magika | **Ngày / Date:** 2026-04-24
> **Target audience:** Storm Bear operator + anyone curious about ML-based file-type detection

---

## 1. Magika là gì? / What is Magika?

### 🇻🇳 Tiếng Việt

Magika là công cụ phát hiện kiểu file bằng AI, do nhóm **Google Research (Anti-Abuse team)** xây dựng. Thay vì dùng magic-bytes truyền thống (như lệnh `file` trên Unix), magika dùng một model deep learning nhỏ (~3 MB) đã được train trên **~100 triệu mẫu file** để nhận dạng **216 kiểu nội dung** khác nhau với độ chính xác trung bình **~99%** và tốc độ inference **~2ms trên CPU đơn**.

Google dùng magika ở quy mô công nghiệp: định tuyến file đính kèm Gmail, upload Drive, Safe Browsing scanner — tổng cộng **hàng trăm tỷ file mỗi tuần**. VirusTotal và abuse.ch cũng dùng magika trong nghiên cứu malware.

### 🇬🇧 English

Magika is an AI-based file-type detection tool built by **Google Research (Anti-Abuse team)**. Instead of classical magic-byte detection (like Unix `file` command), magika uses a small deep-learning model (~3 MB) trained on **~100M file samples** to classify **216 content types** with **~99% average accuracy** at **~2ms inference per file on a single CPU**.

Google deploys magika at industrial scale: routing Gmail attachments, Drive uploads, Safe Browsing scanner files — totaling **hundreds of billions of samples per week**. VirusTotal and abuse.ch also integrate magika for malware research.

---

## 2. Tín hiệu corpus-first / Corpus-first signals

| # | Quan sát / Observation |
|---|------------------------|
| 1 | **ICSE 2025 peer-reviewed** — đây là 3rd CS-conference-class sau ACL 2024 (LlamaFactory v22) + ICLR 2025 (OpenHands v30) |
| 2 | **Google Research corporate-research-lab archetype** — distinct from Google corporate-official (gws v13); Pattern #44 sub-variant 44d NEW |
| 3 | **In-repo paper PDF** (`assets/2025_icse_magika.pdf`) — corpus-first |
| 4 | **CITATION.cff explicit Citation File Format** — corpus-first |
| 5 | **5-language multi-binding** (Rust / Python / JS+WASM / Go / Rust crate) + **6 distribution channels** — corpus-maximum for Pattern #2 |
| 6 | **Python-wheel-embeds-Rust-binary hybrid + pure-Python fallback** — corpus-first hybrid distribution |
| 7 | **.gemini/config.yaml Gemini Code Assist** — corpus-first Gemini-tooling config |
| 8 | **OpenSSF Best Practices + CodeQL + Scorecard + Dependabot** 4-layer security stack |
| 9 | **9 model-version evolution bundled** (v1 → v3_3) — corpus-first ML-model-evolution artifact |
| 10 | **"Not an official Google project" disclaimer** — Google-Research-OSS archetype documentation |

---

## 3. Xếp tier trong Storm Bear corpus / Tier placement

**OUTSIDE-SCOPE — ML-security-classifier (8TH outside-scope sub-type)**

- Không phải agent framework
- Không mở rộng Claude Code hoặc agent platforms
- Không dùng TỪ agent làm primary framing (agent có thể invoke nó, nhưng primary use là Google infrastructure routing)
- ML model là core value, không phải peripheral
- Security-adjacent use case

**Distinct from 7 prior outside-scope sub-types:**
1. education-aggregator (v8)
2. foundation-model (v20)
3. prompt-leak-archive (v21)
4. training-infrastructure (v22 + v23)
5. design-template-aggregator (v25 → absorbed into #68 v31 mini-audit)
6. MCP-server-aggregator (v31 → absorbed into #68)
7. business-OS-as-product (v37 OT#74)
8. **ML-security-classifier (v44 magika)** — NEW

---

## 4. Cài đặt / Installation

### 🇻🇳 Các cách cài đặt (chọn 1)

**Cách 1 — pipx (khuyến nghị cho CLI):**
```bash
pipx install magika
```

**Cách 2 — brew (macOS / Linux):**
```bash
brew install magika
```

**Cách 3 — curl installer script (Unix):**
```bash
curl -LsSf https://securityresearch.google/magika/install.sh | sh
```

**Cách 4 — pip (cho Python dev):**
```bash
pip install magika
```

**Cách 5 — cargo (cho Rust dev):**
```bash
cargo install --locked magika-cli
```

**Cách 6 — npm (cho JS/TS):**
```bash
npm install magika
```

### 🇬🇧 Verify installation

```bash
magika --help
magika README.md
# => README.md: Markdown document (text)
```

---

## 5. Sử dụng cơ bản / Core usage pattern

### CLI (Rust binary — primary interface)

```bash
# Single file
magika file.py
# => file.py: Python source (code)

# Recursive directory
magika -r project/

# JSON output
magika ./file.py --json

# Stdin piping
cat file.ini | magika -
# => -: INI configuration file (text)

# MIME type instead of description
magika -i file.py
# => file.py: text/x-python

# Simple label only
magika -l file.py
# => file.py: python

# Custom format
magika --format "%p => %l (%S%%)" file.py
# => file.py => python (99.7%)
```

### Python API

```python
from magika import Magika
m = Magika()

# From bytes
res = m.identify_bytes(b'function log(msg) {console.log(msg);}')
print(res.output.label)  # => "javascript"

# From path
res = m.identify_path('./file.ini')
print(res.output.label)  # => "ini"

# From stream
with open('./file.ini', 'rb') as f:
    res = m.identify_stream(f)
print(res.output.label)  # => "ini"
```

### JavaScript/TypeScript (Node)

```javascript
import { readFile } from "fs/promises";
import { MagikaNode as Magika } from "magika/node";

const data = await readFile("some-file");
const magika = await Magika().create();
const prediction = await magika.identifyBytes(data);
console.log(prediction);
```

### JavaScript/TypeScript (Browser)

```javascript
import { Magika } from "magika";

const file = new File(["# Hello markdown"], "hello.md");
const fileBytes = new Uint8Array(await file.arrayBuffer());
const magika = await Magika.create();
const prediction = await magika.identifyBytes(fileBytes);
console.log(prediction);
```

Hoặc thử trực tiếp qua web demo: https://securityresearch.google/magika/demo/magika-demo/ (chạy fully trong browser, không cần server).

---

## 6. Khái niệm kiến trúc / Novel architectural concepts

### 6.1 Per-content-type adaptive threshold

Mỗi trong 216 content types có ngưỡng tin cậy riêng được tune empirically. Nếu model prediction dưới ngưỡng → fallback label generic:
- `Generic text document` (textual below threshold)
- `Unknown binary data` (binary below threshold)

→ **Corpus-first classifier primitive.** Cho phép calibration fine-grained per content type thay vì uniform global threshold.

### 6.2 Three prediction modes

| Mode | Use case |
|------|----------|
| `high-confidence` | Security-critical (false-positive expensive) |
| `medium-confidence` | General use |
| `best-guess` | Low-risk informational |

### 6.3 Limited-byte-subset inference

Model không đọc toàn bộ file — chỉ một subset. Kết quả: inference time **gần như constant**, không phụ thuộc file size. File 1 MB hay 10 GB đều ~2ms.

### 6.4 JSON output schema

```json
{
  "path": "./file.py",
  "result": {
    "status": "ok",
    "value": {
      "dl": { "description": "Python source", "label": "python", ... },
      "output": { ... },
      "score": 0.996
    }
  }
}
```

- `dl` = raw deep-learning output
- `output` = post-threshold label (= `dl` nếu trên threshold; generic fallback nếu dưới)

---

## 7. So sánh với corpus Storm Bear / vs other corpus frameworks

| # | Aspect | magika v44 | gws v13 (Google T4) | LlamaFactory v22 (outside-scope training) |
|---|--------|-----------|---------------------|-------------------------------------------|
| 1 | Organizational archetype | Google-Research-OSS (corporate-research-lab fully-OSS) | Google corporate-official product | Academic-lab (Lab4AI) |
| 2 | Peer-review | ICSE 2025 (SE A*) | No (official product doc) | ACL 2024 (NLP A*) |
| 3 | License | Apache-2.0 | Apache-2.0 | Apache-2.0 |
| 4 | Commercial tier | NONE (pure OSS) | NONE (official product; Google services behind) | NONE (pure OSS) |
| 5 | Primary user | Google infrastructure (Gmail/Drive/Safe Browsing) | Google Workspace API users | ML researchers fine-tuning |
| 6 | Distribution channels | 6+ (corpus-max) | 5+ | pip + Docker |
| 7 | Storm Bear pilot rank | LOW-MEDIUM observational | HIGH (VN enterprise Google ubiquity) | LOW-MEDIUM observational |
| 8 | Primary language | Rust + Python + TS + Go | Rust | Python |

---

## 8. Khung quan điểm / Ethical framing

Không có ⚠️ warning cần thiết cho magika:
- ✅ Apache-2.0 — commercial-friendly
- ✅ "Not an official Google project" — rõ ràng về scope và warranty
- ✅ Peer-reviewed ICSE 2025 — legitimate academic work
- ✅ Google Research team với 12 tác giả định danh — transparent authorship
- ✅ No perverse-incentive (không commercial tier nào)
- ✅ No supply-chain risk đáng kể (classifier library, không plugin system)
- ✅ Apache-2.0 model files — không có license ambiguity về training data

**Potential caveat:** adversarial file-type spoofing — magika là ML model, có thể bị fool bằng crafted inputs. Không dùng làm sole security barrier. Dùng như first-pass classifier + defense-in-depth.

---

## 9. Storm Bear relevance / Mức độ liên quan với Storm Bear

### 🇻🇳 LOW-MEDIUM (chủ yếu observational)

**LOW direct pilot:**
- Narrow utility (chỉ file-type detection)
- Không conversational (CLI/API only)
- Không phải agent framework
- Không có VN use case

**MEDIUM potential compositions:**
- magika + markitdown v28 pipeline: classify trước, convert sau
- Client document intake validation (Scrum coach nhận file từ client, verify đúng format trước khi process)
- First-pass sanity check trong automation vault

**HIGH observational value:**
- Template cho Pattern #2 distribution multi-channel nếu Storm Bear publish OSS trong tương lai
- Reference cho Pattern #42 peer-review-discipline
- Google-Research-OSS archetype documentation
- ICSE 2025 paper làm methodological reference cho per-content-type-threshold design

### Pilot ranking update at v44

Magika KHÔNG vào top-11 pilot rankings. Vẫn giữ:
1. claude-hud v35 / 2. claude-howto v32 / 3. spec-kit v17 / 4. OMC v27 / 5. claude-code-best-practice v34 / 6. pi-mono v36 / 7. OpenHands v30 / 8. BMAD v11 / 9-11. markitdown v28 / crawl4ai v29 / awesome-mcp-servers v31

---

## 10. Evaluation roadmap / Lộ trình đánh giá (1 tuần — SHORT)

### Tuần 1 — test drive + composability pilot (1h total)

**Ngày 1 (15 phút):** Install + sanity check
```bash
pipx install magika
cd ~/path/to/any/project
magika -r . --json | jq -r '.[] | "\(.path): \(.result.value.output.label) (\(.result.value.score))"' | head -20
```

**Ngày 2 (15 phút):** Try web demo
- Visit https://securityresearch.google/magika/demo/magika-demo/
- Drop a few files; observe prediction + score
- Read `assets/models/standard_v3_3/README.md` (16 KB) for full 216-content-type catalog

**Ngày 3 (15 phút):** Python API in Scrum-coach workflow context
```python
from magika import Magika
m = Magika()

# Validate client upload
with open('/tmp/client-upload', 'rb') as f:
    res = m.identify_stream(f)

if res.output.label not in ['docx', 'pdf', 'pptx', 'xlsx']:
    print(f"Warning: expected Office/PDF, got {res.output.label}")
```

**Ngày 4-5 (30 phút):** Compose with markitdown v28 (if worthwhile)
```python
from magika import Magika
from markitdown import MarkItDown  # markitdown v28

m = Magika()
md = MarkItDown()

# File-type-aware ingestion
for upload in uploads:
    label = m.identify_path(upload).output.label
    if label in ['docx', 'pdf', 'pptx', 'xlsx', 'html']:
        converted = md.convert(upload)
        save_to_vault(converted)
    else:
        log_skip(upload, reason=f"non-convertible type: {label}")
```

**Decision point day 7:** Worth keeping in workflow? → likely NO for Storm Bear (client uploads are mostly Office/PDF; file-type validation low-value). Uninstall or keep for future opt-in.

---

## 11. Tradeoffs + limitations

**Strengths:**
- ~99% accuracy on 216 types (outperforms libmagic)
- 2ms inference (fast enough for any pipeline)
- Fully OSS (Apache-2.0; no commercial friction)
- Peer-reviewed (ICSE 2025 credibility)
- Multi-language bindings (Python / Rust / JS / Go WIP)
- Zero-commercial-tier (no upsell)

**Weaknesses / Caveats:**
- **Not a security barrier alone** — adversarial inputs can fool ML classifiers
- **Narrow utility** — file-type detection only, not broader analysis
- **216 types ≠ all types** — edge cases may return generic fallback
- **EN-only** — content-type descriptions in English only
- **Go bindings WIP** — not production-ready
- **Model files (~3 MB) bundled in pip install** — large wheel size vs classical `file`
- **"Not an official Google project"** — no Google support warranty

---

## 12. Caveats + safety notes

### Adversarial robustness
ML classifiers can be fooled by carefully crafted inputs. Don't rely on magika as sole security barrier. Use with defense-in-depth (antivirus + sandbox + multiple classifiers).

### Google deployment scale ≠ your scale
"Hundreds billions files weekly" is Google-internal Gmail/Drive/Safe Browsing scale. Your use will likely be much smaller (100s-1000s files). Both work, but scale-marketing is for security credibility, not performance claim for small-scale users.

### File extension ≠ ground truth
Magika classifies based on content, not filename extension. `.doc` might actually be PDF; `.py` might be shell. Magika gives you content-based answer, which can conflict with filename. Usually magika is right.

### Per-content-type threshold = opinionated
Google's empirically-tuned thresholds reflect their use-case priorities (security-routing). Your use case may differ. Use `--json` + `score` to see raw confidence if thresholds feel wrong.

---

## 13. References + next action

### References

- **Repo:** https://github.com/google/magika
- **Homepage:** https://securityresearch.google/magika/
- **Paper (ICSE 2025):** `assets/2025_icse_magika.pdf` in repo; or arXiv [2409.13768](https://arxiv.org/abs/2409.13768)
- **OpenSSF Best Practices badge:** https://www.bestpractices.dev/en/projects/8706
- **Web demo:** https://securityresearch.google/magika/demo/magika-demo/
- **216 content types catalog:** `assets/models/standard_v3_3/README.md`
- **Google OSS blog announcement:** https://opensource.googleblog.com/2024/02/magika-ai-powered-fast-and-efficient-file-type-identification.html

### Storm Bear cross-references

- Wiki index: `02 Wiki/(C) index.md`
- Cluster 1: README + positioning
- Cluster 2: Multi-binding distribution
- Cluster 3: Research credentials + governance
- Pattern implications: Entity 3

### Next action (recommended)

- **If you have 5 minutes:** `pipx install magika && magika -r . | head -20` to see it in action
- **If you have 30 minutes:** read ICSE 2025 paper section on per-content-type-threshold design (methodological interest)
- **If you have 1 hour:** wire magika + markitdown v28 composition into Scrum-doc-intake pipeline prototype
- **If you have no time:** file this wiki as corpus reference; use magika LATER when file-type-validation pain appears in actual workflow

---

> **Wiki v44 summary:** magika = Google Research ML file-type classifier at Google-infrastructure-scale deployment. Peer-reviewed (ICSE 2025). Storm Bear pilot relevance LOW-MEDIUM observational. Pattern Library contributions: #42 N=3 / #17 variant 2 N=5 / #44 sub-variant 44d / #2 corpus-max / 0 new active candidates (8-consecutive streak extends v37-v44).
